import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinet::Reseau,
    petrinet::Arc,
    petrinet::Element,
    ArcSortant,
    petrinet::ReadArc,
    Arc,
    petrinet::ArcEntrant,
    petrinet::ArcSortant,
    Element,
    petrinet::Transition,
    petrinet::Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::reseau_is_not_abstract():
    assert not inspect.isabstract(petrinet::Reseau)


def test_petrinet::reseau_constructor_exists():
    assert callable(petrinet::Reseau.__init__)


def test_petrinet::reseau_constructor_args():
    sig = inspect.signature(petrinet::Reseau.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_petrinet::reseau_has_nom():
    assert hasattr(petrinet::Reseau, "nom")
    descriptor = None
    for klass in petrinet::Reseau.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petrinet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petrinet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "nbJetons" in params, "Missing parameter 'nbJetons'"

def test_petrinet::arc_has_nbJetons():
    assert hasattr(petrinet::Arc, "nbJetons")
    descriptor = None
    for klass in petrinet::Arc.__mro__:
        if "nbJetons" in klass.__dict__:
            descriptor = klass.__dict__["nbJetons"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::element_is_not_abstract():
    assert not inspect.isabstract(petrinet::Element)


def test_petrinet::element_constructor_exists():
    assert callable(petrinet::Element.__init__)


def test_petrinet::element_constructor_args():
    sig = inspect.signature(petrinet::Element.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_petrinet::element_has_nom():
    assert hasattr(petrinet::Element, "nom")
    descriptor = None
    for klass in petrinet::Element.__mro__:
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



def test_petrinet::readarc_is_not_abstract():
    assert not inspect.isabstract(petrinet::ReadArc)


def test_petrinet::readarc_constructor_exists():
    assert callable(petrinet::ReadArc.__init__)


def test_petrinet::readarc_constructor_args():
    sig = inspect.signature(petrinet::ReadArc.__init__)
    params = list(sig.parameters.keys())



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arcentrant_is_not_abstract():
    assert not inspect.isabstract(petrinet::ArcEntrant)


def test_petrinet::arcentrant_constructor_exists():
    assert callable(petrinet::ArcEntrant.__init__)


def test_petrinet::arcentrant_constructor_args():
    sig = inspect.signature(petrinet::ArcEntrant.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arcsortant_is_not_abstract():
    assert not inspect.isabstract(petrinet::ArcSortant)


def test_petrinet::arcsortant_constructor_exists():
    assert callable(petrinet::ArcSortant.__init__)


def test_petrinet::arcsortant_constructor_args():
    sig = inspect.signature(petrinet::ArcSortant.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petrinet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petrinet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "jetons" in params, "Missing parameter 'jetons'"

def test_petrinet::place_has_jetons():
    assert hasattr(petrinet::Place, "jetons")
    descriptor = None
    for klass in petrinet::Place.__mro__:
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
petrinet::Reseau_strategy = st.builds(
    petrinet::Reseau,
    nom=
        safe_text
)
petrinet::Arc_strategy = st.builds(
    petrinet::Arc,
    nbJetons=
        st.integers()
)
petrinet::Element_strategy = st.builds(
    petrinet::Element,
    nom=
        safe_text
)
ArcSortant_strategy = st.builds(
    ArcSortant,
)
petrinet::ReadArc_strategy = st.builds(
    petrinet::ReadArc,
)
Arc_strategy = st.builds(
    Arc,
)
petrinet::ArcEntrant_strategy = st.builds(
    petrinet::ArcEntrant,
)
petrinet::ArcSortant_strategy = st.builds(
    petrinet::ArcSortant,
)
Element_strategy = st.builds(
    Element,
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
)
petrinet::Place_strategy = st.builds(
    petrinet::Place,
    jetons=
        st.integers()
)

@given(instance=petrinet::Reseau_strategy)
@settings(max_examples=50)
def test_petrinet::reseau_instantiation(instance):
    assert isinstance(instance, petrinet::Reseau)

@given(instance=petrinet::Reseau_strategy)
def test_petrinet::reseau_nom_type(instance):
    assert isinstance(instance.nom, str)


@given(instance=petrinet::Reseau_strategy)
def test_petrinet::reseau_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=petrinet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petrinet::Arc)

@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_nbJetons_type(instance):
    assert isinstance(instance.nbJetons, int)


@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_nbJetons_setter(instance):
    original = instance.nbJetons
    instance.nbJetons = original
    assert instance.nbJetons == original

@given(instance=petrinet::Element_strategy)
@settings(max_examples=50)
def test_petrinet::element_instantiation(instance):
    assert isinstance(instance, petrinet::Element)

@given(instance=petrinet::Element_strategy)
def test_petrinet::element_nom_type(instance):
    assert isinstance(instance.nom, str)


@given(instance=petrinet::Element_strategy)
def test_petrinet::element_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=ArcSortant_strategy)
@settings(max_examples=50)
def test_arcsortant_instantiation(instance):
    assert isinstance(instance, ArcSortant)

@given(instance=petrinet::ReadArc_strategy)
@settings(max_examples=50)
def test_petrinet::readarc_instantiation(instance):
    assert isinstance(instance, petrinet::ReadArc)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petrinet::ArcEntrant_strategy)
@settings(max_examples=50)
def test_petrinet::arcentrant_instantiation(instance):
    assert isinstance(instance, petrinet::ArcEntrant)

@given(instance=petrinet::ArcSortant_strategy)
@settings(max_examples=50)
def test_petrinet::arcsortant_instantiation(instance):
    assert isinstance(instance, petrinet::ArcSortant)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petrinet::Transition)

@given(instance=petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petrinet::Place)

@given(instance=petrinet::Place_strategy)
def test_petrinet::place_jetons_type(instance):
    assert isinstance(instance.jetons, int)


@given(instance=petrinet::Place_strategy)
def test_petrinet::place_jetons_setter(instance):
    original = instance.jetons
    instance.jetons = original
    assert instance.jetons == original
