import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    javaDsl_ArrayCreationExpression,
    Primary,
    javaDsl_PrimaryNewArray,
    javaDsl_PrimaryNoNewArray,
    javaDsl_ArrayExpression,
    LeftHandSide,
    javaDsl_ArrayAccess,
    javaDsl_FieldAccess,
    javaDsl_Primary,
    NoArrayExpression,
    javaDsl_NoArrayExpressionWithoutMinus,
    NoArrayExpressionWithoutMinus,
    javaDsl_CastExpression,
    javaDsl_NoArrayExpression,
    javaDsl_MultiplicativeExpression,
    javaDsl_AdditiveExpression,
    javaDsl_ShiftExpression,
    javaDsl_RelationalExpression,
    javaDsl_EqualityExpression,
    javaDsl_AndExpression,
    javaDsl_ExclusiveOrExpression,
    javaDsl_ConditionalAndExpression,
    javaDsl_ConditionalOrExpression,
    javaDsl_LeftHandSide,
    AssignmentExpression,
    javaDsl_ConditionalExpression,
    StatementExpression,
    javaDsl_PostfixExpression,
    javaDsl_MethodInvocation,
    javaDsl_PreIncrementExpression,
    javaDsl_ClassInstanceCreationExpression,
    javaDsl_PreDecrementExpression,
    javaDsl_Assignment,
    Expression,
    javaDsl_AssignmentExpression,
    PrimaryNoNewArray,
    ConstantExpression,
    javaDsl_InclusiveOrExpression,
    javaDsl_ForUpdate,
    javaDsl_ForInit,
    javaDsl_ConstantExpression,
    BlockStatement,
    javaDsl_Statement,
    javaDsl_LocalVariableDeclaration,
    Statement,
    javaDsl_ReturnStatement,
    javaDsl_IfStatement,
    javaDsl_BreakStatement,
    javaDsl_WhileStatement,
    javaDsl_StatementExpression,
    javaDsl_ThrowsStatement,
    javaDsl_ContinueStatement,
    javaDsl_SynchronizedStatement,
    javaDsl_SwitchStatement,
    javaDsl_DoStatement,
    javaDsl_TryStatement,
    javaDsl_ForStatement,
    javaDsl_LabeledStatement,
    VariableInitializer,
    javaDsl_ArrayInitializer,
    InterfaceMemberDeclaration,
    javaDsl_AbstractMethodDeclaration,
    javaDsl_ConstantDeclaration,
    javaDsl_InterfaceMemberDeclaration,
    javaDsl_InterfaceBody,
    javaDsl_ExtendsInterfaces,
    javaDsl_InterfaceDeclaration,
    javaDsl_MethodDeclarator,
    javaDsl_ResultType,
    javaDsl_MethodHeader,
    javaDsl_VariableDeclarator,
    javaDsl_ArgumentList,
    javaDsl_BlockStatement,
    javaDsl_ExplicitConstructorInvocation,
    javaDsl_Type,
    javaDsl_FormalParameter,
    javaDsl_ConstructorBody,
    javaDsl_Exceptions,
    javaDsl_ConstructorDeclarator,
    javaDsl_Block,
    ClassBodyDeclaration,
    javaDsl_ConstructorDeclaration,
    javaDsl_StaticInitializer,
    javaDsl_MethodDeclaration,
    javaDsl_FieldDeclaration,
    javaDsl_ClassMemberDeclaration,
    javaDsl_Expression,
    javaDsl_VariableInitializer,
    javaDsl_ClassBody,
    javaDsl_Interfaces,
    javaDsl_ClassDeclaration,
    javaDsl_EObject,
    javaDsl_TypeDeclaration,
    javaDsl_ImportStatement,
    javaDsl_PackageStatement,
    javaDsl_CompilationUnit,
    javaDsl_Head,
    javaDsl_ClassBodyDeclaration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_javadsl_arraycreationexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ArrayCreationExpression)


def test_javadsl_arraycreationexpression_constructor_exists():
    assert callable(javaDsl_ArrayCreationExpression.__init__)


def test_javadsl_arraycreationexpression_constructor_args():
    sig = inspect.signature(javaDsl_ArrayCreationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "layers" in params, "Missing parameter 'layers'"
    assert "type" in params, "Missing parameter 'type'"

def test_javadsl_arraycreationexpression_has_layers():
    assert hasattr(javaDsl_ArrayCreationExpression, "layers")
    descriptor = None
    for klass in javaDsl_ArrayCreationExpression.__mro__:
        if "layers" in klass.__dict__:
            descriptor = klass.__dict__["layers"]
            break
    assert isinstance(descriptor, property)

def test_javadsl_arraycreationexpression_has_type():
    assert hasattr(javaDsl_ArrayCreationExpression, "type")
    descriptor = None
    for klass in javaDsl_ArrayCreationExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_primary_is_not_abstract():
    assert not inspect.isabstract(Primary)


def test_primary_constructor_exists():
    assert callable(Primary.__init__)


def test_primary_constructor_args():
    sig = inspect.signature(Primary.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_primarynewarray_is_not_abstract():
    assert not inspect.isabstract(javaDsl_PrimaryNewArray)


def test_javadsl_primarynewarray_constructor_exists():
    assert callable(javaDsl_PrimaryNewArray.__init__)


def test_javadsl_primarynewarray_constructor_args():
    sig = inspect.signature(javaDsl_PrimaryNewArray.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_primarynonewarray_is_not_abstract():
    assert not inspect.isabstract(javaDsl_PrimaryNoNewArray)


def test_javadsl_primarynonewarray_constructor_exists():
    assert callable(javaDsl_PrimaryNoNewArray.__init__)


def test_javadsl_primarynonewarray_constructor_args():
    sig = inspect.signature(javaDsl_PrimaryNoNewArray.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"
    assert "method" in params, "Missing parameter 'method'"
    assert "keyword" in params, "Missing parameter 'keyword'"
    assert "reference" in params, "Missing parameter 'reference'"

def test_javadsl_primarynonewarray_has_literal():
    assert hasattr(javaDsl_PrimaryNoNewArray, "literal")
    descriptor = None
    for klass in javaDsl_PrimaryNoNewArray.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)

def test_javadsl_primarynonewarray_has_method():
    assert hasattr(javaDsl_PrimaryNoNewArray, "method")
    descriptor = None
    for klass in javaDsl_PrimaryNoNewArray.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)

def test_javadsl_primarynonewarray_has_keyword():
    assert hasattr(javaDsl_PrimaryNoNewArray, "keyword")
    descriptor = None
    for klass in javaDsl_PrimaryNoNewArray.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)

def test_javadsl_primarynonewarray_has_reference():
    assert hasattr(javaDsl_PrimaryNoNewArray, "reference")
    descriptor = None
    for klass in javaDsl_PrimaryNoNewArray.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_arrayexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ArrayExpression)


def test_javadsl_arrayexpression_constructor_exists():
    assert callable(javaDsl_ArrayExpression.__init__)


def test_javadsl_arrayexpression_constructor_args():
    sig = inspect.signature(javaDsl_ArrayExpression.__init__)
    params = list(sig.parameters.keys())



def test_lefthandside_is_not_abstract():
    assert not inspect.isabstract(LeftHandSide)


def test_lefthandside_constructor_exists():
    assert callable(LeftHandSide.__init__)


def test_lefthandside_constructor_args():
    sig = inspect.signature(LeftHandSide.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ArrayAccess)


def test_javadsl_arrayaccess_constructor_exists():
    assert callable(javaDsl_ArrayAccess.__init__)


def test_javadsl_arrayaccess_constructor_args():
    sig = inspect.signature(javaDsl_ArrayAccess.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"

def test_javadsl_arrayaccess_has_reference():
    assert hasattr(javaDsl_ArrayAccess, "reference")
    descriptor = None
    for klass in javaDsl_ArrayAccess.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_fieldaccess_is_not_abstract():
    assert not inspect.isabstract(javaDsl_FieldAccess)


def test_javadsl_fieldaccess_constructor_exists():
    assert callable(javaDsl_FieldAccess.__init__)


def test_javadsl_fieldaccess_constructor_args():
    sig = inspect.signature(javaDsl_FieldAccess.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"
    assert "field" in params, "Missing parameter 'field'"

def test_javadsl_fieldaccess_has_keyword():
    assert hasattr(javaDsl_FieldAccess, "keyword")
    descriptor = None
    for klass in javaDsl_FieldAccess.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)

def test_javadsl_fieldaccess_has_field():
    assert hasattr(javaDsl_FieldAccess, "field")
    descriptor = None
    for klass in javaDsl_FieldAccess.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_primary_is_not_abstract():
    assert not inspect.isabstract(javaDsl_Primary)


def test_javadsl_primary_constructor_exists():
    assert callable(javaDsl_Primary.__init__)


def test_javadsl_primary_constructor_args():
    sig = inspect.signature(javaDsl_Primary.__init__)
    params = list(sig.parameters.keys())
    assert "fields" in params, "Missing parameter 'fields'"

def test_javadsl_primary_has_fields():
    assert hasattr(javaDsl_Primary, "fields")
    descriptor = None
    for klass in javaDsl_Primary.__mro__:
        if "fields" in klass.__dict__:
            descriptor = klass.__dict__["fields"]
            break
    assert isinstance(descriptor, property)



def test_noarrayexpression_is_not_abstract():
    assert not inspect.isabstract(NoArrayExpression)


def test_noarrayexpression_constructor_exists():
    assert callable(NoArrayExpression.__init__)


def test_noarrayexpression_constructor_args():
    sig = inspect.signature(NoArrayExpression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_noarrayexpressionwithoutminus_is_not_abstract():
    assert not inspect.isabstract(javaDsl_NoArrayExpressionWithoutMinus)


def test_javadsl_noarrayexpressionwithoutminus_constructor_exists():
    assert callable(javaDsl_NoArrayExpressionWithoutMinus.__init__)


def test_javadsl_noarrayexpressionwithoutminus_constructor_args():
    sig = inspect.signature(javaDsl_NoArrayExpressionWithoutMinus.__init__)
    params = list(sig.parameters.keys())



def test_noarrayexpressionwithoutminus_is_not_abstract():
    assert not inspect.isabstract(NoArrayExpressionWithoutMinus)


def test_noarrayexpressionwithoutminus_constructor_exists():
    assert callable(NoArrayExpressionWithoutMinus.__init__)


def test_noarrayexpressionwithoutminus_constructor_args():
    sig = inspect.signature(NoArrayExpressionWithoutMinus.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_castexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_CastExpression)


def test_javadsl_castexpression_constructor_exists():
    assert callable(javaDsl_CastExpression.__init__)


def test_javadsl_castexpression_constructor_args():
    sig = inspect.signature(javaDsl_CastExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_javadsl_castexpression_has_type():
    assert hasattr(javaDsl_CastExpression, "type")
    descriptor = None
    for klass in javaDsl_CastExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_noarrayexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_NoArrayExpression)


def test_javadsl_noarrayexpression_constructor_exists():
    assert callable(javaDsl_NoArrayExpression.__init__)


def test_javadsl_noarrayexpression_constructor_args():
    sig = inspect.signature(javaDsl_NoArrayExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javadsl_noarrayexpression_has_operator():
    assert hasattr(javaDsl_NoArrayExpression, "operator")
    descriptor = None
    for klass in javaDsl_NoArrayExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_MultiplicativeExpression)


def test_javadsl_multiplicativeexpression_constructor_exists():
    assert callable(javaDsl_MultiplicativeExpression.__init__)


def test_javadsl_multiplicativeexpression_constructor_args():
    sig = inspect.signature(javaDsl_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl_multiplicativeexpression_has_operators():
    assert hasattr(javaDsl_MultiplicativeExpression, "operators")
    descriptor = None
    for klass in javaDsl_MultiplicativeExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_AdditiveExpression)


def test_javadsl_additiveexpression_constructor_exists():
    assert callable(javaDsl_AdditiveExpression.__init__)


def test_javadsl_additiveexpression_constructor_args():
    sig = inspect.signature(javaDsl_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl_additiveexpression_has_operators():
    assert hasattr(javaDsl_AdditiveExpression, "operators")
    descriptor = None
    for klass in javaDsl_AdditiveExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ShiftExpression)


def test_javadsl_shiftexpression_constructor_exists():
    assert callable(javaDsl_ShiftExpression.__init__)


def test_javadsl_shiftexpression_constructor_args():
    sig = inspect.signature(javaDsl_ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl_shiftexpression_has_operators():
    assert hasattr(javaDsl_ShiftExpression, "operators")
    descriptor = None
    for klass in javaDsl_ShiftExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_RelationalExpression)


def test_javadsl_relationalexpression_constructor_exists():
    assert callable(javaDsl_RelationalExpression.__init__)


def test_javadsl_relationalexpression_constructor_args():
    sig = inspect.signature(javaDsl_RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"
    assert "classes" in params, "Missing parameter 'classes'"

def test_javadsl_relationalexpression_has_operators():
    assert hasattr(javaDsl_RelationalExpression, "operators")
    descriptor = None
    for klass in javaDsl_RelationalExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)

def test_javadsl_relationalexpression_has_classes():
    assert hasattr(javaDsl_RelationalExpression, "classes")
    descriptor = None
    for klass in javaDsl_RelationalExpression.__mro__:
        if "classes" in klass.__dict__:
            descriptor = klass.__dict__["classes"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_EqualityExpression)


def test_javadsl_equalityexpression_constructor_exists():
    assert callable(javaDsl_EqualityExpression.__init__)


def test_javadsl_equalityexpression_constructor_args():
    sig = inspect.signature(javaDsl_EqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl_equalityexpression_has_operators():
    assert hasattr(javaDsl_EqualityExpression, "operators")
    descriptor = None
    for klass in javaDsl_EqualityExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_andexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_AndExpression)


def test_javadsl_andexpression_constructor_exists():
    assert callable(javaDsl_AndExpression.__init__)


def test_javadsl_andexpression_constructor_args():
    sig = inspect.signature(javaDsl_AndExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl_andexpression_has_operators():
    assert hasattr(javaDsl_AndExpression, "operators")
    descriptor = None
    for klass in javaDsl_AndExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ExclusiveOrExpression)


def test_javadsl_exclusiveorexpression_constructor_exists():
    assert callable(javaDsl_ExclusiveOrExpression.__init__)


def test_javadsl_exclusiveorexpression_constructor_args():
    sig = inspect.signature(javaDsl_ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl_exclusiveorexpression_has_operators():
    assert hasattr(javaDsl_ExclusiveOrExpression, "operators")
    descriptor = None
    for klass in javaDsl_ExclusiveOrExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ConditionalAndExpression)


def test_javadsl_conditionalandexpression_constructor_exists():
    assert callable(javaDsl_ConditionalAndExpression.__init__)


def test_javadsl_conditionalandexpression_constructor_args():
    sig = inspect.signature(javaDsl_ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl_conditionalandexpression_has_operators():
    assert hasattr(javaDsl_ConditionalAndExpression, "operators")
    descriptor = None
    for klass in javaDsl_ConditionalAndExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ConditionalOrExpression)


def test_javadsl_conditionalorexpression_constructor_exists():
    assert callable(javaDsl_ConditionalOrExpression.__init__)


def test_javadsl_conditionalorexpression_constructor_args():
    sig = inspect.signature(javaDsl_ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl_conditionalorexpression_has_operators():
    assert hasattr(javaDsl_ConditionalOrExpression, "operators")
    descriptor = None
    for klass in javaDsl_ConditionalOrExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_lefthandside_is_not_abstract():
    assert not inspect.isabstract(javaDsl_LeftHandSide)


def test_javadsl_lefthandside_constructor_exists():
    assert callable(javaDsl_LeftHandSide.__init__)


def test_javadsl_lefthandside_constructor_args():
    sig = inspect.signature(javaDsl_LeftHandSide.__init__)
    params = list(sig.parameters.keys())



def test_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(AssignmentExpression)


def test_assignmentexpression_constructor_exists():
    assert callable(AssignmentExpression.__init__)


def test_assignmentexpression_constructor_args():
    sig = inspect.signature(AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ConditionalExpression)


def test_javadsl_conditionalexpression_constructor_exists():
    assert callable(javaDsl_ConditionalExpression.__init__)


def test_javadsl_conditionalexpression_constructor_args():
    sig = inspect.signature(javaDsl_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_statementexpression_is_not_abstract():
    assert not inspect.isabstract(StatementExpression)


def test_statementexpression_constructor_exists():
    assert callable(StatementExpression.__init__)


def test_statementexpression_constructor_args():
    sig = inspect.signature(StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_postfixexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_PostfixExpression)


def test_javadsl_postfixexpression_constructor_exists():
    assert callable(javaDsl_PostfixExpression.__init__)


def test_javadsl_postfixexpression_constructor_args():
    sig = inspect.signature(javaDsl_PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl_postfixexpression_has_reference():
    assert hasattr(javaDsl_PostfixExpression, "reference")
    descriptor = None
    for klass in javaDsl_PostfixExpression.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_javadsl_postfixexpression_has_operators():
    assert hasattr(javaDsl_PostfixExpression, "operators")
    descriptor = None
    for klass in javaDsl_PostfixExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(javaDsl_MethodInvocation)


def test_javadsl_methodinvocation_constructor_exists():
    assert callable(javaDsl_MethodInvocation.__init__)


def test_javadsl_methodinvocation_constructor_args():
    sig = inspect.signature(javaDsl_MethodInvocation.__init__)
    params = list(sig.parameters.keys())
    assert "method" in params, "Missing parameter 'method'"
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_javadsl_methodinvocation_has_method():
    assert hasattr(javaDsl_MethodInvocation, "method")
    descriptor = None
    for klass in javaDsl_MethodInvocation.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)

def test_javadsl_methodinvocation_has_keyword():
    assert hasattr(javaDsl_MethodInvocation, "keyword")
    descriptor = None
    for klass in javaDsl_MethodInvocation.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_preincrementexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_PreIncrementExpression)


def test_javadsl_preincrementexpression_constructor_exists():
    assert callable(javaDsl_PreIncrementExpression.__init__)


def test_javadsl_preincrementexpression_constructor_args():
    sig = inspect.signature(javaDsl_PreIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_classinstancecreationexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ClassInstanceCreationExpression)


def test_javadsl_classinstancecreationexpression_constructor_exists():
    assert callable(javaDsl_ClassInstanceCreationExpression.__init__)


def test_javadsl_classinstancecreationexpression_constructor_args():
    sig = inspect.signature(javaDsl_ClassInstanceCreationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_javadsl_classinstancecreationexpression_has_type():
    assert hasattr(javaDsl_ClassInstanceCreationExpression, "type")
    descriptor = None
    for klass in javaDsl_ClassInstanceCreationExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_predecrementexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_PreDecrementExpression)


def test_javadsl_predecrementexpression_constructor_exists():
    assert callable(javaDsl_PreDecrementExpression.__init__)


def test_javadsl_predecrementexpression_constructor_args():
    sig = inspect.signature(javaDsl_PreDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_assignment_is_not_abstract():
    assert not inspect.isabstract(javaDsl_Assignment)


def test_javadsl_assignment_constructor_exists():
    assert callable(javaDsl_Assignment.__init__)


def test_javadsl_assignment_constructor_args():
    sig = inspect.signature(javaDsl_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javadsl_assignment_has_operator():
    assert hasattr(javaDsl_Assignment, "operator")
    descriptor = None
    for klass in javaDsl_Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_AssignmentExpression)


def test_javadsl_assignmentexpression_constructor_exists():
    assert callable(javaDsl_AssignmentExpression.__init__)


def test_javadsl_assignmentexpression_constructor_args():
    sig = inspect.signature(javaDsl_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_primarynonewarray_is_not_abstract():
    assert not inspect.isabstract(PrimaryNoNewArray)


def test_primarynonewarray_constructor_exists():
    assert callable(PrimaryNoNewArray.__init__)


def test_primarynonewarray_constructor_args():
    sig = inspect.signature(PrimaryNoNewArray.__init__)
    params = list(sig.parameters.keys())



def test_constantexpression_is_not_abstract():
    assert not inspect.isabstract(ConstantExpression)


def test_constantexpression_constructor_exists():
    assert callable(ConstantExpression.__init__)


def test_constantexpression_constructor_args():
    sig = inspect.signature(ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_InclusiveOrExpression)


def test_javadsl_inclusiveorexpression_constructor_exists():
    assert callable(javaDsl_InclusiveOrExpression.__init__)


def test_javadsl_inclusiveorexpression_constructor_args():
    sig = inspect.signature(javaDsl_InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"

def test_javadsl_inclusiveorexpression_has_operators():
    assert hasattr(javaDsl_InclusiveOrExpression, "operators")
    descriptor = None
    for klass in javaDsl_InclusiveOrExpression.__mro__:
        if "operators" in klass.__dict__:
            descriptor = klass.__dict__["operators"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_forupdate_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ForUpdate)


def test_javadsl_forupdate_constructor_exists():
    assert callable(javaDsl_ForUpdate.__init__)


def test_javadsl_forupdate_constructor_args():
    sig = inspect.signature(javaDsl_ForUpdate.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_forinit_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ForInit)


def test_javadsl_forinit_constructor_exists():
    assert callable(javaDsl_ForInit.__init__)


def test_javadsl_forinit_constructor_args():
    sig = inspect.signature(javaDsl_ForInit.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_constantexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ConstantExpression)


def test_javadsl_constantexpression_constructor_exists():
    assert callable(javaDsl_ConstantExpression.__init__)


def test_javadsl_constantexpression_constructor_args():
    sig = inspect.signature(javaDsl_ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_blockstatement_is_not_abstract():
    assert not inspect.isabstract(BlockStatement)


def test_blockstatement_constructor_exists():
    assert callable(BlockStatement.__init__)


def test_blockstatement_constructor_args():
    sig = inspect.signature(BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_statement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_Statement)


def test_javadsl_statement_constructor_exists():
    assert callable(javaDsl_Statement.__init__)


def test_javadsl_statement_constructor_args():
    sig = inspect.signature(javaDsl_Statement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_localvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl_LocalVariableDeclaration)


def test_javadsl_localvariabledeclaration_constructor_exists():
    assert callable(javaDsl_LocalVariableDeclaration.__init__)


def test_javadsl_localvariabledeclaration_constructor_args():
    sig = inspect.signature(javaDsl_LocalVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_returnstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ReturnStatement)


def test_javadsl_returnstatement_constructor_exists():
    assert callable(javaDsl_ReturnStatement.__init__)


def test_javadsl_returnstatement_constructor_args():
    sig = inspect.signature(javaDsl_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_ifstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_IfStatement)


def test_javadsl_ifstatement_constructor_exists():
    assert callable(javaDsl_IfStatement.__init__)


def test_javadsl_ifstatement_constructor_args():
    sig = inspect.signature(javaDsl_IfStatement.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_javadsl_ifstatement_has_condition():
    assert hasattr(javaDsl_IfStatement, "condition")
    descriptor = None
    for klass in javaDsl_IfStatement.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_breakstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_BreakStatement)


def test_javadsl_breakstatement_constructor_exists():
    assert callable(javaDsl_BreakStatement.__init__)


def test_javadsl_breakstatement_constructor_args():
    sig = inspect.signature(javaDsl_BreakStatement.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"

def test_javadsl_breakstatement_has_reference():
    assert hasattr(javaDsl_BreakStatement, "reference")
    descriptor = None
    for klass in javaDsl_BreakStatement.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_whilestatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_WhileStatement)


def test_javadsl_whilestatement_constructor_exists():
    assert callable(javaDsl_WhileStatement.__init__)


def test_javadsl_whilestatement_constructor_args():
    sig = inspect.signature(javaDsl_WhileStatement.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_javadsl_whilestatement_has_condition():
    assert hasattr(javaDsl_WhileStatement, "condition")
    descriptor = None
    for klass in javaDsl_WhileStatement.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_statementexpression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_StatementExpression)


def test_javadsl_statementexpression_constructor_exists():
    assert callable(javaDsl_StatementExpression.__init__)


def test_javadsl_statementexpression_constructor_args():
    sig = inspect.signature(javaDsl_StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_throwsstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ThrowsStatement)


def test_javadsl_throwsstatement_constructor_exists():
    assert callable(javaDsl_ThrowsStatement.__init__)


def test_javadsl_throwsstatement_constructor_args():
    sig = inspect.signature(javaDsl_ThrowsStatement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_continuestatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ContinueStatement)


def test_javadsl_continuestatement_constructor_exists():
    assert callable(javaDsl_ContinueStatement.__init__)


def test_javadsl_continuestatement_constructor_args():
    sig = inspect.signature(javaDsl_ContinueStatement.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"

def test_javadsl_continuestatement_has_reference():
    assert hasattr(javaDsl_ContinueStatement, "reference")
    descriptor = None
    for klass in javaDsl_ContinueStatement.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_SynchronizedStatement)


def test_javadsl_synchronizedstatement_constructor_exists():
    assert callable(javaDsl_SynchronizedStatement.__init__)


def test_javadsl_synchronizedstatement_constructor_args():
    sig = inspect.signature(javaDsl_SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_switchstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_SwitchStatement)


def test_javadsl_switchstatement_constructor_exists():
    assert callable(javaDsl_SwitchStatement.__init__)


def test_javadsl_switchstatement_constructor_args():
    sig = inspect.signature(javaDsl_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_dostatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_DoStatement)


def test_javadsl_dostatement_constructor_exists():
    assert callable(javaDsl_DoStatement.__init__)


def test_javadsl_dostatement_constructor_args():
    sig = inspect.signature(javaDsl_DoStatement.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_javadsl_dostatement_has_condition():
    assert hasattr(javaDsl_DoStatement, "condition")
    descriptor = None
    for klass in javaDsl_DoStatement.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_trystatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_TryStatement)


def test_javadsl_trystatement_constructor_exists():
    assert callable(javaDsl_TryStatement.__init__)


def test_javadsl_trystatement_constructor_args():
    sig = inspect.signature(javaDsl_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_forstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ForStatement)


def test_javadsl_forstatement_constructor_exists():
    assert callable(javaDsl_ForStatement.__init__)


def test_javadsl_forstatement_constructor_args():
    sig = inspect.signature(javaDsl_ForStatement.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_javadsl_forstatement_has_condition():
    assert hasattr(javaDsl_ForStatement, "condition")
    descriptor = None
    for klass in javaDsl_ForStatement.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_LabeledStatement)


def test_javadsl_labeledstatement_constructor_exists():
    assert callable(javaDsl_LabeledStatement.__init__)


def test_javadsl_labeledstatement_constructor_args():
    sig = inspect.signature(javaDsl_LabeledStatement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_javadsl_labeledstatement_has_label():
    assert hasattr(javaDsl_LabeledStatement, "label")
    descriptor = None
    for klass in javaDsl_LabeledStatement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_variableinitializer_is_not_abstract():
    assert not inspect.isabstract(VariableInitializer)


def test_variableinitializer_constructor_exists():
    assert callable(VariableInitializer.__init__)


def test_variableinitializer_constructor_args():
    sig = inspect.signature(VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ArrayInitializer)


def test_javadsl_arrayinitializer_constructor_exists():
    assert callable(javaDsl_ArrayInitializer.__init__)


def test_javadsl_arrayinitializer_constructor_args():
    sig = inspect.signature(javaDsl_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_interfacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(InterfaceMemberDeclaration)


def test_interfacememberdeclaration_constructor_exists():
    assert callable(InterfaceMemberDeclaration.__init__)


def test_interfacememberdeclaration_constructor_args():
    sig = inspect.signature(InterfaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl_AbstractMethodDeclaration)


def test_javadsl_abstractmethoddeclaration_constructor_exists():
    assert callable(javaDsl_AbstractMethodDeclaration.__init__)


def test_javadsl_abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(javaDsl_AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ConstantDeclaration)


def test_javadsl_constantdeclaration_constructor_exists():
    assert callable(javaDsl_ConstantDeclaration.__init__)


def test_javadsl_constantdeclaration_constructor_args():
    sig = inspect.signature(javaDsl_ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_interfacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl_InterfaceMemberDeclaration)


def test_javadsl_interfacememberdeclaration_constructor_exists():
    assert callable(javaDsl_InterfaceMemberDeclaration.__init__)


def test_javadsl_interfacememberdeclaration_constructor_args():
    sig = inspect.signature(javaDsl_InterfaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_javadsl_interfacememberdeclaration_has_modifiers():
    assert hasattr(javaDsl_InterfaceMemberDeclaration, "modifiers")
    descriptor = None
    for klass in javaDsl_InterfaceMemberDeclaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_interfacebody_is_not_abstract():
    assert not inspect.isabstract(javaDsl_InterfaceBody)


def test_javadsl_interfacebody_constructor_exists():
    assert callable(javaDsl_InterfaceBody.__init__)


def test_javadsl_interfacebody_constructor_args():
    sig = inspect.signature(javaDsl_InterfaceBody.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_extendsinterfaces_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ExtendsInterfaces)


def test_javadsl_extendsinterfaces_constructor_exists():
    assert callable(javaDsl_ExtendsInterfaces.__init__)


def test_javadsl_extendsinterfaces_constructor_args():
    sig = inspect.signature(javaDsl_ExtendsInterfaces.__init__)
    params = list(sig.parameters.keys())
    assert "interfaces" in params, "Missing parameter 'interfaces'"
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_javadsl_extendsinterfaces_has_interfaces():
    assert hasattr(javaDsl_ExtendsInterfaces, "interfaces")
    descriptor = None
    for klass in javaDsl_ExtendsInterfaces.__mro__:
        if "interfaces" in klass.__dict__:
            descriptor = klass.__dict__["interfaces"]
            break
    assert isinstance(descriptor, property)

def test_javadsl_extendsinterfaces_has_keyword():
    assert hasattr(javaDsl_ExtendsInterfaces, "keyword")
    descriptor = None
    for klass in javaDsl_ExtendsInterfaces.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl_InterfaceDeclaration)


def test_javadsl_interfacedeclaration_constructor_exists():
    assert callable(javaDsl_InterfaceDeclaration.__init__)


def test_javadsl_interfacedeclaration_constructor_args():
    sig = inspect.signature(javaDsl_InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_javadsl_interfacedeclaration_has_name():
    assert hasattr(javaDsl_InterfaceDeclaration, "name")
    descriptor = None
    for klass in javaDsl_InterfaceDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_javadsl_interfacedeclaration_has_modifiers():
    assert hasattr(javaDsl_InterfaceDeclaration, "modifiers")
    descriptor = None
    for klass in javaDsl_InterfaceDeclaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_methoddeclarator_is_not_abstract():
    assert not inspect.isabstract(javaDsl_MethodDeclarator)


def test_javadsl_methoddeclarator_constructor_exists():
    assert callable(javaDsl_MethodDeclarator.__init__)


def test_javadsl_methoddeclarator_constructor_args():
    sig = inspect.signature(javaDsl_MethodDeclarator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javadsl_methoddeclarator_has_name():
    assert hasattr(javaDsl_MethodDeclarator, "name")
    descriptor = None
    for klass in javaDsl_MethodDeclarator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_resulttype_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ResultType)


def test_javadsl_resulttype_constructor_exists():
    assert callable(javaDsl_ResultType.__init__)


def test_javadsl_resulttype_constructor_args():
    sig = inspect.signature(javaDsl_ResultType.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_methodheader_is_not_abstract():
    assert not inspect.isabstract(javaDsl_MethodHeader)


def test_javadsl_methodheader_constructor_exists():
    assert callable(javaDsl_MethodHeader.__init__)


def test_javadsl_methodheader_constructor_args():
    sig = inspect.signature(javaDsl_MethodHeader.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_javadsl_methodheader_has_modifiers():
    assert hasattr(javaDsl_MethodHeader, "modifiers")
    descriptor = None
    for klass in javaDsl_MethodHeader.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_variabledeclarator_is_not_abstract():
    assert not inspect.isabstract(javaDsl_VariableDeclarator)


def test_javadsl_variabledeclarator_constructor_exists():
    assert callable(javaDsl_VariableDeclarator.__init__)


def test_javadsl_variabledeclarator_constructor_args():
    sig = inspect.signature(javaDsl_VariableDeclarator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javadsl_variabledeclarator_has_name():
    assert hasattr(javaDsl_VariableDeclarator, "name")
    descriptor = None
    for klass in javaDsl_VariableDeclarator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_argumentlist_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ArgumentList)


def test_javadsl_argumentlist_constructor_exists():
    assert callable(javaDsl_ArgumentList.__init__)


def test_javadsl_argumentlist_constructor_args():
    sig = inspect.signature(javaDsl_ArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_blockstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_BlockStatement)


def test_javadsl_blockstatement_constructor_exists():
    assert callable(javaDsl_BlockStatement.__init__)


def test_javadsl_blockstatement_constructor_args():
    sig = inspect.signature(javaDsl_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_explicitconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ExplicitConstructorInvocation)


def test_javadsl_explicitconstructorinvocation_constructor_exists():
    assert callable(javaDsl_ExplicitConstructorInvocation.__init__)


def test_javadsl_explicitconstructorinvocation_constructor_args():
    sig = inspect.signature(javaDsl_ExplicitConstructorInvocation.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_javadsl_explicitconstructorinvocation_has_keyword():
    assert hasattr(javaDsl_ExplicitConstructorInvocation, "keyword")
    descriptor = None
    for klass in javaDsl_ExplicitConstructorInvocation.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_type_is_not_abstract():
    assert not inspect.isabstract(javaDsl_Type)


def test_javadsl_type_constructor_exists():
    assert callable(javaDsl_Type.__init__)


def test_javadsl_type_constructor_args():
    sig = inspect.signature(javaDsl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javadsl_type_has_name():
    assert hasattr(javaDsl_Type, "name")
    descriptor = None
    for klass in javaDsl_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_formalparameter_is_not_abstract():
    assert not inspect.isabstract(javaDsl_FormalParameter)


def test_javadsl_formalparameter_constructor_exists():
    assert callable(javaDsl_FormalParameter.__init__)


def test_javadsl_formalparameter_constructor_args():
    sig = inspect.signature(javaDsl_FormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_javadsl_formalparameter_has_variable():
    assert hasattr(javaDsl_FormalParameter, "variable")
    descriptor = None
    for klass in javaDsl_FormalParameter.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_constructorbody_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ConstructorBody)


def test_javadsl_constructorbody_constructor_exists():
    assert callable(javaDsl_ConstructorBody.__init__)


def test_javadsl_constructorbody_constructor_args():
    sig = inspect.signature(javaDsl_ConstructorBody.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_exceptions_is_not_abstract():
    assert not inspect.isabstract(javaDsl_Exceptions)


def test_javadsl_exceptions_constructor_exists():
    assert callable(javaDsl_Exceptions.__init__)


def test_javadsl_exceptions_constructor_args():
    sig = inspect.signature(javaDsl_Exceptions.__init__)
    params = list(sig.parameters.keys())
    assert "exceptions" in params, "Missing parameter 'exceptions'"

def test_javadsl_exceptions_has_exceptions():
    assert hasattr(javaDsl_Exceptions, "exceptions")
    descriptor = None
    for klass in javaDsl_Exceptions.__mro__:
        if "exceptions" in klass.__dict__:
            descriptor = klass.__dict__["exceptions"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_constructordeclarator_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ConstructorDeclarator)


def test_javadsl_constructordeclarator_constructor_exists():
    assert callable(javaDsl_ConstructorDeclarator.__init__)


def test_javadsl_constructordeclarator_constructor_args():
    sig = inspect.signature(javaDsl_ConstructorDeclarator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javadsl_constructordeclarator_has_name():
    assert hasattr(javaDsl_ConstructorDeclarator, "name")
    descriptor = None
    for klass in javaDsl_ConstructorDeclarator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_block_is_not_abstract():
    assert not inspect.isabstract(javaDsl_Block)


def test_javadsl_block_constructor_exists():
    assert callable(javaDsl_Block.__init__)


def test_javadsl_block_constructor_args():
    sig = inspect.signature(javaDsl_Block.__init__)
    params = list(sig.parameters.keys())



def test_classbodydeclaration_is_not_abstract():
    assert not inspect.isabstract(ClassBodyDeclaration)


def test_classbodydeclaration_constructor_exists():
    assert callable(ClassBodyDeclaration.__init__)


def test_classbodydeclaration_constructor_args():
    sig = inspect.signature(ClassBodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_constructordeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ConstructorDeclaration)


def test_javadsl_constructordeclaration_constructor_exists():
    assert callable(javaDsl_ConstructorDeclaration.__init__)


def test_javadsl_constructordeclaration_constructor_args():
    sig = inspect.signature(javaDsl_ConstructorDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_javadsl_constructordeclaration_has_modifiers():
    assert hasattr(javaDsl_ConstructorDeclaration, "modifiers")
    descriptor = None
    for klass in javaDsl_ConstructorDeclaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_staticinitializer_is_not_abstract():
    assert not inspect.isabstract(javaDsl_StaticInitializer)


def test_javadsl_staticinitializer_constructor_exists():
    assert callable(javaDsl_StaticInitializer.__init__)


def test_javadsl_staticinitializer_constructor_args():
    sig = inspect.signature(javaDsl_StaticInitializer.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl_MethodDeclaration)


def test_javadsl_methoddeclaration_constructor_exists():
    assert callable(javaDsl_MethodDeclaration.__init__)


def test_javadsl_methoddeclaration_constructor_args():
    sig = inspect.signature(javaDsl_MethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl_FieldDeclaration)


def test_javadsl_fielddeclaration_constructor_exists():
    assert callable(javaDsl_FieldDeclaration.__init__)


def test_javadsl_fielddeclaration_constructor_args():
    sig = inspect.signature(javaDsl_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_javadsl_fielddeclaration_has_modifiers():
    assert hasattr(javaDsl_FieldDeclaration, "modifiers")
    descriptor = None
    for klass in javaDsl_FieldDeclaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_classmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ClassMemberDeclaration)


def test_javadsl_classmemberdeclaration_constructor_exists():
    assert callable(javaDsl_ClassMemberDeclaration.__init__)


def test_javadsl_classmemberdeclaration_constructor_args():
    sig = inspect.signature(javaDsl_ClassMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_expression_is_not_abstract():
    assert not inspect.isabstract(javaDsl_Expression)


def test_javadsl_expression_constructor_exists():
    assert callable(javaDsl_Expression.__init__)


def test_javadsl_expression_constructor_args():
    sig = inspect.signature(javaDsl_Expression.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_variableinitializer_is_not_abstract():
    assert not inspect.isabstract(javaDsl_VariableInitializer)


def test_javadsl_variableinitializer_constructor_exists():
    assert callable(javaDsl_VariableInitializer.__init__)


def test_javadsl_variableinitializer_constructor_args():
    sig = inspect.signature(javaDsl_VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_classbody_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ClassBody)


def test_javadsl_classbody_constructor_exists():
    assert callable(javaDsl_ClassBody.__init__)


def test_javadsl_classbody_constructor_args():
    sig = inspect.signature(javaDsl_ClassBody.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_interfaces_is_not_abstract():
    assert not inspect.isabstract(javaDsl_Interfaces)


def test_javadsl_interfaces_constructor_exists():
    assert callable(javaDsl_Interfaces.__init__)


def test_javadsl_interfaces_constructor_args():
    sig = inspect.signature(javaDsl_Interfaces.__init__)
    params = list(sig.parameters.keys())
    assert "interfaces" in params, "Missing parameter 'interfaces'"
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_javadsl_interfaces_has_interfaces():
    assert hasattr(javaDsl_Interfaces, "interfaces")
    descriptor = None
    for klass in javaDsl_Interfaces.__mro__:
        if "interfaces" in klass.__dict__:
            descriptor = klass.__dict__["interfaces"]
            break
    assert isinstance(descriptor, property)

def test_javadsl_interfaces_has_keyword():
    assert hasattr(javaDsl_Interfaces, "keyword")
    descriptor = None
    for klass in javaDsl_Interfaces.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ClassDeclaration)


def test_javadsl_classdeclaration_constructor_exists():
    assert callable(javaDsl_ClassDeclaration.__init__)


def test_javadsl_classdeclaration_constructor_args():
    sig = inspect.signature(javaDsl_ClassDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"
    assert "extend" in params, "Missing parameter 'extend'"
    assert "modifiers" in params, "Missing parameter 'modifiers'"

def test_javadsl_classdeclaration_has_className():
    assert hasattr(javaDsl_ClassDeclaration, "className")
    descriptor = None
    for klass in javaDsl_ClassDeclaration.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_javadsl_classdeclaration_has_extend():
    assert hasattr(javaDsl_ClassDeclaration, "extend")
    descriptor = None
    for klass in javaDsl_ClassDeclaration.__mro__:
        if "extend" in klass.__dict__:
            descriptor = klass.__dict__["extend"]
            break
    assert isinstance(descriptor, property)

def test_javadsl_classdeclaration_has_modifiers():
    assert hasattr(javaDsl_ClassDeclaration, "modifiers")
    descriptor = None
    for klass in javaDsl_ClassDeclaration.__mro__:
        if "modifiers" in klass.__dict__:
            descriptor = klass.__dict__["modifiers"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_eobject_is_not_abstract():
    assert not inspect.isabstract(javaDsl_EObject)


def test_javadsl_eobject_constructor_exists():
    assert callable(javaDsl_EObject.__init__)


def test_javadsl_eobject_constructor_args():
    sig = inspect.signature(javaDsl_EObject.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl_TypeDeclaration)


def test_javadsl_typedeclaration_constructor_exists():
    assert callable(javaDsl_TypeDeclaration.__init__)


def test_javadsl_typedeclaration_constructor_args():
    sig = inspect.signature(javaDsl_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "doc" in params, "Missing parameter 'doc'"

def test_javadsl_typedeclaration_has_doc():
    assert hasattr(javaDsl_TypeDeclaration, "doc")
    descriptor = None
    for klass in javaDsl_TypeDeclaration.__mro__:
        if "doc" in klass.__dict__:
            descriptor = klass.__dict__["doc"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_importstatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ImportStatement)


def test_javadsl_importstatement_constructor_exists():
    assert callable(javaDsl_ImportStatement.__init__)


def test_javadsl_importstatement_constructor_args():
    sig = inspect.signature(javaDsl_ImportStatement.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"
    assert "object" in params, "Missing parameter 'object'"

def test_javadsl_importstatement_has_package():
    assert hasattr(javaDsl_ImportStatement, "package")
    descriptor = None
    for klass in javaDsl_ImportStatement.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)

def test_javadsl_importstatement_has_object():
    assert hasattr(javaDsl_ImportStatement, "object")
    descriptor = None
    for klass in javaDsl_ImportStatement.__mro__:
        if "object" in klass.__dict__:
            descriptor = klass.__dict__["object"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_packagestatement_is_not_abstract():
    assert not inspect.isabstract(javaDsl_PackageStatement)


def test_javadsl_packagestatement_constructor_exists():
    assert callable(javaDsl_PackageStatement.__init__)


def test_javadsl_packagestatement_constructor_args():
    sig = inspect.signature(javaDsl_PackageStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javadsl_packagestatement_has_name():
    assert hasattr(javaDsl_PackageStatement, "name")
    descriptor = None
    for klass in javaDsl_PackageStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javadsl_compilationunit_is_not_abstract():
    assert not inspect.isabstract(javaDsl_CompilationUnit)


def test_javadsl_compilationunit_constructor_exists():
    assert callable(javaDsl_CompilationUnit.__init__)


def test_javadsl_compilationunit_constructor_args():
    sig = inspect.signature(javaDsl_CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_head_is_not_abstract():
    assert not inspect.isabstract(javaDsl_Head)


def test_javadsl_head_constructor_exists():
    assert callable(javaDsl_Head.__init__)


def test_javadsl_head_constructor_args():
    sig = inspect.signature(javaDsl_Head.__init__)
    params = list(sig.parameters.keys())



def test_javadsl_classbodydeclaration_is_not_abstract():
    assert not inspect.isabstract(javaDsl_ClassBodyDeclaration)


def test_javadsl_classbodydeclaration_constructor_exists():
    assert callable(javaDsl_ClassBodyDeclaration.__init__)


def test_javadsl_classbodydeclaration_constructor_args():
    sig = inspect.signature(javaDsl_ClassBodyDeclaration.__init__)
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
javaDsl_ArrayCreationExpression_strategy = st.builds(
    javaDsl_ArrayCreationExpression,
    layers=
        safe_text,
    type=
        safe_text
)
Primary_strategy = st.builds(
    Primary,
)
javaDsl_PrimaryNewArray_strategy = st.builds(
    javaDsl_PrimaryNewArray,
)
javaDsl_PrimaryNoNewArray_strategy = st.builds(
    javaDsl_PrimaryNoNewArray,
    literal=
        safe_text,
    method=
        safe_text,
    keyword=
        safe_text,
    reference=
        safe_text
)
javaDsl_ArrayExpression_strategy = st.builds(
    javaDsl_ArrayExpression,
)
LeftHandSide_strategy = st.builds(
    LeftHandSide,
)
javaDsl_ArrayAccess_strategy = st.builds(
    javaDsl_ArrayAccess,
    reference=
        safe_text
)
javaDsl_FieldAccess_strategy = st.builds(
    javaDsl_FieldAccess,
    keyword=
        safe_text,
    field=
        safe_text
)
javaDsl_Primary_strategy = st.builds(
    javaDsl_Primary,
    fields=
        safe_text
)
NoArrayExpression_strategy = st.builds(
    NoArrayExpression,
)
javaDsl_NoArrayExpressionWithoutMinus_strategy = st.builds(
    javaDsl_NoArrayExpressionWithoutMinus,
)
NoArrayExpressionWithoutMinus_strategy = st.builds(
    NoArrayExpressionWithoutMinus,
)
javaDsl_CastExpression_strategy = st.builds(
    javaDsl_CastExpression,
    type=
        safe_text
)
javaDsl_NoArrayExpression_strategy = st.builds(
    javaDsl_NoArrayExpression,
    operator=
        safe_text
)
javaDsl_MultiplicativeExpression_strategy = st.builds(
    javaDsl_MultiplicativeExpression,
    operators=
        safe_text
)
javaDsl_AdditiveExpression_strategy = st.builds(
    javaDsl_AdditiveExpression,
    operators=
        safe_text
)
javaDsl_ShiftExpression_strategy = st.builds(
    javaDsl_ShiftExpression,
    operators=
        safe_text
)
javaDsl_RelationalExpression_strategy = st.builds(
    javaDsl_RelationalExpression,
    operators=
        safe_text,
    classes=
        safe_text
)
javaDsl_EqualityExpression_strategy = st.builds(
    javaDsl_EqualityExpression,
    operators=
        safe_text
)
javaDsl_AndExpression_strategy = st.builds(
    javaDsl_AndExpression,
    operators=
        safe_text
)
javaDsl_ExclusiveOrExpression_strategy = st.builds(
    javaDsl_ExclusiveOrExpression,
    operators=
        safe_text
)
javaDsl_ConditionalAndExpression_strategy = st.builds(
    javaDsl_ConditionalAndExpression,
    operators=
        safe_text
)
javaDsl_ConditionalOrExpression_strategy = st.builds(
    javaDsl_ConditionalOrExpression,
    operators=
        safe_text
)
javaDsl_LeftHandSide_strategy = st.builds(
    javaDsl_LeftHandSide,
)
AssignmentExpression_strategy = st.builds(
    AssignmentExpression,
)
javaDsl_ConditionalExpression_strategy = st.builds(
    javaDsl_ConditionalExpression,
)
StatementExpression_strategy = st.builds(
    StatementExpression,
)
javaDsl_PostfixExpression_strategy = st.builds(
    javaDsl_PostfixExpression,
    reference=
        safe_text,
    operators=
        safe_text
)
javaDsl_MethodInvocation_strategy = st.builds(
    javaDsl_MethodInvocation,
    method=
        safe_text,
    keyword=
        safe_text
)
javaDsl_PreIncrementExpression_strategy = st.builds(
    javaDsl_PreIncrementExpression,
)
javaDsl_ClassInstanceCreationExpression_strategy = st.builds(
    javaDsl_ClassInstanceCreationExpression,
    type=
        safe_text
)
javaDsl_PreDecrementExpression_strategy = st.builds(
    javaDsl_PreDecrementExpression,
)
javaDsl_Assignment_strategy = st.builds(
    javaDsl_Assignment,
    operator=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
javaDsl_AssignmentExpression_strategy = st.builds(
    javaDsl_AssignmentExpression,
)
PrimaryNoNewArray_strategy = st.builds(
    PrimaryNoNewArray,
)
ConstantExpression_strategy = st.builds(
    ConstantExpression,
)
javaDsl_InclusiveOrExpression_strategy = st.builds(
    javaDsl_InclusiveOrExpression,
    operators=
        safe_text
)
javaDsl_ForUpdate_strategy = st.builds(
    javaDsl_ForUpdate,
)
javaDsl_ForInit_strategy = st.builds(
    javaDsl_ForInit,
)
javaDsl_ConstantExpression_strategy = st.builds(
    javaDsl_ConstantExpression,
)
BlockStatement_strategy = st.builds(
    BlockStatement,
)
javaDsl_Statement_strategy = st.builds(
    javaDsl_Statement,
)
javaDsl_LocalVariableDeclaration_strategy = st.builds(
    javaDsl_LocalVariableDeclaration,
)
Statement_strategy = st.builds(
    Statement,
)
javaDsl_ReturnStatement_strategy = st.builds(
    javaDsl_ReturnStatement,
)
javaDsl_IfStatement_strategy = st.builds(
    javaDsl_IfStatement,
    condition=
        st.booleans()
)
javaDsl_BreakStatement_strategy = st.builds(
    javaDsl_BreakStatement,
    reference=
        safe_text
)
javaDsl_WhileStatement_strategy = st.builds(
    javaDsl_WhileStatement,
    condition=
        st.booleans()
)
javaDsl_StatementExpression_strategy = st.builds(
    javaDsl_StatementExpression,
)
javaDsl_ThrowsStatement_strategy = st.builds(
    javaDsl_ThrowsStatement,
)
javaDsl_ContinueStatement_strategy = st.builds(
    javaDsl_ContinueStatement,
    reference=
        safe_text
)
javaDsl_SynchronizedStatement_strategy = st.builds(
    javaDsl_SynchronizedStatement,
)
javaDsl_SwitchStatement_strategy = st.builds(
    javaDsl_SwitchStatement,
)
javaDsl_DoStatement_strategy = st.builds(
    javaDsl_DoStatement,
    condition=
        st.booleans()
)
javaDsl_TryStatement_strategy = st.builds(
    javaDsl_TryStatement,
)
javaDsl_ForStatement_strategy = st.builds(
    javaDsl_ForStatement,
    condition=
        st.booleans()
)
javaDsl_LabeledStatement_strategy = st.builds(
    javaDsl_LabeledStatement,
    label=
        safe_text
)
VariableInitializer_strategy = st.builds(
    VariableInitializer,
)
javaDsl_ArrayInitializer_strategy = st.builds(
    javaDsl_ArrayInitializer,
)
InterfaceMemberDeclaration_strategy = st.builds(
    InterfaceMemberDeclaration,
)
javaDsl_AbstractMethodDeclaration_strategy = st.builds(
    javaDsl_AbstractMethodDeclaration,
)
javaDsl_ConstantDeclaration_strategy = st.builds(
    javaDsl_ConstantDeclaration,
)
javaDsl_InterfaceMemberDeclaration_strategy = st.builds(
    javaDsl_InterfaceMemberDeclaration,
    modifiers=
        safe_text
)
javaDsl_InterfaceBody_strategy = st.builds(
    javaDsl_InterfaceBody,
)
javaDsl_ExtendsInterfaces_strategy = st.builds(
    javaDsl_ExtendsInterfaces,
    interfaces=
        safe_text,
    keyword=
        safe_text
)
javaDsl_InterfaceDeclaration_strategy = st.builds(
    javaDsl_InterfaceDeclaration,
    name=
        safe_text,
    modifiers=
        safe_text
)
javaDsl_MethodDeclarator_strategy = st.builds(
    javaDsl_MethodDeclarator,
    name=
        safe_text
)
javaDsl_ResultType_strategy = st.builds(
    javaDsl_ResultType,
)
javaDsl_MethodHeader_strategy = st.builds(
    javaDsl_MethodHeader,
    modifiers=
        safe_text
)
javaDsl_VariableDeclarator_strategy = st.builds(
    javaDsl_VariableDeclarator,
    name=
        safe_text
)
javaDsl_ArgumentList_strategy = st.builds(
    javaDsl_ArgumentList,
)
javaDsl_BlockStatement_strategy = st.builds(
    javaDsl_BlockStatement,
)
javaDsl_ExplicitConstructorInvocation_strategy = st.builds(
    javaDsl_ExplicitConstructorInvocation,
    keyword=
        safe_text
)
javaDsl_Type_strategy = st.builds(
    javaDsl_Type,
    name=
        safe_text
)
javaDsl_FormalParameter_strategy = st.builds(
    javaDsl_FormalParameter,
    variable=
        safe_text
)
javaDsl_ConstructorBody_strategy = st.builds(
    javaDsl_ConstructorBody,
)
javaDsl_Exceptions_strategy = st.builds(
    javaDsl_Exceptions,
    exceptions=
        safe_text
)
javaDsl_ConstructorDeclarator_strategy = st.builds(
    javaDsl_ConstructorDeclarator,
    name=
        safe_text
)
javaDsl_Block_strategy = st.builds(
    javaDsl_Block,
)
ClassBodyDeclaration_strategy = st.builds(
    ClassBodyDeclaration,
)
javaDsl_ConstructorDeclaration_strategy = st.builds(
    javaDsl_ConstructorDeclaration,
    modifiers=
        safe_text
)
javaDsl_StaticInitializer_strategy = st.builds(
    javaDsl_StaticInitializer,
)
javaDsl_MethodDeclaration_strategy = st.builds(
    javaDsl_MethodDeclaration,
)
javaDsl_FieldDeclaration_strategy = st.builds(
    javaDsl_FieldDeclaration,
    modifiers=
        safe_text
)
javaDsl_ClassMemberDeclaration_strategy = st.builds(
    javaDsl_ClassMemberDeclaration,
)
javaDsl_Expression_strategy = st.builds(
    javaDsl_Expression,
)
javaDsl_VariableInitializer_strategy = st.builds(
    javaDsl_VariableInitializer,
)
javaDsl_ClassBody_strategy = st.builds(
    javaDsl_ClassBody,
)
javaDsl_Interfaces_strategy = st.builds(
    javaDsl_Interfaces,
    interfaces=
        safe_text,
    keyword=
        safe_text
)
javaDsl_ClassDeclaration_strategy = st.builds(
    javaDsl_ClassDeclaration,
    className=
        safe_text,
    extend=
        safe_text,
    modifiers=
        safe_text
)
javaDsl_EObject_strategy = st.builds(
    javaDsl_EObject,
)
javaDsl_TypeDeclaration_strategy = st.builds(
    javaDsl_TypeDeclaration,
    doc=
        safe_text
)
javaDsl_ImportStatement_strategy = st.builds(
    javaDsl_ImportStatement,
    package=
        safe_text,
    object=
        safe_text
)
javaDsl_PackageStatement_strategy = st.builds(
    javaDsl_PackageStatement,
    name=
        safe_text
)
javaDsl_CompilationUnit_strategy = st.builds(
    javaDsl_CompilationUnit,
)
javaDsl_Head_strategy = st.builds(
    javaDsl_Head,
)
javaDsl_ClassBodyDeclaration_strategy = st.builds(
    javaDsl_ClassBodyDeclaration,
)

@given(instance=javaDsl_ArrayCreationExpression_strategy)
@settings(max_examples=50)
def test_javadsl_arraycreationexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_ArrayCreationExpression)



@given(instance=javaDsl_ArrayCreationExpression_strategy)
def test_javadsl_arraycreationexpression_layers_setter(instance):
    original = instance.layers
    instance.layers = original
    assert instance.layers == original



@given(instance=javaDsl_ArrayCreationExpression_strategy)
def test_javadsl_arraycreationexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Primary_strategy)
@settings(max_examples=50)
def test_primary_instantiation(instance):
    assert isinstance(instance, Primary)

@given(instance=javaDsl_PrimaryNewArray_strategy)
@settings(max_examples=50)
def test_javadsl_primarynewarray_instantiation(instance):
    assert isinstance(instance, javaDsl_PrimaryNewArray)

@given(instance=javaDsl_PrimaryNoNewArray_strategy)
@settings(max_examples=50)
def test_javadsl_primarynonewarray_instantiation(instance):
    assert isinstance(instance, javaDsl_PrimaryNoNewArray)



@given(instance=javaDsl_PrimaryNoNewArray_strategy)
def test_javadsl_primarynonewarray_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original



@given(instance=javaDsl_PrimaryNoNewArray_strategy)
def test_javadsl_primarynonewarray_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original



@given(instance=javaDsl_PrimaryNoNewArray_strategy)
def test_javadsl_primarynonewarray_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original



@given(instance=javaDsl_PrimaryNoNewArray_strategy)
def test_javadsl_primarynonewarray_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=javaDsl_ArrayExpression_strategy)
@settings(max_examples=50)
def test_javadsl_arrayexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_ArrayExpression)

@given(instance=LeftHandSide_strategy)
@settings(max_examples=50)
def test_lefthandside_instantiation(instance):
    assert isinstance(instance, LeftHandSide)

@given(instance=javaDsl_ArrayAccess_strategy)
@settings(max_examples=50)
def test_javadsl_arrayaccess_instantiation(instance):
    assert isinstance(instance, javaDsl_ArrayAccess)



@given(instance=javaDsl_ArrayAccess_strategy)
def test_javadsl_arrayaccess_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=javaDsl_FieldAccess_strategy)
@settings(max_examples=50)
def test_javadsl_fieldaccess_instantiation(instance):
    assert isinstance(instance, javaDsl_FieldAccess)



@given(instance=javaDsl_FieldAccess_strategy)
def test_javadsl_fieldaccess_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original



@given(instance=javaDsl_FieldAccess_strategy)
def test_javadsl_fieldaccess_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=javaDsl_Primary_strategy)
@settings(max_examples=50)
def test_javadsl_primary_instantiation(instance):
    assert isinstance(instance, javaDsl_Primary)



@given(instance=javaDsl_Primary_strategy)
def test_javadsl_primary_fields_setter(instance):
    original = instance.fields
    instance.fields = original
    assert instance.fields == original

@given(instance=NoArrayExpression_strategy)
@settings(max_examples=50)
def test_noarrayexpression_instantiation(instance):
    assert isinstance(instance, NoArrayExpression)

@given(instance=javaDsl_NoArrayExpressionWithoutMinus_strategy)
@settings(max_examples=50)
def test_javadsl_noarrayexpressionwithoutminus_instantiation(instance):
    assert isinstance(instance, javaDsl_NoArrayExpressionWithoutMinus)

@given(instance=NoArrayExpressionWithoutMinus_strategy)
@settings(max_examples=50)
def test_noarrayexpressionwithoutminus_instantiation(instance):
    assert isinstance(instance, NoArrayExpressionWithoutMinus)

@given(instance=javaDsl_CastExpression_strategy)
@settings(max_examples=50)
def test_javadsl_castexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_CastExpression)



@given(instance=javaDsl_CastExpression_strategy)
def test_javadsl_castexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=javaDsl_NoArrayExpression_strategy)
@settings(max_examples=50)
def test_javadsl_noarrayexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_NoArrayExpression)



@given(instance=javaDsl_NoArrayExpression_strategy)
def test_javadsl_noarrayexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=javaDsl_MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_javadsl_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_MultiplicativeExpression)



@given(instance=javaDsl_MultiplicativeExpression_strategy)
def test_javadsl_multiplicativeexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl_AdditiveExpression_strategy)
@settings(max_examples=50)
def test_javadsl_additiveexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_AdditiveExpression)



@given(instance=javaDsl_AdditiveExpression_strategy)
def test_javadsl_additiveexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl_ShiftExpression_strategy)
@settings(max_examples=50)
def test_javadsl_shiftexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_ShiftExpression)



@given(instance=javaDsl_ShiftExpression_strategy)
def test_javadsl_shiftexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl_RelationalExpression_strategy)
@settings(max_examples=50)
def test_javadsl_relationalexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_RelationalExpression)



@given(instance=javaDsl_RelationalExpression_strategy)
def test_javadsl_relationalexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original



@given(instance=javaDsl_RelationalExpression_strategy)
def test_javadsl_relationalexpression_classes_setter(instance):
    original = instance.classes
    instance.classes = original
    assert instance.classes == original

@given(instance=javaDsl_EqualityExpression_strategy)
@settings(max_examples=50)
def test_javadsl_equalityexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_EqualityExpression)



@given(instance=javaDsl_EqualityExpression_strategy)
def test_javadsl_equalityexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl_AndExpression_strategy)
@settings(max_examples=50)
def test_javadsl_andexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_AndExpression)



@given(instance=javaDsl_AndExpression_strategy)
def test_javadsl_andexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl_ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_javadsl_exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_ExclusiveOrExpression)



@given(instance=javaDsl_ExclusiveOrExpression_strategy)
def test_javadsl_exclusiveorexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl_ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_javadsl_conditionalandexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_ConditionalAndExpression)



@given(instance=javaDsl_ConditionalAndExpression_strategy)
def test_javadsl_conditionalandexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl_ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_javadsl_conditionalorexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_ConditionalOrExpression)



@given(instance=javaDsl_ConditionalOrExpression_strategy)
def test_javadsl_conditionalorexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl_LeftHandSide_strategy)
@settings(max_examples=50)
def test_javadsl_lefthandside_instantiation(instance):
    assert isinstance(instance, javaDsl_LeftHandSide)

@given(instance=AssignmentExpression_strategy)
@settings(max_examples=50)
def test_assignmentexpression_instantiation(instance):
    assert isinstance(instance, AssignmentExpression)

@given(instance=javaDsl_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_javadsl_conditionalexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_ConditionalExpression)

@given(instance=StatementExpression_strategy)
@settings(max_examples=50)
def test_statementexpression_instantiation(instance):
    assert isinstance(instance, StatementExpression)

@given(instance=javaDsl_PostfixExpression_strategy)
@settings(max_examples=50)
def test_javadsl_postfixexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_PostfixExpression)



@given(instance=javaDsl_PostfixExpression_strategy)
def test_javadsl_postfixexpression_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original



@given(instance=javaDsl_PostfixExpression_strategy)
def test_javadsl_postfixexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl_MethodInvocation_strategy)
@settings(max_examples=50)
def test_javadsl_methodinvocation_instantiation(instance):
    assert isinstance(instance, javaDsl_MethodInvocation)



@given(instance=javaDsl_MethodInvocation_strategy)
def test_javadsl_methodinvocation_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original



@given(instance=javaDsl_MethodInvocation_strategy)
def test_javadsl_methodinvocation_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=javaDsl_PreIncrementExpression_strategy)
@settings(max_examples=50)
def test_javadsl_preincrementexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_PreIncrementExpression)

@given(instance=javaDsl_ClassInstanceCreationExpression_strategy)
@settings(max_examples=50)
def test_javadsl_classinstancecreationexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_ClassInstanceCreationExpression)



@given(instance=javaDsl_ClassInstanceCreationExpression_strategy)
def test_javadsl_classinstancecreationexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=javaDsl_PreDecrementExpression_strategy)
@settings(max_examples=50)
def test_javadsl_predecrementexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_PreDecrementExpression)

@given(instance=javaDsl_Assignment_strategy)
@settings(max_examples=50)
def test_javadsl_assignment_instantiation(instance):
    assert isinstance(instance, javaDsl_Assignment)



@given(instance=javaDsl_Assignment_strategy)
def test_javadsl_assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=javaDsl_AssignmentExpression_strategy)
@settings(max_examples=50)
def test_javadsl_assignmentexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_AssignmentExpression)

@given(instance=PrimaryNoNewArray_strategy)
@settings(max_examples=50)
def test_primarynonewarray_instantiation(instance):
    assert isinstance(instance, PrimaryNoNewArray)

@given(instance=ConstantExpression_strategy)
@settings(max_examples=50)
def test_constantexpression_instantiation(instance):
    assert isinstance(instance, ConstantExpression)

@given(instance=javaDsl_InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_javadsl_inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_InclusiveOrExpression)



@given(instance=javaDsl_InclusiveOrExpression_strategy)
def test_javadsl_inclusiveorexpression_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original

@given(instance=javaDsl_ForUpdate_strategy)
@settings(max_examples=50)
def test_javadsl_forupdate_instantiation(instance):
    assert isinstance(instance, javaDsl_ForUpdate)

@given(instance=javaDsl_ForInit_strategy)
@settings(max_examples=50)
def test_javadsl_forinit_instantiation(instance):
    assert isinstance(instance, javaDsl_ForInit)

@given(instance=javaDsl_ConstantExpression_strategy)
@settings(max_examples=50)
def test_javadsl_constantexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_ConstantExpression)

@given(instance=BlockStatement_strategy)
@settings(max_examples=50)
def test_blockstatement_instantiation(instance):
    assert isinstance(instance, BlockStatement)

@given(instance=javaDsl_Statement_strategy)
@settings(max_examples=50)
def test_javadsl_statement_instantiation(instance):
    assert isinstance(instance, javaDsl_Statement)

@given(instance=javaDsl_LocalVariableDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl_localvariabledeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl_LocalVariableDeclaration)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=javaDsl_ReturnStatement_strategy)
@settings(max_examples=50)
def test_javadsl_returnstatement_instantiation(instance):
    assert isinstance(instance, javaDsl_ReturnStatement)

@given(instance=javaDsl_IfStatement_strategy)
@settings(max_examples=50)
def test_javadsl_ifstatement_instantiation(instance):
    assert isinstance(instance, javaDsl_IfStatement)



@given(instance=javaDsl_IfStatement_strategy)
def test_javadsl_ifstatement_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=javaDsl_BreakStatement_strategy)
@settings(max_examples=50)
def test_javadsl_breakstatement_instantiation(instance):
    assert isinstance(instance, javaDsl_BreakStatement)



@given(instance=javaDsl_BreakStatement_strategy)
def test_javadsl_breakstatement_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=javaDsl_WhileStatement_strategy)
@settings(max_examples=50)
def test_javadsl_whilestatement_instantiation(instance):
    assert isinstance(instance, javaDsl_WhileStatement)



@given(instance=javaDsl_WhileStatement_strategy)
def test_javadsl_whilestatement_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=javaDsl_StatementExpression_strategy)
@settings(max_examples=50)
def test_javadsl_statementexpression_instantiation(instance):
    assert isinstance(instance, javaDsl_StatementExpression)

@given(instance=javaDsl_ThrowsStatement_strategy)
@settings(max_examples=50)
def test_javadsl_throwsstatement_instantiation(instance):
    assert isinstance(instance, javaDsl_ThrowsStatement)

@given(instance=javaDsl_ContinueStatement_strategy)
@settings(max_examples=50)
def test_javadsl_continuestatement_instantiation(instance):
    assert isinstance(instance, javaDsl_ContinueStatement)



@given(instance=javaDsl_ContinueStatement_strategy)
def test_javadsl_continuestatement_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=javaDsl_SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_javadsl_synchronizedstatement_instantiation(instance):
    assert isinstance(instance, javaDsl_SynchronizedStatement)

@given(instance=javaDsl_SwitchStatement_strategy)
@settings(max_examples=50)
def test_javadsl_switchstatement_instantiation(instance):
    assert isinstance(instance, javaDsl_SwitchStatement)

@given(instance=javaDsl_DoStatement_strategy)
@settings(max_examples=50)
def test_javadsl_dostatement_instantiation(instance):
    assert isinstance(instance, javaDsl_DoStatement)



@given(instance=javaDsl_DoStatement_strategy)
def test_javadsl_dostatement_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=javaDsl_TryStatement_strategy)
@settings(max_examples=50)
def test_javadsl_trystatement_instantiation(instance):
    assert isinstance(instance, javaDsl_TryStatement)

@given(instance=javaDsl_ForStatement_strategy)
@settings(max_examples=50)
def test_javadsl_forstatement_instantiation(instance):
    assert isinstance(instance, javaDsl_ForStatement)



@given(instance=javaDsl_ForStatement_strategy)
def test_javadsl_forstatement_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=javaDsl_LabeledStatement_strategy)
@settings(max_examples=50)
def test_javadsl_labeledstatement_instantiation(instance):
    assert isinstance(instance, javaDsl_LabeledStatement)



@given(instance=javaDsl_LabeledStatement_strategy)
def test_javadsl_labeledstatement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=VariableInitializer_strategy)
@settings(max_examples=50)
def test_variableinitializer_instantiation(instance):
    assert isinstance(instance, VariableInitializer)

@given(instance=javaDsl_ArrayInitializer_strategy)
@settings(max_examples=50)
def test_javadsl_arrayinitializer_instantiation(instance):
    assert isinstance(instance, javaDsl_ArrayInitializer)

@given(instance=InterfaceMemberDeclaration_strategy)
@settings(max_examples=50)
def test_interfacememberdeclaration_instantiation(instance):
    assert isinstance(instance, InterfaceMemberDeclaration)

@given(instance=javaDsl_AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl_abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl_AbstractMethodDeclaration)

@given(instance=javaDsl_ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl_constantdeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl_ConstantDeclaration)

@given(instance=javaDsl_InterfaceMemberDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl_interfacememberdeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl_InterfaceMemberDeclaration)



@given(instance=javaDsl_InterfaceMemberDeclaration_strategy)
def test_javadsl_interfacememberdeclaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=javaDsl_InterfaceBody_strategy)
@settings(max_examples=50)
def test_javadsl_interfacebody_instantiation(instance):
    assert isinstance(instance, javaDsl_InterfaceBody)

@given(instance=javaDsl_ExtendsInterfaces_strategy)
@settings(max_examples=50)
def test_javadsl_extendsinterfaces_instantiation(instance):
    assert isinstance(instance, javaDsl_ExtendsInterfaces)



@given(instance=javaDsl_ExtendsInterfaces_strategy)
def test_javadsl_extendsinterfaces_interfaces_setter(instance):
    original = instance.interfaces
    instance.interfaces = original
    assert instance.interfaces == original



@given(instance=javaDsl_ExtendsInterfaces_strategy)
def test_javadsl_extendsinterfaces_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=javaDsl_InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl_interfacedeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl_InterfaceDeclaration)



@given(instance=javaDsl_InterfaceDeclaration_strategy)
def test_javadsl_interfacedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=javaDsl_InterfaceDeclaration_strategy)
def test_javadsl_interfacedeclaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=javaDsl_MethodDeclarator_strategy)
@settings(max_examples=50)
def test_javadsl_methoddeclarator_instantiation(instance):
    assert isinstance(instance, javaDsl_MethodDeclarator)



@given(instance=javaDsl_MethodDeclarator_strategy)
def test_javadsl_methoddeclarator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=javaDsl_ResultType_strategy)
@settings(max_examples=50)
def test_javadsl_resulttype_instantiation(instance):
    assert isinstance(instance, javaDsl_ResultType)

@given(instance=javaDsl_MethodHeader_strategy)
@settings(max_examples=50)
def test_javadsl_methodheader_instantiation(instance):
    assert isinstance(instance, javaDsl_MethodHeader)



@given(instance=javaDsl_MethodHeader_strategy)
def test_javadsl_methodheader_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=javaDsl_VariableDeclarator_strategy)
@settings(max_examples=50)
def test_javadsl_variabledeclarator_instantiation(instance):
    assert isinstance(instance, javaDsl_VariableDeclarator)



@given(instance=javaDsl_VariableDeclarator_strategy)
def test_javadsl_variabledeclarator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=javaDsl_ArgumentList_strategy)
@settings(max_examples=50)
def test_javadsl_argumentlist_instantiation(instance):
    assert isinstance(instance, javaDsl_ArgumentList)

@given(instance=javaDsl_BlockStatement_strategy)
@settings(max_examples=50)
def test_javadsl_blockstatement_instantiation(instance):
    assert isinstance(instance, javaDsl_BlockStatement)

@given(instance=javaDsl_ExplicitConstructorInvocation_strategy)
@settings(max_examples=50)
def test_javadsl_explicitconstructorinvocation_instantiation(instance):
    assert isinstance(instance, javaDsl_ExplicitConstructorInvocation)



@given(instance=javaDsl_ExplicitConstructorInvocation_strategy)
def test_javadsl_explicitconstructorinvocation_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=javaDsl_Type_strategy)
@settings(max_examples=50)
def test_javadsl_type_instantiation(instance):
    assert isinstance(instance, javaDsl_Type)



@given(instance=javaDsl_Type_strategy)
def test_javadsl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=javaDsl_FormalParameter_strategy)
@settings(max_examples=50)
def test_javadsl_formalparameter_instantiation(instance):
    assert isinstance(instance, javaDsl_FormalParameter)



@given(instance=javaDsl_FormalParameter_strategy)
def test_javadsl_formalparameter_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=javaDsl_ConstructorBody_strategy)
@settings(max_examples=50)
def test_javadsl_constructorbody_instantiation(instance):
    assert isinstance(instance, javaDsl_ConstructorBody)

@given(instance=javaDsl_Exceptions_strategy)
@settings(max_examples=50)
def test_javadsl_exceptions_instantiation(instance):
    assert isinstance(instance, javaDsl_Exceptions)



@given(instance=javaDsl_Exceptions_strategy)
def test_javadsl_exceptions_exceptions_setter(instance):
    original = instance.exceptions
    instance.exceptions = original
    assert instance.exceptions == original

@given(instance=javaDsl_ConstructorDeclarator_strategy)
@settings(max_examples=50)
def test_javadsl_constructordeclarator_instantiation(instance):
    assert isinstance(instance, javaDsl_ConstructorDeclarator)



@given(instance=javaDsl_ConstructorDeclarator_strategy)
def test_javadsl_constructordeclarator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=javaDsl_Block_strategy)
@settings(max_examples=50)
def test_javadsl_block_instantiation(instance):
    assert isinstance(instance, javaDsl_Block)

@given(instance=ClassBodyDeclaration_strategy)
@settings(max_examples=50)
def test_classbodydeclaration_instantiation(instance):
    assert isinstance(instance, ClassBodyDeclaration)

@given(instance=javaDsl_ConstructorDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl_constructordeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl_ConstructorDeclaration)



@given(instance=javaDsl_ConstructorDeclaration_strategy)
def test_javadsl_constructordeclaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=javaDsl_StaticInitializer_strategy)
@settings(max_examples=50)
def test_javadsl_staticinitializer_instantiation(instance):
    assert isinstance(instance, javaDsl_StaticInitializer)

@given(instance=javaDsl_MethodDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl_methoddeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl_MethodDeclaration)

@given(instance=javaDsl_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl_fielddeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl_FieldDeclaration)



@given(instance=javaDsl_FieldDeclaration_strategy)
def test_javadsl_fielddeclaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=javaDsl_ClassMemberDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl_classmemberdeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl_ClassMemberDeclaration)

@given(instance=javaDsl_Expression_strategy)
@settings(max_examples=50)
def test_javadsl_expression_instantiation(instance):
    assert isinstance(instance, javaDsl_Expression)

@given(instance=javaDsl_VariableInitializer_strategy)
@settings(max_examples=50)
def test_javadsl_variableinitializer_instantiation(instance):
    assert isinstance(instance, javaDsl_VariableInitializer)

@given(instance=javaDsl_ClassBody_strategy)
@settings(max_examples=50)
def test_javadsl_classbody_instantiation(instance):
    assert isinstance(instance, javaDsl_ClassBody)

@given(instance=javaDsl_Interfaces_strategy)
@settings(max_examples=50)
def test_javadsl_interfaces_instantiation(instance):
    assert isinstance(instance, javaDsl_Interfaces)



@given(instance=javaDsl_Interfaces_strategy)
def test_javadsl_interfaces_interfaces_setter(instance):
    original = instance.interfaces
    instance.interfaces = original
    assert instance.interfaces == original



@given(instance=javaDsl_Interfaces_strategy)
def test_javadsl_interfaces_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=javaDsl_ClassDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl_classdeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl_ClassDeclaration)



@given(instance=javaDsl_ClassDeclaration_strategy)
def test_javadsl_classdeclaration_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original



@given(instance=javaDsl_ClassDeclaration_strategy)
def test_javadsl_classdeclaration_extend_setter(instance):
    original = instance.extend
    instance.extend = original
    assert instance.extend == original



@given(instance=javaDsl_ClassDeclaration_strategy)
def test_javadsl_classdeclaration_modifiers_setter(instance):
    original = instance.modifiers
    instance.modifiers = original
    assert instance.modifiers == original

@given(instance=javaDsl_EObject_strategy)
@settings(max_examples=50)
def test_javadsl_eobject_instantiation(instance):
    assert isinstance(instance, javaDsl_EObject)

@given(instance=javaDsl_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl_typedeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl_TypeDeclaration)



@given(instance=javaDsl_TypeDeclaration_strategy)
def test_javadsl_typedeclaration_doc_setter(instance):
    original = instance.doc
    instance.doc = original
    assert instance.doc == original

@given(instance=javaDsl_ImportStatement_strategy)
@settings(max_examples=50)
def test_javadsl_importstatement_instantiation(instance):
    assert isinstance(instance, javaDsl_ImportStatement)



@given(instance=javaDsl_ImportStatement_strategy)
def test_javadsl_importstatement_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original



@given(instance=javaDsl_ImportStatement_strategy)
def test_javadsl_importstatement_object_setter(instance):
    original = instance.object
    instance.object = original
    assert instance.object == original

@given(instance=javaDsl_PackageStatement_strategy)
@settings(max_examples=50)
def test_javadsl_packagestatement_instantiation(instance):
    assert isinstance(instance, javaDsl_PackageStatement)



@given(instance=javaDsl_PackageStatement_strategy)
def test_javadsl_packagestatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=javaDsl_CompilationUnit_strategy)
@settings(max_examples=50)
def test_javadsl_compilationunit_instantiation(instance):
    assert isinstance(instance, javaDsl_CompilationUnit)

@given(instance=javaDsl_Head_strategy)
@settings(max_examples=50)
def test_javadsl_head_instantiation(instance):
    assert isinstance(instance, javaDsl_Head)

@given(instance=javaDsl_ClassBodyDeclaration_strategy)
@settings(max_examples=50)
def test_javadsl_classbodydeclaration_instantiation(instance):
    assert isinstance(instance, javaDsl_ClassBodyDeclaration)
