import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    kmlogo::asm::LogoProgram,
    ProcCall,
    Parameter,
    BinaryExp,
    kmlogo::asm::Minus,
    kmlogo::asm::Mult,
    kmlogo::asm::Lower,
    kmlogo::asm::Div,
    kmlogo::asm::Equals,
    kmlogo::asm::Greater,
    kmlogo::asm::Plus,
    kmlogo::asm::Parameter,
    Block,
    ControlStructure,
    kmlogo::asm::Repeat,
    kmlogo::asm::While,
    kmlogo::asm::If,
    ProcDeclaration,
    Expression,
    kmlogo::asm::ProcCall,
    kmlogo::asm::Constant,
    kmlogo::asm::ParameterCall,
    kmlogo::asm::BinaryExp,
    Primitive,
    kmlogo::asm::PenUp,
    kmlogo::asm::Forward,
    kmlogo::asm::Right,
    kmlogo::asm::PenDown,
    kmlogo::asm::Clear,
    kmlogo::asm::Left,
    kmlogo::asm::Back,
    Instruction,
    kmlogo::asm::Block,
    kmlogo::asm::ProcDeclaration,
    kmlogo::asm::ControlStructure,
    kmlogo::asm::Expression,
    kmlogo::asm::Primitive,
    kmlogo::asm::Instruction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kmlogo::asm::logoprogram_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::LogoProgram)


def test_kmlogo::asm::logoprogram_constructor_exists():
    assert callable(kmlogo::asm::LogoProgram.__init__)


def test_kmlogo::asm::logoprogram_constructor_args():
    sig = inspect.signature(kmlogo::asm::LogoProgram.__init__)
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



def test_kmlogo::asm::minus_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Minus)


def test_kmlogo::asm::minus_constructor_exists():
    assert callable(kmlogo::asm::Minus.__init__)


def test_kmlogo::asm::minus_constructor_args():
    sig = inspect.signature(kmlogo::asm::Minus.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::mult_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Mult)


def test_kmlogo::asm::mult_constructor_exists():
    assert callable(kmlogo::asm::Mult.__init__)


def test_kmlogo::asm::mult_constructor_args():
    sig = inspect.signature(kmlogo::asm::Mult.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::lower_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Lower)


def test_kmlogo::asm::lower_constructor_exists():
    assert callable(kmlogo::asm::Lower.__init__)


def test_kmlogo::asm::lower_constructor_args():
    sig = inspect.signature(kmlogo::asm::Lower.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::div_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Div)


def test_kmlogo::asm::div_constructor_exists():
    assert callable(kmlogo::asm::Div.__init__)


def test_kmlogo::asm::div_constructor_args():
    sig = inspect.signature(kmlogo::asm::Div.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::equals_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Equals)


def test_kmlogo::asm::equals_constructor_exists():
    assert callable(kmlogo::asm::Equals.__init__)


def test_kmlogo::asm::equals_constructor_args():
    sig = inspect.signature(kmlogo::asm::Equals.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::greater_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Greater)


def test_kmlogo::asm::greater_constructor_exists():
    assert callable(kmlogo::asm::Greater.__init__)


def test_kmlogo::asm::greater_constructor_args():
    sig = inspect.signature(kmlogo::asm::Greater.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::plus_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Plus)


def test_kmlogo::asm::plus_constructor_exists():
    assert callable(kmlogo::asm::Plus.__init__)


def test_kmlogo::asm::plus_constructor_args():
    sig = inspect.signature(kmlogo::asm::Plus.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::parameter_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Parameter)


def test_kmlogo::asm::parameter_constructor_exists():
    assert callable(kmlogo::asm::Parameter.__init__)


def test_kmlogo::asm::parameter_constructor_args():
    sig = inspect.signature(kmlogo::asm::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kmlogo::asm::parameter_has_name():
    assert hasattr(kmlogo::asm::Parameter, "name")
    descriptor = None
    for klass in kmlogo::asm::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_kmlogo::asm::repeat_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Repeat)


def test_kmlogo::asm::repeat_constructor_exists():
    assert callable(kmlogo::asm::Repeat.__init__)


def test_kmlogo::asm::repeat_constructor_args():
    sig = inspect.signature(kmlogo::asm::Repeat.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::while_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::While)


def test_kmlogo::asm::while_constructor_exists():
    assert callable(kmlogo::asm::While.__init__)


def test_kmlogo::asm::while_constructor_args():
    sig = inspect.signature(kmlogo::asm::While.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::if_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::If)


def test_kmlogo::asm::if_constructor_exists():
    assert callable(kmlogo::asm::If.__init__)


def test_kmlogo::asm::if_constructor_args():
    sig = inspect.signature(kmlogo::asm::If.__init__)
    params = list(sig.parameters.keys())



def test_procdeclaration_is_not_abstract():
    assert not inspect.isabstract(ProcDeclaration)


def test_procdeclaration_constructor_exists():
    assert callable(ProcDeclaration.__init__)


def test_procdeclaration_constructor_args():
    sig = inspect.signature(ProcDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::proccall_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::ProcCall)


def test_kmlogo::asm::proccall_constructor_exists():
    assert callable(kmlogo::asm::ProcCall.__init__)


def test_kmlogo::asm::proccall_constructor_args():
    sig = inspect.signature(kmlogo::asm::ProcCall.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::constant_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Constant)


def test_kmlogo::asm::constant_constructor_exists():
    assert callable(kmlogo::asm::Constant.__init__)


def test_kmlogo::asm::constant_constructor_args():
    sig = inspect.signature(kmlogo::asm::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "integerValue" in params, "Missing parameter 'integerValue'"

def test_kmlogo::asm::constant_has_integerValue():
    assert hasattr(kmlogo::asm::Constant, "integerValue")
    descriptor = None
    for klass in kmlogo::asm::Constant.__mro__:
        if "integerValue" in klass.__dict__:
            descriptor = klass.__dict__["integerValue"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo::asm::parametercall_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::ParameterCall)


def test_kmlogo::asm::parametercall_constructor_exists():
    assert callable(kmlogo::asm::ParameterCall.__init__)


def test_kmlogo::asm::parametercall_constructor_args():
    sig = inspect.signature(kmlogo::asm::ParameterCall.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::binaryexp_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::BinaryExp)


def test_kmlogo::asm::binaryexp_constructor_exists():
    assert callable(kmlogo::asm::BinaryExp.__init__)


def test_kmlogo::asm::binaryexp_constructor_args():
    sig = inspect.signature(kmlogo::asm::BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::penup_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::PenUp)


def test_kmlogo::asm::penup_constructor_exists():
    assert callable(kmlogo::asm::PenUp.__init__)


def test_kmlogo::asm::penup_constructor_args():
    sig = inspect.signature(kmlogo::asm::PenUp.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::forward_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Forward)


def test_kmlogo::asm::forward_constructor_exists():
    assert callable(kmlogo::asm::Forward.__init__)


def test_kmlogo::asm::forward_constructor_args():
    sig = inspect.signature(kmlogo::asm::Forward.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::right_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Right)


def test_kmlogo::asm::right_constructor_exists():
    assert callable(kmlogo::asm::Right.__init__)


def test_kmlogo::asm::right_constructor_args():
    sig = inspect.signature(kmlogo::asm::Right.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::pendown_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::PenDown)


def test_kmlogo::asm::pendown_constructor_exists():
    assert callable(kmlogo::asm::PenDown.__init__)


def test_kmlogo::asm::pendown_constructor_args():
    sig = inspect.signature(kmlogo::asm::PenDown.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::clear_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Clear)


def test_kmlogo::asm::clear_constructor_exists():
    assert callable(kmlogo::asm::Clear.__init__)


def test_kmlogo::asm::clear_constructor_args():
    sig = inspect.signature(kmlogo::asm::Clear.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::left_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Left)


def test_kmlogo::asm::left_constructor_exists():
    assert callable(kmlogo::asm::Left.__init__)


def test_kmlogo::asm::left_constructor_args():
    sig = inspect.signature(kmlogo::asm::Left.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::back_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Back)


def test_kmlogo::asm::back_constructor_exists():
    assert callable(kmlogo::asm::Back.__init__)


def test_kmlogo::asm::back_constructor_args():
    sig = inspect.signature(kmlogo::asm::Back.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::block_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Block)


def test_kmlogo::asm::block_constructor_exists():
    assert callable(kmlogo::asm::Block.__init__)


def test_kmlogo::asm::block_constructor_args():
    sig = inspect.signature(kmlogo::asm::Block.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::procdeclaration_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::ProcDeclaration)


def test_kmlogo::asm::procdeclaration_constructor_exists():
    assert callable(kmlogo::asm::ProcDeclaration.__init__)


def test_kmlogo::asm::procdeclaration_constructor_args():
    sig = inspect.signature(kmlogo::asm::ProcDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kmlogo::asm::procdeclaration_has_name():
    assert hasattr(kmlogo::asm::ProcDeclaration, "name")
    descriptor = None
    for klass in kmlogo::asm::ProcDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo::asm::controlstructure_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::ControlStructure)


def test_kmlogo::asm::controlstructure_constructor_exists():
    assert callable(kmlogo::asm::ControlStructure.__init__)


def test_kmlogo::asm::controlstructure_constructor_args():
    sig = inspect.signature(kmlogo::asm::ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::expression_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Expression)


def test_kmlogo::asm::expression_constructor_exists():
    assert callable(kmlogo::asm::Expression.__init__)


def test_kmlogo::asm::expression_constructor_args():
    sig = inspect.signature(kmlogo::asm::Expression.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::primitive_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Primitive)


def test_kmlogo::asm::primitive_constructor_exists():
    assert callable(kmlogo::asm::Primitive.__init__)


def test_kmlogo::asm::primitive_constructor_args():
    sig = inspect.signature(kmlogo::asm::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::asm::instruction_is_not_abstract():
    assert not inspect.isabstract(kmlogo::asm::Instruction)


def test_kmlogo::asm::instruction_constructor_exists():
    assert callable(kmlogo::asm::Instruction.__init__)


def test_kmlogo::asm::instruction_constructor_args():
    sig = inspect.signature(kmlogo::asm::Instruction.__init__)
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
kmlogo::asm::LogoProgram_strategy = st.builds(
    kmlogo::asm::LogoProgram,
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
kmlogo::asm::Minus_strategy = st.builds(
    kmlogo::asm::Minus,
)
kmlogo::asm::Mult_strategy = st.builds(
    kmlogo::asm::Mult,
)
kmlogo::asm::Lower_strategy = st.builds(
    kmlogo::asm::Lower,
)
kmlogo::asm::Div_strategy = st.builds(
    kmlogo::asm::Div,
)
kmlogo::asm::Equals_strategy = st.builds(
    kmlogo::asm::Equals,
)
kmlogo::asm::Greater_strategy = st.builds(
    kmlogo::asm::Greater,
)
kmlogo::asm::Plus_strategy = st.builds(
    kmlogo::asm::Plus,
)
kmlogo::asm::Parameter_strategy = st.builds(
    kmlogo::asm::Parameter,
    name=
        safe_text
)
Block_strategy = st.builds(
    Block,
)
ControlStructure_strategy = st.builds(
    ControlStructure,
)
kmlogo::asm::Repeat_strategy = st.builds(
    kmlogo::asm::Repeat,
)
kmlogo::asm::While_strategy = st.builds(
    kmlogo::asm::While,
)
kmlogo::asm::If_strategy = st.builds(
    kmlogo::asm::If,
)
ProcDeclaration_strategy = st.builds(
    ProcDeclaration,
)
Expression_strategy = st.builds(
    Expression,
)
kmlogo::asm::ProcCall_strategy = st.builds(
    kmlogo::asm::ProcCall,
)
kmlogo::asm::Constant_strategy = st.builds(
    kmlogo::asm::Constant,
    integerValue=
        safe_text
)
kmlogo::asm::ParameterCall_strategy = st.builds(
    kmlogo::asm::ParameterCall,
)
kmlogo::asm::BinaryExp_strategy = st.builds(
    kmlogo::asm::BinaryExp,
)
Primitive_strategy = st.builds(
    Primitive,
)
kmlogo::asm::PenUp_strategy = st.builds(
    kmlogo::asm::PenUp,
)
kmlogo::asm::Forward_strategy = st.builds(
    kmlogo::asm::Forward,
)
kmlogo::asm::Right_strategy = st.builds(
    kmlogo::asm::Right,
)
kmlogo::asm::PenDown_strategy = st.builds(
    kmlogo::asm::PenDown,
)
kmlogo::asm::Clear_strategy = st.builds(
    kmlogo::asm::Clear,
)
kmlogo::asm::Left_strategy = st.builds(
    kmlogo::asm::Left,
)
kmlogo::asm::Back_strategy = st.builds(
    kmlogo::asm::Back,
)
Instruction_strategy = st.builds(
    Instruction,
)
kmlogo::asm::Block_strategy = st.builds(
    kmlogo::asm::Block,
)
kmlogo::asm::ProcDeclaration_strategy = st.builds(
    kmlogo::asm::ProcDeclaration,
    name=
        safe_text
)
kmlogo::asm::ControlStructure_strategy = st.builds(
    kmlogo::asm::ControlStructure,
)
kmlogo::asm::Expression_strategy = st.builds(
    kmlogo::asm::Expression,
)
kmlogo::asm::Primitive_strategy = st.builds(
    kmlogo::asm::Primitive,
)
kmlogo::asm::Instruction_strategy = st.builds(
    kmlogo::asm::Instruction,
)

@given(instance=kmlogo::asm::LogoProgram_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::logoprogram_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::LogoProgram)

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

@given(instance=kmlogo::asm::Minus_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::minus_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Minus)

@given(instance=kmlogo::asm::Mult_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::mult_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Mult)

@given(instance=kmlogo::asm::Lower_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::lower_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Lower)

@given(instance=kmlogo::asm::Div_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::div_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Div)

@given(instance=kmlogo::asm::Equals_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::equals_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Equals)

@given(instance=kmlogo::asm::Greater_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::greater_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Greater)

@given(instance=kmlogo::asm::Plus_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::plus_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Plus)

@given(instance=kmlogo::asm::Parameter_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::parameter_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Parameter)

@given(instance=kmlogo::asm::Parameter_strategy)
def test_kmlogo::asm::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kmlogo::asm::Parameter_strategy)
def test_kmlogo::asm::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=ControlStructure_strategy)
@settings(max_examples=50)
def test_controlstructure_instantiation(instance):
    assert isinstance(instance, ControlStructure)

@given(instance=kmlogo::asm::Repeat_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::repeat_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Repeat)

@given(instance=kmlogo::asm::While_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::while_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::While)

@given(instance=kmlogo::asm::If_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::if_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::If)

@given(instance=ProcDeclaration_strategy)
@settings(max_examples=50)
def test_procdeclaration_instantiation(instance):
    assert isinstance(instance, ProcDeclaration)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=kmlogo::asm::ProcCall_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::proccall_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::ProcCall)

@given(instance=kmlogo::asm::Constant_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::constant_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Constant)

@given(instance=kmlogo::asm::Constant_strategy)
def test_kmlogo::asm::constant_integerValue_type(instance):
    assert isinstance(instance.integerValue, str)


@given(instance=kmlogo::asm::Constant_strategy)
def test_kmlogo::asm::constant_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original

@given(instance=kmlogo::asm::ParameterCall_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::parametercall_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::ParameterCall)

@given(instance=kmlogo::asm::BinaryExp_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::binaryexp_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::BinaryExp)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=kmlogo::asm::PenUp_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::penup_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::PenUp)

@given(instance=kmlogo::asm::Forward_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::forward_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Forward)

@given(instance=kmlogo::asm::Right_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::right_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Right)

@given(instance=kmlogo::asm::PenDown_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::pendown_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::PenDown)

@given(instance=kmlogo::asm::Clear_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::clear_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Clear)

@given(instance=kmlogo::asm::Left_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::left_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Left)

@given(instance=kmlogo::asm::Back_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::back_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Back)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=kmlogo::asm::Block_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::block_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Block)

@given(instance=kmlogo::asm::ProcDeclaration_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::procdeclaration_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::ProcDeclaration)

@given(instance=kmlogo::asm::ProcDeclaration_strategy)
def test_kmlogo::asm::procdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kmlogo::asm::ProcDeclaration_strategy)
def test_kmlogo::asm::procdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kmlogo::asm::ControlStructure_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::controlstructure_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::ControlStructure)

@given(instance=kmlogo::asm::Expression_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::expression_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Expression)

@given(instance=kmlogo::asm::Primitive_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::primitive_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Primitive)

@given(instance=kmlogo::asm::Instruction_strategy)
@settings(max_examples=50)
def test_kmlogo::asm::instruction_instantiation(instance):
    assert isinstance(instance, kmlogo::asm::Instruction)
