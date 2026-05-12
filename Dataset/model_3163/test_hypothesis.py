import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    transformation_EEnumLiteral,
    transformation_EClassifier,
    UnaryExpression,
    transformation_Minus,
    transformation_Negation,
    ArithmeticExpression,
    transformation_Subtraction,
    transformation_Multiplication,
    transformation_Division,
    transformation_Addition,
    RelationalExpression,
    transformation_Greater,
    transformation_GreaterOrEqual,
    transformation_LessOrEqual,
    transformation_Less,
    EqualityExpression,
    transformation_Different,
    transformation_Equal,
    LogicalExpression,
    transformation_And,
    transformation_Or,
    transformation_ETypedElement,
    Expression,
    transformation_FeatureAccess,
    transformation_RealLiteral,
    transformation_StringLiteral,
    transformation_ExtentExpression,
    transformation_UnaryExpression,
    transformation_IntegerLiteral,
    transformation_Map,
    transformation_BooleanLiteral,
    transformation_Invocation,
    transformation_Source,
    transformation_Lambda,
    transformation_Let,
    transformation_ClassLiteral,
    transformation_EnumLiteral,
    transformation_VariableUse,
    transformation_TypeOfExpression,
    transformation_If,
    transformation_VariableInitialization,
    transformation_VariableDefinition,
    BinaryExpression,
    transformation_LogicalExpression,
    transformation_ArithmeticExpression,
    transformation_RelationalExpression,
    transformation_EqualityExpression,
    transformation_CoalescingExpression,
    transformation_BinaryExpression,
    transformation_ConditionalExpression,
    ContentMapping,
    transformation_ConditionalMapping,
    transformation_CompositeMapping,
    transformation_EClass,
    transformation_ContentMapping,
    transformation_EStructuralFeature,
    transformation_FeatureMapping,
    transformation_ResultMapping,
    transformation_Expression,
    CompositeMapping,
    transformation_WhenClause,
    transformation_OtherwiseClause,
    transformation_EPackage,
    transformation_AbstractMapping,
    transformation_MetamodelDeclaration,
    transformation_Transformation,
    transformation_EDataType,
    AbstractMapping,
    transformation_ClassMapping,
    transformation_DataTypeMapping,
    ExplicitMetamodel,
    transformation_TargetMetamodel,
    transformation_SourceMetamodel,
    MetamodelDeclaration,
    transformation_ExtentMetamodel,
    transformation_ExplicitMetamodel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transformation_eenumliteral_is_not_abstract():
    assert not inspect.isabstract(transformation_EEnumLiteral)


def test_transformation_eenumliteral_constructor_exists():
    assert callable(transformation_EEnumLiteral.__init__)


def test_transformation_eenumliteral_constructor_args():
    sig = inspect.signature(transformation_EEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_transformation_eclassifier_is_not_abstract():
    assert not inspect.isabstract(transformation_EClassifier)


def test_transformation_eclassifier_constructor_exists():
    assert callable(transformation_EClassifier.__init__)


def test_transformation_eclassifier_constructor_args():
    sig = inspect.signature(transformation_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_minus_is_not_abstract():
    assert not inspect.isabstract(transformation_Minus)


def test_transformation_minus_constructor_exists():
    assert callable(transformation_Minus.__init__)


def test_transformation_minus_constructor_args():
    sig = inspect.signature(transformation_Minus.__init__)
    params = list(sig.parameters.keys())



def test_transformation_negation_is_not_abstract():
    assert not inspect.isabstract(transformation_Negation)


def test_transformation_negation_constructor_exists():
    assert callable(transformation_Negation.__init__)


def test_transformation_negation_constructor_args():
    sig = inspect.signature(transformation_Negation.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_subtraction_is_not_abstract():
    assert not inspect.isabstract(transformation_Subtraction)


def test_transformation_subtraction_constructor_exists():
    assert callable(transformation_Subtraction.__init__)


def test_transformation_subtraction_constructor_args():
    sig = inspect.signature(transformation_Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_transformation_multiplication_is_not_abstract():
    assert not inspect.isabstract(transformation_Multiplication)


def test_transformation_multiplication_constructor_exists():
    assert callable(transformation_Multiplication.__init__)


def test_transformation_multiplication_constructor_args():
    sig = inspect.signature(transformation_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_transformation_division_is_not_abstract():
    assert not inspect.isabstract(transformation_Division)


def test_transformation_division_constructor_exists():
    assert callable(transformation_Division.__init__)


def test_transformation_division_constructor_args():
    sig = inspect.signature(transformation_Division.__init__)
    params = list(sig.parameters.keys())



def test_transformation_addition_is_not_abstract():
    assert not inspect.isabstract(transformation_Addition)


def test_transformation_addition_constructor_exists():
    assert callable(transformation_Addition.__init__)


def test_transformation_addition_constructor_args():
    sig = inspect.signature(transformation_Addition.__init__)
    params = list(sig.parameters.keys())



def test_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(RelationalExpression)


def test_relationalexpression_constructor_exists():
    assert callable(RelationalExpression.__init__)


def test_relationalexpression_constructor_args():
    sig = inspect.signature(RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_greater_is_not_abstract():
    assert not inspect.isabstract(transformation_Greater)


def test_transformation_greater_constructor_exists():
    assert callable(transformation_Greater.__init__)


def test_transformation_greater_constructor_args():
    sig = inspect.signature(transformation_Greater.__init__)
    params = list(sig.parameters.keys())



def test_transformation_greaterorequal_is_not_abstract():
    assert not inspect.isabstract(transformation_GreaterOrEqual)


def test_transformation_greaterorequal_constructor_exists():
    assert callable(transformation_GreaterOrEqual.__init__)


def test_transformation_greaterorequal_constructor_args():
    sig = inspect.signature(transformation_GreaterOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_transformation_lessorequal_is_not_abstract():
    assert not inspect.isabstract(transformation_LessOrEqual)


def test_transformation_lessorequal_constructor_exists():
    assert callable(transformation_LessOrEqual.__init__)


def test_transformation_lessorequal_constructor_args():
    sig = inspect.signature(transformation_LessOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_transformation_less_is_not_abstract():
    assert not inspect.isabstract(transformation_Less)


def test_transformation_less_constructor_exists():
    assert callable(transformation_Less.__init__)


def test_transformation_less_constructor_args():
    sig = inspect.signature(transformation_Less.__init__)
    params = list(sig.parameters.keys())



def test_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(EqualityExpression)


def test_equalityexpression_constructor_exists():
    assert callable(EqualityExpression.__init__)


def test_equalityexpression_constructor_args():
    sig = inspect.signature(EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_different_is_not_abstract():
    assert not inspect.isabstract(transformation_Different)


def test_transformation_different_constructor_exists():
    assert callable(transformation_Different.__init__)


def test_transformation_different_constructor_args():
    sig = inspect.signature(transformation_Different.__init__)
    params = list(sig.parameters.keys())



def test_transformation_equal_is_not_abstract():
    assert not inspect.isabstract(transformation_Equal)


def test_transformation_equal_constructor_exists():
    assert callable(transformation_Equal.__init__)


def test_transformation_equal_constructor_args():
    sig = inspect.signature(transformation_Equal.__init__)
    params = list(sig.parameters.keys())



def test_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(LogicalExpression)


def test_logicalexpression_constructor_exists():
    assert callable(LogicalExpression.__init__)


def test_logicalexpression_constructor_args():
    sig = inspect.signature(LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_and_is_not_abstract():
    assert not inspect.isabstract(transformation_And)


def test_transformation_and_constructor_exists():
    assert callable(transformation_And.__init__)


def test_transformation_and_constructor_args():
    sig = inspect.signature(transformation_And.__init__)
    params = list(sig.parameters.keys())



def test_transformation_or_is_not_abstract():
    assert not inspect.isabstract(transformation_Or)


def test_transformation_or_constructor_exists():
    assert callable(transformation_Or.__init__)


def test_transformation_or_constructor_args():
    sig = inspect.signature(transformation_Or.__init__)
    params = list(sig.parameters.keys())



def test_transformation_etypedelement_is_not_abstract():
    assert not inspect.isabstract(transformation_ETypedElement)


def test_transformation_etypedelement_constructor_exists():
    assert callable(transformation_ETypedElement.__init__)


def test_transformation_etypedelement_constructor_args():
    sig = inspect.signature(transformation_ETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_featureaccess_is_not_abstract():
    assert not inspect.isabstract(transformation_FeatureAccess)


def test_transformation_featureaccess_constructor_exists():
    assert callable(transformation_FeatureAccess.__init__)


def test_transformation_featureaccess_constructor_args():
    sig = inspect.signature(transformation_FeatureAccess.__init__)
    params = list(sig.parameters.keys())
    assert "spreading" in params, "Missing parameter 'spreading'"
    assert "nullable" in params, "Missing parameter 'nullable'"

def test_transformation_featureaccess_has_spreading():
    assert hasattr(transformation_FeatureAccess, "spreading")
    descriptor = None
    for klass in transformation_FeatureAccess.__mro__:
        if "spreading" in klass.__dict__:
            descriptor = klass.__dict__["spreading"]
            break
    assert isinstance(descriptor, property)

def test_transformation_featureaccess_has_nullable():
    assert hasattr(transformation_FeatureAccess, "nullable")
    descriptor = None
    for klass in transformation_FeatureAccess.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)



def test_transformation_realliteral_is_not_abstract():
    assert not inspect.isabstract(transformation_RealLiteral)


def test_transformation_realliteral_constructor_exists():
    assert callable(transformation_RealLiteral.__init__)


def test_transformation_realliteral_constructor_args():
    sig = inspect.signature(transformation_RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_transformation_realliteral_has_value():
    assert hasattr(transformation_RealLiteral, "value")
    descriptor = None
    for klass in transformation_RealLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_transformation_stringliteral_is_not_abstract():
    assert not inspect.isabstract(transformation_StringLiteral)


def test_transformation_stringliteral_constructor_exists():
    assert callable(transformation_StringLiteral.__init__)


def test_transformation_stringliteral_constructor_args():
    sig = inspect.signature(transformation_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_transformation_stringliteral_has_value():
    assert hasattr(transformation_StringLiteral, "value")
    descriptor = None
    for klass in transformation_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_transformation_extentexpression_is_not_abstract():
    assert not inspect.isabstract(transformation_ExtentExpression)


def test_transformation_extentexpression_constructor_exists():
    assert callable(transformation_ExtentExpression.__init__)


def test_transformation_extentexpression_constructor_args():
    sig = inspect.signature(transformation_ExtentExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(transformation_UnaryExpression)


def test_transformation_unaryexpression_constructor_exists():
    assert callable(transformation_UnaryExpression.__init__)


def test_transformation_unaryexpression_constructor_args():
    sig = inspect.signature(transformation_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_integerliteral_is_not_abstract():
    assert not inspect.isabstract(transformation_IntegerLiteral)


def test_transformation_integerliteral_constructor_exists():
    assert callable(transformation_IntegerLiteral.__init__)


def test_transformation_integerliteral_constructor_args():
    sig = inspect.signature(transformation_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_transformation_integerliteral_has_value():
    assert hasattr(transformation_IntegerLiteral, "value")
    descriptor = None
    for klass in transformation_IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_transformation_map_is_not_abstract():
    assert not inspect.isabstract(transformation_Map)


def test_transformation_map_constructor_exists():
    assert callable(transformation_Map.__init__)


def test_transformation_map_constructor_args():
    sig = inspect.signature(transformation_Map.__init__)
    params = list(sig.parameters.keys())



def test_transformation_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(transformation_BooleanLiteral)


def test_transformation_booleanliteral_constructor_exists():
    assert callable(transformation_BooleanLiteral.__init__)


def test_transformation_booleanliteral_constructor_args():
    sig = inspect.signature(transformation_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_transformation_booleanliteral_has_value():
    assert hasattr(transformation_BooleanLiteral, "value")
    descriptor = None
    for klass in transformation_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_transformation_invocation_is_not_abstract():
    assert not inspect.isabstract(transformation_Invocation)


def test_transformation_invocation_constructor_exists():
    assert callable(transformation_Invocation.__init__)


def test_transformation_invocation_constructor_args():
    sig = inspect.signature(transformation_Invocation.__init__)
    params = list(sig.parameters.keys())



def test_transformation_source_is_not_abstract():
    assert not inspect.isabstract(transformation_Source)


def test_transformation_source_constructor_exists():
    assert callable(transformation_Source.__init__)


def test_transformation_source_constructor_args():
    sig = inspect.signature(transformation_Source.__init__)
    params = list(sig.parameters.keys())



def test_transformation_lambda_is_not_abstract():
    assert not inspect.isabstract(transformation_Lambda)


def test_transformation_lambda_constructor_exists():
    assert callable(transformation_Lambda.__init__)


def test_transformation_lambda_constructor_args():
    sig = inspect.signature(transformation_Lambda.__init__)
    params = list(sig.parameters.keys())



def test_transformation_let_is_not_abstract():
    assert not inspect.isabstract(transformation_Let)


def test_transformation_let_constructor_exists():
    assert callable(transformation_Let.__init__)


def test_transformation_let_constructor_args():
    sig = inspect.signature(transformation_Let.__init__)
    params = list(sig.parameters.keys())



def test_transformation_classliteral_is_not_abstract():
    assert not inspect.isabstract(transformation_ClassLiteral)


def test_transformation_classliteral_constructor_exists():
    assert callable(transformation_ClassLiteral.__init__)


def test_transformation_classliteral_constructor_args():
    sig = inspect.signature(transformation_ClassLiteral.__init__)
    params = list(sig.parameters.keys())



def test_transformation_enumliteral_is_not_abstract():
    assert not inspect.isabstract(transformation_EnumLiteral)


def test_transformation_enumliteral_constructor_exists():
    assert callable(transformation_EnumLiteral.__init__)


def test_transformation_enumliteral_constructor_args():
    sig = inspect.signature(transformation_EnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_transformation_variableuse_is_not_abstract():
    assert not inspect.isabstract(transformation_VariableUse)


def test_transformation_variableuse_constructor_exists():
    assert callable(transformation_VariableUse.__init__)


def test_transformation_variableuse_constructor_args():
    sig = inspect.signature(transformation_VariableUse.__init__)
    params = list(sig.parameters.keys())



def test_transformation_typeofexpression_is_not_abstract():
    assert not inspect.isabstract(transformation_TypeOfExpression)


def test_transformation_typeofexpression_constructor_exists():
    assert callable(transformation_TypeOfExpression.__init__)


def test_transformation_typeofexpression_constructor_args():
    sig = inspect.signature(transformation_TypeOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_if_is_not_abstract():
    assert not inspect.isabstract(transformation_If)


def test_transformation_if_constructor_exists():
    assert callable(transformation_If.__init__)


def test_transformation_if_constructor_args():
    sig = inspect.signature(transformation_If.__init__)
    params = list(sig.parameters.keys())



def test_transformation_variableinitialization_is_not_abstract():
    assert not inspect.isabstract(transformation_VariableInitialization)


def test_transformation_variableinitialization_constructor_exists():
    assert callable(transformation_VariableInitialization.__init__)


def test_transformation_variableinitialization_constructor_args():
    sig = inspect.signature(transformation_VariableInitialization.__init__)
    params = list(sig.parameters.keys())



def test_transformation_variabledefinition_is_not_abstract():
    assert not inspect.isabstract(transformation_VariableDefinition)


def test_transformation_variabledefinition_constructor_exists():
    assert callable(transformation_VariableDefinition.__init__)


def test_transformation_variabledefinition_constructor_args():
    sig = inspect.signature(transformation_VariableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_transformation_variabledefinition_has_name():
    assert hasattr(transformation_VariableDefinition, "name")
    descriptor = None
    for klass in transformation_VariableDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(transformation_LogicalExpression)


def test_transformation_logicalexpression_constructor_exists():
    assert callable(transformation_LogicalExpression.__init__)


def test_transformation_logicalexpression_constructor_args():
    sig = inspect.signature(transformation_LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(transformation_ArithmeticExpression)


def test_transformation_arithmeticexpression_constructor_exists():
    assert callable(transformation_ArithmeticExpression.__init__)


def test_transformation_arithmeticexpression_constructor_args():
    sig = inspect.signature(transformation_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(transformation_RelationalExpression)


def test_transformation_relationalexpression_constructor_exists():
    assert callable(transformation_RelationalExpression.__init__)


def test_transformation_relationalexpression_constructor_args():
    sig = inspect.signature(transformation_RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(transformation_EqualityExpression)


def test_transformation_equalityexpression_constructor_exists():
    assert callable(transformation_EqualityExpression.__init__)


def test_transformation_equalityexpression_constructor_args():
    sig = inspect.signature(transformation_EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_coalescingexpression_is_not_abstract():
    assert not inspect.isabstract(transformation_CoalescingExpression)


def test_transformation_coalescingexpression_constructor_exists():
    assert callable(transformation_CoalescingExpression.__init__)


def test_transformation_coalescingexpression_constructor_args():
    sig = inspect.signature(transformation_CoalescingExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(transformation_BinaryExpression)


def test_transformation_binaryexpression_constructor_exists():
    assert callable(transformation_BinaryExpression.__init__)


def test_transformation_binaryexpression_constructor_args():
    sig = inspect.signature(transformation_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(transformation_ConditionalExpression)


def test_transformation_conditionalexpression_constructor_exists():
    assert callable(transformation_ConditionalExpression.__init__)


def test_transformation_conditionalexpression_constructor_args():
    sig = inspect.signature(transformation_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_contentmapping_is_not_abstract():
    assert not inspect.isabstract(ContentMapping)


def test_contentmapping_constructor_exists():
    assert callable(ContentMapping.__init__)


def test_contentmapping_constructor_args():
    sig = inspect.signature(ContentMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation_conditionalmapping_is_not_abstract():
    assert not inspect.isabstract(transformation_ConditionalMapping)


def test_transformation_conditionalmapping_constructor_exists():
    assert callable(transformation_ConditionalMapping.__init__)


def test_transformation_conditionalmapping_constructor_args():
    sig = inspect.signature(transformation_ConditionalMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation_compositemapping_is_not_abstract():
    assert not inspect.isabstract(transformation_CompositeMapping)


def test_transformation_compositemapping_constructor_exists():
    assert callable(transformation_CompositeMapping.__init__)


def test_transformation_compositemapping_constructor_args():
    sig = inspect.signature(transformation_CompositeMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation_eclass_is_not_abstract():
    assert not inspect.isabstract(transformation_EClass)


def test_transformation_eclass_constructor_exists():
    assert callable(transformation_EClass.__init__)


def test_transformation_eclass_constructor_args():
    sig = inspect.signature(transformation_EClass.__init__)
    params = list(sig.parameters.keys())



def test_transformation_contentmapping_is_not_abstract():
    assert not inspect.isabstract(transformation_ContentMapping)


def test_transformation_contentmapping_constructor_exists():
    assert callable(transformation_ContentMapping.__init__)


def test_transformation_contentmapping_constructor_args():
    sig = inspect.signature(transformation_ContentMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(transformation_EStructuralFeature)


def test_transformation_estructuralfeature_constructor_exists():
    assert callable(transformation_EStructuralFeature.__init__)


def test_transformation_estructuralfeature_constructor_args():
    sig = inspect.signature(transformation_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_transformation_featuremapping_is_not_abstract():
    assert not inspect.isabstract(transformation_FeatureMapping)


def test_transformation_featuremapping_constructor_exists():
    assert callable(transformation_FeatureMapping.__init__)


def test_transformation_featuremapping_constructor_args():
    sig = inspect.signature(transformation_FeatureMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation_resultmapping_is_not_abstract():
    assert not inspect.isabstract(transformation_ResultMapping)


def test_transformation_resultmapping_constructor_exists():
    assert callable(transformation_ResultMapping.__init__)


def test_transformation_resultmapping_constructor_args():
    sig = inspect.signature(transformation_ResultMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation_expression_is_not_abstract():
    assert not inspect.isabstract(transformation_Expression)


def test_transformation_expression_constructor_exists():
    assert callable(transformation_Expression.__init__)


def test_transformation_expression_constructor_args():
    sig = inspect.signature(transformation_Expression.__init__)
    params = list(sig.parameters.keys())



def test_compositemapping_is_not_abstract():
    assert not inspect.isabstract(CompositeMapping)


def test_compositemapping_constructor_exists():
    assert callable(CompositeMapping.__init__)


def test_compositemapping_constructor_args():
    sig = inspect.signature(CompositeMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation_whenclause_is_not_abstract():
    assert not inspect.isabstract(transformation_WhenClause)


def test_transformation_whenclause_constructor_exists():
    assert callable(transformation_WhenClause.__init__)


def test_transformation_whenclause_constructor_args():
    sig = inspect.signature(transformation_WhenClause.__init__)
    params = list(sig.parameters.keys())



def test_transformation_otherwiseclause_is_not_abstract():
    assert not inspect.isabstract(transformation_OtherwiseClause)


def test_transformation_otherwiseclause_constructor_exists():
    assert callable(transformation_OtherwiseClause.__init__)


def test_transformation_otherwiseclause_constructor_args():
    sig = inspect.signature(transformation_OtherwiseClause.__init__)
    params = list(sig.parameters.keys())



def test_transformation_epackage_is_not_abstract():
    assert not inspect.isabstract(transformation_EPackage)


def test_transformation_epackage_constructor_exists():
    assert callable(transformation_EPackage.__init__)


def test_transformation_epackage_constructor_args():
    sig = inspect.signature(transformation_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_transformation_abstractmapping_is_not_abstract():
    assert not inspect.isabstract(transformation_AbstractMapping)


def test_transformation_abstractmapping_constructor_exists():
    assert callable(transformation_AbstractMapping.__init__)


def test_transformation_abstractmapping_constructor_args():
    sig = inspect.signature(transformation_AbstractMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation_metamodeldeclaration_is_not_abstract():
    assert not inspect.isabstract(transformation_MetamodelDeclaration)


def test_transformation_metamodeldeclaration_constructor_exists():
    assert callable(transformation_MetamodelDeclaration.__init__)


def test_transformation_metamodeldeclaration_constructor_args():
    sig = inspect.signature(transformation_MetamodelDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_transformation_transformation_is_not_abstract():
    assert not inspect.isabstract(transformation_Transformation)


def test_transformation_transformation_constructor_exists():
    assert callable(transformation_Transformation.__init__)


def test_transformation_transformation_constructor_args():
    sig = inspect.signature(transformation_Transformation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_transformation_transformation_has_name():
    assert hasattr(transformation_Transformation, "name")
    descriptor = None
    for klass in transformation_Transformation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_transformation_edatatype_is_not_abstract():
    assert not inspect.isabstract(transformation_EDataType)


def test_transformation_edatatype_constructor_exists():
    assert callable(transformation_EDataType.__init__)


def test_transformation_edatatype_constructor_args():
    sig = inspect.signature(transformation_EDataType.__init__)
    params = list(sig.parameters.keys())



def test_abstractmapping_is_not_abstract():
    assert not inspect.isabstract(AbstractMapping)


def test_abstractmapping_constructor_exists():
    assert callable(AbstractMapping.__init__)


def test_abstractmapping_constructor_args():
    sig = inspect.signature(AbstractMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation_classmapping_is_not_abstract():
    assert not inspect.isabstract(transformation_ClassMapping)


def test_transformation_classmapping_constructor_exists():
    assert callable(transformation_ClassMapping.__init__)


def test_transformation_classmapping_constructor_args():
    sig = inspect.signature(transformation_ClassMapping.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_transformation_classmapping_has_default():
    assert hasattr(transformation_ClassMapping, "default")
    descriptor = None
    for klass in transformation_ClassMapping.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_transformation_datatypemapping_is_not_abstract():
    assert not inspect.isabstract(transformation_DataTypeMapping)


def test_transformation_datatypemapping_constructor_exists():
    assert callable(transformation_DataTypeMapping.__init__)


def test_transformation_datatypemapping_constructor_args():
    sig = inspect.signature(transformation_DataTypeMapping.__init__)
    params = list(sig.parameters.keys())



def test_explicitmetamodel_is_not_abstract():
    assert not inspect.isabstract(ExplicitMetamodel)


def test_explicitmetamodel_constructor_exists():
    assert callable(ExplicitMetamodel.__init__)


def test_explicitmetamodel_constructor_args():
    sig = inspect.signature(ExplicitMetamodel.__init__)
    params = list(sig.parameters.keys())



def test_transformation_targetmetamodel_is_not_abstract():
    assert not inspect.isabstract(transformation_TargetMetamodel)


def test_transformation_targetmetamodel_constructor_exists():
    assert callable(transformation_TargetMetamodel.__init__)


def test_transformation_targetmetamodel_constructor_args():
    sig = inspect.signature(transformation_TargetMetamodel.__init__)
    params = list(sig.parameters.keys())



def test_transformation_sourcemetamodel_is_not_abstract():
    assert not inspect.isabstract(transformation_SourceMetamodel)


def test_transformation_sourcemetamodel_constructor_exists():
    assert callable(transformation_SourceMetamodel.__init__)


def test_transformation_sourcemetamodel_constructor_args():
    sig = inspect.signature(transformation_SourceMetamodel.__init__)
    params = list(sig.parameters.keys())



def test_metamodeldeclaration_is_not_abstract():
    assert not inspect.isabstract(MetamodelDeclaration)


def test_metamodeldeclaration_constructor_exists():
    assert callable(MetamodelDeclaration.__init__)


def test_metamodeldeclaration_constructor_args():
    sig = inspect.signature(MetamodelDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_transformation_extentmetamodel_is_not_abstract():
    assert not inspect.isabstract(transformation_ExtentMetamodel)


def test_transformation_extentmetamodel_constructor_exists():
    assert callable(transformation_ExtentMetamodel.__init__)


def test_transformation_extentmetamodel_constructor_args():
    sig = inspect.signature(transformation_ExtentMetamodel.__init__)
    params = list(sig.parameters.keys())
    assert "generated" in params, "Missing parameter 'generated'"

def test_transformation_extentmetamodel_has_generated():
    assert hasattr(transformation_ExtentMetamodel, "generated")
    descriptor = None
    for klass in transformation_ExtentMetamodel.__mro__:
        if "generated" in klass.__dict__:
            descriptor = klass.__dict__["generated"]
            break
    assert isinstance(descriptor, property)



def test_transformation_explicitmetamodel_is_not_abstract():
    assert not inspect.isabstract(transformation_ExplicitMetamodel)


def test_transformation_explicitmetamodel_constructor_exists():
    assert callable(transformation_ExplicitMetamodel.__init__)


def test_transformation_explicitmetamodel_constructor_args():
    sig = inspect.signature(transformation_ExplicitMetamodel.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_transformation_explicitmetamodel_has_alias():
    assert hasattr(transformation_ExplicitMetamodel, "alias")
    descriptor = None
    for klass in transformation_ExplicitMetamodel.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)


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
transformation_EEnumLiteral_strategy = st.builds(
    transformation_EEnumLiteral,
)
transformation_EClassifier_strategy = st.builds(
    transformation_EClassifier,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
transformation_Minus_strategy = st.builds(
    transformation_Minus,
)
transformation_Negation_strategy = st.builds(
    transformation_Negation,
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
transformation_Subtraction_strategy = st.builds(
    transformation_Subtraction,
)
transformation_Multiplication_strategy = st.builds(
    transformation_Multiplication,
)
transformation_Division_strategy = st.builds(
    transformation_Division,
)
transformation_Addition_strategy = st.builds(
    transformation_Addition,
)
RelationalExpression_strategy = st.builds(
    RelationalExpression,
)
transformation_Greater_strategy = st.builds(
    transformation_Greater,
)
transformation_GreaterOrEqual_strategy = st.builds(
    transformation_GreaterOrEqual,
)
transformation_LessOrEqual_strategy = st.builds(
    transformation_LessOrEqual,
)
transformation_Less_strategy = st.builds(
    transformation_Less,
)
EqualityExpression_strategy = st.builds(
    EqualityExpression,
)
transformation_Different_strategy = st.builds(
    transformation_Different,
)
transformation_Equal_strategy = st.builds(
    transformation_Equal,
)
LogicalExpression_strategy = st.builds(
    LogicalExpression,
)
transformation_And_strategy = st.builds(
    transformation_And,
)
transformation_Or_strategy = st.builds(
    transformation_Or,
)
transformation_ETypedElement_strategy = st.builds(
    transformation_ETypedElement,
)
Expression_strategy = st.builds(
    Expression,
)
transformation_FeatureAccess_strategy = st.builds(
    transformation_FeatureAccess,
    spreading=
        st.booleans(),
    nullable=
        st.booleans()
)
transformation_RealLiteral_strategy = st.builds(
    transformation_RealLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
transformation_StringLiteral_strategy = st.builds(
    transformation_StringLiteral,
    value=
        safe_text
)
transformation_ExtentExpression_strategy = st.builds(
    transformation_ExtentExpression,
)
transformation_UnaryExpression_strategy = st.builds(
    transformation_UnaryExpression,
)
transformation_IntegerLiteral_strategy = st.builds(
    transformation_IntegerLiteral,
    value=
        st.integers()
)
transformation_Map_strategy = st.builds(
    transformation_Map,
)
transformation_BooleanLiteral_strategy = st.builds(
    transformation_BooleanLiteral,
    value=
        st.booleans()
)
transformation_Invocation_strategy = st.builds(
    transformation_Invocation,
)
transformation_Source_strategy = st.builds(
    transformation_Source,
)
transformation_Lambda_strategy = st.builds(
    transformation_Lambda,
)
transformation_Let_strategy = st.builds(
    transformation_Let,
)
transformation_ClassLiteral_strategy = st.builds(
    transformation_ClassLiteral,
)
transformation_EnumLiteral_strategy = st.builds(
    transformation_EnumLiteral,
)
transformation_VariableUse_strategy = st.builds(
    transformation_VariableUse,
)
transformation_TypeOfExpression_strategy = st.builds(
    transformation_TypeOfExpression,
)
transformation_If_strategy = st.builds(
    transformation_If,
)
transformation_VariableInitialization_strategy = st.builds(
    transformation_VariableInitialization,
)
transformation_VariableDefinition_strategy = st.builds(
    transformation_VariableDefinition,
    name=
        safe_text
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
transformation_LogicalExpression_strategy = st.builds(
    transformation_LogicalExpression,
)
transformation_ArithmeticExpression_strategy = st.builds(
    transformation_ArithmeticExpression,
)
transformation_RelationalExpression_strategy = st.builds(
    transformation_RelationalExpression,
)
transformation_EqualityExpression_strategy = st.builds(
    transformation_EqualityExpression,
)
transformation_CoalescingExpression_strategy = st.builds(
    transformation_CoalescingExpression,
)
transformation_BinaryExpression_strategy = st.builds(
    transformation_BinaryExpression,
)
transformation_ConditionalExpression_strategy = st.builds(
    transformation_ConditionalExpression,
)
ContentMapping_strategy = st.builds(
    ContentMapping,
)
transformation_ConditionalMapping_strategy = st.builds(
    transformation_ConditionalMapping,
)
transformation_CompositeMapping_strategy = st.builds(
    transformation_CompositeMapping,
)
transformation_EClass_strategy = st.builds(
    transformation_EClass,
)
transformation_ContentMapping_strategy = st.builds(
    transformation_ContentMapping,
)
transformation_EStructuralFeature_strategy = st.builds(
    transformation_EStructuralFeature,
)
transformation_FeatureMapping_strategy = st.builds(
    transformation_FeatureMapping,
)
transformation_ResultMapping_strategy = st.builds(
    transformation_ResultMapping,
)
transformation_Expression_strategy = st.builds(
    transformation_Expression,
)
CompositeMapping_strategy = st.builds(
    CompositeMapping,
)
transformation_WhenClause_strategy = st.builds(
    transformation_WhenClause,
)
transformation_OtherwiseClause_strategy = st.builds(
    transformation_OtherwiseClause,
)
transformation_EPackage_strategy = st.builds(
    transformation_EPackage,
)
transformation_AbstractMapping_strategy = st.builds(
    transformation_AbstractMapping,
)
transformation_MetamodelDeclaration_strategy = st.builds(
    transformation_MetamodelDeclaration,
)
transformation_Transformation_strategy = st.builds(
    transformation_Transformation,
    name=
        safe_text
)
transformation_EDataType_strategy = st.builds(
    transformation_EDataType,
)
AbstractMapping_strategy = st.builds(
    AbstractMapping,
)
transformation_ClassMapping_strategy = st.builds(
    transformation_ClassMapping,
    default=
        st.booleans()
)
transformation_DataTypeMapping_strategy = st.builds(
    transformation_DataTypeMapping,
)
ExplicitMetamodel_strategy = st.builds(
    ExplicitMetamodel,
)
transformation_TargetMetamodel_strategy = st.builds(
    transformation_TargetMetamodel,
)
transformation_SourceMetamodel_strategy = st.builds(
    transformation_SourceMetamodel,
)
MetamodelDeclaration_strategy = st.builds(
    MetamodelDeclaration,
)
transformation_ExtentMetamodel_strategy = st.builds(
    transformation_ExtentMetamodel,
    generated=
        st.booleans()
)
transformation_ExplicitMetamodel_strategy = st.builds(
    transformation_ExplicitMetamodel,
    alias=
        safe_text
)

@given(instance=transformation_EEnumLiteral_strategy)
@settings(max_examples=50)
def test_transformation_eenumliteral_instantiation(instance):
    assert isinstance(instance, transformation_EEnumLiteral)

@given(instance=transformation_EClassifier_strategy)
@settings(max_examples=50)
def test_transformation_eclassifier_instantiation(instance):
    assert isinstance(instance, transformation_EClassifier)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=transformation_Minus_strategy)
@settings(max_examples=50)
def test_transformation_minus_instantiation(instance):
    assert isinstance(instance, transformation_Minus)

@given(instance=transformation_Negation_strategy)
@settings(max_examples=50)
def test_transformation_negation_instantiation(instance):
    assert isinstance(instance, transformation_Negation)

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=transformation_Subtraction_strategy)
@settings(max_examples=50)
def test_transformation_subtraction_instantiation(instance):
    assert isinstance(instance, transformation_Subtraction)

@given(instance=transformation_Multiplication_strategy)
@settings(max_examples=50)
def test_transformation_multiplication_instantiation(instance):
    assert isinstance(instance, transformation_Multiplication)

@given(instance=transformation_Division_strategy)
@settings(max_examples=50)
def test_transformation_division_instantiation(instance):
    assert isinstance(instance, transformation_Division)

@given(instance=transformation_Addition_strategy)
@settings(max_examples=50)
def test_transformation_addition_instantiation(instance):
    assert isinstance(instance, transformation_Addition)

@given(instance=RelationalExpression_strategy)
@settings(max_examples=50)
def test_relationalexpression_instantiation(instance):
    assert isinstance(instance, RelationalExpression)

@given(instance=transformation_Greater_strategy)
@settings(max_examples=50)
def test_transformation_greater_instantiation(instance):
    assert isinstance(instance, transformation_Greater)

@given(instance=transformation_GreaterOrEqual_strategy)
@settings(max_examples=50)
def test_transformation_greaterorequal_instantiation(instance):
    assert isinstance(instance, transformation_GreaterOrEqual)

@given(instance=transformation_LessOrEqual_strategy)
@settings(max_examples=50)
def test_transformation_lessorequal_instantiation(instance):
    assert isinstance(instance, transformation_LessOrEqual)

@given(instance=transformation_Less_strategy)
@settings(max_examples=50)
def test_transformation_less_instantiation(instance):
    assert isinstance(instance, transformation_Less)

@given(instance=EqualityExpression_strategy)
@settings(max_examples=50)
def test_equalityexpression_instantiation(instance):
    assert isinstance(instance, EqualityExpression)

@given(instance=transformation_Different_strategy)
@settings(max_examples=50)
def test_transformation_different_instantiation(instance):
    assert isinstance(instance, transformation_Different)

@given(instance=transformation_Equal_strategy)
@settings(max_examples=50)
def test_transformation_equal_instantiation(instance):
    assert isinstance(instance, transformation_Equal)

@given(instance=LogicalExpression_strategy)
@settings(max_examples=50)
def test_logicalexpression_instantiation(instance):
    assert isinstance(instance, LogicalExpression)

@given(instance=transformation_And_strategy)
@settings(max_examples=50)
def test_transformation_and_instantiation(instance):
    assert isinstance(instance, transformation_And)

@given(instance=transformation_Or_strategy)
@settings(max_examples=50)
def test_transformation_or_instantiation(instance):
    assert isinstance(instance, transformation_Or)

@given(instance=transformation_ETypedElement_strategy)
@settings(max_examples=50)
def test_transformation_etypedelement_instantiation(instance):
    assert isinstance(instance, transformation_ETypedElement)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=transformation_FeatureAccess_strategy)
@settings(max_examples=50)
def test_transformation_featureaccess_instantiation(instance):
    assert isinstance(instance, transformation_FeatureAccess)



@given(instance=transformation_FeatureAccess_strategy)
def test_transformation_featureaccess_spreading_setter(instance):
    original = instance.spreading
    instance.spreading = original
    assert instance.spreading == original



@given(instance=transformation_FeatureAccess_strategy)
def test_transformation_featureaccess_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=transformation_RealLiteral_strategy)
@settings(max_examples=50)
def test_transformation_realliteral_instantiation(instance):
    assert isinstance(instance, transformation_RealLiteral)



@given(instance=transformation_RealLiteral_strategy)
def test_transformation_realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=transformation_StringLiteral_strategy)
@settings(max_examples=50)
def test_transformation_stringliteral_instantiation(instance):
    assert isinstance(instance, transformation_StringLiteral)



@given(instance=transformation_StringLiteral_strategy)
def test_transformation_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=transformation_ExtentExpression_strategy)
@settings(max_examples=50)
def test_transformation_extentexpression_instantiation(instance):
    assert isinstance(instance, transformation_ExtentExpression)

@given(instance=transformation_UnaryExpression_strategy)
@settings(max_examples=50)
def test_transformation_unaryexpression_instantiation(instance):
    assert isinstance(instance, transformation_UnaryExpression)

@given(instance=transformation_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_transformation_integerliteral_instantiation(instance):
    assert isinstance(instance, transformation_IntegerLiteral)



@given(instance=transformation_IntegerLiteral_strategy)
def test_transformation_integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=transformation_Map_strategy)
@settings(max_examples=50)
def test_transformation_map_instantiation(instance):
    assert isinstance(instance, transformation_Map)

@given(instance=transformation_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_transformation_booleanliteral_instantiation(instance):
    assert isinstance(instance, transformation_BooleanLiteral)



@given(instance=transformation_BooleanLiteral_strategy)
def test_transformation_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=transformation_Invocation_strategy)
@settings(max_examples=50)
def test_transformation_invocation_instantiation(instance):
    assert isinstance(instance, transformation_Invocation)

@given(instance=transformation_Source_strategy)
@settings(max_examples=50)
def test_transformation_source_instantiation(instance):
    assert isinstance(instance, transformation_Source)

@given(instance=transformation_Lambda_strategy)
@settings(max_examples=50)
def test_transformation_lambda_instantiation(instance):
    assert isinstance(instance, transformation_Lambda)

@given(instance=transformation_Let_strategy)
@settings(max_examples=50)
def test_transformation_let_instantiation(instance):
    assert isinstance(instance, transformation_Let)

@given(instance=transformation_ClassLiteral_strategy)
@settings(max_examples=50)
def test_transformation_classliteral_instantiation(instance):
    assert isinstance(instance, transformation_ClassLiteral)

@given(instance=transformation_EnumLiteral_strategy)
@settings(max_examples=50)
def test_transformation_enumliteral_instantiation(instance):
    assert isinstance(instance, transformation_EnumLiteral)

@given(instance=transformation_VariableUse_strategy)
@settings(max_examples=50)
def test_transformation_variableuse_instantiation(instance):
    assert isinstance(instance, transformation_VariableUse)

@given(instance=transformation_TypeOfExpression_strategy)
@settings(max_examples=50)
def test_transformation_typeofexpression_instantiation(instance):
    assert isinstance(instance, transformation_TypeOfExpression)

@given(instance=transformation_If_strategy)
@settings(max_examples=50)
def test_transformation_if_instantiation(instance):
    assert isinstance(instance, transformation_If)

@given(instance=transformation_VariableInitialization_strategy)
@settings(max_examples=50)
def test_transformation_variableinitialization_instantiation(instance):
    assert isinstance(instance, transformation_VariableInitialization)

@given(instance=transformation_VariableDefinition_strategy)
@settings(max_examples=50)
def test_transformation_variabledefinition_instantiation(instance):
    assert isinstance(instance, transformation_VariableDefinition)



@given(instance=transformation_VariableDefinition_strategy)
def test_transformation_variabledefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=transformation_LogicalExpression_strategy)
@settings(max_examples=50)
def test_transformation_logicalexpression_instantiation(instance):
    assert isinstance(instance, transformation_LogicalExpression)

@given(instance=transformation_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_transformation_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, transformation_ArithmeticExpression)

@given(instance=transformation_RelationalExpression_strategy)
@settings(max_examples=50)
def test_transformation_relationalexpression_instantiation(instance):
    assert isinstance(instance, transformation_RelationalExpression)

@given(instance=transformation_EqualityExpression_strategy)
@settings(max_examples=50)
def test_transformation_equalityexpression_instantiation(instance):
    assert isinstance(instance, transformation_EqualityExpression)

@given(instance=transformation_CoalescingExpression_strategy)
@settings(max_examples=50)
def test_transformation_coalescingexpression_instantiation(instance):
    assert isinstance(instance, transformation_CoalescingExpression)

@given(instance=transformation_BinaryExpression_strategy)
@settings(max_examples=50)
def test_transformation_binaryexpression_instantiation(instance):
    assert isinstance(instance, transformation_BinaryExpression)

@given(instance=transformation_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_transformation_conditionalexpression_instantiation(instance):
    assert isinstance(instance, transformation_ConditionalExpression)

@given(instance=ContentMapping_strategy)
@settings(max_examples=50)
def test_contentmapping_instantiation(instance):
    assert isinstance(instance, ContentMapping)

@given(instance=transformation_ConditionalMapping_strategy)
@settings(max_examples=50)
def test_transformation_conditionalmapping_instantiation(instance):
    assert isinstance(instance, transformation_ConditionalMapping)

@given(instance=transformation_CompositeMapping_strategy)
@settings(max_examples=50)
def test_transformation_compositemapping_instantiation(instance):
    assert isinstance(instance, transformation_CompositeMapping)

@given(instance=transformation_EClass_strategy)
@settings(max_examples=50)
def test_transformation_eclass_instantiation(instance):
    assert isinstance(instance, transformation_EClass)

@given(instance=transformation_ContentMapping_strategy)
@settings(max_examples=50)
def test_transformation_contentmapping_instantiation(instance):
    assert isinstance(instance, transformation_ContentMapping)

@given(instance=transformation_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_transformation_estructuralfeature_instantiation(instance):
    assert isinstance(instance, transformation_EStructuralFeature)

@given(instance=transformation_FeatureMapping_strategy)
@settings(max_examples=50)
def test_transformation_featuremapping_instantiation(instance):
    assert isinstance(instance, transformation_FeatureMapping)

@given(instance=transformation_ResultMapping_strategy)
@settings(max_examples=50)
def test_transformation_resultmapping_instantiation(instance):
    assert isinstance(instance, transformation_ResultMapping)

@given(instance=transformation_Expression_strategy)
@settings(max_examples=50)
def test_transformation_expression_instantiation(instance):
    assert isinstance(instance, transformation_Expression)

@given(instance=CompositeMapping_strategy)
@settings(max_examples=50)
def test_compositemapping_instantiation(instance):
    assert isinstance(instance, CompositeMapping)

@given(instance=transformation_WhenClause_strategy)
@settings(max_examples=50)
def test_transformation_whenclause_instantiation(instance):
    assert isinstance(instance, transformation_WhenClause)

@given(instance=transformation_OtherwiseClause_strategy)
@settings(max_examples=50)
def test_transformation_otherwiseclause_instantiation(instance):
    assert isinstance(instance, transformation_OtherwiseClause)

@given(instance=transformation_EPackage_strategy)
@settings(max_examples=50)
def test_transformation_epackage_instantiation(instance):
    assert isinstance(instance, transformation_EPackage)

@given(instance=transformation_AbstractMapping_strategy)
@settings(max_examples=50)
def test_transformation_abstractmapping_instantiation(instance):
    assert isinstance(instance, transformation_AbstractMapping)

@given(instance=transformation_MetamodelDeclaration_strategy)
@settings(max_examples=50)
def test_transformation_metamodeldeclaration_instantiation(instance):
    assert isinstance(instance, transformation_MetamodelDeclaration)

@given(instance=transformation_Transformation_strategy)
@settings(max_examples=50)
def test_transformation_transformation_instantiation(instance):
    assert isinstance(instance, transformation_Transformation)



@given(instance=transformation_Transformation_strategy)
def test_transformation_transformation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=transformation_EDataType_strategy)
@settings(max_examples=50)
def test_transformation_edatatype_instantiation(instance):
    assert isinstance(instance, transformation_EDataType)

@given(instance=AbstractMapping_strategy)
@settings(max_examples=50)
def test_abstractmapping_instantiation(instance):
    assert isinstance(instance, AbstractMapping)

@given(instance=transformation_ClassMapping_strategy)
@settings(max_examples=50)
def test_transformation_classmapping_instantiation(instance):
    assert isinstance(instance, transformation_ClassMapping)



@given(instance=transformation_ClassMapping_strategy)
def test_transformation_classmapping_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=transformation_DataTypeMapping_strategy)
@settings(max_examples=50)
def test_transformation_datatypemapping_instantiation(instance):
    assert isinstance(instance, transformation_DataTypeMapping)

@given(instance=ExplicitMetamodel_strategy)
@settings(max_examples=50)
def test_explicitmetamodel_instantiation(instance):
    assert isinstance(instance, ExplicitMetamodel)

@given(instance=transformation_TargetMetamodel_strategy)
@settings(max_examples=50)
def test_transformation_targetmetamodel_instantiation(instance):
    assert isinstance(instance, transformation_TargetMetamodel)

@given(instance=transformation_SourceMetamodel_strategy)
@settings(max_examples=50)
def test_transformation_sourcemetamodel_instantiation(instance):
    assert isinstance(instance, transformation_SourceMetamodel)

@given(instance=MetamodelDeclaration_strategy)
@settings(max_examples=50)
def test_metamodeldeclaration_instantiation(instance):
    assert isinstance(instance, MetamodelDeclaration)

@given(instance=transformation_ExtentMetamodel_strategy)
@settings(max_examples=50)
def test_transformation_extentmetamodel_instantiation(instance):
    assert isinstance(instance, transformation_ExtentMetamodel)



@given(instance=transformation_ExtentMetamodel_strategy)
def test_transformation_extentmetamodel_generated_setter(instance):
    original = instance.generated
    instance.generated = original
    assert instance.generated == original

@given(instance=transformation_ExplicitMetamodel_strategy)
@settings(max_examples=50)
def test_transformation_explicitmetamodel_instantiation(instance):
    assert isinstance(instance, transformation_ExplicitMetamodel)



@given(instance=transformation_ExplicitMetamodel_strategy)
def test_transformation_explicitmetamodel_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original
