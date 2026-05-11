import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BinaryExp,
    kmLogo::Mult,
    kmLogo::Minus,
    kmLogo::Plus,
    kmLogo::Lower,
    kmLogo::Greater,
    kmLogo::Equals,
    kmLogo::Div,
    ControlStructure,
    kmLogo::Repeat,
    kmLogo::While,
    kmLogo::If,
    kmLogo::Parameter,
    kmLogo::Instruction,
    kmLogo::LogoProgram,
    Expression,
    kmLogo::Constant,
    kmLogo::ProcCall,
    kmLogo::ParameterCall,
    kmLogo::BinaryExp,
    Primitive,
    kmLogo::Clear,
    kmLogo::Right,
    kmLogo::Forward,
    kmLogo::PenUp,
    kmLogo::Left,
    kmLogo::PenDown,
    kmLogo::Back,
    Instruction,
    kmLogo::Expression,
    kmLogo::ProcDeclaration,
    kmLogo::ControlStructure,
    kmLogo::Block,
    kmLogo::Primitive,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_binaryexp_is_not_abstract():
    assert not inspect.isabstract(BinaryExp)


def test_binaryexp_constructor_exists():
    assert callable(BinaryExp.__init__)


def test_binaryexp_constructor_args():
    sig = inspect.signature(BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::mult_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Mult)


def test_kmlogo::mult_constructor_exists():
    assert callable(kmLogo::Mult.__init__)


def test_kmlogo::mult_constructor_args():
    sig = inspect.signature(kmLogo::Mult.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::minus_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Minus)


def test_kmlogo::minus_constructor_exists():
    assert callable(kmLogo::Minus.__init__)


def test_kmlogo::minus_constructor_args():
    sig = inspect.signature(kmLogo::Minus.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::plus_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Plus)


def test_kmlogo::plus_constructor_exists():
    assert callable(kmLogo::Plus.__init__)


def test_kmlogo::plus_constructor_args():
    sig = inspect.signature(kmLogo::Plus.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::lower_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Lower)


def test_kmlogo::lower_constructor_exists():
    assert callable(kmLogo::Lower.__init__)


def test_kmlogo::lower_constructor_args():
    sig = inspect.signature(kmLogo::Lower.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::greater_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Greater)


def test_kmlogo::greater_constructor_exists():
    assert callable(kmLogo::Greater.__init__)


def test_kmlogo::greater_constructor_args():
    sig = inspect.signature(kmLogo::Greater.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::equals_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Equals)


def test_kmlogo::equals_constructor_exists():
    assert callable(kmLogo::Equals.__init__)


def test_kmlogo::equals_constructor_args():
    sig = inspect.signature(kmLogo::Equals.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::div_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Div)


def test_kmlogo::div_constructor_exists():
    assert callable(kmLogo::Div.__init__)


def test_kmlogo::div_constructor_args():
    sig = inspect.signature(kmLogo::Div.__init__)
    params = list(sig.parameters.keys())



def test_controlstructure_is_not_abstract():
    assert not inspect.isabstract(ControlStructure)


def test_controlstructure_constructor_exists():
    assert callable(ControlStructure.__init__)


def test_controlstructure_constructor_args():
    sig = inspect.signature(ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::repeat_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Repeat)


def test_kmlogo::repeat_constructor_exists():
    assert callable(kmLogo::Repeat.__init__)


def test_kmlogo::repeat_constructor_args():
    sig = inspect.signature(kmLogo::Repeat.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::while_is_not_abstract():
    assert not inspect.isabstract(kmLogo::While)


def test_kmlogo::while_constructor_exists():
    assert callable(kmLogo::While.__init__)


def test_kmlogo::while_constructor_args():
    sig = inspect.signature(kmLogo::While.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::if_is_not_abstract():
    assert not inspect.isabstract(kmLogo::If)


def test_kmlogo::if_constructor_exists():
    assert callable(kmLogo::If.__init__)


def test_kmlogo::if_constructor_args():
    sig = inspect.signature(kmLogo::If.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::parameter_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Parameter)


def test_kmlogo::parameter_constructor_exists():
    assert callable(kmLogo::Parameter.__init__)


def test_kmlogo::parameter_constructor_args():
    sig = inspect.signature(kmLogo::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kmlogo::parameter_has_name():
    assert hasattr(kmLogo::Parameter, "name")
    descriptor = None
    for klass in kmLogo::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo::instruction_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Instruction)


def test_kmlogo::instruction_constructor_exists():
    assert callable(kmLogo::Instruction.__init__)


def test_kmlogo::instruction_constructor_args():
    sig = inspect.signature(kmLogo::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::logoprogram_is_not_abstract():
    assert not inspect.isabstract(kmLogo::LogoProgram)


def test_kmlogo::logoprogram_constructor_exists():
    assert callable(kmLogo::LogoProgram.__init__)


def test_kmlogo::logoprogram_constructor_args():
    sig = inspect.signature(kmLogo::LogoProgram.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::constant_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Constant)


def test_kmlogo::constant_constructor_exists():
    assert callable(kmLogo::Constant.__init__)


def test_kmlogo::constant_constructor_args():
    sig = inspect.signature(kmLogo::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "integerValue" in params, "Missing parameter 'integerValue'"

def test_kmlogo::constant_has_integerValue():
    assert hasattr(kmLogo::Constant, "integerValue")
    descriptor = None
    for klass in kmLogo::Constant.__mro__:
        if "integerValue" in klass.__dict__:
            descriptor = klass.__dict__["integerValue"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo::proccall_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ProcCall)


def test_kmlogo::proccall_constructor_exists():
    assert callable(kmLogo::ProcCall.__init__)


def test_kmlogo::proccall_constructor_args():
    sig = inspect.signature(kmLogo::ProcCall.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::parametercall_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ParameterCall)


def test_kmlogo::parametercall_constructor_exists():
    assert callable(kmLogo::ParameterCall.__init__)


def test_kmlogo::parametercall_constructor_args():
    sig = inspect.signature(kmLogo::ParameterCall.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::binaryexp_is_not_abstract():
    assert not inspect.isabstract(kmLogo::BinaryExp)


def test_kmlogo::binaryexp_constructor_exists():
    assert callable(kmLogo::BinaryExp.__init__)


def test_kmlogo::binaryexp_constructor_args():
    sig = inspect.signature(kmLogo::BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::clear_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Clear)


def test_kmlogo::clear_constructor_exists():
    assert callable(kmLogo::Clear.__init__)


def test_kmlogo::clear_constructor_args():
    sig = inspect.signature(kmLogo::Clear.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::right_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Right)


def test_kmlogo::right_constructor_exists():
    assert callable(kmLogo::Right.__init__)


def test_kmlogo::right_constructor_args():
    sig = inspect.signature(kmLogo::Right.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::forward_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Forward)


def test_kmlogo::forward_constructor_exists():
    assert callable(kmLogo::Forward.__init__)


def test_kmlogo::forward_constructor_args():
    sig = inspect.signature(kmLogo::Forward.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::penup_is_not_abstract():
    assert not inspect.isabstract(kmLogo::PenUp)


def test_kmlogo::penup_constructor_exists():
    assert callable(kmLogo::PenUp.__init__)


def test_kmlogo::penup_constructor_args():
    sig = inspect.signature(kmLogo::PenUp.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::left_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Left)


def test_kmlogo::left_constructor_exists():
    assert callable(kmLogo::Left.__init__)


def test_kmlogo::left_constructor_args():
    sig = inspect.signature(kmLogo::Left.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::pendown_is_not_abstract():
    assert not inspect.isabstract(kmLogo::PenDown)


def test_kmlogo::pendown_constructor_exists():
    assert callable(kmLogo::PenDown.__init__)


def test_kmlogo::pendown_constructor_args():
    sig = inspect.signature(kmLogo::PenDown.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::back_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Back)


def test_kmlogo::back_constructor_exists():
    assert callable(kmLogo::Back.__init__)


def test_kmlogo::back_constructor_args():
    sig = inspect.signature(kmLogo::Back.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::expression_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Expression)


def test_kmlogo::expression_constructor_exists():
    assert callable(kmLogo::Expression.__init__)


def test_kmlogo::expression_constructor_args():
    sig = inspect.signature(kmLogo::Expression.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::procdeclaration_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ProcDeclaration)


def test_kmlogo::procdeclaration_constructor_exists():
    assert callable(kmLogo::ProcDeclaration.__init__)


def test_kmlogo::procdeclaration_constructor_args():
    sig = inspect.signature(kmLogo::ProcDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kmlogo::procdeclaration_has_name():
    assert hasattr(kmLogo::ProcDeclaration, "name")
    descriptor = None
    for klass in kmLogo::ProcDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo::controlstructure_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ControlStructure)


def test_kmlogo::controlstructure_constructor_exists():
    assert callable(kmLogo::ControlStructure.__init__)


def test_kmlogo::controlstructure_constructor_args():
    sig = inspect.signature(kmLogo::ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::block_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Block)


def test_kmlogo::block_constructor_exists():
    assert callable(kmLogo::Block.__init__)


def test_kmlogo::block_constructor_args():
    sig = inspect.signature(kmLogo::Block.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::primitive_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Primitive)


def test_kmlogo::primitive_constructor_exists():
    assert callable(kmLogo::Primitive.__init__)


def test_kmlogo::primitive_constructor_args():
    sig = inspect.signature(kmLogo::Primitive.__init__)
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
BinaryExp_strategy = st.builds(
    BinaryExp,
)
kmLogo::Mult_strategy = st.builds(
    kmLogo::Mult,
)
kmLogo::Minus_strategy = st.builds(
    kmLogo::Minus,
)
kmLogo::Plus_strategy = st.builds(
    kmLogo::Plus,
)
kmLogo::Lower_strategy = st.builds(
    kmLogo::Lower,
)
kmLogo::Greater_strategy = st.builds(
    kmLogo::Greater,
)
kmLogo::Equals_strategy = st.builds(
    kmLogo::Equals,
)
kmLogo::Div_strategy = st.builds(
    kmLogo::Div,
)
ControlStructure_strategy = st.builds(
    ControlStructure,
)
kmLogo::Repeat_strategy = st.builds(
    kmLogo::Repeat,
)
kmLogo::While_strategy = st.builds(
    kmLogo::While,
)
kmLogo::If_strategy = st.builds(
    kmLogo::If,
)
kmLogo::Parameter_strategy = st.builds(
    kmLogo::Parameter,
    name=
        safe_text
)
kmLogo::Instruction_strategy = st.builds(
    kmLogo::Instruction,
)
kmLogo::LogoProgram_strategy = st.builds(
    kmLogo::LogoProgram,
)
Expression_strategy = st.builds(
    Expression,
)
kmLogo::Constant_strategy = st.builds(
    kmLogo::Constant,
    integerValue=
        st.integers()
)
kmLogo::ProcCall_strategy = st.builds(
    kmLogo::ProcCall,
)
kmLogo::ParameterCall_strategy = st.builds(
    kmLogo::ParameterCall,
)
kmLogo::BinaryExp_strategy = st.builds(
    kmLogo::BinaryExp,
)
Primitive_strategy = st.builds(
    Primitive,
)
kmLogo::Clear_strategy = st.builds(
    kmLogo::Clear,
)
kmLogo::Right_strategy = st.builds(
    kmLogo::Right,
)
kmLogo::Forward_strategy = st.builds(
    kmLogo::Forward,
)
kmLogo::PenUp_strategy = st.builds(
    kmLogo::PenUp,
)
kmLogo::Left_strategy = st.builds(
    kmLogo::Left,
)
kmLogo::PenDown_strategy = st.builds(
    kmLogo::PenDown,
)
kmLogo::Back_strategy = st.builds(
    kmLogo::Back,
)
Instruction_strategy = st.builds(
    Instruction,
)
kmLogo::Expression_strategy = st.builds(
    kmLogo::Expression,
)
kmLogo::ProcDeclaration_strategy = st.builds(
    kmLogo::ProcDeclaration,
    name=
        safe_text
)
kmLogo::ControlStructure_strategy = st.builds(
    kmLogo::ControlStructure,
)
kmLogo::Block_strategy = st.builds(
    kmLogo::Block,
)
kmLogo::Primitive_strategy = st.builds(
    kmLogo::Primitive,
)

@given(instance=BinaryExp_strategy)
@settings(max_examples=50)
def test_binaryexp_instantiation(instance):
    assert isinstance(instance, BinaryExp)

@given(instance=kmLogo::Mult_strategy)
@settings(max_examples=50)
def test_kmlogo::mult_instantiation(instance):
    assert isinstance(instance, kmLogo::Mult)

@given(instance=kmLogo::Minus_strategy)
@settings(max_examples=50)
def test_kmlogo::minus_instantiation(instance):
    assert isinstance(instance, kmLogo::Minus)

@given(instance=kmLogo::Plus_strategy)
@settings(max_examples=50)
def test_kmlogo::plus_instantiation(instance):
    assert isinstance(instance, kmLogo::Plus)

@given(instance=kmLogo::Lower_strategy)
@settings(max_examples=50)
def test_kmlogo::lower_instantiation(instance):
    assert isinstance(instance, kmLogo::Lower)

@given(instance=kmLogo::Greater_strategy)
@settings(max_examples=50)
def test_kmlogo::greater_instantiation(instance):
    assert isinstance(instance, kmLogo::Greater)

@given(instance=kmLogo::Equals_strategy)
@settings(max_examples=50)
def test_kmlogo::equals_instantiation(instance):
    assert isinstance(instance, kmLogo::Equals)

@given(instance=kmLogo::Div_strategy)
@settings(max_examples=50)
def test_kmlogo::div_instantiation(instance):
    assert isinstance(instance, kmLogo::Div)

@given(instance=ControlStructure_strategy)
@settings(max_examples=50)
def test_controlstructure_instantiation(instance):
    assert isinstance(instance, ControlStructure)

@given(instance=kmLogo::Repeat_strategy)
@settings(max_examples=50)
def test_kmlogo::repeat_instantiation(instance):
    assert isinstance(instance, kmLogo::Repeat)

@given(instance=kmLogo::While_strategy)
@settings(max_examples=50)
def test_kmlogo::while_instantiation(instance):
    assert isinstance(instance, kmLogo::While)

@given(instance=kmLogo::If_strategy)
@settings(max_examples=50)
def test_kmlogo::if_instantiation(instance):
    assert isinstance(instance, kmLogo::If)

@given(instance=kmLogo::Parameter_strategy)
@settings(max_examples=50)
def test_kmlogo::parameter_instantiation(instance):
    assert isinstance(instance, kmLogo::Parameter)

@given(instance=kmLogo::Parameter_strategy)
def test_kmlogo::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kmLogo::Parameter_strategy)
def test_kmlogo::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kmLogo::Instruction_strategy)
@settings(max_examples=50)
def test_kmlogo::instruction_instantiation(instance):
    assert isinstance(instance, kmLogo::Instruction)

@given(instance=kmLogo::LogoProgram_strategy)
@settings(max_examples=50)
def test_kmlogo::logoprogram_instantiation(instance):
    assert isinstance(instance, kmLogo::LogoProgram)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=kmLogo::Constant_strategy)
@settings(max_examples=50)
def test_kmlogo::constant_instantiation(instance):
    assert isinstance(instance, kmLogo::Constant)

@given(instance=kmLogo::Constant_strategy)
def test_kmlogo::constant_integerValue_type(instance):
    assert isinstance(instance.integerValue, int)


@given(instance=kmLogo::Constant_strategy)
def test_kmlogo::constant_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original

@given(instance=kmLogo::ProcCall_strategy)
@settings(max_examples=50)
def test_kmlogo::proccall_instantiation(instance):
    assert isinstance(instance, kmLogo::ProcCall)

@given(instance=kmLogo::ParameterCall_strategy)
@settings(max_examples=50)
def test_kmlogo::parametercall_instantiation(instance):
    assert isinstance(instance, kmLogo::ParameterCall)

@given(instance=kmLogo::BinaryExp_strategy)
@settings(max_examples=50)
def test_kmlogo::binaryexp_instantiation(instance):
    assert isinstance(instance, kmLogo::BinaryExp)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=kmLogo::Clear_strategy)
@settings(max_examples=50)
def test_kmlogo::clear_instantiation(instance):
    assert isinstance(instance, kmLogo::Clear)

@given(instance=kmLogo::Right_strategy)
@settings(max_examples=50)
def test_kmlogo::right_instantiation(instance):
    assert isinstance(instance, kmLogo::Right)

@given(instance=kmLogo::Forward_strategy)
@settings(max_examples=50)
def test_kmlogo::forward_instantiation(instance):
    assert isinstance(instance, kmLogo::Forward)

@given(instance=kmLogo::PenUp_strategy)
@settings(max_examples=50)
def test_kmlogo::penup_instantiation(instance):
    assert isinstance(instance, kmLogo::PenUp)

@given(instance=kmLogo::Left_strategy)
@settings(max_examples=50)
def test_kmlogo::left_instantiation(instance):
    assert isinstance(instance, kmLogo::Left)

@given(instance=kmLogo::PenDown_strategy)
@settings(max_examples=50)
def test_kmlogo::pendown_instantiation(instance):
    assert isinstance(instance, kmLogo::PenDown)

@given(instance=kmLogo::Back_strategy)
@settings(max_examples=50)
def test_kmlogo::back_instantiation(instance):
    assert isinstance(instance, kmLogo::Back)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=kmLogo::Expression_strategy)
@settings(max_examples=50)
def test_kmlogo::expression_instantiation(instance):
    assert isinstance(instance, kmLogo::Expression)

@given(instance=kmLogo::ProcDeclaration_strategy)
@settings(max_examples=50)
def test_kmlogo::procdeclaration_instantiation(instance):
    assert isinstance(instance, kmLogo::ProcDeclaration)

@given(instance=kmLogo::ProcDeclaration_strategy)
def test_kmlogo::procdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kmLogo::ProcDeclaration_strategy)
def test_kmlogo::procdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kmLogo::ControlStructure_strategy)
@settings(max_examples=50)
def test_kmlogo::controlstructure_instantiation(instance):
    assert isinstance(instance, kmLogo::ControlStructure)

@given(instance=kmLogo::Block_strategy)
@settings(max_examples=50)
def test_kmlogo::block_instantiation(instance):
    assert isinstance(instance, kmLogo::Block)

@given(instance=kmLogo::Primitive_strategy)
@settings(max_examples=50)
def test_kmlogo::primitive_instantiation(instance):
    assert isinstance(instance, kmLogo::Primitive)
