import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Lambda,
    pp2::RubyLambda,
    pp2::JavaLambda,
    IfExpression,
    pp2::ElseIfExpression,
    TextExpression,
    pp2::VariableTE,
    pp2::ExpressionTE,
    pp2::VerbatimTE,
    pp2::TextExpression,
    IQuotedString,
    StringExpression,
    pp2::UnquotedString,
    pp2::SingleQuotedString,
    pp2::DoubleQuotedString,
    WithLambdaExpression,
    pp2::MethodCall,
    pp2::FunctionCall,
    ParameterizedExpression,
    pp2::SelectorExpression,
    pp2::AtExpression,
    pp2::WithLambdaExpression,
    pp2::HashEntry,
    pp2::IQuotedString,
    LiteralExpression,
    pp2::VirtualNameOrReference,
    pp2::LiteralClass,
    pp2::LiteralHash,
    pp2::LiteralList,
    pp2::LiteralNameOrReference,
    BinaryExpression,
    pp2::NamedAccessExpression,
    pp2::AndExpression,
    pp2::BinaryOpExpression,
    pp2::AppendExpression,
    pp2::OrExpression,
    pp2::SelectorEntry,
    pp2::AssignmentExpression,
    BinaryOpExpression,
    pp2::RelationalExpression,
    pp2::AdditiveExpression,
    pp2::ShiftExpression,
    pp2::MultiplicativeExpression,
    pp2::EqualityExpression,
    pp2::MatchingExpression,
    pp2::InExpression,
    pp2::RelationshipExpression,
    pp2::LiteralName,
    pp2::LiteralRegex,
    pp2::LiteralDefault,
    pp2::LiteralUndef,
    pp2::LiteralBoolean,
    Definition,
    pp2::HostClassDefinition,
    ICollectQuery,
    UnaryExpression,
    pp2::UnaryNotExpression,
    pp2::ExportedCollectQuery,
    pp2::UnaryMinusExpression,
    pp2::VirtualCollectQuery,
    pp2::ICollectQuery,
    pp2::AttributeOperation,
    pp2::AttributeOperations,
    pp2::ResourceBody,
    pp2::Expression,
    ExpressionBlock,
    pp2::IfExpression,
    pp2::Lambda,
    pp2::ElseExpression,
    pp2::UnlessExpression,
    pp2::Definition,
    pp2::NodeDefinition,
    pp2::Case,
    Expression,
    pp2::ExpressionBlock,
    pp2::LiteralExpression,
    pp2::ResourceExpression,
    pp2::InterpolatedVariable,
    pp2::VariableExpression,
    pp2::ExprList,
    pp2::UnaryExpression,
    pp2::BinaryExpression,
    pp2::ImportExpression,
    pp2::ParenthesisedExpression,
    pp2::SeparatorExpression,
    pp2::StringExpression,
    pp2::ParameterizedExpression,
    pp2::CollectExpression,
    pp2::CaseExpression,
    pp2::DefinitionArgument,
    pp2::DefinitionArgumentList,
    pp2::PuppetManifest,
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



def test_pp2::rubylambda_is_not_abstract():
    assert not inspect.isabstract(pp2::RubyLambda)


def test_pp2::rubylambda_constructor_exists():
    assert callable(pp2::RubyLambda.__init__)


def test_pp2::rubylambda_constructor_args():
    sig = inspect.signature(pp2::RubyLambda.__init__)
    params = list(sig.parameters.keys())



def test_pp2::javalambda_is_not_abstract():
    assert not inspect.isabstract(pp2::JavaLambda)


def test_pp2::javalambda_constructor_exists():
    assert callable(pp2::JavaLambda.__init__)


def test_pp2::javalambda_constructor_args():
    sig = inspect.signature(pp2::JavaLambda.__init__)
    params = list(sig.parameters.keys())
    assert "farrow" in params, "Missing parameter 'farrow'"

def test_pp2::javalambda_has_farrow():
    assert hasattr(pp2::JavaLambda, "farrow")
    descriptor = None
    for klass in pp2::JavaLambda.__mro__:
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



def test_pp2::elseifexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::ElseIfExpression)


def test_pp2::elseifexpression_constructor_exists():
    assert callable(pp2::ElseIfExpression.__init__)


def test_pp2::elseifexpression_constructor_args():
    sig = inspect.signature(pp2::ElseIfExpression.__init__)
    params = list(sig.parameters.keys())



def test_textexpression_is_not_abstract():
    assert not inspect.isabstract(TextExpression)


def test_textexpression_constructor_exists():
    assert callable(TextExpression.__init__)


def test_textexpression_constructor_args():
    sig = inspect.signature(TextExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::variablete_is_not_abstract():
    assert not inspect.isabstract(pp2::VariableTE)


def test_pp2::variablete_constructor_exists():
    assert callable(pp2::VariableTE.__init__)


def test_pp2::variablete_constructor_args():
    sig = inspect.signature(pp2::VariableTE.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_pp2::variablete_has_varName():
    assert hasattr(pp2::VariableTE, "varName")
    descriptor = None
    for klass in pp2::VariableTE.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_pp2::expressionte_is_not_abstract():
    assert not inspect.isabstract(pp2::ExpressionTE)


def test_pp2::expressionte_constructor_exists():
    assert callable(pp2::ExpressionTE.__init__)


def test_pp2::expressionte_constructor_args():
    sig = inspect.signature(pp2::ExpressionTE.__init__)
    params = list(sig.parameters.keys())



def test_pp2::verbatimte_is_not_abstract():
    assert not inspect.isabstract(pp2::VerbatimTE)


def test_pp2::verbatimte_constructor_exists():
    assert callable(pp2::VerbatimTE.__init__)


def test_pp2::verbatimte_constructor_args():
    sig = inspect.signature(pp2::VerbatimTE.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_pp2::verbatimte_has_text():
    assert hasattr(pp2::VerbatimTE, "text")
    descriptor = None
    for klass in pp2::VerbatimTE.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_pp2::textexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::TextExpression)


def test_pp2::textexpression_constructor_exists():
    assert callable(pp2::TextExpression.__init__)


def test_pp2::textexpression_constructor_args():
    sig = inspect.signature(pp2::TextExpression.__init__)
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



def test_pp2::unquotedstring_is_not_abstract():
    assert not inspect.isabstract(pp2::UnquotedString)


def test_pp2::unquotedstring_constructor_exists():
    assert callable(pp2::UnquotedString.__init__)


def test_pp2::unquotedstring_constructor_args():
    sig = inspect.signature(pp2::UnquotedString.__init__)
    params = list(sig.parameters.keys())



def test_pp2::singlequotedstring_is_not_abstract():
    assert not inspect.isabstract(pp2::SingleQuotedString)


def test_pp2::singlequotedstring_constructor_exists():
    assert callable(pp2::SingleQuotedString.__init__)


def test_pp2::singlequotedstring_constructor_args():
    sig = inspect.signature(pp2::SingleQuotedString.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_pp2::singlequotedstring_has_text():
    assert hasattr(pp2::SingleQuotedString, "text")
    descriptor = None
    for klass in pp2::SingleQuotedString.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_pp2::doublequotedstring_is_not_abstract():
    assert not inspect.isabstract(pp2::DoubleQuotedString)


def test_pp2::doublequotedstring_constructor_exists():
    assert callable(pp2::DoubleQuotedString.__init__)


def test_pp2::doublequotedstring_constructor_args():
    sig = inspect.signature(pp2::DoubleQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_withlambdaexpression_is_not_abstract():
    assert not inspect.isabstract(WithLambdaExpression)


def test_withlambdaexpression_constructor_exists():
    assert callable(WithLambdaExpression.__init__)


def test_withlambdaexpression_constructor_args():
    sig = inspect.signature(WithLambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::methodcall_is_not_abstract():
    assert not inspect.isabstract(pp2::MethodCall)


def test_pp2::methodcall_constructor_exists():
    assert callable(pp2::MethodCall.__init__)


def test_pp2::methodcall_constructor_args():
    sig = inspect.signature(pp2::MethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "parenthesized" in params, "Missing parameter 'parenthesized'"

def test_pp2::methodcall_has_parenthesized():
    assert hasattr(pp2::MethodCall, "parenthesized")
    descriptor = None
    for klass in pp2::MethodCall.__mro__:
        if "parenthesized" in klass.__dict__:
            descriptor = klass.__dict__["parenthesized"]
            break
    assert isinstance(descriptor, property)



def test_pp2::functioncall_is_not_abstract():
    assert not inspect.isabstract(pp2::FunctionCall)


def test_pp2::functioncall_constructor_exists():
    assert callable(pp2::FunctionCall.__init__)


def test_pp2::functioncall_constructor_args():
    sig = inspect.signature(pp2::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_parameterizedexpression_is_not_abstract():
    assert not inspect.isabstract(ParameterizedExpression)


def test_parameterizedexpression_constructor_exists():
    assert callable(ParameterizedExpression.__init__)


def test_parameterizedexpression_constructor_args():
    sig = inspect.signature(ParameterizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::selectorexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::SelectorExpression)


def test_pp2::selectorexpression_constructor_exists():
    assert callable(pp2::SelectorExpression.__init__)


def test_pp2::selectorexpression_constructor_args():
    sig = inspect.signature(pp2::SelectorExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::atexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::AtExpression)


def test_pp2::atexpression_constructor_exists():
    assert callable(pp2::AtExpression.__init__)


def test_pp2::atexpression_constructor_args():
    sig = inspect.signature(pp2::AtExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::withlambdaexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::WithLambdaExpression)


def test_pp2::withlambdaexpression_constructor_exists():
    assert callable(pp2::WithLambdaExpression.__init__)


def test_pp2::withlambdaexpression_constructor_args():
    sig = inspect.signature(pp2::WithLambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::hashentry_is_not_abstract():
    assert not inspect.isabstract(pp2::HashEntry)


def test_pp2::hashentry_constructor_exists():
    assert callable(pp2::HashEntry.__init__)


def test_pp2::hashentry_constructor_args():
    sig = inspect.signature(pp2::HashEntry.__init__)
    params = list(sig.parameters.keys())



def test_pp2::iquotedstring_is_not_abstract():
    assert not inspect.isabstract(pp2::IQuotedString)


def test_pp2::iquotedstring_constructor_exists():
    assert callable(pp2::IQuotedString.__init__)


def test_pp2::iquotedstring_constructor_args():
    sig = inspect.signature(pp2::IQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::virtualnameorreference_is_not_abstract():
    assert not inspect.isabstract(pp2::VirtualNameOrReference)


def test_pp2::virtualnameorreference_constructor_exists():
    assert callable(pp2::VirtualNameOrReference.__init__)


def test_pp2::virtualnameorreference_constructor_args():
    sig = inspect.signature(pp2::VirtualNameOrReference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "exported" in params, "Missing parameter 'exported'"

def test_pp2::virtualnameorreference_has_value():
    assert hasattr(pp2::VirtualNameOrReference, "value")
    descriptor = None
    for klass in pp2::VirtualNameOrReference.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_pp2::virtualnameorreference_has_exported():
    assert hasattr(pp2::VirtualNameOrReference, "exported")
    descriptor = None
    for klass in pp2::VirtualNameOrReference.__mro__:
        if "exported" in klass.__dict__:
            descriptor = klass.__dict__["exported"]
            break
    assert isinstance(descriptor, property)



def test_pp2::literalclass_is_not_abstract():
    assert not inspect.isabstract(pp2::LiteralClass)


def test_pp2::literalclass_constructor_exists():
    assert callable(pp2::LiteralClass.__init__)


def test_pp2::literalclass_constructor_args():
    sig = inspect.signature(pp2::LiteralClass.__init__)
    params = list(sig.parameters.keys())



def test_pp2::literalhash_is_not_abstract():
    assert not inspect.isabstract(pp2::LiteralHash)


def test_pp2::literalhash_constructor_exists():
    assert callable(pp2::LiteralHash.__init__)


def test_pp2::literalhash_constructor_args():
    sig = inspect.signature(pp2::LiteralHash.__init__)
    params = list(sig.parameters.keys())



def test_pp2::literallist_is_not_abstract():
    assert not inspect.isabstract(pp2::LiteralList)


def test_pp2::literallist_constructor_exists():
    assert callable(pp2::LiteralList.__init__)


def test_pp2::literallist_constructor_args():
    sig = inspect.signature(pp2::LiteralList.__init__)
    params = list(sig.parameters.keys())



def test_pp2::literalnameorreference_is_not_abstract():
    assert not inspect.isabstract(pp2::LiteralNameOrReference)


def test_pp2::literalnameorreference_constructor_exists():
    assert callable(pp2::LiteralNameOrReference.__init__)


def test_pp2::literalnameorreference_constructor_args():
    sig = inspect.signature(pp2::LiteralNameOrReference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp2::literalnameorreference_has_value():
    assert hasattr(pp2::LiteralNameOrReference, "value")
    descriptor = None
    for klass in pp2::LiteralNameOrReference.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::namedaccessexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::NamedAccessExpression)


def test_pp2::namedaccessexpression_constructor_exists():
    assert callable(pp2::NamedAccessExpression.__init__)


def test_pp2::namedaccessexpression_constructor_args():
    sig = inspect.signature(pp2::NamedAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::andexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::AndExpression)


def test_pp2::andexpression_constructor_exists():
    assert callable(pp2::AndExpression.__init__)


def test_pp2::andexpression_constructor_args():
    sig = inspect.signature(pp2::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::BinaryOpExpression)


def test_pp2::binaryopexpression_constructor_exists():
    assert callable(pp2::BinaryOpExpression.__init__)


def test_pp2::binaryopexpression_constructor_args():
    sig = inspect.signature(pp2::BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_pp2::binaryopexpression_has_opName():
    assert hasattr(pp2::BinaryOpExpression, "opName")
    descriptor = None
    for klass in pp2::BinaryOpExpression.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_pp2::appendexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::AppendExpression)


def test_pp2::appendexpression_constructor_exists():
    assert callable(pp2::AppendExpression.__init__)


def test_pp2::appendexpression_constructor_args():
    sig = inspect.signature(pp2::AppendExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::orexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::OrExpression)


def test_pp2::orexpression_constructor_exists():
    assert callable(pp2::OrExpression.__init__)


def test_pp2::orexpression_constructor_args():
    sig = inspect.signature(pp2::OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::selectorentry_is_not_abstract():
    assert not inspect.isabstract(pp2::SelectorEntry)


def test_pp2::selectorentry_constructor_exists():
    assert callable(pp2::SelectorEntry.__init__)


def test_pp2::selectorentry_constructor_args():
    sig = inspect.signature(pp2::SelectorEntry.__init__)
    params = list(sig.parameters.keys())



def test_pp2::assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::AssignmentExpression)


def test_pp2::assignmentexpression_constructor_exists():
    assert callable(pp2::AssignmentExpression.__init__)


def test_pp2::assignmentexpression_constructor_args():
    sig = inspect.signature(pp2::AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOpExpression)


def test_binaryopexpression_constructor_exists():
    assert callable(BinaryOpExpression.__init__)


def test_binaryopexpression_constructor_args():
    sig = inspect.signature(BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::RelationalExpression)


def test_pp2::relationalexpression_constructor_exists():
    assert callable(pp2::RelationalExpression.__init__)


def test_pp2::relationalexpression_constructor_args():
    sig = inspect.signature(pp2::RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::additiveexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::AdditiveExpression)


def test_pp2::additiveexpression_constructor_exists():
    assert callable(pp2::AdditiveExpression.__init__)


def test_pp2::additiveexpression_constructor_args():
    sig = inspect.signature(pp2::AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::ShiftExpression)


def test_pp2::shiftexpression_constructor_exists():
    assert callable(pp2::ShiftExpression.__init__)


def test_pp2::shiftexpression_constructor_args():
    sig = inspect.signature(pp2::ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::MultiplicativeExpression)


def test_pp2::multiplicativeexpression_constructor_exists():
    assert callable(pp2::MultiplicativeExpression.__init__)


def test_pp2::multiplicativeexpression_constructor_args():
    sig = inspect.signature(pp2::MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::EqualityExpression)


def test_pp2::equalityexpression_constructor_exists():
    assert callable(pp2::EqualityExpression.__init__)


def test_pp2::equalityexpression_constructor_args():
    sig = inspect.signature(pp2::EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::matchingexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::MatchingExpression)


def test_pp2::matchingexpression_constructor_exists():
    assert callable(pp2::MatchingExpression.__init__)


def test_pp2::matchingexpression_constructor_args():
    sig = inspect.signature(pp2::MatchingExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::inexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::InExpression)


def test_pp2::inexpression_constructor_exists():
    assert callable(pp2::InExpression.__init__)


def test_pp2::inexpression_constructor_args():
    sig = inspect.signature(pp2::InExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::relationshipexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::RelationshipExpression)


def test_pp2::relationshipexpression_constructor_exists():
    assert callable(pp2::RelationshipExpression.__init__)


def test_pp2::relationshipexpression_constructor_args():
    sig = inspect.signature(pp2::RelationshipExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::literalname_is_not_abstract():
    assert not inspect.isabstract(pp2::LiteralName)


def test_pp2::literalname_constructor_exists():
    assert callable(pp2::LiteralName.__init__)


def test_pp2::literalname_constructor_args():
    sig = inspect.signature(pp2::LiteralName.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp2::literalname_has_value():
    assert hasattr(pp2::LiteralName, "value")
    descriptor = None
    for klass in pp2::LiteralName.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp2::literalregex_is_not_abstract():
    assert not inspect.isabstract(pp2::LiteralRegex)


def test_pp2::literalregex_constructor_exists():
    assert callable(pp2::LiteralRegex.__init__)


def test_pp2::literalregex_constructor_args():
    sig = inspect.signature(pp2::LiteralRegex.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp2::literalregex_has_value():
    assert hasattr(pp2::LiteralRegex, "value")
    descriptor = None
    for klass in pp2::LiteralRegex.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp2::literaldefault_is_not_abstract():
    assert not inspect.isabstract(pp2::LiteralDefault)


def test_pp2::literaldefault_constructor_exists():
    assert callable(pp2::LiteralDefault.__init__)


def test_pp2::literaldefault_constructor_args():
    sig = inspect.signature(pp2::LiteralDefault.__init__)
    params = list(sig.parameters.keys())



def test_pp2::literalundef_is_not_abstract():
    assert not inspect.isabstract(pp2::LiteralUndef)


def test_pp2::literalundef_constructor_exists():
    assert callable(pp2::LiteralUndef.__init__)


def test_pp2::literalundef_constructor_args():
    sig = inspect.signature(pp2::LiteralUndef.__init__)
    params = list(sig.parameters.keys())



def test_pp2::literalboolean_is_not_abstract():
    assert not inspect.isabstract(pp2::LiteralBoolean)


def test_pp2::literalboolean_constructor_exists():
    assert callable(pp2::LiteralBoolean.__init__)


def test_pp2::literalboolean_constructor_args():
    sig = inspect.signature(pp2::LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp2::literalboolean_has_value():
    assert hasattr(pp2::LiteralBoolean, "value")
    descriptor = None
    for klass in pp2::LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_pp2::hostclassdefinition_is_not_abstract():
    assert not inspect.isabstract(pp2::HostClassDefinition)


def test_pp2::hostclassdefinition_constructor_exists():
    assert callable(pp2::HostClassDefinition.__init__)


def test_pp2::hostclassdefinition_constructor_args():
    sig = inspect.signature(pp2::HostClassDefinition.__init__)
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



def test_pp2::unarynotexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::UnaryNotExpression)


def test_pp2::unarynotexpression_constructor_exists():
    assert callable(pp2::UnaryNotExpression.__init__)


def test_pp2::unarynotexpression_constructor_args():
    sig = inspect.signature(pp2::UnaryNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::exportedcollectquery_is_not_abstract():
    assert not inspect.isabstract(pp2::ExportedCollectQuery)


def test_pp2::exportedcollectquery_constructor_exists():
    assert callable(pp2::ExportedCollectQuery.__init__)


def test_pp2::exportedcollectquery_constructor_args():
    sig = inspect.signature(pp2::ExportedCollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_pp2::unaryminusexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::UnaryMinusExpression)


def test_pp2::unaryminusexpression_constructor_exists():
    assert callable(pp2::UnaryMinusExpression.__init__)


def test_pp2::unaryminusexpression_constructor_args():
    sig = inspect.signature(pp2::UnaryMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::virtualcollectquery_is_not_abstract():
    assert not inspect.isabstract(pp2::VirtualCollectQuery)


def test_pp2::virtualcollectquery_constructor_exists():
    assert callable(pp2::VirtualCollectQuery.__init__)


def test_pp2::virtualcollectquery_constructor_args():
    sig = inspect.signature(pp2::VirtualCollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_pp2::icollectquery_is_not_abstract():
    assert not inspect.isabstract(pp2::ICollectQuery)


def test_pp2::icollectquery_constructor_exists():
    assert callable(pp2::ICollectQuery.__init__)


def test_pp2::icollectquery_constructor_args():
    sig = inspect.signature(pp2::ICollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_pp2::attributeoperation_is_not_abstract():
    assert not inspect.isabstract(pp2::AttributeOperation)


def test_pp2::attributeoperation_constructor_exists():
    assert callable(pp2::AttributeOperation.__init__)


def test_pp2::attributeoperation_constructor_args():
    sig = inspect.signature(pp2::AttributeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "op" in params, "Missing parameter 'op'"

def test_pp2::attributeoperation_has_key():
    assert hasattr(pp2::AttributeOperation, "key")
    descriptor = None
    for klass in pp2::AttributeOperation.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_pp2::attributeoperation_has_op():
    assert hasattr(pp2::AttributeOperation, "op")
    descriptor = None
    for klass in pp2::AttributeOperation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_pp2::attributeoperations_is_not_abstract():
    assert not inspect.isabstract(pp2::AttributeOperations)


def test_pp2::attributeoperations_constructor_exists():
    assert callable(pp2::AttributeOperations.__init__)


def test_pp2::attributeoperations_constructor_args():
    sig = inspect.signature(pp2::AttributeOperations.__init__)
    params = list(sig.parameters.keys())



def test_pp2::resourcebody_is_not_abstract():
    assert not inspect.isabstract(pp2::ResourceBody)


def test_pp2::resourcebody_constructor_exists():
    assert callable(pp2::ResourceBody.__init__)


def test_pp2::resourcebody_constructor_args():
    sig = inspect.signature(pp2::ResourceBody.__init__)
    params = list(sig.parameters.keys())



def test_pp2::expression_is_not_abstract():
    assert not inspect.isabstract(pp2::Expression)


def test_pp2::expression_constructor_exists():
    assert callable(pp2::Expression.__init__)


def test_pp2::expression_constructor_args():
    sig = inspect.signature(pp2::Expression.__init__)
    params = list(sig.parameters.keys())



def test_expressionblock_is_not_abstract():
    assert not inspect.isabstract(ExpressionBlock)


def test_expressionblock_constructor_exists():
    assert callable(ExpressionBlock.__init__)


def test_expressionblock_constructor_args():
    sig = inspect.signature(ExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_pp2::ifexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::IfExpression)


def test_pp2::ifexpression_constructor_exists():
    assert callable(pp2::IfExpression.__init__)


def test_pp2::ifexpression_constructor_args():
    sig = inspect.signature(pp2::IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::lambda_is_not_abstract():
    assert not inspect.isabstract(pp2::Lambda)


def test_pp2::lambda_constructor_exists():
    assert callable(pp2::Lambda.__init__)


def test_pp2::lambda_constructor_args():
    sig = inspect.signature(pp2::Lambda.__init__)
    params = list(sig.parameters.keys())



def test_pp2::elseexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::ElseExpression)


def test_pp2::elseexpression_constructor_exists():
    assert callable(pp2::ElseExpression.__init__)


def test_pp2::elseexpression_constructor_args():
    sig = inspect.signature(pp2::ElseExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::unlessexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::UnlessExpression)


def test_pp2::unlessexpression_constructor_exists():
    assert callable(pp2::UnlessExpression.__init__)


def test_pp2::unlessexpression_constructor_args():
    sig = inspect.signature(pp2::UnlessExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::definition_is_not_abstract():
    assert not inspect.isabstract(pp2::Definition)


def test_pp2::definition_constructor_exists():
    assert callable(pp2::Definition.__init__)


def test_pp2::definition_constructor_args():
    sig = inspect.signature(pp2::Definition.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"

def test_pp2::definition_has_className():
    assert hasattr(pp2::Definition, "className")
    descriptor = None
    for klass in pp2::Definition.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_pp2::nodedefinition_is_not_abstract():
    assert not inspect.isabstract(pp2::NodeDefinition)


def test_pp2::nodedefinition_constructor_exists():
    assert callable(pp2::NodeDefinition.__init__)


def test_pp2::nodedefinition_constructor_args():
    sig = inspect.signature(pp2::NodeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_pp2::case_is_not_abstract():
    assert not inspect.isabstract(pp2::Case)


def test_pp2::case_constructor_exists():
    assert callable(pp2::Case.__init__)


def test_pp2::case_constructor_args():
    sig = inspect.signature(pp2::Case.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::expressionblock_is_not_abstract():
    assert not inspect.isabstract(pp2::ExpressionBlock)


def test_pp2::expressionblock_constructor_exists():
    assert callable(pp2::ExpressionBlock.__init__)


def test_pp2::expressionblock_constructor_args():
    sig = inspect.signature(pp2::ExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_pp2::literalexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::LiteralExpression)


def test_pp2::literalexpression_constructor_exists():
    assert callable(pp2::LiteralExpression.__init__)


def test_pp2::literalexpression_constructor_args():
    sig = inspect.signature(pp2::LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::resourceexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::ResourceExpression)


def test_pp2::resourceexpression_constructor_exists():
    assert callable(pp2::ResourceExpression.__init__)


def test_pp2::resourceexpression_constructor_args():
    sig = inspect.signature(pp2::ResourceExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::interpolatedvariable_is_not_abstract():
    assert not inspect.isabstract(pp2::InterpolatedVariable)


def test_pp2::interpolatedvariable_constructor_exists():
    assert callable(pp2::InterpolatedVariable.__init__)


def test_pp2::interpolatedvariable_constructor_args():
    sig = inspect.signature(pp2::InterpolatedVariable.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_pp2::interpolatedvariable_has_varName():
    assert hasattr(pp2::InterpolatedVariable, "varName")
    descriptor = None
    for klass in pp2::InterpolatedVariable.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_pp2::variableexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::VariableExpression)


def test_pp2::variableexpression_constructor_exists():
    assert callable(pp2::VariableExpression.__init__)


def test_pp2::variableexpression_constructor_args():
    sig = inspect.signature(pp2::VariableExpression.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_pp2::variableexpression_has_varName():
    assert hasattr(pp2::VariableExpression, "varName")
    descriptor = None
    for klass in pp2::VariableExpression.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_pp2::exprlist_is_not_abstract():
    assert not inspect.isabstract(pp2::ExprList)


def test_pp2::exprlist_constructor_exists():
    assert callable(pp2::ExprList.__init__)


def test_pp2::exprlist_constructor_args():
    sig = inspect.signature(pp2::ExprList.__init__)
    params = list(sig.parameters.keys())



def test_pp2::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::UnaryExpression)


def test_pp2::unaryexpression_constructor_exists():
    assert callable(pp2::UnaryExpression.__init__)


def test_pp2::unaryexpression_constructor_args():
    sig = inspect.signature(pp2::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::BinaryExpression)


def test_pp2::binaryexpression_constructor_exists():
    assert callable(pp2::BinaryExpression.__init__)


def test_pp2::binaryexpression_constructor_args():
    sig = inspect.signature(pp2::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::importexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::ImportExpression)


def test_pp2::importexpression_constructor_exists():
    assert callable(pp2::ImportExpression.__init__)


def test_pp2::importexpression_constructor_args():
    sig = inspect.signature(pp2::ImportExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::parenthesisedexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::ParenthesisedExpression)


def test_pp2::parenthesisedexpression_constructor_exists():
    assert callable(pp2::ParenthesisedExpression.__init__)


def test_pp2::parenthesisedexpression_constructor_args():
    sig = inspect.signature(pp2::ParenthesisedExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::separatorexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::SeparatorExpression)


def test_pp2::separatorexpression_constructor_exists():
    assert callable(pp2::SeparatorExpression.__init__)


def test_pp2::separatorexpression_constructor_args():
    sig = inspect.signature(pp2::SeparatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::stringexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::StringExpression)


def test_pp2::stringexpression_constructor_exists():
    assert callable(pp2::StringExpression.__init__)


def test_pp2::stringexpression_constructor_args():
    sig = inspect.signature(pp2::StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::parameterizedexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::ParameterizedExpression)


def test_pp2::parameterizedexpression_constructor_exists():
    assert callable(pp2::ParameterizedExpression.__init__)


def test_pp2::parameterizedexpression_constructor_args():
    sig = inspect.signature(pp2::ParameterizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::collectexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::CollectExpression)


def test_pp2::collectexpression_constructor_exists():
    assert callable(pp2::CollectExpression.__init__)


def test_pp2::collectexpression_constructor_args():
    sig = inspect.signature(pp2::CollectExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::caseexpression_is_not_abstract():
    assert not inspect.isabstract(pp2::CaseExpression)


def test_pp2::caseexpression_constructor_exists():
    assert callable(pp2::CaseExpression.__init__)


def test_pp2::caseexpression_constructor_args():
    sig = inspect.signature(pp2::CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp2::definitionargument_is_not_abstract():
    assert not inspect.isabstract(pp2::DefinitionArgument)


def test_pp2::definitionargument_constructor_exists():
    assert callable(pp2::DefinitionArgument.__init__)


def test_pp2::definitionargument_constructor_args():
    sig = inspect.signature(pp2::DefinitionArgument.__init__)
    params = list(sig.parameters.keys())
    assert "argName" in params, "Missing parameter 'argName'"
    assert "op" in params, "Missing parameter 'op'"

def test_pp2::definitionargument_has_argName():
    assert hasattr(pp2::DefinitionArgument, "argName")
    descriptor = None
    for klass in pp2::DefinitionArgument.__mro__:
        if "argName" in klass.__dict__:
            descriptor = klass.__dict__["argName"]
            break
    assert isinstance(descriptor, property)

def test_pp2::definitionargument_has_op():
    assert hasattr(pp2::DefinitionArgument, "op")
    descriptor = None
    for klass in pp2::DefinitionArgument.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_pp2::definitionargumentlist_is_not_abstract():
    assert not inspect.isabstract(pp2::DefinitionArgumentList)


def test_pp2::definitionargumentlist_constructor_exists():
    assert callable(pp2::DefinitionArgumentList.__init__)


def test_pp2::definitionargumentlist_constructor_args():
    sig = inspect.signature(pp2::DefinitionArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_pp2::puppetmanifest_is_not_abstract():
    assert not inspect.isabstract(pp2::PuppetManifest)


def test_pp2::puppetmanifest_constructor_exists():
    assert callable(pp2::PuppetManifest.__init__)


def test_pp2::puppetmanifest_constructor_args():
    sig = inspect.signature(pp2::PuppetManifest.__init__)
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
pp2::RubyLambda_strategy = st.builds(
    pp2::RubyLambda,
)
pp2::JavaLambda_strategy = st.builds(
    pp2::JavaLambda,
    farrow=
        st.booleans()
)
IfExpression_strategy = st.builds(
    IfExpression,
)
pp2::ElseIfExpression_strategy = st.builds(
    pp2::ElseIfExpression,
)
TextExpression_strategy = st.builds(
    TextExpression,
)
pp2::VariableTE_strategy = st.builds(
    pp2::VariableTE,
    varName=
        safe_text
)
pp2::ExpressionTE_strategy = st.builds(
    pp2::ExpressionTE,
)
pp2::VerbatimTE_strategy = st.builds(
    pp2::VerbatimTE,
    text=
        safe_text
)
pp2::TextExpression_strategy = st.builds(
    pp2::TextExpression,
)
IQuotedString_strategy = st.builds(
    IQuotedString,
)
StringExpression_strategy = st.builds(
    StringExpression,
)
pp2::UnquotedString_strategy = st.builds(
    pp2::UnquotedString,
)
pp2::SingleQuotedString_strategy = st.builds(
    pp2::SingleQuotedString,
    text=
        safe_text
)
pp2::DoubleQuotedString_strategy = st.builds(
    pp2::DoubleQuotedString,
)
WithLambdaExpression_strategy = st.builds(
    WithLambdaExpression,
)
pp2::MethodCall_strategy = st.builds(
    pp2::MethodCall,
    parenthesized=
        st.booleans()
)
pp2::FunctionCall_strategy = st.builds(
    pp2::FunctionCall,
)
ParameterizedExpression_strategy = st.builds(
    ParameterizedExpression,
)
pp2::SelectorExpression_strategy = st.builds(
    pp2::SelectorExpression,
)
pp2::AtExpression_strategy = st.builds(
    pp2::AtExpression,
)
pp2::WithLambdaExpression_strategy = st.builds(
    pp2::WithLambdaExpression,
)
pp2::HashEntry_strategy = st.builds(
    pp2::HashEntry,
)
pp2::IQuotedString_strategy = st.builds(
    pp2::IQuotedString,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
pp2::VirtualNameOrReference_strategy = st.builds(
    pp2::VirtualNameOrReference,
    value=
        safe_text,
    exported=
        st.booleans()
)
pp2::LiteralClass_strategy = st.builds(
    pp2::LiteralClass,
)
pp2::LiteralHash_strategy = st.builds(
    pp2::LiteralHash,
)
pp2::LiteralList_strategy = st.builds(
    pp2::LiteralList,
)
pp2::LiteralNameOrReference_strategy = st.builds(
    pp2::LiteralNameOrReference,
    value=
        safe_text
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
pp2::NamedAccessExpression_strategy = st.builds(
    pp2::NamedAccessExpression,
)
pp2::AndExpression_strategy = st.builds(
    pp2::AndExpression,
)
pp2::BinaryOpExpression_strategy = st.builds(
    pp2::BinaryOpExpression,
    opName=
        safe_text
)
pp2::AppendExpression_strategy = st.builds(
    pp2::AppendExpression,
)
pp2::OrExpression_strategy = st.builds(
    pp2::OrExpression,
)
pp2::SelectorEntry_strategy = st.builds(
    pp2::SelectorEntry,
)
pp2::AssignmentExpression_strategy = st.builds(
    pp2::AssignmentExpression,
)
BinaryOpExpression_strategy = st.builds(
    BinaryOpExpression,
)
pp2::RelationalExpression_strategy = st.builds(
    pp2::RelationalExpression,
)
pp2::AdditiveExpression_strategy = st.builds(
    pp2::AdditiveExpression,
)
pp2::ShiftExpression_strategy = st.builds(
    pp2::ShiftExpression,
)
pp2::MultiplicativeExpression_strategy = st.builds(
    pp2::MultiplicativeExpression,
)
pp2::EqualityExpression_strategy = st.builds(
    pp2::EqualityExpression,
)
pp2::MatchingExpression_strategy = st.builds(
    pp2::MatchingExpression,
)
pp2::InExpression_strategy = st.builds(
    pp2::InExpression,
)
pp2::RelationshipExpression_strategy = st.builds(
    pp2::RelationshipExpression,
)
pp2::LiteralName_strategy = st.builds(
    pp2::LiteralName,
    value=
        safe_text
)
pp2::LiteralRegex_strategy = st.builds(
    pp2::LiteralRegex,
    value=
        safe_text
)
pp2::LiteralDefault_strategy = st.builds(
    pp2::LiteralDefault,
)
pp2::LiteralUndef_strategy = st.builds(
    pp2::LiteralUndef,
)
pp2::LiteralBoolean_strategy = st.builds(
    pp2::LiteralBoolean,
    value=
        st.booleans()
)
Definition_strategy = st.builds(
    Definition,
)
pp2::HostClassDefinition_strategy = st.builds(
    pp2::HostClassDefinition,
)
ICollectQuery_strategy = st.builds(
    ICollectQuery,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
pp2::UnaryNotExpression_strategy = st.builds(
    pp2::UnaryNotExpression,
)
pp2::ExportedCollectQuery_strategy = st.builds(
    pp2::ExportedCollectQuery,
)
pp2::UnaryMinusExpression_strategy = st.builds(
    pp2::UnaryMinusExpression,
)
pp2::VirtualCollectQuery_strategy = st.builds(
    pp2::VirtualCollectQuery,
)
pp2::ICollectQuery_strategy = st.builds(
    pp2::ICollectQuery,
)
pp2::AttributeOperation_strategy = st.builds(
    pp2::AttributeOperation,
    key=
        safe_text,
    op=
        safe_text
)
pp2::AttributeOperations_strategy = st.builds(
    pp2::AttributeOperations,
)
pp2::ResourceBody_strategy = st.builds(
    pp2::ResourceBody,
)
pp2::Expression_strategy = st.builds(
    pp2::Expression,
)
ExpressionBlock_strategy = st.builds(
    ExpressionBlock,
)
pp2::IfExpression_strategy = st.builds(
    pp2::IfExpression,
)
pp2::Lambda_strategy = st.builds(
    pp2::Lambda,
)
pp2::ElseExpression_strategy = st.builds(
    pp2::ElseExpression,
)
pp2::UnlessExpression_strategy = st.builds(
    pp2::UnlessExpression,
)
pp2::Definition_strategy = st.builds(
    pp2::Definition,
    className=
        safe_text
)
pp2::NodeDefinition_strategy = st.builds(
    pp2::NodeDefinition,
)
pp2::Case_strategy = st.builds(
    pp2::Case,
)
Expression_strategy = st.builds(
    Expression,
)
pp2::ExpressionBlock_strategy = st.builds(
    pp2::ExpressionBlock,
)
pp2::LiteralExpression_strategy = st.builds(
    pp2::LiteralExpression,
)
pp2::ResourceExpression_strategy = st.builds(
    pp2::ResourceExpression,
)
pp2::InterpolatedVariable_strategy = st.builds(
    pp2::InterpolatedVariable,
    varName=
        safe_text
)
pp2::VariableExpression_strategy = st.builds(
    pp2::VariableExpression,
    varName=
        safe_text
)
pp2::ExprList_strategy = st.builds(
    pp2::ExprList,
)
pp2::UnaryExpression_strategy = st.builds(
    pp2::UnaryExpression,
)
pp2::BinaryExpression_strategy = st.builds(
    pp2::BinaryExpression,
)
pp2::ImportExpression_strategy = st.builds(
    pp2::ImportExpression,
)
pp2::ParenthesisedExpression_strategy = st.builds(
    pp2::ParenthesisedExpression,
)
pp2::SeparatorExpression_strategy = st.builds(
    pp2::SeparatorExpression,
)
pp2::StringExpression_strategy = st.builds(
    pp2::StringExpression,
)
pp2::ParameterizedExpression_strategy = st.builds(
    pp2::ParameterizedExpression,
)
pp2::CollectExpression_strategy = st.builds(
    pp2::CollectExpression,
)
pp2::CaseExpression_strategy = st.builds(
    pp2::CaseExpression,
)
pp2::DefinitionArgument_strategy = st.builds(
    pp2::DefinitionArgument,
    argName=
        safe_text,
    op=
        safe_text
)
pp2::DefinitionArgumentList_strategy = st.builds(
    pp2::DefinitionArgumentList,
)
pp2::PuppetManifest_strategy = st.builds(
    pp2::PuppetManifest,
)

@given(instance=Lambda_strategy)
@settings(max_examples=50)
def test_lambda_instantiation(instance):
    assert isinstance(instance, Lambda)

@given(instance=pp2::RubyLambda_strategy)
@settings(max_examples=50)
def test_pp2::rubylambda_instantiation(instance):
    assert isinstance(instance, pp2::RubyLambda)

@given(instance=pp2::JavaLambda_strategy)
@settings(max_examples=50)
def test_pp2::javalambda_instantiation(instance):
    assert isinstance(instance, pp2::JavaLambda)

@given(instance=pp2::JavaLambda_strategy)
def test_pp2::javalambda_farrow_type(instance):
    assert isinstance(instance.farrow, bool)


@given(instance=pp2::JavaLambda_strategy)
def test_pp2::javalambda_farrow_setter(instance):
    original = instance.farrow
    instance.farrow = original
    assert instance.farrow == original

@given(instance=IfExpression_strategy)
@settings(max_examples=50)
def test_ifexpression_instantiation(instance):
    assert isinstance(instance, IfExpression)

@given(instance=pp2::ElseIfExpression_strategy)
@settings(max_examples=50)
def test_pp2::elseifexpression_instantiation(instance):
    assert isinstance(instance, pp2::ElseIfExpression)

@given(instance=TextExpression_strategy)
@settings(max_examples=50)
def test_textexpression_instantiation(instance):
    assert isinstance(instance, TextExpression)

@given(instance=pp2::VariableTE_strategy)
@settings(max_examples=50)
def test_pp2::variablete_instantiation(instance):
    assert isinstance(instance, pp2::VariableTE)

@given(instance=pp2::VariableTE_strategy)
def test_pp2::variablete_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=pp2::VariableTE_strategy)
def test_pp2::variablete_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=pp2::ExpressionTE_strategy)
@settings(max_examples=50)
def test_pp2::expressionte_instantiation(instance):
    assert isinstance(instance, pp2::ExpressionTE)

@given(instance=pp2::VerbatimTE_strategy)
@settings(max_examples=50)
def test_pp2::verbatimte_instantiation(instance):
    assert isinstance(instance, pp2::VerbatimTE)

@given(instance=pp2::VerbatimTE_strategy)
def test_pp2::verbatimte_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=pp2::VerbatimTE_strategy)
def test_pp2::verbatimte_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=pp2::TextExpression_strategy)
@settings(max_examples=50)
def test_pp2::textexpression_instantiation(instance):
    assert isinstance(instance, pp2::TextExpression)

@given(instance=IQuotedString_strategy)
@settings(max_examples=50)
def test_iquotedstring_instantiation(instance):
    assert isinstance(instance, IQuotedString)

@given(instance=StringExpression_strategy)
@settings(max_examples=50)
def test_stringexpression_instantiation(instance):
    assert isinstance(instance, StringExpression)

@given(instance=pp2::UnquotedString_strategy)
@settings(max_examples=50)
def test_pp2::unquotedstring_instantiation(instance):
    assert isinstance(instance, pp2::UnquotedString)

@given(instance=pp2::SingleQuotedString_strategy)
@settings(max_examples=50)
def test_pp2::singlequotedstring_instantiation(instance):
    assert isinstance(instance, pp2::SingleQuotedString)

@given(instance=pp2::SingleQuotedString_strategy)
def test_pp2::singlequotedstring_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=pp2::SingleQuotedString_strategy)
def test_pp2::singlequotedstring_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=pp2::DoubleQuotedString_strategy)
@settings(max_examples=50)
def test_pp2::doublequotedstring_instantiation(instance):
    assert isinstance(instance, pp2::DoubleQuotedString)

@given(instance=WithLambdaExpression_strategy)
@settings(max_examples=50)
def test_withlambdaexpression_instantiation(instance):
    assert isinstance(instance, WithLambdaExpression)

@given(instance=pp2::MethodCall_strategy)
@settings(max_examples=50)
def test_pp2::methodcall_instantiation(instance):
    assert isinstance(instance, pp2::MethodCall)

@given(instance=pp2::MethodCall_strategy)
def test_pp2::methodcall_parenthesized_type(instance):
    assert isinstance(instance.parenthesized, bool)


@given(instance=pp2::MethodCall_strategy)
def test_pp2::methodcall_parenthesized_setter(instance):
    original = instance.parenthesized
    instance.parenthesized = original
    assert instance.parenthesized == original

@given(instance=pp2::FunctionCall_strategy)
@settings(max_examples=50)
def test_pp2::functioncall_instantiation(instance):
    assert isinstance(instance, pp2::FunctionCall)

@given(instance=ParameterizedExpression_strategy)
@settings(max_examples=50)
def test_parameterizedexpression_instantiation(instance):
    assert isinstance(instance, ParameterizedExpression)

@given(instance=pp2::SelectorExpression_strategy)
@settings(max_examples=50)
def test_pp2::selectorexpression_instantiation(instance):
    assert isinstance(instance, pp2::SelectorExpression)

@given(instance=pp2::AtExpression_strategy)
@settings(max_examples=50)
def test_pp2::atexpression_instantiation(instance):
    assert isinstance(instance, pp2::AtExpression)

@given(instance=pp2::WithLambdaExpression_strategy)
@settings(max_examples=50)
def test_pp2::withlambdaexpression_instantiation(instance):
    assert isinstance(instance, pp2::WithLambdaExpression)

@given(instance=pp2::HashEntry_strategy)
@settings(max_examples=50)
def test_pp2::hashentry_instantiation(instance):
    assert isinstance(instance, pp2::HashEntry)

@given(instance=pp2::IQuotedString_strategy)
@settings(max_examples=50)
def test_pp2::iquotedstring_instantiation(instance):
    assert isinstance(instance, pp2::IQuotedString)

@given(instance=LiteralExpression_strategy)
@settings(max_examples=50)
def test_literalexpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)

@given(instance=pp2::VirtualNameOrReference_strategy)
@settings(max_examples=50)
def test_pp2::virtualnameorreference_instantiation(instance):
    assert isinstance(instance, pp2::VirtualNameOrReference)

@given(instance=pp2::VirtualNameOrReference_strategy)
def test_pp2::virtualnameorreference_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pp2::VirtualNameOrReference_strategy)
def test_pp2::virtualnameorreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp2::VirtualNameOrReference_strategy)
def test_pp2::virtualnameorreference_exported_type(instance):
    assert isinstance(instance.exported, bool)


@given(instance=pp2::VirtualNameOrReference_strategy)
def test_pp2::virtualnameorreference_exported_setter(instance):
    original = instance.exported
    instance.exported = original
    assert instance.exported == original

@given(instance=pp2::LiteralClass_strategy)
@settings(max_examples=50)
def test_pp2::literalclass_instantiation(instance):
    assert isinstance(instance, pp2::LiteralClass)

@given(instance=pp2::LiteralHash_strategy)
@settings(max_examples=50)
def test_pp2::literalhash_instantiation(instance):
    assert isinstance(instance, pp2::LiteralHash)

@given(instance=pp2::LiteralList_strategy)
@settings(max_examples=50)
def test_pp2::literallist_instantiation(instance):
    assert isinstance(instance, pp2::LiteralList)

@given(instance=pp2::LiteralNameOrReference_strategy)
@settings(max_examples=50)
def test_pp2::literalnameorreference_instantiation(instance):
    assert isinstance(instance, pp2::LiteralNameOrReference)

@given(instance=pp2::LiteralNameOrReference_strategy)
def test_pp2::literalnameorreference_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pp2::LiteralNameOrReference_strategy)
def test_pp2::literalnameorreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=pp2::NamedAccessExpression_strategy)
@settings(max_examples=50)
def test_pp2::namedaccessexpression_instantiation(instance):
    assert isinstance(instance, pp2::NamedAccessExpression)

@given(instance=pp2::AndExpression_strategy)
@settings(max_examples=50)
def test_pp2::andexpression_instantiation(instance):
    assert isinstance(instance, pp2::AndExpression)

@given(instance=pp2::BinaryOpExpression_strategy)
@settings(max_examples=50)
def test_pp2::binaryopexpression_instantiation(instance):
    assert isinstance(instance, pp2::BinaryOpExpression)

@given(instance=pp2::BinaryOpExpression_strategy)
def test_pp2::binaryopexpression_opName_type(instance):
    assert isinstance(instance.opName, str)


@given(instance=pp2::BinaryOpExpression_strategy)
def test_pp2::binaryopexpression_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=pp2::AppendExpression_strategy)
@settings(max_examples=50)
def test_pp2::appendexpression_instantiation(instance):
    assert isinstance(instance, pp2::AppendExpression)

@given(instance=pp2::OrExpression_strategy)
@settings(max_examples=50)
def test_pp2::orexpression_instantiation(instance):
    assert isinstance(instance, pp2::OrExpression)

@given(instance=pp2::SelectorEntry_strategy)
@settings(max_examples=50)
def test_pp2::selectorentry_instantiation(instance):
    assert isinstance(instance, pp2::SelectorEntry)

@given(instance=pp2::AssignmentExpression_strategy)
@settings(max_examples=50)
def test_pp2::assignmentexpression_instantiation(instance):
    assert isinstance(instance, pp2::AssignmentExpression)

@given(instance=BinaryOpExpression_strategy)
@settings(max_examples=50)
def test_binaryopexpression_instantiation(instance):
    assert isinstance(instance, BinaryOpExpression)

@given(instance=pp2::RelationalExpression_strategy)
@settings(max_examples=50)
def test_pp2::relationalexpression_instantiation(instance):
    assert isinstance(instance, pp2::RelationalExpression)

@given(instance=pp2::AdditiveExpression_strategy)
@settings(max_examples=50)
def test_pp2::additiveexpression_instantiation(instance):
    assert isinstance(instance, pp2::AdditiveExpression)

@given(instance=pp2::ShiftExpression_strategy)
@settings(max_examples=50)
def test_pp2::shiftexpression_instantiation(instance):
    assert isinstance(instance, pp2::ShiftExpression)

@given(instance=pp2::MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_pp2::multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, pp2::MultiplicativeExpression)

@given(instance=pp2::EqualityExpression_strategy)
@settings(max_examples=50)
def test_pp2::equalityexpression_instantiation(instance):
    assert isinstance(instance, pp2::EqualityExpression)

@given(instance=pp2::MatchingExpression_strategy)
@settings(max_examples=50)
def test_pp2::matchingexpression_instantiation(instance):
    assert isinstance(instance, pp2::MatchingExpression)

@given(instance=pp2::InExpression_strategy)
@settings(max_examples=50)
def test_pp2::inexpression_instantiation(instance):
    assert isinstance(instance, pp2::InExpression)

@given(instance=pp2::RelationshipExpression_strategy)
@settings(max_examples=50)
def test_pp2::relationshipexpression_instantiation(instance):
    assert isinstance(instance, pp2::RelationshipExpression)

@given(instance=pp2::LiteralName_strategy)
@settings(max_examples=50)
def test_pp2::literalname_instantiation(instance):
    assert isinstance(instance, pp2::LiteralName)

@given(instance=pp2::LiteralName_strategy)
def test_pp2::literalname_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pp2::LiteralName_strategy)
def test_pp2::literalname_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp2::LiteralRegex_strategy)
@settings(max_examples=50)
def test_pp2::literalregex_instantiation(instance):
    assert isinstance(instance, pp2::LiteralRegex)

@given(instance=pp2::LiteralRegex_strategy)
def test_pp2::literalregex_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=pp2::LiteralRegex_strategy)
def test_pp2::literalregex_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp2::LiteralDefault_strategy)
@settings(max_examples=50)
def test_pp2::literaldefault_instantiation(instance):
    assert isinstance(instance, pp2::LiteralDefault)

@given(instance=pp2::LiteralUndef_strategy)
@settings(max_examples=50)
def test_pp2::literalundef_instantiation(instance):
    assert isinstance(instance, pp2::LiteralUndef)

@given(instance=pp2::LiteralBoolean_strategy)
@settings(max_examples=50)
def test_pp2::literalboolean_instantiation(instance):
    assert isinstance(instance, pp2::LiteralBoolean)

@given(instance=pp2::LiteralBoolean_strategy)
def test_pp2::literalboolean_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=pp2::LiteralBoolean_strategy)
def test_pp2::literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=pp2::HostClassDefinition_strategy)
@settings(max_examples=50)
def test_pp2::hostclassdefinition_instantiation(instance):
    assert isinstance(instance, pp2::HostClassDefinition)

@given(instance=ICollectQuery_strategy)
@settings(max_examples=50)
def test_icollectquery_instantiation(instance):
    assert isinstance(instance, ICollectQuery)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=pp2::UnaryNotExpression_strategy)
@settings(max_examples=50)
def test_pp2::unarynotexpression_instantiation(instance):
    assert isinstance(instance, pp2::UnaryNotExpression)

@given(instance=pp2::ExportedCollectQuery_strategy)
@settings(max_examples=50)
def test_pp2::exportedcollectquery_instantiation(instance):
    assert isinstance(instance, pp2::ExportedCollectQuery)

@given(instance=pp2::UnaryMinusExpression_strategy)
@settings(max_examples=50)
def test_pp2::unaryminusexpression_instantiation(instance):
    assert isinstance(instance, pp2::UnaryMinusExpression)

@given(instance=pp2::VirtualCollectQuery_strategy)
@settings(max_examples=50)
def test_pp2::virtualcollectquery_instantiation(instance):
    assert isinstance(instance, pp2::VirtualCollectQuery)

@given(instance=pp2::ICollectQuery_strategy)
@settings(max_examples=50)
def test_pp2::icollectquery_instantiation(instance):
    assert isinstance(instance, pp2::ICollectQuery)

@given(instance=pp2::AttributeOperation_strategy)
@settings(max_examples=50)
def test_pp2::attributeoperation_instantiation(instance):
    assert isinstance(instance, pp2::AttributeOperation)

@given(instance=pp2::AttributeOperation_strategy)
def test_pp2::attributeoperation_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=pp2::AttributeOperation_strategy)
def test_pp2::attributeoperation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=pp2::AttributeOperation_strategy)
def test_pp2::attributeoperation_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=pp2::AttributeOperation_strategy)
def test_pp2::attributeoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=pp2::AttributeOperations_strategy)
@settings(max_examples=50)
def test_pp2::attributeoperations_instantiation(instance):
    assert isinstance(instance, pp2::AttributeOperations)

@given(instance=pp2::ResourceBody_strategy)
@settings(max_examples=50)
def test_pp2::resourcebody_instantiation(instance):
    assert isinstance(instance, pp2::ResourceBody)

@given(instance=pp2::Expression_strategy)
@settings(max_examples=50)
def test_pp2::expression_instantiation(instance):
    assert isinstance(instance, pp2::Expression)

@given(instance=ExpressionBlock_strategy)
@settings(max_examples=50)
def test_expressionblock_instantiation(instance):
    assert isinstance(instance, ExpressionBlock)

@given(instance=pp2::IfExpression_strategy)
@settings(max_examples=50)
def test_pp2::ifexpression_instantiation(instance):
    assert isinstance(instance, pp2::IfExpression)

@given(instance=pp2::Lambda_strategy)
@settings(max_examples=50)
def test_pp2::lambda_instantiation(instance):
    assert isinstance(instance, pp2::Lambda)

@given(instance=pp2::ElseExpression_strategy)
@settings(max_examples=50)
def test_pp2::elseexpression_instantiation(instance):
    assert isinstance(instance, pp2::ElseExpression)

@given(instance=pp2::UnlessExpression_strategy)
@settings(max_examples=50)
def test_pp2::unlessexpression_instantiation(instance):
    assert isinstance(instance, pp2::UnlessExpression)

@given(instance=pp2::Definition_strategy)
@settings(max_examples=50)
def test_pp2::definition_instantiation(instance):
    assert isinstance(instance, pp2::Definition)

@given(instance=pp2::Definition_strategy)
def test_pp2::definition_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=pp2::Definition_strategy)
def test_pp2::definition_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=pp2::NodeDefinition_strategy)
@settings(max_examples=50)
def test_pp2::nodedefinition_instantiation(instance):
    assert isinstance(instance, pp2::NodeDefinition)

@given(instance=pp2::Case_strategy)
@settings(max_examples=50)
def test_pp2::case_instantiation(instance):
    assert isinstance(instance, pp2::Case)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=pp2::ExpressionBlock_strategy)
@settings(max_examples=50)
def test_pp2::expressionblock_instantiation(instance):
    assert isinstance(instance, pp2::ExpressionBlock)

@given(instance=pp2::LiteralExpression_strategy)
@settings(max_examples=50)
def test_pp2::literalexpression_instantiation(instance):
    assert isinstance(instance, pp2::LiteralExpression)

@given(instance=pp2::ResourceExpression_strategy)
@settings(max_examples=50)
def test_pp2::resourceexpression_instantiation(instance):
    assert isinstance(instance, pp2::ResourceExpression)

@given(instance=pp2::InterpolatedVariable_strategy)
@settings(max_examples=50)
def test_pp2::interpolatedvariable_instantiation(instance):
    assert isinstance(instance, pp2::InterpolatedVariable)

@given(instance=pp2::InterpolatedVariable_strategy)
def test_pp2::interpolatedvariable_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=pp2::InterpolatedVariable_strategy)
def test_pp2::interpolatedvariable_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=pp2::VariableExpression_strategy)
@settings(max_examples=50)
def test_pp2::variableexpression_instantiation(instance):
    assert isinstance(instance, pp2::VariableExpression)

@given(instance=pp2::VariableExpression_strategy)
def test_pp2::variableexpression_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=pp2::VariableExpression_strategy)
def test_pp2::variableexpression_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=pp2::ExprList_strategy)
@settings(max_examples=50)
def test_pp2::exprlist_instantiation(instance):
    assert isinstance(instance, pp2::ExprList)

@given(instance=pp2::UnaryExpression_strategy)
@settings(max_examples=50)
def test_pp2::unaryexpression_instantiation(instance):
    assert isinstance(instance, pp2::UnaryExpression)

@given(instance=pp2::BinaryExpression_strategy)
@settings(max_examples=50)
def test_pp2::binaryexpression_instantiation(instance):
    assert isinstance(instance, pp2::BinaryExpression)

@given(instance=pp2::ImportExpression_strategy)
@settings(max_examples=50)
def test_pp2::importexpression_instantiation(instance):
    assert isinstance(instance, pp2::ImportExpression)

@given(instance=pp2::ParenthesisedExpression_strategy)
@settings(max_examples=50)
def test_pp2::parenthesisedexpression_instantiation(instance):
    assert isinstance(instance, pp2::ParenthesisedExpression)

@given(instance=pp2::SeparatorExpression_strategy)
@settings(max_examples=50)
def test_pp2::separatorexpression_instantiation(instance):
    assert isinstance(instance, pp2::SeparatorExpression)

@given(instance=pp2::StringExpression_strategy)
@settings(max_examples=50)
def test_pp2::stringexpression_instantiation(instance):
    assert isinstance(instance, pp2::StringExpression)

@given(instance=pp2::ParameterizedExpression_strategy)
@settings(max_examples=50)
def test_pp2::parameterizedexpression_instantiation(instance):
    assert isinstance(instance, pp2::ParameterizedExpression)

@given(instance=pp2::CollectExpression_strategy)
@settings(max_examples=50)
def test_pp2::collectexpression_instantiation(instance):
    assert isinstance(instance, pp2::CollectExpression)

@given(instance=pp2::CaseExpression_strategy)
@settings(max_examples=50)
def test_pp2::caseexpression_instantiation(instance):
    assert isinstance(instance, pp2::CaseExpression)

@given(instance=pp2::DefinitionArgument_strategy)
@settings(max_examples=50)
def test_pp2::definitionargument_instantiation(instance):
    assert isinstance(instance, pp2::DefinitionArgument)

@given(instance=pp2::DefinitionArgument_strategy)
def test_pp2::definitionargument_argName_type(instance):
    assert isinstance(instance.argName, str)


@given(instance=pp2::DefinitionArgument_strategy)
def test_pp2::definitionargument_argName_setter(instance):
    original = instance.argName
    instance.argName = original
    assert instance.argName == original

@given(instance=pp2::DefinitionArgument_strategy)
def test_pp2::definitionargument_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=pp2::DefinitionArgument_strategy)
def test_pp2::definitionargument_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=pp2::DefinitionArgumentList_strategy)
@settings(max_examples=50)
def test_pp2::definitionargumentlist_instantiation(instance):
    assert isinstance(instance, pp2::DefinitionArgumentList)

@given(instance=pp2::PuppetManifest_strategy)
@settings(max_examples=50)
def test_pp2::puppetmanifest_instantiation(instance):
    assert isinstance(instance, pp2::PuppetManifest)
