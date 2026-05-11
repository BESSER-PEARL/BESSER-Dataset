import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    smarthome::Mode,
    smarthome::Duration,
    smarthome::Predicate,
    smarthome::Rule,
    smarthome::CSVSensor,
    Predicate,
    smarthome::PersonPredicate,
    smarthome::SensorPredicate,
    smarthome::Home,
    Sensor,
    smarthome::DigitalSensor,
    smarthome::AnalogSensor,
    NamedEntity,
    smarthome::Tag,
    smarthome::Room,
    smarthome::Person,
    smarthome::Sensor,
    smarthome::NamedEntity,
    smarthome::Pattern,
    Precision,
    Activity,
    Operator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smarthome::mode_is_not_abstract():
    assert not inspect.isabstract(smarthome::Mode)


def test_smarthome::mode_constructor_exists():
    assert callable(smarthome::Mode.__init__)


def test_smarthome::mode_constructor_args():
    sig = inspect.signature(smarthome::Mode.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::duration_is_not_abstract():
    assert not inspect.isabstract(smarthome::Duration)


def test_smarthome::duration_constructor_exists():
    assert callable(smarthome::Duration.__init__)


def test_smarthome::duration_constructor_args():
    sig = inspect.signature(smarthome::Duration.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_smarthome::duration_has_time():
    assert hasattr(smarthome::Duration, "time")
    descriptor = None
    for klass in smarthome::Duration.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_smarthome::duration_has_precision():
    assert hasattr(smarthome::Duration, "precision")
    descriptor = None
    for klass in smarthome::Duration.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_smarthome::predicate_is_not_abstract():
    assert not inspect.isabstract(smarthome::Predicate)


def test_smarthome::predicate_constructor_exists():
    assert callable(smarthome::Predicate.__init__)


def test_smarthome::predicate_constructor_args():
    sig = inspect.signature(smarthome::Predicate.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::rule_is_not_abstract():
    assert not inspect.isabstract(smarthome::Rule)


def test_smarthome::rule_constructor_exists():
    assert callable(smarthome::Rule.__init__)


def test_smarthome::rule_constructor_args():
    sig = inspect.signature(smarthome::Rule.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::csvsensor_is_not_abstract():
    assert not inspect.isabstract(smarthome::CSVSensor)


def test_smarthome::csvsensor_constructor_exists():
    assert callable(smarthome::CSVSensor.__init__)


def test_smarthome::csvsensor_constructor_args():
    sig = inspect.signature(smarthome::CSVSensor.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_smarthome::csvsensor_has_file():
    assert hasattr(smarthome::CSVSensor, "file")
    descriptor = None
    for klass in smarthome::CSVSensor.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::personpredicate_is_not_abstract():
    assert not inspect.isabstract(smarthome::PersonPredicate)


def test_smarthome::personpredicate_constructor_exists():
    assert callable(smarthome::PersonPredicate.__init__)


def test_smarthome::personpredicate_constructor_args():
    sig = inspect.signature(smarthome::PersonPredicate.__init__)
    params = list(sig.parameters.keys())
    assert "activity" in params, "Missing parameter 'activity'"

def test_smarthome::personpredicate_has_activity():
    assert hasattr(smarthome::PersonPredicate, "activity")
    descriptor = None
    for klass in smarthome::PersonPredicate.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)



def test_smarthome::sensorpredicate_is_not_abstract():
    assert not inspect.isabstract(smarthome::SensorPredicate)


def test_smarthome::sensorpredicate_constructor_exists():
    assert callable(smarthome::SensorPredicate.__init__)


def test_smarthome::sensorpredicate_constructor_args():
    sig = inspect.signature(smarthome::SensorPredicate.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "value" in params, "Missing parameter 'value'"

def test_smarthome::sensorpredicate_has_operator():
    assert hasattr(smarthome::SensorPredicate, "operator")
    descriptor = None
    for klass in smarthome::SensorPredicate.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_smarthome::sensorpredicate_has_value():
    assert hasattr(smarthome::SensorPredicate, "value")
    descriptor = None
    for klass in smarthome::SensorPredicate.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smarthome::home_is_not_abstract():
    assert not inspect.isabstract(smarthome::Home)


def test_smarthome::home_constructor_exists():
    assert callable(smarthome::Home.__init__)


def test_smarthome::home_constructor_args():
    sig = inspect.signature(smarthome::Home.__init__)
    params = list(sig.parameters.keys())
    assert "fileEvents" in params, "Missing parameter 'fileEvents'"

def test_smarthome::home_has_fileEvents():
    assert hasattr(smarthome::Home, "fileEvents")
    descriptor = None
    for klass in smarthome::Home.__mro__:
        if "fileEvents" in klass.__dict__:
            descriptor = klass.__dict__["fileEvents"]
            break
    assert isinstance(descriptor, property)



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::digitalsensor_is_not_abstract():
    assert not inspect.isabstract(smarthome::DigitalSensor)


def test_smarthome::digitalsensor_constructor_exists():
    assert callable(smarthome::DigitalSensor.__init__)


def test_smarthome::digitalsensor_constructor_args():
    sig = inspect.signature(smarthome::DigitalSensor.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::analogsensor_is_not_abstract():
    assert not inspect.isabstract(smarthome::AnalogSensor)


def test_smarthome::analogsensor_constructor_exists():
    assert callable(smarthome::AnalogSensor.__init__)


def test_smarthome::analogsensor_constructor_args():
    sig = inspect.signature(smarthome::AnalogSensor.__init__)
    params = list(sig.parameters.keys())



def test_namedentity_is_not_abstract():
    assert not inspect.isabstract(NamedEntity)


def test_namedentity_constructor_exists():
    assert callable(NamedEntity.__init__)


def test_namedentity_constructor_args():
    sig = inspect.signature(NamedEntity.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::tag_is_not_abstract():
    assert not inspect.isabstract(smarthome::Tag)


def test_smarthome::tag_constructor_exists():
    assert callable(smarthome::Tag.__init__)


def test_smarthome::tag_constructor_args():
    sig = inspect.signature(smarthome::Tag.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::room_is_not_abstract():
    assert not inspect.isabstract(smarthome::Room)


def test_smarthome::room_constructor_exists():
    assert callable(smarthome::Room.__init__)


def test_smarthome::room_constructor_args():
    sig = inspect.signature(smarthome::Room.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::person_is_not_abstract():
    assert not inspect.isabstract(smarthome::Person)


def test_smarthome::person_constructor_exists():
    assert callable(smarthome::Person.__init__)


def test_smarthome::person_constructor_args():
    sig = inspect.signature(smarthome::Person.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::sensor_is_not_abstract():
    assert not inspect.isabstract(smarthome::Sensor)


def test_smarthome::sensor_constructor_exists():
    assert callable(smarthome::Sensor.__init__)


def test_smarthome::sensor_constructor_args():
    sig = inspect.signature(smarthome::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_smarthome::namedentity_is_not_abstract():
    assert not inspect.isabstract(smarthome::NamedEntity)


def test_smarthome::namedentity_constructor_exists():
    assert callable(smarthome::NamedEntity.__init__)


def test_smarthome::namedentity_constructor_args():
    sig = inspect.signature(smarthome::NamedEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smarthome::namedentity_has_name():
    assert hasattr(smarthome::NamedEntity, "name")
    descriptor = None
    for klass in smarthome::NamedEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smarthome::pattern_is_not_abstract():
    assert not inspect.isabstract(smarthome::Pattern)


def test_smarthome::pattern_constructor_exists():
    assert callable(smarthome::Pattern.__init__)


def test_smarthome::pattern_constructor_args():
    sig = inspect.signature(smarthome::Pattern.__init__)
    params = list(sig.parameters.keys())

def test_precision_exists():
    # Check that the Enumeration exists
    assert Precision is not None

def test_precision_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Precision]
    expected_literals = [
        "ms",
        "s",
        "m",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Precision"

def test_activity_exists():
    # Check that the Enumeration exists
    assert Activity is not None

def test_activity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Activity]
    expected_literals = [
        "sitting",
        "laying",
        "standing",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Activity"

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "inferior",
        "equal",
        "superior",
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
smarthome::Mode_strategy = st.builds(
    smarthome::Mode,
)
smarthome::Duration_strategy = st.builds(
    smarthome::Duration,
    time=
        st.integers(),
    precision=
        safe_text
)
smarthome::Predicate_strategy = st.builds(
    smarthome::Predicate,
)
smarthome::Rule_strategy = st.builds(
    smarthome::Rule,
)
smarthome::CSVSensor_strategy = st.builds(
    smarthome::CSVSensor,
    file=
        safe_text
)
Predicate_strategy = st.builds(
    Predicate,
)
smarthome::PersonPredicate_strategy = st.builds(
    smarthome::PersonPredicate,
    activity=
        safe_text
)
smarthome::SensorPredicate_strategy = st.builds(
    smarthome::SensorPredicate,
    operator=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
smarthome::Home_strategy = st.builds(
    smarthome::Home,
    fileEvents=
        safe_text
)
Sensor_strategy = st.builds(
    Sensor,
)
smarthome::DigitalSensor_strategy = st.builds(
    smarthome::DigitalSensor,
)
smarthome::AnalogSensor_strategy = st.builds(
    smarthome::AnalogSensor,
)
NamedEntity_strategy = st.builds(
    NamedEntity,
)
smarthome::Tag_strategy = st.builds(
    smarthome::Tag,
)
smarthome::Room_strategy = st.builds(
    smarthome::Room,
)
smarthome::Person_strategy = st.builds(
    smarthome::Person,
)
smarthome::Sensor_strategy = st.builds(
    smarthome::Sensor,
)
smarthome::NamedEntity_strategy = st.builds(
    smarthome::NamedEntity,
    name=
        safe_text
)
smarthome::Pattern_strategy = st.builds(
    smarthome::Pattern,
)

@given(instance=smarthome::Mode_strategy)
@settings(max_examples=50)
def test_smarthome::mode_instantiation(instance):
    assert isinstance(instance, smarthome::Mode)

@given(instance=smarthome::Duration_strategy)
@settings(max_examples=50)
def test_smarthome::duration_instantiation(instance):
    assert isinstance(instance, smarthome::Duration)

@given(instance=smarthome::Duration_strategy)
def test_smarthome::duration_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=smarthome::Duration_strategy)
def test_smarthome::duration_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=smarthome::Duration_strategy)
def test_smarthome::duration_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=smarthome::Duration_strategy)
def test_smarthome::duration_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=smarthome::Predicate_strategy)
@settings(max_examples=50)
def test_smarthome::predicate_instantiation(instance):
    assert isinstance(instance, smarthome::Predicate)

@given(instance=smarthome::Rule_strategy)
@settings(max_examples=50)
def test_smarthome::rule_instantiation(instance):
    assert isinstance(instance, smarthome::Rule)

@given(instance=smarthome::CSVSensor_strategy)
@settings(max_examples=50)
def test_smarthome::csvsensor_instantiation(instance):
    assert isinstance(instance, smarthome::CSVSensor)

@given(instance=smarthome::CSVSensor_strategy)
def test_smarthome::csvsensor_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=smarthome::CSVSensor_strategy)
def test_smarthome::csvsensor_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=smarthome::PersonPredicate_strategy)
@settings(max_examples=50)
def test_smarthome::personpredicate_instantiation(instance):
    assert isinstance(instance, smarthome::PersonPredicate)

@given(instance=smarthome::PersonPredicate_strategy)
def test_smarthome::personpredicate_activity_type(instance):
    assert isinstance(instance.activity, str)


@given(instance=smarthome::PersonPredicate_strategy)
def test_smarthome::personpredicate_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original

@given(instance=smarthome::SensorPredicate_strategy)
@settings(max_examples=50)
def test_smarthome::sensorpredicate_instantiation(instance):
    assert isinstance(instance, smarthome::SensorPredicate)

@given(instance=smarthome::SensorPredicate_strategy)
def test_smarthome::sensorpredicate_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=smarthome::SensorPredicate_strategy)
def test_smarthome::sensorpredicate_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=smarthome::SensorPredicate_strategy)
def test_smarthome::sensorpredicate_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=smarthome::SensorPredicate_strategy)
def test_smarthome::sensorpredicate_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smarthome::Home_strategy)
@settings(max_examples=50)
def test_smarthome::home_instantiation(instance):
    assert isinstance(instance, smarthome::Home)

@given(instance=smarthome::Home_strategy)
def test_smarthome::home_fileEvents_type(instance):
    assert isinstance(instance.fileEvents, str)


@given(instance=smarthome::Home_strategy)
def test_smarthome::home_fileEvents_setter(instance):
    original = instance.fileEvents
    instance.fileEvents = original
    assert instance.fileEvents == original

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=smarthome::DigitalSensor_strategy)
@settings(max_examples=50)
def test_smarthome::digitalsensor_instantiation(instance):
    assert isinstance(instance, smarthome::DigitalSensor)

@given(instance=smarthome::AnalogSensor_strategy)
@settings(max_examples=50)
def test_smarthome::analogsensor_instantiation(instance):
    assert isinstance(instance, smarthome::AnalogSensor)

@given(instance=NamedEntity_strategy)
@settings(max_examples=50)
def test_namedentity_instantiation(instance):
    assert isinstance(instance, NamedEntity)

@given(instance=smarthome::Tag_strategy)
@settings(max_examples=50)
def test_smarthome::tag_instantiation(instance):
    assert isinstance(instance, smarthome::Tag)

@given(instance=smarthome::Room_strategy)
@settings(max_examples=50)
def test_smarthome::room_instantiation(instance):
    assert isinstance(instance, smarthome::Room)

@given(instance=smarthome::Person_strategy)
@settings(max_examples=50)
def test_smarthome::person_instantiation(instance):
    assert isinstance(instance, smarthome::Person)

@given(instance=smarthome::Sensor_strategy)
@settings(max_examples=50)
def test_smarthome::sensor_instantiation(instance):
    assert isinstance(instance, smarthome::Sensor)

@given(instance=smarthome::NamedEntity_strategy)
@settings(max_examples=50)
def test_smarthome::namedentity_instantiation(instance):
    assert isinstance(instance, smarthome::NamedEntity)

@given(instance=smarthome::NamedEntity_strategy)
def test_smarthome::namedentity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smarthome::NamedEntity_strategy)
def test_smarthome::namedentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smarthome::Pattern_strategy)
@settings(max_examples=50)
def test_smarthome::pattern_instantiation(instance):
    assert isinstance(instance, smarthome::Pattern)
