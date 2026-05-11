import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Lambda,
    pp::RubyLambda,
    pp::JavaLambda,
    IfExpression,
    pp::ElseIfExpression,
    TextExpression,
    pp::ExpressionTE,
    pp::VariableTE,
    pp::VerbatimTE,
    pp::TextExpression,
    IQuotedString,
    StringExpression,
    pp::UnquotedString,
    pp::SingleQuotedString,
    pp::DoubleQuotedString,
    WithLambdaExpression,
    pp::MethodCall,
    pp::FunctionCall,
    pp::HashEntry,
    pp::IQuotedString,
    ParameterizedExpression,
    pp::WithLambdaExpression,
    pp::SelectorExpression,
    pp::AtExpression,
    BinaryExpression,
    pp::NamedAccessExpression,
    pp::BinaryOpExpression,
    pp::AppendExpression,
    pp::OrExpression,
    pp::SelectorEntry,
    pp::AndExpression,
    pp::AssignmentExpression,
    BinaryOpExpression,
    pp::EqualityExpression,
    pp::AdditiveExpression,
    pp::ShiftExpression,
    pp::InExpression,
    pp::MultiplicativeExpression,
    pp::MatchingExpression,
    pp::RelationalExpression,
    pp::RelationshipExpression,
    pp::DefinitionArgumentList,
    Expression,
    pp::ResourceExpression,
    pp::StringExpression,
    pp::UnaryExpression,
    pp::ParameterizedExpression,
    pp::InterpolatedVariable,
    pp::ExprList,
    pp::BinaryExpression,
    pp::CollectExpression,
    pp::ImportExpression,
    pp::UnlessExpression,
    pp::ParenthesisedExpression,
    pp::ExpressionBlock,
    pp::NodeDefinition,
    pp::SeparatorExpression,
    pp::VariableExpression,
    pp::Definition,
    pp::LiteralExpression,
    Definition,
    pp::HostClassDefinition,
    ICollectQuery,
    UnaryExpression,
    pp::ExportedCollectQuery,
    pp::UnaryMinusExpression,
    pp::UnaryNotExpression,
    pp::VirtualCollectQuery,
    pp::ICollectQuery,
    LiteralExpression,
    pp::VirtualNameOrReference,
    pp::LiteralName,
    pp::LiteralBoolean,
    pp::LiteralClass,
    pp::LiteralList,
    pp::LiteralDefault,
    pp::LiteralUndef,
    pp::LiteralHash,
    pp::LiteralRegex,
    pp::LiteralNameOrReference,
    pp::IfExpression,
    pp::Case,
    pp::CaseExpression,
    pp::DefinitionArgument,
    pp::AttributeOperation,
    pp::AttributeOperations,
    pp::ResourceBody,
    pp::Expression,
    ExpressionBlock,
    pp::Lambda,
    pp::ElseExpression,
    pp::PuppetManifest,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lambda_is_not_abstract():
    assert not inspect.isabstract(Lambda)


def test_lambda_constructor_exists():
    assert callable(Lambda.__init__)


def test_lambda_constructor_args():
    sig = inspect.signature(Lambda.__init__)
    params = list(sig.parameters.keys())



def test_pp::rubylambda_is_not_abstract():
    assert not inspect.isabstract(pp::RubyLambda)


def test_pp::rubylambda_constructor_exists():
    assert callable(pp::RubyLambda.__init__)


def test_pp::rubylambda_constructor_args():
    sig = inspect.signature(pp::RubyLambda.__init__)
    params = list(sig.parameters.keys())



def test_pp::javalambda_is_not_abstract():
    assert not inspect.isabstract(pp::JavaLambda)


def test_pp::javalambda_constructor_exists():
    assert callable(pp::JavaLambda.__init__)


def test_pp::javalambda_constructor_args():
    sig = inspect.signature(pp::JavaLambda.__init__)
    params = list(sig.parameters.keys())
    assert "farrow" in params, "Missing parameter 'farrow'"

def test_pp::javalambda_has_farrow():
    assert hasattr(pp::JavaLambda, "farrow")
    descriptor = None
    for klass in pp::JavaLambda.__mro__:
        if "farrow" in klass.__dict__:
            descriptor = klass.__dict__["farrow"]
            break
    assert isinstance(descriptor, property)



def test_ifexpression_is_not_abstract():
    assert not inspect.isabstract(IfExpression)


def test_ifexpression_constructor_exists():
    assert callable(IfExpression.__init__)


def test_ifexpression_constructor_args():
    sig = inspect.signature(IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::elseifexpression_is_not_abstract():
    assert not inspect.isabstract(pp::ElseIfExpression)


def test_pp::elseifexpression_constructor_exists():
    assert callable(pp::ElseIfExpression.__init__)


def test_pp::elseifexpression_constructor_args():
    sig = inspect.signature(pp::ElseIfExpression.__init__)
    params = list(sig.parameters.keys())



def test_textexpression_is_not_abstract():
    assert not inspect.isabstract(TextExpression)


def test_textexpression_constructor_exists():
    assert callable(TextExpression.__init__)


def test_textexpression_constructor_args():
    sig = inspect.signature(TextExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::expressionte_is_not_abstract():
    assert not inspect.isabstract(pp::ExpressionTE)


def test_pp::expressionte_constructor_exists():
    assert callable(pp::ExpressionTE.__init__)


def test_pp::expressionte_constructor_args():
    sig = inspect.signature(pp::ExpressionTE.__init__)
    params = list(sig.parameters.keys())



def test_pp::variablete_is_not_abstract():
    assert not inspect.isabstract(pp::VariableTE)


def test_pp::variablete_constructor_exists():
    assert callable(pp::VariableTE.__init__)


def test_pp::variablete_constructor_args():
    sig = inspect.signature(pp::VariableTE.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_pp::variablete_has_varName():
    assert hasattr(pp::VariableTE, "varName")
    descriptor = None
    for klass in pp::VariableTE.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_pp::verbatimte_is_not_abstract():
    assert not inspect.isabstract(pp::VerbatimTE)


def test_pp::verbatimte_constructor_exists():
    assert callable(pp::VerbatimTE.__init__)


def test_pp::verbatimte_constructor_args():
    sig = inspect.signature(pp::VerbatimTE.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_pp::verbatimte_has_text():
    assert hasattr(pp::VerbatimTE, "text")
    descriptor = None
    for klass in pp::VerbatimTE.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_pp::textexpression_is_not_abstract():
    assert not inspect.isabstract(pp::TextExpression)


def test_pp::textexpression_constructor_exists():
    assert callable(pp::TextExpression.__init__)


def test_pp::textexpression_constructor_args():
    sig = inspect.signature(pp::TextExpression.__init__)
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



def test_pp::unquotedstring_is_not_abstract():
    assert not inspect.isabstract(pp::UnquotedString)


def test_pp::unquotedstring_constructor_exists():
    assert callable(pp::UnquotedString.__init__)


def test_pp::unquotedstring_constructor_args():
    sig = inspect.signature(pp::UnquotedString.__init__)
    params = list(sig.parameters.keys())



def test_pp::singlequotedstring_is_not_abstract():
    assert not inspect.isabstract(pp::SingleQuotedString)


def test_pp::singlequotedstring_constructor_exists():
    assert callable(pp::SingleQuotedString.__init__)


def test_pp::singlequotedstring_constructor_args():
    sig = inspect.signature(pp::SingleQuotedString.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_pp::singlequotedstring_has_text():
    assert hasattr(pp::SingleQuotedString, "text")
    descriptor = None
    for klass in pp::SingleQuotedString.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_pp::doublequotedstring_is_not_abstract():
    assert not inspect.isabstract(pp::DoubleQuotedString)


def test_pp::doublequotedstring_constructor_exists():
    assert callable(pp::DoubleQuotedString.__init__)


def test_pp::doublequotedstring_constructor_args():
    sig = inspect.signature(pp::DoubleQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_withlambdaexpression_is_not_abstract():
    assert not inspect.isabstract(WithLambdaExpression)


def test_withlambdaexpression_constructor_exists():
    assert callable(WithLambdaExpression.__init__)


def test_withlambdaexpression_constructor_args():
    sig = inspect.signature(WithLambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::methodcall_is_not_abstract():
    assert not inspect.isabstract(pp::MethodCall)


def test_pp::methodcall_constructor_exists():
    assert callable(pp::MethodCall.__init__)


def test_pp::methodcall_constructor_args():
    sig = inspect.signature(pp::MethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "parenthesized" in params, "Missing parameter 'parenthesized'"

def test_pp::methodcall_has_parenthesized():
    assert hasattr(pp::MethodCall, "parenthesized")
    descriptor = None
    for klass in pp::MethodCall.__mro__:
        if "parenthesized" in klass.__dict__:
            descriptor = klass.__dict__["parenthesized"]
            break
    assert isinstance(descriptor, property)



def test_pp::functioncall_is_not_abstract():
    assert not inspect.isabstract(pp::FunctionCall)


def test_pp::functioncall_constructor_exists():
    assert callable(pp::FunctionCall.__init__)


def test_pp::functioncall_constructor_args():
    sig = inspect.signature(pp::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_pp::hashentry_is_not_abstract():
    assert not inspect.isabstract(pp::HashEntry)


def test_pp::hashentry_constructor_exists():
    assert callable(pp::HashEntry.__init__)


def test_pp::hashentry_constructor_args():
    sig = inspect.signature(pp::HashEntry.__init__)
    params = list(sig.parameters.keys())



def test_pp::iquotedstring_is_not_abstract():
    assert not inspect.isabstract(pp::IQuotedString)


def test_pp::iquotedstring_constructor_exists():
    assert callable(pp::IQuotedString.__init__)


def test_pp::iquotedstring_constructor_args():
    sig = inspect.signature(pp::IQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_parameterizedexpression_is_not_abstract():
    assert not inspect.isabstract(ParameterizedExpression)


def test_parameterizedexpression_constructor_exists():
    assert callable(ParameterizedExpression.__init__)


def test_parameterizedexpression_constructor_args():
    sig = inspect.signature(ParameterizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::withlambdaexpression_is_not_abstract():
    assert not inspect.isabstract(pp::WithLambdaExpression)


def test_pp::withlambdaexpression_constructor_exists():
    assert callable(pp::WithLambdaExpression.__init__)


def test_pp::withlambdaexpression_constructor_args():
    sig = inspect.signature(pp::WithLambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::selectorexpression_is_not_abstract():
    assert not inspect.isabstract(pp::SelectorExpression)


def test_pp::selectorexpression_constructor_exists():
    assert callable(pp::SelectorExpression.__init__)


def test_pp::selectorexpression_constructor_args():
    sig = inspect.signature(pp::SelectorExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::atexpression_is_not_abstract():
    assert not inspect.isabstract(pp::AtExpression)


def test_pp::atexpression_constructor_exists():
    assert callable(pp::AtExpression.__init__)


def test_pp::atexpression_constructor_args():
    sig = inspect.signature(pp::AtExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::namedaccessexpression_is_not_abstract():
    assert not inspect.isabstract(pp::NamedAccessExpression)


def test_pp::namedaccessexpression_constructor_exists():
    assert callable(pp::NamedAccessExpression.__init__)


def test_pp::namedaccessexpression_constructor_args():
    sig = inspect.signature(pp::NamedAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(pp::BinaryOpExpression)


def test_pp::binaryopexpression_constructor_exists():
    assert callable(pp::BinaryOpExpression.__init__)


def test_pp::binaryopexpression_constructor_args():
    sig = inspect.signature(pp::BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_pp::binaryopexpression_has_opName():
    assert hasattr(pp::BinaryOpExpression, "opName")
    descriptor = None
    for klass in pp::BinaryOpExpression.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_pp::appendexpression_is_not_abstract():
    assert not inspect.isabstract(pp::AppendExpression)


def test_pp::appendexpression_constructor_exists():
    assert callable(pp::AppendExpression.__init__)


def test_pp::appendexpression_constructor_args():
    sig = inspect.signature(pp::AppendExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::orexpression_is_not_abstract():
    assert not inspect.isabstract(pp::OrExpression)


def test_pp::orexpression_constructor_exists():
    assert callable(pp::OrExpression.__init__)


def test_pp::orexpression_constructor_args():
    sig = inspect.signature(pp::OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::selectorentry_is_not_abstract():
    assert not inspect.isabstract(pp::SelectorEntry)


def test_pp::selectorentry_constructor_exists():
    assert callable(pp::SelectorEntry.__init__)


def test_pp::selectorentry_constructor_args():
    sig = inspect.signature(pp::SelectorEntry.__init__)
    params = list(sig.parameters.keys())



def test_pp::andexpression_is_not_abstract():
    assert not inspect.isabstract(pp::AndExpression)


def test_pp::andexpression_constructor_exists():
    assert callable(pp::AndExpression.__init__)


def test_pp::andexpression_constructor_args():
    sig = inspect.signature(pp::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(pp::AssignmentExpression)


def test_pp::assignmentexpression_constructor_exists():
    assert callable(pp::AssignmentExpression.__init__)


def test_pp::assignmentexpression_constructor_args():
    sig = inspect.signature(pp::AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOpExpression)


def test_binaryopexpression_constructor_exists():
    assert callable(BinaryOpExpression.__init__)


def test_binaryopexpression_constructor_args():
    sig = inspect.signature(BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(pp::EqualityExpression)


def test_pp::equalityexpression_constructor_exists():
    assert callable(pp::EqualityExpression.__init__)


def test_pp::equalityexpression_constructor_args():
    sig = inspect.signature(pp::EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::additiveexpression_is_not_abstract():
    assert not inspect.isabstract(pp::AdditiveExpression)


def test_pp::additiveexpression_constructor_exists():
    assert callable(pp::AdditiveExpression.__init__)


def test_pp::additiveexpression_constructor_args():
    sig = inspect.signature(pp::AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(pp::ShiftExpression)


def test_pp::shiftexpression_constructor_exists():
    assert callable(pp::ShiftExpression.__init__)


def test_pp::shiftexpression_constructor_args():
    sig = inspect.signature(pp::ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::inexpression_is_not_abstract():
    assert not inspect.isabstract(pp::InExpression)


def test_pp::inexpression_constructor_exists():
    assert callable(pp::InExpression.__init__)


def test_pp::inexpression_constructor_args():
    sig = inspect.signature(pp::InExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(pp::MultiplicativeExpression)


def test_pp::multiplicativeexpression_constructor_exists():
    assert callable(pp::MultiplicativeExpression.__init__)


def test_pp::multiplicativeexpression_constructor_args():
    sig = inspect.signature(pp::MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::matchingexpression_is_not_abstract():
    assert not inspect.isabstract(pp::MatchingExpression)


def test_pp::matchingexpression_constructor_exists():
    assert callable(pp::MatchingExpression.__init__)


def test_pp::matchingexpression_constructor_args():
    sig = inspect.signature(pp::MatchingExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(pp::RelationalExpression)


def test_pp::relationalexpression_constructor_exists():
    assert callable(pp::RelationalExpression.__init__)


def test_pp::relationalexpression_constructor_args():
    sig = inspect.signature(pp::RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::relationshipexpression_is_not_abstract():
    assert not inspect.isabstract(pp::RelationshipExpression)


def test_pp::relationshipexpression_constructor_exists():
    assert callable(pp::RelationshipExpression.__init__)


def test_pp::relationshipexpression_constructor_args():
    sig = inspect.signature(pp::RelationshipExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::definitionargumentlist_is_not_abstract():
    assert not inspect.isabstract(pp::DefinitionArgumentList)


def test_pp::definitionargumentlist_constructor_exists():
    assert callable(pp::DefinitionArgumentList.__init__)


def test_pp::definitionargumentlist_constructor_args():
    sig = inspect.signature(pp::DefinitionArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_pp::resourceexpression_is_not_abstract():
    assert not inspect.isabstract(pp::ResourceExpression)


def test_pp::resourceexpression_constructor_exists():
    assert callable(pp::ResourceExpression.__init__)


def test_pp::resourceexpression_constructor_args():
    sig = inspect.signature(pp::ResourceExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::stringexpression_is_not_abstract():
    assert not inspect.isabstract(pp::StringExpression)


def test_pp::stringexpression_constructor_exists():
    assert callable(pp::StringExpression.__init__)


def test_pp::stringexpression_constructor_args():
    sig = inspect.signature(pp::StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(pp::UnaryExpression)


def test_pp::unaryexpression_constructor_exists():
    assert callable(pp::UnaryExpression.__init__)


def test_pp::unaryexpression_constructor_args():
    sig = inspect.signature(pp::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::parameterizedexpression_is_not_abstract():
    assert not inspect.isabstract(pp::ParameterizedExpression)


def test_pp::parameterizedexpression_constructor_exists():
    assert callable(pp::ParameterizedExpression.__init__)


def test_pp::parameterizedexpression_constructor_args():
    sig = inspect.signature(pp::ParameterizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::interpolatedvariable_is_not_abstract():
    assert not inspect.isabstract(pp::InterpolatedVariable)


def test_pp::interpolatedvariable_constructor_exists():
    assert callable(pp::InterpolatedVariable.__init__)


def test_pp::interpolatedvariable_constructor_args():
    sig = inspect.signature(pp::InterpolatedVariable.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_pp::interpolatedvariable_has_varName():
    assert hasattr(pp::InterpolatedVariable, "varName")
    descriptor = None
    for klass in pp::InterpolatedVariable.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_pp::exprlist_is_not_abstract():
    assert not inspect.isabstract(pp::ExprList)


def test_pp::exprlist_constructor_exists():
    assert callable(pp::ExprList.__init__)


def test_pp::exprlist_constructor_args():
    sig = inspect.signature(pp::ExprList.__init__)
    params = list(sig.parameters.keys())



def test_pp::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(pp::BinaryExpression)


def test_pp::binaryexpression_constructor_exists():
    assert callable(pp::BinaryExpression.__init__)


def test_pp::binaryexpression_constructor_args():
    sig = inspect.signature(pp::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::collectexpression_is_not_abstract():
    assert not inspect.isabstract(pp::CollectExpression)


def test_pp::collectexpression_constructor_exists():
    assert callable(pp::CollectExpression.__init__)


def test_pp::collectexpression_constructor_args():
    sig = inspect.signature(pp::CollectExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::importexpression_is_not_abstract():
    assert not inspect.isabstract(pp::ImportExpression)


def test_pp::importexpression_constructor_exists():
    assert callable(pp::ImportExpression.__init__)


def test_pp::importexpression_constructor_args():
    sig = inspect.signature(pp::ImportExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::unlessexpression_is_not_abstract():
    assert not inspect.isabstract(pp::UnlessExpression)


def test_pp::unlessexpression_constructor_exists():
    assert callable(pp::UnlessExpression.__init__)


def test_pp::unlessexpression_constructor_args():
    sig = inspect.signature(pp::UnlessExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::parenthesisedexpression_is_not_abstract():
    assert not inspect.isabstract(pp::ParenthesisedExpression)


def test_pp::parenthesisedexpression_constructor_exists():
    assert callable(pp::ParenthesisedExpression.__init__)


def test_pp::parenthesisedexpression_constructor_args():
    sig = inspect.signature(pp::ParenthesisedExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::expressionblock_is_not_abstract():
    assert not inspect.isabstract(pp::ExpressionBlock)


def test_pp::expressionblock_constructor_exists():
    assert callable(pp::ExpressionBlock.__init__)


def test_pp::expressionblock_constructor_args():
    sig = inspect.signature(pp::ExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_pp::nodedefinition_is_not_abstract():
    assert not inspect.isabstract(pp::NodeDefinition)


def test_pp::nodedefinition_constructor_exists():
    assert callable(pp::NodeDefinition.__init__)


def test_pp::nodedefinition_constructor_args():
    sig = inspect.signature(pp::NodeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_pp::separatorexpression_is_not_abstract():
    assert not inspect.isabstract(pp::SeparatorExpression)


def test_pp::separatorexpression_constructor_exists():
    assert callable(pp::SeparatorExpression.__init__)


def test_pp::separatorexpression_constructor_args():
    sig = inspect.signature(pp::SeparatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::variableexpression_is_not_abstract():
    assert not inspect.isabstract(pp::VariableExpression)


def test_pp::variableexpression_constructor_exists():
    assert callable(pp::VariableExpression.__init__)


def test_pp::variableexpression_constructor_args():
    sig = inspect.signature(pp::VariableExpression.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_pp::variableexpression_has_varName():
    assert hasattr(pp::VariableExpression, "varName")
    descriptor = None
    for klass in pp::VariableExpression.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_pp::definition_is_not_abstract():
    assert not inspect.isabstract(pp::Definition)


def test_pp::definition_constructor_exists():
    assert callable(pp::Definition.__init__)


def test_pp::definition_constructor_args():
    sig = inspect.signature(pp::Definition.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"

def test_pp::definition_has_className():
    assert hasattr(pp::Definition, "className")
    descriptor = None
    for klass in pp::Definition.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_pp::literalexpression_is_not_abstract():
    assert not inspect.isabstract(pp::LiteralExpression)


def test_pp::literalexpression_constructor_exists():
    assert callable(pp::LiteralExpression.__init__)


def test_pp::literalexpression_constructor_args():
    sig = inspect.signature(pp::LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_pp::hostclassdefinition_is_not_abstract():
    assert not inspect.isabstract(pp::HostClassDefinition)


def test_pp::hostclassdefinition_constructor_exists():
    assert callable(pp::HostClassDefinition.__init__)


def test_pp::hostclassdefinition_constructor_args():
    sig = inspect.signature(pp::HostClassDefinition.__init__)
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



def test_pp::exportedcollectquery_is_not_abstract():
    assert not inspect.isabstract(pp::ExportedCollectQuery)


def test_pp::exportedcollectquery_constructor_exists():
    assert callable(pp::ExportedCollectQuery.__init__)


def test_pp::exportedcollectquery_constructor_args():
    sig = inspect.signature(pp::ExportedCollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_pp::unaryminusexpression_is_not_abstract():
    assert not inspect.isabstract(pp::UnaryMinusExpression)


def test_pp::unaryminusexpression_constructor_exists():
    assert callable(pp::UnaryMinusExpression.__init__)


def test_pp::unaryminusexpression_constructor_args():
    sig = inspect.signature(pp::UnaryMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::unarynotexpression_is_not_abstract():
    assert not inspect.isabstract(pp::UnaryNotExpression)


def test_pp::unarynotexpression_constructor_exists():
    assert callable(pp::UnaryNotExpression.__init__)


def test_pp::unarynotexpression_constructor_args():
    sig = inspect.signature(pp::UnaryNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::virtualcollectquery_is_not_abstract():
    assert not inspect.isabstract(pp::VirtualCollectQuery)


def test_pp::virtualcollectquery_constructor_exists():
    assert callable(pp::VirtualCollectQuery.__init__)


def test_pp::virtualcollectquery_constructor_args():
    sig = inspect.signature(pp::VirtualCollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_pp::icollectquery_is_not_abstract():
    assert not inspect.isabstract(pp::ICollectQuery)


def test_pp::icollectquery_constructor_exists():
    assert callable(pp::ICollectQuery.__init__)


def test_pp::icollectquery_constructor_args():
    sig = inspect.signature(pp::ICollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::virtualnameorreference_is_not_abstract():
    assert not inspect.isabstract(pp::VirtualNameOrReference)


def test_pp::virtualnameorreference_constructor_exists():
    assert callable(pp::VirtualNameOrReference.__init__)


def test_pp::virtualnameorreference_constructor_args():
    sig = inspect.signature(pp::VirtualNameOrReference.__init__)
    params = list(sig.parameters.keys())
    assert "exported" in params, "Missing parameter 'exported'"
    assert "value" in params, "Missing parameter 'value'"

def test_pp::virtualnameorreference_has_exported():
    assert hasattr(pp::VirtualNameOrReference, "exported")
    descriptor = None
    for klass in pp::VirtualNameOrReference.__mro__:
        if "exported" in klass.__dict__:
            descriptor = klass.__dict__["exported"]
            break
    assert isinstance(descriptor, property)

def test_pp::virtualnameorreference_has_value():
    assert hasattr(pp::VirtualNameOrReference, "value")
    descriptor = None
    for klass in pp::VirtualNameOrReference.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp::literalname_is_not_abstract():
    assert not inspect.isabstract(pp::LiteralName)


def test_pp::literalname_constructor_exists():
    assert callable(pp::LiteralName.__init__)


def test_pp::literalname_constructor_args():
    sig = inspect.signature(pp::LiteralName.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp::literalname_has_value():
    assert hasattr(pp::LiteralName, "value")
    descriptor = None
    for klass in pp::LiteralName.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp::literalboolean_is_not_abstract():
    assert not inspect.isabstract(pp::LiteralBoolean)


def test_pp::literalboolean_constructor_exists():
    assert callable(pp::LiteralBoolean.__init__)


def test_pp::literalboolean_constructor_args():
    sig = inspect.signature(pp::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp::literalboolean_has_value():
    assert hasattr(pp::LiteralBoolean, "value")
    descriptor = None
    for klass in pp::LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp::literalclass_is_not_abstract():
    assert not inspect.isabstract(pp::LiteralClass)


def test_pp::literalclass_constructor_exists():
    assert callable(pp::LiteralClass.__init__)


def test_pp::literalclass_constructor_args():
    sig = inspect.signature(pp::LiteralClass.__init__)
    params = list(sig.parameters.keys())



def test_pp::literallist_is_not_abstract():
    assert not inspect.isabstract(pp::LiteralList)


def test_pp::literallist_constructor_exists():
    assert callable(pp::LiteralList.__init__)


def test_pp::literallist_constructor_args():
    sig = inspect.signature(pp::LiteralList.__init__)
    params = list(sig.parameters.keys())



def test_pp::literaldefault_is_not_abstract():
    assert not inspect.isabstract(pp::LiteralDefault)


def test_pp::literaldefault_constructor_exists():
    assert callable(pp::LiteralDefault.__init__)


def test_pp::literaldefault_constructor_args():
    sig = inspect.signature(pp::LiteralDefault.__init__)
    params = list(sig.parameters.keys())



def test_pp::literalundef_is_not_abstract():
    assert not inspect.isabstract(pp::LiteralUndef)


def test_pp::literalundef_constructor_exists():
    assert callable(pp::LiteralUndef.__init__)


def test_pp::literalundef_constructor_args():
    sig = inspect.signature(pp::LiteralUndef.__init__)
    params = list(sig.parameters.keys())



def test_pp::literalhash_is_not_abstract():
    assert not inspect.isabstract(pp::LiteralHash)


def test_pp::literalhash_constructor_exists():
    assert callable(pp::LiteralHash.__init__)


def test_pp::literalhash_constructor_args():
    sig = inspect.signature(pp::LiteralHash.__init__)
    params = list(sig.parameters.keys())



def test_pp::literalregex_is_not_abstract():
    assert not inspect.isabstract(pp::LiteralRegex)


def test_pp::literalregex_constructor_exists():
    assert callable(pp::LiteralRegex.__init__)


def test_pp::literalregex_constructor_args():
    sig = inspect.signature(pp::LiteralRegex.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp::literalregex_has_value():
    assert hasattr(pp::LiteralRegex, "value")
    descriptor = None
    for klass in pp::LiteralRegex.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp::literalnameorreference_is_not_abstract():
    assert not inspect.isabstract(pp::LiteralNameOrReference)


def test_pp::literalnameorreference_constructor_exists():
    assert callable(pp::LiteralNameOrReference.__init__)


def test_pp::literalnameorreference_constructor_args():
    sig = inspect.signature(pp::LiteralNameOrReference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp::literalnameorreference_has_value():
    assert hasattr(pp::LiteralNameOrReference, "value")
    descriptor = None
    for klass in pp::LiteralNameOrReference.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp::ifexpression_is_not_abstract():
    assert not inspect.isabstract(pp::IfExpression)


def test_pp::ifexpression_constructor_exists():
    assert callable(pp::IfExpression.__init__)


def test_pp::ifexpression_constructor_args():
    sig = inspect.signature(pp::IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::case_is_not_abstract():
    assert not inspect.isabstract(pp::Case)


def test_pp::case_constructor_exists():
    assert callable(pp::Case.__init__)


def test_pp::case_constructor_args():
    sig = inspect.signature(pp::Case.__init__)
    params = list(sig.parameters.keys())



def test_pp::caseexpression_is_not_abstract():
    assert not inspect.isabstract(pp::CaseExpression)


def test_pp::caseexpression_constructor_exists():
    assert callable(pp::CaseExpression.__init__)


def test_pp::caseexpression_constructor_args():
    sig = inspect.signature(pp::CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::definitionargument_is_not_abstract():
    assert not inspect.isabstract(pp::DefinitionArgument)


def test_pp::definitionargument_constructor_exists():
    assert callable(pp::DefinitionArgument.__init__)


def test_pp::definitionargument_constructor_args():
    sig = inspect.signature(pp::DefinitionArgument.__init__)
    params = list(sig.parameters.keys())
    assert "argName" in params, "Missing parameter 'argName'"
    assert "op" in params, "Missing parameter 'op'"

def test_pp::definitionargument_has_argName():
    assert hasattr(pp::DefinitionArgument, "argName")
    descriptor = None
    for klass in pp::DefinitionArgument.__mro__:
        if "argName" in klass.__dict__:
            descriptor = klass.__dict__["argName"]
            break
    assert isinstance(descriptor, property)

def test_pp::definitionargument_has_op():
    assert hasattr(pp::DefinitionArgument, "op")
    descriptor = None
    for klass in pp::DefinitionArgument.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_pp::attributeoperation_is_not_abstract():
    assert not inspect.isabstract(pp::AttributeOperation)


def test_pp::attributeoperation_constructor_exists():
    assert callable(pp::AttributeOperation.__init__)


def test_pp::attributeoperation_constructor_args():
    sig = inspect.signature(pp::AttributeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "key" in params, "Missing parameter 'key'"

def test_pp::attributeoperation_has_op():
    assert hasattr(pp::AttributeOperation, "op")
    descriptor = None
    for klass in pp::AttributeOperation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_pp::attributeoperation_has_key():
    assert hasattr(pp::AttributeOperation, "key")
    descriptor = None
    for klass in pp::AttributeOperation.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_pp::attributeoperations_is_not_abstract():
    assert not inspect.isabstract(pp::AttributeOperations)


def test_pp::attributeoperations_constructor_exists():
    assert callable(pp::AttributeOperations.__init__)


def test_pp::attributeoperations_constructor_args():
    sig = inspect.signature(pp::AttributeOperations.__init__)
    params = list(sig.parameters.keys())



def test_pp::resourcebody_is_not_abstract():
    assert not inspect.isabstract(pp::ResourceBody)


def test_pp::resourcebody_constructor_exists():
    assert callable(pp::ResourceBody.__init__)


def test_pp::resourcebody_constructor_args():
    sig = inspect.signature(pp::ResourceBody.__init__)
    params = list(sig.parameters.keys())



def test_pp::expression_is_not_abstract():
    assert not inspect.isabstract(pp::Expression)


def test_pp::expression_constructor_exists():
    assert callable(pp::Expression.__init__)


def test_pp::expression_constructor_args():
    sig = inspect.signature(pp::Expression.__init__)
    params = list(sig.parameters.keys())



def test_expressionblock_is_not_abstract():
    assert not inspect.isabstract(ExpressionBlock)


def test_expressionblock_constructor_exists():
    assert callable(ExpressionBlock.__init__)


def test_expressionblock_constructor_args():
    sig = inspect.signature(ExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_pp::lambda_is_not_abstract():
    assert not inspect.isabstract(pp::Lambda)


def test_pp::lambda_constructor_exists():
    assert callable(pp::Lambda.__init__)


def test_pp::lambda_constructor_args():
    sig = inspect.signature(pp::Lambda.__init__)
    params = list(sig.parameters.keys())



def test_pp::elseexpression_is_not_abstract():
    assert not inspect.isabstract(pp::ElseExpression)


def test_pp::elseexpression_constructor_exists():
    assert callable(pp::ElseExpression.__init__)


def test_pp::elseexpression_constructor_args():
    sig = inspect.signature(pp::ElseExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp::puppetmanifest_is_not_abstract():
    assert not inspect.isabstract(pp::PuppetManifest)


def test_pp::puppetmanifest_constructor_exists():
    assert callable(pp::PuppetManifest.__init__)


def test_pp::puppetmanifest_constructor_args():
    sig = inspect.signature(pp::PuppetManifest.__init__)
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
Lambda_strategy = st.builds(
    Lambda,
)
pp::RubyLambda_strategy = st.builds(
    pp::RubyLambda,
)
pp::JavaLambda_strategy = st.builds(
    pp::JavaLambda,
    farrow=
        st.booleans()
)
IfExpression_strategy = st.builds(
    IfExpression,
)
pp::ElseIfExpression_strategy = st.builds(
    pp::ElseIfExpression,
)
TextExpression_strategy = st.builds(
    TextExpression,
)
pp::ExpressionTE_strategy = st.builds(
    pp::ExpressionTE,
)
pp::VariableTE_strategy = st.builds(
    pp::VariableTE,
    varName=
        safe_text
)
pp::VerbatimTE_strategy = st.builds(
    pp::VerbatimTE,
    text=
        safe_text
)
pp::TextExpression_strategy = st.builds(
    pp::TextExpression,
)
IQuotedString_strategy = st.builds(
    IQuotedString,
)
StringExpression_strategy = st.builds(
    StringExpression,
)
pp::UnquotedString_strategy = st.builds(
    pp::UnquotedString,
)
pp::SingleQuotedString_strategy = st.builds(
    pp::SingleQuotedString,
    text=
        safe_text
)
pp::DoubleQuotedString_strategy = st.builds(
    pp::DoubleQuotedString,
)
WithLambdaExpression_strategy = st.builds(
    WithLambdaExpression,
)
pp::MethodCall_strategy = st.builds(
    pp::MethodCall,
    parenthesized=
        st.booleans()
)
pp::FunctionCall_strategy = st.builds(
    pp::FunctionCall,
)
pp::HashEntry_strategy = st.builds(
    pp::HashEntry,
)
pp::IQuotedString_strategy = st.builds(
    pp::IQuotedString,
)
ParameterizedExpression_strategy = st.builds(
    ParameterizedExpression,
)
pp::WithLambdaExpression_strategy = st.builds(
    pp::WithLambdaExpression,
)
pp::SelectorExpression_strategy = st.builds(
    pp::SelectorExpression,
)
pp::AtExpression_strategy = st.builds(
    pp::AtExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
pp::NamedAccessExpression_strategy = st.builds(
    pp::NamedAccessExpression,
)
pp::BinaryOpExpression_strategy = st.builds(
    pp::BinaryOpExpression,
    opName=
        safe_text
)
pp::AppendExpression_strategy = st.builds(
    pp::AppendExpression,
)
pp::OrExpression_strategy = st.builds(
    pp::OrExpression,
)
pp::SelectorEntry_strategy = st.builds(
    pp::SelectorEntry,
)
pp::AndExpression_strategy = st.builds(
    pp::AndExpression,
)
pp::AssignmentExpression_strategy = st.builds(
    pp::AssignmentExpression,
)
BinaryOpExpression_strategy = st.builds(
    BinaryOpExpression,
)
pp::EqualityExpression_strategy = st.builds(
    pp::EqualityExpression,
)
pp::AdditiveExpression_strategy = st.builds(
    pp::AdditiveExpression,
)
pp::ShiftExpression_strategy = st.builds(
    pp::ShiftExpression,
)
pp::InExpression_strategy = st.builds(
    pp::InExpression,
)
pp::MultiplicativeExpression_strategy = st.builds(
    pp::MultiplicativeExpression,
)
pp::MatchingExpression_strategy = st.builds(
    pp::MatchingExpression,
)
pp::RelationalExpression_strategy = st.builds(
    pp::RelationalExpression,
)
pp::RelationshipExpression_strategy = st.builds(
    pp::RelationshipExpression,
)
pp::DefinitionArgumentList_strategy = st.builds(
    pp::DefinitionArgumentList,
)
Expression_strategy = st.builds(
    Expression,
)
pp::ResourceExpression_strategy = st.builds(
    pp::ResourceExpression,
)
pp::StringExpression_strategy = st.builds(
    pp::StringExpression,
)
pp::UnaryExpression_strategy = st.builds(
    pp::UnaryExpression,
)
pp::ParameterizedExpression_strategy = st.builds(
    pp::ParameterizedExpression,
)
pp::InterpolatedVariable_strategy = st.builds(
    pp::InterpolatedVariable,
    varName=
        safe_text
)
pp::ExprList_strategy = st.builds(
    pp::ExprList,
)
pp::BinaryExpression_strategy = st.builds(
    pp::BinaryExpression,
)
pp::CollectExpression_strategy = st.builds(
    pp::CollectExpression,
)
pp::ImportExpression_strategy = st.builds(
    pp::ImportExpression,
)
pp::UnlessExpression_strategy = st.builds(
    pp::UnlessExpression,
)
pp::ParenthesisedExpression_strategy = st.builds(
    pp::ParenthesisedExpression,
)
pp::ExpressionBlock_strategy = st.builds(
    pp::ExpressionBlock,
)
pp::NodeDefinition_strategy = st.builds(
    pp::NodeDefinition,
)
pp::SeparatorExpression_strategy = st.builds(
    pp::SeparatorExpression,
)
pp::VariableExpression_strategy = st.builds(
    pp::VariableExpression,
    varName=
        safe_text
)
pp::Definition_strategy = st.builds(
    pp::Definition,
    className=
        safe_text
)
pp::LiteralExpression_strategy = st.builds(
    pp::LiteralExpression,
)
Definition_strategy = st.builds(
    Definition,
)
pp::HostClassDefinition_strategy = st.builds(
    pp::HostClassDefinition,
)
ICollectQuery_strategy = st.builds(
    ICollectQuery,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
pp::ExportedCollectQuery_strategy = st.builds(
    pp::ExportedCollectQuery,
)
pp::UnaryMinusExpression_strategy = st.builds(
    pp::UnaryMinusExpression,
)
pp::UnaryNotExpression_strategy = st.builds(
    pp::UnaryNotExpression,
)
pp::VirtualCollectQuery_strategy = st.builds(
    pp::VirtualCollectQuery,
)
pp::ICollectQuery_strategy = st.builds(
    pp::ICollectQuery,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
pp::VirtualNameOrReference_strategy = st.builds(
    pp::VirtualNameOrReference,
    exported=
        st.booleans(),
    value=
        safe_text
)
pp::LiteralName_strategy = st.builds(
    pp::LiteralName,
    value=
        safe_text
)
pp::LiteralBoolean_strategy = st.builds(
    pp::LiteralBoolean,
    value=
        st.booleans()
)
pp::LiteralClass_strategy = st.builds(
    pp::LiteralClass,
)
pp::LiteralList_strategy = st.builds(
    pp::LiteralList,
)
pp::LiteralDefault_strategy = st.builds(
    pp::LiteralDefault,
)
pp::LiteralUndef_strategy = st.builds(
    pp::LiteralUndef,
)
pp::LiteralHash_strategy = st.builds(
    pp::LiteralHash,
)
pp::LiteralRegex_strategy = st.builds(
    pp::LiteralRegex,
    value=
        safe_text
)
pp::LiteralNameOrReference_strategy = st.builds(
    pp::LiteralNameOrReference,
    value=
        safe_text
)
pp::IfExpression_strategy = st.builds(
    pp::IfExpression,
)
pp::Case_strategy = st.builds(
    pp::Case,
)
pp::CaseExpression_strategy = st.builds(
    pp::CaseExpression,
)
pp::DefinitionArgument_strategy = st.builds(
    pp::DefinitionArgument,
    argName=
        safe_text,
    op=
        safe_text
)
pp::AttributeOperation_strategy = st.builds(
    pp::AttributeOperation,
    op=
        safe_text,
    key=
        safe_text
)
pp::AttributeOperations_strategy = st.builds(
    pp::AttributeOperations,
)
pp::ResourceBody_strategy = st.builds(
    pp::ResourceBody,
)
pp::Expression_strategy = st.builds(
    pp::Expression,
)
ExpressionBlock_strategy = st.builds(
    ExpressionBlock,
)
pp::Lambda_strategy = st.builds(
    pp::Lambda,
)
pp::ElseExpression_strategy = st.builds(
    pp::ElseExpression,
)
pp::PuppetManifest_strategy = st.builds(
    pp::PuppetManifest,
)

@given(instance=Lambda_strategy)
@settings(max_examples=50)
def test_lambda_instantiation(instance):
    assert isinstance(instance, Lambda)

@given(instance=pp::RubyLambda_strategy)
@settings(max_examples=50)
def test_pp::rubylambda_instantiation(instance):
    assert isinstance(instance, pp::RubyLambda)

@given(instance=pp::JavaLambda_strategy)
@settings(max_examples=50)
def test_pp::javalambda_instantiation(instance):
    assert isinstance(instance, pp::JavaLambda)

@given(instance=pp::JavaLambda_strategy)
def test_pp::javalambda_farrow_type(instance):
    assert isinstance(instance.farrow, bool)


@given(instance=pp::JavaLambda_strategy)
def test_pp::javalambda_farrow_setter(instance):
    original = instance.farrow
    instance.farrow = original
    assert instance.farrow == original

@given(instance=IfExpression_strategy)
@settings(max_examples=50)
def test_ifexpression_instantiation(instance):
    assert isinstance(instance, IfExpression)

@given(instance=pp::ElseIfExpression_strategy)
@settings(max_examples=50)
def test_pp::elseifexpression_instantiation(instance):
    assert isinstance(instance, pp::ElseIfExpression)

@given(instance=TextExpression_strategy)
@settings(max_examples=50)
def test_textexpression_instantiation(instance):
    assert isinstance(instance, TextExpression)

@given(instance=pp::ExpressionTE_strategy)
@settings(max_examples=50)
def test_pp::expressionte_instantiation(instance):
    assert isinstance(instance, pp::ExpressionTE)

@given(instance=pp::VariableTE_strategy)
@settings(max_examples=50)
def test_pp::variablete_instantiation(instance):
    assert isinstance(instance, pp::VariableTE)

@given(instance=pp::VariableTE_strategy)
def test_pp::variablete_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=pp::VariableTE_strategy)
def test_pp::variablete_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=pp::VerbatimTE_strategy)
@settings(max_examples=50)
def test_pp::verbatimte_instantiation(instance):
    assert isinstance(instance, pp::VerbatimTE)

@given(instance=pp::VerbatimTE_strategy)
def test_pp::verbatimte_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=pp::VerbatimTE_strategy)
def test_pp::verbatimte_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=pp::TextExpression_strategy)
@settings(max_examples=50)
def test_pp::textexpression_instantiation(instance):
    assert isinstance(instance, pp::TextExpression)

@given(instance=IQuotedString_strategy)
@settings(max_examples=50)
def test_iquotedstring_instantiation(instance):
    assert isinstance(instance, IQuotedString)

@given(instance=StringExpression_strategy)
@settings(max_examples=50)
def test_stringexpression_instantiation(instance):
    assert isinstance(instance, StringExpression)

@given(instance=pp::UnquotedString_strategy)
@settings(max_examples=50)
def test_pp::unquotedstring_instantiation(instance):
    assert isinstance(instance, pp::UnquotedString)

@given(instance=pp::SingleQuotedString_strategy)
@settings(max_examples=50)
def test_pp::singlequotedstring_instantiation(instance):
    assert isinstance(instance, pp::SingleQuotedString)

@given(instance=pp::SingleQuotedString_strategy)
def test_pp::singlequotedstring_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=pp::SingleQuotedString_strategy)
def test_pp::singlequotedstring_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=pp::DoubleQuotedString_strategy)
@settings(max_examples=50)
def test_pp::doublequotedstring_instantiation(instance):
    assert isinstance(instance, pp::DoubleQuotedString)

@given(instance=WithLambdaExpression_strategy)
@settings(max_examples=50)
def test_withlambdaexpression_instantiation(instance):
    assert isinstance(instance, WithLambdaExpression)

@given(instance=pp::MethodCall_strategy)
@settings(max_examples=50)
def test_pp::methodcall_instantiation(instance):
    assert isinstance(instance, pp::MethodCall)

@given(instance=pp::MethodCall_strategy)
def test_pp::methodcall_parenthesized_type(instance):
    assert isinstance(instance.parenthesized, bool)


@given(instance=pp::MethodCall_strategy)
def test_pp::methodcall_parenthesized_setter(instance):
    original = instance.parenthesized
    instance.parenthesized = original
    assert instance.parenthesized == original

@given(instance=pp::FunctionCall_strategy)
@settings(max_examples=50)
def test_pp::functioncall_instantiation(instance):
    assert isinstance(instance, pp::FunctionCall)

@given(instance=pp::HashEntry_strategy)
@settings(max_examples=50)
def test_pp::hashentry_instantiation(instance):
    assert isinstance(instance, pp::HashEntry)

@given(instance=pp::IQuotedString_strategy)
@settings(max_examples=50)
def test_pp::iquotedstring_instantiation(instance):
    assert isinstance(instance, pp::IQuotedString)

@given(instance=ParameterizedExpression_strategy)
@settings(max_examples=50)
def test_parameterizedexpression_instantiation(instance):
    assert isinstance(instance, ParameterizedExpression)

@given(instance=pp::WithLambdaExpression_strategy)
@settings(max_examples=50)
def test_pp::withlambdaexpression_instantiation(instance):
    assert isinstance(instance, pp::WithLambdaExpression)

@given(instance=pp::SelectorExpression_strategy)
@settings(max_examples=50)
def test_pp::selectorexpression_instantiation(instance):
    assert isinstance(instance, pp::SelectorExpression)

@given(instance=pp::AtExpression_strategy)
@settings(max_examples=50)
def test_pp::atexpression_instantiation(instance):
    assert isinstance(instance, pp::AtExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=pp::NamedAccessExpression_strategy)
@settings(max_examples=50)
def test_pp::namedaccessexpression_instantiation(instance):
    assert isinstance(instance, pp::NamedAccessExpression)

@given(instance=pp::BinaryOpExpression_strategy)
@settings(max_examples=50)
def test_pp::binaryopexpression_instantiation(instance):
    assert isinstance(instance, pp::BinaryOpExpression)

@given(instance=pp::BinaryOpExpression_strategy)
def test_pp::binaryopexpression_opName_type(instance):
    assert isinstance(instance.opName, str)


@given(instance=pp::BinaryOpExpression_strategy)
def test_pp::binaryopexpression_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=pp::AppendExpression_strategy)
@settings(max_examples=50)
def test_pp::appendexpression_instantiation(instance):
    assert isinstance(instance, pp::AppendExpression)

@given(instance=pp::OrExpression_strategy)
@settings(max_examples=50)
def test_pp::orexpression_instantiation(instance):
    assert isinstance(instance, pp::OrExpression)

@given(instance=pp::SelectorEntry_strategy)
@settings(max_examples=50)
def test_pp::selectorentry_instantiation(instance):
    assert isinstance(instance, pp::SelectorEntry)

@given(instance=pp::AndExpression_strategy)
@settings(max_examples=50)
def test_pp::andexpression_instantiation(instance):
    assert isinstance(instance, pp::AndExpression)

@given(instance=pp::AssignmentExpression_strategy)
@settings(max_examples=50)
def test_pp::assignmentexpression_instantiation(instance):
    assert isinstance(instance, pp::AssignmentExpression)

@given(instance=BinaryOpExpression_strategy)
@settings(max_examples=50)
def test_binaryopexpression_instantiation(instance):
    assert isinstance(instance, BinaryOpExpression)

@given(instance=pp::EqualityExpression_strategy)
@settings(max_examples=50)
def test_pp::equalityexpression_instantiation(instance):
    assert isinstance(instance, pp::EqualityExpression)

@given(instance=pp::AdditiveExpression_strategy)
@settings(max_examples=50)
def test_pp::additiveexpression_instantiation(instance):
    assert isinstance(instance, pp::AdditiveExpression)

@given(instance=pp::ShiftExpression_strategy)
@settings(max_examples=50)
def test_pp::shiftexpression_instantiation(instance):
    assert isinstance(instance, pp::ShiftExpression)

@given(instance=pp::InExpression_strategy)
@settings(max_examples=50)
def test_pp::inexpression_instantiation(instance):
    assert isinstance(instance, pp::InExpression)

@given(instance=pp::MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_pp::multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, pp::MultiplicativeExpression)

@given(instance=pp::MatchingExpression_strategy)
@settings(max_examples=50)
def test_pp::matchingexpression_instantiation(instance):
    assert isinstance(instance, pp::MatchingExpression)

@given(instance=pp::RelationalExpression_strategy)
@settings(max_examples=50)
def test_pp::relationalexpression_instantiation(instance):
    assert isinstance(instance, pp::RelationalExpression)

@given(instance=pp::RelationshipExpression_strategy)
@settings(max_examples=50)
def test_pp::relationshipexpression_instantiation(instance):
    assert isinstance(instance, pp::RelationshipExpression)

@given(instance=pp::DefinitionArgumentList_strategy)
@settings(max_examples=50)
def test_pp::definitionargumentlist_instantiation(instance):
    assert isinstance(instance, pp::DefinitionArgumentList)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=pp::ResourceExpression_strategy)
@settings(max_examples=50)
def test_pp::resourceexpression_instantiation(instance):
    assert isinstance(instance, pp::ResourceExpression)

@given(instance=pp::StringExpression_strategy)
@settings(max_examples=50)
def test_pp::stringexpression_instantiation(instance):
    assert isinstance(instance, pp::StringExpression)

@given(instance=pp::UnaryExpression_strategy)
@settings(max_examples=50)
def test_pp::unaryexpression_instantiation(instance):
    assert isinstance(instance, pp::UnaryExpression)

@given(instance=pp::ParameterizedExpression_strategy)
@settings(max_examples=50)
def test_pp::parameterizedexpression_instantiation(instance):
    assert isinstance(instance, pp::ParameterizedExpression)

@given(instance=pp::InterpolatedVariable_strategy)
@settings(max_examples=50)
def test_pp::interpolatedvariable_instantiation(instance):
    assert isinstance(instance, pp::InterpolatedVariable)

@given(instance=pp::InterpolatedVariable_strategy)
def test_pp::interpolatedvariable_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=pp::InterpolatedVariable_strategy)
def test_pp::interpolatedvariable_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=pp::ExprList_strategy)
@settings(max_examples=50)
def test_pp::exprlist_instantiation(instance):
    assert isinstance(instance, pp::ExprList)

@given(instance=pp::BinaryExpression_strategy)
@settings(max_examples=50)
def test_pp::binaryexpression_instantiation(instance):
    assert isinstance(instance, pp::BinaryExpression)

@given(instance=pp::CollectExpression_strategy)
@settings(max_examples=50)
def test_pp::collectexpression_instantiation(instance):
    assert isinstance(instance, pp::CollectExpression)

@given(instance=pp::ImportExpression_strategy)
@settings(max_examples=50)
def test_pp::importexpression_instantiation(instance):
    assert isinstance(instance, pp::ImportExpression)

@given(instance=pp::UnlessExpression_strategy)
@settings(max_examples=50)
def test_pp::unlessexpression_instantiation(instance):
    assert isinstance(instance, pp::UnlessExpression)

@given(instance=pp::ParenthesisedExpression_strategy)
@settings(max_examples=50)
def test_pp::parenthesisedexpression_instantiation(instance):
    assert isinstance(instance, pp::ParenthesisedExpression)

@given(instance=pp::ExpressionBlock_strategy)
@settings(max_examples=50)
def test_pp::expressionblock_instantiation(instance):
    assert isinstance(instance, pp::ExpressionBlock)

@given(instance=pp::NodeDefinition_strategy)
@settings(max_examples=50)
def test_pp::nodedefinition_instantiation(instance):
    assert isinstance(instance, pp::NodeDefinition)

@given(instance=pp::SeparatorExpression_strategy)
@settings(max_examples=50)
def test_pp::separatorexpression_instantiation(instance):
    assert isinstance(instance, pp::SeparatorExpression)

@given(instance=pp::VariableExpression_strategy)
@settings(max_examples=50)
def test_pp::variableexpression_instantiation(instance):
    assert isinstance(instance, pp::VariableExpression)

@given(instance=pp::VariableExpression_strategy)
def test_pp::variableexpression_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=pp::VariableExpression_strategy)
def test_pp::variableexpression_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=pp::Definition_strategy)
@settings(max_examples=50)
def test_pp::definition_instantiation(instance):
    assert isinstance(instance, pp::Definition)

@given(instance=pp::Definition_strategy)
def test_pp::definition_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=pp::Definition_strategy)
def test_pp::definition_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=pp::LiteralExpression_strategy)
@settings(max_examples=50)
def test_pp::literalexpression_instantiation(instance):
    assert isinstance(instance, pp::LiteralExpression)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=pp::HostClassDefinition_strategy)
@settings(max_examples=50)
def test_pp::hostclassdefinition_instantiation(instance):
    assert isinstance(instance, pp::HostClassDefinition)

@given(instance=ICollectQuery_strategy)
@settings(max_examples=50)
def test_icollectquery_instantiation(instance):
    assert isinstance(instance, ICollectQuery)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=pp::ExportedCollectQuery_strategy)
@settings(max_examples=50)
def test_pp::exportedcollectquery_instantiation(instance):
    assert isinstance(instance, pp::ExportedCollectQuery)

@given(instance=pp::UnaryMinusExpression_strategy)
@settings(max_examples=50)
def test_pp::unaryminusexpression_instantiation(instance):
    assert isinstance(instance, pp::UnaryMinusExpression)

@given(instance=pp::UnaryNotExpression_strategy)
@settings(max_examples=50)
def test_pp::unarynotexpression_instantiation(instance):
    assert isinstance(instance, pp::UnaryNotExpression)

@given(instance=pp::VirtualCollectQuery_strategy)
@settings(max_examples=50)
def test_pp::virtualcollectquery_instantiation(instance):
    assert isinstance(instance, pp::VirtualCollectQuery)

@given(instance=pp::ICollectQuery_strategy)
@settings(max_examples=50)
def test_pp::icollectquery_instantiation(instance):
    assert isinstance(instance, pp::ICollectQuery)

@given(instance=LiteralExpression_strategy)
@settings(max_examples=50)
def test_literalexpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)

@given(instance=pp::VirtualNameOrReference_strategy)
@settings(max_examples=50)
def test_pp::virtualnameorreference_instantiation(instance):
    assert isinstance(instance, pp::VirtualNameOrReference)

@given(instance=pp::VirtualNameOrReference_strategy)
def test_pp::virtualnameorreference_exported_type(instance):
    assert isinstance(instance.exported, bool)


@given(instance=pp::VirtualNameOrReference_strategy)
def test_pp::virtualnameorreference_exported_setter(instance):
    original = instance.exported
    instance.exported = original
    assert instance.exported == original

@given(instance=pp::VirtualNameOrReference_strategy)
def test_pp::virtualnameorreference_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pp::VirtualNameOrReference_strategy)
def test_pp::virtualnameorreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp::LiteralName_strategy)
@settings(max_examples=50)
def test_pp::literalname_instantiation(instance):
    assert isinstance(instance, pp::LiteralName)

@given(instance=pp::LiteralName_strategy)
def test_pp::literalname_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pp::LiteralName_strategy)
def test_pp::literalname_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_pp::literalboolean_instantiation(instance):
    assert isinstance(instance, pp::LiteralBoolean)

@given(instance=pp::LiteralBoolean_strategy)
def test_pp::literalboolean_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=pp::LiteralBoolean_strategy)
def test_pp::literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp::LiteralClass_strategy)
@settings(max_examples=50)
def test_pp::literalclass_instantiation(instance):
    assert isinstance(instance, pp::LiteralClass)

@given(instance=pp::LiteralList_strategy)
@settings(max_examples=50)
def test_pp::literallist_instantiation(instance):
    assert isinstance(instance, pp::LiteralList)

@given(instance=pp::LiteralDefault_strategy)
@settings(max_examples=50)
def test_pp::literaldefault_instantiation(instance):
    assert isinstance(instance, pp::LiteralDefault)

@given(instance=pp::LiteralUndef_strategy)
@settings(max_examples=50)
def test_pp::literalundef_instantiation(instance):
    assert isinstance(instance, pp::LiteralUndef)

@given(instance=pp::LiteralHash_strategy)
@settings(max_examples=50)
def test_pp::literalhash_instantiation(instance):
    assert isinstance(instance, pp::LiteralHash)

@given(instance=pp::LiteralRegex_strategy)
@settings(max_examples=50)
def test_pp::literalregex_instantiation(instance):
    assert isinstance(instance, pp::LiteralRegex)

@given(instance=pp::LiteralRegex_strategy)
def test_pp::literalregex_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pp::LiteralRegex_strategy)
def test_pp::literalregex_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp::LiteralNameOrReference_strategy)
@settings(max_examples=50)
def test_pp::literalnameorreference_instantiation(instance):
    assert isinstance(instance, pp::LiteralNameOrReference)

@given(instance=pp::LiteralNameOrReference_strategy)
def test_pp::literalnameorreference_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pp::LiteralNameOrReference_strategy)
def test_pp::literalnameorreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp::IfExpression_strategy)
@settings(max_examples=50)
def test_pp::ifexpression_instantiation(instance):
    assert isinstance(instance, pp::IfExpression)

@given(instance=pp::Case_strategy)
@settings(max_examples=50)
def test_pp::case_instantiation(instance):
    assert isinstance(instance, pp::Case)

@given(instance=pp::CaseExpression_strategy)
@settings(max_examples=50)
def test_pp::caseexpression_instantiation(instance):
    assert isinstance(instance, pp::CaseExpression)

@given(instance=pp::DefinitionArgument_strategy)
@settings(max_examples=50)
def test_pp::definitionargument_instantiation(instance):
    assert isinstance(instance, pp::DefinitionArgument)

@given(instance=pp::DefinitionArgument_strategy)
def test_pp::definitionargument_argName_type(instance):
    assert isinstance(instance.argName, str)


@given(instance=pp::DefinitionArgument_strategy)
def test_pp::definitionargument_argName_setter(instance):
    original = instance.argName
    instance.argName = original
    assert instance.argName == original

@given(instance=pp::DefinitionArgument_strategy)
def test_pp::definitionargument_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=pp::DefinitionArgument_strategy)
def test_pp::definitionargument_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=pp::AttributeOperation_strategy)
@settings(max_examples=50)
def test_pp::attributeoperation_instantiation(instance):
    assert isinstance(instance, pp::AttributeOperation)

@given(instance=pp::AttributeOperation_strategy)
def test_pp::attributeoperation_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=pp::AttributeOperation_strategy)
def test_pp::attributeoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=pp::AttributeOperation_strategy)
def test_pp::attributeoperation_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=pp::AttributeOperation_strategy)
def test_pp::attributeoperation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=pp::AttributeOperations_strategy)
@settings(max_examples=50)
def test_pp::attributeoperations_instantiation(instance):
    assert isinstance(instance, pp::AttributeOperations)

@given(instance=pp::ResourceBody_strategy)
@settings(max_examples=50)
def test_pp::resourcebody_instantiation(instance):
    assert isinstance(instance, pp::ResourceBody)

@given(instance=pp::Expression_strategy)
@settings(max_examples=50)
def test_pp::expression_instantiation(instance):
    assert isinstance(instance, pp::Expression)

@given(instance=ExpressionBlock_strategy)
@settings(max_examples=50)
def test_expressionblock_instantiation(instance):
    assert isinstance(instance, ExpressionBlock)

@given(instance=pp::Lambda_strategy)
@settings(max_examples=50)
def test_pp::lambda_instantiation(instance):
    assert isinstance(instance, pp::Lambda)

@given(instance=pp::ElseExpression_strategy)
@settings(max_examples=50)
def test_pp::elseexpression_instantiation(instance):
    assert isinstance(instance, pp::ElseExpression)

@given(instance=pp::PuppetManifest_strategy)
@settings(max_examples=50)
def test_pp::puppetmanifest_instantiation(instance):
    assert isinstance(instance, pp::PuppetManifest)
