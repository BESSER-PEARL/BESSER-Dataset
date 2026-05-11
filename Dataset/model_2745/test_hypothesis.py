import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    A,
    ModelElement,
    systemmodel::A,
    Sum,
    systemmodel::Sum2,
    systemmodel::Sum1,
    Block,
    systemmodel::SrcBlock,
    systemmodel::Sum,
    systemmodel::Test,
    systemmodel::UnitDelay,
    systemmodel::C,
    systemmodel::B,
    SMElement,
    systemmodel::ModelElement,
    systemmodel::Signal,
    systemmodel::Outport,
    systemmodel::Inport,
    systemmodel::Root,
    systemmodel::SystemModel,
    systemmodel::SMElement,
    systemmodel::Block,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::a_is_not_abstract():
    assert not inspect.isabstract(systemmodel::A)


def test_systemmodel::a_constructor_exists():
    assert callable(systemmodel::A.__init__)


def test_systemmodel::a_constructor_args():
    sig = inspect.signature(systemmodel::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "multiValAtt" in params, "Missing parameter 'multiValAtt'"

def test_systemmodel::a_has_name():
    assert hasattr(systemmodel::A, "name")
    descriptor = None
    for klass in systemmodel::A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_systemmodel::a_has_multiValAtt():
    assert hasattr(systemmodel::A, "multiValAtt")
    descriptor = None
    for klass in systemmodel::A.__mro__:
        if "multiValAtt" in klass.__dict__:
            descriptor = klass.__dict__["multiValAtt"]
            break
    assert isinstance(descriptor, property)



def test_sum_is_not_abstract():
    assert not inspect.isabstract(Sum)


def test_sum_constructor_exists():
    assert callable(Sum.__init__)


def test_sum_constructor_args():
    sig = inspect.signature(Sum.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::sum2_is_not_abstract():
    assert not inspect.isabstract(systemmodel::Sum2)


def test_systemmodel::sum2_constructor_exists():
    assert callable(systemmodel::Sum2.__init__)


def test_systemmodel::sum2_constructor_args():
    sig = inspect.signature(systemmodel::Sum2.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::sum1_is_not_abstract():
    assert not inspect.isabstract(systemmodel::Sum1)


def test_systemmodel::sum1_constructor_exists():
    assert callable(systemmodel::Sum1.__init__)


def test_systemmodel::sum1_constructor_args():
    sig = inspect.signature(systemmodel::Sum1.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::srcblock_is_not_abstract():
    assert not inspect.isabstract(systemmodel::SrcBlock)


def test_systemmodel::srcblock_constructor_exists():
    assert callable(systemmodel::SrcBlock.__init__)


def test_systemmodel::srcblock_constructor_args():
    sig = inspect.signature(systemmodel::SrcBlock.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::sum_is_not_abstract():
    assert not inspect.isabstract(systemmodel::Sum)


def test_systemmodel::sum_constructor_exists():
    assert callable(systemmodel::Sum.__init__)


def test_systemmodel::sum_constructor_args():
    sig = inspect.signature(systemmodel::Sum.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::test_is_not_abstract():
    assert not inspect.isabstract(systemmodel::Test)


def test_systemmodel::test_constructor_exists():
    assert callable(systemmodel::Test.__init__)


def test_systemmodel::test_constructor_args():
    sig = inspect.signature(systemmodel::Test.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::unitdelay_is_not_abstract():
    assert not inspect.isabstract(systemmodel::UnitDelay)


def test_systemmodel::unitdelay_constructor_exists():
    assert callable(systemmodel::UnitDelay.__init__)


def test_systemmodel::unitdelay_constructor_args():
    sig = inspect.signature(systemmodel::UnitDelay.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::c_is_not_abstract():
    assert not inspect.isabstract(systemmodel::C)


def test_systemmodel::c_constructor_exists():
    assert callable(systemmodel::C.__init__)


def test_systemmodel::c_constructor_args():
    sig = inspect.signature(systemmodel::C.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_systemmodel::c_has_name():
    assert hasattr(systemmodel::C, "name")
    descriptor = None
    for klass in systemmodel::C.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_systemmodel::b_is_not_abstract():
    assert not inspect.isabstract(systemmodel::B)


def test_systemmodel::b_constructor_exists():
    assert callable(systemmodel::B.__init__)


def test_systemmodel::b_constructor_args():
    sig = inspect.signature(systemmodel::B.__init__)
    params = list(sig.parameters.keys())



def test_smelement_is_not_abstract():
    assert not inspect.isabstract(SMElement)


def test_smelement_constructor_exists():
    assert callable(SMElement.__init__)


def test_smelement_constructor_args():
    sig = inspect.signature(SMElement.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::modelelement_is_not_abstract():
    assert not inspect.isabstract(systemmodel::ModelElement)


def test_systemmodel::modelelement_constructor_exists():
    assert callable(systemmodel::ModelElement.__init__)


def test_systemmodel::modelelement_constructor_args():
    sig = inspect.signature(systemmodel::ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::signal_is_not_abstract():
    assert not inspect.isabstract(systemmodel::Signal)


def test_systemmodel::signal_constructor_exists():
    assert callable(systemmodel::Signal.__init__)


def test_systemmodel::signal_constructor_args():
    sig = inspect.signature(systemmodel::Signal.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::outport_is_not_abstract():
    assert not inspect.isabstract(systemmodel::Outport)


def test_systemmodel::outport_constructor_exists():
    assert callable(systemmodel::Outport.__init__)


def test_systemmodel::outport_constructor_args():
    sig = inspect.signature(systemmodel::Outport.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::inport_is_not_abstract():
    assert not inspect.isabstract(systemmodel::Inport)


def test_systemmodel::inport_constructor_exists():
    assert callable(systemmodel::Inport.__init__)


def test_systemmodel::inport_constructor_args():
    sig = inspect.signature(systemmodel::Inport.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::root_is_not_abstract():
    assert not inspect.isabstract(systemmodel::Root)


def test_systemmodel::root_constructor_exists():
    assert callable(systemmodel::Root.__init__)


def test_systemmodel::root_constructor_args():
    sig = inspect.signature(systemmodel::Root.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::systemmodel_is_not_abstract():
    assert not inspect.isabstract(systemmodel::SystemModel)


def test_systemmodel::systemmodel_constructor_exists():
    assert callable(systemmodel::SystemModel.__init__)


def test_systemmodel::systemmodel_constructor_args():
    sig = inspect.signature(systemmodel::SystemModel.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::smelement_is_not_abstract():
    assert not inspect.isabstract(systemmodel::SMElement)


def test_systemmodel::smelement_constructor_exists():
    assert callable(systemmodel::SMElement.__init__)


def test_systemmodel::smelement_constructor_args():
    sig = inspect.signature(systemmodel::SMElement.__init__)
    params = list(sig.parameters.keys())



def test_systemmodel::block_is_not_abstract():
    assert not inspect.isabstract(systemmodel::Block)


def test_systemmodel::block_constructor_exists():
    assert callable(systemmodel::Block.__init__)


def test_systemmodel::block_constructor_args():
    sig = inspect.signature(systemmodel::Block.__init__)
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
A_strategy = st.builds(
    A,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
systemmodel::A_strategy = st.builds(
    systemmodel::A,
    name=
        safe_text,
    multiValAtt=
        safe_text
)
Sum_strategy = st.builds(
    Sum,
)
systemmodel::Sum2_strategy = st.builds(
    systemmodel::Sum2,
)
systemmodel::Sum1_strategy = st.builds(
    systemmodel::Sum1,
)
Block_strategy = st.builds(
    Block,
)
systemmodel::SrcBlock_strategy = st.builds(
    systemmodel::SrcBlock,
)
systemmodel::Sum_strategy = st.builds(
    systemmodel::Sum,
)
systemmodel::Test_strategy = st.builds(
    systemmodel::Test,
)
systemmodel::UnitDelay_strategy = st.builds(
    systemmodel::UnitDelay,
)
systemmodel::C_strategy = st.builds(
    systemmodel::C,
    name=
        safe_text
)
systemmodel::B_strategy = st.builds(
    systemmodel::B,
)
SMElement_strategy = st.builds(
    SMElement,
)
systemmodel::ModelElement_strategy = st.builds(
    systemmodel::ModelElement,
)
systemmodel::Signal_strategy = st.builds(
    systemmodel::Signal,
)
systemmodel::Outport_strategy = st.builds(
    systemmodel::Outport,
)
systemmodel::Inport_strategy = st.builds(
    systemmodel::Inport,
)
systemmodel::Root_strategy = st.builds(
    systemmodel::Root,
)
systemmodel::SystemModel_strategy = st.builds(
    systemmodel::SystemModel,
)
systemmodel::SMElement_strategy = st.builds(
    systemmodel::SMElement,
)
systemmodel::Block_strategy = st.builds(
    systemmodel::Block,
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=systemmodel::A_strategy)
@settings(max_examples=50)
def test_systemmodel::a_instantiation(instance):
    assert isinstance(instance, systemmodel::A)

@given(instance=systemmodel::A_strategy)
def test_systemmodel::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=systemmodel::A_strategy)
def test_systemmodel::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=systemmodel::A_strategy)
def test_systemmodel::a_multiValAtt_type(instance):
    assert isinstance(instance.multiValAtt, str)


@given(instance=systemmodel::A_strategy)
def test_systemmodel::a_multiValAtt_setter(instance):
    original = instance.multiValAtt
    instance.multiValAtt = original
    assert instance.multiValAtt == original

@given(instance=Sum_strategy)
@settings(max_examples=50)
def test_sum_instantiation(instance):
    assert isinstance(instance, Sum)

@given(instance=systemmodel::Sum2_strategy)
@settings(max_examples=50)
def test_systemmodel::sum2_instantiation(instance):
    assert isinstance(instance, systemmodel::Sum2)

@given(instance=systemmodel::Sum1_strategy)
@settings(max_examples=50)
def test_systemmodel::sum1_instantiation(instance):
    assert isinstance(instance, systemmodel::Sum1)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=systemmodel::SrcBlock_strategy)
@settings(max_examples=50)
def test_systemmodel::srcblock_instantiation(instance):
    assert isinstance(instance, systemmodel::SrcBlock)

@given(instance=systemmodel::Sum_strategy)
@settings(max_examples=50)
def test_systemmodel::sum_instantiation(instance):
    assert isinstance(instance, systemmodel::Sum)

@given(instance=systemmodel::Test_strategy)
@settings(max_examples=50)
def test_systemmodel::test_instantiation(instance):
    assert isinstance(instance, systemmodel::Test)

@given(instance=systemmodel::UnitDelay_strategy)
@settings(max_examples=50)
def test_systemmodel::unitdelay_instantiation(instance):
    assert isinstance(instance, systemmodel::UnitDelay)

@given(instance=systemmodel::C_strategy)
@settings(max_examples=50)
def test_systemmodel::c_instantiation(instance):
    assert isinstance(instance, systemmodel::C)

@given(instance=systemmodel::C_strategy)
def test_systemmodel::c_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=systemmodel::C_strategy)
def test_systemmodel::c_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=systemmodel::B_strategy)
@settings(max_examples=50)
def test_systemmodel::b_instantiation(instance):
    assert isinstance(instance, systemmodel::B)

@given(instance=SMElement_strategy)
@settings(max_examples=50)
def test_smelement_instantiation(instance):
    assert isinstance(instance, SMElement)

@given(instance=systemmodel::ModelElement_strategy)
@settings(max_examples=50)
def test_systemmodel::modelelement_instantiation(instance):
    assert isinstance(instance, systemmodel::ModelElement)

@given(instance=systemmodel::Signal_strategy)
@settings(max_examples=50)
def test_systemmodel::signal_instantiation(instance):
    assert isinstance(instance, systemmodel::Signal)

@given(instance=systemmodel::Outport_strategy)
@settings(max_examples=50)
def test_systemmodel::outport_instantiation(instance):
    assert isinstance(instance, systemmodel::Outport)

@given(instance=systemmodel::Inport_strategy)
@settings(max_examples=50)
def test_systemmodel::inport_instantiation(instance):
    assert isinstance(instance, systemmodel::Inport)

@given(instance=systemmodel::Root_strategy)
@settings(max_examples=50)
def test_systemmodel::root_instantiation(instance):
    assert isinstance(instance, systemmodel::Root)

@given(instance=systemmodel::SystemModel_strategy)
@settings(max_examples=50)
def test_systemmodel::systemmodel_instantiation(instance):
    assert isinstance(instance, systemmodel::SystemModel)

@given(instance=systemmodel::SMElement_strategy)
@settings(max_examples=50)
def test_systemmodel::smelement_instantiation(instance):
    assert isinstance(instance, systemmodel::SMElement)

@given(instance=systemmodel::Block_strategy)
@settings(max_examples=50)
def test_systemmodel::block_instantiation(instance):
    assert isinstance(instance, systemmodel::Block)
