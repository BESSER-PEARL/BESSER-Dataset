import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ParametrizedElement,
    AccessExpression,
    TTMCConstraint_TupleAccessExpression,
    TTMCConstraint_RecordAccessExpression,
    TTMCConstraint_ArrayAccessExpression,
    TTMCConstraint_FunctionAccessExpression,
    EquivalenceExpression,
    TTMCConstraint_InequalityExpression,
    TTMCConstraint_EqualityExpression,
    PredicateExpression,
    TemporalStateExpression,
    QuantifierExpression,
    TTMCConstraint_ExistsExpression,
    TTMCConstraint_ForallExpression,
    TemporalPathExpression,
    MultiaryExpression,
    BinaryExpression,
    TTMCConstraint_EquivalenceExpression,
    TTMCConstraint_ReleaseExpression,
    TTMCConstraint_UntilExpression,
    ComparisionExpression,
    TTMCConstraint_GreaterEqualExpression,
    TTMCConstraint_LessExpression,
    TTMCConstraint_LessEqualExpression,
    TTMCConstraint_GreaterExpression,
    TTMCConstraint_ComparisionExpression,
    TTMCConstraint_FieldAssignment,
    BooleanLiteralExpression,
    TTMCConstraint_FalseExpression,
    TTMCConstraint_TrueExpression,
    BooleanExpression,
    TTMCConstraint_EqualExpression,
    TTMCConstraint_OrExpression,
    TTMCConstraint_AndExpression,
    TTMCConstraint_ImplyExpression,
    ArithmeticLiteralExpression,
    TTMCConstraint_RationalLiteralExpression,
    TTMCConstraint_DecimalLiteralExpression,
    TTMCConstraint_IntegerLiteralExpression,
    Expression,
    TTMCConstraint_ArithmeticExpression,
    TTMCConstraint_UnaryExpression,
    TTMCConstraint_LetExpression,
    TTMCConstraint_MultiaryExpression,
    TTMCConstraint_IfThenElseExpression,
    TTMCConstraint_PredicateExpression,
    TTMCConstraint_BinaryExpression,
    TTMCConstraint_AccessExpression,
    TTMCConstraint_NullaryExpression,
    ConstraintDefinition,
    TTMCConstraint_ConstraintDefinition,
    ArithmeticExpression,
    TTMCConstraint_DivExpression,
    TTMCConstraint_MultiplyExpression,
    TTMCConstraint_SubtractExpression,
    TTMCConstraint_ModExpression,
    TTMCConstraint_DivideExpression,
    TTMCConstraint_AddExpression,
    LiteralExpression,
    TTMCConstraint_RecordLiteralExpression,
    TTMCConstraint_TupleLiteralExpression,
    NullaryExpression,
    TTMCConstraint_BooleanLiteralExpression,
    TTMCConstraint_ReferenceExpression,
    TTMCConstraint_EnumerationLiteralExpression,
    TTMCConstraint_ArithmeticLiteralExpression,
    TTMCConstraint_LiteralExpression,
    TemporalExpression,
    TTMCConstraint_TemporalStateExpression,
    TTMCConstraint_TemporalPathExpression,
    TTMCConstraint_TemporalExpression,
    UnaryExpression,
    TTMCConstraint_TemporalExistsExpression,
    TTMCConstraint_GloballyExpression,
    TTMCConstraint_UnaryMinusExpression,
    TTMCConstraint_TemporalForallExpression,
    TTMCConstraint_UnaryPlusExpression,
    TTMCConstraint_NotExpression,
    TTMCConstraint_InExpression,
    TTMCConstraint_PrimedExpression,
    TTMCConstraint_NextExpression,
    TTMCConstraint_FinallyExpression,
    TTMCConstraint_BooleanExpression,
    BasicTypeDefinition,
    TTMCConstraint_RealTypeDefinition,
    TTMCConstraint_NaturalTypeDefinition,
    TTMCConstraint_BooleanTypeDefinition,
    TTMCConstraint_IntegerTypeDefinition,
    TypeDefinition,
    TTMCConstraint_RecordTypeDefinition,
    TTMCConstraint_SubrangeTypeDefinition,
    TTMCConstraint_EnumerationTypeDefinition,
    TTMCConstraint_TupleTypeDefinition,
    TTMCConstraint_BasicTypeDefinition,
    Type,
    TTMCConstraint_TypeDefinition,
    TTMCConstraint_TypeReference,
    TTMCConstraint_ArrayTypeDefinition,
    TTMCConstraint_FunctionTypeDefinition,
    TTMCConstraint_BasicConstraintDefinition,
    ParametricElement,
    TTMCConstraint_FunctionLiteralExpression,
    TTMCConstraint_ArrayLiteralExpression,
    TTMCConstraint_SubTypeDefinition,
    TTMCConstraint_QuantifierExpression,
    NamedElement,
    TTMCConstraint_Declaration,
    TTMCConstraint_TypeDeclaration,
    TTMCConstraint_EnumerationLiteralDefinition,
    TTMCConstraint_ConstraintSpecification,
    TTMCConstraint_Expression,
    TTMCConstraint_ParametrizedElement,
    TTMCConstraint_ParametricElement,
    TTMCConstraint_NamedElement,
    DefinableDeclaration,
    TTMCConstraint_ConstantDeclaration,
    TTMCConstraint_FunctionDeclaration,
    TTMCConstraint_LetDeclaration,
    Declaration,
    TTMCConstraint_ParameterDeclaration,
    TTMCConstraint_FieldDeclaration,
    TTMCConstraint_DefinableDeclaration,
    TTMCConstraint_Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_parametrizedelement_is_not_abstract():
    assert not inspect.isabstract(ParametrizedElement)


def test_parametrizedelement_constructor_exists():
    assert callable(ParametrizedElement.__init__)


def test_parametrizedelement_constructor_args():
    sig = inspect.signature(ParametrizedElement.__init__)
    params = list(sig.parameters.keys())



def test_accessexpression_is_not_abstract():
    assert not inspect.isabstract(AccessExpression)


def test_accessexpression_constructor_exists():
    assert callable(AccessExpression.__init__)


def test_accessexpression_constructor_args():
    sig = inspect.signature(AccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_tupleaccessexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_TupleAccessExpression)


def test_ttmcconstraint_tupleaccessexpression_constructor_exists():
    assert callable(TTMCConstraint_TupleAccessExpression.__init__)


def test_ttmcconstraint_tupleaccessexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_TupleAccessExpression.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_ttmcconstraint_tupleaccessexpression_has_index():
    assert hasattr(TTMCConstraint_TupleAccessExpression, "index")
    descriptor = None
    for klass in TTMCConstraint_TupleAccessExpression.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_ttmcconstraint_recordaccessexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_RecordAccessExpression)


def test_ttmcconstraint_recordaccessexpression_constructor_exists():
    assert callable(TTMCConstraint_RecordAccessExpression.__init__)


def test_ttmcconstraint_recordaccessexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_RecordAccessExpression.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_ttmcconstraint_recordaccessexpression_has_field():
    assert hasattr(TTMCConstraint_RecordAccessExpression, "field")
    descriptor = None
    for klass in TTMCConstraint_RecordAccessExpression.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_ttmcconstraint_arrayaccessexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ArrayAccessExpression)


def test_ttmcconstraint_arrayaccessexpression_constructor_exists():
    assert callable(TTMCConstraint_ArrayAccessExpression.__init__)


def test_ttmcconstraint_arrayaccessexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_ArrayAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_functionaccessexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_FunctionAccessExpression)


def test_ttmcconstraint_functionaccessexpression_constructor_exists():
    assert callable(TTMCConstraint_FunctionAccessExpression.__init__)


def test_ttmcconstraint_functionaccessexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_FunctionAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_equivalenceexpression_is_not_abstract():
    assert not inspect.isabstract(EquivalenceExpression)


def test_equivalenceexpression_constructor_exists():
    assert callable(EquivalenceExpression.__init__)


def test_equivalenceexpression_constructor_args():
    sig = inspect.signature(EquivalenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_inequalityexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_InequalityExpression)


def test_ttmcconstraint_inequalityexpression_constructor_exists():
    assert callable(TTMCConstraint_InequalityExpression.__init__)


def test_ttmcconstraint_inequalityexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_InequalityExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_EqualityExpression)


def test_ttmcconstraint_equalityexpression_constructor_exists():
    assert callable(TTMCConstraint_EqualityExpression.__init__)


def test_ttmcconstraint_equalityexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_predicateexpression_is_not_abstract():
    assert not inspect.isabstract(PredicateExpression)


def test_predicateexpression_constructor_exists():
    assert callable(PredicateExpression.__init__)


def test_predicateexpression_constructor_args():
    sig = inspect.signature(PredicateExpression.__init__)
    params = list(sig.parameters.keys())



def test_temporalstateexpression_is_not_abstract():
    assert not inspect.isabstract(TemporalStateExpression)


def test_temporalstateexpression_constructor_exists():
    assert callable(TemporalStateExpression.__init__)


def test_temporalstateexpression_constructor_args():
    sig = inspect.signature(TemporalStateExpression.__init__)
    params = list(sig.parameters.keys())



def test_quantifierexpression_is_not_abstract():
    assert not inspect.isabstract(QuantifierExpression)


def test_quantifierexpression_constructor_exists():
    assert callable(QuantifierExpression.__init__)


def test_quantifierexpression_constructor_args():
    sig = inspect.signature(QuantifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_existsexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ExistsExpression)


def test_ttmcconstraint_existsexpression_constructor_exists():
    assert callable(TTMCConstraint_ExistsExpression.__init__)


def test_ttmcconstraint_existsexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_ExistsExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_forallexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ForallExpression)


def test_ttmcconstraint_forallexpression_constructor_exists():
    assert callable(TTMCConstraint_ForallExpression.__init__)


def test_ttmcconstraint_forallexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_ForallExpression.__init__)
    params = list(sig.parameters.keys())



def test_temporalpathexpression_is_not_abstract():
    assert not inspect.isabstract(TemporalPathExpression)


def test_temporalpathexpression_constructor_exists():
    assert callable(TemporalPathExpression.__init__)


def test_temporalpathexpression_constructor_args():
    sig = inspect.signature(TemporalPathExpression.__init__)
    params = list(sig.parameters.keys())



def test_multiaryexpression_is_not_abstract():
    assert not inspect.isabstract(MultiaryExpression)


def test_multiaryexpression_constructor_exists():
    assert callable(MultiaryExpression.__init__)


def test_multiaryexpression_constructor_args():
    sig = inspect.signature(MultiaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_equivalenceexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_EquivalenceExpression)


def test_ttmcconstraint_equivalenceexpression_constructor_exists():
    assert callable(TTMCConstraint_EquivalenceExpression.__init__)


def test_ttmcconstraint_equivalenceexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_EquivalenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_releaseexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ReleaseExpression)


def test_ttmcconstraint_releaseexpression_constructor_exists():
    assert callable(TTMCConstraint_ReleaseExpression.__init__)


def test_ttmcconstraint_releaseexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_ReleaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_untilexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_UntilExpression)


def test_ttmcconstraint_untilexpression_constructor_exists():
    assert callable(TTMCConstraint_UntilExpression.__init__)


def test_ttmcconstraint_untilexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_UntilExpression.__init__)
    params = list(sig.parameters.keys())



def test_comparisionexpression_is_not_abstract():
    assert not inspect.isabstract(ComparisionExpression)


def test_comparisionexpression_constructor_exists():
    assert callable(ComparisionExpression.__init__)


def test_comparisionexpression_constructor_args():
    sig = inspect.signature(ComparisionExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_greaterequalexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_GreaterEqualExpression)


def test_ttmcconstraint_greaterequalexpression_constructor_exists():
    assert callable(TTMCConstraint_GreaterEqualExpression.__init__)


def test_ttmcconstraint_greaterequalexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_GreaterEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_lessexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_LessExpression)


def test_ttmcconstraint_lessexpression_constructor_exists():
    assert callable(TTMCConstraint_LessExpression.__init__)


def test_ttmcconstraint_lessexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_LessExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_lessequalexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_LessEqualExpression)


def test_ttmcconstraint_lessequalexpression_constructor_exists():
    assert callable(TTMCConstraint_LessEqualExpression.__init__)


def test_ttmcconstraint_lessequalexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_LessEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_greaterexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_GreaterExpression)


def test_ttmcconstraint_greaterexpression_constructor_exists():
    assert callable(TTMCConstraint_GreaterExpression.__init__)


def test_ttmcconstraint_greaterexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_GreaterExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_comparisionexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ComparisionExpression)


def test_ttmcconstraint_comparisionexpression_constructor_exists():
    assert callable(TTMCConstraint_ComparisionExpression.__init__)


def test_ttmcconstraint_comparisionexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_ComparisionExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_fieldassignment_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_FieldAssignment)


def test_ttmcconstraint_fieldassignment_constructor_exists():
    assert callable(TTMCConstraint_FieldAssignment.__init__)


def test_ttmcconstraint_fieldassignment_constructor_args():
    sig = inspect.signature(TTMCConstraint_FieldAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"

def test_ttmcconstraint_fieldassignment_has_reference():
    assert hasattr(TTMCConstraint_FieldAssignment, "reference")
    descriptor = None
    for klass in TTMCConstraint_FieldAssignment.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_booleanliteralexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanLiteralExpression)


def test_booleanliteralexpression_constructor_exists():
    assert callable(BooleanLiteralExpression.__init__)


def test_booleanliteralexpression_constructor_args():
    sig = inspect.signature(BooleanLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_falseexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_FalseExpression)


def test_ttmcconstraint_falseexpression_constructor_exists():
    assert callable(TTMCConstraint_FalseExpression.__init__)


def test_ttmcconstraint_falseexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_FalseExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_trueexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_TrueExpression)


def test_ttmcconstraint_trueexpression_constructor_exists():
    assert callable(TTMCConstraint_TrueExpression.__init__)


def test_ttmcconstraint_trueexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_TrueExpression.__init__)
    params = list(sig.parameters.keys())



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_equalexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_EqualExpression)


def test_ttmcconstraint_equalexpression_constructor_exists():
    assert callable(TTMCConstraint_EqualExpression.__init__)


def test_ttmcconstraint_equalexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_EqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_orexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_OrExpression)


def test_ttmcconstraint_orexpression_constructor_exists():
    assert callable(TTMCConstraint_OrExpression.__init__)


def test_ttmcconstraint_orexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_andexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_AndExpression)


def test_ttmcconstraint_andexpression_constructor_exists():
    assert callable(TTMCConstraint_AndExpression.__init__)


def test_ttmcconstraint_andexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_implyexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ImplyExpression)


def test_ttmcconstraint_implyexpression_constructor_exists():
    assert callable(TTMCConstraint_ImplyExpression.__init__)


def test_ttmcconstraint_implyexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_ImplyExpression.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticliteralexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticLiteralExpression)


def test_arithmeticliteralexpression_constructor_exists():
    assert callable(ArithmeticLiteralExpression.__init__)


def test_arithmeticliteralexpression_constructor_args():
    sig = inspect.signature(ArithmeticLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_rationalliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_RationalLiteralExpression)


def test_ttmcconstraint_rationalliteralexpression_constructor_exists():
    assert callable(TTMCConstraint_RationalLiteralExpression.__init__)


def test_ttmcconstraint_rationalliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_RationalLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "numerator" in params, "Missing parameter 'numerator'"
    assert "denominator" in params, "Missing parameter 'denominator'"

def test_ttmcconstraint_rationalliteralexpression_has_numerator():
    assert hasattr(TTMCConstraint_RationalLiteralExpression, "numerator")
    descriptor = None
    for klass in TTMCConstraint_RationalLiteralExpression.__mro__:
        if "numerator" in klass.__dict__:
            descriptor = klass.__dict__["numerator"]
            break
    assert isinstance(descriptor, property)

def test_ttmcconstraint_rationalliteralexpression_has_denominator():
    assert hasattr(TTMCConstraint_RationalLiteralExpression, "denominator")
    descriptor = None
    for klass in TTMCConstraint_RationalLiteralExpression.__mro__:
        if "denominator" in klass.__dict__:
            descriptor = klass.__dict__["denominator"]
            break
    assert isinstance(descriptor, property)



def test_ttmcconstraint_decimalliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_DecimalLiteralExpression)


def test_ttmcconstraint_decimalliteralexpression_constructor_exists():
    assert callable(TTMCConstraint_DecimalLiteralExpression.__init__)


def test_ttmcconstraint_decimalliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_DecimalLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ttmcconstraint_decimalliteralexpression_has_value():
    assert hasattr(TTMCConstraint_DecimalLiteralExpression, "value")
    descriptor = None
    for klass in TTMCConstraint_DecimalLiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ttmcconstraint_integerliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_IntegerLiteralExpression)


def test_ttmcconstraint_integerliteralexpression_constructor_exists():
    assert callable(TTMCConstraint_IntegerLiteralExpression.__init__)


def test_ttmcconstraint_integerliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_IntegerLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ttmcconstraint_integerliteralexpression_has_value():
    assert hasattr(TTMCConstraint_IntegerLiteralExpression, "value")
    descriptor = None
    for klass in TTMCConstraint_IntegerLiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ArithmeticExpression)


def test_ttmcconstraint_arithmeticexpression_constructor_exists():
    assert callable(TTMCConstraint_ArithmeticExpression.__init__)


def test_ttmcconstraint_arithmeticexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_UnaryExpression)


def test_ttmcconstraint_unaryexpression_constructor_exists():
    assert callable(TTMCConstraint_UnaryExpression.__init__)


def test_ttmcconstraint_unaryexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_letexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_LetExpression)


def test_ttmcconstraint_letexpression_constructor_exists():
    assert callable(TTMCConstraint_LetExpression.__init__)


def test_ttmcconstraint_letexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_LetExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_multiaryexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_MultiaryExpression)


def test_ttmcconstraint_multiaryexpression_constructor_exists():
    assert callable(TTMCConstraint_MultiaryExpression.__init__)


def test_ttmcconstraint_multiaryexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_MultiaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_ifthenelseexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_IfThenElseExpression)


def test_ttmcconstraint_ifthenelseexpression_constructor_exists():
    assert callable(TTMCConstraint_IfThenElseExpression.__init__)


def test_ttmcconstraint_ifthenelseexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_IfThenElseExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_predicateexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_PredicateExpression)


def test_ttmcconstraint_predicateexpression_constructor_exists():
    assert callable(TTMCConstraint_PredicateExpression.__init__)


def test_ttmcconstraint_predicateexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_PredicateExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_BinaryExpression)


def test_ttmcconstraint_binaryexpression_constructor_exists():
    assert callable(TTMCConstraint_BinaryExpression.__init__)


def test_ttmcconstraint_binaryexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_accessexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_AccessExpression)


def test_ttmcconstraint_accessexpression_constructor_exists():
    assert callable(TTMCConstraint_AccessExpression.__init__)


def test_ttmcconstraint_accessexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_AccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_nullaryexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_NullaryExpression)


def test_ttmcconstraint_nullaryexpression_constructor_exists():
    assert callable(TTMCConstraint_NullaryExpression.__init__)


def test_ttmcconstraint_nullaryexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_NullaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_constraintdefinition_is_not_abstract():
    assert not inspect.isabstract(ConstraintDefinition)


def test_constraintdefinition_constructor_exists():
    assert callable(ConstraintDefinition.__init__)


def test_constraintdefinition_constructor_args():
    sig = inspect.signature(ConstraintDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_constraintdefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ConstraintDefinition)


def test_ttmcconstraint_constraintdefinition_constructor_exists():
    assert callable(TTMCConstraint_ConstraintDefinition.__init__)


def test_ttmcconstraint_constraintdefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_ConstraintDefinition.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_divexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_DivExpression)


def test_ttmcconstraint_divexpression_constructor_exists():
    assert callable(TTMCConstraint_DivExpression.__init__)


def test_ttmcconstraint_divexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_DivExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_multiplyexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_MultiplyExpression)


def test_ttmcconstraint_multiplyexpression_constructor_exists():
    assert callable(TTMCConstraint_MultiplyExpression.__init__)


def test_ttmcconstraint_multiplyexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_MultiplyExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_subtractexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_SubtractExpression)


def test_ttmcconstraint_subtractexpression_constructor_exists():
    assert callable(TTMCConstraint_SubtractExpression.__init__)


def test_ttmcconstraint_subtractexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_SubtractExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_modexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ModExpression)


def test_ttmcconstraint_modexpression_constructor_exists():
    assert callable(TTMCConstraint_ModExpression.__init__)


def test_ttmcconstraint_modexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_ModExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_divideexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_DivideExpression)


def test_ttmcconstraint_divideexpression_constructor_exists():
    assert callable(TTMCConstraint_DivideExpression.__init__)


def test_ttmcconstraint_divideexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_DivideExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_addexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_AddExpression)


def test_ttmcconstraint_addexpression_constructor_exists():
    assert callable(TTMCConstraint_AddExpression.__init__)


def test_ttmcconstraint_addexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_AddExpression.__init__)
    params = list(sig.parameters.keys())



def test_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_recordliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_RecordLiteralExpression)


def test_ttmcconstraint_recordliteralexpression_constructor_exists():
    assert callable(TTMCConstraint_RecordLiteralExpression.__init__)


def test_ttmcconstraint_recordliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_RecordLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_tupleliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_TupleLiteralExpression)


def test_ttmcconstraint_tupleliteralexpression_constructor_exists():
    assert callable(TTMCConstraint_TupleLiteralExpression.__init__)


def test_ttmcconstraint_tupleliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_TupleLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_nullaryexpression_is_not_abstract():
    assert not inspect.isabstract(NullaryExpression)


def test_nullaryexpression_constructor_exists():
    assert callable(NullaryExpression.__init__)


def test_nullaryexpression_constructor_args():
    sig = inspect.signature(NullaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_booleanliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_BooleanLiteralExpression)


def test_ttmcconstraint_booleanliteralexpression_constructor_exists():
    assert callable(TTMCConstraint_BooleanLiteralExpression.__init__)


def test_ttmcconstraint_booleanliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_BooleanLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_referenceexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ReferenceExpression)


def test_ttmcconstraint_referenceexpression_constructor_exists():
    assert callable(TTMCConstraint_ReferenceExpression.__init__)


def test_ttmcconstraint_referenceexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_ReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_enumerationliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_EnumerationLiteralExpression)


def test_ttmcconstraint_enumerationliteralexpression_constructor_exists():
    assert callable(TTMCConstraint_EnumerationLiteralExpression.__init__)


def test_ttmcconstraint_enumerationliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_EnumerationLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_arithmeticliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ArithmeticLiteralExpression)


def test_ttmcconstraint_arithmeticliteralexpression_constructor_exists():
    assert callable(TTMCConstraint_ArithmeticLiteralExpression.__init__)


def test_ttmcconstraint_arithmeticliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_ArithmeticLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_literalexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_LiteralExpression)


def test_ttmcconstraint_literalexpression_constructor_exists():
    assert callable(TTMCConstraint_LiteralExpression.__init__)


def test_ttmcconstraint_literalexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_temporalexpression_is_not_abstract():
    assert not inspect.isabstract(TemporalExpression)


def test_temporalexpression_constructor_exists():
    assert callable(TemporalExpression.__init__)


def test_temporalexpression_constructor_args():
    sig = inspect.signature(TemporalExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_temporalstateexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_TemporalStateExpression)


def test_ttmcconstraint_temporalstateexpression_constructor_exists():
    assert callable(TTMCConstraint_TemporalStateExpression.__init__)


def test_ttmcconstraint_temporalstateexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_TemporalStateExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_temporalpathexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_TemporalPathExpression)


def test_ttmcconstraint_temporalpathexpression_constructor_exists():
    assert callable(TTMCConstraint_TemporalPathExpression.__init__)


def test_ttmcconstraint_temporalpathexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_TemporalPathExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_temporalexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_TemporalExpression)


def test_ttmcconstraint_temporalexpression_constructor_exists():
    assert callable(TTMCConstraint_TemporalExpression.__init__)


def test_ttmcconstraint_temporalexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_TemporalExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_temporalexistsexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_TemporalExistsExpression)


def test_ttmcconstraint_temporalexistsexpression_constructor_exists():
    assert callable(TTMCConstraint_TemporalExistsExpression.__init__)


def test_ttmcconstraint_temporalexistsexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_TemporalExistsExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_globallyexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_GloballyExpression)


def test_ttmcconstraint_globallyexpression_constructor_exists():
    assert callable(TTMCConstraint_GloballyExpression.__init__)


def test_ttmcconstraint_globallyexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_GloballyExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_unaryminusexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_UnaryMinusExpression)


def test_ttmcconstraint_unaryminusexpression_constructor_exists():
    assert callable(TTMCConstraint_UnaryMinusExpression.__init__)


def test_ttmcconstraint_unaryminusexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_UnaryMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_temporalforallexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_TemporalForallExpression)


def test_ttmcconstraint_temporalforallexpression_constructor_exists():
    assert callable(TTMCConstraint_TemporalForallExpression.__init__)


def test_ttmcconstraint_temporalforallexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_TemporalForallExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_unaryplusexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_UnaryPlusExpression)


def test_ttmcconstraint_unaryplusexpression_constructor_exists():
    assert callable(TTMCConstraint_UnaryPlusExpression.__init__)


def test_ttmcconstraint_unaryplusexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_UnaryPlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_notexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_NotExpression)


def test_ttmcconstraint_notexpression_constructor_exists():
    assert callable(TTMCConstraint_NotExpression.__init__)


def test_ttmcconstraint_notexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_inexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_InExpression)


def test_ttmcconstraint_inexpression_constructor_exists():
    assert callable(TTMCConstraint_InExpression.__init__)


def test_ttmcconstraint_inexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_InExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_primedexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_PrimedExpression)


def test_ttmcconstraint_primedexpression_constructor_exists():
    assert callable(TTMCConstraint_PrimedExpression.__init__)


def test_ttmcconstraint_primedexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_PrimedExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_nextexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_NextExpression)


def test_ttmcconstraint_nextexpression_constructor_exists():
    assert callable(TTMCConstraint_NextExpression.__init__)


def test_ttmcconstraint_nextexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_NextExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_finallyexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_FinallyExpression)


def test_ttmcconstraint_finallyexpression_constructor_exists():
    assert callable(TTMCConstraint_FinallyExpression.__init__)


def test_ttmcconstraint_finallyexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_FinallyExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_BooleanExpression)


def test_ttmcconstraint_booleanexpression_constructor_exists():
    assert callable(TTMCConstraint_BooleanExpression.__init__)


def test_ttmcconstraint_booleanexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_basictypedefinition_is_not_abstract():
    assert not inspect.isabstract(BasicTypeDefinition)


def test_basictypedefinition_constructor_exists():
    assert callable(BasicTypeDefinition.__init__)


def test_basictypedefinition_constructor_args():
    sig = inspect.signature(BasicTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_realtypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_RealTypeDefinition)


def test_ttmcconstraint_realtypedefinition_constructor_exists():
    assert callable(TTMCConstraint_RealTypeDefinition.__init__)


def test_ttmcconstraint_realtypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_RealTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_naturaltypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_NaturalTypeDefinition)


def test_ttmcconstraint_naturaltypedefinition_constructor_exists():
    assert callable(TTMCConstraint_NaturalTypeDefinition.__init__)


def test_ttmcconstraint_naturaltypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_NaturalTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_booleantypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_BooleanTypeDefinition)


def test_ttmcconstraint_booleantypedefinition_constructor_exists():
    assert callable(TTMCConstraint_BooleanTypeDefinition.__init__)


def test_ttmcconstraint_booleantypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_BooleanTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_integertypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_IntegerTypeDefinition)


def test_ttmcconstraint_integertypedefinition_constructor_exists():
    assert callable(TTMCConstraint_IntegerTypeDefinition.__init__)


def test_ttmcconstraint_integertypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_IntegerTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_recordtypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_RecordTypeDefinition)


def test_ttmcconstraint_recordtypedefinition_constructor_exists():
    assert callable(TTMCConstraint_RecordTypeDefinition.__init__)


def test_ttmcconstraint_recordtypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_RecordTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_subrangetypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_SubrangeTypeDefinition)


def test_ttmcconstraint_subrangetypedefinition_constructor_exists():
    assert callable(TTMCConstraint_SubrangeTypeDefinition.__init__)


def test_ttmcconstraint_subrangetypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_SubrangeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_enumerationtypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_EnumerationTypeDefinition)


def test_ttmcconstraint_enumerationtypedefinition_constructor_exists():
    assert callable(TTMCConstraint_EnumerationTypeDefinition.__init__)


def test_ttmcconstraint_enumerationtypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_EnumerationTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_tupletypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_TupleTypeDefinition)


def test_ttmcconstraint_tupletypedefinition_constructor_exists():
    assert callable(TTMCConstraint_TupleTypeDefinition.__init__)


def test_ttmcconstraint_tupletypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_TupleTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_basictypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_BasicTypeDefinition)


def test_ttmcconstraint_basictypedefinition_constructor_exists():
    assert callable(TTMCConstraint_BasicTypeDefinition.__init__)


def test_ttmcconstraint_basictypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_BasicTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_TypeDefinition)


def test_ttmcconstraint_typedefinition_constructor_exists():
    assert callable(TTMCConstraint_TypeDefinition.__init__)


def test_ttmcconstraint_typedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_typereference_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_TypeReference)


def test_ttmcconstraint_typereference_constructor_exists():
    assert callable(TTMCConstraint_TypeReference.__init__)


def test_ttmcconstraint_typereference_constructor_args():
    sig = inspect.signature(TTMCConstraint_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_arraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ArrayTypeDefinition)


def test_ttmcconstraint_arraytypedefinition_constructor_exists():
    assert callable(TTMCConstraint_ArrayTypeDefinition.__init__)


def test_ttmcconstraint_arraytypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_ArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_functiontypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_FunctionTypeDefinition)


def test_ttmcconstraint_functiontypedefinition_constructor_exists():
    assert callable(TTMCConstraint_FunctionTypeDefinition.__init__)


def test_ttmcconstraint_functiontypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_FunctionTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_basicconstraintdefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_BasicConstraintDefinition)


def test_ttmcconstraint_basicconstraintdefinition_constructor_exists():
    assert callable(TTMCConstraint_BasicConstraintDefinition.__init__)


def test_ttmcconstraint_basicconstraintdefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_BasicConstraintDefinition.__init__)
    params = list(sig.parameters.keys())



def test_parametricelement_is_not_abstract():
    assert not inspect.isabstract(ParametricElement)


def test_parametricelement_constructor_exists():
    assert callable(ParametricElement.__init__)


def test_parametricelement_constructor_args():
    sig = inspect.signature(ParametricElement.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_functionliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_FunctionLiteralExpression)


def test_ttmcconstraint_functionliteralexpression_constructor_exists():
    assert callable(TTMCConstraint_FunctionLiteralExpression.__init__)


def test_ttmcconstraint_functionliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_FunctionLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_arrayliteralexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ArrayLiteralExpression)


def test_ttmcconstraint_arrayliteralexpression_constructor_exists():
    assert callable(TTMCConstraint_ArrayLiteralExpression.__init__)


def test_ttmcconstraint_arrayliteralexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_ArrayLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_subtypedefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_SubTypeDefinition)


def test_ttmcconstraint_subtypedefinition_constructor_exists():
    assert callable(TTMCConstraint_SubTypeDefinition.__init__)


def test_ttmcconstraint_subtypedefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_SubTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_quantifierexpression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_QuantifierExpression)


def test_ttmcconstraint_quantifierexpression_constructor_exists():
    assert callable(TTMCConstraint_QuantifierExpression.__init__)


def test_ttmcconstraint_quantifierexpression_constructor_args():
    sig = inspect.signature(TTMCConstraint_QuantifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_declaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_Declaration)


def test_ttmcconstraint_declaration_constructor_exists():
    assert callable(TTMCConstraint_Declaration.__init__)


def test_ttmcconstraint_declaration_constructor_args():
    sig = inspect.signature(TTMCConstraint_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_TypeDeclaration)


def test_ttmcconstraint_typedeclaration_constructor_exists():
    assert callable(TTMCConstraint_TypeDeclaration.__init__)


def test_ttmcconstraint_typedeclaration_constructor_args():
    sig = inspect.signature(TTMCConstraint_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_enumerationliteraldefinition_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_EnumerationLiteralDefinition)


def test_ttmcconstraint_enumerationliteraldefinition_constructor_exists():
    assert callable(TTMCConstraint_EnumerationLiteralDefinition.__init__)


def test_ttmcconstraint_enumerationliteraldefinition_constructor_args():
    sig = inspect.signature(TTMCConstraint_EnumerationLiteralDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_constraintspecification_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ConstraintSpecification)


def test_ttmcconstraint_constraintspecification_constructor_exists():
    assert callable(TTMCConstraint_ConstraintSpecification.__init__)


def test_ttmcconstraint_constraintspecification_constructor_args():
    sig = inspect.signature(TTMCConstraint_ConstraintSpecification.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_expression_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_Expression)


def test_ttmcconstraint_expression_constructor_exists():
    assert callable(TTMCConstraint_Expression.__init__)


def test_ttmcconstraint_expression_constructor_args():
    sig = inspect.signature(TTMCConstraint_Expression.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_parametrizedelement_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ParametrizedElement)


def test_ttmcconstraint_parametrizedelement_constructor_exists():
    assert callable(TTMCConstraint_ParametrizedElement.__init__)


def test_ttmcconstraint_parametrizedelement_constructor_args():
    sig = inspect.signature(TTMCConstraint_ParametrizedElement.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_parametricelement_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ParametricElement)


def test_ttmcconstraint_parametricelement_constructor_exists():
    assert callable(TTMCConstraint_ParametricElement.__init__)


def test_ttmcconstraint_parametricelement_constructor_args():
    sig = inspect.signature(TTMCConstraint_ParametricElement.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_namedelement_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_NamedElement)


def test_ttmcconstraint_namedelement_constructor_exists():
    assert callable(TTMCConstraint_NamedElement.__init__)


def test_ttmcconstraint_namedelement_constructor_args():
    sig = inspect.signature(TTMCConstraint_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ttmcconstraint_namedelement_has_name():
    assert hasattr(TTMCConstraint_NamedElement, "name")
    descriptor = None
    for klass in TTMCConstraint_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_definabledeclaration_is_not_abstract():
    assert not inspect.isabstract(DefinableDeclaration)


def test_definabledeclaration_constructor_exists():
    assert callable(DefinableDeclaration.__init__)


def test_definabledeclaration_constructor_args():
    sig = inspect.signature(DefinableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ConstantDeclaration)


def test_ttmcconstraint_constantdeclaration_constructor_exists():
    assert callable(TTMCConstraint_ConstantDeclaration.__init__)


def test_ttmcconstraint_constantdeclaration_constructor_args():
    sig = inspect.signature(TTMCConstraint_ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_FunctionDeclaration)


def test_ttmcconstraint_functiondeclaration_constructor_exists():
    assert callable(TTMCConstraint_FunctionDeclaration.__init__)


def test_ttmcconstraint_functiondeclaration_constructor_args():
    sig = inspect.signature(TTMCConstraint_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_letdeclaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_LetDeclaration)


def test_ttmcconstraint_letdeclaration_constructor_exists():
    assert callable(TTMCConstraint_LetDeclaration.__init__)


def test_ttmcconstraint_letdeclaration_constructor_args():
    sig = inspect.signature(TTMCConstraint_LetDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_ParameterDeclaration)


def test_ttmcconstraint_parameterdeclaration_constructor_exists():
    assert callable(TTMCConstraint_ParameterDeclaration.__init__)


def test_ttmcconstraint_parameterdeclaration_constructor_args():
    sig = inspect.signature(TTMCConstraint_ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_FieldDeclaration)


def test_ttmcconstraint_fielddeclaration_constructor_exists():
    assert callable(TTMCConstraint_FieldDeclaration.__init__)


def test_ttmcconstraint_fielddeclaration_constructor_args():
    sig = inspect.signature(TTMCConstraint_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_definabledeclaration_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_DefinableDeclaration)


def test_ttmcconstraint_definabledeclaration_constructor_exists():
    assert callable(TTMCConstraint_DefinableDeclaration.__init__)


def test_ttmcconstraint_definabledeclaration_constructor_args():
    sig = inspect.signature(TTMCConstraint_DefinableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ttmcconstraint_type_is_not_abstract():
    assert not inspect.isabstract(TTMCConstraint_Type)


def test_ttmcconstraint_type_constructor_exists():
    assert callable(TTMCConstraint_Type.__init__)


def test_ttmcconstraint_type_constructor_args():
    sig = inspect.signature(TTMCConstraint_Type.__init__)
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
ParametrizedElement_strategy = st.builds(
    ParametrizedElement,
)
AccessExpression_strategy = st.builds(
    AccessExpression,
)
TTMCConstraint_TupleAccessExpression_strategy = st.builds(
    TTMCConstraint_TupleAccessExpression,
    index=
        safe_text
)
TTMCConstraint_RecordAccessExpression_strategy = st.builds(
    TTMCConstraint_RecordAccessExpression,
    field=
        safe_text
)
TTMCConstraint_ArrayAccessExpression_strategy = st.builds(
    TTMCConstraint_ArrayAccessExpression,
)
TTMCConstraint_FunctionAccessExpression_strategy = st.builds(
    TTMCConstraint_FunctionAccessExpression,
)
EquivalenceExpression_strategy = st.builds(
    EquivalenceExpression,
)
TTMCConstraint_InequalityExpression_strategy = st.builds(
    TTMCConstraint_InequalityExpression,
)
TTMCConstraint_EqualityExpression_strategy = st.builds(
    TTMCConstraint_EqualityExpression,
)
PredicateExpression_strategy = st.builds(
    PredicateExpression,
)
TemporalStateExpression_strategy = st.builds(
    TemporalStateExpression,
)
QuantifierExpression_strategy = st.builds(
    QuantifierExpression,
)
TTMCConstraint_ExistsExpression_strategy = st.builds(
    TTMCConstraint_ExistsExpression,
)
TTMCConstraint_ForallExpression_strategy = st.builds(
    TTMCConstraint_ForallExpression,
)
TemporalPathExpression_strategy = st.builds(
    TemporalPathExpression,
)
MultiaryExpression_strategy = st.builds(
    MultiaryExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
TTMCConstraint_EquivalenceExpression_strategy = st.builds(
    TTMCConstraint_EquivalenceExpression,
)
TTMCConstraint_ReleaseExpression_strategy = st.builds(
    TTMCConstraint_ReleaseExpression,
)
TTMCConstraint_UntilExpression_strategy = st.builds(
    TTMCConstraint_UntilExpression,
)
ComparisionExpression_strategy = st.builds(
    ComparisionExpression,
)
TTMCConstraint_GreaterEqualExpression_strategy = st.builds(
    TTMCConstraint_GreaterEqualExpression,
)
TTMCConstraint_LessExpression_strategy = st.builds(
    TTMCConstraint_LessExpression,
)
TTMCConstraint_LessEqualExpression_strategy = st.builds(
    TTMCConstraint_LessEqualExpression,
)
TTMCConstraint_GreaterExpression_strategy = st.builds(
    TTMCConstraint_GreaterExpression,
)
TTMCConstraint_ComparisionExpression_strategy = st.builds(
    TTMCConstraint_ComparisionExpression,
)
TTMCConstraint_FieldAssignment_strategy = st.builds(
    TTMCConstraint_FieldAssignment,
    reference=
        safe_text
)
BooleanLiteralExpression_strategy = st.builds(
    BooleanLiteralExpression,
)
TTMCConstraint_FalseExpression_strategy = st.builds(
    TTMCConstraint_FalseExpression,
)
TTMCConstraint_TrueExpression_strategy = st.builds(
    TTMCConstraint_TrueExpression,
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
TTMCConstraint_EqualExpression_strategy = st.builds(
    TTMCConstraint_EqualExpression,
)
TTMCConstraint_OrExpression_strategy = st.builds(
    TTMCConstraint_OrExpression,
)
TTMCConstraint_AndExpression_strategy = st.builds(
    TTMCConstraint_AndExpression,
)
TTMCConstraint_ImplyExpression_strategy = st.builds(
    TTMCConstraint_ImplyExpression,
)
ArithmeticLiteralExpression_strategy = st.builds(
    ArithmeticLiteralExpression,
)
TTMCConstraint_RationalLiteralExpression_strategy = st.builds(
    TTMCConstraint_RationalLiteralExpression,
    numerator=
        safe_text,
    denominator=
        safe_text
)
TTMCConstraint_DecimalLiteralExpression_strategy = st.builds(
    TTMCConstraint_DecimalLiteralExpression,
    value=
        safe_text
)
TTMCConstraint_IntegerLiteralExpression_strategy = st.builds(
    TTMCConstraint_IntegerLiteralExpression,
    value=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
TTMCConstraint_ArithmeticExpression_strategy = st.builds(
    TTMCConstraint_ArithmeticExpression,
)
TTMCConstraint_UnaryExpression_strategy = st.builds(
    TTMCConstraint_UnaryExpression,
)
TTMCConstraint_LetExpression_strategy = st.builds(
    TTMCConstraint_LetExpression,
)
TTMCConstraint_MultiaryExpression_strategy = st.builds(
    TTMCConstraint_MultiaryExpression,
)
TTMCConstraint_IfThenElseExpression_strategy = st.builds(
    TTMCConstraint_IfThenElseExpression,
)
TTMCConstraint_PredicateExpression_strategy = st.builds(
    TTMCConstraint_PredicateExpression,
)
TTMCConstraint_BinaryExpression_strategy = st.builds(
    TTMCConstraint_BinaryExpression,
)
TTMCConstraint_AccessExpression_strategy = st.builds(
    TTMCConstraint_AccessExpression,
)
TTMCConstraint_NullaryExpression_strategy = st.builds(
    TTMCConstraint_NullaryExpression,
)
ConstraintDefinition_strategy = st.builds(
    ConstraintDefinition,
)
TTMCConstraint_ConstraintDefinition_strategy = st.builds(
    TTMCConstraint_ConstraintDefinition,
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
TTMCConstraint_DivExpression_strategy = st.builds(
    TTMCConstraint_DivExpression,
)
TTMCConstraint_MultiplyExpression_strategy = st.builds(
    TTMCConstraint_MultiplyExpression,
)
TTMCConstraint_SubtractExpression_strategy = st.builds(
    TTMCConstraint_SubtractExpression,
)
TTMCConstraint_ModExpression_strategy = st.builds(
    TTMCConstraint_ModExpression,
)
TTMCConstraint_DivideExpression_strategy = st.builds(
    TTMCConstraint_DivideExpression,
)
TTMCConstraint_AddExpression_strategy = st.builds(
    TTMCConstraint_AddExpression,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
TTMCConstraint_RecordLiteralExpression_strategy = st.builds(
    TTMCConstraint_RecordLiteralExpression,
)
TTMCConstraint_TupleLiteralExpression_strategy = st.builds(
    TTMCConstraint_TupleLiteralExpression,
)
NullaryExpression_strategy = st.builds(
    NullaryExpression,
)
TTMCConstraint_BooleanLiteralExpression_strategy = st.builds(
    TTMCConstraint_BooleanLiteralExpression,
)
TTMCConstraint_ReferenceExpression_strategy = st.builds(
    TTMCConstraint_ReferenceExpression,
)
TTMCConstraint_EnumerationLiteralExpression_strategy = st.builds(
    TTMCConstraint_EnumerationLiteralExpression,
)
TTMCConstraint_ArithmeticLiteralExpression_strategy = st.builds(
    TTMCConstraint_ArithmeticLiteralExpression,
)
TTMCConstraint_LiteralExpression_strategy = st.builds(
    TTMCConstraint_LiteralExpression,
)
TemporalExpression_strategy = st.builds(
    TemporalExpression,
)
TTMCConstraint_TemporalStateExpression_strategy = st.builds(
    TTMCConstraint_TemporalStateExpression,
)
TTMCConstraint_TemporalPathExpression_strategy = st.builds(
    TTMCConstraint_TemporalPathExpression,
)
TTMCConstraint_TemporalExpression_strategy = st.builds(
    TTMCConstraint_TemporalExpression,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
TTMCConstraint_TemporalExistsExpression_strategy = st.builds(
    TTMCConstraint_TemporalExistsExpression,
)
TTMCConstraint_GloballyExpression_strategy = st.builds(
    TTMCConstraint_GloballyExpression,
)
TTMCConstraint_UnaryMinusExpression_strategy = st.builds(
    TTMCConstraint_UnaryMinusExpression,
)
TTMCConstraint_TemporalForallExpression_strategy = st.builds(
    TTMCConstraint_TemporalForallExpression,
)
TTMCConstraint_UnaryPlusExpression_strategy = st.builds(
    TTMCConstraint_UnaryPlusExpression,
)
TTMCConstraint_NotExpression_strategy = st.builds(
    TTMCConstraint_NotExpression,
)
TTMCConstraint_InExpression_strategy = st.builds(
    TTMCConstraint_InExpression,
)
TTMCConstraint_PrimedExpression_strategy = st.builds(
    TTMCConstraint_PrimedExpression,
)
TTMCConstraint_NextExpression_strategy = st.builds(
    TTMCConstraint_NextExpression,
)
TTMCConstraint_FinallyExpression_strategy = st.builds(
    TTMCConstraint_FinallyExpression,
)
TTMCConstraint_BooleanExpression_strategy = st.builds(
    TTMCConstraint_BooleanExpression,
)
BasicTypeDefinition_strategy = st.builds(
    BasicTypeDefinition,
)
TTMCConstraint_RealTypeDefinition_strategy = st.builds(
    TTMCConstraint_RealTypeDefinition,
)
TTMCConstraint_NaturalTypeDefinition_strategy = st.builds(
    TTMCConstraint_NaturalTypeDefinition,
)
TTMCConstraint_BooleanTypeDefinition_strategy = st.builds(
    TTMCConstraint_BooleanTypeDefinition,
)
TTMCConstraint_IntegerTypeDefinition_strategy = st.builds(
    TTMCConstraint_IntegerTypeDefinition,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
TTMCConstraint_RecordTypeDefinition_strategy = st.builds(
    TTMCConstraint_RecordTypeDefinition,
)
TTMCConstraint_SubrangeTypeDefinition_strategy = st.builds(
    TTMCConstraint_SubrangeTypeDefinition,
)
TTMCConstraint_EnumerationTypeDefinition_strategy = st.builds(
    TTMCConstraint_EnumerationTypeDefinition,
)
TTMCConstraint_TupleTypeDefinition_strategy = st.builds(
    TTMCConstraint_TupleTypeDefinition,
)
TTMCConstraint_BasicTypeDefinition_strategy = st.builds(
    TTMCConstraint_BasicTypeDefinition,
)
Type_strategy = st.builds(
    Type,
)
TTMCConstraint_TypeDefinition_strategy = st.builds(
    TTMCConstraint_TypeDefinition,
)
TTMCConstraint_TypeReference_strategy = st.builds(
    TTMCConstraint_TypeReference,
)
TTMCConstraint_ArrayTypeDefinition_strategy = st.builds(
    TTMCConstraint_ArrayTypeDefinition,
)
TTMCConstraint_FunctionTypeDefinition_strategy = st.builds(
    TTMCConstraint_FunctionTypeDefinition,
)
TTMCConstraint_BasicConstraintDefinition_strategy = st.builds(
    TTMCConstraint_BasicConstraintDefinition,
)
ParametricElement_strategy = st.builds(
    ParametricElement,
)
TTMCConstraint_FunctionLiteralExpression_strategy = st.builds(
    TTMCConstraint_FunctionLiteralExpression,
)
TTMCConstraint_ArrayLiteralExpression_strategy = st.builds(
    TTMCConstraint_ArrayLiteralExpression,
)
TTMCConstraint_SubTypeDefinition_strategy = st.builds(
    TTMCConstraint_SubTypeDefinition,
)
TTMCConstraint_QuantifierExpression_strategy = st.builds(
    TTMCConstraint_QuantifierExpression,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
TTMCConstraint_Declaration_strategy = st.builds(
    TTMCConstraint_Declaration,
)
TTMCConstraint_TypeDeclaration_strategy = st.builds(
    TTMCConstraint_TypeDeclaration,
)
TTMCConstraint_EnumerationLiteralDefinition_strategy = st.builds(
    TTMCConstraint_EnumerationLiteralDefinition,
)
TTMCConstraint_ConstraintSpecification_strategy = st.builds(
    TTMCConstraint_ConstraintSpecification,
)
TTMCConstraint_Expression_strategy = st.builds(
    TTMCConstraint_Expression,
)
TTMCConstraint_ParametrizedElement_strategy = st.builds(
    TTMCConstraint_ParametrizedElement,
)
TTMCConstraint_ParametricElement_strategy = st.builds(
    TTMCConstraint_ParametricElement,
)
TTMCConstraint_NamedElement_strategy = st.builds(
    TTMCConstraint_NamedElement,
    name=
        safe_text
)
DefinableDeclaration_strategy = st.builds(
    DefinableDeclaration,
)
TTMCConstraint_ConstantDeclaration_strategy = st.builds(
    TTMCConstraint_ConstantDeclaration,
)
TTMCConstraint_FunctionDeclaration_strategy = st.builds(
    TTMCConstraint_FunctionDeclaration,
)
TTMCConstraint_LetDeclaration_strategy = st.builds(
    TTMCConstraint_LetDeclaration,
)
Declaration_strategy = st.builds(
    Declaration,
)
TTMCConstraint_ParameterDeclaration_strategy = st.builds(
    TTMCConstraint_ParameterDeclaration,
)
TTMCConstraint_FieldDeclaration_strategy = st.builds(
    TTMCConstraint_FieldDeclaration,
)
TTMCConstraint_DefinableDeclaration_strategy = st.builds(
    TTMCConstraint_DefinableDeclaration,
)
TTMCConstraint_Type_strategy = st.builds(
    TTMCConstraint_Type,
)

@given(instance=ParametrizedElement_strategy)
@settings(max_examples=50)
def test_parametrizedelement_instantiation(instance):
    assert isinstance(instance, ParametrizedElement)

@given(instance=AccessExpression_strategy)
@settings(max_examples=50)
def test_accessexpression_instantiation(instance):
    assert isinstance(instance, AccessExpression)

@given(instance=TTMCConstraint_TupleAccessExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_tupleaccessexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_TupleAccessExpression)



@given(instance=TTMCConstraint_TupleAccessExpression_strategy)
def test_ttmcconstraint_tupleaccessexpression_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=TTMCConstraint_RecordAccessExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_recordaccessexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_RecordAccessExpression)



@given(instance=TTMCConstraint_RecordAccessExpression_strategy)
def test_ttmcconstraint_recordaccessexpression_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=TTMCConstraint_ArrayAccessExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_arrayaccessexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ArrayAccessExpression)

@given(instance=TTMCConstraint_FunctionAccessExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_functionaccessexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_FunctionAccessExpression)

@given(instance=EquivalenceExpression_strategy)
@settings(max_examples=50)
def test_equivalenceexpression_instantiation(instance):
    assert isinstance(instance, EquivalenceExpression)

@given(instance=TTMCConstraint_InequalityExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_inequalityexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_InequalityExpression)

@given(instance=TTMCConstraint_EqualityExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_equalityexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_EqualityExpression)

@given(instance=PredicateExpression_strategy)
@settings(max_examples=50)
def test_predicateexpression_instantiation(instance):
    assert isinstance(instance, PredicateExpression)

@given(instance=TemporalStateExpression_strategy)
@settings(max_examples=50)
def test_temporalstateexpression_instantiation(instance):
    assert isinstance(instance, TemporalStateExpression)

@given(instance=QuantifierExpression_strategy)
@settings(max_examples=50)
def test_quantifierexpression_instantiation(instance):
    assert isinstance(instance, QuantifierExpression)

@given(instance=TTMCConstraint_ExistsExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_existsexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ExistsExpression)

@given(instance=TTMCConstraint_ForallExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_forallexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ForallExpression)

@given(instance=TemporalPathExpression_strategy)
@settings(max_examples=50)
def test_temporalpathexpression_instantiation(instance):
    assert isinstance(instance, TemporalPathExpression)

@given(instance=MultiaryExpression_strategy)
@settings(max_examples=50)
def test_multiaryexpression_instantiation(instance):
    assert isinstance(instance, MultiaryExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=TTMCConstraint_EquivalenceExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_equivalenceexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_EquivalenceExpression)

@given(instance=TTMCConstraint_ReleaseExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_releaseexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ReleaseExpression)

@given(instance=TTMCConstraint_UntilExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_untilexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_UntilExpression)

@given(instance=ComparisionExpression_strategy)
@settings(max_examples=50)
def test_comparisionexpression_instantiation(instance):
    assert isinstance(instance, ComparisionExpression)

@given(instance=TTMCConstraint_GreaterEqualExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_greaterequalexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_GreaterEqualExpression)

@given(instance=TTMCConstraint_LessExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_lessexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_LessExpression)

@given(instance=TTMCConstraint_LessEqualExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_lessequalexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_LessEqualExpression)

@given(instance=TTMCConstraint_GreaterExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_greaterexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_GreaterExpression)

@given(instance=TTMCConstraint_ComparisionExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_comparisionexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ComparisionExpression)

@given(instance=TTMCConstraint_FieldAssignment_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_fieldassignment_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_FieldAssignment)



@given(instance=TTMCConstraint_FieldAssignment_strategy)
def test_ttmcconstraint_fieldassignment_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=BooleanLiteralExpression_strategy)
@settings(max_examples=50)
def test_booleanliteralexpression_instantiation(instance):
    assert isinstance(instance, BooleanLiteralExpression)

@given(instance=TTMCConstraint_FalseExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_falseexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_FalseExpression)

@given(instance=TTMCConstraint_TrueExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_trueexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_TrueExpression)

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=TTMCConstraint_EqualExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_equalexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_EqualExpression)

@given(instance=TTMCConstraint_OrExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_orexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_OrExpression)

@given(instance=TTMCConstraint_AndExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_andexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_AndExpression)

@given(instance=TTMCConstraint_ImplyExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_implyexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ImplyExpression)

@given(instance=ArithmeticLiteralExpression_strategy)
@settings(max_examples=50)
def test_arithmeticliteralexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticLiteralExpression)

@given(instance=TTMCConstraint_RationalLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_rationalliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_RationalLiteralExpression)



@given(instance=TTMCConstraint_RationalLiteralExpression_strategy)
def test_ttmcconstraint_rationalliteralexpression_numerator_setter(instance):
    original = instance.numerator
    instance.numerator = original
    assert instance.numerator == original



@given(instance=TTMCConstraint_RationalLiteralExpression_strategy)
def test_ttmcconstraint_rationalliteralexpression_denominator_setter(instance):
    original = instance.denominator
    instance.denominator = original
    assert instance.denominator == original

@given(instance=TTMCConstraint_DecimalLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_decimalliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_DecimalLiteralExpression)



@given(instance=TTMCConstraint_DecimalLiteralExpression_strategy)
def test_ttmcconstraint_decimalliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=TTMCConstraint_IntegerLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_integerliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_IntegerLiteralExpression)



@given(instance=TTMCConstraint_IntegerLiteralExpression_strategy)
def test_ttmcconstraint_integerliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=TTMCConstraint_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ArithmeticExpression)

@given(instance=TTMCConstraint_UnaryExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_unaryexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_UnaryExpression)

@given(instance=TTMCConstraint_LetExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_letexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_LetExpression)

@given(instance=TTMCConstraint_MultiaryExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_multiaryexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_MultiaryExpression)

@given(instance=TTMCConstraint_IfThenElseExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_ifthenelseexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_IfThenElseExpression)

@given(instance=TTMCConstraint_PredicateExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_predicateexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_PredicateExpression)

@given(instance=TTMCConstraint_BinaryExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_binaryexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_BinaryExpression)

@given(instance=TTMCConstraint_AccessExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_accessexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_AccessExpression)

@given(instance=TTMCConstraint_NullaryExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_nullaryexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_NullaryExpression)

@given(instance=ConstraintDefinition_strategy)
@settings(max_examples=50)
def test_constraintdefinition_instantiation(instance):
    assert isinstance(instance, ConstraintDefinition)

@given(instance=TTMCConstraint_ConstraintDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_constraintdefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ConstraintDefinition)

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=TTMCConstraint_DivExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_divexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_DivExpression)

@given(instance=TTMCConstraint_MultiplyExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_multiplyexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_MultiplyExpression)

@given(instance=TTMCConstraint_SubtractExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_subtractexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_SubtractExpression)

@given(instance=TTMCConstraint_ModExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_modexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ModExpression)

@given(instance=TTMCConstraint_DivideExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_divideexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_DivideExpression)

@given(instance=TTMCConstraint_AddExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_addexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_AddExpression)

@given(instance=LiteralExpression_strategy)
@settings(max_examples=50)
def test_literalexpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)

@given(instance=TTMCConstraint_RecordLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_recordliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_RecordLiteralExpression)

@given(instance=TTMCConstraint_TupleLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_tupleliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_TupleLiteralExpression)

@given(instance=NullaryExpression_strategy)
@settings(max_examples=50)
def test_nullaryexpression_instantiation(instance):
    assert isinstance(instance, NullaryExpression)

@given(instance=TTMCConstraint_BooleanLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_booleanliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_BooleanLiteralExpression)

@given(instance=TTMCConstraint_ReferenceExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_referenceexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ReferenceExpression)

@given(instance=TTMCConstraint_EnumerationLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_enumerationliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_EnumerationLiteralExpression)

@given(instance=TTMCConstraint_ArithmeticLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_arithmeticliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ArithmeticLiteralExpression)

@given(instance=TTMCConstraint_LiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_literalexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_LiteralExpression)

@given(instance=TemporalExpression_strategy)
@settings(max_examples=50)
def test_temporalexpression_instantiation(instance):
    assert isinstance(instance, TemporalExpression)

@given(instance=TTMCConstraint_TemporalStateExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_temporalstateexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_TemporalStateExpression)

@given(instance=TTMCConstraint_TemporalPathExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_temporalpathexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_TemporalPathExpression)

@given(instance=TTMCConstraint_TemporalExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_temporalexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_TemporalExpression)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=TTMCConstraint_TemporalExistsExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_temporalexistsexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_TemporalExistsExpression)

@given(instance=TTMCConstraint_GloballyExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_globallyexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_GloballyExpression)

@given(instance=TTMCConstraint_UnaryMinusExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_unaryminusexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_UnaryMinusExpression)

@given(instance=TTMCConstraint_TemporalForallExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_temporalforallexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_TemporalForallExpression)

@given(instance=TTMCConstraint_UnaryPlusExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_unaryplusexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_UnaryPlusExpression)

@given(instance=TTMCConstraint_NotExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_notexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_NotExpression)

@given(instance=TTMCConstraint_InExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_inexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_InExpression)

@given(instance=TTMCConstraint_PrimedExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_primedexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_PrimedExpression)

@given(instance=TTMCConstraint_NextExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_nextexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_NextExpression)

@given(instance=TTMCConstraint_FinallyExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_finallyexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_FinallyExpression)

@given(instance=TTMCConstraint_BooleanExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_booleanexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_BooleanExpression)

@given(instance=BasicTypeDefinition_strategy)
@settings(max_examples=50)
def test_basictypedefinition_instantiation(instance):
    assert isinstance(instance, BasicTypeDefinition)

@given(instance=TTMCConstraint_RealTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_realtypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_RealTypeDefinition)

@given(instance=TTMCConstraint_NaturalTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_naturaltypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_NaturalTypeDefinition)

@given(instance=TTMCConstraint_BooleanTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_booleantypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_BooleanTypeDefinition)

@given(instance=TTMCConstraint_IntegerTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_integertypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_IntegerTypeDefinition)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=TTMCConstraint_RecordTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_recordtypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_RecordTypeDefinition)

@given(instance=TTMCConstraint_SubrangeTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_subrangetypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_SubrangeTypeDefinition)

@given(instance=TTMCConstraint_EnumerationTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_enumerationtypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_EnumerationTypeDefinition)

@given(instance=TTMCConstraint_TupleTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_tupletypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_TupleTypeDefinition)

@given(instance=TTMCConstraint_BasicTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_basictypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_BasicTypeDefinition)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=TTMCConstraint_TypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_typedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_TypeDefinition)

@given(instance=TTMCConstraint_TypeReference_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_typereference_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_TypeReference)

@given(instance=TTMCConstraint_ArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_arraytypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ArrayTypeDefinition)

@given(instance=TTMCConstraint_FunctionTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_functiontypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_FunctionTypeDefinition)

@given(instance=TTMCConstraint_BasicConstraintDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_basicconstraintdefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_BasicConstraintDefinition)

@given(instance=ParametricElement_strategy)
@settings(max_examples=50)
def test_parametricelement_instantiation(instance):
    assert isinstance(instance, ParametricElement)

@given(instance=TTMCConstraint_FunctionLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_functionliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_FunctionLiteralExpression)

@given(instance=TTMCConstraint_ArrayLiteralExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_arrayliteralexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ArrayLiteralExpression)

@given(instance=TTMCConstraint_SubTypeDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_subtypedefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_SubTypeDefinition)

@given(instance=TTMCConstraint_QuantifierExpression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_quantifierexpression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_QuantifierExpression)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=TTMCConstraint_Declaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_declaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_Declaration)

@given(instance=TTMCConstraint_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_typedeclaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_TypeDeclaration)

@given(instance=TTMCConstraint_EnumerationLiteralDefinition_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_enumerationliteraldefinition_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_EnumerationLiteralDefinition)

@given(instance=TTMCConstraint_ConstraintSpecification_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_constraintspecification_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ConstraintSpecification)

@given(instance=TTMCConstraint_Expression_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_expression_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_Expression)

@given(instance=TTMCConstraint_ParametrizedElement_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_parametrizedelement_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ParametrizedElement)

@given(instance=TTMCConstraint_ParametricElement_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_parametricelement_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ParametricElement)

@given(instance=TTMCConstraint_NamedElement_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_namedelement_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_NamedElement)



@given(instance=TTMCConstraint_NamedElement_strategy)
def test_ttmcconstraint_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DefinableDeclaration_strategy)
@settings(max_examples=50)
def test_definabledeclaration_instantiation(instance):
    assert isinstance(instance, DefinableDeclaration)

@given(instance=TTMCConstraint_ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_constantdeclaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ConstantDeclaration)

@given(instance=TTMCConstraint_FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_functiondeclaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_FunctionDeclaration)

@given(instance=TTMCConstraint_LetDeclaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_letdeclaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_LetDeclaration)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=TTMCConstraint_ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_parameterdeclaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_ParameterDeclaration)

@given(instance=TTMCConstraint_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_fielddeclaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_FieldDeclaration)

@given(instance=TTMCConstraint_DefinableDeclaration_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_definabledeclaration_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_DefinableDeclaration)

@given(instance=TTMCConstraint_Type_strategy)
@settings(max_examples=50)
def test_ttmcconstraint_type_instantiation(instance):
    assert isinstance(instance, TTMCConstraint_Type)
