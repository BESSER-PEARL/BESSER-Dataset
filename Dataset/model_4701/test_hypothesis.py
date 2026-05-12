import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl_Field,
    Expr,
    TopLevelCmd,
    myDsl_Var,
    myDsl_Not,
    myDsl_ArithOpRemainder,
    myDsl_Let,
    myDsl_Bool,
    myDsl_CmpOpUnequal,
    myDsl_BoolOpOr,
    myDsl_Project,
    myDsl_Copy,
    myDsl_Int,
    myDsl_BoolOpAnd,
    myDsl_This,
    myDsl_Assign,
    myDsl_CmpOpLess,
    myDsl_Seq,
    myDsl_With,
    myDsl_BObject,
    myDsl_ArithOpMinus,
    myDsl_CmpOpEqual,
    myDsl_Fun,
    myDsl_If,
    myDsl_ArithOpTimes,
    myDsl_App,
    myDsl_ArithOpDivide,
    myDsl_Skip,
    myDsl_ArithOpPlus,
    myDsl_Def,
    myDsl_Expr,
    myDsl_TopLevelCmd,
    myDsl_File,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_field_is_not_abstract():
    assert not inspect.isabstract(myDsl_Field)


def test_mydsl_field_constructor_exists():
    assert callable(myDsl_Field.__init__)


def test_mydsl_field_constructor_args():
    sig = inspect.signature(myDsl_Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_field_has_name():
    assert hasattr(myDsl_Field, "name")
    descriptor = None
    for klass in myDsl_Field.__mro__:
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



def test_mydsl_var_is_not_abstract():
    assert not inspect.isabstract(myDsl_Var)


def test_mydsl_var_constructor_exists():
    assert callable(myDsl_Var.__init__)


def test_mydsl_var_constructor_args():
    sig = inspect.signature(myDsl_Var.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_var_has_name():
    assert hasattr(myDsl_Var, "name")
    descriptor = None
    for klass in myDsl_Var.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_not_is_not_abstract():
    assert not inspect.isabstract(myDsl_Not)


def test_mydsl_not_constructor_exists():
    assert callable(myDsl_Not.__init__)


def test_mydsl_not_constructor_args():
    sig = inspect.signature(myDsl_Not.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_arithopremainder_is_not_abstract():
    assert not inspect.isabstract(myDsl_ArithOpRemainder)


def test_mydsl_arithopremainder_constructor_exists():
    assert callable(myDsl_ArithOpRemainder.__init__)


def test_mydsl_arithopremainder_constructor_args():
    sig = inspect.signature(myDsl_ArithOpRemainder.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_let_is_not_abstract():
    assert not inspect.isabstract(myDsl_Let)


def test_mydsl_let_constructor_exists():
    assert callable(myDsl_Let.__init__)


def test_mydsl_let_constructor_args():
    sig = inspect.signature(myDsl_Let.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_let_has_name():
    assert hasattr(myDsl_Let, "name")
    descriptor = None
    for klass in myDsl_Let.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_bool_is_not_abstract():
    assert not inspect.isabstract(myDsl_Bool)


def test_mydsl_bool_constructor_exists():
    assert callable(myDsl_Bool.__init__)


def test_mydsl_bool_constructor_args():
    sig = inspect.signature(myDsl_Bool.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl_bool_has_value():
    assert hasattr(myDsl_Bool, "value")
    descriptor = None
    for klass in myDsl_Bool.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_cmpopunequal_is_not_abstract():
    assert not inspect.isabstract(myDsl_CmpOpUnequal)


def test_mydsl_cmpopunequal_constructor_exists():
    assert callable(myDsl_CmpOpUnequal.__init__)


def test_mydsl_cmpopunequal_constructor_args():
    sig = inspect.signature(myDsl_CmpOpUnequal.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_boolopor_is_not_abstract():
    assert not inspect.isabstract(myDsl_BoolOpOr)


def test_mydsl_boolopor_constructor_exists():
    assert callable(myDsl_BoolOpOr.__init__)


def test_mydsl_boolopor_constructor_args():
    sig = inspect.signature(myDsl_BoolOpOr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_project_is_not_abstract():
    assert not inspect.isabstract(myDsl_Project)


def test_mydsl_project_constructor_exists():
    assert callable(myDsl_Project.__init__)


def test_mydsl_project_constructor_args():
    sig = inspect.signature(myDsl_Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_project_has_name():
    assert hasattr(myDsl_Project, "name")
    descriptor = None
    for klass in myDsl_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_copy_is_not_abstract():
    assert not inspect.isabstract(myDsl_Copy)


def test_mydsl_copy_constructor_exists():
    assert callable(myDsl_Copy.__init__)


def test_mydsl_copy_constructor_args():
    sig = inspect.signature(myDsl_Copy.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_int_is_not_abstract():
    assert not inspect.isabstract(myDsl_Int)


def test_mydsl_int_constructor_exists():
    assert callable(myDsl_Int.__init__)


def test_mydsl_int_constructor_args():
    sig = inspect.signature(myDsl_Int.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl_int_has_value():
    assert hasattr(myDsl_Int, "value")
    descriptor = None
    for klass in myDsl_Int.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_boolopand_is_not_abstract():
    assert not inspect.isabstract(myDsl_BoolOpAnd)


def test_mydsl_boolopand_constructor_exists():
    assert callable(myDsl_BoolOpAnd.__init__)


def test_mydsl_boolopand_constructor_args():
    sig = inspect.signature(myDsl_BoolOpAnd.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_this_is_not_abstract():
    assert not inspect.isabstract(myDsl_This)


def test_mydsl_this_constructor_exists():
    assert callable(myDsl_This.__init__)


def test_mydsl_this_constructor_args():
    sig = inspect.signature(myDsl_This.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_assign_is_not_abstract():
    assert not inspect.isabstract(myDsl_Assign)


def test_mydsl_assign_constructor_exists():
    assert callable(myDsl_Assign.__init__)


def test_mydsl_assign_constructor_args():
    sig = inspect.signature(myDsl_Assign.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_assign_has_name():
    assert hasattr(myDsl_Assign, "name")
    descriptor = None
    for klass in myDsl_Assign.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_cmpopless_is_not_abstract():
    assert not inspect.isabstract(myDsl_CmpOpLess)


def test_mydsl_cmpopless_constructor_exists():
    assert callable(myDsl_CmpOpLess.__init__)


def test_mydsl_cmpopless_constructor_args():
    sig = inspect.signature(myDsl_CmpOpLess.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_seq_is_not_abstract():
    assert not inspect.isabstract(myDsl_Seq)


def test_mydsl_seq_constructor_exists():
    assert callable(myDsl_Seq.__init__)


def test_mydsl_seq_constructor_args():
    sig = inspect.signature(myDsl_Seq.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_with_is_not_abstract():
    assert not inspect.isabstract(myDsl_With)


def test_mydsl_with_constructor_exists():
    assert callable(myDsl_With.__init__)


def test_mydsl_with_constructor_args():
    sig = inspect.signature(myDsl_With.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_bobject_is_not_abstract():
    assert not inspect.isabstract(myDsl_BObject)


def test_mydsl_bobject_constructor_exists():
    assert callable(myDsl_BObject.__init__)


def test_mydsl_bobject_constructor_args():
    sig = inspect.signature(myDsl_BObject.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_arithopminus_is_not_abstract():
    assert not inspect.isabstract(myDsl_ArithOpMinus)


def test_mydsl_arithopminus_constructor_exists():
    assert callable(myDsl_ArithOpMinus.__init__)


def test_mydsl_arithopminus_constructor_args():
    sig = inspect.signature(myDsl_ArithOpMinus.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_cmpopequal_is_not_abstract():
    assert not inspect.isabstract(myDsl_CmpOpEqual)


def test_mydsl_cmpopequal_constructor_exists():
    assert callable(myDsl_CmpOpEqual.__init__)


def test_mydsl_cmpopequal_constructor_args():
    sig = inspect.signature(myDsl_CmpOpEqual.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_fun_is_not_abstract():
    assert not inspect.isabstract(myDsl_Fun)


def test_mydsl_fun_constructor_exists():
    assert callable(myDsl_Fun.__init__)


def test_mydsl_fun_constructor_args():
    sig = inspect.signature(myDsl_Fun.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_fun_has_name():
    assert hasattr(myDsl_Fun, "name")
    descriptor = None
    for klass in myDsl_Fun.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_if_is_not_abstract():
    assert not inspect.isabstract(myDsl_If)


def test_mydsl_if_constructor_exists():
    assert callable(myDsl_If.__init__)


def test_mydsl_if_constructor_args():
    sig = inspect.signature(myDsl_If.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_arithoptimes_is_not_abstract():
    assert not inspect.isabstract(myDsl_ArithOpTimes)


def test_mydsl_arithoptimes_constructor_exists():
    assert callable(myDsl_ArithOpTimes.__init__)


def test_mydsl_arithoptimes_constructor_args():
    sig = inspect.signature(myDsl_ArithOpTimes.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_app_is_not_abstract():
    assert not inspect.isabstract(myDsl_App)


def test_mydsl_app_constructor_exists():
    assert callable(myDsl_App.__init__)


def test_mydsl_app_constructor_args():
    sig = inspect.signature(myDsl_App.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_arithopdivide_is_not_abstract():
    assert not inspect.isabstract(myDsl_ArithOpDivide)


def test_mydsl_arithopdivide_constructor_exists():
    assert callable(myDsl_ArithOpDivide.__init__)


def test_mydsl_arithopdivide_constructor_args():
    sig = inspect.signature(myDsl_ArithOpDivide.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_skip_is_not_abstract():
    assert not inspect.isabstract(myDsl_Skip)


def test_mydsl_skip_constructor_exists():
    assert callable(myDsl_Skip.__init__)


def test_mydsl_skip_constructor_args():
    sig = inspect.signature(myDsl_Skip.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_arithopplus_is_not_abstract():
    assert not inspect.isabstract(myDsl_ArithOpPlus)


def test_mydsl_arithopplus_constructor_exists():
    assert callable(myDsl_ArithOpPlus.__init__)


def test_mydsl_arithopplus_constructor_args():
    sig = inspect.signature(myDsl_ArithOpPlus.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_def_is_not_abstract():
    assert not inspect.isabstract(myDsl_Def)


def test_mydsl_def_constructor_exists():
    assert callable(myDsl_Def.__init__)


def test_mydsl_def_constructor_args():
    sig = inspect.signature(myDsl_Def.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_def_has_name():
    assert hasattr(myDsl_Def, "name")
    descriptor = None
    for klass in myDsl_Def.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_expr_is_not_abstract():
    assert not inspect.isabstract(myDsl_Expr)


def test_mydsl_expr_constructor_exists():
    assert callable(myDsl_Expr.__init__)


def test_mydsl_expr_constructor_args():
    sig = inspect.signature(myDsl_Expr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_toplevelcmd_is_not_abstract():
    assert not inspect.isabstract(myDsl_TopLevelCmd)


def test_mydsl_toplevelcmd_constructor_exists():
    assert callable(myDsl_TopLevelCmd.__init__)


def test_mydsl_toplevelcmd_constructor_args():
    sig = inspect.signature(myDsl_TopLevelCmd.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_file_is_not_abstract():
    assert not inspect.isabstract(myDsl_File)


def test_mydsl_file_constructor_exists():
    assert callable(myDsl_File.__init__)


def test_mydsl_file_constructor_args():
    sig = inspect.signature(myDsl_File.__init__)
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
myDsl_Field_strategy = st.builds(
    myDsl_Field,
    name=
        safe_text
)
Expr_strategy = st.builds(
    Expr,
)
TopLevelCmd_strategy = st.builds(
    TopLevelCmd,
)
myDsl_Var_strategy = st.builds(
    myDsl_Var,
    name=
        safe_text
)
myDsl_Not_strategy = st.builds(
    myDsl_Not,
)
myDsl_ArithOpRemainder_strategy = st.builds(
    myDsl_ArithOpRemainder,
)
myDsl_Let_strategy = st.builds(
    myDsl_Let,
    name=
        safe_text
)
myDsl_Bool_strategy = st.builds(
    myDsl_Bool,
    value=
        st.booleans()
)
myDsl_CmpOpUnequal_strategy = st.builds(
    myDsl_CmpOpUnequal,
)
myDsl_BoolOpOr_strategy = st.builds(
    myDsl_BoolOpOr,
)
myDsl_Project_strategy = st.builds(
    myDsl_Project,
    name=
        safe_text
)
myDsl_Copy_strategy = st.builds(
    myDsl_Copy,
)
myDsl_Int_strategy = st.builds(
    myDsl_Int,
    value=
        st.integers()
)
myDsl_BoolOpAnd_strategy = st.builds(
    myDsl_BoolOpAnd,
)
myDsl_This_strategy = st.builds(
    myDsl_This,
)
myDsl_Assign_strategy = st.builds(
    myDsl_Assign,
    name=
        safe_text
)
myDsl_CmpOpLess_strategy = st.builds(
    myDsl_CmpOpLess,
)
myDsl_Seq_strategy = st.builds(
    myDsl_Seq,
)
myDsl_With_strategy = st.builds(
    myDsl_With,
)
myDsl_BObject_strategy = st.builds(
    myDsl_BObject,
)
myDsl_ArithOpMinus_strategy = st.builds(
    myDsl_ArithOpMinus,
)
myDsl_CmpOpEqual_strategy = st.builds(
    myDsl_CmpOpEqual,
)
myDsl_Fun_strategy = st.builds(
    myDsl_Fun,
    name=
        safe_text
)
myDsl_If_strategy = st.builds(
    myDsl_If,
)
myDsl_ArithOpTimes_strategy = st.builds(
    myDsl_ArithOpTimes,
)
myDsl_App_strategy = st.builds(
    myDsl_App,
)
myDsl_ArithOpDivide_strategy = st.builds(
    myDsl_ArithOpDivide,
)
myDsl_Skip_strategy = st.builds(
    myDsl_Skip,
)
myDsl_ArithOpPlus_strategy = st.builds(
    myDsl_ArithOpPlus,
)
myDsl_Def_strategy = st.builds(
    myDsl_Def,
    name=
        safe_text
)
myDsl_Expr_strategy = st.builds(
    myDsl_Expr,
)
myDsl_TopLevelCmd_strategy = st.builds(
    myDsl_TopLevelCmd,
)
myDsl_File_strategy = st.builds(
    myDsl_File,
)

@given(instance=myDsl_Field_strategy)
@settings(max_examples=50)
def test_mydsl_field_instantiation(instance):
    assert isinstance(instance, myDsl_Field)



@given(instance=myDsl_Field_strategy)
def test_mydsl_field_name_setter(instance):
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

@given(instance=myDsl_Var_strategy)
@settings(max_examples=50)
def test_mydsl_var_instantiation(instance):
    assert isinstance(instance, myDsl_Var)



@given(instance=myDsl_Var_strategy)
def test_mydsl_var_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Not_strategy)
@settings(max_examples=50)
def test_mydsl_not_instantiation(instance):
    assert isinstance(instance, myDsl_Not)

@given(instance=myDsl_ArithOpRemainder_strategy)
@settings(max_examples=50)
def test_mydsl_arithopremainder_instantiation(instance):
    assert isinstance(instance, myDsl_ArithOpRemainder)

@given(instance=myDsl_Let_strategy)
@settings(max_examples=50)
def test_mydsl_let_instantiation(instance):
    assert isinstance(instance, myDsl_Let)



@given(instance=myDsl_Let_strategy)
def test_mydsl_let_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Bool_strategy)
@settings(max_examples=50)
def test_mydsl_bool_instantiation(instance):
    assert isinstance(instance, myDsl_Bool)



@given(instance=myDsl_Bool_strategy)
def test_mydsl_bool_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl_CmpOpUnequal_strategy)
@settings(max_examples=50)
def test_mydsl_cmpopunequal_instantiation(instance):
    assert isinstance(instance, myDsl_CmpOpUnequal)

@given(instance=myDsl_BoolOpOr_strategy)
@settings(max_examples=50)
def test_mydsl_boolopor_instantiation(instance):
    assert isinstance(instance, myDsl_BoolOpOr)

@given(instance=myDsl_Project_strategy)
@settings(max_examples=50)
def test_mydsl_project_instantiation(instance):
    assert isinstance(instance, myDsl_Project)



@given(instance=myDsl_Project_strategy)
def test_mydsl_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Copy_strategy)
@settings(max_examples=50)
def test_mydsl_copy_instantiation(instance):
    assert isinstance(instance, myDsl_Copy)

@given(instance=myDsl_Int_strategy)
@settings(max_examples=50)
def test_mydsl_int_instantiation(instance):
    assert isinstance(instance, myDsl_Int)



@given(instance=myDsl_Int_strategy)
def test_mydsl_int_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl_BoolOpAnd_strategy)
@settings(max_examples=50)
def test_mydsl_boolopand_instantiation(instance):
    assert isinstance(instance, myDsl_BoolOpAnd)

@given(instance=myDsl_This_strategy)
@settings(max_examples=50)
def test_mydsl_this_instantiation(instance):
    assert isinstance(instance, myDsl_This)

@given(instance=myDsl_Assign_strategy)
@settings(max_examples=50)
def test_mydsl_assign_instantiation(instance):
    assert isinstance(instance, myDsl_Assign)



@given(instance=myDsl_Assign_strategy)
def test_mydsl_assign_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_CmpOpLess_strategy)
@settings(max_examples=50)
def test_mydsl_cmpopless_instantiation(instance):
    assert isinstance(instance, myDsl_CmpOpLess)

@given(instance=myDsl_Seq_strategy)
@settings(max_examples=50)
def test_mydsl_seq_instantiation(instance):
    assert isinstance(instance, myDsl_Seq)

@given(instance=myDsl_With_strategy)
@settings(max_examples=50)
def test_mydsl_with_instantiation(instance):
    assert isinstance(instance, myDsl_With)

@given(instance=myDsl_BObject_strategy)
@settings(max_examples=50)
def test_mydsl_bobject_instantiation(instance):
    assert isinstance(instance, myDsl_BObject)

@given(instance=myDsl_ArithOpMinus_strategy)
@settings(max_examples=50)
def test_mydsl_arithopminus_instantiation(instance):
    assert isinstance(instance, myDsl_ArithOpMinus)

@given(instance=myDsl_CmpOpEqual_strategy)
@settings(max_examples=50)
def test_mydsl_cmpopequal_instantiation(instance):
    assert isinstance(instance, myDsl_CmpOpEqual)

@given(instance=myDsl_Fun_strategy)
@settings(max_examples=50)
def test_mydsl_fun_instantiation(instance):
    assert isinstance(instance, myDsl_Fun)



@given(instance=myDsl_Fun_strategy)
def test_mydsl_fun_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_If_strategy)
@settings(max_examples=50)
def test_mydsl_if_instantiation(instance):
    assert isinstance(instance, myDsl_If)

@given(instance=myDsl_ArithOpTimes_strategy)
@settings(max_examples=50)
def test_mydsl_arithoptimes_instantiation(instance):
    assert isinstance(instance, myDsl_ArithOpTimes)

@given(instance=myDsl_App_strategy)
@settings(max_examples=50)
def test_mydsl_app_instantiation(instance):
    assert isinstance(instance, myDsl_App)

@given(instance=myDsl_ArithOpDivide_strategy)
@settings(max_examples=50)
def test_mydsl_arithopdivide_instantiation(instance):
    assert isinstance(instance, myDsl_ArithOpDivide)

@given(instance=myDsl_Skip_strategy)
@settings(max_examples=50)
def test_mydsl_skip_instantiation(instance):
    assert isinstance(instance, myDsl_Skip)

@given(instance=myDsl_ArithOpPlus_strategy)
@settings(max_examples=50)
def test_mydsl_arithopplus_instantiation(instance):
    assert isinstance(instance, myDsl_ArithOpPlus)

@given(instance=myDsl_Def_strategy)
@settings(max_examples=50)
def test_mydsl_def_instantiation(instance):
    assert isinstance(instance, myDsl_Def)



@given(instance=myDsl_Def_strategy)
def test_mydsl_def_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Expr_strategy)
@settings(max_examples=50)
def test_mydsl_expr_instantiation(instance):
    assert isinstance(instance, myDsl_Expr)

@given(instance=myDsl_TopLevelCmd_strategy)
@settings(max_examples=50)
def test_mydsl_toplevelcmd_instantiation(instance):
    assert isinstance(instance, myDsl_TopLevelCmd)

@given(instance=myDsl_File_strategy)
@settings(max_examples=50)
def test_mydsl_file_instantiation(instance):
    assert isinstance(instance, myDsl_File)
