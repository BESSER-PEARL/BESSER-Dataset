import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    logoASM::LogoProgram,
    BinaryExp,
    logoASM::Lower,
    logoASM::Div,
    logoASM::Greater,
    logoASM::Equals,
    logoASM::Mult,
    logoASM::Minus,
    logoASM::Plus,
    Expression,
    logoASM::ParameterCall,
    logoASM::BinaryExp,
    ControlStructure,
    logoASM::While,
    logoASM::Repeat,
    logoASM::If,
    logoASM::Parameter,
    logoASM::ProcCall,
    logoASM::Constant,
    Primitive,
    logoASM::Clear,
    logoASM::PenDown,
    logoASM::Forward,
    logoASM::Right,
    logoASM::Left,
    logoASM::PenUp,
    logoASM::Back,
    Instruction,
    logoASM::ProcDeclaration,
    logoASM::Block,
    logoASM::ControlStructure,
    logoASM::Expression,
    logoASM::Primitive,
    logoASM::Instruction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_logoasm::logoprogram_is_not_abstract():
    assert not inspect.isabstract(logoASM::LogoProgram)


def test_logoasm::logoprogram_constructor_exists():
    assert callable(logoASM::LogoProgram.__init__)


def test_logoasm::logoprogram_constructor_args():
    sig = inspect.signature(logoASM::LogoProgram.__init__)
    params = list(sig.parameters.keys())



def test_binaryexp_is_not_abstract():
    assert not inspect.isabstract(BinaryExp)


def test_binaryexp_constructor_exists():
    assert callable(BinaryExp.__init__)


def test_binaryexp_constructor_args():
    sig = inspect.signature(BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::lower_is_not_abstract():
    assert not inspect.isabstract(logoASM::Lower)


def test_logoasm::lower_constructor_exists():
    assert callable(logoASM::Lower.__init__)


def test_logoasm::lower_constructor_args():
    sig = inspect.signature(logoASM::Lower.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::div_is_not_abstract():
    assert not inspect.isabstract(logoASM::Div)


def test_logoasm::div_constructor_exists():
    assert callable(logoASM::Div.__init__)


def test_logoasm::div_constructor_args():
    sig = inspect.signature(logoASM::Div.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::greater_is_not_abstract():
    assert not inspect.isabstract(logoASM::Greater)


def test_logoasm::greater_constructor_exists():
    assert callable(logoASM::Greater.__init__)


def test_logoasm::greater_constructor_args():
    sig = inspect.signature(logoASM::Greater.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::equals_is_not_abstract():
    assert not inspect.isabstract(logoASM::Equals)


def test_logoasm::equals_constructor_exists():
    assert callable(logoASM::Equals.__init__)


def test_logoasm::equals_constructor_args():
    sig = inspect.signature(logoASM::Equals.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::mult_is_not_abstract():
    assert not inspect.isabstract(logoASM::Mult)


def test_logoasm::mult_constructor_exists():
    assert callable(logoASM::Mult.__init__)


def test_logoasm::mult_constructor_args():
    sig = inspect.signature(logoASM::Mult.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::minus_is_not_abstract():
    assert not inspect.isabstract(logoASM::Minus)


def test_logoasm::minus_constructor_exists():
    assert callable(logoASM::Minus.__init__)


def test_logoasm::minus_constructor_args():
    sig = inspect.signature(logoASM::Minus.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::plus_is_not_abstract():
    assert not inspect.isabstract(logoASM::Plus)


def test_logoasm::plus_constructor_exists():
    assert callable(logoASM::Plus.__init__)


def test_logoasm::plus_constructor_args():
    sig = inspect.signature(logoASM::Plus.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::parametercall_is_not_abstract():
    assert not inspect.isabstract(logoASM::ParameterCall)


def test_logoasm::parametercall_constructor_exists():
    assert callable(logoASM::ParameterCall.__init__)


def test_logoasm::parametercall_constructor_args():
    sig = inspect.signature(logoASM::ParameterCall.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::binaryexp_is_not_abstract():
    assert not inspect.isabstract(logoASM::BinaryExp)


def test_logoasm::binaryexp_constructor_exists():
    assert callable(logoASM::BinaryExp.__init__)


def test_logoasm::binaryexp_constructor_args():
    sig = inspect.signature(logoASM::BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_controlstructure_is_not_abstract():
    assert not inspect.isabstract(ControlStructure)


def test_controlstructure_constructor_exists():
    assert callable(ControlStructure.__init__)


def test_controlstructure_constructor_args():
    sig = inspect.signature(ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::while_is_not_abstract():
    assert not inspect.isabstract(logoASM::While)


def test_logoasm::while_constructor_exists():
    assert callable(logoASM::While.__init__)


def test_logoasm::while_constructor_args():
    sig = inspect.signature(logoASM::While.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::repeat_is_not_abstract():
    assert not inspect.isabstract(logoASM::Repeat)


def test_logoasm::repeat_constructor_exists():
    assert callable(logoASM::Repeat.__init__)


def test_logoasm::repeat_constructor_args():
    sig = inspect.signature(logoASM::Repeat.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::if_is_not_abstract():
    assert not inspect.isabstract(logoASM::If)


def test_logoasm::if_constructor_exists():
    assert callable(logoASM::If.__init__)


def test_logoasm::if_constructor_args():
    sig = inspect.signature(logoASM::If.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::parameter_is_not_abstract():
    assert not inspect.isabstract(logoASM::Parameter)


def test_logoasm::parameter_constructor_exists():
    assert callable(logoASM::Parameter.__init__)


def test_logoasm::parameter_constructor_args():
    sig = inspect.signature(logoASM::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logoasm::parameter_has_name():
    assert hasattr(logoASM::Parameter, "name")
    descriptor = None
    for klass in logoASM::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logoasm::proccall_is_not_abstract():
    assert not inspect.isabstract(logoASM::ProcCall)


def test_logoasm::proccall_constructor_exists():
    assert callable(logoASM::ProcCall.__init__)


def test_logoasm::proccall_constructor_args():
    sig = inspect.signature(logoASM::ProcCall.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::constant_is_not_abstract():
    assert not inspect.isabstract(logoASM::Constant)


def test_logoasm::constant_constructor_exists():
    assert callable(logoASM::Constant.__init__)


def test_logoasm::constant_constructor_args():
    sig = inspect.signature(logoASM::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "integerValue" in params, "Missing parameter 'integerValue'"

def test_logoasm::constant_has_integerValue():
    assert hasattr(logoASM::Constant, "integerValue")
    descriptor = None
    for klass in logoASM::Constant.__mro__:
        if "integerValue" in klass.__dict__:
            descriptor = klass.__dict__["integerValue"]
            break
    assert isinstance(descriptor, property)



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::clear_is_not_abstract():
    assert not inspect.isabstract(logoASM::Clear)


def test_logoasm::clear_constructor_exists():
    assert callable(logoASM::Clear.__init__)


def test_logoasm::clear_constructor_args():
    sig = inspect.signature(logoASM::Clear.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::pendown_is_not_abstract():
    assert not inspect.isabstract(logoASM::PenDown)


def test_logoasm::pendown_constructor_exists():
    assert callable(logoASM::PenDown.__init__)


def test_logoasm::pendown_constructor_args():
    sig = inspect.signature(logoASM::PenDown.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::forward_is_not_abstract():
    assert not inspect.isabstract(logoASM::Forward)


def test_logoasm::forward_constructor_exists():
    assert callable(logoASM::Forward.__init__)


def test_logoasm::forward_constructor_args():
    sig = inspect.signature(logoASM::Forward.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::right_is_not_abstract():
    assert not inspect.isabstract(logoASM::Right)


def test_logoasm::right_constructor_exists():
    assert callable(logoASM::Right.__init__)


def test_logoasm::right_constructor_args():
    sig = inspect.signature(logoASM::Right.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::left_is_not_abstract():
    assert not inspect.isabstract(logoASM::Left)


def test_logoasm::left_constructor_exists():
    assert callable(logoASM::Left.__init__)


def test_logoasm::left_constructor_args():
    sig = inspect.signature(logoASM::Left.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::penup_is_not_abstract():
    assert not inspect.isabstract(logoASM::PenUp)


def test_logoasm::penup_constructor_exists():
    assert callable(logoASM::PenUp.__init__)


def test_logoasm::penup_constructor_args():
    sig = inspect.signature(logoASM::PenUp.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::back_is_not_abstract():
    assert not inspect.isabstract(logoASM::Back)


def test_logoasm::back_constructor_exists():
    assert callable(logoASM::Back.__init__)


def test_logoasm::back_constructor_args():
    sig = inspect.signature(logoASM::Back.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::procdeclaration_is_not_abstract():
    assert not inspect.isabstract(logoASM::ProcDeclaration)


def test_logoasm::procdeclaration_constructor_exists():
    assert callable(logoASM::ProcDeclaration.__init__)


def test_logoasm::procdeclaration_constructor_args():
    sig = inspect.signature(logoASM::ProcDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logoasm::procdeclaration_has_name():
    assert hasattr(logoASM::ProcDeclaration, "name")
    descriptor = None
    for klass in logoASM::ProcDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logoasm::block_is_not_abstract():
    assert not inspect.isabstract(logoASM::Block)


def test_logoasm::block_constructor_exists():
    assert callable(logoASM::Block.__init__)


def test_logoasm::block_constructor_args():
    sig = inspect.signature(logoASM::Block.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::controlstructure_is_not_abstract():
    assert not inspect.isabstract(logoASM::ControlStructure)


def test_logoasm::controlstructure_constructor_exists():
    assert callable(logoASM::ControlStructure.__init__)


def test_logoasm::controlstructure_constructor_args():
    sig = inspect.signature(logoASM::ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::expression_is_not_abstract():
    assert not inspect.isabstract(logoASM::Expression)


def test_logoasm::expression_constructor_exists():
    assert callable(logoASM::Expression.__init__)


def test_logoasm::expression_constructor_args():
    sig = inspect.signature(logoASM::Expression.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::primitive_is_not_abstract():
    assert not inspect.isabstract(logoASM::Primitive)


def test_logoasm::primitive_constructor_exists():
    assert callable(logoASM::Primitive.__init__)


def test_logoasm::primitive_constructor_args():
    sig = inspect.signature(logoASM::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_logoasm::instruction_is_not_abstract():
    assert not inspect.isabstract(logoASM::Instruction)


def test_logoasm::instruction_constructor_exists():
    assert callable(logoASM::Instruction.__init__)


def test_logoasm::instruction_constructor_args():
    sig = inspect.signature(logoASM::Instruction.__init__)
    params = list(sig.parameters.keys())


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
logoASM::LogoProgram_strategy = st.builds(
    logoASM::LogoProgram,
)
BinaryExp_strategy = st.builds(
    BinaryExp,
)
logoASM::Lower_strategy = st.builds(
    logoASM::Lower,
)
logoASM::Div_strategy = st.builds(
    logoASM::Div,
)
logoASM::Greater_strategy = st.builds(
    logoASM::Greater,
)
logoASM::Equals_strategy = st.builds(
    logoASM::Equals,
)
logoASM::Mult_strategy = st.builds(
    logoASM::Mult,
)
logoASM::Minus_strategy = st.builds(
    logoASM::Minus,
)
logoASM::Plus_strategy = st.builds(
    logoASM::Plus,
)
Expression_strategy = st.builds(
    Expression,
)
logoASM::ParameterCall_strategy = st.builds(
    logoASM::ParameterCall,
)
logoASM::BinaryExp_strategy = st.builds(
    logoASM::BinaryExp,
)
ControlStructure_strategy = st.builds(
    ControlStructure,
)
logoASM::While_strategy = st.builds(
    logoASM::While,
)
logoASM::Repeat_strategy = st.builds(
    logoASM::Repeat,
)
logoASM::If_strategy = st.builds(
    logoASM::If,
)
logoASM::Parameter_strategy = st.builds(
    logoASM::Parameter,
    name=
        safe_text
)
logoASM::ProcCall_strategy = st.builds(
    logoASM::ProcCall,
)
logoASM::Constant_strategy = st.builds(
    logoASM::Constant,
    integerValue=
        st.integers()
)
Primitive_strategy = st.builds(
    Primitive,
)
logoASM::Clear_strategy = st.builds(
    logoASM::Clear,
)
logoASM::PenDown_strategy = st.builds(
    logoASM::PenDown,
)
logoASM::Forward_strategy = st.builds(
    logoASM::Forward,
)
logoASM::Right_strategy = st.builds(
    logoASM::Right,
)
logoASM::Left_strategy = st.builds(
    logoASM::Left,
)
logoASM::PenUp_strategy = st.builds(
    logoASM::PenUp,
)
logoASM::Back_strategy = st.builds(
    logoASM::Back,
)
Instruction_strategy = st.builds(
    Instruction,
)
logoASM::ProcDeclaration_strategy = st.builds(
    logoASM::ProcDeclaration,
    name=
        safe_text
)
logoASM::Block_strategy = st.builds(
    logoASM::Block,
)
logoASM::ControlStructure_strategy = st.builds(
    logoASM::ControlStructure,
)
logoASM::Expression_strategy = st.builds(
    logoASM::Expression,
)
logoASM::Primitive_strategy = st.builds(
    logoASM::Primitive,
)
logoASM::Instruction_strategy = st.builds(
    logoASM::Instruction,
)

@given(instance=logoASM::LogoProgram_strategy)
@settings(max_examples=50)
def test_logoasm::logoprogram_instantiation(instance):
    assert isinstance(instance, logoASM::LogoProgram)

@given(instance=BinaryExp_strategy)
@settings(max_examples=50)
def test_binaryexp_instantiation(instance):
    assert isinstance(instance, BinaryExp)

@given(instance=logoASM::Lower_strategy)
@settings(max_examples=50)
def test_logoasm::lower_instantiation(instance):
    assert isinstance(instance, logoASM::Lower)

@given(instance=logoASM::Div_strategy)
@settings(max_examples=50)
def test_logoasm::div_instantiation(instance):
    assert isinstance(instance, logoASM::Div)

@given(instance=logoASM::Greater_strategy)
@settings(max_examples=50)
def test_logoasm::greater_instantiation(instance):
    assert isinstance(instance, logoASM::Greater)

@given(instance=logoASM::Equals_strategy)
@settings(max_examples=50)
def test_logoasm::equals_instantiation(instance):
    assert isinstance(instance, logoASM::Equals)

@given(instance=logoASM::Mult_strategy)
@settings(max_examples=50)
def test_logoasm::mult_instantiation(instance):
    assert isinstance(instance, logoASM::Mult)

@given(instance=logoASM::Minus_strategy)
@settings(max_examples=50)
def test_logoasm::minus_instantiation(instance):
    assert isinstance(instance, logoASM::Minus)

@given(instance=logoASM::Plus_strategy)
@settings(max_examples=50)
def test_logoasm::plus_instantiation(instance):
    assert isinstance(instance, logoASM::Plus)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=logoASM::ParameterCall_strategy)
@settings(max_examples=50)
def test_logoasm::parametercall_instantiation(instance):
    assert isinstance(instance, logoASM::ParameterCall)

@given(instance=logoASM::BinaryExp_strategy)
@settings(max_examples=50)
def test_logoasm::binaryexp_instantiation(instance):
    assert isinstance(instance, logoASM::BinaryExp)

@given(instance=ControlStructure_strategy)
@settings(max_examples=50)
def test_controlstructure_instantiation(instance):
    assert isinstance(instance, ControlStructure)

@given(instance=logoASM::While_strategy)
@settings(max_examples=50)
def test_logoasm::while_instantiation(instance):
    assert isinstance(instance, logoASM::While)

@given(instance=logoASM::Repeat_strategy)
@settings(max_examples=50)
def test_logoasm::repeat_instantiation(instance):
    assert isinstance(instance, logoASM::Repeat)

@given(instance=logoASM::If_strategy)
@settings(max_examples=50)
def test_logoasm::if_instantiation(instance):
    assert isinstance(instance, logoASM::If)

@given(instance=logoASM::Parameter_strategy)
@settings(max_examples=50)
def test_logoasm::parameter_instantiation(instance):
    assert isinstance(instance, logoASM::Parameter)

@given(instance=logoASM::Parameter_strategy)
def test_logoasm::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=logoASM::Parameter_strategy)
def test_logoasm::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logoASM::ProcCall_strategy)
@settings(max_examples=50)
def test_logoasm::proccall_instantiation(instance):
    assert isinstance(instance, logoASM::ProcCall)

@given(instance=logoASM::Constant_strategy)
@settings(max_examples=50)
def test_logoasm::constant_instantiation(instance):
    assert isinstance(instance, logoASM::Constant)

@given(instance=logoASM::Constant_strategy)
def test_logoasm::constant_integerValue_type(instance):
    assert isinstance(instance.integerValue, int)


@given(instance=logoASM::Constant_strategy)
def test_logoasm::constant_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=logoASM::Clear_strategy)
@settings(max_examples=50)
def test_logoasm::clear_instantiation(instance):
    assert isinstance(instance, logoASM::Clear)

@given(instance=logoASM::PenDown_strategy)
@settings(max_examples=50)
def test_logoasm::pendown_instantiation(instance):
    assert isinstance(instance, logoASM::PenDown)

@given(instance=logoASM::Forward_strategy)
@settings(max_examples=50)
def test_logoasm::forward_instantiation(instance):
    assert isinstance(instance, logoASM::Forward)

@given(instance=logoASM::Right_strategy)
@settings(max_examples=50)
def test_logoasm::right_instantiation(instance):
    assert isinstance(instance, logoASM::Right)

@given(instance=logoASM::Left_strategy)
@settings(max_examples=50)
def test_logoasm::left_instantiation(instance):
    assert isinstance(instance, logoASM::Left)

@given(instance=logoASM::PenUp_strategy)
@settings(max_examples=50)
def test_logoasm::penup_instantiation(instance):
    assert isinstance(instance, logoASM::PenUp)

@given(instance=logoASM::Back_strategy)
@settings(max_examples=50)
def test_logoasm::back_instantiation(instance):
    assert isinstance(instance, logoASM::Back)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=logoASM::ProcDeclaration_strategy)
@settings(max_examples=50)
def test_logoasm::procdeclaration_instantiation(instance):
    assert isinstance(instance, logoASM::ProcDeclaration)

@given(instance=logoASM::ProcDeclaration_strategy)
def test_logoasm::procdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=logoASM::ProcDeclaration_strategy)
def test_logoasm::procdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logoASM::Block_strategy)
@settings(max_examples=50)
def test_logoasm::block_instantiation(instance):
    assert isinstance(instance, logoASM::Block)

@given(instance=logoASM::ControlStructure_strategy)
@settings(max_examples=50)
def test_logoasm::controlstructure_instantiation(instance):
    assert isinstance(instance, logoASM::ControlStructure)

@given(instance=logoASM::Expression_strategy)
@settings(max_examples=50)
def test_logoasm::expression_instantiation(instance):
    assert isinstance(instance, logoASM::Expression)

@given(instance=logoASM::Primitive_strategy)
@settings(max_examples=50)
def test_logoasm::primitive_instantiation(instance):
    assert isinstance(instance, logoASM::Primitive)

@given(instance=logoASM::Instruction_strategy)
@settings(max_examples=50)
def test_logoasm::instruction_instantiation(instance):
    assert isinstance(instance, logoASM::Instruction)
