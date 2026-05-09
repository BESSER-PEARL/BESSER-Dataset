import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinetsemantics::TM3PetriNet::PNSimEvent,
    PNScenario,
    petrinetsemantics::TM3PetriNet::PNTrace,
    PNTrace,
    petrinetsemantics::TM3PetriNet::PNScenario,
    Transition,
    PetriNetEvent,
    petrinetsemantics::EDMMPetriNet::FireTransitionEvent,
    PNSimEvent,
    petrinetsemantics::EDMMPetriNet::PetriNetEvent,
    petrinetsemantics::DDMMPetriNet::Arc,
    PetriNet,
    petrinetsemantics::DDMMPetriNet::Node,
    Arc,
    petrinetsemantics::SDMMPetriNet::PetriNet::dynamic,
    Place,
    Node::dynamic,
    petrinetsemantics::SDMMPetriNet::Place::dynamic,
    petrinetsemantics::SDMMPetriNet::Node::dynamic,
    Node,
    petrinetsemantics::DDMMPetriNet::Transition,
    petrinetsemantics::DDMMPetriNet::Place,
    petrinetsemantics::DDMMPetriNet::PetriNet,
    ArcKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetsemantics::tm3petrinet::pnsimevent_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics::TM3PetriNet::PNSimEvent)


def test_petrinetsemantics::tm3petrinet::pnsimevent_constructor_exists():
    assert callable(petrinetsemantics::TM3PetriNet::PNSimEvent.__init__)


def test_petrinetsemantics::tm3petrinet::pnsimevent_constructor_args():
    sig = inspect.signature(petrinetsemantics::TM3PetriNet::PNSimEvent.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "name" in params, "Missing parameter 'name'"
    assert "internal" in params, "Missing parameter 'internal'"

def test_petrinetsemantics::tm3petrinet::pnsimevent_has_date():
    assert hasattr(petrinetsemantics::TM3PetriNet::PNSimEvent, "date")
    descriptor = None
    for klass in petrinetsemantics::TM3PetriNet::PNSimEvent.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_petrinetsemantics::tm3petrinet::pnsimevent_has_name():
    assert hasattr(petrinetsemantics::TM3PetriNet::PNSimEvent, "name")
    descriptor = None
    for klass in petrinetsemantics::TM3PetriNet::PNSimEvent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetsemantics::tm3petrinet::pnsimevent_has_internal():
    assert hasattr(petrinetsemantics::TM3PetriNet::PNSimEvent, "internal")
    descriptor = None
    for klass in petrinetsemantics::TM3PetriNet::PNSimEvent.__mro__:
        if "internal" in klass.__dict__:
            descriptor = klass.__dict__["internal"]
            break
    assert isinstance(descriptor, property)



def test_pnscenario_is_not_abstract():
    assert not inspect.isabstract(PNScenario)


def test_pnscenario_constructor_exists():
    assert callable(PNScenario.__init__)


def test_pnscenario_constructor_args():
    sig = inspect.signature(PNScenario.__init__)
    params = list(sig.parameters.keys())



def test_petrinetsemantics::tm3petrinet::pntrace_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics::TM3PetriNet::PNTrace)


def test_petrinetsemantics::tm3petrinet::pntrace_constructor_exists():
    assert callable(petrinetsemantics::TM3PetriNet::PNTrace.__init__)


def test_petrinetsemantics::tm3petrinet::pntrace_constructor_args():
    sig = inspect.signature(petrinetsemantics::TM3PetriNet::PNTrace.__init__)
    params = list(sig.parameters.keys())



def test_pntrace_is_not_abstract():
    assert not inspect.isabstract(PNTrace)


def test_pntrace_constructor_exists():
    assert callable(PNTrace.__init__)


def test_pntrace_constructor_args():
    sig = inspect.signature(PNTrace.__init__)
    params = list(sig.parameters.keys())



def test_petrinetsemantics::tm3petrinet::pnscenario_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics::TM3PetriNet::PNScenario)


def test_petrinetsemantics::tm3petrinet::pnscenario_constructor_exists():
    assert callable(petrinetsemantics::TM3PetriNet::PNScenario.__init__)


def test_petrinetsemantics::tm3petrinet::pnscenario_constructor_args():
    sig = inspect.signature(petrinetsemantics::TM3PetriNet::PNScenario.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinetevent_is_not_abstract():
    assert not inspect.isabstract(PetriNetEvent)


def test_petrinetevent_constructor_exists():
    assert callable(PetriNetEvent.__init__)


def test_petrinetevent_constructor_args():
    sig = inspect.signature(PetriNetEvent.__init__)
    params = list(sig.parameters.keys())



def test_petrinetsemantics::edmmpetrinet::firetransitionevent_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics::EDMMPetriNet::FireTransitionEvent)


def test_petrinetsemantics::edmmpetrinet::firetransitionevent_constructor_exists():
    assert callable(petrinetsemantics::EDMMPetriNet::FireTransitionEvent.__init__)


def test_petrinetsemantics::edmmpetrinet::firetransitionevent_constructor_args():
    sig = inspect.signature(petrinetsemantics::EDMMPetriNet::FireTransitionEvent.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_petrinetsemantics::edmmpetrinet::firetransitionevent_has_time():
    assert hasattr(petrinetsemantics::EDMMPetriNet::FireTransitionEvent, "time")
    descriptor = None
    for klass in petrinetsemantics::EDMMPetriNet::FireTransitionEvent.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_pnsimevent_is_not_abstract():
    assert not inspect.isabstract(PNSimEvent)


def test_pnsimevent_constructor_exists():
    assert callable(PNSimEvent.__init__)


def test_pnsimevent_constructor_args():
    sig = inspect.signature(PNSimEvent.__init__)
    params = list(sig.parameters.keys())



def test_petrinetsemantics::edmmpetrinet::petrinetevent_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics::EDMMPetriNet::PetriNetEvent)


def test_petrinetsemantics::edmmpetrinet::petrinetevent_constructor_exists():
    assert callable(petrinetsemantics::EDMMPetriNet::PetriNetEvent.__init__)


def test_petrinetsemantics::edmmpetrinet::petrinetevent_constructor_args():
    sig = inspect.signature(petrinetsemantics::EDMMPetriNet::PetriNetEvent.__init__)
    params = list(sig.parameters.keys())



def test_petrinetsemantics::ddmmpetrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics::DDMMPetriNet::Arc)


def test_petrinetsemantics::ddmmpetrinet::arc_constructor_exists():
    assert callable(petrinetsemantics::DDMMPetriNet::Arc.__init__)


def test_petrinetsemantics::ddmmpetrinet::arc_constructor_args():
    sig = inspect.signature(petrinetsemantics::DDMMPetriNet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_petrinetsemantics::ddmmpetrinet::arc_has_weight():
    assert hasattr(petrinetsemantics::DDMMPetriNet::Arc, "weight")
    descriptor = None
    for klass in petrinetsemantics::DDMMPetriNet::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_petrinetsemantics::ddmmpetrinet::arc_has_kind():
    assert hasattr(petrinetsemantics::DDMMPetriNet::Arc, "kind")
    descriptor = None
    for klass in petrinetsemantics::DDMMPetriNet::Arc.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet)


def test_petrinet_constructor_exists():
    assert callable(PetriNet.__init__)


def test_petrinet_constructor_args():
    sig = inspect.signature(PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinetsemantics::ddmmpetrinet::node_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics::DDMMPetriNet::Node)


def test_petrinetsemantics::ddmmpetrinet::node_constructor_exists():
    assert callable(petrinetsemantics::DDMMPetriNet::Node.__init__)


def test_petrinetsemantics::ddmmpetrinet::node_constructor_args():
    sig = inspect.signature(petrinetsemantics::DDMMPetriNet::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetsemantics::ddmmpetrinet::node_has_name():
    assert hasattr(petrinetsemantics::DDMMPetriNet::Node, "name")
    descriptor = None
    for klass in petrinetsemantics::DDMMPetriNet::Node.__mro__:
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



def test_petrinetsemantics::sdmmpetrinet::petrinet::dynamic_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics::SDMMPetriNet::PetriNet::dynamic)


def test_petrinetsemantics::sdmmpetrinet::petrinet::dynamic_constructor_exists():
    assert callable(petrinetsemantics::SDMMPetriNet::PetriNet::dynamic.__init__)


def test_petrinetsemantics::sdmmpetrinet::petrinet::dynamic_constructor_args():
    sig = inspect.signature(petrinetsemantics::SDMMPetriNet::PetriNet::dynamic.__init__)
    params = list(sig.parameters.keys())



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_node::dynamic_is_not_abstract():
    assert not inspect.isabstract(Node::dynamic)


def test_node::dynamic_constructor_exists():
    assert callable(Node::dynamic.__init__)


def test_node::dynamic_constructor_args():
    sig = inspect.signature(Node::dynamic.__init__)
    params = list(sig.parameters.keys())



def test_petrinetsemantics::sdmmpetrinet::place::dynamic_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics::SDMMPetriNet::Place::dynamic)


def test_petrinetsemantics::sdmmpetrinet::place::dynamic_constructor_exists():
    assert callable(petrinetsemantics::SDMMPetriNet::Place::dynamic.__init__)


def test_petrinetsemantics::sdmmpetrinet::place::dynamic_constructor_args():
    sig = inspect.signature(petrinetsemantics::SDMMPetriNet::Place::dynamic.__init__)
    params = list(sig.parameters.keys())
    assert "marking" in params, "Missing parameter 'marking'"

def test_petrinetsemantics::sdmmpetrinet::place::dynamic_has_marking():
    assert hasattr(petrinetsemantics::SDMMPetriNet::Place::dynamic, "marking")
    descriptor = None
    for klass in petrinetsemantics::SDMMPetriNet::Place::dynamic.__mro__:
        if "marking" in klass.__dict__:
            descriptor = klass.__dict__["marking"]
            break
    assert isinstance(descriptor, property)



def test_petrinetsemantics::sdmmpetrinet::node::dynamic_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics::SDMMPetriNet::Node::dynamic)


def test_petrinetsemantics::sdmmpetrinet::node::dynamic_constructor_exists():
    assert callable(petrinetsemantics::SDMMPetriNet::Node::dynamic.__init__)


def test_petrinetsemantics::sdmmpetrinet::node::dynamic_constructor_args():
    sig = inspect.signature(petrinetsemantics::SDMMPetriNet::Node::dynamic.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinetsemantics::ddmmpetrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics::DDMMPetriNet::Transition)


def test_petrinetsemantics::ddmmpetrinet::transition_constructor_exists():
    assert callable(petrinetsemantics::DDMMPetriNet::Transition.__init__)


def test_petrinetsemantics::ddmmpetrinet::transition_constructor_args():
    sig = inspect.signature(petrinetsemantics::DDMMPetriNet::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "max_time" in params, "Missing parameter 'max_time'"
    assert "min_time" in params, "Missing parameter 'min_time'"

def test_petrinetsemantics::ddmmpetrinet::transition_has_max_time():
    assert hasattr(petrinetsemantics::DDMMPetriNet::Transition, "max_time")
    descriptor = None
    for klass in petrinetsemantics::DDMMPetriNet::Transition.__mro__:
        if "max_time" in klass.__dict__:
            descriptor = klass.__dict__["max_time"]
            break
    assert isinstance(descriptor, property)

def test_petrinetsemantics::ddmmpetrinet::transition_has_min_time():
    assert hasattr(petrinetsemantics::DDMMPetriNet::Transition, "min_time")
    descriptor = None
    for klass in petrinetsemantics::DDMMPetriNet::Transition.__mro__:
        if "min_time" in klass.__dict__:
            descriptor = klass.__dict__["min_time"]
            break
    assert isinstance(descriptor, property)



def test_petrinetsemantics::ddmmpetrinet::place_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics::DDMMPetriNet::Place)


def test_petrinetsemantics::ddmmpetrinet::place_constructor_exists():
    assert callable(petrinetsemantics::DDMMPetriNet::Place.__init__)


def test_petrinetsemantics::ddmmpetrinet::place_constructor_args():
    sig = inspect.signature(petrinetsemantics::DDMMPetriNet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "initialMarking" in params, "Missing parameter 'initialMarking'"

def test_petrinetsemantics::ddmmpetrinet::place_has_initialMarking():
    assert hasattr(petrinetsemantics::DDMMPetriNet::Place, "initialMarking")
    descriptor = None
    for klass in petrinetsemantics::DDMMPetriNet::Place.__mro__:
        if "initialMarking" in klass.__dict__:
            descriptor = klass.__dict__["initialMarking"]
            break
    assert isinstance(descriptor, property)



def test_petrinetsemantics::ddmmpetrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics::DDMMPetriNet::PetriNet)


def test_petrinetsemantics::ddmmpetrinet::petrinet_constructor_exists():
    assert callable(petrinetsemantics::DDMMPetriNet::PetriNet.__init__)


def test_petrinetsemantics::ddmmpetrinet::petrinet_constructor_args():
    sig = inspect.signature(petrinetsemantics::DDMMPetriNet::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetsemantics::ddmmpetrinet::petrinet_has_name():
    assert hasattr(petrinetsemantics::DDMMPetriNet::PetriNet, "name")
    descriptor = None
    for klass in petrinetsemantics::DDMMPetriNet::PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_arckind_exists():
    # Check that the Enumeration exists
    assert ArcKind is not None

def test_arckind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArcKind]
    expected_literals = [
        "normal",
        "read_arc",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArcKind"


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
petrinetsemantics::TM3PetriNet::PNSimEvent_strategy = st.builds(
    petrinetsemantics::TM3PetriNet::PNSimEvent,
    date=
        st.integers(),
    name=
        safe_text,
    internal=
        st.booleans()
)
PNScenario_strategy = st.builds(
    PNScenario,
)
petrinetsemantics::TM3PetriNet::PNTrace_strategy = st.builds(
    petrinetsemantics::TM3PetriNet::PNTrace,
)
PNTrace_strategy = st.builds(
    PNTrace,
)
petrinetsemantics::TM3PetriNet::PNScenario_strategy = st.builds(
    petrinetsemantics::TM3PetriNet::PNScenario,
)
Transition_strategy = st.builds(
    Transition,
)
PetriNetEvent_strategy = st.builds(
    PetriNetEvent,
)
petrinetsemantics::EDMMPetriNet::FireTransitionEvent_strategy = st.builds(
    petrinetsemantics::EDMMPetriNet::FireTransitionEvent,
    time=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
PNSimEvent_strategy = st.builds(
    PNSimEvent,
)
petrinetsemantics::EDMMPetriNet::PetriNetEvent_strategy = st.builds(
    petrinetsemantics::EDMMPetriNet::PetriNetEvent,
)
petrinetsemantics::DDMMPetriNet::Arc_strategy = st.builds(
    petrinetsemantics::DDMMPetriNet::Arc,
    weight=
        st.integers(),
    kind=
        safe_text
)
PetriNet_strategy = st.builds(
    PetriNet,
)
petrinetsemantics::DDMMPetriNet::Node_strategy = st.builds(
    petrinetsemantics::DDMMPetriNet::Node,
    name=
        safe_text
)
Arc_strategy = st.builds(
    Arc,
)
petrinetsemantics::SDMMPetriNet::PetriNet::dynamic_strategy = st.builds(
    petrinetsemantics::SDMMPetriNet::PetriNet::dynamic,
)
Place_strategy = st.builds(
    Place,
)
Node::dynamic_strategy = st.builds(
    Node::dynamic,
)
petrinetsemantics::SDMMPetriNet::Place::dynamic_strategy = st.builds(
    petrinetsemantics::SDMMPetriNet::Place::dynamic,
    marking=
        st.integers()
)
petrinetsemantics::SDMMPetriNet::Node::dynamic_strategy = st.builds(
    petrinetsemantics::SDMMPetriNet::Node::dynamic,
)
Node_strategy = st.builds(
    Node,
)
petrinetsemantics::DDMMPetriNet::Transition_strategy = st.builds(
    petrinetsemantics::DDMMPetriNet::Transition,
    max_time=
        st.integers(),
    min_time=
        st.integers()
)
petrinetsemantics::DDMMPetriNet::Place_strategy = st.builds(
    petrinetsemantics::DDMMPetriNet::Place,
    initialMarking=
        st.integers()
)
petrinetsemantics::DDMMPetriNet::PetriNet_strategy = st.builds(
    petrinetsemantics::DDMMPetriNet::PetriNet,
    name=
        safe_text
)

@given(instance=petrinetsemantics::TM3PetriNet::PNSimEvent_strategy)
@settings(max_examples=50)
def test_petrinetsemantics::tm3petrinet::pnsimevent_instantiation(instance):
    assert isinstance(instance, petrinetsemantics::TM3PetriNet::PNSimEvent)

@given(instance=petrinetsemantics::TM3PetriNet::PNSimEvent_strategy)
def test_petrinetsemantics::tm3petrinet::pnsimevent_date_type(instance):
    assert isinstance(instance.date, int)


@given(instance=petrinetsemantics::TM3PetriNet::PNSimEvent_strategy)
def test_petrinetsemantics::tm3petrinet::pnsimevent_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=petrinetsemantics::TM3PetriNet::PNSimEvent_strategy)
def test_petrinetsemantics::tm3petrinet::pnsimevent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinetsemantics::TM3PetriNet::PNSimEvent_strategy)
def test_petrinetsemantics::tm3petrinet::pnsimevent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetsemantics::TM3PetriNet::PNSimEvent_strategy)
def test_petrinetsemantics::tm3petrinet::pnsimevent_internal_type(instance):
    assert isinstance(instance.internal, bool)


@given(instance=petrinetsemantics::TM3PetriNet::PNSimEvent_strategy)
def test_petrinetsemantics::tm3petrinet::pnsimevent_internal_setter(instance):
    original = instance.internal
    instance.internal = original
    assert instance.internal == original

@given(instance=PNScenario_strategy)
@settings(max_examples=50)
def test_pnscenario_instantiation(instance):
    assert isinstance(instance, PNScenario)

@given(instance=petrinetsemantics::TM3PetriNet::PNTrace_strategy)
@settings(max_examples=50)
def test_petrinetsemantics::tm3petrinet::pntrace_instantiation(instance):
    assert isinstance(instance, petrinetsemantics::TM3PetriNet::PNTrace)

@given(instance=PNTrace_strategy)
@settings(max_examples=50)
def test_pntrace_instantiation(instance):
    assert isinstance(instance, PNTrace)

@given(instance=petrinetsemantics::TM3PetriNet::PNScenario_strategy)
@settings(max_examples=50)
def test_petrinetsemantics::tm3petrinet::pnscenario_instantiation(instance):
    assert isinstance(instance, petrinetsemantics::TM3PetriNet::PNScenario)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=PetriNetEvent_strategy)
@settings(max_examples=50)
def test_petrinetevent_instantiation(instance):
    assert isinstance(instance, PetriNetEvent)

@given(instance=petrinetsemantics::EDMMPetriNet::FireTransitionEvent_strategy)
@settings(max_examples=50)
def test_petrinetsemantics::edmmpetrinet::firetransitionevent_instantiation(instance):
    assert isinstance(instance, petrinetsemantics::EDMMPetriNet::FireTransitionEvent)

@given(instance=petrinetsemantics::EDMMPetriNet::FireTransitionEvent_strategy)
def test_petrinetsemantics::edmmpetrinet::firetransitionevent_time_type(instance):
    assert isinstance(instance.time, float)


@given(instance=petrinetsemantics::EDMMPetriNet::FireTransitionEvent_strategy)
def test_petrinetsemantics::edmmpetrinet::firetransitionevent_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=PNSimEvent_strategy)
@settings(max_examples=50)
def test_pnsimevent_instantiation(instance):
    assert isinstance(instance, PNSimEvent)

@given(instance=petrinetsemantics::EDMMPetriNet::PetriNetEvent_strategy)
@settings(max_examples=50)
def test_petrinetsemantics::edmmpetrinet::petrinetevent_instantiation(instance):
    assert isinstance(instance, petrinetsemantics::EDMMPetriNet::PetriNetEvent)

@given(instance=petrinetsemantics::DDMMPetriNet::Arc_strategy)
@settings(max_examples=50)
def test_petrinetsemantics::ddmmpetrinet::arc_instantiation(instance):
    assert isinstance(instance, petrinetsemantics::DDMMPetriNet::Arc)

@given(instance=petrinetsemantics::DDMMPetriNet::Arc_strategy)
def test_petrinetsemantics::ddmmpetrinet::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=petrinetsemantics::DDMMPetriNet::Arc_strategy)
def test_petrinetsemantics::ddmmpetrinet::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=petrinetsemantics::DDMMPetriNet::Arc_strategy)
def test_petrinetsemantics::ddmmpetrinet::arc_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=petrinetsemantics::DDMMPetriNet::Arc_strategy)
def test_petrinetsemantics::ddmmpetrinet::arc_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet)

@given(instance=petrinetsemantics::DDMMPetriNet::Node_strategy)
@settings(max_examples=50)
def test_petrinetsemantics::ddmmpetrinet::node_instantiation(instance):
    assert isinstance(instance, petrinetsemantics::DDMMPetriNet::Node)

@given(instance=petrinetsemantics::DDMMPetriNet::Node_strategy)
def test_petrinetsemantics::ddmmpetrinet::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinetsemantics::DDMMPetriNet::Node_strategy)
def test_petrinetsemantics::ddmmpetrinet::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petrinetsemantics::SDMMPetriNet::PetriNet::dynamic_strategy)
@settings(max_examples=50)
def test_petrinetsemantics::sdmmpetrinet::petrinet::dynamic_instantiation(instance):
    assert isinstance(instance, petrinetsemantics::SDMMPetriNet::PetriNet::dynamic)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=Node::dynamic_strategy)
@settings(max_examples=50)
def test_node::dynamic_instantiation(instance):
    assert isinstance(instance, Node::dynamic)

@given(instance=petrinetsemantics::SDMMPetriNet::Place::dynamic_strategy)
@settings(max_examples=50)
def test_petrinetsemantics::sdmmpetrinet::place::dynamic_instantiation(instance):
    assert isinstance(instance, petrinetsemantics::SDMMPetriNet::Place::dynamic)

@given(instance=petrinetsemantics::SDMMPetriNet::Place::dynamic_strategy)
def test_petrinetsemantics::sdmmpetrinet::place::dynamic_marking_type(instance):
    assert isinstance(instance.marking, int)


@given(instance=petrinetsemantics::SDMMPetriNet::Place::dynamic_strategy)
def test_petrinetsemantics::sdmmpetrinet::place::dynamic_marking_setter(instance):
    original = instance.marking
    instance.marking = original
    assert instance.marking == original

@given(instance=petrinetsemantics::SDMMPetriNet::Node::dynamic_strategy)
@settings(max_examples=50)
def test_petrinetsemantics::sdmmpetrinet::node::dynamic_instantiation(instance):
    assert isinstance(instance, petrinetsemantics::SDMMPetriNet::Node::dynamic)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinetsemantics::DDMMPetriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinetsemantics::ddmmpetrinet::transition_instantiation(instance):
    assert isinstance(instance, petrinetsemantics::DDMMPetriNet::Transition)

@given(instance=petrinetsemantics::DDMMPetriNet::Transition_strategy)
def test_petrinetsemantics::ddmmpetrinet::transition_max_time_type(instance):
    assert isinstance(instance.max_time, int)


@given(instance=petrinetsemantics::DDMMPetriNet::Transition_strategy)
def test_petrinetsemantics::ddmmpetrinet::transition_max_time_setter(instance):
    original = instance.max_time
    instance.max_time = original
    assert instance.max_time == original

@given(instance=petrinetsemantics::DDMMPetriNet::Transition_strategy)
def test_petrinetsemantics::ddmmpetrinet::transition_min_time_type(instance):
    assert isinstance(instance.min_time, int)


@given(instance=petrinetsemantics::DDMMPetriNet::Transition_strategy)
def test_petrinetsemantics::ddmmpetrinet::transition_min_time_setter(instance):
    original = instance.min_time
    instance.min_time = original
    assert instance.min_time == original

@given(instance=petrinetsemantics::DDMMPetriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinetsemantics::ddmmpetrinet::place_instantiation(instance):
    assert isinstance(instance, petrinetsemantics::DDMMPetriNet::Place)

@given(instance=petrinetsemantics::DDMMPetriNet::Place_strategy)
def test_petrinetsemantics::ddmmpetrinet::place_initialMarking_type(instance):
    assert isinstance(instance.initialMarking, int)


@given(instance=petrinetsemantics::DDMMPetriNet::Place_strategy)
def test_petrinetsemantics::ddmmpetrinet::place_initialMarking_setter(instance):
    original = instance.initialMarking
    instance.initialMarking = original
    assert instance.initialMarking == original

@given(instance=petrinetsemantics::DDMMPetriNet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinetsemantics::ddmmpetrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petrinetsemantics::DDMMPetriNet::PetriNet)

@given(instance=petrinetsemantics::DDMMPetriNet::PetriNet_strategy)
def test_petrinetsemantics::ddmmpetrinet::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinetsemantics::DDMMPetriNet::PetriNet_strategy)
def test_petrinetsemantics::ddmmpetrinet::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
