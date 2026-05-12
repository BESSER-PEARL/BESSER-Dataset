import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    whileComp_Tl,
    whileComp_Hd,
    whileComp_List,
    whileComp_Nil2,
    whileComp_Cons,
    whileComp_Not,
    whileComp_Lexpr,
    whileComp_ExprSimple,
    whileComp_While,
    whileComp_For,
    whileComp_If,
    whileComp_Program,
    whileComp_Foreach,
    whileComp_EObject,
    whileComp_Command,
    whileComp_Nop,
    whileComp_Expr,
    whileComp_Affectation,
    whileComp_Write,
    whileComp_Commands,
    whileComp_Read,
    whileComp_Definition,
    whileComp_Function,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_whilecomp_tl_is_not_abstract():
    assert not inspect.isabstract(whileComp_Tl)


def test_whilecomp_tl_constructor_exists():
    assert callable(whileComp_Tl.__init__)


def test_whilecomp_tl_constructor_args():
    sig = inspect.signature(whileComp_Tl.__init__)
    params = list(sig.parameters.keys())
    assert "tl" in params, "Missing parameter 'tl'"

def test_whilecomp_tl_has_tl():
    assert hasattr(whileComp_Tl, "tl")
    descriptor = None
    for klass in whileComp_Tl.__mro__:
        if "tl" in klass.__dict__:
            descriptor = klass.__dict__["tl"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp_hd_is_not_abstract():
    assert not inspect.isabstract(whileComp_Hd)


def test_whilecomp_hd_constructor_exists():
    assert callable(whileComp_Hd.__init__)


def test_whilecomp_hd_constructor_args():
    sig = inspect.signature(whileComp_Hd.__init__)
    params = list(sig.parameters.keys())
    assert "hd" in params, "Missing parameter 'hd'"

def test_whilecomp_hd_has_hd():
    assert hasattr(whileComp_Hd, "hd")
    descriptor = None
    for klass in whileComp_Hd.__mro__:
        if "hd" in klass.__dict__:
            descriptor = klass.__dict__["hd"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp_list_is_not_abstract():
    assert not inspect.isabstract(whileComp_List)


def test_whilecomp_list_constructor_exists():
    assert callable(whileComp_List.__init__)


def test_whilecomp_list_constructor_args():
    sig = inspect.signature(whileComp_List.__init__)
    params = list(sig.parameters.keys())
    assert "list" in params, "Missing parameter 'list'"

def test_whilecomp_list_has_list():
    assert hasattr(whileComp_List, "list")
    descriptor = None
    for klass in whileComp_List.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp_nil2_is_not_abstract():
    assert not inspect.isabstract(whileComp_Nil2)


def test_whilecomp_nil2_constructor_exists():
    assert callable(whileComp_Nil2.__init__)


def test_whilecomp_nil2_constructor_args():
    sig = inspect.signature(whileComp_Nil2.__init__)
    params = list(sig.parameters.keys())
    assert "nil" in params, "Missing parameter 'nil'"

def test_whilecomp_nil2_has_nil():
    assert hasattr(whileComp_Nil2, "nil")
    descriptor = None
    for klass in whileComp_Nil2.__mro__:
        if "nil" in klass.__dict__:
            descriptor = klass.__dict__["nil"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp_cons_is_not_abstract():
    assert not inspect.isabstract(whileComp_Cons)


def test_whilecomp_cons_constructor_exists():
    assert callable(whileComp_Cons.__init__)


def test_whilecomp_cons_constructor_args():
    sig = inspect.signature(whileComp_Cons.__init__)
    params = list(sig.parameters.keys())
    assert "cons" in params, "Missing parameter 'cons'"

def test_whilecomp_cons_has_cons():
    assert hasattr(whileComp_Cons, "cons")
    descriptor = None
    for klass in whileComp_Cons.__mro__:
        if "cons" in klass.__dict__:
            descriptor = klass.__dict__["cons"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp_not_is_not_abstract():
    assert not inspect.isabstract(whileComp_Not)


def test_whilecomp_not_constructor_exists():
    assert callable(whileComp_Not.__init__)


def test_whilecomp_not_constructor_args():
    sig = inspect.signature(whileComp_Not.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_whilecomp_not_has_not_():
    assert hasattr(whileComp_Not, "not_")
    descriptor = None
    for klass in whileComp_Not.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp_lexpr_is_not_abstract():
    assert not inspect.isabstract(whileComp_Lexpr)


def test_whilecomp_lexpr_constructor_exists():
    assert callable(whileComp_Lexpr.__init__)


def test_whilecomp_lexpr_constructor_args():
    sig = inspect.signature(whileComp_Lexpr.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp_exprsimple_is_not_abstract():
    assert not inspect.isabstract(whileComp_ExprSimple)


def test_whilecomp_exprsimple_constructor_exists():
    assert callable(whileComp_ExprSimple.__init__)


def test_whilecomp_exprsimple_constructor_args():
    sig = inspect.signature(whileComp_ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "ope" in params, "Missing parameter 'ope'"
    assert "call" in params, "Missing parameter 'call'"
    assert "valeur" in params, "Missing parameter 'valeur'"

def test_whilecomp_exprsimple_has_ope():
    assert hasattr(whileComp_ExprSimple, "ope")
    descriptor = None
    for klass in whileComp_ExprSimple.__mro__:
        if "ope" in klass.__dict__:
            descriptor = klass.__dict__["ope"]
            break
    assert isinstance(descriptor, property)

def test_whilecomp_exprsimple_has_call():
    assert hasattr(whileComp_ExprSimple, "call")
    descriptor = None
    for klass in whileComp_ExprSimple.__mro__:
        if "call" in klass.__dict__:
            descriptor = klass.__dict__["call"]
            break
    assert isinstance(descriptor, property)

def test_whilecomp_exprsimple_has_valeur():
    assert hasattr(whileComp_ExprSimple, "valeur")
    descriptor = None
    for klass in whileComp_ExprSimple.__mro__:
        if "valeur" in klass.__dict__:
            descriptor = klass.__dict__["valeur"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp_while_is_not_abstract():
    assert not inspect.isabstract(whileComp_While)


def test_whilecomp_while_constructor_exists():
    assert callable(whileComp_While.__init__)


def test_whilecomp_while_constructor_args():
    sig = inspect.signature(whileComp_While.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp_for_is_not_abstract():
    assert not inspect.isabstract(whileComp_For)


def test_whilecomp_for_constructor_exists():
    assert callable(whileComp_For.__init__)


def test_whilecomp_for_constructor_args():
    sig = inspect.signature(whileComp_For.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp_if_is_not_abstract():
    assert not inspect.isabstract(whileComp_If)


def test_whilecomp_if_constructor_exists():
    assert callable(whileComp_If.__init__)


def test_whilecomp_if_constructor_args():
    sig = inspect.signature(whileComp_If.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp_program_is_not_abstract():
    assert not inspect.isabstract(whileComp_Program)


def test_whilecomp_program_constructor_exists():
    assert callable(whileComp_Program.__init__)


def test_whilecomp_program_constructor_args():
    sig = inspect.signature(whileComp_Program.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp_foreach_is_not_abstract():
    assert not inspect.isabstract(whileComp_Foreach)


def test_whilecomp_foreach_constructor_exists():
    assert callable(whileComp_Foreach.__init__)


def test_whilecomp_foreach_constructor_args():
    sig = inspect.signature(whileComp_Foreach.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp_eobject_is_not_abstract():
    assert not inspect.isabstract(whileComp_EObject)


def test_whilecomp_eobject_constructor_exists():
    assert callable(whileComp_EObject.__init__)


def test_whilecomp_eobject_constructor_args():
    sig = inspect.signature(whileComp_EObject.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp_command_is_not_abstract():
    assert not inspect.isabstract(whileComp_Command)


def test_whilecomp_command_constructor_exists():
    assert callable(whileComp_Command.__init__)


def test_whilecomp_command_constructor_args():
    sig = inspect.signature(whileComp_Command.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp_nop_is_not_abstract():
    assert not inspect.isabstract(whileComp_Nop)


def test_whilecomp_nop_constructor_exists():
    assert callable(whileComp_Nop.__init__)


def test_whilecomp_nop_constructor_args():
    sig = inspect.signature(whileComp_Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_whilecomp_nop_has_nop():
    assert hasattr(whileComp_Nop, "nop")
    descriptor = None
    for klass in whileComp_Nop.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp_expr_is_not_abstract():
    assert not inspect.isabstract(whileComp_Expr)


def test_whilecomp_expr_constructor_exists():
    assert callable(whileComp_Expr.__init__)


def test_whilecomp_expr_constructor_args():
    sig = inspect.signature(whileComp_Expr.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp_affectation_is_not_abstract():
    assert not inspect.isabstract(whileComp_Affectation)


def test_whilecomp_affectation_constructor_exists():
    assert callable(whileComp_Affectation.__init__)


def test_whilecomp_affectation_constructor_args():
    sig = inspect.signature(whileComp_Affectation.__init__)
    params = list(sig.parameters.keys())
    assert "affectations" in params, "Missing parameter 'affectations'"

def test_whilecomp_affectation_has_affectations():
    assert hasattr(whileComp_Affectation, "affectations")
    descriptor = None
    for klass in whileComp_Affectation.__mro__:
        if "affectations" in klass.__dict__:
            descriptor = klass.__dict__["affectations"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp_write_is_not_abstract():
    assert not inspect.isabstract(whileComp_Write)


def test_whilecomp_write_constructor_exists():
    assert callable(whileComp_Write.__init__)


def test_whilecomp_write_constructor_args():
    sig = inspect.signature(whileComp_Write.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_whilecomp_write_has_variable():
    assert hasattr(whileComp_Write, "variable")
    descriptor = None
    for klass in whileComp_Write.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp_commands_is_not_abstract():
    assert not inspect.isabstract(whileComp_Commands)


def test_whilecomp_commands_constructor_exists():
    assert callable(whileComp_Commands.__init__)


def test_whilecomp_commands_constructor_args():
    sig = inspect.signature(whileComp_Commands.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp_read_is_not_abstract():
    assert not inspect.isabstract(whileComp_Read)


def test_whilecomp_read_constructor_exists():
    assert callable(whileComp_Read.__init__)


def test_whilecomp_read_constructor_args():
    sig = inspect.signature(whileComp_Read.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_whilecomp_read_has_variable():
    assert hasattr(whileComp_Read, "variable")
    descriptor = None
    for klass in whileComp_Read.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_whilecomp_definition_is_not_abstract():
    assert not inspect.isabstract(whileComp_Definition)


def test_whilecomp_definition_constructor_exists():
    assert callable(whileComp_Definition.__init__)


def test_whilecomp_definition_constructor_args():
    sig = inspect.signature(whileComp_Definition.__init__)
    params = list(sig.parameters.keys())



def test_whilecomp_function_is_not_abstract():
    assert not inspect.isabstract(whileComp_Function)


def test_whilecomp_function_constructor_exists():
    assert callable(whileComp_Function.__init__)


def test_whilecomp_function_constructor_args():
    sig = inspect.signature(whileComp_Function.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_whilecomp_function_has_function():
    assert hasattr(whileComp_Function, "function")
    descriptor = None
    for klass in whileComp_Function.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)


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
whileComp_Tl_strategy = st.builds(
    whileComp_Tl,
    tl=
        safe_text
)
whileComp_Hd_strategy = st.builds(
    whileComp_Hd,
    hd=
        safe_text
)
whileComp_List_strategy = st.builds(
    whileComp_List,
    list=
        safe_text
)
whileComp_Nil2_strategy = st.builds(
    whileComp_Nil2,
    nil=
        safe_text
)
whileComp_Cons_strategy = st.builds(
    whileComp_Cons,
    cons=
        safe_text
)
whileComp_Not_strategy = st.builds(
    whileComp_Not,
    not_=
        safe_text
)
whileComp_Lexpr_strategy = st.builds(
    whileComp_Lexpr,
)
whileComp_ExprSimple_strategy = st.builds(
    whileComp_ExprSimple,
    ope=
        safe_text,
    call=
        safe_text,
    valeur=
        safe_text
)
whileComp_While_strategy = st.builds(
    whileComp_While,
)
whileComp_For_strategy = st.builds(
    whileComp_For,
)
whileComp_If_strategy = st.builds(
    whileComp_If,
)
whileComp_Program_strategy = st.builds(
    whileComp_Program,
)
whileComp_Foreach_strategy = st.builds(
    whileComp_Foreach,
)
whileComp_EObject_strategy = st.builds(
    whileComp_EObject,
)
whileComp_Command_strategy = st.builds(
    whileComp_Command,
)
whileComp_Nop_strategy = st.builds(
    whileComp_Nop,
    nop=
        safe_text
)
whileComp_Expr_strategy = st.builds(
    whileComp_Expr,
)
whileComp_Affectation_strategy = st.builds(
    whileComp_Affectation,
    affectations=
        safe_text
)
whileComp_Write_strategy = st.builds(
    whileComp_Write,
    variable=
        safe_text
)
whileComp_Commands_strategy = st.builds(
    whileComp_Commands,
)
whileComp_Read_strategy = st.builds(
    whileComp_Read,
    variable=
        safe_text
)
whileComp_Definition_strategy = st.builds(
    whileComp_Definition,
)
whileComp_Function_strategy = st.builds(
    whileComp_Function,
    function=
        safe_text
)

@given(instance=whileComp_Tl_strategy)
@settings(max_examples=50)
def test_whilecomp_tl_instantiation(instance):
    assert isinstance(instance, whileComp_Tl)



@given(instance=whileComp_Tl_strategy)
def test_whilecomp_tl_tl_setter(instance):
    original = instance.tl
    instance.tl = original
    assert instance.tl == original

@given(instance=whileComp_Hd_strategy)
@settings(max_examples=50)
def test_whilecomp_hd_instantiation(instance):
    assert isinstance(instance, whileComp_Hd)



@given(instance=whileComp_Hd_strategy)
def test_whilecomp_hd_hd_setter(instance):
    original = instance.hd
    instance.hd = original
    assert instance.hd == original

@given(instance=whileComp_List_strategy)
@settings(max_examples=50)
def test_whilecomp_list_instantiation(instance):
    assert isinstance(instance, whileComp_List)



@given(instance=whileComp_List_strategy)
def test_whilecomp_list_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=whileComp_Nil2_strategy)
@settings(max_examples=50)
def test_whilecomp_nil2_instantiation(instance):
    assert isinstance(instance, whileComp_Nil2)



@given(instance=whileComp_Nil2_strategy)
def test_whilecomp_nil2_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original

@given(instance=whileComp_Cons_strategy)
@settings(max_examples=50)
def test_whilecomp_cons_instantiation(instance):
    assert isinstance(instance, whileComp_Cons)



@given(instance=whileComp_Cons_strategy)
def test_whilecomp_cons_cons_setter(instance):
    original = instance.cons
    instance.cons = original
    assert instance.cons == original

@given(instance=whileComp_Not_strategy)
@settings(max_examples=50)
def test_whilecomp_not_instantiation(instance):
    assert isinstance(instance, whileComp_Not)



@given(instance=whileComp_Not_strategy)
def test_whilecomp_not_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=whileComp_Lexpr_strategy)
@settings(max_examples=50)
def test_whilecomp_lexpr_instantiation(instance):
    assert isinstance(instance, whileComp_Lexpr)

@given(instance=whileComp_ExprSimple_strategy)
@settings(max_examples=50)
def test_whilecomp_exprsimple_instantiation(instance):
    assert isinstance(instance, whileComp_ExprSimple)



@given(instance=whileComp_ExprSimple_strategy)
def test_whilecomp_exprsimple_ope_setter(instance):
    original = instance.ope
    instance.ope = original
    assert instance.ope == original



@given(instance=whileComp_ExprSimple_strategy)
def test_whilecomp_exprsimple_call_setter(instance):
    original = instance.call
    instance.call = original
    assert instance.call == original



@given(instance=whileComp_ExprSimple_strategy)
def test_whilecomp_exprsimple_valeur_setter(instance):
    original = instance.valeur
    instance.valeur = original
    assert instance.valeur == original

@given(instance=whileComp_While_strategy)
@settings(max_examples=50)
def test_whilecomp_while_instantiation(instance):
    assert isinstance(instance, whileComp_While)

@given(instance=whileComp_For_strategy)
@settings(max_examples=50)
def test_whilecomp_for_instantiation(instance):
    assert isinstance(instance, whileComp_For)

@given(instance=whileComp_If_strategy)
@settings(max_examples=50)
def test_whilecomp_if_instantiation(instance):
    assert isinstance(instance, whileComp_If)

@given(instance=whileComp_Program_strategy)
@settings(max_examples=50)
def test_whilecomp_program_instantiation(instance):
    assert isinstance(instance, whileComp_Program)

@given(instance=whileComp_Foreach_strategy)
@settings(max_examples=50)
def test_whilecomp_foreach_instantiation(instance):
    assert isinstance(instance, whileComp_Foreach)

@given(instance=whileComp_EObject_strategy)
@settings(max_examples=50)
def test_whilecomp_eobject_instantiation(instance):
    assert isinstance(instance, whileComp_EObject)

@given(instance=whileComp_Command_strategy)
@settings(max_examples=50)
def test_whilecomp_command_instantiation(instance):
    assert isinstance(instance, whileComp_Command)

@given(instance=whileComp_Nop_strategy)
@settings(max_examples=50)
def test_whilecomp_nop_instantiation(instance):
    assert isinstance(instance, whileComp_Nop)



@given(instance=whileComp_Nop_strategy)
def test_whilecomp_nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=whileComp_Expr_strategy)
@settings(max_examples=50)
def test_whilecomp_expr_instantiation(instance):
    assert isinstance(instance, whileComp_Expr)

@given(instance=whileComp_Affectation_strategy)
@settings(max_examples=50)
def test_whilecomp_affectation_instantiation(instance):
    assert isinstance(instance, whileComp_Affectation)



@given(instance=whileComp_Affectation_strategy)
def test_whilecomp_affectation_affectations_setter(instance):
    original = instance.affectations
    instance.affectations = original
    assert instance.affectations == original

@given(instance=whileComp_Write_strategy)
@settings(max_examples=50)
def test_whilecomp_write_instantiation(instance):
    assert isinstance(instance, whileComp_Write)



@given(instance=whileComp_Write_strategy)
def test_whilecomp_write_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=whileComp_Commands_strategy)
@settings(max_examples=50)
def test_whilecomp_commands_instantiation(instance):
    assert isinstance(instance, whileComp_Commands)

@given(instance=whileComp_Read_strategy)
@settings(max_examples=50)
def test_whilecomp_read_instantiation(instance):
    assert isinstance(instance, whileComp_Read)



@given(instance=whileComp_Read_strategy)
def test_whilecomp_read_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=whileComp_Definition_strategy)
@settings(max_examples=50)
def test_whilecomp_definition_instantiation(instance):
    assert isinstance(instance, whileComp_Definition)

@given(instance=whileComp_Function_strategy)
@settings(max_examples=50)
def test_whilecomp_function_instantiation(instance):
    assert isinstance(instance, whileComp_Function)



@given(instance=whileComp_Function_strategy)
def test_whilecomp_function_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original
