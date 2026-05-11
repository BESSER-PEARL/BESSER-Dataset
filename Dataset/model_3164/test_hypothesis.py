import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    transformation::EEnumLiteral,
    UnaryExpression,
    transformation::Negation,
    ArithmeticExpression,
    transformation::Multiplication,
    transformation::Division,
    transformation::Subtraction,
    transformation::Addition,
    RelationalExpression,
    transformation::GreaterOrEqual,
    transformation::Greater,
    transformation::LessOrEqual,
    transformation::Less,
    EqualityExpression,
    transformation::Different,
    transformation::Equal,
    LogicalExpression,
    transformation::And,
    transformation::Or,
    BinaryExpression,
    transformation::LogicalExpression,
    transformation::ArithmeticExpression,
    transformation::RelationalExpression,
    transformation::EqualityExpression,
    transformation::CoalescingExpression,
    transformation::ETypedElement,
    transformation::Minus,
    transformation::VariableInitialization,
    transformation::VariableDefinition,
    transformation::EStructuralFeature,
    transformation::Expression,
    CompositeMapping,
    transformation::OtherwiseClause,
    transformation::WhenClause,
    ContentMapping,
    transformation::ResultMapping,
    transformation::ConditionalMapping,
    transformation::FeatureMapping,
    transformation::CompositeMapping,
    transformation::EClass,
    transformation::ContentMapping,
    transformation::EDataType,
    Expression,
    transformation::BinaryExpression,
    transformation::IntegerLiteral,
    transformation::ConditionalExpression,
    transformation::FeatureAccess,
    transformation::Let,
    transformation::UnaryExpression,
    transformation::EnumLiteral,
    transformation::BooleanLiteral,
    transformation::If,
    ExplicitMetamodel,
    transformation::TargetMetamodel,
    transformation::SourceMetamodel,
    MetamodelDeclaration,
    transformation::ExplicitMetamodel,
    transformation::EPackage,
    transformation::AbstractMapping,
    transformation::MetamodelDeclaration,
    transformation::Transformation,
    AbstractMapping,
    transformation::ClassMapping,
    transformation::DataTypeMapping,
    transformation::ExtentMetamodel,
    transformation::ClassLiteral,
    transformation::VariableUse,
    transformation::Source,
    transformation::EClassifier,
    transformation::Map,
    transformation::Lambda,
    transformation::Invocation,
    transformation::StringLiteral,
    transformation::TypeOfExpression,
    transformation::RealLiteral,
    transformation::ExtentExpression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transformation::eenumliteral_is_not_abstract():
    assert not inspect.isabstract(transformation::EEnumLiteral)


def test_transformation::eenumliteral_constructor_exists():
    assert callable(transformation::EEnumLiteral.__init__)


def test_transformation::eenumliteral_constructor_args():
    sig = inspect.signature(transformation::EEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::negation_is_not_abstract():
    assert not inspect.isabstract(transformation::Negation)


def test_transformation::negation_constructor_exists():
    assert callable(transformation::Negation.__init__)


def test_transformation::negation_constructor_args():
    sig = inspect.signature(transformation::Negation.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::multiplication_is_not_abstract():
    assert not inspect.isabstract(transformation::Multiplication)


def test_transformation::multiplication_constructor_exists():
    assert callable(transformation::Multiplication.__init__)


def test_transformation::multiplication_constructor_args():
    sig = inspect.signature(transformation::Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_transformation::division_is_not_abstract():
    assert not inspect.isabstract(transformation::Division)


def test_transformation::division_constructor_exists():
    assert callable(transformation::Division.__init__)


def test_transformation::division_constructor_args():
    sig = inspect.signature(transformation::Division.__init__)
    params = list(sig.parameters.keys())



def test_transformation::subtraction_is_not_abstract():
    assert not inspect.isabstract(transformation::Subtraction)


def test_transformation::subtraction_constructor_exists():
    assert callable(transformation::Subtraction.__init__)


def test_transformation::subtraction_constructor_args():
    sig = inspect.signature(transformation::Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_transformation::addition_is_not_abstract():
    assert not inspect.isabstract(transformation::Addition)


def test_transformation::addition_constructor_exists():
    assert callable(transformation::Addition.__init__)


def test_transformation::addition_constructor_args():
    sig = inspect.signature(transformation::Addition.__init__)
    params = list(sig.parameters.keys())



def test_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(RelationalExpression)


def test_relationalexpression_constructor_exists():
    assert callable(RelationalExpression.__init__)


def test_relationalexpression_constructor_args():
    sig = inspect.signature(RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::greaterorequal_is_not_abstract():
    assert not inspect.isabstract(transformation::GreaterOrEqual)


def test_transformation::greaterorequal_constructor_exists():
    assert callable(transformation::GreaterOrEqual.__init__)


def test_transformation::greaterorequal_constructor_args():
    sig = inspect.signature(transformation::GreaterOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_transformation::greater_is_not_abstract():
    assert not inspect.isabstract(transformation::Greater)


def test_transformation::greater_constructor_exists():
    assert callable(transformation::Greater.__init__)


def test_transformation::greater_constructor_args():
    sig = inspect.signature(transformation::Greater.__init__)
    params = list(sig.parameters.keys())



def test_transformation::lessorequal_is_not_abstract():
    assert not inspect.isabstract(transformation::LessOrEqual)


def test_transformation::lessorequal_constructor_exists():
    assert callable(transformation::LessOrEqual.__init__)


def test_transformation::lessorequal_constructor_args():
    sig = inspect.signature(transformation::LessOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_transformation::less_is_not_abstract():
    assert not inspect.isabstract(transformation::Less)


def test_transformation::less_constructor_exists():
    assert callable(transformation::Less.__init__)


def test_transformation::less_constructor_args():
    sig = inspect.signature(transformation::Less.__init__)
    params = list(sig.parameters.keys())



def test_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(EqualityExpression)


def test_equalityexpression_constructor_exists():
    assert callable(EqualityExpression.__init__)


def test_equalityexpression_constructor_args():
    sig = inspect.signature(EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::different_is_not_abstract():
    assert not inspect.isabstract(transformation::Different)


def test_transformation::different_constructor_exists():
    assert callable(transformation::Different.__init__)


def test_transformation::different_constructor_args():
    sig = inspect.signature(transformation::Different.__init__)
    params = list(sig.parameters.keys())



def test_transformation::equal_is_not_abstract():
    assert not inspect.isabstract(transformation::Equal)


def test_transformation::equal_constructor_exists():
    assert callable(transformation::Equal.__init__)


def test_transformation::equal_constructor_args():
    sig = inspect.signature(transformation::Equal.__init__)
    params = list(sig.parameters.keys())



def test_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(LogicalExpression)


def test_logicalexpression_constructor_exists():
    assert callable(LogicalExpression.__init__)


def test_logicalexpression_constructor_args():
    sig = inspect.signature(LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::and_is_not_abstract():
    assert not inspect.isabstract(transformation::And)


def test_transformation::and_constructor_exists():
    assert callable(transformation::And.__init__)


def test_transformation::and_constructor_args():
    sig = inspect.signature(transformation::And.__init__)
    params = list(sig.parameters.keys())



def test_transformation::or_is_not_abstract():
    assert not inspect.isabstract(transformation::Or)


def test_transformation::or_constructor_exists():
    assert callable(transformation::Or.__init__)


def test_transformation::or_constructor_args():
    sig = inspect.signature(transformation::Or.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::logicalexpression_is_not_abstract():
    assert not inspect.isabstract(transformation::LogicalExpression)


def test_transformation::logicalexpression_constructor_exists():
    assert callable(transformation::LogicalExpression.__init__)


def test_transformation::logicalexpression_constructor_args():
    sig = inspect.signature(transformation::LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(transformation::ArithmeticExpression)


def test_transformation::arithmeticexpression_constructor_exists():
    assert callable(transformation::ArithmeticExpression.__init__)


def test_transformation::arithmeticexpression_constructor_args():
    sig = inspect.signature(transformation::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(transformation::RelationalExpression)


def test_transformation::relationalexpression_constructor_exists():
    assert callable(transformation::RelationalExpression.__init__)


def test_transformation::relationalexpression_constructor_args():
    sig = inspect.signature(transformation::RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(transformation::EqualityExpression)


def test_transformation::equalityexpression_constructor_exists():
    assert callable(transformation::EqualityExpression.__init__)


def test_transformation::equalityexpression_constructor_args():
    sig = inspect.signature(transformation::EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::coalescingexpression_is_not_abstract():
    assert not inspect.isabstract(transformation::CoalescingExpression)


def test_transformation::coalescingexpression_constructor_exists():
    assert callable(transformation::CoalescingExpression.__init__)


def test_transformation::coalescingexpression_constructor_args():
    sig = inspect.signature(transformation::CoalescingExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::etypedelement_is_not_abstract():
    assert not inspect.isabstract(transformation::ETypedElement)


def test_transformation::etypedelement_constructor_exists():
    assert callable(transformation::ETypedElement.__init__)


def test_transformation::etypedelement_constructor_args():
    sig = inspect.signature(transformation::ETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_transformation::minus_is_not_abstract():
    assert not inspect.isabstract(transformation::Minus)


def test_transformation::minus_constructor_exists():
    assert callable(transformation::Minus.__init__)


def test_transformation::minus_constructor_args():
    sig = inspect.signature(transformation::Minus.__init__)
    params = list(sig.parameters.keys())



def test_transformation::variableinitialization_is_not_abstract():
    assert not inspect.isabstract(transformation::VariableInitialization)


def test_transformation::variableinitialization_constructor_exists():
    assert callable(transformation::VariableInitialization.__init__)


def test_transformation::variableinitialization_constructor_args():
    sig = inspect.signature(transformation::VariableInitialization.__init__)
    params = list(sig.parameters.keys())



def test_transformation::variabledefinition_is_not_abstract():
    assert not inspect.isabstract(transformation::VariableDefinition)


def test_transformation::variabledefinition_constructor_exists():
    assert callable(transformation::VariableDefinition.__init__)


def test_transformation::variabledefinition_constructor_args():
    sig = inspect.signature(transformation::VariableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_transformation::variabledefinition_has_name():
    assert hasattr(transformation::VariableDefinition, "name")
    descriptor = None
    for klass in transformation::VariableDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_transformation::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(transformation::EStructuralFeature)


def test_transformation::estructuralfeature_constructor_exists():
    assert callable(transformation::EStructuralFeature.__init__)


def test_transformation::estructuralfeature_constructor_args():
    sig = inspect.signature(transformation::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_transformation::expression_is_not_abstract():
    assert not inspect.isabstract(transformation::Expression)


def test_transformation::expression_constructor_exists():
    assert callable(transformation::Expression.__init__)


def test_transformation::expression_constructor_args():
    sig = inspect.signature(transformation::Expression.__init__)
    params = list(sig.parameters.keys())



def test_compositemapping_is_not_abstract():
    assert not inspect.isabstract(CompositeMapping)


def test_compositemapping_constructor_exists():
    assert callable(CompositeMapping.__init__)


def test_compositemapping_constructor_args():
    sig = inspect.signature(CompositeMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation::otherwiseclause_is_not_abstract():
    assert not inspect.isabstract(transformation::OtherwiseClause)


def test_transformation::otherwiseclause_constructor_exists():
    assert callable(transformation::OtherwiseClause.__init__)


def test_transformation::otherwiseclause_constructor_args():
    sig = inspect.signature(transformation::OtherwiseClause.__init__)
    params = list(sig.parameters.keys())



def test_transformation::whenclause_is_not_abstract():
    assert not inspect.isabstract(transformation::WhenClause)


def test_transformation::whenclause_constructor_exists():
    assert callable(transformation::WhenClause.__init__)


def test_transformation::whenclause_constructor_args():
    sig = inspect.signature(transformation::WhenClause.__init__)
    params = list(sig.parameters.keys())



def test_contentmapping_is_not_abstract():
    assert not inspect.isabstract(ContentMapping)


def test_contentmapping_constructor_exists():
    assert callable(ContentMapping.__init__)


def test_contentmapping_constructor_args():
    sig = inspect.signature(ContentMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation::resultmapping_is_not_abstract():
    assert not inspect.isabstract(transformation::ResultMapping)


def test_transformation::resultmapping_constructor_exists():
    assert callable(transformation::ResultMapping.__init__)


def test_transformation::resultmapping_constructor_args():
    sig = inspect.signature(transformation::ResultMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation::conditionalmapping_is_not_abstract():
    assert not inspect.isabstract(transformation::ConditionalMapping)


def test_transformation::conditionalmapping_constructor_exists():
    assert callable(transformation::ConditionalMapping.__init__)


def test_transformation::conditionalmapping_constructor_args():
    sig = inspect.signature(transformation::ConditionalMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation::featuremapping_is_not_abstract():
    assert not inspect.isabstract(transformation::FeatureMapping)


def test_transformation::featuremapping_constructor_exists():
    assert callable(transformation::FeatureMapping.__init__)


def test_transformation::featuremapping_constructor_args():
    sig = inspect.signature(transformation::FeatureMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation::compositemapping_is_not_abstract():
    assert not inspect.isabstract(transformation::CompositeMapping)


def test_transformation::compositemapping_constructor_exists():
    assert callable(transformation::CompositeMapping.__init__)


def test_transformation::compositemapping_constructor_args():
    sig = inspect.signature(transformation::CompositeMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation::eclass_is_not_abstract():
    assert not inspect.isabstract(transformation::EClass)


def test_transformation::eclass_constructor_exists():
    assert callable(transformation::EClass.__init__)


def test_transformation::eclass_constructor_args():
    sig = inspect.signature(transformation::EClass.__init__)
    params = list(sig.parameters.keys())



def test_transformation::contentmapping_is_not_abstract():
    assert not inspect.isabstract(transformation::ContentMapping)


def test_transformation::contentmapping_constructor_exists():
    assert callable(transformation::ContentMapping.__init__)


def test_transformation::contentmapping_constructor_args():
    sig = inspect.signature(transformation::ContentMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation::edatatype_is_not_abstract():
    assert not inspect.isabstract(transformation::EDataType)


def test_transformation::edatatype_constructor_exists():
    assert callable(transformation::EDataType.__init__)


def test_transformation::edatatype_constructor_args():
    sig = inspect.signature(transformation::EDataType.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(transformation::BinaryExpression)


def test_transformation::binaryexpression_constructor_exists():
    assert callable(transformation::BinaryExpression.__init__)


def test_transformation::binaryexpression_constructor_args():
    sig = inspect.signature(transformation::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::integerliteral_is_not_abstract():
    assert not inspect.isabstract(transformation::IntegerLiteral)


def test_transformation::integerliteral_constructor_exists():
    assert callable(transformation::IntegerLiteral.__init__)


def test_transformation::integerliteral_constructor_args():
    sig = inspect.signature(transformation::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_transformation::integerliteral_has_value():
    assert hasattr(transformation::IntegerLiteral, "value")
    descriptor = None
    for klass in transformation::IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_transformation::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(transformation::ConditionalExpression)


def test_transformation::conditionalexpression_constructor_exists():
    assert callable(transformation::ConditionalExpression.__init__)


def test_transformation::conditionalexpression_constructor_args():
    sig = inspect.signature(transformation::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::featureaccess_is_not_abstract():
    assert not inspect.isabstract(transformation::FeatureAccess)


def test_transformation::featureaccess_constructor_exists():
    assert callable(transformation::FeatureAccess.__init__)


def test_transformation::featureaccess_constructor_args():
    sig = inspect.signature(transformation::FeatureAccess.__init__)
    params = list(sig.parameters.keys())
    assert "spreading" in params, "Missing parameter 'spreading'"
    assert "nullable" in params, "Missing parameter 'nullable'"

def test_transformation::featureaccess_has_spreading():
    assert hasattr(transformation::FeatureAccess, "spreading")
    descriptor = None
    for klass in transformation::FeatureAccess.__mro__:
        if "spreading" in klass.__dict__:
            descriptor = klass.__dict__["spreading"]
            break
    assert isinstance(descriptor, property)

def test_transformation::featureaccess_has_nullable():
    assert hasattr(transformation::FeatureAccess, "nullable")
    descriptor = None
    for klass in transformation::FeatureAccess.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)



def test_transformation::let_is_not_abstract():
    assert not inspect.isabstract(transformation::Let)


def test_transformation::let_constructor_exists():
    assert callable(transformation::Let.__init__)


def test_transformation::let_constructor_args():
    sig = inspect.signature(transformation::Let.__init__)
    params = list(sig.parameters.keys())



def test_transformation::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(transformation::UnaryExpression)


def test_transformation::unaryexpression_constructor_exists():
    assert callable(transformation::UnaryExpression.__init__)


def test_transformation::unaryexpression_constructor_args():
    sig = inspect.signature(transformation::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::enumliteral_is_not_abstract():
    assert not inspect.isabstract(transformation::EnumLiteral)


def test_transformation::enumliteral_constructor_exists():
    assert callable(transformation::EnumLiteral.__init__)


def test_transformation::enumliteral_constructor_args():
    sig = inspect.signature(transformation::EnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_transformation::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(transformation::BooleanLiteral)


def test_transformation::booleanliteral_constructor_exists():
    assert callable(transformation::BooleanLiteral.__init__)


def test_transformation::booleanliteral_constructor_args():
    sig = inspect.signature(transformation::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_transformation::booleanliteral_has_value():
    assert hasattr(transformation::BooleanLiteral, "value")
    descriptor = None
    for klass in transformation::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_transformation::if_is_not_abstract():
    assert not inspect.isabstract(transformation::If)


def test_transformation::if_constructor_exists():
    assert callable(transformation::If.__init__)


def test_transformation::if_constructor_args():
    sig = inspect.signature(transformation::If.__init__)
    params = list(sig.parameters.keys())



def test_explicitmetamodel_is_not_abstract():
    assert not inspect.isabstract(ExplicitMetamodel)


def test_explicitmetamodel_constructor_exists():
    assert callable(ExplicitMetamodel.__init__)


def test_explicitmetamodel_constructor_args():
    sig = inspect.signature(ExplicitMetamodel.__init__)
    params = list(sig.parameters.keys())



def test_transformation::targetmetamodel_is_not_abstract():
    assert not inspect.isabstract(transformation::TargetMetamodel)


def test_transformation::targetmetamodel_constructor_exists():
    assert callable(transformation::TargetMetamodel.__init__)


def test_transformation::targetmetamodel_constructor_args():
    sig = inspect.signature(transformation::TargetMetamodel.__init__)
    params = list(sig.parameters.keys())



def test_transformation::sourcemetamodel_is_not_abstract():
    assert not inspect.isabstract(transformation::SourceMetamodel)


def test_transformation::sourcemetamodel_constructor_exists():
    assert callable(transformation::SourceMetamodel.__init__)


def test_transformation::sourcemetamodel_constructor_args():
    sig = inspect.signature(transformation::SourceMetamodel.__init__)
    params = list(sig.parameters.keys())



def test_metamodeldeclaration_is_not_abstract():
    assert not inspect.isabstract(MetamodelDeclaration)


def test_metamodeldeclaration_constructor_exists():
    assert callable(MetamodelDeclaration.__init__)


def test_metamodeldeclaration_constructor_args():
    sig = inspect.signature(MetamodelDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_transformation::explicitmetamodel_is_not_abstract():
    assert not inspect.isabstract(transformation::ExplicitMetamodel)


def test_transformation::explicitmetamodel_constructor_exists():
    assert callable(transformation::ExplicitMetamodel.__init__)


def test_transformation::explicitmetamodel_constructor_args():
    sig = inspect.signature(transformation::ExplicitMetamodel.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_transformation::explicitmetamodel_has_alias():
    assert hasattr(transformation::ExplicitMetamodel, "alias")
    descriptor = None
    for klass in transformation::ExplicitMetamodel.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_transformation::epackage_is_not_abstract():
    assert not inspect.isabstract(transformation::EPackage)


def test_transformation::epackage_constructor_exists():
    assert callable(transformation::EPackage.__init__)


def test_transformation::epackage_constructor_args():
    sig = inspect.signature(transformation::EPackage.__init__)
    params = list(sig.parameters.keys())



def test_transformation::abstractmapping_is_not_abstract():
    assert not inspect.isabstract(transformation::AbstractMapping)


def test_transformation::abstractmapping_constructor_exists():
    assert callable(transformation::AbstractMapping.__init__)


def test_transformation::abstractmapping_constructor_args():
    sig = inspect.signature(transformation::AbstractMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation::metamodeldeclaration_is_not_abstract():
    assert not inspect.isabstract(transformation::MetamodelDeclaration)


def test_transformation::metamodeldeclaration_constructor_exists():
    assert callable(transformation::MetamodelDeclaration.__init__)


def test_transformation::metamodeldeclaration_constructor_args():
    sig = inspect.signature(transformation::MetamodelDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_transformation::transformation_is_not_abstract():
    assert not inspect.isabstract(transformation::Transformation)


def test_transformation::transformation_constructor_exists():
    assert callable(transformation::Transformation.__init__)


def test_transformation::transformation_constructor_args():
    sig = inspect.signature(transformation::Transformation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_transformation::transformation_has_name():
    assert hasattr(transformation::Transformation, "name")
    descriptor = None
    for klass in transformation::Transformation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractmapping_is_not_abstract():
    assert not inspect.isabstract(AbstractMapping)


def test_abstractmapping_constructor_exists():
    assert callable(AbstractMapping.__init__)


def test_abstractmapping_constructor_args():
    sig = inspect.signature(AbstractMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation::classmapping_is_not_abstract():
    assert not inspect.isabstract(transformation::ClassMapping)


def test_transformation::classmapping_constructor_exists():
    assert callable(transformation::ClassMapping.__init__)


def test_transformation::classmapping_constructor_args():
    sig = inspect.signature(transformation::ClassMapping.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_transformation::classmapping_has_default():
    assert hasattr(transformation::ClassMapping, "default")
    descriptor = None
    for klass in transformation::ClassMapping.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_transformation::datatypemapping_is_not_abstract():
    assert not inspect.isabstract(transformation::DataTypeMapping)


def test_transformation::datatypemapping_constructor_exists():
    assert callable(transformation::DataTypeMapping.__init__)


def test_transformation::datatypemapping_constructor_args():
    sig = inspect.signature(transformation::DataTypeMapping.__init__)
    params = list(sig.parameters.keys())



def test_transformation::extentmetamodel_is_not_abstract():
    assert not inspect.isabstract(transformation::ExtentMetamodel)


def test_transformation::extentmetamodel_constructor_exists():
    assert callable(transformation::ExtentMetamodel.__init__)


def test_transformation::extentmetamodel_constructor_args():
    sig = inspect.signature(transformation::ExtentMetamodel.__init__)
    params = list(sig.parameters.keys())
    assert "generated" in params, "Missing parameter 'generated'"

def test_transformation::extentmetamodel_has_generated():
    assert hasattr(transformation::ExtentMetamodel, "generated")
    descriptor = None
    for klass in transformation::ExtentMetamodel.__mro__:
        if "generated" in klass.__dict__:
            descriptor = klass.__dict__["generated"]
            break
    assert isinstance(descriptor, property)



def test_transformation::classliteral_is_not_abstract():
    assert not inspect.isabstract(transformation::ClassLiteral)


def test_transformation::classliteral_constructor_exists():
    assert callable(transformation::ClassLiteral.__init__)


def test_transformation::classliteral_constructor_args():
    sig = inspect.signature(transformation::ClassLiteral.__init__)
    params = list(sig.parameters.keys())



def test_transformation::variableuse_is_not_abstract():
    assert not inspect.isabstract(transformation::VariableUse)


def test_transformation::variableuse_constructor_exists():
    assert callable(transformation::VariableUse.__init__)


def test_transformation::variableuse_constructor_args():
    sig = inspect.signature(transformation::VariableUse.__init__)
    params = list(sig.parameters.keys())



def test_transformation::source_is_not_abstract():
    assert not inspect.isabstract(transformation::Source)


def test_transformation::source_constructor_exists():
    assert callable(transformation::Source.__init__)


def test_transformation::source_constructor_args():
    sig = inspect.signature(transformation::Source.__init__)
    params = list(sig.parameters.keys())



def test_transformation::eclassifier_is_not_abstract():
    assert not inspect.isabstract(transformation::EClassifier)


def test_transformation::eclassifier_constructor_exists():
    assert callable(transformation::EClassifier.__init__)


def test_transformation::eclassifier_constructor_args():
    sig = inspect.signature(transformation::EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_transformation::map_is_not_abstract():
    assert not inspect.isabstract(transformation::Map)


def test_transformation::map_constructor_exists():
    assert callable(transformation::Map.__init__)


def test_transformation::map_constructor_args():
    sig = inspect.signature(transformation::Map.__init__)
    params = list(sig.parameters.keys())



def test_transformation::lambda_is_not_abstract():
    assert not inspect.isabstract(transformation::Lambda)


def test_transformation::lambda_constructor_exists():
    assert callable(transformation::Lambda.__init__)


def test_transformation::lambda_constructor_args():
    sig = inspect.signature(transformation::Lambda.__init__)
    params = list(sig.parameters.keys())



def test_transformation::invocation_is_not_abstract():
    assert not inspect.isabstract(transformation::Invocation)


def test_transformation::invocation_constructor_exists():
    assert callable(transformation::Invocation.__init__)


def test_transformation::invocation_constructor_args():
    sig = inspect.signature(transformation::Invocation.__init__)
    params = list(sig.parameters.keys())



def test_transformation::stringliteral_is_not_abstract():
    assert not inspect.isabstract(transformation::StringLiteral)


def test_transformation::stringliteral_constructor_exists():
    assert callable(transformation::StringLiteral.__init__)


def test_transformation::stringliteral_constructor_args():
    sig = inspect.signature(transformation::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_transformation::stringliteral_has_value():
    assert hasattr(transformation::StringLiteral, "value")
    descriptor = None
    for klass in transformation::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_transformation::typeofexpression_is_not_abstract():
    assert not inspect.isabstract(transformation::TypeOfExpression)


def test_transformation::typeofexpression_constructor_exists():
    assert callable(transformation::TypeOfExpression.__init__)


def test_transformation::typeofexpression_constructor_args():
    sig = inspect.signature(transformation::TypeOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_transformation::realliteral_is_not_abstract():
    assert not inspect.isabstract(transformation::RealLiteral)


def test_transformation::realliteral_constructor_exists():
    assert callable(transformation::RealLiteral.__init__)


def test_transformation::realliteral_constructor_args():
    sig = inspect.signature(transformation::RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_transformation::realliteral_has_value():
    assert hasattr(transformation::RealLiteral, "value")
    descriptor = None
    for klass in transformation::RealLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_transformation::extentexpression_is_not_abstract():
    assert not inspect.isabstract(transformation::ExtentExpression)


def test_transformation::extentexpression_constructor_exists():
    assert callable(transformation::ExtentExpression.__init__)


def test_transformation::extentexpression_constructor_args():
    sig = inspect.signature(transformation::ExtentExpression.__init__)
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
transformation::EEnumLiteral_strategy = st.builds(
    transformation::EEnumLiteral,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
transformation::Negation_strategy = st.builds(
    transformation::Negation,
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
transformation::Multiplication_strategy = st.builds(
    transformation::Multiplication,
)
transformation::Division_strategy = st.builds(
    transformation::Division,
)
transformation::Subtraction_strategy = st.builds(
    transformation::Subtraction,
)
transformation::Addition_strategy = st.builds(
    transformation::Addition,
)
RelationalExpression_strategy = st.builds(
    RelationalExpression,
)
transformation::GreaterOrEqual_strategy = st.builds(
    transformation::GreaterOrEqual,
)
transformation::Greater_strategy = st.builds(
    transformation::Greater,
)
transformation::LessOrEqual_strategy = st.builds(
    transformation::LessOrEqual,
)
transformation::Less_strategy = st.builds(
    transformation::Less,
)
EqualityExpression_strategy = st.builds(
    EqualityExpression,
)
transformation::Different_strategy = st.builds(
    transformation::Different,
)
transformation::Equal_strategy = st.builds(
    transformation::Equal,
)
LogicalExpression_strategy = st.builds(
    LogicalExpression,
)
transformation::And_strategy = st.builds(
    transformation::And,
)
transformation::Or_strategy = st.builds(
    transformation::Or,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
transformation::LogicalExpression_strategy = st.builds(
    transformation::LogicalExpression,
)
transformation::ArithmeticExpression_strategy = st.builds(
    transformation::ArithmeticExpression,
)
transformation::RelationalExpression_strategy = st.builds(
    transformation::RelationalExpression,
)
transformation::EqualityExpression_strategy = st.builds(
    transformation::EqualityExpression,
)
transformation::CoalescingExpression_strategy = st.builds(
    transformation::CoalescingExpression,
)
transformation::ETypedElement_strategy = st.builds(
    transformation::ETypedElement,
)
transformation::Minus_strategy = st.builds(
    transformation::Minus,
)
transformation::VariableInitialization_strategy = st.builds(
    transformation::VariableInitialization,
)
transformation::VariableDefinition_strategy = st.builds(
    transformation::VariableDefinition,
    name=
        safe_text
)
transformation::EStructuralFeature_strategy = st.builds(
    transformation::EStructuralFeature,
)
transformation::Expression_strategy = st.builds(
    transformation::Expression,
)
CompositeMapping_strategy = st.builds(
    CompositeMapping,
)
transformation::OtherwiseClause_strategy = st.builds(
    transformation::OtherwiseClause,
)
transformation::WhenClause_strategy = st.builds(
    transformation::WhenClause,
)
ContentMapping_strategy = st.builds(
    ContentMapping,
)
transformation::ResultMapping_strategy = st.builds(
    transformation::ResultMapping,
)
transformation::ConditionalMapping_strategy = st.builds(
    transformation::ConditionalMapping,
)
transformation::FeatureMapping_strategy = st.builds(
    transformation::FeatureMapping,
)
transformation::CompositeMapping_strategy = st.builds(
    transformation::CompositeMapping,
)
transformation::EClass_strategy = st.builds(
    transformation::EClass,
)
transformation::ContentMapping_strategy = st.builds(
    transformation::ContentMapping,
)
transformation::EDataType_strategy = st.builds(
    transformation::EDataType,
)
Expression_strategy = st.builds(
    Expression,
)
transformation::BinaryExpression_strategy = st.builds(
    transformation::BinaryExpression,
)
transformation::IntegerLiteral_strategy = st.builds(
    transformation::IntegerLiteral,
    value=
        st.integers()
)
transformation::ConditionalExpression_strategy = st.builds(
    transformation::ConditionalExpression,
)
transformation::FeatureAccess_strategy = st.builds(
    transformation::FeatureAccess,
    spreading=
        st.booleans(),
    nullable=
        st.booleans()
)
transformation::Let_strategy = st.builds(
    transformation::Let,
)
transformation::UnaryExpression_strategy = st.builds(
    transformation::UnaryExpression,
)
transformation::EnumLiteral_strategy = st.builds(
    transformation::EnumLiteral,
)
transformation::BooleanLiteral_strategy = st.builds(
    transformation::BooleanLiteral,
    value=
        st.booleans()
)
transformation::If_strategy = st.builds(
    transformation::If,
)
ExplicitMetamodel_strategy = st.builds(
    ExplicitMetamodel,
)
transformation::TargetMetamodel_strategy = st.builds(
    transformation::TargetMetamodel,
)
transformation::SourceMetamodel_strategy = st.builds(
    transformation::SourceMetamodel,
)
MetamodelDeclaration_strategy = st.builds(
    MetamodelDeclaration,
)
transformation::ExplicitMetamodel_strategy = st.builds(
    transformation::ExplicitMetamodel,
    alias=
        safe_text
)
transformation::EPackage_strategy = st.builds(
    transformation::EPackage,
)
transformation::AbstractMapping_strategy = st.builds(
    transformation::AbstractMapping,
)
transformation::MetamodelDeclaration_strategy = st.builds(
    transformation::MetamodelDeclaration,
)
transformation::Transformation_strategy = st.builds(
    transformation::Transformation,
    name=
        safe_text
)
AbstractMapping_strategy = st.builds(
    AbstractMapping,
)
transformation::ClassMapping_strategy = st.builds(
    transformation::ClassMapping,
    default=
        st.booleans()
)
transformation::DataTypeMapping_strategy = st.builds(
    transformation::DataTypeMapping,
)
transformation::ExtentMetamodel_strategy = st.builds(
    transformation::ExtentMetamodel,
    generated=
        st.booleans()
)
transformation::ClassLiteral_strategy = st.builds(
    transformation::ClassLiteral,
)
transformation::VariableUse_strategy = st.builds(
    transformation::VariableUse,
)
transformation::Source_strategy = st.builds(
    transformation::Source,
)
transformation::EClassifier_strategy = st.builds(
    transformation::EClassifier,
)
transformation::Map_strategy = st.builds(
    transformation::Map,
)
transformation::Lambda_strategy = st.builds(
    transformation::Lambda,
)
transformation::Invocation_strategy = st.builds(
    transformation::Invocation,
)
transformation::StringLiteral_strategy = st.builds(
    transformation::StringLiteral,
    value=
        safe_text
)
transformation::TypeOfExpression_strategy = st.builds(
    transformation::TypeOfExpression,
)
transformation::RealLiteral_strategy = st.builds(
    transformation::RealLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
transformation::ExtentExpression_strategy = st.builds(
    transformation::ExtentExpression,
)

@given(instance=transformation::EEnumLiteral_strategy)
@settings(max_examples=50)
def test_transformation::eenumliteral_instantiation(instance):
    assert isinstance(instance, transformation::EEnumLiteral)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=transformation::Negation_strategy)
@settings(max_examples=50)
def test_transformation::negation_instantiation(instance):
    assert isinstance(instance, transformation::Negation)

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=transformation::Multiplication_strategy)
@settings(max_examples=50)
def test_transformation::multiplication_instantiation(instance):
    assert isinstance(instance, transformation::Multiplication)

@given(instance=transformation::Division_strategy)
@settings(max_examples=50)
def test_transformation::division_instantiation(instance):
    assert isinstance(instance, transformation::Division)

@given(instance=transformation::Subtraction_strategy)
@settings(max_examples=50)
def test_transformation::subtraction_instantiation(instance):
    assert isinstance(instance, transformation::Subtraction)

@given(instance=transformation::Addition_strategy)
@settings(max_examples=50)
def test_transformation::addition_instantiation(instance):
    assert isinstance(instance, transformation::Addition)

@given(instance=RelationalExpression_strategy)
@settings(max_examples=50)
def test_relationalexpression_instantiation(instance):
    assert isinstance(instance, RelationalExpression)

@given(instance=transformation::GreaterOrEqual_strategy)
@settings(max_examples=50)
def test_transformation::greaterorequal_instantiation(instance):
    assert isinstance(instance, transformation::GreaterOrEqual)

@given(instance=transformation::Greater_strategy)
@settings(max_examples=50)
def test_transformation::greater_instantiation(instance):
    assert isinstance(instance, transformation::Greater)

@given(instance=transformation::LessOrEqual_strategy)
@settings(max_examples=50)
def test_transformation::lessorequal_instantiation(instance):
    assert isinstance(instance, transformation::LessOrEqual)

@given(instance=transformation::Less_strategy)
@settings(max_examples=50)
def test_transformation::less_instantiation(instance):
    assert isinstance(instance, transformation::Less)

@given(instance=EqualityExpression_strategy)
@settings(max_examples=50)
def test_equalityexpression_instantiation(instance):
    assert isinstance(instance, EqualityExpression)

@given(instance=transformation::Different_strategy)
@settings(max_examples=50)
def test_transformation::different_instantiation(instance):
    assert isinstance(instance, transformation::Different)

@given(instance=transformation::Equal_strategy)
@settings(max_examples=50)
def test_transformation::equal_instantiation(instance):
    assert isinstance(instance, transformation::Equal)

@given(instance=LogicalExpression_strategy)
@settings(max_examples=50)
def test_logicalexpression_instantiation(instance):
    assert isinstance(instance, LogicalExpression)

@given(instance=transformation::And_strategy)
@settings(max_examples=50)
def test_transformation::and_instantiation(instance):
    assert isinstance(instance, transformation::And)

@given(instance=transformation::Or_strategy)
@settings(max_examples=50)
def test_transformation::or_instantiation(instance):
    assert isinstance(instance, transformation::Or)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=transformation::LogicalExpression_strategy)
@settings(max_examples=50)
def test_transformation::logicalexpression_instantiation(instance):
    assert isinstance(instance, transformation::LogicalExpression)

@given(instance=transformation::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_transformation::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, transformation::ArithmeticExpression)

@given(instance=transformation::RelationalExpression_strategy)
@settings(max_examples=50)
def test_transformation::relationalexpression_instantiation(instance):
    assert isinstance(instance, transformation::RelationalExpression)

@given(instance=transformation::EqualityExpression_strategy)
@settings(max_examples=50)
def test_transformation::equalityexpression_instantiation(instance):
    assert isinstance(instance, transformation::EqualityExpression)

@given(instance=transformation::CoalescingExpression_strategy)
@settings(max_examples=50)
def test_transformation::coalescingexpression_instantiation(instance):
    assert isinstance(instance, transformation::CoalescingExpression)

@given(instance=transformation::ETypedElement_strategy)
@settings(max_examples=50)
def test_transformation::etypedelement_instantiation(instance):
    assert isinstance(instance, transformation::ETypedElement)

@given(instance=transformation::Minus_strategy)
@settings(max_examples=50)
def test_transformation::minus_instantiation(instance):
    assert isinstance(instance, transformation::Minus)

@given(instance=transformation::VariableInitialization_strategy)
@settings(max_examples=50)
def test_transformation::variableinitialization_instantiation(instance):
    assert isinstance(instance, transformation::VariableInitialization)

@given(instance=transformation::VariableDefinition_strategy)
@settings(max_examples=50)
def test_transformation::variabledefinition_instantiation(instance):
    assert isinstance(instance, transformation::VariableDefinition)

@given(instance=transformation::VariableDefinition_strategy)
def test_transformation::variabledefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=transformation::VariableDefinition_strategy)
def test_transformation::variabledefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=transformation::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_transformation::estructuralfeature_instantiation(instance):
    assert isinstance(instance, transformation::EStructuralFeature)

@given(instance=transformation::Expression_strategy)
@settings(max_examples=50)
def test_transformation::expression_instantiation(instance):
    assert isinstance(instance, transformation::Expression)

@given(instance=CompositeMapping_strategy)
@settings(max_examples=50)
def test_compositemapping_instantiation(instance):
    assert isinstance(instance, CompositeMapping)

@given(instance=transformation::OtherwiseClause_strategy)
@settings(max_examples=50)
def test_transformation::otherwiseclause_instantiation(instance):
    assert isinstance(instance, transformation::OtherwiseClause)

@given(instance=transformation::WhenClause_strategy)
@settings(max_examples=50)
def test_transformation::whenclause_instantiation(instance):
    assert isinstance(instance, transformation::WhenClause)

@given(instance=ContentMapping_strategy)
@settings(max_examples=50)
def test_contentmapping_instantiation(instance):
    assert isinstance(instance, ContentMapping)

@given(instance=transformation::ResultMapping_strategy)
@settings(max_examples=50)
def test_transformation::resultmapping_instantiation(instance):
    assert isinstance(instance, transformation::ResultMapping)

@given(instance=transformation::ConditionalMapping_strategy)
@settings(max_examples=50)
def test_transformation::conditionalmapping_instantiation(instance):
    assert isinstance(instance, transformation::ConditionalMapping)

@given(instance=transformation::FeatureMapping_strategy)
@settings(max_examples=50)
def test_transformation::featuremapping_instantiation(instance):
    assert isinstance(instance, transformation::FeatureMapping)

@given(instance=transformation::CompositeMapping_strategy)
@settings(max_examples=50)
def test_transformation::compositemapping_instantiation(instance):
    assert isinstance(instance, transformation::CompositeMapping)

@given(instance=transformation::EClass_strategy)
@settings(max_examples=50)
def test_transformation::eclass_instantiation(instance):
    assert isinstance(instance, transformation::EClass)

@given(instance=transformation::ContentMapping_strategy)
@settings(max_examples=50)
def test_transformation::contentmapping_instantiation(instance):
    assert isinstance(instance, transformation::ContentMapping)

@given(instance=transformation::EDataType_strategy)
@settings(max_examples=50)
def test_transformation::edatatype_instantiation(instance):
    assert isinstance(instance, transformation::EDataType)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=transformation::BinaryExpression_strategy)
@settings(max_examples=50)
def test_transformation::binaryexpression_instantiation(instance):
    assert isinstance(instance, transformation::BinaryExpression)

@given(instance=transformation::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_transformation::integerliteral_instantiation(instance):
    assert isinstance(instance, transformation::IntegerLiteral)

@given(instance=transformation::IntegerLiteral_strategy)
def test_transformation::integerliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=transformation::IntegerLiteral_strategy)
def test_transformation::integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=transformation::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_transformation::conditionalexpression_instantiation(instance):
    assert isinstance(instance, transformation::ConditionalExpression)

@given(instance=transformation::FeatureAccess_strategy)
@settings(max_examples=50)
def test_transformation::featureaccess_instantiation(instance):
    assert isinstance(instance, transformation::FeatureAccess)

@given(instance=transformation::FeatureAccess_strategy)
def test_transformation::featureaccess_spreading_type(instance):
    assert isinstance(instance.spreading, bool)


@given(instance=transformation::FeatureAccess_strategy)
def test_transformation::featureaccess_spreading_setter(instance):
    original = instance.spreading
    instance.spreading = original
    assert instance.spreading == original

@given(instance=transformation::FeatureAccess_strategy)
def test_transformation::featureaccess_nullable_type(instance):
    assert isinstance(instance.nullable, bool)


@given(instance=transformation::FeatureAccess_strategy)
def test_transformation::featureaccess_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=transformation::Let_strategy)
@settings(max_examples=50)
def test_transformation::let_instantiation(instance):
    assert isinstance(instance, transformation::Let)

@given(instance=transformation::UnaryExpression_strategy)
@settings(max_examples=50)
def test_transformation::unaryexpression_instantiation(instance):
    assert isinstance(instance, transformation::UnaryExpression)

@given(instance=transformation::EnumLiteral_strategy)
@settings(max_examples=50)
def test_transformation::enumliteral_instantiation(instance):
    assert isinstance(instance, transformation::EnumLiteral)

@given(instance=transformation::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_transformation::booleanliteral_instantiation(instance):
    assert isinstance(instance, transformation::BooleanLiteral)

@given(instance=transformation::BooleanLiteral_strategy)
def test_transformation::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=transformation::BooleanLiteral_strategy)
def test_transformation::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=transformation::If_strategy)
@settings(max_examples=50)
def test_transformation::if_instantiation(instance):
    assert isinstance(instance, transformation::If)

@given(instance=ExplicitMetamodel_strategy)
@settings(max_examples=50)
def test_explicitmetamodel_instantiation(instance):
    assert isinstance(instance, ExplicitMetamodel)

@given(instance=transformation::TargetMetamodel_strategy)
@settings(max_examples=50)
def test_transformation::targetmetamodel_instantiation(instance):
    assert isinstance(instance, transformation::TargetMetamodel)

@given(instance=transformation::SourceMetamodel_strategy)
@settings(max_examples=50)
def test_transformation::sourcemetamodel_instantiation(instance):
    assert isinstance(instance, transformation::SourceMetamodel)

@given(instance=MetamodelDeclaration_strategy)
@settings(max_examples=50)
def test_metamodeldeclaration_instantiation(instance):
    assert isinstance(instance, MetamodelDeclaration)

@given(instance=transformation::ExplicitMetamodel_strategy)
@settings(max_examples=50)
def test_transformation::explicitmetamodel_instantiation(instance):
    assert isinstance(instance, transformation::ExplicitMetamodel)

@given(instance=transformation::ExplicitMetamodel_strategy)
def test_transformation::explicitmetamodel_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=transformation::ExplicitMetamodel_strategy)
def test_transformation::explicitmetamodel_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=transformation::EPackage_strategy)
@settings(max_examples=50)
def test_transformation::epackage_instantiation(instance):
    assert isinstance(instance, transformation::EPackage)

@given(instance=transformation::AbstractMapping_strategy)
@settings(max_examples=50)
def test_transformation::abstractmapping_instantiation(instance):
    assert isinstance(instance, transformation::AbstractMapping)

@given(instance=transformation::MetamodelDeclaration_strategy)
@settings(max_examples=50)
def test_transformation::metamodeldeclaration_instantiation(instance):
    assert isinstance(instance, transformation::MetamodelDeclaration)

@given(instance=transformation::Transformation_strategy)
@settings(max_examples=50)
def test_transformation::transformation_instantiation(instance):
    assert isinstance(instance, transformation::Transformation)

@given(instance=transformation::Transformation_strategy)
def test_transformation::transformation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=transformation::Transformation_strategy)
def test_transformation::transformation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractMapping_strategy)
@settings(max_examples=50)
def test_abstractmapping_instantiation(instance):
    assert isinstance(instance, AbstractMapping)

@given(instance=transformation::ClassMapping_strategy)
@settings(max_examples=50)
def test_transformation::classmapping_instantiation(instance):
    assert isinstance(instance, transformation::ClassMapping)

@given(instance=transformation::ClassMapping_strategy)
def test_transformation::classmapping_default_type(instance):
    assert isinstance(instance.default, bool)


@given(instance=transformation::ClassMapping_strategy)
def test_transformation::classmapping_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=transformation::DataTypeMapping_strategy)
@settings(max_examples=50)
def test_transformation::datatypemapping_instantiation(instance):
    assert isinstance(instance, transformation::DataTypeMapping)

@given(instance=transformation::ExtentMetamodel_strategy)
@settings(max_examples=50)
def test_transformation::extentmetamodel_instantiation(instance):
    assert isinstance(instance, transformation::ExtentMetamodel)

@given(instance=transformation::ExtentMetamodel_strategy)
def test_transformation::extentmetamodel_generated_type(instance):
    assert isinstance(instance.generated, bool)


@given(instance=transformation::ExtentMetamodel_strategy)
def test_transformation::extentmetamodel_generated_setter(instance):
    original = instance.generated
    instance.generated = original
    assert instance.generated == original

@given(instance=transformation::ClassLiteral_strategy)
@settings(max_examples=50)
def test_transformation::classliteral_instantiation(instance):
    assert isinstance(instance, transformation::ClassLiteral)

@given(instance=transformation::VariableUse_strategy)
@settings(max_examples=50)
def test_transformation::variableuse_instantiation(instance):
    assert isinstance(instance, transformation::VariableUse)

@given(instance=transformation::Source_strategy)
@settings(max_examples=50)
def test_transformation::source_instantiation(instance):
    assert isinstance(instance, transformation::Source)

@given(instance=transformation::EClassifier_strategy)
@settings(max_examples=50)
def test_transformation::eclassifier_instantiation(instance):
    assert isinstance(instance, transformation::EClassifier)

@given(instance=transformation::Map_strategy)
@settings(max_examples=50)
def test_transformation::map_instantiation(instance):
    assert isinstance(instance, transformation::Map)

@given(instance=transformation::Lambda_strategy)
@settings(max_examples=50)
def test_transformation::lambda_instantiation(instance):
    assert isinstance(instance, transformation::Lambda)

@given(instance=transformation::Invocation_strategy)
@settings(max_examples=50)
def test_transformation::invocation_instantiation(instance):
    assert isinstance(instance, transformation::Invocation)

@given(instance=transformation::StringLiteral_strategy)
@settings(max_examples=50)
def test_transformation::stringliteral_instantiation(instance):
    assert isinstance(instance, transformation::StringLiteral)

@given(instance=transformation::StringLiteral_strategy)
def test_transformation::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=transformation::StringLiteral_strategy)
def test_transformation::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=transformation::TypeOfExpression_strategy)
@settings(max_examples=50)
def test_transformation::typeofexpression_instantiation(instance):
    assert isinstance(instance, transformation::TypeOfExpression)

@given(instance=transformation::RealLiteral_strategy)
@settings(max_examples=50)
def test_transformation::realliteral_instantiation(instance):
    assert isinstance(instance, transformation::RealLiteral)

@given(instance=transformation::RealLiteral_strategy)
def test_transformation::realliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=transformation::RealLiteral_strategy)
def test_transformation::realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=transformation::ExtentExpression_strategy)
@settings(max_examples=50)
def test_transformation::extentexpression_instantiation(instance):
    assert isinstance(instance, transformation::ExtentExpression)
