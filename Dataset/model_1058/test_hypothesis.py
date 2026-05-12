import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PlaceToTransArc,
    TransToPlaceArc,
    Arc,
    PetriNet_TransToPlaceArc,
    PetriNet_PlaceToTransArc,
    PetriNet_Arc,
    PetriNet,
    Transition,
    Place,
    Element,
    PetriNet_Transition,
    PetriNet_Place,
    PetriNet_PetriNet,
    PetriNet_Element,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_placetotransarc_is_not_abstract():
    assert not inspect.isabstract(PlaceToTransArc)


def test_placetotransarc_constructor_exists():
    assert callable(PlaceToTransArc.__init__)


def test_placetotransarc_constructor_args():
    sig = inspect.signature(PlaceToTransArc.__init__)
    params = list(sig.parameters.keys())



def test_transtoplacearc_is_not_abstract():
    assert not inspect.isabstract(TransToPlaceArc)


def test_transtoplacearc_constructor_exists():
    assert callable(TransToPlaceArc.__init__)


def test_transtoplacearc_constructor_args():
    sig = inspect.signature(TransToPlaceArc.__init__)
    params = list(sig.parameters.keys())



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transtoplacearc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_TransToPlaceArc)


def test_petrinet_transtoplacearc_constructor_exists():
    assert callable(PetriNet_TransToPlaceArc.__init__)


def test_petrinet_transtoplacearc_constructor_args():
    sig = inspect.signature(PetriNet_TransToPlaceArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_placetotransarc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PlaceToTransArc)


def test_petrinet_placetotransarc_constructor_exists():
    assert callable(PetriNet_PlaceToTransArc.__init__)


def test_petrinet_placetotransarc_constructor_args():
    sig = inspect.signature(PetriNet_PlaceToTransArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(PetriNet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(PetriNet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet_arc_has_weight():
    assert hasattr(PetriNet_Arc, "weight")
    descriptor = None
    for klass in PetriNet_Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet)


def test_petrinet_constructor_exists():
    assert callable(PetriNet.__init__)


def test_petrinet_constructor_args():
    sig = inspect.signature(PetriNet.__init__)
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



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(PetriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(PetriNet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(PetriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(PetriNet_Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PetriNet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(PetriNet_PetriNet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(PetriNet_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_element_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Element)


def test_petrinet_element_constructor_exists():
    assert callable(PetriNet_Element.__init__)


def test_petrinet_element_constructor_args():
    sig = inspect.signature(PetriNet_Element.__init__)
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
PlaceToTransArc_strategy = st.builds(
    PlaceToTransArc,
)
TransToPlaceArc_strategy = st.builds(
    TransToPlaceArc,
)
Arc_strategy = st.builds(
    Arc,
)
PetriNet_TransToPlaceArc_strategy = st.builds(
    PetriNet_TransToPlaceArc,
)
PetriNet_PlaceToTransArc_strategy = st.builds(
    PetriNet_PlaceToTransArc,
)
PetriNet_Arc_strategy = st.builds(
    PetriNet_Arc,
    weight=
        safe_text
)
PetriNet_strategy = st.builds(
    PetriNet,
)
Transition_strategy = st.builds(
    Transition,
)
Place_strategy = st.builds(
    Place,
)
Element_strategy = st.builds(
    Element,
)
PetriNet_Transition_strategy = st.builds(
    PetriNet_Transition,
)
PetriNet_Place_strategy = st.builds(
    PetriNet_Place,
)
PetriNet_PetriNet_strategy = st.builds(
    PetriNet_PetriNet,
)
PetriNet_Element_strategy = st.builds(
    PetriNet_Element,
)

@given(instance=PlaceToTransArc_strategy)
@settings(max_examples=50)
def test_placetotransarc_instantiation(instance):
    assert isinstance(instance, PlaceToTransArc)

@given(instance=TransToPlaceArc_strategy)
@settings(max_examples=50)
def test_transtoplacearc_instantiation(instance):
    assert isinstance(instance, TransToPlaceArc)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PetriNet_TransToPlaceArc_strategy)
@settings(max_examples=50)
def test_petrinet_transtoplacearc_instantiation(instance):
    assert isinstance(instance, PetriNet_TransToPlaceArc)

@given(instance=PetriNet_PlaceToTransArc_strategy)
@settings(max_examples=50)
def test_petrinet_placetotransarc_instantiation(instance):
    assert isinstance(instance, PetriNet_PlaceToTransArc)

@given(instance=PetriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, PetriNet_Arc)



@given(instance=PetriNet_Arc_strategy)
def test_petrinet_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=PetriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, PetriNet_Transition)

@given(instance=PetriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, PetriNet_Place)

@given(instance=PetriNet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet_PetriNet)

@given(instance=PetriNet_Element_strategy)
@settings(max_examples=50)
def test_petrinet_element_instantiation(instance):
    assert isinstance(instance, PetriNet_Element)
