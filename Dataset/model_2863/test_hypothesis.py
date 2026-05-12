import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    gDSL_ValueDecl,
    gDSL_Field,
    ApplyExp,
    gDSL_Args,
    gDSL_AtomicExp,
    SelectExp,
    gDSL_ApplyExp,
    MExp,
    gDSL_SelectExp,
    AExp,
    gDSL_MExp,
    RExp,
    gDSL_AExp,
    AndAlsoExp,
    gDSL_RExp,
    OrElseExp,
    gDSL_AndAlsoExp,
    ClosedExp,
    gDSL_OrElseExp,
    gDSL_MonadicExp,
    CaseExp,
    gDSL_PAT,
    gDSL_ClosedExp,
    gDSL_CaseExp,
    gDSL_TyElement,
    gDSL_TyBind,
    gDSL_CONS,
    gDSL_Exp,
    gDSL_Ty,
    gDSL_TyVars,
    Decl,
    gDSL_Type,
    gDSL_Val,
    gDSL_DeclExport,
    gDSL_Decl,
    gDSL_Model,
    gDSL_ConDecl,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gdsl_valuedecl_is_not_abstract():
    assert not inspect.isabstract(gDSL_ValueDecl)


def test_gdsl_valuedecl_constructor_exists():
    assert callable(gDSL_ValueDecl.__init__)


def test_gdsl_valuedecl_constructor_args():
    sig = inspect.signature(gDSL_ValueDecl.__init__)
    params = list(sig.parameters.keys())
    assert "ids" in params, "Missing parameter 'ids'"
    assert "name" in params, "Missing parameter 'name'"

def test_gdsl_valuedecl_has_ids():
    assert hasattr(gDSL_ValueDecl, "ids")
    descriptor = None
    for klass in gDSL_ValueDecl.__mro__:
        if "ids" in klass.__dict__:
            descriptor = klass.__dict__["ids"]
            break
    assert isinstance(descriptor, property)

def test_gdsl_valuedecl_has_name():
    assert hasattr(gDSL_ValueDecl, "name")
    descriptor = None
    for klass in gDSL_ValueDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gdsl_field_is_not_abstract():
    assert not inspect.isabstract(gDSL_Field)


def test_gdsl_field_constructor_exists():
    assert callable(gDSL_Field.__init__)


def test_gdsl_field_constructor_args():
    sig = inspect.signature(gDSL_Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gdsl_field_has_name():
    assert hasattr(gDSL_Field, "name")
    descriptor = None
    for klass in gDSL_Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_applyexp_is_not_abstract():
    assert not inspect.isabstract(ApplyExp)


def test_applyexp_constructor_exists():
    assert callable(ApplyExp.__init__)


def test_applyexp_constructor_args():
    sig = inspect.signature(ApplyExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_args_is_not_abstract():
    assert not inspect.isabstract(gDSL_Args)


def test_gdsl_args_constructor_exists():
    assert callable(gDSL_Args.__init__)


def test_gdsl_args_constructor_args():
    sig = inspect.signature(gDSL_Args.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_atomicexp_is_not_abstract():
    assert not inspect.isabstract(gDSL_AtomicExp)


def test_gdsl_atomicexp_constructor_exists():
    assert callable(gDSL_AtomicExp.__init__)


def test_gdsl_atomicexp_constructor_args():
    sig = inspect.signature(gDSL_AtomicExp.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_gdsl_atomicexp_has_id():
    assert hasattr(gDSL_AtomicExp, "id")
    descriptor = None
    for klass in gDSL_AtomicExp.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_selectexp_is_not_abstract():
    assert not inspect.isabstract(SelectExp)


def test_selectexp_constructor_exists():
    assert callable(SelectExp.__init__)


def test_selectexp_constructor_args():
    sig = inspect.signature(SelectExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_applyexp_is_not_abstract():
    assert not inspect.isabstract(gDSL_ApplyExp)


def test_gdsl_applyexp_constructor_exists():
    assert callable(gDSL_ApplyExp.__init__)


def test_gdsl_applyexp_constructor_args():
    sig = inspect.signature(gDSL_ApplyExp.__init__)
    params = list(sig.parameters.keys())



def test_mexp_is_not_abstract():
    assert not inspect.isabstract(MExp)


def test_mexp_constructor_exists():
    assert callable(MExp.__init__)


def test_mexp_constructor_args():
    sig = inspect.signature(MExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_selectexp_is_not_abstract():
    assert not inspect.isabstract(gDSL_SelectExp)


def test_gdsl_selectexp_constructor_exists():
    assert callable(gDSL_SelectExp.__init__)


def test_gdsl_selectexp_constructor_args():
    sig = inspect.signature(gDSL_SelectExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_gdsl_selectexp_has_symbol():
    assert hasattr(gDSL_SelectExp, "symbol")
    descriptor = None
    for klass in gDSL_SelectExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_aexp_is_not_abstract():
    assert not inspect.isabstract(AExp)


def test_aexp_constructor_exists():
    assert callable(AExp.__init__)


def test_aexp_constructor_args():
    sig = inspect.signature(AExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_mexp_is_not_abstract():
    assert not inspect.isabstract(gDSL_MExp)


def test_gdsl_mexp_constructor_exists():
    assert callable(gDSL_MExp.__init__)


def test_gdsl_mexp_constructor_args():
    sig = inspect.signature(gDSL_MExp.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"

def test_gdsl_mexp_has_sign():
    assert hasattr(gDSL_MExp, "sign")
    descriptor = None
    for klass in gDSL_MExp.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)



def test_rexp_is_not_abstract():
    assert not inspect.isabstract(RExp)


def test_rexp_constructor_exists():
    assert callable(RExp.__init__)


def test_rexp_constructor_args():
    sig = inspect.signature(RExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_aexp_is_not_abstract():
    assert not inspect.isabstract(gDSL_AExp)


def test_gdsl_aexp_constructor_exists():
    assert callable(gDSL_AExp.__init__)


def test_gdsl_aexp_constructor_args():
    sig = inspect.signature(gDSL_AExp.__init__)
    params = list(sig.parameters.keys())
    assert "sym" in params, "Missing parameter 'sym'"

def test_gdsl_aexp_has_sym():
    assert hasattr(gDSL_AExp, "sym")
    descriptor = None
    for klass in gDSL_AExp.__mro__:
        if "sym" in klass.__dict__:
            descriptor = klass.__dict__["sym"]
            break
    assert isinstance(descriptor, property)



def test_andalsoexp_is_not_abstract():
    assert not inspect.isabstract(AndAlsoExp)


def test_andalsoexp_constructor_exists():
    assert callable(AndAlsoExp.__init__)


def test_andalsoexp_constructor_args():
    sig = inspect.signature(AndAlsoExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_rexp_is_not_abstract():
    assert not inspect.isabstract(gDSL_RExp)


def test_gdsl_rexp_constructor_exists():
    assert callable(gDSL_RExp.__init__)


def test_gdsl_rexp_constructor_args():
    sig = inspect.signature(gDSL_RExp.__init__)
    params = list(sig.parameters.keys())



def test_orelseexp_is_not_abstract():
    assert not inspect.isabstract(OrElseExp)


def test_orelseexp_constructor_exists():
    assert callable(OrElseExp.__init__)


def test_orelseexp_constructor_args():
    sig = inspect.signature(OrElseExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_andalsoexp_is_not_abstract():
    assert not inspect.isabstract(gDSL_AndAlsoExp)


def test_gdsl_andalsoexp_constructor_exists():
    assert callable(gDSL_AndAlsoExp.__init__)


def test_gdsl_andalsoexp_constructor_args():
    sig = inspect.signature(gDSL_AndAlsoExp.__init__)
    params = list(sig.parameters.keys())



def test_closedexp_is_not_abstract():
    assert not inspect.isabstract(ClosedExp)


def test_closedexp_constructor_exists():
    assert callable(ClosedExp.__init__)


def test_closedexp_constructor_args():
    sig = inspect.signature(ClosedExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_orelseexp_is_not_abstract():
    assert not inspect.isabstract(gDSL_OrElseExp)


def test_gdsl_orelseexp_constructor_exists():
    assert callable(gDSL_OrElseExp.__init__)


def test_gdsl_orelseexp_constructor_args():
    sig = inspect.signature(gDSL_OrElseExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_monadicexp_is_not_abstract():
    assert not inspect.isabstract(gDSL_MonadicExp)


def test_gdsl_monadicexp_constructor_exists():
    assert callable(gDSL_MonadicExp.__init__)


def test_gdsl_monadicexp_constructor_args():
    sig = inspect.signature(gDSL_MonadicExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gdsl_monadicexp_has_name():
    assert hasattr(gDSL_MonadicExp, "name")
    descriptor = None
    for klass in gDSL_MonadicExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_caseexp_is_not_abstract():
    assert not inspect.isabstract(CaseExp)


def test_caseexp_constructor_exists():
    assert callable(CaseExp.__init__)


def test_caseexp_constructor_args():
    sig = inspect.signature(CaseExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_pat_is_not_abstract():
    assert not inspect.isabstract(gDSL_PAT)


def test_gdsl_pat_constructor_exists():
    assert callable(gDSL_PAT.__init__)


def test_gdsl_pat_constructor_args():
    sig = inspect.signature(gDSL_PAT.__init__)
    params = list(sig.parameters.keys())
    assert "int" in params, "Missing parameter 'int'"
    assert "bitpat" in params, "Missing parameter 'bitpat'"
    assert "uscore" in params, "Missing parameter 'uscore'"
    assert "id" in params, "Missing parameter 'id'"

def test_gdsl_pat_has_int():
    assert hasattr(gDSL_PAT, "int")
    descriptor = None
    for klass in gDSL_PAT.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)

def test_gdsl_pat_has_bitpat():
    assert hasattr(gDSL_PAT, "bitpat")
    descriptor = None
    for klass in gDSL_PAT.__mro__:
        if "bitpat" in klass.__dict__:
            descriptor = klass.__dict__["bitpat"]
            break
    assert isinstance(descriptor, property)

def test_gdsl_pat_has_uscore():
    assert hasattr(gDSL_PAT, "uscore")
    descriptor = None
    for klass in gDSL_PAT.__mro__:
        if "uscore" in klass.__dict__:
            descriptor = klass.__dict__["uscore"]
            break
    assert isinstance(descriptor, property)

def test_gdsl_pat_has_id():
    assert hasattr(gDSL_PAT, "id")
    descriptor = None
    for klass in gDSL_PAT.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_gdsl_closedexp_is_not_abstract():
    assert not inspect.isabstract(gDSL_ClosedExp)


def test_gdsl_closedexp_constructor_exists():
    assert callable(gDSL_ClosedExp.__init__)


def test_gdsl_closedexp_constructor_args():
    sig = inspect.signature(gDSL_ClosedExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_caseexp_is_not_abstract():
    assert not inspect.isabstract(gDSL_CaseExp)


def test_gdsl_caseexp_constructor_exists():
    assert callable(gDSL_CaseExp.__init__)


def test_gdsl_caseexp_constructor_args():
    sig = inspect.signature(gDSL_CaseExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gdsl_caseexp_has_name():
    assert hasattr(gDSL_CaseExp, "name")
    descriptor = None
    for klass in gDSL_CaseExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gdsl_tyelement_is_not_abstract():
    assert not inspect.isabstract(gDSL_TyElement)


def test_gdsl_tyelement_constructor_exists():
    assert callable(gDSL_TyElement.__init__)


def test_gdsl_tyelement_constructor_args():
    sig = inspect.signature(gDSL_TyElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gdsl_tyelement_has_name():
    assert hasattr(gDSL_TyElement, "name")
    descriptor = None
    for klass in gDSL_TyElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gdsl_tybind_is_not_abstract():
    assert not inspect.isabstract(gDSL_TyBind)


def test_gdsl_tybind_constructor_exists():
    assert callable(gDSL_TyBind.__init__)


def test_gdsl_tybind_constructor_args():
    sig = inspect.signature(gDSL_TyBind.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gdsl_tybind_has_name():
    assert hasattr(gDSL_TyBind, "name")
    descriptor = None
    for klass in gDSL_TyBind.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gdsl_cons_is_not_abstract():
    assert not inspect.isabstract(gDSL_CONS)


def test_gdsl_cons_constructor_exists():
    assert callable(gDSL_CONS.__init__)


def test_gdsl_cons_constructor_args():
    sig = inspect.signature(gDSL_CONS.__init__)
    params = list(sig.parameters.keys())
    assert "conName" in params, "Missing parameter 'conName'"

def test_gdsl_cons_has_conName():
    assert hasattr(gDSL_CONS, "conName")
    descriptor = None
    for klass in gDSL_CONS.__mro__:
        if "conName" in klass.__dict__:
            descriptor = klass.__dict__["conName"]
            break
    assert isinstance(descriptor, property)



def test_gdsl_exp_is_not_abstract():
    assert not inspect.isabstract(gDSL_Exp)


def test_gdsl_exp_constructor_exists():
    assert callable(gDSL_Exp.__init__)


def test_gdsl_exp_constructor_args():
    sig = inspect.signature(gDSL_Exp.__init__)
    params = list(sig.parameters.keys())
    assert "mid" in params, "Missing parameter 'mid'"

def test_gdsl_exp_has_mid():
    assert hasattr(gDSL_Exp, "mid")
    descriptor = None
    for klass in gDSL_Exp.__mro__:
        if "mid" in klass.__dict__:
            descriptor = klass.__dict__["mid"]
            break
    assert isinstance(descriptor, property)



def test_gdsl_ty_is_not_abstract():
    assert not inspect.isabstract(gDSL_Ty)


def test_gdsl_ty_constructor_exists():
    assert callable(gDSL_Ty.__init__)


def test_gdsl_ty_constructor_args():
    sig = inspect.signature(gDSL_Ty.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_gdsl_ty_has_type():
    assert hasattr(gDSL_Ty, "type")
    descriptor = None
    for klass in gDSL_Ty.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_gdsl_ty_has_value():
    assert hasattr(gDSL_Ty, "value")
    descriptor = None
    for klass in gDSL_Ty.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gdsl_tyvars_is_not_abstract():
    assert not inspect.isabstract(gDSL_TyVars)


def test_gdsl_tyvars_constructor_exists():
    assert callable(gDSL_TyVars.__init__)


def test_gdsl_tyvars_constructor_args():
    sig = inspect.signature(gDSL_TyVars.__init__)
    params = list(sig.parameters.keys())



def test_decl_is_not_abstract():
    assert not inspect.isabstract(Decl)


def test_decl_constructor_exists():
    assert callable(Decl.__init__)


def test_decl_constructor_args():
    sig = inspect.signature(Decl.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_type_is_not_abstract():
    assert not inspect.isabstract(gDSL_Type)


def test_gdsl_type_constructor_exists():
    assert callable(gDSL_Type.__init__)


def test_gdsl_type_constructor_args():
    sig = inspect.signature(gDSL_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gdsl_type_has_name():
    assert hasattr(gDSL_Type, "name")
    descriptor = None
    for klass in gDSL_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gdsl_val_is_not_abstract():
    assert not inspect.isabstract(gDSL_Val)


def test_gdsl_val_constructor_exists():
    assert callable(gDSL_Val.__init__)


def test_gdsl_val_constructor_args():
    sig = inspect.signature(gDSL_Val.__init__)
    params = list(sig.parameters.keys())
    assert "attr" in params, "Missing parameter 'attr'"
    assert "mid" in params, "Missing parameter 'mid'"
    assert "name" in params, "Missing parameter 'name'"
    assert "decPat" in params, "Missing parameter 'decPat'"

def test_gdsl_val_has_attr():
    assert hasattr(gDSL_Val, "attr")
    descriptor = None
    for klass in gDSL_Val.__mro__:
        if "attr" in klass.__dict__:
            descriptor = klass.__dict__["attr"]
            break
    assert isinstance(descriptor, property)

def test_gdsl_val_has_mid():
    assert hasattr(gDSL_Val, "mid")
    descriptor = None
    for klass in gDSL_Val.__mro__:
        if "mid" in klass.__dict__:
            descriptor = klass.__dict__["mid"]
            break
    assert isinstance(descriptor, property)

def test_gdsl_val_has_name():
    assert hasattr(gDSL_Val, "name")
    descriptor = None
    for klass in gDSL_Val.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gdsl_val_has_decPat():
    assert hasattr(gDSL_Val, "decPat")
    descriptor = None
    for klass in gDSL_Val.__mro__:
        if "decPat" in klass.__dict__:
            descriptor = klass.__dict__["decPat"]
            break
    assert isinstance(descriptor, property)



def test_gdsl_declexport_is_not_abstract():
    assert not inspect.isabstract(gDSL_DeclExport)


def test_gdsl_declexport_constructor_exists():
    assert callable(gDSL_DeclExport.__init__)


def test_gdsl_declexport_constructor_args():
    sig = inspect.signature(gDSL_DeclExport.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_decl_is_not_abstract():
    assert not inspect.isabstract(gDSL_Decl)


def test_gdsl_decl_constructor_exists():
    assert callable(gDSL_Decl.__init__)


def test_gdsl_decl_constructor_args():
    sig = inspect.signature(gDSL_Decl.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_model_is_not_abstract():
    assert not inspect.isabstract(gDSL_Model)


def test_gdsl_model_constructor_exists():
    assert callable(gDSL_Model.__init__)


def test_gdsl_model_constructor_args():
    sig = inspect.signature(gDSL_Model.__init__)
    params = list(sig.parameters.keys())



def test_gdsl_condecl_is_not_abstract():
    assert not inspect.isabstract(gDSL_ConDecl)


def test_gdsl_condecl_constructor_exists():
    assert callable(gDSL_ConDecl.__init__)


def test_gdsl_condecl_constructor_args():
    sig = inspect.signature(gDSL_ConDecl.__init__)
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
gDSL_ValueDecl_strategy = st.builds(
    gDSL_ValueDecl,
    ids=
        safe_text,
    name=
        safe_text
)
gDSL_Field_strategy = st.builds(
    gDSL_Field,
    name=
        safe_text
)
ApplyExp_strategy = st.builds(
    ApplyExp,
)
gDSL_Args_strategy = st.builds(
    gDSL_Args,
)
gDSL_AtomicExp_strategy = st.builds(
    gDSL_AtomicExp,
    id=
        safe_text
)
SelectExp_strategy = st.builds(
    SelectExp,
)
gDSL_ApplyExp_strategy = st.builds(
    gDSL_ApplyExp,
)
MExp_strategy = st.builds(
    MExp,
)
gDSL_SelectExp_strategy = st.builds(
    gDSL_SelectExp,
    symbol=
        safe_text
)
AExp_strategy = st.builds(
    AExp,
)
gDSL_MExp_strategy = st.builds(
    gDSL_MExp,
    sign=
        safe_text
)
RExp_strategy = st.builds(
    RExp,
)
gDSL_AExp_strategy = st.builds(
    gDSL_AExp,
    sym=
        safe_text
)
AndAlsoExp_strategy = st.builds(
    AndAlsoExp,
)
gDSL_RExp_strategy = st.builds(
    gDSL_RExp,
)
OrElseExp_strategy = st.builds(
    OrElseExp,
)
gDSL_AndAlsoExp_strategy = st.builds(
    gDSL_AndAlsoExp,
)
ClosedExp_strategy = st.builds(
    ClosedExp,
)
gDSL_OrElseExp_strategy = st.builds(
    gDSL_OrElseExp,
)
gDSL_MonadicExp_strategy = st.builds(
    gDSL_MonadicExp,
    name=
        safe_text
)
CaseExp_strategy = st.builds(
    CaseExp,
)
gDSL_PAT_strategy = st.builds(
    gDSL_PAT,
    int=
        safe_text,
    bitpat=
        safe_text,
    uscore=
        safe_text,
    id=
        safe_text
)
gDSL_ClosedExp_strategy = st.builds(
    gDSL_ClosedExp,
)
gDSL_CaseExp_strategy = st.builds(
    gDSL_CaseExp,
    name=
        safe_text
)
gDSL_TyElement_strategy = st.builds(
    gDSL_TyElement,
    name=
        safe_text
)
gDSL_TyBind_strategy = st.builds(
    gDSL_TyBind,
    name=
        safe_text
)
gDSL_CONS_strategy = st.builds(
    gDSL_CONS,
    conName=
        safe_text
)
gDSL_Exp_strategy = st.builds(
    gDSL_Exp,
    mid=
        safe_text
)
gDSL_Ty_strategy = st.builds(
    gDSL_Ty,
    type=
        safe_text,
    value=
        safe_text
)
gDSL_TyVars_strategy = st.builds(
    gDSL_TyVars,
)
Decl_strategy = st.builds(
    Decl,
)
gDSL_Type_strategy = st.builds(
    gDSL_Type,
    name=
        safe_text
)
gDSL_Val_strategy = st.builds(
    gDSL_Val,
    attr=
        safe_text,
    mid=
        safe_text,
    name=
        safe_text,
    decPat=
        safe_text
)
gDSL_DeclExport_strategy = st.builds(
    gDSL_DeclExport,
)
gDSL_Decl_strategy = st.builds(
    gDSL_Decl,
)
gDSL_Model_strategy = st.builds(
    gDSL_Model,
)
gDSL_ConDecl_strategy = st.builds(
    gDSL_ConDecl,
)

@given(instance=gDSL_ValueDecl_strategy)
@settings(max_examples=50)
def test_gdsl_valuedecl_instantiation(instance):
    assert isinstance(instance, gDSL_ValueDecl)



@given(instance=gDSL_ValueDecl_strategy)
def test_gdsl_valuedecl_ids_setter(instance):
    original = instance.ids
    instance.ids = original
    assert instance.ids == original



@given(instance=gDSL_ValueDecl_strategy)
def test_gdsl_valuedecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gDSL_Field_strategy)
@settings(max_examples=50)
def test_gdsl_field_instantiation(instance):
    assert isinstance(instance, gDSL_Field)



@given(instance=gDSL_Field_strategy)
def test_gdsl_field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ApplyExp_strategy)
@settings(max_examples=50)
def test_applyexp_instantiation(instance):
    assert isinstance(instance, ApplyExp)

@given(instance=gDSL_Args_strategy)
@settings(max_examples=50)
def test_gdsl_args_instantiation(instance):
    assert isinstance(instance, gDSL_Args)

@given(instance=gDSL_AtomicExp_strategy)
@settings(max_examples=50)
def test_gdsl_atomicexp_instantiation(instance):
    assert isinstance(instance, gDSL_AtomicExp)



@given(instance=gDSL_AtomicExp_strategy)
def test_gdsl_atomicexp_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=SelectExp_strategy)
@settings(max_examples=50)
def test_selectexp_instantiation(instance):
    assert isinstance(instance, SelectExp)

@given(instance=gDSL_ApplyExp_strategy)
@settings(max_examples=50)
def test_gdsl_applyexp_instantiation(instance):
    assert isinstance(instance, gDSL_ApplyExp)

@given(instance=MExp_strategy)
@settings(max_examples=50)
def test_mexp_instantiation(instance):
    assert isinstance(instance, MExp)

@given(instance=gDSL_SelectExp_strategy)
@settings(max_examples=50)
def test_gdsl_selectexp_instantiation(instance):
    assert isinstance(instance, gDSL_SelectExp)



@given(instance=gDSL_SelectExp_strategy)
def test_gdsl_selectexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=AExp_strategy)
@settings(max_examples=50)
def test_aexp_instantiation(instance):
    assert isinstance(instance, AExp)

@given(instance=gDSL_MExp_strategy)
@settings(max_examples=50)
def test_gdsl_mexp_instantiation(instance):
    assert isinstance(instance, gDSL_MExp)



@given(instance=gDSL_MExp_strategy)
def test_gdsl_mexp_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=RExp_strategy)
@settings(max_examples=50)
def test_rexp_instantiation(instance):
    assert isinstance(instance, RExp)

@given(instance=gDSL_AExp_strategy)
@settings(max_examples=50)
def test_gdsl_aexp_instantiation(instance):
    assert isinstance(instance, gDSL_AExp)



@given(instance=gDSL_AExp_strategy)
def test_gdsl_aexp_sym_setter(instance):
    original = instance.sym
    instance.sym = original
    assert instance.sym == original

@given(instance=AndAlsoExp_strategy)
@settings(max_examples=50)
def test_andalsoexp_instantiation(instance):
    assert isinstance(instance, AndAlsoExp)

@given(instance=gDSL_RExp_strategy)
@settings(max_examples=50)
def test_gdsl_rexp_instantiation(instance):
    assert isinstance(instance, gDSL_RExp)

@given(instance=OrElseExp_strategy)
@settings(max_examples=50)
def test_orelseexp_instantiation(instance):
    assert isinstance(instance, OrElseExp)

@given(instance=gDSL_AndAlsoExp_strategy)
@settings(max_examples=50)
def test_gdsl_andalsoexp_instantiation(instance):
    assert isinstance(instance, gDSL_AndAlsoExp)

@given(instance=ClosedExp_strategy)
@settings(max_examples=50)
def test_closedexp_instantiation(instance):
    assert isinstance(instance, ClosedExp)

@given(instance=gDSL_OrElseExp_strategy)
@settings(max_examples=50)
def test_gdsl_orelseexp_instantiation(instance):
    assert isinstance(instance, gDSL_OrElseExp)

@given(instance=gDSL_MonadicExp_strategy)
@settings(max_examples=50)
def test_gdsl_monadicexp_instantiation(instance):
    assert isinstance(instance, gDSL_MonadicExp)



@given(instance=gDSL_MonadicExp_strategy)
def test_gdsl_monadicexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CaseExp_strategy)
@settings(max_examples=50)
def test_caseexp_instantiation(instance):
    assert isinstance(instance, CaseExp)

@given(instance=gDSL_PAT_strategy)
@settings(max_examples=50)
def test_gdsl_pat_instantiation(instance):
    assert isinstance(instance, gDSL_PAT)



@given(instance=gDSL_PAT_strategy)
def test_gdsl_pat_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original



@given(instance=gDSL_PAT_strategy)
def test_gdsl_pat_bitpat_setter(instance):
    original = instance.bitpat
    instance.bitpat = original
    assert instance.bitpat == original



@given(instance=gDSL_PAT_strategy)
def test_gdsl_pat_uscore_setter(instance):
    original = instance.uscore
    instance.uscore = original
    assert instance.uscore == original



@given(instance=gDSL_PAT_strategy)
def test_gdsl_pat_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=gDSL_ClosedExp_strategy)
@settings(max_examples=50)
def test_gdsl_closedexp_instantiation(instance):
    assert isinstance(instance, gDSL_ClosedExp)

@given(instance=gDSL_CaseExp_strategy)
@settings(max_examples=50)
def test_gdsl_caseexp_instantiation(instance):
    assert isinstance(instance, gDSL_CaseExp)



@given(instance=gDSL_CaseExp_strategy)
def test_gdsl_caseexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gDSL_TyElement_strategy)
@settings(max_examples=50)
def test_gdsl_tyelement_instantiation(instance):
    assert isinstance(instance, gDSL_TyElement)



@given(instance=gDSL_TyElement_strategy)
def test_gdsl_tyelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gDSL_TyBind_strategy)
@settings(max_examples=50)
def test_gdsl_tybind_instantiation(instance):
    assert isinstance(instance, gDSL_TyBind)



@given(instance=gDSL_TyBind_strategy)
def test_gdsl_tybind_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gDSL_CONS_strategy)
@settings(max_examples=50)
def test_gdsl_cons_instantiation(instance):
    assert isinstance(instance, gDSL_CONS)



@given(instance=gDSL_CONS_strategy)
def test_gdsl_cons_conName_setter(instance):
    original = instance.conName
    instance.conName = original
    assert instance.conName == original

@given(instance=gDSL_Exp_strategy)
@settings(max_examples=50)
def test_gdsl_exp_instantiation(instance):
    assert isinstance(instance, gDSL_Exp)



@given(instance=gDSL_Exp_strategy)
def test_gdsl_exp_mid_setter(instance):
    original = instance.mid
    instance.mid = original
    assert instance.mid == original

@given(instance=gDSL_Ty_strategy)
@settings(max_examples=50)
def test_gdsl_ty_instantiation(instance):
    assert isinstance(instance, gDSL_Ty)



@given(instance=gDSL_Ty_strategy)
def test_gdsl_ty_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=gDSL_Ty_strategy)
def test_gdsl_ty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gDSL_TyVars_strategy)
@settings(max_examples=50)
def test_gdsl_tyvars_instantiation(instance):
    assert isinstance(instance, gDSL_TyVars)

@given(instance=Decl_strategy)
@settings(max_examples=50)
def test_decl_instantiation(instance):
    assert isinstance(instance, Decl)

@given(instance=gDSL_Type_strategy)
@settings(max_examples=50)
def test_gdsl_type_instantiation(instance):
    assert isinstance(instance, gDSL_Type)



@given(instance=gDSL_Type_strategy)
def test_gdsl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gDSL_Val_strategy)
@settings(max_examples=50)
def test_gdsl_val_instantiation(instance):
    assert isinstance(instance, gDSL_Val)



@given(instance=gDSL_Val_strategy)
def test_gdsl_val_attr_setter(instance):
    original = instance.attr
    instance.attr = original
    assert instance.attr == original



@given(instance=gDSL_Val_strategy)
def test_gdsl_val_mid_setter(instance):
    original = instance.mid
    instance.mid = original
    assert instance.mid == original



@given(instance=gDSL_Val_strategy)
def test_gdsl_val_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=gDSL_Val_strategy)
def test_gdsl_val_decPat_setter(instance):
    original = instance.decPat
    instance.decPat = original
    assert instance.decPat == original

@given(instance=gDSL_DeclExport_strategy)
@settings(max_examples=50)
def test_gdsl_declexport_instantiation(instance):
    assert isinstance(instance, gDSL_DeclExport)

@given(instance=gDSL_Decl_strategy)
@settings(max_examples=50)
def test_gdsl_decl_instantiation(instance):
    assert isinstance(instance, gDSL_Decl)

@given(instance=gDSL_Model_strategy)
@settings(max_examples=50)
def test_gdsl_model_instantiation(instance):
    assert isinstance(instance, gDSL_Model)

@given(instance=gDSL_ConDecl_strategy)
@settings(max_examples=50)
def test_gdsl_condecl_instantiation(instance):
    assert isinstance(instance, gDSL_ConDecl)
