import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    llp::Block,
    ControlFlowInstruction,
    llp::RepetitionInstruction,
    llp::SkipInstruction,
    llp::ParenthesisInstruction,
    llp::ControlFlowBranchingInstruction,
    SynchronisationInstruction,
    llp::UnlockInstruction,
    llp::LockInstruction,
    CacheInstruction,
    llp::CommitInstruction,
    llp::MemoryReference,
    DataAccessPattern,
    llp::CacheInstruction,
    llp::SynchronisationInstruction,
    llp::SpawnInstruction,
    llp::ControlFlowInstruction,
    llp::IOInstruction,
    IOInstruction,
    llp::WriteInstruction,
    llp::ReadInstruction,
    llp::DataAccessPattern,
    llp::Task,
    llp::LowLevelProgram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_llp::block_is_not_abstract():
    assert not inspect.isabstract(llp::Block)


def test_llp::block_constructor_exists():
    assert callable(llp::Block.__init__)


def test_llp::block_constructor_args():
    sig = inspect.signature(llp::Block.__init__)
    params = list(sig.parameters.keys())



def test_controlflowinstruction_is_not_abstract():
    assert not inspect.isabstract(ControlFlowInstruction)


def test_controlflowinstruction_constructor_exists():
    assert callable(ControlFlowInstruction.__init__)


def test_controlflowinstruction_constructor_args():
    sig = inspect.signature(ControlFlowInstruction.__init__)
    params = list(sig.parameters.keys())



def test_llp::repetitioninstruction_is_not_abstract():
    assert not inspect.isabstract(llp::RepetitionInstruction)


def test_llp::repetitioninstruction_constructor_exists():
    assert callable(llp::RepetitionInstruction.__init__)


def test_llp::repetitioninstruction_constructor_args():
    sig = inspect.signature(llp::RepetitionInstruction.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfRepetitions" in params, "Missing parameter 'numberOfRepetitions'"

def test_llp::repetitioninstruction_has_numberOfRepetitions():
    assert hasattr(llp::RepetitionInstruction, "numberOfRepetitions")
    descriptor = None
    for klass in llp::RepetitionInstruction.__mro__:
        if "numberOfRepetitions" in klass.__dict__:
            descriptor = klass.__dict__["numberOfRepetitions"]
            break
    assert isinstance(descriptor, property)



def test_llp::skipinstruction_is_not_abstract():
    assert not inspect.isabstract(llp::SkipInstruction)


def test_llp::skipinstruction_constructor_exists():
    assert callable(llp::SkipInstruction.__init__)


def test_llp::skipinstruction_constructor_args():
    sig = inspect.signature(llp::SkipInstruction.__init__)
    params = list(sig.parameters.keys())



def test_llp::parenthesisinstruction_is_not_abstract():
    assert not inspect.isabstract(llp::ParenthesisInstruction)


def test_llp::parenthesisinstruction_constructor_exists():
    assert callable(llp::ParenthesisInstruction.__init__)


def test_llp::parenthesisinstruction_constructor_args():
    sig = inspect.signature(llp::ParenthesisInstruction.__init__)
    params = list(sig.parameters.keys())



def test_llp::controlflowbranchinginstruction_is_not_abstract():
    assert not inspect.isabstract(llp::ControlFlowBranchingInstruction)


def test_llp::controlflowbranchinginstruction_constructor_exists():
    assert callable(llp::ControlFlowBranchingInstruction.__init__)


def test_llp::controlflowbranchinginstruction_constructor_args():
    sig = inspect.signature(llp::ControlFlowBranchingInstruction.__init__)
    params = list(sig.parameters.keys())



def test_synchronisationinstruction_is_not_abstract():
    assert not inspect.isabstract(SynchronisationInstruction)


def test_synchronisationinstruction_constructor_exists():
    assert callable(SynchronisationInstruction.__init__)


def test_synchronisationinstruction_constructor_args():
    sig = inspect.signature(SynchronisationInstruction.__init__)
    params = list(sig.parameters.keys())



def test_llp::unlockinstruction_is_not_abstract():
    assert not inspect.isabstract(llp::UnlockInstruction)


def test_llp::unlockinstruction_constructor_exists():
    assert callable(llp::UnlockInstruction.__init__)


def test_llp::unlockinstruction_constructor_args():
    sig = inspect.signature(llp::UnlockInstruction.__init__)
    params = list(sig.parameters.keys())



def test_llp::lockinstruction_is_not_abstract():
    assert not inspect.isabstract(llp::LockInstruction)


def test_llp::lockinstruction_constructor_exists():
    assert callable(llp::LockInstruction.__init__)


def test_llp::lockinstruction_constructor_args():
    sig = inspect.signature(llp::LockInstruction.__init__)
    params = list(sig.parameters.keys())



def test_cacheinstruction_is_not_abstract():
    assert not inspect.isabstract(CacheInstruction)


def test_cacheinstruction_constructor_exists():
    assert callable(CacheInstruction.__init__)


def test_cacheinstruction_constructor_args():
    sig = inspect.signature(CacheInstruction.__init__)
    params = list(sig.parameters.keys())



def test_llp::commitinstruction_is_not_abstract():
    assert not inspect.isabstract(llp::CommitInstruction)


def test_llp::commitinstruction_constructor_exists():
    assert callable(llp::CommitInstruction.__init__)


def test_llp::commitinstruction_constructor_args():
    sig = inspect.signature(llp::CommitInstruction.__init__)
    params = list(sig.parameters.keys())



def test_llp::memoryreference_is_not_abstract():
    assert not inspect.isabstract(llp::MemoryReference)


def test_llp::memoryreference_constructor_exists():
    assert callable(llp::MemoryReference.__init__)


def test_llp::memoryreference_constructor_args():
    sig = inspect.signature(llp::MemoryReference.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_llp::memoryreference_has_address():
    assert hasattr(llp::MemoryReference, "address")
    descriptor = None
    for klass in llp::MemoryReference.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_dataaccesspattern_is_not_abstract():
    assert not inspect.isabstract(DataAccessPattern)


def test_dataaccesspattern_constructor_exists():
    assert callable(DataAccessPattern.__init__)


def test_dataaccesspattern_constructor_args():
    sig = inspect.signature(DataAccessPattern.__init__)
    params = list(sig.parameters.keys())



def test_llp::cacheinstruction_is_not_abstract():
    assert not inspect.isabstract(llp::CacheInstruction)


def test_llp::cacheinstruction_constructor_exists():
    assert callable(llp::CacheInstruction.__init__)


def test_llp::cacheinstruction_constructor_args():
    sig = inspect.signature(llp::CacheInstruction.__init__)
    params = list(sig.parameters.keys())



def test_llp::synchronisationinstruction_is_not_abstract():
    assert not inspect.isabstract(llp::SynchronisationInstruction)


def test_llp::synchronisationinstruction_constructor_exists():
    assert callable(llp::SynchronisationInstruction.__init__)


def test_llp::synchronisationinstruction_constructor_args():
    sig = inspect.signature(llp::SynchronisationInstruction.__init__)
    params = list(sig.parameters.keys())



def test_llp::spawninstruction_is_not_abstract():
    assert not inspect.isabstract(llp::SpawnInstruction)


def test_llp::spawninstruction_constructor_exists():
    assert callable(llp::SpawnInstruction.__init__)


def test_llp::spawninstruction_constructor_args():
    sig = inspect.signature(llp::SpawnInstruction.__init__)
    params = list(sig.parameters.keys())



def test_llp::controlflowinstruction_is_not_abstract():
    assert not inspect.isabstract(llp::ControlFlowInstruction)


def test_llp::controlflowinstruction_constructor_exists():
    assert callable(llp::ControlFlowInstruction.__init__)


def test_llp::controlflowinstruction_constructor_args():
    sig = inspect.signature(llp::ControlFlowInstruction.__init__)
    params = list(sig.parameters.keys())



def test_llp::ioinstruction_is_not_abstract():
    assert not inspect.isabstract(llp::IOInstruction)


def test_llp::ioinstruction_constructor_exists():
    assert callable(llp::IOInstruction.__init__)


def test_llp::ioinstruction_constructor_args():
    sig = inspect.signature(llp::IOInstruction.__init__)
    params = list(sig.parameters.keys())



def test_ioinstruction_is_not_abstract():
    assert not inspect.isabstract(IOInstruction)


def test_ioinstruction_constructor_exists():
    assert callable(IOInstruction.__init__)


def test_ioinstruction_constructor_args():
    sig = inspect.signature(IOInstruction.__init__)
    params = list(sig.parameters.keys())



def test_llp::writeinstruction_is_not_abstract():
    assert not inspect.isabstract(llp::WriteInstruction)


def test_llp::writeinstruction_constructor_exists():
    assert callable(llp::WriteInstruction.__init__)


def test_llp::writeinstruction_constructor_args():
    sig = inspect.signature(llp::WriteInstruction.__init__)
    params = list(sig.parameters.keys())



def test_llp::readinstruction_is_not_abstract():
    assert not inspect.isabstract(llp::ReadInstruction)


def test_llp::readinstruction_constructor_exists():
    assert callable(llp::ReadInstruction.__init__)


def test_llp::readinstruction_constructor_args():
    sig = inspect.signature(llp::ReadInstruction.__init__)
    params = list(sig.parameters.keys())



def test_llp::dataaccesspattern_is_not_abstract():
    assert not inspect.isabstract(llp::DataAccessPattern)


def test_llp::dataaccesspattern_constructor_exists():
    assert callable(llp::DataAccessPattern.__init__)


def test_llp::dataaccesspattern_constructor_args():
    sig = inspect.signature(llp::DataAccessPattern.__init__)
    params = list(sig.parameters.keys())



def test_llp::task_is_not_abstract():
    assert not inspect.isabstract(llp::Task)


def test_llp::task_constructor_exists():
    assert callable(llp::Task.__init__)


def test_llp::task_constructor_args():
    sig = inspect.signature(llp::Task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_llp::task_has_name():
    assert hasattr(llp::Task, "name")
    descriptor = None
    for klass in llp::Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_llp::lowlevelprogram_is_not_abstract():
    assert not inspect.isabstract(llp::LowLevelProgram)


def test_llp::lowlevelprogram_constructor_exists():
    assert callable(llp::LowLevelProgram.__init__)


def test_llp::lowlevelprogram_constructor_args():
    sig = inspect.signature(llp::LowLevelProgram.__init__)
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
llp::Block_strategy = st.builds(
    llp::Block,
)
ControlFlowInstruction_strategy = st.builds(
    ControlFlowInstruction,
)
llp::RepetitionInstruction_strategy = st.builds(
    llp::RepetitionInstruction,
    numberOfRepetitions=
        st.integers()
)
llp::SkipInstruction_strategy = st.builds(
    llp::SkipInstruction,
)
llp::ParenthesisInstruction_strategy = st.builds(
    llp::ParenthesisInstruction,
)
llp::ControlFlowBranchingInstruction_strategy = st.builds(
    llp::ControlFlowBranchingInstruction,
)
SynchronisationInstruction_strategy = st.builds(
    SynchronisationInstruction,
)
llp::UnlockInstruction_strategy = st.builds(
    llp::UnlockInstruction,
)
llp::LockInstruction_strategy = st.builds(
    llp::LockInstruction,
)
CacheInstruction_strategy = st.builds(
    CacheInstruction,
)
llp::CommitInstruction_strategy = st.builds(
    llp::CommitInstruction,
)
llp::MemoryReference_strategy = st.builds(
    llp::MemoryReference,
    address=
        safe_text
)
DataAccessPattern_strategy = st.builds(
    DataAccessPattern,
)
llp::CacheInstruction_strategy = st.builds(
    llp::CacheInstruction,
)
llp::SynchronisationInstruction_strategy = st.builds(
    llp::SynchronisationInstruction,
)
llp::SpawnInstruction_strategy = st.builds(
    llp::SpawnInstruction,
)
llp::ControlFlowInstruction_strategy = st.builds(
    llp::ControlFlowInstruction,
)
llp::IOInstruction_strategy = st.builds(
    llp::IOInstruction,
)
IOInstruction_strategy = st.builds(
    IOInstruction,
)
llp::WriteInstruction_strategy = st.builds(
    llp::WriteInstruction,
)
llp::ReadInstruction_strategy = st.builds(
    llp::ReadInstruction,
)
llp::DataAccessPattern_strategy = st.builds(
    llp::DataAccessPattern,
)
llp::Task_strategy = st.builds(
    llp::Task,
    name=
        safe_text
)
llp::LowLevelProgram_strategy = st.builds(
    llp::LowLevelProgram,
)

@given(instance=llp::Block_strategy)
@settings(max_examples=50)
def test_llp::block_instantiation(instance):
    assert isinstance(instance, llp::Block)

@given(instance=ControlFlowInstruction_strategy)
@settings(max_examples=50)
def test_controlflowinstruction_instantiation(instance):
    assert isinstance(instance, ControlFlowInstruction)

@given(instance=llp::RepetitionInstruction_strategy)
@settings(max_examples=50)
def test_llp::repetitioninstruction_instantiation(instance):
    assert isinstance(instance, llp::RepetitionInstruction)

@given(instance=llp::RepetitionInstruction_strategy)
def test_llp::repetitioninstruction_numberOfRepetitions_type(instance):
    assert isinstance(instance.numberOfRepetitions, int)


@given(instance=llp::RepetitionInstruction_strategy)
def test_llp::repetitioninstruction_numberOfRepetitions_setter(instance):
    original = instance.numberOfRepetitions
    instance.numberOfRepetitions = original
    assert instance.numberOfRepetitions == original

@given(instance=llp::SkipInstruction_strategy)
@settings(max_examples=50)
def test_llp::skipinstruction_instantiation(instance):
    assert isinstance(instance, llp::SkipInstruction)

@given(instance=llp::ParenthesisInstruction_strategy)
@settings(max_examples=50)
def test_llp::parenthesisinstruction_instantiation(instance):
    assert isinstance(instance, llp::ParenthesisInstruction)

@given(instance=llp::ControlFlowBranchingInstruction_strategy)
@settings(max_examples=50)
def test_llp::controlflowbranchinginstruction_instantiation(instance):
    assert isinstance(instance, llp::ControlFlowBranchingInstruction)

@given(instance=SynchronisationInstruction_strategy)
@settings(max_examples=50)
def test_synchronisationinstruction_instantiation(instance):
    assert isinstance(instance, SynchronisationInstruction)

@given(instance=llp::UnlockInstruction_strategy)
@settings(max_examples=50)
def test_llp::unlockinstruction_instantiation(instance):
    assert isinstance(instance, llp::UnlockInstruction)

@given(instance=llp::LockInstruction_strategy)
@settings(max_examples=50)
def test_llp::lockinstruction_instantiation(instance):
    assert isinstance(instance, llp::LockInstruction)

@given(instance=CacheInstruction_strategy)
@settings(max_examples=50)
def test_cacheinstruction_instantiation(instance):
    assert isinstance(instance, CacheInstruction)

@given(instance=llp::CommitInstruction_strategy)
@settings(max_examples=50)
def test_llp::commitinstruction_instantiation(instance):
    assert isinstance(instance, llp::CommitInstruction)

@given(instance=llp::MemoryReference_strategy)
@settings(max_examples=50)
def test_llp::memoryreference_instantiation(instance):
    assert isinstance(instance, llp::MemoryReference)

@given(instance=llp::MemoryReference_strategy)
def test_llp::memoryreference_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=llp::MemoryReference_strategy)
def test_llp::memoryreference_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=DataAccessPattern_strategy)
@settings(max_examples=50)
def test_dataaccesspattern_instantiation(instance):
    assert isinstance(instance, DataAccessPattern)

@given(instance=llp::CacheInstruction_strategy)
@settings(max_examples=50)
def test_llp::cacheinstruction_instantiation(instance):
    assert isinstance(instance, llp::CacheInstruction)

@given(instance=llp::SynchronisationInstruction_strategy)
@settings(max_examples=50)
def test_llp::synchronisationinstruction_instantiation(instance):
    assert isinstance(instance, llp::SynchronisationInstruction)

@given(instance=llp::SpawnInstruction_strategy)
@settings(max_examples=50)
def test_llp::spawninstruction_instantiation(instance):
    assert isinstance(instance, llp::SpawnInstruction)

@given(instance=llp::ControlFlowInstruction_strategy)
@settings(max_examples=50)
def test_llp::controlflowinstruction_instantiation(instance):
    assert isinstance(instance, llp::ControlFlowInstruction)

@given(instance=llp::IOInstruction_strategy)
@settings(max_examples=50)
def test_llp::ioinstruction_instantiation(instance):
    assert isinstance(instance, llp::IOInstruction)

@given(instance=IOInstruction_strategy)
@settings(max_examples=50)
def test_ioinstruction_instantiation(instance):
    assert isinstance(instance, IOInstruction)

@given(instance=llp::WriteInstruction_strategy)
@settings(max_examples=50)
def test_llp::writeinstruction_instantiation(instance):
    assert isinstance(instance, llp::WriteInstruction)

@given(instance=llp::ReadInstruction_strategy)
@settings(max_examples=50)
def test_llp::readinstruction_instantiation(instance):
    assert isinstance(instance, llp::ReadInstruction)

@given(instance=llp::DataAccessPattern_strategy)
@settings(max_examples=50)
def test_llp::dataaccesspattern_instantiation(instance):
    assert isinstance(instance, llp::DataAccessPattern)

@given(instance=llp::Task_strategy)
@settings(max_examples=50)
def test_llp::task_instantiation(instance):
    assert isinstance(instance, llp::Task)

@given(instance=llp::Task_strategy)
def test_llp::task_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=llp::Task_strategy)
def test_llp::task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=llp::LowLevelProgram_strategy)
@settings(max_examples=50)
def test_llp::lowlevelprogram_instantiation(instance):
    assert isinstance(instance, llp::LowLevelProgram)
