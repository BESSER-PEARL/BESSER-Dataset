import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EvalRes,
    boa::EvalFunRes,
    boa::EvalMapRes,
    boa::EvalRes,
    boa::StringToEvalResMap,
    boa::EvalBoolRes,
    boa::EvalIntRes,
    EvalFunRes,
    boa::EvalBoundFunRes,
    BoolOp,
    boa::BoolOpAnd,
    ArithOp,
    boa::ArithOpDivide,
    boa::ArithOpTimes,
    boa::ArithOpMinus,
    boa::ArithOpRemainder,
    boa::ArithOpPlus,
    boa::Ctx,
    CmpOp,
    boa::CmpOpLess,
    boa::CmpOpUnequal,
    boa::CmpOpEqual,
    boa::BoolOpOr,
    boa::Field,
    Expr,
    boa::BoolOp,
    boa::Not,
    boa::ArithOp,
    boa::Fun,
    boa::Var,
    boa::Assign,
    boa::Copy,
    boa::CmpOp,
    boa::Let,
    boa::If,
    boa::With,
    boa::BObject,
    boa::Seq,
    boa::App,
    TopLevelCmd,
    boa::Def,
    boa::Expr,
    boa::Project,
    boa::TopLevelCmd,
    boa::Skip,
    boa::Int,
    boa::Bool,
    boa::This,
    boa::File,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_evalres_is_not_abstract():
    assert not inspect.isabstract(EvalRes)


def test_evalres_constructor_exists():
    assert callable(EvalRes.__init__)


def test_evalres_constructor_args():
    sig = inspect.signature(EvalRes.__init__)
    params = list(sig.parameters.keys())



def test_boa::evalfunres_is_not_abstract():
    assert not inspect.isabstract(boa::EvalFunRes)


def test_boa::evalfunres_constructor_exists():
    assert callable(boa::EvalFunRes.__init__)


def test_boa::evalfunres_constructor_args():
    sig = inspect.signature(boa::EvalFunRes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa::evalfunres_has_name():
    assert hasattr(boa::EvalFunRes, "name")
    descriptor = None
    for klass in boa::EvalFunRes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_boa::evalmapres_is_not_abstract():
    assert not inspect.isabstract(boa::EvalMapRes)


def test_boa::evalmapres_constructor_exists():
    assert callable(boa::EvalMapRes.__init__)


def test_boa::evalmapres_constructor_args():
    sig = inspect.signature(boa::EvalMapRes.__init__)
    params = list(sig.parameters.keys())



def test_boa::evalres_is_not_abstract():
    assert not inspect.isabstract(boa::EvalRes)


def test_boa::evalres_constructor_exists():
    assert callable(boa::EvalRes.__init__)


def test_boa::evalres_constructor_args():
    sig = inspect.signature(boa::EvalRes.__init__)
    params = list(sig.parameters.keys())



def test_boa::stringtoevalresmap_is_not_abstract():
    assert not inspect.isabstract(boa::StringToEvalResMap)


def test_boa::stringtoevalresmap_constructor_exists():
    assert callable(boa::StringToEvalResMap.__init__)


def test_boa::stringtoevalresmap_constructor_args():
    sig = inspect.signature(boa::StringToEvalResMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_boa::stringtoevalresmap_has_key():
    assert hasattr(boa::StringToEvalResMap, "key")
    descriptor = None
    for klass in boa::StringToEvalResMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_boa::evalboolres_is_not_abstract():
    assert not inspect.isabstract(boa::EvalBoolRes)


def test_boa::evalboolres_constructor_exists():
    assert callable(boa::EvalBoolRes.__init__)


def test_boa::evalboolres_constructor_args():
    sig = inspect.signature(boa::EvalBoolRes.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_boa::evalboolres_has_value():
    assert hasattr(boa::EvalBoolRes, "value")
    descriptor = None
    for klass in boa::EvalBoolRes.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_boa::evalintres_is_not_abstract():
    assert not inspect.isabstract(boa::EvalIntRes)


def test_boa::evalintres_constructor_exists():
    assert callable(boa::EvalIntRes.__init__)


def test_boa::evalintres_constructor_args():
    sig = inspect.signature(boa::EvalIntRes.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_boa::evalintres_has_value():
    assert hasattr(boa::EvalIntRes, "value")
    descriptor = None
    for klass in boa::EvalIntRes.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_evalfunres_is_not_abstract():
    assert not inspect.isabstract(EvalFunRes)


def test_evalfunres_constructor_exists():
    assert callable(EvalFunRes.__init__)


def test_evalfunres_constructor_args():
    sig = inspect.signature(EvalFunRes.__init__)
    params = list(sig.parameters.keys())



def test_boa::evalboundfunres_is_not_abstract():
    assert not inspect.isabstract(boa::EvalBoundFunRes)


def test_boa::evalboundfunres_constructor_exists():
    assert callable(boa::EvalBoundFunRes.__init__)


def test_boa::evalboundfunres_constructor_args():
    sig = inspect.signature(boa::EvalBoundFunRes.__init__)
    params = list(sig.parameters.keys())



def test_boolop_is_not_abstract():
    assert not inspect.isabstract(BoolOp)


def test_boolop_constructor_exists():
    assert callable(BoolOp.__init__)


def test_boolop_constructor_args():
    sig = inspect.signature(BoolOp.__init__)
    params = list(sig.parameters.keys())



def test_boa::boolopand_is_not_abstract():
    assert not inspect.isabstract(boa::BoolOpAnd)


def test_boa::boolopand_constructor_exists():
    assert callable(boa::BoolOpAnd.__init__)


def test_boa::boolopand_constructor_args():
    sig = inspect.signature(boa::BoolOpAnd.__init__)
    params = list(sig.parameters.keys())



def test_arithop_is_not_abstract():
    assert not inspect.isabstract(ArithOp)


def test_arithop_constructor_exists():
    assert callable(ArithOp.__init__)


def test_arithop_constructor_args():
    sig = inspect.signature(ArithOp.__init__)
    params = list(sig.parameters.keys())



def test_boa::arithopdivide_is_not_abstract():
    assert not inspect.isabstract(boa::ArithOpDivide)


def test_boa::arithopdivide_constructor_exists():
    assert callable(boa::ArithOpDivide.__init__)


def test_boa::arithopdivide_constructor_args():
    sig = inspect.signature(boa::ArithOpDivide.__init__)
    params = list(sig.parameters.keys())



def test_boa::arithoptimes_is_not_abstract():
    assert not inspect.isabstract(boa::ArithOpTimes)


def test_boa::arithoptimes_constructor_exists():
    assert callable(boa::ArithOpTimes.__init__)


def test_boa::arithoptimes_constructor_args():
    sig = inspect.signature(boa::ArithOpTimes.__init__)
    params = list(sig.parameters.keys())



def test_boa::arithopminus_is_not_abstract():
    assert not inspect.isabstract(boa::ArithOpMinus)


def test_boa::arithopminus_constructor_exists():
    assert callable(boa::ArithOpMinus.__init__)


def test_boa::arithopminus_constructor_args():
    sig = inspect.signature(boa::ArithOpMinus.__init__)
    params = list(sig.parameters.keys())



def test_boa::arithopremainder_is_not_abstract():
    assert not inspect.isabstract(boa::ArithOpRemainder)


def test_boa::arithopremainder_constructor_exists():
    assert callable(boa::ArithOpRemainder.__init__)


def test_boa::arithopremainder_constructor_args():
    sig = inspect.signature(boa::ArithOpRemainder.__init__)
    params = list(sig.parameters.keys())



def test_boa::arithopplus_is_not_abstract():
    assert not inspect.isabstract(boa::ArithOpPlus)


def test_boa::arithopplus_constructor_exists():
    assert callable(boa::ArithOpPlus.__init__)


def test_boa::arithopplus_constructor_args():
    sig = inspect.signature(boa::ArithOpPlus.__init__)
    params = list(sig.parameters.keys())



def test_boa::ctx_is_not_abstract():
    assert not inspect.isabstract(boa::Ctx)


def test_boa::ctx_constructor_exists():
    assert callable(boa::Ctx.__init__)


def test_boa::ctx_constructor_args():
    sig = inspect.signature(boa::Ctx.__init__)
    params = list(sig.parameters.keys())



def test_cmpop_is_not_abstract():
    assert not inspect.isabstract(CmpOp)


def test_cmpop_constructor_exists():
    assert callable(CmpOp.__init__)


def test_cmpop_constructor_args():
    sig = inspect.signature(CmpOp.__init__)
    params = list(sig.parameters.keys())



def test_boa::cmpopless_is_not_abstract():
    assert not inspect.isabstract(boa::CmpOpLess)


def test_boa::cmpopless_constructor_exists():
    assert callable(boa::CmpOpLess.__init__)


def test_boa::cmpopless_constructor_args():
    sig = inspect.signature(boa::CmpOpLess.__init__)
    params = list(sig.parameters.keys())



def test_boa::cmpopunequal_is_not_abstract():
    assert not inspect.isabstract(boa::CmpOpUnequal)


def test_boa::cmpopunequal_constructor_exists():
    assert callable(boa::CmpOpUnequal.__init__)


def test_boa::cmpopunequal_constructor_args():
    sig = inspect.signature(boa::CmpOpUnequal.__init__)
    params = list(sig.parameters.keys())



def test_boa::cmpopequal_is_not_abstract():
    assert not inspect.isabstract(boa::CmpOpEqual)


def test_boa::cmpopequal_constructor_exists():
    assert callable(boa::CmpOpEqual.__init__)


def test_boa::cmpopequal_constructor_args():
    sig = inspect.signature(boa::CmpOpEqual.__init__)
    params = list(sig.parameters.keys())



def test_boa::boolopor_is_not_abstract():
    assert not inspect.isabstract(boa::BoolOpOr)


def test_boa::boolopor_constructor_exists():
    assert callable(boa::BoolOpOr.__init__)


def test_boa::boolopor_constructor_args():
    sig = inspect.signature(boa::BoolOpOr.__init__)
    params = list(sig.parameters.keys())



def test_boa::field_is_not_abstract():
    assert not inspect.isabstract(boa::Field)


def test_boa::field_constructor_exists():
    assert callable(boa::Field.__init__)


def test_boa::field_constructor_args():
    sig = inspect.signature(boa::Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa::field_has_name():
    assert hasattr(boa::Field, "name")
    descriptor = None
    for klass in boa::Field.__mro__:
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



def test_boa::boolop_is_not_abstract():
    assert not inspect.isabstract(boa::BoolOp)


def test_boa::boolop_constructor_exists():
    assert callable(boa::BoolOp.__init__)


def test_boa::boolop_constructor_args():
    sig = inspect.signature(boa::BoolOp.__init__)
    params = list(sig.parameters.keys())



def test_boa::not_is_not_abstract():
    assert not inspect.isabstract(boa::Not)


def test_boa::not_constructor_exists():
    assert callable(boa::Not.__init__)


def test_boa::not_constructor_args():
    sig = inspect.signature(boa::Not.__init__)
    params = list(sig.parameters.keys())



def test_boa::arithop_is_not_abstract():
    assert not inspect.isabstract(boa::ArithOp)


def test_boa::arithop_constructor_exists():
    assert callable(boa::ArithOp.__init__)


def test_boa::arithop_constructor_args():
    sig = inspect.signature(boa::ArithOp.__init__)
    params = list(sig.parameters.keys())



def test_boa::fun_is_not_abstract():
    assert not inspect.isabstract(boa::Fun)


def test_boa::fun_constructor_exists():
    assert callable(boa::Fun.__init__)


def test_boa::fun_constructor_args():
    sig = inspect.signature(boa::Fun.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa::fun_has_name():
    assert hasattr(boa::Fun, "name")
    descriptor = None
    for klass in boa::Fun.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_boa::var_is_not_abstract():
    assert not inspect.isabstract(boa::Var)


def test_boa::var_constructor_exists():
    assert callable(boa::Var.__init__)


def test_boa::var_constructor_args():
    sig = inspect.signature(boa::Var.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa::var_has_name():
    assert hasattr(boa::Var, "name")
    descriptor = None
    for klass in boa::Var.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_boa::assign_is_not_abstract():
    assert not inspect.isabstract(boa::Assign)


def test_boa::assign_constructor_exists():
    assert callable(boa::Assign.__init__)


def test_boa::assign_constructor_args():
    sig = inspect.signature(boa::Assign.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa::assign_has_name():
    assert hasattr(boa::Assign, "name")
    descriptor = None
    for klass in boa::Assign.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_boa::copy_is_not_abstract():
    assert not inspect.isabstract(boa::Copy)


def test_boa::copy_constructor_exists():
    assert callable(boa::Copy.__init__)


def test_boa::copy_constructor_args():
    sig = inspect.signature(boa::Copy.__init__)
    params = list(sig.parameters.keys())



def test_boa::cmpop_is_not_abstract():
    assert not inspect.isabstract(boa::CmpOp)


def test_boa::cmpop_constructor_exists():
    assert callable(boa::CmpOp.__init__)


def test_boa::cmpop_constructor_args():
    sig = inspect.signature(boa::CmpOp.__init__)
    params = list(sig.parameters.keys())



def test_boa::let_is_not_abstract():
    assert not inspect.isabstract(boa::Let)


def test_boa::let_constructor_exists():
    assert callable(boa::Let.__init__)


def test_boa::let_constructor_args():
    sig = inspect.signature(boa::Let.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa::let_has_name():
    assert hasattr(boa::Let, "name")
    descriptor = None
    for klass in boa::Let.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_boa::if_is_not_abstract():
    assert not inspect.isabstract(boa::If)


def test_boa::if_constructor_exists():
    assert callable(boa::If.__init__)


def test_boa::if_constructor_args():
    sig = inspect.signature(boa::If.__init__)
    params = list(sig.parameters.keys())



def test_boa::with_is_not_abstract():
    assert not inspect.isabstract(boa::With)


def test_boa::with_constructor_exists():
    assert callable(boa::With.__init__)


def test_boa::with_constructor_args():
    sig = inspect.signature(boa::With.__init__)
    params = list(sig.parameters.keys())



def test_boa::bobject_is_not_abstract():
    assert not inspect.isabstract(boa::BObject)


def test_boa::bobject_constructor_exists():
    assert callable(boa::BObject.__init__)


def test_boa::bobject_constructor_args():
    sig = inspect.signature(boa::BObject.__init__)
    params = list(sig.parameters.keys())



def test_boa::seq_is_not_abstract():
    assert not inspect.isabstract(boa::Seq)


def test_boa::seq_constructor_exists():
    assert callable(boa::Seq.__init__)


def test_boa::seq_constructor_args():
    sig = inspect.signature(boa::Seq.__init__)
    params = list(sig.parameters.keys())



def test_boa::app_is_not_abstract():
    assert not inspect.isabstract(boa::App)


def test_boa::app_constructor_exists():
    assert callable(boa::App.__init__)


def test_boa::app_constructor_args():
    sig = inspect.signature(boa::App.__init__)
    params = list(sig.parameters.keys())



def test_toplevelcmd_is_not_abstract():
    assert not inspect.isabstract(TopLevelCmd)


def test_toplevelcmd_constructor_exists():
    assert callable(TopLevelCmd.__init__)


def test_toplevelcmd_constructor_args():
    sig = inspect.signature(TopLevelCmd.__init__)
    params = list(sig.parameters.keys())



def test_boa::def_is_not_abstract():
    assert not inspect.isabstract(boa::Def)


def test_boa::def_constructor_exists():
    assert callable(boa::Def.__init__)


def test_boa::def_constructor_args():
    sig = inspect.signature(boa::Def.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa::def_has_name():
    assert hasattr(boa::Def, "name")
    descriptor = None
    for klass in boa::Def.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_boa::expr_is_not_abstract():
    assert not inspect.isabstract(boa::Expr)


def test_boa::expr_constructor_exists():
    assert callable(boa::Expr.__init__)


def test_boa::expr_constructor_args():
    sig = inspect.signature(boa::Expr.__init__)
    params = list(sig.parameters.keys())



def test_boa::project_is_not_abstract():
    assert not inspect.isabstract(boa::Project)


def test_boa::project_constructor_exists():
    assert callable(boa::Project.__init__)


def test_boa::project_constructor_args():
    sig = inspect.signature(boa::Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boa::project_has_name():
    assert hasattr(boa::Project, "name")
    descriptor = None
    for klass in boa::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_boa::toplevelcmd_is_not_abstract():
    assert not inspect.isabstract(boa::TopLevelCmd)


def test_boa::toplevelcmd_constructor_exists():
    assert callable(boa::TopLevelCmd.__init__)


def test_boa::toplevelcmd_constructor_args():
    sig = inspect.signature(boa::TopLevelCmd.__init__)
    params = list(sig.parameters.keys())



def test_boa::skip_is_not_abstract():
    assert not inspect.isabstract(boa::Skip)


def test_boa::skip_constructor_exists():
    assert callable(boa::Skip.__init__)


def test_boa::skip_constructor_args():
    sig = inspect.signature(boa::Skip.__init__)
    params = list(sig.parameters.keys())



def test_boa::int_is_not_abstract():
    assert not inspect.isabstract(boa::Int)


def test_boa::int_constructor_exists():
    assert callable(boa::Int.__init__)


def test_boa::int_constructor_args():
    sig = inspect.signature(boa::Int.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_boa::int_has_value():
    assert hasattr(boa::Int, "value")
    descriptor = None
    for klass in boa::Int.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_boa::bool_is_not_abstract():
    assert not inspect.isabstract(boa::Bool)


def test_boa::bool_constructor_exists():
    assert callable(boa::Bool.__init__)


def test_boa::bool_constructor_args():
    sig = inspect.signature(boa::Bool.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_boa::bool_has_value():
    assert hasattr(boa::Bool, "value")
    descriptor = None
    for klass in boa::Bool.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_boa::this_is_not_abstract():
    assert not inspect.isabstract(boa::This)


def test_boa::this_constructor_exists():
    assert callable(boa::This.__init__)


def test_boa::this_constructor_args():
    sig = inspect.signature(boa::This.__init__)
    params = list(sig.parameters.keys())



def test_boa::file_is_not_abstract():
    assert not inspect.isabstract(boa::File)


def test_boa::file_constructor_exists():
    assert callable(boa::File.__init__)


def test_boa::file_constructor_args():
    sig = inspect.signature(boa::File.__init__)
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
EvalRes_strategy = st.builds(
    EvalRes,
)
boa::EvalFunRes_strategy = st.builds(
    boa::EvalFunRes,
    name=
        safe_text
)
boa::EvalMapRes_strategy = st.builds(
    boa::EvalMapRes,
)
boa::EvalRes_strategy = st.builds(
    boa::EvalRes,
)
boa::StringToEvalResMap_strategy = st.builds(
    boa::StringToEvalResMap,
    key=
        safe_text
)
boa::EvalBoolRes_strategy = st.builds(
    boa::EvalBoolRes,
    value=
        st.booleans()
)
boa::EvalIntRes_strategy = st.builds(
    boa::EvalIntRes,
    value=
        st.integers()
)
EvalFunRes_strategy = st.builds(
    EvalFunRes,
)
boa::EvalBoundFunRes_strategy = st.builds(
    boa::EvalBoundFunRes,
)
BoolOp_strategy = st.builds(
    BoolOp,
)
boa::BoolOpAnd_strategy = st.builds(
    boa::BoolOpAnd,
)
ArithOp_strategy = st.builds(
    ArithOp,
)
boa::ArithOpDivide_strategy = st.builds(
    boa::ArithOpDivide,
)
boa::ArithOpTimes_strategy = st.builds(
    boa::ArithOpTimes,
)
boa::ArithOpMinus_strategy = st.builds(
    boa::ArithOpMinus,
)
boa::ArithOpRemainder_strategy = st.builds(
    boa::ArithOpRemainder,
)
boa::ArithOpPlus_strategy = st.builds(
    boa::ArithOpPlus,
)
boa::Ctx_strategy = st.builds(
    boa::Ctx,
)
CmpOp_strategy = st.builds(
    CmpOp,
)
boa::CmpOpLess_strategy = st.builds(
    boa::CmpOpLess,
)
boa::CmpOpUnequal_strategy = st.builds(
    boa::CmpOpUnequal,
)
boa::CmpOpEqual_strategy = st.builds(
    boa::CmpOpEqual,
)
boa::BoolOpOr_strategy = st.builds(
    boa::BoolOpOr,
)
boa::Field_strategy = st.builds(
    boa::Field,
    name=
        safe_text
)
Expr_strategy = st.builds(
    Expr,
)
boa::BoolOp_strategy = st.builds(
    boa::BoolOp,
)
boa::Not_strategy = st.builds(
    boa::Not,
)
boa::ArithOp_strategy = st.builds(
    boa::ArithOp,
)
boa::Fun_strategy = st.builds(
    boa::Fun,
    name=
        safe_text
)
boa::Var_strategy = st.builds(
    boa::Var,
    name=
        safe_text
)
boa::Assign_strategy = st.builds(
    boa::Assign,
    name=
        safe_text
)
boa::Copy_strategy = st.builds(
    boa::Copy,
)
boa::CmpOp_strategy = st.builds(
    boa::CmpOp,
)
boa::Let_strategy = st.builds(
    boa::Let,
    name=
        safe_text
)
boa::If_strategy = st.builds(
    boa::If,
)
boa::With_strategy = st.builds(
    boa::With,
)
boa::BObject_strategy = st.builds(
    boa::BObject,
)
boa::Seq_strategy = st.builds(
    boa::Seq,
)
boa::App_strategy = st.builds(
    boa::App,
)
TopLevelCmd_strategy = st.builds(
    TopLevelCmd,
)
boa::Def_strategy = st.builds(
    boa::Def,
    name=
        safe_text
)
boa::Expr_strategy = st.builds(
    boa::Expr,
)
boa::Project_strategy = st.builds(
    boa::Project,
    name=
        safe_text
)
boa::TopLevelCmd_strategy = st.builds(
    boa::TopLevelCmd,
)
boa::Skip_strategy = st.builds(
    boa::Skip,
)
boa::Int_strategy = st.builds(
    boa::Int,
    value=
        st.integers()
)
boa::Bool_strategy = st.builds(
    boa::Bool,
    value=
        st.booleans()
)
boa::This_strategy = st.builds(
    boa::This,
)
boa::File_strategy = st.builds(
    boa::File,
)

@given(instance=EvalRes_strategy)
@settings(max_examples=50)
def test_evalres_instantiation(instance):
    assert isinstance(instance, EvalRes)

@given(instance=boa::EvalFunRes_strategy)
@settings(max_examples=50)
def test_boa::evalfunres_instantiation(instance):
    assert isinstance(instance, boa::EvalFunRes)

@given(instance=boa::EvalFunRes_strategy)
def test_boa::evalfunres_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=boa::EvalFunRes_strategy)
def test_boa::evalfunres_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=boa::EvalMapRes_strategy)
@settings(max_examples=50)
def test_boa::evalmapres_instantiation(instance):
    assert isinstance(instance, boa::EvalMapRes)

@given(instance=boa::EvalRes_strategy)
@settings(max_examples=50)
def test_boa::evalres_instantiation(instance):
    assert isinstance(instance, boa::EvalRes)

@given(instance=boa::StringToEvalResMap_strategy)
@settings(max_examples=50)
def test_boa::stringtoevalresmap_instantiation(instance):
    assert isinstance(instance, boa::StringToEvalResMap)

@given(instance=boa::StringToEvalResMap_strategy)
def test_boa::stringtoevalresmap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=boa::StringToEvalResMap_strategy)
def test_boa::stringtoevalresmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=boa::EvalBoolRes_strategy)
@settings(max_examples=50)
def test_boa::evalboolres_instantiation(instance):
    assert isinstance(instance, boa::EvalBoolRes)

@given(instance=boa::EvalBoolRes_strategy)
def test_boa::evalboolres_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=boa::EvalBoolRes_strategy)
def test_boa::evalboolres_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=boa::EvalIntRes_strategy)
@settings(max_examples=50)
def test_boa::evalintres_instantiation(instance):
    assert isinstance(instance, boa::EvalIntRes)

@given(instance=boa::EvalIntRes_strategy)
def test_boa::evalintres_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=boa::EvalIntRes_strategy)
def test_boa::evalintres_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=EvalFunRes_strategy)
@settings(max_examples=50)
def test_evalfunres_instantiation(instance):
    assert isinstance(instance, EvalFunRes)

@given(instance=boa::EvalBoundFunRes_strategy)
@settings(max_examples=50)
def test_boa::evalboundfunres_instantiation(instance):
    assert isinstance(instance, boa::EvalBoundFunRes)

@given(instance=BoolOp_strategy)
@settings(max_examples=50)
def test_boolop_instantiation(instance):
    assert isinstance(instance, BoolOp)

@given(instance=boa::BoolOpAnd_strategy)
@settings(max_examples=50)
def test_boa::boolopand_instantiation(instance):
    assert isinstance(instance, boa::BoolOpAnd)

@given(instance=ArithOp_strategy)
@settings(max_examples=50)
def test_arithop_instantiation(instance):
    assert isinstance(instance, ArithOp)

@given(instance=boa::ArithOpDivide_strategy)
@settings(max_examples=50)
def test_boa::arithopdivide_instantiation(instance):
    assert isinstance(instance, boa::ArithOpDivide)

@given(instance=boa::ArithOpTimes_strategy)
@settings(max_examples=50)
def test_boa::arithoptimes_instantiation(instance):
    assert isinstance(instance, boa::ArithOpTimes)

@given(instance=boa::ArithOpMinus_strategy)
@settings(max_examples=50)
def test_boa::arithopminus_instantiation(instance):
    assert isinstance(instance, boa::ArithOpMinus)

@given(instance=boa::ArithOpRemainder_strategy)
@settings(max_examples=50)
def test_boa::arithopremainder_instantiation(instance):
    assert isinstance(instance, boa::ArithOpRemainder)

@given(instance=boa::ArithOpPlus_strategy)
@settings(max_examples=50)
def test_boa::arithopplus_instantiation(instance):
    assert isinstance(instance, boa::ArithOpPlus)

@given(instance=boa::Ctx_strategy)
@settings(max_examples=50)
def test_boa::ctx_instantiation(instance):
    assert isinstance(instance, boa::Ctx)

@given(instance=CmpOp_strategy)
@settings(max_examples=50)
def test_cmpop_instantiation(instance):
    assert isinstance(instance, CmpOp)

@given(instance=boa::CmpOpLess_strategy)
@settings(max_examples=50)
def test_boa::cmpopless_instantiation(instance):
    assert isinstance(instance, boa::CmpOpLess)

@given(instance=boa::CmpOpUnequal_strategy)
@settings(max_examples=50)
def test_boa::cmpopunequal_instantiation(instance):
    assert isinstance(instance, boa::CmpOpUnequal)

@given(instance=boa::CmpOpEqual_strategy)
@settings(max_examples=50)
def test_boa::cmpopequal_instantiation(instance):
    assert isinstance(instance, boa::CmpOpEqual)

@given(instance=boa::BoolOpOr_strategy)
@settings(max_examples=50)
def test_boa::boolopor_instantiation(instance):
    assert isinstance(instance, boa::BoolOpOr)

@given(instance=boa::Field_strategy)
@settings(max_examples=50)
def test_boa::field_instantiation(instance):
    assert isinstance(instance, boa::Field)

@given(instance=boa::Field_strategy)
def test_boa::field_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=boa::Field_strategy)
def test_boa::field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=boa::BoolOp_strategy)
@settings(max_examples=50)
def test_boa::boolop_instantiation(instance):
    assert isinstance(instance, boa::BoolOp)

@given(instance=boa::Not_strategy)
@settings(max_examples=50)
def test_boa::not_instantiation(instance):
    assert isinstance(instance, boa::Not)

@given(instance=boa::ArithOp_strategy)
@settings(max_examples=50)
def test_boa::arithop_instantiation(instance):
    assert isinstance(instance, boa::ArithOp)

@given(instance=boa::Fun_strategy)
@settings(max_examples=50)
def test_boa::fun_instantiation(instance):
    assert isinstance(instance, boa::Fun)

@given(instance=boa::Fun_strategy)
def test_boa::fun_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=boa::Fun_strategy)
def test_boa::fun_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=boa::Var_strategy)
@settings(max_examples=50)
def test_boa::var_instantiation(instance):
    assert isinstance(instance, boa::Var)

@given(instance=boa::Var_strategy)
def test_boa::var_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=boa::Var_strategy)
def test_boa::var_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=boa::Assign_strategy)
@settings(max_examples=50)
def test_boa::assign_instantiation(instance):
    assert isinstance(instance, boa::Assign)

@given(instance=boa::Assign_strategy)
def test_boa::assign_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=boa::Assign_strategy)
def test_boa::assign_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=boa::Copy_strategy)
@settings(max_examples=50)
def test_boa::copy_instantiation(instance):
    assert isinstance(instance, boa::Copy)

@given(instance=boa::CmpOp_strategy)
@settings(max_examples=50)
def test_boa::cmpop_instantiation(instance):
    assert isinstance(instance, boa::CmpOp)

@given(instance=boa::Let_strategy)
@settings(max_examples=50)
def test_boa::let_instantiation(instance):
    assert isinstance(instance, boa::Let)

@given(instance=boa::Let_strategy)
def test_boa::let_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=boa::Let_strategy)
def test_boa::let_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=boa::If_strategy)
@settings(max_examples=50)
def test_boa::if_instantiation(instance):
    assert isinstance(instance, boa::If)

@given(instance=boa::With_strategy)
@settings(max_examples=50)
def test_boa::with_instantiation(instance):
    assert isinstance(instance, boa::With)

@given(instance=boa::BObject_strategy)
@settings(max_examples=50)
def test_boa::bobject_instantiation(instance):
    assert isinstance(instance, boa::BObject)

@given(instance=boa::Seq_strategy)
@settings(max_examples=50)
def test_boa::seq_instantiation(instance):
    assert isinstance(instance, boa::Seq)

@given(instance=boa::App_strategy)
@settings(max_examples=50)
def test_boa::app_instantiation(instance):
    assert isinstance(instance, boa::App)

@given(instance=TopLevelCmd_strategy)
@settings(max_examples=50)
def test_toplevelcmd_instantiation(instance):
    assert isinstance(instance, TopLevelCmd)

@given(instance=boa::Def_strategy)
@settings(max_examples=50)
def test_boa::def_instantiation(instance):
    assert isinstance(instance, boa::Def)

@given(instance=boa::Def_strategy)
def test_boa::def_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=boa::Def_strategy)
def test_boa::def_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=boa::Expr_strategy)
@settings(max_examples=50)
def test_boa::expr_instantiation(instance):
    assert isinstance(instance, boa::Expr)

@given(instance=boa::Project_strategy)
@settings(max_examples=50)
def test_boa::project_instantiation(instance):
    assert isinstance(instance, boa::Project)

@given(instance=boa::Project_strategy)
def test_boa::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=boa::Project_strategy)
def test_boa::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=boa::TopLevelCmd_strategy)
@settings(max_examples=50)
def test_boa::toplevelcmd_instantiation(instance):
    assert isinstance(instance, boa::TopLevelCmd)

@given(instance=boa::Skip_strategy)
@settings(max_examples=50)
def test_boa::skip_instantiation(instance):
    assert isinstance(instance, boa::Skip)

@given(instance=boa::Int_strategy)
@settings(max_examples=50)
def test_boa::int_instantiation(instance):
    assert isinstance(instance, boa::Int)

@given(instance=boa::Int_strategy)
def test_boa::int_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=boa::Int_strategy)
def test_boa::int_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=boa::Bool_strategy)
@settings(max_examples=50)
def test_boa::bool_instantiation(instance):
    assert isinstance(instance, boa::Bool)

@given(instance=boa::Bool_strategy)
def test_boa::bool_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=boa::Bool_strategy)
def test_boa::bool_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=boa::This_strategy)
@settings(max_examples=50)
def test_boa::this_instantiation(instance):
    assert isinstance(instance, boa::This)

@given(instance=boa::File_strategy)
@settings(max_examples=50)
def test_boa::file_instantiation(instance):
    assert isinstance(instance, boa::File)
