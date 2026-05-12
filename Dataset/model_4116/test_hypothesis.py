import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl_ExprEq,
    myDsl_ExprNotDo,
    myDsl_LExpr,
    myDsl_SymboleEx,
    myDsl_Tl,
    myDsl_Hd,
    myDsl_Liste,
    myDsl_Cons,
    myDsl_ExprSimple,
    myDsl_ExprAnd,
    myDsl_ExprNotNot,
    myDsl_ExprNot,
    myDsl_ExprOr,
    myDsl_Exprs,
    myDsl_Vars,
    myDsl_Foreach,
    myDsl_If,
    myDsl_For,
    myDsl_While,
    myDsl_AffectVar,
    myDsl_Commande,
    myDsl_Expr,
    myDsl_Output,
    myDsl_Commandes,
    myDsl_Input,
    myDsl_Fonction,
    myDsl_Programme,
    myDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_expreq_is_not_abstract():
    assert not inspect.isabstract(myDsl_ExprEq)


def test_mydsl_expreq_constructor_exists():
    assert callable(myDsl_ExprEq.__init__)


def test_mydsl_expreq_constructor_args():
    sig = inspect.signature(myDsl_ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_exprnotdo_is_not_abstract():
    assert not inspect.isabstract(myDsl_ExprNotDo)


def test_mydsl_exprnotdo_constructor_exists():
    assert callable(myDsl_ExprNotDo.__init__)


def test_mydsl_exprnotdo_constructor_args():
    sig = inspect.signature(myDsl_ExprNotDo.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_lexpr_is_not_abstract():
    assert not inspect.isabstract(myDsl_LExpr)


def test_mydsl_lexpr_constructor_exists():
    assert callable(myDsl_LExpr.__init__)


def test_mydsl_lexpr_constructor_args():
    sig = inspect.signature(myDsl_LExpr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_symboleex_is_not_abstract():
    assert not inspect.isabstract(myDsl_SymboleEx)


def test_mydsl_symboleex_constructor_exists():
    assert callable(myDsl_SymboleEx.__init__)


def test_mydsl_symboleex_constructor_args():
    sig = inspect.signature(myDsl_SymboleEx.__init__)
    params = list(sig.parameters.keys())
    assert "p" in params, "Missing parameter 'p'"

def test_mydsl_symboleex_has_p():
    assert hasattr(myDsl_SymboleEx, "p")
    descriptor = None
    for klass in myDsl_SymboleEx.__mro__:
        if "p" in klass.__dict__:
            descriptor = klass.__dict__["p"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_tl_is_not_abstract():
    assert not inspect.isabstract(myDsl_Tl)


def test_mydsl_tl_constructor_exists():
    assert callable(myDsl_Tl.__init__)


def test_mydsl_tl_constructor_args():
    sig = inspect.signature(myDsl_Tl.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_hd_is_not_abstract():
    assert not inspect.isabstract(myDsl_Hd)


def test_mydsl_hd_constructor_exists():
    assert callable(myDsl_Hd.__init__)


def test_mydsl_hd_constructor_args():
    sig = inspect.signature(myDsl_Hd.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_liste_is_not_abstract():
    assert not inspect.isabstract(myDsl_Liste)


def test_mydsl_liste_constructor_exists():
    assert callable(myDsl_Liste.__init__)


def test_mydsl_liste_constructor_args():
    sig = inspect.signature(myDsl_Liste.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_cons_is_not_abstract():
    assert not inspect.isabstract(myDsl_Cons)


def test_mydsl_cons_constructor_exists():
    assert callable(myDsl_Cons.__init__)


def test_mydsl_cons_constructor_args():
    sig = inspect.signature(myDsl_Cons.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_exprsimple_is_not_abstract():
    assert not inspect.isabstract(myDsl_ExprSimple)


def test_mydsl_exprsimple_constructor_exists():
    assert callable(myDsl_ExprSimple.__init__)


def test_mydsl_exprsimple_constructor_args():
    sig = inspect.signature(myDsl_ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "vide" in params, "Missing parameter 'vide'"
    assert "symbole" in params, "Missing parameter 'symbole'"
    assert "variable" in params, "Missing parameter 'variable'"

def test_mydsl_exprsimple_has_vide():
    assert hasattr(myDsl_ExprSimple, "vide")
    descriptor = None
    for klass in myDsl_ExprSimple.__mro__:
        if "vide" in klass.__dict__:
            descriptor = klass.__dict__["vide"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_exprsimple_has_symbole():
    assert hasattr(myDsl_ExprSimple, "symbole")
    descriptor = None
    for klass in myDsl_ExprSimple.__mro__:
        if "symbole" in klass.__dict__:
            descriptor = klass.__dict__["symbole"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_exprsimple_has_variable():
    assert hasattr(myDsl_ExprSimple, "variable")
    descriptor = None
    for klass in myDsl_ExprSimple.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_exprand_is_not_abstract():
    assert not inspect.isabstract(myDsl_ExprAnd)


def test_mydsl_exprand_constructor_exists():
    assert callable(myDsl_ExprAnd.__init__)


def test_mydsl_exprand_constructor_args():
    sig = inspect.signature(myDsl_ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_exprnotnot_is_not_abstract():
    assert not inspect.isabstract(myDsl_ExprNotNot)


def test_mydsl_exprnotnot_constructor_exists():
    assert callable(myDsl_ExprNotNot.__init__)


def test_mydsl_exprnotnot_constructor_args():
    sig = inspect.signature(myDsl_ExprNotNot.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_exprnot_is_not_abstract():
    assert not inspect.isabstract(myDsl_ExprNot)


def test_mydsl_exprnot_constructor_exists():
    assert callable(myDsl_ExprNot.__init__)


def test_mydsl_exprnot_constructor_args():
    sig = inspect.signature(myDsl_ExprNot.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_expror_is_not_abstract():
    assert not inspect.isabstract(myDsl_ExprOr)


def test_mydsl_expror_constructor_exists():
    assert callable(myDsl_ExprOr.__init__)


def test_mydsl_expror_constructor_args():
    sig = inspect.signature(myDsl_ExprOr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_exprs_is_not_abstract():
    assert not inspect.isabstract(myDsl_Exprs)


def test_mydsl_exprs_constructor_exists():
    assert callable(myDsl_Exprs.__init__)


def test_mydsl_exprs_constructor_args():
    sig = inspect.signature(myDsl_Exprs.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_vars_is_not_abstract():
    assert not inspect.isabstract(myDsl_Vars)


def test_mydsl_vars_constructor_exists():
    assert callable(myDsl_Vars.__init__)


def test_mydsl_vars_constructor_args():
    sig = inspect.signature(myDsl_Vars.__init__)
    params = list(sig.parameters.keys())
    assert "var3" in params, "Missing parameter 'var3'"
    assert "var2" in params, "Missing parameter 'var2'"

def test_mydsl_vars_has_var3():
    assert hasattr(myDsl_Vars, "var3")
    descriptor = None
    for klass in myDsl_Vars.__mro__:
        if "var3" in klass.__dict__:
            descriptor = klass.__dict__["var3"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_vars_has_var2():
    assert hasattr(myDsl_Vars, "var2")
    descriptor = None
    for klass in myDsl_Vars.__mro__:
        if "var2" in klass.__dict__:
            descriptor = klass.__dict__["var2"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_foreach_is_not_abstract():
    assert not inspect.isabstract(myDsl_Foreach)


def test_mydsl_foreach_constructor_exists():
    assert callable(myDsl_Foreach.__init__)


def test_mydsl_foreach_constructor_args():
    sig = inspect.signature(myDsl_Foreach.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_if_is_not_abstract():
    assert not inspect.isabstract(myDsl_If)


def test_mydsl_if_constructor_exists():
    assert callable(myDsl_If.__init__)


def test_mydsl_if_constructor_args():
    sig = inspect.signature(myDsl_If.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_for_is_not_abstract():
    assert not inspect.isabstract(myDsl_For)


def test_mydsl_for_constructor_exists():
    assert callable(myDsl_For.__init__)


def test_mydsl_for_constructor_args():
    sig = inspect.signature(myDsl_For.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_while_is_not_abstract():
    assert not inspect.isabstract(myDsl_While)


def test_mydsl_while_constructor_exists():
    assert callable(myDsl_While.__init__)


def test_mydsl_while_constructor_args():
    sig = inspect.signature(myDsl_While.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_affectvar_is_not_abstract():
    assert not inspect.isabstract(myDsl_AffectVar)


def test_mydsl_affectvar_constructor_exists():
    assert callable(myDsl_AffectVar.__init__)


def test_mydsl_affectvar_constructor_args():
    sig = inspect.signature(myDsl_AffectVar.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_commande_is_not_abstract():
    assert not inspect.isabstract(myDsl_Commande)


def test_mydsl_commande_constructor_exists():
    assert callable(myDsl_Commande.__init__)


def test_mydsl_commande_constructor_args():
    sig = inspect.signature(myDsl_Commande.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_mydsl_commande_has_nop():
    assert hasattr(myDsl_Commande, "nop")
    descriptor = None
    for klass in myDsl_Commande.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_expr_is_not_abstract():
    assert not inspect.isabstract(myDsl_Expr)


def test_mydsl_expr_constructor_exists():
    assert callable(myDsl_Expr.__init__)


def test_mydsl_expr_constructor_args():
    sig = inspect.signature(myDsl_Expr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_output_is_not_abstract():
    assert not inspect.isabstract(myDsl_Output)


def test_mydsl_output_constructor_exists():
    assert callable(myDsl_Output.__init__)


def test_mydsl_output_constructor_args():
    sig = inspect.signature(myDsl_Output.__init__)
    params = list(sig.parameters.keys())
    assert "var2" in params, "Missing parameter 'var2'"
    assert "var1" in params, "Missing parameter 'var1'"

def test_mydsl_output_has_var2():
    assert hasattr(myDsl_Output, "var2")
    descriptor = None
    for klass in myDsl_Output.__mro__:
        if "var2" in klass.__dict__:
            descriptor = klass.__dict__["var2"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_output_has_var1():
    assert hasattr(myDsl_Output, "var1")
    descriptor = None
    for klass in myDsl_Output.__mro__:
        if "var1" in klass.__dict__:
            descriptor = klass.__dict__["var1"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_commandes_is_not_abstract():
    assert not inspect.isabstract(myDsl_Commandes)


def test_mydsl_commandes_constructor_exists():
    assert callable(myDsl_Commandes.__init__)


def test_mydsl_commandes_constructor_args():
    sig = inspect.signature(myDsl_Commandes.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_input_is_not_abstract():
    assert not inspect.isabstract(myDsl_Input)


def test_mydsl_input_constructor_exists():
    assert callable(myDsl_Input.__init__)


def test_mydsl_input_constructor_args():
    sig = inspect.signature(myDsl_Input.__init__)
    params = list(sig.parameters.keys())
    assert "var1" in params, "Missing parameter 'var1'"
    assert "var2" in params, "Missing parameter 'var2'"

def test_mydsl_input_has_var1():
    assert hasattr(myDsl_Input, "var1")
    descriptor = None
    for klass in myDsl_Input.__mro__:
        if "var1" in klass.__dict__:
            descriptor = klass.__dict__["var1"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_input_has_var2():
    assert hasattr(myDsl_Input, "var2")
    descriptor = None
    for klass in myDsl_Input.__mro__:
        if "var2" in klass.__dict__:
            descriptor = klass.__dict__["var2"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_fonction_is_not_abstract():
    assert not inspect.isabstract(myDsl_Fonction)


def test_mydsl_fonction_constructor_exists():
    assert callable(myDsl_Fonction.__init__)


def test_mydsl_fonction_constructor_args():
    sig = inspect.signature(myDsl_Fonction.__init__)
    params = list(sig.parameters.keys())
    assert "symbole" in params, "Missing parameter 'symbole'"

def test_mydsl_fonction_has_symbole():
    assert hasattr(myDsl_Fonction, "symbole")
    descriptor = None
    for klass in myDsl_Fonction.__mro__:
        if "symbole" in klass.__dict__:
            descriptor = klass.__dict__["symbole"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_programme_is_not_abstract():
    assert not inspect.isabstract(myDsl_Programme)


def test_mydsl_programme_constructor_exists():
    assert callable(myDsl_Programme.__init__)


def test_mydsl_programme_constructor_args():
    sig = inspect.signature(myDsl_Programme.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_model_is_not_abstract():
    assert not inspect.isabstract(myDsl_Model)


def test_mydsl_model_constructor_exists():
    assert callable(myDsl_Model.__init__)


def test_mydsl_model_constructor_args():
    sig = inspect.signature(myDsl_Model.__init__)
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
myDsl_ExprEq_strategy = st.builds(
    myDsl_ExprEq,
)
myDsl_ExprNotDo_strategy = st.builds(
    myDsl_ExprNotDo,
)
myDsl_LExpr_strategy = st.builds(
    myDsl_LExpr,
)
myDsl_SymboleEx_strategy = st.builds(
    myDsl_SymboleEx,
    p=
        safe_text
)
myDsl_Tl_strategy = st.builds(
    myDsl_Tl,
)
myDsl_Hd_strategy = st.builds(
    myDsl_Hd,
)
myDsl_Liste_strategy = st.builds(
    myDsl_Liste,
)
myDsl_Cons_strategy = st.builds(
    myDsl_Cons,
)
myDsl_ExprSimple_strategy = st.builds(
    myDsl_ExprSimple,
    vide=
        safe_text,
    symbole=
        safe_text,
    variable=
        safe_text
)
myDsl_ExprAnd_strategy = st.builds(
    myDsl_ExprAnd,
)
myDsl_ExprNotNot_strategy = st.builds(
    myDsl_ExprNotNot,
)
myDsl_ExprNot_strategy = st.builds(
    myDsl_ExprNot,
)
myDsl_ExprOr_strategy = st.builds(
    myDsl_ExprOr,
)
myDsl_Exprs_strategy = st.builds(
    myDsl_Exprs,
)
myDsl_Vars_strategy = st.builds(
    myDsl_Vars,
    var3=
        safe_text,
    var2=
        safe_text
)
myDsl_Foreach_strategy = st.builds(
    myDsl_Foreach,
)
myDsl_If_strategy = st.builds(
    myDsl_If,
)
myDsl_For_strategy = st.builds(
    myDsl_For,
)
myDsl_While_strategy = st.builds(
    myDsl_While,
)
myDsl_AffectVar_strategy = st.builds(
    myDsl_AffectVar,
)
myDsl_Commande_strategy = st.builds(
    myDsl_Commande,
    nop=
        safe_text
)
myDsl_Expr_strategy = st.builds(
    myDsl_Expr,
)
myDsl_Output_strategy = st.builds(
    myDsl_Output,
    var2=
        safe_text,
    var1=
        safe_text
)
myDsl_Commandes_strategy = st.builds(
    myDsl_Commandes,
)
myDsl_Input_strategy = st.builds(
    myDsl_Input,
    var1=
        safe_text,
    var2=
        safe_text
)
myDsl_Fonction_strategy = st.builds(
    myDsl_Fonction,
    symbole=
        safe_text
)
myDsl_Programme_strategy = st.builds(
    myDsl_Programme,
)
myDsl_Model_strategy = st.builds(
    myDsl_Model,
)

@given(instance=myDsl_ExprEq_strategy)
@settings(max_examples=50)
def test_mydsl_expreq_instantiation(instance):
    assert isinstance(instance, myDsl_ExprEq)

@given(instance=myDsl_ExprNotDo_strategy)
@settings(max_examples=50)
def test_mydsl_exprnotdo_instantiation(instance):
    assert isinstance(instance, myDsl_ExprNotDo)

@given(instance=myDsl_LExpr_strategy)
@settings(max_examples=50)
def test_mydsl_lexpr_instantiation(instance):
    assert isinstance(instance, myDsl_LExpr)

@given(instance=myDsl_SymboleEx_strategy)
@settings(max_examples=50)
def test_mydsl_symboleex_instantiation(instance):
    assert isinstance(instance, myDsl_SymboleEx)



@given(instance=myDsl_SymboleEx_strategy)
def test_mydsl_symboleex_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original

@given(instance=myDsl_Tl_strategy)
@settings(max_examples=50)
def test_mydsl_tl_instantiation(instance):
    assert isinstance(instance, myDsl_Tl)

@given(instance=myDsl_Hd_strategy)
@settings(max_examples=50)
def test_mydsl_hd_instantiation(instance):
    assert isinstance(instance, myDsl_Hd)

@given(instance=myDsl_Liste_strategy)
@settings(max_examples=50)
def test_mydsl_liste_instantiation(instance):
    assert isinstance(instance, myDsl_Liste)

@given(instance=myDsl_Cons_strategy)
@settings(max_examples=50)
def test_mydsl_cons_instantiation(instance):
    assert isinstance(instance, myDsl_Cons)

@given(instance=myDsl_ExprSimple_strategy)
@settings(max_examples=50)
def test_mydsl_exprsimple_instantiation(instance):
    assert isinstance(instance, myDsl_ExprSimple)



@given(instance=myDsl_ExprSimple_strategy)
def test_mydsl_exprsimple_vide_setter(instance):
    original = instance.vide
    instance.vide = original
    assert instance.vide == original



@given(instance=myDsl_ExprSimple_strategy)
def test_mydsl_exprsimple_symbole_setter(instance):
    original = instance.symbole
    instance.symbole = original
    assert instance.symbole == original



@given(instance=myDsl_ExprSimple_strategy)
def test_mydsl_exprsimple_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=myDsl_ExprAnd_strategy)
@settings(max_examples=50)
def test_mydsl_exprand_instantiation(instance):
    assert isinstance(instance, myDsl_ExprAnd)

@given(instance=myDsl_ExprNotNot_strategy)
@settings(max_examples=50)
def test_mydsl_exprnotnot_instantiation(instance):
    assert isinstance(instance, myDsl_ExprNotNot)

@given(instance=myDsl_ExprNot_strategy)
@settings(max_examples=50)
def test_mydsl_exprnot_instantiation(instance):
    assert isinstance(instance, myDsl_ExprNot)

@given(instance=myDsl_ExprOr_strategy)
@settings(max_examples=50)
def test_mydsl_expror_instantiation(instance):
    assert isinstance(instance, myDsl_ExprOr)

@given(instance=myDsl_Exprs_strategy)
@settings(max_examples=50)
def test_mydsl_exprs_instantiation(instance):
    assert isinstance(instance, myDsl_Exprs)

@given(instance=myDsl_Vars_strategy)
@settings(max_examples=50)
def test_mydsl_vars_instantiation(instance):
    assert isinstance(instance, myDsl_Vars)



@given(instance=myDsl_Vars_strategy)
def test_mydsl_vars_var3_setter(instance):
    original = instance.var3
    instance.var3 = original
    assert instance.var3 == original



@given(instance=myDsl_Vars_strategy)
def test_mydsl_vars_var2_setter(instance):
    original = instance.var2
    instance.var2 = original
    assert instance.var2 == original

@given(instance=myDsl_Foreach_strategy)
@settings(max_examples=50)
def test_mydsl_foreach_instantiation(instance):
    assert isinstance(instance, myDsl_Foreach)

@given(instance=myDsl_If_strategy)
@settings(max_examples=50)
def test_mydsl_if_instantiation(instance):
    assert isinstance(instance, myDsl_If)

@given(instance=myDsl_For_strategy)
@settings(max_examples=50)
def test_mydsl_for_instantiation(instance):
    assert isinstance(instance, myDsl_For)

@given(instance=myDsl_While_strategy)
@settings(max_examples=50)
def test_mydsl_while_instantiation(instance):
    assert isinstance(instance, myDsl_While)

@given(instance=myDsl_AffectVar_strategy)
@settings(max_examples=50)
def test_mydsl_affectvar_instantiation(instance):
    assert isinstance(instance, myDsl_AffectVar)

@given(instance=myDsl_Commande_strategy)
@settings(max_examples=50)
def test_mydsl_commande_instantiation(instance):
    assert isinstance(instance, myDsl_Commande)



@given(instance=myDsl_Commande_strategy)
def test_mydsl_commande_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=myDsl_Expr_strategy)
@settings(max_examples=50)
def test_mydsl_expr_instantiation(instance):
    assert isinstance(instance, myDsl_Expr)

@given(instance=myDsl_Output_strategy)
@settings(max_examples=50)
def test_mydsl_output_instantiation(instance):
    assert isinstance(instance, myDsl_Output)



@given(instance=myDsl_Output_strategy)
def test_mydsl_output_var2_setter(instance):
    original = instance.var2
    instance.var2 = original
    assert instance.var2 == original



@given(instance=myDsl_Output_strategy)
def test_mydsl_output_var1_setter(instance):
    original = instance.var1
    instance.var1 = original
    assert instance.var1 == original

@given(instance=myDsl_Commandes_strategy)
@settings(max_examples=50)
def test_mydsl_commandes_instantiation(instance):
    assert isinstance(instance, myDsl_Commandes)

@given(instance=myDsl_Input_strategy)
@settings(max_examples=50)
def test_mydsl_input_instantiation(instance):
    assert isinstance(instance, myDsl_Input)



@given(instance=myDsl_Input_strategy)
def test_mydsl_input_var1_setter(instance):
    original = instance.var1
    instance.var1 = original
    assert instance.var1 == original



@given(instance=myDsl_Input_strategy)
def test_mydsl_input_var2_setter(instance):
    original = instance.var2
    instance.var2 = original
    assert instance.var2 == original

@given(instance=myDsl_Fonction_strategy)
@settings(max_examples=50)
def test_mydsl_fonction_instantiation(instance):
    assert isinstance(instance, myDsl_Fonction)



@given(instance=myDsl_Fonction_strategy)
def test_mydsl_fonction_symbole_setter(instance):
    original = instance.symbole
    instance.symbole = original
    assert instance.symbole == original

@given(instance=myDsl_Programme_strategy)
@settings(max_examples=50)
def test_mydsl_programme_instantiation(instance):
    assert isinstance(instance, myDsl_Programme)

@given(instance=myDsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, myDsl_Model)
