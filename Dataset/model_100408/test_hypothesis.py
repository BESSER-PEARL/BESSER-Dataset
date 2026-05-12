import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sgraph::Statement,
    sgraph::ScopedElement,
    sgraph::Scope,
    sgraph::Reaction,
    sgraph::ExpressionElement,
    sgraph::Effect,
    sgraph::Trigger,
    sgraph::ReactiveElement,
    ScopedElement,
    ReactiveElement,
    Pseudostate,
    sgraph::Exit,
    sgraph::Synchronization,
    sgraph::Choice,
    sgraph::Junction,
    Declaration,
    sgraph::Event,
    sgraph::Variable,
    sgraph::Entry,
    sgraph::NamedElement,
    Reaction,
    ExpressionElement,
    Vertex,
    sgraph::FinalState,
    sgraph::State,
    sgraph::Pseudostate,
    sgraph::Transition,
    NamedElement,
    sgraph::Region,
    sgraph::Statechart,
    sgraph::Declaration,
    sgraph::Vertex,
    EntryKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sgraph::statement_is_not_abstract():
    assert not inspect.isabstract(sgraph::Statement)


def test_sgraph::statement_constructor_exists():
    assert callable(sgraph::Statement.__init__)


def test_sgraph::statement_constructor_args():
    sig = inspect.signature(sgraph::Statement.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::scopedelement_is_not_abstract():
    assert not inspect.isabstract(sgraph::ScopedElement)


def test_sgraph::scopedelement_constructor_exists():
    assert callable(sgraph::ScopedElement.__init__)


def test_sgraph::scopedelement_constructor_args():
    sig = inspect.signature(sgraph::ScopedElement.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_sgraph::scopedelement_has_namespace():
    assert hasattr(sgraph::ScopedElement, "namespace")
    descriptor = None
    for klass in sgraph::ScopedElement.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_sgraph::scope_is_not_abstract():
    assert not inspect.isabstract(sgraph::Scope)


def test_sgraph::scope_constructor_exists():
    assert callable(sgraph::Scope.__init__)


def test_sgraph::scope_constructor_args():
    sig = inspect.signature(sgraph::Scope.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::reaction_is_not_abstract():
    assert not inspect.isabstract(sgraph::Reaction)


def test_sgraph::reaction_constructor_exists():
    assert callable(sgraph::Reaction.__init__)


def test_sgraph::reaction_constructor_args():
    sig = inspect.signature(sgraph::Reaction.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::expressionelement_is_not_abstract():
    assert not inspect.isabstract(sgraph::ExpressionElement)


def test_sgraph::expressionelement_constructor_exists():
    assert callable(sgraph::ExpressionElement.__init__)


def test_sgraph::expressionelement_constructor_args():
    sig = inspect.signature(sgraph::ExpressionElement.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_sgraph::expressionelement_has_expression():
    assert hasattr(sgraph::ExpressionElement, "expression")
    descriptor = None
    for klass in sgraph::ExpressionElement.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_sgraph::effect_is_not_abstract():
    assert not inspect.isabstract(sgraph::Effect)


def test_sgraph::effect_constructor_exists():
    assert callable(sgraph::Effect.__init__)


def test_sgraph::effect_constructor_args():
    sig = inspect.signature(sgraph::Effect.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::trigger_is_not_abstract():
    assert not inspect.isabstract(sgraph::Trigger)


def test_sgraph::trigger_constructor_exists():
    assert callable(sgraph::Trigger.__init__)


def test_sgraph::trigger_constructor_args():
    sig = inspect.signature(sgraph::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::reactiveelement_is_not_abstract():
    assert not inspect.isabstract(sgraph::ReactiveElement)


def test_sgraph::reactiveelement_constructor_exists():
    assert callable(sgraph::ReactiveElement.__init__)


def test_sgraph::reactiveelement_constructor_args():
    sig = inspect.signature(sgraph::ReactiveElement.__init__)
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



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::exit_is_not_abstract():
    assert not inspect.isabstract(sgraph::Exit)


def test_sgraph::exit_constructor_exists():
    assert callable(sgraph::Exit.__init__)


def test_sgraph::exit_constructor_args():
    sig = inspect.signature(sgraph::Exit.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::synchronization_is_not_abstract():
    assert not inspect.isabstract(sgraph::Synchronization)


def test_sgraph::synchronization_constructor_exists():
    assert callable(sgraph::Synchronization.__init__)


def test_sgraph::synchronization_constructor_args():
    sig = inspect.signature(sgraph::Synchronization.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::choice_is_not_abstract():
    assert not inspect.isabstract(sgraph::Choice)


def test_sgraph::choice_constructor_exists():
    assert callable(sgraph::Choice.__init__)


def test_sgraph::choice_constructor_args():
    sig = inspect.signature(sgraph::Choice.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::junction_is_not_abstract():
    assert not inspect.isabstract(sgraph::Junction)


def test_sgraph::junction_constructor_exists():
    assert callable(sgraph::Junction.__init__)


def test_sgraph::junction_constructor_args():
    sig = inspect.signature(sgraph::Junction.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::event_is_not_abstract():
    assert not inspect.isabstract(sgraph::Event)


def test_sgraph::event_constructor_exists():
    assert callable(sgraph::Event.__init__)


def test_sgraph::event_constructor_args():
    sig = inspect.signature(sgraph::Event.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::variable_is_not_abstract():
    assert not inspect.isabstract(sgraph::Variable)


def test_sgraph::variable_constructor_exists():
    assert callable(sgraph::Variable.__init__)


def test_sgraph::variable_constructor_args():
    sig = inspect.signature(sgraph::Variable.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::entry_is_not_abstract():
    assert not inspect.isabstract(sgraph::Entry)


def test_sgraph::entry_constructor_exists():
    assert callable(sgraph::Entry.__init__)


def test_sgraph::entry_constructor_args():
    sig = inspect.signature(sgraph::Entry.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_sgraph::entry_has_kind():
    assert hasattr(sgraph::Entry, "kind")
    descriptor = None
    for klass in sgraph::Entry.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_sgraph::namedelement_is_not_abstract():
    assert not inspect.isabstract(sgraph::NamedElement)


def test_sgraph::namedelement_constructor_exists():
    assert callable(sgraph::NamedElement.__init__)


def test_sgraph::namedelement_constructor_args():
    sig = inspect.signature(sgraph::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sgraph::namedelement_has_name():
    assert hasattr(sgraph::NamedElement, "name")
    descriptor = None
    for klass in sgraph::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::finalstate_is_not_abstract():
    assert not inspect.isabstract(sgraph::FinalState)


def test_sgraph::finalstate_constructor_exists():
    assert callable(sgraph::FinalState.__init__)


def test_sgraph::finalstate_constructor_args():
    sig = inspect.signature(sgraph::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::state_is_not_abstract():
    assert not inspect.isabstract(sgraph::State)


def test_sgraph::state_constructor_exists():
    assert callable(sgraph::State.__init__)


def test_sgraph::state_constructor_args():
    sig = inspect.signature(sgraph::State.__init__)
    params = list(sig.parameters.keys())
    assert "orthogonal" in params, "Missing parameter 'orthogonal'"
    assert "simple" in params, "Missing parameter 'simple'"
    assert "composite" in params, "Missing parameter 'composite'"
    assert "submachine" in params, "Missing parameter 'submachine'"
    assert "leaf" in params, "Missing parameter 'leaf'"

def test_sgraph::state_has_orthogonal():
    assert hasattr(sgraph::State, "orthogonal")
    descriptor = None
    for klass in sgraph::State.__mro__:
        if "orthogonal" in klass.__dict__:
            descriptor = klass.__dict__["orthogonal"]
            break
    assert isinstance(descriptor, property)

def test_sgraph::state_has_simple():
    assert hasattr(sgraph::State, "simple")
    descriptor = None
    for klass in sgraph::State.__mro__:
        if "simple" in klass.__dict__:
            descriptor = klass.__dict__["simple"]
            break
    assert isinstance(descriptor, property)

def test_sgraph::state_has_composite():
    assert hasattr(sgraph::State, "composite")
    descriptor = None
    for klass in sgraph::State.__mro__:
        if "composite" in klass.__dict__:
            descriptor = klass.__dict__["composite"]
            break
    assert isinstance(descriptor, property)

def test_sgraph::state_has_submachine():
    assert hasattr(sgraph::State, "submachine")
    descriptor = None
    for klass in sgraph::State.__mro__:
        if "submachine" in klass.__dict__:
            descriptor = klass.__dict__["submachine"]
            break
    assert isinstance(descriptor, property)

def test_sgraph::state_has_leaf():
    assert hasattr(sgraph::State, "leaf")
    descriptor = None
    for klass in sgraph::State.__mro__:
        if "leaf" in klass.__dict__:
            descriptor = klass.__dict__["leaf"]
            break
    assert isinstance(descriptor, property)



def test_sgraph::pseudostate_is_not_abstract():
    assert not inspect.isabstract(sgraph::Pseudostate)


def test_sgraph::pseudostate_constructor_exists():
    assert callable(sgraph::Pseudostate.__init__)


def test_sgraph::pseudostate_constructor_args():
    sig = inspect.signature(sgraph::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::transition_is_not_abstract():
    assert not inspect.isabstract(sgraph::Transition)


def test_sgraph::transition_constructor_exists():
    assert callable(sgraph::Transition.__init__)


def test_sgraph::transition_constructor_args():
    sig = inspect.signature(sgraph::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_sgraph::transition_has_priority():
    assert hasattr(sgraph::Transition, "priority")
    descriptor = None
    for klass in sgraph::Transition.__mro__:
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



def test_sgraph::region_is_not_abstract():
    assert not inspect.isabstract(sgraph::Region)


def test_sgraph::region_constructor_exists():
    assert callable(sgraph::Region.__init__)


def test_sgraph::region_constructor_args():
    sig = inspect.signature(sgraph::Region.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_sgraph::region_has_priority():
    assert hasattr(sgraph::Region, "priority")
    descriptor = None
    for klass in sgraph::Region.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_sgraph::statechart_is_not_abstract():
    assert not inspect.isabstract(sgraph::Statechart)


def test_sgraph::statechart_constructor_exists():
    assert callable(sgraph::Statechart.__init__)


def test_sgraph::statechart_constructor_args():
    sig = inspect.signature(sgraph::Statechart.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::declaration_is_not_abstract():
    assert not inspect.isabstract(sgraph::Declaration)


def test_sgraph::declaration_constructor_exists():
    assert callable(sgraph::Declaration.__init__)


def test_sgraph::declaration_constructor_args():
    sig = inspect.signature(sgraph::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_sgraph::vertex_is_not_abstract():
    assert not inspect.isabstract(sgraph::Vertex)


def test_sgraph::vertex_constructor_exists():
    assert callable(sgraph::Vertex.__init__)


def test_sgraph::vertex_constructor_args():
    sig = inspect.signature(sgraph::Vertex.__init__)
    params = list(sig.parameters.keys())

def test_entrykind_exists():
    # Check that the Enumeration exists
    assert EntryKind is not None

def test_entrykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntryKind]
    expected_literals = [
        "shallowHistory",
        "initial",
        "deepHistory",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntryKind"


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
sgraph::Statement_strategy = st.builds(
    sgraph::Statement,
)
sgraph::ScopedElement_strategy = st.builds(
    sgraph::ScopedElement,
    namespace=
        safe_text
)
sgraph::Scope_strategy = st.builds(
    sgraph::Scope,
)
sgraph::Reaction_strategy = st.builds(
    sgraph::Reaction,
)
sgraph::ExpressionElement_strategy = st.builds(
    sgraph::ExpressionElement,
    expression=
        safe_text
)
sgraph::Effect_strategy = st.builds(
    sgraph::Effect,
)
sgraph::Trigger_strategy = st.builds(
    sgraph::Trigger,
)
sgraph::ReactiveElement_strategy = st.builds(
    sgraph::ReactiveElement,
)
ScopedElement_strategy = st.builds(
    ScopedElement,
)
ReactiveElement_strategy = st.builds(
    ReactiveElement,
)
Pseudostate_strategy = st.builds(
    Pseudostate,
)
sgraph::Exit_strategy = st.builds(
    sgraph::Exit,
)
sgraph::Synchronization_strategy = st.builds(
    sgraph::Synchronization,
)
sgraph::Choice_strategy = st.builds(
    sgraph::Choice,
)
sgraph::Junction_strategy = st.builds(
    sgraph::Junction,
)
Declaration_strategy = st.builds(
    Declaration,
)
sgraph::Event_strategy = st.builds(
    sgraph::Event,
)
sgraph::Variable_strategy = st.builds(
    sgraph::Variable,
)
sgraph::Entry_strategy = st.builds(
    sgraph::Entry,
    kind=
        safe_text
)
sgraph::NamedElement_strategy = st.builds(
    sgraph::NamedElement,
    name=
        safe_text
)
Reaction_strategy = st.builds(
    Reaction,
)
ExpressionElement_strategy = st.builds(
    ExpressionElement,
)
Vertex_strategy = st.builds(
    Vertex,
)
sgraph::FinalState_strategy = st.builds(
    sgraph::FinalState,
)
sgraph::State_strategy = st.builds(
    sgraph::State,
    orthogonal=
        st.booleans(),
    simple=
        st.booleans(),
    composite=
        st.booleans(),
    submachine=
        st.booleans(),
    leaf=
        st.booleans()
)
sgraph::Pseudostate_strategy = st.builds(
    sgraph::Pseudostate,
)
sgraph::Transition_strategy = st.builds(
    sgraph::Transition,
    priority=
        st.integers()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
sgraph::Region_strategy = st.builds(
    sgraph::Region,
    priority=
        st.integers()
)
sgraph::Statechart_strategy = st.builds(
    sgraph::Statechart,
)
sgraph::Declaration_strategy = st.builds(
    sgraph::Declaration,
)
sgraph::Vertex_strategy = st.builds(
    sgraph::Vertex,
)

@given(instance=sgraph::Statement_strategy)
@settings(max_examples=50)
def test_sgraph::statement_instantiation(instance):
    assert isinstance(instance, sgraph::Statement)

@given(instance=sgraph::ScopedElement_strategy)
@settings(max_examples=50)
def test_sgraph::scopedelement_instantiation(instance):
    assert isinstance(instance, sgraph::ScopedElement)

@given(instance=sgraph::ScopedElement_strategy)
def test_sgraph::scopedelement_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=sgraph::ScopedElement_strategy)
def test_sgraph::scopedelement_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=sgraph::Scope_strategy)
@settings(max_examples=50)
def test_sgraph::scope_instantiation(instance):
    assert isinstance(instance, sgraph::Scope)

@given(instance=sgraph::Reaction_strategy)
@settings(max_examples=50)
def test_sgraph::reaction_instantiation(instance):
    assert isinstance(instance, sgraph::Reaction)

@given(instance=sgraph::ExpressionElement_strategy)
@settings(max_examples=50)
def test_sgraph::expressionelement_instantiation(instance):
    assert isinstance(instance, sgraph::ExpressionElement)

@given(instance=sgraph::ExpressionElement_strategy)
def test_sgraph::expressionelement_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=sgraph::ExpressionElement_strategy)
def test_sgraph::expressionelement_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=sgraph::Effect_strategy)
@settings(max_examples=50)
def test_sgraph::effect_instantiation(instance):
    assert isinstance(instance, sgraph::Effect)

@given(instance=sgraph::Trigger_strategy)
@settings(max_examples=50)
def test_sgraph::trigger_instantiation(instance):
    assert isinstance(instance, sgraph::Trigger)

@given(instance=sgraph::ReactiveElement_strategy)
@settings(max_examples=50)
def test_sgraph::reactiveelement_instantiation(instance):
    assert isinstance(instance, sgraph::ReactiveElement)

@given(instance=ScopedElement_strategy)
@settings(max_examples=50)
def test_scopedelement_instantiation(instance):
    assert isinstance(instance, ScopedElement)

@given(instance=ReactiveElement_strategy)
@settings(max_examples=50)
def test_reactiveelement_instantiation(instance):
    assert isinstance(instance, ReactiveElement)

@given(instance=Pseudostate_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)

@given(instance=sgraph::Exit_strategy)
@settings(max_examples=50)
def test_sgraph::exit_instantiation(instance):
    assert isinstance(instance, sgraph::Exit)

@given(instance=sgraph::Synchronization_strategy)
@settings(max_examples=50)
def test_sgraph::synchronization_instantiation(instance):
    assert isinstance(instance, sgraph::Synchronization)

@given(instance=sgraph::Choice_strategy)
@settings(max_examples=50)
def test_sgraph::choice_instantiation(instance):
    assert isinstance(instance, sgraph::Choice)

@given(instance=sgraph::Junction_strategy)
@settings(max_examples=50)
def test_sgraph::junction_instantiation(instance):
    assert isinstance(instance, sgraph::Junction)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=sgraph::Event_strategy)
@settings(max_examples=50)
def test_sgraph::event_instantiation(instance):
    assert isinstance(instance, sgraph::Event)

@given(instance=sgraph::Variable_strategy)
@settings(max_examples=50)
def test_sgraph::variable_instantiation(instance):
    assert isinstance(instance, sgraph::Variable)

@given(instance=sgraph::Entry_strategy)
@settings(max_examples=50)
def test_sgraph::entry_instantiation(instance):
    assert isinstance(instance, sgraph::Entry)

@given(instance=sgraph::Entry_strategy)
def test_sgraph::entry_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=sgraph::Entry_strategy)
def test_sgraph::entry_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=sgraph::NamedElement_strategy)
@settings(max_examples=50)
def test_sgraph::namedelement_instantiation(instance):
    assert isinstance(instance, sgraph::NamedElement)

@given(instance=sgraph::NamedElement_strategy)
def test_sgraph::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sgraph::NamedElement_strategy)
def test_sgraph::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Reaction_strategy)
@settings(max_examples=50)
def test_reaction_instantiation(instance):
    assert isinstance(instance, Reaction)

@given(instance=ExpressionElement_strategy)
@settings(max_examples=50)
def test_expressionelement_instantiation(instance):
    assert isinstance(instance, ExpressionElement)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=sgraph::FinalState_strategy)
@settings(max_examples=50)
def test_sgraph::finalstate_instantiation(instance):
    assert isinstance(instance, sgraph::FinalState)

@given(instance=sgraph::State_strategy)
@settings(max_examples=50)
def test_sgraph::state_instantiation(instance):
    assert isinstance(instance, sgraph::State)

@given(instance=sgraph::State_strategy)
def test_sgraph::state_orthogonal_type(instance):
    assert isinstance(instance.orthogonal, bool)


@given(instance=sgraph::State_strategy)
def test_sgraph::state_orthogonal_setter(instance):
    original = instance.orthogonal
    instance.orthogonal = original
    assert instance.orthogonal == original

@given(instance=sgraph::State_strategy)
def test_sgraph::state_simple_type(instance):
    assert isinstance(instance.simple, bool)


@given(instance=sgraph::State_strategy)
def test_sgraph::state_simple_setter(instance):
    original = instance.simple
    instance.simple = original
    assert instance.simple == original

@given(instance=sgraph::State_strategy)
def test_sgraph::state_composite_type(instance):
    assert isinstance(instance.composite, bool)


@given(instance=sgraph::State_strategy)
def test_sgraph::state_composite_setter(instance):
    original = instance.composite
    instance.composite = original
    assert instance.composite == original

@given(instance=sgraph::State_strategy)
def test_sgraph::state_submachine_type(instance):
    assert isinstance(instance.submachine, bool)


@given(instance=sgraph::State_strategy)
def test_sgraph::state_submachine_setter(instance):
    original = instance.submachine
    instance.submachine = original
    assert instance.submachine == original

@given(instance=sgraph::State_strategy)
def test_sgraph::state_leaf_type(instance):
    assert isinstance(instance.leaf, bool)


@given(instance=sgraph::State_strategy)
def test_sgraph::state_leaf_setter(instance):
    original = instance.leaf
    instance.leaf = original
    assert instance.leaf == original

@given(instance=sgraph::Pseudostate_strategy)
@settings(max_examples=50)
def test_sgraph::pseudostate_instantiation(instance):
    assert isinstance(instance, sgraph::Pseudostate)

@given(instance=sgraph::Transition_strategy)
@settings(max_examples=50)
def test_sgraph::transition_instantiation(instance):
    assert isinstance(instance, sgraph::Transition)

@given(instance=sgraph::Transition_strategy)
def test_sgraph::transition_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=sgraph::Transition_strategy)
def test_sgraph::transition_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=sgraph::Region_strategy)
@settings(max_examples=50)
def test_sgraph::region_instantiation(instance):
    assert isinstance(instance, sgraph::Region)

@given(instance=sgraph::Region_strategy)
def test_sgraph::region_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=sgraph::Region_strategy)
def test_sgraph::region_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=sgraph::Statechart_strategy)
@settings(max_examples=50)
def test_sgraph::statechart_instantiation(instance):
    assert isinstance(instance, sgraph::Statechart)

@given(instance=sgraph::Declaration_strategy)
@settings(max_examples=50)
def test_sgraph::declaration_instantiation(instance):
    assert isinstance(instance, sgraph::Declaration)

@given(instance=sgraph::Vertex_strategy)
@settings(max_examples=50)
def test_sgraph::vertex_instantiation(instance):
    assert isinstance(instance, sgraph::Vertex)
