import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Lambda,
    pp_RubyLambda,
    pp_JavaLambda,
    TextExpression,
    pp_VariableTE,
    pp_ExpressionTE,
    pp_VerbatimTE,
    pp_TextExpression,
    IQuotedString,
    StringExpression,
    pp_UnquotedString,
    pp_SingleQuotedString,
    pp_DoubleQuotedString,
    IfExpression,
    pp_ElseIfExpression,
    ParameterizedExpression,
    pp_WithLambdaExpression,
    pp_AtExpression,
    BinaryExpression,
    pp_AndExpression,
    pp_NamedAccessExpression,
    pp_AppendExpression,
    pp_OrExpression,
    pp_AssignmentExpression,
    BinaryOpExpression,
    pp_RelationalExpression,
    pp_EqualityExpression,
    pp_ShiftExpression,
    pp_AdditiveExpression,
    pp_MatchingExpression,
    pp_InExpression,
    pp_MultiplicativeExpression,
    pp_RelationshipExpression,
    pp_BinaryOpExpression,
    WithLambdaExpression,
    pp_MethodCall,
    pp_FunctionCall,
    pp_SelectorEntry,
    pp_SelectorExpression,
    LiteralExpression,
    pp_LiteralName,
    pp_LiteralBoolean,
    pp_LiteralRegex,
    pp_VirtualNameOrReference,
    pp_LiteralUndef,
    pp_LiteralClass,
    pp_LiteralDefault,
    pp_LiteralNameOrReference,
    pp_Case,
    pp_HashEntry,
    pp_LiteralHash,
    pp_LiteralList,
    pp_IQuotedString,
    Expression,
    pp_CaseExpression,
    pp_BinaryExpression,
    pp_UnlessExpression,
    pp_ExpressionBlock,
    pp_SeparatorExpression,
    pp_NodeDefinition,
    pp_IfExpression,
    pp_ExprList,
    pp_ParenthesisedExpression,
    pp_ImportExpression,
    pp_VariableExpression,
    pp_ResourceExpression,
    pp_UnaryExpression,
    pp_InterpolatedVariable,
    pp_CollectExpression,
    pp_ParameterizedExpression,
    pp_StringExpression,
    pp_Definition,
    pp_LiteralExpression,
    Definition,
    pp_HostClassDefinition,
    ICollectQuery,
    UnaryExpression,
    pp_ExportedCollectQuery,
    pp_UnaryMinusExpression,
    pp_UnaryNotExpression,
    pp_VirtualCollectQuery,
    pp_ICollectQuery,
    pp_AttributeOperation,
    pp_AttributeOperations,
    pp_ResourceBody,
    pp_Expression,
    ExpressionBlock,
    pp_Lambda,
    pp_ElseExpression,
    pp_PuppetManifest,
    pp_DefinitionArgument,
    pp_DefinitionArgumentList,
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



def test_pp_rubylambda_is_not_abstract():
    assert not inspect.isabstract(pp_RubyLambda)


def test_pp_rubylambda_constructor_exists():
    assert callable(pp_RubyLambda.__init__)


def test_pp_rubylambda_constructor_args():
    sig = inspect.signature(pp_RubyLambda.__init__)
    params = list(sig.parameters.keys())



def test_pp_javalambda_is_not_abstract():
    assert not inspect.isabstract(pp_JavaLambda)


def test_pp_javalambda_constructor_exists():
    assert callable(pp_JavaLambda.__init__)


def test_pp_javalambda_constructor_args():
    sig = inspect.signature(pp_JavaLambda.__init__)
    params = list(sig.parameters.keys())
    assert "farrow" in params, "Missing parameter 'farrow'"

def test_pp_javalambda_has_farrow():
    assert hasattr(pp_JavaLambda, "farrow")
    descriptor = None
    for klass in pp_JavaLambda.__mro__:
        if "farrow" in klass.__dict__:
            descriptor = klass.__dict__["farrow"]
            break
    assert isinstance(descriptor, property)



def test_textexpression_is_not_abstract():
    assert not inspect.isabstract(TextExpression)


def test_textexpression_constructor_exists():
    assert callable(TextExpression.__init__)


def test_textexpression_constructor_args():
    sig = inspect.signature(TextExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_variablete_is_not_abstract():
    assert not inspect.isabstract(pp_VariableTE)


def test_pp_variablete_constructor_exists():
    assert callable(pp_VariableTE.__init__)


def test_pp_variablete_constructor_args():
    sig = inspect.signature(pp_VariableTE.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_pp_variablete_has_varName():
    assert hasattr(pp_VariableTE, "varName")
    descriptor = None
    for klass in pp_VariableTE.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_pp_expressionte_is_not_abstract():
    assert not inspect.isabstract(pp_ExpressionTE)


def test_pp_expressionte_constructor_exists():
    assert callable(pp_ExpressionTE.__init__)


def test_pp_expressionte_constructor_args():
    sig = inspect.signature(pp_ExpressionTE.__init__)
    params = list(sig.parameters.keys())



def test_pp_verbatimte_is_not_abstract():
    assert not inspect.isabstract(pp_VerbatimTE)


def test_pp_verbatimte_constructor_exists():
    assert callable(pp_VerbatimTE.__init__)


def test_pp_verbatimte_constructor_args():
    sig = inspect.signature(pp_VerbatimTE.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_pp_verbatimte_has_text():
    assert hasattr(pp_VerbatimTE, "text")
    descriptor = None
    for klass in pp_VerbatimTE.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_pp_textexpression_is_not_abstract():
    assert not inspect.isabstract(pp_TextExpression)


def test_pp_textexpression_constructor_exists():
    assert callable(pp_TextExpression.__init__)


def test_pp_textexpression_constructor_args():
    sig = inspect.signature(pp_TextExpression.__init__)
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



def test_pp_unquotedstring_is_not_abstract():
    assert not inspect.isabstract(pp_UnquotedString)


def test_pp_unquotedstring_constructor_exists():
    assert callable(pp_UnquotedString.__init__)


def test_pp_unquotedstring_constructor_args():
    sig = inspect.signature(pp_UnquotedString.__init__)
    params = list(sig.parameters.keys())



def test_pp_singlequotedstring_is_not_abstract():
    assert not inspect.isabstract(pp_SingleQuotedString)


def test_pp_singlequotedstring_constructor_exists():
    assert callable(pp_SingleQuotedString.__init__)


def test_pp_singlequotedstring_constructor_args():
    sig = inspect.signature(pp_SingleQuotedString.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_pp_singlequotedstring_has_text():
    assert hasattr(pp_SingleQuotedString, "text")
    descriptor = None
    for klass in pp_SingleQuotedString.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_pp_doublequotedstring_is_not_abstract():
    assert not inspect.isabstract(pp_DoubleQuotedString)


def test_pp_doublequotedstring_constructor_exists():
    assert callable(pp_DoubleQuotedString.__init__)


def test_pp_doublequotedstring_constructor_args():
    sig = inspect.signature(pp_DoubleQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_ifexpression_is_not_abstract():
    assert not inspect.isabstract(IfExpression)


def test_ifexpression_constructor_exists():
    assert callable(IfExpression.__init__)


def test_ifexpression_constructor_args():
    sig = inspect.signature(IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_elseifexpression_is_not_abstract():
    assert not inspect.isabstract(pp_ElseIfExpression)


def test_pp_elseifexpression_constructor_exists():
    assert callable(pp_ElseIfExpression.__init__)


def test_pp_elseifexpression_constructor_args():
    sig = inspect.signature(pp_ElseIfExpression.__init__)
    params = list(sig.parameters.keys())



def test_parameterizedexpression_is_not_abstract():
    assert not inspect.isabstract(ParameterizedExpression)


def test_parameterizedexpression_constructor_exists():
    assert callable(ParameterizedExpression.__init__)


def test_parameterizedexpression_constructor_args():
    sig = inspect.signature(ParameterizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_withlambdaexpression_is_not_abstract():
    assert not inspect.isabstract(pp_WithLambdaExpression)


def test_pp_withlambdaexpression_constructor_exists():
    assert callable(pp_WithLambdaExpression.__init__)


def test_pp_withlambdaexpression_constructor_args():
    sig = inspect.signature(pp_WithLambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_atexpression_is_not_abstract():
    assert not inspect.isabstract(pp_AtExpression)


def test_pp_atexpression_constructor_exists():
    assert callable(pp_AtExpression.__init__)


def test_pp_atexpression_constructor_args():
    sig = inspect.signature(pp_AtExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_andexpression_is_not_abstract():
    assert not inspect.isabstract(pp_AndExpression)


def test_pp_andexpression_constructor_exists():
    assert callable(pp_AndExpression.__init__)


def test_pp_andexpression_constructor_args():
    sig = inspect.signature(pp_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_namedaccessexpression_is_not_abstract():
    assert not inspect.isabstract(pp_NamedAccessExpression)


def test_pp_namedaccessexpression_constructor_exists():
    assert callable(pp_NamedAccessExpression.__init__)


def test_pp_namedaccessexpression_constructor_args():
    sig = inspect.signature(pp_NamedAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_appendexpression_is_not_abstract():
    assert not inspect.isabstract(pp_AppendExpression)


def test_pp_appendexpression_constructor_exists():
    assert callable(pp_AppendExpression.__init__)


def test_pp_appendexpression_constructor_args():
    sig = inspect.signature(pp_AppendExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_orexpression_is_not_abstract():
    assert not inspect.isabstract(pp_OrExpression)


def test_pp_orexpression_constructor_exists():
    assert callable(pp_OrExpression.__init__)


def test_pp_orexpression_constructor_args():
    sig = inspect.signature(pp_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(pp_AssignmentExpression)


def test_pp_assignmentexpression_constructor_exists():
    assert callable(pp_AssignmentExpression.__init__)


def test_pp_assignmentexpression_constructor_args():
    sig = inspect.signature(pp_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOpExpression)


def test_binaryopexpression_constructor_exists():
    assert callable(BinaryOpExpression.__init__)


def test_binaryopexpression_constructor_args():
    sig = inspect.signature(BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(pp_RelationalExpression)


def test_pp_relationalexpression_constructor_exists():
    assert callable(pp_RelationalExpression.__init__)


def test_pp_relationalexpression_constructor_args():
    sig = inspect.signature(pp_RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(pp_EqualityExpression)


def test_pp_equalityexpression_constructor_exists():
    assert callable(pp_EqualityExpression.__init__)


def test_pp_equalityexpression_constructor_args():
    sig = inspect.signature(pp_EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(pp_ShiftExpression)


def test_pp_shiftexpression_constructor_exists():
    assert callable(pp_ShiftExpression.__init__)


def test_pp_shiftexpression_constructor_args():
    sig = inspect.signature(pp_ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(pp_AdditiveExpression)


def test_pp_additiveexpression_constructor_exists():
    assert callable(pp_AdditiveExpression.__init__)


def test_pp_additiveexpression_constructor_args():
    sig = inspect.signature(pp_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_matchingexpression_is_not_abstract():
    assert not inspect.isabstract(pp_MatchingExpression)


def test_pp_matchingexpression_constructor_exists():
    assert callable(pp_MatchingExpression.__init__)


def test_pp_matchingexpression_constructor_args():
    sig = inspect.signature(pp_MatchingExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_inexpression_is_not_abstract():
    assert not inspect.isabstract(pp_InExpression)


def test_pp_inexpression_constructor_exists():
    assert callable(pp_InExpression.__init__)


def test_pp_inexpression_constructor_args():
    sig = inspect.signature(pp_InExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(pp_MultiplicativeExpression)


def test_pp_multiplicativeexpression_constructor_exists():
    assert callable(pp_MultiplicativeExpression.__init__)


def test_pp_multiplicativeexpression_constructor_args():
    sig = inspect.signature(pp_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_relationshipexpression_is_not_abstract():
    assert not inspect.isabstract(pp_RelationshipExpression)


def test_pp_relationshipexpression_constructor_exists():
    assert callable(pp_RelationshipExpression.__init__)


def test_pp_relationshipexpression_constructor_args():
    sig = inspect.signature(pp_RelationshipExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(pp_BinaryOpExpression)


def test_pp_binaryopexpression_constructor_exists():
    assert callable(pp_BinaryOpExpression.__init__)


def test_pp_binaryopexpression_constructor_args():
    sig = inspect.signature(pp_BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_pp_binaryopexpression_has_opName():
    assert hasattr(pp_BinaryOpExpression, "opName")
    descriptor = None
    for klass in pp_BinaryOpExpression.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_withlambdaexpression_is_not_abstract():
    assert not inspect.isabstract(WithLambdaExpression)


def test_withlambdaexpression_constructor_exists():
    assert callable(WithLambdaExpression.__init__)


def test_withlambdaexpression_constructor_args():
    sig = inspect.signature(WithLambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_methodcall_is_not_abstract():
    assert not inspect.isabstract(pp_MethodCall)


def test_pp_methodcall_constructor_exists():
    assert callable(pp_MethodCall.__init__)


def test_pp_methodcall_constructor_args():
    sig = inspect.signature(pp_MethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "parenthesized" in params, "Missing parameter 'parenthesized'"

def test_pp_methodcall_has_parenthesized():
    assert hasattr(pp_MethodCall, "parenthesized")
    descriptor = None
    for klass in pp_MethodCall.__mro__:
        if "parenthesized" in klass.__dict__:
            descriptor = klass.__dict__["parenthesized"]
            break
    assert isinstance(descriptor, property)



def test_pp_functioncall_is_not_abstract():
    assert not inspect.isabstract(pp_FunctionCall)


def test_pp_functioncall_constructor_exists():
    assert callable(pp_FunctionCall.__init__)


def test_pp_functioncall_constructor_args():
    sig = inspect.signature(pp_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_pp_selectorentry_is_not_abstract():
    assert not inspect.isabstract(pp_SelectorEntry)


def test_pp_selectorentry_constructor_exists():
    assert callable(pp_SelectorEntry.__init__)


def test_pp_selectorentry_constructor_args():
    sig = inspect.signature(pp_SelectorEntry.__init__)
    params = list(sig.parameters.keys())



def test_pp_selectorexpression_is_not_abstract():
    assert not inspect.isabstract(pp_SelectorExpression)


def test_pp_selectorexpression_constructor_exists():
    assert callable(pp_SelectorExpression.__init__)


def test_pp_selectorexpression_constructor_args():
    sig = inspect.signature(pp_SelectorExpression.__init__)
    params = list(sig.parameters.keys())



def test_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_literalname_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralName)


def test_pp_literalname_constructor_exists():
    assert callable(pp_LiteralName.__init__)


def test_pp_literalname_constructor_args():
    sig = inspect.signature(pp_LiteralName.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp_literalname_has_value():
    assert hasattr(pp_LiteralName, "value")
    descriptor = None
    for klass in pp_LiteralName.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp_literalboolean_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralBoolean)


def test_pp_literalboolean_constructor_exists():
    assert callable(pp_LiteralBoolean.__init__)


def test_pp_literalboolean_constructor_args():
    sig = inspect.signature(pp_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp_literalboolean_has_value():
    assert hasattr(pp_LiteralBoolean, "value")
    descriptor = None
    for klass in pp_LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp_literalregex_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralRegex)


def test_pp_literalregex_constructor_exists():
    assert callable(pp_LiteralRegex.__init__)


def test_pp_literalregex_constructor_args():
    sig = inspect.signature(pp_LiteralRegex.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp_literalregex_has_value():
    assert hasattr(pp_LiteralRegex, "value")
    descriptor = None
    for klass in pp_LiteralRegex.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp_virtualnameorreference_is_not_abstract():
    assert not inspect.isabstract(pp_VirtualNameOrReference)


def test_pp_virtualnameorreference_constructor_exists():
    assert callable(pp_VirtualNameOrReference.__init__)


def test_pp_virtualnameorreference_constructor_args():
    sig = inspect.signature(pp_VirtualNameOrReference.__init__)
    params = list(sig.parameters.keys())
    assert "exported" in params, "Missing parameter 'exported'"
    assert "value" in params, "Missing parameter 'value'"

def test_pp_virtualnameorreference_has_exported():
    assert hasattr(pp_VirtualNameOrReference, "exported")
    descriptor = None
    for klass in pp_VirtualNameOrReference.__mro__:
        if "exported" in klass.__dict__:
            descriptor = klass.__dict__["exported"]
            break
    assert isinstance(descriptor, property)

def test_pp_virtualnameorreference_has_value():
    assert hasattr(pp_VirtualNameOrReference, "value")
    descriptor = None
    for klass in pp_VirtualNameOrReference.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp_literalundef_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralUndef)


def test_pp_literalundef_constructor_exists():
    assert callable(pp_LiteralUndef.__init__)


def test_pp_literalundef_constructor_args():
    sig = inspect.signature(pp_LiteralUndef.__init__)
    params = list(sig.parameters.keys())



def test_pp_literalclass_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralClass)


def test_pp_literalclass_constructor_exists():
    assert callable(pp_LiteralClass.__init__)


def test_pp_literalclass_constructor_args():
    sig = inspect.signature(pp_LiteralClass.__init__)
    params = list(sig.parameters.keys())



def test_pp_literaldefault_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralDefault)


def test_pp_literaldefault_constructor_exists():
    assert callable(pp_LiteralDefault.__init__)


def test_pp_literaldefault_constructor_args():
    sig = inspect.signature(pp_LiteralDefault.__init__)
    params = list(sig.parameters.keys())



def test_pp_literalnameorreference_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralNameOrReference)


def test_pp_literalnameorreference_constructor_exists():
    assert callable(pp_LiteralNameOrReference.__init__)


def test_pp_literalnameorreference_constructor_args():
    sig = inspect.signature(pp_LiteralNameOrReference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp_literalnameorreference_has_value():
    assert hasattr(pp_LiteralNameOrReference, "value")
    descriptor = None
    for klass in pp_LiteralNameOrReference.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp_case_is_not_abstract():
    assert not inspect.isabstract(pp_Case)


def test_pp_case_constructor_exists():
    assert callable(pp_Case.__init__)


def test_pp_case_constructor_args():
    sig = inspect.signature(pp_Case.__init__)
    params = list(sig.parameters.keys())



def test_pp_hashentry_is_not_abstract():
    assert not inspect.isabstract(pp_HashEntry)


def test_pp_hashentry_constructor_exists():
    assert callable(pp_HashEntry.__init__)


def test_pp_hashentry_constructor_args():
    sig = inspect.signature(pp_HashEntry.__init__)
    params = list(sig.parameters.keys())



def test_pp_literalhash_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralHash)


def test_pp_literalhash_constructor_exists():
    assert callable(pp_LiteralHash.__init__)


def test_pp_literalhash_constructor_args():
    sig = inspect.signature(pp_LiteralHash.__init__)
    params = list(sig.parameters.keys())



def test_pp_literallist_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralList)


def test_pp_literallist_constructor_exists():
    assert callable(pp_LiteralList.__init__)


def test_pp_literallist_constructor_args():
    sig = inspect.signature(pp_LiteralList.__init__)
    params = list(sig.parameters.keys())



def test_pp_iquotedstring_is_not_abstract():
    assert not inspect.isabstract(pp_IQuotedString)


def test_pp_iquotedstring_constructor_exists():
    assert callable(pp_IQuotedString.__init__)


def test_pp_iquotedstring_constructor_args():
    sig = inspect.signature(pp_IQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_pp_caseexpression_is_not_abstract():
    assert not inspect.isabstract(pp_CaseExpression)


def test_pp_caseexpression_constructor_exists():
    assert callable(pp_CaseExpression.__init__)


def test_pp_caseexpression_constructor_args():
    sig = inspect.signature(pp_CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(pp_BinaryExpression)


def test_pp_binaryexpression_constructor_exists():
    assert callable(pp_BinaryExpression.__init__)


def test_pp_binaryexpression_constructor_args():
    sig = inspect.signature(pp_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_unlessexpression_is_not_abstract():
    assert not inspect.isabstract(pp_UnlessExpression)


def test_pp_unlessexpression_constructor_exists():
    assert callable(pp_UnlessExpression.__init__)


def test_pp_unlessexpression_constructor_args():
    sig = inspect.signature(pp_UnlessExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_expressionblock_is_not_abstract():
    assert not inspect.isabstract(pp_ExpressionBlock)


def test_pp_expressionblock_constructor_exists():
    assert callable(pp_ExpressionBlock.__init__)


def test_pp_expressionblock_constructor_args():
    sig = inspect.signature(pp_ExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_pp_separatorexpression_is_not_abstract():
    assert not inspect.isabstract(pp_SeparatorExpression)


def test_pp_separatorexpression_constructor_exists():
    assert callable(pp_SeparatorExpression.__init__)


def test_pp_separatorexpression_constructor_args():
    sig = inspect.signature(pp_SeparatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_nodedefinition_is_not_abstract():
    assert not inspect.isabstract(pp_NodeDefinition)


def test_pp_nodedefinition_constructor_exists():
    assert callable(pp_NodeDefinition.__init__)


def test_pp_nodedefinition_constructor_args():
    sig = inspect.signature(pp_NodeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_pp_ifexpression_is_not_abstract():
    assert not inspect.isabstract(pp_IfExpression)


def test_pp_ifexpression_constructor_exists():
    assert callable(pp_IfExpression.__init__)


def test_pp_ifexpression_constructor_args():
    sig = inspect.signature(pp_IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_exprlist_is_not_abstract():
    assert not inspect.isabstract(pp_ExprList)


def test_pp_exprlist_constructor_exists():
    assert callable(pp_ExprList.__init__)


def test_pp_exprlist_constructor_args():
    sig = inspect.signature(pp_ExprList.__init__)
    params = list(sig.parameters.keys())



def test_pp_parenthesisedexpression_is_not_abstract():
    assert not inspect.isabstract(pp_ParenthesisedExpression)


def test_pp_parenthesisedexpression_constructor_exists():
    assert callable(pp_ParenthesisedExpression.__init__)


def test_pp_parenthesisedexpression_constructor_args():
    sig = inspect.signature(pp_ParenthesisedExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_importexpression_is_not_abstract():
    assert not inspect.isabstract(pp_ImportExpression)


def test_pp_importexpression_constructor_exists():
    assert callable(pp_ImportExpression.__init__)


def test_pp_importexpression_constructor_args():
    sig = inspect.signature(pp_ImportExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_variableexpression_is_not_abstract():
    assert not inspect.isabstract(pp_VariableExpression)


def test_pp_variableexpression_constructor_exists():
    assert callable(pp_VariableExpression.__init__)


def test_pp_variableexpression_constructor_args():
    sig = inspect.signature(pp_VariableExpression.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_pp_variableexpression_has_varName():
    assert hasattr(pp_VariableExpression, "varName")
    descriptor = None
    for klass in pp_VariableExpression.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_pp_resourceexpression_is_not_abstract():
    assert not inspect.isabstract(pp_ResourceExpression)


def test_pp_resourceexpression_constructor_exists():
    assert callable(pp_ResourceExpression.__init__)


def test_pp_resourceexpression_constructor_args():
    sig = inspect.signature(pp_ResourceExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(pp_UnaryExpression)


def test_pp_unaryexpression_constructor_exists():
    assert callable(pp_UnaryExpression.__init__)


def test_pp_unaryexpression_constructor_args():
    sig = inspect.signature(pp_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_interpolatedvariable_is_not_abstract():
    assert not inspect.isabstract(pp_InterpolatedVariable)


def test_pp_interpolatedvariable_constructor_exists():
    assert callable(pp_InterpolatedVariable.__init__)


def test_pp_interpolatedvariable_constructor_args():
    sig = inspect.signature(pp_InterpolatedVariable.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_pp_interpolatedvariable_has_varName():
    assert hasattr(pp_InterpolatedVariable, "varName")
    descriptor = None
    for klass in pp_InterpolatedVariable.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_pp_collectexpression_is_not_abstract():
    assert not inspect.isabstract(pp_CollectExpression)


def test_pp_collectexpression_constructor_exists():
    assert callable(pp_CollectExpression.__init__)


def test_pp_collectexpression_constructor_args():
    sig = inspect.signature(pp_CollectExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_parameterizedexpression_is_not_abstract():
    assert not inspect.isabstract(pp_ParameterizedExpression)


def test_pp_parameterizedexpression_constructor_exists():
    assert callable(pp_ParameterizedExpression.__init__)


def test_pp_parameterizedexpression_constructor_args():
    sig = inspect.signature(pp_ParameterizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_stringexpression_is_not_abstract():
    assert not inspect.isabstract(pp_StringExpression)


def test_pp_stringexpression_constructor_exists():
    assert callable(pp_StringExpression.__init__)


def test_pp_stringexpression_constructor_args():
    sig = inspect.signature(pp_StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_definition_is_not_abstract():
    assert not inspect.isabstract(pp_Definition)


def test_pp_definition_constructor_exists():
    assert callable(pp_Definition.__init__)


def test_pp_definition_constructor_args():
    sig = inspect.signature(pp_Definition.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"

def test_pp_definition_has_className():
    assert hasattr(pp_Definition, "className")
    descriptor = None
    for klass in pp_Definition.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_pp_literalexpression_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralExpression)


def test_pp_literalexpression_constructor_exists():
    assert callable(pp_LiteralExpression.__init__)


def test_pp_literalexpression_constructor_args():
    sig = inspect.signature(pp_LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_pp_hostclassdefinition_is_not_abstract():
    assert not inspect.isabstract(pp_HostClassDefinition)


def test_pp_hostclassdefinition_constructor_exists():
    assert callable(pp_HostClassDefinition.__init__)


def test_pp_hostclassdefinition_constructor_args():
    sig = inspect.signature(pp_HostClassDefinition.__init__)
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



def test_pp_exportedcollectquery_is_not_abstract():
    assert not inspect.isabstract(pp_ExportedCollectQuery)


def test_pp_exportedcollectquery_constructor_exists():
    assert callable(pp_ExportedCollectQuery.__init__)


def test_pp_exportedcollectquery_constructor_args():
    sig = inspect.signature(pp_ExportedCollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_pp_unaryminusexpression_is_not_abstract():
    assert not inspect.isabstract(pp_UnaryMinusExpression)


def test_pp_unaryminusexpression_constructor_exists():
    assert callable(pp_UnaryMinusExpression.__init__)


def test_pp_unaryminusexpression_constructor_args():
    sig = inspect.signature(pp_UnaryMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_unarynotexpression_is_not_abstract():
    assert not inspect.isabstract(pp_UnaryNotExpression)


def test_pp_unarynotexpression_constructor_exists():
    assert callable(pp_UnaryNotExpression.__init__)


def test_pp_unarynotexpression_constructor_args():
    sig = inspect.signature(pp_UnaryNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_virtualcollectquery_is_not_abstract():
    assert not inspect.isabstract(pp_VirtualCollectQuery)


def test_pp_virtualcollectquery_constructor_exists():
    assert callable(pp_VirtualCollectQuery.__init__)


def test_pp_virtualcollectquery_constructor_args():
    sig = inspect.signature(pp_VirtualCollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_pp_icollectquery_is_not_abstract():
    assert not inspect.isabstract(pp_ICollectQuery)


def test_pp_icollectquery_constructor_exists():
    assert callable(pp_ICollectQuery.__init__)


def test_pp_icollectquery_constructor_args():
    sig = inspect.signature(pp_ICollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_pp_attributeoperation_is_not_abstract():
    assert not inspect.isabstract(pp_AttributeOperation)


def test_pp_attributeoperation_constructor_exists():
    assert callable(pp_AttributeOperation.__init__)


def test_pp_attributeoperation_constructor_args():
    sig = inspect.signature(pp_AttributeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "key" in params, "Missing parameter 'key'"

def test_pp_attributeoperation_has_op():
    assert hasattr(pp_AttributeOperation, "op")
    descriptor = None
    for klass in pp_AttributeOperation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_pp_attributeoperation_has_key():
    assert hasattr(pp_AttributeOperation, "key")
    descriptor = None
    for klass in pp_AttributeOperation.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_pp_attributeoperations_is_not_abstract():
    assert not inspect.isabstract(pp_AttributeOperations)


def test_pp_attributeoperations_constructor_exists():
    assert callable(pp_AttributeOperations.__init__)


def test_pp_attributeoperations_constructor_args():
    sig = inspect.signature(pp_AttributeOperations.__init__)
    params = list(sig.parameters.keys())



def test_pp_resourcebody_is_not_abstract():
    assert not inspect.isabstract(pp_ResourceBody)


def test_pp_resourcebody_constructor_exists():
    assert callable(pp_ResourceBody.__init__)


def test_pp_resourcebody_constructor_args():
    sig = inspect.signature(pp_ResourceBody.__init__)
    params = list(sig.parameters.keys())



def test_pp_expression_is_not_abstract():
    assert not inspect.isabstract(pp_Expression)


def test_pp_expression_constructor_exists():
    assert callable(pp_Expression.__init__)


def test_pp_expression_constructor_args():
    sig = inspect.signature(pp_Expression.__init__)
    params = list(sig.parameters.keys())



def test_expressionblock_is_not_abstract():
    assert not inspect.isabstract(ExpressionBlock)


def test_expressionblock_constructor_exists():
    assert callable(ExpressionBlock.__init__)


def test_expressionblock_constructor_args():
    sig = inspect.signature(ExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_pp_lambda_is_not_abstract():
    assert not inspect.isabstract(pp_Lambda)


def test_pp_lambda_constructor_exists():
    assert callable(pp_Lambda.__init__)


def test_pp_lambda_constructor_args():
    sig = inspect.signature(pp_Lambda.__init__)
    params = list(sig.parameters.keys())



def test_pp_elseexpression_is_not_abstract():
    assert not inspect.isabstract(pp_ElseExpression)


def test_pp_elseexpression_constructor_exists():
    assert callable(pp_ElseExpression.__init__)


def test_pp_elseexpression_constructor_args():
    sig = inspect.signature(pp_ElseExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp_puppetmanifest_is_not_abstract():
    assert not inspect.isabstract(pp_PuppetManifest)


def test_pp_puppetmanifest_constructor_exists():
    assert callable(pp_PuppetManifest.__init__)


def test_pp_puppetmanifest_constructor_args():
    sig = inspect.signature(pp_PuppetManifest.__init__)
    params = list(sig.parameters.keys())



def test_pp_definitionargument_is_not_abstract():
    assert not inspect.isabstract(pp_DefinitionArgument)


def test_pp_definitionargument_constructor_exists():
    assert callable(pp_DefinitionArgument.__init__)


def test_pp_definitionargument_constructor_args():
    sig = inspect.signature(pp_DefinitionArgument.__init__)
    params = list(sig.parameters.keys())
    assert "argName" in params, "Missing parameter 'argName'"
    assert "op" in params, "Missing parameter 'op'"

def test_pp_definitionargument_has_argName():
    assert hasattr(pp_DefinitionArgument, "argName")
    descriptor = None
    for klass in pp_DefinitionArgument.__mro__:
        if "argName" in klass.__dict__:
            descriptor = klass.__dict__["argName"]
            break
    assert isinstance(descriptor, property)

def test_pp_definitionargument_has_op():
    assert hasattr(pp_DefinitionArgument, "op")
    descriptor = None
    for klass in pp_DefinitionArgument.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_pp_definitionargumentlist_is_not_abstract():
    assert not inspect.isabstract(pp_DefinitionArgumentList)


def test_pp_definitionargumentlist_constructor_exists():
    assert callable(pp_DefinitionArgumentList.__init__)


def test_pp_definitionargumentlist_constructor_args():
    sig = inspect.signature(pp_DefinitionArgumentList.__init__)
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
pp_RubyLambda_strategy = st.builds(
    pp_RubyLambda,
)
pp_JavaLambda_strategy = st.builds(
    pp_JavaLambda,
    farrow=
        st.booleans()
)
TextExpression_strategy = st.builds(
    TextExpression,
)
pp_VariableTE_strategy = st.builds(
    pp_VariableTE,
    varName=
        safe_text
)
pp_ExpressionTE_strategy = st.builds(
    pp_ExpressionTE,
)
pp_VerbatimTE_strategy = st.builds(
    pp_VerbatimTE,
    text=
        safe_text
)
pp_TextExpression_strategy = st.builds(
    pp_TextExpression,
)
IQuotedString_strategy = st.builds(
    IQuotedString,
)
StringExpression_strategy = st.builds(
    StringExpression,
)
pp_UnquotedString_strategy = st.builds(
    pp_UnquotedString,
)
pp_SingleQuotedString_strategy = st.builds(
    pp_SingleQuotedString,
    text=
        safe_text
)
pp_DoubleQuotedString_strategy = st.builds(
    pp_DoubleQuotedString,
)
IfExpression_strategy = st.builds(
    IfExpression,
)
pp_ElseIfExpression_strategy = st.builds(
    pp_ElseIfExpression,
)
ParameterizedExpression_strategy = st.builds(
    ParameterizedExpression,
)
pp_WithLambdaExpression_strategy = st.builds(
    pp_WithLambdaExpression,
)
pp_AtExpression_strategy = st.builds(
    pp_AtExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
pp_AndExpression_strategy = st.builds(
    pp_AndExpression,
)
pp_NamedAccessExpression_strategy = st.builds(
    pp_NamedAccessExpression,
)
pp_AppendExpression_strategy = st.builds(
    pp_AppendExpression,
)
pp_OrExpression_strategy = st.builds(
    pp_OrExpression,
)
pp_AssignmentExpression_strategy = st.builds(
    pp_AssignmentExpression,
)
BinaryOpExpression_strategy = st.builds(
    BinaryOpExpression,
)
pp_RelationalExpression_strategy = st.builds(
    pp_RelationalExpression,
)
pp_EqualityExpression_strategy = st.builds(
    pp_EqualityExpression,
)
pp_ShiftExpression_strategy = st.builds(
    pp_ShiftExpression,
)
pp_AdditiveExpression_strategy = st.builds(
    pp_AdditiveExpression,
)
pp_MatchingExpression_strategy = st.builds(
    pp_MatchingExpression,
)
pp_InExpression_strategy = st.builds(
    pp_InExpression,
)
pp_MultiplicativeExpression_strategy = st.builds(
    pp_MultiplicativeExpression,
)
pp_RelationshipExpression_strategy = st.builds(
    pp_RelationshipExpression,
)
pp_BinaryOpExpression_strategy = st.builds(
    pp_BinaryOpExpression,
    opName=
        safe_text
)
WithLambdaExpression_strategy = st.builds(
    WithLambdaExpression,
)
pp_MethodCall_strategy = st.builds(
    pp_MethodCall,
    parenthesized=
        st.booleans()
)
pp_FunctionCall_strategy = st.builds(
    pp_FunctionCall,
)
pp_SelectorEntry_strategy = st.builds(
    pp_SelectorEntry,
)
pp_SelectorExpression_strategy = st.builds(
    pp_SelectorExpression,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
pp_LiteralName_strategy = st.builds(
    pp_LiteralName,
    value=
        safe_text
)
pp_LiteralBoolean_strategy = st.builds(
    pp_LiteralBoolean,
    value=
        st.booleans()
)
pp_LiteralRegex_strategy = st.builds(
    pp_LiteralRegex,
    value=
        safe_text
)
pp_VirtualNameOrReference_strategy = st.builds(
    pp_VirtualNameOrReference,
    exported=
        st.booleans(),
    value=
        safe_text
)
pp_LiteralUndef_strategy = st.builds(
    pp_LiteralUndef,
)
pp_LiteralClass_strategy = st.builds(
    pp_LiteralClass,
)
pp_LiteralDefault_strategy = st.builds(
    pp_LiteralDefault,
)
pp_LiteralNameOrReference_strategy = st.builds(
    pp_LiteralNameOrReference,
    value=
        safe_text
)
pp_Case_strategy = st.builds(
    pp_Case,
)
pp_HashEntry_strategy = st.builds(
    pp_HashEntry,
)
pp_LiteralHash_strategy = st.builds(
    pp_LiteralHash,
)
pp_LiteralList_strategy = st.builds(
    pp_LiteralList,
)
pp_IQuotedString_strategy = st.builds(
    pp_IQuotedString,
)
Expression_strategy = st.builds(
    Expression,
)
pp_CaseExpression_strategy = st.builds(
    pp_CaseExpression,
)
pp_BinaryExpression_strategy = st.builds(
    pp_BinaryExpression,
)
pp_UnlessExpression_strategy = st.builds(
    pp_UnlessExpression,
)
pp_ExpressionBlock_strategy = st.builds(
    pp_ExpressionBlock,
)
pp_SeparatorExpression_strategy = st.builds(
    pp_SeparatorExpression,
)
pp_NodeDefinition_strategy = st.builds(
    pp_NodeDefinition,
)
pp_IfExpression_strategy = st.builds(
    pp_IfExpression,
)
pp_ExprList_strategy = st.builds(
    pp_ExprList,
)
pp_ParenthesisedExpression_strategy = st.builds(
    pp_ParenthesisedExpression,
)
pp_ImportExpression_strategy = st.builds(
    pp_ImportExpression,
)
pp_VariableExpression_strategy = st.builds(
    pp_VariableExpression,
    varName=
        safe_text
)
pp_ResourceExpression_strategy = st.builds(
    pp_ResourceExpression,
)
pp_UnaryExpression_strategy = st.builds(
    pp_UnaryExpression,
)
pp_InterpolatedVariable_strategy = st.builds(
    pp_InterpolatedVariable,
    varName=
        safe_text
)
pp_CollectExpression_strategy = st.builds(
    pp_CollectExpression,
)
pp_ParameterizedExpression_strategy = st.builds(
    pp_ParameterizedExpression,
)
pp_StringExpression_strategy = st.builds(
    pp_StringExpression,
)
pp_Definition_strategy = st.builds(
    pp_Definition,
    className=
        safe_text
)
pp_LiteralExpression_strategy = st.builds(
    pp_LiteralExpression,
)
Definition_strategy = st.builds(
    Definition,
)
pp_HostClassDefinition_strategy = st.builds(
    pp_HostClassDefinition,
)
ICollectQuery_strategy = st.builds(
    ICollectQuery,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
pp_ExportedCollectQuery_strategy = st.builds(
    pp_ExportedCollectQuery,
)
pp_UnaryMinusExpression_strategy = st.builds(
    pp_UnaryMinusExpression,
)
pp_UnaryNotExpression_strategy = st.builds(
    pp_UnaryNotExpression,
)
pp_VirtualCollectQuery_strategy = st.builds(
    pp_VirtualCollectQuery,
)
pp_ICollectQuery_strategy = st.builds(
    pp_ICollectQuery,
)
pp_AttributeOperation_strategy = st.builds(
    pp_AttributeOperation,
    op=
        safe_text,
    key=
        safe_text
)
pp_AttributeOperations_strategy = st.builds(
    pp_AttributeOperations,
)
pp_ResourceBody_strategy = st.builds(
    pp_ResourceBody,
)
pp_Expression_strategy = st.builds(
    pp_Expression,
)
ExpressionBlock_strategy = st.builds(
    ExpressionBlock,
)
pp_Lambda_strategy = st.builds(
    pp_Lambda,
)
pp_ElseExpression_strategy = st.builds(
    pp_ElseExpression,
)
pp_PuppetManifest_strategy = st.builds(
    pp_PuppetManifest,
)
pp_DefinitionArgument_strategy = st.builds(
    pp_DefinitionArgument,
    argName=
        safe_text,
    op=
        safe_text
)
pp_DefinitionArgumentList_strategy = st.builds(
    pp_DefinitionArgumentList,
)

@given(instance=Lambda_strategy)
@settings(max_examples=50)
def test_lambda_instantiation(instance):
    assert isinstance(instance, Lambda)

@given(instance=pp_RubyLambda_strategy)
@settings(max_examples=50)
def test_pp_rubylambda_instantiation(instance):
    assert isinstance(instance, pp_RubyLambda)

@given(instance=pp_JavaLambda_strategy)
@settings(max_examples=50)
def test_pp_javalambda_instantiation(instance):
    assert isinstance(instance, pp_JavaLambda)



@given(instance=pp_JavaLambda_strategy)
def test_pp_javalambda_farrow_setter(instance):
    original = instance.farrow
    instance.farrow = original
    assert instance.farrow == original

@given(instance=TextExpression_strategy)
@settings(max_examples=50)
def test_textexpression_instantiation(instance):
    assert isinstance(instance, TextExpression)

@given(instance=pp_VariableTE_strategy)
@settings(max_examples=50)
def test_pp_variablete_instantiation(instance):
    assert isinstance(instance, pp_VariableTE)



@given(instance=pp_VariableTE_strategy)
def test_pp_variablete_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=pp_ExpressionTE_strategy)
@settings(max_examples=50)
def test_pp_expressionte_instantiation(instance):
    assert isinstance(instance, pp_ExpressionTE)

@given(instance=pp_VerbatimTE_strategy)
@settings(max_examples=50)
def test_pp_verbatimte_instantiation(instance):
    assert isinstance(instance, pp_VerbatimTE)



@given(instance=pp_VerbatimTE_strategy)
def test_pp_verbatimte_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=pp_TextExpression_strategy)
@settings(max_examples=50)
def test_pp_textexpression_instantiation(instance):
    assert isinstance(instance, pp_TextExpression)

@given(instance=IQuotedString_strategy)
@settings(max_examples=50)
def test_iquotedstring_instantiation(instance):
    assert isinstance(instance, IQuotedString)

@given(instance=StringExpression_strategy)
@settings(max_examples=50)
def test_stringexpression_instantiation(instance):
    assert isinstance(instance, StringExpression)

@given(instance=pp_UnquotedString_strategy)
@settings(max_examples=50)
def test_pp_unquotedstring_instantiation(instance):
    assert isinstance(instance, pp_UnquotedString)

@given(instance=pp_SingleQuotedString_strategy)
@settings(max_examples=50)
def test_pp_singlequotedstring_instantiation(instance):
    assert isinstance(instance, pp_SingleQuotedString)



@given(instance=pp_SingleQuotedString_strategy)
def test_pp_singlequotedstring_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=pp_DoubleQuotedString_strategy)
@settings(max_examples=50)
def test_pp_doublequotedstring_instantiation(instance):
    assert isinstance(instance, pp_DoubleQuotedString)

@given(instance=IfExpression_strategy)
@settings(max_examples=50)
def test_ifexpression_instantiation(instance):
    assert isinstance(instance, IfExpression)

@given(instance=pp_ElseIfExpression_strategy)
@settings(max_examples=50)
def test_pp_elseifexpression_instantiation(instance):
    assert isinstance(instance, pp_ElseIfExpression)

@given(instance=ParameterizedExpression_strategy)
@settings(max_examples=50)
def test_parameterizedexpression_instantiation(instance):
    assert isinstance(instance, ParameterizedExpression)

@given(instance=pp_WithLambdaExpression_strategy)
@settings(max_examples=50)
def test_pp_withlambdaexpression_instantiation(instance):
    assert isinstance(instance, pp_WithLambdaExpression)

@given(instance=pp_AtExpression_strategy)
@settings(max_examples=50)
def test_pp_atexpression_instantiation(instance):
    assert isinstance(instance, pp_AtExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=pp_AndExpression_strategy)
@settings(max_examples=50)
def test_pp_andexpression_instantiation(instance):
    assert isinstance(instance, pp_AndExpression)

@given(instance=pp_NamedAccessExpression_strategy)
@settings(max_examples=50)
def test_pp_namedaccessexpression_instantiation(instance):
    assert isinstance(instance, pp_NamedAccessExpression)

@given(instance=pp_AppendExpression_strategy)
@settings(max_examples=50)
def test_pp_appendexpression_instantiation(instance):
    assert isinstance(instance, pp_AppendExpression)

@given(instance=pp_OrExpression_strategy)
@settings(max_examples=50)
def test_pp_orexpression_instantiation(instance):
    assert isinstance(instance, pp_OrExpression)

@given(instance=pp_AssignmentExpression_strategy)
@settings(max_examples=50)
def test_pp_assignmentexpression_instantiation(instance):
    assert isinstance(instance, pp_AssignmentExpression)

@given(instance=BinaryOpExpression_strategy)
@settings(max_examples=50)
def test_binaryopexpression_instantiation(instance):
    assert isinstance(instance, BinaryOpExpression)

@given(instance=pp_RelationalExpression_strategy)
@settings(max_examples=50)
def test_pp_relationalexpression_instantiation(instance):
    assert isinstance(instance, pp_RelationalExpression)

@given(instance=pp_EqualityExpression_strategy)
@settings(max_examples=50)
def test_pp_equalityexpression_instantiation(instance):
    assert isinstance(instance, pp_EqualityExpression)

@given(instance=pp_ShiftExpression_strategy)
@settings(max_examples=50)
def test_pp_shiftexpression_instantiation(instance):
    assert isinstance(instance, pp_ShiftExpression)

@given(instance=pp_AdditiveExpression_strategy)
@settings(max_examples=50)
def test_pp_additiveexpression_instantiation(instance):
    assert isinstance(instance, pp_AdditiveExpression)

@given(instance=pp_MatchingExpression_strategy)
@settings(max_examples=50)
def test_pp_matchingexpression_instantiation(instance):
    assert isinstance(instance, pp_MatchingExpression)

@given(instance=pp_InExpression_strategy)
@settings(max_examples=50)
def test_pp_inexpression_instantiation(instance):
    assert isinstance(instance, pp_InExpression)

@given(instance=pp_MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_pp_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, pp_MultiplicativeExpression)

@given(instance=pp_RelationshipExpression_strategy)
@settings(max_examples=50)
def test_pp_relationshipexpression_instantiation(instance):
    assert isinstance(instance, pp_RelationshipExpression)

@given(instance=pp_BinaryOpExpression_strategy)
@settings(max_examples=50)
def test_pp_binaryopexpression_instantiation(instance):
    assert isinstance(instance, pp_BinaryOpExpression)



@given(instance=pp_BinaryOpExpression_strategy)
def test_pp_binaryopexpression_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=WithLambdaExpression_strategy)
@settings(max_examples=50)
def test_withlambdaexpression_instantiation(instance):
    assert isinstance(instance, WithLambdaExpression)

@given(instance=pp_MethodCall_strategy)
@settings(max_examples=50)
def test_pp_methodcall_instantiation(instance):
    assert isinstance(instance, pp_MethodCall)



@given(instance=pp_MethodCall_strategy)
def test_pp_methodcall_parenthesized_setter(instance):
    original = instance.parenthesized
    instance.parenthesized = original
    assert instance.parenthesized == original

@given(instance=pp_FunctionCall_strategy)
@settings(max_examples=50)
def test_pp_functioncall_instantiation(instance):
    assert isinstance(instance, pp_FunctionCall)

@given(instance=pp_SelectorEntry_strategy)
@settings(max_examples=50)
def test_pp_selectorentry_instantiation(instance):
    assert isinstance(instance, pp_SelectorEntry)

@given(instance=pp_SelectorExpression_strategy)
@settings(max_examples=50)
def test_pp_selectorexpression_instantiation(instance):
    assert isinstance(instance, pp_SelectorExpression)

@given(instance=LiteralExpression_strategy)
@settings(max_examples=50)
def test_literalexpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)

@given(instance=pp_LiteralName_strategy)
@settings(max_examples=50)
def test_pp_literalname_instantiation(instance):
    assert isinstance(instance, pp_LiteralName)



@given(instance=pp_LiteralName_strategy)
def test_pp_literalname_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp_LiteralBoolean_strategy)
@settings(max_examples=50)
def test_pp_literalboolean_instantiation(instance):
    assert isinstance(instance, pp_LiteralBoolean)



@given(instance=pp_LiteralBoolean_strategy)
def test_pp_literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp_LiteralRegex_strategy)
@settings(max_examples=50)
def test_pp_literalregex_instantiation(instance):
    assert isinstance(instance, pp_LiteralRegex)



@given(instance=pp_LiteralRegex_strategy)
def test_pp_literalregex_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp_VirtualNameOrReference_strategy)
@settings(max_examples=50)
def test_pp_virtualnameorreference_instantiation(instance):
    assert isinstance(instance, pp_VirtualNameOrReference)



@given(instance=pp_VirtualNameOrReference_strategy)
def test_pp_virtualnameorreference_exported_setter(instance):
    original = instance.exported
    instance.exported = original
    assert instance.exported == original



@given(instance=pp_VirtualNameOrReference_strategy)
def test_pp_virtualnameorreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp_LiteralUndef_strategy)
@settings(max_examples=50)
def test_pp_literalundef_instantiation(instance):
    assert isinstance(instance, pp_LiteralUndef)

@given(instance=pp_LiteralClass_strategy)
@settings(max_examples=50)
def test_pp_literalclass_instantiation(instance):
    assert isinstance(instance, pp_LiteralClass)

@given(instance=pp_LiteralDefault_strategy)
@settings(max_examples=50)
def test_pp_literaldefault_instantiation(instance):
    assert isinstance(instance, pp_LiteralDefault)

@given(instance=pp_LiteralNameOrReference_strategy)
@settings(max_examples=50)
def test_pp_literalnameorreference_instantiation(instance):
    assert isinstance(instance, pp_LiteralNameOrReference)



@given(instance=pp_LiteralNameOrReference_strategy)
def test_pp_literalnameorreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp_Case_strategy)
@settings(max_examples=50)
def test_pp_case_instantiation(instance):
    assert isinstance(instance, pp_Case)

@given(instance=pp_HashEntry_strategy)
@settings(max_examples=50)
def test_pp_hashentry_instantiation(instance):
    assert isinstance(instance, pp_HashEntry)

@given(instance=pp_LiteralHash_strategy)
@settings(max_examples=50)
def test_pp_literalhash_instantiation(instance):
    assert isinstance(instance, pp_LiteralHash)

@given(instance=pp_LiteralList_strategy)
@settings(max_examples=50)
def test_pp_literallist_instantiation(instance):
    assert isinstance(instance, pp_LiteralList)

@given(instance=pp_IQuotedString_strategy)
@settings(max_examples=50)
def test_pp_iquotedstring_instantiation(instance):
    assert isinstance(instance, pp_IQuotedString)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=pp_CaseExpression_strategy)
@settings(max_examples=50)
def test_pp_caseexpression_instantiation(instance):
    assert isinstance(instance, pp_CaseExpression)

@given(instance=pp_BinaryExpression_strategy)
@settings(max_examples=50)
def test_pp_binaryexpression_instantiation(instance):
    assert isinstance(instance, pp_BinaryExpression)

@given(instance=pp_UnlessExpression_strategy)
@settings(max_examples=50)
def test_pp_unlessexpression_instantiation(instance):
    assert isinstance(instance, pp_UnlessExpression)

@given(instance=pp_ExpressionBlock_strategy)
@settings(max_examples=50)
def test_pp_expressionblock_instantiation(instance):
    assert isinstance(instance, pp_ExpressionBlock)

@given(instance=pp_SeparatorExpression_strategy)
@settings(max_examples=50)
def test_pp_separatorexpression_instantiation(instance):
    assert isinstance(instance, pp_SeparatorExpression)

@given(instance=pp_NodeDefinition_strategy)
@settings(max_examples=50)
def test_pp_nodedefinition_instantiation(instance):
    assert isinstance(instance, pp_NodeDefinition)

@given(instance=pp_IfExpression_strategy)
@settings(max_examples=50)
def test_pp_ifexpression_instantiation(instance):
    assert isinstance(instance, pp_IfExpression)

@given(instance=pp_ExprList_strategy)
@settings(max_examples=50)
def test_pp_exprlist_instantiation(instance):
    assert isinstance(instance, pp_ExprList)

@given(instance=pp_ParenthesisedExpression_strategy)
@settings(max_examples=50)
def test_pp_parenthesisedexpression_instantiation(instance):
    assert isinstance(instance, pp_ParenthesisedExpression)

@given(instance=pp_ImportExpression_strategy)
@settings(max_examples=50)
def test_pp_importexpression_instantiation(instance):
    assert isinstance(instance, pp_ImportExpression)

@given(instance=pp_VariableExpression_strategy)
@settings(max_examples=50)
def test_pp_variableexpression_instantiation(instance):
    assert isinstance(instance, pp_VariableExpression)



@given(instance=pp_VariableExpression_strategy)
def test_pp_variableexpression_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=pp_ResourceExpression_strategy)
@settings(max_examples=50)
def test_pp_resourceexpression_instantiation(instance):
    assert isinstance(instance, pp_ResourceExpression)

@given(instance=pp_UnaryExpression_strategy)
@settings(max_examples=50)
def test_pp_unaryexpression_instantiation(instance):
    assert isinstance(instance, pp_UnaryExpression)

@given(instance=pp_InterpolatedVariable_strategy)
@settings(max_examples=50)
def test_pp_interpolatedvariable_instantiation(instance):
    assert isinstance(instance, pp_InterpolatedVariable)



@given(instance=pp_InterpolatedVariable_strategy)
def test_pp_interpolatedvariable_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=pp_CollectExpression_strategy)
@settings(max_examples=50)
def test_pp_collectexpression_instantiation(instance):
    assert isinstance(instance, pp_CollectExpression)

@given(instance=pp_ParameterizedExpression_strategy)
@settings(max_examples=50)
def test_pp_parameterizedexpression_instantiation(instance):
    assert isinstance(instance, pp_ParameterizedExpression)

@given(instance=pp_StringExpression_strategy)
@settings(max_examples=50)
def test_pp_stringexpression_instantiation(instance):
    assert isinstance(instance, pp_StringExpression)

@given(instance=pp_Definition_strategy)
@settings(max_examples=50)
def test_pp_definition_instantiation(instance):
    assert isinstance(instance, pp_Definition)



@given(instance=pp_Definition_strategy)
def test_pp_definition_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=pp_LiteralExpression_strategy)
@settings(max_examples=50)
def test_pp_literalexpression_instantiation(instance):
    assert isinstance(instance, pp_LiteralExpression)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=pp_HostClassDefinition_strategy)
@settings(max_examples=50)
def test_pp_hostclassdefinition_instantiation(instance):
    assert isinstance(instance, pp_HostClassDefinition)

@given(instance=ICollectQuery_strategy)
@settings(max_examples=50)
def test_icollectquery_instantiation(instance):
    assert isinstance(instance, ICollectQuery)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=pp_ExportedCollectQuery_strategy)
@settings(max_examples=50)
def test_pp_exportedcollectquery_instantiation(instance):
    assert isinstance(instance, pp_ExportedCollectQuery)

@given(instance=pp_UnaryMinusExpression_strategy)
@settings(max_examples=50)
def test_pp_unaryminusexpression_instantiation(instance):
    assert isinstance(instance, pp_UnaryMinusExpression)

@given(instance=pp_UnaryNotExpression_strategy)
@settings(max_examples=50)
def test_pp_unarynotexpression_instantiation(instance):
    assert isinstance(instance, pp_UnaryNotExpression)

@given(instance=pp_VirtualCollectQuery_strategy)
@settings(max_examples=50)
def test_pp_virtualcollectquery_instantiation(instance):
    assert isinstance(instance, pp_VirtualCollectQuery)

@given(instance=pp_ICollectQuery_strategy)
@settings(max_examples=50)
def test_pp_icollectquery_instantiation(instance):
    assert isinstance(instance, pp_ICollectQuery)

@given(instance=pp_AttributeOperation_strategy)
@settings(max_examples=50)
def test_pp_attributeoperation_instantiation(instance):
    assert isinstance(instance, pp_AttributeOperation)



@given(instance=pp_AttributeOperation_strategy)
def test_pp_attributeoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=pp_AttributeOperation_strategy)
def test_pp_attributeoperation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=pp_AttributeOperations_strategy)
@settings(max_examples=50)
def test_pp_attributeoperations_instantiation(instance):
    assert isinstance(instance, pp_AttributeOperations)

@given(instance=pp_ResourceBody_strategy)
@settings(max_examples=50)
def test_pp_resourcebody_instantiation(instance):
    assert isinstance(instance, pp_ResourceBody)

@given(instance=pp_Expression_strategy)
@settings(max_examples=50)
def test_pp_expression_instantiation(instance):
    assert isinstance(instance, pp_Expression)

@given(instance=ExpressionBlock_strategy)
@settings(max_examples=50)
def test_expressionblock_instantiation(instance):
    assert isinstance(instance, ExpressionBlock)

@given(instance=pp_Lambda_strategy)
@settings(max_examples=50)
def test_pp_lambda_instantiation(instance):
    assert isinstance(instance, pp_Lambda)

@given(instance=pp_ElseExpression_strategy)
@settings(max_examples=50)
def test_pp_elseexpression_instantiation(instance):
    assert isinstance(instance, pp_ElseExpression)

@given(instance=pp_PuppetManifest_strategy)
@settings(max_examples=50)
def test_pp_puppetmanifest_instantiation(instance):
    assert isinstance(instance, pp_PuppetManifest)

@given(instance=pp_DefinitionArgument_strategy)
@settings(max_examples=50)
def test_pp_definitionargument_instantiation(instance):
    assert isinstance(instance, pp_DefinitionArgument)



@given(instance=pp_DefinitionArgument_strategy)
def test_pp_definitionargument_argName_setter(instance):
    original = instance.argName
    instance.argName = original
    assert instance.argName == original



@given(instance=pp_DefinitionArgument_strategy)
def test_pp_definitionargument_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=pp_DefinitionArgumentList_strategy)
@settings(max_examples=50)
def test_pp_definitionargumentlist_instantiation(instance):
    assert isinstance(instance, pp_DefinitionArgumentList)
