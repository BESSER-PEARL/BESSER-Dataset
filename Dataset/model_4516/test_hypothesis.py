import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    smarthome_Mode,
    smarthome_Duration,
    smarthome_Predicate,
    smarthome_Rule,
    smarthome_CSVSensor,
    Predicate,
    smarthome_PersonPredicate,
    smarthome_SensorPredicate,
    smarthome_Home,
    Sensor,
    smarthome_DigitalSensor,
    smarthome_AnalogSensor,
    NamedEntity,
    smarthome_Room,
    smarthome_Tag,
    smarthome_Person,
    smarthome_Sensor,
    smarthome_NamedEntity,
    smarthome_Pattern,
    Precision,
    Operator,
    Activity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smarthome_mode_is_not_abstract():
    assert not inspect.isabstract(smarthome_Mode)


def test_smarthome_mode_constructor_exists():
    assert callable(smarthome_Mode.__init__)


def test_smarthome_mode_constructor_args():
    sig = inspect.signature(smarthome_Mode.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_duration_is_not_abstract():
    assert not inspect.isabstract(smarthome_Duration)


def test_smarthome_duration_constructor_exists():
    assert callable(smarthome_Duration.__init__)


def test_smarthome_duration_constructor_args():
    sig = inspect.signature(smarthome_Duration.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "time" in params, "Missing parameter 'time'"

def test_smarthome_duration_has_precision():
    assert hasattr(smarthome_Duration, "precision")
    descriptor = None
    for klass in smarthome_Duration.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_smarthome_duration_has_time():
    assert hasattr(smarthome_Duration, "time")
    descriptor = None
    for klass in smarthome_Duration.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_predicate_is_not_abstract():
    assert not inspect.isabstract(smarthome_Predicate)


def test_smarthome_predicate_constructor_exists():
    assert callable(smarthome_Predicate.__init__)


def test_smarthome_predicate_constructor_args():
    sig = inspect.signature(smarthome_Predicate.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_rule_is_not_abstract():
    assert not inspect.isabstract(smarthome_Rule)


def test_smarthome_rule_constructor_exists():
    assert callable(smarthome_Rule.__init__)


def test_smarthome_rule_constructor_args():
    sig = inspect.signature(smarthome_Rule.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_csvsensor_is_not_abstract():
    assert not inspect.isabstract(smarthome_CSVSensor)


def test_smarthome_csvsensor_constructor_exists():
    assert callable(smarthome_CSVSensor.__init__)


def test_smarthome_csvsensor_constructor_args():
    sig = inspect.signature(smarthome_CSVSensor.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_smarthome_csvsensor_has_file():
    assert hasattr(smarthome_CSVSensor, "file")
    descriptor = None
    for klass in smarthome_CSVSensor.__mro__:
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



def test_smarthome_personpredicate_is_not_abstract():
    assert not inspect.isabstract(smarthome_PersonPredicate)


def test_smarthome_personpredicate_constructor_exists():
    assert callable(smarthome_PersonPredicate.__init__)


def test_smarthome_personpredicate_constructor_args():
    sig = inspect.signature(smarthome_PersonPredicate.__init__)
    params = list(sig.parameters.keys())
    assert "activity" in params, "Missing parameter 'activity'"

def test_smarthome_personpredicate_has_activity():
    assert hasattr(smarthome_PersonPredicate, "activity")
    descriptor = None
    for klass in smarthome_PersonPredicate.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_sensorpredicate_is_not_abstract():
    assert not inspect.isabstract(smarthome_SensorPredicate)


def test_smarthome_sensorpredicate_constructor_exists():
    assert callable(smarthome_SensorPredicate.__init__)


def test_smarthome_sensorpredicate_constructor_args():
    sig = inspect.signature(smarthome_SensorPredicate.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_smarthome_sensorpredicate_has_value():
    assert hasattr(smarthome_SensorPredicate, "value")
    descriptor = None
    for klass in smarthome_SensorPredicate.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_smarthome_sensorpredicate_has_operator():
    assert hasattr(smarthome_SensorPredicate, "operator")
    descriptor = None
    for klass in smarthome_SensorPredicate.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_home_is_not_abstract():
    assert not inspect.isabstract(smarthome_Home)


def test_smarthome_home_constructor_exists():
    assert callable(smarthome_Home.__init__)


def test_smarthome_home_constructor_args():
    sig = inspect.signature(smarthome_Home.__init__)
    params = list(sig.parameters.keys())
    assert "fileEvents" in params, "Missing parameter 'fileEvents'"

def test_smarthome_home_has_fileEvents():
    assert hasattr(smarthome_Home, "fileEvents")
    descriptor = None
    for klass in smarthome_Home.__mro__:
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



def test_smarthome_digitalsensor_is_not_abstract():
    assert not inspect.isabstract(smarthome_DigitalSensor)


def test_smarthome_digitalsensor_constructor_exists():
    assert callable(smarthome_DigitalSensor.__init__)


def test_smarthome_digitalsensor_constructor_args():
    sig = inspect.signature(smarthome_DigitalSensor.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_analogsensor_is_not_abstract():
    assert not inspect.isabstract(smarthome_AnalogSensor)


def test_smarthome_analogsensor_constructor_exists():
    assert callable(smarthome_AnalogSensor.__init__)


def test_smarthome_analogsensor_constructor_args():
    sig = inspect.signature(smarthome_AnalogSensor.__init__)
    params = list(sig.parameters.keys())



def test_namedentity_is_not_abstract():
    assert not inspect.isabstract(NamedEntity)


def test_namedentity_constructor_exists():
    assert callable(NamedEntity.__init__)


def test_namedentity_constructor_args():
    sig = inspect.signature(NamedEntity.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_room_is_not_abstract():
    assert not inspect.isabstract(smarthome_Room)


def test_smarthome_room_constructor_exists():
    assert callable(smarthome_Room.__init__)


def test_smarthome_room_constructor_args():
    sig = inspect.signature(smarthome_Room.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_tag_is_not_abstract():
    assert not inspect.isabstract(smarthome_Tag)


def test_smarthome_tag_constructor_exists():
    assert callable(smarthome_Tag.__init__)


def test_smarthome_tag_constructor_args():
    sig = inspect.signature(smarthome_Tag.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_person_is_not_abstract():
    assert not inspect.isabstract(smarthome_Person)


def test_smarthome_person_constructor_exists():
    assert callable(smarthome_Person.__init__)


def test_smarthome_person_constructor_args():
    sig = inspect.signature(smarthome_Person.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_sensor_is_not_abstract():
    assert not inspect.isabstract(smarthome_Sensor)


def test_smarthome_sensor_constructor_exists():
    assert callable(smarthome_Sensor.__init__)


def test_smarthome_sensor_constructor_args():
    sig = inspect.signature(smarthome_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_smarthome_namedentity_is_not_abstract():
    assert not inspect.isabstract(smarthome_NamedEntity)


def test_smarthome_namedentity_constructor_exists():
    assert callable(smarthome_NamedEntity.__init__)


def test_smarthome_namedentity_constructor_args():
    sig = inspect.signature(smarthome_NamedEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smarthome_namedentity_has_name():
    assert hasattr(smarthome_NamedEntity, "name")
    descriptor = None
    for klass in smarthome_NamedEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smarthome_pattern_is_not_abstract():
    assert not inspect.isabstract(smarthome_Pattern)


def test_smarthome_pattern_constructor_exists():
    assert callable(smarthome_Pattern.__init__)


def test_smarthome_pattern_constructor_args():
    sig = inspect.signature(smarthome_Pattern.__init__)
    params = list(sig.parameters.keys())

def test_precision_exists():
    # Check that the Enumeration exists
    assert Precision is not None

def test_precision_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Precision]
    expected_literals = [
        "m",
        "ms",
        "s",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Precision"

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
smarthome_Mode_strategy = st.builds(
    smarthome_Mode,
)
smarthome_Duration_strategy = st.builds(
    smarthome_Duration,
    precision=
        safe_text,
    time=
        st.integers()
)
smarthome_Predicate_strategy = st.builds(
    smarthome_Predicate,
)
smarthome_Rule_strategy = st.builds(
    smarthome_Rule,
)
smarthome_CSVSensor_strategy = st.builds(
    smarthome_CSVSensor,
    file=
        safe_text
)
Predicate_strategy = st.builds(
    Predicate,
)
smarthome_PersonPredicate_strategy = st.builds(
    smarthome_PersonPredicate,
    activity=
        safe_text
)
smarthome_SensorPredicate_strategy = st.builds(
    smarthome_SensorPredicate,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    operator=
        safe_text
)
smarthome_Home_strategy = st.builds(
    smarthome_Home,
    fileEvents=
        safe_text
)
Sensor_strategy = st.builds(
    Sensor,
)
smarthome_DigitalSensor_strategy = st.builds(
    smarthome_DigitalSensor,
)
smarthome_AnalogSensor_strategy = st.builds(
    smarthome_AnalogSensor,
)
NamedEntity_strategy = st.builds(
    NamedEntity,
)
smarthome_Room_strategy = st.builds(
    smarthome_Room,
)
smarthome_Tag_strategy = st.builds(
    smarthome_Tag,
)
smarthome_Person_strategy = st.builds(
    smarthome_Person,
)
smarthome_Sensor_strategy = st.builds(
    smarthome_Sensor,
)
smarthome_NamedEntity_strategy = st.builds(
    smarthome_NamedEntity,
    name=
        safe_text
)
smarthome_Pattern_strategy = st.builds(
    smarthome_Pattern,
)

@given(instance=smarthome_Mode_strategy)
@settings(max_examples=50)
def test_smarthome_mode_instantiation(instance):
    assert isinstance(instance, smarthome_Mode)

@given(instance=smarthome_Duration_strategy)
@settings(max_examples=50)
def test_smarthome_duration_instantiation(instance):
    assert isinstance(instance, smarthome_Duration)



@given(instance=smarthome_Duration_strategy)
def test_smarthome_duration_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=smarthome_Duration_strategy)
def test_smarthome_duration_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=smarthome_Predicate_strategy)
@settings(max_examples=50)
def test_smarthome_predicate_instantiation(instance):
    assert isinstance(instance, smarthome_Predicate)

@given(instance=smarthome_Rule_strategy)
@settings(max_examples=50)
def test_smarthome_rule_instantiation(instance):
    assert isinstance(instance, smarthome_Rule)

@given(instance=smarthome_CSVSensor_strategy)
@settings(max_examples=50)
def test_smarthome_csvsensor_instantiation(instance):
    assert isinstance(instance, smarthome_CSVSensor)



@given(instance=smarthome_CSVSensor_strategy)
def test_smarthome_csvsensor_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=smarthome_PersonPredicate_strategy)
@settings(max_examples=50)
def test_smarthome_personpredicate_instantiation(instance):
    assert isinstance(instance, smarthome_PersonPredicate)



@given(instance=smarthome_PersonPredicate_strategy)
def test_smarthome_personpredicate_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original

@given(instance=smarthome_SensorPredicate_strategy)
@settings(max_examples=50)
def test_smarthome_sensorpredicate_instantiation(instance):
    assert isinstance(instance, smarthome_SensorPredicate)



@given(instance=smarthome_SensorPredicate_strategy)
def test_smarthome_sensorpredicate_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=smarthome_SensorPredicate_strategy)
def test_smarthome_sensorpredicate_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=smarthome_Home_strategy)
@settings(max_examples=50)
def test_smarthome_home_instantiation(instance):
    assert isinstance(instance, smarthome_Home)



@given(instance=smarthome_Home_strategy)
def test_smarthome_home_fileEvents_setter(instance):
    original = instance.fileEvents
    instance.fileEvents = original
    assert instance.fileEvents == original

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=smarthome_DigitalSensor_strategy)
@settings(max_examples=50)
def test_smarthome_digitalsensor_instantiation(instance):
    assert isinstance(instance, smarthome_DigitalSensor)

@given(instance=smarthome_AnalogSensor_strategy)
@settings(max_examples=50)
def test_smarthome_analogsensor_instantiation(instance):
    assert isinstance(instance, smarthome_AnalogSensor)

@given(instance=NamedEntity_strategy)
@settings(max_examples=50)
def test_namedentity_instantiation(instance):
    assert isinstance(instance, NamedEntity)

@given(instance=smarthome_Room_strategy)
@settings(max_examples=50)
def test_smarthome_room_instantiation(instance):
    assert isinstance(instance, smarthome_Room)

@given(instance=smarthome_Tag_strategy)
@settings(max_examples=50)
def test_smarthome_tag_instantiation(instance):
    assert isinstance(instance, smarthome_Tag)

@given(instance=smarthome_Person_strategy)
@settings(max_examples=50)
def test_smarthome_person_instantiation(instance):
    assert isinstance(instance, smarthome_Person)

@given(instance=smarthome_Sensor_strategy)
@settings(max_examples=50)
def test_smarthome_sensor_instantiation(instance):
    assert isinstance(instance, smarthome_Sensor)

@given(instance=smarthome_NamedEntity_strategy)
@settings(max_examples=50)
def test_smarthome_namedentity_instantiation(instance):
    assert isinstance(instance, smarthome_NamedEntity)



@given(instance=smarthome_NamedEntity_strategy)
def test_smarthome_namedentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smarthome_Pattern_strategy)
@settings(max_examples=50)
def test_smarthome_pattern_instantiation(instance):
    assert isinstance(instance, smarthome_Pattern)
