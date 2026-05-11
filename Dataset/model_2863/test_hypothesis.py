import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    gDSL::ValueDecl,
    gDSL::Field,
    ApplyExp,
    gDSL::Args,
    gDSL::AtomicExp,
    SelectExp,
    gDSL::ApplyExp,
    MExp,
    gDSL::SelectExp,
    AExp,
    gDSL::MExp,
    RExp,
    gDSL::AExp,
    AndAlsoExp,
    gDSL::RExp,
    OrElseExp,
    gDSL::AndAlsoExp,
    ClosedExp,
    gDSL::OrElseExp,
    gDSL::MonadicExp,
    CaseExp,
    gDSL::PAT,
    gDSL::ClosedExp,
    gDSL::CaseExp,
    gDSL::TyElement,
    gDSL::TyBind,
    gDSL::CONS,
    gDSL::Exp,
    gDSL::Ty,
    gDSL::TyVars,
    Decl,
    gDSL::Val,
    gDSL::Type,
    gDSL::DeclExport,
    gDSL::Decl,
    gDSL::Model,
    gDSL::ConDecl,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gdsl::valuedecl_is_not_abstract():
    assert not inspect.isabstract(gDSL::ValueDecl)


def test_gdsl::valuedecl_constructor_exists():
    assert callable(gDSL::ValueDecl.__init__)


def test_gdsl::valuedecl_constructor_args():
    sig = inspect.signature(gDSL::ValueDecl.__init__)
    params = list(sig.parameters.keys())
    assert "ids" in params, "Missing parameter 'ids'"
    assert "name" in params, "Missing parameter 'name'"

def test_gdsl::valuedecl_has_ids():
    assert hasattr(gDSL::ValueDecl, "ids")
    descriptor = None
    for klass in gDSL::ValueDecl.__mro__:
        if "ids" in klass.__dict__:
            descriptor = klass.__dict__["ids"]
            break
    assert isinstance(descriptor, property)

def test_gdsl::valuedecl_has_name():
    assert hasattr(gDSL::ValueDecl, "name")
    descriptor = None
    for klass in gDSL::ValueDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gdsl::field_is_not_abstract():
    assert not inspect.isabstract(gDSL::Field)


def test_gdsl::field_constructor_exists():
    assert callable(gDSL::Field.__init__)


def test_gdsl::field_constructor_args():
    sig = inspect.signature(gDSL::Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gdsl::field_has_name():
    assert hasattr(gDSL::Field, "name")
    descriptor = None
    for klass in gDSL::Field.__mro__:
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



def test_gdsl::args_is_not_abstract():
    assert not inspect.isabstract(gDSL::Args)


def test_gdsl::args_constructor_exists():
    assert callable(gDSL::Args.__init__)


def test_gdsl::args_constructor_args():
    sig = inspect.signature(gDSL::Args.__init__)
    params = list(sig.parameters.keys())



def test_gdsl::atomicexp_is_not_abstract():
    assert not inspect.isabstract(gDSL::AtomicExp)


def test_gdsl::atomicexp_constructor_exists():
    assert callable(gDSL::AtomicExp.__init__)


def test_gdsl::atomicexp_constructor_args():
    sig = inspect.signature(gDSL::AtomicExp.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_gdsl::atomicexp_has_id():
    assert hasattr(gDSL::AtomicExp, "id")
    descriptor = None
    for klass in gDSL::AtomicExp.__mro__:
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



def test_gdsl::applyexp_is_not_abstract():
    assert not inspect.isabstract(gDSL::ApplyExp)


def test_gdsl::applyexp_constructor_exists():
    assert callable(gDSL::ApplyExp.__init__)


def test_gdsl::applyexp_constructor_args():
    sig = inspect.signature(gDSL::ApplyExp.__init__)
    params = list(sig.parameters.keys())



def test_mexp_is_not_abstract():
    assert not inspect.isabstract(MExp)


def test_mexp_constructor_exists():
    assert callable(MExp.__init__)


def test_mexp_constructor_args():
    sig = inspect.signature(MExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl::selectexp_is_not_abstract():
    assert not inspect.isabstract(gDSL::SelectExp)


def test_gdsl::selectexp_constructor_exists():
    assert callable(gDSL::SelectExp.__init__)


def test_gdsl::selectexp_constructor_args():
    sig = inspect.signature(gDSL::SelectExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_gdsl::selectexp_has_symbol():
    assert hasattr(gDSL::SelectExp, "symbol")
    descriptor = None
    for klass in gDSL::SelectExp.__mro__:
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



def test_gdsl::mexp_is_not_abstract():
    assert not inspect.isabstract(gDSL::MExp)


def test_gdsl::mexp_constructor_exists():
    assert callable(gDSL::MExp.__init__)


def test_gdsl::mexp_constructor_args():
    sig = inspect.signature(gDSL::MExp.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"

def test_gdsl::mexp_has_sign():
    assert hasattr(gDSL::MExp, "sign")
    descriptor = None
    for klass in gDSL::MExp.__mro__:
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



def test_gdsl::aexp_is_not_abstract():
    assert not inspect.isabstract(gDSL::AExp)


def test_gdsl::aexp_constructor_exists():
    assert callable(gDSL::AExp.__init__)


def test_gdsl::aexp_constructor_args():
    sig = inspect.signature(gDSL::AExp.__init__)
    params = list(sig.parameters.keys())
    assert "sym" in params, "Missing parameter 'sym'"

def test_gdsl::aexp_has_sym():
    assert hasattr(gDSL::AExp, "sym")
    descriptor = None
    for klass in gDSL::AExp.__mro__:
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



def test_gdsl::rexp_is_not_abstract():
    assert not inspect.isabstract(gDSL::RExp)


def test_gdsl::rexp_constructor_exists():
    assert callable(gDSL::RExp.__init__)


def test_gdsl::rexp_constructor_args():
    sig = inspect.signature(gDSL::RExp.__init__)
    params = list(sig.parameters.keys())



def test_orelseexp_is_not_abstract():
    assert not inspect.isabstract(OrElseExp)


def test_orelseexp_constructor_exists():
    assert callable(OrElseExp.__init__)


def test_orelseexp_constructor_args():
    sig = inspect.signature(OrElseExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl::andalsoexp_is_not_abstract():
    assert not inspect.isabstract(gDSL::AndAlsoExp)


def test_gdsl::andalsoexp_constructor_exists():
    assert callable(gDSL::AndAlsoExp.__init__)


def test_gdsl::andalsoexp_constructor_args():
    sig = inspect.signature(gDSL::AndAlsoExp.__init__)
    params = list(sig.parameters.keys())



def test_closedexp_is_not_abstract():
    assert not inspect.isabstract(ClosedExp)


def test_closedexp_constructor_exists():
    assert callable(ClosedExp.__init__)


def test_closedexp_constructor_args():
    sig = inspect.signature(ClosedExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl::orelseexp_is_not_abstract():
    assert not inspect.isabstract(gDSL::OrElseExp)


def test_gdsl::orelseexp_constructor_exists():
    assert callable(gDSL::OrElseExp.__init__)


def test_gdsl::orelseexp_constructor_args():
    sig = inspect.signature(gDSL::OrElseExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl::monadicexp_is_not_abstract():
    assert not inspect.isabstract(gDSL::MonadicExp)


def test_gdsl::monadicexp_constructor_exists():
    assert callable(gDSL::MonadicExp.__init__)


def test_gdsl::monadicexp_constructor_args():
    sig = inspect.signature(gDSL::MonadicExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gdsl::monadicexp_has_name():
    assert hasattr(gDSL::MonadicExp, "name")
    descriptor = None
    for klass in gDSL::MonadicExp.__mro__:
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



def test_gdsl::pat_is_not_abstract():
    assert not inspect.isabstract(gDSL::PAT)


def test_gdsl::pat_constructor_exists():
    assert callable(gDSL::PAT.__init__)


def test_gdsl::pat_constructor_args():
    sig = inspect.signature(gDSL::PAT.__init__)
    params = list(sig.parameters.keys())
    assert "uscore" in params, "Missing parameter 'uscore'"
    assert "int" in params, "Missing parameter 'int'"
    assert "id" in params, "Missing parameter 'id'"
    assert "bitpat" in params, "Missing parameter 'bitpat'"

def test_gdsl::pat_has_uscore():
    assert hasattr(gDSL::PAT, "uscore")
    descriptor = None
    for klass in gDSL::PAT.__mro__:
        if "uscore" in klass.__dict__:
            descriptor = klass.__dict__["uscore"]
            break
    assert isinstance(descriptor, property)

def test_gdsl::pat_has_int():
    assert hasattr(gDSL::PAT, "int")
    descriptor = None
    for klass in gDSL::PAT.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)

def test_gdsl::pat_has_id():
    assert hasattr(gDSL::PAT, "id")
    descriptor = None
    for klass in gDSL::PAT.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_gdsl::pat_has_bitpat():
    assert hasattr(gDSL::PAT, "bitpat")
    descriptor = None
    for klass in gDSL::PAT.__mro__:
        if "bitpat" in klass.__dict__:
            descriptor = klass.__dict__["bitpat"]
            break
    assert isinstance(descriptor, property)



def test_gdsl::closedexp_is_not_abstract():
    assert not inspect.isabstract(gDSL::ClosedExp)


def test_gdsl::closedexp_constructor_exists():
    assert callable(gDSL::ClosedExp.__init__)


def test_gdsl::closedexp_constructor_args():
    sig = inspect.signature(gDSL::ClosedExp.__init__)
    params = list(sig.parameters.keys())



def test_gdsl::caseexp_is_not_abstract():
    assert not inspect.isabstract(gDSL::CaseExp)


def test_gdsl::caseexp_constructor_exists():
    assert callable(gDSL::CaseExp.__init__)


def test_gdsl::caseexp_constructor_args():
    sig = inspect.signature(gDSL::CaseExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gdsl::caseexp_has_name():
    assert hasattr(gDSL::CaseExp, "name")
    descriptor = None
    for klass in gDSL::CaseExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gdsl::tyelement_is_not_abstract():
    assert not inspect.isabstract(gDSL::TyElement)


def test_gdsl::tyelement_constructor_exists():
    assert callable(gDSL::TyElement.__init__)


def test_gdsl::tyelement_constructor_args():
    sig = inspect.signature(gDSL::TyElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gdsl::tyelement_has_name():
    assert hasattr(gDSL::TyElement, "name")
    descriptor = None
    for klass in gDSL::TyElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gdsl::tybind_is_not_abstract():
    assert not inspect.isabstract(gDSL::TyBind)


def test_gdsl::tybind_constructor_exists():
    assert callable(gDSL::TyBind.__init__)


def test_gdsl::tybind_constructor_args():
    sig = inspect.signature(gDSL::TyBind.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gdsl::tybind_has_name():
    assert hasattr(gDSL::TyBind, "name")
    descriptor = None
    for klass in gDSL::TyBind.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gdsl::cons_is_not_abstract():
    assert not inspect.isabstract(gDSL::CONS)


def test_gdsl::cons_constructor_exists():
    assert callable(gDSL::CONS.__init__)


def test_gdsl::cons_constructor_args():
    sig = inspect.signature(gDSL::CONS.__init__)
    params = list(sig.parameters.keys())
    assert "conName" in params, "Missing parameter 'conName'"

def test_gdsl::cons_has_conName():
    assert hasattr(gDSL::CONS, "conName")
    descriptor = None
    for klass in gDSL::CONS.__mro__:
        if "conName" in klass.__dict__:
            descriptor = klass.__dict__["conName"]
            break
    assert isinstance(descriptor, property)



def test_gdsl::exp_is_not_abstract():
    assert not inspect.isabstract(gDSL::Exp)


def test_gdsl::exp_constructor_exists():
    assert callable(gDSL::Exp.__init__)


def test_gdsl::exp_constructor_args():
    sig = inspect.signature(gDSL::Exp.__init__)
    params = list(sig.parameters.keys())
    assert "mid" in params, "Missing parameter 'mid'"

def test_gdsl::exp_has_mid():
    assert hasattr(gDSL::Exp, "mid")
    descriptor = None
    for klass in gDSL::Exp.__mro__:
        if "mid" in klass.__dict__:
            descriptor = klass.__dict__["mid"]
            break
    assert isinstance(descriptor, property)



def test_gdsl::ty_is_not_abstract():
    assert not inspect.isabstract(gDSL::Ty)


def test_gdsl::ty_constructor_exists():
    assert callable(gDSL::Ty.__init__)


def test_gdsl::ty_constructor_args():
    sig = inspect.signature(gDSL::Ty.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_gdsl::ty_has_value():
    assert hasattr(gDSL::Ty, "value")
    descriptor = None
    for klass in gDSL::Ty.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_gdsl::ty_has_type():
    assert hasattr(gDSL::Ty, "type")
    descriptor = None
    for klass in gDSL::Ty.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_gdsl::tyvars_is_not_abstract():
    assert not inspect.isabstract(gDSL::TyVars)


def test_gdsl::tyvars_constructor_exists():
    assert callable(gDSL::TyVars.__init__)


def test_gdsl::tyvars_constructor_args():
    sig = inspect.signature(gDSL::TyVars.__init__)
    params = list(sig.parameters.keys())



def test_decl_is_not_abstract():
    assert not inspect.isabstract(Decl)


def test_decl_constructor_exists():
    assert callable(Decl.__init__)


def test_decl_constructor_args():
    sig = inspect.signature(Decl.__init__)
    params = list(sig.parameters.keys())



def test_gdsl::val_is_not_abstract():
    assert not inspect.isabstract(gDSL::Val)


def test_gdsl::val_constructor_exists():
    assert callable(gDSL::Val.__init__)


def test_gdsl::val_constructor_args():
    sig = inspect.signature(gDSL::Val.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "attr" in params, "Missing parameter 'attr'"
    assert "mid" in params, "Missing parameter 'mid'"
    assert "decPat" in params, "Missing parameter 'decPat'"

def test_gdsl::val_has_name():
    assert hasattr(gDSL::Val, "name")
    descriptor = None
    for klass in gDSL::Val.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gdsl::val_has_attr():
    assert hasattr(gDSL::Val, "attr")
    descriptor = None
    for klass in gDSL::Val.__mro__:
        if "attr" in klass.__dict__:
            descriptor = klass.__dict__["attr"]
            break
    assert isinstance(descriptor, property)

def test_gdsl::val_has_mid():
    assert hasattr(gDSL::Val, "mid")
    descriptor = None
    for klass in gDSL::Val.__mro__:
        if "mid" in klass.__dict__:
            descriptor = klass.__dict__["mid"]
            break
    assert isinstance(descriptor, property)

def test_gdsl::val_has_decPat():
    assert hasattr(gDSL::Val, "decPat")
    descriptor = None
    for klass in gDSL::Val.__mro__:
        if "decPat" in klass.__dict__:
            descriptor = klass.__dict__["decPat"]
            break
    assert isinstance(descriptor, property)



def test_gdsl::type_is_not_abstract():
    assert not inspect.isabstract(gDSL::Type)


def test_gdsl::type_constructor_exists():
    assert callable(gDSL::Type.__init__)


def test_gdsl::type_constructor_args():
    sig = inspect.signature(gDSL::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gdsl::type_has_name():
    assert hasattr(gDSL::Type, "name")
    descriptor = None
    for klass in gDSL::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gdsl::declexport_is_not_abstract():
    assert not inspect.isabstract(gDSL::DeclExport)


def test_gdsl::declexport_constructor_exists():
    assert callable(gDSL::DeclExport.__init__)


def test_gdsl::declexport_constructor_args():
    sig = inspect.signature(gDSL::DeclExport.__init__)
    params = list(sig.parameters.keys())



def test_gdsl::decl_is_not_abstract():
    assert not inspect.isabstract(gDSL::Decl)


def test_gdsl::decl_constructor_exists():
    assert callable(gDSL::Decl.__init__)


def test_gdsl::decl_constructor_args():
    sig = inspect.signature(gDSL::Decl.__init__)
    params = list(sig.parameters.keys())



def test_gdsl::model_is_not_abstract():
    assert not inspect.isabstract(gDSL::Model)


def test_gdsl::model_constructor_exists():
    assert callable(gDSL::Model.__init__)


def test_gdsl::model_constructor_args():
    sig = inspect.signature(gDSL::Model.__init__)
    params = list(sig.parameters.keys())



def test_gdsl::condecl_is_not_abstract():
    assert not inspect.isabstract(gDSL::ConDecl)


def test_gdsl::condecl_constructor_exists():
    assert callable(gDSL::ConDecl.__init__)


def test_gdsl::condecl_constructor_args():
    sig = inspect.signature(gDSL::ConDecl.__init__)
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
gDSL::ValueDecl_strategy = st.builds(
    gDSL::ValueDecl,
    ids=
        safe_text,
    name=
        safe_text
)
gDSL::Field_strategy = st.builds(
    gDSL::Field,
    name=
        safe_text
)
ApplyExp_strategy = st.builds(
    ApplyExp,
)
gDSL::Args_strategy = st.builds(
    gDSL::Args,
)
gDSL::AtomicExp_strategy = st.builds(
    gDSL::AtomicExp,
    id=
        safe_text
)
SelectExp_strategy = st.builds(
    SelectExp,
)
gDSL::ApplyExp_strategy = st.builds(
    gDSL::ApplyExp,
)
MExp_strategy = st.builds(
    MExp,
)
gDSL::SelectExp_strategy = st.builds(
    gDSL::SelectExp,
    symbol=
        safe_text
)
AExp_strategy = st.builds(
    AExp,
)
gDSL::MExp_strategy = st.builds(
    gDSL::MExp,
    sign=
        safe_text
)
RExp_strategy = st.builds(
    RExp,
)
gDSL::AExp_strategy = st.builds(
    gDSL::AExp,
    sym=
        safe_text
)
AndAlsoExp_strategy = st.builds(
    AndAlsoExp,
)
gDSL::RExp_strategy = st.builds(
    gDSL::RExp,
)
OrElseExp_strategy = st.builds(
    OrElseExp,
)
gDSL::AndAlsoExp_strategy = st.builds(
    gDSL::AndAlsoExp,
)
ClosedExp_strategy = st.builds(
    ClosedExp,
)
gDSL::OrElseExp_strategy = st.builds(
    gDSL::OrElseExp,
)
gDSL::MonadicExp_strategy = st.builds(
    gDSL::MonadicExp,
    name=
        safe_text
)
CaseExp_strategy = st.builds(
    CaseExp,
)
gDSL::PAT_strategy = st.builds(
    gDSL::PAT,
    uscore=
        safe_text,
    int=
        safe_text,
    id=
        safe_text,
    bitpat=
        safe_text
)
gDSL::ClosedExp_strategy = st.builds(
    gDSL::ClosedExp,
)
gDSL::CaseExp_strategy = st.builds(
    gDSL::CaseExp,
    name=
        safe_text
)
gDSL::TyElement_strategy = st.builds(
    gDSL::TyElement,
    name=
        safe_text
)
gDSL::TyBind_strategy = st.builds(
    gDSL::TyBind,
    name=
        safe_text
)
gDSL::CONS_strategy = st.builds(
    gDSL::CONS,
    conName=
        safe_text
)
gDSL::Exp_strategy = st.builds(
    gDSL::Exp,
    mid=
        safe_text
)
gDSL::Ty_strategy = st.builds(
    gDSL::Ty,
    value=
        safe_text,
    type=
        safe_text
)
gDSL::TyVars_strategy = st.builds(
    gDSL::TyVars,
)
Decl_strategy = st.builds(
    Decl,
)
gDSL::Val_strategy = st.builds(
    gDSL::Val,
    name=
        safe_text,
    attr=
        safe_text,
    mid=
        safe_text,
    decPat=
        safe_text
)
gDSL::Type_strategy = st.builds(
    gDSL::Type,
    name=
        safe_text
)
gDSL::DeclExport_strategy = st.builds(
    gDSL::DeclExport,
)
gDSL::Decl_strategy = st.builds(
    gDSL::Decl,
)
gDSL::Model_strategy = st.builds(
    gDSL::Model,
)
gDSL::ConDecl_strategy = st.builds(
    gDSL::ConDecl,
)

@given(instance=gDSL::ValueDecl_strategy)
@settings(max_examples=50)
def test_gdsl::valuedecl_instantiation(instance):
    assert isinstance(instance, gDSL::ValueDecl)

@given(instance=gDSL::ValueDecl_strategy)
def test_gdsl::valuedecl_ids_type(instance):
    assert isinstance(instance.ids, str)


@given(instance=gDSL::ValueDecl_strategy)
def test_gdsl::valuedecl_ids_setter(instance):
    original = instance.ids
    instance.ids = original
    assert instance.ids == original

@given(instance=gDSL::ValueDecl_strategy)
def test_gdsl::valuedecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gDSL::ValueDecl_strategy)
def test_gdsl::valuedecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gDSL::Field_strategy)
@settings(max_examples=50)
def test_gdsl::field_instantiation(instance):
    assert isinstance(instance, gDSL::Field)

@given(instance=gDSL::Field_strategy)
def test_gdsl::field_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gDSL::Field_strategy)
def test_gdsl::field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ApplyExp_strategy)
@settings(max_examples=50)
def test_applyexp_instantiation(instance):
    assert isinstance(instance, ApplyExp)

@given(instance=gDSL::Args_strategy)
@settings(max_examples=50)
def test_gdsl::args_instantiation(instance):
    assert isinstance(instance, gDSL::Args)

@given(instance=gDSL::AtomicExp_strategy)
@settings(max_examples=50)
def test_gdsl::atomicexp_instantiation(instance):
    assert isinstance(instance, gDSL::AtomicExp)

@given(instance=gDSL::AtomicExp_strategy)
def test_gdsl::atomicexp_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=gDSL::AtomicExp_strategy)
def test_gdsl::atomicexp_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=SelectExp_strategy)
@settings(max_examples=50)
def test_selectexp_instantiation(instance):
    assert isinstance(instance, SelectExp)

@given(instance=gDSL::ApplyExp_strategy)
@settings(max_examples=50)
def test_gdsl::applyexp_instantiation(instance):
    assert isinstance(instance, gDSL::ApplyExp)

@given(instance=MExp_strategy)
@settings(max_examples=50)
def test_mexp_instantiation(instance):
    assert isinstance(instance, MExp)

@given(instance=gDSL::SelectExp_strategy)
@settings(max_examples=50)
def test_gdsl::selectexp_instantiation(instance):
    assert isinstance(instance, gDSL::SelectExp)

@given(instance=gDSL::SelectExp_strategy)
def test_gdsl::selectexp_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=gDSL::SelectExp_strategy)
def test_gdsl::selectexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=AExp_strategy)
@settings(max_examples=50)
def test_aexp_instantiation(instance):
    assert isinstance(instance, AExp)

@given(instance=gDSL::MExp_strategy)
@settings(max_examples=50)
def test_gdsl::mexp_instantiation(instance):
    assert isinstance(instance, gDSL::MExp)

@given(instance=gDSL::MExp_strategy)
def test_gdsl::mexp_sign_type(instance):
    assert isinstance(instance.sign, str)


@given(instance=gDSL::MExp_strategy)
def test_gdsl::mexp_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=RExp_strategy)
@settings(max_examples=50)
def test_rexp_instantiation(instance):
    assert isinstance(instance, RExp)

@given(instance=gDSL::AExp_strategy)
@settings(max_examples=50)
def test_gdsl::aexp_instantiation(instance):
    assert isinstance(instance, gDSL::AExp)

@given(instance=gDSL::AExp_strategy)
def test_gdsl::aexp_sym_type(instance):
    assert isinstance(instance.sym, str)


@given(instance=gDSL::AExp_strategy)
def test_gdsl::aexp_sym_setter(instance):
    original = instance.sym
    instance.sym = original
    assert instance.sym == original

@given(instance=AndAlsoExp_strategy)
@settings(max_examples=50)
def test_andalsoexp_instantiation(instance):
    assert isinstance(instance, AndAlsoExp)

@given(instance=gDSL::RExp_strategy)
@settings(max_examples=50)
def test_gdsl::rexp_instantiation(instance):
    assert isinstance(instance, gDSL::RExp)

@given(instance=OrElseExp_strategy)
@settings(max_examples=50)
def test_orelseexp_instantiation(instance):
    assert isinstance(instance, OrElseExp)

@given(instance=gDSL::AndAlsoExp_strategy)
@settings(max_examples=50)
def test_gdsl::andalsoexp_instantiation(instance):
    assert isinstance(instance, gDSL::AndAlsoExp)

@given(instance=ClosedExp_strategy)
@settings(max_examples=50)
def test_closedexp_instantiation(instance):
    assert isinstance(instance, ClosedExp)

@given(instance=gDSL::OrElseExp_strategy)
@settings(max_examples=50)
def test_gdsl::orelseexp_instantiation(instance):
    assert isinstance(instance, gDSL::OrElseExp)

@given(instance=gDSL::MonadicExp_strategy)
@settings(max_examples=50)
def test_gdsl::monadicexp_instantiation(instance):
    assert isinstance(instance, gDSL::MonadicExp)

@given(instance=gDSL::MonadicExp_strategy)
def test_gdsl::monadicexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gDSL::MonadicExp_strategy)
def test_gdsl::monadicexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CaseExp_strategy)
@settings(max_examples=50)
def test_caseexp_instantiation(instance):
    assert isinstance(instance, CaseExp)

@given(instance=gDSL::PAT_strategy)
@settings(max_examples=50)
def test_gdsl::pat_instantiation(instance):
    assert isinstance(instance, gDSL::PAT)

@given(instance=gDSL::PAT_strategy)
def test_gdsl::pat_uscore_type(instance):
    assert isinstance(instance.uscore, str)


@given(instance=gDSL::PAT_strategy)
def test_gdsl::pat_uscore_setter(instance):
    original = instance.uscore
    instance.uscore = original
    assert instance.uscore == original

@given(instance=gDSL::PAT_strategy)
def test_gdsl::pat_int_type(instance):
    assert isinstance(instance.int, str)


@given(instance=gDSL::PAT_strategy)
def test_gdsl::pat_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original

@given(instance=gDSL::PAT_strategy)
def test_gdsl::pat_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=gDSL::PAT_strategy)
def test_gdsl::pat_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=gDSL::PAT_strategy)
def test_gdsl::pat_bitpat_type(instance):
    assert isinstance(instance.bitpat, str)


@given(instance=gDSL::PAT_strategy)
def test_gdsl::pat_bitpat_setter(instance):
    original = instance.bitpat
    instance.bitpat = original
    assert instance.bitpat == original

@given(instance=gDSL::ClosedExp_strategy)
@settings(max_examples=50)
def test_gdsl::closedexp_instantiation(instance):
    assert isinstance(instance, gDSL::ClosedExp)

@given(instance=gDSL::CaseExp_strategy)
@settings(max_examples=50)
def test_gdsl::caseexp_instantiation(instance):
    assert isinstance(instance, gDSL::CaseExp)

@given(instance=gDSL::CaseExp_strategy)
def test_gdsl::caseexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gDSL::CaseExp_strategy)
def test_gdsl::caseexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gDSL::TyElement_strategy)
@settings(max_examples=50)
def test_gdsl::tyelement_instantiation(instance):
    assert isinstance(instance, gDSL::TyElement)

@given(instance=gDSL::TyElement_strategy)
def test_gdsl::tyelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gDSL::TyElement_strategy)
def test_gdsl::tyelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gDSL::TyBind_strategy)
@settings(max_examples=50)
def test_gdsl::tybind_instantiation(instance):
    assert isinstance(instance, gDSL::TyBind)

@given(instance=gDSL::TyBind_strategy)
def test_gdsl::tybind_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gDSL::TyBind_strategy)
def test_gdsl::tybind_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gDSL::CONS_strategy)
@settings(max_examples=50)
def test_gdsl::cons_instantiation(instance):
    assert isinstance(instance, gDSL::CONS)

@given(instance=gDSL::CONS_strategy)
def test_gdsl::cons_conName_type(instance):
    assert isinstance(instance.conName, str)


@given(instance=gDSL::CONS_strategy)
def test_gdsl::cons_conName_setter(instance):
    original = instance.conName
    instance.conName = original
    assert instance.conName == original

@given(instance=gDSL::Exp_strategy)
@settings(max_examples=50)
def test_gdsl::exp_instantiation(instance):
    assert isinstance(instance, gDSL::Exp)

@given(instance=gDSL::Exp_strategy)
def test_gdsl::exp_mid_type(instance):
    assert isinstance(instance.mid, str)


@given(instance=gDSL::Exp_strategy)
def test_gdsl::exp_mid_setter(instance):
    original = instance.mid
    instance.mid = original
    assert instance.mid == original

@given(instance=gDSL::Ty_strategy)
@settings(max_examples=50)
def test_gdsl::ty_instantiation(instance):
    assert isinstance(instance, gDSL::Ty)

@given(instance=gDSL::Ty_strategy)
def test_gdsl::ty_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=gDSL::Ty_strategy)
def test_gdsl::ty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gDSL::Ty_strategy)
def test_gdsl::ty_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=gDSL::Ty_strategy)
def test_gdsl::ty_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=gDSL::TyVars_strategy)
@settings(max_examples=50)
def test_gdsl::tyvars_instantiation(instance):
    assert isinstance(instance, gDSL::TyVars)

@given(instance=Decl_strategy)
@settings(max_examples=50)
def test_decl_instantiation(instance):
    assert isinstance(instance, Decl)

@given(instance=gDSL::Val_strategy)
@settings(max_examples=50)
def test_gdsl::val_instantiation(instance):
    assert isinstance(instance, gDSL::Val)

@given(instance=gDSL::Val_strategy)
def test_gdsl::val_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gDSL::Val_strategy)
def test_gdsl::val_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gDSL::Val_strategy)
def test_gdsl::val_attr_type(instance):
    assert isinstance(instance.attr, str)


@given(instance=gDSL::Val_strategy)
def test_gdsl::val_attr_setter(instance):
    original = instance.attr
    instance.attr = original
    assert instance.attr == original

@given(instance=gDSL::Val_strategy)
def test_gdsl::val_mid_type(instance):
    assert isinstance(instance.mid, str)


@given(instance=gDSL::Val_strategy)
def test_gdsl::val_mid_setter(instance):
    original = instance.mid
    instance.mid = original
    assert instance.mid == original

@given(instance=gDSL::Val_strategy)
def test_gdsl::val_decPat_type(instance):
    assert isinstance(instance.decPat, str)


@given(instance=gDSL::Val_strategy)
def test_gdsl::val_decPat_setter(instance):
    original = instance.decPat
    instance.decPat = original
    assert instance.decPat == original

@given(instance=gDSL::Type_strategy)
@settings(max_examples=50)
def test_gdsl::type_instantiation(instance):
    assert isinstance(instance, gDSL::Type)

@given(instance=gDSL::Type_strategy)
def test_gdsl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gDSL::Type_strategy)
def test_gdsl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gDSL::DeclExport_strategy)
@settings(max_examples=50)
def test_gdsl::declexport_instantiation(instance):
    assert isinstance(instance, gDSL::DeclExport)

@given(instance=gDSL::Decl_strategy)
@settings(max_examples=50)
def test_gdsl::decl_instantiation(instance):
    assert isinstance(instance, gDSL::Decl)

@given(instance=gDSL::Model_strategy)
@settings(max_examples=50)
def test_gdsl::model_instantiation(instance):
    assert isinstance(instance, gDSL::Model)

@given(instance=gDSL::ConDecl_strategy)
@settings(max_examples=50)
def test_gdsl::condecl_instantiation(instance):
    assert isinstance(instance, gDSL::ConDecl)
