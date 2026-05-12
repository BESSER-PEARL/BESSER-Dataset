import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TextExpression,
    pp1_VariableTE,
    pp1_ExpressionTE,
    pp1_VerbatimTE,
    Lambda,
    pp1_RubyLambda,
    pp1_JavaLambda,
    pp1_TextExpression,
    IQuotedString,
    StringExpression,
    pp1_SingleQuotedString,
    pp1_UnquotedString,
    pp1_DoubleQuotedString,
    IfExpression,
    pp1_ElseIfExpression,
    WithLambdaExpression,
    pp1_MethodCall,
    pp1_FunctionCall,
    ParameterizedExpression,
    pp1_WithLambdaExpression,
    pp1_SelectorExpression,
    pp1_AtExpression,
    BinaryExpression,
    pp1_OrExpression,
    pp1_NamedAccessExpression,
    pp1_AppendExpression,
    pp1_BinaryOpExpression,
    pp1_SelectorEntry,
    pp1_AndExpression,
    pp1_AssignmentExpression,
    pp1_Case,
    BinaryOpExpression,
    pp1_ShiftExpression,
    pp1_AdditiveExpression,
    pp1_RelationalExpression,
    pp1_EqualityExpression,
    pp1_InExpression,
    pp1_MatchingExpression,
    pp1_MultiplicativeExpression,
    pp1_RelationshipExpression,
    pp1_HashEntry,
    pp1_IQuotedString,
    LiteralExpression,
    pp1_LiteralList,
    pp1_LiteralBoolean,
    pp1_LiteralDefault,
    pp1_LiteralName,
    pp1_LiteralUndef,
    pp1_LiteralClass,
    pp1_VirtualNameOrReference,
    pp1_LiteralHash,
    pp1_LiteralRegex,
    pp1_LiteralNameOrReference,
    pp1_DefinitionArgument,
    pp1_DefinitionArgumentList,
    Expression,
    pp1_InterpolatedVariable,
    pp1_SeparatorExpression,
    pp1_NodeDefinition,
    pp1_ExpressionBlock,
    pp1_ExprList,
    pp1_ParameterizedExpression,
    pp1_VariableExpression,
    pp1_UnaryExpression,
    pp1_ResourceExpression,
    pp1_StringExpression,
    pp1_IfExpression,
    pp1_ImportExpression,
    pp1_CaseExpression,
    pp1_CollectExpression,
    pp1_ParenthesisedExpression,
    pp1_BinaryExpression,
    pp1_UnlessExpression,
    pp1_Definition,
    pp1_LiteralExpression,
    Definition,
    pp1_HostClassDefinition,
    ICollectQuery,
    UnaryExpression,
    pp1_UnaryMinusExpression,
    pp1_ExportedCollectQuery,
    pp1_UnaryNotExpression,
    pp1_VirtualCollectQuery,
    pp1_ICollectQuery,
    pp1_AttributeOperation,
    pp1_AttributeOperations,
    pp1_ResourceBody,
    pp1_Expression,
    ExpressionBlock,
    pp1_ElseExpression,
    pp1_Lambda,
    pp1_PuppetManifest,
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



def test_pp1_variablete_is_not_abstract():
    assert not inspect.isabstract(pp1_VariableTE)


def test_pp1_variablete_constructor_exists():
    assert callable(pp1_VariableTE.__init__)


def test_pp1_variablete_constructor_args():
    sig = inspect.signature(pp1_VariableTE.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_pp1_variablete_has_varName():
    assert hasattr(pp1_VariableTE, "varName")
    descriptor = None
    for klass in pp1_VariableTE.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_pp1_expressionte_is_not_abstract():
    assert not inspect.isabstract(pp1_ExpressionTE)


def test_pp1_expressionte_constructor_exists():
    assert callable(pp1_ExpressionTE.__init__)


def test_pp1_expressionte_constructor_args():
    sig = inspect.signature(pp1_ExpressionTE.__init__)
    params = list(sig.parameters.keys())



def test_pp1_verbatimte_is_not_abstract():
    assert not inspect.isabstract(pp1_VerbatimTE)


def test_pp1_verbatimte_constructor_exists():
    assert callable(pp1_VerbatimTE.__init__)


def test_pp1_verbatimte_constructor_args():
    sig = inspect.signature(pp1_VerbatimTE.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_pp1_verbatimte_has_text():
    assert hasattr(pp1_VerbatimTE, "text")
    descriptor = None
    for klass in pp1_VerbatimTE.__mro__:
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



def test_pp1_rubylambda_is_not_abstract():
    assert not inspect.isabstract(pp1_RubyLambda)


def test_pp1_rubylambda_constructor_exists():
    assert callable(pp1_RubyLambda.__init__)


def test_pp1_rubylambda_constructor_args():
    sig = inspect.signature(pp1_RubyLambda.__init__)
    params = list(sig.parameters.keys())



def test_pp1_javalambda_is_not_abstract():
    assert not inspect.isabstract(pp1_JavaLambda)


def test_pp1_javalambda_constructor_exists():
    assert callable(pp1_JavaLambda.__init__)


def test_pp1_javalambda_constructor_args():
    sig = inspect.signature(pp1_JavaLambda.__init__)
    params = list(sig.parameters.keys())
    assert "farrow" in params, "Missing parameter 'farrow'"

def test_pp1_javalambda_has_farrow():
    assert hasattr(pp1_JavaLambda, "farrow")
    descriptor = None
    for klass in pp1_JavaLambda.__mro__:
        if "farrow" in klass.__dict__:
            descriptor = klass.__dict__["farrow"]
            break
    assert isinstance(descriptor, property)



def test_pp1_textexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_TextExpression)


def test_pp1_textexpression_constructor_exists():
    assert callable(pp1_TextExpression.__init__)


def test_pp1_textexpression_constructor_args():
    sig = inspect.signature(pp1_TextExpression.__init__)
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



def test_pp1_singlequotedstring_is_not_abstract():
    assert not inspect.isabstract(pp1_SingleQuotedString)


def test_pp1_singlequotedstring_constructor_exists():
    assert callable(pp1_SingleQuotedString.__init__)


def test_pp1_singlequotedstring_constructor_args():
    sig = inspect.signature(pp1_SingleQuotedString.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_pp1_singlequotedstring_has_text():
    assert hasattr(pp1_SingleQuotedString, "text")
    descriptor = None
    for klass in pp1_SingleQuotedString.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_pp1_unquotedstring_is_not_abstract():
    assert not inspect.isabstract(pp1_UnquotedString)


def test_pp1_unquotedstring_constructor_exists():
    assert callable(pp1_UnquotedString.__init__)


def test_pp1_unquotedstring_constructor_args():
    sig = inspect.signature(pp1_UnquotedString.__init__)
    params = list(sig.parameters.keys())



def test_pp1_doublequotedstring_is_not_abstract():
    assert not inspect.isabstract(pp1_DoubleQuotedString)


def test_pp1_doublequotedstring_constructor_exists():
    assert callable(pp1_DoubleQuotedString.__init__)


def test_pp1_doublequotedstring_constructor_args():
    sig = inspect.signature(pp1_DoubleQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_ifexpression_is_not_abstract():
    assert not inspect.isabstract(IfExpression)


def test_ifexpression_constructor_exists():
    assert callable(IfExpression.__init__)


def test_ifexpression_constructor_args():
    sig = inspect.signature(IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_elseifexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_ElseIfExpression)


def test_pp1_elseifexpression_constructor_exists():
    assert callable(pp1_ElseIfExpression.__init__)


def test_pp1_elseifexpression_constructor_args():
    sig = inspect.signature(pp1_ElseIfExpression.__init__)
    params = list(sig.parameters.keys())



def test_withlambdaexpression_is_not_abstract():
    assert not inspect.isabstract(WithLambdaExpression)


def test_withlambdaexpression_constructor_exists():
    assert callable(WithLambdaExpression.__init__)


def test_withlambdaexpression_constructor_args():
    sig = inspect.signature(WithLambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_methodcall_is_not_abstract():
    assert not inspect.isabstract(pp1_MethodCall)


def test_pp1_methodcall_constructor_exists():
    assert callable(pp1_MethodCall.__init__)


def test_pp1_methodcall_constructor_args():
    sig = inspect.signature(pp1_MethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "parenthesized" in params, "Missing parameter 'parenthesized'"

def test_pp1_methodcall_has_parenthesized():
    assert hasattr(pp1_MethodCall, "parenthesized")
    descriptor = None
    for klass in pp1_MethodCall.__mro__:
        if "parenthesized" in klass.__dict__:
            descriptor = klass.__dict__["parenthesized"]
            break
    assert isinstance(descriptor, property)



def test_pp1_functioncall_is_not_abstract():
    assert not inspect.isabstract(pp1_FunctionCall)


def test_pp1_functioncall_constructor_exists():
    assert callable(pp1_FunctionCall.__init__)


def test_pp1_functioncall_constructor_args():
    sig = inspect.signature(pp1_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_parameterizedexpression_is_not_abstract():
    assert not inspect.isabstract(ParameterizedExpression)


def test_parameterizedexpression_constructor_exists():
    assert callable(ParameterizedExpression.__init__)


def test_parameterizedexpression_constructor_args():
    sig = inspect.signature(ParameterizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_withlambdaexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_WithLambdaExpression)


def test_pp1_withlambdaexpression_constructor_exists():
    assert callable(pp1_WithLambdaExpression.__init__)


def test_pp1_withlambdaexpression_constructor_args():
    sig = inspect.signature(pp1_WithLambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_selectorexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_SelectorExpression)


def test_pp1_selectorexpression_constructor_exists():
    assert callable(pp1_SelectorExpression.__init__)


def test_pp1_selectorexpression_constructor_args():
    sig = inspect.signature(pp1_SelectorExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_atexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_AtExpression)


def test_pp1_atexpression_constructor_exists():
    assert callable(pp1_AtExpression.__init__)


def test_pp1_atexpression_constructor_args():
    sig = inspect.signature(pp1_AtExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_orexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_OrExpression)


def test_pp1_orexpression_constructor_exists():
    assert callable(pp1_OrExpression.__init__)


def test_pp1_orexpression_constructor_args():
    sig = inspect.signature(pp1_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_namedaccessexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_NamedAccessExpression)


def test_pp1_namedaccessexpression_constructor_exists():
    assert callable(pp1_NamedAccessExpression.__init__)


def test_pp1_namedaccessexpression_constructor_args():
    sig = inspect.signature(pp1_NamedAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_appendexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_AppendExpression)


def test_pp1_appendexpression_constructor_exists():
    assert callable(pp1_AppendExpression.__init__)


def test_pp1_appendexpression_constructor_args():
    sig = inspect.signature(pp1_AppendExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_BinaryOpExpression)


def test_pp1_binaryopexpression_constructor_exists():
    assert callable(pp1_BinaryOpExpression.__init__)


def test_pp1_binaryopexpression_constructor_args():
    sig = inspect.signature(pp1_BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_pp1_binaryopexpression_has_opName():
    assert hasattr(pp1_BinaryOpExpression, "opName")
    descriptor = None
    for klass in pp1_BinaryOpExpression.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_pp1_selectorentry_is_not_abstract():
    assert not inspect.isabstract(pp1_SelectorEntry)


def test_pp1_selectorentry_constructor_exists():
    assert callable(pp1_SelectorEntry.__init__)


def test_pp1_selectorentry_constructor_args():
    sig = inspect.signature(pp1_SelectorEntry.__init__)
    params = list(sig.parameters.keys())



def test_pp1_andexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_AndExpression)


def test_pp1_andexpression_constructor_exists():
    assert callable(pp1_AndExpression.__init__)


def test_pp1_andexpression_constructor_args():
    sig = inspect.signature(pp1_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_AssignmentExpression)


def test_pp1_assignmentexpression_constructor_exists():
    assert callable(pp1_AssignmentExpression.__init__)


def test_pp1_assignmentexpression_constructor_args():
    sig = inspect.signature(pp1_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_case_is_not_abstract():
    assert not inspect.isabstract(pp1_Case)


def test_pp1_case_constructor_exists():
    assert callable(pp1_Case.__init__)


def test_pp1_case_constructor_args():
    sig = inspect.signature(pp1_Case.__init__)
    params = list(sig.parameters.keys())



def test_binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOpExpression)


def test_binaryopexpression_constructor_exists():
    assert callable(BinaryOpExpression.__init__)


def test_binaryopexpression_constructor_args():
    sig = inspect.signature(BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_ShiftExpression)


def test_pp1_shiftexpression_constructor_exists():
    assert callable(pp1_ShiftExpression.__init__)


def test_pp1_shiftexpression_constructor_args():
    sig = inspect.signature(pp1_ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_AdditiveExpression)


def test_pp1_additiveexpression_constructor_exists():
    assert callable(pp1_AdditiveExpression.__init__)


def test_pp1_additiveexpression_constructor_args():
    sig = inspect.signature(pp1_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_RelationalExpression)


def test_pp1_relationalexpression_constructor_exists():
    assert callable(pp1_RelationalExpression.__init__)


def test_pp1_relationalexpression_constructor_args():
    sig = inspect.signature(pp1_RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_EqualityExpression)


def test_pp1_equalityexpression_constructor_exists():
    assert callable(pp1_EqualityExpression.__init__)


def test_pp1_equalityexpression_constructor_args():
    sig = inspect.signature(pp1_EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_inexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_InExpression)


def test_pp1_inexpression_constructor_exists():
    assert callable(pp1_InExpression.__init__)


def test_pp1_inexpression_constructor_args():
    sig = inspect.signature(pp1_InExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_matchingexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_MatchingExpression)


def test_pp1_matchingexpression_constructor_exists():
    assert callable(pp1_MatchingExpression.__init__)


def test_pp1_matchingexpression_constructor_args():
    sig = inspect.signature(pp1_MatchingExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_MultiplicativeExpression)


def test_pp1_multiplicativeexpression_constructor_exists():
    assert callable(pp1_MultiplicativeExpression.__init__)


def test_pp1_multiplicativeexpression_constructor_args():
    sig = inspect.signature(pp1_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_relationshipexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_RelationshipExpression)


def test_pp1_relationshipexpression_constructor_exists():
    assert callable(pp1_RelationshipExpression.__init__)


def test_pp1_relationshipexpression_constructor_args():
    sig = inspect.signature(pp1_RelationshipExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_hashentry_is_not_abstract():
    assert not inspect.isabstract(pp1_HashEntry)


def test_pp1_hashentry_constructor_exists():
    assert callable(pp1_HashEntry.__init__)


def test_pp1_hashentry_constructor_args():
    sig = inspect.signature(pp1_HashEntry.__init__)
    params = list(sig.parameters.keys())



def test_pp1_iquotedstring_is_not_abstract():
    assert not inspect.isabstract(pp1_IQuotedString)


def test_pp1_iquotedstring_constructor_exists():
    assert callable(pp1_IQuotedString.__init__)


def test_pp1_iquotedstring_constructor_args():
    sig = inspect.signature(pp1_IQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_literallist_is_not_abstract():
    assert not inspect.isabstract(pp1_LiteralList)


def test_pp1_literallist_constructor_exists():
    assert callable(pp1_LiteralList.__init__)


def test_pp1_literallist_constructor_args():
    sig = inspect.signature(pp1_LiteralList.__init__)
    params = list(sig.parameters.keys())



def test_pp1_literalboolean_is_not_abstract():
    assert not inspect.isabstract(pp1_LiteralBoolean)


def test_pp1_literalboolean_constructor_exists():
    assert callable(pp1_LiteralBoolean.__init__)


def test_pp1_literalboolean_constructor_args():
    sig = inspect.signature(pp1_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp1_literalboolean_has_value():
    assert hasattr(pp1_LiteralBoolean, "value")
    descriptor = None
    for klass in pp1_LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp1_literaldefault_is_not_abstract():
    assert not inspect.isabstract(pp1_LiteralDefault)


def test_pp1_literaldefault_constructor_exists():
    assert callable(pp1_LiteralDefault.__init__)


def test_pp1_literaldefault_constructor_args():
    sig = inspect.signature(pp1_LiteralDefault.__init__)
    params = list(sig.parameters.keys())



def test_pp1_literalname_is_not_abstract():
    assert not inspect.isabstract(pp1_LiteralName)


def test_pp1_literalname_constructor_exists():
    assert callable(pp1_LiteralName.__init__)


def test_pp1_literalname_constructor_args():
    sig = inspect.signature(pp1_LiteralName.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp1_literalname_has_value():
    assert hasattr(pp1_LiteralName, "value")
    descriptor = None
    for klass in pp1_LiteralName.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp1_literalundef_is_not_abstract():
    assert not inspect.isabstract(pp1_LiteralUndef)


def test_pp1_literalundef_constructor_exists():
    assert callable(pp1_LiteralUndef.__init__)


def test_pp1_literalundef_constructor_args():
    sig = inspect.signature(pp1_LiteralUndef.__init__)
    params = list(sig.parameters.keys())



def test_pp1_literalclass_is_not_abstract():
    assert not inspect.isabstract(pp1_LiteralClass)


def test_pp1_literalclass_constructor_exists():
    assert callable(pp1_LiteralClass.__init__)


def test_pp1_literalclass_constructor_args():
    sig = inspect.signature(pp1_LiteralClass.__init__)
    params = list(sig.parameters.keys())



def test_pp1_virtualnameorreference_is_not_abstract():
    assert not inspect.isabstract(pp1_VirtualNameOrReference)


def test_pp1_virtualnameorreference_constructor_exists():
    assert callable(pp1_VirtualNameOrReference.__init__)


def test_pp1_virtualnameorreference_constructor_args():
    sig = inspect.signature(pp1_VirtualNameOrReference.__init__)
    params = list(sig.parameters.keys())
    assert "exported" in params, "Missing parameter 'exported'"
    assert "value" in params, "Missing parameter 'value'"

def test_pp1_virtualnameorreference_has_exported():
    assert hasattr(pp1_VirtualNameOrReference, "exported")
    descriptor = None
    for klass in pp1_VirtualNameOrReference.__mro__:
        if "exported" in klass.__dict__:
            descriptor = klass.__dict__["exported"]
            break
    assert isinstance(descriptor, property)

def test_pp1_virtualnameorreference_has_value():
    assert hasattr(pp1_VirtualNameOrReference, "value")
    descriptor = None
    for klass in pp1_VirtualNameOrReference.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp1_literalhash_is_not_abstract():
    assert not inspect.isabstract(pp1_LiteralHash)


def test_pp1_literalhash_constructor_exists():
    assert callable(pp1_LiteralHash.__init__)


def test_pp1_literalhash_constructor_args():
    sig = inspect.signature(pp1_LiteralHash.__init__)
    params = list(sig.parameters.keys())



def test_pp1_literalregex_is_not_abstract():
    assert not inspect.isabstract(pp1_LiteralRegex)


def test_pp1_literalregex_constructor_exists():
    assert callable(pp1_LiteralRegex.__init__)


def test_pp1_literalregex_constructor_args():
    sig = inspect.signature(pp1_LiteralRegex.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp1_literalregex_has_value():
    assert hasattr(pp1_LiteralRegex, "value")
    descriptor = None
    for klass in pp1_LiteralRegex.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp1_literalnameorreference_is_not_abstract():
    assert not inspect.isabstract(pp1_LiteralNameOrReference)


def test_pp1_literalnameorreference_constructor_exists():
    assert callable(pp1_LiteralNameOrReference.__init__)


def test_pp1_literalnameorreference_constructor_args():
    sig = inspect.signature(pp1_LiteralNameOrReference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pp1_literalnameorreference_has_value():
    assert hasattr(pp1_LiteralNameOrReference, "value")
    descriptor = None
    for klass in pp1_LiteralNameOrReference.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pp1_definitionargument_is_not_abstract():
    assert not inspect.isabstract(pp1_DefinitionArgument)


def test_pp1_definitionargument_constructor_exists():
    assert callable(pp1_DefinitionArgument.__init__)


def test_pp1_definitionargument_constructor_args():
    sig = inspect.signature(pp1_DefinitionArgument.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "argName" in params, "Missing parameter 'argName'"

def test_pp1_definitionargument_has_op():
    assert hasattr(pp1_DefinitionArgument, "op")
    descriptor = None
    for klass in pp1_DefinitionArgument.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_pp1_definitionargument_has_argName():
    assert hasattr(pp1_DefinitionArgument, "argName")
    descriptor = None
    for klass in pp1_DefinitionArgument.__mro__:
        if "argName" in klass.__dict__:
            descriptor = klass.__dict__["argName"]
            break
    assert isinstance(descriptor, property)



def test_pp1_definitionargumentlist_is_not_abstract():
    assert not inspect.isabstract(pp1_DefinitionArgumentList)


def test_pp1_definitionargumentlist_constructor_exists():
    assert callable(pp1_DefinitionArgumentList.__init__)


def test_pp1_definitionargumentlist_constructor_args():
    sig = inspect.signature(pp1_DefinitionArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_interpolatedvariable_is_not_abstract():
    assert not inspect.isabstract(pp1_InterpolatedVariable)


def test_pp1_interpolatedvariable_constructor_exists():
    assert callable(pp1_InterpolatedVariable.__init__)


def test_pp1_interpolatedvariable_constructor_args():
    sig = inspect.signature(pp1_InterpolatedVariable.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_pp1_interpolatedvariable_has_varName():
    assert hasattr(pp1_InterpolatedVariable, "varName")
    descriptor = None
    for klass in pp1_InterpolatedVariable.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_pp1_separatorexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_SeparatorExpression)


def test_pp1_separatorexpression_constructor_exists():
    assert callable(pp1_SeparatorExpression.__init__)


def test_pp1_separatorexpression_constructor_args():
    sig = inspect.signature(pp1_SeparatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_nodedefinition_is_not_abstract():
    assert not inspect.isabstract(pp1_NodeDefinition)


def test_pp1_nodedefinition_constructor_exists():
    assert callable(pp1_NodeDefinition.__init__)


def test_pp1_nodedefinition_constructor_args():
    sig = inspect.signature(pp1_NodeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_pp1_expressionblock_is_not_abstract():
    assert not inspect.isabstract(pp1_ExpressionBlock)


def test_pp1_expressionblock_constructor_exists():
    assert callable(pp1_ExpressionBlock.__init__)


def test_pp1_expressionblock_constructor_args():
    sig = inspect.signature(pp1_ExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_pp1_exprlist_is_not_abstract():
    assert not inspect.isabstract(pp1_ExprList)


def test_pp1_exprlist_constructor_exists():
    assert callable(pp1_ExprList.__init__)


def test_pp1_exprlist_constructor_args():
    sig = inspect.signature(pp1_ExprList.__init__)
    params = list(sig.parameters.keys())



def test_pp1_parameterizedexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_ParameterizedExpression)


def test_pp1_parameterizedexpression_constructor_exists():
    assert callable(pp1_ParameterizedExpression.__init__)


def test_pp1_parameterizedexpression_constructor_args():
    sig = inspect.signature(pp1_ParameterizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_variableexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_VariableExpression)


def test_pp1_variableexpression_constructor_exists():
    assert callable(pp1_VariableExpression.__init__)


def test_pp1_variableexpression_constructor_args():
    sig = inspect.signature(pp1_VariableExpression.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_pp1_variableexpression_has_varName():
    assert hasattr(pp1_VariableExpression, "varName")
    descriptor = None
    for klass in pp1_VariableExpression.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_pp1_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_UnaryExpression)


def test_pp1_unaryexpression_constructor_exists():
    assert callable(pp1_UnaryExpression.__init__)


def test_pp1_unaryexpression_constructor_args():
    sig = inspect.signature(pp1_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_resourceexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_ResourceExpression)


def test_pp1_resourceexpression_constructor_exists():
    assert callable(pp1_ResourceExpression.__init__)


def test_pp1_resourceexpression_constructor_args():
    sig = inspect.signature(pp1_ResourceExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_stringexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_StringExpression)


def test_pp1_stringexpression_constructor_exists():
    assert callable(pp1_StringExpression.__init__)


def test_pp1_stringexpression_constructor_args():
    sig = inspect.signature(pp1_StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_ifexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_IfExpression)


def test_pp1_ifexpression_constructor_exists():
    assert callable(pp1_IfExpression.__init__)


def test_pp1_ifexpression_constructor_args():
    sig = inspect.signature(pp1_IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_importexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_ImportExpression)


def test_pp1_importexpression_constructor_exists():
    assert callable(pp1_ImportExpression.__init__)


def test_pp1_importexpression_constructor_args():
    sig = inspect.signature(pp1_ImportExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_caseexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_CaseExpression)


def test_pp1_caseexpression_constructor_exists():
    assert callable(pp1_CaseExpression.__init__)


def test_pp1_caseexpression_constructor_args():
    sig = inspect.signature(pp1_CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_collectexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_CollectExpression)


def test_pp1_collectexpression_constructor_exists():
    assert callable(pp1_CollectExpression.__init__)


def test_pp1_collectexpression_constructor_args():
    sig = inspect.signature(pp1_CollectExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_parenthesisedexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_ParenthesisedExpression)


def test_pp1_parenthesisedexpression_constructor_exists():
    assert callable(pp1_ParenthesisedExpression.__init__)


def test_pp1_parenthesisedexpression_constructor_args():
    sig = inspect.signature(pp1_ParenthesisedExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_BinaryExpression)


def test_pp1_binaryexpression_constructor_exists():
    assert callable(pp1_BinaryExpression.__init__)


def test_pp1_binaryexpression_constructor_args():
    sig = inspect.signature(pp1_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_unlessexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_UnlessExpression)


def test_pp1_unlessexpression_constructor_exists():
    assert callable(pp1_UnlessExpression.__init__)


def test_pp1_unlessexpression_constructor_args():
    sig = inspect.signature(pp1_UnlessExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_definition_is_not_abstract():
    assert not inspect.isabstract(pp1_Definition)


def test_pp1_definition_constructor_exists():
    assert callable(pp1_Definition.__init__)


def test_pp1_definition_constructor_args():
    sig = inspect.signature(pp1_Definition.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"

def test_pp1_definition_has_className():
    assert hasattr(pp1_Definition, "className")
    descriptor = None
    for klass in pp1_Definition.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_pp1_literalexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_LiteralExpression)


def test_pp1_literalexpression_constructor_exists():
    assert callable(pp1_LiteralExpression.__init__)


def test_pp1_literalexpression_constructor_args():
    sig = inspect.signature(pp1_LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_pp1_hostclassdefinition_is_not_abstract():
    assert not inspect.isabstract(pp1_HostClassDefinition)


def test_pp1_hostclassdefinition_constructor_exists():
    assert callable(pp1_HostClassDefinition.__init__)


def test_pp1_hostclassdefinition_constructor_args():
    sig = inspect.signature(pp1_HostClassDefinition.__init__)
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



def test_pp1_unaryminusexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_UnaryMinusExpression)


def test_pp1_unaryminusexpression_constructor_exists():
    assert callable(pp1_UnaryMinusExpression.__init__)


def test_pp1_unaryminusexpression_constructor_args():
    sig = inspect.signature(pp1_UnaryMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_exportedcollectquery_is_not_abstract():
    assert not inspect.isabstract(pp1_ExportedCollectQuery)


def test_pp1_exportedcollectquery_constructor_exists():
    assert callable(pp1_ExportedCollectQuery.__init__)


def test_pp1_exportedcollectquery_constructor_args():
    sig = inspect.signature(pp1_ExportedCollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_pp1_unarynotexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_UnaryNotExpression)


def test_pp1_unarynotexpression_constructor_exists():
    assert callable(pp1_UnaryNotExpression.__init__)


def test_pp1_unarynotexpression_constructor_args():
    sig = inspect.signature(pp1_UnaryNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_virtualcollectquery_is_not_abstract():
    assert not inspect.isabstract(pp1_VirtualCollectQuery)


def test_pp1_virtualcollectquery_constructor_exists():
    assert callable(pp1_VirtualCollectQuery.__init__)


def test_pp1_virtualcollectquery_constructor_args():
    sig = inspect.signature(pp1_VirtualCollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_pp1_icollectquery_is_not_abstract():
    assert not inspect.isabstract(pp1_ICollectQuery)


def test_pp1_icollectquery_constructor_exists():
    assert callable(pp1_ICollectQuery.__init__)


def test_pp1_icollectquery_constructor_args():
    sig = inspect.signature(pp1_ICollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_pp1_attributeoperation_is_not_abstract():
    assert not inspect.isabstract(pp1_AttributeOperation)


def test_pp1_attributeoperation_constructor_exists():
    assert callable(pp1_AttributeOperation.__init__)


def test_pp1_attributeoperation_constructor_args():
    sig = inspect.signature(pp1_AttributeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "op" in params, "Missing parameter 'op'"

def test_pp1_attributeoperation_has_key():
    assert hasattr(pp1_AttributeOperation, "key")
    descriptor = None
    for klass in pp1_AttributeOperation.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_pp1_attributeoperation_has_op():
    assert hasattr(pp1_AttributeOperation, "op")
    descriptor = None
    for klass in pp1_AttributeOperation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_pp1_attributeoperations_is_not_abstract():
    assert not inspect.isabstract(pp1_AttributeOperations)


def test_pp1_attributeoperations_constructor_exists():
    assert callable(pp1_AttributeOperations.__init__)


def test_pp1_attributeoperations_constructor_args():
    sig = inspect.signature(pp1_AttributeOperations.__init__)
    params = list(sig.parameters.keys())



def test_pp1_resourcebody_is_not_abstract():
    assert not inspect.isabstract(pp1_ResourceBody)


def test_pp1_resourcebody_constructor_exists():
    assert callable(pp1_ResourceBody.__init__)


def test_pp1_resourcebody_constructor_args():
    sig = inspect.signature(pp1_ResourceBody.__init__)
    params = list(sig.parameters.keys())



def test_pp1_expression_is_not_abstract():
    assert not inspect.isabstract(pp1_Expression)


def test_pp1_expression_constructor_exists():
    assert callable(pp1_Expression.__init__)


def test_pp1_expression_constructor_args():
    sig = inspect.signature(pp1_Expression.__init__)
    params = list(sig.parameters.keys())



def test_expressionblock_is_not_abstract():
    assert not inspect.isabstract(ExpressionBlock)


def test_expressionblock_constructor_exists():
    assert callable(ExpressionBlock.__init__)


def test_expressionblock_constructor_args():
    sig = inspect.signature(ExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_pp1_elseexpression_is_not_abstract():
    assert not inspect.isabstract(pp1_ElseExpression)


def test_pp1_elseexpression_constructor_exists():
    assert callable(pp1_ElseExpression.__init__)


def test_pp1_elseexpression_constructor_args():
    sig = inspect.signature(pp1_ElseExpression.__init__)
    params = list(sig.parameters.keys())



def test_pp1_lambda_is_not_abstract():
    assert not inspect.isabstract(pp1_Lambda)


def test_pp1_lambda_constructor_exists():
    assert callable(pp1_Lambda.__init__)


def test_pp1_lambda_constructor_args():
    sig = inspect.signature(pp1_Lambda.__init__)
    params = list(sig.parameters.keys())



def test_pp1_puppetmanifest_is_not_abstract():
    assert not inspect.isabstract(pp1_PuppetManifest)


def test_pp1_puppetmanifest_constructor_exists():
    assert callable(pp1_PuppetManifest.__init__)


def test_pp1_puppetmanifest_constructor_args():
    sig = inspect.signature(pp1_PuppetManifest.__init__)
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
pp1_VariableTE_strategy = st.builds(
    pp1_VariableTE,
    varName=
        safe_text
)
pp1_ExpressionTE_strategy = st.builds(
    pp1_ExpressionTE,
)
pp1_VerbatimTE_strategy = st.builds(
    pp1_VerbatimTE,
    text=
        safe_text
)
Lambda_strategy = st.builds(
    Lambda,
)
pp1_RubyLambda_strategy = st.builds(
    pp1_RubyLambda,
)
pp1_JavaLambda_strategy = st.builds(
    pp1_JavaLambda,
    farrow=
        st.booleans()
)
pp1_TextExpression_strategy = st.builds(
    pp1_TextExpression,
)
IQuotedString_strategy = st.builds(
    IQuotedString,
)
StringExpression_strategy = st.builds(
    StringExpression,
)
pp1_SingleQuotedString_strategy = st.builds(
    pp1_SingleQuotedString,
    text=
        safe_text
)
pp1_UnquotedString_strategy = st.builds(
    pp1_UnquotedString,
)
pp1_DoubleQuotedString_strategy = st.builds(
    pp1_DoubleQuotedString,
)
IfExpression_strategy = st.builds(
    IfExpression,
)
pp1_ElseIfExpression_strategy = st.builds(
    pp1_ElseIfExpression,
)
WithLambdaExpression_strategy = st.builds(
    WithLambdaExpression,
)
pp1_MethodCall_strategy = st.builds(
    pp1_MethodCall,
    parenthesized=
        st.booleans()
)
pp1_FunctionCall_strategy = st.builds(
    pp1_FunctionCall,
)
ParameterizedExpression_strategy = st.builds(
    ParameterizedExpression,
)
pp1_WithLambdaExpression_strategy = st.builds(
    pp1_WithLambdaExpression,
)
pp1_SelectorExpression_strategy = st.builds(
    pp1_SelectorExpression,
)
pp1_AtExpression_strategy = st.builds(
    pp1_AtExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
pp1_OrExpression_strategy = st.builds(
    pp1_OrExpression,
)
pp1_NamedAccessExpression_strategy = st.builds(
    pp1_NamedAccessExpression,
)
pp1_AppendExpression_strategy = st.builds(
    pp1_AppendExpression,
)
pp1_BinaryOpExpression_strategy = st.builds(
    pp1_BinaryOpExpression,
    opName=
        safe_text
)
pp1_SelectorEntry_strategy = st.builds(
    pp1_SelectorEntry,
)
pp1_AndExpression_strategy = st.builds(
    pp1_AndExpression,
)
pp1_AssignmentExpression_strategy = st.builds(
    pp1_AssignmentExpression,
)
pp1_Case_strategy = st.builds(
    pp1_Case,
)
BinaryOpExpression_strategy = st.builds(
    BinaryOpExpression,
)
pp1_ShiftExpression_strategy = st.builds(
    pp1_ShiftExpression,
)
pp1_AdditiveExpression_strategy = st.builds(
    pp1_AdditiveExpression,
)
pp1_RelationalExpression_strategy = st.builds(
    pp1_RelationalExpression,
)
pp1_EqualityExpression_strategy = st.builds(
    pp1_EqualityExpression,
)
pp1_InExpression_strategy = st.builds(
    pp1_InExpression,
)
pp1_MatchingExpression_strategy = st.builds(
    pp1_MatchingExpression,
)
pp1_MultiplicativeExpression_strategy = st.builds(
    pp1_MultiplicativeExpression,
)
pp1_RelationshipExpression_strategy = st.builds(
    pp1_RelationshipExpression,
)
pp1_HashEntry_strategy = st.builds(
    pp1_HashEntry,
)
pp1_IQuotedString_strategy = st.builds(
    pp1_IQuotedString,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
pp1_LiteralList_strategy = st.builds(
    pp1_LiteralList,
)
pp1_LiteralBoolean_strategy = st.builds(
    pp1_LiteralBoolean,
    value=
        st.booleans()
)
pp1_LiteralDefault_strategy = st.builds(
    pp1_LiteralDefault,
)
pp1_LiteralName_strategy = st.builds(
    pp1_LiteralName,
    value=
        safe_text
)
pp1_LiteralUndef_strategy = st.builds(
    pp1_LiteralUndef,
)
pp1_LiteralClass_strategy = st.builds(
    pp1_LiteralClass,
)
pp1_VirtualNameOrReference_strategy = st.builds(
    pp1_VirtualNameOrReference,
    exported=
        st.booleans(),
    value=
        safe_text
)
pp1_LiteralHash_strategy = st.builds(
    pp1_LiteralHash,
)
pp1_LiteralRegex_strategy = st.builds(
    pp1_LiteralRegex,
    value=
        safe_text
)
pp1_LiteralNameOrReference_strategy = st.builds(
    pp1_LiteralNameOrReference,
    value=
        safe_text
)
pp1_DefinitionArgument_strategy = st.builds(
    pp1_DefinitionArgument,
    op=
        safe_text,
    argName=
        safe_text
)
pp1_DefinitionArgumentList_strategy = st.builds(
    pp1_DefinitionArgumentList,
)
Expression_strategy = st.builds(
    Expression,
)
pp1_InterpolatedVariable_strategy = st.builds(
    pp1_InterpolatedVariable,
    varName=
        safe_text
)
pp1_SeparatorExpression_strategy = st.builds(
    pp1_SeparatorExpression,
)
pp1_NodeDefinition_strategy = st.builds(
    pp1_NodeDefinition,
)
pp1_ExpressionBlock_strategy = st.builds(
    pp1_ExpressionBlock,
)
pp1_ExprList_strategy = st.builds(
    pp1_ExprList,
)
pp1_ParameterizedExpression_strategy = st.builds(
    pp1_ParameterizedExpression,
)
pp1_VariableExpression_strategy = st.builds(
    pp1_VariableExpression,
    varName=
        safe_text
)
pp1_UnaryExpression_strategy = st.builds(
    pp1_UnaryExpression,
)
pp1_ResourceExpression_strategy = st.builds(
    pp1_ResourceExpression,
)
pp1_StringExpression_strategy = st.builds(
    pp1_StringExpression,
)
pp1_IfExpression_strategy = st.builds(
    pp1_IfExpression,
)
pp1_ImportExpression_strategy = st.builds(
    pp1_ImportExpression,
)
pp1_CaseExpression_strategy = st.builds(
    pp1_CaseExpression,
)
pp1_CollectExpression_strategy = st.builds(
    pp1_CollectExpression,
)
pp1_ParenthesisedExpression_strategy = st.builds(
    pp1_ParenthesisedExpression,
)
pp1_BinaryExpression_strategy = st.builds(
    pp1_BinaryExpression,
)
pp1_UnlessExpression_strategy = st.builds(
    pp1_UnlessExpression,
)
pp1_Definition_strategy = st.builds(
    pp1_Definition,
    className=
        safe_text
)
pp1_LiteralExpression_strategy = st.builds(
    pp1_LiteralExpression,
)
Definition_strategy = st.builds(
    Definition,
)
pp1_HostClassDefinition_strategy = st.builds(
    pp1_HostClassDefinition,
)
ICollectQuery_strategy = st.builds(
    ICollectQuery,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
pp1_UnaryMinusExpression_strategy = st.builds(
    pp1_UnaryMinusExpression,
)
pp1_ExportedCollectQuery_strategy = st.builds(
    pp1_ExportedCollectQuery,
)
pp1_UnaryNotExpression_strategy = st.builds(
    pp1_UnaryNotExpression,
)
pp1_VirtualCollectQuery_strategy = st.builds(
    pp1_VirtualCollectQuery,
)
pp1_ICollectQuery_strategy = st.builds(
    pp1_ICollectQuery,
)
pp1_AttributeOperation_strategy = st.builds(
    pp1_AttributeOperation,
    key=
        safe_text,
    op=
        safe_text
)
pp1_AttributeOperations_strategy = st.builds(
    pp1_AttributeOperations,
)
pp1_ResourceBody_strategy = st.builds(
    pp1_ResourceBody,
)
pp1_Expression_strategy = st.builds(
    pp1_Expression,
)
ExpressionBlock_strategy = st.builds(
    ExpressionBlock,
)
pp1_ElseExpression_strategy = st.builds(
    pp1_ElseExpression,
)
pp1_Lambda_strategy = st.builds(
    pp1_Lambda,
)
pp1_PuppetManifest_strategy = st.builds(
    pp1_PuppetManifest,
)

@given(instance=TextExpression_strategy)
@settings(max_examples=50)
def test_textexpression_instantiation(instance):
    assert isinstance(instance, TextExpression)

@given(instance=pp1_VariableTE_strategy)
@settings(max_examples=50)
def test_pp1_variablete_instantiation(instance):
    assert isinstance(instance, pp1_VariableTE)



@given(instance=pp1_VariableTE_strategy)
def test_pp1_variablete_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=pp1_ExpressionTE_strategy)
@settings(max_examples=50)
def test_pp1_expressionte_instantiation(instance):
    assert isinstance(instance, pp1_ExpressionTE)

@given(instance=pp1_VerbatimTE_strategy)
@settings(max_examples=50)
def test_pp1_verbatimte_instantiation(instance):
    assert isinstance(instance, pp1_VerbatimTE)



@given(instance=pp1_VerbatimTE_strategy)
def test_pp1_verbatimte_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Lambda_strategy)
@settings(max_examples=50)
def test_lambda_instantiation(instance):
    assert isinstance(instance, Lambda)

@given(instance=pp1_RubyLambda_strategy)
@settings(max_examples=50)
def test_pp1_rubylambda_instantiation(instance):
    assert isinstance(instance, pp1_RubyLambda)

@given(instance=pp1_JavaLambda_strategy)
@settings(max_examples=50)
def test_pp1_javalambda_instantiation(instance):
    assert isinstance(instance, pp1_JavaLambda)



@given(instance=pp1_JavaLambda_strategy)
def test_pp1_javalambda_farrow_setter(instance):
    original = instance.farrow
    instance.farrow = original
    assert instance.farrow == original

@given(instance=pp1_TextExpression_strategy)
@settings(max_examples=50)
def test_pp1_textexpression_instantiation(instance):
    assert isinstance(instance, pp1_TextExpression)

@given(instance=IQuotedString_strategy)
@settings(max_examples=50)
def test_iquotedstring_instantiation(instance):
    assert isinstance(instance, IQuotedString)

@given(instance=StringExpression_strategy)
@settings(max_examples=50)
def test_stringexpression_instantiation(instance):
    assert isinstance(instance, StringExpression)

@given(instance=pp1_SingleQuotedString_strategy)
@settings(max_examples=50)
def test_pp1_singlequotedstring_instantiation(instance):
    assert isinstance(instance, pp1_SingleQuotedString)



@given(instance=pp1_SingleQuotedString_strategy)
def test_pp1_singlequotedstring_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=pp1_UnquotedString_strategy)
@settings(max_examples=50)
def test_pp1_unquotedstring_instantiation(instance):
    assert isinstance(instance, pp1_UnquotedString)

@given(instance=pp1_DoubleQuotedString_strategy)
@settings(max_examples=50)
def test_pp1_doublequotedstring_instantiation(instance):
    assert isinstance(instance, pp1_DoubleQuotedString)

@given(instance=IfExpression_strategy)
@settings(max_examples=50)
def test_ifexpression_instantiation(instance):
    assert isinstance(instance, IfExpression)

@given(instance=pp1_ElseIfExpression_strategy)
@settings(max_examples=50)
def test_pp1_elseifexpression_instantiation(instance):
    assert isinstance(instance, pp1_ElseIfExpression)

@given(instance=WithLambdaExpression_strategy)
@settings(max_examples=50)
def test_withlambdaexpression_instantiation(instance):
    assert isinstance(instance, WithLambdaExpression)

@given(instance=pp1_MethodCall_strategy)
@settings(max_examples=50)
def test_pp1_methodcall_instantiation(instance):
    assert isinstance(instance, pp1_MethodCall)



@given(instance=pp1_MethodCall_strategy)
def test_pp1_methodcall_parenthesized_setter(instance):
    original = instance.parenthesized
    instance.parenthesized = original
    assert instance.parenthesized == original

@given(instance=pp1_FunctionCall_strategy)
@settings(max_examples=50)
def test_pp1_functioncall_instantiation(instance):
    assert isinstance(instance, pp1_FunctionCall)

@given(instance=ParameterizedExpression_strategy)
@settings(max_examples=50)
def test_parameterizedexpression_instantiation(instance):
    assert isinstance(instance, ParameterizedExpression)

@given(instance=pp1_WithLambdaExpression_strategy)
@settings(max_examples=50)
def test_pp1_withlambdaexpression_instantiation(instance):
    assert isinstance(instance, pp1_WithLambdaExpression)

@given(instance=pp1_SelectorExpression_strategy)
@settings(max_examples=50)
def test_pp1_selectorexpression_instantiation(instance):
    assert isinstance(instance, pp1_SelectorExpression)

@given(instance=pp1_AtExpression_strategy)
@settings(max_examples=50)
def test_pp1_atexpression_instantiation(instance):
    assert isinstance(instance, pp1_AtExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=pp1_OrExpression_strategy)
@settings(max_examples=50)
def test_pp1_orexpression_instantiation(instance):
    assert isinstance(instance, pp1_OrExpression)

@given(instance=pp1_NamedAccessExpression_strategy)
@settings(max_examples=50)
def test_pp1_namedaccessexpression_instantiation(instance):
    assert isinstance(instance, pp1_NamedAccessExpression)

@given(instance=pp1_AppendExpression_strategy)
@settings(max_examples=50)
def test_pp1_appendexpression_instantiation(instance):
    assert isinstance(instance, pp1_AppendExpression)

@given(instance=pp1_BinaryOpExpression_strategy)
@settings(max_examples=50)
def test_pp1_binaryopexpression_instantiation(instance):
    assert isinstance(instance, pp1_BinaryOpExpression)



@given(instance=pp1_BinaryOpExpression_strategy)
def test_pp1_binaryopexpression_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=pp1_SelectorEntry_strategy)
@settings(max_examples=50)
def test_pp1_selectorentry_instantiation(instance):
    assert isinstance(instance, pp1_SelectorEntry)

@given(instance=pp1_AndExpression_strategy)
@settings(max_examples=50)
def test_pp1_andexpression_instantiation(instance):
    assert isinstance(instance, pp1_AndExpression)

@given(instance=pp1_AssignmentExpression_strategy)
@settings(max_examples=50)
def test_pp1_assignmentexpression_instantiation(instance):
    assert isinstance(instance, pp1_AssignmentExpression)

@given(instance=pp1_Case_strategy)
@settings(max_examples=50)
def test_pp1_case_instantiation(instance):
    assert isinstance(instance, pp1_Case)

@given(instance=BinaryOpExpression_strategy)
@settings(max_examples=50)
def test_binaryopexpression_instantiation(instance):
    assert isinstance(instance, BinaryOpExpression)

@given(instance=pp1_ShiftExpression_strategy)
@settings(max_examples=50)
def test_pp1_shiftexpression_instantiation(instance):
    assert isinstance(instance, pp1_ShiftExpression)

@given(instance=pp1_AdditiveExpression_strategy)
@settings(max_examples=50)
def test_pp1_additiveexpression_instantiation(instance):
    assert isinstance(instance, pp1_AdditiveExpression)

@given(instance=pp1_RelationalExpression_strategy)
@settings(max_examples=50)
def test_pp1_relationalexpression_instantiation(instance):
    assert isinstance(instance, pp1_RelationalExpression)

@given(instance=pp1_EqualityExpression_strategy)
@settings(max_examples=50)
def test_pp1_equalityexpression_instantiation(instance):
    assert isinstance(instance, pp1_EqualityExpression)

@given(instance=pp1_InExpression_strategy)
@settings(max_examples=50)
def test_pp1_inexpression_instantiation(instance):
    assert isinstance(instance, pp1_InExpression)

@given(instance=pp1_MatchingExpression_strategy)
@settings(max_examples=50)
def test_pp1_matchingexpression_instantiation(instance):
    assert isinstance(instance, pp1_MatchingExpression)

@given(instance=pp1_MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_pp1_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, pp1_MultiplicativeExpression)

@given(instance=pp1_RelationshipExpression_strategy)
@settings(max_examples=50)
def test_pp1_relationshipexpression_instantiation(instance):
    assert isinstance(instance, pp1_RelationshipExpression)

@given(instance=pp1_HashEntry_strategy)
@settings(max_examples=50)
def test_pp1_hashentry_instantiation(instance):
    assert isinstance(instance, pp1_HashEntry)

@given(instance=pp1_IQuotedString_strategy)
@settings(max_examples=50)
def test_pp1_iquotedstring_instantiation(instance):
    assert isinstance(instance, pp1_IQuotedString)

@given(instance=LiteralExpression_strategy)
@settings(max_examples=50)
def test_literalexpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)

@given(instance=pp1_LiteralList_strategy)
@settings(max_examples=50)
def test_pp1_literallist_instantiation(instance):
    assert isinstance(instance, pp1_LiteralList)

@given(instance=pp1_LiteralBoolean_strategy)
@settings(max_examples=50)
def test_pp1_literalboolean_instantiation(instance):
    assert isinstance(instance, pp1_LiteralBoolean)



@given(instance=pp1_LiteralBoolean_strategy)
def test_pp1_literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp1_LiteralDefault_strategy)
@settings(max_examples=50)
def test_pp1_literaldefault_instantiation(instance):
    assert isinstance(instance, pp1_LiteralDefault)

@given(instance=pp1_LiteralName_strategy)
@settings(max_examples=50)
def test_pp1_literalname_instantiation(instance):
    assert isinstance(instance, pp1_LiteralName)



@given(instance=pp1_LiteralName_strategy)
def test_pp1_literalname_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp1_LiteralUndef_strategy)
@settings(max_examples=50)
def test_pp1_literalundef_instantiation(instance):
    assert isinstance(instance, pp1_LiteralUndef)

@given(instance=pp1_LiteralClass_strategy)
@settings(max_examples=50)
def test_pp1_literalclass_instantiation(instance):
    assert isinstance(instance, pp1_LiteralClass)

@given(instance=pp1_VirtualNameOrReference_strategy)
@settings(max_examples=50)
def test_pp1_virtualnameorreference_instantiation(instance):
    assert isinstance(instance, pp1_VirtualNameOrReference)



@given(instance=pp1_VirtualNameOrReference_strategy)
def test_pp1_virtualnameorreference_exported_setter(instance):
    original = instance.exported
    instance.exported = original
    assert instance.exported == original



@given(instance=pp1_VirtualNameOrReference_strategy)
def test_pp1_virtualnameorreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp1_LiteralHash_strategy)
@settings(max_examples=50)
def test_pp1_literalhash_instantiation(instance):
    assert isinstance(instance, pp1_LiteralHash)

@given(instance=pp1_LiteralRegex_strategy)
@settings(max_examples=50)
def test_pp1_literalregex_instantiation(instance):
    assert isinstance(instance, pp1_LiteralRegex)



@given(instance=pp1_LiteralRegex_strategy)
def test_pp1_literalregex_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp1_LiteralNameOrReference_strategy)
@settings(max_examples=50)
def test_pp1_literalnameorreference_instantiation(instance):
    assert isinstance(instance, pp1_LiteralNameOrReference)



@given(instance=pp1_LiteralNameOrReference_strategy)
def test_pp1_literalnameorreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pp1_DefinitionArgument_strategy)
@settings(max_examples=50)
def test_pp1_definitionargument_instantiation(instance):
    assert isinstance(instance, pp1_DefinitionArgument)



@given(instance=pp1_DefinitionArgument_strategy)
def test_pp1_definitionargument_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=pp1_DefinitionArgument_strategy)
def test_pp1_definitionargument_argName_setter(instance):
    original = instance.argName
    instance.argName = original
    assert instance.argName == original

@given(instance=pp1_DefinitionArgumentList_strategy)
@settings(max_examples=50)
def test_pp1_definitionargumentlist_instantiation(instance):
    assert isinstance(instance, pp1_DefinitionArgumentList)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=pp1_InterpolatedVariable_strategy)
@settings(max_examples=50)
def test_pp1_interpolatedvariable_instantiation(instance):
    assert isinstance(instance, pp1_InterpolatedVariable)



@given(instance=pp1_InterpolatedVariable_strategy)
def test_pp1_interpolatedvariable_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=pp1_SeparatorExpression_strategy)
@settings(max_examples=50)
def test_pp1_separatorexpression_instantiation(instance):
    assert isinstance(instance, pp1_SeparatorExpression)

@given(instance=pp1_NodeDefinition_strategy)
@settings(max_examples=50)
def test_pp1_nodedefinition_instantiation(instance):
    assert isinstance(instance, pp1_NodeDefinition)

@given(instance=pp1_ExpressionBlock_strategy)
@settings(max_examples=50)
def test_pp1_expressionblock_instantiation(instance):
    assert isinstance(instance, pp1_ExpressionBlock)

@given(instance=pp1_ExprList_strategy)
@settings(max_examples=50)
def test_pp1_exprlist_instantiation(instance):
    assert isinstance(instance, pp1_ExprList)

@given(instance=pp1_ParameterizedExpression_strategy)
@settings(max_examples=50)
def test_pp1_parameterizedexpression_instantiation(instance):
    assert isinstance(instance, pp1_ParameterizedExpression)

@given(instance=pp1_VariableExpression_strategy)
@settings(max_examples=50)
def test_pp1_variableexpression_instantiation(instance):
    assert isinstance(instance, pp1_VariableExpression)



@given(instance=pp1_VariableExpression_strategy)
def test_pp1_variableexpression_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=pp1_UnaryExpression_strategy)
@settings(max_examples=50)
def test_pp1_unaryexpression_instantiation(instance):
    assert isinstance(instance, pp1_UnaryExpression)

@given(instance=pp1_ResourceExpression_strategy)
@settings(max_examples=50)
def test_pp1_resourceexpression_instantiation(instance):
    assert isinstance(instance, pp1_ResourceExpression)

@given(instance=pp1_StringExpression_strategy)
@settings(max_examples=50)
def test_pp1_stringexpression_instantiation(instance):
    assert isinstance(instance, pp1_StringExpression)

@given(instance=pp1_IfExpression_strategy)
@settings(max_examples=50)
def test_pp1_ifexpression_instantiation(instance):
    assert isinstance(instance, pp1_IfExpression)

@given(instance=pp1_ImportExpression_strategy)
@settings(max_examples=50)
def test_pp1_importexpression_instantiation(instance):
    assert isinstance(instance, pp1_ImportExpression)

@given(instance=pp1_CaseExpression_strategy)
@settings(max_examples=50)
def test_pp1_caseexpression_instantiation(instance):
    assert isinstance(instance, pp1_CaseExpression)

@given(instance=pp1_CollectExpression_strategy)
@settings(max_examples=50)
def test_pp1_collectexpression_instantiation(instance):
    assert isinstance(instance, pp1_CollectExpression)

@given(instance=pp1_ParenthesisedExpression_strategy)
@settings(max_examples=50)
def test_pp1_parenthesisedexpression_instantiation(instance):
    assert isinstance(instance, pp1_ParenthesisedExpression)

@given(instance=pp1_BinaryExpression_strategy)
@settings(max_examples=50)
def test_pp1_binaryexpression_instantiation(instance):
    assert isinstance(instance, pp1_BinaryExpression)

@given(instance=pp1_UnlessExpression_strategy)
@settings(max_examples=50)
def test_pp1_unlessexpression_instantiation(instance):
    assert isinstance(instance, pp1_UnlessExpression)

@given(instance=pp1_Definition_strategy)
@settings(max_examples=50)
def test_pp1_definition_instantiation(instance):
    assert isinstance(instance, pp1_Definition)



@given(instance=pp1_Definition_strategy)
def test_pp1_definition_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=pp1_LiteralExpression_strategy)
@settings(max_examples=50)
def test_pp1_literalexpression_instantiation(instance):
    assert isinstance(instance, pp1_LiteralExpression)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=pp1_HostClassDefinition_strategy)
@settings(max_examples=50)
def test_pp1_hostclassdefinition_instantiation(instance):
    assert isinstance(instance, pp1_HostClassDefinition)

@given(instance=ICollectQuery_strategy)
@settings(max_examples=50)
def test_icollectquery_instantiation(instance):
    assert isinstance(instance, ICollectQuery)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=pp1_UnaryMinusExpression_strategy)
@settings(max_examples=50)
def test_pp1_unaryminusexpression_instantiation(instance):
    assert isinstance(instance, pp1_UnaryMinusExpression)

@given(instance=pp1_ExportedCollectQuery_strategy)
@settings(max_examples=50)
def test_pp1_exportedcollectquery_instantiation(instance):
    assert isinstance(instance, pp1_ExportedCollectQuery)

@given(instance=pp1_UnaryNotExpression_strategy)
@settings(max_examples=50)
def test_pp1_unarynotexpression_instantiation(instance):
    assert isinstance(instance, pp1_UnaryNotExpression)

@given(instance=pp1_VirtualCollectQuery_strategy)
@settings(max_examples=50)
def test_pp1_virtualcollectquery_instantiation(instance):
    assert isinstance(instance, pp1_VirtualCollectQuery)

@given(instance=pp1_ICollectQuery_strategy)
@settings(max_examples=50)
def test_pp1_icollectquery_instantiation(instance):
    assert isinstance(instance, pp1_ICollectQuery)

@given(instance=pp1_AttributeOperation_strategy)
@settings(max_examples=50)
def test_pp1_attributeoperation_instantiation(instance):
    assert isinstance(instance, pp1_AttributeOperation)



@given(instance=pp1_AttributeOperation_strategy)
def test_pp1_attributeoperation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=pp1_AttributeOperation_strategy)
def test_pp1_attributeoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=pp1_AttributeOperations_strategy)
@settings(max_examples=50)
def test_pp1_attributeoperations_instantiation(instance):
    assert isinstance(instance, pp1_AttributeOperations)

@given(instance=pp1_ResourceBody_strategy)
@settings(max_examples=50)
def test_pp1_resourcebody_instantiation(instance):
    assert isinstance(instance, pp1_ResourceBody)

@given(instance=pp1_Expression_strategy)
@settings(max_examples=50)
def test_pp1_expression_instantiation(instance):
    assert isinstance(instance, pp1_Expression)

@given(instance=ExpressionBlock_strategy)
@settings(max_examples=50)
def test_expressionblock_instantiation(instance):
    assert isinstance(instance, ExpressionBlock)

@given(instance=pp1_ElseExpression_strategy)
@settings(max_examples=50)
def test_pp1_elseexpression_instantiation(instance):
    assert isinstance(instance, pp1_ElseExpression)

@given(instance=pp1_Lambda_strategy)
@settings(max_examples=50)
def test_pp1_lambda_instantiation(instance):
    assert isinstance(instance, pp1_Lambda)

@given(instance=pp1_PuppetManifest_strategy)
@settings(max_examples=50)
def test_pp1_puppetmanifest_instantiation(instance):
    assert isinstance(instance, pp1_PuppetManifest)
