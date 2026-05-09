import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UnaryOp,
    ast::BitwiseComplementOp,
    BinaryOp,
    ast::BitwiseAndOp,
    AssignmentOperation,
    ast::BitwiseOrAssignmentOp,
    ast::BitwiseAndAssignmentOp,
    ast::AssignmentOp,
    ast::ConditionalAndOp,
    Expression,
    ast::ArrayConstructor,
    ast::AssignmentOperation,
    ast::ClassifierOp,
    ast::ApplyRoundOp,
    ast::BinaryOp,
    ast::AccessOp,
    ScopeStatement,
    ast::TryStatement,
    ast::SynchronizedStatement,
    ast::ApplySquareOp,
    LabeledStatement,
    ast::SwitchStatement,
    ast::LoopStatement,
    SwitchPart,
    ast::SwitchDefaultPart,
    ast::SwitchCasePart,
    MethodContentStatement,
    ast::ThrowStatement,
    ast::ScopeStatement,
    ast::JumpStatement,
    ast::IfStatement,
    ast::LocalVarStatement,
    ast::MethodClassifier,
    ast::LabeledStatement,
    ast::ExpressionStatement,
    ConditionalLoop,
    ast::ForStatement,
    ast::WhileStatement,
    ast::DoWhileStatement,
    TopLevelStatement,
    ast::TopLevelClassifier,
    ast::PackageStatement,
    ast::ImportStatement,
    ClassifierStatement,
    ast::InterfaceStatement,
    ast::ImplemenationClassifierStatement,
    LoopStatement,
    ast::ForeachStatement,
    ast::ConditionalLoop,
    JumpStatement,
    ast::ContinueStatement,
    ast::BreakStatement,
    InitStatement,
    ast::StaticInitStatement,
    ast::InstanceInitStatement,
    ImplemenationClassifierStatement,
    ast::EnumStatement,
    ast::ClassStatement,
    ClassifierMemberStatement,
    ast::Feature,
    ast::InnerClassifier,
    ast::InitStatement,
    ast::EnumLiteral,
    ast::MethodBlock,
    BehaviorFeature,
    ast::MethodStatement,
    ast::ConstructorStatement,
    EJBase,
    ast::MethodContentStatement,
    ast::CatchPart,
    ast::SwitchPart,
    ast::ClassifierStatement,
    ast::TopLevelStatement,
    ast::IfThenPart,
    ast::ClassifierMemberStatement,
    ast::ClassBlock,
    ast::Identifier,
    Feature,
    ast::BehaviorFeature,
    ast::FieldStatement,
    NamedElement,
    ast::TemplateParameter,
    ast::Variable,
    ast::Parameter,
    ast::Expression,
    EJElement,
    ast::AttributeSet,
    ast::Label,
    ast::Modifier,
    ast::SwitchDefaultPartRef,
    ast::DocumentationLine,
    ast::EJBase,
    ast::EJElement,
    ast::AttributeDefinition,
    ast::EmptyStatement,
    ast::WildcardType,
    ast::RangeExpression,
    ast::AssertStatement,
    ast::NamedElement,
    ast::UnaryOp,
    ast::UnaryMinusOp,
    ast::ThisReference,
    ast::SuperReference,
    ast::ShiftOp,
    ast::RightShiftAssignmentOp,
    ast::ReturnStatement,
    ast::RemainderAssignmentOp,
    ast::PrimitiveType,
    ast::PrefixIncrementOp,
    ast::PrefixDecrementOp,
    ast::PostfixIncrementOp,
    ast::ZeroExtensionRightShiftAssignmentOp,
    ast::UnaryPlusOp,
    ast::NewOp,
    ast::MultiplyAssignmentOp,
    ast::MultiplyOp,
    ast::MinusOp,
    ast::MinusAssignmentOp,
    ast::LogicalComplementOp,
    ast::Literal,
    ast::LessThenOp,
    ast::LessOrEqualOp,
    ast::PostfixDecrementOp,
    ast::PlusOp,
    ast::PlusAssignmentOp,
    ast::NotEqualOp,
    ast::IdentityOp,
    ast::GreaterThenOp,
    ast::GreaterOrEqualOp,
    ast::EqualOp,
    ast::DivisionOp,
    DivisionOp,
    ast::RemainderOp,
    ast::DivideOp,
    ast::DivideAssignmentOp,
    ast::ConditionalOrOp,
    ast::ConditionalOp,
    ShiftOp,
    ast::RightShiftOp,
    ast::ZeroExtensionRightShiftOp,
    ast::LeftShiftOp,
    ast::LeftShiftAssignmentOp,
    ClassifierOp,
    ast::InstanceOfOp,
    ast::CastOp,
    Literal,
    ast::FloatLiteral,
    ast::LongIntegerLiteral,
    ast::IntegerLiteral,
    ast::DoubleLiteral,
    ast::CharacterLiteral,
    ast::StringLiteral,
    ast::NullReference,
    ast::BooleanLiteral,
    ast::BitwiseXorOp,
    ast::BitwiseXorAssignmentOp,
    ast::BitwiseOrOp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_unaryop_is_not_abstract():
    assert not inspect.isabstract(UnaryOp)


def test_unaryop_constructor_exists():
    assert callable(UnaryOp.__init__)


def test_unaryop_constructor_args():
    sig = inspect.signature(UnaryOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::bitwisecomplementop_is_not_abstract():
    assert not inspect.isabstract(ast::BitwiseComplementOp)


def test_ast::bitwisecomplementop_constructor_exists():
    assert callable(ast::BitwiseComplementOp.__init__)


def test_ast::bitwisecomplementop_constructor_args():
    sig = inspect.signature(ast::BitwiseComplementOp.__init__)
    params = list(sig.parameters.keys())



def test_binaryop_is_not_abstract():
    assert not inspect.isabstract(BinaryOp)


def test_binaryop_constructor_exists():
    assert callable(BinaryOp.__init__)


def test_binaryop_constructor_args():
    sig = inspect.signature(BinaryOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::bitwiseandop_is_not_abstract():
    assert not inspect.isabstract(ast::BitwiseAndOp)


def test_ast::bitwiseandop_constructor_exists():
    assert callable(ast::BitwiseAndOp.__init__)


def test_ast::bitwiseandop_constructor_args():
    sig = inspect.signature(ast::BitwiseAndOp.__init__)
    params = list(sig.parameters.keys())



def test_assignmentoperation_is_not_abstract():
    assert not inspect.isabstract(AssignmentOperation)


def test_assignmentoperation_constructor_exists():
    assert callable(AssignmentOperation.__init__)


def test_assignmentoperation_constructor_args():
    sig = inspect.signature(AssignmentOperation.__init__)
    params = list(sig.parameters.keys())



def test_ast::bitwiseorassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast::BitwiseOrAssignmentOp)


def test_ast::bitwiseorassignmentop_constructor_exists():
    assert callable(ast::BitwiseOrAssignmentOp.__init__)


def test_ast::bitwiseorassignmentop_constructor_args():
    sig = inspect.signature(ast::BitwiseOrAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::bitwiseandassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast::BitwiseAndAssignmentOp)


def test_ast::bitwiseandassignmentop_constructor_exists():
    assert callable(ast::BitwiseAndAssignmentOp.__init__)


def test_ast::bitwiseandassignmentop_constructor_args():
    sig = inspect.signature(ast::BitwiseAndAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::assignmentop_is_not_abstract():
    assert not inspect.isabstract(ast::AssignmentOp)


def test_ast::assignmentop_constructor_exists():
    assert callable(ast::AssignmentOp.__init__)


def test_ast::assignmentop_constructor_args():
    sig = inspect.signature(ast::AssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::conditionalandop_is_not_abstract():
    assert not inspect.isabstract(ast::ConditionalAndOp)


def test_ast::conditionalandop_constructor_exists():
    assert callable(ast::ConditionalAndOp.__init__)


def test_ast::conditionalandop_constructor_args():
    sig = inspect.signature(ast::ConditionalAndOp.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_ast::arrayconstructor_is_not_abstract():
    assert not inspect.isabstract(ast::ArrayConstructor)


def test_ast::arrayconstructor_constructor_exists():
    assert callable(ast::ArrayConstructor.__init__)


def test_ast::arrayconstructor_constructor_args():
    sig = inspect.signature(ast::ArrayConstructor.__init__)
    params = list(sig.parameters.keys())



def test_ast::assignmentoperation_is_not_abstract():
    assert not inspect.isabstract(ast::AssignmentOperation)


def test_ast::assignmentoperation_constructor_exists():
    assert callable(ast::AssignmentOperation.__init__)


def test_ast::assignmentoperation_constructor_args():
    sig = inspect.signature(ast::AssignmentOperation.__init__)
    params = list(sig.parameters.keys())



def test_ast::classifierop_is_not_abstract():
    assert not inspect.isabstract(ast::ClassifierOp)


def test_ast::classifierop_constructor_exists():
    assert callable(ast::ClassifierOp.__init__)


def test_ast::classifierop_constructor_args():
    sig = inspect.signature(ast::ClassifierOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::applyroundop_is_not_abstract():
    assert not inspect.isabstract(ast::ApplyRoundOp)


def test_ast::applyroundop_constructor_exists():
    assert callable(ast::ApplyRoundOp.__init__)


def test_ast::applyroundop_constructor_args():
    sig = inspect.signature(ast::ApplyRoundOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::binaryop_is_not_abstract():
    assert not inspect.isabstract(ast::BinaryOp)


def test_ast::binaryop_constructor_exists():
    assert callable(ast::BinaryOp.__init__)


def test_ast::binaryop_constructor_args():
    sig = inspect.signature(ast::BinaryOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::accessop_is_not_abstract():
    assert not inspect.isabstract(ast::AccessOp)


def test_ast::accessop_constructor_exists():
    assert callable(ast::AccessOp.__init__)


def test_ast::accessop_constructor_args():
    sig = inspect.signature(ast::AccessOp.__init__)
    params = list(sig.parameters.keys())



def test_scopestatement_is_not_abstract():
    assert not inspect.isabstract(ScopeStatement)


def test_scopestatement_constructor_exists():
    assert callable(ScopeStatement.__init__)


def test_scopestatement_constructor_args():
    sig = inspect.signature(ScopeStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::trystatement_is_not_abstract():
    assert not inspect.isabstract(ast::TryStatement)


def test_ast::trystatement_constructor_exists():
    assert callable(ast::TryStatement.__init__)


def test_ast::trystatement_constructor_args():
    sig = inspect.signature(ast::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(ast::SynchronizedStatement)


def test_ast::synchronizedstatement_constructor_exists():
    assert callable(ast::SynchronizedStatement.__init__)


def test_ast::synchronizedstatement_constructor_args():
    sig = inspect.signature(ast::SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::applysquareop_is_not_abstract():
    assert not inspect.isabstract(ast::ApplySquareOp)


def test_ast::applysquareop_constructor_exists():
    assert callable(ast::ApplySquareOp.__init__)


def test_ast::applysquareop_constructor_args():
    sig = inspect.signature(ast::ApplySquareOp.__init__)
    params = list(sig.parameters.keys())



def test_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(LabeledStatement)


def test_labeledstatement_constructor_exists():
    assert callable(LabeledStatement.__init__)


def test_labeledstatement_constructor_args():
    sig = inspect.signature(LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::switchstatement_is_not_abstract():
    assert not inspect.isabstract(ast::SwitchStatement)


def test_ast::switchstatement_constructor_exists():
    assert callable(ast::SwitchStatement.__init__)


def test_ast::switchstatement_constructor_args():
    sig = inspect.signature(ast::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::loopstatement_is_not_abstract():
    assert not inspect.isabstract(ast::LoopStatement)


def test_ast::loopstatement_constructor_exists():
    assert callable(ast::LoopStatement.__init__)


def test_ast::loopstatement_constructor_args():
    sig = inspect.signature(ast::LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_switchpart_is_not_abstract():
    assert not inspect.isabstract(SwitchPart)


def test_switchpart_constructor_exists():
    assert callable(SwitchPart.__init__)


def test_switchpart_constructor_args():
    sig = inspect.signature(SwitchPart.__init__)
    params = list(sig.parameters.keys())



def test_ast::switchdefaultpart_is_not_abstract():
    assert not inspect.isabstract(ast::SwitchDefaultPart)


def test_ast::switchdefaultpart_constructor_exists():
    assert callable(ast::SwitchDefaultPart.__init__)


def test_ast::switchdefaultpart_constructor_args():
    sig = inspect.signature(ast::SwitchDefaultPart.__init__)
    params = list(sig.parameters.keys())



def test_ast::switchcasepart_is_not_abstract():
    assert not inspect.isabstract(ast::SwitchCasePart)


def test_ast::switchcasepart_constructor_exists():
    assert callable(ast::SwitchCasePart.__init__)


def test_ast::switchcasepart_constructor_args():
    sig = inspect.signature(ast::SwitchCasePart.__init__)
    params = list(sig.parameters.keys())



def test_methodcontentstatement_is_not_abstract():
    assert not inspect.isabstract(MethodContentStatement)


def test_methodcontentstatement_constructor_exists():
    assert callable(MethodContentStatement.__init__)


def test_methodcontentstatement_constructor_args():
    sig = inspect.signature(MethodContentStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::throwstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ThrowStatement)


def test_ast::throwstatement_constructor_exists():
    assert callable(ast::ThrowStatement.__init__)


def test_ast::throwstatement_constructor_args():
    sig = inspect.signature(ast::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::scopestatement_is_not_abstract():
    assert not inspect.isabstract(ast::ScopeStatement)


def test_ast::scopestatement_constructor_exists():
    assert callable(ast::ScopeStatement.__init__)


def test_ast::scopestatement_constructor_args():
    sig = inspect.signature(ast::ScopeStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::jumpstatement_is_not_abstract():
    assert not inspect.isabstract(ast::JumpStatement)


def test_ast::jumpstatement_constructor_exists():
    assert callable(ast::JumpStatement.__init__)


def test_ast::jumpstatement_constructor_args():
    sig = inspect.signature(ast::JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::ifstatement_is_not_abstract():
    assert not inspect.isabstract(ast::IfStatement)


def test_ast::ifstatement_constructor_exists():
    assert callable(ast::IfStatement.__init__)


def test_ast::ifstatement_constructor_args():
    sig = inspect.signature(ast::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::localvarstatement_is_not_abstract():
    assert not inspect.isabstract(ast::LocalVarStatement)


def test_ast::localvarstatement_constructor_exists():
    assert callable(ast::LocalVarStatement.__init__)


def test_ast::localvarstatement_constructor_args():
    sig = inspect.signature(ast::LocalVarStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::methodclassifier_is_not_abstract():
    assert not inspect.isabstract(ast::MethodClassifier)


def test_ast::methodclassifier_constructor_exists():
    assert callable(ast::MethodClassifier.__init__)


def test_ast::methodclassifier_constructor_args():
    sig = inspect.signature(ast::MethodClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ast::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(ast::LabeledStatement)


def test_ast::labeledstatement_constructor_exists():
    assert callable(ast::LabeledStatement.__init__)


def test_ast::labeledstatement_constructor_args():
    sig = inspect.signature(ast::LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ExpressionStatement)


def test_ast::expressionstatement_constructor_exists():
    assert callable(ast::ExpressionStatement.__init__)


def test_ast::expressionstatement_constructor_args():
    sig = inspect.signature(ast::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_conditionalloop_is_not_abstract():
    assert not inspect.isabstract(ConditionalLoop)


def test_conditionalloop_constructor_exists():
    assert callable(ConditionalLoop.__init__)


def test_conditionalloop_constructor_args():
    sig = inspect.signature(ConditionalLoop.__init__)
    params = list(sig.parameters.keys())



def test_ast::forstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ForStatement)


def test_ast::forstatement_constructor_exists():
    assert callable(ast::ForStatement.__init__)


def test_ast::forstatement_constructor_args():
    sig = inspect.signature(ast::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::whilestatement_is_not_abstract():
    assert not inspect.isabstract(ast::WhileStatement)


def test_ast::whilestatement_constructor_exists():
    assert callable(ast::WhileStatement.__init__)


def test_ast::whilestatement_constructor_args():
    sig = inspect.signature(ast::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(ast::DoWhileStatement)


def test_ast::dowhilestatement_constructor_exists():
    assert callable(ast::DoWhileStatement.__init__)


def test_ast::dowhilestatement_constructor_args():
    sig = inspect.signature(ast::DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_toplevelstatement_is_not_abstract():
    assert not inspect.isabstract(TopLevelStatement)


def test_toplevelstatement_constructor_exists():
    assert callable(TopLevelStatement.__init__)


def test_toplevelstatement_constructor_args():
    sig = inspect.signature(TopLevelStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::toplevelclassifier_is_not_abstract():
    assert not inspect.isabstract(ast::TopLevelClassifier)


def test_ast::toplevelclassifier_constructor_exists():
    assert callable(ast::TopLevelClassifier.__init__)


def test_ast::toplevelclassifier_constructor_args():
    sig = inspect.signature(ast::TopLevelClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ast::packagestatement_is_not_abstract():
    assert not inspect.isabstract(ast::PackageStatement)


def test_ast::packagestatement_constructor_exists():
    assert callable(ast::PackageStatement.__init__)


def test_ast::packagestatement_constructor_args():
    sig = inspect.signature(ast::PackageStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::importstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ImportStatement)


def test_ast::importstatement_constructor_exists():
    assert callable(ast::ImportStatement.__init__)


def test_ast::importstatement_constructor_args():
    sig = inspect.signature(ast::ImportStatement.__init__)
    params = list(sig.parameters.keys())



def test_classifierstatement_is_not_abstract():
    assert not inspect.isabstract(ClassifierStatement)


def test_classifierstatement_constructor_exists():
    assert callable(ClassifierStatement.__init__)


def test_classifierstatement_constructor_args():
    sig = inspect.signature(ClassifierStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::interfacestatement_is_not_abstract():
    assert not inspect.isabstract(ast::InterfaceStatement)


def test_ast::interfacestatement_constructor_exists():
    assert callable(ast::InterfaceStatement.__init__)


def test_ast::interfacestatement_constructor_args():
    sig = inspect.signature(ast::InterfaceStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::implemenationclassifierstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ImplemenationClassifierStatement)


def test_ast::implemenationclassifierstatement_constructor_exists():
    assert callable(ast::ImplemenationClassifierStatement.__init__)


def test_ast::implemenationclassifierstatement_constructor_args():
    sig = inspect.signature(ast::ImplemenationClassifierStatement.__init__)
    params = list(sig.parameters.keys())



def test_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::foreachstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ForeachStatement)


def test_ast::foreachstatement_constructor_exists():
    assert callable(ast::ForeachStatement.__init__)


def test_ast::foreachstatement_constructor_args():
    sig = inspect.signature(ast::ForeachStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::conditionalloop_is_not_abstract():
    assert not inspect.isabstract(ast::ConditionalLoop)


def test_ast::conditionalloop_constructor_exists():
    assert callable(ast::ConditionalLoop.__init__)


def test_ast::conditionalloop_constructor_args():
    sig = inspect.signature(ast::ConditionalLoop.__init__)
    params = list(sig.parameters.keys())



def test_jumpstatement_is_not_abstract():
    assert not inspect.isabstract(JumpStatement)


def test_jumpstatement_constructor_exists():
    assert callable(JumpStatement.__init__)


def test_jumpstatement_constructor_args():
    sig = inspect.signature(JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::continuestatement_is_not_abstract():
    assert not inspect.isabstract(ast::ContinueStatement)


def test_ast::continuestatement_constructor_exists():
    assert callable(ast::ContinueStatement.__init__)


def test_ast::continuestatement_constructor_args():
    sig = inspect.signature(ast::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::breakstatement_is_not_abstract():
    assert not inspect.isabstract(ast::BreakStatement)


def test_ast::breakstatement_constructor_exists():
    assert callable(ast::BreakStatement.__init__)


def test_ast::breakstatement_constructor_args():
    sig = inspect.signature(ast::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_initstatement_is_not_abstract():
    assert not inspect.isabstract(InitStatement)


def test_initstatement_constructor_exists():
    assert callable(InitStatement.__init__)


def test_initstatement_constructor_args():
    sig = inspect.signature(InitStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::staticinitstatement_is_not_abstract():
    assert not inspect.isabstract(ast::StaticInitStatement)


def test_ast::staticinitstatement_constructor_exists():
    assert callable(ast::StaticInitStatement.__init__)


def test_ast::staticinitstatement_constructor_args():
    sig = inspect.signature(ast::StaticInitStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::instanceinitstatement_is_not_abstract():
    assert not inspect.isabstract(ast::InstanceInitStatement)


def test_ast::instanceinitstatement_constructor_exists():
    assert callable(ast::InstanceInitStatement.__init__)


def test_ast::instanceinitstatement_constructor_args():
    sig = inspect.signature(ast::InstanceInitStatement.__init__)
    params = list(sig.parameters.keys())



def test_implemenationclassifierstatement_is_not_abstract():
    assert not inspect.isabstract(ImplemenationClassifierStatement)


def test_implemenationclassifierstatement_constructor_exists():
    assert callable(ImplemenationClassifierStatement.__init__)


def test_implemenationclassifierstatement_constructor_args():
    sig = inspect.signature(ImplemenationClassifierStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::enumstatement_is_not_abstract():
    assert not inspect.isabstract(ast::EnumStatement)


def test_ast::enumstatement_constructor_exists():
    assert callable(ast::EnumStatement.__init__)


def test_ast::enumstatement_constructor_args():
    sig = inspect.signature(ast::EnumStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::classstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ClassStatement)


def test_ast::classstatement_constructor_exists():
    assert callable(ast::ClassStatement.__init__)


def test_ast::classstatement_constructor_args():
    sig = inspect.signature(ast::ClassStatement.__init__)
    params = list(sig.parameters.keys())



def test_classifiermemberstatement_is_not_abstract():
    assert not inspect.isabstract(ClassifierMemberStatement)


def test_classifiermemberstatement_constructor_exists():
    assert callable(ClassifierMemberStatement.__init__)


def test_classifiermemberstatement_constructor_args():
    sig = inspect.signature(ClassifierMemberStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::feature_is_not_abstract():
    assert not inspect.isabstract(ast::Feature)


def test_ast::feature_constructor_exists():
    assert callable(ast::Feature.__init__)


def test_ast::feature_constructor_args():
    sig = inspect.signature(ast::Feature.__init__)
    params = list(sig.parameters.keys())



def test_ast::innerclassifier_is_not_abstract():
    assert not inspect.isabstract(ast::InnerClassifier)


def test_ast::innerclassifier_constructor_exists():
    assert callable(ast::InnerClassifier.__init__)


def test_ast::innerclassifier_constructor_args():
    sig = inspect.signature(ast::InnerClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ast::initstatement_is_not_abstract():
    assert not inspect.isabstract(ast::InitStatement)


def test_ast::initstatement_constructor_exists():
    assert callable(ast::InitStatement.__init__)


def test_ast::initstatement_constructor_args():
    sig = inspect.signature(ast::InitStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::enumliteral_is_not_abstract():
    assert not inspect.isabstract(ast::EnumLiteral)


def test_ast::enumliteral_constructor_exists():
    assert callable(ast::EnumLiteral.__init__)


def test_ast::enumliteral_constructor_args():
    sig = inspect.signature(ast::EnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ast::methodblock_is_not_abstract():
    assert not inspect.isabstract(ast::MethodBlock)


def test_ast::methodblock_constructor_exists():
    assert callable(ast::MethodBlock.__init__)


def test_ast::methodblock_constructor_args():
    sig = inspect.signature(ast::MethodBlock.__init__)
    params = list(sig.parameters.keys())



def test_behaviorfeature_is_not_abstract():
    assert not inspect.isabstract(BehaviorFeature)


def test_behaviorfeature_constructor_exists():
    assert callable(BehaviorFeature.__init__)


def test_behaviorfeature_constructor_args():
    sig = inspect.signature(BehaviorFeature.__init__)
    params = list(sig.parameters.keys())



def test_ast::methodstatement_is_not_abstract():
    assert not inspect.isabstract(ast::MethodStatement)


def test_ast::methodstatement_constructor_exists():
    assert callable(ast::MethodStatement.__init__)


def test_ast::methodstatement_constructor_args():
    sig = inspect.signature(ast::MethodStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::constructorstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ConstructorStatement)


def test_ast::constructorstatement_constructor_exists():
    assert callable(ast::ConstructorStatement.__init__)


def test_ast::constructorstatement_constructor_args():
    sig = inspect.signature(ast::ConstructorStatement.__init__)
    params = list(sig.parameters.keys())



def test_ejbase_is_not_abstract():
    assert not inspect.isabstract(EJBase)


def test_ejbase_constructor_exists():
    assert callable(EJBase.__init__)


def test_ejbase_constructor_args():
    sig = inspect.signature(EJBase.__init__)
    params = list(sig.parameters.keys())



def test_ast::methodcontentstatement_is_not_abstract():
    assert not inspect.isabstract(ast::MethodContentStatement)


def test_ast::methodcontentstatement_constructor_exists():
    assert callable(ast::MethodContentStatement.__init__)


def test_ast::methodcontentstatement_constructor_args():
    sig = inspect.signature(ast::MethodContentStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::catchpart_is_not_abstract():
    assert not inspect.isabstract(ast::CatchPart)


def test_ast::catchpart_constructor_exists():
    assert callable(ast::CatchPart.__init__)


def test_ast::catchpart_constructor_args():
    sig = inspect.signature(ast::CatchPart.__init__)
    params = list(sig.parameters.keys())



def test_ast::switchpart_is_not_abstract():
    assert not inspect.isabstract(ast::SwitchPart)


def test_ast::switchpart_constructor_exists():
    assert callable(ast::SwitchPart.__init__)


def test_ast::switchpart_constructor_args():
    sig = inspect.signature(ast::SwitchPart.__init__)
    params = list(sig.parameters.keys())



def test_ast::classifierstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ClassifierStatement)


def test_ast::classifierstatement_constructor_exists():
    assert callable(ast::ClassifierStatement.__init__)


def test_ast::classifierstatement_constructor_args():
    sig = inspect.signature(ast::ClassifierStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::toplevelstatement_is_not_abstract():
    assert not inspect.isabstract(ast::TopLevelStatement)


def test_ast::toplevelstatement_constructor_exists():
    assert callable(ast::TopLevelStatement.__init__)


def test_ast::toplevelstatement_constructor_args():
    sig = inspect.signature(ast::TopLevelStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::ifthenpart_is_not_abstract():
    assert not inspect.isabstract(ast::IfThenPart)


def test_ast::ifthenpart_constructor_exists():
    assert callable(ast::IfThenPart.__init__)


def test_ast::ifthenpart_constructor_args():
    sig = inspect.signature(ast::IfThenPart.__init__)
    params = list(sig.parameters.keys())



def test_ast::classifiermemberstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ClassifierMemberStatement)


def test_ast::classifiermemberstatement_constructor_exists():
    assert callable(ast::ClassifierMemberStatement.__init__)


def test_ast::classifiermemberstatement_constructor_args():
    sig = inspect.signature(ast::ClassifierMemberStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::classblock_is_not_abstract():
    assert not inspect.isabstract(ast::ClassBlock)


def test_ast::classblock_constructor_exists():
    assert callable(ast::ClassBlock.__init__)


def test_ast::classblock_constructor_args():
    sig = inspect.signature(ast::ClassBlock.__init__)
    params = list(sig.parameters.keys())



def test_ast::identifier_is_not_abstract():
    assert not inspect.isabstract(ast::Identifier)


def test_ast::identifier_constructor_exists():
    assert callable(ast::Identifier.__init__)


def test_ast::identifier_constructor_args():
    sig = inspect.signature(ast::Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "quotedValue" in params, "Missing parameter 'quotedValue'"
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "value" in params, "Missing parameter 'value'"

def test_ast::identifier_has_quotedValue():
    assert hasattr(ast::Identifier, "quotedValue")
    descriptor = None
    for klass in ast::Identifier.__mro__:
        if "quotedValue" in klass.__dict__:
            descriptor = klass.__dict__["quotedValue"]
            break
    assert isinstance(descriptor, property)

def test_ast::identifier_has_escapedValue():
    assert hasattr(ast::Identifier, "escapedValue")
    descriptor = None
    for klass in ast::Identifier.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)

def test_ast::identifier_has_value():
    assert hasattr(ast::Identifier, "value")
    descriptor = None
    for klass in ast::Identifier.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_ast::behaviorfeature_is_not_abstract():
    assert not inspect.isabstract(ast::BehaviorFeature)


def test_ast::behaviorfeature_constructor_exists():
    assert callable(ast::BehaviorFeature.__init__)


def test_ast::behaviorfeature_constructor_args():
    sig = inspect.signature(ast::BehaviorFeature.__init__)
    params = list(sig.parameters.keys())



def test_ast::fieldstatement_is_not_abstract():
    assert not inspect.isabstract(ast::FieldStatement)


def test_ast::fieldstatement_constructor_exists():
    assert callable(ast::FieldStatement.__init__)


def test_ast::fieldstatement_constructor_args():
    sig = inspect.signature(ast::FieldStatement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ast::templateparameter_is_not_abstract():
    assert not inspect.isabstract(ast::TemplateParameter)


def test_ast::templateparameter_constructor_exists():
    assert callable(ast::TemplateParameter.__init__)


def test_ast::templateparameter_constructor_args():
    sig = inspect.signature(ast::TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_ast::variable_is_not_abstract():
    assert not inspect.isabstract(ast::Variable)


def test_ast::variable_constructor_exists():
    assert callable(ast::Variable.__init__)


def test_ast::variable_constructor_args():
    sig = inspect.signature(ast::Variable.__init__)
    params = list(sig.parameters.keys())



def test_ast::parameter_is_not_abstract():
    assert not inspect.isabstract(ast::Parameter)


def test_ast::parameter_constructor_exists():
    assert callable(ast::Parameter.__init__)


def test_ast::parameter_constructor_args():
    sig = inspect.signature(ast::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_ast::expression_is_not_abstract():
    assert not inspect.isabstract(ast::Expression)


def test_ast::expression_constructor_exists():
    assert callable(ast::Expression.__init__)


def test_ast::expression_constructor_args():
    sig = inspect.signature(ast::Expression.__init__)
    params = list(sig.parameters.keys())



def test_ejelement_is_not_abstract():
    assert not inspect.isabstract(EJElement)


def test_ejelement_constructor_exists():
    assert callable(EJElement.__init__)


def test_ejelement_constructor_args():
    sig = inspect.signature(EJElement.__init__)
    params = list(sig.parameters.keys())



def test_ast::attributeset_is_not_abstract():
    assert not inspect.isabstract(ast::AttributeSet)


def test_ast::attributeset_constructor_exists():
    assert callable(ast::AttributeSet.__init__)


def test_ast::attributeset_constructor_args():
    sig = inspect.signature(ast::AttributeSet.__init__)
    params = list(sig.parameters.keys())



def test_ast::label_is_not_abstract():
    assert not inspect.isabstract(ast::Label)


def test_ast::label_constructor_exists():
    assert callable(ast::Label.__init__)


def test_ast::label_constructor_args():
    sig = inspect.signature(ast::Label.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast::label_has_name():
    assert hasattr(ast::Label, "name")
    descriptor = None
    for klass in ast::Label.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast::modifier_is_not_abstract():
    assert not inspect.isabstract(ast::Modifier)


def test_ast::modifier_constructor_exists():
    assert callable(ast::Modifier.__init__)


def test_ast::modifier_constructor_args():
    sig = inspect.signature(ast::Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ast::modifier_has_value():
    assert hasattr(ast::Modifier, "value")
    descriptor = None
    for klass in ast::Modifier.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ast::switchdefaultpartref_is_not_abstract():
    assert not inspect.isabstract(ast::SwitchDefaultPartRef)


def test_ast::switchdefaultpartref_constructor_exists():
    assert callable(ast::SwitchDefaultPartRef.__init__)


def test_ast::switchdefaultpartref_constructor_args():
    sig = inspect.signature(ast::SwitchDefaultPartRef.__init__)
    params = list(sig.parameters.keys())



def test_ast::documentationline_is_not_abstract():
    assert not inspect.isabstract(ast::DocumentationLine)


def test_ast::documentationline_constructor_exists():
    assert callable(ast::DocumentationLine.__init__)


def test_ast::documentationline_constructor_args():
    sig = inspect.signature(ast::DocumentationLine.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_ast::documentationline_has_text():
    assert hasattr(ast::DocumentationLine, "text")
    descriptor = None
    for klass in ast::DocumentationLine.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_ast::ejbase_is_not_abstract():
    assert not inspect.isabstract(ast::EJBase)


def test_ast::ejbase_constructor_exists():
    assert callable(ast::EJBase.__init__)


def test_ast::ejbase_constructor_args():
    sig = inspect.signature(ast::EJBase.__init__)
    params = list(sig.parameters.keys())



def test_ast::ejelement_is_not_abstract():
    assert not inspect.isabstract(ast::EJElement)


def test_ast::ejelement_constructor_exists():
    assert callable(ast::EJElement.__init__)


def test_ast::ejelement_constructor_args():
    sig = inspect.signature(ast::EJElement.__init__)
    params = list(sig.parameters.keys())
    assert "endLine" in params, "Missing parameter 'endLine'"
    assert "startOffset" in params, "Missing parameter 'startOffset'"
    assert "startColumn" in params, "Missing parameter 'startColumn'"
    assert "endColumn" in params, "Missing parameter 'endColumn'"
    assert "startLine" in params, "Missing parameter 'startLine'"
    assert "endOffset" in params, "Missing parameter 'endOffset'"

def test_ast::ejelement_has_endLine():
    assert hasattr(ast::EJElement, "endLine")
    descriptor = None
    for klass in ast::EJElement.__mro__:
        if "endLine" in klass.__dict__:
            descriptor = klass.__dict__["endLine"]
            break
    assert isinstance(descriptor, property)

def test_ast::ejelement_has_startOffset():
    assert hasattr(ast::EJElement, "startOffset")
    descriptor = None
    for klass in ast::EJElement.__mro__:
        if "startOffset" in klass.__dict__:
            descriptor = klass.__dict__["startOffset"]
            break
    assert isinstance(descriptor, property)

def test_ast::ejelement_has_startColumn():
    assert hasattr(ast::EJElement, "startColumn")
    descriptor = None
    for klass in ast::EJElement.__mro__:
        if "startColumn" in klass.__dict__:
            descriptor = klass.__dict__["startColumn"]
            break
    assert isinstance(descriptor, property)

def test_ast::ejelement_has_endColumn():
    assert hasattr(ast::EJElement, "endColumn")
    descriptor = None
    for klass in ast::EJElement.__mro__:
        if "endColumn" in klass.__dict__:
            descriptor = klass.__dict__["endColumn"]
            break
    assert isinstance(descriptor, property)

def test_ast::ejelement_has_startLine():
    assert hasattr(ast::EJElement, "startLine")
    descriptor = None
    for klass in ast::EJElement.__mro__:
        if "startLine" in klass.__dict__:
            descriptor = klass.__dict__["startLine"]
            break
    assert isinstance(descriptor, property)

def test_ast::ejelement_has_endOffset():
    assert hasattr(ast::EJElement, "endOffset")
    descriptor = None
    for klass in ast::EJElement.__mro__:
        if "endOffset" in klass.__dict__:
            descriptor = klass.__dict__["endOffset"]
            break
    assert isinstance(descriptor, property)



def test_ast::attributedefinition_is_not_abstract():
    assert not inspect.isabstract(ast::AttributeDefinition)


def test_ast::attributedefinition_constructor_exists():
    assert callable(ast::AttributeDefinition.__init__)


def test_ast::attributedefinition_constructor_args():
    sig = inspect.signature(ast::AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ast::emptystatement_is_not_abstract():
    assert not inspect.isabstract(ast::EmptyStatement)


def test_ast::emptystatement_constructor_exists():
    assert callable(ast::EmptyStatement.__init__)


def test_ast::emptystatement_constructor_args():
    sig = inspect.signature(ast::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::wildcardtype_is_not_abstract():
    assert not inspect.isabstract(ast::WildcardType)


def test_ast::wildcardtype_constructor_exists():
    assert callable(ast::WildcardType.__init__)


def test_ast::wildcardtype_constructor_args():
    sig = inspect.signature(ast::WildcardType.__init__)
    params = list(sig.parameters.keys())



def test_ast::rangeexpression_is_not_abstract():
    assert not inspect.isabstract(ast::RangeExpression)


def test_ast::rangeexpression_constructor_exists():
    assert callable(ast::RangeExpression.__init__)


def test_ast::rangeexpression_constructor_args():
    sig = inspect.signature(ast::RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast::assertstatement_is_not_abstract():
    assert not inspect.isabstract(ast::AssertStatement)


def test_ast::assertstatement_constructor_exists():
    assert callable(ast::AssertStatement.__init__)


def test_ast::assertstatement_constructor_args():
    sig = inspect.signature(ast::AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::namedelement_is_not_abstract():
    assert not inspect.isabstract(ast::NamedElement)


def test_ast::namedelement_constructor_exists():
    assert callable(ast::NamedElement.__init__)


def test_ast::namedelement_constructor_args():
    sig = inspect.signature(ast::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ast::unaryop_is_not_abstract():
    assert not inspect.isabstract(ast::UnaryOp)


def test_ast::unaryop_constructor_exists():
    assert callable(ast::UnaryOp.__init__)


def test_ast::unaryop_constructor_args():
    sig = inspect.signature(ast::UnaryOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::unaryminusop_is_not_abstract():
    assert not inspect.isabstract(ast::UnaryMinusOp)


def test_ast::unaryminusop_constructor_exists():
    assert callable(ast::UnaryMinusOp.__init__)


def test_ast::unaryminusop_constructor_args():
    sig = inspect.signature(ast::UnaryMinusOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::thisreference_is_not_abstract():
    assert not inspect.isabstract(ast::ThisReference)


def test_ast::thisreference_constructor_exists():
    assert callable(ast::ThisReference.__init__)


def test_ast::thisreference_constructor_args():
    sig = inspect.signature(ast::ThisReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast::thisreference_has_name():
    assert hasattr(ast::ThisReference, "name")
    descriptor = None
    for klass in ast::ThisReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast::superreference_is_not_abstract():
    assert not inspect.isabstract(ast::SuperReference)


def test_ast::superreference_constructor_exists():
    assert callable(ast::SuperReference.__init__)


def test_ast::superreference_constructor_args():
    sig = inspect.signature(ast::SuperReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast::superreference_has_name():
    assert hasattr(ast::SuperReference, "name")
    descriptor = None
    for klass in ast::SuperReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast::shiftop_is_not_abstract():
    assert not inspect.isabstract(ast::ShiftOp)


def test_ast::shiftop_constructor_exists():
    assert callable(ast::ShiftOp.__init__)


def test_ast::shiftop_constructor_args():
    sig = inspect.signature(ast::ShiftOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::rightshiftassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast::RightShiftAssignmentOp)


def test_ast::rightshiftassignmentop_constructor_exists():
    assert callable(ast::RightShiftAssignmentOp.__init__)


def test_ast::rightshiftassignmentop_constructor_args():
    sig = inspect.signature(ast::RightShiftAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::returnstatement_is_not_abstract():
    assert not inspect.isabstract(ast::ReturnStatement)


def test_ast::returnstatement_constructor_exists():
    assert callable(ast::ReturnStatement.__init__)


def test_ast::returnstatement_constructor_args():
    sig = inspect.signature(ast::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast::remainderassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast::RemainderAssignmentOp)


def test_ast::remainderassignmentop_constructor_exists():
    assert callable(ast::RemainderAssignmentOp.__init__)


def test_ast::remainderassignmentop_constructor_args():
    sig = inspect.signature(ast::RemainderAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::primitivetype_is_not_abstract():
    assert not inspect.isabstract(ast::PrimitiveType)


def test_ast::primitivetype_constructor_exists():
    assert callable(ast::PrimitiveType.__init__)


def test_ast::primitivetype_constructor_args():
    sig = inspect.signature(ast::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast::primitivetype_has_name():
    assert hasattr(ast::PrimitiveType, "name")
    descriptor = None
    for klass in ast::PrimitiveType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast::prefixincrementop_is_not_abstract():
    assert not inspect.isabstract(ast::PrefixIncrementOp)


def test_ast::prefixincrementop_constructor_exists():
    assert callable(ast::PrefixIncrementOp.__init__)


def test_ast::prefixincrementop_constructor_args():
    sig = inspect.signature(ast::PrefixIncrementOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::prefixdecrementop_is_not_abstract():
    assert not inspect.isabstract(ast::PrefixDecrementOp)


def test_ast::prefixdecrementop_constructor_exists():
    assert callable(ast::PrefixDecrementOp.__init__)


def test_ast::prefixdecrementop_constructor_args():
    sig = inspect.signature(ast::PrefixDecrementOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::postfixincrementop_is_not_abstract():
    assert not inspect.isabstract(ast::PostfixIncrementOp)


def test_ast::postfixincrementop_constructor_exists():
    assert callable(ast::PostfixIncrementOp.__init__)


def test_ast::postfixincrementop_constructor_args():
    sig = inspect.signature(ast::PostfixIncrementOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::zeroextensionrightshiftassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast::ZeroExtensionRightShiftAssignmentOp)


def test_ast::zeroextensionrightshiftassignmentop_constructor_exists():
    assert callable(ast::ZeroExtensionRightShiftAssignmentOp.__init__)


def test_ast::zeroextensionrightshiftassignmentop_constructor_args():
    sig = inspect.signature(ast::ZeroExtensionRightShiftAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::unaryplusop_is_not_abstract():
    assert not inspect.isabstract(ast::UnaryPlusOp)


def test_ast::unaryplusop_constructor_exists():
    assert callable(ast::UnaryPlusOp.__init__)


def test_ast::unaryplusop_constructor_args():
    sig = inspect.signature(ast::UnaryPlusOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::newop_is_not_abstract():
    assert not inspect.isabstract(ast::NewOp)


def test_ast::newop_constructor_exists():
    assert callable(ast::NewOp.__init__)


def test_ast::newop_constructor_args():
    sig = inspect.signature(ast::NewOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::multiplyassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast::MultiplyAssignmentOp)


def test_ast::multiplyassignmentop_constructor_exists():
    assert callable(ast::MultiplyAssignmentOp.__init__)


def test_ast::multiplyassignmentop_constructor_args():
    sig = inspect.signature(ast::MultiplyAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::multiplyop_is_not_abstract():
    assert not inspect.isabstract(ast::MultiplyOp)


def test_ast::multiplyop_constructor_exists():
    assert callable(ast::MultiplyOp.__init__)


def test_ast::multiplyop_constructor_args():
    sig = inspect.signature(ast::MultiplyOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::minusop_is_not_abstract():
    assert not inspect.isabstract(ast::MinusOp)


def test_ast::minusop_constructor_exists():
    assert callable(ast::MinusOp.__init__)


def test_ast::minusop_constructor_args():
    sig = inspect.signature(ast::MinusOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::minusassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast::MinusAssignmentOp)


def test_ast::minusassignmentop_constructor_exists():
    assert callable(ast::MinusAssignmentOp.__init__)


def test_ast::minusassignmentop_constructor_args():
    sig = inspect.signature(ast::MinusAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::logicalcomplementop_is_not_abstract():
    assert not inspect.isabstract(ast::LogicalComplementOp)


def test_ast::logicalcomplementop_constructor_exists():
    assert callable(ast::LogicalComplementOp.__init__)


def test_ast::logicalcomplementop_constructor_args():
    sig = inspect.signature(ast::LogicalComplementOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::literal_is_not_abstract():
    assert not inspect.isabstract(ast::Literal)


def test_ast::literal_constructor_exists():
    assert callable(ast::Literal.__init__)


def test_ast::literal_constructor_args():
    sig = inspect.signature(ast::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ast::literal_has_value():
    assert hasattr(ast::Literal, "value")
    descriptor = None
    for klass in ast::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ast::lessthenop_is_not_abstract():
    assert not inspect.isabstract(ast::LessThenOp)


def test_ast::lessthenop_constructor_exists():
    assert callable(ast::LessThenOp.__init__)


def test_ast::lessthenop_constructor_args():
    sig = inspect.signature(ast::LessThenOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::lessorequalop_is_not_abstract():
    assert not inspect.isabstract(ast::LessOrEqualOp)


def test_ast::lessorequalop_constructor_exists():
    assert callable(ast::LessOrEqualOp.__init__)


def test_ast::lessorequalop_constructor_args():
    sig = inspect.signature(ast::LessOrEqualOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::postfixdecrementop_is_not_abstract():
    assert not inspect.isabstract(ast::PostfixDecrementOp)


def test_ast::postfixdecrementop_constructor_exists():
    assert callable(ast::PostfixDecrementOp.__init__)


def test_ast::postfixdecrementop_constructor_args():
    sig = inspect.signature(ast::PostfixDecrementOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::plusop_is_not_abstract():
    assert not inspect.isabstract(ast::PlusOp)


def test_ast::plusop_constructor_exists():
    assert callable(ast::PlusOp.__init__)


def test_ast::plusop_constructor_args():
    sig = inspect.signature(ast::PlusOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::plusassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast::PlusAssignmentOp)


def test_ast::plusassignmentop_constructor_exists():
    assert callable(ast::PlusAssignmentOp.__init__)


def test_ast::plusassignmentop_constructor_args():
    sig = inspect.signature(ast::PlusAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::notequalop_is_not_abstract():
    assert not inspect.isabstract(ast::NotEqualOp)


def test_ast::notequalop_constructor_exists():
    assert callable(ast::NotEqualOp.__init__)


def test_ast::notequalop_constructor_args():
    sig = inspect.signature(ast::NotEqualOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::identityop_is_not_abstract():
    assert not inspect.isabstract(ast::IdentityOp)


def test_ast::identityop_constructor_exists():
    assert callable(ast::IdentityOp.__init__)


def test_ast::identityop_constructor_args():
    sig = inspect.signature(ast::IdentityOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::greaterthenop_is_not_abstract():
    assert not inspect.isabstract(ast::GreaterThenOp)


def test_ast::greaterthenop_constructor_exists():
    assert callable(ast::GreaterThenOp.__init__)


def test_ast::greaterthenop_constructor_args():
    sig = inspect.signature(ast::GreaterThenOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::greaterorequalop_is_not_abstract():
    assert not inspect.isabstract(ast::GreaterOrEqualOp)


def test_ast::greaterorequalop_constructor_exists():
    assert callable(ast::GreaterOrEqualOp.__init__)


def test_ast::greaterorequalop_constructor_args():
    sig = inspect.signature(ast::GreaterOrEqualOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::equalop_is_not_abstract():
    assert not inspect.isabstract(ast::EqualOp)


def test_ast::equalop_constructor_exists():
    assert callable(ast::EqualOp.__init__)


def test_ast::equalop_constructor_args():
    sig = inspect.signature(ast::EqualOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::divisionop_is_not_abstract():
    assert not inspect.isabstract(ast::DivisionOp)


def test_ast::divisionop_constructor_exists():
    assert callable(ast::DivisionOp.__init__)


def test_ast::divisionop_constructor_args():
    sig = inspect.signature(ast::DivisionOp.__init__)
    params = list(sig.parameters.keys())



def test_divisionop_is_not_abstract():
    assert not inspect.isabstract(DivisionOp)


def test_divisionop_constructor_exists():
    assert callable(DivisionOp.__init__)


def test_divisionop_constructor_args():
    sig = inspect.signature(DivisionOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::remainderop_is_not_abstract():
    assert not inspect.isabstract(ast::RemainderOp)


def test_ast::remainderop_constructor_exists():
    assert callable(ast::RemainderOp.__init__)


def test_ast::remainderop_constructor_args():
    sig = inspect.signature(ast::RemainderOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::divideop_is_not_abstract():
    assert not inspect.isabstract(ast::DivideOp)


def test_ast::divideop_constructor_exists():
    assert callable(ast::DivideOp.__init__)


def test_ast::divideop_constructor_args():
    sig = inspect.signature(ast::DivideOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::divideassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast::DivideAssignmentOp)


def test_ast::divideassignmentop_constructor_exists():
    assert callable(ast::DivideAssignmentOp.__init__)


def test_ast::divideassignmentop_constructor_args():
    sig = inspect.signature(ast::DivideAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::conditionalorop_is_not_abstract():
    assert not inspect.isabstract(ast::ConditionalOrOp)


def test_ast::conditionalorop_constructor_exists():
    assert callable(ast::ConditionalOrOp.__init__)


def test_ast::conditionalorop_constructor_args():
    sig = inspect.signature(ast::ConditionalOrOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::conditionalop_is_not_abstract():
    assert not inspect.isabstract(ast::ConditionalOp)


def test_ast::conditionalop_constructor_exists():
    assert callable(ast::ConditionalOp.__init__)


def test_ast::conditionalop_constructor_args():
    sig = inspect.signature(ast::ConditionalOp.__init__)
    params = list(sig.parameters.keys())



def test_shiftop_is_not_abstract():
    assert not inspect.isabstract(ShiftOp)


def test_shiftop_constructor_exists():
    assert callable(ShiftOp.__init__)


def test_shiftop_constructor_args():
    sig = inspect.signature(ShiftOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::rightshiftop_is_not_abstract():
    assert not inspect.isabstract(ast::RightShiftOp)


def test_ast::rightshiftop_constructor_exists():
    assert callable(ast::RightShiftOp.__init__)


def test_ast::rightshiftop_constructor_args():
    sig = inspect.signature(ast::RightShiftOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::zeroextensionrightshiftop_is_not_abstract():
    assert not inspect.isabstract(ast::ZeroExtensionRightShiftOp)


def test_ast::zeroextensionrightshiftop_constructor_exists():
    assert callable(ast::ZeroExtensionRightShiftOp.__init__)


def test_ast::zeroextensionrightshiftop_constructor_args():
    sig = inspect.signature(ast::ZeroExtensionRightShiftOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::leftshiftop_is_not_abstract():
    assert not inspect.isabstract(ast::LeftShiftOp)


def test_ast::leftshiftop_constructor_exists():
    assert callable(ast::LeftShiftOp.__init__)


def test_ast::leftshiftop_constructor_args():
    sig = inspect.signature(ast::LeftShiftOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::leftshiftassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast::LeftShiftAssignmentOp)


def test_ast::leftshiftassignmentop_constructor_exists():
    assert callable(ast::LeftShiftAssignmentOp.__init__)


def test_ast::leftshiftassignmentop_constructor_args():
    sig = inspect.signature(ast::LeftShiftAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_classifierop_is_not_abstract():
    assert not inspect.isabstract(ClassifierOp)


def test_classifierop_constructor_exists():
    assert callable(ClassifierOp.__init__)


def test_classifierop_constructor_args():
    sig = inspect.signature(ClassifierOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::instanceofop_is_not_abstract():
    assert not inspect.isabstract(ast::InstanceOfOp)


def test_ast::instanceofop_constructor_exists():
    assert callable(ast::InstanceOfOp.__init__)


def test_ast::instanceofop_constructor_args():
    sig = inspect.signature(ast::InstanceOfOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::castop_is_not_abstract():
    assert not inspect.isabstract(ast::CastOp)


def test_ast::castop_constructor_exists():
    assert callable(ast::CastOp.__init__)


def test_ast::castop_constructor_args():
    sig = inspect.signature(ast::CastOp.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_ast::floatliteral_is_not_abstract():
    assert not inspect.isabstract(ast::FloatLiteral)


def test_ast::floatliteral_constructor_exists():
    assert callable(ast::FloatLiteral.__init__)


def test_ast::floatliteral_constructor_args():
    sig = inspect.signature(ast::FloatLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ast::longintegerliteral_is_not_abstract():
    assert not inspect.isabstract(ast::LongIntegerLiteral)


def test_ast::longintegerliteral_constructor_exists():
    assert callable(ast::LongIntegerLiteral.__init__)


def test_ast::longintegerliteral_constructor_args():
    sig = inspect.signature(ast::LongIntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ast::integerliteral_is_not_abstract():
    assert not inspect.isabstract(ast::IntegerLiteral)


def test_ast::integerliteral_constructor_exists():
    assert callable(ast::IntegerLiteral.__init__)


def test_ast::integerliteral_constructor_args():
    sig = inspect.signature(ast::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ast::doubleliteral_is_not_abstract():
    assert not inspect.isabstract(ast::DoubleLiteral)


def test_ast::doubleliteral_constructor_exists():
    assert callable(ast::DoubleLiteral.__init__)


def test_ast::doubleliteral_constructor_args():
    sig = inspect.signature(ast::DoubleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ast::characterliteral_is_not_abstract():
    assert not inspect.isabstract(ast::CharacterLiteral)


def test_ast::characterliteral_constructor_exists():
    assert callable(ast::CharacterLiteral.__init__)


def test_ast::characterliteral_constructor_args():
    sig = inspect.signature(ast::CharacterLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ast::stringliteral_is_not_abstract():
    assert not inspect.isabstract(ast::StringLiteral)


def test_ast::stringliteral_constructor_exists():
    assert callable(ast::StringLiteral.__init__)


def test_ast::stringliteral_constructor_args():
    sig = inspect.signature(ast::StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ast::nullreference_is_not_abstract():
    assert not inspect.isabstract(ast::NullReference)


def test_ast::nullreference_constructor_exists():
    assert callable(ast::NullReference.__init__)


def test_ast::nullreference_constructor_args():
    sig = inspect.signature(ast::NullReference.__init__)
    params = list(sig.parameters.keys())



def test_ast::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(ast::BooleanLiteral)


def test_ast::booleanliteral_constructor_exists():
    assert callable(ast::BooleanLiteral.__init__)


def test_ast::booleanliteral_constructor_args():
    sig = inspect.signature(ast::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ast::bitwisexorop_is_not_abstract():
    assert not inspect.isabstract(ast::BitwiseXorOp)


def test_ast::bitwisexorop_constructor_exists():
    assert callable(ast::BitwiseXorOp.__init__)


def test_ast::bitwisexorop_constructor_args():
    sig = inspect.signature(ast::BitwiseXorOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::bitwisexorassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast::BitwiseXorAssignmentOp)


def test_ast::bitwisexorassignmentop_constructor_exists():
    assert callable(ast::BitwiseXorAssignmentOp.__init__)


def test_ast::bitwisexorassignmentop_constructor_args():
    sig = inspect.signature(ast::BitwiseXorAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast::bitwiseorop_is_not_abstract():
    assert not inspect.isabstract(ast::BitwiseOrOp)


def test_ast::bitwiseorop_constructor_exists():
    assert callable(ast::BitwiseOrOp.__init__)


def test_ast::bitwiseorop_constructor_args():
    sig = inspect.signature(ast::BitwiseOrOp.__init__)
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
UnaryOp_strategy = st.builds(
    UnaryOp,
)
ast::BitwiseComplementOp_strategy = st.builds(
    ast::BitwiseComplementOp,
)
BinaryOp_strategy = st.builds(
    BinaryOp,
)
ast::BitwiseAndOp_strategy = st.builds(
    ast::BitwiseAndOp,
)
AssignmentOperation_strategy = st.builds(
    AssignmentOperation,
)
ast::BitwiseOrAssignmentOp_strategy = st.builds(
    ast::BitwiseOrAssignmentOp,
)
ast::BitwiseAndAssignmentOp_strategy = st.builds(
    ast::BitwiseAndAssignmentOp,
)
ast::AssignmentOp_strategy = st.builds(
    ast::AssignmentOp,
)
ast::ConditionalAndOp_strategy = st.builds(
    ast::ConditionalAndOp,
)
Expression_strategy = st.builds(
    Expression,
)
ast::ArrayConstructor_strategy = st.builds(
    ast::ArrayConstructor,
)
ast::AssignmentOperation_strategy = st.builds(
    ast::AssignmentOperation,
)
ast::ClassifierOp_strategy = st.builds(
    ast::ClassifierOp,
)
ast::ApplyRoundOp_strategy = st.builds(
    ast::ApplyRoundOp,
)
ast::BinaryOp_strategy = st.builds(
    ast::BinaryOp,
)
ast::AccessOp_strategy = st.builds(
    ast::AccessOp,
)
ScopeStatement_strategy = st.builds(
    ScopeStatement,
)
ast::TryStatement_strategy = st.builds(
    ast::TryStatement,
)
ast::SynchronizedStatement_strategy = st.builds(
    ast::SynchronizedStatement,
)
ast::ApplySquareOp_strategy = st.builds(
    ast::ApplySquareOp,
)
LabeledStatement_strategy = st.builds(
    LabeledStatement,
)
ast::SwitchStatement_strategy = st.builds(
    ast::SwitchStatement,
)
ast::LoopStatement_strategy = st.builds(
    ast::LoopStatement,
)
SwitchPart_strategy = st.builds(
    SwitchPart,
)
ast::SwitchDefaultPart_strategy = st.builds(
    ast::SwitchDefaultPart,
)
ast::SwitchCasePart_strategy = st.builds(
    ast::SwitchCasePart,
)
MethodContentStatement_strategy = st.builds(
    MethodContentStatement,
)
ast::ThrowStatement_strategy = st.builds(
    ast::ThrowStatement,
)
ast::ScopeStatement_strategy = st.builds(
    ast::ScopeStatement,
)
ast::JumpStatement_strategy = st.builds(
    ast::JumpStatement,
)
ast::IfStatement_strategy = st.builds(
    ast::IfStatement,
)
ast::LocalVarStatement_strategy = st.builds(
    ast::LocalVarStatement,
)
ast::MethodClassifier_strategy = st.builds(
    ast::MethodClassifier,
)
ast::LabeledStatement_strategy = st.builds(
    ast::LabeledStatement,
)
ast::ExpressionStatement_strategy = st.builds(
    ast::ExpressionStatement,
)
ConditionalLoop_strategy = st.builds(
    ConditionalLoop,
)
ast::ForStatement_strategy = st.builds(
    ast::ForStatement,
)
ast::WhileStatement_strategy = st.builds(
    ast::WhileStatement,
)
ast::DoWhileStatement_strategy = st.builds(
    ast::DoWhileStatement,
)
TopLevelStatement_strategy = st.builds(
    TopLevelStatement,
)
ast::TopLevelClassifier_strategy = st.builds(
    ast::TopLevelClassifier,
)
ast::PackageStatement_strategy = st.builds(
    ast::PackageStatement,
)
ast::ImportStatement_strategy = st.builds(
    ast::ImportStatement,
)
ClassifierStatement_strategy = st.builds(
    ClassifierStatement,
)
ast::InterfaceStatement_strategy = st.builds(
    ast::InterfaceStatement,
)
ast::ImplemenationClassifierStatement_strategy = st.builds(
    ast::ImplemenationClassifierStatement,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
ast::ForeachStatement_strategy = st.builds(
    ast::ForeachStatement,
)
ast::ConditionalLoop_strategy = st.builds(
    ast::ConditionalLoop,
)
JumpStatement_strategy = st.builds(
    JumpStatement,
)
ast::ContinueStatement_strategy = st.builds(
    ast::ContinueStatement,
)
ast::BreakStatement_strategy = st.builds(
    ast::BreakStatement,
)
InitStatement_strategy = st.builds(
    InitStatement,
)
ast::StaticInitStatement_strategy = st.builds(
    ast::StaticInitStatement,
)
ast::InstanceInitStatement_strategy = st.builds(
    ast::InstanceInitStatement,
)
ImplemenationClassifierStatement_strategy = st.builds(
    ImplemenationClassifierStatement,
)
ast::EnumStatement_strategy = st.builds(
    ast::EnumStatement,
)
ast::ClassStatement_strategy = st.builds(
    ast::ClassStatement,
)
ClassifierMemberStatement_strategy = st.builds(
    ClassifierMemberStatement,
)
ast::Feature_strategy = st.builds(
    ast::Feature,
)
ast::InnerClassifier_strategy = st.builds(
    ast::InnerClassifier,
)
ast::InitStatement_strategy = st.builds(
    ast::InitStatement,
)
ast::EnumLiteral_strategy = st.builds(
    ast::EnumLiteral,
)
ast::MethodBlock_strategy = st.builds(
    ast::MethodBlock,
)
BehaviorFeature_strategy = st.builds(
    BehaviorFeature,
)
ast::MethodStatement_strategy = st.builds(
    ast::MethodStatement,
)
ast::ConstructorStatement_strategy = st.builds(
    ast::ConstructorStatement,
)
EJBase_strategy = st.builds(
    EJBase,
)
ast::MethodContentStatement_strategy = st.builds(
    ast::MethodContentStatement,
)
ast::CatchPart_strategy = st.builds(
    ast::CatchPart,
)
ast::SwitchPart_strategy = st.builds(
    ast::SwitchPart,
)
ast::ClassifierStatement_strategy = st.builds(
    ast::ClassifierStatement,
)
ast::TopLevelStatement_strategy = st.builds(
    ast::TopLevelStatement,
)
ast::IfThenPart_strategy = st.builds(
    ast::IfThenPart,
)
ast::ClassifierMemberStatement_strategy = st.builds(
    ast::ClassifierMemberStatement,
)
ast::ClassBlock_strategy = st.builds(
    ast::ClassBlock,
)
ast::Identifier_strategy = st.builds(
    ast::Identifier,
    quotedValue=
        safe_text,
    escapedValue=
        safe_text,
    value=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
ast::BehaviorFeature_strategy = st.builds(
    ast::BehaviorFeature,
)
ast::FieldStatement_strategy = st.builds(
    ast::FieldStatement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ast::TemplateParameter_strategy = st.builds(
    ast::TemplateParameter,
)
ast::Variable_strategy = st.builds(
    ast::Variable,
)
ast::Parameter_strategy = st.builds(
    ast::Parameter,
)
ast::Expression_strategy = st.builds(
    ast::Expression,
)
EJElement_strategy = st.builds(
    EJElement,
)
ast::AttributeSet_strategy = st.builds(
    ast::AttributeSet,
)
ast::Label_strategy = st.builds(
    ast::Label,
    name=
        safe_text
)
ast::Modifier_strategy = st.builds(
    ast::Modifier,
    value=
        safe_text
)
ast::SwitchDefaultPartRef_strategy = st.builds(
    ast::SwitchDefaultPartRef,
)
ast::DocumentationLine_strategy = st.builds(
    ast::DocumentationLine,
    text=
        safe_text
)
ast::EJBase_strategy = st.builds(
    ast::EJBase,
)
ast::EJElement_strategy = st.builds(
    ast::EJElement,
    endLine=
        st.integers(),
    startOffset=
        safe_text,
    startColumn=
        st.integers(),
    endColumn=
        st.integers(),
    startLine=
        st.integers(),
    endOffset=
        safe_text
)
ast::AttributeDefinition_strategy = st.builds(
    ast::AttributeDefinition,
)
ast::EmptyStatement_strategy = st.builds(
    ast::EmptyStatement,
)
ast::WildcardType_strategy = st.builds(
    ast::WildcardType,
)
ast::RangeExpression_strategy = st.builds(
    ast::RangeExpression,
)
ast::AssertStatement_strategy = st.builds(
    ast::AssertStatement,
)
ast::NamedElement_strategy = st.builds(
    ast::NamedElement,
)
ast::UnaryOp_strategy = st.builds(
    ast::UnaryOp,
)
ast::UnaryMinusOp_strategy = st.builds(
    ast::UnaryMinusOp,
)
ast::ThisReference_strategy = st.builds(
    ast::ThisReference,
    name=
        safe_text
)
ast::SuperReference_strategy = st.builds(
    ast::SuperReference,
    name=
        safe_text
)
ast::ShiftOp_strategy = st.builds(
    ast::ShiftOp,
)
ast::RightShiftAssignmentOp_strategy = st.builds(
    ast::RightShiftAssignmentOp,
)
ast::ReturnStatement_strategy = st.builds(
    ast::ReturnStatement,
)
ast::RemainderAssignmentOp_strategy = st.builds(
    ast::RemainderAssignmentOp,
)
ast::PrimitiveType_strategy = st.builds(
    ast::PrimitiveType,
    name=
        safe_text
)
ast::PrefixIncrementOp_strategy = st.builds(
    ast::PrefixIncrementOp,
)
ast::PrefixDecrementOp_strategy = st.builds(
    ast::PrefixDecrementOp,
)
ast::PostfixIncrementOp_strategy = st.builds(
    ast::PostfixIncrementOp,
)
ast::ZeroExtensionRightShiftAssignmentOp_strategy = st.builds(
    ast::ZeroExtensionRightShiftAssignmentOp,
)
ast::UnaryPlusOp_strategy = st.builds(
    ast::UnaryPlusOp,
)
ast::NewOp_strategy = st.builds(
    ast::NewOp,
)
ast::MultiplyAssignmentOp_strategy = st.builds(
    ast::MultiplyAssignmentOp,
)
ast::MultiplyOp_strategy = st.builds(
    ast::MultiplyOp,
)
ast::MinusOp_strategy = st.builds(
    ast::MinusOp,
)
ast::MinusAssignmentOp_strategy = st.builds(
    ast::MinusAssignmentOp,
)
ast::LogicalComplementOp_strategy = st.builds(
    ast::LogicalComplementOp,
)
ast::Literal_strategy = st.builds(
    ast::Literal,
    value=
        safe_text
)
ast::LessThenOp_strategy = st.builds(
    ast::LessThenOp,
)
ast::LessOrEqualOp_strategy = st.builds(
    ast::LessOrEqualOp,
)
ast::PostfixDecrementOp_strategy = st.builds(
    ast::PostfixDecrementOp,
)
ast::PlusOp_strategy = st.builds(
    ast::PlusOp,
)
ast::PlusAssignmentOp_strategy = st.builds(
    ast::PlusAssignmentOp,
)
ast::NotEqualOp_strategy = st.builds(
    ast::NotEqualOp,
)
ast::IdentityOp_strategy = st.builds(
    ast::IdentityOp,
)
ast::GreaterThenOp_strategy = st.builds(
    ast::GreaterThenOp,
)
ast::GreaterOrEqualOp_strategy = st.builds(
    ast::GreaterOrEqualOp,
)
ast::EqualOp_strategy = st.builds(
    ast::EqualOp,
)
ast::DivisionOp_strategy = st.builds(
    ast::DivisionOp,
)
DivisionOp_strategy = st.builds(
    DivisionOp,
)
ast::RemainderOp_strategy = st.builds(
    ast::RemainderOp,
)
ast::DivideOp_strategy = st.builds(
    ast::DivideOp,
)
ast::DivideAssignmentOp_strategy = st.builds(
    ast::DivideAssignmentOp,
)
ast::ConditionalOrOp_strategy = st.builds(
    ast::ConditionalOrOp,
)
ast::ConditionalOp_strategy = st.builds(
    ast::ConditionalOp,
)
ShiftOp_strategy = st.builds(
    ShiftOp,
)
ast::RightShiftOp_strategy = st.builds(
    ast::RightShiftOp,
)
ast::ZeroExtensionRightShiftOp_strategy = st.builds(
    ast::ZeroExtensionRightShiftOp,
)
ast::LeftShiftOp_strategy = st.builds(
    ast::LeftShiftOp,
)
ast::LeftShiftAssignmentOp_strategy = st.builds(
    ast::LeftShiftAssignmentOp,
)
ClassifierOp_strategy = st.builds(
    ClassifierOp,
)
ast::InstanceOfOp_strategy = st.builds(
    ast::InstanceOfOp,
)
ast::CastOp_strategy = st.builds(
    ast::CastOp,
)
Literal_strategy = st.builds(
    Literal,
)
ast::FloatLiteral_strategy = st.builds(
    ast::FloatLiteral,
)
ast::LongIntegerLiteral_strategy = st.builds(
    ast::LongIntegerLiteral,
)
ast::IntegerLiteral_strategy = st.builds(
    ast::IntegerLiteral,
)
ast::DoubleLiteral_strategy = st.builds(
    ast::DoubleLiteral,
)
ast::CharacterLiteral_strategy = st.builds(
    ast::CharacterLiteral,
)
ast::StringLiteral_strategy = st.builds(
    ast::StringLiteral,
)
ast::NullReference_strategy = st.builds(
    ast::NullReference,
)
ast::BooleanLiteral_strategy = st.builds(
    ast::BooleanLiteral,
)
ast::BitwiseXorOp_strategy = st.builds(
    ast::BitwiseXorOp,
)
ast::BitwiseXorAssignmentOp_strategy = st.builds(
    ast::BitwiseXorAssignmentOp,
)
ast::BitwiseOrOp_strategy = st.builds(
    ast::BitwiseOrOp,
)

@given(instance=UnaryOp_strategy)
@settings(max_examples=50)
def test_unaryop_instantiation(instance):
    assert isinstance(instance, UnaryOp)

@given(instance=ast::BitwiseComplementOp_strategy)
@settings(max_examples=50)
def test_ast::bitwisecomplementop_instantiation(instance):
    assert isinstance(instance, ast::BitwiseComplementOp)

@given(instance=BinaryOp_strategy)
@settings(max_examples=50)
def test_binaryop_instantiation(instance):
    assert isinstance(instance, BinaryOp)

@given(instance=ast::BitwiseAndOp_strategy)
@settings(max_examples=50)
def test_ast::bitwiseandop_instantiation(instance):
    assert isinstance(instance, ast::BitwiseAndOp)

@given(instance=AssignmentOperation_strategy)
@settings(max_examples=50)
def test_assignmentoperation_instantiation(instance):
    assert isinstance(instance, AssignmentOperation)

@given(instance=ast::BitwiseOrAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast::bitwiseorassignmentop_instantiation(instance):
    assert isinstance(instance, ast::BitwiseOrAssignmentOp)

@given(instance=ast::BitwiseAndAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast::bitwiseandassignmentop_instantiation(instance):
    assert isinstance(instance, ast::BitwiseAndAssignmentOp)

@given(instance=ast::AssignmentOp_strategy)
@settings(max_examples=50)
def test_ast::assignmentop_instantiation(instance):
    assert isinstance(instance, ast::AssignmentOp)

@given(instance=ast::ConditionalAndOp_strategy)
@settings(max_examples=50)
def test_ast::conditionalandop_instantiation(instance):
    assert isinstance(instance, ast::ConditionalAndOp)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ast::ArrayConstructor_strategy)
@settings(max_examples=50)
def test_ast::arrayconstructor_instantiation(instance):
    assert isinstance(instance, ast::ArrayConstructor)

@given(instance=ast::AssignmentOperation_strategy)
@settings(max_examples=50)
def test_ast::assignmentoperation_instantiation(instance):
    assert isinstance(instance, ast::AssignmentOperation)

@given(instance=ast::ClassifierOp_strategy)
@settings(max_examples=50)
def test_ast::classifierop_instantiation(instance):
    assert isinstance(instance, ast::ClassifierOp)

@given(instance=ast::ApplyRoundOp_strategy)
@settings(max_examples=50)
def test_ast::applyroundop_instantiation(instance):
    assert isinstance(instance, ast::ApplyRoundOp)

@given(instance=ast::BinaryOp_strategy)
@settings(max_examples=50)
def test_ast::binaryop_instantiation(instance):
    assert isinstance(instance, ast::BinaryOp)

@given(instance=ast::AccessOp_strategy)
@settings(max_examples=50)
def test_ast::accessop_instantiation(instance):
    assert isinstance(instance, ast::AccessOp)

@given(instance=ScopeStatement_strategy)
@settings(max_examples=50)
def test_scopestatement_instantiation(instance):
    assert isinstance(instance, ScopeStatement)

@given(instance=ast::TryStatement_strategy)
@settings(max_examples=50)
def test_ast::trystatement_instantiation(instance):
    assert isinstance(instance, ast::TryStatement)

@given(instance=ast::SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_ast::synchronizedstatement_instantiation(instance):
    assert isinstance(instance, ast::SynchronizedStatement)

@given(instance=ast::ApplySquareOp_strategy)
@settings(max_examples=50)
def test_ast::applysquareop_instantiation(instance):
    assert isinstance(instance, ast::ApplySquareOp)

@given(instance=LabeledStatement_strategy)
@settings(max_examples=50)
def test_labeledstatement_instantiation(instance):
    assert isinstance(instance, LabeledStatement)

@given(instance=ast::SwitchStatement_strategy)
@settings(max_examples=50)
def test_ast::switchstatement_instantiation(instance):
    assert isinstance(instance, ast::SwitchStatement)

@given(instance=ast::LoopStatement_strategy)
@settings(max_examples=50)
def test_ast::loopstatement_instantiation(instance):
    assert isinstance(instance, ast::LoopStatement)

@given(instance=SwitchPart_strategy)
@settings(max_examples=50)
def test_switchpart_instantiation(instance):
    assert isinstance(instance, SwitchPart)

@given(instance=ast::SwitchDefaultPart_strategy)
@settings(max_examples=50)
def test_ast::switchdefaultpart_instantiation(instance):
    assert isinstance(instance, ast::SwitchDefaultPart)

@given(instance=ast::SwitchCasePart_strategy)
@settings(max_examples=50)
def test_ast::switchcasepart_instantiation(instance):
    assert isinstance(instance, ast::SwitchCasePart)

@given(instance=MethodContentStatement_strategy)
@settings(max_examples=50)
def test_methodcontentstatement_instantiation(instance):
    assert isinstance(instance, MethodContentStatement)

@given(instance=ast::ThrowStatement_strategy)
@settings(max_examples=50)
def test_ast::throwstatement_instantiation(instance):
    assert isinstance(instance, ast::ThrowStatement)

@given(instance=ast::ScopeStatement_strategy)
@settings(max_examples=50)
def test_ast::scopestatement_instantiation(instance):
    assert isinstance(instance, ast::ScopeStatement)

@given(instance=ast::JumpStatement_strategy)
@settings(max_examples=50)
def test_ast::jumpstatement_instantiation(instance):
    assert isinstance(instance, ast::JumpStatement)

@given(instance=ast::IfStatement_strategy)
@settings(max_examples=50)
def test_ast::ifstatement_instantiation(instance):
    assert isinstance(instance, ast::IfStatement)

@given(instance=ast::LocalVarStatement_strategy)
@settings(max_examples=50)
def test_ast::localvarstatement_instantiation(instance):
    assert isinstance(instance, ast::LocalVarStatement)

@given(instance=ast::MethodClassifier_strategy)
@settings(max_examples=50)
def test_ast::methodclassifier_instantiation(instance):
    assert isinstance(instance, ast::MethodClassifier)

@given(instance=ast::LabeledStatement_strategy)
@settings(max_examples=50)
def test_ast::labeledstatement_instantiation(instance):
    assert isinstance(instance, ast::LabeledStatement)

@given(instance=ast::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_ast::expressionstatement_instantiation(instance):
    assert isinstance(instance, ast::ExpressionStatement)

@given(instance=ConditionalLoop_strategy)
@settings(max_examples=50)
def test_conditionalloop_instantiation(instance):
    assert isinstance(instance, ConditionalLoop)

@given(instance=ast::ForStatement_strategy)
@settings(max_examples=50)
def test_ast::forstatement_instantiation(instance):
    assert isinstance(instance, ast::ForStatement)

@given(instance=ast::WhileStatement_strategy)
@settings(max_examples=50)
def test_ast::whilestatement_instantiation(instance):
    assert isinstance(instance, ast::WhileStatement)

@given(instance=ast::DoWhileStatement_strategy)
@settings(max_examples=50)
def test_ast::dowhilestatement_instantiation(instance):
    assert isinstance(instance, ast::DoWhileStatement)

@given(instance=TopLevelStatement_strategy)
@settings(max_examples=50)
def test_toplevelstatement_instantiation(instance):
    assert isinstance(instance, TopLevelStatement)

@given(instance=ast::TopLevelClassifier_strategy)
@settings(max_examples=50)
def test_ast::toplevelclassifier_instantiation(instance):
    assert isinstance(instance, ast::TopLevelClassifier)

@given(instance=ast::PackageStatement_strategy)
@settings(max_examples=50)
def test_ast::packagestatement_instantiation(instance):
    assert isinstance(instance, ast::PackageStatement)

@given(instance=ast::ImportStatement_strategy)
@settings(max_examples=50)
def test_ast::importstatement_instantiation(instance):
    assert isinstance(instance, ast::ImportStatement)

@given(instance=ClassifierStatement_strategy)
@settings(max_examples=50)
def test_classifierstatement_instantiation(instance):
    assert isinstance(instance, ClassifierStatement)

@given(instance=ast::InterfaceStatement_strategy)
@settings(max_examples=50)
def test_ast::interfacestatement_instantiation(instance):
    assert isinstance(instance, ast::InterfaceStatement)

@given(instance=ast::ImplemenationClassifierStatement_strategy)
@settings(max_examples=50)
def test_ast::implemenationclassifierstatement_instantiation(instance):
    assert isinstance(instance, ast::ImplemenationClassifierStatement)

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=ast::ForeachStatement_strategy)
@settings(max_examples=50)
def test_ast::foreachstatement_instantiation(instance):
    assert isinstance(instance, ast::ForeachStatement)

@given(instance=ast::ConditionalLoop_strategy)
@settings(max_examples=50)
def test_ast::conditionalloop_instantiation(instance):
    assert isinstance(instance, ast::ConditionalLoop)

@given(instance=JumpStatement_strategy)
@settings(max_examples=50)
def test_jumpstatement_instantiation(instance):
    assert isinstance(instance, JumpStatement)

@given(instance=ast::ContinueStatement_strategy)
@settings(max_examples=50)
def test_ast::continuestatement_instantiation(instance):
    assert isinstance(instance, ast::ContinueStatement)

@given(instance=ast::BreakStatement_strategy)
@settings(max_examples=50)
def test_ast::breakstatement_instantiation(instance):
    assert isinstance(instance, ast::BreakStatement)

@given(instance=InitStatement_strategy)
@settings(max_examples=50)
def test_initstatement_instantiation(instance):
    assert isinstance(instance, InitStatement)

@given(instance=ast::StaticInitStatement_strategy)
@settings(max_examples=50)
def test_ast::staticinitstatement_instantiation(instance):
    assert isinstance(instance, ast::StaticInitStatement)

@given(instance=ast::InstanceInitStatement_strategy)
@settings(max_examples=50)
def test_ast::instanceinitstatement_instantiation(instance):
    assert isinstance(instance, ast::InstanceInitStatement)

@given(instance=ImplemenationClassifierStatement_strategy)
@settings(max_examples=50)
def test_implemenationclassifierstatement_instantiation(instance):
    assert isinstance(instance, ImplemenationClassifierStatement)

@given(instance=ast::EnumStatement_strategy)
@settings(max_examples=50)
def test_ast::enumstatement_instantiation(instance):
    assert isinstance(instance, ast::EnumStatement)

@given(instance=ast::ClassStatement_strategy)
@settings(max_examples=50)
def test_ast::classstatement_instantiation(instance):
    assert isinstance(instance, ast::ClassStatement)

@given(instance=ClassifierMemberStatement_strategy)
@settings(max_examples=50)
def test_classifiermemberstatement_instantiation(instance):
    assert isinstance(instance, ClassifierMemberStatement)

@given(instance=ast::Feature_strategy)
@settings(max_examples=50)
def test_ast::feature_instantiation(instance):
    assert isinstance(instance, ast::Feature)

@given(instance=ast::InnerClassifier_strategy)
@settings(max_examples=50)
def test_ast::innerclassifier_instantiation(instance):
    assert isinstance(instance, ast::InnerClassifier)

@given(instance=ast::InitStatement_strategy)
@settings(max_examples=50)
def test_ast::initstatement_instantiation(instance):
    assert isinstance(instance, ast::InitStatement)

@given(instance=ast::EnumLiteral_strategy)
@settings(max_examples=50)
def test_ast::enumliteral_instantiation(instance):
    assert isinstance(instance, ast::EnumLiteral)

@given(instance=ast::MethodBlock_strategy)
@settings(max_examples=50)
def test_ast::methodblock_instantiation(instance):
    assert isinstance(instance, ast::MethodBlock)

@given(instance=BehaviorFeature_strategy)
@settings(max_examples=50)
def test_behaviorfeature_instantiation(instance):
    assert isinstance(instance, BehaviorFeature)

@given(instance=ast::MethodStatement_strategy)
@settings(max_examples=50)
def test_ast::methodstatement_instantiation(instance):
    assert isinstance(instance, ast::MethodStatement)

@given(instance=ast::ConstructorStatement_strategy)
@settings(max_examples=50)
def test_ast::constructorstatement_instantiation(instance):
    assert isinstance(instance, ast::ConstructorStatement)

@given(instance=EJBase_strategy)
@settings(max_examples=50)
def test_ejbase_instantiation(instance):
    assert isinstance(instance, EJBase)

@given(instance=ast::MethodContentStatement_strategy)
@settings(max_examples=50)
def test_ast::methodcontentstatement_instantiation(instance):
    assert isinstance(instance, ast::MethodContentStatement)

@given(instance=ast::CatchPart_strategy)
@settings(max_examples=50)
def test_ast::catchpart_instantiation(instance):
    assert isinstance(instance, ast::CatchPart)

@given(instance=ast::SwitchPart_strategy)
@settings(max_examples=50)
def test_ast::switchpart_instantiation(instance):
    assert isinstance(instance, ast::SwitchPart)

@given(instance=ast::ClassifierStatement_strategy)
@settings(max_examples=50)
def test_ast::classifierstatement_instantiation(instance):
    assert isinstance(instance, ast::ClassifierStatement)

@given(instance=ast::TopLevelStatement_strategy)
@settings(max_examples=50)
def test_ast::toplevelstatement_instantiation(instance):
    assert isinstance(instance, ast::TopLevelStatement)

@given(instance=ast::IfThenPart_strategy)
@settings(max_examples=50)
def test_ast::ifthenpart_instantiation(instance):
    assert isinstance(instance, ast::IfThenPart)

@given(instance=ast::ClassifierMemberStatement_strategy)
@settings(max_examples=50)
def test_ast::classifiermemberstatement_instantiation(instance):
    assert isinstance(instance, ast::ClassifierMemberStatement)

@given(instance=ast::ClassBlock_strategy)
@settings(max_examples=50)
def test_ast::classblock_instantiation(instance):
    assert isinstance(instance, ast::ClassBlock)

@given(instance=ast::Identifier_strategy)
@settings(max_examples=50)
def test_ast::identifier_instantiation(instance):
    assert isinstance(instance, ast::Identifier)

@given(instance=ast::Identifier_strategy)
def test_ast::identifier_quotedValue_type(instance):
    assert isinstance(instance.quotedValue, str)


@given(instance=ast::Identifier_strategy)
def test_ast::identifier_quotedValue_setter(instance):
    original = instance.quotedValue
    instance.quotedValue = original
    assert instance.quotedValue == original

@given(instance=ast::Identifier_strategy)
def test_ast::identifier_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=ast::Identifier_strategy)
def test_ast::identifier_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=ast::Identifier_strategy)
def test_ast::identifier_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ast::Identifier_strategy)
def test_ast::identifier_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=ast::BehaviorFeature_strategy)
@settings(max_examples=50)
def test_ast::behaviorfeature_instantiation(instance):
    assert isinstance(instance, ast::BehaviorFeature)

@given(instance=ast::FieldStatement_strategy)
@settings(max_examples=50)
def test_ast::fieldstatement_instantiation(instance):
    assert isinstance(instance, ast::FieldStatement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ast::TemplateParameter_strategy)
@settings(max_examples=50)
def test_ast::templateparameter_instantiation(instance):
    assert isinstance(instance, ast::TemplateParameter)

@given(instance=ast::Variable_strategy)
@settings(max_examples=50)
def test_ast::variable_instantiation(instance):
    assert isinstance(instance, ast::Variable)

@given(instance=ast::Parameter_strategy)
@settings(max_examples=50)
def test_ast::parameter_instantiation(instance):
    assert isinstance(instance, ast::Parameter)

@given(instance=ast::Expression_strategy)
@settings(max_examples=50)
def test_ast::expression_instantiation(instance):
    assert isinstance(instance, ast::Expression)

@given(instance=EJElement_strategy)
@settings(max_examples=50)
def test_ejelement_instantiation(instance):
    assert isinstance(instance, EJElement)

@given(instance=ast::AttributeSet_strategy)
@settings(max_examples=50)
def test_ast::attributeset_instantiation(instance):
    assert isinstance(instance, ast::AttributeSet)

@given(instance=ast::Label_strategy)
@settings(max_examples=50)
def test_ast::label_instantiation(instance):
    assert isinstance(instance, ast::Label)

@given(instance=ast::Label_strategy)
def test_ast::label_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ast::Label_strategy)
def test_ast::label_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast::Modifier_strategy)
@settings(max_examples=50)
def test_ast::modifier_instantiation(instance):
    assert isinstance(instance, ast::Modifier)

@given(instance=ast::Modifier_strategy)
def test_ast::modifier_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ast::Modifier_strategy)
def test_ast::modifier_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ast::SwitchDefaultPartRef_strategy)
@settings(max_examples=50)
def test_ast::switchdefaultpartref_instantiation(instance):
    assert isinstance(instance, ast::SwitchDefaultPartRef)

@given(instance=ast::DocumentationLine_strategy)
@settings(max_examples=50)
def test_ast::documentationline_instantiation(instance):
    assert isinstance(instance, ast::DocumentationLine)

@given(instance=ast::DocumentationLine_strategy)
def test_ast::documentationline_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=ast::DocumentationLine_strategy)
def test_ast::documentationline_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=ast::EJBase_strategy)
@settings(max_examples=50)
def test_ast::ejbase_instantiation(instance):
    assert isinstance(instance, ast::EJBase)

@given(instance=ast::EJElement_strategy)
@settings(max_examples=50)
def test_ast::ejelement_instantiation(instance):
    assert isinstance(instance, ast::EJElement)

@given(instance=ast::EJElement_strategy)
def test_ast::ejelement_endLine_type(instance):
    assert isinstance(instance.endLine, int)


@given(instance=ast::EJElement_strategy)
def test_ast::ejelement_endLine_setter(instance):
    original = instance.endLine
    instance.endLine = original
    assert instance.endLine == original

@given(instance=ast::EJElement_strategy)
def test_ast::ejelement_startOffset_type(instance):
    assert isinstance(instance.startOffset, str)


@given(instance=ast::EJElement_strategy)
def test_ast::ejelement_startOffset_setter(instance):
    original = instance.startOffset
    instance.startOffset = original
    assert instance.startOffset == original

@given(instance=ast::EJElement_strategy)
def test_ast::ejelement_startColumn_type(instance):
    assert isinstance(instance.startColumn, int)


@given(instance=ast::EJElement_strategy)
def test_ast::ejelement_startColumn_setter(instance):
    original = instance.startColumn
    instance.startColumn = original
    assert instance.startColumn == original

@given(instance=ast::EJElement_strategy)
def test_ast::ejelement_endColumn_type(instance):
    assert isinstance(instance.endColumn, int)


@given(instance=ast::EJElement_strategy)
def test_ast::ejelement_endColumn_setter(instance):
    original = instance.endColumn
    instance.endColumn = original
    assert instance.endColumn == original

@given(instance=ast::EJElement_strategy)
def test_ast::ejelement_startLine_type(instance):
    assert isinstance(instance.startLine, int)


@given(instance=ast::EJElement_strategy)
def test_ast::ejelement_startLine_setter(instance):
    original = instance.startLine
    instance.startLine = original
    assert instance.startLine == original

@given(instance=ast::EJElement_strategy)
def test_ast::ejelement_endOffset_type(instance):
    assert isinstance(instance.endOffset, str)


@given(instance=ast::EJElement_strategy)
def test_ast::ejelement_endOffset_setter(instance):
    original = instance.endOffset
    instance.endOffset = original
    assert instance.endOffset == original

@given(instance=ast::AttributeDefinition_strategy)
@settings(max_examples=50)
def test_ast::attributedefinition_instantiation(instance):
    assert isinstance(instance, ast::AttributeDefinition)

@given(instance=ast::EmptyStatement_strategy)
@settings(max_examples=50)
def test_ast::emptystatement_instantiation(instance):
    assert isinstance(instance, ast::EmptyStatement)

@given(instance=ast::WildcardType_strategy)
@settings(max_examples=50)
def test_ast::wildcardtype_instantiation(instance):
    assert isinstance(instance, ast::WildcardType)

@given(instance=ast::RangeExpression_strategy)
@settings(max_examples=50)
def test_ast::rangeexpression_instantiation(instance):
    assert isinstance(instance, ast::RangeExpression)

@given(instance=ast::AssertStatement_strategy)
@settings(max_examples=50)
def test_ast::assertstatement_instantiation(instance):
    assert isinstance(instance, ast::AssertStatement)

@given(instance=ast::NamedElement_strategy)
@settings(max_examples=50)
def test_ast::namedelement_instantiation(instance):
    assert isinstance(instance, ast::NamedElement)

@given(instance=ast::UnaryOp_strategy)
@settings(max_examples=50)
def test_ast::unaryop_instantiation(instance):
    assert isinstance(instance, ast::UnaryOp)

@given(instance=ast::UnaryMinusOp_strategy)
@settings(max_examples=50)
def test_ast::unaryminusop_instantiation(instance):
    assert isinstance(instance, ast::UnaryMinusOp)

@given(instance=ast::ThisReference_strategy)
@settings(max_examples=50)
def test_ast::thisreference_instantiation(instance):
    assert isinstance(instance, ast::ThisReference)

@given(instance=ast::ThisReference_strategy)
def test_ast::thisreference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ast::ThisReference_strategy)
def test_ast::thisreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast::SuperReference_strategy)
@settings(max_examples=50)
def test_ast::superreference_instantiation(instance):
    assert isinstance(instance, ast::SuperReference)

@given(instance=ast::SuperReference_strategy)
def test_ast::superreference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ast::SuperReference_strategy)
def test_ast::superreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast::ShiftOp_strategy)
@settings(max_examples=50)
def test_ast::shiftop_instantiation(instance):
    assert isinstance(instance, ast::ShiftOp)

@given(instance=ast::RightShiftAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast::rightshiftassignmentop_instantiation(instance):
    assert isinstance(instance, ast::RightShiftAssignmentOp)

@given(instance=ast::ReturnStatement_strategy)
@settings(max_examples=50)
def test_ast::returnstatement_instantiation(instance):
    assert isinstance(instance, ast::ReturnStatement)

@given(instance=ast::RemainderAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast::remainderassignmentop_instantiation(instance):
    assert isinstance(instance, ast::RemainderAssignmentOp)

@given(instance=ast::PrimitiveType_strategy)
@settings(max_examples=50)
def test_ast::primitivetype_instantiation(instance):
    assert isinstance(instance, ast::PrimitiveType)

@given(instance=ast::PrimitiveType_strategy)
def test_ast::primitivetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ast::PrimitiveType_strategy)
def test_ast::primitivetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast::PrefixIncrementOp_strategy)
@settings(max_examples=50)
def test_ast::prefixincrementop_instantiation(instance):
    assert isinstance(instance, ast::PrefixIncrementOp)

@given(instance=ast::PrefixDecrementOp_strategy)
@settings(max_examples=50)
def test_ast::prefixdecrementop_instantiation(instance):
    assert isinstance(instance, ast::PrefixDecrementOp)

@given(instance=ast::PostfixIncrementOp_strategy)
@settings(max_examples=50)
def test_ast::postfixincrementop_instantiation(instance):
    assert isinstance(instance, ast::PostfixIncrementOp)

@given(instance=ast::ZeroExtensionRightShiftAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast::zeroextensionrightshiftassignmentop_instantiation(instance):
    assert isinstance(instance, ast::ZeroExtensionRightShiftAssignmentOp)

@given(instance=ast::UnaryPlusOp_strategy)
@settings(max_examples=50)
def test_ast::unaryplusop_instantiation(instance):
    assert isinstance(instance, ast::UnaryPlusOp)

@given(instance=ast::NewOp_strategy)
@settings(max_examples=50)
def test_ast::newop_instantiation(instance):
    assert isinstance(instance, ast::NewOp)

@given(instance=ast::MultiplyAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast::multiplyassignmentop_instantiation(instance):
    assert isinstance(instance, ast::MultiplyAssignmentOp)

@given(instance=ast::MultiplyOp_strategy)
@settings(max_examples=50)
def test_ast::multiplyop_instantiation(instance):
    assert isinstance(instance, ast::MultiplyOp)

@given(instance=ast::MinusOp_strategy)
@settings(max_examples=50)
def test_ast::minusop_instantiation(instance):
    assert isinstance(instance, ast::MinusOp)

@given(instance=ast::MinusAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast::minusassignmentop_instantiation(instance):
    assert isinstance(instance, ast::MinusAssignmentOp)

@given(instance=ast::LogicalComplementOp_strategy)
@settings(max_examples=50)
def test_ast::logicalcomplementop_instantiation(instance):
    assert isinstance(instance, ast::LogicalComplementOp)

@given(instance=ast::Literal_strategy)
@settings(max_examples=50)
def test_ast::literal_instantiation(instance):
    assert isinstance(instance, ast::Literal)

@given(instance=ast::Literal_strategy)
def test_ast::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ast::Literal_strategy)
def test_ast::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ast::LessThenOp_strategy)
@settings(max_examples=50)
def test_ast::lessthenop_instantiation(instance):
    assert isinstance(instance, ast::LessThenOp)

@given(instance=ast::LessOrEqualOp_strategy)
@settings(max_examples=50)
def test_ast::lessorequalop_instantiation(instance):
    assert isinstance(instance, ast::LessOrEqualOp)

@given(instance=ast::PostfixDecrementOp_strategy)
@settings(max_examples=50)
def test_ast::postfixdecrementop_instantiation(instance):
    assert isinstance(instance, ast::PostfixDecrementOp)

@given(instance=ast::PlusOp_strategy)
@settings(max_examples=50)
def test_ast::plusop_instantiation(instance):
    assert isinstance(instance, ast::PlusOp)

@given(instance=ast::PlusAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast::plusassignmentop_instantiation(instance):
    assert isinstance(instance, ast::PlusAssignmentOp)

@given(instance=ast::NotEqualOp_strategy)
@settings(max_examples=50)
def test_ast::notequalop_instantiation(instance):
    assert isinstance(instance, ast::NotEqualOp)

@given(instance=ast::IdentityOp_strategy)
@settings(max_examples=50)
def test_ast::identityop_instantiation(instance):
    assert isinstance(instance, ast::IdentityOp)

@given(instance=ast::GreaterThenOp_strategy)
@settings(max_examples=50)
def test_ast::greaterthenop_instantiation(instance):
    assert isinstance(instance, ast::GreaterThenOp)

@given(instance=ast::GreaterOrEqualOp_strategy)
@settings(max_examples=50)
def test_ast::greaterorequalop_instantiation(instance):
    assert isinstance(instance, ast::GreaterOrEqualOp)

@given(instance=ast::EqualOp_strategy)
@settings(max_examples=50)
def test_ast::equalop_instantiation(instance):
    assert isinstance(instance, ast::EqualOp)

@given(instance=ast::DivisionOp_strategy)
@settings(max_examples=50)
def test_ast::divisionop_instantiation(instance):
    assert isinstance(instance, ast::DivisionOp)

@given(instance=DivisionOp_strategy)
@settings(max_examples=50)
def test_divisionop_instantiation(instance):
    assert isinstance(instance, DivisionOp)

@given(instance=ast::RemainderOp_strategy)
@settings(max_examples=50)
def test_ast::remainderop_instantiation(instance):
    assert isinstance(instance, ast::RemainderOp)

@given(instance=ast::DivideOp_strategy)
@settings(max_examples=50)
def test_ast::divideop_instantiation(instance):
    assert isinstance(instance, ast::DivideOp)

@given(instance=ast::DivideAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast::divideassignmentop_instantiation(instance):
    assert isinstance(instance, ast::DivideAssignmentOp)

@given(instance=ast::ConditionalOrOp_strategy)
@settings(max_examples=50)
def test_ast::conditionalorop_instantiation(instance):
    assert isinstance(instance, ast::ConditionalOrOp)

@given(instance=ast::ConditionalOp_strategy)
@settings(max_examples=50)
def test_ast::conditionalop_instantiation(instance):
    assert isinstance(instance, ast::ConditionalOp)

@given(instance=ShiftOp_strategy)
@settings(max_examples=50)
def test_shiftop_instantiation(instance):
    assert isinstance(instance, ShiftOp)

@given(instance=ast::RightShiftOp_strategy)
@settings(max_examples=50)
def test_ast::rightshiftop_instantiation(instance):
    assert isinstance(instance, ast::RightShiftOp)

@given(instance=ast::ZeroExtensionRightShiftOp_strategy)
@settings(max_examples=50)
def test_ast::zeroextensionrightshiftop_instantiation(instance):
    assert isinstance(instance, ast::ZeroExtensionRightShiftOp)

@given(instance=ast::LeftShiftOp_strategy)
@settings(max_examples=50)
def test_ast::leftshiftop_instantiation(instance):
    assert isinstance(instance, ast::LeftShiftOp)

@given(instance=ast::LeftShiftAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast::leftshiftassignmentop_instantiation(instance):
    assert isinstance(instance, ast::LeftShiftAssignmentOp)

@given(instance=ClassifierOp_strategy)
@settings(max_examples=50)
def test_classifierop_instantiation(instance):
    assert isinstance(instance, ClassifierOp)

@given(instance=ast::InstanceOfOp_strategy)
@settings(max_examples=50)
def test_ast::instanceofop_instantiation(instance):
    assert isinstance(instance, ast::InstanceOfOp)

@given(instance=ast::CastOp_strategy)
@settings(max_examples=50)
def test_ast::castop_instantiation(instance):
    assert isinstance(instance, ast::CastOp)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=ast::FloatLiteral_strategy)
@settings(max_examples=50)
def test_ast::floatliteral_instantiation(instance):
    assert isinstance(instance, ast::FloatLiteral)

@given(instance=ast::LongIntegerLiteral_strategy)
@settings(max_examples=50)
def test_ast::longintegerliteral_instantiation(instance):
    assert isinstance(instance, ast::LongIntegerLiteral)

@given(instance=ast::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_ast::integerliteral_instantiation(instance):
    assert isinstance(instance, ast::IntegerLiteral)

@given(instance=ast::DoubleLiteral_strategy)
@settings(max_examples=50)
def test_ast::doubleliteral_instantiation(instance):
    assert isinstance(instance, ast::DoubleLiteral)

@given(instance=ast::CharacterLiteral_strategy)
@settings(max_examples=50)
def test_ast::characterliteral_instantiation(instance):
    assert isinstance(instance, ast::CharacterLiteral)

@given(instance=ast::StringLiteral_strategy)
@settings(max_examples=50)
def test_ast::stringliteral_instantiation(instance):
    assert isinstance(instance, ast::StringLiteral)

@given(instance=ast::NullReference_strategy)
@settings(max_examples=50)
def test_ast::nullreference_instantiation(instance):
    assert isinstance(instance, ast::NullReference)

@given(instance=ast::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_ast::booleanliteral_instantiation(instance):
    assert isinstance(instance, ast::BooleanLiteral)

@given(instance=ast::BitwiseXorOp_strategy)
@settings(max_examples=50)
def test_ast::bitwisexorop_instantiation(instance):
    assert isinstance(instance, ast::BitwiseXorOp)

@given(instance=ast::BitwiseXorAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast::bitwisexorassignmentop_instantiation(instance):
    assert isinstance(instance, ast::BitwiseXorAssignmentOp)

@given(instance=ast::BitwiseOrOp_strategy)
@settings(max_examples=50)
def test_ast::bitwiseorop_instantiation(instance):
    assert isinstance(instance, ast::BitwiseOrOp)
