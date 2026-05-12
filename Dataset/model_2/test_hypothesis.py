import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ArcToTransition,
    ptnetLoLA_ArcToTransitionExt,
    ArcToPlace,
    ptnetLoLA_ArcToPlaceExt,
    Place,
    ptnetLoLA_PlaceExt,
    Transition,
    ptnetLoLA_TransitionExt,
    Arc,
    ptnetLoLA_ArcToTransition,
    ptnetLoLA_ArcToPlace,
    PlaceReference,
    ptnetLoLA_PlaceReference,
    ptnetLoLA_RefMarkedPlace,
    ptnetLoLA_Node,
    ptnetLoLA_Arc,
    ptnetLoLA_Marking,
    ptnetLoLA_PtNet,
    Node,
    ptnetLoLA_Transition,
    ptnetLoLA_Place,
    ptnetLoLA_Annotation,
    NodeType,
    Confidentiality,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_arctotransition_is_not_abstract():
    assert not inspect.isabstract(ArcToTransition)


def test_arctotransition_constructor_exists():
    assert callable(ArcToTransition.__init__)


def test_arctotransition_constructor_args():
    sig = inspect.signature(ArcToTransition.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola_arctotransitionext_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA_ArcToTransitionExt)


def test_ptnetlola_arctotransitionext_constructor_exists():
    assert callable(ptnetLoLA_ArcToTransitionExt.__init__)


def test_ptnetlola_arctotransitionext_constructor_args():
    sig = inspect.signature(ptnetLoLA_ArcToTransitionExt.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_ptnetlola_arctotransitionext_has_probability():
    assert hasattr(ptnetLoLA_ArcToTransitionExt, "probability")
    descriptor = None
    for klass in ptnetLoLA_ArcToTransitionExt.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_arctoplace_is_not_abstract():
    assert not inspect.isabstract(ArcToPlace)


def test_arctoplace_constructor_exists():
    assert callable(ArcToPlace.__init__)


def test_arctoplace_constructor_args():
    sig = inspect.signature(ArcToPlace.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola_arctoplaceext_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA_ArcToPlaceExt)


def test_ptnetlola_arctoplaceext_constructor_exists():
    assert callable(ptnetLoLA_ArcToPlaceExt.__init__)


def test_ptnetlola_arctoplaceext_constructor_args():
    sig = inspect.signature(ptnetLoLA_ArcToPlaceExt.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_ptnetlola_arctoplaceext_has_probability():
    assert hasattr(ptnetLoLA_ArcToPlaceExt, "probability")
    descriptor = None
    for klass in ptnetLoLA_ArcToPlaceExt.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola_placeext_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA_PlaceExt)


def test_ptnetlola_placeext_constructor_exists():
    assert callable(ptnetLoLA_PlaceExt.__init__)


def test_ptnetlola_placeext_constructor_args():
    sig = inspect.signature(ptnetLoLA_PlaceExt.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"
    assert "isStart" in params, "Missing parameter 'isStart'"

def test_ptnetlola_placeext_has_probability():
    assert hasattr(ptnetLoLA_PlaceExt, "probability")
    descriptor = None
    for klass in ptnetLoLA_PlaceExt.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)

def test_ptnetlola_placeext_has_isStart():
    assert hasattr(ptnetLoLA_PlaceExt, "isStart")
    descriptor = None
    for klass in ptnetLoLA_PlaceExt.__mro__:
        if "isStart" in klass.__dict__:
            descriptor = klass.__dict__["isStart"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola_transitionext_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA_TransitionExt)


def test_ptnetlola_transitionext_constructor_exists():
    assert callable(ptnetLoLA_TransitionExt.__init__)


def test_ptnetlola_transitionext_constructor_args():
    sig = inspect.signature(ptnetLoLA_TransitionExt.__init__)
    params = list(sig.parameters.keys())
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "confidentiality" in params, "Missing parameter 'confidentiality'"
    assert "probability" in params, "Missing parameter 'probability'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"
    assert "cost" in params, "Missing parameter 'cost'"

def test_ptnetlola_transitionext_has_minTime():
    assert hasattr(ptnetLoLA_TransitionExt, "minTime")
    descriptor = None
    for klass in ptnetLoLA_TransitionExt.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_ptnetlola_transitionext_has_confidentiality():
    assert hasattr(ptnetLoLA_TransitionExt, "confidentiality")
    descriptor = None
    for klass in ptnetLoLA_TransitionExt.__mro__:
        if "confidentiality" in klass.__dict__:
            descriptor = klass.__dict__["confidentiality"]
            break
    assert isinstance(descriptor, property)

def test_ptnetlola_transitionext_has_probability():
    assert hasattr(ptnetLoLA_TransitionExt, "probability")
    descriptor = None
    for klass in ptnetLoLA_TransitionExt.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)

def test_ptnetlola_transitionext_has_maxTime():
    assert hasattr(ptnetLoLA_TransitionExt, "maxTime")
    descriptor = None
    for klass in ptnetLoLA_TransitionExt.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)

def test_ptnetlola_transitionext_has_cost():
    assert hasattr(ptnetLoLA_TransitionExt, "cost")
    descriptor = None
    for klass in ptnetLoLA_TransitionExt.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola_arctotransition_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA_ArcToTransition)


def test_ptnetlola_arctotransition_constructor_exists():
    assert callable(ptnetLoLA_ArcToTransition.__init__)


def test_ptnetlola_arctotransition_constructor_args():
    sig = inspect.signature(ptnetLoLA_ArcToTransition.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola_arctoplace_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA_ArcToPlace)


def test_ptnetlola_arctoplace_constructor_exists():
    assert callable(ptnetLoLA_ArcToPlace.__init__)


def test_ptnetlola_arctoplace_constructor_args():
    sig = inspect.signature(ptnetLoLA_ArcToPlace.__init__)
    params = list(sig.parameters.keys())



def test_placereference_is_not_abstract():
    assert not inspect.isabstract(PlaceReference)


def test_placereference_constructor_exists():
    assert callable(PlaceReference.__init__)


def test_placereference_constructor_args():
    sig = inspect.signature(PlaceReference.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola_placereference_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA_PlaceReference)


def test_ptnetlola_placereference_constructor_exists():
    assert callable(ptnetLoLA_PlaceReference.__init__)


def test_ptnetlola_placereference_constructor_args():
    sig = inspect.signature(ptnetLoLA_PlaceReference.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola_refmarkedplace_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA_RefMarkedPlace)


def test_ptnetlola_refmarkedplace_constructor_exists():
    assert callable(ptnetLoLA_RefMarkedPlace.__init__)


def test_ptnetlola_refmarkedplace_constructor_args():
    sig = inspect.signature(ptnetLoLA_RefMarkedPlace.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_ptnetlola_refmarkedplace_has_token():
    assert hasattr(ptnetLoLA_RefMarkedPlace, "token")
    descriptor = None
    for klass in ptnetLoLA_RefMarkedPlace.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_ptnetlola_node_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA_Node)


def test_ptnetlola_node_constructor_exists():
    assert callable(ptnetLoLA_Node.__init__)


def test_ptnetlola_node_constructor_args():
    sig = inspect.signature(ptnetLoLA_Node.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_ptnetlola_node_has_type():
    assert hasattr(ptnetLoLA_Node, "type")
    descriptor = None
    for klass in ptnetLoLA_Node.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ptnetlola_node_has_name():
    assert hasattr(ptnetLoLA_Node, "name")
    descriptor = None
    for klass in ptnetLoLA_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ptnetlola_arc_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA_Arc)


def test_ptnetlola_arc_constructor_exists():
    assert callable(ptnetLoLA_Arc.__init__)


def test_ptnetlola_arc_constructor_args():
    sig = inspect.signature(ptnetLoLA_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_ptnetlola_arc_has_weight():
    assert hasattr(ptnetLoLA_Arc, "weight")
    descriptor = None
    for klass in ptnetLoLA_Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_ptnetlola_marking_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA_Marking)


def test_ptnetlola_marking_constructor_exists():
    assert callable(ptnetLoLA_Marking.__init__)


def test_ptnetlola_marking_constructor_args():
    sig = inspect.signature(ptnetLoLA_Marking.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola_ptnet_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA_PtNet)


def test_ptnetlola_ptnet_constructor_exists():
    assert callable(ptnetLoLA_PtNet.__init__)


def test_ptnetlola_ptnet_constructor_args():
    sig = inspect.signature(ptnetLoLA_PtNet.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola_transition_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA_Transition)


def test_ptnetlola_transition_constructor_exists():
    assert callable(ptnetLoLA_Transition.__init__)


def test_ptnetlola_transition_constructor_args():
    sig = inspect.signature(ptnetLoLA_Transition.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola_place_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA_Place)


def test_ptnetlola_place_constructor_exists():
    assert callable(ptnetLoLA_Place.__init__)


def test_ptnetlola_place_constructor_args():
    sig = inspect.signature(ptnetLoLA_Place.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"
    assert "finalMarking" in params, "Missing parameter 'finalMarking'"

def test_ptnetlola_place_has_token():
    assert hasattr(ptnetLoLA_Place, "token")
    descriptor = None
    for klass in ptnetLoLA_Place.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)

def test_ptnetlola_place_has_finalMarking():
    assert hasattr(ptnetLoLA_Place, "finalMarking")
    descriptor = None
    for klass in ptnetLoLA_Place.__mro__:
        if "finalMarking" in klass.__dict__:
            descriptor = klass.__dict__["finalMarking"]
            break
    assert isinstance(descriptor, property)



def test_ptnetlola_annotation_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA_Annotation)


def test_ptnetlola_annotation_constructor_exists():
    assert callable(ptnetLoLA_Annotation.__init__)


def test_ptnetlola_annotation_constructor_args():
    sig = inspect.signature(ptnetLoLA_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_ptnetlola_annotation_has_text():
    assert hasattr(ptnetLoLA_Annotation, "text")
    descriptor = None
    for klass in ptnetLoLA_Annotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_nodetype_exists():
    # Check that the Enumeration exists
    assert NodeType is not None

def test_nodetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NodeType]
    expected_literals = [
        "internal",
        "input",
        "output",
        "inout",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NodeType"

def test_confidentiality_exists():
    # Check that the Enumeration exists
    assert Confidentiality is not None

def test_confidentiality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Confidentiality]
    expected_literals = [
        "UNKNOWN",
        "HIGH",
        "LOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Confidentiality"


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
ArcToTransition_strategy = st.builds(
    ArcToTransition,
)
ptnetLoLA_ArcToTransitionExt_strategy = st.builds(
    ptnetLoLA_ArcToTransitionExt,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ArcToPlace_strategy = st.builds(
    ArcToPlace,
)
ptnetLoLA_ArcToPlaceExt_strategy = st.builds(
    ptnetLoLA_ArcToPlaceExt,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Place_strategy = st.builds(
    Place,
)
ptnetLoLA_PlaceExt_strategy = st.builds(
    ptnetLoLA_PlaceExt,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isStart=
        st.booleans()
)
Transition_strategy = st.builds(
    Transition,
)
ptnetLoLA_TransitionExt_strategy = st.builds(
    ptnetLoLA_TransitionExt,
    minTime=
        st.integers(),
    confidentiality=
        safe_text,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maxTime=
        st.integers(),
    cost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Arc_strategy = st.builds(
    Arc,
)
ptnetLoLA_ArcToTransition_strategy = st.builds(
    ptnetLoLA_ArcToTransition,
)
ptnetLoLA_ArcToPlace_strategy = st.builds(
    ptnetLoLA_ArcToPlace,
)
PlaceReference_strategy = st.builds(
    PlaceReference,
)
ptnetLoLA_PlaceReference_strategy = st.builds(
    ptnetLoLA_PlaceReference,
)
ptnetLoLA_RefMarkedPlace_strategy = st.builds(
    ptnetLoLA_RefMarkedPlace,
    token=
        st.integers()
)
ptnetLoLA_Node_strategy = st.builds(
    ptnetLoLA_Node,
    type=
        safe_text,
    name=
        safe_text
)
ptnetLoLA_Arc_strategy = st.builds(
    ptnetLoLA_Arc,
    weight=
        st.integers()
)
ptnetLoLA_Marking_strategy = st.builds(
    ptnetLoLA_Marking,
)
ptnetLoLA_PtNet_strategy = st.builds(
    ptnetLoLA_PtNet,
)
Node_strategy = st.builds(
    Node,
)
ptnetLoLA_Transition_strategy = st.builds(
    ptnetLoLA_Transition,
)
ptnetLoLA_Place_strategy = st.builds(
    ptnetLoLA_Place,
    token=
        st.integers(),
    finalMarking=
        st.integers()
)
ptnetLoLA_Annotation_strategy = st.builds(
    ptnetLoLA_Annotation,
    text=
        safe_text
)

@given(instance=ArcToTransition_strategy)
@settings(max_examples=50)
def test_arctotransition_instantiation(instance):
    assert isinstance(instance, ArcToTransition)

@given(instance=ptnetLoLA_ArcToTransitionExt_strategy)
@settings(max_examples=50)
def test_ptnetlola_arctotransitionext_instantiation(instance):
    assert isinstance(instance, ptnetLoLA_ArcToTransitionExt)



@given(instance=ptnetLoLA_ArcToTransitionExt_strategy)
def test_ptnetlola_arctotransitionext_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=ArcToPlace_strategy)
@settings(max_examples=50)
def test_arctoplace_instantiation(instance):
    assert isinstance(instance, ArcToPlace)

@given(instance=ptnetLoLA_ArcToPlaceExt_strategy)
@settings(max_examples=50)
def test_ptnetlola_arctoplaceext_instantiation(instance):
    assert isinstance(instance, ptnetLoLA_ArcToPlaceExt)



@given(instance=ptnetLoLA_ArcToPlaceExt_strategy)
def test_ptnetlola_arctoplaceext_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=ptnetLoLA_PlaceExt_strategy)
@settings(max_examples=50)
def test_ptnetlola_placeext_instantiation(instance):
    assert isinstance(instance, ptnetLoLA_PlaceExt)



@given(instance=ptnetLoLA_PlaceExt_strategy)
def test_ptnetlola_placeext_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original



@given(instance=ptnetLoLA_PlaceExt_strategy)
def test_ptnetlola_placeext_isStart_setter(instance):
    original = instance.isStart
    instance.isStart = original
    assert instance.isStart == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=ptnetLoLA_TransitionExt_strategy)
@settings(max_examples=50)
def test_ptnetlola_transitionext_instantiation(instance):
    assert isinstance(instance, ptnetLoLA_TransitionExt)



@given(instance=ptnetLoLA_TransitionExt_strategy)
def test_ptnetlola_transitionext_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original



@given(instance=ptnetLoLA_TransitionExt_strategy)
def test_ptnetlola_transitionext_confidentiality_setter(instance):
    original = instance.confidentiality
    instance.confidentiality = original
    assert instance.confidentiality == original



@given(instance=ptnetLoLA_TransitionExt_strategy)
def test_ptnetlola_transitionext_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original



@given(instance=ptnetLoLA_TransitionExt_strategy)
def test_ptnetlola_transitionext_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original



@given(instance=ptnetLoLA_TransitionExt_strategy)
def test_ptnetlola_transitionext_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=ptnetLoLA_ArcToTransition_strategy)
@settings(max_examples=50)
def test_ptnetlola_arctotransition_instantiation(instance):
    assert isinstance(instance, ptnetLoLA_ArcToTransition)

@given(instance=ptnetLoLA_ArcToPlace_strategy)
@settings(max_examples=50)
def test_ptnetlola_arctoplace_instantiation(instance):
    assert isinstance(instance, ptnetLoLA_ArcToPlace)

@given(instance=PlaceReference_strategy)
@settings(max_examples=50)
def test_placereference_instantiation(instance):
    assert isinstance(instance, PlaceReference)

@given(instance=ptnetLoLA_PlaceReference_strategy)
@settings(max_examples=50)
def test_ptnetlola_placereference_instantiation(instance):
    assert isinstance(instance, ptnetLoLA_PlaceReference)

@given(instance=ptnetLoLA_RefMarkedPlace_strategy)
@settings(max_examples=50)
def test_ptnetlola_refmarkedplace_instantiation(instance):
    assert isinstance(instance, ptnetLoLA_RefMarkedPlace)



@given(instance=ptnetLoLA_RefMarkedPlace_strategy)
def test_ptnetlola_refmarkedplace_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=ptnetLoLA_Node_strategy)
@settings(max_examples=50)
def test_ptnetlola_node_instantiation(instance):
    assert isinstance(instance, ptnetLoLA_Node)



@given(instance=ptnetLoLA_Node_strategy)
def test_ptnetlola_node_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=ptnetLoLA_Node_strategy)
def test_ptnetlola_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ptnetLoLA_Arc_strategy)
@settings(max_examples=50)
def test_ptnetlola_arc_instantiation(instance):
    assert isinstance(instance, ptnetLoLA_Arc)



@given(instance=ptnetLoLA_Arc_strategy)
def test_ptnetlola_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=ptnetLoLA_Marking_strategy)
@settings(max_examples=50)
def test_ptnetlola_marking_instantiation(instance):
    assert isinstance(instance, ptnetLoLA_Marking)

@given(instance=ptnetLoLA_PtNet_strategy)
@settings(max_examples=50)
def test_ptnetlola_ptnet_instantiation(instance):
    assert isinstance(instance, ptnetLoLA_PtNet)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=ptnetLoLA_Transition_strategy)
@settings(max_examples=50)
def test_ptnetlola_transition_instantiation(instance):
    assert isinstance(instance, ptnetLoLA_Transition)

@given(instance=ptnetLoLA_Place_strategy)
@settings(max_examples=50)
def test_ptnetlola_place_instantiation(instance):
    assert isinstance(instance, ptnetLoLA_Place)



@given(instance=ptnetLoLA_Place_strategy)
def test_ptnetlola_place_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original



@given(instance=ptnetLoLA_Place_strategy)
def test_ptnetlola_place_finalMarking_setter(instance):
    original = instance.finalMarking
    instance.finalMarking = original
    assert instance.finalMarking == original

@given(instance=ptnetLoLA_Annotation_strategy)
@settings(max_examples=50)
def test_ptnetlola_annotation_instantiation(instance):
    assert isinstance(instance, ptnetLoLA_Annotation)



@given(instance=ptnetLoLA_Annotation_strategy)
def test_ptnetlola_annotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original
