import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petrinetsemantics_TM3PetriNet_PNSimEvent,
    PNScenario,
    petrinetsemantics_TM3PetriNet_PNTrace,
    PNTrace,
    petrinetsemantics_TM3PetriNet_PNScenario,
    Transition,
    PetriNetEvent,
    petrinetsemantics_EDMMPetriNet_FireTransitionEvent,
    PNSimEvent,
    petrinetsemantics_EDMMPetriNet_PetriNetEvent,
    petrinetsemantics_DDMMPetriNet_Arc,
    PetriNet,
    petrinetsemantics_DDMMPetriNet_Node,
    Arc,
    petrinetsemantics_SDMMPetriNet_PetriNet_dynamic,
    Place,
    Node_dynamic,
    petrinetsemantics_SDMMPetriNet_Place_dynamic,
    petrinetsemantics_SDMMPetriNet_Node_dynamic,
    Node,
    petrinetsemantics_DDMMPetriNet_Place,
    petrinetsemantics_DDMMPetriNet_Transition,
    petrinetsemantics_DDMMPetriNet_PetriNet,
    ArcKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetsemantics_tm3petrinet_pnsimevent_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics_TM3PetriNet_PNSimEvent)


def test_petrinetsemantics_tm3petrinet_pnsimevent_constructor_exists():
    assert callable(petrinetsemantics_TM3PetriNet_PNSimEvent.__init__)


def test_petrinetsemantics_tm3petrinet_pnsimevent_constructor_args():
    sig = inspect.signature(petrinetsemantics_TM3PetriNet_PNSimEvent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "date" in params, "Missing parameter 'date'"
    assert "internal" in params, "Missing parameter 'internal'"

def test_petrinetsemantics_tm3petrinet_pnsimevent_has_name():
    assert hasattr(petrinetsemantics_TM3PetriNet_PNSimEvent, "name")
    descriptor = None
    for klass in petrinetsemantics_TM3PetriNet_PNSimEvent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetsemantics_tm3petrinet_pnsimevent_has_date():
    assert hasattr(petrinetsemantics_TM3PetriNet_PNSimEvent, "date")
    descriptor = None
    for klass in petrinetsemantics_TM3PetriNet_PNSimEvent.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_petrinetsemantics_tm3petrinet_pnsimevent_has_internal():
    assert hasattr(petrinetsemantics_TM3PetriNet_PNSimEvent, "internal")
    descriptor = None
    for klass in petrinetsemantics_TM3PetriNet_PNSimEvent.__mro__:
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



def test_petrinetsemantics_tm3petrinet_pntrace_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics_TM3PetriNet_PNTrace)


def test_petrinetsemantics_tm3petrinet_pntrace_constructor_exists():
    assert callable(petrinetsemantics_TM3PetriNet_PNTrace.__init__)


def test_petrinetsemantics_tm3petrinet_pntrace_constructor_args():
    sig = inspect.signature(petrinetsemantics_TM3PetriNet_PNTrace.__init__)
    params = list(sig.parameters.keys())



def test_pntrace_is_not_abstract():
    assert not inspect.isabstract(PNTrace)


def test_pntrace_constructor_exists():
    assert callable(PNTrace.__init__)


def test_pntrace_constructor_args():
    sig = inspect.signature(PNTrace.__init__)
    params = list(sig.parameters.keys())



def test_petrinetsemantics_tm3petrinet_pnscenario_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics_TM3PetriNet_PNScenario)


def test_petrinetsemantics_tm3petrinet_pnscenario_constructor_exists():
    assert callable(petrinetsemantics_TM3PetriNet_PNScenario.__init__)


def test_petrinetsemantics_tm3petrinet_pnscenario_constructor_args():
    sig = inspect.signature(petrinetsemantics_TM3PetriNet_PNScenario.__init__)
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



def test_petrinetsemantics_edmmpetrinet_firetransitionevent_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics_EDMMPetriNet_FireTransitionEvent)


def test_petrinetsemantics_edmmpetrinet_firetransitionevent_constructor_exists():
    assert callable(petrinetsemantics_EDMMPetriNet_FireTransitionEvent.__init__)


def test_petrinetsemantics_edmmpetrinet_firetransitionevent_constructor_args():
    sig = inspect.signature(petrinetsemantics_EDMMPetriNet_FireTransitionEvent.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_petrinetsemantics_edmmpetrinet_firetransitionevent_has_time():
    assert hasattr(petrinetsemantics_EDMMPetriNet_FireTransitionEvent, "time")
    descriptor = None
    for klass in petrinetsemantics_EDMMPetriNet_FireTransitionEvent.__mro__:
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



def test_petrinetsemantics_edmmpetrinet_petrinetevent_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics_EDMMPetriNet_PetriNetEvent)


def test_petrinetsemantics_edmmpetrinet_petrinetevent_constructor_exists():
    assert callable(petrinetsemantics_EDMMPetriNet_PetriNetEvent.__init__)


def test_petrinetsemantics_edmmpetrinet_petrinetevent_constructor_args():
    sig = inspect.signature(petrinetsemantics_EDMMPetriNet_PetriNetEvent.__init__)
    params = list(sig.parameters.keys())



def test_petrinetsemantics_ddmmpetrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics_DDMMPetriNet_Arc)


def test_petrinetsemantics_ddmmpetrinet_arc_constructor_exists():
    assert callable(petrinetsemantics_DDMMPetriNet_Arc.__init__)


def test_petrinetsemantics_ddmmpetrinet_arc_constructor_args():
    sig = inspect.signature(petrinetsemantics_DDMMPetriNet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinetsemantics_ddmmpetrinet_arc_has_kind():
    assert hasattr(petrinetsemantics_DDMMPetriNet_Arc, "kind")
    descriptor = None
    for klass in petrinetsemantics_DDMMPetriNet_Arc.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_petrinetsemantics_ddmmpetrinet_arc_has_weight():
    assert hasattr(petrinetsemantics_DDMMPetriNet_Arc, "weight")
    descriptor = None
    for klass in petrinetsemantics_DDMMPetriNet_Arc.__mro__:
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



def test_petrinetsemantics_ddmmpetrinet_node_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics_DDMMPetriNet_Node)


def test_petrinetsemantics_ddmmpetrinet_node_constructor_exists():
    assert callable(petrinetsemantics_DDMMPetriNet_Node.__init__)


def test_petrinetsemantics_ddmmpetrinet_node_constructor_args():
    sig = inspect.signature(petrinetsemantics_DDMMPetriNet_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetsemantics_ddmmpetrinet_node_has_name():
    assert hasattr(petrinetsemantics_DDMMPetriNet_Node, "name")
    descriptor = None
    for klass in petrinetsemantics_DDMMPetriNet_Node.__mro__:
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



def test_petrinetsemantics_sdmmpetrinet_petrinet_dynamic_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics_SDMMPetriNet_PetriNet_dynamic)


def test_petrinetsemantics_sdmmpetrinet_petrinet_dynamic_constructor_exists():
    assert callable(petrinetsemantics_SDMMPetriNet_PetriNet_dynamic.__init__)


def test_petrinetsemantics_sdmmpetrinet_petrinet_dynamic_constructor_args():
    sig = inspect.signature(petrinetsemantics_SDMMPetriNet_PetriNet_dynamic.__init__)
    params = list(sig.parameters.keys())



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_node_dynamic_is_not_abstract():
    assert not inspect.isabstract(Node_dynamic)


def test_node_dynamic_constructor_exists():
    assert callable(Node_dynamic.__init__)


def test_node_dynamic_constructor_args():
    sig = inspect.signature(Node_dynamic.__init__)
    params = list(sig.parameters.keys())



def test_petrinetsemantics_sdmmpetrinet_place_dynamic_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics_SDMMPetriNet_Place_dynamic)


def test_petrinetsemantics_sdmmpetrinet_place_dynamic_constructor_exists():
    assert callable(petrinetsemantics_SDMMPetriNet_Place_dynamic.__init__)


def test_petrinetsemantics_sdmmpetrinet_place_dynamic_constructor_args():
    sig = inspect.signature(petrinetsemantics_SDMMPetriNet_Place_dynamic.__init__)
    params = list(sig.parameters.keys())
    assert "marking" in params, "Missing parameter 'marking'"

def test_petrinetsemantics_sdmmpetrinet_place_dynamic_has_marking():
    assert hasattr(petrinetsemantics_SDMMPetriNet_Place_dynamic, "marking")
    descriptor = None
    for klass in petrinetsemantics_SDMMPetriNet_Place_dynamic.__mro__:
        if "marking" in klass.__dict__:
            descriptor = klass.__dict__["marking"]
            break
    assert isinstance(descriptor, property)



def test_petrinetsemantics_sdmmpetrinet_node_dynamic_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics_SDMMPetriNet_Node_dynamic)


def test_petrinetsemantics_sdmmpetrinet_node_dynamic_constructor_exists():
    assert callable(petrinetsemantics_SDMMPetriNet_Node_dynamic.__init__)


def test_petrinetsemantics_sdmmpetrinet_node_dynamic_constructor_args():
    sig = inspect.signature(petrinetsemantics_SDMMPetriNet_Node_dynamic.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinetsemantics_ddmmpetrinet_place_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics_DDMMPetriNet_Place)


def test_petrinetsemantics_ddmmpetrinet_place_constructor_exists():
    assert callable(petrinetsemantics_DDMMPetriNet_Place.__init__)


def test_petrinetsemantics_ddmmpetrinet_place_constructor_args():
    sig = inspect.signature(petrinetsemantics_DDMMPetriNet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "initialMarking" in params, "Missing parameter 'initialMarking'"

def test_petrinetsemantics_ddmmpetrinet_place_has_initialMarking():
    assert hasattr(petrinetsemantics_DDMMPetriNet_Place, "initialMarking")
    descriptor = None
    for klass in petrinetsemantics_DDMMPetriNet_Place.__mro__:
        if "initialMarking" in klass.__dict__:
            descriptor = klass.__dict__["initialMarking"]
            break
    assert isinstance(descriptor, property)



def test_petrinetsemantics_ddmmpetrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics_DDMMPetriNet_Transition)


def test_petrinetsemantics_ddmmpetrinet_transition_constructor_exists():
    assert callable(petrinetsemantics_DDMMPetriNet_Transition.__init__)


def test_petrinetsemantics_ddmmpetrinet_transition_constructor_args():
    sig = inspect.signature(petrinetsemantics_DDMMPetriNet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "min_time" in params, "Missing parameter 'min_time'"
    assert "max_time" in params, "Missing parameter 'max_time'"

def test_petrinetsemantics_ddmmpetrinet_transition_has_min_time():
    assert hasattr(petrinetsemantics_DDMMPetriNet_Transition, "min_time")
    descriptor = None
    for klass in petrinetsemantics_DDMMPetriNet_Transition.__mro__:
        if "min_time" in klass.__dict__:
            descriptor = klass.__dict__["min_time"]
            break
    assert isinstance(descriptor, property)

def test_petrinetsemantics_ddmmpetrinet_transition_has_max_time():
    assert hasattr(petrinetsemantics_DDMMPetriNet_Transition, "max_time")
    descriptor = None
    for klass in petrinetsemantics_DDMMPetriNet_Transition.__mro__:
        if "max_time" in klass.__dict__:
            descriptor = klass.__dict__["max_time"]
            break
    assert isinstance(descriptor, property)



def test_petrinetsemantics_ddmmpetrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinetsemantics_DDMMPetriNet_PetriNet)


def test_petrinetsemantics_ddmmpetrinet_petrinet_constructor_exists():
    assert callable(petrinetsemantics_DDMMPetriNet_PetriNet.__init__)


def test_petrinetsemantics_ddmmpetrinet_petrinet_constructor_args():
    sig = inspect.signature(petrinetsemantics_DDMMPetriNet_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetsemantics_ddmmpetrinet_petrinet_has_name():
    assert hasattr(petrinetsemantics_DDMMPetriNet_PetriNet, "name")
    descriptor = None
    for klass in petrinetsemantics_DDMMPetriNet_PetriNet.__mro__:
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
        "read_arc",
        "normal",
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
petrinetsemantics_TM3PetriNet_PNSimEvent_strategy = st.builds(
    petrinetsemantics_TM3PetriNet_PNSimEvent,
    name=
        safe_text,
    date=
        st.integers(),
    internal=
        st.booleans()
)
PNScenario_strategy = st.builds(
    PNScenario,
)
petrinetsemantics_TM3PetriNet_PNTrace_strategy = st.builds(
    petrinetsemantics_TM3PetriNet_PNTrace,
)
PNTrace_strategy = st.builds(
    PNTrace,
)
petrinetsemantics_TM3PetriNet_PNScenario_strategy = st.builds(
    petrinetsemantics_TM3PetriNet_PNScenario,
)
Transition_strategy = st.builds(
    Transition,
)
PetriNetEvent_strategy = st.builds(
    PetriNetEvent,
)
petrinetsemantics_EDMMPetriNet_FireTransitionEvent_strategy = st.builds(
    petrinetsemantics_EDMMPetriNet_FireTransitionEvent,
    time=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
PNSimEvent_strategy = st.builds(
    PNSimEvent,
)
petrinetsemantics_EDMMPetriNet_PetriNetEvent_strategy = st.builds(
    petrinetsemantics_EDMMPetriNet_PetriNetEvent,
)
petrinetsemantics_DDMMPetriNet_Arc_strategy = st.builds(
    petrinetsemantics_DDMMPetriNet_Arc,
    kind=
        safe_text,
    weight=
        st.integers()
)
PetriNet_strategy = st.builds(
    PetriNet,
)
petrinetsemantics_DDMMPetriNet_Node_strategy = st.builds(
    petrinetsemantics_DDMMPetriNet_Node,
    name=
        safe_text
)
Arc_strategy = st.builds(
    Arc,
)
petrinetsemantics_SDMMPetriNet_PetriNet_dynamic_strategy = st.builds(
    petrinetsemantics_SDMMPetriNet_PetriNet_dynamic,
)
Place_strategy = st.builds(
    Place,
)
Node_dynamic_strategy = st.builds(
    Node_dynamic,
)
petrinetsemantics_SDMMPetriNet_Place_dynamic_strategy = st.builds(
    petrinetsemantics_SDMMPetriNet_Place_dynamic,
    marking=
        st.integers()
)
petrinetsemantics_SDMMPetriNet_Node_dynamic_strategy = st.builds(
    petrinetsemantics_SDMMPetriNet_Node_dynamic,
)
Node_strategy = st.builds(
    Node,
)
petrinetsemantics_DDMMPetriNet_Place_strategy = st.builds(
    petrinetsemantics_DDMMPetriNet_Place,
    initialMarking=
        st.integers()
)
petrinetsemantics_DDMMPetriNet_Transition_strategy = st.builds(
    petrinetsemantics_DDMMPetriNet_Transition,
    min_time=
        st.integers(),
    max_time=
        st.integers()
)
petrinetsemantics_DDMMPetriNet_PetriNet_strategy = st.builds(
    petrinetsemantics_DDMMPetriNet_PetriNet,
    name=
        safe_text
)

@given(instance=petrinetsemantics_TM3PetriNet_PNSimEvent_strategy)
@settings(max_examples=50)
def test_petrinetsemantics_tm3petrinet_pnsimevent_instantiation(instance):
    assert isinstance(instance, petrinetsemantics_TM3PetriNet_PNSimEvent)



@given(instance=petrinetsemantics_TM3PetriNet_PNSimEvent_strategy)
def test_petrinetsemantics_tm3petrinet_pnsimevent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=petrinetsemantics_TM3PetriNet_PNSimEvent_strategy)
def test_petrinetsemantics_tm3petrinet_pnsimevent_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=petrinetsemantics_TM3PetriNet_PNSimEvent_strategy)
def test_petrinetsemantics_tm3petrinet_pnsimevent_internal_setter(instance):
    original = instance.internal
    instance.internal = original
    assert instance.internal == original

@given(instance=PNScenario_strategy)
@settings(max_examples=50)
def test_pnscenario_instantiation(instance):
    assert isinstance(instance, PNScenario)

@given(instance=petrinetsemantics_TM3PetriNet_PNTrace_strategy)
@settings(max_examples=50)
def test_petrinetsemantics_tm3petrinet_pntrace_instantiation(instance):
    assert isinstance(instance, petrinetsemantics_TM3PetriNet_PNTrace)

@given(instance=PNTrace_strategy)
@settings(max_examples=50)
def test_pntrace_instantiation(instance):
    assert isinstance(instance, PNTrace)

@given(instance=petrinetsemantics_TM3PetriNet_PNScenario_strategy)
@settings(max_examples=50)
def test_petrinetsemantics_tm3petrinet_pnscenario_instantiation(instance):
    assert isinstance(instance, petrinetsemantics_TM3PetriNet_PNScenario)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=PetriNetEvent_strategy)
@settings(max_examples=50)
def test_petrinetevent_instantiation(instance):
    assert isinstance(instance, PetriNetEvent)

@given(instance=petrinetsemantics_EDMMPetriNet_FireTransitionEvent_strategy)
@settings(max_examples=50)
def test_petrinetsemantics_edmmpetrinet_firetransitionevent_instantiation(instance):
    assert isinstance(instance, petrinetsemantics_EDMMPetriNet_FireTransitionEvent)



@given(instance=petrinetsemantics_EDMMPetriNet_FireTransitionEvent_strategy)
def test_petrinetsemantics_edmmpetrinet_firetransitionevent_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=PNSimEvent_strategy)
@settings(max_examples=50)
def test_pnsimevent_instantiation(instance):
    assert isinstance(instance, PNSimEvent)

@given(instance=petrinetsemantics_EDMMPetriNet_PetriNetEvent_strategy)
@settings(max_examples=50)
def test_petrinetsemantics_edmmpetrinet_petrinetevent_instantiation(instance):
    assert isinstance(instance, petrinetsemantics_EDMMPetriNet_PetriNetEvent)

@given(instance=petrinetsemantics_DDMMPetriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinetsemantics_ddmmpetrinet_arc_instantiation(instance):
    assert isinstance(instance, petrinetsemantics_DDMMPetriNet_Arc)



@given(instance=petrinetsemantics_DDMMPetriNet_Arc_strategy)
def test_petrinetsemantics_ddmmpetrinet_arc_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=petrinetsemantics_DDMMPetriNet_Arc_strategy)
def test_petrinetsemantics_ddmmpetrinet_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet)

@given(instance=petrinetsemantics_DDMMPetriNet_Node_strategy)
@settings(max_examples=50)
def test_petrinetsemantics_ddmmpetrinet_node_instantiation(instance):
    assert isinstance(instance, petrinetsemantics_DDMMPetriNet_Node)



@given(instance=petrinetsemantics_DDMMPetriNet_Node_strategy)
def test_petrinetsemantics_ddmmpetrinet_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petrinetsemantics_SDMMPetriNet_PetriNet_dynamic_strategy)
@settings(max_examples=50)
def test_petrinetsemantics_sdmmpetrinet_petrinet_dynamic_instantiation(instance):
    assert isinstance(instance, petrinetsemantics_SDMMPetriNet_PetriNet_dynamic)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=Node_dynamic_strategy)
@settings(max_examples=50)
def test_node_dynamic_instantiation(instance):
    assert isinstance(instance, Node_dynamic)

@given(instance=petrinetsemantics_SDMMPetriNet_Place_dynamic_strategy)
@settings(max_examples=50)
def test_petrinetsemantics_sdmmpetrinet_place_dynamic_instantiation(instance):
    assert isinstance(instance, petrinetsemantics_SDMMPetriNet_Place_dynamic)



@given(instance=petrinetsemantics_SDMMPetriNet_Place_dynamic_strategy)
def test_petrinetsemantics_sdmmpetrinet_place_dynamic_marking_setter(instance):
    original = instance.marking
    instance.marking = original
    assert instance.marking == original

@given(instance=petrinetsemantics_SDMMPetriNet_Node_dynamic_strategy)
@settings(max_examples=50)
def test_petrinetsemantics_sdmmpetrinet_node_dynamic_instantiation(instance):
    assert isinstance(instance, petrinetsemantics_SDMMPetriNet_Node_dynamic)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinetsemantics_DDMMPetriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinetsemantics_ddmmpetrinet_place_instantiation(instance):
    assert isinstance(instance, petrinetsemantics_DDMMPetriNet_Place)



@given(instance=petrinetsemantics_DDMMPetriNet_Place_strategy)
def test_petrinetsemantics_ddmmpetrinet_place_initialMarking_setter(instance):
    original = instance.initialMarking
    instance.initialMarking = original
    assert instance.initialMarking == original

@given(instance=petrinetsemantics_DDMMPetriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinetsemantics_ddmmpetrinet_transition_instantiation(instance):
    assert isinstance(instance, petrinetsemantics_DDMMPetriNet_Transition)



@given(instance=petrinetsemantics_DDMMPetriNet_Transition_strategy)
def test_petrinetsemantics_ddmmpetrinet_transition_min_time_setter(instance):
    original = instance.min_time
    instance.min_time = original
    assert instance.min_time == original



@given(instance=petrinetsemantics_DDMMPetriNet_Transition_strategy)
def test_petrinetsemantics_ddmmpetrinet_transition_max_time_setter(instance):
    original = instance.max_time
    instance.max_time = original
    assert instance.max_time == original

@given(instance=petrinetsemantics_DDMMPetriNet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinetsemantics_ddmmpetrinet_petrinet_instantiation(instance):
    assert isinstance(instance, petrinetsemantics_DDMMPetriNet_PetriNet)



@given(instance=petrinetsemantics_DDMMPetriNet_PetriNet_strategy)
def test_petrinetsemantics_ddmmpetrinet_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
