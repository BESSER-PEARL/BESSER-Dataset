import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    ast_AccessOp,
    ScopeStatement,
    ast_TryStatement,
    ast_SynchronizedStatement,
    ast_ApplySquareOp,
    LabeledStatement,
    ast_SwitchStatement,
    ast_LoopStatement,
    SwitchPart,
    ast_SwitchDefaultPart,
    ast_SwitchCasePart,
    MethodContentStatement,
    ast_MethodClassifier,
    ast_ThrowStatement,
    ast_LabeledStatement,
    ast_IfStatement,
    ast_LocalVarStatement,
    ast_JumpStatement,
    ast_ScopeStatement,
    ast_ExpressionStatement,
    ConditionalLoop,
    ast_WhileStatement,
    ast_ForStatement,
    ast_DoWhileStatement,
    TopLevelStatement,
    ast_TopLevelClassifier,
    ast_PackageStatement,
    ast_ImportStatement,
    ClassifierStatement,
    ast_InterfaceStatement,
    ast_ImplemenationClassifierStatement,
    LoopStatement,
    ast_ForeachStatement,
    ast_ConditionalLoop,
    JumpStatement,
    ast_ContinueStatement,
    ast_BreakStatement,
    InitStatement,
    ast_StaticInitStatement,
    ast_InstanceInitStatement,
    ImplemenationClassifierStatement,
    ast_EnumStatement,
    ast_ClassStatement,
    ClassifierMemberStatement,
    ast_Feature,
    ast_InitStatement,
    ast_InnerClassifier,
    ast_EnumLiteral,
    ast_MethodBlock,
    BehaviorFeature,
    ast_MethodStatement,
    ast_ConstructorStatement,
    EJBase,
    ast_CatchPart,
    ast_ClassifierMemberStatement,
    ast_MethodContentStatement,
    ast_ClassifierStatement,
    ast_SwitchPart,
    ast_TopLevelStatement,
    ast_IfThenPart,
    ast_ClassBlock,
    ast_Identifier,
    Feature,
    ast_BehaviorFeature,
    ast_FieldStatement,
    NamedElement,
    ast_TemplateParameter,
    ast_Variable,
    ast_Parameter,
    ast_Expression,
    EJElement,
    ast_SwitchDefaultPartRef,
    ast_AttributeSet,
    ast_Modifier,
    ast_Label,
    ast_DocumentationLine,
    ast_EJBase,
    ast_EJElement,
    ast_AttributeDefinition,
    ast_EmptyStatement,
    ast_WildcardType,
    ast_RangeExpression,
    ast_AssertStatement,
    ast_NamedElement,
    ast_UnaryOp,
    ast_ThisReference,
    ast_SuperReference,
    ast_ShiftOp,
    ast_ReturnStatement,
    ast_PrimitiveType,
    ast_NewOp,
    ast_MultiplyOp,
    ast_MinusOp,
    ast_Literal,
    ast_PlusOp,
    ast_IdentityOp,
    ast_DivisionOp,
    DivisionOp,
    ast_RemainderOp,
    ast_DivideOp,
    ast_ConditionalOp,
    ShiftOp,
    ast_RightShiftOp,
    ast_ZeroExtensionRightShiftOp,
    ast_LeftShiftOp,
    ClassifierOp,
    ast_InstanceOfOp,
    ast_CastOp,
    Literal,
    ast_DoubleLiteral,
    ast_LongIntegerLiteral,
    ast_NullReference,
    ast_FloatLiteral,
    ast_IntegerLiteral,
    ast_StringLiteral,
    ast_BooleanLiteral,
    UnaryOp,
    ast_PostfixDecrementOp,
    ast_PostfixIncrementOp,
    ast_LogicalComplementOp,
    ast_PrefixIncrementOp,
    ast_UnaryPlusOp,
    ast_UnaryMinusOp,
    ast_PrefixDecrementOp,
    ast_BitwiseComplementOp,
    BinaryOp,
    ast_LessThenOp,
    ast_GreaterOrEqualOp,
    ast_BitwiseXorOp,
    ast_LessOrEqualOp,
    ast_ConditionalOrOp,
    ast_NotEqualOp,
    ast_BitwiseOrOp,
    ast_EqualOp,
    ast_GreaterThenOp,
    ast_BitwiseAndOp,
    ast_BinaryOp,
    ast_AssignmentOperation,
    AssignmentOperation,
    ast_ZeroExtensionRightShiftAssignmentOp,
    ast_MinusAssignmentOp,
    ast_BitwiseXorAssignmentOp,
    ast_RemainderAssignmentOp,
    ast_MultiplyAssignmentOp,
    ast_PlusAssignmentOp,
    ast_BitwiseAndAssignmentOp,
    ast_BitwiseOrAssignmentOp,
    ast_LeftShiftAssignmentOp,
    ast_DivideAssignmentOp,
    ast_RightShiftAssignmentOp,
    ast_AssignmentOp,
    ast_ArrayConstructor,
    ast_ConditionalAndOp,
    ast_ClassifierOp,
    ast_CharacterLiteral,
    ast_ApplyRoundOp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_ast_accessop_is_not_abstract():
    assert not inspect.isabstract(ast_AccessOp)


def test_ast_accessop_constructor_exists():
    assert callable(ast_AccessOp.__init__)


def test_ast_accessop_constructor_args():
    sig = inspect.signature(ast_AccessOp.__init__)
    params = list(sig.parameters.keys())



def test_scopestatement_is_not_abstract():
    assert not inspect.isabstract(ScopeStatement)


def test_scopestatement_constructor_exists():
    assert callable(ScopeStatement.__init__)


def test_scopestatement_constructor_args():
    sig = inspect.signature(ScopeStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_trystatement_is_not_abstract():
    assert not inspect.isabstract(ast_TryStatement)


def test_ast_trystatement_constructor_exists():
    assert callable(ast_TryStatement.__init__)


def test_ast_trystatement_constructor_args():
    sig = inspect.signature(ast_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(ast_SynchronizedStatement)


def test_ast_synchronizedstatement_constructor_exists():
    assert callable(ast_SynchronizedStatement.__init__)


def test_ast_synchronizedstatement_constructor_args():
    sig = inspect.signature(ast_SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_applysquareop_is_not_abstract():
    assert not inspect.isabstract(ast_ApplySquareOp)


def test_ast_applysquareop_constructor_exists():
    assert callable(ast_ApplySquareOp.__init__)


def test_ast_applysquareop_constructor_args():
    sig = inspect.signature(ast_ApplySquareOp.__init__)
    params = list(sig.parameters.keys())



def test_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(LabeledStatement)


def test_labeledstatement_constructor_exists():
    assert callable(LabeledStatement.__init__)


def test_labeledstatement_constructor_args():
    sig = inspect.signature(LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_switchstatement_is_not_abstract():
    assert not inspect.isabstract(ast_SwitchStatement)


def test_ast_switchstatement_constructor_exists():
    assert callable(ast_SwitchStatement.__init__)


def test_ast_switchstatement_constructor_args():
    sig = inspect.signature(ast_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_loopstatement_is_not_abstract():
    assert not inspect.isabstract(ast_LoopStatement)


def test_ast_loopstatement_constructor_exists():
    assert callable(ast_LoopStatement.__init__)


def test_ast_loopstatement_constructor_args():
    sig = inspect.signature(ast_LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_switchpart_is_not_abstract():
    assert not inspect.isabstract(SwitchPart)


def test_switchpart_constructor_exists():
    assert callable(SwitchPart.__init__)


def test_switchpart_constructor_args():
    sig = inspect.signature(SwitchPart.__init__)
    params = list(sig.parameters.keys())



def test_ast_switchdefaultpart_is_not_abstract():
    assert not inspect.isabstract(ast_SwitchDefaultPart)


def test_ast_switchdefaultpart_constructor_exists():
    assert callable(ast_SwitchDefaultPart.__init__)


def test_ast_switchdefaultpart_constructor_args():
    sig = inspect.signature(ast_SwitchDefaultPart.__init__)
    params = list(sig.parameters.keys())



def test_ast_switchcasepart_is_not_abstract():
    assert not inspect.isabstract(ast_SwitchCasePart)


def test_ast_switchcasepart_constructor_exists():
    assert callable(ast_SwitchCasePart.__init__)


def test_ast_switchcasepart_constructor_args():
    sig = inspect.signature(ast_SwitchCasePart.__init__)
    params = list(sig.parameters.keys())



def test_methodcontentstatement_is_not_abstract():
    assert not inspect.isabstract(MethodContentStatement)


def test_methodcontentstatement_constructor_exists():
    assert callable(MethodContentStatement.__init__)


def test_methodcontentstatement_constructor_args():
    sig = inspect.signature(MethodContentStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_methodclassifier_is_not_abstract():
    assert not inspect.isabstract(ast_MethodClassifier)


def test_ast_methodclassifier_constructor_exists():
    assert callable(ast_MethodClassifier.__init__)


def test_ast_methodclassifier_constructor_args():
    sig = inspect.signature(ast_MethodClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ast_throwstatement_is_not_abstract():
    assert not inspect.isabstract(ast_ThrowStatement)


def test_ast_throwstatement_constructor_exists():
    assert callable(ast_ThrowStatement.__init__)


def test_ast_throwstatement_constructor_args():
    sig = inspect.signature(ast_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(ast_LabeledStatement)


def test_ast_labeledstatement_constructor_exists():
    assert callable(ast_LabeledStatement.__init__)


def test_ast_labeledstatement_constructor_args():
    sig = inspect.signature(ast_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_ifstatement_is_not_abstract():
    assert not inspect.isabstract(ast_IfStatement)


def test_ast_ifstatement_constructor_exists():
    assert callable(ast_IfStatement.__init__)


def test_ast_ifstatement_constructor_args():
    sig = inspect.signature(ast_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_localvarstatement_is_not_abstract():
    assert not inspect.isabstract(ast_LocalVarStatement)


def test_ast_localvarstatement_constructor_exists():
    assert callable(ast_LocalVarStatement.__init__)


def test_ast_localvarstatement_constructor_args():
    sig = inspect.signature(ast_LocalVarStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_jumpstatement_is_not_abstract():
    assert not inspect.isabstract(ast_JumpStatement)


def test_ast_jumpstatement_constructor_exists():
    assert callable(ast_JumpStatement.__init__)


def test_ast_jumpstatement_constructor_args():
    sig = inspect.signature(ast_JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_scopestatement_is_not_abstract():
    assert not inspect.isabstract(ast_ScopeStatement)


def test_ast_scopestatement_constructor_exists():
    assert callable(ast_ScopeStatement.__init__)


def test_ast_scopestatement_constructor_args():
    sig = inspect.signature(ast_ScopeStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(ast_ExpressionStatement)


def test_ast_expressionstatement_constructor_exists():
    assert callable(ast_ExpressionStatement.__init__)


def test_ast_expressionstatement_constructor_args():
    sig = inspect.signature(ast_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_conditionalloop_is_not_abstract():
    assert not inspect.isabstract(ConditionalLoop)


def test_conditionalloop_constructor_exists():
    assert callable(ConditionalLoop.__init__)


def test_conditionalloop_constructor_args():
    sig = inspect.signature(ConditionalLoop.__init__)
    params = list(sig.parameters.keys())



def test_ast_whilestatement_is_not_abstract():
    assert not inspect.isabstract(ast_WhileStatement)


def test_ast_whilestatement_constructor_exists():
    assert callable(ast_WhileStatement.__init__)


def test_ast_whilestatement_constructor_args():
    sig = inspect.signature(ast_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_forstatement_is_not_abstract():
    assert not inspect.isabstract(ast_ForStatement)


def test_ast_forstatement_constructor_exists():
    assert callable(ast_ForStatement.__init__)


def test_ast_forstatement_constructor_args():
    sig = inspect.signature(ast_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(ast_DoWhileStatement)


def test_ast_dowhilestatement_constructor_exists():
    assert callable(ast_DoWhileStatement.__init__)


def test_ast_dowhilestatement_constructor_args():
    sig = inspect.signature(ast_DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_toplevelstatement_is_not_abstract():
    assert not inspect.isabstract(TopLevelStatement)


def test_toplevelstatement_constructor_exists():
    assert callable(TopLevelStatement.__init__)


def test_toplevelstatement_constructor_args():
    sig = inspect.signature(TopLevelStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_toplevelclassifier_is_not_abstract():
    assert not inspect.isabstract(ast_TopLevelClassifier)


def test_ast_toplevelclassifier_constructor_exists():
    assert callable(ast_TopLevelClassifier.__init__)


def test_ast_toplevelclassifier_constructor_args():
    sig = inspect.signature(ast_TopLevelClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ast_packagestatement_is_not_abstract():
    assert not inspect.isabstract(ast_PackageStatement)


def test_ast_packagestatement_constructor_exists():
    assert callable(ast_PackageStatement.__init__)


def test_ast_packagestatement_constructor_args():
    sig = inspect.signature(ast_PackageStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_importstatement_is_not_abstract():
    assert not inspect.isabstract(ast_ImportStatement)


def test_ast_importstatement_constructor_exists():
    assert callable(ast_ImportStatement.__init__)


def test_ast_importstatement_constructor_args():
    sig = inspect.signature(ast_ImportStatement.__init__)
    params = list(sig.parameters.keys())



def test_classifierstatement_is_not_abstract():
    assert not inspect.isabstract(ClassifierStatement)


def test_classifierstatement_constructor_exists():
    assert callable(ClassifierStatement.__init__)


def test_classifierstatement_constructor_args():
    sig = inspect.signature(ClassifierStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_interfacestatement_is_not_abstract():
    assert not inspect.isabstract(ast_InterfaceStatement)


def test_ast_interfacestatement_constructor_exists():
    assert callable(ast_InterfaceStatement.__init__)


def test_ast_interfacestatement_constructor_args():
    sig = inspect.signature(ast_InterfaceStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_implemenationclassifierstatement_is_not_abstract():
    assert not inspect.isabstract(ast_ImplemenationClassifierStatement)


def test_ast_implemenationclassifierstatement_constructor_exists():
    assert callable(ast_ImplemenationClassifierStatement.__init__)


def test_ast_implemenationclassifierstatement_constructor_args():
    sig = inspect.signature(ast_ImplemenationClassifierStatement.__init__)
    params = list(sig.parameters.keys())



def test_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_foreachstatement_is_not_abstract():
    assert not inspect.isabstract(ast_ForeachStatement)


def test_ast_foreachstatement_constructor_exists():
    assert callable(ast_ForeachStatement.__init__)


def test_ast_foreachstatement_constructor_args():
    sig = inspect.signature(ast_ForeachStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_conditionalloop_is_not_abstract():
    assert not inspect.isabstract(ast_ConditionalLoop)


def test_ast_conditionalloop_constructor_exists():
    assert callable(ast_ConditionalLoop.__init__)


def test_ast_conditionalloop_constructor_args():
    sig = inspect.signature(ast_ConditionalLoop.__init__)
    params = list(sig.parameters.keys())



def test_jumpstatement_is_not_abstract():
    assert not inspect.isabstract(JumpStatement)


def test_jumpstatement_constructor_exists():
    assert callable(JumpStatement.__init__)


def test_jumpstatement_constructor_args():
    sig = inspect.signature(JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_continuestatement_is_not_abstract():
    assert not inspect.isabstract(ast_ContinueStatement)


def test_ast_continuestatement_constructor_exists():
    assert callable(ast_ContinueStatement.__init__)


def test_ast_continuestatement_constructor_args():
    sig = inspect.signature(ast_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_breakstatement_is_not_abstract():
    assert not inspect.isabstract(ast_BreakStatement)


def test_ast_breakstatement_constructor_exists():
    assert callable(ast_BreakStatement.__init__)


def test_ast_breakstatement_constructor_args():
    sig = inspect.signature(ast_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_initstatement_is_not_abstract():
    assert not inspect.isabstract(InitStatement)


def test_initstatement_constructor_exists():
    assert callable(InitStatement.__init__)


def test_initstatement_constructor_args():
    sig = inspect.signature(InitStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_staticinitstatement_is_not_abstract():
    assert not inspect.isabstract(ast_StaticInitStatement)


def test_ast_staticinitstatement_constructor_exists():
    assert callable(ast_StaticInitStatement.__init__)


def test_ast_staticinitstatement_constructor_args():
    sig = inspect.signature(ast_StaticInitStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_instanceinitstatement_is_not_abstract():
    assert not inspect.isabstract(ast_InstanceInitStatement)


def test_ast_instanceinitstatement_constructor_exists():
    assert callable(ast_InstanceInitStatement.__init__)


def test_ast_instanceinitstatement_constructor_args():
    sig = inspect.signature(ast_InstanceInitStatement.__init__)
    params = list(sig.parameters.keys())



def test_implemenationclassifierstatement_is_not_abstract():
    assert not inspect.isabstract(ImplemenationClassifierStatement)


def test_implemenationclassifierstatement_constructor_exists():
    assert callable(ImplemenationClassifierStatement.__init__)


def test_implemenationclassifierstatement_constructor_args():
    sig = inspect.signature(ImplemenationClassifierStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_enumstatement_is_not_abstract():
    assert not inspect.isabstract(ast_EnumStatement)


def test_ast_enumstatement_constructor_exists():
    assert callable(ast_EnumStatement.__init__)


def test_ast_enumstatement_constructor_args():
    sig = inspect.signature(ast_EnumStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_classstatement_is_not_abstract():
    assert not inspect.isabstract(ast_ClassStatement)


def test_ast_classstatement_constructor_exists():
    assert callable(ast_ClassStatement.__init__)


def test_ast_classstatement_constructor_args():
    sig = inspect.signature(ast_ClassStatement.__init__)
    params = list(sig.parameters.keys())



def test_classifiermemberstatement_is_not_abstract():
    assert not inspect.isabstract(ClassifierMemberStatement)


def test_classifiermemberstatement_constructor_exists():
    assert callable(ClassifierMemberStatement.__init__)


def test_classifiermemberstatement_constructor_args():
    sig = inspect.signature(ClassifierMemberStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_feature_is_not_abstract():
    assert not inspect.isabstract(ast_Feature)


def test_ast_feature_constructor_exists():
    assert callable(ast_Feature.__init__)


def test_ast_feature_constructor_args():
    sig = inspect.signature(ast_Feature.__init__)
    params = list(sig.parameters.keys())



def test_ast_initstatement_is_not_abstract():
    assert not inspect.isabstract(ast_InitStatement)


def test_ast_initstatement_constructor_exists():
    assert callable(ast_InitStatement.__init__)


def test_ast_initstatement_constructor_args():
    sig = inspect.signature(ast_InitStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_innerclassifier_is_not_abstract():
    assert not inspect.isabstract(ast_InnerClassifier)


def test_ast_innerclassifier_constructor_exists():
    assert callable(ast_InnerClassifier.__init__)


def test_ast_innerclassifier_constructor_args():
    sig = inspect.signature(ast_InnerClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ast_enumliteral_is_not_abstract():
    assert not inspect.isabstract(ast_EnumLiteral)


def test_ast_enumliteral_constructor_exists():
    assert callable(ast_EnumLiteral.__init__)


def test_ast_enumliteral_constructor_args():
    sig = inspect.signature(ast_EnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ast_methodblock_is_not_abstract():
    assert not inspect.isabstract(ast_MethodBlock)


def test_ast_methodblock_constructor_exists():
    assert callable(ast_MethodBlock.__init__)


def test_ast_methodblock_constructor_args():
    sig = inspect.signature(ast_MethodBlock.__init__)
    params = list(sig.parameters.keys())



def test_behaviorfeature_is_not_abstract():
    assert not inspect.isabstract(BehaviorFeature)


def test_behaviorfeature_constructor_exists():
    assert callable(BehaviorFeature.__init__)


def test_behaviorfeature_constructor_args():
    sig = inspect.signature(BehaviorFeature.__init__)
    params = list(sig.parameters.keys())



def test_ast_methodstatement_is_not_abstract():
    assert not inspect.isabstract(ast_MethodStatement)


def test_ast_methodstatement_constructor_exists():
    assert callable(ast_MethodStatement.__init__)


def test_ast_methodstatement_constructor_args():
    sig = inspect.signature(ast_MethodStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_constructorstatement_is_not_abstract():
    assert not inspect.isabstract(ast_ConstructorStatement)


def test_ast_constructorstatement_constructor_exists():
    assert callable(ast_ConstructorStatement.__init__)


def test_ast_constructorstatement_constructor_args():
    sig = inspect.signature(ast_ConstructorStatement.__init__)
    params = list(sig.parameters.keys())



def test_ejbase_is_not_abstract():
    assert not inspect.isabstract(EJBase)


def test_ejbase_constructor_exists():
    assert callable(EJBase.__init__)


def test_ejbase_constructor_args():
    sig = inspect.signature(EJBase.__init__)
    params = list(sig.parameters.keys())



def test_ast_catchpart_is_not_abstract():
    assert not inspect.isabstract(ast_CatchPart)


def test_ast_catchpart_constructor_exists():
    assert callable(ast_CatchPart.__init__)


def test_ast_catchpart_constructor_args():
    sig = inspect.signature(ast_CatchPart.__init__)
    params = list(sig.parameters.keys())



def test_ast_classifiermemberstatement_is_not_abstract():
    assert not inspect.isabstract(ast_ClassifierMemberStatement)


def test_ast_classifiermemberstatement_constructor_exists():
    assert callable(ast_ClassifierMemberStatement.__init__)


def test_ast_classifiermemberstatement_constructor_args():
    sig = inspect.signature(ast_ClassifierMemberStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_methodcontentstatement_is_not_abstract():
    assert not inspect.isabstract(ast_MethodContentStatement)


def test_ast_methodcontentstatement_constructor_exists():
    assert callable(ast_MethodContentStatement.__init__)


def test_ast_methodcontentstatement_constructor_args():
    sig = inspect.signature(ast_MethodContentStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_classifierstatement_is_not_abstract():
    assert not inspect.isabstract(ast_ClassifierStatement)


def test_ast_classifierstatement_constructor_exists():
    assert callable(ast_ClassifierStatement.__init__)


def test_ast_classifierstatement_constructor_args():
    sig = inspect.signature(ast_ClassifierStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_switchpart_is_not_abstract():
    assert not inspect.isabstract(ast_SwitchPart)


def test_ast_switchpart_constructor_exists():
    assert callable(ast_SwitchPart.__init__)


def test_ast_switchpart_constructor_args():
    sig = inspect.signature(ast_SwitchPart.__init__)
    params = list(sig.parameters.keys())



def test_ast_toplevelstatement_is_not_abstract():
    assert not inspect.isabstract(ast_TopLevelStatement)


def test_ast_toplevelstatement_constructor_exists():
    assert callable(ast_TopLevelStatement.__init__)


def test_ast_toplevelstatement_constructor_args():
    sig = inspect.signature(ast_TopLevelStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_ifthenpart_is_not_abstract():
    assert not inspect.isabstract(ast_IfThenPart)


def test_ast_ifthenpart_constructor_exists():
    assert callable(ast_IfThenPart.__init__)


def test_ast_ifthenpart_constructor_args():
    sig = inspect.signature(ast_IfThenPart.__init__)
    params = list(sig.parameters.keys())



def test_ast_classblock_is_not_abstract():
    assert not inspect.isabstract(ast_ClassBlock)


def test_ast_classblock_constructor_exists():
    assert callable(ast_ClassBlock.__init__)


def test_ast_classblock_constructor_args():
    sig = inspect.signature(ast_ClassBlock.__init__)
    params = list(sig.parameters.keys())



def test_ast_identifier_is_not_abstract():
    assert not inspect.isabstract(ast_Identifier)


def test_ast_identifier_constructor_exists():
    assert callable(ast_Identifier.__init__)


def test_ast_identifier_constructor_args():
    sig = inspect.signature(ast_Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "quotedValue" in params, "Missing parameter 'quotedValue'"
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_ast_identifier_has_value():
    assert hasattr(ast_Identifier, "value")
    descriptor = None
    for klass in ast_Identifier.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ast_identifier_has_quotedValue():
    assert hasattr(ast_Identifier, "quotedValue")
    descriptor = None
    for klass in ast_Identifier.__mro__:
        if "quotedValue" in klass.__dict__:
            descriptor = klass.__dict__["quotedValue"]
            break
    assert isinstance(descriptor, property)

def test_ast_identifier_has_escapedValue():
    assert hasattr(ast_Identifier, "escapedValue")
    descriptor = None
    for klass in ast_Identifier.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_ast_behaviorfeature_is_not_abstract():
    assert not inspect.isabstract(ast_BehaviorFeature)


def test_ast_behaviorfeature_constructor_exists():
    assert callable(ast_BehaviorFeature.__init__)


def test_ast_behaviorfeature_constructor_args():
    sig = inspect.signature(ast_BehaviorFeature.__init__)
    params = list(sig.parameters.keys())



def test_ast_fieldstatement_is_not_abstract():
    assert not inspect.isabstract(ast_FieldStatement)


def test_ast_fieldstatement_constructor_exists():
    assert callable(ast_FieldStatement.__init__)


def test_ast_fieldstatement_constructor_args():
    sig = inspect.signature(ast_FieldStatement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ast_templateparameter_is_not_abstract():
    assert not inspect.isabstract(ast_TemplateParameter)


def test_ast_templateparameter_constructor_exists():
    assert callable(ast_TemplateParameter.__init__)


def test_ast_templateparameter_constructor_args():
    sig = inspect.signature(ast_TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_ast_variable_is_not_abstract():
    assert not inspect.isabstract(ast_Variable)


def test_ast_variable_constructor_exists():
    assert callable(ast_Variable.__init__)


def test_ast_variable_constructor_args():
    sig = inspect.signature(ast_Variable.__init__)
    params = list(sig.parameters.keys())



def test_ast_parameter_is_not_abstract():
    assert not inspect.isabstract(ast_Parameter)


def test_ast_parameter_constructor_exists():
    assert callable(ast_Parameter.__init__)


def test_ast_parameter_constructor_args():
    sig = inspect.signature(ast_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_ast_expression_is_not_abstract():
    assert not inspect.isabstract(ast_Expression)


def test_ast_expression_constructor_exists():
    assert callable(ast_Expression.__init__)


def test_ast_expression_constructor_args():
    sig = inspect.signature(ast_Expression.__init__)
    params = list(sig.parameters.keys())



def test_ejelement_is_not_abstract():
    assert not inspect.isabstract(EJElement)


def test_ejelement_constructor_exists():
    assert callable(EJElement.__init__)


def test_ejelement_constructor_args():
    sig = inspect.signature(EJElement.__init__)
    params = list(sig.parameters.keys())



def test_ast_switchdefaultpartref_is_not_abstract():
    assert not inspect.isabstract(ast_SwitchDefaultPartRef)


def test_ast_switchdefaultpartref_constructor_exists():
    assert callable(ast_SwitchDefaultPartRef.__init__)


def test_ast_switchdefaultpartref_constructor_args():
    sig = inspect.signature(ast_SwitchDefaultPartRef.__init__)
    params = list(sig.parameters.keys())



def test_ast_attributeset_is_not_abstract():
    assert not inspect.isabstract(ast_AttributeSet)


def test_ast_attributeset_constructor_exists():
    assert callable(ast_AttributeSet.__init__)


def test_ast_attributeset_constructor_args():
    sig = inspect.signature(ast_AttributeSet.__init__)
    params = list(sig.parameters.keys())



def test_ast_modifier_is_not_abstract():
    assert not inspect.isabstract(ast_Modifier)


def test_ast_modifier_constructor_exists():
    assert callable(ast_Modifier.__init__)


def test_ast_modifier_constructor_args():
    sig = inspect.signature(ast_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ast_modifier_has_value():
    assert hasattr(ast_Modifier, "value")
    descriptor = None
    for klass in ast_Modifier.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ast_label_is_not_abstract():
    assert not inspect.isabstract(ast_Label)


def test_ast_label_constructor_exists():
    assert callable(ast_Label.__init__)


def test_ast_label_constructor_args():
    sig = inspect.signature(ast_Label.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast_label_has_name():
    assert hasattr(ast_Label, "name")
    descriptor = None
    for klass in ast_Label.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast_documentationline_is_not_abstract():
    assert not inspect.isabstract(ast_DocumentationLine)


def test_ast_documentationline_constructor_exists():
    assert callable(ast_DocumentationLine.__init__)


def test_ast_documentationline_constructor_args():
    sig = inspect.signature(ast_DocumentationLine.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_ast_documentationline_has_text():
    assert hasattr(ast_DocumentationLine, "text")
    descriptor = None
    for klass in ast_DocumentationLine.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_ast_ejbase_is_not_abstract():
    assert not inspect.isabstract(ast_EJBase)


def test_ast_ejbase_constructor_exists():
    assert callable(ast_EJBase.__init__)


def test_ast_ejbase_constructor_args():
    sig = inspect.signature(ast_EJBase.__init__)
    params = list(sig.parameters.keys())



def test_ast_ejelement_is_not_abstract():
    assert not inspect.isabstract(ast_EJElement)


def test_ast_ejelement_constructor_exists():
    assert callable(ast_EJElement.__init__)


def test_ast_ejelement_constructor_args():
    sig = inspect.signature(ast_EJElement.__init__)
    params = list(sig.parameters.keys())
    assert "startLine" in params, "Missing parameter 'startLine'"
    assert "endLine" in params, "Missing parameter 'endLine'"
    assert "startOffset" in params, "Missing parameter 'startOffset'"
    assert "endColumn" in params, "Missing parameter 'endColumn'"
    assert "startColumn" in params, "Missing parameter 'startColumn'"
    assert "endOffset" in params, "Missing parameter 'endOffset'"

def test_ast_ejelement_has_startLine():
    assert hasattr(ast_EJElement, "startLine")
    descriptor = None
    for klass in ast_EJElement.__mro__:
        if "startLine" in klass.__dict__:
            descriptor = klass.__dict__["startLine"]
            break
    assert isinstance(descriptor, property)

def test_ast_ejelement_has_endLine():
    assert hasattr(ast_EJElement, "endLine")
    descriptor = None
    for klass in ast_EJElement.__mro__:
        if "endLine" in klass.__dict__:
            descriptor = klass.__dict__["endLine"]
            break
    assert isinstance(descriptor, property)

def test_ast_ejelement_has_startOffset():
    assert hasattr(ast_EJElement, "startOffset")
    descriptor = None
    for klass in ast_EJElement.__mro__:
        if "startOffset" in klass.__dict__:
            descriptor = klass.__dict__["startOffset"]
            break
    assert isinstance(descriptor, property)

def test_ast_ejelement_has_endColumn():
    assert hasattr(ast_EJElement, "endColumn")
    descriptor = None
    for klass in ast_EJElement.__mro__:
        if "endColumn" in klass.__dict__:
            descriptor = klass.__dict__["endColumn"]
            break
    assert isinstance(descriptor, property)

def test_ast_ejelement_has_startColumn():
    assert hasattr(ast_EJElement, "startColumn")
    descriptor = None
    for klass in ast_EJElement.__mro__:
        if "startColumn" in klass.__dict__:
            descriptor = klass.__dict__["startColumn"]
            break
    assert isinstance(descriptor, property)

def test_ast_ejelement_has_endOffset():
    assert hasattr(ast_EJElement, "endOffset")
    descriptor = None
    for klass in ast_EJElement.__mro__:
        if "endOffset" in klass.__dict__:
            descriptor = klass.__dict__["endOffset"]
            break
    assert isinstance(descriptor, property)



def test_ast_attributedefinition_is_not_abstract():
    assert not inspect.isabstract(ast_AttributeDefinition)


def test_ast_attributedefinition_constructor_exists():
    assert callable(ast_AttributeDefinition.__init__)


def test_ast_attributedefinition_constructor_args():
    sig = inspect.signature(ast_AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ast_emptystatement_is_not_abstract():
    assert not inspect.isabstract(ast_EmptyStatement)


def test_ast_emptystatement_constructor_exists():
    assert callable(ast_EmptyStatement.__init__)


def test_ast_emptystatement_constructor_args():
    sig = inspect.signature(ast_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_wildcardtype_is_not_abstract():
    assert not inspect.isabstract(ast_WildcardType)


def test_ast_wildcardtype_constructor_exists():
    assert callable(ast_WildcardType.__init__)


def test_ast_wildcardtype_constructor_args():
    sig = inspect.signature(ast_WildcardType.__init__)
    params = list(sig.parameters.keys())



def test_ast_rangeexpression_is_not_abstract():
    assert not inspect.isabstract(ast_RangeExpression)


def test_ast_rangeexpression_constructor_exists():
    assert callable(ast_RangeExpression.__init__)


def test_ast_rangeexpression_constructor_args():
    sig = inspect.signature(ast_RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_ast_assertstatement_is_not_abstract():
    assert not inspect.isabstract(ast_AssertStatement)


def test_ast_assertstatement_constructor_exists():
    assert callable(ast_AssertStatement.__init__)


def test_ast_assertstatement_constructor_args():
    sig = inspect.signature(ast_AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_namedelement_is_not_abstract():
    assert not inspect.isabstract(ast_NamedElement)


def test_ast_namedelement_constructor_exists():
    assert callable(ast_NamedElement.__init__)


def test_ast_namedelement_constructor_args():
    sig = inspect.signature(ast_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ast_unaryop_is_not_abstract():
    assert not inspect.isabstract(ast_UnaryOp)


def test_ast_unaryop_constructor_exists():
    assert callable(ast_UnaryOp.__init__)


def test_ast_unaryop_constructor_args():
    sig = inspect.signature(ast_UnaryOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_thisreference_is_not_abstract():
    assert not inspect.isabstract(ast_ThisReference)


def test_ast_thisreference_constructor_exists():
    assert callable(ast_ThisReference.__init__)


def test_ast_thisreference_constructor_args():
    sig = inspect.signature(ast_ThisReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast_thisreference_has_name():
    assert hasattr(ast_ThisReference, "name")
    descriptor = None
    for klass in ast_ThisReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast_superreference_is_not_abstract():
    assert not inspect.isabstract(ast_SuperReference)


def test_ast_superreference_constructor_exists():
    assert callable(ast_SuperReference.__init__)


def test_ast_superreference_constructor_args():
    sig = inspect.signature(ast_SuperReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast_superreference_has_name():
    assert hasattr(ast_SuperReference, "name")
    descriptor = None
    for klass in ast_SuperReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast_shiftop_is_not_abstract():
    assert not inspect.isabstract(ast_ShiftOp)


def test_ast_shiftop_constructor_exists():
    assert callable(ast_ShiftOp.__init__)


def test_ast_shiftop_constructor_args():
    sig = inspect.signature(ast_ShiftOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_returnstatement_is_not_abstract():
    assert not inspect.isabstract(ast_ReturnStatement)


def test_ast_returnstatement_constructor_exists():
    assert callable(ast_ReturnStatement.__init__)


def test_ast_returnstatement_constructor_args():
    sig = inspect.signature(ast_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_ast_primitivetype_is_not_abstract():
    assert not inspect.isabstract(ast_PrimitiveType)


def test_ast_primitivetype_constructor_exists():
    assert callable(ast_PrimitiveType.__init__)


def test_ast_primitivetype_constructor_args():
    sig = inspect.signature(ast_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ast_primitivetype_has_name():
    assert hasattr(ast_PrimitiveType, "name")
    descriptor = None
    for klass in ast_PrimitiveType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ast_newop_is_not_abstract():
    assert not inspect.isabstract(ast_NewOp)


def test_ast_newop_constructor_exists():
    assert callable(ast_NewOp.__init__)


def test_ast_newop_constructor_args():
    sig = inspect.signature(ast_NewOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_multiplyop_is_not_abstract():
    assert not inspect.isabstract(ast_MultiplyOp)


def test_ast_multiplyop_constructor_exists():
    assert callable(ast_MultiplyOp.__init__)


def test_ast_multiplyop_constructor_args():
    sig = inspect.signature(ast_MultiplyOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_minusop_is_not_abstract():
    assert not inspect.isabstract(ast_MinusOp)


def test_ast_minusop_constructor_exists():
    assert callable(ast_MinusOp.__init__)


def test_ast_minusop_constructor_args():
    sig = inspect.signature(ast_MinusOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_literal_is_not_abstract():
    assert not inspect.isabstract(ast_Literal)


def test_ast_literal_constructor_exists():
    assert callable(ast_Literal.__init__)


def test_ast_literal_constructor_args():
    sig = inspect.signature(ast_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ast_literal_has_value():
    assert hasattr(ast_Literal, "value")
    descriptor = None
    for klass in ast_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ast_plusop_is_not_abstract():
    assert not inspect.isabstract(ast_PlusOp)


def test_ast_plusop_constructor_exists():
    assert callable(ast_PlusOp.__init__)


def test_ast_plusop_constructor_args():
    sig = inspect.signature(ast_PlusOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_identityop_is_not_abstract():
    assert not inspect.isabstract(ast_IdentityOp)


def test_ast_identityop_constructor_exists():
    assert callable(ast_IdentityOp.__init__)


def test_ast_identityop_constructor_args():
    sig = inspect.signature(ast_IdentityOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_divisionop_is_not_abstract():
    assert not inspect.isabstract(ast_DivisionOp)


def test_ast_divisionop_constructor_exists():
    assert callable(ast_DivisionOp.__init__)


def test_ast_divisionop_constructor_args():
    sig = inspect.signature(ast_DivisionOp.__init__)
    params = list(sig.parameters.keys())



def test_divisionop_is_not_abstract():
    assert not inspect.isabstract(DivisionOp)


def test_divisionop_constructor_exists():
    assert callable(DivisionOp.__init__)


def test_divisionop_constructor_args():
    sig = inspect.signature(DivisionOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_remainderop_is_not_abstract():
    assert not inspect.isabstract(ast_RemainderOp)


def test_ast_remainderop_constructor_exists():
    assert callable(ast_RemainderOp.__init__)


def test_ast_remainderop_constructor_args():
    sig = inspect.signature(ast_RemainderOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_divideop_is_not_abstract():
    assert not inspect.isabstract(ast_DivideOp)


def test_ast_divideop_constructor_exists():
    assert callable(ast_DivideOp.__init__)


def test_ast_divideop_constructor_args():
    sig = inspect.signature(ast_DivideOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_conditionalop_is_not_abstract():
    assert not inspect.isabstract(ast_ConditionalOp)


def test_ast_conditionalop_constructor_exists():
    assert callable(ast_ConditionalOp.__init__)


def test_ast_conditionalop_constructor_args():
    sig = inspect.signature(ast_ConditionalOp.__init__)
    params = list(sig.parameters.keys())



def test_shiftop_is_not_abstract():
    assert not inspect.isabstract(ShiftOp)


def test_shiftop_constructor_exists():
    assert callable(ShiftOp.__init__)


def test_shiftop_constructor_args():
    sig = inspect.signature(ShiftOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_rightshiftop_is_not_abstract():
    assert not inspect.isabstract(ast_RightShiftOp)


def test_ast_rightshiftop_constructor_exists():
    assert callable(ast_RightShiftOp.__init__)


def test_ast_rightshiftop_constructor_args():
    sig = inspect.signature(ast_RightShiftOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_zeroextensionrightshiftop_is_not_abstract():
    assert not inspect.isabstract(ast_ZeroExtensionRightShiftOp)


def test_ast_zeroextensionrightshiftop_constructor_exists():
    assert callable(ast_ZeroExtensionRightShiftOp.__init__)


def test_ast_zeroextensionrightshiftop_constructor_args():
    sig = inspect.signature(ast_ZeroExtensionRightShiftOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_leftshiftop_is_not_abstract():
    assert not inspect.isabstract(ast_LeftShiftOp)


def test_ast_leftshiftop_constructor_exists():
    assert callable(ast_LeftShiftOp.__init__)


def test_ast_leftshiftop_constructor_args():
    sig = inspect.signature(ast_LeftShiftOp.__init__)
    params = list(sig.parameters.keys())



def test_classifierop_is_not_abstract():
    assert not inspect.isabstract(ClassifierOp)


def test_classifierop_constructor_exists():
    assert callable(ClassifierOp.__init__)


def test_classifierop_constructor_args():
    sig = inspect.signature(ClassifierOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_instanceofop_is_not_abstract():
    assert not inspect.isabstract(ast_InstanceOfOp)


def test_ast_instanceofop_constructor_exists():
    assert callable(ast_InstanceOfOp.__init__)


def test_ast_instanceofop_constructor_args():
    sig = inspect.signature(ast_InstanceOfOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_castop_is_not_abstract():
    assert not inspect.isabstract(ast_CastOp)


def test_ast_castop_constructor_exists():
    assert callable(ast_CastOp.__init__)


def test_ast_castop_constructor_args():
    sig = inspect.signature(ast_CastOp.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_ast_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(ast_DoubleLiteral)


def test_ast_doubleliteral_constructor_exists():
    assert callable(ast_DoubleLiteral.__init__)


def test_ast_doubleliteral_constructor_args():
    sig = inspect.signature(ast_DoubleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ast_longintegerliteral_is_not_abstract():
    assert not inspect.isabstract(ast_LongIntegerLiteral)


def test_ast_longintegerliteral_constructor_exists():
    assert callable(ast_LongIntegerLiteral.__init__)


def test_ast_longintegerliteral_constructor_args():
    sig = inspect.signature(ast_LongIntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ast_nullreference_is_not_abstract():
    assert not inspect.isabstract(ast_NullReference)


def test_ast_nullreference_constructor_exists():
    assert callable(ast_NullReference.__init__)


def test_ast_nullreference_constructor_args():
    sig = inspect.signature(ast_NullReference.__init__)
    params = list(sig.parameters.keys())



def test_ast_floatliteral_is_not_abstract():
    assert not inspect.isabstract(ast_FloatLiteral)


def test_ast_floatliteral_constructor_exists():
    assert callable(ast_FloatLiteral.__init__)


def test_ast_floatliteral_constructor_args():
    sig = inspect.signature(ast_FloatLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ast_integerliteral_is_not_abstract():
    assert not inspect.isabstract(ast_IntegerLiteral)


def test_ast_integerliteral_constructor_exists():
    assert callable(ast_IntegerLiteral.__init__)


def test_ast_integerliteral_constructor_args():
    sig = inspect.signature(ast_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ast_stringliteral_is_not_abstract():
    assert not inspect.isabstract(ast_StringLiteral)


def test_ast_stringliteral_constructor_exists():
    assert callable(ast_StringLiteral.__init__)


def test_ast_stringliteral_constructor_args():
    sig = inspect.signature(ast_StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ast_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(ast_BooleanLiteral)


def test_ast_booleanliteral_constructor_exists():
    assert callable(ast_BooleanLiteral.__init__)


def test_ast_booleanliteral_constructor_args():
    sig = inspect.signature(ast_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_unaryop_is_not_abstract():
    assert not inspect.isabstract(UnaryOp)


def test_unaryop_constructor_exists():
    assert callable(UnaryOp.__init__)


def test_unaryop_constructor_args():
    sig = inspect.signature(UnaryOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_postfixdecrementop_is_not_abstract():
    assert not inspect.isabstract(ast_PostfixDecrementOp)


def test_ast_postfixdecrementop_constructor_exists():
    assert callable(ast_PostfixDecrementOp.__init__)


def test_ast_postfixdecrementop_constructor_args():
    sig = inspect.signature(ast_PostfixDecrementOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_postfixincrementop_is_not_abstract():
    assert not inspect.isabstract(ast_PostfixIncrementOp)


def test_ast_postfixincrementop_constructor_exists():
    assert callable(ast_PostfixIncrementOp.__init__)


def test_ast_postfixincrementop_constructor_args():
    sig = inspect.signature(ast_PostfixIncrementOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_logicalcomplementop_is_not_abstract():
    assert not inspect.isabstract(ast_LogicalComplementOp)


def test_ast_logicalcomplementop_constructor_exists():
    assert callable(ast_LogicalComplementOp.__init__)


def test_ast_logicalcomplementop_constructor_args():
    sig = inspect.signature(ast_LogicalComplementOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_prefixincrementop_is_not_abstract():
    assert not inspect.isabstract(ast_PrefixIncrementOp)


def test_ast_prefixincrementop_constructor_exists():
    assert callable(ast_PrefixIncrementOp.__init__)


def test_ast_prefixincrementop_constructor_args():
    sig = inspect.signature(ast_PrefixIncrementOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_unaryplusop_is_not_abstract():
    assert not inspect.isabstract(ast_UnaryPlusOp)


def test_ast_unaryplusop_constructor_exists():
    assert callable(ast_UnaryPlusOp.__init__)


def test_ast_unaryplusop_constructor_args():
    sig = inspect.signature(ast_UnaryPlusOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_unaryminusop_is_not_abstract():
    assert not inspect.isabstract(ast_UnaryMinusOp)


def test_ast_unaryminusop_constructor_exists():
    assert callable(ast_UnaryMinusOp.__init__)


def test_ast_unaryminusop_constructor_args():
    sig = inspect.signature(ast_UnaryMinusOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_prefixdecrementop_is_not_abstract():
    assert not inspect.isabstract(ast_PrefixDecrementOp)


def test_ast_prefixdecrementop_constructor_exists():
    assert callable(ast_PrefixDecrementOp.__init__)


def test_ast_prefixdecrementop_constructor_args():
    sig = inspect.signature(ast_PrefixDecrementOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_bitwisecomplementop_is_not_abstract():
    assert not inspect.isabstract(ast_BitwiseComplementOp)


def test_ast_bitwisecomplementop_constructor_exists():
    assert callable(ast_BitwiseComplementOp.__init__)


def test_ast_bitwisecomplementop_constructor_args():
    sig = inspect.signature(ast_BitwiseComplementOp.__init__)
    params = list(sig.parameters.keys())



def test_binaryop_is_not_abstract():
    assert not inspect.isabstract(BinaryOp)


def test_binaryop_constructor_exists():
    assert callable(BinaryOp.__init__)


def test_binaryop_constructor_args():
    sig = inspect.signature(BinaryOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_lessthenop_is_not_abstract():
    assert not inspect.isabstract(ast_LessThenOp)


def test_ast_lessthenop_constructor_exists():
    assert callable(ast_LessThenOp.__init__)


def test_ast_lessthenop_constructor_args():
    sig = inspect.signature(ast_LessThenOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_greaterorequalop_is_not_abstract():
    assert not inspect.isabstract(ast_GreaterOrEqualOp)


def test_ast_greaterorequalop_constructor_exists():
    assert callable(ast_GreaterOrEqualOp.__init__)


def test_ast_greaterorequalop_constructor_args():
    sig = inspect.signature(ast_GreaterOrEqualOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_bitwisexorop_is_not_abstract():
    assert not inspect.isabstract(ast_BitwiseXorOp)


def test_ast_bitwisexorop_constructor_exists():
    assert callable(ast_BitwiseXorOp.__init__)


def test_ast_bitwisexorop_constructor_args():
    sig = inspect.signature(ast_BitwiseXorOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_lessorequalop_is_not_abstract():
    assert not inspect.isabstract(ast_LessOrEqualOp)


def test_ast_lessorequalop_constructor_exists():
    assert callable(ast_LessOrEqualOp.__init__)


def test_ast_lessorequalop_constructor_args():
    sig = inspect.signature(ast_LessOrEqualOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_conditionalorop_is_not_abstract():
    assert not inspect.isabstract(ast_ConditionalOrOp)


def test_ast_conditionalorop_constructor_exists():
    assert callable(ast_ConditionalOrOp.__init__)


def test_ast_conditionalorop_constructor_args():
    sig = inspect.signature(ast_ConditionalOrOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_notequalop_is_not_abstract():
    assert not inspect.isabstract(ast_NotEqualOp)


def test_ast_notequalop_constructor_exists():
    assert callable(ast_NotEqualOp.__init__)


def test_ast_notequalop_constructor_args():
    sig = inspect.signature(ast_NotEqualOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_bitwiseorop_is_not_abstract():
    assert not inspect.isabstract(ast_BitwiseOrOp)


def test_ast_bitwiseorop_constructor_exists():
    assert callable(ast_BitwiseOrOp.__init__)


def test_ast_bitwiseorop_constructor_args():
    sig = inspect.signature(ast_BitwiseOrOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_equalop_is_not_abstract():
    assert not inspect.isabstract(ast_EqualOp)


def test_ast_equalop_constructor_exists():
    assert callable(ast_EqualOp.__init__)


def test_ast_equalop_constructor_args():
    sig = inspect.signature(ast_EqualOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_greaterthenop_is_not_abstract():
    assert not inspect.isabstract(ast_GreaterThenOp)


def test_ast_greaterthenop_constructor_exists():
    assert callable(ast_GreaterThenOp.__init__)


def test_ast_greaterthenop_constructor_args():
    sig = inspect.signature(ast_GreaterThenOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_bitwiseandop_is_not_abstract():
    assert not inspect.isabstract(ast_BitwiseAndOp)


def test_ast_bitwiseandop_constructor_exists():
    assert callable(ast_BitwiseAndOp.__init__)


def test_ast_bitwiseandop_constructor_args():
    sig = inspect.signature(ast_BitwiseAndOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_binaryop_is_not_abstract():
    assert not inspect.isabstract(ast_BinaryOp)


def test_ast_binaryop_constructor_exists():
    assert callable(ast_BinaryOp.__init__)


def test_ast_binaryop_constructor_args():
    sig = inspect.signature(ast_BinaryOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_assignmentoperation_is_not_abstract():
    assert not inspect.isabstract(ast_AssignmentOperation)


def test_ast_assignmentoperation_constructor_exists():
    assert callable(ast_AssignmentOperation.__init__)


def test_ast_assignmentoperation_constructor_args():
    sig = inspect.signature(ast_AssignmentOperation.__init__)
    params = list(sig.parameters.keys())



def test_assignmentoperation_is_not_abstract():
    assert not inspect.isabstract(AssignmentOperation)


def test_assignmentoperation_constructor_exists():
    assert callable(AssignmentOperation.__init__)


def test_assignmentoperation_constructor_args():
    sig = inspect.signature(AssignmentOperation.__init__)
    params = list(sig.parameters.keys())



def test_ast_zeroextensionrightshiftassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast_ZeroExtensionRightShiftAssignmentOp)


def test_ast_zeroextensionrightshiftassignmentop_constructor_exists():
    assert callable(ast_ZeroExtensionRightShiftAssignmentOp.__init__)


def test_ast_zeroextensionrightshiftassignmentop_constructor_args():
    sig = inspect.signature(ast_ZeroExtensionRightShiftAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_minusassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast_MinusAssignmentOp)


def test_ast_minusassignmentop_constructor_exists():
    assert callable(ast_MinusAssignmentOp.__init__)


def test_ast_minusassignmentop_constructor_args():
    sig = inspect.signature(ast_MinusAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_bitwisexorassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast_BitwiseXorAssignmentOp)


def test_ast_bitwisexorassignmentop_constructor_exists():
    assert callable(ast_BitwiseXorAssignmentOp.__init__)


def test_ast_bitwisexorassignmentop_constructor_args():
    sig = inspect.signature(ast_BitwiseXorAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_remainderassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast_RemainderAssignmentOp)


def test_ast_remainderassignmentop_constructor_exists():
    assert callable(ast_RemainderAssignmentOp.__init__)


def test_ast_remainderassignmentop_constructor_args():
    sig = inspect.signature(ast_RemainderAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_multiplyassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast_MultiplyAssignmentOp)


def test_ast_multiplyassignmentop_constructor_exists():
    assert callable(ast_MultiplyAssignmentOp.__init__)


def test_ast_multiplyassignmentop_constructor_args():
    sig = inspect.signature(ast_MultiplyAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_plusassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast_PlusAssignmentOp)


def test_ast_plusassignmentop_constructor_exists():
    assert callable(ast_PlusAssignmentOp.__init__)


def test_ast_plusassignmentop_constructor_args():
    sig = inspect.signature(ast_PlusAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_bitwiseandassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast_BitwiseAndAssignmentOp)


def test_ast_bitwiseandassignmentop_constructor_exists():
    assert callable(ast_BitwiseAndAssignmentOp.__init__)


def test_ast_bitwiseandassignmentop_constructor_args():
    sig = inspect.signature(ast_BitwiseAndAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_bitwiseorassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast_BitwiseOrAssignmentOp)


def test_ast_bitwiseorassignmentop_constructor_exists():
    assert callable(ast_BitwiseOrAssignmentOp.__init__)


def test_ast_bitwiseorassignmentop_constructor_args():
    sig = inspect.signature(ast_BitwiseOrAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_leftshiftassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast_LeftShiftAssignmentOp)


def test_ast_leftshiftassignmentop_constructor_exists():
    assert callable(ast_LeftShiftAssignmentOp.__init__)


def test_ast_leftshiftassignmentop_constructor_args():
    sig = inspect.signature(ast_LeftShiftAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_divideassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast_DivideAssignmentOp)


def test_ast_divideassignmentop_constructor_exists():
    assert callable(ast_DivideAssignmentOp.__init__)


def test_ast_divideassignmentop_constructor_args():
    sig = inspect.signature(ast_DivideAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_rightshiftassignmentop_is_not_abstract():
    assert not inspect.isabstract(ast_RightShiftAssignmentOp)


def test_ast_rightshiftassignmentop_constructor_exists():
    assert callable(ast_RightShiftAssignmentOp.__init__)


def test_ast_rightshiftassignmentop_constructor_args():
    sig = inspect.signature(ast_RightShiftAssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_assignmentop_is_not_abstract():
    assert not inspect.isabstract(ast_AssignmentOp)


def test_ast_assignmentop_constructor_exists():
    assert callable(ast_AssignmentOp.__init__)


def test_ast_assignmentop_constructor_args():
    sig = inspect.signature(ast_AssignmentOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_arrayconstructor_is_not_abstract():
    assert not inspect.isabstract(ast_ArrayConstructor)


def test_ast_arrayconstructor_constructor_exists():
    assert callable(ast_ArrayConstructor.__init__)


def test_ast_arrayconstructor_constructor_args():
    sig = inspect.signature(ast_ArrayConstructor.__init__)
    params = list(sig.parameters.keys())



def test_ast_conditionalandop_is_not_abstract():
    assert not inspect.isabstract(ast_ConditionalAndOp)


def test_ast_conditionalandop_constructor_exists():
    assert callable(ast_ConditionalAndOp.__init__)


def test_ast_conditionalandop_constructor_args():
    sig = inspect.signature(ast_ConditionalAndOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_classifierop_is_not_abstract():
    assert not inspect.isabstract(ast_ClassifierOp)


def test_ast_classifierop_constructor_exists():
    assert callable(ast_ClassifierOp.__init__)


def test_ast_classifierop_constructor_args():
    sig = inspect.signature(ast_ClassifierOp.__init__)
    params = list(sig.parameters.keys())



def test_ast_characterliteral_is_not_abstract():
    assert not inspect.isabstract(ast_CharacterLiteral)


def test_ast_characterliteral_constructor_exists():
    assert callable(ast_CharacterLiteral.__init__)


def test_ast_characterliteral_constructor_args():
    sig = inspect.signature(ast_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ast_applyroundop_is_not_abstract():
    assert not inspect.isabstract(ast_ApplyRoundOp)


def test_ast_applyroundop_constructor_exists():
    assert callable(ast_ApplyRoundOp.__init__)


def test_ast_applyroundop_constructor_args():
    sig = inspect.signature(ast_ApplyRoundOp.__init__)
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
Expression_strategy = st.builds(
    Expression,
)
ast_AccessOp_strategy = st.builds(
    ast_AccessOp,
)
ScopeStatement_strategy = st.builds(
    ScopeStatement,
)
ast_TryStatement_strategy = st.builds(
    ast_TryStatement,
)
ast_SynchronizedStatement_strategy = st.builds(
    ast_SynchronizedStatement,
)
ast_ApplySquareOp_strategy = st.builds(
    ast_ApplySquareOp,
)
LabeledStatement_strategy = st.builds(
    LabeledStatement,
)
ast_SwitchStatement_strategy = st.builds(
    ast_SwitchStatement,
)
ast_LoopStatement_strategy = st.builds(
    ast_LoopStatement,
)
SwitchPart_strategy = st.builds(
    SwitchPart,
)
ast_SwitchDefaultPart_strategy = st.builds(
    ast_SwitchDefaultPart,
)
ast_SwitchCasePart_strategy = st.builds(
    ast_SwitchCasePart,
)
MethodContentStatement_strategy = st.builds(
    MethodContentStatement,
)
ast_MethodClassifier_strategy = st.builds(
    ast_MethodClassifier,
)
ast_ThrowStatement_strategy = st.builds(
    ast_ThrowStatement,
)
ast_LabeledStatement_strategy = st.builds(
    ast_LabeledStatement,
)
ast_IfStatement_strategy = st.builds(
    ast_IfStatement,
)
ast_LocalVarStatement_strategy = st.builds(
    ast_LocalVarStatement,
)
ast_JumpStatement_strategy = st.builds(
    ast_JumpStatement,
)
ast_ScopeStatement_strategy = st.builds(
    ast_ScopeStatement,
)
ast_ExpressionStatement_strategy = st.builds(
    ast_ExpressionStatement,
)
ConditionalLoop_strategy = st.builds(
    ConditionalLoop,
)
ast_WhileStatement_strategy = st.builds(
    ast_WhileStatement,
)
ast_ForStatement_strategy = st.builds(
    ast_ForStatement,
)
ast_DoWhileStatement_strategy = st.builds(
    ast_DoWhileStatement,
)
TopLevelStatement_strategy = st.builds(
    TopLevelStatement,
)
ast_TopLevelClassifier_strategy = st.builds(
    ast_TopLevelClassifier,
)
ast_PackageStatement_strategy = st.builds(
    ast_PackageStatement,
)
ast_ImportStatement_strategy = st.builds(
    ast_ImportStatement,
)
ClassifierStatement_strategy = st.builds(
    ClassifierStatement,
)
ast_InterfaceStatement_strategy = st.builds(
    ast_InterfaceStatement,
)
ast_ImplemenationClassifierStatement_strategy = st.builds(
    ast_ImplemenationClassifierStatement,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
ast_ForeachStatement_strategy = st.builds(
    ast_ForeachStatement,
)
ast_ConditionalLoop_strategy = st.builds(
    ast_ConditionalLoop,
)
JumpStatement_strategy = st.builds(
    JumpStatement,
)
ast_ContinueStatement_strategy = st.builds(
    ast_ContinueStatement,
)
ast_BreakStatement_strategy = st.builds(
    ast_BreakStatement,
)
InitStatement_strategy = st.builds(
    InitStatement,
)
ast_StaticInitStatement_strategy = st.builds(
    ast_StaticInitStatement,
)
ast_InstanceInitStatement_strategy = st.builds(
    ast_InstanceInitStatement,
)
ImplemenationClassifierStatement_strategy = st.builds(
    ImplemenationClassifierStatement,
)
ast_EnumStatement_strategy = st.builds(
    ast_EnumStatement,
)
ast_ClassStatement_strategy = st.builds(
    ast_ClassStatement,
)
ClassifierMemberStatement_strategy = st.builds(
    ClassifierMemberStatement,
)
ast_Feature_strategy = st.builds(
    ast_Feature,
)
ast_InitStatement_strategy = st.builds(
    ast_InitStatement,
)
ast_InnerClassifier_strategy = st.builds(
    ast_InnerClassifier,
)
ast_EnumLiteral_strategy = st.builds(
    ast_EnumLiteral,
)
ast_MethodBlock_strategy = st.builds(
    ast_MethodBlock,
)
BehaviorFeature_strategy = st.builds(
    BehaviorFeature,
)
ast_MethodStatement_strategy = st.builds(
    ast_MethodStatement,
)
ast_ConstructorStatement_strategy = st.builds(
    ast_ConstructorStatement,
)
EJBase_strategy = st.builds(
    EJBase,
)
ast_CatchPart_strategy = st.builds(
    ast_CatchPart,
)
ast_ClassifierMemberStatement_strategy = st.builds(
    ast_ClassifierMemberStatement,
)
ast_MethodContentStatement_strategy = st.builds(
    ast_MethodContentStatement,
)
ast_ClassifierStatement_strategy = st.builds(
    ast_ClassifierStatement,
)
ast_SwitchPart_strategy = st.builds(
    ast_SwitchPart,
)
ast_TopLevelStatement_strategy = st.builds(
    ast_TopLevelStatement,
)
ast_IfThenPart_strategy = st.builds(
    ast_IfThenPart,
)
ast_ClassBlock_strategy = st.builds(
    ast_ClassBlock,
)
ast_Identifier_strategy = st.builds(
    ast_Identifier,
    value=
        safe_text,
    quotedValue=
        safe_text,
    escapedValue=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
ast_BehaviorFeature_strategy = st.builds(
    ast_BehaviorFeature,
)
ast_FieldStatement_strategy = st.builds(
    ast_FieldStatement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ast_TemplateParameter_strategy = st.builds(
    ast_TemplateParameter,
)
ast_Variable_strategy = st.builds(
    ast_Variable,
)
ast_Parameter_strategy = st.builds(
    ast_Parameter,
)
ast_Expression_strategy = st.builds(
    ast_Expression,
)
EJElement_strategy = st.builds(
    EJElement,
)
ast_SwitchDefaultPartRef_strategy = st.builds(
    ast_SwitchDefaultPartRef,
)
ast_AttributeSet_strategy = st.builds(
    ast_AttributeSet,
)
ast_Modifier_strategy = st.builds(
    ast_Modifier,
    value=
        safe_text
)
ast_Label_strategy = st.builds(
    ast_Label,
    name=
        safe_text
)
ast_DocumentationLine_strategy = st.builds(
    ast_DocumentationLine,
    text=
        safe_text
)
ast_EJBase_strategy = st.builds(
    ast_EJBase,
)
ast_EJElement_strategy = st.builds(
    ast_EJElement,
    startLine=
        st.integers(),
    endLine=
        st.integers(),
    startOffset=
        safe_text,
    endColumn=
        st.integers(),
    startColumn=
        st.integers(),
    endOffset=
        safe_text
)
ast_AttributeDefinition_strategy = st.builds(
    ast_AttributeDefinition,
)
ast_EmptyStatement_strategy = st.builds(
    ast_EmptyStatement,
)
ast_WildcardType_strategy = st.builds(
    ast_WildcardType,
)
ast_RangeExpression_strategy = st.builds(
    ast_RangeExpression,
)
ast_AssertStatement_strategy = st.builds(
    ast_AssertStatement,
)
ast_NamedElement_strategy = st.builds(
    ast_NamedElement,
)
ast_UnaryOp_strategy = st.builds(
    ast_UnaryOp,
)
ast_ThisReference_strategy = st.builds(
    ast_ThisReference,
    name=
        safe_text
)
ast_SuperReference_strategy = st.builds(
    ast_SuperReference,
    name=
        safe_text
)
ast_ShiftOp_strategy = st.builds(
    ast_ShiftOp,
)
ast_ReturnStatement_strategy = st.builds(
    ast_ReturnStatement,
)
ast_PrimitiveType_strategy = st.builds(
    ast_PrimitiveType,
    name=
        safe_text
)
ast_NewOp_strategy = st.builds(
    ast_NewOp,
)
ast_MultiplyOp_strategy = st.builds(
    ast_MultiplyOp,
)
ast_MinusOp_strategy = st.builds(
    ast_MinusOp,
)
ast_Literal_strategy = st.builds(
    ast_Literal,
    value=
        safe_text
)
ast_PlusOp_strategy = st.builds(
    ast_PlusOp,
)
ast_IdentityOp_strategy = st.builds(
    ast_IdentityOp,
)
ast_DivisionOp_strategy = st.builds(
    ast_DivisionOp,
)
DivisionOp_strategy = st.builds(
    DivisionOp,
)
ast_RemainderOp_strategy = st.builds(
    ast_RemainderOp,
)
ast_DivideOp_strategy = st.builds(
    ast_DivideOp,
)
ast_ConditionalOp_strategy = st.builds(
    ast_ConditionalOp,
)
ShiftOp_strategy = st.builds(
    ShiftOp,
)
ast_RightShiftOp_strategy = st.builds(
    ast_RightShiftOp,
)
ast_ZeroExtensionRightShiftOp_strategy = st.builds(
    ast_ZeroExtensionRightShiftOp,
)
ast_LeftShiftOp_strategy = st.builds(
    ast_LeftShiftOp,
)
ClassifierOp_strategy = st.builds(
    ClassifierOp,
)
ast_InstanceOfOp_strategy = st.builds(
    ast_InstanceOfOp,
)
ast_CastOp_strategy = st.builds(
    ast_CastOp,
)
Literal_strategy = st.builds(
    Literal,
)
ast_DoubleLiteral_strategy = st.builds(
    ast_DoubleLiteral,
)
ast_LongIntegerLiteral_strategy = st.builds(
    ast_LongIntegerLiteral,
)
ast_NullReference_strategy = st.builds(
    ast_NullReference,
)
ast_FloatLiteral_strategy = st.builds(
    ast_FloatLiteral,
)
ast_IntegerLiteral_strategy = st.builds(
    ast_IntegerLiteral,
)
ast_StringLiteral_strategy = st.builds(
    ast_StringLiteral,
)
ast_BooleanLiteral_strategy = st.builds(
    ast_BooleanLiteral,
)
UnaryOp_strategy = st.builds(
    UnaryOp,
)
ast_PostfixDecrementOp_strategy = st.builds(
    ast_PostfixDecrementOp,
)
ast_PostfixIncrementOp_strategy = st.builds(
    ast_PostfixIncrementOp,
)
ast_LogicalComplementOp_strategy = st.builds(
    ast_LogicalComplementOp,
)
ast_PrefixIncrementOp_strategy = st.builds(
    ast_PrefixIncrementOp,
)
ast_UnaryPlusOp_strategy = st.builds(
    ast_UnaryPlusOp,
)
ast_UnaryMinusOp_strategy = st.builds(
    ast_UnaryMinusOp,
)
ast_PrefixDecrementOp_strategy = st.builds(
    ast_PrefixDecrementOp,
)
ast_BitwiseComplementOp_strategy = st.builds(
    ast_BitwiseComplementOp,
)
BinaryOp_strategy = st.builds(
    BinaryOp,
)
ast_LessThenOp_strategy = st.builds(
    ast_LessThenOp,
)
ast_GreaterOrEqualOp_strategy = st.builds(
    ast_GreaterOrEqualOp,
)
ast_BitwiseXorOp_strategy = st.builds(
    ast_BitwiseXorOp,
)
ast_LessOrEqualOp_strategy = st.builds(
    ast_LessOrEqualOp,
)
ast_ConditionalOrOp_strategy = st.builds(
    ast_ConditionalOrOp,
)
ast_NotEqualOp_strategy = st.builds(
    ast_NotEqualOp,
)
ast_BitwiseOrOp_strategy = st.builds(
    ast_BitwiseOrOp,
)
ast_EqualOp_strategy = st.builds(
    ast_EqualOp,
)
ast_GreaterThenOp_strategy = st.builds(
    ast_GreaterThenOp,
)
ast_BitwiseAndOp_strategy = st.builds(
    ast_BitwiseAndOp,
)
ast_BinaryOp_strategy = st.builds(
    ast_BinaryOp,
)
ast_AssignmentOperation_strategy = st.builds(
    ast_AssignmentOperation,
)
AssignmentOperation_strategy = st.builds(
    AssignmentOperation,
)
ast_ZeroExtensionRightShiftAssignmentOp_strategy = st.builds(
    ast_ZeroExtensionRightShiftAssignmentOp,
)
ast_MinusAssignmentOp_strategy = st.builds(
    ast_MinusAssignmentOp,
)
ast_BitwiseXorAssignmentOp_strategy = st.builds(
    ast_BitwiseXorAssignmentOp,
)
ast_RemainderAssignmentOp_strategy = st.builds(
    ast_RemainderAssignmentOp,
)
ast_MultiplyAssignmentOp_strategy = st.builds(
    ast_MultiplyAssignmentOp,
)
ast_PlusAssignmentOp_strategy = st.builds(
    ast_PlusAssignmentOp,
)
ast_BitwiseAndAssignmentOp_strategy = st.builds(
    ast_BitwiseAndAssignmentOp,
)
ast_BitwiseOrAssignmentOp_strategy = st.builds(
    ast_BitwiseOrAssignmentOp,
)
ast_LeftShiftAssignmentOp_strategy = st.builds(
    ast_LeftShiftAssignmentOp,
)
ast_DivideAssignmentOp_strategy = st.builds(
    ast_DivideAssignmentOp,
)
ast_RightShiftAssignmentOp_strategy = st.builds(
    ast_RightShiftAssignmentOp,
)
ast_AssignmentOp_strategy = st.builds(
    ast_AssignmentOp,
)
ast_ArrayConstructor_strategy = st.builds(
    ast_ArrayConstructor,
)
ast_ConditionalAndOp_strategy = st.builds(
    ast_ConditionalAndOp,
)
ast_ClassifierOp_strategy = st.builds(
    ast_ClassifierOp,
)
ast_CharacterLiteral_strategy = st.builds(
    ast_CharacterLiteral,
)
ast_ApplyRoundOp_strategy = st.builds(
    ast_ApplyRoundOp,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ast_AccessOp_strategy)
@settings(max_examples=50)
def test_ast_accessop_instantiation(instance):
    assert isinstance(instance, ast_AccessOp)

@given(instance=ScopeStatement_strategy)
@settings(max_examples=50)
def test_scopestatement_instantiation(instance):
    assert isinstance(instance, ScopeStatement)

@given(instance=ast_TryStatement_strategy)
@settings(max_examples=50)
def test_ast_trystatement_instantiation(instance):
    assert isinstance(instance, ast_TryStatement)

@given(instance=ast_SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_ast_synchronizedstatement_instantiation(instance):
    assert isinstance(instance, ast_SynchronizedStatement)

@given(instance=ast_ApplySquareOp_strategy)
@settings(max_examples=50)
def test_ast_applysquareop_instantiation(instance):
    assert isinstance(instance, ast_ApplySquareOp)

@given(instance=LabeledStatement_strategy)
@settings(max_examples=50)
def test_labeledstatement_instantiation(instance):
    assert isinstance(instance, LabeledStatement)

@given(instance=ast_SwitchStatement_strategy)
@settings(max_examples=50)
def test_ast_switchstatement_instantiation(instance):
    assert isinstance(instance, ast_SwitchStatement)

@given(instance=ast_LoopStatement_strategy)
@settings(max_examples=50)
def test_ast_loopstatement_instantiation(instance):
    assert isinstance(instance, ast_LoopStatement)

@given(instance=SwitchPart_strategy)
@settings(max_examples=50)
def test_switchpart_instantiation(instance):
    assert isinstance(instance, SwitchPart)

@given(instance=ast_SwitchDefaultPart_strategy)
@settings(max_examples=50)
def test_ast_switchdefaultpart_instantiation(instance):
    assert isinstance(instance, ast_SwitchDefaultPart)

@given(instance=ast_SwitchCasePart_strategy)
@settings(max_examples=50)
def test_ast_switchcasepart_instantiation(instance):
    assert isinstance(instance, ast_SwitchCasePart)

@given(instance=MethodContentStatement_strategy)
@settings(max_examples=50)
def test_methodcontentstatement_instantiation(instance):
    assert isinstance(instance, MethodContentStatement)

@given(instance=ast_MethodClassifier_strategy)
@settings(max_examples=50)
def test_ast_methodclassifier_instantiation(instance):
    assert isinstance(instance, ast_MethodClassifier)

@given(instance=ast_ThrowStatement_strategy)
@settings(max_examples=50)
def test_ast_throwstatement_instantiation(instance):
    assert isinstance(instance, ast_ThrowStatement)

@given(instance=ast_LabeledStatement_strategy)
@settings(max_examples=50)
def test_ast_labeledstatement_instantiation(instance):
    assert isinstance(instance, ast_LabeledStatement)

@given(instance=ast_IfStatement_strategy)
@settings(max_examples=50)
def test_ast_ifstatement_instantiation(instance):
    assert isinstance(instance, ast_IfStatement)

@given(instance=ast_LocalVarStatement_strategy)
@settings(max_examples=50)
def test_ast_localvarstatement_instantiation(instance):
    assert isinstance(instance, ast_LocalVarStatement)

@given(instance=ast_JumpStatement_strategy)
@settings(max_examples=50)
def test_ast_jumpstatement_instantiation(instance):
    assert isinstance(instance, ast_JumpStatement)

@given(instance=ast_ScopeStatement_strategy)
@settings(max_examples=50)
def test_ast_scopestatement_instantiation(instance):
    assert isinstance(instance, ast_ScopeStatement)

@given(instance=ast_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_ast_expressionstatement_instantiation(instance):
    assert isinstance(instance, ast_ExpressionStatement)

@given(instance=ConditionalLoop_strategy)
@settings(max_examples=50)
def test_conditionalloop_instantiation(instance):
    assert isinstance(instance, ConditionalLoop)

@given(instance=ast_WhileStatement_strategy)
@settings(max_examples=50)
def test_ast_whilestatement_instantiation(instance):
    assert isinstance(instance, ast_WhileStatement)

@given(instance=ast_ForStatement_strategy)
@settings(max_examples=50)
def test_ast_forstatement_instantiation(instance):
    assert isinstance(instance, ast_ForStatement)

@given(instance=ast_DoWhileStatement_strategy)
@settings(max_examples=50)
def test_ast_dowhilestatement_instantiation(instance):
    assert isinstance(instance, ast_DoWhileStatement)

@given(instance=TopLevelStatement_strategy)
@settings(max_examples=50)
def test_toplevelstatement_instantiation(instance):
    assert isinstance(instance, TopLevelStatement)

@given(instance=ast_TopLevelClassifier_strategy)
@settings(max_examples=50)
def test_ast_toplevelclassifier_instantiation(instance):
    assert isinstance(instance, ast_TopLevelClassifier)

@given(instance=ast_PackageStatement_strategy)
@settings(max_examples=50)
def test_ast_packagestatement_instantiation(instance):
    assert isinstance(instance, ast_PackageStatement)

@given(instance=ast_ImportStatement_strategy)
@settings(max_examples=50)
def test_ast_importstatement_instantiation(instance):
    assert isinstance(instance, ast_ImportStatement)

@given(instance=ClassifierStatement_strategy)
@settings(max_examples=50)
def test_classifierstatement_instantiation(instance):
    assert isinstance(instance, ClassifierStatement)

@given(instance=ast_InterfaceStatement_strategy)
@settings(max_examples=50)
def test_ast_interfacestatement_instantiation(instance):
    assert isinstance(instance, ast_InterfaceStatement)

@given(instance=ast_ImplemenationClassifierStatement_strategy)
@settings(max_examples=50)
def test_ast_implemenationclassifierstatement_instantiation(instance):
    assert isinstance(instance, ast_ImplemenationClassifierStatement)

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=ast_ForeachStatement_strategy)
@settings(max_examples=50)
def test_ast_foreachstatement_instantiation(instance):
    assert isinstance(instance, ast_ForeachStatement)

@given(instance=ast_ConditionalLoop_strategy)
@settings(max_examples=50)
def test_ast_conditionalloop_instantiation(instance):
    assert isinstance(instance, ast_ConditionalLoop)

@given(instance=JumpStatement_strategy)
@settings(max_examples=50)
def test_jumpstatement_instantiation(instance):
    assert isinstance(instance, JumpStatement)

@given(instance=ast_ContinueStatement_strategy)
@settings(max_examples=50)
def test_ast_continuestatement_instantiation(instance):
    assert isinstance(instance, ast_ContinueStatement)

@given(instance=ast_BreakStatement_strategy)
@settings(max_examples=50)
def test_ast_breakstatement_instantiation(instance):
    assert isinstance(instance, ast_BreakStatement)

@given(instance=InitStatement_strategy)
@settings(max_examples=50)
def test_initstatement_instantiation(instance):
    assert isinstance(instance, InitStatement)

@given(instance=ast_StaticInitStatement_strategy)
@settings(max_examples=50)
def test_ast_staticinitstatement_instantiation(instance):
    assert isinstance(instance, ast_StaticInitStatement)

@given(instance=ast_InstanceInitStatement_strategy)
@settings(max_examples=50)
def test_ast_instanceinitstatement_instantiation(instance):
    assert isinstance(instance, ast_InstanceInitStatement)

@given(instance=ImplemenationClassifierStatement_strategy)
@settings(max_examples=50)
def test_implemenationclassifierstatement_instantiation(instance):
    assert isinstance(instance, ImplemenationClassifierStatement)

@given(instance=ast_EnumStatement_strategy)
@settings(max_examples=50)
def test_ast_enumstatement_instantiation(instance):
    assert isinstance(instance, ast_EnumStatement)

@given(instance=ast_ClassStatement_strategy)
@settings(max_examples=50)
def test_ast_classstatement_instantiation(instance):
    assert isinstance(instance, ast_ClassStatement)

@given(instance=ClassifierMemberStatement_strategy)
@settings(max_examples=50)
def test_classifiermemberstatement_instantiation(instance):
    assert isinstance(instance, ClassifierMemberStatement)

@given(instance=ast_Feature_strategy)
@settings(max_examples=50)
def test_ast_feature_instantiation(instance):
    assert isinstance(instance, ast_Feature)

@given(instance=ast_InitStatement_strategy)
@settings(max_examples=50)
def test_ast_initstatement_instantiation(instance):
    assert isinstance(instance, ast_InitStatement)

@given(instance=ast_InnerClassifier_strategy)
@settings(max_examples=50)
def test_ast_innerclassifier_instantiation(instance):
    assert isinstance(instance, ast_InnerClassifier)

@given(instance=ast_EnumLiteral_strategy)
@settings(max_examples=50)
def test_ast_enumliteral_instantiation(instance):
    assert isinstance(instance, ast_EnumLiteral)

@given(instance=ast_MethodBlock_strategy)
@settings(max_examples=50)
def test_ast_methodblock_instantiation(instance):
    assert isinstance(instance, ast_MethodBlock)

@given(instance=BehaviorFeature_strategy)
@settings(max_examples=50)
def test_behaviorfeature_instantiation(instance):
    assert isinstance(instance, BehaviorFeature)

@given(instance=ast_MethodStatement_strategy)
@settings(max_examples=50)
def test_ast_methodstatement_instantiation(instance):
    assert isinstance(instance, ast_MethodStatement)

@given(instance=ast_ConstructorStatement_strategy)
@settings(max_examples=50)
def test_ast_constructorstatement_instantiation(instance):
    assert isinstance(instance, ast_ConstructorStatement)

@given(instance=EJBase_strategy)
@settings(max_examples=50)
def test_ejbase_instantiation(instance):
    assert isinstance(instance, EJBase)

@given(instance=ast_CatchPart_strategy)
@settings(max_examples=50)
def test_ast_catchpart_instantiation(instance):
    assert isinstance(instance, ast_CatchPart)

@given(instance=ast_ClassifierMemberStatement_strategy)
@settings(max_examples=50)
def test_ast_classifiermemberstatement_instantiation(instance):
    assert isinstance(instance, ast_ClassifierMemberStatement)

@given(instance=ast_MethodContentStatement_strategy)
@settings(max_examples=50)
def test_ast_methodcontentstatement_instantiation(instance):
    assert isinstance(instance, ast_MethodContentStatement)

@given(instance=ast_ClassifierStatement_strategy)
@settings(max_examples=50)
def test_ast_classifierstatement_instantiation(instance):
    assert isinstance(instance, ast_ClassifierStatement)

@given(instance=ast_SwitchPart_strategy)
@settings(max_examples=50)
def test_ast_switchpart_instantiation(instance):
    assert isinstance(instance, ast_SwitchPart)

@given(instance=ast_TopLevelStatement_strategy)
@settings(max_examples=50)
def test_ast_toplevelstatement_instantiation(instance):
    assert isinstance(instance, ast_TopLevelStatement)

@given(instance=ast_IfThenPart_strategy)
@settings(max_examples=50)
def test_ast_ifthenpart_instantiation(instance):
    assert isinstance(instance, ast_IfThenPart)

@given(instance=ast_ClassBlock_strategy)
@settings(max_examples=50)
def test_ast_classblock_instantiation(instance):
    assert isinstance(instance, ast_ClassBlock)

@given(instance=ast_Identifier_strategy)
@settings(max_examples=50)
def test_ast_identifier_instantiation(instance):
    assert isinstance(instance, ast_Identifier)



@given(instance=ast_Identifier_strategy)
def test_ast_identifier_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=ast_Identifier_strategy)
def test_ast_identifier_quotedValue_setter(instance):
    original = instance.quotedValue
    instance.quotedValue = original
    assert instance.quotedValue == original



@given(instance=ast_Identifier_strategy)
def test_ast_identifier_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=ast_BehaviorFeature_strategy)
@settings(max_examples=50)
def test_ast_behaviorfeature_instantiation(instance):
    assert isinstance(instance, ast_BehaviorFeature)

@given(instance=ast_FieldStatement_strategy)
@settings(max_examples=50)
def test_ast_fieldstatement_instantiation(instance):
    assert isinstance(instance, ast_FieldStatement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ast_TemplateParameter_strategy)
@settings(max_examples=50)
def test_ast_templateparameter_instantiation(instance):
    assert isinstance(instance, ast_TemplateParameter)

@given(instance=ast_Variable_strategy)
@settings(max_examples=50)
def test_ast_variable_instantiation(instance):
    assert isinstance(instance, ast_Variable)

@given(instance=ast_Parameter_strategy)
@settings(max_examples=50)
def test_ast_parameter_instantiation(instance):
    assert isinstance(instance, ast_Parameter)

@given(instance=ast_Expression_strategy)
@settings(max_examples=50)
def test_ast_expression_instantiation(instance):
    assert isinstance(instance, ast_Expression)

@given(instance=EJElement_strategy)
@settings(max_examples=50)
def test_ejelement_instantiation(instance):
    assert isinstance(instance, EJElement)

@given(instance=ast_SwitchDefaultPartRef_strategy)
@settings(max_examples=50)
def test_ast_switchdefaultpartref_instantiation(instance):
    assert isinstance(instance, ast_SwitchDefaultPartRef)

@given(instance=ast_AttributeSet_strategy)
@settings(max_examples=50)
def test_ast_attributeset_instantiation(instance):
    assert isinstance(instance, ast_AttributeSet)

@given(instance=ast_Modifier_strategy)
@settings(max_examples=50)
def test_ast_modifier_instantiation(instance):
    assert isinstance(instance, ast_Modifier)



@given(instance=ast_Modifier_strategy)
def test_ast_modifier_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ast_Label_strategy)
@settings(max_examples=50)
def test_ast_label_instantiation(instance):
    assert isinstance(instance, ast_Label)



@given(instance=ast_Label_strategy)
def test_ast_label_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast_DocumentationLine_strategy)
@settings(max_examples=50)
def test_ast_documentationline_instantiation(instance):
    assert isinstance(instance, ast_DocumentationLine)



@given(instance=ast_DocumentationLine_strategy)
def test_ast_documentationline_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=ast_EJBase_strategy)
@settings(max_examples=50)
def test_ast_ejbase_instantiation(instance):
    assert isinstance(instance, ast_EJBase)

@given(instance=ast_EJElement_strategy)
@settings(max_examples=50)
def test_ast_ejelement_instantiation(instance):
    assert isinstance(instance, ast_EJElement)



@given(instance=ast_EJElement_strategy)
def test_ast_ejelement_startLine_setter(instance):
    original = instance.startLine
    instance.startLine = original
    assert instance.startLine == original



@given(instance=ast_EJElement_strategy)
def test_ast_ejelement_endLine_setter(instance):
    original = instance.endLine
    instance.endLine = original
    assert instance.endLine == original



@given(instance=ast_EJElement_strategy)
def test_ast_ejelement_startOffset_setter(instance):
    original = instance.startOffset
    instance.startOffset = original
    assert instance.startOffset == original



@given(instance=ast_EJElement_strategy)
def test_ast_ejelement_endColumn_setter(instance):
    original = instance.endColumn
    instance.endColumn = original
    assert instance.endColumn == original



@given(instance=ast_EJElement_strategy)
def test_ast_ejelement_startColumn_setter(instance):
    original = instance.startColumn
    instance.startColumn = original
    assert instance.startColumn == original



@given(instance=ast_EJElement_strategy)
def test_ast_ejelement_endOffset_setter(instance):
    original = instance.endOffset
    instance.endOffset = original
    assert instance.endOffset == original

@given(instance=ast_AttributeDefinition_strategy)
@settings(max_examples=50)
def test_ast_attributedefinition_instantiation(instance):
    assert isinstance(instance, ast_AttributeDefinition)

@given(instance=ast_EmptyStatement_strategy)
@settings(max_examples=50)
def test_ast_emptystatement_instantiation(instance):
    assert isinstance(instance, ast_EmptyStatement)

@given(instance=ast_WildcardType_strategy)
@settings(max_examples=50)
def test_ast_wildcardtype_instantiation(instance):
    assert isinstance(instance, ast_WildcardType)

@given(instance=ast_RangeExpression_strategy)
@settings(max_examples=50)
def test_ast_rangeexpression_instantiation(instance):
    assert isinstance(instance, ast_RangeExpression)

@given(instance=ast_AssertStatement_strategy)
@settings(max_examples=50)
def test_ast_assertstatement_instantiation(instance):
    assert isinstance(instance, ast_AssertStatement)

@given(instance=ast_NamedElement_strategy)
@settings(max_examples=50)
def test_ast_namedelement_instantiation(instance):
    assert isinstance(instance, ast_NamedElement)

@given(instance=ast_UnaryOp_strategy)
@settings(max_examples=50)
def test_ast_unaryop_instantiation(instance):
    assert isinstance(instance, ast_UnaryOp)

@given(instance=ast_ThisReference_strategy)
@settings(max_examples=50)
def test_ast_thisreference_instantiation(instance):
    assert isinstance(instance, ast_ThisReference)



@given(instance=ast_ThisReference_strategy)
def test_ast_thisreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast_SuperReference_strategy)
@settings(max_examples=50)
def test_ast_superreference_instantiation(instance):
    assert isinstance(instance, ast_SuperReference)



@given(instance=ast_SuperReference_strategy)
def test_ast_superreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast_ShiftOp_strategy)
@settings(max_examples=50)
def test_ast_shiftop_instantiation(instance):
    assert isinstance(instance, ast_ShiftOp)

@given(instance=ast_ReturnStatement_strategy)
@settings(max_examples=50)
def test_ast_returnstatement_instantiation(instance):
    assert isinstance(instance, ast_ReturnStatement)

@given(instance=ast_PrimitiveType_strategy)
@settings(max_examples=50)
def test_ast_primitivetype_instantiation(instance):
    assert isinstance(instance, ast_PrimitiveType)



@given(instance=ast_PrimitiveType_strategy)
def test_ast_primitivetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ast_NewOp_strategy)
@settings(max_examples=50)
def test_ast_newop_instantiation(instance):
    assert isinstance(instance, ast_NewOp)

@given(instance=ast_MultiplyOp_strategy)
@settings(max_examples=50)
def test_ast_multiplyop_instantiation(instance):
    assert isinstance(instance, ast_MultiplyOp)

@given(instance=ast_MinusOp_strategy)
@settings(max_examples=50)
def test_ast_minusop_instantiation(instance):
    assert isinstance(instance, ast_MinusOp)

@given(instance=ast_Literal_strategy)
@settings(max_examples=50)
def test_ast_literal_instantiation(instance):
    assert isinstance(instance, ast_Literal)



@given(instance=ast_Literal_strategy)
def test_ast_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ast_PlusOp_strategy)
@settings(max_examples=50)
def test_ast_plusop_instantiation(instance):
    assert isinstance(instance, ast_PlusOp)

@given(instance=ast_IdentityOp_strategy)
@settings(max_examples=50)
def test_ast_identityop_instantiation(instance):
    assert isinstance(instance, ast_IdentityOp)

@given(instance=ast_DivisionOp_strategy)
@settings(max_examples=50)
def test_ast_divisionop_instantiation(instance):
    assert isinstance(instance, ast_DivisionOp)

@given(instance=DivisionOp_strategy)
@settings(max_examples=50)
def test_divisionop_instantiation(instance):
    assert isinstance(instance, DivisionOp)

@given(instance=ast_RemainderOp_strategy)
@settings(max_examples=50)
def test_ast_remainderop_instantiation(instance):
    assert isinstance(instance, ast_RemainderOp)

@given(instance=ast_DivideOp_strategy)
@settings(max_examples=50)
def test_ast_divideop_instantiation(instance):
    assert isinstance(instance, ast_DivideOp)

@given(instance=ast_ConditionalOp_strategy)
@settings(max_examples=50)
def test_ast_conditionalop_instantiation(instance):
    assert isinstance(instance, ast_ConditionalOp)

@given(instance=ShiftOp_strategy)
@settings(max_examples=50)
def test_shiftop_instantiation(instance):
    assert isinstance(instance, ShiftOp)

@given(instance=ast_RightShiftOp_strategy)
@settings(max_examples=50)
def test_ast_rightshiftop_instantiation(instance):
    assert isinstance(instance, ast_RightShiftOp)

@given(instance=ast_ZeroExtensionRightShiftOp_strategy)
@settings(max_examples=50)
def test_ast_zeroextensionrightshiftop_instantiation(instance):
    assert isinstance(instance, ast_ZeroExtensionRightShiftOp)

@given(instance=ast_LeftShiftOp_strategy)
@settings(max_examples=50)
def test_ast_leftshiftop_instantiation(instance):
    assert isinstance(instance, ast_LeftShiftOp)

@given(instance=ClassifierOp_strategy)
@settings(max_examples=50)
def test_classifierop_instantiation(instance):
    assert isinstance(instance, ClassifierOp)

@given(instance=ast_InstanceOfOp_strategy)
@settings(max_examples=50)
def test_ast_instanceofop_instantiation(instance):
    assert isinstance(instance, ast_InstanceOfOp)

@given(instance=ast_CastOp_strategy)
@settings(max_examples=50)
def test_ast_castop_instantiation(instance):
    assert isinstance(instance, ast_CastOp)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=ast_DoubleLiteral_strategy)
@settings(max_examples=50)
def test_ast_doubleliteral_instantiation(instance):
    assert isinstance(instance, ast_DoubleLiteral)

@given(instance=ast_LongIntegerLiteral_strategy)
@settings(max_examples=50)
def test_ast_longintegerliteral_instantiation(instance):
    assert isinstance(instance, ast_LongIntegerLiteral)

@given(instance=ast_NullReference_strategy)
@settings(max_examples=50)
def test_ast_nullreference_instantiation(instance):
    assert isinstance(instance, ast_NullReference)

@given(instance=ast_FloatLiteral_strategy)
@settings(max_examples=50)
def test_ast_floatliteral_instantiation(instance):
    assert isinstance(instance, ast_FloatLiteral)

@given(instance=ast_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_ast_integerliteral_instantiation(instance):
    assert isinstance(instance, ast_IntegerLiteral)

@given(instance=ast_StringLiteral_strategy)
@settings(max_examples=50)
def test_ast_stringliteral_instantiation(instance):
    assert isinstance(instance, ast_StringLiteral)

@given(instance=ast_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_ast_booleanliteral_instantiation(instance):
    assert isinstance(instance, ast_BooleanLiteral)

@given(instance=UnaryOp_strategy)
@settings(max_examples=50)
def test_unaryop_instantiation(instance):
    assert isinstance(instance, UnaryOp)

@given(instance=ast_PostfixDecrementOp_strategy)
@settings(max_examples=50)
def test_ast_postfixdecrementop_instantiation(instance):
    assert isinstance(instance, ast_PostfixDecrementOp)

@given(instance=ast_PostfixIncrementOp_strategy)
@settings(max_examples=50)
def test_ast_postfixincrementop_instantiation(instance):
    assert isinstance(instance, ast_PostfixIncrementOp)

@given(instance=ast_LogicalComplementOp_strategy)
@settings(max_examples=50)
def test_ast_logicalcomplementop_instantiation(instance):
    assert isinstance(instance, ast_LogicalComplementOp)

@given(instance=ast_PrefixIncrementOp_strategy)
@settings(max_examples=50)
def test_ast_prefixincrementop_instantiation(instance):
    assert isinstance(instance, ast_PrefixIncrementOp)

@given(instance=ast_UnaryPlusOp_strategy)
@settings(max_examples=50)
def test_ast_unaryplusop_instantiation(instance):
    assert isinstance(instance, ast_UnaryPlusOp)

@given(instance=ast_UnaryMinusOp_strategy)
@settings(max_examples=50)
def test_ast_unaryminusop_instantiation(instance):
    assert isinstance(instance, ast_UnaryMinusOp)

@given(instance=ast_PrefixDecrementOp_strategy)
@settings(max_examples=50)
def test_ast_prefixdecrementop_instantiation(instance):
    assert isinstance(instance, ast_PrefixDecrementOp)

@given(instance=ast_BitwiseComplementOp_strategy)
@settings(max_examples=50)
def test_ast_bitwisecomplementop_instantiation(instance):
    assert isinstance(instance, ast_BitwiseComplementOp)

@given(instance=BinaryOp_strategy)
@settings(max_examples=50)
def test_binaryop_instantiation(instance):
    assert isinstance(instance, BinaryOp)

@given(instance=ast_LessThenOp_strategy)
@settings(max_examples=50)
def test_ast_lessthenop_instantiation(instance):
    assert isinstance(instance, ast_LessThenOp)

@given(instance=ast_GreaterOrEqualOp_strategy)
@settings(max_examples=50)
def test_ast_greaterorequalop_instantiation(instance):
    assert isinstance(instance, ast_GreaterOrEqualOp)

@given(instance=ast_BitwiseXorOp_strategy)
@settings(max_examples=50)
def test_ast_bitwisexorop_instantiation(instance):
    assert isinstance(instance, ast_BitwiseXorOp)

@given(instance=ast_LessOrEqualOp_strategy)
@settings(max_examples=50)
def test_ast_lessorequalop_instantiation(instance):
    assert isinstance(instance, ast_LessOrEqualOp)

@given(instance=ast_ConditionalOrOp_strategy)
@settings(max_examples=50)
def test_ast_conditionalorop_instantiation(instance):
    assert isinstance(instance, ast_ConditionalOrOp)

@given(instance=ast_NotEqualOp_strategy)
@settings(max_examples=50)
def test_ast_notequalop_instantiation(instance):
    assert isinstance(instance, ast_NotEqualOp)

@given(instance=ast_BitwiseOrOp_strategy)
@settings(max_examples=50)
def test_ast_bitwiseorop_instantiation(instance):
    assert isinstance(instance, ast_BitwiseOrOp)

@given(instance=ast_EqualOp_strategy)
@settings(max_examples=50)
def test_ast_equalop_instantiation(instance):
    assert isinstance(instance, ast_EqualOp)

@given(instance=ast_GreaterThenOp_strategy)
@settings(max_examples=50)
def test_ast_greaterthenop_instantiation(instance):
    assert isinstance(instance, ast_GreaterThenOp)

@given(instance=ast_BitwiseAndOp_strategy)
@settings(max_examples=50)
def test_ast_bitwiseandop_instantiation(instance):
    assert isinstance(instance, ast_BitwiseAndOp)

@given(instance=ast_BinaryOp_strategy)
@settings(max_examples=50)
def test_ast_binaryop_instantiation(instance):
    assert isinstance(instance, ast_BinaryOp)

@given(instance=ast_AssignmentOperation_strategy)
@settings(max_examples=50)
def test_ast_assignmentoperation_instantiation(instance):
    assert isinstance(instance, ast_AssignmentOperation)

@given(instance=AssignmentOperation_strategy)
@settings(max_examples=50)
def test_assignmentoperation_instantiation(instance):
    assert isinstance(instance, AssignmentOperation)

@given(instance=ast_ZeroExtensionRightShiftAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast_zeroextensionrightshiftassignmentop_instantiation(instance):
    assert isinstance(instance, ast_ZeroExtensionRightShiftAssignmentOp)

@given(instance=ast_MinusAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast_minusassignmentop_instantiation(instance):
    assert isinstance(instance, ast_MinusAssignmentOp)

@given(instance=ast_BitwiseXorAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast_bitwisexorassignmentop_instantiation(instance):
    assert isinstance(instance, ast_BitwiseXorAssignmentOp)

@given(instance=ast_RemainderAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast_remainderassignmentop_instantiation(instance):
    assert isinstance(instance, ast_RemainderAssignmentOp)

@given(instance=ast_MultiplyAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast_multiplyassignmentop_instantiation(instance):
    assert isinstance(instance, ast_MultiplyAssignmentOp)

@given(instance=ast_PlusAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast_plusassignmentop_instantiation(instance):
    assert isinstance(instance, ast_PlusAssignmentOp)

@given(instance=ast_BitwiseAndAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast_bitwiseandassignmentop_instantiation(instance):
    assert isinstance(instance, ast_BitwiseAndAssignmentOp)

@given(instance=ast_BitwiseOrAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast_bitwiseorassignmentop_instantiation(instance):
    assert isinstance(instance, ast_BitwiseOrAssignmentOp)

@given(instance=ast_LeftShiftAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast_leftshiftassignmentop_instantiation(instance):
    assert isinstance(instance, ast_LeftShiftAssignmentOp)

@given(instance=ast_DivideAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast_divideassignmentop_instantiation(instance):
    assert isinstance(instance, ast_DivideAssignmentOp)

@given(instance=ast_RightShiftAssignmentOp_strategy)
@settings(max_examples=50)
def test_ast_rightshiftassignmentop_instantiation(instance):
    assert isinstance(instance, ast_RightShiftAssignmentOp)

@given(instance=ast_AssignmentOp_strategy)
@settings(max_examples=50)
def test_ast_assignmentop_instantiation(instance):
    assert isinstance(instance, ast_AssignmentOp)

@given(instance=ast_ArrayConstructor_strategy)
@settings(max_examples=50)
def test_ast_arrayconstructor_instantiation(instance):
    assert isinstance(instance, ast_ArrayConstructor)

@given(instance=ast_ConditionalAndOp_strategy)
@settings(max_examples=50)
def test_ast_conditionalandop_instantiation(instance):
    assert isinstance(instance, ast_ConditionalAndOp)

@given(instance=ast_ClassifierOp_strategy)
@settings(max_examples=50)
def test_ast_classifierop_instantiation(instance):
    assert isinstance(instance, ast_ClassifierOp)

@given(instance=ast_CharacterLiteral_strategy)
@settings(max_examples=50)
def test_ast_characterliteral_instantiation(instance):
    assert isinstance(instance, ast_CharacterLiteral)

@given(instance=ast_ApplyRoundOp_strategy)
@settings(max_examples=50)
def test_ast_applyroundop_instantiation(instance):
    assert isinstance(instance, ast_ApplyRoundOp)
