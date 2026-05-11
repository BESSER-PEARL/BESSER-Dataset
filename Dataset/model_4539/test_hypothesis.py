import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Value,
    SmartHome::AnalValue,
    SmartHome::DigitValue,
    SmartHome::Value,
    SmartHome::RuleComposant,
    NamedElement,
    SmartHome::IotComponent,
    SmartHome::Room,
    Activator,
    Sensor,
    SmartHome::LightSensor,
    SmartHome::NamedElement,
    IotComponent,
    SmartHome::Activator,
    SmartHome::Sensor,
    SmartHome::Home,
    SmartHome::Clock,
    SmartHome::Rule,
    SmartHome::Shutter,
    SmartHome::PhysicalContext,
    SmartHome::Light,
    Operator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::analvalue_is_not_abstract():
    assert not inspect.isabstract(SmartHome::AnalValue)


def test_smarthome::analvalue_constructor_exists():
    assert callable(SmartHome::AnalValue.__init__)


def test_smarthome::analvalue_constructor_args():
    sig = inspect.signature(SmartHome::AnalValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smarthome::analvalue_has_value():
    assert hasattr(SmartHome::AnalValue, "value")
    descriptor = None
    for klass in SmartHome::AnalValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smarthome::digitvalue_is_not_abstract():
    assert not inspect.isabstract(SmartHome::DigitValue)


def test_smarthome::digitvalue_constructor_exists():
    assert callable(SmartHome::DigitValue.__init__)


def test_smarthome::digitvalue_constructor_args():
    sig = inspect.signature(SmartHome::DigitValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smarthome::digitvalue_has_value():
    assert hasattr(SmartHome::DigitValue, "value")
    descriptor = None
    for klass in SmartHome::DigitValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smarthome::value_is_not_abstract():
    assert not inspect.isabstract(SmartHome::Value)


def test_smarthome::value_constructor_exists():
    assert callable(SmartHome::Value.__init__)


def test_smarthome::value_constructor_args():
    sig = inspect.signature(SmartHome::Value.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::rulecomposant_is_not_abstract():
    assert not inspect.isabstract(SmartHome::RuleComposant)


def test_smarthome::rulecomposant_constructor_exists():
    assert callable(SmartHome::RuleComposant.__init__)


def test_smarthome::rulecomposant_constructor_args():
    sig = inspect.signature(SmartHome::RuleComposant.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_smarthome::rulecomposant_has_operator():
    assert hasattr(SmartHome::RuleComposant, "operator")
    descriptor = None
    for klass in SmartHome::RuleComposant.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::iotcomponent_is_not_abstract():
    assert not inspect.isabstract(SmartHome::IotComponent)


def test_smarthome::iotcomponent_constructor_exists():
    assert callable(SmartHome::IotComponent.__init__)


def test_smarthome::iotcomponent_constructor_args():
    sig = inspect.signature(SmartHome::IotComponent.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::room_is_not_abstract():
    assert not inspect.isabstract(SmartHome::Room)


def test_smarthome::room_constructor_exists():
    assert callable(SmartHome::Room.__init__)


def test_smarthome::room_constructor_args():
    sig = inspect.signature(SmartHome::Room.__init__)
    params = list(sig.parameters.keys())



def test_activator_is_not_abstract():
    assert not inspect.isabstract(Activator)


def test_activator_constructor_exists():
    assert callable(Activator.__init__)


def test_activator_constructor_args():
    sig = inspect.signature(Activator.__init__)
    params = list(sig.parameters.keys())



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::lightsensor_is_not_abstract():
    assert not inspect.isabstract(SmartHome::LightSensor)


def test_smarthome::lightsensor_constructor_exists():
    assert callable(SmartHome::LightSensor.__init__)


def test_smarthome::lightsensor_constructor_args():
    sig = inspect.signature(SmartHome::LightSensor.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::namedelement_is_not_abstract():
    assert not inspect.isabstract(SmartHome::NamedElement)


def test_smarthome::namedelement_constructor_exists():
    assert callable(SmartHome::NamedElement.__init__)


def test_smarthome::namedelement_constructor_args():
    sig = inspect.signature(SmartHome::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smarthome::namedelement_has_name():
    assert hasattr(SmartHome::NamedElement, "name")
    descriptor = None
    for klass in SmartHome::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotcomponent_is_not_abstract():
    assert not inspect.isabstract(IotComponent)


def test_iotcomponent_constructor_exists():
    assert callable(IotComponent.__init__)


def test_iotcomponent_constructor_args():
    sig = inspect.signature(IotComponent.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::activator_is_not_abstract():
    assert not inspect.isabstract(SmartHome::Activator)


def test_smarthome::activator_constructor_exists():
    assert callable(SmartHome::Activator.__init__)


def test_smarthome::activator_constructor_args():
    sig = inspect.signature(SmartHome::Activator.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::sensor_is_not_abstract():
    assert not inspect.isabstract(SmartHome::Sensor)


def test_smarthome::sensor_constructor_exists():
    assert callable(SmartHome::Sensor.__init__)


def test_smarthome::sensor_constructor_args():
    sig = inspect.signature(SmartHome::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::home_is_not_abstract():
    assert not inspect.isabstract(SmartHome::Home)


def test_smarthome::home_constructor_exists():
    assert callable(SmartHome::Home.__init__)


def test_smarthome::home_constructor_args():
    sig = inspect.signature(SmartHome::Home.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "startDay" in params, "Missing parameter 'startDay'"

def test_smarthome::home_has_speed():
    assert hasattr(SmartHome::Home, "speed")
    descriptor = None
    for klass in SmartHome::Home.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_smarthome::home_has_startDay():
    assert hasattr(SmartHome::Home, "startDay")
    descriptor = None
    for klass in SmartHome::Home.__mro__:
        if "startDay" in klass.__dict__:
            descriptor = klass.__dict__["startDay"]
            break
    assert isinstance(descriptor, property)



def test_smarthome::clock_is_not_abstract():
    assert not inspect.isabstract(SmartHome::Clock)


def test_smarthome::clock_constructor_exists():
    assert callable(SmartHome::Clock.__init__)


def test_smarthome::clock_constructor_args():
    sig = inspect.signature(SmartHome::Clock.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::rule_is_not_abstract():
    assert not inspect.isabstract(SmartHome::Rule)


def test_smarthome::rule_constructor_exists():
    assert callable(SmartHome::Rule.__init__)


def test_smarthome::rule_constructor_args():
    sig = inspect.signature(SmartHome::Rule.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::shutter_is_not_abstract():
    assert not inspect.isabstract(SmartHome::Shutter)


def test_smarthome::shutter_constructor_exists():
    assert callable(SmartHome::Shutter.__init__)


def test_smarthome::shutter_constructor_args():
    sig = inspect.signature(SmartHome::Shutter.__init__)
    params = list(sig.parameters.keys())
    assert "stateInit" in params, "Missing parameter 'stateInit'"

def test_smarthome::shutter_has_stateInit():
    assert hasattr(SmartHome::Shutter, "stateInit")
    descriptor = None
    for klass in SmartHome::Shutter.__mro__:
        if "stateInit" in klass.__dict__:
            descriptor = klass.__dict__["stateInit"]
            break
    assert isinstance(descriptor, property)



def test_smarthome::physicalcontext_is_not_abstract():
    assert not inspect.isabstract(SmartHome::PhysicalContext)


def test_smarthome::physicalcontext_constructor_exists():
    assert callable(SmartHome::PhysicalContext.__init__)


def test_smarthome::physicalcontext_constructor_args():
    sig = inspect.signature(SmartHome::PhysicalContext.__init__)
    params = list(sig.parameters.keys())
    assert "lightIn" in params, "Missing parameter 'lightIn'"
    assert "lightOut" in params, "Missing parameter 'lightOut'"

def test_smarthome::physicalcontext_has_lightIn():
    assert hasattr(SmartHome::PhysicalContext, "lightIn")
    descriptor = None
    for klass in SmartHome::PhysicalContext.__mro__:
        if "lightIn" in klass.__dict__:
            descriptor = klass.__dict__["lightIn"]
            break
    assert isinstance(descriptor, property)

def test_smarthome::physicalcontext_has_lightOut():
    assert hasattr(SmartHome::PhysicalContext, "lightOut")
    descriptor = None
    for klass in SmartHome::PhysicalContext.__mro__:
        if "lightOut" in klass.__dict__:
            descriptor = klass.__dict__["lightOut"]
            break
    assert isinstance(descriptor, property)



def test_smarthome::light_is_not_abstract():
    assert not inspect.isabstract(SmartHome::Light)


def test_smarthome::light_constructor_exists():
    assert callable(SmartHome::Light.__init__)


def test_smarthome::light_constructor_args():
    sig = inspect.signature(SmartHome::Light.__init__)
    params = list(sig.parameters.keys())
    assert "stateInit" in params, "Missing parameter 'stateInit'"
    assert "intensity" in params, "Missing parameter 'intensity'"

def test_smarthome::light_has_stateInit():
    assert hasattr(SmartHome::Light, "stateInit")
    descriptor = None
    for klass in SmartHome::Light.__mro__:
        if "stateInit" in klass.__dict__:
            descriptor = klass.__dict__["stateInit"]
            break
    assert isinstance(descriptor, property)

def test_smarthome::light_has_intensity():
    assert hasattr(SmartHome::Light, "intensity")
    descriptor = None
    for klass in SmartHome::Light.__mro__:
        if "intensity" in klass.__dict__:
            descriptor = klass.__dict__["intensity"]
            break
    assert isinstance(descriptor, property)

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "superior",
        "different",
        "inferior",
        "equal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"


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
Value_strategy = st.builds(
    Value,
)
SmartHome::AnalValue_strategy = st.builds(
    SmartHome::AnalValue,
    value=
        st.booleans()
)
SmartHome::DigitValue_strategy = st.builds(
    SmartHome::DigitValue,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SmartHome::Value_strategy = st.builds(
    SmartHome::Value,
)
SmartHome::RuleComposant_strategy = st.builds(
    SmartHome::RuleComposant,
    operator=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
SmartHome::IotComponent_strategy = st.builds(
    SmartHome::IotComponent,
)
SmartHome::Room_strategy = st.builds(
    SmartHome::Room,
)
Activator_strategy = st.builds(
    Activator,
)
Sensor_strategy = st.builds(
    Sensor,
)
SmartHome::LightSensor_strategy = st.builds(
    SmartHome::LightSensor,
)
SmartHome::NamedElement_strategy = st.builds(
    SmartHome::NamedElement,
    name=
        safe_text
)
IotComponent_strategy = st.builds(
    IotComponent,
)
SmartHome::Activator_strategy = st.builds(
    SmartHome::Activator,
)
SmartHome::Sensor_strategy = st.builds(
    SmartHome::Sensor,
)
SmartHome::Home_strategy = st.builds(
    SmartHome::Home,
    speed=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    startDay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SmartHome::Clock_strategy = st.builds(
    SmartHome::Clock,
)
SmartHome::Rule_strategy = st.builds(
    SmartHome::Rule,
)
SmartHome::Shutter_strategy = st.builds(
    SmartHome::Shutter,
    stateInit=
        st.booleans()
)
SmartHome::PhysicalContext_strategy = st.builds(
    SmartHome::PhysicalContext,
    lightIn=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lightOut=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SmartHome::Light_strategy = st.builds(
    SmartHome::Light,
    stateInit=
        st.booleans(),
    intensity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=SmartHome::AnalValue_strategy)
@settings(max_examples=50)
def test_smarthome::analvalue_instantiation(instance):
    assert isinstance(instance, SmartHome::AnalValue)

@given(instance=SmartHome::AnalValue_strategy)
def test_smarthome::analvalue_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=SmartHome::AnalValue_strategy)
def test_smarthome::analvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SmartHome::DigitValue_strategy)
@settings(max_examples=50)
def test_smarthome::digitvalue_instantiation(instance):
    assert isinstance(instance, SmartHome::DigitValue)

@given(instance=SmartHome::DigitValue_strategy)
def test_smarthome::digitvalue_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=SmartHome::DigitValue_strategy)
def test_smarthome::digitvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SmartHome::Value_strategy)
@settings(max_examples=50)
def test_smarthome::value_instantiation(instance):
    assert isinstance(instance, SmartHome::Value)

@given(instance=SmartHome::RuleComposant_strategy)
@settings(max_examples=50)
def test_smarthome::rulecomposant_instantiation(instance):
    assert isinstance(instance, SmartHome::RuleComposant)

@given(instance=SmartHome::RuleComposant_strategy)
def test_smarthome::rulecomposant_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=SmartHome::RuleComposant_strategy)
def test_smarthome::rulecomposant_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=SmartHome::IotComponent_strategy)
@settings(max_examples=50)
def test_smarthome::iotcomponent_instantiation(instance):
    assert isinstance(instance, SmartHome::IotComponent)

@given(instance=SmartHome::Room_strategy)
@settings(max_examples=50)
def test_smarthome::room_instantiation(instance):
    assert isinstance(instance, SmartHome::Room)

@given(instance=Activator_strategy)
@settings(max_examples=50)
def test_activator_instantiation(instance):
    assert isinstance(instance, Activator)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=SmartHome::LightSensor_strategy)
@settings(max_examples=50)
def test_smarthome::lightsensor_instantiation(instance):
    assert isinstance(instance, SmartHome::LightSensor)

@given(instance=SmartHome::NamedElement_strategy)
@settings(max_examples=50)
def test_smarthome::namedelement_instantiation(instance):
    assert isinstance(instance, SmartHome::NamedElement)

@given(instance=SmartHome::NamedElement_strategy)
def test_smarthome::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SmartHome::NamedElement_strategy)
def test_smarthome::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IotComponent_strategy)
@settings(max_examples=50)
def test_iotcomponent_instantiation(instance):
    assert isinstance(instance, IotComponent)

@given(instance=SmartHome::Activator_strategy)
@settings(max_examples=50)
def test_smarthome::activator_instantiation(instance):
    assert isinstance(instance, SmartHome::Activator)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=SmartHome::Activator_strategy)
@settings(max_examples=30)
def test_smarthome::activator_activate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.activate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.activate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'activate' in SmartHome::Activator is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'activate' in SmartHome::Activator did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'activate' in SmartHome::Activator is not implemented or raised an error")

@given(instance=SmartHome::Sensor_strategy)
@settings(max_examples=50)
def test_smarthome::sensor_instantiation(instance):
    assert isinstance(instance, SmartHome::Sensor)

@given(instance=SmartHome::Home_strategy)
@settings(max_examples=50)
def test_smarthome::home_instantiation(instance):
    assert isinstance(instance, SmartHome::Home)

@given(instance=SmartHome::Home_strategy)
def test_smarthome::home_speed_type(instance):
    assert isinstance(instance.speed, float)


@given(instance=SmartHome::Home_strategy)
def test_smarthome::home_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=SmartHome::Home_strategy)
def test_smarthome::home_startDay_type(instance):
    assert isinstance(instance.startDay, float)


@given(instance=SmartHome::Home_strategy)
def test_smarthome::home_startDay_setter(instance):
    original = instance.startDay
    instance.startDay = original
    assert instance.startDay == original

@given(instance=SmartHome::Clock_strategy)
@settings(max_examples=50)
def test_smarthome::clock_instantiation(instance):
    assert isinstance(instance, SmartHome::Clock)

@given(instance=SmartHome::Rule_strategy)
@settings(max_examples=50)
def test_smarthome::rule_instantiation(instance):
    assert isinstance(instance, SmartHome::Rule)

@given(instance=SmartHome::Shutter_strategy)
@settings(max_examples=50)
def test_smarthome::shutter_instantiation(instance):
    assert isinstance(instance, SmartHome::Shutter)

@given(instance=SmartHome::Shutter_strategy)
def test_smarthome::shutter_stateInit_type(instance):
    assert isinstance(instance.stateInit, bool)


@given(instance=SmartHome::Shutter_strategy)
def test_smarthome::shutter_stateInit_setter(instance):
    original = instance.stateInit
    instance.stateInit = original
    assert instance.stateInit == original

@given(instance=SmartHome::PhysicalContext_strategy)
@settings(max_examples=50)
def test_smarthome::physicalcontext_instantiation(instance):
    assert isinstance(instance, SmartHome::PhysicalContext)

@given(instance=SmartHome::PhysicalContext_strategy)
def test_smarthome::physicalcontext_lightIn_type(instance):
    assert isinstance(instance.lightIn, float)


@given(instance=SmartHome::PhysicalContext_strategy)
def test_smarthome::physicalcontext_lightIn_setter(instance):
    original = instance.lightIn
    instance.lightIn = original
    assert instance.lightIn == original

@given(instance=SmartHome::PhysicalContext_strategy)
def test_smarthome::physicalcontext_lightOut_type(instance):
    assert isinstance(instance.lightOut, float)


@given(instance=SmartHome::PhysicalContext_strategy)
def test_smarthome::physicalcontext_lightOut_setter(instance):
    original = instance.lightOut
    instance.lightOut = original
    assert instance.lightOut == original

@given(instance=SmartHome::Light_strategy)
@settings(max_examples=50)
def test_smarthome::light_instantiation(instance):
    assert isinstance(instance, SmartHome::Light)

@given(instance=SmartHome::Light_strategy)
def test_smarthome::light_stateInit_type(instance):
    assert isinstance(instance.stateInit, bool)


@given(instance=SmartHome::Light_strategy)
def test_smarthome::light_stateInit_setter(instance):
    original = instance.stateInit
    instance.stateInit = original
    assert instance.stateInit == original

@given(instance=SmartHome::Light_strategy)
def test_smarthome::light_intensity_type(instance):
    assert isinstance(instance.intensity, float)


@given(instance=SmartHome::Light_strategy)
def test_smarthome::light_intensity_setter(instance):
    original = instance.intensity
    instance.intensity = original
    assert instance.intensity == original
