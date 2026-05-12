import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ArcToTransition,
    ptnetLoLA::ArcToTransitionExt,
    ArcToPlace,
    ptnetLoLA::ArcToPlaceExt,
    Arc,
    ptnetLoLA::ArcToTransition,
    ptnetLoLA::ArcToPlace,
    Place,
    ptnetLoLA::PlaceExt,
    Transition,
    ptnetLoLA::TransitionExt,
    PlaceReference,
    ptnetLoLA::RefMarkedPlace,
    ptnetLoLA::PlaceReference,
    ptnetLoLA::Annotation,
    ptnetLoLA::Marking,
    ptnetLoLA::Node,
    ptnetLoLA::Arc,
    ptnetLoLA::PtNet,
    Node,
    ptnetLoLA::Transition,
    ptnetLoLA::Place,
    NodeType,
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



def test_ptnetlola::arctotransitionext_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA::ArcToTransitionExt)


def test_ptnetlola::arctotransitionext_constructor_exists():
    assert callable(ptnetLoLA::ArcToTransitionExt.__init__)


def test_ptnetlola::arctotransitionext_constructor_args():
    sig = inspect.signature(ptnetLoLA::ArcToTransitionExt.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_ptnetlola::arctotransitionext_has_probability():
    assert hasattr(ptnetLoLA::ArcToTransitionExt, "probability")
    descriptor = None
    for klass in ptnetLoLA::ArcToTransitionExt.__mro__:
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



def test_ptnetlola::arctoplaceext_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA::ArcToPlaceExt)


def test_ptnetlola::arctoplaceext_constructor_exists():
    assert callable(ptnetLoLA::ArcToPlaceExt.__init__)


def test_ptnetlola::arctoplaceext_constructor_args():
    sig = inspect.signature(ptnetLoLA::ArcToPlaceExt.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_ptnetlola::arctoplaceext_has_probability():
    assert hasattr(ptnetLoLA::ArcToPlaceExt, "probability")
    descriptor = None
    for klass in ptnetLoLA::ArcToPlaceExt.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola::arctotransition_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA::ArcToTransition)


def test_ptnetlola::arctotransition_constructor_exists():
    assert callable(ptnetLoLA::ArcToTransition.__init__)


def test_ptnetlola::arctotransition_constructor_args():
    sig = inspect.signature(ptnetLoLA::ArcToTransition.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola::arctoplace_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA::ArcToPlace)


def test_ptnetlola::arctoplace_constructor_exists():
    assert callable(ptnetLoLA::ArcToPlace.__init__)


def test_ptnetlola::arctoplace_constructor_args():
    sig = inspect.signature(ptnetLoLA::ArcToPlace.__init__)
    params = list(sig.parameters.keys())



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola::placeext_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA::PlaceExt)


def test_ptnetlola::placeext_constructor_exists():
    assert callable(ptnetLoLA::PlaceExt.__init__)


def test_ptnetlola::placeext_constructor_args():
    sig = inspect.signature(ptnetLoLA::PlaceExt.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"
    assert "isStart" in params, "Missing parameter 'isStart'"

def test_ptnetlola::placeext_has_probability():
    assert hasattr(ptnetLoLA::PlaceExt, "probability")
    descriptor = None
    for klass in ptnetLoLA::PlaceExt.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)

def test_ptnetlola::placeext_has_isStart():
    assert hasattr(ptnetLoLA::PlaceExt, "isStart")
    descriptor = None
    for klass in ptnetLoLA::PlaceExt.__mro__:
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



def test_ptnetlola::transitionext_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA::TransitionExt)


def test_ptnetlola::transitionext_constructor_exists():
    assert callable(ptnetLoLA::TransitionExt.__init__)


def test_ptnetlola::transitionext_constructor_args():
    sig = inspect.signature(ptnetLoLA::TransitionExt.__init__)
    params = list(sig.parameters.keys())
    assert "cost" in params, "Missing parameter 'cost'"
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"
    assert "probability" in params, "Missing parameter 'probability'"

def test_ptnetlola::transitionext_has_cost():
    assert hasattr(ptnetLoLA::TransitionExt, "cost")
    descriptor = None
    for klass in ptnetLoLA::TransitionExt.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_ptnetlola::transitionext_has_minTime():
    assert hasattr(ptnetLoLA::TransitionExt, "minTime")
    descriptor = None
    for klass in ptnetLoLA::TransitionExt.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_ptnetlola::transitionext_has_maxTime():
    assert hasattr(ptnetLoLA::TransitionExt, "maxTime")
    descriptor = None
    for klass in ptnetLoLA::TransitionExt.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)

def test_ptnetlola::transitionext_has_probability():
    assert hasattr(ptnetLoLA::TransitionExt, "probability")
    descriptor = None
    for klass in ptnetLoLA::TransitionExt.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_placereference_is_not_abstract():
    assert not inspect.isabstract(PlaceReference)


def test_placereference_constructor_exists():
    assert callable(PlaceReference.__init__)


def test_placereference_constructor_args():
    sig = inspect.signature(PlaceReference.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola::refmarkedplace_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA::RefMarkedPlace)


def test_ptnetlola::refmarkedplace_constructor_exists():
    assert callable(ptnetLoLA::RefMarkedPlace.__init__)


def test_ptnetlola::refmarkedplace_constructor_args():
    sig = inspect.signature(ptnetLoLA::RefMarkedPlace.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_ptnetlola::refmarkedplace_has_token():
    assert hasattr(ptnetLoLA::RefMarkedPlace, "token")
    descriptor = None
    for klass in ptnetLoLA::RefMarkedPlace.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_ptnetlola::placereference_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA::PlaceReference)


def test_ptnetlola::placereference_constructor_exists():
    assert callable(ptnetLoLA::PlaceReference.__init__)


def test_ptnetlola::placereference_constructor_args():
    sig = inspect.signature(ptnetLoLA::PlaceReference.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola::annotation_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA::Annotation)


def test_ptnetlola::annotation_constructor_exists():
    assert callable(ptnetLoLA::Annotation.__init__)


def test_ptnetlola::annotation_constructor_args():
    sig = inspect.signature(ptnetLoLA::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_ptnetlola::annotation_has_text():
    assert hasattr(ptnetLoLA::Annotation, "text")
    descriptor = None
    for klass in ptnetLoLA::Annotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_ptnetlola::marking_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA::Marking)


def test_ptnetlola::marking_constructor_exists():
    assert callable(ptnetLoLA::Marking.__init__)


def test_ptnetlola::marking_constructor_args():
    sig = inspect.signature(ptnetLoLA::Marking.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola::node_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA::Node)


def test_ptnetlola::node_constructor_exists():
    assert callable(ptnetLoLA::Node.__init__)


def test_ptnetlola::node_constructor_args():
    sig = inspect.signature(ptnetLoLA::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_ptnetlola::node_has_name():
    assert hasattr(ptnetLoLA::Node, "name")
    descriptor = None
    for klass in ptnetLoLA::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ptnetlola::node_has_type():
    assert hasattr(ptnetLoLA::Node, "type")
    descriptor = None
    for klass in ptnetLoLA::Node.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ptnetlola::arc_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA::Arc)


def test_ptnetlola::arc_constructor_exists():
    assert callable(ptnetLoLA::Arc.__init__)


def test_ptnetlola::arc_constructor_args():
    sig = inspect.signature(ptnetLoLA::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_ptnetlola::arc_has_weight():
    assert hasattr(ptnetLoLA::Arc, "weight")
    descriptor = None
    for klass in ptnetLoLA::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_ptnetlola::ptnet_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA::PtNet)


def test_ptnetlola::ptnet_constructor_exists():
    assert callable(ptnetLoLA::PtNet.__init__)


def test_ptnetlola::ptnet_constructor_args():
    sig = inspect.signature(ptnetLoLA::PtNet.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola::transition_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA::Transition)


def test_ptnetlola::transition_constructor_exists():
    assert callable(ptnetLoLA::Transition.__init__)


def test_ptnetlola::transition_constructor_args():
    sig = inspect.signature(ptnetLoLA::Transition.__init__)
    params = list(sig.parameters.keys())



def test_ptnetlola::place_is_not_abstract():
    assert not inspect.isabstract(ptnetLoLA::Place)


def test_ptnetlola::place_constructor_exists():
    assert callable(ptnetLoLA::Place.__init__)


def test_ptnetlola::place_constructor_args():
    sig = inspect.signature(ptnetLoLA::Place.__init__)
    params = list(sig.parameters.keys())
    assert "finalMarking" in params, "Missing parameter 'finalMarking'"
    assert "token" in params, "Missing parameter 'token'"

def test_ptnetlola::place_has_finalMarking():
    assert hasattr(ptnetLoLA::Place, "finalMarking")
    descriptor = None
    for klass in ptnetLoLA::Place.__mro__:
        if "finalMarking" in klass.__dict__:
            descriptor = klass.__dict__["finalMarking"]
            break
    assert isinstance(descriptor, property)

def test_ptnetlola::place_has_token():
    assert hasattr(ptnetLoLA::Place, "token")
    descriptor = None
    for klass in ptnetLoLA::Place.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)

def test_nodetype_exists():
    # Check that the Enumeration exists
    assert NodeType is not None

def test_nodetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NodeType]
    expected_literals = [
        "output",
        "input",
        "inout",
        "internal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NodeType"


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
ptnetLoLA::ArcToTransitionExt_strategy = st.builds(
    ptnetLoLA::ArcToTransitionExt,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ArcToPlace_strategy = st.builds(
    ArcToPlace,
)
ptnetLoLA::ArcToPlaceExt_strategy = st.builds(
    ptnetLoLA::ArcToPlaceExt,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Arc_strategy = st.builds(
    Arc,
)
ptnetLoLA::ArcToTransition_strategy = st.builds(
    ptnetLoLA::ArcToTransition,
)
ptnetLoLA::ArcToPlace_strategy = st.builds(
    ptnetLoLA::ArcToPlace,
)
Place_strategy = st.builds(
    Place,
)
ptnetLoLA::PlaceExt_strategy = st.builds(
    ptnetLoLA::PlaceExt,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isStart=
        st.booleans()
)
Transition_strategy = st.builds(
    Transition,
)
ptnetLoLA::TransitionExt_strategy = st.builds(
    ptnetLoLA::TransitionExt,
    cost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minTime=
        st.integers(),
    maxTime=
        st.integers(),
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
PlaceReference_strategy = st.builds(
    PlaceReference,
)
ptnetLoLA::RefMarkedPlace_strategy = st.builds(
    ptnetLoLA::RefMarkedPlace,
    token=
        st.integers()
)
ptnetLoLA::PlaceReference_strategy = st.builds(
    ptnetLoLA::PlaceReference,
)
ptnetLoLA::Annotation_strategy = st.builds(
    ptnetLoLA::Annotation,
    text=
        safe_text
)
ptnetLoLA::Marking_strategy = st.builds(
    ptnetLoLA::Marking,
)
ptnetLoLA::Node_strategy = st.builds(
    ptnetLoLA::Node,
    name=
        safe_text,
    type=
        safe_text
)
ptnetLoLA::Arc_strategy = st.builds(
    ptnetLoLA::Arc,
    weight=
        st.integers()
)
ptnetLoLA::PtNet_strategy = st.builds(
    ptnetLoLA::PtNet,
)
Node_strategy = st.builds(
    Node,
)
ptnetLoLA::Transition_strategy = st.builds(
    ptnetLoLA::Transition,
)
ptnetLoLA::Place_strategy = st.builds(
    ptnetLoLA::Place,
    finalMarking=
        st.integers(),
    token=
        st.integers()
)

@given(instance=ArcToTransition_strategy)
@settings(max_examples=50)
def test_arctotransition_instantiation(instance):
    assert isinstance(instance, ArcToTransition)

@given(instance=ptnetLoLA::ArcToTransitionExt_strategy)
@settings(max_examples=50)
def test_ptnetlola::arctotransitionext_instantiation(instance):
    assert isinstance(instance, ptnetLoLA::ArcToTransitionExt)

@given(instance=ptnetLoLA::ArcToTransitionExt_strategy)
def test_ptnetlola::arctotransitionext_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=ptnetLoLA::ArcToTransitionExt_strategy)
def test_ptnetlola::arctotransitionext_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=ArcToPlace_strategy)
@settings(max_examples=50)
def test_arctoplace_instantiation(instance):
    assert isinstance(instance, ArcToPlace)

@given(instance=ptnetLoLA::ArcToPlaceExt_strategy)
@settings(max_examples=50)
def test_ptnetlola::arctoplaceext_instantiation(instance):
    assert isinstance(instance, ptnetLoLA::ArcToPlaceExt)

@given(instance=ptnetLoLA::ArcToPlaceExt_strategy)
def test_ptnetlola::arctoplaceext_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=ptnetLoLA::ArcToPlaceExt_strategy)
def test_ptnetlola::arctoplaceext_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=ptnetLoLA::ArcToTransition_strategy)
@settings(max_examples=50)
def test_ptnetlola::arctotransition_instantiation(instance):
    assert isinstance(instance, ptnetLoLA::ArcToTransition)

@given(instance=ptnetLoLA::ArcToPlace_strategy)
@settings(max_examples=50)
def test_ptnetlola::arctoplace_instantiation(instance):
    assert isinstance(instance, ptnetLoLA::ArcToPlace)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=ptnetLoLA::PlaceExt_strategy)
@settings(max_examples=50)
def test_ptnetlola::placeext_instantiation(instance):
    assert isinstance(instance, ptnetLoLA::PlaceExt)

@given(instance=ptnetLoLA::PlaceExt_strategy)
def test_ptnetlola::placeext_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=ptnetLoLA::PlaceExt_strategy)
def test_ptnetlola::placeext_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=ptnetLoLA::PlaceExt_strategy)
def test_ptnetlola::placeext_isStart_type(instance):
    assert isinstance(instance.isStart, bool)


@given(instance=ptnetLoLA::PlaceExt_strategy)
def test_ptnetlola::placeext_isStart_setter(instance):
    original = instance.isStart
    instance.isStart = original
    assert instance.isStart == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=ptnetLoLA::TransitionExt_strategy)
@settings(max_examples=50)
def test_ptnetlola::transitionext_instantiation(instance):
    assert isinstance(instance, ptnetLoLA::TransitionExt)

@given(instance=ptnetLoLA::TransitionExt_strategy)
def test_ptnetlola::transitionext_cost_type(instance):
    assert isinstance(instance.cost, float)


@given(instance=ptnetLoLA::TransitionExt_strategy)
def test_ptnetlola::transitionext_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original

@given(instance=ptnetLoLA::TransitionExt_strategy)
def test_ptnetlola::transitionext_minTime_type(instance):
    assert isinstance(instance.minTime, int)


@given(instance=ptnetLoLA::TransitionExt_strategy)
def test_ptnetlola::transitionext_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=ptnetLoLA::TransitionExt_strategy)
def test_ptnetlola::transitionext_maxTime_type(instance):
    assert isinstance(instance.maxTime, int)


@given(instance=ptnetLoLA::TransitionExt_strategy)
def test_ptnetlola::transitionext_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original

@given(instance=ptnetLoLA::TransitionExt_strategy)
def test_ptnetlola::transitionext_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=ptnetLoLA::TransitionExt_strategy)
def test_ptnetlola::transitionext_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=PlaceReference_strategy)
@settings(max_examples=50)
def test_placereference_instantiation(instance):
    assert isinstance(instance, PlaceReference)

@given(instance=ptnetLoLA::RefMarkedPlace_strategy)
@settings(max_examples=50)
def test_ptnetlola::refmarkedplace_instantiation(instance):
    assert isinstance(instance, ptnetLoLA::RefMarkedPlace)

@given(instance=ptnetLoLA::RefMarkedPlace_strategy)
def test_ptnetlola::refmarkedplace_token_type(instance):
    assert isinstance(instance.token, int)


@given(instance=ptnetLoLA::RefMarkedPlace_strategy)
def test_ptnetlola::refmarkedplace_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=ptnetLoLA::PlaceReference_strategy)
@settings(max_examples=50)
def test_ptnetlola::placereference_instantiation(instance):
    assert isinstance(instance, ptnetLoLA::PlaceReference)

@given(instance=ptnetLoLA::Annotation_strategy)
@settings(max_examples=50)
def test_ptnetlola::annotation_instantiation(instance):
    assert isinstance(instance, ptnetLoLA::Annotation)

@given(instance=ptnetLoLA::Annotation_strategy)
def test_ptnetlola::annotation_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=ptnetLoLA::Annotation_strategy)
def test_ptnetlola::annotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=ptnetLoLA::Marking_strategy)
@settings(max_examples=50)
def test_ptnetlola::marking_instantiation(instance):
    assert isinstance(instance, ptnetLoLA::Marking)

@given(instance=ptnetLoLA::Node_strategy)
@settings(max_examples=50)
def test_ptnetlola::node_instantiation(instance):
    assert isinstance(instance, ptnetLoLA::Node)

@given(instance=ptnetLoLA::Node_strategy)
def test_ptnetlola::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ptnetLoLA::Node_strategy)
def test_ptnetlola::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ptnetLoLA::Node_strategy)
def test_ptnetlola::node_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ptnetLoLA::Node_strategy)
def test_ptnetlola::node_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ptnetLoLA::Arc_strategy)
@settings(max_examples=50)
def test_ptnetlola::arc_instantiation(instance):
    assert isinstance(instance, ptnetLoLA::Arc)

@given(instance=ptnetLoLA::Arc_strategy)
def test_ptnetlola::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=ptnetLoLA::Arc_strategy)
def test_ptnetlola::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=ptnetLoLA::PtNet_strategy)
@settings(max_examples=50)
def test_ptnetlola::ptnet_instantiation(instance):
    assert isinstance(instance, ptnetLoLA::PtNet)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=ptnetLoLA::Transition_strategy)
@settings(max_examples=50)
def test_ptnetlola::transition_instantiation(instance):
    assert isinstance(instance, ptnetLoLA::Transition)

@given(instance=ptnetLoLA::Place_strategy)
@settings(max_examples=50)
def test_ptnetlola::place_instantiation(instance):
    assert isinstance(instance, ptnetLoLA::Place)

@given(instance=ptnetLoLA::Place_strategy)
def test_ptnetlola::place_finalMarking_type(instance):
    assert isinstance(instance.finalMarking, int)


@given(instance=ptnetLoLA::Place_strategy)
def test_ptnetlola::place_finalMarking_setter(instance):
    original = instance.finalMarking
    instance.finalMarking = original
    assert instance.finalMarking == original

@given(instance=ptnetLoLA::Place_strategy)
def test_ptnetlola::place_token_type(instance):
    assert isinstance(instance.token, int)


@given(instance=ptnetLoLA::Place_strategy)
def test_ptnetlola::place_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original
