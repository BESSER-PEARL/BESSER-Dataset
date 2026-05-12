import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dsl_DefaultValue,
    dsl_AnnotationTypeMemberDeclaration,
    dsl_AnnotationTypeBody,
    dsl_MemberValueArrayInitializer,
    DefaultValue,
    dsl_MemberValuePair,
    dsl_MemberValue,
    dsl_MemberValuePairs,
    dsl_Annotation,
    dsl_StatementExpressionList,
    dsl_ForUpdate,
    dsl_ForInit,
    dsl_SwitchLabel,
    dsl_LocalVariableDeclaration,
    dsl_TryStatement,
    dsl_SynchronizedStatement,
    dsl_ThrowStatement,
    dsl_ReturnStatement,
    dsl_ContinueStatement,
    dsl_BreakStatement,
    dsl_ForStatement,
    dsl_DoStatement,
    dsl_WhileStatement,
    dsl_IfStatement,
    dsl_SwitchStatement,
    dsl_StatementExpression,
    dsl_AssertStatement,
    dsl_LabeledStatement,
    dsl_ArrayDimsAndInits,
    dsl_BaseLiteral,
    dsl_ArgumentList,
    dsl_BooleanLiteral,
    dsl_FloatLiteral,
    dsl_IntegerLiteral,
    dsl_SignedIntLiteral,
    dsl_UnsignedIntLiteral,
    dsl_MemberSelector,
    dsl_DecimalNumber,
    dsl_PrimarySuffix,
    dsl_AllocationExpression,
    dsl_PrimaryPrefix,
    dsl_PreDecrementExpression,
    dsl_PreIncrementExpression,
    dsl_EObject,
    dsl_Literal,
    dsl_CastLookahead,
    dsl_PostfixExpression,
    dsl_CastExpression,
    dsl_UnaryExpressionNotPlusMinus,
    dsl_UnaryExpression,
    dsl_MultiplicativeExpression,
    dsl_AdditiveExpression,
    dsl_ShiftExpression,
    dsl_RelationalExpression,
    dsl_InstanceOfExpression,
    dsl_EqualityExpression,
    dsl_AndExpression,
    dsl_ExclusiveOrExpression,
    dsl_InclusiveOrExpression,
    dsl_ConditionalAndExpression,
    IfStatement,
    dsl_ConditionalOrExpression,
    dsl_Statement,
    dsl_ConditionalExpression,
    dsl_WildcardBounds,
    dsl_TypeArgument,
    dsl_TypeArguments,
    dsl_ReferenceType,
    dsl_PrimaryExpression,
    dsl_VariableDeclaratorId,
    dsl_VariableDeclarator,
    dsl_FormalParameter,
    dsl_Block,
    dsl_MethodDeclarator,
    dsl_ResultType,
    dsl_BlockStatement,
    dsl_ExplicitConstructorInvocation,
    dsl_NameList,
    dsl_FormalParameters,
    dsl_Expression,
    dsl_ArrayInitializer,
    dsl_VariableInitializer,
    dsl_Type,
    dsl_FieldDeclaration,
    dsl_MethodOrCtorDeclaration,
    dsl_Initializer,
    dsl_TypeBound,
    dsl_TypeParameter,
    dsl_Arguments,
    dsl_ClassOrInterfaceBodyDeclaration,
    dsl_EnumConstant,
    dsl_EnumBody,
    dsl_ClassOrInterfaceType,
    dsl_ClassOrInterfaceBody,
    dsl_ImplementsList,
    dsl_ExtendsList,
    dsl_TypeParameters,
    dsl_AnnotationTypeDeclaration,
    dsl_EnumDeclaration,
    dsl_ClassOrInterfaceDeclaration,
    dsl_TypeBodyModifier,
    dsl_CommonModifier,
    dsl_Name,
    dsl_TypeDeclaration,
    dsl_ImportDeclaration,
    dsl_PackageDeclaration,
    dsl_CompilationUnit,
    Visibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsl_defaultvalue_is_not_abstract():
    assert not inspect.isabstract(dsl_DefaultValue)


def test_dsl_defaultvalue_constructor_exists():
    assert callable(dsl_DefaultValue.__init__)


def test_dsl_defaultvalue_constructor_args():
    sig = inspect.signature(dsl_DefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_dsl_annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl_AnnotationTypeMemberDeclaration)


def test_dsl_annotationtypememberdeclaration_constructor_exists():
    assert callable(dsl_AnnotationTypeMemberDeclaration.__init__)


def test_dsl_annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(dsl_AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl_annotationtypememberdeclaration_has_id():
    assert hasattr(dsl_AnnotationTypeMemberDeclaration, "id")
    descriptor = None
    for klass in dsl_AnnotationTypeMemberDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl_annotationtypebody_is_not_abstract():
    assert not inspect.isabstract(dsl_AnnotationTypeBody)


def test_dsl_annotationtypebody_constructor_exists():
    assert callable(dsl_AnnotationTypeBody.__init__)


def test_dsl_annotationtypebody_constructor_args():
    sig = inspect.signature(dsl_AnnotationTypeBody.__init__)
    params = list(sig.parameters.keys())



def test_dsl_membervaluearrayinitializer_is_not_abstract():
    assert not inspect.isabstract(dsl_MemberValueArrayInitializer)


def test_dsl_membervaluearrayinitializer_constructor_exists():
    assert callable(dsl_MemberValueArrayInitializer.__init__)


def test_dsl_membervaluearrayinitializer_constructor_args():
    sig = inspect.signature(dsl_MemberValueArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_defaultvalue_is_not_abstract():
    assert not inspect.isabstract(DefaultValue)


def test_defaultvalue_constructor_exists():
    assert callable(DefaultValue.__init__)


def test_defaultvalue_constructor_args():
    sig = inspect.signature(DefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_dsl_membervaluepair_is_not_abstract():
    assert not inspect.isabstract(dsl_MemberValuePair)


def test_dsl_membervaluepair_constructor_exists():
    assert callable(dsl_MemberValuePair.__init__)


def test_dsl_membervaluepair_constructor_args():
    sig = inspect.signature(dsl_MemberValuePair.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl_membervaluepair_has_id():
    assert hasattr(dsl_MemberValuePair, "id")
    descriptor = None
    for klass in dsl_MemberValuePair.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl_membervalue_is_not_abstract():
    assert not inspect.isabstract(dsl_MemberValue)


def test_dsl_membervalue_constructor_exists():
    assert callable(dsl_MemberValue.__init__)


def test_dsl_membervalue_constructor_args():
    sig = inspect.signature(dsl_MemberValue.__init__)
    params = list(sig.parameters.keys())



def test_dsl_membervaluepairs_is_not_abstract():
    assert not inspect.isabstract(dsl_MemberValuePairs)


def test_dsl_membervaluepairs_constructor_exists():
    assert callable(dsl_MemberValuePairs.__init__)


def test_dsl_membervaluepairs_constructor_args():
    sig = inspect.signature(dsl_MemberValuePairs.__init__)
    params = list(sig.parameters.keys())



def test_dsl_annotation_is_not_abstract():
    assert not inspect.isabstract(dsl_Annotation)


def test_dsl_annotation_constructor_exists():
    assert callable(dsl_Annotation.__init__)


def test_dsl_annotation_constructor_args():
    sig = inspect.signature(dsl_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_dsl_statementexpressionlist_is_not_abstract():
    assert not inspect.isabstract(dsl_StatementExpressionList)


def test_dsl_statementexpressionlist_constructor_exists():
    assert callable(dsl_StatementExpressionList.__init__)


def test_dsl_statementexpressionlist_constructor_args():
    sig = inspect.signature(dsl_StatementExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_dsl_forupdate_is_not_abstract():
    assert not inspect.isabstract(dsl_ForUpdate)


def test_dsl_forupdate_constructor_exists():
    assert callable(dsl_ForUpdate.__init__)


def test_dsl_forupdate_constructor_args():
    sig = inspect.signature(dsl_ForUpdate.__init__)
    params = list(sig.parameters.keys())



def test_dsl_forinit_is_not_abstract():
    assert not inspect.isabstract(dsl_ForInit)


def test_dsl_forinit_constructor_exists():
    assert callable(dsl_ForInit.__init__)


def test_dsl_forinit_constructor_args():
    sig = inspect.signature(dsl_ForInit.__init__)
    params = list(sig.parameters.keys())



def test_dsl_switchlabel_is_not_abstract():
    assert not inspect.isabstract(dsl_SwitchLabel)


def test_dsl_switchlabel_constructor_exists():
    assert callable(dsl_SwitchLabel.__init__)


def test_dsl_switchlabel_constructor_args():
    sig = inspect.signature(dsl_SwitchLabel.__init__)
    params = list(sig.parameters.keys())
    assert "defaultOp" in params, "Missing parameter 'defaultOp'"

def test_dsl_switchlabel_has_defaultOp():
    assert hasattr(dsl_SwitchLabel, "defaultOp")
    descriptor = None
    for klass in dsl_SwitchLabel.__mro__:
        if "defaultOp" in klass.__dict__:
            descriptor = klass.__dict__["defaultOp"]
            break
    assert isinstance(descriptor, property)



def test_dsl_localvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl_LocalVariableDeclaration)


def test_dsl_localvariabledeclaration_constructor_exists():
    assert callable(dsl_LocalVariableDeclaration.__init__)


def test_dsl_localvariabledeclaration_constructor_args():
    sig = inspect.signature(dsl_LocalVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "finality" in params, "Missing parameter 'finality'"

def test_dsl_localvariabledeclaration_has_finality():
    assert hasattr(dsl_LocalVariableDeclaration, "finality")
    descriptor = None
    for klass in dsl_LocalVariableDeclaration.__mro__:
        if "finality" in klass.__dict__:
            descriptor = klass.__dict__["finality"]
            break
    assert isinstance(descriptor, property)



def test_dsl_trystatement_is_not_abstract():
    assert not inspect.isabstract(dsl_TryStatement)


def test_dsl_trystatement_constructor_exists():
    assert callable(dsl_TryStatement.__init__)


def test_dsl_trystatement_constructor_args():
    sig = inspect.signature(dsl_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl_synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(dsl_SynchronizedStatement)


def test_dsl_synchronizedstatement_constructor_exists():
    assert callable(dsl_SynchronizedStatement.__init__)


def test_dsl_synchronizedstatement_constructor_args():
    sig = inspect.signature(dsl_SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl_throwstatement_is_not_abstract():
    assert not inspect.isabstract(dsl_ThrowStatement)


def test_dsl_throwstatement_constructor_exists():
    assert callable(dsl_ThrowStatement.__init__)


def test_dsl_throwstatement_constructor_args():
    sig = inspect.signature(dsl_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl_returnstatement_is_not_abstract():
    assert not inspect.isabstract(dsl_ReturnStatement)


def test_dsl_returnstatement_constructor_exists():
    assert callable(dsl_ReturnStatement.__init__)


def test_dsl_returnstatement_constructor_args():
    sig = inspect.signature(dsl_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl_continuestatement_is_not_abstract():
    assert not inspect.isabstract(dsl_ContinueStatement)


def test_dsl_continuestatement_constructor_exists():
    assert callable(dsl_ContinueStatement.__init__)


def test_dsl_continuestatement_constructor_args():
    sig = inspect.signature(dsl_ContinueStatement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl_continuestatement_has_id():
    assert hasattr(dsl_ContinueStatement, "id")
    descriptor = None
    for klass in dsl_ContinueStatement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl_breakstatement_is_not_abstract():
    assert not inspect.isabstract(dsl_BreakStatement)


def test_dsl_breakstatement_constructor_exists():
    assert callable(dsl_BreakStatement.__init__)


def test_dsl_breakstatement_constructor_args():
    sig = inspect.signature(dsl_BreakStatement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl_breakstatement_has_id():
    assert hasattr(dsl_BreakStatement, "id")
    descriptor = None
    for klass in dsl_BreakStatement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl_forstatement_is_not_abstract():
    assert not inspect.isabstract(dsl_ForStatement)


def test_dsl_forstatement_constructor_exists():
    assert callable(dsl_ForStatement.__init__)


def test_dsl_forstatement_constructor_args():
    sig = inspect.signature(dsl_ForStatement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl_forstatement_has_id():
    assert hasattr(dsl_ForStatement, "id")
    descriptor = None
    for klass in dsl_ForStatement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl_dostatement_is_not_abstract():
    assert not inspect.isabstract(dsl_DoStatement)


def test_dsl_dostatement_constructor_exists():
    assert callable(dsl_DoStatement.__init__)


def test_dsl_dostatement_constructor_args():
    sig = inspect.signature(dsl_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl_whilestatement_is_not_abstract():
    assert not inspect.isabstract(dsl_WhileStatement)


def test_dsl_whilestatement_constructor_exists():
    assert callable(dsl_WhileStatement.__init__)


def test_dsl_whilestatement_constructor_args():
    sig = inspect.signature(dsl_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl_ifstatement_is_not_abstract():
    assert not inspect.isabstract(dsl_IfStatement)


def test_dsl_ifstatement_constructor_exists():
    assert callable(dsl_IfStatement.__init__)


def test_dsl_ifstatement_constructor_args():
    sig = inspect.signature(dsl_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl_switchstatement_is_not_abstract():
    assert not inspect.isabstract(dsl_SwitchStatement)


def test_dsl_switchstatement_constructor_exists():
    assert callable(dsl_SwitchStatement.__init__)


def test_dsl_switchstatement_constructor_args():
    sig = inspect.signature(dsl_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl_statementexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_StatementExpression)


def test_dsl_statementexpression_constructor_exists():
    assert callable(dsl_StatementExpression.__init__)


def test_dsl_statementexpression_constructor_args():
    sig = inspect.signature(dsl_StatementExpression.__init__)
    params = list(sig.parameters.keys())
    assert "minOp" in params, "Missing parameter 'minOp'"
    assert "plusOp" in params, "Missing parameter 'plusOp'"
    assert "assignOp" in params, "Missing parameter 'assignOp'"

def test_dsl_statementexpression_has_minOp():
    assert hasattr(dsl_StatementExpression, "minOp")
    descriptor = None
    for klass in dsl_StatementExpression.__mro__:
        if "minOp" in klass.__dict__:
            descriptor = klass.__dict__["minOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl_statementexpression_has_plusOp():
    assert hasattr(dsl_StatementExpression, "plusOp")
    descriptor = None
    for klass in dsl_StatementExpression.__mro__:
        if "plusOp" in klass.__dict__:
            descriptor = klass.__dict__["plusOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl_statementexpression_has_assignOp():
    assert hasattr(dsl_StatementExpression, "assignOp")
    descriptor = None
    for klass in dsl_StatementExpression.__mro__:
        if "assignOp" in klass.__dict__:
            descriptor = klass.__dict__["assignOp"]
            break
    assert isinstance(descriptor, property)



def test_dsl_assertstatement_is_not_abstract():
    assert not inspect.isabstract(dsl_AssertStatement)


def test_dsl_assertstatement_constructor_exists():
    assert callable(dsl_AssertStatement.__init__)


def test_dsl_assertstatement_constructor_args():
    sig = inspect.signature(dsl_AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(dsl_LabeledStatement)


def test_dsl_labeledstatement_constructor_exists():
    assert callable(dsl_LabeledStatement.__init__)


def test_dsl_labeledstatement_constructor_args():
    sig = inspect.signature(dsl_LabeledStatement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl_labeledstatement_has_id():
    assert hasattr(dsl_LabeledStatement, "id")
    descriptor = None
    for klass in dsl_LabeledStatement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl_arraydimsandinits_is_not_abstract():
    assert not inspect.isabstract(dsl_ArrayDimsAndInits)


def test_dsl_arraydimsandinits_constructor_exists():
    assert callable(dsl_ArrayDimsAndInits.__init__)


def test_dsl_arraydimsandinits_constructor_args():
    sig = inspect.signature(dsl_ArrayDimsAndInits.__init__)
    params = list(sig.parameters.keys())
    assert "squareBrackets" in params, "Missing parameter 'squareBrackets'"

def test_dsl_arraydimsandinits_has_squareBrackets():
    assert hasattr(dsl_ArrayDimsAndInits, "squareBrackets")
    descriptor = None
    for klass in dsl_ArrayDimsAndInits.__mro__:
        if "squareBrackets" in klass.__dict__:
            descriptor = klass.__dict__["squareBrackets"]
            break
    assert isinstance(descriptor, property)



def test_dsl_baseliteral_is_not_abstract():
    assert not inspect.isabstract(dsl_BaseLiteral)


def test_dsl_baseliteral_constructor_exists():
    assert callable(dsl_BaseLiteral.__init__)


def test_dsl_baseliteral_constructor_args():
    sig = inspect.signature(dsl_BaseLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "hexDigitsUnderscore" in params, "Missing parameter 'hexDigitsUnderscore'"
    assert "decDigitsUnderscore" in params, "Missing parameter 'decDigitsUnderscore'"
    assert "binDigitsUnderscore" in params, "Missing parameter 'binDigitsUnderscore'"

def test_dsl_baseliteral_has_hexDigitsUnderscore():
    assert hasattr(dsl_BaseLiteral, "hexDigitsUnderscore")
    descriptor = None
    for klass in dsl_BaseLiteral.__mro__:
        if "hexDigitsUnderscore" in klass.__dict__:
            descriptor = klass.__dict__["hexDigitsUnderscore"]
            break
    assert isinstance(descriptor, property)

def test_dsl_baseliteral_has_decDigitsUnderscore():
    assert hasattr(dsl_BaseLiteral, "decDigitsUnderscore")
    descriptor = None
    for klass in dsl_BaseLiteral.__mro__:
        if "decDigitsUnderscore" in klass.__dict__:
            descriptor = klass.__dict__["decDigitsUnderscore"]
            break
    assert isinstance(descriptor, property)

def test_dsl_baseliteral_has_binDigitsUnderscore():
    assert hasattr(dsl_BaseLiteral, "binDigitsUnderscore")
    descriptor = None
    for klass in dsl_BaseLiteral.__mro__:
        if "binDigitsUnderscore" in klass.__dict__:
            descriptor = klass.__dict__["binDigitsUnderscore"]
            break
    assert isinstance(descriptor, property)



def test_dsl_argumentlist_is_not_abstract():
    assert not inspect.isabstract(dsl_ArgumentList)


def test_dsl_argumentlist_constructor_exists():
    assert callable(dsl_ArgumentList.__init__)


def test_dsl_argumentlist_constructor_args():
    sig = inspect.signature(dsl_ArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_dsl_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(dsl_BooleanLiteral)


def test_dsl_booleanliteral_constructor_exists():
    assert callable(dsl_BooleanLiteral.__init__)


def test_dsl_booleanliteral_constructor_args():
    sig = inspect.signature(dsl_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "truthiness" in params, "Missing parameter 'truthiness'"

def test_dsl_booleanliteral_has_truthiness():
    assert hasattr(dsl_BooleanLiteral, "truthiness")
    descriptor = None
    for klass in dsl_BooleanLiteral.__mro__:
        if "truthiness" in klass.__dict__:
            descriptor = klass.__dict__["truthiness"]
            break
    assert isinstance(descriptor, property)



def test_dsl_floatliteral_is_not_abstract():
    assert not inspect.isabstract(dsl_FloatLiteral)


def test_dsl_floatliteral_constructor_exists():
    assert callable(dsl_FloatLiteral.__init__)


def test_dsl_floatliteral_constructor_args():
    sig = inspect.signature(dsl_FloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "digits" in params, "Missing parameter 'digits'"

def test_dsl_floatliteral_has_digits():
    assert hasattr(dsl_FloatLiteral, "digits")
    descriptor = None
    for klass in dsl_FloatLiteral.__mro__:
        if "digits" in klass.__dict__:
            descriptor = klass.__dict__["digits"]
            break
    assert isinstance(descriptor, property)



def test_dsl_integerliteral_is_not_abstract():
    assert not inspect.isabstract(dsl_IntegerLiteral)


def test_dsl_integerliteral_constructor_exists():
    assert callable(dsl_IntegerLiteral.__init__)


def test_dsl_integerliteral_constructor_args():
    sig = inspect.signature(dsl_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "one" in params, "Missing parameter 'one'"
    assert "zero" in params, "Missing parameter 'zero'"

def test_dsl_integerliteral_has_one():
    assert hasattr(dsl_IntegerLiteral, "one")
    descriptor = None
    for klass in dsl_IntegerLiteral.__mro__:
        if "one" in klass.__dict__:
            descriptor = klass.__dict__["one"]
            break
    assert isinstance(descriptor, property)

def test_dsl_integerliteral_has_zero():
    assert hasattr(dsl_IntegerLiteral, "zero")
    descriptor = None
    for klass in dsl_IntegerLiteral.__mro__:
        if "zero" in klass.__dict__:
            descriptor = klass.__dict__["zero"]
            break
    assert isinstance(descriptor, property)



def test_dsl_signedintliteral_is_not_abstract():
    assert not inspect.isabstract(dsl_SignedIntLiteral)


def test_dsl_signedintliteral_constructor_exists():
    assert callable(dsl_SignedIntLiteral.__init__)


def test_dsl_signedintliteral_constructor_args():
    sig = inspect.signature(dsl_SignedIntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "bitWidth" in params, "Missing parameter 'bitWidth'"

def test_dsl_signedintliteral_has_bitWidth():
    assert hasattr(dsl_SignedIntLiteral, "bitWidth")
    descriptor = None
    for klass in dsl_SignedIntLiteral.__mro__:
        if "bitWidth" in klass.__dict__:
            descriptor = klass.__dict__["bitWidth"]
            break
    assert isinstance(descriptor, property)



def test_dsl_unsignedintliteral_is_not_abstract():
    assert not inspect.isabstract(dsl_UnsignedIntLiteral)


def test_dsl_unsignedintliteral_constructor_exists():
    assert callable(dsl_UnsignedIntLiteral.__init__)


def test_dsl_unsignedintliteral_constructor_args():
    sig = inspect.signature(dsl_UnsignedIntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"

def test_dsl_unsignedintliteral_has_sign():
    assert hasattr(dsl_UnsignedIntLiteral, "sign")
    descriptor = None
    for klass in dsl_UnsignedIntLiteral.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)



def test_dsl_memberselector_is_not_abstract():
    assert not inspect.isabstract(dsl_MemberSelector)


def test_dsl_memberselector_constructor_exists():
    assert callable(dsl_MemberSelector.__init__)


def test_dsl_memberselector_constructor_args():
    sig = inspect.signature(dsl_MemberSelector.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl_memberselector_has_id():
    assert hasattr(dsl_MemberSelector, "id")
    descriptor = None
    for klass in dsl_MemberSelector.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl_decimalnumber_is_not_abstract():
    assert not inspect.isabstract(dsl_DecimalNumber)


def test_dsl_decimalnumber_constructor_exists():
    assert callable(dsl_DecimalNumber.__init__)


def test_dsl_decimalnumber_constructor_args():
    sig = inspect.signature(dsl_DecimalNumber.__init__)
    params = list(sig.parameters.keys())
    assert "decDigits" in params, "Missing parameter 'decDigits'"
    assert "decDigitsUnderscore" in params, "Missing parameter 'decDigitsUnderscore'"

def test_dsl_decimalnumber_has_decDigits():
    assert hasattr(dsl_DecimalNumber, "decDigits")
    descriptor = None
    for klass in dsl_DecimalNumber.__mro__:
        if "decDigits" in klass.__dict__:
            descriptor = klass.__dict__["decDigits"]
            break
    assert isinstance(descriptor, property)

def test_dsl_decimalnumber_has_decDigitsUnderscore():
    assert hasattr(dsl_DecimalNumber, "decDigitsUnderscore")
    descriptor = None
    for klass in dsl_DecimalNumber.__mro__:
        if "decDigitsUnderscore" in klass.__dict__:
            descriptor = klass.__dict__["decDigitsUnderscore"]
            break
    assert isinstance(descriptor, property)



def test_dsl_primarysuffix_is_not_abstract():
    assert not inspect.isabstract(dsl_PrimarySuffix)


def test_dsl_primarysuffix_constructor_exists():
    assert callable(dsl_PrimarySuffix.__init__)


def test_dsl_primarysuffix_constructor_args():
    sig = inspect.signature(dsl_PrimarySuffix.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "thisOp" in params, "Missing parameter 'thisOp'"

def test_dsl_primarysuffix_has_id():
    assert hasattr(dsl_PrimarySuffix, "id")
    descriptor = None
    for klass in dsl_PrimarySuffix.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_dsl_primarysuffix_has_thisOp():
    assert hasattr(dsl_PrimarySuffix, "thisOp")
    descriptor = None
    for klass in dsl_PrimarySuffix.__mro__:
        if "thisOp" in klass.__dict__:
            descriptor = klass.__dict__["thisOp"]
            break
    assert isinstance(descriptor, property)



def test_dsl_allocationexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_AllocationExpression)


def test_dsl_allocationexpression_constructor_exists():
    assert callable(dsl_AllocationExpression.__init__)


def test_dsl_allocationexpression_constructor_args():
    sig = inspect.signature(dsl_AllocationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "primType" in params, "Missing parameter 'primType'"

def test_dsl_allocationexpression_has_primType():
    assert hasattr(dsl_AllocationExpression, "primType")
    descriptor = None
    for klass in dsl_AllocationExpression.__mro__:
        if "primType" in klass.__dict__:
            descriptor = klass.__dict__["primType"]
            break
    assert isinstance(descriptor, property)



def test_dsl_primaryprefix_is_not_abstract():
    assert not inspect.isabstract(dsl_PrimaryPrefix)


def test_dsl_primaryprefix_constructor_exists():
    assert callable(dsl_PrimaryPrefix.__init__)


def test_dsl_primaryprefix_constructor_args():
    sig = inspect.signature(dsl_PrimaryPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "superOp" in params, "Missing parameter 'superOp'"
    assert "thisOp" in params, "Missing parameter 'thisOp'"

def test_dsl_primaryprefix_has_id():
    assert hasattr(dsl_PrimaryPrefix, "id")
    descriptor = None
    for klass in dsl_PrimaryPrefix.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_dsl_primaryprefix_has_superOp():
    assert hasattr(dsl_PrimaryPrefix, "superOp")
    descriptor = None
    for klass in dsl_PrimaryPrefix.__mro__:
        if "superOp" in klass.__dict__:
            descriptor = klass.__dict__["superOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl_primaryprefix_has_thisOp():
    assert hasattr(dsl_PrimaryPrefix, "thisOp")
    descriptor = None
    for klass in dsl_PrimaryPrefix.__mro__:
        if "thisOp" in klass.__dict__:
            descriptor = klass.__dict__["thisOp"]
            break
    assert isinstance(descriptor, property)



def test_dsl_predecrementexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_PreDecrementExpression)


def test_dsl_predecrementexpression_constructor_exists():
    assert callable(dsl_PreDecrementExpression.__init__)


def test_dsl_predecrementexpression_constructor_args():
    sig = inspect.signature(dsl_PreDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl_preincrementexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_PreIncrementExpression)


def test_dsl_preincrementexpression_constructor_exists():
    assert callable(dsl_PreIncrementExpression.__init__)


def test_dsl_preincrementexpression_constructor_args():
    sig = inspect.signature(dsl_PreIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl_eobject_is_not_abstract():
    assert not inspect.isabstract(dsl_EObject)


def test_dsl_eobject_constructor_exists():
    assert callable(dsl_EObject.__init__)


def test_dsl_eobject_constructor_args():
    sig = inspect.signature(dsl_EObject.__init__)
    params = list(sig.parameters.keys())



def test_dsl_literal_is_not_abstract():
    assert not inspect.isabstract(dsl_Literal)


def test_dsl_literal_constructor_exists():
    assert callable(dsl_Literal.__init__)


def test_dsl_literal_constructor_args():
    sig = inspect.signature(dsl_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "stringLit" in params, "Missing parameter 'stringLit'"
    assert "charLit" in params, "Missing parameter 'charLit'"
    assert "nullLit" in params, "Missing parameter 'nullLit'"

def test_dsl_literal_has_stringLit():
    assert hasattr(dsl_Literal, "stringLit")
    descriptor = None
    for klass in dsl_Literal.__mro__:
        if "stringLit" in klass.__dict__:
            descriptor = klass.__dict__["stringLit"]
            break
    assert isinstance(descriptor, property)

def test_dsl_literal_has_charLit():
    assert hasattr(dsl_Literal, "charLit")
    descriptor = None
    for klass in dsl_Literal.__mro__:
        if "charLit" in klass.__dict__:
            descriptor = klass.__dict__["charLit"]
            break
    assert isinstance(descriptor, property)

def test_dsl_literal_has_nullLit():
    assert hasattr(dsl_Literal, "nullLit")
    descriptor = None
    for klass in dsl_Literal.__mro__:
        if "nullLit" in klass.__dict__:
            descriptor = klass.__dict__["nullLit"]
            break
    assert isinstance(descriptor, property)



def test_dsl_castlookahead_is_not_abstract():
    assert not inspect.isabstract(dsl_CastLookahead)


def test_dsl_castlookahead_constructor_exists():
    assert callable(dsl_CastLookahead.__init__)


def test_dsl_castlookahead_constructor_args():
    sig = inspect.signature(dsl_CastLookahead.__init__)
    params = list(sig.parameters.keys())
    assert "newOp" in params, "Missing parameter 'newOp'"
    assert "id" in params, "Missing parameter 'id'"
    assert "bitNegOp" in params, "Missing parameter 'bitNegOp'"
    assert "openBracket" in params, "Missing parameter 'openBracket'"
    assert "negOp" in params, "Missing parameter 'negOp'"
    assert "thisOp" in params, "Missing parameter 'thisOp'"
    assert "superOp" in params, "Missing parameter 'superOp'"
    assert "primType" in params, "Missing parameter 'primType'"

def test_dsl_castlookahead_has_newOp():
    assert hasattr(dsl_CastLookahead, "newOp")
    descriptor = None
    for klass in dsl_CastLookahead.__mro__:
        if "newOp" in klass.__dict__:
            descriptor = klass.__dict__["newOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl_castlookahead_has_id():
    assert hasattr(dsl_CastLookahead, "id")
    descriptor = None
    for klass in dsl_CastLookahead.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_dsl_castlookahead_has_bitNegOp():
    assert hasattr(dsl_CastLookahead, "bitNegOp")
    descriptor = None
    for klass in dsl_CastLookahead.__mro__:
        if "bitNegOp" in klass.__dict__:
            descriptor = klass.__dict__["bitNegOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl_castlookahead_has_openBracket():
    assert hasattr(dsl_CastLookahead, "openBracket")
    descriptor = None
    for klass in dsl_CastLookahead.__mro__:
        if "openBracket" in klass.__dict__:
            descriptor = klass.__dict__["openBracket"]
            break
    assert isinstance(descriptor, property)

def test_dsl_castlookahead_has_negOp():
    assert hasattr(dsl_CastLookahead, "negOp")
    descriptor = None
    for klass in dsl_CastLookahead.__mro__:
        if "negOp" in klass.__dict__:
            descriptor = klass.__dict__["negOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl_castlookahead_has_thisOp():
    assert hasattr(dsl_CastLookahead, "thisOp")
    descriptor = None
    for klass in dsl_CastLookahead.__mro__:
        if "thisOp" in klass.__dict__:
            descriptor = klass.__dict__["thisOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl_castlookahead_has_superOp():
    assert hasattr(dsl_CastLookahead, "superOp")
    descriptor = None
    for klass in dsl_CastLookahead.__mro__:
        if "superOp" in klass.__dict__:
            descriptor = klass.__dict__["superOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl_castlookahead_has_primType():
    assert hasattr(dsl_CastLookahead, "primType")
    descriptor = None
    for klass in dsl_CastLookahead.__mro__:
        if "primType" in klass.__dict__:
            descriptor = klass.__dict__["primType"]
            break
    assert isinstance(descriptor, property)



def test_dsl_postfixexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_PostfixExpression)


def test_dsl_postfixexpression_constructor_exists():
    assert callable(dsl_PostfixExpression.__init__)


def test_dsl_postfixexpression_constructor_args():
    sig = inspect.signature(dsl_PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_dsl_postfixexpression_has_op():
    assert hasattr(dsl_PostfixExpression, "op")
    descriptor = None
    for klass in dsl_PostfixExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_dsl_castexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_CastExpression)


def test_dsl_castexpression_constructor_exists():
    assert callable(dsl_CastExpression.__init__)


def test_dsl_castexpression_constructor_args():
    sig = inspect.signature(dsl_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl_unaryexpressionnotplusminus_is_not_abstract():
    assert not inspect.isabstract(dsl_UnaryExpressionNotPlusMinus)


def test_dsl_unaryexpressionnotplusminus_constructor_exists():
    assert callable(dsl_UnaryExpressionNotPlusMinus.__init__)


def test_dsl_unaryexpressionnotplusminus_constructor_args():
    sig = inspect.signature(dsl_UnaryExpressionNotPlusMinus.__init__)
    params = list(sig.parameters.keys())
    assert "negOp" in params, "Missing parameter 'negOp'"

def test_dsl_unaryexpressionnotplusminus_has_negOp():
    assert hasattr(dsl_UnaryExpressionNotPlusMinus, "negOp")
    descriptor = None
    for klass in dsl_UnaryExpressionNotPlusMinus.__mro__:
        if "negOp" in klass.__dict__:
            descriptor = klass.__dict__["negOp"]
            break
    assert isinstance(descriptor, property)



def test_dsl_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_UnaryExpression)


def test_dsl_unaryexpression_constructor_exists():
    assert callable(dsl_UnaryExpression.__init__)


def test_dsl_unaryexpression_constructor_args():
    sig = inspect.signature(dsl_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"

def test_dsl_unaryexpression_has_sign():
    assert hasattr(dsl_UnaryExpression, "sign")
    descriptor = None
    for klass in dsl_UnaryExpression.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)



def test_dsl_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_MultiplicativeExpression)


def test_dsl_multiplicativeexpression_constructor_exists():
    assert callable(dsl_MultiplicativeExpression.__init__)


def test_dsl_multiplicativeexpression_constructor_args():
    sig = inspect.signature(dsl_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "ops" in params, "Missing parameter 'ops'"

def test_dsl_multiplicativeexpression_has_ops():
    assert hasattr(dsl_MultiplicativeExpression, "ops")
    descriptor = None
    for klass in dsl_MultiplicativeExpression.__mro__:
        if "ops" in klass.__dict__:
            descriptor = klass.__dict__["ops"]
            break
    assert isinstance(descriptor, property)



def test_dsl_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_AdditiveExpression)


def test_dsl_additiveexpression_constructor_exists():
    assert callable(dsl_AdditiveExpression.__init__)


def test_dsl_additiveexpression_constructor_args():
    sig = inspect.signature(dsl_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "ops" in params, "Missing parameter 'ops'"

def test_dsl_additiveexpression_has_ops():
    assert hasattr(dsl_AdditiveExpression, "ops")
    descriptor = None
    for klass in dsl_AdditiveExpression.__mro__:
        if "ops" in klass.__dict__:
            descriptor = klass.__dict__["ops"]
            break
    assert isinstance(descriptor, property)



def test_dsl_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_ShiftExpression)


def test_dsl_shiftexpression_constructor_exists():
    assert callable(dsl_ShiftExpression.__init__)


def test_dsl_shiftexpression_constructor_args():
    sig = inspect.signature(dsl_ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "ops" in params, "Missing parameter 'ops'"

def test_dsl_shiftexpression_has_ops():
    assert hasattr(dsl_ShiftExpression, "ops")
    descriptor = None
    for klass in dsl_ShiftExpression.__mro__:
        if "ops" in klass.__dict__:
            descriptor = klass.__dict__["ops"]
            break
    assert isinstance(descriptor, property)



def test_dsl_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_RelationalExpression)


def test_dsl_relationalexpression_constructor_exists():
    assert callable(dsl_RelationalExpression.__init__)


def test_dsl_relationalexpression_constructor_args():
    sig = inspect.signature(dsl_RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "ops" in params, "Missing parameter 'ops'"

def test_dsl_relationalexpression_has_ops():
    assert hasattr(dsl_RelationalExpression, "ops")
    descriptor = None
    for klass in dsl_RelationalExpression.__mro__:
        if "ops" in klass.__dict__:
            descriptor = klass.__dict__["ops"]
            break
    assert isinstance(descriptor, property)



def test_dsl_instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_InstanceOfExpression)


def test_dsl_instanceofexpression_constructor_exists():
    assert callable(dsl_InstanceOfExpression.__init__)


def test_dsl_instanceofexpression_constructor_args():
    sig = inspect.signature(dsl_InstanceOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_EqualityExpression)


def test_dsl_equalityexpression_constructor_exists():
    assert callable(dsl_EqualityExpression.__init__)


def test_dsl_equalityexpression_constructor_args():
    sig = inspect.signature(dsl_EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl_andexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_AndExpression)


def test_dsl_andexpression_constructor_exists():
    assert callable(dsl_AndExpression.__init__)


def test_dsl_andexpression_constructor_args():
    sig = inspect.signature(dsl_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl_exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_ExclusiveOrExpression)


def test_dsl_exclusiveorexpression_constructor_exists():
    assert callable(dsl_ExclusiveOrExpression.__init__)


def test_dsl_exclusiveorexpression_constructor_args():
    sig = inspect.signature(dsl_ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl_inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_InclusiveOrExpression)


def test_dsl_inclusiveorexpression_constructor_exists():
    assert callable(dsl_InclusiveOrExpression.__init__)


def test_dsl_inclusiveorexpression_constructor_args():
    sig = inspect.signature(dsl_InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl_conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_ConditionalAndExpression)


def test_dsl_conditionalandexpression_constructor_exists():
    assert callable(dsl_ConditionalAndExpression.__init__)


def test_dsl_conditionalandexpression_constructor_args():
    sig = inspect.signature(dsl_ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_ifstatement_is_not_abstract():
    assert not inspect.isabstract(IfStatement)


def test_ifstatement_constructor_exists():
    assert callable(IfStatement.__init__)


def test_ifstatement_constructor_args():
    sig = inspect.signature(IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_ConditionalOrExpression)


def test_dsl_conditionalorexpression_constructor_exists():
    assert callable(dsl_ConditionalOrExpression.__init__)


def test_dsl_conditionalorexpression_constructor_args():
    sig = inspect.signature(dsl_ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl_statement_is_not_abstract():
    assert not inspect.isabstract(dsl_Statement)


def test_dsl_statement_constructor_exists():
    assert callable(dsl_Statement.__init__)


def test_dsl_statement_constructor_args():
    sig = inspect.signature(dsl_Statement.__init__)
    params = list(sig.parameters.keys())



def test_dsl_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_ConditionalExpression)


def test_dsl_conditionalexpression_constructor_exists():
    assert callable(dsl_ConditionalExpression.__init__)


def test_dsl_conditionalexpression_constructor_args():
    sig = inspect.signature(dsl_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl_wildcardbounds_is_not_abstract():
    assert not inspect.isabstract(dsl_WildcardBounds)


def test_dsl_wildcardbounds_constructor_exists():
    assert callable(dsl_WildcardBounds.__init__)


def test_dsl_wildcardbounds_constructor_args():
    sig = inspect.signature(dsl_WildcardBounds.__init__)
    params = list(sig.parameters.keys())
    assert "ext" in params, "Missing parameter 'ext'"
    assert "sup" in params, "Missing parameter 'sup'"

def test_dsl_wildcardbounds_has_ext():
    assert hasattr(dsl_WildcardBounds, "ext")
    descriptor = None
    for klass in dsl_WildcardBounds.__mro__:
        if "ext" in klass.__dict__:
            descriptor = klass.__dict__["ext"]
            break
    assert isinstance(descriptor, property)

def test_dsl_wildcardbounds_has_sup():
    assert hasattr(dsl_WildcardBounds, "sup")
    descriptor = None
    for klass in dsl_WildcardBounds.__mro__:
        if "sup" in klass.__dict__:
            descriptor = klass.__dict__["sup"]
            break
    assert isinstance(descriptor, property)



def test_dsl_typeargument_is_not_abstract():
    assert not inspect.isabstract(dsl_TypeArgument)


def test_dsl_typeargument_constructor_exists():
    assert callable(dsl_TypeArgument.__init__)


def test_dsl_typeargument_constructor_args():
    sig = inspect.signature(dsl_TypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_dsl_typearguments_is_not_abstract():
    assert not inspect.isabstract(dsl_TypeArguments)


def test_dsl_typearguments_constructor_exists():
    assert callable(dsl_TypeArguments.__init__)


def test_dsl_typearguments_constructor_args():
    sig = inspect.signature(dsl_TypeArguments.__init__)
    params = list(sig.parameters.keys())



def test_dsl_referencetype_is_not_abstract():
    assert not inspect.isabstract(dsl_ReferenceType)


def test_dsl_referencetype_constructor_exists():
    assert callable(dsl_ReferenceType.__init__)


def test_dsl_referencetype_constructor_args():
    sig = inspect.signature(dsl_ReferenceType.__init__)
    params = list(sig.parameters.keys())
    assert "primType" in params, "Missing parameter 'primType'"
    assert "squareBracketsAlpha" in params, "Missing parameter 'squareBracketsAlpha'"
    assert "squareBracketsBeta" in params, "Missing parameter 'squareBracketsBeta'"

def test_dsl_referencetype_has_primType():
    assert hasattr(dsl_ReferenceType, "primType")
    descriptor = None
    for klass in dsl_ReferenceType.__mro__:
        if "primType" in klass.__dict__:
            descriptor = klass.__dict__["primType"]
            break
    assert isinstance(descriptor, property)

def test_dsl_referencetype_has_squareBracketsAlpha():
    assert hasattr(dsl_ReferenceType, "squareBracketsAlpha")
    descriptor = None
    for klass in dsl_ReferenceType.__mro__:
        if "squareBracketsAlpha" in klass.__dict__:
            descriptor = klass.__dict__["squareBracketsAlpha"]
            break
    assert isinstance(descriptor, property)

def test_dsl_referencetype_has_squareBracketsBeta():
    assert hasattr(dsl_ReferenceType, "squareBracketsBeta")
    descriptor = None
    for klass in dsl_ReferenceType.__mro__:
        if "squareBracketsBeta" in klass.__dict__:
            descriptor = klass.__dict__["squareBracketsBeta"]
            break
    assert isinstance(descriptor, property)



def test_dsl_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(dsl_PrimaryExpression)


def test_dsl_primaryexpression_constructor_exists():
    assert callable(dsl_PrimaryExpression.__init__)


def test_dsl_primaryexpression_constructor_args():
    sig = inspect.signature(dsl_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl_variabledeclaratorid_is_not_abstract():
    assert not inspect.isabstract(dsl_VariableDeclaratorId)


def test_dsl_variabledeclaratorid_constructor_exists():
    assert callable(dsl_VariableDeclaratorId.__init__)


def test_dsl_variabledeclaratorid_constructor_args():
    sig = inspect.signature(dsl_VariableDeclaratorId.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "squareBrackets" in params, "Missing parameter 'squareBrackets'"

def test_dsl_variabledeclaratorid_has_id():
    assert hasattr(dsl_VariableDeclaratorId, "id")
    descriptor = None
    for klass in dsl_VariableDeclaratorId.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_dsl_variabledeclaratorid_has_squareBrackets():
    assert hasattr(dsl_VariableDeclaratorId, "squareBrackets")
    descriptor = None
    for klass in dsl_VariableDeclaratorId.__mro__:
        if "squareBrackets" in klass.__dict__:
            descriptor = klass.__dict__["squareBrackets"]
            break
    assert isinstance(descriptor, property)



def test_dsl_variabledeclarator_is_not_abstract():
    assert not inspect.isabstract(dsl_VariableDeclarator)


def test_dsl_variabledeclarator_constructor_exists():
    assert callable(dsl_VariableDeclarator.__init__)


def test_dsl_variabledeclarator_constructor_args():
    sig = inspect.signature(dsl_VariableDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_dsl_formalparameter_is_not_abstract():
    assert not inspect.isabstract(dsl_FormalParameter)


def test_dsl_formalparameter_constructor_exists():
    assert callable(dsl_FormalParameter.__init__)


def test_dsl_formalparameter_constructor_args():
    sig = inspect.signature(dsl_FormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"

def test_dsl_formalparameter_has_final():
    assert hasattr(dsl_FormalParameter, "final")
    descriptor = None
    for klass in dsl_FormalParameter.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_dsl_block_is_not_abstract():
    assert not inspect.isabstract(dsl_Block)


def test_dsl_block_constructor_exists():
    assert callable(dsl_Block.__init__)


def test_dsl_block_constructor_args():
    sig = inspect.signature(dsl_Block.__init__)
    params = list(sig.parameters.keys())



def test_dsl_methoddeclarator_is_not_abstract():
    assert not inspect.isabstract(dsl_MethodDeclarator)


def test_dsl_methoddeclarator_constructor_exists():
    assert callable(dsl_MethodDeclarator.__init__)


def test_dsl_methoddeclarator_constructor_args():
    sig = inspect.signature(dsl_MethodDeclarator.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "squareBrackets" in params, "Missing parameter 'squareBrackets'"

def test_dsl_methoddeclarator_has_id():
    assert hasattr(dsl_MethodDeclarator, "id")
    descriptor = None
    for klass in dsl_MethodDeclarator.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_dsl_methoddeclarator_has_squareBrackets():
    assert hasattr(dsl_MethodDeclarator, "squareBrackets")
    descriptor = None
    for klass in dsl_MethodDeclarator.__mro__:
        if "squareBrackets" in klass.__dict__:
            descriptor = klass.__dict__["squareBrackets"]
            break
    assert isinstance(descriptor, property)



def test_dsl_resulttype_is_not_abstract():
    assert not inspect.isabstract(dsl_ResultType)


def test_dsl_resulttype_constructor_exists():
    assert callable(dsl_ResultType.__init__)


def test_dsl_resulttype_constructor_args():
    sig = inspect.signature(dsl_ResultType.__init__)
    params = list(sig.parameters.keys())



def test_dsl_blockstatement_is_not_abstract():
    assert not inspect.isabstract(dsl_BlockStatement)


def test_dsl_blockstatement_constructor_exists():
    assert callable(dsl_BlockStatement.__init__)


def test_dsl_blockstatement_constructor_args():
    sig = inspect.signature(dsl_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl_explicitconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(dsl_ExplicitConstructorInvocation)


def test_dsl_explicitconstructorinvocation_constructor_exists():
    assert callable(dsl_ExplicitConstructorInvocation.__init__)


def test_dsl_explicitconstructorinvocation_constructor_args():
    sig = inspect.signature(dsl_ExplicitConstructorInvocation.__init__)
    params = list(sig.parameters.keys())
    assert "parent" in params, "Missing parameter 'parent'"
    assert "self" in params, "Missing parameter 'self'"

def test_dsl_explicitconstructorinvocation_has_parent():
    assert hasattr(dsl_ExplicitConstructorInvocation, "parent")
    descriptor = None
    for klass in dsl_ExplicitConstructorInvocation.__mro__:
        if "parent" in klass.__dict__:
            descriptor = klass.__dict__["parent"]
            break
    assert isinstance(descriptor, property)

def test_dsl_explicitconstructorinvocation_has_self():
    assert hasattr(dsl_ExplicitConstructorInvocation, "self")
    descriptor = None
    for klass in dsl_ExplicitConstructorInvocation.__mro__:
        if "self" in klass.__dict__:
            descriptor = klass.__dict__["self"]
            break
    assert isinstance(descriptor, property)



def test_dsl_namelist_is_not_abstract():
    assert not inspect.isabstract(dsl_NameList)


def test_dsl_namelist_constructor_exists():
    assert callable(dsl_NameList.__init__)


def test_dsl_namelist_constructor_args():
    sig = inspect.signature(dsl_NameList.__init__)
    params = list(sig.parameters.keys())



def test_dsl_formalparameters_is_not_abstract():
    assert not inspect.isabstract(dsl_FormalParameters)


def test_dsl_formalparameters_constructor_exists():
    assert callable(dsl_FormalParameters.__init__)


def test_dsl_formalparameters_constructor_args():
    sig = inspect.signature(dsl_FormalParameters.__init__)
    params = list(sig.parameters.keys())



def test_dsl_expression_is_not_abstract():
    assert not inspect.isabstract(dsl_Expression)


def test_dsl_expression_constructor_exists():
    assert callable(dsl_Expression.__init__)


def test_dsl_expression_constructor_args():
    sig = inspect.signature(dsl_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "assignOp" in params, "Missing parameter 'assignOp'"

def test_dsl_expression_has_assignOp():
    assert hasattr(dsl_Expression, "assignOp")
    descriptor = None
    for klass in dsl_Expression.__mro__:
        if "assignOp" in klass.__dict__:
            descriptor = klass.__dict__["assignOp"]
            break
    assert isinstance(descriptor, property)



def test_dsl_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(dsl_ArrayInitializer)


def test_dsl_arrayinitializer_constructor_exists():
    assert callable(dsl_ArrayInitializer.__init__)


def test_dsl_arrayinitializer_constructor_args():
    sig = inspect.signature(dsl_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_dsl_variableinitializer_is_not_abstract():
    assert not inspect.isabstract(dsl_VariableInitializer)


def test_dsl_variableinitializer_constructor_exists():
    assert callable(dsl_VariableInitializer.__init__)


def test_dsl_variableinitializer_constructor_args():
    sig = inspect.signature(dsl_VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_dsl_type_is_not_abstract():
    assert not inspect.isabstract(dsl_Type)


def test_dsl_type_constructor_exists():
    assert callable(dsl_Type.__init__)


def test_dsl_type_constructor_args():
    sig = inspect.signature(dsl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "primType" in params, "Missing parameter 'primType'"

def test_dsl_type_has_primType():
    assert hasattr(dsl_Type, "primType")
    descriptor = None
    for klass in dsl_Type.__mro__:
        if "primType" in klass.__dict__:
            descriptor = klass.__dict__["primType"]
            break
    assert isinstance(descriptor, property)



def test_dsl_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl_FieldDeclaration)


def test_dsl_fielddeclaration_constructor_exists():
    assert callable(dsl_FieldDeclaration.__init__)


def test_dsl_fielddeclaration_constructor_args():
    sig = inspect.signature(dsl_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dsl_methodorctordeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl_MethodOrCtorDeclaration)


def test_dsl_methodorctordeclaration_constructor_exists():
    assert callable(dsl_MethodOrCtorDeclaration.__init__)


def test_dsl_methodorctordeclaration_constructor_args():
    sig = inspect.signature(dsl_MethodOrCtorDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl_methodorctordeclaration_has_id():
    assert hasattr(dsl_MethodOrCtorDeclaration, "id")
    descriptor = None
    for klass in dsl_MethodOrCtorDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl_initializer_is_not_abstract():
    assert not inspect.isabstract(dsl_Initializer)


def test_dsl_initializer_constructor_exists():
    assert callable(dsl_Initializer.__init__)


def test_dsl_initializer_constructor_args():
    sig = inspect.signature(dsl_Initializer.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_dsl_initializer_has_static():
    assert hasattr(dsl_Initializer, "static")
    descriptor = None
    for klass in dsl_Initializer.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_dsl_typebound_is_not_abstract():
    assert not inspect.isabstract(dsl_TypeBound)


def test_dsl_typebound_constructor_exists():
    assert callable(dsl_TypeBound.__init__)


def test_dsl_typebound_constructor_args():
    sig = inspect.signature(dsl_TypeBound.__init__)
    params = list(sig.parameters.keys())



def test_dsl_typeparameter_is_not_abstract():
    assert not inspect.isabstract(dsl_TypeParameter)


def test_dsl_typeparameter_constructor_exists():
    assert callable(dsl_TypeParameter.__init__)


def test_dsl_typeparameter_constructor_args():
    sig = inspect.signature(dsl_TypeParameter.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl_typeparameter_has_id():
    assert hasattr(dsl_TypeParameter, "id")
    descriptor = None
    for klass in dsl_TypeParameter.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl_arguments_is_not_abstract():
    assert not inspect.isabstract(dsl_Arguments)


def test_dsl_arguments_constructor_exists():
    assert callable(dsl_Arguments.__init__)


def test_dsl_arguments_constructor_args():
    sig = inspect.signature(dsl_Arguments.__init__)
    params = list(sig.parameters.keys())



def test_dsl_classorinterfacebodydeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl_ClassOrInterfaceBodyDeclaration)


def test_dsl_classorinterfacebodydeclaration_constructor_exists():
    assert callable(dsl_ClassOrInterfaceBodyDeclaration.__init__)


def test_dsl_classorinterfacebodydeclaration_constructor_args():
    sig = inspect.signature(dsl_ClassOrInterfaceBodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dsl_enumconstant_is_not_abstract():
    assert not inspect.isabstract(dsl_EnumConstant)


def test_dsl_enumconstant_constructor_exists():
    assert callable(dsl_EnumConstant.__init__)


def test_dsl_enumconstant_constructor_args():
    sig = inspect.signature(dsl_EnumConstant.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl_enumconstant_has_id():
    assert hasattr(dsl_EnumConstant, "id")
    descriptor = None
    for klass in dsl_EnumConstant.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl_enumbody_is_not_abstract():
    assert not inspect.isabstract(dsl_EnumBody)


def test_dsl_enumbody_constructor_exists():
    assert callable(dsl_EnumBody.__init__)


def test_dsl_enumbody_constructor_args():
    sig = inspect.signature(dsl_EnumBody.__init__)
    params = list(sig.parameters.keys())



def test_dsl_classorinterfacetype_is_not_abstract():
    assert not inspect.isabstract(dsl_ClassOrInterfaceType)


def test_dsl_classorinterfacetype_constructor_exists():
    assert callable(dsl_ClassOrInterfaceType.__init__)


def test_dsl_classorinterfacetype_constructor_args():
    sig = inspect.signature(dsl_ClassOrInterfaceType.__init__)
    params = list(sig.parameters.keys())
    assert "ids" in params, "Missing parameter 'ids'"

def test_dsl_classorinterfacetype_has_ids():
    assert hasattr(dsl_ClassOrInterfaceType, "ids")
    descriptor = None
    for klass in dsl_ClassOrInterfaceType.__mro__:
        if "ids" in klass.__dict__:
            descriptor = klass.__dict__["ids"]
            break
    assert isinstance(descriptor, property)



def test_dsl_classorinterfacebody_is_not_abstract():
    assert not inspect.isabstract(dsl_ClassOrInterfaceBody)


def test_dsl_classorinterfacebody_constructor_exists():
    assert callable(dsl_ClassOrInterfaceBody.__init__)


def test_dsl_classorinterfacebody_constructor_args():
    sig = inspect.signature(dsl_ClassOrInterfaceBody.__init__)
    params = list(sig.parameters.keys())



def test_dsl_implementslist_is_not_abstract():
    assert not inspect.isabstract(dsl_ImplementsList)


def test_dsl_implementslist_constructor_exists():
    assert callable(dsl_ImplementsList.__init__)


def test_dsl_implementslist_constructor_args():
    sig = inspect.signature(dsl_ImplementsList.__init__)
    params = list(sig.parameters.keys())



def test_dsl_extendslist_is_not_abstract():
    assert not inspect.isabstract(dsl_ExtendsList)


def test_dsl_extendslist_constructor_exists():
    assert callable(dsl_ExtendsList.__init__)


def test_dsl_extendslist_constructor_args():
    sig = inspect.signature(dsl_ExtendsList.__init__)
    params = list(sig.parameters.keys())



def test_dsl_typeparameters_is_not_abstract():
    assert not inspect.isabstract(dsl_TypeParameters)


def test_dsl_typeparameters_constructor_exists():
    assert callable(dsl_TypeParameters.__init__)


def test_dsl_typeparameters_constructor_args():
    sig = inspect.signature(dsl_TypeParameters.__init__)
    params = list(sig.parameters.keys())



def test_dsl_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl_AnnotationTypeDeclaration)


def test_dsl_annotationtypedeclaration_constructor_exists():
    assert callable(dsl_AnnotationTypeDeclaration.__init__)


def test_dsl_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(dsl_AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl_annotationtypedeclaration_has_id():
    assert hasattr(dsl_AnnotationTypeDeclaration, "id")
    descriptor = None
    for klass in dsl_AnnotationTypeDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl_EnumDeclaration)


def test_dsl_enumdeclaration_constructor_exists():
    assert callable(dsl_EnumDeclaration.__init__)


def test_dsl_enumdeclaration_constructor_args():
    sig = inspect.signature(dsl_EnumDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl_enumdeclaration_has_id():
    assert hasattr(dsl_EnumDeclaration, "id")
    descriptor = None
    for klass in dsl_EnumDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl_classorinterfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl_ClassOrInterfaceDeclaration)


def test_dsl_classorinterfacedeclaration_constructor_exists():
    assert callable(dsl_ClassOrInterfaceDeclaration.__init__)


def test_dsl_classorinterfacedeclaration_constructor_args():
    sig = inspect.signature(dsl_ClassOrInterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "typeCategory" in params, "Missing parameter 'typeCategory'"

def test_dsl_classorinterfacedeclaration_has_id():
    assert hasattr(dsl_ClassOrInterfaceDeclaration, "id")
    descriptor = None
    for klass in dsl_ClassOrInterfaceDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_dsl_classorinterfacedeclaration_has_typeCategory():
    assert hasattr(dsl_ClassOrInterfaceDeclaration, "typeCategory")
    descriptor = None
    for klass in dsl_ClassOrInterfaceDeclaration.__mro__:
        if "typeCategory" in klass.__dict__:
            descriptor = klass.__dict__["typeCategory"]
            break
    assert isinstance(descriptor, property)



def test_dsl_typebodymodifier_is_not_abstract():
    assert not inspect.isabstract(dsl_TypeBodyModifier)


def test_dsl_typebodymodifier_constructor_exists():
    assert callable(dsl_TypeBodyModifier.__init__)


def test_dsl_typebodymodifier_constructor_args():
    sig = inspect.signature(dsl_TypeBodyModifier.__init__)
    params = list(sig.parameters.keys())
    assert "transient" in params, "Missing parameter 'transient'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "native" in params, "Missing parameter 'native'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"

def test_dsl_typebodymodifier_has_transient():
    assert hasattr(dsl_TypeBodyModifier, "transient")
    descriptor = None
    for klass in dsl_TypeBodyModifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_dsl_typebodymodifier_has_volatile():
    assert hasattr(dsl_TypeBodyModifier, "volatile")
    descriptor = None
    for klass in dsl_TypeBodyModifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_dsl_typebodymodifier_has_synchronized():
    assert hasattr(dsl_TypeBodyModifier, "synchronized")
    descriptor = None
    for klass in dsl_TypeBodyModifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_dsl_typebodymodifier_has_native():
    assert hasattr(dsl_TypeBodyModifier, "native")
    descriptor = None
    for klass in dsl_TypeBodyModifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)

def test_dsl_typebodymodifier_has_strictfp():
    assert hasattr(dsl_TypeBodyModifier, "strictfp")
    descriptor = None
    for klass in dsl_TypeBodyModifier.__mro__:
        if "strictfp" in klass.__dict__:
            descriptor = klass.__dict__["strictfp"]
            break
    assert isinstance(descriptor, property)



def test_dsl_commonmodifier_is_not_abstract():
    assert not inspect.isabstract(dsl_CommonModifier)


def test_dsl_commonmodifier_constructor_exists():
    assert callable(dsl_CommonModifier.__init__)


def test_dsl_commonmodifier_constructor_args():
    sig = inspect.signature(dsl_CommonModifier.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "final" in params, "Missing parameter 'final'"
    assert "static" in params, "Missing parameter 'static'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_dsl_commonmodifier_has_visibility():
    assert hasattr(dsl_CommonModifier, "visibility")
    descriptor = None
    for klass in dsl_CommonModifier.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_dsl_commonmodifier_has_final():
    assert hasattr(dsl_CommonModifier, "final")
    descriptor = None
    for klass in dsl_CommonModifier.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_dsl_commonmodifier_has_static():
    assert hasattr(dsl_CommonModifier, "static")
    descriptor = None
    for klass in dsl_CommonModifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_dsl_commonmodifier_has_abstract():
    assert hasattr(dsl_CommonModifier, "abstract")
    descriptor = None
    for klass in dsl_CommonModifier.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_dsl_name_is_not_abstract():
    assert not inspect.isabstract(dsl_Name)


def test_dsl_name_constructor_exists():
    assert callable(dsl_Name.__init__)


def test_dsl_name_constructor_args():
    sig = inspect.signature(dsl_Name.__init__)
    params = list(sig.parameters.keys())
    assert "ids" in params, "Missing parameter 'ids'"

def test_dsl_name_has_ids():
    assert hasattr(dsl_Name, "ids")
    descriptor = None
    for klass in dsl_Name.__mro__:
        if "ids" in klass.__dict__:
            descriptor = klass.__dict__["ids"]
            break
    assert isinstance(descriptor, property)



def test_dsl_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl_TypeDeclaration)


def test_dsl_typedeclaration_constructor_exists():
    assert callable(dsl_TypeDeclaration.__init__)


def test_dsl_typedeclaration_constructor_args():
    sig = inspect.signature(dsl_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dsl_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl_ImportDeclaration)


def test_dsl_importdeclaration_constructor_exists():
    assert callable(dsl_ImportDeclaration.__init__)


def test_dsl_importdeclaration_constructor_args():
    sig = inspect.signature(dsl_ImportDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dsl_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl_PackageDeclaration)


def test_dsl_packagedeclaration_constructor_exists():
    assert callable(dsl_PackageDeclaration.__init__)


def test_dsl_packagedeclaration_constructor_args():
    sig = inspect.signature(dsl_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dsl_compilationunit_is_not_abstract():
    assert not inspect.isabstract(dsl_CompilationUnit)


def test_dsl_compilationunit_constructor_exists():
    assert callable(dsl_CompilationUnit.__init__)


def test_dsl_compilationunit_constructor_args():
    sig = inspect.signature(dsl_CompilationUnit.__init__)
    params = list(sig.parameters.keys())

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "PRIVATE",
        "PROTECTED",
        "PUBLIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"


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
dsl_DefaultValue_strategy = st.builds(
    dsl_DefaultValue,
)
dsl_AnnotationTypeMemberDeclaration_strategy = st.builds(
    dsl_AnnotationTypeMemberDeclaration,
    id=
        safe_text
)
dsl_AnnotationTypeBody_strategy = st.builds(
    dsl_AnnotationTypeBody,
)
dsl_MemberValueArrayInitializer_strategy = st.builds(
    dsl_MemberValueArrayInitializer,
)
DefaultValue_strategy = st.builds(
    DefaultValue,
)
dsl_MemberValuePair_strategy = st.builds(
    dsl_MemberValuePair,
    id=
        safe_text
)
dsl_MemberValue_strategy = st.builds(
    dsl_MemberValue,
)
dsl_MemberValuePairs_strategy = st.builds(
    dsl_MemberValuePairs,
)
dsl_Annotation_strategy = st.builds(
    dsl_Annotation,
)
dsl_StatementExpressionList_strategy = st.builds(
    dsl_StatementExpressionList,
)
dsl_ForUpdate_strategy = st.builds(
    dsl_ForUpdate,
)
dsl_ForInit_strategy = st.builds(
    dsl_ForInit,
)
dsl_SwitchLabel_strategy = st.builds(
    dsl_SwitchLabel,
    defaultOp=
        safe_text
)
dsl_LocalVariableDeclaration_strategy = st.builds(
    dsl_LocalVariableDeclaration,
    finality=
        safe_text
)
dsl_TryStatement_strategy = st.builds(
    dsl_TryStatement,
)
dsl_SynchronizedStatement_strategy = st.builds(
    dsl_SynchronizedStatement,
)
dsl_ThrowStatement_strategy = st.builds(
    dsl_ThrowStatement,
)
dsl_ReturnStatement_strategy = st.builds(
    dsl_ReturnStatement,
)
dsl_ContinueStatement_strategy = st.builds(
    dsl_ContinueStatement,
    id=
        safe_text
)
dsl_BreakStatement_strategy = st.builds(
    dsl_BreakStatement,
    id=
        safe_text
)
dsl_ForStatement_strategy = st.builds(
    dsl_ForStatement,
    id=
        safe_text
)
dsl_DoStatement_strategy = st.builds(
    dsl_DoStatement,
)
dsl_WhileStatement_strategy = st.builds(
    dsl_WhileStatement,
)
dsl_IfStatement_strategy = st.builds(
    dsl_IfStatement,
)
dsl_SwitchStatement_strategy = st.builds(
    dsl_SwitchStatement,
)
dsl_StatementExpression_strategy = st.builds(
    dsl_StatementExpression,
    minOp=
        safe_text,
    plusOp=
        safe_text,
    assignOp=
        safe_text
)
dsl_AssertStatement_strategy = st.builds(
    dsl_AssertStatement,
)
dsl_LabeledStatement_strategy = st.builds(
    dsl_LabeledStatement,
    id=
        safe_text
)
dsl_ArrayDimsAndInits_strategy = st.builds(
    dsl_ArrayDimsAndInits,
    squareBrackets=
        safe_text
)
dsl_BaseLiteral_strategy = st.builds(
    dsl_BaseLiteral,
    hexDigitsUnderscore=
        safe_text,
    decDigitsUnderscore=
        safe_text,
    binDigitsUnderscore=
        safe_text
)
dsl_ArgumentList_strategy = st.builds(
    dsl_ArgumentList,
)
dsl_BooleanLiteral_strategy = st.builds(
    dsl_BooleanLiteral,
    truthiness=
        safe_text
)
dsl_FloatLiteral_strategy = st.builds(
    dsl_FloatLiteral,
    digits=
        safe_text
)
dsl_IntegerLiteral_strategy = st.builds(
    dsl_IntegerLiteral,
    one=
        safe_text,
    zero=
        safe_text
)
dsl_SignedIntLiteral_strategy = st.builds(
    dsl_SignedIntLiteral,
    bitWidth=
        st.integers()
)
dsl_UnsignedIntLiteral_strategy = st.builds(
    dsl_UnsignedIntLiteral,
    sign=
        safe_text
)
dsl_MemberSelector_strategy = st.builds(
    dsl_MemberSelector,
    id=
        safe_text
)
dsl_DecimalNumber_strategy = st.builds(
    dsl_DecimalNumber,
    decDigits=
        st.integers(),
    decDigitsUnderscore=
        safe_text
)
dsl_PrimarySuffix_strategy = st.builds(
    dsl_PrimarySuffix,
    id=
        safe_text,
    thisOp=
        st.booleans()
)
dsl_AllocationExpression_strategy = st.builds(
    dsl_AllocationExpression,
    primType=
        safe_text
)
dsl_PrimaryPrefix_strategy = st.builds(
    dsl_PrimaryPrefix,
    id=
        safe_text,
    superOp=
        safe_text,
    thisOp=
        safe_text
)
dsl_PreDecrementExpression_strategy = st.builds(
    dsl_PreDecrementExpression,
)
dsl_PreIncrementExpression_strategy = st.builds(
    dsl_PreIncrementExpression,
)
dsl_EObject_strategy = st.builds(
    dsl_EObject,
)
dsl_Literal_strategy = st.builds(
    dsl_Literal,
    stringLit=
        safe_text,
    charLit=
        safe_text,
    nullLit=
        safe_text
)
dsl_CastLookahead_strategy = st.builds(
    dsl_CastLookahead,
    newOp=
        safe_text,
    id=
        safe_text,
    bitNegOp=
        safe_text,
    openBracket=
        safe_text,
    negOp=
        safe_text,
    thisOp=
        safe_text,
    superOp=
        safe_text,
    primType=
        safe_text
)
dsl_PostfixExpression_strategy = st.builds(
    dsl_PostfixExpression,
    op=
        safe_text
)
dsl_CastExpression_strategy = st.builds(
    dsl_CastExpression,
)
dsl_UnaryExpressionNotPlusMinus_strategy = st.builds(
    dsl_UnaryExpressionNotPlusMinus,
    negOp=
        safe_text
)
dsl_UnaryExpression_strategy = st.builds(
    dsl_UnaryExpression,
    sign=
        safe_text
)
dsl_MultiplicativeExpression_strategy = st.builds(
    dsl_MultiplicativeExpression,
    ops=
        safe_text
)
dsl_AdditiveExpression_strategy = st.builds(
    dsl_AdditiveExpression,
    ops=
        safe_text
)
dsl_ShiftExpression_strategy = st.builds(
    dsl_ShiftExpression,
    ops=
        safe_text
)
dsl_RelationalExpression_strategy = st.builds(
    dsl_RelationalExpression,
    ops=
        safe_text
)
dsl_InstanceOfExpression_strategy = st.builds(
    dsl_InstanceOfExpression,
)
dsl_EqualityExpression_strategy = st.builds(
    dsl_EqualityExpression,
)
dsl_AndExpression_strategy = st.builds(
    dsl_AndExpression,
)
dsl_ExclusiveOrExpression_strategy = st.builds(
    dsl_ExclusiveOrExpression,
)
dsl_InclusiveOrExpression_strategy = st.builds(
    dsl_InclusiveOrExpression,
)
dsl_ConditionalAndExpression_strategy = st.builds(
    dsl_ConditionalAndExpression,
)
IfStatement_strategy = st.builds(
    IfStatement,
)
dsl_ConditionalOrExpression_strategy = st.builds(
    dsl_ConditionalOrExpression,
)
dsl_Statement_strategy = st.builds(
    dsl_Statement,
)
dsl_ConditionalExpression_strategy = st.builds(
    dsl_ConditionalExpression,
)
dsl_WildcardBounds_strategy = st.builds(
    dsl_WildcardBounds,
    ext=
        st.booleans(),
    sup=
        st.booleans()
)
dsl_TypeArgument_strategy = st.builds(
    dsl_TypeArgument,
)
dsl_TypeArguments_strategy = st.builds(
    dsl_TypeArguments,
)
dsl_ReferenceType_strategy = st.builds(
    dsl_ReferenceType,
    primType=
        safe_text,
    squareBracketsAlpha=
        safe_text,
    squareBracketsBeta=
        safe_text
)
dsl_PrimaryExpression_strategy = st.builds(
    dsl_PrimaryExpression,
)
dsl_VariableDeclaratorId_strategy = st.builds(
    dsl_VariableDeclaratorId,
    id=
        safe_text,
    squareBrackets=
        safe_text
)
dsl_VariableDeclarator_strategy = st.builds(
    dsl_VariableDeclarator,
)
dsl_FormalParameter_strategy = st.builds(
    dsl_FormalParameter,
    final=
        st.booleans()
)
dsl_Block_strategy = st.builds(
    dsl_Block,
)
dsl_MethodDeclarator_strategy = st.builds(
    dsl_MethodDeclarator,
    id=
        safe_text,
    squareBrackets=
        safe_text
)
dsl_ResultType_strategy = st.builds(
    dsl_ResultType,
)
dsl_BlockStatement_strategy = st.builds(
    dsl_BlockStatement,
)
dsl_ExplicitConstructorInvocation_strategy = st.builds(
    dsl_ExplicitConstructorInvocation,
    parent=
        safe_text,
    self=
        st.booleans()
)
dsl_NameList_strategy = st.builds(
    dsl_NameList,
)
dsl_FormalParameters_strategy = st.builds(
    dsl_FormalParameters,
)
dsl_Expression_strategy = st.builds(
    dsl_Expression,
    assignOp=
        safe_text
)
dsl_ArrayInitializer_strategy = st.builds(
    dsl_ArrayInitializer,
)
dsl_VariableInitializer_strategy = st.builds(
    dsl_VariableInitializer,
)
dsl_Type_strategy = st.builds(
    dsl_Type,
    primType=
        safe_text
)
dsl_FieldDeclaration_strategy = st.builds(
    dsl_FieldDeclaration,
)
dsl_MethodOrCtorDeclaration_strategy = st.builds(
    dsl_MethodOrCtorDeclaration,
    id=
        safe_text
)
dsl_Initializer_strategy = st.builds(
    dsl_Initializer,
    static=
        st.booleans()
)
dsl_TypeBound_strategy = st.builds(
    dsl_TypeBound,
)
dsl_TypeParameter_strategy = st.builds(
    dsl_TypeParameter,
    id=
        safe_text
)
dsl_Arguments_strategy = st.builds(
    dsl_Arguments,
)
dsl_ClassOrInterfaceBodyDeclaration_strategy = st.builds(
    dsl_ClassOrInterfaceBodyDeclaration,
)
dsl_EnumConstant_strategy = st.builds(
    dsl_EnumConstant,
    id=
        safe_text
)
dsl_EnumBody_strategy = st.builds(
    dsl_EnumBody,
)
dsl_ClassOrInterfaceType_strategy = st.builds(
    dsl_ClassOrInterfaceType,
    ids=
        safe_text
)
dsl_ClassOrInterfaceBody_strategy = st.builds(
    dsl_ClassOrInterfaceBody,
)
dsl_ImplementsList_strategy = st.builds(
    dsl_ImplementsList,
)
dsl_ExtendsList_strategy = st.builds(
    dsl_ExtendsList,
)
dsl_TypeParameters_strategy = st.builds(
    dsl_TypeParameters,
)
dsl_AnnotationTypeDeclaration_strategy = st.builds(
    dsl_AnnotationTypeDeclaration,
    id=
        safe_text
)
dsl_EnumDeclaration_strategy = st.builds(
    dsl_EnumDeclaration,
    id=
        safe_text
)
dsl_ClassOrInterfaceDeclaration_strategy = st.builds(
    dsl_ClassOrInterfaceDeclaration,
    id=
        safe_text,
    typeCategory=
        safe_text
)
dsl_TypeBodyModifier_strategy = st.builds(
    dsl_TypeBodyModifier,
    transient=
        st.booleans(),
    volatile=
        st.booleans(),
    synchronized=
        st.booleans(),
    native=
        st.booleans(),
    strictfp=
        st.booleans()
)
dsl_CommonModifier_strategy = st.builds(
    dsl_CommonModifier,
    visibility=
        safe_text,
    final=
        st.booleans(),
    static=
        st.booleans(),
    abstract=
        st.booleans()
)
dsl_Name_strategy = st.builds(
    dsl_Name,
    ids=
        safe_text
)
dsl_TypeDeclaration_strategy = st.builds(
    dsl_TypeDeclaration,
)
dsl_ImportDeclaration_strategy = st.builds(
    dsl_ImportDeclaration,
)
dsl_PackageDeclaration_strategy = st.builds(
    dsl_PackageDeclaration,
)
dsl_CompilationUnit_strategy = st.builds(
    dsl_CompilationUnit,
)

@given(instance=dsl_DefaultValue_strategy)
@settings(max_examples=50)
def test_dsl_defaultvalue_instantiation(instance):
    assert isinstance(instance, dsl_DefaultValue)

@given(instance=dsl_AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_dsl_annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, dsl_AnnotationTypeMemberDeclaration)



@given(instance=dsl_AnnotationTypeMemberDeclaration_strategy)
def test_dsl_annotationtypememberdeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl_AnnotationTypeBody_strategy)
@settings(max_examples=50)
def test_dsl_annotationtypebody_instantiation(instance):
    assert isinstance(instance, dsl_AnnotationTypeBody)

@given(instance=dsl_MemberValueArrayInitializer_strategy)
@settings(max_examples=50)
def test_dsl_membervaluearrayinitializer_instantiation(instance):
    assert isinstance(instance, dsl_MemberValueArrayInitializer)

@given(instance=DefaultValue_strategy)
@settings(max_examples=50)
def test_defaultvalue_instantiation(instance):
    assert isinstance(instance, DefaultValue)

@given(instance=dsl_MemberValuePair_strategy)
@settings(max_examples=50)
def test_dsl_membervaluepair_instantiation(instance):
    assert isinstance(instance, dsl_MemberValuePair)



@given(instance=dsl_MemberValuePair_strategy)
def test_dsl_membervaluepair_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl_MemberValue_strategy)
@settings(max_examples=50)
def test_dsl_membervalue_instantiation(instance):
    assert isinstance(instance, dsl_MemberValue)

@given(instance=dsl_MemberValuePairs_strategy)
@settings(max_examples=50)
def test_dsl_membervaluepairs_instantiation(instance):
    assert isinstance(instance, dsl_MemberValuePairs)

@given(instance=dsl_Annotation_strategy)
@settings(max_examples=50)
def test_dsl_annotation_instantiation(instance):
    assert isinstance(instance, dsl_Annotation)

@given(instance=dsl_StatementExpressionList_strategy)
@settings(max_examples=50)
def test_dsl_statementexpressionlist_instantiation(instance):
    assert isinstance(instance, dsl_StatementExpressionList)

@given(instance=dsl_ForUpdate_strategy)
@settings(max_examples=50)
def test_dsl_forupdate_instantiation(instance):
    assert isinstance(instance, dsl_ForUpdate)

@given(instance=dsl_ForInit_strategy)
@settings(max_examples=50)
def test_dsl_forinit_instantiation(instance):
    assert isinstance(instance, dsl_ForInit)

@given(instance=dsl_SwitchLabel_strategy)
@settings(max_examples=50)
def test_dsl_switchlabel_instantiation(instance):
    assert isinstance(instance, dsl_SwitchLabel)



@given(instance=dsl_SwitchLabel_strategy)
def test_dsl_switchlabel_defaultOp_setter(instance):
    original = instance.defaultOp
    instance.defaultOp = original
    assert instance.defaultOp == original

@given(instance=dsl_LocalVariableDeclaration_strategy)
@settings(max_examples=50)
def test_dsl_localvariabledeclaration_instantiation(instance):
    assert isinstance(instance, dsl_LocalVariableDeclaration)



@given(instance=dsl_LocalVariableDeclaration_strategy)
def test_dsl_localvariabledeclaration_finality_setter(instance):
    original = instance.finality
    instance.finality = original
    assert instance.finality == original

@given(instance=dsl_TryStatement_strategy)
@settings(max_examples=50)
def test_dsl_trystatement_instantiation(instance):
    assert isinstance(instance, dsl_TryStatement)

@given(instance=dsl_SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_dsl_synchronizedstatement_instantiation(instance):
    assert isinstance(instance, dsl_SynchronizedStatement)

@given(instance=dsl_ThrowStatement_strategy)
@settings(max_examples=50)
def test_dsl_throwstatement_instantiation(instance):
    assert isinstance(instance, dsl_ThrowStatement)

@given(instance=dsl_ReturnStatement_strategy)
@settings(max_examples=50)
def test_dsl_returnstatement_instantiation(instance):
    assert isinstance(instance, dsl_ReturnStatement)

@given(instance=dsl_ContinueStatement_strategy)
@settings(max_examples=50)
def test_dsl_continuestatement_instantiation(instance):
    assert isinstance(instance, dsl_ContinueStatement)



@given(instance=dsl_ContinueStatement_strategy)
def test_dsl_continuestatement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl_BreakStatement_strategy)
@settings(max_examples=50)
def test_dsl_breakstatement_instantiation(instance):
    assert isinstance(instance, dsl_BreakStatement)



@given(instance=dsl_BreakStatement_strategy)
def test_dsl_breakstatement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl_ForStatement_strategy)
@settings(max_examples=50)
def test_dsl_forstatement_instantiation(instance):
    assert isinstance(instance, dsl_ForStatement)



@given(instance=dsl_ForStatement_strategy)
def test_dsl_forstatement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl_DoStatement_strategy)
@settings(max_examples=50)
def test_dsl_dostatement_instantiation(instance):
    assert isinstance(instance, dsl_DoStatement)

@given(instance=dsl_WhileStatement_strategy)
@settings(max_examples=50)
def test_dsl_whilestatement_instantiation(instance):
    assert isinstance(instance, dsl_WhileStatement)

@given(instance=dsl_IfStatement_strategy)
@settings(max_examples=50)
def test_dsl_ifstatement_instantiation(instance):
    assert isinstance(instance, dsl_IfStatement)

@given(instance=dsl_SwitchStatement_strategy)
@settings(max_examples=50)
def test_dsl_switchstatement_instantiation(instance):
    assert isinstance(instance, dsl_SwitchStatement)

@given(instance=dsl_StatementExpression_strategy)
@settings(max_examples=50)
def test_dsl_statementexpression_instantiation(instance):
    assert isinstance(instance, dsl_StatementExpression)



@given(instance=dsl_StatementExpression_strategy)
def test_dsl_statementexpression_minOp_setter(instance):
    original = instance.minOp
    instance.minOp = original
    assert instance.minOp == original



@given(instance=dsl_StatementExpression_strategy)
def test_dsl_statementexpression_plusOp_setter(instance):
    original = instance.plusOp
    instance.plusOp = original
    assert instance.plusOp == original



@given(instance=dsl_StatementExpression_strategy)
def test_dsl_statementexpression_assignOp_setter(instance):
    original = instance.assignOp
    instance.assignOp = original
    assert instance.assignOp == original

@given(instance=dsl_AssertStatement_strategy)
@settings(max_examples=50)
def test_dsl_assertstatement_instantiation(instance):
    assert isinstance(instance, dsl_AssertStatement)

@given(instance=dsl_LabeledStatement_strategy)
@settings(max_examples=50)
def test_dsl_labeledstatement_instantiation(instance):
    assert isinstance(instance, dsl_LabeledStatement)



@given(instance=dsl_LabeledStatement_strategy)
def test_dsl_labeledstatement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl_ArrayDimsAndInits_strategy)
@settings(max_examples=50)
def test_dsl_arraydimsandinits_instantiation(instance):
    assert isinstance(instance, dsl_ArrayDimsAndInits)



@given(instance=dsl_ArrayDimsAndInits_strategy)
def test_dsl_arraydimsandinits_squareBrackets_setter(instance):
    original = instance.squareBrackets
    instance.squareBrackets = original
    assert instance.squareBrackets == original

@given(instance=dsl_BaseLiteral_strategy)
@settings(max_examples=50)
def test_dsl_baseliteral_instantiation(instance):
    assert isinstance(instance, dsl_BaseLiteral)



@given(instance=dsl_BaseLiteral_strategy)
def test_dsl_baseliteral_hexDigitsUnderscore_setter(instance):
    original = instance.hexDigitsUnderscore
    instance.hexDigitsUnderscore = original
    assert instance.hexDigitsUnderscore == original



@given(instance=dsl_BaseLiteral_strategy)
def test_dsl_baseliteral_decDigitsUnderscore_setter(instance):
    original = instance.decDigitsUnderscore
    instance.decDigitsUnderscore = original
    assert instance.decDigitsUnderscore == original



@given(instance=dsl_BaseLiteral_strategy)
def test_dsl_baseliteral_binDigitsUnderscore_setter(instance):
    original = instance.binDigitsUnderscore
    instance.binDigitsUnderscore = original
    assert instance.binDigitsUnderscore == original

@given(instance=dsl_ArgumentList_strategy)
@settings(max_examples=50)
def test_dsl_argumentlist_instantiation(instance):
    assert isinstance(instance, dsl_ArgumentList)

@given(instance=dsl_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_dsl_booleanliteral_instantiation(instance):
    assert isinstance(instance, dsl_BooleanLiteral)



@given(instance=dsl_BooleanLiteral_strategy)
def test_dsl_booleanliteral_truthiness_setter(instance):
    original = instance.truthiness
    instance.truthiness = original
    assert instance.truthiness == original

@given(instance=dsl_FloatLiteral_strategy)
@settings(max_examples=50)
def test_dsl_floatliteral_instantiation(instance):
    assert isinstance(instance, dsl_FloatLiteral)



@given(instance=dsl_FloatLiteral_strategy)
def test_dsl_floatliteral_digits_setter(instance):
    original = instance.digits
    instance.digits = original
    assert instance.digits == original

@given(instance=dsl_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_dsl_integerliteral_instantiation(instance):
    assert isinstance(instance, dsl_IntegerLiteral)



@given(instance=dsl_IntegerLiteral_strategy)
def test_dsl_integerliteral_one_setter(instance):
    original = instance.one
    instance.one = original
    assert instance.one == original



@given(instance=dsl_IntegerLiteral_strategy)
def test_dsl_integerliteral_zero_setter(instance):
    original = instance.zero
    instance.zero = original
    assert instance.zero == original

@given(instance=dsl_SignedIntLiteral_strategy)
@settings(max_examples=50)
def test_dsl_signedintliteral_instantiation(instance):
    assert isinstance(instance, dsl_SignedIntLiteral)



@given(instance=dsl_SignedIntLiteral_strategy)
def test_dsl_signedintliteral_bitWidth_setter(instance):
    original = instance.bitWidth
    instance.bitWidth = original
    assert instance.bitWidth == original

@given(instance=dsl_UnsignedIntLiteral_strategy)
@settings(max_examples=50)
def test_dsl_unsignedintliteral_instantiation(instance):
    assert isinstance(instance, dsl_UnsignedIntLiteral)



@given(instance=dsl_UnsignedIntLiteral_strategy)
def test_dsl_unsignedintliteral_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=dsl_MemberSelector_strategy)
@settings(max_examples=50)
def test_dsl_memberselector_instantiation(instance):
    assert isinstance(instance, dsl_MemberSelector)



@given(instance=dsl_MemberSelector_strategy)
def test_dsl_memberselector_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl_DecimalNumber_strategy)
@settings(max_examples=50)
def test_dsl_decimalnumber_instantiation(instance):
    assert isinstance(instance, dsl_DecimalNumber)



@given(instance=dsl_DecimalNumber_strategy)
def test_dsl_decimalnumber_decDigits_setter(instance):
    original = instance.decDigits
    instance.decDigits = original
    assert instance.decDigits == original



@given(instance=dsl_DecimalNumber_strategy)
def test_dsl_decimalnumber_decDigitsUnderscore_setter(instance):
    original = instance.decDigitsUnderscore
    instance.decDigitsUnderscore = original
    assert instance.decDigitsUnderscore == original

@given(instance=dsl_PrimarySuffix_strategy)
@settings(max_examples=50)
def test_dsl_primarysuffix_instantiation(instance):
    assert isinstance(instance, dsl_PrimarySuffix)



@given(instance=dsl_PrimarySuffix_strategy)
def test_dsl_primarysuffix_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=dsl_PrimarySuffix_strategy)
def test_dsl_primarysuffix_thisOp_setter(instance):
    original = instance.thisOp
    instance.thisOp = original
    assert instance.thisOp == original

@given(instance=dsl_AllocationExpression_strategy)
@settings(max_examples=50)
def test_dsl_allocationexpression_instantiation(instance):
    assert isinstance(instance, dsl_AllocationExpression)



@given(instance=dsl_AllocationExpression_strategy)
def test_dsl_allocationexpression_primType_setter(instance):
    original = instance.primType
    instance.primType = original
    assert instance.primType == original

@given(instance=dsl_PrimaryPrefix_strategy)
@settings(max_examples=50)
def test_dsl_primaryprefix_instantiation(instance):
    assert isinstance(instance, dsl_PrimaryPrefix)



@given(instance=dsl_PrimaryPrefix_strategy)
def test_dsl_primaryprefix_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=dsl_PrimaryPrefix_strategy)
def test_dsl_primaryprefix_superOp_setter(instance):
    original = instance.superOp
    instance.superOp = original
    assert instance.superOp == original



@given(instance=dsl_PrimaryPrefix_strategy)
def test_dsl_primaryprefix_thisOp_setter(instance):
    original = instance.thisOp
    instance.thisOp = original
    assert instance.thisOp == original

@given(instance=dsl_PreDecrementExpression_strategy)
@settings(max_examples=50)
def test_dsl_predecrementexpression_instantiation(instance):
    assert isinstance(instance, dsl_PreDecrementExpression)

@given(instance=dsl_PreIncrementExpression_strategy)
@settings(max_examples=50)
def test_dsl_preincrementexpression_instantiation(instance):
    assert isinstance(instance, dsl_PreIncrementExpression)

@given(instance=dsl_EObject_strategy)
@settings(max_examples=50)
def test_dsl_eobject_instantiation(instance):
    assert isinstance(instance, dsl_EObject)

@given(instance=dsl_Literal_strategy)
@settings(max_examples=50)
def test_dsl_literal_instantiation(instance):
    assert isinstance(instance, dsl_Literal)



@given(instance=dsl_Literal_strategy)
def test_dsl_literal_stringLit_setter(instance):
    original = instance.stringLit
    instance.stringLit = original
    assert instance.stringLit == original



@given(instance=dsl_Literal_strategy)
def test_dsl_literal_charLit_setter(instance):
    original = instance.charLit
    instance.charLit = original
    assert instance.charLit == original



@given(instance=dsl_Literal_strategy)
def test_dsl_literal_nullLit_setter(instance):
    original = instance.nullLit
    instance.nullLit = original
    assert instance.nullLit == original

@given(instance=dsl_CastLookahead_strategy)
@settings(max_examples=50)
def test_dsl_castlookahead_instantiation(instance):
    assert isinstance(instance, dsl_CastLookahead)



@given(instance=dsl_CastLookahead_strategy)
def test_dsl_castlookahead_newOp_setter(instance):
    original = instance.newOp
    instance.newOp = original
    assert instance.newOp == original



@given(instance=dsl_CastLookahead_strategy)
def test_dsl_castlookahead_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=dsl_CastLookahead_strategy)
def test_dsl_castlookahead_bitNegOp_setter(instance):
    original = instance.bitNegOp
    instance.bitNegOp = original
    assert instance.bitNegOp == original



@given(instance=dsl_CastLookahead_strategy)
def test_dsl_castlookahead_openBracket_setter(instance):
    original = instance.openBracket
    instance.openBracket = original
    assert instance.openBracket == original



@given(instance=dsl_CastLookahead_strategy)
def test_dsl_castlookahead_negOp_setter(instance):
    original = instance.negOp
    instance.negOp = original
    assert instance.negOp == original



@given(instance=dsl_CastLookahead_strategy)
def test_dsl_castlookahead_thisOp_setter(instance):
    original = instance.thisOp
    instance.thisOp = original
    assert instance.thisOp == original



@given(instance=dsl_CastLookahead_strategy)
def test_dsl_castlookahead_superOp_setter(instance):
    original = instance.superOp
    instance.superOp = original
    assert instance.superOp == original



@given(instance=dsl_CastLookahead_strategy)
def test_dsl_castlookahead_primType_setter(instance):
    original = instance.primType
    instance.primType = original
    assert instance.primType == original

@given(instance=dsl_PostfixExpression_strategy)
@settings(max_examples=50)
def test_dsl_postfixexpression_instantiation(instance):
    assert isinstance(instance, dsl_PostfixExpression)



@given(instance=dsl_PostfixExpression_strategy)
def test_dsl_postfixexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=dsl_CastExpression_strategy)
@settings(max_examples=50)
def test_dsl_castexpression_instantiation(instance):
    assert isinstance(instance, dsl_CastExpression)

@given(instance=dsl_UnaryExpressionNotPlusMinus_strategy)
@settings(max_examples=50)
def test_dsl_unaryexpressionnotplusminus_instantiation(instance):
    assert isinstance(instance, dsl_UnaryExpressionNotPlusMinus)



@given(instance=dsl_UnaryExpressionNotPlusMinus_strategy)
def test_dsl_unaryexpressionnotplusminus_negOp_setter(instance):
    original = instance.negOp
    instance.negOp = original
    assert instance.negOp == original

@given(instance=dsl_UnaryExpression_strategy)
@settings(max_examples=50)
def test_dsl_unaryexpression_instantiation(instance):
    assert isinstance(instance, dsl_UnaryExpression)



@given(instance=dsl_UnaryExpression_strategy)
def test_dsl_unaryexpression_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=dsl_MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_dsl_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, dsl_MultiplicativeExpression)



@given(instance=dsl_MultiplicativeExpression_strategy)
def test_dsl_multiplicativeexpression_ops_setter(instance):
    original = instance.ops
    instance.ops = original
    assert instance.ops == original

@given(instance=dsl_AdditiveExpression_strategy)
@settings(max_examples=50)
def test_dsl_additiveexpression_instantiation(instance):
    assert isinstance(instance, dsl_AdditiveExpression)



@given(instance=dsl_AdditiveExpression_strategy)
def test_dsl_additiveexpression_ops_setter(instance):
    original = instance.ops
    instance.ops = original
    assert instance.ops == original

@given(instance=dsl_ShiftExpression_strategy)
@settings(max_examples=50)
def test_dsl_shiftexpression_instantiation(instance):
    assert isinstance(instance, dsl_ShiftExpression)



@given(instance=dsl_ShiftExpression_strategy)
def test_dsl_shiftexpression_ops_setter(instance):
    original = instance.ops
    instance.ops = original
    assert instance.ops == original

@given(instance=dsl_RelationalExpression_strategy)
@settings(max_examples=50)
def test_dsl_relationalexpression_instantiation(instance):
    assert isinstance(instance, dsl_RelationalExpression)



@given(instance=dsl_RelationalExpression_strategy)
def test_dsl_relationalexpression_ops_setter(instance):
    original = instance.ops
    instance.ops = original
    assert instance.ops == original

@given(instance=dsl_InstanceOfExpression_strategy)
@settings(max_examples=50)
def test_dsl_instanceofexpression_instantiation(instance):
    assert isinstance(instance, dsl_InstanceOfExpression)

@given(instance=dsl_EqualityExpression_strategy)
@settings(max_examples=50)
def test_dsl_equalityexpression_instantiation(instance):
    assert isinstance(instance, dsl_EqualityExpression)

@given(instance=dsl_AndExpression_strategy)
@settings(max_examples=50)
def test_dsl_andexpression_instantiation(instance):
    assert isinstance(instance, dsl_AndExpression)

@given(instance=dsl_ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_dsl_exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, dsl_ExclusiveOrExpression)

@given(instance=dsl_InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_dsl_inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, dsl_InclusiveOrExpression)

@given(instance=dsl_ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_dsl_conditionalandexpression_instantiation(instance):
    assert isinstance(instance, dsl_ConditionalAndExpression)

@given(instance=IfStatement_strategy)
@settings(max_examples=50)
def test_ifstatement_instantiation(instance):
    assert isinstance(instance, IfStatement)

@given(instance=dsl_ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_dsl_conditionalorexpression_instantiation(instance):
    assert isinstance(instance, dsl_ConditionalOrExpression)

@given(instance=dsl_Statement_strategy)
@settings(max_examples=50)
def test_dsl_statement_instantiation(instance):
    assert isinstance(instance, dsl_Statement)

@given(instance=dsl_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_dsl_conditionalexpression_instantiation(instance):
    assert isinstance(instance, dsl_ConditionalExpression)

@given(instance=dsl_WildcardBounds_strategy)
@settings(max_examples=50)
def test_dsl_wildcardbounds_instantiation(instance):
    assert isinstance(instance, dsl_WildcardBounds)



@given(instance=dsl_WildcardBounds_strategy)
def test_dsl_wildcardbounds_ext_setter(instance):
    original = instance.ext
    instance.ext = original
    assert instance.ext == original



@given(instance=dsl_WildcardBounds_strategy)
def test_dsl_wildcardbounds_sup_setter(instance):
    original = instance.sup
    instance.sup = original
    assert instance.sup == original

@given(instance=dsl_TypeArgument_strategy)
@settings(max_examples=50)
def test_dsl_typeargument_instantiation(instance):
    assert isinstance(instance, dsl_TypeArgument)

@given(instance=dsl_TypeArguments_strategy)
@settings(max_examples=50)
def test_dsl_typearguments_instantiation(instance):
    assert isinstance(instance, dsl_TypeArguments)

@given(instance=dsl_ReferenceType_strategy)
@settings(max_examples=50)
def test_dsl_referencetype_instantiation(instance):
    assert isinstance(instance, dsl_ReferenceType)



@given(instance=dsl_ReferenceType_strategy)
def test_dsl_referencetype_primType_setter(instance):
    original = instance.primType
    instance.primType = original
    assert instance.primType == original



@given(instance=dsl_ReferenceType_strategy)
def test_dsl_referencetype_squareBracketsAlpha_setter(instance):
    original = instance.squareBracketsAlpha
    instance.squareBracketsAlpha = original
    assert instance.squareBracketsAlpha == original



@given(instance=dsl_ReferenceType_strategy)
def test_dsl_referencetype_squareBracketsBeta_setter(instance):
    original = instance.squareBracketsBeta
    instance.squareBracketsBeta = original
    assert instance.squareBracketsBeta == original

@given(instance=dsl_PrimaryExpression_strategy)
@settings(max_examples=50)
def test_dsl_primaryexpression_instantiation(instance):
    assert isinstance(instance, dsl_PrimaryExpression)

@given(instance=dsl_VariableDeclaratorId_strategy)
@settings(max_examples=50)
def test_dsl_variabledeclaratorid_instantiation(instance):
    assert isinstance(instance, dsl_VariableDeclaratorId)



@given(instance=dsl_VariableDeclaratorId_strategy)
def test_dsl_variabledeclaratorid_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=dsl_VariableDeclaratorId_strategy)
def test_dsl_variabledeclaratorid_squareBrackets_setter(instance):
    original = instance.squareBrackets
    instance.squareBrackets = original
    assert instance.squareBrackets == original

@given(instance=dsl_VariableDeclarator_strategy)
@settings(max_examples=50)
def test_dsl_variabledeclarator_instantiation(instance):
    assert isinstance(instance, dsl_VariableDeclarator)

@given(instance=dsl_FormalParameter_strategy)
@settings(max_examples=50)
def test_dsl_formalparameter_instantiation(instance):
    assert isinstance(instance, dsl_FormalParameter)



@given(instance=dsl_FormalParameter_strategy)
def test_dsl_formalparameter_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=dsl_Block_strategy)
@settings(max_examples=50)
def test_dsl_block_instantiation(instance):
    assert isinstance(instance, dsl_Block)

@given(instance=dsl_MethodDeclarator_strategy)
@settings(max_examples=50)
def test_dsl_methoddeclarator_instantiation(instance):
    assert isinstance(instance, dsl_MethodDeclarator)



@given(instance=dsl_MethodDeclarator_strategy)
def test_dsl_methoddeclarator_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=dsl_MethodDeclarator_strategy)
def test_dsl_methoddeclarator_squareBrackets_setter(instance):
    original = instance.squareBrackets
    instance.squareBrackets = original
    assert instance.squareBrackets == original

@given(instance=dsl_ResultType_strategy)
@settings(max_examples=50)
def test_dsl_resulttype_instantiation(instance):
    assert isinstance(instance, dsl_ResultType)

@given(instance=dsl_BlockStatement_strategy)
@settings(max_examples=50)
def test_dsl_blockstatement_instantiation(instance):
    assert isinstance(instance, dsl_BlockStatement)

@given(instance=dsl_ExplicitConstructorInvocation_strategy)
@settings(max_examples=50)
def test_dsl_explicitconstructorinvocation_instantiation(instance):
    assert isinstance(instance, dsl_ExplicitConstructorInvocation)



@given(instance=dsl_ExplicitConstructorInvocation_strategy)
def test_dsl_explicitconstructorinvocation_parent_setter(instance):
    original = instance.parent
    instance.parent = original
    assert instance.parent == original



@given(instance=dsl_ExplicitConstructorInvocation_strategy)
def test_dsl_explicitconstructorinvocation_self_setter(instance):
    original = instance.self
    instance.self = original
    assert instance.self == original

@given(instance=dsl_NameList_strategy)
@settings(max_examples=50)
def test_dsl_namelist_instantiation(instance):
    assert isinstance(instance, dsl_NameList)

@given(instance=dsl_FormalParameters_strategy)
@settings(max_examples=50)
def test_dsl_formalparameters_instantiation(instance):
    assert isinstance(instance, dsl_FormalParameters)

@given(instance=dsl_Expression_strategy)
@settings(max_examples=50)
def test_dsl_expression_instantiation(instance):
    assert isinstance(instance, dsl_Expression)



@given(instance=dsl_Expression_strategy)
def test_dsl_expression_assignOp_setter(instance):
    original = instance.assignOp
    instance.assignOp = original
    assert instance.assignOp == original

@given(instance=dsl_ArrayInitializer_strategy)
@settings(max_examples=50)
def test_dsl_arrayinitializer_instantiation(instance):
    assert isinstance(instance, dsl_ArrayInitializer)

@given(instance=dsl_VariableInitializer_strategy)
@settings(max_examples=50)
def test_dsl_variableinitializer_instantiation(instance):
    assert isinstance(instance, dsl_VariableInitializer)

@given(instance=dsl_Type_strategy)
@settings(max_examples=50)
def test_dsl_type_instantiation(instance):
    assert isinstance(instance, dsl_Type)



@given(instance=dsl_Type_strategy)
def test_dsl_type_primType_setter(instance):
    original = instance.primType
    instance.primType = original
    assert instance.primType == original

@given(instance=dsl_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_dsl_fielddeclaration_instantiation(instance):
    assert isinstance(instance, dsl_FieldDeclaration)

@given(instance=dsl_MethodOrCtorDeclaration_strategy)
@settings(max_examples=50)
def test_dsl_methodorctordeclaration_instantiation(instance):
    assert isinstance(instance, dsl_MethodOrCtorDeclaration)



@given(instance=dsl_MethodOrCtorDeclaration_strategy)
def test_dsl_methodorctordeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl_Initializer_strategy)
@settings(max_examples=50)
def test_dsl_initializer_instantiation(instance):
    assert isinstance(instance, dsl_Initializer)



@given(instance=dsl_Initializer_strategy)
def test_dsl_initializer_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=dsl_TypeBound_strategy)
@settings(max_examples=50)
def test_dsl_typebound_instantiation(instance):
    assert isinstance(instance, dsl_TypeBound)

@given(instance=dsl_TypeParameter_strategy)
@settings(max_examples=50)
def test_dsl_typeparameter_instantiation(instance):
    assert isinstance(instance, dsl_TypeParameter)



@given(instance=dsl_TypeParameter_strategy)
def test_dsl_typeparameter_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl_Arguments_strategy)
@settings(max_examples=50)
def test_dsl_arguments_instantiation(instance):
    assert isinstance(instance, dsl_Arguments)

@given(instance=dsl_ClassOrInterfaceBodyDeclaration_strategy)
@settings(max_examples=50)
def test_dsl_classorinterfacebodydeclaration_instantiation(instance):
    assert isinstance(instance, dsl_ClassOrInterfaceBodyDeclaration)

@given(instance=dsl_EnumConstant_strategy)
@settings(max_examples=50)
def test_dsl_enumconstant_instantiation(instance):
    assert isinstance(instance, dsl_EnumConstant)



@given(instance=dsl_EnumConstant_strategy)
def test_dsl_enumconstant_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl_EnumBody_strategy)
@settings(max_examples=50)
def test_dsl_enumbody_instantiation(instance):
    assert isinstance(instance, dsl_EnumBody)

@given(instance=dsl_ClassOrInterfaceType_strategy)
@settings(max_examples=50)
def test_dsl_classorinterfacetype_instantiation(instance):
    assert isinstance(instance, dsl_ClassOrInterfaceType)



@given(instance=dsl_ClassOrInterfaceType_strategy)
def test_dsl_classorinterfacetype_ids_setter(instance):
    original = instance.ids
    instance.ids = original
    assert instance.ids == original

@given(instance=dsl_ClassOrInterfaceBody_strategy)
@settings(max_examples=50)
def test_dsl_classorinterfacebody_instantiation(instance):
    assert isinstance(instance, dsl_ClassOrInterfaceBody)

@given(instance=dsl_ImplementsList_strategy)
@settings(max_examples=50)
def test_dsl_implementslist_instantiation(instance):
    assert isinstance(instance, dsl_ImplementsList)

@given(instance=dsl_ExtendsList_strategy)
@settings(max_examples=50)
def test_dsl_extendslist_instantiation(instance):
    assert isinstance(instance, dsl_ExtendsList)

@given(instance=dsl_TypeParameters_strategy)
@settings(max_examples=50)
def test_dsl_typeparameters_instantiation(instance):
    assert isinstance(instance, dsl_TypeParameters)

@given(instance=dsl_AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_dsl_annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, dsl_AnnotationTypeDeclaration)



@given(instance=dsl_AnnotationTypeDeclaration_strategy)
def test_dsl_annotationtypedeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl_EnumDeclaration_strategy)
@settings(max_examples=50)
def test_dsl_enumdeclaration_instantiation(instance):
    assert isinstance(instance, dsl_EnumDeclaration)



@given(instance=dsl_EnumDeclaration_strategy)
def test_dsl_enumdeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl_ClassOrInterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_dsl_classorinterfacedeclaration_instantiation(instance):
    assert isinstance(instance, dsl_ClassOrInterfaceDeclaration)



@given(instance=dsl_ClassOrInterfaceDeclaration_strategy)
def test_dsl_classorinterfacedeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=dsl_ClassOrInterfaceDeclaration_strategy)
def test_dsl_classorinterfacedeclaration_typeCategory_setter(instance):
    original = instance.typeCategory
    instance.typeCategory = original
    assert instance.typeCategory == original

@given(instance=dsl_TypeBodyModifier_strategy)
@settings(max_examples=50)
def test_dsl_typebodymodifier_instantiation(instance):
    assert isinstance(instance, dsl_TypeBodyModifier)



@given(instance=dsl_TypeBodyModifier_strategy)
def test_dsl_typebodymodifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=dsl_TypeBodyModifier_strategy)
def test_dsl_typebodymodifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=dsl_TypeBodyModifier_strategy)
def test_dsl_typebodymodifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original



@given(instance=dsl_TypeBodyModifier_strategy)
def test_dsl_typebodymodifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original



@given(instance=dsl_TypeBodyModifier_strategy)
def test_dsl_typebodymodifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original

@given(instance=dsl_CommonModifier_strategy)
@settings(max_examples=50)
def test_dsl_commonmodifier_instantiation(instance):
    assert isinstance(instance, dsl_CommonModifier)



@given(instance=dsl_CommonModifier_strategy)
def test_dsl_commonmodifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=dsl_CommonModifier_strategy)
def test_dsl_commonmodifier_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=dsl_CommonModifier_strategy)
def test_dsl_commonmodifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=dsl_CommonModifier_strategy)
def test_dsl_commonmodifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=dsl_Name_strategy)
@settings(max_examples=50)
def test_dsl_name_instantiation(instance):
    assert isinstance(instance, dsl_Name)



@given(instance=dsl_Name_strategy)
def test_dsl_name_ids_setter(instance):
    original = instance.ids
    instance.ids = original
    assert instance.ids == original

@given(instance=dsl_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_dsl_typedeclaration_instantiation(instance):
    assert isinstance(instance, dsl_TypeDeclaration)

@given(instance=dsl_ImportDeclaration_strategy)
@settings(max_examples=50)
def test_dsl_importdeclaration_instantiation(instance):
    assert isinstance(instance, dsl_ImportDeclaration)

@given(instance=dsl_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_dsl_packagedeclaration_instantiation(instance):
    assert isinstance(instance, dsl_PackageDeclaration)

@given(instance=dsl_CompilationUnit_strategy)
@settings(max_examples=50)
def test_dsl_compilationunit_instantiation(instance):
    assert isinstance(instance, dsl_CompilationUnit)
