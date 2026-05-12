import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Element,
    MMInterModel_Guard,
    MMInterModel_StringEnumeration,
    MMInterModel_Attribute,
    MMInterModel_StateMachine,
    MMInterModel_Component,
    MMInterModel_Event,
    MMInterModel_StateConfiguration,
    MMInterModel_Model,
    MMInterModel_State,
    MMInterModel_Transition,
    MMInterModel_Element,
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



def test_mmintermodel_guard_is_not_abstract():
    assert not inspect.isabstract(MMInterModel_Guard)


def test_mmintermodel_guard_constructor_exists():
    assert callable(MMInterModel_Guard.__init__)


def test_mmintermodel_guard_constructor_args():
    sig = inspect.signature(MMInterModel_Guard.__init__)
    params = list(sig.parameters.keys())
    assert "transition" in params, "Missing parameter 'transition'"
    assert "specification" in params, "Missing parameter 'specification'"

def test_mmintermodel_guard_has_transition():
    assert hasattr(MMInterModel_Guard, "transition")
    descriptor = None
    for klass in MMInterModel_Guard.__mro__:
        if "transition" in klass.__dict__:
            descriptor = klass.__dict__["transition"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_guard_has_specification():
    assert hasattr(MMInterModel_Guard, "specification")
    descriptor = None
    for klass in MMInterModel_Guard.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel_stringenumeration_is_not_abstract():
    assert not inspect.isabstract(MMInterModel_StringEnumeration)


def test_mmintermodel_stringenumeration_constructor_exists():
    assert callable(MMInterModel_StringEnumeration.__init__)


def test_mmintermodel_stringenumeration_constructor_args():
    sig = inspect.signature(MMInterModel_StringEnumeration.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_mmintermodel_stringenumeration_has_attribute():
    assert hasattr(MMInterModel_StringEnumeration, "attribute")
    descriptor = None
    for klass in MMInterModel_StringEnumeration.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel_attribute_is_not_abstract():
    assert not inspect.isabstract(MMInterModel_Attribute)


def test_mmintermodel_attribute_constructor_exists():
    assert callable(MMInterModel_Attribute.__init__)


def test_mmintermodel_attribute_constructor_args():
    sig = inspect.signature(MMInterModel_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "arraySize" in params, "Missing parameter 'arraySize'"
    assert "component" in params, "Missing parameter 'component'"
    assert "type" in params, "Missing parameter 'type'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "isArray" in params, "Missing parameter 'isArray'"
    assert "model" in params, "Missing parameter 'model'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_mmintermodel_attribute_has_defaultValue():
    assert hasattr(MMInterModel_Attribute, "defaultValue")
    descriptor = None
    for klass in MMInterModel_Attribute.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_attribute_has_arraySize():
    assert hasattr(MMInterModel_Attribute, "arraySize")
    descriptor = None
    for klass in MMInterModel_Attribute.__mro__:
        if "arraySize" in klass.__dict__:
            descriptor = klass.__dict__["arraySize"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_attribute_has_component():
    assert hasattr(MMInterModel_Attribute, "component")
    descriptor = None
    for klass in MMInterModel_Attribute.__mro__:
        if "component" in klass.__dict__:
            descriptor = klass.__dict__["component"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_attribute_has_type():
    assert hasattr(MMInterModel_Attribute, "type")
    descriptor = None
    for klass in MMInterModel_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_attribute_has_upperBound():
    assert hasattr(MMInterModel_Attribute, "upperBound")
    descriptor = None
    for klass in MMInterModel_Attribute.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_attribute_has_isArray():
    assert hasattr(MMInterModel_Attribute, "isArray")
    descriptor = None
    for klass in MMInterModel_Attribute.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_attribute_has_model():
    assert hasattr(MMInterModel_Attribute, "model")
    descriptor = None
    for klass in MMInterModel_Attribute.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_attribute_has_lowerBound():
    assert hasattr(MMInterModel_Attribute, "lowerBound")
    descriptor = None
    for klass in MMInterModel_Attribute.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel_statemachine_is_not_abstract():
    assert not inspect.isabstract(MMInterModel_StateMachine)


def test_mmintermodel_statemachine_constructor_exists():
    assert callable(MMInterModel_StateMachine.__init__)


def test_mmintermodel_statemachine_constructor_args():
    sig = inspect.signature(MMInterModel_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "superState" in params, "Missing parameter 'superState'"
    assert "component" in params, "Missing parameter 'component'"
    assert "type" in params, "Missing parameter 'type'"

def test_mmintermodel_statemachine_has_superState():
    assert hasattr(MMInterModel_StateMachine, "superState")
    descriptor = None
    for klass in MMInterModel_StateMachine.__mro__:
        if "superState" in klass.__dict__:
            descriptor = klass.__dict__["superState"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_statemachine_has_component():
    assert hasattr(MMInterModel_StateMachine, "component")
    descriptor = None
    for klass in MMInterModel_StateMachine.__mro__:
        if "component" in klass.__dict__:
            descriptor = klass.__dict__["component"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_statemachine_has_type():
    assert hasattr(MMInterModel_StateMachine, "type")
    descriptor = None
    for klass in MMInterModel_StateMachine.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel_component_is_not_abstract():
    assert not inspect.isabstract(MMInterModel_Component)


def test_mmintermodel_component_constructor_exists():
    assert callable(MMInterModel_Component.__init__)


def test_mmintermodel_component_constructor_args():
    sig = inspect.signature(MMInterModel_Component.__init__)
    params = list(sig.parameters.keys())
    assert "model" in params, "Missing parameter 'model'"
    assert "numberOfSpares" in params, "Missing parameter 'numberOfSpares'"

def test_mmintermodel_component_has_model():
    assert hasattr(MMInterModel_Component, "model")
    descriptor = None
    for klass in MMInterModel_Component.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_component_has_numberOfSpares():
    assert hasattr(MMInterModel_Component, "numberOfSpares")
    descriptor = None
    for klass in MMInterModel_Component.__mro__:
        if "numberOfSpares" in klass.__dict__:
            descriptor = klass.__dict__["numberOfSpares"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel_event_is_not_abstract():
    assert not inspect.isabstract(MMInterModel_Event)


def test_mmintermodel_event_constructor_exists():
    assert callable(MMInterModel_Event.__init__)


def test_mmintermodel_event_constructor_args():
    sig = inspect.signature(MMInterModel_Event.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "model" in params, "Missing parameter 'model'"

def test_mmintermodel_event_has_type():
    assert hasattr(MMInterModel_Event, "type")
    descriptor = None
    for klass in MMInterModel_Event.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_event_has_model():
    assert hasattr(MMInterModel_Event, "model")
    descriptor = None
    for klass in MMInterModel_Event.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel_stateconfiguration_is_not_abstract():
    assert not inspect.isabstract(MMInterModel_StateConfiguration)


def test_mmintermodel_stateconfiguration_constructor_exists():
    assert callable(MMInterModel_StateConfiguration.__init__)


def test_mmintermodel_stateconfiguration_constructor_args():
    sig = inspect.signature(MMInterModel_StateConfiguration.__init__)
    params = list(sig.parameters.keys())
    assert "configOperator" in params, "Missing parameter 'configOperator'"
    assert "negation" in params, "Missing parameter 'negation'"
    assert "model" in params, "Missing parameter 'model'"
    assert "condition" in params, "Missing parameter 'condition'"

def test_mmintermodel_stateconfiguration_has_configOperator():
    assert hasattr(MMInterModel_StateConfiguration, "configOperator")
    descriptor = None
    for klass in MMInterModel_StateConfiguration.__mro__:
        if "configOperator" in klass.__dict__:
            descriptor = klass.__dict__["configOperator"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_stateconfiguration_has_negation():
    assert hasattr(MMInterModel_StateConfiguration, "negation")
    descriptor = None
    for klass in MMInterModel_StateConfiguration.__mro__:
        if "negation" in klass.__dict__:
            descriptor = klass.__dict__["negation"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_stateconfiguration_has_model():
    assert hasattr(MMInterModel_StateConfiguration, "model")
    descriptor = None
    for klass in MMInterModel_StateConfiguration.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_stateconfiguration_has_condition():
    assert hasattr(MMInterModel_StateConfiguration, "condition")
    descriptor = None
    for klass in MMInterModel_StateConfiguration.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel_model_is_not_abstract():
    assert not inspect.isabstract(MMInterModel_Model)


def test_mmintermodel_model_constructor_exists():
    assert callable(MMInterModel_Model.__init__)


def test_mmintermodel_model_constructor_args():
    sig = inspect.signature(MMInterModel_Model.__init__)
    params = list(sig.parameters.keys())



def test_mmintermodel_state_is_not_abstract():
    assert not inspect.isabstract(MMInterModel_State)


def test_mmintermodel_state_constructor_exists():
    assert callable(MMInterModel_State.__init__)


def test_mmintermodel_state_constructor_args():
    sig = inspect.signature(MMInterModel_State.__init__)
    params = list(sig.parameters.keys())
    assert "entryBehaviour" in params, "Missing parameter 'entryBehaviour'"
    assert "stateMachine" in params, "Missing parameter 'stateMachine'"
    assert "duringBehaviour" in params, "Missing parameter 'duringBehaviour'"
    assert "stateNumber" in params, "Missing parameter 'stateNumber'"
    assert "exitBehaviour" in params, "Missing parameter 'exitBehaviour'"
    assert "stateConfiguration" in params, "Missing parameter 'stateConfiguration'"

def test_mmintermodel_state_has_entryBehaviour():
    assert hasattr(MMInterModel_State, "entryBehaviour")
    descriptor = None
    for klass in MMInterModel_State.__mro__:
        if "entryBehaviour" in klass.__dict__:
            descriptor = klass.__dict__["entryBehaviour"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_state_has_stateMachine():
    assert hasattr(MMInterModel_State, "stateMachine")
    descriptor = None
    for klass in MMInterModel_State.__mro__:
        if "stateMachine" in klass.__dict__:
            descriptor = klass.__dict__["stateMachine"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_state_has_duringBehaviour():
    assert hasattr(MMInterModel_State, "duringBehaviour")
    descriptor = None
    for klass in MMInterModel_State.__mro__:
        if "duringBehaviour" in klass.__dict__:
            descriptor = klass.__dict__["duringBehaviour"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_state_has_stateNumber():
    assert hasattr(MMInterModel_State, "stateNumber")
    descriptor = None
    for klass in MMInterModel_State.__mro__:
        if "stateNumber" in klass.__dict__:
            descriptor = klass.__dict__["stateNumber"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_state_has_exitBehaviour():
    assert hasattr(MMInterModel_State, "exitBehaviour")
    descriptor = None
    for klass in MMInterModel_State.__mro__:
        if "exitBehaviour" in klass.__dict__:
            descriptor = klass.__dict__["exitBehaviour"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_state_has_stateConfiguration():
    assert hasattr(MMInterModel_State, "stateConfiguration")
    descriptor = None
    for klass in MMInterModel_State.__mro__:
        if "stateConfiguration" in klass.__dict__:
            descriptor = klass.__dict__["stateConfiguration"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel_transition_is_not_abstract():
    assert not inspect.isabstract(MMInterModel_Transition)


def test_mmintermodel_transition_constructor_exists():
    assert callable(MMInterModel_Transition.__init__)


def test_mmintermodel_transition_constructor_args():
    sig = inspect.signature(MMInterModel_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "stateMachine" in params, "Missing parameter 'stateMachine'"

def test_mmintermodel_transition_has_action():
    assert hasattr(MMInterModel_Transition, "action")
    descriptor = None
    for klass in MMInterModel_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_transition_has_stateMachine():
    assert hasattr(MMInterModel_Transition, "stateMachine")
    descriptor = None
    for klass in MMInterModel_Transition.__mro__:
        if "stateMachine" in klass.__dict__:
            descriptor = klass.__dict__["stateMachine"]
            break
    assert isinstance(descriptor, property)



def test_mmintermodel_element_is_not_abstract():
    assert not inspect.isabstract(MMInterModel_Element)


def test_mmintermodel_element_constructor_exists():
    assert callable(MMInterModel_Element.__init__)


def test_mmintermodel_element_constructor_args():
    sig = inspect.signature(MMInterModel_Element.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_mmintermodel_element_has_id():
    assert hasattr(MMInterModel_Element, "id")
    descriptor = None
    for klass in MMInterModel_Element.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mmintermodel_element_has_name():
    assert hasattr(MMInterModel_Element, "name")
    descriptor = None
    for klass in MMInterModel_Element.__mro__:
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
MMInterModel_Guard_strategy = st.builds(
    MMInterModel_Guard,
    transition=
        safe_text,
    specification=
        safe_text
)
MMInterModel_StringEnumeration_strategy = st.builds(
    MMInterModel_StringEnumeration,
    attribute=
        safe_text
)
MMInterModel_Attribute_strategy = st.builds(
    MMInterModel_Attribute,
    defaultValue=
        safe_text,
    arraySize=
        st.integers(),
    component=
        safe_text,
    type=
        safe_text,
    upperBound=
        st.integers(),
    isArray=
        st.booleans(),
    model=
        safe_text,
    lowerBound=
        st.integers()
)
MMInterModel_StateMachine_strategy = st.builds(
    MMInterModel_StateMachine,
    superState=
        safe_text,
    component=
        safe_text,
    type=
        safe_text
)
MMInterModel_Component_strategy = st.builds(
    MMInterModel_Component,
    model=
        safe_text,
    numberOfSpares=
        st.integers()
)
MMInterModel_Event_strategy = st.builds(
    MMInterModel_Event,
    type=
        safe_text,
    model=
        safe_text
)
MMInterModel_StateConfiguration_strategy = st.builds(
    MMInterModel_StateConfiguration,
    configOperator=
        safe_text,
    negation=
        st.booleans(),
    model=
        safe_text,
    condition=
        safe_text
)
MMInterModel_Model_strategy = st.builds(
    MMInterModel_Model,
)
MMInterModel_State_strategy = st.builds(
    MMInterModel_State,
    entryBehaviour=
        safe_text,
    stateMachine=
        safe_text,
    duringBehaviour=
        safe_text,
    stateNumber=
        st.integers(),
    exitBehaviour=
        safe_text,
    stateConfiguration=
        safe_text
)
MMInterModel_Transition_strategy = st.builds(
    MMInterModel_Transition,
    action=
        safe_text,
    stateMachine=
        safe_text
)
MMInterModel_Element_strategy = st.builds(
    MMInterModel_Element,
    id=
        safe_text,
    name=
        safe_text
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=MMInterModel_Guard_strategy)
@settings(max_examples=50)
def test_mmintermodel_guard_instantiation(instance):
    assert isinstance(instance, MMInterModel_Guard)



@given(instance=MMInterModel_Guard_strategy)
def test_mmintermodel_guard_transition_setter(instance):
    original = instance.transition
    instance.transition = original
    assert instance.transition == original



@given(instance=MMInterModel_Guard_strategy)
def test_mmintermodel_guard_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=MMInterModel_StringEnumeration_strategy)
@settings(max_examples=50)
def test_mmintermodel_stringenumeration_instantiation(instance):
    assert isinstance(instance, MMInterModel_StringEnumeration)



@given(instance=MMInterModel_StringEnumeration_strategy)
def test_mmintermodel_stringenumeration_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=MMInterModel_Attribute_strategy)
@settings(max_examples=50)
def test_mmintermodel_attribute_instantiation(instance):
    assert isinstance(instance, MMInterModel_Attribute)



@given(instance=MMInterModel_Attribute_strategy)
def test_mmintermodel_attribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=MMInterModel_Attribute_strategy)
def test_mmintermodel_attribute_arraySize_setter(instance):
    original = instance.arraySize
    instance.arraySize = original
    assert instance.arraySize == original



@given(instance=MMInterModel_Attribute_strategy)
def test_mmintermodel_attribute_component_setter(instance):
    original = instance.component
    instance.component = original
    assert instance.component == original



@given(instance=MMInterModel_Attribute_strategy)
def test_mmintermodel_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MMInterModel_Attribute_strategy)
def test_mmintermodel_attribute_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=MMInterModel_Attribute_strategy)
def test_mmintermodel_attribute_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original



@given(instance=MMInterModel_Attribute_strategy)
def test_mmintermodel_attribute_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=MMInterModel_Attribute_strategy)
def test_mmintermodel_attribute_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=MMInterModel_StateMachine_strategy)
@settings(max_examples=50)
def test_mmintermodel_statemachine_instantiation(instance):
    assert isinstance(instance, MMInterModel_StateMachine)



@given(instance=MMInterModel_StateMachine_strategy)
def test_mmintermodel_statemachine_superState_setter(instance):
    original = instance.superState
    instance.superState = original
    assert instance.superState == original



@given(instance=MMInterModel_StateMachine_strategy)
def test_mmintermodel_statemachine_component_setter(instance):
    original = instance.component
    instance.component = original
    assert instance.component == original



@given(instance=MMInterModel_StateMachine_strategy)
def test_mmintermodel_statemachine_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MMInterModel_Component_strategy)
@settings(max_examples=50)
def test_mmintermodel_component_instantiation(instance):
    assert isinstance(instance, MMInterModel_Component)



@given(instance=MMInterModel_Component_strategy)
def test_mmintermodel_component_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=MMInterModel_Component_strategy)
def test_mmintermodel_component_numberOfSpares_setter(instance):
    original = instance.numberOfSpares
    instance.numberOfSpares = original
    assert instance.numberOfSpares == original

@given(instance=MMInterModel_Event_strategy)
@settings(max_examples=50)
def test_mmintermodel_event_instantiation(instance):
    assert isinstance(instance, MMInterModel_Event)



@given(instance=MMInterModel_Event_strategy)
def test_mmintermodel_event_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MMInterModel_Event_strategy)
def test_mmintermodel_event_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original

@given(instance=MMInterModel_StateConfiguration_strategy)
@settings(max_examples=50)
def test_mmintermodel_stateconfiguration_instantiation(instance):
    assert isinstance(instance, MMInterModel_StateConfiguration)



@given(instance=MMInterModel_StateConfiguration_strategy)
def test_mmintermodel_stateconfiguration_configOperator_setter(instance):
    original = instance.configOperator
    instance.configOperator = original
    assert instance.configOperator == original



@given(instance=MMInterModel_StateConfiguration_strategy)
def test_mmintermodel_stateconfiguration_negation_setter(instance):
    original = instance.negation
    instance.negation = original
    assert instance.negation == original



@given(instance=MMInterModel_StateConfiguration_strategy)
def test_mmintermodel_stateconfiguration_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=MMInterModel_StateConfiguration_strategy)
def test_mmintermodel_stateconfiguration_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=MMInterModel_Model_strategy)
@settings(max_examples=50)
def test_mmintermodel_model_instantiation(instance):
    assert isinstance(instance, MMInterModel_Model)

@given(instance=MMInterModel_State_strategy)
@settings(max_examples=50)
def test_mmintermodel_state_instantiation(instance):
    assert isinstance(instance, MMInterModel_State)



@given(instance=MMInterModel_State_strategy)
def test_mmintermodel_state_entryBehaviour_setter(instance):
    original = instance.entryBehaviour
    instance.entryBehaviour = original
    assert instance.entryBehaviour == original



@given(instance=MMInterModel_State_strategy)
def test_mmintermodel_state_stateMachine_setter(instance):
    original = instance.stateMachine
    instance.stateMachine = original
    assert instance.stateMachine == original



@given(instance=MMInterModel_State_strategy)
def test_mmintermodel_state_duringBehaviour_setter(instance):
    original = instance.duringBehaviour
    instance.duringBehaviour = original
    assert instance.duringBehaviour == original



@given(instance=MMInterModel_State_strategy)
def test_mmintermodel_state_stateNumber_setter(instance):
    original = instance.stateNumber
    instance.stateNumber = original
    assert instance.stateNumber == original



@given(instance=MMInterModel_State_strategy)
def test_mmintermodel_state_exitBehaviour_setter(instance):
    original = instance.exitBehaviour
    instance.exitBehaviour = original
    assert instance.exitBehaviour == original



@given(instance=MMInterModel_State_strategy)
def test_mmintermodel_state_stateConfiguration_setter(instance):
    original = instance.stateConfiguration
    instance.stateConfiguration = original
    assert instance.stateConfiguration == original

@given(instance=MMInterModel_Transition_strategy)
@settings(max_examples=50)
def test_mmintermodel_transition_instantiation(instance):
    assert isinstance(instance, MMInterModel_Transition)



@given(instance=MMInterModel_Transition_strategy)
def test_mmintermodel_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=MMInterModel_Transition_strategy)
def test_mmintermodel_transition_stateMachine_setter(instance):
    original = instance.stateMachine
    instance.stateMachine = original
    assert instance.stateMachine == original

@given(instance=MMInterModel_Element_strategy)
@settings(max_examples=50)
def test_mmintermodel_element_instantiation(instance):
    assert isinstance(instance, MMInterModel_Element)



@given(instance=MMInterModel_Element_strategy)
def test_mmintermodel_element_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=MMInterModel_Element_strategy)
def test_mmintermodel_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
