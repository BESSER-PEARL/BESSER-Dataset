import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TextExpression,
    pp1::ExpressionTE,
    pp1::VariableTE,
    pp1::VerbatimTE,
    Lambda,
    pp1::RubyLambda,
    pp1::JavaLambda,
    pp1::TextExpression,
    IQuotedString,
    StringExpression,
    pp1::SingleQuotedString,
    pp1::UnquotedString,
    pp1::DoubleQuotedString,
    IfExpression,
    pp1::ElseIfExpression,
    WithLambdaExpression,
    pp1::MethodCall,
    pp1::FunctionCall,
    ParameterizedExpression,
    pp1::WithLambdaExpression,
    pp1::SelectorExpression,
    pp1::AtExpression,
    BinaryExpression,
    pp1::OrExpression,
    pp1::AndExpression,
    pp1::SelectorEntry,
    pp1::NamedAccessExpression,
    pp1::BinaryOpExpression,
    pp1::AppendExpression,
    pp1::AssignmentExpression,
    pp1::Case,
    BinaryOpExpression,
    pp1::AdditiveExpression,
    pp1::EqualityExpression,
    pp1::InExpression,
    pp1::ShiftExpression,
    pp1::MatchingExpression,
    pp1::MultiplicativeExpression,
    pp1::RelationalExpression,
    pp1::RelationshipExpression,
    Expression,
    pp1::VariableExpression,
    pp1::ExpressionBlock,
    pp1::ExprList,
    pp1::UnlessExpression,
    pp1::ParameterizedExpression,
    pp1::ParenthesisedExpression,
    pp1::SeparatorExpression,
    pp1::BinaryExpression,
    pp1::NodeDefinition,
    pp1::InterpolatedVariable,
    pp1::UnaryExpression,
    pp1::StringExpression,
    pp1::CaseExpression,
    pp1::CollectExpression,
    pp1::Definition,
    pp1::LiteralExpression,
    Definition,
    pp1::HostClassDefinition,
    ICollectQuery,
    UnaryExpression,
    pp1::ExportedCollectQuery,
    pp1::UnaryNotExpression,
    pp1::UnaryMinusExpression,
    pp1::VirtualCollectQuery,
    pp1::ICollectQuery,
    pp1::AttributeOperation,
    pp1::AttributeOperations,
    pp1::ResourceBody,
    pp1::Expression,
    ExpressionBlock,
    pp1::Lambda,
    pp1::ElseExpression,
    pp1::PuppetManifest,
    pp1::HashEntry,
    pp1::IQuotedString,
    pp1::ImportExpression,
    pp1::ResourceExpression,
    LiteralExpression,
    pp1::LiteralRegex,
    pp1::LiteralHash,
    pp1::LiteralName,
    pp1::LiteralList,
    pp1::LiteralDefault,
    pp1::LiteralUndef,
    pp1::VirtualNameOrReference,
    pp1::LiteralClass,
    pp1::LiteralBoolean,
    pp1::LiteralNameOrReference,
    pp1::IfExpression,
    pp1::DefinitionArgument,
    pp1::DefinitionArgumentList,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_textexpression_is_not_abstract():
    assert not inspect.isabstract(TextExpression)


def test_textexpression_constructor_exists():
    assert callable(TextExpression.__init__)


def test_textexpression_constructor_args():
    sig = inspect.signature(TextExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::expressionte_is_not_abstract():
    assert not inspect.isabstract(pp1::ExpressionTE)


def test_pp1::expressionte_constructor_exists():
    assert callable(pp1::ExpressionTE.__init__)


def test_pp1::expressionte_constructor_args():
    sig = inspect.signature(pp1::ExpressionTE.__init__)
    params = list(sig.parameters.keys())



def test_pp1::variablete_is_not_abstract():
    assert not inspect.isabstract(pp1::VariableTE)


def test_pp1::variablete_constructor_exists():
    assert callable(pp1::VariableTE.__init__)


def test_pp1::variablete_constructor_args():
    sig = inspect.signature(pp1::VariableTE.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_pp1::variablete_has_varName():
    assert hasattr(pp1::VariableTE, "varName")
    descriptor = None
    for klass in pp1::VariableTE.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_pp1::verbatimte_is_not_abstract():
    assert not inspect.isabstract(pp1::VerbatimTE)


def test_pp1::verbatimte_constructor_exists():
    assert callable(pp1::VerbatimTE.__init__)


def test_pp1::verbatimte_constructor_args():
    sig = inspect.signature(pp1::VerbatimTE.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_pp1::verbatimte_has_text():
    assert hasattr(pp1::VerbatimTE, "text")
    descriptor = None
    for klass in pp1::VerbatimTE.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_lambda_is_not_abstract():
    assert not inspect.isabstract(Lambda)


def test_lambda_constructor_exists():
    assert callable(Lambda.__init__)


def test_lambda_constructor_args():
    sig = inspect.signature(Lambda.__init__)
    params = list(sig.parameters.keys())



def test_pp1::rubylambda_is_not_abstract():
    assert not inspect.isabstract(pp1::RubyLambda)


def test_pp1::rubylambda_constructor_exists():
    assert callable(pp1::RubyLambda.__init__)


def test_pp1::rubylambda_constructor_args():
    sig = inspect.signature(pp1::RubyLambda.__init__)
    params = list(sig.parameters.keys())



def test_pp1::javalambda_is_not_abstract():
    assert not inspect.isabstract(pp1::JavaLambda)


def test_pp1::javalambda_constructor_exists():
    assert callable(pp1::JavaLambda.__init__)


def test_pp1::javalambda_constructor_args():
    sig = inspect.signature(pp1::JavaLambda.__init__)
    params = list(sig.parameters.keys())
    assert "farrow" in params, "Missing parameter 'farrow'"

def test_pp1::javalambda_has_farrow():
    assert hasattr(pp1::JavaLambda, "farrow")
    descriptor = None
    for klass in pp1::JavaLambda.__mro__:
        if "farrow" in klass.__dict__:
            descriptor = klass.__dict__["farrow"]
            break
    assert isinstance(descriptor, property)



def test_pp1::textexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::TextExpression)


def test_pp1::textexpression_constructor_exists():
    assert callable(pp1::TextExpression.__init__)


def test_pp1::textexpression_constructor_args():
    sig = inspect.signature(pp1::TextExpression.__init__)
    params = list(sig.parameters.keys())



def test_iquotedstring_is_not_abstract():
    assert not inspect.isabstract(IQuotedString)


def test_iquotedstring_constructor_exists():
    assert callable(IQuotedString.__init__)


def test_iquotedstring_constructor_args():
    sig = inspect.signature(IQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_stringexpression_is_not_abstract():
    assert not inspect.isabstract(StringExpression)


def test_stringexpression_constructor_exists():
    assert callable(StringExpression.__init__)


def test_stringexpression_constructor_args():
    sig = inspect.signature(StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::singlequotedstring_is_not_abstract():
    assert not inspect.isabstract(pp1::SingleQuotedString)


def test_pp1::singlequotedstring_constructor_exists():
    assert callable(pp1::SingleQuotedString.__init__)


def test_pp1::singlequotedstring_constructor_args():
    sig = inspect.signature(pp1::SingleQuotedString.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_pp1::singlequotedstring_has_text():
    assert hasattr(pp1::SingleQuotedString, "text")
    descriptor = None
    for klass in pp1::SingleQuotedString.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_pp1::unquotedstring_is_not_abstract():
    assert not inspect.isabstract(pp1::UnquotedString)


def test_pp1::unquotedstring_constructor_exists():
    assert callable(pp1::UnquotedString.__init__)


def test_pp1::unquotedstring_constructor_args():
    sig = inspect.signature(pp1::UnquotedString.__init__)
    params = list(sig.parameters.keys())



def test_pp1::doublequotedstring_is_not_abstract():
    assert not inspect.isabstract(pp1::DoubleQuotedString)


def test_pp1::doublequotedstring_constructor_exists():
    assert callable(pp1::DoubleQuotedString.__init__)


def test_pp1::doublequotedstring_constructor_args():
    sig = inspect.signature(pp1::DoubleQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_ifexpression_is_not_abstract():
    assert not inspect.isabstract(IfExpression)


def test_ifexpression_constructor_exists():
    assert callable(IfExpression.__init__)


def test_ifexpression_constructor_args():
    sig = inspect.signature(IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::elseifexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::ElseIfExpression)


def test_pp1::elseifexpression_constructor_exists():
    assert callable(pp1::ElseIfExpression.__init__)


def test_pp1::elseifexpression_constructor_args():
    sig = inspect.signature(pp1::ElseIfExpression.__init__)
    params = list(sig.parameters.keys())



def test_withlambdaexpression_is_not_abstract():
    assert not inspect.isabstract(WithLambdaExpression)


def test_withlambdaexpression_constructor_exists():
    assert callable(WithLambdaExpression.__init__)


def test_withlambdaexpression_constructor_args():
    sig = inspect.signature(WithLambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::methodcall_is_not_abstract():
    assert not inspect.isabstract(pp1::MethodCall)


def test_pp1::methodcall_constructor_exists():
    assert callable(pp1::MethodCall.__init__)


def test_pp1::methodcall_constructor_args():
    sig = inspect.signature(pp1::MethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "parenthesized" in params, "Missing parameter 'parenthesized'"

def test_pp1::methodcall_has_parenthesized():
    assert hasattr(pp1::MethodCall, "parenthesized")
    descriptor = None
    for klass in pp1::MethodCall.__mro__:
        if "parenthesized" in klass.__dict__:
            descriptor = klass.__dict__["parenthesized"]
            break
    assert isinstance(descriptor, property)



def test_pp1::functioncall_is_not_abstract():
    assert not inspect.isabstract(pp1::FunctionCall)


def test_pp1::functioncall_constructor_exists():
    assert callable(pp1::FunctionCall.__init__)


def test_pp1::functioncall_constructor_args():
    sig = inspect.signature(pp1::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_parameterizedexpression_is_not_abstract():
    assert not inspect.isabstract(ParameterizedExpression)


def test_parameterizedexpression_constructor_exists():
    assert callable(ParameterizedExpression.__init__)


def test_parameterizedexpression_constructor_args():
    sig = inspect.signature(ParameterizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::withlambdaexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::WithLambdaExpression)


def test_pp1::withlambdaexpression_constructor_exists():
    assert callable(pp1::WithLambdaExpression.__init__)


def test_pp1::withlambdaexpression_constructor_args():
    sig = inspect.signature(pp1::WithLambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::selectorexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::SelectorExpression)


def test_pp1::selectorexpression_constructor_exists():
    assert callable(pp1::SelectorExpression.__init__)


def test_pp1::selectorexpression_constructor_args():
    sig = inspect.signature(pp1::SelectorExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::atexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::AtExpression)


def test_pp1::atexpression_constructor_exists():
    assert callable(pp1::AtExpression.__init__)


def test_pp1::atexpression_constructor_args():
    sig = inspect.signature(pp1::AtExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::orexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::OrExpression)


def test_pp1::orexpression_constructor_exists():
    assert callable(pp1::OrExpression.__init__)


def test_pp1::orexpression_constructor_args():
    sig = inspect.signature(pp1::OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::andexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::AndExpression)


def test_pp1::andexpression_constructor_exists():
    assert callable(pp1::AndExpression.__init__)


def test_pp1::andexpression_constructor_args():
    sig = inspect.signature(pp1::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::selectorentry_is_not_abstract():
    assert not inspect.isabstract(pp1::SelectorEntry)


def test_pp1::selectorentry_constructor_exists():
    assert callable(pp1::SelectorEntry.__init__)


def test_pp1::selectorentry_constructor_args():
    sig = inspect.signature(pp1::SelectorEntry.__init__)
    params = list(sig.parameters.keys())



def test_pp1::namedaccessexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::NamedAccessExpression)


def test_pp1::namedaccessexpression_constructor_exists():
    assert callable(pp1::NamedAccessExpression.__init__)


def test_pp1::namedaccessexpression_constructor_args():
    sig = inspect.signature(pp1::NamedAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::BinaryOpExpression)


def test_pp1::binaryopexpression_constructor_exists():
    assert callable(pp1::BinaryOpExpression.__init__)


def test_pp1::binaryopexpression_constructor_args():
    sig = inspect.signature(pp1::BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_pp1::binaryopexpression_has_opName():
    assert hasattr(pp1::BinaryOpExpression, "opName")
    descriptor = None
    for klass in pp1::BinaryOpExpression.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_pp1::appendexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::AppendExpression)


def test_pp1::appendexpression_constructor_exists():
    assert callable(pp1::AppendExpression.__init__)


def test_pp1::appendexpression_constructor_args():
    sig = inspect.signature(pp1::AppendExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::AssignmentExpression)


def test_pp1::assignmentexpression_constructor_exists():
    assert callable(pp1::AssignmentExpression.__init__)


def test_pp1::assignmentexpression_constructor_args():
    sig = inspect.signature(pp1::AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::case_is_not_abstract():
    assert not inspect.isabstract(pp1::Case)


def test_pp1::case_constructor_exists():
    assert callable(pp1::Case.__init__)


def test_pp1::case_constructor_args():
    sig = inspect.signature(pp1::Case.__init__)
    params = list(sig.parameters.keys())



def test_binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOpExpression)


def test_binaryopexpression_constructor_exists():
    assert callable(BinaryOpExpression.__init__)


def test_binaryopexpression_constructor_args():
    sig = inspect.signature(BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::additiveexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::AdditiveExpression)


def test_pp1::additiveexpression_constructor_exists():
    assert callable(pp1::AdditiveExpression.__init__)


def test_pp1::additiveexpression_constructor_args():
    sig = inspect.signature(pp1::AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::EqualityExpression)


def test_pp1::equalityexpression_constructor_exists():
    assert callable(pp1::EqualityExpression.__init__)


def test_pp1::equalityexpression_constructor_args():
    sig = inspect.signature(pp1::EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::inexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::InExpression)


def test_pp1::inexpression_constructor_exists():
    assert callable(pp1::InExpression.__init__)


def test_pp1::inexpression_constructor_args():
    sig = inspect.signature(pp1::InExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::ShiftExpression)


def test_pp1::shiftexpression_constructor_exists():
    assert callable(pp1::ShiftExpression.__init__)


def test_pp1::shiftexpression_constructor_args():
    sig = inspect.signature(pp1::ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::matchingexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::MatchingExpression)


def test_pp1::matchingexpression_constructor_exists():
    assert callable(pp1::MatchingExpression.__init__)


def test_pp1::matchingexpression_constructor_args():
    sig = inspect.signature(pp1::MatchingExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::MultiplicativeExpression)


def test_pp1::multiplicativeexpression_constructor_exists():
    assert callable(pp1::MultiplicativeExpression.__init__)


def test_pp1::multiplicativeexpression_constructor_args():
    sig = inspect.signature(pp1::MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::RelationalExpression)


def test_pp1::relationalexpression_constructor_exists():
    assert callable(pp1::RelationalExpression.__init__)


def test_pp1::relationalexpression_constructor_args():
    sig = inspect.signature(pp1::RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::relationshipexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::RelationshipExpression)


def test_pp1::relationshipexpression_constructor_exists():
    assert callable(pp1::RelationshipExpression.__init__)


def test_pp1::relationshipexpression_constructor_args():
    sig = inspect.signature(pp1::RelationshipExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::variableexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::VariableExpression)


def test_pp1::variableexpression_constructor_exists():
    assert callable(pp1::VariableExpression.__init__)


def test_pp1::variableexpression_constructor_args():
    sig = inspect.signature(pp1::VariableExpression.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_pp1::variableexpression_has_varName():
    assert hasattr(pp1::VariableExpression, "varName")
    descriptor = None
    for klass in pp1::VariableExpression.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_pp1::expressionblock_is_not_abstract():
    assert not inspect.isabstract(pp1::ExpressionBlock)


def test_pp1::expressionblock_constructor_exists():
    assert callable(pp1::ExpressionBlock.__init__)


def test_pp1::expressionblock_constructor_args():
    sig = inspect.signature(pp1::ExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_pp1::exprlist_is_not_abstract():
    assert not inspect.isabstract(pp1::ExprList)


def test_pp1::exprlist_constructor_exists():
    assert callable(pp1::ExprList.__init__)


def test_pp1::exprlist_constructor_args():
    sig = inspect.signature(pp1::ExprList.__init__)
    params = list(sig.parameters.keys())



def test_pp1::unlessexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::UnlessExpression)


def test_pp1::unlessexpression_constructor_exists():
    assert callable(pp1::UnlessExpression.__init__)


def test_pp1::unlessexpression_constructor_args():
    sig = inspect.signature(pp1::UnlessExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::parameterizedexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::ParameterizedExpression)


def test_pp1::parameterizedexpression_constructor_exists():
    assert callable(pp1::ParameterizedExpression.__init__)


def test_pp1::parameterizedexpression_constructor_args():
    sig = inspect.signature(pp1::ParameterizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::parenthesisedexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::ParenthesisedExpression)


def test_pp1::parenthesisedexpression_constructor_exists():
    assert callable(pp1::ParenthesisedExpression.__init__)


def test_pp1::parenthesisedexpression_constructor_args():
    sig = inspect.signature(pp1::ParenthesisedExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::separatorexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::SeparatorExpression)


def test_pp1::separatorexpression_constructor_exists():
    assert callable(pp1::SeparatorExpression.__init__)


def test_pp1::separatorexpression_constructor_args():
    sig = inspect.signature(pp1::SeparatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::BinaryExpression)


def test_pp1::binaryexpression_constructor_exists():
    assert callable(pp1::BinaryExpression.__init__)


def test_pp1::binaryexpression_constructor_args():
    sig = inspect.signature(pp1::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::nodedefinition_is_not_abstract():
    assert not inspect.isabstract(pp1::NodeDefinition)


def test_pp1::nodedefinition_constructor_exists():
    assert callable(pp1::NodeDefinition.__init__)


def test_pp1::nodedefinition_constructor_args():
    sig = inspect.signature(pp1::NodeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_pp1::interpolatedvariable_is_not_abstract():
    assert not inspect.isabstract(pp1::InterpolatedVariable)


def test_pp1::interpolatedvariable_constructor_exists():
    assert callable(pp1::InterpolatedVariable.__init__)


def test_pp1::interpolatedvariable_constructor_args():
    sig = inspect.signature(pp1::InterpolatedVariable.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_pp1::interpolatedvariable_has_varName():
    assert hasattr(pp1::InterpolatedVariable, "varName")
    descriptor = None
    for klass in pp1::InterpolatedVariable.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_pp1::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::UnaryExpression)


def test_pp1::unaryexpression_constructor_exists():
    assert callable(pp1::UnaryExpression.__init__)


def test_pp1::unaryexpression_constructor_args():
    sig = inspect.signature(pp1::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::stringexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::StringExpression)


def test_pp1::stringexpression_constructor_exists():
    assert callable(pp1::StringExpression.__init__)


def test_pp1::stringexpression_constructor_args():
    sig = inspect.signature(pp1::StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::caseexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::CaseExpression)


def test_pp1::caseexpression_constructor_exists():
    assert callable(pp1::CaseExpression.__init__)


def test_pp1::caseexpression_constructor_args():
    sig = inspect.signature(pp1::CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::collectexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::CollectExpression)


def test_pp1::collectexpression_constructor_exists():
    assert callable(pp1::CollectExpression.__init__)


def test_pp1::collectexpression_constructor_args():
    sig = inspect.signature(pp1::CollectExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::definition_is_not_abstract():
    assert not inspect.isabstract(pp1::Definition)


def test_pp1::definition_constructor_exists():
    assert callable(pp1::Definition.__init__)


def test_pp1::definition_constructor_args():
    sig = inspect.signature(pp1::Definition.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"

def test_pp1::definition_has_className():
    assert hasattr(pp1::Definition, "className")
    descriptor = None
    for klass in pp1::Definition.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_pp1::literalexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::LiteralExpression)


def test_pp1::literalexpression_constructor_exists():
    assert callable(pp1::LiteralExpression.__init__)


def test_pp1::literalexpression_constructor_args():
    sig = inspect.signature(pp1::LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_pp1::hostclassdefinition_is_not_abstract():
    assert not inspect.isabstract(pp1::HostClassDefinition)


def test_pp1::hostclassdefinition_constructor_exists():
    assert callable(pp1::HostClassDefinition.__init__)


def test_pp1::hostclassdefinition_constructor_args():
    sig = inspect.signature(pp1::HostClassDefinition.__init__)
    params = list(sig.parameters.keys())



def test_icollectquery_is_not_abstract():
    assert not inspect.isabstract(ICollectQuery)


def test_icollectquery_constructor_exists():
    assert callable(ICollectQuery.__init__)


def test_icollectquery_constructor_args():
    sig = inspect.signature(ICollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::exportedcollectquery_is_not_abstract():
    assert not inspect.isabstract(pp1::ExportedCollectQuery)


def test_pp1::exportedcollectquery_constructor_exists():
    assert callable(pp1::ExportedCollectQuery.__init__)


def test_pp1::exportedcollectquery_constructor_args():
    sig = inspect.signature(pp1::ExportedCollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_pp1::unarynotexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::UnaryNotExpression)


def test_pp1::unarynotexpression_constructor_exists():
    assert callable(pp1::UnaryNotExpression.__init__)


def test_pp1::unarynotexpression_constructor_args():
    sig = inspect.signature(pp1::UnaryNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::unaryminusexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::UnaryMinusExpression)


def test_pp1::unaryminusexpression_constructor_exists():
    assert callable(pp1::UnaryMinusExpression.__init__)


def test_pp1::unaryminusexpression_constructor_args():
    sig = inspect.signature(pp1::UnaryMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::virtualcollectquery_is_not_abstract():
    assert not inspect.isabstract(pp1::VirtualCollectQuery)


def test_pp1::virtualcollectquery_constructor_exists():
    assert callable(pp1::VirtualCollectQuery.__init__)


def test_pp1::virtualcollectquery_constructor_args():
    sig = inspect.signature(pp1::VirtualCollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_pp1::icollectquery_is_not_abstract():
    assert not inspect.isabstract(pp1::ICollectQuery)


def test_pp1::icollectquery_constructor_exists():
    assert callable(pp1::ICollectQuery.__init__)


def test_pp1::icollectquery_constructor_args():
    sig = inspect.signature(pp1::ICollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_pp1::attributeoperation_is_not_abstract():
    assert not inspect.isabstract(pp1::AttributeOperation)


def test_pp1::attributeoperation_constructor_exists():
    assert callable(pp1::AttributeOperation.__init__)


def test_pp1::attributeoperation_constructor_args():
    sig = inspect.signature(pp1::AttributeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "op" in params, "Missing parameter 'op'"

def test_pp1::attributeoperation_has_key():
    assert hasattr(pp1::AttributeOperation, "key")
    descriptor = None
    for klass in pp1::AttributeOperation.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_pp1::attributeoperation_has_op():
    assert hasattr(pp1::AttributeOperation, "op")
    descriptor = None
    for klass in pp1::AttributeOperation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_pp1::attributeoperations_is_not_abstract():
    assert not inspect.isabstract(pp1::AttributeOperations)


def test_pp1::attributeoperations_constructor_exists():
    assert callable(pp1::AttributeOperations.__init__)


def test_pp1::attributeoperations_constructor_args():
    sig = inspect.signature(pp1::AttributeOperations.__init__)
    params = list(sig.parameters.keys())



def test_pp1::resourcebody_is_not_abstract():
    assert not inspect.isabstract(pp1::ResourceBody)


def test_pp1::resourcebody_constructor_exists():
    assert callable(pp1::ResourceBody.__init__)


def test_pp1::resourcebody_constructor_args():
    sig = inspect.signature(pp1::ResourceBody.__init__)
    params = list(sig.parameters.keys())



def test_pp1::expression_is_not_abstract():
    assert not inspect.isabstract(pp1::Expression)


def test_pp1::expression_constructor_exists():
    assert callable(pp1::Expression.__init__)


def test_pp1::expression_constructor_args():
    sig = inspect.signature(pp1::Expression.__init__)
    params = list(sig.parameters.keys())



def test_expressionblock_is_not_abstract():
    assert not inspect.isabstract(ExpressionBlock)


def test_expressionblock_constructor_exists():
    assert callable(ExpressionBlock.__init__)


def test_expressionblock_constructor_args():
    sig = inspect.signature(ExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_pp1::lambda_is_not_abstract():
    assert not inspect.isabstract(pp1::Lambda)


def test_pp1::lambda_constructor_exists():
    assert callable(pp1::Lambda.__init__)


def test_pp1::lambda_constructor_args():
    sig = inspect.signature(pp1::Lambda.__init__)
    params = list(sig.parameters.keys())



def test_pp1::elseexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::ElseExpression)


def test_pp1::elseexpression_constructor_exists():
    assert callable(pp1::ElseExpression.__init__)


def test_pp1::elseexpression_constructor_args():
    sig = inspect.signature(pp1::ElseExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::puppetmanifest_is_not_abstract():
    assert not inspect.isabstract(pp1::PuppetManifest)


def test_pp1::puppetmanifest_constructor_exists():
    assert callable(pp1::PuppetManifest.__init__)


def test_pp1::puppetmanifest_constructor_args():
    sig = inspect.signature(pp1::PuppetManifest.__init__)
    params = list(sig.parameters.keys())



def test_pp1::hashentry_is_not_abstract():
    assert not inspect.isabstract(pp1::HashEntry)


def test_pp1::hashentry_constructor_exists():
    assert callable(pp1::HashEntry.__init__)


def test_pp1::hashentry_constructor_args():
    sig = inspect.signature(pp1::HashEntry.__init__)
    params = list(sig.parameters.keys())



def test_pp1::iquotedstring_is_not_abstract():
    assert not inspect.isabstract(pp1::IQuotedString)


def test_pp1::iquotedstring_constructor_exists():
    assert callable(pp1::IQuotedString.__init__)


def test_pp1::iquotedstring_constructor_args():
    sig = inspect.signature(pp1::IQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_pp1::importexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::ImportExpression)


def test_pp1::importexpression_constructor_exists():
    assert callable(pp1::ImportExpression.__init__)


def test_pp1::importexpression_constructor_args():
    sig = inspect.signature(pp1::ImportExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::resourceexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::ResourceExpression)


def test_pp1::resourceexpression_constructor_exists():
    assert callable(pp1::ResourceExpression.__init__)


def test_pp1::resourceexpression_constructor_args():
    sig = inspect.signature(pp1::ResourceExpression.__init__)
    params = list(sig.parameters.keys())



def test_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::literalregex_is_not_abstract():
    assert not inspect.isabstract(pp1::LiteralRegex)


def test_pp1::literalregex_constructor_exists():
    assert callable(pp1::LiteralRegex.__init__)


def test_pp1::literalregex_constructor_args():
    sig = inspect.signature(pp1::LiteralRegex.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp1::literalregex_has_value():
    assert hasattr(pp1::LiteralRegex, "value")
    descriptor = None
    for klass in pp1::LiteralRegex.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp1::literalhash_is_not_abstract():
    assert not inspect.isabstract(pp1::LiteralHash)


def test_pp1::literalhash_constructor_exists():
    assert callable(pp1::LiteralHash.__init__)


def test_pp1::literalhash_constructor_args():
    sig = inspect.signature(pp1::LiteralHash.__init__)
    params = list(sig.parameters.keys())



def test_pp1::literalname_is_not_abstract():
    assert not inspect.isabstract(pp1::LiteralName)


def test_pp1::literalname_constructor_exists():
    assert callable(pp1::LiteralName.__init__)


def test_pp1::literalname_constructor_args():
    sig = inspect.signature(pp1::LiteralName.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp1::literalname_has_value():
    assert hasattr(pp1::LiteralName, "value")
    descriptor = None
    for klass in pp1::LiteralName.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp1::literallist_is_not_abstract():
    assert not inspect.isabstract(pp1::LiteralList)


def test_pp1::literallist_constructor_exists():
    assert callable(pp1::LiteralList.__init__)


def test_pp1::literallist_constructor_args():
    sig = inspect.signature(pp1::LiteralList.__init__)
    params = list(sig.parameters.keys())



def test_pp1::literaldefault_is_not_abstract():
    assert not inspect.isabstract(pp1::LiteralDefault)


def test_pp1::literaldefault_constructor_exists():
    assert callable(pp1::LiteralDefault.__init__)


def test_pp1::literaldefault_constructor_args():
    sig = inspect.signature(pp1::LiteralDefault.__init__)
    params = list(sig.parameters.keys())



def test_pp1::literalundef_is_not_abstract():
    assert not inspect.isabstract(pp1::LiteralUndef)


def test_pp1::literalundef_constructor_exists():
    assert callable(pp1::LiteralUndef.__init__)


def test_pp1::literalundef_constructor_args():
    sig = inspect.signature(pp1::LiteralUndef.__init__)
    params = list(sig.parameters.keys())



def test_pp1::virtualnameorreference_is_not_abstract():
    assert not inspect.isabstract(pp1::VirtualNameOrReference)


def test_pp1::virtualnameorreference_constructor_exists():
    assert callable(pp1::VirtualNameOrReference.__init__)


def test_pp1::virtualnameorreference_constructor_args():
    sig = inspect.signature(pp1::VirtualNameOrReference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "exported" in params, "Missing parameter 'exported'"

def test_pp1::virtualnameorreference_has_value():
    assert hasattr(pp1::VirtualNameOrReference, "value")
    descriptor = None
    for klass in pp1::VirtualNameOrReference.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_pp1::virtualnameorreference_has_exported():
    assert hasattr(pp1::VirtualNameOrReference, "exported")
    descriptor = None
    for klass in pp1::VirtualNameOrReference.__mro__:
        if "exported" in klass.__dict__:
            descriptor = klass.__dict__["exported"]
            break
    assert isinstance(descriptor, property)



def test_pp1::literalclass_is_not_abstract():
    assert not inspect.isabstract(pp1::LiteralClass)


def test_pp1::literalclass_constructor_exists():
    assert callable(pp1::LiteralClass.__init__)


def test_pp1::literalclass_constructor_args():
    sig = inspect.signature(pp1::LiteralClass.__init__)
    params = list(sig.parameters.keys())



def test_pp1::literalboolean_is_not_abstract():
    assert not inspect.isabstract(pp1::LiteralBoolean)


def test_pp1::literalboolean_constructor_exists():
    assert callable(pp1::LiteralBoolean.__init__)


def test_pp1::literalboolean_constructor_args():
    sig = inspect.signature(pp1::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp1::literalboolean_has_value():
    assert hasattr(pp1::LiteralBoolean, "value")
    descriptor = None
    for klass in pp1::LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp1::literalnameorreference_is_not_abstract():
    assert not inspect.isabstract(pp1::LiteralNameOrReference)


def test_pp1::literalnameorreference_constructor_exists():
    assert callable(pp1::LiteralNameOrReference.__init__)


def test_pp1::literalnameorreference_constructor_args():
    sig = inspect.signature(pp1::LiteralNameOrReference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp1::literalnameorreference_has_value():
    assert hasattr(pp1::LiteralNameOrReference, "value")
    descriptor = None
    for klass in pp1::LiteralNameOrReference.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp1::ifexpression_is_not_abstract():
    assert not inspect.isabstract(pp1::IfExpression)


def test_pp1::ifexpression_constructor_exists():
    assert callable(pp1::IfExpression.__init__)


def test_pp1::ifexpression_constructor_args():
    sig = inspect.signature(pp1::IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1::definitionargument_is_not_abstract():
    assert not inspect.isabstract(pp1::DefinitionArgument)


def test_pp1::definitionargument_constructor_exists():
    assert callable(pp1::DefinitionArgument.__init__)


def test_pp1::definitionargument_constructor_args():
    sig = inspect.signature(pp1::DefinitionArgument.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "argName" in params, "Missing parameter 'argName'"

def test_pp1::definitionargument_has_op():
    assert hasattr(pp1::DefinitionArgument, "op")
    descriptor = None
    for klass in pp1::DefinitionArgument.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_pp1::definitionargument_has_argName():
    assert hasattr(pp1::DefinitionArgument, "argName")
    descriptor = None
    for klass in pp1::DefinitionArgument.__mro__:
        if "argName" in klass.__dict__:
            descriptor = klass.__dict__["argName"]
            break
    assert isinstance(descriptor, property)



def test_pp1::definitionargumentlist_is_not_abstract():
    assert not inspect.isabstract(pp1::DefinitionArgumentList)


def test_pp1::definitionargumentlist_constructor_exists():
    assert callable(pp1::DefinitionArgumentList.__init__)


def test_pp1::definitionargumentlist_constructor_args():
    sig = inspect.signature(pp1::DefinitionArgumentList.__init__)
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
TextExpression_strategy = st.builds(
    TextExpression,
)
pp1::ExpressionTE_strategy = st.builds(
    pp1::ExpressionTE,
)
pp1::VariableTE_strategy = st.builds(
    pp1::VariableTE,
    varName=
        safe_text
)
pp1::VerbatimTE_strategy = st.builds(
    pp1::VerbatimTE,
    text=
        safe_text
)
Lambda_strategy = st.builds(
    Lambda,
)
pp1::RubyLambda_strategy = st.builds(
    pp1::RubyLambda,
)
pp1::JavaLambda_strategy = st.builds(
    pp1::JavaLambda,
    farrow=
        st.booleans()
)
pp1::TextExpression_strategy = st.builds(
    pp1::TextExpression,
)
IQuotedString_strategy = st.builds(
    IQuotedString,
)
StringExpression_strategy = st.builds(
    StringExpression,
)
pp1::SingleQuotedString_strategy = st.builds(
    pp1::SingleQuotedString,
    text=
        safe_text
)
pp1::UnquotedString_strategy = st.builds(
    pp1::UnquotedString,
)
pp1::DoubleQuotedString_strategy = st.builds(
    pp1::DoubleQuotedString,
)
IfExpression_strategy = st.builds(
    IfExpression,
)
pp1::ElseIfExpression_strategy = st.builds(
    pp1::ElseIfExpression,
)
WithLambdaExpression_strategy = st.builds(
    WithLambdaExpression,
)
pp1::MethodCall_strategy = st.builds(
    pp1::MethodCall,
    parenthesized=
        st.booleans()
)
pp1::FunctionCall_strategy = st.builds(
    pp1::FunctionCall,
)
ParameterizedExpression_strategy = st.builds(
    ParameterizedExpression,
)
pp1::WithLambdaExpression_strategy = st.builds(
    pp1::WithLambdaExpression,
)
pp1::SelectorExpression_strategy = st.builds(
    pp1::SelectorExpression,
)
pp1::AtExpression_strategy = st.builds(
    pp1::AtExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
pp1::OrExpression_strategy = st.builds(
    pp1::OrExpression,
)
pp1::AndExpression_strategy = st.builds(
    pp1::AndExpression,
)
pp1::SelectorEntry_strategy = st.builds(
    pp1::SelectorEntry,
)
pp1::NamedAccessExpression_strategy = st.builds(
    pp1::NamedAccessExpression,
)
pp1::BinaryOpExpression_strategy = st.builds(
    pp1::BinaryOpExpression,
    opName=
        safe_text
)
pp1::AppendExpression_strategy = st.builds(
    pp1::AppendExpression,
)
pp1::AssignmentExpression_strategy = st.builds(
    pp1::AssignmentExpression,
)
pp1::Case_strategy = st.builds(
    pp1::Case,
)
BinaryOpExpression_strategy = st.builds(
    BinaryOpExpression,
)
pp1::AdditiveExpression_strategy = st.builds(
    pp1::AdditiveExpression,
)
pp1::EqualityExpression_strategy = st.builds(
    pp1::EqualityExpression,
)
pp1::InExpression_strategy = st.builds(
    pp1::InExpression,
)
pp1::ShiftExpression_strategy = st.builds(
    pp1::ShiftExpression,
)
pp1::MatchingExpression_strategy = st.builds(
    pp1::MatchingExpression,
)
pp1::MultiplicativeExpression_strategy = st.builds(
    pp1::MultiplicativeExpression,
)
pp1::RelationalExpression_strategy = st.builds(
    pp1::RelationalExpression,
)
pp1::RelationshipExpression_strategy = st.builds(
    pp1::RelationshipExpression,
)
Expression_strategy = st.builds(
    Expression,
)
pp1::VariableExpression_strategy = st.builds(
    pp1::VariableExpression,
    varName=
        safe_text
)
pp1::ExpressionBlock_strategy = st.builds(
    pp1::ExpressionBlock,
)
pp1::ExprList_strategy = st.builds(
    pp1::ExprList,
)
pp1::UnlessExpression_strategy = st.builds(
    pp1::UnlessExpression,
)
pp1::ParameterizedExpression_strategy = st.builds(
    pp1::ParameterizedExpression,
)
pp1::ParenthesisedExpression_strategy = st.builds(
    pp1::ParenthesisedExpression,
)
pp1::SeparatorExpression_strategy = st.builds(
    pp1::SeparatorExpression,
)
pp1::BinaryExpression_strategy = st.builds(
    pp1::BinaryExpression,
)
pp1::NodeDefinition_strategy = st.builds(
    pp1::NodeDefinition,
)
pp1::InterpolatedVariable_strategy = st.builds(
    pp1::InterpolatedVariable,
    varName=
        safe_text
)
pp1::UnaryExpression_strategy = st.builds(
    pp1::UnaryExpression,
)
pp1::StringExpression_strategy = st.builds(
    pp1::StringExpression,
)
pp1::CaseExpression_strategy = st.builds(
    pp1::CaseExpression,
)
pp1::CollectExpression_strategy = st.builds(
    pp1::CollectExpression,
)
pp1::Definition_strategy = st.builds(
    pp1::Definition,
    className=
        safe_text
)
pp1::LiteralExpression_strategy = st.builds(
    pp1::LiteralExpression,
)
Definition_strategy = st.builds(
    Definition,
)
pp1::HostClassDefinition_strategy = st.builds(
    pp1::HostClassDefinition,
)
ICollectQuery_strategy = st.builds(
    ICollectQuery,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
pp1::ExportedCollectQuery_strategy = st.builds(
    pp1::ExportedCollectQuery,
)
pp1::UnaryNotExpression_strategy = st.builds(
    pp1::UnaryNotExpression,
)
pp1::UnaryMinusExpression_strategy = st.builds(
    pp1::UnaryMinusExpression,
)
pp1::VirtualCollectQuery_strategy = st.builds(
    pp1::VirtualCollectQuery,
)
pp1::ICollectQuery_strategy = st.builds(
    pp1::ICollectQuery,
)
pp1::AttributeOperation_strategy = st.builds(
    pp1::AttributeOperation,
    key=
        safe_text,
    op=
        safe_text
)
pp1::AttributeOperations_strategy = st.builds(
    pp1::AttributeOperations,
)
pp1::ResourceBody_strategy = st.builds(
    pp1::ResourceBody,
)
pp1::Expression_strategy = st.builds(
    pp1::Expression,
)
ExpressionBlock_strategy = st.builds(
    ExpressionBlock,
)
pp1::Lambda_strategy = st.builds(
    pp1::Lambda,
)
pp1::ElseExpression_strategy = st.builds(
    pp1::ElseExpression,
)
pp1::PuppetManifest_strategy = st.builds(
    pp1::PuppetManifest,
)
pp1::HashEntry_strategy = st.builds(
    pp1::HashEntry,
)
pp1::IQuotedString_strategy = st.builds(
    pp1::IQuotedString,
)
pp1::ImportExpression_strategy = st.builds(
    pp1::ImportExpression,
)
pp1::ResourceExpression_strategy = st.builds(
    pp1::ResourceExpression,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
pp1::LiteralRegex_strategy = st.builds(
    pp1::LiteralRegex,
    value=
        safe_text
)
pp1::LiteralHash_strategy = st.builds(
    pp1::LiteralHash,
)
pp1::LiteralName_strategy = st.builds(
    pp1::LiteralName,
    value=
        safe_text
)
pp1::LiteralList_strategy = st.builds(
    pp1::LiteralList,
)
pp1::LiteralDefault_strategy = st.builds(
    pp1::LiteralDefault,
)
pp1::LiteralUndef_strategy = st.builds(
    pp1::LiteralUndef,
)
pp1::VirtualNameOrReference_strategy = st.builds(
    pp1::VirtualNameOrReference,
    value=
        safe_text,
    exported=
        st.booleans()
)
pp1::LiteralClass_strategy = st.builds(
    pp1::LiteralClass,
)
pp1::LiteralBoolean_strategy = st.builds(
    pp1::LiteralBoolean,
    value=
        st.booleans()
)
pp1::LiteralNameOrReference_strategy = st.builds(
    pp1::LiteralNameOrReference,
    value=
        safe_text
)
pp1::IfExpression_strategy = st.builds(
    pp1::IfExpression,
)
pp1::DefinitionArgument_strategy = st.builds(
    pp1::DefinitionArgument,
    op=
        safe_text,
    argName=
        safe_text
)
pp1::DefinitionArgumentList_strategy = st.builds(
    pp1::DefinitionArgumentList,
)

@given(instance=TextExpression_strategy)
@settings(max_examples=50)
def test_textexpression_instantiation(instance):
    assert isinstance(instance, TextExpression)

@given(instance=pp1::ExpressionTE_strategy)
@settings(max_examples=50)
def test_pp1::expressionte_instantiation(instance):
    assert isinstance(instance, pp1::ExpressionTE)

@given(instance=pp1::VariableTE_strategy)
@settings(max_examples=50)
def test_pp1::variablete_instantiation(instance):
    assert isinstance(instance, pp1::VariableTE)

@given(instance=pp1::VariableTE_strategy)
def test_pp1::variablete_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=pp1::VariableTE_strategy)
def test_pp1::variablete_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=pp1::VerbatimTE_strategy)
@settings(max_examples=50)
def test_pp1::verbatimte_instantiation(instance):
    assert isinstance(instance, pp1::VerbatimTE)

@given(instance=pp1::VerbatimTE_strategy)
def test_pp1::verbatimte_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=pp1::VerbatimTE_strategy)
def test_pp1::verbatimte_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Lambda_strategy)
@settings(max_examples=50)
def test_lambda_instantiation(instance):
    assert isinstance(instance, Lambda)

@given(instance=pp1::RubyLambda_strategy)
@settings(max_examples=50)
def test_pp1::rubylambda_instantiation(instance):
    assert isinstance(instance, pp1::RubyLambda)

@given(instance=pp1::JavaLambda_strategy)
@settings(max_examples=50)
def test_pp1::javalambda_instantiation(instance):
    assert isinstance(instance, pp1::JavaLambda)

@given(instance=pp1::JavaLambda_strategy)
def test_pp1::javalambda_farrow_type(instance):
    assert isinstance(instance.farrow, bool)


@given(instance=pp1::JavaLambda_strategy)
def test_pp1::javalambda_farrow_setter(instance):
    original = instance.farrow
    instance.farrow = original
    assert instance.farrow == original

@given(instance=pp1::TextExpression_strategy)
@settings(max_examples=50)
def test_pp1::textexpression_instantiation(instance):
    assert isinstance(instance, pp1::TextExpression)

@given(instance=IQuotedString_strategy)
@settings(max_examples=50)
def test_iquotedstring_instantiation(instance):
    assert isinstance(instance, IQuotedString)

@given(instance=StringExpression_strategy)
@settings(max_examples=50)
def test_stringexpression_instantiation(instance):
    assert isinstance(instance, StringExpression)

@given(instance=pp1::SingleQuotedString_strategy)
@settings(max_examples=50)
def test_pp1::singlequotedstring_instantiation(instance):
    assert isinstance(instance, pp1::SingleQuotedString)

@given(instance=pp1::SingleQuotedString_strategy)
def test_pp1::singlequotedstring_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=pp1::SingleQuotedString_strategy)
def test_pp1::singlequotedstring_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=pp1::UnquotedString_strategy)
@settings(max_examples=50)
def test_pp1::unquotedstring_instantiation(instance):
    assert isinstance(instance, pp1::UnquotedString)

@given(instance=pp1::DoubleQuotedString_strategy)
@settings(max_examples=50)
def test_pp1::doublequotedstring_instantiation(instance):
    assert isinstance(instance, pp1::DoubleQuotedString)

@given(instance=IfExpression_strategy)
@settings(max_examples=50)
def test_ifexpression_instantiation(instance):
    assert isinstance(instance, IfExpression)

@given(instance=pp1::ElseIfExpression_strategy)
@settings(max_examples=50)
def test_pp1::elseifexpression_instantiation(instance):
    assert isinstance(instance, pp1::ElseIfExpression)

@given(instance=WithLambdaExpression_strategy)
@settings(max_examples=50)
def test_withlambdaexpression_instantiation(instance):
    assert isinstance(instance, WithLambdaExpression)

@given(instance=pp1::MethodCall_strategy)
@settings(max_examples=50)
def test_pp1::methodcall_instantiation(instance):
    assert isinstance(instance, pp1::MethodCall)

@given(instance=pp1::MethodCall_strategy)
def test_pp1::methodcall_parenthesized_type(instance):
    assert isinstance(instance.parenthesized, bool)


@given(instance=pp1::MethodCall_strategy)
def test_pp1::methodcall_parenthesized_setter(instance):
    original = instance.parenthesized
    instance.parenthesized = original
    assert instance.parenthesized == original

@given(instance=pp1::FunctionCall_strategy)
@settings(max_examples=50)
def test_pp1::functioncall_instantiation(instance):
    assert isinstance(instance, pp1::FunctionCall)

@given(instance=ParameterizedExpression_strategy)
@settings(max_examples=50)
def test_parameterizedexpression_instantiation(instance):
    assert isinstance(instance, ParameterizedExpression)

@given(instance=pp1::WithLambdaExpression_strategy)
@settings(max_examples=50)
def test_pp1::withlambdaexpression_instantiation(instance):
    assert isinstance(instance, pp1::WithLambdaExpression)

@given(instance=pp1::SelectorExpression_strategy)
@settings(max_examples=50)
def test_pp1::selectorexpression_instantiation(instance):
    assert isinstance(instance, pp1::SelectorExpression)

@given(instance=pp1::AtExpression_strategy)
@settings(max_examples=50)
def test_pp1::atexpression_instantiation(instance):
    assert isinstance(instance, pp1::AtExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=pp1::OrExpression_strategy)
@settings(max_examples=50)
def test_pp1::orexpression_instantiation(instance):
    assert isinstance(instance, pp1::OrExpression)

@given(instance=pp1::AndExpression_strategy)
@settings(max_examples=50)
def test_pp1::andexpression_instantiation(instance):
    assert isinstance(instance, pp1::AndExpression)

@given(instance=pp1::SelectorEntry_strategy)
@settings(max_examples=50)
def test_pp1::selectorentry_instantiation(instance):
    assert isinstance(instance, pp1::SelectorEntry)

@given(instance=pp1::NamedAccessExpression_strategy)
@settings(max_examples=50)
def test_pp1::namedaccessexpression_instantiation(instance):
    assert isinstance(instance, pp1::NamedAccessExpression)

@given(instance=pp1::BinaryOpExpression_strategy)
@settings(max_examples=50)
def test_pp1::binaryopexpression_instantiation(instance):
    assert isinstance(instance, pp1::BinaryOpExpression)

@given(instance=pp1::BinaryOpExpression_strategy)
def test_pp1::binaryopexpression_opName_type(instance):
    assert isinstance(instance.opName, str)


@given(instance=pp1::BinaryOpExpression_strategy)
def test_pp1::binaryopexpression_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=pp1::AppendExpression_strategy)
@settings(max_examples=50)
def test_pp1::appendexpression_instantiation(instance):
    assert isinstance(instance, pp1::AppendExpression)

@given(instance=pp1::AssignmentExpression_strategy)
@settings(max_examples=50)
def test_pp1::assignmentexpression_instantiation(instance):
    assert isinstance(instance, pp1::AssignmentExpression)

@given(instance=pp1::Case_strategy)
@settings(max_examples=50)
def test_pp1::case_instantiation(instance):
    assert isinstance(instance, pp1::Case)

@given(instance=BinaryOpExpression_strategy)
@settings(max_examples=50)
def test_binaryopexpression_instantiation(instance):
    assert isinstance(instance, BinaryOpExpression)

@given(instance=pp1::AdditiveExpression_strategy)
@settings(max_examples=50)
def test_pp1::additiveexpression_instantiation(instance):
    assert isinstance(instance, pp1::AdditiveExpression)

@given(instance=pp1::EqualityExpression_strategy)
@settings(max_examples=50)
def test_pp1::equalityexpression_instantiation(instance):
    assert isinstance(instance, pp1::EqualityExpression)

@given(instance=pp1::InExpression_strategy)
@settings(max_examples=50)
def test_pp1::inexpression_instantiation(instance):
    assert isinstance(instance, pp1::InExpression)

@given(instance=pp1::ShiftExpression_strategy)
@settings(max_examples=50)
def test_pp1::shiftexpression_instantiation(instance):
    assert isinstance(instance, pp1::ShiftExpression)

@given(instance=pp1::MatchingExpression_strategy)
@settings(max_examples=50)
def test_pp1::matchingexpression_instantiation(instance):
    assert isinstance(instance, pp1::MatchingExpression)

@given(instance=pp1::MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_pp1::multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, pp1::MultiplicativeExpression)

@given(instance=pp1::RelationalExpression_strategy)
@settings(max_examples=50)
def test_pp1::relationalexpression_instantiation(instance):
    assert isinstance(instance, pp1::RelationalExpression)

@given(instance=pp1::RelationshipExpression_strategy)
@settings(max_examples=50)
def test_pp1::relationshipexpression_instantiation(instance):
    assert isinstance(instance, pp1::RelationshipExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=pp1::VariableExpression_strategy)
@settings(max_examples=50)
def test_pp1::variableexpression_instantiation(instance):
    assert isinstance(instance, pp1::VariableExpression)

@given(instance=pp1::VariableExpression_strategy)
def test_pp1::variableexpression_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=pp1::VariableExpression_strategy)
def test_pp1::variableexpression_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=pp1::ExpressionBlock_strategy)
@settings(max_examples=50)
def test_pp1::expressionblock_instantiation(instance):
    assert isinstance(instance, pp1::ExpressionBlock)

@given(instance=pp1::ExprList_strategy)
@settings(max_examples=50)
def test_pp1::exprlist_instantiation(instance):
    assert isinstance(instance, pp1::ExprList)

@given(instance=pp1::UnlessExpression_strategy)
@settings(max_examples=50)
def test_pp1::unlessexpression_instantiation(instance):
    assert isinstance(instance, pp1::UnlessExpression)

@given(instance=pp1::ParameterizedExpression_strategy)
@settings(max_examples=50)
def test_pp1::parameterizedexpression_instantiation(instance):
    assert isinstance(instance, pp1::ParameterizedExpression)

@given(instance=pp1::ParenthesisedExpression_strategy)
@settings(max_examples=50)
def test_pp1::parenthesisedexpression_instantiation(instance):
    assert isinstance(instance, pp1::ParenthesisedExpression)

@given(instance=pp1::SeparatorExpression_strategy)
@settings(max_examples=50)
def test_pp1::separatorexpression_instantiation(instance):
    assert isinstance(instance, pp1::SeparatorExpression)

@given(instance=pp1::BinaryExpression_strategy)
@settings(max_examples=50)
def test_pp1::binaryexpression_instantiation(instance):
    assert isinstance(instance, pp1::BinaryExpression)

@given(instance=pp1::NodeDefinition_strategy)
@settings(max_examples=50)
def test_pp1::nodedefinition_instantiation(instance):
    assert isinstance(instance, pp1::NodeDefinition)

@given(instance=pp1::InterpolatedVariable_strategy)
@settings(max_examples=50)
def test_pp1::interpolatedvariable_instantiation(instance):
    assert isinstance(instance, pp1::InterpolatedVariable)

@given(instance=pp1::InterpolatedVariable_strategy)
def test_pp1::interpolatedvariable_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=pp1::InterpolatedVariable_strategy)
def test_pp1::interpolatedvariable_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=pp1::UnaryExpression_strategy)
@settings(max_examples=50)
def test_pp1::unaryexpression_instantiation(instance):
    assert isinstance(instance, pp1::UnaryExpression)

@given(instance=pp1::StringExpression_strategy)
@settings(max_examples=50)
def test_pp1::stringexpression_instantiation(instance):
    assert isinstance(instance, pp1::StringExpression)

@given(instance=pp1::CaseExpression_strategy)
@settings(max_examples=50)
def test_pp1::caseexpression_instantiation(instance):
    assert isinstance(instance, pp1::CaseExpression)

@given(instance=pp1::CollectExpression_strategy)
@settings(max_examples=50)
def test_pp1::collectexpression_instantiation(instance):
    assert isinstance(instance, pp1::CollectExpression)

@given(instance=pp1::Definition_strategy)
@settings(max_examples=50)
def test_pp1::definition_instantiation(instance):
    assert isinstance(instance, pp1::Definition)

@given(instance=pp1::Definition_strategy)
def test_pp1::definition_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=pp1::Definition_strategy)
def test_pp1::definition_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=pp1::LiteralExpression_strategy)
@settings(max_examples=50)
def test_pp1::literalexpression_instantiation(instance):
    assert isinstance(instance, pp1::LiteralExpression)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=pp1::HostClassDefinition_strategy)
@settings(max_examples=50)
def test_pp1::hostclassdefinition_instantiation(instance):
    assert isinstance(instance, pp1::HostClassDefinition)

@given(instance=ICollectQuery_strategy)
@settings(max_examples=50)
def test_icollectquery_instantiation(instance):
    assert isinstance(instance, ICollectQuery)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=pp1::ExportedCollectQuery_strategy)
@settings(max_examples=50)
def test_pp1::exportedcollectquery_instantiation(instance):
    assert isinstance(instance, pp1::ExportedCollectQuery)

@given(instance=pp1::UnaryNotExpression_strategy)
@settings(max_examples=50)
def test_pp1::unarynotexpression_instantiation(instance):
    assert isinstance(instance, pp1::UnaryNotExpression)

@given(instance=pp1::UnaryMinusExpression_strategy)
@settings(max_examples=50)
def test_pp1::unaryminusexpression_instantiation(instance):
    assert isinstance(instance, pp1::UnaryMinusExpression)

@given(instance=pp1::VirtualCollectQuery_strategy)
@settings(max_examples=50)
def test_pp1::virtualcollectquery_instantiation(instance):
    assert isinstance(instance, pp1::VirtualCollectQuery)

@given(instance=pp1::ICollectQuery_strategy)
@settings(max_examples=50)
def test_pp1::icollectquery_instantiation(instance):
    assert isinstance(instance, pp1::ICollectQuery)

@given(instance=pp1::AttributeOperation_strategy)
@settings(max_examples=50)
def test_pp1::attributeoperation_instantiation(instance):
    assert isinstance(instance, pp1::AttributeOperation)

@given(instance=pp1::AttributeOperation_strategy)
def test_pp1::attributeoperation_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=pp1::AttributeOperation_strategy)
def test_pp1::attributeoperation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=pp1::AttributeOperation_strategy)
def test_pp1::attributeoperation_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=pp1::AttributeOperation_strategy)
def test_pp1::attributeoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=pp1::AttributeOperations_strategy)
@settings(max_examples=50)
def test_pp1::attributeoperations_instantiation(instance):
    assert isinstance(instance, pp1::AttributeOperations)

@given(instance=pp1::ResourceBody_strategy)
@settings(max_examples=50)
def test_pp1::resourcebody_instantiation(instance):
    assert isinstance(instance, pp1::ResourceBody)

@given(instance=pp1::Expression_strategy)
@settings(max_examples=50)
def test_pp1::expression_instantiation(instance):
    assert isinstance(instance, pp1::Expression)

@given(instance=ExpressionBlock_strategy)
@settings(max_examples=50)
def test_expressionblock_instantiation(instance):
    assert isinstance(instance, ExpressionBlock)

@given(instance=pp1::Lambda_strategy)
@settings(max_examples=50)
def test_pp1::lambda_instantiation(instance):
    assert isinstance(instance, pp1::Lambda)

@given(instance=pp1::ElseExpression_strategy)
@settings(max_examples=50)
def test_pp1::elseexpression_instantiation(instance):
    assert isinstance(instance, pp1::ElseExpression)

@given(instance=pp1::PuppetManifest_strategy)
@settings(max_examples=50)
def test_pp1::puppetmanifest_instantiation(instance):
    assert isinstance(instance, pp1::PuppetManifest)

@given(instance=pp1::HashEntry_strategy)
@settings(max_examples=50)
def test_pp1::hashentry_instantiation(instance):
    assert isinstance(instance, pp1::HashEntry)

@given(instance=pp1::IQuotedString_strategy)
@settings(max_examples=50)
def test_pp1::iquotedstring_instantiation(instance):
    assert isinstance(instance, pp1::IQuotedString)

@given(instance=pp1::ImportExpression_strategy)
@settings(max_examples=50)
def test_pp1::importexpression_instantiation(instance):
    assert isinstance(instance, pp1::ImportExpression)

@given(instance=pp1::ResourceExpression_strategy)
@settings(max_examples=50)
def test_pp1::resourceexpression_instantiation(instance):
    assert isinstance(instance, pp1::ResourceExpression)

@given(instance=LiteralExpression_strategy)
@settings(max_examples=50)
def test_literalexpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)

@given(instance=pp1::LiteralRegex_strategy)
@settings(max_examples=50)
def test_pp1::literalregex_instantiation(instance):
    assert isinstance(instance, pp1::LiteralRegex)

@given(instance=pp1::LiteralRegex_strategy)
def test_pp1::literalregex_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pp1::LiteralRegex_strategy)
def test_pp1::literalregex_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp1::LiteralHash_strategy)
@settings(max_examples=50)
def test_pp1::literalhash_instantiation(instance):
    assert isinstance(instance, pp1::LiteralHash)

@given(instance=pp1::LiteralName_strategy)
@settings(max_examples=50)
def test_pp1::literalname_instantiation(instance):
    assert isinstance(instance, pp1::LiteralName)

@given(instance=pp1::LiteralName_strategy)
def test_pp1::literalname_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pp1::LiteralName_strategy)
def test_pp1::literalname_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp1::LiteralList_strategy)
@settings(max_examples=50)
def test_pp1::literallist_instantiation(instance):
    assert isinstance(instance, pp1::LiteralList)

@given(instance=pp1::LiteralDefault_strategy)
@settings(max_examples=50)
def test_pp1::literaldefault_instantiation(instance):
    assert isinstance(instance, pp1::LiteralDefault)

@given(instance=pp1::LiteralUndef_strategy)
@settings(max_examples=50)
def test_pp1::literalundef_instantiation(instance):
    assert isinstance(instance, pp1::LiteralUndef)

@given(instance=pp1::VirtualNameOrReference_strategy)
@settings(max_examples=50)
def test_pp1::virtualnameorreference_instantiation(instance):
    assert isinstance(instance, pp1::VirtualNameOrReference)

@given(instance=pp1::VirtualNameOrReference_strategy)
def test_pp1::virtualnameorreference_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pp1::VirtualNameOrReference_strategy)
def test_pp1::virtualnameorreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp1::VirtualNameOrReference_strategy)
def test_pp1::virtualnameorreference_exported_type(instance):
    assert isinstance(instance.exported, bool)


@given(instance=pp1::VirtualNameOrReference_strategy)
def test_pp1::virtualnameorreference_exported_setter(instance):
    original = instance.exported
    instance.exported = original
    assert instance.exported == original

@given(instance=pp1::LiteralClass_strategy)
@settings(max_examples=50)
def test_pp1::literalclass_instantiation(instance):
    assert isinstance(instance, pp1::LiteralClass)

@given(instance=pp1::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_pp1::literalboolean_instantiation(instance):
    assert isinstance(instance, pp1::LiteralBoolean)

@given(instance=pp1::LiteralBoolean_strategy)
def test_pp1::literalboolean_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=pp1::LiteralBoolean_strategy)
def test_pp1::literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp1::LiteralNameOrReference_strategy)
@settings(max_examples=50)
def test_pp1::literalnameorreference_instantiation(instance):
    assert isinstance(instance, pp1::LiteralNameOrReference)

@given(instance=pp1::LiteralNameOrReference_strategy)
def test_pp1::literalnameorreference_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pp1::LiteralNameOrReference_strategy)
def test_pp1::literalnameorreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp1::IfExpression_strategy)
@settings(max_examples=50)
def test_pp1::ifexpression_instantiation(instance):
    assert isinstance(instance, pp1::IfExpression)

@given(instance=pp1::DefinitionArgument_strategy)
@settings(max_examples=50)
def test_pp1::definitionargument_instantiation(instance):
    assert isinstance(instance, pp1::DefinitionArgument)

@given(instance=pp1::DefinitionArgument_strategy)
def test_pp1::definitionargument_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=pp1::DefinitionArgument_strategy)
def test_pp1::definitionargument_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=pp1::DefinitionArgument_strategy)
def test_pp1::definitionargument_argName_type(instance):
    assert isinstance(instance.argName, str)


@given(instance=pp1::DefinitionArgument_strategy)
def test_pp1::definitionargument_argName_setter(instance):
    original = instance.argName
    instance.argName = original
    assert instance.argName == original

@given(instance=pp1::DefinitionArgumentList_strategy)
@settings(max_examples=50)
def test_pp1::definitionargumentlist_instantiation(instance):
    assert isinstance(instance, pp1::DefinitionArgumentList)
