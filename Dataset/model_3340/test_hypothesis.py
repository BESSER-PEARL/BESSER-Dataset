import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    JavaSimplified_MethodCall,
    JavaSimplified_TypedElement,
    JavaSimplified_StringElement,
    JavaSimplified_NamedElement,
    Feature,
    TypedElement,
    JavaSimplified_Field,
    NamedElement,
    JavaSimplified_Parameter,
    CommentedElement,
    JavaSimplified_JavaModel,
    JavaSimplified_Method,
    JavaSimplified_JavaClass,
    Expression,
    JavaSimplified_Name,
    JavaSimplified_ThisExpression,
    JavaSimplified_FieldAccess,
    JavaSimplified_Literal,
    JavaSimplified_InfixExpression,
    JavaSimplified_MethodInvocation,
    JavaSimplified_Assignment,
    Statement,
    JavaSimplified_ReturnStatement,
    JavaSimplified_IfStatement,
    JavaSimplified_ExpressionStatement,
    JavaSimplified_VariableDeclarationStatement,
    JavaSimplified_CommentStatement,
    JavaSimplified_CommentedElement,
    StringElement,
    JavaSimplified_Expression,
    JavaSimplified_Feature,
    JavaSimplified_Statement,
    JavaSimplified_Comment,
    JavaSimplified_ClassInstanceCreation,
    JavaSimplified_Type,
    JavaSimplified_CastExpression,
    InfixOperatorType,
    VisibilityType,
    LiteralType,
    AssignmentOperatorType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_javasimplified_methodcall_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_MethodCall)


def test_javasimplified_methodcall_constructor_exists():
    assert callable(JavaSimplified_MethodCall.__init__)


def test_javasimplified_methodcall_constructor_args():
    sig = inspect.signature(JavaSimplified_MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_typedelement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_TypedElement)


def test_javasimplified_typedelement_constructor_exists():
    assert callable(JavaSimplified_TypedElement.__init__)


def test_javasimplified_typedelement_constructor_args():
    sig = inspect.signature(JavaSimplified_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_stringelement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_StringElement)


def test_javasimplified_stringelement_constructor_exists():
    assert callable(JavaSimplified_StringElement.__init__)


def test_javasimplified_stringelement_constructor_args():
    sig = inspect.signature(JavaSimplified_StringElement.__init__)
    params = list(sig.parameters.keys())
    assert "strValue" in params, "Missing parameter 'strValue'"

def test_javasimplified_stringelement_has_strValue():
    assert hasattr(JavaSimplified_StringElement, "strValue")
    descriptor = None
    for klass in JavaSimplified_StringElement.__mro__:
        if "strValue" in klass.__dict__:
            descriptor = klass.__dict__["strValue"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified_namedelement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_NamedElement)


def test_javasimplified_namedelement_constructor_exists():
    assert callable(JavaSimplified_NamedElement.__init__)


def test_javasimplified_namedelement_constructor_args():
    sig = inspect.signature(JavaSimplified_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_field_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_Field)


def test_javasimplified_field_constructor_exists():
    assert callable(JavaSimplified_Field.__init__)


def test_javasimplified_field_constructor_args():
    sig = inspect.signature(JavaSimplified_Field.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_parameter_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_Parameter)


def test_javasimplified_parameter_constructor_exists():
    assert callable(JavaSimplified_Parameter.__init__)


def test_javasimplified_parameter_constructor_args():
    sig = inspect.signature(JavaSimplified_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_commentedelement_is_not_abstract():
    assert not inspect.isabstract(CommentedElement)


def test_commentedelement_constructor_exists():
    assert callable(CommentedElement.__init__)


def test_commentedelement_constructor_args():
    sig = inspect.signature(CommentedElement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_javamodel_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_JavaModel)


def test_javasimplified_javamodel_constructor_exists():
    assert callable(JavaSimplified_JavaModel.__init__)


def test_javasimplified_javamodel_constructor_args():
    sig = inspect.signature(JavaSimplified_JavaModel.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_method_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_Method)


def test_javasimplified_method_constructor_exists():
    assert callable(JavaSimplified_Method.__init__)


def test_javasimplified_method_constructor_args():
    sig = inspect.signature(JavaSimplified_Method.__init__)
    params = list(sig.parameters.keys())
    assert "exceptions" in params, "Missing parameter 'exceptions'"

def test_javasimplified_method_has_exceptions():
    assert hasattr(JavaSimplified_Method, "exceptions")
    descriptor = None
    for klass in JavaSimplified_Method.__mro__:
        if "exceptions" in klass.__dict__:
            descriptor = klass.__dict__["exceptions"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified_javaclass_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_JavaClass)


def test_javasimplified_javaclass_constructor_exists():
    assert callable(JavaSimplified_JavaClass.__init__)


def test_javasimplified_javaclass_constructor_args():
    sig = inspect.signature(JavaSimplified_JavaClass.__init__)
    params = list(sig.parameters.keys())
    assert "imports" in params, "Missing parameter 'imports'"

def test_javasimplified_javaclass_has_imports():
    assert hasattr(JavaSimplified_JavaClass, "imports")
    descriptor = None
    for klass in JavaSimplified_JavaClass.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_name_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_Name)


def test_javasimplified_name_constructor_exists():
    assert callable(JavaSimplified_Name.__init__)


def test_javasimplified_name_constructor_args():
    sig = inspect.signature(JavaSimplified_Name.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_javasimplified_name_has_identifier():
    assert hasattr(JavaSimplified_Name, "identifier")
    descriptor = None
    for klass in JavaSimplified_Name.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified_thisexpression_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_ThisExpression)


def test_javasimplified_thisexpression_constructor_exists():
    assert callable(JavaSimplified_ThisExpression.__init__)


def test_javasimplified_thisexpression_constructor_args():
    sig = inspect.signature(JavaSimplified_ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_fieldaccess_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_FieldAccess)


def test_javasimplified_fieldaccess_constructor_exists():
    assert callable(JavaSimplified_FieldAccess.__init__)


def test_javasimplified_fieldaccess_constructor_args():
    sig = inspect.signature(JavaSimplified_FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_literal_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_Literal)


def test_javasimplified_literal_constructor_exists():
    assert callable(JavaSimplified_Literal.__init__)


def test_javasimplified_literal_constructor_args():
    sig = inspect.signature(JavaSimplified_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_javasimplified_literal_has_type():
    assert hasattr(JavaSimplified_Literal, "type")
    descriptor = None
    for klass in JavaSimplified_Literal.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_javasimplified_literal_has_value():
    assert hasattr(JavaSimplified_Literal, "value")
    descriptor = None
    for klass in JavaSimplified_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified_infixexpression_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_InfixExpression)


def test_javasimplified_infixexpression_constructor_exists():
    assert callable(JavaSimplified_InfixExpression.__init__)


def test_javasimplified_infixexpression_constructor_args():
    sig = inspect.signature(JavaSimplified_InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javasimplified_infixexpression_has_operator():
    assert hasattr(JavaSimplified_InfixExpression, "operator")
    descriptor = None
    for klass in JavaSimplified_InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_MethodInvocation)


def test_javasimplified_methodinvocation_constructor_exists():
    assert callable(JavaSimplified_MethodInvocation.__init__)


def test_javasimplified_methodinvocation_constructor_args():
    sig = inspect.signature(JavaSimplified_MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_assignment_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_Assignment)


def test_javasimplified_assignment_constructor_exists():
    assert callable(JavaSimplified_Assignment.__init__)


def test_javasimplified_assignment_constructor_args():
    sig = inspect.signature(JavaSimplified_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_javasimplified_assignment_has_operator():
    assert hasattr(JavaSimplified_Assignment, "operator")
    descriptor = None
    for klass in JavaSimplified_Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_returnstatement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_ReturnStatement)


def test_javasimplified_returnstatement_constructor_exists():
    assert callable(JavaSimplified_ReturnStatement.__init__)


def test_javasimplified_returnstatement_constructor_args():
    sig = inspect.signature(JavaSimplified_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_ifstatement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_IfStatement)


def test_javasimplified_ifstatement_constructor_exists():
    assert callable(JavaSimplified_IfStatement.__init__)


def test_javasimplified_ifstatement_constructor_args():
    sig = inspect.signature(JavaSimplified_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_ExpressionStatement)


def test_javasimplified_expressionstatement_constructor_exists():
    assert callable(JavaSimplified_ExpressionStatement.__init__)


def test_javasimplified_expressionstatement_constructor_args():
    sig = inspect.signature(JavaSimplified_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_VariableDeclarationStatement)


def test_javasimplified_variabledeclarationstatement_constructor_exists():
    assert callable(JavaSimplified_VariableDeclarationStatement.__init__)


def test_javasimplified_variabledeclarationstatement_constructor_args():
    sig = inspect.signature(JavaSimplified_VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_commentstatement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_CommentStatement)


def test_javasimplified_commentstatement_constructor_exists():
    assert callable(JavaSimplified_CommentStatement.__init__)


def test_javasimplified_commentstatement_constructor_args():
    sig = inspect.signature(JavaSimplified_CommentStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_commentedelement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_CommentedElement)


def test_javasimplified_commentedelement_constructor_exists():
    assert callable(JavaSimplified_CommentedElement.__init__)


def test_javasimplified_commentedelement_constructor_args():
    sig = inspect.signature(JavaSimplified_CommentedElement.__init__)
    params = list(sig.parameters.keys())



def test_stringelement_is_not_abstract():
    assert not inspect.isabstract(StringElement)


def test_stringelement_constructor_exists():
    assert callable(StringElement.__init__)


def test_stringelement_constructor_args():
    sig = inspect.signature(StringElement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_expression_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_Expression)


def test_javasimplified_expression_constructor_exists():
    assert callable(JavaSimplified_Expression.__init__)


def test_javasimplified_expression_constructor_args():
    sig = inspect.signature(JavaSimplified_Expression.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_feature_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_Feature)


def test_javasimplified_feature_constructor_exists():
    assert callable(JavaSimplified_Feature.__init__)


def test_javasimplified_feature_constructor_args():
    sig = inspect.signature(JavaSimplified_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_javasimplified_feature_has_visibility():
    assert hasattr(JavaSimplified_Feature, "visibility")
    descriptor = None
    for klass in JavaSimplified_Feature.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified_statement_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_Statement)


def test_javasimplified_statement_constructor_exists():
    assert callable(JavaSimplified_Statement.__init__)


def test_javasimplified_statement_constructor_args():
    sig = inspect.signature(JavaSimplified_Statement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_comment_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_Comment)


def test_javasimplified_comment_constructor_exists():
    assert callable(JavaSimplified_Comment.__init__)


def test_javasimplified_comment_constructor_args():
    sig = inspect.signature(JavaSimplified_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "isJavadoc" in params, "Missing parameter 'isJavadoc'"

def test_javasimplified_comment_has_isJavadoc():
    assert hasattr(JavaSimplified_Comment, "isJavadoc")
    descriptor = None
    for klass in JavaSimplified_Comment.__mro__:
        if "isJavadoc" in klass.__dict__:
            descriptor = klass.__dict__["isJavadoc"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified_classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_ClassInstanceCreation)


def test_javasimplified_classinstancecreation_constructor_exists():
    assert callable(JavaSimplified_ClassInstanceCreation.__init__)


def test_javasimplified_classinstancecreation_constructor_args():
    sig = inspect.signature(JavaSimplified_ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified_type_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_Type)


def test_javasimplified_type_constructor_exists():
    assert callable(JavaSimplified_Type.__init__)


def test_javasimplified_type_constructor_args():
    sig = inspect.signature(JavaSimplified_Type.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_javasimplified_type_has_type():
    assert hasattr(JavaSimplified_Type, "type")
    descriptor = None
    for klass in JavaSimplified_Type.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified_castexpression_is_not_abstract():
    assert not inspect.isabstract(JavaSimplified_CastExpression)


def test_javasimplified_castexpression_constructor_exists():
    assert callable(JavaSimplified_CastExpression.__init__)


def test_javasimplified_castexpression_constructor_args():
    sig = inspect.signature(JavaSimplified_CastExpression.__init__)
    params = list(sig.parameters.keys())

def test_infixoperatortype_exists():
    # Check that the Enumeration exists
    assert InfixOperatorType is not None

def test_infixoperatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixOperatorType]
    expected_literals = [
        "NOT_EQUALS",
        "CONDITIONAL_AND",
        "CONDITIONAL_OR",
        "EQUALS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InfixOperatorType"

def test_visibilitytype_exists():
    # Check that the Enumeration exists
    assert VisibilityType is not None

def test_visibilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityType]
    expected_literals = [
        "PACKAGE",
        "PUBLIC",
        "PRIVATE",
        "PROTECTED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityType"

def test_literaltype_exists():
    # Check that the Enumeration exists
    assert LiteralType is not None

def test_literaltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LiteralType]
    expected_literals = [
        "BOOLEAN",
        "NULL",
        "STRING",
        "INTEGER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LiteralType"

def test_assignmentoperatortype_exists():
    # Check that the Enumeration exists
    assert AssignmentOperatorType is not None

def test_assignmentoperatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperatorType]
    expected_literals = [
        "ASSIGN",
        "PLUS_ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperatorType"


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
JavaSimplified_MethodCall_strategy = st.builds(
    JavaSimplified_MethodCall,
)
JavaSimplified_TypedElement_strategy = st.builds(
    JavaSimplified_TypedElement,
)
JavaSimplified_StringElement_strategy = st.builds(
    JavaSimplified_StringElement,
    strValue=
        safe_text
)
JavaSimplified_NamedElement_strategy = st.builds(
    JavaSimplified_NamedElement,
)
Feature_strategy = st.builds(
    Feature,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
JavaSimplified_Field_strategy = st.builds(
    JavaSimplified_Field,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
JavaSimplified_Parameter_strategy = st.builds(
    JavaSimplified_Parameter,
)
CommentedElement_strategy = st.builds(
    CommentedElement,
)
JavaSimplified_JavaModel_strategy = st.builds(
    JavaSimplified_JavaModel,
)
JavaSimplified_Method_strategy = st.builds(
    JavaSimplified_Method,
    exceptions=
        safe_text
)
JavaSimplified_JavaClass_strategy = st.builds(
    JavaSimplified_JavaClass,
    imports=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
JavaSimplified_Name_strategy = st.builds(
    JavaSimplified_Name,
    identifier=
        safe_text
)
JavaSimplified_ThisExpression_strategy = st.builds(
    JavaSimplified_ThisExpression,
)
JavaSimplified_FieldAccess_strategy = st.builds(
    JavaSimplified_FieldAccess,
)
JavaSimplified_Literal_strategy = st.builds(
    JavaSimplified_Literal,
    type=
        safe_text,
    value=
        safe_text
)
JavaSimplified_InfixExpression_strategy = st.builds(
    JavaSimplified_InfixExpression,
    operator=
        safe_text
)
JavaSimplified_MethodInvocation_strategy = st.builds(
    JavaSimplified_MethodInvocation,
)
JavaSimplified_Assignment_strategy = st.builds(
    JavaSimplified_Assignment,
    operator=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
JavaSimplified_ReturnStatement_strategy = st.builds(
    JavaSimplified_ReturnStatement,
)
JavaSimplified_IfStatement_strategy = st.builds(
    JavaSimplified_IfStatement,
)
JavaSimplified_ExpressionStatement_strategy = st.builds(
    JavaSimplified_ExpressionStatement,
)
JavaSimplified_VariableDeclarationStatement_strategy = st.builds(
    JavaSimplified_VariableDeclarationStatement,
)
JavaSimplified_CommentStatement_strategy = st.builds(
    JavaSimplified_CommentStatement,
)
JavaSimplified_CommentedElement_strategy = st.builds(
    JavaSimplified_CommentedElement,
)
StringElement_strategy = st.builds(
    StringElement,
)
JavaSimplified_Expression_strategy = st.builds(
    JavaSimplified_Expression,
)
JavaSimplified_Feature_strategy = st.builds(
    JavaSimplified_Feature,
    visibility=
        safe_text
)
JavaSimplified_Statement_strategy = st.builds(
    JavaSimplified_Statement,
)
JavaSimplified_Comment_strategy = st.builds(
    JavaSimplified_Comment,
    isJavadoc=
        st.booleans()
)
JavaSimplified_ClassInstanceCreation_strategy = st.builds(
    JavaSimplified_ClassInstanceCreation,
)
JavaSimplified_Type_strategy = st.builds(
    JavaSimplified_Type,
    type=
        safe_text
)
JavaSimplified_CastExpression_strategy = st.builds(
    JavaSimplified_CastExpression,
)

@given(instance=JavaSimplified_MethodCall_strategy)
@settings(max_examples=50)
def test_javasimplified_methodcall_instantiation(instance):
    assert isinstance(instance, JavaSimplified_MethodCall)

@given(instance=JavaSimplified_TypedElement_strategy)
@settings(max_examples=50)
def test_javasimplified_typedelement_instantiation(instance):
    assert isinstance(instance, JavaSimplified_TypedElement)

@given(instance=JavaSimplified_StringElement_strategy)
@settings(max_examples=50)
def test_javasimplified_stringelement_instantiation(instance):
    assert isinstance(instance, JavaSimplified_StringElement)



@given(instance=JavaSimplified_StringElement_strategy)
def test_javasimplified_stringelement_strValue_setter(instance):
    original = instance.strValue
    instance.strValue = original
    assert instance.strValue == original

@given(instance=JavaSimplified_NamedElement_strategy)
@settings(max_examples=50)
def test_javasimplified_namedelement_instantiation(instance):
    assert isinstance(instance, JavaSimplified_NamedElement)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=JavaSimplified_Field_strategy)
@settings(max_examples=50)
def test_javasimplified_field_instantiation(instance):
    assert isinstance(instance, JavaSimplified_Field)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=JavaSimplified_Parameter_strategy)
@settings(max_examples=50)
def test_javasimplified_parameter_instantiation(instance):
    assert isinstance(instance, JavaSimplified_Parameter)

@given(instance=CommentedElement_strategy)
@settings(max_examples=50)
def test_commentedelement_instantiation(instance):
    assert isinstance(instance, CommentedElement)

@given(instance=JavaSimplified_JavaModel_strategy)
@settings(max_examples=50)
def test_javasimplified_javamodel_instantiation(instance):
    assert isinstance(instance, JavaSimplified_JavaModel)

@given(instance=JavaSimplified_Method_strategy)
@settings(max_examples=50)
def test_javasimplified_method_instantiation(instance):
    assert isinstance(instance, JavaSimplified_Method)



@given(instance=JavaSimplified_Method_strategy)
def test_javasimplified_method_exceptions_setter(instance):
    original = instance.exceptions
    instance.exceptions = original
    assert instance.exceptions == original

@given(instance=JavaSimplified_JavaClass_strategy)
@settings(max_examples=50)
def test_javasimplified_javaclass_instantiation(instance):
    assert isinstance(instance, JavaSimplified_JavaClass)



@given(instance=JavaSimplified_JavaClass_strategy)
def test_javasimplified_javaclass_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=JavaSimplified_Name_strategy)
@settings(max_examples=50)
def test_javasimplified_name_instantiation(instance):
    assert isinstance(instance, JavaSimplified_Name)



@given(instance=JavaSimplified_Name_strategy)
def test_javasimplified_name_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=JavaSimplified_ThisExpression_strategy)
@settings(max_examples=50)
def test_javasimplified_thisexpression_instantiation(instance):
    assert isinstance(instance, JavaSimplified_ThisExpression)

@given(instance=JavaSimplified_FieldAccess_strategy)
@settings(max_examples=50)
def test_javasimplified_fieldaccess_instantiation(instance):
    assert isinstance(instance, JavaSimplified_FieldAccess)

@given(instance=JavaSimplified_Literal_strategy)
@settings(max_examples=50)
def test_javasimplified_literal_instantiation(instance):
    assert isinstance(instance, JavaSimplified_Literal)



@given(instance=JavaSimplified_Literal_strategy)
def test_javasimplified_literal_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=JavaSimplified_Literal_strategy)
def test_javasimplified_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=JavaSimplified_InfixExpression_strategy)
@settings(max_examples=50)
def test_javasimplified_infixexpression_instantiation(instance):
    assert isinstance(instance, JavaSimplified_InfixExpression)



@given(instance=JavaSimplified_InfixExpression_strategy)
def test_javasimplified_infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=JavaSimplified_MethodInvocation_strategy)
@settings(max_examples=50)
def test_javasimplified_methodinvocation_instantiation(instance):
    assert isinstance(instance, JavaSimplified_MethodInvocation)

@given(instance=JavaSimplified_Assignment_strategy)
@settings(max_examples=50)
def test_javasimplified_assignment_instantiation(instance):
    assert isinstance(instance, JavaSimplified_Assignment)



@given(instance=JavaSimplified_Assignment_strategy)
def test_javasimplified_assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=JavaSimplified_ReturnStatement_strategy)
@settings(max_examples=50)
def test_javasimplified_returnstatement_instantiation(instance):
    assert isinstance(instance, JavaSimplified_ReturnStatement)

@given(instance=JavaSimplified_IfStatement_strategy)
@settings(max_examples=50)
def test_javasimplified_ifstatement_instantiation(instance):
    assert isinstance(instance, JavaSimplified_IfStatement)

@given(instance=JavaSimplified_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_javasimplified_expressionstatement_instantiation(instance):
    assert isinstance(instance, JavaSimplified_ExpressionStatement)

@given(instance=JavaSimplified_VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_javasimplified_variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, JavaSimplified_VariableDeclarationStatement)

@given(instance=JavaSimplified_CommentStatement_strategy)
@settings(max_examples=50)
def test_javasimplified_commentstatement_instantiation(instance):
    assert isinstance(instance, JavaSimplified_CommentStatement)

@given(instance=JavaSimplified_CommentedElement_strategy)
@settings(max_examples=50)
def test_javasimplified_commentedelement_instantiation(instance):
    assert isinstance(instance, JavaSimplified_CommentedElement)

@given(instance=StringElement_strategy)
@settings(max_examples=50)
def test_stringelement_instantiation(instance):
    assert isinstance(instance, StringElement)

@given(instance=JavaSimplified_Expression_strategy)
@settings(max_examples=50)
def test_javasimplified_expression_instantiation(instance):
    assert isinstance(instance, JavaSimplified_Expression)

@given(instance=JavaSimplified_Feature_strategy)
@settings(max_examples=50)
def test_javasimplified_feature_instantiation(instance):
    assert isinstance(instance, JavaSimplified_Feature)



@given(instance=JavaSimplified_Feature_strategy)
def test_javasimplified_feature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=JavaSimplified_Statement_strategy)
@settings(max_examples=50)
def test_javasimplified_statement_instantiation(instance):
    assert isinstance(instance, JavaSimplified_Statement)

@given(instance=JavaSimplified_Comment_strategy)
@settings(max_examples=50)
def test_javasimplified_comment_instantiation(instance):
    assert isinstance(instance, JavaSimplified_Comment)



@given(instance=JavaSimplified_Comment_strategy)
def test_javasimplified_comment_isJavadoc_setter(instance):
    original = instance.isJavadoc
    instance.isJavadoc = original
    assert instance.isJavadoc == original

@given(instance=JavaSimplified_ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_javasimplified_classinstancecreation_instantiation(instance):
    assert isinstance(instance, JavaSimplified_ClassInstanceCreation)

@given(instance=JavaSimplified_Type_strategy)
@settings(max_examples=50)
def test_javasimplified_type_instantiation(instance):
    assert isinstance(instance, JavaSimplified_Type)



@given(instance=JavaSimplified_Type_strategy)
def test_javasimplified_type_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=JavaSimplified_CastExpression_strategy)
@settings(max_examples=50)
def test_javasimplified_castexpression_instantiation(instance):
    assert isinstance(instance, JavaSimplified_CastExpression)
