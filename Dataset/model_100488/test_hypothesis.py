import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UMLMetamodelFragment::Event,
    Event,
    UMLMetamodelFragment::Transition,
    CompositeState,
    UMLMetamodelFragment::StateVertex,
    Transition,
    Stereotype,
    Class,
    StateMachine,
    UMLMetamodelFragment::Dependency,
    UMLMetamodelFragment::Generalization_,
    Dependency,
    Generalization_,
    UMLMetamodelFragment::Class,
    StateVertex,
    UMLMetamodelFragment::PseudoState,
    UMLMetamodelFragment::State,
    State,
    UMLMetamodelFragment::FinalState,
    UMLMetamodelFragment::SimpleState,
    UMLMetamodelFragment::CompositeState,
    UMLMetamodelFragment::StateMachine,
    UMLMetamodelFragment::Stereotype,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_umlmetamodelfragment::event_is_not_abstract():
    assert not inspect.isabstract(UMLMetamodelFragment::Event)


def test_umlmetamodelfragment::event_constructor_exists():
    assert callable(UMLMetamodelFragment::Event.__init__)


def test_umlmetamodelfragment::event_constructor_args():
    sig = inspect.signature(UMLMetamodelFragment::Event.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_umlmetamodelfragment::transition_is_not_abstract():
    assert not inspect.isabstract(UMLMetamodelFragment::Transition)


def test_umlmetamodelfragment::transition_constructor_exists():
    assert callable(UMLMetamodelFragment::Transition.__init__)


def test_umlmetamodelfragment::transition_constructor_args():
    sig = inspect.signature(UMLMetamodelFragment::Transition.__init__)
    params = list(sig.parameters.keys())



def test_compositestate_is_not_abstract():
    assert not inspect.isabstract(CompositeState)


def test_compositestate_constructor_exists():
    assert callable(CompositeState.__init__)


def test_compositestate_constructor_args():
    sig = inspect.signature(CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_umlmetamodelfragment::statevertex_is_not_abstract():
    assert not inspect.isabstract(UMLMetamodelFragment::StateVertex)


def test_umlmetamodelfragment::statevertex_constructor_exists():
    assert callable(UMLMetamodelFragment::StateVertex.__init__)


def test_umlmetamodelfragment::statevertex_constructor_args():
    sig = inspect.signature(UMLMetamodelFragment::StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_stereotype_is_not_abstract():
    assert not inspect.isabstract(Stereotype)


def test_stereotype_constructor_exists():
    assert callable(Stereotype.__init__)


def test_stereotype_constructor_args():
    sig = inspect.signature(Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_umlmetamodelfragment::dependency_is_not_abstract():
    assert not inspect.isabstract(UMLMetamodelFragment::Dependency)


def test_umlmetamodelfragment::dependency_constructor_exists():
    assert callable(UMLMetamodelFragment::Dependency.__init__)


def test_umlmetamodelfragment::dependency_constructor_args():
    sig = inspect.signature(UMLMetamodelFragment::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_umlmetamodelfragment::generalization__is_not_abstract():
    assert not inspect.isabstract(UMLMetamodelFragment::Generalization_)


def test_umlmetamodelfragment::generalization__constructor_exists():
    assert callable(UMLMetamodelFragment::Generalization_.__init__)


def test_umlmetamodelfragment::generalization__constructor_args():
    sig = inspect.signature(UMLMetamodelFragment::Generalization_.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_generalization__is_not_abstract():
    assert not inspect.isabstract(Generalization_)


def test_generalization__constructor_exists():
    assert callable(Generalization_.__init__)


def test_generalization__constructor_args():
    sig = inspect.signature(Generalization_.__init__)
    params = list(sig.parameters.keys())



def test_umlmetamodelfragment::class_is_not_abstract():
    assert not inspect.isabstract(UMLMetamodelFragment::Class)


def test_umlmetamodelfragment::class_constructor_exists():
    assert callable(UMLMetamodelFragment::Class.__init__)


def test_umlmetamodelfragment::class_constructor_args():
    sig = inspect.signature(UMLMetamodelFragment::Class.__init__)
    params = list(sig.parameters.keys())



def test_statevertex_is_not_abstract():
    assert not inspect.isabstract(StateVertex)


def test_statevertex_constructor_exists():
    assert callable(StateVertex.__init__)


def test_statevertex_constructor_args():
    sig = inspect.signature(StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_umlmetamodelfragment::pseudostate_is_not_abstract():
    assert not inspect.isabstract(UMLMetamodelFragment::PseudoState)


def test_umlmetamodelfragment::pseudostate_constructor_exists():
    assert callable(UMLMetamodelFragment::PseudoState.__init__)


def test_umlmetamodelfragment::pseudostate_constructor_args():
    sig = inspect.signature(UMLMetamodelFragment::PseudoState.__init__)
    params = list(sig.parameters.keys())



def test_umlmetamodelfragment::state_is_not_abstract():
    assert not inspect.isabstract(UMLMetamodelFragment::State)


def test_umlmetamodelfragment::state_constructor_exists():
    assert callable(UMLMetamodelFragment::State.__init__)


def test_umlmetamodelfragment::state_constructor_args():
    sig = inspect.signature(UMLMetamodelFragment::State.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_umlmetamodelfragment::finalstate_is_not_abstract():
    assert not inspect.isabstract(UMLMetamodelFragment::FinalState)


def test_umlmetamodelfragment::finalstate_constructor_exists():
    assert callable(UMLMetamodelFragment::FinalState.__init__)


def test_umlmetamodelfragment::finalstate_constructor_args():
    sig = inspect.signature(UMLMetamodelFragment::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_umlmetamodelfragment::simplestate_is_not_abstract():
    assert not inspect.isabstract(UMLMetamodelFragment::SimpleState)


def test_umlmetamodelfragment::simplestate_constructor_exists():
    assert callable(UMLMetamodelFragment::SimpleState.__init__)


def test_umlmetamodelfragment::simplestate_constructor_args():
    sig = inspect.signature(UMLMetamodelFragment::SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_umlmetamodelfragment::compositestate_is_not_abstract():
    assert not inspect.isabstract(UMLMetamodelFragment::CompositeState)


def test_umlmetamodelfragment::compositestate_constructor_exists():
    assert callable(UMLMetamodelFragment::CompositeState.__init__)


def test_umlmetamodelfragment::compositestate_constructor_args():
    sig = inspect.signature(UMLMetamodelFragment::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_umlmetamodelfragment::statemachine_is_not_abstract():
    assert not inspect.isabstract(UMLMetamodelFragment::StateMachine)


def test_umlmetamodelfragment::statemachine_constructor_exists():
    assert callable(UMLMetamodelFragment::StateMachine.__init__)


def test_umlmetamodelfragment::statemachine_constructor_args():
    sig = inspect.signature(UMLMetamodelFragment::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_umlmetamodelfragment::stereotype_is_not_abstract():
    assert not inspect.isabstract(UMLMetamodelFragment::Stereotype)


def test_umlmetamodelfragment::stereotype_constructor_exists():
    assert callable(UMLMetamodelFragment::Stereotype.__init__)


def test_umlmetamodelfragment::stereotype_constructor_args():
    sig = inspect.signature(UMLMetamodelFragment::Stereotype.__init__)
    params = list(sig.parameters.keys())
    assert "baseClass" in params, "Missing parameter 'baseClass'"

def test_umlmetamodelfragment::stereotype_has_baseClass():
    assert hasattr(UMLMetamodelFragment::Stereotype, "baseClass")
    descriptor = None
    for klass in UMLMetamodelFragment::Stereotype.__mro__:
        if "baseClass" in klass.__dict__:
            descriptor = klass.__dict__["baseClass"]
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
UMLMetamodelFragment::Event_strategy = st.builds(
    UMLMetamodelFragment::Event,
)
Event_strategy = st.builds(
    Event,
)
UMLMetamodelFragment::Transition_strategy = st.builds(
    UMLMetamodelFragment::Transition,
)
CompositeState_strategy = st.builds(
    CompositeState,
)
UMLMetamodelFragment::StateVertex_strategy = st.builds(
    UMLMetamodelFragment::StateVertex,
)
Transition_strategy = st.builds(
    Transition,
)
Stereotype_strategy = st.builds(
    Stereotype,
)
Class_strategy = st.builds(
    Class,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UMLMetamodelFragment::Dependency_strategy = st.builds(
    UMLMetamodelFragment::Dependency,
)
UMLMetamodelFragment::Generalization__strategy = st.builds(
    UMLMetamodelFragment::Generalization_,
)
Dependency_strategy = st.builds(
    Dependency,
)
Generalization__strategy = st.builds(
    Generalization_,
)
UMLMetamodelFragment::Class_strategy = st.builds(
    UMLMetamodelFragment::Class,
)
StateVertex_strategy = st.builds(
    StateVertex,
)
UMLMetamodelFragment::PseudoState_strategy = st.builds(
    UMLMetamodelFragment::PseudoState,
)
UMLMetamodelFragment::State_strategy = st.builds(
    UMLMetamodelFragment::State,
)
State_strategy = st.builds(
    State,
)
UMLMetamodelFragment::FinalState_strategy = st.builds(
    UMLMetamodelFragment::FinalState,
)
UMLMetamodelFragment::SimpleState_strategy = st.builds(
    UMLMetamodelFragment::SimpleState,
)
UMLMetamodelFragment::CompositeState_strategy = st.builds(
    UMLMetamodelFragment::CompositeState,
)
UMLMetamodelFragment::StateMachine_strategy = st.builds(
    UMLMetamodelFragment::StateMachine,
)
UMLMetamodelFragment::Stereotype_strategy = st.builds(
    UMLMetamodelFragment::Stereotype,
    baseClass=
        safe_text
)

@given(instance=UMLMetamodelFragment::Event_strategy)
@settings(max_examples=50)
def test_umlmetamodelfragment::event_instantiation(instance):
    assert isinstance(instance, UMLMetamodelFragment::Event)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=UMLMetamodelFragment::Transition_strategy)
@settings(max_examples=50)
def test_umlmetamodelfragment::transition_instantiation(instance):
    assert isinstance(instance, UMLMetamodelFragment::Transition)

@given(instance=CompositeState_strategy)
@settings(max_examples=50)
def test_compositestate_instantiation(instance):
    assert isinstance(instance, CompositeState)

@given(instance=UMLMetamodelFragment::StateVertex_strategy)
@settings(max_examples=50)
def test_umlmetamodelfragment::statevertex_instantiation(instance):
    assert isinstance(instance, UMLMetamodelFragment::StateVertex)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Stereotype_strategy)
@settings(max_examples=50)
def test_stereotype_instantiation(instance):
    assert isinstance(instance, Stereotype)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UMLMetamodelFragment::Dependency_strategy)
@settings(max_examples=50)
def test_umlmetamodelfragment::dependency_instantiation(instance):
    assert isinstance(instance, UMLMetamodelFragment::Dependency)

@given(instance=UMLMetamodelFragment::Generalization__strategy)
@settings(max_examples=50)
def test_umlmetamodelfragment::generalization__instantiation(instance):
    assert isinstance(instance, UMLMetamodelFragment::Generalization_)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=Generalization__strategy)
@settings(max_examples=50)
def test_generalization__instantiation(instance):
    assert isinstance(instance, Generalization_)

@given(instance=UMLMetamodelFragment::Class_strategy)
@settings(max_examples=50)
def test_umlmetamodelfragment::class_instantiation(instance):
    assert isinstance(instance, UMLMetamodelFragment::Class)

@given(instance=StateVertex_strategy)
@settings(max_examples=50)
def test_statevertex_instantiation(instance):
    assert isinstance(instance, StateVertex)

@given(instance=UMLMetamodelFragment::PseudoState_strategy)
@settings(max_examples=50)
def test_umlmetamodelfragment::pseudostate_instantiation(instance):
    assert isinstance(instance, UMLMetamodelFragment::PseudoState)

@given(instance=UMLMetamodelFragment::State_strategy)
@settings(max_examples=50)
def test_umlmetamodelfragment::state_instantiation(instance):
    assert isinstance(instance, UMLMetamodelFragment::State)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=UMLMetamodelFragment::FinalState_strategy)
@settings(max_examples=50)
def test_umlmetamodelfragment::finalstate_instantiation(instance):
    assert isinstance(instance, UMLMetamodelFragment::FinalState)

@given(instance=UMLMetamodelFragment::SimpleState_strategy)
@settings(max_examples=50)
def test_umlmetamodelfragment::simplestate_instantiation(instance):
    assert isinstance(instance, UMLMetamodelFragment::SimpleState)

@given(instance=UMLMetamodelFragment::CompositeState_strategy)
@settings(max_examples=50)
def test_umlmetamodelfragment::compositestate_instantiation(instance):
    assert isinstance(instance, UMLMetamodelFragment::CompositeState)

@given(instance=UMLMetamodelFragment::StateMachine_strategy)
@settings(max_examples=50)
def test_umlmetamodelfragment::statemachine_instantiation(instance):
    assert isinstance(instance, UMLMetamodelFragment::StateMachine)

@given(instance=UMLMetamodelFragment::Stereotype_strategy)
@settings(max_examples=50)
def test_umlmetamodelfragment::stereotype_instantiation(instance):
    assert isinstance(instance, UMLMetamodelFragment::Stereotype)

@given(instance=UMLMetamodelFragment::Stereotype_strategy)
def test_umlmetamodelfragment::stereotype_baseClass_type(instance):
    assert isinstance(instance.baseClass, str)


@given(instance=UMLMetamodelFragment::Stereotype_strategy)
def test_umlmetamodelfragment::stereotype_baseClass_setter(instance):
    original = instance.baseClass
    instance.baseClass = original
    assert instance.baseClass == original
