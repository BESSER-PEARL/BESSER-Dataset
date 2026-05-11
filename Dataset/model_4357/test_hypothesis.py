import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Value,
    mil::ConstantInteger,
    BinaryOperation,
    mil::DivInstruction,
    mil::MultInstruction,
    mil::SubInstruction,
    mil::AddInstruction,
    mil::RegisterReference,
    UnaryOperation,
    mil::NegateInstruction,
    mil::StoreInstruction,
    mil::Value,
    Instruction,
    mil::UnaryOperation,
    mil::BinaryOperation,
    mil::LoadInstruction,
    mil::ReturnInstruction,
    mil::Jumper,
    mil::PrintInstruction,
    mil::YieldInstruction,
    Comparison,
    mil::LowerEqualsComparison,
    mil::GreaterThanComparison,
    mil::NotEqualsComparison,
    mil::GreaterEqualsComparison,
    mil::LowerThanComparison,
    mil::EqualsComparison,
    mil::Comparison,
    Jumper,
    mil::CallInstruction,
    mil::ConditionalJumpInstruction,
    mil::JumpInstruction,
    Statement,
    mil::JumpMarker,
    mil::Instruction,
    mil::Statement,
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



def test_binaryoperation_is_not_abstract():
    assert not inspect.isabstract(BinaryOperation)


def test_binaryoperation_constructor_exists():
    assert callable(BinaryOperation.__init__)


def test_binaryoperation_constructor_args():
    sig = inspect.signature(BinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_mil::divinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::DivInstruction)


def test_mil::divinstruction_constructor_exists():
    assert callable(mil::DivInstruction.__init__)


def test_mil::divinstruction_constructor_args():
    sig = inspect.signature(mil::DivInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::multinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::MultInstruction)


def test_mil::multinstruction_constructor_exists():
    assert callable(mil::MultInstruction.__init__)


def test_mil::multinstruction_constructor_args():
    sig = inspect.signature(mil::MultInstruction.__init__)
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



def test_unaryoperation_is_not_abstract():
    assert not inspect.isabstract(UnaryOperation)


def test_unaryoperation_constructor_exists():
    assert callable(UnaryOperation.__init__)


def test_unaryoperation_constructor_args():
    sig = inspect.signature(UnaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_mil::negateinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::NegateInstruction)


def test_mil::negateinstruction_constructor_exists():
    assert callable(mil::NegateInstruction.__init__)


def test_mil::negateinstruction_constructor_args():
    sig = inspect.signature(mil::NegateInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::storeinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::StoreInstruction)


def test_mil::storeinstruction_constructor_exists():
    assert callable(mil::StoreInstruction.__init__)


def test_mil::storeinstruction_constructor_args():
    sig = inspect.signature(mil::StoreInstruction.__init__)
    params = list(sig.parameters.keys())



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



def test_mil::unaryoperation_is_not_abstract():
    assert not inspect.isabstract(mil::UnaryOperation)


def test_mil::unaryoperation_constructor_exists():
    assert callable(mil::UnaryOperation.__init__)


def test_mil::unaryoperation_constructor_args():
    sig = inspect.signature(mil::UnaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_mil::binaryoperation_is_not_abstract():
    assert not inspect.isabstract(mil::BinaryOperation)


def test_mil::binaryoperation_constructor_exists():
    assert callable(mil::BinaryOperation.__init__)


def test_mil::binaryoperation_constructor_args():
    sig = inspect.signature(mil::BinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_mil::loadinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::LoadInstruction)


def test_mil::loadinstruction_constructor_exists():
    assert callable(mil::LoadInstruction.__init__)


def test_mil::loadinstruction_constructor_args():
    sig = inspect.signature(mil::LoadInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::returninstruction_is_not_abstract():
    assert not inspect.isabstract(mil::ReturnInstruction)


def test_mil::returninstruction_constructor_exists():
    assert callable(mil::ReturnInstruction.__init__)


def test_mil::returninstruction_constructor_args():
    sig = inspect.signature(mil::ReturnInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::jumper_is_not_abstract():
    assert not inspect.isabstract(mil::Jumper)


def test_mil::jumper_constructor_exists():
    assert callable(mil::Jumper.__init__)


def test_mil::jumper_constructor_args():
    sig = inspect.signature(mil::Jumper.__init__)
    params = list(sig.parameters.keys())



def test_mil::printinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::PrintInstruction)


def test_mil::printinstruction_constructor_exists():
    assert callable(mil::PrintInstruction.__init__)


def test_mil::printinstruction_constructor_args():
    sig = inspect.signature(mil::PrintInstruction.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_mil::printinstruction_has_text():
    assert hasattr(mil::PrintInstruction, "text")
    descriptor = None
    for klass in mil::PrintInstruction.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_mil::yieldinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::YieldInstruction)


def test_mil::yieldinstruction_constructor_exists():
    assert callable(mil::YieldInstruction.__init__)


def test_mil::yieldinstruction_constructor_args():
    sig = inspect.signature(mil::YieldInstruction.__init__)
    params = list(sig.parameters.keys())



def test_comparison_is_not_abstract():
    assert not inspect.isabstract(Comparison)


def test_comparison_constructor_exists():
    assert callable(Comparison.__init__)


def test_comparison_constructor_args():
    sig = inspect.signature(Comparison.__init__)
    params = list(sig.parameters.keys())



def test_mil::lowerequalscomparison_is_not_abstract():
    assert not inspect.isabstract(mil::LowerEqualsComparison)


def test_mil::lowerequalscomparison_constructor_exists():
    assert callable(mil::LowerEqualsComparison.__init__)


def test_mil::lowerequalscomparison_constructor_args():
    sig = inspect.signature(mil::LowerEqualsComparison.__init__)
    params = list(sig.parameters.keys())



def test_mil::greaterthancomparison_is_not_abstract():
    assert not inspect.isabstract(mil::GreaterThanComparison)


def test_mil::greaterthancomparison_constructor_exists():
    assert callable(mil::GreaterThanComparison.__init__)


def test_mil::greaterthancomparison_constructor_args():
    sig = inspect.signature(mil::GreaterThanComparison.__init__)
    params = list(sig.parameters.keys())



def test_mil::notequalscomparison_is_not_abstract():
    assert not inspect.isabstract(mil::NotEqualsComparison)


def test_mil::notequalscomparison_constructor_exists():
    assert callable(mil::NotEqualsComparison.__init__)


def test_mil::notequalscomparison_constructor_args():
    sig = inspect.signature(mil::NotEqualsComparison.__init__)
    params = list(sig.parameters.keys())



def test_mil::greaterequalscomparison_is_not_abstract():
    assert not inspect.isabstract(mil::GreaterEqualsComparison)


def test_mil::greaterequalscomparison_constructor_exists():
    assert callable(mil::GreaterEqualsComparison.__init__)


def test_mil::greaterequalscomparison_constructor_args():
    sig = inspect.signature(mil::GreaterEqualsComparison.__init__)
    params = list(sig.parameters.keys())



def test_mil::lowerthancomparison_is_not_abstract():
    assert not inspect.isabstract(mil::LowerThanComparison)


def test_mil::lowerthancomparison_constructor_exists():
    assert callable(mil::LowerThanComparison.__init__)


def test_mil::lowerthancomparison_constructor_args():
    sig = inspect.signature(mil::LowerThanComparison.__init__)
    params = list(sig.parameters.keys())



def test_mil::equalscomparison_is_not_abstract():
    assert not inspect.isabstract(mil::EqualsComparison)


def test_mil::equalscomparison_constructor_exists():
    assert callable(mil::EqualsComparison.__init__)


def test_mil::equalscomparison_constructor_args():
    sig = inspect.signature(mil::EqualsComparison.__init__)
    params = list(sig.parameters.keys())



def test_mil::comparison_is_not_abstract():
    assert not inspect.isabstract(mil::Comparison)


def test_mil::comparison_constructor_exists():
    assert callable(mil::Comparison.__init__)


def test_mil::comparison_constructor_args():
    sig = inspect.signature(mil::Comparison.__init__)
    params = list(sig.parameters.keys())



def test_jumper_is_not_abstract():
    assert not inspect.isabstract(Jumper)


def test_jumper_constructor_exists():
    assert callable(Jumper.__init__)


def test_jumper_constructor_args():
    sig = inspect.signature(Jumper.__init__)
    params = list(sig.parameters.keys())



def test_mil::callinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::CallInstruction)


def test_mil::callinstruction_constructor_exists():
    assert callable(mil::CallInstruction.__init__)


def test_mil::callinstruction_constructor_args():
    sig = inspect.signature(mil::CallInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::conditionaljumpinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::ConditionalJumpInstruction)


def test_mil::conditionaljumpinstruction_constructor_exists():
    assert callable(mil::ConditionalJumpInstruction.__init__)


def test_mil::conditionaljumpinstruction_constructor_args():
    sig = inspect.signature(mil::ConditionalJumpInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::jumpinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::JumpInstruction)


def test_mil::jumpinstruction_constructor_exists():
    assert callable(mil::JumpInstruction.__init__)


def test_mil::jumpinstruction_constructor_args():
    sig = inspect.signature(mil::JumpInstruction.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_mil::jumpmarker_is_not_abstract():
    assert not inspect.isabstract(mil::JumpMarker)


def test_mil::jumpmarker_constructor_exists():
    assert callable(mil::JumpMarker.__init__)


def test_mil::jumpmarker_constructor_args():
    sig = inspect.signature(mil::JumpMarker.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mil::jumpmarker_has_name():
    assert hasattr(mil::JumpMarker, "name")
    descriptor = None
    for klass in mil::JumpMarker.__mro__:
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



def test_mil::statement_is_not_abstract():
    assert not inspect.isabstract(mil::Statement)


def test_mil::statement_constructor_exists():
    assert callable(mil::Statement.__init__)


def test_mil::statement_constructor_args():
    sig = inspect.signature(mil::Statement.__init__)
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
BinaryOperation_strategy = st.builds(
    BinaryOperation,
)
mil::DivInstruction_strategy = st.builds(
    mil::DivInstruction,
)
mil::MultInstruction_strategy = st.builds(
    mil::MultInstruction,
)
mil::SubInstruction_strategy = st.builds(
    mil::SubInstruction,
)
mil::AddInstruction_strategy = st.builds(
    mil::AddInstruction,
)
mil::RegisterReference_strategy = st.builds(
    mil::RegisterReference,
    address=
        safe_text
)
UnaryOperation_strategy = st.builds(
    UnaryOperation,
)
mil::NegateInstruction_strategy = st.builds(
    mil::NegateInstruction,
)
mil::StoreInstruction_strategy = st.builds(
    mil::StoreInstruction,
)
mil::Value_strategy = st.builds(
    mil::Value,
)
Instruction_strategy = st.builds(
    Instruction,
)
mil::UnaryOperation_strategy = st.builds(
    mil::UnaryOperation,
)
mil::BinaryOperation_strategy = st.builds(
    mil::BinaryOperation,
)
mil::LoadInstruction_strategy = st.builds(
    mil::LoadInstruction,
)
mil::ReturnInstruction_strategy = st.builds(
    mil::ReturnInstruction,
)
mil::Jumper_strategy = st.builds(
    mil::Jumper,
)
mil::PrintInstruction_strategy = st.builds(
    mil::PrintInstruction,
    text=
        safe_text
)
mil::YieldInstruction_strategy = st.builds(
    mil::YieldInstruction,
)
Comparison_strategy = st.builds(
    Comparison,
)
mil::LowerEqualsComparison_strategy = st.builds(
    mil::LowerEqualsComparison,
)
mil::GreaterThanComparison_strategy = st.builds(
    mil::GreaterThanComparison,
)
mil::NotEqualsComparison_strategy = st.builds(
    mil::NotEqualsComparison,
)
mil::GreaterEqualsComparison_strategy = st.builds(
    mil::GreaterEqualsComparison,
)
mil::LowerThanComparison_strategy = st.builds(
    mil::LowerThanComparison,
)
mil::EqualsComparison_strategy = st.builds(
    mil::EqualsComparison,
)
mil::Comparison_strategy = st.builds(
    mil::Comparison,
)
Jumper_strategy = st.builds(
    Jumper,
)
mil::CallInstruction_strategy = st.builds(
    mil::CallInstruction,
)
mil::ConditionalJumpInstruction_strategy = st.builds(
    mil::ConditionalJumpInstruction,
)
mil::JumpInstruction_strategy = st.builds(
    mil::JumpInstruction,
)
Statement_strategy = st.builds(
    Statement,
)
mil::JumpMarker_strategy = st.builds(
    mil::JumpMarker,
    name=
        safe_text
)
mil::Instruction_strategy = st.builds(
    mil::Instruction,
)
mil::Statement_strategy = st.builds(
    mil::Statement,
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

@given(instance=BinaryOperation_strategy)
@settings(max_examples=50)
def test_binaryoperation_instantiation(instance):
    assert isinstance(instance, BinaryOperation)

@given(instance=mil::DivInstruction_strategy)
@settings(max_examples=50)
def test_mil::divinstruction_instantiation(instance):
    assert isinstance(instance, mil::DivInstruction)

@given(instance=mil::MultInstruction_strategy)
@settings(max_examples=50)
def test_mil::multinstruction_instantiation(instance):
    assert isinstance(instance, mil::MultInstruction)

@given(instance=mil::SubInstruction_strategy)
@settings(max_examples=50)
def test_mil::subinstruction_instantiation(instance):
    assert isinstance(instance, mil::SubInstruction)

@given(instance=mil::AddInstruction_strategy)
@settings(max_examples=50)
def test_mil::addinstruction_instantiation(instance):
    assert isinstance(instance, mil::AddInstruction)

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

@given(instance=UnaryOperation_strategy)
@settings(max_examples=50)
def test_unaryoperation_instantiation(instance):
    assert isinstance(instance, UnaryOperation)

@given(instance=mil::NegateInstruction_strategy)
@settings(max_examples=50)
def test_mil::negateinstruction_instantiation(instance):
    assert isinstance(instance, mil::NegateInstruction)

@given(instance=mil::StoreInstruction_strategy)
@settings(max_examples=50)
def test_mil::storeinstruction_instantiation(instance):
    assert isinstance(instance, mil::StoreInstruction)

@given(instance=mil::Value_strategy)
@settings(max_examples=50)
def test_mil::value_instantiation(instance):
    assert isinstance(instance, mil::Value)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=mil::UnaryOperation_strategy)
@settings(max_examples=50)
def test_mil::unaryoperation_instantiation(instance):
    assert isinstance(instance, mil::UnaryOperation)

@given(instance=mil::BinaryOperation_strategy)
@settings(max_examples=50)
def test_mil::binaryoperation_instantiation(instance):
    assert isinstance(instance, mil::BinaryOperation)

@given(instance=mil::LoadInstruction_strategy)
@settings(max_examples=50)
def test_mil::loadinstruction_instantiation(instance):
    assert isinstance(instance, mil::LoadInstruction)

@given(instance=mil::ReturnInstruction_strategy)
@settings(max_examples=50)
def test_mil::returninstruction_instantiation(instance):
    assert isinstance(instance, mil::ReturnInstruction)

@given(instance=mil::Jumper_strategy)
@settings(max_examples=50)
def test_mil::jumper_instantiation(instance):
    assert isinstance(instance, mil::Jumper)

@given(instance=mil::PrintInstruction_strategy)
@settings(max_examples=50)
def test_mil::printinstruction_instantiation(instance):
    assert isinstance(instance, mil::PrintInstruction)

@given(instance=mil::PrintInstruction_strategy)
def test_mil::printinstruction_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=mil::PrintInstruction_strategy)
def test_mil::printinstruction_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=mil::YieldInstruction_strategy)
@settings(max_examples=50)
def test_mil::yieldinstruction_instantiation(instance):
    assert isinstance(instance, mil::YieldInstruction)

@given(instance=Comparison_strategy)
@settings(max_examples=50)
def test_comparison_instantiation(instance):
    assert isinstance(instance, Comparison)

@given(instance=mil::LowerEqualsComparison_strategy)
@settings(max_examples=50)
def test_mil::lowerequalscomparison_instantiation(instance):
    assert isinstance(instance, mil::LowerEqualsComparison)

@given(instance=mil::GreaterThanComparison_strategy)
@settings(max_examples=50)
def test_mil::greaterthancomparison_instantiation(instance):
    assert isinstance(instance, mil::GreaterThanComparison)

@given(instance=mil::NotEqualsComparison_strategy)
@settings(max_examples=50)
def test_mil::notequalscomparison_instantiation(instance):
    assert isinstance(instance, mil::NotEqualsComparison)

@given(instance=mil::GreaterEqualsComparison_strategy)
@settings(max_examples=50)
def test_mil::greaterequalscomparison_instantiation(instance):
    assert isinstance(instance, mil::GreaterEqualsComparison)

@given(instance=mil::LowerThanComparison_strategy)
@settings(max_examples=50)
def test_mil::lowerthancomparison_instantiation(instance):
    assert isinstance(instance, mil::LowerThanComparison)

@given(instance=mil::EqualsComparison_strategy)
@settings(max_examples=50)
def test_mil::equalscomparison_instantiation(instance):
    assert isinstance(instance, mil::EqualsComparison)

@given(instance=mil::Comparison_strategy)
@settings(max_examples=50)
def test_mil::comparison_instantiation(instance):
    assert isinstance(instance, mil::Comparison)

@given(instance=Jumper_strategy)
@settings(max_examples=50)
def test_jumper_instantiation(instance):
    assert isinstance(instance, Jumper)

@given(instance=mil::CallInstruction_strategy)
@settings(max_examples=50)
def test_mil::callinstruction_instantiation(instance):
    assert isinstance(instance, mil::CallInstruction)

@given(instance=mil::ConditionalJumpInstruction_strategy)
@settings(max_examples=50)
def test_mil::conditionaljumpinstruction_instantiation(instance):
    assert isinstance(instance, mil::ConditionalJumpInstruction)

@given(instance=mil::JumpInstruction_strategy)
@settings(max_examples=50)
def test_mil::jumpinstruction_instantiation(instance):
    assert isinstance(instance, mil::JumpInstruction)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=mil::JumpMarker_strategy)
@settings(max_examples=50)
def test_mil::jumpmarker_instantiation(instance):
    assert isinstance(instance, mil::JumpMarker)

@given(instance=mil::JumpMarker_strategy)
def test_mil::jumpmarker_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mil::JumpMarker_strategy)
def test_mil::jumpmarker_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mil::Instruction_strategy)
@settings(max_examples=50)
def test_mil::instruction_instantiation(instance):
    assert isinstance(instance, mil::Instruction)

@given(instance=mil::Statement_strategy)
@settings(max_examples=50)
def test_mil::statement_instantiation(instance):
    assert isinstance(instance, mil::Statement)

@given(instance=mil::MILModel_strategy)
@settings(max_examples=50)
def test_mil::milmodel_instantiation(instance):
    assert isinstance(instance, mil::MILModel)
