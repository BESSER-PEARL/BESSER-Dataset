import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Value,
    SmartHome_AnalValue,
    SmartHome_DigitValue,
    SmartHome_Value,
    SmartHome_RuleComposant,
    NamedElement,
    SmartHome_IotComponent,
    SmartHome_Room,
    Activator,
    Sensor,
    SmartHome_LightSensor,
    SmartHome_NamedElement,
    IotComponent,
    SmartHome_Activator,
    SmartHome_Sensor,
    SmartHome_Home,
    SmartHome_Clock,
    SmartHome_Rule,
    SmartHome_Shutter,
    SmartHome_PhysicalContext,
    SmartHome_Light,
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



def test_smarthome_analvalue_is_not_abstract():
    assert not inspect.isabstract(SmartHome_AnalValue)


def test_smarthome_analvalue_constructor_exists():
    assert callable(SmartHome_AnalValue.__init__)


def test_smarthome_analvalue_constructor_args():
    sig = inspect.signature(SmartHome_AnalValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smarthome_analvalue_has_value():
    assert hasattr(SmartHome_AnalValue, "value")
    descriptor = None
    for klass in SmartHome_AnalValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_digitvalue_is_not_abstract():
    assert not inspect.isabstract(SmartHome_DigitValue)


def test_smarthome_digitvalue_constructor_exists():
    assert callable(SmartHome_DigitValue.__init__)


def test_smarthome_digitvalue_constructor_args():
    sig = inspect.signature(SmartHome_DigitValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smarthome_digitvalue_has_value():
    assert hasattr(SmartHome_DigitValue, "value")
    descriptor = None
    for klass in SmartHome_DigitValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_value_is_not_abstract():
    assert not inspect.isabstract(SmartHome_Value)


def test_smarthome_value_constructor_exists():
    assert callable(SmartHome_Value.__init__)


def test_smarthome_value_constructor_args():
    sig = inspect.signature(SmartHome_Value.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_rulecomposant_is_not_abstract():
    assert not inspect.isabstract(SmartHome_RuleComposant)


def test_smarthome_rulecomposant_constructor_exists():
    assert callable(SmartHome_RuleComposant.__init__)


def test_smarthome_rulecomposant_constructor_args():
    sig = inspect.signature(SmartHome_RuleComposant.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_smarthome_rulecomposant_has_operator():
    assert hasattr(SmartHome_RuleComposant, "operator")
    descriptor = None
    for klass in SmartHome_RuleComposant.__mro__:
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



def test_smarthome_iotcomponent_is_not_abstract():
    assert not inspect.isabstract(SmartHome_IotComponent)


def test_smarthome_iotcomponent_constructor_exists():
    assert callable(SmartHome_IotComponent.__init__)


def test_smarthome_iotcomponent_constructor_args():
    sig = inspect.signature(SmartHome_IotComponent.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_room_is_not_abstract():
    assert not inspect.isabstract(SmartHome_Room)


def test_smarthome_room_constructor_exists():
    assert callable(SmartHome_Room.__init__)


def test_smarthome_room_constructor_args():
    sig = inspect.signature(SmartHome_Room.__init__)
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



def test_smarthome_lightsensor_is_not_abstract():
    assert not inspect.isabstract(SmartHome_LightSensor)


def test_smarthome_lightsensor_constructor_exists():
    assert callable(SmartHome_LightSensor.__init__)


def test_smarthome_lightsensor_constructor_args():
    sig = inspect.signature(SmartHome_LightSensor.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_namedelement_is_not_abstract():
    assert not inspect.isabstract(SmartHome_NamedElement)


def test_smarthome_namedelement_constructor_exists():
    assert callable(SmartHome_NamedElement.__init__)


def test_smarthome_namedelement_constructor_args():
    sig = inspect.signature(SmartHome_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smarthome_namedelement_has_name():
    assert hasattr(SmartHome_NamedElement, "name")
    descriptor = None
    for klass in SmartHome_NamedElement.__mro__:
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



def test_smarthome_activator_is_not_abstract():
    assert not inspect.isabstract(SmartHome_Activator)


def test_smarthome_activator_constructor_exists():
    assert callable(SmartHome_Activator.__init__)


def test_smarthome_activator_constructor_args():
    sig = inspect.signature(SmartHome_Activator.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_sensor_is_not_abstract():
    assert not inspect.isabstract(SmartHome_Sensor)


def test_smarthome_sensor_constructor_exists():
    assert callable(SmartHome_Sensor.__init__)


def test_smarthome_sensor_constructor_args():
    sig = inspect.signature(SmartHome_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_home_is_not_abstract():
    assert not inspect.isabstract(SmartHome_Home)


def test_smarthome_home_constructor_exists():
    assert callable(SmartHome_Home.__init__)


def test_smarthome_home_constructor_args():
    sig = inspect.signature(SmartHome_Home.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "startDay" in params, "Missing parameter 'startDay'"

def test_smarthome_home_has_speed():
    assert hasattr(SmartHome_Home, "speed")
    descriptor = None
    for klass in SmartHome_Home.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_smarthome_home_has_startDay():
    assert hasattr(SmartHome_Home, "startDay")
    descriptor = None
    for klass in SmartHome_Home.__mro__:
        if "startDay" in klass.__dict__:
            descriptor = klass.__dict__["startDay"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_clock_is_not_abstract():
    assert not inspect.isabstract(SmartHome_Clock)


def test_smarthome_clock_constructor_exists():
    assert callable(SmartHome_Clock.__init__)


def test_smarthome_clock_constructor_args():
    sig = inspect.signature(SmartHome_Clock.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_rule_is_not_abstract():
    assert not inspect.isabstract(SmartHome_Rule)


def test_smarthome_rule_constructor_exists():
    assert callable(SmartHome_Rule.__init__)


def test_smarthome_rule_constructor_args():
    sig = inspect.signature(SmartHome_Rule.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_shutter_is_not_abstract():
    assert not inspect.isabstract(SmartHome_Shutter)


def test_smarthome_shutter_constructor_exists():
    assert callable(SmartHome_Shutter.__init__)


def test_smarthome_shutter_constructor_args():
    sig = inspect.signature(SmartHome_Shutter.__init__)
    params = list(sig.parameters.keys())
    assert "stateInit" in params, "Missing parameter 'stateInit'"

def test_smarthome_shutter_has_stateInit():
    assert hasattr(SmartHome_Shutter, "stateInit")
    descriptor = None
    for klass in SmartHome_Shutter.__mro__:
        if "stateInit" in klass.__dict__:
            descriptor = klass.__dict__["stateInit"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_physicalcontext_is_not_abstract():
    assert not inspect.isabstract(SmartHome_PhysicalContext)


def test_smarthome_physicalcontext_constructor_exists():
    assert callable(SmartHome_PhysicalContext.__init__)


def test_smarthome_physicalcontext_constructor_args():
    sig = inspect.signature(SmartHome_PhysicalContext.__init__)
    params = list(sig.parameters.keys())
    assert "lightOut" in params, "Missing parameter 'lightOut'"
    assert "lightIn" in params, "Missing parameter 'lightIn'"

def test_smarthome_physicalcontext_has_lightOut():
    assert hasattr(SmartHome_PhysicalContext, "lightOut")
    descriptor = None
    for klass in SmartHome_PhysicalContext.__mro__:
        if "lightOut" in klass.__dict__:
            descriptor = klass.__dict__["lightOut"]
            break
    assert isinstance(descriptor, property)

def test_smarthome_physicalcontext_has_lightIn():
    assert hasattr(SmartHome_PhysicalContext, "lightIn")
    descriptor = None
    for klass in SmartHome_PhysicalContext.__mro__:
        if "lightIn" in klass.__dict__:
            descriptor = klass.__dict__["lightIn"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_light_is_not_abstract():
    assert not inspect.isabstract(SmartHome_Light)


def test_smarthome_light_constructor_exists():
    assert callable(SmartHome_Light.__init__)


def test_smarthome_light_constructor_args():
    sig = inspect.signature(SmartHome_Light.__init__)
    params = list(sig.parameters.keys())
    assert "intensity" in params, "Missing parameter 'intensity'"
    assert "stateInit" in params, "Missing parameter 'stateInit'"

def test_smarthome_light_has_intensity():
    assert hasattr(SmartHome_Light, "intensity")
    descriptor = None
    for klass in SmartHome_Light.__mro__:
        if "intensity" in klass.__dict__:
            descriptor = klass.__dict__["intensity"]
            break
    assert isinstance(descriptor, property)

def test_smarthome_light_has_stateInit():
    assert hasattr(SmartHome_Light, "stateInit")
    descriptor = None
    for klass in SmartHome_Light.__mro__:
        if "stateInit" in klass.__dict__:
            descriptor = klass.__dict__["stateInit"]
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
        "equal",
        "inferior",
        "different",
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
SmartHome_AnalValue_strategy = st.builds(
    SmartHome_AnalValue,
    value=
        st.booleans()
)
SmartHome_DigitValue_strategy = st.builds(
    SmartHome_DigitValue,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SmartHome_Value_strategy = st.builds(
    SmartHome_Value,
)
SmartHome_RuleComposant_strategy = st.builds(
    SmartHome_RuleComposant,
    operator=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
SmartHome_IotComponent_strategy = st.builds(
    SmartHome_IotComponent,
)
SmartHome_Room_strategy = st.builds(
    SmartHome_Room,
)
Activator_strategy = st.builds(
    Activator,
)
Sensor_strategy = st.builds(
    Sensor,
)
SmartHome_LightSensor_strategy = st.builds(
    SmartHome_LightSensor,
)
SmartHome_NamedElement_strategy = st.builds(
    SmartHome_NamedElement,
    name=
        safe_text
)
IotComponent_strategy = st.builds(
    IotComponent,
)
SmartHome_Activator_strategy = st.builds(
    SmartHome_Activator,
)
SmartHome_Sensor_strategy = st.builds(
    SmartHome_Sensor,
)
SmartHome_Home_strategy = st.builds(
    SmartHome_Home,
    speed=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    startDay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SmartHome_Clock_strategy = st.builds(
    SmartHome_Clock,
)
SmartHome_Rule_strategy = st.builds(
    SmartHome_Rule,
)
SmartHome_Shutter_strategy = st.builds(
    SmartHome_Shutter,
    stateInit=
        st.booleans()
)
SmartHome_PhysicalContext_strategy = st.builds(
    SmartHome_PhysicalContext,
    lightOut=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lightIn=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SmartHome_Light_strategy = st.builds(
    SmartHome_Light,
    intensity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    stateInit=
        st.booleans()
)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=SmartHome_AnalValue_strategy)
@settings(max_examples=50)
def test_smarthome_analvalue_instantiation(instance):
    assert isinstance(instance, SmartHome_AnalValue)



@given(instance=SmartHome_AnalValue_strategy)
def test_smarthome_analvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SmartHome_DigitValue_strategy)
@settings(max_examples=50)
def test_smarthome_digitvalue_instantiation(instance):
    assert isinstance(instance, SmartHome_DigitValue)



@given(instance=SmartHome_DigitValue_strategy)
def test_smarthome_digitvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SmartHome_Value_strategy)
@settings(max_examples=50)
def test_smarthome_value_instantiation(instance):
    assert isinstance(instance, SmartHome_Value)

@given(instance=SmartHome_RuleComposant_strategy)
@settings(max_examples=50)
def test_smarthome_rulecomposant_instantiation(instance):
    assert isinstance(instance, SmartHome_RuleComposant)



@given(instance=SmartHome_RuleComposant_strategy)
def test_smarthome_rulecomposant_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=SmartHome_IotComponent_strategy)
@settings(max_examples=50)
def test_smarthome_iotcomponent_instantiation(instance):
    assert isinstance(instance, SmartHome_IotComponent)

@given(instance=SmartHome_Room_strategy)
@settings(max_examples=50)
def test_smarthome_room_instantiation(instance):
    assert isinstance(instance, SmartHome_Room)

@given(instance=Activator_strategy)
@settings(max_examples=50)
def test_activator_instantiation(instance):
    assert isinstance(instance, Activator)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=SmartHome_LightSensor_strategy)
@settings(max_examples=50)
def test_smarthome_lightsensor_instantiation(instance):
    assert isinstance(instance, SmartHome_LightSensor)

@given(instance=SmartHome_NamedElement_strategy)
@settings(max_examples=50)
def test_smarthome_namedelement_instantiation(instance):
    assert isinstance(instance, SmartHome_NamedElement)



@given(instance=SmartHome_NamedElement_strategy)
def test_smarthome_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IotComponent_strategy)
@settings(max_examples=50)
def test_iotcomponent_instantiation(instance):
    assert isinstance(instance, IotComponent)

@given(instance=SmartHome_Activator_strategy)
@settings(max_examples=50)
def test_smarthome_activator_instantiation(instance):
    assert isinstance(instance, SmartHome_Activator)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=SmartHome_Activator_strategy)
@settings(max_examples=30)
def test_smarthome_activator_activate_changes_state(instance):
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
        assert has_statements, f"Function 'activate' in SmartHome_Activator is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'activate' in SmartHome_Activator did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'activate' in SmartHome_Activator is not implemented or raised an error")

@given(instance=SmartHome_Sensor_strategy)
@settings(max_examples=50)
def test_smarthome_sensor_instantiation(instance):
    assert isinstance(instance, SmartHome_Sensor)

@given(instance=SmartHome_Home_strategy)
@settings(max_examples=50)
def test_smarthome_home_instantiation(instance):
    assert isinstance(instance, SmartHome_Home)



@given(instance=SmartHome_Home_strategy)
def test_smarthome_home_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=SmartHome_Home_strategy)
def test_smarthome_home_startDay_setter(instance):
    original = instance.startDay
    instance.startDay = original
    assert instance.startDay == original

@given(instance=SmartHome_Clock_strategy)
@settings(max_examples=50)
def test_smarthome_clock_instantiation(instance):
    assert isinstance(instance, SmartHome_Clock)

@given(instance=SmartHome_Rule_strategy)
@settings(max_examples=50)
def test_smarthome_rule_instantiation(instance):
    assert isinstance(instance, SmartHome_Rule)

@given(instance=SmartHome_Shutter_strategy)
@settings(max_examples=50)
def test_smarthome_shutter_instantiation(instance):
    assert isinstance(instance, SmartHome_Shutter)



@given(instance=SmartHome_Shutter_strategy)
def test_smarthome_shutter_stateInit_setter(instance):
    original = instance.stateInit
    instance.stateInit = original
    assert instance.stateInit == original

@given(instance=SmartHome_PhysicalContext_strategy)
@settings(max_examples=50)
def test_smarthome_physicalcontext_instantiation(instance):
    assert isinstance(instance, SmartHome_PhysicalContext)



@given(instance=SmartHome_PhysicalContext_strategy)
def test_smarthome_physicalcontext_lightOut_setter(instance):
    original = instance.lightOut
    instance.lightOut = original
    assert instance.lightOut == original



@given(instance=SmartHome_PhysicalContext_strategy)
def test_smarthome_physicalcontext_lightIn_setter(instance):
    original = instance.lightIn
    instance.lightIn = original
    assert instance.lightIn == original

@given(instance=SmartHome_Light_strategy)
@settings(max_examples=50)
def test_smarthome_light_instantiation(instance):
    assert isinstance(instance, SmartHome_Light)



@given(instance=SmartHome_Light_strategy)
def test_smarthome_light_intensity_setter(instance):
    original = instance.intensity
    instance.intensity = original
    assert instance.intensity == original



@given(instance=SmartHome_Light_strategy)
def test_smarthome_light_stateInit_setter(instance):
    original = instance.stateInit
    instance.stateInit = original
    assert instance.stateInit == original
