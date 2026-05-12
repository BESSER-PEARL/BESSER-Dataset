import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Arc,
    petrinet::Arc,
    Attribute,
    petrinet::Identity,
    petrinet::Animation,
    StructuredLabel,
    petrinet::AnimationLabel,
    Label,
    petrinet::InputPlace,
    petrinet::Token,
    petrinet::GeometryLabel,
    Place,
    petrinet::Place,
    PetriNetType,
    petrinet::ExtendedPetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petrinet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petrinet::Arc.__init__)
    params = list(sig.parameters.keys())



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::identity_is_not_abstract():
    assert not inspect.isabstract(petrinet::Identity)


def test_petrinet::identity_constructor_exists():
    assert callable(petrinet::Identity.__init__)


def test_petrinet::identity_constructor_args():
    sig = inspect.signature(petrinet::Identity.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_petrinet::identity_has_text():
    assert hasattr(petrinet::Identity, "text")
    descriptor = None
    for klass in petrinet::Identity.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::animation_is_not_abstract():
    assert not inspect.isabstract(petrinet::Animation)


def test_petrinet::animation_constructor_exists():
    assert callable(petrinet::Animation.__init__)


def test_petrinet::animation_constructor_args():
    sig = inspect.signature(petrinet::Animation.__init__)
    params = list(sig.parameters.keys())



def test_structuredlabel_is_not_abstract():
    assert not inspect.isabstract(StructuredLabel)


def test_structuredlabel_constructor_exists():
    assert callable(StructuredLabel.__init__)


def test_structuredlabel_constructor_args():
    sig = inspect.signature(StructuredLabel.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::animationlabel_is_not_abstract():
    assert not inspect.isabstract(petrinet::AnimationLabel)


def test_petrinet::animationlabel_constructor_exists():
    assert callable(petrinet::AnimationLabel.__init__)


def test_petrinet::animationlabel_constructor_args():
    sig = inspect.signature(petrinet::AnimationLabel.__init__)
    params = list(sig.parameters.keys())



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::inputplace_is_not_abstract():
    assert not inspect.isabstract(petrinet::InputPlace)


def test_petrinet::inputplace_constructor_exists():
    assert callable(petrinet::InputPlace.__init__)


def test_petrinet::inputplace_constructor_args():
    sig = inspect.signature(petrinet::InputPlace.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_petrinet::inputplace_has_text():
    assert hasattr(petrinet::InputPlace, "text")
    descriptor = None
    for klass in petrinet::InputPlace.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::token_is_not_abstract():
    assert not inspect.isabstract(petrinet::Token)


def test_petrinet::token_constructor_exists():
    assert callable(petrinet::Token.__init__)


def test_petrinet::token_constructor_args():
    sig = inspect.signature(petrinet::Token.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_petrinet::token_has_text():
    assert hasattr(petrinet::Token, "text")
    descriptor = None
    for klass in petrinet::Token.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::geometrylabel_is_not_abstract():
    assert not inspect.isabstract(petrinet::GeometryLabel)


def test_petrinet::geometrylabel_constructor_exists():
    assert callable(petrinet::GeometryLabel.__init__)


def test_petrinet::geometrylabel_constructor_args():
    sig = inspect.signature(petrinet::GeometryLabel.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_petrinet::geometrylabel_has_text():
    assert hasattr(petrinet::GeometryLabel, "text")
    descriptor = None
    for klass in petrinet::GeometryLabel.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petrinet::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinettype_is_not_abstract():
    assert not inspect.isabstract(PetriNetType)


def test_petrinettype_constructor_exists():
    assert callable(PetriNetType.__init__)


def test_petrinettype_constructor_args():
    sig = inspect.signature(PetriNetType.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::extendedpetrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet::ExtendedPetriNet)


def test_petrinet::extendedpetrinet_constructor_exists():
    assert callable(petrinet::ExtendedPetriNet.__init__)


def test_petrinet::extendedpetrinet_constructor_args():
    sig = inspect.signature(petrinet::ExtendedPetriNet.__init__)
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
Arc_strategy = st.builds(
    Arc,
)
petrinet::Arc_strategy = st.builds(
    petrinet::Arc,
)
Attribute_strategy = st.builds(
    Attribute,
)
petrinet::Identity_strategy = st.builds(
    petrinet::Identity,
    text=
        safe_text
)
petrinet::Animation_strategy = st.builds(
    petrinet::Animation,
)
StructuredLabel_strategy = st.builds(
    StructuredLabel,
)
petrinet::AnimationLabel_strategy = st.builds(
    petrinet::AnimationLabel,
)
Label_strategy = st.builds(
    Label,
)
petrinet::InputPlace_strategy = st.builds(
    petrinet::InputPlace,
    text=
        st.booleans()
)
petrinet::Token_strategy = st.builds(
    petrinet::Token,
    text=
        safe_text
)
petrinet::GeometryLabel_strategy = st.builds(
    petrinet::GeometryLabel,
    text=
        safe_text
)
Place_strategy = st.builds(
    Place,
)
petrinet::Place_strategy = st.builds(
    petrinet::Place,
)
PetriNetType_strategy = st.builds(
    PetriNetType,
)
petrinet::ExtendedPetriNet_strategy = st.builds(
    petrinet::ExtendedPetriNet,
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petrinet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petrinet::Arc)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=petrinet::Identity_strategy)
@settings(max_examples=50)
def test_petrinet::identity_instantiation(instance):
    assert isinstance(instance, petrinet::Identity)

@given(instance=petrinet::Identity_strategy)
def test_petrinet::identity_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=petrinet::Identity_strategy)
def test_petrinet::identity_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=petrinet::Animation_strategy)
@settings(max_examples=50)
def test_petrinet::animation_instantiation(instance):
    assert isinstance(instance, petrinet::Animation)

@given(instance=StructuredLabel_strategy)
@settings(max_examples=50)
def test_structuredlabel_instantiation(instance):
    assert isinstance(instance, StructuredLabel)

@given(instance=petrinet::AnimationLabel_strategy)
@settings(max_examples=50)
def test_petrinet::animationlabel_instantiation(instance):
    assert isinstance(instance, petrinet::AnimationLabel)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=petrinet::InputPlace_strategy)
@settings(max_examples=50)
def test_petrinet::inputplace_instantiation(instance):
    assert isinstance(instance, petrinet::InputPlace)

@given(instance=petrinet::InputPlace_strategy)
def test_petrinet::inputplace_text_type(instance):
    assert isinstance(instance.text, bool)


@given(instance=petrinet::InputPlace_strategy)
def test_petrinet::inputplace_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=petrinet::Token_strategy)
@settings(max_examples=50)
def test_petrinet::token_instantiation(instance):
    assert isinstance(instance, petrinet::Token)

@given(instance=petrinet::Token_strategy)
def test_petrinet::token_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=petrinet::Token_strategy)
def test_petrinet::token_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=petrinet::GeometryLabel_strategy)
@settings(max_examples=50)
def test_petrinet::geometrylabel_instantiation(instance):
    assert isinstance(instance, petrinet::GeometryLabel)

@given(instance=petrinet::GeometryLabel_strategy)
def test_petrinet::geometrylabel_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=petrinet::GeometryLabel_strategy)
def test_petrinet::geometrylabel_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petrinet::Place)

@given(instance=PetriNetType_strategy)
@settings(max_examples=50)
def test_petrinettype_instantiation(instance):
    assert isinstance(instance, PetriNetType)

@given(instance=petrinet::ExtendedPetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::extendedpetrinet_instantiation(instance):
    assert isinstance(instance, petrinet::ExtendedPetriNet)
