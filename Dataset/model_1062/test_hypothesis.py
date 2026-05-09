import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriNet::PrimitiveAttribute,
    PetriNet::Type,
    PetriNet::IdentifiableElement,
    Arc,
    PetriNet::TransToPlaceArc,
    PetriNet::PlaceToTransArc,
    PetriNet::Token,
    PetriNet::Arc,
    IdentifiableElement,
    PetriNet::Place,
    PetriNet::Transition,
    PetriNet::PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::primitiveattribute_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PrimitiveAttribute)


def test_petrinet::primitiveattribute_constructor_exists():
    assert callable(PetriNet::PrimitiveAttribute.__init__)


def test_petrinet::primitiveattribute_constructor_args():
    sig = inspect.signature(PetriNet::PrimitiveAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "primType" in params, "Missing parameter 'primType'"
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::primitiveattribute_has_primType():
    assert hasattr(PetriNet::PrimitiveAttribute, "primType")
    descriptor = None
    for klass in PetriNet::PrimitiveAttribute.__mro__:
        if "primType" in klass.__dict__:
            descriptor = klass.__dict__["primType"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::primitiveattribute_has_name():
    assert hasattr(PetriNet::PrimitiveAttribute, "name")
    descriptor = None
    for klass in PetriNet::PrimitiveAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::type_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Type)


def test_petrinet::type_constructor_exists():
    assert callable(PetriNet::Type.__init__)


def test_petrinet::type_constructor_args():
    sig = inspect.signature(PetriNet::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::type_has_name():
    assert hasattr(PetriNet::Type, "name")
    descriptor = None
    for klass in PetriNet::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::identifiableelement_is_not_abstract():
    assert not inspect.isabstract(PetriNet::IdentifiableElement)


def test_petrinet::identifiableelement_constructor_exists():
    assert callable(PetriNet::IdentifiableElement.__init__)


def test_petrinet::identifiableelement_constructor_args():
    sig = inspect.signature(PetriNet::IdentifiableElement.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::identifiableelement_has_author():
    assert hasattr(PetriNet::IdentifiableElement, "author")
    descriptor = None
    for klass in PetriNet::IdentifiableElement.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::identifiableelement_has_name():
    assert hasattr(PetriNet::IdentifiableElement, "name")
    descriptor = None
    for klass in PetriNet::IdentifiableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transtoplacearc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::TransToPlaceArc)


def test_petrinet::transtoplacearc_constructor_exists():
    assert callable(PetriNet::TransToPlaceArc.__init__)


def test_petrinet::transtoplacearc_constructor_args():
    sig = inspect.signature(PetriNet::TransToPlaceArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::placetotransarc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PlaceToTransArc)


def test_petrinet::placetotransarc_constructor_exists():
    assert callable(PetriNet::PlaceToTransArc.__init__)


def test_petrinet::placetotransarc_constructor_args():
    sig = inspect.signature(PetriNet::PlaceToTransArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::token_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Token)


def test_petrinet::token_constructor_exists():
    assert callable(PetriNet::Token.__init__)


def test_petrinet::token_constructor_args():
    sig = inspect.signature(PetriNet::Token.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_petrinet::token_has_values():
    assert hasattr(PetriNet::Token, "values")
    descriptor = None
    for klass in PetriNet::Token.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(PetriNet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(PetriNet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet::arc_has_weight():
    assert hasattr(PetriNet::Arc, "weight")
    descriptor = None
    for klass in PetriNet::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_identifiableelement_is_not_abstract():
    assert not inspect.isabstract(IdentifiableElement)


def test_identifiableelement_constructor_exists():
    assert callable(IdentifiableElement.__init__)


def test_identifiableelement_constructor_args():
    sig = inspect.signature(IdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(PetriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(PetriNet::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(PetriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(PetriNet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(PetriNet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(PetriNet::PetriNet.__init__)
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
PetriNet::PrimitiveAttribute_strategy = st.builds(
    PetriNet::PrimitiveAttribute,
    primType=
        safe_text,
    name=
        safe_text
)
PetriNet::Type_strategy = st.builds(
    PetriNet::Type,
    name=
        safe_text
)
PetriNet::IdentifiableElement_strategy = st.builds(
    PetriNet::IdentifiableElement,
    author=
        safe_text,
    name=
        safe_text
)
Arc_strategy = st.builds(
    Arc,
)
PetriNet::TransToPlaceArc_strategy = st.builds(
    PetriNet::TransToPlaceArc,
)
PetriNet::PlaceToTransArc_strategy = st.builds(
    PetriNet::PlaceToTransArc,
)
PetriNet::Token_strategy = st.builds(
    PetriNet::Token,
    values=
        safe_text
)
PetriNet::Arc_strategy = st.builds(
    PetriNet::Arc,
    weight=
        st.integers()
)
IdentifiableElement_strategy = st.builds(
    IdentifiableElement,
)
PetriNet::Place_strategy = st.builds(
    PetriNet::Place,
)
PetriNet::Transition_strategy = st.builds(
    PetriNet::Transition,
)
PetriNet::PetriNet_strategy = st.builds(
    PetriNet::PetriNet,
)

@given(instance=PetriNet::PrimitiveAttribute_strategy)
@settings(max_examples=50)
def test_petrinet::primitiveattribute_instantiation(instance):
    assert isinstance(instance, PetriNet::PrimitiveAttribute)

@given(instance=PetriNet::PrimitiveAttribute_strategy)
def test_petrinet::primitiveattribute_primType_type(instance):
    assert isinstance(instance.primType, str)


@given(instance=PetriNet::PrimitiveAttribute_strategy)
def test_petrinet::primitiveattribute_primType_setter(instance):
    original = instance.primType
    instance.primType = original
    assert instance.primType == original

@given(instance=PetriNet::PrimitiveAttribute_strategy)
def test_petrinet::primitiveattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNet::PrimitiveAttribute_strategy)
def test_petrinet::primitiveattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet::Type_strategy)
@settings(max_examples=50)
def test_petrinet::type_instantiation(instance):
    assert isinstance(instance, PetriNet::Type)

@given(instance=PetriNet::Type_strategy)
def test_petrinet::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNet::Type_strategy)
def test_petrinet::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet::IdentifiableElement_strategy)
@settings(max_examples=50)
def test_petrinet::identifiableelement_instantiation(instance):
    assert isinstance(instance, PetriNet::IdentifiableElement)

@given(instance=PetriNet::IdentifiableElement_strategy)
def test_petrinet::identifiableelement_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=PetriNet::IdentifiableElement_strategy)
def test_petrinet::identifiableelement_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=PetriNet::IdentifiableElement_strategy)
def test_petrinet::identifiableelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNet::IdentifiableElement_strategy)
def test_petrinet::identifiableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PetriNet::TransToPlaceArc_strategy)
@settings(max_examples=50)
def test_petrinet::transtoplacearc_instantiation(instance):
    assert isinstance(instance, PetriNet::TransToPlaceArc)

@given(instance=PetriNet::PlaceToTransArc_strategy)
@settings(max_examples=50)
def test_petrinet::placetotransarc_instantiation(instance):
    assert isinstance(instance, PetriNet::PlaceToTransArc)

@given(instance=PetriNet::Token_strategy)
@settings(max_examples=50)
def test_petrinet::token_instantiation(instance):
    assert isinstance(instance, PetriNet::Token)

@given(instance=PetriNet::Token_strategy)
def test_petrinet::token_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=PetriNet::Token_strategy)
def test_petrinet::token_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=PetriNet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, PetriNet::Arc)

@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=IdentifiableElement_strategy)
@settings(max_examples=50)
def test_identifiableelement_instantiation(instance):
    assert isinstance(instance, IdentifiableElement)

@given(instance=PetriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, PetriNet::Place)

@given(instance=PetriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, PetriNet::Transition)

@given(instance=PetriNet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet::PetriNet)
