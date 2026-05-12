import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TopLevelCmd,
    boa_Expr,
    EvalFunRes,
    boa_EvalBoundFunRes,
    EvalRes,
    boa_EvalBoolRes,
    boa_EvalFunRes,
    boa_EvalMapRes,
    boa_EvalIntRes,
    CmpOp,
    boa_CmpOpUnequal,
    boa_CmpOpEqual,
    BoolOp,
    boa_BoolOpOr,
    boa_BoolOpAnd,
    ArithOp,
    boa_ArithOpRemainder,
    boa_ArithOpMinus,
    boa_ArithOpTimes,
    boa_ArithOpDivide,
    boa_ArithOpPlus,
    boa_EvalRes,
    boa_StringToEvalResMap,
    boa_Ctx,
    boa_CmpOpLess,
    boa_Field,
    Expr,
    boa_Not,
    boa_Var,
    boa_Let,
    boa_Seq,
    boa_Int,
    boa_Project,
    boa_This,
    boa_Bool,
    boa_CmpOp,
    boa_BoolOp,
    boa_Fun,
    boa_If,
    boa_Skip,
    boa_Assign,
    boa_BObject,
    boa_Copy,
    boa_App,
    boa_ArithOp,
    boa_Def,
    boa_With,
    boa_TopLevelCmd,
    boa_File,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_toplevelcmd_is_not_abstract():
    assert not inspect.isabstract(TopLevelCmd)


def test_toplevelcmd_constructor_exists():
    assert callable(TopLevelCmd.__init__)


def test_toplevelcmd_constructor_args():
    sig = inspect.signature(TopLevelCmd.__init__)
    params = list(sig.parameters.keys())



def test_boa_expr_is_not_abstract():
    assert not inspect.isabstract(boa_Expr)


def test_boa_expr_constructor_exists():
    assert callable(boa_Expr.__init__)


def test_boa_expr_constructor_args():
    sig = inspect.signature(boa_Expr.__init__)
    params = list(sig.parameters.keys())



def test_evalfunres_is_not_abstract():
    assert not inspect.isabstract(EvalFunRes)


def test_evalfunres_constructor_exists():
    assert callable(EvalFunRes.__init__)


def test_evalfunres_constructor_args():
    sig = inspect.signature(EvalFunRes.__init__)
    params = list(sig.parameters.keys())



def test_boa_evalboundfunres_is_not_abstract():
    assert not inspect.isabstract(boa_EvalBoundFunRes)


def test_boa_evalboundfunres_constructor_exists():
    assert callable(boa_EvalBoundFunRes.__init__)


def test_boa_evalboundfunres_constructor_args():
    sig = inspect.signature(boa_EvalBoundFunRes.__init__)
    params = list(sig.parameters.keys())



def test_evalres_is_not_abstract():
    assert not inspect.isabstract(EvalRes)


def test_evalres_constructor_exists():
    assert callable(EvalRes.__init__)


def test_evalres_constructor_args():
    sig = inspect.signature(EvalRes.__init__)
    params = list(sig.parameters.keys())



def test_boa_evalboolres_is_not_abstract():
    assert not inspect.isabstract(boa_EvalBoolRes)


def test_boa_evalboolres_constructor_exists():
    assert callable(boa_EvalBoolRes.__init__)


def test_boa_evalboolres_constructor_args():
    sig = inspect.signature(boa_EvalBoolRes.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_boa_evalboolres_has_value():
    assert hasattr(boa_EvalBoolRes, "value")
    descriptor = None
    for klass in boa_EvalBoolRes.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_boa_evalfunres_is_not_abstract():
    assert not inspect.isabstract(boa_EvalFunRes)


def test_boa_evalfunres_constructor_exists():
    assert callable(boa_EvalFunRes.__init__)


def test_boa_evalfunres_constructor_args():
    sig = inspect.signature(boa_EvalFunRes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa_evalfunres_has_name():
    assert hasattr(boa_EvalFunRes, "name")
    descriptor = None
    for klass in boa_EvalFunRes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_boa_evalmapres_is_not_abstract():
    assert not inspect.isabstract(boa_EvalMapRes)


def test_boa_evalmapres_constructor_exists():
    assert callable(boa_EvalMapRes.__init__)


def test_boa_evalmapres_constructor_args():
    sig = inspect.signature(boa_EvalMapRes.__init__)
    params = list(sig.parameters.keys())



def test_boa_evalintres_is_not_abstract():
    assert not inspect.isabstract(boa_EvalIntRes)


def test_boa_evalintres_constructor_exists():
    assert callable(boa_EvalIntRes.__init__)


def test_boa_evalintres_constructor_args():
    sig = inspect.signature(boa_EvalIntRes.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_boa_evalintres_has_value():
    assert hasattr(boa_EvalIntRes, "value")
    descriptor = None
    for klass in boa_EvalIntRes.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cmpop_is_not_abstract():
    assert not inspect.isabstract(CmpOp)


def test_cmpop_constructor_exists():
    assert callable(CmpOp.__init__)


def test_cmpop_constructor_args():
    sig = inspect.signature(CmpOp.__init__)
    params = list(sig.parameters.keys())



def test_boa_cmpopunequal_is_not_abstract():
    assert not inspect.isabstract(boa_CmpOpUnequal)


def test_boa_cmpopunequal_constructor_exists():
    assert callable(boa_CmpOpUnequal.__init__)


def test_boa_cmpopunequal_constructor_args():
    sig = inspect.signature(boa_CmpOpUnequal.__init__)
    params = list(sig.parameters.keys())



def test_boa_cmpopequal_is_not_abstract():
    assert not inspect.isabstract(boa_CmpOpEqual)


def test_boa_cmpopequal_constructor_exists():
    assert callable(boa_CmpOpEqual.__init__)


def test_boa_cmpopequal_constructor_args():
    sig = inspect.signature(boa_CmpOpEqual.__init__)
    params = list(sig.parameters.keys())



def test_boolop_is_not_abstract():
    assert not inspect.isabstract(BoolOp)


def test_boolop_constructor_exists():
    assert callable(BoolOp.__init__)


def test_boolop_constructor_args():
    sig = inspect.signature(BoolOp.__init__)
    params = list(sig.parameters.keys())



def test_boa_boolopor_is_not_abstract():
    assert not inspect.isabstract(boa_BoolOpOr)


def test_boa_boolopor_constructor_exists():
    assert callable(boa_BoolOpOr.__init__)


def test_boa_boolopor_constructor_args():
    sig = inspect.signature(boa_BoolOpOr.__init__)
    params = list(sig.parameters.keys())



def test_boa_boolopand_is_not_abstract():
    assert not inspect.isabstract(boa_BoolOpAnd)


def test_boa_boolopand_constructor_exists():
    assert callable(boa_BoolOpAnd.__init__)


def test_boa_boolopand_constructor_args():
    sig = inspect.signature(boa_BoolOpAnd.__init__)
    params = list(sig.parameters.keys())



def test_arithop_is_not_abstract():
    assert not inspect.isabstract(ArithOp)


def test_arithop_constructor_exists():
    assert callable(ArithOp.__init__)


def test_arithop_constructor_args():
    sig = inspect.signature(ArithOp.__init__)
    params = list(sig.parameters.keys())



def test_boa_arithopremainder_is_not_abstract():
    assert not inspect.isabstract(boa_ArithOpRemainder)


def test_boa_arithopremainder_constructor_exists():
    assert callable(boa_ArithOpRemainder.__init__)


def test_boa_arithopremainder_constructor_args():
    sig = inspect.signature(boa_ArithOpRemainder.__init__)
    params = list(sig.parameters.keys())



def test_boa_arithopminus_is_not_abstract():
    assert not inspect.isabstract(boa_ArithOpMinus)


def test_boa_arithopminus_constructor_exists():
    assert callable(boa_ArithOpMinus.__init__)


def test_boa_arithopminus_constructor_args():
    sig = inspect.signature(boa_ArithOpMinus.__init__)
    params = list(sig.parameters.keys())



def test_boa_arithoptimes_is_not_abstract():
    assert not inspect.isabstract(boa_ArithOpTimes)


def test_boa_arithoptimes_constructor_exists():
    assert callable(boa_ArithOpTimes.__init__)


def test_boa_arithoptimes_constructor_args():
    sig = inspect.signature(boa_ArithOpTimes.__init__)
    params = list(sig.parameters.keys())



def test_boa_arithopdivide_is_not_abstract():
    assert not inspect.isabstract(boa_ArithOpDivide)


def test_boa_arithopdivide_constructor_exists():
    assert callable(boa_ArithOpDivide.__init__)


def test_boa_arithopdivide_constructor_args():
    sig = inspect.signature(boa_ArithOpDivide.__init__)
    params = list(sig.parameters.keys())



def test_boa_arithopplus_is_not_abstract():
    assert not inspect.isabstract(boa_ArithOpPlus)


def test_boa_arithopplus_constructor_exists():
    assert callable(boa_ArithOpPlus.__init__)


def test_boa_arithopplus_constructor_args():
    sig = inspect.signature(boa_ArithOpPlus.__init__)
    params = list(sig.parameters.keys())



def test_boa_evalres_is_not_abstract():
    assert not inspect.isabstract(boa_EvalRes)


def test_boa_evalres_constructor_exists():
    assert callable(boa_EvalRes.__init__)


def test_boa_evalres_constructor_args():
    sig = inspect.signature(boa_EvalRes.__init__)
    params = list(sig.parameters.keys())



def test_boa_stringtoevalresmap_is_not_abstract():
    assert not inspect.isabstract(boa_StringToEvalResMap)


def test_boa_stringtoevalresmap_constructor_exists():
    assert callable(boa_StringToEvalResMap.__init__)


def test_boa_stringtoevalresmap_constructor_args():
    sig = inspect.signature(boa_StringToEvalResMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_boa_stringtoevalresmap_has_key():
    assert hasattr(boa_StringToEvalResMap, "key")
    descriptor = None
    for klass in boa_StringToEvalResMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_boa_ctx_is_not_abstract():
    assert not inspect.isabstract(boa_Ctx)


def test_boa_ctx_constructor_exists():
    assert callable(boa_Ctx.__init__)


def test_boa_ctx_constructor_args():
    sig = inspect.signature(boa_Ctx.__init__)
    params = list(sig.parameters.keys())



def test_boa_cmpopless_is_not_abstract():
    assert not inspect.isabstract(boa_CmpOpLess)


def test_boa_cmpopless_constructor_exists():
    assert callable(boa_CmpOpLess.__init__)


def test_boa_cmpopless_constructor_args():
    sig = inspect.signature(boa_CmpOpLess.__init__)
    params = list(sig.parameters.keys())



def test_boa_field_is_not_abstract():
    assert not inspect.isabstract(boa_Field)


def test_boa_field_constructor_exists():
    assert callable(boa_Field.__init__)


def test_boa_field_constructor_args():
    sig = inspect.signature(boa_Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa_field_has_name():
    assert hasattr(boa_Field, "name")
    descriptor = None
    for klass in boa_Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_boa_not_is_not_abstract():
    assert not inspect.isabstract(boa_Not)


def test_boa_not_constructor_exists():
    assert callable(boa_Not.__init__)


def test_boa_not_constructor_args():
    sig = inspect.signature(boa_Not.__init__)
    params = list(sig.parameters.keys())



def test_boa_var_is_not_abstract():
    assert not inspect.isabstract(boa_Var)


def test_boa_var_constructor_exists():
    assert callable(boa_Var.__init__)


def test_boa_var_constructor_args():
    sig = inspect.signature(boa_Var.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa_var_has_name():
    assert hasattr(boa_Var, "name")
    descriptor = None
    for klass in boa_Var.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_boa_let_is_not_abstract():
    assert not inspect.isabstract(boa_Let)


def test_boa_let_constructor_exists():
    assert callable(boa_Let.__init__)


def test_boa_let_constructor_args():
    sig = inspect.signature(boa_Let.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa_let_has_name():
    assert hasattr(boa_Let, "name")
    descriptor = None
    for klass in boa_Let.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_boa_seq_is_not_abstract():
    assert not inspect.isabstract(boa_Seq)


def test_boa_seq_constructor_exists():
    assert callable(boa_Seq.__init__)


def test_boa_seq_constructor_args():
    sig = inspect.signature(boa_Seq.__init__)
    params = list(sig.parameters.keys())



def test_boa_int_is_not_abstract():
    assert not inspect.isabstract(boa_Int)


def test_boa_int_constructor_exists():
    assert callable(boa_Int.__init__)


def test_boa_int_constructor_args():
    sig = inspect.signature(boa_Int.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_boa_int_has_value():
    assert hasattr(boa_Int, "value")
    descriptor = None
    for klass in boa_Int.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_boa_project_is_not_abstract():
    assert not inspect.isabstract(boa_Project)


def test_boa_project_constructor_exists():
    assert callable(boa_Project.__init__)


def test_boa_project_constructor_args():
    sig = inspect.signature(boa_Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa_project_has_name():
    assert hasattr(boa_Project, "name")
    descriptor = None
    for klass in boa_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_boa_this_is_not_abstract():
    assert not inspect.isabstract(boa_This)


def test_boa_this_constructor_exists():
    assert callable(boa_This.__init__)


def test_boa_this_constructor_args():
    sig = inspect.signature(boa_This.__init__)
    params = list(sig.parameters.keys())



def test_boa_bool_is_not_abstract():
    assert not inspect.isabstract(boa_Bool)


def test_boa_bool_constructor_exists():
    assert callable(boa_Bool.__init__)


def test_boa_bool_constructor_args():
    sig = inspect.signature(boa_Bool.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_boa_bool_has_value():
    assert hasattr(boa_Bool, "value")
    descriptor = None
    for klass in boa_Bool.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_boa_cmpop_is_not_abstract():
    assert not inspect.isabstract(boa_CmpOp)


def test_boa_cmpop_constructor_exists():
    assert callable(boa_CmpOp.__init__)


def test_boa_cmpop_constructor_args():
    sig = inspect.signature(boa_CmpOp.__init__)
    params = list(sig.parameters.keys())



def test_boa_boolop_is_not_abstract():
    assert not inspect.isabstract(boa_BoolOp)


def test_boa_boolop_constructor_exists():
    assert callable(boa_BoolOp.__init__)


def test_boa_boolop_constructor_args():
    sig = inspect.signature(boa_BoolOp.__init__)
    params = list(sig.parameters.keys())



def test_boa_fun_is_not_abstract():
    assert not inspect.isabstract(boa_Fun)


def test_boa_fun_constructor_exists():
    assert callable(boa_Fun.__init__)


def test_boa_fun_constructor_args():
    sig = inspect.signature(boa_Fun.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa_fun_has_name():
    assert hasattr(boa_Fun, "name")
    descriptor = None
    for klass in boa_Fun.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_boa_if_is_not_abstract():
    assert not inspect.isabstract(boa_If)


def test_boa_if_constructor_exists():
    assert callable(boa_If.__init__)


def test_boa_if_constructor_args():
    sig = inspect.signature(boa_If.__init__)
    params = list(sig.parameters.keys())



def test_boa_skip_is_not_abstract():
    assert not inspect.isabstract(boa_Skip)


def test_boa_skip_constructor_exists():
    assert callable(boa_Skip.__init__)


def test_boa_skip_constructor_args():
    sig = inspect.signature(boa_Skip.__init__)
    params = list(sig.parameters.keys())



def test_boa_assign_is_not_abstract():
    assert not inspect.isabstract(boa_Assign)


def test_boa_assign_constructor_exists():
    assert callable(boa_Assign.__init__)


def test_boa_assign_constructor_args():
    sig = inspect.signature(boa_Assign.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa_assign_has_name():
    assert hasattr(boa_Assign, "name")
    descriptor = None
    for klass in boa_Assign.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_boa_bobject_is_not_abstract():
    assert not inspect.isabstract(boa_BObject)


def test_boa_bobject_constructor_exists():
    assert callable(boa_BObject.__init__)


def test_boa_bobject_constructor_args():
    sig = inspect.signature(boa_BObject.__init__)
    params = list(sig.parameters.keys())



def test_boa_copy_is_not_abstract():
    assert not inspect.isabstract(boa_Copy)


def test_boa_copy_constructor_exists():
    assert callable(boa_Copy.__init__)


def test_boa_copy_constructor_args():
    sig = inspect.signature(boa_Copy.__init__)
    params = list(sig.parameters.keys())



def test_boa_app_is_not_abstract():
    assert not inspect.isabstract(boa_App)


def test_boa_app_constructor_exists():
    assert callable(boa_App.__init__)


def test_boa_app_constructor_args():
    sig = inspect.signature(boa_App.__init__)
    params = list(sig.parameters.keys())



def test_boa_arithop_is_not_abstract():
    assert not inspect.isabstract(boa_ArithOp)


def test_boa_arithop_constructor_exists():
    assert callable(boa_ArithOp.__init__)


def test_boa_arithop_constructor_args():
    sig = inspect.signature(boa_ArithOp.__init__)
    params = list(sig.parameters.keys())



def test_boa_def_is_not_abstract():
    assert not inspect.isabstract(boa_Def)


def test_boa_def_constructor_exists():
    assert callable(boa_Def.__init__)


def test_boa_def_constructor_args():
    sig = inspect.signature(boa_Def.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa_def_has_name():
    assert hasattr(boa_Def, "name")
    descriptor = None
    for klass in boa_Def.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_boa_with_is_not_abstract():
    assert not inspect.isabstract(boa_With)


def test_boa_with_constructor_exists():
    assert callable(boa_With.__init__)


def test_boa_with_constructor_args():
    sig = inspect.signature(boa_With.__init__)
    params = list(sig.parameters.keys())



def test_boa_toplevelcmd_is_not_abstract():
    assert not inspect.isabstract(boa_TopLevelCmd)


def test_boa_toplevelcmd_constructor_exists():
    assert callable(boa_TopLevelCmd.__init__)


def test_boa_toplevelcmd_constructor_args():
    sig = inspect.signature(boa_TopLevelCmd.__init__)
    params = list(sig.parameters.keys())



def test_boa_file_is_not_abstract():
    assert not inspect.isabstract(boa_File)


def test_boa_file_constructor_exists():
    assert callable(boa_File.__init__)


def test_boa_file_constructor_args():
    sig = inspect.signature(boa_File.__init__)
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
TopLevelCmd_strategy = st.builds(
    TopLevelCmd,
)
boa_Expr_strategy = st.builds(
    boa_Expr,
)
EvalFunRes_strategy = st.builds(
    EvalFunRes,
)
boa_EvalBoundFunRes_strategy = st.builds(
    boa_EvalBoundFunRes,
)
EvalRes_strategy = st.builds(
    EvalRes,
)
boa_EvalBoolRes_strategy = st.builds(
    boa_EvalBoolRes,
    value=
        st.booleans()
)
boa_EvalFunRes_strategy = st.builds(
    boa_EvalFunRes,
    name=
        safe_text
)
boa_EvalMapRes_strategy = st.builds(
    boa_EvalMapRes,
)
boa_EvalIntRes_strategy = st.builds(
    boa_EvalIntRes,
    value=
        st.integers()
)
CmpOp_strategy = st.builds(
    CmpOp,
)
boa_CmpOpUnequal_strategy = st.builds(
    boa_CmpOpUnequal,
)
boa_CmpOpEqual_strategy = st.builds(
    boa_CmpOpEqual,
)
BoolOp_strategy = st.builds(
    BoolOp,
)
boa_BoolOpOr_strategy = st.builds(
    boa_BoolOpOr,
)
boa_BoolOpAnd_strategy = st.builds(
    boa_BoolOpAnd,
)
ArithOp_strategy = st.builds(
    ArithOp,
)
boa_ArithOpRemainder_strategy = st.builds(
    boa_ArithOpRemainder,
)
boa_ArithOpMinus_strategy = st.builds(
    boa_ArithOpMinus,
)
boa_ArithOpTimes_strategy = st.builds(
    boa_ArithOpTimes,
)
boa_ArithOpDivide_strategy = st.builds(
    boa_ArithOpDivide,
)
boa_ArithOpPlus_strategy = st.builds(
    boa_ArithOpPlus,
)
boa_EvalRes_strategy = st.builds(
    boa_EvalRes,
)
boa_StringToEvalResMap_strategy = st.builds(
    boa_StringToEvalResMap,
    key=
        safe_text
)
boa_Ctx_strategy = st.builds(
    boa_Ctx,
)
boa_CmpOpLess_strategy = st.builds(
    boa_CmpOpLess,
)
boa_Field_strategy = st.builds(
    boa_Field,
    name=
        safe_text
)
Expr_strategy = st.builds(
    Expr,
)
boa_Not_strategy = st.builds(
    boa_Not,
)
boa_Var_strategy = st.builds(
    boa_Var,
    name=
        safe_text
)
boa_Let_strategy = st.builds(
    boa_Let,
    name=
        safe_text
)
boa_Seq_strategy = st.builds(
    boa_Seq,
)
boa_Int_strategy = st.builds(
    boa_Int,
    value=
        st.integers()
)
boa_Project_strategy = st.builds(
    boa_Project,
    name=
        safe_text
)
boa_This_strategy = st.builds(
    boa_This,
)
boa_Bool_strategy = st.builds(
    boa_Bool,
    value=
        st.booleans()
)
boa_CmpOp_strategy = st.builds(
    boa_CmpOp,
)
boa_BoolOp_strategy = st.builds(
    boa_BoolOp,
)
boa_Fun_strategy = st.builds(
    boa_Fun,
    name=
        safe_text
)
boa_If_strategy = st.builds(
    boa_If,
)
boa_Skip_strategy = st.builds(
    boa_Skip,
)
boa_Assign_strategy = st.builds(
    boa_Assign,
    name=
        safe_text
)
boa_BObject_strategy = st.builds(
    boa_BObject,
)
boa_Copy_strategy = st.builds(
    boa_Copy,
)
boa_App_strategy = st.builds(
    boa_App,
)
boa_ArithOp_strategy = st.builds(
    boa_ArithOp,
)
boa_Def_strategy = st.builds(
    boa_Def,
    name=
        safe_text
)
boa_With_strategy = st.builds(
    boa_With,
)
boa_TopLevelCmd_strategy = st.builds(
    boa_TopLevelCmd,
)
boa_File_strategy = st.builds(
    boa_File,
)

@given(instance=TopLevelCmd_strategy)
@settings(max_examples=50)
def test_toplevelcmd_instantiation(instance):
    assert isinstance(instance, TopLevelCmd)

@given(instance=boa_Expr_strategy)
@settings(max_examples=50)
def test_boa_expr_instantiation(instance):
    assert isinstance(instance, boa_Expr)

@given(instance=EvalFunRes_strategy)
@settings(max_examples=50)
def test_evalfunres_instantiation(instance):
    assert isinstance(instance, EvalFunRes)

@given(instance=boa_EvalBoundFunRes_strategy)
@settings(max_examples=50)
def test_boa_evalboundfunres_instantiation(instance):
    assert isinstance(instance, boa_EvalBoundFunRes)

@given(instance=EvalRes_strategy)
@settings(max_examples=50)
def test_evalres_instantiation(instance):
    assert isinstance(instance, EvalRes)

@given(instance=boa_EvalBoolRes_strategy)
@settings(max_examples=50)
def test_boa_evalboolres_instantiation(instance):
    assert isinstance(instance, boa_EvalBoolRes)



@given(instance=boa_EvalBoolRes_strategy)
def test_boa_evalboolres_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=boa_EvalFunRes_strategy)
@settings(max_examples=50)
def test_boa_evalfunres_instantiation(instance):
    assert isinstance(instance, boa_EvalFunRes)



@given(instance=boa_EvalFunRes_strategy)
def test_boa_evalfunres_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=boa_EvalMapRes_strategy)
@settings(max_examples=50)
def test_boa_evalmapres_instantiation(instance):
    assert isinstance(instance, boa_EvalMapRes)

@given(instance=boa_EvalIntRes_strategy)
@settings(max_examples=50)
def test_boa_evalintres_instantiation(instance):
    assert isinstance(instance, boa_EvalIntRes)



@given(instance=boa_EvalIntRes_strategy)
def test_boa_evalintres_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=CmpOp_strategy)
@settings(max_examples=50)
def test_cmpop_instantiation(instance):
    assert isinstance(instance, CmpOp)

@given(instance=boa_CmpOpUnequal_strategy)
@settings(max_examples=50)
def test_boa_cmpopunequal_instantiation(instance):
    assert isinstance(instance, boa_CmpOpUnequal)

@given(instance=boa_CmpOpEqual_strategy)
@settings(max_examples=50)
def test_boa_cmpopequal_instantiation(instance):
    assert isinstance(instance, boa_CmpOpEqual)

@given(instance=BoolOp_strategy)
@settings(max_examples=50)
def test_boolop_instantiation(instance):
    assert isinstance(instance, BoolOp)

@given(instance=boa_BoolOpOr_strategy)
@settings(max_examples=50)
def test_boa_boolopor_instantiation(instance):
    assert isinstance(instance, boa_BoolOpOr)

@given(instance=boa_BoolOpAnd_strategy)
@settings(max_examples=50)
def test_boa_boolopand_instantiation(instance):
    assert isinstance(instance, boa_BoolOpAnd)

@given(instance=ArithOp_strategy)
@settings(max_examples=50)
def test_arithop_instantiation(instance):
    assert isinstance(instance, ArithOp)

@given(instance=boa_ArithOpRemainder_strategy)
@settings(max_examples=50)
def test_boa_arithopremainder_instantiation(instance):
    assert isinstance(instance, boa_ArithOpRemainder)

@given(instance=boa_ArithOpMinus_strategy)
@settings(max_examples=50)
def test_boa_arithopminus_instantiation(instance):
    assert isinstance(instance, boa_ArithOpMinus)

@given(instance=boa_ArithOpTimes_strategy)
@settings(max_examples=50)
def test_boa_arithoptimes_instantiation(instance):
    assert isinstance(instance, boa_ArithOpTimes)

@given(instance=boa_ArithOpDivide_strategy)
@settings(max_examples=50)
def test_boa_arithopdivide_instantiation(instance):
    assert isinstance(instance, boa_ArithOpDivide)

@given(instance=boa_ArithOpPlus_strategy)
@settings(max_examples=50)
def test_boa_arithopplus_instantiation(instance):
    assert isinstance(instance, boa_ArithOpPlus)

@given(instance=boa_EvalRes_strategy)
@settings(max_examples=50)
def test_boa_evalres_instantiation(instance):
    assert isinstance(instance, boa_EvalRes)

@given(instance=boa_StringToEvalResMap_strategy)
@settings(max_examples=50)
def test_boa_stringtoevalresmap_instantiation(instance):
    assert isinstance(instance, boa_StringToEvalResMap)



@given(instance=boa_StringToEvalResMap_strategy)
def test_boa_stringtoevalresmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=boa_Ctx_strategy)
@settings(max_examples=50)
def test_boa_ctx_instantiation(instance):
    assert isinstance(instance, boa_Ctx)

@given(instance=boa_CmpOpLess_strategy)
@settings(max_examples=50)
def test_boa_cmpopless_instantiation(instance):
    assert isinstance(instance, boa_CmpOpLess)

@given(instance=boa_Field_strategy)
@settings(max_examples=50)
def test_boa_field_instantiation(instance):
    assert isinstance(instance, boa_Field)



@given(instance=boa_Field_strategy)
def test_boa_field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=boa_Not_strategy)
@settings(max_examples=50)
def test_boa_not_instantiation(instance):
    assert isinstance(instance, boa_Not)

@given(instance=boa_Var_strategy)
@settings(max_examples=50)
def test_boa_var_instantiation(instance):
    assert isinstance(instance, boa_Var)



@given(instance=boa_Var_strategy)
def test_boa_var_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=boa_Let_strategy)
@settings(max_examples=50)
def test_boa_let_instantiation(instance):
    assert isinstance(instance, boa_Let)



@given(instance=boa_Let_strategy)
def test_boa_let_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=boa_Seq_strategy)
@settings(max_examples=50)
def test_boa_seq_instantiation(instance):
    assert isinstance(instance, boa_Seq)

@given(instance=boa_Int_strategy)
@settings(max_examples=50)
def test_boa_int_instantiation(instance):
    assert isinstance(instance, boa_Int)



@given(instance=boa_Int_strategy)
def test_boa_int_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=boa_Project_strategy)
@settings(max_examples=50)
def test_boa_project_instantiation(instance):
    assert isinstance(instance, boa_Project)



@given(instance=boa_Project_strategy)
def test_boa_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=boa_This_strategy)
@settings(max_examples=50)
def test_boa_this_instantiation(instance):
    assert isinstance(instance, boa_This)

@given(instance=boa_Bool_strategy)
@settings(max_examples=50)
def test_boa_bool_instantiation(instance):
    assert isinstance(instance, boa_Bool)



@given(instance=boa_Bool_strategy)
def test_boa_bool_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=boa_CmpOp_strategy)
@settings(max_examples=50)
def test_boa_cmpop_instantiation(instance):
    assert isinstance(instance, boa_CmpOp)

@given(instance=boa_BoolOp_strategy)
@settings(max_examples=50)
def test_boa_boolop_instantiation(instance):
    assert isinstance(instance, boa_BoolOp)

@given(instance=boa_Fun_strategy)
@settings(max_examples=50)
def test_boa_fun_instantiation(instance):
    assert isinstance(instance, boa_Fun)



@given(instance=boa_Fun_strategy)
def test_boa_fun_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=boa_If_strategy)
@settings(max_examples=50)
def test_boa_if_instantiation(instance):
    assert isinstance(instance, boa_If)

@given(instance=boa_Skip_strategy)
@settings(max_examples=50)
def test_boa_skip_instantiation(instance):
    assert isinstance(instance, boa_Skip)

@given(instance=boa_Assign_strategy)
@settings(max_examples=50)
def test_boa_assign_instantiation(instance):
    assert isinstance(instance, boa_Assign)



@given(instance=boa_Assign_strategy)
def test_boa_assign_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=boa_BObject_strategy)
@settings(max_examples=50)
def test_boa_bobject_instantiation(instance):
    assert isinstance(instance, boa_BObject)

@given(instance=boa_Copy_strategy)
@settings(max_examples=50)
def test_boa_copy_instantiation(instance):
    assert isinstance(instance, boa_Copy)

@given(instance=boa_App_strategy)
@settings(max_examples=50)
def test_boa_app_instantiation(instance):
    assert isinstance(instance, boa_App)

@given(instance=boa_ArithOp_strategy)
@settings(max_examples=50)
def test_boa_arithop_instantiation(instance):
    assert isinstance(instance, boa_ArithOp)

@given(instance=boa_Def_strategy)
@settings(max_examples=50)
def test_boa_def_instantiation(instance):
    assert isinstance(instance, boa_Def)



@given(instance=boa_Def_strategy)
def test_boa_def_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=boa_With_strategy)
@settings(max_examples=50)
def test_boa_with_instantiation(instance):
    assert isinstance(instance, boa_With)

@given(instance=boa_TopLevelCmd_strategy)
@settings(max_examples=50)
def test_boa_toplevelcmd_instantiation(instance):
    assert isinstance(instance, boa_TopLevelCmd)

@given(instance=boa_File_strategy)
@settings(max_examples=50)
def test_boa_file_instantiation(instance):
    assert isinstance(instance, boa_File)
