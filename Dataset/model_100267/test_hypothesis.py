import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PetriNet_IdentifiableElement,
    Arc,
    PetriNet_TransToPlaceArc,
    PetriNet_PlaceToTransArc,
    PetriNet_PrimitiveAttribute,
    PetriNet_Token,
    PetriNet_Type,
    PetriNet_Arc,
    IdentifiableElement,
    PetriNet_Transition,
    PetriNet_Place,
    PetriNet_PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet_identifiableelement_is_not_abstract():
    assert not inspect.isabstract(PetriNet_IdentifiableElement)


def test_petrinet_identifiableelement_constructor_exists():
    assert callable(PetriNet_IdentifiableElement.__init__)


def test_petrinet_identifiableelement_constructor_args():
    sig = inspect.signature(PetriNet_IdentifiableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "author" in params, "Missing parameter 'author'"

def test_petrinet_identifiableelement_has_name():
    assert hasattr(PetriNet_IdentifiableElement, "name")
    descriptor = None
    for klass in PetriNet_IdentifiableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_identifiableelement_has_author():
    assert hasattr(PetriNet_IdentifiableElement, "author")
    descriptor = None
    for klass in PetriNet_IdentifiableElement.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)



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



def test_petrinet_primitiveattribute_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PrimitiveAttribute)


def test_petrinet_primitiveattribute_constructor_exists():
    assert callable(PetriNet_PrimitiveAttribute.__init__)


def test_petrinet_primitiveattribute_constructor_args():
    sig = inspect.signature(PetriNet_PrimitiveAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "primType" in params, "Missing parameter 'primType'"

def test_petrinet_primitiveattribute_has_name():
    assert hasattr(PetriNet_PrimitiveAttribute, "name")
    descriptor = None
    for klass in PetriNet_PrimitiveAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_primitiveattribute_has_primType():
    assert hasattr(PetriNet_PrimitiveAttribute, "primType")
    descriptor = None
    for klass in PetriNet_PrimitiveAttribute.__mro__:
        if "primType" in klass.__dict__:
            descriptor = klass.__dict__["primType"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_token_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Token)


def test_petrinet_token_constructor_exists():
    assert callable(PetriNet_Token.__init__)


def test_petrinet_token_constructor_args():
    sig = inspect.signature(PetriNet_Token.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_petrinet_token_has_values():
    assert hasattr(PetriNet_Token, "values")
    descriptor = None
    for klass in PetriNet_Token.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_type_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Type)


def test_petrinet_type_constructor_exists():
    assert callable(PetriNet_Type.__init__)


def test_petrinet_type_constructor_args():
    sig = inspect.signature(PetriNet_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_type_has_name():
    assert hasattr(PetriNet_Type, "name")
    descriptor = None
    for klass in PetriNet_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_identifiableelement_is_not_abstract():
    assert not inspect.isabstract(IdentifiableElement)


def test_identifiableelement_constructor_exists():
    assert callable(IdentifiableElement.__init__)


def test_identifiableelement_constructor_args():
    sig = inspect.signature(IdentifiableElement.__init__)
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
PetriNet_IdentifiableElement_strategy = st.builds(
    PetriNet_IdentifiableElement,
    name=
        safe_text,
    author=
        safe_text
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
PetriNet_PrimitiveAttribute_strategy = st.builds(
    PetriNet_PrimitiveAttribute,
    name=
        safe_text,
    primType=
        safe_text
)
PetriNet_Token_strategy = st.builds(
    PetriNet_Token,
    values=
        safe_text
)
PetriNet_Type_strategy = st.builds(
    PetriNet_Type,
    name=
        safe_text
)
PetriNet_Arc_strategy = st.builds(
    PetriNet_Arc,
    weight=
        st.integers()
)
IdentifiableElement_strategy = st.builds(
    IdentifiableElement,
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

@given(instance=PetriNet_IdentifiableElement_strategy)
@settings(max_examples=50)
def test_petrinet_identifiableelement_instantiation(instance):
    assert isinstance(instance, PetriNet_IdentifiableElement)



@given(instance=PetriNet_IdentifiableElement_strategy)
def test_petrinet_identifiableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=PetriNet_IdentifiableElement_strategy)
def test_petrinet_identifiableelement_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

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

@given(instance=PetriNet_PrimitiveAttribute_strategy)
@settings(max_examples=50)
def test_petrinet_primitiveattribute_instantiation(instance):
    assert isinstance(instance, PetriNet_PrimitiveAttribute)



@given(instance=PetriNet_PrimitiveAttribute_strategy)
def test_petrinet_primitiveattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=PetriNet_PrimitiveAttribute_strategy)
def test_petrinet_primitiveattribute_primType_setter(instance):
    original = instance.primType
    instance.primType = original
    assert instance.primType == original

@given(instance=PetriNet_Token_strategy)
@settings(max_examples=50)
def test_petrinet_token_instantiation(instance):
    assert isinstance(instance, PetriNet_Token)



@given(instance=PetriNet_Token_strategy)
def test_petrinet_token_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=PetriNet_Type_strategy)
@settings(max_examples=50)
def test_petrinet_type_instantiation(instance):
    assert isinstance(instance, PetriNet_Type)



@given(instance=PetriNet_Type_strategy)
def test_petrinet_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, PetriNet_Arc)



@given(instance=PetriNet_Arc_strategy)
def test_petrinet_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=IdentifiableElement_strategy)
@settings(max_examples=50)
def test_identifiableelement_instantiation(instance):
    assert isinstance(instance, IdentifiableElement)

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
