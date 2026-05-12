import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Declaration,
    sgraph_ImportDeclaration,
    sgraph_ScopedElement,
    sgraph_Property,
    sgraph_Event,
    sgraph_Declaration,
    sgraph_Scope,
    sgraph_SpecificationElement,
    sgraph_ReactionProperty,
    sgraph_ReactiveElement,
    sgraph_Import,
    DomainElement,
    CompositeElement,
    ScopedElement,
    ReactiveElement,
    Pseudostate,
    sgraph_Entry,
    sgraph_Exit,
    sgraph_Synchronization,
    sgraph_Choice,
    RegularState,
    sgraph_FinalState,
    sgraph_Effect,
    sgraph_Trigger,
    sgraph_Reaction,
    NamedElement,
    sgraph_Region,
    sgraph_Vertex,
    Vertex,
    sgraph_RegularState,
    sgraph_Pseudostate,
    DocumentedElement,
    Reaction,
    SpecificationElement,
    sgraph_Statechart,
    sgraph_Transition,
    sgraph_State,
    sgraph_CompositeElement,
    ChoiceKind,
    EntryKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(sgraph_ImportDeclaration)


def test_sgraph_importdeclaration_constructor_exists():
    assert callable(sgraph_ImportDeclaration.__init__)


def test_sgraph_importdeclaration_constructor_args():
    sig = inspect.signature(sgraph_ImportDeclaration.__init__)
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



def test_sgraph_property_is_not_abstract():
    assert not inspect.isabstract(sgraph_Property)


def test_sgraph_property_constructor_exists():
    assert callable(sgraph_Property.__init__)


def test_sgraph_property_constructor_args():
    sig = inspect.signature(sgraph_Property.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_event_is_not_abstract():
    assert not inspect.isabstract(sgraph_Event)


def test_sgraph_event_constructor_exists():
    assert callable(sgraph_Event.__init__)


def test_sgraph_event_constructor_args():
    sig = inspect.signature(sgraph_Event.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_declaration_is_not_abstract():
    assert not inspect.isabstract(sgraph_Declaration)


def test_sgraph_declaration_constructor_exists():
    assert callable(sgraph_Declaration.__init__)


def test_sgraph_declaration_constructor_args():
    sig = inspect.signature(sgraph_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_scope_is_not_abstract():
    assert not inspect.isabstract(sgraph_Scope)


def test_sgraph_scope_constructor_exists():
    assert callable(sgraph_Scope.__init__)


def test_sgraph_scope_constructor_args():
    sig = inspect.signature(sgraph_Scope.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_specificationelement_is_not_abstract():
    assert not inspect.isabstract(sgraph_SpecificationElement)


def test_sgraph_specificationelement_constructor_exists():
    assert callable(sgraph_SpecificationElement.__init__)


def test_sgraph_specificationelement_constructor_args():
    sig = inspect.signature(sgraph_SpecificationElement.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_sgraph_specificationelement_has_specification():
    assert hasattr(sgraph_SpecificationElement, "specification")
    descriptor = None
    for klass in sgraph_SpecificationElement.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_sgraph_reactionproperty_is_not_abstract():
    assert not inspect.isabstract(sgraph_ReactionProperty)


def test_sgraph_reactionproperty_constructor_exists():
    assert callable(sgraph_ReactionProperty.__init__)


def test_sgraph_reactionproperty_constructor_args():
    sig = inspect.signature(sgraph_ReactionProperty.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_reactiveelement_is_not_abstract():
    assert not inspect.isabstract(sgraph_ReactiveElement)


def test_sgraph_reactiveelement_constructor_exists():
    assert callable(sgraph_ReactiveElement.__init__)


def test_sgraph_reactiveelement_constructor_args():
    sig = inspect.signature(sgraph_ReactiveElement.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_import_is_not_abstract():
    assert not inspect.isabstract(sgraph_Import)


def test_sgraph_import_constructor_exists():
    assert callable(sgraph_Import.__init__)


def test_sgraph_import_constructor_args():
    sig = inspect.signature(sgraph_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_sgraph_import_has_importedNamespace():
    assert hasattr(sgraph_Import, "importedNamespace")
    descriptor = None
    for klass in sgraph_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_domainelement_is_not_abstract():
    assert not inspect.isabstract(DomainElement)


def test_domainelement_constructor_exists():
    assert callable(DomainElement.__init__)


def test_domainelement_constructor_args():
    sig = inspect.signature(DomainElement.__init__)
    params = list(sig.parameters.keys())



def test_compositeelement_is_not_abstract():
    assert not inspect.isabstract(CompositeElement)


def test_compositeelement_constructor_exists():
    assert callable(CompositeElement.__init__)


def test_compositeelement_constructor_args():
    sig = inspect.signature(CompositeElement.__init__)
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



def test_sgraph_exit_is_not_abstract():
    assert not inspect.isabstract(sgraph_Exit)


def test_sgraph_exit_constructor_exists():
    assert callable(sgraph_Exit.__init__)


def test_sgraph_exit_constructor_args():
    sig = inspect.signature(sgraph_Exit.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_synchronization_is_not_abstract():
    assert not inspect.isabstract(sgraph_Synchronization)


def test_sgraph_synchronization_constructor_exists():
    assert callable(sgraph_Synchronization.__init__)


def test_sgraph_synchronization_constructor_args():
    sig = inspect.signature(sgraph_Synchronization.__init__)
    params = list(sig.parameters.keys())



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



def test_regularstate_is_not_abstract():
    assert not inspect.isabstract(RegularState)


def test_regularstate_constructor_exists():
    assert callable(RegularState.__init__)


def test_regularstate_constructor_args():
    sig = inspect.signature(RegularState.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_finalstate_is_not_abstract():
    assert not inspect.isabstract(sgraph_FinalState)


def test_sgraph_finalstate_constructor_exists():
    assert callable(sgraph_FinalState.__init__)


def test_sgraph_finalstate_constructor_args():
    sig = inspect.signature(sgraph_FinalState.__init__)
    params = list(sig.parameters.keys())



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



def test_sgraph_reaction_is_not_abstract():
    assert not inspect.isabstract(sgraph_Reaction)


def test_sgraph_reaction_constructor_exists():
    assert callable(sgraph_Reaction.__init__)


def test_sgraph_reaction_constructor_args():
    sig = inspect.signature(sgraph_Reaction.__init__)
    params = list(sig.parameters.keys())



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



def test_documentedelement_is_not_abstract():
    assert not inspect.isabstract(DocumentedElement)


def test_documentedelement_constructor_exists():
    assert callable(DocumentedElement.__init__)


def test_documentedelement_constructor_args():
    sig = inspect.signature(DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_reaction_is_not_abstract():
    assert not inspect.isabstract(Reaction)


def test_reaction_constructor_exists():
    assert callable(Reaction.__init__)


def test_reaction_constructor_args():
    sig = inspect.signature(Reaction.__init__)
    params = list(sig.parameters.keys())



def test_specificationelement_is_not_abstract():
    assert not inspect.isabstract(SpecificationElement)


def test_specificationelement_constructor_exists():
    assert callable(SpecificationElement.__init__)


def test_specificationelement_constructor_args():
    sig = inspect.signature(SpecificationElement.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_statechart_is_not_abstract():
    assert not inspect.isabstract(sgraph_Statechart)


def test_sgraph_statechart_constructor_exists():
    assert callable(sgraph_Statechart.__init__)


def test_sgraph_statechart_constructor_args():
    sig = inspect.signature(sgraph_Statechart.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_transition_is_not_abstract():
    assert not inspect.isabstract(sgraph_Transition)


def test_sgraph_transition_constructor_exists():
    assert callable(sgraph_Transition.__init__)


def test_sgraph_transition_constructor_args():
    sig = inspect.signature(sgraph_Transition.__init__)
    params = list(sig.parameters.keys())



def test_sgraph_state_is_not_abstract():
    assert not inspect.isabstract(sgraph_State)


def test_sgraph_state_constructor_exists():
    assert callable(sgraph_State.__init__)


def test_sgraph_state_constructor_args():
    sig = inspect.signature(sgraph_State.__init__)
    params = list(sig.parameters.keys())
    assert "composite" in params, "Missing parameter 'composite'"
    assert "substatechartId" in params, "Missing parameter 'substatechartId'"
    assert "simple" in params, "Missing parameter 'simple'"
    assert "orthogonal" in params, "Missing parameter 'orthogonal'"
    assert "subchart" in params, "Missing parameter 'subchart'"
    assert "leaf" in params, "Missing parameter 'leaf'"

def test_sgraph_state_has_composite():
    assert hasattr(sgraph_State, "composite")
    descriptor = None
    for klass in sgraph_State.__mro__:
        if "composite" in klass.__dict__:
            descriptor = klass.__dict__["composite"]
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

def test_sgraph_state_has_simple():
    assert hasattr(sgraph_State, "simple")
    descriptor = None
    for klass in sgraph_State.__mro__:
        if "simple" in klass.__dict__:
            descriptor = klass.__dict__["simple"]
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

def test_sgraph_state_has_subchart():
    assert hasattr(sgraph_State, "subchart")
    descriptor = None
    for klass in sgraph_State.__mro__:
        if "subchart" in klass.__dict__:
            descriptor = klass.__dict__["subchart"]
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



def test_sgraph_compositeelement_is_not_abstract():
    assert not inspect.isabstract(sgraph_CompositeElement)


def test_sgraph_compositeelement_constructor_exists():
    assert callable(sgraph_CompositeElement.__init__)


def test_sgraph_compositeelement_constructor_args():
    sig = inspect.signature(sgraph_CompositeElement.__init__)
    params = list(sig.parameters.keys())

def test_choicekind_exists():
    # Check that the Enumeration exists
    assert ChoiceKind is not None

def test_choicekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ChoiceKind]
    expected_literals = [
        "static",
        "dynamic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ChoiceKind"

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
Declaration_strategy = st.builds(
    Declaration,
)
sgraph_ImportDeclaration_strategy = st.builds(
    sgraph_ImportDeclaration,
)
sgraph_ScopedElement_strategy = st.builds(
    sgraph_ScopedElement,
    namespace=
        safe_text
)
sgraph_Property_strategy = st.builds(
    sgraph_Property,
)
sgraph_Event_strategy = st.builds(
    sgraph_Event,
)
sgraph_Declaration_strategy = st.builds(
    sgraph_Declaration,
)
sgraph_Scope_strategy = st.builds(
    sgraph_Scope,
)
sgraph_SpecificationElement_strategy = st.builds(
    sgraph_SpecificationElement,
    specification=
        safe_text
)
sgraph_ReactionProperty_strategy = st.builds(
    sgraph_ReactionProperty,
)
sgraph_ReactiveElement_strategy = st.builds(
    sgraph_ReactiveElement,
)
sgraph_Import_strategy = st.builds(
    sgraph_Import,
    importedNamespace=
        safe_text
)
DomainElement_strategy = st.builds(
    DomainElement,
)
CompositeElement_strategy = st.builds(
    CompositeElement,
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
sgraph_Entry_strategy = st.builds(
    sgraph_Entry,
    kind=
        safe_text
)
sgraph_Exit_strategy = st.builds(
    sgraph_Exit,
)
sgraph_Synchronization_strategy = st.builds(
    sgraph_Synchronization,
)
sgraph_Choice_strategy = st.builds(
    sgraph_Choice,
    kind=
        safe_text
)
RegularState_strategy = st.builds(
    RegularState,
)
sgraph_FinalState_strategy = st.builds(
    sgraph_FinalState,
)
sgraph_Effect_strategy = st.builds(
    sgraph_Effect,
)
sgraph_Trigger_strategy = st.builds(
    sgraph_Trigger,
)
sgraph_Reaction_strategy = st.builds(
    sgraph_Reaction,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
sgraph_Region_strategy = st.builds(
    sgraph_Region,
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
DocumentedElement_strategy = st.builds(
    DocumentedElement,
)
Reaction_strategy = st.builds(
    Reaction,
)
SpecificationElement_strategy = st.builds(
    SpecificationElement,
)
sgraph_Statechart_strategy = st.builds(
    sgraph_Statechart,
)
sgraph_Transition_strategy = st.builds(
    sgraph_Transition,
)
sgraph_State_strategy = st.builds(
    sgraph_State,
    composite=
        st.booleans(),
    substatechartId=
        safe_text,
    simple=
        st.booleans(),
    orthogonal=
        st.booleans(),
    subchart=
        st.booleans(),
    leaf=
        st.booleans()
)
sgraph_CompositeElement_strategy = st.builds(
    sgraph_CompositeElement,
)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=sgraph_ImportDeclaration_strategy)
@settings(max_examples=50)
def test_sgraph_importdeclaration_instantiation(instance):
    assert isinstance(instance, sgraph_ImportDeclaration)

@given(instance=sgraph_ScopedElement_strategy)
@settings(max_examples=50)
def test_sgraph_scopedelement_instantiation(instance):
    assert isinstance(instance, sgraph_ScopedElement)



@given(instance=sgraph_ScopedElement_strategy)
def test_sgraph_scopedelement_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=sgraph_Property_strategy)
@settings(max_examples=50)
def test_sgraph_property_instantiation(instance):
    assert isinstance(instance, sgraph_Property)

@given(instance=sgraph_Event_strategy)
@settings(max_examples=50)
def test_sgraph_event_instantiation(instance):
    assert isinstance(instance, sgraph_Event)

@given(instance=sgraph_Declaration_strategy)
@settings(max_examples=50)
def test_sgraph_declaration_instantiation(instance):
    assert isinstance(instance, sgraph_Declaration)

@given(instance=sgraph_Scope_strategy)
@settings(max_examples=50)
def test_sgraph_scope_instantiation(instance):
    assert isinstance(instance, sgraph_Scope)

@given(instance=sgraph_SpecificationElement_strategy)
@settings(max_examples=50)
def test_sgraph_specificationelement_instantiation(instance):
    assert isinstance(instance, sgraph_SpecificationElement)



@given(instance=sgraph_SpecificationElement_strategy)
def test_sgraph_specificationelement_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=sgraph_ReactionProperty_strategy)
@settings(max_examples=50)
def test_sgraph_reactionproperty_instantiation(instance):
    assert isinstance(instance, sgraph_ReactionProperty)

@given(instance=sgraph_ReactiveElement_strategy)
@settings(max_examples=50)
def test_sgraph_reactiveelement_instantiation(instance):
    assert isinstance(instance, sgraph_ReactiveElement)

@given(instance=sgraph_Import_strategy)
@settings(max_examples=50)
def test_sgraph_import_instantiation(instance):
    assert isinstance(instance, sgraph_Import)



@given(instance=sgraph_Import_strategy)
def test_sgraph_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=DomainElement_strategy)
@settings(max_examples=50)
def test_domainelement_instantiation(instance):
    assert isinstance(instance, DomainElement)

@given(instance=CompositeElement_strategy)
@settings(max_examples=50)
def test_compositeelement_instantiation(instance):
    assert isinstance(instance, CompositeElement)

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

@given(instance=sgraph_Entry_strategy)
@settings(max_examples=50)
def test_sgraph_entry_instantiation(instance):
    assert isinstance(instance, sgraph_Entry)



@given(instance=sgraph_Entry_strategy)
def test_sgraph_entry_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=sgraph_Exit_strategy)
@settings(max_examples=50)
def test_sgraph_exit_instantiation(instance):
    assert isinstance(instance, sgraph_Exit)

@given(instance=sgraph_Synchronization_strategy)
@settings(max_examples=50)
def test_sgraph_synchronization_instantiation(instance):
    assert isinstance(instance, sgraph_Synchronization)

@given(instance=sgraph_Choice_strategy)
@settings(max_examples=50)
def test_sgraph_choice_instantiation(instance):
    assert isinstance(instance, sgraph_Choice)



@given(instance=sgraph_Choice_strategy)
def test_sgraph_choice_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=RegularState_strategy)
@settings(max_examples=50)
def test_regularstate_instantiation(instance):
    assert isinstance(instance, RegularState)

@given(instance=sgraph_FinalState_strategy)
@settings(max_examples=50)
def test_sgraph_finalstate_instantiation(instance):
    assert isinstance(instance, sgraph_FinalState)

@given(instance=sgraph_Effect_strategy)
@settings(max_examples=50)
def test_sgraph_effect_instantiation(instance):
    assert isinstance(instance, sgraph_Effect)

@given(instance=sgraph_Trigger_strategy)
@settings(max_examples=50)
def test_sgraph_trigger_instantiation(instance):
    assert isinstance(instance, sgraph_Trigger)

@given(instance=sgraph_Reaction_strategy)
@settings(max_examples=50)
def test_sgraph_reaction_instantiation(instance):
    assert isinstance(instance, sgraph_Reaction)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=sgraph_Region_strategy)
@settings(max_examples=50)
def test_sgraph_region_instantiation(instance):
    assert isinstance(instance, sgraph_Region)

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

@given(instance=DocumentedElement_strategy)
@settings(max_examples=50)
def test_documentedelement_instantiation(instance):
    assert isinstance(instance, DocumentedElement)

@given(instance=Reaction_strategy)
@settings(max_examples=50)
def test_reaction_instantiation(instance):
    assert isinstance(instance, Reaction)

@given(instance=SpecificationElement_strategy)
@settings(max_examples=50)
def test_specificationelement_instantiation(instance):
    assert isinstance(instance, SpecificationElement)

@given(instance=sgraph_Statechart_strategy)
@settings(max_examples=50)
def test_sgraph_statechart_instantiation(instance):
    assert isinstance(instance, sgraph_Statechart)

@given(instance=sgraph_Transition_strategy)
@settings(max_examples=50)
def test_sgraph_transition_instantiation(instance):
    assert isinstance(instance, sgraph_Transition)

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
def test_sgraph_state_substatechartId_setter(instance):
    original = instance.substatechartId
    instance.substatechartId = original
    assert instance.substatechartId == original



@given(instance=sgraph_State_strategy)
def test_sgraph_state_simple_setter(instance):
    original = instance.simple
    instance.simple = original
    assert instance.simple == original



@given(instance=sgraph_State_strategy)
def test_sgraph_state_orthogonal_setter(instance):
    original = instance.orthogonal
    instance.orthogonal = original
    assert instance.orthogonal == original



@given(instance=sgraph_State_strategy)
def test_sgraph_state_subchart_setter(instance):
    original = instance.subchart
    instance.subchart = original
    assert instance.subchart == original



@given(instance=sgraph_State_strategy)
def test_sgraph_state_leaf_setter(instance):
    original = instance.leaf
    instance.leaf = original
    assert instance.leaf == original

@given(instance=sgraph_CompositeElement_strategy)
@settings(max_examples=50)
def test_sgraph_compositeelement_instantiation(instance):
    assert isinstance(instance, sgraph_CompositeElement)
