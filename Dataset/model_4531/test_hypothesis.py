import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    drone_Parameter,
    drone_FlightPerformance,
    drone_Size,
    NamedElement,
    drone_Device,
    drone_Battery,
    drone_Property,
    drone_Action,
    drone_ROSDriver,
    drone_Memory,
    drone_Drone,
    drone_Processor,
    drone_NamedElement,
    LaunchType,
    MemoryType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_drone_parameter_is_not_abstract():
    assert not inspect.isabstract(drone_Parameter)


def test_drone_parameter_constructor_exists():
    assert callable(drone_Parameter.__init__)


def test_drone_parameter_constructor_args():
    sig = inspect.signature(drone_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "description" in params, "Missing parameter 'description'"

def test_drone_parameter_has_key():
    assert hasattr(drone_Parameter, "key")
    descriptor = None
    for klass in drone_Parameter.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_drone_parameter_has_description():
    assert hasattr(drone_Parameter, "description")
    descriptor = None
    for klass in drone_Parameter.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_drone_flightperformance_is_not_abstract():
    assert not inspect.isabstract(drone_FlightPerformance)


def test_drone_flightperformance_constructor_exists():
    assert callable(drone_FlightPerformance.__init__)


def test_drone_flightperformance_constructor_args():
    sig = inspect.signature(drone_FlightPerformance.__init__)
    params = list(sig.parameters.keys())
    assert "minAcceleration" in params, "Missing parameter 'minAcceleration'"
    assert "maxTurnRate" in params, "Missing parameter 'maxTurnRate'"
    assert "minTurnRate" in params, "Missing parameter 'minTurnRate'"
    assert "maxClimbRate" in params, "Missing parameter 'maxClimbRate'"
    assert "maxPayload" in params, "Missing parameter 'maxPayload'"
    assert "maxFlightTimeWithMaxPayload" in params, "Missing parameter 'maxFlightTimeWithMaxPayload'"
    assert "maxAltitude" in params, "Missing parameter 'maxAltitude'"
    assert "maxDescendRate" in params, "Missing parameter 'maxDescendRate'"
    assert "minOperatingTemperature" in params, "Missing parameter 'minOperatingTemperature'"
    assert "maxAcceleration" in params, "Missing parameter 'maxAcceleration'"
    assert "maxOperatingTemperature" in params, "Missing parameter 'maxOperatingTemperature'"
    assert "launchType" in params, "Missing parameter 'launchType'"
    assert "minSpeed" in params, "Missing parameter 'minSpeed'"
    assert "positionHold" in params, "Missing parameter 'positionHold'"
    assert "maxFlightTime" in params, "Missing parameter 'maxFlightTime'"
    assert "maxSpeed" in params, "Missing parameter 'maxSpeed'"

def test_drone_flightperformance_has_minAcceleration():
    assert hasattr(drone_FlightPerformance, "minAcceleration")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "minAcceleration" in klass.__dict__:
            descriptor = klass.__dict__["minAcceleration"]
            break
    assert isinstance(descriptor, property)

def test_drone_flightperformance_has_maxTurnRate():
    assert hasattr(drone_FlightPerformance, "maxTurnRate")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "maxTurnRate" in klass.__dict__:
            descriptor = klass.__dict__["maxTurnRate"]
            break
    assert isinstance(descriptor, property)

def test_drone_flightperformance_has_minTurnRate():
    assert hasattr(drone_FlightPerformance, "minTurnRate")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "minTurnRate" in klass.__dict__:
            descriptor = klass.__dict__["minTurnRate"]
            break
    assert isinstance(descriptor, property)

def test_drone_flightperformance_has_maxClimbRate():
    assert hasattr(drone_FlightPerformance, "maxClimbRate")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "maxClimbRate" in klass.__dict__:
            descriptor = klass.__dict__["maxClimbRate"]
            break
    assert isinstance(descriptor, property)

def test_drone_flightperformance_has_maxPayload():
    assert hasattr(drone_FlightPerformance, "maxPayload")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "maxPayload" in klass.__dict__:
            descriptor = klass.__dict__["maxPayload"]
            break
    assert isinstance(descriptor, property)

def test_drone_flightperformance_has_maxFlightTimeWithMaxPayload():
    assert hasattr(drone_FlightPerformance, "maxFlightTimeWithMaxPayload")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "maxFlightTimeWithMaxPayload" in klass.__dict__:
            descriptor = klass.__dict__["maxFlightTimeWithMaxPayload"]
            break
    assert isinstance(descriptor, property)

def test_drone_flightperformance_has_maxAltitude():
    assert hasattr(drone_FlightPerformance, "maxAltitude")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "maxAltitude" in klass.__dict__:
            descriptor = klass.__dict__["maxAltitude"]
            break
    assert isinstance(descriptor, property)

def test_drone_flightperformance_has_maxDescendRate():
    assert hasattr(drone_FlightPerformance, "maxDescendRate")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "maxDescendRate" in klass.__dict__:
            descriptor = klass.__dict__["maxDescendRate"]
            break
    assert isinstance(descriptor, property)

def test_drone_flightperformance_has_minOperatingTemperature():
    assert hasattr(drone_FlightPerformance, "minOperatingTemperature")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "minOperatingTemperature" in klass.__dict__:
            descriptor = klass.__dict__["minOperatingTemperature"]
            break
    assert isinstance(descriptor, property)

def test_drone_flightperformance_has_maxAcceleration():
    assert hasattr(drone_FlightPerformance, "maxAcceleration")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "maxAcceleration" in klass.__dict__:
            descriptor = klass.__dict__["maxAcceleration"]
            break
    assert isinstance(descriptor, property)

def test_drone_flightperformance_has_maxOperatingTemperature():
    assert hasattr(drone_FlightPerformance, "maxOperatingTemperature")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "maxOperatingTemperature" in klass.__dict__:
            descriptor = klass.__dict__["maxOperatingTemperature"]
            break
    assert isinstance(descriptor, property)

def test_drone_flightperformance_has_launchType():
    assert hasattr(drone_FlightPerformance, "launchType")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "launchType" in klass.__dict__:
            descriptor = klass.__dict__["launchType"]
            break
    assert isinstance(descriptor, property)

def test_drone_flightperformance_has_minSpeed():
    assert hasattr(drone_FlightPerformance, "minSpeed")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "minSpeed" in klass.__dict__:
            descriptor = klass.__dict__["minSpeed"]
            break
    assert isinstance(descriptor, property)

def test_drone_flightperformance_has_positionHold():
    assert hasattr(drone_FlightPerformance, "positionHold")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "positionHold" in klass.__dict__:
            descriptor = klass.__dict__["positionHold"]
            break
    assert isinstance(descriptor, property)

def test_drone_flightperformance_has_maxFlightTime():
    assert hasattr(drone_FlightPerformance, "maxFlightTime")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "maxFlightTime" in klass.__dict__:
            descriptor = klass.__dict__["maxFlightTime"]
            break
    assert isinstance(descriptor, property)

def test_drone_flightperformance_has_maxSpeed():
    assert hasattr(drone_FlightPerformance, "maxSpeed")
    descriptor = None
    for klass in drone_FlightPerformance.__mro__:
        if "maxSpeed" in klass.__dict__:
            descriptor = klass.__dict__["maxSpeed"]
            break
    assert isinstance(descriptor, property)



def test_drone_size_is_not_abstract():
    assert not inspect.isabstract(drone_Size)


def test_drone_size_constructor_exists():
    assert callable(drone_Size.__init__)


def test_drone_size_constructor_args():
    sig = inspect.signature(drone_Size.__init__)
    params = list(sig.parameters.keys())
    assert "propellers" in params, "Missing parameter 'propellers'"
    assert "height" in params, "Missing parameter 'height'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "propellerSize" in params, "Missing parameter 'propellerSize'"
    assert "width" in params, "Missing parameter 'width'"
    assert "length" in params, "Missing parameter 'length'"

def test_drone_size_has_propellers():
    assert hasattr(drone_Size, "propellers")
    descriptor = None
    for klass in drone_Size.__mro__:
        if "propellers" in klass.__dict__:
            descriptor = klass.__dict__["propellers"]
            break
    assert isinstance(descriptor, property)

def test_drone_size_has_height():
    assert hasattr(drone_Size, "height")
    descriptor = None
    for klass in drone_Size.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_drone_size_has_weight():
    assert hasattr(drone_Size, "weight")
    descriptor = None
    for klass in drone_Size.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_drone_size_has_propellerSize():
    assert hasattr(drone_Size, "propellerSize")
    descriptor = None
    for klass in drone_Size.__mro__:
        if "propellerSize" in klass.__dict__:
            descriptor = klass.__dict__["propellerSize"]
            break
    assert isinstance(descriptor, property)

def test_drone_size_has_width():
    assert hasattr(drone_Size, "width")
    descriptor = None
    for klass in drone_Size.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_drone_size_has_length():
    assert hasattr(drone_Size, "length")
    descriptor = None
    for klass in drone_Size.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_drone_device_is_not_abstract():
    assert not inspect.isabstract(drone_Device)


def test_drone_device_constructor_exists():
    assert callable(drone_Device.__init__)


def test_drone_device_constructor_args():
    sig = inspect.signature(drone_Device.__init__)
    params = list(sig.parameters.keys())



def test_drone_battery_is_not_abstract():
    assert not inspect.isabstract(drone_Battery)


def test_drone_battery_constructor_exists():
    assert callable(drone_Battery.__init__)


def test_drone_battery_constructor_args():
    sig = inspect.signature(drone_Battery.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "rechargeTime" in params, "Missing parameter 'rechargeTime'"
    assert "voltage" in params, "Missing parameter 'voltage'"
    assert "cellType" in params, "Missing parameter 'cellType'"

def test_drone_battery_has_capacity():
    assert hasattr(drone_Battery, "capacity")
    descriptor = None
    for klass in drone_Battery.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_drone_battery_has_rechargeTime():
    assert hasattr(drone_Battery, "rechargeTime")
    descriptor = None
    for klass in drone_Battery.__mro__:
        if "rechargeTime" in klass.__dict__:
            descriptor = klass.__dict__["rechargeTime"]
            break
    assert isinstance(descriptor, property)

def test_drone_battery_has_voltage():
    assert hasattr(drone_Battery, "voltage")
    descriptor = None
    for klass in drone_Battery.__mro__:
        if "voltage" in klass.__dict__:
            descriptor = klass.__dict__["voltage"]
            break
    assert isinstance(descriptor, property)

def test_drone_battery_has_cellType():
    assert hasattr(drone_Battery, "cellType")
    descriptor = None
    for klass in drone_Battery.__mro__:
        if "cellType" in klass.__dict__:
            descriptor = klass.__dict__["cellType"]
            break
    assert isinstance(descriptor, property)



def test_drone_property_is_not_abstract():
    assert not inspect.isabstract(drone_Property)


def test_drone_property_constructor_exists():
    assert callable(drone_Property.__init__)


def test_drone_property_constructor_args():
    sig = inspect.signature(drone_Property.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_drone_property_has_value():
    assert hasattr(drone_Property, "value")
    descriptor = None
    for klass in drone_Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_drone_action_is_not_abstract():
    assert not inspect.isabstract(drone_Action)


def test_drone_action_constructor_exists():
    assert callable(drone_Action.__init__)


def test_drone_action_constructor_args():
    sig = inspect.signature(drone_Action.__init__)
    params = list(sig.parameters.keys())



def test_drone_rosdriver_is_not_abstract():
    assert not inspect.isabstract(drone_ROSDriver)


def test_drone_rosdriver_constructor_exists():
    assert callable(drone_ROSDriver.__init__)


def test_drone_rosdriver_constructor_args():
    sig = inspect.signature(drone_ROSDriver.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "version" in params, "Missing parameter 'version'"

def test_drone_rosdriver_has_url():
    assert hasattr(drone_ROSDriver, "url")
    descriptor = None
    for klass in drone_ROSDriver.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_drone_rosdriver_has_version():
    assert hasattr(drone_ROSDriver, "version")
    descriptor = None
    for klass in drone_ROSDriver.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_drone_memory_is_not_abstract():
    assert not inspect.isabstract(drone_Memory)


def test_drone_memory_constructor_exists():
    assert callable(drone_Memory.__init__)


def test_drone_memory_constructor_args():
    sig = inspect.signature(drone_Memory.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "type" in params, "Missing parameter 'type'"
    assert "subType" in params, "Missing parameter 'subType'"

def test_drone_memory_has_size():
    assert hasattr(drone_Memory, "size")
    descriptor = None
    for klass in drone_Memory.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_drone_memory_has_type():
    assert hasattr(drone_Memory, "type")
    descriptor = None
    for klass in drone_Memory.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_drone_memory_has_subType():
    assert hasattr(drone_Memory, "subType")
    descriptor = None
    for klass in drone_Memory.__mro__:
        if "subType" in klass.__dict__:
            descriptor = klass.__dict__["subType"]
            break
    assert isinstance(descriptor, property)



def test_drone_drone_is_not_abstract():
    assert not inspect.isabstract(drone_Drone)


def test_drone_drone_constructor_exists():
    assert callable(drone_Drone.__init__)


def test_drone_drone_constructor_args():
    sig = inspect.signature(drone_Drone.__init__)
    params = list(sig.parameters.keys())
    assert "maxVoltage" in params, "Missing parameter 'maxVoltage'"
    assert "radioFrequency" in params, "Missing parameter 'radioFrequency'"
    assert "barometer" in params, "Missing parameter 'barometer'"
    assert "minVoltage" in params, "Missing parameter 'minVoltage'"
    assert "maxPowerConsumption" in params, "Missing parameter 'maxPowerConsumption'"
    assert "magnetometer" in params, "Missing parameter 'magnetometer'"
    assert "onBoardObstacleAvoidance" in params, "Missing parameter 'onBoardObstacleAvoidance'"
    assert "gps" in params, "Missing parameter 'gps'"
    assert "accelerometer" in params, "Missing parameter 'accelerometer'"
    assert "dataRate" in params, "Missing parameter 'dataRate'"
    assert "giro" in params, "Missing parameter 'giro'"
    assert "communicationRange" in params, "Missing parameter 'communicationRange'"

def test_drone_drone_has_maxVoltage():
    assert hasattr(drone_Drone, "maxVoltage")
    descriptor = None
    for klass in drone_Drone.__mro__:
        if "maxVoltage" in klass.__dict__:
            descriptor = klass.__dict__["maxVoltage"]
            break
    assert isinstance(descriptor, property)

def test_drone_drone_has_radioFrequency():
    assert hasattr(drone_Drone, "radioFrequency")
    descriptor = None
    for klass in drone_Drone.__mro__:
        if "radioFrequency" in klass.__dict__:
            descriptor = klass.__dict__["radioFrequency"]
            break
    assert isinstance(descriptor, property)

def test_drone_drone_has_barometer():
    assert hasattr(drone_Drone, "barometer")
    descriptor = None
    for klass in drone_Drone.__mro__:
        if "barometer" in klass.__dict__:
            descriptor = klass.__dict__["barometer"]
            break
    assert isinstance(descriptor, property)

def test_drone_drone_has_minVoltage():
    assert hasattr(drone_Drone, "minVoltage")
    descriptor = None
    for klass in drone_Drone.__mro__:
        if "minVoltage" in klass.__dict__:
            descriptor = klass.__dict__["minVoltage"]
            break
    assert isinstance(descriptor, property)

def test_drone_drone_has_maxPowerConsumption():
    assert hasattr(drone_Drone, "maxPowerConsumption")
    descriptor = None
    for klass in drone_Drone.__mro__:
        if "maxPowerConsumption" in klass.__dict__:
            descriptor = klass.__dict__["maxPowerConsumption"]
            break
    assert isinstance(descriptor, property)

def test_drone_drone_has_magnetometer():
    assert hasattr(drone_Drone, "magnetometer")
    descriptor = None
    for klass in drone_Drone.__mro__:
        if "magnetometer" in klass.__dict__:
            descriptor = klass.__dict__["magnetometer"]
            break
    assert isinstance(descriptor, property)

def test_drone_drone_has_onBoardObstacleAvoidance():
    assert hasattr(drone_Drone, "onBoardObstacleAvoidance")
    descriptor = None
    for klass in drone_Drone.__mro__:
        if "onBoardObstacleAvoidance" in klass.__dict__:
            descriptor = klass.__dict__["onBoardObstacleAvoidance"]
            break
    assert isinstance(descriptor, property)

def test_drone_drone_has_gps():
    assert hasattr(drone_Drone, "gps")
    descriptor = None
    for klass in drone_Drone.__mro__:
        if "gps" in klass.__dict__:
            descriptor = klass.__dict__["gps"]
            break
    assert isinstance(descriptor, property)

def test_drone_drone_has_accelerometer():
    assert hasattr(drone_Drone, "accelerometer")
    descriptor = None
    for klass in drone_Drone.__mro__:
        if "accelerometer" in klass.__dict__:
            descriptor = klass.__dict__["accelerometer"]
            break
    assert isinstance(descriptor, property)

def test_drone_drone_has_dataRate():
    assert hasattr(drone_Drone, "dataRate")
    descriptor = None
    for klass in drone_Drone.__mro__:
        if "dataRate" in klass.__dict__:
            descriptor = klass.__dict__["dataRate"]
            break
    assert isinstance(descriptor, property)

def test_drone_drone_has_giro():
    assert hasattr(drone_Drone, "giro")
    descriptor = None
    for klass in drone_Drone.__mro__:
        if "giro" in klass.__dict__:
            descriptor = klass.__dict__["giro"]
            break
    assert isinstance(descriptor, property)

def test_drone_drone_has_communicationRange():
    assert hasattr(drone_Drone, "communicationRange")
    descriptor = None
    for klass in drone_Drone.__mro__:
        if "communicationRange" in klass.__dict__:
            descriptor = klass.__dict__["communicationRange"]
            break
    assert isinstance(descriptor, property)



def test_drone_processor_is_not_abstract():
    assert not inspect.isabstract(drone_Processor)


def test_drone_processor_constructor_exists():
    assert callable(drone_Processor.__init__)


def test_drone_processor_constructor_args():
    sig = inspect.signature(drone_Processor.__init__)
    params = list(sig.parameters.keys())
    assert "architecture" in params, "Missing parameter 'architecture'"
    assert "frequency" in params, "Missing parameter 'frequency'"

def test_drone_processor_has_architecture():
    assert hasattr(drone_Processor, "architecture")
    descriptor = None
    for klass in drone_Processor.__mro__:
        if "architecture" in klass.__dict__:
            descriptor = klass.__dict__["architecture"]
            break
    assert isinstance(descriptor, property)

def test_drone_processor_has_frequency():
    assert hasattr(drone_Processor, "frequency")
    descriptor = None
    for klass in drone_Processor.__mro__:
        if "frequency" in klass.__dict__:
            descriptor = klass.__dict__["frequency"]
            break
    assert isinstance(descriptor, property)



def test_drone_namedelement_is_not_abstract():
    assert not inspect.isabstract(drone_NamedElement)


def test_drone_namedelement_constructor_exists():
    assert callable(drone_NamedElement.__init__)


def test_drone_namedelement_constructor_args():
    sig = inspect.signature(drone_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_drone_namedelement_has_name():
    assert hasattr(drone_NamedElement, "name")
    descriptor = None
    for klass in drone_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_launchtype_exists():
    # Check that the Enumeration exists
    assert LaunchType is not None

def test_launchtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LaunchType]
    expected_literals = [
        "VTOL",
        "HTOL",
        "OTHER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LaunchType"

def test_memorytype_exists():
    # Check that the Enumeration exists
    assert MemoryType is not None

def test_memorytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MemoryType]
    expected_literals = [
        "VOLATILE",
        "STORAGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MemoryType"


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
drone_Parameter_strategy = st.builds(
    drone_Parameter,
    key=
        safe_text,
    description=
        safe_text
)
drone_FlightPerformance_strategy = st.builds(
    drone_FlightPerformance,
    minAcceleration=
        st.integers(),
    maxTurnRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minTurnRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maxClimbRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maxPayload=
        st.integers(),
    maxFlightTimeWithMaxPayload=
        st.integers(),
    maxAltitude=
        st.integers(),
    maxDescendRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minOperatingTemperature=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maxAcceleration=
        st.integers(),
    maxOperatingTemperature=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    launchType=
        safe_text,
    minSpeed=
        st.integers(),
    positionHold=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maxFlightTime=
        st.integers(),
    maxSpeed=
        st.integers()
)
drone_Size_strategy = st.builds(
    drone_Size,
    propellers=
        st.integers(),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    propellerSize=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
NamedElement_strategy = st.builds(
    NamedElement,
)
drone_Device_strategy = st.builds(
    drone_Device,
)
drone_Battery_strategy = st.builds(
    drone_Battery,
    capacity=
        st.integers(),
    rechargeTime=
        st.integers(),
    voltage=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cellType=
        safe_text
)
drone_Property_strategy = st.builds(
    drone_Property,
    value=
        safe_text
)
drone_Action_strategy = st.builds(
    drone_Action,
)
drone_ROSDriver_strategy = st.builds(
    drone_ROSDriver,
    url=
        safe_text,
    version=
        safe_text
)
drone_Memory_strategy = st.builds(
    drone_Memory,
    size=
        st.integers(),
    type=
        safe_text,
    subType=
        safe_text
)
drone_Drone_strategy = st.builds(
    drone_Drone,
    maxVoltage=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    radioFrequency=
        st.integers(),
    barometer=
        st.booleans(),
    minVoltage=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maxPowerConsumption=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    magnetometer=
        st.booleans(),
    onBoardObstacleAvoidance=
        st.booleans(),
    gps=
        st.booleans(),
    accelerometer=
        st.booleans(),
    dataRate=
        st.integers(),
    giro=
        st.booleans(),
    communicationRange=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
drone_Processor_strategy = st.builds(
    drone_Processor,
    architecture=
        safe_text,
    frequency=
        st.integers()
)
drone_NamedElement_strategy = st.builds(
    drone_NamedElement,
    name=
        safe_text
)

@given(instance=drone_Parameter_strategy)
@settings(max_examples=50)
def test_drone_parameter_instantiation(instance):
    assert isinstance(instance, drone_Parameter)



@given(instance=drone_Parameter_strategy)
def test_drone_parameter_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=drone_Parameter_strategy)
def test_drone_parameter_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=drone_FlightPerformance_strategy)
@settings(max_examples=50)
def test_drone_flightperformance_instantiation(instance):
    assert isinstance(instance, drone_FlightPerformance)



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_minAcceleration_setter(instance):
    original = instance.minAcceleration
    instance.minAcceleration = original
    assert instance.minAcceleration == original



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_maxTurnRate_setter(instance):
    original = instance.maxTurnRate
    instance.maxTurnRate = original
    assert instance.maxTurnRate == original



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_minTurnRate_setter(instance):
    original = instance.minTurnRate
    instance.minTurnRate = original
    assert instance.minTurnRate == original



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_maxClimbRate_setter(instance):
    original = instance.maxClimbRate
    instance.maxClimbRate = original
    assert instance.maxClimbRate == original



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_maxPayload_setter(instance):
    original = instance.maxPayload
    instance.maxPayload = original
    assert instance.maxPayload == original



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_maxFlightTimeWithMaxPayload_setter(instance):
    original = instance.maxFlightTimeWithMaxPayload
    instance.maxFlightTimeWithMaxPayload = original
    assert instance.maxFlightTimeWithMaxPayload == original



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_maxAltitude_setter(instance):
    original = instance.maxAltitude
    instance.maxAltitude = original
    assert instance.maxAltitude == original



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_maxDescendRate_setter(instance):
    original = instance.maxDescendRate
    instance.maxDescendRate = original
    assert instance.maxDescendRate == original



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_minOperatingTemperature_setter(instance):
    original = instance.minOperatingTemperature
    instance.minOperatingTemperature = original
    assert instance.minOperatingTemperature == original



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_maxAcceleration_setter(instance):
    original = instance.maxAcceleration
    instance.maxAcceleration = original
    assert instance.maxAcceleration == original



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_maxOperatingTemperature_setter(instance):
    original = instance.maxOperatingTemperature
    instance.maxOperatingTemperature = original
    assert instance.maxOperatingTemperature == original



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_launchType_setter(instance):
    original = instance.launchType
    instance.launchType = original
    assert instance.launchType == original



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_minSpeed_setter(instance):
    original = instance.minSpeed
    instance.minSpeed = original
    assert instance.minSpeed == original



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_positionHold_setter(instance):
    original = instance.positionHold
    instance.positionHold = original
    assert instance.positionHold == original



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_maxFlightTime_setter(instance):
    original = instance.maxFlightTime
    instance.maxFlightTime = original
    assert instance.maxFlightTime == original



@given(instance=drone_FlightPerformance_strategy)
def test_drone_flightperformance_maxSpeed_setter(instance):
    original = instance.maxSpeed
    instance.maxSpeed = original
    assert instance.maxSpeed == original

@given(instance=drone_Size_strategy)
@settings(max_examples=50)
def test_drone_size_instantiation(instance):
    assert isinstance(instance, drone_Size)



@given(instance=drone_Size_strategy)
def test_drone_size_propellers_setter(instance):
    original = instance.propellers
    instance.propellers = original
    assert instance.propellers == original



@given(instance=drone_Size_strategy)
def test_drone_size_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=drone_Size_strategy)
def test_drone_size_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=drone_Size_strategy)
def test_drone_size_propellerSize_setter(instance):
    original = instance.propellerSize
    instance.propellerSize = original
    assert instance.propellerSize == original



@given(instance=drone_Size_strategy)
def test_drone_size_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=drone_Size_strategy)
def test_drone_size_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=drone_Device_strategy)
@settings(max_examples=50)
def test_drone_device_instantiation(instance):
    assert isinstance(instance, drone_Device)

@given(instance=drone_Battery_strategy)
@settings(max_examples=50)
def test_drone_battery_instantiation(instance):
    assert isinstance(instance, drone_Battery)



@given(instance=drone_Battery_strategy)
def test_drone_battery_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=drone_Battery_strategy)
def test_drone_battery_rechargeTime_setter(instance):
    original = instance.rechargeTime
    instance.rechargeTime = original
    assert instance.rechargeTime == original



@given(instance=drone_Battery_strategy)
def test_drone_battery_voltage_setter(instance):
    original = instance.voltage
    instance.voltage = original
    assert instance.voltage == original



@given(instance=drone_Battery_strategy)
def test_drone_battery_cellType_setter(instance):
    original = instance.cellType
    instance.cellType = original
    assert instance.cellType == original

@given(instance=drone_Property_strategy)
@settings(max_examples=50)
def test_drone_property_instantiation(instance):
    assert isinstance(instance, drone_Property)



@given(instance=drone_Property_strategy)
def test_drone_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=drone_Action_strategy)
@settings(max_examples=50)
def test_drone_action_instantiation(instance):
    assert isinstance(instance, drone_Action)

@given(instance=drone_ROSDriver_strategy)
@settings(max_examples=50)
def test_drone_rosdriver_instantiation(instance):
    assert isinstance(instance, drone_ROSDriver)



@given(instance=drone_ROSDriver_strategy)
def test_drone_rosdriver_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=drone_ROSDriver_strategy)
def test_drone_rosdriver_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=drone_Memory_strategy)
@settings(max_examples=50)
def test_drone_memory_instantiation(instance):
    assert isinstance(instance, drone_Memory)



@given(instance=drone_Memory_strategy)
def test_drone_memory_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=drone_Memory_strategy)
def test_drone_memory_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=drone_Memory_strategy)
def test_drone_memory_subType_setter(instance):
    original = instance.subType
    instance.subType = original
    assert instance.subType == original

@given(instance=drone_Drone_strategy)
@settings(max_examples=50)
def test_drone_drone_instantiation(instance):
    assert isinstance(instance, drone_Drone)



@given(instance=drone_Drone_strategy)
def test_drone_drone_maxVoltage_setter(instance):
    original = instance.maxVoltage
    instance.maxVoltage = original
    assert instance.maxVoltage == original



@given(instance=drone_Drone_strategy)
def test_drone_drone_radioFrequency_setter(instance):
    original = instance.radioFrequency
    instance.radioFrequency = original
    assert instance.radioFrequency == original



@given(instance=drone_Drone_strategy)
def test_drone_drone_barometer_setter(instance):
    original = instance.barometer
    instance.barometer = original
    assert instance.barometer == original



@given(instance=drone_Drone_strategy)
def test_drone_drone_minVoltage_setter(instance):
    original = instance.minVoltage
    instance.minVoltage = original
    assert instance.minVoltage == original



@given(instance=drone_Drone_strategy)
def test_drone_drone_maxPowerConsumption_setter(instance):
    original = instance.maxPowerConsumption
    instance.maxPowerConsumption = original
    assert instance.maxPowerConsumption == original



@given(instance=drone_Drone_strategy)
def test_drone_drone_magnetometer_setter(instance):
    original = instance.magnetometer
    instance.magnetometer = original
    assert instance.magnetometer == original



@given(instance=drone_Drone_strategy)
def test_drone_drone_onBoardObstacleAvoidance_setter(instance):
    original = instance.onBoardObstacleAvoidance
    instance.onBoardObstacleAvoidance = original
    assert instance.onBoardObstacleAvoidance == original



@given(instance=drone_Drone_strategy)
def test_drone_drone_gps_setter(instance):
    original = instance.gps
    instance.gps = original
    assert instance.gps == original



@given(instance=drone_Drone_strategy)
def test_drone_drone_accelerometer_setter(instance):
    original = instance.accelerometer
    instance.accelerometer = original
    assert instance.accelerometer == original



@given(instance=drone_Drone_strategy)
def test_drone_drone_dataRate_setter(instance):
    original = instance.dataRate
    instance.dataRate = original
    assert instance.dataRate == original



@given(instance=drone_Drone_strategy)
def test_drone_drone_giro_setter(instance):
    original = instance.giro
    instance.giro = original
    assert instance.giro == original



@given(instance=drone_Drone_strategy)
def test_drone_drone_communicationRange_setter(instance):
    original = instance.communicationRange
    instance.communicationRange = original
    assert instance.communicationRange == original

@given(instance=drone_Processor_strategy)
@settings(max_examples=50)
def test_drone_processor_instantiation(instance):
    assert isinstance(instance, drone_Processor)



@given(instance=drone_Processor_strategy)
def test_drone_processor_architecture_setter(instance):
    original = instance.architecture
    instance.architecture = original
    assert instance.architecture == original



@given(instance=drone_Processor_strategy)
def test_drone_processor_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original

@given(instance=drone_NamedElement_strategy)
@settings(max_examples=50)
def test_drone_namedelement_instantiation(instance):
    assert isinstance(instance, drone_NamedElement)



@given(instance=drone_NamedElement_strategy)
def test_drone_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
