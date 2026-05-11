import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ArduinoMetamodel::Action,
    ArduinoMetamodel::Transition,
    ArduinoMetamodel::State,
    Instruccion,
    ArduinoMetamodel::delay,
    Pin,
    ArduinoMetamodel::Pin,
    ArduinoMetamodel::Analog,
    ArduinoMetamodel::Digital,
    ArduinoMetamodel::Instruccion,
    Analog,
    ArduinoMetamodel::PWM,
    ArduinoMetamodel::FiniteStateMachine,
    ArduinoMetamodel::Metodo,
    ArduinoMetamodel::ArduinoBoardUNO,
    ArduinoMetamodel::Project,
    DigitalID,
    AnalogID,
    PinMode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_arduinometamodel::action_is_not_abstract():
    assert not inspect.isabstract(ArduinoMetamodel::Action)


def test_arduinometamodel::action_constructor_exists():
    assert callable(ArduinoMetamodel::Action.__init__)


def test_arduinometamodel::action_constructor_args():
    sig = inspect.signature(ArduinoMetamodel::Action.__init__)
    params = list(sig.parameters.keys())



def test_arduinometamodel::transition_is_not_abstract():
    assert not inspect.isabstract(ArduinoMetamodel::Transition)


def test_arduinometamodel::transition_constructor_exists():
    assert callable(ArduinoMetamodel::Transition.__init__)


def test_arduinometamodel::transition_constructor_args():
    sig = inspect.signature(ArduinoMetamodel::Transition.__init__)
    params = list(sig.parameters.keys())



def test_arduinometamodel::state_is_not_abstract():
    assert not inspect.isabstract(ArduinoMetamodel::State)


def test_arduinometamodel::state_constructor_exists():
    assert callable(ArduinoMetamodel::State.__init__)


def test_arduinometamodel::state_constructor_args():
    sig = inspect.signature(ArduinoMetamodel::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isInitial" in params, "Missing parameter 'isInitial'"

def test_arduinometamodel::state_has_name():
    assert hasattr(ArduinoMetamodel::State, "name")
    descriptor = None
    for klass in ArduinoMetamodel::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_arduinometamodel::state_has_isInitial():
    assert hasattr(ArduinoMetamodel::State, "isInitial")
    descriptor = None
    for klass in ArduinoMetamodel::State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)



def test_instruccion_is_not_abstract():
    assert not inspect.isabstract(Instruccion)


def test_instruccion_constructor_exists():
    assert callable(Instruccion.__init__)


def test_instruccion_constructor_args():
    sig = inspect.signature(Instruccion.__init__)
    params = list(sig.parameters.keys())



def test_arduinometamodel::delay_is_not_abstract():
    assert not inspect.isabstract(ArduinoMetamodel::delay)


def test_arduinometamodel::delay_constructor_exists():
    assert callable(ArduinoMetamodel::delay.__init__)


def test_arduinometamodel::delay_constructor_args():
    sig = inspect.signature(ArduinoMetamodel::delay.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_arduinometamodel::pin_is_not_abstract():
    assert not inspect.isabstract(ArduinoMetamodel::Pin)


def test_arduinometamodel::pin_constructor_exists():
    assert callable(ArduinoMetamodel::Pin.__init__)


def test_arduinometamodel::pin_constructor_args():
    sig = inspect.signature(ArduinoMetamodel::Pin.__init__)
    params = list(sig.parameters.keys())
    assert "pinMode" in params, "Missing parameter 'pinMode'"
    assert "label" in params, "Missing parameter 'label'"

def test_arduinometamodel::pin_has_pinMode():
    assert hasattr(ArduinoMetamodel::Pin, "pinMode")
    descriptor = None
    for klass in ArduinoMetamodel::Pin.__mro__:
        if "pinMode" in klass.__dict__:
            descriptor = klass.__dict__["pinMode"]
            break
    assert isinstance(descriptor, property)

def test_arduinometamodel::pin_has_label():
    assert hasattr(ArduinoMetamodel::Pin, "label")
    descriptor = None
    for klass in ArduinoMetamodel::Pin.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_arduinometamodel::analog_is_not_abstract():
    assert not inspect.isabstract(ArduinoMetamodel::Analog)


def test_arduinometamodel::analog_constructor_exists():
    assert callable(ArduinoMetamodel::Analog.__init__)


def test_arduinometamodel::analog_constructor_args():
    sig = inspect.signature(ArduinoMetamodel::Analog.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_arduinometamodel::analog_has_ID():
    assert hasattr(ArduinoMetamodel::Analog, "ID")
    descriptor = None
    for klass in ArduinoMetamodel::Analog.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_arduinometamodel::digital_is_not_abstract():
    assert not inspect.isabstract(ArduinoMetamodel::Digital)


def test_arduinometamodel::digital_constructor_exists():
    assert callable(ArduinoMetamodel::Digital.__init__)


def test_arduinometamodel::digital_constructor_args():
    sig = inspect.signature(ArduinoMetamodel::Digital.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_arduinometamodel::digital_has_ID():
    assert hasattr(ArduinoMetamodel::Digital, "ID")
    descriptor = None
    for klass in ArduinoMetamodel::Digital.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_arduinometamodel::instruccion_is_not_abstract():
    assert not inspect.isabstract(ArduinoMetamodel::Instruccion)


def test_arduinometamodel::instruccion_constructor_exists():
    assert callable(ArduinoMetamodel::Instruccion.__init__)


def test_arduinometamodel::instruccion_constructor_args():
    sig = inspect.signature(ArduinoMetamodel::Instruccion.__init__)
    params = list(sig.parameters.keys())
    assert "codigo" in params, "Missing parameter 'codigo'"

def test_arduinometamodel::instruccion_has_codigo():
    assert hasattr(ArduinoMetamodel::Instruccion, "codigo")
    descriptor = None
    for klass in ArduinoMetamodel::Instruccion.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)



def test_analog_is_not_abstract():
    assert not inspect.isabstract(Analog)


def test_analog_constructor_exists():
    assert callable(Analog.__init__)


def test_analog_constructor_args():
    sig = inspect.signature(Analog.__init__)
    params = list(sig.parameters.keys())



def test_arduinometamodel::pwm_is_not_abstract():
    assert not inspect.isabstract(ArduinoMetamodel::PWM)


def test_arduinometamodel::pwm_constructor_exists():
    assert callable(ArduinoMetamodel::PWM.__init__)


def test_arduinometamodel::pwm_constructor_args():
    sig = inspect.signature(ArduinoMetamodel::PWM.__init__)
    params = list(sig.parameters.keys())



def test_arduinometamodel::finitestatemachine_is_not_abstract():
    assert not inspect.isabstract(ArduinoMetamodel::FiniteStateMachine)


def test_arduinometamodel::finitestatemachine_constructor_exists():
    assert callable(ArduinoMetamodel::FiniteStateMachine.__init__)


def test_arduinometamodel::finitestatemachine_constructor_args():
    sig = inspect.signature(ArduinoMetamodel::FiniteStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_arduinometamodel::metodo_is_not_abstract():
    assert not inspect.isabstract(ArduinoMetamodel::Metodo)


def test_arduinometamodel::metodo_constructor_exists():
    assert callable(ArduinoMetamodel::Metodo.__init__)


def test_arduinometamodel::metodo_constructor_args():
    sig = inspect.signature(ArduinoMetamodel::Metodo.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_arduinometamodel::metodo_has_nombre():
    assert hasattr(ArduinoMetamodel::Metodo, "nombre")
    descriptor = None
    for klass in ArduinoMetamodel::Metodo.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_arduinometamodel::arduinoboarduno_is_not_abstract():
    assert not inspect.isabstract(ArduinoMetamodel::ArduinoBoardUNO)


def test_arduinometamodel::arduinoboarduno_constructor_exists():
    assert callable(ArduinoMetamodel::ArduinoBoardUNO.__init__)


def test_arduinometamodel::arduinoboarduno_constructor_args():
    sig = inspect.signature(ArduinoMetamodel::ArduinoBoardUNO.__init__)
    params = list(sig.parameters.keys())



def test_arduinometamodel::project_is_not_abstract():
    assert not inspect.isabstract(ArduinoMetamodel::Project)


def test_arduinometamodel::project_constructor_exists():
    assert callable(ArduinoMetamodel::Project.__init__)


def test_arduinometamodel::project_constructor_args():
    sig = inspect.signature(ArduinoMetamodel::Project.__init__)
    params = list(sig.parameters.keys())

def test_digitalid_exists():
    # Check that the Enumeration exists
    assert DigitalID is not None

def test_digitalid_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DigitalID]
    expected_literals = [
        "D7",
        "D2",
        "D12",
        "D8",
        "D4",
        "D13",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DigitalID"

def test_analogid_exists():
    # Check that the Enumeration exists
    assert AnalogID is not None

def test_analogid_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnalogID]
    expected_literals = [
        "A0",
        "A5",
        "A4",
        "A1",
        "A6",
        "A2",
        "A3",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnalogID"

def test_pinmode_exists():
    # Check that the Enumeration exists
    assert PinMode is not None

def test_pinmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PinMode]
    expected_literals = [
        "INPUT",
        "OUTPUT",
        "INPUT_PULLUP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PinMode"


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
ArduinoMetamodel::Action_strategy = st.builds(
    ArduinoMetamodel::Action,
)
ArduinoMetamodel::Transition_strategy = st.builds(
    ArduinoMetamodel::Transition,
)
ArduinoMetamodel::State_strategy = st.builds(
    ArduinoMetamodel::State,
    name=
        safe_text,
    isInitial=
        st.booleans()
)
Instruccion_strategy = st.builds(
    Instruccion,
)
ArduinoMetamodel::delay_strategy = st.builds(
    ArduinoMetamodel::delay,
)
Pin_strategy = st.builds(
    Pin,
)
ArduinoMetamodel::Pin_strategy = st.builds(
    ArduinoMetamodel::Pin,
    pinMode=
        safe_text,
    label=
        safe_text
)
ArduinoMetamodel::Analog_strategy = st.builds(
    ArduinoMetamodel::Analog,
    ID=
        safe_text
)
ArduinoMetamodel::Digital_strategy = st.builds(
    ArduinoMetamodel::Digital,
    ID=
        safe_text
)
ArduinoMetamodel::Instruccion_strategy = st.builds(
    ArduinoMetamodel::Instruccion,
    codigo=
        safe_text
)
Analog_strategy = st.builds(
    Analog,
)
ArduinoMetamodel::PWM_strategy = st.builds(
    ArduinoMetamodel::PWM,
)
ArduinoMetamodel::FiniteStateMachine_strategy = st.builds(
    ArduinoMetamodel::FiniteStateMachine,
)
ArduinoMetamodel::Metodo_strategy = st.builds(
    ArduinoMetamodel::Metodo,
    nombre=
        safe_text
)
ArduinoMetamodel::ArduinoBoardUNO_strategy = st.builds(
    ArduinoMetamodel::ArduinoBoardUNO,
)
ArduinoMetamodel::Project_strategy = st.builds(
    ArduinoMetamodel::Project,
)

@given(instance=ArduinoMetamodel::Action_strategy)
@settings(max_examples=50)
def test_arduinometamodel::action_instantiation(instance):
    assert isinstance(instance, ArduinoMetamodel::Action)

@given(instance=ArduinoMetamodel::Transition_strategy)
@settings(max_examples=50)
def test_arduinometamodel::transition_instantiation(instance):
    assert isinstance(instance, ArduinoMetamodel::Transition)

@given(instance=ArduinoMetamodel::State_strategy)
@settings(max_examples=50)
def test_arduinometamodel::state_instantiation(instance):
    assert isinstance(instance, ArduinoMetamodel::State)

@given(instance=ArduinoMetamodel::State_strategy)
def test_arduinometamodel::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ArduinoMetamodel::State_strategy)
def test_arduinometamodel::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ArduinoMetamodel::State_strategy)
def test_arduinometamodel::state_isInitial_type(instance):
    assert isinstance(instance.isInitial, bool)


@given(instance=ArduinoMetamodel::State_strategy)
def test_arduinometamodel::state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=Instruccion_strategy)
@settings(max_examples=50)
def test_instruccion_instantiation(instance):
    assert isinstance(instance, Instruccion)

@given(instance=ArduinoMetamodel::delay_strategy)
@settings(max_examples=50)
def test_arduinometamodel::delay_instantiation(instance):
    assert isinstance(instance, ArduinoMetamodel::delay)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=ArduinoMetamodel::Pin_strategy)
@settings(max_examples=50)
def test_arduinometamodel::pin_instantiation(instance):
    assert isinstance(instance, ArduinoMetamodel::Pin)

@given(instance=ArduinoMetamodel::Pin_strategy)
def test_arduinometamodel::pin_pinMode_type(instance):
    assert isinstance(instance.pinMode, str)


@given(instance=ArduinoMetamodel::Pin_strategy)
def test_arduinometamodel::pin_pinMode_setter(instance):
    original = instance.pinMode
    instance.pinMode = original
    assert instance.pinMode == original

@given(instance=ArduinoMetamodel::Pin_strategy)
def test_arduinometamodel::pin_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=ArduinoMetamodel::Pin_strategy)
def test_arduinometamodel::pin_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=ArduinoMetamodel::Analog_strategy)
@settings(max_examples=50)
def test_arduinometamodel::analog_instantiation(instance):
    assert isinstance(instance, ArduinoMetamodel::Analog)

@given(instance=ArduinoMetamodel::Analog_strategy)
def test_arduinometamodel::analog_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=ArduinoMetamodel::Analog_strategy)
def test_arduinometamodel::analog_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=ArduinoMetamodel::Digital_strategy)
@settings(max_examples=50)
def test_arduinometamodel::digital_instantiation(instance):
    assert isinstance(instance, ArduinoMetamodel::Digital)

@given(instance=ArduinoMetamodel::Digital_strategy)
def test_arduinometamodel::digital_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=ArduinoMetamodel::Digital_strategy)
def test_arduinometamodel::digital_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=ArduinoMetamodel::Instruccion_strategy)
@settings(max_examples=50)
def test_arduinometamodel::instruccion_instantiation(instance):
    assert isinstance(instance, ArduinoMetamodel::Instruccion)

@given(instance=ArduinoMetamodel::Instruccion_strategy)
def test_arduinometamodel::instruccion_codigo_type(instance):
    assert isinstance(instance.codigo, str)


@given(instance=ArduinoMetamodel::Instruccion_strategy)
def test_arduinometamodel::instruccion_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original

@given(instance=Analog_strategy)
@settings(max_examples=50)
def test_analog_instantiation(instance):
    assert isinstance(instance, Analog)

@given(instance=ArduinoMetamodel::PWM_strategy)
@settings(max_examples=50)
def test_arduinometamodel::pwm_instantiation(instance):
    assert isinstance(instance, ArduinoMetamodel::PWM)

@given(instance=ArduinoMetamodel::FiniteStateMachine_strategy)
@settings(max_examples=50)
def test_arduinometamodel::finitestatemachine_instantiation(instance):
    assert isinstance(instance, ArduinoMetamodel::FiniteStateMachine)

@given(instance=ArduinoMetamodel::Metodo_strategy)
@settings(max_examples=50)
def test_arduinometamodel::metodo_instantiation(instance):
    assert isinstance(instance, ArduinoMetamodel::Metodo)

@given(instance=ArduinoMetamodel::Metodo_strategy)
def test_arduinometamodel::metodo_nombre_type(instance):
    assert isinstance(instance.nombre, str)


@given(instance=ArduinoMetamodel::Metodo_strategy)
def test_arduinometamodel::metodo_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=ArduinoMetamodel::ArduinoBoardUNO_strategy)
@settings(max_examples=50)
def test_arduinometamodel::arduinoboarduno_instantiation(instance):
    assert isinstance(instance, ArduinoMetamodel::ArduinoBoardUNO)

@given(instance=ArduinoMetamodel::Project_strategy)
@settings(max_examples=50)
def test_arduinometamodel::project_instantiation(instance):
    assert isinstance(instance, ArduinoMetamodel::Project)
