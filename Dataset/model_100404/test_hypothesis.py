import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sgraph_Statement,
    sgraph_ScopedElement,
    sgraph_Scope,
    sgraph_ReactiveElement,
    ScopedElement,
    ReactiveElement,
    sgraph_Reaction,
    sgraph_ExpressionElement,
    sgraph_Effect,
    sgraph_Trigger,
    Reaction,
    ExpressionElement,
    Pseudostate,
    sgraph_Synchronization,
    sgraph_Exit,
    sgraph_Entry,
    sgraph_Choice,
    Declaration,
    sgraph_Event,
    sgraph_Variable,
    RegularState,
    sgraph_State,
    sgraph_FinalState,
    sgraph_NamedElement,
    sgraph_Transition,
    NamedElement,
    sgraph_Region,
    sgraph_Declaration,
    sgraph_Statechart,
    sgraph_Vertex,
    Vertex,
    sgraph_RegularState,
    sgraph_Pseudostate,
    EntryKind,
    ChoiceKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sgraph_statement_is_not_abstract():
    assert not inspect.isabstract(sgraph_Statement)


def test_sgraph_statement_constructor_exists():
    assert callable(sgraph_Statement.__init__)


def test_sgraph_statement_constructor_args():
    sig = inspect.signature(sgraph_Statement.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_scopedelement_is_not_abstract():
    assert not inspect.isabstract(sgraph_ScopedElement)


def test_sgraph_scopedelement_constructor_exists():
    assert callable(sgraph_ScopedElement.__init__)


def test_sgraph_scopedelement_constructor_args():
    sig = inspect.signature(sgraph_ScopedElement.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_sgraph_scopedelement_has_namespace():
    assert hasattr(sgraph_ScopedElement, "namespace")
    descriptor = None
    for klass in sgraph_ScopedElement.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_sgraph_scope_is_not_abstract():
    assert not inspect.isabstract(sgraph_Scope)


def test_sgraph_scope_constructor_exists():
    assert callable(sgraph_Scope.__init__)


def test_sgraph_scope_constructor_args():
    sig = inspect.signature(sgraph_Scope.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_reactiveelement_is_not_abstract():
    assert not inspect.isabstract(sgraph_ReactiveElement)


def test_sgraph_reactiveelement_constructor_exists():
    assert callable(sgraph_ReactiveElement.__init__)


def test_sgraph_reactiveelement_constructor_args():
    sig = inspect.signature(sgraph_ReactiveElement.__init__)
    params = list(sig.parameters.keys())



def test_scopedelement_is_not_abstract():
    assert not inspect.isabstract(ScopedElement)


def test_scopedelement_constructor_exists():
    assert callable(ScopedElement.__init__)


def test_scopedelement_constructor_args():
    sig = inspect.signature(ScopedElement.__init__)
    params = list(sig.parameters.keys())



def test_reactiveelement_is_not_abstract():
    assert not inspect.isabstract(ReactiveElement)


def test_reactiveelement_constructor_exists():
    assert callable(ReactiveElement.__init__)


def test_reactiveelement_constructor_args():
    sig = inspect.signature(ReactiveElement.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_reaction_is_not_abstract():
    assert not inspect.isabstract(sgraph_Reaction)


def test_sgraph_reaction_constructor_exists():
    assert callable(sgraph_Reaction.__init__)


def test_sgraph_reaction_constructor_args():
    sig = inspect.signature(sgraph_Reaction.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_expressionelement_is_not_abstract():
    assert not inspect.isabstract(sgraph_ExpressionElement)


def test_sgraph_expressionelement_constructor_exists():
    assert callable(sgraph_ExpressionElement.__init__)


def test_sgraph_expressionelement_constructor_args():
    sig = inspect.signature(sgraph_ExpressionElement.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_sgraph_expressionelement_has_expression():
    assert hasattr(sgraph_ExpressionElement, "expression")
    descriptor = None
    for klass in sgraph_ExpressionElement.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_sgraph_effect_is_not_abstract():
    assert not inspect.isabstract(sgraph_Effect)


def test_sgraph_effect_constructor_exists():
    assert callable(sgraph_Effect.__init__)


def test_sgraph_effect_constructor_args():
    sig = inspect.signature(sgraph_Effect.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_trigger_is_not_abstract():
    assert not inspect.isabstract(sgraph_Trigger)


def test_sgraph_trigger_constructor_exists():
    assert callable(sgraph_Trigger.__init__)


def test_sgraph_trigger_constructor_args():
    sig = inspect.signature(sgraph_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_reaction_is_not_abstract():
    assert not inspect.isabstract(Reaction)


def test_reaction_constructor_exists():
    assert callable(Reaction.__init__)


def test_reaction_constructor_args():
    sig = inspect.signature(Reaction.__init__)
    params = list(sig.parameters.keys())



def test_expressionelement_is_not_abstract():
    assert not inspect.isabstract(ExpressionElement)


def test_expressionelement_constructor_exists():
    assert callable(ExpressionElement.__init__)


def test_expressionelement_constructor_args():
    sig = inspect.signature(ExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_synchronization_is_not_abstract():
    assert not inspect.isabstract(sgraph_Synchronization)


def test_sgraph_synchronization_constructor_exists():
    assert callable(sgraph_Synchronization.__init__)


def test_sgraph_synchronization_constructor_args():
    sig = inspect.signature(sgraph_Synchronization.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_exit_is_not_abstract():
    assert not inspect.isabstract(sgraph_Exit)


def test_sgraph_exit_constructor_exists():
    assert callable(sgraph_Exit.__init__)


def test_sgraph_exit_constructor_args():
    sig = inspect.signature(sgraph_Exit.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_entry_is_not_abstract():
    assert not inspect.isabstract(sgraph_Entry)


def test_sgraph_entry_constructor_exists():
    assert callable(sgraph_Entry.__init__)


def test_sgraph_entry_constructor_args():
    sig = inspect.signature(sgraph_Entry.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_sgraph_entry_has_kind():
    assert hasattr(sgraph_Entry, "kind")
    descriptor = None
    for klass in sgraph_Entry.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_sgraph_choice_is_not_abstract():
    assert not inspect.isabstract(sgraph_Choice)


def test_sgraph_choice_constructor_exists():
    assert callable(sgraph_Choice.__init__)


def test_sgraph_choice_constructor_args():
    sig = inspect.signature(sgraph_Choice.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_sgraph_choice_has_kind():
    assert hasattr(sgraph_Choice, "kind")
    descriptor = None
    for klass in sgraph_Choice.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_event_is_not_abstract():
    assert not inspect.isabstract(sgraph_Event)


def test_sgraph_event_constructor_exists():
    assert callable(sgraph_Event.__init__)


def test_sgraph_event_constructor_args():
    sig = inspect.signature(sgraph_Event.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_variable_is_not_abstract():
    assert not inspect.isabstract(sgraph_Variable)


def test_sgraph_variable_constructor_exists():
    assert callable(sgraph_Variable.__init__)


def test_sgraph_variable_constructor_args():
    sig = inspect.signature(sgraph_Variable.__init__)
    params = list(sig.parameters.keys())



def test_regularstate_is_not_abstract():
    assert not inspect.isabstract(RegularState)


def test_regularstate_constructor_exists():
    assert callable(RegularState.__init__)


def test_regularstate_constructor_args():
    sig = inspect.signature(RegularState.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_state_is_not_abstract():
    assert not inspect.isabstract(sgraph_State)


def test_sgraph_state_constructor_exists():
    assert callable(sgraph_State.__init__)


def test_sgraph_state_constructor_args():
    sig = inspect.signature(sgraph_State.__init__)
    params = list(sig.parameters.keys())
    assert "composite" in params, "Missing parameter 'composite'"
    assert "orthogonal" in params, "Missing parameter 'orthogonal'"
    assert "submachine" in params, "Missing parameter 'submachine'"
    assert "leaf" in params, "Missing parameter 'leaf'"
    assert "simple" in params, "Missing parameter 'simple'"
    assert "substatechartId" in params, "Missing parameter 'substatechartId'"

def test_sgraph_state_has_composite():
    assert hasattr(sgraph_State, "composite")
    descriptor = None
    for klass in sgraph_State.__mro__:
        if "composite" in klass.__dict__:
            descriptor = klass.__dict__["composite"]
            break
    assert isinstance(descriptor, property)

def test_sgraph_state_has_orthogonal():
    assert hasattr(sgraph_State, "orthogonal")
    descriptor = None
    for klass in sgraph_State.__mro__:
        if "orthogonal" in klass.__dict__:
            descriptor = klass.__dict__["orthogonal"]
            break
    assert isinstance(descriptor, property)

def test_sgraph_state_has_submachine():
    assert hasattr(sgraph_State, "submachine")
    descriptor = None
    for klass in sgraph_State.__mro__:
        if "submachine" in klass.__dict__:
            descriptor = klass.__dict__["submachine"]
            break
    assert isinstance(descriptor, property)

def test_sgraph_state_has_leaf():
    assert hasattr(sgraph_State, "leaf")
    descriptor = None
    for klass in sgraph_State.__mro__:
        if "leaf" in klass.__dict__:
            descriptor = klass.__dict__["leaf"]
            break
    assert isinstance(descriptor, property)

def test_sgraph_state_has_simple():
    assert hasattr(sgraph_State, "simple")
    descriptor = None
    for klass in sgraph_State.__mro__:
        if "simple" in klass.__dict__:
            descriptor = klass.__dict__["simple"]
            break
    assert isinstance(descriptor, property)

def test_sgraph_state_has_substatechartId():
    assert hasattr(sgraph_State, "substatechartId")
    descriptor = None
    for klass in sgraph_State.__mro__:
        if "substatechartId" in klass.__dict__:
            descriptor = klass.__dict__["substatechartId"]
            break
    assert isinstance(descriptor, property)



def test_sgraph_finalstate_is_not_abstract():
    assert not inspect.isabstract(sgraph_FinalState)


def test_sgraph_finalstate_constructor_exists():
    assert callable(sgraph_FinalState.__init__)


def test_sgraph_finalstate_constructor_args():
    sig = inspect.signature(sgraph_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_namedelement_is_not_abstract():
    assert not inspect.isabstract(sgraph_NamedElement)


def test_sgraph_namedelement_constructor_exists():
    assert callable(sgraph_NamedElement.__init__)


def test_sgraph_namedelement_constructor_args():
    sig = inspect.signature(sgraph_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sgraph_namedelement_has_name():
    assert hasattr(sgraph_NamedElement, "name")
    descriptor = None
    for klass in sgraph_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sgraph_transition_is_not_abstract():
    assert not inspect.isabstract(sgraph_Transition)


def test_sgraph_transition_constructor_exists():
    assert callable(sgraph_Transition.__init__)


def test_sgraph_transition_constructor_args():
    sig = inspect.signature(sgraph_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_sgraph_transition_has_priority():
    assert hasattr(sgraph_Transition, "priority")
    descriptor = None
    for klass in sgraph_Transition.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_region_is_not_abstract():
    assert not inspect.isabstract(sgraph_Region)


def test_sgraph_region_constructor_exists():
    assert callable(sgraph_Region.__init__)


def test_sgraph_region_constructor_args():
    sig = inspect.signature(sgraph_Region.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_sgraph_region_has_priority():
    assert hasattr(sgraph_Region, "priority")
    descriptor = None
    for klass in sgraph_Region.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_sgraph_declaration_is_not_abstract():
    assert not inspect.isabstract(sgraph_Declaration)


def test_sgraph_declaration_constructor_exists():
    assert callable(sgraph_Declaration.__init__)


def test_sgraph_declaration_constructor_args():
    sig = inspect.signature(sgraph_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_statechart_is_not_abstract():
    assert not inspect.isabstract(sgraph_Statechart)


def test_sgraph_statechart_constructor_exists():
    assert callable(sgraph_Statechart.__init__)


def test_sgraph_statechart_constructor_args():
    sig = inspect.signature(sgraph_Statechart.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_vertex_is_not_abstract():
    assert not inspect.isabstract(sgraph_Vertex)


def test_sgraph_vertex_constructor_exists():
    assert callable(sgraph_Vertex.__init__)


def test_sgraph_vertex_constructor_args():
    sig = inspect.signature(sgraph_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_regularstate_is_not_abstract():
    assert not inspect.isabstract(sgraph_RegularState)


def test_sgraph_regularstate_constructor_exists():
    assert callable(sgraph_RegularState.__init__)


def test_sgraph_regularstate_constructor_args():
    sig = inspect.signature(sgraph_RegularState.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_pseudostate_is_not_abstract():
    assert not inspect.isabstract(sgraph_Pseudostate)


def test_sgraph_pseudostate_constructor_exists():
    assert callable(sgraph_Pseudostate.__init__)


def test_sgraph_pseudostate_constructor_args():
    sig = inspect.signature(sgraph_Pseudostate.__init__)
    params = list(sig.parameters.keys())

def test_entrykind_exists():
    # Check that the Enumeration exists
    assert EntryKind is not None

def test_entrykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntryKind]
    expected_literals = [
        "initial",
        "deepHistory",
        "shallowHistory",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntryKind"

def test_choicekind_exists():
    # Check that the Enumeration exists
    assert ChoiceKind is not None

def test_choicekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ChoiceKind]
    expected_literals = [
        "dynamic",
        "static",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ChoiceKind"


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
sgraph_Statement_strategy = st.builds(
    sgraph_Statement,
)
sgraph_ScopedElement_strategy = st.builds(
    sgraph_ScopedElement,
    namespace=
        safe_text
)
sgraph_Scope_strategy = st.builds(
    sgraph_Scope,
)
sgraph_ReactiveElement_strategy = st.builds(
    sgraph_ReactiveElement,
)
ScopedElement_strategy = st.builds(
    ScopedElement,
)
ReactiveElement_strategy = st.builds(
    ReactiveElement,
)
sgraph_Reaction_strategy = st.builds(
    sgraph_Reaction,
)
sgraph_ExpressionElement_strategy = st.builds(
    sgraph_ExpressionElement,
    expression=
        safe_text
)
sgraph_Effect_strategy = st.builds(
    sgraph_Effect,
)
sgraph_Trigger_strategy = st.builds(
    sgraph_Trigger,
)
Reaction_strategy = st.builds(
    Reaction,
)
ExpressionElement_strategy = st.builds(
    ExpressionElement,
)
Pseudostate_strategy = st.builds(
    Pseudostate,
)
sgraph_Synchronization_strategy = st.builds(
    sgraph_Synchronization,
)
sgraph_Exit_strategy = st.builds(
    sgraph_Exit,
)
sgraph_Entry_strategy = st.builds(
    sgraph_Entry,
    kind=
        safe_text
)
sgraph_Choice_strategy = st.builds(
    sgraph_Choice,
    kind=
        safe_text
)
Declaration_strategy = st.builds(
    Declaration,
)
sgraph_Event_strategy = st.builds(
    sgraph_Event,
)
sgraph_Variable_strategy = st.builds(
    sgraph_Variable,
)
RegularState_strategy = st.builds(
    RegularState,
)
sgraph_State_strategy = st.builds(
    sgraph_State,
    composite=
        st.booleans(),
    orthogonal=
        st.booleans(),
    submachine=
        st.booleans(),
    leaf=
        st.booleans(),
    simple=
        st.booleans(),
    substatechartId=
        safe_text
)
sgraph_FinalState_strategy = st.builds(
    sgraph_FinalState,
)
sgraph_NamedElement_strategy = st.builds(
    sgraph_NamedElement,
    name=
        safe_text
)
sgraph_Transition_strategy = st.builds(
    sgraph_Transition,
    priority=
        st.integers()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
sgraph_Region_strategy = st.builds(
    sgraph_Region,
    priority=
        st.integers()
)
sgraph_Declaration_strategy = st.builds(
    sgraph_Declaration,
)
sgraph_Statechart_strategy = st.builds(
    sgraph_Statechart,
)
sgraph_Vertex_strategy = st.builds(
    sgraph_Vertex,
)
Vertex_strategy = st.builds(
    Vertex,
)
sgraph_RegularState_strategy = st.builds(
    sgraph_RegularState,
)
sgraph_Pseudostate_strategy = st.builds(
    sgraph_Pseudostate,
)

@given(instance=sgraph_Statement_strategy)
@settings(max_examples=50)
def test_sgraph_statement_instantiation(instance):
    assert isinstance(instance, sgraph_Statement)

@given(instance=sgraph_ScopedElement_strategy)
@settings(max_examples=50)
def test_sgraph_scopedelement_instantiation(instance):
    assert isinstance(instance, sgraph_ScopedElement)



@given(instance=sgraph_ScopedElement_strategy)
def test_sgraph_scopedelement_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=sgraph_Scope_strategy)
@settings(max_examples=50)
def test_sgraph_scope_instantiation(instance):
    assert isinstance(instance, sgraph_Scope)

@given(instance=sgraph_ReactiveElement_strategy)
@settings(max_examples=50)
def test_sgraph_reactiveelement_instantiation(instance):
    assert isinstance(instance, sgraph_ReactiveElement)

@given(instance=ScopedElement_strategy)
@settings(max_examples=50)
def test_scopedelement_instantiation(instance):
    assert isinstance(instance, ScopedElement)

@given(instance=ReactiveElement_strategy)
@settings(max_examples=50)
def test_reactiveelement_instantiation(instance):
    assert isinstance(instance, ReactiveElement)

@given(instance=sgraph_Reaction_strategy)
@settings(max_examples=50)
def test_sgraph_reaction_instantiation(instance):
    assert isinstance(instance, sgraph_Reaction)

@given(instance=sgraph_ExpressionElement_strategy)
@settings(max_examples=50)
def test_sgraph_expressionelement_instantiation(instance):
    assert isinstance(instance, sgraph_ExpressionElement)



@given(instance=sgraph_ExpressionElement_strategy)
def test_sgraph_expressionelement_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=sgraph_Effect_strategy)
@settings(max_examples=50)
def test_sgraph_effect_instantiation(instance):
    assert isinstance(instance, sgraph_Effect)

@given(instance=sgraph_Trigger_strategy)
@settings(max_examples=50)
def test_sgraph_trigger_instantiation(instance):
    assert isinstance(instance, sgraph_Trigger)

@given(instance=Reaction_strategy)
@settings(max_examples=50)
def test_reaction_instantiation(instance):
    assert isinstance(instance, Reaction)

@given(instance=ExpressionElement_strategy)
@settings(max_examples=50)
def test_expressionelement_instantiation(instance):
    assert isinstance(instance, ExpressionElement)

@given(instance=Pseudostate_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)

@given(instance=sgraph_Synchronization_strategy)
@settings(max_examples=50)
def test_sgraph_synchronization_instantiation(instance):
    assert isinstance(instance, sgraph_Synchronization)

@given(instance=sgraph_Exit_strategy)
@settings(max_examples=50)
def test_sgraph_exit_instantiation(instance):
    assert isinstance(instance, sgraph_Exit)

@given(instance=sgraph_Entry_strategy)
@settings(max_examples=50)
def test_sgraph_entry_instantiation(instance):
    assert isinstance(instance, sgraph_Entry)



@given(instance=sgraph_Entry_strategy)
def test_sgraph_entry_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=sgraph_Choice_strategy)
@settings(max_examples=50)
def test_sgraph_choice_instantiation(instance):
    assert isinstance(instance, sgraph_Choice)



@given(instance=sgraph_Choice_strategy)
def test_sgraph_choice_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=sgraph_Event_strategy)
@settings(max_examples=50)
def test_sgraph_event_instantiation(instance):
    assert isinstance(instance, sgraph_Event)

@given(instance=sgraph_Variable_strategy)
@settings(max_examples=50)
def test_sgraph_variable_instantiation(instance):
    assert isinstance(instance, sgraph_Variable)

@given(instance=RegularState_strategy)
@settings(max_examples=50)
def test_regularstate_instantiation(instance):
    assert isinstance(instance, RegularState)

@given(instance=sgraph_State_strategy)
@settings(max_examples=50)
def test_sgraph_state_instantiation(instance):
    assert isinstance(instance, sgraph_State)



@given(instance=sgraph_State_strategy)
def test_sgraph_state_composite_setter(instance):
    original = instance.composite
    instance.composite = original
    assert instance.composite == original



@given(instance=sgraph_State_strategy)
def test_sgraph_state_orthogonal_setter(instance):
    original = instance.orthogonal
    instance.orthogonal = original
    assert instance.orthogonal == original



@given(instance=sgraph_State_strategy)
def test_sgraph_state_submachine_setter(instance):
    original = instance.submachine
    instance.submachine = original
    assert instance.submachine == original



@given(instance=sgraph_State_strategy)
def test_sgraph_state_leaf_setter(instance):
    original = instance.leaf
    instance.leaf = original
    assert instance.leaf == original



@given(instance=sgraph_State_strategy)
def test_sgraph_state_simple_setter(instance):
    original = instance.simple
    instance.simple = original
    assert instance.simple == original



@given(instance=sgraph_State_strategy)
def test_sgraph_state_substatechartId_setter(instance):
    original = instance.substatechartId
    instance.substatechartId = original
    assert instance.substatechartId == original

@given(instance=sgraph_FinalState_strategy)
@settings(max_examples=50)
def test_sgraph_finalstate_instantiation(instance):
    assert isinstance(instance, sgraph_FinalState)

@given(instance=sgraph_NamedElement_strategy)
@settings(max_examples=50)
def test_sgraph_namedelement_instantiation(instance):
    assert isinstance(instance, sgraph_NamedElement)



@given(instance=sgraph_NamedElement_strategy)
def test_sgraph_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sgraph_Transition_strategy)
@settings(max_examples=50)
def test_sgraph_transition_instantiation(instance):
    assert isinstance(instance, sgraph_Transition)



@given(instance=sgraph_Transition_strategy)
def test_sgraph_transition_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=sgraph_Region_strategy)
@settings(max_examples=50)
def test_sgraph_region_instantiation(instance):
    assert isinstance(instance, sgraph_Region)



@given(instance=sgraph_Region_strategy)
def test_sgraph_region_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=sgraph_Declaration_strategy)
@settings(max_examples=50)
def test_sgraph_declaration_instantiation(instance):
    assert isinstance(instance, sgraph_Declaration)

@given(instance=sgraph_Statechart_strategy)
@settings(max_examples=50)
def test_sgraph_statechart_instantiation(instance):
    assert isinstance(instance, sgraph_Statechart)

@given(instance=sgraph_Vertex_strategy)
@settings(max_examples=50)
def test_sgraph_vertex_instantiation(instance):
    assert isinstance(instance, sgraph_Vertex)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=sgraph_RegularState_strategy)
@settings(max_examples=50)
def test_sgraph_regularstate_instantiation(instance):
    assert isinstance(instance, sgraph_RegularState)

@given(instance=sgraph_Pseudostate_strategy)
@settings(max_examples=50)
def test_sgraph_pseudostate_instantiation(instance):
    assert isinstance(instance, sgraph_Pseudostate)
