import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Block,
    ControlStructure,
    kmLogo::ASM::If,
    kmLogo::ASM::LogoProgram,
    ProcCall,
    Parameter,
    BinaryExp,
    kmLogo::ASM::Mult,
    kmLogo::ASM::Lower,
    kmLogo::ASM::Greater,
    kmLogo::ASM::Equals,
    kmLogo::ASM::Minus,
    kmLogo::ASM::Div,
    kmLogo::ASM::Plus,
    kmLogo::ASM::Parameter,
    kmLogo::ASM::While,
    kmLogo::ASM::Repeat,
    Expression,
    kmLogo::ASM::ParameterCall,
    kmLogo::ASM::BinaryExp,
    ProcDeclaration,
    kmLogo::ASM::ProcCall,
    kmLogo::ASM::Constant,
    Primitive,
    kmLogo::ASM::Clear,
    kmLogo::ASM::Forward,
    kmLogo::ASM::PenUp,
    kmLogo::ASM::Left,
    kmLogo::ASM::Right,
    kmLogo::ASM::PenDown,
    kmLogo::ASM::Back,
    Instruction,
    kmLogo::ASM::ControlStructure,
    kmLogo::ASM::Block,
    kmLogo::ASM::Expression,
    kmLogo::ASM::ProcDeclaration,
    kmLogo::ASM::Primitive,
    kmLogo::ASM::Instruction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_controlstructure_is_not_abstract():
    assert not inspect.isabstract(ControlStructure)


def test_controlstructure_constructor_exists():
    assert callable(ControlStructure.__init__)


def test_controlstructure_constructor_args():
    sig = inspect.signature(ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::if_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::If)


def test_kmlogo::asm::if_constructor_exists():
    assert callable(kmLogo::ASM::If.__init__)


def test_kmlogo::asm::if_constructor_args():
    sig = inspect.signature(kmLogo::ASM::If.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::logoprogram_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::LogoProgram)


def test_kmlogo::asm::logoprogram_constructor_exists():
    assert callable(kmLogo::ASM::LogoProgram.__init__)


def test_kmlogo::asm::logoprogram_constructor_args():
    sig = inspect.signature(kmLogo::ASM::LogoProgram.__init__)
    params = list(sig.parameters.keys())



def test_proccall_is_not_abstract():
    assert not inspect.isabstract(ProcCall)


def test_proccall_constructor_exists():
    assert callable(ProcCall.__init__)


def test_proccall_constructor_args():
    sig = inspect.signature(ProcCall.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_binaryexp_is_not_abstract():
    assert not inspect.isabstract(BinaryExp)


def test_binaryexp_constructor_exists():
    assert callable(BinaryExp.__init__)


def test_binaryexp_constructor_args():
    sig = inspect.signature(BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::mult_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Mult)


def test_kmlogo::asm::mult_constructor_exists():
    assert callable(kmLogo::ASM::Mult.__init__)


def test_kmlogo::asm::mult_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Mult.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::lower_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Lower)


def test_kmlogo::asm::lower_constructor_exists():
    assert callable(kmLogo::ASM::Lower.__init__)


def test_kmlogo::asm::lower_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Lower.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::greater_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Greater)


def test_kmlogo::asm::greater_constructor_exists():
    assert callable(kmLogo::ASM::Greater.__init__)


def test_kmlogo::asm::greater_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Greater.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::equals_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Equals)


def test_kmlogo::asm::equals_constructor_exists():
    assert callable(kmLogo::ASM::Equals.__init__)


def test_kmlogo::asm::equals_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Equals.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::minus_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Minus)


def test_kmlogo::asm::minus_constructor_exists():
    assert callable(kmLogo::ASM::Minus.__init__)


def test_kmlogo::asm::minus_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Minus.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::div_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Div)


def test_kmlogo::asm::div_constructor_exists():
    assert callable(kmLogo::ASM::Div.__init__)


def test_kmlogo::asm::div_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Div.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::plus_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Plus)


def test_kmlogo::asm::plus_constructor_exists():
    assert callable(kmLogo::ASM::Plus.__init__)


def test_kmlogo::asm::plus_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Plus.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::parameter_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Parameter)


def test_kmlogo::asm::parameter_constructor_exists():
    assert callable(kmLogo::ASM::Parameter.__init__)


def test_kmlogo::asm::parameter_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kmlogo::asm::parameter_has_name():
    assert hasattr(kmLogo::ASM::Parameter, "name")
    descriptor = None
    for klass in kmLogo::ASM::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo::asm::while_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::While)


def test_kmlogo::asm::while_constructor_exists():
    assert callable(kmLogo::ASM::While.__init__)


def test_kmlogo::asm::while_constructor_args():
    sig = inspect.signature(kmLogo::ASM::While.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::repeat_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Repeat)


def test_kmlogo::asm::repeat_constructor_exists():
    assert callable(kmLogo::ASM::Repeat.__init__)


def test_kmlogo::asm::repeat_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Repeat.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::parametercall_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::ParameterCall)


def test_kmlogo::asm::parametercall_constructor_exists():
    assert callable(kmLogo::ASM::ParameterCall.__init__)


def test_kmlogo::asm::parametercall_constructor_args():
    sig = inspect.signature(kmLogo::ASM::ParameterCall.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::binaryexp_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::BinaryExp)


def test_kmlogo::asm::binaryexp_constructor_exists():
    assert callable(kmLogo::ASM::BinaryExp.__init__)


def test_kmlogo::asm::binaryexp_constructor_args():
    sig = inspect.signature(kmLogo::ASM::BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_procdeclaration_is_not_abstract():
    assert not inspect.isabstract(ProcDeclaration)


def test_procdeclaration_constructor_exists():
    assert callable(ProcDeclaration.__init__)


def test_procdeclaration_constructor_args():
    sig = inspect.signature(ProcDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::proccall_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::ProcCall)


def test_kmlogo::asm::proccall_constructor_exists():
    assert callable(kmLogo::ASM::ProcCall.__init__)


def test_kmlogo::asm::proccall_constructor_args():
    sig = inspect.signature(kmLogo::ASM::ProcCall.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::constant_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Constant)


def test_kmlogo::asm::constant_constructor_exists():
    assert callable(kmLogo::ASM::Constant.__init__)


def test_kmlogo::asm::constant_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "integerValue" in params, "Missing parameter 'integerValue'"

def test_kmlogo::asm::constant_has_integerValue():
    assert hasattr(kmLogo::ASM::Constant, "integerValue")
    descriptor = None
    for klass in kmLogo::ASM::Constant.__mro__:
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



def test_kmlogo::asm::clear_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Clear)


def test_kmlogo::asm::clear_constructor_exists():
    assert callable(kmLogo::ASM::Clear.__init__)


def test_kmlogo::asm::clear_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Clear.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::forward_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Forward)


def test_kmlogo::asm::forward_constructor_exists():
    assert callable(kmLogo::ASM::Forward.__init__)


def test_kmlogo::asm::forward_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Forward.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::penup_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::PenUp)


def test_kmlogo::asm::penup_constructor_exists():
    assert callable(kmLogo::ASM::PenUp.__init__)


def test_kmlogo::asm::penup_constructor_args():
    sig = inspect.signature(kmLogo::ASM::PenUp.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::left_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Left)


def test_kmlogo::asm::left_constructor_exists():
    assert callable(kmLogo::ASM::Left.__init__)


def test_kmlogo::asm::left_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Left.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::right_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Right)


def test_kmlogo::asm::right_constructor_exists():
    assert callable(kmLogo::ASM::Right.__init__)


def test_kmlogo::asm::right_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Right.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::pendown_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::PenDown)


def test_kmlogo::asm::pendown_constructor_exists():
    assert callable(kmLogo::ASM::PenDown.__init__)


def test_kmlogo::asm::pendown_constructor_args():
    sig = inspect.signature(kmLogo::ASM::PenDown.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::back_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Back)


def test_kmlogo::asm::back_constructor_exists():
    assert callable(kmLogo::ASM::Back.__init__)


def test_kmlogo::asm::back_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Back.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::controlstructure_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::ControlStructure)


def test_kmlogo::asm::controlstructure_constructor_exists():
    assert callable(kmLogo::ASM::ControlStructure.__init__)


def test_kmlogo::asm::controlstructure_constructor_args():
    sig = inspect.signature(kmLogo::ASM::ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::block_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Block)


def test_kmlogo::asm::block_constructor_exists():
    assert callable(kmLogo::ASM::Block.__init__)


def test_kmlogo::asm::block_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Block.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::expression_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Expression)


def test_kmlogo::asm::expression_constructor_exists():
    assert callable(kmLogo::ASM::Expression.__init__)


def test_kmlogo::asm::expression_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Expression.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::procdeclaration_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::ProcDeclaration)


def test_kmlogo::asm::procdeclaration_constructor_exists():
    assert callable(kmLogo::ASM::ProcDeclaration.__init__)


def test_kmlogo::asm::procdeclaration_constructor_args():
    sig = inspect.signature(kmLogo::ASM::ProcDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kmlogo::asm::procdeclaration_has_name():
    assert hasattr(kmLogo::ASM::ProcDeclaration, "name")
    descriptor = None
    for klass in kmLogo::ASM::ProcDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo::asm::primitive_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Primitive)


def test_kmlogo::asm::primitive_constructor_exists():
    assert callable(kmLogo::ASM::Primitive.__init__)


def test_kmlogo::asm::primitive_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::instruction_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ASM::Instruction)


def test_kmlogo::asm::instruction_constructor_exists():
    assert callable(kmLogo::ASM::Instruction.__init__)


def test_kmlogo::asm::instruction_constructor_args():
    sig = inspect.signature(kmLogo::ASM::Instruction.__init__)
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
Block_strategy = st.builds(
    Block,
)
ControlStructure_strategy = st.builds(
    ControlStructure,
)
kmLogo::ASM::If_strategy = st.builds(
    kmLogo::ASM::If,
)
kmLogo::ASM::LogoProgram_strategy = st.builds(
    kmLogo::ASM::LogoProgram,
)
ProcCall_strategy = st.builds(
    ProcCall,
)
Parameter_strategy = st.builds(
    Parameter,
)
BinaryExp_strategy = st.builds(
    BinaryExp,
)
kmLogo::ASM::Mult_strategy = st.builds(
    kmLogo::ASM::Mult,
)
kmLogo::ASM::Lower_strategy = st.builds(
    kmLogo::ASM::Lower,
)
kmLogo::ASM::Greater_strategy = st.builds(
    kmLogo::ASM::Greater,
)
kmLogo::ASM::Equals_strategy = st.builds(
    kmLogo::ASM::Equals,
)
kmLogo::ASM::Minus_strategy = st.builds(
    kmLogo::ASM::Minus,
)
kmLogo::ASM::Div_strategy = st.builds(
    kmLogo::ASM::Div,
)
kmLogo::ASM::Plus_strategy = st.builds(
    kmLogo::ASM::Plus,
)
kmLogo::ASM::Parameter_strategy = st.builds(
    kmLogo::ASM::Parameter,
    name=
        safe_text
)
kmLogo::ASM::While_strategy = st.builds(
    kmLogo::ASM::While,
)
kmLogo::ASM::Repeat_strategy = st.builds(
    kmLogo::ASM::Repeat,
)
Expression_strategy = st.builds(
    Expression,
)
kmLogo::ASM::ParameterCall_strategy = st.builds(
    kmLogo::ASM::ParameterCall,
)
kmLogo::ASM::BinaryExp_strategy = st.builds(
    kmLogo::ASM::BinaryExp,
)
ProcDeclaration_strategy = st.builds(
    ProcDeclaration,
)
kmLogo::ASM::ProcCall_strategy = st.builds(
    kmLogo::ASM::ProcCall,
)
kmLogo::ASM::Constant_strategy = st.builds(
    kmLogo::ASM::Constant,
    integerValue=
        safe_text
)
Primitive_strategy = st.builds(
    Primitive,
)
kmLogo::ASM::Clear_strategy = st.builds(
    kmLogo::ASM::Clear,
)
kmLogo::ASM::Forward_strategy = st.builds(
    kmLogo::ASM::Forward,
)
kmLogo::ASM::PenUp_strategy = st.builds(
    kmLogo::ASM::PenUp,
)
kmLogo::ASM::Left_strategy = st.builds(
    kmLogo::ASM::Left,
)
kmLogo::ASM::Right_strategy = st.builds(
    kmLogo::ASM::Right,
)
kmLogo::ASM::PenDown_strategy = st.builds(
    kmLogo::ASM::PenDown,
)
kmLogo::ASM::Back_strategy = st.builds(
    kmLogo::ASM::Back,
)
Instruction_strategy = st.builds(
    Instruction,
)
kmLogo::ASM::ControlStructure_strategy = st.builds(
    kmLogo::ASM::ControlStructure,
)
kmLogo::ASM::Block_strategy = st.builds(
    kmLogo::ASM::Block,
)
kmLogo::ASM::Expression_strategy = st.builds(
    kmLogo::ASM::Expression,
)
kmLogo::ASM::ProcDeclaration_strategy = st.builds(
    kmLogo::ASM::ProcDeclaration,
    name=
        safe_text
)
kmLogo::ASM::Primitive_strategy = st.builds(
    kmLogo::ASM::Primitive,
)
kmLogo::ASM::Instruction_strategy = st.builds(
    kmLogo::ASM::Instruction,
)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=ControlStructure_strategy)
@settings(max_examples=50)
def test_controlstructure_instantiation(instance):
    assert isinstance(instance, ControlStructure)

@given(instance=kmLogo::ASM::If_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::if_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::If)

@given(instance=kmLogo::ASM::LogoProgram_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::logoprogram_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::LogoProgram)

@given(instance=ProcCall_strategy)
@settings(max_examples=50)
def test_proccall_instantiation(instance):
    assert isinstance(instance, ProcCall)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=BinaryExp_strategy)
@settings(max_examples=50)
def test_binaryexp_instantiation(instance):
    assert isinstance(instance, BinaryExp)

@given(instance=kmLogo::ASM::Mult_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::mult_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Mult)

@given(instance=kmLogo::ASM::Lower_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::lower_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Lower)

@given(instance=kmLogo::ASM::Greater_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::greater_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Greater)

@given(instance=kmLogo::ASM::Equals_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::equals_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Equals)

@given(instance=kmLogo::ASM::Minus_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::minus_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Minus)

@given(instance=kmLogo::ASM::Div_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::div_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Div)

@given(instance=kmLogo::ASM::Plus_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::plus_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Plus)

@given(instance=kmLogo::ASM::Parameter_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::parameter_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Parameter)

@given(instance=kmLogo::ASM::Parameter_strategy)
def test_kmlogo::asm::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kmLogo::ASM::Parameter_strategy)
def test_kmlogo::asm::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kmLogo::ASM::While_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::while_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::While)

@given(instance=kmLogo::ASM::Repeat_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::repeat_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Repeat)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=kmLogo::ASM::ParameterCall_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::parametercall_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::ParameterCall)

@given(instance=kmLogo::ASM::BinaryExp_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::binaryexp_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::BinaryExp)

@given(instance=ProcDeclaration_strategy)
@settings(max_examples=50)
def test_procdeclaration_instantiation(instance):
    assert isinstance(instance, ProcDeclaration)

@given(instance=kmLogo::ASM::ProcCall_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::proccall_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::ProcCall)

@given(instance=kmLogo::ASM::Constant_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::constant_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Constant)

@given(instance=kmLogo::ASM::Constant_strategy)
def test_kmlogo::asm::constant_integerValue_type(instance):
    assert isinstance(instance.integerValue, str)


@given(instance=kmLogo::ASM::Constant_strategy)
def test_kmlogo::asm::constant_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=kmLogo::ASM::Clear_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::clear_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Clear)

@given(instance=kmLogo::ASM::Forward_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::forward_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Forward)

@given(instance=kmLogo::ASM::PenUp_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::penup_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::PenUp)

@given(instance=kmLogo::ASM::Left_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::left_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Left)

@given(instance=kmLogo::ASM::Right_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::right_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Right)

@given(instance=kmLogo::ASM::PenDown_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::pendown_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::PenDown)

@given(instance=kmLogo::ASM::Back_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::back_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Back)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=kmLogo::ASM::ControlStructure_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::controlstructure_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::ControlStructure)

@given(instance=kmLogo::ASM::Block_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::block_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Block)

@given(instance=kmLogo::ASM::Expression_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::expression_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Expression)

@given(instance=kmLogo::ASM::ProcDeclaration_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::procdeclaration_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::ProcDeclaration)

@given(instance=kmLogo::ASM::ProcDeclaration_strategy)
def test_kmlogo::asm::procdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kmLogo::ASM::ProcDeclaration_strategy)
def test_kmlogo::asm::procdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kmLogo::ASM::Primitive_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::primitive_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Primitive)

@given(instance=kmLogo::ASM::Instruction_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::instruction_instantiation(instance):
    assert isinstance(instance, kmLogo::ASM::Instruction)
