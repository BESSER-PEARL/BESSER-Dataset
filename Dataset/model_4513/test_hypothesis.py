import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    iotsystem::NamedElement,
    iotsystem::Parameter,
    iotsystem::Resource,
    NamedElement,
    iotsystem::Rule,
    iotsystem::PhysicalEntity,
    iotsystem::IotSystem,
    iotsystem::DigitalArtifact,
    iotsystem::Device,
    Device,
    iotsystem::Actuator,
    iotsystem::Sensor,
    iotsystem::Condition,
    iotsystem::Action,
    RelationalOperator,
    Actions,
    EnvironmentConditions,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iotsystem::namedelement_is_not_abstract():
    assert not inspect.isabstract(iotsystem::NamedElement)


def test_iotsystem::namedelement_constructor_exists():
    assert callable(iotsystem::NamedElement.__init__)


def test_iotsystem::namedelement_constructor_args():
    sig = inspect.signature(iotsystem::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotsystem::namedelement_has_name():
    assert hasattr(iotsystem::NamedElement, "name")
    descriptor = None
    for klass in iotsystem::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotsystem::parameter_is_not_abstract():
    assert not inspect.isabstract(iotsystem::Parameter)


def test_iotsystem::parameter_constructor_exists():
    assert callable(iotsystem::Parameter.__init__)


def test_iotsystem::parameter_constructor_args():
    sig = inspect.signature(iotsystem::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_iotsystem::parameter_has_value():
    assert hasattr(iotsystem::Parameter, "value")
    descriptor = None
    for klass in iotsystem::Parameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_iotsystem::parameter_has_name():
    assert hasattr(iotsystem::Parameter, "name")
    descriptor = None
    for klass in iotsystem::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotsystem::resource_is_not_abstract():
    assert not inspect.isabstract(iotsystem::Resource)


def test_iotsystem::resource_constructor_exists():
    assert callable(iotsystem::Resource.__init__)


def test_iotsystem::resource_constructor_args():
    sig = inspect.signature(iotsystem::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "measurement" in params, "Missing parameter 'measurement'"
    assert "url" in params, "Missing parameter 'url'"

def test_iotsystem::resource_has_measurement():
    assert hasattr(iotsystem::Resource, "measurement")
    descriptor = None
    for klass in iotsystem::Resource.__mro__:
        if "measurement" in klass.__dict__:
            descriptor = klass.__dict__["measurement"]
            break
    assert isinstance(descriptor, property)

def test_iotsystem::resource_has_url():
    assert hasattr(iotsystem::Resource, "url")
    descriptor = None
    for klass in iotsystem::Resource.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem::rule_is_not_abstract():
    assert not inspect.isabstract(iotsystem::Rule)


def test_iotsystem::rule_constructor_exists():
    assert callable(iotsystem::Rule.__init__)


def test_iotsystem::rule_constructor_args():
    sig = inspect.signature(iotsystem::Rule.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem::physicalentity_is_not_abstract():
    assert not inspect.isabstract(iotsystem::PhysicalEntity)


def test_iotsystem::physicalentity_constructor_exists():
    assert callable(iotsystem::PhysicalEntity.__init__)


def test_iotsystem::physicalentity_constructor_args():
    sig = inspect.signature(iotsystem::PhysicalEntity.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem::iotsystem_is_not_abstract():
    assert not inspect.isabstract(iotsystem::IotSystem)


def test_iotsystem::iotsystem_constructor_exists():
    assert callable(iotsystem::IotSystem.__init__)


def test_iotsystem::iotsystem_constructor_args():
    sig = inspect.signature(iotsystem::IotSystem.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem::digitalartifact_is_not_abstract():
    assert not inspect.isabstract(iotsystem::DigitalArtifact)


def test_iotsystem::digitalartifact_constructor_exists():
    assert callable(iotsystem::DigitalArtifact.__init__)


def test_iotsystem::digitalartifact_constructor_args():
    sig = inspect.signature(iotsystem::DigitalArtifact.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem::device_is_not_abstract():
    assert not inspect.isabstract(iotsystem::Device)


def test_iotsystem::device_constructor_exists():
    assert callable(iotsystem::Device.__init__)


def test_iotsystem::device_constructor_args():
    sig = inspect.signature(iotsystem::Device.__init__)
    params = list(sig.parameters.keys())



def test_device_is_not_abstract():
    assert not inspect.isabstract(Device)


def test_device_constructor_exists():
    assert callable(Device.__init__)


def test_device_constructor_args():
    sig = inspect.signature(Device.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem::actuator_is_not_abstract():
    assert not inspect.isabstract(iotsystem::Actuator)


def test_iotsystem::actuator_constructor_exists():
    assert callable(iotsystem::Actuator.__init__)


def test_iotsystem::actuator_constructor_args():
    sig = inspect.signature(iotsystem::Actuator.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem::sensor_is_not_abstract():
    assert not inspect.isabstract(iotsystem::Sensor)


def test_iotsystem::sensor_constructor_exists():
    assert callable(iotsystem::Sensor.__init__)


def test_iotsystem::sensor_constructor_args():
    sig = inspect.signature(iotsystem::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_iotsystem::condition_is_not_abstract():
    assert not inspect.isabstract(iotsystem::Condition)


def test_iotsystem::condition_constructor_exists():
    assert callable(iotsystem::Condition.__init__)


def test_iotsystem::condition_constructor_args():
    sig = inspect.signature(iotsystem::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "expectedValue" in params, "Missing parameter 'expectedValue'"
    assert "relationalOperator" in params, "Missing parameter 'relationalOperator'"

def test_iotsystem::condition_has_expectedValue():
    assert hasattr(iotsystem::Condition, "expectedValue")
    descriptor = None
    for klass in iotsystem::Condition.__mro__:
        if "expectedValue" in klass.__dict__:
            descriptor = klass.__dict__["expectedValue"]
            break
    assert isinstance(descriptor, property)

def test_iotsystem::condition_has_relationalOperator():
    assert hasattr(iotsystem::Condition, "relationalOperator")
    descriptor = None
    for klass in iotsystem::Condition.__mro__:
        if "relationalOperator" in klass.__dict__:
            descriptor = klass.__dict__["relationalOperator"]
            break
    assert isinstance(descriptor, property)



def test_iotsystem::action_is_not_abstract():
    assert not inspect.isabstract(iotsystem::Action)


def test_iotsystem::action_constructor_exists():
    assert callable(iotsystem::Action.__init__)


def test_iotsystem::action_constructor_args():
    sig = inspect.signature(iotsystem::Action.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"

def test_iotsystem::action_has_action():
    assert hasattr(iotsystem::Action, "action")
    descriptor = None
    for klass in iotsystem::Action.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "MINOREQUAL",
        "MAJOREQUAL",
        "DIFFERENT",
        "MINOR",
        "EQUAL",
        "MAJOR",
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

def test_environmentconditions_exists():
    # Check that the Enumeration exists
    assert EnvironmentConditions is not None

def test_environmentconditions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnvironmentConditions]
    expected_literals = [
        "SOUND",
        "LIGHT",
        "TEMPERATURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnvironmentConditions"


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
iotsystem::NamedElement_strategy = st.builds(
    iotsystem::NamedElement,
    name=
        safe_text
)
iotsystem::Parameter_strategy = st.builds(
    iotsystem::Parameter,
    value=
        safe_text,
    name=
        safe_text
)
iotsystem::Resource_strategy = st.builds(
    iotsystem::Resource,
    measurement=
        safe_text,
    url=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
iotsystem::Rule_strategy = st.builds(
    iotsystem::Rule,
)
iotsystem::PhysicalEntity_strategy = st.builds(
    iotsystem::PhysicalEntity,
)
iotsystem::IotSystem_strategy = st.builds(
    iotsystem::IotSystem,
)
iotsystem::DigitalArtifact_strategy = st.builds(
    iotsystem::DigitalArtifact,
)
iotsystem::Device_strategy = st.builds(
    iotsystem::Device,
)
Device_strategy = st.builds(
    Device,
)
iotsystem::Actuator_strategy = st.builds(
    iotsystem::Actuator,
)
iotsystem::Sensor_strategy = st.builds(
    iotsystem::Sensor,
)
iotsystem::Condition_strategy = st.builds(
    iotsystem::Condition,
    expectedValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    relationalOperator=
        safe_text
)
iotsystem::Action_strategy = st.builds(
    iotsystem::Action,
    action=
        safe_text
)

@given(instance=iotsystem::NamedElement_strategy)
@settings(max_examples=50)
def test_iotsystem::namedelement_instantiation(instance):
    assert isinstance(instance, iotsystem::NamedElement)

@given(instance=iotsystem::NamedElement_strategy)
def test_iotsystem::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iotsystem::NamedElement_strategy)
def test_iotsystem::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotsystem::Parameter_strategy)
@settings(max_examples=50)
def test_iotsystem::parameter_instantiation(instance):
    assert isinstance(instance, iotsystem::Parameter)

@given(instance=iotsystem::Parameter_strategy)
def test_iotsystem::parameter_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=iotsystem::Parameter_strategy)
def test_iotsystem::parameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iotsystem::Parameter_strategy)
def test_iotsystem::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iotsystem::Parameter_strategy)
def test_iotsystem::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotsystem::Resource_strategy)
@settings(max_examples=50)
def test_iotsystem::resource_instantiation(instance):
    assert isinstance(instance, iotsystem::Resource)

@given(instance=iotsystem::Resource_strategy)
def test_iotsystem::resource_measurement_type(instance):
    assert isinstance(instance.measurement, str)


@given(instance=iotsystem::Resource_strategy)
def test_iotsystem::resource_measurement_setter(instance):
    original = instance.measurement
    instance.measurement = original
    assert instance.measurement == original

@given(instance=iotsystem::Resource_strategy)
def test_iotsystem::resource_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=iotsystem::Resource_strategy)
def test_iotsystem::resource_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=iotsystem::Rule_strategy)
@settings(max_examples=50)
def test_iotsystem::rule_instantiation(instance):
    assert isinstance(instance, iotsystem::Rule)

@given(instance=iotsystem::PhysicalEntity_strategy)
@settings(max_examples=50)
def test_iotsystem::physicalentity_instantiation(instance):
    assert isinstance(instance, iotsystem::PhysicalEntity)

@given(instance=iotsystem::IotSystem_strategy)
@settings(max_examples=50)
def test_iotsystem::iotsystem_instantiation(instance):
    assert isinstance(instance, iotsystem::IotSystem)

@given(instance=iotsystem::DigitalArtifact_strategy)
@settings(max_examples=50)
def test_iotsystem::digitalartifact_instantiation(instance):
    assert isinstance(instance, iotsystem::DigitalArtifact)

@given(instance=iotsystem::Device_strategy)
@settings(max_examples=50)
def test_iotsystem::device_instantiation(instance):
    assert isinstance(instance, iotsystem::Device)

@given(instance=Device_strategy)
@settings(max_examples=50)
def test_device_instantiation(instance):
    assert isinstance(instance, Device)

@given(instance=iotsystem::Actuator_strategy)
@settings(max_examples=50)
def test_iotsystem::actuator_instantiation(instance):
    assert isinstance(instance, iotsystem::Actuator)

@given(instance=iotsystem::Sensor_strategy)
@settings(max_examples=50)
def test_iotsystem::sensor_instantiation(instance):
    assert isinstance(instance, iotsystem::Sensor)

@given(instance=iotsystem::Condition_strategy)
@settings(max_examples=50)
def test_iotsystem::condition_instantiation(instance):
    assert isinstance(instance, iotsystem::Condition)

@given(instance=iotsystem::Condition_strategy)
def test_iotsystem::condition_expectedValue_type(instance):
    assert isinstance(instance.expectedValue, float)


@given(instance=iotsystem::Condition_strategy)
def test_iotsystem::condition_expectedValue_setter(instance):
    original = instance.expectedValue
    instance.expectedValue = original
    assert instance.expectedValue == original

@given(instance=iotsystem::Condition_strategy)
def test_iotsystem::condition_relationalOperator_type(instance):
    assert isinstance(instance.relationalOperator, str)


@given(instance=iotsystem::Condition_strategy)
def test_iotsystem::condition_relationalOperator_setter(instance):
    original = instance.relationalOperator
    instance.relationalOperator = original
    assert instance.relationalOperator == original

@given(instance=iotsystem::Action_strategy)
@settings(max_examples=50)
def test_iotsystem::action_instantiation(instance):
    assert isinstance(instance, iotsystem::Action)

@given(instance=iotsystem::Action_strategy)
def test_iotsystem::action_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=iotsystem::Action_strategy)
def test_iotsystem::action_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original
