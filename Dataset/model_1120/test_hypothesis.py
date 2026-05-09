import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Element,
    MMInterModel::Guard,
    MMInterModel::StateConfiguration,
    MMInterModel::Component,
    MMInterModel::Attribute,
    MMInterModel::StateMachine,
    MMInterModel::StringEnumeration,
    MMInterModel::Event,
    MMInterModel::Model,
    MMInterModel::State,
    MMInterModel::Transition,
    MMInterModel::Element,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_mmintermodel::guard_is_not_abstract():
    assert not inspect.isabstract(MMInterModel::Guard)


def test_mmintermodel::guard_constructor_exists():
    assert callable(MMInterModel::Guard.__init__)


def test_mmintermodel::guard_constructor_args():
    sig = inspect.signature(MMInterModel::Guard.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"
    assert "transition" in params, "Missing parameter 'transition'"

def test_mmintermodel::guard_has_specification():
    assert hasattr(MMInterModel::Guard, "specification")
    descriptor = None
    for klass in MMInterModel::Guard.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::guard_has_transition():
    assert hasattr(MMInterModel::Guard, "transition")
    descriptor = None
    for klass in MMInterModel::Guard.__mro__:
        if "transition" in klass.__dict__:
            descriptor = klass.__dict__["transition"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel::stateconfiguration_is_not_abstract():
    assert not inspect.isabstract(MMInterModel::StateConfiguration)


def test_mmintermodel::stateconfiguration_constructor_exists():
    assert callable(MMInterModel::StateConfiguration.__init__)


def test_mmintermodel::stateconfiguration_constructor_args():
    sig = inspect.signature(MMInterModel::StateConfiguration.__init__)
    params = list(sig.parameters.keys())
    assert "model" in params, "Missing parameter 'model'"
    assert "configOperator" in params, "Missing parameter 'configOperator'"
    assert "negation" in params, "Missing parameter 'negation'"
    assert "condition" in params, "Missing parameter 'condition'"

def test_mmintermodel::stateconfiguration_has_model():
    assert hasattr(MMInterModel::StateConfiguration, "model")
    descriptor = None
    for klass in MMInterModel::StateConfiguration.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::stateconfiguration_has_configOperator():
    assert hasattr(MMInterModel::StateConfiguration, "configOperator")
    descriptor = None
    for klass in MMInterModel::StateConfiguration.__mro__:
        if "configOperator" in klass.__dict__:
            descriptor = klass.__dict__["configOperator"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::stateconfiguration_has_negation():
    assert hasattr(MMInterModel::StateConfiguration, "negation")
    descriptor = None
    for klass in MMInterModel::StateConfiguration.__mro__:
        if "negation" in klass.__dict__:
            descriptor = klass.__dict__["negation"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::stateconfiguration_has_condition():
    assert hasattr(MMInterModel::StateConfiguration, "condition")
    descriptor = None
    for klass in MMInterModel::StateConfiguration.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel::component_is_not_abstract():
    assert not inspect.isabstract(MMInterModel::Component)


def test_mmintermodel::component_constructor_exists():
    assert callable(MMInterModel::Component.__init__)


def test_mmintermodel::component_constructor_args():
    sig = inspect.signature(MMInterModel::Component.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfSpares" in params, "Missing parameter 'numberOfSpares'"
    assert "model" in params, "Missing parameter 'model'"

def test_mmintermodel::component_has_numberOfSpares():
    assert hasattr(MMInterModel::Component, "numberOfSpares")
    descriptor = None
    for klass in MMInterModel::Component.__mro__:
        if "numberOfSpares" in klass.__dict__:
            descriptor = klass.__dict__["numberOfSpares"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::component_has_model():
    assert hasattr(MMInterModel::Component, "model")
    descriptor = None
    for klass in MMInterModel::Component.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel::attribute_is_not_abstract():
    assert not inspect.isabstract(MMInterModel::Attribute)


def test_mmintermodel::attribute_constructor_exists():
    assert callable(MMInterModel::Attribute.__init__)


def test_mmintermodel::attribute_constructor_args():
    sig = inspect.signature(MMInterModel::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "component" in params, "Missing parameter 'component'"
    assert "model" in params, "Missing parameter 'model'"
    assert "type" in params, "Missing parameter 'type'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "isArray" in params, "Missing parameter 'isArray'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "arraySize" in params, "Missing parameter 'arraySize'"

def test_mmintermodel::attribute_has_defaultValue():
    assert hasattr(MMInterModel::Attribute, "defaultValue")
    descriptor = None
    for klass in MMInterModel::Attribute.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::attribute_has_component():
    assert hasattr(MMInterModel::Attribute, "component")
    descriptor = None
    for klass in MMInterModel::Attribute.__mro__:
        if "component" in klass.__dict__:
            descriptor = klass.__dict__["component"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::attribute_has_model():
    assert hasattr(MMInterModel::Attribute, "model")
    descriptor = None
    for klass in MMInterModel::Attribute.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::attribute_has_type():
    assert hasattr(MMInterModel::Attribute, "type")
    descriptor = None
    for klass in MMInterModel::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::attribute_has_lowerBound():
    assert hasattr(MMInterModel::Attribute, "lowerBound")
    descriptor = None
    for klass in MMInterModel::Attribute.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::attribute_has_isArray():
    assert hasattr(MMInterModel::Attribute, "isArray")
    descriptor = None
    for klass in MMInterModel::Attribute.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::attribute_has_upperBound():
    assert hasattr(MMInterModel::Attribute, "upperBound")
    descriptor = None
    for klass in MMInterModel::Attribute.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::attribute_has_arraySize():
    assert hasattr(MMInterModel::Attribute, "arraySize")
    descriptor = None
    for klass in MMInterModel::Attribute.__mro__:
        if "arraySize" in klass.__dict__:
            descriptor = klass.__dict__["arraySize"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel::statemachine_is_not_abstract():
    assert not inspect.isabstract(MMInterModel::StateMachine)


def test_mmintermodel::statemachine_constructor_exists():
    assert callable(MMInterModel::StateMachine.__init__)


def test_mmintermodel::statemachine_constructor_args():
    sig = inspect.signature(MMInterModel::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "component" in params, "Missing parameter 'component'"
    assert "type" in params, "Missing parameter 'type'"
    assert "superState" in params, "Missing parameter 'superState'"

def test_mmintermodel::statemachine_has_component():
    assert hasattr(MMInterModel::StateMachine, "component")
    descriptor = None
    for klass in MMInterModel::StateMachine.__mro__:
        if "component" in klass.__dict__:
            descriptor = klass.__dict__["component"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::statemachine_has_type():
    assert hasattr(MMInterModel::StateMachine, "type")
    descriptor = None
    for klass in MMInterModel::StateMachine.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::statemachine_has_superState():
    assert hasattr(MMInterModel::StateMachine, "superState")
    descriptor = None
    for klass in MMInterModel::StateMachine.__mro__:
        if "superState" in klass.__dict__:
            descriptor = klass.__dict__["superState"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel::stringenumeration_is_not_abstract():
    assert not inspect.isabstract(MMInterModel::StringEnumeration)


def test_mmintermodel::stringenumeration_constructor_exists():
    assert callable(MMInterModel::StringEnumeration.__init__)


def test_mmintermodel::stringenumeration_constructor_args():
    sig = inspect.signature(MMInterModel::StringEnumeration.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_mmintermodel::stringenumeration_has_attribute():
    assert hasattr(MMInterModel::StringEnumeration, "attribute")
    descriptor = None
    for klass in MMInterModel::StringEnumeration.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel::event_is_not_abstract():
    assert not inspect.isabstract(MMInterModel::Event)


def test_mmintermodel::event_constructor_exists():
    assert callable(MMInterModel::Event.__init__)


def test_mmintermodel::event_constructor_args():
    sig = inspect.signature(MMInterModel::Event.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "model" in params, "Missing parameter 'model'"

def test_mmintermodel::event_has_type():
    assert hasattr(MMInterModel::Event, "type")
    descriptor = None
    for klass in MMInterModel::Event.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::event_has_model():
    assert hasattr(MMInterModel::Event, "model")
    descriptor = None
    for klass in MMInterModel::Event.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel::model_is_not_abstract():
    assert not inspect.isabstract(MMInterModel::Model)


def test_mmintermodel::model_constructor_exists():
    assert callable(MMInterModel::Model.__init__)


def test_mmintermodel::model_constructor_args():
    sig = inspect.signature(MMInterModel::Model.__init__)
    params = list(sig.parameters.keys())



def test_mmintermodel::state_is_not_abstract():
    assert not inspect.isabstract(MMInterModel::State)


def test_mmintermodel::state_constructor_exists():
    assert callable(MMInterModel::State.__init__)


def test_mmintermodel::state_constructor_args():
    sig = inspect.signature(MMInterModel::State.__init__)
    params = list(sig.parameters.keys())
    assert "exitBehaviour" in params, "Missing parameter 'exitBehaviour'"
    assert "duringBehaviour" in params, "Missing parameter 'duringBehaviour'"
    assert "entryBehaviour" in params, "Missing parameter 'entryBehaviour'"
    assert "stateNumber" in params, "Missing parameter 'stateNumber'"
    assert "stateMachine" in params, "Missing parameter 'stateMachine'"
    assert "stateConfiguration" in params, "Missing parameter 'stateConfiguration'"

def test_mmintermodel::state_has_exitBehaviour():
    assert hasattr(MMInterModel::State, "exitBehaviour")
    descriptor = None
    for klass in MMInterModel::State.__mro__:
        if "exitBehaviour" in klass.__dict__:
            descriptor = klass.__dict__["exitBehaviour"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::state_has_duringBehaviour():
    assert hasattr(MMInterModel::State, "duringBehaviour")
    descriptor = None
    for klass in MMInterModel::State.__mro__:
        if "duringBehaviour" in klass.__dict__:
            descriptor = klass.__dict__["duringBehaviour"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::state_has_entryBehaviour():
    assert hasattr(MMInterModel::State, "entryBehaviour")
    descriptor = None
    for klass in MMInterModel::State.__mro__:
        if "entryBehaviour" in klass.__dict__:
            descriptor = klass.__dict__["entryBehaviour"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::state_has_stateNumber():
    assert hasattr(MMInterModel::State, "stateNumber")
    descriptor = None
    for klass in MMInterModel::State.__mro__:
        if "stateNumber" in klass.__dict__:
            descriptor = klass.__dict__["stateNumber"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::state_has_stateMachine():
    assert hasattr(MMInterModel::State, "stateMachine")
    descriptor = None
    for klass in MMInterModel::State.__mro__:
        if "stateMachine" in klass.__dict__:
            descriptor = klass.__dict__["stateMachine"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::state_has_stateConfiguration():
    assert hasattr(MMInterModel::State, "stateConfiguration")
    descriptor = None
    for klass in MMInterModel::State.__mro__:
        if "stateConfiguration" in klass.__dict__:
            descriptor = klass.__dict__["stateConfiguration"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel::transition_is_not_abstract():
    assert not inspect.isabstract(MMInterModel::Transition)


def test_mmintermodel::transition_constructor_exists():
    assert callable(MMInterModel::Transition.__init__)


def test_mmintermodel::transition_constructor_args():
    sig = inspect.signature(MMInterModel::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "stateMachine" in params, "Missing parameter 'stateMachine'"
    assert "action" in params, "Missing parameter 'action'"

def test_mmintermodel::transition_has_stateMachine():
    assert hasattr(MMInterModel::Transition, "stateMachine")
    descriptor = None
    for klass in MMInterModel::Transition.__mro__:
        if "stateMachine" in klass.__dict__:
            descriptor = klass.__dict__["stateMachine"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::transition_has_action():
    assert hasattr(MMInterModel::Transition, "action")
    descriptor = None
    for klass in MMInterModel::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel::element_is_not_abstract():
    assert not inspect.isabstract(MMInterModel::Element)


def test_mmintermodel::element_constructor_exists():
    assert callable(MMInterModel::Element.__init__)


def test_mmintermodel::element_constructor_args():
    sig = inspect.signature(MMInterModel::Element.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_mmintermodel::element_has_id():
    assert hasattr(MMInterModel::Element, "id")
    descriptor = None
    for klass in MMInterModel::Element.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel::element_has_name():
    assert hasattr(MMInterModel::Element, "name")
    descriptor = None
    for klass in MMInterModel::Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
Element_strategy = st.builds(
    Element,
)
MMInterModel::Guard_strategy = st.builds(
    MMInterModel::Guard,
    specification=
        safe_text,
    transition=
        safe_text
)
MMInterModel::StateConfiguration_strategy = st.builds(
    MMInterModel::StateConfiguration,
    model=
        safe_text,
    configOperator=
        safe_text,
    negation=
        st.booleans(),
    condition=
        safe_text
)
MMInterModel::Component_strategy = st.builds(
    MMInterModel::Component,
    numberOfSpares=
        st.integers(),
    model=
        safe_text
)
MMInterModel::Attribute_strategy = st.builds(
    MMInterModel::Attribute,
    defaultValue=
        safe_text,
    component=
        safe_text,
    model=
        safe_text,
    type=
        safe_text,
    lowerBound=
        st.integers(),
    isArray=
        st.booleans(),
    upperBound=
        st.integers(),
    arraySize=
        st.integers()
)
MMInterModel::StateMachine_strategy = st.builds(
    MMInterModel::StateMachine,
    component=
        safe_text,
    type=
        safe_text,
    superState=
        safe_text
)
MMInterModel::StringEnumeration_strategy = st.builds(
    MMInterModel::StringEnumeration,
    attribute=
        safe_text
)
MMInterModel::Event_strategy = st.builds(
    MMInterModel::Event,
    type=
        safe_text,
    model=
        safe_text
)
MMInterModel::Model_strategy = st.builds(
    MMInterModel::Model,
)
MMInterModel::State_strategy = st.builds(
    MMInterModel::State,
    exitBehaviour=
        safe_text,
    duringBehaviour=
        safe_text,
    entryBehaviour=
        safe_text,
    stateNumber=
        st.integers(),
    stateMachine=
        safe_text,
    stateConfiguration=
        safe_text
)
MMInterModel::Transition_strategy = st.builds(
    MMInterModel::Transition,
    stateMachine=
        safe_text,
    action=
        safe_text
)
MMInterModel::Element_strategy = st.builds(
    MMInterModel::Element,
    id=
        safe_text,
    name=
        safe_text
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=MMInterModel::Guard_strategy)
@settings(max_examples=50)
def test_mmintermodel::guard_instantiation(instance):
    assert isinstance(instance, MMInterModel::Guard)

@given(instance=MMInterModel::Guard_strategy)
def test_mmintermodel::guard_specification_type(instance):
    assert isinstance(instance.specification, str)


@given(instance=MMInterModel::Guard_strategy)
def test_mmintermodel::guard_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=MMInterModel::Guard_strategy)
def test_mmintermodel::guard_transition_type(instance):
    assert isinstance(instance.transition, str)


@given(instance=MMInterModel::Guard_strategy)
def test_mmintermodel::guard_transition_setter(instance):
    original = instance.transition
    instance.transition = original
    assert instance.transition == original

@given(instance=MMInterModel::StateConfiguration_strategy)
@settings(max_examples=50)
def test_mmintermodel::stateconfiguration_instantiation(instance):
    assert isinstance(instance, MMInterModel::StateConfiguration)

@given(instance=MMInterModel::StateConfiguration_strategy)
def test_mmintermodel::stateconfiguration_model_type(instance):
    assert isinstance(instance.model, str)


@given(instance=MMInterModel::StateConfiguration_strategy)
def test_mmintermodel::stateconfiguration_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original

@given(instance=MMInterModel::StateConfiguration_strategy)
def test_mmintermodel::stateconfiguration_configOperator_type(instance):
    assert isinstance(instance.configOperator, str)


@given(instance=MMInterModel::StateConfiguration_strategy)
def test_mmintermodel::stateconfiguration_configOperator_setter(instance):
    original = instance.configOperator
    instance.configOperator = original
    assert instance.configOperator == original

@given(instance=MMInterModel::StateConfiguration_strategy)
def test_mmintermodel::stateconfiguration_negation_type(instance):
    assert isinstance(instance.negation, bool)


@given(instance=MMInterModel::StateConfiguration_strategy)
def test_mmintermodel::stateconfiguration_negation_setter(instance):
    original = instance.negation
    instance.negation = original
    assert instance.negation == original

@given(instance=MMInterModel::StateConfiguration_strategy)
def test_mmintermodel::stateconfiguration_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=MMInterModel::StateConfiguration_strategy)
def test_mmintermodel::stateconfiguration_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=MMInterModel::Component_strategy)
@settings(max_examples=50)
def test_mmintermodel::component_instantiation(instance):
    assert isinstance(instance, MMInterModel::Component)

@given(instance=MMInterModel::Component_strategy)
def test_mmintermodel::component_numberOfSpares_type(instance):
    assert isinstance(instance.numberOfSpares, int)


@given(instance=MMInterModel::Component_strategy)
def test_mmintermodel::component_numberOfSpares_setter(instance):
    original = instance.numberOfSpares
    instance.numberOfSpares = original
    assert instance.numberOfSpares == original

@given(instance=MMInterModel::Component_strategy)
def test_mmintermodel::component_model_type(instance):
    assert isinstance(instance.model, str)


@given(instance=MMInterModel::Component_strategy)
def test_mmintermodel::component_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original

@given(instance=MMInterModel::Attribute_strategy)
@settings(max_examples=50)
def test_mmintermodel::attribute_instantiation(instance):
    assert isinstance(instance, MMInterModel::Attribute)

@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_component_type(instance):
    assert isinstance(instance.component, str)


@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_component_setter(instance):
    original = instance.component
    instance.component = original
    assert instance.component == original

@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_model_type(instance):
    assert isinstance(instance.model, str)


@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original

@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_isArray_type(instance):
    assert isinstance(instance.isArray, bool)


@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original

@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_arraySize_type(instance):
    assert isinstance(instance.arraySize, int)


@given(instance=MMInterModel::Attribute_strategy)
def test_mmintermodel::attribute_arraySize_setter(instance):
    original = instance.arraySize
    instance.arraySize = original
    assert instance.arraySize == original

@given(instance=MMInterModel::StateMachine_strategy)
@settings(max_examples=50)
def test_mmintermodel::statemachine_instantiation(instance):
    assert isinstance(instance, MMInterModel::StateMachine)

@given(instance=MMInterModel::StateMachine_strategy)
def test_mmintermodel::statemachine_component_type(instance):
    assert isinstance(instance.component, str)


@given(instance=MMInterModel::StateMachine_strategy)
def test_mmintermodel::statemachine_component_setter(instance):
    original = instance.component
    instance.component = original
    assert instance.component == original

@given(instance=MMInterModel::StateMachine_strategy)
def test_mmintermodel::statemachine_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MMInterModel::StateMachine_strategy)
def test_mmintermodel::statemachine_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MMInterModel::StateMachine_strategy)
def test_mmintermodel::statemachine_superState_type(instance):
    assert isinstance(instance.superState, str)


@given(instance=MMInterModel::StateMachine_strategy)
def test_mmintermodel::statemachine_superState_setter(instance):
    original = instance.superState
    instance.superState = original
    assert instance.superState == original

@given(instance=MMInterModel::StringEnumeration_strategy)
@settings(max_examples=50)
def test_mmintermodel::stringenumeration_instantiation(instance):
    assert isinstance(instance, MMInterModel::StringEnumeration)

@given(instance=MMInterModel::StringEnumeration_strategy)
def test_mmintermodel::stringenumeration_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=MMInterModel::StringEnumeration_strategy)
def test_mmintermodel::stringenumeration_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=MMInterModel::Event_strategy)
@settings(max_examples=50)
def test_mmintermodel::event_instantiation(instance):
    assert isinstance(instance, MMInterModel::Event)

@given(instance=MMInterModel::Event_strategy)
def test_mmintermodel::event_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MMInterModel::Event_strategy)
def test_mmintermodel::event_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MMInterModel::Event_strategy)
def test_mmintermodel::event_model_type(instance):
    assert isinstance(instance.model, str)


@given(instance=MMInterModel::Event_strategy)
def test_mmintermodel::event_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original

@given(instance=MMInterModel::Model_strategy)
@settings(max_examples=50)
def test_mmintermodel::model_instantiation(instance):
    assert isinstance(instance, MMInterModel::Model)

@given(instance=MMInterModel::State_strategy)
@settings(max_examples=50)
def test_mmintermodel::state_instantiation(instance):
    assert isinstance(instance, MMInterModel::State)

@given(instance=MMInterModel::State_strategy)
def test_mmintermodel::state_exitBehaviour_type(instance):
    assert isinstance(instance.exitBehaviour, str)


@given(instance=MMInterModel::State_strategy)
def test_mmintermodel::state_exitBehaviour_setter(instance):
    original = instance.exitBehaviour
    instance.exitBehaviour = original
    assert instance.exitBehaviour == original

@given(instance=MMInterModel::State_strategy)
def test_mmintermodel::state_duringBehaviour_type(instance):
    assert isinstance(instance.duringBehaviour, str)


@given(instance=MMInterModel::State_strategy)
def test_mmintermodel::state_duringBehaviour_setter(instance):
    original = instance.duringBehaviour
    instance.duringBehaviour = original
    assert instance.duringBehaviour == original

@given(instance=MMInterModel::State_strategy)
def test_mmintermodel::state_entryBehaviour_type(instance):
    assert isinstance(instance.entryBehaviour, str)


@given(instance=MMInterModel::State_strategy)
def test_mmintermodel::state_entryBehaviour_setter(instance):
    original = instance.entryBehaviour
    instance.entryBehaviour = original
    assert instance.entryBehaviour == original

@given(instance=MMInterModel::State_strategy)
def test_mmintermodel::state_stateNumber_type(instance):
    assert isinstance(instance.stateNumber, int)


@given(instance=MMInterModel::State_strategy)
def test_mmintermodel::state_stateNumber_setter(instance):
    original = instance.stateNumber
    instance.stateNumber = original
    assert instance.stateNumber == original

@given(instance=MMInterModel::State_strategy)
def test_mmintermodel::state_stateMachine_type(instance):
    assert isinstance(instance.stateMachine, str)


@given(instance=MMInterModel::State_strategy)
def test_mmintermodel::state_stateMachine_setter(instance):
    original = instance.stateMachine
    instance.stateMachine = original
    assert instance.stateMachine == original

@given(instance=MMInterModel::State_strategy)
def test_mmintermodel::state_stateConfiguration_type(instance):
    assert isinstance(instance.stateConfiguration, str)


@given(instance=MMInterModel::State_strategy)
def test_mmintermodel::state_stateConfiguration_setter(instance):
    original = instance.stateConfiguration
    instance.stateConfiguration = original
    assert instance.stateConfiguration == original

@given(instance=MMInterModel::Transition_strategy)
@settings(max_examples=50)
def test_mmintermodel::transition_instantiation(instance):
    assert isinstance(instance, MMInterModel::Transition)

@given(instance=MMInterModel::Transition_strategy)
def test_mmintermodel::transition_stateMachine_type(instance):
    assert isinstance(instance.stateMachine, str)


@given(instance=MMInterModel::Transition_strategy)
def test_mmintermodel::transition_stateMachine_setter(instance):
    original = instance.stateMachine
    instance.stateMachine = original
    assert instance.stateMachine == original

@given(instance=MMInterModel::Transition_strategy)
def test_mmintermodel::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=MMInterModel::Transition_strategy)
def test_mmintermodel::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=MMInterModel::Element_strategy)
@settings(max_examples=50)
def test_mmintermodel::element_instantiation(instance):
    assert isinstance(instance, MMInterModel::Element)

@given(instance=MMInterModel::Element_strategy)
def test_mmintermodel::element_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=MMInterModel::Element_strategy)
def test_mmintermodel::element_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=MMInterModel::Element_strategy)
def test_mmintermodel::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MMInterModel::Element_strategy)
def test_mmintermodel::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
