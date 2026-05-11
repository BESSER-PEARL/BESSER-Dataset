import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    VHDLModel::VHDLSpecification,
    Port,
    VHDLModel::Signal,
    VHDLModel::Port,
    ComplexBlock,
    VHDLModel::CompositeBlock,
    VHDLModel::BlockRef,
    VHDLModel::Block,
    VHDLModel::OutputPort,
    VHDLModel::InputPort,
    Block,
    VHDLModel::ComplexBlock,
    VHDLModel::BinaryGate,
    BinaryGate,
    VHDLModel::OrGate,
    VHDLModel::AndGate,
    VHDLModel::NotGate,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vhdlmodel::vhdlspecification_is_not_abstract():
    assert not inspect.isabstract(VHDLModel::VHDLSpecification)


def test_vhdlmodel::vhdlspecification_constructor_exists():
    assert callable(VHDLModel::VHDLSpecification.__init__)


def test_vhdlmodel::vhdlspecification_constructor_args():
    sig = inspect.signature(VHDLModel::VHDLSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdlmodel::vhdlspecification_has_name():
    assert hasattr(VHDLModel::VHDLSpecification, "name")
    descriptor = None
    for klass in VHDLModel::VHDLSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_vhdlmodel::signal_is_not_abstract():
    assert not inspect.isabstract(VHDLModel::Signal)


def test_vhdlmodel::signal_constructor_exists():
    assert callable(VHDLModel::Signal.__init__)


def test_vhdlmodel::signal_constructor_args():
    sig = inspect.signature(VHDLModel::Signal.__init__)
    params = list(sig.parameters.keys())



def test_vhdlmodel::port_is_not_abstract():
    assert not inspect.isabstract(VHDLModel::Port)


def test_vhdlmodel::port_constructor_exists():
    assert callable(VHDLModel::Port.__init__)


def test_vhdlmodel::port_constructor_args():
    sig = inspect.signature(VHDLModel::Port.__init__)
    params = list(sig.parameters.keys())
    assert "high" in params, "Missing parameter 'high'"
    assert "name" in params, "Missing parameter 'name'"

def test_vhdlmodel::port_has_high():
    assert hasattr(VHDLModel::Port, "high")
    descriptor = None
    for klass in VHDLModel::Port.__mro__:
        if "high" in klass.__dict__:
            descriptor = klass.__dict__["high"]
            break
    assert isinstance(descriptor, property)

def test_vhdlmodel::port_has_name():
    assert hasattr(VHDLModel::Port, "name")
    descriptor = None
    for klass in VHDLModel::Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_complexblock_is_not_abstract():
    assert not inspect.isabstract(ComplexBlock)


def test_complexblock_constructor_exists():
    assert callable(ComplexBlock.__init__)


def test_complexblock_constructor_args():
    sig = inspect.signature(ComplexBlock.__init__)
    params = list(sig.parameters.keys())



def test_vhdlmodel::compositeblock_is_not_abstract():
    assert not inspect.isabstract(VHDLModel::CompositeBlock)


def test_vhdlmodel::compositeblock_constructor_exists():
    assert callable(VHDLModel::CompositeBlock.__init__)


def test_vhdlmodel::compositeblock_constructor_args():
    sig = inspect.signature(VHDLModel::CompositeBlock.__init__)
    params = list(sig.parameters.keys())



def test_vhdlmodel::blockref_is_not_abstract():
    assert not inspect.isabstract(VHDLModel::BlockRef)


def test_vhdlmodel::blockref_constructor_exists():
    assert callable(VHDLModel::BlockRef.__init__)


def test_vhdlmodel::blockref_constructor_args():
    sig = inspect.signature(VHDLModel::BlockRef.__init__)
    params = list(sig.parameters.keys())



def test_vhdlmodel::block_is_not_abstract():
    assert not inspect.isabstract(VHDLModel::Block)


def test_vhdlmodel::block_constructor_exists():
    assert callable(VHDLModel::Block.__init__)


def test_vhdlmodel::block_constructor_args():
    sig = inspect.signature(VHDLModel::Block.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdlmodel::block_has_name():
    assert hasattr(VHDLModel::Block, "name")
    descriptor = None
    for klass in VHDLModel::Block.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdlmodel::outputport_is_not_abstract():
    assert not inspect.isabstract(VHDLModel::OutputPort)


def test_vhdlmodel::outputport_constructor_exists():
    assert callable(VHDLModel::OutputPort.__init__)


def test_vhdlmodel::outputport_constructor_args():
    sig = inspect.signature(VHDLModel::OutputPort.__init__)
    params = list(sig.parameters.keys())



def test_vhdlmodel::inputport_is_not_abstract():
    assert not inspect.isabstract(VHDLModel::InputPort)


def test_vhdlmodel::inputport_constructor_exists():
    assert callable(VHDLModel::InputPort.__init__)


def test_vhdlmodel::inputport_constructor_args():
    sig = inspect.signature(VHDLModel::InputPort.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_vhdlmodel::complexblock_is_not_abstract():
    assert not inspect.isabstract(VHDLModel::ComplexBlock)


def test_vhdlmodel::complexblock_constructor_exists():
    assert callable(VHDLModel::ComplexBlock.__init__)


def test_vhdlmodel::complexblock_constructor_args():
    sig = inspect.signature(VHDLModel::ComplexBlock.__init__)
    params = list(sig.parameters.keys())



def test_vhdlmodel::binarygate_is_not_abstract():
    assert not inspect.isabstract(VHDLModel::BinaryGate)


def test_vhdlmodel::binarygate_constructor_exists():
    assert callable(VHDLModel::BinaryGate.__init__)


def test_vhdlmodel::binarygate_constructor_args():
    sig = inspect.signature(VHDLModel::BinaryGate.__init__)
    params = list(sig.parameters.keys())



def test_binarygate_is_not_abstract():
    assert not inspect.isabstract(BinaryGate)


def test_binarygate_constructor_exists():
    assert callable(BinaryGate.__init__)


def test_binarygate_constructor_args():
    sig = inspect.signature(BinaryGate.__init__)
    params = list(sig.parameters.keys())



def test_vhdlmodel::orgate_is_not_abstract():
    assert not inspect.isabstract(VHDLModel::OrGate)


def test_vhdlmodel::orgate_constructor_exists():
    assert callable(VHDLModel::OrGate.__init__)


def test_vhdlmodel::orgate_constructor_args():
    sig = inspect.signature(VHDLModel::OrGate.__init__)
    params = list(sig.parameters.keys())



def test_vhdlmodel::andgate_is_not_abstract():
    assert not inspect.isabstract(VHDLModel::AndGate)


def test_vhdlmodel::andgate_constructor_exists():
    assert callable(VHDLModel::AndGate.__init__)


def test_vhdlmodel::andgate_constructor_args():
    sig = inspect.signature(VHDLModel::AndGate.__init__)
    params = list(sig.parameters.keys())



def test_vhdlmodel::notgate_is_not_abstract():
    assert not inspect.isabstract(VHDLModel::NotGate)


def test_vhdlmodel::notgate_constructor_exists():
    assert callable(VHDLModel::NotGate.__init__)


def test_vhdlmodel::notgate_constructor_args():
    sig = inspect.signature(VHDLModel::NotGate.__init__)
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
VHDLModel::VHDLSpecification_strategy = st.builds(
    VHDLModel::VHDLSpecification,
    name=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
VHDLModel::Signal_strategy = st.builds(
    VHDLModel::Signal,
)
VHDLModel::Port_strategy = st.builds(
    VHDLModel::Port,
    high=
        st.booleans(),
    name=
        safe_text
)
ComplexBlock_strategy = st.builds(
    ComplexBlock,
)
VHDLModel::CompositeBlock_strategy = st.builds(
    VHDLModel::CompositeBlock,
)
VHDLModel::BlockRef_strategy = st.builds(
    VHDLModel::BlockRef,
)
VHDLModel::Block_strategy = st.builds(
    VHDLModel::Block,
    name=
        safe_text
)
VHDLModel::OutputPort_strategy = st.builds(
    VHDLModel::OutputPort,
)
VHDLModel::InputPort_strategy = st.builds(
    VHDLModel::InputPort,
)
Block_strategy = st.builds(
    Block,
)
VHDLModel::ComplexBlock_strategy = st.builds(
    VHDLModel::ComplexBlock,
)
VHDLModel::BinaryGate_strategy = st.builds(
    VHDLModel::BinaryGate,
)
BinaryGate_strategy = st.builds(
    BinaryGate,
)
VHDLModel::OrGate_strategy = st.builds(
    VHDLModel::OrGate,
)
VHDLModel::AndGate_strategy = st.builds(
    VHDLModel::AndGate,
)
VHDLModel::NotGate_strategy = st.builds(
    VHDLModel::NotGate,
)

@given(instance=VHDLModel::VHDLSpecification_strategy)
@settings(max_examples=50)
def test_vhdlmodel::vhdlspecification_instantiation(instance):
    assert isinstance(instance, VHDLModel::VHDLSpecification)

@given(instance=VHDLModel::VHDLSpecification_strategy)
def test_vhdlmodel::vhdlspecification_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=VHDLModel::VHDLSpecification_strategy)
def test_vhdlmodel::vhdlspecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=VHDLModel::Signal_strategy)
@settings(max_examples=50)
def test_vhdlmodel::signal_instantiation(instance):
    assert isinstance(instance, VHDLModel::Signal)

@given(instance=VHDLModel::Port_strategy)
@settings(max_examples=50)
def test_vhdlmodel::port_instantiation(instance):
    assert isinstance(instance, VHDLModel::Port)

@given(instance=VHDLModel::Port_strategy)
def test_vhdlmodel::port_high_type(instance):
    assert isinstance(instance.high, bool)


@given(instance=VHDLModel::Port_strategy)
def test_vhdlmodel::port_high_setter(instance):
    original = instance.high
    instance.high = original
    assert instance.high == original

@given(instance=VHDLModel::Port_strategy)
def test_vhdlmodel::port_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=VHDLModel::Port_strategy)
def test_vhdlmodel::port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ComplexBlock_strategy)
@settings(max_examples=50)
def test_complexblock_instantiation(instance):
    assert isinstance(instance, ComplexBlock)

@given(instance=VHDLModel::CompositeBlock_strategy)
@settings(max_examples=50)
def test_vhdlmodel::compositeblock_instantiation(instance):
    assert isinstance(instance, VHDLModel::CompositeBlock)

@given(instance=VHDLModel::BlockRef_strategy)
@settings(max_examples=50)
def test_vhdlmodel::blockref_instantiation(instance):
    assert isinstance(instance, VHDLModel::BlockRef)

@given(instance=VHDLModel::Block_strategy)
@settings(max_examples=50)
def test_vhdlmodel::block_instantiation(instance):
    assert isinstance(instance, VHDLModel::Block)

@given(instance=VHDLModel::Block_strategy)
def test_vhdlmodel::block_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=VHDLModel::Block_strategy)
def test_vhdlmodel::block_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=VHDLModel::OutputPort_strategy)
@settings(max_examples=50)
def test_vhdlmodel::outputport_instantiation(instance):
    assert isinstance(instance, VHDLModel::OutputPort)

@given(instance=VHDLModel::InputPort_strategy)
@settings(max_examples=50)
def test_vhdlmodel::inputport_instantiation(instance):
    assert isinstance(instance, VHDLModel::InputPort)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=VHDLModel::ComplexBlock_strategy)
@settings(max_examples=50)
def test_vhdlmodel::complexblock_instantiation(instance):
    assert isinstance(instance, VHDLModel::ComplexBlock)

@given(instance=VHDLModel::BinaryGate_strategy)
@settings(max_examples=50)
def test_vhdlmodel::binarygate_instantiation(instance):
    assert isinstance(instance, VHDLModel::BinaryGate)

@given(instance=BinaryGate_strategy)
@settings(max_examples=50)
def test_binarygate_instantiation(instance):
    assert isinstance(instance, BinaryGate)

@given(instance=VHDLModel::OrGate_strategy)
@settings(max_examples=50)
def test_vhdlmodel::orgate_instantiation(instance):
    assert isinstance(instance, VHDLModel::OrGate)

@given(instance=VHDLModel::AndGate_strategy)
@settings(max_examples=50)
def test_vhdlmodel::andgate_instantiation(instance):
    assert isinstance(instance, VHDLModel::AndGate)

@given(instance=VHDLModel::NotGate_strategy)
@settings(max_examples=50)
def test_vhdlmodel::notgate_instantiation(instance):
    assert isinstance(instance, VHDLModel::NotGate)
