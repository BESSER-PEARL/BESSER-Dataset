import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    arduino::Instruction,
    arduino::Block,
    NamedElement,
    arduino::Module,
    arduino::Board,
    arduino::Sketch,
    arduino::Project,
    arduino::NamedElement,
    Expression,
    arduino::BinaryExpression,
    arduino::UnaryExpression,
    arduino::Constant,
    arduino::ModuleGet,
    arduino::Expression,
    Control,
    arduino::While,
    arduino::If,
    Instruction,
    arduino::Delay,
    arduino::WaitFor,
    arduino::Control,
    ModuleSet,
    arduino::SetLed,
    InputModule,
    arduino::ModuleSet,
    arduino::PushButton,
    OutputModule,
    arduino::Led,
    Module,
    arduino::InputModule,
    arduino::OutputModule,
    UnaryOperatorKind,
    BinaryOperatorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_arduino::instruction_is_not_abstract():
    assert not inspect.isabstract(arduino::Instruction)


def test_arduino::instruction_constructor_exists():
    assert callable(arduino::Instruction.__init__)


def test_arduino::instruction_constructor_args():
    sig = inspect.signature(arduino::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_arduino::block_is_not_abstract():
    assert not inspect.isabstract(arduino::Block)


def test_arduino::block_constructor_exists():
    assert callable(arduino::Block.__init__)


def test_arduino::block_constructor_args():
    sig = inspect.signature(arduino::Block.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_arduino::module_is_not_abstract():
    assert not inspect.isabstract(arduino::Module)


def test_arduino::module_constructor_exists():
    assert callable(arduino::Module.__init__)


def test_arduino::module_constructor_args():
    sig = inspect.signature(arduino::Module.__init__)
    params = list(sig.parameters.keys())



def test_arduino::board_is_not_abstract():
    assert not inspect.isabstract(arduino::Board)


def test_arduino::board_constructor_exists():
    assert callable(arduino::Board.__init__)


def test_arduino::board_constructor_args():
    sig = inspect.signature(arduino::Board.__init__)
    params = list(sig.parameters.keys())



def test_arduino::sketch_is_not_abstract():
    assert not inspect.isabstract(arduino::Sketch)


def test_arduino::sketch_constructor_exists():
    assert callable(arduino::Sketch.__init__)


def test_arduino::sketch_constructor_args():
    sig = inspect.signature(arduino::Sketch.__init__)
    params = list(sig.parameters.keys())



def test_arduino::project_is_not_abstract():
    assert not inspect.isabstract(arduino::Project)


def test_arduino::project_constructor_exists():
    assert callable(arduino::Project.__init__)


def test_arduino::project_constructor_args():
    sig = inspect.signature(arduino::Project.__init__)
    params = list(sig.parameters.keys())



def test_arduino::namedelement_is_not_abstract():
    assert not inspect.isabstract(arduino::NamedElement)


def test_arduino::namedelement_constructor_exists():
    assert callable(arduino::NamedElement.__init__)


def test_arduino::namedelement_constructor_args():
    sig = inspect.signature(arduino::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduino::namedelement_has_name():
    assert hasattr(arduino::NamedElement, "name")
    descriptor = None
    for klass in arduino::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_arduino::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(arduino::BinaryExpression)


def test_arduino::binaryexpression_constructor_exists():
    assert callable(arduino::BinaryExpression.__init__)


def test_arduino::binaryexpression_constructor_args():
    sig = inspect.signature(arduino::BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_arduino::binaryexpression_has_operator():
    assert hasattr(arduino::BinaryExpression, "operator")
    descriptor = None
    for klass in arduino::BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_arduino::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(arduino::UnaryExpression)


def test_arduino::unaryexpression_constructor_exists():
    assert callable(arduino::UnaryExpression.__init__)


def test_arduino::unaryexpression_constructor_args():
    sig = inspect.signature(arduino::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_arduino::unaryexpression_has_operator():
    assert hasattr(arduino::UnaryExpression, "operator")
    descriptor = None
    for klass in arduino::UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_arduino::constant_is_not_abstract():
    assert not inspect.isabstract(arduino::Constant)


def test_arduino::constant_constructor_exists():
    assert callable(arduino::Constant.__init__)


def test_arduino::constant_constructor_args():
    sig = inspect.signature(arduino::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduino::constant_has_value():
    assert hasattr(arduino::Constant, "value")
    descriptor = None
    for klass in arduino::Constant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arduino::moduleget_is_not_abstract():
    assert not inspect.isabstract(arduino::ModuleGet)


def test_arduino::moduleget_constructor_exists():
    assert callable(arduino::ModuleGet.__init__)


def test_arduino::moduleget_constructor_args():
    sig = inspect.signature(arduino::ModuleGet.__init__)
    params = list(sig.parameters.keys())



def test_arduino::expression_is_not_abstract():
    assert not inspect.isabstract(arduino::Expression)


def test_arduino::expression_constructor_exists():
    assert callable(arduino::Expression.__init__)


def test_arduino::expression_constructor_args():
    sig = inspect.signature(arduino::Expression.__init__)
    params = list(sig.parameters.keys())



def test_control_is_not_abstract():
    assert not inspect.isabstract(Control)


def test_control_constructor_exists():
    assert callable(Control.__init__)


def test_control_constructor_args():
    sig = inspect.signature(Control.__init__)
    params = list(sig.parameters.keys())



def test_arduino::while_is_not_abstract():
    assert not inspect.isabstract(arduino::While)


def test_arduino::while_constructor_exists():
    assert callable(arduino::While.__init__)


def test_arduino::while_constructor_args():
    sig = inspect.signature(arduino::While.__init__)
    params = list(sig.parameters.keys())



def test_arduino::if_is_not_abstract():
    assert not inspect.isabstract(arduino::If)


def test_arduino::if_constructor_exists():
    assert callable(arduino::If.__init__)


def test_arduino::if_constructor_args():
    sig = inspect.signature(arduino::If.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_arduino::delay_is_not_abstract():
    assert not inspect.isabstract(arduino::Delay)


def test_arduino::delay_constructor_exists():
    assert callable(arduino::Delay.__init__)


def test_arduino::delay_constructor_args():
    sig = inspect.signature(arduino::Delay.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduino::delay_has_value():
    assert hasattr(arduino::Delay, "value")
    descriptor = None
    for klass in arduino::Delay.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arduino::waitfor_is_not_abstract():
    assert not inspect.isabstract(arduino::WaitFor)


def test_arduino::waitfor_constructor_exists():
    assert callable(arduino::WaitFor.__init__)


def test_arduino::waitfor_constructor_args():
    sig = inspect.signature(arduino::WaitFor.__init__)
    params = list(sig.parameters.keys())



def test_arduino::control_is_not_abstract():
    assert not inspect.isabstract(arduino::Control)


def test_arduino::control_constructor_exists():
    assert callable(arduino::Control.__init__)


def test_arduino::control_constructor_args():
    sig = inspect.signature(arduino::Control.__init__)
    params = list(sig.parameters.keys())



def test_moduleset_is_not_abstract():
    assert not inspect.isabstract(ModuleSet)


def test_moduleset_constructor_exists():
    assert callable(ModuleSet.__init__)


def test_moduleset_constructor_args():
    sig = inspect.signature(ModuleSet.__init__)
    params = list(sig.parameters.keys())



def test_arduino::setled_is_not_abstract():
    assert not inspect.isabstract(arduino::SetLed)


def test_arduino::setled_constructor_exists():
    assert callable(arduino::SetLed.__init__)


def test_arduino::setled_constructor_args():
    sig = inspect.signature(arduino::SetLed.__init__)
    params = list(sig.parameters.keys())



def test_inputmodule_is_not_abstract():
    assert not inspect.isabstract(InputModule)


def test_inputmodule_constructor_exists():
    assert callable(InputModule.__init__)


def test_inputmodule_constructor_args():
    sig = inspect.signature(InputModule.__init__)
    params = list(sig.parameters.keys())



def test_arduino::moduleset_is_not_abstract():
    assert not inspect.isabstract(arduino::ModuleSet)


def test_arduino::moduleset_constructor_exists():
    assert callable(arduino::ModuleSet.__init__)


def test_arduino::moduleset_constructor_args():
    sig = inspect.signature(arduino::ModuleSet.__init__)
    params = list(sig.parameters.keys())



def test_arduino::pushbutton_is_not_abstract():
    assert not inspect.isabstract(arduino::PushButton)


def test_arduino::pushbutton_constructor_exists():
    assert callable(arduino::PushButton.__init__)


def test_arduino::pushbutton_constructor_args():
    sig = inspect.signature(arduino::PushButton.__init__)
    params = list(sig.parameters.keys())



def test_outputmodule_is_not_abstract():
    assert not inspect.isabstract(OutputModule)


def test_outputmodule_constructor_exists():
    assert callable(OutputModule.__init__)


def test_outputmodule_constructor_args():
    sig = inspect.signature(OutputModule.__init__)
    params = list(sig.parameters.keys())



def test_arduino::led_is_not_abstract():
    assert not inspect.isabstract(arduino::Led)


def test_arduino::led_constructor_exists():
    assert callable(arduino::Led.__init__)


def test_arduino::led_constructor_args():
    sig = inspect.signature(arduino::Led.__init__)
    params = list(sig.parameters.keys())



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_arduino::inputmodule_is_not_abstract():
    assert not inspect.isabstract(arduino::InputModule)


def test_arduino::inputmodule_constructor_exists():
    assert callable(arduino::InputModule.__init__)


def test_arduino::inputmodule_constructor_args():
    sig = inspect.signature(arduino::InputModule.__init__)
    params = list(sig.parameters.keys())



def test_arduino::outputmodule_is_not_abstract():
    assert not inspect.isabstract(arduino::OutputModule)


def test_arduino::outputmodule_constructor_exists():
    assert callable(arduino::OutputModule.__init__)


def test_arduino::outputmodule_constructor_args():
    sig = inspect.signature(arduino::OutputModule.__init__)
    params = list(sig.parameters.keys())

def test_unaryoperatorkind_exists():
    # Check that the Enumeration exists
    assert UnaryOperatorKind is not None

def test_unaryoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperatorKind]
    expected_literals = [
        "minus",
        "neg",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperatorKind"

def test_binaryoperatorkind_exists():
    # Check that the Enumeration exists
    assert BinaryOperatorKind is not None

def test_binaryoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOperatorKind]
    expected_literals = [
        "div",
        "min",
        "mul",
        "mod",
        "eq",
        "ge",
        "le",
        "lt",
        "gt",
        "sub",
        "max",
        "neq",
        "add",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOperatorKind"


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
arduino::Instruction_strategy = st.builds(
    arduino::Instruction,
)
arduino::Block_strategy = st.builds(
    arduino::Block,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
arduino::Module_strategy = st.builds(
    arduino::Module,
)
arduino::Board_strategy = st.builds(
    arduino::Board,
)
arduino::Sketch_strategy = st.builds(
    arduino::Sketch,
)
arduino::Project_strategy = st.builds(
    arduino::Project,
)
arduino::NamedElement_strategy = st.builds(
    arduino::NamedElement,
    name=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
arduino::BinaryExpression_strategy = st.builds(
    arduino::BinaryExpression,
    operator=
        safe_text
)
arduino::UnaryExpression_strategy = st.builds(
    arduino::UnaryExpression,
    operator=
        safe_text
)
arduino::Constant_strategy = st.builds(
    arduino::Constant,
    value=
        st.integers()
)
arduino::ModuleGet_strategy = st.builds(
    arduino::ModuleGet,
)
arduino::Expression_strategy = st.builds(
    arduino::Expression,
)
Control_strategy = st.builds(
    Control,
)
arduino::While_strategy = st.builds(
    arduino::While,
)
arduino::If_strategy = st.builds(
    arduino::If,
)
Instruction_strategy = st.builds(
    Instruction,
)
arduino::Delay_strategy = st.builds(
    arduino::Delay,
    value=
        st.integers()
)
arduino::WaitFor_strategy = st.builds(
    arduino::WaitFor,
)
arduino::Control_strategy = st.builds(
    arduino::Control,
)
ModuleSet_strategy = st.builds(
    ModuleSet,
)
arduino::SetLed_strategy = st.builds(
    arduino::SetLed,
)
InputModule_strategy = st.builds(
    InputModule,
)
arduino::ModuleSet_strategy = st.builds(
    arduino::ModuleSet,
)
arduino::PushButton_strategy = st.builds(
    arduino::PushButton,
)
OutputModule_strategy = st.builds(
    OutputModule,
)
arduino::Led_strategy = st.builds(
    arduino::Led,
)
Module_strategy = st.builds(
    Module,
)
arduino::InputModule_strategy = st.builds(
    arduino::InputModule,
)
arduino::OutputModule_strategy = st.builds(
    arduino::OutputModule,
)

@given(instance=arduino::Instruction_strategy)
@settings(max_examples=50)
def test_arduino::instruction_instantiation(instance):
    assert isinstance(instance, arduino::Instruction)

@given(instance=arduino::Block_strategy)
@settings(max_examples=50)
def test_arduino::block_instantiation(instance):
    assert isinstance(instance, arduino::Block)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=arduino::Module_strategy)
@settings(max_examples=50)
def test_arduino::module_instantiation(instance):
    assert isinstance(instance, arduino::Module)

@given(instance=arduino::Board_strategy)
@settings(max_examples=50)
def test_arduino::board_instantiation(instance):
    assert isinstance(instance, arduino::Board)

@given(instance=arduino::Sketch_strategy)
@settings(max_examples=50)
def test_arduino::sketch_instantiation(instance):
    assert isinstance(instance, arduino::Sketch)

@given(instance=arduino::Project_strategy)
@settings(max_examples=50)
def test_arduino::project_instantiation(instance):
    assert isinstance(instance, arduino::Project)

@given(instance=arduino::NamedElement_strategy)
@settings(max_examples=50)
def test_arduino::namedelement_instantiation(instance):
    assert isinstance(instance, arduino::NamedElement)

@given(instance=arduino::NamedElement_strategy)
def test_arduino::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduino::NamedElement_strategy)
def test_arduino::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=arduino::BinaryExpression_strategy)
@settings(max_examples=50)
def test_arduino::binaryexpression_instantiation(instance):
    assert isinstance(instance, arduino::BinaryExpression)

@given(instance=arduino::BinaryExpression_strategy)
def test_arduino::binaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=arduino::BinaryExpression_strategy)
def test_arduino::binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=arduino::UnaryExpression_strategy)
@settings(max_examples=50)
def test_arduino::unaryexpression_instantiation(instance):
    assert isinstance(instance, arduino::UnaryExpression)

@given(instance=arduino::UnaryExpression_strategy)
def test_arduino::unaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=arduino::UnaryExpression_strategy)
def test_arduino::unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=arduino::Constant_strategy)
@settings(max_examples=50)
def test_arduino::constant_instantiation(instance):
    assert isinstance(instance, arduino::Constant)

@given(instance=arduino::Constant_strategy)
def test_arduino::constant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=arduino::Constant_strategy)
def test_arduino::constant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduino::ModuleGet_strategy)
@settings(max_examples=50)
def test_arduino::moduleget_instantiation(instance):
    assert isinstance(instance, arduino::ModuleGet)

@given(instance=arduino::Expression_strategy)
@settings(max_examples=50)
def test_arduino::expression_instantiation(instance):
    assert isinstance(instance, arduino::Expression)

@given(instance=Control_strategy)
@settings(max_examples=50)
def test_control_instantiation(instance):
    assert isinstance(instance, Control)

@given(instance=arduino::While_strategy)
@settings(max_examples=50)
def test_arduino::while_instantiation(instance):
    assert isinstance(instance, arduino::While)

@given(instance=arduino::If_strategy)
@settings(max_examples=50)
def test_arduino::if_instantiation(instance):
    assert isinstance(instance, arduino::If)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=arduino::Delay_strategy)
@settings(max_examples=50)
def test_arduino::delay_instantiation(instance):
    assert isinstance(instance, arduino::Delay)

@given(instance=arduino::Delay_strategy)
def test_arduino::delay_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=arduino::Delay_strategy)
def test_arduino::delay_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduino::WaitFor_strategy)
@settings(max_examples=50)
def test_arduino::waitfor_instantiation(instance):
    assert isinstance(instance, arduino::WaitFor)

@given(instance=arduino::Control_strategy)
@settings(max_examples=50)
def test_arduino::control_instantiation(instance):
    assert isinstance(instance, arduino::Control)

@given(instance=ModuleSet_strategy)
@settings(max_examples=50)
def test_moduleset_instantiation(instance):
    assert isinstance(instance, ModuleSet)

@given(instance=arduino::SetLed_strategy)
@settings(max_examples=50)
def test_arduino::setled_instantiation(instance):
    assert isinstance(instance, arduino::SetLed)

@given(instance=InputModule_strategy)
@settings(max_examples=50)
def test_inputmodule_instantiation(instance):
    assert isinstance(instance, InputModule)

@given(instance=arduino::ModuleSet_strategy)
@settings(max_examples=50)
def test_arduino::moduleset_instantiation(instance):
    assert isinstance(instance, arduino::ModuleSet)

@given(instance=arduino::PushButton_strategy)
@settings(max_examples=50)
def test_arduino::pushbutton_instantiation(instance):
    assert isinstance(instance, arduino::PushButton)

@given(instance=OutputModule_strategy)
@settings(max_examples=50)
def test_outputmodule_instantiation(instance):
    assert isinstance(instance, OutputModule)

@given(instance=arduino::Led_strategy)
@settings(max_examples=50)
def test_arduino::led_instantiation(instance):
    assert isinstance(instance, arduino::Led)

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=arduino::InputModule_strategy)
@settings(max_examples=50)
def test_arduino::inputmodule_instantiation(instance):
    assert isinstance(instance, arduino::InputModule)

@given(instance=arduino::OutputModule_strategy)
@settings(max_examples=50)
def test_arduino::outputmodule_instantiation(instance):
    assert isinstance(instance, arduino::OutputModule)
