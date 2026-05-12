import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Page,
    Arc,
    Transition,
    pragmacpndefinition::OntologyMember,
    PetriNet,
    pragmacpndefinition::OntologyDocument,
    Label,
    pragmacpndefinition::PragmaticsOntology,
    pragmacpndefinition::Pragma,
    OntologyMember,
    pragmacpndefinition::Transition,
    pragmacpndefinition::Arc,
    pragmacpndefinition::Page,
    Place,
    pragmacpndefinition::Place,
    CPN,
    pragmacpndefinition::PragmaCPN,
    pragmacpndefinition::PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_pragmacpndefinition::ontologymember_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition::OntologyMember)


def test_pragmacpndefinition::ontologymember_constructor_exists():
    assert callable(pragmacpndefinition::OntologyMember.__init__)


def test_pragmacpndefinition::ontologymember_constructor_args():
    sig = inspect.signature(pragmacpndefinition::OntologyMember.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet)


def test_petrinet_constructor_exists():
    assert callable(PetriNet.__init__)


def test_petrinet_constructor_args():
    sig = inspect.signature(PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_pragmacpndefinition::ontologydocument_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition::OntologyDocument)


def test_pragmacpndefinition::ontologydocument_constructor_exists():
    assert callable(pragmacpndefinition::OntologyDocument.__init__)


def test_pragmacpndefinition::ontologydocument_constructor_args():
    sig = inspect.signature(pragmacpndefinition::OntologyDocument.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "iri" in params, "Missing parameter 'iri'"

def test_pragmacpndefinition::ontologydocument_has_path():
    assert hasattr(pragmacpndefinition::OntologyDocument, "path")
    descriptor = None
    for klass in pragmacpndefinition::OntologyDocument.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_pragmacpndefinition::ontologydocument_has_iri():
    assert hasattr(pragmacpndefinition::OntologyDocument, "iri")
    descriptor = None
    for klass in pragmacpndefinition::OntologyDocument.__mro__:
        if "iri" in klass.__dict__:
            descriptor = klass.__dict__["iri"]
            break
    assert isinstance(descriptor, property)



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_pragmacpndefinition::pragmaticsontology_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition::PragmaticsOntology)


def test_pragmacpndefinition::pragmaticsontology_constructor_exists():
    assert callable(pragmacpndefinition::PragmaticsOntology.__init__)


def test_pragmacpndefinition::pragmaticsontology_constructor_args():
    sig = inspect.signature(pragmacpndefinition::PragmaticsOntology.__init__)
    params = list(sig.parameters.keys())
    assert "manager" in params, "Missing parameter 'manager'"

def test_pragmacpndefinition::pragmaticsontology_has_manager():
    assert hasattr(pragmacpndefinition::PragmaticsOntology, "manager")
    descriptor = None
    for klass in pragmacpndefinition::PragmaticsOntology.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)



def test_pragmacpndefinition::pragma_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition::Pragma)


def test_pragmacpndefinition::pragma_constructor_exists():
    assert callable(pragmacpndefinition::Pragma.__init__)


def test_pragmacpndefinition::pragma_constructor_args():
    sig = inspect.signature(pragmacpndefinition::Pragma.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_pragmacpndefinition::pragma_has_text():
    assert hasattr(pragmacpndefinition::Pragma, "text")
    descriptor = None
    for klass in pragmacpndefinition::Pragma.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_ontologymember_is_not_abstract():
    assert not inspect.isabstract(OntologyMember)


def test_ontologymember_constructor_exists():
    assert callable(OntologyMember.__init__)


def test_ontologymember_constructor_args():
    sig = inspect.signature(OntologyMember.__init__)
    params = list(sig.parameters.keys())



def test_pragmacpndefinition::transition_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition::Transition)


def test_pragmacpndefinition::transition_constructor_exists():
    assert callable(pragmacpndefinition::Transition.__init__)


def test_pragmacpndefinition::transition_constructor_args():
    sig = inspect.signature(pragmacpndefinition::Transition.__init__)
    params = list(sig.parameters.keys())



def test_pragmacpndefinition::arc_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition::Arc)


def test_pragmacpndefinition::arc_constructor_exists():
    assert callable(pragmacpndefinition::Arc.__init__)


def test_pragmacpndefinition::arc_constructor_args():
    sig = inspect.signature(pragmacpndefinition::Arc.__init__)
    params = list(sig.parameters.keys())



def test_pragmacpndefinition::page_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition::Page)


def test_pragmacpndefinition::page_constructor_exists():
    assert callable(pragmacpndefinition::Page.__init__)


def test_pragmacpndefinition::page_constructor_args():
    sig = inspect.signature(pragmacpndefinition::Page.__init__)
    params = list(sig.parameters.keys())



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_pragmacpndefinition::place_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition::Place)


def test_pragmacpndefinition::place_constructor_exists():
    assert callable(pragmacpndefinition::Place.__init__)


def test_pragmacpndefinition::place_constructor_args():
    sig = inspect.signature(pragmacpndefinition::Place.__init__)
    params = list(sig.parameters.keys())



def test_cpn_is_not_abstract():
    assert not inspect.isabstract(CPN)


def test_cpn_constructor_exists():
    assert callable(CPN.__init__)


def test_cpn_constructor_args():
    sig = inspect.signature(CPN.__init__)
    params = list(sig.parameters.keys())



def test_pragmacpndefinition::pragmacpn_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition::PragmaCPN)


def test_pragmacpndefinition::pragmacpn_constructor_exists():
    assert callable(pragmacpndefinition::PragmaCPN.__init__)


def test_pragmacpndefinition::pragmacpn_constructor_args():
    sig = inspect.signature(pragmacpndefinition::PragmaCPN.__init__)
    params = list(sig.parameters.keys())



def test_pragmacpndefinition::petrinet_is_not_abstract():
    assert not inspect.isabstract(pragmacpndefinition::PetriNet)


def test_pragmacpndefinition::petrinet_constructor_exists():
    assert callable(pragmacpndefinition::PetriNet.__init__)


def test_pragmacpndefinition::petrinet_constructor_args():
    sig = inspect.signature(pragmacpndefinition::PetriNet.__init__)
    params = list(sig.parameters.keys())


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
Page_strategy = st.builds(
    Page,
)
Arc_strategy = st.builds(
    Arc,
)
Transition_strategy = st.builds(
    Transition,
)
pragmacpndefinition::OntologyMember_strategy = st.builds(
    pragmacpndefinition::OntologyMember,
)
PetriNet_strategy = st.builds(
    PetriNet,
)
pragmacpndefinition::OntologyDocument_strategy = st.builds(
    pragmacpndefinition::OntologyDocument,
    path=
        safe_text,
    iri=
        safe_text
)
Label_strategy = st.builds(
    Label,
)
pragmacpndefinition::PragmaticsOntology_strategy = st.builds(
    pragmacpndefinition::PragmaticsOntology,
    manager=
        safe_text
)
pragmacpndefinition::Pragma_strategy = st.builds(
    pragmacpndefinition::Pragma,
    text=
        safe_text
)
OntologyMember_strategy = st.builds(
    OntologyMember,
)
pragmacpndefinition::Transition_strategy = st.builds(
    pragmacpndefinition::Transition,
)
pragmacpndefinition::Arc_strategy = st.builds(
    pragmacpndefinition::Arc,
)
pragmacpndefinition::Page_strategy = st.builds(
    pragmacpndefinition::Page,
)
Place_strategy = st.builds(
    Place,
)
pragmacpndefinition::Place_strategy = st.builds(
    pragmacpndefinition::Place,
)
CPN_strategy = st.builds(
    CPN,
)
pragmacpndefinition::PragmaCPN_strategy = st.builds(
    pragmacpndefinition::PragmaCPN,
)
pragmacpndefinition::PetriNet_strategy = st.builds(
    pragmacpndefinition::PetriNet,
)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=pragmacpndefinition::OntologyMember_strategy)
@settings(max_examples=50)
def test_pragmacpndefinition::ontologymember_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition::OntologyMember)

@given(instance=PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet)

@given(instance=pragmacpndefinition::OntologyDocument_strategy)
@settings(max_examples=50)
def test_pragmacpndefinition::ontologydocument_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition::OntologyDocument)

@given(instance=pragmacpndefinition::OntologyDocument_strategy)
def test_pragmacpndefinition::ontologydocument_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=pragmacpndefinition::OntologyDocument_strategy)
def test_pragmacpndefinition::ontologydocument_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=pragmacpndefinition::OntologyDocument_strategy)
def test_pragmacpndefinition::ontologydocument_iri_type(instance):
    assert isinstance(instance.iri, str)


@given(instance=pragmacpndefinition::OntologyDocument_strategy)
def test_pragmacpndefinition::ontologydocument_iri_setter(instance):
    original = instance.iri
    instance.iri = original
    assert instance.iri == original

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=pragmacpndefinition::PragmaticsOntology_strategy)
@settings(max_examples=50)
def test_pragmacpndefinition::pragmaticsontology_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition::PragmaticsOntology)

@given(instance=pragmacpndefinition::PragmaticsOntology_strategy)
def test_pragmacpndefinition::pragmaticsontology_manager_type(instance):
    assert isinstance(instance.manager, str)


@given(instance=pragmacpndefinition::PragmaticsOntology_strategy)
def test_pragmacpndefinition::pragmaticsontology_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pragmacpndefinition::PragmaticsOntology_strategy)
@settings(max_examples=30)
def test_pragmacpndefinition::pragmaticsontology_addontologyfromfile_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addOntologyFromFile(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addOntologyFromFile).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addOntologyFromFile' in pragmacpndefinition::PragmaticsOntology is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addOntologyFromFile' in pragmacpndefinition::PragmaticsOntology did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addOntologyFromFile' in pragmacpndefinition::PragmaticsOntology is not implemented or raised an error")

@given(instance=pragmacpndefinition::Pragma_strategy)
@settings(max_examples=50)
def test_pragmacpndefinition::pragma_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition::Pragma)

@given(instance=pragmacpndefinition::Pragma_strategy)
def test_pragmacpndefinition::pragma_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=pragmacpndefinition::Pragma_strategy)
def test_pragmacpndefinition::pragma_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=OntologyMember_strategy)
@settings(max_examples=50)
def test_ontologymember_instantiation(instance):
    assert isinstance(instance, OntologyMember)

@given(instance=pragmacpndefinition::Transition_strategy)
@settings(max_examples=50)
def test_pragmacpndefinition::transition_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition::Transition)

@given(instance=pragmacpndefinition::Arc_strategy)
@settings(max_examples=50)
def test_pragmacpndefinition::arc_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition::Arc)

@given(instance=pragmacpndefinition::Page_strategy)
@settings(max_examples=50)
def test_pragmacpndefinition::page_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition::Page)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=pragmacpndefinition::Place_strategy)
@settings(max_examples=50)
def test_pragmacpndefinition::place_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition::Place)

@given(instance=CPN_strategy)
@settings(max_examples=50)
def test_cpn_instantiation(instance):
    assert isinstance(instance, CPN)

@given(instance=pragmacpndefinition::PragmaCPN_strategy)
@settings(max_examples=50)
def test_pragmacpndefinition::pragmacpn_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition::PragmaCPN)

@given(instance=pragmacpndefinition::PetriNet_strategy)
@settings(max_examples=50)
def test_pragmacpndefinition::petrinet_instantiation(instance):
    assert isinstance(instance, pragmacpndefinition::PetriNet)
