import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::ExprEq,
    myDsl::ExprNotDo,
    myDsl::LExpr,
    myDsl::SymboleEx,
    myDsl::Tl,
    myDsl::Hd,
    myDsl::Liste,
    myDsl::Cons,
    myDsl::ExprSimple,
    myDsl::ExprAnd,
    myDsl::ExprNotNot,
    myDsl::ExprNot,
    myDsl::ExprOr,
    myDsl::Exprs,
    myDsl::Vars,
    myDsl::Foreach,
    myDsl::If,
    myDsl::For,
    myDsl::While,
    myDsl::AffectVar,
    myDsl::Commande,
    myDsl::Expr,
    myDsl::Output,
    myDsl::Commandes,
    myDsl::Input,
    myDsl::Fonction,
    myDsl::Programme,
    myDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::expreq_is_not_abstract():
    assert not inspect.isabstract(myDsl::ExprEq)


def test_mydsl::expreq_constructor_exists():
    assert callable(myDsl::ExprEq.__init__)


def test_mydsl::expreq_constructor_args():
    sig = inspect.signature(myDsl::ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::exprnotdo_is_not_abstract():
    assert not inspect.isabstract(myDsl::ExprNotDo)


def test_mydsl::exprnotdo_constructor_exists():
    assert callable(myDsl::ExprNotDo.__init__)


def test_mydsl::exprnotdo_constructor_args():
    sig = inspect.signature(myDsl::ExprNotDo.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::lexpr_is_not_abstract():
    assert not inspect.isabstract(myDsl::LExpr)


def test_mydsl::lexpr_constructor_exists():
    assert callable(myDsl::LExpr.__init__)


def test_mydsl::lexpr_constructor_args():
    sig = inspect.signature(myDsl::LExpr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::symboleex_is_not_abstract():
    assert not inspect.isabstract(myDsl::SymboleEx)


def test_mydsl::symboleex_constructor_exists():
    assert callable(myDsl::SymboleEx.__init__)


def test_mydsl::symboleex_constructor_args():
    sig = inspect.signature(myDsl::SymboleEx.__init__)
    params = list(sig.parameters.keys())
    assert "p" in params, "Missing parameter 'p'"

def test_mydsl::symboleex_has_p():
    assert hasattr(myDsl::SymboleEx, "p")
    descriptor = None
    for klass in myDsl::SymboleEx.__mro__:
        if "p" in klass.__dict__:
            descriptor = klass.__dict__["p"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::tl_is_not_abstract():
    assert not inspect.isabstract(myDsl::Tl)


def test_mydsl::tl_constructor_exists():
    assert callable(myDsl::Tl.__init__)


def test_mydsl::tl_constructor_args():
    sig = inspect.signature(myDsl::Tl.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::hd_is_not_abstract():
    assert not inspect.isabstract(myDsl::Hd)


def test_mydsl::hd_constructor_exists():
    assert callable(myDsl::Hd.__init__)


def test_mydsl::hd_constructor_args():
    sig = inspect.signature(myDsl::Hd.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::liste_is_not_abstract():
    assert not inspect.isabstract(myDsl::Liste)


def test_mydsl::liste_constructor_exists():
    assert callable(myDsl::Liste.__init__)


def test_mydsl::liste_constructor_args():
    sig = inspect.signature(myDsl::Liste.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::cons_is_not_abstract():
    assert not inspect.isabstract(myDsl::Cons)


def test_mydsl::cons_constructor_exists():
    assert callable(myDsl::Cons.__init__)


def test_mydsl::cons_constructor_args():
    sig = inspect.signature(myDsl::Cons.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::exprsimple_is_not_abstract():
    assert not inspect.isabstract(myDsl::ExprSimple)


def test_mydsl::exprsimple_constructor_exists():
    assert callable(myDsl::ExprSimple.__init__)


def test_mydsl::exprsimple_constructor_args():
    sig = inspect.signature(myDsl::ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"
    assert "vide" in params, "Missing parameter 'vide'"
    assert "symbole" in params, "Missing parameter 'symbole'"

def test_mydsl::exprsimple_has_variable():
    assert hasattr(myDsl::ExprSimple, "variable")
    descriptor = None
    for klass in myDsl::ExprSimple.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::exprsimple_has_vide():
    assert hasattr(myDsl::ExprSimple, "vide")
    descriptor = None
    for klass in myDsl::ExprSimple.__mro__:
        if "vide" in klass.__dict__:
            descriptor = klass.__dict__["vide"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::exprsimple_has_symbole():
    assert hasattr(myDsl::ExprSimple, "symbole")
    descriptor = None
    for klass in myDsl::ExprSimple.__mro__:
        if "symbole" in klass.__dict__:
            descriptor = klass.__dict__["symbole"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::exprand_is_not_abstract():
    assert not inspect.isabstract(myDsl::ExprAnd)


def test_mydsl::exprand_constructor_exists():
    assert callable(myDsl::ExprAnd.__init__)


def test_mydsl::exprand_constructor_args():
    sig = inspect.signature(myDsl::ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::exprnotnot_is_not_abstract():
    assert not inspect.isabstract(myDsl::ExprNotNot)


def test_mydsl::exprnotnot_constructor_exists():
    assert callable(myDsl::ExprNotNot.__init__)


def test_mydsl::exprnotnot_constructor_args():
    sig = inspect.signature(myDsl::ExprNotNot.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::exprnot_is_not_abstract():
    assert not inspect.isabstract(myDsl::ExprNot)


def test_mydsl::exprnot_constructor_exists():
    assert callable(myDsl::ExprNot.__init__)


def test_mydsl::exprnot_constructor_args():
    sig = inspect.signature(myDsl::ExprNot.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::expror_is_not_abstract():
    assert not inspect.isabstract(myDsl::ExprOr)


def test_mydsl::expror_constructor_exists():
    assert callable(myDsl::ExprOr.__init__)


def test_mydsl::expror_constructor_args():
    sig = inspect.signature(myDsl::ExprOr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::exprs_is_not_abstract():
    assert not inspect.isabstract(myDsl::Exprs)


def test_mydsl::exprs_constructor_exists():
    assert callable(myDsl::Exprs.__init__)


def test_mydsl::exprs_constructor_args():
    sig = inspect.signature(myDsl::Exprs.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::vars_is_not_abstract():
    assert not inspect.isabstract(myDsl::Vars)


def test_mydsl::vars_constructor_exists():
    assert callable(myDsl::Vars.__init__)


def test_mydsl::vars_constructor_args():
    sig = inspect.signature(myDsl::Vars.__init__)
    params = list(sig.parameters.keys())
    assert "var3" in params, "Missing parameter 'var3'"
    assert "var2" in params, "Missing parameter 'var2'"

def test_mydsl::vars_has_var3():
    assert hasattr(myDsl::Vars, "var3")
    descriptor = None
    for klass in myDsl::Vars.__mro__:
        if "var3" in klass.__dict__:
            descriptor = klass.__dict__["var3"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::vars_has_var2():
    assert hasattr(myDsl::Vars, "var2")
    descriptor = None
    for klass in myDsl::Vars.__mro__:
        if "var2" in klass.__dict__:
            descriptor = klass.__dict__["var2"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::foreach_is_not_abstract():
    assert not inspect.isabstract(myDsl::Foreach)


def test_mydsl::foreach_constructor_exists():
    assert callable(myDsl::Foreach.__init__)


def test_mydsl::foreach_constructor_args():
    sig = inspect.signature(myDsl::Foreach.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::if_is_not_abstract():
    assert not inspect.isabstract(myDsl::If)


def test_mydsl::if_constructor_exists():
    assert callable(myDsl::If.__init__)


def test_mydsl::if_constructor_args():
    sig = inspect.signature(myDsl::If.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::for_is_not_abstract():
    assert not inspect.isabstract(myDsl::For)


def test_mydsl::for_constructor_exists():
    assert callable(myDsl::For.__init__)


def test_mydsl::for_constructor_args():
    sig = inspect.signature(myDsl::For.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::while_is_not_abstract():
    assert not inspect.isabstract(myDsl::While)


def test_mydsl::while_constructor_exists():
    assert callable(myDsl::While.__init__)


def test_mydsl::while_constructor_args():
    sig = inspect.signature(myDsl::While.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::affectvar_is_not_abstract():
    assert not inspect.isabstract(myDsl::AffectVar)


def test_mydsl::affectvar_constructor_exists():
    assert callable(myDsl::AffectVar.__init__)


def test_mydsl::affectvar_constructor_args():
    sig = inspect.signature(myDsl::AffectVar.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::commande_is_not_abstract():
    assert not inspect.isabstract(myDsl::Commande)


def test_mydsl::commande_constructor_exists():
    assert callable(myDsl::Commande.__init__)


def test_mydsl::commande_constructor_args():
    sig = inspect.signature(myDsl::Commande.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_mydsl::commande_has_nop():
    assert hasattr(myDsl::Commande, "nop")
    descriptor = None
    for klass in myDsl::Commande.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::expr_is_not_abstract():
    assert not inspect.isabstract(myDsl::Expr)


def test_mydsl::expr_constructor_exists():
    assert callable(myDsl::Expr.__init__)


def test_mydsl::expr_constructor_args():
    sig = inspect.signature(myDsl::Expr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::output_is_not_abstract():
    assert not inspect.isabstract(myDsl::Output)


def test_mydsl::output_constructor_exists():
    assert callable(myDsl::Output.__init__)


def test_mydsl::output_constructor_args():
    sig = inspect.signature(myDsl::Output.__init__)
    params = list(sig.parameters.keys())
    assert "var1" in params, "Missing parameter 'var1'"
    assert "var2" in params, "Missing parameter 'var2'"

def test_mydsl::output_has_var1():
    assert hasattr(myDsl::Output, "var1")
    descriptor = None
    for klass in myDsl::Output.__mro__:
        if "var1" in klass.__dict__:
            descriptor = klass.__dict__["var1"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::output_has_var2():
    assert hasattr(myDsl::Output, "var2")
    descriptor = None
    for klass in myDsl::Output.__mro__:
        if "var2" in klass.__dict__:
            descriptor = klass.__dict__["var2"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::commandes_is_not_abstract():
    assert not inspect.isabstract(myDsl::Commandes)


def test_mydsl::commandes_constructor_exists():
    assert callable(myDsl::Commandes.__init__)


def test_mydsl::commandes_constructor_args():
    sig = inspect.signature(myDsl::Commandes.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::input_is_not_abstract():
    assert not inspect.isabstract(myDsl::Input)


def test_mydsl::input_constructor_exists():
    assert callable(myDsl::Input.__init__)


def test_mydsl::input_constructor_args():
    sig = inspect.signature(myDsl::Input.__init__)
    params = list(sig.parameters.keys())
    assert "var2" in params, "Missing parameter 'var2'"
    assert "var1" in params, "Missing parameter 'var1'"

def test_mydsl::input_has_var2():
    assert hasattr(myDsl::Input, "var2")
    descriptor = None
    for klass in myDsl::Input.__mro__:
        if "var2" in klass.__dict__:
            descriptor = klass.__dict__["var2"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::input_has_var1():
    assert hasattr(myDsl::Input, "var1")
    descriptor = None
    for klass in myDsl::Input.__mro__:
        if "var1" in klass.__dict__:
            descriptor = klass.__dict__["var1"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::fonction_is_not_abstract():
    assert not inspect.isabstract(myDsl::Fonction)


def test_mydsl::fonction_constructor_exists():
    assert callable(myDsl::Fonction.__init__)


def test_mydsl::fonction_constructor_args():
    sig = inspect.signature(myDsl::Fonction.__init__)
    params = list(sig.parameters.keys())
    assert "symbole" in params, "Missing parameter 'symbole'"

def test_mydsl::fonction_has_symbole():
    assert hasattr(myDsl::Fonction, "symbole")
    descriptor = None
    for klass in myDsl::Fonction.__mro__:
        if "symbole" in klass.__dict__:
            descriptor = klass.__dict__["symbole"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::programme_is_not_abstract():
    assert not inspect.isabstract(myDsl::Programme)


def test_mydsl::programme_constructor_exists():
    assert callable(myDsl::Programme.__init__)


def test_mydsl::programme_constructor_args():
    sig = inspect.signature(myDsl::Programme.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
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
myDsl::ExprEq_strategy = st.builds(
    myDsl::ExprEq,
)
myDsl::ExprNotDo_strategy = st.builds(
    myDsl::ExprNotDo,
)
myDsl::LExpr_strategy = st.builds(
    myDsl::LExpr,
)
myDsl::SymboleEx_strategy = st.builds(
    myDsl::SymboleEx,
    p=
        safe_text
)
myDsl::Tl_strategy = st.builds(
    myDsl::Tl,
)
myDsl::Hd_strategy = st.builds(
    myDsl::Hd,
)
myDsl::Liste_strategy = st.builds(
    myDsl::Liste,
)
myDsl::Cons_strategy = st.builds(
    myDsl::Cons,
)
myDsl::ExprSimple_strategy = st.builds(
    myDsl::ExprSimple,
    variable=
        safe_text,
    vide=
        safe_text,
    symbole=
        safe_text
)
myDsl::ExprAnd_strategy = st.builds(
    myDsl::ExprAnd,
)
myDsl::ExprNotNot_strategy = st.builds(
    myDsl::ExprNotNot,
)
myDsl::ExprNot_strategy = st.builds(
    myDsl::ExprNot,
)
myDsl::ExprOr_strategy = st.builds(
    myDsl::ExprOr,
)
myDsl::Exprs_strategy = st.builds(
    myDsl::Exprs,
)
myDsl::Vars_strategy = st.builds(
    myDsl::Vars,
    var3=
        safe_text,
    var2=
        safe_text
)
myDsl::Foreach_strategy = st.builds(
    myDsl::Foreach,
)
myDsl::If_strategy = st.builds(
    myDsl::If,
)
myDsl::For_strategy = st.builds(
    myDsl::For,
)
myDsl::While_strategy = st.builds(
    myDsl::While,
)
myDsl::AffectVar_strategy = st.builds(
    myDsl::AffectVar,
)
myDsl::Commande_strategy = st.builds(
    myDsl::Commande,
    nop=
        safe_text
)
myDsl::Expr_strategy = st.builds(
    myDsl::Expr,
)
myDsl::Output_strategy = st.builds(
    myDsl::Output,
    var1=
        safe_text,
    var2=
        safe_text
)
myDsl::Commandes_strategy = st.builds(
    myDsl::Commandes,
)
myDsl::Input_strategy = st.builds(
    myDsl::Input,
    var2=
        safe_text,
    var1=
        safe_text
)
myDsl::Fonction_strategy = st.builds(
    myDsl::Fonction,
    symbole=
        safe_text
)
myDsl::Programme_strategy = st.builds(
    myDsl::Programme,
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)

@given(instance=myDsl::ExprEq_strategy)
@settings(max_examples=50)
def test_mydsl::expreq_instantiation(instance):
    assert isinstance(instance, myDsl::ExprEq)

@given(instance=myDsl::ExprNotDo_strategy)
@settings(max_examples=50)
def test_mydsl::exprnotdo_instantiation(instance):
    assert isinstance(instance, myDsl::ExprNotDo)

@given(instance=myDsl::LExpr_strategy)
@settings(max_examples=50)
def test_mydsl::lexpr_instantiation(instance):
    assert isinstance(instance, myDsl::LExpr)

@given(instance=myDsl::SymboleEx_strategy)
@settings(max_examples=50)
def test_mydsl::symboleex_instantiation(instance):
    assert isinstance(instance, myDsl::SymboleEx)

@given(instance=myDsl::SymboleEx_strategy)
def test_mydsl::symboleex_p_type(instance):
    assert isinstance(instance.p, str)


@given(instance=myDsl::SymboleEx_strategy)
def test_mydsl::symboleex_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original

@given(instance=myDsl::Tl_strategy)
@settings(max_examples=50)
def test_mydsl::tl_instantiation(instance):
    assert isinstance(instance, myDsl::Tl)

@given(instance=myDsl::Hd_strategy)
@settings(max_examples=50)
def test_mydsl::hd_instantiation(instance):
    assert isinstance(instance, myDsl::Hd)

@given(instance=myDsl::Liste_strategy)
@settings(max_examples=50)
def test_mydsl::liste_instantiation(instance):
    assert isinstance(instance, myDsl::Liste)

@given(instance=myDsl::Cons_strategy)
@settings(max_examples=50)
def test_mydsl::cons_instantiation(instance):
    assert isinstance(instance, myDsl::Cons)

@given(instance=myDsl::ExprSimple_strategy)
@settings(max_examples=50)
def test_mydsl::exprsimple_instantiation(instance):
    assert isinstance(instance, myDsl::ExprSimple)

@given(instance=myDsl::ExprSimple_strategy)
def test_mydsl::exprsimple_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=myDsl::ExprSimple_strategy)
def test_mydsl::exprsimple_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=myDsl::ExprSimple_strategy)
def test_mydsl::exprsimple_vide_type(instance):
    assert isinstance(instance.vide, str)


@given(instance=myDsl::ExprSimple_strategy)
def test_mydsl::exprsimple_vide_setter(instance):
    original = instance.vide
    instance.vide = original
    assert instance.vide == original

@given(instance=myDsl::ExprSimple_strategy)
def test_mydsl::exprsimple_symbole_type(instance):
    assert isinstance(instance.symbole, str)


@given(instance=myDsl::ExprSimple_strategy)
def test_mydsl::exprsimple_symbole_setter(instance):
    original = instance.symbole
    instance.symbole = original
    assert instance.symbole == original

@given(instance=myDsl::ExprAnd_strategy)
@settings(max_examples=50)
def test_mydsl::exprand_instantiation(instance):
    assert isinstance(instance, myDsl::ExprAnd)

@given(instance=myDsl::ExprNotNot_strategy)
@settings(max_examples=50)
def test_mydsl::exprnotnot_instantiation(instance):
    assert isinstance(instance, myDsl::ExprNotNot)

@given(instance=myDsl::ExprNot_strategy)
@settings(max_examples=50)
def test_mydsl::exprnot_instantiation(instance):
    assert isinstance(instance, myDsl::ExprNot)

@given(instance=myDsl::ExprOr_strategy)
@settings(max_examples=50)
def test_mydsl::expror_instantiation(instance):
    assert isinstance(instance, myDsl::ExprOr)

@given(instance=myDsl::Exprs_strategy)
@settings(max_examples=50)
def test_mydsl::exprs_instantiation(instance):
    assert isinstance(instance, myDsl::Exprs)

@given(instance=myDsl::Vars_strategy)
@settings(max_examples=50)
def test_mydsl::vars_instantiation(instance):
    assert isinstance(instance, myDsl::Vars)

@given(instance=myDsl::Vars_strategy)
def test_mydsl::vars_var3_type(instance):
    assert isinstance(instance.var3, str)


@given(instance=myDsl::Vars_strategy)
def test_mydsl::vars_var3_setter(instance):
    original = instance.var3
    instance.var3 = original
    assert instance.var3 == original

@given(instance=myDsl::Vars_strategy)
def test_mydsl::vars_var2_type(instance):
    assert isinstance(instance.var2, str)


@given(instance=myDsl::Vars_strategy)
def test_mydsl::vars_var2_setter(instance):
    original = instance.var2
    instance.var2 = original
    assert instance.var2 == original

@given(instance=myDsl::Foreach_strategy)
@settings(max_examples=50)
def test_mydsl::foreach_instantiation(instance):
    assert isinstance(instance, myDsl::Foreach)

@given(instance=myDsl::If_strategy)
@settings(max_examples=50)
def test_mydsl::if_instantiation(instance):
    assert isinstance(instance, myDsl::If)

@given(instance=myDsl::For_strategy)
@settings(max_examples=50)
def test_mydsl::for_instantiation(instance):
    assert isinstance(instance, myDsl::For)

@given(instance=myDsl::While_strategy)
@settings(max_examples=50)
def test_mydsl::while_instantiation(instance):
    assert isinstance(instance, myDsl::While)

@given(instance=myDsl::AffectVar_strategy)
@settings(max_examples=50)
def test_mydsl::affectvar_instantiation(instance):
    assert isinstance(instance, myDsl::AffectVar)

@given(instance=myDsl::Commande_strategy)
@settings(max_examples=50)
def test_mydsl::commande_instantiation(instance):
    assert isinstance(instance, myDsl::Commande)

@given(instance=myDsl::Commande_strategy)
def test_mydsl::commande_nop_type(instance):
    assert isinstance(instance.nop, str)


@given(instance=myDsl::Commande_strategy)
def test_mydsl::commande_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=myDsl::Expr_strategy)
@settings(max_examples=50)
def test_mydsl::expr_instantiation(instance):
    assert isinstance(instance, myDsl::Expr)

@given(instance=myDsl::Output_strategy)
@settings(max_examples=50)
def test_mydsl::output_instantiation(instance):
    assert isinstance(instance, myDsl::Output)

@given(instance=myDsl::Output_strategy)
def test_mydsl::output_var1_type(instance):
    assert isinstance(instance.var1, str)


@given(instance=myDsl::Output_strategy)
def test_mydsl::output_var1_setter(instance):
    original = instance.var1
    instance.var1 = original
    assert instance.var1 == original

@given(instance=myDsl::Output_strategy)
def test_mydsl::output_var2_type(instance):
    assert isinstance(instance.var2, str)


@given(instance=myDsl::Output_strategy)
def test_mydsl::output_var2_setter(instance):
    original = instance.var2
    instance.var2 = original
    assert instance.var2 == original

@given(instance=myDsl::Commandes_strategy)
@settings(max_examples=50)
def test_mydsl::commandes_instantiation(instance):
    assert isinstance(instance, myDsl::Commandes)

@given(instance=myDsl::Input_strategy)
@settings(max_examples=50)
def test_mydsl::input_instantiation(instance):
    assert isinstance(instance, myDsl::Input)

@given(instance=myDsl::Input_strategy)
def test_mydsl::input_var2_type(instance):
    assert isinstance(instance.var2, str)


@given(instance=myDsl::Input_strategy)
def test_mydsl::input_var2_setter(instance):
    original = instance.var2
    instance.var2 = original
    assert instance.var2 == original

@given(instance=myDsl::Input_strategy)
def test_mydsl::input_var1_type(instance):
    assert isinstance(instance.var1, str)


@given(instance=myDsl::Input_strategy)
def test_mydsl::input_var1_setter(instance):
    original = instance.var1
    instance.var1 = original
    assert instance.var1 == original

@given(instance=myDsl::Fonction_strategy)
@settings(max_examples=50)
def test_mydsl::fonction_instantiation(instance):
    assert isinstance(instance, myDsl::Fonction)

@given(instance=myDsl::Fonction_strategy)
def test_mydsl::fonction_symbole_type(instance):
    assert isinstance(instance.symbole, str)


@given(instance=myDsl::Fonction_strategy)
def test_mydsl::fonction_symbole_setter(instance):
    original = instance.symbole
    instance.symbole = original
    assert instance.symbole == original

@given(instance=myDsl::Programme_strategy)
@settings(max_examples=50)
def test_mydsl::programme_instantiation(instance):
    assert isinstance(instance, myDsl::Programme)

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)
