import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    drone::Parameter,
    drone::FlightPerformance,
    drone::Size,
    NamedElement,
    drone::Property,
    drone::Action,
    drone::Device,
    drone::Battery,
    drone::ROSDriver,
    drone::Memory,
    drone::Drone,
    drone::Processor,
    drone::NamedElement,
    MemoryType,
    LaunchType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_drone::parameter_is_not_abstract():
    assert not inspect.isabstract(drone::Parameter)


def test_drone::parameter_constructor_exists():
    assert callable(drone::Parameter.__init__)


def test_drone::parameter_constructor_args():
    sig = inspect.signature(drone::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "key" in params, "Missing parameter 'key'"

def test_drone::parameter_has_description():
    assert hasattr(drone::Parameter, "description")
    descriptor = None
    for klass in drone::Parameter.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_drone::parameter_has_key():
    assert hasattr(drone::Parameter, "key")
    descriptor = None
    for klass in drone::Parameter.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_drone::flightperformance_is_not_abstract():
    assert not inspect.isabstract(drone::FlightPerformance)


def test_drone::flightperformance_constructor_exists():
    assert callable(drone::FlightPerformance.__init__)


def test_drone::flightperformance_constructor_args():
    sig = inspect.signature(drone::FlightPerformance.__init__)
    params = list(sig.parameters.keys())
    assert "minOperatingTemperature" in params, "Missing parameter 'minOperatingTemperature'"
    assert "maxFlightTimeWithMaxPayload" in params, "Missing parameter 'maxFlightTimeWithMaxPayload'"
    assert "maxSpeed" in params, "Missing parameter 'maxSpeed'"
    assert "maxAltitude" in params, "Missing parameter 'maxAltitude'"
    assert "minAcceleration" in params, "Missing parameter 'minAcceleration'"
    assert "maxDescendRate" in params, "Missing parameter 'maxDescendRate'"
    assert "minTurnRate" in params, "Missing parameter 'minTurnRate'"
    assert "maxClimbRate" in params, "Missing parameter 'maxClimbRate'"
    assert "launchType" in params, "Missing parameter 'launchType'"
    assert "maxPayload" in params, "Missing parameter 'maxPayload'"
    assert "maxAcceleration" in params, "Missing parameter 'maxAcceleration'"
    assert "positionHold" in params, "Missing parameter 'positionHold'"
    assert "maxOperatingTemperature" in params, "Missing parameter 'maxOperatingTemperature'"
    assert "maxFlightTime" in params, "Missing parameter 'maxFlightTime'"
    assert "minSpeed" in params, "Missing parameter 'minSpeed'"
    assert "maxTurnRate" in params, "Missing parameter 'maxTurnRate'"

def test_drone::flightperformance_has_minOperatingTemperature():
    assert hasattr(drone::FlightPerformance, "minOperatingTemperature")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "minOperatingTemperature" in klass.__dict__:
            descriptor = klass.__dict__["minOperatingTemperature"]
            break
    assert isinstance(descriptor, property)

def test_drone::flightperformance_has_maxFlightTimeWithMaxPayload():
    assert hasattr(drone::FlightPerformance, "maxFlightTimeWithMaxPayload")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "maxFlightTimeWithMaxPayload" in klass.__dict__:
            descriptor = klass.__dict__["maxFlightTimeWithMaxPayload"]
            break
    assert isinstance(descriptor, property)

def test_drone::flightperformance_has_maxSpeed():
    assert hasattr(drone::FlightPerformance, "maxSpeed")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "maxSpeed" in klass.__dict__:
            descriptor = klass.__dict__["maxSpeed"]
            break
    assert isinstance(descriptor, property)

def test_drone::flightperformance_has_maxAltitude():
    assert hasattr(drone::FlightPerformance, "maxAltitude")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "maxAltitude" in klass.__dict__:
            descriptor = klass.__dict__["maxAltitude"]
            break
    assert isinstance(descriptor, property)

def test_drone::flightperformance_has_minAcceleration():
    assert hasattr(drone::FlightPerformance, "minAcceleration")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "minAcceleration" in klass.__dict__:
            descriptor = klass.__dict__["minAcceleration"]
            break
    assert isinstance(descriptor, property)

def test_drone::flightperformance_has_maxDescendRate():
    assert hasattr(drone::FlightPerformance, "maxDescendRate")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "maxDescendRate" in klass.__dict__:
            descriptor = klass.__dict__["maxDescendRate"]
            break
    assert isinstance(descriptor, property)

def test_drone::flightperformance_has_minTurnRate():
    assert hasattr(drone::FlightPerformance, "minTurnRate")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "minTurnRate" in klass.__dict__:
            descriptor = klass.__dict__["minTurnRate"]
            break
    assert isinstance(descriptor, property)

def test_drone::flightperformance_has_maxClimbRate():
    assert hasattr(drone::FlightPerformance, "maxClimbRate")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "maxClimbRate" in klass.__dict__:
            descriptor = klass.__dict__["maxClimbRate"]
            break
    assert isinstance(descriptor, property)

def test_drone::flightperformance_has_launchType():
    assert hasattr(drone::FlightPerformance, "launchType")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "launchType" in klass.__dict__:
            descriptor = klass.__dict__["launchType"]
            break
    assert isinstance(descriptor, property)

def test_drone::flightperformance_has_maxPayload():
    assert hasattr(drone::FlightPerformance, "maxPayload")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "maxPayload" in klass.__dict__:
            descriptor = klass.__dict__["maxPayload"]
            break
    assert isinstance(descriptor, property)

def test_drone::flightperformance_has_maxAcceleration():
    assert hasattr(drone::FlightPerformance, "maxAcceleration")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "maxAcceleration" in klass.__dict__:
            descriptor = klass.__dict__["maxAcceleration"]
            break
    assert isinstance(descriptor, property)

def test_drone::flightperformance_has_positionHold():
    assert hasattr(drone::FlightPerformance, "positionHold")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "positionHold" in klass.__dict__:
            descriptor = klass.__dict__["positionHold"]
            break
    assert isinstance(descriptor, property)

def test_drone::flightperformance_has_maxOperatingTemperature():
    assert hasattr(drone::FlightPerformance, "maxOperatingTemperature")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "maxOperatingTemperature" in klass.__dict__:
            descriptor = klass.__dict__["maxOperatingTemperature"]
            break
    assert isinstance(descriptor, property)

def test_drone::flightperformance_has_maxFlightTime():
    assert hasattr(drone::FlightPerformance, "maxFlightTime")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "maxFlightTime" in klass.__dict__:
            descriptor = klass.__dict__["maxFlightTime"]
            break
    assert isinstance(descriptor, property)

def test_drone::flightperformance_has_minSpeed():
    assert hasattr(drone::FlightPerformance, "minSpeed")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "minSpeed" in klass.__dict__:
            descriptor = klass.__dict__["minSpeed"]
            break
    assert isinstance(descriptor, property)

def test_drone::flightperformance_has_maxTurnRate():
    assert hasattr(drone::FlightPerformance, "maxTurnRate")
    descriptor = None
    for klass in drone::FlightPerformance.__mro__:
        if "maxTurnRate" in klass.__dict__:
            descriptor = klass.__dict__["maxTurnRate"]
            break
    assert isinstance(descriptor, property)



def test_drone::size_is_not_abstract():
    assert not inspect.isabstract(drone::Size)


def test_drone::size_constructor_exists():
    assert callable(drone::Size.__init__)


def test_drone::size_constructor_args():
    sig = inspect.signature(drone::Size.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "length" in params, "Missing parameter 'length'"
    assert "width" in params, "Missing parameter 'width'"
    assert "propellers" in params, "Missing parameter 'propellers'"
    assert "propellerSize" in params, "Missing parameter 'propellerSize'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_drone::size_has_height():
    assert hasattr(drone::Size, "height")
    descriptor = None
    for klass in drone::Size.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_drone::size_has_length():
    assert hasattr(drone::Size, "length")
    descriptor = None
    for klass in drone::Size.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_drone::size_has_width():
    assert hasattr(drone::Size, "width")
    descriptor = None
    for klass in drone::Size.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_drone::size_has_propellers():
    assert hasattr(drone::Size, "propellers")
    descriptor = None
    for klass in drone::Size.__mro__:
        if "propellers" in klass.__dict__:
            descriptor = klass.__dict__["propellers"]
            break
    assert isinstance(descriptor, property)

def test_drone::size_has_propellerSize():
    assert hasattr(drone::Size, "propellerSize")
    descriptor = None
    for klass in drone::Size.__mro__:
        if "propellerSize" in klass.__dict__:
            descriptor = klass.__dict__["propellerSize"]
            break
    assert isinstance(descriptor, property)

def test_drone::size_has_weight():
    assert hasattr(drone::Size, "weight")
    descriptor = None
    for klass in drone::Size.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_drone::property_is_not_abstract():
    assert not inspect.isabstract(drone::Property)


def test_drone::property_constructor_exists():
    assert callable(drone::Property.__init__)


def test_drone::property_constructor_args():
    sig = inspect.signature(drone::Property.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_drone::property_has_value():
    assert hasattr(drone::Property, "value")
    descriptor = None
    for klass in drone::Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_drone::action_is_not_abstract():
    assert not inspect.isabstract(drone::Action)


def test_drone::action_constructor_exists():
    assert callable(drone::Action.__init__)


def test_drone::action_constructor_args():
    sig = inspect.signature(drone::Action.__init__)
    params = list(sig.parameters.keys())



def test_drone::device_is_not_abstract():
    assert not inspect.isabstract(drone::Device)


def test_drone::device_constructor_exists():
    assert callable(drone::Device.__init__)


def test_drone::device_constructor_args():
    sig = inspect.signature(drone::Device.__init__)
    params = list(sig.parameters.keys())



def test_drone::battery_is_not_abstract():
    assert not inspect.isabstract(drone::Battery)


def test_drone::battery_constructor_exists():
    assert callable(drone::Battery.__init__)


def test_drone::battery_constructor_args():
    sig = inspect.signature(drone::Battery.__init__)
    params = list(sig.parameters.keys())
    assert "voltage" in params, "Missing parameter 'voltage'"
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "rechargeTime" in params, "Missing parameter 'rechargeTime'"
    assert "cellType" in params, "Missing parameter 'cellType'"

def test_drone::battery_has_voltage():
    assert hasattr(drone::Battery, "voltage")
    descriptor = None
    for klass in drone::Battery.__mro__:
        if "voltage" in klass.__dict__:
            descriptor = klass.__dict__["voltage"]
            break
    assert isinstance(descriptor, property)

def test_drone::battery_has_capacity():
    assert hasattr(drone::Battery, "capacity")
    descriptor = None
    for klass in drone::Battery.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_drone::battery_has_rechargeTime():
    assert hasattr(drone::Battery, "rechargeTime")
    descriptor = None
    for klass in drone::Battery.__mro__:
        if "rechargeTime" in klass.__dict__:
            descriptor = klass.__dict__["rechargeTime"]
            break
    assert isinstance(descriptor, property)

def test_drone::battery_has_cellType():
    assert hasattr(drone::Battery, "cellType")
    descriptor = None
    for klass in drone::Battery.__mro__:
        if "cellType" in klass.__dict__:
            descriptor = klass.__dict__["cellType"]
            break
    assert isinstance(descriptor, property)



def test_drone::rosdriver_is_not_abstract():
    assert not inspect.isabstract(drone::ROSDriver)


def test_drone::rosdriver_constructor_exists():
    assert callable(drone::ROSDriver.__init__)


def test_drone::rosdriver_constructor_args():
    sig = inspect.signature(drone::ROSDriver.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "version" in params, "Missing parameter 'version'"

def test_drone::rosdriver_has_url():
    assert hasattr(drone::ROSDriver, "url")
    descriptor = None
    for klass in drone::ROSDriver.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_drone::rosdriver_has_version():
    assert hasattr(drone::ROSDriver, "version")
    descriptor = None
    for klass in drone::ROSDriver.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_drone::memory_is_not_abstract():
    assert not inspect.isabstract(drone::Memory)


def test_drone::memory_constructor_exists():
    assert callable(drone::Memory.__init__)


def test_drone::memory_constructor_args():
    sig = inspect.signature(drone::Memory.__init__)
    params = list(sig.parameters.keys())
    assert "subType" in params, "Missing parameter 'subType'"
    assert "size" in params, "Missing parameter 'size'"
    assert "type" in params, "Missing parameter 'type'"

def test_drone::memory_has_subType():
    assert hasattr(drone::Memory, "subType")
    descriptor = None
    for klass in drone::Memory.__mro__:
        if "subType" in klass.__dict__:
            descriptor = klass.__dict__["subType"]
            break
    assert isinstance(descriptor, property)

def test_drone::memory_has_size():
    assert hasattr(drone::Memory, "size")
    descriptor = None
    for klass in drone::Memory.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_drone::memory_has_type():
    assert hasattr(drone::Memory, "type")
    descriptor = None
    for klass in drone::Memory.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_drone::drone_is_not_abstract():
    assert not inspect.isabstract(drone::Drone)


def test_drone::drone_constructor_exists():
    assert callable(drone::Drone.__init__)


def test_drone::drone_constructor_args():
    sig = inspect.signature(drone::Drone.__init__)
    params = list(sig.parameters.keys())
    assert "radioFrequency" in params, "Missing parameter 'radioFrequency'"
    assert "communicationRange" in params, "Missing parameter 'communicationRange'"
    assert "minVoltage" in params, "Missing parameter 'minVoltage'"
    assert "dataRate" in params, "Missing parameter 'dataRate'"
    assert "onBoardObstacleAvoidance" in params, "Missing parameter 'onBoardObstacleAvoidance'"
    assert "maxVoltage" in params, "Missing parameter 'maxVoltage'"
    assert "magnetometer" in params, "Missing parameter 'magnetometer'"
    assert "giro" in params, "Missing parameter 'giro'"
    assert "maxPowerConsumption" in params, "Missing parameter 'maxPowerConsumption'"
    assert "accelerometer" in params, "Missing parameter 'accelerometer'"
    assert "barometer" in params, "Missing parameter 'barometer'"
    assert "gps" in params, "Missing parameter 'gps'"

def test_drone::drone_has_radioFrequency():
    assert hasattr(drone::Drone, "radioFrequency")
    descriptor = None
    for klass in drone::Drone.__mro__:
        if "radioFrequency" in klass.__dict__:
            descriptor = klass.__dict__["radioFrequency"]
            break
    assert isinstance(descriptor, property)

def test_drone::drone_has_communicationRange():
    assert hasattr(drone::Drone, "communicationRange")
    descriptor = None
    for klass in drone::Drone.__mro__:
        if "communicationRange" in klass.__dict__:
            descriptor = klass.__dict__["communicationRange"]
            break
    assert isinstance(descriptor, property)

def test_drone::drone_has_minVoltage():
    assert hasattr(drone::Drone, "minVoltage")
    descriptor = None
    for klass in drone::Drone.__mro__:
        if "minVoltage" in klass.__dict__:
            descriptor = klass.__dict__["minVoltage"]
            break
    assert isinstance(descriptor, property)

def test_drone::drone_has_dataRate():
    assert hasattr(drone::Drone, "dataRate")
    descriptor = None
    for klass in drone::Drone.__mro__:
        if "dataRate" in klass.__dict__:
            descriptor = klass.__dict__["dataRate"]
            break
    assert isinstance(descriptor, property)

def test_drone::drone_has_onBoardObstacleAvoidance():
    assert hasattr(drone::Drone, "onBoardObstacleAvoidance")
    descriptor = None
    for klass in drone::Drone.__mro__:
        if "onBoardObstacleAvoidance" in klass.__dict__:
            descriptor = klass.__dict__["onBoardObstacleAvoidance"]
            break
    assert isinstance(descriptor, property)

def test_drone::drone_has_maxVoltage():
    assert hasattr(drone::Drone, "maxVoltage")
    descriptor = None
    for klass in drone::Drone.__mro__:
        if "maxVoltage" in klass.__dict__:
            descriptor = klass.__dict__["maxVoltage"]
            break
    assert isinstance(descriptor, property)

def test_drone::drone_has_magnetometer():
    assert hasattr(drone::Drone, "magnetometer")
    descriptor = None
    for klass in drone::Drone.__mro__:
        if "magnetometer" in klass.__dict__:
            descriptor = klass.__dict__["magnetometer"]
            break
    assert isinstance(descriptor, property)

def test_drone::drone_has_giro():
    assert hasattr(drone::Drone, "giro")
    descriptor = None
    for klass in drone::Drone.__mro__:
        if "giro" in klass.__dict__:
            descriptor = klass.__dict__["giro"]
            break
    assert isinstance(descriptor, property)

def test_drone::drone_has_maxPowerConsumption():
    assert hasattr(drone::Drone, "maxPowerConsumption")
    descriptor = None
    for klass in drone::Drone.__mro__:
        if "maxPowerConsumption" in klass.__dict__:
            descriptor = klass.__dict__["maxPowerConsumption"]
            break
    assert isinstance(descriptor, property)

def test_drone::drone_has_accelerometer():
    assert hasattr(drone::Drone, "accelerometer")
    descriptor = None
    for klass in drone::Drone.__mro__:
        if "accelerometer" in klass.__dict__:
            descriptor = klass.__dict__["accelerometer"]
            break
    assert isinstance(descriptor, property)

def test_drone::drone_has_barometer():
    assert hasattr(drone::Drone, "barometer")
    descriptor = None
    for klass in drone::Drone.__mro__:
        if "barometer" in klass.__dict__:
            descriptor = klass.__dict__["barometer"]
            break
    assert isinstance(descriptor, property)

def test_drone::drone_has_gps():
    assert hasattr(drone::Drone, "gps")
    descriptor = None
    for klass in drone::Drone.__mro__:
        if "gps" in klass.__dict__:
            descriptor = klass.__dict__["gps"]
            break
    assert isinstance(descriptor, property)



def test_drone::processor_is_not_abstract():
    assert not inspect.isabstract(drone::Processor)


def test_drone::processor_constructor_exists():
    assert callable(drone::Processor.__init__)


def test_drone::processor_constructor_args():
    sig = inspect.signature(drone::Processor.__init__)
    params = list(sig.parameters.keys())
    assert "architecture" in params, "Missing parameter 'architecture'"
    assert "frequency" in params, "Missing parameter 'frequency'"

def test_drone::processor_has_architecture():
    assert hasattr(drone::Processor, "architecture")
    descriptor = None
    for klass in drone::Processor.__mro__:
        if "architecture" in klass.__dict__:
            descriptor = klass.__dict__["architecture"]
            break
    assert isinstance(descriptor, property)

def test_drone::processor_has_frequency():
    assert hasattr(drone::Processor, "frequency")
    descriptor = None
    for klass in drone::Processor.__mro__:
        if "frequency" in klass.__dict__:
            descriptor = klass.__dict__["frequency"]
            break
    assert isinstance(descriptor, property)



def test_drone::namedelement_is_not_abstract():
    assert not inspect.isabstract(drone::NamedElement)


def test_drone::namedelement_constructor_exists():
    assert callable(drone::NamedElement.__init__)


def test_drone::namedelement_constructor_args():
    sig = inspect.signature(drone::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_drone::namedelement_has_name():
    assert hasattr(drone::NamedElement, "name")
    descriptor = None
    for klass in drone::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

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

def test_launchtype_exists():
    # Check that the Enumeration exists
    assert LaunchType is not None

def test_launchtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LaunchType]
    expected_literals = [
        "VTOL",
        "OTHER",
        "HTOL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LaunchType"


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
drone::Parameter_strategy = st.builds(
    drone::Parameter,
    description=
        safe_text,
    key=
        safe_text
)
drone::FlightPerformance_strategy = st.builds(
    drone::FlightPerformance,
    minOperatingTemperature=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maxFlightTimeWithMaxPayload=
        st.integers(),
    maxSpeed=
        st.integers(),
    maxAltitude=
        st.integers(),
    minAcceleration=
        st.integers(),
    maxDescendRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minTurnRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maxClimbRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    launchType=
        safe_text,
    maxPayload=
        st.integers(),
    maxAcceleration=
        st.integers(),
    positionHold=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maxOperatingTemperature=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maxFlightTime=
        st.integers(),
    minSpeed=
        st.integers(),
    maxTurnRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
drone::Size_strategy = st.builds(
    drone::Size,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    propellers=
        st.integers(),
    propellerSize=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
NamedElement_strategy = st.builds(
    NamedElement,
)
drone::Property_strategy = st.builds(
    drone::Property,
    value=
        safe_text
)
drone::Action_strategy = st.builds(
    drone::Action,
)
drone::Device_strategy = st.builds(
    drone::Device,
)
drone::Battery_strategy = st.builds(
    drone::Battery,
    voltage=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    capacity=
        st.integers(),
    rechargeTime=
        st.integers(),
    cellType=
        safe_text
)
drone::ROSDriver_strategy = st.builds(
    drone::ROSDriver,
    url=
        safe_text,
    version=
        safe_text
)
drone::Memory_strategy = st.builds(
    drone::Memory,
    subType=
        safe_text,
    size=
        st.integers(),
    type=
        safe_text
)
drone::Drone_strategy = st.builds(
    drone::Drone,
    radioFrequency=
        st.integers(),
    communicationRange=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minVoltage=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    dataRate=
        st.integers(),
    onBoardObstacleAvoidance=
        st.booleans(),
    maxVoltage=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    magnetometer=
        st.booleans(),
    giro=
        st.booleans(),
    maxPowerConsumption=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    accelerometer=
        st.booleans(),
    barometer=
        st.booleans(),
    gps=
        st.booleans()
)
drone::Processor_strategy = st.builds(
    drone::Processor,
    architecture=
        safe_text,
    frequency=
        st.integers()
)
drone::NamedElement_strategy = st.builds(
    drone::NamedElement,
    name=
        safe_text
)

@given(instance=drone::Parameter_strategy)
@settings(max_examples=50)
def test_drone::parameter_instantiation(instance):
    assert isinstance(instance, drone::Parameter)

@given(instance=drone::Parameter_strategy)
def test_drone::parameter_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=drone::Parameter_strategy)
def test_drone::parameter_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=drone::Parameter_strategy)
def test_drone::parameter_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=drone::Parameter_strategy)
def test_drone::parameter_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=drone::FlightPerformance_strategy)
@settings(max_examples=50)
def test_drone::flightperformance_instantiation(instance):
    assert isinstance(instance, drone::FlightPerformance)

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_minOperatingTemperature_type(instance):
    assert isinstance(instance.minOperatingTemperature, float)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_minOperatingTemperature_setter(instance):
    original = instance.minOperatingTemperature
    instance.minOperatingTemperature = original
    assert instance.minOperatingTemperature == original

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxFlightTimeWithMaxPayload_type(instance):
    assert isinstance(instance.maxFlightTimeWithMaxPayload, int)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxFlightTimeWithMaxPayload_setter(instance):
    original = instance.maxFlightTimeWithMaxPayload
    instance.maxFlightTimeWithMaxPayload = original
    assert instance.maxFlightTimeWithMaxPayload == original

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxSpeed_type(instance):
    assert isinstance(instance.maxSpeed, int)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxSpeed_setter(instance):
    original = instance.maxSpeed
    instance.maxSpeed = original
    assert instance.maxSpeed == original

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxAltitude_type(instance):
    assert isinstance(instance.maxAltitude, int)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxAltitude_setter(instance):
    original = instance.maxAltitude
    instance.maxAltitude = original
    assert instance.maxAltitude == original

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_minAcceleration_type(instance):
    assert isinstance(instance.minAcceleration, int)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_minAcceleration_setter(instance):
    original = instance.minAcceleration
    instance.minAcceleration = original
    assert instance.minAcceleration == original

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxDescendRate_type(instance):
    assert isinstance(instance.maxDescendRate, float)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxDescendRate_setter(instance):
    original = instance.maxDescendRate
    instance.maxDescendRate = original
    assert instance.maxDescendRate == original

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_minTurnRate_type(instance):
    assert isinstance(instance.minTurnRate, float)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_minTurnRate_setter(instance):
    original = instance.minTurnRate
    instance.minTurnRate = original
    assert instance.minTurnRate == original

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxClimbRate_type(instance):
    assert isinstance(instance.maxClimbRate, float)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxClimbRate_setter(instance):
    original = instance.maxClimbRate
    instance.maxClimbRate = original
    assert instance.maxClimbRate == original

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_launchType_type(instance):
    assert isinstance(instance.launchType, str)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_launchType_setter(instance):
    original = instance.launchType
    instance.launchType = original
    assert instance.launchType == original

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxPayload_type(instance):
    assert isinstance(instance.maxPayload, int)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxPayload_setter(instance):
    original = instance.maxPayload
    instance.maxPayload = original
    assert instance.maxPayload == original

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxAcceleration_type(instance):
    assert isinstance(instance.maxAcceleration, int)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxAcceleration_setter(instance):
    original = instance.maxAcceleration
    instance.maxAcceleration = original
    assert instance.maxAcceleration == original

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_positionHold_type(instance):
    assert isinstance(instance.positionHold, float)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_positionHold_setter(instance):
    original = instance.positionHold
    instance.positionHold = original
    assert instance.positionHold == original

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxOperatingTemperature_type(instance):
    assert isinstance(instance.maxOperatingTemperature, float)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxOperatingTemperature_setter(instance):
    original = instance.maxOperatingTemperature
    instance.maxOperatingTemperature = original
    assert instance.maxOperatingTemperature == original

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxFlightTime_type(instance):
    assert isinstance(instance.maxFlightTime, int)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxFlightTime_setter(instance):
    original = instance.maxFlightTime
    instance.maxFlightTime = original
    assert instance.maxFlightTime == original

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_minSpeed_type(instance):
    assert isinstance(instance.minSpeed, int)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_minSpeed_setter(instance):
    original = instance.minSpeed
    instance.minSpeed = original
    assert instance.minSpeed == original

@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxTurnRate_type(instance):
    assert isinstance(instance.maxTurnRate, float)


@given(instance=drone::FlightPerformance_strategy)
def test_drone::flightperformance_maxTurnRate_setter(instance):
    original = instance.maxTurnRate
    instance.maxTurnRate = original
    assert instance.maxTurnRate == original

@given(instance=drone::Size_strategy)
@settings(max_examples=50)
def test_drone::size_instantiation(instance):
    assert isinstance(instance, drone::Size)

@given(instance=drone::Size_strategy)
def test_drone::size_height_type(instance):
    assert isinstance(instance.height, float)


@given(instance=drone::Size_strategy)
def test_drone::size_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=drone::Size_strategy)
def test_drone::size_length_type(instance):
    assert isinstance(instance.length, float)


@given(instance=drone::Size_strategy)
def test_drone::size_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=drone::Size_strategy)
def test_drone::size_width_type(instance):
    assert isinstance(instance.width, float)


@given(instance=drone::Size_strategy)
def test_drone::size_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=drone::Size_strategy)
def test_drone::size_propellers_type(instance):
    assert isinstance(instance.propellers, int)


@given(instance=drone::Size_strategy)
def test_drone::size_propellers_setter(instance):
    original = instance.propellers
    instance.propellers = original
    assert instance.propellers == original

@given(instance=drone::Size_strategy)
def test_drone::size_propellerSize_type(instance):
    assert isinstance(instance.propellerSize, float)


@given(instance=drone::Size_strategy)
def test_drone::size_propellerSize_setter(instance):
    original = instance.propellerSize
    instance.propellerSize = original
    assert instance.propellerSize == original

@given(instance=drone::Size_strategy)
def test_drone::size_weight_type(instance):
    assert isinstance(instance.weight, float)


@given(instance=drone::Size_strategy)
def test_drone::size_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=drone::Property_strategy)
@settings(max_examples=50)
def test_drone::property_instantiation(instance):
    assert isinstance(instance, drone::Property)

@given(instance=drone::Property_strategy)
def test_drone::property_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=drone::Property_strategy)
def test_drone::property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=drone::Action_strategy)
@settings(max_examples=50)
def test_drone::action_instantiation(instance):
    assert isinstance(instance, drone::Action)

@given(instance=drone::Device_strategy)
@settings(max_examples=50)
def test_drone::device_instantiation(instance):
    assert isinstance(instance, drone::Device)

@given(instance=drone::Battery_strategy)
@settings(max_examples=50)
def test_drone::battery_instantiation(instance):
    assert isinstance(instance, drone::Battery)

@given(instance=drone::Battery_strategy)
def test_drone::battery_voltage_type(instance):
    assert isinstance(instance.voltage, float)


@given(instance=drone::Battery_strategy)
def test_drone::battery_voltage_setter(instance):
    original = instance.voltage
    instance.voltage = original
    assert instance.voltage == original

@given(instance=drone::Battery_strategy)
def test_drone::battery_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=drone::Battery_strategy)
def test_drone::battery_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=drone::Battery_strategy)
def test_drone::battery_rechargeTime_type(instance):
    assert isinstance(instance.rechargeTime, int)


@given(instance=drone::Battery_strategy)
def test_drone::battery_rechargeTime_setter(instance):
    original = instance.rechargeTime
    instance.rechargeTime = original
    assert instance.rechargeTime == original

@given(instance=drone::Battery_strategy)
def test_drone::battery_cellType_type(instance):
    assert isinstance(instance.cellType, str)


@given(instance=drone::Battery_strategy)
def test_drone::battery_cellType_setter(instance):
    original = instance.cellType
    instance.cellType = original
    assert instance.cellType == original

@given(instance=drone::ROSDriver_strategy)
@settings(max_examples=50)
def test_drone::rosdriver_instantiation(instance):
    assert isinstance(instance, drone::ROSDriver)

@given(instance=drone::ROSDriver_strategy)
def test_drone::rosdriver_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=drone::ROSDriver_strategy)
def test_drone::rosdriver_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=drone::ROSDriver_strategy)
def test_drone::rosdriver_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=drone::ROSDriver_strategy)
def test_drone::rosdriver_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=drone::Memory_strategy)
@settings(max_examples=50)
def test_drone::memory_instantiation(instance):
    assert isinstance(instance, drone::Memory)

@given(instance=drone::Memory_strategy)
def test_drone::memory_subType_type(instance):
    assert isinstance(instance.subType, str)


@given(instance=drone::Memory_strategy)
def test_drone::memory_subType_setter(instance):
    original = instance.subType
    instance.subType = original
    assert instance.subType == original

@given(instance=drone::Memory_strategy)
def test_drone::memory_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=drone::Memory_strategy)
def test_drone::memory_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=drone::Memory_strategy)
def test_drone::memory_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=drone::Memory_strategy)
def test_drone::memory_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=drone::Drone_strategy)
@settings(max_examples=50)
def test_drone::drone_instantiation(instance):
    assert isinstance(instance, drone::Drone)

@given(instance=drone::Drone_strategy)
def test_drone::drone_radioFrequency_type(instance):
    assert isinstance(instance.radioFrequency, int)


@given(instance=drone::Drone_strategy)
def test_drone::drone_radioFrequency_setter(instance):
    original = instance.radioFrequency
    instance.radioFrequency = original
    assert instance.radioFrequency == original

@given(instance=drone::Drone_strategy)
def test_drone::drone_communicationRange_type(instance):
    assert isinstance(instance.communicationRange, float)


@given(instance=drone::Drone_strategy)
def test_drone::drone_communicationRange_setter(instance):
    original = instance.communicationRange
    instance.communicationRange = original
    assert instance.communicationRange == original

@given(instance=drone::Drone_strategy)
def test_drone::drone_minVoltage_type(instance):
    assert isinstance(instance.minVoltage, float)


@given(instance=drone::Drone_strategy)
def test_drone::drone_minVoltage_setter(instance):
    original = instance.minVoltage
    instance.minVoltage = original
    assert instance.minVoltage == original

@given(instance=drone::Drone_strategy)
def test_drone::drone_dataRate_type(instance):
    assert isinstance(instance.dataRate, int)


@given(instance=drone::Drone_strategy)
def test_drone::drone_dataRate_setter(instance):
    original = instance.dataRate
    instance.dataRate = original
    assert instance.dataRate == original

@given(instance=drone::Drone_strategy)
def test_drone::drone_onBoardObstacleAvoidance_type(instance):
    assert isinstance(instance.onBoardObstacleAvoidance, bool)


@given(instance=drone::Drone_strategy)
def test_drone::drone_onBoardObstacleAvoidance_setter(instance):
    original = instance.onBoardObstacleAvoidance
    instance.onBoardObstacleAvoidance = original
    assert instance.onBoardObstacleAvoidance == original

@given(instance=drone::Drone_strategy)
def test_drone::drone_maxVoltage_type(instance):
    assert isinstance(instance.maxVoltage, float)


@given(instance=drone::Drone_strategy)
def test_drone::drone_maxVoltage_setter(instance):
    original = instance.maxVoltage
    instance.maxVoltage = original
    assert instance.maxVoltage == original

@given(instance=drone::Drone_strategy)
def test_drone::drone_magnetometer_type(instance):
    assert isinstance(instance.magnetometer, bool)


@given(instance=drone::Drone_strategy)
def test_drone::drone_magnetometer_setter(instance):
    original = instance.magnetometer
    instance.magnetometer = original
    assert instance.magnetometer == original

@given(instance=drone::Drone_strategy)
def test_drone::drone_giro_type(instance):
    assert isinstance(instance.giro, bool)


@given(instance=drone::Drone_strategy)
def test_drone::drone_giro_setter(instance):
    original = instance.giro
    instance.giro = original
    assert instance.giro == original

@given(instance=drone::Drone_strategy)
def test_drone::drone_maxPowerConsumption_type(instance):
    assert isinstance(instance.maxPowerConsumption, float)


@given(instance=drone::Drone_strategy)
def test_drone::drone_maxPowerConsumption_setter(instance):
    original = instance.maxPowerConsumption
    instance.maxPowerConsumption = original
    assert instance.maxPowerConsumption == original

@given(instance=drone::Drone_strategy)
def test_drone::drone_accelerometer_type(instance):
    assert isinstance(instance.accelerometer, bool)


@given(instance=drone::Drone_strategy)
def test_drone::drone_accelerometer_setter(instance):
    original = instance.accelerometer
    instance.accelerometer = original
    assert instance.accelerometer == original

@given(instance=drone::Drone_strategy)
def test_drone::drone_barometer_type(instance):
    assert isinstance(instance.barometer, bool)


@given(instance=drone::Drone_strategy)
def test_drone::drone_barometer_setter(instance):
    original = instance.barometer
    instance.barometer = original
    assert instance.barometer == original

@given(instance=drone::Drone_strategy)
def test_drone::drone_gps_type(instance):
    assert isinstance(instance.gps, bool)


@given(instance=drone::Drone_strategy)
def test_drone::drone_gps_setter(instance):
    original = instance.gps
    instance.gps = original
    assert instance.gps == original

@given(instance=drone::Processor_strategy)
@settings(max_examples=50)
def test_drone::processor_instantiation(instance):
    assert isinstance(instance, drone::Processor)

@given(instance=drone::Processor_strategy)
def test_drone::processor_architecture_type(instance):
    assert isinstance(instance.architecture, str)


@given(instance=drone::Processor_strategy)
def test_drone::processor_architecture_setter(instance):
    original = instance.architecture
    instance.architecture = original
    assert instance.architecture == original

@given(instance=drone::Processor_strategy)
def test_drone::processor_frequency_type(instance):
    assert isinstance(instance.frequency, int)


@given(instance=drone::Processor_strategy)
def test_drone::processor_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original

@given(instance=drone::NamedElement_strategy)
@settings(max_examples=50)
def test_drone::namedelement_instantiation(instance):
    assert isinstance(instance, drone::NamedElement)

@given(instance=drone::NamedElement_strategy)
def test_drone::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=drone::NamedElement_strategy)
def test_drone::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
