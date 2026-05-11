import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Pin,
    arduino::Pin,
    Instruction,
    arduino::Function,
    arduino::DigitalPin,
    Function,
    arduino::Read,
    arduino::Write,
    arduino::Instruction,
    arduino::Loop,
    arduino::Setup,
    arduino::Sketch,
    arduino::Project,
    Direction,
    DigitalPinNumber,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_arduino::pin_is_not_abstract():
    assert not inspect.isabstract(arduino::Pin)


def test_arduino::pin_constructor_exists():
    assert callable(arduino::Pin.__init__)


def test_arduino::pin_constructor_args():
    sig = inspect.signature(arduino::Pin.__init__)
    params = list(sig.parameters.keys())
    assert "Direction" in params, "Missing parameter 'Direction'"
    assert "name" in params, "Missing parameter 'name'"

def test_arduino::pin_has_Direction():
    assert hasattr(arduino::Pin, "Direction")
    descriptor = None
    for klass in arduino::Pin.__mro__:
        if "Direction" in klass.__dict__:
            descriptor = klass.__dict__["Direction"]
            break
    assert isinstance(descriptor, property)

def test_arduino::pin_has_name():
    assert hasattr(arduino::Pin, "name")
    descriptor = None
    for klass in arduino::Pin.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_arduino::function_is_not_abstract():
    assert not inspect.isabstract(arduino::Function)


def test_arduino::function_constructor_exists():
    assert callable(arduino::Function.__init__)


def test_arduino::function_constructor_args():
    sig = inspect.signature(arduino::Function.__init__)
    params = list(sig.parameters.keys())



def test_arduino::digitalpin_is_not_abstract():
    assert not inspect.isabstract(arduino::DigitalPin)


def test_arduino::digitalpin_constructor_exists():
    assert callable(arduino::DigitalPin.__init__)


def test_arduino::digitalpin_constructor_args():
    sig = inspect.signature(arduino::DigitalPin.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_arduino::digitalpin_has_number():
    assert hasattr(arduino::DigitalPin, "number")
    descriptor = None
    for klass in arduino::DigitalPin.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_arduino::read_is_not_abstract():
    assert not inspect.isabstract(arduino::Read)


def test_arduino::read_constructor_exists():
    assert callable(arduino::Read.__init__)


def test_arduino::read_constructor_args():
    sig = inspect.signature(arduino::Read.__init__)
    params = list(sig.parameters.keys())
    assert "returnValue" in params, "Missing parameter 'returnValue'"
    assert "name" in params, "Missing parameter 'name'"

def test_arduino::read_has_returnValue():
    assert hasattr(arduino::Read, "returnValue")
    descriptor = None
    for klass in arduino::Read.__mro__:
        if "returnValue" in klass.__dict__:
            descriptor = klass.__dict__["returnValue"]
            break
    assert isinstance(descriptor, property)

def test_arduino::read_has_name():
    assert hasattr(arduino::Read, "name")
    descriptor = None
    for klass in arduino::Read.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduino::write_is_not_abstract():
    assert not inspect.isabstract(arduino::Write)


def test_arduino::write_constructor_exists():
    assert callable(arduino::Write.__init__)


def test_arduino::write_constructor_args():
    sig = inspect.signature(arduino::Write.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduino::write_has_name():
    assert hasattr(arduino::Write, "name")
    descriptor = None
    for klass in arduino::Write.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduino::instruction_is_not_abstract():
    assert not inspect.isabstract(arduino::Instruction)


def test_arduino::instruction_constructor_exists():
    assert callable(arduino::Instruction.__init__)


def test_arduino::instruction_constructor_args():
    sig = inspect.signature(arduino::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_arduino::loop_is_not_abstract():
    assert not inspect.isabstract(arduino::Loop)


def test_arduino::loop_constructor_exists():
    assert callable(arduino::Loop.__init__)


def test_arduino::loop_constructor_args():
    sig = inspect.signature(arduino::Loop.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduino::loop_has_name():
    assert hasattr(arduino::Loop, "name")
    descriptor = None
    for klass in arduino::Loop.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduino::setup_is_not_abstract():
    assert not inspect.isabstract(arduino::Setup)


def test_arduino::setup_constructor_exists():
    assert callable(arduino::Setup.__init__)


def test_arduino::setup_constructor_args():
    sig = inspect.signature(arduino::Setup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduino::setup_has_name():
    assert hasattr(arduino::Setup, "name")
    descriptor = None
    for klass in arduino::Setup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduino::sketch_is_not_abstract():
    assert not inspect.isabstract(arduino::Sketch)


def test_arduino::sketch_constructor_exists():
    assert callable(arduino::Sketch.__init__)


def test_arduino::sketch_constructor_args():
    sig = inspect.signature(arduino::Sketch.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduino::sketch_has_name():
    assert hasattr(arduino::Sketch, "name")
    descriptor = None
    for klass in arduino::Sketch.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduino::project_is_not_abstract():
    assert not inspect.isabstract(arduino::Project)


def test_arduino::project_constructor_exists():
    assert callable(arduino::Project.__init__)


def test_arduino::project_constructor_args():
    sig = inspect.signature(arduino::Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduino::project_has_name():
    assert hasattr(arduino::Project, "name")
    descriptor = None
    for klass in arduino::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "OUTPUT",
        "INPUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_digitalpinnumber_exists():
    # Check that the Enumeration exists
    assert DigitalPinNumber is not None

def test_digitalpinnumber_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DigitalPinNumber]
    expected_literals = [
        "D2",
        "D0",
        "D1",
        "D4",
        "D5",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DigitalPinNumber"


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
Pin_strategy = st.builds(
    Pin,
)
arduino::Pin_strategy = st.builds(
    arduino::Pin,
    Direction=
        safe_text,
    name=
        safe_text
)
Instruction_strategy = st.builds(
    Instruction,
)
arduino::Function_strategy = st.builds(
    arduino::Function,
)
arduino::DigitalPin_strategy = st.builds(
    arduino::DigitalPin,
    number=
        safe_text
)
Function_strategy = st.builds(
    Function,
)
arduino::Read_strategy = st.builds(
    arduino::Read,
    returnValue=
        safe_text,
    name=
        safe_text
)
arduino::Write_strategy = st.builds(
    arduino::Write,
    name=
        safe_text
)
arduino::Instruction_strategy = st.builds(
    arduino::Instruction,
)
arduino::Loop_strategy = st.builds(
    arduino::Loop,
    name=
        safe_text
)
arduino::Setup_strategy = st.builds(
    arduino::Setup,
    name=
        safe_text
)
arduino::Sketch_strategy = st.builds(
    arduino::Sketch,
    name=
        safe_text
)
arduino::Project_strategy = st.builds(
    arduino::Project,
    name=
        safe_text
)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=arduino::Pin_strategy)
@settings(max_examples=50)
def test_arduino::pin_instantiation(instance):
    assert isinstance(instance, arduino::Pin)

@given(instance=arduino::Pin_strategy)
def test_arduino::pin_Direction_type(instance):
    assert isinstance(instance.Direction, str)


@given(instance=arduino::Pin_strategy)
def test_arduino::pin_Direction_setter(instance):
    original = instance.Direction
    instance.Direction = original
    assert instance.Direction == original

@given(instance=arduino::Pin_strategy)
def test_arduino::pin_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduino::Pin_strategy)
def test_arduino::pin_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=arduino::Function_strategy)
@settings(max_examples=50)
def test_arduino::function_instantiation(instance):
    assert isinstance(instance, arduino::Function)

@given(instance=arduino::DigitalPin_strategy)
@settings(max_examples=50)
def test_arduino::digitalpin_instantiation(instance):
    assert isinstance(instance, arduino::DigitalPin)

@given(instance=arduino::DigitalPin_strategy)
def test_arduino::digitalpin_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=arduino::DigitalPin_strategy)
def test_arduino::digitalpin_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=arduino::Read_strategy)
@settings(max_examples=50)
def test_arduino::read_instantiation(instance):
    assert isinstance(instance, arduino::Read)

@given(instance=arduino::Read_strategy)
def test_arduino::read_returnValue_type(instance):
    assert isinstance(instance.returnValue, str)


@given(instance=arduino::Read_strategy)
def test_arduino::read_returnValue_setter(instance):
    original = instance.returnValue
    instance.returnValue = original
    assert instance.returnValue == original

@given(instance=arduino::Read_strategy)
def test_arduino::read_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduino::Read_strategy)
def test_arduino::read_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduino::Write_strategy)
@settings(max_examples=50)
def test_arduino::write_instantiation(instance):
    assert isinstance(instance, arduino::Write)

@given(instance=arduino::Write_strategy)
def test_arduino::write_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduino::Write_strategy)
def test_arduino::write_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduino::Instruction_strategy)
@settings(max_examples=50)
def test_arduino::instruction_instantiation(instance):
    assert isinstance(instance, arduino::Instruction)

@given(instance=arduino::Loop_strategy)
@settings(max_examples=50)
def test_arduino::loop_instantiation(instance):
    assert isinstance(instance, arduino::Loop)

@given(instance=arduino::Loop_strategy)
def test_arduino::loop_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduino::Loop_strategy)
def test_arduino::loop_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduino::Setup_strategy)
@settings(max_examples=50)
def test_arduino::setup_instantiation(instance):
    assert isinstance(instance, arduino::Setup)

@given(instance=arduino::Setup_strategy)
def test_arduino::setup_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduino::Setup_strategy)
def test_arduino::setup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduino::Sketch_strategy)
@settings(max_examples=50)
def test_arduino::sketch_instantiation(instance):
    assert isinstance(instance, arduino::Sketch)

@given(instance=arduino::Sketch_strategy)
def test_arduino::sketch_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduino::Sketch_strategy)
def test_arduino::sketch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduino::Project_strategy)
@settings(max_examples=50)
def test_arduino::project_instantiation(instance):
    assert isinstance(instance, arduino::Project)

@given(instance=arduino::Project_strategy)
def test_arduino::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduino::Project_strategy)
def test_arduino::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
