import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SummablePrimitiveType,
    ComparablePrimitiveType,
    eol::RealType,
    PrimitiveType,
    eol::BooleanType,
    eol::SummablePrimitiveType,
    eol::ComparablePrimitiveType,
    OrderedCollectionType,
    eol::SequenceType,
    UniqueCollectionType,
    eol::OrderedSetType,
    eol::SetType,
    CollectionType,
    eol::UniqueCollectionType,
    eol::OrderedCollectionType,
    eol::BagType,
    eol::StringType,
    RealType,
    eol::IntegerType,
    Type,
    eol::AnyType,
    AnnotationStatement,
    eol::ExecutableAnnotationStatement,
    eol::SimpleAnnotationStatement,
    AssignmentStatement,
    eol::SpecialAssignmentStatement,
    PseudoType,
    eol::SelfContentType,
    eol::SelfType,
    AnyType,
    eol::InvalidType,
    eol::MapType,
    eol::ModelElementType,
    eol::PseudoType,
    eol::CollectionType,
    eol::NativeType,
    eol::VoidType,
    eol::PrimitiveType,
    eol::ModelType,
    SwitchCaseStatement,
    Statement,
    eol::BreakAllStatement,
    eol::DeleteStatement,
    eol::AbortStatement,
    eol::ThrowStatement,
    eol::AssignmentStatement,
    eol::BreakStatement,
    eol::ReturnStatement,
    eol::AnnotationStatement,
    eol::ContinueStatement,
    eol::WhileStatement,
    eol::SwitchCaseStatement,
    eol::IfStatement,
    eol::ForStatement,
    eol::TransactionStatement,
    CollectionInitialisationExpression,
    eol::ExpressionList,
    eol::ExpressionRange,
    OrderedCollection,
    eol::SequenceExpression,
    UniqueCollection,
    eol::OrderedSetExpression,
    eol::SetExpression,
    CollectionExpression,
    eol::UniqueCollection,
    eol::OrderedCollection,
    eol::BagExpression,
    eol::SwitchCaseDefaultStatement,
    eol::SwitchCaseExpressionStatement,
    eol::SwitchStatement,
    eol::ExpressionStatement,
    SummableExpression,
    ComparableExpression,
    eol::RealExpression,
    eol::IntegerExpression,
    eol::StringExpression,
    PrimitiveExpression,
    eol::SummableExpression,
    eol::BooleanExpression,
    eol::ComparableExpression,
    FeatureCallExpression,
    eol::FOLMethodCallExpression,
    eol::PropertyCallExpression,
    eol::MethodCallExpression,
    VariableDeclarationExpression,
    KeyValueExpression,
    eol::ModelDeclarationParameter,
    UnaryOperatorExpression,
    eol::NegativeOperatorExpression,
    eol::NotOperatorExpression,
    OperatorExpression,
    eol::BinaryOperatorExpression,
    eol::UnaryOperatorExpression,
    Expression,
    eol::CollectionInitialisationExpression,
    eol::KeyValueExpression,
    eol::CollectionExpression,
    eol::PrimitiveExpression,
    eol::MapExpression,
    eol::FeatureCallExpression,
    eol::EnumerationLiteralExpression,
    eol::NewExpression,
    eol::OperatorExpression,
    eol::VariableDeclarationExpression,
    eol::FormalParameterExpression,
    eol::NameExpression,
    ComparisonOperatorExpression,
    eol::NotEqualsOperatorExpression,
    eol::GreaterThanOperatorExpression,
    eol::LessThanOrEqualToOperatorExpression,
    eol::LessThanOperatorExpression,
    eol::EqualsOperatorExpression,
    eol::GreaterThanOrEqualToOperatorExpression,
    ArithmeticOperatorExpression,
    eol::MultiplyOperatorExpression,
    eol::MinusOperatorExpression,
    eol::PlusOperatorExpression,
    eol::DivideOperatorExpression,
    LogicalOperatorExpression,
    eol::ImpliesOperatorExpression,
    eol::XorOperatorExpression,
    eol::OrOperatorExpression,
    eol::AndOperatorExpression,
    BinaryOperatorExpression,
    eol::ArithmeticOperatorExpression,
    eol::ComparisonOperatorExpression,
    eol::LogicalOperatorExpression,
    Block,
    eol::AnnotationBlock,
    EOLLibraryModule,
    eol::EOLModule,
    eol::ModelDeclarationStatement,
    EOLElement,
    eol::ExpressionOrStatementBlock,
    eol::Import,
    eol::OperationDefinition,
    eol::Statement,
    eol::Block,
    eol::EOLLibraryModule,
    eol::Type,
    eol::Expression,
    eol::EOLElement,
    eol::TextPosition,
    eol::TextRegion,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_summableprimitivetype_is_not_abstract():
    assert not inspect.isabstract(SummablePrimitiveType)


def test_summableprimitivetype_constructor_exists():
    assert callable(SummablePrimitiveType.__init__)


def test_summableprimitivetype_constructor_args():
    sig = inspect.signature(SummablePrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_comparableprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ComparablePrimitiveType)


def test_comparableprimitivetype_constructor_exists():
    assert callable(ComparablePrimitiveType.__init__)


def test_comparableprimitivetype_constructor_args():
    sig = inspect.signature(ComparablePrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_eol::realtype_is_not_abstract():
    assert not inspect.isabstract(eol::RealType)


def test_eol::realtype_constructor_exists():
    assert callable(eol::RealType.__init__)


def test_eol::realtype_constructor_args():
    sig = inspect.signature(eol::RealType.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_eol::booleantype_is_not_abstract():
    assert not inspect.isabstract(eol::BooleanType)


def test_eol::booleantype_constructor_exists():
    assert callable(eol::BooleanType.__init__)


def test_eol::booleantype_constructor_args():
    sig = inspect.signature(eol::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_eol::summableprimitivetype_is_not_abstract():
    assert not inspect.isabstract(eol::SummablePrimitiveType)


def test_eol::summableprimitivetype_constructor_exists():
    assert callable(eol::SummablePrimitiveType.__init__)


def test_eol::summableprimitivetype_constructor_args():
    sig = inspect.signature(eol::SummablePrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_eol::comparableprimitivetype_is_not_abstract():
    assert not inspect.isabstract(eol::ComparablePrimitiveType)


def test_eol::comparableprimitivetype_constructor_exists():
    assert callable(eol::ComparablePrimitiveType.__init__)


def test_eol::comparableprimitivetype_constructor_args():
    sig = inspect.signature(eol::ComparablePrimitiveType.__init__)
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



def test_eol::stringtype_is_not_abstract():
    assert not inspect.isabstract(eol::StringType)


def test_eol::stringtype_constructor_exists():
    assert callable(eol::StringType.__init__)


def test_eol::stringtype_constructor_args():
    sig = inspect.signature(eol::StringType.__init__)
    params = list(sig.parameters.keys())



def test_realtype_is_not_abstract():
    assert not inspect.isabstract(RealType)


def test_realtype_constructor_exists():
    assert callable(RealType.__init__)


def test_realtype_constructor_args():
    sig = inspect.signature(RealType.__init__)
    params = list(sig.parameters.keys())



def test_eol::integertype_is_not_abstract():
    assert not inspect.isabstract(eol::IntegerType)


def test_eol::integertype_constructor_exists():
    assert callable(eol::IntegerType.__init__)


def test_eol::integertype_constructor_args():
    sig = inspect.signature(eol::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
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



def test_annotationstatement_is_not_abstract():
    assert not inspect.isabstract(AnnotationStatement)


def test_annotationstatement_constructor_exists():
    assert callable(AnnotationStatement.__init__)


def test_annotationstatement_constructor_args():
    sig = inspect.signature(AnnotationStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::executableannotationstatement_is_not_abstract():
    assert not inspect.isabstract(eol::ExecutableAnnotationStatement)


def test_eol::executableannotationstatement_constructor_exists():
    assert callable(eol::ExecutableAnnotationStatement.__init__)


def test_eol::executableannotationstatement_constructor_args():
    sig = inspect.signature(eol::ExecutableAnnotationStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::simpleannotationstatement_is_not_abstract():
    assert not inspect.isabstract(eol::SimpleAnnotationStatement)


def test_eol::simpleannotationstatement_constructor_exists():
    assert callable(eol::SimpleAnnotationStatement.__init__)


def test_eol::simpleannotationstatement_constructor_args():
    sig = inspect.signature(eol::SimpleAnnotationStatement.__init__)
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



def test_anytype_is_not_abstract():
    assert not inspect.isabstract(AnyType)


def test_anytype_constructor_exists():
    assert callable(AnyType.__init__)


def test_anytype_constructor_args():
    sig = inspect.signature(AnyType.__init__)
    params = list(sig.parameters.keys())



def test_eol::invalidtype_is_not_abstract():
    assert not inspect.isabstract(eol::InvalidType)


def test_eol::invalidtype_constructor_exists():
    assert callable(eol::InvalidType.__init__)


def test_eol::invalidtype_constructor_args():
    sig = inspect.signature(eol::InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_eol::maptype_is_not_abstract():
    assert not inspect.isabstract(eol::MapType)


def test_eol::maptype_constructor_exists():
    assert callable(eol::MapType.__init__)


def test_eol::maptype_constructor_args():
    sig = inspect.signature(eol::MapType.__init__)
    params = list(sig.parameters.keys())



def test_eol::modelelementtype_is_not_abstract():
    assert not inspect.isabstract(eol::ModelElementType)


def test_eol::modelelementtype_constructor_exists():
    assert callable(eol::ModelElementType.__init__)


def test_eol::modelelementtype_constructor_args():
    sig = inspect.signature(eol::ModelElementType.__init__)
    params = list(sig.parameters.keys())
    assert "modelName" in params, "Missing parameter 'modelName'"
    assert "resolvedIMetamodel" in params, "Missing parameter 'resolvedIMetamodel'"
    assert "resolvedIPackage" in params, "Missing parameter 'resolvedIPackage'"
    assert "elementName" in params, "Missing parameter 'elementName'"
    assert "modelElementType" in params, "Missing parameter 'modelElementType'"

def test_eol::modelelementtype_has_modelName():
    assert hasattr(eol::ModelElementType, "modelName")
    descriptor = None
    for klass in eol::ModelElementType.__mro__:
        if "modelName" in klass.__dict__:
            descriptor = klass.__dict__["modelName"]
            break
    assert isinstance(descriptor, property)

def test_eol::modelelementtype_has_resolvedIMetamodel():
    assert hasattr(eol::ModelElementType, "resolvedIMetamodel")
    descriptor = None
    for klass in eol::ModelElementType.__mro__:
        if "resolvedIMetamodel" in klass.__dict__:
            descriptor = klass.__dict__["resolvedIMetamodel"]
            break
    assert isinstance(descriptor, property)

def test_eol::modelelementtype_has_resolvedIPackage():
    assert hasattr(eol::ModelElementType, "resolvedIPackage")
    descriptor = None
    for klass in eol::ModelElementType.__mro__:
        if "resolvedIPackage" in klass.__dict__:
            descriptor = klass.__dict__["resolvedIPackage"]
            break
    assert isinstance(descriptor, property)

def test_eol::modelelementtype_has_elementName():
    assert hasattr(eol::ModelElementType, "elementName")
    descriptor = None
    for klass in eol::ModelElementType.__mro__:
        if "elementName" in klass.__dict__:
            descriptor = klass.__dict__["elementName"]
            break
    assert isinstance(descriptor, property)

def test_eol::modelelementtype_has_modelElementType():
    assert hasattr(eol::ModelElementType, "modelElementType")
    descriptor = None
    for klass in eol::ModelElementType.__mro__:
        if "modelElementType" in klass.__dict__:
            descriptor = klass.__dict__["modelElementType"]
            break
    assert isinstance(descriptor, property)



def test_eol::pseudotype_is_not_abstract():
    assert not inspect.isabstract(eol::PseudoType)


def test_eol::pseudotype_constructor_exists():
    assert callable(eol::PseudoType.__init__)


def test_eol::pseudotype_constructor_args():
    sig = inspect.signature(eol::PseudoType.__init__)
    params = list(sig.parameters.keys())



def test_eol::collectiontype_is_not_abstract():
    assert not inspect.isabstract(eol::CollectionType)


def test_eol::collectiontype_constructor_exists():
    assert callable(eol::CollectionType.__init__)


def test_eol::collectiontype_constructor_args():
    sig = inspect.signature(eol::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol::nativetype_is_not_abstract():
    assert not inspect.isabstract(eol::NativeType)


def test_eol::nativetype_constructor_exists():
    assert callable(eol::NativeType.__init__)


def test_eol::nativetype_constructor_args():
    sig = inspect.signature(eol::NativeType.__init__)
    params = list(sig.parameters.keys())



def test_eol::voidtype_is_not_abstract():
    assert not inspect.isabstract(eol::VoidType)


def test_eol::voidtype_constructor_exists():
    assert callable(eol::VoidType.__init__)


def test_eol::voidtype_constructor_args():
    sig = inspect.signature(eol::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_eol::primitivetype_is_not_abstract():
    assert not inspect.isabstract(eol::PrimitiveType)


def test_eol::primitivetype_constructor_exists():
    assert callable(eol::PrimitiveType.__init__)


def test_eol::primitivetype_constructor_args():
    sig = inspect.signature(eol::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_eol::modeltype_is_not_abstract():
    assert not inspect.isabstract(eol::ModelType)


def test_eol::modeltype_constructor_exists():
    assert callable(eol::ModelType.__init__)


def test_eol::modeltype_constructor_args():
    sig = inspect.signature(eol::ModelType.__init__)
    params = list(sig.parameters.keys())
    assert "modelName" in params, "Missing parameter 'modelName'"
    assert "resolvedIMetamodel" in params, "Missing parameter 'resolvedIMetamodel'"

def test_eol::modeltype_has_modelName():
    assert hasattr(eol::ModelType, "modelName")
    descriptor = None
    for klass in eol::ModelType.__mro__:
        if "modelName" in klass.__dict__:
            descriptor = klass.__dict__["modelName"]
            break
    assert isinstance(descriptor, property)

def test_eol::modeltype_has_resolvedIMetamodel():
    assert hasattr(eol::ModelType, "resolvedIMetamodel")
    descriptor = None
    for klass in eol::ModelType.__mro__:
        if "resolvedIMetamodel" in klass.__dict__:
            descriptor = klass.__dict__["resolvedIMetamodel"]
            break
    assert isinstance(descriptor, property)



def test_switchcasestatement_is_not_abstract():
    assert not inspect.isabstract(SwitchCaseStatement)


def test_switchcasestatement_constructor_exists():
    assert callable(SwitchCaseStatement.__init__)


def test_switchcasestatement_constructor_args():
    sig = inspect.signature(SwitchCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_eol::breakallstatement_is_not_abstract():
    assert not inspect.isabstract(eol::BreakAllStatement)


def test_eol::breakallstatement_constructor_exists():
    assert callable(eol::BreakAllStatement.__init__)


def test_eol::breakallstatement_constructor_args():
    sig = inspect.signature(eol::BreakAllStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::deletestatement_is_not_abstract():
    assert not inspect.isabstract(eol::DeleteStatement)


def test_eol::deletestatement_constructor_exists():
    assert callable(eol::DeleteStatement.__init__)


def test_eol::deletestatement_constructor_args():
    sig = inspect.signature(eol::DeleteStatement.__init__)
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



def test_eol::assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(eol::AssignmentStatement)


def test_eol::assignmentstatement_constructor_exists():
    assert callable(eol::AssignmentStatement.__init__)


def test_eol::assignmentstatement_constructor_args():
    sig = inspect.signature(eol::AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::breakstatement_is_not_abstract():
    assert not inspect.isabstract(eol::BreakStatement)


def test_eol::breakstatement_constructor_exists():
    assert callable(eol::BreakStatement.__init__)


def test_eol::breakstatement_constructor_args():
    sig = inspect.signature(eol::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::returnstatement_is_not_abstract():
    assert not inspect.isabstract(eol::ReturnStatement)


def test_eol::returnstatement_constructor_exists():
    assert callable(eol::ReturnStatement.__init__)


def test_eol::returnstatement_constructor_args():
    sig = inspect.signature(eol::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::annotationstatement_is_not_abstract():
    assert not inspect.isabstract(eol::AnnotationStatement)


def test_eol::annotationstatement_constructor_exists():
    assert callable(eol::AnnotationStatement.__init__)


def test_eol::annotationstatement_constructor_args():
    sig = inspect.signature(eol::AnnotationStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::continuestatement_is_not_abstract():
    assert not inspect.isabstract(eol::ContinueStatement)


def test_eol::continuestatement_constructor_exists():
    assert callable(eol::ContinueStatement.__init__)


def test_eol::continuestatement_constructor_args():
    sig = inspect.signature(eol::ContinueStatement.__init__)
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



def test_eol::ifstatement_is_not_abstract():
    assert not inspect.isabstract(eol::IfStatement)


def test_eol::ifstatement_constructor_exists():
    assert callable(eol::IfStatement.__init__)


def test_eol::ifstatement_constructor_args():
    sig = inspect.signature(eol::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::forstatement_is_not_abstract():
    assert not inspect.isabstract(eol::ForStatement)


def test_eol::forstatement_constructor_exists():
    assert callable(eol::ForStatement.__init__)


def test_eol::forstatement_constructor_args():
    sig = inspect.signature(eol::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::transactionstatement_is_not_abstract():
    assert not inspect.isabstract(eol::TransactionStatement)


def test_eol::transactionstatement_constructor_exists():
    assert callable(eol::TransactionStatement.__init__)


def test_eol::transactionstatement_constructor_args():
    sig = inspect.signature(eol::TransactionStatement.__init__)
    params = list(sig.parameters.keys())



def test_collectioninitialisationexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionInitialisationExpression)


def test_collectioninitialisationexpression_constructor_exists():
    assert callable(CollectionInitialisationExpression.__init__)


def test_collectioninitialisationexpression_constructor_args():
    sig = inspect.signature(CollectionInitialisationExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::expressionlist_is_not_abstract():
    assert not inspect.isabstract(eol::ExpressionList)


def test_eol::expressionlist_constructor_exists():
    assert callable(eol::ExpressionList.__init__)


def test_eol::expressionlist_constructor_args():
    sig = inspect.signature(eol::ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_eol::expressionrange_is_not_abstract():
    assert not inspect.isabstract(eol::ExpressionRange)


def test_eol::expressionrange_constructor_exists():
    assert callable(eol::ExpressionRange.__init__)


def test_eol::expressionrange_constructor_args():
    sig = inspect.signature(eol::ExpressionRange.__init__)
    params = list(sig.parameters.keys())



def test_orderedcollection_is_not_abstract():
    assert not inspect.isabstract(OrderedCollection)


def test_orderedcollection_constructor_exists():
    assert callable(OrderedCollection.__init__)


def test_orderedcollection_constructor_args():
    sig = inspect.signature(OrderedCollection.__init__)
    params = list(sig.parameters.keys())



def test_eol::sequenceexpression_is_not_abstract():
    assert not inspect.isabstract(eol::SequenceExpression)


def test_eol::sequenceexpression_constructor_exists():
    assert callable(eol::SequenceExpression.__init__)


def test_eol::sequenceexpression_constructor_args():
    sig = inspect.signature(eol::SequenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_uniquecollection_is_not_abstract():
    assert not inspect.isabstract(UniqueCollection)


def test_uniquecollection_constructor_exists():
    assert callable(UniqueCollection.__init__)


def test_uniquecollection_constructor_args():
    sig = inspect.signature(UniqueCollection.__init__)
    params = list(sig.parameters.keys())



def test_eol::orderedsetexpression_is_not_abstract():
    assert not inspect.isabstract(eol::OrderedSetExpression)


def test_eol::orderedsetexpression_constructor_exists():
    assert callable(eol::OrderedSetExpression.__init__)


def test_eol::orderedsetexpression_constructor_args():
    sig = inspect.signature(eol::OrderedSetExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::setexpression_is_not_abstract():
    assert not inspect.isabstract(eol::SetExpression)


def test_eol::setexpression_constructor_exists():
    assert callable(eol::SetExpression.__init__)


def test_eol::setexpression_constructor_args():
    sig = inspect.signature(eol::SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionExpression)


def test_collectionexpression_constructor_exists():
    assert callable(CollectionExpression.__init__)


def test_collectionexpression_constructor_args():
    sig = inspect.signature(CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::uniquecollection_is_not_abstract():
    assert not inspect.isabstract(eol::UniqueCollection)


def test_eol::uniquecollection_constructor_exists():
    assert callable(eol::UniqueCollection.__init__)


def test_eol::uniquecollection_constructor_args():
    sig = inspect.signature(eol::UniqueCollection.__init__)
    params = list(sig.parameters.keys())



def test_eol::orderedcollection_is_not_abstract():
    assert not inspect.isabstract(eol::OrderedCollection)


def test_eol::orderedcollection_constructor_exists():
    assert callable(eol::OrderedCollection.__init__)


def test_eol::orderedcollection_constructor_args():
    sig = inspect.signature(eol::OrderedCollection.__init__)
    params = list(sig.parameters.keys())



def test_eol::bagexpression_is_not_abstract():
    assert not inspect.isabstract(eol::BagExpression)


def test_eol::bagexpression_constructor_exists():
    assert callable(eol::BagExpression.__init__)


def test_eol::bagexpression_constructor_args():
    sig = inspect.signature(eol::BagExpression.__init__)
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



def test_eol::switchstatement_is_not_abstract():
    assert not inspect.isabstract(eol::SwitchStatement)


def test_eol::switchstatement_constructor_exists():
    assert callable(eol::SwitchStatement.__init__)


def test_eol::switchstatement_constructor_args():
    sig = inspect.signature(eol::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(eol::ExpressionStatement)


def test_eol::expressionstatement_constructor_exists():
    assert callable(eol::ExpressionStatement.__init__)


def test_eol::expressionstatement_constructor_args():
    sig = inspect.signature(eol::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_summableexpression_is_not_abstract():
    assert not inspect.isabstract(SummableExpression)


def test_summableexpression_constructor_exists():
    assert callable(SummableExpression.__init__)


def test_summableexpression_constructor_args():
    sig = inspect.signature(SummableExpression.__init__)
    params = list(sig.parameters.keys())



def test_comparableexpression_is_not_abstract():
    assert not inspect.isabstract(ComparableExpression)


def test_comparableexpression_constructor_exists():
    assert callable(ComparableExpression.__init__)


def test_comparableexpression_constructor_args():
    sig = inspect.signature(ComparableExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::realexpression_is_not_abstract():
    assert not inspect.isabstract(eol::RealExpression)


def test_eol::realexpression_constructor_exists():
    assert callable(eol::RealExpression.__init__)


def test_eol::realexpression_constructor_args():
    sig = inspect.signature(eol::RealExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol::realexpression_has_value():
    assert hasattr(eol::RealExpression, "value")
    descriptor = None
    for klass in eol::RealExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_eol::integerexpression_is_not_abstract():
    assert not inspect.isabstract(eol::IntegerExpression)


def test_eol::integerexpression_constructor_exists():
    assert callable(eol::IntegerExpression.__init__)


def test_eol::integerexpression_constructor_args():
    sig = inspect.signature(eol::IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol::integerexpression_has_value():
    assert hasattr(eol::IntegerExpression, "value")
    descriptor = None
    for klass in eol::IntegerExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_eol::stringexpression_is_not_abstract():
    assert not inspect.isabstract(eol::StringExpression)


def test_eol::stringexpression_constructor_exists():
    assert callable(eol::StringExpression.__init__)


def test_eol::stringexpression_constructor_args():
    sig = inspect.signature(eol::StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol::stringexpression_has_value():
    assert hasattr(eol::StringExpression, "value")
    descriptor = None
    for klass in eol::StringExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExpression)


def test_primitiveexpression_constructor_exists():
    assert callable(PrimitiveExpression.__init__)


def test_primitiveexpression_constructor_args():
    sig = inspect.signature(PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::summableexpression_is_not_abstract():
    assert not inspect.isabstract(eol::SummableExpression)


def test_eol::summableexpression_constructor_exists():
    assert callable(eol::SummableExpression.__init__)


def test_eol::summableexpression_constructor_args():
    sig = inspect.signature(eol::SummableExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(eol::BooleanExpression)


def test_eol::booleanexpression_constructor_exists():
    assert callable(eol::BooleanExpression.__init__)


def test_eol::booleanexpression_constructor_args():
    sig = inspect.signature(eol::BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol::booleanexpression_has_value():
    assert hasattr(eol::BooleanExpression, "value")
    descriptor = None
    for klass in eol::BooleanExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_eol::comparableexpression_is_not_abstract():
    assert not inspect.isabstract(eol::ComparableExpression)


def test_eol::comparableexpression_constructor_exists():
    assert callable(eol::ComparableExpression.__init__)


def test_eol::comparableexpression_constructor_args():
    sig = inspect.signature(eol::ComparableExpression.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExpression)


def test_featurecallexpression_constructor_exists():
    assert callable(FeatureCallExpression.__init__)


def test_featurecallexpression_constructor_args():
    sig = inspect.signature(FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::folmethodcallexpression_is_not_abstract():
    assert not inspect.isabstract(eol::FOLMethodCallExpression)


def test_eol::folmethodcallexpression_constructor_exists():
    assert callable(eol::FOLMethodCallExpression.__init__)


def test_eol::folmethodcallexpression_constructor_args():
    sig = inspect.signature(eol::FOLMethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::propertycallexpression_is_not_abstract():
    assert not inspect.isabstract(eol::PropertyCallExpression)


def test_eol::propertycallexpression_constructor_exists():
    assert callable(eol::PropertyCallExpression.__init__)


def test_eol::propertycallexpression_constructor_args():
    sig = inspect.signature(eol::PropertyCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "extended" in params, "Missing parameter 'extended'"

def test_eol::propertycallexpression_has_extended():
    assert hasattr(eol::PropertyCallExpression, "extended")
    descriptor = None
    for klass in eol::PropertyCallExpression.__mro__:
        if "extended" in klass.__dict__:
            descriptor = klass.__dict__["extended"]
            break
    assert isinstance(descriptor, property)



def test_eol::methodcallexpression_is_not_abstract():
    assert not inspect.isabstract(eol::MethodCallExpression)


def test_eol::methodcallexpression_constructor_exists():
    assert callable(eol::MethodCallExpression.__init__)


def test_eol::methodcallexpression_constructor_args():
    sig = inspect.signature(eol::MethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationExpression)


def test_variabledeclarationexpression_constructor_exists():
    assert callable(VariableDeclarationExpression.__init__)


def test_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_keyvalueexpression_is_not_abstract():
    assert not inspect.isabstract(KeyValueExpression)


def test_keyvalueexpression_constructor_exists():
    assert callable(KeyValueExpression.__init__)


def test_keyvalueexpression_constructor_args():
    sig = inspect.signature(KeyValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::modeldeclarationparameter_is_not_abstract():
    assert not inspect.isabstract(eol::ModelDeclarationParameter)


def test_eol::modeldeclarationparameter_constructor_exists():
    assert callable(eol::ModelDeclarationParameter.__init__)


def test_eol::modeldeclarationparameter_constructor_args():
    sig = inspect.signature(eol::ModelDeclarationParameter.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryOperatorExpression)


def test_unaryoperatorexpression_constructor_exists():
    assert callable(UnaryOperatorExpression.__init__)


def test_unaryoperatorexpression_constructor_args():
    sig = inspect.signature(UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::negativeoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::NegativeOperatorExpression)


def test_eol::negativeoperatorexpression_constructor_exists():
    assert callable(eol::NegativeOperatorExpression.__init__)


def test_eol::negativeoperatorexpression_constructor_args():
    sig = inspect.signature(eol::NegativeOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::notoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::NotOperatorExpression)


def test_eol::notoperatorexpression_constructor_exists():
    assert callable(eol::NotOperatorExpression.__init__)


def test_eol::notoperatorexpression_constructor_args():
    sig = inspect.signature(eol::NotOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(OperatorExpression)


def test_operatorexpression_constructor_exists():
    assert callable(OperatorExpression.__init__)


def test_operatorexpression_constructor_args():
    sig = inspect.signature(OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::BinaryOperatorExpression)


def test_eol::binaryoperatorexpression_constructor_exists():
    assert callable(eol::BinaryOperatorExpression.__init__)


def test_eol::binaryoperatorexpression_constructor_args():
    sig = inspect.signature(eol::BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::UnaryOperatorExpression)


def test_eol::unaryoperatorexpression_constructor_exists():
    assert callable(eol::UnaryOperatorExpression.__init__)


def test_eol::unaryoperatorexpression_constructor_args():
    sig = inspect.signature(eol::UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_eol::collectioninitialisationexpression_is_not_abstract():
    assert not inspect.isabstract(eol::CollectionInitialisationExpression)


def test_eol::collectioninitialisationexpression_constructor_exists():
    assert callable(eol::CollectionInitialisationExpression.__init__)


def test_eol::collectioninitialisationexpression_constructor_args():
    sig = inspect.signature(eol::CollectionInitialisationExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::keyvalueexpression_is_not_abstract():
    assert not inspect.isabstract(eol::KeyValueExpression)


def test_eol::keyvalueexpression_constructor_exists():
    assert callable(eol::KeyValueExpression.__init__)


def test_eol::keyvalueexpression_constructor_args():
    sig = inspect.signature(eol::KeyValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::collectionexpression_is_not_abstract():
    assert not inspect.isabstract(eol::CollectionExpression)


def test_eol::collectionexpression_constructor_exists():
    assert callable(eol::CollectionExpression.__init__)


def test_eol::collectionexpression_constructor_args():
    sig = inspect.signature(eol::CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(eol::PrimitiveExpression)


def test_eol::primitiveexpression_constructor_exists():
    assert callable(eol::PrimitiveExpression.__init__)


def test_eol::primitiveexpression_constructor_args():
    sig = inspect.signature(eol::PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::mapexpression_is_not_abstract():
    assert not inspect.isabstract(eol::MapExpression)


def test_eol::mapexpression_constructor_exists():
    assert callable(eol::MapExpression.__init__)


def test_eol::mapexpression_constructor_args():
    sig = inspect.signature(eol::MapExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(eol::FeatureCallExpression)


def test_eol::featurecallexpression_constructor_exists():
    assert callable(eol::FeatureCallExpression.__init__)


def test_eol::featurecallexpression_constructor_args():
    sig = inspect.signature(eol::FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "arrow" in params, "Missing parameter 'arrow'"

def test_eol::featurecallexpression_has_arrow():
    assert hasattr(eol::FeatureCallExpression, "arrow")
    descriptor = None
    for klass in eol::FeatureCallExpression.__mro__:
        if "arrow" in klass.__dict__:
            descriptor = klass.__dict__["arrow"]
            break
    assert isinstance(descriptor, property)



def test_eol::enumerationliteralexpression_is_not_abstract():
    assert not inspect.isabstract(eol::EnumerationLiteralExpression)


def test_eol::enumerationliteralexpression_constructor_exists():
    assert callable(eol::EnumerationLiteralExpression.__init__)


def test_eol::enumerationliteralexpression_constructor_args():
    sig = inspect.signature(eol::EnumerationLiteralExpression.__init__)
    params = list(sig.parameters.keys())



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



def test_eol::variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(eol::VariableDeclarationExpression)


def test_eol::variabledeclarationexpression_constructor_exists():
    assert callable(eol::VariableDeclarationExpression.__init__)


def test_eol::variabledeclarationexpression_constructor_args():
    sig = inspect.signature(eol::VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "create" in params, "Missing parameter 'create'"

def test_eol::variabledeclarationexpression_has_create():
    assert hasattr(eol::VariableDeclarationExpression, "create")
    descriptor = None
    for klass in eol::VariableDeclarationExpression.__mro__:
        if "create" in klass.__dict__:
            descriptor = klass.__dict__["create"]
            break
    assert isinstance(descriptor, property)



def test_eol::formalparameterexpression_is_not_abstract():
    assert not inspect.isabstract(eol::FormalParameterExpression)


def test_eol::formalparameterexpression_constructor_exists():
    assert callable(eol::FormalParameterExpression.__init__)


def test_eol::formalparameterexpression_constructor_args():
    sig = inspect.signature(eol::FormalParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::nameexpression_is_not_abstract():
    assert not inspect.isabstract(eol::NameExpression)


def test_eol::nameexpression_constructor_exists():
    assert callable(eol::NameExpression.__init__)


def test_eol::nameexpression_constructor_args():
    sig = inspect.signature(eol::NameExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isType" in params, "Missing parameter 'isType'"
    assert "resolvedContent" in params, "Missing parameter 'resolvedContent'"
    assert "name" in params, "Missing parameter 'name'"

def test_eol::nameexpression_has_isType():
    assert hasattr(eol::NameExpression, "isType")
    descriptor = None
    for klass in eol::NameExpression.__mro__:
        if "isType" in klass.__dict__:
            descriptor = klass.__dict__["isType"]
            break
    assert isinstance(descriptor, property)

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



def test_eol::greaterthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::GreaterThanOperatorExpression)


def test_eol::greaterthanoperatorexpression_constructor_exists():
    assert callable(eol::GreaterThanOperatorExpression.__init__)


def test_eol::greaterthanoperatorexpression_constructor_args():
    sig = inspect.signature(eol::GreaterThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::lessthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::LessThanOrEqualToOperatorExpression)


def test_eol::lessthanorequaltooperatorexpression_constructor_exists():
    assert callable(eol::LessThanOrEqualToOperatorExpression.__init__)


def test_eol::lessthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(eol::LessThanOrEqualToOperatorExpression.__init__)
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



def test_eol::greaterthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::GreaterThanOrEqualToOperatorExpression)


def test_eol::greaterthanorequaltooperatorexpression_constructor_exists():
    assert callable(eol::GreaterThanOrEqualToOperatorExpression.__init__)


def test_eol::greaterthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(eol::GreaterThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticOperatorExpression)


def test_arithmeticoperatorexpression_constructor_exists():
    assert callable(ArithmeticOperatorExpression.__init__)


def test_arithmeticoperatorexpression_constructor_args():
    sig = inspect.signature(ArithmeticOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::multiplyoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::MultiplyOperatorExpression)


def test_eol::multiplyoperatorexpression_constructor_exists():
    assert callable(eol::MultiplyOperatorExpression.__init__)


def test_eol::multiplyoperatorexpression_constructor_args():
    sig = inspect.signature(eol::MultiplyOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::minusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::MinusOperatorExpression)


def test_eol::minusoperatorexpression_constructor_exists():
    assert callable(eol::MinusOperatorExpression.__init__)


def test_eol::minusoperatorexpression_constructor_args():
    sig = inspect.signature(eol::MinusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::plusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::PlusOperatorExpression)


def test_eol::plusoperatorexpression_constructor_exists():
    assert callable(eol::PlusOperatorExpression.__init__)


def test_eol::plusoperatorexpression_constructor_args():
    sig = inspect.signature(eol::PlusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::divideoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::DivideOperatorExpression)


def test_eol::divideoperatorexpression_constructor_exists():
    assert callable(eol::DivideOperatorExpression.__init__)


def test_eol::divideoperatorexpression_constructor_args():
    sig = inspect.signature(eol::DivideOperatorExpression.__init__)
    params = list(sig.parameters.keys())



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



def test_eol::xoroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::XorOperatorExpression)


def test_eol::xoroperatorexpression_constructor_exists():
    assert callable(eol::XorOperatorExpression.__init__)


def test_eol::xoroperatorexpression_constructor_args():
    sig = inspect.signature(eol::XorOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::oroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::OrOperatorExpression)


def test_eol::oroperatorexpression_constructor_exists():
    assert callable(eol::OrOperatorExpression.__init__)


def test_eol::oroperatorexpression_constructor_args():
    sig = inspect.signature(eol::OrOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::andoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::AndOperatorExpression)


def test_eol::andoperatorexpression_constructor_exists():
    assert callable(eol::AndOperatorExpression.__init__)


def test_eol::andoperatorexpression_constructor_args():
    sig = inspect.signature(eol::AndOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOperatorExpression)


def test_binaryoperatorexpression_constructor_exists():
    assert callable(BinaryOperatorExpression.__init__)


def test_binaryoperatorexpression_constructor_args():
    sig = inspect.signature(BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::arithmeticoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::ArithmeticOperatorExpression)


def test_eol::arithmeticoperatorexpression_constructor_exists():
    assert callable(eol::ArithmeticOperatorExpression.__init__)


def test_eol::arithmeticoperatorexpression_constructor_args():
    sig = inspect.signature(eol::ArithmeticOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::ComparisonOperatorExpression)


def test_eol::comparisonoperatorexpression_constructor_exists():
    assert callable(eol::ComparisonOperatorExpression.__init__)


def test_eol::comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(eol::ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::logicaloperatorexpression_is_not_abstract():
    assert not inspect.isabstract(eol::LogicalOperatorExpression)


def test_eol::logicaloperatorexpression_constructor_exists():
    assert callable(eol::LogicalOperatorExpression.__init__)


def test_eol::logicaloperatorexpression_constructor_args():
    sig = inspect.signature(eol::LogicalOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_eol::annotationblock_is_not_abstract():
    assert not inspect.isabstract(eol::AnnotationBlock)


def test_eol::annotationblock_constructor_exists():
    assert callable(eol::AnnotationBlock.__init__)


def test_eol::annotationblock_constructor_args():
    sig = inspect.signature(eol::AnnotationBlock.__init__)
    params = list(sig.parameters.keys())



def test_eollibrarymodule_is_not_abstract():
    assert not inspect.isabstract(EOLLibraryModule)


def test_eollibrarymodule_constructor_exists():
    assert callable(EOLLibraryModule.__init__)


def test_eollibrarymodule_constructor_args():
    sig = inspect.signature(EOLLibraryModule.__init__)
    params = list(sig.parameters.keys())



def test_eol::eolmodule_is_not_abstract():
    assert not inspect.isabstract(eol::EOLModule)


def test_eol::eolmodule_constructor_exists():
    assert callable(eol::EOLModule.__init__)


def test_eol::eolmodule_constructor_args():
    sig = inspect.signature(eol::EOLModule.__init__)
    params = list(sig.parameters.keys())



def test_eol::modeldeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(eol::ModelDeclarationStatement)


def test_eol::modeldeclarationstatement_constructor_exists():
    assert callable(eol::ModelDeclarationStatement.__init__)


def test_eol::modeldeclarationstatement_constructor_args():
    sig = inspect.signature(eol::ModelDeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "resolvedIMetamodel" in params, "Missing parameter 'resolvedIMetamodel'"

def test_eol::modeldeclarationstatement_has_resolvedIMetamodel():
    assert hasattr(eol::ModelDeclarationStatement, "resolvedIMetamodel")
    descriptor = None
    for klass in eol::ModelDeclarationStatement.__mro__:
        if "resolvedIMetamodel" in klass.__dict__:
            descriptor = klass.__dict__["resolvedIMetamodel"]
            break
    assert isinstance(descriptor, property)



def test_eolelement_is_not_abstract():
    assert not inspect.isabstract(EOLElement)


def test_eolelement_constructor_exists():
    assert callable(EOLElement.__init__)


def test_eolelement_constructor_args():
    sig = inspect.signature(EOLElement.__init__)
    params = list(sig.parameters.keys())



def test_eol::expressionorstatementblock_is_not_abstract():
    assert not inspect.isabstract(eol::ExpressionOrStatementBlock)


def test_eol::expressionorstatementblock_constructor_exists():
    assert callable(eol::ExpressionOrStatementBlock.__init__)


def test_eol::expressionorstatementblock_constructor_args():
    sig = inspect.signature(eol::ExpressionOrStatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_eol::import_is_not_abstract():
    assert not inspect.isabstract(eol::Import)


def test_eol::import_constructor_exists():
    assert callable(eol::Import.__init__)


def test_eol::import_constructor_args():
    sig = inspect.signature(eol::Import.__init__)
    params = list(sig.parameters.keys())
    assert "imported" in params, "Missing parameter 'imported'"

def test_eol::import_has_imported():
    assert hasattr(eol::Import, "imported")
    descriptor = None
    for klass in eol::Import.__mro__:
        if "imported" in klass.__dict__:
            descriptor = klass.__dict__["imported"]
            break
    assert isinstance(descriptor, property)



def test_eol::operationdefinition_is_not_abstract():
    assert not inspect.isabstract(eol::OperationDefinition)


def test_eol::operationdefinition_constructor_exists():
    assert callable(eol::OperationDefinition.__init__)


def test_eol::operationdefinition_constructor_args():
    sig = inspect.signature(eol::OperationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_eol::statement_is_not_abstract():
    assert not inspect.isabstract(eol::Statement)


def test_eol::statement_constructor_exists():
    assert callable(eol::Statement.__init__)


def test_eol::statement_constructor_args():
    sig = inspect.signature(eol::Statement.__init__)
    params = list(sig.parameters.keys())



def test_eol::block_is_not_abstract():
    assert not inspect.isabstract(eol::Block)


def test_eol::block_constructor_exists():
    assert callable(eol::Block.__init__)


def test_eol::block_constructor_args():
    sig = inspect.signature(eol::Block.__init__)
    params = list(sig.parameters.keys())



def test_eol::eollibrarymodule_is_not_abstract():
    assert not inspect.isabstract(eol::EOLLibraryModule)


def test_eol::eollibrarymodule_constructor_exists():
    assert callable(eol::EOLLibraryModule.__init__)


def test_eol::eollibrarymodule_constructor_args():
    sig = inspect.signature(eol::EOLLibraryModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eol::eollibrarymodule_has_name():
    assert hasattr(eol::EOLLibraryModule, "name")
    descriptor = None
    for klass in eol::EOLLibraryModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eol::type_is_not_abstract():
    assert not inspect.isabstract(eol::Type)


def test_eol::type_constructor_exists():
    assert callable(eol::Type.__init__)


def test_eol::type_constructor_args():
    sig = inspect.signature(eol::Type.__init__)
    params = list(sig.parameters.keys())



def test_eol::expression_is_not_abstract():
    assert not inspect.isabstract(eol::Expression)


def test_eol::expression_constructor_exists():
    assert callable(eol::Expression.__init__)


def test_eol::expression_constructor_args():
    sig = inspect.signature(eol::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "inBrackets" in params, "Missing parameter 'inBrackets'"

def test_eol::expression_has_inBrackets():
    assert hasattr(eol::Expression, "inBrackets")
    descriptor = None
    for klass in eol::Expression.__mro__:
        if "inBrackets" in klass.__dict__:
            descriptor = klass.__dict__["inBrackets"]
            break
    assert isinstance(descriptor, property)



def test_eol::eolelement_is_not_abstract():
    assert not inspect.isabstract(eol::EOLElement)


def test_eol::eolelement_constructor_exists():
    assert callable(eol::EOLElement.__init__)


def test_eol::eolelement_constructor_args():
    sig = inspect.signature(eol::EOLElement.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_eol::eolelement_has_uri():
    assert hasattr(eol::EOLElement, "uri")
    descriptor = None
    for klass in eol::EOLElement.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_eol::textposition_is_not_abstract():
    assert not inspect.isabstract(eol::TextPosition)


def test_eol::textposition_constructor_exists():
    assert callable(eol::TextPosition.__init__)


def test_eol::textposition_constructor_args():
    sig = inspect.signature(eol::TextPosition.__init__)
    params = list(sig.parameters.keys())
    assert "line" in params, "Missing parameter 'line'"
    assert "column" in params, "Missing parameter 'column'"

def test_eol::textposition_has_line():
    assert hasattr(eol::TextPosition, "line")
    descriptor = None
    for klass in eol::TextPosition.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_eol::textposition_has_column():
    assert hasattr(eol::TextPosition, "column")
    descriptor = None
    for klass in eol::TextPosition.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)



def test_eol::textregion_is_not_abstract():
    assert not inspect.isabstract(eol::TextRegion)


def test_eol::textregion_constructor_exists():
    assert callable(eol::TextRegion.__init__)


def test_eol::textregion_constructor_args():
    sig = inspect.signature(eol::TextRegion.__init__)
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
SummablePrimitiveType_strategy = st.builds(
    SummablePrimitiveType,
)
ComparablePrimitiveType_strategy = st.builds(
    ComparablePrimitiveType,
)
eol::RealType_strategy = st.builds(
    eol::RealType,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
eol::BooleanType_strategy = st.builds(
    eol::BooleanType,
)
eol::SummablePrimitiveType_strategy = st.builds(
    eol::SummablePrimitiveType,
)
eol::ComparablePrimitiveType_strategy = st.builds(
    eol::ComparablePrimitiveType,
)
OrderedCollectionType_strategy = st.builds(
    OrderedCollectionType,
)
eol::SequenceType_strategy = st.builds(
    eol::SequenceType,
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
eol::StringType_strategy = st.builds(
    eol::StringType,
)
RealType_strategy = st.builds(
    RealType,
)
eol::IntegerType_strategy = st.builds(
    eol::IntegerType,
)
Type_strategy = st.builds(
    Type,
)
eol::AnyType_strategy = st.builds(
    eol::AnyType,
    declared=
        st.booleans()
)
AnnotationStatement_strategy = st.builds(
    AnnotationStatement,
)
eol::ExecutableAnnotationStatement_strategy = st.builds(
    eol::ExecutableAnnotationStatement,
)
eol::SimpleAnnotationStatement_strategy = st.builds(
    eol::SimpleAnnotationStatement,
)
AssignmentStatement_strategy = st.builds(
    AssignmentStatement,
)
eol::SpecialAssignmentStatement_strategy = st.builds(
    eol::SpecialAssignmentStatement,
)
PseudoType_strategy = st.builds(
    PseudoType,
)
eol::SelfContentType_strategy = st.builds(
    eol::SelfContentType,
)
eol::SelfType_strategy = st.builds(
    eol::SelfType,
)
AnyType_strategy = st.builds(
    AnyType,
)
eol::InvalidType_strategy = st.builds(
    eol::InvalidType,
)
eol::MapType_strategy = st.builds(
    eol::MapType,
)
eol::ModelElementType_strategy = st.builds(
    eol::ModelElementType,
    modelName=
        safe_text,
    resolvedIMetamodel=
        safe_text,
    resolvedIPackage=
        safe_text,
    elementName=
        safe_text,
    modelElementType=
        safe_text
)
eol::PseudoType_strategy = st.builds(
    eol::PseudoType,
)
eol::CollectionType_strategy = st.builds(
    eol::CollectionType,
)
eol::NativeType_strategy = st.builds(
    eol::NativeType,
)
eol::VoidType_strategy = st.builds(
    eol::VoidType,
)
eol::PrimitiveType_strategy = st.builds(
    eol::PrimitiveType,
)
eol::ModelType_strategy = st.builds(
    eol::ModelType,
    modelName=
        safe_text,
    resolvedIMetamodel=
        safe_text
)
SwitchCaseStatement_strategy = st.builds(
    SwitchCaseStatement,
)
Statement_strategy = st.builds(
    Statement,
)
eol::BreakAllStatement_strategy = st.builds(
    eol::BreakAllStatement,
)
eol::DeleteStatement_strategy = st.builds(
    eol::DeleteStatement,
)
eol::AbortStatement_strategy = st.builds(
    eol::AbortStatement,
)
eol::ThrowStatement_strategy = st.builds(
    eol::ThrowStatement,
)
eol::AssignmentStatement_strategy = st.builds(
    eol::AssignmentStatement,
)
eol::BreakStatement_strategy = st.builds(
    eol::BreakStatement,
)
eol::ReturnStatement_strategy = st.builds(
    eol::ReturnStatement,
)
eol::AnnotationStatement_strategy = st.builds(
    eol::AnnotationStatement,
)
eol::ContinueStatement_strategy = st.builds(
    eol::ContinueStatement,
)
eol::WhileStatement_strategy = st.builds(
    eol::WhileStatement,
)
eol::SwitchCaseStatement_strategy = st.builds(
    eol::SwitchCaseStatement,
)
eol::IfStatement_strategy = st.builds(
    eol::IfStatement,
)
eol::ForStatement_strategy = st.builds(
    eol::ForStatement,
)
eol::TransactionStatement_strategy = st.builds(
    eol::TransactionStatement,
)
CollectionInitialisationExpression_strategy = st.builds(
    CollectionInitialisationExpression,
)
eol::ExpressionList_strategy = st.builds(
    eol::ExpressionList,
)
eol::ExpressionRange_strategy = st.builds(
    eol::ExpressionRange,
)
OrderedCollection_strategy = st.builds(
    OrderedCollection,
)
eol::SequenceExpression_strategy = st.builds(
    eol::SequenceExpression,
)
UniqueCollection_strategy = st.builds(
    UniqueCollection,
)
eol::OrderedSetExpression_strategy = st.builds(
    eol::OrderedSetExpression,
)
eol::SetExpression_strategy = st.builds(
    eol::SetExpression,
)
CollectionExpression_strategy = st.builds(
    CollectionExpression,
)
eol::UniqueCollection_strategy = st.builds(
    eol::UniqueCollection,
)
eol::OrderedCollection_strategy = st.builds(
    eol::OrderedCollection,
)
eol::BagExpression_strategy = st.builds(
    eol::BagExpression,
)
eol::SwitchCaseDefaultStatement_strategy = st.builds(
    eol::SwitchCaseDefaultStatement,
)
eol::SwitchCaseExpressionStatement_strategy = st.builds(
    eol::SwitchCaseExpressionStatement,
)
eol::SwitchStatement_strategy = st.builds(
    eol::SwitchStatement,
)
eol::ExpressionStatement_strategy = st.builds(
    eol::ExpressionStatement,
)
SummableExpression_strategy = st.builds(
    SummableExpression,
)
ComparableExpression_strategy = st.builds(
    ComparableExpression,
)
eol::RealExpression_strategy = st.builds(
    eol::RealExpression,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
eol::IntegerExpression_strategy = st.builds(
    eol::IntegerExpression,
    value=
        st.integers()
)
eol::StringExpression_strategy = st.builds(
    eol::StringExpression,
    value=
        safe_text
)
PrimitiveExpression_strategy = st.builds(
    PrimitiveExpression,
)
eol::SummableExpression_strategy = st.builds(
    eol::SummableExpression,
)
eol::BooleanExpression_strategy = st.builds(
    eol::BooleanExpression,
    value=
        st.booleans()
)
eol::ComparableExpression_strategy = st.builds(
    eol::ComparableExpression,
)
FeatureCallExpression_strategy = st.builds(
    FeatureCallExpression,
)
eol::FOLMethodCallExpression_strategy = st.builds(
    eol::FOLMethodCallExpression,
)
eol::PropertyCallExpression_strategy = st.builds(
    eol::PropertyCallExpression,
    extended=
        st.booleans()
)
eol::MethodCallExpression_strategy = st.builds(
    eol::MethodCallExpression,
)
VariableDeclarationExpression_strategy = st.builds(
    VariableDeclarationExpression,
)
KeyValueExpression_strategy = st.builds(
    KeyValueExpression,
)
eol::ModelDeclarationParameter_strategy = st.builds(
    eol::ModelDeclarationParameter,
)
UnaryOperatorExpression_strategy = st.builds(
    UnaryOperatorExpression,
)
eol::NegativeOperatorExpression_strategy = st.builds(
    eol::NegativeOperatorExpression,
)
eol::NotOperatorExpression_strategy = st.builds(
    eol::NotOperatorExpression,
)
OperatorExpression_strategy = st.builds(
    OperatorExpression,
)
eol::BinaryOperatorExpression_strategy = st.builds(
    eol::BinaryOperatorExpression,
)
eol::UnaryOperatorExpression_strategy = st.builds(
    eol::UnaryOperatorExpression,
)
Expression_strategy = st.builds(
    Expression,
)
eol::CollectionInitialisationExpression_strategy = st.builds(
    eol::CollectionInitialisationExpression,
)
eol::KeyValueExpression_strategy = st.builds(
    eol::KeyValueExpression,
)
eol::CollectionExpression_strategy = st.builds(
    eol::CollectionExpression,
)
eol::PrimitiveExpression_strategy = st.builds(
    eol::PrimitiveExpression,
)
eol::MapExpression_strategy = st.builds(
    eol::MapExpression,
)
eol::FeatureCallExpression_strategy = st.builds(
    eol::FeatureCallExpression,
    arrow=
        st.booleans()
)
eol::EnumerationLiteralExpression_strategy = st.builds(
    eol::EnumerationLiteralExpression,
)
eol::NewExpression_strategy = st.builds(
    eol::NewExpression,
)
eol::OperatorExpression_strategy = st.builds(
    eol::OperatorExpression,
)
eol::VariableDeclarationExpression_strategy = st.builds(
    eol::VariableDeclarationExpression,
    create=
        st.booleans()
)
eol::FormalParameterExpression_strategy = st.builds(
    eol::FormalParameterExpression,
)
eol::NameExpression_strategy = st.builds(
    eol::NameExpression,
    isType=
        st.booleans(),
    resolvedContent=
        safe_text,
    name=
        safe_text
)
ComparisonOperatorExpression_strategy = st.builds(
    ComparisonOperatorExpression,
)
eol::NotEqualsOperatorExpression_strategy = st.builds(
    eol::NotEqualsOperatorExpression,
)
eol::GreaterThanOperatorExpression_strategy = st.builds(
    eol::GreaterThanOperatorExpression,
)
eol::LessThanOrEqualToOperatorExpression_strategy = st.builds(
    eol::LessThanOrEqualToOperatorExpression,
)
eol::LessThanOperatorExpression_strategy = st.builds(
    eol::LessThanOperatorExpression,
)
eol::EqualsOperatorExpression_strategy = st.builds(
    eol::EqualsOperatorExpression,
)
eol::GreaterThanOrEqualToOperatorExpression_strategy = st.builds(
    eol::GreaterThanOrEqualToOperatorExpression,
)
ArithmeticOperatorExpression_strategy = st.builds(
    ArithmeticOperatorExpression,
)
eol::MultiplyOperatorExpression_strategy = st.builds(
    eol::MultiplyOperatorExpression,
)
eol::MinusOperatorExpression_strategy = st.builds(
    eol::MinusOperatorExpression,
)
eol::PlusOperatorExpression_strategy = st.builds(
    eol::PlusOperatorExpression,
)
eol::DivideOperatorExpression_strategy = st.builds(
    eol::DivideOperatorExpression,
)
LogicalOperatorExpression_strategy = st.builds(
    LogicalOperatorExpression,
)
eol::ImpliesOperatorExpression_strategy = st.builds(
    eol::ImpliesOperatorExpression,
)
eol::XorOperatorExpression_strategy = st.builds(
    eol::XorOperatorExpression,
)
eol::OrOperatorExpression_strategy = st.builds(
    eol::OrOperatorExpression,
)
eol::AndOperatorExpression_strategy = st.builds(
    eol::AndOperatorExpression,
)
BinaryOperatorExpression_strategy = st.builds(
    BinaryOperatorExpression,
)
eol::ArithmeticOperatorExpression_strategy = st.builds(
    eol::ArithmeticOperatorExpression,
)
eol::ComparisonOperatorExpression_strategy = st.builds(
    eol::ComparisonOperatorExpression,
)
eol::LogicalOperatorExpression_strategy = st.builds(
    eol::LogicalOperatorExpression,
)
Block_strategy = st.builds(
    Block,
)
eol::AnnotationBlock_strategy = st.builds(
    eol::AnnotationBlock,
)
EOLLibraryModule_strategy = st.builds(
    EOLLibraryModule,
)
eol::EOLModule_strategy = st.builds(
    eol::EOLModule,
)
eol::ModelDeclarationStatement_strategy = st.builds(
    eol::ModelDeclarationStatement,
    resolvedIMetamodel=
        safe_text
)
EOLElement_strategy = st.builds(
    EOLElement,
)
eol::ExpressionOrStatementBlock_strategy = st.builds(
    eol::ExpressionOrStatementBlock,
)
eol::Import_strategy = st.builds(
    eol::Import,
    imported=
        safe_text
)
eol::OperationDefinition_strategy = st.builds(
    eol::OperationDefinition,
)
eol::Statement_strategy = st.builds(
    eol::Statement,
)
eol::Block_strategy = st.builds(
    eol::Block,
)
eol::EOLLibraryModule_strategy = st.builds(
    eol::EOLLibraryModule,
    name=
        safe_text
)
eol::Type_strategy = st.builds(
    eol::Type,
)
eol::Expression_strategy = st.builds(
    eol::Expression,
    inBrackets=
        st.booleans()
)
eol::EOLElement_strategy = st.builds(
    eol::EOLElement,
    uri=
        safe_text
)
eol::TextPosition_strategy = st.builds(
    eol::TextPosition,
    line=
        st.integers(),
    column=
        st.integers()
)
eol::TextRegion_strategy = st.builds(
    eol::TextRegion,
)

@given(instance=SummablePrimitiveType_strategy)
@settings(max_examples=50)
def test_summableprimitivetype_instantiation(instance):
    assert isinstance(instance, SummablePrimitiveType)

@given(instance=ComparablePrimitiveType_strategy)
@settings(max_examples=50)
def test_comparableprimitivetype_instantiation(instance):
    assert isinstance(instance, ComparablePrimitiveType)

@given(instance=eol::RealType_strategy)
@settings(max_examples=50)
def test_eol::realtype_instantiation(instance):
    assert isinstance(instance, eol::RealType)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=eol::BooleanType_strategy)
@settings(max_examples=50)
def test_eol::booleantype_instantiation(instance):
    assert isinstance(instance, eol::BooleanType)

@given(instance=eol::SummablePrimitiveType_strategy)
@settings(max_examples=50)
def test_eol::summableprimitivetype_instantiation(instance):
    assert isinstance(instance, eol::SummablePrimitiveType)

@given(instance=eol::ComparablePrimitiveType_strategy)
@settings(max_examples=50)
def test_eol::comparableprimitivetype_instantiation(instance):
    assert isinstance(instance, eol::ComparablePrimitiveType)

@given(instance=OrderedCollectionType_strategy)
@settings(max_examples=50)
def test_orderedcollectiontype_instantiation(instance):
    assert isinstance(instance, OrderedCollectionType)

@given(instance=eol::SequenceType_strategy)
@settings(max_examples=50)
def test_eol::sequencetype_instantiation(instance):
    assert isinstance(instance, eol::SequenceType)

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

@given(instance=eol::StringType_strategy)
@settings(max_examples=50)
def test_eol::stringtype_instantiation(instance):
    assert isinstance(instance, eol::StringType)

@given(instance=RealType_strategy)
@settings(max_examples=50)
def test_realtype_instantiation(instance):
    assert isinstance(instance, RealType)

@given(instance=eol::IntegerType_strategy)
@settings(max_examples=50)
def test_eol::integertype_instantiation(instance):
    assert isinstance(instance, eol::IntegerType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

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

@given(instance=AnnotationStatement_strategy)
@settings(max_examples=50)
def test_annotationstatement_instantiation(instance):
    assert isinstance(instance, AnnotationStatement)

@given(instance=eol::ExecutableAnnotationStatement_strategy)
@settings(max_examples=50)
def test_eol::executableannotationstatement_instantiation(instance):
    assert isinstance(instance, eol::ExecutableAnnotationStatement)

@given(instance=eol::SimpleAnnotationStatement_strategy)
@settings(max_examples=50)
def test_eol::simpleannotationstatement_instantiation(instance):
    assert isinstance(instance, eol::SimpleAnnotationStatement)

@given(instance=AssignmentStatement_strategy)
@settings(max_examples=50)
def test_assignmentstatement_instantiation(instance):
    assert isinstance(instance, AssignmentStatement)

@given(instance=eol::SpecialAssignmentStatement_strategy)
@settings(max_examples=50)
def test_eol::specialassignmentstatement_instantiation(instance):
    assert isinstance(instance, eol::SpecialAssignmentStatement)

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

@given(instance=AnyType_strategy)
@settings(max_examples=50)
def test_anytype_instantiation(instance):
    assert isinstance(instance, AnyType)

@given(instance=eol::InvalidType_strategy)
@settings(max_examples=50)
def test_eol::invalidtype_instantiation(instance):
    assert isinstance(instance, eol::InvalidType)

@given(instance=eol::MapType_strategy)
@settings(max_examples=50)
def test_eol::maptype_instantiation(instance):
    assert isinstance(instance, eol::MapType)

@given(instance=eol::ModelElementType_strategy)
@settings(max_examples=50)
def test_eol::modelelementtype_instantiation(instance):
    assert isinstance(instance, eol::ModelElementType)

@given(instance=eol::ModelElementType_strategy)
def test_eol::modelelementtype_modelName_type(instance):
    assert isinstance(instance.modelName, str)


@given(instance=eol::ModelElementType_strategy)
def test_eol::modelelementtype_modelName_setter(instance):
    original = instance.modelName
    instance.modelName = original
    assert instance.modelName == original

@given(instance=eol::ModelElementType_strategy)
def test_eol::modelelementtype_resolvedIMetamodel_type(instance):
    assert isinstance(instance.resolvedIMetamodel, str)


@given(instance=eol::ModelElementType_strategy)
def test_eol::modelelementtype_resolvedIMetamodel_setter(instance):
    original = instance.resolvedIMetamodel
    instance.resolvedIMetamodel = original
    assert instance.resolvedIMetamodel == original

@given(instance=eol::ModelElementType_strategy)
def test_eol::modelelementtype_resolvedIPackage_type(instance):
    assert isinstance(instance.resolvedIPackage, str)


@given(instance=eol::ModelElementType_strategy)
def test_eol::modelelementtype_resolvedIPackage_setter(instance):
    original = instance.resolvedIPackage
    instance.resolvedIPackage = original
    assert instance.resolvedIPackage == original

@given(instance=eol::ModelElementType_strategy)
def test_eol::modelelementtype_elementName_type(instance):
    assert isinstance(instance.elementName, str)


@given(instance=eol::ModelElementType_strategy)
def test_eol::modelelementtype_elementName_setter(instance):
    original = instance.elementName
    instance.elementName = original
    assert instance.elementName == original

@given(instance=eol::ModelElementType_strategy)
def test_eol::modelelementtype_modelElementType_type(instance):
    assert isinstance(instance.modelElementType, str)


@given(instance=eol::ModelElementType_strategy)
def test_eol::modelelementtype_modelElementType_setter(instance):
    original = instance.modelElementType
    instance.modelElementType = original
    assert instance.modelElementType == original

@given(instance=eol::PseudoType_strategy)
@settings(max_examples=50)
def test_eol::pseudotype_instantiation(instance):
    assert isinstance(instance, eol::PseudoType)

@given(instance=eol::CollectionType_strategy)
@settings(max_examples=50)
def test_eol::collectiontype_instantiation(instance):
    assert isinstance(instance, eol::CollectionType)

@given(instance=eol::NativeType_strategy)
@settings(max_examples=50)
def test_eol::nativetype_instantiation(instance):
    assert isinstance(instance, eol::NativeType)

@given(instance=eol::VoidType_strategy)
@settings(max_examples=50)
def test_eol::voidtype_instantiation(instance):
    assert isinstance(instance, eol::VoidType)

@given(instance=eol::PrimitiveType_strategy)
@settings(max_examples=50)
def test_eol::primitivetype_instantiation(instance):
    assert isinstance(instance, eol::PrimitiveType)

@given(instance=eol::ModelType_strategy)
@settings(max_examples=50)
def test_eol::modeltype_instantiation(instance):
    assert isinstance(instance, eol::ModelType)

@given(instance=eol::ModelType_strategy)
def test_eol::modeltype_modelName_type(instance):
    assert isinstance(instance.modelName, str)


@given(instance=eol::ModelType_strategy)
def test_eol::modeltype_modelName_setter(instance):
    original = instance.modelName
    instance.modelName = original
    assert instance.modelName == original

@given(instance=eol::ModelType_strategy)
def test_eol::modeltype_resolvedIMetamodel_type(instance):
    assert isinstance(instance.resolvedIMetamodel, str)


@given(instance=eol::ModelType_strategy)
def test_eol::modeltype_resolvedIMetamodel_setter(instance):
    original = instance.resolvedIMetamodel
    instance.resolvedIMetamodel = original
    assert instance.resolvedIMetamodel == original

@given(instance=SwitchCaseStatement_strategy)
@settings(max_examples=50)
def test_switchcasestatement_instantiation(instance):
    assert isinstance(instance, SwitchCaseStatement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=eol::BreakAllStatement_strategy)
@settings(max_examples=50)
def test_eol::breakallstatement_instantiation(instance):
    assert isinstance(instance, eol::BreakAllStatement)

@given(instance=eol::DeleteStatement_strategy)
@settings(max_examples=50)
def test_eol::deletestatement_instantiation(instance):
    assert isinstance(instance, eol::DeleteStatement)

@given(instance=eol::AbortStatement_strategy)
@settings(max_examples=50)
def test_eol::abortstatement_instantiation(instance):
    assert isinstance(instance, eol::AbortStatement)

@given(instance=eol::ThrowStatement_strategy)
@settings(max_examples=50)
def test_eol::throwstatement_instantiation(instance):
    assert isinstance(instance, eol::ThrowStatement)

@given(instance=eol::AssignmentStatement_strategy)
@settings(max_examples=50)
def test_eol::assignmentstatement_instantiation(instance):
    assert isinstance(instance, eol::AssignmentStatement)

@given(instance=eol::BreakStatement_strategy)
@settings(max_examples=50)
def test_eol::breakstatement_instantiation(instance):
    assert isinstance(instance, eol::BreakStatement)

@given(instance=eol::ReturnStatement_strategy)
@settings(max_examples=50)
def test_eol::returnstatement_instantiation(instance):
    assert isinstance(instance, eol::ReturnStatement)

@given(instance=eol::AnnotationStatement_strategy)
@settings(max_examples=50)
def test_eol::annotationstatement_instantiation(instance):
    assert isinstance(instance, eol::AnnotationStatement)

@given(instance=eol::ContinueStatement_strategy)
@settings(max_examples=50)
def test_eol::continuestatement_instantiation(instance):
    assert isinstance(instance, eol::ContinueStatement)

@given(instance=eol::WhileStatement_strategy)
@settings(max_examples=50)
def test_eol::whilestatement_instantiation(instance):
    assert isinstance(instance, eol::WhileStatement)

@given(instance=eol::SwitchCaseStatement_strategy)
@settings(max_examples=50)
def test_eol::switchcasestatement_instantiation(instance):
    assert isinstance(instance, eol::SwitchCaseStatement)

@given(instance=eol::IfStatement_strategy)
@settings(max_examples=50)
def test_eol::ifstatement_instantiation(instance):
    assert isinstance(instance, eol::IfStatement)

@given(instance=eol::ForStatement_strategy)
@settings(max_examples=50)
def test_eol::forstatement_instantiation(instance):
    assert isinstance(instance, eol::ForStatement)

@given(instance=eol::TransactionStatement_strategy)
@settings(max_examples=50)
def test_eol::transactionstatement_instantiation(instance):
    assert isinstance(instance, eol::TransactionStatement)

@given(instance=CollectionInitialisationExpression_strategy)
@settings(max_examples=50)
def test_collectioninitialisationexpression_instantiation(instance):
    assert isinstance(instance, CollectionInitialisationExpression)

@given(instance=eol::ExpressionList_strategy)
@settings(max_examples=50)
def test_eol::expressionlist_instantiation(instance):
    assert isinstance(instance, eol::ExpressionList)

@given(instance=eol::ExpressionRange_strategy)
@settings(max_examples=50)
def test_eol::expressionrange_instantiation(instance):
    assert isinstance(instance, eol::ExpressionRange)

@given(instance=OrderedCollection_strategy)
@settings(max_examples=50)
def test_orderedcollection_instantiation(instance):
    assert isinstance(instance, OrderedCollection)

@given(instance=eol::SequenceExpression_strategy)
@settings(max_examples=50)
def test_eol::sequenceexpression_instantiation(instance):
    assert isinstance(instance, eol::SequenceExpression)

@given(instance=UniqueCollection_strategy)
@settings(max_examples=50)
def test_uniquecollection_instantiation(instance):
    assert isinstance(instance, UniqueCollection)

@given(instance=eol::OrderedSetExpression_strategy)
@settings(max_examples=50)
def test_eol::orderedsetexpression_instantiation(instance):
    assert isinstance(instance, eol::OrderedSetExpression)

@given(instance=eol::SetExpression_strategy)
@settings(max_examples=50)
def test_eol::setexpression_instantiation(instance):
    assert isinstance(instance, eol::SetExpression)

@given(instance=CollectionExpression_strategy)
@settings(max_examples=50)
def test_collectionexpression_instantiation(instance):
    assert isinstance(instance, CollectionExpression)

@given(instance=eol::UniqueCollection_strategy)
@settings(max_examples=50)
def test_eol::uniquecollection_instantiation(instance):
    assert isinstance(instance, eol::UniqueCollection)

@given(instance=eol::OrderedCollection_strategy)
@settings(max_examples=50)
def test_eol::orderedcollection_instantiation(instance):
    assert isinstance(instance, eol::OrderedCollection)

@given(instance=eol::BagExpression_strategy)
@settings(max_examples=50)
def test_eol::bagexpression_instantiation(instance):
    assert isinstance(instance, eol::BagExpression)

@given(instance=eol::SwitchCaseDefaultStatement_strategy)
@settings(max_examples=50)
def test_eol::switchcasedefaultstatement_instantiation(instance):
    assert isinstance(instance, eol::SwitchCaseDefaultStatement)

@given(instance=eol::SwitchCaseExpressionStatement_strategy)
@settings(max_examples=50)
def test_eol::switchcaseexpressionstatement_instantiation(instance):
    assert isinstance(instance, eol::SwitchCaseExpressionStatement)

@given(instance=eol::SwitchStatement_strategy)
@settings(max_examples=50)
def test_eol::switchstatement_instantiation(instance):
    assert isinstance(instance, eol::SwitchStatement)

@given(instance=eol::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_eol::expressionstatement_instantiation(instance):
    assert isinstance(instance, eol::ExpressionStatement)

@given(instance=SummableExpression_strategy)
@settings(max_examples=50)
def test_summableexpression_instantiation(instance):
    assert isinstance(instance, SummableExpression)

@given(instance=ComparableExpression_strategy)
@settings(max_examples=50)
def test_comparableexpression_instantiation(instance):
    assert isinstance(instance, ComparableExpression)

@given(instance=eol::RealExpression_strategy)
@settings(max_examples=50)
def test_eol::realexpression_instantiation(instance):
    assert isinstance(instance, eol::RealExpression)

@given(instance=eol::RealExpression_strategy)
def test_eol::realexpression_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=eol::RealExpression_strategy)
def test_eol::realexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eol::IntegerExpression_strategy)
@settings(max_examples=50)
def test_eol::integerexpression_instantiation(instance):
    assert isinstance(instance, eol::IntegerExpression)

@given(instance=eol::IntegerExpression_strategy)
def test_eol::integerexpression_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=eol::IntegerExpression_strategy)
def test_eol::integerexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eol::StringExpression_strategy)
@settings(max_examples=50)
def test_eol::stringexpression_instantiation(instance):
    assert isinstance(instance, eol::StringExpression)

@given(instance=eol::StringExpression_strategy)
def test_eol::stringexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=eol::StringExpression_strategy)
def test_eol::stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_primitiveexpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)

@given(instance=eol::SummableExpression_strategy)
@settings(max_examples=50)
def test_eol::summableexpression_instantiation(instance):
    assert isinstance(instance, eol::SummableExpression)

@given(instance=eol::BooleanExpression_strategy)
@settings(max_examples=50)
def test_eol::booleanexpression_instantiation(instance):
    assert isinstance(instance, eol::BooleanExpression)

@given(instance=eol::BooleanExpression_strategy)
def test_eol::booleanexpression_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=eol::BooleanExpression_strategy)
def test_eol::booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eol::ComparableExpression_strategy)
@settings(max_examples=50)
def test_eol::comparableexpression_instantiation(instance):
    assert isinstance(instance, eol::ComparableExpression)

@given(instance=FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_featurecallexpression_instantiation(instance):
    assert isinstance(instance, FeatureCallExpression)

@given(instance=eol::FOLMethodCallExpression_strategy)
@settings(max_examples=50)
def test_eol::folmethodcallexpression_instantiation(instance):
    assert isinstance(instance, eol::FOLMethodCallExpression)

@given(instance=eol::PropertyCallExpression_strategy)
@settings(max_examples=50)
def test_eol::propertycallexpression_instantiation(instance):
    assert isinstance(instance, eol::PropertyCallExpression)

@given(instance=eol::PropertyCallExpression_strategy)
def test_eol::propertycallexpression_extended_type(instance):
    assert isinstance(instance.extended, bool)


@given(instance=eol::PropertyCallExpression_strategy)
def test_eol::propertycallexpression_extended_setter(instance):
    original = instance.extended
    instance.extended = original
    assert instance.extended == original

@given(instance=eol::MethodCallExpression_strategy)
@settings(max_examples=50)
def test_eol::methodcallexpression_instantiation(instance):
    assert isinstance(instance, eol::MethodCallExpression)

@given(instance=VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, VariableDeclarationExpression)

@given(instance=KeyValueExpression_strategy)
@settings(max_examples=50)
def test_keyvalueexpression_instantiation(instance):
    assert isinstance(instance, KeyValueExpression)

@given(instance=eol::ModelDeclarationParameter_strategy)
@settings(max_examples=50)
def test_eol::modeldeclarationparameter_instantiation(instance):
    assert isinstance(instance, eol::ModelDeclarationParameter)

@given(instance=UnaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_unaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, UnaryOperatorExpression)

@given(instance=eol::NegativeOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::negativeoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::NegativeOperatorExpression)

@given(instance=eol::NotOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::notoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::NotOperatorExpression)

@given(instance=OperatorExpression_strategy)
@settings(max_examples=50)
def test_operatorexpression_instantiation(instance):
    assert isinstance(instance, OperatorExpression)

@given(instance=eol::BinaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::binaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::BinaryOperatorExpression)

@given(instance=eol::UnaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::unaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::UnaryOperatorExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=eol::CollectionInitialisationExpression_strategy)
@settings(max_examples=50)
def test_eol::collectioninitialisationexpression_instantiation(instance):
    assert isinstance(instance, eol::CollectionInitialisationExpression)

@given(instance=eol::KeyValueExpression_strategy)
@settings(max_examples=50)
def test_eol::keyvalueexpression_instantiation(instance):
    assert isinstance(instance, eol::KeyValueExpression)

@given(instance=eol::CollectionExpression_strategy)
@settings(max_examples=50)
def test_eol::collectionexpression_instantiation(instance):
    assert isinstance(instance, eol::CollectionExpression)

@given(instance=eol::PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_eol::primitiveexpression_instantiation(instance):
    assert isinstance(instance, eol::PrimitiveExpression)

@given(instance=eol::MapExpression_strategy)
@settings(max_examples=50)
def test_eol::mapexpression_instantiation(instance):
    assert isinstance(instance, eol::MapExpression)

@given(instance=eol::FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_eol::featurecallexpression_instantiation(instance):
    assert isinstance(instance, eol::FeatureCallExpression)

@given(instance=eol::FeatureCallExpression_strategy)
def test_eol::featurecallexpression_arrow_type(instance):
    assert isinstance(instance.arrow, bool)


@given(instance=eol::FeatureCallExpression_strategy)
def test_eol::featurecallexpression_arrow_setter(instance):
    original = instance.arrow
    instance.arrow = original
    assert instance.arrow == original

@given(instance=eol::EnumerationLiteralExpression_strategy)
@settings(max_examples=50)
def test_eol::enumerationliteralexpression_instantiation(instance):
    assert isinstance(instance, eol::EnumerationLiteralExpression)

@given(instance=eol::NewExpression_strategy)
@settings(max_examples=50)
def test_eol::newexpression_instantiation(instance):
    assert isinstance(instance, eol::NewExpression)

@given(instance=eol::OperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::operatorexpression_instantiation(instance):
    assert isinstance(instance, eol::OperatorExpression)

@given(instance=eol::VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_eol::variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, eol::VariableDeclarationExpression)

@given(instance=eol::VariableDeclarationExpression_strategy)
def test_eol::variabledeclarationexpression_create_type(instance):
    assert isinstance(instance.create, bool)


@given(instance=eol::VariableDeclarationExpression_strategy)
def test_eol::variabledeclarationexpression_create_setter(instance):
    original = instance.create
    instance.create = original
    assert instance.create == original

@given(instance=eol::FormalParameterExpression_strategy)
@settings(max_examples=50)
def test_eol::formalparameterexpression_instantiation(instance):
    assert isinstance(instance, eol::FormalParameterExpression)

@given(instance=eol::NameExpression_strategy)
@settings(max_examples=50)
def test_eol::nameexpression_instantiation(instance):
    assert isinstance(instance, eol::NameExpression)

@given(instance=eol::NameExpression_strategy)
def test_eol::nameexpression_isType_type(instance):
    assert isinstance(instance.isType, bool)


@given(instance=eol::NameExpression_strategy)
def test_eol::nameexpression_isType_setter(instance):
    original = instance.isType
    instance.isType = original
    assert instance.isType == original

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

@given(instance=ComparisonOperatorExpression_strategy)
@settings(max_examples=50)
def test_comparisonoperatorexpression_instantiation(instance):
    assert isinstance(instance, ComparisonOperatorExpression)

@given(instance=eol::NotEqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::notequalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::NotEqualsOperatorExpression)

@given(instance=eol::GreaterThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::greaterthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::GreaterThanOperatorExpression)

@given(instance=eol::LessThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::lessthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::LessThanOrEqualToOperatorExpression)

@given(instance=eol::LessThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::lessthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::LessThanOperatorExpression)

@given(instance=eol::EqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::equalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::EqualsOperatorExpression)

@given(instance=eol::GreaterThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::greaterthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::GreaterThanOrEqualToOperatorExpression)

@given(instance=ArithmeticOperatorExpression_strategy)
@settings(max_examples=50)
def test_arithmeticoperatorexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticOperatorExpression)

@given(instance=eol::MultiplyOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::multiplyoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::MultiplyOperatorExpression)

@given(instance=eol::MinusOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::minusoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::MinusOperatorExpression)

@given(instance=eol::PlusOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::plusoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::PlusOperatorExpression)

@given(instance=eol::DivideOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::divideoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::DivideOperatorExpression)

@given(instance=LogicalOperatorExpression_strategy)
@settings(max_examples=50)
def test_logicaloperatorexpression_instantiation(instance):
    assert isinstance(instance, LogicalOperatorExpression)

@given(instance=eol::ImpliesOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::impliesoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::ImpliesOperatorExpression)

@given(instance=eol::XorOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::xoroperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::XorOperatorExpression)

@given(instance=eol::OrOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::oroperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::OrOperatorExpression)

@given(instance=eol::AndOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::andoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::AndOperatorExpression)

@given(instance=BinaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_binaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, BinaryOperatorExpression)

@given(instance=eol::ArithmeticOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::arithmeticoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::ArithmeticOperatorExpression)

@given(instance=eol::ComparisonOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::comparisonoperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::ComparisonOperatorExpression)

@given(instance=eol::LogicalOperatorExpression_strategy)
@settings(max_examples=50)
def test_eol::logicaloperatorexpression_instantiation(instance):
    assert isinstance(instance, eol::LogicalOperatorExpression)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=eol::AnnotationBlock_strategy)
@settings(max_examples=50)
def test_eol::annotationblock_instantiation(instance):
    assert isinstance(instance, eol::AnnotationBlock)

@given(instance=EOLLibraryModule_strategy)
@settings(max_examples=50)
def test_eollibrarymodule_instantiation(instance):
    assert isinstance(instance, EOLLibraryModule)

@given(instance=eol::EOLModule_strategy)
@settings(max_examples=50)
def test_eol::eolmodule_instantiation(instance):
    assert isinstance(instance, eol::EOLModule)

@given(instance=eol::ModelDeclarationStatement_strategy)
@settings(max_examples=50)
def test_eol::modeldeclarationstatement_instantiation(instance):
    assert isinstance(instance, eol::ModelDeclarationStatement)

@given(instance=eol::ModelDeclarationStatement_strategy)
def test_eol::modeldeclarationstatement_resolvedIMetamodel_type(instance):
    assert isinstance(instance.resolvedIMetamodel, str)


@given(instance=eol::ModelDeclarationStatement_strategy)
def test_eol::modeldeclarationstatement_resolvedIMetamodel_setter(instance):
    original = instance.resolvedIMetamodel
    instance.resolvedIMetamodel = original
    assert instance.resolvedIMetamodel == original

@given(instance=EOLElement_strategy)
@settings(max_examples=50)
def test_eolelement_instantiation(instance):
    assert isinstance(instance, EOLElement)

@given(instance=eol::ExpressionOrStatementBlock_strategy)
@settings(max_examples=50)
def test_eol::expressionorstatementblock_instantiation(instance):
    assert isinstance(instance, eol::ExpressionOrStatementBlock)

@given(instance=eol::Import_strategy)
@settings(max_examples=50)
def test_eol::import_instantiation(instance):
    assert isinstance(instance, eol::Import)

@given(instance=eol::Import_strategy)
def test_eol::import_imported_type(instance):
    assert isinstance(instance.imported, str)


@given(instance=eol::Import_strategy)
def test_eol::import_imported_setter(instance):
    original = instance.imported
    instance.imported = original
    assert instance.imported == original

@given(instance=eol::OperationDefinition_strategy)
@settings(max_examples=50)
def test_eol::operationdefinition_instantiation(instance):
    assert isinstance(instance, eol::OperationDefinition)

@given(instance=eol::Statement_strategy)
@settings(max_examples=50)
def test_eol::statement_instantiation(instance):
    assert isinstance(instance, eol::Statement)

@given(instance=eol::Block_strategy)
@settings(max_examples=50)
def test_eol::block_instantiation(instance):
    assert isinstance(instance, eol::Block)

@given(instance=eol::EOLLibraryModule_strategy)
@settings(max_examples=50)
def test_eol::eollibrarymodule_instantiation(instance):
    assert isinstance(instance, eol::EOLLibraryModule)

@given(instance=eol::EOLLibraryModule_strategy)
def test_eol::eollibrarymodule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eol::EOLLibraryModule_strategy)
def test_eol::eollibrarymodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eol::Type_strategy)
@settings(max_examples=50)
def test_eol::type_instantiation(instance):
    assert isinstance(instance, eol::Type)

@given(instance=eol::Expression_strategy)
@settings(max_examples=50)
def test_eol::expression_instantiation(instance):
    assert isinstance(instance, eol::Expression)

@given(instance=eol::Expression_strategy)
def test_eol::expression_inBrackets_type(instance):
    assert isinstance(instance.inBrackets, bool)


@given(instance=eol::Expression_strategy)
def test_eol::expression_inBrackets_setter(instance):
    original = instance.inBrackets
    instance.inBrackets = original
    assert instance.inBrackets == original

@given(instance=eol::EOLElement_strategy)
@settings(max_examples=50)
def test_eol::eolelement_instantiation(instance):
    assert isinstance(instance, eol::EOLElement)

@given(instance=eol::EOLElement_strategy)
def test_eol::eolelement_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=eol::EOLElement_strategy)
def test_eol::eolelement_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=eol::TextPosition_strategy)
@settings(max_examples=50)
def test_eol::textposition_instantiation(instance):
    assert isinstance(instance, eol::TextPosition)

@given(instance=eol::TextPosition_strategy)
def test_eol::textposition_line_type(instance):
    assert isinstance(instance.line, int)


@given(instance=eol::TextPosition_strategy)
def test_eol::textposition_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=eol::TextPosition_strategy)
def test_eol::textposition_column_type(instance):
    assert isinstance(instance.column, int)


@given(instance=eol::TextPosition_strategy)
def test_eol::textposition_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=eol::TextRegion_strategy)
@settings(max_examples=50)
def test_eol::textregion_instantiation(instance):
    assert isinstance(instance, eol::TextRegion)
