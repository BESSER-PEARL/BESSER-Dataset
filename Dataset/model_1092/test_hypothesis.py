import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petrinet_Reseau,
    petrinet_Arc,
    petrinet_Element,
    ArcSortant,
    petrinet_ReadArc,
    Arc,
    petrinet_ArcEntrant,
    petrinet_ArcSortant,
    Element,
    petrinet_Transition,
    petrinet_Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet_reseau_is_not_abstract():
    assert not inspect.isabstract(petrinet_Reseau)


def test_petrinet_reseau_constructor_exists():
    assert callable(petrinet_Reseau.__init__)


def test_petrinet_reseau_constructor_args():
    sig = inspect.signature(petrinet_Reseau.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_petrinet_reseau_has_nom():
    assert hasattr(petrinet_Reseau, "nom")
    descriptor = None
    for klass in petrinet_Reseau.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petrinet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(petrinet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(petrinet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "nbJetons" in params, "Missing parameter 'nbJetons'"

def test_petrinet_arc_has_nbJetons():
    assert hasattr(petrinet_Arc, "nbJetons")
    descriptor = None
    for klass in petrinet_Arc.__mro__:
        if "nbJetons" in klass.__dict__:
            descriptor = klass.__dict__["nbJetons"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_element_is_not_abstract():
    assert not inspect.isabstract(petrinet_Element)


def test_petrinet_element_constructor_exists():
    assert callable(petrinet_Element.__init__)


def test_petrinet_element_constructor_args():
    sig = inspect.signature(petrinet_Element.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_petrinet_element_has_nom():
    assert hasattr(petrinet_Element, "nom")
    descriptor = None
    for klass in petrinet_Element.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_arcsortant_is_not_abstract():
    assert not inspect.isabstract(ArcSortant)


def test_arcsortant_constructor_exists():
    assert callable(ArcSortant.__init__)


def test_arcsortant_constructor_args():
    sig = inspect.signature(ArcSortant.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_readarc_is_not_abstract():
    assert not inspect.isabstract(petrinet_ReadArc)


def test_petrinet_readarc_constructor_exists():
    assert callable(petrinet_ReadArc.__init__)


def test_petrinet_readarc_constructor_args():
    sig = inspect.signature(petrinet_ReadArc.__init__)
    params = list(sig.parameters.keys())



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_arcentrant_is_not_abstract():
    assert not inspect.isabstract(petrinet_ArcEntrant)


def test_petrinet_arcentrant_constructor_exists():
    assert callable(petrinet_ArcEntrant.__init__)


def test_petrinet_arcentrant_constructor_args():
    sig = inspect.signature(petrinet_ArcEntrant.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_arcsortant_is_not_abstract():
    assert not inspect.isabstract(petrinet_ArcSortant)


def test_petrinet_arcsortant_constructor_exists():
    assert callable(petrinet_ArcSortant.__init__)


def test_petrinet_arcsortant_constructor_args():
    sig = inspect.signature(petrinet_ArcSortant.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petrinet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petrinet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petrinet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(petrinet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(petrinet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "jetons" in params, "Missing parameter 'jetons'"

def test_petrinet_place_has_jetons():
    assert hasattr(petrinet_Place, "jetons")
    descriptor = None
    for klass in petrinet_Place.__mro__:
        if "jetons" in klass.__dict__:
            descriptor = klass.__dict__["jetons"]
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
petrinet_Reseau_strategy = st.builds(
    petrinet_Reseau,
    nom=
        safe_text
)
petrinet_Arc_strategy = st.builds(
    petrinet_Arc,
    nbJetons=
        st.integers()
)
petrinet_Element_strategy = st.builds(
    petrinet_Element,
    nom=
        safe_text
)
ArcSortant_strategy = st.builds(
    ArcSortant,
)
petrinet_ReadArc_strategy = st.builds(
    petrinet_ReadArc,
)
Arc_strategy = st.builds(
    Arc,
)
petrinet_ArcEntrant_strategy = st.builds(
    petrinet_ArcEntrant,
)
petrinet_ArcSortant_strategy = st.builds(
    petrinet_ArcSortant,
)
Element_strategy = st.builds(
    Element,
)
petrinet_Transition_strategy = st.builds(
    petrinet_Transition,
)
petrinet_Place_strategy = st.builds(
    petrinet_Place,
    jetons=
        st.integers()
)

@given(instance=petrinet_Reseau_strategy)
@settings(max_examples=50)
def test_petrinet_reseau_instantiation(instance):
    assert isinstance(instance, petrinet_Reseau)



@given(instance=petrinet_Reseau_strategy)
def test_petrinet_reseau_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=petrinet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, petrinet_Arc)



@given(instance=petrinet_Arc_strategy)
def test_petrinet_arc_nbJetons_setter(instance):
    original = instance.nbJetons
    instance.nbJetons = original
    assert instance.nbJetons == original

@given(instance=petrinet_Element_strategy)
@settings(max_examples=50)
def test_petrinet_element_instantiation(instance):
    assert isinstance(instance, petrinet_Element)



@given(instance=petrinet_Element_strategy)
def test_petrinet_element_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=ArcSortant_strategy)
@settings(max_examples=50)
def test_arcsortant_instantiation(instance):
    assert isinstance(instance, ArcSortant)

@given(instance=petrinet_ReadArc_strategy)
@settings(max_examples=50)
def test_petrinet_readarc_instantiation(instance):
    assert isinstance(instance, petrinet_ReadArc)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petrinet_ArcEntrant_strategy)
@settings(max_examples=50)
def test_petrinet_arcentrant_instantiation(instance):
    assert isinstance(instance, petrinet_ArcEntrant)

@given(instance=petrinet_ArcSortant_strategy)
@settings(max_examples=50)
def test_petrinet_arcsortant_instantiation(instance):
    assert isinstance(instance, petrinet_ArcSortant)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=petrinet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petrinet_Transition)

@given(instance=petrinet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petrinet_Place)



@given(instance=petrinet_Place_strategy)
def test_petrinet_place_jetons_setter(instance):
    original = instance.jetons
    instance.jetons = original
    assert instance.jetons == original
