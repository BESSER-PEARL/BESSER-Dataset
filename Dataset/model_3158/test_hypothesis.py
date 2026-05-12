import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ComparisonExpression,
    model_GreaterEqualExpression,
    model_GreaterExpression,
    EquivalenceExpression,
    model_InequalityExpression,
    model_EqualityExpression,
    PredicateExpression,
    QuantifierExpression,
    model_ExistsExpression,
    model_ForallExpression,
    ArgumentedElement,
    AccessExpression,
    model_SelectExpression,
    model_RecordAccessExpression,
    model_ArrayAccessExpression,
    model_FunctionAccessExpression,
    model_LessEqualExpression,
    model_LessExpression,
    BooleanLiteralExpression,
    model_FalseExpression,
    model_TrueExpression,
    BooleanExpression,
    ArithmeticLiteralExpression,
    model_RationalLiteralExpression,
    model_DecimalLiteralExpression,
    model_IntegerLiteralExpression,
    ArithmeticExpression,
    LiteralExpression,
    model_FieldAssignment,
    model_RecordLiteralExpression,
    BinaryExpression,
    model_ImplyExpression,
    model_SubtractExpression,
    model_DivExpression,
    model_ModExpression,
    model_DivideExpression,
    model_EquivalenceExpression,
    model_ComparisonExpression,
    MultiaryExpression,
    model_OrExpression,
    model_XorExpression,
    model_AndExpression,
    model_AddExpression,
    model_MultiplyExpression,
    EnumerableExpression,
    model_IntegerRangeLiteralExpression,
    model_ArrayLiteralExpression,
    Expression,
    model_EnumerableExpression,
    model_UnaryExpression,
    model_LiteralExpression,
    model_AccessExpression,
    model_IfThenElseExpression,
    model_NullaryExpression,
    ConstraintDefinition,
    model_ConstraintDefinition,
    UnaryExpression,
    model_NotExpression,
    model_UnaryMinusExpression,
    model_UnaryPlusExpression,
    ElseExpression,
    model_DefaultExpression,
    NullaryExpression,
    model_ArithmeticLiteralExpression,
    model_BooleanLiteralExpression,
    model_ReferenceExpression,
    model_EnumerationLiteralExpression,
    model_OpaqueExpression,
    LogicExpression,
    model_PredicateExpression,
    model_ElseExpression,
    model_BooleanExpression,
    model_LogicExpression,
    model_ArithmeticExpression,
    model_MultiaryExpression,
    model_BinaryExpression,
    CompositeTypeDefinition,
    model_FunctionTypeDefinition,
    model_RecordTypeDefinition,
    EnumerableTypeDefinition,
    model_ArrayTypeDefinition,
    model_IntegerRangeTypeDefinition,
    model_EnumerationTypeDefinition,
    model_EnumerableTypeDefinition,
    Declaration,
    model_ValueDeclaration,
    model_Type,
    model_BasicConstraintDefinition,
    model_TypeDeclaration,
    ParametricElement,
    model_QuantifierExpression,
    model_FunctionDeclaration,
    NamedElement,
    model_InitializableElement,
    model_Declaration,
    model_EnumerationLiteralDefinition,
    model_ExpressionPackage,
    NumericalTypeDefinition,
    model_DecimalTypeDefinition,
    model_SubrangeTypeDefinition,
    model_RationalTypeDefinition,
    model_IntegerTypeDefinition,
    TypeDefinition,
    model_BooleanTypeDefinition,
    model_VoidTypeDefinition,
    model_CompositeTypeDefinition,
    model_NumericalTypeDefinition,
    Type,
    model_TypeDefinition,
    model_TypeReference,
    FunctionDeclaration,
    InitializableElement,
    model_LambdaDeclaration,
    ValueDeclaration,
    model_FieldDeclaration,
    model_ConstantDeclaration,
    model_VariableDeclaration,
    model_Comment,
    model_CommentableElement,
    model_NamedElement,
    model_Expression,
    model_ArgumentedElement,
    model_ParameterDeclaration,
    model_ParametricElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(ComparisonExpression)


def test_comparisonexpression_constructor_exists():
    assert callable(ComparisonExpression.__init__)


def test_comparisonexpression_constructor_args():
    sig = inspect.signature(ComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_greaterequalexpression_is_not_abstract():
    assert not inspect.isabstract(model_GreaterEqualExpression)


def test_model_greaterequalexpression_constructor_exists():
    assert callable(model_GreaterEqualExpression.__init__)


def test_model_greaterequalexpression_constructor_args():
    sig = inspect.signature(model_GreaterEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_greaterexpression_is_not_abstract():
    assert not inspect.isabstract(model_GreaterExpression)


def test_model_greaterexpression_constructor_exists():
    assert callable(model_GreaterExpression.__init__)


def test_model_greaterexpression_constructor_args():
    sig = inspect.signature(model_GreaterExpression.__init__)
    params = list(sig.parameters.keys())



def test_equivalenceexpression_is_not_abstract():
    assert not inspect.isabstract(EquivalenceExpression)


def test_equivalenceexpression_constructor_exists():
    assert callable(EquivalenceExpression.__init__)


def test_equivalenceexpression_constructor_args():
    sig = inspect.signature(EquivalenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_inequalityexpression_is_not_abstract():
    assert not inspect.isabstract(model_InequalityExpression)


def test_model_inequalityexpression_constructor_exists():
    assert callable(model_InequalityExpression.__init__)


def test_model_inequalityexpression_constructor_args():
    sig = inspect.signature(model_InequalityExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(model_EqualityExpression)


def test_model_equalityexpression_constructor_exists():
    assert callable(model_EqualityExpression.__init__)


def test_model_equalityexpression_constructor_args():
    sig = inspect.signature(model_EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_predicateexpression_is_not_abstract():
    assert not inspect.isabstract(PredicateExpression)


def test_predicateexpression_constructor_exists():
    assert callable(PredicateExpression.__init__)


def test_predicateexpression_constructor_args():
    sig = inspect.signature(PredicateExpression.__init__)
    params = list(sig.parameters.keys())



def test_quantifierexpression_is_not_abstract():
    assert not inspect.isabstract(QuantifierExpression)


def test_quantifierexpression_constructor_exists():
    assert callable(QuantifierExpression.__init__)


def test_quantifierexpression_constructor_args():
    sig = inspect.signature(QuantifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_existsexpression_is_not_abstract():
    assert not inspect.isabstract(model_ExistsExpression)


def test_model_existsexpression_constructor_exists():
    assert callable(model_ExistsExpression.__init__)


def test_model_existsexpression_constructor_args():
    sig = inspect.signature(model_ExistsExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_forallexpression_is_not_abstract():
    assert not inspect.isabstract(model_ForallExpression)


def test_model_forallexpression_constructor_exists():
    assert callable(model_ForallExpression.__init__)


def test_model_forallexpression_constructor_args():
    sig = inspect.signature(model_ForallExpression.__init__)
    params = list(sig.parameters.keys())



def test_argumentedelement_is_not_abstract():
    assert not inspect.isabstract(ArgumentedElement)


def test_argumentedelement_constructor_exists():
    assert callable(ArgumentedElement.__init__)


def test_argumentedelement_constructor_args():
    sig = inspect.signature(ArgumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_accessexpression_is_not_abstract():
    assert not inspect.isabstract(AccessExpression)


def test_accessexpression_constructor_exists():
    assert callable(AccessExpression.__init__)


def test_accessexpression_constructor_args():
    sig = inspect.signature(AccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_selectexpression_is_not_abstract():
    assert not inspect.isabstract(model_SelectExpression)


def test_model_selectexpression_constructor_exists():
    assert callable(model_SelectExpression.__init__)


def test_model_selectexpression_constructor_args():
    sig = inspect.signature(model_SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_recordaccessexpression_is_not_abstract():
    assert not inspect.isabstract(model_RecordAccessExpression)


def test_model_recordaccessexpression_constructor_exists():
    assert callable(model_RecordAccessExpression.__init__)


def test_model_recordaccessexpression_constructor_args():
    sig = inspect.signature(model_RecordAccessExpression.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_model_recordaccessexpression_has_field():
    assert hasattr(model_RecordAccessExpression, "field")
    descriptor = None
    for klass in model_RecordAccessExpression.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_model_arrayaccessexpression_is_not_abstract():
    assert not inspect.isabstract(model_ArrayAccessExpression)


def test_model_arrayaccessexpression_constructor_exists():
    assert callable(model_ArrayAccessExpression.__init__)


def test_model_arrayaccessexpression_constructor_args():
    sig = inspect.signature(model_ArrayAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_functionaccessexpression_is_not_abstract():
    assert not inspect.isabstract(model_FunctionAccessExpression)


def test_model_functionaccessexpression_constructor_exists():
    assert callable(model_FunctionAccessExpression.__init__)


def test_model_functionaccessexpression_constructor_args():
    sig = inspect.signature(model_FunctionAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_lessequalexpression_is_not_abstract():
    assert not inspect.isabstract(model_LessEqualExpression)


def test_model_lessequalexpression_constructor_exists():
    assert callable(model_LessEqualExpression.__init__)


def test_model_lessequalexpression_constructor_args():
    sig = inspect.signature(model_LessEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_lessexpression_is_not_abstract():
    assert not inspect.isabstract(model_LessExpression)


def test_model_lessexpression_constructor_exists():
    assert callable(model_LessExpression.__init__)


def test_model_lessexpression_constructor_args():
    sig = inspect.signature(model_LessExpression.__init__)
    params = list(sig.parameters.keys())



def test_booleanliteralexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanLiteralExpression)


def test_booleanliteralexpression_constructor_exists():
    assert callable(BooleanLiteralExpression.__init__)


def test_booleanliteralexpression_constructor_args():
    sig = inspect.signature(BooleanLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_falseexpression_is_not_abstract():
    assert not inspect.isabstract(model_FalseExpression)


def test_model_falseexpression_constructor_exists():
    assert callable(model_FalseExpression.__init__)


def test_model_falseexpression_constructor_args():
    sig = inspect.signature(model_FalseExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_trueexpression_is_not_abstract():
    assert not inspect.isabstract(model_TrueExpression)


def test_model_trueexpression_constructor_exists():
    assert callable(model_TrueExpression.__init__)


def test_model_trueexpression_constructor_args():
    sig = inspect.signature(model_TrueExpression.__init__)
    params = list(sig.parameters.keys())



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticliteralexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticLiteralExpression)


def test_arithmeticliteralexpression_constructor_exists():
    assert callable(ArithmeticLiteralExpression.__init__)


def test_arithmeticliteralexpression_constructor_args():
    sig = inspect.signature(ArithmeticLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_rationalliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model_RationalLiteralExpression)


def test_model_rationalliteralexpression_constructor_exists():
    assert callable(model_RationalLiteralExpression.__init__)


def test_model_rationalliteralexpression_constructor_args():
    sig = inspect.signature(model_RationalLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "numerator" in params, "Missing parameter 'numerator'"
    assert "denominator" in params, "Missing parameter 'denominator'"

def test_model_rationalliteralexpression_has_numerator():
    assert hasattr(model_RationalLiteralExpression, "numerator")
    descriptor = None
    for klass in model_RationalLiteralExpression.__mro__:
        if "numerator" in klass.__dict__:
            descriptor = klass.__dict__["numerator"]
            break
    assert isinstance(descriptor, property)

def test_model_rationalliteralexpression_has_denominator():
    assert hasattr(model_RationalLiteralExpression, "denominator")
    descriptor = None
    for klass in model_RationalLiteralExpression.__mro__:
        if "denominator" in klass.__dict__:
            descriptor = klass.__dict__["denominator"]
            break
    assert isinstance(descriptor, property)



def test_model_decimalliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model_DecimalLiteralExpression)


def test_model_decimalliteralexpression_constructor_exists():
    assert callable(model_DecimalLiteralExpression.__init__)


def test_model_decimalliteralexpression_constructor_args():
    sig = inspect.signature(model_DecimalLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model_decimalliteralexpression_has_value():
    assert hasattr(model_DecimalLiteralExpression, "value")
    descriptor = None
    for klass in model_DecimalLiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model_integerliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model_IntegerLiteralExpression)


def test_model_integerliteralexpression_constructor_exists():
    assert callable(model_IntegerLiteralExpression.__init__)


def test_model_integerliteralexpression_constructor_args():
    sig = inspect.signature(model_IntegerLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model_integerliteralexpression_has_value():
    assert hasattr(model_IntegerLiteralExpression, "value")
    descriptor = None
    for klass in model_IntegerLiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_fieldassignment_is_not_abstract():
    assert not inspect.isabstract(model_FieldAssignment)


def test_model_fieldassignment_constructor_exists():
    assert callable(model_FieldAssignment.__init__)


def test_model_fieldassignment_constructor_args():
    sig = inspect.signature(model_FieldAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"

def test_model_fieldassignment_has_reference():
    assert hasattr(model_FieldAssignment, "reference")
    descriptor = None
    for klass in model_FieldAssignment.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_model_recordliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model_RecordLiteralExpression)


def test_model_recordliteralexpression_constructor_exists():
    assert callable(model_RecordLiteralExpression.__init__)


def test_model_recordliteralexpression_constructor_args():
    sig = inspect.signature(model_RecordLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_implyexpression_is_not_abstract():
    assert not inspect.isabstract(model_ImplyExpression)


def test_model_implyexpression_constructor_exists():
    assert callable(model_ImplyExpression.__init__)


def test_model_implyexpression_constructor_args():
    sig = inspect.signature(model_ImplyExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_subtractexpression_is_not_abstract():
    assert not inspect.isabstract(model_SubtractExpression)


def test_model_subtractexpression_constructor_exists():
    assert callable(model_SubtractExpression.__init__)


def test_model_subtractexpression_constructor_args():
    sig = inspect.signature(model_SubtractExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_divexpression_is_not_abstract():
    assert not inspect.isabstract(model_DivExpression)


def test_model_divexpression_constructor_exists():
    assert callable(model_DivExpression.__init__)


def test_model_divexpression_constructor_args():
    sig = inspect.signature(model_DivExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_modexpression_is_not_abstract():
    assert not inspect.isabstract(model_ModExpression)


def test_model_modexpression_constructor_exists():
    assert callable(model_ModExpression.__init__)


def test_model_modexpression_constructor_args():
    sig = inspect.signature(model_ModExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_divideexpression_is_not_abstract():
    assert not inspect.isabstract(model_DivideExpression)


def test_model_divideexpression_constructor_exists():
    assert callable(model_DivideExpression.__init__)


def test_model_divideexpression_constructor_args():
    sig = inspect.signature(model_DivideExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_equivalenceexpression_is_not_abstract():
    assert not inspect.isabstract(model_EquivalenceExpression)


def test_model_equivalenceexpression_constructor_exists():
    assert callable(model_EquivalenceExpression.__init__)


def test_model_equivalenceexpression_constructor_args():
    sig = inspect.signature(model_EquivalenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_comparisonexpression_is_not_abstract():
    assert not inspect.isabstract(model_ComparisonExpression)


def test_model_comparisonexpression_constructor_exists():
    assert callable(model_ComparisonExpression.__init__)


def test_model_comparisonexpression_constructor_args():
    sig = inspect.signature(model_ComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_multiaryexpression_is_not_abstract():
    assert not inspect.isabstract(MultiaryExpression)


def test_multiaryexpression_constructor_exists():
    assert callable(MultiaryExpression.__init__)


def test_multiaryexpression_constructor_args():
    sig = inspect.signature(MultiaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_orexpression_is_not_abstract():
    assert not inspect.isabstract(model_OrExpression)


def test_model_orexpression_constructor_exists():
    assert callable(model_OrExpression.__init__)


def test_model_orexpression_constructor_args():
    sig = inspect.signature(model_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_xorexpression_is_not_abstract():
    assert not inspect.isabstract(model_XorExpression)


def test_model_xorexpression_constructor_exists():
    assert callable(model_XorExpression.__init__)


def test_model_xorexpression_constructor_args():
    sig = inspect.signature(model_XorExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_andexpression_is_not_abstract():
    assert not inspect.isabstract(model_AndExpression)


def test_model_andexpression_constructor_exists():
    assert callable(model_AndExpression.__init__)


def test_model_andexpression_constructor_args():
    sig = inspect.signature(model_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_addexpression_is_not_abstract():
    assert not inspect.isabstract(model_AddExpression)


def test_model_addexpression_constructor_exists():
    assert callable(model_AddExpression.__init__)


def test_model_addexpression_constructor_args():
    sig = inspect.signature(model_AddExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_multiplyexpression_is_not_abstract():
    assert not inspect.isabstract(model_MultiplyExpression)


def test_model_multiplyexpression_constructor_exists():
    assert callable(model_MultiplyExpression.__init__)


def test_model_multiplyexpression_constructor_args():
    sig = inspect.signature(model_MultiplyExpression.__init__)
    params = list(sig.parameters.keys())



def test_enumerableexpression_is_not_abstract():
    assert not inspect.isabstract(EnumerableExpression)


def test_enumerableexpression_constructor_exists():
    assert callable(EnumerableExpression.__init__)


def test_enumerableexpression_constructor_args():
    sig = inspect.signature(EnumerableExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_integerrangeliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model_IntegerRangeLiteralExpression)


def test_model_integerrangeliteralexpression_constructor_exists():
    assert callable(model_IntegerRangeLiteralExpression.__init__)


def test_model_integerrangeliteralexpression_constructor_args():
    sig = inspect.signature(model_IntegerRangeLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "leftInclusive" in params, "Missing parameter 'leftInclusive'"
    assert "rightInclusive" in params, "Missing parameter 'rightInclusive'"

def test_model_integerrangeliteralexpression_has_leftInclusive():
    assert hasattr(model_IntegerRangeLiteralExpression, "leftInclusive")
    descriptor = None
    for klass in model_IntegerRangeLiteralExpression.__mro__:
        if "leftInclusive" in klass.__dict__:
            descriptor = klass.__dict__["leftInclusive"]
            break
    assert isinstance(descriptor, property)

def test_model_integerrangeliteralexpression_has_rightInclusive():
    assert hasattr(model_IntegerRangeLiteralExpression, "rightInclusive")
    descriptor = None
    for klass in model_IntegerRangeLiteralExpression.__mro__:
        if "rightInclusive" in klass.__dict__:
            descriptor = klass.__dict__["rightInclusive"]
            break
    assert isinstance(descriptor, property)



def test_model_arrayliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model_ArrayLiteralExpression)


def test_model_arrayliteralexpression_constructor_exists():
    assert callable(model_ArrayLiteralExpression.__init__)


def test_model_arrayliteralexpression_constructor_args():
    sig = inspect.signature(model_ArrayLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_model_enumerableexpression_is_not_abstract():
    assert not inspect.isabstract(model_EnumerableExpression)


def test_model_enumerableexpression_constructor_exists():
    assert callable(model_EnumerableExpression.__init__)


def test_model_enumerableexpression_constructor_args():
    sig = inspect.signature(model_EnumerableExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(model_UnaryExpression)


def test_model_unaryexpression_constructor_exists():
    assert callable(model_UnaryExpression.__init__)


def test_model_unaryexpression_constructor_args():
    sig = inspect.signature(model_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_literalexpression_is_not_abstract():
    assert not inspect.isabstract(model_LiteralExpression)


def test_model_literalexpression_constructor_exists():
    assert callable(model_LiteralExpression.__init__)


def test_model_literalexpression_constructor_args():
    sig = inspect.signature(model_LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_accessexpression_is_not_abstract():
    assert not inspect.isabstract(model_AccessExpression)


def test_model_accessexpression_constructor_exists():
    assert callable(model_AccessExpression.__init__)


def test_model_accessexpression_constructor_args():
    sig = inspect.signature(model_AccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_ifthenelseexpression_is_not_abstract():
    assert not inspect.isabstract(model_IfThenElseExpression)


def test_model_ifthenelseexpression_constructor_exists():
    assert callable(model_IfThenElseExpression.__init__)


def test_model_ifthenelseexpression_constructor_args():
    sig = inspect.signature(model_IfThenElseExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_nullaryexpression_is_not_abstract():
    assert not inspect.isabstract(model_NullaryExpression)


def test_model_nullaryexpression_constructor_exists():
    assert callable(model_NullaryExpression.__init__)


def test_model_nullaryexpression_constructor_args():
    sig = inspect.signature(model_NullaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_constraintdefinition_is_not_abstract():
    assert not inspect.isabstract(ConstraintDefinition)


def test_constraintdefinition_constructor_exists():
    assert callable(ConstraintDefinition.__init__)


def test_constraintdefinition_constructor_args():
    sig = inspect.signature(ConstraintDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_constraintdefinition_is_not_abstract():
    assert not inspect.isabstract(model_ConstraintDefinition)


def test_model_constraintdefinition_constructor_exists():
    assert callable(model_ConstraintDefinition.__init__)


def test_model_constraintdefinition_constructor_args():
    sig = inspect.signature(model_ConstraintDefinition.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_notexpression_is_not_abstract():
    assert not inspect.isabstract(model_NotExpression)


def test_model_notexpression_constructor_exists():
    assert callable(model_NotExpression.__init__)


def test_model_notexpression_constructor_args():
    sig = inspect.signature(model_NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_unaryminusexpression_is_not_abstract():
    assert not inspect.isabstract(model_UnaryMinusExpression)


def test_model_unaryminusexpression_constructor_exists():
    assert callable(model_UnaryMinusExpression.__init__)


def test_model_unaryminusexpression_constructor_args():
    sig = inspect.signature(model_UnaryMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_unaryplusexpression_is_not_abstract():
    assert not inspect.isabstract(model_UnaryPlusExpression)


def test_model_unaryplusexpression_constructor_exists():
    assert callable(model_UnaryPlusExpression.__init__)


def test_model_unaryplusexpression_constructor_args():
    sig = inspect.signature(model_UnaryPlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_elseexpression_is_not_abstract():
    assert not inspect.isabstract(ElseExpression)


def test_elseexpression_constructor_exists():
    assert callable(ElseExpression.__init__)


def test_elseexpression_constructor_args():
    sig = inspect.signature(ElseExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_defaultexpression_is_not_abstract():
    assert not inspect.isabstract(model_DefaultExpression)


def test_model_defaultexpression_constructor_exists():
    assert callable(model_DefaultExpression.__init__)


def test_model_defaultexpression_constructor_args():
    sig = inspect.signature(model_DefaultExpression.__init__)
    params = list(sig.parameters.keys())



def test_nullaryexpression_is_not_abstract():
    assert not inspect.isabstract(NullaryExpression)


def test_nullaryexpression_constructor_exists():
    assert callable(NullaryExpression.__init__)


def test_nullaryexpression_constructor_args():
    sig = inspect.signature(NullaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_arithmeticliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model_ArithmeticLiteralExpression)


def test_model_arithmeticliteralexpression_constructor_exists():
    assert callable(model_ArithmeticLiteralExpression.__init__)


def test_model_arithmeticliteralexpression_constructor_args():
    sig = inspect.signature(model_ArithmeticLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_booleanliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model_BooleanLiteralExpression)


def test_model_booleanliteralexpression_constructor_exists():
    assert callable(model_BooleanLiteralExpression.__init__)


def test_model_booleanliteralexpression_constructor_args():
    sig = inspect.signature(model_BooleanLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_referenceexpression_is_not_abstract():
    assert not inspect.isabstract(model_ReferenceExpression)


def test_model_referenceexpression_constructor_exists():
    assert callable(model_ReferenceExpression.__init__)


def test_model_referenceexpression_constructor_args():
    sig = inspect.signature(model_ReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_enumerationliteralexpression_is_not_abstract():
    assert not inspect.isabstract(model_EnumerationLiteralExpression)


def test_model_enumerationliteralexpression_constructor_exists():
    assert callable(model_EnumerationLiteralExpression.__init__)


def test_model_enumerationliteralexpression_constructor_args():
    sig = inspect.signature(model_EnumerationLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(model_OpaqueExpression)


def test_model_opaqueexpression_constructor_exists():
    assert callable(model_OpaqueExpression.__init__)


def test_model_opaqueexpression_constructor_args():
    sig = inspect.signature(model_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_model_opaqueexpression_has_expression():
    assert hasattr(model_OpaqueExpression, "expression")
    descriptor = None
    for klass in model_OpaqueExpression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_logicexpression_is_not_abstract():
    assert not inspect.isabstract(LogicExpression)


def test_logicexpression_constructor_exists():
    assert callable(LogicExpression.__init__)


def test_logicexpression_constructor_args():
    sig = inspect.signature(LogicExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_predicateexpression_is_not_abstract():
    assert not inspect.isabstract(model_PredicateExpression)


def test_model_predicateexpression_constructor_exists():
    assert callable(model_PredicateExpression.__init__)


def test_model_predicateexpression_constructor_args():
    sig = inspect.signature(model_PredicateExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_elseexpression_is_not_abstract():
    assert not inspect.isabstract(model_ElseExpression)


def test_model_elseexpression_constructor_exists():
    assert callable(model_ElseExpression.__init__)


def test_model_elseexpression_constructor_args():
    sig = inspect.signature(model_ElseExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(model_BooleanExpression)


def test_model_booleanexpression_constructor_exists():
    assert callable(model_BooleanExpression.__init__)


def test_model_booleanexpression_constructor_args():
    sig = inspect.signature(model_BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_logicexpression_is_not_abstract():
    assert not inspect.isabstract(model_LogicExpression)


def test_model_logicexpression_constructor_exists():
    assert callable(model_LogicExpression.__init__)


def test_model_logicexpression_constructor_args():
    sig = inspect.signature(model_LogicExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(model_ArithmeticExpression)


def test_model_arithmeticexpression_constructor_exists():
    assert callable(model_ArithmeticExpression.__init__)


def test_model_arithmeticexpression_constructor_args():
    sig = inspect.signature(model_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_multiaryexpression_is_not_abstract():
    assert not inspect.isabstract(model_MultiaryExpression)


def test_model_multiaryexpression_constructor_exists():
    assert callable(model_MultiaryExpression.__init__)


def test_model_multiaryexpression_constructor_args():
    sig = inspect.signature(model_MultiaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(model_BinaryExpression)


def test_model_binaryexpression_constructor_exists():
    assert callable(model_BinaryExpression.__init__)


def test_model_binaryexpression_constructor_args():
    sig = inspect.signature(model_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_compositetypedefinition_is_not_abstract():
    assert not inspect.isabstract(CompositeTypeDefinition)


def test_compositetypedefinition_constructor_exists():
    assert callable(CompositeTypeDefinition.__init__)


def test_compositetypedefinition_constructor_args():
    sig = inspect.signature(CompositeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_functiontypedefinition_is_not_abstract():
    assert not inspect.isabstract(model_FunctionTypeDefinition)


def test_model_functiontypedefinition_constructor_exists():
    assert callable(model_FunctionTypeDefinition.__init__)


def test_model_functiontypedefinition_constructor_args():
    sig = inspect.signature(model_FunctionTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_recordtypedefinition_is_not_abstract():
    assert not inspect.isabstract(model_RecordTypeDefinition)


def test_model_recordtypedefinition_constructor_exists():
    assert callable(model_RecordTypeDefinition.__init__)


def test_model_recordtypedefinition_constructor_args():
    sig = inspect.signature(model_RecordTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_enumerabletypedefinition_is_not_abstract():
    assert not inspect.isabstract(EnumerableTypeDefinition)


def test_enumerabletypedefinition_constructor_exists():
    assert callable(EnumerableTypeDefinition.__init__)


def test_enumerabletypedefinition_constructor_args():
    sig = inspect.signature(EnumerableTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_arraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(model_ArrayTypeDefinition)


def test_model_arraytypedefinition_constructor_exists():
    assert callable(model_ArrayTypeDefinition.__init__)


def test_model_arraytypedefinition_constructor_args():
    sig = inspect.signature(model_ArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_integerrangetypedefinition_is_not_abstract():
    assert not inspect.isabstract(model_IntegerRangeTypeDefinition)


def test_model_integerrangetypedefinition_constructor_exists():
    assert callable(model_IntegerRangeTypeDefinition.__init__)


def test_model_integerrangetypedefinition_constructor_args():
    sig = inspect.signature(model_IntegerRangeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_enumerationtypedefinition_is_not_abstract():
    assert not inspect.isabstract(model_EnumerationTypeDefinition)


def test_model_enumerationtypedefinition_constructor_exists():
    assert callable(model_EnumerationTypeDefinition.__init__)


def test_model_enumerationtypedefinition_constructor_args():
    sig = inspect.signature(model_EnumerationTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_enumerabletypedefinition_is_not_abstract():
    assert not inspect.isabstract(model_EnumerableTypeDefinition)


def test_model_enumerabletypedefinition_constructor_exists():
    assert callable(model_EnumerableTypeDefinition.__init__)


def test_model_enumerabletypedefinition_constructor_args():
    sig = inspect.signature(model_EnumerableTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_model_valuedeclaration_is_not_abstract():
    assert not inspect.isabstract(model_ValueDeclaration)


def test_model_valuedeclaration_constructor_exists():
    assert callable(model_ValueDeclaration.__init__)


def test_model_valuedeclaration_constructor_args():
    sig = inspect.signature(model_ValueDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model_type_is_not_abstract():
    assert not inspect.isabstract(model_Type)


def test_model_type_constructor_exists():
    assert callable(model_Type.__init__)


def test_model_type_constructor_args():
    sig = inspect.signature(model_Type.__init__)
    params = list(sig.parameters.keys())



def test_model_basicconstraintdefinition_is_not_abstract():
    assert not inspect.isabstract(model_BasicConstraintDefinition)


def test_model_basicconstraintdefinition_constructor_exists():
    assert callable(model_BasicConstraintDefinition.__init__)


def test_model_basicconstraintdefinition_constructor_args():
    sig = inspect.signature(model_BasicConstraintDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(model_TypeDeclaration)


def test_model_typedeclaration_constructor_exists():
    assert callable(model_TypeDeclaration.__init__)


def test_model_typedeclaration_constructor_args():
    sig = inspect.signature(model_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_parametricelement_is_not_abstract():
    assert not inspect.isabstract(ParametricElement)


def test_parametricelement_constructor_exists():
    assert callable(ParametricElement.__init__)


def test_parametricelement_constructor_args():
    sig = inspect.signature(ParametricElement.__init__)
    params = list(sig.parameters.keys())



def test_model_quantifierexpression_is_not_abstract():
    assert not inspect.isabstract(model_QuantifierExpression)


def test_model_quantifierexpression_constructor_exists():
    assert callable(model_QuantifierExpression.__init__)


def test_model_quantifierexpression_constructor_args():
    sig = inspect.signature(model_QuantifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(model_FunctionDeclaration)


def test_model_functiondeclaration_constructor_exists():
    assert callable(model_FunctionDeclaration.__init__)


def test_model_functiondeclaration_constructor_args():
    sig = inspect.signature(model_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_model_initializableelement_is_not_abstract():
    assert not inspect.isabstract(model_InitializableElement)


def test_model_initializableelement_constructor_exists():
    assert callable(model_InitializableElement.__init__)


def test_model_initializableelement_constructor_args():
    sig = inspect.signature(model_InitializableElement.__init__)
    params = list(sig.parameters.keys())



def test_model_declaration_is_not_abstract():
    assert not inspect.isabstract(model_Declaration)


def test_model_declaration_constructor_exists():
    assert callable(model_Declaration.__init__)


def test_model_declaration_constructor_args():
    sig = inspect.signature(model_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_model_enumerationliteraldefinition_is_not_abstract():
    assert not inspect.isabstract(model_EnumerationLiteralDefinition)


def test_model_enumerationliteraldefinition_constructor_exists():
    assert callable(model_EnumerationLiteralDefinition.__init__)


def test_model_enumerationliteraldefinition_constructor_args():
    sig = inspect.signature(model_EnumerationLiteralDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_expressionpackage_is_not_abstract():
    assert not inspect.isabstract(model_ExpressionPackage)


def test_model_expressionpackage_constructor_exists():
    assert callable(model_ExpressionPackage.__init__)


def test_model_expressionpackage_constructor_args():
    sig = inspect.signature(model_ExpressionPackage.__init__)
    params = list(sig.parameters.keys())



def test_numericaltypedefinition_is_not_abstract():
    assert not inspect.isabstract(NumericalTypeDefinition)


def test_numericaltypedefinition_constructor_exists():
    assert callable(NumericalTypeDefinition.__init__)


def test_numericaltypedefinition_constructor_args():
    sig = inspect.signature(NumericalTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_decimaltypedefinition_is_not_abstract():
    assert not inspect.isabstract(model_DecimalTypeDefinition)


def test_model_decimaltypedefinition_constructor_exists():
    assert callable(model_DecimalTypeDefinition.__init__)


def test_model_decimaltypedefinition_constructor_args():
    sig = inspect.signature(model_DecimalTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_subrangetypedefinition_is_not_abstract():
    assert not inspect.isabstract(model_SubrangeTypeDefinition)


def test_model_subrangetypedefinition_constructor_exists():
    assert callable(model_SubrangeTypeDefinition.__init__)


def test_model_subrangetypedefinition_constructor_args():
    sig = inspect.signature(model_SubrangeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_rationaltypedefinition_is_not_abstract():
    assert not inspect.isabstract(model_RationalTypeDefinition)


def test_model_rationaltypedefinition_constructor_exists():
    assert callable(model_RationalTypeDefinition.__init__)


def test_model_rationaltypedefinition_constructor_args():
    sig = inspect.signature(model_RationalTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_integertypedefinition_is_not_abstract():
    assert not inspect.isabstract(model_IntegerTypeDefinition)


def test_model_integertypedefinition_constructor_exists():
    assert callable(model_IntegerTypeDefinition.__init__)


def test_model_integertypedefinition_constructor_args():
    sig = inspect.signature(model_IntegerTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_booleantypedefinition_is_not_abstract():
    assert not inspect.isabstract(model_BooleanTypeDefinition)


def test_model_booleantypedefinition_constructor_exists():
    assert callable(model_BooleanTypeDefinition.__init__)


def test_model_booleantypedefinition_constructor_args():
    sig = inspect.signature(model_BooleanTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_voidtypedefinition_is_not_abstract():
    assert not inspect.isabstract(model_VoidTypeDefinition)


def test_model_voidtypedefinition_constructor_exists():
    assert callable(model_VoidTypeDefinition.__init__)


def test_model_voidtypedefinition_constructor_args():
    sig = inspect.signature(model_VoidTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_compositetypedefinition_is_not_abstract():
    assert not inspect.isabstract(model_CompositeTypeDefinition)


def test_model_compositetypedefinition_constructor_exists():
    assert callable(model_CompositeTypeDefinition.__init__)


def test_model_compositetypedefinition_constructor_args():
    sig = inspect.signature(model_CompositeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_numericaltypedefinition_is_not_abstract():
    assert not inspect.isabstract(model_NumericalTypeDefinition)


def test_model_numericaltypedefinition_constructor_exists():
    assert callable(model_NumericalTypeDefinition.__init__)


def test_model_numericaltypedefinition_constructor_args():
    sig = inspect.signature(model_NumericalTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_model_typedefinition_is_not_abstract():
    assert not inspect.isabstract(model_TypeDefinition)


def test_model_typedefinition_constructor_exists():
    assert callable(model_TypeDefinition.__init__)


def test_model_typedefinition_constructor_args():
    sig = inspect.signature(model_TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_model_typereference_is_not_abstract():
    assert not inspect.isabstract(model_TypeReference)


def test_model_typereference_constructor_exists():
    assert callable(model_TypeReference.__init__)


def test_model_typereference_constructor_args():
    sig = inspect.signature(model_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(FunctionDeclaration)


def test_functiondeclaration_constructor_exists():
    assert callable(FunctionDeclaration.__init__)


def test_functiondeclaration_constructor_args():
    sig = inspect.signature(FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_initializableelement_is_not_abstract():
    assert not inspect.isabstract(InitializableElement)


def test_initializableelement_constructor_exists():
    assert callable(InitializableElement.__init__)


def test_initializableelement_constructor_args():
    sig = inspect.signature(InitializableElement.__init__)
    params = list(sig.parameters.keys())



def test_model_lambdadeclaration_is_not_abstract():
    assert not inspect.isabstract(model_LambdaDeclaration)


def test_model_lambdadeclaration_constructor_exists():
    assert callable(model_LambdaDeclaration.__init__)


def test_model_lambdadeclaration_constructor_args():
    sig = inspect.signature(model_LambdaDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_valuedeclaration_is_not_abstract():
    assert not inspect.isabstract(ValueDeclaration)


def test_valuedeclaration_constructor_exists():
    assert callable(ValueDeclaration.__init__)


def test_valuedeclaration_constructor_args():
    sig = inspect.signature(ValueDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(model_FieldDeclaration)


def test_model_fielddeclaration_constructor_exists():
    assert callable(model_FieldDeclaration.__init__)


def test_model_fielddeclaration_constructor_args():
    sig = inspect.signature(model_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(model_ConstantDeclaration)


def test_model_constantdeclaration_constructor_exists():
    assert callable(model_ConstantDeclaration.__init__)


def test_model_constantdeclaration_constructor_args():
    sig = inspect.signature(model_ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(model_VariableDeclaration)


def test_model_variabledeclaration_constructor_exists():
    assert callable(model_VariableDeclaration.__init__)


def test_model_variabledeclaration_constructor_args():
    sig = inspect.signature(model_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model_comment_is_not_abstract():
    assert not inspect.isabstract(model_Comment)


def test_model_comment_constructor_exists():
    assert callable(model_Comment.__init__)


def test_model_comment_constructor_args():
    sig = inspect.signature(model_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_model_comment_has_comment():
    assert hasattr(model_Comment, "comment")
    descriptor = None
    for klass in model_Comment.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_model_commentableelement_is_not_abstract():
    assert not inspect.isabstract(model_CommentableElement)


def test_model_commentableelement_constructor_exists():
    assert callable(model_CommentableElement.__init__)


def test_model_commentableelement_constructor_args():
    sig = inspect.signature(model_CommentableElement.__init__)
    params = list(sig.parameters.keys())



def test_model_namedelement_is_not_abstract():
    assert not inspect.isabstract(model_NamedElement)


def test_model_namedelement_constructor_exists():
    assert callable(model_NamedElement.__init__)


def test_model_namedelement_constructor_args():
    sig = inspect.signature(model_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_namedelement_has_name():
    assert hasattr(model_NamedElement, "name")
    descriptor = None
    for klass in model_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_expression_is_not_abstract():
    assert not inspect.isabstract(model_Expression)


def test_model_expression_constructor_exists():
    assert callable(model_Expression.__init__)


def test_model_expression_constructor_args():
    sig = inspect.signature(model_Expression.__init__)
    params = list(sig.parameters.keys())



def test_model_argumentedelement_is_not_abstract():
    assert not inspect.isabstract(model_ArgumentedElement)


def test_model_argumentedelement_constructor_exists():
    assert callable(model_ArgumentedElement.__init__)


def test_model_argumentedelement_constructor_args():
    sig = inspect.signature(model_ArgumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_model_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(model_ParameterDeclaration)


def test_model_parameterdeclaration_constructor_exists():
    assert callable(model_ParameterDeclaration.__init__)


def test_model_parameterdeclaration_constructor_args():
    sig = inspect.signature(model_ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model_parametricelement_is_not_abstract():
    assert not inspect.isabstract(model_ParametricElement)


def test_model_parametricelement_constructor_exists():
    assert callable(model_ParametricElement.__init__)


def test_model_parametricelement_constructor_args():
    sig = inspect.signature(model_ParametricElement.__init__)
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
ComparisonExpression_strategy = st.builds(
    ComparisonExpression,
)
model_GreaterEqualExpression_strategy = st.builds(
    model_GreaterEqualExpression,
)
model_GreaterExpression_strategy = st.builds(
    model_GreaterExpression,
)
EquivalenceExpression_strategy = st.builds(
    EquivalenceExpression,
)
model_InequalityExpression_strategy = st.builds(
    model_InequalityExpression,
)
model_EqualityExpression_strategy = st.builds(
    model_EqualityExpression,
)
PredicateExpression_strategy = st.builds(
    PredicateExpression,
)
QuantifierExpression_strategy = st.builds(
    QuantifierExpression,
)
model_ExistsExpression_strategy = st.builds(
    model_ExistsExpression,
)
model_ForallExpression_strategy = st.builds(
    model_ForallExpression,
)
ArgumentedElement_strategy = st.builds(
    ArgumentedElement,
)
AccessExpression_strategy = st.builds(
    AccessExpression,
)
model_SelectExpression_strategy = st.builds(
    model_SelectExpression,
)
model_RecordAccessExpression_strategy = st.builds(
    model_RecordAccessExpression,
    field=
        safe_text
)
model_ArrayAccessExpression_strategy = st.builds(
    model_ArrayAccessExpression,
)
model_FunctionAccessExpression_strategy = st.builds(
    model_FunctionAccessExpression,
)
model_LessEqualExpression_strategy = st.builds(
    model_LessEqualExpression,
)
model_LessExpression_strategy = st.builds(
    model_LessExpression,
)
BooleanLiteralExpression_strategy = st.builds(
    BooleanLiteralExpression,
)
model_FalseExpression_strategy = st.builds(
    model_FalseExpression,
)
model_TrueExpression_strategy = st.builds(
    model_TrueExpression,
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
ArithmeticLiteralExpression_strategy = st.builds(
    ArithmeticLiteralExpression,
)
model_RationalLiteralExpression_strategy = st.builds(
    model_RationalLiteralExpression,
    numerator=
        safe_text,
    denominator=
        safe_text
)
model_DecimalLiteralExpression_strategy = st.builds(
    model_DecimalLiteralExpression,
    value=
        safe_text
)
model_IntegerLiteralExpression_strategy = st.builds(
    model_IntegerLiteralExpression,
    value=
        safe_text
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
model_FieldAssignment_strategy = st.builds(
    model_FieldAssignment,
    reference=
        safe_text
)
model_RecordLiteralExpression_strategy = st.builds(
    model_RecordLiteralExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
model_ImplyExpression_strategy = st.builds(
    model_ImplyExpression,
)
model_SubtractExpression_strategy = st.builds(
    model_SubtractExpression,
)
model_DivExpression_strategy = st.builds(
    model_DivExpression,
)
model_ModExpression_strategy = st.builds(
    model_ModExpression,
)
model_DivideExpression_strategy = st.builds(
    model_DivideExpression,
)
model_EquivalenceExpression_strategy = st.builds(
    model_EquivalenceExpression,
)
model_ComparisonExpression_strategy = st.builds(
    model_ComparisonExpression,
)
MultiaryExpression_strategy = st.builds(
    MultiaryExpression,
)
model_OrExpression_strategy = st.builds(
    model_OrExpression,
)
model_XorExpression_strategy = st.builds(
    model_XorExpression,
)
model_AndExpression_strategy = st.builds(
    model_AndExpression,
)
model_AddExpression_strategy = st.builds(
    model_AddExpression,
)
model_MultiplyExpression_strategy = st.builds(
    model_MultiplyExpression,
)
EnumerableExpression_strategy = st.builds(
    EnumerableExpression,
)
model_IntegerRangeLiteralExpression_strategy = st.builds(
    model_IntegerRangeLiteralExpression,
    leftInclusive=
        st.booleans(),
    rightInclusive=
        st.booleans()
)
model_ArrayLiteralExpression_strategy = st.builds(
    model_ArrayLiteralExpression,
)
Expression_strategy = st.builds(
    Expression,
)
model_EnumerableExpression_strategy = st.builds(
    model_EnumerableExpression,
)
model_UnaryExpression_strategy = st.builds(
    model_UnaryExpression,
)
model_LiteralExpression_strategy = st.builds(
    model_LiteralExpression,
)
model_AccessExpression_strategy = st.builds(
    model_AccessExpression,
)
model_IfThenElseExpression_strategy = st.builds(
    model_IfThenElseExpression,
)
model_NullaryExpression_strategy = st.builds(
    model_NullaryExpression,
)
ConstraintDefinition_strategy = st.builds(
    ConstraintDefinition,
)
model_ConstraintDefinition_strategy = st.builds(
    model_ConstraintDefinition,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
model_NotExpression_strategy = st.builds(
    model_NotExpression,
)
model_UnaryMinusExpression_strategy = st.builds(
    model_UnaryMinusExpression,
)
model_UnaryPlusExpression_strategy = st.builds(
    model_UnaryPlusExpression,
)
ElseExpression_strategy = st.builds(
    ElseExpression,
)
model_DefaultExpression_strategy = st.builds(
    model_DefaultExpression,
)
NullaryExpression_strategy = st.builds(
    NullaryExpression,
)
model_ArithmeticLiteralExpression_strategy = st.builds(
    model_ArithmeticLiteralExpression,
)
model_BooleanLiteralExpression_strategy = st.builds(
    model_BooleanLiteralExpression,
)
model_ReferenceExpression_strategy = st.builds(
    model_ReferenceExpression,
)
model_EnumerationLiteralExpression_strategy = st.builds(
    model_EnumerationLiteralExpression,
)
model_OpaqueExpression_strategy = st.builds(
    model_OpaqueExpression,
    expression=
        safe_text
)
LogicExpression_strategy = st.builds(
    LogicExpression,
)
model_PredicateExpression_strategy = st.builds(
    model_PredicateExpression,
)
model_ElseExpression_strategy = st.builds(
    model_ElseExpression,
)
model_BooleanExpression_strategy = st.builds(
    model_BooleanExpression,
)
model_LogicExpression_strategy = st.builds(
    model_LogicExpression,
)
model_ArithmeticExpression_strategy = st.builds(
    model_ArithmeticExpression,
)
model_MultiaryExpression_strategy = st.builds(
    model_MultiaryExpression,
)
model_BinaryExpression_strategy = st.builds(
    model_BinaryExpression,
)
CompositeTypeDefinition_strategy = st.builds(
    CompositeTypeDefinition,
)
model_FunctionTypeDefinition_strategy = st.builds(
    model_FunctionTypeDefinition,
)
model_RecordTypeDefinition_strategy = st.builds(
    model_RecordTypeDefinition,
)
EnumerableTypeDefinition_strategy = st.builds(
    EnumerableTypeDefinition,
)
model_ArrayTypeDefinition_strategy = st.builds(
    model_ArrayTypeDefinition,
)
model_IntegerRangeTypeDefinition_strategy = st.builds(
    model_IntegerRangeTypeDefinition,
)
model_EnumerationTypeDefinition_strategy = st.builds(
    model_EnumerationTypeDefinition,
)
model_EnumerableTypeDefinition_strategy = st.builds(
    model_EnumerableTypeDefinition,
)
Declaration_strategy = st.builds(
    Declaration,
)
model_ValueDeclaration_strategy = st.builds(
    model_ValueDeclaration,
)
model_Type_strategy = st.builds(
    model_Type,
)
model_BasicConstraintDefinition_strategy = st.builds(
    model_BasicConstraintDefinition,
)
model_TypeDeclaration_strategy = st.builds(
    model_TypeDeclaration,
)
ParametricElement_strategy = st.builds(
    ParametricElement,
)
model_QuantifierExpression_strategy = st.builds(
    model_QuantifierExpression,
)
model_FunctionDeclaration_strategy = st.builds(
    model_FunctionDeclaration,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
model_InitializableElement_strategy = st.builds(
    model_InitializableElement,
)
model_Declaration_strategy = st.builds(
    model_Declaration,
)
model_EnumerationLiteralDefinition_strategy = st.builds(
    model_EnumerationLiteralDefinition,
)
model_ExpressionPackage_strategy = st.builds(
    model_ExpressionPackage,
)
NumericalTypeDefinition_strategy = st.builds(
    NumericalTypeDefinition,
)
model_DecimalTypeDefinition_strategy = st.builds(
    model_DecimalTypeDefinition,
)
model_SubrangeTypeDefinition_strategy = st.builds(
    model_SubrangeTypeDefinition,
)
model_RationalTypeDefinition_strategy = st.builds(
    model_RationalTypeDefinition,
)
model_IntegerTypeDefinition_strategy = st.builds(
    model_IntegerTypeDefinition,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
model_BooleanTypeDefinition_strategy = st.builds(
    model_BooleanTypeDefinition,
)
model_VoidTypeDefinition_strategy = st.builds(
    model_VoidTypeDefinition,
)
model_CompositeTypeDefinition_strategy = st.builds(
    model_CompositeTypeDefinition,
)
model_NumericalTypeDefinition_strategy = st.builds(
    model_NumericalTypeDefinition,
)
Type_strategy = st.builds(
    Type,
)
model_TypeDefinition_strategy = st.builds(
    model_TypeDefinition,
)
model_TypeReference_strategy = st.builds(
    model_TypeReference,
)
FunctionDeclaration_strategy = st.builds(
    FunctionDeclaration,
)
InitializableElement_strategy = st.builds(
    InitializableElement,
)
model_LambdaDeclaration_strategy = st.builds(
    model_LambdaDeclaration,
)
ValueDeclaration_strategy = st.builds(
    ValueDeclaration,
)
model_FieldDeclaration_strategy = st.builds(
    model_FieldDeclaration,
)
model_ConstantDeclaration_strategy = st.builds(
    model_ConstantDeclaration,
)
model_VariableDeclaration_strategy = st.builds(
    model_VariableDeclaration,
)
model_Comment_strategy = st.builds(
    model_Comment,
    comment=
        safe_text
)
model_CommentableElement_strategy = st.builds(
    model_CommentableElement,
)
model_NamedElement_strategy = st.builds(
    model_NamedElement,
    name=
        safe_text
)
model_Expression_strategy = st.builds(
    model_Expression,
)
model_ArgumentedElement_strategy = st.builds(
    model_ArgumentedElement,
)
model_ParameterDeclaration_strategy = st.builds(
    model_ParameterDeclaration,
)
model_ParametricElement_strategy = st.builds(
    model_ParametricElement,
)

@given(instance=ComparisonExpression_strategy)
@settings(max_examples=50)
def test_comparisonexpression_instantiation(instance):
    assert isinstance(instance, ComparisonExpression)

@given(instance=model_GreaterEqualExpression_strategy)
@settings(max_examples=50)
def test_model_greaterequalexpression_instantiation(instance):
    assert isinstance(instance, model_GreaterEqualExpression)

@given(instance=model_GreaterExpression_strategy)
@settings(max_examples=50)
def test_model_greaterexpression_instantiation(instance):
    assert isinstance(instance, model_GreaterExpression)

@given(instance=EquivalenceExpression_strategy)
@settings(max_examples=50)
def test_equivalenceexpression_instantiation(instance):
    assert isinstance(instance, EquivalenceExpression)

@given(instance=model_InequalityExpression_strategy)
@settings(max_examples=50)
def test_model_inequalityexpression_instantiation(instance):
    assert isinstance(instance, model_InequalityExpression)

@given(instance=model_EqualityExpression_strategy)
@settings(max_examples=50)
def test_model_equalityexpression_instantiation(instance):
    assert isinstance(instance, model_EqualityExpression)

@given(instance=PredicateExpression_strategy)
@settings(max_examples=50)
def test_predicateexpression_instantiation(instance):
    assert isinstance(instance, PredicateExpression)

@given(instance=QuantifierExpression_strategy)
@settings(max_examples=50)
def test_quantifierexpression_instantiation(instance):
    assert isinstance(instance, QuantifierExpression)

@given(instance=model_ExistsExpression_strategy)
@settings(max_examples=50)
def test_model_existsexpression_instantiation(instance):
    assert isinstance(instance, model_ExistsExpression)

@given(instance=model_ForallExpression_strategy)
@settings(max_examples=50)
def test_model_forallexpression_instantiation(instance):
    assert isinstance(instance, model_ForallExpression)

@given(instance=ArgumentedElement_strategy)
@settings(max_examples=50)
def test_argumentedelement_instantiation(instance):
    assert isinstance(instance, ArgumentedElement)

@given(instance=AccessExpression_strategy)
@settings(max_examples=50)
def test_accessexpression_instantiation(instance):
    assert isinstance(instance, AccessExpression)

@given(instance=model_SelectExpression_strategy)
@settings(max_examples=50)
def test_model_selectexpression_instantiation(instance):
    assert isinstance(instance, model_SelectExpression)

@given(instance=model_RecordAccessExpression_strategy)
@settings(max_examples=50)
def test_model_recordaccessexpression_instantiation(instance):
    assert isinstance(instance, model_RecordAccessExpression)



@given(instance=model_RecordAccessExpression_strategy)
def test_model_recordaccessexpression_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=model_ArrayAccessExpression_strategy)
@settings(max_examples=50)
def test_model_arrayaccessexpression_instantiation(instance):
    assert isinstance(instance, model_ArrayAccessExpression)

@given(instance=model_FunctionAccessExpression_strategy)
@settings(max_examples=50)
def test_model_functionaccessexpression_instantiation(instance):
    assert isinstance(instance, model_FunctionAccessExpression)

@given(instance=model_LessEqualExpression_strategy)
@settings(max_examples=50)
def test_model_lessequalexpression_instantiation(instance):
    assert isinstance(instance, model_LessEqualExpression)

@given(instance=model_LessExpression_strategy)
@settings(max_examples=50)
def test_model_lessexpression_instantiation(instance):
    assert isinstance(instance, model_LessExpression)

@given(instance=BooleanLiteralExpression_strategy)
@settings(max_examples=50)
def test_booleanliteralexpression_instantiation(instance):
    assert isinstance(instance, BooleanLiteralExpression)

@given(instance=model_FalseExpression_strategy)
@settings(max_examples=50)
def test_model_falseexpression_instantiation(instance):
    assert isinstance(instance, model_FalseExpression)

@given(instance=model_TrueExpression_strategy)
@settings(max_examples=50)
def test_model_trueexpression_instantiation(instance):
    assert isinstance(instance, model_TrueExpression)

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=ArithmeticLiteralExpression_strategy)
@settings(max_examples=50)
def test_arithmeticliteralexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticLiteralExpression)

@given(instance=model_RationalLiteralExpression_strategy)
@settings(max_examples=50)
def test_model_rationalliteralexpression_instantiation(instance):
    assert isinstance(instance, model_RationalLiteralExpression)



@given(instance=model_RationalLiteralExpression_strategy)
def test_model_rationalliteralexpression_numerator_setter(instance):
    original = instance.numerator
    instance.numerator = original
    assert instance.numerator == original



@given(instance=model_RationalLiteralExpression_strategy)
def test_model_rationalliteralexpression_denominator_setter(instance):
    original = instance.denominator
    instance.denominator = original
    assert instance.denominator == original

@given(instance=model_DecimalLiteralExpression_strategy)
@settings(max_examples=50)
def test_model_decimalliteralexpression_instantiation(instance):
    assert isinstance(instance, model_DecimalLiteralExpression)



@given(instance=model_DecimalLiteralExpression_strategy)
def test_model_decimalliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model_IntegerLiteralExpression_strategy)
@settings(max_examples=50)
def test_model_integerliteralexpression_instantiation(instance):
    assert isinstance(instance, model_IntegerLiteralExpression)



@given(instance=model_IntegerLiteralExpression_strategy)
def test_model_integerliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=LiteralExpression_strategy)
@settings(max_examples=50)
def test_literalexpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)

@given(instance=model_FieldAssignment_strategy)
@settings(max_examples=50)
def test_model_fieldassignment_instantiation(instance):
    assert isinstance(instance, model_FieldAssignment)



@given(instance=model_FieldAssignment_strategy)
def test_model_fieldassignment_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=model_RecordLiteralExpression_strategy)
@settings(max_examples=50)
def test_model_recordliteralexpression_instantiation(instance):
    assert isinstance(instance, model_RecordLiteralExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=model_ImplyExpression_strategy)
@settings(max_examples=50)
def test_model_implyexpression_instantiation(instance):
    assert isinstance(instance, model_ImplyExpression)

@given(instance=model_SubtractExpression_strategy)
@settings(max_examples=50)
def test_model_subtractexpression_instantiation(instance):
    assert isinstance(instance, model_SubtractExpression)

@given(instance=model_DivExpression_strategy)
@settings(max_examples=50)
def test_model_divexpression_instantiation(instance):
    assert isinstance(instance, model_DivExpression)

@given(instance=model_ModExpression_strategy)
@settings(max_examples=50)
def test_model_modexpression_instantiation(instance):
    assert isinstance(instance, model_ModExpression)

@given(instance=model_DivideExpression_strategy)
@settings(max_examples=50)
def test_model_divideexpression_instantiation(instance):
    assert isinstance(instance, model_DivideExpression)

@given(instance=model_EquivalenceExpression_strategy)
@settings(max_examples=50)
def test_model_equivalenceexpression_instantiation(instance):
    assert isinstance(instance, model_EquivalenceExpression)

@given(instance=model_ComparisonExpression_strategy)
@settings(max_examples=50)
def test_model_comparisonexpression_instantiation(instance):
    assert isinstance(instance, model_ComparisonExpression)

@given(instance=MultiaryExpression_strategy)
@settings(max_examples=50)
def test_multiaryexpression_instantiation(instance):
    assert isinstance(instance, MultiaryExpression)

@given(instance=model_OrExpression_strategy)
@settings(max_examples=50)
def test_model_orexpression_instantiation(instance):
    assert isinstance(instance, model_OrExpression)

@given(instance=model_XorExpression_strategy)
@settings(max_examples=50)
def test_model_xorexpression_instantiation(instance):
    assert isinstance(instance, model_XorExpression)

@given(instance=model_AndExpression_strategy)
@settings(max_examples=50)
def test_model_andexpression_instantiation(instance):
    assert isinstance(instance, model_AndExpression)

@given(instance=model_AddExpression_strategy)
@settings(max_examples=50)
def test_model_addexpression_instantiation(instance):
    assert isinstance(instance, model_AddExpression)

@given(instance=model_MultiplyExpression_strategy)
@settings(max_examples=50)
def test_model_multiplyexpression_instantiation(instance):
    assert isinstance(instance, model_MultiplyExpression)

@given(instance=EnumerableExpression_strategy)
@settings(max_examples=50)
def test_enumerableexpression_instantiation(instance):
    assert isinstance(instance, EnumerableExpression)

@given(instance=model_IntegerRangeLiteralExpression_strategy)
@settings(max_examples=50)
def test_model_integerrangeliteralexpression_instantiation(instance):
    assert isinstance(instance, model_IntegerRangeLiteralExpression)



@given(instance=model_IntegerRangeLiteralExpression_strategy)
def test_model_integerrangeliteralexpression_leftInclusive_setter(instance):
    original = instance.leftInclusive
    instance.leftInclusive = original
    assert instance.leftInclusive == original



@given(instance=model_IntegerRangeLiteralExpression_strategy)
def test_model_integerrangeliteralexpression_rightInclusive_setter(instance):
    original = instance.rightInclusive
    instance.rightInclusive = original
    assert instance.rightInclusive == original

@given(instance=model_ArrayLiteralExpression_strategy)
@settings(max_examples=50)
def test_model_arrayliteralexpression_instantiation(instance):
    assert isinstance(instance, model_ArrayLiteralExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=model_EnumerableExpression_strategy)
@settings(max_examples=50)
def test_model_enumerableexpression_instantiation(instance):
    assert isinstance(instance, model_EnumerableExpression)

@given(instance=model_UnaryExpression_strategy)
@settings(max_examples=50)
def test_model_unaryexpression_instantiation(instance):
    assert isinstance(instance, model_UnaryExpression)

@given(instance=model_LiteralExpression_strategy)
@settings(max_examples=50)
def test_model_literalexpression_instantiation(instance):
    assert isinstance(instance, model_LiteralExpression)

@given(instance=model_AccessExpression_strategy)
@settings(max_examples=50)
def test_model_accessexpression_instantiation(instance):
    assert isinstance(instance, model_AccessExpression)

@given(instance=model_IfThenElseExpression_strategy)
@settings(max_examples=50)
def test_model_ifthenelseexpression_instantiation(instance):
    assert isinstance(instance, model_IfThenElseExpression)

@given(instance=model_NullaryExpression_strategy)
@settings(max_examples=50)
def test_model_nullaryexpression_instantiation(instance):
    assert isinstance(instance, model_NullaryExpression)

@given(instance=ConstraintDefinition_strategy)
@settings(max_examples=50)
def test_constraintdefinition_instantiation(instance):
    assert isinstance(instance, ConstraintDefinition)

@given(instance=model_ConstraintDefinition_strategy)
@settings(max_examples=50)
def test_model_constraintdefinition_instantiation(instance):
    assert isinstance(instance, model_ConstraintDefinition)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=model_NotExpression_strategy)
@settings(max_examples=50)
def test_model_notexpression_instantiation(instance):
    assert isinstance(instance, model_NotExpression)

@given(instance=model_UnaryMinusExpression_strategy)
@settings(max_examples=50)
def test_model_unaryminusexpression_instantiation(instance):
    assert isinstance(instance, model_UnaryMinusExpression)

@given(instance=model_UnaryPlusExpression_strategy)
@settings(max_examples=50)
def test_model_unaryplusexpression_instantiation(instance):
    assert isinstance(instance, model_UnaryPlusExpression)

@given(instance=ElseExpression_strategy)
@settings(max_examples=50)
def test_elseexpression_instantiation(instance):
    assert isinstance(instance, ElseExpression)

@given(instance=model_DefaultExpression_strategy)
@settings(max_examples=50)
def test_model_defaultexpression_instantiation(instance):
    assert isinstance(instance, model_DefaultExpression)

@given(instance=NullaryExpression_strategy)
@settings(max_examples=50)
def test_nullaryexpression_instantiation(instance):
    assert isinstance(instance, NullaryExpression)

@given(instance=model_ArithmeticLiteralExpression_strategy)
@settings(max_examples=50)
def test_model_arithmeticliteralexpression_instantiation(instance):
    assert isinstance(instance, model_ArithmeticLiteralExpression)

@given(instance=model_BooleanLiteralExpression_strategy)
@settings(max_examples=50)
def test_model_booleanliteralexpression_instantiation(instance):
    assert isinstance(instance, model_BooleanLiteralExpression)

@given(instance=model_ReferenceExpression_strategy)
@settings(max_examples=50)
def test_model_referenceexpression_instantiation(instance):
    assert isinstance(instance, model_ReferenceExpression)

@given(instance=model_EnumerationLiteralExpression_strategy)
@settings(max_examples=50)
def test_model_enumerationliteralexpression_instantiation(instance):
    assert isinstance(instance, model_EnumerationLiteralExpression)

@given(instance=model_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_model_opaqueexpression_instantiation(instance):
    assert isinstance(instance, model_OpaqueExpression)



@given(instance=model_OpaqueExpression_strategy)
def test_model_opaqueexpression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=LogicExpression_strategy)
@settings(max_examples=50)
def test_logicexpression_instantiation(instance):
    assert isinstance(instance, LogicExpression)

@given(instance=model_PredicateExpression_strategy)
@settings(max_examples=50)
def test_model_predicateexpression_instantiation(instance):
    assert isinstance(instance, model_PredicateExpression)

@given(instance=model_ElseExpression_strategy)
@settings(max_examples=50)
def test_model_elseexpression_instantiation(instance):
    assert isinstance(instance, model_ElseExpression)

@given(instance=model_BooleanExpression_strategy)
@settings(max_examples=50)
def test_model_booleanexpression_instantiation(instance):
    assert isinstance(instance, model_BooleanExpression)

@given(instance=model_LogicExpression_strategy)
@settings(max_examples=50)
def test_model_logicexpression_instantiation(instance):
    assert isinstance(instance, model_LogicExpression)

@given(instance=model_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_model_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, model_ArithmeticExpression)

@given(instance=model_MultiaryExpression_strategy)
@settings(max_examples=50)
def test_model_multiaryexpression_instantiation(instance):
    assert isinstance(instance, model_MultiaryExpression)

@given(instance=model_BinaryExpression_strategy)
@settings(max_examples=50)
def test_model_binaryexpression_instantiation(instance):
    assert isinstance(instance, model_BinaryExpression)

@given(instance=CompositeTypeDefinition_strategy)
@settings(max_examples=50)
def test_compositetypedefinition_instantiation(instance):
    assert isinstance(instance, CompositeTypeDefinition)

@given(instance=model_FunctionTypeDefinition_strategy)
@settings(max_examples=50)
def test_model_functiontypedefinition_instantiation(instance):
    assert isinstance(instance, model_FunctionTypeDefinition)

@given(instance=model_RecordTypeDefinition_strategy)
@settings(max_examples=50)
def test_model_recordtypedefinition_instantiation(instance):
    assert isinstance(instance, model_RecordTypeDefinition)

@given(instance=EnumerableTypeDefinition_strategy)
@settings(max_examples=50)
def test_enumerabletypedefinition_instantiation(instance):
    assert isinstance(instance, EnumerableTypeDefinition)

@given(instance=model_ArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_model_arraytypedefinition_instantiation(instance):
    assert isinstance(instance, model_ArrayTypeDefinition)

@given(instance=model_IntegerRangeTypeDefinition_strategy)
@settings(max_examples=50)
def test_model_integerrangetypedefinition_instantiation(instance):
    assert isinstance(instance, model_IntegerRangeTypeDefinition)

@given(instance=model_EnumerationTypeDefinition_strategy)
@settings(max_examples=50)
def test_model_enumerationtypedefinition_instantiation(instance):
    assert isinstance(instance, model_EnumerationTypeDefinition)

@given(instance=model_EnumerableTypeDefinition_strategy)
@settings(max_examples=50)
def test_model_enumerabletypedefinition_instantiation(instance):
    assert isinstance(instance, model_EnumerableTypeDefinition)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=model_ValueDeclaration_strategy)
@settings(max_examples=50)
def test_model_valuedeclaration_instantiation(instance):
    assert isinstance(instance, model_ValueDeclaration)

@given(instance=model_Type_strategy)
@settings(max_examples=50)
def test_model_type_instantiation(instance):
    assert isinstance(instance, model_Type)

@given(instance=model_BasicConstraintDefinition_strategy)
@settings(max_examples=50)
def test_model_basicconstraintdefinition_instantiation(instance):
    assert isinstance(instance, model_BasicConstraintDefinition)

@given(instance=model_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_model_typedeclaration_instantiation(instance):
    assert isinstance(instance, model_TypeDeclaration)

@given(instance=ParametricElement_strategy)
@settings(max_examples=50)
def test_parametricelement_instantiation(instance):
    assert isinstance(instance, ParametricElement)

@given(instance=model_QuantifierExpression_strategy)
@settings(max_examples=50)
def test_model_quantifierexpression_instantiation(instance):
    assert isinstance(instance, model_QuantifierExpression)

@given(instance=model_FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_model_functiondeclaration_instantiation(instance):
    assert isinstance(instance, model_FunctionDeclaration)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=model_InitializableElement_strategy)
@settings(max_examples=50)
def test_model_initializableelement_instantiation(instance):
    assert isinstance(instance, model_InitializableElement)

@given(instance=model_Declaration_strategy)
@settings(max_examples=50)
def test_model_declaration_instantiation(instance):
    assert isinstance(instance, model_Declaration)

@given(instance=model_EnumerationLiteralDefinition_strategy)
@settings(max_examples=50)
def test_model_enumerationliteraldefinition_instantiation(instance):
    assert isinstance(instance, model_EnumerationLiteralDefinition)

@given(instance=model_ExpressionPackage_strategy)
@settings(max_examples=50)
def test_model_expressionpackage_instantiation(instance):
    assert isinstance(instance, model_ExpressionPackage)

@given(instance=NumericalTypeDefinition_strategy)
@settings(max_examples=50)
def test_numericaltypedefinition_instantiation(instance):
    assert isinstance(instance, NumericalTypeDefinition)

@given(instance=model_DecimalTypeDefinition_strategy)
@settings(max_examples=50)
def test_model_decimaltypedefinition_instantiation(instance):
    assert isinstance(instance, model_DecimalTypeDefinition)

@given(instance=model_SubrangeTypeDefinition_strategy)
@settings(max_examples=50)
def test_model_subrangetypedefinition_instantiation(instance):
    assert isinstance(instance, model_SubrangeTypeDefinition)

@given(instance=model_RationalTypeDefinition_strategy)
@settings(max_examples=50)
def test_model_rationaltypedefinition_instantiation(instance):
    assert isinstance(instance, model_RationalTypeDefinition)

@given(instance=model_IntegerTypeDefinition_strategy)
@settings(max_examples=50)
def test_model_integertypedefinition_instantiation(instance):
    assert isinstance(instance, model_IntegerTypeDefinition)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=model_BooleanTypeDefinition_strategy)
@settings(max_examples=50)
def test_model_booleantypedefinition_instantiation(instance):
    assert isinstance(instance, model_BooleanTypeDefinition)

@given(instance=model_VoidTypeDefinition_strategy)
@settings(max_examples=50)
def test_model_voidtypedefinition_instantiation(instance):
    assert isinstance(instance, model_VoidTypeDefinition)

@given(instance=model_CompositeTypeDefinition_strategy)
@settings(max_examples=50)
def test_model_compositetypedefinition_instantiation(instance):
    assert isinstance(instance, model_CompositeTypeDefinition)

@given(instance=model_NumericalTypeDefinition_strategy)
@settings(max_examples=50)
def test_model_numericaltypedefinition_instantiation(instance):
    assert isinstance(instance, model_NumericalTypeDefinition)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=model_TypeDefinition_strategy)
@settings(max_examples=50)
def test_model_typedefinition_instantiation(instance):
    assert isinstance(instance, model_TypeDefinition)

@given(instance=model_TypeReference_strategy)
@settings(max_examples=50)
def test_model_typereference_instantiation(instance):
    assert isinstance(instance, model_TypeReference)

@given(instance=FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_functiondeclaration_instantiation(instance):
    assert isinstance(instance, FunctionDeclaration)

@given(instance=InitializableElement_strategy)
@settings(max_examples=50)
def test_initializableelement_instantiation(instance):
    assert isinstance(instance, InitializableElement)

@given(instance=model_LambdaDeclaration_strategy)
@settings(max_examples=50)
def test_model_lambdadeclaration_instantiation(instance):
    assert isinstance(instance, model_LambdaDeclaration)

@given(instance=ValueDeclaration_strategy)
@settings(max_examples=50)
def test_valuedeclaration_instantiation(instance):
    assert isinstance(instance, ValueDeclaration)

@given(instance=model_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_model_fielddeclaration_instantiation(instance):
    assert isinstance(instance, model_FieldDeclaration)

@given(instance=model_ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_model_constantdeclaration_instantiation(instance):
    assert isinstance(instance, model_ConstantDeclaration)

@given(instance=model_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_model_variabledeclaration_instantiation(instance):
    assert isinstance(instance, model_VariableDeclaration)

@given(instance=model_Comment_strategy)
@settings(max_examples=50)
def test_model_comment_instantiation(instance):
    assert isinstance(instance, model_Comment)



@given(instance=model_Comment_strategy)
def test_model_comment_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=model_CommentableElement_strategy)
@settings(max_examples=50)
def test_model_commentableelement_instantiation(instance):
    assert isinstance(instance, model_CommentableElement)

@given(instance=model_NamedElement_strategy)
@settings(max_examples=50)
def test_model_namedelement_instantiation(instance):
    assert isinstance(instance, model_NamedElement)



@given(instance=model_NamedElement_strategy)
def test_model_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_Expression_strategy)
@settings(max_examples=50)
def test_model_expression_instantiation(instance):
    assert isinstance(instance, model_Expression)

@given(instance=model_ArgumentedElement_strategy)
@settings(max_examples=50)
def test_model_argumentedelement_instantiation(instance):
    assert isinstance(instance, model_ArgumentedElement)

@given(instance=model_ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_model_parameterdeclaration_instantiation(instance):
    assert isinstance(instance, model_ParameterDeclaration)

@given(instance=model_ParametricElement_strategy)
@settings(max_examples=50)
def test_model_parametricelement_instantiation(instance):
    assert isinstance(instance, model_ParametricElement)
