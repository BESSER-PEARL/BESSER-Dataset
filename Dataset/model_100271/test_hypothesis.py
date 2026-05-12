import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Transition,
    Step,
    StepToTransition,
    TransitionToStep,
    Connection,
    Grafcet_StepToTransition,
    Grafcet_TransitionToStep,
    Grafcet,
    LocatedElement,
    Grafcet_NamedElement,
    Grafcet_LocatedElement,
    Element,
    Grafcet_Step,
    Grafcet_Transition,
    NamedElement,
    Grafcet_Connection,
    Grafcet_Element,
    Grafcet_Grafcet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_step_is_not_abstract():
    assert not inspect.isabstract(Step)


def test_step_constructor_exists():
    assert callable(Step.__init__)


def test_step_constructor_args():
    sig = inspect.signature(Step.__init__)
    params = list(sig.parameters.keys())



def test_steptotransition_is_not_abstract():
    assert not inspect.isabstract(StepToTransition)


def test_steptotransition_constructor_exists():
    assert callable(StepToTransition.__init__)


def test_steptotransition_constructor_args():
    sig = inspect.signature(StepToTransition.__init__)
    params = list(sig.parameters.keys())



def test_transitiontostep_is_not_abstract():
    assert not inspect.isabstract(TransitionToStep)


def test_transitiontostep_constructor_exists():
    assert callable(TransitionToStep.__init__)


def test_transitiontostep_constructor_args():
    sig = inspect.signature(TransitionToStep.__init__)
    params = list(sig.parameters.keys())



def test_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_grafcet_steptotransition_is_not_abstract():
    assert not inspect.isabstract(Grafcet_StepToTransition)


def test_grafcet_steptotransition_constructor_exists():
    assert callable(Grafcet_StepToTransition.__init__)


def test_grafcet_steptotransition_constructor_args():
    sig = inspect.signature(Grafcet_StepToTransition.__init__)
    params = list(sig.parameters.keys())



def test_grafcet_transitiontostep_is_not_abstract():
    assert not inspect.isabstract(Grafcet_TransitionToStep)


def test_grafcet_transitiontostep_constructor_exists():
    assert callable(Grafcet_TransitionToStep.__init__)


def test_grafcet_transitiontostep_constructor_args():
    sig = inspect.signature(Grafcet_TransitionToStep.__init__)
    params = list(sig.parameters.keys())



def test_grafcet_is_not_abstract():
    assert not inspect.isabstract(Grafcet)


def test_grafcet_constructor_exists():
    assert callable(Grafcet.__init__)


def test_grafcet_constructor_args():
    sig = inspect.signature(Grafcet.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_grafcet_namedelement_is_not_abstract():
    assert not inspect.isabstract(Grafcet_NamedElement)


def test_grafcet_namedelement_constructor_exists():
    assert callable(Grafcet_NamedElement.__init__)


def test_grafcet_namedelement_constructor_args():
    sig = inspect.signature(Grafcet_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_grafcet_namedelement_has_name():
    assert hasattr(Grafcet_NamedElement, "name")
    descriptor = None
    for klass in Grafcet_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_grafcet_locatedelement_is_not_abstract():
    assert not inspect.isabstract(Grafcet_LocatedElement)


def test_grafcet_locatedelement_constructor_exists():
    assert callable(Grafcet_LocatedElement.__init__)


def test_grafcet_locatedelement_constructor_args():
    sig = inspect.signature(Grafcet_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_grafcet_locatedelement_has_location():
    assert hasattr(Grafcet_LocatedElement, "location")
    descriptor = None
    for klass in Grafcet_LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_grafcet_step_is_not_abstract():
    assert not inspect.isabstract(Grafcet_Step)


def test_grafcet_step_constructor_exists():
    assert callable(Grafcet_Step.__init__)


def test_grafcet_step_constructor_args():
    sig = inspect.signature(Grafcet_Step.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "isInitial" in params, "Missing parameter 'isInitial'"
    assert "action" in params, "Missing parameter 'action'"

def test_grafcet_step_has_isActive():
    assert hasattr(Grafcet_Step, "isActive")
    descriptor = None
    for klass in Grafcet_Step.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_grafcet_step_has_isInitial():
    assert hasattr(Grafcet_Step, "isInitial")
    descriptor = None
    for klass in Grafcet_Step.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)

def test_grafcet_step_has_action():
    assert hasattr(Grafcet_Step, "action")
    descriptor = None
    for klass in Grafcet_Step.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_grafcet_transition_is_not_abstract():
    assert not inspect.isabstract(Grafcet_Transition)


def test_grafcet_transition_constructor_exists():
    assert callable(Grafcet_Transition.__init__)


def test_grafcet_transition_constructor_args():
    sig = inspect.signature(Grafcet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_grafcet_transition_has_condition():
    assert hasattr(Grafcet_Transition, "condition")
    descriptor = None
    for klass in Grafcet_Transition.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_grafcet_connection_is_not_abstract():
    assert not inspect.isabstract(Grafcet_Connection)


def test_grafcet_connection_constructor_exists():
    assert callable(Grafcet_Connection.__init__)


def test_grafcet_connection_constructor_args():
    sig = inspect.signature(Grafcet_Connection.__init__)
    params = list(sig.parameters.keys())



def test_grafcet_element_is_not_abstract():
    assert not inspect.isabstract(Grafcet_Element)


def test_grafcet_element_constructor_exists():
    assert callable(Grafcet_Element.__init__)


def test_grafcet_element_constructor_args():
    sig = inspect.signature(Grafcet_Element.__init__)
    params = list(sig.parameters.keys())



def test_grafcet_grafcet_is_not_abstract():
    assert not inspect.isabstract(Grafcet_Grafcet)


def test_grafcet_grafcet_constructor_exists():
    assert callable(Grafcet_Grafcet.__init__)


def test_grafcet_grafcet_constructor_args():
    sig = inspect.signature(Grafcet_Grafcet.__init__)
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
Transition_strategy = st.builds(
    Transition,
)
Step_strategy = st.builds(
    Step,
)
StepToTransition_strategy = st.builds(
    StepToTransition,
)
TransitionToStep_strategy = st.builds(
    TransitionToStep,
)
Connection_strategy = st.builds(
    Connection,
)
Grafcet_StepToTransition_strategy = st.builds(
    Grafcet_StepToTransition,
)
Grafcet_TransitionToStep_strategy = st.builds(
    Grafcet_TransitionToStep,
)
Grafcet_strategy = st.builds(
    Grafcet,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
Grafcet_NamedElement_strategy = st.builds(
    Grafcet_NamedElement,
    name=
        safe_text
)
Grafcet_LocatedElement_strategy = st.builds(
    Grafcet_LocatedElement,
    location=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
Grafcet_Step_strategy = st.builds(
    Grafcet_Step,
    isActive=
        safe_text,
    isInitial=
        safe_text,
    action=
        safe_text
)
Grafcet_Transition_strategy = st.builds(
    Grafcet_Transition,
    condition=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Grafcet_Connection_strategy = st.builds(
    Grafcet_Connection,
)
Grafcet_Element_strategy = st.builds(
    Grafcet_Element,
)
Grafcet_Grafcet_strategy = st.builds(
    Grafcet_Grafcet,
)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Step_strategy)
@settings(max_examples=50)
def test_step_instantiation(instance):
    assert isinstance(instance, Step)

@given(instance=StepToTransition_strategy)
@settings(max_examples=50)
def test_steptotransition_instantiation(instance):
    assert isinstance(instance, StepToTransition)

@given(instance=TransitionToStep_strategy)
@settings(max_examples=50)
def test_transitiontostep_instantiation(instance):
    assert isinstance(instance, TransitionToStep)

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=Grafcet_StepToTransition_strategy)
@settings(max_examples=50)
def test_grafcet_steptotransition_instantiation(instance):
    assert isinstance(instance, Grafcet_StepToTransition)

@given(instance=Grafcet_TransitionToStep_strategy)
@settings(max_examples=50)
def test_grafcet_transitiontostep_instantiation(instance):
    assert isinstance(instance, Grafcet_TransitionToStep)

@given(instance=Grafcet_strategy)
@settings(max_examples=50)
def test_grafcet_instantiation(instance):
    assert isinstance(instance, Grafcet)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=Grafcet_NamedElement_strategy)
@settings(max_examples=50)
def test_grafcet_namedelement_instantiation(instance):
    assert isinstance(instance, Grafcet_NamedElement)



@given(instance=Grafcet_NamedElement_strategy)
def test_grafcet_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Grafcet_LocatedElement_strategy)
@settings(max_examples=50)
def test_grafcet_locatedelement_instantiation(instance):
    assert isinstance(instance, Grafcet_LocatedElement)



@given(instance=Grafcet_LocatedElement_strategy)
def test_grafcet_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=Grafcet_Step_strategy)
@settings(max_examples=50)
def test_grafcet_step_instantiation(instance):
    assert isinstance(instance, Grafcet_Step)



@given(instance=Grafcet_Step_strategy)
def test_grafcet_step_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original



@given(instance=Grafcet_Step_strategy)
def test_grafcet_step_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original



@given(instance=Grafcet_Step_strategy)
def test_grafcet_step_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=Grafcet_Transition_strategy)
@settings(max_examples=50)
def test_grafcet_transition_instantiation(instance):
    assert isinstance(instance, Grafcet_Transition)



@given(instance=Grafcet_Transition_strategy)
def test_grafcet_transition_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Grafcet_Connection_strategy)
@settings(max_examples=50)
def test_grafcet_connection_instantiation(instance):
    assert isinstance(instance, Grafcet_Connection)

@given(instance=Grafcet_Element_strategy)
@settings(max_examples=50)
def test_grafcet_element_instantiation(instance):
    assert isinstance(instance, Grafcet_Element)

@given(instance=Grafcet_Grafcet_strategy)
@settings(max_examples=50)
def test_grafcet_grafcet_instantiation(instance):
    assert isinstance(instance, Grafcet_Grafcet)
