import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PseudoType,
    eol::SelfContentType,
    eol::SelfType,
    AssignmentStatement,
    eol::SpecialAssignmentStatement,
    CollectionInitValue,
    eol::ExpRange,
    eol::ExprList,
    VariableDeclarationExpression,
    eol::EClassifier,
    NameExpression,
    eol::SpecialNameExpression,
    Annotation,
    eol::SimpleAnnotation,
    eol::ExecutableAnnotation,
    OrderedCollectionType,
    eol::SequenceType,
    CollectionType,
    eol::UniqueCollectionType,
    eol::OrderedCollectionType,
    eol::BagType,
    UniqueCollectionType,
    eol::OrderedSetType,
    eol::SetType,
    PrimitiveType,
    eol::RealType,
    eol::IntegerType,
    eol::StringType,
    eol::BooleanType,
    Type,
    eol::MapType,
    eol::CollectionType,
    eol::EType,
    eol::ModelElementType,
    eol::PrimitiveType,
    eol::VoidType,
    eol::NativeType,
    eol::PseudoType,
    eol::ModelType,
    eol::AnyType,
    CollectionExpression,
    eol::OrderedSetExpression,
    eol::SequenceExpression,
    eol::BagExpression,
    eol::SetExpression,
    LiteralExpression,
    eol::MapExpression,
    eol::CollectionExpression,
    eol::NativeExpression,
    eol::PrimitiveExpression,
    SwitchCaseStatement,
    eol::EPackage,
    eol::SwitchCaseDefaultStatement,
    eol::SwitchCaseExpressionStatement,
    Statement,
    eol::TransactionStatement,
    eol::ReturnStatement,
    eol::BreakAllStatement,
    eol::SwitchStatement,
    eol::DeleteStatement,
    eol::ForStatement,
    eol::AbortStatement,
    eol::ThrowStatement,
    eol::IfStatement,
    eol::ModelDeclarationStatement,
    eol::WhileStatement,
    eol::SwitchCaseStatement,
    eol::BreakStatement,
    eol::ContinueStatement,
    eol::ExpressionStatement,
    BinaryOperatorExpression,
    eol::ComparisonOperatorExpression,
    eol::ArithmeticOperatorExpression,
    eol::LogicalOperatorExpression,
    eol::OperationArgType,
    eol::SelfInnermostType,
    eol::AssignmentStatement,
    eol::FormalParameterExpression,
    UnaryOperatorExpression,
    eol::NotOperatorExpression,
    eol::NegativeOperatorExpression,
    eol::EObject,
    FeatureCallExpression,
    eol::PropertyCallExpression,
    eol::FOLMethodCallExpression,
    eol::MethodCallExpression,
    ComparisonOperatorExpression,
    eol::NotEqualsOperatorExpression,
    eol::LessThanOrEqualToOperatorExpression,
    eol::GreaterThanOrEqualToOperatorExpression,
    eol::GreaterThanOperatorExpression,
    eol::LessThanOperatorExpression,
    eol::EqualsOperatorExpression,
    eol::ModelExpression,
    ArithmeticOperatorExpression,
    eol::PlusOperatorExpression,
    eol::MinusOperatorExpression,
    eol::MultiplyOperatorExpression,
    eol::DivideOperatorExpression,
    PrimitiveExpression,
    eol::RealExpression,
    eol::IntegerExpression,
    eol::BooleanExpression,
    LogicalOperatorExpression,
    eol::ImpliesOperatorExpression,
    eol::OrOperatorExpression,
    eol::XorOperatorExpression,
    eol::AndOperatorExpression,
    OperatorExpression,
    eol::UnaryOperatorExpression,
    eol::BinaryOperatorExpression,
    Expression,
    eol::EnumerationLiteralExpression,
    eol::NameExpression,
    eol::LiteralExpression,
    eol::ModelDeclarationParameter,
    eol::FeatureCallExpression,
    eol::CollectionInitValue,
    eol::KeyValue,
    eol::VariableDeclarationExpression,
    eol::NewExpression,
    eol::OperatorExpression,
    eol::StringExpression,
    EolElement,
    eol::EolLibraryModule,
    eol::Statement,
    eol::Expression,
    eol::OperationDefinition,
    eol::AnnotationBlock,
    eol::ExpressionOrStatementBlock,
    eol::Annotation,
    eol::Type,
    eol::Import,
    eol::Block,
    EolLibraryModule,
    eol::EolProgram,
    eol::TextPosition,
    eol::TextRegion,
    eol::EolElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pseudotype_is_not_abstract():
    assert not inspect.isabstract(PseudoType)


def test_pseudotype_constructor_exists():
    assert callable(PseudoType.__init__)


def test_pseudotype_constructor_args():
    sig = inspect.signature(PseudoType.__init__)
    params = list(sig.parameters.keys())



def test_eol::selfcontenttype_is_not_abstract():
    assert not inspect.isabstract(eol::SelfContentType)


def test_eol::selfcontenttype_constructor_exists():
    assert callable(eol::SelfContentType.__init__)


def test_eol::selfcontenttype_constructor_args():
    sig = inspect.signature(eol::SelfContentType.__init__)
    params = list(sig.parameters.keys())



def test_eol::selftype_is_not_abstract():
    assert not inspect.isabstract(eol::SelfType)


def test_eol::selftype_constructor_exists():
    assert callable(eol::SelfType.__init__)


def test_eol::selftype_constructor_args():
    sig = inspect.signature(eol::SelfType.__init__)
    params = list(sig.parameters.keys())



def test_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(AssignmentStatement)


def test_assignmentstatement_constructor_exists():
    assert callable(AssignmentStatement.__init__)


def test_assignmentstatement_constructor_args():
    sig = inspect.signature(AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::specialassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(eol::SpecialAssignmentStatement)


def test_eol::specialassignmentstatement_constructor_exists():
    assert callable(eol::SpecialAssignmentStatement.__init__)


def test_eol::specialassignmentstatement_constructor_args():
    sig = inspect.signature(eol::SpecialAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_collectioninitvalue_is_not_abstract():
    assert not inspect.isabstract(CollectionInitValue)


def test_collectioninitvalue_constructor_exists():
    assert callable(CollectionInitValue.__init__)


def test_collectioninitvalue_constructor_args():
    sig = inspect.signature(CollectionInitValue.__init__)
    params = list(sig.parameters.keys())



def test_eol::exprange_is_not_abstract():
    assert not inspect.isabstract(eol::ExpRange)


def test_eol::exprange_constructor_exists():
    assert callable(eol::ExpRange.__init__)


def test_eol::exprange_constructor_args():
    sig = inspect.signature(eol::ExpRange.__init__)
    params = list(sig.parameters.keys())



def test_eol::exprlist_is_not_abstract():
    assert not inspect.isabstract(eol::ExprList)


def test_eol::exprlist_constructor_exists():
    assert callable(eol::ExprList.__init__)


def test_eol::exprlist_constructor_args():
    sig = inspect.signature(eol::ExprList.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationExpression)


def test_variabledeclarationexpression_constructor_exists():
    assert callable(VariableDeclarationExpression.__init__)


def test_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::eclassifier_is_not_abstract():
    assert not inspect.isabstract(eol::EClassifier)


def test_eol::eclassifier_constructor_exists():
    assert callable(eol::EClassifier.__init__)


def test_eol::eclassifier_constructor_args():
    sig = inspect.signature(eol::EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_nameexpression_is_not_abstract():
    assert not inspect.isabstract(NameExpression)


def test_nameexpression_constructor_exists():
    assert callable(NameExpression.__init__)


def test_nameexpression_constructor_args():
    sig = inspect.signature(NameExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::specialnameexpression_is_not_abstract():
    assert not inspect.isabstract(eol::SpecialNameExpression)


def test_eol::specialnameexpression_constructor_exists():
    assert callable(eol::SpecialNameExpression.__init__)


def test_eol::specialnameexpression_constructor_args():
    sig = inspect.signature(eol::SpecialNameExpression.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_eol::simpleannotation_is_not_abstract():
    assert not inspect.isabstract(eol::SimpleAnnotation)


def test_eol::simpleannotation_constructor_exists():
    assert callable(eol::SimpleAnnotation.__init__)


def test_eol::simpleannotation_constructor_args():
    sig = inspect.signature(eol::SimpleAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_eol::executableannotation_is_not_abstract():
    assert not inspect.isabstract(eol::ExecutableAnnotation)


def test_eol::executableannotation_constructor_exists():
    assert callable(eol::ExecutableAnnotation.__init__)


def test_eol::executableannotation_constructor_args():
    sig = inspect.signature(eol::ExecutableAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_orderedcollectiontype_is_not_abstract():
    assert not inspect.isabstract(OrderedCollectionType)


def test_orderedcollectiontype_constructor_exists():
    assert callable(OrderedCollectionType.__init__)


def test_orderedcollectiontype_constructor_args():
    sig = inspect.signature(OrderedCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol::sequencetype_is_not_abstract():
    assert not inspect.isabstract(eol::SequenceType)


def test_eol::sequencetype_constructor_exists():
    assert callable(eol::SequenceType.__init__)


def test_eol::sequencetype_constructor_args():
    sig = inspect.signature(eol::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol::uniquecollectiontype_is_not_abstract():
    assert not inspect.isabstract(eol::UniqueCollectionType)


def test_eol::uniquecollectiontype_constructor_exists():
    assert callable(eol::UniqueCollectionType.__init__)


def test_eol::uniquecollectiontype_constructor_args():
    sig = inspect.signature(eol::UniqueCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol::orderedcollectiontype_is_not_abstract():
    assert not inspect.isabstract(eol::OrderedCollectionType)


def test_eol::orderedcollectiontype_constructor_exists():
    assert callable(eol::OrderedCollectionType.__init__)


def test_eol::orderedcollectiontype_constructor_args():
    sig = inspect.signature(eol::OrderedCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol::bagtype_is_not_abstract():
    assert not inspect.isabstract(eol::BagType)


def test_eol::bagtype_constructor_exists():
    assert callable(eol::BagType.__init__)


def test_eol::bagtype_constructor_args():
    sig = inspect.signature(eol::BagType.__init__)
    params = list(sig.parameters.keys())



def test_uniquecollectiontype_is_not_abstract():
    assert not inspect.isabstract(UniqueCollectionType)


def test_uniquecollectiontype_constructor_exists():
    assert callable(UniqueCollectionType.__init__)


def test_uniquecollectiontype_constructor_args():
    sig = inspect.signature(UniqueCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(eol::OrderedSetType)


def test_eol::orderedsettype_constructor_exists():
    assert callable(eol::OrderedSetType.__init__)


def test_eol::orderedsettype_constructor_args():
    sig = inspect.signature(eol::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_eol::settype_is_not_abstract():
    assert not inspect.isabstract(eol::SetType)


def test_eol::settype_constructor_exists():
    assert callable(eol::SetType.__init__)


def test_eol::settype_constructor_args():
    sig = inspect.signature(eol::SetType.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_eol::realtype_is_not_abstract():
    assert not inspect.isabstract(eol::RealType)


def test_eol::realtype_constructor_exists():
    assert callable(eol::RealType.__init__)


def test_eol::realtype_constructor_args():
    sig = inspect.signature(eol::RealType.__init__)
    params = list(sig.parameters.keys())



def test_eol::integertype_is_not_abstract():
    assert not inspect.isabstract(eol::IntegerType)


def test_eol::integertype_constructor_exists():
    assert callable(eol::IntegerType.__init__)


def test_eol::integertype_constructor_args():
    sig = inspect.signature(eol::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_eol::stringtype_is_not_abstract():
    assert not inspect.isabstract(eol::StringType)


def test_eol::stringtype_constructor_exists():
    assert callable(eol::StringType.__init__)


def test_eol::stringtype_constructor_args():
    sig = inspect.signature(eol::StringType.__init__)
    params = list(sig.parameters.keys())



def test_eol::booleantype_is_not_abstract():
    assert not inspect.isabstract(eol::BooleanType)


def test_eol::booleantype_constructor_exists():
    assert callable(eol::BooleanType.__init__)


def test_eol::booleantype_constructor_args():
    sig = inspect.signature(eol::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_eol::maptype_is_not_abstract():
    assert not inspect.isabstract(eol::MapType)


def test_eol::maptype_constructor_exists():
    assert callable(eol::MapType.__init__)


def test_eol::maptype_constructor_args():
    sig = inspect.signature(eol::MapType.__init__)
    params = list(sig.parameters.keys())



def test_eol::collectiontype_is_not_abstract():
    assert not inspect.isabstract(eol::CollectionType)


def test_eol::collectiontype_constructor_exists():
    assert callable(eol::CollectionType.__init__)


def test_eol::collectiontype_constructor_args():
    sig = inspect.signature(eol::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol::etype_is_not_abstract():
    assert not inspect.isabstract(eol::EType)


def test_eol::etype_constructor_exists():
    assert callable(eol::EType.__init__)


def test_eol::etype_constructor_args():
    sig = inspect.signature(eol::EType.__init__)
    params = list(sig.parameters.keys())



def test_eol::modelelementtype_is_not_abstract():
    assert not inspect.isabstract(eol::ModelElementType)


def test_eol::modelelementtype_constructor_exists():
    assert callable(eol::ModelElementType.__init__)


def test_eol::modelelementtype_constructor_args():
    sig = inspect.signature(eol::ModelElementType.__init__)
    params = list(sig.parameters.keys())
    assert "elementName" in params, "Missing parameter 'elementName'"
    assert "modelName" in params, "Missing parameter 'modelName'"

def test_eol::modelelementtype_has_elementName():
    assert hasattr(eol::ModelElementType, "elementName")
    descriptor = None
    for klass in eol::ModelElementType.__mro__:
        if "elementName" in klass.__dict__:
            descriptor = klass.__dict__["elementName"]
            break
    assert isinstance(descriptor, property)

def test_eol::modelelementtype_has_modelName():
    assert hasattr(eol::ModelElementType, "modelName")
    descriptor = None
    for klass in eol::ModelElementType.__mro__:
        if "modelName" in klass.__dict__:
            descriptor = klass.__dict__["modelName"]
            break
    assert isinstance(descriptor, property)



def test_eol::primitivetype_is_not_abstract():
    assert not inspect.isabstract(eol::PrimitiveType)


def test_eol::primitivetype_constructor_exists():
    assert callable(eol::PrimitiveType.__init__)


def test_eol::primitivetype_constructor_args():
    sig = inspect.signature(eol::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_eol::voidtype_is_not_abstract():
    assert not inspect.isabstract(eol::VoidType)


def test_eol::voidtype_constructor_exists():
    assert callable(eol::VoidType.__init__)


def test_eol::voidtype_constructor_args():
    sig = inspect.signature(eol::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_eol::nativetype_is_not_abstract():
    assert not inspect.isabstract(eol::NativeType)


def test_eol::nativetype_constructor_exists():
    assert callable(eol::NativeType.__init__)


def test_eol::nativetype_constructor_args():
    sig = inspect.signature(eol::NativeType.__init__)
    params = list(sig.parameters.keys())



def test_eol::pseudotype_is_not_abstract():
    assert not inspect.isabstract(eol::PseudoType)


def test_eol::pseudotype_constructor_exists():
    assert callable(eol::PseudoType.__init__)


def test_eol::pseudotype_constructor_args():
    sig = inspect.signature(eol::PseudoType.__init__)
    params = list(sig.parameters.keys())



def test_eol::modeltype_is_not_abstract():
    assert not inspect.isabstract(eol::ModelType)


def test_eol::modeltype_constructor_exists():
    assert callable(eol::ModelType.__init__)


def test_eol::modeltype_constructor_args():
    sig = inspect.signature(eol::ModelType.__init__)
    params = list(sig.parameters.keys())



def test_eol::anytype_is_not_abstract():
    assert not inspect.isabstract(eol::AnyType)


def test_eol::anytype_constructor_exists():
    assert callable(eol::AnyType.__init__)


def test_eol::anytype_constructor_args():
    sig = inspect.signature(eol::AnyType.__init__)
    params = list(sig.parameters.keys())
    assert "declared" in params, "Missing parameter 'declared'"

def test_eol::anytype_has_declared():
    assert hasattr(eol::AnyType, "declared")
    descriptor = None
    for klass in eol::AnyType.__mro__:
        if "declared" in klass.__dict__:
            descriptor = klass.__dict__["declared"]
            break
    assert isinstance(descriptor, property)



def test_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionExpression)


def test_collectionexpression_constructor_exists():
    assert callable(CollectionExpression.__init__)


def test_collectionexpression_constructor_args():
    sig = inspect.signature(CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::orderedsetexpression_is_not_abstract():
    assert not inspect.isabstract(eol::OrderedSetExpression)


def test_eol::orderedsetexpression_constructor_exists():
    assert callable(eol::OrderedSetExpression.__init__)


def test_eol::orderedsetexpression_constructor_args():
    sig = inspect.signature(eol::OrderedSetExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::sequenceexpression_is_not_abstract():
    assert not inspect.isabstract(eol::SequenceExpression)


def test_eol::sequenceexpression_constructor_exists():
    assert callable(eol::SequenceExpression.__init__)


def test_eol::sequenceexpression_constructor_args():
    sig = inspect.signature(eol::SequenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::bagexpression_is_not_abstract():
    assert not inspect.isabstract(eol::BagExpression)


def test_eol::bagexpression_constructor_exists():
    assert callable(eol::BagExpression.__init__)


def test_eol::bagexpression_constructor_args():
    sig = inspect.signature(eol::BagExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::setexpression_is_not_abstract():
    assert not inspect.isabstract(eol::SetExpression)


def test_eol::setexpression_constructor_exists():
    assert callable(eol::SetExpression.__init__)


def test_eol::setexpression_constructor_args():
    sig = inspect.signature(eol::SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::mapexpression_is_not_abstract():
    assert not inspect.isabstract(eol::MapExpression)


def test_eol::mapexpression_constructor_exists():
    assert callable(eol::MapExpression.__init__)


def test_eol::mapexpression_constructor_args():
    sig = inspect.signature(eol::MapExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::collectionexpression_is_not_abstract():
    assert not inspect.isabstract(eol::CollectionExpression)


def test_eol::collectionexpression_constructor_exists():
    assert callable(eol::CollectionExpression.__init__)


def test_eol::collectionexpression_constructor_args():
    sig = inspect.signature(eol::CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::nativeexpression_is_not_abstract():
    assert not inspect.isabstract(eol::NativeExpression)


def test_eol::nativeexpression_constructor_exists():
    assert callable(eol::NativeExpression.__init__)


def test_eol::nativeexpression_constructor_args():
    sig = inspect.signature(eol::NativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(eol::PrimitiveExpression)


def test_eol::primitiveexpression_constructor_exists():
    assert callable(eol::PrimitiveExpression.__init__)


def test_eol::primitiveexpression_constructor_args():
    sig = inspect.signature(eol::PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_switchcasestatement_is_not_abstract():
    assert not inspect.isabstract(SwitchCaseStatement)


def test_switchcasestatement_constructor_exists():
    assert callable(SwitchCaseStatement.__init__)


def test_switchcasestatement_constructor_args():
    sig = inspect.signature(SwitchCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::epackage_is_not_abstract():
    assert not inspect.isabstract(eol::EPackage)


def test_eol::epackage_constructor_exists():
    assert callable(eol::EPackage.__init__)


def test_eol::epackage_constructor_args():
    sig = inspect.signature(eol::EPackage.__init__)
    params = list(sig.parameters.keys())



def test_eol::switchcasedefaultstatement_is_not_abstract():
    assert not inspect.isabstract(eol::SwitchCaseDefaultStatement)


def test_eol::switchcasedefaultstatement_constructor_exists():
    assert callable(eol::SwitchCaseDefaultStatement.__init__)


def test_eol::switchcasedefaultstatement_constructor_args():
    sig = inspect.signature(eol::SwitchCaseDefaultStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::switchcaseexpressionstatement_is_not_abstract():
    assert not inspect.isabstract(eol::SwitchCaseExpressionStatement)


def test_eol::switchcaseexpressionstatement_constructor_exists():
    assert callable(eol::SwitchCaseExpressionStatement.__init__)


def test_eol::switchcaseexpressionstatement_constructor_args():
    sig = inspect.signature(eol::SwitchCaseExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_eol::transactionstatement_is_not_abstract():
    assert not inspect.isabstract(eol::TransactionStatement)


def test_eol::transactionstatement_constructor_exists():
    assert callable(eol::TransactionStatement.__init__)


def test_eol::transactionstatement_constructor_args():
    sig = inspect.signature(eol::TransactionStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::returnstatement_is_not_abstract():
    assert not inspect.isabstract(eol::ReturnStatement)


def test_eol::returnstatement_constructor_exists():
    assert callable(eol::ReturnStatement.__init__)


def test_eol::returnstatement_constructor_args():
    sig = inspect.signature(eol::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::breakallstatement_is_not_abstract():
    assert not inspect.isabstract(eol::BreakAllStatement)


def test_eol::breakallstatement_constructor_exists():
    assert callable(eol::BreakAllStatement.__init__)


def test_eol::breakallstatement_constructor_args():
    sig = inspect.signature(eol::BreakAllStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::switchstatement_is_not_abstract():
    assert not inspect.isabstract(eol::SwitchStatement)


def test_eol::switchstatement_constructor_exists():
    assert callable(eol::SwitchStatement.__init__)


def test_eol::switchstatement_constructor_args():
    sig = inspect.signature(eol::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::deletestatement_is_not_abstract():
    assert not inspect.isabstract(eol::DeleteStatement)


def test_eol::deletestatement_constructor_exists():
    assert callable(eol::DeleteStatement.__init__)


def test_eol::deletestatement_constructor_args():
    sig = inspect.signature(eol::DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::forstatement_is_not_abstract():
    assert not inspect.isabstract(eol::ForStatement)


def test_eol::forstatement_constructor_exists():
    assert callable(eol::ForStatement.__init__)


def test_eol::forstatement_constructor_args():
    sig = inspect.signature(eol::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::abortstatement_is_not_abstract():
    assert not inspect.isabstract(eol::AbortStatement)


def test_eol::abortstatement_constructor_exists():
    assert callable(eol::AbortStatement.__init__)


def test_eol::abortstatement_constructor_args():
    sig = inspect.signature(eol::AbortStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::throwstatement_is_not_abstract():
    assert not inspect.isabstract(eol::ThrowStatement)


def test_eol::throwstatement_constructor_exists():
    assert callable(eol::ThrowStatement.__init__)


def test_eol::throwstatement_constructor_args():
    sig = inspect.signature(eol::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::ifstatement_is_not_abstract():
    assert not inspect.isabstract(eol::IfStatement)


def test_eol::ifstatement_constructor_exists():
    assert callable(eol::IfStatement.__init__)


def test_eol::ifstatement_constructor_args():
    sig = inspect.signature(eol::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::modeldeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(eol::ModelDeclarationStatement)


def test_eol::modeldeclarationstatement_constructor_exists():
    assert callable(eol::ModelDeclarationStatement.__init__)


def test_eol::modeldeclarationstatement_constructor_args():
    sig = inspect.signature(eol::ModelDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::whilestatement_is_not_abstract():
    assert not inspect.isabstract(eol::WhileStatement)


def test_eol::whilestatement_constructor_exists():
    assert callable(eol::WhileStatement.__init__)


def test_eol::whilestatement_constructor_args():
    sig = inspect.signature(eol::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::switchcasestatement_is_not_abstract():
    assert not inspect.isabstract(eol::SwitchCaseStatement)


def test_eol::switchcasestatement_constructor_exists():
    assert callable(eol::SwitchCaseStatement.__init__)


def test_eol::switchcasestatement_constructor_args():
    sig = inspect.signature(eol::SwitchCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::breakstatement_is_not_abstract():
    assert not inspect.isabstract(eol::BreakStatement)


def test_eol::breakstatement_constructor_exists():
    assert callable(eol::BreakStatement.__init__)


def test_eol::breakstatement_constructor_args():
    sig = inspect.signature(eol::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::continuestatement_is_not_abstract():
    assert not inspect.isabstract(eol::ContinueStatement)


def test_eol::continuestatement_constructor_exists():
    assert callable(eol::ContinueStatement.__init__)


def test_eol::continuestatement_constructor_args():
    sig = inspect.signature(eol::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(eol::ExpressionStatement)


def test_eol::expressionstatement_constructor_exists():
    assert callable(eol::ExpressionStatement.__init__)


def test_eol::expressionstatement_constructor_args():
    sig = inspect.signature(eol::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOperatorExpression)


def test_binaryoperatorexpression_constructor_exists():
    assert callable(BinaryOperatorExpression.__init__)


def test_binaryoperatorexpression_constructor_args():
    sig = inspect.signature(BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::ComparisonOperatorExpression)


def test_eol::comparisonoperatorexpression_constructor_exists():
    assert callable(eol::ComparisonOperatorExpression.__init__)


def test_eol::comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(eol::ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::arithmeticoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::ArithmeticOperatorExpression)


def test_eol::arithmeticoperatorexpression_constructor_exists():
    assert callable(eol::ArithmeticOperatorExpression.__init__)


def test_eol::arithmeticoperatorexpression_constructor_args():
    sig = inspect.signature(eol::ArithmeticOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::logicaloperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::LogicalOperatorExpression)


def test_eol::logicaloperatorexpression_constructor_exists():
    assert callable(eol::LogicalOperatorExpression.__init__)


def test_eol::logicaloperatorexpression_constructor_args():
    sig = inspect.signature(eol::LogicalOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::operationargtype_is_not_abstract():
    assert not inspect.isabstract(eol::OperationArgType)


def test_eol::operationargtype_constructor_exists():
    assert callable(eol::OperationArgType.__init__)


def test_eol::operationargtype_constructor_args():
    sig = inspect.signature(eol::OperationArgType.__init__)
    params = list(sig.parameters.keys())



def test_eol::selfinnermosttype_is_not_abstract():
    assert not inspect.isabstract(eol::SelfInnermostType)


def test_eol::selfinnermosttype_constructor_exists():
    assert callable(eol::SelfInnermostType.__init__)


def test_eol::selfinnermosttype_constructor_args():
    sig = inspect.signature(eol::SelfInnermostType.__init__)
    params = list(sig.parameters.keys())



def test_eol::assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(eol::AssignmentStatement)


def test_eol::assignmentstatement_constructor_exists():
    assert callable(eol::AssignmentStatement.__init__)


def test_eol::assignmentstatement_constructor_args():
    sig = inspect.signature(eol::AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::formalparameterexpression_is_not_abstract():
    assert not inspect.isabstract(eol::FormalParameterExpression)


def test_eol::formalparameterexpression_constructor_exists():
    assert callable(eol::FormalParameterExpression.__init__)


def test_eol::formalparameterexpression_constructor_args():
    sig = inspect.signature(eol::FormalParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryOperatorExpression)


def test_unaryoperatorexpression_constructor_exists():
    assert callable(UnaryOperatorExpression.__init__)


def test_unaryoperatorexpression_constructor_args():
    sig = inspect.signature(UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::notoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::NotOperatorExpression)


def test_eol::notoperatorexpression_constructor_exists():
    assert callable(eol::NotOperatorExpression.__init__)


def test_eol::notoperatorexpression_constructor_args():
    sig = inspect.signature(eol::NotOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::negativeoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::NegativeOperatorExpression)


def test_eol::negativeoperatorexpression_constructor_exists():
    assert callable(eol::NegativeOperatorExpression.__init__)


def test_eol::negativeoperatorexpression_constructor_args():
    sig = inspect.signature(eol::NegativeOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::eobject_is_not_abstract():
    assert not inspect.isabstract(eol::EObject)


def test_eol::eobject_constructor_exists():
    assert callable(eol::EObject.__init__)


def test_eol::eobject_constructor_args():
    sig = inspect.signature(eol::EObject.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExpression)


def test_featurecallexpression_constructor_exists():
    assert callable(FeatureCallExpression.__init__)


def test_featurecallexpression_constructor_args():
    sig = inspect.signature(FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::propertycallexpression_is_not_abstract():
    assert not inspect.isabstract(eol::PropertyCallExpression)


def test_eol::propertycallexpression_constructor_exists():
    assert callable(eol::PropertyCallExpression.__init__)


def test_eol::propertycallexpression_constructor_args():
    sig = inspect.signature(eol::PropertyCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::folmethodcallexpression_is_not_abstract():
    assert not inspect.isabstract(eol::FOLMethodCallExpression)


def test_eol::folmethodcallexpression_constructor_exists():
    assert callable(eol::FOLMethodCallExpression.__init__)


def test_eol::folmethodcallexpression_constructor_args():
    sig = inspect.signature(eol::FOLMethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::methodcallexpression_is_not_abstract():
    assert not inspect.isabstract(eol::MethodCallExpression)


def test_eol::methodcallexpression_constructor_exists():
    assert callable(eol::MethodCallExpression.__init__)


def test_eol::methodcallexpression_constructor_args():
    sig = inspect.signature(eol::MethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(ComparisonOperatorExpression)


def test_comparisonoperatorexpression_constructor_exists():
    assert callable(ComparisonOperatorExpression.__init__)


def test_comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::notequalsoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::NotEqualsOperatorExpression)


def test_eol::notequalsoperatorexpression_constructor_exists():
    assert callable(eol::NotEqualsOperatorExpression.__init__)


def test_eol::notequalsoperatorexpression_constructor_args():
    sig = inspect.signature(eol::NotEqualsOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::lessthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::LessThanOrEqualToOperatorExpression)


def test_eol::lessthanorequaltooperatorexpression_constructor_exists():
    assert callable(eol::LessThanOrEqualToOperatorExpression.__init__)


def test_eol::lessthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(eol::LessThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::greaterthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::GreaterThanOrEqualToOperatorExpression)


def test_eol::greaterthanorequaltooperatorexpression_constructor_exists():
    assert callable(eol::GreaterThanOrEqualToOperatorExpression.__init__)


def test_eol::greaterthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(eol::GreaterThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::greaterthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::GreaterThanOperatorExpression)


def test_eol::greaterthanoperatorexpression_constructor_exists():
    assert callable(eol::GreaterThanOperatorExpression.__init__)


def test_eol::greaterthanoperatorexpression_constructor_args():
    sig = inspect.signature(eol::GreaterThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::lessthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::LessThanOperatorExpression)


def test_eol::lessthanoperatorexpression_constructor_exists():
    assert callable(eol::LessThanOperatorExpression.__init__)


def test_eol::lessthanoperatorexpression_constructor_args():
    sig = inspect.signature(eol::LessThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::equalsoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::EqualsOperatorExpression)


def test_eol::equalsoperatorexpression_constructor_exists():
    assert callable(eol::EqualsOperatorExpression.__init__)


def test_eol::equalsoperatorexpression_constructor_args():
    sig = inspect.signature(eol::EqualsOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::modelexpression_is_not_abstract():
    assert not inspect.isabstract(eol::ModelExpression)


def test_eol::modelexpression_constructor_exists():
    assert callable(eol::ModelExpression.__init__)


def test_eol::modelexpression_constructor_args():
    sig = inspect.signature(eol::ModelExpression.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticOperatorExpression)


def test_arithmeticoperatorexpression_constructor_exists():
    assert callable(ArithmeticOperatorExpression.__init__)


def test_arithmeticoperatorexpression_constructor_args():
    sig = inspect.signature(ArithmeticOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::plusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::PlusOperatorExpression)


def test_eol::plusoperatorexpression_constructor_exists():
    assert callable(eol::PlusOperatorExpression.__init__)


def test_eol::plusoperatorexpression_constructor_args():
    sig = inspect.signature(eol::PlusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::minusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::MinusOperatorExpression)


def test_eol::minusoperatorexpression_constructor_exists():
    assert callable(eol::MinusOperatorExpression.__init__)


def test_eol::minusoperatorexpression_constructor_args():
    sig = inspect.signature(eol::MinusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::multiplyoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::MultiplyOperatorExpression)


def test_eol::multiplyoperatorexpression_constructor_exists():
    assert callable(eol::MultiplyOperatorExpression.__init__)


def test_eol::multiplyoperatorexpression_constructor_args():
    sig = inspect.signature(eol::MultiplyOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::divideoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::DivideOperatorExpression)


def test_eol::divideoperatorexpression_constructor_exists():
    assert callable(eol::DivideOperatorExpression.__init__)


def test_eol::divideoperatorexpression_constructor_args():
    sig = inspect.signature(eol::DivideOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExpression)


def test_primitiveexpression_constructor_exists():
    assert callable(PrimitiveExpression.__init__)


def test_primitiveexpression_constructor_args():
    sig = inspect.signature(PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::realexpression_is_not_abstract():
    assert not inspect.isabstract(eol::RealExpression)


def test_eol::realexpression_constructor_exists():
    assert callable(eol::RealExpression.__init__)


def test_eol::realexpression_constructor_args():
    sig = inspect.signature(eol::RealExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_eol::realexpression_has_val():
    assert hasattr(eol::RealExpression, "val")
    descriptor = None
    for klass in eol::RealExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_eol::integerexpression_is_not_abstract():
    assert not inspect.isabstract(eol::IntegerExpression)


def test_eol::integerexpression_constructor_exists():
    assert callable(eol::IntegerExpression.__init__)


def test_eol::integerexpression_constructor_args():
    sig = inspect.signature(eol::IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_eol::integerexpression_has_val():
    assert hasattr(eol::IntegerExpression, "val")
    descriptor = None
    for klass in eol::IntegerExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_eol::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(eol::BooleanExpression)


def test_eol::booleanexpression_constructor_exists():
    assert callable(eol::BooleanExpression.__init__)


def test_eol::booleanexpression_constructor_args():
    sig = inspect.signature(eol::BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_eol::booleanexpression_has_val():
    assert hasattr(eol::BooleanExpression, "val")
    descriptor = None
    for klass in eol::BooleanExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_logicaloperatorexpression_is_not_abstract():
    assert not inspect.isabstract(LogicalOperatorExpression)


def test_logicaloperatorexpression_constructor_exists():
    assert callable(LogicalOperatorExpression.__init__)


def test_logicaloperatorexpression_constructor_args():
    sig = inspect.signature(LogicalOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::impliesoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::ImpliesOperatorExpression)


def test_eol::impliesoperatorexpression_constructor_exists():
    assert callable(eol::ImpliesOperatorExpression.__init__)


def test_eol::impliesoperatorexpression_constructor_args():
    sig = inspect.signature(eol::ImpliesOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::oroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::OrOperatorExpression)


def test_eol::oroperatorexpression_constructor_exists():
    assert callable(eol::OrOperatorExpression.__init__)


def test_eol::oroperatorexpression_constructor_args():
    sig = inspect.signature(eol::OrOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::xoroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::XorOperatorExpression)


def test_eol::xoroperatorexpression_constructor_exists():
    assert callable(eol::XorOperatorExpression.__init__)


def test_eol::xoroperatorexpression_constructor_args():
    sig = inspect.signature(eol::XorOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::andoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::AndOperatorExpression)


def test_eol::andoperatorexpression_constructor_exists():
    assert callable(eol::AndOperatorExpression.__init__)


def test_eol::andoperatorexpression_constructor_args():
    sig = inspect.signature(eol::AndOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(OperatorExpression)


def test_operatorexpression_constructor_exists():
    assert callable(OperatorExpression.__init__)


def test_operatorexpression_constructor_args():
    sig = inspect.signature(OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::UnaryOperatorExpression)


def test_eol::unaryoperatorexpression_constructor_exists():
    assert callable(eol::UnaryOperatorExpression.__init__)


def test_eol::unaryoperatorexpression_constructor_args():
    sig = inspect.signature(eol::UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::BinaryOperatorExpression)


def test_eol::binaryoperatorexpression_constructor_exists():
    assert callable(eol::BinaryOperatorExpression.__init__)


def test_eol::binaryoperatorexpression_constructor_args():
    sig = inspect.signature(eol::BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_eol::enumerationliteralexpression_is_not_abstract():
    assert not inspect.isabstract(eol::EnumerationLiteralExpression)


def test_eol::enumerationliteralexpression_constructor_exists():
    assert callable(eol::EnumerationLiteralExpression.__init__)


def test_eol::enumerationliteralexpression_constructor_args():
    sig = inspect.signature(eol::EnumerationLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::nameexpression_is_not_abstract():
    assert not inspect.isabstract(eol::NameExpression)


def test_eol::nameexpression_constructor_exists():
    assert callable(eol::NameExpression.__init__)


def test_eol::nameexpression_constructor_args():
    sig = inspect.signature(eol::NameExpression.__init__)
    params = list(sig.parameters.keys())
    assert "resolvedContent" in params, "Missing parameter 'resolvedContent'"
    assert "name" in params, "Missing parameter 'name'"

def test_eol::nameexpression_has_resolvedContent():
    assert hasattr(eol::NameExpression, "resolvedContent")
    descriptor = None
    for klass in eol::NameExpression.__mro__:
        if "resolvedContent" in klass.__dict__:
            descriptor = klass.__dict__["resolvedContent"]
            break
    assert isinstance(descriptor, property)

def test_eol::nameexpression_has_name():
    assert hasattr(eol::NameExpression, "name")
    descriptor = None
    for klass in eol::NameExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eol::literalexpression_is_not_abstract():
    assert not inspect.isabstract(eol::LiteralExpression)


def test_eol::literalexpression_constructor_exists():
    assert callable(eol::LiteralExpression.__init__)


def test_eol::literalexpression_constructor_args():
    sig = inspect.signature(eol::LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::modeldeclarationparameter_is_not_abstract():
    assert not inspect.isabstract(eol::ModelDeclarationParameter)


def test_eol::modeldeclarationparameter_constructor_exists():
    assert callable(eol::ModelDeclarationParameter.__init__)


def test_eol::modeldeclarationparameter_constructor_args():
    sig = inspect.signature(eol::ModelDeclarationParameter.__init__)
    params = list(sig.parameters.keys())



def test_eol::featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(eol::FeatureCallExpression)


def test_eol::featurecallexpression_constructor_exists():
    assert callable(eol::FeatureCallExpression.__init__)


def test_eol::featurecallexpression_constructor_args():
    sig = inspect.signature(eol::FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::collectioninitvalue_is_not_abstract():
    assert not inspect.isabstract(eol::CollectionInitValue)


def test_eol::collectioninitvalue_constructor_exists():
    assert callable(eol::CollectionInitValue.__init__)


def test_eol::collectioninitvalue_constructor_args():
    sig = inspect.signature(eol::CollectionInitValue.__init__)
    params = list(sig.parameters.keys())



def test_eol::keyvalue_is_not_abstract():
    assert not inspect.isabstract(eol::KeyValue)


def test_eol::keyvalue_constructor_exists():
    assert callable(eol::KeyValue.__init__)


def test_eol::keyvalue_constructor_args():
    sig = inspect.signature(eol::KeyValue.__init__)
    params = list(sig.parameters.keys())



def test_eol::variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(eol::VariableDeclarationExpression)


def test_eol::variabledeclarationexpression_constructor_exists():
    assert callable(eol::VariableDeclarationExpression.__init__)


def test_eol::variabledeclarationexpression_constructor_args():
    sig = inspect.signature(eol::VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "definitionPoints" in params, "Missing parameter 'definitionPoints'"

def test_eol::variabledeclarationexpression_has_definitionPoints():
    assert hasattr(eol::VariableDeclarationExpression, "definitionPoints")
    descriptor = None
    for klass in eol::VariableDeclarationExpression.__mro__:
        if "definitionPoints" in klass.__dict__:
            descriptor = klass.__dict__["definitionPoints"]
            break
    assert isinstance(descriptor, property)



def test_eol::newexpression_is_not_abstract():
    assert not inspect.isabstract(eol::NewExpression)


def test_eol::newexpression_constructor_exists():
    assert callable(eol::NewExpression.__init__)


def test_eol::newexpression_constructor_args():
    sig = inspect.signature(eol::NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::operatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::OperatorExpression)


def test_eol::operatorexpression_constructor_exists():
    assert callable(eol::OperatorExpression.__init__)


def test_eol::operatorexpression_constructor_args():
    sig = inspect.signature(eol::OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::stringexpression_is_not_abstract():
    assert not inspect.isabstract(eol::StringExpression)


def test_eol::stringexpression_constructor_exists():
    assert callable(eol::StringExpression.__init__)


def test_eol::stringexpression_constructor_args():
    sig = inspect.signature(eol::StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_eol::stringexpression_has_val():
    assert hasattr(eol::StringExpression, "val")
    descriptor = None
    for klass in eol::StringExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_eolelement_is_not_abstract():
    assert not inspect.isabstract(EolElement)


def test_eolelement_constructor_exists():
    assert callable(EolElement.__init__)


def test_eolelement_constructor_args():
    sig = inspect.signature(EolElement.__init__)
    params = list(sig.parameters.keys())



def test_eol::eollibrarymodule_is_not_abstract():
    assert not inspect.isabstract(eol::EolLibraryModule)


def test_eol::eollibrarymodule_constructor_exists():
    assert callable(eol::EolLibraryModule.__init__)


def test_eol::eollibrarymodule_constructor_args():
    sig = inspect.signature(eol::EolLibraryModule.__init__)
    params = list(sig.parameters.keys())



def test_eol::statement_is_not_abstract():
    assert not inspect.isabstract(eol::Statement)


def test_eol::statement_constructor_exists():
    assert callable(eol::Statement.__init__)


def test_eol::statement_constructor_args():
    sig = inspect.signature(eol::Statement.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression_is_not_abstract():
    assert not inspect.isabstract(eol::Expression)


def test_eol::expression_constructor_exists():
    assert callable(eol::Expression.__init__)


def test_eol::expression_constructor_args():
    sig = inspect.signature(eol::Expression.__init__)
    params = list(sig.parameters.keys())



def test_eol::operationdefinition_is_not_abstract():
    assert not inspect.isabstract(eol::OperationDefinition)


def test_eol::operationdefinition_constructor_exists():
    assert callable(eol::OperationDefinition.__init__)


def test_eol::operationdefinition_constructor_args():
    sig = inspect.signature(eol::OperationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_eol::annotationblock_is_not_abstract():
    assert not inspect.isabstract(eol::AnnotationBlock)


def test_eol::annotationblock_constructor_exists():
    assert callable(eol::AnnotationBlock.__init__)


def test_eol::annotationblock_constructor_args():
    sig = inspect.signature(eol::AnnotationBlock.__init__)
    params = list(sig.parameters.keys())



def test_eol::expressionorstatementblock_is_not_abstract():
    assert not inspect.isabstract(eol::ExpressionOrStatementBlock)


def test_eol::expressionorstatementblock_constructor_exists():
    assert callable(eol::ExpressionOrStatementBlock.__init__)


def test_eol::expressionorstatementblock_constructor_args():
    sig = inspect.signature(eol::ExpressionOrStatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_eol::annotation_is_not_abstract():
    assert not inspect.isabstract(eol::Annotation)


def test_eol::annotation_constructor_exists():
    assert callable(eol::Annotation.__init__)


def test_eol::annotation_constructor_args():
    sig = inspect.signature(eol::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_eol::type_is_not_abstract():
    assert not inspect.isabstract(eol::Type)


def test_eol::type_constructor_exists():
    assert callable(eol::Type.__init__)


def test_eol::type_constructor_args():
    sig = inspect.signature(eol::Type.__init__)
    params = list(sig.parameters.keys())



def test_eol::import_is_not_abstract():
    assert not inspect.isabstract(eol::Import)


def test_eol::import_constructor_exists():
    assert callable(eol::Import.__init__)


def test_eol::import_constructor_args():
    sig = inspect.signature(eol::Import.__init__)
    params = list(sig.parameters.keys())



def test_eol::block_is_not_abstract():
    assert not inspect.isabstract(eol::Block)


def test_eol::block_constructor_exists():
    assert callable(eol::Block.__init__)


def test_eol::block_constructor_args():
    sig = inspect.signature(eol::Block.__init__)
    params = list(sig.parameters.keys())



def test_eollibrarymodule_is_not_abstract():
    assert not inspect.isabstract(EolLibraryModule)


def test_eollibrarymodule_constructor_exists():
    assert callable(EolLibraryModule.__init__)


def test_eollibrarymodule_constructor_args():
    sig = inspect.signature(EolLibraryModule.__init__)
    params = list(sig.parameters.keys())



def test_eol::eolprogram_is_not_abstract():
    assert not inspect.isabstract(eol::EolProgram)


def test_eol::eolprogram_constructor_exists():
    assert callable(eol::EolProgram.__init__)


def test_eol::eolprogram_constructor_args():
    sig = inspect.signature(eol::EolProgram.__init__)
    params = list(sig.parameters.keys())



def test_eol::textposition_is_not_abstract():
    assert not inspect.isabstract(eol::TextPosition)


def test_eol::textposition_constructor_exists():
    assert callable(eol::TextPosition.__init__)


def test_eol::textposition_constructor_args():
    sig = inspect.signature(eol::TextPosition.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"
    assert "line" in params, "Missing parameter 'line'"

def test_eol::textposition_has_column():
    assert hasattr(eol::TextPosition, "column")
    descriptor = None
    for klass in eol::TextPosition.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)

def test_eol::textposition_has_line():
    assert hasattr(eol::TextPosition, "line")
    descriptor = None
    for klass in eol::TextPosition.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)



def test_eol::textregion_is_not_abstract():
    assert not inspect.isabstract(eol::TextRegion)


def test_eol::textregion_constructor_exists():
    assert callable(eol::TextRegion.__init__)


def test_eol::textregion_constructor_args():
    sig = inspect.signature(eol::TextRegion.__init__)
    params = list(sig.parameters.keys())



def test_eol::eolelement_is_not_abstract():
    assert not inspect.isabstract(eol::EolElement)


def test_eol::eolelement_constructor_exists():
    assert callable(eol::EolElement.__init__)


def test_eol::eolelement_constructor_args():
    sig = inspect.signature(eol::EolElement.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"
    assert "line" in params, "Missing parameter 'line'"
    assert "column" in params, "Missing parameter 'column'"

def test_eol::eolelement_has_uri():
    assert hasattr(eol::EolElement, "uri")
    descriptor = None
    for klass in eol::EolElement.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)

def test_eol::eolelement_has_line():
    assert hasattr(eol::EolElement, "line")
    descriptor = None
    for klass in eol::EolElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_eol::eolelement_has_column():
    assert hasattr(eol::EolElement, "column")
    descriptor = None
    for klass in eol::EolElement.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
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
PseudoType_strategy = st.builds(
    PseudoType,
)
eol::SelfContentType_strategy = st.builds(
    eol::SelfContentType,
)
eol::SelfType_strategy = st.builds(
    eol::SelfType,
)
AssignmentStatement_strategy = st.builds(
    AssignmentStatement,
)
eol::SpecialAssignmentStatement_strategy = st.builds(
    eol::SpecialAssignmentStatement,
)
CollectionInitValue_strategy = st.builds(
    CollectionInitValue,
)
eol::ExpRange_strategy = st.builds(
    eol::ExpRange,
)
eol::ExprList_strategy = st.builds(
    eol::ExprList,
)
VariableDeclarationExpression_strategy = st.builds(
    VariableDeclarationExpression,
)
eol::EClassifier_strategy = st.builds(
    eol::EClassifier,
)
NameExpression_strategy = st.builds(
    NameExpression,
)
eol::SpecialNameExpression_strategy = st.builds(
    eol::SpecialNameExpression,
)
Annotation_strategy = st.builds(
    Annotation,
)
eol::SimpleAnnotation_strategy = st.builds(
    eol::SimpleAnnotation,
)
eol::ExecutableAnnotation_strategy = st.builds(
    eol::ExecutableAnnotation,
)
OrderedCollectionType_strategy = st.builds(
    OrderedCollectionType,
)
eol::SequenceType_strategy = st.builds(
    eol::SequenceType,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
eol::UniqueCollectionType_strategy = st.builds(
    eol::UniqueCollectionType,
)
eol::OrderedCollectionType_strategy = st.builds(
    eol::OrderedCollectionType,
)
eol::BagType_strategy = st.builds(
    eol::BagType,
)
UniqueCollectionType_strategy = st.builds(
    UniqueCollectionType,
)
eol::OrderedSetType_strategy = st.builds(
    eol::OrderedSetType,
)
eol::SetType_strategy = st.builds(
    eol::SetType,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
eol::RealType_strategy = st.builds(
    eol::RealType,
)
eol::IntegerType_strategy = st.builds(
    eol::IntegerType,
)
eol::StringType_strategy = st.builds(
    eol::StringType,
)
eol::BooleanType_strategy = st.builds(
    eol::BooleanType,
)
Type_strategy = st.builds(
    Type,
)
eol::MapType_strategy = st.builds(
    eol::MapType,
)
eol::CollectionType_strategy = st.builds(
    eol::CollectionType,
)
eol::EType_strategy = st.builds(
    eol::EType,
)
eol::ModelElementType_strategy = st.builds(
    eol::ModelElementType,
    elementName=
        safe_text,
    modelName=
        safe_text
)
eol::PrimitiveType_strategy = st.builds(
    eol::PrimitiveType,
)
eol::VoidType_strategy = st.builds(
    eol::VoidType,
)
eol::NativeType_strategy = st.builds(
    eol::NativeType,
)
eol::PseudoType_strategy = st.builds(
    eol::PseudoType,
)
eol::ModelType_strategy = st.builds(
    eol::ModelType,
)
eol::AnyType_strategy = st.builds(
    eol::AnyType,
    declared=
        st.booleans()
)
CollectionExpression_strategy = st.builds(
    CollectionExpression,
)
eol::OrderedSetExpression_strategy = st.builds(
    eol::OrderedSetExpression,
)
eol::SequenceExpression_strategy = st.builds(
    eol::SequenceExpression,
)
eol::BagExpression_strategy = st.builds(
    eol::BagExpression,
)
eol::SetExpression_strategy = st.builds(
    eol::SetExpression,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
eol::MapExpression_strategy = st.builds(
    eol::MapExpression,
)
eol::CollectionExpression_strategy = st.builds(
    eol::CollectionExpression,
)
eol::NativeExpression_strategy = st.builds(
    eol::NativeExpression,
)
eol::PrimitiveExpression_strategy = st.builds(
    eol::PrimitiveExpression,
)
SwitchCaseStatement_strategy = st.builds(
    SwitchCaseStatement,
)
eol::EPackage_strategy = st.builds(
    eol::EPackage,
)
eol::SwitchCaseDefaultStatement_strategy = st.builds(
    eol::SwitchCaseDefaultStatement,
)
eol::SwitchCaseExpressionStatement_strategy = st.builds(
    eol::SwitchCaseExpressionStatement,
)
Statement_strategy = st.builds(
    Statement,
)
eol::TransactionStatement_strategy = st.builds(
    eol::TransactionStatement,
)
eol::ReturnStatement_strategy = st.builds(
    eol::ReturnStatement,
)
eol::BreakAllStatement_strategy = st.builds(
    eol::BreakAllStatement,
)
eol::SwitchStatement_strategy = st.builds(
    eol::SwitchStatement,
)
eol::DeleteStatement_strategy = st.builds(
    eol::DeleteStatement,
)
eol::ForStatement_strategy = st.builds(
    eol::ForStatement,
)
eol::AbortStatement_strategy = st.builds(
    eol::AbortStatement,
)
eol::ThrowStatement_strategy = st.builds(
    eol::ThrowStatement,
)
eol::IfStatement_strategy = st.builds(
    eol::IfStatement,
)
eol::ModelDeclarationStatement_strategy = st.builds(
    eol::ModelDeclarationStatement,
)
eol::WhileStatement_strategy = st.builds(
    eol::WhileStatement,
)
eol::SwitchCaseStatement_strategy = st.builds(
    eol::SwitchCaseStatement,
)
eol::BreakStatement_strategy = st.builds(
    eol::BreakStatement,
)
eol::ContinueStatement_strategy = st.builds(
    eol::ContinueStatement,
)
eol::ExpressionStatement_strategy = st.builds(
    eol::ExpressionStatement,
)
BinaryOperatorExpression_strategy = st.builds(
    BinaryOperatorExpression,
)
eol::ComparisonOperatorExpression_strategy = st.builds(
    eol::ComparisonOperatorExpression,
)
eol::ArithmeticOperatorExpression_strategy = st.builds(
    eol::ArithmeticOperatorExpression,
)
eol::LogicalOperatorExpression_strategy = st.builds(
    eol::LogicalOperatorExpression,
)
eol::OperationArgType_strategy = st.builds(
    eol::OperationArgType,
)
eol::SelfInnermostType_strategy = st.builds(
    eol::SelfInnermostType,
)
eol::AssignmentStatement_strategy = st.builds(
    eol::AssignmentStatement,
)
eol::FormalParameterExpression_strategy = st.builds(
    eol::FormalParameterExpression,
)
UnaryOperatorExpression_strategy = st.builds(
    UnaryOperatorExpression,
)
eol::NotOperatorExpression_strategy = st.builds(
    eol::NotOperatorExpression,
)
eol::NegativeOperatorExpression_strategy = st.builds(
    eol::NegativeOperatorExpression,
)
eol::EObject_strategy = st.builds(
    eol::EObject,
)
FeatureCallExpression_strategy = st.builds(
    FeatureCallExpression,
)
eol::PropertyCallExpression_strategy = st.builds(
    eol::PropertyCallExpression,
)
eol::FOLMethodCallExpression_strategy = st.builds(
    eol::FOLMethodCallExpression,
)
eol::MethodCallExpression_strategy = st.builds(
    eol::MethodCallExpression,
)
ComparisonOperatorExpression_strategy = st.builds(
    ComparisonOperatorExpression,
)
eol::NotEqualsOperatorExpression_strategy = st.builds(
    eol::NotEqualsOperatorExpression,
)
eol::LessThanOrEqualToOperatorExpression_strategy = st.builds(
    eol::LessThanOrEqualToOperatorExpression,
)
eol::GreaterThanOrEqualToOperatorExpression_strategy = st.builds(
    eol::GreaterThanOrEqualToOperatorExpression,
)
eol::GreaterThanOperatorExpression_strategy = st.builds(
    eol::GreaterThanOperatorExpression,
)
eol::LessThanOperatorExpression_strategy = st.builds(
    eol::LessThanOperatorExpression,
)
eol::EqualsOperatorExpression_strategy = st.builds(
    eol::EqualsOperatorExpression,
)
eol::ModelExpression_strategy = st.builds(
    eol::ModelExpression,
)
ArithmeticOperatorExpression_strategy = st.builds(
    ArithmeticOperatorExpression,
)
eol::PlusOperatorExpression_strategy = st.builds(
    eol::PlusOperatorExpression,
)
eol::MinusOperatorExpression_strategy = st.builds(
    eol::MinusOperatorExpression,
)
eol::MultiplyOperatorExpression_strategy = st.builds(
    eol::MultiplyOperatorExpression,
)
eol::DivideOperatorExpression_strategy = st.builds(
    eol::DivideOperatorExpression,
)
PrimitiveExpression_strategy = st.builds(
    PrimitiveExpression,
)
eol::RealExpression_strategy = st.builds(
    eol::RealExpression,
    val=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eol::IntegerExpression_strategy = st.builds(
    eol::IntegerExpression,
    val=
        st.integers()
)
eol::BooleanExpression_strategy = st.builds(
    eol::BooleanExpression,
    val=
        st.booleans()
)
LogicalOperatorExpression_strategy = st.builds(
    LogicalOperatorExpression,
)
eol::ImpliesOperatorExpression_strategy = st.builds(
    eol::ImpliesOperatorExpression,
)
eol::OrOperatorExpression_strategy = st.builds(
    eol::OrOperatorExpression,
)
eol::XorOperatorExpression_strategy = st.builds(
    eol::XorOperatorExpression,
)
eol::AndOperatorExpression_strategy = st.builds(
    eol::AndOperatorExpression,
)
OperatorExpression_strategy = st.builds(
    OperatorExpression,
)
eol::UnaryOperatorExpression_strategy = st.builds(
    eol::UnaryOperatorExpression,
)
eol::BinaryOperatorExpression_strategy = st.builds(
    eol::BinaryOperatorExpression,
)
Expression_strategy = st.builds(
    Expression,
)
eol::EnumerationLiteralExpression_strategy = st.builds(
    eol::EnumerationLiteralExpression,
)
eol::NameExpression_strategy = st.builds(
    eol::NameExpression,
    resolvedContent=
        safe_text,
    name=
        safe_text
)
eol::LiteralExpression_strategy = st.builds(
    eol::LiteralExpression,
)
eol::ModelDeclarationParameter_strategy = st.builds(
    eol::ModelDeclarationParameter,
)
eol::FeatureCallExpression_strategy = st.builds(
    eol::FeatureCallExpression,
)
eol::CollectionInitValue_strategy = st.builds(
    eol::CollectionInitValue,
)
eol::KeyValue_strategy = st.builds(
    eol::KeyValue,
)
eol::VariableDeclarationExpression_strategy = st.builds(
    eol::VariableDeclarationExpression,
    definitionPoints=
        safe_text
)
eol::NewExpression_strategy = st.builds(
    eol::NewExpression,
)
eol::OperatorExpression_strategy = st.builds(
    eol::OperatorExpression,
)
eol::StringExpression_strategy = st.builds(
    eol::StringExpression,
    val=
        safe_text
)
EolElement_strategy = st.builds(
    EolElement,
)
eol::EolLibraryModule_strategy = st.builds(
    eol::EolLibraryModule,
)
eol::Statement_strategy = st.builds(
    eol::Statement,
)
eol::Expression_strategy = st.builds(
    eol::Expression,
)
eol::OperationDefinition_strategy = st.builds(
    eol::OperationDefinition,
)
eol::AnnotationBlock_strategy = st.builds(
    eol::AnnotationBlock,
)
eol::ExpressionOrStatementBlock_strategy = st.builds(
    eol::ExpressionOrStatementBlock,
)
eol::Annotation_strategy = st.builds(
    eol::Annotation,
)
eol::Type_strategy = st.builds(
    eol::Type,
)
eol::Import_strategy = st.builds(
    eol::Import,
)
eol::Block_strategy = st.builds(
    eol::Block,
)
EolLibraryModule_strategy = st.builds(
    EolLibraryModule,
)
eol::EolProgram_strategy = st.builds(
    eol::EolProgram,
)
eol::TextPosition_strategy = st.builds(
    eol::TextPosition,
    column=
        st.integers(),
    line=
        st.integers()
)
eol::TextRegion_strategy = st.builds(
    eol::TextRegion,
)
eol::EolElement_strategy = st.builds(
    eol::EolElement,
    uri=
        safe_text,
    line=
        st.integers(),
    column=
        st.integers()
)

@given(instance=PseudoType_strategy)
@settings(max_examples=50)
def test_pseudotype_instantiation(instance):
    assert isinstance(instance, PseudoType)

@given(instance=eol::SelfContentType_strategy)
@settings(max_examples=50)
def test_eol::selfcontenttype_instantiation(instance):
    assert isinstance(instance, eol::SelfContentType)

@given(instance=eol::SelfType_strategy)
@settings(max_examples=50)
def test_eol::selftype_instantiation(instance):
    assert isinstance(instance, eol::SelfType)

@given(instance=AssignmentStatement_strategy)
@settings(max_examples=50)
def test_assignmentstatement_instantiation(instance):
    assert isinstance(instance, AssignmentStatement)

@given(instance=eol::SpecialAssignmentStatement_strategy)
@settings(max_examples=50)
def test_eol::specialassignmentstatement_instantiation(instance):
    assert isinstance(instance, eol::SpecialAssignmentStatement)

@given(instance=CollectionInitValue_strategy)
@settings(max_examples=50)
def test_collectioninitvalue_instantiation(instance):
    assert isinstance(instance, CollectionInitValue)

@given(instance=eol::ExpRange_strategy)
@settings(max_examples=50)
def test_eol::exprange_instantiation(instance):
    assert isinstance(instance, eol::ExpRange)

@given(instance=eol::ExprList_strategy)
@settings(max_examples=50)
def test_eol::exprlist_instantiation(instance):
    assert isinstance(instance, eol::ExprList)

@given(instance=VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, VariableDeclarationExpression)

@given(instance=eol::EClassifier_strategy)
@settings(max_examples=50)
def test_eol::eclassifier_instantiation(instance):
    assert isinstance(instance, eol::EClassifier)

@given(instance=NameExpression_strategy)
@settings(max_examples=50)
def test_nameexpression_instantiation(instance):
    assert isinstance(instance, NameExpression)

@given(instance=eol::SpecialNameExpression_strategy)
@settings(max_examples=50)
def test_eol::specialnameexpression_instantiation(instance):
    assert isinstance(instance, eol::SpecialNameExpression)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=eol::SimpleAnnotation_strategy)
@settings(max_examples=50)
def test_eol::simpleannotation_instantiation(instance):
    assert isinstance(instance, eol::SimpleAnnotation)

@given(instance=eol::ExecutableAnnotation_strategy)
@settings(max_examples=50)
def test_eol::executableannotation_instantiation(instance):
    assert isinstance(instance, eol::ExecutableAnnotation)

@given(instance=OrderedCollectionType_strategy)
@settings(max_examples=50)
def test_orderedcollectiontype_instantiation(instance):
    assert isinstance(instance, OrderedCollectionType)

@given(instance=eol::SequenceType_strategy)
@settings(max_examples=50)
def test_eol::sequencetype_instantiation(instance):
    assert isinstance(instance, eol::SequenceType)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=eol::UniqueCollectionType_strategy)
@settings(max_examples=50)
def test_eol::uniquecollectiontype_instantiation(instance):
    assert isinstance(instance, eol::UniqueCollectionType)

@given(instance=eol::OrderedCollectionType_strategy)
@settings(max_examples=50)
def test_eol::orderedcollectiontype_instantiation(instance):
    assert isinstance(instance, eol::OrderedCollectionType)

@given(instance=eol::BagType_strategy)
@settings(max_examples=50)
def test_eol::bagtype_instantiation(instance):
    assert isinstance(instance, eol::BagType)

@given(instance=UniqueCollectionType_strategy)
@settings(max_examples=50)
def test_uniquecollectiontype_instantiation(instance):
    assert isinstance(instance, UniqueCollectionType)

@given(instance=eol::OrderedSetType_strategy)
@settings(max_examples=50)
def test_eol::orderedsettype_instantiation(instance):
    assert isinstance(instance, eol::OrderedSetType)

@given(instance=eol::SetType_strategy)
@settings(max_examples=50)
def test_eol::settype_instantiation(instance):
    assert isinstance(instance, eol::SetType)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=eol::RealType_strategy)
@settings(max_examples=50)
def test_eol::realtype_instantiation(instance):
    assert isinstance(instance, eol::RealType)

@given(instance=eol::IntegerType_strategy)
@settings(max_examples=50)
def test_eol::integertype_instantiation(instance):
    assert isinstance(instance, eol::IntegerType)

@given(instance=eol::StringType_strategy)
@settings(max_examples=50)
def test_eol::stringtype_instantiation(instance):
    assert isinstance(instance, eol::StringType)

@given(instance=eol::BooleanType_strategy)
@settings(max_examples=50)
def test_eol::booleantype_instantiation(instance):
    assert isinstance(instance, eol::BooleanType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=eol::MapType_strategy)
@settings(max_examples=50)
def test_eol::maptype_instantiation(instance):
    assert isinstance(instance, eol::MapType)

@given(instance=eol::CollectionType_strategy)
@settings(max_examples=50)
def test_eol::collectiontype_instantiation(instance):
    assert isinstance(instance, eol::CollectionType)

@given(instance=eol::EType_strategy)
@settings(max_examples=50)
def test_eol::etype_instantiation(instance):
    assert isinstance(instance, eol::EType)

@given(instance=eol::ModelElementType_strategy)
@settings(max_examples=50)
def test_eol::modelelementtype_instantiation(instance):
    assert isinstance(instance, eol::ModelElementType)

@given(instance=eol::ModelElementType_strategy)
def test_eol::modelelementtype_elementName_type(instance):
    assert isinstance(instance.elementName, str)


@given(instance=eol::ModelElementType_strategy)
def test_eol::modelelementtype_elementName_setter(instance):
    original = instance.elementName
    instance.elementName = original
    assert instance.elementName == original

@given(instance=eol::ModelElementType_strategy)
def test_eol::modelelementtype_modelName_type(instance):
    assert isinstance(instance.modelName, str)


@given(instance=eol::ModelElementType_strategy)
def test_eol::modelelementtype_modelName_setter(instance):
    original = instance.modelName
    instance.modelName = original
    assert instance.modelName == original

@given(instance=eol::PrimitiveType_strategy)
@settings(max_examples=50)
def test_eol::primitivetype_instantiation(instance):
    assert isinstance(instance, eol::PrimitiveType)

@given(instance=eol::VoidType_strategy)
@settings(max_examples=50)
def test_eol::voidtype_instantiation(instance):
    assert isinstance(instance, eol::VoidType)

@given(instance=eol::NativeType_strategy)
@settings(max_examples=50)
def test_eol::nativetype_instantiation(instance):
    assert isinstance(instance, eol::NativeType)

@given(instance=eol::PseudoType_strategy)
@settings(max_examples=50)
def test_eol::pseudotype_instantiation(instance):
    assert isinstance(instance, eol::PseudoType)

@given(instance=eol::ModelType_strategy)
@settings(max_examples=50)
def test_eol::modeltype_instantiation(instance):
    assert isinstance(instance, eol::ModelType)

@given(instance=eol::AnyType_strategy)
@settings(max_examples=50)
def test_eol::anytype_instantiation(instance):
    assert isinstance(instance, eol::AnyType)

@given(instance=eol::AnyType_strategy)
def test_eol::anytype_declared_type(instance):
    assert isinstance(instance.declared, bool)


@given(instance=eol::AnyType_strategy)
def test_eol::anytype_declared_setter(instance):
    original = instance.declared
    instance.declared = original
    assert instance.declared == original

@given(instance=CollectionExpression_strategy)
@settings(max_examples=50)
def test_collectionexpression_instantiation(instance):
    assert isinstance(instance, CollectionExpression)

@given(instance=eol::OrderedSetExpression_strategy)
@settings(max_examples=50)
def test_eol::orderedsetexpression_instantiation(instance):
    assert isinstance(instance, eol::OrderedSetExpression)

@given(instance=eol::SequenceExpression_strategy)
@settings(max_examples=50)
def test_eol::sequenceexpression_instantiation(instance):
    assert isinstance(instance, eol::SequenceExpression)

@given(instance=eol::BagExpression_strategy)
@settings(max_examples=50)
def test_eol::bagexpression_instantiation(instance):
    assert isinstance(instance, eol::BagExpression)

@given(instance=eol::SetExpression_strategy)
@settings(max_examples=50)
def test_eol::setexpression_instantiation(instance):
    assert isinstance(instance, eol::SetExpression)

@given(instance=LiteralExpression_strategy)
@settings(max_examples=50)
def test_literalexpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)

@given(instance=eol::MapExpression_strategy)
@settings(max_examples=50)
def test_eol::mapexpression_instantiation(instance):
    assert isinstance(instance, eol::MapExpression)

@given(instance=eol::CollectionExpression_strategy)
@settings(max_examples=50)
def test_eol::collectionexpression_instantiation(instance):
    assert isinstance(instance, eol::CollectionExpression)

@given(instance=eol::NativeExpression_strategy)
@settings(max_examples=50)
def test_eol::nativeexpression_instantiation(instance):
    assert isinstance(instance, eol::NativeExpression)

@given(instance=eol::PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_eol::primitiveexpression_instantiation(instance):
    assert isinstance(instance, eol::PrimitiveExpression)

@given(instance=SwitchCaseStatement_strategy)
@settings(max_examples=50)
def test_switchcasestatement_instantiation(instance):
    assert isinstance(instance, SwitchCaseStatement)

@given(instance=eol::EPackage_strategy)
@settings(max_examples=50)
def test_eol::epackage_instantiation(instance):
    assert isinstance(instance, eol::EPackage)

@given(instance=eol::SwitchCaseDefaultStatement_strategy)
@settings(max_examples=50)
def test_eol::switchcasedefaultstatement_instantiation(instance):
    assert isinstance(instance, eol::SwitchCaseDefaultStatement)

@given(instance=eol::SwitchCaseExpressionStatement_strategy)
@settings(max_examples=50)
def test_eol::switchcaseexpressionstatement_instantiation(instance):
    assert isinstance(instance, eol::SwitchCaseExpressionStatement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=eol::TransactionStatement_strategy)
@settings(max_examples=50)
def test_eol::transactionstatement_instantiation(instance):
    assert isinstance(instance, eol::TransactionStatement)

@given(instance=eol::ReturnStatement_strategy)
@settings(max_examples=50)
def test_eol::returnstatement_instantiation(instance):
    assert isinstance(instance, eol::ReturnStatement)

@given(instance=eol::BreakAllStatement_strategy)
@settings(max_examples=50)
def test_eol::breakallstatement_instantiation(instance):
    assert isinstance(instance, eol::BreakAllStatement)

@given(instance=eol::SwitchStatement_strategy)
@settings(max_examples=50)
def test_eol::switchstatement_instantiation(instance):
    assert isinstance(instance, eol::SwitchStatement)

@given(instance=eol::DeleteStatement_strategy)
@settings(max_examples=50)
def test_eol::deletestatement_instantiation(instance):
    assert isinstance(instance, eol::DeleteStatement)

@given(instance=eol::ForStatement_strategy)
@settings(max_examples=50)
def test_eol::forstatement_instantiation(instance):
    assert isinstance(instance, eol::ForStatement)

@given(instance=eol::AbortStatement_strategy)
@settings(max_examples=50)
def test_eol::abortstatement_instantiation(instance):
    assert isinstance(instance, eol::AbortStatement)

@given(instance=eol::ThrowStatement_strategy)
@settings(max_examples=50)
def test_eol::throwstatement_instantiation(instance):
    assert isinstance(instance, eol::ThrowStatement)

@given(instance=eol::IfStatement_strategy)
@settings(max_examples=50)
def test_eol::ifstatement_instantiation(instance):
    assert isinstance(instance, eol::IfStatement)

@given(instance=eol::ModelDeclarationStatement_strategy)
@settings(max_examples=50)
def test_eol::modeldeclarationstatement_instantiation(instance):
    assert isinstance(instance, eol::ModelDeclarationStatement)

@given(instance=eol::WhileStatement_strategy)
@settings(max_examples=50)
def test_eol::whilestatement_instantiation(instance):
    assert isinstance(instance, eol::WhileStatement)

@given(instance=eol::SwitchCaseStatement_strategy)
@settings(max_examples=50)
def test_eol::switchcasestatement_instantiation(instance):
    assert isinstance(instance, eol::SwitchCaseStatement)

@given(instance=eol::BreakStatement_strategy)
@settings(max_examples=50)
def test_eol::breakstatement_instantiation(instance):
    assert isinstance(instance, eol::BreakStatement)

@given(instance=eol::ContinueStatement_strategy)
@settings(max_examples=50)
def test_eol::continuestatement_instantiation(instance):
    assert isinstance(instance, eol::ContinueStatement)

@given(instance=eol::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_eol::expressionstatement_instantiation(instance):
    assert isinstance(instance, eol::ExpressionStatement)

@given(instance=BinaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_binaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, BinaryOperatorExpression)

@given(instance=eol::ComparisonOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::comparisonoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::ComparisonOperatorExpression)

@given(instance=eol::ArithmeticOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::arithmeticoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::ArithmeticOperatorExpression)

@given(instance=eol::LogicalOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::logicaloperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::LogicalOperatorExpression)

@given(instance=eol::OperationArgType_strategy)
@settings(max_examples=50)
def test_eol::operationargtype_instantiation(instance):
    assert isinstance(instance, eol::OperationArgType)

@given(instance=eol::SelfInnermostType_strategy)
@settings(max_examples=50)
def test_eol::selfinnermosttype_instantiation(instance):
    assert isinstance(instance, eol::SelfInnermostType)

@given(instance=eol::AssignmentStatement_strategy)
@settings(max_examples=50)
def test_eol::assignmentstatement_instantiation(instance):
    assert isinstance(instance, eol::AssignmentStatement)

@given(instance=eol::FormalParameterExpression_strategy)
@settings(max_examples=50)
def test_eol::formalparameterexpression_instantiation(instance):
    assert isinstance(instance, eol::FormalParameterExpression)

@given(instance=UnaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_unaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, UnaryOperatorExpression)

@given(instance=eol::NotOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::notoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::NotOperatorExpression)

@given(instance=eol::NegativeOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::negativeoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::NegativeOperatorExpression)

@given(instance=eol::EObject_strategy)
@settings(max_examples=50)
def test_eol::eobject_instantiation(instance):
    assert isinstance(instance, eol::EObject)

@given(instance=FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_featurecallexpression_instantiation(instance):
    assert isinstance(instance, FeatureCallExpression)

@given(instance=eol::PropertyCallExpression_strategy)
@settings(max_examples=50)
def test_eol::propertycallexpression_instantiation(instance):
    assert isinstance(instance, eol::PropertyCallExpression)

@given(instance=eol::FOLMethodCallExpression_strategy)
@settings(max_examples=50)
def test_eol::folmethodcallexpression_instantiation(instance):
    assert isinstance(instance, eol::FOLMethodCallExpression)

@given(instance=eol::MethodCallExpression_strategy)
@settings(max_examples=50)
def test_eol::methodcallexpression_instantiation(instance):
    assert isinstance(instance, eol::MethodCallExpression)

@given(instance=ComparisonOperatorExpression_strategy)
@settings(max_examples=50)
def test_comparisonoperatorexpression_instantiation(instance):
    assert isinstance(instance, ComparisonOperatorExpression)

@given(instance=eol::NotEqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::notequalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::NotEqualsOperatorExpression)

@given(instance=eol::LessThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::lessthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::LessThanOrEqualToOperatorExpression)

@given(instance=eol::GreaterThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::greaterthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::GreaterThanOrEqualToOperatorExpression)

@given(instance=eol::GreaterThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::greaterthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::GreaterThanOperatorExpression)

@given(instance=eol::LessThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::lessthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::LessThanOperatorExpression)

@given(instance=eol::EqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::equalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::EqualsOperatorExpression)

@given(instance=eol::ModelExpression_strategy)
@settings(max_examples=50)
def test_eol::modelexpression_instantiation(instance):
    assert isinstance(instance, eol::ModelExpression)

@given(instance=ArithmeticOperatorExpression_strategy)
@settings(max_examples=50)
def test_arithmeticoperatorexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticOperatorExpression)

@given(instance=eol::PlusOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::plusoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::PlusOperatorExpression)

@given(instance=eol::MinusOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::minusoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::MinusOperatorExpression)

@given(instance=eol::MultiplyOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::multiplyoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::MultiplyOperatorExpression)

@given(instance=eol::DivideOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::divideoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::DivideOperatorExpression)

@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_primitiveexpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)

@given(instance=eol::RealExpression_strategy)
@settings(max_examples=50)
def test_eol::realexpression_instantiation(instance):
    assert isinstance(instance, eol::RealExpression)

@given(instance=eol::RealExpression_strategy)
def test_eol::realexpression_val_type(instance):
    assert isinstance(instance.val, float)


@given(instance=eol::RealExpression_strategy)
def test_eol::realexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=eol::IntegerExpression_strategy)
@settings(max_examples=50)
def test_eol::integerexpression_instantiation(instance):
    assert isinstance(instance, eol::IntegerExpression)

@given(instance=eol::IntegerExpression_strategy)
def test_eol::integerexpression_val_type(instance):
    assert isinstance(instance.val, int)


@given(instance=eol::IntegerExpression_strategy)
def test_eol::integerexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=eol::BooleanExpression_strategy)
@settings(max_examples=50)
def test_eol::booleanexpression_instantiation(instance):
    assert isinstance(instance, eol::BooleanExpression)

@given(instance=eol::BooleanExpression_strategy)
def test_eol::booleanexpression_val_type(instance):
    assert isinstance(instance.val, bool)


@given(instance=eol::BooleanExpression_strategy)
def test_eol::booleanexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=LogicalOperatorExpression_strategy)
@settings(max_examples=50)
def test_logicaloperatorexpression_instantiation(instance):
    assert isinstance(instance, LogicalOperatorExpression)

@given(instance=eol::ImpliesOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::impliesoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::ImpliesOperatorExpression)

@given(instance=eol::OrOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::oroperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::OrOperatorExpression)

@given(instance=eol::XorOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::xoroperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::XorOperatorExpression)

@given(instance=eol::AndOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::andoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::AndOperatorExpression)

@given(instance=OperatorExpression_strategy)
@settings(max_examples=50)
def test_operatorexpression_instantiation(instance):
    assert isinstance(instance, OperatorExpression)

@given(instance=eol::UnaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::unaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::UnaryOperatorExpression)

@given(instance=eol::BinaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::binaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::BinaryOperatorExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=eol::EnumerationLiteralExpression_strategy)
@settings(max_examples=50)
def test_eol::enumerationliteralexpression_instantiation(instance):
    assert isinstance(instance, eol::EnumerationLiteralExpression)

@given(instance=eol::NameExpression_strategy)
@settings(max_examples=50)
def test_eol::nameexpression_instantiation(instance):
    assert isinstance(instance, eol::NameExpression)

@given(instance=eol::NameExpression_strategy)
def test_eol::nameexpression_resolvedContent_type(instance):
    assert isinstance(instance.resolvedContent, str)


@given(instance=eol::NameExpression_strategy)
def test_eol::nameexpression_resolvedContent_setter(instance):
    original = instance.resolvedContent
    instance.resolvedContent = original
    assert instance.resolvedContent == original

@given(instance=eol::NameExpression_strategy)
def test_eol::nameexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eol::NameExpression_strategy)
def test_eol::nameexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eol::LiteralExpression_strategy)
@settings(max_examples=50)
def test_eol::literalexpression_instantiation(instance):
    assert isinstance(instance, eol::LiteralExpression)

@given(instance=eol::ModelDeclarationParameter_strategy)
@settings(max_examples=50)
def test_eol::modeldeclarationparameter_instantiation(instance):
    assert isinstance(instance, eol::ModelDeclarationParameter)

@given(instance=eol::FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_eol::featurecallexpression_instantiation(instance):
    assert isinstance(instance, eol::FeatureCallExpression)

@given(instance=eol::CollectionInitValue_strategy)
@settings(max_examples=50)
def test_eol::collectioninitvalue_instantiation(instance):
    assert isinstance(instance, eol::CollectionInitValue)

@given(instance=eol::KeyValue_strategy)
@settings(max_examples=50)
def test_eol::keyvalue_instantiation(instance):
    assert isinstance(instance, eol::KeyValue)

@given(instance=eol::VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_eol::variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, eol::VariableDeclarationExpression)

@given(instance=eol::VariableDeclarationExpression_strategy)
def test_eol::variabledeclarationexpression_definitionPoints_type(instance):
    assert isinstance(instance.definitionPoints, str)


@given(instance=eol::VariableDeclarationExpression_strategy)
def test_eol::variabledeclarationexpression_definitionPoints_setter(instance):
    original = instance.definitionPoints
    instance.definitionPoints = original
    assert instance.definitionPoints == original

@given(instance=eol::NewExpression_strategy)
@settings(max_examples=50)
def test_eol::newexpression_instantiation(instance):
    assert isinstance(instance, eol::NewExpression)

@given(instance=eol::OperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::operatorexpression_instantiation(instance):
    assert isinstance(instance, eol::OperatorExpression)

@given(instance=eol::StringExpression_strategy)
@settings(max_examples=50)
def test_eol::stringexpression_instantiation(instance):
    assert isinstance(instance, eol::StringExpression)

@given(instance=eol::StringExpression_strategy)
def test_eol::stringexpression_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=eol::StringExpression_strategy)
def test_eol::stringexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=EolElement_strategy)
@settings(max_examples=50)
def test_eolelement_instantiation(instance):
    assert isinstance(instance, EolElement)

@given(instance=eol::EolLibraryModule_strategy)
@settings(max_examples=50)
def test_eol::eollibrarymodule_instantiation(instance):
    assert isinstance(instance, eol::EolLibraryModule)

@given(instance=eol::Statement_strategy)
@settings(max_examples=50)
def test_eol::statement_instantiation(instance):
    assert isinstance(instance, eol::Statement)

@given(instance=eol::Expression_strategy)
@settings(max_examples=50)
def test_eol::expression_instantiation(instance):
    assert isinstance(instance, eol::Expression)

@given(instance=eol::OperationDefinition_strategy)
@settings(max_examples=50)
def test_eol::operationdefinition_instantiation(instance):
    assert isinstance(instance, eol::OperationDefinition)

@given(instance=eol::AnnotationBlock_strategy)
@settings(max_examples=50)
def test_eol::annotationblock_instantiation(instance):
    assert isinstance(instance, eol::AnnotationBlock)

@given(instance=eol::ExpressionOrStatementBlock_strategy)
@settings(max_examples=50)
def test_eol::expressionorstatementblock_instantiation(instance):
    assert isinstance(instance, eol::ExpressionOrStatementBlock)

@given(instance=eol::Annotation_strategy)
@settings(max_examples=50)
def test_eol::annotation_instantiation(instance):
    assert isinstance(instance, eol::Annotation)

@given(instance=eol::Type_strategy)
@settings(max_examples=50)
def test_eol::type_instantiation(instance):
    assert isinstance(instance, eol::Type)

@given(instance=eol::Import_strategy)
@settings(max_examples=50)
def test_eol::import_instantiation(instance):
    assert isinstance(instance, eol::Import)

@given(instance=eol::Block_strategy)
@settings(max_examples=50)
def test_eol::block_instantiation(instance):
    assert isinstance(instance, eol::Block)

@given(instance=EolLibraryModule_strategy)
@settings(max_examples=50)
def test_eollibrarymodule_instantiation(instance):
    assert isinstance(instance, EolLibraryModule)

@given(instance=eol::EolProgram_strategy)
@settings(max_examples=50)
def test_eol::eolprogram_instantiation(instance):
    assert isinstance(instance, eol::EolProgram)

@given(instance=eol::TextPosition_strategy)
@settings(max_examples=50)
def test_eol::textposition_instantiation(instance):
    assert isinstance(instance, eol::TextPosition)

@given(instance=eol::TextPosition_strategy)
def test_eol::textposition_column_type(instance):
    assert isinstance(instance.column, int)


@given(instance=eol::TextPosition_strategy)
def test_eol::textposition_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=eol::TextPosition_strategy)
def test_eol::textposition_line_type(instance):
    assert isinstance(instance.line, int)


@given(instance=eol::TextPosition_strategy)
def test_eol::textposition_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=eol::TextRegion_strategy)
@settings(max_examples=50)
def test_eol::textregion_instantiation(instance):
    assert isinstance(instance, eol::TextRegion)

@given(instance=eol::EolElement_strategy)
@settings(max_examples=50)
def test_eol::eolelement_instantiation(instance):
    assert isinstance(instance, eol::EolElement)

@given(instance=eol::EolElement_strategy)
def test_eol::eolelement_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=eol::EolElement_strategy)
def test_eol::eolelement_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=eol::EolElement_strategy)
def test_eol::eolelement_line_type(instance):
    assert isinstance(instance.line, int)


@given(instance=eol::EolElement_strategy)
def test_eol::eolelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=eol::EolElement_strategy)
def test_eol::eolelement_column_type(instance):
    assert isinstance(instance.column, int)


@given(instance=eol::EolElement_strategy)
def test_eol::eolelement_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original
