import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TypeDef,
    jkind::AbbreviationType,
    Type,
    jkind::UserType,
    jkind::IntType,
    jkind::BoolType,
    jkind::SubrangeType,
    jkind::RealType,
    jkind::ArrayType,
    jkind::EnumType,
    jkind::RecordType,
    jkind::RealizabilityInputs,
    jkind::IdRef,
    jkind::Callable,
    Expr,
    jkind::BoolExpr,
    jkind::IfThenElseExpr,
    jkind::BinaryExpr,
    jkind::ArrayExpr,
    jkind::IdExpr,
    jkind::ArrayUpdateExpr,
    jkind::RecordAccessExpr,
    jkind::UnaryExpr,
    jkind::CastExpr,
    jkind::ArrayAccessExpr,
    jkind::CondactExpr,
    jkind::RecordUpdateExpr,
    jkind::TupleExpr,
    jkind::IntExpr,
    jkind::RealExpr,
    jkind::RecordExpr,
    jkind::CallExpr,
    jkind::TypeDef,
    jkind::File,
    jkind::Ivc,
    jkind::Property,
    jkind::Assertion,
    jkind::Equation,
    jkind::VariableGroup,
    Callable,
    jkind::Expr,
    jkind::Field,
    jkind::Type,
    IdRef,
    jkind::Variable,
    jkind::EnumValue,
    jkind::Node,
    jkind::Function,
    jkind::Constant,
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



def test_jkind::abbreviationtype_is_not_abstract():
    assert not inspect.isabstract(jkind::AbbreviationType)


def test_jkind::abbreviationtype_constructor_exists():
    assert callable(jkind::AbbreviationType.__init__)


def test_jkind::abbreviationtype_constructor_args():
    sig = inspect.signature(jkind::AbbreviationType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_jkind::usertype_is_not_abstract():
    assert not inspect.isabstract(jkind::UserType)


def test_jkind::usertype_constructor_exists():
    assert callable(jkind::UserType.__init__)


def test_jkind::usertype_constructor_args():
    sig = inspect.signature(jkind::UserType.__init__)
    params = list(sig.parameters.keys())



def test_jkind::inttype_is_not_abstract():
    assert not inspect.isabstract(jkind::IntType)


def test_jkind::inttype_constructor_exists():
    assert callable(jkind::IntType.__init__)


def test_jkind::inttype_constructor_args():
    sig = inspect.signature(jkind::IntType.__init__)
    params = list(sig.parameters.keys())



def test_jkind::booltype_is_not_abstract():
    assert not inspect.isabstract(jkind::BoolType)


def test_jkind::booltype_constructor_exists():
    assert callable(jkind::BoolType.__init__)


def test_jkind::booltype_constructor_args():
    sig = inspect.signature(jkind::BoolType.__init__)
    params = list(sig.parameters.keys())



def test_jkind::subrangetype_is_not_abstract():
    assert not inspect.isabstract(jkind::SubrangeType)


def test_jkind::subrangetype_constructor_exists():
    assert callable(jkind::SubrangeType.__init__)


def test_jkind::subrangetype_constructor_args():
    sig = inspect.signature(jkind::SubrangeType.__init__)
    params = list(sig.parameters.keys())
    assert "high" in params, "Missing parameter 'high'"
    assert "low" in params, "Missing parameter 'low'"

def test_jkind::subrangetype_has_high():
    assert hasattr(jkind::SubrangeType, "high")
    descriptor = None
    for klass in jkind::SubrangeType.__mro__:
        if "high" in klass.__dict__:
            descriptor = klass.__dict__["high"]
            break
    assert isinstance(descriptor, property)

def test_jkind::subrangetype_has_low():
    assert hasattr(jkind::SubrangeType, "low")
    descriptor = None
    for klass in jkind::SubrangeType.__mro__:
        if "low" in klass.__dict__:
            descriptor = klass.__dict__["low"]
            break
    assert isinstance(descriptor, property)



def test_jkind::realtype_is_not_abstract():
    assert not inspect.isabstract(jkind::RealType)


def test_jkind::realtype_constructor_exists():
    assert callable(jkind::RealType.__init__)


def test_jkind::realtype_constructor_args():
    sig = inspect.signature(jkind::RealType.__init__)
    params = list(sig.parameters.keys())



def test_jkind::arraytype_is_not_abstract():
    assert not inspect.isabstract(jkind::ArrayType)


def test_jkind::arraytype_constructor_exists():
    assert callable(jkind::ArrayType.__init__)


def test_jkind::arraytype_constructor_args():
    sig = inspect.signature(jkind::ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_jkind::arraytype_has_size():
    assert hasattr(jkind::ArrayType, "size")
    descriptor = None
    for klass in jkind::ArrayType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_jkind::enumtype_is_not_abstract():
    assert not inspect.isabstract(jkind::EnumType)


def test_jkind::enumtype_constructor_exists():
    assert callable(jkind::EnumType.__init__)


def test_jkind::enumtype_constructor_args():
    sig = inspect.signature(jkind::EnumType.__init__)
    params = list(sig.parameters.keys())



def test_jkind::recordtype_is_not_abstract():
    assert not inspect.isabstract(jkind::RecordType)


def test_jkind::recordtype_constructor_exists():
    assert callable(jkind::RecordType.__init__)


def test_jkind::recordtype_constructor_args():
    sig = inspect.signature(jkind::RecordType.__init__)
    params = list(sig.parameters.keys())



def test_jkind::realizabilityinputs_is_not_abstract():
    assert not inspect.isabstract(jkind::RealizabilityInputs)


def test_jkind::realizabilityinputs_constructor_exists():
    assert callable(jkind::RealizabilityInputs.__init__)


def test_jkind::realizabilityinputs_constructor_args():
    sig = inspect.signature(jkind::RealizabilityInputs.__init__)
    params = list(sig.parameters.keys())



def test_jkind::idref_is_not_abstract():
    assert not inspect.isabstract(jkind::IdRef)


def test_jkind::idref_constructor_exists():
    assert callable(jkind::IdRef.__init__)


def test_jkind::idref_constructor_args():
    sig = inspect.signature(jkind::IdRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jkind::idref_has_name():
    assert hasattr(jkind::IdRef, "name")
    descriptor = None
    for klass in jkind::IdRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jkind::callable_is_not_abstract():
    assert not inspect.isabstract(jkind::Callable)


def test_jkind::callable_constructor_exists():
    assert callable(jkind::Callable.__init__)


def test_jkind::callable_constructor_args():
    sig = inspect.signature(jkind::Callable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jkind::callable_has_name():
    assert hasattr(jkind::Callable, "name")
    descriptor = None
    for klass in jkind::Callable.__mro__:
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



def test_jkind::boolexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::BoolExpr)


def test_jkind::boolexpr_constructor_exists():
    assert callable(jkind::BoolExpr.__init__)


def test_jkind::boolexpr_constructor_args():
    sig = inspect.signature(jkind::BoolExpr.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_jkind::boolexpr_has_val():
    assert hasattr(jkind::BoolExpr, "val")
    descriptor = None
    for klass in jkind::BoolExpr.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_jkind::ifthenelseexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::IfThenElseExpr)


def test_jkind::ifthenelseexpr_constructor_exists():
    assert callable(jkind::IfThenElseExpr.__init__)


def test_jkind::ifthenelseexpr_constructor_args():
    sig = inspect.signature(jkind::IfThenElseExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind::binaryexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::BinaryExpr)


def test_jkind::binaryexpr_constructor_exists():
    assert callable(jkind::BinaryExpr.__init__)


def test_jkind::binaryexpr_constructor_args():
    sig = inspect.signature(jkind::BinaryExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_jkind::binaryexpr_has_op():
    assert hasattr(jkind::BinaryExpr, "op")
    descriptor = None
    for klass in jkind::BinaryExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_jkind::arrayexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::ArrayExpr)


def test_jkind::arrayexpr_constructor_exists():
    assert callable(jkind::ArrayExpr.__init__)


def test_jkind::arrayexpr_constructor_args():
    sig = inspect.signature(jkind::ArrayExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind::idexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::IdExpr)


def test_jkind::idexpr_constructor_exists():
    assert callable(jkind::IdExpr.__init__)


def test_jkind::idexpr_constructor_args():
    sig = inspect.signature(jkind::IdExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind::arrayupdateexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::ArrayUpdateExpr)


def test_jkind::arrayupdateexpr_constructor_exists():
    assert callable(jkind::ArrayUpdateExpr.__init__)


def test_jkind::arrayupdateexpr_constructor_args():
    sig = inspect.signature(jkind::ArrayUpdateExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind::recordaccessexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::RecordAccessExpr)


def test_jkind::recordaccessexpr_constructor_exists():
    assert callable(jkind::RecordAccessExpr.__init__)


def test_jkind::recordaccessexpr_constructor_args():
    sig = inspect.signature(jkind::RecordAccessExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind::unaryexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::UnaryExpr)


def test_jkind::unaryexpr_constructor_exists():
    assert callable(jkind::UnaryExpr.__init__)


def test_jkind::unaryexpr_constructor_args():
    sig = inspect.signature(jkind::UnaryExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_jkind::unaryexpr_has_op():
    assert hasattr(jkind::UnaryExpr, "op")
    descriptor = None
    for klass in jkind::UnaryExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_jkind::castexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::CastExpr)


def test_jkind::castexpr_constructor_exists():
    assert callable(jkind::CastExpr.__init__)


def test_jkind::castexpr_constructor_args():
    sig = inspect.signature(jkind::CastExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_jkind::castexpr_has_op():
    assert hasattr(jkind::CastExpr, "op")
    descriptor = None
    for klass in jkind::CastExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_jkind::arrayaccessexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::ArrayAccessExpr)


def test_jkind::arrayaccessexpr_constructor_exists():
    assert callable(jkind::ArrayAccessExpr.__init__)


def test_jkind::arrayaccessexpr_constructor_args():
    sig = inspect.signature(jkind::ArrayAccessExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind::condactexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::CondactExpr)


def test_jkind::condactexpr_constructor_exists():
    assert callable(jkind::CondactExpr.__init__)


def test_jkind::condactexpr_constructor_args():
    sig = inspect.signature(jkind::CondactExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind::recordupdateexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::RecordUpdateExpr)


def test_jkind::recordupdateexpr_constructor_exists():
    assert callable(jkind::RecordUpdateExpr.__init__)


def test_jkind::recordupdateexpr_constructor_args():
    sig = inspect.signature(jkind::RecordUpdateExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind::tupleexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::TupleExpr)


def test_jkind::tupleexpr_constructor_exists():
    assert callable(jkind::TupleExpr.__init__)


def test_jkind::tupleexpr_constructor_args():
    sig = inspect.signature(jkind::TupleExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind::intexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::IntExpr)


def test_jkind::intexpr_constructor_exists():
    assert callable(jkind::IntExpr.__init__)


def test_jkind::intexpr_constructor_args():
    sig = inspect.signature(jkind::IntExpr.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_jkind::intexpr_has_val():
    assert hasattr(jkind::IntExpr, "val")
    descriptor = None
    for klass in jkind::IntExpr.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_jkind::realexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::RealExpr)


def test_jkind::realexpr_constructor_exists():
    assert callable(jkind::RealExpr.__init__)


def test_jkind::realexpr_constructor_args():
    sig = inspect.signature(jkind::RealExpr.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_jkind::realexpr_has_val():
    assert hasattr(jkind::RealExpr, "val")
    descriptor = None
    for klass in jkind::RealExpr.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_jkind::recordexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::RecordExpr)


def test_jkind::recordexpr_constructor_exists():
    assert callable(jkind::RecordExpr.__init__)


def test_jkind::recordexpr_constructor_args():
    sig = inspect.signature(jkind::RecordExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind::callexpr_is_not_abstract():
    assert not inspect.isabstract(jkind::CallExpr)


def test_jkind::callexpr_constructor_exists():
    assert callable(jkind::CallExpr.__init__)


def test_jkind::callexpr_constructor_args():
    sig = inspect.signature(jkind::CallExpr.__init__)
    params = list(sig.parameters.keys())



def test_jkind::typedef_is_not_abstract():
    assert not inspect.isabstract(jkind::TypeDef)


def test_jkind::typedef_constructor_exists():
    assert callable(jkind::TypeDef.__init__)


def test_jkind::typedef_constructor_args():
    sig = inspect.signature(jkind::TypeDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jkind::typedef_has_name():
    assert hasattr(jkind::TypeDef, "name")
    descriptor = None
    for klass in jkind::TypeDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jkind::file_is_not_abstract():
    assert not inspect.isabstract(jkind::File)


def test_jkind::file_constructor_exists():
    assert callable(jkind::File.__init__)


def test_jkind::file_constructor_args():
    sig = inspect.signature(jkind::File.__init__)
    params = list(sig.parameters.keys())



def test_jkind::ivc_is_not_abstract():
    assert not inspect.isabstract(jkind::Ivc)


def test_jkind::ivc_constructor_exists():
    assert callable(jkind::Ivc.__init__)


def test_jkind::ivc_constructor_args():
    sig = inspect.signature(jkind::Ivc.__init__)
    params = list(sig.parameters.keys())



def test_jkind::property_is_not_abstract():
    assert not inspect.isabstract(jkind::Property)


def test_jkind::property_constructor_exists():
    assert callable(jkind::Property.__init__)


def test_jkind::property_constructor_args():
    sig = inspect.signature(jkind::Property.__init__)
    params = list(sig.parameters.keys())



def test_jkind::assertion_is_not_abstract():
    assert not inspect.isabstract(jkind::Assertion)


def test_jkind::assertion_constructor_exists():
    assert callable(jkind::Assertion.__init__)


def test_jkind::assertion_constructor_args():
    sig = inspect.signature(jkind::Assertion.__init__)
    params = list(sig.parameters.keys())



def test_jkind::equation_is_not_abstract():
    assert not inspect.isabstract(jkind::Equation)


def test_jkind::equation_constructor_exists():
    assert callable(jkind::Equation.__init__)


def test_jkind::equation_constructor_args():
    sig = inspect.signature(jkind::Equation.__init__)
    params = list(sig.parameters.keys())



def test_jkind::variablegroup_is_not_abstract():
    assert not inspect.isabstract(jkind::VariableGroup)


def test_jkind::variablegroup_constructor_exists():
    assert callable(jkind::VariableGroup.__init__)


def test_jkind::variablegroup_constructor_args():
    sig = inspect.signature(jkind::VariableGroup.__init__)
    params = list(sig.parameters.keys())



def test_callable_is_not_abstract():
    assert not inspect.isabstract(Callable)


def test_callable_constructor_exists():
    assert callable(Callable.__init__)


def test_callable_constructor_args():
    sig = inspect.signature(Callable.__init__)
    params = list(sig.parameters.keys())



def test_jkind::expr_is_not_abstract():
    assert not inspect.isabstract(jkind::Expr)


def test_jkind::expr_constructor_exists():
    assert callable(jkind::Expr.__init__)


def test_jkind::expr_constructor_args():
    sig = inspect.signature(jkind::Expr.__init__)
    params = list(sig.parameters.keys())



def test_jkind::field_is_not_abstract():
    assert not inspect.isabstract(jkind::Field)


def test_jkind::field_constructor_exists():
    assert callable(jkind::Field.__init__)


def test_jkind::field_constructor_args():
    sig = inspect.signature(jkind::Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jkind::field_has_name():
    assert hasattr(jkind::Field, "name")
    descriptor = None
    for klass in jkind::Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jkind::type_is_not_abstract():
    assert not inspect.isabstract(jkind::Type)


def test_jkind::type_constructor_exists():
    assert callable(jkind::Type.__init__)


def test_jkind::type_constructor_args():
    sig = inspect.signature(jkind::Type.__init__)
    params = list(sig.parameters.keys())



def test_idref_is_not_abstract():
    assert not inspect.isabstract(IdRef)


def test_idref_constructor_exists():
    assert callable(IdRef.__init__)


def test_idref_constructor_args():
    sig = inspect.signature(IdRef.__init__)
    params = list(sig.parameters.keys())



def test_jkind::variable_is_not_abstract():
    assert not inspect.isabstract(jkind::Variable)


def test_jkind::variable_constructor_exists():
    assert callable(jkind::Variable.__init__)


def test_jkind::variable_constructor_args():
    sig = inspect.signature(jkind::Variable.__init__)
    params = list(sig.parameters.keys())



def test_jkind::enumvalue_is_not_abstract():
    assert not inspect.isabstract(jkind::EnumValue)


def test_jkind::enumvalue_constructor_exists():
    assert callable(jkind::EnumValue.__init__)


def test_jkind::enumvalue_constructor_args():
    sig = inspect.signature(jkind::EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_jkind::node_is_not_abstract():
    assert not inspect.isabstract(jkind::Node)


def test_jkind::node_constructor_exists():
    assert callable(jkind::Node.__init__)


def test_jkind::node_constructor_args():
    sig = inspect.signature(jkind::Node.__init__)
    params = list(sig.parameters.keys())
    assert "main" in params, "Missing parameter 'main'"

def test_jkind::node_has_main():
    assert hasattr(jkind::Node, "main")
    descriptor = None
    for klass in jkind::Node.__mro__:
        if "main" in klass.__dict__:
            descriptor = klass.__dict__["main"]
            break
    assert isinstance(descriptor, property)



def test_jkind::function_is_not_abstract():
    assert not inspect.isabstract(jkind::Function)


def test_jkind::function_constructor_exists():
    assert callable(jkind::Function.__init__)


def test_jkind::function_constructor_args():
    sig = inspect.signature(jkind::Function.__init__)
    params = list(sig.parameters.keys())



def test_jkind::constant_is_not_abstract():
    assert not inspect.isabstract(jkind::Constant)


def test_jkind::constant_constructor_exists():
    assert callable(jkind::Constant.__init__)


def test_jkind::constant_constructor_args():
    sig = inspect.signature(jkind::Constant.__init__)
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
jkind::AbbreviationType_strategy = st.builds(
    jkind::AbbreviationType,
)
Type_strategy = st.builds(
    Type,
)
jkind::UserType_strategy = st.builds(
    jkind::UserType,
)
jkind::IntType_strategy = st.builds(
    jkind::IntType,
)
jkind::BoolType_strategy = st.builds(
    jkind::BoolType,
)
jkind::SubrangeType_strategy = st.builds(
    jkind::SubrangeType,
    high=
        safe_text,
    low=
        safe_text
)
jkind::RealType_strategy = st.builds(
    jkind::RealType,
)
jkind::ArrayType_strategy = st.builds(
    jkind::ArrayType,
    size=
        safe_text
)
jkind::EnumType_strategy = st.builds(
    jkind::EnumType,
)
jkind::RecordType_strategy = st.builds(
    jkind::RecordType,
)
jkind::RealizabilityInputs_strategy = st.builds(
    jkind::RealizabilityInputs,
)
jkind::IdRef_strategy = st.builds(
    jkind::IdRef,
    name=
        safe_text
)
jkind::Callable_strategy = st.builds(
    jkind::Callable,
    name=
        safe_text
)
Expr_strategy = st.builds(
    Expr,
)
jkind::BoolExpr_strategy = st.builds(
    jkind::BoolExpr,
    val=
        safe_text
)
jkind::IfThenElseExpr_strategy = st.builds(
    jkind::IfThenElseExpr,
)
jkind::BinaryExpr_strategy = st.builds(
    jkind::BinaryExpr,
    op=
        safe_text
)
jkind::ArrayExpr_strategy = st.builds(
    jkind::ArrayExpr,
)
jkind::IdExpr_strategy = st.builds(
    jkind::IdExpr,
)
jkind::ArrayUpdateExpr_strategy = st.builds(
    jkind::ArrayUpdateExpr,
)
jkind::RecordAccessExpr_strategy = st.builds(
    jkind::RecordAccessExpr,
)
jkind::UnaryExpr_strategy = st.builds(
    jkind::UnaryExpr,
    op=
        safe_text
)
jkind::CastExpr_strategy = st.builds(
    jkind::CastExpr,
    op=
        safe_text
)
jkind::ArrayAccessExpr_strategy = st.builds(
    jkind::ArrayAccessExpr,
)
jkind::CondactExpr_strategy = st.builds(
    jkind::CondactExpr,
)
jkind::RecordUpdateExpr_strategy = st.builds(
    jkind::RecordUpdateExpr,
)
jkind::TupleExpr_strategy = st.builds(
    jkind::TupleExpr,
)
jkind::IntExpr_strategy = st.builds(
    jkind::IntExpr,
    val=
        safe_text
)
jkind::RealExpr_strategy = st.builds(
    jkind::RealExpr,
    val=
        safe_text
)
jkind::RecordExpr_strategy = st.builds(
    jkind::RecordExpr,
)
jkind::CallExpr_strategy = st.builds(
    jkind::CallExpr,
)
jkind::TypeDef_strategy = st.builds(
    jkind::TypeDef,
    name=
        safe_text
)
jkind::File_strategy = st.builds(
    jkind::File,
)
jkind::Ivc_strategy = st.builds(
    jkind::Ivc,
)
jkind::Property_strategy = st.builds(
    jkind::Property,
)
jkind::Assertion_strategy = st.builds(
    jkind::Assertion,
)
jkind::Equation_strategy = st.builds(
    jkind::Equation,
)
jkind::VariableGroup_strategy = st.builds(
    jkind::VariableGroup,
)
Callable_strategy = st.builds(
    Callable,
)
jkind::Expr_strategy = st.builds(
    jkind::Expr,
)
jkind::Field_strategy = st.builds(
    jkind::Field,
    name=
        safe_text
)
jkind::Type_strategy = st.builds(
    jkind::Type,
)
IdRef_strategy = st.builds(
    IdRef,
)
jkind::Variable_strategy = st.builds(
    jkind::Variable,
)
jkind::EnumValue_strategy = st.builds(
    jkind::EnumValue,
)
jkind::Node_strategy = st.builds(
    jkind::Node,
    main=
        safe_text
)
jkind::Function_strategy = st.builds(
    jkind::Function,
)
jkind::Constant_strategy = st.builds(
    jkind::Constant,
)

@given(instance=TypeDef_strategy)
@settings(max_examples=50)
def test_typedef_instantiation(instance):
    assert isinstance(instance, TypeDef)

@given(instance=jkind::AbbreviationType_strategy)
@settings(max_examples=50)
def test_jkind::abbreviationtype_instantiation(instance):
    assert isinstance(instance, jkind::AbbreviationType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=jkind::UserType_strategy)
@settings(max_examples=50)
def test_jkind::usertype_instantiation(instance):
    assert isinstance(instance, jkind::UserType)

@given(instance=jkind::IntType_strategy)
@settings(max_examples=50)
def test_jkind::inttype_instantiation(instance):
    assert isinstance(instance, jkind::IntType)

@given(instance=jkind::BoolType_strategy)
@settings(max_examples=50)
def test_jkind::booltype_instantiation(instance):
    assert isinstance(instance, jkind::BoolType)

@given(instance=jkind::SubrangeType_strategy)
@settings(max_examples=50)
def test_jkind::subrangetype_instantiation(instance):
    assert isinstance(instance, jkind::SubrangeType)

@given(instance=jkind::SubrangeType_strategy)
def test_jkind::subrangetype_high_type(instance):
    assert isinstance(instance.high, str)


@given(instance=jkind::SubrangeType_strategy)
def test_jkind::subrangetype_high_setter(instance):
    original = instance.high
    instance.high = original
    assert instance.high == original

@given(instance=jkind::SubrangeType_strategy)
def test_jkind::subrangetype_low_type(instance):
    assert isinstance(instance.low, str)


@given(instance=jkind::SubrangeType_strategy)
def test_jkind::subrangetype_low_setter(instance):
    original = instance.low
    instance.low = original
    assert instance.low == original

@given(instance=jkind::RealType_strategy)
@settings(max_examples=50)
def test_jkind::realtype_instantiation(instance):
    assert isinstance(instance, jkind::RealType)

@given(instance=jkind::ArrayType_strategy)
@settings(max_examples=50)
def test_jkind::arraytype_instantiation(instance):
    assert isinstance(instance, jkind::ArrayType)

@given(instance=jkind::ArrayType_strategy)
def test_jkind::arraytype_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=jkind::ArrayType_strategy)
def test_jkind::arraytype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=jkind::EnumType_strategy)
@settings(max_examples=50)
def test_jkind::enumtype_instantiation(instance):
    assert isinstance(instance, jkind::EnumType)

@given(instance=jkind::RecordType_strategy)
@settings(max_examples=50)
def test_jkind::recordtype_instantiation(instance):
    assert isinstance(instance, jkind::RecordType)

@given(instance=jkind::RealizabilityInputs_strategy)
@settings(max_examples=50)
def test_jkind::realizabilityinputs_instantiation(instance):
    assert isinstance(instance, jkind::RealizabilityInputs)

@given(instance=jkind::IdRef_strategy)
@settings(max_examples=50)
def test_jkind::idref_instantiation(instance):
    assert isinstance(instance, jkind::IdRef)

@given(instance=jkind::IdRef_strategy)
def test_jkind::idref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jkind::IdRef_strategy)
def test_jkind::idref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jkind::Callable_strategy)
@settings(max_examples=50)
def test_jkind::callable_instantiation(instance):
    assert isinstance(instance, jkind::Callable)

@given(instance=jkind::Callable_strategy)
def test_jkind::callable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jkind::Callable_strategy)
def test_jkind::callable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=jkind::BoolExpr_strategy)
@settings(max_examples=50)
def test_jkind::boolexpr_instantiation(instance):
    assert isinstance(instance, jkind::BoolExpr)

@given(instance=jkind::BoolExpr_strategy)
def test_jkind::boolexpr_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=jkind::BoolExpr_strategy)
def test_jkind::boolexpr_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=jkind::IfThenElseExpr_strategy)
@settings(max_examples=50)
def test_jkind::ifthenelseexpr_instantiation(instance):
    assert isinstance(instance, jkind::IfThenElseExpr)

@given(instance=jkind::BinaryExpr_strategy)
@settings(max_examples=50)
def test_jkind::binaryexpr_instantiation(instance):
    assert isinstance(instance, jkind::BinaryExpr)

@given(instance=jkind::BinaryExpr_strategy)
def test_jkind::binaryexpr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=jkind::BinaryExpr_strategy)
def test_jkind::binaryexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=jkind::ArrayExpr_strategy)
@settings(max_examples=50)
def test_jkind::arrayexpr_instantiation(instance):
    assert isinstance(instance, jkind::ArrayExpr)

@given(instance=jkind::IdExpr_strategy)
@settings(max_examples=50)
def test_jkind::idexpr_instantiation(instance):
    assert isinstance(instance, jkind::IdExpr)

@given(instance=jkind::ArrayUpdateExpr_strategy)
@settings(max_examples=50)
def test_jkind::arrayupdateexpr_instantiation(instance):
    assert isinstance(instance, jkind::ArrayUpdateExpr)

@given(instance=jkind::RecordAccessExpr_strategy)
@settings(max_examples=50)
def test_jkind::recordaccessexpr_instantiation(instance):
    assert isinstance(instance, jkind::RecordAccessExpr)

@given(instance=jkind::UnaryExpr_strategy)
@settings(max_examples=50)
def test_jkind::unaryexpr_instantiation(instance):
    assert isinstance(instance, jkind::UnaryExpr)

@given(instance=jkind::UnaryExpr_strategy)
def test_jkind::unaryexpr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=jkind::UnaryExpr_strategy)
def test_jkind::unaryexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=jkind::CastExpr_strategy)
@settings(max_examples=50)
def test_jkind::castexpr_instantiation(instance):
    assert isinstance(instance, jkind::CastExpr)

@given(instance=jkind::CastExpr_strategy)
def test_jkind::castexpr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=jkind::CastExpr_strategy)
def test_jkind::castexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=jkind::ArrayAccessExpr_strategy)
@settings(max_examples=50)
def test_jkind::arrayaccessexpr_instantiation(instance):
    assert isinstance(instance, jkind::ArrayAccessExpr)

@given(instance=jkind::CondactExpr_strategy)
@settings(max_examples=50)
def test_jkind::condactexpr_instantiation(instance):
    assert isinstance(instance, jkind::CondactExpr)

@given(instance=jkind::RecordUpdateExpr_strategy)
@settings(max_examples=50)
def test_jkind::recordupdateexpr_instantiation(instance):
    assert isinstance(instance, jkind::RecordUpdateExpr)

@given(instance=jkind::TupleExpr_strategy)
@settings(max_examples=50)
def test_jkind::tupleexpr_instantiation(instance):
    assert isinstance(instance, jkind::TupleExpr)

@given(instance=jkind::IntExpr_strategy)
@settings(max_examples=50)
def test_jkind::intexpr_instantiation(instance):
    assert isinstance(instance, jkind::IntExpr)

@given(instance=jkind::IntExpr_strategy)
def test_jkind::intexpr_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=jkind::IntExpr_strategy)
def test_jkind::intexpr_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=jkind::RealExpr_strategy)
@settings(max_examples=50)
def test_jkind::realexpr_instantiation(instance):
    assert isinstance(instance, jkind::RealExpr)

@given(instance=jkind::RealExpr_strategy)
def test_jkind::realexpr_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=jkind::RealExpr_strategy)
def test_jkind::realexpr_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=jkind::RecordExpr_strategy)
@settings(max_examples=50)
def test_jkind::recordexpr_instantiation(instance):
    assert isinstance(instance, jkind::RecordExpr)

@given(instance=jkind::CallExpr_strategy)
@settings(max_examples=50)
def test_jkind::callexpr_instantiation(instance):
    assert isinstance(instance, jkind::CallExpr)

@given(instance=jkind::TypeDef_strategy)
@settings(max_examples=50)
def test_jkind::typedef_instantiation(instance):
    assert isinstance(instance, jkind::TypeDef)

@given(instance=jkind::TypeDef_strategy)
def test_jkind::typedef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jkind::TypeDef_strategy)
def test_jkind::typedef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jkind::File_strategy)
@settings(max_examples=50)
def test_jkind::file_instantiation(instance):
    assert isinstance(instance, jkind::File)

@given(instance=jkind::Ivc_strategy)
@settings(max_examples=50)
def test_jkind::ivc_instantiation(instance):
    assert isinstance(instance, jkind::Ivc)

@given(instance=jkind::Property_strategy)
@settings(max_examples=50)
def test_jkind::property_instantiation(instance):
    assert isinstance(instance, jkind::Property)

@given(instance=jkind::Assertion_strategy)
@settings(max_examples=50)
def test_jkind::assertion_instantiation(instance):
    assert isinstance(instance, jkind::Assertion)

@given(instance=jkind::Equation_strategy)
@settings(max_examples=50)
def test_jkind::equation_instantiation(instance):
    assert isinstance(instance, jkind::Equation)

@given(instance=jkind::VariableGroup_strategy)
@settings(max_examples=50)
def test_jkind::variablegroup_instantiation(instance):
    assert isinstance(instance, jkind::VariableGroup)

@given(instance=Callable_strategy)
@settings(max_examples=50)
def test_callable_instantiation(instance):
    assert isinstance(instance, Callable)

@given(instance=jkind::Expr_strategy)
@settings(max_examples=50)
def test_jkind::expr_instantiation(instance):
    assert isinstance(instance, jkind::Expr)

@given(instance=jkind::Field_strategy)
@settings(max_examples=50)
def test_jkind::field_instantiation(instance):
    assert isinstance(instance, jkind::Field)

@given(instance=jkind::Field_strategy)
def test_jkind::field_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jkind::Field_strategy)
def test_jkind::field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jkind::Type_strategy)
@settings(max_examples=50)
def test_jkind::type_instantiation(instance):
    assert isinstance(instance, jkind::Type)

@given(instance=IdRef_strategy)
@settings(max_examples=50)
def test_idref_instantiation(instance):
    assert isinstance(instance, IdRef)

@given(instance=jkind::Variable_strategy)
@settings(max_examples=50)
def test_jkind::variable_instantiation(instance):
    assert isinstance(instance, jkind::Variable)

@given(instance=jkind::EnumValue_strategy)
@settings(max_examples=50)
def test_jkind::enumvalue_instantiation(instance):
    assert isinstance(instance, jkind::EnumValue)

@given(instance=jkind::Node_strategy)
@settings(max_examples=50)
def test_jkind::node_instantiation(instance):
    assert isinstance(instance, jkind::Node)

@given(instance=jkind::Node_strategy)
def test_jkind::node_main_type(instance):
    assert isinstance(instance.main, str)


@given(instance=jkind::Node_strategy)
def test_jkind::node_main_setter(instance):
    original = instance.main
    instance.main = original
    assert instance.main == original

@given(instance=jkind::Function_strategy)
@settings(max_examples=50)
def test_jkind::function_instantiation(instance):
    assert isinstance(instance, jkind::Function)

@given(instance=jkind::Constant_strategy)
@settings(max_examples=50)
def test_jkind::constant_instantiation(instance):
    assert isinstance(instance, jkind::Constant)
