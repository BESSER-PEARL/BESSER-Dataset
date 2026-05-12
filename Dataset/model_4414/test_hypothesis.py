import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Pin,
    arduino_Pin,
    Instruction,
    arduino_Function,
    arduino_DigitalPin,
    Function,
    arduino_Read,
    arduino_Write,
    arduino_Instruction,
    arduino_Loop,
    arduino_Setup,
    arduino_Sketch,
    arduino_Project,
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



def test_arduino_pin_is_not_abstract():
    assert not inspect.isabstract(arduino_Pin)


def test_arduino_pin_constructor_exists():
    assert callable(arduino_Pin.__init__)


def test_arduino_pin_constructor_args():
    sig = inspect.signature(arduino_Pin.__init__)
    params = list(sig.parameters.keys())
    assert "Direction" in params, "Missing parameter 'Direction'"
    assert "name" in params, "Missing parameter 'name'"

def test_arduino_pin_has_Direction():
    assert hasattr(arduino_Pin, "Direction")
    descriptor = None
    for klass in arduino_Pin.__mro__:
        if "Direction" in klass.__dict__:
            descriptor = klass.__dict__["Direction"]
            break
    assert isinstance(descriptor, property)

def test_arduino_pin_has_name():
    assert hasattr(arduino_Pin, "name")
    descriptor = None
    for klass in arduino_Pin.__mro__:
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



def test_arduino_function_is_not_abstract():
    assert not inspect.isabstract(arduino_Function)


def test_arduino_function_constructor_exists():
    assert callable(arduino_Function.__init__)


def test_arduino_function_constructor_args():
    sig = inspect.signature(arduino_Function.__init__)
    params = list(sig.parameters.keys())



def test_arduino_digitalpin_is_not_abstract():
    assert not inspect.isabstract(arduino_DigitalPin)


def test_arduino_digitalpin_constructor_exists():
    assert callable(arduino_DigitalPin.__init__)


def test_arduino_digitalpin_constructor_args():
    sig = inspect.signature(arduino_DigitalPin.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_arduino_digitalpin_has_number():
    assert hasattr(arduino_DigitalPin, "number")
    descriptor = None
    for klass in arduino_DigitalPin.__mro__:
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



def test_arduino_read_is_not_abstract():
    assert not inspect.isabstract(arduino_Read)


def test_arduino_read_constructor_exists():
    assert callable(arduino_Read.__init__)


def test_arduino_read_constructor_args():
    sig = inspect.signature(arduino_Read.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "returnValue" in params, "Missing parameter 'returnValue'"

def test_arduino_read_has_name():
    assert hasattr(arduino_Read, "name")
    descriptor = None
    for klass in arduino_Read.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_arduino_read_has_returnValue():
    assert hasattr(arduino_Read, "returnValue")
    descriptor = None
    for klass in arduino_Read.__mro__:
        if "returnValue" in klass.__dict__:
            descriptor = klass.__dict__["returnValue"]
            break
    assert isinstance(descriptor, property)



def test_arduino_write_is_not_abstract():
    assert not inspect.isabstract(arduino_Write)


def test_arduino_write_constructor_exists():
    assert callable(arduino_Write.__init__)


def test_arduino_write_constructor_args():
    sig = inspect.signature(arduino_Write.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduino_write_has_name():
    assert hasattr(arduino_Write, "name")
    descriptor = None
    for klass in arduino_Write.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduino_instruction_is_not_abstract():
    assert not inspect.isabstract(arduino_Instruction)


def test_arduino_instruction_constructor_exists():
    assert callable(arduino_Instruction.__init__)


def test_arduino_instruction_constructor_args():
    sig = inspect.signature(arduino_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_arduino_loop_is_not_abstract():
    assert not inspect.isabstract(arduino_Loop)


def test_arduino_loop_constructor_exists():
    assert callable(arduino_Loop.__init__)


def test_arduino_loop_constructor_args():
    sig = inspect.signature(arduino_Loop.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduino_loop_has_name():
    assert hasattr(arduino_Loop, "name")
    descriptor = None
    for klass in arduino_Loop.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduino_setup_is_not_abstract():
    assert not inspect.isabstract(arduino_Setup)


def test_arduino_setup_constructor_exists():
    assert callable(arduino_Setup.__init__)


def test_arduino_setup_constructor_args():
    sig = inspect.signature(arduino_Setup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduino_setup_has_name():
    assert hasattr(arduino_Setup, "name")
    descriptor = None
    for klass in arduino_Setup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduino_sketch_is_not_abstract():
    assert not inspect.isabstract(arduino_Sketch)


def test_arduino_sketch_constructor_exists():
    assert callable(arduino_Sketch.__init__)


def test_arduino_sketch_constructor_args():
    sig = inspect.signature(arduino_Sketch.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduino_sketch_has_name():
    assert hasattr(arduino_Sketch, "name")
    descriptor = None
    for klass in arduino_Sketch.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduino_project_is_not_abstract():
    assert not inspect.isabstract(arduino_Project)


def test_arduino_project_constructor_exists():
    assert callable(arduino_Project.__init__)


def test_arduino_project_constructor_args():
    sig = inspect.signature(arduino_Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduino_project_has_name():
    assert hasattr(arduino_Project, "name")
    descriptor = None
    for klass in arduino_Project.__mro__:
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
        "D5",
        "D4",
        "D0",
        "D2",
        "D1",
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
arduino_Pin_strategy = st.builds(
    arduino_Pin,
    Direction=
        safe_text,
    name=
        safe_text
)
Instruction_strategy = st.builds(
    Instruction,
)
arduino_Function_strategy = st.builds(
    arduino_Function,
)
arduino_DigitalPin_strategy = st.builds(
    arduino_DigitalPin,
    number=
        safe_text
)
Function_strategy = st.builds(
    Function,
)
arduino_Read_strategy = st.builds(
    arduino_Read,
    name=
        safe_text,
    returnValue=
        safe_text
)
arduino_Write_strategy = st.builds(
    arduino_Write,
    name=
        safe_text
)
arduino_Instruction_strategy = st.builds(
    arduino_Instruction,
)
arduino_Loop_strategy = st.builds(
    arduino_Loop,
    name=
        safe_text
)
arduino_Setup_strategy = st.builds(
    arduino_Setup,
    name=
        safe_text
)
arduino_Sketch_strategy = st.builds(
    arduino_Sketch,
    name=
        safe_text
)
arduino_Project_strategy = st.builds(
    arduino_Project,
    name=
        safe_text
)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=arduino_Pin_strategy)
@settings(max_examples=50)
def test_arduino_pin_instantiation(instance):
    assert isinstance(instance, arduino_Pin)



@given(instance=arduino_Pin_strategy)
def test_arduino_pin_Direction_setter(instance):
    original = instance.Direction
    instance.Direction = original
    assert instance.Direction == original



@given(instance=arduino_Pin_strategy)
def test_arduino_pin_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=arduino_Function_strategy)
@settings(max_examples=50)
def test_arduino_function_instantiation(instance):
    assert isinstance(instance, arduino_Function)

@given(instance=arduino_DigitalPin_strategy)
@settings(max_examples=50)
def test_arduino_digitalpin_instantiation(instance):
    assert isinstance(instance, arduino_DigitalPin)



@given(instance=arduino_DigitalPin_strategy)
def test_arduino_digitalpin_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=arduino_Read_strategy)
@settings(max_examples=50)
def test_arduino_read_instantiation(instance):
    assert isinstance(instance, arduino_Read)



@given(instance=arduino_Read_strategy)
def test_arduino_read_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=arduino_Read_strategy)
def test_arduino_read_returnValue_setter(instance):
    original = instance.returnValue
    instance.returnValue = original
    assert instance.returnValue == original

@given(instance=arduino_Write_strategy)
@settings(max_examples=50)
def test_arduino_write_instantiation(instance):
    assert isinstance(instance, arduino_Write)



@given(instance=arduino_Write_strategy)
def test_arduino_write_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduino_Instruction_strategy)
@settings(max_examples=50)
def test_arduino_instruction_instantiation(instance):
    assert isinstance(instance, arduino_Instruction)

@given(instance=arduino_Loop_strategy)
@settings(max_examples=50)
def test_arduino_loop_instantiation(instance):
    assert isinstance(instance, arduino_Loop)



@given(instance=arduino_Loop_strategy)
def test_arduino_loop_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduino_Setup_strategy)
@settings(max_examples=50)
def test_arduino_setup_instantiation(instance):
    assert isinstance(instance, arduino_Setup)



@given(instance=arduino_Setup_strategy)
def test_arduino_setup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduino_Sketch_strategy)
@settings(max_examples=50)
def test_arduino_sketch_instantiation(instance):
    assert isinstance(instance, arduino_Sketch)



@given(instance=arduino_Sketch_strategy)
def test_arduino_sketch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduino_Project_strategy)
@settings(max_examples=50)
def test_arduino_project_instantiation(instance):
    assert isinstance(instance, arduino_Project)



@given(instance=arduino_Project_strategy)
def test_arduino_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
