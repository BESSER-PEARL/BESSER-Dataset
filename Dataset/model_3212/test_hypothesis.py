import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OPLmetamodel::TupleBinding,
    PiecewiseLinearFunction,
    ScriptStatement,
    OPLmetamodel::Writeln,
    OPLmetamodel::VariableBinding,
    BooleanExpression,
    BinaryExpression,
    OPLmetamodel::RelationalExpression,
    BuiltInFunction,
    OPLmetamodel::ReflectiveFunction,
    OPLmetamodel::Sequence,
    OPLmetamodel::ScriptStatement,
    DataInitMethods,
    OPLmetamodel::QueryUser,
    OPLmetamodel::PiecewiseExpression,
    OPLmetamodel::RecordField,
    ParameterDomain,
    OPLmetamodel::ReadFile,
    OPLmetamodel::Model,
    OPLmetamodel::Operator,
    OPLmetamodel::SearchProcedure,
    IntegerType,
    OPLmetamodel::PositiveIntegerType,
    OPLmetamodel::StepFunction,
    OPLmetamodel::Interval,
    OPLmetamodel::In,
    FloatType,
    OPLmetamodel::PositiveFloatType,
    OPLmetamodel::Error,
    OPLmetamodel::Entity,
    OPLmetamodel::FunctionRef,
    Constraint,
    OPLmetamodel::IfConstraint,
    OPLmetamodel::ForAllConstraint,
    NumericExpression,
    OPLmetamodel::IntegerExpression,
    OPLmetamodel::RangeExpression,
    OPLmetamodel::FloatExpression,
    OPLmetamodel::ParameterDomain,
    NumericType,
    OPLmetamodel::IntegerType,
    OPLmetamodel::FloatType,
    RangeType,
    OPLmetamodel::FloatRangeType,
    OPLmetamodel::IntegerRangeType,
    Initialization,
    OPLmetamodel::RelationalInit,
    OPLmetamodel::DataObject,
    OPLmetamodel::DataInitMethods,
    OPLmetamodel::Initialization,
    SetType,
    OPLmetamodel::RangeType,
    OPLmetamodel::EnumerationType,
    OPLmetamodel::ParameterDeclaration,
    OPLmetamodel::DisplayInstruction,
    AbstractType,
    OPLmetamodel::PrimitiveType,
    OPLmetamodel::DeferredInit,
    OPLmetamodel::Declaration,
    DefinedType,
    OPLmetamodel::Record,
    OPLmetamodel::SetType,
    OPLmetamodel::ArrayType,
    CollectionExpression,
    OPLmetamodel::Extension,
    OPLmetamodel::Comprehension,
    Function,
    OPLmetamodel::CumulativeFunction,
    OPLmetamodel::PiecewiseLinearFunction,
    OPLmetamodel::StateFunction,
    OPLmetamodel::BuiltInFunction,
    PrimitiveType,
    OPLmetamodel::StringType,
    OPLmetamodel::NumericType,
    OPLmetamodel::BooleanType,
    PrimitiveExpression,
    OPLmetamodel::StringExpression,
    OPLmetamodel::NumericExpression,
    OPLmetamodel::EnumLiteral,
    OPLmetamodel::BooleanExpression,
    OPLmetamodel::BooleanBlock,
    Reference,
    OPLmetamodel::DataRef,
    OPLmetamodel::ParameterRef,
    OPLmetamodel::BindingRef,
    AbstractBinaryOperator,
    OPLmetamodel::RelationalOperator,
    OPLmetamodel::BinaryOperator,
    OPLmetamodel::AbstractBinaryOperator,
    PathExpression,
    OPLmetamodel::PathDereference,
    OPLmetamodel::FunctionCall,
    OPLmetamodel::ArrayDereference,
    OPLmetamodel::AllExpression,
    OPLmetamodel::Expression,
    OPLmetamodel::FormalParameter,
    Expression,
    OPLmetamodel::PrimitiveExpression,
    OPLmetamodel::ArrayValue,
    OPLmetamodel::BlockExpression,
    OPLmetamodel::BinaryExpression,
    OPLmetamodel::ArraySlotConstraint,
    OPLmetamodel::RecordValue,
    OPLmetamodel::UnaryExpression,
    OPLmetamodel::IndexValuePair,
    OPLmetamodel::PathExpression,
    OPLmetamodel::Reference,
    OPLmetamodel::IfExpression,
    OPLmetamodel::SetValue,
    OPLmetamodel::CollectionExpression,
    OPLmetamodel::AggregateExp,
    OPLmetamodel::Number,
    Declaration,
    OPLmetamodel::DefinedType,
    OPLmetamodel::Function,
    OPLmetamodel::ScheduleInitialization,
    OPLmetamodel::ResourceDeclaration,
    OPLmetamodel::DataDeclaration,
    OPLmetamodel::Setting,
    OPLmetamodel::Assertion,
    OPLmetamodel::Constraint,
    OPLmetamodel::Objective,
    OPLmetamodel::Script,
    OPLmetamodel::ActivityDeclaration,
    OPLmetamodel::AbstractType,
    BinaryOp,
    Quantifier,
    UnaryOp,
    OptimizationMode,
    RelationalOp,
    LogicalOp,
    AggOp,
    SetOp,
    MembershipOp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oplmetamodel::tuplebinding_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::TupleBinding)


def test_oplmetamodel::tuplebinding_constructor_exists():
    assert callable(OPLmetamodel::TupleBinding.__init__)


def test_oplmetamodel::tuplebinding_constructor_args():
    sig = inspect.signature(OPLmetamodel::TupleBinding.__init__)
    params = list(sig.parameters.keys())



def test_piecewiselinearfunction_is_not_abstract():
    assert not inspect.isabstract(PiecewiseLinearFunction)


def test_piecewiselinearfunction_constructor_exists():
    assert callable(PiecewiseLinearFunction.__init__)


def test_piecewiselinearfunction_constructor_args():
    sig = inspect.signature(PiecewiseLinearFunction.__init__)
    params = list(sig.parameters.keys())



def test_scriptstatement_is_not_abstract():
    assert not inspect.isabstract(ScriptStatement)


def test_scriptstatement_constructor_exists():
    assert callable(ScriptStatement.__init__)


def test_scriptstatement_constructor_args():
    sig = inspect.signature(ScriptStatement.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::writeln_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Writeln)


def test_oplmetamodel::writeln_constructor_exists():
    assert callable(OPLmetamodel::Writeln.__init__)


def test_oplmetamodel::writeln_constructor_args():
    sig = inspect.signature(OPLmetamodel::Writeln.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "arg" in params, "Missing parameter 'arg'"

def test_oplmetamodel::writeln_has_string():
    assert hasattr(OPLmetamodel::Writeln, "string")
    descriptor = None
    for klass in OPLmetamodel::Writeln.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_oplmetamodel::writeln_has_arg():
    assert hasattr(OPLmetamodel::Writeln, "arg")
    descriptor = None
    for klass in OPLmetamodel::Writeln.__mro__:
        if "arg" in klass.__dict__:
            descriptor = klass.__dict__["arg"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::variablebinding_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::VariableBinding)


def test_oplmetamodel::variablebinding_constructor_exists():
    assert callable(OPLmetamodel::VariableBinding.__init__)


def test_oplmetamodel::variablebinding_constructor_args():
    sig = inspect.signature(OPLmetamodel::VariableBinding.__init__)
    params = list(sig.parameters.keys())



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::RelationalExpression)


def test_oplmetamodel::relationalexpression_constructor_exists():
    assert callable(OPLmetamodel::RelationalExpression.__init__)


def test_oplmetamodel::relationalexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "redefinedOp" in params, "Missing parameter 'redefinedOp'"

def test_oplmetamodel::relationalexpression_has_redefinedOp():
    assert hasattr(OPLmetamodel::RelationalExpression, "redefinedOp")
    descriptor = None
    for klass in OPLmetamodel::RelationalExpression.__mro__:
        if "redefinedOp" in klass.__dict__:
            descriptor = klass.__dict__["redefinedOp"]
            break
    assert isinstance(descriptor, property)



def test_builtinfunction_is_not_abstract():
    assert not inspect.isabstract(BuiltInFunction)


def test_builtinfunction_constructor_exists():
    assert callable(BuiltInFunction.__init__)


def test_builtinfunction_constructor_args():
    sig = inspect.signature(BuiltInFunction.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::reflectivefunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::ReflectiveFunction)


def test_oplmetamodel::reflectivefunction_constructor_exists():
    assert callable(OPLmetamodel::ReflectiveFunction.__init__)


def test_oplmetamodel::reflectivefunction_constructor_args():
    sig = inspect.signature(OPLmetamodel::ReflectiveFunction.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::sequence_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Sequence)


def test_oplmetamodel::sequence_constructor_exists():
    assert callable(OPLmetamodel::Sequence.__init__)


def test_oplmetamodel::sequence_constructor_args():
    sig = inspect.signature(OPLmetamodel::Sequence.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::scriptstatement_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::ScriptStatement)


def test_oplmetamodel::scriptstatement_constructor_exists():
    assert callable(OPLmetamodel::ScriptStatement.__init__)


def test_oplmetamodel::scriptstatement_constructor_args():
    sig = inspect.signature(OPLmetamodel::ScriptStatement.__init__)
    params = list(sig.parameters.keys())



def test_datainitmethods_is_not_abstract():
    assert not inspect.isabstract(DataInitMethods)


def test_datainitmethods_constructor_exists():
    assert callable(DataInitMethods.__init__)


def test_datainitmethods_constructor_args():
    sig = inspect.signature(DataInitMethods.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::queryuser_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::QueryUser)


def test_oplmetamodel::queryuser_constructor_exists():
    assert callable(OPLmetamodel::QueryUser.__init__)


def test_oplmetamodel::queryuser_constructor_args():
    sig = inspect.signature(OPLmetamodel::QueryUser.__init__)
    params = list(sig.parameters.keys())
    assert "ask" in params, "Missing parameter 'ask'"

def test_oplmetamodel::queryuser_has_ask():
    assert hasattr(OPLmetamodel::QueryUser, "ask")
    descriptor = None
    for klass in OPLmetamodel::QueryUser.__mro__:
        if "ask" in klass.__dict__:
            descriptor = klass.__dict__["ask"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::piecewiseexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::PiecewiseExpression)


def test_oplmetamodel::piecewiseexpression_constructor_exists():
    assert callable(OPLmetamodel::PiecewiseExpression.__init__)


def test_oplmetamodel::piecewiseexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::PiecewiseExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::recordfield_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::RecordField)


def test_oplmetamodel::recordfield_constructor_exists():
    assert callable(OPLmetamodel::RecordField.__init__)


def test_oplmetamodel::recordfield_constructor_args():
    sig = inspect.signature(OPLmetamodel::RecordField.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oplmetamodel::recordfield_has_name():
    assert hasattr(OPLmetamodel::RecordField, "name")
    descriptor = None
    for klass in OPLmetamodel::RecordField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_parameterdomain_is_not_abstract():
    assert not inspect.isabstract(ParameterDomain)


def test_parameterdomain_constructor_exists():
    assert callable(ParameterDomain.__init__)


def test_parameterdomain_constructor_args():
    sig = inspect.signature(ParameterDomain.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::readfile_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::ReadFile)


def test_oplmetamodel::readfile_constructor_exists():
    assert callable(OPLmetamodel::ReadFile.__init__)


def test_oplmetamodel::readfile_constructor_args():
    sig = inspect.signature(OPLmetamodel::ReadFile.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_oplmetamodel::readfile_has_path():
    assert hasattr(OPLmetamodel::ReadFile, "path")
    descriptor = None
    for klass in OPLmetamodel::ReadFile.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::model_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Model)


def test_oplmetamodel::model_constructor_exists():
    assert callable(OPLmetamodel::Model.__init__)


def test_oplmetamodel::model_constructor_args():
    sig = inspect.signature(OPLmetamodel::Model.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "isConstraintProblem" in params, "Missing parameter 'isConstraintProblem'"

def test_oplmetamodel::model_has_id():
    assert hasattr(OPLmetamodel::Model, "id")
    descriptor = None
    for klass in OPLmetamodel::Model.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_oplmetamodel::model_has_isConstraintProblem():
    assert hasattr(OPLmetamodel::Model, "isConstraintProblem")
    descriptor = None
    for klass in OPLmetamodel::Model.__mro__:
        if "isConstraintProblem" in klass.__dict__:
            descriptor = klass.__dict__["isConstraintProblem"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::operator_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Operator)


def test_oplmetamodel::operator_constructor_exists():
    assert callable(OPLmetamodel::Operator.__init__)


def test_oplmetamodel::operator_constructor_args():
    sig = inspect.signature(OPLmetamodel::Operator.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::searchprocedure_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::SearchProcedure)


def test_oplmetamodel::searchprocedure_constructor_exists():
    assert callable(OPLmetamodel::SearchProcedure.__init__)


def test_oplmetamodel::searchprocedure_constructor_args():
    sig = inspect.signature(OPLmetamodel::SearchProcedure.__init__)
    params = list(sig.parameters.keys())



def test_integertype_is_not_abstract():
    assert not inspect.isabstract(IntegerType)


def test_integertype_constructor_exists():
    assert callable(IntegerType.__init__)


def test_integertype_constructor_args():
    sig = inspect.signature(IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::positiveintegertype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::PositiveIntegerType)


def test_oplmetamodel::positiveintegertype_constructor_exists():
    assert callable(OPLmetamodel::PositiveIntegerType.__init__)


def test_oplmetamodel::positiveintegertype_constructor_args():
    sig = inspect.signature(OPLmetamodel::PositiveIntegerType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::stepfunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::StepFunction)


def test_oplmetamodel::stepfunction_constructor_exists():
    assert callable(OPLmetamodel::StepFunction.__init__)


def test_oplmetamodel::stepfunction_constructor_args():
    sig = inspect.signature(OPLmetamodel::StepFunction.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::interval_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Interval)


def test_oplmetamodel::interval_constructor_exists():
    assert callable(OPLmetamodel::Interval.__init__)


def test_oplmetamodel::interval_constructor_args():
    sig = inspect.signature(OPLmetamodel::Interval.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"

def test_oplmetamodel::interval_has_isOptional():
    assert hasattr(OPLmetamodel::Interval, "isOptional")
    descriptor = None
    for klass in OPLmetamodel::Interval.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::in_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::In)


def test_oplmetamodel::in_constructor_exists():
    assert callable(OPLmetamodel::In.__init__)


def test_oplmetamodel::in_constructor_args():
    sig = inspect.signature(OPLmetamodel::In.__init__)
    params = list(sig.parameters.keys())



def test_floattype_is_not_abstract():
    assert not inspect.isabstract(FloatType)


def test_floattype_constructor_exists():
    assert callable(FloatType.__init__)


def test_floattype_constructor_args():
    sig = inspect.signature(FloatType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::positivefloattype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::PositiveFloatType)


def test_oplmetamodel::positivefloattype_constructor_exists():
    assert callable(OPLmetamodel::PositiveFloatType.__init__)


def test_oplmetamodel::positivefloattype_constructor_args():
    sig = inspect.signature(OPLmetamodel::PositiveFloatType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::error_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Error)


def test_oplmetamodel::error_constructor_exists():
    assert callable(OPLmetamodel::Error.__init__)


def test_oplmetamodel::error_constructor_args():
    sig = inspect.signature(OPLmetamodel::Error.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::entity_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Entity)


def test_oplmetamodel::entity_constructor_exists():
    assert callable(OPLmetamodel::Entity.__init__)


def test_oplmetamodel::entity_constructor_args():
    sig = inspect.signature(OPLmetamodel::Entity.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::functionref_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::FunctionRef)


def test_oplmetamodel::functionref_constructor_exists():
    assert callable(OPLmetamodel::FunctionRef.__init__)


def test_oplmetamodel::functionref_constructor_args():
    sig = inspect.signature(OPLmetamodel::FunctionRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oplmetamodel::functionref_has_name():
    assert hasattr(OPLmetamodel::FunctionRef, "name")
    descriptor = None
    for klass in OPLmetamodel::FunctionRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::ifconstraint_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::IfConstraint)


def test_oplmetamodel::ifconstraint_constructor_exists():
    assert callable(OPLmetamodel::IfConstraint.__init__)


def test_oplmetamodel::ifconstraint_constructor_args():
    sig = inspect.signature(OPLmetamodel::IfConstraint.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::forallconstraint_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::ForAllConstraint)


def test_oplmetamodel::forallconstraint_constructor_exists():
    assert callable(OPLmetamodel::ForAllConstraint.__init__)


def test_oplmetamodel::forallconstraint_constructor_args():
    sig = inspect.signature(OPLmetamodel::ForAllConstraint.__init__)
    params = list(sig.parameters.keys())



def test_numericexpression_is_not_abstract():
    assert not inspect.isabstract(NumericExpression)


def test_numericexpression_constructor_exists():
    assert callable(NumericExpression.__init__)


def test_numericexpression_constructor_args():
    sig = inspect.signature(NumericExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::integerexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::IntegerExpression)


def test_oplmetamodel::integerexpression_constructor_exists():
    assert callable(OPLmetamodel::IntegerExpression.__init__)


def test_oplmetamodel::integerexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_oplmetamodel::integerexpression_has_body():
    assert hasattr(OPLmetamodel::IntegerExpression, "body")
    descriptor = None
    for klass in OPLmetamodel::IntegerExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::rangeexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::RangeExpression)


def test_oplmetamodel::rangeexpression_constructor_exists():
    assert callable(OPLmetamodel::RangeExpression.__init__)


def test_oplmetamodel::rangeexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::floatexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::FloatExpression)


def test_oplmetamodel::floatexpression_constructor_exists():
    assert callable(OPLmetamodel::FloatExpression.__init__)


def test_oplmetamodel::floatexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::FloatExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_oplmetamodel::floatexpression_has_body():
    assert hasattr(OPLmetamodel::FloatExpression, "body")
    descriptor = None
    for klass in OPLmetamodel::FloatExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::parameterdomain_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::ParameterDomain)


def test_oplmetamodel::parameterdomain_constructor_exists():
    assert callable(OPLmetamodel::ParameterDomain.__init__)


def test_oplmetamodel::parameterdomain_constructor_args():
    sig = inspect.signature(OPLmetamodel::ParameterDomain.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::integertype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::IntegerType)


def test_oplmetamodel::integertype_constructor_exists():
    assert callable(OPLmetamodel::IntegerType.__init__)


def test_oplmetamodel::integertype_constructor_args():
    sig = inspect.signature(OPLmetamodel::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::floattype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::FloatType)


def test_oplmetamodel::floattype_constructor_exists():
    assert callable(OPLmetamodel::FloatType.__init__)


def test_oplmetamodel::floattype_constructor_args():
    sig = inspect.signature(OPLmetamodel::FloatType.__init__)
    params = list(sig.parameters.keys())



def test_rangetype_is_not_abstract():
    assert not inspect.isabstract(RangeType)


def test_rangetype_constructor_exists():
    assert callable(RangeType.__init__)


def test_rangetype_constructor_args():
    sig = inspect.signature(RangeType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::floatrangetype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::FloatRangeType)


def test_oplmetamodel::floatrangetype_constructor_exists():
    assert callable(OPLmetamodel::FloatRangeType.__init__)


def test_oplmetamodel::floatrangetype_constructor_args():
    sig = inspect.signature(OPLmetamodel::FloatRangeType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::integerrangetype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::IntegerRangeType)


def test_oplmetamodel::integerrangetype_constructor_exists():
    assert callable(OPLmetamodel::IntegerRangeType.__init__)


def test_oplmetamodel::integerrangetype_constructor_args():
    sig = inspect.signature(OPLmetamodel::IntegerRangeType.__init__)
    params = list(sig.parameters.keys())



def test_initialization_is_not_abstract():
    assert not inspect.isabstract(Initialization)


def test_initialization_constructor_exists():
    assert callable(Initialization.__init__)


def test_initialization_constructor_args():
    sig = inspect.signature(Initialization.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::relationalinit_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::RelationalInit)


def test_oplmetamodel::relationalinit_constructor_exists():
    assert callable(OPLmetamodel::RelationalInit.__init__)


def test_oplmetamodel::relationalinit_constructor_args():
    sig = inspect.signature(OPLmetamodel::RelationalInit.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::dataobject_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::DataObject)


def test_oplmetamodel::dataobject_constructor_exists():
    assert callable(OPLmetamodel::DataObject.__init__)


def test_oplmetamodel::dataobject_constructor_args():
    sig = inspect.signature(OPLmetamodel::DataObject.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_oplmetamodel::dataobject_has_body():
    assert hasattr(OPLmetamodel::DataObject, "body")
    descriptor = None
    for klass in OPLmetamodel::DataObject.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::datainitmethods_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::DataInitMethods)


def test_oplmetamodel::datainitmethods_constructor_exists():
    assert callable(OPLmetamodel::DataInitMethods.__init__)


def test_oplmetamodel::datainitmethods_constructor_args():
    sig = inspect.signature(OPLmetamodel::DataInitMethods.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::initialization_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Initialization)


def test_oplmetamodel::initialization_constructor_exists():
    assert callable(OPLmetamodel::Initialization.__init__)


def test_oplmetamodel::initialization_constructor_args():
    sig = inspect.signature(OPLmetamodel::Initialization.__init__)
    params = list(sig.parameters.keys())



def test_settype_is_not_abstract():
    assert not inspect.isabstract(SetType)


def test_settype_constructor_exists():
    assert callable(SetType.__init__)


def test_settype_constructor_args():
    sig = inspect.signature(SetType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::rangetype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::RangeType)


def test_oplmetamodel::rangetype_constructor_exists():
    assert callable(OPLmetamodel::RangeType.__init__)


def test_oplmetamodel::rangetype_constructor_args():
    sig = inspect.signature(OPLmetamodel::RangeType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::enumerationtype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::EnumerationType)


def test_oplmetamodel::enumerationtype_constructor_exists():
    assert callable(OPLmetamodel::EnumerationType.__init__)


def test_oplmetamodel::enumerationtype_constructor_args():
    sig = inspect.signature(OPLmetamodel::EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::ParameterDeclaration)


def test_oplmetamodel::parameterdeclaration_constructor_exists():
    assert callable(OPLmetamodel::ParameterDeclaration.__init__)


def test_oplmetamodel::parameterdeclaration_constructor_args():
    sig = inspect.signature(OPLmetamodel::ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::displayinstruction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::DisplayInstruction)


def test_oplmetamodel::displayinstruction_constructor_exists():
    assert callable(OPLmetamodel::DisplayInstruction.__init__)


def test_oplmetamodel::displayinstruction_constructor_args():
    sig = inspect.signature(OPLmetamodel::DisplayInstruction.__init__)
    params = list(sig.parameters.keys())



def test_abstracttype_is_not_abstract():
    assert not inspect.isabstract(AbstractType)


def test_abstracttype_constructor_exists():
    assert callable(AbstractType.__init__)


def test_abstracttype_constructor_args():
    sig = inspect.signature(AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::primitivetype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::PrimitiveType)


def test_oplmetamodel::primitivetype_constructor_exists():
    assert callable(OPLmetamodel::PrimitiveType.__init__)


def test_oplmetamodel::primitivetype_constructor_args():
    sig = inspect.signature(OPLmetamodel::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::deferredinit_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::DeferredInit)


def test_oplmetamodel::deferredinit_constructor_exists():
    assert callable(OPLmetamodel::DeferredInit.__init__)


def test_oplmetamodel::deferredinit_constructor_args():
    sig = inspect.signature(OPLmetamodel::DeferredInit.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::declaration_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Declaration)


def test_oplmetamodel::declaration_constructor_exists():
    assert callable(OPLmetamodel::Declaration.__init__)


def test_oplmetamodel::declaration_constructor_args():
    sig = inspect.signature(OPLmetamodel::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"

def test_oplmetamodel::declaration_has_order():
    assert hasattr(OPLmetamodel::Declaration, "order")
    descriptor = None
    for klass in OPLmetamodel::Declaration.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_definedtype_is_not_abstract():
    assert not inspect.isabstract(DefinedType)


def test_definedtype_constructor_exists():
    assert callable(DefinedType.__init__)


def test_definedtype_constructor_args():
    sig = inspect.signature(DefinedType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::record_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Record)


def test_oplmetamodel::record_constructor_exists():
    assert callable(OPLmetamodel::Record.__init__)


def test_oplmetamodel::record_constructor_args():
    sig = inspect.signature(OPLmetamodel::Record.__init__)
    params = list(sig.parameters.keys())
    assert "isTuple" in params, "Missing parameter 'isTuple'"
    assert "name" in params, "Missing parameter 'name'"

def test_oplmetamodel::record_has_isTuple():
    assert hasattr(OPLmetamodel::Record, "isTuple")
    descriptor = None
    for klass in OPLmetamodel::Record.__mro__:
        if "isTuple" in klass.__dict__:
            descriptor = klass.__dict__["isTuple"]
            break
    assert isinstance(descriptor, property)

def test_oplmetamodel::record_has_name():
    assert hasattr(OPLmetamodel::Record, "name")
    descriptor = None
    for klass in OPLmetamodel::Record.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::settype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::SetType)


def test_oplmetamodel::settype_constructor_exists():
    assert callable(OPLmetamodel::SetType.__init__)


def test_oplmetamodel::settype_constructor_args():
    sig = inspect.signature(OPLmetamodel::SetType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oplmetamodel::settype_has_name():
    assert hasattr(OPLmetamodel::SetType, "name")
    descriptor = None
    for klass in OPLmetamodel::SetType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::arraytype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::ArrayType)


def test_oplmetamodel::arraytype_constructor_exists():
    assert callable(OPLmetamodel::ArrayType.__init__)


def test_oplmetamodel::arraytype_constructor_args():
    sig = inspect.signature(OPLmetamodel::ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionExpression)


def test_collectionexpression_constructor_exists():
    assert callable(CollectionExpression.__init__)


def test_collectionexpression_constructor_args():
    sig = inspect.signature(CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::extension_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Extension)


def test_oplmetamodel::extension_constructor_exists():
    assert callable(OPLmetamodel::Extension.__init__)


def test_oplmetamodel::extension_constructor_args():
    sig = inspect.signature(OPLmetamodel::Extension.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::comprehension_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Comprehension)


def test_oplmetamodel::comprehension_constructor_exists():
    assert callable(OPLmetamodel::Comprehension.__init__)


def test_oplmetamodel::comprehension_constructor_args():
    sig = inspect.signature(OPLmetamodel::Comprehension.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::cumulativefunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::CumulativeFunction)


def test_oplmetamodel::cumulativefunction_constructor_exists():
    assert callable(OPLmetamodel::CumulativeFunction.__init__)


def test_oplmetamodel::cumulativefunction_constructor_args():
    sig = inspect.signature(OPLmetamodel::CumulativeFunction.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::piecewiselinearfunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::PiecewiseLinearFunction)


def test_oplmetamodel::piecewiselinearfunction_constructor_exists():
    assert callable(OPLmetamodel::PiecewiseLinearFunction.__init__)


def test_oplmetamodel::piecewiselinearfunction_constructor_args():
    sig = inspect.signature(OPLmetamodel::PiecewiseLinearFunction.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::statefunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::StateFunction)


def test_oplmetamodel::statefunction_constructor_exists():
    assert callable(OPLmetamodel::StateFunction.__init__)


def test_oplmetamodel::statefunction_constructor_args():
    sig = inspect.signature(OPLmetamodel::StateFunction.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::builtinfunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::BuiltInFunction)


def test_oplmetamodel::builtinfunction_constructor_exists():
    assert callable(OPLmetamodel::BuiltInFunction.__init__)


def test_oplmetamodel::builtinfunction_constructor_args():
    sig = inspect.signature(OPLmetamodel::BuiltInFunction.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::stringtype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::StringType)


def test_oplmetamodel::stringtype_constructor_exists():
    assert callable(OPLmetamodel::StringType.__init__)


def test_oplmetamodel::stringtype_constructor_args():
    sig = inspect.signature(OPLmetamodel::StringType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::numerictype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::NumericType)


def test_oplmetamodel::numerictype_constructor_exists():
    assert callable(OPLmetamodel::NumericType.__init__)


def test_oplmetamodel::numerictype_constructor_args():
    sig = inspect.signature(OPLmetamodel::NumericType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::booleantype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::BooleanType)


def test_oplmetamodel::booleantype_constructor_exists():
    assert callable(OPLmetamodel::BooleanType.__init__)


def test_oplmetamodel::booleantype_constructor_args():
    sig = inspect.signature(OPLmetamodel::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExpression)


def test_primitiveexpression_constructor_exists():
    assert callable(PrimitiveExpression.__init__)


def test_primitiveexpression_constructor_args():
    sig = inspect.signature(PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::stringexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::StringExpression)


def test_oplmetamodel::stringexpression_constructor_exists():
    assert callable(OPLmetamodel::StringExpression.__init__)


def test_oplmetamodel::stringexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_oplmetamodel::stringexpression_has_body():
    assert hasattr(OPLmetamodel::StringExpression, "body")
    descriptor = None
    for klass in OPLmetamodel::StringExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::numericexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::NumericExpression)


def test_oplmetamodel::numericexpression_constructor_exists():
    assert callable(OPLmetamodel::NumericExpression.__init__)


def test_oplmetamodel::numericexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::NumericExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::enumliteral_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::EnumLiteral)


def test_oplmetamodel::enumliteral_constructor_exists():
    assert callable(OPLmetamodel::EnumLiteral.__init__)


def test_oplmetamodel::enumliteral_constructor_args():
    sig = inspect.signature(OPLmetamodel::EnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::BooleanExpression)


def test_oplmetamodel::booleanexpression_constructor_exists():
    assert callable(OPLmetamodel::BooleanExpression.__init__)


def test_oplmetamodel::booleanexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_oplmetamodel::booleanexpression_has_body():
    assert hasattr(OPLmetamodel::BooleanExpression, "body")
    descriptor = None
    for klass in OPLmetamodel::BooleanExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::booleanblock_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::BooleanBlock)


def test_oplmetamodel::booleanblock_constructor_exists():
    assert callable(OPLmetamodel::BooleanBlock.__init__)


def test_oplmetamodel::booleanblock_constructor_args():
    sig = inspect.signature(OPLmetamodel::BooleanBlock.__init__)
    params = list(sig.parameters.keys())



def test_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::dataref_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::DataRef)


def test_oplmetamodel::dataref_constructor_exists():
    assert callable(OPLmetamodel::DataRef.__init__)


def test_oplmetamodel::dataref_constructor_args():
    sig = inspect.signature(OPLmetamodel::DataRef.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::parameterref_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::ParameterRef)


def test_oplmetamodel::parameterref_constructor_exists():
    assert callable(OPLmetamodel::ParameterRef.__init__)


def test_oplmetamodel::parameterref_constructor_args():
    sig = inspect.signature(OPLmetamodel::ParameterRef.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::bindingref_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::BindingRef)


def test_oplmetamodel::bindingref_constructor_exists():
    assert callable(OPLmetamodel::BindingRef.__init__)


def test_oplmetamodel::bindingref_constructor_args():
    sig = inspect.signature(OPLmetamodel::BindingRef.__init__)
    params = list(sig.parameters.keys())



def test_abstractbinaryoperator_is_not_abstract():
    assert not inspect.isabstract(AbstractBinaryOperator)


def test_abstractbinaryoperator_constructor_exists():
    assert callable(AbstractBinaryOperator.__init__)


def test_abstractbinaryoperator_constructor_args():
    sig = inspect.signature(AbstractBinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::relationaloperator_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::RelationalOperator)


def test_oplmetamodel::relationaloperator_constructor_exists():
    assert callable(OPLmetamodel::RelationalOperator.__init__)


def test_oplmetamodel::relationaloperator_constructor_args():
    sig = inspect.signature(OPLmetamodel::RelationalOperator.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_oplmetamodel::relationaloperator_has_op():
    assert hasattr(OPLmetamodel::RelationalOperator, "op")
    descriptor = None
    for klass in OPLmetamodel::RelationalOperator.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::BinaryOperator)


def test_oplmetamodel::binaryoperator_constructor_exists():
    assert callable(OPLmetamodel::BinaryOperator.__init__)


def test_oplmetamodel::binaryoperator_constructor_args():
    sig = inspect.signature(OPLmetamodel::BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_oplmetamodel::binaryoperator_has_op():
    assert hasattr(OPLmetamodel::BinaryOperator, "op")
    descriptor = None
    for klass in OPLmetamodel::BinaryOperator.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::abstractbinaryoperator_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::AbstractBinaryOperator)


def test_oplmetamodel::abstractbinaryoperator_constructor_exists():
    assert callable(OPLmetamodel::AbstractBinaryOperator.__init__)


def test_oplmetamodel::abstractbinaryoperator_constructor_args():
    sig = inspect.signature(OPLmetamodel::AbstractBinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_pathexpression_is_not_abstract():
    assert not inspect.isabstract(PathExpression)


def test_pathexpression_constructor_exists():
    assert callable(PathExpression.__init__)


def test_pathexpression_constructor_args():
    sig = inspect.signature(PathExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::pathdereference_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::PathDereference)


def test_oplmetamodel::pathdereference_constructor_exists():
    assert callable(OPLmetamodel::PathDereference.__init__)


def test_oplmetamodel::pathdereference_constructor_args():
    sig = inspect.signature(OPLmetamodel::PathDereference.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::functioncall_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::FunctionCall)


def test_oplmetamodel::functioncall_constructor_exists():
    assert callable(OPLmetamodel::FunctionCall.__init__)


def test_oplmetamodel::functioncall_constructor_args():
    sig = inspect.signature(OPLmetamodel::FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_oplmetamodel::functioncall_has_functionName():
    assert hasattr(OPLmetamodel::FunctionCall, "functionName")
    descriptor = None
    for klass in OPLmetamodel::FunctionCall.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::arraydereference_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::ArrayDereference)


def test_oplmetamodel::arraydereference_constructor_exists():
    assert callable(OPLmetamodel::ArrayDereference.__init__)


def test_oplmetamodel::arraydereference_constructor_args():
    sig = inspect.signature(OPLmetamodel::ArrayDereference.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::allexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::AllExpression)


def test_oplmetamodel::allexpression_constructor_exists():
    assert callable(OPLmetamodel::AllExpression.__init__)


def test_oplmetamodel::allexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::AllExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::expression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Expression)


def test_oplmetamodel::expression_constructor_exists():
    assert callable(OPLmetamodel::Expression.__init__)


def test_oplmetamodel::expression_constructor_args():
    sig = inspect.signature(OPLmetamodel::Expression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::formalparameter_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::FormalParameter)


def test_oplmetamodel::formalparameter_constructor_exists():
    assert callable(OPLmetamodel::FormalParameter.__init__)


def test_oplmetamodel::formalparameter_constructor_args():
    sig = inspect.signature(OPLmetamodel::FormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_oplmetamodel::formalparameter_has_isOrdered():
    assert hasattr(OPLmetamodel::FormalParameter, "isOrdered")
    descriptor = None
    for klass in OPLmetamodel::FormalParameter.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::PrimitiveExpression)


def test_oplmetamodel::primitiveexpression_constructor_exists():
    assert callable(OPLmetamodel::PrimitiveExpression.__init__)


def test_oplmetamodel::primitiveexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::arrayvalue_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::ArrayValue)


def test_oplmetamodel::arrayvalue_constructor_exists():
    assert callable(OPLmetamodel::ArrayValue.__init__)


def test_oplmetamodel::arrayvalue_constructor_args():
    sig = inspect.signature(OPLmetamodel::ArrayValue.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::blockexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::BlockExpression)


def test_oplmetamodel::blockexpression_constructor_exists():
    assert callable(OPLmetamodel::BlockExpression.__init__)


def test_oplmetamodel::blockexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::BlockExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::BinaryExpression)


def test_oplmetamodel::binaryexpression_constructor_exists():
    assert callable(OPLmetamodel::BinaryExpression.__init__)


def test_oplmetamodel::binaryexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::arrayslotconstraint_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::ArraySlotConstraint)


def test_oplmetamodel::arrayslotconstraint_constructor_exists():
    assert callable(OPLmetamodel::ArraySlotConstraint.__init__)


def test_oplmetamodel::arrayslotconstraint_constructor_args():
    sig = inspect.signature(OPLmetamodel::ArraySlotConstraint.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::recordvalue_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::RecordValue)


def test_oplmetamodel::recordvalue_constructor_exists():
    assert callable(OPLmetamodel::RecordValue.__init__)


def test_oplmetamodel::recordvalue_constructor_args():
    sig = inspect.signature(OPLmetamodel::RecordValue.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::UnaryExpression)


def test_oplmetamodel::unaryexpression_constructor_exists():
    assert callable(OPLmetamodel::UnaryExpression.__init__)


def test_oplmetamodel::unaryexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_oplmetamodel::unaryexpression_has_op():
    assert hasattr(OPLmetamodel::UnaryExpression, "op")
    descriptor = None
    for klass in OPLmetamodel::UnaryExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::indexvaluepair_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::IndexValuePair)


def test_oplmetamodel::indexvaluepair_constructor_exists():
    assert callable(OPLmetamodel::IndexValuePair.__init__)


def test_oplmetamodel::indexvaluepair_constructor_args():
    sig = inspect.signature(OPLmetamodel::IndexValuePair.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::pathexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::PathExpression)


def test_oplmetamodel::pathexpression_constructor_exists():
    assert callable(OPLmetamodel::PathExpression.__init__)


def test_oplmetamodel::pathexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::PathExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::reference_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Reference)


def test_oplmetamodel::reference_constructor_exists():
    assert callable(OPLmetamodel::Reference.__init__)


def test_oplmetamodel::reference_constructor_args():
    sig = inspect.signature(OPLmetamodel::Reference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oplmetamodel::reference_has_name():
    assert hasattr(OPLmetamodel::Reference, "name")
    descriptor = None
    for klass in OPLmetamodel::Reference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::ifexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::IfExpression)


def test_oplmetamodel::ifexpression_constructor_exists():
    assert callable(OPLmetamodel::IfExpression.__init__)


def test_oplmetamodel::ifexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::setvalue_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::SetValue)


def test_oplmetamodel::setvalue_constructor_exists():
    assert callable(OPLmetamodel::SetValue.__init__)


def test_oplmetamodel::setvalue_constructor_args():
    sig = inspect.signature(OPLmetamodel::SetValue.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::collectionexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::CollectionExpression)


def test_oplmetamodel::collectionexpression_constructor_exists():
    assert callable(OPLmetamodel::CollectionExpression.__init__)


def test_oplmetamodel::collectionexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel::CollectionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_oplmetamodel::collectionexpression_has_isUnique():
    assert hasattr(OPLmetamodel::CollectionExpression, "isUnique")
    descriptor = None
    for klass in OPLmetamodel::CollectionExpression.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::aggregateexp_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::AggregateExp)


def test_oplmetamodel::aggregateexp_constructor_exists():
    assert callable(OPLmetamodel::AggregateExp.__init__)


def test_oplmetamodel::aggregateexp_constructor_args():
    sig = inspect.signature(OPLmetamodel::AggregateExp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_oplmetamodel::aggregateexp_has_op():
    assert hasattr(OPLmetamodel::AggregateExp, "op")
    descriptor = None
    for klass in OPLmetamodel::AggregateExp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::number_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Number)


def test_oplmetamodel::number_constructor_exists():
    assert callable(OPLmetamodel::Number.__init__)


def test_oplmetamodel::number_constructor_args():
    sig = inspect.signature(OPLmetamodel::Number.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::definedtype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::DefinedType)


def test_oplmetamodel::definedtype_constructor_exists():
    assert callable(OPLmetamodel::DefinedType.__init__)


def test_oplmetamodel::definedtype_constructor_args():
    sig = inspect.signature(OPLmetamodel::DefinedType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::function_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Function)


def test_oplmetamodel::function_constructor_exists():
    assert callable(OPLmetamodel::Function.__init__)


def test_oplmetamodel::function_constructor_args():
    sig = inspect.signature(OPLmetamodel::Function.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::scheduleinitialization_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::ScheduleInitialization)


def test_oplmetamodel::scheduleinitialization_constructor_exists():
    assert callable(OPLmetamodel::ScheduleInitialization.__init__)


def test_oplmetamodel::scheduleinitialization_constructor_args():
    sig = inspect.signature(OPLmetamodel::ScheduleInitialization.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::resourcedeclaration_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::ResourceDeclaration)


def test_oplmetamodel::resourcedeclaration_constructor_exists():
    assert callable(OPLmetamodel::ResourceDeclaration.__init__)


def test_oplmetamodel::resourcedeclaration_constructor_args():
    sig = inspect.signature(OPLmetamodel::ResourceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::datadeclaration_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::DataDeclaration)


def test_oplmetamodel::datadeclaration_constructor_exists():
    assert callable(OPLmetamodel::DataDeclaration.__init__)


def test_oplmetamodel::datadeclaration_constructor_args():
    sig = inspect.signature(OPLmetamodel::DataDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isDecisionVar" in params, "Missing parameter 'isDecisionVar'"
    assert "isDecisionExpr" in params, "Missing parameter 'isDecisionExpr'"

def test_oplmetamodel::datadeclaration_has_isDecisionVar():
    assert hasattr(OPLmetamodel::DataDeclaration, "isDecisionVar")
    descriptor = None
    for klass in OPLmetamodel::DataDeclaration.__mro__:
        if "isDecisionVar" in klass.__dict__:
            descriptor = klass.__dict__["isDecisionVar"]
            break
    assert isinstance(descriptor, property)

def test_oplmetamodel::datadeclaration_has_isDecisionExpr():
    assert hasattr(OPLmetamodel::DataDeclaration, "isDecisionExpr")
    descriptor = None
    for klass in OPLmetamodel::DataDeclaration.__mro__:
        if "isDecisionExpr" in klass.__dict__:
            descriptor = klass.__dict__["isDecisionExpr"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::setting_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Setting)


def test_oplmetamodel::setting_constructor_exists():
    assert callable(OPLmetamodel::Setting.__init__)


def test_oplmetamodel::setting_constructor_args():
    sig = inspect.signature(OPLmetamodel::Setting.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::assertion_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Assertion)


def test_oplmetamodel::assertion_constructor_exists():
    assert callable(OPLmetamodel::Assertion.__init__)


def test_oplmetamodel::assertion_constructor_args():
    sig = inspect.signature(OPLmetamodel::Assertion.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel::constraint_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Constraint)


def test_oplmetamodel::constraint_constructor_exists():
    assert callable(OPLmetamodel::Constraint.__init__)


def test_oplmetamodel::constraint_constructor_args():
    sig = inspect.signature(OPLmetamodel::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oplmetamodel::constraint_has_name():
    assert hasattr(OPLmetamodel::Constraint, "name")
    descriptor = None
    for klass in OPLmetamodel::Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::objective_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Objective)


def test_oplmetamodel::objective_constructor_exists():
    assert callable(OPLmetamodel::Objective.__init__)


def test_oplmetamodel::objective_constructor_args():
    sig = inspect.signature(OPLmetamodel::Objective.__init__)
    params = list(sig.parameters.keys())
    assert "isLinearRelaxation" in params, "Missing parameter 'isLinearRelaxation'"
    assert "action" in params, "Missing parameter 'action'"

def test_oplmetamodel::objective_has_isLinearRelaxation():
    assert hasattr(OPLmetamodel::Objective, "isLinearRelaxation")
    descriptor = None
    for klass in OPLmetamodel::Objective.__mro__:
        if "isLinearRelaxation" in klass.__dict__:
            descriptor = klass.__dict__["isLinearRelaxation"]
            break
    assert isinstance(descriptor, property)

def test_oplmetamodel::objective_has_action():
    assert hasattr(OPLmetamodel::Objective, "action")
    descriptor = None
    for klass in OPLmetamodel::Objective.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::script_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::Script)


def test_oplmetamodel::script_constructor_exists():
    assert callable(OPLmetamodel::Script.__init__)


def test_oplmetamodel::script_constructor_args():
    sig = inspect.signature(OPLmetamodel::Script.__init__)
    params = list(sig.parameters.keys())
    assert "isMain" in params, "Missing parameter 'isMain'"

def test_oplmetamodel::script_has_isMain():
    assert hasattr(OPLmetamodel::Script, "isMain")
    descriptor = None
    for klass in OPLmetamodel::Script.__mro__:
        if "isMain" in klass.__dict__:
            descriptor = klass.__dict__["isMain"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::activitydeclaration_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::ActivityDeclaration)


def test_oplmetamodel::activitydeclaration_constructor_exists():
    assert callable(OPLmetamodel::ActivityDeclaration.__init__)


def test_oplmetamodel::activitydeclaration_constructor_args():
    sig = inspect.signature(OPLmetamodel::ActivityDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "earliestStartTime" in params, "Missing parameter 'earliestStartTime'"
    assert "latestEndTime" in params, "Missing parameter 'latestEndTime'"

def test_oplmetamodel::activitydeclaration_has_earliestStartTime():
    assert hasattr(OPLmetamodel::ActivityDeclaration, "earliestStartTime")
    descriptor = None
    for klass in OPLmetamodel::ActivityDeclaration.__mro__:
        if "earliestStartTime" in klass.__dict__:
            descriptor = klass.__dict__["earliestStartTime"]
            break
    assert isinstance(descriptor, property)

def test_oplmetamodel::activitydeclaration_has_latestEndTime():
    assert hasattr(OPLmetamodel::ActivityDeclaration, "latestEndTime")
    descriptor = None
    for klass in OPLmetamodel::ActivityDeclaration.__mro__:
        if "latestEndTime" in klass.__dict__:
            descriptor = klass.__dict__["latestEndTime"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel::abstracttype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel::AbstractType)


def test_oplmetamodel::abstracttype_constructor_exists():
    assert callable(OPLmetamodel::AbstractType.__init__)


def test_oplmetamodel::abstracttype_constructor_args():
    sig = inspect.signature(OPLmetamodel::AbstractType.__init__)
    params = list(sig.parameters.keys())

def test_binaryop_exists():
    # Check that the Enumeration exists
    assert BinaryOp is not None

def test_binaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOp]
    expected_literals = [
        "subtract",
        "union",
        "diff",
        "inter",
        "symdiff",
        "divide",
        "mod",
        "percent",
        "add",
        "multiply",
        "power",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOp"

def test_quantifier_exists():
    # Check that the Enumeration exists
    assert Quantifier is not None

def test_quantifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Quantifier]
    expected_literals = [
        "forAll",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Quantifier"

def test_unaryop_exists():
    # Check that the Enumeration exists
    assert UnaryOp is not None

def test_unaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOp]
    expected_literals = [
        "unaryMinus",
        "negate",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOp"

def test_optimizationmode_exists():
    # Check that the Enumeration exists
    assert OptimizationMode is not None

def test_optimizationmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OptimizationMode]
    expected_literals = [
        "minimize",
        "solve",
        "maximize",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OptimizationMode"

def test_relationalop_exists():
    # Check that the Enumeration exists
    assert RelationalOp is not None

def test_relationalop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOp]
    expected_literals = [
        "greaterThan",
        "lessThanOrEqualTo",
        "equalTo",
        "greaterThanOrEqualTo",
        "notEqualTo",
        "lessThan",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOp"

def test_logicalop_exists():
    # Check that the Enumeration exists
    assert LogicalOp is not None

def test_logicalop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOp]
    expected_literals = [
        "conjunction",
        "and_",
        "or_",
        "disjunction",
        "negation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOp"

def test_aggop_exists():
    # Check that the Enumeration exists
    assert AggOp is not None

def test_aggop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggOp]
    expected_literals = [
        "inter",
        "union",
        "prod",
        "max",
        "sum",
        "and_",
        "min",
        "or_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggOp"

def test_setop_exists():
    # Check that the Enumeration exists
    assert SetOp is not None

def test_setop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SetOp]
    expected_literals = [
        "inter",
        "symdiff",
        "diff",
        "union",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SetOp"

def test_membershipop_exists():
    # Check that the Enumeration exists
    assert MembershipOp is not None

def test_membershipop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MembershipOp]
    expected_literals = [
        "not_in",
        "or_",
        "and_",
        "in_",
        "conjunction",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MembershipOp"


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
OPLmetamodel::TupleBinding_strategy = st.builds(
    OPLmetamodel::TupleBinding,
)
PiecewiseLinearFunction_strategy = st.builds(
    PiecewiseLinearFunction,
)
ScriptStatement_strategy = st.builds(
    ScriptStatement,
)
OPLmetamodel::Writeln_strategy = st.builds(
    OPLmetamodel::Writeln,
    string=
        safe_text,
    arg=
        safe_text
)
OPLmetamodel::VariableBinding_strategy = st.builds(
    OPLmetamodel::VariableBinding,
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
OPLmetamodel::RelationalExpression_strategy = st.builds(
    OPLmetamodel::RelationalExpression,
    redefinedOp=
        safe_text
)
BuiltInFunction_strategy = st.builds(
    BuiltInFunction,
)
OPLmetamodel::ReflectiveFunction_strategy = st.builds(
    OPLmetamodel::ReflectiveFunction,
)
OPLmetamodel::Sequence_strategy = st.builds(
    OPLmetamodel::Sequence,
)
OPLmetamodel::ScriptStatement_strategy = st.builds(
    OPLmetamodel::ScriptStatement,
)
DataInitMethods_strategy = st.builds(
    DataInitMethods,
)
OPLmetamodel::QueryUser_strategy = st.builds(
    OPLmetamodel::QueryUser,
    ask=
        safe_text
)
OPLmetamodel::PiecewiseExpression_strategy = st.builds(
    OPLmetamodel::PiecewiseExpression,
)
OPLmetamodel::RecordField_strategy = st.builds(
    OPLmetamodel::RecordField,
    name=
        safe_text
)
ParameterDomain_strategy = st.builds(
    ParameterDomain,
)
OPLmetamodel::ReadFile_strategy = st.builds(
    OPLmetamodel::ReadFile,
    path=
        safe_text
)
OPLmetamodel::Model_strategy = st.builds(
    OPLmetamodel::Model,
    id=
        safe_text,
    isConstraintProblem=
        st.booleans()
)
OPLmetamodel::Operator_strategy = st.builds(
    OPLmetamodel::Operator,
)
OPLmetamodel::SearchProcedure_strategy = st.builds(
    OPLmetamodel::SearchProcedure,
)
IntegerType_strategy = st.builds(
    IntegerType,
)
OPLmetamodel::PositiveIntegerType_strategy = st.builds(
    OPLmetamodel::PositiveIntegerType,
)
OPLmetamodel::StepFunction_strategy = st.builds(
    OPLmetamodel::StepFunction,
)
OPLmetamodel::Interval_strategy = st.builds(
    OPLmetamodel::Interval,
    isOptional=
        st.booleans()
)
OPLmetamodel::In_strategy = st.builds(
    OPLmetamodel::In,
)
FloatType_strategy = st.builds(
    FloatType,
)
OPLmetamodel::PositiveFloatType_strategy = st.builds(
    OPLmetamodel::PositiveFloatType,
)
OPLmetamodel::Error_strategy = st.builds(
    OPLmetamodel::Error,
)
OPLmetamodel::Entity_strategy = st.builds(
    OPLmetamodel::Entity,
)
OPLmetamodel::FunctionRef_strategy = st.builds(
    OPLmetamodel::FunctionRef,
    name=
        safe_text
)
Constraint_strategy = st.builds(
    Constraint,
)
OPLmetamodel::IfConstraint_strategy = st.builds(
    OPLmetamodel::IfConstraint,
)
OPLmetamodel::ForAllConstraint_strategy = st.builds(
    OPLmetamodel::ForAllConstraint,
)
NumericExpression_strategy = st.builds(
    NumericExpression,
)
OPLmetamodel::IntegerExpression_strategy = st.builds(
    OPLmetamodel::IntegerExpression,
    body=
        safe_text
)
OPLmetamodel::RangeExpression_strategy = st.builds(
    OPLmetamodel::RangeExpression,
)
OPLmetamodel::FloatExpression_strategy = st.builds(
    OPLmetamodel::FloatExpression,
    body=
        safe_text
)
OPLmetamodel::ParameterDomain_strategy = st.builds(
    OPLmetamodel::ParameterDomain,
)
NumericType_strategy = st.builds(
    NumericType,
)
OPLmetamodel::IntegerType_strategy = st.builds(
    OPLmetamodel::IntegerType,
)
OPLmetamodel::FloatType_strategy = st.builds(
    OPLmetamodel::FloatType,
)
RangeType_strategy = st.builds(
    RangeType,
)
OPLmetamodel::FloatRangeType_strategy = st.builds(
    OPLmetamodel::FloatRangeType,
)
OPLmetamodel::IntegerRangeType_strategy = st.builds(
    OPLmetamodel::IntegerRangeType,
)
Initialization_strategy = st.builds(
    Initialization,
)
OPLmetamodel::RelationalInit_strategy = st.builds(
    OPLmetamodel::RelationalInit,
)
OPLmetamodel::DataObject_strategy = st.builds(
    OPLmetamodel::DataObject,
    body=
        safe_text
)
OPLmetamodel::DataInitMethods_strategy = st.builds(
    OPLmetamodel::DataInitMethods,
)
OPLmetamodel::Initialization_strategy = st.builds(
    OPLmetamodel::Initialization,
)
SetType_strategy = st.builds(
    SetType,
)
OPLmetamodel::RangeType_strategy = st.builds(
    OPLmetamodel::RangeType,
)
OPLmetamodel::EnumerationType_strategy = st.builds(
    OPLmetamodel::EnumerationType,
)
OPLmetamodel::ParameterDeclaration_strategy = st.builds(
    OPLmetamodel::ParameterDeclaration,
)
OPLmetamodel::DisplayInstruction_strategy = st.builds(
    OPLmetamodel::DisplayInstruction,
)
AbstractType_strategy = st.builds(
    AbstractType,
)
OPLmetamodel::PrimitiveType_strategy = st.builds(
    OPLmetamodel::PrimitiveType,
)
OPLmetamodel::DeferredInit_strategy = st.builds(
    OPLmetamodel::DeferredInit,
)
OPLmetamodel::Declaration_strategy = st.builds(
    OPLmetamodel::Declaration,
    order=
        st.none()
)
DefinedType_strategy = st.builds(
    DefinedType,
)
OPLmetamodel::Record_strategy = st.builds(
    OPLmetamodel::Record,
    isTuple=
        st.booleans(),
    name=
        safe_text
)
OPLmetamodel::SetType_strategy = st.builds(
    OPLmetamodel::SetType,
    name=
        safe_text
)
OPLmetamodel::ArrayType_strategy = st.builds(
    OPLmetamodel::ArrayType,
)
CollectionExpression_strategy = st.builds(
    CollectionExpression,
)
OPLmetamodel::Extension_strategy = st.builds(
    OPLmetamodel::Extension,
)
OPLmetamodel::Comprehension_strategy = st.builds(
    OPLmetamodel::Comprehension,
)
Function_strategy = st.builds(
    Function,
)
OPLmetamodel::CumulativeFunction_strategy = st.builds(
    OPLmetamodel::CumulativeFunction,
)
OPLmetamodel::PiecewiseLinearFunction_strategy = st.builds(
    OPLmetamodel::PiecewiseLinearFunction,
)
OPLmetamodel::StateFunction_strategy = st.builds(
    OPLmetamodel::StateFunction,
)
OPLmetamodel::BuiltInFunction_strategy = st.builds(
    OPLmetamodel::BuiltInFunction,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
OPLmetamodel::StringType_strategy = st.builds(
    OPLmetamodel::StringType,
)
OPLmetamodel::NumericType_strategy = st.builds(
    OPLmetamodel::NumericType,
)
OPLmetamodel::BooleanType_strategy = st.builds(
    OPLmetamodel::BooleanType,
)
PrimitiveExpression_strategy = st.builds(
    PrimitiveExpression,
)
OPLmetamodel::StringExpression_strategy = st.builds(
    OPLmetamodel::StringExpression,
    body=
        safe_text
)
OPLmetamodel::NumericExpression_strategy = st.builds(
    OPLmetamodel::NumericExpression,
)
OPLmetamodel::EnumLiteral_strategy = st.builds(
    OPLmetamodel::EnumLiteral,
)
OPLmetamodel::BooleanExpression_strategy = st.builds(
    OPLmetamodel::BooleanExpression,
    body=
        safe_text
)
OPLmetamodel::BooleanBlock_strategy = st.builds(
    OPLmetamodel::BooleanBlock,
)
Reference_strategy = st.builds(
    Reference,
)
OPLmetamodel::DataRef_strategy = st.builds(
    OPLmetamodel::DataRef,
)
OPLmetamodel::ParameterRef_strategy = st.builds(
    OPLmetamodel::ParameterRef,
)
OPLmetamodel::BindingRef_strategy = st.builds(
    OPLmetamodel::BindingRef,
)
AbstractBinaryOperator_strategy = st.builds(
    AbstractBinaryOperator,
)
OPLmetamodel::RelationalOperator_strategy = st.builds(
    OPLmetamodel::RelationalOperator,
    op=
        safe_text
)
OPLmetamodel::BinaryOperator_strategy = st.builds(
    OPLmetamodel::BinaryOperator,
    op=
        safe_text
)
OPLmetamodel::AbstractBinaryOperator_strategy = st.builds(
    OPLmetamodel::AbstractBinaryOperator,
)
PathExpression_strategy = st.builds(
    PathExpression,
)
OPLmetamodel::PathDereference_strategy = st.builds(
    OPLmetamodel::PathDereference,
)
OPLmetamodel::FunctionCall_strategy = st.builds(
    OPLmetamodel::FunctionCall,
    functionName=
        safe_text
)
OPLmetamodel::ArrayDereference_strategy = st.builds(
    OPLmetamodel::ArrayDereference,
)
OPLmetamodel::AllExpression_strategy = st.builds(
    OPLmetamodel::AllExpression,
)
OPLmetamodel::Expression_strategy = st.builds(
    OPLmetamodel::Expression,
)
OPLmetamodel::FormalParameter_strategy = st.builds(
    OPLmetamodel::FormalParameter,
    isOrdered=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
OPLmetamodel::PrimitiveExpression_strategy = st.builds(
    OPLmetamodel::PrimitiveExpression,
)
OPLmetamodel::ArrayValue_strategy = st.builds(
    OPLmetamodel::ArrayValue,
)
OPLmetamodel::BlockExpression_strategy = st.builds(
    OPLmetamodel::BlockExpression,
)
OPLmetamodel::BinaryExpression_strategy = st.builds(
    OPLmetamodel::BinaryExpression,
)
OPLmetamodel::ArraySlotConstraint_strategy = st.builds(
    OPLmetamodel::ArraySlotConstraint,
)
OPLmetamodel::RecordValue_strategy = st.builds(
    OPLmetamodel::RecordValue,
)
OPLmetamodel::UnaryExpression_strategy = st.builds(
    OPLmetamodel::UnaryExpression,
    op=
        safe_text
)
OPLmetamodel::IndexValuePair_strategy = st.builds(
    OPLmetamodel::IndexValuePair,
)
OPLmetamodel::PathExpression_strategy = st.builds(
    OPLmetamodel::PathExpression,
)
OPLmetamodel::Reference_strategy = st.builds(
    OPLmetamodel::Reference,
    name=
        safe_text
)
OPLmetamodel::IfExpression_strategy = st.builds(
    OPLmetamodel::IfExpression,
)
OPLmetamodel::SetValue_strategy = st.builds(
    OPLmetamodel::SetValue,
)
OPLmetamodel::CollectionExpression_strategy = st.builds(
    OPLmetamodel::CollectionExpression,
    isUnique=
        st.booleans()
)
OPLmetamodel::AggregateExp_strategy = st.builds(
    OPLmetamodel::AggregateExp,
    op=
        safe_text
)
OPLmetamodel::Number_strategy = st.builds(
    OPLmetamodel::Number,
)
Declaration_strategy = st.builds(
    Declaration,
)
OPLmetamodel::DefinedType_strategy = st.builds(
    OPLmetamodel::DefinedType,
)
OPLmetamodel::Function_strategy = st.builds(
    OPLmetamodel::Function,
)
OPLmetamodel::ScheduleInitialization_strategy = st.builds(
    OPLmetamodel::ScheduleInitialization,
)
OPLmetamodel::ResourceDeclaration_strategy = st.builds(
    OPLmetamodel::ResourceDeclaration,
)
OPLmetamodel::DataDeclaration_strategy = st.builds(
    OPLmetamodel::DataDeclaration,
    isDecisionVar=
        st.booleans(),
    isDecisionExpr=
        st.booleans()
)
OPLmetamodel::Setting_strategy = st.builds(
    OPLmetamodel::Setting,
)
OPLmetamodel::Assertion_strategy = st.builds(
    OPLmetamodel::Assertion,
)
OPLmetamodel::Constraint_strategy = st.builds(
    OPLmetamodel::Constraint,
    name=
        safe_text
)
OPLmetamodel::Objective_strategy = st.builds(
    OPLmetamodel::Objective,
    isLinearRelaxation=
        st.booleans(),
    action=
        safe_text
)
OPLmetamodel::Script_strategy = st.builds(
    OPLmetamodel::Script,
    isMain=
        st.booleans()
)
OPLmetamodel::ActivityDeclaration_strategy = st.builds(
    OPLmetamodel::ActivityDeclaration,
    earliestStartTime=
        safe_text,
    latestEndTime=
        safe_text
)
OPLmetamodel::AbstractType_strategy = st.builds(
    OPLmetamodel::AbstractType,
)

@given(instance=OPLmetamodel::TupleBinding_strategy)
@settings(max_examples=50)
def test_oplmetamodel::tuplebinding_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::TupleBinding)

@given(instance=PiecewiseLinearFunction_strategy)
@settings(max_examples=50)
def test_piecewiselinearfunction_instantiation(instance):
    assert isinstance(instance, PiecewiseLinearFunction)

@given(instance=ScriptStatement_strategy)
@settings(max_examples=50)
def test_scriptstatement_instantiation(instance):
    assert isinstance(instance, ScriptStatement)

@given(instance=OPLmetamodel::Writeln_strategy)
@settings(max_examples=50)
def test_oplmetamodel::writeln_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Writeln)

@given(instance=OPLmetamodel::Writeln_strategy)
def test_oplmetamodel::writeln_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=OPLmetamodel::Writeln_strategy)
def test_oplmetamodel::writeln_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=OPLmetamodel::Writeln_strategy)
def test_oplmetamodel::writeln_arg_type(instance):
    assert isinstance(instance.arg, str)


@given(instance=OPLmetamodel::Writeln_strategy)
def test_oplmetamodel::writeln_arg_setter(instance):
    original = instance.arg
    instance.arg = original
    assert instance.arg == original

@given(instance=OPLmetamodel::VariableBinding_strategy)
@settings(max_examples=50)
def test_oplmetamodel::variablebinding_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::VariableBinding)

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=OPLmetamodel::RelationalExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::relationalexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::RelationalExpression)

@given(instance=OPLmetamodel::RelationalExpression_strategy)
def test_oplmetamodel::relationalexpression_redefinedOp_type(instance):
    assert isinstance(instance.redefinedOp, str)


@given(instance=OPLmetamodel::RelationalExpression_strategy)
def test_oplmetamodel::relationalexpression_redefinedOp_setter(instance):
    original = instance.redefinedOp
    instance.redefinedOp = original
    assert instance.redefinedOp == original

@given(instance=BuiltInFunction_strategy)
@settings(max_examples=50)
def test_builtinfunction_instantiation(instance):
    assert isinstance(instance, BuiltInFunction)

@given(instance=OPLmetamodel::ReflectiveFunction_strategy)
@settings(max_examples=50)
def test_oplmetamodel::reflectivefunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::ReflectiveFunction)

@given(instance=OPLmetamodel::Sequence_strategy)
@settings(max_examples=50)
def test_oplmetamodel::sequence_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Sequence)

@given(instance=OPLmetamodel::ScriptStatement_strategy)
@settings(max_examples=50)
def test_oplmetamodel::scriptstatement_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::ScriptStatement)

@given(instance=DataInitMethods_strategy)
@settings(max_examples=50)
def test_datainitmethods_instantiation(instance):
    assert isinstance(instance, DataInitMethods)

@given(instance=OPLmetamodel::QueryUser_strategy)
@settings(max_examples=50)
def test_oplmetamodel::queryuser_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::QueryUser)

@given(instance=OPLmetamodel::QueryUser_strategy)
def test_oplmetamodel::queryuser_ask_type(instance):
    assert isinstance(instance.ask, str)


@given(instance=OPLmetamodel::QueryUser_strategy)
def test_oplmetamodel::queryuser_ask_setter(instance):
    original = instance.ask
    instance.ask = original
    assert instance.ask == original

@given(instance=OPLmetamodel::PiecewiseExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::piecewiseexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::PiecewiseExpression)

@given(instance=OPLmetamodel::RecordField_strategy)
@settings(max_examples=50)
def test_oplmetamodel::recordfield_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::RecordField)

@given(instance=OPLmetamodel::RecordField_strategy)
def test_oplmetamodel::recordfield_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OPLmetamodel::RecordField_strategy)
def test_oplmetamodel::recordfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ParameterDomain_strategy)
@settings(max_examples=50)
def test_parameterdomain_instantiation(instance):
    assert isinstance(instance, ParameterDomain)

@given(instance=OPLmetamodel::ReadFile_strategy)
@settings(max_examples=50)
def test_oplmetamodel::readfile_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::ReadFile)

@given(instance=OPLmetamodel::ReadFile_strategy)
def test_oplmetamodel::readfile_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=OPLmetamodel::ReadFile_strategy)
def test_oplmetamodel::readfile_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=OPLmetamodel::Model_strategy)
@settings(max_examples=50)
def test_oplmetamodel::model_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Model)

@given(instance=OPLmetamodel::Model_strategy)
def test_oplmetamodel::model_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=OPLmetamodel::Model_strategy)
def test_oplmetamodel::model_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=OPLmetamodel::Model_strategy)
def test_oplmetamodel::model_isConstraintProblem_type(instance):
    assert isinstance(instance.isConstraintProblem, bool)


@given(instance=OPLmetamodel::Model_strategy)
def test_oplmetamodel::model_isConstraintProblem_setter(instance):
    original = instance.isConstraintProblem
    instance.isConstraintProblem = original
    assert instance.isConstraintProblem == original

@given(instance=OPLmetamodel::Operator_strategy)
@settings(max_examples=50)
def test_oplmetamodel::operator_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Operator)

@given(instance=OPLmetamodel::SearchProcedure_strategy)
@settings(max_examples=50)
def test_oplmetamodel::searchprocedure_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::SearchProcedure)

@given(instance=IntegerType_strategy)
@settings(max_examples=50)
def test_integertype_instantiation(instance):
    assert isinstance(instance, IntegerType)

@given(instance=OPLmetamodel::PositiveIntegerType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::positiveintegertype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::PositiveIntegerType)

@given(instance=OPLmetamodel::StepFunction_strategy)
@settings(max_examples=50)
def test_oplmetamodel::stepfunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::StepFunction)

@given(instance=OPLmetamodel::Interval_strategy)
@settings(max_examples=50)
def test_oplmetamodel::interval_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Interval)

@given(instance=OPLmetamodel::Interval_strategy)
def test_oplmetamodel::interval_isOptional_type(instance):
    assert isinstance(instance.isOptional, bool)


@given(instance=OPLmetamodel::Interval_strategy)
def test_oplmetamodel::interval_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=OPLmetamodel::In_strategy)
@settings(max_examples=50)
def test_oplmetamodel::in_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::In)

@given(instance=FloatType_strategy)
@settings(max_examples=50)
def test_floattype_instantiation(instance):
    assert isinstance(instance, FloatType)

@given(instance=OPLmetamodel::PositiveFloatType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::positivefloattype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::PositiveFloatType)

@given(instance=OPLmetamodel::Error_strategy)
@settings(max_examples=50)
def test_oplmetamodel::error_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Error)

@given(instance=OPLmetamodel::Entity_strategy)
@settings(max_examples=50)
def test_oplmetamodel::entity_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Entity)

@given(instance=OPLmetamodel::FunctionRef_strategy)
@settings(max_examples=50)
def test_oplmetamodel::functionref_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::FunctionRef)

@given(instance=OPLmetamodel::FunctionRef_strategy)
def test_oplmetamodel::functionref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OPLmetamodel::FunctionRef_strategy)
def test_oplmetamodel::functionref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=OPLmetamodel::IfConstraint_strategy)
@settings(max_examples=50)
def test_oplmetamodel::ifconstraint_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::IfConstraint)

@given(instance=OPLmetamodel::ForAllConstraint_strategy)
@settings(max_examples=50)
def test_oplmetamodel::forallconstraint_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::ForAllConstraint)

@given(instance=NumericExpression_strategy)
@settings(max_examples=50)
def test_numericexpression_instantiation(instance):
    assert isinstance(instance, NumericExpression)

@given(instance=OPLmetamodel::IntegerExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::integerexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::IntegerExpression)

@given(instance=OPLmetamodel::IntegerExpression_strategy)
def test_oplmetamodel::integerexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=OPLmetamodel::IntegerExpression_strategy)
def test_oplmetamodel::integerexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=OPLmetamodel::RangeExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::rangeexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::RangeExpression)

@given(instance=OPLmetamodel::FloatExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::floatexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::FloatExpression)

@given(instance=OPLmetamodel::FloatExpression_strategy)
def test_oplmetamodel::floatexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=OPLmetamodel::FloatExpression_strategy)
def test_oplmetamodel::floatexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=OPLmetamodel::ParameterDomain_strategy)
@settings(max_examples=50)
def test_oplmetamodel::parameterdomain_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::ParameterDomain)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=OPLmetamodel::IntegerType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::integertype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::IntegerType)

@given(instance=OPLmetamodel::FloatType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::floattype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::FloatType)

@given(instance=RangeType_strategy)
@settings(max_examples=50)
def test_rangetype_instantiation(instance):
    assert isinstance(instance, RangeType)

@given(instance=OPLmetamodel::FloatRangeType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::floatrangetype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::FloatRangeType)

@given(instance=OPLmetamodel::IntegerRangeType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::integerrangetype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::IntegerRangeType)

@given(instance=Initialization_strategy)
@settings(max_examples=50)
def test_initialization_instantiation(instance):
    assert isinstance(instance, Initialization)

@given(instance=OPLmetamodel::RelationalInit_strategy)
@settings(max_examples=50)
def test_oplmetamodel::relationalinit_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::RelationalInit)

@given(instance=OPLmetamodel::DataObject_strategy)
@settings(max_examples=50)
def test_oplmetamodel::dataobject_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::DataObject)

@given(instance=OPLmetamodel::DataObject_strategy)
def test_oplmetamodel::dataobject_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=OPLmetamodel::DataObject_strategy)
def test_oplmetamodel::dataobject_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=OPLmetamodel::DataInitMethods_strategy)
@settings(max_examples=50)
def test_oplmetamodel::datainitmethods_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::DataInitMethods)

@given(instance=OPLmetamodel::Initialization_strategy)
@settings(max_examples=50)
def test_oplmetamodel::initialization_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Initialization)

@given(instance=SetType_strategy)
@settings(max_examples=50)
def test_settype_instantiation(instance):
    assert isinstance(instance, SetType)

@given(instance=OPLmetamodel::RangeType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::rangetype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::RangeType)

@given(instance=OPLmetamodel::EnumerationType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::enumerationtype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::EnumerationType)

@given(instance=OPLmetamodel::ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_oplmetamodel::parameterdeclaration_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::ParameterDeclaration)

@given(instance=OPLmetamodel::DisplayInstruction_strategy)
@settings(max_examples=50)
def test_oplmetamodel::displayinstruction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::DisplayInstruction)

@given(instance=AbstractType_strategy)
@settings(max_examples=50)
def test_abstracttype_instantiation(instance):
    assert isinstance(instance, AbstractType)

@given(instance=OPLmetamodel::PrimitiveType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::primitivetype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::PrimitiveType)

@given(instance=OPLmetamodel::DeferredInit_strategy)
@settings(max_examples=50)
def test_oplmetamodel::deferredinit_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::DeferredInit)

@given(instance=OPLmetamodel::Declaration_strategy)
@settings(max_examples=50)
def test_oplmetamodel::declaration_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Declaration)

@given(instance=OPLmetamodel::Declaration_strategy)
def test_oplmetamodel::declaration_order_type(instance):
    assert isinstance(instance.order, integertype)


@given(instance=OPLmetamodel::Declaration_strategy)
def test_oplmetamodel::declaration_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=DefinedType_strategy)
@settings(max_examples=50)
def test_definedtype_instantiation(instance):
    assert isinstance(instance, DefinedType)

@given(instance=OPLmetamodel::Record_strategy)
@settings(max_examples=50)
def test_oplmetamodel::record_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Record)

@given(instance=OPLmetamodel::Record_strategy)
def test_oplmetamodel::record_isTuple_type(instance):
    assert isinstance(instance.isTuple, bool)


@given(instance=OPLmetamodel::Record_strategy)
def test_oplmetamodel::record_isTuple_setter(instance):
    original = instance.isTuple
    instance.isTuple = original
    assert instance.isTuple == original

@given(instance=OPLmetamodel::Record_strategy)
def test_oplmetamodel::record_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OPLmetamodel::Record_strategy)
def test_oplmetamodel::record_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OPLmetamodel::SetType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::settype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::SetType)

@given(instance=OPLmetamodel::SetType_strategy)
def test_oplmetamodel::settype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OPLmetamodel::SetType_strategy)
def test_oplmetamodel::settype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OPLmetamodel::ArrayType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::arraytype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::ArrayType)

@given(instance=CollectionExpression_strategy)
@settings(max_examples=50)
def test_collectionexpression_instantiation(instance):
    assert isinstance(instance, CollectionExpression)

@given(instance=OPLmetamodel::Extension_strategy)
@settings(max_examples=50)
def test_oplmetamodel::extension_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Extension)

@given(instance=OPLmetamodel::Comprehension_strategy)
@settings(max_examples=50)
def test_oplmetamodel::comprehension_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Comprehension)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=OPLmetamodel::CumulativeFunction_strategy)
@settings(max_examples=50)
def test_oplmetamodel::cumulativefunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::CumulativeFunction)

@given(instance=OPLmetamodel::PiecewiseLinearFunction_strategy)
@settings(max_examples=50)
def test_oplmetamodel::piecewiselinearfunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::PiecewiseLinearFunction)

@given(instance=OPLmetamodel::StateFunction_strategy)
@settings(max_examples=50)
def test_oplmetamodel::statefunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::StateFunction)

@given(instance=OPLmetamodel::BuiltInFunction_strategy)
@settings(max_examples=50)
def test_oplmetamodel::builtinfunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::BuiltInFunction)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=OPLmetamodel::StringType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::stringtype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::StringType)

@given(instance=OPLmetamodel::NumericType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::numerictype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::NumericType)

@given(instance=OPLmetamodel::BooleanType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::booleantype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::BooleanType)

@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_primitiveexpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)

@given(instance=OPLmetamodel::StringExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::stringexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::StringExpression)

@given(instance=OPLmetamodel::StringExpression_strategy)
def test_oplmetamodel::stringexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=OPLmetamodel::StringExpression_strategy)
def test_oplmetamodel::stringexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=OPLmetamodel::NumericExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::numericexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::NumericExpression)

@given(instance=OPLmetamodel::EnumLiteral_strategy)
@settings(max_examples=50)
def test_oplmetamodel::enumliteral_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::EnumLiteral)

@given(instance=OPLmetamodel::BooleanExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::booleanexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::BooleanExpression)

@given(instance=OPLmetamodel::BooleanExpression_strategy)
def test_oplmetamodel::booleanexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=OPLmetamodel::BooleanExpression_strategy)
def test_oplmetamodel::booleanexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=OPLmetamodel::BooleanBlock_strategy)
@settings(max_examples=50)
def test_oplmetamodel::booleanblock_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::BooleanBlock)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=OPLmetamodel::DataRef_strategy)
@settings(max_examples=50)
def test_oplmetamodel::dataref_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::DataRef)

@given(instance=OPLmetamodel::ParameterRef_strategy)
@settings(max_examples=50)
def test_oplmetamodel::parameterref_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::ParameterRef)

@given(instance=OPLmetamodel::BindingRef_strategy)
@settings(max_examples=50)
def test_oplmetamodel::bindingref_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::BindingRef)

@given(instance=AbstractBinaryOperator_strategy)
@settings(max_examples=50)
def test_abstractbinaryoperator_instantiation(instance):
    assert isinstance(instance, AbstractBinaryOperator)

@given(instance=OPLmetamodel::RelationalOperator_strategy)
@settings(max_examples=50)
def test_oplmetamodel::relationaloperator_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::RelationalOperator)

@given(instance=OPLmetamodel::RelationalOperator_strategy)
def test_oplmetamodel::relationaloperator_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=OPLmetamodel::RelationalOperator_strategy)
def test_oplmetamodel::relationaloperator_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=OPLmetamodel::BinaryOperator_strategy)
@settings(max_examples=50)
def test_oplmetamodel::binaryoperator_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::BinaryOperator)

@given(instance=OPLmetamodel::BinaryOperator_strategy)
def test_oplmetamodel::binaryoperator_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=OPLmetamodel::BinaryOperator_strategy)
def test_oplmetamodel::binaryoperator_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=OPLmetamodel::AbstractBinaryOperator_strategy)
@settings(max_examples=50)
def test_oplmetamodel::abstractbinaryoperator_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::AbstractBinaryOperator)

@given(instance=PathExpression_strategy)
@settings(max_examples=50)
def test_pathexpression_instantiation(instance):
    assert isinstance(instance, PathExpression)

@given(instance=OPLmetamodel::PathDereference_strategy)
@settings(max_examples=50)
def test_oplmetamodel::pathdereference_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::PathDereference)

@given(instance=OPLmetamodel::FunctionCall_strategy)
@settings(max_examples=50)
def test_oplmetamodel::functioncall_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::FunctionCall)

@given(instance=OPLmetamodel::FunctionCall_strategy)
def test_oplmetamodel::functioncall_functionName_type(instance):
    assert isinstance(instance.functionName, str)


@given(instance=OPLmetamodel::FunctionCall_strategy)
def test_oplmetamodel::functioncall_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=OPLmetamodel::ArrayDereference_strategy)
@settings(max_examples=50)
def test_oplmetamodel::arraydereference_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::ArrayDereference)

@given(instance=OPLmetamodel::AllExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::allexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::AllExpression)

@given(instance=OPLmetamodel::Expression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::expression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Expression)

@given(instance=OPLmetamodel::FormalParameter_strategy)
@settings(max_examples=50)
def test_oplmetamodel::formalparameter_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::FormalParameter)

@given(instance=OPLmetamodel::FormalParameter_strategy)
def test_oplmetamodel::formalparameter_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, bool)


@given(instance=OPLmetamodel::FormalParameter_strategy)
def test_oplmetamodel::formalparameter_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=OPLmetamodel::PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::primitiveexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::PrimitiveExpression)

@given(instance=OPLmetamodel::ArrayValue_strategy)
@settings(max_examples=50)
def test_oplmetamodel::arrayvalue_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::ArrayValue)

@given(instance=OPLmetamodel::BlockExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::blockexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::BlockExpression)

@given(instance=OPLmetamodel::BinaryExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::binaryexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::BinaryExpression)

@given(instance=OPLmetamodel::ArraySlotConstraint_strategy)
@settings(max_examples=50)
def test_oplmetamodel::arrayslotconstraint_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::ArraySlotConstraint)

@given(instance=OPLmetamodel::RecordValue_strategy)
@settings(max_examples=50)
def test_oplmetamodel::recordvalue_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::RecordValue)

@given(instance=OPLmetamodel::UnaryExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::unaryexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::UnaryExpression)

@given(instance=OPLmetamodel::UnaryExpression_strategy)
def test_oplmetamodel::unaryexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=OPLmetamodel::UnaryExpression_strategy)
def test_oplmetamodel::unaryexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=OPLmetamodel::IndexValuePair_strategy)
@settings(max_examples=50)
def test_oplmetamodel::indexvaluepair_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::IndexValuePair)

@given(instance=OPLmetamodel::PathExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::pathexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::PathExpression)

@given(instance=OPLmetamodel::Reference_strategy)
@settings(max_examples=50)
def test_oplmetamodel::reference_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Reference)

@given(instance=OPLmetamodel::Reference_strategy)
def test_oplmetamodel::reference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OPLmetamodel::Reference_strategy)
def test_oplmetamodel::reference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OPLmetamodel::IfExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::ifexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::IfExpression)

@given(instance=OPLmetamodel::SetValue_strategy)
@settings(max_examples=50)
def test_oplmetamodel::setvalue_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::SetValue)

@given(instance=OPLmetamodel::CollectionExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel::collectionexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::CollectionExpression)

@given(instance=OPLmetamodel::CollectionExpression_strategy)
def test_oplmetamodel::collectionexpression_isUnique_type(instance):
    assert isinstance(instance.isUnique, bool)


@given(instance=OPLmetamodel::CollectionExpression_strategy)
def test_oplmetamodel::collectionexpression_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=OPLmetamodel::AggregateExp_strategy)
@settings(max_examples=50)
def test_oplmetamodel::aggregateexp_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::AggregateExp)

@given(instance=OPLmetamodel::AggregateExp_strategy)
def test_oplmetamodel::aggregateexp_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=OPLmetamodel::AggregateExp_strategy)
def test_oplmetamodel::aggregateexp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=OPLmetamodel::Number_strategy)
@settings(max_examples=50)
def test_oplmetamodel::number_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Number)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=OPLmetamodel::DefinedType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::definedtype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::DefinedType)

@given(instance=OPLmetamodel::Function_strategy)
@settings(max_examples=50)
def test_oplmetamodel::function_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Function)

@given(instance=OPLmetamodel::ScheduleInitialization_strategy)
@settings(max_examples=50)
def test_oplmetamodel::scheduleinitialization_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::ScheduleInitialization)

@given(instance=OPLmetamodel::ResourceDeclaration_strategy)
@settings(max_examples=50)
def test_oplmetamodel::resourcedeclaration_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::ResourceDeclaration)

@given(instance=OPLmetamodel::DataDeclaration_strategy)
@settings(max_examples=50)
def test_oplmetamodel::datadeclaration_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::DataDeclaration)

@given(instance=OPLmetamodel::DataDeclaration_strategy)
def test_oplmetamodel::datadeclaration_isDecisionVar_type(instance):
    assert isinstance(instance.isDecisionVar, bool)


@given(instance=OPLmetamodel::DataDeclaration_strategy)
def test_oplmetamodel::datadeclaration_isDecisionVar_setter(instance):
    original = instance.isDecisionVar
    instance.isDecisionVar = original
    assert instance.isDecisionVar == original

@given(instance=OPLmetamodel::DataDeclaration_strategy)
def test_oplmetamodel::datadeclaration_isDecisionExpr_type(instance):
    assert isinstance(instance.isDecisionExpr, bool)


@given(instance=OPLmetamodel::DataDeclaration_strategy)
def test_oplmetamodel::datadeclaration_isDecisionExpr_setter(instance):
    original = instance.isDecisionExpr
    instance.isDecisionExpr = original
    assert instance.isDecisionExpr == original

@given(instance=OPLmetamodel::Setting_strategy)
@settings(max_examples=50)
def test_oplmetamodel::setting_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Setting)

@given(instance=OPLmetamodel::Assertion_strategy)
@settings(max_examples=50)
def test_oplmetamodel::assertion_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Assertion)

@given(instance=OPLmetamodel::Constraint_strategy)
@settings(max_examples=50)
def test_oplmetamodel::constraint_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Constraint)

@given(instance=OPLmetamodel::Constraint_strategy)
def test_oplmetamodel::constraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OPLmetamodel::Constraint_strategy)
def test_oplmetamodel::constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OPLmetamodel::Objective_strategy)
@settings(max_examples=50)
def test_oplmetamodel::objective_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Objective)

@given(instance=OPLmetamodel::Objective_strategy)
def test_oplmetamodel::objective_isLinearRelaxation_type(instance):
    assert isinstance(instance.isLinearRelaxation, bool)


@given(instance=OPLmetamodel::Objective_strategy)
def test_oplmetamodel::objective_isLinearRelaxation_setter(instance):
    original = instance.isLinearRelaxation
    instance.isLinearRelaxation = original
    assert instance.isLinearRelaxation == original

@given(instance=OPLmetamodel::Objective_strategy)
def test_oplmetamodel::objective_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=OPLmetamodel::Objective_strategy)
def test_oplmetamodel::objective_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=OPLmetamodel::Script_strategy)
@settings(max_examples=50)
def test_oplmetamodel::script_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::Script)

@given(instance=OPLmetamodel::Script_strategy)
def test_oplmetamodel::script_isMain_type(instance):
    assert isinstance(instance.isMain, bool)


@given(instance=OPLmetamodel::Script_strategy)
def test_oplmetamodel::script_isMain_setter(instance):
    original = instance.isMain
    instance.isMain = original
    assert instance.isMain == original

@given(instance=OPLmetamodel::ActivityDeclaration_strategy)
@settings(max_examples=50)
def test_oplmetamodel::activitydeclaration_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::ActivityDeclaration)

@given(instance=OPLmetamodel::ActivityDeclaration_strategy)
def test_oplmetamodel::activitydeclaration_earliestStartTime_type(instance):
    assert isinstance(instance.earliestStartTime, str)


@given(instance=OPLmetamodel::ActivityDeclaration_strategy)
def test_oplmetamodel::activitydeclaration_earliestStartTime_setter(instance):
    original = instance.earliestStartTime
    instance.earliestStartTime = original
    assert instance.earliestStartTime == original

@given(instance=OPLmetamodel::ActivityDeclaration_strategy)
def test_oplmetamodel::activitydeclaration_latestEndTime_type(instance):
    assert isinstance(instance.latestEndTime, str)


@given(instance=OPLmetamodel::ActivityDeclaration_strategy)
def test_oplmetamodel::activitydeclaration_latestEndTime_setter(instance):
    original = instance.latestEndTime
    instance.latestEndTime = original
    assert instance.latestEndTime == original

@given(instance=OPLmetamodel::AbstractType_strategy)
@settings(max_examples=50)
def test_oplmetamodel::abstracttype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel::AbstractType)
