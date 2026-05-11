import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    b::Program,
    ReturnTypeExpr,
    b::ReturnOr,
    PropertyExpr,
    b::PropertyTyped,
    ReturnExpr,
    b::Neg,
    Type,
    b::PrimitiveType,
    b::SimpleCall,
    b::PropertyRange,
    Return,
    b::ReturnTuple,
    b::ReturnTypeExpr,
    b::ReturnExpr,
    Statement,
    b::BeginBody,
    BeginBody,
    b::FinalExpr,
    b::CaseExpr,
    b::Statement,
    Expr,
    b::Assign,
    b::Call,
    Body,
    b::Seq,
    b::Begin,
    b::Skip,
    b::Expr,
    b::Body,
    b::Operation,
    b::PreExpr,
    b::Pre,
    b::Condition,
    b::IfCond,
    FinalExpr,
    b::Var,
    b::Case,
    b::Return,
    b::If,
    b::LogicalExpr,
    b::Definition,
    b::AssertionExpr,
    b::Range,
    b::Set,
    Arg,
    b::StringLiteral,
    b::ArgMinus,
    Condition,
    b::CondAnd,
    b::CondLessThan,
    b::BoolLiteral,
    b::CondMinus,
    b::CondEq,
    b::CondNeg,
    b::Arg,
    LogicalExpr,
    b::IntLiteral,
    b::Ref,
    b::EqualExpr,
    b::ConstantExpr,
    b::TypeConstraint,
    b::InequalityExpr,
    b::AndExpr,
    b::BoolTest,
    b::ImplyExpr,
    b::NegExpr,
    b::DefinitionCall,
    b::InvariantExpr,
    b::Variable,
    b::ValueExpr,
    b::PropertyExpr,
    b::InitialisationExpr,
    b::Type,
    b::Operations,
    b::Properties,
    b::Definitions,
    b::ConcreteConstants,
    b::Sees,
    b::Abstraction,
    b::LocalOperations,
    b::Values,
    b::Imports,
    b::Sets,
    b::Assertions,
    b::Initialisation,
    b::Invariant,
    b::ConcreteVariables,
    Abstraction,
    b::Implementation,
    b::Machine,
    PrimitiveTypeEnum,
    BoolLiteralEnum,
    InequalityOp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b::program_is_not_abstract():
    assert not inspect.isabstract(b::Program)


def test_b::program_constructor_exists():
    assert callable(b::Program.__init__)


def test_b::program_constructor_args():
    sig = inspect.signature(b::Program.__init__)
    params = list(sig.parameters.keys())



def test_returntypeexpr_is_not_abstract():
    assert not inspect.isabstract(ReturnTypeExpr)


def test_returntypeexpr_constructor_exists():
    assert callable(ReturnTypeExpr.__init__)


def test_returntypeexpr_constructor_args():
    sig = inspect.signature(ReturnTypeExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::returnor_is_not_abstract():
    assert not inspect.isabstract(b::ReturnOr)


def test_b::returnor_constructor_exists():
    assert callable(b::ReturnOr.__init__)


def test_b::returnor_constructor_args():
    sig = inspect.signature(b::ReturnOr.__init__)
    params = list(sig.parameters.keys())



def test_propertyexpr_is_not_abstract():
    assert not inspect.isabstract(PropertyExpr)


def test_propertyexpr_constructor_exists():
    assert callable(PropertyExpr.__init__)


def test_propertyexpr_constructor_args():
    sig = inspect.signature(PropertyExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::propertytyped_is_not_abstract():
    assert not inspect.isabstract(b::PropertyTyped)


def test_b::propertytyped_constructor_exists():
    assert callable(b::PropertyTyped.__init__)


def test_b::propertytyped_constructor_args():
    sig = inspect.signature(b::PropertyTyped.__init__)
    params = list(sig.parameters.keys())



def test_returnexpr_is_not_abstract():
    assert not inspect.isabstract(ReturnExpr)


def test_returnexpr_constructor_exists():
    assert callable(ReturnExpr.__init__)


def test_returnexpr_constructor_args():
    sig = inspect.signature(ReturnExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::neg_is_not_abstract():
    assert not inspect.isabstract(b::Neg)


def test_b::neg_constructor_exists():
    assert callable(b::Neg.__init__)


def test_b::neg_constructor_args():
    sig = inspect.signature(b::Neg.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_b::primitivetype_is_not_abstract():
    assert not inspect.isabstract(b::PrimitiveType)


def test_b::primitivetype_constructor_exists():
    assert callable(b::PrimitiveType.__init__)


def test_b::primitivetype_constructor_args():
    sig = inspect.signature(b::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_b::primitivetype_has_type():
    assert hasattr(b::PrimitiveType, "type")
    descriptor = None
    for klass in b::PrimitiveType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_b::simplecall_is_not_abstract():
    assert not inspect.isabstract(b::SimpleCall)


def test_b::simplecall_constructor_exists():
    assert callable(b::SimpleCall.__init__)


def test_b::simplecall_constructor_args():
    sig = inspect.signature(b::SimpleCall.__init__)
    params = list(sig.parameters.keys())



def test_b::propertyrange_is_not_abstract():
    assert not inspect.isabstract(b::PropertyRange)


def test_b::propertyrange_constructor_exists():
    assert callable(b::PropertyRange.__init__)


def test_b::propertyrange_constructor_args():
    sig = inspect.signature(b::PropertyRange.__init__)
    params = list(sig.parameters.keys())



def test_return_is_not_abstract():
    assert not inspect.isabstract(Return)


def test_return_constructor_exists():
    assert callable(Return.__init__)


def test_return_constructor_args():
    sig = inspect.signature(Return.__init__)
    params = list(sig.parameters.keys())



def test_b::returntuple_is_not_abstract():
    assert not inspect.isabstract(b::ReturnTuple)


def test_b::returntuple_constructor_exists():
    assert callable(b::ReturnTuple.__init__)


def test_b::returntuple_constructor_args():
    sig = inspect.signature(b::ReturnTuple.__init__)
    params = list(sig.parameters.keys())



def test_b::returntypeexpr_is_not_abstract():
    assert not inspect.isabstract(b::ReturnTypeExpr)


def test_b::returntypeexpr_constructor_exists():
    assert callable(b::ReturnTypeExpr.__init__)


def test_b::returntypeexpr_constructor_args():
    sig = inspect.signature(b::ReturnTypeExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::returnexpr_is_not_abstract():
    assert not inspect.isabstract(b::ReturnExpr)


def test_b::returnexpr_constructor_exists():
    assert callable(b::ReturnExpr.__init__)


def test_b::returnexpr_constructor_args():
    sig = inspect.signature(b::ReturnExpr.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_b::beginbody_is_not_abstract():
    assert not inspect.isabstract(b::BeginBody)


def test_b::beginbody_constructor_exists():
    assert callable(b::BeginBody.__init__)


def test_b::beginbody_constructor_args():
    sig = inspect.signature(b::BeginBody.__init__)
    params = list(sig.parameters.keys())



def test_beginbody_is_not_abstract():
    assert not inspect.isabstract(BeginBody)


def test_beginbody_constructor_exists():
    assert callable(BeginBody.__init__)


def test_beginbody_constructor_args():
    sig = inspect.signature(BeginBody.__init__)
    params = list(sig.parameters.keys())



def test_b::finalexpr_is_not_abstract():
    assert not inspect.isabstract(b::FinalExpr)


def test_b::finalexpr_constructor_exists():
    assert callable(b::FinalExpr.__init__)


def test_b::finalexpr_constructor_args():
    sig = inspect.signature(b::FinalExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::caseexpr_is_not_abstract():
    assert not inspect.isabstract(b::CaseExpr)


def test_b::caseexpr_constructor_exists():
    assert callable(b::CaseExpr.__init__)


def test_b::caseexpr_constructor_args():
    sig = inspect.signature(b::CaseExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::statement_is_not_abstract():
    assert not inspect.isabstract(b::Statement)


def test_b::statement_constructor_exists():
    assert callable(b::Statement.__init__)


def test_b::statement_constructor_args():
    sig = inspect.signature(b::Statement.__init__)
    params = list(sig.parameters.keys())



def test_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_b::assign_is_not_abstract():
    assert not inspect.isabstract(b::Assign)


def test_b::assign_constructor_exists():
    assert callable(b::Assign.__init__)


def test_b::assign_constructor_args():
    sig = inspect.signature(b::Assign.__init__)
    params = list(sig.parameters.keys())



def test_b::call_is_not_abstract():
    assert not inspect.isabstract(b::Call)


def test_b::call_constructor_exists():
    assert callable(b::Call.__init__)


def test_b::call_constructor_args():
    sig = inspect.signature(b::Call.__init__)
    params = list(sig.parameters.keys())



def test_body_is_not_abstract():
    assert not inspect.isabstract(Body)


def test_body_constructor_exists():
    assert callable(Body.__init__)


def test_body_constructor_args():
    sig = inspect.signature(Body.__init__)
    params = list(sig.parameters.keys())



def test_b::seq_is_not_abstract():
    assert not inspect.isabstract(b::Seq)


def test_b::seq_constructor_exists():
    assert callable(b::Seq.__init__)


def test_b::seq_constructor_args():
    sig = inspect.signature(b::Seq.__init__)
    params = list(sig.parameters.keys())



def test_b::begin_is_not_abstract():
    assert not inspect.isabstract(b::Begin)


def test_b::begin_constructor_exists():
    assert callable(b::Begin.__init__)


def test_b::begin_constructor_args():
    sig = inspect.signature(b::Begin.__init__)
    params = list(sig.parameters.keys())



def test_b::skip_is_not_abstract():
    assert not inspect.isabstract(b::Skip)


def test_b::skip_constructor_exists():
    assert callable(b::Skip.__init__)


def test_b::skip_constructor_args():
    sig = inspect.signature(b::Skip.__init__)
    params = list(sig.parameters.keys())



def test_b::expr_is_not_abstract():
    assert not inspect.isabstract(b::Expr)


def test_b::expr_constructor_exists():
    assert callable(b::Expr.__init__)


def test_b::expr_constructor_args():
    sig = inspect.signature(b::Expr.__init__)
    params = list(sig.parameters.keys())



def test_b::body_is_not_abstract():
    assert not inspect.isabstract(b::Body)


def test_b::body_constructor_exists():
    assert callable(b::Body.__init__)


def test_b::body_constructor_args():
    sig = inspect.signature(b::Body.__init__)
    params = list(sig.parameters.keys())



def test_b::operation_is_not_abstract():
    assert not inspect.isabstract(b::Operation)


def test_b::operation_constructor_exists():
    assert callable(b::Operation.__init__)


def test_b::operation_constructor_args():
    sig = inspect.signature(b::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b::operation_has_name():
    assert hasattr(b::Operation, "name")
    descriptor = None
    for klass in b::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_b::preexpr_is_not_abstract():
    assert not inspect.isabstract(b::PreExpr)


def test_b::preexpr_constructor_exists():
    assert callable(b::PreExpr.__init__)


def test_b::preexpr_constructor_args():
    sig = inspect.signature(b::PreExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::pre_is_not_abstract():
    assert not inspect.isabstract(b::Pre)


def test_b::pre_constructor_exists():
    assert callable(b::Pre.__init__)


def test_b::pre_constructor_args():
    sig = inspect.signature(b::Pre.__init__)
    params = list(sig.parameters.keys())



def test_b::condition_is_not_abstract():
    assert not inspect.isabstract(b::Condition)


def test_b::condition_constructor_exists():
    assert callable(b::Condition.__init__)


def test_b::condition_constructor_args():
    sig = inspect.signature(b::Condition.__init__)
    params = list(sig.parameters.keys())



def test_b::ifcond_is_not_abstract():
    assert not inspect.isabstract(b::IfCond)


def test_b::ifcond_constructor_exists():
    assert callable(b::IfCond.__init__)


def test_b::ifcond_constructor_args():
    sig = inspect.signature(b::IfCond.__init__)
    params = list(sig.parameters.keys())



def test_finalexpr_is_not_abstract():
    assert not inspect.isabstract(FinalExpr)


def test_finalexpr_constructor_exists():
    assert callable(FinalExpr.__init__)


def test_finalexpr_constructor_args():
    sig = inspect.signature(FinalExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::var_is_not_abstract():
    assert not inspect.isabstract(b::Var)


def test_b::var_constructor_exists():
    assert callable(b::Var.__init__)


def test_b::var_constructor_args():
    sig = inspect.signature(b::Var.__init__)
    params = list(sig.parameters.keys())



def test_b::case_is_not_abstract():
    assert not inspect.isabstract(b::Case)


def test_b::case_constructor_exists():
    assert callable(b::Case.__init__)


def test_b::case_constructor_args():
    sig = inspect.signature(b::Case.__init__)
    params = list(sig.parameters.keys())



def test_b::return_is_not_abstract():
    assert not inspect.isabstract(b::Return)


def test_b::return_constructor_exists():
    assert callable(b::Return.__init__)


def test_b::return_constructor_args():
    sig = inspect.signature(b::Return.__init__)
    params = list(sig.parameters.keys())



def test_b::if_is_not_abstract():
    assert not inspect.isabstract(b::If)


def test_b::if_constructor_exists():
    assert callable(b::If.__init__)


def test_b::if_constructor_args():
    sig = inspect.signature(b::If.__init__)
    params = list(sig.parameters.keys())



def test_b::logicalexpr_is_not_abstract():
    assert not inspect.isabstract(b::LogicalExpr)


def test_b::logicalexpr_constructor_exists():
    assert callable(b::LogicalExpr.__init__)


def test_b::logicalexpr_constructor_args():
    sig = inspect.signature(b::LogicalExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::definition_is_not_abstract():
    assert not inspect.isabstract(b::Definition)


def test_b::definition_constructor_exists():
    assert callable(b::Definition.__init__)


def test_b::definition_constructor_args():
    sig = inspect.signature(b::Definition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b::definition_has_name():
    assert hasattr(b::Definition, "name")
    descriptor = None
    for klass in b::Definition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_b::assertionexpr_is_not_abstract():
    assert not inspect.isabstract(b::AssertionExpr)


def test_b::assertionexpr_constructor_exists():
    assert callable(b::AssertionExpr.__init__)


def test_b::assertionexpr_constructor_args():
    sig = inspect.signature(b::AssertionExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::range_is_not_abstract():
    assert not inspect.isabstract(b::Range)


def test_b::range_constructor_exists():
    assert callable(b::Range.__init__)


def test_b::range_constructor_args():
    sig = inspect.signature(b::Range.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_b::range_has_lowerBound():
    assert hasattr(b::Range, "lowerBound")
    descriptor = None
    for klass in b::Range.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)



def test_b::set_is_not_abstract():
    assert not inspect.isabstract(b::Set)


def test_b::set_constructor_exists():
    assert callable(b::Set.__init__)


def test_b::set_constructor_args():
    sig = inspect.signature(b::Set.__init__)
    params = list(sig.parameters.keys())



def test_arg_is_not_abstract():
    assert not inspect.isabstract(Arg)


def test_arg_constructor_exists():
    assert callable(Arg.__init__)


def test_arg_constructor_args():
    sig = inspect.signature(Arg.__init__)
    params = list(sig.parameters.keys())



def test_b::stringliteral_is_not_abstract():
    assert not inspect.isabstract(b::StringLiteral)


def test_b::stringliteral_constructor_exists():
    assert callable(b::StringLiteral.__init__)


def test_b::stringliteral_constructor_args():
    sig = inspect.signature(b::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_b::stringliteral_has_value():
    assert hasattr(b::StringLiteral, "value")
    descriptor = None
    for klass in b::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_b::argminus_is_not_abstract():
    assert not inspect.isabstract(b::ArgMinus)


def test_b::argminus_constructor_exists():
    assert callable(b::ArgMinus.__init__)


def test_b::argminus_constructor_args():
    sig = inspect.signature(b::ArgMinus.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_b::condand_is_not_abstract():
    assert not inspect.isabstract(b::CondAnd)


def test_b::condand_constructor_exists():
    assert callable(b::CondAnd.__init__)


def test_b::condand_constructor_args():
    sig = inspect.signature(b::CondAnd.__init__)
    params = list(sig.parameters.keys())



def test_b::condlessthan_is_not_abstract():
    assert not inspect.isabstract(b::CondLessThan)


def test_b::condlessthan_constructor_exists():
    assert callable(b::CondLessThan.__init__)


def test_b::condlessthan_constructor_args():
    sig = inspect.signature(b::CondLessThan.__init__)
    params = list(sig.parameters.keys())



def test_b::boolliteral_is_not_abstract():
    assert not inspect.isabstract(b::BoolLiteral)


def test_b::boolliteral_constructor_exists():
    assert callable(b::BoolLiteral.__init__)


def test_b::boolliteral_constructor_args():
    sig = inspect.signature(b::BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "constant" in params, "Missing parameter 'constant'"

def test_b::boolliteral_has_value():
    assert hasattr(b::BoolLiteral, "value")
    descriptor = None
    for klass in b::BoolLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_b::boolliteral_has_constant():
    assert hasattr(b::BoolLiteral, "constant")
    descriptor = None
    for klass in b::BoolLiteral.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_b::condminus_is_not_abstract():
    assert not inspect.isabstract(b::CondMinus)


def test_b::condminus_constructor_exists():
    assert callable(b::CondMinus.__init__)


def test_b::condminus_constructor_args():
    sig = inspect.signature(b::CondMinus.__init__)
    params = list(sig.parameters.keys())



def test_b::condeq_is_not_abstract():
    assert not inspect.isabstract(b::CondEq)


def test_b::condeq_constructor_exists():
    assert callable(b::CondEq.__init__)


def test_b::condeq_constructor_args():
    sig = inspect.signature(b::CondEq.__init__)
    params = list(sig.parameters.keys())



def test_b::condneg_is_not_abstract():
    assert not inspect.isabstract(b::CondNeg)


def test_b::condneg_constructor_exists():
    assert callable(b::CondNeg.__init__)


def test_b::condneg_constructor_args():
    sig = inspect.signature(b::CondNeg.__init__)
    params = list(sig.parameters.keys())



def test_b::arg_is_not_abstract():
    assert not inspect.isabstract(b::Arg)


def test_b::arg_constructor_exists():
    assert callable(b::Arg.__init__)


def test_b::arg_constructor_args():
    sig = inspect.signature(b::Arg.__init__)
    params = list(sig.parameters.keys())



def test_logicalexpr_is_not_abstract():
    assert not inspect.isabstract(LogicalExpr)


def test_logicalexpr_constructor_exists():
    assert callable(LogicalExpr.__init__)


def test_logicalexpr_constructor_args():
    sig = inspect.signature(LogicalExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::intliteral_is_not_abstract():
    assert not inspect.isabstract(b::IntLiteral)


def test_b::intliteral_constructor_exists():
    assert callable(b::IntLiteral.__init__)


def test_b::intliteral_constructor_args():
    sig = inspect.signature(b::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_b::intliteral_has_value():
    assert hasattr(b::IntLiteral, "value")
    descriptor = None
    for klass in b::IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_b::ref_is_not_abstract():
    assert not inspect.isabstract(b::Ref)


def test_b::ref_constructor_exists():
    assert callable(b::Ref.__init__)


def test_b::ref_constructor_args():
    sig = inspect.signature(b::Ref.__init__)
    params = list(sig.parameters.keys())



def test_b::equalexpr_is_not_abstract():
    assert not inspect.isabstract(b::EqualExpr)


def test_b::equalexpr_constructor_exists():
    assert callable(b::EqualExpr.__init__)


def test_b::equalexpr_constructor_args():
    sig = inspect.signature(b::EqualExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::constantexpr_is_not_abstract():
    assert not inspect.isabstract(b::ConstantExpr)


def test_b::constantexpr_constructor_exists():
    assert callable(b::ConstantExpr.__init__)


def test_b::constantexpr_constructor_args():
    sig = inspect.signature(b::ConstantExpr.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"

def test_b::constantexpr_has_constant():
    assert hasattr(b::ConstantExpr, "constant")
    descriptor = None
    for klass in b::ConstantExpr.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_b::typeconstraint_is_not_abstract():
    assert not inspect.isabstract(b::TypeConstraint)


def test_b::typeconstraint_constructor_exists():
    assert callable(b::TypeConstraint.__init__)


def test_b::typeconstraint_constructor_args():
    sig = inspect.signature(b::TypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_b::inequalityexpr_is_not_abstract():
    assert not inspect.isabstract(b::InequalityExpr)


def test_b::inequalityexpr_constructor_exists():
    assert callable(b::InequalityExpr.__init__)


def test_b::inequalityexpr_constructor_args():
    sig = inspect.signature(b::InequalityExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_b::inequalityexpr_has_op():
    assert hasattr(b::InequalityExpr, "op")
    descriptor = None
    for klass in b::InequalityExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_b::andexpr_is_not_abstract():
    assert not inspect.isabstract(b::AndExpr)


def test_b::andexpr_constructor_exists():
    assert callable(b::AndExpr.__init__)


def test_b::andexpr_constructor_args():
    sig = inspect.signature(b::AndExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::booltest_is_not_abstract():
    assert not inspect.isabstract(b::BoolTest)


def test_b::booltest_constructor_exists():
    assert callable(b::BoolTest.__init__)


def test_b::booltest_constructor_args():
    sig = inspect.signature(b::BoolTest.__init__)
    params = list(sig.parameters.keys())



def test_b::implyexpr_is_not_abstract():
    assert not inspect.isabstract(b::ImplyExpr)


def test_b::implyexpr_constructor_exists():
    assert callable(b::ImplyExpr.__init__)


def test_b::implyexpr_constructor_args():
    sig = inspect.signature(b::ImplyExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::negexpr_is_not_abstract():
    assert not inspect.isabstract(b::NegExpr)


def test_b::negexpr_constructor_exists():
    assert callable(b::NegExpr.__init__)


def test_b::negexpr_constructor_args():
    sig = inspect.signature(b::NegExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::definitioncall_is_not_abstract():
    assert not inspect.isabstract(b::DefinitionCall)


def test_b::definitioncall_constructor_exists():
    assert callable(b::DefinitionCall.__init__)


def test_b::definitioncall_constructor_args():
    sig = inspect.signature(b::DefinitionCall.__init__)
    params = list(sig.parameters.keys())



def test_b::invariantexpr_is_not_abstract():
    assert not inspect.isabstract(b::InvariantExpr)


def test_b::invariantexpr_constructor_exists():
    assert callable(b::InvariantExpr.__init__)


def test_b::invariantexpr_constructor_args():
    sig = inspect.signature(b::InvariantExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::variable_is_not_abstract():
    assert not inspect.isabstract(b::Variable)


def test_b::variable_constructor_exists():
    assert callable(b::Variable.__init__)


def test_b::variable_constructor_args():
    sig = inspect.signature(b::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b::variable_has_name():
    assert hasattr(b::Variable, "name")
    descriptor = None
    for klass in b::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_b::valueexpr_is_not_abstract():
    assert not inspect.isabstract(b::ValueExpr)


def test_b::valueexpr_constructor_exists():
    assert callable(b::ValueExpr.__init__)


def test_b::valueexpr_constructor_args():
    sig = inspect.signature(b::ValueExpr.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_b::valueexpr_has_value():
    assert hasattr(b::ValueExpr, "value")
    descriptor = None
    for klass in b::ValueExpr.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_b::propertyexpr_is_not_abstract():
    assert not inspect.isabstract(b::PropertyExpr)


def test_b::propertyexpr_constructor_exists():
    assert callable(b::PropertyExpr.__init__)


def test_b::propertyexpr_constructor_args():
    sig = inspect.signature(b::PropertyExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::initialisationexpr_is_not_abstract():
    assert not inspect.isabstract(b::InitialisationExpr)


def test_b::initialisationexpr_constructor_exists():
    assert callable(b::InitialisationExpr.__init__)


def test_b::initialisationexpr_constructor_args():
    sig = inspect.signature(b::InitialisationExpr.__init__)
    params = list(sig.parameters.keys())



def test_b::type_is_not_abstract():
    assert not inspect.isabstract(b::Type)


def test_b::type_constructor_exists():
    assert callable(b::Type.__init__)


def test_b::type_constructor_args():
    sig = inspect.signature(b::Type.__init__)
    params = list(sig.parameters.keys())



def test_b::operations_is_not_abstract():
    assert not inspect.isabstract(b::Operations)


def test_b::operations_constructor_exists():
    assert callable(b::Operations.__init__)


def test_b::operations_constructor_args():
    sig = inspect.signature(b::Operations.__init__)
    params = list(sig.parameters.keys())



def test_b::properties_is_not_abstract():
    assert not inspect.isabstract(b::Properties)


def test_b::properties_constructor_exists():
    assert callable(b::Properties.__init__)


def test_b::properties_constructor_args():
    sig = inspect.signature(b::Properties.__init__)
    params = list(sig.parameters.keys())



def test_b::definitions_is_not_abstract():
    assert not inspect.isabstract(b::Definitions)


def test_b::definitions_constructor_exists():
    assert callable(b::Definitions.__init__)


def test_b::definitions_constructor_args():
    sig = inspect.signature(b::Definitions.__init__)
    params = list(sig.parameters.keys())



def test_b::concreteconstants_is_not_abstract():
    assert not inspect.isabstract(b::ConcreteConstants)


def test_b::concreteconstants_constructor_exists():
    assert callable(b::ConcreteConstants.__init__)


def test_b::concreteconstants_constructor_args():
    sig = inspect.signature(b::ConcreteConstants.__init__)
    params = list(sig.parameters.keys())



def test_b::sees_is_not_abstract():
    assert not inspect.isabstract(b::Sees)


def test_b::sees_constructor_exists():
    assert callable(b::Sees.__init__)


def test_b::sees_constructor_args():
    sig = inspect.signature(b::Sees.__init__)
    params = list(sig.parameters.keys())



def test_b::abstraction_is_not_abstract():
    assert not inspect.isabstract(b::Abstraction)


def test_b::abstraction_constructor_exists():
    assert callable(b::Abstraction.__init__)


def test_b::abstraction_constructor_args():
    sig = inspect.signature(b::Abstraction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b::abstraction_has_name():
    assert hasattr(b::Abstraction, "name")
    descriptor = None
    for klass in b::Abstraction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_b::localoperations_is_not_abstract():
    assert not inspect.isabstract(b::LocalOperations)


def test_b::localoperations_constructor_exists():
    assert callable(b::LocalOperations.__init__)


def test_b::localoperations_constructor_args():
    sig = inspect.signature(b::LocalOperations.__init__)
    params = list(sig.parameters.keys())



def test_b::values_is_not_abstract():
    assert not inspect.isabstract(b::Values)


def test_b::values_constructor_exists():
    assert callable(b::Values.__init__)


def test_b::values_constructor_args():
    sig = inspect.signature(b::Values.__init__)
    params = list(sig.parameters.keys())



def test_b::imports_is_not_abstract():
    assert not inspect.isabstract(b::Imports)


def test_b::imports_constructor_exists():
    assert callable(b::Imports.__init__)


def test_b::imports_constructor_args():
    sig = inspect.signature(b::Imports.__init__)
    params = list(sig.parameters.keys())



def test_b::sets_is_not_abstract():
    assert not inspect.isabstract(b::Sets)


def test_b::sets_constructor_exists():
    assert callable(b::Sets.__init__)


def test_b::sets_constructor_args():
    sig = inspect.signature(b::Sets.__init__)
    params = list(sig.parameters.keys())



def test_b::assertions_is_not_abstract():
    assert not inspect.isabstract(b::Assertions)


def test_b::assertions_constructor_exists():
    assert callable(b::Assertions.__init__)


def test_b::assertions_constructor_args():
    sig = inspect.signature(b::Assertions.__init__)
    params = list(sig.parameters.keys())



def test_b::initialisation_is_not_abstract():
    assert not inspect.isabstract(b::Initialisation)


def test_b::initialisation_constructor_exists():
    assert callable(b::Initialisation.__init__)


def test_b::initialisation_constructor_args():
    sig = inspect.signature(b::Initialisation.__init__)
    params = list(sig.parameters.keys())



def test_b::invariant_is_not_abstract():
    assert not inspect.isabstract(b::Invariant)


def test_b::invariant_constructor_exists():
    assert callable(b::Invariant.__init__)


def test_b::invariant_constructor_args():
    sig = inspect.signature(b::Invariant.__init__)
    params = list(sig.parameters.keys())



def test_b::concretevariables_is_not_abstract():
    assert not inspect.isabstract(b::ConcreteVariables)


def test_b::concretevariables_constructor_exists():
    assert callable(b::ConcreteVariables.__init__)


def test_b::concretevariables_constructor_args():
    sig = inspect.signature(b::ConcreteVariables.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_b::implementation_is_not_abstract():
    assert not inspect.isabstract(b::Implementation)


def test_b::implementation_constructor_exists():
    assert callable(b::Implementation.__init__)


def test_b::implementation_constructor_args():
    sig = inspect.signature(b::Implementation.__init__)
    params = list(sig.parameters.keys())



def test_b::machine_is_not_abstract():
    assert not inspect.isabstract(b::Machine)


def test_b::machine_constructor_exists():
    assert callable(b::Machine.__init__)


def test_b::machine_constructor_args():
    sig = inspect.signature(b::Machine.__init__)
    params = list(sig.parameters.keys())

def test_primitivetypeenum_exists():
    # Check that the Enumeration exists
    assert PrimitiveTypeEnum is not None

def test_primitivetypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveTypeEnum]
    expected_literals = [
        "NAT",
        "INT",
        "STRING",
        "NAT1",
        "BOOL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveTypeEnum"

def test_boolliteralenum_exists():
    # Check that the Enumeration exists
    assert BoolLiteralEnum is not None

def test_boolliteralenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BoolLiteralEnum]
    expected_literals = [
        "FALSE",
        "TRUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BoolLiteralEnum"

def test_inequalityop_exists():
    # Check that the Enumeration exists
    assert InequalityOp is not None

def test_inequalityop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InequalityOp]
    expected_literals = [
        "LESS",
        "GREATER_EQ",
        "LESS_EQ",
        "GREATER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InequalityOp"


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
b::Program_strategy = st.builds(
    b::Program,
)
ReturnTypeExpr_strategy = st.builds(
    ReturnTypeExpr,
)
b::ReturnOr_strategy = st.builds(
    b::ReturnOr,
)
PropertyExpr_strategy = st.builds(
    PropertyExpr,
)
b::PropertyTyped_strategy = st.builds(
    b::PropertyTyped,
)
ReturnExpr_strategy = st.builds(
    ReturnExpr,
)
b::Neg_strategy = st.builds(
    b::Neg,
)
Type_strategy = st.builds(
    Type,
)
b::PrimitiveType_strategy = st.builds(
    b::PrimitiveType,
    type=
        safe_text
)
b::SimpleCall_strategy = st.builds(
    b::SimpleCall,
)
b::PropertyRange_strategy = st.builds(
    b::PropertyRange,
)
Return_strategy = st.builds(
    Return,
)
b::ReturnTuple_strategy = st.builds(
    b::ReturnTuple,
)
b::ReturnTypeExpr_strategy = st.builds(
    b::ReturnTypeExpr,
)
b::ReturnExpr_strategy = st.builds(
    b::ReturnExpr,
)
Statement_strategy = st.builds(
    Statement,
)
b::BeginBody_strategy = st.builds(
    b::BeginBody,
)
BeginBody_strategy = st.builds(
    BeginBody,
)
b::FinalExpr_strategy = st.builds(
    b::FinalExpr,
)
b::CaseExpr_strategy = st.builds(
    b::CaseExpr,
)
b::Statement_strategy = st.builds(
    b::Statement,
)
Expr_strategy = st.builds(
    Expr,
)
b::Assign_strategy = st.builds(
    b::Assign,
)
b::Call_strategy = st.builds(
    b::Call,
)
Body_strategy = st.builds(
    Body,
)
b::Seq_strategy = st.builds(
    b::Seq,
)
b::Begin_strategy = st.builds(
    b::Begin,
)
b::Skip_strategy = st.builds(
    b::Skip,
)
b::Expr_strategy = st.builds(
    b::Expr,
)
b::Body_strategy = st.builds(
    b::Body,
)
b::Operation_strategy = st.builds(
    b::Operation,
    name=
        safe_text
)
b::PreExpr_strategy = st.builds(
    b::PreExpr,
)
b::Pre_strategy = st.builds(
    b::Pre,
)
b::Condition_strategy = st.builds(
    b::Condition,
)
b::IfCond_strategy = st.builds(
    b::IfCond,
)
FinalExpr_strategy = st.builds(
    FinalExpr,
)
b::Var_strategy = st.builds(
    b::Var,
)
b::Case_strategy = st.builds(
    b::Case,
)
b::Return_strategy = st.builds(
    b::Return,
)
b::If_strategy = st.builds(
    b::If,
)
b::LogicalExpr_strategy = st.builds(
    b::LogicalExpr,
)
b::Definition_strategy = st.builds(
    b::Definition,
    name=
        safe_text
)
b::AssertionExpr_strategy = st.builds(
    b::AssertionExpr,
)
b::Range_strategy = st.builds(
    b::Range,
    lowerBound=
        st.integers()
)
b::Set_strategy = st.builds(
    b::Set,
)
Arg_strategy = st.builds(
    Arg,
)
b::StringLiteral_strategy = st.builds(
    b::StringLiteral,
    value=
        safe_text
)
b::ArgMinus_strategy = st.builds(
    b::ArgMinus,
)
Condition_strategy = st.builds(
    Condition,
)
b::CondAnd_strategy = st.builds(
    b::CondAnd,
)
b::CondLessThan_strategy = st.builds(
    b::CondLessThan,
)
b::BoolLiteral_strategy = st.builds(
    b::BoolLiteral,
    value=
        safe_text,
    constant=
        safe_text
)
b::CondMinus_strategy = st.builds(
    b::CondMinus,
)
b::CondEq_strategy = st.builds(
    b::CondEq,
)
b::CondNeg_strategy = st.builds(
    b::CondNeg,
)
b::Arg_strategy = st.builds(
    b::Arg,
)
LogicalExpr_strategy = st.builds(
    LogicalExpr,
)
b::IntLiteral_strategy = st.builds(
    b::IntLiteral,
    value=
        st.integers()
)
b::Ref_strategy = st.builds(
    b::Ref,
)
b::EqualExpr_strategy = st.builds(
    b::EqualExpr,
)
b::ConstantExpr_strategy = st.builds(
    b::ConstantExpr,
    constant=
        safe_text
)
b::TypeConstraint_strategy = st.builds(
    b::TypeConstraint,
)
b::InequalityExpr_strategy = st.builds(
    b::InequalityExpr,
    op=
        safe_text
)
b::AndExpr_strategy = st.builds(
    b::AndExpr,
)
b::BoolTest_strategy = st.builds(
    b::BoolTest,
)
b::ImplyExpr_strategy = st.builds(
    b::ImplyExpr,
)
b::NegExpr_strategy = st.builds(
    b::NegExpr,
)
b::DefinitionCall_strategy = st.builds(
    b::DefinitionCall,
)
b::InvariantExpr_strategy = st.builds(
    b::InvariantExpr,
)
b::Variable_strategy = st.builds(
    b::Variable,
    name=
        safe_text
)
b::ValueExpr_strategy = st.builds(
    b::ValueExpr,
    value=
        safe_text
)
b::PropertyExpr_strategy = st.builds(
    b::PropertyExpr,
)
b::InitialisationExpr_strategy = st.builds(
    b::InitialisationExpr,
)
b::Type_strategy = st.builds(
    b::Type,
)
b::Operations_strategy = st.builds(
    b::Operations,
)
b::Properties_strategy = st.builds(
    b::Properties,
)
b::Definitions_strategy = st.builds(
    b::Definitions,
)
b::ConcreteConstants_strategy = st.builds(
    b::ConcreteConstants,
)
b::Sees_strategy = st.builds(
    b::Sees,
)
b::Abstraction_strategy = st.builds(
    b::Abstraction,
    name=
        safe_text
)
b::LocalOperations_strategy = st.builds(
    b::LocalOperations,
)
b::Values_strategy = st.builds(
    b::Values,
)
b::Imports_strategy = st.builds(
    b::Imports,
)
b::Sets_strategy = st.builds(
    b::Sets,
)
b::Assertions_strategy = st.builds(
    b::Assertions,
)
b::Initialisation_strategy = st.builds(
    b::Initialisation,
)
b::Invariant_strategy = st.builds(
    b::Invariant,
)
b::ConcreteVariables_strategy = st.builds(
    b::ConcreteVariables,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
b::Implementation_strategy = st.builds(
    b::Implementation,
)
b::Machine_strategy = st.builds(
    b::Machine,
)

@given(instance=b::Program_strategy)
@settings(max_examples=50)
def test_b::program_instantiation(instance):
    assert isinstance(instance, b::Program)

@given(instance=ReturnTypeExpr_strategy)
@settings(max_examples=50)
def test_returntypeexpr_instantiation(instance):
    assert isinstance(instance, ReturnTypeExpr)

@given(instance=b::ReturnOr_strategy)
@settings(max_examples=50)
def test_b::returnor_instantiation(instance):
    assert isinstance(instance, b::ReturnOr)

@given(instance=PropertyExpr_strategy)
@settings(max_examples=50)
def test_propertyexpr_instantiation(instance):
    assert isinstance(instance, PropertyExpr)

@given(instance=b::PropertyTyped_strategy)
@settings(max_examples=50)
def test_b::propertytyped_instantiation(instance):
    assert isinstance(instance, b::PropertyTyped)

@given(instance=ReturnExpr_strategy)
@settings(max_examples=50)
def test_returnexpr_instantiation(instance):
    assert isinstance(instance, ReturnExpr)

@given(instance=b::Neg_strategy)
@settings(max_examples=50)
def test_b::neg_instantiation(instance):
    assert isinstance(instance, b::Neg)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=b::PrimitiveType_strategy)
@settings(max_examples=50)
def test_b::primitivetype_instantiation(instance):
    assert isinstance(instance, b::PrimitiveType)

@given(instance=b::PrimitiveType_strategy)
def test_b::primitivetype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=b::PrimitiveType_strategy)
def test_b::primitivetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=b::SimpleCall_strategy)
@settings(max_examples=50)
def test_b::simplecall_instantiation(instance):
    assert isinstance(instance, b::SimpleCall)

@given(instance=b::PropertyRange_strategy)
@settings(max_examples=50)
def test_b::propertyrange_instantiation(instance):
    assert isinstance(instance, b::PropertyRange)

@given(instance=Return_strategy)
@settings(max_examples=50)
def test_return_instantiation(instance):
    assert isinstance(instance, Return)

@given(instance=b::ReturnTuple_strategy)
@settings(max_examples=50)
def test_b::returntuple_instantiation(instance):
    assert isinstance(instance, b::ReturnTuple)

@given(instance=b::ReturnTypeExpr_strategy)
@settings(max_examples=50)
def test_b::returntypeexpr_instantiation(instance):
    assert isinstance(instance, b::ReturnTypeExpr)

@given(instance=b::ReturnExpr_strategy)
@settings(max_examples=50)
def test_b::returnexpr_instantiation(instance):
    assert isinstance(instance, b::ReturnExpr)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=b::BeginBody_strategy)
@settings(max_examples=50)
def test_b::beginbody_instantiation(instance):
    assert isinstance(instance, b::BeginBody)

@given(instance=BeginBody_strategy)
@settings(max_examples=50)
def test_beginbody_instantiation(instance):
    assert isinstance(instance, BeginBody)

@given(instance=b::FinalExpr_strategy)
@settings(max_examples=50)
def test_b::finalexpr_instantiation(instance):
    assert isinstance(instance, b::FinalExpr)

@given(instance=b::CaseExpr_strategy)
@settings(max_examples=50)
def test_b::caseexpr_instantiation(instance):
    assert isinstance(instance, b::CaseExpr)

@given(instance=b::Statement_strategy)
@settings(max_examples=50)
def test_b::statement_instantiation(instance):
    assert isinstance(instance, b::Statement)

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=b::Assign_strategy)
@settings(max_examples=50)
def test_b::assign_instantiation(instance):
    assert isinstance(instance, b::Assign)

@given(instance=b::Call_strategy)
@settings(max_examples=50)
def test_b::call_instantiation(instance):
    assert isinstance(instance, b::Call)

@given(instance=Body_strategy)
@settings(max_examples=50)
def test_body_instantiation(instance):
    assert isinstance(instance, Body)

@given(instance=b::Seq_strategy)
@settings(max_examples=50)
def test_b::seq_instantiation(instance):
    assert isinstance(instance, b::Seq)

@given(instance=b::Begin_strategy)
@settings(max_examples=50)
def test_b::begin_instantiation(instance):
    assert isinstance(instance, b::Begin)

@given(instance=b::Skip_strategy)
@settings(max_examples=50)
def test_b::skip_instantiation(instance):
    assert isinstance(instance, b::Skip)

@given(instance=b::Expr_strategy)
@settings(max_examples=50)
def test_b::expr_instantiation(instance):
    assert isinstance(instance, b::Expr)

@given(instance=b::Body_strategy)
@settings(max_examples=50)
def test_b::body_instantiation(instance):
    assert isinstance(instance, b::Body)

@given(instance=b::Operation_strategy)
@settings(max_examples=50)
def test_b::operation_instantiation(instance):
    assert isinstance(instance, b::Operation)

@given(instance=b::Operation_strategy)
def test_b::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=b::Operation_strategy)
def test_b::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=b::PreExpr_strategy)
@settings(max_examples=50)
def test_b::preexpr_instantiation(instance):
    assert isinstance(instance, b::PreExpr)

@given(instance=b::Pre_strategy)
@settings(max_examples=50)
def test_b::pre_instantiation(instance):
    assert isinstance(instance, b::Pre)

@given(instance=b::Condition_strategy)
@settings(max_examples=50)
def test_b::condition_instantiation(instance):
    assert isinstance(instance, b::Condition)

@given(instance=b::IfCond_strategy)
@settings(max_examples=50)
def test_b::ifcond_instantiation(instance):
    assert isinstance(instance, b::IfCond)

@given(instance=FinalExpr_strategy)
@settings(max_examples=50)
def test_finalexpr_instantiation(instance):
    assert isinstance(instance, FinalExpr)

@given(instance=b::Var_strategy)
@settings(max_examples=50)
def test_b::var_instantiation(instance):
    assert isinstance(instance, b::Var)

@given(instance=b::Case_strategy)
@settings(max_examples=50)
def test_b::case_instantiation(instance):
    assert isinstance(instance, b::Case)

@given(instance=b::Return_strategy)
@settings(max_examples=50)
def test_b::return_instantiation(instance):
    assert isinstance(instance, b::Return)

@given(instance=b::If_strategy)
@settings(max_examples=50)
def test_b::if_instantiation(instance):
    assert isinstance(instance, b::If)

@given(instance=b::LogicalExpr_strategy)
@settings(max_examples=50)
def test_b::logicalexpr_instantiation(instance):
    assert isinstance(instance, b::LogicalExpr)

@given(instance=b::Definition_strategy)
@settings(max_examples=50)
def test_b::definition_instantiation(instance):
    assert isinstance(instance, b::Definition)

@given(instance=b::Definition_strategy)
def test_b::definition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=b::Definition_strategy)
def test_b::definition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=b::AssertionExpr_strategy)
@settings(max_examples=50)
def test_b::assertionexpr_instantiation(instance):
    assert isinstance(instance, b::AssertionExpr)

@given(instance=b::Range_strategy)
@settings(max_examples=50)
def test_b::range_instantiation(instance):
    assert isinstance(instance, b::Range)

@given(instance=b::Range_strategy)
def test_b::range_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=b::Range_strategy)
def test_b::range_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=b::Set_strategy)
@settings(max_examples=50)
def test_b::set_instantiation(instance):
    assert isinstance(instance, b::Set)

@given(instance=Arg_strategy)
@settings(max_examples=50)
def test_arg_instantiation(instance):
    assert isinstance(instance, Arg)

@given(instance=b::StringLiteral_strategy)
@settings(max_examples=50)
def test_b::stringliteral_instantiation(instance):
    assert isinstance(instance, b::StringLiteral)

@given(instance=b::StringLiteral_strategy)
def test_b::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=b::StringLiteral_strategy)
def test_b::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=b::ArgMinus_strategy)
@settings(max_examples=50)
def test_b::argminus_instantiation(instance):
    assert isinstance(instance, b::ArgMinus)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=b::CondAnd_strategy)
@settings(max_examples=50)
def test_b::condand_instantiation(instance):
    assert isinstance(instance, b::CondAnd)

@given(instance=b::CondLessThan_strategy)
@settings(max_examples=50)
def test_b::condlessthan_instantiation(instance):
    assert isinstance(instance, b::CondLessThan)

@given(instance=b::BoolLiteral_strategy)
@settings(max_examples=50)
def test_b::boolliteral_instantiation(instance):
    assert isinstance(instance, b::BoolLiteral)

@given(instance=b::BoolLiteral_strategy)
def test_b::boolliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=b::BoolLiteral_strategy)
def test_b::boolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=b::BoolLiteral_strategy)
def test_b::boolliteral_constant_type(instance):
    assert isinstance(instance.constant, str)


@given(instance=b::BoolLiteral_strategy)
def test_b::boolliteral_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=b::CondMinus_strategy)
@settings(max_examples=50)
def test_b::condminus_instantiation(instance):
    assert isinstance(instance, b::CondMinus)

@given(instance=b::CondEq_strategy)
@settings(max_examples=50)
def test_b::condeq_instantiation(instance):
    assert isinstance(instance, b::CondEq)

@given(instance=b::CondNeg_strategy)
@settings(max_examples=50)
def test_b::condneg_instantiation(instance):
    assert isinstance(instance, b::CondNeg)

@given(instance=b::Arg_strategy)
@settings(max_examples=50)
def test_b::arg_instantiation(instance):
    assert isinstance(instance, b::Arg)

@given(instance=LogicalExpr_strategy)
@settings(max_examples=50)
def test_logicalexpr_instantiation(instance):
    assert isinstance(instance, LogicalExpr)

@given(instance=b::IntLiteral_strategy)
@settings(max_examples=50)
def test_b::intliteral_instantiation(instance):
    assert isinstance(instance, b::IntLiteral)

@given(instance=b::IntLiteral_strategy)
def test_b::intliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=b::IntLiteral_strategy)
def test_b::intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=b::Ref_strategy)
@settings(max_examples=50)
def test_b::ref_instantiation(instance):
    assert isinstance(instance, b::Ref)

@given(instance=b::EqualExpr_strategy)
@settings(max_examples=50)
def test_b::equalexpr_instantiation(instance):
    assert isinstance(instance, b::EqualExpr)

@given(instance=b::ConstantExpr_strategy)
@settings(max_examples=50)
def test_b::constantexpr_instantiation(instance):
    assert isinstance(instance, b::ConstantExpr)

@given(instance=b::ConstantExpr_strategy)
def test_b::constantexpr_constant_type(instance):
    assert isinstance(instance.constant, str)


@given(instance=b::ConstantExpr_strategy)
def test_b::constantexpr_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=b::TypeConstraint_strategy)
@settings(max_examples=50)
def test_b::typeconstraint_instantiation(instance):
    assert isinstance(instance, b::TypeConstraint)

@given(instance=b::InequalityExpr_strategy)
@settings(max_examples=50)
def test_b::inequalityexpr_instantiation(instance):
    assert isinstance(instance, b::InequalityExpr)

@given(instance=b::InequalityExpr_strategy)
def test_b::inequalityexpr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=b::InequalityExpr_strategy)
def test_b::inequalityexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=b::AndExpr_strategy)
@settings(max_examples=50)
def test_b::andexpr_instantiation(instance):
    assert isinstance(instance, b::AndExpr)

@given(instance=b::BoolTest_strategy)
@settings(max_examples=50)
def test_b::booltest_instantiation(instance):
    assert isinstance(instance, b::BoolTest)

@given(instance=b::ImplyExpr_strategy)
@settings(max_examples=50)
def test_b::implyexpr_instantiation(instance):
    assert isinstance(instance, b::ImplyExpr)

@given(instance=b::NegExpr_strategy)
@settings(max_examples=50)
def test_b::negexpr_instantiation(instance):
    assert isinstance(instance, b::NegExpr)

@given(instance=b::DefinitionCall_strategy)
@settings(max_examples=50)
def test_b::definitioncall_instantiation(instance):
    assert isinstance(instance, b::DefinitionCall)

@given(instance=b::InvariantExpr_strategy)
@settings(max_examples=50)
def test_b::invariantexpr_instantiation(instance):
    assert isinstance(instance, b::InvariantExpr)

@given(instance=b::Variable_strategy)
@settings(max_examples=50)
def test_b::variable_instantiation(instance):
    assert isinstance(instance, b::Variable)

@given(instance=b::Variable_strategy)
def test_b::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=b::Variable_strategy)
def test_b::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=b::ValueExpr_strategy)
@settings(max_examples=50)
def test_b::valueexpr_instantiation(instance):
    assert isinstance(instance, b::ValueExpr)

@given(instance=b::ValueExpr_strategy)
def test_b::valueexpr_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=b::ValueExpr_strategy)
def test_b::valueexpr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=b::PropertyExpr_strategy)
@settings(max_examples=50)
def test_b::propertyexpr_instantiation(instance):
    assert isinstance(instance, b::PropertyExpr)

@given(instance=b::InitialisationExpr_strategy)
@settings(max_examples=50)
def test_b::initialisationexpr_instantiation(instance):
    assert isinstance(instance, b::InitialisationExpr)

@given(instance=b::Type_strategy)
@settings(max_examples=50)
def test_b::type_instantiation(instance):
    assert isinstance(instance, b::Type)

@given(instance=b::Operations_strategy)
@settings(max_examples=50)
def test_b::operations_instantiation(instance):
    assert isinstance(instance, b::Operations)

@given(instance=b::Properties_strategy)
@settings(max_examples=50)
def test_b::properties_instantiation(instance):
    assert isinstance(instance, b::Properties)

@given(instance=b::Definitions_strategy)
@settings(max_examples=50)
def test_b::definitions_instantiation(instance):
    assert isinstance(instance, b::Definitions)

@given(instance=b::ConcreteConstants_strategy)
@settings(max_examples=50)
def test_b::concreteconstants_instantiation(instance):
    assert isinstance(instance, b::ConcreteConstants)

@given(instance=b::Sees_strategy)
@settings(max_examples=50)
def test_b::sees_instantiation(instance):
    assert isinstance(instance, b::Sees)

@given(instance=b::Abstraction_strategy)
@settings(max_examples=50)
def test_b::abstraction_instantiation(instance):
    assert isinstance(instance, b::Abstraction)

@given(instance=b::Abstraction_strategy)
def test_b::abstraction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=b::Abstraction_strategy)
def test_b::abstraction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=b::LocalOperations_strategy)
@settings(max_examples=50)
def test_b::localoperations_instantiation(instance):
    assert isinstance(instance, b::LocalOperations)

@given(instance=b::Values_strategy)
@settings(max_examples=50)
def test_b::values_instantiation(instance):
    assert isinstance(instance, b::Values)

@given(instance=b::Imports_strategy)
@settings(max_examples=50)
def test_b::imports_instantiation(instance):
    assert isinstance(instance, b::Imports)

@given(instance=b::Sets_strategy)
@settings(max_examples=50)
def test_b::sets_instantiation(instance):
    assert isinstance(instance, b::Sets)

@given(instance=b::Assertions_strategy)
@settings(max_examples=50)
def test_b::assertions_instantiation(instance):
    assert isinstance(instance, b::Assertions)

@given(instance=b::Initialisation_strategy)
@settings(max_examples=50)
def test_b::initialisation_instantiation(instance):
    assert isinstance(instance, b::Initialisation)

@given(instance=b::Invariant_strategy)
@settings(max_examples=50)
def test_b::invariant_instantiation(instance):
    assert isinstance(instance, b::Invariant)

@given(instance=b::ConcreteVariables_strategy)
@settings(max_examples=50)
def test_b::concretevariables_instantiation(instance):
    assert isinstance(instance, b::ConcreteVariables)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=b::Implementation_strategy)
@settings(max_examples=50)
def test_b::implementation_instantiation(instance):
    assert isinstance(instance, b::Implementation)

@given(instance=b::Machine_strategy)
@settings(max_examples=50)
def test_b::machine_instantiation(instance):
    assert isinstance(instance, b::Machine)
