import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    iotsystem_NamedElement,
    iotsystem_Parameter,
    iotsystem_Resource,
    NamedElement,
    iotsystem_Rule,
    iotsystem_PhysicalEntity,
    iotsystem_IotSystem,
    iotsystem_DigitalArtifact,
    iotsystem_Device,
    Device,
    iotsystem_Actuator,
    iotsystem_Sensor,
    iotsystem_Condition,
    iotsystem_Action,
    EnvironmentConditions,
    RelationalOperator,
    Actions,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iotsystem_namedelement_is_not_abstract():
    assert not inspect.isabstract(iotsystem_NamedElement)


def test_iotsystem_namedelement_constructor_exists():
    assert callable(iotsystem_NamedElement.__init__)


def test_iotsystem_namedelement_constructor_args():
    sig = inspect.signature(iotsystem_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotsystem_namedelement_has_name():
    assert hasattr(iotsystem_NamedElement, "name")
    descriptor = None
    for klass in iotsystem_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotsystem_parameter_is_not_abstract():
    assert not inspect.isabstract(iotsystem_Parameter)


def test_iotsystem_parameter_constructor_exists():
    assert callable(iotsystem_Parameter.__init__)


def test_iotsystem_parameter_constructor_args():
    sig = inspect.signature(iotsystem_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_iotsystem_parameter_has_value():
    assert hasattr(iotsystem_Parameter, "value")
    descriptor = None
    for klass in iotsystem_Parameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_iotsystem_parameter_has_name():
    assert hasattr(iotsystem_Parameter, "name")
    descriptor = None
    for klass in iotsystem_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotsystem_resource_is_not_abstract():
    assert not inspect.isabstract(iotsystem_Resource)


def test_iotsystem_resource_constructor_exists():
    assert callable(iotsystem_Resource.__init__)


def test_iotsystem_resource_constructor_args():
    sig = inspect.signature(iotsystem_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "measurement" in params, "Missing parameter 'measurement'"

def test_iotsystem_resource_has_url():
    assert hasattr(iotsystem_Resource, "url")
    descriptor = None
    for klass in iotsystem_Resource.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_iotsystem_resource_has_measurement():
    assert hasattr(iotsystem_Resource, "measurement")
    descriptor = None
    for klass in iotsystem_Resource.__mro__:
        if "measurement" in klass.__dict__:
            descriptor = klass.__dict__["measurement"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem_rule_is_not_abstract():
    assert not inspect.isabstract(iotsystem_Rule)


def test_iotsystem_rule_constructor_exists():
    assert callable(iotsystem_Rule.__init__)


def test_iotsystem_rule_constructor_args():
    sig = inspect.signature(iotsystem_Rule.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem_physicalentity_is_not_abstract():
    assert not inspect.isabstract(iotsystem_PhysicalEntity)


def test_iotsystem_physicalentity_constructor_exists():
    assert callable(iotsystem_PhysicalEntity.__init__)


def test_iotsystem_physicalentity_constructor_args():
    sig = inspect.signature(iotsystem_PhysicalEntity.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem_iotsystem_is_not_abstract():
    assert not inspect.isabstract(iotsystem_IotSystem)


def test_iotsystem_iotsystem_constructor_exists():
    assert callable(iotsystem_IotSystem.__init__)


def test_iotsystem_iotsystem_constructor_args():
    sig = inspect.signature(iotsystem_IotSystem.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem_digitalartifact_is_not_abstract():
    assert not inspect.isabstract(iotsystem_DigitalArtifact)


def test_iotsystem_digitalartifact_constructor_exists():
    assert callable(iotsystem_DigitalArtifact.__init__)


def test_iotsystem_digitalartifact_constructor_args():
    sig = inspect.signature(iotsystem_DigitalArtifact.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem_device_is_not_abstract():
    assert not inspect.isabstract(iotsystem_Device)


def test_iotsystem_device_constructor_exists():
    assert callable(iotsystem_Device.__init__)


def test_iotsystem_device_constructor_args():
    sig = inspect.signature(iotsystem_Device.__init__)
    params = list(sig.parameters.keys())



def test_device_is_not_abstract():
    assert not inspect.isabstract(Device)


def test_device_constructor_exists():
    assert callable(Device.__init__)


def test_device_constructor_args():
    sig = inspect.signature(Device.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem_actuator_is_not_abstract():
    assert not inspect.isabstract(iotsystem_Actuator)


def test_iotsystem_actuator_constructor_exists():
    assert callable(iotsystem_Actuator.__init__)


def test_iotsystem_actuator_constructor_args():
    sig = inspect.signature(iotsystem_Actuator.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem_sensor_is_not_abstract():
    assert not inspect.isabstract(iotsystem_Sensor)


def test_iotsystem_sensor_constructor_exists():
    assert callable(iotsystem_Sensor.__init__)


def test_iotsystem_sensor_constructor_args():
    sig = inspect.signature(iotsystem_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem_condition_is_not_abstract():
    assert not inspect.isabstract(iotsystem_Condition)


def test_iotsystem_condition_constructor_exists():
    assert callable(iotsystem_Condition.__init__)


def test_iotsystem_condition_constructor_args():
    sig = inspect.signature(iotsystem_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "expectedValue" in params, "Missing parameter 'expectedValue'"
    assert "relationalOperator" in params, "Missing parameter 'relationalOperator'"

def test_iotsystem_condition_has_expectedValue():
    assert hasattr(iotsystem_Condition, "expectedValue")
    descriptor = None
    for klass in iotsystem_Condition.__mro__:
        if "expectedValue" in klass.__dict__:
            descriptor = klass.__dict__["expectedValue"]
            break
    assert isinstance(descriptor, property)

def test_iotsystem_condition_has_relationalOperator():
    assert hasattr(iotsystem_Condition, "relationalOperator")
    descriptor = None
    for klass in iotsystem_Condition.__mro__:
        if "relationalOperator" in klass.__dict__:
            descriptor = klass.__dict__["relationalOperator"]
            break
    assert isinstance(descriptor, property)



def test_iotsystem_action_is_not_abstract():
    assert not inspect.isabstract(iotsystem_Action)


def test_iotsystem_action_constructor_exists():
    assert callable(iotsystem_Action.__init__)


def test_iotsystem_action_constructor_args():
    sig = inspect.signature(iotsystem_Action.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"

def test_iotsystem_action_has_action():
    assert hasattr(iotsystem_Action, "action")
    descriptor = None
    for klass in iotsystem_Action.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_environmentconditions_exists():
    # Check that the Enumeration exists
    assert EnvironmentConditions is not None

def test_environmentconditions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnvironmentConditions]
    expected_literals = [
        "LIGHT",
        "SOUND",
        "TEMPERATURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnvironmentConditions"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "EQUAL",
        "DIFFERENT",
        "MAJOR",
        "MAJOREQUAL",
        "MINOR",
        "MINOREQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_actions_exists():
    # Check that the Enumeration exists
    assert Actions is not None

def test_actions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Actions]
    expected_literals = [
        "SMS",
        "EMAIL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Actions"


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
iotsystem_NamedElement_strategy = st.builds(
    iotsystem_NamedElement,
    name=
        safe_text
)
iotsystem_Parameter_strategy = st.builds(
    iotsystem_Parameter,
    value=
        safe_text,
    name=
        safe_text
)
iotsystem_Resource_strategy = st.builds(
    iotsystem_Resource,
    url=
        safe_text,
    measurement=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
iotsystem_Rule_strategy = st.builds(
    iotsystem_Rule,
)
iotsystem_PhysicalEntity_strategy = st.builds(
    iotsystem_PhysicalEntity,
)
iotsystem_IotSystem_strategy = st.builds(
    iotsystem_IotSystem,
)
iotsystem_DigitalArtifact_strategy = st.builds(
    iotsystem_DigitalArtifact,
)
iotsystem_Device_strategy = st.builds(
    iotsystem_Device,
)
Device_strategy = st.builds(
    Device,
)
iotsystem_Actuator_strategy = st.builds(
    iotsystem_Actuator,
)
iotsystem_Sensor_strategy = st.builds(
    iotsystem_Sensor,
)
iotsystem_Condition_strategy = st.builds(
    iotsystem_Condition,
    expectedValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    relationalOperator=
        safe_text
)
iotsystem_Action_strategy = st.builds(
    iotsystem_Action,
    action=
        safe_text
)

@given(instance=iotsystem_NamedElement_strategy)
@settings(max_examples=50)
def test_iotsystem_namedelement_instantiation(instance):
    assert isinstance(instance, iotsystem_NamedElement)



@given(instance=iotsystem_NamedElement_strategy)
def test_iotsystem_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotsystem_Parameter_strategy)
@settings(max_examples=50)
def test_iotsystem_parameter_instantiation(instance):
    assert isinstance(instance, iotsystem_Parameter)



@given(instance=iotsystem_Parameter_strategy)
def test_iotsystem_parameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=iotsystem_Parameter_strategy)
def test_iotsystem_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotsystem_Resource_strategy)
@settings(max_examples=50)
def test_iotsystem_resource_instantiation(instance):
    assert isinstance(instance, iotsystem_Resource)



@given(instance=iotsystem_Resource_strategy)
def test_iotsystem_resource_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=iotsystem_Resource_strategy)
def test_iotsystem_resource_measurement_setter(instance):
    original = instance.measurement
    instance.measurement = original
    assert instance.measurement == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=iotsystem_Rule_strategy)
@settings(max_examples=50)
def test_iotsystem_rule_instantiation(instance):
    assert isinstance(instance, iotsystem_Rule)

@given(instance=iotsystem_PhysicalEntity_strategy)
@settings(max_examples=50)
def test_iotsystem_physicalentity_instantiation(instance):
    assert isinstance(instance, iotsystem_PhysicalEntity)

@given(instance=iotsystem_IotSystem_strategy)
@settings(max_examples=50)
def test_iotsystem_iotsystem_instantiation(instance):
    assert isinstance(instance, iotsystem_IotSystem)

@given(instance=iotsystem_DigitalArtifact_strategy)
@settings(max_examples=50)
def test_iotsystem_digitalartifact_instantiation(instance):
    assert isinstance(instance, iotsystem_DigitalArtifact)

@given(instance=iotsystem_Device_strategy)
@settings(max_examples=50)
def test_iotsystem_device_instantiation(instance):
    assert isinstance(instance, iotsystem_Device)

@given(instance=Device_strategy)
@settings(max_examples=50)
def test_device_instantiation(instance):
    assert isinstance(instance, Device)

@given(instance=iotsystem_Actuator_strategy)
@settings(max_examples=50)
def test_iotsystem_actuator_instantiation(instance):
    assert isinstance(instance, iotsystem_Actuator)

@given(instance=iotsystem_Sensor_strategy)
@settings(max_examples=50)
def test_iotsystem_sensor_instantiation(instance):
    assert isinstance(instance, iotsystem_Sensor)

@given(instance=iotsystem_Condition_strategy)
@settings(max_examples=50)
def test_iotsystem_condition_instantiation(instance):
    assert isinstance(instance, iotsystem_Condition)



@given(instance=iotsystem_Condition_strategy)
def test_iotsystem_condition_expectedValue_setter(instance):
    original = instance.expectedValue
    instance.expectedValue = original
    assert instance.expectedValue == original



@given(instance=iotsystem_Condition_strategy)
def test_iotsystem_condition_relationalOperator_setter(instance):
    original = instance.relationalOperator
    instance.relationalOperator = original
    assert instance.relationalOperator == original

@given(instance=iotsystem_Action_strategy)
@settings(max_examples=50)
def test_iotsystem_action_instantiation(instance):
    assert isinstance(instance, iotsystem_Action)



@given(instance=iotsystem_Action_strategy)
def test_iotsystem_action_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original
