import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Value,
    PrtInstruction,
    mil::ErrInstruction,
    mil::ConstantInteger,
    JumpInstruction,
    mil::JpcInstruction,
    mil::CalInstruction,
    mil::JmpInstruction,
    mil::Instruction,
    mil::MILModel,
    mil::RegisterReference,
    mil::Value,
    Instruction,
    mil::LtInstruction,
    mil::YldInstruction,
    mil::EqInstruction,
    mil::DivInstruction,
    mil::GtInstruction,
    mil::LabelInstruction,
    mil::GeqInstruction,
    mil::RetInstruction,
    mil::MulInstruction,
    mil::AddInstruction,
    mil::InpInstruction,
    mil::JumpInstruction,
    mil::NeqInstruction,
    mil::PrtInstruction,
    mil::StoreInstruction,
    mil::LeqInstruction,
    mil::SubInstruction,
    mil::NegInstruction,
    mil::LoadInstruction,
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



def test_prtinstruction_is_not_abstract():
    assert not inspect.isabstract(PrtInstruction)


def test_prtinstruction_constructor_exists():
    assert callable(PrtInstruction.__init__)


def test_prtinstruction_constructor_args():
    sig = inspect.signature(PrtInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::errinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::ErrInstruction)


def test_mil::errinstruction_constructor_exists():
    assert callable(mil::ErrInstruction.__init__)


def test_mil::errinstruction_constructor_args():
    sig = inspect.signature(mil::ErrInstruction.__init__)
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



def test_jumpinstruction_is_not_abstract():
    assert not inspect.isabstract(JumpInstruction)


def test_jumpinstruction_constructor_exists():
    assert callable(JumpInstruction.__init__)


def test_jumpinstruction_constructor_args():
    sig = inspect.signature(JumpInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::jpcinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::JpcInstruction)


def test_mil::jpcinstruction_constructor_exists():
    assert callable(mil::JpcInstruction.__init__)


def test_mil::jpcinstruction_constructor_args():
    sig = inspect.signature(mil::JpcInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::calinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::CalInstruction)


def test_mil::calinstruction_constructor_exists():
    assert callable(mil::CalInstruction.__init__)


def test_mil::calinstruction_constructor_args():
    sig = inspect.signature(mil::CalInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::jmpinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::JmpInstruction)


def test_mil::jmpinstruction_constructor_exists():
    assert callable(mil::JmpInstruction.__init__)


def test_mil::jmpinstruction_constructor_args():
    sig = inspect.signature(mil::JmpInstruction.__init__)
    params = list(sig.parameters.keys())



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



def test_mil::ltinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::LtInstruction)


def test_mil::ltinstruction_constructor_exists():
    assert callable(mil::LtInstruction.__init__)


def test_mil::ltinstruction_constructor_args():
    sig = inspect.signature(mil::LtInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::yldinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::YldInstruction)


def test_mil::yldinstruction_constructor_exists():
    assert callable(mil::YldInstruction.__init__)


def test_mil::yldinstruction_constructor_args():
    sig = inspect.signature(mil::YldInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::eqinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::EqInstruction)


def test_mil::eqinstruction_constructor_exists():
    assert callable(mil::EqInstruction.__init__)


def test_mil::eqinstruction_constructor_args():
    sig = inspect.signature(mil::EqInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::divinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::DivInstruction)


def test_mil::divinstruction_constructor_exists():
    assert callable(mil::DivInstruction.__init__)


def test_mil::divinstruction_constructor_args():
    sig = inspect.signature(mil::DivInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::gtinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::GtInstruction)


def test_mil::gtinstruction_constructor_exists():
    assert callable(mil::GtInstruction.__init__)


def test_mil::gtinstruction_constructor_args():
    sig = inspect.signature(mil::GtInstruction.__init__)
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



def test_mil::geqinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::GeqInstruction)


def test_mil::geqinstruction_constructor_exists():
    assert callable(mil::GeqInstruction.__init__)


def test_mil::geqinstruction_constructor_args():
    sig = inspect.signature(mil::GeqInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::retinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::RetInstruction)


def test_mil::retinstruction_constructor_exists():
    assert callable(mil::RetInstruction.__init__)


def test_mil::retinstruction_constructor_args():
    sig = inspect.signature(mil::RetInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::mulinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::MulInstruction)


def test_mil::mulinstruction_constructor_exists():
    assert callable(mil::MulInstruction.__init__)


def test_mil::mulinstruction_constructor_args():
    sig = inspect.signature(mil::MulInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::addinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::AddInstruction)


def test_mil::addinstruction_constructor_exists():
    assert callable(mil::AddInstruction.__init__)


def test_mil::addinstruction_constructor_args():
    sig = inspect.signature(mil::AddInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::inpinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::InpInstruction)


def test_mil::inpinstruction_constructor_exists():
    assert callable(mil::InpInstruction.__init__)


def test_mil::inpinstruction_constructor_args():
    sig = inspect.signature(mil::InpInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::jumpinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::JumpInstruction)


def test_mil::jumpinstruction_constructor_exists():
    assert callable(mil::JumpInstruction.__init__)


def test_mil::jumpinstruction_constructor_args():
    sig = inspect.signature(mil::JumpInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::neqinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::NeqInstruction)


def test_mil::neqinstruction_constructor_exists():
    assert callable(mil::NeqInstruction.__init__)


def test_mil::neqinstruction_constructor_args():
    sig = inspect.signature(mil::NeqInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::prtinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::PrtInstruction)


def test_mil::prtinstruction_constructor_exists():
    assert callable(mil::PrtInstruction.__init__)


def test_mil::prtinstruction_constructor_args():
    sig = inspect.signature(mil::PrtInstruction.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mil::prtinstruction_has_value():
    assert hasattr(mil::PrtInstruction, "value")
    descriptor = None
    for klass in mil::PrtInstruction.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mil::storeinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::StoreInstruction)


def test_mil::storeinstruction_constructor_exists():
    assert callable(mil::StoreInstruction.__init__)


def test_mil::storeinstruction_constructor_args():
    sig = inspect.signature(mil::StoreInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::leqinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::LeqInstruction)


def test_mil::leqinstruction_constructor_exists():
    assert callable(mil::LeqInstruction.__init__)


def test_mil::leqinstruction_constructor_args():
    sig = inspect.signature(mil::LeqInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::subinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::SubInstruction)


def test_mil::subinstruction_constructor_exists():
    assert callable(mil::SubInstruction.__init__)


def test_mil::subinstruction_constructor_args():
    sig = inspect.signature(mil::SubInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::neginstruction_is_not_abstract():
    assert not inspect.isabstract(mil::NegInstruction)


def test_mil::neginstruction_constructor_exists():
    assert callable(mil::NegInstruction.__init__)


def test_mil::neginstruction_constructor_args():
    sig = inspect.signature(mil::NegInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mil::loadinstruction_is_not_abstract():
    assert not inspect.isabstract(mil::LoadInstruction)


def test_mil::loadinstruction_constructor_exists():
    assert callable(mil::LoadInstruction.__init__)


def test_mil::loadinstruction_constructor_args():
    sig = inspect.signature(mil::LoadInstruction.__init__)
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
PrtInstruction_strategy = st.builds(
    PrtInstruction,
)
mil::ErrInstruction_strategy = st.builds(
    mil::ErrInstruction,
)
mil::ConstantInteger_strategy = st.builds(
    mil::ConstantInteger,
    rawValue=
        st.integers()
)
JumpInstruction_strategy = st.builds(
    JumpInstruction,
)
mil::JpcInstruction_strategy = st.builds(
    mil::JpcInstruction,
)
mil::CalInstruction_strategy = st.builds(
    mil::CalInstruction,
)
mil::JmpInstruction_strategy = st.builds(
    mil::JmpInstruction,
)
mil::Instruction_strategy = st.builds(
    mil::Instruction,
)
mil::MILModel_strategy = st.builds(
    mil::MILModel,
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
mil::LtInstruction_strategy = st.builds(
    mil::LtInstruction,
)
mil::YldInstruction_strategy = st.builds(
    mil::YldInstruction,
)
mil::EqInstruction_strategy = st.builds(
    mil::EqInstruction,
)
mil::DivInstruction_strategy = st.builds(
    mil::DivInstruction,
)
mil::GtInstruction_strategy = st.builds(
    mil::GtInstruction,
)
mil::LabelInstruction_strategy = st.builds(
    mil::LabelInstruction,
    name=
        safe_text
)
mil::GeqInstruction_strategy = st.builds(
    mil::GeqInstruction,
)
mil::RetInstruction_strategy = st.builds(
    mil::RetInstruction,
)
mil::MulInstruction_strategy = st.builds(
    mil::MulInstruction,
)
mil::AddInstruction_strategy = st.builds(
    mil::AddInstruction,
)
mil::InpInstruction_strategy = st.builds(
    mil::InpInstruction,
)
mil::JumpInstruction_strategy = st.builds(
    mil::JumpInstruction,
)
mil::NeqInstruction_strategy = st.builds(
    mil::NeqInstruction,
)
mil::PrtInstruction_strategy = st.builds(
    mil::PrtInstruction,
    value=
        safe_text
)
mil::StoreInstruction_strategy = st.builds(
    mil::StoreInstruction,
)
mil::LeqInstruction_strategy = st.builds(
    mil::LeqInstruction,
)
mil::SubInstruction_strategy = st.builds(
    mil::SubInstruction,
)
mil::NegInstruction_strategy = st.builds(
    mil::NegInstruction,
)
mil::LoadInstruction_strategy = st.builds(
    mil::LoadInstruction,
)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=PrtInstruction_strategy)
@settings(max_examples=50)
def test_prtinstruction_instantiation(instance):
    assert isinstance(instance, PrtInstruction)

@given(instance=mil::ErrInstruction_strategy)
@settings(max_examples=50)
def test_mil::errinstruction_instantiation(instance):
    assert isinstance(instance, mil::ErrInstruction)

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

@given(instance=JumpInstruction_strategy)
@settings(max_examples=50)
def test_jumpinstruction_instantiation(instance):
    assert isinstance(instance, JumpInstruction)

@given(instance=mil::JpcInstruction_strategy)
@settings(max_examples=50)
def test_mil::jpcinstruction_instantiation(instance):
    assert isinstance(instance, mil::JpcInstruction)

@given(instance=mil::CalInstruction_strategy)
@settings(max_examples=50)
def test_mil::calinstruction_instantiation(instance):
    assert isinstance(instance, mil::CalInstruction)

@given(instance=mil::JmpInstruction_strategy)
@settings(max_examples=50)
def test_mil::jmpinstruction_instantiation(instance):
    assert isinstance(instance, mil::JmpInstruction)

@given(instance=mil::Instruction_strategy)
@settings(max_examples=50)
def test_mil::instruction_instantiation(instance):
    assert isinstance(instance, mil::Instruction)

@given(instance=mil::MILModel_strategy)
@settings(max_examples=50)
def test_mil::milmodel_instantiation(instance):
    assert isinstance(instance, mil::MILModel)

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

@given(instance=mil::LtInstruction_strategy)
@settings(max_examples=50)
def test_mil::ltinstruction_instantiation(instance):
    assert isinstance(instance, mil::LtInstruction)

@given(instance=mil::YldInstruction_strategy)
@settings(max_examples=50)
def test_mil::yldinstruction_instantiation(instance):
    assert isinstance(instance, mil::YldInstruction)

@given(instance=mil::EqInstruction_strategy)
@settings(max_examples=50)
def test_mil::eqinstruction_instantiation(instance):
    assert isinstance(instance, mil::EqInstruction)

@given(instance=mil::DivInstruction_strategy)
@settings(max_examples=50)
def test_mil::divinstruction_instantiation(instance):
    assert isinstance(instance, mil::DivInstruction)

@given(instance=mil::GtInstruction_strategy)
@settings(max_examples=50)
def test_mil::gtinstruction_instantiation(instance):
    assert isinstance(instance, mil::GtInstruction)

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

@given(instance=mil::GeqInstruction_strategy)
@settings(max_examples=50)
def test_mil::geqinstruction_instantiation(instance):
    assert isinstance(instance, mil::GeqInstruction)

@given(instance=mil::RetInstruction_strategy)
@settings(max_examples=50)
def test_mil::retinstruction_instantiation(instance):
    assert isinstance(instance, mil::RetInstruction)

@given(instance=mil::MulInstruction_strategy)
@settings(max_examples=50)
def test_mil::mulinstruction_instantiation(instance):
    assert isinstance(instance, mil::MulInstruction)

@given(instance=mil::AddInstruction_strategy)
@settings(max_examples=50)
def test_mil::addinstruction_instantiation(instance):
    assert isinstance(instance, mil::AddInstruction)

@given(instance=mil::InpInstruction_strategy)
@settings(max_examples=50)
def test_mil::inpinstruction_instantiation(instance):
    assert isinstance(instance, mil::InpInstruction)

@given(instance=mil::JumpInstruction_strategy)
@settings(max_examples=50)
def test_mil::jumpinstruction_instantiation(instance):
    assert isinstance(instance, mil::JumpInstruction)

@given(instance=mil::NeqInstruction_strategy)
@settings(max_examples=50)
def test_mil::neqinstruction_instantiation(instance):
    assert isinstance(instance, mil::NeqInstruction)

@given(instance=mil::PrtInstruction_strategy)
@settings(max_examples=50)
def test_mil::prtinstruction_instantiation(instance):
    assert isinstance(instance, mil::PrtInstruction)

@given(instance=mil::PrtInstruction_strategy)
def test_mil::prtinstruction_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=mil::PrtInstruction_strategy)
def test_mil::prtinstruction_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mil::StoreInstruction_strategy)
@settings(max_examples=50)
def test_mil::storeinstruction_instantiation(instance):
    assert isinstance(instance, mil::StoreInstruction)

@given(instance=mil::LeqInstruction_strategy)
@settings(max_examples=50)
def test_mil::leqinstruction_instantiation(instance):
    assert isinstance(instance, mil::LeqInstruction)

@given(instance=mil::SubInstruction_strategy)
@settings(max_examples=50)
def test_mil::subinstruction_instantiation(instance):
    assert isinstance(instance, mil::SubInstruction)

@given(instance=mil::NegInstruction_strategy)
@settings(max_examples=50)
def test_mil::neginstruction_instantiation(instance):
    assert isinstance(instance, mil::NegInstruction)

@given(instance=mil::LoadInstruction_strategy)
@settings(max_examples=50)
def test_mil::loadinstruction_instantiation(instance):
    assert isinstance(instance, mil::LoadInstruction)
