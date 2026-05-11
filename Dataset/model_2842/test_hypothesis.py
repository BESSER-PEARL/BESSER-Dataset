import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    alf::Annotation,
    alf::NonFinalClause,
    alf::ConcurrentClauses,
    alf::FinalClause,
    alf::DocumentedStatement,
    alf::StatementSequence,
    alf::ClassExtentExpression,
    alf::SequenceElement,
    Statement,
    alf::EmptyStatement,
    alf::InlineStatement,
    alf::BlockStatement,
    alf::AnnotatedStatement,
    alf::AccessCompletion,
    alf::NonLiteralValueSpecification,
    alf::SequenceConstructionCompletion,
    alf::PartialSequenceConstructionCompletion,
    SequenceExpansionExpression,
    alf::SelectOrRejectOperation,
    alf::IsUniqueOperation,
    alf::ForAllOrExistsOrOneOperation,
    alf::CollectOrIterateOperation,
    alf::LinkOperationTupleElement,
    alf::LinkOperationTuple,
    alf::ShiftExpression,
    alf::RelationalExpression,
    alf::OperationCallExpressionWithoutDot,
    SuffixExpression,
    alf::PropertyCallExpression,
    alf::SequenceReductionExpression,
    alf::SequenceExpansionExpression,
    alf::LinkOperationExpression,
    alf::SequenceOperationExpression,
    alf::OperationCallExpression,
    alf::ValueSpecification,
    alf::PrimaryExpression,
    alf::UnaryExpression,
    alf::MultiplicativeExpression,
    alf::AdditiveExpression,
    alf::TupleElement,
    alf::NamedTemplateBinding,
    alf::ClassificationExpression,
    alf::EqualityExpression,
    alf::AndExpression,
    alf::ExclusiveOrExpression,
    alf::InclusiveOrExpression,
    alf::ConditionalAndExpression,
    alf::ConditionalOrExpression,
    alf::InstanceCreationInvocationStatement,
    alf::ThisInvocationStatement,
    alf::InvocationOrAssignementOrDeclarationStatement,
    alf::ReclassifyAllClause,
    alf::ClassificationToClause,
    alf::ClassificationFromClause,
    alf::ClassificationClause,
    alf::ClassifyStatement,
    alf::SuperInvocationStatement,
    alf::VariableDeclarationCompletion,
    alf::CompoundAcceptStatementCompletion,
    alf::SimpleAcceptStatementCompletion,
    alf::AcceptClause,
    alf::AcceptStatement,
    alf::ReturnStatement,
    alf::BreakStatement,
    alf::LoopVariableDefinition,
    alf::ForControl,
    alf::ForStatement,
    alf::AcceptBlock,
    alf::WhileStatement,
    alf::NonEmptyStatementSequence,
    alf::SwitchCase,
    alf::SwitchDefaultClause,
    alf::SwitchClause,
    alf::SwitchStatement,
    alf::DoStatement,
    alf::SequentialClauses,
    alf::IfStatement,
    alf::LocalNameDeclarationStatement,
    Expression,
    alf::ConditionalTestExpression,
    SequenceElement,
    alf::SequenceConstructionExpression,
    LITERAL,
    alf::BOOLEAN::LITERAL,
    alf::SuffixExpression,
    ValueSpecification,
    alf::NullExpression,
    alf::LITERAL,
    alf::Statement,
    alf::AssignmentCompletion,
    alf::TemplateBinding,
    alf::UnqualifiedName,
    alf::SequenceConstructionOrAccessCompletion,
    alf::Tuple,
    alf::QualifiedNamePath,
    NonLiteralValueSpecification,
    alf::ParenthesizedExpression,
    alf::InstanceCreationExpression,
    alf::SuperInvocationExpression,
    alf::ThisExpression,
    alf::NameExpression,
    alf::STRING::LITERAL,
    NUMBER::LITERAL,
    alf::UNLIMITED::LITERAL,
    alf::INTEGER::LITERAL,
    alf::NUMBER::LITERAL,
    alf::MultiplicityRange,
    alf::Multiplicity,
    alf::Expression,
    alf::Test,
    alf::QualifiedNameList,
    alf::QualifiedNameWithBinding,
    NUMBER::LITERAL::WITHOUT::SUFFIX,
    alf::UNLIMITED::LITERAL::WITHOUT::SUFFIX,
    alf::INTEGER::LITERAL::WITHOUT::SUFFIX,
    alf::NUMBER::LITERAL::WITHOUT::SUFFIX,
    alf::FormalParameters,
    alf::Block,
    alf::OperationDeclaration,
    alf::TypeName,
    alf::FormalParameter,
    alf::FormalParameterList,
    alf::RedefinitionClause,
    alf::OperationDefinitionOrStub,
    alf::TypePart,
    alf::Operations,
    LinkOperationKind,
    SelectOrRejectOperator,
    ParameterDirection,
    AnnotationKind,
    ForAllOrExistsOrOneOperator,
    BooleanValue,
    AssignmentOperator,
    CollectOrIterateOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_alf::annotation_is_not_abstract():
    assert not inspect.isabstract(alf::Annotation)


def test_alf::annotation_constructor_exists():
    assert callable(alf::Annotation.__init__)


def test_alf::annotation_constructor_args():
    sig = inspect.signature(alf::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "args" in params, "Missing parameter 'args'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_alf::annotation_has_args():
    assert hasattr(alf::Annotation, "args")
    descriptor = None
    for klass in alf::Annotation.__mro__:
        if "args" in klass.__dict__:
            descriptor = klass.__dict__["args"]
            break
    assert isinstance(descriptor, property)

def test_alf::annotation_has_kind():
    assert hasattr(alf::Annotation, "kind")
    descriptor = None
    for klass in alf::Annotation.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



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



def test_alf::classextentexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ClassExtentExpression)


def test_alf::classextentexpression_constructor_exists():
    assert callable(alf::ClassExtentExpression.__init__)


def test_alf::classextentexpression_constructor_args():
    sig = inspect.signature(alf::ClassExtentExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::sequenceelement_is_not_abstract():
    assert not inspect.isabstract(alf::SequenceElement)


def test_alf::sequenceelement_constructor_exists():
    assert callable(alf::SequenceElement.__init__)


def test_alf::sequenceelement_constructor_args():
    sig = inspect.signature(alf::SequenceElement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_alf::emptystatement_is_not_abstract():
    assert not inspect.isabstract(alf::EmptyStatement)


def test_alf::emptystatement_constructor_exists():
    assert callable(alf::EmptyStatement.__init__)


def test_alf::emptystatement_constructor_args():
    sig = inspect.signature(alf::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::inlinestatement_is_not_abstract():
    assert not inspect.isabstract(alf::InlineStatement)


def test_alf::inlinestatement_constructor_exists():
    assert callable(alf::InlineStatement.__init__)


def test_alf::inlinestatement_constructor_args():
    sig = inspect.signature(alf::InlineStatement.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "langageName" in params, "Missing parameter 'langageName'"

def test_alf::inlinestatement_has_body():
    assert hasattr(alf::InlineStatement, "body")
    descriptor = None
    for klass in alf::InlineStatement.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_alf::inlinestatement_has_langageName():
    assert hasattr(alf::InlineStatement, "langageName")
    descriptor = None
    for klass in alf::InlineStatement.__mro__:
        if "langageName" in klass.__dict__:
            descriptor = klass.__dict__["langageName"]
            break
    assert isinstance(descriptor, property)



def test_alf::blockstatement_is_not_abstract():
    assert not inspect.isabstract(alf::BlockStatement)


def test_alf::blockstatement_constructor_exists():
    assert callable(alf::BlockStatement.__init__)


def test_alf::blockstatement_constructor_args():
    sig = inspect.signature(alf::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::annotatedstatement_is_not_abstract():
    assert not inspect.isabstract(alf::AnnotatedStatement)


def test_alf::annotatedstatement_constructor_exists():
    assert callable(alf::AnnotatedStatement.__init__)


def test_alf::annotatedstatement_constructor_args():
    sig = inspect.signature(alf::AnnotatedStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::accesscompletion_is_not_abstract():
    assert not inspect.isabstract(alf::AccessCompletion)


def test_alf::accesscompletion_constructor_exists():
    assert callable(alf::AccessCompletion.__init__)


def test_alf::accesscompletion_constructor_args():
    sig = inspect.signature(alf::AccessCompletion.__init__)
    params = list(sig.parameters.keys())



def test_alf::nonliteralvaluespecification_is_not_abstract():
    assert not inspect.isabstract(alf::NonLiteralValueSpecification)


def test_alf::nonliteralvaluespecification_constructor_exists():
    assert callable(alf::NonLiteralValueSpecification.__init__)


def test_alf::nonliteralvaluespecification_constructor_args():
    sig = inspect.signature(alf::NonLiteralValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_alf::sequenceconstructioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::SequenceConstructionCompletion)


def test_alf::sequenceconstructioncompletion_constructor_exists():
    assert callable(alf::SequenceConstructionCompletion.__init__)


def test_alf::sequenceconstructioncompletion_constructor_args():
    sig = inspect.signature(alf::SequenceConstructionCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicityIndicator" in params, "Missing parameter 'multiplicityIndicator'"

def test_alf::sequenceconstructioncompletion_has_multiplicityIndicator():
    assert hasattr(alf::SequenceConstructionCompletion, "multiplicityIndicator")
    descriptor = None
    for klass in alf::SequenceConstructionCompletion.__mro__:
        if "multiplicityIndicator" in klass.__dict__:
            descriptor = klass.__dict__["multiplicityIndicator"]
            break
    assert isinstance(descriptor, property)



def test_alf::partialsequenceconstructioncompletion_is_not_abstract():
    assert not inspect.isabstract(alf::PartialSequenceConstructionCompletion)


def test_alf::partialsequenceconstructioncompletion_constructor_exists():
    assert callable(alf::PartialSequenceConstructionCompletion.__init__)


def test_alf::partialsequenceconstructioncompletion_constructor_args():
    sig = inspect.signature(alf::PartialSequenceConstructionCompletion.__init__)
    params = list(sig.parameters.keys())



def test_sequenceexpansionexpression_is_not_abstract():
    assert not inspect.isabstract(SequenceExpansionExpression)


def test_sequenceexpansionexpression_constructor_exists():
    assert callable(SequenceExpansionExpression.__init__)


def test_sequenceexpansionexpression_constructor_args():
    sig = inspect.signature(SequenceExpansionExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::selectorrejectoperation_is_not_abstract():
    assert not inspect.isabstract(alf::SelectOrRejectOperation)


def test_alf::selectorrejectoperation_constructor_exists():
    assert callable(alf::SelectOrRejectOperation.__init__)


def test_alf::selectorrejectoperation_constructor_args():
    sig = inspect.signature(alf::SelectOrRejectOperation.__init__)
    params = list(sig.parameters.keys())
    assert "expr1" in params, "Missing parameter 'expr1'"
    assert "expr3" in params, "Missing parameter 'expr3'"
    assert "expr2" in params, "Missing parameter 'expr2'"
    assert "op" in params, "Missing parameter 'op'"
    assert "expr4" in params, "Missing parameter 'expr4'"

def test_alf::selectorrejectoperation_has_expr1():
    assert hasattr(alf::SelectOrRejectOperation, "expr1")
    descriptor = None
    for klass in alf::SelectOrRejectOperation.__mro__:
        if "expr1" in klass.__dict__:
            descriptor = klass.__dict__["expr1"]
            break
    assert isinstance(descriptor, property)

def test_alf::selectorrejectoperation_has_expr3():
    assert hasattr(alf::SelectOrRejectOperation, "expr3")
    descriptor = None
    for klass in alf::SelectOrRejectOperation.__mro__:
        if "expr3" in klass.__dict__:
            descriptor = klass.__dict__["expr3"]
            break
    assert isinstance(descriptor, property)

def test_alf::selectorrejectoperation_has_expr2():
    assert hasattr(alf::SelectOrRejectOperation, "expr2")
    descriptor = None
    for klass in alf::SelectOrRejectOperation.__mro__:
        if "expr2" in klass.__dict__:
            descriptor = klass.__dict__["expr2"]
            break
    assert isinstance(descriptor, property)

def test_alf::selectorrejectoperation_has_op():
    assert hasattr(alf::SelectOrRejectOperation, "op")
    descriptor = None
    for klass in alf::SelectOrRejectOperation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_alf::selectorrejectoperation_has_expr4():
    assert hasattr(alf::SelectOrRejectOperation, "expr4")
    descriptor = None
    for klass in alf::SelectOrRejectOperation.__mro__:
        if "expr4" in klass.__dict__:
            descriptor = klass.__dict__["expr4"]
            break
    assert isinstance(descriptor, property)



def test_alf::isuniqueoperation_is_not_abstract():
    assert not inspect.isabstract(alf::IsUniqueOperation)


def test_alf::isuniqueoperation_constructor_exists():
    assert callable(alf::IsUniqueOperation.__init__)


def test_alf::isuniqueoperation_constructor_args():
    sig = inspect.signature(alf::IsUniqueOperation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_alf::isuniqueoperation_has_name():
    assert hasattr(alf::IsUniqueOperation, "name")
    descriptor = None
    for klass in alf::IsUniqueOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_alf::forallorexistsoroneoperation_is_not_abstract():
    assert not inspect.isabstract(alf::ForAllOrExistsOrOneOperation)


def test_alf::forallorexistsoroneoperation_constructor_exists():
    assert callable(alf::ForAllOrExistsOrOneOperation.__init__)


def test_alf::forallorexistsoroneoperation_constructor_args():
    sig = inspect.signature(alf::ForAllOrExistsOrOneOperation.__init__)
    params = list(sig.parameters.keys())
    assert "expr2" in params, "Missing parameter 'expr2'"
    assert "op" in params, "Missing parameter 'op'"
    assert "expr1" in params, "Missing parameter 'expr1'"
    assert "expr4" in params, "Missing parameter 'expr4'"
    assert "expr3" in params, "Missing parameter 'expr3'"

def test_alf::forallorexistsoroneoperation_has_expr2():
    assert hasattr(alf::ForAllOrExistsOrOneOperation, "expr2")
    descriptor = None
    for klass in alf::ForAllOrExistsOrOneOperation.__mro__:
        if "expr2" in klass.__dict__:
            descriptor = klass.__dict__["expr2"]
            break
    assert isinstance(descriptor, property)

def test_alf::forallorexistsoroneoperation_has_op():
    assert hasattr(alf::ForAllOrExistsOrOneOperation, "op")
    descriptor = None
    for klass in alf::ForAllOrExistsOrOneOperation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_alf::forallorexistsoroneoperation_has_expr1():
    assert hasattr(alf::ForAllOrExistsOrOneOperation, "expr1")
    descriptor = None
    for klass in alf::ForAllOrExistsOrOneOperation.__mro__:
        if "expr1" in klass.__dict__:
            descriptor = klass.__dict__["expr1"]
            break
    assert isinstance(descriptor, property)

def test_alf::forallorexistsoroneoperation_has_expr4():
    assert hasattr(alf::ForAllOrExistsOrOneOperation, "expr4")
    descriptor = None
    for klass in alf::ForAllOrExistsOrOneOperation.__mro__:
        if "expr4" in klass.__dict__:
            descriptor = klass.__dict__["expr4"]
            break
    assert isinstance(descriptor, property)

def test_alf::forallorexistsoroneoperation_has_expr3():
    assert hasattr(alf::ForAllOrExistsOrOneOperation, "expr3")
    descriptor = None
    for klass in alf::ForAllOrExistsOrOneOperation.__mro__:
        if "expr3" in klass.__dict__:
            descriptor = klass.__dict__["expr3"]
            break
    assert isinstance(descriptor, property)



def test_alf::collectoriterateoperation_is_not_abstract():
    assert not inspect.isabstract(alf::CollectOrIterateOperation)


def test_alf::collectoriterateoperation_constructor_exists():
    assert callable(alf::CollectOrIterateOperation.__init__)


def test_alf::collectoriterateoperation_constructor_args():
    sig = inspect.signature(alf::CollectOrIterateOperation.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "expr3" in params, "Missing parameter 'expr3'"
    assert "expr4" in params, "Missing parameter 'expr4'"
    assert "expr1" in params, "Missing parameter 'expr1'"
    assert "expr2" in params, "Missing parameter 'expr2'"

def test_alf::collectoriterateoperation_has_op():
    assert hasattr(alf::CollectOrIterateOperation, "op")
    descriptor = None
    for klass in alf::CollectOrIterateOperation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_alf::collectoriterateoperation_has_expr3():
    assert hasattr(alf::CollectOrIterateOperation, "expr3")
    descriptor = None
    for klass in alf::CollectOrIterateOperation.__mro__:
        if "expr3" in klass.__dict__:
            descriptor = klass.__dict__["expr3"]
            break
    assert isinstance(descriptor, property)

def test_alf::collectoriterateoperation_has_expr4():
    assert hasattr(alf::CollectOrIterateOperation, "expr4")
    descriptor = None
    for klass in alf::CollectOrIterateOperation.__mro__:
        if "expr4" in klass.__dict__:
            descriptor = klass.__dict__["expr4"]
            break
    assert isinstance(descriptor, property)

def test_alf::collectoriterateoperation_has_expr1():
    assert hasattr(alf::CollectOrIterateOperation, "expr1")
    descriptor = None
    for klass in alf::CollectOrIterateOperation.__mro__:
        if "expr1" in klass.__dict__:
            descriptor = klass.__dict__["expr1"]
            break
    assert isinstance(descriptor, property)

def test_alf::collectoriterateoperation_has_expr2():
    assert hasattr(alf::CollectOrIterateOperation, "expr2")
    descriptor = None
    for klass in alf::CollectOrIterateOperation.__mro__:
        if "expr2" in klass.__dict__:
            descriptor = klass.__dict__["expr2"]
            break
    assert isinstance(descriptor, property)



def test_alf::linkoperationtupleelement_is_not_abstract():
    assert not inspect.isabstract(alf::LinkOperationTupleElement)


def test_alf::linkoperationtupleelement_constructor_exists():
    assert callable(alf::LinkOperationTupleElement.__init__)


def test_alf::linkoperationtupleelement_constructor_args():
    sig = inspect.signature(alf::LinkOperationTupleElement.__init__)
    params = list(sig.parameters.keys())
    assert "objectOrRole" in params, "Missing parameter 'objectOrRole'"

def test_alf::linkoperationtupleelement_has_objectOrRole():
    assert hasattr(alf::LinkOperationTupleElement, "objectOrRole")
    descriptor = None
    for klass in alf::LinkOperationTupleElement.__mro__:
        if "objectOrRole" in klass.__dict__:
            descriptor = klass.__dict__["objectOrRole"]
            break
    assert isinstance(descriptor, property)



def test_alf::linkoperationtuple_is_not_abstract():
    assert not inspect.isabstract(alf::LinkOperationTuple)


def test_alf::linkoperationtuple_constructor_exists():
    assert callable(alf::LinkOperationTuple.__init__)


def test_alf::linkoperationtuple_constructor_args():
    sig = inspect.signature(alf::LinkOperationTuple.__init__)
    params = list(sig.parameters.keys())



def test_alf::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ShiftExpression)


def test_alf::shiftexpression_constructor_exists():
    assert callable(alf::ShiftExpression.__init__)


def test_alf::shiftexpression_constructor_args():
    sig = inspect.signature(alf::ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf::shiftexpression_has_op():
    assert hasattr(alf::ShiftExpression, "op")
    descriptor = None
    for klass in alf::ShiftExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(alf::RelationalExpression)


def test_alf::relationalexpression_constructor_exists():
    assert callable(alf::RelationalExpression.__init__)


def test_alf::relationalexpression_constructor_args():
    sig = inspect.signature(alf::RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf::relationalexpression_has_op():
    assert hasattr(alf::RelationalExpression, "op")
    descriptor = None
    for klass in alf::RelationalExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf::operationcallexpressionwithoutdot_is_not_abstract():
    assert not inspect.isabstract(alf::OperationCallExpressionWithoutDot)


def test_alf::operationcallexpressionwithoutdot_constructor_exists():
    assert callable(alf::OperationCallExpressionWithoutDot.__init__)


def test_alf::operationcallexpressionwithoutdot_constructor_args():
    sig = inspect.signature(alf::OperationCallExpressionWithoutDot.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_alf::operationcallexpressionwithoutdot_has_operationName():
    assert hasattr(alf::OperationCallExpressionWithoutDot, "operationName")
    descriptor = None
    for klass in alf::OperationCallExpressionWithoutDot.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_suffixexpression_is_not_abstract():
    assert not inspect.isabstract(SuffixExpression)


def test_suffixexpression_constructor_exists():
    assert callable(SuffixExpression.__init__)


def test_suffixexpression_constructor_args():
    sig = inspect.signature(SuffixExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::propertycallexpression_is_not_abstract():
    assert not inspect.isabstract(alf::PropertyCallExpression)


def test_alf::propertycallexpression_constructor_exists():
    assert callable(alf::PropertyCallExpression.__init__)


def test_alf::propertycallexpression_constructor_args():
    sig = inspect.signature(alf::PropertyCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_alf::propertycallexpression_has_propertyName():
    assert hasattr(alf::PropertyCallExpression, "propertyName")
    descriptor = None
    for klass in alf::PropertyCallExpression.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_alf::sequencereductionexpression_is_not_abstract():
    assert not inspect.isabstract(alf::SequenceReductionExpression)


def test_alf::sequencereductionexpression_constructor_exists():
    assert callable(alf::SequenceReductionExpression.__init__)


def test_alf::sequencereductionexpression_constructor_args():
    sig = inspect.signature(alf::SequenceReductionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_alf::sequencereductionexpression_has_isOrdered():
    assert hasattr(alf::SequenceReductionExpression, "isOrdered")
    descriptor = None
    for klass in alf::SequenceReductionExpression.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_alf::sequenceexpansionexpression_is_not_abstract():
    assert not inspect.isabstract(alf::SequenceExpansionExpression)


def test_alf::sequenceexpansionexpression_constructor_exists():
    assert callable(alf::SequenceExpansionExpression.__init__)


def test_alf::sequenceexpansionexpression_constructor_args():
    sig = inspect.signature(alf::SequenceExpansionExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::linkoperationexpression_is_not_abstract():
    assert not inspect.isabstract(alf::LinkOperationExpression)


def test_alf::linkoperationexpression_constructor_exists():
    assert callable(alf::LinkOperationExpression.__init__)


def test_alf::linkoperationexpression_constructor_args():
    sig = inspect.signature(alf::LinkOperationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_alf::linkoperationexpression_has_kind():
    assert hasattr(alf::LinkOperationExpression, "kind")
    descriptor = None
    for klass in alf::LinkOperationExpression.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_alf::sequenceoperationexpression_is_not_abstract():
    assert not inspect.isabstract(alf::SequenceOperationExpression)


def test_alf::sequenceoperationexpression_constructor_exists():
    assert callable(alf::SequenceOperationExpression.__init__)


def test_alf::sequenceoperationexpression_constructor_args():
    sig = inspect.signature(alf::SequenceOperationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_alf::sequenceoperationexpression_has_operationName():
    assert hasattr(alf::SequenceOperationExpression, "operationName")
    descriptor = None
    for klass in alf::SequenceOperationExpression.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_alf::operationcallexpression_is_not_abstract():
    assert not inspect.isabstract(alf::OperationCallExpression)


def test_alf::operationcallexpression_constructor_exists():
    assert callable(alf::OperationCallExpression.__init__)


def test_alf::operationcallexpression_constructor_args():
    sig = inspect.signature(alf::OperationCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_alf::operationcallexpression_has_operationName():
    assert hasattr(alf::OperationCallExpression, "operationName")
    descriptor = None
    for klass in alf::OperationCallExpression.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_alf::valuespecification_is_not_abstract():
    assert not inspect.isabstract(alf::ValueSpecification)


def test_alf::valuespecification_constructor_exists():
    assert callable(alf::ValueSpecification.__init__)


def test_alf::valuespecification_constructor_args():
    sig = inspect.signature(alf::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_alf::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf::PrimaryExpression)


def test_alf::primaryexpression_constructor_exists():
    assert callable(alf::PrimaryExpression.__init__)


def test_alf::primaryexpression_constructor_args():
    sig = inspect.signature(alf::PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(alf::UnaryExpression)


def test_alf::unaryexpression_constructor_exists():
    assert callable(alf::UnaryExpression.__init__)


def test_alf::unaryexpression_constructor_args():
    sig = inspect.signature(alf::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf::unaryexpression_has_op():
    assert hasattr(alf::UnaryExpression, "op")
    descriptor = None
    for klass in alf::UnaryExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf::multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(alf::MultiplicativeExpression)


def test_alf::multiplicativeexpression_constructor_exists():
    assert callable(alf::MultiplicativeExpression.__init__)


def test_alf::multiplicativeexpression_constructor_args():
    sig = inspect.signature(alf::MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf::multiplicativeexpression_has_op():
    assert hasattr(alf::MultiplicativeExpression, "op")
    descriptor = None
    for klass in alf::MultiplicativeExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf::additiveexpression_is_not_abstract():
    assert not inspect.isabstract(alf::AdditiveExpression)


def test_alf::additiveexpression_constructor_exists():
    assert callable(alf::AdditiveExpression.__init__)


def test_alf::additiveexpression_constructor_args():
    sig = inspect.signature(alf::AdditiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf::additiveexpression_has_op():
    assert hasattr(alf::AdditiveExpression, "op")
    descriptor = None
    for klass in alf::AdditiveExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf::tupleelement_is_not_abstract():
    assert not inspect.isabstract(alf::TupleElement)


def test_alf::tupleelement_constructor_exists():
    assert callable(alf::TupleElement.__init__)


def test_alf::tupleelement_constructor_args():
    sig = inspect.signature(alf::TupleElement.__init__)
    params = list(sig.parameters.keys())



def test_alf::namedtemplatebinding_is_not_abstract():
    assert not inspect.isabstract(alf::NamedTemplateBinding)


def test_alf::namedtemplatebinding_constructor_exists():
    assert callable(alf::NamedTemplateBinding.__init__)


def test_alf::namedtemplatebinding_constructor_args():
    sig = inspect.signature(alf::NamedTemplateBinding.__init__)
    params = list(sig.parameters.keys())
    assert "formal" in params, "Missing parameter 'formal'"

def test_alf::namedtemplatebinding_has_formal():
    assert hasattr(alf::NamedTemplateBinding, "formal")
    descriptor = None
    for klass in alf::NamedTemplateBinding.__mro__:
        if "formal" in klass.__dict__:
            descriptor = klass.__dict__["formal"]
            break
    assert isinstance(descriptor, property)



def test_alf::classificationexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ClassificationExpression)


def test_alf::classificationexpression_constructor_exists():
    assert callable(alf::ClassificationExpression.__init__)


def test_alf::classificationexpression_constructor_args():
    sig = inspect.signature(alf::ClassificationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf::classificationexpression_has_op():
    assert hasattr(alf::ClassificationExpression, "op")
    descriptor = None
    for klass in alf::ClassificationExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(alf::EqualityExpression)


def test_alf::equalityexpression_constructor_exists():
    assert callable(alf::EqualityExpression.__init__)


def test_alf::equalityexpression_constructor_args():
    sig = inspect.signature(alf::EqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf::equalityexpression_has_op():
    assert hasattr(alf::EqualityExpression, "op")
    descriptor = None
    for klass in alf::EqualityExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf::andexpression_is_not_abstract():
    assert not inspect.isabstract(alf::AndExpression)


def test_alf::andexpression_constructor_exists():
    assert callable(alf::AndExpression.__init__)


def test_alf::andexpression_constructor_args():
    sig = inspect.signature(alf::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ExclusiveOrExpression)


def test_alf::exclusiveorexpression_constructor_exists():
    assert callable(alf::ExclusiveOrExpression.__init__)


def test_alf::exclusiveorexpression_constructor_args():
    sig = inspect.signature(alf::ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(alf::InclusiveOrExpression)


def test_alf::inclusiveorexpression_constructor_exists():
    assert callable(alf::InclusiveOrExpression.__init__)


def test_alf::inclusiveorexpression_constructor_args():
    sig = inspect.signature(alf::InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ConditionalAndExpression)


def test_alf::conditionalandexpression_constructor_exists():
    assert callable(alf::ConditionalAndExpression.__init__)


def test_alf::conditionalandexpression_constructor_args():
    sig = inspect.signature(alf::ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ConditionalOrExpression)


def test_alf::conditionalorexpression_constructor_exists():
    assert callable(alf::ConditionalOrExpression.__init__)


def test_alf::conditionalorexpression_constructor_args():
    sig = inspect.signature(alf::ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::instancecreationinvocationstatement_is_not_abstract():
    assert not inspect.isabstract(alf::InstanceCreationInvocationStatement)


def test_alf::instancecreationinvocationstatement_constructor_exists():
    assert callable(alf::InstanceCreationInvocationStatement.__init__)


def test_alf::instancecreationinvocationstatement_constructor_args():
    sig = inspect.signature(alf::InstanceCreationInvocationStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::thisinvocationstatement_is_not_abstract():
    assert not inspect.isabstract(alf::ThisInvocationStatement)


def test_alf::thisinvocationstatement_constructor_exists():
    assert callable(alf::ThisInvocationStatement.__init__)


def test_alf::thisinvocationstatement_constructor_args():
    sig = inspect.signature(alf::ThisInvocationStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::invocationorassignementordeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(alf::InvocationOrAssignementOrDeclarationStatement)


def test_alf::invocationorassignementordeclarationstatement_constructor_exists():
    assert callable(alf::InvocationOrAssignementOrDeclarationStatement.__init__)


def test_alf::invocationorassignementordeclarationstatement_constructor_args():
    sig = inspect.signature(alf::InvocationOrAssignementOrDeclarationStatement.__init__)
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



def test_alf::classifystatement_is_not_abstract():
    assert not inspect.isabstract(alf::ClassifyStatement)


def test_alf::classifystatement_constructor_exists():
    assert callable(alf::ClassifyStatement.__init__)


def test_alf::classifystatement_constructor_args():
    sig = inspect.signature(alf::ClassifyStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::superinvocationstatement_is_not_abstract():
    assert not inspect.isabstract(alf::SuperInvocationStatement)


def test_alf::superinvocationstatement_constructor_exists():
    assert callable(alf::SuperInvocationStatement.__init__)


def test_alf::superinvocationstatement_constructor_args():
    sig = inspect.signature(alf::SuperInvocationStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::variabledeclarationcompletion_is_not_abstract():
    assert not inspect.isabstract(alf::VariableDeclarationCompletion)


def test_alf::variabledeclarationcompletion_constructor_exists():
    assert callable(alf::VariableDeclarationCompletion.__init__)


def test_alf::variabledeclarationcompletion_constructor_args():
    sig = inspect.signature(alf::VariableDeclarationCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicityIndicator" in params, "Missing parameter 'multiplicityIndicator'"
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_alf::variabledeclarationcompletion_has_multiplicityIndicator():
    assert hasattr(alf::VariableDeclarationCompletion, "multiplicityIndicator")
    descriptor = None
    for klass in alf::VariableDeclarationCompletion.__mro__:
        if "multiplicityIndicator" in klass.__dict__:
            descriptor = klass.__dict__["multiplicityIndicator"]
            break
    assert isinstance(descriptor, property)

def test_alf::variabledeclarationcompletion_has_variableName():
    assert hasattr(alf::VariableDeclarationCompletion, "variableName")
    descriptor = None
    for klass in alf::VariableDeclarationCompletion.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



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



def test_alf::acceptclause_is_not_abstract():
    assert not inspect.isabstract(alf::AcceptClause)


def test_alf::acceptclause_constructor_exists():
    assert callable(alf::AcceptClause.__init__)


def test_alf::acceptclause_constructor_args():
    sig = inspect.signature(alf::AcceptClause.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_alf::acceptclause_has_name():
    assert hasattr(alf::AcceptClause, "name")
    descriptor = None
    for klass in alf::AcceptClause.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_alf::acceptstatement_is_not_abstract():
    assert not inspect.isabstract(alf::AcceptStatement)


def test_alf::acceptstatement_constructor_exists():
    assert callable(alf::AcceptStatement.__init__)


def test_alf::acceptstatement_constructor_args():
    sig = inspect.signature(alf::AcceptStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::returnstatement_is_not_abstract():
    assert not inspect.isabstract(alf::ReturnStatement)


def test_alf::returnstatement_constructor_exists():
    assert callable(alf::ReturnStatement.__init__)


def test_alf::returnstatement_constructor_args():
    sig = inspect.signature(alf::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::breakstatement_is_not_abstract():
    assert not inspect.isabstract(alf::BreakStatement)


def test_alf::breakstatement_constructor_exists():
    assert callable(alf::BreakStatement.__init__)


def test_alf::breakstatement_constructor_args():
    sig = inspect.signature(alf::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::loopvariabledefinition_is_not_abstract():
    assert not inspect.isabstract(alf::LoopVariableDefinition)


def test_alf::loopvariabledefinition_constructor_exists():
    assert callable(alf::LoopVariableDefinition.__init__)


def test_alf::loopvariabledefinition_constructor_args():
    sig = inspect.signature(alf::LoopVariableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_alf::loopvariabledefinition_has_name():
    assert hasattr(alf::LoopVariableDefinition, "name")
    descriptor = None
    for klass in alf::LoopVariableDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_alf::forcontrol_is_not_abstract():
    assert not inspect.isabstract(alf::ForControl)


def test_alf::forcontrol_constructor_exists():
    assert callable(alf::ForControl.__init__)


def test_alf::forcontrol_constructor_args():
    sig = inspect.signature(alf::ForControl.__init__)
    params = list(sig.parameters.keys())



def test_alf::forstatement_is_not_abstract():
    assert not inspect.isabstract(alf::ForStatement)


def test_alf::forstatement_constructor_exists():
    assert callable(alf::ForStatement.__init__)


def test_alf::forstatement_constructor_args():
    sig = inspect.signature(alf::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::acceptblock_is_not_abstract():
    assert not inspect.isabstract(alf::AcceptBlock)


def test_alf::acceptblock_constructor_exists():
    assert callable(alf::AcceptBlock.__init__)


def test_alf::acceptblock_constructor_args():
    sig = inspect.signature(alf::AcceptBlock.__init__)
    params = list(sig.parameters.keys())



def test_alf::whilestatement_is_not_abstract():
    assert not inspect.isabstract(alf::WhileStatement)


def test_alf::whilestatement_constructor_exists():
    assert callable(alf::WhileStatement.__init__)


def test_alf::whilestatement_constructor_args():
    sig = inspect.signature(alf::WhileStatement.__init__)
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



def test_alf::switchstatement_is_not_abstract():
    assert not inspect.isabstract(alf::SwitchStatement)


def test_alf::switchstatement_constructor_exists():
    assert callable(alf::SwitchStatement.__init__)


def test_alf::switchstatement_constructor_args():
    sig = inspect.signature(alf::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::dostatement_is_not_abstract():
    assert not inspect.isabstract(alf::DoStatement)


def test_alf::dostatement_constructor_exists():
    assert callable(alf::DoStatement.__init__)


def test_alf::dostatement_constructor_args():
    sig = inspect.signature(alf::DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::sequentialclauses_is_not_abstract():
    assert not inspect.isabstract(alf::SequentialClauses)


def test_alf::sequentialclauses_constructor_exists():
    assert callable(alf::SequentialClauses.__init__)


def test_alf::sequentialclauses_constructor_args():
    sig = inspect.signature(alf::SequentialClauses.__init__)
    params = list(sig.parameters.keys())



def test_alf::ifstatement_is_not_abstract():
    assert not inspect.isabstract(alf::IfStatement)


def test_alf::ifstatement_constructor_exists():
    assert callable(alf::IfStatement.__init__)


def test_alf::ifstatement_constructor_args():
    sig = inspect.signature(alf::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_alf::localnamedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(alf::LocalNameDeclarationStatement)


def test_alf::localnamedeclarationstatement_constructor_exists():
    assert callable(alf::LocalNameDeclarationStatement.__init__)


def test_alf::localnamedeclarationstatement_constructor_args():
    sig = inspect.signature(alf::LocalNameDeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"
    assert "multiplicityIndicator" in params, "Missing parameter 'multiplicityIndicator'"

def test_alf::localnamedeclarationstatement_has_varName():
    assert hasattr(alf::LocalNameDeclarationStatement, "varName")
    descriptor = None
    for klass in alf::LocalNameDeclarationStatement.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)

def test_alf::localnamedeclarationstatement_has_multiplicityIndicator():
    assert hasattr(alf::LocalNameDeclarationStatement, "multiplicityIndicator")
    descriptor = None
    for klass in alf::LocalNameDeclarationStatement.__mro__:
        if "multiplicityIndicator" in klass.__dict__:
            descriptor = klass.__dict__["multiplicityIndicator"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_alf::conditionaltestexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ConditionalTestExpression)


def test_alf::conditionaltestexpression_constructor_exists():
    assert callable(alf::ConditionalTestExpression.__init__)


def test_alf::conditionaltestexpression_constructor_args():
    sig = inspect.signature(alf::ConditionalTestExpression.__init__)
    params = list(sig.parameters.keys())



def test_sequenceelement_is_not_abstract():
    assert not inspect.isabstract(SequenceElement)


def test_sequenceelement_constructor_exists():
    assert callable(SequenceElement.__init__)


def test_sequenceelement_constructor_args():
    sig = inspect.signature(SequenceElement.__init__)
    params = list(sig.parameters.keys())



def test_alf::sequenceconstructionexpression_is_not_abstract():
    assert not inspect.isabstract(alf::SequenceConstructionExpression)


def test_alf::sequenceconstructionexpression_constructor_exists():
    assert callable(alf::SequenceConstructionExpression.__init__)


def test_alf::sequenceconstructionexpression_constructor_args():
    sig = inspect.signature(alf::SequenceConstructionExpression.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(LITERAL)


def test_literal_constructor_exists():
    assert callable(LITERAL.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf::boolean::literal_is_not_abstract():
    assert not inspect.isabstract(alf::BOOLEAN::LITERAL)


def test_alf::boolean::literal_constructor_exists():
    assert callable(alf::BOOLEAN::LITERAL.__init__)


def test_alf::boolean::literal_constructor_args():
    sig = inspect.signature(alf::BOOLEAN::LITERAL.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_alf::boolean::literal_has_value():
    assert hasattr(alf::BOOLEAN::LITERAL, "value")
    descriptor = None
    for klass in alf::BOOLEAN::LITERAL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_alf::suffixexpression_is_not_abstract():
    assert not inspect.isabstract(alf::SuffixExpression)


def test_alf::suffixexpression_constructor_exists():
    assert callable(alf::SuffixExpression.__init__)


def test_alf::suffixexpression_constructor_args():
    sig = inspect.signature(alf::SuffixExpression.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_alf::nullexpression_is_not_abstract():
    assert not inspect.isabstract(alf::NullExpression)


def test_alf::nullexpression_constructor_exists():
    assert callable(alf::NullExpression.__init__)


def test_alf::nullexpression_constructor_args():
    sig = inspect.signature(alf::NullExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::literal_is_not_abstract():
    assert not inspect.isabstract(alf::LITERAL)


def test_alf::literal_constructor_exists():
    assert callable(alf::LITERAL.__init__)


def test_alf::literal_constructor_args():
    sig = inspect.signature(alf::LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf::statement_is_not_abstract():
    assert not inspect.isabstract(alf::Statement)


def test_alf::statement_constructor_exists():
    assert callable(alf::Statement.__init__)


def test_alf::statement_constructor_args():
    sig = inspect.signature(alf::Statement.__init__)
    params = list(sig.parameters.keys())



def test_alf::assignmentcompletion_is_not_abstract():
    assert not inspect.isabstract(alf::AssignmentCompletion)


def test_alf::assignmentcompletion_constructor_exists():
    assert callable(alf::AssignmentCompletion.__init__)


def test_alf::assignmentcompletion_constructor_args():
    sig = inspect.signature(alf::AssignmentCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_alf::assignmentcompletion_has_op():
    assert hasattr(alf::AssignmentCompletion, "op")
    descriptor = None
    for klass in alf::AssignmentCompletion.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_alf::templatebinding_is_not_abstract():
    assert not inspect.isabstract(alf::TemplateBinding)


def test_alf::templatebinding_constructor_exists():
    assert callable(alf::TemplateBinding.__init__)


def test_alf::templatebinding_constructor_args():
    sig = inspect.signature(alf::TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_alf::unqualifiedname_is_not_abstract():
    assert not inspect.isabstract(alf::UnqualifiedName)


def test_alf::unqualifiedname_constructor_exists():
    assert callable(alf::UnqualifiedName.__init__)


def test_alf::unqualifiedname_constructor_args():
    sig = inspect.signature(alf::UnqualifiedName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_alf::unqualifiedname_has_name():
    assert hasattr(alf::UnqualifiedName, "name")
    descriptor = None
    for klass in alf::UnqualifiedName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_alf::sequenceconstructionoraccesscompletion_is_not_abstract():
    assert not inspect.isabstract(alf::SequenceConstructionOrAccessCompletion)


def test_alf::sequenceconstructionoraccesscompletion_constructor_exists():
    assert callable(alf::SequenceConstructionOrAccessCompletion.__init__)


def test_alf::sequenceconstructionoraccesscompletion_constructor_args():
    sig = inspect.signature(alf::SequenceConstructionOrAccessCompletion.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicityIndicator" in params, "Missing parameter 'multiplicityIndicator'"

def test_alf::sequenceconstructionoraccesscompletion_has_multiplicityIndicator():
    assert hasattr(alf::SequenceConstructionOrAccessCompletion, "multiplicityIndicator")
    descriptor = None
    for klass in alf::SequenceConstructionOrAccessCompletion.__mro__:
        if "multiplicityIndicator" in klass.__dict__:
            descriptor = klass.__dict__["multiplicityIndicator"]
            break
    assert isinstance(descriptor, property)



def test_alf::tuple_is_not_abstract():
    assert not inspect.isabstract(alf::Tuple)


def test_alf::tuple_constructor_exists():
    assert callable(alf::Tuple.__init__)


def test_alf::tuple_constructor_args():
    sig = inspect.signature(alf::Tuple.__init__)
    params = list(sig.parameters.keys())



def test_alf::qualifiednamepath_is_not_abstract():
    assert not inspect.isabstract(alf::QualifiedNamePath)


def test_alf::qualifiednamepath_constructor_exists():
    assert callable(alf::QualifiedNamePath.__init__)


def test_alf::qualifiednamepath_constructor_args():
    sig = inspect.signature(alf::QualifiedNamePath.__init__)
    params = list(sig.parameters.keys())



def test_nonliteralvaluespecification_is_not_abstract():
    assert not inspect.isabstract(NonLiteralValueSpecification)


def test_nonliteralvaluespecification_constructor_exists():
    assert callable(NonLiteralValueSpecification.__init__)


def test_nonliteralvaluespecification_constructor_args():
    sig = inspect.signature(NonLiteralValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_alf::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ParenthesizedExpression)


def test_alf::parenthesizedexpression_constructor_exists():
    assert callable(alf::ParenthesizedExpression.__init__)


def test_alf::parenthesizedexpression_constructor_args():
    sig = inspect.signature(alf::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::instancecreationexpression_is_not_abstract():
    assert not inspect.isabstract(alf::InstanceCreationExpression)


def test_alf::instancecreationexpression_constructor_exists():
    assert callable(alf::InstanceCreationExpression.__init__)


def test_alf::instancecreationexpression_constructor_args():
    sig = inspect.signature(alf::InstanceCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::superinvocationexpression_is_not_abstract():
    assert not inspect.isabstract(alf::SuperInvocationExpression)


def test_alf::superinvocationexpression_constructor_exists():
    assert callable(alf::SuperInvocationExpression.__init__)


def test_alf::superinvocationexpression_constructor_args():
    sig = inspect.signature(alf::SuperInvocationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"

def test_alf::superinvocationexpression_has_className():
    assert hasattr(alf::SuperInvocationExpression, "className")
    descriptor = None
    for klass in alf::SuperInvocationExpression.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_alf::thisexpression_is_not_abstract():
    assert not inspect.isabstract(alf::ThisExpression)


def test_alf::thisexpression_constructor_exists():
    assert callable(alf::ThisExpression.__init__)


def test_alf::thisexpression_constructor_args():
    sig = inspect.signature(alf::ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_alf::nameexpression_is_not_abstract():
    assert not inspect.isabstract(alf::NameExpression)


def test_alf::nameexpression_constructor_exists():
    assert callable(alf::NameExpression.__init__)


def test_alf::nameexpression_constructor_args():
    sig = inspect.signature(alf::NameExpression.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "prefixOp" in params, "Missing parameter 'prefixOp'"
    assert "postfixOp" in params, "Missing parameter 'postfixOp'"

def test_alf::nameexpression_has_id():
    assert hasattr(alf::NameExpression, "id")
    descriptor = None
    for klass in alf::NameExpression.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_alf::nameexpression_has_prefixOp():
    assert hasattr(alf::NameExpression, "prefixOp")
    descriptor = None
    for klass in alf::NameExpression.__mro__:
        if "prefixOp" in klass.__dict__:
            descriptor = klass.__dict__["prefixOp"]
            break
    assert isinstance(descriptor, property)

def test_alf::nameexpression_has_postfixOp():
    assert hasattr(alf::NameExpression, "postfixOp")
    descriptor = None
    for klass in alf::NameExpression.__mro__:
        if "postfixOp" in klass.__dict__:
            descriptor = klass.__dict__["postfixOp"]
            break
    assert isinstance(descriptor, property)



def test_alf::string::literal_is_not_abstract():
    assert not inspect.isabstract(alf::STRING::LITERAL)


def test_alf::string::literal_constructor_exists():
    assert callable(alf::STRING::LITERAL.__init__)


def test_alf::string::literal_constructor_args():
    sig = inspect.signature(alf::STRING::LITERAL.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_alf::string::literal_has_value():
    assert hasattr(alf::STRING::LITERAL, "value")
    descriptor = None
    for klass in alf::STRING::LITERAL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_number::literal_is_not_abstract():
    assert not inspect.isabstract(NUMBER::LITERAL)


def test_number::literal_constructor_exists():
    assert callable(NUMBER::LITERAL.__init__)


def test_number::literal_constructor_args():
    sig = inspect.signature(NUMBER::LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf::unlimited::literal_is_not_abstract():
    assert not inspect.isabstract(alf::UNLIMITED::LITERAL)


def test_alf::unlimited::literal_constructor_exists():
    assert callable(alf::UNLIMITED::LITERAL.__init__)


def test_alf::unlimited::literal_constructor_args():
    sig = inspect.signature(alf::UNLIMITED::LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf::integer::literal_is_not_abstract():
    assert not inspect.isabstract(alf::INTEGER::LITERAL)


def test_alf::integer::literal_constructor_exists():
    assert callable(alf::INTEGER::LITERAL.__init__)


def test_alf::integer::literal_constructor_args():
    sig = inspect.signature(alf::INTEGER::LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_alf::number::literal_is_not_abstract():
    assert not inspect.isabstract(alf::NUMBER::LITERAL)


def test_alf::number::literal_constructor_exists():
    assert callable(alf::NUMBER::LITERAL.__init__)


def test_alf::number::literal_constructor_args():
    sig = inspect.signature(alf::NUMBER::LITERAL.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_alf::number::literal_has_value():
    assert hasattr(alf::NUMBER::LITERAL, "value")
    descriptor = None
    for klass in alf::NUMBER::LITERAL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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
    assert "nonUnique" in params, "Missing parameter 'nonUnique'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "sequence" in params, "Missing parameter 'sequence'"

def test_alf::multiplicity_has_nonUnique():
    assert hasattr(alf::Multiplicity, "nonUnique")
    descriptor = None
    for klass in alf::Multiplicity.__mro__:
        if "nonUnique" in klass.__dict__:
            descriptor = klass.__dict__["nonUnique"]
            break
    assert isinstance(descriptor, property)

def test_alf::multiplicity_has_ordered():
    assert hasattr(alf::Multiplicity, "ordered")
    descriptor = None
    for klass in alf::Multiplicity.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_alf::multiplicity_has_sequence():
    assert hasattr(alf::Multiplicity, "sequence")
    descriptor = None
    for klass in alf::Multiplicity.__mro__:
        if "sequence" in klass.__dict__:
            descriptor = klass.__dict__["sequence"]
            break
    assert isinstance(descriptor, property)



def test_alf::expression_is_not_abstract():
    assert not inspect.isabstract(alf::Expression)


def test_alf::expression_constructor_exists():
    assert callable(alf::Expression.__init__)


def test_alf::expression_constructor_args():
    sig = inspect.signature(alf::Expression.__init__)
    params = list(sig.parameters.keys())



def test_alf::test_is_not_abstract():
    assert not inspect.isabstract(alf::Test)


def test_alf::test_constructor_exists():
    assert callable(alf::Test.__init__)


def test_alf::test_constructor_args():
    sig = inspect.signature(alf::Test.__init__)
    params = list(sig.parameters.keys())



def test_alf::qualifiednamelist_is_not_abstract():
    assert not inspect.isabstract(alf::QualifiedNameList)


def test_alf::qualifiednamelist_constructor_exists():
    assert callable(alf::QualifiedNameList.__init__)


def test_alf::qualifiednamelist_constructor_args():
    sig = inspect.signature(alf::QualifiedNameList.__init__)
    params = list(sig.parameters.keys())



def test_alf::qualifiednamewithbinding_is_not_abstract():
    assert not inspect.isabstract(alf::QualifiedNameWithBinding)


def test_alf::qualifiednamewithbinding_constructor_exists():
    assert callable(alf::QualifiedNameWithBinding.__init__)


def test_alf::qualifiednamewithbinding_constructor_args():
    sig = inspect.signature(alf::QualifiedNameWithBinding.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_alf::qualifiednamewithbinding_has_id():
    assert hasattr(alf::QualifiedNameWithBinding, "id")
    descriptor = None
    for klass in alf::QualifiedNameWithBinding.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_number::literal::without::suffix_is_not_abstract():
    assert not inspect.isabstract(NUMBER::LITERAL::WITHOUT::SUFFIX)


def test_number::literal::without::suffix_constructor_exists():
    assert callable(NUMBER::LITERAL::WITHOUT::SUFFIX.__init__)


def test_number::literal::without::suffix_constructor_args():
    sig = inspect.signature(NUMBER::LITERAL::WITHOUT::SUFFIX.__init__)
    params = list(sig.parameters.keys())



def test_alf::unlimited::literal::without::suffix_is_not_abstract():
    assert not inspect.isabstract(alf::UNLIMITED::LITERAL::WITHOUT::SUFFIX)


def test_alf::unlimited::literal::without::suffix_constructor_exists():
    assert callable(alf::UNLIMITED::LITERAL::WITHOUT::SUFFIX.__init__)


def test_alf::unlimited::literal::without::suffix_constructor_args():
    sig = inspect.signature(alf::UNLIMITED::LITERAL::WITHOUT::SUFFIX.__init__)
    params = list(sig.parameters.keys())



def test_alf::integer::literal::without::suffix_is_not_abstract():
    assert not inspect.isabstract(alf::INTEGER::LITERAL::WITHOUT::SUFFIX)


def test_alf::integer::literal::without::suffix_constructor_exists():
    assert callable(alf::INTEGER::LITERAL::WITHOUT::SUFFIX.__init__)


def test_alf::integer::literal::without::suffix_constructor_args():
    sig = inspect.signature(alf::INTEGER::LITERAL::WITHOUT::SUFFIX.__init__)
    params = list(sig.parameters.keys())



def test_alf::number::literal::without::suffix_is_not_abstract():
    assert not inspect.isabstract(alf::NUMBER::LITERAL::WITHOUT::SUFFIX)


def test_alf::number::literal::without::suffix_constructor_exists():
    assert callable(alf::NUMBER::LITERAL::WITHOUT::SUFFIX.__init__)


def test_alf::number::literal::without::suffix_constructor_args():
    sig = inspect.signature(alf::NUMBER::LITERAL::WITHOUT::SUFFIX.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_alf::number::literal::without::suffix_has_value():
    assert hasattr(alf::NUMBER::LITERAL::WITHOUT::SUFFIX, "value")
    descriptor = None
    for klass in alf::NUMBER::LITERAL::WITHOUT::SUFFIX.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_alf::formalparameters_is_not_abstract():
    assert not inspect.isabstract(alf::FormalParameters)


def test_alf::formalparameters_constructor_exists():
    assert callable(alf::FormalParameters.__init__)


def test_alf::formalparameters_constructor_args():
    sig = inspect.signature(alf::FormalParameters.__init__)
    params = list(sig.parameters.keys())



def test_alf::block_is_not_abstract():
    assert not inspect.isabstract(alf::Block)


def test_alf::block_constructor_exists():
    assert callable(alf::Block.__init__)


def test_alf::block_constructor_args():
    sig = inspect.signature(alf::Block.__init__)
    params = list(sig.parameters.keys())



def test_alf::operationdeclaration_is_not_abstract():
    assert not inspect.isabstract(alf::OperationDeclaration)


def test_alf::operationdeclaration_constructor_exists():
    assert callable(alf::OperationDeclaration.__init__)


def test_alf::operationdeclaration_constructor_args():
    sig = inspect.signature(alf::OperationDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_alf::operationdeclaration_has_name():
    assert hasattr(alf::OperationDeclaration, "name")
    descriptor = None
    for klass in alf::OperationDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_alf::typename_is_not_abstract():
    assert not inspect.isabstract(alf::TypeName)


def test_alf::typename_constructor_exists():
    assert callable(alf::TypeName.__init__)


def test_alf::typename_constructor_args():
    sig = inspect.signature(alf::TypeName.__init__)
    params = list(sig.parameters.keys())



def test_alf::formalparameter_is_not_abstract():
    assert not inspect.isabstract(alf::FormalParameter)


def test_alf::formalparameter_constructor_exists():
    assert callable(alf::FormalParameter.__init__)


def test_alf::formalparameter_constructor_args():
    sig = inspect.signature(alf::FormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "name" in params, "Missing parameter 'name'"

def test_alf::formalparameter_has_direction():
    assert hasattr(alf::FormalParameter, "direction")
    descriptor = None
    for klass in alf::FormalParameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_alf::formalparameter_has_name():
    assert hasattr(alf::FormalParameter, "name")
    descriptor = None
    for klass in alf::FormalParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_alf::formalparameterlist_is_not_abstract():
    assert not inspect.isabstract(alf::FormalParameterList)


def test_alf::formalparameterlist_constructor_exists():
    assert callable(alf::FormalParameterList.__init__)


def test_alf::formalparameterlist_constructor_args():
    sig = inspect.signature(alf::FormalParameterList.__init__)
    params = list(sig.parameters.keys())



def test_alf::redefinitionclause_is_not_abstract():
    assert not inspect.isabstract(alf::RedefinitionClause)


def test_alf::redefinitionclause_constructor_exists():
    assert callable(alf::RedefinitionClause.__init__)


def test_alf::redefinitionclause_constructor_args():
    sig = inspect.signature(alf::RedefinitionClause.__init__)
    params = list(sig.parameters.keys())



def test_alf::operationdefinitionorstub_is_not_abstract():
    assert not inspect.isabstract(alf::OperationDefinitionOrStub)


def test_alf::operationdefinitionorstub_constructor_exists():
    assert callable(alf::OperationDefinitionOrStub.__init__)


def test_alf::operationdefinitionorstub_constructor_args():
    sig = inspect.signature(alf::OperationDefinitionOrStub.__init__)
    params = list(sig.parameters.keys())



def test_alf::typepart_is_not_abstract():
    assert not inspect.isabstract(alf::TypePart)


def test_alf::typepart_constructor_exists():
    assert callable(alf::TypePart.__init__)


def test_alf::typepart_constructor_args():
    sig = inspect.signature(alf::TypePart.__init__)
    params = list(sig.parameters.keys())



def test_alf::operations_is_not_abstract():
    assert not inspect.isabstract(alf::Operations)


def test_alf::operations_constructor_exists():
    assert callable(alf::Operations.__init__)


def test_alf::operations_constructor_args():
    sig = inspect.signature(alf::Operations.__init__)
    params = list(sig.parameters.keys())
    assert "imports" in params, "Missing parameter 'imports'"

def test_alf::operations_has_imports():
    assert hasattr(alf::Operations, "imports")
    descriptor = None
    for klass in alf::Operations.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)

def test_linkoperationkind_exists():
    # Check that the Enumeration exists
    assert LinkOperationKind is not None

def test_linkoperationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkOperationKind]
    expected_literals = [
        "CREATE",
        "CLEAR",
        "DESTROY",
        "DESTROY_OBJECT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkOperationKind"

def test_selectorrejectoperator_exists():
    # Check that the Enumeration exists
    assert SelectOrRejectOperator is not None

def test_selectorrejectoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SelectOrRejectOperator]
    expected_literals = [
        "REJECT",
        "SELECT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SelectOrRejectOperator"

def test_parameterdirection_exists():
    # Check that the Enumeration exists
    assert ParameterDirection is not None

def test_parameterdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirection]
    expected_literals = [
        "OUT",
        "IN",
        "INOUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirection"

def test_annotationkind_exists():
    # Check that the Enumeration exists
    assert AnnotationKind is not None

def test_annotationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnnotationKind]
    expected_literals = [
        "ASSURED",
        "ISOLATED",
        "PARALLEL",
        "DETERMINED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnnotationKind"

def test_forallorexistsoroneoperator_exists():
    # Check that the Enumeration exists
    assert ForAllOrExistsOrOneOperator is not None

def test_forallorexistsoroneoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ForAllOrExistsOrOneOperator]
    expected_literals = [
        "EXISTS",
        "ONE",
        "FORALL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ForAllOrExistsOrOneOperator"

def test_booleanvalue_exists():
    # Check that the Enumeration exists
    assert BooleanValue is not None

def test_booleanvalue_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanValue]
    expected_literals = [
        "TRUE",
        "FALSE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanValue"

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "MODASSIGN",
        "MULTASSIGN",
        "URSHIFTASSIGN",
        "XORASSIGN",
        "ORASSIGN",
        "ASSIGN",
        "DIVASSIGN",
        "RSHIFTASSIGN",
        "ANDASSIGN",
        "PLUSASSIGN",
        "MINUSASSIGN",
        "LSHIFTASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_collectoriterateoperator_exists():
    # Check that the Enumeration exists
    assert CollectOrIterateOperator is not None

def test_collectoriterateoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectOrIterateOperator]
    expected_literals = [
        "ITERATE",
        "COLLECT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectOrIterateOperator"


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
alf::Annotation_strategy = st.builds(
    alf::Annotation,
    args=
        safe_text,
    kind=
        safe_text
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
alf::DocumentedStatement_strategy = st.builds(
    alf::DocumentedStatement,
    comment=
        safe_text
)
alf::StatementSequence_strategy = st.builds(
    alf::StatementSequence,
)
alf::ClassExtentExpression_strategy = st.builds(
    alf::ClassExtentExpression,
)
alf::SequenceElement_strategy = st.builds(
    alf::SequenceElement,
)
Statement_strategy = st.builds(
    Statement,
)
alf::EmptyStatement_strategy = st.builds(
    alf::EmptyStatement,
)
alf::InlineStatement_strategy = st.builds(
    alf::InlineStatement,
    body=
        safe_text,
    langageName=
        safe_text
)
alf::BlockStatement_strategy = st.builds(
    alf::BlockStatement,
)
alf::AnnotatedStatement_strategy = st.builds(
    alf::AnnotatedStatement,
)
alf::AccessCompletion_strategy = st.builds(
    alf::AccessCompletion,
)
alf::NonLiteralValueSpecification_strategy = st.builds(
    alf::NonLiteralValueSpecification,
)
alf::SequenceConstructionCompletion_strategy = st.builds(
    alf::SequenceConstructionCompletion,
    multiplicityIndicator=
        st.booleans()
)
alf::PartialSequenceConstructionCompletion_strategy = st.builds(
    alf::PartialSequenceConstructionCompletion,
)
SequenceExpansionExpression_strategy = st.builds(
    SequenceExpansionExpression,
)
alf::SelectOrRejectOperation_strategy = st.builds(
    alf::SelectOrRejectOperation,
    expr1=
        safe_text,
    expr3=
        safe_text,
    expr2=
        safe_text,
    op=
        safe_text,
    expr4=
        safe_text
)
alf::IsUniqueOperation_strategy = st.builds(
    alf::IsUniqueOperation,
    name=
        safe_text
)
alf::ForAllOrExistsOrOneOperation_strategy = st.builds(
    alf::ForAllOrExistsOrOneOperation,
    expr2=
        safe_text,
    op=
        safe_text,
    expr1=
        safe_text,
    expr4=
        safe_text,
    expr3=
        safe_text
)
alf::CollectOrIterateOperation_strategy = st.builds(
    alf::CollectOrIterateOperation,
    op=
        safe_text,
    expr3=
        safe_text,
    expr4=
        safe_text,
    expr1=
        safe_text,
    expr2=
        safe_text
)
alf::LinkOperationTupleElement_strategy = st.builds(
    alf::LinkOperationTupleElement,
    objectOrRole=
        safe_text
)
alf::LinkOperationTuple_strategy = st.builds(
    alf::LinkOperationTuple,
)
alf::ShiftExpression_strategy = st.builds(
    alf::ShiftExpression,
    op=
        safe_text
)
alf::RelationalExpression_strategy = st.builds(
    alf::RelationalExpression,
    op=
        safe_text
)
alf::OperationCallExpressionWithoutDot_strategy = st.builds(
    alf::OperationCallExpressionWithoutDot,
    operationName=
        safe_text
)
SuffixExpression_strategy = st.builds(
    SuffixExpression,
)
alf::PropertyCallExpression_strategy = st.builds(
    alf::PropertyCallExpression,
    propertyName=
        safe_text
)
alf::SequenceReductionExpression_strategy = st.builds(
    alf::SequenceReductionExpression,
    isOrdered=
        st.booleans()
)
alf::SequenceExpansionExpression_strategy = st.builds(
    alf::SequenceExpansionExpression,
)
alf::LinkOperationExpression_strategy = st.builds(
    alf::LinkOperationExpression,
    kind=
        safe_text
)
alf::SequenceOperationExpression_strategy = st.builds(
    alf::SequenceOperationExpression,
    operationName=
        safe_text
)
alf::OperationCallExpression_strategy = st.builds(
    alf::OperationCallExpression,
    operationName=
        safe_text
)
alf::ValueSpecification_strategy = st.builds(
    alf::ValueSpecification,
)
alf::PrimaryExpression_strategy = st.builds(
    alf::PrimaryExpression,
)
alf::UnaryExpression_strategy = st.builds(
    alf::UnaryExpression,
    op=
        safe_text
)
alf::MultiplicativeExpression_strategy = st.builds(
    alf::MultiplicativeExpression,
    op=
        safe_text
)
alf::AdditiveExpression_strategy = st.builds(
    alf::AdditiveExpression,
    op=
        safe_text
)
alf::TupleElement_strategy = st.builds(
    alf::TupleElement,
)
alf::NamedTemplateBinding_strategy = st.builds(
    alf::NamedTemplateBinding,
    formal=
        safe_text
)
alf::ClassificationExpression_strategy = st.builds(
    alf::ClassificationExpression,
    op=
        safe_text
)
alf::EqualityExpression_strategy = st.builds(
    alf::EqualityExpression,
    op=
        safe_text
)
alf::AndExpression_strategy = st.builds(
    alf::AndExpression,
)
alf::ExclusiveOrExpression_strategy = st.builds(
    alf::ExclusiveOrExpression,
)
alf::InclusiveOrExpression_strategy = st.builds(
    alf::InclusiveOrExpression,
)
alf::ConditionalAndExpression_strategy = st.builds(
    alf::ConditionalAndExpression,
)
alf::ConditionalOrExpression_strategy = st.builds(
    alf::ConditionalOrExpression,
)
alf::InstanceCreationInvocationStatement_strategy = st.builds(
    alf::InstanceCreationInvocationStatement,
)
alf::ThisInvocationStatement_strategy = st.builds(
    alf::ThisInvocationStatement,
)
alf::InvocationOrAssignementOrDeclarationStatement_strategy = st.builds(
    alf::InvocationOrAssignementOrDeclarationStatement,
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
alf::ClassifyStatement_strategy = st.builds(
    alf::ClassifyStatement,
)
alf::SuperInvocationStatement_strategy = st.builds(
    alf::SuperInvocationStatement,
)
alf::VariableDeclarationCompletion_strategy = st.builds(
    alf::VariableDeclarationCompletion,
    multiplicityIndicator=
        st.booleans(),
    variableName=
        safe_text
)
alf::CompoundAcceptStatementCompletion_strategy = st.builds(
    alf::CompoundAcceptStatementCompletion,
)
alf::SimpleAcceptStatementCompletion_strategy = st.builds(
    alf::SimpleAcceptStatementCompletion,
)
alf::AcceptClause_strategy = st.builds(
    alf::AcceptClause,
    name=
        safe_text
)
alf::AcceptStatement_strategy = st.builds(
    alf::AcceptStatement,
)
alf::ReturnStatement_strategy = st.builds(
    alf::ReturnStatement,
)
alf::BreakStatement_strategy = st.builds(
    alf::BreakStatement,
)
alf::LoopVariableDefinition_strategy = st.builds(
    alf::LoopVariableDefinition,
    name=
        safe_text
)
alf::ForControl_strategy = st.builds(
    alf::ForControl,
)
alf::ForStatement_strategy = st.builds(
    alf::ForStatement,
)
alf::AcceptBlock_strategy = st.builds(
    alf::AcceptBlock,
)
alf::WhileStatement_strategy = st.builds(
    alf::WhileStatement,
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
alf::SwitchStatement_strategy = st.builds(
    alf::SwitchStatement,
)
alf::DoStatement_strategy = st.builds(
    alf::DoStatement,
)
alf::SequentialClauses_strategy = st.builds(
    alf::SequentialClauses,
)
alf::IfStatement_strategy = st.builds(
    alf::IfStatement,
)
alf::LocalNameDeclarationStatement_strategy = st.builds(
    alf::LocalNameDeclarationStatement,
    varName=
        safe_text,
    multiplicityIndicator=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
alf::ConditionalTestExpression_strategy = st.builds(
    alf::ConditionalTestExpression,
)
SequenceElement_strategy = st.builds(
    SequenceElement,
)
alf::SequenceConstructionExpression_strategy = st.builds(
    alf::SequenceConstructionExpression,
)
LITERAL_strategy = st.builds(
    LITERAL,
)
alf::BOOLEAN::LITERAL_strategy = st.builds(
    alf::BOOLEAN::LITERAL,
    value=
        safe_text
)
alf::SuffixExpression_strategy = st.builds(
    alf::SuffixExpression,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
alf::NullExpression_strategy = st.builds(
    alf::NullExpression,
)
alf::LITERAL_strategy = st.builds(
    alf::LITERAL,
)
alf::Statement_strategy = st.builds(
    alf::Statement,
)
alf::AssignmentCompletion_strategy = st.builds(
    alf::AssignmentCompletion,
    op=
        safe_text
)
alf::TemplateBinding_strategy = st.builds(
    alf::TemplateBinding,
)
alf::UnqualifiedName_strategy = st.builds(
    alf::UnqualifiedName,
    name=
        safe_text
)
alf::SequenceConstructionOrAccessCompletion_strategy = st.builds(
    alf::SequenceConstructionOrAccessCompletion,
    multiplicityIndicator=
        st.booleans()
)
alf::Tuple_strategy = st.builds(
    alf::Tuple,
)
alf::QualifiedNamePath_strategy = st.builds(
    alf::QualifiedNamePath,
)
NonLiteralValueSpecification_strategy = st.builds(
    NonLiteralValueSpecification,
)
alf::ParenthesizedExpression_strategy = st.builds(
    alf::ParenthesizedExpression,
)
alf::InstanceCreationExpression_strategy = st.builds(
    alf::InstanceCreationExpression,
)
alf::SuperInvocationExpression_strategy = st.builds(
    alf::SuperInvocationExpression,
    className=
        safe_text
)
alf::ThisExpression_strategy = st.builds(
    alf::ThisExpression,
)
alf::NameExpression_strategy = st.builds(
    alf::NameExpression,
    id=
        safe_text,
    prefixOp=
        safe_text,
    postfixOp=
        safe_text
)
alf::STRING::LITERAL_strategy = st.builds(
    alf::STRING::LITERAL,
    value=
        safe_text
)
NUMBER::LITERAL_strategy = st.builds(
    NUMBER::LITERAL,
)
alf::UNLIMITED::LITERAL_strategy = st.builds(
    alf::UNLIMITED::LITERAL,
)
alf::INTEGER::LITERAL_strategy = st.builds(
    alf::INTEGER::LITERAL,
)
alf::NUMBER::LITERAL_strategy = st.builds(
    alf::NUMBER::LITERAL,
    value=
        safe_text
)
alf::MultiplicityRange_strategy = st.builds(
    alf::MultiplicityRange,
)
alf::Multiplicity_strategy = st.builds(
    alf::Multiplicity,
    nonUnique=
        st.booleans(),
    ordered=
        st.booleans(),
    sequence=
        st.booleans()
)
alf::Expression_strategy = st.builds(
    alf::Expression,
)
alf::Test_strategy = st.builds(
    alf::Test,
)
alf::QualifiedNameList_strategy = st.builds(
    alf::QualifiedNameList,
)
alf::QualifiedNameWithBinding_strategy = st.builds(
    alf::QualifiedNameWithBinding,
    id=
        safe_text
)
NUMBER::LITERAL::WITHOUT::SUFFIX_strategy = st.builds(
    NUMBER::LITERAL::WITHOUT::SUFFIX,
)
alf::UNLIMITED::LITERAL::WITHOUT::SUFFIX_strategy = st.builds(
    alf::UNLIMITED::LITERAL::WITHOUT::SUFFIX,
)
alf::INTEGER::LITERAL::WITHOUT::SUFFIX_strategy = st.builds(
    alf::INTEGER::LITERAL::WITHOUT::SUFFIX,
)
alf::NUMBER::LITERAL::WITHOUT::SUFFIX_strategy = st.builds(
    alf::NUMBER::LITERAL::WITHOUT::SUFFIX,
    value=
        safe_text
)
alf::FormalParameters_strategy = st.builds(
    alf::FormalParameters,
)
alf::Block_strategy = st.builds(
    alf::Block,
)
alf::OperationDeclaration_strategy = st.builds(
    alf::OperationDeclaration,
    name=
        safe_text
)
alf::TypeName_strategy = st.builds(
    alf::TypeName,
)
alf::FormalParameter_strategy = st.builds(
    alf::FormalParameter,
    direction=
        safe_text,
    name=
        safe_text
)
alf::FormalParameterList_strategy = st.builds(
    alf::FormalParameterList,
)
alf::RedefinitionClause_strategy = st.builds(
    alf::RedefinitionClause,
)
alf::OperationDefinitionOrStub_strategy = st.builds(
    alf::OperationDefinitionOrStub,
)
alf::TypePart_strategy = st.builds(
    alf::TypePart,
)
alf::Operations_strategy = st.builds(
    alf::Operations,
    imports=
        safe_text
)

@given(instance=alf::Annotation_strategy)
@settings(max_examples=50)
def test_alf::annotation_instantiation(instance):
    assert isinstance(instance, alf::Annotation)

@given(instance=alf::Annotation_strategy)
def test_alf::annotation_args_type(instance):
    assert isinstance(instance.args, str)


@given(instance=alf::Annotation_strategy)
def test_alf::annotation_args_setter(instance):
    original = instance.args
    instance.args = original
    assert instance.args == original

@given(instance=alf::Annotation_strategy)
def test_alf::annotation_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=alf::Annotation_strategy)
def test_alf::annotation_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

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

@given(instance=alf::ClassExtentExpression_strategy)
@settings(max_examples=50)
def test_alf::classextentexpression_instantiation(instance):
    assert isinstance(instance, alf::ClassExtentExpression)

@given(instance=alf::SequenceElement_strategy)
@settings(max_examples=50)
def test_alf::sequenceelement_instantiation(instance):
    assert isinstance(instance, alf::SequenceElement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=alf::EmptyStatement_strategy)
@settings(max_examples=50)
def test_alf::emptystatement_instantiation(instance):
    assert isinstance(instance, alf::EmptyStatement)

@given(instance=alf::InlineStatement_strategy)
@settings(max_examples=50)
def test_alf::inlinestatement_instantiation(instance):
    assert isinstance(instance, alf::InlineStatement)

@given(instance=alf::InlineStatement_strategy)
def test_alf::inlinestatement_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=alf::InlineStatement_strategy)
def test_alf::inlinestatement_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=alf::InlineStatement_strategy)
def test_alf::inlinestatement_langageName_type(instance):
    assert isinstance(instance.langageName, str)


@given(instance=alf::InlineStatement_strategy)
def test_alf::inlinestatement_langageName_setter(instance):
    original = instance.langageName
    instance.langageName = original
    assert instance.langageName == original

@given(instance=alf::BlockStatement_strategy)
@settings(max_examples=50)
def test_alf::blockstatement_instantiation(instance):
    assert isinstance(instance, alf::BlockStatement)

@given(instance=alf::AnnotatedStatement_strategy)
@settings(max_examples=50)
def test_alf::annotatedstatement_instantiation(instance):
    assert isinstance(instance, alf::AnnotatedStatement)

@given(instance=alf::AccessCompletion_strategy)
@settings(max_examples=50)
def test_alf::accesscompletion_instantiation(instance):
    assert isinstance(instance, alf::AccessCompletion)

@given(instance=alf::NonLiteralValueSpecification_strategy)
@settings(max_examples=50)
def test_alf::nonliteralvaluespecification_instantiation(instance):
    assert isinstance(instance, alf::NonLiteralValueSpecification)

@given(instance=alf::SequenceConstructionCompletion_strategy)
@settings(max_examples=50)
def test_alf::sequenceconstructioncompletion_instantiation(instance):
    assert isinstance(instance, alf::SequenceConstructionCompletion)

@given(instance=alf::SequenceConstructionCompletion_strategy)
def test_alf::sequenceconstructioncompletion_multiplicityIndicator_type(instance):
    assert isinstance(instance.multiplicityIndicator, bool)


@given(instance=alf::SequenceConstructionCompletion_strategy)
def test_alf::sequenceconstructioncompletion_multiplicityIndicator_setter(instance):
    original = instance.multiplicityIndicator
    instance.multiplicityIndicator = original
    assert instance.multiplicityIndicator == original

@given(instance=alf::PartialSequenceConstructionCompletion_strategy)
@settings(max_examples=50)
def test_alf::partialsequenceconstructioncompletion_instantiation(instance):
    assert isinstance(instance, alf::PartialSequenceConstructionCompletion)

@given(instance=SequenceExpansionExpression_strategy)
@settings(max_examples=50)
def test_sequenceexpansionexpression_instantiation(instance):
    assert isinstance(instance, SequenceExpansionExpression)

@given(instance=alf::SelectOrRejectOperation_strategy)
@settings(max_examples=50)
def test_alf::selectorrejectoperation_instantiation(instance):
    assert isinstance(instance, alf::SelectOrRejectOperation)

@given(instance=alf::SelectOrRejectOperation_strategy)
def test_alf::selectorrejectoperation_expr1_type(instance):
    assert isinstance(instance.expr1, str)


@given(instance=alf::SelectOrRejectOperation_strategy)
def test_alf::selectorrejectoperation_expr1_setter(instance):
    original = instance.expr1
    instance.expr1 = original
    assert instance.expr1 == original

@given(instance=alf::SelectOrRejectOperation_strategy)
def test_alf::selectorrejectoperation_expr3_type(instance):
    assert isinstance(instance.expr3, str)


@given(instance=alf::SelectOrRejectOperation_strategy)
def test_alf::selectorrejectoperation_expr3_setter(instance):
    original = instance.expr3
    instance.expr3 = original
    assert instance.expr3 == original

@given(instance=alf::SelectOrRejectOperation_strategy)
def test_alf::selectorrejectoperation_expr2_type(instance):
    assert isinstance(instance.expr2, str)


@given(instance=alf::SelectOrRejectOperation_strategy)
def test_alf::selectorrejectoperation_expr2_setter(instance):
    original = instance.expr2
    instance.expr2 = original
    assert instance.expr2 == original

@given(instance=alf::SelectOrRejectOperation_strategy)
def test_alf::selectorrejectoperation_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=alf::SelectOrRejectOperation_strategy)
def test_alf::selectorrejectoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf::SelectOrRejectOperation_strategy)
def test_alf::selectorrejectoperation_expr4_type(instance):
    assert isinstance(instance.expr4, str)


@given(instance=alf::SelectOrRejectOperation_strategy)
def test_alf::selectorrejectoperation_expr4_setter(instance):
    original = instance.expr4
    instance.expr4 = original
    assert instance.expr4 == original

@given(instance=alf::IsUniqueOperation_strategy)
@settings(max_examples=50)
def test_alf::isuniqueoperation_instantiation(instance):
    assert isinstance(instance, alf::IsUniqueOperation)

@given(instance=alf::IsUniqueOperation_strategy)
def test_alf::isuniqueoperation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=alf::IsUniqueOperation_strategy)
def test_alf::isuniqueoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=alf::ForAllOrExistsOrOneOperation_strategy)
@settings(max_examples=50)
def test_alf::forallorexistsoroneoperation_instantiation(instance):
    assert isinstance(instance, alf::ForAllOrExistsOrOneOperation)

@given(instance=alf::ForAllOrExistsOrOneOperation_strategy)
def test_alf::forallorexistsoroneoperation_expr2_type(instance):
    assert isinstance(instance.expr2, str)


@given(instance=alf::ForAllOrExistsOrOneOperation_strategy)
def test_alf::forallorexistsoroneoperation_expr2_setter(instance):
    original = instance.expr2
    instance.expr2 = original
    assert instance.expr2 == original

@given(instance=alf::ForAllOrExistsOrOneOperation_strategy)
def test_alf::forallorexistsoroneoperation_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=alf::ForAllOrExistsOrOneOperation_strategy)
def test_alf::forallorexistsoroneoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf::ForAllOrExistsOrOneOperation_strategy)
def test_alf::forallorexistsoroneoperation_expr1_type(instance):
    assert isinstance(instance.expr1, str)


@given(instance=alf::ForAllOrExistsOrOneOperation_strategy)
def test_alf::forallorexistsoroneoperation_expr1_setter(instance):
    original = instance.expr1
    instance.expr1 = original
    assert instance.expr1 == original

@given(instance=alf::ForAllOrExistsOrOneOperation_strategy)
def test_alf::forallorexistsoroneoperation_expr4_type(instance):
    assert isinstance(instance.expr4, str)


@given(instance=alf::ForAllOrExistsOrOneOperation_strategy)
def test_alf::forallorexistsoroneoperation_expr4_setter(instance):
    original = instance.expr4
    instance.expr4 = original
    assert instance.expr4 == original

@given(instance=alf::ForAllOrExistsOrOneOperation_strategy)
def test_alf::forallorexistsoroneoperation_expr3_type(instance):
    assert isinstance(instance.expr3, str)


@given(instance=alf::ForAllOrExistsOrOneOperation_strategy)
def test_alf::forallorexistsoroneoperation_expr3_setter(instance):
    original = instance.expr3
    instance.expr3 = original
    assert instance.expr3 == original

@given(instance=alf::CollectOrIterateOperation_strategy)
@settings(max_examples=50)
def test_alf::collectoriterateoperation_instantiation(instance):
    assert isinstance(instance, alf::CollectOrIterateOperation)

@given(instance=alf::CollectOrIterateOperation_strategy)
def test_alf::collectoriterateoperation_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=alf::CollectOrIterateOperation_strategy)
def test_alf::collectoriterateoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf::CollectOrIterateOperation_strategy)
def test_alf::collectoriterateoperation_expr3_type(instance):
    assert isinstance(instance.expr3, str)


@given(instance=alf::CollectOrIterateOperation_strategy)
def test_alf::collectoriterateoperation_expr3_setter(instance):
    original = instance.expr3
    instance.expr3 = original
    assert instance.expr3 == original

@given(instance=alf::CollectOrIterateOperation_strategy)
def test_alf::collectoriterateoperation_expr4_type(instance):
    assert isinstance(instance.expr4, str)


@given(instance=alf::CollectOrIterateOperation_strategy)
def test_alf::collectoriterateoperation_expr4_setter(instance):
    original = instance.expr4
    instance.expr4 = original
    assert instance.expr4 == original

@given(instance=alf::CollectOrIterateOperation_strategy)
def test_alf::collectoriterateoperation_expr1_type(instance):
    assert isinstance(instance.expr1, str)


@given(instance=alf::CollectOrIterateOperation_strategy)
def test_alf::collectoriterateoperation_expr1_setter(instance):
    original = instance.expr1
    instance.expr1 = original
    assert instance.expr1 == original

@given(instance=alf::CollectOrIterateOperation_strategy)
def test_alf::collectoriterateoperation_expr2_type(instance):
    assert isinstance(instance.expr2, str)


@given(instance=alf::CollectOrIterateOperation_strategy)
def test_alf::collectoriterateoperation_expr2_setter(instance):
    original = instance.expr2
    instance.expr2 = original
    assert instance.expr2 == original

@given(instance=alf::LinkOperationTupleElement_strategy)
@settings(max_examples=50)
def test_alf::linkoperationtupleelement_instantiation(instance):
    assert isinstance(instance, alf::LinkOperationTupleElement)

@given(instance=alf::LinkOperationTupleElement_strategy)
def test_alf::linkoperationtupleelement_objectOrRole_type(instance):
    assert isinstance(instance.objectOrRole, str)


@given(instance=alf::LinkOperationTupleElement_strategy)
def test_alf::linkoperationtupleelement_objectOrRole_setter(instance):
    original = instance.objectOrRole
    instance.objectOrRole = original
    assert instance.objectOrRole == original

@given(instance=alf::LinkOperationTuple_strategy)
@settings(max_examples=50)
def test_alf::linkoperationtuple_instantiation(instance):
    assert isinstance(instance, alf::LinkOperationTuple)

@given(instance=alf::ShiftExpression_strategy)
@settings(max_examples=50)
def test_alf::shiftexpression_instantiation(instance):
    assert isinstance(instance, alf::ShiftExpression)

@given(instance=alf::ShiftExpression_strategy)
def test_alf::shiftexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=alf::ShiftExpression_strategy)
def test_alf::shiftexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf::RelationalExpression_strategy)
@settings(max_examples=50)
def test_alf::relationalexpression_instantiation(instance):
    assert isinstance(instance, alf::RelationalExpression)

@given(instance=alf::RelationalExpression_strategy)
def test_alf::relationalexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=alf::RelationalExpression_strategy)
def test_alf::relationalexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf::OperationCallExpressionWithoutDot_strategy)
@settings(max_examples=50)
def test_alf::operationcallexpressionwithoutdot_instantiation(instance):
    assert isinstance(instance, alf::OperationCallExpressionWithoutDot)

@given(instance=alf::OperationCallExpressionWithoutDot_strategy)
def test_alf::operationcallexpressionwithoutdot_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=alf::OperationCallExpressionWithoutDot_strategy)
def test_alf::operationcallexpressionwithoutdot_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=SuffixExpression_strategy)
@settings(max_examples=50)
def test_suffixexpression_instantiation(instance):
    assert isinstance(instance, SuffixExpression)

@given(instance=alf::PropertyCallExpression_strategy)
@settings(max_examples=50)
def test_alf::propertycallexpression_instantiation(instance):
    assert isinstance(instance, alf::PropertyCallExpression)

@given(instance=alf::PropertyCallExpression_strategy)
def test_alf::propertycallexpression_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=alf::PropertyCallExpression_strategy)
def test_alf::propertycallexpression_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=alf::SequenceReductionExpression_strategy)
@settings(max_examples=50)
def test_alf::sequencereductionexpression_instantiation(instance):
    assert isinstance(instance, alf::SequenceReductionExpression)

@given(instance=alf::SequenceReductionExpression_strategy)
def test_alf::sequencereductionexpression_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, bool)


@given(instance=alf::SequenceReductionExpression_strategy)
def test_alf::sequencereductionexpression_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=alf::SequenceExpansionExpression_strategy)
@settings(max_examples=50)
def test_alf::sequenceexpansionexpression_instantiation(instance):
    assert isinstance(instance, alf::SequenceExpansionExpression)

@given(instance=alf::LinkOperationExpression_strategy)
@settings(max_examples=50)
def test_alf::linkoperationexpression_instantiation(instance):
    assert isinstance(instance, alf::LinkOperationExpression)

@given(instance=alf::LinkOperationExpression_strategy)
def test_alf::linkoperationexpression_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=alf::LinkOperationExpression_strategy)
def test_alf::linkoperationexpression_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=alf::SequenceOperationExpression_strategy)
@settings(max_examples=50)
def test_alf::sequenceoperationexpression_instantiation(instance):
    assert isinstance(instance, alf::SequenceOperationExpression)

@given(instance=alf::SequenceOperationExpression_strategy)
def test_alf::sequenceoperationexpression_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=alf::SequenceOperationExpression_strategy)
def test_alf::sequenceoperationexpression_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=alf::OperationCallExpression_strategy)
@settings(max_examples=50)
def test_alf::operationcallexpression_instantiation(instance):
    assert isinstance(instance, alf::OperationCallExpression)

@given(instance=alf::OperationCallExpression_strategy)
def test_alf::operationcallexpression_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=alf::OperationCallExpression_strategy)
def test_alf::operationcallexpression_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=alf::ValueSpecification_strategy)
@settings(max_examples=50)
def test_alf::valuespecification_instantiation(instance):
    assert isinstance(instance, alf::ValueSpecification)

@given(instance=alf::PrimaryExpression_strategy)
@settings(max_examples=50)
def test_alf::primaryexpression_instantiation(instance):
    assert isinstance(instance, alf::PrimaryExpression)

@given(instance=alf::UnaryExpression_strategy)
@settings(max_examples=50)
def test_alf::unaryexpression_instantiation(instance):
    assert isinstance(instance, alf::UnaryExpression)

@given(instance=alf::UnaryExpression_strategy)
def test_alf::unaryexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=alf::UnaryExpression_strategy)
def test_alf::unaryexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf::MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_alf::multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, alf::MultiplicativeExpression)

@given(instance=alf::MultiplicativeExpression_strategy)
def test_alf::multiplicativeexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=alf::MultiplicativeExpression_strategy)
def test_alf::multiplicativeexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf::AdditiveExpression_strategy)
@settings(max_examples=50)
def test_alf::additiveexpression_instantiation(instance):
    assert isinstance(instance, alf::AdditiveExpression)

@given(instance=alf::AdditiveExpression_strategy)
def test_alf::additiveexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=alf::AdditiveExpression_strategy)
def test_alf::additiveexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf::TupleElement_strategy)
@settings(max_examples=50)
def test_alf::tupleelement_instantiation(instance):
    assert isinstance(instance, alf::TupleElement)

@given(instance=alf::NamedTemplateBinding_strategy)
@settings(max_examples=50)
def test_alf::namedtemplatebinding_instantiation(instance):
    assert isinstance(instance, alf::NamedTemplateBinding)

@given(instance=alf::NamedTemplateBinding_strategy)
def test_alf::namedtemplatebinding_formal_type(instance):
    assert isinstance(instance.formal, str)


@given(instance=alf::NamedTemplateBinding_strategy)
def test_alf::namedtemplatebinding_formal_setter(instance):
    original = instance.formal
    instance.formal = original
    assert instance.formal == original

@given(instance=alf::ClassificationExpression_strategy)
@settings(max_examples=50)
def test_alf::classificationexpression_instantiation(instance):
    assert isinstance(instance, alf::ClassificationExpression)

@given(instance=alf::ClassificationExpression_strategy)
def test_alf::classificationexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=alf::ClassificationExpression_strategy)
def test_alf::classificationexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf::EqualityExpression_strategy)
@settings(max_examples=50)
def test_alf::equalityexpression_instantiation(instance):
    assert isinstance(instance, alf::EqualityExpression)

@given(instance=alf::EqualityExpression_strategy)
def test_alf::equalityexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=alf::EqualityExpression_strategy)
def test_alf::equalityexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf::AndExpression_strategy)
@settings(max_examples=50)
def test_alf::andexpression_instantiation(instance):
    assert isinstance(instance, alf::AndExpression)

@given(instance=alf::ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_alf::exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, alf::ExclusiveOrExpression)

@given(instance=alf::InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_alf::inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, alf::InclusiveOrExpression)

@given(instance=alf::ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_alf::conditionalandexpression_instantiation(instance):
    assert isinstance(instance, alf::ConditionalAndExpression)

@given(instance=alf::ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_alf::conditionalorexpression_instantiation(instance):
    assert isinstance(instance, alf::ConditionalOrExpression)

@given(instance=alf::InstanceCreationInvocationStatement_strategy)
@settings(max_examples=50)
def test_alf::instancecreationinvocationstatement_instantiation(instance):
    assert isinstance(instance, alf::InstanceCreationInvocationStatement)

@given(instance=alf::ThisInvocationStatement_strategy)
@settings(max_examples=50)
def test_alf::thisinvocationstatement_instantiation(instance):
    assert isinstance(instance, alf::ThisInvocationStatement)

@given(instance=alf::InvocationOrAssignementOrDeclarationStatement_strategy)
@settings(max_examples=50)
def test_alf::invocationorassignementordeclarationstatement_instantiation(instance):
    assert isinstance(instance, alf::InvocationOrAssignementOrDeclarationStatement)

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

@given(instance=alf::ClassifyStatement_strategy)
@settings(max_examples=50)
def test_alf::classifystatement_instantiation(instance):
    assert isinstance(instance, alf::ClassifyStatement)

@given(instance=alf::SuperInvocationStatement_strategy)
@settings(max_examples=50)
def test_alf::superinvocationstatement_instantiation(instance):
    assert isinstance(instance, alf::SuperInvocationStatement)

@given(instance=alf::VariableDeclarationCompletion_strategy)
@settings(max_examples=50)
def test_alf::variabledeclarationcompletion_instantiation(instance):
    assert isinstance(instance, alf::VariableDeclarationCompletion)

@given(instance=alf::VariableDeclarationCompletion_strategy)
def test_alf::variabledeclarationcompletion_multiplicityIndicator_type(instance):
    assert isinstance(instance.multiplicityIndicator, bool)


@given(instance=alf::VariableDeclarationCompletion_strategy)
def test_alf::variabledeclarationcompletion_multiplicityIndicator_setter(instance):
    original = instance.multiplicityIndicator
    instance.multiplicityIndicator = original
    assert instance.multiplicityIndicator == original

@given(instance=alf::VariableDeclarationCompletion_strategy)
def test_alf::variabledeclarationcompletion_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=alf::VariableDeclarationCompletion_strategy)
def test_alf::variabledeclarationcompletion_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=alf::CompoundAcceptStatementCompletion_strategy)
@settings(max_examples=50)
def test_alf::compoundacceptstatementcompletion_instantiation(instance):
    assert isinstance(instance, alf::CompoundAcceptStatementCompletion)

@given(instance=alf::SimpleAcceptStatementCompletion_strategy)
@settings(max_examples=50)
def test_alf::simpleacceptstatementcompletion_instantiation(instance):
    assert isinstance(instance, alf::SimpleAcceptStatementCompletion)

@given(instance=alf::AcceptClause_strategy)
@settings(max_examples=50)
def test_alf::acceptclause_instantiation(instance):
    assert isinstance(instance, alf::AcceptClause)

@given(instance=alf::AcceptClause_strategy)
def test_alf::acceptclause_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=alf::AcceptClause_strategy)
def test_alf::acceptclause_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=alf::AcceptStatement_strategy)
@settings(max_examples=50)
def test_alf::acceptstatement_instantiation(instance):
    assert isinstance(instance, alf::AcceptStatement)

@given(instance=alf::ReturnStatement_strategy)
@settings(max_examples=50)
def test_alf::returnstatement_instantiation(instance):
    assert isinstance(instance, alf::ReturnStatement)

@given(instance=alf::BreakStatement_strategy)
@settings(max_examples=50)
def test_alf::breakstatement_instantiation(instance):
    assert isinstance(instance, alf::BreakStatement)

@given(instance=alf::LoopVariableDefinition_strategy)
@settings(max_examples=50)
def test_alf::loopvariabledefinition_instantiation(instance):
    assert isinstance(instance, alf::LoopVariableDefinition)

@given(instance=alf::LoopVariableDefinition_strategy)
def test_alf::loopvariabledefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=alf::LoopVariableDefinition_strategy)
def test_alf::loopvariabledefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=alf::ForControl_strategy)
@settings(max_examples=50)
def test_alf::forcontrol_instantiation(instance):
    assert isinstance(instance, alf::ForControl)

@given(instance=alf::ForStatement_strategy)
@settings(max_examples=50)
def test_alf::forstatement_instantiation(instance):
    assert isinstance(instance, alf::ForStatement)

@given(instance=alf::AcceptBlock_strategy)
@settings(max_examples=50)
def test_alf::acceptblock_instantiation(instance):
    assert isinstance(instance, alf::AcceptBlock)

@given(instance=alf::WhileStatement_strategy)
@settings(max_examples=50)
def test_alf::whilestatement_instantiation(instance):
    assert isinstance(instance, alf::WhileStatement)

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

@given(instance=alf::SwitchStatement_strategy)
@settings(max_examples=50)
def test_alf::switchstatement_instantiation(instance):
    assert isinstance(instance, alf::SwitchStatement)

@given(instance=alf::DoStatement_strategy)
@settings(max_examples=50)
def test_alf::dostatement_instantiation(instance):
    assert isinstance(instance, alf::DoStatement)

@given(instance=alf::SequentialClauses_strategy)
@settings(max_examples=50)
def test_alf::sequentialclauses_instantiation(instance):
    assert isinstance(instance, alf::SequentialClauses)

@given(instance=alf::IfStatement_strategy)
@settings(max_examples=50)
def test_alf::ifstatement_instantiation(instance):
    assert isinstance(instance, alf::IfStatement)

@given(instance=alf::LocalNameDeclarationStatement_strategy)
@settings(max_examples=50)
def test_alf::localnamedeclarationstatement_instantiation(instance):
    assert isinstance(instance, alf::LocalNameDeclarationStatement)

@given(instance=alf::LocalNameDeclarationStatement_strategy)
def test_alf::localnamedeclarationstatement_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=alf::LocalNameDeclarationStatement_strategy)
def test_alf::localnamedeclarationstatement_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=alf::LocalNameDeclarationStatement_strategy)
def test_alf::localnamedeclarationstatement_multiplicityIndicator_type(instance):
    assert isinstance(instance.multiplicityIndicator, bool)


@given(instance=alf::LocalNameDeclarationStatement_strategy)
def test_alf::localnamedeclarationstatement_multiplicityIndicator_setter(instance):
    original = instance.multiplicityIndicator
    instance.multiplicityIndicator = original
    assert instance.multiplicityIndicator == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=alf::ConditionalTestExpression_strategy)
@settings(max_examples=50)
def test_alf::conditionaltestexpression_instantiation(instance):
    assert isinstance(instance, alf::ConditionalTestExpression)

@given(instance=SequenceElement_strategy)
@settings(max_examples=50)
def test_sequenceelement_instantiation(instance):
    assert isinstance(instance, SequenceElement)

@given(instance=alf::SequenceConstructionExpression_strategy)
@settings(max_examples=50)
def test_alf::sequenceconstructionexpression_instantiation(instance):
    assert isinstance(instance, alf::SequenceConstructionExpression)

@given(instance=LITERAL_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, LITERAL)

@given(instance=alf::BOOLEAN::LITERAL_strategy)
@settings(max_examples=50)
def test_alf::boolean::literal_instantiation(instance):
    assert isinstance(instance, alf::BOOLEAN::LITERAL)

@given(instance=alf::BOOLEAN::LITERAL_strategy)
def test_alf::boolean::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=alf::BOOLEAN::LITERAL_strategy)
def test_alf::boolean::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=alf::SuffixExpression_strategy)
@settings(max_examples=50)
def test_alf::suffixexpression_instantiation(instance):
    assert isinstance(instance, alf::SuffixExpression)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=alf::NullExpression_strategy)
@settings(max_examples=50)
def test_alf::nullexpression_instantiation(instance):
    assert isinstance(instance, alf::NullExpression)

@given(instance=alf::LITERAL_strategy)
@settings(max_examples=50)
def test_alf::literal_instantiation(instance):
    assert isinstance(instance, alf::LITERAL)

@given(instance=alf::Statement_strategy)
@settings(max_examples=50)
def test_alf::statement_instantiation(instance):
    assert isinstance(instance, alf::Statement)

@given(instance=alf::AssignmentCompletion_strategy)
@settings(max_examples=50)
def test_alf::assignmentcompletion_instantiation(instance):
    assert isinstance(instance, alf::AssignmentCompletion)

@given(instance=alf::AssignmentCompletion_strategy)
def test_alf::assignmentcompletion_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=alf::AssignmentCompletion_strategy)
def test_alf::assignmentcompletion_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=alf::TemplateBinding_strategy)
@settings(max_examples=50)
def test_alf::templatebinding_instantiation(instance):
    assert isinstance(instance, alf::TemplateBinding)

@given(instance=alf::UnqualifiedName_strategy)
@settings(max_examples=50)
def test_alf::unqualifiedname_instantiation(instance):
    assert isinstance(instance, alf::UnqualifiedName)

@given(instance=alf::UnqualifiedName_strategy)
def test_alf::unqualifiedname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=alf::UnqualifiedName_strategy)
def test_alf::unqualifiedname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=alf::SequenceConstructionOrAccessCompletion_strategy)
@settings(max_examples=50)
def test_alf::sequenceconstructionoraccesscompletion_instantiation(instance):
    assert isinstance(instance, alf::SequenceConstructionOrAccessCompletion)

@given(instance=alf::SequenceConstructionOrAccessCompletion_strategy)
def test_alf::sequenceconstructionoraccesscompletion_multiplicityIndicator_type(instance):
    assert isinstance(instance.multiplicityIndicator, bool)


@given(instance=alf::SequenceConstructionOrAccessCompletion_strategy)
def test_alf::sequenceconstructionoraccesscompletion_multiplicityIndicator_setter(instance):
    original = instance.multiplicityIndicator
    instance.multiplicityIndicator = original
    assert instance.multiplicityIndicator == original

@given(instance=alf::Tuple_strategy)
@settings(max_examples=50)
def test_alf::tuple_instantiation(instance):
    assert isinstance(instance, alf::Tuple)

@given(instance=alf::QualifiedNamePath_strategy)
@settings(max_examples=50)
def test_alf::qualifiednamepath_instantiation(instance):
    assert isinstance(instance, alf::QualifiedNamePath)

@given(instance=NonLiteralValueSpecification_strategy)
@settings(max_examples=50)
def test_nonliteralvaluespecification_instantiation(instance):
    assert isinstance(instance, NonLiteralValueSpecification)

@given(instance=alf::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_alf::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, alf::ParenthesizedExpression)

@given(instance=alf::InstanceCreationExpression_strategy)
@settings(max_examples=50)
def test_alf::instancecreationexpression_instantiation(instance):
    assert isinstance(instance, alf::InstanceCreationExpression)

@given(instance=alf::SuperInvocationExpression_strategy)
@settings(max_examples=50)
def test_alf::superinvocationexpression_instantiation(instance):
    assert isinstance(instance, alf::SuperInvocationExpression)

@given(instance=alf::SuperInvocationExpression_strategy)
def test_alf::superinvocationexpression_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=alf::SuperInvocationExpression_strategy)
def test_alf::superinvocationexpression_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=alf::ThisExpression_strategy)
@settings(max_examples=50)
def test_alf::thisexpression_instantiation(instance):
    assert isinstance(instance, alf::ThisExpression)

@given(instance=alf::NameExpression_strategy)
@settings(max_examples=50)
def test_alf::nameexpression_instantiation(instance):
    assert isinstance(instance, alf::NameExpression)

@given(instance=alf::NameExpression_strategy)
def test_alf::nameexpression_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=alf::NameExpression_strategy)
def test_alf::nameexpression_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=alf::NameExpression_strategy)
def test_alf::nameexpression_prefixOp_type(instance):
    assert isinstance(instance.prefixOp, str)


@given(instance=alf::NameExpression_strategy)
def test_alf::nameexpression_prefixOp_setter(instance):
    original = instance.prefixOp
    instance.prefixOp = original
    assert instance.prefixOp == original

@given(instance=alf::NameExpression_strategy)
def test_alf::nameexpression_postfixOp_type(instance):
    assert isinstance(instance.postfixOp, str)


@given(instance=alf::NameExpression_strategy)
def test_alf::nameexpression_postfixOp_setter(instance):
    original = instance.postfixOp
    instance.postfixOp = original
    assert instance.postfixOp == original

@given(instance=alf::STRING::LITERAL_strategy)
@settings(max_examples=50)
def test_alf::string::literal_instantiation(instance):
    assert isinstance(instance, alf::STRING::LITERAL)

@given(instance=alf::STRING::LITERAL_strategy)
def test_alf::string::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=alf::STRING::LITERAL_strategy)
def test_alf::string::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NUMBER::LITERAL_strategy)
@settings(max_examples=50)
def test_number::literal_instantiation(instance):
    assert isinstance(instance, NUMBER::LITERAL)

@given(instance=alf::UNLIMITED::LITERAL_strategy)
@settings(max_examples=50)
def test_alf::unlimited::literal_instantiation(instance):
    assert isinstance(instance, alf::UNLIMITED::LITERAL)

@given(instance=alf::INTEGER::LITERAL_strategy)
@settings(max_examples=50)
def test_alf::integer::literal_instantiation(instance):
    assert isinstance(instance, alf::INTEGER::LITERAL)

@given(instance=alf::NUMBER::LITERAL_strategy)
@settings(max_examples=50)
def test_alf::number::literal_instantiation(instance):
    assert isinstance(instance, alf::NUMBER::LITERAL)

@given(instance=alf::NUMBER::LITERAL_strategy)
def test_alf::number::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=alf::NUMBER::LITERAL_strategy)
def test_alf::number::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=alf::MultiplicityRange_strategy)
@settings(max_examples=50)
def test_alf::multiplicityrange_instantiation(instance):
    assert isinstance(instance, alf::MultiplicityRange)

@given(instance=alf::Multiplicity_strategy)
@settings(max_examples=50)
def test_alf::multiplicity_instantiation(instance):
    assert isinstance(instance, alf::Multiplicity)

@given(instance=alf::Multiplicity_strategy)
def test_alf::multiplicity_nonUnique_type(instance):
    assert isinstance(instance.nonUnique, bool)


@given(instance=alf::Multiplicity_strategy)
def test_alf::multiplicity_nonUnique_setter(instance):
    original = instance.nonUnique
    instance.nonUnique = original
    assert instance.nonUnique == original

@given(instance=alf::Multiplicity_strategy)
def test_alf::multiplicity_ordered_type(instance):
    assert isinstance(instance.ordered, bool)


@given(instance=alf::Multiplicity_strategy)
def test_alf::multiplicity_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=alf::Multiplicity_strategy)
def test_alf::multiplicity_sequence_type(instance):
    assert isinstance(instance.sequence, bool)


@given(instance=alf::Multiplicity_strategy)
def test_alf::multiplicity_sequence_setter(instance):
    original = instance.sequence
    instance.sequence = original
    assert instance.sequence == original

@given(instance=alf::Expression_strategy)
@settings(max_examples=50)
def test_alf::expression_instantiation(instance):
    assert isinstance(instance, alf::Expression)

@given(instance=alf::Test_strategy)
@settings(max_examples=50)
def test_alf::test_instantiation(instance):
    assert isinstance(instance, alf::Test)

@given(instance=alf::QualifiedNameList_strategy)
@settings(max_examples=50)
def test_alf::qualifiednamelist_instantiation(instance):
    assert isinstance(instance, alf::QualifiedNameList)

@given(instance=alf::QualifiedNameWithBinding_strategy)
@settings(max_examples=50)
def test_alf::qualifiednamewithbinding_instantiation(instance):
    assert isinstance(instance, alf::QualifiedNameWithBinding)

@given(instance=alf::QualifiedNameWithBinding_strategy)
def test_alf::qualifiednamewithbinding_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=alf::QualifiedNameWithBinding_strategy)
def test_alf::qualifiednamewithbinding_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=NUMBER::LITERAL::WITHOUT::SUFFIX_strategy)
@settings(max_examples=50)
def test_number::literal::without::suffix_instantiation(instance):
    assert isinstance(instance, NUMBER::LITERAL::WITHOUT::SUFFIX)

@given(instance=alf::UNLIMITED::LITERAL::WITHOUT::SUFFIX_strategy)
@settings(max_examples=50)
def test_alf::unlimited::literal::without::suffix_instantiation(instance):
    assert isinstance(instance, alf::UNLIMITED::LITERAL::WITHOUT::SUFFIX)

@given(instance=alf::INTEGER::LITERAL::WITHOUT::SUFFIX_strategy)
@settings(max_examples=50)
def test_alf::integer::literal::without::suffix_instantiation(instance):
    assert isinstance(instance, alf::INTEGER::LITERAL::WITHOUT::SUFFIX)

@given(instance=alf::NUMBER::LITERAL::WITHOUT::SUFFIX_strategy)
@settings(max_examples=50)
def test_alf::number::literal::without::suffix_instantiation(instance):
    assert isinstance(instance, alf::NUMBER::LITERAL::WITHOUT::SUFFIX)

@given(instance=alf::NUMBER::LITERAL::WITHOUT::SUFFIX_strategy)
def test_alf::number::literal::without::suffix_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=alf::NUMBER::LITERAL::WITHOUT::SUFFIX_strategy)
def test_alf::number::literal::without::suffix_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=alf::FormalParameters_strategy)
@settings(max_examples=50)
def test_alf::formalparameters_instantiation(instance):
    assert isinstance(instance, alf::FormalParameters)

@given(instance=alf::Block_strategy)
@settings(max_examples=50)
def test_alf::block_instantiation(instance):
    assert isinstance(instance, alf::Block)

@given(instance=alf::OperationDeclaration_strategy)
@settings(max_examples=50)
def test_alf::operationdeclaration_instantiation(instance):
    assert isinstance(instance, alf::OperationDeclaration)

@given(instance=alf::OperationDeclaration_strategy)
def test_alf::operationdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=alf::OperationDeclaration_strategy)
def test_alf::operationdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=alf::TypeName_strategy)
@settings(max_examples=50)
def test_alf::typename_instantiation(instance):
    assert isinstance(instance, alf::TypeName)

@given(instance=alf::FormalParameter_strategy)
@settings(max_examples=50)
def test_alf::formalparameter_instantiation(instance):
    assert isinstance(instance, alf::FormalParameter)

@given(instance=alf::FormalParameter_strategy)
def test_alf::formalparameter_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=alf::FormalParameter_strategy)
def test_alf::formalparameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=alf::FormalParameter_strategy)
def test_alf::formalparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=alf::FormalParameter_strategy)
def test_alf::formalparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=alf::FormalParameterList_strategy)
@settings(max_examples=50)
def test_alf::formalparameterlist_instantiation(instance):
    assert isinstance(instance, alf::FormalParameterList)

@given(instance=alf::RedefinitionClause_strategy)
@settings(max_examples=50)
def test_alf::redefinitionclause_instantiation(instance):
    assert isinstance(instance, alf::RedefinitionClause)

@given(instance=alf::OperationDefinitionOrStub_strategy)
@settings(max_examples=50)
def test_alf::operationdefinitionorstub_instantiation(instance):
    assert isinstance(instance, alf::OperationDefinitionOrStub)

@given(instance=alf::TypePart_strategy)
@settings(max_examples=50)
def test_alf::typepart_instantiation(instance):
    assert isinstance(instance, alf::TypePart)

@given(instance=alf::Operations_strategy)
@settings(max_examples=50)
def test_alf::operations_instantiation(instance):
    assert isinstance(instance, alf::Operations)

@given(instance=alf::Operations_strategy)
def test_alf::operations_imports_type(instance):
    assert isinstance(instance.imports, str)


@given(instance=alf::Operations_strategy)
def test_alf::operations_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original
