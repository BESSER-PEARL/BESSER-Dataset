import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TPArc,
    PTArc,
    PetriNet,
    GenericPT,
    PetriNetMM2::Transition,
    PetriNetMM2::Place,
    PetriNetModel,
    PetriNetMM2::PetriNetModelElement,
    PetriNetModelElement,
    PetriNetMM2::GenericPT,
    PetriNetMM2::Arc,
    PetriNetMM2::PetriNetModel,
    Arc,
    PetriNetMM2::PTArc,
    PetriNetMM2::TPArc,
    Transition,
    Place,
    PetriNetMM2::PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tparc_is_not_abstract():
    assert not inspect.isabstract(TPArc)


def test_tparc_constructor_exists():
    assert callable(TPArc.__init__)


def test_tparc_constructor_args():
    sig = inspect.signature(TPArc.__init__)
    params = list(sig.parameters.keys())



def test_ptarc_is_not_abstract():
    assert not inspect.isabstract(PTArc)


def test_ptarc_constructor_exists():
    assert callable(PTArc.__init__)


def test_ptarc_constructor_args():
    sig = inspect.signature(PTArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet)


def test_petrinet_constructor_exists():
    assert callable(PetriNet.__init__)


def test_petrinet_constructor_args():
    sig = inspect.signature(PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_genericpt_is_not_abstract():
    assert not inspect.isabstract(GenericPT)


def test_genericpt_constructor_exists():
    assert callable(GenericPT.__init__)


def test_genericpt_constructor_args():
    sig = inspect.signature(GenericPT.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmm2::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNetMM2::Transition)


def test_petrinetmm2::transition_constructor_exists():
    assert callable(PetriNetMM2::Transition.__init__)


def test_petrinetmm2::transition_constructor_args():
    sig = inspect.signature(PetriNetMM2::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "relevance" in params, "Missing parameter 'relevance'"

def test_petrinetmm2::transition_has_name():
    assert hasattr(PetriNetMM2::Transition, "name")
    descriptor = None
    for klass in PetriNetMM2::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetmm2::transition_has_relevance():
    assert hasattr(PetriNetMM2::Transition, "relevance")
    descriptor = None
    for klass in PetriNetMM2::Transition.__mro__:
        if "relevance" in klass.__dict__:
            descriptor = klass.__dict__["relevance"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmm2::place_is_not_abstract():
    assert not inspect.isabstract(PetriNetMM2::Place)


def test_petrinetmm2::place_constructor_exists():
    assert callable(PetriNetMM2::Place.__init__)


def test_petrinetmm2::place_constructor_args():
    sig = inspect.signature(PetriNetMM2::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "relevance" in params, "Missing parameter 'relevance'"

def test_petrinetmm2::place_has_name():
    assert hasattr(PetriNetMM2::Place, "name")
    descriptor = None
    for klass in PetriNetMM2::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetmm2::place_has_relevance():
    assert hasattr(PetriNetMM2::Place, "relevance")
    descriptor = None
    for klass in PetriNetMM2::Place.__mro__:
        if "relevance" in klass.__dict__:
            descriptor = klass.__dict__["relevance"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmodel_is_not_abstract():
    assert not inspect.isabstract(PetriNetModel)


def test_petrinetmodel_constructor_exists():
    assert callable(PetriNetModel.__init__)


def test_petrinetmodel_constructor_args():
    sig = inspect.signature(PetriNetModel.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmm2::petrinetmodelelement_is_not_abstract():
    assert not inspect.isabstract(PetriNetMM2::PetriNetModelElement)


def test_petrinetmm2::petrinetmodelelement_constructor_exists():
    assert callable(PetriNetMM2::PetriNetModelElement.__init__)


def test_petrinetmm2::petrinetmodelelement_constructor_args():
    sig = inspect.signature(PetriNetMM2::PetriNetModelElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmodelelement_is_not_abstract():
    assert not inspect.isabstract(PetriNetModelElement)


def test_petrinetmodelelement_constructor_exists():
    assert callable(PetriNetModelElement.__init__)


def test_petrinetmodelelement_constructor_args():
    sig = inspect.signature(PetriNetModelElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmm2::genericpt_is_not_abstract():
    assert not inspect.isabstract(PetriNetMM2::GenericPT)


def test_petrinetmm2::genericpt_constructor_exists():
    assert callable(PetriNetMM2::GenericPT.__init__)


def test_petrinetmm2::genericpt_constructor_args():
    sig = inspect.signature(PetriNetMM2::GenericPT.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_petrinetmm2::genericpt_has_label():
    assert hasattr(PetriNetMM2::GenericPT, "label")
    descriptor = None
    for klass in PetriNetMM2::GenericPT.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmm2::arc_is_not_abstract():
    assert not inspect.isabstract(PetriNetMM2::Arc)


def test_petrinetmm2::arc_constructor_exists():
    assert callable(PetriNetMM2::Arc.__init__)


def test_petrinetmm2::arc_constructor_args():
    sig = inspect.signature(PetriNetMM2::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinetmm2::arc_has_weight():
    assert hasattr(PetriNetMM2::Arc, "weight")
    descriptor = None
    for klass in PetriNetMM2::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinetmm2::petrinetmodel_is_not_abstract():
    assert not inspect.isabstract(PetriNetMM2::PetriNetModel)


def test_petrinetmm2::petrinetmodel_constructor_exists():
    assert callable(PetriNetMM2::PetriNetModel.__init__)


def test_petrinetmm2::petrinetmodel_constructor_args():
    sig = inspect.signature(PetriNetMM2::PetriNetModel.__init__)
    params = list(sig.parameters.keys())



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmm2::ptarc_is_not_abstract():
    assert not inspect.isabstract(PetriNetMM2::PTArc)


def test_petrinetmm2::ptarc_constructor_exists():
    assert callable(PetriNetMM2::PTArc.__init__)


def test_petrinetmm2::ptarc_constructor_args():
    sig = inspect.signature(PetriNetMM2::PTArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmm2::tparc_is_not_abstract():
    assert not inspect.isabstract(PetriNetMM2::TPArc)


def test_petrinetmm2::tparc_constructor_exists():
    assert callable(PetriNetMM2::TPArc.__init__)


def test_petrinetmm2::tparc_constructor_args():
    sig = inspect.signature(PetriNetMM2::TPArc.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmm2::petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNetMM2::PetriNet)


def test_petrinetmm2::petrinet_constructor_exists():
    assert callable(PetriNetMM2::PetriNet.__init__)


def test_petrinetmm2::petrinet_constructor_args():
    sig = inspect.signature(PetriNetMM2::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetmm2::petrinet_has_name():
    assert hasattr(PetriNetMM2::PetriNet, "name")
    descriptor = None
    for klass in PetriNetMM2::PetriNet.__mro__:
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
TPArc_strategy = st.builds(
    TPArc,
)
PTArc_strategy = st.builds(
    PTArc,
)
PetriNet_strategy = st.builds(
    PetriNet,
)
GenericPT_strategy = st.builds(
    GenericPT,
)
PetriNetMM2::Transition_strategy = st.builds(
    PetriNetMM2::Transition,
    name=
        safe_text,
    relevance=
        st.integers()
)
PetriNetMM2::Place_strategy = st.builds(
    PetriNetMM2::Place,
    name=
        safe_text,
    relevance=
        st.integers()
)
PetriNetModel_strategy = st.builds(
    PetriNetModel,
)
PetriNetMM2::PetriNetModelElement_strategy = st.builds(
    PetriNetMM2::PetriNetModelElement,
)
PetriNetModelElement_strategy = st.builds(
    PetriNetModelElement,
)
PetriNetMM2::GenericPT_strategy = st.builds(
    PetriNetMM2::GenericPT,
    label=
        safe_text
)
PetriNetMM2::Arc_strategy = st.builds(
    PetriNetMM2::Arc,
    weight=
        st.integers()
)
PetriNetMM2::PetriNetModel_strategy = st.builds(
    PetriNetMM2::PetriNetModel,
)
Arc_strategy = st.builds(
    Arc,
)
PetriNetMM2::PTArc_strategy = st.builds(
    PetriNetMM2::PTArc,
)
PetriNetMM2::TPArc_strategy = st.builds(
    PetriNetMM2::TPArc,
)
Transition_strategy = st.builds(
    Transition,
)
Place_strategy = st.builds(
    Place,
)
PetriNetMM2::PetriNet_strategy = st.builds(
    PetriNetMM2::PetriNet,
    name=
        safe_text
)

@given(instance=TPArc_strategy)
@settings(max_examples=50)
def test_tparc_instantiation(instance):
    assert isinstance(instance, TPArc)

@given(instance=PTArc_strategy)
@settings(max_examples=50)
def test_ptarc_instantiation(instance):
    assert isinstance(instance, PTArc)

@given(instance=PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet)

@given(instance=GenericPT_strategy)
@settings(max_examples=50)
def test_genericpt_instantiation(instance):
    assert isinstance(instance, GenericPT)

@given(instance=PetriNetMM2::Transition_strategy)
@settings(max_examples=50)
def test_petrinetmm2::transition_instantiation(instance):
    assert isinstance(instance, PetriNetMM2::Transition)

@given(instance=PetriNetMM2::Transition_strategy)
def test_petrinetmm2::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNetMM2::Transition_strategy)
def test_petrinetmm2::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNetMM2::Transition_strategy)
def test_petrinetmm2::transition_relevance_type(instance):
    assert isinstance(instance.relevance, int)


@given(instance=PetriNetMM2::Transition_strategy)
def test_petrinetmm2::transition_relevance_setter(instance):
    original = instance.relevance
    instance.relevance = original
    assert instance.relevance == original

@given(instance=PetriNetMM2::Place_strategy)
@settings(max_examples=50)
def test_petrinetmm2::place_instantiation(instance):
    assert isinstance(instance, PetriNetMM2::Place)

@given(instance=PetriNetMM2::Place_strategy)
def test_petrinetmm2::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNetMM2::Place_strategy)
def test_petrinetmm2::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNetMM2::Place_strategy)
def test_petrinetmm2::place_relevance_type(instance):
    assert isinstance(instance.relevance, int)


@given(instance=PetriNetMM2::Place_strategy)
def test_petrinetmm2::place_relevance_setter(instance):
    original = instance.relevance
    instance.relevance = original
    assert instance.relevance == original

@given(instance=PetriNetModel_strategy)
@settings(max_examples=50)
def test_petrinetmodel_instantiation(instance):
    assert isinstance(instance, PetriNetModel)

@given(instance=PetriNetMM2::PetriNetModelElement_strategy)
@settings(max_examples=50)
def test_petrinetmm2::petrinetmodelelement_instantiation(instance):
    assert isinstance(instance, PetriNetMM2::PetriNetModelElement)

@given(instance=PetriNetModelElement_strategy)
@settings(max_examples=50)
def test_petrinetmodelelement_instantiation(instance):
    assert isinstance(instance, PetriNetModelElement)

@given(instance=PetriNetMM2::GenericPT_strategy)
@settings(max_examples=50)
def test_petrinetmm2::genericpt_instantiation(instance):
    assert isinstance(instance, PetriNetMM2::GenericPT)

@given(instance=PetriNetMM2::GenericPT_strategy)
def test_petrinetmm2::genericpt_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=PetriNetMM2::GenericPT_strategy)
def test_petrinetmm2::genericpt_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=PetriNetMM2::Arc_strategy)
@settings(max_examples=50)
def test_petrinetmm2::arc_instantiation(instance):
    assert isinstance(instance, PetriNetMM2::Arc)

@given(instance=PetriNetMM2::Arc_strategy)
def test_petrinetmm2::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=PetriNetMM2::Arc_strategy)
def test_petrinetmm2::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=PetriNetMM2::PetriNetModel_strategy)
@settings(max_examples=50)
def test_petrinetmm2::petrinetmodel_instantiation(instance):
    assert isinstance(instance, PetriNetMM2::PetriNetModel)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PetriNetMM2::PTArc_strategy)
@settings(max_examples=50)
def test_petrinetmm2::ptarc_instantiation(instance):
    assert isinstance(instance, PetriNetMM2::PTArc)

@given(instance=PetriNetMM2::TPArc_strategy)
@settings(max_examples=50)
def test_petrinetmm2::tparc_instantiation(instance):
    assert isinstance(instance, PetriNetMM2::TPArc)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=PetriNetMM2::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinetmm2::petrinet_instantiation(instance):
    assert isinstance(instance, PetriNetMM2::PetriNet)

@given(instance=PetriNetMM2::PetriNet_strategy)
def test_petrinetmm2::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNetMM2::PetriNet_strategy)
def test_petrinetmm2::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
