import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Value,
    mil::ConstantInteger,
    ArithmeticInstruction,
    mil::DivInstruction,
    mil::MulInstruction,
    mil::SubInstruction,
    mil::AddInstruction,
    OutputInstruction,
    mil::PrintInstruction,
    mil::YieldInstruciton,
    CompareInstruction,
    mil::GreaterThanEqualInstruction,
    mil::LessThanInstruction,
    mil::LessThanEqualInstruction,
    mil::NotEqualInstruction,
    mil::GreaterThanInstruction,
    mil::EqualInstruction,
    JumpInstruction,
    mil::ConditionalJumpInstruction,
    mil::UnconditionalJumpInstruction,
    mil::RegisterReference,
    mil::Value,
    Instruction,
    mil::CallInstruction,
    mil::StoreInstruction,
    mil::OutputInstruction,
    mil::LoadInstruction,
    mil::CompareInstruction,
    mil::ReturnInstruction,
    mil::ArithmeticInstruction,
    mil::JumpInstruction,
    mil::NegateInstruction,
    mil::LabelInstruction,
    mil::Instruction,
    mil::MILModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_mil::constantinteger_is_not_abstract():
    assert not inspect.isabstract(mil::ConstantInteger)


def test_mil::constantinteger_constructor_exists():
    assert callable(mil::ConstantInteger.__init__)


def test_mil::constantinteger_constructor_args():
    sig = inspect.signature(mil::ConstantInteger.__init__)
    params = list(sig.parameters.keys())
    assert "rawValue" in params, "Missing parameter 'rawValue'"

def test_mil::constantinteger_has_rawValue():
    assert hasattr(mil::ConstantInteger, "rawValue")
    descriptor = None
    for klass in mil::ConstantInteger.__mro__:
        if "rawValue" in klass.__dict__:
            descriptor = klass.__dict__["rawValue"]
            break
    assert isinstance(descriptor, property)



def test_arithmeticinstruction_is_not_abstract():
    assert not inspect.isabstract(ArithmeticInstruction)


def test_arithmeticinstruction_constructor_exists():
    assert callable(ArithmeticInstruction.__init__)


def test_arithmeticinstruction_constructor_args():
    sig = inspect.signature(ArithmeticInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::divinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::DivInstruction)


def test_mil::divinstruction_constructor_exists():
    assert callable(mil::DivInstruction.__init__)


def test_mil::divinstruction_constructor_args():
    sig = inspect.signature(mil::DivInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::mulinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::MulInstruction)


def test_mil::mulinstruction_constructor_exists():
    assert callable(mil::MulInstruction.__init__)


def test_mil::mulinstruction_constructor_args():
    sig = inspect.signature(mil::MulInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::subinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::SubInstruction)


def test_mil::subinstruction_constructor_exists():
    assert callable(mil::SubInstruction.__init__)


def test_mil::subinstruction_constructor_args():
    sig = inspect.signature(mil::SubInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::addinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::AddInstruction)


def test_mil::addinstruction_constructor_exists():
    assert callable(mil::AddInstruction.__init__)


def test_mil::addinstruction_constructor_args():
    sig = inspect.signature(mil::AddInstruction.__init__)
    params = list(sig.parameters.keys())



def test_outputinstruction_is_not_abstract():
    assert not inspect.isabstract(OutputInstruction)


def test_outputinstruction_constructor_exists():
    assert callable(OutputInstruction.__init__)


def test_outputinstruction_constructor_args():
    sig = inspect.signature(OutputInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::printinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::PrintInstruction)


def test_mil::printinstruction_constructor_exists():
    assert callable(mil::PrintInstruction.__init__)


def test_mil::printinstruction_constructor_args():
    sig = inspect.signature(mil::PrintInstruction.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"

def test_mil::printinstruction_has_output():
    assert hasattr(mil::PrintInstruction, "output")
    descriptor = None
    for klass in mil::PrintInstruction.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_mil::yieldinstruciton_is_not_abstract():
    assert not inspect.isabstract(mil::YieldInstruciton)


def test_mil::yieldinstruciton_constructor_exists():
    assert callable(mil::YieldInstruciton.__init__)


def test_mil::yieldinstruciton_constructor_args():
    sig = inspect.signature(mil::YieldInstruciton.__init__)
    params = list(sig.parameters.keys())



def test_compareinstruction_is_not_abstract():
    assert not inspect.isabstract(CompareInstruction)


def test_compareinstruction_constructor_exists():
    assert callable(CompareInstruction.__init__)


def test_compareinstruction_constructor_args():
    sig = inspect.signature(CompareInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::greaterthanequalinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::GreaterThanEqualInstruction)


def test_mil::greaterthanequalinstruction_constructor_exists():
    assert callable(mil::GreaterThanEqualInstruction.__init__)


def test_mil::greaterthanequalinstruction_constructor_args():
    sig = inspect.signature(mil::GreaterThanEqualInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::lessthaninstruction_is_not_abstract():
    assert not inspect.isabstract(mil::LessThanInstruction)


def test_mil::lessthaninstruction_constructor_exists():
    assert callable(mil::LessThanInstruction.__init__)


def test_mil::lessthaninstruction_constructor_args():
    sig = inspect.signature(mil::LessThanInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::lessthanequalinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::LessThanEqualInstruction)


def test_mil::lessthanequalinstruction_constructor_exists():
    assert callable(mil::LessThanEqualInstruction.__init__)


def test_mil::lessthanequalinstruction_constructor_args():
    sig = inspect.signature(mil::LessThanEqualInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::notequalinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::NotEqualInstruction)


def test_mil::notequalinstruction_constructor_exists():
    assert callable(mil::NotEqualInstruction.__init__)


def test_mil::notequalinstruction_constructor_args():
    sig = inspect.signature(mil::NotEqualInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::greaterthaninstruction_is_not_abstract():
    assert not inspect.isabstract(mil::GreaterThanInstruction)


def test_mil::greaterthaninstruction_constructor_exists():
    assert callable(mil::GreaterThanInstruction.__init__)


def test_mil::greaterthaninstruction_constructor_args():
    sig = inspect.signature(mil::GreaterThanInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::equalinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::EqualInstruction)


def test_mil::equalinstruction_constructor_exists():
    assert callable(mil::EqualInstruction.__init__)


def test_mil::equalinstruction_constructor_args():
    sig = inspect.signature(mil::EqualInstruction.__init__)
    params = list(sig.parameters.keys())



def test_jumpinstruction_is_not_abstract():
    assert not inspect.isabstract(JumpInstruction)


def test_jumpinstruction_constructor_exists():
    assert callable(JumpInstruction.__init__)


def test_jumpinstruction_constructor_args():
    sig = inspect.signature(JumpInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::conditionaljumpinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::ConditionalJumpInstruction)


def test_mil::conditionaljumpinstruction_constructor_exists():
    assert callable(mil::ConditionalJumpInstruction.__init__)


def test_mil::conditionaljumpinstruction_constructor_args():
    sig = inspect.signature(mil::ConditionalJumpInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::unconditionaljumpinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::UnconditionalJumpInstruction)


def test_mil::unconditionaljumpinstruction_constructor_exists():
    assert callable(mil::UnconditionalJumpInstruction.__init__)


def test_mil::unconditionaljumpinstruction_constructor_args():
    sig = inspect.signature(mil::UnconditionalJumpInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::registerreference_is_not_abstract():
    assert not inspect.isabstract(mil::RegisterReference)


def test_mil::registerreference_constructor_exists():
    assert callable(mil::RegisterReference.__init__)


def test_mil::registerreference_constructor_args():
    sig = inspect.signature(mil::RegisterReference.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_mil::registerreference_has_address():
    assert hasattr(mil::RegisterReference, "address")
    descriptor = None
    for klass in mil::RegisterReference.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_mil::value_is_not_abstract():
    assert not inspect.isabstract(mil::Value)


def test_mil::value_constructor_exists():
    assert callable(mil::Value.__init__)


def test_mil::value_constructor_args():
    sig = inspect.signature(mil::Value.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::callinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::CallInstruction)


def test_mil::callinstruction_constructor_exists():
    assert callable(mil::CallInstruction.__init__)


def test_mil::callinstruction_constructor_args():
    sig = inspect.signature(mil::CallInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::storeinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::StoreInstruction)


def test_mil::storeinstruction_constructor_exists():
    assert callable(mil::StoreInstruction.__init__)


def test_mil::storeinstruction_constructor_args():
    sig = inspect.signature(mil::StoreInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::outputinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::OutputInstruction)


def test_mil::outputinstruction_constructor_exists():
    assert callable(mil::OutputInstruction.__init__)


def test_mil::outputinstruction_constructor_args():
    sig = inspect.signature(mil::OutputInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::loadinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::LoadInstruction)


def test_mil::loadinstruction_constructor_exists():
    assert callable(mil::LoadInstruction.__init__)


def test_mil::loadinstruction_constructor_args():
    sig = inspect.signature(mil::LoadInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::compareinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::CompareInstruction)


def test_mil::compareinstruction_constructor_exists():
    assert callable(mil::CompareInstruction.__init__)


def test_mil::compareinstruction_constructor_args():
    sig = inspect.signature(mil::CompareInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::returninstruction_is_not_abstract():
    assert not inspect.isabstract(mil::ReturnInstruction)


def test_mil::returninstruction_constructor_exists():
    assert callable(mil::ReturnInstruction.__init__)


def test_mil::returninstruction_constructor_args():
    sig = inspect.signature(mil::ReturnInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::arithmeticinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::ArithmeticInstruction)


def test_mil::arithmeticinstruction_constructor_exists():
    assert callable(mil::ArithmeticInstruction.__init__)


def test_mil::arithmeticinstruction_constructor_args():
    sig = inspect.signature(mil::ArithmeticInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::jumpinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::JumpInstruction)


def test_mil::jumpinstruction_constructor_exists():
    assert callable(mil::JumpInstruction.__init__)


def test_mil::jumpinstruction_constructor_args():
    sig = inspect.signature(mil::JumpInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::negateinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::NegateInstruction)


def test_mil::negateinstruction_constructor_exists():
    assert callable(mil::NegateInstruction.__init__)


def test_mil::negateinstruction_constructor_args():
    sig = inspect.signature(mil::NegateInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::labelinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::LabelInstruction)


def test_mil::labelinstruction_constructor_exists():
    assert callable(mil::LabelInstruction.__init__)


def test_mil::labelinstruction_constructor_args():
    sig = inspect.signature(mil::LabelInstruction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mil::labelinstruction_has_name():
    assert hasattr(mil::LabelInstruction, "name")
    descriptor = None
    for klass in mil::LabelInstruction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mil::instruction_is_not_abstract():
    assert not inspect.isabstract(mil::Instruction)


def test_mil::instruction_constructor_exists():
    assert callable(mil::Instruction.__init__)


def test_mil::instruction_constructor_args():
    sig = inspect.signature(mil::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::milmodel_is_not_abstract():
    assert not inspect.isabstract(mil::MILModel)


def test_mil::milmodel_constructor_exists():
    assert callable(mil::MILModel.__init__)


def test_mil::milmodel_constructor_args():
    sig = inspect.signature(mil::MILModel.__init__)
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
Value_strategy = st.builds(
    Value,
)
mil::ConstantInteger_strategy = st.builds(
    mil::ConstantInteger,
    rawValue=
        st.integers()
)
ArithmeticInstruction_strategy = st.builds(
    ArithmeticInstruction,
)
mil::DivInstruction_strategy = st.builds(
    mil::DivInstruction,
)
mil::MulInstruction_strategy = st.builds(
    mil::MulInstruction,
)
mil::SubInstruction_strategy = st.builds(
    mil::SubInstruction,
)
mil::AddInstruction_strategy = st.builds(
    mil::AddInstruction,
)
OutputInstruction_strategy = st.builds(
    OutputInstruction,
)
mil::PrintInstruction_strategy = st.builds(
    mil::PrintInstruction,
    output=
        safe_text
)
mil::YieldInstruciton_strategy = st.builds(
    mil::YieldInstruciton,
)
CompareInstruction_strategy = st.builds(
    CompareInstruction,
)
mil::GreaterThanEqualInstruction_strategy = st.builds(
    mil::GreaterThanEqualInstruction,
)
mil::LessThanInstruction_strategy = st.builds(
    mil::LessThanInstruction,
)
mil::LessThanEqualInstruction_strategy = st.builds(
    mil::LessThanEqualInstruction,
)
mil::NotEqualInstruction_strategy = st.builds(
    mil::NotEqualInstruction,
)
mil::GreaterThanInstruction_strategy = st.builds(
    mil::GreaterThanInstruction,
)
mil::EqualInstruction_strategy = st.builds(
    mil::EqualInstruction,
)
JumpInstruction_strategy = st.builds(
    JumpInstruction,
)
mil::ConditionalJumpInstruction_strategy = st.builds(
    mil::ConditionalJumpInstruction,
)
mil::UnconditionalJumpInstruction_strategy = st.builds(
    mil::UnconditionalJumpInstruction,
)
mil::RegisterReference_strategy = st.builds(
    mil::RegisterReference,
    address=
        safe_text
)
mil::Value_strategy = st.builds(
    mil::Value,
)
Instruction_strategy = st.builds(
    Instruction,
)
mil::CallInstruction_strategy = st.builds(
    mil::CallInstruction,
)
mil::StoreInstruction_strategy = st.builds(
    mil::StoreInstruction,
)
mil::OutputInstruction_strategy = st.builds(
    mil::OutputInstruction,
)
mil::LoadInstruction_strategy = st.builds(
    mil::LoadInstruction,
)
mil::CompareInstruction_strategy = st.builds(
    mil::CompareInstruction,
)
mil::ReturnInstruction_strategy = st.builds(
    mil::ReturnInstruction,
)
mil::ArithmeticInstruction_strategy = st.builds(
    mil::ArithmeticInstruction,
)
mil::JumpInstruction_strategy = st.builds(
    mil::JumpInstruction,
)
mil::NegateInstruction_strategy = st.builds(
    mil::NegateInstruction,
)
mil::LabelInstruction_strategy = st.builds(
    mil::LabelInstruction,
    name=
        safe_text
)
mil::Instruction_strategy = st.builds(
    mil::Instruction,
)
mil::MILModel_strategy = st.builds(
    mil::MILModel,
)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=mil::ConstantInteger_strategy)
@settings(max_examples=50)
def test_mil::constantinteger_instantiation(instance):
    assert isinstance(instance, mil::ConstantInteger)

@given(instance=mil::ConstantInteger_strategy)
def test_mil::constantinteger_rawValue_type(instance):
    assert isinstance(instance.rawValue, int)


@given(instance=mil::ConstantInteger_strategy)
def test_mil::constantinteger_rawValue_setter(instance):
    original = instance.rawValue
    instance.rawValue = original
    assert instance.rawValue == original

@given(instance=ArithmeticInstruction_strategy)
@settings(max_examples=50)
def test_arithmeticinstruction_instantiation(instance):
    assert isinstance(instance, ArithmeticInstruction)

@given(instance=mil::DivInstruction_strategy)
@settings(max_examples=50)
def test_mil::divinstruction_instantiation(instance):
    assert isinstance(instance, mil::DivInstruction)

@given(instance=mil::MulInstruction_strategy)
@settings(max_examples=50)
def test_mil::mulinstruction_instantiation(instance):
    assert isinstance(instance, mil::MulInstruction)

@given(instance=mil::SubInstruction_strategy)
@settings(max_examples=50)
def test_mil::subinstruction_instantiation(instance):
    assert isinstance(instance, mil::SubInstruction)

@given(instance=mil::AddInstruction_strategy)
@settings(max_examples=50)
def test_mil::addinstruction_instantiation(instance):
    assert isinstance(instance, mil::AddInstruction)

@given(instance=OutputInstruction_strategy)
@settings(max_examples=50)
def test_outputinstruction_instantiation(instance):
    assert isinstance(instance, OutputInstruction)

@given(instance=mil::PrintInstruction_strategy)
@settings(max_examples=50)
def test_mil::printinstruction_instantiation(instance):
    assert isinstance(instance, mil::PrintInstruction)

@given(instance=mil::PrintInstruction_strategy)
def test_mil::printinstruction_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=mil::PrintInstruction_strategy)
def test_mil::printinstruction_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=mil::YieldInstruciton_strategy)
@settings(max_examples=50)
def test_mil::yieldinstruciton_instantiation(instance):
    assert isinstance(instance, mil::YieldInstruciton)

@given(instance=CompareInstruction_strategy)
@settings(max_examples=50)
def test_compareinstruction_instantiation(instance):
    assert isinstance(instance, CompareInstruction)

@given(instance=mil::GreaterThanEqualInstruction_strategy)
@settings(max_examples=50)
def test_mil::greaterthanequalinstruction_instantiation(instance):
    assert isinstance(instance, mil::GreaterThanEqualInstruction)

@given(instance=mil::LessThanInstruction_strategy)
@settings(max_examples=50)
def test_mil::lessthaninstruction_instantiation(instance):
    assert isinstance(instance, mil::LessThanInstruction)

@given(instance=mil::LessThanEqualInstruction_strategy)
@settings(max_examples=50)
def test_mil::lessthanequalinstruction_instantiation(instance):
    assert isinstance(instance, mil::LessThanEqualInstruction)

@given(instance=mil::NotEqualInstruction_strategy)
@settings(max_examples=50)
def test_mil::notequalinstruction_instantiation(instance):
    assert isinstance(instance, mil::NotEqualInstruction)

@given(instance=mil::GreaterThanInstruction_strategy)
@settings(max_examples=50)
def test_mil::greaterthaninstruction_instantiation(instance):
    assert isinstance(instance, mil::GreaterThanInstruction)

@given(instance=mil::EqualInstruction_strategy)
@settings(max_examples=50)
def test_mil::equalinstruction_instantiation(instance):
    assert isinstance(instance, mil::EqualInstruction)

@given(instance=JumpInstruction_strategy)
@settings(max_examples=50)
def test_jumpinstruction_instantiation(instance):
    assert isinstance(instance, JumpInstruction)

@given(instance=mil::ConditionalJumpInstruction_strategy)
@settings(max_examples=50)
def test_mil::conditionaljumpinstruction_instantiation(instance):
    assert isinstance(instance, mil::ConditionalJumpInstruction)

@given(instance=mil::UnconditionalJumpInstruction_strategy)
@settings(max_examples=50)
def test_mil::unconditionaljumpinstruction_instantiation(instance):
    assert isinstance(instance, mil::UnconditionalJumpInstruction)

@given(instance=mil::RegisterReference_strategy)
@settings(max_examples=50)
def test_mil::registerreference_instantiation(instance):
    assert isinstance(instance, mil::RegisterReference)

@given(instance=mil::RegisterReference_strategy)
def test_mil::registerreference_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=mil::RegisterReference_strategy)
def test_mil::registerreference_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=mil::Value_strategy)
@settings(max_examples=50)
def test_mil::value_instantiation(instance):
    assert isinstance(instance, mil::Value)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=mil::CallInstruction_strategy)
@settings(max_examples=50)
def test_mil::callinstruction_instantiation(instance):
    assert isinstance(instance, mil::CallInstruction)

@given(instance=mil::StoreInstruction_strategy)
@settings(max_examples=50)
def test_mil::storeinstruction_instantiation(instance):
    assert isinstance(instance, mil::StoreInstruction)

@given(instance=mil::OutputInstruction_strategy)
@settings(max_examples=50)
def test_mil::outputinstruction_instantiation(instance):
    assert isinstance(instance, mil::OutputInstruction)

@given(instance=mil::LoadInstruction_strategy)
@settings(max_examples=50)
def test_mil::loadinstruction_instantiation(instance):
    assert isinstance(instance, mil::LoadInstruction)

@given(instance=mil::CompareInstruction_strategy)
@settings(max_examples=50)
def test_mil::compareinstruction_instantiation(instance):
    assert isinstance(instance, mil::CompareInstruction)

@given(instance=mil::ReturnInstruction_strategy)
@settings(max_examples=50)
def test_mil::returninstruction_instantiation(instance):
    assert isinstance(instance, mil::ReturnInstruction)

@given(instance=mil::ArithmeticInstruction_strategy)
@settings(max_examples=50)
def test_mil::arithmeticinstruction_instantiation(instance):
    assert isinstance(instance, mil::ArithmeticInstruction)

@given(instance=mil::JumpInstruction_strategy)
@settings(max_examples=50)
def test_mil::jumpinstruction_instantiation(instance):
    assert isinstance(instance, mil::JumpInstruction)

@given(instance=mil::NegateInstruction_strategy)
@settings(max_examples=50)
def test_mil::negateinstruction_instantiation(instance):
    assert isinstance(instance, mil::NegateInstruction)

@given(instance=mil::LabelInstruction_strategy)
@settings(max_examples=50)
def test_mil::labelinstruction_instantiation(instance):
    assert isinstance(instance, mil::LabelInstruction)

@given(instance=mil::LabelInstruction_strategy)
def test_mil::labelinstruction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mil::LabelInstruction_strategy)
def test_mil::labelinstruction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mil::Instruction_strategy)
@settings(max_examples=50)
def test_mil::instruction_instantiation(instance):
    assert isinstance(instance, mil::Instruction)

@given(instance=mil::MILModel_strategy)
@settings(max_examples=50)
def test_mil::milmodel_instantiation(instance):
    assert isinstance(instance, mil::MILModel)
