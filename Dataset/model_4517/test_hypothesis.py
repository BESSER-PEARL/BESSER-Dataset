import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    logo::Parameter,
    Expression,
    logo::Mult,
    logo::Lower,
    logo::Equals,
    logo::Div,
    logo::Greater,
    logo::Plus,
    logo::Minus,
    logo::Constant,
    logo::LogoProgram,
    logo::Expression,
    Instruction,
    logo::Right,
    logo::ParameterCall,
    logo::Block,
    logo::PenDown,
    logo::If,
    logo::Left,
    logo::Forward,
    logo::While,
    logo::Clear,
    logo::PenUp,
    logo::Repeat,
    logo::ProcCall,
    logo::ProcDeclaration,
    logo::Backward,
    logo::Instruction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_logo::parameter_is_not_abstract():
    assert not inspect.isabstract(logo::Parameter)


def test_logo::parameter_constructor_exists():
    assert callable(logo::Parameter.__init__)


def test_logo::parameter_constructor_args():
    sig = inspect.signature(logo::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo::parameter_has_name():
    assert hasattr(logo::Parameter, "name")
    descriptor = None
    for klass in logo::Parameter.__mro__:
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



def test_logo::mult_is_not_abstract():
    assert not inspect.isabstract(logo::Mult)


def test_logo::mult_constructor_exists():
    assert callable(logo::Mult.__init__)


def test_logo::mult_constructor_args():
    sig = inspect.signature(logo::Mult.__init__)
    params = list(sig.parameters.keys())



def test_logo::lower_is_not_abstract():
    assert not inspect.isabstract(logo::Lower)


def test_logo::lower_constructor_exists():
    assert callable(logo::Lower.__init__)


def test_logo::lower_constructor_args():
    sig = inspect.signature(logo::Lower.__init__)
    params = list(sig.parameters.keys())



def test_logo::equals_is_not_abstract():
    assert not inspect.isabstract(logo::Equals)


def test_logo::equals_constructor_exists():
    assert callable(logo::Equals.__init__)


def test_logo::equals_constructor_args():
    sig = inspect.signature(logo::Equals.__init__)
    params = list(sig.parameters.keys())



def test_logo::div_is_not_abstract():
    assert not inspect.isabstract(logo::Div)


def test_logo::div_constructor_exists():
    assert callable(logo::Div.__init__)


def test_logo::div_constructor_args():
    sig = inspect.signature(logo::Div.__init__)
    params = list(sig.parameters.keys())



def test_logo::greater_is_not_abstract():
    assert not inspect.isabstract(logo::Greater)


def test_logo::greater_constructor_exists():
    assert callable(logo::Greater.__init__)


def test_logo::greater_constructor_args():
    sig = inspect.signature(logo::Greater.__init__)
    params = list(sig.parameters.keys())



def test_logo::plus_is_not_abstract():
    assert not inspect.isabstract(logo::Plus)


def test_logo::plus_constructor_exists():
    assert callable(logo::Plus.__init__)


def test_logo::plus_constructor_args():
    sig = inspect.signature(logo::Plus.__init__)
    params = list(sig.parameters.keys())



def test_logo::minus_is_not_abstract():
    assert not inspect.isabstract(logo::Minus)


def test_logo::minus_constructor_exists():
    assert callable(logo::Minus.__init__)


def test_logo::minus_constructor_args():
    sig = inspect.signature(logo::Minus.__init__)
    params = list(sig.parameters.keys())



def test_logo::constant_is_not_abstract():
    assert not inspect.isabstract(logo::Constant)


def test_logo::constant_constructor_exists():
    assert callable(logo::Constant.__init__)


def test_logo::constant_constructor_args():
    sig = inspect.signature(logo::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "integerValue" in params, "Missing parameter 'integerValue'"

def test_logo::constant_has_integerValue():
    assert hasattr(logo::Constant, "integerValue")
    descriptor = None
    for klass in logo::Constant.__mro__:
        if "integerValue" in klass.__dict__:
            descriptor = klass.__dict__["integerValue"]
            break
    assert isinstance(descriptor, property)



def test_logo::logoprogram_is_not_abstract():
    assert not inspect.isabstract(logo::LogoProgram)


def test_logo::logoprogram_constructor_exists():
    assert callable(logo::LogoProgram.__init__)


def test_logo::logoprogram_constructor_args():
    sig = inspect.signature(logo::LogoProgram.__init__)
    params = list(sig.parameters.keys())



def test_logo::expression_is_not_abstract():
    assert not inspect.isabstract(logo::Expression)


def test_logo::expression_constructor_exists():
    assert callable(logo::Expression.__init__)


def test_logo::expression_constructor_args():
    sig = inspect.signature(logo::Expression.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_logo::right_is_not_abstract():
    assert not inspect.isabstract(logo::Right)


def test_logo::right_constructor_exists():
    assert callable(logo::Right.__init__)


def test_logo::right_constructor_args():
    sig = inspect.signature(logo::Right.__init__)
    params = list(sig.parameters.keys())



def test_logo::parametercall_is_not_abstract():
    assert not inspect.isabstract(logo::ParameterCall)


def test_logo::parametercall_constructor_exists():
    assert callable(logo::ParameterCall.__init__)


def test_logo::parametercall_constructor_args():
    sig = inspect.signature(logo::ParameterCall.__init__)
    params = list(sig.parameters.keys())



def test_logo::block_is_not_abstract():
    assert not inspect.isabstract(logo::Block)


def test_logo::block_constructor_exists():
    assert callable(logo::Block.__init__)


def test_logo::block_constructor_args():
    sig = inspect.signature(logo::Block.__init__)
    params = list(sig.parameters.keys())



def test_logo::pendown_is_not_abstract():
    assert not inspect.isabstract(logo::PenDown)


def test_logo::pendown_constructor_exists():
    assert callable(logo::PenDown.__init__)


def test_logo::pendown_constructor_args():
    sig = inspect.signature(logo::PenDown.__init__)
    params = list(sig.parameters.keys())



def test_logo::if_is_not_abstract():
    assert not inspect.isabstract(logo::If)


def test_logo::if_constructor_exists():
    assert callable(logo::If.__init__)


def test_logo::if_constructor_args():
    sig = inspect.signature(logo::If.__init__)
    params = list(sig.parameters.keys())



def test_logo::left_is_not_abstract():
    assert not inspect.isabstract(logo::Left)


def test_logo::left_constructor_exists():
    assert callable(logo::Left.__init__)


def test_logo::left_constructor_args():
    sig = inspect.signature(logo::Left.__init__)
    params = list(sig.parameters.keys())



def test_logo::forward_is_not_abstract():
    assert not inspect.isabstract(logo::Forward)


def test_logo::forward_constructor_exists():
    assert callable(logo::Forward.__init__)


def test_logo::forward_constructor_args():
    sig = inspect.signature(logo::Forward.__init__)
    params = list(sig.parameters.keys())



def test_logo::while_is_not_abstract():
    assert not inspect.isabstract(logo::While)


def test_logo::while_constructor_exists():
    assert callable(logo::While.__init__)


def test_logo::while_constructor_args():
    sig = inspect.signature(logo::While.__init__)
    params = list(sig.parameters.keys())



def test_logo::clear_is_not_abstract():
    assert not inspect.isabstract(logo::Clear)


def test_logo::clear_constructor_exists():
    assert callable(logo::Clear.__init__)


def test_logo::clear_constructor_args():
    sig = inspect.signature(logo::Clear.__init__)
    params = list(sig.parameters.keys())



def test_logo::penup_is_not_abstract():
    assert not inspect.isabstract(logo::PenUp)


def test_logo::penup_constructor_exists():
    assert callable(logo::PenUp.__init__)


def test_logo::penup_constructor_args():
    sig = inspect.signature(logo::PenUp.__init__)
    params = list(sig.parameters.keys())



def test_logo::repeat_is_not_abstract():
    assert not inspect.isabstract(logo::Repeat)


def test_logo::repeat_constructor_exists():
    assert callable(logo::Repeat.__init__)


def test_logo::repeat_constructor_args():
    sig = inspect.signature(logo::Repeat.__init__)
    params = list(sig.parameters.keys())



def test_logo::proccall_is_not_abstract():
    assert not inspect.isabstract(logo::ProcCall)


def test_logo::proccall_constructor_exists():
    assert callable(logo::ProcCall.__init__)


def test_logo::proccall_constructor_args():
    sig = inspect.signature(logo::ProcCall.__init__)
    params = list(sig.parameters.keys())



def test_logo::procdeclaration_is_not_abstract():
    assert not inspect.isabstract(logo::ProcDeclaration)


def test_logo::procdeclaration_constructor_exists():
    assert callable(logo::ProcDeclaration.__init__)


def test_logo::procdeclaration_constructor_args():
    sig = inspect.signature(logo::ProcDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo::procdeclaration_has_name():
    assert hasattr(logo::ProcDeclaration, "name")
    descriptor = None
    for klass in logo::ProcDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logo::backward_is_not_abstract():
    assert not inspect.isabstract(logo::Backward)


def test_logo::backward_constructor_exists():
    assert callable(logo::Backward.__init__)


def test_logo::backward_constructor_args():
    sig = inspect.signature(logo::Backward.__init__)
    params = list(sig.parameters.keys())



def test_logo::instruction_is_not_abstract():
    assert not inspect.isabstract(logo::Instruction)


def test_logo::instruction_constructor_exists():
    assert callable(logo::Instruction.__init__)


def test_logo::instruction_constructor_args():
    sig = inspect.signature(logo::Instruction.__init__)
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
logo::Parameter_strategy = st.builds(
    logo::Parameter,
    name=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
logo::Mult_strategy = st.builds(
    logo::Mult,
)
logo::Lower_strategy = st.builds(
    logo::Lower,
)
logo::Equals_strategy = st.builds(
    logo::Equals,
)
logo::Div_strategy = st.builds(
    logo::Div,
)
logo::Greater_strategy = st.builds(
    logo::Greater,
)
logo::Plus_strategy = st.builds(
    logo::Plus,
)
logo::Minus_strategy = st.builds(
    logo::Minus,
)
logo::Constant_strategy = st.builds(
    logo::Constant,
    integerValue=
        st.integers()
)
logo::LogoProgram_strategy = st.builds(
    logo::LogoProgram,
)
logo::Expression_strategy = st.builds(
    logo::Expression,
)
Instruction_strategy = st.builds(
    Instruction,
)
logo::Right_strategy = st.builds(
    logo::Right,
)
logo::ParameterCall_strategy = st.builds(
    logo::ParameterCall,
)
logo::Block_strategy = st.builds(
    logo::Block,
)
logo::PenDown_strategy = st.builds(
    logo::PenDown,
)
logo::If_strategy = st.builds(
    logo::If,
)
logo::Left_strategy = st.builds(
    logo::Left,
)
logo::Forward_strategy = st.builds(
    logo::Forward,
)
logo::While_strategy = st.builds(
    logo::While,
)
logo::Clear_strategy = st.builds(
    logo::Clear,
)
logo::PenUp_strategy = st.builds(
    logo::PenUp,
)
logo::Repeat_strategy = st.builds(
    logo::Repeat,
)
logo::ProcCall_strategy = st.builds(
    logo::ProcCall,
)
logo::ProcDeclaration_strategy = st.builds(
    logo::ProcDeclaration,
    name=
        safe_text
)
logo::Backward_strategy = st.builds(
    logo::Backward,
)
logo::Instruction_strategy = st.builds(
    logo::Instruction,
)

@given(instance=logo::Parameter_strategy)
@settings(max_examples=50)
def test_logo::parameter_instantiation(instance):
    assert isinstance(instance, logo::Parameter)

@given(instance=logo::Parameter_strategy)
def test_logo::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=logo::Parameter_strategy)
def test_logo::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=logo::Mult_strategy)
@settings(max_examples=50)
def test_logo::mult_instantiation(instance):
    assert isinstance(instance, logo::Mult)

@given(instance=logo::Lower_strategy)
@settings(max_examples=50)
def test_logo::lower_instantiation(instance):
    assert isinstance(instance, logo::Lower)

@given(instance=logo::Equals_strategy)
@settings(max_examples=50)
def test_logo::equals_instantiation(instance):
    assert isinstance(instance, logo::Equals)

@given(instance=logo::Div_strategy)
@settings(max_examples=50)
def test_logo::div_instantiation(instance):
    assert isinstance(instance, logo::Div)

@given(instance=logo::Greater_strategy)
@settings(max_examples=50)
def test_logo::greater_instantiation(instance):
    assert isinstance(instance, logo::Greater)

@given(instance=logo::Plus_strategy)
@settings(max_examples=50)
def test_logo::plus_instantiation(instance):
    assert isinstance(instance, logo::Plus)

@given(instance=logo::Minus_strategy)
@settings(max_examples=50)
def test_logo::minus_instantiation(instance):
    assert isinstance(instance, logo::Minus)

@given(instance=logo::Constant_strategy)
@settings(max_examples=50)
def test_logo::constant_instantiation(instance):
    assert isinstance(instance, logo::Constant)

@given(instance=logo::Constant_strategy)
def test_logo::constant_integerValue_type(instance):
    assert isinstance(instance.integerValue, int)


@given(instance=logo::Constant_strategy)
def test_logo::constant_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original

@given(instance=logo::LogoProgram_strategy)
@settings(max_examples=50)
def test_logo::logoprogram_instantiation(instance):
    assert isinstance(instance, logo::LogoProgram)

@given(instance=logo::Expression_strategy)
@settings(max_examples=50)
def test_logo::expression_instantiation(instance):
    assert isinstance(instance, logo::Expression)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=logo::Right_strategy)
@settings(max_examples=50)
def test_logo::right_instantiation(instance):
    assert isinstance(instance, logo::Right)

@given(instance=logo::ParameterCall_strategy)
@settings(max_examples=50)
def test_logo::parametercall_instantiation(instance):
    assert isinstance(instance, logo::ParameterCall)

@given(instance=logo::Block_strategy)
@settings(max_examples=50)
def test_logo::block_instantiation(instance):
    assert isinstance(instance, logo::Block)

@given(instance=logo::PenDown_strategy)
@settings(max_examples=50)
def test_logo::pendown_instantiation(instance):
    assert isinstance(instance, logo::PenDown)

@given(instance=logo::If_strategy)
@settings(max_examples=50)
def test_logo::if_instantiation(instance):
    assert isinstance(instance, logo::If)

@given(instance=logo::Left_strategy)
@settings(max_examples=50)
def test_logo::left_instantiation(instance):
    assert isinstance(instance, logo::Left)

@given(instance=logo::Forward_strategy)
@settings(max_examples=50)
def test_logo::forward_instantiation(instance):
    assert isinstance(instance, logo::Forward)

@given(instance=logo::While_strategy)
@settings(max_examples=50)
def test_logo::while_instantiation(instance):
    assert isinstance(instance, logo::While)

@given(instance=logo::Clear_strategy)
@settings(max_examples=50)
def test_logo::clear_instantiation(instance):
    assert isinstance(instance, logo::Clear)

@given(instance=logo::PenUp_strategy)
@settings(max_examples=50)
def test_logo::penup_instantiation(instance):
    assert isinstance(instance, logo::PenUp)

@given(instance=logo::Repeat_strategy)
@settings(max_examples=50)
def test_logo::repeat_instantiation(instance):
    assert isinstance(instance, logo::Repeat)

@given(instance=logo::ProcCall_strategy)
@settings(max_examples=50)
def test_logo::proccall_instantiation(instance):
    assert isinstance(instance, logo::ProcCall)

@given(instance=logo::ProcDeclaration_strategy)
@settings(max_examples=50)
def test_logo::procdeclaration_instantiation(instance):
    assert isinstance(instance, logo::ProcDeclaration)

@given(instance=logo::ProcDeclaration_strategy)
def test_logo::procdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=logo::ProcDeclaration_strategy)
def test_logo::procdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logo::Backward_strategy)
@settings(max_examples=50)
def test_logo::backward_instantiation(instance):
    assert isinstance(instance, logo::Backward)

@given(instance=logo::Instruction_strategy)
@settings(max_examples=50)
def test_logo::instruction_instantiation(instance):
    assert isinstance(instance, logo::Instruction)
