import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TypeDef,
    jkind_AbbreviationType,
    Type,
    jkind_RealType,
    jkind_UserType,
    jkind_IntType,
    jkind_BoolType,
    jkind_SubrangeType,
    jkind_ArrayType,
    jkind_EnumType,
    jkind_RecordType,
    jkind_RealizabilityInputs,
    jkind_IdRef,
    jkind_Callable,
    Expr,
    jkind_RecordUpdateExpr,
    jkind_RecordExpr,
    jkind_ArrayUpdateExpr,
    jkind_RealExpr,
    jkind_RecordAccessExpr,
    jkind_IfThenElseExpr,
    jkind_TupleExpr,
    jkind_ArrayExpr,
    jkind_CondactExpr,
    jkind_IntExpr,
    jkind_UnaryExpr,
    jkind_CastExpr,
    jkind_BoolExpr,
    jkind_BinaryExpr,
    jkind_IdExpr,
    jkind_ArrayAccessExpr,
    jkind_CallExpr,
    jkind_TypeDef,
    jkind_File,
    jkind_Ivc,
    jkind_Property,
    jkind_Assertion,
    jkind_Equation,
    jkind_VariableGroup,
    Callable,
    jkind_Expr,
    jkind_Field,
    jkind_Type,
    IdRef,
    jkind_Variable,
    jkind_EnumValue,
    jkind_Node,
    jkind_Function,
    jkind_Constant,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typedef_is_not_abstract():
    assert not inspect.isabstract(TypeDef)


def test_typedef_constructor_exists():
    assert callable(TypeDef.__init__)


def test_typedef_constructor_args():
    sig = inspect.signature(TypeDef.__init__)
    params = list(sig.parameters.keys())



def test_jkind_abbreviationtype_is_not_abstract():
    assert not inspect.isabstract(jkind_AbbreviationType)


def test_jkind_abbreviationtype_constructor_exists():
    assert callable(jkind_AbbreviationType.__init__)


def test_jkind_abbreviationtype_constructor_args():
    sig = inspect.signature(jkind_AbbreviationType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_jkind_realtype_is_not_abstract():
    assert not inspect.isabstract(jkind_RealType)


def test_jkind_realtype_constructor_exists():
    assert callable(jkind_RealType.__init__)


def test_jkind_realtype_constructor_args():
    sig = inspect.signature(jkind_RealType.__init__)
    params = list(sig.parameters.keys())



def test_jkind_usertype_is_not_abstract():
    assert not inspect.isabstract(jkind_UserType)


def test_jkind_usertype_constructor_exists():
    assert callable(jkind_UserType.__init__)


def test_jkind_usertype_constructor_args():
    sig = inspect.signature(jkind_UserType.__init__)
    params = list(sig.parameters.keys())



def test_jkind_inttype_is_not_abstract():
    assert not inspect.isabstract(jkind_IntType)


def test_jkind_inttype_constructor_exists():
    assert callable(jkind_IntType.__init__)


def test_jkind_inttype_constructor_args():
    sig = inspect.signature(jkind_IntType.__init__)
    params = list(sig.parameters.keys())



def test_jkind_booltype_is_not_abstract():
    assert not inspect.isabstract(jkind_BoolType)


def test_jkind_booltype_constructor_exists():
    assert callable(jkind_BoolType.__init__)


def test_jkind_booltype_constructor_args():
    sig = inspect.signature(jkind_BoolType.__init__)
    params = list(sig.parameters.keys())



def test_jkind_subrangetype_is_not_abstract():
    assert not inspect.isabstract(jkind_SubrangeType)


def test_jkind_subrangetype_constructor_exists():
    assert callable(jkind_SubrangeType.__init__)


def test_jkind_subrangetype_constructor_args():
    sig = inspect.signature(jkind_SubrangeType.__init__)
    params = list(sig.parameters.keys())
    assert "high" in params, "Missing parameter 'high'"
    assert "low" in params, "Missing parameter 'low'"

def test_jkind_subrangetype_has_high():
    assert hasattr(jkind_SubrangeType, "high")
    descriptor = None
    for klass in jkind_SubrangeType.__mro__:
        if "high" in klass.__dict__:
            descriptor = klass.__dict__["high"]
            break
    assert isinstance(descriptor, property)

def test_jkind_subrangetype_has_low():
    assert hasattr(jkind_SubrangeType, "low")
    descriptor = None
    for klass in jkind_SubrangeType.__mro__:
        if "low" in klass.__dict__:
            descriptor = klass.__dict__["low"]
            break
    assert isinstance(descriptor, property)



def test_jkind_arraytype_is_not_abstract():
    assert not inspect.isabstract(jkind_ArrayType)


def test_jkind_arraytype_constructor_exists():
    assert callable(jkind_ArrayType.__init__)


def test_jkind_arraytype_constructor_args():
    sig = inspect.signature(jkind_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_jkind_arraytype_has_size():
    assert hasattr(jkind_ArrayType, "size")
    descriptor = None
    for klass in jkind_ArrayType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_jkind_enumtype_is_not_abstract():
    assert not inspect.isabstract(jkind_EnumType)


def test_jkind_enumtype_constructor_exists():
    assert callable(jkind_EnumType.__init__)


def test_jkind_enumtype_constructor_args():
    sig = inspect.signature(jkind_EnumType.__init__)
    params = list(sig.parameters.keys())



def test_jkind_recordtype_is_not_abstract():
    assert not inspect.isabstract(jkind_RecordType)


def test_jkind_recordtype_constructor_exists():
    assert callable(jkind_RecordType.__init__)


def test_jkind_recordtype_constructor_args():
    sig = inspect.signature(jkind_RecordType.__init__)
    params = list(sig.parameters.keys())



def test_jkind_realizabilityinputs_is_not_abstract():
    assert not inspect.isabstract(jkind_RealizabilityInputs)


def test_jkind_realizabilityinputs_constructor_exists():
    assert callable(jkind_RealizabilityInputs.__init__)


def test_jkind_realizabilityinputs_constructor_args():
    sig = inspect.signature(jkind_RealizabilityInputs.__init__)
    params = list(sig.parameters.keys())



def test_jkind_idref_is_not_abstract():
    assert not inspect.isabstract(jkind_IdRef)


def test_jkind_idref_constructor_exists():
    assert callable(jkind_IdRef.__init__)


def test_jkind_idref_constructor_args():
    sig = inspect.signature(jkind_IdRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jkind_idref_has_name():
    assert hasattr(jkind_IdRef, "name")
    descriptor = None
    for klass in jkind_IdRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jkind_callable_is_not_abstract():
    assert not inspect.isabstract(jkind_Callable)


def test_jkind_callable_constructor_exists():
    assert callable(jkind_Callable.__init__)


def test_jkind_callable_constructor_args():
    sig = inspect.signature(jkind_Callable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jkind_callable_has_name():
    assert hasattr(jkind_Callable, "name")
    descriptor = None
    for klass in jkind_Callable.__mro__:
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



def test_jkind_recordupdateexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_RecordUpdateExpr)


def test_jkind_recordupdateexpr_constructor_exists():
    assert callable(jkind_RecordUpdateExpr.__init__)


def test_jkind_recordupdateexpr_constructor_args():
    sig = inspect.signature(jkind_RecordUpdateExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind_recordexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_RecordExpr)


def test_jkind_recordexpr_constructor_exists():
    assert callable(jkind_RecordExpr.__init__)


def test_jkind_recordexpr_constructor_args():
    sig = inspect.signature(jkind_RecordExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind_arrayupdateexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_ArrayUpdateExpr)


def test_jkind_arrayupdateexpr_constructor_exists():
    assert callable(jkind_ArrayUpdateExpr.__init__)


def test_jkind_arrayupdateexpr_constructor_args():
    sig = inspect.signature(jkind_ArrayUpdateExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind_realexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_RealExpr)


def test_jkind_realexpr_constructor_exists():
    assert callable(jkind_RealExpr.__init__)


def test_jkind_realexpr_constructor_args():
    sig = inspect.signature(jkind_RealExpr.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_jkind_realexpr_has_val():
    assert hasattr(jkind_RealExpr, "val")
    descriptor = None
    for klass in jkind_RealExpr.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_jkind_recordaccessexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_RecordAccessExpr)


def test_jkind_recordaccessexpr_constructor_exists():
    assert callable(jkind_RecordAccessExpr.__init__)


def test_jkind_recordaccessexpr_constructor_args():
    sig = inspect.signature(jkind_RecordAccessExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind_ifthenelseexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_IfThenElseExpr)


def test_jkind_ifthenelseexpr_constructor_exists():
    assert callable(jkind_IfThenElseExpr.__init__)


def test_jkind_ifthenelseexpr_constructor_args():
    sig = inspect.signature(jkind_IfThenElseExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind_tupleexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_TupleExpr)


def test_jkind_tupleexpr_constructor_exists():
    assert callable(jkind_TupleExpr.__init__)


def test_jkind_tupleexpr_constructor_args():
    sig = inspect.signature(jkind_TupleExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind_arrayexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_ArrayExpr)


def test_jkind_arrayexpr_constructor_exists():
    assert callable(jkind_ArrayExpr.__init__)


def test_jkind_arrayexpr_constructor_args():
    sig = inspect.signature(jkind_ArrayExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind_condactexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_CondactExpr)


def test_jkind_condactexpr_constructor_exists():
    assert callable(jkind_CondactExpr.__init__)


def test_jkind_condactexpr_constructor_args():
    sig = inspect.signature(jkind_CondactExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind_intexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_IntExpr)


def test_jkind_intexpr_constructor_exists():
    assert callable(jkind_IntExpr.__init__)


def test_jkind_intexpr_constructor_args():
    sig = inspect.signature(jkind_IntExpr.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_jkind_intexpr_has_val():
    assert hasattr(jkind_IntExpr, "val")
    descriptor = None
    for klass in jkind_IntExpr.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_jkind_unaryexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_UnaryExpr)


def test_jkind_unaryexpr_constructor_exists():
    assert callable(jkind_UnaryExpr.__init__)


def test_jkind_unaryexpr_constructor_args():
    sig = inspect.signature(jkind_UnaryExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_jkind_unaryexpr_has_op():
    assert hasattr(jkind_UnaryExpr, "op")
    descriptor = None
    for klass in jkind_UnaryExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_jkind_castexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_CastExpr)


def test_jkind_castexpr_constructor_exists():
    assert callable(jkind_CastExpr.__init__)


def test_jkind_castexpr_constructor_args():
    sig = inspect.signature(jkind_CastExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_jkind_castexpr_has_op():
    assert hasattr(jkind_CastExpr, "op")
    descriptor = None
    for klass in jkind_CastExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_jkind_boolexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_BoolExpr)


def test_jkind_boolexpr_constructor_exists():
    assert callable(jkind_BoolExpr.__init__)


def test_jkind_boolexpr_constructor_args():
    sig = inspect.signature(jkind_BoolExpr.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_jkind_boolexpr_has_val():
    assert hasattr(jkind_BoolExpr, "val")
    descriptor = None
    for klass in jkind_BoolExpr.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_jkind_binaryexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_BinaryExpr)


def test_jkind_binaryexpr_constructor_exists():
    assert callable(jkind_BinaryExpr.__init__)


def test_jkind_binaryexpr_constructor_args():
    sig = inspect.signature(jkind_BinaryExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_jkind_binaryexpr_has_op():
    assert hasattr(jkind_BinaryExpr, "op")
    descriptor = None
    for klass in jkind_BinaryExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_jkind_idexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_IdExpr)


def test_jkind_idexpr_constructor_exists():
    assert callable(jkind_IdExpr.__init__)


def test_jkind_idexpr_constructor_args():
    sig = inspect.signature(jkind_IdExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind_arrayaccessexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_ArrayAccessExpr)


def test_jkind_arrayaccessexpr_constructor_exists():
    assert callable(jkind_ArrayAccessExpr.__init__)


def test_jkind_arrayaccessexpr_constructor_args():
    sig = inspect.signature(jkind_ArrayAccessExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind_callexpr_is_not_abstract():
    assert not inspect.isabstract(jkind_CallExpr)


def test_jkind_callexpr_constructor_exists():
    assert callable(jkind_CallExpr.__init__)


def test_jkind_callexpr_constructor_args():
    sig = inspect.signature(jkind_CallExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind_typedef_is_not_abstract():
    assert not inspect.isabstract(jkind_TypeDef)


def test_jkind_typedef_constructor_exists():
    assert callable(jkind_TypeDef.__init__)


def test_jkind_typedef_constructor_args():
    sig = inspect.signature(jkind_TypeDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jkind_typedef_has_name():
    assert hasattr(jkind_TypeDef, "name")
    descriptor = None
    for klass in jkind_TypeDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jkind_file_is_not_abstract():
    assert not inspect.isabstract(jkind_File)


def test_jkind_file_constructor_exists():
    assert callable(jkind_File.__init__)


def test_jkind_file_constructor_args():
    sig = inspect.signature(jkind_File.__init__)
    params = list(sig.parameters.keys())



def test_jkind_ivc_is_not_abstract():
    assert not inspect.isabstract(jkind_Ivc)


def test_jkind_ivc_constructor_exists():
    assert callable(jkind_Ivc.__init__)


def test_jkind_ivc_constructor_args():
    sig = inspect.signature(jkind_Ivc.__init__)
    params = list(sig.parameters.keys())



def test_jkind_property_is_not_abstract():
    assert not inspect.isabstract(jkind_Property)


def test_jkind_property_constructor_exists():
    assert callable(jkind_Property.__init__)


def test_jkind_property_constructor_args():
    sig = inspect.signature(jkind_Property.__init__)
    params = list(sig.parameters.keys())



def test_jkind_assertion_is_not_abstract():
    assert not inspect.isabstract(jkind_Assertion)


def test_jkind_assertion_constructor_exists():
    assert callable(jkind_Assertion.__init__)


def test_jkind_assertion_constructor_args():
    sig = inspect.signature(jkind_Assertion.__init__)
    params = list(sig.parameters.keys())



def test_jkind_equation_is_not_abstract():
    assert not inspect.isabstract(jkind_Equation)


def test_jkind_equation_constructor_exists():
    assert callable(jkind_Equation.__init__)


def test_jkind_equation_constructor_args():
    sig = inspect.signature(jkind_Equation.__init__)
    params = list(sig.parameters.keys())



def test_jkind_variablegroup_is_not_abstract():
    assert not inspect.isabstract(jkind_VariableGroup)


def test_jkind_variablegroup_constructor_exists():
    assert callable(jkind_VariableGroup.__init__)


def test_jkind_variablegroup_constructor_args():
    sig = inspect.signature(jkind_VariableGroup.__init__)
    params = list(sig.parameters.keys())



def test_callable_is_not_abstract():
    assert not inspect.isabstract(Callable)


def test_callable_constructor_exists():
    assert callable(Callable.__init__)


def test_callable_constructor_args():
    sig = inspect.signature(Callable.__init__)
    params = list(sig.parameters.keys())



def test_jkind_expr_is_not_abstract():
    assert not inspect.isabstract(jkind_Expr)


def test_jkind_expr_constructor_exists():
    assert callable(jkind_Expr.__init__)


def test_jkind_expr_constructor_args():
    sig = inspect.signature(jkind_Expr.__init__)
    params = list(sig.parameters.keys())



def test_jkind_field_is_not_abstract():
    assert not inspect.isabstract(jkind_Field)


def test_jkind_field_constructor_exists():
    assert callable(jkind_Field.__init__)


def test_jkind_field_constructor_args():
    sig = inspect.signature(jkind_Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jkind_field_has_name():
    assert hasattr(jkind_Field, "name")
    descriptor = None
    for klass in jkind_Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jkind_type_is_not_abstract():
    assert not inspect.isabstract(jkind_Type)


def test_jkind_type_constructor_exists():
    assert callable(jkind_Type.__init__)


def test_jkind_type_constructor_args():
    sig = inspect.signature(jkind_Type.__init__)
    params = list(sig.parameters.keys())



def test_idref_is_not_abstract():
    assert not inspect.isabstract(IdRef)


def test_idref_constructor_exists():
    assert callable(IdRef.__init__)


def test_idref_constructor_args():
    sig = inspect.signature(IdRef.__init__)
    params = list(sig.parameters.keys())



def test_jkind_variable_is_not_abstract():
    assert not inspect.isabstract(jkind_Variable)


def test_jkind_variable_constructor_exists():
    assert callable(jkind_Variable.__init__)


def test_jkind_variable_constructor_args():
    sig = inspect.signature(jkind_Variable.__init__)
    params = list(sig.parameters.keys())



def test_jkind_enumvalue_is_not_abstract():
    assert not inspect.isabstract(jkind_EnumValue)


def test_jkind_enumvalue_constructor_exists():
    assert callable(jkind_EnumValue.__init__)


def test_jkind_enumvalue_constructor_args():
    sig = inspect.signature(jkind_EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_jkind_node_is_not_abstract():
    assert not inspect.isabstract(jkind_Node)


def test_jkind_node_constructor_exists():
    assert callable(jkind_Node.__init__)


def test_jkind_node_constructor_args():
    sig = inspect.signature(jkind_Node.__init__)
    params = list(sig.parameters.keys())
    assert "main" in params, "Missing parameter 'main'"

def test_jkind_node_has_main():
    assert hasattr(jkind_Node, "main")
    descriptor = None
    for klass in jkind_Node.__mro__:
        if "main" in klass.__dict__:
            descriptor = klass.__dict__["main"]
            break
    assert isinstance(descriptor, property)



def test_jkind_function_is_not_abstract():
    assert not inspect.isabstract(jkind_Function)


def test_jkind_function_constructor_exists():
    assert callable(jkind_Function.__init__)


def test_jkind_function_constructor_args():
    sig = inspect.signature(jkind_Function.__init__)
    params = list(sig.parameters.keys())



def test_jkind_constant_is_not_abstract():
    assert not inspect.isabstract(jkind_Constant)


def test_jkind_constant_constructor_exists():
    assert callable(jkind_Constant.__init__)


def test_jkind_constant_constructor_args():
    sig = inspect.signature(jkind_Constant.__init__)
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
TypeDef_strategy = st.builds(
    TypeDef,
)
jkind_AbbreviationType_strategy = st.builds(
    jkind_AbbreviationType,
)
Type_strategy = st.builds(
    Type,
)
jkind_RealType_strategy = st.builds(
    jkind_RealType,
)
jkind_UserType_strategy = st.builds(
    jkind_UserType,
)
jkind_IntType_strategy = st.builds(
    jkind_IntType,
)
jkind_BoolType_strategy = st.builds(
    jkind_BoolType,
)
jkind_SubrangeType_strategy = st.builds(
    jkind_SubrangeType,
    high=
        safe_text,
    low=
        safe_text
)
jkind_ArrayType_strategy = st.builds(
    jkind_ArrayType,
    size=
        safe_text
)
jkind_EnumType_strategy = st.builds(
    jkind_EnumType,
)
jkind_RecordType_strategy = st.builds(
    jkind_RecordType,
)
jkind_RealizabilityInputs_strategy = st.builds(
    jkind_RealizabilityInputs,
)
jkind_IdRef_strategy = st.builds(
    jkind_IdRef,
    name=
        safe_text
)
jkind_Callable_strategy = st.builds(
    jkind_Callable,
    name=
        safe_text
)
Expr_strategy = st.builds(
    Expr,
)
jkind_RecordUpdateExpr_strategy = st.builds(
    jkind_RecordUpdateExpr,
)
jkind_RecordExpr_strategy = st.builds(
    jkind_RecordExpr,
)
jkind_ArrayUpdateExpr_strategy = st.builds(
    jkind_ArrayUpdateExpr,
)
jkind_RealExpr_strategy = st.builds(
    jkind_RealExpr,
    val=
        safe_text
)
jkind_RecordAccessExpr_strategy = st.builds(
    jkind_RecordAccessExpr,
)
jkind_IfThenElseExpr_strategy = st.builds(
    jkind_IfThenElseExpr,
)
jkind_TupleExpr_strategy = st.builds(
    jkind_TupleExpr,
)
jkind_ArrayExpr_strategy = st.builds(
    jkind_ArrayExpr,
)
jkind_CondactExpr_strategy = st.builds(
    jkind_CondactExpr,
)
jkind_IntExpr_strategy = st.builds(
    jkind_IntExpr,
    val=
        safe_text
)
jkind_UnaryExpr_strategy = st.builds(
    jkind_UnaryExpr,
    op=
        safe_text
)
jkind_CastExpr_strategy = st.builds(
    jkind_CastExpr,
    op=
        safe_text
)
jkind_BoolExpr_strategy = st.builds(
    jkind_BoolExpr,
    val=
        safe_text
)
jkind_BinaryExpr_strategy = st.builds(
    jkind_BinaryExpr,
    op=
        safe_text
)
jkind_IdExpr_strategy = st.builds(
    jkind_IdExpr,
)
jkind_ArrayAccessExpr_strategy = st.builds(
    jkind_ArrayAccessExpr,
)
jkind_CallExpr_strategy = st.builds(
    jkind_CallExpr,
)
jkind_TypeDef_strategy = st.builds(
    jkind_TypeDef,
    name=
        safe_text
)
jkind_File_strategy = st.builds(
    jkind_File,
)
jkind_Ivc_strategy = st.builds(
    jkind_Ivc,
)
jkind_Property_strategy = st.builds(
    jkind_Property,
)
jkind_Assertion_strategy = st.builds(
    jkind_Assertion,
)
jkind_Equation_strategy = st.builds(
    jkind_Equation,
)
jkind_VariableGroup_strategy = st.builds(
    jkind_VariableGroup,
)
Callable_strategy = st.builds(
    Callable,
)
jkind_Expr_strategy = st.builds(
    jkind_Expr,
)
jkind_Field_strategy = st.builds(
    jkind_Field,
    name=
        safe_text
)
jkind_Type_strategy = st.builds(
    jkind_Type,
)
IdRef_strategy = st.builds(
    IdRef,
)
jkind_Variable_strategy = st.builds(
    jkind_Variable,
)
jkind_EnumValue_strategy = st.builds(
    jkind_EnumValue,
)
jkind_Node_strategy = st.builds(
    jkind_Node,
    main=
        safe_text
)
jkind_Function_strategy = st.builds(
    jkind_Function,
)
jkind_Constant_strategy = st.builds(
    jkind_Constant,
)

@given(instance=TypeDef_strategy)
@settings(max_examples=50)
def test_typedef_instantiation(instance):
    assert isinstance(instance, TypeDef)

@given(instance=jkind_AbbreviationType_strategy)
@settings(max_examples=50)
def test_jkind_abbreviationtype_instantiation(instance):
    assert isinstance(instance, jkind_AbbreviationType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=jkind_RealType_strategy)
@settings(max_examples=50)
def test_jkind_realtype_instantiation(instance):
    assert isinstance(instance, jkind_RealType)

@given(instance=jkind_UserType_strategy)
@settings(max_examples=50)
def test_jkind_usertype_instantiation(instance):
    assert isinstance(instance, jkind_UserType)

@given(instance=jkind_IntType_strategy)
@settings(max_examples=50)
def test_jkind_inttype_instantiation(instance):
    assert isinstance(instance, jkind_IntType)

@given(instance=jkind_BoolType_strategy)
@settings(max_examples=50)
def test_jkind_booltype_instantiation(instance):
    assert isinstance(instance, jkind_BoolType)

@given(instance=jkind_SubrangeType_strategy)
@settings(max_examples=50)
def test_jkind_subrangetype_instantiation(instance):
    assert isinstance(instance, jkind_SubrangeType)



@given(instance=jkind_SubrangeType_strategy)
def test_jkind_subrangetype_high_setter(instance):
    original = instance.high
    instance.high = original
    assert instance.high == original



@given(instance=jkind_SubrangeType_strategy)
def test_jkind_subrangetype_low_setter(instance):
    original = instance.low
    instance.low = original
    assert instance.low == original

@given(instance=jkind_ArrayType_strategy)
@settings(max_examples=50)
def test_jkind_arraytype_instantiation(instance):
    assert isinstance(instance, jkind_ArrayType)



@given(instance=jkind_ArrayType_strategy)
def test_jkind_arraytype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=jkind_EnumType_strategy)
@settings(max_examples=50)
def test_jkind_enumtype_instantiation(instance):
    assert isinstance(instance, jkind_EnumType)

@given(instance=jkind_RecordType_strategy)
@settings(max_examples=50)
def test_jkind_recordtype_instantiation(instance):
    assert isinstance(instance, jkind_RecordType)

@given(instance=jkind_RealizabilityInputs_strategy)
@settings(max_examples=50)
def test_jkind_realizabilityinputs_instantiation(instance):
    assert isinstance(instance, jkind_RealizabilityInputs)

@given(instance=jkind_IdRef_strategy)
@settings(max_examples=50)
def test_jkind_idref_instantiation(instance):
    assert isinstance(instance, jkind_IdRef)



@given(instance=jkind_IdRef_strategy)
def test_jkind_idref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jkind_Callable_strategy)
@settings(max_examples=50)
def test_jkind_callable_instantiation(instance):
    assert isinstance(instance, jkind_Callable)



@given(instance=jkind_Callable_strategy)
def test_jkind_callable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=jkind_RecordUpdateExpr_strategy)
@settings(max_examples=50)
def test_jkind_recordupdateexpr_instantiation(instance):
    assert isinstance(instance, jkind_RecordUpdateExpr)

@given(instance=jkind_RecordExpr_strategy)
@settings(max_examples=50)
def test_jkind_recordexpr_instantiation(instance):
    assert isinstance(instance, jkind_RecordExpr)

@given(instance=jkind_ArrayUpdateExpr_strategy)
@settings(max_examples=50)
def test_jkind_arrayupdateexpr_instantiation(instance):
    assert isinstance(instance, jkind_ArrayUpdateExpr)

@given(instance=jkind_RealExpr_strategy)
@settings(max_examples=50)
def test_jkind_realexpr_instantiation(instance):
    assert isinstance(instance, jkind_RealExpr)



@given(instance=jkind_RealExpr_strategy)
def test_jkind_realexpr_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=jkind_RecordAccessExpr_strategy)
@settings(max_examples=50)
def test_jkind_recordaccessexpr_instantiation(instance):
    assert isinstance(instance, jkind_RecordAccessExpr)

@given(instance=jkind_IfThenElseExpr_strategy)
@settings(max_examples=50)
def test_jkind_ifthenelseexpr_instantiation(instance):
    assert isinstance(instance, jkind_IfThenElseExpr)

@given(instance=jkind_TupleExpr_strategy)
@settings(max_examples=50)
def test_jkind_tupleexpr_instantiation(instance):
    assert isinstance(instance, jkind_TupleExpr)

@given(instance=jkind_ArrayExpr_strategy)
@settings(max_examples=50)
def test_jkind_arrayexpr_instantiation(instance):
    assert isinstance(instance, jkind_ArrayExpr)

@given(instance=jkind_CondactExpr_strategy)
@settings(max_examples=50)
def test_jkind_condactexpr_instantiation(instance):
    assert isinstance(instance, jkind_CondactExpr)

@given(instance=jkind_IntExpr_strategy)
@settings(max_examples=50)
def test_jkind_intexpr_instantiation(instance):
    assert isinstance(instance, jkind_IntExpr)



@given(instance=jkind_IntExpr_strategy)
def test_jkind_intexpr_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=jkind_UnaryExpr_strategy)
@settings(max_examples=50)
def test_jkind_unaryexpr_instantiation(instance):
    assert isinstance(instance, jkind_UnaryExpr)



@given(instance=jkind_UnaryExpr_strategy)
def test_jkind_unaryexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=jkind_CastExpr_strategy)
@settings(max_examples=50)
def test_jkind_castexpr_instantiation(instance):
    assert isinstance(instance, jkind_CastExpr)



@given(instance=jkind_CastExpr_strategy)
def test_jkind_castexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=jkind_BoolExpr_strategy)
@settings(max_examples=50)
def test_jkind_boolexpr_instantiation(instance):
    assert isinstance(instance, jkind_BoolExpr)



@given(instance=jkind_BoolExpr_strategy)
def test_jkind_boolexpr_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=jkind_BinaryExpr_strategy)
@settings(max_examples=50)
def test_jkind_binaryexpr_instantiation(instance):
    assert isinstance(instance, jkind_BinaryExpr)



@given(instance=jkind_BinaryExpr_strategy)
def test_jkind_binaryexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=jkind_IdExpr_strategy)
@settings(max_examples=50)
def test_jkind_idexpr_instantiation(instance):
    assert isinstance(instance, jkind_IdExpr)

@given(instance=jkind_ArrayAccessExpr_strategy)
@settings(max_examples=50)
def test_jkind_arrayaccessexpr_instantiation(instance):
    assert isinstance(instance, jkind_ArrayAccessExpr)

@given(instance=jkind_CallExpr_strategy)
@settings(max_examples=50)
def test_jkind_callexpr_instantiation(instance):
    assert isinstance(instance, jkind_CallExpr)

@given(instance=jkind_TypeDef_strategy)
@settings(max_examples=50)
def test_jkind_typedef_instantiation(instance):
    assert isinstance(instance, jkind_TypeDef)



@given(instance=jkind_TypeDef_strategy)
def test_jkind_typedef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jkind_File_strategy)
@settings(max_examples=50)
def test_jkind_file_instantiation(instance):
    assert isinstance(instance, jkind_File)

@given(instance=jkind_Ivc_strategy)
@settings(max_examples=50)
def test_jkind_ivc_instantiation(instance):
    assert isinstance(instance, jkind_Ivc)

@given(instance=jkind_Property_strategy)
@settings(max_examples=50)
def test_jkind_property_instantiation(instance):
    assert isinstance(instance, jkind_Property)

@given(instance=jkind_Assertion_strategy)
@settings(max_examples=50)
def test_jkind_assertion_instantiation(instance):
    assert isinstance(instance, jkind_Assertion)

@given(instance=jkind_Equation_strategy)
@settings(max_examples=50)
def test_jkind_equation_instantiation(instance):
    assert isinstance(instance, jkind_Equation)

@given(instance=jkind_VariableGroup_strategy)
@settings(max_examples=50)
def test_jkind_variablegroup_instantiation(instance):
    assert isinstance(instance, jkind_VariableGroup)

@given(instance=Callable_strategy)
@settings(max_examples=50)
def test_callable_instantiation(instance):
    assert isinstance(instance, Callable)

@given(instance=jkind_Expr_strategy)
@settings(max_examples=50)
def test_jkind_expr_instantiation(instance):
    assert isinstance(instance, jkind_Expr)

@given(instance=jkind_Field_strategy)
@settings(max_examples=50)
def test_jkind_field_instantiation(instance):
    assert isinstance(instance, jkind_Field)



@given(instance=jkind_Field_strategy)
def test_jkind_field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jkind_Type_strategy)
@settings(max_examples=50)
def test_jkind_type_instantiation(instance):
    assert isinstance(instance, jkind_Type)

@given(instance=IdRef_strategy)
@settings(max_examples=50)
def test_idref_instantiation(instance):
    assert isinstance(instance, IdRef)

@given(instance=jkind_Variable_strategy)
@settings(max_examples=50)
def test_jkind_variable_instantiation(instance):
    assert isinstance(instance, jkind_Variable)

@given(instance=jkind_EnumValue_strategy)
@settings(max_examples=50)
def test_jkind_enumvalue_instantiation(instance):
    assert isinstance(instance, jkind_EnumValue)

@given(instance=jkind_Node_strategy)
@settings(max_examples=50)
def test_jkind_node_instantiation(instance):
    assert isinstance(instance, jkind_Node)



@given(instance=jkind_Node_strategy)
def test_jkind_node_main_setter(instance):
    original = instance.main
    instance.main = original
    assert instance.main == original

@given(instance=jkind_Function_strategy)
@settings(max_examples=50)
def test_jkind_function_instantiation(instance):
    assert isinstance(instance, jkind_Function)

@given(instance=jkind_Constant_strategy)
@settings(max_examples=50)
def test_jkind_constant_instantiation(instance):
    assert isinstance(instance, jkind_Constant)
