import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Stmt,
    simpleal_Assign,
    simpleal_Print,
    ArithOp,
    simpleal_ArithMinus,
    simpleal_ArithPlus,
    Arith,
    simpleal_ArithOp,
    simpleal_ArithLit,
    simpleal_VarRef,
    simpleal_Arith,
    simpleal_Stmt,
    simpleal_Block,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stmt_is_not_abstract():
    assert not inspect.isabstract(Stmt)


def test_stmt_constructor_exists():
    assert callable(Stmt.__init__)


def test_stmt_constructor_args():
    sig = inspect.signature(Stmt.__init__)
    params = list(sig.parameters.keys())



def test_simpleal_assign_is_not_abstract():
    assert not inspect.isabstract(simpleal_Assign)


def test_simpleal_assign_constructor_exists():
    assert callable(simpleal_Assign.__init__)


def test_simpleal_assign_constructor_args():
    sig = inspect.signature(simpleal_Assign.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleal_assign_has_name():
    assert hasattr(simpleal_Assign, "name")
    descriptor = None
    for klass in simpleal_Assign.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleal_print_is_not_abstract():
    assert not inspect.isabstract(simpleal_Print)


def test_simpleal_print_constructor_exists():
    assert callable(simpleal_Print.__init__)


def test_simpleal_print_constructor_args():
    sig = inspect.signature(simpleal_Print.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleal_print_has_name():
    assert hasattr(simpleal_Print, "name")
    descriptor = None
    for klass in simpleal_Print.__mro__:
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



def test_simpleal_arithminus_is_not_abstract():
    assert not inspect.isabstract(simpleal_ArithMinus)


def test_simpleal_arithminus_constructor_exists():
    assert callable(simpleal_ArithMinus.__init__)


def test_simpleal_arithminus_constructor_args():
    sig = inspect.signature(simpleal_ArithMinus.__init__)
    params = list(sig.parameters.keys())



def test_simpleal_arithplus_is_not_abstract():
    assert not inspect.isabstract(simpleal_ArithPlus)


def test_simpleal_arithplus_constructor_exists():
    assert callable(simpleal_ArithPlus.__init__)


def test_simpleal_arithplus_constructor_args():
    sig = inspect.signature(simpleal_ArithPlus.__init__)
    params = list(sig.parameters.keys())



def test_arith_is_not_abstract():
    assert not inspect.isabstract(Arith)


def test_arith_constructor_exists():
    assert callable(Arith.__init__)


def test_arith_constructor_args():
    sig = inspect.signature(Arith.__init__)
    params = list(sig.parameters.keys())



def test_simpleal_arithop_is_not_abstract():
    assert not inspect.isabstract(simpleal_ArithOp)


def test_simpleal_arithop_constructor_exists():
    assert callable(simpleal_ArithOp.__init__)


def test_simpleal_arithop_constructor_args():
    sig = inspect.signature(simpleal_ArithOp.__init__)
    params = list(sig.parameters.keys())



def test_simpleal_arithlit_is_not_abstract():
    assert not inspect.isabstract(simpleal_ArithLit)


def test_simpleal_arithlit_constructor_exists():
    assert callable(simpleal_ArithLit.__init__)


def test_simpleal_arithlit_constructor_args():
    sig = inspect.signature(simpleal_ArithLit.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_simpleal_arithlit_has_val():
    assert hasattr(simpleal_ArithLit, "val")
    descriptor = None
    for klass in simpleal_ArithLit.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_simpleal_varref_is_not_abstract():
    assert not inspect.isabstract(simpleal_VarRef)


def test_simpleal_varref_constructor_exists():
    assert callable(simpleal_VarRef.__init__)


def test_simpleal_varref_constructor_args():
    sig = inspect.signature(simpleal_VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleal_varref_has_name():
    assert hasattr(simpleal_VarRef, "name")
    descriptor = None
    for klass in simpleal_VarRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleal_arith_is_not_abstract():
    assert not inspect.isabstract(simpleal_Arith)


def test_simpleal_arith_constructor_exists():
    assert callable(simpleal_Arith.__init__)


def test_simpleal_arith_constructor_args():
    sig = inspect.signature(simpleal_Arith.__init__)
    params = list(sig.parameters.keys())



def test_simpleal_stmt_is_not_abstract():
    assert not inspect.isabstract(simpleal_Stmt)


def test_simpleal_stmt_constructor_exists():
    assert callable(simpleal_Stmt.__init__)


def test_simpleal_stmt_constructor_args():
    sig = inspect.signature(simpleal_Stmt.__init__)
    params = list(sig.parameters.keys())



def test_simpleal_block_is_not_abstract():
    assert not inspect.isabstract(simpleal_Block)


def test_simpleal_block_constructor_exists():
    assert callable(simpleal_Block.__init__)


def test_simpleal_block_constructor_args():
    sig = inspect.signature(simpleal_Block.__init__)
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
Stmt_strategy = st.builds(
    Stmt,
)
simpleal_Assign_strategy = st.builds(
    simpleal_Assign,
    name=
        safe_text
)
simpleal_Print_strategy = st.builds(
    simpleal_Print,
    name=
        safe_text
)
ArithOp_strategy = st.builds(
    ArithOp,
)
simpleal_ArithMinus_strategy = st.builds(
    simpleal_ArithMinus,
)
simpleal_ArithPlus_strategy = st.builds(
    simpleal_ArithPlus,
)
Arith_strategy = st.builds(
    Arith,
)
simpleal_ArithOp_strategy = st.builds(
    simpleal_ArithOp,
)
simpleal_ArithLit_strategy = st.builds(
    simpleal_ArithLit,
    val=
        st.integers()
)
simpleal_VarRef_strategy = st.builds(
    simpleal_VarRef,
    name=
        safe_text
)
simpleal_Arith_strategy = st.builds(
    simpleal_Arith,
)
simpleal_Stmt_strategy = st.builds(
    simpleal_Stmt,
)
simpleal_Block_strategy = st.builds(
    simpleal_Block,
)

@given(instance=Stmt_strategy)
@settings(max_examples=50)
def test_stmt_instantiation(instance):
    assert isinstance(instance, Stmt)

@given(instance=simpleal_Assign_strategy)
@settings(max_examples=50)
def test_simpleal_assign_instantiation(instance):
    assert isinstance(instance, simpleal_Assign)



@given(instance=simpleal_Assign_strategy)
def test_simpleal_assign_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleal_Print_strategy)
@settings(max_examples=50)
def test_simpleal_print_instantiation(instance):
    assert isinstance(instance, simpleal_Print)



@given(instance=simpleal_Print_strategy)
def test_simpleal_print_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ArithOp_strategy)
@settings(max_examples=50)
def test_arithop_instantiation(instance):
    assert isinstance(instance, ArithOp)

@given(instance=simpleal_ArithMinus_strategy)
@settings(max_examples=50)
def test_simpleal_arithminus_instantiation(instance):
    assert isinstance(instance, simpleal_ArithMinus)

@given(instance=simpleal_ArithPlus_strategy)
@settings(max_examples=50)
def test_simpleal_arithplus_instantiation(instance):
    assert isinstance(instance, simpleal_ArithPlus)

@given(instance=Arith_strategy)
@settings(max_examples=50)
def test_arith_instantiation(instance):
    assert isinstance(instance, Arith)

@given(instance=simpleal_ArithOp_strategy)
@settings(max_examples=50)
def test_simpleal_arithop_instantiation(instance):
    assert isinstance(instance, simpleal_ArithOp)

@given(instance=simpleal_ArithLit_strategy)
@settings(max_examples=50)
def test_simpleal_arithlit_instantiation(instance):
    assert isinstance(instance, simpleal_ArithLit)



@given(instance=simpleal_ArithLit_strategy)
def test_simpleal_arithlit_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=simpleal_VarRef_strategy)
@settings(max_examples=50)
def test_simpleal_varref_instantiation(instance):
    assert isinstance(instance, simpleal_VarRef)



@given(instance=simpleal_VarRef_strategy)
def test_simpleal_varref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleal_Arith_strategy)
@settings(max_examples=50)
def test_simpleal_arith_instantiation(instance):
    assert isinstance(instance, simpleal_Arith)

@given(instance=simpleal_Stmt_strategy)
@settings(max_examples=50)
def test_simpleal_stmt_instantiation(instance):
    assert isinstance(instance, simpleal_Stmt)

@given(instance=simpleal_Block_strategy)
@settings(max_examples=50)
def test_simpleal_block_instantiation(instance):
    assert isinstance(instance, simpleal_Block)
