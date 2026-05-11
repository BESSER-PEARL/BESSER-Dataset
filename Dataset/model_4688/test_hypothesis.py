import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Arith,
    simpleALEnv::ArithLit,
    simpleALEnv::ArithOp,
    simpleALEnv::ALVarRef,
    simpleALEnv::Arith,
    simpleALEnv::RandRange,
    simpleALEnv::EqualityTest,
    Stmt,
    simpleALEnv::IfStmt,
    simpleALEnv::Assign,
    simpleALEnv::Print,
    ArithOp,
    simpleALEnv::ArithMinus,
    simpleALEnv::ArithPlus,
    simpleALEnv::Stmt,
    simpleALEnv::Block,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_arith_is_not_abstract():
    assert not inspect.isabstract(Arith)


def test_arith_constructor_exists():
    assert callable(Arith.__init__)


def test_arith_constructor_args():
    sig = inspect.signature(Arith.__init__)
    params = list(sig.parameters.keys())



def test_simplealenv::arithlit_is_not_abstract():
    assert not inspect.isabstract(simpleALEnv::ArithLit)


def test_simplealenv::arithlit_constructor_exists():
    assert callable(simpleALEnv::ArithLit.__init__)


def test_simplealenv::arithlit_constructor_args():
    sig = inspect.signature(simpleALEnv::ArithLit.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_simplealenv::arithlit_has_val():
    assert hasattr(simpleALEnv::ArithLit, "val")
    descriptor = None
    for klass in simpleALEnv::ArithLit.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_simplealenv::arithop_is_not_abstract():
    assert not inspect.isabstract(simpleALEnv::ArithOp)


def test_simplealenv::arithop_constructor_exists():
    assert callable(simpleALEnv::ArithOp.__init__)


def test_simplealenv::arithop_constructor_args():
    sig = inspect.signature(simpleALEnv::ArithOp.__init__)
    params = list(sig.parameters.keys())



def test_simplealenv::alvarref_is_not_abstract():
    assert not inspect.isabstract(simpleALEnv::ALVarRef)


def test_simplealenv::alvarref_constructor_exists():
    assert callable(simpleALEnv::ALVarRef.__init__)


def test_simplealenv::alvarref_constructor_args():
    sig = inspect.signature(simpleALEnv::ALVarRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplealenv::alvarref_has_name():
    assert hasattr(simpleALEnv::ALVarRef, "name")
    descriptor = None
    for klass in simpleALEnv::ALVarRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplealenv::arith_is_not_abstract():
    assert not inspect.isabstract(simpleALEnv::Arith)


def test_simplealenv::arith_constructor_exists():
    assert callable(simpleALEnv::Arith.__init__)


def test_simplealenv::arith_constructor_args():
    sig = inspect.signature(simpleALEnv::Arith.__init__)
    params = list(sig.parameters.keys())



def test_simplealenv::randrange_is_not_abstract():
    assert not inspect.isabstract(simpleALEnv::RandRange)


def test_simplealenv::randrange_constructor_exists():
    assert callable(simpleALEnv::RandRange.__init__)


def test_simplealenv::randrange_constructor_args():
    sig = inspect.signature(simpleALEnv::RandRange.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_simplealenv::randrange_has_max():
    assert hasattr(simpleALEnv::RandRange, "max")
    descriptor = None
    for klass in simpleALEnv::RandRange.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_simplealenv::randrange_has_min():
    assert hasattr(simpleALEnv::RandRange, "min")
    descriptor = None
    for klass in simpleALEnv::RandRange.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_simplealenv::equalitytest_is_not_abstract():
    assert not inspect.isabstract(simpleALEnv::EqualityTest)


def test_simplealenv::equalitytest_constructor_exists():
    assert callable(simpleALEnv::EqualityTest.__init__)


def test_simplealenv::equalitytest_constructor_args():
    sig = inspect.signature(simpleALEnv::EqualityTest.__init__)
    params = list(sig.parameters.keys())



def test_stmt_is_not_abstract():
    assert not inspect.isabstract(Stmt)


def test_stmt_constructor_exists():
    assert callable(Stmt.__init__)


def test_stmt_constructor_args():
    sig = inspect.signature(Stmt.__init__)
    params = list(sig.parameters.keys())



def test_simplealenv::ifstmt_is_not_abstract():
    assert not inspect.isabstract(simpleALEnv::IfStmt)


def test_simplealenv::ifstmt_constructor_exists():
    assert callable(simpleALEnv::IfStmt.__init__)


def test_simplealenv::ifstmt_constructor_args():
    sig = inspect.signature(simpleALEnv::IfStmt.__init__)
    params = list(sig.parameters.keys())



def test_simplealenv::assign_is_not_abstract():
    assert not inspect.isabstract(simpleALEnv::Assign)


def test_simplealenv::assign_constructor_exists():
    assert callable(simpleALEnv::Assign.__init__)


def test_simplealenv::assign_constructor_args():
    sig = inspect.signature(simpleALEnv::Assign.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplealenv::assign_has_name():
    assert hasattr(simpleALEnv::Assign, "name")
    descriptor = None
    for klass in simpleALEnv::Assign.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplealenv::print_is_not_abstract():
    assert not inspect.isabstract(simpleALEnv::Print)


def test_simplealenv::print_constructor_exists():
    assert callable(simpleALEnv::Print.__init__)


def test_simplealenv::print_constructor_args():
    sig = inspect.signature(simpleALEnv::Print.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplealenv::print_has_name():
    assert hasattr(simpleALEnv::Print, "name")
    descriptor = None
    for klass in simpleALEnv::Print.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arithop_is_not_abstract():
    assert not inspect.isabstract(ArithOp)


def test_arithop_constructor_exists():
    assert callable(ArithOp.__init__)


def test_arithop_constructor_args():
    sig = inspect.signature(ArithOp.__init__)
    params = list(sig.parameters.keys())



def test_simplealenv::arithminus_is_not_abstract():
    assert not inspect.isabstract(simpleALEnv::ArithMinus)


def test_simplealenv::arithminus_constructor_exists():
    assert callable(simpleALEnv::ArithMinus.__init__)


def test_simplealenv::arithminus_constructor_args():
    sig = inspect.signature(simpleALEnv::ArithMinus.__init__)
    params = list(sig.parameters.keys())



def test_simplealenv::arithplus_is_not_abstract():
    assert not inspect.isabstract(simpleALEnv::ArithPlus)


def test_simplealenv::arithplus_constructor_exists():
    assert callable(simpleALEnv::ArithPlus.__init__)


def test_simplealenv::arithplus_constructor_args():
    sig = inspect.signature(simpleALEnv::ArithPlus.__init__)
    params = list(sig.parameters.keys())



def test_simplealenv::stmt_is_not_abstract():
    assert not inspect.isabstract(simpleALEnv::Stmt)


def test_simplealenv::stmt_constructor_exists():
    assert callable(simpleALEnv::Stmt.__init__)


def test_simplealenv::stmt_constructor_args():
    sig = inspect.signature(simpleALEnv::Stmt.__init__)
    params = list(sig.parameters.keys())



def test_simplealenv::block_is_not_abstract():
    assert not inspect.isabstract(simpleALEnv::Block)


def test_simplealenv::block_constructor_exists():
    assert callable(simpleALEnv::Block.__init__)


def test_simplealenv::block_constructor_args():
    sig = inspect.signature(simpleALEnv::Block.__init__)
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
Arith_strategy = st.builds(
    Arith,
)
simpleALEnv::ArithLit_strategy = st.builds(
    simpleALEnv::ArithLit,
    val=
        st.integers()
)
simpleALEnv::ArithOp_strategy = st.builds(
    simpleALEnv::ArithOp,
)
simpleALEnv::ALVarRef_strategy = st.builds(
    simpleALEnv::ALVarRef,
    name=
        safe_text
)
simpleALEnv::Arith_strategy = st.builds(
    simpleALEnv::Arith,
)
simpleALEnv::RandRange_strategy = st.builds(
    simpleALEnv::RandRange,
    max=
        st.integers(),
    min=
        st.integers()
)
simpleALEnv::EqualityTest_strategy = st.builds(
    simpleALEnv::EqualityTest,
)
Stmt_strategy = st.builds(
    Stmt,
)
simpleALEnv::IfStmt_strategy = st.builds(
    simpleALEnv::IfStmt,
)
simpleALEnv::Assign_strategy = st.builds(
    simpleALEnv::Assign,
    name=
        safe_text
)
simpleALEnv::Print_strategy = st.builds(
    simpleALEnv::Print,
    name=
        safe_text
)
ArithOp_strategy = st.builds(
    ArithOp,
)
simpleALEnv::ArithMinus_strategy = st.builds(
    simpleALEnv::ArithMinus,
)
simpleALEnv::ArithPlus_strategy = st.builds(
    simpleALEnv::ArithPlus,
)
simpleALEnv::Stmt_strategy = st.builds(
    simpleALEnv::Stmt,
)
simpleALEnv::Block_strategy = st.builds(
    simpleALEnv::Block,
)

@given(instance=Arith_strategy)
@settings(max_examples=50)
def test_arith_instantiation(instance):
    assert isinstance(instance, Arith)

@given(instance=simpleALEnv::ArithLit_strategy)
@settings(max_examples=50)
def test_simplealenv::arithlit_instantiation(instance):
    assert isinstance(instance, simpleALEnv::ArithLit)

@given(instance=simpleALEnv::ArithLit_strategy)
def test_simplealenv::arithlit_val_type(instance):
    assert isinstance(instance.val, int)


@given(instance=simpleALEnv::ArithLit_strategy)
def test_simplealenv::arithlit_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=simpleALEnv::ArithOp_strategy)
@settings(max_examples=50)
def test_simplealenv::arithop_instantiation(instance):
    assert isinstance(instance, simpleALEnv::ArithOp)

@given(instance=simpleALEnv::ALVarRef_strategy)
@settings(max_examples=50)
def test_simplealenv::alvarref_instantiation(instance):
    assert isinstance(instance, simpleALEnv::ALVarRef)

@given(instance=simpleALEnv::ALVarRef_strategy)
def test_simplealenv::alvarref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleALEnv::ALVarRef_strategy)
def test_simplealenv::alvarref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleALEnv::Arith_strategy)
@settings(max_examples=50)
def test_simplealenv::arith_instantiation(instance):
    assert isinstance(instance, simpleALEnv::Arith)

@given(instance=simpleALEnv::RandRange_strategy)
@settings(max_examples=50)
def test_simplealenv::randrange_instantiation(instance):
    assert isinstance(instance, simpleALEnv::RandRange)

@given(instance=simpleALEnv::RandRange_strategy)
def test_simplealenv::randrange_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=simpleALEnv::RandRange_strategy)
def test_simplealenv::randrange_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=simpleALEnv::RandRange_strategy)
def test_simplealenv::randrange_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=simpleALEnv::RandRange_strategy)
def test_simplealenv::randrange_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=simpleALEnv::EqualityTest_strategy)
@settings(max_examples=50)
def test_simplealenv::equalitytest_instantiation(instance):
    assert isinstance(instance, simpleALEnv::EqualityTest)

@given(instance=Stmt_strategy)
@settings(max_examples=50)
def test_stmt_instantiation(instance):
    assert isinstance(instance, Stmt)

@given(instance=simpleALEnv::IfStmt_strategy)
@settings(max_examples=50)
def test_simplealenv::ifstmt_instantiation(instance):
    assert isinstance(instance, simpleALEnv::IfStmt)

@given(instance=simpleALEnv::Assign_strategy)
@settings(max_examples=50)
def test_simplealenv::assign_instantiation(instance):
    assert isinstance(instance, simpleALEnv::Assign)

@given(instance=simpleALEnv::Assign_strategy)
def test_simplealenv::assign_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleALEnv::Assign_strategy)
def test_simplealenv::assign_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleALEnv::Print_strategy)
@settings(max_examples=50)
def test_simplealenv::print_instantiation(instance):
    assert isinstance(instance, simpleALEnv::Print)

@given(instance=simpleALEnv::Print_strategy)
def test_simplealenv::print_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleALEnv::Print_strategy)
def test_simplealenv::print_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ArithOp_strategy)
@settings(max_examples=50)
def test_arithop_instantiation(instance):
    assert isinstance(instance, ArithOp)

@given(instance=simpleALEnv::ArithMinus_strategy)
@settings(max_examples=50)
def test_simplealenv::arithminus_instantiation(instance):
    assert isinstance(instance, simpleALEnv::ArithMinus)

@given(instance=simpleALEnv::ArithPlus_strategy)
@settings(max_examples=50)
def test_simplealenv::arithplus_instantiation(instance):
    assert isinstance(instance, simpleALEnv::ArithPlus)

@given(instance=simpleALEnv::Stmt_strategy)
@settings(max_examples=50)
def test_simplealenv::stmt_instantiation(instance):
    assert isinstance(instance, simpleALEnv::Stmt)

@given(instance=simpleALEnv::Block_strategy)
@settings(max_examples=50)
def test_simplealenv::block_instantiation(instance):
    assert isinstance(instance, simpleALEnv::Block)
