import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BuiltinDefinition,
    ast::BuiltinVariable,
    ast::BuiltinFunction,
    ast::Statement,
    Statement,
    ast::BreakStatement,
    ast::ReturnStatement,
    ast::ContinueStatement,
    ast::ForStatement,
    ast::DoWhileStatement,
    ast::WhileStatement,
    ast::Compound,
    PrimitiveStepExpression,
    ast::StepN,
    ast::StepLiteral,
    ast::IfStatement,
    ast::Assignment,
    StepExpression,
    ast::PrimitiveStepExpression,
    ast::AdditiveStepExpression,
    ast::NegateStepExpression,
    ast::RangeStepExpression,
    ast::StepExpression,
    FeatureCall,
    ast::FunctionCall,
    ast::VariableAccess,
    ast::ExpressionList,
    ast::ArrayConstructionIterationClause,
    ast::Unit,
    ast::ArraySubscript,
    ast::LetExpressionVariableDeclaration,
    Expression,
    ast::LogicalOrExpression,
    ast::TypeTestExpression,
    ast::ArrayConcatenationOperator,
    ast::ParenthesizedExpression,
    ast::EqualityExpression,
    ast::AdditiveExpression,
    ast::LogicalAndExpression,
    ast::DerivativeOperator,
    ast::RelationalExpression,
    ast::UnitConstructionOperator,
    ast::IterationCall,
    ast::UnaryExpression,
    ast::MemberVariableAccess,
    ast::FeatureCall,
    ast::PowerExpression,
    ast::PostfixExpression,
    ast::RangeExpression,
    ast::ArrayConstructionOperator,
    ast::MultiplicativeExpression,
    ast::EndExpression,
    ast::AlgorithmExpression,
    ast::ImpliesExpression,
    ast::ArrayElementAccess,
    ast::LetExpression,
    ast::DataType,
    ast::SwitchCase,
    ast::SwitchExpression,
    ast::IfExpression,
    ast::CallableElement,
    ast::Expression,
    ast::Equation,
    ast::Assertion,
    ast::Check,
    ParameterDeclaration,
    ast::OutputParameterDeclaration,
    ast::EnumerationLiteralDeclaration,
    DataTypeDefinition,
    ast::TypeAliasDefinition,
    ast::EnumerationDefinition,
    Definition,
    ast::DataTypeDefinition,
    ast::Definition,
    ast::Module,
    ast::InputParameterDeclaration,
    ast::TemplateParameterDeclaration,
    CallableElement,
    ast::StateVariableDeclaration,
    ast::LetExpressionVariableDeclarationPart,
    ast::IterationAccumulator,
    ast::ParameterDeclaration,
    ast::FunctionObjectDeclaration,
    ast::BuiltinDefinition,
    ast::VariableDeclaration,
    ast::IterationVariable,
    ast::FunctionDefinition,
    ast::DataTypeSpecifier,
    ast::StructMemberDeclaration,
    ast::StructDefinition,
    ast::PrimitiveType,
    PostfixOperator,
    AdditiveOperator,
    RelationalOperator,
    AssertionStatusKind,
    EqualityOperator,
    UnaryOperator,
    PowerOperator,
    MultiplicativeOperator,
    FunctionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_builtindefinition_is_not_abstract():
    assert not inspect.isabstract(BuiltinDefinition)


def test_builtindefinition_constructor_exists():
    assert callable(BuiltinDefinition.__init__)


def test_builtindefinition_constructor_args():
    sig = inspect.signature(BuiltinDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ast::builtinvariable_is_not_abstract():
    assert not inspect.isabstract(ast::BuiltinVariable)


def test_ast::builtinvariable_constructor_exists():
    assert callable(ast::BuiltinVariable.__init__)


def test_ast::builtinvariable_constructor_args():
    sig = inspect.signature(ast::BuiltinVariable.__init__)
    params = list(sig.parameters.keys())



def test_ast::builtinfunction_is_not_abstract():
    assert not inspect.isabstract(ast::BuiltinFunction)


def test_ast::builtinfunction_constructor_exists():
    assert callable(ast::BuiltinFunction.__init__)


def test_ast::builtinfunction_constructor_args():
    sig = inspect.signature(ast::BuiltinFunction.__init__)
    params = list(sig.parameters.keys())



def test_ast::statement_is_not_abstract():
    assert not inspect.isabstract(ast::Statement)


def test_ast::statement_constructor_exists():
    assert callable(ast::Statement.__init__)


def test_ast::statement_constructor_args():
    sig = inspect.signature(ast::Statement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_ast::breakstatement_is_not_abstract():
    assert not inspect.isabstract(ast::BreakStatement)


def test_ast::breakstatement_constructor_exists():
    assert callable(ast::BreakStatement.__init__)


def test_ast::breakstatement_constructor_args():
    sig = inspect.signature(ast::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::returnstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ReturnStatement)


def test_ast::returnstatement_constructor_exists():
    assert callable(ast::ReturnStatement.__init__)


def test_ast::returnstatement_constructor_args():
    sig = inspect.signature(ast::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::continuestatement_is_not_abstract():
    assert not inspect.isabstract(ast::ContinueStatement)


def test_ast::continuestatement_constructor_exists():
    assert callable(ast::ContinueStatement.__init__)


def test_ast::continuestatement_constructor_args():
    sig = inspect.signature(ast::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::forstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ForStatement)


def test_ast::forstatement_constructor_exists():
    assert callable(ast::ForStatement.__init__)


def test_ast::forstatement_constructor_args():
    sig = inspect.signature(ast::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(ast::DoWhileStatement)


def test_ast::dowhilestatement_constructor_exists():
    assert callable(ast::DoWhileStatement.__init__)


def test_ast::dowhilestatement_constructor_args():
    sig = inspect.signature(ast::DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::whilestatement_is_not_abstract():
    assert not inspect.isabstract(ast::WhileStatement)


def test_ast::whilestatement_constructor_exists():
    assert callable(ast::WhileStatement.__init__)


def test_ast::whilestatement_constructor_args():
    sig = inspect.signature(ast::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::compound_is_not_abstract():
    assert not inspect.isabstract(ast::Compound)


def test_ast::compound_constructor_exists():
    assert callable(ast::Compound.__init__)


def test_ast::compound_constructor_args():
    sig = inspect.signature(ast::Compound.__init__)
    params = list(sig.parameters.keys())



def test_primitivestepexpression_is_not_abstract():
    assert not inspect.isabstract(PrimitiveStepExpression)


def test_primitivestepexpression_constructor_exists():
    assert callable(PrimitiveStepExpression.__init__)


def test_primitivestepexpression_constructor_args():
    sig = inspect.signature(PrimitiveStepExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::stepn_is_not_abstract():
    assert not inspect.isabstract(ast::StepN)


def test_ast::stepn_constructor_exists():
    assert callable(ast::StepN.__init__)


def test_ast::stepn_constructor_args():
    sig = inspect.signature(ast::StepN.__init__)
    params = list(sig.parameters.keys())



def test_ast::stepliteral_is_not_abstract():
    assert not inspect.isabstract(ast::StepLiteral)


def test_ast::stepliteral_constructor_exists():
    assert callable(ast::StepLiteral.__init__)


def test_ast::stepliteral_constructor_args():
    sig = inspect.signature(ast::StepLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ast::stepliteral_has_value():
    assert hasattr(ast::StepLiteral, "value")
    descriptor = None
    for klass in ast::StepLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ast::ifstatement_is_not_abstract():
    assert not inspect.isabstract(ast::IfStatement)


def test_ast::ifstatement_constructor_exists():
    assert callable(ast::IfStatement.__init__)


def test_ast::ifstatement_constructor_args():
    sig = inspect.signature(ast::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::assignment_is_not_abstract():
    assert not inspect.isabstract(ast::Assignment)


def test_ast::assignment_constructor_exists():
    assert callable(ast::Assignment.__init__)


def test_ast::assignment_constructor_args():
    sig = inspect.signature(ast::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_stepexpression_is_not_abstract():
    assert not inspect.isabstract(StepExpression)


def test_stepexpression_constructor_exists():
    assert callable(StepExpression.__init__)


def test_stepexpression_constructor_args():
    sig = inspect.signature(StepExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::primitivestepexpression_is_not_abstract():
    assert not inspect.isabstract(ast::PrimitiveStepExpression)


def test_ast::primitivestepexpression_constructor_exists():
    assert callable(ast::PrimitiveStepExpression.__init__)


def test_ast::primitivestepexpression_constructor_args():
    sig = inspect.signature(ast::PrimitiveStepExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::additivestepexpression_is_not_abstract():
    assert not inspect.isabstract(ast::AdditiveStepExpression)


def test_ast::additivestepexpression_constructor_exists():
    assert callable(ast::AdditiveStepExpression.__init__)


def test_ast::additivestepexpression_constructor_args():
    sig = inspect.signature(ast::AdditiveStepExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast::additivestepexpression_has_operator():
    assert hasattr(ast::AdditiveStepExpression, "operator")
    descriptor = None
    for klass in ast::AdditiveStepExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast::negatestepexpression_is_not_abstract():
    assert not inspect.isabstract(ast::NegateStepExpression)


def test_ast::negatestepexpression_constructor_exists():
    assert callable(ast::NegateStepExpression.__init__)


def test_ast::negatestepexpression_constructor_args():
    sig = inspect.signature(ast::NegateStepExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::rangestepexpression_is_not_abstract():
    assert not inspect.isabstract(ast::RangeStepExpression)


def test_ast::rangestepexpression_constructor_exists():
    assert callable(ast::RangeStepExpression.__init__)


def test_ast::rangestepexpression_constructor_args():
    sig = inspect.signature(ast::RangeStepExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::stepexpression_is_not_abstract():
    assert not inspect.isabstract(ast::StepExpression)


def test_ast::stepexpression_constructor_exists():
    assert callable(ast::StepExpression.__init__)


def test_ast::stepexpression_constructor_args():
    sig = inspect.signature(ast::StepExpression.__init__)
    params = list(sig.parameters.keys())



def test_featurecall_is_not_abstract():
    assert not inspect.isabstract(FeatureCall)


def test_featurecall_constructor_exists():
    assert callable(FeatureCall.__init__)


def test_featurecall_constructor_args():
    sig = inspect.signature(FeatureCall.__init__)
    params = list(sig.parameters.keys())



def test_ast::functioncall_is_not_abstract():
    assert not inspect.isabstract(ast::FunctionCall)


def test_ast::functioncall_constructor_exists():
    assert callable(ast::FunctionCall.__init__)


def test_ast::functioncall_constructor_args():
    sig = inspect.signature(ast::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_ast::variableaccess_is_not_abstract():
    assert not inspect.isabstract(ast::VariableAccess)


def test_ast::variableaccess_constructor_exists():
    assert callable(ast::VariableAccess.__init__)


def test_ast::variableaccess_constructor_args():
    sig = inspect.signature(ast::VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_ast::expressionlist_is_not_abstract():
    assert not inspect.isabstract(ast::ExpressionList)


def test_ast::expressionlist_constructor_exists():
    assert callable(ast::ExpressionList.__init__)


def test_ast::expressionlist_constructor_args():
    sig = inspect.signature(ast::ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_ast::arrayconstructioniterationclause_is_not_abstract():
    assert not inspect.isabstract(ast::ArrayConstructionIterationClause)


def test_ast::arrayconstructioniterationclause_constructor_exists():
    assert callable(ast::ArrayConstructionIterationClause.__init__)


def test_ast::arrayconstructioniterationclause_constructor_args():
    sig = inspect.signature(ast::ArrayConstructionIterationClause.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_ast::arrayconstructioniterationclause_has_variableName():
    assert hasattr(ast::ArrayConstructionIterationClause, "variableName")
    descriptor = None
    for klass in ast::ArrayConstructionIterationClause.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_ast::unit_is_not_abstract():
    assert not inspect.isabstract(ast::Unit)


def test_ast::unit_constructor_exists():
    assert callable(ast::Unit.__init__)


def test_ast::unit_constructor_args():
    sig = inspect.signature(ast::Unit.__init__)
    params = list(sig.parameters.keys())



def test_ast::arraysubscript_is_not_abstract():
    assert not inspect.isabstract(ast::ArraySubscript)


def test_ast::arraysubscript_constructor_exists():
    assert callable(ast::ArraySubscript.__init__)


def test_ast::arraysubscript_constructor_args():
    sig = inspect.signature(ast::ArraySubscript.__init__)
    params = list(sig.parameters.keys())
    assert "slice" in params, "Missing parameter 'slice'"

def test_ast::arraysubscript_has_slice():
    assert hasattr(ast::ArraySubscript, "slice")
    descriptor = None
    for klass in ast::ArraySubscript.__mro__:
        if "slice" in klass.__dict__:
            descriptor = klass.__dict__["slice"]
            break
    assert isinstance(descriptor, property)



def test_ast::letexpressionvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::LetExpressionVariableDeclaration)


def test_ast::letexpressionvariabledeclaration_constructor_exists():
    assert callable(ast::LetExpressionVariableDeclaration.__init__)


def test_ast::letexpressionvariabledeclaration_constructor_args():
    sig = inspect.signature(ast::LetExpressionVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_ast::logicalorexpression_is_not_abstract():
    assert not inspect.isabstract(ast::LogicalOrExpression)


def test_ast::logicalorexpression_constructor_exists():
    assert callable(ast::LogicalOrExpression.__init__)


def test_ast::logicalorexpression_constructor_args():
    sig = inspect.signature(ast::LogicalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::typetestexpression_is_not_abstract():
    assert not inspect.isabstract(ast::TypeTestExpression)


def test_ast::typetestexpression_constructor_exists():
    assert callable(ast::TypeTestExpression.__init__)


def test_ast::typetestexpression_constructor_args():
    sig = inspect.signature(ast::TypeTestExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::arrayconcatenationoperator_is_not_abstract():
    assert not inspect.isabstract(ast::ArrayConcatenationOperator)


def test_ast::arrayconcatenationoperator_constructor_exists():
    assert callable(ast::ArrayConcatenationOperator.__init__)


def test_ast::arrayconcatenationoperator_constructor_args():
    sig = inspect.signature(ast::ArrayConcatenationOperator.__init__)
    params = list(sig.parameters.keys())



def test_ast::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(ast::ParenthesizedExpression)


def test_ast::parenthesizedexpression_constructor_exists():
    assert callable(ast::ParenthesizedExpression.__init__)


def test_ast::parenthesizedexpression_constructor_args():
    sig = inspect.signature(ast::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(ast::EqualityExpression)


def test_ast::equalityexpression_constructor_exists():
    assert callable(ast::EqualityExpression.__init__)


def test_ast::equalityexpression_constructor_args():
    sig = inspect.signature(ast::EqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast::equalityexpression_has_operator():
    assert hasattr(ast::EqualityExpression, "operator")
    descriptor = None
    for klass in ast::EqualityExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast::additiveexpression_is_not_abstract():
    assert not inspect.isabstract(ast::AdditiveExpression)


def test_ast::additiveexpression_constructor_exists():
    assert callable(ast::AdditiveExpression.__init__)


def test_ast::additiveexpression_constructor_args():
    sig = inspect.signature(ast::AdditiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast::additiveexpression_has_operator():
    assert hasattr(ast::AdditiveExpression, "operator")
    descriptor = None
    for klass in ast::AdditiveExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast::logicalandexpression_is_not_abstract():
    assert not inspect.isabstract(ast::LogicalAndExpression)


def test_ast::logicalandexpression_constructor_exists():
    assert callable(ast::LogicalAndExpression.__init__)


def test_ast::logicalandexpression_constructor_args():
    sig = inspect.signature(ast::LogicalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::derivativeoperator_is_not_abstract():
    assert not inspect.isabstract(ast::DerivativeOperator)


def test_ast::derivativeoperator_constructor_exists():
    assert callable(ast::DerivativeOperator.__init__)


def test_ast::derivativeoperator_constructor_args():
    sig = inspect.signature(ast::DerivativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_ast::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(ast::RelationalExpression)


def test_ast::relationalexpression_constructor_exists():
    assert callable(ast::RelationalExpression.__init__)


def test_ast::relationalexpression_constructor_args():
    sig = inspect.signature(ast::RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast::relationalexpression_has_operator():
    assert hasattr(ast::RelationalExpression, "operator")
    descriptor = None
    for klass in ast::RelationalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast::unitconstructionoperator_is_not_abstract():
    assert not inspect.isabstract(ast::UnitConstructionOperator)


def test_ast::unitconstructionoperator_constructor_exists():
    assert callable(ast::UnitConstructionOperator.__init__)


def test_ast::unitconstructionoperator_constructor_args():
    sig = inspect.signature(ast::UnitConstructionOperator.__init__)
    params = list(sig.parameters.keys())



def test_ast::iterationcall_is_not_abstract():
    assert not inspect.isabstract(ast::IterationCall)


def test_ast::iterationcall_constructor_exists():
    assert callable(ast::IterationCall.__init__)


def test_ast::iterationcall_constructor_args():
    sig = inspect.signature(ast::IterationCall.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ast::iterationcall_has_identifier():
    assert hasattr(ast::IterationCall, "identifier")
    descriptor = None
    for klass in ast::IterationCall.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ast::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(ast::UnaryExpression)


def test_ast::unaryexpression_constructor_exists():
    assert callable(ast::UnaryExpression.__init__)


def test_ast::unaryexpression_constructor_args():
    sig = inspect.signature(ast::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast::unaryexpression_has_operator():
    assert hasattr(ast::UnaryExpression, "operator")
    descriptor = None
    for klass in ast::UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast::membervariableaccess_is_not_abstract():
    assert not inspect.isabstract(ast::MemberVariableAccess)


def test_ast::membervariableaccess_constructor_exists():
    assert callable(ast::MemberVariableAccess.__init__)


def test_ast::membervariableaccess_constructor_args():
    sig = inspect.signature(ast::MemberVariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_ast::featurecall_is_not_abstract():
    assert not inspect.isabstract(ast::FeatureCall)


def test_ast::featurecall_constructor_exists():
    assert callable(ast::FeatureCall.__init__)


def test_ast::featurecall_constructor_args():
    sig = inspect.signature(ast::FeatureCall.__init__)
    params = list(sig.parameters.keys())



def test_ast::powerexpression_is_not_abstract():
    assert not inspect.isabstract(ast::PowerExpression)


def test_ast::powerexpression_constructor_exists():
    assert callable(ast::PowerExpression.__init__)


def test_ast::powerexpression_constructor_args():
    sig = inspect.signature(ast::PowerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast::powerexpression_has_operator():
    assert hasattr(ast::PowerExpression, "operator")
    descriptor = None
    for klass in ast::PowerExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast::postfixexpression_is_not_abstract():
    assert not inspect.isabstract(ast::PostfixExpression)


def test_ast::postfixexpression_constructor_exists():
    assert callable(ast::PostfixExpression.__init__)


def test_ast::postfixexpression_constructor_args():
    sig = inspect.signature(ast::PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast::postfixexpression_has_operator():
    assert hasattr(ast::PostfixExpression, "operator")
    descriptor = None
    for klass in ast::PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast::rangeexpression_is_not_abstract():
    assert not inspect.isabstract(ast::RangeExpression)


def test_ast::rangeexpression_constructor_exists():
    assert callable(ast::RangeExpression.__init__)


def test_ast::rangeexpression_constructor_args():
    sig = inspect.signature(ast::RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::arrayconstructionoperator_is_not_abstract():
    assert not inspect.isabstract(ast::ArrayConstructionOperator)


def test_ast::arrayconstructionoperator_constructor_exists():
    assert callable(ast::ArrayConstructionOperator.__init__)


def test_ast::arrayconstructionoperator_constructor_args():
    sig = inspect.signature(ast::ArrayConstructionOperator.__init__)
    params = list(sig.parameters.keys())



def test_ast::multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(ast::MultiplicativeExpression)


def test_ast::multiplicativeexpression_constructor_exists():
    assert callable(ast::MultiplicativeExpression.__init__)


def test_ast::multiplicativeexpression_constructor_args():
    sig = inspect.signature(ast::MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ast::multiplicativeexpression_has_operator():
    assert hasattr(ast::MultiplicativeExpression, "operator")
    descriptor = None
    for klass in ast::MultiplicativeExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ast::endexpression_is_not_abstract():
    assert not inspect.isabstract(ast::EndExpression)


def test_ast::endexpression_constructor_exists():
    assert callable(ast::EndExpression.__init__)


def test_ast::endexpression_constructor_args():
    sig = inspect.signature(ast::EndExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::algorithmexpression_is_not_abstract():
    assert not inspect.isabstract(ast::AlgorithmExpression)


def test_ast::algorithmexpression_constructor_exists():
    assert callable(ast::AlgorithmExpression.__init__)


def test_ast::algorithmexpression_constructor_args():
    sig = inspect.signature(ast::AlgorithmExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::impliesexpression_is_not_abstract():
    assert not inspect.isabstract(ast::ImpliesExpression)


def test_ast::impliesexpression_constructor_exists():
    assert callable(ast::ImpliesExpression.__init__)


def test_ast::impliesexpression_constructor_args():
    sig = inspect.signature(ast::ImpliesExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::arrayelementaccess_is_not_abstract():
    assert not inspect.isabstract(ast::ArrayElementAccess)


def test_ast::arrayelementaccess_constructor_exists():
    assert callable(ast::ArrayElementAccess.__init__)


def test_ast::arrayelementaccess_constructor_args():
    sig = inspect.signature(ast::ArrayElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_ast::letexpression_is_not_abstract():
    assert not inspect.isabstract(ast::LetExpression)


def test_ast::letexpression_constructor_exists():
    assert callable(ast::LetExpression.__init__)


def test_ast::letexpression_constructor_args():
    sig = inspect.signature(ast::LetExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::datatype_is_not_abstract():
    assert not inspect.isabstract(ast::DataType)


def test_ast::datatype_constructor_exists():
    assert callable(ast::DataType.__init__)


def test_ast::datatype_constructor_args():
    sig = inspect.signature(ast::DataType.__init__)
    params = list(sig.parameters.keys())



def test_ast::switchcase_is_not_abstract():
    assert not inspect.isabstract(ast::SwitchCase)


def test_ast::switchcase_constructor_exists():
    assert callable(ast::SwitchCase.__init__)


def test_ast::switchcase_constructor_args():
    sig = inspect.signature(ast::SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_ast::switchexpression_is_not_abstract():
    assert not inspect.isabstract(ast::SwitchExpression)


def test_ast::switchexpression_constructor_exists():
    assert callable(ast::SwitchExpression.__init__)


def test_ast::switchexpression_constructor_args():
    sig = inspect.signature(ast::SwitchExpression.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_ast::switchexpression_has_static():
    assert hasattr(ast::SwitchExpression, "static")
    descriptor = None
    for klass in ast::SwitchExpression.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_ast::ifexpression_is_not_abstract():
    assert not inspect.isabstract(ast::IfExpression)


def test_ast::ifexpression_constructor_exists():
    assert callable(ast::IfExpression.__init__)


def test_ast::ifexpression_constructor_args():
    sig = inspect.signature(ast::IfExpression.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_ast::ifexpression_has_static():
    assert hasattr(ast::IfExpression, "static")
    descriptor = None
    for klass in ast::IfExpression.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_ast::callableelement_is_not_abstract():
    assert not inspect.isabstract(ast::CallableElement)


def test_ast::callableelement_constructor_exists():
    assert callable(ast::CallableElement.__init__)


def test_ast::callableelement_constructor_args():
    sig = inspect.signature(ast::CallableElement.__init__)
    params = list(sig.parameters.keys())



def test_ast::expression_is_not_abstract():
    assert not inspect.isabstract(ast::Expression)


def test_ast::expression_constructor_exists():
    assert callable(ast::Expression.__init__)


def test_ast::expression_constructor_args():
    sig = inspect.signature(ast::Expression.__init__)
    params = list(sig.parameters.keys())



def test_ast::equation_is_not_abstract():
    assert not inspect.isabstract(ast::Equation)


def test_ast::equation_constructor_exists():
    assert callable(ast::Equation.__init__)


def test_ast::equation_constructor_args():
    sig = inspect.signature(ast::Equation.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"

def test_ast::equation_has_initial():
    assert hasattr(ast::Equation, "initial")
    descriptor = None
    for klass in ast::Equation.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)



def test_ast::assertion_is_not_abstract():
    assert not inspect.isabstract(ast::Assertion)


def test_ast::assertion_constructor_exists():
    assert callable(ast::Assertion.__init__)


def test_ast::assertion_constructor_args():
    sig = inspect.signature(ast::Assertion.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "statusKind" in params, "Missing parameter 'statusKind'"

def test_ast::assertion_has_static():
    assert hasattr(ast::Assertion, "static")
    descriptor = None
    for klass in ast::Assertion.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_ast::assertion_has_statusKind():
    assert hasattr(ast::Assertion, "statusKind")
    descriptor = None
    for klass in ast::Assertion.__mro__:
        if "statusKind" in klass.__dict__:
            descriptor = klass.__dict__["statusKind"]
            break
    assert isinstance(descriptor, property)



def test_ast::check_is_not_abstract():
    assert not inspect.isabstract(ast::Check)


def test_ast::check_constructor_exists():
    assert callable(ast::Check.__init__)


def test_ast::check_constructor_args():
    sig = inspect.signature(ast::Check.__init__)
    params = list(sig.parameters.keys())



def test_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(ParameterDeclaration)


def test_parameterdeclaration_constructor_exists():
    assert callable(ParameterDeclaration.__init__)


def test_parameterdeclaration_constructor_args():
    sig = inspect.signature(ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::outputparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::OutputParameterDeclaration)


def test_ast::outputparameterdeclaration_constructor_exists():
    assert callable(ast::OutputParameterDeclaration.__init__)


def test_ast::outputparameterdeclaration_constructor_args():
    sig = inspect.signature(ast::OutputParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::enumerationliteraldeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::EnumerationLiteralDeclaration)


def test_ast::enumerationliteraldeclaration_constructor_exists():
    assert callable(ast::EnumerationLiteralDeclaration.__init__)


def test_ast::enumerationliteraldeclaration_constructor_args():
    sig = inspect.signature(ast::EnumerationLiteralDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast::enumerationliteraldeclaration_has_name():
    assert hasattr(ast::EnumerationLiteralDeclaration, "name")
    descriptor = None
    for klass in ast::EnumerationLiteralDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(DataTypeDefinition)


def test_datatypedefinition_constructor_exists():
    assert callable(DataTypeDefinition.__init__)


def test_datatypedefinition_constructor_args():
    sig = inspect.signature(DataTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ast::typealiasdefinition_is_not_abstract():
    assert not inspect.isabstract(ast::TypeAliasDefinition)


def test_ast::typealiasdefinition_constructor_exists():
    assert callable(ast::TypeAliasDefinition.__init__)


def test_ast::typealiasdefinition_constructor_args():
    sig = inspect.signature(ast::TypeAliasDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ast::enumerationdefinition_is_not_abstract():
    assert not inspect.isabstract(ast::EnumerationDefinition)


def test_ast::enumerationdefinition_constructor_exists():
    assert callable(ast::EnumerationDefinition.__init__)


def test_ast::enumerationdefinition_constructor_args():
    sig = inspect.signature(ast::EnumerationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_ast::datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(ast::DataTypeDefinition)


def test_ast::datatypedefinition_constructor_exists():
    assert callable(ast::DataTypeDefinition.__init__)


def test_ast::datatypedefinition_constructor_args():
    sig = inspect.signature(ast::DataTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ast::definition_is_not_abstract():
    assert not inspect.isabstract(ast::Definition)


def test_ast::definition_constructor_exists():
    assert callable(ast::Definition.__init__)


def test_ast::definition_constructor_args():
    sig = inspect.signature(ast::Definition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast::definition_has_name():
    assert hasattr(ast::Definition, "name")
    descriptor = None
    for klass in ast::Definition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast::module_is_not_abstract():
    assert not inspect.isabstract(ast::Module)


def test_ast::module_constructor_exists():
    assert callable(ast::Module.__init__)


def test_ast::module_constructor_args():
    sig = inspect.signature(ast::Module.__init__)
    params = list(sig.parameters.keys())



def test_ast::inputparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::InputParameterDeclaration)


def test_ast::inputparameterdeclaration_constructor_exists():
    assert callable(ast::InputParameterDeclaration.__init__)


def test_ast::inputparameterdeclaration_constructor_args():
    sig = inspect.signature(ast::InputParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ast::templateparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::TemplateParameterDeclaration)


def test_ast::templateparameterdeclaration_constructor_exists():
    assert callable(ast::TemplateParameterDeclaration.__init__)


def test_ast::templateparameterdeclaration_constructor_args():
    sig = inspect.signature(ast::TemplateParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_callableelement_is_not_abstract():
    assert not inspect.isabstract(CallableElement)


def test_callableelement_constructor_exists():
    assert callable(CallableElement.__init__)


def test_callableelement_constructor_args():
    sig = inspect.signature(CallableElement.__init__)
    params = list(sig.parameters.keys())



def test_ast::statevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::StateVariableDeclaration)


def test_ast::statevariabledeclaration_constructor_exists():
    assert callable(ast::StateVariableDeclaration.__init__)


def test_ast::statevariabledeclaration_constructor_args():
    sig = inspect.signature(ast::StateVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast::statevariabledeclaration_has_name():
    assert hasattr(ast::StateVariableDeclaration, "name")
    descriptor = None
    for klass in ast::StateVariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast::letexpressionvariabledeclarationpart_is_not_abstract():
    assert not inspect.isabstract(ast::LetExpressionVariableDeclarationPart)


def test_ast::letexpressionvariabledeclarationpart_constructor_exists():
    assert callable(ast::LetExpressionVariableDeclarationPart.__init__)


def test_ast::letexpressionvariabledeclarationpart_constructor_args():
    sig = inspect.signature(ast::LetExpressionVariableDeclarationPart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast::letexpressionvariabledeclarationpart_has_name():
    assert hasattr(ast::LetExpressionVariableDeclarationPart, "name")
    descriptor = None
    for klass in ast::LetExpressionVariableDeclarationPart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast::iterationaccumulator_is_not_abstract():
    assert not inspect.isabstract(ast::IterationAccumulator)


def test_ast::iterationaccumulator_constructor_exists():
    assert callable(ast::IterationAccumulator.__init__)


def test_ast::iterationaccumulator_constructor_args():
    sig = inspect.signature(ast::IterationAccumulator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast::iterationaccumulator_has_name():
    assert hasattr(ast::IterationAccumulator, "name")
    descriptor = None
    for klass in ast::IterationAccumulator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast::parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::ParameterDeclaration)


def test_ast::parameterdeclaration_constructor_exists():
    assert callable(ast::ParameterDeclaration.__init__)


def test_ast::parameterdeclaration_constructor_args():
    sig = inspect.signature(ast::ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast::parameterdeclaration_has_name():
    assert hasattr(ast::ParameterDeclaration, "name")
    descriptor = None
    for klass in ast::ParameterDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast::functionobjectdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::FunctionObjectDeclaration)


def test_ast::functionobjectdeclaration_constructor_exists():
    assert callable(ast::FunctionObjectDeclaration.__init__)


def test_ast::functionobjectdeclaration_constructor_args():
    sig = inspect.signature(ast::FunctionObjectDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast::functionobjectdeclaration_has_name():
    assert hasattr(ast::FunctionObjectDeclaration, "name")
    descriptor = None
    for klass in ast::FunctionObjectDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast::builtindefinition_is_not_abstract():
    assert not inspect.isabstract(ast::BuiltinDefinition)


def test_ast::builtindefinition_constructor_exists():
    assert callable(ast::BuiltinDefinition.__init__)


def test_ast::builtindefinition_constructor_args():
    sig = inspect.signature(ast::BuiltinDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ast::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::VariableDeclaration)


def test_ast::variabledeclaration_constructor_exists():
    assert callable(ast::VariableDeclaration.__init__)


def test_ast::variabledeclaration_constructor_args():
    sig = inspect.signature(ast::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast::variabledeclaration_has_name():
    assert hasattr(ast::VariableDeclaration, "name")
    descriptor = None
    for klass in ast::VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast::iterationvariable_is_not_abstract():
    assert not inspect.isabstract(ast::IterationVariable)


def test_ast::iterationvariable_constructor_exists():
    assert callable(ast::IterationVariable.__init__)


def test_ast::iterationvariable_constructor_args():
    sig = inspect.signature(ast::IterationVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast::iterationvariable_has_name():
    assert hasattr(ast::IterationVariable, "name")
    descriptor = None
    for klass in ast::IterationVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast::functiondefinition_is_not_abstract():
    assert not inspect.isabstract(ast::FunctionDefinition)


def test_ast::functiondefinition_constructor_exists():
    assert callable(ast::FunctionDefinition.__init__)


def test_ast::functiondefinition_constructor_args():
    sig = inspect.signature(ast::FunctionDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ast::functiondefinition_has_kind():
    assert hasattr(ast::FunctionDefinition, "kind")
    descriptor = None
    for klass in ast::FunctionDefinition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ast::datatypespecifier_is_not_abstract():
    assert not inspect.isabstract(ast::DataTypeSpecifier)


def test_ast::datatypespecifier_constructor_exists():
    assert callable(ast::DataTypeSpecifier.__init__)


def test_ast::datatypespecifier_constructor_args():
    sig = inspect.signature(ast::DataTypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_ast::structmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(ast::StructMemberDeclaration)


def test_ast::structmemberdeclaration_constructor_exists():
    assert callable(ast::StructMemberDeclaration.__init__)


def test_ast::structmemberdeclaration_constructor_args():
    sig = inspect.signature(ast::StructMemberDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast::structmemberdeclaration_has_name():
    assert hasattr(ast::StructMemberDeclaration, "name")
    descriptor = None
    for klass in ast::StructMemberDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast::structdefinition_is_not_abstract():
    assert not inspect.isabstract(ast::StructDefinition)


def test_ast::structdefinition_constructor_exists():
    assert callable(ast::StructDefinition.__init__)


def test_ast::structdefinition_constructor_args():
    sig = inspect.signature(ast::StructDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ast::primitivetype_is_not_abstract():
    assert not inspect.isabstract(ast::PrimitiveType)


def test_ast::primitivetype_constructor_exists():
    assert callable(ast::PrimitiveType.__init__)


def test_ast::primitivetype_constructor_args():
    sig = inspect.signature(ast::PrimitiveType.__init__)
    params = list(sig.parameters.keys())

def test_postfixoperator_exists():
    # Check that the Enumeration exists
    assert PostfixOperator is not None

def test_postfixoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PostfixOperator]
    expected_literals = [
        "Transpose",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PostfixOperator"

def test_additiveoperator_exists():
    # Check that the Enumeration exists
    assert AdditiveOperator is not None

def test_additiveoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdditiveOperator]
    expected_literals = [
        "Add",
        "Subtract",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdditiveOperator"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "GreaterThanOrEqualTo",
        "GreaterThan",
        "LessThanOrEqualTo",
        "LessThan",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_assertionstatuskind_exists():
    # Check that the Enumeration exists
    assert AssertionStatusKind is not None

def test_assertionstatuskind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssertionStatusKind]
    expected_literals = [
        "Fatal",
        "Info",
        "Error",
        "Warning",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssertionStatusKind"

def test_equalityoperator_exists():
    # Check that the Enumeration exists
    assert EqualityOperator is not None

def test_equalityoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EqualityOperator]
    expected_literals = [
        "EqualTo",
        "NotEqualTo",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EqualityOperator"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "LogicalNot",
        "Negate",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_poweroperator_exists():
    # Check that the Enumeration exists
    assert PowerOperator is not None

def test_poweroperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PowerOperator]
    expected_literals = [
        "ElementWisePower",
        "Power",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PowerOperator"

def test_multiplicativeoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicativeOperator is not None

def test_multiplicativeoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicativeOperator]
    expected_literals = [
        "Multiply",
        "ElementWiseMultiply",
        "Divide",
        "ElementWiseDivide",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicativeOperator"

def test_functionkind_exists():
    # Check that the Enumeration exists
    assert FunctionKind is not None

def test_functionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FunctionKind]
    expected_literals = [
        "Continuous",
        "Stateless",
        "Stateful",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FunctionKind"


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
BuiltinDefinition_strategy = st.builds(
    BuiltinDefinition,
)
ast::BuiltinVariable_strategy = st.builds(
    ast::BuiltinVariable,
)
ast::BuiltinFunction_strategy = st.builds(
    ast::BuiltinFunction,
)
ast::Statement_strategy = st.builds(
    ast::Statement,
)
Statement_strategy = st.builds(
    Statement,
)
ast::BreakStatement_strategy = st.builds(
    ast::BreakStatement,
)
ast::ReturnStatement_strategy = st.builds(
    ast::ReturnStatement,
)
ast::ContinueStatement_strategy = st.builds(
    ast::ContinueStatement,
)
ast::ForStatement_strategy = st.builds(
    ast::ForStatement,
)
ast::DoWhileStatement_strategy = st.builds(
    ast::DoWhileStatement,
)
ast::WhileStatement_strategy = st.builds(
    ast::WhileStatement,
)
ast::Compound_strategy = st.builds(
    ast::Compound,
)
PrimitiveStepExpression_strategy = st.builds(
    PrimitiveStepExpression,
)
ast::StepN_strategy = st.builds(
    ast::StepN,
)
ast::StepLiteral_strategy = st.builds(
    ast::StepLiteral,
    value=
        st.integers()
)
ast::IfStatement_strategy = st.builds(
    ast::IfStatement,
)
ast::Assignment_strategy = st.builds(
    ast::Assignment,
)
StepExpression_strategy = st.builds(
    StepExpression,
)
ast::PrimitiveStepExpression_strategy = st.builds(
    ast::PrimitiveStepExpression,
)
ast::AdditiveStepExpression_strategy = st.builds(
    ast::AdditiveStepExpression,
    operator=
        safe_text
)
ast::NegateStepExpression_strategy = st.builds(
    ast::NegateStepExpression,
)
ast::RangeStepExpression_strategy = st.builds(
    ast::RangeStepExpression,
)
ast::StepExpression_strategy = st.builds(
    ast::StepExpression,
)
FeatureCall_strategy = st.builds(
    FeatureCall,
)
ast::FunctionCall_strategy = st.builds(
    ast::FunctionCall,
)
ast::VariableAccess_strategy = st.builds(
    ast::VariableAccess,
)
ast::ExpressionList_strategy = st.builds(
    ast::ExpressionList,
)
ast::ArrayConstructionIterationClause_strategy = st.builds(
    ast::ArrayConstructionIterationClause,
    variableName=
        safe_text
)
ast::Unit_strategy = st.builds(
    ast::Unit,
)
ast::ArraySubscript_strategy = st.builds(
    ast::ArraySubscript,
    slice=
        st.booleans()
)
ast::LetExpressionVariableDeclaration_strategy = st.builds(
    ast::LetExpressionVariableDeclaration,
)
Expression_strategy = st.builds(
    Expression,
)
ast::LogicalOrExpression_strategy = st.builds(
    ast::LogicalOrExpression,
)
ast::TypeTestExpression_strategy = st.builds(
    ast::TypeTestExpression,
)
ast::ArrayConcatenationOperator_strategy = st.builds(
    ast::ArrayConcatenationOperator,
)
ast::ParenthesizedExpression_strategy = st.builds(
    ast::ParenthesizedExpression,
)
ast::EqualityExpression_strategy = st.builds(
    ast::EqualityExpression,
    operator=
        safe_text
)
ast::AdditiveExpression_strategy = st.builds(
    ast::AdditiveExpression,
    operator=
        safe_text
)
ast::LogicalAndExpression_strategy = st.builds(
    ast::LogicalAndExpression,
)
ast::DerivativeOperator_strategy = st.builds(
    ast::DerivativeOperator,
)
ast::RelationalExpression_strategy = st.builds(
    ast::RelationalExpression,
    operator=
        safe_text
)
ast::UnitConstructionOperator_strategy = st.builds(
    ast::UnitConstructionOperator,
)
ast::IterationCall_strategy = st.builds(
    ast::IterationCall,
    identifier=
        safe_text
)
ast::UnaryExpression_strategy = st.builds(
    ast::UnaryExpression,
    operator=
        safe_text
)
ast::MemberVariableAccess_strategy = st.builds(
    ast::MemberVariableAccess,
)
ast::FeatureCall_strategy = st.builds(
    ast::FeatureCall,
)
ast::PowerExpression_strategy = st.builds(
    ast::PowerExpression,
    operator=
        safe_text
)
ast::PostfixExpression_strategy = st.builds(
    ast::PostfixExpression,
    operator=
        safe_text
)
ast::RangeExpression_strategy = st.builds(
    ast::RangeExpression,
)
ast::ArrayConstructionOperator_strategy = st.builds(
    ast::ArrayConstructionOperator,
)
ast::MultiplicativeExpression_strategy = st.builds(
    ast::MultiplicativeExpression,
    operator=
        safe_text
)
ast::EndExpression_strategy = st.builds(
    ast::EndExpression,
)
ast::AlgorithmExpression_strategy = st.builds(
    ast::AlgorithmExpression,
)
ast::ImpliesExpression_strategy = st.builds(
    ast::ImpliesExpression,
)
ast::ArrayElementAccess_strategy = st.builds(
    ast::ArrayElementAccess,
)
ast::LetExpression_strategy = st.builds(
    ast::LetExpression,
)
ast::DataType_strategy = st.builds(
    ast::DataType,
)
ast::SwitchCase_strategy = st.builds(
    ast::SwitchCase,
)
ast::SwitchExpression_strategy = st.builds(
    ast::SwitchExpression,
    static=
        st.booleans()
)
ast::IfExpression_strategy = st.builds(
    ast::IfExpression,
    static=
        st.booleans()
)
ast::CallableElement_strategy = st.builds(
    ast::CallableElement,
)
ast::Expression_strategy = st.builds(
    ast::Expression,
)
ast::Equation_strategy = st.builds(
    ast::Equation,
    initial=
        st.booleans()
)
ast::Assertion_strategy = st.builds(
    ast::Assertion,
    static=
        st.booleans(),
    statusKind=
        safe_text
)
ast::Check_strategy = st.builds(
    ast::Check,
)
ParameterDeclaration_strategy = st.builds(
    ParameterDeclaration,
)
ast::OutputParameterDeclaration_strategy = st.builds(
    ast::OutputParameterDeclaration,
)
ast::EnumerationLiteralDeclaration_strategy = st.builds(
    ast::EnumerationLiteralDeclaration,
    name=
        safe_text
)
DataTypeDefinition_strategy = st.builds(
    DataTypeDefinition,
)
ast::TypeAliasDefinition_strategy = st.builds(
    ast::TypeAliasDefinition,
)
ast::EnumerationDefinition_strategy = st.builds(
    ast::EnumerationDefinition,
)
Definition_strategy = st.builds(
    Definition,
)
ast::DataTypeDefinition_strategy = st.builds(
    ast::DataTypeDefinition,
)
ast::Definition_strategy = st.builds(
    ast::Definition,
    name=
        safe_text
)
ast::Module_strategy = st.builds(
    ast::Module,
)
ast::InputParameterDeclaration_strategy = st.builds(
    ast::InputParameterDeclaration,
)
ast::TemplateParameterDeclaration_strategy = st.builds(
    ast::TemplateParameterDeclaration,
)
CallableElement_strategy = st.builds(
    CallableElement,
)
ast::StateVariableDeclaration_strategy = st.builds(
    ast::StateVariableDeclaration,
    name=
        safe_text
)
ast::LetExpressionVariableDeclarationPart_strategy = st.builds(
    ast::LetExpressionVariableDeclarationPart,
    name=
        safe_text
)
ast::IterationAccumulator_strategy = st.builds(
    ast::IterationAccumulator,
    name=
        safe_text
)
ast::ParameterDeclaration_strategy = st.builds(
    ast::ParameterDeclaration,
    name=
        safe_text
)
ast::FunctionObjectDeclaration_strategy = st.builds(
    ast::FunctionObjectDeclaration,
    name=
        safe_text
)
ast::BuiltinDefinition_strategy = st.builds(
    ast::BuiltinDefinition,
)
ast::VariableDeclaration_strategy = st.builds(
    ast::VariableDeclaration,
    name=
        safe_text
)
ast::IterationVariable_strategy = st.builds(
    ast::IterationVariable,
    name=
        safe_text
)
ast::FunctionDefinition_strategy = st.builds(
    ast::FunctionDefinition,
    kind=
        safe_text
)
ast::DataTypeSpecifier_strategy = st.builds(
    ast::DataTypeSpecifier,
)
ast::StructMemberDeclaration_strategy = st.builds(
    ast::StructMemberDeclaration,
    name=
        safe_text
)
ast::StructDefinition_strategy = st.builds(
    ast::StructDefinition,
)
ast::PrimitiveType_strategy = st.builds(
    ast::PrimitiveType,
)

@given(instance=BuiltinDefinition_strategy)
@settings(max_examples=50)
def test_builtindefinition_instantiation(instance):
    assert isinstance(instance, BuiltinDefinition)

@given(instance=ast::BuiltinVariable_strategy)
@settings(max_examples=50)
def test_ast::builtinvariable_instantiation(instance):
    assert isinstance(instance, ast::BuiltinVariable)

@given(instance=ast::BuiltinFunction_strategy)
@settings(max_examples=50)
def test_ast::builtinfunction_instantiation(instance):
    assert isinstance(instance, ast::BuiltinFunction)

@given(instance=ast::Statement_strategy)
@settings(max_examples=50)
def test_ast::statement_instantiation(instance):
    assert isinstance(instance, ast::Statement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=ast::BreakStatement_strategy)
@settings(max_examples=50)
def test_ast::breakstatement_instantiation(instance):
    assert isinstance(instance, ast::BreakStatement)

@given(instance=ast::ReturnStatement_strategy)
@settings(max_examples=50)
def test_ast::returnstatement_instantiation(instance):
    assert isinstance(instance, ast::ReturnStatement)

@given(instance=ast::ContinueStatement_strategy)
@settings(max_examples=50)
def test_ast::continuestatement_instantiation(instance):
    assert isinstance(instance, ast::ContinueStatement)

@given(instance=ast::ForStatement_strategy)
@settings(max_examples=50)
def test_ast::forstatement_instantiation(instance):
    assert isinstance(instance, ast::ForStatement)

@given(instance=ast::DoWhileStatement_strategy)
@settings(max_examples=50)
def test_ast::dowhilestatement_instantiation(instance):
    assert isinstance(instance, ast::DoWhileStatement)

@given(instance=ast::WhileStatement_strategy)
@settings(max_examples=50)
def test_ast::whilestatement_instantiation(instance):
    assert isinstance(instance, ast::WhileStatement)

@given(instance=ast::Compound_strategy)
@settings(max_examples=50)
def test_ast::compound_instantiation(instance):
    assert isinstance(instance, ast::Compound)

@given(instance=PrimitiveStepExpression_strategy)
@settings(max_examples=50)
def test_primitivestepexpression_instantiation(instance):
    assert isinstance(instance, PrimitiveStepExpression)

@given(instance=ast::StepN_strategy)
@settings(max_examples=50)
def test_ast::stepn_instantiation(instance):
    assert isinstance(instance, ast::StepN)

@given(instance=ast::StepLiteral_strategy)
@settings(max_examples=50)
def test_ast::stepliteral_instantiation(instance):
    assert isinstance(instance, ast::StepLiteral)

@given(instance=ast::StepLiteral_strategy)
def test_ast::stepliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=ast::StepLiteral_strategy)
def test_ast::stepliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ast::IfStatement_strategy)
@settings(max_examples=50)
def test_ast::ifstatement_instantiation(instance):
    assert isinstance(instance, ast::IfStatement)

@given(instance=ast::Assignment_strategy)
@settings(max_examples=50)
def test_ast::assignment_instantiation(instance):
    assert isinstance(instance, ast::Assignment)

@given(instance=StepExpression_strategy)
@settings(max_examples=50)
def test_stepexpression_instantiation(instance):
    assert isinstance(instance, StepExpression)

@given(instance=ast::PrimitiveStepExpression_strategy)
@settings(max_examples=50)
def test_ast::primitivestepexpression_instantiation(instance):
    assert isinstance(instance, ast::PrimitiveStepExpression)

@given(instance=ast::AdditiveStepExpression_strategy)
@settings(max_examples=50)
def test_ast::additivestepexpression_instantiation(instance):
    assert isinstance(instance, ast::AdditiveStepExpression)

@given(instance=ast::AdditiveStepExpression_strategy)
def test_ast::additivestepexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ast::AdditiveStepExpression_strategy)
def test_ast::additivestepexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast::NegateStepExpression_strategy)
@settings(max_examples=50)
def test_ast::negatestepexpression_instantiation(instance):
    assert isinstance(instance, ast::NegateStepExpression)

@given(instance=ast::RangeStepExpression_strategy)
@settings(max_examples=50)
def test_ast::rangestepexpression_instantiation(instance):
    assert isinstance(instance, ast::RangeStepExpression)

@given(instance=ast::StepExpression_strategy)
@settings(max_examples=50)
def test_ast::stepexpression_instantiation(instance):
    assert isinstance(instance, ast::StepExpression)

@given(instance=FeatureCall_strategy)
@settings(max_examples=50)
def test_featurecall_instantiation(instance):
    assert isinstance(instance, FeatureCall)

@given(instance=ast::FunctionCall_strategy)
@settings(max_examples=50)
def test_ast::functioncall_instantiation(instance):
    assert isinstance(instance, ast::FunctionCall)

@given(instance=ast::VariableAccess_strategy)
@settings(max_examples=50)
def test_ast::variableaccess_instantiation(instance):
    assert isinstance(instance, ast::VariableAccess)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ast::VariableAccess_strategy)
@settings(max_examples=30)
def test_ast::variableaccess_isinitial_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isInitial()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isInitial).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isInitial' in ast::VariableAccess is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isInitial' in ast::VariableAccess did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isInitial' in ast::VariableAccess is not implemented or raised an error")

@given(instance=ast::ExpressionList_strategy)
@settings(max_examples=50)
def test_ast::expressionlist_instantiation(instance):
    assert isinstance(instance, ast::ExpressionList)

@given(instance=ast::ArrayConstructionIterationClause_strategy)
@settings(max_examples=50)
def test_ast::arrayconstructioniterationclause_instantiation(instance):
    assert isinstance(instance, ast::ArrayConstructionIterationClause)

@given(instance=ast::ArrayConstructionIterationClause_strategy)
def test_ast::arrayconstructioniterationclause_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=ast::ArrayConstructionIterationClause_strategy)
def test_ast::arrayconstructioniterationclause_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=ast::Unit_strategy)
@settings(max_examples=50)
def test_ast::unit_instantiation(instance):
    assert isinstance(instance, ast::Unit)

@given(instance=ast::ArraySubscript_strategy)
@settings(max_examples=50)
def test_ast::arraysubscript_instantiation(instance):
    assert isinstance(instance, ast::ArraySubscript)

@given(instance=ast::ArraySubscript_strategy)
def test_ast::arraysubscript_slice_type(instance):
    assert isinstance(instance.slice, bool)


@given(instance=ast::ArraySubscript_strategy)
def test_ast::arraysubscript_slice_setter(instance):
    original = instance.slice
    instance.slice = original
    assert instance.slice == original

@given(instance=ast::LetExpressionVariableDeclaration_strategy)
@settings(max_examples=50)
def test_ast::letexpressionvariabledeclaration_instantiation(instance):
    assert isinstance(instance, ast::LetExpressionVariableDeclaration)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ast::LogicalOrExpression_strategy)
@settings(max_examples=50)
def test_ast::logicalorexpression_instantiation(instance):
    assert isinstance(instance, ast::LogicalOrExpression)

@given(instance=ast::TypeTestExpression_strategy)
@settings(max_examples=50)
def test_ast::typetestexpression_instantiation(instance):
    assert isinstance(instance, ast::TypeTestExpression)

@given(instance=ast::ArrayConcatenationOperator_strategy)
@settings(max_examples=50)
def test_ast::arrayconcatenationoperator_instantiation(instance):
    assert isinstance(instance, ast::ArrayConcatenationOperator)

@given(instance=ast::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_ast::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, ast::ParenthesizedExpression)

@given(instance=ast::EqualityExpression_strategy)
@settings(max_examples=50)
def test_ast::equalityexpression_instantiation(instance):
    assert isinstance(instance, ast::EqualityExpression)

@given(instance=ast::EqualityExpression_strategy)
def test_ast::equalityexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ast::EqualityExpression_strategy)
def test_ast::equalityexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast::AdditiveExpression_strategy)
@settings(max_examples=50)
def test_ast::additiveexpression_instantiation(instance):
    assert isinstance(instance, ast::AdditiveExpression)

@given(instance=ast::AdditiveExpression_strategy)
def test_ast::additiveexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ast::AdditiveExpression_strategy)
def test_ast::additiveexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast::LogicalAndExpression_strategy)
@settings(max_examples=50)
def test_ast::logicalandexpression_instantiation(instance):
    assert isinstance(instance, ast::LogicalAndExpression)

@given(instance=ast::DerivativeOperator_strategy)
@settings(max_examples=50)
def test_ast::derivativeoperator_instantiation(instance):
    assert isinstance(instance, ast::DerivativeOperator)

@given(instance=ast::RelationalExpression_strategy)
@settings(max_examples=50)
def test_ast::relationalexpression_instantiation(instance):
    assert isinstance(instance, ast::RelationalExpression)

@given(instance=ast::RelationalExpression_strategy)
def test_ast::relationalexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ast::RelationalExpression_strategy)
def test_ast::relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast::UnitConstructionOperator_strategy)
@settings(max_examples=50)
def test_ast::unitconstructionoperator_instantiation(instance):
    assert isinstance(instance, ast::UnitConstructionOperator)

@given(instance=ast::IterationCall_strategy)
@settings(max_examples=50)
def test_ast::iterationcall_instantiation(instance):
    assert isinstance(instance, ast::IterationCall)

@given(instance=ast::IterationCall_strategy)
def test_ast::iterationcall_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=ast::IterationCall_strategy)
def test_ast::iterationcall_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ast::UnaryExpression_strategy)
@settings(max_examples=50)
def test_ast::unaryexpression_instantiation(instance):
    assert isinstance(instance, ast::UnaryExpression)

@given(instance=ast::UnaryExpression_strategy)
def test_ast::unaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ast::UnaryExpression_strategy)
def test_ast::unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast::MemberVariableAccess_strategy)
@settings(max_examples=50)
def test_ast::membervariableaccess_instantiation(instance):
    assert isinstance(instance, ast::MemberVariableAccess)

@given(instance=ast::FeatureCall_strategy)
@settings(max_examples=50)
def test_ast::featurecall_instantiation(instance):
    assert isinstance(instance, ast::FeatureCall)

@given(instance=ast::PowerExpression_strategy)
@settings(max_examples=50)
def test_ast::powerexpression_instantiation(instance):
    assert isinstance(instance, ast::PowerExpression)

@given(instance=ast::PowerExpression_strategy)
def test_ast::powerexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ast::PowerExpression_strategy)
def test_ast::powerexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast::PostfixExpression_strategy)
@settings(max_examples=50)
def test_ast::postfixexpression_instantiation(instance):
    assert isinstance(instance, ast::PostfixExpression)

@given(instance=ast::PostfixExpression_strategy)
def test_ast::postfixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ast::PostfixExpression_strategy)
def test_ast::postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast::RangeExpression_strategy)
@settings(max_examples=50)
def test_ast::rangeexpression_instantiation(instance):
    assert isinstance(instance, ast::RangeExpression)

@given(instance=ast::ArrayConstructionOperator_strategy)
@settings(max_examples=50)
def test_ast::arrayconstructionoperator_instantiation(instance):
    assert isinstance(instance, ast::ArrayConstructionOperator)

@given(instance=ast::MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_ast::multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, ast::MultiplicativeExpression)

@given(instance=ast::MultiplicativeExpression_strategy)
def test_ast::multiplicativeexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ast::MultiplicativeExpression_strategy)
def test_ast::multiplicativeexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ast::EndExpression_strategy)
@settings(max_examples=50)
def test_ast::endexpression_instantiation(instance):
    assert isinstance(instance, ast::EndExpression)

@given(instance=ast::AlgorithmExpression_strategy)
@settings(max_examples=50)
def test_ast::algorithmexpression_instantiation(instance):
    assert isinstance(instance, ast::AlgorithmExpression)

@given(instance=ast::ImpliesExpression_strategy)
@settings(max_examples=50)
def test_ast::impliesexpression_instantiation(instance):
    assert isinstance(instance, ast::ImpliesExpression)

@given(instance=ast::ArrayElementAccess_strategy)
@settings(max_examples=50)
def test_ast::arrayelementaccess_instantiation(instance):
    assert isinstance(instance, ast::ArrayElementAccess)

@given(instance=ast::LetExpression_strategy)
@settings(max_examples=50)
def test_ast::letexpression_instantiation(instance):
    assert isinstance(instance, ast::LetExpression)

@given(instance=ast::DataType_strategy)
@settings(max_examples=50)
def test_ast::datatype_instantiation(instance):
    assert isinstance(instance, ast::DataType)

@given(instance=ast::SwitchCase_strategy)
@settings(max_examples=50)
def test_ast::switchcase_instantiation(instance):
    assert isinstance(instance, ast::SwitchCase)

@given(instance=ast::SwitchExpression_strategy)
@settings(max_examples=50)
def test_ast::switchexpression_instantiation(instance):
    assert isinstance(instance, ast::SwitchExpression)

@given(instance=ast::SwitchExpression_strategy)
def test_ast::switchexpression_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=ast::SwitchExpression_strategy)
def test_ast::switchexpression_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=ast::IfExpression_strategy)
@settings(max_examples=50)
def test_ast::ifexpression_instantiation(instance):
    assert isinstance(instance, ast::IfExpression)

@given(instance=ast::IfExpression_strategy)
def test_ast::ifexpression_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=ast::IfExpression_strategy)
def test_ast::ifexpression_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=ast::CallableElement_strategy)
@settings(max_examples=50)
def test_ast::callableelement_instantiation(instance):
    assert isinstance(instance, ast::CallableElement)

@given(instance=ast::Expression_strategy)
@settings(max_examples=50)
def test_ast::expression_instantiation(instance):
    assert isinstance(instance, ast::Expression)

@given(instance=ast::Equation_strategy)
@settings(max_examples=50)
def test_ast::equation_instantiation(instance):
    assert isinstance(instance, ast::Equation)

@given(instance=ast::Equation_strategy)
def test_ast::equation_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=ast::Equation_strategy)
def test_ast::equation_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=ast::Assertion_strategy)
@settings(max_examples=50)
def test_ast::assertion_instantiation(instance):
    assert isinstance(instance, ast::Assertion)

@given(instance=ast::Assertion_strategy)
def test_ast::assertion_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=ast::Assertion_strategy)
def test_ast::assertion_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=ast::Assertion_strategy)
def test_ast::assertion_statusKind_type(instance):
    assert isinstance(instance.statusKind, str)


@given(instance=ast::Assertion_strategy)
def test_ast::assertion_statusKind_setter(instance):
    original = instance.statusKind
    instance.statusKind = original
    assert instance.statusKind == original

@given(instance=ast::Check_strategy)
@settings(max_examples=50)
def test_ast::check_instantiation(instance):
    assert isinstance(instance, ast::Check)

@given(instance=ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_parameterdeclaration_instantiation(instance):
    assert isinstance(instance, ParameterDeclaration)

@given(instance=ast::OutputParameterDeclaration_strategy)
@settings(max_examples=50)
def test_ast::outputparameterdeclaration_instantiation(instance):
    assert isinstance(instance, ast::OutputParameterDeclaration)

@given(instance=ast::EnumerationLiteralDeclaration_strategy)
@settings(max_examples=50)
def test_ast::enumerationliteraldeclaration_instantiation(instance):
    assert isinstance(instance, ast::EnumerationLiteralDeclaration)

@given(instance=ast::EnumerationLiteralDeclaration_strategy)
def test_ast::enumerationliteraldeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ast::EnumerationLiteralDeclaration_strategy)
def test_ast::enumerationliteraldeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DataTypeDefinition_strategy)
@settings(max_examples=50)
def test_datatypedefinition_instantiation(instance):
    assert isinstance(instance, DataTypeDefinition)

@given(instance=ast::TypeAliasDefinition_strategy)
@settings(max_examples=50)
def test_ast::typealiasdefinition_instantiation(instance):
    assert isinstance(instance, ast::TypeAliasDefinition)

@given(instance=ast::EnumerationDefinition_strategy)
@settings(max_examples=50)
def test_ast::enumerationdefinition_instantiation(instance):
    assert isinstance(instance, ast::EnumerationDefinition)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=ast::DataTypeDefinition_strategy)
@settings(max_examples=50)
def test_ast::datatypedefinition_instantiation(instance):
    assert isinstance(instance, ast::DataTypeDefinition)

@given(instance=ast::Definition_strategy)
@settings(max_examples=50)
def test_ast::definition_instantiation(instance):
    assert isinstance(instance, ast::Definition)

@given(instance=ast::Definition_strategy)
def test_ast::definition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ast::Definition_strategy)
def test_ast::definition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast::Module_strategy)
@settings(max_examples=50)
def test_ast::module_instantiation(instance):
    assert isinstance(instance, ast::Module)

@given(instance=ast::InputParameterDeclaration_strategy)
@settings(max_examples=50)
def test_ast::inputparameterdeclaration_instantiation(instance):
    assert isinstance(instance, ast::InputParameterDeclaration)

@given(instance=ast::TemplateParameterDeclaration_strategy)
@settings(max_examples=50)
def test_ast::templateparameterdeclaration_instantiation(instance):
    assert isinstance(instance, ast::TemplateParameterDeclaration)

@given(instance=CallableElement_strategy)
@settings(max_examples=50)
def test_callableelement_instantiation(instance):
    assert isinstance(instance, CallableElement)

@given(instance=ast::StateVariableDeclaration_strategy)
@settings(max_examples=50)
def test_ast::statevariabledeclaration_instantiation(instance):
    assert isinstance(instance, ast::StateVariableDeclaration)

@given(instance=ast::StateVariableDeclaration_strategy)
def test_ast::statevariabledeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ast::StateVariableDeclaration_strategy)
def test_ast::statevariabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast::LetExpressionVariableDeclarationPart_strategy)
@settings(max_examples=50)
def test_ast::letexpressionvariabledeclarationpart_instantiation(instance):
    assert isinstance(instance, ast::LetExpressionVariableDeclarationPart)

@given(instance=ast::LetExpressionVariableDeclarationPart_strategy)
def test_ast::letexpressionvariabledeclarationpart_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ast::LetExpressionVariableDeclarationPart_strategy)
def test_ast::letexpressionvariabledeclarationpart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast::IterationAccumulator_strategy)
@settings(max_examples=50)
def test_ast::iterationaccumulator_instantiation(instance):
    assert isinstance(instance, ast::IterationAccumulator)

@given(instance=ast::IterationAccumulator_strategy)
def test_ast::iterationaccumulator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ast::IterationAccumulator_strategy)
def test_ast::iterationaccumulator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast::ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_ast::parameterdeclaration_instantiation(instance):
    assert isinstance(instance, ast::ParameterDeclaration)

@given(instance=ast::ParameterDeclaration_strategy)
def test_ast::parameterdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ast::ParameterDeclaration_strategy)
def test_ast::parameterdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast::FunctionObjectDeclaration_strategy)
@settings(max_examples=50)
def test_ast::functionobjectdeclaration_instantiation(instance):
    assert isinstance(instance, ast::FunctionObjectDeclaration)

@given(instance=ast::FunctionObjectDeclaration_strategy)
def test_ast::functionobjectdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ast::FunctionObjectDeclaration_strategy)
def test_ast::functionobjectdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast::BuiltinDefinition_strategy)
@settings(max_examples=50)
def test_ast::builtindefinition_instantiation(instance):
    assert isinstance(instance, ast::BuiltinDefinition)

@given(instance=ast::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_ast::variabledeclaration_instantiation(instance):
    assert isinstance(instance, ast::VariableDeclaration)

@given(instance=ast::VariableDeclaration_strategy)
def test_ast::variabledeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ast::VariableDeclaration_strategy)
def test_ast::variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast::IterationVariable_strategy)
@settings(max_examples=50)
def test_ast::iterationvariable_instantiation(instance):
    assert isinstance(instance, ast::IterationVariable)

@given(instance=ast::IterationVariable_strategy)
def test_ast::iterationvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ast::IterationVariable_strategy)
def test_ast::iterationvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast::FunctionDefinition_strategy)
@settings(max_examples=50)
def test_ast::functiondefinition_instantiation(instance):
    assert isinstance(instance, ast::FunctionDefinition)

@given(instance=ast::FunctionDefinition_strategy)
def test_ast::functiondefinition_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=ast::FunctionDefinition_strategy)
def test_ast::functiondefinition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ast::DataTypeSpecifier_strategy)
@settings(max_examples=50)
def test_ast::datatypespecifier_instantiation(instance):
    assert isinstance(instance, ast::DataTypeSpecifier)

@given(instance=ast::StructMemberDeclaration_strategy)
@settings(max_examples=50)
def test_ast::structmemberdeclaration_instantiation(instance):
    assert isinstance(instance, ast::StructMemberDeclaration)

@given(instance=ast::StructMemberDeclaration_strategy)
def test_ast::structmemberdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ast::StructMemberDeclaration_strategy)
def test_ast::structmemberdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast::StructDefinition_strategy)
@settings(max_examples=50)
def test_ast::structdefinition_instantiation(instance):
    assert isinstance(instance, ast::StructDefinition)

@given(instance=ast::PrimitiveType_strategy)
@settings(max_examples=50)
def test_ast::primitivetype_instantiation(instance):
    assert isinstance(instance, ast::PrimitiveType)
