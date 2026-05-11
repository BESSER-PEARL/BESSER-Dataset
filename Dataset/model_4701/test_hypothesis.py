import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::Field,
    Expr,
    TopLevelCmd,
    myDsl::Not,
    myDsl::App,
    myDsl::Let,
    myDsl::CmpOpLess,
    myDsl::ArithOpPlus,
    myDsl::ArithOpTimes,
    myDsl::BoolOpAnd,
    myDsl::ArithOpMinus,
    myDsl::With,
    myDsl::BoolOpOr,
    myDsl::ArithOpRemainder,
    myDsl::CmpOpUnequal,
    myDsl::CmpOpEqual,
    myDsl::BObject,
    myDsl::Bool,
    myDsl::Var,
    myDsl::Fun,
    myDsl::If,
    myDsl::Skip,
    myDsl::Int,
    myDsl::Assign,
    myDsl::Seq,
    myDsl::Project,
    myDsl::This,
    myDsl::ArithOpDivide,
    myDsl::Copy,
    myDsl::Def,
    myDsl::Expr,
    myDsl::TopLevelCmd,
    myDsl::File,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::field_is_not_abstract():
    assert not inspect.isabstract(myDsl::Field)


def test_mydsl::field_constructor_exists():
    assert callable(myDsl::Field.__init__)


def test_mydsl::field_constructor_args():
    sig = inspect.signature(myDsl::Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::field_has_name():
    assert hasattr(myDsl::Field, "name")
    descriptor = None
    for klass in myDsl::Field.__mro__:
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



def test_toplevelcmd_is_not_abstract():
    assert not inspect.isabstract(TopLevelCmd)


def test_toplevelcmd_constructor_exists():
    assert callable(TopLevelCmd.__init__)


def test_toplevelcmd_constructor_args():
    sig = inspect.signature(TopLevelCmd.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::not_is_not_abstract():
    assert not inspect.isabstract(myDsl::Not)


def test_mydsl::not_constructor_exists():
    assert callable(myDsl::Not.__init__)


def test_mydsl::not_constructor_args():
    sig = inspect.signature(myDsl::Not.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::app_is_not_abstract():
    assert not inspect.isabstract(myDsl::App)


def test_mydsl::app_constructor_exists():
    assert callable(myDsl::App.__init__)


def test_mydsl::app_constructor_args():
    sig = inspect.signature(myDsl::App.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::let_is_not_abstract():
    assert not inspect.isabstract(myDsl::Let)


def test_mydsl::let_constructor_exists():
    assert callable(myDsl::Let.__init__)


def test_mydsl::let_constructor_args():
    sig = inspect.signature(myDsl::Let.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::let_has_name():
    assert hasattr(myDsl::Let, "name")
    descriptor = None
    for klass in myDsl::Let.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::cmpopless_is_not_abstract():
    assert not inspect.isabstract(myDsl::CmpOpLess)


def test_mydsl::cmpopless_constructor_exists():
    assert callable(myDsl::CmpOpLess.__init__)


def test_mydsl::cmpopless_constructor_args():
    sig = inspect.signature(myDsl::CmpOpLess.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::arithopplus_is_not_abstract():
    assert not inspect.isabstract(myDsl::ArithOpPlus)


def test_mydsl::arithopplus_constructor_exists():
    assert callable(myDsl::ArithOpPlus.__init__)


def test_mydsl::arithopplus_constructor_args():
    sig = inspect.signature(myDsl::ArithOpPlus.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::arithoptimes_is_not_abstract():
    assert not inspect.isabstract(myDsl::ArithOpTimes)


def test_mydsl::arithoptimes_constructor_exists():
    assert callable(myDsl::ArithOpTimes.__init__)


def test_mydsl::arithoptimes_constructor_args():
    sig = inspect.signature(myDsl::ArithOpTimes.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::boolopand_is_not_abstract():
    assert not inspect.isabstract(myDsl::BoolOpAnd)


def test_mydsl::boolopand_constructor_exists():
    assert callable(myDsl::BoolOpAnd.__init__)


def test_mydsl::boolopand_constructor_args():
    sig = inspect.signature(myDsl::BoolOpAnd.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::arithopminus_is_not_abstract():
    assert not inspect.isabstract(myDsl::ArithOpMinus)


def test_mydsl::arithopminus_constructor_exists():
    assert callable(myDsl::ArithOpMinus.__init__)


def test_mydsl::arithopminus_constructor_args():
    sig = inspect.signature(myDsl::ArithOpMinus.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::with_is_not_abstract():
    assert not inspect.isabstract(myDsl::With)


def test_mydsl::with_constructor_exists():
    assert callable(myDsl::With.__init__)


def test_mydsl::with_constructor_args():
    sig = inspect.signature(myDsl::With.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::boolopor_is_not_abstract():
    assert not inspect.isabstract(myDsl::BoolOpOr)


def test_mydsl::boolopor_constructor_exists():
    assert callable(myDsl::BoolOpOr.__init__)


def test_mydsl::boolopor_constructor_args():
    sig = inspect.signature(myDsl::BoolOpOr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::arithopremainder_is_not_abstract():
    assert not inspect.isabstract(myDsl::ArithOpRemainder)


def test_mydsl::arithopremainder_constructor_exists():
    assert callable(myDsl::ArithOpRemainder.__init__)


def test_mydsl::arithopremainder_constructor_args():
    sig = inspect.signature(myDsl::ArithOpRemainder.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::cmpopunequal_is_not_abstract():
    assert not inspect.isabstract(myDsl::CmpOpUnequal)


def test_mydsl::cmpopunequal_constructor_exists():
    assert callable(myDsl::CmpOpUnequal.__init__)


def test_mydsl::cmpopunequal_constructor_args():
    sig = inspect.signature(myDsl::CmpOpUnequal.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::cmpopequal_is_not_abstract():
    assert not inspect.isabstract(myDsl::CmpOpEqual)


def test_mydsl::cmpopequal_constructor_exists():
    assert callable(myDsl::CmpOpEqual.__init__)


def test_mydsl::cmpopequal_constructor_args():
    sig = inspect.signature(myDsl::CmpOpEqual.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::bobject_is_not_abstract():
    assert not inspect.isabstract(myDsl::BObject)


def test_mydsl::bobject_constructor_exists():
    assert callable(myDsl::BObject.__init__)


def test_mydsl::bobject_constructor_args():
    sig = inspect.signature(myDsl::BObject.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::bool_is_not_abstract():
    assert not inspect.isabstract(myDsl::Bool)


def test_mydsl::bool_constructor_exists():
    assert callable(myDsl::Bool.__init__)


def test_mydsl::bool_constructor_args():
    sig = inspect.signature(myDsl::Bool.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl::bool_has_value():
    assert hasattr(myDsl::Bool, "value")
    descriptor = None
    for klass in myDsl::Bool.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::var_is_not_abstract():
    assert not inspect.isabstract(myDsl::Var)


def test_mydsl::var_constructor_exists():
    assert callable(myDsl::Var.__init__)


def test_mydsl::var_constructor_args():
    sig = inspect.signature(myDsl::Var.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::var_has_name():
    assert hasattr(myDsl::Var, "name")
    descriptor = None
    for klass in myDsl::Var.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::fun_is_not_abstract():
    assert not inspect.isabstract(myDsl::Fun)


def test_mydsl::fun_constructor_exists():
    assert callable(myDsl::Fun.__init__)


def test_mydsl::fun_constructor_args():
    sig = inspect.signature(myDsl::Fun.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::fun_has_name():
    assert hasattr(myDsl::Fun, "name")
    descriptor = None
    for klass in myDsl::Fun.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::if_is_not_abstract():
    assert not inspect.isabstract(myDsl::If)


def test_mydsl::if_constructor_exists():
    assert callable(myDsl::If.__init__)


def test_mydsl::if_constructor_args():
    sig = inspect.signature(myDsl::If.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::skip_is_not_abstract():
    assert not inspect.isabstract(myDsl::Skip)


def test_mydsl::skip_constructor_exists():
    assert callable(myDsl::Skip.__init__)


def test_mydsl::skip_constructor_args():
    sig = inspect.signature(myDsl::Skip.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::int_is_not_abstract():
    assert not inspect.isabstract(myDsl::Int)


def test_mydsl::int_constructor_exists():
    assert callable(myDsl::Int.__init__)


def test_mydsl::int_constructor_args():
    sig = inspect.signature(myDsl::Int.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl::int_has_value():
    assert hasattr(myDsl::Int, "value")
    descriptor = None
    for klass in myDsl::Int.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::assign_is_not_abstract():
    assert not inspect.isabstract(myDsl::Assign)


def test_mydsl::assign_constructor_exists():
    assert callable(myDsl::Assign.__init__)


def test_mydsl::assign_constructor_args():
    sig = inspect.signature(myDsl::Assign.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::assign_has_name():
    assert hasattr(myDsl::Assign, "name")
    descriptor = None
    for klass in myDsl::Assign.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::seq_is_not_abstract():
    assert not inspect.isabstract(myDsl::Seq)


def test_mydsl::seq_constructor_exists():
    assert callable(myDsl::Seq.__init__)


def test_mydsl::seq_constructor_args():
    sig = inspect.signature(myDsl::Seq.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::project_is_not_abstract():
    assert not inspect.isabstract(myDsl::Project)


def test_mydsl::project_constructor_exists():
    assert callable(myDsl::Project.__init__)


def test_mydsl::project_constructor_args():
    sig = inspect.signature(myDsl::Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::project_has_name():
    assert hasattr(myDsl::Project, "name")
    descriptor = None
    for klass in myDsl::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::this_is_not_abstract():
    assert not inspect.isabstract(myDsl::This)


def test_mydsl::this_constructor_exists():
    assert callable(myDsl::This.__init__)


def test_mydsl::this_constructor_args():
    sig = inspect.signature(myDsl::This.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::arithopdivide_is_not_abstract():
    assert not inspect.isabstract(myDsl::ArithOpDivide)


def test_mydsl::arithopdivide_constructor_exists():
    assert callable(myDsl::ArithOpDivide.__init__)


def test_mydsl::arithopdivide_constructor_args():
    sig = inspect.signature(myDsl::ArithOpDivide.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::copy_is_not_abstract():
    assert not inspect.isabstract(myDsl::Copy)


def test_mydsl::copy_constructor_exists():
    assert callable(myDsl::Copy.__init__)


def test_mydsl::copy_constructor_args():
    sig = inspect.signature(myDsl::Copy.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::def_is_not_abstract():
    assert not inspect.isabstract(myDsl::Def)


def test_mydsl::def_constructor_exists():
    assert callable(myDsl::Def.__init__)


def test_mydsl::def_constructor_args():
    sig = inspect.signature(myDsl::Def.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::def_has_name():
    assert hasattr(myDsl::Def, "name")
    descriptor = None
    for klass in myDsl::Def.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::expr_is_not_abstract():
    assert not inspect.isabstract(myDsl::Expr)


def test_mydsl::expr_constructor_exists():
    assert callable(myDsl::Expr.__init__)


def test_mydsl::expr_constructor_args():
    sig = inspect.signature(myDsl::Expr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::toplevelcmd_is_not_abstract():
    assert not inspect.isabstract(myDsl::TopLevelCmd)


def test_mydsl::toplevelcmd_constructor_exists():
    assert callable(myDsl::TopLevelCmd.__init__)


def test_mydsl::toplevelcmd_constructor_args():
    sig = inspect.signature(myDsl::TopLevelCmd.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::file_is_not_abstract():
    assert not inspect.isabstract(myDsl::File)


def test_mydsl::file_constructor_exists():
    assert callable(myDsl::File.__init__)


def test_mydsl::file_constructor_args():
    sig = inspect.signature(myDsl::File.__init__)
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
myDsl::Field_strategy = st.builds(
    myDsl::Field,
    name=
        safe_text
)
Expr_strategy = st.builds(
    Expr,
)
TopLevelCmd_strategy = st.builds(
    TopLevelCmd,
)
myDsl::Not_strategy = st.builds(
    myDsl::Not,
)
myDsl::App_strategy = st.builds(
    myDsl::App,
)
myDsl::Let_strategy = st.builds(
    myDsl::Let,
    name=
        safe_text
)
myDsl::CmpOpLess_strategy = st.builds(
    myDsl::CmpOpLess,
)
myDsl::ArithOpPlus_strategy = st.builds(
    myDsl::ArithOpPlus,
)
myDsl::ArithOpTimes_strategy = st.builds(
    myDsl::ArithOpTimes,
)
myDsl::BoolOpAnd_strategy = st.builds(
    myDsl::BoolOpAnd,
)
myDsl::ArithOpMinus_strategy = st.builds(
    myDsl::ArithOpMinus,
)
myDsl::With_strategy = st.builds(
    myDsl::With,
)
myDsl::BoolOpOr_strategy = st.builds(
    myDsl::BoolOpOr,
)
myDsl::ArithOpRemainder_strategy = st.builds(
    myDsl::ArithOpRemainder,
)
myDsl::CmpOpUnequal_strategy = st.builds(
    myDsl::CmpOpUnequal,
)
myDsl::CmpOpEqual_strategy = st.builds(
    myDsl::CmpOpEqual,
)
myDsl::BObject_strategy = st.builds(
    myDsl::BObject,
)
myDsl::Bool_strategy = st.builds(
    myDsl::Bool,
    value=
        st.booleans()
)
myDsl::Var_strategy = st.builds(
    myDsl::Var,
    name=
        safe_text
)
myDsl::Fun_strategy = st.builds(
    myDsl::Fun,
    name=
        safe_text
)
myDsl::If_strategy = st.builds(
    myDsl::If,
)
myDsl::Skip_strategy = st.builds(
    myDsl::Skip,
)
myDsl::Int_strategy = st.builds(
    myDsl::Int,
    value=
        st.integers()
)
myDsl::Assign_strategy = st.builds(
    myDsl::Assign,
    name=
        safe_text
)
myDsl::Seq_strategy = st.builds(
    myDsl::Seq,
)
myDsl::Project_strategy = st.builds(
    myDsl::Project,
    name=
        safe_text
)
myDsl::This_strategy = st.builds(
    myDsl::This,
)
myDsl::ArithOpDivide_strategy = st.builds(
    myDsl::ArithOpDivide,
)
myDsl::Copy_strategy = st.builds(
    myDsl::Copy,
)
myDsl::Def_strategy = st.builds(
    myDsl::Def,
    name=
        safe_text
)
myDsl::Expr_strategy = st.builds(
    myDsl::Expr,
)
myDsl::TopLevelCmd_strategy = st.builds(
    myDsl::TopLevelCmd,
)
myDsl::File_strategy = st.builds(
    myDsl::File,
)

@given(instance=myDsl::Field_strategy)
@settings(max_examples=50)
def test_mydsl::field_instantiation(instance):
    assert isinstance(instance, myDsl::Field)

@given(instance=myDsl::Field_strategy)
def test_mydsl::field_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Field_strategy)
def test_mydsl::field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=TopLevelCmd_strategy)
@settings(max_examples=50)
def test_toplevelcmd_instantiation(instance):
    assert isinstance(instance, TopLevelCmd)

@given(instance=myDsl::Not_strategy)
@settings(max_examples=50)
def test_mydsl::not_instantiation(instance):
    assert isinstance(instance, myDsl::Not)

@given(instance=myDsl::App_strategy)
@settings(max_examples=50)
def test_mydsl::app_instantiation(instance):
    assert isinstance(instance, myDsl::App)

@given(instance=myDsl::Let_strategy)
@settings(max_examples=50)
def test_mydsl::let_instantiation(instance):
    assert isinstance(instance, myDsl::Let)

@given(instance=myDsl::Let_strategy)
def test_mydsl::let_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Let_strategy)
def test_mydsl::let_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::CmpOpLess_strategy)
@settings(max_examples=50)
def test_mydsl::cmpopless_instantiation(instance):
    assert isinstance(instance, myDsl::CmpOpLess)

@given(instance=myDsl::ArithOpPlus_strategy)
@settings(max_examples=50)
def test_mydsl::arithopplus_instantiation(instance):
    assert isinstance(instance, myDsl::ArithOpPlus)

@given(instance=myDsl::ArithOpTimes_strategy)
@settings(max_examples=50)
def test_mydsl::arithoptimes_instantiation(instance):
    assert isinstance(instance, myDsl::ArithOpTimes)

@given(instance=myDsl::BoolOpAnd_strategy)
@settings(max_examples=50)
def test_mydsl::boolopand_instantiation(instance):
    assert isinstance(instance, myDsl::BoolOpAnd)

@given(instance=myDsl::ArithOpMinus_strategy)
@settings(max_examples=50)
def test_mydsl::arithopminus_instantiation(instance):
    assert isinstance(instance, myDsl::ArithOpMinus)

@given(instance=myDsl::With_strategy)
@settings(max_examples=50)
def test_mydsl::with_instantiation(instance):
    assert isinstance(instance, myDsl::With)

@given(instance=myDsl::BoolOpOr_strategy)
@settings(max_examples=50)
def test_mydsl::boolopor_instantiation(instance):
    assert isinstance(instance, myDsl::BoolOpOr)

@given(instance=myDsl::ArithOpRemainder_strategy)
@settings(max_examples=50)
def test_mydsl::arithopremainder_instantiation(instance):
    assert isinstance(instance, myDsl::ArithOpRemainder)

@given(instance=myDsl::CmpOpUnequal_strategy)
@settings(max_examples=50)
def test_mydsl::cmpopunequal_instantiation(instance):
    assert isinstance(instance, myDsl::CmpOpUnequal)

@given(instance=myDsl::CmpOpEqual_strategy)
@settings(max_examples=50)
def test_mydsl::cmpopequal_instantiation(instance):
    assert isinstance(instance, myDsl::CmpOpEqual)

@given(instance=myDsl::BObject_strategy)
@settings(max_examples=50)
def test_mydsl::bobject_instantiation(instance):
    assert isinstance(instance, myDsl::BObject)

@given(instance=myDsl::Bool_strategy)
@settings(max_examples=50)
def test_mydsl::bool_instantiation(instance):
    assert isinstance(instance, myDsl::Bool)

@given(instance=myDsl::Bool_strategy)
def test_mydsl::bool_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=myDsl::Bool_strategy)
def test_mydsl::bool_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl::Var_strategy)
@settings(max_examples=50)
def test_mydsl::var_instantiation(instance):
    assert isinstance(instance, myDsl::Var)

@given(instance=myDsl::Var_strategy)
def test_mydsl::var_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Var_strategy)
def test_mydsl::var_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Fun_strategy)
@settings(max_examples=50)
def test_mydsl::fun_instantiation(instance):
    assert isinstance(instance, myDsl::Fun)

@given(instance=myDsl::Fun_strategy)
def test_mydsl::fun_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Fun_strategy)
def test_mydsl::fun_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::If_strategy)
@settings(max_examples=50)
def test_mydsl::if_instantiation(instance):
    assert isinstance(instance, myDsl::If)

@given(instance=myDsl::Skip_strategy)
@settings(max_examples=50)
def test_mydsl::skip_instantiation(instance):
    assert isinstance(instance, myDsl::Skip)

@given(instance=myDsl::Int_strategy)
@settings(max_examples=50)
def test_mydsl::int_instantiation(instance):
    assert isinstance(instance, myDsl::Int)

@given(instance=myDsl::Int_strategy)
def test_mydsl::int_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=myDsl::Int_strategy)
def test_mydsl::int_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl::Assign_strategy)
@settings(max_examples=50)
def test_mydsl::assign_instantiation(instance):
    assert isinstance(instance, myDsl::Assign)

@given(instance=myDsl::Assign_strategy)
def test_mydsl::assign_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Assign_strategy)
def test_mydsl::assign_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Seq_strategy)
@settings(max_examples=50)
def test_mydsl::seq_instantiation(instance):
    assert isinstance(instance, myDsl::Seq)

@given(instance=myDsl::Project_strategy)
@settings(max_examples=50)
def test_mydsl::project_instantiation(instance):
    assert isinstance(instance, myDsl::Project)

@given(instance=myDsl::Project_strategy)
def test_mydsl::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Project_strategy)
def test_mydsl::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::This_strategy)
@settings(max_examples=50)
def test_mydsl::this_instantiation(instance):
    assert isinstance(instance, myDsl::This)

@given(instance=myDsl::ArithOpDivide_strategy)
@settings(max_examples=50)
def test_mydsl::arithopdivide_instantiation(instance):
    assert isinstance(instance, myDsl::ArithOpDivide)

@given(instance=myDsl::Copy_strategy)
@settings(max_examples=50)
def test_mydsl::copy_instantiation(instance):
    assert isinstance(instance, myDsl::Copy)

@given(instance=myDsl::Def_strategy)
@settings(max_examples=50)
def test_mydsl::def_instantiation(instance):
    assert isinstance(instance, myDsl::Def)

@given(instance=myDsl::Def_strategy)
def test_mydsl::def_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Def_strategy)
def test_mydsl::def_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Expr_strategy)
@settings(max_examples=50)
def test_mydsl::expr_instantiation(instance):
    assert isinstance(instance, myDsl::Expr)

@given(instance=myDsl::TopLevelCmd_strategy)
@settings(max_examples=50)
def test_mydsl::toplevelcmd_instantiation(instance):
    assert isinstance(instance, myDsl::TopLevelCmd)

@given(instance=myDsl::File_strategy)
@settings(max_examples=50)
def test_mydsl::file_instantiation(instance):
    assert isinstance(instance, myDsl::File)
