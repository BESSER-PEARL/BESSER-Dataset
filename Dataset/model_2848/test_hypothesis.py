import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    aDSL::IntegerNegative,
    Expression,
    aDSL::Equality,
    aDSL::And,
    aDSL::Plus,
    aDSL::StringConstant,
    aDSL::Or,
    aDSL::Minus,
    aDSL::MemberSelection,
    aDSL::Comparison,
    aDSL::Assignment,
    aDSL::Block,
    aDSL::Statement,
    aDSL::VarDef,
    Statement,
    aDSL::ForStat,
    aDSL::Expression,
    aDSL::For2Statement,
    aDSL::FinishStat,
    aDSL::WhileStat,
    aDSL::TryCatchStat,
    aDSL::ReturnStat,
    aDSL::WhenStatement,
    aDSL::AsyncStat,
    aDSL::AtStat,
    aDSL::IfStat,
    aDSL::AtomicStatement,
    aDSL::Body,
    aDSL::Init,
    aDSL::Not,
    aDSL::MulOrDiv,
    aDSL::New,
    aDSL::Reference,
    aDSL::Here,
    aDSL::Null,
    aDSL::This,
    aDSL::DeRef,
    aDSL::BoolConstant,
    aDSL::IntConstant,
    Member,
    aDSL::PrintInst,
    aDSL::MainMethod,
    SharedDef,
    aDSL::SharedVarDef,
    aDSL::SharedArrayDef,
    aDSL::Operator,
    aDSL::Method,
    aDSL::Member,
    VarDef,
    aDSL::VariableDef,
    aDSL::FuncVarDef,
    aDSL::SharedDef,
    aDSL::Parameter,
    aDSL::VariableType,
    aDSL::XClass,
    aDSL::AbstractElements,
    aDSL::Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_adsl::integernegative_is_not_abstract():
    assert not inspect.isabstract(aDSL::IntegerNegative)


def test_adsl::integernegative_constructor_exists():
    assert callable(aDSL::IntegerNegative.__init__)


def test_adsl::integernegative_constructor_args():
    sig = inspect.signature(aDSL::IntegerNegative.__init__)
    params = list(sig.parameters.keys())
    assert "isneg" in params, "Missing parameter 'isneg'"
    assert "value" in params, "Missing parameter 'value'"

def test_adsl::integernegative_has_isneg():
    assert hasattr(aDSL::IntegerNegative, "isneg")
    descriptor = None
    for klass in aDSL::IntegerNegative.__mro__:
        if "isneg" in klass.__dict__:
            descriptor = klass.__dict__["isneg"]
            break
    assert isinstance(descriptor, property)

def test_adsl::integernegative_has_value():
    assert hasattr(aDSL::IntegerNegative, "value")
    descriptor = None
    for klass in aDSL::IntegerNegative.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_adsl::equality_is_not_abstract():
    assert not inspect.isabstract(aDSL::Equality)


def test_adsl::equality_constructor_exists():
    assert callable(aDSL::Equality.__init__)


def test_adsl::equality_constructor_args():
    sig = inspect.signature(aDSL::Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_adsl::equality_has_op():
    assert hasattr(aDSL::Equality, "op")
    descriptor = None
    for klass in aDSL::Equality.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_adsl::and_is_not_abstract():
    assert not inspect.isabstract(aDSL::And)


def test_adsl::and_constructor_exists():
    assert callable(aDSL::And.__init__)


def test_adsl::and_constructor_args():
    sig = inspect.signature(aDSL::And.__init__)
    params = list(sig.parameters.keys())



def test_adsl::plus_is_not_abstract():
    assert not inspect.isabstract(aDSL::Plus)


def test_adsl::plus_constructor_exists():
    assert callable(aDSL::Plus.__init__)


def test_adsl::plus_constructor_args():
    sig = inspect.signature(aDSL::Plus.__init__)
    params = list(sig.parameters.keys())



def test_adsl::stringconstant_is_not_abstract():
    assert not inspect.isabstract(aDSL::StringConstant)


def test_adsl::stringconstant_constructor_exists():
    assert callable(aDSL::StringConstant.__init__)


def test_adsl::stringconstant_constructor_args():
    sig = inspect.signature(aDSL::StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_adsl::stringconstant_has_value():
    assert hasattr(aDSL::StringConstant, "value")
    descriptor = None
    for klass in aDSL::StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_adsl::or_is_not_abstract():
    assert not inspect.isabstract(aDSL::Or)


def test_adsl::or_constructor_exists():
    assert callable(aDSL::Or.__init__)


def test_adsl::or_constructor_args():
    sig = inspect.signature(aDSL::Or.__init__)
    params = list(sig.parameters.keys())



def test_adsl::minus_is_not_abstract():
    assert not inspect.isabstract(aDSL::Minus)


def test_adsl::minus_constructor_exists():
    assert callable(aDSL::Minus.__init__)


def test_adsl::minus_constructor_args():
    sig = inspect.signature(aDSL::Minus.__init__)
    params = list(sig.parameters.keys())



def test_adsl::memberselection_is_not_abstract():
    assert not inspect.isabstract(aDSL::MemberSelection)


def test_adsl::memberselection_constructor_exists():
    assert callable(aDSL::MemberSelection.__init__)


def test_adsl::memberselection_constructor_args():
    sig = inspect.signature(aDSL::MemberSelection.__init__)
    params = list(sig.parameters.keys())
    assert "methodinvocation" in params, "Missing parameter 'methodinvocation'"
    assert "ispar" in params, "Missing parameter 'ispar'"

def test_adsl::memberselection_has_methodinvocation():
    assert hasattr(aDSL::MemberSelection, "methodinvocation")
    descriptor = None
    for klass in aDSL::MemberSelection.__mro__:
        if "methodinvocation" in klass.__dict__:
            descriptor = klass.__dict__["methodinvocation"]
            break
    assert isinstance(descriptor, property)

def test_adsl::memberselection_has_ispar():
    assert hasattr(aDSL::MemberSelection, "ispar")
    descriptor = None
    for klass in aDSL::MemberSelection.__mro__:
        if "ispar" in klass.__dict__:
            descriptor = klass.__dict__["ispar"]
            break
    assert isinstance(descriptor, property)



def test_adsl::comparison_is_not_abstract():
    assert not inspect.isabstract(aDSL::Comparison)


def test_adsl::comparison_constructor_exists():
    assert callable(aDSL::Comparison.__init__)


def test_adsl::comparison_constructor_args():
    sig = inspect.signature(aDSL::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_adsl::comparison_has_op():
    assert hasattr(aDSL::Comparison, "op")
    descriptor = None
    for klass in aDSL::Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_adsl::assignment_is_not_abstract():
    assert not inspect.isabstract(aDSL::Assignment)


def test_adsl::assignment_constructor_exists():
    assert callable(aDSL::Assignment.__init__)


def test_adsl::assignment_constructor_args():
    sig = inspect.signature(aDSL::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_adsl::block_is_not_abstract():
    assert not inspect.isabstract(aDSL::Block)


def test_adsl::block_constructor_exists():
    assert callable(aDSL::Block.__init__)


def test_adsl::block_constructor_args():
    sig = inspect.signature(aDSL::Block.__init__)
    params = list(sig.parameters.keys())
    assert "ispar" in params, "Missing parameter 'ispar'"

def test_adsl::block_has_ispar():
    assert hasattr(aDSL::Block, "ispar")
    descriptor = None
    for klass in aDSL::Block.__mro__:
        if "ispar" in klass.__dict__:
            descriptor = klass.__dict__["ispar"]
            break
    assert isinstance(descriptor, property)



def test_adsl::statement_is_not_abstract():
    assert not inspect.isabstract(aDSL::Statement)


def test_adsl::statement_constructor_exists():
    assert callable(aDSL::Statement.__init__)


def test_adsl::statement_constructor_args():
    sig = inspect.signature(aDSL::Statement.__init__)
    params = list(sig.parameters.keys())



def test_adsl::vardef_is_not_abstract():
    assert not inspect.isabstract(aDSL::VarDef)


def test_adsl::vardef_constructor_exists():
    assert callable(aDSL::VarDef.__init__)


def test_adsl::vardef_constructor_args():
    sig = inspect.signature(aDSL::VarDef.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_adsl::forstat_is_not_abstract():
    assert not inspect.isabstract(aDSL::ForStat)


def test_adsl::forstat_constructor_exists():
    assert callable(aDSL::ForStat.__init__)


def test_adsl::forstat_constructor_args():
    sig = inspect.signature(aDSL::ForStat.__init__)
    params = list(sig.parameters.keys())



def test_adsl::expression_is_not_abstract():
    assert not inspect.isabstract(aDSL::Expression)


def test_adsl::expression_constructor_exists():
    assert callable(aDSL::Expression.__init__)


def test_adsl::expression_constructor_args():
    sig = inspect.signature(aDSL::Expression.__init__)
    params = list(sig.parameters.keys())



def test_adsl::for2statement_is_not_abstract():
    assert not inspect.isabstract(aDSL::For2Statement)


def test_adsl::for2statement_constructor_exists():
    assert callable(aDSL::For2Statement.__init__)


def test_adsl::for2statement_constructor_args():
    sig = inspect.signature(aDSL::For2Statement.__init__)
    params = list(sig.parameters.keys())



def test_adsl::finishstat_is_not_abstract():
    assert not inspect.isabstract(aDSL::FinishStat)


def test_adsl::finishstat_constructor_exists():
    assert callable(aDSL::FinishStat.__init__)


def test_adsl::finishstat_constructor_args():
    sig = inspect.signature(aDSL::FinishStat.__init__)
    params = list(sig.parameters.keys())



def test_adsl::whilestat_is_not_abstract():
    assert not inspect.isabstract(aDSL::WhileStat)


def test_adsl::whilestat_constructor_exists():
    assert callable(aDSL::WhileStat.__init__)


def test_adsl::whilestat_constructor_args():
    sig = inspect.signature(aDSL::WhileStat.__init__)
    params = list(sig.parameters.keys())



def test_adsl::trycatchstat_is_not_abstract():
    assert not inspect.isabstract(aDSL::TryCatchStat)


def test_adsl::trycatchstat_constructor_exists():
    assert callable(aDSL::TryCatchStat.__init__)


def test_adsl::trycatchstat_constructor_args():
    sig = inspect.signature(aDSL::TryCatchStat.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adsl::trycatchstat_has_name():
    assert hasattr(aDSL::TryCatchStat, "name")
    descriptor = None
    for klass in aDSL::TryCatchStat.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adsl::returnstat_is_not_abstract():
    assert not inspect.isabstract(aDSL::ReturnStat)


def test_adsl::returnstat_constructor_exists():
    assert callable(aDSL::ReturnStat.__init__)


def test_adsl::returnstat_constructor_args():
    sig = inspect.signature(aDSL::ReturnStat.__init__)
    params = list(sig.parameters.keys())



def test_adsl::whenstatement_is_not_abstract():
    assert not inspect.isabstract(aDSL::WhenStatement)


def test_adsl::whenstatement_constructor_exists():
    assert callable(aDSL::WhenStatement.__init__)


def test_adsl::whenstatement_constructor_args():
    sig = inspect.signature(aDSL::WhenStatement.__init__)
    params = list(sig.parameters.keys())



def test_adsl::asyncstat_is_not_abstract():
    assert not inspect.isabstract(aDSL::AsyncStat)


def test_adsl::asyncstat_constructor_exists():
    assert callable(aDSL::AsyncStat.__init__)


def test_adsl::asyncstat_constructor_args():
    sig = inspect.signature(aDSL::AsyncStat.__init__)
    params = list(sig.parameters.keys())



def test_adsl::atstat_is_not_abstract():
    assert not inspect.isabstract(aDSL::AtStat)


def test_adsl::atstat_constructor_exists():
    assert callable(aDSL::AtStat.__init__)


def test_adsl::atstat_constructor_args():
    sig = inspect.signature(aDSL::AtStat.__init__)
    params = list(sig.parameters.keys())



def test_adsl::ifstat_is_not_abstract():
    assert not inspect.isabstract(aDSL::IfStat)


def test_adsl::ifstat_constructor_exists():
    assert callable(aDSL::IfStat.__init__)


def test_adsl::ifstat_constructor_args():
    sig = inspect.signature(aDSL::IfStat.__init__)
    params = list(sig.parameters.keys())
    assert "iselse" in params, "Missing parameter 'iselse'"

def test_adsl::ifstat_has_iselse():
    assert hasattr(aDSL::IfStat, "iselse")
    descriptor = None
    for klass in aDSL::IfStat.__mro__:
        if "iselse" in klass.__dict__:
            descriptor = klass.__dict__["iselse"]
            break
    assert isinstance(descriptor, property)



def test_adsl::atomicstatement_is_not_abstract():
    assert not inspect.isabstract(aDSL::AtomicStatement)


def test_adsl::atomicstatement_constructor_exists():
    assert callable(aDSL::AtomicStatement.__init__)


def test_adsl::atomicstatement_constructor_args():
    sig = inspect.signature(aDSL::AtomicStatement.__init__)
    params = list(sig.parameters.keys())



def test_adsl::body_is_not_abstract():
    assert not inspect.isabstract(aDSL::Body)


def test_adsl::body_constructor_exists():
    assert callable(aDSL::Body.__init__)


def test_adsl::body_constructor_args():
    sig = inspect.signature(aDSL::Body.__init__)
    params = list(sig.parameters.keys())



def test_adsl::init_is_not_abstract():
    assert not inspect.isabstract(aDSL::Init)


def test_adsl::init_constructor_exists():
    assert callable(aDSL::Init.__init__)


def test_adsl::init_constructor_args():
    sig = inspect.signature(aDSL::Init.__init__)
    params = list(sig.parameters.keys())



def test_adsl::not_is_not_abstract():
    assert not inspect.isabstract(aDSL::Not)


def test_adsl::not_constructor_exists():
    assert callable(aDSL::Not.__init__)


def test_adsl::not_constructor_args():
    sig = inspect.signature(aDSL::Not.__init__)
    params = list(sig.parameters.keys())



def test_adsl::mulordiv_is_not_abstract():
    assert not inspect.isabstract(aDSL::MulOrDiv)


def test_adsl::mulordiv_constructor_exists():
    assert callable(aDSL::MulOrDiv.__init__)


def test_adsl::mulordiv_constructor_args():
    sig = inspect.signature(aDSL::MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_adsl::mulordiv_has_op():
    assert hasattr(aDSL::MulOrDiv, "op")
    descriptor = None
    for klass in aDSL::MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_adsl::new_is_not_abstract():
    assert not inspect.isabstract(aDSL::New)


def test_adsl::new_constructor_exists():
    assert callable(aDSL::New.__init__)


def test_adsl::new_constructor_args():
    sig = inspect.signature(aDSL::New.__init__)
    params = list(sig.parameters.keys())



def test_adsl::reference_is_not_abstract():
    assert not inspect.isabstract(aDSL::Reference)


def test_adsl::reference_constructor_exists():
    assert callable(aDSL::Reference.__init__)


def test_adsl::reference_constructor_args():
    sig = inspect.signature(aDSL::Reference.__init__)
    params = list(sig.parameters.keys())
    assert "isarray" in params, "Missing parameter 'isarray'"

def test_adsl::reference_has_isarray():
    assert hasattr(aDSL::Reference, "isarray")
    descriptor = None
    for klass in aDSL::Reference.__mro__:
        if "isarray" in klass.__dict__:
            descriptor = klass.__dict__["isarray"]
            break
    assert isinstance(descriptor, property)



def test_adsl::here_is_not_abstract():
    assert not inspect.isabstract(aDSL::Here)


def test_adsl::here_constructor_exists():
    assert callable(aDSL::Here.__init__)


def test_adsl::here_constructor_args():
    sig = inspect.signature(aDSL::Here.__init__)
    params = list(sig.parameters.keys())



def test_adsl::null_is_not_abstract():
    assert not inspect.isabstract(aDSL::Null)


def test_adsl::null_constructor_exists():
    assert callable(aDSL::Null.__init__)


def test_adsl::null_constructor_args():
    sig = inspect.signature(aDSL::Null.__init__)
    params = list(sig.parameters.keys())



def test_adsl::this_is_not_abstract():
    assert not inspect.isabstract(aDSL::This)


def test_adsl::this_constructor_exists():
    assert callable(aDSL::This.__init__)


def test_adsl::this_constructor_args():
    sig = inspect.signature(aDSL::This.__init__)
    params = list(sig.parameters.keys())



def test_adsl::deref_is_not_abstract():
    assert not inspect.isabstract(aDSL::DeRef)


def test_adsl::deref_constructor_exists():
    assert callable(aDSL::DeRef.__init__)


def test_adsl::deref_constructor_args():
    sig = inspect.signature(aDSL::DeRef.__init__)
    params = list(sig.parameters.keys())



def test_adsl::boolconstant_is_not_abstract():
    assert not inspect.isabstract(aDSL::BoolConstant)


def test_adsl::boolconstant_constructor_exists():
    assert callable(aDSL::BoolConstant.__init__)


def test_adsl::boolconstant_constructor_args():
    sig = inspect.signature(aDSL::BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_adsl::boolconstant_has_value():
    assert hasattr(aDSL::BoolConstant, "value")
    descriptor = None
    for klass in aDSL::BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_adsl::intconstant_is_not_abstract():
    assert not inspect.isabstract(aDSL::IntConstant)


def test_adsl::intconstant_constructor_exists():
    assert callable(aDSL::IntConstant.__init__)


def test_adsl::intconstant_constructor_args():
    sig = inspect.signature(aDSL::IntConstant.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_adsl::printinst_is_not_abstract():
    assert not inspect.isabstract(aDSL::PrintInst)


def test_adsl::printinst_constructor_exists():
    assert callable(aDSL::PrintInst.__init__)


def test_adsl::printinst_constructor_args():
    sig = inspect.signature(aDSL::PrintInst.__init__)
    params = list(sig.parameters.keys())



def test_adsl::mainmethod_is_not_abstract():
    assert not inspect.isabstract(aDSL::MainMethod)


def test_adsl::mainmethod_constructor_exists():
    assert callable(aDSL::MainMethod.__init__)


def test_adsl::mainmethod_constructor_args():
    sig = inspect.signature(aDSL::MainMethod.__init__)
    params = list(sig.parameters.keys())



def test_shareddef_is_not_abstract():
    assert not inspect.isabstract(SharedDef)


def test_shareddef_constructor_exists():
    assert callable(SharedDef.__init__)


def test_shareddef_constructor_args():
    sig = inspect.signature(SharedDef.__init__)
    params = list(sig.parameters.keys())



def test_adsl::sharedvardef_is_not_abstract():
    assert not inspect.isabstract(aDSL::SharedVarDef)


def test_adsl::sharedvardef_constructor_exists():
    assert callable(aDSL::SharedVarDef.__init__)


def test_adsl::sharedvardef_constructor_args():
    sig = inspect.signature(aDSL::SharedVarDef.__init__)
    params = list(sig.parameters.keys())



def test_adsl::sharedarraydef_is_not_abstract():
    assert not inspect.isabstract(aDSL::SharedArrayDef)


def test_adsl::sharedarraydef_constructor_exists():
    assert callable(aDSL::SharedArrayDef.__init__)


def test_adsl::sharedarraydef_constructor_args():
    sig = inspect.signature(aDSL::SharedArrayDef.__init__)
    params = list(sig.parameters.keys())



def test_adsl::operator_is_not_abstract():
    assert not inspect.isabstract(aDSL::Operator)


def test_adsl::operator_constructor_exists():
    assert callable(aDSL::Operator.__init__)


def test_adsl::operator_constructor_args():
    sig = inspect.signature(aDSL::Operator.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_adsl::operator_has_opName():
    assert hasattr(aDSL::Operator, "opName")
    descriptor = None
    for klass in aDSL::Operator.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_adsl::method_is_not_abstract():
    assert not inspect.isabstract(aDSL::Method)


def test_adsl::method_constructor_exists():
    assert callable(aDSL::Method.__init__)


def test_adsl::method_constructor_args():
    sig = inspect.signature(aDSL::Method.__init__)
    params = list(sig.parameters.keys())
    assert "istyped" in params, "Missing parameter 'istyped'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isconst" in params, "Missing parameter 'isconst'"

def test_adsl::method_has_istyped():
    assert hasattr(aDSL::Method, "istyped")
    descriptor = None
    for klass in aDSL::Method.__mro__:
        if "istyped" in klass.__dict__:
            descriptor = klass.__dict__["istyped"]
            break
    assert isinstance(descriptor, property)

def test_adsl::method_has_name():
    assert hasattr(aDSL::Method, "name")
    descriptor = None
    for klass in aDSL::Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adsl::method_has_isconst():
    assert hasattr(aDSL::Method, "isconst")
    descriptor = None
    for klass in aDSL::Method.__mro__:
        if "isconst" in klass.__dict__:
            descriptor = klass.__dict__["isconst"]
            break
    assert isinstance(descriptor, property)



def test_adsl::member_is_not_abstract():
    assert not inspect.isabstract(aDSL::Member)


def test_adsl::member_constructor_exists():
    assert callable(aDSL::Member.__init__)


def test_adsl::member_constructor_args():
    sig = inspect.signature(aDSL::Member.__init__)
    params = list(sig.parameters.keys())



def test_vardef_is_not_abstract():
    assert not inspect.isabstract(VarDef)


def test_vardef_constructor_exists():
    assert callable(VarDef.__init__)


def test_vardef_constructor_args():
    sig = inspect.signature(VarDef.__init__)
    params = list(sig.parameters.keys())



def test_adsl::variabledef_is_not_abstract():
    assert not inspect.isabstract(aDSL::VariableDef)


def test_adsl::variabledef_constructor_exists():
    assert callable(aDSL::VariableDef.__init__)


def test_adsl::variabledef_constructor_args():
    sig = inspect.signature(aDSL::VariableDef.__init__)
    params = list(sig.parameters.keys())
    assert "vartype" in params, "Missing parameter 'vartype'"
    assert "istyped" in params, "Missing parameter 'istyped'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isstatic" in params, "Missing parameter 'isstatic'"
    assert "isinit" in params, "Missing parameter 'isinit'"

def test_adsl::variabledef_has_vartype():
    assert hasattr(aDSL::VariableDef, "vartype")
    descriptor = None
    for klass in aDSL::VariableDef.__mro__:
        if "vartype" in klass.__dict__:
            descriptor = klass.__dict__["vartype"]
            break
    assert isinstance(descriptor, property)

def test_adsl::variabledef_has_istyped():
    assert hasattr(aDSL::VariableDef, "istyped")
    descriptor = None
    for klass in aDSL::VariableDef.__mro__:
        if "istyped" in klass.__dict__:
            descriptor = klass.__dict__["istyped"]
            break
    assert isinstance(descriptor, property)

def test_adsl::variabledef_has_name():
    assert hasattr(aDSL::VariableDef, "name")
    descriptor = None
    for klass in aDSL::VariableDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adsl::variabledef_has_isstatic():
    assert hasattr(aDSL::VariableDef, "isstatic")
    descriptor = None
    for klass in aDSL::VariableDef.__mro__:
        if "isstatic" in klass.__dict__:
            descriptor = klass.__dict__["isstatic"]
            break
    assert isinstance(descriptor, property)

def test_adsl::variabledef_has_isinit():
    assert hasattr(aDSL::VariableDef, "isinit")
    descriptor = None
    for klass in aDSL::VariableDef.__mro__:
        if "isinit" in klass.__dict__:
            descriptor = klass.__dict__["isinit"]
            break
    assert isinstance(descriptor, property)



def test_adsl::funcvardef_is_not_abstract():
    assert not inspect.isabstract(aDSL::FuncVarDef)


def test_adsl::funcvardef_constructor_exists():
    assert callable(aDSL::FuncVarDef.__init__)


def test_adsl::funcvardef_constructor_args():
    sig = inspect.signature(aDSL::FuncVarDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adsl::funcvardef_has_name():
    assert hasattr(aDSL::FuncVarDef, "name")
    descriptor = None
    for klass in aDSL::FuncVarDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adsl::shareddef_is_not_abstract():
    assert not inspect.isabstract(aDSL::SharedDef)


def test_adsl::shareddef_constructor_exists():
    assert callable(aDSL::SharedDef.__init__)


def test_adsl::shareddef_constructor_args():
    sig = inspect.signature(aDSL::SharedDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "replicas" in params, "Missing parameter 'replicas'"

def test_adsl::shareddef_has_name():
    assert hasattr(aDSL::SharedDef, "name")
    descriptor = None
    for klass in aDSL::SharedDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adsl::shareddef_has_replicas():
    assert hasattr(aDSL::SharedDef, "replicas")
    descriptor = None
    for klass in aDSL::SharedDef.__mro__:
        if "replicas" in klass.__dict__:
            descriptor = klass.__dict__["replicas"]
            break
    assert isinstance(descriptor, property)



def test_adsl::parameter_is_not_abstract():
    assert not inspect.isabstract(aDSL::Parameter)


def test_adsl::parameter_constructor_exists():
    assert callable(aDSL::Parameter.__init__)


def test_adsl::parameter_constructor_args():
    sig = inspect.signature(aDSL::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "istyped" in params, "Missing parameter 'istyped'"
    assert "name" in params, "Missing parameter 'name'"

def test_adsl::parameter_has_istyped():
    assert hasattr(aDSL::Parameter, "istyped")
    descriptor = None
    for klass in aDSL::Parameter.__mro__:
        if "istyped" in klass.__dict__:
            descriptor = klass.__dict__["istyped"]
            break
    assert isinstance(descriptor, property)

def test_adsl::parameter_has_name():
    assert hasattr(aDSL::Parameter, "name")
    descriptor = None
    for klass in aDSL::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adsl::variabletype_is_not_abstract():
    assert not inspect.isabstract(aDSL::VariableType)


def test_adsl::variabletype_constructor_exists():
    assert callable(aDSL::VariableType.__init__)


def test_adsl::variabletype_constructor_args():
    sig = inspect.signature(aDSL::VariableType.__init__)
    params = list(sig.parameters.keys())
    assert "isarray" in params, "Missing parameter 'isarray'"

def test_adsl::variabletype_has_isarray():
    assert hasattr(aDSL::VariableType, "isarray")
    descriptor = None
    for klass in aDSL::VariableType.__mro__:
        if "isarray" in klass.__dict__:
            descriptor = klass.__dict__["isarray"]
            break
    assert isinstance(descriptor, property)



def test_adsl::xclass_is_not_abstract():
    assert not inspect.isabstract(aDSL::XClass)


def test_adsl::xclass_constructor_exists():
    assert callable(aDSL::XClass.__init__)


def test_adsl::xclass_constructor_args():
    sig = inspect.signature(aDSL::XClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adsl::xclass_has_name():
    assert hasattr(aDSL::XClass, "name")
    descriptor = None
    for klass in aDSL::XClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adsl::abstractelements_is_not_abstract():
    assert not inspect.isabstract(aDSL::AbstractElements)


def test_adsl::abstractelements_constructor_exists():
    assert callable(aDSL::AbstractElements.__init__)


def test_adsl::abstractelements_constructor_args():
    sig = inspect.signature(aDSL::AbstractElements.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_adsl::abstractelements_has_importedNamespace():
    assert hasattr(aDSL::AbstractElements, "importedNamespace")
    descriptor = None
    for klass in aDSL::AbstractElements.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_adsl::program_is_not_abstract():
    assert not inspect.isabstract(aDSL::Program)


def test_adsl::program_constructor_exists():
    assert callable(aDSL::Program.__init__)


def test_adsl::program_constructor_args():
    sig = inspect.signature(aDSL::Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adsl::program_has_name():
    assert hasattr(aDSL::Program, "name")
    descriptor = None
    for klass in aDSL::Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
aDSL::IntegerNegative_strategy = st.builds(
    aDSL::IntegerNegative,
    isneg=
        st.booleans(),
    value=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
aDSL::Equality_strategy = st.builds(
    aDSL::Equality,
    op=
        safe_text
)
aDSL::And_strategy = st.builds(
    aDSL::And,
)
aDSL::Plus_strategy = st.builds(
    aDSL::Plus,
)
aDSL::StringConstant_strategy = st.builds(
    aDSL::StringConstant,
    value=
        safe_text
)
aDSL::Or_strategy = st.builds(
    aDSL::Or,
)
aDSL::Minus_strategy = st.builds(
    aDSL::Minus,
)
aDSL::MemberSelection_strategy = st.builds(
    aDSL::MemberSelection,
    methodinvocation=
        st.booleans(),
    ispar=
        st.booleans()
)
aDSL::Comparison_strategy = st.builds(
    aDSL::Comparison,
    op=
        safe_text
)
aDSL::Assignment_strategy = st.builds(
    aDSL::Assignment,
)
aDSL::Block_strategy = st.builds(
    aDSL::Block,
    ispar=
        st.booleans()
)
aDSL::Statement_strategy = st.builds(
    aDSL::Statement,
)
aDSL::VarDef_strategy = st.builds(
    aDSL::VarDef,
)
Statement_strategy = st.builds(
    Statement,
)
aDSL::ForStat_strategy = st.builds(
    aDSL::ForStat,
)
aDSL::Expression_strategy = st.builds(
    aDSL::Expression,
)
aDSL::For2Statement_strategy = st.builds(
    aDSL::For2Statement,
)
aDSL::FinishStat_strategy = st.builds(
    aDSL::FinishStat,
)
aDSL::WhileStat_strategy = st.builds(
    aDSL::WhileStat,
)
aDSL::TryCatchStat_strategy = st.builds(
    aDSL::TryCatchStat,
    name=
        safe_text
)
aDSL::ReturnStat_strategy = st.builds(
    aDSL::ReturnStat,
)
aDSL::WhenStatement_strategy = st.builds(
    aDSL::WhenStatement,
)
aDSL::AsyncStat_strategy = st.builds(
    aDSL::AsyncStat,
)
aDSL::AtStat_strategy = st.builds(
    aDSL::AtStat,
)
aDSL::IfStat_strategy = st.builds(
    aDSL::IfStat,
    iselse=
        st.booleans()
)
aDSL::AtomicStatement_strategy = st.builds(
    aDSL::AtomicStatement,
)
aDSL::Body_strategy = st.builds(
    aDSL::Body,
)
aDSL::Init_strategy = st.builds(
    aDSL::Init,
)
aDSL::Not_strategy = st.builds(
    aDSL::Not,
)
aDSL::MulOrDiv_strategy = st.builds(
    aDSL::MulOrDiv,
    op=
        safe_text
)
aDSL::New_strategy = st.builds(
    aDSL::New,
)
aDSL::Reference_strategy = st.builds(
    aDSL::Reference,
    isarray=
        st.booleans()
)
aDSL::Here_strategy = st.builds(
    aDSL::Here,
)
aDSL::Null_strategy = st.builds(
    aDSL::Null,
)
aDSL::This_strategy = st.builds(
    aDSL::This,
)
aDSL::DeRef_strategy = st.builds(
    aDSL::DeRef,
)
aDSL::BoolConstant_strategy = st.builds(
    aDSL::BoolConstant,
    value=
        safe_text
)
aDSL::IntConstant_strategy = st.builds(
    aDSL::IntConstant,
)
Member_strategy = st.builds(
    Member,
)
aDSL::PrintInst_strategy = st.builds(
    aDSL::PrintInst,
)
aDSL::MainMethod_strategy = st.builds(
    aDSL::MainMethod,
)
SharedDef_strategy = st.builds(
    SharedDef,
)
aDSL::SharedVarDef_strategy = st.builds(
    aDSL::SharedVarDef,
)
aDSL::SharedArrayDef_strategy = st.builds(
    aDSL::SharedArrayDef,
)
aDSL::Operator_strategy = st.builds(
    aDSL::Operator,
    opName=
        safe_text
)
aDSL::Method_strategy = st.builds(
    aDSL::Method,
    istyped=
        st.booleans(),
    name=
        safe_text,
    isconst=
        st.booleans()
)
aDSL::Member_strategy = st.builds(
    aDSL::Member,
)
VarDef_strategy = st.builds(
    VarDef,
)
aDSL::VariableDef_strategy = st.builds(
    aDSL::VariableDef,
    vartype=
        safe_text,
    istyped=
        st.booleans(),
    name=
        safe_text,
    isstatic=
        st.booleans(),
    isinit=
        st.booleans()
)
aDSL::FuncVarDef_strategy = st.builds(
    aDSL::FuncVarDef,
    name=
        safe_text
)
aDSL::SharedDef_strategy = st.builds(
    aDSL::SharedDef,
    name=
        safe_text,
    replicas=
        st.booleans()
)
aDSL::Parameter_strategy = st.builds(
    aDSL::Parameter,
    istyped=
        st.booleans(),
    name=
        safe_text
)
aDSL::VariableType_strategy = st.builds(
    aDSL::VariableType,
    isarray=
        st.booleans()
)
aDSL::XClass_strategy = st.builds(
    aDSL::XClass,
    name=
        safe_text
)
aDSL::AbstractElements_strategy = st.builds(
    aDSL::AbstractElements,
    importedNamespace=
        safe_text
)
aDSL::Program_strategy = st.builds(
    aDSL::Program,
    name=
        safe_text
)

@given(instance=aDSL::IntegerNegative_strategy)
@settings(max_examples=50)
def test_adsl::integernegative_instantiation(instance):
    assert isinstance(instance, aDSL::IntegerNegative)

@given(instance=aDSL::IntegerNegative_strategy)
def test_adsl::integernegative_isneg_type(instance):
    assert isinstance(instance.isneg, bool)


@given(instance=aDSL::IntegerNegative_strategy)
def test_adsl::integernegative_isneg_setter(instance):
    original = instance.isneg
    instance.isneg = original
    assert instance.isneg == original

@given(instance=aDSL::IntegerNegative_strategy)
def test_adsl::integernegative_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=aDSL::IntegerNegative_strategy)
def test_adsl::integernegative_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=aDSL::Equality_strategy)
@settings(max_examples=50)
def test_adsl::equality_instantiation(instance):
    assert isinstance(instance, aDSL::Equality)

@given(instance=aDSL::Equality_strategy)
def test_adsl::equality_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=aDSL::Equality_strategy)
def test_adsl::equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=aDSL::And_strategy)
@settings(max_examples=50)
def test_adsl::and_instantiation(instance):
    assert isinstance(instance, aDSL::And)

@given(instance=aDSL::Plus_strategy)
@settings(max_examples=50)
def test_adsl::plus_instantiation(instance):
    assert isinstance(instance, aDSL::Plus)

@given(instance=aDSL::StringConstant_strategy)
@settings(max_examples=50)
def test_adsl::stringconstant_instantiation(instance):
    assert isinstance(instance, aDSL::StringConstant)

@given(instance=aDSL::StringConstant_strategy)
def test_adsl::stringconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=aDSL::StringConstant_strategy)
def test_adsl::stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aDSL::Or_strategy)
@settings(max_examples=50)
def test_adsl::or_instantiation(instance):
    assert isinstance(instance, aDSL::Or)

@given(instance=aDSL::Minus_strategy)
@settings(max_examples=50)
def test_adsl::minus_instantiation(instance):
    assert isinstance(instance, aDSL::Minus)

@given(instance=aDSL::MemberSelection_strategy)
@settings(max_examples=50)
def test_adsl::memberselection_instantiation(instance):
    assert isinstance(instance, aDSL::MemberSelection)

@given(instance=aDSL::MemberSelection_strategy)
def test_adsl::memberselection_methodinvocation_type(instance):
    assert isinstance(instance.methodinvocation, bool)


@given(instance=aDSL::MemberSelection_strategy)
def test_adsl::memberselection_methodinvocation_setter(instance):
    original = instance.methodinvocation
    instance.methodinvocation = original
    assert instance.methodinvocation == original

@given(instance=aDSL::MemberSelection_strategy)
def test_adsl::memberselection_ispar_type(instance):
    assert isinstance(instance.ispar, bool)


@given(instance=aDSL::MemberSelection_strategy)
def test_adsl::memberselection_ispar_setter(instance):
    original = instance.ispar
    instance.ispar = original
    assert instance.ispar == original

@given(instance=aDSL::Comparison_strategy)
@settings(max_examples=50)
def test_adsl::comparison_instantiation(instance):
    assert isinstance(instance, aDSL::Comparison)

@given(instance=aDSL::Comparison_strategy)
def test_adsl::comparison_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=aDSL::Comparison_strategy)
def test_adsl::comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=aDSL::Assignment_strategy)
@settings(max_examples=50)
def test_adsl::assignment_instantiation(instance):
    assert isinstance(instance, aDSL::Assignment)

@given(instance=aDSL::Block_strategy)
@settings(max_examples=50)
def test_adsl::block_instantiation(instance):
    assert isinstance(instance, aDSL::Block)

@given(instance=aDSL::Block_strategy)
def test_adsl::block_ispar_type(instance):
    assert isinstance(instance.ispar, bool)


@given(instance=aDSL::Block_strategy)
def test_adsl::block_ispar_setter(instance):
    original = instance.ispar
    instance.ispar = original
    assert instance.ispar == original

@given(instance=aDSL::Statement_strategy)
@settings(max_examples=50)
def test_adsl::statement_instantiation(instance):
    assert isinstance(instance, aDSL::Statement)

@given(instance=aDSL::VarDef_strategy)
@settings(max_examples=50)
def test_adsl::vardef_instantiation(instance):
    assert isinstance(instance, aDSL::VarDef)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=aDSL::ForStat_strategy)
@settings(max_examples=50)
def test_adsl::forstat_instantiation(instance):
    assert isinstance(instance, aDSL::ForStat)

@given(instance=aDSL::Expression_strategy)
@settings(max_examples=50)
def test_adsl::expression_instantiation(instance):
    assert isinstance(instance, aDSL::Expression)

@given(instance=aDSL::For2Statement_strategy)
@settings(max_examples=50)
def test_adsl::for2statement_instantiation(instance):
    assert isinstance(instance, aDSL::For2Statement)

@given(instance=aDSL::FinishStat_strategy)
@settings(max_examples=50)
def test_adsl::finishstat_instantiation(instance):
    assert isinstance(instance, aDSL::FinishStat)

@given(instance=aDSL::WhileStat_strategy)
@settings(max_examples=50)
def test_adsl::whilestat_instantiation(instance):
    assert isinstance(instance, aDSL::WhileStat)

@given(instance=aDSL::TryCatchStat_strategy)
@settings(max_examples=50)
def test_adsl::trycatchstat_instantiation(instance):
    assert isinstance(instance, aDSL::TryCatchStat)

@given(instance=aDSL::TryCatchStat_strategy)
def test_adsl::trycatchstat_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aDSL::TryCatchStat_strategy)
def test_adsl::trycatchstat_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aDSL::ReturnStat_strategy)
@settings(max_examples=50)
def test_adsl::returnstat_instantiation(instance):
    assert isinstance(instance, aDSL::ReturnStat)

@given(instance=aDSL::WhenStatement_strategy)
@settings(max_examples=50)
def test_adsl::whenstatement_instantiation(instance):
    assert isinstance(instance, aDSL::WhenStatement)

@given(instance=aDSL::AsyncStat_strategy)
@settings(max_examples=50)
def test_adsl::asyncstat_instantiation(instance):
    assert isinstance(instance, aDSL::AsyncStat)

@given(instance=aDSL::AtStat_strategy)
@settings(max_examples=50)
def test_adsl::atstat_instantiation(instance):
    assert isinstance(instance, aDSL::AtStat)

@given(instance=aDSL::IfStat_strategy)
@settings(max_examples=50)
def test_adsl::ifstat_instantiation(instance):
    assert isinstance(instance, aDSL::IfStat)

@given(instance=aDSL::IfStat_strategy)
def test_adsl::ifstat_iselse_type(instance):
    assert isinstance(instance.iselse, bool)


@given(instance=aDSL::IfStat_strategy)
def test_adsl::ifstat_iselse_setter(instance):
    original = instance.iselse
    instance.iselse = original
    assert instance.iselse == original

@given(instance=aDSL::AtomicStatement_strategy)
@settings(max_examples=50)
def test_adsl::atomicstatement_instantiation(instance):
    assert isinstance(instance, aDSL::AtomicStatement)

@given(instance=aDSL::Body_strategy)
@settings(max_examples=50)
def test_adsl::body_instantiation(instance):
    assert isinstance(instance, aDSL::Body)

@given(instance=aDSL::Init_strategy)
@settings(max_examples=50)
def test_adsl::init_instantiation(instance):
    assert isinstance(instance, aDSL::Init)

@given(instance=aDSL::Not_strategy)
@settings(max_examples=50)
def test_adsl::not_instantiation(instance):
    assert isinstance(instance, aDSL::Not)

@given(instance=aDSL::MulOrDiv_strategy)
@settings(max_examples=50)
def test_adsl::mulordiv_instantiation(instance):
    assert isinstance(instance, aDSL::MulOrDiv)

@given(instance=aDSL::MulOrDiv_strategy)
def test_adsl::mulordiv_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=aDSL::MulOrDiv_strategy)
def test_adsl::mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=aDSL::New_strategy)
@settings(max_examples=50)
def test_adsl::new_instantiation(instance):
    assert isinstance(instance, aDSL::New)

@given(instance=aDSL::Reference_strategy)
@settings(max_examples=50)
def test_adsl::reference_instantiation(instance):
    assert isinstance(instance, aDSL::Reference)

@given(instance=aDSL::Reference_strategy)
def test_adsl::reference_isarray_type(instance):
    assert isinstance(instance.isarray, bool)


@given(instance=aDSL::Reference_strategy)
def test_adsl::reference_isarray_setter(instance):
    original = instance.isarray
    instance.isarray = original
    assert instance.isarray == original

@given(instance=aDSL::Here_strategy)
@settings(max_examples=50)
def test_adsl::here_instantiation(instance):
    assert isinstance(instance, aDSL::Here)

@given(instance=aDSL::Null_strategy)
@settings(max_examples=50)
def test_adsl::null_instantiation(instance):
    assert isinstance(instance, aDSL::Null)

@given(instance=aDSL::This_strategy)
@settings(max_examples=50)
def test_adsl::this_instantiation(instance):
    assert isinstance(instance, aDSL::This)

@given(instance=aDSL::DeRef_strategy)
@settings(max_examples=50)
def test_adsl::deref_instantiation(instance):
    assert isinstance(instance, aDSL::DeRef)

@given(instance=aDSL::BoolConstant_strategy)
@settings(max_examples=50)
def test_adsl::boolconstant_instantiation(instance):
    assert isinstance(instance, aDSL::BoolConstant)

@given(instance=aDSL::BoolConstant_strategy)
def test_adsl::boolconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=aDSL::BoolConstant_strategy)
def test_adsl::boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aDSL::IntConstant_strategy)
@settings(max_examples=50)
def test_adsl::intconstant_instantiation(instance):
    assert isinstance(instance, aDSL::IntConstant)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=aDSL::PrintInst_strategy)
@settings(max_examples=50)
def test_adsl::printinst_instantiation(instance):
    assert isinstance(instance, aDSL::PrintInst)

@given(instance=aDSL::MainMethod_strategy)
@settings(max_examples=50)
def test_adsl::mainmethod_instantiation(instance):
    assert isinstance(instance, aDSL::MainMethod)

@given(instance=SharedDef_strategy)
@settings(max_examples=50)
def test_shareddef_instantiation(instance):
    assert isinstance(instance, SharedDef)

@given(instance=aDSL::SharedVarDef_strategy)
@settings(max_examples=50)
def test_adsl::sharedvardef_instantiation(instance):
    assert isinstance(instance, aDSL::SharedVarDef)

@given(instance=aDSL::SharedArrayDef_strategy)
@settings(max_examples=50)
def test_adsl::sharedarraydef_instantiation(instance):
    assert isinstance(instance, aDSL::SharedArrayDef)

@given(instance=aDSL::Operator_strategy)
@settings(max_examples=50)
def test_adsl::operator_instantiation(instance):
    assert isinstance(instance, aDSL::Operator)

@given(instance=aDSL::Operator_strategy)
def test_adsl::operator_opName_type(instance):
    assert isinstance(instance.opName, str)


@given(instance=aDSL::Operator_strategy)
def test_adsl::operator_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=aDSL::Method_strategy)
@settings(max_examples=50)
def test_adsl::method_instantiation(instance):
    assert isinstance(instance, aDSL::Method)

@given(instance=aDSL::Method_strategy)
def test_adsl::method_istyped_type(instance):
    assert isinstance(instance.istyped, bool)


@given(instance=aDSL::Method_strategy)
def test_adsl::method_istyped_setter(instance):
    original = instance.istyped
    instance.istyped = original
    assert instance.istyped == original

@given(instance=aDSL::Method_strategy)
def test_adsl::method_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aDSL::Method_strategy)
def test_adsl::method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aDSL::Method_strategy)
def test_adsl::method_isconst_type(instance):
    assert isinstance(instance.isconst, bool)


@given(instance=aDSL::Method_strategy)
def test_adsl::method_isconst_setter(instance):
    original = instance.isconst
    instance.isconst = original
    assert instance.isconst == original

@given(instance=aDSL::Member_strategy)
@settings(max_examples=50)
def test_adsl::member_instantiation(instance):
    assert isinstance(instance, aDSL::Member)

@given(instance=VarDef_strategy)
@settings(max_examples=50)
def test_vardef_instantiation(instance):
    assert isinstance(instance, VarDef)

@given(instance=aDSL::VariableDef_strategy)
@settings(max_examples=50)
def test_adsl::variabledef_instantiation(instance):
    assert isinstance(instance, aDSL::VariableDef)

@given(instance=aDSL::VariableDef_strategy)
def test_adsl::variabledef_vartype_type(instance):
    assert isinstance(instance.vartype, str)


@given(instance=aDSL::VariableDef_strategy)
def test_adsl::variabledef_vartype_setter(instance):
    original = instance.vartype
    instance.vartype = original
    assert instance.vartype == original

@given(instance=aDSL::VariableDef_strategy)
def test_adsl::variabledef_istyped_type(instance):
    assert isinstance(instance.istyped, bool)


@given(instance=aDSL::VariableDef_strategy)
def test_adsl::variabledef_istyped_setter(instance):
    original = instance.istyped
    instance.istyped = original
    assert instance.istyped == original

@given(instance=aDSL::VariableDef_strategy)
def test_adsl::variabledef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aDSL::VariableDef_strategy)
def test_adsl::variabledef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aDSL::VariableDef_strategy)
def test_adsl::variabledef_isstatic_type(instance):
    assert isinstance(instance.isstatic, bool)


@given(instance=aDSL::VariableDef_strategy)
def test_adsl::variabledef_isstatic_setter(instance):
    original = instance.isstatic
    instance.isstatic = original
    assert instance.isstatic == original

@given(instance=aDSL::VariableDef_strategy)
def test_adsl::variabledef_isinit_type(instance):
    assert isinstance(instance.isinit, bool)


@given(instance=aDSL::VariableDef_strategy)
def test_adsl::variabledef_isinit_setter(instance):
    original = instance.isinit
    instance.isinit = original
    assert instance.isinit == original

@given(instance=aDSL::FuncVarDef_strategy)
@settings(max_examples=50)
def test_adsl::funcvardef_instantiation(instance):
    assert isinstance(instance, aDSL::FuncVarDef)

@given(instance=aDSL::FuncVarDef_strategy)
def test_adsl::funcvardef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aDSL::FuncVarDef_strategy)
def test_adsl::funcvardef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aDSL::SharedDef_strategy)
@settings(max_examples=50)
def test_adsl::shareddef_instantiation(instance):
    assert isinstance(instance, aDSL::SharedDef)

@given(instance=aDSL::SharedDef_strategy)
def test_adsl::shareddef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aDSL::SharedDef_strategy)
def test_adsl::shareddef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aDSL::SharedDef_strategy)
def test_adsl::shareddef_replicas_type(instance):
    assert isinstance(instance.replicas, bool)


@given(instance=aDSL::SharedDef_strategy)
def test_adsl::shareddef_replicas_setter(instance):
    original = instance.replicas
    instance.replicas = original
    assert instance.replicas == original

@given(instance=aDSL::Parameter_strategy)
@settings(max_examples=50)
def test_adsl::parameter_instantiation(instance):
    assert isinstance(instance, aDSL::Parameter)

@given(instance=aDSL::Parameter_strategy)
def test_adsl::parameter_istyped_type(instance):
    assert isinstance(instance.istyped, bool)


@given(instance=aDSL::Parameter_strategy)
def test_adsl::parameter_istyped_setter(instance):
    original = instance.istyped
    instance.istyped = original
    assert instance.istyped == original

@given(instance=aDSL::Parameter_strategy)
def test_adsl::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aDSL::Parameter_strategy)
def test_adsl::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aDSL::VariableType_strategy)
@settings(max_examples=50)
def test_adsl::variabletype_instantiation(instance):
    assert isinstance(instance, aDSL::VariableType)

@given(instance=aDSL::VariableType_strategy)
def test_adsl::variabletype_isarray_type(instance):
    assert isinstance(instance.isarray, bool)


@given(instance=aDSL::VariableType_strategy)
def test_adsl::variabletype_isarray_setter(instance):
    original = instance.isarray
    instance.isarray = original
    assert instance.isarray == original

@given(instance=aDSL::XClass_strategy)
@settings(max_examples=50)
def test_adsl::xclass_instantiation(instance):
    assert isinstance(instance, aDSL::XClass)

@given(instance=aDSL::XClass_strategy)
def test_adsl::xclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aDSL::XClass_strategy)
def test_adsl::xclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aDSL::AbstractElements_strategy)
@settings(max_examples=50)
def test_adsl::abstractelements_instantiation(instance):
    assert isinstance(instance, aDSL::AbstractElements)

@given(instance=aDSL::AbstractElements_strategy)
def test_adsl::abstractelements_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=aDSL::AbstractElements_strategy)
def test_adsl::abstractelements_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=aDSL::Program_strategy)
@settings(max_examples=50)
def test_adsl::program_instantiation(instance):
    assert isinstance(instance, aDSL::Program)

@given(instance=aDSL::Program_strategy)
def test_adsl::program_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aDSL::Program_strategy)
def test_adsl::program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
