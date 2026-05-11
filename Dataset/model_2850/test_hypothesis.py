import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    alf::AcceptClause,
    alf::ReclassifyAllClause,
    alf::ClassificationToClause,
    alf::ClassificationFromClause,
    alf::ClassificationClause,
    alf::AcceptBlock,
    alf::CompoundAcceptStatementCompletion,
    alf::SimpleAcceptStatementCompletion,
    alf::NonEmptyStatementSequence,
    alf::SwitchCase,
    alf::SwitchDefaultClause,
    alf::SwitchClause,
    alf::LoopVariableDefinition,
    alf::ForControl,
    alf::LocalNameDeclarationStatementCompletion,
    alf::NonFinalClause,
    alf::ConcurrentClauses,
    alf::FinalClause,
    alf::SequentialClauses,
    alf::NameList,
    alf::Annotation,
    alf::ConditionalExpression,
    alf::ConditionalOrExpressionCompletion,
    alf::ConditionalOrExpression,
    alf::Annotations,
    Statement,
    alf::ReturnStatement,
    alf::SwitchStatement,
    alf::ClassifyStatement,
    alf::BreakStatement,
    alf::DoStatement,
    alf::InLineStatement,
    alf::EmptyStatement,
    alf::WhileStatement,
    alf::ForStatement,
    alf::BlockStatement,
    alf::IfStatement,
    alf::AcceptStatement,
    alf::LocalNameDeclarationStatement,
    alf::LocalNameDeclarationOrExpressionStatement,
    alf::AnnotatedStatement,
    alf::Statement,
    alf::DocumentedStatement,
    alf::StatementSequence,
    ExpressionCompletion,
    alf::AssignmentExpressionCompletion,
    alf::ConditionalExpressionCompletion,
    alf::AndExpression,
    alf::EqualityExpressionCompletion,
    alf::RedefinitionClause,
    OperationDefinitionOrStub,
    alf::OperationDeclaration,
    alf::UnlimitedNaturalLiteral,
    alf::MultiplicityRange,
    alf::Multiplicity,
    alf::TypeName,
    alf::TypePart,
    alf::FormalParameters,
    FeatureDefinitionOrStub,
    alf::AttributeDefinition,
    alf::PropertyDeclaration,
    alf::FormalParameter,
    alf::FormalParameterList,
    alf::AssociationDeclaration,
    alf::PropertyDefinition,
    alf::ActivityDeclaration,
    alf::SignalDeclaration,
    alf::EnumerationLiteralName,
    alf::EnumerationBody,
    alf::EnumerationDeclaration,
    alf::ActiveClassBody,
    alf::StructuredMember,
    alf::StructuredBody,
    alf::DataTypeDeclaration,
    alf::ActiveClassMemberDefinition,
    alf::Block,
    alf::BehaviorClause,
    alf::ActiveClassMember,
    alf::PackagedElementDefinition,
    alf::ActiveClassDeclaration,
    alf::PackagedElement,
    ActiveClassMemberDefinition,
    alf::ActiveFeatureDefinitionOrStub,
    alf::ClassMemberDefinition,
    alf::ClassMember,
    ClassifierDefinitionOrStub,
    alf::DataTypeDefinitionOrStub,
    alf::ActivityDefinitionOrStub,
    alf::AssociationDefinitionOrStub,
    alf::SignalDefinitionOrStub,
    alf::EnumerationDefinitionOrStub,
    alf::ActiveClassDefinitionOrStub,
    alf::ClassDefinitionOrStub,
    alf::ClassBody,
    ClassifierDefinition,
    alf::EnumerationDefinition,
    alf::DataTypeDefinition,
    alf::ActivityDefinition,
    alf::ActiveClassDefinition,
    alf::SignalDefinition,
    alf::AssociationDefinition,
    alf::ClassDefinition,
    alf::ClassDeclaration,
    alf::ClassifierTemplateParameter,
    alf::SpecializationClause,
    PackagedElementDefinition,
    alf::PackageDefinitionOrStub,
    alf::TemplateParameters,
    alf::PackageBody,
    alf::ClassifierSignature,
    ClassMemberDefinition,
    alf::ClassifierDefinitionOrStub,
    alf::FeatureDefinitionOrStub,
    NamespaceDefinition,
    alf::ClassifierDefinition,
    alf::PackageDefinition,
    alf::PackageDeclaration,
    alf::VisibilityIndicator,
    ImportReferenceQualifiedNameCompletion,
    alf::ColonQualifiedNameCompletionOfImportReference,
    alf::AliasDefinition,
    alf::ImportReferenceQualifiedNameCompletion,
    alf::Name,
    alf::PRIMITIVE::LITERAL,
    alf::TaggedValue,
    TaggedValues,
    alf::QualifiedNameList,
    alf::TaggedValueList,
    alf::TaggedValues,
    alf::QualifiedName,
    alf::StereotypeAnnotation,
    NUMBER::LITERAL,
    alf::UNLIMITED::NATURAL,
    alf::INTEGER::LITERAL,
    PRIMITIVE::LITERAL,
    alf::NUMBER::LITERAL,
    alf::STRING::LITERAL,
    alf::BOOLEAN::LITERAL,
    alf::NamespaceDefinition,
    alf::StereotypeAnnotations,
    alf::ImportDeclaration,
    alf::NamespaceDeclaration,
    alf::UnitDefinition,
    alf::ImportReference,
    alf::ConditionalAndExpressionCompletion,
    alf::ConditionalAndExpression,
    alf::InclusiveOrExpressionCompletion,
    alf::InclusiveOrExpression,
    alf::ExclusiveOrExpressionCompletion,
    alf::ExclusiveOrExpression,
    alf::AndExpressionCompletion,
    alf::ShiftExpressionCompletion,
    alf::ShiftExpression,
    alf::EqualityExpression,
    alf::ClassificationExpressionCompletion,
    alf::ClassificationExpression,
    alf::RelationalExpressionCompletion,
    alf::RelationalExpression,
    alf::AdditiveExpressionCompletion,
    alf::AdditiveExpression,
    alf::MultiplicativeExpressionCompletion,
    alf::MultiplicativeExpression,
    alf::CastCompletion,
    NonNameUnaryExpression,
    alf::NonNamePostfixOrCastExpression,
    CastCompletion,
    UnaryExpression,
    alf::NonPostfixNonCastUnaryExpression,
    alf::PostfixOrCastExpression,
    NonPostfixNonCastUnaryExpression,
    alf::NumericUnaryExpression,
    alf::BooleanNegationExpression,
    alf::IsolationExpression,
    alf::BitStringComplementExpression,
    alf::PrefixExpression,
    alf::PostfixOperation,
    alf::EObject,
    alf::SequenceElement,
    alf::SequenceElementListCompletion,
    alf::SequenceElements,
    alf::MultiplicityIndicator,
    alf::IndexedNamedExpression,
    alf::IndexedNamedExpressionListCompletion,
    alf::LinkOperationTuple,
    BaseExpression,
    alf::SuperInvocationExpression,
    alf::InstanceCreationOrSequenceConstructionExpression,
    alf::SequenceAnyExpression,
    alf::LiteralExpression,
    alf::Index,
    alf::NamedExpression,
    alf::PositionalTupleExpressionListCompletion,
    alf::PositionalTupleExpressionList,
    alf::NamedTupleExpressionList,
    alf::Tuple,
    alf::ThisExpression,
    alf::ExpressionCompletion,
    alf::UnaryExpression,
    InitializationExpression,
    alf::InstanceInitializationExpression,
    alf::SequenceInitializationExpression,
    alf::Expression,
    alf::SequenceOperationOrReductionOrExpansion,
    alf::FeatureInvocation,
    alf::Feature,
    alf::Feature::Or::SequenceOperationOrReductionOrExpansion::Or::Index,
    alf::BehaviorInvocation,
    alf::SequenceConstructionExpressionCompletion,
    alf::ClassExtentExpressionCompletion,
    alf::LinkOperationCompletion,
    alf::PrimaryExpressionCompletion,
    alf::ParenthesizedExpression,
    alf::BaseExpression,
    alf::NameOrPrimaryExpression,
    alf::PrimaryExpression,
    alf::PostfixExpressionCompletion,
    alf::PrimaryToExpressionCompletion,
    alf::NameToPrimaryExpression,
    alf::NameToExpressionCompletion,
    alf::NonNameUnaryExpression,
    alf::NonNameExpression,
    alf::SignalReceptionDeclaration,
    alf::TemplateParameterSubstitution,
    TemplateBinding,
    alf::NamedTemplateBinding,
    alf::PositionalTemplateBinding,
    alf::ColonQualifiedNameCompletionWithoutBinding,
    alf::QualifiedNameWithoutBinding,
    alf::TemplateBinding,
    UnqualifiedName,
    alf::NameBinding,
    alf::ColonQualifiedNameCompletion,
    alf::UnqualifiedName,
    alf::InitializationExpression,
    ActiveFeatureDefinitionOrStub,
    alf::SignalReceptionDefinitionOrStub,
    alf::ReceptionDefinition,
    alf::AttributeInitializer,
    alf::OperationDefinitionOrStub,
    ParameterDirection,
    ClassificationOperator,
    ShiftOperator,
    AssignmentOperator,
    MultiplicativeOperator,
    ImportVisibilityIndicator,
    EqualityOperator,
    AffixOperator,
    LinkOperation,
    NumericUnaryOperator,
    RelationalOperator,
    AdditiveOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_alf::acceptclause_is_not_abstract():
    assert not inspect.isabstract(alf::AcceptClause)


def test_alf::acceptclause_constructor_exists():
    assert callable(alf::AcceptClause.__init__)


def test_alf::acceptclause_constructor_args():
    sig = inspect.signature(alf::AcceptClause.__init__)
    params = list(sig.parameters.keys())



def test_alf::reclassifyallclause_is_not_abstract():
    assert not inspect.isabstract(alf::ReclassifyAllClause)


def test_alf::reclassifyallclause_constructor_exists():
    assert callable(alf::ReclassifyAllClause.__init__)


def test_alf::reclassifyallclause_constructor_args():
    sig = inspect.signature(alf::ReclassifyAllClause.__init__)
    params = list(sig.parameters.keys())



def test_alf::classificationtoclause_is_not_abstract():
    assert not inspect.isabstract(alf::ClassificationToClause)


def test_alf::classificationtoclause_constructor_exists():
    assert callable(alf::ClassificationToClause.__init__)


def test_alf::classificationtoclause_constructor_args():
    sig = inspect.signature(alf::ClassificationToClause.__init__)
    params = list(sig.parameters.keys())



def test_alf::classificationfromclause_is_not_abstract():
    assert not inspect.isabstract(alf::ClassificationFromClause)


def test_alf::classificationfromclause_constructor_exists():
    assert callable(alf::ClassificationFromClause.__init__)


def test_alf::classificationfromclause_constructor_args():
    sig = inspect.signature(alf::ClassificationFromClause.__init__)
    params = list(sig.parameters.keys())



def test_alf::classificationclause_is_not_abstract():
    assert not inspect.isabstract(alf::ClassificationClause)


def test_alf::classificationclause_constructor_exists():
    assert callable(alf::ClassificationClause.__init__)


def test_alf::classificationclause_constructor_args():
    sig = inspect.signature(alf::ClassificationClause.__init__)
    params = list(sig.parameters.keys())



def test_alf::acceptblock_is_not_abstract():
    assert not inspect.isabstract(alf::AcceptBlock)


def test_alf::acceptblock_constructor_exists():
    assert callable(alf::AcceptBlock.__init__)


def test_alf::acceptblock_constructor_args():
    sig = inspect.signature(alf::AcceptBlock.__init__)
    params = list(sig.parameters.keys())



def test_alf::compoundacceptstatementcompletion_is_not_abstract():
    assert not inspect.isabstract(alf::CompoundAcceptStatementCompletion)


def test_alf::compoundacceptstatementcompletion_constructor_exists():
    assert callable(alf::CompoundAcceptStatementCompletion.__init__)


def test_alf::compoundacceptstatementcompletion_constructor_args():
    sig = inspect.signature(alf::CompoundAcceptStatementCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::simpleacceptstatementcompletion_is_not_abstract():
    assert not inspect.isabstract(alf::SimpleAcceptStatementCompletion)


def test_alf::simpleacceptstatementcompletion_constructor_exists():
    assert callable(alf::SimpleAcceptStatementCompletion.__init__)


def test_alf::simpleacceptstatementcompletion_constructor_args():
    sig = inspect.signature(alf::SimpleAcceptStatementCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::nonemptystatementsequence_is_not_abstract():
    assert not inspect.isabstract(alf::NonEmptyStatementSequence)


def test_alf::nonemptystatementsequence_constructor_exists():
    assert callable(alf::NonEmptyStatementSequence.__init__)


def test_alf::nonemptystatementsequence_constructor_args():
    sig = inspect.signature(alf::NonEmptyStatementSequence.__init__)
    params = list(sig.parameters.keys())



def test_alf::switchcase_is_not_abstract():
    assert not inspect.isabstract(alf::SwitchCase)


def test_alf::switchcase_constructor_exists():
    assert callable(alf::SwitchCase.__init__)


def test_alf::switchcase_constructor_args():
    sig = inspect.signature(alf::SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_alf::switchdefaultclause_is_not_abstract():
    assert not inspect.isabstract(alf::SwitchDefaultClause)


def test_alf::switchdefaultclause_constructor_exists():
    assert callable(alf::SwitchDefaultClause.__init__)


def test_alf::switchdefaultclause_constructor_args():
    sig = inspect.signature(alf::SwitchDefaultClause.__init__)
    params = list(sig.parameters.keys())



def test_alf::switchclause_is_not_abstract():
    assert not inspect.isabstract(alf::SwitchClause)


def test_alf::switchclause_constructor_exists():
    assert callable(alf::SwitchClause.__init__)


def test_alf::switchclause_constructor_args():
    sig = inspect.signature(alf::SwitchClause.__init__)
    params = list(sig.parameters.keys())



def test_alf::loopvariabledefinition_is_not_abstract():
    assert not inspect.isabstract(alf::LoopVariableDefinition)


def test_alf::loopvariabledefinition_constructor_exists():
    assert callable(alf::LoopVariableDefinition.__init__)


def test_alf::loopvariabledefinition_constructor_args():
    sig = inspect.signature(alf::LoopVariableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::forcontrol_is_not_abstract():
    assert not inspect.isabstract(alf::ForControl)


def test_alf::forcontrol_constructor_exists():
    assert callable(alf::ForControl.__init__)


def test_alf::forcontrol_constructor_args():
    sig = inspect.signature(alf::ForControl.__init__)
    params = list(sig.parameters.keys())



def test_alf::localnamedeclarationstatementcompletion_is_not_abstract():
    assert not inspect.isabstract(alf::LocalNameDeclarationStatementCompletion)


def test_alf::localnamedeclarationstatementcompletion_constructor_exists():
    assert callable(alf::LocalNameDeclarationStatementCompletion.__init__)


def test_alf::localnamedeclarationstatementcompletion_constructor_args():
    sig = inspect.signature(alf::LocalNameDeclarationStatementCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::nonfinalclause_is_not_abstract():
    assert not inspect.isabstract(alf::NonFinalClause)


def test_alf::nonfinalclause_constructor_exists():
    assert callable(alf::NonFinalClause.__init__)


def test_alf::nonfinalclause_constructor_args():
    sig = inspect.signature(alf::NonFinalClause.__init__)
    params = list(sig.parameters.keys())



def test_alf::concurrentclauses_is_not_abstract():
    assert not inspect.isabstract(alf::ConcurrentClauses)


def test_alf::concurrentclauses_constructor_exists():
    assert callable(alf::ConcurrentClauses.__init__)


def test_alf::concurrentclauses_constructor_args():
    sig = inspect.signature(alf::ConcurrentClauses.__init__)
    params = list(sig.parameters.keys())



def test_alf::finalclause_is_not_abstract():
    assert not inspect.isabstract(alf::FinalClause)


def test_alf::finalclause_constructor_exists():
    assert callable(alf::FinalClause.__init__)


def test_alf::finalclause_constructor_args():
    sig = inspect.signature(alf::FinalClause.__init__)
    params = list(sig.parameters.keys())



def test_alf::sequentialclauses_is_not_abstract():
    assert not inspect.isabstract(alf::SequentialClauses)


def test_alf::sequentialclauses_constructor_exists():
    assert callable(alf::SequentialClauses.__init__)


def test_alf::sequentialclauses_constructor_args():
    sig = inspect.signature(alf::SequentialClauses.__init__)
    params = list(sig.parameters.keys())



def test_alf::namelist_is_not_abstract():
    assert not inspect.isabstract(alf::NameList)


def test_alf::namelist_constructor_exists():
    assert callable(alf::NameList.__init__)


def test_alf::namelist_constructor_args():
    sig = inspect.signature(alf::NameList.__init__)
    params = list(sig.parameters.keys())



def test_alf::annotation_is_not_abstract():
    assert not inspect.isabstract(alf::Annotation)


def test_alf::annotation_constructor_exists():
    assert callable(alf::Annotation.__init__)


def test_alf::annotation_constructor_args():
    sig = inspect.signature(alf::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_alf::annotation_has_id():
    assert hasattr(alf::Annotation, "id")
    descriptor = None
    for klass in alf::Annotation.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_alf::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ConditionalExpression)


def test_alf::conditionalexpression_constructor_exists():
    assert callable(alf::ConditionalExpression.__init__)


def test_alf::conditionalexpression_constructor_args():
    sig = inspect.signature(alf::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::conditionalorexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::ConditionalOrExpressionCompletion)


def test_alf::conditionalorexpressioncompletion_constructor_exists():
    assert callable(alf::ConditionalOrExpressionCompletion.__init__)


def test_alf::conditionalorexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::ConditionalOrExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ConditionalOrExpression)


def test_alf::conditionalorexpression_constructor_exists():
    assert callable(alf::ConditionalOrExpression.__init__)


def test_alf::conditionalorexpression_constructor_args():
    sig = inspect.signature(alf::ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::annotations_is_not_abstract():
    assert not inspect.isabstract(alf::Annotations)


def test_alf::annotations_constructor_exists():
    assert callable(alf::Annotations.__init__)


def test_alf::annotations_constructor_args():
    sig = inspect.signature(alf::Annotations.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_alf::returnstatement_is_not_abstract():
    assert not inspect.isabstract(alf::ReturnStatement)


def test_alf::returnstatement_constructor_exists():
    assert callable(alf::ReturnStatement.__init__)


def test_alf::returnstatement_constructor_args():
    sig = inspect.signature(alf::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::switchstatement_is_not_abstract():
    assert not inspect.isabstract(alf::SwitchStatement)


def test_alf::switchstatement_constructor_exists():
    assert callable(alf::SwitchStatement.__init__)


def test_alf::switchstatement_constructor_args():
    sig = inspect.signature(alf::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::classifystatement_is_not_abstract():
    assert not inspect.isabstract(alf::ClassifyStatement)


def test_alf::classifystatement_constructor_exists():
    assert callable(alf::ClassifyStatement.__init__)


def test_alf::classifystatement_constructor_args():
    sig = inspect.signature(alf::ClassifyStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::breakstatement_is_not_abstract():
    assert not inspect.isabstract(alf::BreakStatement)


def test_alf::breakstatement_constructor_exists():
    assert callable(alf::BreakStatement.__init__)


def test_alf::breakstatement_constructor_args():
    sig = inspect.signature(alf::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::dostatement_is_not_abstract():
    assert not inspect.isabstract(alf::DoStatement)


def test_alf::dostatement_constructor_exists():
    assert callable(alf::DoStatement.__init__)


def test_alf::dostatement_constructor_args():
    sig = inspect.signature(alf::DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::inlinestatement_is_not_abstract():
    assert not inspect.isabstract(alf::InLineStatement)


def test_alf::inlinestatement_constructor_exists():
    assert callable(alf::InLineStatement.__init__)


def test_alf::inlinestatement_constructor_args():
    sig = inspect.signature(alf::InLineStatement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_alf::inlinestatement_has_id():
    assert hasattr(alf::InLineStatement, "id")
    descriptor = None
    for klass in alf::InLineStatement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_alf::emptystatement_is_not_abstract():
    assert not inspect.isabstract(alf::EmptyStatement)


def test_alf::emptystatement_constructor_exists():
    assert callable(alf::EmptyStatement.__init__)


def test_alf::emptystatement_constructor_args():
    sig = inspect.signature(alf::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::whilestatement_is_not_abstract():
    assert not inspect.isabstract(alf::WhileStatement)


def test_alf::whilestatement_constructor_exists():
    assert callable(alf::WhileStatement.__init__)


def test_alf::whilestatement_constructor_args():
    sig = inspect.signature(alf::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::forstatement_is_not_abstract():
    assert not inspect.isabstract(alf::ForStatement)


def test_alf::forstatement_constructor_exists():
    assert callable(alf::ForStatement.__init__)


def test_alf::forstatement_constructor_args():
    sig = inspect.signature(alf::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::blockstatement_is_not_abstract():
    assert not inspect.isabstract(alf::BlockStatement)


def test_alf::blockstatement_constructor_exists():
    assert callable(alf::BlockStatement.__init__)


def test_alf::blockstatement_constructor_args():
    sig = inspect.signature(alf::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::ifstatement_is_not_abstract():
    assert not inspect.isabstract(alf::IfStatement)


def test_alf::ifstatement_constructor_exists():
    assert callable(alf::IfStatement.__init__)


def test_alf::ifstatement_constructor_args():
    sig = inspect.signature(alf::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::acceptstatement_is_not_abstract():
    assert not inspect.isabstract(alf::AcceptStatement)


def test_alf::acceptstatement_constructor_exists():
    assert callable(alf::AcceptStatement.__init__)


def test_alf::acceptstatement_constructor_args():
    sig = inspect.signature(alf::AcceptStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::localnamedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(alf::LocalNameDeclarationStatement)


def test_alf::localnamedeclarationstatement_constructor_exists():
    assert callable(alf::LocalNameDeclarationStatement.__init__)


def test_alf::localnamedeclarationstatement_constructor_args():
    sig = inspect.signature(alf::LocalNameDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::localnamedeclarationorexpressionstatement_is_not_abstract():
    assert not inspect.isabstract(alf::LocalNameDeclarationOrExpressionStatement)


def test_alf::localnamedeclarationorexpressionstatement_constructor_exists():
    assert callable(alf::LocalNameDeclarationOrExpressionStatement.__init__)


def test_alf::localnamedeclarationorexpressionstatement_constructor_args():
    sig = inspect.signature(alf::LocalNameDeclarationOrExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::annotatedstatement_is_not_abstract():
    assert not inspect.isabstract(alf::AnnotatedStatement)


def test_alf::annotatedstatement_constructor_exists():
    assert callable(alf::AnnotatedStatement.__init__)


def test_alf::annotatedstatement_constructor_args():
    sig = inspect.signature(alf::AnnotatedStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::statement_is_not_abstract():
    assert not inspect.isabstract(alf::Statement)


def test_alf::statement_constructor_exists():
    assert callable(alf::Statement.__init__)


def test_alf::statement_constructor_args():
    sig = inspect.signature(alf::Statement.__init__)
    params = list(sig.parameters.keys())



def test_alf::documentedstatement_is_not_abstract():
    assert not inspect.isabstract(alf::DocumentedStatement)


def test_alf::documentedstatement_constructor_exists():
    assert callable(alf::DocumentedStatement.__init__)


def test_alf::documentedstatement_constructor_args():
    sig = inspect.signature(alf::DocumentedStatement.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_alf::documentedstatement_has_comment():
    assert hasattr(alf::DocumentedStatement, "comment")
    descriptor = None
    for klass in alf::DocumentedStatement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_alf::statementsequence_is_not_abstract():
    assert not inspect.isabstract(alf::StatementSequence)


def test_alf::statementsequence_constructor_exists():
    assert callable(alf::StatementSequence.__init__)


def test_alf::statementsequence_constructor_args():
    sig = inspect.signature(alf::StatementSequence.__init__)
    params = list(sig.parameters.keys())



def test_expressioncompletion_is_not_abstract():
    assert not inspect.isabstract(ExpressionCompletion)


def test_expressioncompletion_constructor_exists():
    assert callable(ExpressionCompletion.__init__)


def test_expressioncompletion_constructor_args():
    sig = inspect.signature(ExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::assignmentexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::AssignmentExpressionCompletion)


def test_alf::assignmentexpressioncompletion_constructor_exists():
    assert callable(alf::AssignmentExpressionCompletion.__init__)


def test_alf::assignmentexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::AssignmentExpressionCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf::assignmentexpressioncompletion_has_operator():
    assert hasattr(alf::AssignmentExpressionCompletion, "operator")
    descriptor = None
    for klass in alf::AssignmentExpressionCompletion.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf::conditionalexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::ConditionalExpressionCompletion)


def test_alf::conditionalexpressioncompletion_constructor_exists():
    assert callable(alf::ConditionalExpressionCompletion.__init__)


def test_alf::conditionalexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::ConditionalExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::andexpression_is_not_abstract():
    assert not inspect.isabstract(alf::AndExpression)


def test_alf::andexpression_constructor_exists():
    assert callable(alf::AndExpression.__init__)


def test_alf::andexpression_constructor_args():
    sig = inspect.signature(alf::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::equalityexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::EqualityExpressionCompletion)


def test_alf::equalityexpressioncompletion_constructor_exists():
    assert callable(alf::EqualityExpressionCompletion.__init__)


def test_alf::equalityexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::EqualityExpressionCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf::equalityexpressioncompletion_has_operator():
    assert hasattr(alf::EqualityExpressionCompletion, "operator")
    descriptor = None
    for klass in alf::EqualityExpressionCompletion.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf::redefinitionclause_is_not_abstract():
    assert not inspect.isabstract(alf::RedefinitionClause)


def test_alf::redefinitionclause_constructor_exists():
    assert callable(alf::RedefinitionClause.__init__)


def test_alf::redefinitionclause_constructor_args():
    sig = inspect.signature(alf::RedefinitionClause.__init__)
    params = list(sig.parameters.keys())



def test_operationdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(OperationDefinitionOrStub)


def test_operationdefinitionorstub_constructor_exists():
    assert callable(OperationDefinitionOrStub.__init__)


def test_operationdefinitionorstub_constructor_args():
    sig = inspect.signature(OperationDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::operationdeclaration_is_not_abstract():
    assert not inspect.isabstract(alf::OperationDeclaration)


def test_alf::operationdeclaration_constructor_exists():
    assert callable(alf::OperationDeclaration.__init__)


def test_alf::operationdeclaration_constructor_args():
    sig = inspect.signature(alf::OperationDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_alf::operationdeclaration_has_isAbstract():
    assert hasattr(alf::OperationDeclaration, "isAbstract")
    descriptor = None
    for klass in alf::OperationDeclaration.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_alf::unlimitednaturalliteral_is_not_abstract():
    assert not inspect.isabstract(alf::UnlimitedNaturalLiteral)


def test_alf::unlimitednaturalliteral_constructor_exists():
    assert callable(alf::UnlimitedNaturalLiteral.__init__)


def test_alf::unlimitednaturalliteral_constructor_args():
    sig = inspect.signature(alf::UnlimitedNaturalLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "star" in params, "Missing parameter 'star'"

def test_alf::unlimitednaturalliteral_has_star():
    assert hasattr(alf::UnlimitedNaturalLiteral, "star")
    descriptor = None
    for klass in alf::UnlimitedNaturalLiteral.__mro__:
        if "star" in klass.__dict__:
            descriptor = klass.__dict__["star"]
            break
    assert isinstance(descriptor, property)



def test_alf::multiplicityrange_is_not_abstract():
    assert not inspect.isabstract(alf::MultiplicityRange)


def test_alf::multiplicityrange_constructor_exists():
    assert callable(alf::MultiplicityRange.__init__)


def test_alf::multiplicityrange_constructor_args():
    sig = inspect.signature(alf::MultiplicityRange.__init__)
    params = list(sig.parameters.keys())



def test_alf::multiplicity_is_not_abstract():
    assert not inspect.isabstract(alf::Multiplicity)


def test_alf::multiplicity_constructor_exists():
    assert callable(alf::Multiplicity.__init__)


def test_alf::multiplicity_constructor_args():
    sig = inspect.signature(alf::Multiplicity.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isSequence" in params, "Missing parameter 'isSequence'"
    assert "isNonUnique" in params, "Missing parameter 'isNonUnique'"

def test_alf::multiplicity_has_isOrdered():
    assert hasattr(alf::Multiplicity, "isOrdered")
    descriptor = None
    for klass in alf::Multiplicity.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_alf::multiplicity_has_isSequence():
    assert hasattr(alf::Multiplicity, "isSequence")
    descriptor = None
    for klass in alf::Multiplicity.__mro__:
        if "isSequence" in klass.__dict__:
            descriptor = klass.__dict__["isSequence"]
            break
    assert isinstance(descriptor, property)

def test_alf::multiplicity_has_isNonUnique():
    assert hasattr(alf::Multiplicity, "isNonUnique")
    descriptor = None
    for klass in alf::Multiplicity.__mro__:
        if "isNonUnique" in klass.__dict__:
            descriptor = klass.__dict__["isNonUnique"]
            break
    assert isinstance(descriptor, property)



def test_alf::typename_is_not_abstract():
    assert not inspect.isabstract(alf::TypeName)


def test_alf::typename_constructor_exists():
    assert callable(alf::TypeName.__init__)


def test_alf::typename_constructor_args():
    sig = inspect.signature(alf::TypeName.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"

def test_alf::typename_has_any():
    assert hasattr(alf::TypeName, "any")
    descriptor = None
    for klass in alf::TypeName.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_alf::typepart_is_not_abstract():
    assert not inspect.isabstract(alf::TypePart)


def test_alf::typepart_constructor_exists():
    assert callable(alf::TypePart.__init__)


def test_alf::typepart_constructor_args():
    sig = inspect.signature(alf::TypePart.__init__)
    params = list(sig.parameters.keys())



def test_alf::formalparameters_is_not_abstract():
    assert not inspect.isabstract(alf::FormalParameters)


def test_alf::formalparameters_constructor_exists():
    assert callable(alf::FormalParameters.__init__)


def test_alf::formalparameters_constructor_args():
    sig = inspect.signature(alf::FormalParameters.__init__)
    params = list(sig.parameters.keys())



def test_featuredefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(FeatureDefinitionOrStub)


def test_featuredefinitionorstub_constructor_exists():
    assert callable(FeatureDefinitionOrStub.__init__)


def test_featuredefinitionorstub_constructor_args():
    sig = inspect.signature(FeatureDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::attributedefinition_is_not_abstract():
    assert not inspect.isabstract(alf::AttributeDefinition)


def test_alf::attributedefinition_constructor_exists():
    assert callable(alf::AttributeDefinition.__init__)


def test_alf::attributedefinition_constructor_args():
    sig = inspect.signature(alf::AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::propertydeclaration_is_not_abstract():
    assert not inspect.isabstract(alf::PropertyDeclaration)


def test_alf::propertydeclaration_constructor_exists():
    assert callable(alf::PropertyDeclaration.__init__)


def test_alf::propertydeclaration_constructor_args():
    sig = inspect.signature(alf::PropertyDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isComposite" in params, "Missing parameter 'isComposite'"

def test_alf::propertydeclaration_has_isComposite():
    assert hasattr(alf::PropertyDeclaration, "isComposite")
    descriptor = None
    for klass in alf::PropertyDeclaration.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)



def test_alf::formalparameter_is_not_abstract():
    assert not inspect.isabstract(alf::FormalParameter)


def test_alf::formalparameter_constructor_exists():
    assert callable(alf::FormalParameter.__init__)


def test_alf::formalparameter_constructor_args():
    sig = inspect.signature(alf::FormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterDirection" in params, "Missing parameter 'parameterDirection'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_alf::formalparameter_has_parameterDirection():
    assert hasattr(alf::FormalParameter, "parameterDirection")
    descriptor = None
    for klass in alf::FormalParameter.__mro__:
        if "parameterDirection" in klass.__dict__:
            descriptor = klass.__dict__["parameterDirection"]
            break
    assert isinstance(descriptor, property)

def test_alf::formalparameter_has_comment():
    assert hasattr(alf::FormalParameter, "comment")
    descriptor = None
    for klass in alf::FormalParameter.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_alf::formalparameterlist_is_not_abstract():
    assert not inspect.isabstract(alf::FormalParameterList)


def test_alf::formalparameterlist_constructor_exists():
    assert callable(alf::FormalParameterList.__init__)


def test_alf::formalparameterlist_constructor_args():
    sig = inspect.signature(alf::FormalParameterList.__init__)
    params = list(sig.parameters.keys())



def test_alf::associationdeclaration_is_not_abstract():
    assert not inspect.isabstract(alf::AssociationDeclaration)


def test_alf::associationdeclaration_constructor_exists():
    assert callable(alf::AssociationDeclaration.__init__)


def test_alf::associationdeclaration_constructor_args():
    sig = inspect.signature(alf::AssociationDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_alf::associationdeclaration_has_isAbstract():
    assert hasattr(alf::AssociationDeclaration, "isAbstract")
    descriptor = None
    for klass in alf::AssociationDeclaration.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_alf::propertydefinition_is_not_abstract():
    assert not inspect.isabstract(alf::PropertyDefinition)


def test_alf::propertydefinition_constructor_exists():
    assert callable(alf::PropertyDefinition.__init__)


def test_alf::propertydefinition_constructor_args():
    sig = inspect.signature(alf::PropertyDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::activitydeclaration_is_not_abstract():
    assert not inspect.isabstract(alf::ActivityDeclaration)


def test_alf::activitydeclaration_constructor_exists():
    assert callable(alf::ActivityDeclaration.__init__)


def test_alf::activitydeclaration_constructor_args():
    sig = inspect.signature(alf::ActivityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_alf::signaldeclaration_is_not_abstract():
    assert not inspect.isabstract(alf::SignalDeclaration)


def test_alf::signaldeclaration_constructor_exists():
    assert callable(alf::SignalDeclaration.__init__)


def test_alf::signaldeclaration_constructor_args():
    sig = inspect.signature(alf::SignalDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_alf::signaldeclaration_has_isAbstract():
    assert hasattr(alf::SignalDeclaration, "isAbstract")
    descriptor = None
    for klass in alf::SignalDeclaration.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_alf::enumerationliteralname_is_not_abstract():
    assert not inspect.isabstract(alf::EnumerationLiteralName)


def test_alf::enumerationliteralname_constructor_exists():
    assert callable(alf::EnumerationLiteralName.__init__)


def test_alf::enumerationliteralname_constructor_args():
    sig = inspect.signature(alf::EnumerationLiteralName.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_alf::enumerationliteralname_has_comment():
    assert hasattr(alf::EnumerationLiteralName, "comment")
    descriptor = None
    for klass in alf::EnumerationLiteralName.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_alf::enumerationbody_is_not_abstract():
    assert not inspect.isabstract(alf::EnumerationBody)


def test_alf::enumerationbody_constructor_exists():
    assert callable(alf::EnumerationBody.__init__)


def test_alf::enumerationbody_constructor_args():
    sig = inspect.signature(alf::EnumerationBody.__init__)
    params = list(sig.parameters.keys())



def test_alf::enumerationdeclaration_is_not_abstract():
    assert not inspect.isabstract(alf::EnumerationDeclaration)


def test_alf::enumerationdeclaration_constructor_exists():
    assert callable(alf::EnumerationDeclaration.__init__)


def test_alf::enumerationdeclaration_constructor_args():
    sig = inspect.signature(alf::EnumerationDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_alf::activeclassbody_is_not_abstract():
    assert not inspect.isabstract(alf::ActiveClassBody)


def test_alf::activeclassbody_constructor_exists():
    assert callable(alf::ActiveClassBody.__init__)


def test_alf::activeclassbody_constructor_args():
    sig = inspect.signature(alf::ActiveClassBody.__init__)
    params = list(sig.parameters.keys())



def test_alf::structuredmember_is_not_abstract():
    assert not inspect.isabstract(alf::StructuredMember)


def test_alf::structuredmember_constructor_exists():
    assert callable(alf::StructuredMember.__init__)


def test_alf::structuredmember_constructor_args():
    sig = inspect.signature(alf::StructuredMember.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "isPublic" in params, "Missing parameter 'isPublic'"

def test_alf::structuredmember_has_comment():
    assert hasattr(alf::StructuredMember, "comment")
    descriptor = None
    for klass in alf::StructuredMember.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_alf::structuredmember_has_isPublic():
    assert hasattr(alf::StructuredMember, "isPublic")
    descriptor = None
    for klass in alf::StructuredMember.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)



def test_alf::structuredbody_is_not_abstract():
    assert not inspect.isabstract(alf::StructuredBody)


def test_alf::structuredbody_constructor_exists():
    assert callable(alf::StructuredBody.__init__)


def test_alf::structuredbody_constructor_args():
    sig = inspect.signature(alf::StructuredBody.__init__)
    params = list(sig.parameters.keys())



def test_alf::datatypedeclaration_is_not_abstract():
    assert not inspect.isabstract(alf::DataTypeDeclaration)


def test_alf::datatypedeclaration_constructor_exists():
    assert callable(alf::DataTypeDeclaration.__init__)


def test_alf::datatypedeclaration_constructor_args():
    sig = inspect.signature(alf::DataTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_alf::datatypedeclaration_has_isAbstract():
    assert hasattr(alf::DataTypeDeclaration, "isAbstract")
    descriptor = None
    for klass in alf::DataTypeDeclaration.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_alf::activeclassmemberdefinition_is_not_abstract():
    assert not inspect.isabstract(alf::ActiveClassMemberDefinition)


def test_alf::activeclassmemberdefinition_constructor_exists():
    assert callable(alf::ActiveClassMemberDefinition.__init__)


def test_alf::activeclassmemberdefinition_constructor_args():
    sig = inspect.signature(alf::ActiveClassMemberDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::block_is_not_abstract():
    assert not inspect.isabstract(alf::Block)


def test_alf::block_constructor_exists():
    assert callable(alf::Block.__init__)


def test_alf::block_constructor_args():
    sig = inspect.signature(alf::Block.__init__)
    params = list(sig.parameters.keys())



def test_alf::behaviorclause_is_not_abstract():
    assert not inspect.isabstract(alf::BehaviorClause)


def test_alf::behaviorclause_constructor_exists():
    assert callable(alf::BehaviorClause.__init__)


def test_alf::behaviorclause_constructor_args():
    sig = inspect.signature(alf::BehaviorClause.__init__)
    params = list(sig.parameters.keys())



def test_alf::activeclassmember_is_not_abstract():
    assert not inspect.isabstract(alf::ActiveClassMember)


def test_alf::activeclassmember_constructor_exists():
    assert callable(alf::ActiveClassMember.__init__)


def test_alf::activeclassmember_constructor_args():
    sig = inspect.signature(alf::ActiveClassMember.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_alf::activeclassmember_has_comment():
    assert hasattr(alf::ActiveClassMember, "comment")
    descriptor = None
    for klass in alf::ActiveClassMember.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_alf::packagedelementdefinition_is_not_abstract():
    assert not inspect.isabstract(alf::PackagedElementDefinition)


def test_alf::packagedelementdefinition_constructor_exists():
    assert callable(alf::PackagedElementDefinition.__init__)


def test_alf::packagedelementdefinition_constructor_args():
    sig = inspect.signature(alf::PackagedElementDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::activeclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(alf::ActiveClassDeclaration)


def test_alf::activeclassdeclaration_constructor_exists():
    assert callable(alf::ActiveClassDeclaration.__init__)


def test_alf::activeclassdeclaration_constructor_args():
    sig = inspect.signature(alf::ActiveClassDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_alf::activeclassdeclaration_has_isAbstract():
    assert hasattr(alf::ActiveClassDeclaration, "isAbstract")
    descriptor = None
    for klass in alf::ActiveClassDeclaration.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_alf::packagedelement_is_not_abstract():
    assert not inspect.isabstract(alf::PackagedElement)


def test_alf::packagedelement_constructor_exists():
    assert callable(alf::PackagedElement.__init__)


def test_alf::packagedelement_constructor_args():
    sig = inspect.signature(alf::PackagedElement.__init__)
    params = list(sig.parameters.keys())
    assert "importVisibilityIndicator" in params, "Missing parameter 'importVisibilityIndicator'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_alf::packagedelement_has_importVisibilityIndicator():
    assert hasattr(alf::PackagedElement, "importVisibilityIndicator")
    descriptor = None
    for klass in alf::PackagedElement.__mro__:
        if "importVisibilityIndicator" in klass.__dict__:
            descriptor = klass.__dict__["importVisibilityIndicator"]
            break
    assert isinstance(descriptor, property)

def test_alf::packagedelement_has_comment():
    assert hasattr(alf::PackagedElement, "comment")
    descriptor = None
    for klass in alf::PackagedElement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_activeclassmemberdefinition_is_not_abstract():
    assert not inspect.isabstract(ActiveClassMemberDefinition)


def test_activeclassmemberdefinition_constructor_exists():
    assert callable(ActiveClassMemberDefinition.__init__)


def test_activeclassmemberdefinition_constructor_args():
    sig = inspect.signature(ActiveClassMemberDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::activefeaturedefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf::ActiveFeatureDefinitionOrStub)


def test_alf::activefeaturedefinitionorstub_constructor_exists():
    assert callable(alf::ActiveFeatureDefinitionOrStub.__init__)


def test_alf::activefeaturedefinitionorstub_constructor_args():
    sig = inspect.signature(alf::ActiveFeatureDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::classmemberdefinition_is_not_abstract():
    assert not inspect.isabstract(alf::ClassMemberDefinition)


def test_alf::classmemberdefinition_constructor_exists():
    assert callable(alf::ClassMemberDefinition.__init__)


def test_alf::classmemberdefinition_constructor_args():
    sig = inspect.signature(alf::ClassMemberDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::classmember_is_not_abstract():
    assert not inspect.isabstract(alf::ClassMember)


def test_alf::classmember_constructor_exists():
    assert callable(alf::ClassMember.__init__)


def test_alf::classmember_constructor_args():
    sig = inspect.signature(alf::ClassMember.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_alf::classmember_has_comment():
    assert hasattr(alf::ClassMember, "comment")
    descriptor = None
    for klass in alf::ClassMember.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_classifierdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(ClassifierDefinitionOrStub)


def test_classifierdefinitionorstub_constructor_exists():
    assert callable(ClassifierDefinitionOrStub.__init__)


def test_classifierdefinitionorstub_constructor_args():
    sig = inspect.signature(ClassifierDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::datatypedefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf::DataTypeDefinitionOrStub)


def test_alf::datatypedefinitionorstub_constructor_exists():
    assert callable(alf::DataTypeDefinitionOrStub.__init__)


def test_alf::datatypedefinitionorstub_constructor_args():
    sig = inspect.signature(alf::DataTypeDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::activitydefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf::ActivityDefinitionOrStub)


def test_alf::activitydefinitionorstub_constructor_exists():
    assert callable(alf::ActivityDefinitionOrStub.__init__)


def test_alf::activitydefinitionorstub_constructor_args():
    sig = inspect.signature(alf::ActivityDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::associationdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf::AssociationDefinitionOrStub)


def test_alf::associationdefinitionorstub_constructor_exists():
    assert callable(alf::AssociationDefinitionOrStub.__init__)


def test_alf::associationdefinitionorstub_constructor_args():
    sig = inspect.signature(alf::AssociationDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::signaldefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf::SignalDefinitionOrStub)


def test_alf::signaldefinitionorstub_constructor_exists():
    assert callable(alf::SignalDefinitionOrStub.__init__)


def test_alf::signaldefinitionorstub_constructor_args():
    sig = inspect.signature(alf::SignalDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::enumerationdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf::EnumerationDefinitionOrStub)


def test_alf::enumerationdefinitionorstub_constructor_exists():
    assert callable(alf::EnumerationDefinitionOrStub.__init__)


def test_alf::enumerationdefinitionorstub_constructor_args():
    sig = inspect.signature(alf::EnumerationDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::activeclassdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf::ActiveClassDefinitionOrStub)


def test_alf::activeclassdefinitionorstub_constructor_exists():
    assert callable(alf::ActiveClassDefinitionOrStub.__init__)


def test_alf::activeclassdefinitionorstub_constructor_args():
    sig = inspect.signature(alf::ActiveClassDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::classdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf::ClassDefinitionOrStub)


def test_alf::classdefinitionorstub_constructor_exists():
    assert callable(alf::ClassDefinitionOrStub.__init__)


def test_alf::classdefinitionorstub_constructor_args():
    sig = inspect.signature(alf::ClassDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::classbody_is_not_abstract():
    assert not inspect.isabstract(alf::ClassBody)


def test_alf::classbody_constructor_exists():
    assert callable(alf::ClassBody.__init__)


def test_alf::classbody_constructor_args():
    sig = inspect.signature(alf::ClassBody.__init__)
    params = list(sig.parameters.keys())



def test_classifierdefinition_is_not_abstract():
    assert not inspect.isabstract(ClassifierDefinition)


def test_classifierdefinition_constructor_exists():
    assert callable(ClassifierDefinition.__init__)


def test_classifierdefinition_constructor_args():
    sig = inspect.signature(ClassifierDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::enumerationdefinition_is_not_abstract():
    assert not inspect.isabstract(alf::EnumerationDefinition)


def test_alf::enumerationdefinition_constructor_exists():
    assert callable(alf::EnumerationDefinition.__init__)


def test_alf::enumerationdefinition_constructor_args():
    sig = inspect.signature(alf::EnumerationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::datatypedefinition_is_not_abstract():
    assert not inspect.isabstract(alf::DataTypeDefinition)


def test_alf::datatypedefinition_constructor_exists():
    assert callable(alf::DataTypeDefinition.__init__)


def test_alf::datatypedefinition_constructor_args():
    sig = inspect.signature(alf::DataTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::activitydefinition_is_not_abstract():
    assert not inspect.isabstract(alf::ActivityDefinition)


def test_alf::activitydefinition_constructor_exists():
    assert callable(alf::ActivityDefinition.__init__)


def test_alf::activitydefinition_constructor_args():
    sig = inspect.signature(alf::ActivityDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::activeclassdefinition_is_not_abstract():
    assert not inspect.isabstract(alf::ActiveClassDefinition)


def test_alf::activeclassdefinition_constructor_exists():
    assert callable(alf::ActiveClassDefinition.__init__)


def test_alf::activeclassdefinition_constructor_args():
    sig = inspect.signature(alf::ActiveClassDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::signaldefinition_is_not_abstract():
    assert not inspect.isabstract(alf::SignalDefinition)


def test_alf::signaldefinition_constructor_exists():
    assert callable(alf::SignalDefinition.__init__)


def test_alf::signaldefinition_constructor_args():
    sig = inspect.signature(alf::SignalDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::associationdefinition_is_not_abstract():
    assert not inspect.isabstract(alf::AssociationDefinition)


def test_alf::associationdefinition_constructor_exists():
    assert callable(alf::AssociationDefinition.__init__)


def test_alf::associationdefinition_constructor_args():
    sig = inspect.signature(alf::AssociationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::classdefinition_is_not_abstract():
    assert not inspect.isabstract(alf::ClassDefinition)


def test_alf::classdefinition_constructor_exists():
    assert callable(alf::ClassDefinition.__init__)


def test_alf::classdefinition_constructor_args():
    sig = inspect.signature(alf::ClassDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::classdeclaration_is_not_abstract():
    assert not inspect.isabstract(alf::ClassDeclaration)


def test_alf::classdeclaration_constructor_exists():
    assert callable(alf::ClassDeclaration.__init__)


def test_alf::classdeclaration_constructor_args():
    sig = inspect.signature(alf::ClassDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_alf::classdeclaration_has_isAbstract():
    assert hasattr(alf::ClassDeclaration, "isAbstract")
    descriptor = None
    for klass in alf::ClassDeclaration.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_alf::classifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(alf::ClassifierTemplateParameter)


def test_alf::classifiertemplateparameter_constructor_exists():
    assert callable(alf::ClassifierTemplateParameter.__init__)


def test_alf::classifiertemplateparameter_constructor_args():
    sig = inspect.signature(alf::ClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_alf::classifiertemplateparameter_has_comment():
    assert hasattr(alf::ClassifierTemplateParameter, "comment")
    descriptor = None
    for klass in alf::ClassifierTemplateParameter.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_alf::specializationclause_is_not_abstract():
    assert not inspect.isabstract(alf::SpecializationClause)


def test_alf::specializationclause_constructor_exists():
    assert callable(alf::SpecializationClause.__init__)


def test_alf::specializationclause_constructor_args():
    sig = inspect.signature(alf::SpecializationClause.__init__)
    params = list(sig.parameters.keys())



def test_packagedelementdefinition_is_not_abstract():
    assert not inspect.isabstract(PackagedElementDefinition)


def test_packagedelementdefinition_constructor_exists():
    assert callable(PackagedElementDefinition.__init__)


def test_packagedelementdefinition_constructor_args():
    sig = inspect.signature(PackagedElementDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::packagedefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf::PackageDefinitionOrStub)


def test_alf::packagedefinitionorstub_constructor_exists():
    assert callable(alf::PackageDefinitionOrStub.__init__)


def test_alf::packagedefinitionorstub_constructor_args():
    sig = inspect.signature(alf::PackageDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::templateparameters_is_not_abstract():
    assert not inspect.isabstract(alf::TemplateParameters)


def test_alf::templateparameters_constructor_exists():
    assert callable(alf::TemplateParameters.__init__)


def test_alf::templateparameters_constructor_args():
    sig = inspect.signature(alf::TemplateParameters.__init__)
    params = list(sig.parameters.keys())



def test_alf::packagebody_is_not_abstract():
    assert not inspect.isabstract(alf::PackageBody)


def test_alf::packagebody_constructor_exists():
    assert callable(alf::PackageBody.__init__)


def test_alf::packagebody_constructor_args():
    sig = inspect.signature(alf::PackageBody.__init__)
    params = list(sig.parameters.keys())



def test_alf::classifiersignature_is_not_abstract():
    assert not inspect.isabstract(alf::ClassifierSignature)


def test_alf::classifiersignature_constructor_exists():
    assert callable(alf::ClassifierSignature.__init__)


def test_alf::classifiersignature_constructor_args():
    sig = inspect.signature(alf::ClassifierSignature.__init__)
    params = list(sig.parameters.keys())



def test_classmemberdefinition_is_not_abstract():
    assert not inspect.isabstract(ClassMemberDefinition)


def test_classmemberdefinition_constructor_exists():
    assert callable(ClassMemberDefinition.__init__)


def test_classmemberdefinition_constructor_args():
    sig = inspect.signature(ClassMemberDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::classifierdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf::ClassifierDefinitionOrStub)


def test_alf::classifierdefinitionorstub_constructor_exists():
    assert callable(alf::ClassifierDefinitionOrStub.__init__)


def test_alf::classifierdefinitionorstub_constructor_args():
    sig = inspect.signature(alf::ClassifierDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::featuredefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf::FeatureDefinitionOrStub)


def test_alf::featuredefinitionorstub_constructor_exists():
    assert callable(alf::FeatureDefinitionOrStub.__init__)


def test_alf::featuredefinitionorstub_constructor_args():
    sig = inspect.signature(alf::FeatureDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_namespacedefinition_is_not_abstract():
    assert not inspect.isabstract(NamespaceDefinition)


def test_namespacedefinition_constructor_exists():
    assert callable(NamespaceDefinition.__init__)


def test_namespacedefinition_constructor_args():
    sig = inspect.signature(NamespaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::classifierdefinition_is_not_abstract():
    assert not inspect.isabstract(alf::ClassifierDefinition)


def test_alf::classifierdefinition_constructor_exists():
    assert callable(alf::ClassifierDefinition.__init__)


def test_alf::classifierdefinition_constructor_args():
    sig = inspect.signature(alf::ClassifierDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::packagedefinition_is_not_abstract():
    assert not inspect.isabstract(alf::PackageDefinition)


def test_alf::packagedefinition_constructor_exists():
    assert callable(alf::PackageDefinition.__init__)


def test_alf::packagedefinition_constructor_args():
    sig = inspect.signature(alf::PackageDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(alf::PackageDeclaration)


def test_alf::packagedeclaration_constructor_exists():
    assert callable(alf::PackageDeclaration.__init__)


def test_alf::packagedeclaration_constructor_args():
    sig = inspect.signature(alf::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_alf::visibilityindicator_is_not_abstract():
    assert not inspect.isabstract(alf::VisibilityIndicator)


def test_alf::visibilityindicator_constructor_exists():
    assert callable(alf::VisibilityIndicator.__init__)


def test_alf::visibilityindicator_constructor_args():
    sig = inspect.signature(alf::VisibilityIndicator.__init__)
    params = list(sig.parameters.keys())
    assert "PRIVATE" in params, "Missing parameter 'PRIVATE'"
    assert "PUBLIC" in params, "Missing parameter 'PUBLIC'"
    assert "PROTECTED" in params, "Missing parameter 'PROTECTED'"

def test_alf::visibilityindicator_has_PRIVATE():
    assert hasattr(alf::VisibilityIndicator, "PRIVATE")
    descriptor = None
    for klass in alf::VisibilityIndicator.__mro__:
        if "PRIVATE" in klass.__dict__:
            descriptor = klass.__dict__["PRIVATE"]
            break
    assert isinstance(descriptor, property)

def test_alf::visibilityindicator_has_PUBLIC():
    assert hasattr(alf::VisibilityIndicator, "PUBLIC")
    descriptor = None
    for klass in alf::VisibilityIndicator.__mro__:
        if "PUBLIC" in klass.__dict__:
            descriptor = klass.__dict__["PUBLIC"]
            break
    assert isinstance(descriptor, property)

def test_alf::visibilityindicator_has_PROTECTED():
    assert hasattr(alf::VisibilityIndicator, "PROTECTED")
    descriptor = None
    for klass in alf::VisibilityIndicator.__mro__:
        if "PROTECTED" in klass.__dict__:
            descriptor = klass.__dict__["PROTECTED"]
            break
    assert isinstance(descriptor, property)



def test_importreferencequalifiednamecompletion_is_not_abstract():
    assert not inspect.isabstract(ImportReferenceQualifiedNameCompletion)


def test_importreferencequalifiednamecompletion_constructor_exists():
    assert callable(ImportReferenceQualifiedNameCompletion.__init__)


def test_importreferencequalifiednamecompletion_constructor_args():
    sig = inspect.signature(ImportReferenceQualifiedNameCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::colonqualifiednamecompletionofimportreference_is_not_abstract():
    assert not inspect.isabstract(alf::ColonQualifiedNameCompletionOfImportReference)


def test_alf::colonqualifiednamecompletionofimportreference_constructor_exists():
    assert callable(alf::ColonQualifiedNameCompletionOfImportReference.__init__)


def test_alf::colonqualifiednamecompletionofimportreference_constructor_args():
    sig = inspect.signature(alf::ColonQualifiedNameCompletionOfImportReference.__init__)
    params = list(sig.parameters.keys())
    assert "star" in params, "Missing parameter 'star'"

def test_alf::colonqualifiednamecompletionofimportreference_has_star():
    assert hasattr(alf::ColonQualifiedNameCompletionOfImportReference, "star")
    descriptor = None
    for klass in alf::ColonQualifiedNameCompletionOfImportReference.__mro__:
        if "star" in klass.__dict__:
            descriptor = klass.__dict__["star"]
            break
    assert isinstance(descriptor, property)



def test_alf::aliasdefinition_is_not_abstract():
    assert not inspect.isabstract(alf::AliasDefinition)


def test_alf::aliasdefinition_constructor_exists():
    assert callable(alf::AliasDefinition.__init__)


def test_alf::aliasdefinition_constructor_args():
    sig = inspect.signature(alf::AliasDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::importreferencequalifiednamecompletion_is_not_abstract():
    assert not inspect.isabstract(alf::ImportReferenceQualifiedNameCompletion)


def test_alf::importreferencequalifiednamecompletion_constructor_exists():
    assert callable(alf::ImportReferenceQualifiedNameCompletion.__init__)


def test_alf::importreferencequalifiednamecompletion_constructor_args():
    sig = inspect.signature(alf::ImportReferenceQualifiedNameCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::name_is_not_abstract():
    assert not inspect.isabstract(alf::Name)


def test_alf::name_constructor_exists():
    assert callable(alf::Name.__init__)


def test_alf::name_constructor_args():
    sig = inspect.signature(alf::Name.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_alf::name_has_id():
    assert hasattr(alf::Name, "id")
    descriptor = None
    for klass in alf::Name.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_alf::primitive::literal_is_not_abstract():
    assert not inspect.isabstract(alf::PRIMITIVE::LITERAL)


def test_alf::primitive::literal_constructor_exists():
    assert callable(alf::PRIMITIVE::LITERAL.__init__)


def test_alf::primitive::literal_constructor_args():
    sig = inspect.signature(alf::PRIMITIVE::LITERAL.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_alf::primitive::literal_has_value():
    assert hasattr(alf::PRIMITIVE::LITERAL, "value")
    descriptor = None
    for klass in alf::PRIMITIVE::LITERAL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_alf::taggedvalue_is_not_abstract():
    assert not inspect.isabstract(alf::TaggedValue)


def test_alf::taggedvalue_constructor_exists():
    assert callable(alf::TaggedValue.__init__)


def test_alf::taggedvalue_constructor_args():
    sig = inspect.signature(alf::TaggedValue.__init__)
    params = list(sig.parameters.keys())



def test_taggedvalues_is_not_abstract():
    assert not inspect.isabstract(TaggedValues)


def test_taggedvalues_constructor_exists():
    assert callable(TaggedValues.__init__)


def test_taggedvalues_constructor_args():
    sig = inspect.signature(TaggedValues.__init__)
    params = list(sig.parameters.keys())



def test_alf::qualifiednamelist_is_not_abstract():
    assert not inspect.isabstract(alf::QualifiedNameList)


def test_alf::qualifiednamelist_constructor_exists():
    assert callable(alf::QualifiedNameList.__init__)


def test_alf::qualifiednamelist_constructor_args():
    sig = inspect.signature(alf::QualifiedNameList.__init__)
    params = list(sig.parameters.keys())



def test_alf::taggedvaluelist_is_not_abstract():
    assert not inspect.isabstract(alf::TaggedValueList)


def test_alf::taggedvaluelist_constructor_exists():
    assert callable(alf::TaggedValueList.__init__)


def test_alf::taggedvaluelist_constructor_args():
    sig = inspect.signature(alf::TaggedValueList.__init__)
    params = list(sig.parameters.keys())



def test_alf::taggedvalues_is_not_abstract():
    assert not inspect.isabstract(alf::TaggedValues)


def test_alf::taggedvalues_constructor_exists():
    assert callable(alf::TaggedValues.__init__)


def test_alf::taggedvalues_constructor_args():
    sig = inspect.signature(alf::TaggedValues.__init__)
    params = list(sig.parameters.keys())



def test_alf::qualifiedname_is_not_abstract():
    assert not inspect.isabstract(alf::QualifiedName)


def test_alf::qualifiedname_constructor_exists():
    assert callable(alf::QualifiedName.__init__)


def test_alf::qualifiedname_constructor_args():
    sig = inspect.signature(alf::QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_alf::stereotypeannotation_is_not_abstract():
    assert not inspect.isabstract(alf::StereotypeAnnotation)


def test_alf::stereotypeannotation_constructor_exists():
    assert callable(alf::StereotypeAnnotation.__init__)


def test_alf::stereotypeannotation_constructor_args():
    sig = inspect.signature(alf::StereotypeAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_number::literal_is_not_abstract():
    assert not inspect.isabstract(NUMBER::LITERAL)


def test_number::literal_constructor_exists():
    assert callable(NUMBER::LITERAL.__init__)


def test_number::literal_constructor_args():
    sig = inspect.signature(NUMBER::LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf::unlimited::natural_is_not_abstract():
    assert not inspect.isabstract(alf::UNLIMITED::NATURAL)


def test_alf::unlimited::natural_constructor_exists():
    assert callable(alf::UNLIMITED::NATURAL.__init__)


def test_alf::unlimited::natural_constructor_args():
    sig = inspect.signature(alf::UNLIMITED::NATURAL.__init__)
    params = list(sig.parameters.keys())



def test_alf::integer::literal_is_not_abstract():
    assert not inspect.isabstract(alf::INTEGER::LITERAL)


def test_alf::integer::literal_constructor_exists():
    assert callable(alf::INTEGER::LITERAL.__init__)


def test_alf::integer::literal_constructor_args():
    sig = inspect.signature(alf::INTEGER::LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_primitive::literal_is_not_abstract():
    assert not inspect.isabstract(PRIMITIVE::LITERAL)


def test_primitive::literal_constructor_exists():
    assert callable(PRIMITIVE::LITERAL.__init__)


def test_primitive::literal_constructor_args():
    sig = inspect.signature(PRIMITIVE::LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf::number::literal_is_not_abstract():
    assert not inspect.isabstract(alf::NUMBER::LITERAL)


def test_alf::number::literal_constructor_exists():
    assert callable(alf::NUMBER::LITERAL.__init__)


def test_alf::number::literal_constructor_args():
    sig = inspect.signature(alf::NUMBER::LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf::string::literal_is_not_abstract():
    assert not inspect.isabstract(alf::STRING::LITERAL)


def test_alf::string::literal_constructor_exists():
    assert callable(alf::STRING::LITERAL.__init__)


def test_alf::string::literal_constructor_args():
    sig = inspect.signature(alf::STRING::LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf::boolean::literal_is_not_abstract():
    assert not inspect.isabstract(alf::BOOLEAN::LITERAL)


def test_alf::boolean::literal_constructor_exists():
    assert callable(alf::BOOLEAN::LITERAL.__init__)


def test_alf::boolean::literal_constructor_args():
    sig = inspect.signature(alf::BOOLEAN::LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf::namespacedefinition_is_not_abstract():
    assert not inspect.isabstract(alf::NamespaceDefinition)


def test_alf::namespacedefinition_constructor_exists():
    assert callable(alf::NamespaceDefinition.__init__)


def test_alf::namespacedefinition_constructor_args():
    sig = inspect.signature(alf::NamespaceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::stereotypeannotations_is_not_abstract():
    assert not inspect.isabstract(alf::StereotypeAnnotations)


def test_alf::stereotypeannotations_constructor_exists():
    assert callable(alf::StereotypeAnnotations.__init__)


def test_alf::stereotypeannotations_constructor_args():
    sig = inspect.signature(alf::StereotypeAnnotations.__init__)
    params = list(sig.parameters.keys())



def test_alf::importdeclaration_is_not_abstract():
    assert not inspect.isabstract(alf::ImportDeclaration)


def test_alf::importdeclaration_constructor_exists():
    assert callable(alf::ImportDeclaration.__init__)


def test_alf::importdeclaration_constructor_args():
    sig = inspect.signature(alf::ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_alf::importdeclaration_has_visibility():
    assert hasattr(alf::ImportDeclaration, "visibility")
    descriptor = None
    for klass in alf::ImportDeclaration.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_alf::namespacedeclaration_is_not_abstract():
    assert not inspect.isabstract(alf::NamespaceDeclaration)


def test_alf::namespacedeclaration_constructor_exists():
    assert callable(alf::NamespaceDeclaration.__init__)


def test_alf::namespacedeclaration_constructor_args():
    sig = inspect.signature(alf::NamespaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_alf::unitdefinition_is_not_abstract():
    assert not inspect.isabstract(alf::UnitDefinition)


def test_alf::unitdefinition_constructor_exists():
    assert callable(alf::UnitDefinition.__init__)


def test_alf::unitdefinition_constructor_args():
    sig = inspect.signature(alf::UnitDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_alf::unitdefinition_has_comment():
    assert hasattr(alf::UnitDefinition, "comment")
    descriptor = None
    for klass in alf::UnitDefinition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_alf::importreference_is_not_abstract():
    assert not inspect.isabstract(alf::ImportReference)


def test_alf::importreference_constructor_exists():
    assert callable(alf::ImportReference.__init__)


def test_alf::importreference_constructor_args():
    sig = inspect.signature(alf::ImportReference.__init__)
    params = list(sig.parameters.keys())
    assert "star" in params, "Missing parameter 'star'"

def test_alf::importreference_has_star():
    assert hasattr(alf::ImportReference, "star")
    descriptor = None
    for klass in alf::ImportReference.__mro__:
        if "star" in klass.__dict__:
            descriptor = klass.__dict__["star"]
            break
    assert isinstance(descriptor, property)



def test_alf::conditionalandexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::ConditionalAndExpressionCompletion)


def test_alf::conditionalandexpressioncompletion_constructor_exists():
    assert callable(alf::ConditionalAndExpressionCompletion.__init__)


def test_alf::conditionalandexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::ConditionalAndExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ConditionalAndExpression)


def test_alf::conditionalandexpression_constructor_exists():
    assert callable(alf::ConditionalAndExpression.__init__)


def test_alf::conditionalandexpression_constructor_args():
    sig = inspect.signature(alf::ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::inclusiveorexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::InclusiveOrExpressionCompletion)


def test_alf::inclusiveorexpressioncompletion_constructor_exists():
    assert callable(alf::InclusiveOrExpressionCompletion.__init__)


def test_alf::inclusiveorexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::InclusiveOrExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(alf::InclusiveOrExpression)


def test_alf::inclusiveorexpression_constructor_exists():
    assert callable(alf::InclusiveOrExpression.__init__)


def test_alf::inclusiveorexpression_constructor_args():
    sig = inspect.signature(alf::InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::exclusiveorexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::ExclusiveOrExpressionCompletion)


def test_alf::exclusiveorexpressioncompletion_constructor_exists():
    assert callable(alf::ExclusiveOrExpressionCompletion.__init__)


def test_alf::exclusiveorexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::ExclusiveOrExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ExclusiveOrExpression)


def test_alf::exclusiveorexpression_constructor_exists():
    assert callable(alf::ExclusiveOrExpression.__init__)


def test_alf::exclusiveorexpression_constructor_args():
    sig = inspect.signature(alf::ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::andexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::AndExpressionCompletion)


def test_alf::andexpressioncompletion_constructor_exists():
    assert callable(alf::AndExpressionCompletion.__init__)


def test_alf::andexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::AndExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::shiftexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::ShiftExpressionCompletion)


def test_alf::shiftexpressioncompletion_constructor_exists():
    assert callable(alf::ShiftExpressionCompletion.__init__)


def test_alf::shiftexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::ShiftExpressionCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf::shiftexpressioncompletion_has_operator():
    assert hasattr(alf::ShiftExpressionCompletion, "operator")
    descriptor = None
    for klass in alf::ShiftExpressionCompletion.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ShiftExpression)


def test_alf::shiftexpression_constructor_exists():
    assert callable(alf::ShiftExpression.__init__)


def test_alf::shiftexpression_constructor_args():
    sig = inspect.signature(alf::ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(alf::EqualityExpression)


def test_alf::equalityexpression_constructor_exists():
    assert callable(alf::EqualityExpression.__init__)


def test_alf::equalityexpression_constructor_args():
    sig = inspect.signature(alf::EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::classificationexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::ClassificationExpressionCompletion)


def test_alf::classificationexpressioncompletion_constructor_exists():
    assert callable(alf::ClassificationExpressionCompletion.__init__)


def test_alf::classificationexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::ClassificationExpressionCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf::classificationexpressioncompletion_has_operator():
    assert hasattr(alf::ClassificationExpressionCompletion, "operator")
    descriptor = None
    for klass in alf::ClassificationExpressionCompletion.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf::classificationexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ClassificationExpression)


def test_alf::classificationexpression_constructor_exists():
    assert callable(alf::ClassificationExpression.__init__)


def test_alf::classificationexpression_constructor_args():
    sig = inspect.signature(alf::ClassificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::relationalexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::RelationalExpressionCompletion)


def test_alf::relationalexpressioncompletion_constructor_exists():
    assert callable(alf::RelationalExpressionCompletion.__init__)


def test_alf::relationalexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::RelationalExpressionCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "relationalOperator" in params, "Missing parameter 'relationalOperator'"

def test_alf::relationalexpressioncompletion_has_relationalOperator():
    assert hasattr(alf::RelationalExpressionCompletion, "relationalOperator")
    descriptor = None
    for klass in alf::RelationalExpressionCompletion.__mro__:
        if "relationalOperator" in klass.__dict__:
            descriptor = klass.__dict__["relationalOperator"]
            break
    assert isinstance(descriptor, property)



def test_alf::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(alf::RelationalExpression)


def test_alf::relationalexpression_constructor_exists():
    assert callable(alf::RelationalExpression.__init__)


def test_alf::relationalexpression_constructor_args():
    sig = inspect.signature(alf::RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::additiveexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::AdditiveExpressionCompletion)


def test_alf::additiveexpressioncompletion_constructor_exists():
    assert callable(alf::AdditiveExpressionCompletion.__init__)


def test_alf::additiveexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::AdditiveExpressionCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf::additiveexpressioncompletion_has_operator():
    assert hasattr(alf::AdditiveExpressionCompletion, "operator")
    descriptor = None
    for klass in alf::AdditiveExpressionCompletion.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf::additiveexpression_is_not_abstract():
    assert not inspect.isabstract(alf::AdditiveExpression)


def test_alf::additiveexpression_constructor_exists():
    assert callable(alf::AdditiveExpression.__init__)


def test_alf::additiveexpression_constructor_args():
    sig = inspect.signature(alf::AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::multiplicativeexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::MultiplicativeExpressionCompletion)


def test_alf::multiplicativeexpressioncompletion_constructor_exists():
    assert callable(alf::MultiplicativeExpressionCompletion.__init__)


def test_alf::multiplicativeexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::MultiplicativeExpressionCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf::multiplicativeexpressioncompletion_has_operator():
    assert hasattr(alf::MultiplicativeExpressionCompletion, "operator")
    descriptor = None
    for klass in alf::MultiplicativeExpressionCompletion.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf::multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(alf::MultiplicativeExpression)


def test_alf::multiplicativeexpression_constructor_exists():
    assert callable(alf::MultiplicativeExpression.__init__)


def test_alf::multiplicativeexpression_constructor_args():
    sig = inspect.signature(alf::MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::castcompletion_is_not_abstract():
    assert not inspect.isabstract(alf::CastCompletion)


def test_alf::castcompletion_constructor_exists():
    assert callable(alf::CastCompletion.__init__)


def test_alf::castcompletion_constructor_args():
    sig = inspect.signature(alf::CastCompletion.__init__)
    params = list(sig.parameters.keys())



def test_nonnameunaryexpression_is_not_abstract():
    assert not inspect.isabstract(NonNameUnaryExpression)


def test_nonnameunaryexpression_constructor_exists():
    assert callable(NonNameUnaryExpression.__init__)


def test_nonnameunaryexpression_constructor_args():
    sig = inspect.signature(NonNameUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::nonnamepostfixorcastexpression_is_not_abstract():
    assert not inspect.isabstract(alf::NonNamePostfixOrCastExpression)


def test_alf::nonnamepostfixorcastexpression_constructor_exists():
    assert callable(alf::NonNamePostfixOrCastExpression.__init__)


def test_alf::nonnamepostfixorcastexpression_constructor_args():
    sig = inspect.signature(alf::NonNamePostfixOrCastExpression.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"

def test_alf::nonnamepostfixorcastexpression_has_any():
    assert hasattr(alf::NonNamePostfixOrCastExpression, "any")
    descriptor = None
    for klass in alf::NonNamePostfixOrCastExpression.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_castcompletion_is_not_abstract():
    assert not inspect.isabstract(CastCompletion)


def test_castcompletion_constructor_exists():
    assert callable(CastCompletion.__init__)


def test_castcompletion_constructor_args():
    sig = inspect.signature(CastCompletion.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::nonpostfixnoncastunaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf::NonPostfixNonCastUnaryExpression)


def test_alf::nonpostfixnoncastunaryexpression_constructor_exists():
    assert callable(alf::NonPostfixNonCastUnaryExpression.__init__)


def test_alf::nonpostfixnoncastunaryexpression_constructor_args():
    sig = inspect.signature(alf::NonPostfixNonCastUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::postfixorcastexpression_is_not_abstract():
    assert not inspect.isabstract(alf::PostfixOrCastExpression)


def test_alf::postfixorcastexpression_constructor_exists():
    assert callable(alf::PostfixOrCastExpression.__init__)


def test_alf::postfixorcastexpression_constructor_args():
    sig = inspect.signature(alf::PostfixOrCastExpression.__init__)
    params = list(sig.parameters.keys())



def test_nonpostfixnoncastunaryexpression_is_not_abstract():
    assert not inspect.isabstract(NonPostfixNonCastUnaryExpression)


def test_nonpostfixnoncastunaryexpression_constructor_exists():
    assert callable(NonPostfixNonCastUnaryExpression.__init__)


def test_nonpostfixnoncastunaryexpression_constructor_args():
    sig = inspect.signature(NonPostfixNonCastUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::numericunaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf::NumericUnaryExpression)


def test_alf::numericunaryexpression_constructor_exists():
    assert callable(alf::NumericUnaryExpression.__init__)


def test_alf::numericunaryexpression_constructor_args():
    sig = inspect.signature(alf::NumericUnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf::numericunaryexpression_has_operator():
    assert hasattr(alf::NumericUnaryExpression, "operator")
    descriptor = None
    for klass in alf::NumericUnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf::booleannegationexpression_is_not_abstract():
    assert not inspect.isabstract(alf::BooleanNegationExpression)


def test_alf::booleannegationexpression_constructor_exists():
    assert callable(alf::BooleanNegationExpression.__init__)


def test_alf::booleannegationexpression_constructor_args():
    sig = inspect.signature(alf::BooleanNegationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::isolationexpression_is_not_abstract():
    assert not inspect.isabstract(alf::IsolationExpression)


def test_alf::isolationexpression_constructor_exists():
    assert callable(alf::IsolationExpression.__init__)


def test_alf::isolationexpression_constructor_args():
    sig = inspect.signature(alf::IsolationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::bitstringcomplementexpression_is_not_abstract():
    assert not inspect.isabstract(alf::BitStringComplementExpression)


def test_alf::bitstringcomplementexpression_constructor_exists():
    assert callable(alf::BitStringComplementExpression.__init__)


def test_alf::bitstringcomplementexpression_constructor_args():
    sig = inspect.signature(alf::BitStringComplementExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::prefixexpression_is_not_abstract():
    assert not inspect.isabstract(alf::PrefixExpression)


def test_alf::prefixexpression_constructor_exists():
    assert callable(alf::PrefixExpression.__init__)


def test_alf::prefixexpression_constructor_args():
    sig = inspect.signature(alf::PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf::prefixexpression_has_operator():
    assert hasattr(alf::PrefixExpression, "operator")
    descriptor = None
    for klass in alf::PrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf::postfixoperation_is_not_abstract():
    assert not inspect.isabstract(alf::PostfixOperation)


def test_alf::postfixoperation_constructor_exists():
    assert callable(alf::PostfixOperation.__init__)


def test_alf::postfixoperation_constructor_args():
    sig = inspect.signature(alf::PostfixOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_alf::postfixoperation_has_operator():
    assert hasattr(alf::PostfixOperation, "operator")
    descriptor = None
    for klass in alf::PostfixOperation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_alf::eobject_is_not_abstract():
    assert not inspect.isabstract(alf::EObject)


def test_alf::eobject_constructor_exists():
    assert callable(alf::EObject.__init__)


def test_alf::eobject_constructor_args():
    sig = inspect.signature(alf::EObject.__init__)
    params = list(sig.parameters.keys())



def test_alf::sequenceelement_is_not_abstract():
    assert not inspect.isabstract(alf::SequenceElement)


def test_alf::sequenceelement_constructor_exists():
    assert callable(alf::SequenceElement.__init__)


def test_alf::sequenceelement_constructor_args():
    sig = inspect.signature(alf::SequenceElement.__init__)
    params = list(sig.parameters.keys())



def test_alf::sequenceelementlistcompletion_is_not_abstract():
    assert not inspect.isabstract(alf::SequenceElementListCompletion)


def test_alf::sequenceelementlistcompletion_constructor_exists():
    assert callable(alf::SequenceElementListCompletion.__init__)


def test_alf::sequenceelementlistcompletion_constructor_args():
    sig = inspect.signature(alf::SequenceElementListCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::sequenceelements_is_not_abstract():
    assert not inspect.isabstract(alf::SequenceElements)


def test_alf::sequenceelements_constructor_exists():
    assert callable(alf::SequenceElements.__init__)


def test_alf::sequenceelements_constructor_args():
    sig = inspect.signature(alf::SequenceElements.__init__)
    params = list(sig.parameters.keys())



def test_alf::multiplicityindicator_is_not_abstract():
    assert not inspect.isabstract(alf::MultiplicityIndicator)


def test_alf::multiplicityindicator_constructor_exists():
    assert callable(alf::MultiplicityIndicator.__init__)


def test_alf::multiplicityindicator_constructor_args():
    sig = inspect.signature(alf::MultiplicityIndicator.__init__)
    params = list(sig.parameters.keys())



def test_alf::indexednamedexpression_is_not_abstract():
    assert not inspect.isabstract(alf::IndexedNamedExpression)


def test_alf::indexednamedexpression_constructor_exists():
    assert callable(alf::IndexedNamedExpression.__init__)


def test_alf::indexednamedexpression_constructor_args():
    sig = inspect.signature(alf::IndexedNamedExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::indexednamedexpressionlistcompletion_is_not_abstract():
    assert not inspect.isabstract(alf::IndexedNamedExpressionListCompletion)


def test_alf::indexednamedexpressionlistcompletion_constructor_exists():
    assert callable(alf::IndexedNamedExpressionListCompletion.__init__)


def test_alf::indexednamedexpressionlistcompletion_constructor_args():
    sig = inspect.signature(alf::IndexedNamedExpressionListCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::linkoperationtuple_is_not_abstract():
    assert not inspect.isabstract(alf::LinkOperationTuple)


def test_alf::linkoperationtuple_constructor_exists():
    assert callable(alf::LinkOperationTuple.__init__)


def test_alf::linkoperationtuple_constructor_args():
    sig = inspect.signature(alf::LinkOperationTuple.__init__)
    params = list(sig.parameters.keys())



def test_baseexpression_is_not_abstract():
    assert not inspect.isabstract(BaseExpression)


def test_baseexpression_constructor_exists():
    assert callable(BaseExpression.__init__)


def test_baseexpression_constructor_args():
    sig = inspect.signature(BaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::superinvocationexpression_is_not_abstract():
    assert not inspect.isabstract(alf::SuperInvocationExpression)


def test_alf::superinvocationexpression_constructor_exists():
    assert callable(alf::SuperInvocationExpression.__init__)


def test_alf::superinvocationexpression_constructor_args():
    sig = inspect.signature(alf::SuperInvocationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::instancecreationorsequenceconstructionexpression_is_not_abstract():
    assert not inspect.isabstract(alf::InstanceCreationOrSequenceConstructionExpression)


def test_alf::instancecreationorsequenceconstructionexpression_constructor_exists():
    assert callable(alf::InstanceCreationOrSequenceConstructionExpression.__init__)


def test_alf::instancecreationorsequenceconstructionexpression_constructor_args():
    sig = inspect.signature(alf::InstanceCreationOrSequenceConstructionExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::sequenceanyexpression_is_not_abstract():
    assert not inspect.isabstract(alf::SequenceAnyExpression)


def test_alf::sequenceanyexpression_constructor_exists():
    assert callable(alf::SequenceAnyExpression.__init__)


def test_alf::sequenceanyexpression_constructor_args():
    sig = inspect.signature(alf::SequenceAnyExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::literalexpression_is_not_abstract():
    assert not inspect.isabstract(alf::LiteralExpression)


def test_alf::literalexpression_constructor_exists():
    assert callable(alf::LiteralExpression.__init__)


def test_alf::literalexpression_constructor_args():
    sig = inspect.signature(alf::LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::index_is_not_abstract():
    assert not inspect.isabstract(alf::Index)


def test_alf::index_constructor_exists():
    assert callable(alf::Index.__init__)


def test_alf::index_constructor_args():
    sig = inspect.signature(alf::Index.__init__)
    params = list(sig.parameters.keys())



def test_alf::namedexpression_is_not_abstract():
    assert not inspect.isabstract(alf::NamedExpression)


def test_alf::namedexpression_constructor_exists():
    assert callable(alf::NamedExpression.__init__)


def test_alf::namedexpression_constructor_args():
    sig = inspect.signature(alf::NamedExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::positionaltupleexpressionlistcompletion_is_not_abstract():
    assert not inspect.isabstract(alf::PositionalTupleExpressionListCompletion)


def test_alf::positionaltupleexpressionlistcompletion_constructor_exists():
    assert callable(alf::PositionalTupleExpressionListCompletion.__init__)


def test_alf::positionaltupleexpressionlistcompletion_constructor_args():
    sig = inspect.signature(alf::PositionalTupleExpressionListCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::positionaltupleexpressionlist_is_not_abstract():
    assert not inspect.isabstract(alf::PositionalTupleExpressionList)


def test_alf::positionaltupleexpressionlist_constructor_exists():
    assert callable(alf::PositionalTupleExpressionList.__init__)


def test_alf::positionaltupleexpressionlist_constructor_args():
    sig = inspect.signature(alf::PositionalTupleExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_alf::namedtupleexpressionlist_is_not_abstract():
    assert not inspect.isabstract(alf::NamedTupleExpressionList)


def test_alf::namedtupleexpressionlist_constructor_exists():
    assert callable(alf::NamedTupleExpressionList.__init__)


def test_alf::namedtupleexpressionlist_constructor_args():
    sig = inspect.signature(alf::NamedTupleExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_alf::tuple_is_not_abstract():
    assert not inspect.isabstract(alf::Tuple)


def test_alf::tuple_constructor_exists():
    assert callable(alf::Tuple.__init__)


def test_alf::tuple_constructor_args():
    sig = inspect.signature(alf::Tuple.__init__)
    params = list(sig.parameters.keys())



def test_alf::thisexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ThisExpression)


def test_alf::thisexpression_constructor_exists():
    assert callable(alf::ThisExpression.__init__)


def test_alf::thisexpression_constructor_args():
    sig = inspect.signature(alf::ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::expressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::ExpressionCompletion)


def test_alf::expressioncompletion_constructor_exists():
    assert callable(alf::ExpressionCompletion.__init__)


def test_alf::expressioncompletion_constructor_args():
    sig = inspect.signature(alf::ExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf::UnaryExpression)


def test_alf::unaryexpression_constructor_exists():
    assert callable(alf::UnaryExpression.__init__)


def test_alf::unaryexpression_constructor_args():
    sig = inspect.signature(alf::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_initializationexpression_is_not_abstract():
    assert not inspect.isabstract(InitializationExpression)


def test_initializationexpression_constructor_exists():
    assert callable(InitializationExpression.__init__)


def test_initializationexpression_constructor_args():
    sig = inspect.signature(InitializationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::instanceinitializationexpression_is_not_abstract():
    assert not inspect.isabstract(alf::InstanceInitializationExpression)


def test_alf::instanceinitializationexpression_constructor_exists():
    assert callable(alf::InstanceInitializationExpression.__init__)


def test_alf::instanceinitializationexpression_constructor_args():
    sig = inspect.signature(alf::InstanceInitializationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::sequenceinitializationexpression_is_not_abstract():
    assert not inspect.isabstract(alf::SequenceInitializationExpression)


def test_alf::sequenceinitializationexpression_constructor_exists():
    assert callable(alf::SequenceInitializationExpression.__init__)


def test_alf::sequenceinitializationexpression_constructor_args():
    sig = inspect.signature(alf::SequenceInitializationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNew" in params, "Missing parameter 'isNew'"

def test_alf::sequenceinitializationexpression_has_isNew():
    assert hasattr(alf::SequenceInitializationExpression, "isNew")
    descriptor = None
    for klass in alf::SequenceInitializationExpression.__mro__:
        if "isNew" in klass.__dict__:
            descriptor = klass.__dict__["isNew"]
            break
    assert isinstance(descriptor, property)



def test_alf::expression_is_not_abstract():
    assert not inspect.isabstract(alf::Expression)


def test_alf::expression_constructor_exists():
    assert callable(alf::Expression.__init__)


def test_alf::expression_constructor_args():
    sig = inspect.signature(alf::Expression.__init__)
    params = list(sig.parameters.keys())



def test_alf::sequenceoperationorreductionorexpansion_is_not_abstract():
    assert not inspect.isabstract(alf::SequenceOperationOrReductionOrExpansion)


def test_alf::sequenceoperationorreductionorexpansion_constructor_exists():
    assert callable(alf::SequenceOperationOrReductionOrExpansion.__init__)


def test_alf::sequenceoperationorreductionorexpansion_constructor_args():
    sig = inspect.signature(alf::SequenceOperationOrReductionOrExpansion.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "id" in params, "Missing parameter 'id'"
    assert "isReduce" in params, "Missing parameter 'isReduce'"

def test_alf::sequenceoperationorreductionorexpansion_has_isOrdered():
    assert hasattr(alf::SequenceOperationOrReductionOrExpansion, "isOrdered")
    descriptor = None
    for klass in alf::SequenceOperationOrReductionOrExpansion.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_alf::sequenceoperationorreductionorexpansion_has_id():
    assert hasattr(alf::SequenceOperationOrReductionOrExpansion, "id")
    descriptor = None
    for klass in alf::SequenceOperationOrReductionOrExpansion.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_alf::sequenceoperationorreductionorexpansion_has_isReduce():
    assert hasattr(alf::SequenceOperationOrReductionOrExpansion, "isReduce")
    descriptor = None
    for klass in alf::SequenceOperationOrReductionOrExpansion.__mro__:
        if "isReduce" in klass.__dict__:
            descriptor = klass.__dict__["isReduce"]
            break
    assert isinstance(descriptor, property)



def test_alf::featureinvocation_is_not_abstract():
    assert not inspect.isabstract(alf::FeatureInvocation)


def test_alf::featureinvocation_constructor_exists():
    assert callable(alf::FeatureInvocation.__init__)


def test_alf::featureinvocation_constructor_args():
    sig = inspect.signature(alf::FeatureInvocation.__init__)
    params = list(sig.parameters.keys())



def test_alf::feature_is_not_abstract():
    assert not inspect.isabstract(alf::Feature)


def test_alf::feature_constructor_exists():
    assert callable(alf::Feature.__init__)


def test_alf::feature_constructor_args():
    sig = inspect.signature(alf::Feature.__init__)
    params = list(sig.parameters.keys())



def test_alf::feature::or::sequenceoperationorreductionorexpansion::or::index_is_not_abstract():
    assert not inspect.isabstract(alf::Feature::Or::SequenceOperationOrReductionOrExpansion::Or::Index)


def test_alf::feature::or::sequenceoperationorreductionorexpansion::or::index_constructor_exists():
    assert callable(alf::Feature::Or::SequenceOperationOrReductionOrExpansion::Or::Index.__init__)


def test_alf::feature::or::sequenceoperationorreductionorexpansion::or::index_constructor_args():
    sig = inspect.signature(alf::Feature::Or::SequenceOperationOrReductionOrExpansion::Or::Index.__init__)
    params = list(sig.parameters.keys())



def test_alf::behaviorinvocation_is_not_abstract():
    assert not inspect.isabstract(alf::BehaviorInvocation)


def test_alf::behaviorinvocation_constructor_exists():
    assert callable(alf::BehaviorInvocation.__init__)


def test_alf::behaviorinvocation_constructor_args():
    sig = inspect.signature(alf::BehaviorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_alf::sequenceconstructionexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::SequenceConstructionExpressionCompletion)


def test_alf::sequenceconstructionexpressioncompletion_constructor_exists():
    assert callable(alf::SequenceConstructionExpressionCompletion.__init__)


def test_alf::sequenceconstructionexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::SequenceConstructionExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::classextentexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::ClassExtentExpressionCompletion)


def test_alf::classextentexpressioncompletion_constructor_exists():
    assert callable(alf::ClassExtentExpressionCompletion.__init__)


def test_alf::classextentexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::ClassExtentExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::linkoperationcompletion_is_not_abstract():
    assert not inspect.isabstract(alf::LinkOperationCompletion)


def test_alf::linkoperationcompletion_constructor_exists():
    assert callable(alf::LinkOperationCompletion.__init__)


def test_alf::linkoperationcompletion_constructor_args():
    sig = inspect.signature(alf::LinkOperationCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "linkOperation" in params, "Missing parameter 'linkOperation'"

def test_alf::linkoperationcompletion_has_linkOperation():
    assert hasattr(alf::LinkOperationCompletion, "linkOperation")
    descriptor = None
    for klass in alf::LinkOperationCompletion.__mro__:
        if "linkOperation" in klass.__dict__:
            descriptor = klass.__dict__["linkOperation"]
            break
    assert isinstance(descriptor, property)



def test_alf::primaryexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::PrimaryExpressionCompletion)


def test_alf::primaryexpressioncompletion_constructor_exists():
    assert callable(alf::PrimaryExpressionCompletion.__init__)


def test_alf::primaryexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::PrimaryExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ParenthesizedExpression)


def test_alf::parenthesizedexpression_constructor_exists():
    assert callable(alf::ParenthesizedExpression.__init__)


def test_alf::parenthesizedexpression_constructor_args():
    sig = inspect.signature(alf::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::baseexpression_is_not_abstract():
    assert not inspect.isabstract(alf::BaseExpression)


def test_alf::baseexpression_constructor_exists():
    assert callable(alf::BaseExpression.__init__)


def test_alf::baseexpression_constructor_args():
    sig = inspect.signature(alf::BaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::nameorprimaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf::NameOrPrimaryExpression)


def test_alf::nameorprimaryexpression_constructor_exists():
    assert callable(alf::NameOrPrimaryExpression.__init__)


def test_alf::nameorprimaryexpression_constructor_args():
    sig = inspect.signature(alf::NameOrPrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf::PrimaryExpression)


def test_alf::primaryexpression_constructor_exists():
    assert callable(alf::PrimaryExpression.__init__)


def test_alf::primaryexpression_constructor_args():
    sig = inspect.signature(alf::PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::postfixexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::PostfixExpressionCompletion)


def test_alf::postfixexpressioncompletion_constructor_exists():
    assert callable(alf::PostfixExpressionCompletion.__init__)


def test_alf::postfixexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::PostfixExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::primarytoexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::PrimaryToExpressionCompletion)


def test_alf::primarytoexpressioncompletion_constructor_exists():
    assert callable(alf::PrimaryToExpressionCompletion.__init__)


def test_alf::primarytoexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::PrimaryToExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::nametoprimaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf::NameToPrimaryExpression)


def test_alf::nametoprimaryexpression_constructor_exists():
    assert callable(alf::NameToPrimaryExpression.__init__)


def test_alf::nametoprimaryexpression_constructor_args():
    sig = inspect.signature(alf::NameToPrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::nametoexpressioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::NameToExpressionCompletion)


def test_alf::nametoexpressioncompletion_constructor_exists():
    assert callable(alf::NameToExpressionCompletion.__init__)


def test_alf::nametoexpressioncompletion_constructor_args():
    sig = inspect.signature(alf::NameToExpressionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::nonnameunaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf::NonNameUnaryExpression)


def test_alf::nonnameunaryexpression_constructor_exists():
    assert callable(alf::NonNameUnaryExpression.__init__)


def test_alf::nonnameunaryexpression_constructor_args():
    sig = inspect.signature(alf::NonNameUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::nonnameexpression_is_not_abstract():
    assert not inspect.isabstract(alf::NonNameExpression)


def test_alf::nonnameexpression_constructor_exists():
    assert callable(alf::NonNameExpression.__init__)


def test_alf::nonnameexpression_constructor_args():
    sig = inspect.signature(alf::NonNameExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::signalreceptiondeclaration_is_not_abstract():
    assert not inspect.isabstract(alf::SignalReceptionDeclaration)


def test_alf::signalreceptiondeclaration_constructor_exists():
    assert callable(alf::SignalReceptionDeclaration.__init__)


def test_alf::signalreceptiondeclaration_constructor_args():
    sig = inspect.signature(alf::SignalReceptionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_alf::templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(alf::TemplateParameterSubstitution)


def test_alf::templateparametersubstitution_constructor_exists():
    assert callable(alf::TemplateParameterSubstitution.__init__)


def test_alf::templateparametersubstitution_constructor_args():
    sig = inspect.signature(alf::TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_templatebinding_is_not_abstract():
    assert not inspect.isabstract(TemplateBinding)


def test_templatebinding_constructor_exists():
    assert callable(TemplateBinding.__init__)


def test_templatebinding_constructor_args():
    sig = inspect.signature(TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_alf::namedtemplatebinding_is_not_abstract():
    assert not inspect.isabstract(alf::NamedTemplateBinding)


def test_alf::namedtemplatebinding_constructor_exists():
    assert callable(alf::NamedTemplateBinding.__init__)


def test_alf::namedtemplatebinding_constructor_args():
    sig = inspect.signature(alf::NamedTemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_alf::positionaltemplatebinding_is_not_abstract():
    assert not inspect.isabstract(alf::PositionalTemplateBinding)


def test_alf::positionaltemplatebinding_constructor_exists():
    assert callable(alf::PositionalTemplateBinding.__init__)


def test_alf::positionaltemplatebinding_constructor_args():
    sig = inspect.signature(alf::PositionalTemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_alf::colonqualifiednamecompletionwithoutbinding_is_not_abstract():
    assert not inspect.isabstract(alf::ColonQualifiedNameCompletionWithoutBinding)


def test_alf::colonqualifiednamecompletionwithoutbinding_constructor_exists():
    assert callable(alf::ColonQualifiedNameCompletionWithoutBinding.__init__)


def test_alf::colonqualifiednamecompletionwithoutbinding_constructor_args():
    sig = inspect.signature(alf::ColonQualifiedNameCompletionWithoutBinding.__init__)
    params = list(sig.parameters.keys())



def test_alf::qualifiednamewithoutbinding_is_not_abstract():
    assert not inspect.isabstract(alf::QualifiedNameWithoutBinding)


def test_alf::qualifiednamewithoutbinding_constructor_exists():
    assert callable(alf::QualifiedNameWithoutBinding.__init__)


def test_alf::qualifiednamewithoutbinding_constructor_args():
    sig = inspect.signature(alf::QualifiedNameWithoutBinding.__init__)
    params = list(sig.parameters.keys())



def test_alf::templatebinding_is_not_abstract():
    assert not inspect.isabstract(alf::TemplateBinding)


def test_alf::templatebinding_constructor_exists():
    assert callable(alf::TemplateBinding.__init__)


def test_alf::templatebinding_constructor_args():
    sig = inspect.signature(alf::TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_unqualifiedname_is_not_abstract():
    assert not inspect.isabstract(UnqualifiedName)


def test_unqualifiedname_constructor_exists():
    assert callable(UnqualifiedName.__init__)


def test_unqualifiedname_constructor_args():
    sig = inspect.signature(UnqualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_alf::namebinding_is_not_abstract():
    assert not inspect.isabstract(alf::NameBinding)


def test_alf::namebinding_constructor_exists():
    assert callable(alf::NameBinding.__init__)


def test_alf::namebinding_constructor_args():
    sig = inspect.signature(alf::NameBinding.__init__)
    params = list(sig.parameters.keys())



def test_alf::colonqualifiednamecompletion_is_not_abstract():
    assert not inspect.isabstract(alf::ColonQualifiedNameCompletion)


def test_alf::colonqualifiednamecompletion_constructor_exists():
    assert callable(alf::ColonQualifiedNameCompletion.__init__)


def test_alf::colonqualifiednamecompletion_constructor_args():
    sig = inspect.signature(alf::ColonQualifiedNameCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::unqualifiedname_is_not_abstract():
    assert not inspect.isabstract(alf::UnqualifiedName)


def test_alf::unqualifiedname_constructor_exists():
    assert callable(alf::UnqualifiedName.__init__)


def test_alf::unqualifiedname_constructor_args():
    sig = inspect.signature(alf::UnqualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_alf::initializationexpression_is_not_abstract():
    assert not inspect.isabstract(alf::InitializationExpression)


def test_alf::initializationexpression_constructor_exists():
    assert callable(alf::InitializationExpression.__init__)


def test_alf::initializationexpression_constructor_args():
    sig = inspect.signature(alf::InitializationExpression.__init__)
    params = list(sig.parameters.keys())



def test_activefeaturedefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(ActiveFeatureDefinitionOrStub)


def test_activefeaturedefinitionorstub_constructor_exists():
    assert callable(ActiveFeatureDefinitionOrStub.__init__)


def test_activefeaturedefinitionorstub_constructor_args():
    sig = inspect.signature(ActiveFeatureDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::signalreceptiondefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf::SignalReceptionDefinitionOrStub)


def test_alf::signalreceptiondefinitionorstub_constructor_exists():
    assert callable(alf::SignalReceptionDefinitionOrStub.__init__)


def test_alf::signalreceptiondefinitionorstub_constructor_args():
    sig = inspect.signature(alf::SignalReceptionDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::receptiondefinition_is_not_abstract():
    assert not inspect.isabstract(alf::ReceptionDefinition)


def test_alf::receptiondefinition_constructor_exists():
    assert callable(alf::ReceptionDefinition.__init__)


def test_alf::receptiondefinition_constructor_args():
    sig = inspect.signature(alf::ReceptionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_alf::attributeinitializer_is_not_abstract():
    assert not inspect.isabstract(alf::AttributeInitializer)


def test_alf::attributeinitializer_constructor_exists():
    assert callable(alf::AttributeInitializer.__init__)


def test_alf::attributeinitializer_constructor_args():
    sig = inspect.signature(alf::AttributeInitializer.__init__)
    params = list(sig.parameters.keys())



def test_alf::operationdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf::OperationDefinitionOrStub)


def test_alf::operationdefinitionorstub_constructor_exists():
    assert callable(alf::OperationDefinitionOrStub.__init__)


def test_alf::operationdefinitionorstub_constructor_args():
    sig = inspect.signature(alf::OperationDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())

def test_parameterdirection_exists():
    # Check that the Enumeration exists
    assert ParameterDirection is not None

def test_parameterdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirection]
    expected_literals = [
        "INOUT",
        "IN",
        "OUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirection"

def test_classificationoperator_exists():
    # Check that the Enumeration exists
    assert ClassificationOperator is not None

def test_classificationoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ClassificationOperator]
    expected_literals = [
        "INSTANCEOF",
        "HASTYPE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ClassificationOperator"

def test_shiftoperator_exists():
    # Check that the Enumeration exists
    assert ShiftOperator is not None

def test_shiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShiftOperator]
    expected_literals = [
        "RSHIFT",
        "URSHIFT",
        "LSHIFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShiftOperator"

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "MINUSASSIGN",
        "REMASSIGN",
        "RSHIFTASSIGN",
        "URSHIFTASSIGN",
        "ANSASSIGN",
        "STARASSIGN",
        "LSHIFTASSIGN",
        "PLUSASSIGN",
        "XORASSIGN",
        "ASSIGN",
        "ORASSIGN",
        "SLASHASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_multiplicativeoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicativeOperator is not None

def test_multiplicativeoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicativeOperator]
    expected_literals = [
        "STAR",
        "SLASH",
        "REM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicativeOperator"

def test_importvisibilityindicator_exists():
    # Check that the Enumeration exists
    assert ImportVisibilityIndicator is not None

def test_importvisibilityindicator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImportVisibilityIndicator]
    expected_literals = [
        "PUBLIC",
        "PRIVATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImportVisibilityIndicator"

def test_equalityoperator_exists():
    # Check that the Enumeration exists
    assert EqualityOperator is not None

def test_equalityoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EqualityOperator]
    expected_literals = [
        "EQ",
        "NE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EqualityOperator"

def test_affixoperator_exists():
    # Check that the Enumeration exists
    assert AffixOperator is not None

def test_affixoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AffixOperator]
    expected_literals = [
        "INCR",
        "DECR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AffixOperator"

def test_linkoperation_exists():
    # Check that the Enumeration exists
    assert LinkOperation is not None

def test_linkoperation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkOperation]
    expected_literals = [
        "CREATE_LINK",
        "DESTROY_LINK",
        "CLEAR_ASSOC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkOperation"

def test_numericunaryoperator_exists():
    # Check that the Enumeration exists
    assert NumericUnaryOperator is not None

def test_numericunaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumericUnaryOperator]
    expected_literals = [
        "PLUS",
        "MINUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericUnaryOperator"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "LE",
        "GT",
        "LT",
        "GE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_additiveoperator_exists():
    # Check that the Enumeration exists
    assert AdditiveOperator is not None

def test_additiveoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdditiveOperator]
    expected_literals = [
        "PLUS",
        "MINUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdditiveOperator"


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
alf::AcceptClause_strategy = st.builds(
    alf::AcceptClause,
)
alf::ReclassifyAllClause_strategy = st.builds(
    alf::ReclassifyAllClause,
)
alf::ClassificationToClause_strategy = st.builds(
    alf::ClassificationToClause,
)
alf::ClassificationFromClause_strategy = st.builds(
    alf::ClassificationFromClause,
)
alf::ClassificationClause_strategy = st.builds(
    alf::ClassificationClause,
)
alf::AcceptBlock_strategy = st.builds(
    alf::AcceptBlock,
)
alf::CompoundAcceptStatementCompletion_strategy = st.builds(
    alf::CompoundAcceptStatementCompletion,
)
alf::SimpleAcceptStatementCompletion_strategy = st.builds(
    alf::SimpleAcceptStatementCompletion,
)
alf::NonEmptyStatementSequence_strategy = st.builds(
    alf::NonEmptyStatementSequence,
)
alf::SwitchCase_strategy = st.builds(
    alf::SwitchCase,
)
alf::SwitchDefaultClause_strategy = st.builds(
    alf::SwitchDefaultClause,
)
alf::SwitchClause_strategy = st.builds(
    alf::SwitchClause,
)
alf::LoopVariableDefinition_strategy = st.builds(
    alf::LoopVariableDefinition,
)
alf::ForControl_strategy = st.builds(
    alf::ForControl,
)
alf::LocalNameDeclarationStatementCompletion_strategy = st.builds(
    alf::LocalNameDeclarationStatementCompletion,
)
alf::NonFinalClause_strategy = st.builds(
    alf::NonFinalClause,
)
alf::ConcurrentClauses_strategy = st.builds(
    alf::ConcurrentClauses,
)
alf::FinalClause_strategy = st.builds(
    alf::FinalClause,
)
alf::SequentialClauses_strategy = st.builds(
    alf::SequentialClauses,
)
alf::NameList_strategy = st.builds(
    alf::NameList,
)
alf::Annotation_strategy = st.builds(
    alf::Annotation,
    id=
        safe_text
)
alf::ConditionalExpression_strategy = st.builds(
    alf::ConditionalExpression,
)
alf::ConditionalOrExpressionCompletion_strategy = st.builds(
    alf::ConditionalOrExpressionCompletion,
)
alf::ConditionalOrExpression_strategy = st.builds(
    alf::ConditionalOrExpression,
)
alf::Annotations_strategy = st.builds(
    alf::Annotations,
)
Statement_strategy = st.builds(
    Statement,
)
alf::ReturnStatement_strategy = st.builds(
    alf::ReturnStatement,
)
alf::SwitchStatement_strategy = st.builds(
    alf::SwitchStatement,
)
alf::ClassifyStatement_strategy = st.builds(
    alf::ClassifyStatement,
)
alf::BreakStatement_strategy = st.builds(
    alf::BreakStatement,
)
alf::DoStatement_strategy = st.builds(
    alf::DoStatement,
)
alf::InLineStatement_strategy = st.builds(
    alf::InLineStatement,
    id=
        safe_text
)
alf::EmptyStatement_strategy = st.builds(
    alf::EmptyStatement,
)
alf::WhileStatement_strategy = st.builds(
    alf::WhileStatement,
)
alf::ForStatement_strategy = st.builds(
    alf::ForStatement,
)
alf::BlockStatement_strategy = st.builds(
    alf::BlockStatement,
)
alf::IfStatement_strategy = st.builds(
    alf::IfStatement,
)
alf::AcceptStatement_strategy = st.builds(
    alf::AcceptStatement,
)
alf::LocalNameDeclarationStatement_strategy = st.builds(
    alf::LocalNameDeclarationStatement,
)
alf::LocalNameDeclarationOrExpressionStatement_strategy = st.builds(
    alf::LocalNameDeclarationOrExpressionStatement,
)
alf::AnnotatedStatement_strategy = st.builds(
    alf::AnnotatedStatement,
)
alf::Statement_strategy = st.builds(
    alf::Statement,
)
alf::DocumentedStatement_strategy = st.builds(
    alf::DocumentedStatement,
    comment=
        safe_text
)
alf::StatementSequence_strategy = st.builds(
    alf::StatementSequence,
)
ExpressionCompletion_strategy = st.builds(
    ExpressionCompletion,
)
alf::AssignmentExpressionCompletion_strategy = st.builds(
    alf::AssignmentExpressionCompletion,
    operator=
        safe_text
)
alf::ConditionalExpressionCompletion_strategy = st.builds(
    alf::ConditionalExpressionCompletion,
)
alf::AndExpression_strategy = st.builds(
    alf::AndExpression,
)
alf::EqualityExpressionCompletion_strategy = st.builds(
    alf::EqualityExpressionCompletion,
    operator=
        safe_text
)
alf::RedefinitionClause_strategy = st.builds(
    alf::RedefinitionClause,
)
OperationDefinitionOrStub_strategy = st.builds(
    OperationDefinitionOrStub,
)
alf::OperationDeclaration_strategy = st.builds(
    alf::OperationDeclaration,
    isAbstract=
        st.booleans()
)
alf::UnlimitedNaturalLiteral_strategy = st.builds(
    alf::UnlimitedNaturalLiteral,
    star=
        st.booleans()
)
alf::MultiplicityRange_strategy = st.builds(
    alf::MultiplicityRange,
)
alf::Multiplicity_strategy = st.builds(
    alf::Multiplicity,
    isOrdered=
        st.booleans(),
    isSequence=
        st.booleans(),
    isNonUnique=
        st.booleans()
)
alf::TypeName_strategy = st.builds(
    alf::TypeName,
    any=
        st.booleans()
)
alf::TypePart_strategy = st.builds(
    alf::TypePart,
)
alf::FormalParameters_strategy = st.builds(
    alf::FormalParameters,
)
FeatureDefinitionOrStub_strategy = st.builds(
    FeatureDefinitionOrStub,
)
alf::AttributeDefinition_strategy = st.builds(
    alf::AttributeDefinition,
)
alf::PropertyDeclaration_strategy = st.builds(
    alf::PropertyDeclaration,
    isComposite=
        st.booleans()
)
alf::FormalParameter_strategy = st.builds(
    alf::FormalParameter,
    parameterDirection=
        safe_text,
    comment=
        safe_text
)
alf::FormalParameterList_strategy = st.builds(
    alf::FormalParameterList,
)
alf::AssociationDeclaration_strategy = st.builds(
    alf::AssociationDeclaration,
    isAbstract=
        st.booleans()
)
alf::PropertyDefinition_strategy = st.builds(
    alf::PropertyDefinition,
)
alf::ActivityDeclaration_strategy = st.builds(
    alf::ActivityDeclaration,
)
alf::SignalDeclaration_strategy = st.builds(
    alf::SignalDeclaration,
    isAbstract=
        st.booleans()
)
alf::EnumerationLiteralName_strategy = st.builds(
    alf::EnumerationLiteralName,
    comment=
        safe_text
)
alf::EnumerationBody_strategy = st.builds(
    alf::EnumerationBody,
)
alf::EnumerationDeclaration_strategy = st.builds(
    alf::EnumerationDeclaration,
)
alf::ActiveClassBody_strategy = st.builds(
    alf::ActiveClassBody,
)
alf::StructuredMember_strategy = st.builds(
    alf::StructuredMember,
    comment=
        safe_text,
    isPublic=
        st.booleans()
)
alf::StructuredBody_strategy = st.builds(
    alf::StructuredBody,
)
alf::DataTypeDeclaration_strategy = st.builds(
    alf::DataTypeDeclaration,
    isAbstract=
        st.booleans()
)
alf::ActiveClassMemberDefinition_strategy = st.builds(
    alf::ActiveClassMemberDefinition,
)
alf::Block_strategy = st.builds(
    alf::Block,
)
alf::BehaviorClause_strategy = st.builds(
    alf::BehaviorClause,
)
alf::ActiveClassMember_strategy = st.builds(
    alf::ActiveClassMember,
    comment=
        safe_text
)
alf::PackagedElementDefinition_strategy = st.builds(
    alf::PackagedElementDefinition,
)
alf::ActiveClassDeclaration_strategy = st.builds(
    alf::ActiveClassDeclaration,
    isAbstract=
        st.booleans()
)
alf::PackagedElement_strategy = st.builds(
    alf::PackagedElement,
    importVisibilityIndicator=
        safe_text,
    comment=
        safe_text
)
ActiveClassMemberDefinition_strategy = st.builds(
    ActiveClassMemberDefinition,
)
alf::ActiveFeatureDefinitionOrStub_strategy = st.builds(
    alf::ActiveFeatureDefinitionOrStub,
)
alf::ClassMemberDefinition_strategy = st.builds(
    alf::ClassMemberDefinition,
)
alf::ClassMember_strategy = st.builds(
    alf::ClassMember,
    comment=
        safe_text
)
ClassifierDefinitionOrStub_strategy = st.builds(
    ClassifierDefinitionOrStub,
)
alf::DataTypeDefinitionOrStub_strategy = st.builds(
    alf::DataTypeDefinitionOrStub,
)
alf::ActivityDefinitionOrStub_strategy = st.builds(
    alf::ActivityDefinitionOrStub,
)
alf::AssociationDefinitionOrStub_strategy = st.builds(
    alf::AssociationDefinitionOrStub,
)
alf::SignalDefinitionOrStub_strategy = st.builds(
    alf::SignalDefinitionOrStub,
)
alf::EnumerationDefinitionOrStub_strategy = st.builds(
    alf::EnumerationDefinitionOrStub,
)
alf::ActiveClassDefinitionOrStub_strategy = st.builds(
    alf::ActiveClassDefinitionOrStub,
)
alf::ClassDefinitionOrStub_strategy = st.builds(
    alf::ClassDefinitionOrStub,
)
alf::ClassBody_strategy = st.builds(
    alf::ClassBody,
)
ClassifierDefinition_strategy = st.builds(
    ClassifierDefinition,
)
alf::EnumerationDefinition_strategy = st.builds(
    alf::EnumerationDefinition,
)
alf::DataTypeDefinition_strategy = st.builds(
    alf::DataTypeDefinition,
)
alf::ActivityDefinition_strategy = st.builds(
    alf::ActivityDefinition,
)
alf::ActiveClassDefinition_strategy = st.builds(
    alf::ActiveClassDefinition,
)
alf::SignalDefinition_strategy = st.builds(
    alf::SignalDefinition,
)
alf::AssociationDefinition_strategy = st.builds(
    alf::AssociationDefinition,
)
alf::ClassDefinition_strategy = st.builds(
    alf::ClassDefinition,
)
alf::ClassDeclaration_strategy = st.builds(
    alf::ClassDeclaration,
    isAbstract=
        st.booleans()
)
alf::ClassifierTemplateParameter_strategy = st.builds(
    alf::ClassifierTemplateParameter,
    comment=
        safe_text
)
alf::SpecializationClause_strategy = st.builds(
    alf::SpecializationClause,
)
PackagedElementDefinition_strategy = st.builds(
    PackagedElementDefinition,
)
alf::PackageDefinitionOrStub_strategy = st.builds(
    alf::PackageDefinitionOrStub,
)
alf::TemplateParameters_strategy = st.builds(
    alf::TemplateParameters,
)
alf::PackageBody_strategy = st.builds(
    alf::PackageBody,
)
alf::ClassifierSignature_strategy = st.builds(
    alf::ClassifierSignature,
)
ClassMemberDefinition_strategy = st.builds(
    ClassMemberDefinition,
)
alf::ClassifierDefinitionOrStub_strategy = st.builds(
    alf::ClassifierDefinitionOrStub,
)
alf::FeatureDefinitionOrStub_strategy = st.builds(
    alf::FeatureDefinitionOrStub,
)
NamespaceDefinition_strategy = st.builds(
    NamespaceDefinition,
)
alf::ClassifierDefinition_strategy = st.builds(
    alf::ClassifierDefinition,
)
alf::PackageDefinition_strategy = st.builds(
    alf::PackageDefinition,
)
alf::PackageDeclaration_strategy = st.builds(
    alf::PackageDeclaration,
)
alf::VisibilityIndicator_strategy = st.builds(
    alf::VisibilityIndicator,
    PRIVATE=
        safe_text,
    PUBLIC=
        safe_text,
    PROTECTED=
        safe_text
)
ImportReferenceQualifiedNameCompletion_strategy = st.builds(
    ImportReferenceQualifiedNameCompletion,
)
alf::ColonQualifiedNameCompletionOfImportReference_strategy = st.builds(
    alf::ColonQualifiedNameCompletionOfImportReference,
    star=
        st.booleans()
)
alf::AliasDefinition_strategy = st.builds(
    alf::AliasDefinition,
)
alf::ImportReferenceQualifiedNameCompletion_strategy = st.builds(
    alf::ImportReferenceQualifiedNameCompletion,
)
alf::Name_strategy = st.builds(
    alf::Name,
    id=
        safe_text
)
alf::PRIMITIVE::LITERAL_strategy = st.builds(
    alf::PRIMITIVE::LITERAL,
    value=
        safe_text
)
alf::TaggedValue_strategy = st.builds(
    alf::TaggedValue,
)
TaggedValues_strategy = st.builds(
    TaggedValues,
)
alf::QualifiedNameList_strategy = st.builds(
    alf::QualifiedNameList,
)
alf::TaggedValueList_strategy = st.builds(
    alf::TaggedValueList,
)
alf::TaggedValues_strategy = st.builds(
    alf::TaggedValues,
)
alf::QualifiedName_strategy = st.builds(
    alf::QualifiedName,
)
alf::StereotypeAnnotation_strategy = st.builds(
    alf::StereotypeAnnotation,
)
NUMBER::LITERAL_strategy = st.builds(
    NUMBER::LITERAL,
)
alf::UNLIMITED::NATURAL_strategy = st.builds(
    alf::UNLIMITED::NATURAL,
)
alf::INTEGER::LITERAL_strategy = st.builds(
    alf::INTEGER::LITERAL,
)
PRIMITIVE::LITERAL_strategy = st.builds(
    PRIMITIVE::LITERAL,
)
alf::NUMBER::LITERAL_strategy = st.builds(
    alf::NUMBER::LITERAL,
)
alf::STRING::LITERAL_strategy = st.builds(
    alf::STRING::LITERAL,
)
alf::BOOLEAN::LITERAL_strategy = st.builds(
    alf::BOOLEAN::LITERAL,
)
alf::NamespaceDefinition_strategy = st.builds(
    alf::NamespaceDefinition,
)
alf::StereotypeAnnotations_strategy = st.builds(
    alf::StereotypeAnnotations,
)
alf::ImportDeclaration_strategy = st.builds(
    alf::ImportDeclaration,
    visibility=
        safe_text
)
alf::NamespaceDeclaration_strategy = st.builds(
    alf::NamespaceDeclaration,
)
alf::UnitDefinition_strategy = st.builds(
    alf::UnitDefinition,
    comment=
        safe_text
)
alf::ImportReference_strategy = st.builds(
    alf::ImportReference,
    star=
        st.booleans()
)
alf::ConditionalAndExpressionCompletion_strategy = st.builds(
    alf::ConditionalAndExpressionCompletion,
)
alf::ConditionalAndExpression_strategy = st.builds(
    alf::ConditionalAndExpression,
)
alf::InclusiveOrExpressionCompletion_strategy = st.builds(
    alf::InclusiveOrExpressionCompletion,
)
alf::InclusiveOrExpression_strategy = st.builds(
    alf::InclusiveOrExpression,
)
alf::ExclusiveOrExpressionCompletion_strategy = st.builds(
    alf::ExclusiveOrExpressionCompletion,
)
alf::ExclusiveOrExpression_strategy = st.builds(
    alf::ExclusiveOrExpression,
)
alf::AndExpressionCompletion_strategy = st.builds(
    alf::AndExpressionCompletion,
)
alf::ShiftExpressionCompletion_strategy = st.builds(
    alf::ShiftExpressionCompletion,
    operator=
        safe_text
)
alf::ShiftExpression_strategy = st.builds(
    alf::ShiftExpression,
)
alf::EqualityExpression_strategy = st.builds(
    alf::EqualityExpression,
)
alf::ClassificationExpressionCompletion_strategy = st.builds(
    alf::ClassificationExpressionCompletion,
    operator=
        safe_text
)
alf::ClassificationExpression_strategy = st.builds(
    alf::ClassificationExpression,
)
alf::RelationalExpressionCompletion_strategy = st.builds(
    alf::RelationalExpressionCompletion,
    relationalOperator=
        safe_text
)
alf::RelationalExpression_strategy = st.builds(
    alf::RelationalExpression,
)
alf::AdditiveExpressionCompletion_strategy = st.builds(
    alf::AdditiveExpressionCompletion,
    operator=
        safe_text
)
alf::AdditiveExpression_strategy = st.builds(
    alf::AdditiveExpression,
)
alf::MultiplicativeExpressionCompletion_strategy = st.builds(
    alf::MultiplicativeExpressionCompletion,
    operator=
        safe_text
)
alf::MultiplicativeExpression_strategy = st.builds(
    alf::MultiplicativeExpression,
)
alf::CastCompletion_strategy = st.builds(
    alf::CastCompletion,
)
NonNameUnaryExpression_strategy = st.builds(
    NonNameUnaryExpression,
)
alf::NonNamePostfixOrCastExpression_strategy = st.builds(
    alf::NonNamePostfixOrCastExpression,
    any=
        st.booleans()
)
CastCompletion_strategy = st.builds(
    CastCompletion,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
alf::NonPostfixNonCastUnaryExpression_strategy = st.builds(
    alf::NonPostfixNonCastUnaryExpression,
)
alf::PostfixOrCastExpression_strategy = st.builds(
    alf::PostfixOrCastExpression,
)
NonPostfixNonCastUnaryExpression_strategy = st.builds(
    NonPostfixNonCastUnaryExpression,
)
alf::NumericUnaryExpression_strategy = st.builds(
    alf::NumericUnaryExpression,
    operator=
        safe_text
)
alf::BooleanNegationExpression_strategy = st.builds(
    alf::BooleanNegationExpression,
)
alf::IsolationExpression_strategy = st.builds(
    alf::IsolationExpression,
)
alf::BitStringComplementExpression_strategy = st.builds(
    alf::BitStringComplementExpression,
)
alf::PrefixExpression_strategy = st.builds(
    alf::PrefixExpression,
    operator=
        safe_text
)
alf::PostfixOperation_strategy = st.builds(
    alf::PostfixOperation,
    operator=
        safe_text
)
alf::EObject_strategy = st.builds(
    alf::EObject,
)
alf::SequenceElement_strategy = st.builds(
    alf::SequenceElement,
)
alf::SequenceElementListCompletion_strategy = st.builds(
    alf::SequenceElementListCompletion,
)
alf::SequenceElements_strategy = st.builds(
    alf::SequenceElements,
)
alf::MultiplicityIndicator_strategy = st.builds(
    alf::MultiplicityIndicator,
)
alf::IndexedNamedExpression_strategy = st.builds(
    alf::IndexedNamedExpression,
)
alf::IndexedNamedExpressionListCompletion_strategy = st.builds(
    alf::IndexedNamedExpressionListCompletion,
)
alf::LinkOperationTuple_strategy = st.builds(
    alf::LinkOperationTuple,
)
BaseExpression_strategy = st.builds(
    BaseExpression,
)
alf::SuperInvocationExpression_strategy = st.builds(
    alf::SuperInvocationExpression,
)
alf::InstanceCreationOrSequenceConstructionExpression_strategy = st.builds(
    alf::InstanceCreationOrSequenceConstructionExpression,
)
alf::SequenceAnyExpression_strategy = st.builds(
    alf::SequenceAnyExpression,
)
alf::LiteralExpression_strategy = st.builds(
    alf::LiteralExpression,
)
alf::Index_strategy = st.builds(
    alf::Index,
)
alf::NamedExpression_strategy = st.builds(
    alf::NamedExpression,
)
alf::PositionalTupleExpressionListCompletion_strategy = st.builds(
    alf::PositionalTupleExpressionListCompletion,
)
alf::PositionalTupleExpressionList_strategy = st.builds(
    alf::PositionalTupleExpressionList,
)
alf::NamedTupleExpressionList_strategy = st.builds(
    alf::NamedTupleExpressionList,
)
alf::Tuple_strategy = st.builds(
    alf::Tuple,
)
alf::ThisExpression_strategy = st.builds(
    alf::ThisExpression,
)
alf::ExpressionCompletion_strategy = st.builds(
    alf::ExpressionCompletion,
)
alf::UnaryExpression_strategy = st.builds(
    alf::UnaryExpression,
)
InitializationExpression_strategy = st.builds(
    InitializationExpression,
)
alf::InstanceInitializationExpression_strategy = st.builds(
    alf::InstanceInitializationExpression,
)
alf::SequenceInitializationExpression_strategy = st.builds(
    alf::SequenceInitializationExpression,
    isNew=
        st.booleans()
)
alf::Expression_strategy = st.builds(
    alf::Expression,
)
alf::SequenceOperationOrReductionOrExpansion_strategy = st.builds(
    alf::SequenceOperationOrReductionOrExpansion,
    isOrdered=
        st.booleans(),
    id=
        safe_text,
    isReduce=
        st.booleans()
)
alf::FeatureInvocation_strategy = st.builds(
    alf::FeatureInvocation,
)
alf::Feature_strategy = st.builds(
    alf::Feature,
)
alf::Feature::Or::SequenceOperationOrReductionOrExpansion::Or::Index_strategy = st.builds(
    alf::Feature::Or::SequenceOperationOrReductionOrExpansion::Or::Index,
)
alf::BehaviorInvocation_strategy = st.builds(
    alf::BehaviorInvocation,
)
alf::SequenceConstructionExpressionCompletion_strategy = st.builds(
    alf::SequenceConstructionExpressionCompletion,
)
alf::ClassExtentExpressionCompletion_strategy = st.builds(
    alf::ClassExtentExpressionCompletion,
)
alf::LinkOperationCompletion_strategy = st.builds(
    alf::LinkOperationCompletion,
    linkOperation=
        safe_text
)
alf::PrimaryExpressionCompletion_strategy = st.builds(
    alf::PrimaryExpressionCompletion,
)
alf::ParenthesizedExpression_strategy = st.builds(
    alf::ParenthesizedExpression,
)
alf::BaseExpression_strategy = st.builds(
    alf::BaseExpression,
)
alf::NameOrPrimaryExpression_strategy = st.builds(
    alf::NameOrPrimaryExpression,
)
alf::PrimaryExpression_strategy = st.builds(
    alf::PrimaryExpression,
)
alf::PostfixExpressionCompletion_strategy = st.builds(
    alf::PostfixExpressionCompletion,
)
alf::PrimaryToExpressionCompletion_strategy = st.builds(
    alf::PrimaryToExpressionCompletion,
)
alf::NameToPrimaryExpression_strategy = st.builds(
    alf::NameToPrimaryExpression,
)
alf::NameToExpressionCompletion_strategy = st.builds(
    alf::NameToExpressionCompletion,
)
alf::NonNameUnaryExpression_strategy = st.builds(
    alf::NonNameUnaryExpression,
)
alf::NonNameExpression_strategy = st.builds(
    alf::NonNameExpression,
)
alf::SignalReceptionDeclaration_strategy = st.builds(
    alf::SignalReceptionDeclaration,
)
alf::TemplateParameterSubstitution_strategy = st.builds(
    alf::TemplateParameterSubstitution,
)
TemplateBinding_strategy = st.builds(
    TemplateBinding,
)
alf::NamedTemplateBinding_strategy = st.builds(
    alf::NamedTemplateBinding,
)
alf::PositionalTemplateBinding_strategy = st.builds(
    alf::PositionalTemplateBinding,
)
alf::ColonQualifiedNameCompletionWithoutBinding_strategy = st.builds(
    alf::ColonQualifiedNameCompletionWithoutBinding,
)
alf::QualifiedNameWithoutBinding_strategy = st.builds(
    alf::QualifiedNameWithoutBinding,
)
alf::TemplateBinding_strategy = st.builds(
    alf::TemplateBinding,
)
UnqualifiedName_strategy = st.builds(
    UnqualifiedName,
)
alf::NameBinding_strategy = st.builds(
    alf::NameBinding,
)
alf::ColonQualifiedNameCompletion_strategy = st.builds(
    alf::ColonQualifiedNameCompletion,
)
alf::UnqualifiedName_strategy = st.builds(
    alf::UnqualifiedName,
)
alf::InitializationExpression_strategy = st.builds(
    alf::InitializationExpression,
)
ActiveFeatureDefinitionOrStub_strategy = st.builds(
    ActiveFeatureDefinitionOrStub,
)
alf::SignalReceptionDefinitionOrStub_strategy = st.builds(
    alf::SignalReceptionDefinitionOrStub,
)
alf::ReceptionDefinition_strategy = st.builds(
    alf::ReceptionDefinition,
)
alf::AttributeInitializer_strategy = st.builds(
    alf::AttributeInitializer,
)
alf::OperationDefinitionOrStub_strategy = st.builds(
    alf::OperationDefinitionOrStub,
)

@given(instance=alf::AcceptClause_strategy)
@settings(max_examples=50)
def test_alf::acceptclause_instantiation(instance):
    assert isinstance(instance, alf::AcceptClause)

@given(instance=alf::ReclassifyAllClause_strategy)
@settings(max_examples=50)
def test_alf::reclassifyallclause_instantiation(instance):
    assert isinstance(instance, alf::ReclassifyAllClause)

@given(instance=alf::ClassificationToClause_strategy)
@settings(max_examples=50)
def test_alf::classificationtoclause_instantiation(instance):
    assert isinstance(instance, alf::ClassificationToClause)

@given(instance=alf::ClassificationFromClause_strategy)
@settings(max_examples=50)
def test_alf::classificationfromclause_instantiation(instance):
    assert isinstance(instance, alf::ClassificationFromClause)

@given(instance=alf::ClassificationClause_strategy)
@settings(max_examples=50)
def test_alf::classificationclause_instantiation(instance):
    assert isinstance(instance, alf::ClassificationClause)

@given(instance=alf::AcceptBlock_strategy)
@settings(max_examples=50)
def test_alf::acceptblock_instantiation(instance):
    assert isinstance(instance, alf::AcceptBlock)

@given(instance=alf::CompoundAcceptStatementCompletion_strategy)
@settings(max_examples=50)
def test_alf::compoundacceptstatementcompletion_instantiation(instance):
    assert isinstance(instance, alf::CompoundAcceptStatementCompletion)

@given(instance=alf::SimpleAcceptStatementCompletion_strategy)
@settings(max_examples=50)
def test_alf::simpleacceptstatementcompletion_instantiation(instance):
    assert isinstance(instance, alf::SimpleAcceptStatementCompletion)

@given(instance=alf::NonEmptyStatementSequence_strategy)
@settings(max_examples=50)
def test_alf::nonemptystatementsequence_instantiation(instance):
    assert isinstance(instance, alf::NonEmptyStatementSequence)

@given(instance=alf::SwitchCase_strategy)
@settings(max_examples=50)
def test_alf::switchcase_instantiation(instance):
    assert isinstance(instance, alf::SwitchCase)

@given(instance=alf::SwitchDefaultClause_strategy)
@settings(max_examples=50)
def test_alf::switchdefaultclause_instantiation(instance):
    assert isinstance(instance, alf::SwitchDefaultClause)

@given(instance=alf::SwitchClause_strategy)
@settings(max_examples=50)
def test_alf::switchclause_instantiation(instance):
    assert isinstance(instance, alf::SwitchClause)

@given(instance=alf::LoopVariableDefinition_strategy)
@settings(max_examples=50)
def test_alf::loopvariabledefinition_instantiation(instance):
    assert isinstance(instance, alf::LoopVariableDefinition)

@given(instance=alf::ForControl_strategy)
@settings(max_examples=50)
def test_alf::forcontrol_instantiation(instance):
    assert isinstance(instance, alf::ForControl)

@given(instance=alf::LocalNameDeclarationStatementCompletion_strategy)
@settings(max_examples=50)
def test_alf::localnamedeclarationstatementcompletion_instantiation(instance):
    assert isinstance(instance, alf::LocalNameDeclarationStatementCompletion)

@given(instance=alf::NonFinalClause_strategy)
@settings(max_examples=50)
def test_alf::nonfinalclause_instantiation(instance):
    assert isinstance(instance, alf::NonFinalClause)

@given(instance=alf::ConcurrentClauses_strategy)
@settings(max_examples=50)
def test_alf::concurrentclauses_instantiation(instance):
    assert isinstance(instance, alf::ConcurrentClauses)

@given(instance=alf::FinalClause_strategy)
@settings(max_examples=50)
def test_alf::finalclause_instantiation(instance):
    assert isinstance(instance, alf::FinalClause)

@given(instance=alf::SequentialClauses_strategy)
@settings(max_examples=50)
def test_alf::sequentialclauses_instantiation(instance):
    assert isinstance(instance, alf::SequentialClauses)

@given(instance=alf::NameList_strategy)
@settings(max_examples=50)
def test_alf::namelist_instantiation(instance):
    assert isinstance(instance, alf::NameList)

@given(instance=alf::Annotation_strategy)
@settings(max_examples=50)
def test_alf::annotation_instantiation(instance):
    assert isinstance(instance, alf::Annotation)

@given(instance=alf::Annotation_strategy)
def test_alf::annotation_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=alf::Annotation_strategy)
def test_alf::annotation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=alf::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_alf::conditionalexpression_instantiation(instance):
    assert isinstance(instance, alf::ConditionalExpression)

@given(instance=alf::ConditionalOrExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::conditionalorexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::ConditionalOrExpressionCompletion)

@given(instance=alf::ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_alf::conditionalorexpression_instantiation(instance):
    assert isinstance(instance, alf::ConditionalOrExpression)

@given(instance=alf::Annotations_strategy)
@settings(max_examples=50)
def test_alf::annotations_instantiation(instance):
    assert isinstance(instance, alf::Annotations)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=alf::ReturnStatement_strategy)
@settings(max_examples=50)
def test_alf::returnstatement_instantiation(instance):
    assert isinstance(instance, alf::ReturnStatement)

@given(instance=alf::SwitchStatement_strategy)
@settings(max_examples=50)
def test_alf::switchstatement_instantiation(instance):
    assert isinstance(instance, alf::SwitchStatement)

@given(instance=alf::ClassifyStatement_strategy)
@settings(max_examples=50)
def test_alf::classifystatement_instantiation(instance):
    assert isinstance(instance, alf::ClassifyStatement)

@given(instance=alf::BreakStatement_strategy)
@settings(max_examples=50)
def test_alf::breakstatement_instantiation(instance):
    assert isinstance(instance, alf::BreakStatement)

@given(instance=alf::DoStatement_strategy)
@settings(max_examples=50)
def test_alf::dostatement_instantiation(instance):
    assert isinstance(instance, alf::DoStatement)

@given(instance=alf::InLineStatement_strategy)
@settings(max_examples=50)
def test_alf::inlinestatement_instantiation(instance):
    assert isinstance(instance, alf::InLineStatement)

@given(instance=alf::InLineStatement_strategy)
def test_alf::inlinestatement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=alf::InLineStatement_strategy)
def test_alf::inlinestatement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=alf::EmptyStatement_strategy)
@settings(max_examples=50)
def test_alf::emptystatement_instantiation(instance):
    assert isinstance(instance, alf::EmptyStatement)

@given(instance=alf::WhileStatement_strategy)
@settings(max_examples=50)
def test_alf::whilestatement_instantiation(instance):
    assert isinstance(instance, alf::WhileStatement)

@given(instance=alf::ForStatement_strategy)
@settings(max_examples=50)
def test_alf::forstatement_instantiation(instance):
    assert isinstance(instance, alf::ForStatement)

@given(instance=alf::BlockStatement_strategy)
@settings(max_examples=50)
def test_alf::blockstatement_instantiation(instance):
    assert isinstance(instance, alf::BlockStatement)

@given(instance=alf::IfStatement_strategy)
@settings(max_examples=50)
def test_alf::ifstatement_instantiation(instance):
    assert isinstance(instance, alf::IfStatement)

@given(instance=alf::AcceptStatement_strategy)
@settings(max_examples=50)
def test_alf::acceptstatement_instantiation(instance):
    assert isinstance(instance, alf::AcceptStatement)

@given(instance=alf::LocalNameDeclarationStatement_strategy)
@settings(max_examples=50)
def test_alf::localnamedeclarationstatement_instantiation(instance):
    assert isinstance(instance, alf::LocalNameDeclarationStatement)

@given(instance=alf::LocalNameDeclarationOrExpressionStatement_strategy)
@settings(max_examples=50)
def test_alf::localnamedeclarationorexpressionstatement_instantiation(instance):
    assert isinstance(instance, alf::LocalNameDeclarationOrExpressionStatement)

@given(instance=alf::AnnotatedStatement_strategy)
@settings(max_examples=50)
def test_alf::annotatedstatement_instantiation(instance):
    assert isinstance(instance, alf::AnnotatedStatement)

@given(instance=alf::Statement_strategy)
@settings(max_examples=50)
def test_alf::statement_instantiation(instance):
    assert isinstance(instance, alf::Statement)

@given(instance=alf::DocumentedStatement_strategy)
@settings(max_examples=50)
def test_alf::documentedstatement_instantiation(instance):
    assert isinstance(instance, alf::DocumentedStatement)

@given(instance=alf::DocumentedStatement_strategy)
def test_alf::documentedstatement_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=alf::DocumentedStatement_strategy)
def test_alf::documentedstatement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=alf::StatementSequence_strategy)
@settings(max_examples=50)
def test_alf::statementsequence_instantiation(instance):
    assert isinstance(instance, alf::StatementSequence)

@given(instance=ExpressionCompletion_strategy)
@settings(max_examples=50)
def test_expressioncompletion_instantiation(instance):
    assert isinstance(instance, ExpressionCompletion)

@given(instance=alf::AssignmentExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::assignmentexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::AssignmentExpressionCompletion)

@given(instance=alf::AssignmentExpressionCompletion_strategy)
def test_alf::assignmentexpressioncompletion_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=alf::AssignmentExpressionCompletion_strategy)
def test_alf::assignmentexpressioncompletion_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf::ConditionalExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::conditionalexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::ConditionalExpressionCompletion)

@given(instance=alf::AndExpression_strategy)
@settings(max_examples=50)
def test_alf::andexpression_instantiation(instance):
    assert isinstance(instance, alf::AndExpression)

@given(instance=alf::EqualityExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::equalityexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::EqualityExpressionCompletion)

@given(instance=alf::EqualityExpressionCompletion_strategy)
def test_alf::equalityexpressioncompletion_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=alf::EqualityExpressionCompletion_strategy)
def test_alf::equalityexpressioncompletion_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf::RedefinitionClause_strategy)
@settings(max_examples=50)
def test_alf::redefinitionclause_instantiation(instance):
    assert isinstance(instance, alf::RedefinitionClause)

@given(instance=OperationDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_operationdefinitionorstub_instantiation(instance):
    assert isinstance(instance, OperationDefinitionOrStub)

@given(instance=alf::OperationDeclaration_strategy)
@settings(max_examples=50)
def test_alf::operationdeclaration_instantiation(instance):
    assert isinstance(instance, alf::OperationDeclaration)

@given(instance=alf::OperationDeclaration_strategy)
def test_alf::operationdeclaration_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=alf::OperationDeclaration_strategy)
def test_alf::operationdeclaration_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=alf::UnlimitedNaturalLiteral_strategy)
@settings(max_examples=50)
def test_alf::unlimitednaturalliteral_instantiation(instance):
    assert isinstance(instance, alf::UnlimitedNaturalLiteral)

@given(instance=alf::UnlimitedNaturalLiteral_strategy)
def test_alf::unlimitednaturalliteral_star_type(instance):
    assert isinstance(instance.star, bool)


@given(instance=alf::UnlimitedNaturalLiteral_strategy)
def test_alf::unlimitednaturalliteral_star_setter(instance):
    original = instance.star
    instance.star = original
    assert instance.star == original

@given(instance=alf::MultiplicityRange_strategy)
@settings(max_examples=50)
def test_alf::multiplicityrange_instantiation(instance):
    assert isinstance(instance, alf::MultiplicityRange)

@given(instance=alf::Multiplicity_strategy)
@settings(max_examples=50)
def test_alf::multiplicity_instantiation(instance):
    assert isinstance(instance, alf::Multiplicity)

@given(instance=alf::Multiplicity_strategy)
def test_alf::multiplicity_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, bool)


@given(instance=alf::Multiplicity_strategy)
def test_alf::multiplicity_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=alf::Multiplicity_strategy)
def test_alf::multiplicity_isSequence_type(instance):
    assert isinstance(instance.isSequence, bool)


@given(instance=alf::Multiplicity_strategy)
def test_alf::multiplicity_isSequence_setter(instance):
    original = instance.isSequence
    instance.isSequence = original
    assert instance.isSequence == original

@given(instance=alf::Multiplicity_strategy)
def test_alf::multiplicity_isNonUnique_type(instance):
    assert isinstance(instance.isNonUnique, bool)


@given(instance=alf::Multiplicity_strategy)
def test_alf::multiplicity_isNonUnique_setter(instance):
    original = instance.isNonUnique
    instance.isNonUnique = original
    assert instance.isNonUnique == original

@given(instance=alf::TypeName_strategy)
@settings(max_examples=50)
def test_alf::typename_instantiation(instance):
    assert isinstance(instance, alf::TypeName)

@given(instance=alf::TypeName_strategy)
def test_alf::typename_any_type(instance):
    assert isinstance(instance.any, bool)


@given(instance=alf::TypeName_strategy)
def test_alf::typename_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=alf::TypePart_strategy)
@settings(max_examples=50)
def test_alf::typepart_instantiation(instance):
    assert isinstance(instance, alf::TypePart)

@given(instance=alf::FormalParameters_strategy)
@settings(max_examples=50)
def test_alf::formalparameters_instantiation(instance):
    assert isinstance(instance, alf::FormalParameters)

@given(instance=FeatureDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_featuredefinitionorstub_instantiation(instance):
    assert isinstance(instance, FeatureDefinitionOrStub)

@given(instance=alf::AttributeDefinition_strategy)
@settings(max_examples=50)
def test_alf::attributedefinition_instantiation(instance):
    assert isinstance(instance, alf::AttributeDefinition)

@given(instance=alf::PropertyDeclaration_strategy)
@settings(max_examples=50)
def test_alf::propertydeclaration_instantiation(instance):
    assert isinstance(instance, alf::PropertyDeclaration)

@given(instance=alf::PropertyDeclaration_strategy)
def test_alf::propertydeclaration_isComposite_type(instance):
    assert isinstance(instance.isComposite, bool)


@given(instance=alf::PropertyDeclaration_strategy)
def test_alf::propertydeclaration_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=alf::FormalParameter_strategy)
@settings(max_examples=50)
def test_alf::formalparameter_instantiation(instance):
    assert isinstance(instance, alf::FormalParameter)

@given(instance=alf::FormalParameter_strategy)
def test_alf::formalparameter_parameterDirection_type(instance):
    assert isinstance(instance.parameterDirection, str)


@given(instance=alf::FormalParameter_strategy)
def test_alf::formalparameter_parameterDirection_setter(instance):
    original = instance.parameterDirection
    instance.parameterDirection = original
    assert instance.parameterDirection == original

@given(instance=alf::FormalParameter_strategy)
def test_alf::formalparameter_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=alf::FormalParameter_strategy)
def test_alf::formalparameter_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=alf::FormalParameterList_strategy)
@settings(max_examples=50)
def test_alf::formalparameterlist_instantiation(instance):
    assert isinstance(instance, alf::FormalParameterList)

@given(instance=alf::AssociationDeclaration_strategy)
@settings(max_examples=50)
def test_alf::associationdeclaration_instantiation(instance):
    assert isinstance(instance, alf::AssociationDeclaration)

@given(instance=alf::AssociationDeclaration_strategy)
def test_alf::associationdeclaration_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=alf::AssociationDeclaration_strategy)
def test_alf::associationdeclaration_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=alf::PropertyDefinition_strategy)
@settings(max_examples=50)
def test_alf::propertydefinition_instantiation(instance):
    assert isinstance(instance, alf::PropertyDefinition)

@given(instance=alf::ActivityDeclaration_strategy)
@settings(max_examples=50)
def test_alf::activitydeclaration_instantiation(instance):
    assert isinstance(instance, alf::ActivityDeclaration)

@given(instance=alf::SignalDeclaration_strategy)
@settings(max_examples=50)
def test_alf::signaldeclaration_instantiation(instance):
    assert isinstance(instance, alf::SignalDeclaration)

@given(instance=alf::SignalDeclaration_strategy)
def test_alf::signaldeclaration_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=alf::SignalDeclaration_strategy)
def test_alf::signaldeclaration_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=alf::EnumerationLiteralName_strategy)
@settings(max_examples=50)
def test_alf::enumerationliteralname_instantiation(instance):
    assert isinstance(instance, alf::EnumerationLiteralName)

@given(instance=alf::EnumerationLiteralName_strategy)
def test_alf::enumerationliteralname_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=alf::EnumerationLiteralName_strategy)
def test_alf::enumerationliteralname_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=alf::EnumerationBody_strategy)
@settings(max_examples=50)
def test_alf::enumerationbody_instantiation(instance):
    assert isinstance(instance, alf::EnumerationBody)

@given(instance=alf::EnumerationDeclaration_strategy)
@settings(max_examples=50)
def test_alf::enumerationdeclaration_instantiation(instance):
    assert isinstance(instance, alf::EnumerationDeclaration)

@given(instance=alf::ActiveClassBody_strategy)
@settings(max_examples=50)
def test_alf::activeclassbody_instantiation(instance):
    assert isinstance(instance, alf::ActiveClassBody)

@given(instance=alf::StructuredMember_strategy)
@settings(max_examples=50)
def test_alf::structuredmember_instantiation(instance):
    assert isinstance(instance, alf::StructuredMember)

@given(instance=alf::StructuredMember_strategy)
def test_alf::structuredmember_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=alf::StructuredMember_strategy)
def test_alf::structuredmember_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=alf::StructuredMember_strategy)
def test_alf::structuredmember_isPublic_type(instance):
    assert isinstance(instance.isPublic, bool)


@given(instance=alf::StructuredMember_strategy)
def test_alf::structuredmember_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original

@given(instance=alf::StructuredBody_strategy)
@settings(max_examples=50)
def test_alf::structuredbody_instantiation(instance):
    assert isinstance(instance, alf::StructuredBody)

@given(instance=alf::DataTypeDeclaration_strategy)
@settings(max_examples=50)
def test_alf::datatypedeclaration_instantiation(instance):
    assert isinstance(instance, alf::DataTypeDeclaration)

@given(instance=alf::DataTypeDeclaration_strategy)
def test_alf::datatypedeclaration_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=alf::DataTypeDeclaration_strategy)
def test_alf::datatypedeclaration_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=alf::ActiveClassMemberDefinition_strategy)
@settings(max_examples=50)
def test_alf::activeclassmemberdefinition_instantiation(instance):
    assert isinstance(instance, alf::ActiveClassMemberDefinition)

@given(instance=alf::Block_strategy)
@settings(max_examples=50)
def test_alf::block_instantiation(instance):
    assert isinstance(instance, alf::Block)

@given(instance=alf::BehaviorClause_strategy)
@settings(max_examples=50)
def test_alf::behaviorclause_instantiation(instance):
    assert isinstance(instance, alf::BehaviorClause)

@given(instance=alf::ActiveClassMember_strategy)
@settings(max_examples=50)
def test_alf::activeclassmember_instantiation(instance):
    assert isinstance(instance, alf::ActiveClassMember)

@given(instance=alf::ActiveClassMember_strategy)
def test_alf::activeclassmember_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=alf::ActiveClassMember_strategy)
def test_alf::activeclassmember_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=alf::PackagedElementDefinition_strategy)
@settings(max_examples=50)
def test_alf::packagedelementdefinition_instantiation(instance):
    assert isinstance(instance, alf::PackagedElementDefinition)

@given(instance=alf::ActiveClassDeclaration_strategy)
@settings(max_examples=50)
def test_alf::activeclassdeclaration_instantiation(instance):
    assert isinstance(instance, alf::ActiveClassDeclaration)

@given(instance=alf::ActiveClassDeclaration_strategy)
def test_alf::activeclassdeclaration_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=alf::ActiveClassDeclaration_strategy)
def test_alf::activeclassdeclaration_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=alf::PackagedElement_strategy)
@settings(max_examples=50)
def test_alf::packagedelement_instantiation(instance):
    assert isinstance(instance, alf::PackagedElement)

@given(instance=alf::PackagedElement_strategy)
def test_alf::packagedelement_importVisibilityIndicator_type(instance):
    assert isinstance(instance.importVisibilityIndicator, str)


@given(instance=alf::PackagedElement_strategy)
def test_alf::packagedelement_importVisibilityIndicator_setter(instance):
    original = instance.importVisibilityIndicator
    instance.importVisibilityIndicator = original
    assert instance.importVisibilityIndicator == original

@given(instance=alf::PackagedElement_strategy)
def test_alf::packagedelement_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=alf::PackagedElement_strategy)
def test_alf::packagedelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=ActiveClassMemberDefinition_strategy)
@settings(max_examples=50)
def test_activeclassmemberdefinition_instantiation(instance):
    assert isinstance(instance, ActiveClassMemberDefinition)

@given(instance=alf::ActiveFeatureDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf::activefeaturedefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf::ActiveFeatureDefinitionOrStub)

@given(instance=alf::ClassMemberDefinition_strategy)
@settings(max_examples=50)
def test_alf::classmemberdefinition_instantiation(instance):
    assert isinstance(instance, alf::ClassMemberDefinition)

@given(instance=alf::ClassMember_strategy)
@settings(max_examples=50)
def test_alf::classmember_instantiation(instance):
    assert isinstance(instance, alf::ClassMember)

@given(instance=alf::ClassMember_strategy)
def test_alf::classmember_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=alf::ClassMember_strategy)
def test_alf::classmember_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=ClassifierDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_classifierdefinitionorstub_instantiation(instance):
    assert isinstance(instance, ClassifierDefinitionOrStub)

@given(instance=alf::DataTypeDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf::datatypedefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf::DataTypeDefinitionOrStub)

@given(instance=alf::ActivityDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf::activitydefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf::ActivityDefinitionOrStub)

@given(instance=alf::AssociationDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf::associationdefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf::AssociationDefinitionOrStub)

@given(instance=alf::SignalDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf::signaldefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf::SignalDefinitionOrStub)

@given(instance=alf::EnumerationDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf::enumerationdefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf::EnumerationDefinitionOrStub)

@given(instance=alf::ActiveClassDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf::activeclassdefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf::ActiveClassDefinitionOrStub)

@given(instance=alf::ClassDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf::classdefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf::ClassDefinitionOrStub)

@given(instance=alf::ClassBody_strategy)
@settings(max_examples=50)
def test_alf::classbody_instantiation(instance):
    assert isinstance(instance, alf::ClassBody)

@given(instance=ClassifierDefinition_strategy)
@settings(max_examples=50)
def test_classifierdefinition_instantiation(instance):
    assert isinstance(instance, ClassifierDefinition)

@given(instance=alf::EnumerationDefinition_strategy)
@settings(max_examples=50)
def test_alf::enumerationdefinition_instantiation(instance):
    assert isinstance(instance, alf::EnumerationDefinition)

@given(instance=alf::DataTypeDefinition_strategy)
@settings(max_examples=50)
def test_alf::datatypedefinition_instantiation(instance):
    assert isinstance(instance, alf::DataTypeDefinition)

@given(instance=alf::ActivityDefinition_strategy)
@settings(max_examples=50)
def test_alf::activitydefinition_instantiation(instance):
    assert isinstance(instance, alf::ActivityDefinition)

@given(instance=alf::ActiveClassDefinition_strategy)
@settings(max_examples=50)
def test_alf::activeclassdefinition_instantiation(instance):
    assert isinstance(instance, alf::ActiveClassDefinition)

@given(instance=alf::SignalDefinition_strategy)
@settings(max_examples=50)
def test_alf::signaldefinition_instantiation(instance):
    assert isinstance(instance, alf::SignalDefinition)

@given(instance=alf::AssociationDefinition_strategy)
@settings(max_examples=50)
def test_alf::associationdefinition_instantiation(instance):
    assert isinstance(instance, alf::AssociationDefinition)

@given(instance=alf::ClassDefinition_strategy)
@settings(max_examples=50)
def test_alf::classdefinition_instantiation(instance):
    assert isinstance(instance, alf::ClassDefinition)

@given(instance=alf::ClassDeclaration_strategy)
@settings(max_examples=50)
def test_alf::classdeclaration_instantiation(instance):
    assert isinstance(instance, alf::ClassDeclaration)

@given(instance=alf::ClassDeclaration_strategy)
def test_alf::classdeclaration_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=alf::ClassDeclaration_strategy)
def test_alf::classdeclaration_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=alf::ClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_alf::classifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, alf::ClassifierTemplateParameter)

@given(instance=alf::ClassifierTemplateParameter_strategy)
def test_alf::classifiertemplateparameter_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=alf::ClassifierTemplateParameter_strategy)
def test_alf::classifiertemplateparameter_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=alf::SpecializationClause_strategy)
@settings(max_examples=50)
def test_alf::specializationclause_instantiation(instance):
    assert isinstance(instance, alf::SpecializationClause)

@given(instance=PackagedElementDefinition_strategy)
@settings(max_examples=50)
def test_packagedelementdefinition_instantiation(instance):
    assert isinstance(instance, PackagedElementDefinition)

@given(instance=alf::PackageDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf::packagedefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf::PackageDefinitionOrStub)

@given(instance=alf::TemplateParameters_strategy)
@settings(max_examples=50)
def test_alf::templateparameters_instantiation(instance):
    assert isinstance(instance, alf::TemplateParameters)

@given(instance=alf::PackageBody_strategy)
@settings(max_examples=50)
def test_alf::packagebody_instantiation(instance):
    assert isinstance(instance, alf::PackageBody)

@given(instance=alf::ClassifierSignature_strategy)
@settings(max_examples=50)
def test_alf::classifiersignature_instantiation(instance):
    assert isinstance(instance, alf::ClassifierSignature)

@given(instance=ClassMemberDefinition_strategy)
@settings(max_examples=50)
def test_classmemberdefinition_instantiation(instance):
    assert isinstance(instance, ClassMemberDefinition)

@given(instance=alf::ClassifierDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf::classifierdefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf::ClassifierDefinitionOrStub)

@given(instance=alf::FeatureDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf::featuredefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf::FeatureDefinitionOrStub)

@given(instance=NamespaceDefinition_strategy)
@settings(max_examples=50)
def test_namespacedefinition_instantiation(instance):
    assert isinstance(instance, NamespaceDefinition)

@given(instance=alf::ClassifierDefinition_strategy)
@settings(max_examples=50)
def test_alf::classifierdefinition_instantiation(instance):
    assert isinstance(instance, alf::ClassifierDefinition)

@given(instance=alf::PackageDefinition_strategy)
@settings(max_examples=50)
def test_alf::packagedefinition_instantiation(instance):
    assert isinstance(instance, alf::PackageDefinition)

@given(instance=alf::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_alf::packagedeclaration_instantiation(instance):
    assert isinstance(instance, alf::PackageDeclaration)

@given(instance=alf::VisibilityIndicator_strategy)
@settings(max_examples=50)
def test_alf::visibilityindicator_instantiation(instance):
    assert isinstance(instance, alf::VisibilityIndicator)

@given(instance=alf::VisibilityIndicator_strategy)
def test_alf::visibilityindicator_PRIVATE_type(instance):
    assert isinstance(instance.PRIVATE, str)


@given(instance=alf::VisibilityIndicator_strategy)
def test_alf::visibilityindicator_PRIVATE_setter(instance):
    original = instance.PRIVATE
    instance.PRIVATE = original
    assert instance.PRIVATE == original

@given(instance=alf::VisibilityIndicator_strategy)
def test_alf::visibilityindicator_PUBLIC_type(instance):
    assert isinstance(instance.PUBLIC, str)


@given(instance=alf::VisibilityIndicator_strategy)
def test_alf::visibilityindicator_PUBLIC_setter(instance):
    original = instance.PUBLIC
    instance.PUBLIC = original
    assert instance.PUBLIC == original

@given(instance=alf::VisibilityIndicator_strategy)
def test_alf::visibilityindicator_PROTECTED_type(instance):
    assert isinstance(instance.PROTECTED, str)


@given(instance=alf::VisibilityIndicator_strategy)
def test_alf::visibilityindicator_PROTECTED_setter(instance):
    original = instance.PROTECTED
    instance.PROTECTED = original
    assert instance.PROTECTED == original

@given(instance=ImportReferenceQualifiedNameCompletion_strategy)
@settings(max_examples=50)
def test_importreferencequalifiednamecompletion_instantiation(instance):
    assert isinstance(instance, ImportReferenceQualifiedNameCompletion)

@given(instance=alf::ColonQualifiedNameCompletionOfImportReference_strategy)
@settings(max_examples=50)
def test_alf::colonqualifiednamecompletionofimportreference_instantiation(instance):
    assert isinstance(instance, alf::ColonQualifiedNameCompletionOfImportReference)

@given(instance=alf::ColonQualifiedNameCompletionOfImportReference_strategy)
def test_alf::colonqualifiednamecompletionofimportreference_star_type(instance):
    assert isinstance(instance.star, bool)


@given(instance=alf::ColonQualifiedNameCompletionOfImportReference_strategy)
def test_alf::colonqualifiednamecompletionofimportreference_star_setter(instance):
    original = instance.star
    instance.star = original
    assert instance.star == original

@given(instance=alf::AliasDefinition_strategy)
@settings(max_examples=50)
def test_alf::aliasdefinition_instantiation(instance):
    assert isinstance(instance, alf::AliasDefinition)

@given(instance=alf::ImportReferenceQualifiedNameCompletion_strategy)
@settings(max_examples=50)
def test_alf::importreferencequalifiednamecompletion_instantiation(instance):
    assert isinstance(instance, alf::ImportReferenceQualifiedNameCompletion)

@given(instance=alf::Name_strategy)
@settings(max_examples=50)
def test_alf::name_instantiation(instance):
    assert isinstance(instance, alf::Name)

@given(instance=alf::Name_strategy)
def test_alf::name_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=alf::Name_strategy)
def test_alf::name_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=alf::PRIMITIVE::LITERAL_strategy)
@settings(max_examples=50)
def test_alf::primitive::literal_instantiation(instance):
    assert isinstance(instance, alf::PRIMITIVE::LITERAL)

@given(instance=alf::PRIMITIVE::LITERAL_strategy)
def test_alf::primitive::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=alf::PRIMITIVE::LITERAL_strategy)
def test_alf::primitive::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=alf::TaggedValue_strategy)
@settings(max_examples=50)
def test_alf::taggedvalue_instantiation(instance):
    assert isinstance(instance, alf::TaggedValue)

@given(instance=TaggedValues_strategy)
@settings(max_examples=50)
def test_taggedvalues_instantiation(instance):
    assert isinstance(instance, TaggedValues)

@given(instance=alf::QualifiedNameList_strategy)
@settings(max_examples=50)
def test_alf::qualifiednamelist_instantiation(instance):
    assert isinstance(instance, alf::QualifiedNameList)

@given(instance=alf::TaggedValueList_strategy)
@settings(max_examples=50)
def test_alf::taggedvaluelist_instantiation(instance):
    assert isinstance(instance, alf::TaggedValueList)

@given(instance=alf::TaggedValues_strategy)
@settings(max_examples=50)
def test_alf::taggedvalues_instantiation(instance):
    assert isinstance(instance, alf::TaggedValues)

@given(instance=alf::QualifiedName_strategy)
@settings(max_examples=50)
def test_alf::qualifiedname_instantiation(instance):
    assert isinstance(instance, alf::QualifiedName)

@given(instance=alf::StereotypeAnnotation_strategy)
@settings(max_examples=50)
def test_alf::stereotypeannotation_instantiation(instance):
    assert isinstance(instance, alf::StereotypeAnnotation)

@given(instance=NUMBER::LITERAL_strategy)
@settings(max_examples=50)
def test_number::literal_instantiation(instance):
    assert isinstance(instance, NUMBER::LITERAL)

@given(instance=alf::UNLIMITED::NATURAL_strategy)
@settings(max_examples=50)
def test_alf::unlimited::natural_instantiation(instance):
    assert isinstance(instance, alf::UNLIMITED::NATURAL)

@given(instance=alf::INTEGER::LITERAL_strategy)
@settings(max_examples=50)
def test_alf::integer::literal_instantiation(instance):
    assert isinstance(instance, alf::INTEGER::LITERAL)

@given(instance=PRIMITIVE::LITERAL_strategy)
@settings(max_examples=50)
def test_primitive::literal_instantiation(instance):
    assert isinstance(instance, PRIMITIVE::LITERAL)

@given(instance=alf::NUMBER::LITERAL_strategy)
@settings(max_examples=50)
def test_alf::number::literal_instantiation(instance):
    assert isinstance(instance, alf::NUMBER::LITERAL)

@given(instance=alf::STRING::LITERAL_strategy)
@settings(max_examples=50)
def test_alf::string::literal_instantiation(instance):
    assert isinstance(instance, alf::STRING::LITERAL)

@given(instance=alf::BOOLEAN::LITERAL_strategy)
@settings(max_examples=50)
def test_alf::boolean::literal_instantiation(instance):
    assert isinstance(instance, alf::BOOLEAN::LITERAL)

@given(instance=alf::NamespaceDefinition_strategy)
@settings(max_examples=50)
def test_alf::namespacedefinition_instantiation(instance):
    assert isinstance(instance, alf::NamespaceDefinition)

@given(instance=alf::StereotypeAnnotations_strategy)
@settings(max_examples=50)
def test_alf::stereotypeannotations_instantiation(instance):
    assert isinstance(instance, alf::StereotypeAnnotations)

@given(instance=alf::ImportDeclaration_strategy)
@settings(max_examples=50)
def test_alf::importdeclaration_instantiation(instance):
    assert isinstance(instance, alf::ImportDeclaration)

@given(instance=alf::ImportDeclaration_strategy)
def test_alf::importdeclaration_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=alf::ImportDeclaration_strategy)
def test_alf::importdeclaration_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=alf::NamespaceDeclaration_strategy)
@settings(max_examples=50)
def test_alf::namespacedeclaration_instantiation(instance):
    assert isinstance(instance, alf::NamespaceDeclaration)

@given(instance=alf::UnitDefinition_strategy)
@settings(max_examples=50)
def test_alf::unitdefinition_instantiation(instance):
    assert isinstance(instance, alf::UnitDefinition)

@given(instance=alf::UnitDefinition_strategy)
def test_alf::unitdefinition_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=alf::UnitDefinition_strategy)
def test_alf::unitdefinition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=alf::ImportReference_strategy)
@settings(max_examples=50)
def test_alf::importreference_instantiation(instance):
    assert isinstance(instance, alf::ImportReference)

@given(instance=alf::ImportReference_strategy)
def test_alf::importreference_star_type(instance):
    assert isinstance(instance.star, bool)


@given(instance=alf::ImportReference_strategy)
def test_alf::importreference_star_setter(instance):
    original = instance.star
    instance.star = original
    assert instance.star == original

@given(instance=alf::ConditionalAndExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::conditionalandexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::ConditionalAndExpressionCompletion)

@given(instance=alf::ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_alf::conditionalandexpression_instantiation(instance):
    assert isinstance(instance, alf::ConditionalAndExpression)

@given(instance=alf::InclusiveOrExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::inclusiveorexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::InclusiveOrExpressionCompletion)

@given(instance=alf::InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_alf::inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, alf::InclusiveOrExpression)

@given(instance=alf::ExclusiveOrExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::exclusiveorexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::ExclusiveOrExpressionCompletion)

@given(instance=alf::ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_alf::exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, alf::ExclusiveOrExpression)

@given(instance=alf::AndExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::andexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::AndExpressionCompletion)

@given(instance=alf::ShiftExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::shiftexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::ShiftExpressionCompletion)

@given(instance=alf::ShiftExpressionCompletion_strategy)
def test_alf::shiftexpressioncompletion_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=alf::ShiftExpressionCompletion_strategy)
def test_alf::shiftexpressioncompletion_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf::ShiftExpression_strategy)
@settings(max_examples=50)
def test_alf::shiftexpression_instantiation(instance):
    assert isinstance(instance, alf::ShiftExpression)

@given(instance=alf::EqualityExpression_strategy)
@settings(max_examples=50)
def test_alf::equalityexpression_instantiation(instance):
    assert isinstance(instance, alf::EqualityExpression)

@given(instance=alf::ClassificationExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::classificationexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::ClassificationExpressionCompletion)

@given(instance=alf::ClassificationExpressionCompletion_strategy)
def test_alf::classificationexpressioncompletion_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=alf::ClassificationExpressionCompletion_strategy)
def test_alf::classificationexpressioncompletion_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf::ClassificationExpression_strategy)
@settings(max_examples=50)
def test_alf::classificationexpression_instantiation(instance):
    assert isinstance(instance, alf::ClassificationExpression)

@given(instance=alf::RelationalExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::relationalexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::RelationalExpressionCompletion)

@given(instance=alf::RelationalExpressionCompletion_strategy)
def test_alf::relationalexpressioncompletion_relationalOperator_type(instance):
    assert isinstance(instance.relationalOperator, str)


@given(instance=alf::RelationalExpressionCompletion_strategy)
def test_alf::relationalexpressioncompletion_relationalOperator_setter(instance):
    original = instance.relationalOperator
    instance.relationalOperator = original
    assert instance.relationalOperator == original

@given(instance=alf::RelationalExpression_strategy)
@settings(max_examples=50)
def test_alf::relationalexpression_instantiation(instance):
    assert isinstance(instance, alf::RelationalExpression)

@given(instance=alf::AdditiveExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::additiveexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::AdditiveExpressionCompletion)

@given(instance=alf::AdditiveExpressionCompletion_strategy)
def test_alf::additiveexpressioncompletion_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=alf::AdditiveExpressionCompletion_strategy)
def test_alf::additiveexpressioncompletion_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf::AdditiveExpression_strategy)
@settings(max_examples=50)
def test_alf::additiveexpression_instantiation(instance):
    assert isinstance(instance, alf::AdditiveExpression)

@given(instance=alf::MultiplicativeExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::multiplicativeexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::MultiplicativeExpressionCompletion)

@given(instance=alf::MultiplicativeExpressionCompletion_strategy)
def test_alf::multiplicativeexpressioncompletion_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=alf::MultiplicativeExpressionCompletion_strategy)
def test_alf::multiplicativeexpressioncompletion_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf::MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_alf::multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, alf::MultiplicativeExpression)

@given(instance=alf::CastCompletion_strategy)
@settings(max_examples=50)
def test_alf::castcompletion_instantiation(instance):
    assert isinstance(instance, alf::CastCompletion)

@given(instance=NonNameUnaryExpression_strategy)
@settings(max_examples=50)
def test_nonnameunaryexpression_instantiation(instance):
    assert isinstance(instance, NonNameUnaryExpression)

@given(instance=alf::NonNamePostfixOrCastExpression_strategy)
@settings(max_examples=50)
def test_alf::nonnamepostfixorcastexpression_instantiation(instance):
    assert isinstance(instance, alf::NonNamePostfixOrCastExpression)

@given(instance=alf::NonNamePostfixOrCastExpression_strategy)
def test_alf::nonnamepostfixorcastexpression_any_type(instance):
    assert isinstance(instance.any, bool)


@given(instance=alf::NonNamePostfixOrCastExpression_strategy)
def test_alf::nonnamepostfixorcastexpression_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=CastCompletion_strategy)
@settings(max_examples=50)
def test_castcompletion_instantiation(instance):
    assert isinstance(instance, CastCompletion)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=alf::NonPostfixNonCastUnaryExpression_strategy)
@settings(max_examples=50)
def test_alf::nonpostfixnoncastunaryexpression_instantiation(instance):
    assert isinstance(instance, alf::NonPostfixNonCastUnaryExpression)

@given(instance=alf::PostfixOrCastExpression_strategy)
@settings(max_examples=50)
def test_alf::postfixorcastexpression_instantiation(instance):
    assert isinstance(instance, alf::PostfixOrCastExpression)

@given(instance=NonPostfixNonCastUnaryExpression_strategy)
@settings(max_examples=50)
def test_nonpostfixnoncastunaryexpression_instantiation(instance):
    assert isinstance(instance, NonPostfixNonCastUnaryExpression)

@given(instance=alf::NumericUnaryExpression_strategy)
@settings(max_examples=50)
def test_alf::numericunaryexpression_instantiation(instance):
    assert isinstance(instance, alf::NumericUnaryExpression)

@given(instance=alf::NumericUnaryExpression_strategy)
def test_alf::numericunaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=alf::NumericUnaryExpression_strategy)
def test_alf::numericunaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf::BooleanNegationExpression_strategy)
@settings(max_examples=50)
def test_alf::booleannegationexpression_instantiation(instance):
    assert isinstance(instance, alf::BooleanNegationExpression)

@given(instance=alf::IsolationExpression_strategy)
@settings(max_examples=50)
def test_alf::isolationexpression_instantiation(instance):
    assert isinstance(instance, alf::IsolationExpression)

@given(instance=alf::BitStringComplementExpression_strategy)
@settings(max_examples=50)
def test_alf::bitstringcomplementexpression_instantiation(instance):
    assert isinstance(instance, alf::BitStringComplementExpression)

@given(instance=alf::PrefixExpression_strategy)
@settings(max_examples=50)
def test_alf::prefixexpression_instantiation(instance):
    assert isinstance(instance, alf::PrefixExpression)

@given(instance=alf::PrefixExpression_strategy)
def test_alf::prefixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=alf::PrefixExpression_strategy)
def test_alf::prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf::PostfixOperation_strategy)
@settings(max_examples=50)
def test_alf::postfixoperation_instantiation(instance):
    assert isinstance(instance, alf::PostfixOperation)

@given(instance=alf::PostfixOperation_strategy)
def test_alf::postfixoperation_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=alf::PostfixOperation_strategy)
def test_alf::postfixoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=alf::EObject_strategy)
@settings(max_examples=50)
def test_alf::eobject_instantiation(instance):
    assert isinstance(instance, alf::EObject)

@given(instance=alf::SequenceElement_strategy)
@settings(max_examples=50)
def test_alf::sequenceelement_instantiation(instance):
    assert isinstance(instance, alf::SequenceElement)

@given(instance=alf::SequenceElementListCompletion_strategy)
@settings(max_examples=50)
def test_alf::sequenceelementlistcompletion_instantiation(instance):
    assert isinstance(instance, alf::SequenceElementListCompletion)

@given(instance=alf::SequenceElements_strategy)
@settings(max_examples=50)
def test_alf::sequenceelements_instantiation(instance):
    assert isinstance(instance, alf::SequenceElements)

@given(instance=alf::MultiplicityIndicator_strategy)
@settings(max_examples=50)
def test_alf::multiplicityindicator_instantiation(instance):
    assert isinstance(instance, alf::MultiplicityIndicator)

@given(instance=alf::IndexedNamedExpression_strategy)
@settings(max_examples=50)
def test_alf::indexednamedexpression_instantiation(instance):
    assert isinstance(instance, alf::IndexedNamedExpression)

@given(instance=alf::IndexedNamedExpressionListCompletion_strategy)
@settings(max_examples=50)
def test_alf::indexednamedexpressionlistcompletion_instantiation(instance):
    assert isinstance(instance, alf::IndexedNamedExpressionListCompletion)

@given(instance=alf::LinkOperationTuple_strategy)
@settings(max_examples=50)
def test_alf::linkoperationtuple_instantiation(instance):
    assert isinstance(instance, alf::LinkOperationTuple)

@given(instance=BaseExpression_strategy)
@settings(max_examples=50)
def test_baseexpression_instantiation(instance):
    assert isinstance(instance, BaseExpression)

@given(instance=alf::SuperInvocationExpression_strategy)
@settings(max_examples=50)
def test_alf::superinvocationexpression_instantiation(instance):
    assert isinstance(instance, alf::SuperInvocationExpression)

@given(instance=alf::InstanceCreationOrSequenceConstructionExpression_strategy)
@settings(max_examples=50)
def test_alf::instancecreationorsequenceconstructionexpression_instantiation(instance):
    assert isinstance(instance, alf::InstanceCreationOrSequenceConstructionExpression)

@given(instance=alf::SequenceAnyExpression_strategy)
@settings(max_examples=50)
def test_alf::sequenceanyexpression_instantiation(instance):
    assert isinstance(instance, alf::SequenceAnyExpression)

@given(instance=alf::LiteralExpression_strategy)
@settings(max_examples=50)
def test_alf::literalexpression_instantiation(instance):
    assert isinstance(instance, alf::LiteralExpression)

@given(instance=alf::Index_strategy)
@settings(max_examples=50)
def test_alf::index_instantiation(instance):
    assert isinstance(instance, alf::Index)

@given(instance=alf::NamedExpression_strategy)
@settings(max_examples=50)
def test_alf::namedexpression_instantiation(instance):
    assert isinstance(instance, alf::NamedExpression)

@given(instance=alf::PositionalTupleExpressionListCompletion_strategy)
@settings(max_examples=50)
def test_alf::positionaltupleexpressionlistcompletion_instantiation(instance):
    assert isinstance(instance, alf::PositionalTupleExpressionListCompletion)

@given(instance=alf::PositionalTupleExpressionList_strategy)
@settings(max_examples=50)
def test_alf::positionaltupleexpressionlist_instantiation(instance):
    assert isinstance(instance, alf::PositionalTupleExpressionList)

@given(instance=alf::NamedTupleExpressionList_strategy)
@settings(max_examples=50)
def test_alf::namedtupleexpressionlist_instantiation(instance):
    assert isinstance(instance, alf::NamedTupleExpressionList)

@given(instance=alf::Tuple_strategy)
@settings(max_examples=50)
def test_alf::tuple_instantiation(instance):
    assert isinstance(instance, alf::Tuple)

@given(instance=alf::ThisExpression_strategy)
@settings(max_examples=50)
def test_alf::thisexpression_instantiation(instance):
    assert isinstance(instance, alf::ThisExpression)

@given(instance=alf::ExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::expressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::ExpressionCompletion)

@given(instance=alf::UnaryExpression_strategy)
@settings(max_examples=50)
def test_alf::unaryexpression_instantiation(instance):
    assert isinstance(instance, alf::UnaryExpression)

@given(instance=InitializationExpression_strategy)
@settings(max_examples=50)
def test_initializationexpression_instantiation(instance):
    assert isinstance(instance, InitializationExpression)

@given(instance=alf::InstanceInitializationExpression_strategy)
@settings(max_examples=50)
def test_alf::instanceinitializationexpression_instantiation(instance):
    assert isinstance(instance, alf::InstanceInitializationExpression)

@given(instance=alf::SequenceInitializationExpression_strategy)
@settings(max_examples=50)
def test_alf::sequenceinitializationexpression_instantiation(instance):
    assert isinstance(instance, alf::SequenceInitializationExpression)

@given(instance=alf::SequenceInitializationExpression_strategy)
def test_alf::sequenceinitializationexpression_isNew_type(instance):
    assert isinstance(instance.isNew, bool)


@given(instance=alf::SequenceInitializationExpression_strategy)
def test_alf::sequenceinitializationexpression_isNew_setter(instance):
    original = instance.isNew
    instance.isNew = original
    assert instance.isNew == original

@given(instance=alf::Expression_strategy)
@settings(max_examples=50)
def test_alf::expression_instantiation(instance):
    assert isinstance(instance, alf::Expression)

@given(instance=alf::SequenceOperationOrReductionOrExpansion_strategy)
@settings(max_examples=50)
def test_alf::sequenceoperationorreductionorexpansion_instantiation(instance):
    assert isinstance(instance, alf::SequenceOperationOrReductionOrExpansion)

@given(instance=alf::SequenceOperationOrReductionOrExpansion_strategy)
def test_alf::sequenceoperationorreductionorexpansion_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, bool)


@given(instance=alf::SequenceOperationOrReductionOrExpansion_strategy)
def test_alf::sequenceoperationorreductionorexpansion_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=alf::SequenceOperationOrReductionOrExpansion_strategy)
def test_alf::sequenceoperationorreductionorexpansion_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=alf::SequenceOperationOrReductionOrExpansion_strategy)
def test_alf::sequenceoperationorreductionorexpansion_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=alf::SequenceOperationOrReductionOrExpansion_strategy)
def test_alf::sequenceoperationorreductionorexpansion_isReduce_type(instance):
    assert isinstance(instance.isReduce, bool)


@given(instance=alf::SequenceOperationOrReductionOrExpansion_strategy)
def test_alf::sequenceoperationorreductionorexpansion_isReduce_setter(instance):
    original = instance.isReduce
    instance.isReduce = original
    assert instance.isReduce == original

@given(instance=alf::FeatureInvocation_strategy)
@settings(max_examples=50)
def test_alf::featureinvocation_instantiation(instance):
    assert isinstance(instance, alf::FeatureInvocation)

@given(instance=alf::Feature_strategy)
@settings(max_examples=50)
def test_alf::feature_instantiation(instance):
    assert isinstance(instance, alf::Feature)

@given(instance=alf::Feature::Or::SequenceOperationOrReductionOrExpansion::Or::Index_strategy)
@settings(max_examples=50)
def test_alf::feature::or::sequenceoperationorreductionorexpansion::or::index_instantiation(instance):
    assert isinstance(instance, alf::Feature::Or::SequenceOperationOrReductionOrExpansion::Or::Index)

@given(instance=alf::BehaviorInvocation_strategy)
@settings(max_examples=50)
def test_alf::behaviorinvocation_instantiation(instance):
    assert isinstance(instance, alf::BehaviorInvocation)

@given(instance=alf::SequenceConstructionExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::sequenceconstructionexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::SequenceConstructionExpressionCompletion)

@given(instance=alf::ClassExtentExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::classextentexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::ClassExtentExpressionCompletion)

@given(instance=alf::LinkOperationCompletion_strategy)
@settings(max_examples=50)
def test_alf::linkoperationcompletion_instantiation(instance):
    assert isinstance(instance, alf::LinkOperationCompletion)

@given(instance=alf::LinkOperationCompletion_strategy)
def test_alf::linkoperationcompletion_linkOperation_type(instance):
    assert isinstance(instance.linkOperation, str)


@given(instance=alf::LinkOperationCompletion_strategy)
def test_alf::linkoperationcompletion_linkOperation_setter(instance):
    original = instance.linkOperation
    instance.linkOperation = original
    assert instance.linkOperation == original

@given(instance=alf::PrimaryExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::primaryexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::PrimaryExpressionCompletion)

@given(instance=alf::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_alf::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, alf::ParenthesizedExpression)

@given(instance=alf::BaseExpression_strategy)
@settings(max_examples=50)
def test_alf::baseexpression_instantiation(instance):
    assert isinstance(instance, alf::BaseExpression)

@given(instance=alf::NameOrPrimaryExpression_strategy)
@settings(max_examples=50)
def test_alf::nameorprimaryexpression_instantiation(instance):
    assert isinstance(instance, alf::NameOrPrimaryExpression)

@given(instance=alf::PrimaryExpression_strategy)
@settings(max_examples=50)
def test_alf::primaryexpression_instantiation(instance):
    assert isinstance(instance, alf::PrimaryExpression)

@given(instance=alf::PostfixExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::postfixexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::PostfixExpressionCompletion)

@given(instance=alf::PrimaryToExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::primarytoexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::PrimaryToExpressionCompletion)

@given(instance=alf::NameToPrimaryExpression_strategy)
@settings(max_examples=50)
def test_alf::nametoprimaryexpression_instantiation(instance):
    assert isinstance(instance, alf::NameToPrimaryExpression)

@given(instance=alf::NameToExpressionCompletion_strategy)
@settings(max_examples=50)
def test_alf::nametoexpressioncompletion_instantiation(instance):
    assert isinstance(instance, alf::NameToExpressionCompletion)

@given(instance=alf::NonNameUnaryExpression_strategy)
@settings(max_examples=50)
def test_alf::nonnameunaryexpression_instantiation(instance):
    assert isinstance(instance, alf::NonNameUnaryExpression)

@given(instance=alf::NonNameExpression_strategy)
@settings(max_examples=50)
def test_alf::nonnameexpression_instantiation(instance):
    assert isinstance(instance, alf::NonNameExpression)

@given(instance=alf::SignalReceptionDeclaration_strategy)
@settings(max_examples=50)
def test_alf::signalreceptiondeclaration_instantiation(instance):
    assert isinstance(instance, alf::SignalReceptionDeclaration)

@given(instance=alf::TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_alf::templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, alf::TemplateParameterSubstitution)

@given(instance=TemplateBinding_strategy)
@settings(max_examples=50)
def test_templatebinding_instantiation(instance):
    assert isinstance(instance, TemplateBinding)

@given(instance=alf::NamedTemplateBinding_strategy)
@settings(max_examples=50)
def test_alf::namedtemplatebinding_instantiation(instance):
    assert isinstance(instance, alf::NamedTemplateBinding)

@given(instance=alf::PositionalTemplateBinding_strategy)
@settings(max_examples=50)
def test_alf::positionaltemplatebinding_instantiation(instance):
    assert isinstance(instance, alf::PositionalTemplateBinding)

@given(instance=alf::ColonQualifiedNameCompletionWithoutBinding_strategy)
@settings(max_examples=50)
def test_alf::colonqualifiednamecompletionwithoutbinding_instantiation(instance):
    assert isinstance(instance, alf::ColonQualifiedNameCompletionWithoutBinding)

@given(instance=alf::QualifiedNameWithoutBinding_strategy)
@settings(max_examples=50)
def test_alf::qualifiednamewithoutbinding_instantiation(instance):
    assert isinstance(instance, alf::QualifiedNameWithoutBinding)

@given(instance=alf::TemplateBinding_strategy)
@settings(max_examples=50)
def test_alf::templatebinding_instantiation(instance):
    assert isinstance(instance, alf::TemplateBinding)

@given(instance=UnqualifiedName_strategy)
@settings(max_examples=50)
def test_unqualifiedname_instantiation(instance):
    assert isinstance(instance, UnqualifiedName)

@given(instance=alf::NameBinding_strategy)
@settings(max_examples=50)
def test_alf::namebinding_instantiation(instance):
    assert isinstance(instance, alf::NameBinding)

@given(instance=alf::ColonQualifiedNameCompletion_strategy)
@settings(max_examples=50)
def test_alf::colonqualifiednamecompletion_instantiation(instance):
    assert isinstance(instance, alf::ColonQualifiedNameCompletion)

@given(instance=alf::UnqualifiedName_strategy)
@settings(max_examples=50)
def test_alf::unqualifiedname_instantiation(instance):
    assert isinstance(instance, alf::UnqualifiedName)

@given(instance=alf::InitializationExpression_strategy)
@settings(max_examples=50)
def test_alf::initializationexpression_instantiation(instance):
    assert isinstance(instance, alf::InitializationExpression)

@given(instance=ActiveFeatureDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_activefeaturedefinitionorstub_instantiation(instance):
    assert isinstance(instance, ActiveFeatureDefinitionOrStub)

@given(instance=alf::SignalReceptionDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf::signalreceptiondefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf::SignalReceptionDefinitionOrStub)

@given(instance=alf::ReceptionDefinition_strategy)
@settings(max_examples=50)
def test_alf::receptiondefinition_instantiation(instance):
    assert isinstance(instance, alf::ReceptionDefinition)

@given(instance=alf::AttributeInitializer_strategy)
@settings(max_examples=50)
def test_alf::attributeinitializer_instantiation(instance):
    assert isinstance(instance, alf::AttributeInitializer)

@given(instance=alf::OperationDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf::operationdefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf::OperationDefinitionOrStub)
