import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RenameCS,
    ClassifierPropertyCS,
    ScopedNameCS,
    DictLiteralPartCS,
    CollectionLiteralPartCS,
    LiteralExpCS,
    qvtoperational_cst_DictLiteralExpCS,
    qvtoperational_cst_ListLiteralExpCS,
    ModuleRefCS,
    ModuleKindCS,
    LogExpCS,
    TransformationRefineCS,
    ModuleUsageCS,
    PackageRefCS,
    ResolveExpCS,
    qvtoperational_cst_ResolveInExpCS,
    CallExpCS,
    qvtoperational_cst_ResolveExpCS,
    qvtoperational_cst_ElementWithBody,
    OperationCallExpCS,
    qvtoperational_cst_LogExpCS,
    qvtoperational_cst_ImperativeOperationCallExpCS,
    ImperativeOperationCallExpCS,
    qvtoperational_cst_MappingCallExpCS,
    cst_InstantiationExpCS,
    SwitchAltExpCS,
    ImperativeLoopExpCS,
    qvtoperational_cst_ImperativeIterateExpCS,
    qvtoperational_cst_ForExpCS,
    cst_StatementCS,
    cst_LoopExpCS,
    qvtoperational_cst_ImperativeLoopExpCS,
    VariableCS,
    StatementCS,
    qvtoperational_cst_WhileExpCS,
    qvtoperational_cst_AssignStatementCS,
    qvtoperational_cst_ExpressionStatementCS,
    qvtoperational_cst_AssertExpCS,
    qvtoperational_cst_ContinueExpCS,
    qvtoperational_cst_VariableInitializationCS,
    qvtoperational_cst_SwitchAltExpCS,
    qvtoperational_cst_SwitchExpCS,
    qvtoperational_cst_ReturnExpCS,
    qvtoperational_cst_ComputeExpCS,
    qvtoperational_cst_BreakExpCS,
    qvtoperational_cst_InstantiationExpCS,
    qvtoperational_cst_BlockExpCS,
    MappingEndCS,
    MappingBodyCS,
    MappingInitCS,
    MappingSectionCS,
    qvtoperational_cst_MappingEndCS,
    qvtoperational_cst_MappingBodyCS,
    qvtoperational_cst_MappingInitCS,
    MappingRuleCS,
    cst_ElementWithBody,
    qvtoperational_cst_ObjectExpCS,
    cst_CSTNode,
    qvtoperational_cst_ModelTypeCS,
    qvtoperational_cst_MappingSectionCS,
    MappingSectionsCS,
    MappingDeclarationCS,
    SimpleSignatureCS,
    TypeSpecCS,
    MappingExtensionCS,
    DirectionKindCS,
    ParameterDeclarationCS,
    PrimitiveLiteralExpCS,
    OppositePropertyCS,
    MultiplicityDefCS,
    LocalPropertyCS,
    qvtoperational_cst_ClassifierPropertyCS,
    OCLExpressionCS,
    qvtoperational_cst_StatementCS,
    StringLiteralExpCS,
    SimpleNameCS,
    TypeCS,
    qvtoperational_cst_ListTypeCS,
    qvtoperational_cst_DictionaryTypeCS,
    PathNameCS,
    MappingModuleCS,
    qvtoperational_cst_LibraryCS,
    TagCS,
    ClassifierDefCS,
    MappingMethodCS,
    qvtoperational_cst_MappingRuleCS,
    qvtoperational_cst_MappingQueryCS,
    qvtoperational_cst_ConstructorCS,
    ModulePropertyCS,
    qvtoperational_cst_LocalPropertyCS,
    qvtoperational_cst_ConfigPropertyCS,
    qvtoperational_cst_ContextualPropertyCS,
    ModelTypeCS,
    ImportCS,
    qvtoperational_cst_LibraryImportCS,
    TransformationHeaderCS,
    CSTNode,
    qvtoperational_cst_MultiplicityDefCS,
    qvtoperational_cst_MappingMethodCS,
    qvtoperational_cst_CompleteSignatureCS,
    qvtoperational_cst_ModulePropertyCS,
    qvtoperational_cst_SimpleSignatureCS,
    qvtoperational_cst_RenameCS,
    qvtoperational_cst_MappingDeclarationCS,
    qvtoperational_cst_TransformationHeaderCS,
    qvtoperational_cst_MappingExtensionCS,
    qvtoperational_cst_ClassifierDefCS,
    qvtoperational_cst_TransformationRefineCS,
    qvtoperational_cst_TypeSpecCS,
    qvtoperational_cst_ModuleKindCS,
    qvtoperational_cst_ResolveOpArgsExpCS,
    qvtoperational_cst_TagCS,
    qvtoperational_cst_UnitCS,
    qvtoperational_cst_MappingSectionsCS,
    qvtoperational_cst_ParameterDeclarationCS,
    qvtoperational_cst_ImportCS,
    qvtoperational_cst_ModuleRefCS,
    qvtoperational_cst_OppositePropertyCS,
    qvtoperational_cst_ModuleUsageCS,
    qvtoperational_cst_PackageRefCS,
    qvtoperational_cst_DictLiteralPartCS,
    qvtoperational_cst_DirectionKindCS,
    qvtoperational_cst_ScopedNameCS,
    qvtoperational_cst_MappingModuleCS,
    ModuleKindEnum,
    QualifierKindCS,
    DirectionKindEnum,
    ImportKindEnum,
    MappingExtensionKindCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_renamecs_is_not_abstract():
    assert not inspect.isabstract(RenameCS)


def test_renamecs_constructor_exists():
    assert callable(RenameCS.__init__)


def test_renamecs_constructor_args():
    sig = inspect.signature(RenameCS.__init__)
    params = list(sig.parameters.keys())



def test_classifierpropertycs_is_not_abstract():
    assert not inspect.isabstract(ClassifierPropertyCS)


def test_classifierpropertycs_constructor_exists():
    assert callable(ClassifierPropertyCS.__init__)


def test_classifierpropertycs_constructor_args():
    sig = inspect.signature(ClassifierPropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_scopednamecs_is_not_abstract():
    assert not inspect.isabstract(ScopedNameCS)


def test_scopednamecs_constructor_exists():
    assert callable(ScopedNameCS.__init__)


def test_scopednamecs_constructor_args():
    sig = inspect.signature(ScopedNameCS.__init__)
    params = list(sig.parameters.keys())



def test_dictliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPartCS)


def test_dictliteralpartcs_constructor_exists():
    assert callable(DictLiteralPartCS.__init__)


def test_dictliteralpartcs_constructor_args():
    sig = inspect.signature(DictLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPartCS)


def test_collectionliteralpartcs_constructor_exists():
    assert callable(CollectionLiteralPartCS.__init__)


def test_collectionliteralpartcs_constructor_args():
    sig = inspect.signature(CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_dictliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_DictLiteralExpCS)


def test_qvtoperational_cst_dictliteralexpcs_constructor_exists():
    assert callable(qvtoperational_cst_DictLiteralExpCS.__init__)


def test_qvtoperational_cst_dictliteralexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_DictLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_listliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ListLiteralExpCS)


def test_qvtoperational_cst_listliteralexpcs_constructor_exists():
    assert callable(qvtoperational_cst_ListLiteralExpCS.__init__)


def test_qvtoperational_cst_listliteralexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ListLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_modulerefcs_is_not_abstract():
    assert not inspect.isabstract(ModuleRefCS)


def test_modulerefcs_constructor_exists():
    assert callable(ModuleRefCS.__init__)


def test_modulerefcs_constructor_args():
    sig = inspect.signature(ModuleRefCS.__init__)
    params = list(sig.parameters.keys())



def test_modulekindcs_is_not_abstract():
    assert not inspect.isabstract(ModuleKindCS)


def test_modulekindcs_constructor_exists():
    assert callable(ModuleKindCS.__init__)


def test_modulekindcs_constructor_args():
    sig = inspect.signature(ModuleKindCS.__init__)
    params = list(sig.parameters.keys())



def test_logexpcs_is_not_abstract():
    assert not inspect.isabstract(LogExpCS)


def test_logexpcs_constructor_exists():
    assert callable(LogExpCS.__init__)


def test_logexpcs_constructor_args():
    sig = inspect.signature(LogExpCS.__init__)
    params = list(sig.parameters.keys())



def test_transformationrefinecs_is_not_abstract():
    assert not inspect.isabstract(TransformationRefineCS)


def test_transformationrefinecs_constructor_exists():
    assert callable(TransformationRefineCS.__init__)


def test_transformationrefinecs_constructor_args():
    sig = inspect.signature(TransformationRefineCS.__init__)
    params = list(sig.parameters.keys())



def test_moduleusagecs_is_not_abstract():
    assert not inspect.isabstract(ModuleUsageCS)


def test_moduleusagecs_constructor_exists():
    assert callable(ModuleUsageCS.__init__)


def test_moduleusagecs_constructor_args():
    sig = inspect.signature(ModuleUsageCS.__init__)
    params = list(sig.parameters.keys())



def test_packagerefcs_is_not_abstract():
    assert not inspect.isabstract(PackageRefCS)


def test_packagerefcs_constructor_exists():
    assert callable(PackageRefCS.__init__)


def test_packagerefcs_constructor_args():
    sig = inspect.signature(PackageRefCS.__init__)
    params = list(sig.parameters.keys())



def test_resolveexpcs_is_not_abstract():
    assert not inspect.isabstract(ResolveExpCS)


def test_resolveexpcs_constructor_exists():
    assert callable(ResolveExpCS.__init__)


def test_resolveexpcs_constructor_args():
    sig = inspect.signature(ResolveExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_resolveinexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ResolveInExpCS)


def test_qvtoperational_cst_resolveinexpcs_constructor_exists():
    assert callable(qvtoperational_cst_ResolveInExpCS.__init__)


def test_qvtoperational_cst_resolveinexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ResolveInExpCS.__init__)
    params = list(sig.parameters.keys())



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_resolveexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ResolveExpCS)


def test_qvtoperational_cst_resolveexpcs_constructor_exists():
    assert callable(qvtoperational_cst_ResolveExpCS.__init__)


def test_qvtoperational_cst_resolveexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ResolveExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "isDeferred" in params, "Missing parameter 'isDeferred'"
    assert "isInverse" in params, "Missing parameter 'isInverse'"
    assert "one" in params, "Missing parameter 'one'"

def test_qvtoperational_cst_resolveexpcs_has_isDeferred():
    assert hasattr(qvtoperational_cst_ResolveExpCS, "isDeferred")
    descriptor = None
    for klass in qvtoperational_cst_ResolveExpCS.__mro__:
        if "isDeferred" in klass.__dict__:
            descriptor = klass.__dict__["isDeferred"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational_cst_resolveexpcs_has_isInverse():
    assert hasattr(qvtoperational_cst_ResolveExpCS, "isInverse")
    descriptor = None
    for klass in qvtoperational_cst_ResolveExpCS.__mro__:
        if "isInverse" in klass.__dict__:
            descriptor = klass.__dict__["isInverse"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational_cst_resolveexpcs_has_one():
    assert hasattr(qvtoperational_cst_ResolveExpCS, "one")
    descriptor = None
    for klass in qvtoperational_cst_ResolveExpCS.__mro__:
        if "one" in klass.__dict__:
            descriptor = klass.__dict__["one"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_cst_elementwithbody_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ElementWithBody)


def test_qvtoperational_cst_elementwithbody_constructor_exists():
    assert callable(qvtoperational_cst_ElementWithBody.__init__)


def test_qvtoperational_cst_elementwithbody_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ElementWithBody.__init__)
    params = list(sig.parameters.keys())
    assert "bodyEndLocation" in params, "Missing parameter 'bodyEndLocation'"
    assert "bodyStartLocation" in params, "Missing parameter 'bodyStartLocation'"

def test_qvtoperational_cst_elementwithbody_has_bodyEndLocation():
    assert hasattr(qvtoperational_cst_ElementWithBody, "bodyEndLocation")
    descriptor = None
    for klass in qvtoperational_cst_ElementWithBody.__mro__:
        if "bodyEndLocation" in klass.__dict__:
            descriptor = klass.__dict__["bodyEndLocation"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational_cst_elementwithbody_has_bodyStartLocation():
    assert hasattr(qvtoperational_cst_ElementWithBody, "bodyStartLocation")
    descriptor = None
    for klass in qvtoperational_cst_ElementWithBody.__mro__:
        if "bodyStartLocation" in klass.__dict__:
            descriptor = klass.__dict__["bodyStartLocation"]
            break
    assert isinstance(descriptor, property)



def test_operationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(OperationCallExpCS)


def test_operationcallexpcs_constructor_exists():
    assert callable(OperationCallExpCS.__init__)


def test_operationcallexpcs_constructor_args():
    sig = inspect.signature(OperationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_logexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_LogExpCS)


def test_qvtoperational_cst_logexpcs_constructor_exists():
    assert callable(qvtoperational_cst_LogExpCS.__init__)


def test_qvtoperational_cst_logexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_LogExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_imperativeoperationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ImperativeOperationCallExpCS)


def test_qvtoperational_cst_imperativeoperationcallexpcs_constructor_exists():
    assert callable(qvtoperational_cst_ImperativeOperationCallExpCS.__init__)


def test_qvtoperational_cst_imperativeoperationcallexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ImperativeOperationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoperationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(ImperativeOperationCallExpCS)


def test_imperativeoperationcallexpcs_constructor_exists():
    assert callable(ImperativeOperationCallExpCS.__init__)


def test_imperativeoperationcallexpcs_constructor_args():
    sig = inspect.signature(ImperativeOperationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_mappingcallexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_MappingCallExpCS)


def test_qvtoperational_cst_mappingcallexpcs_constructor_exists():
    assert callable(qvtoperational_cst_MappingCallExpCS.__init__)


def test_qvtoperational_cst_mappingcallexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_MappingCallExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "strict" in params, "Missing parameter 'strict'"

def test_qvtoperational_cst_mappingcallexpcs_has_strict():
    assert hasattr(qvtoperational_cst_MappingCallExpCS, "strict")
    descriptor = None
    for klass in qvtoperational_cst_MappingCallExpCS.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)



def test_cst_instantiationexpcs_is_not_abstract():
    assert not inspect.isabstract(cst_InstantiationExpCS)


def test_cst_instantiationexpcs_constructor_exists():
    assert callable(cst_InstantiationExpCS.__init__)


def test_cst_instantiationexpcs_constructor_args():
    sig = inspect.signature(cst_InstantiationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_switchaltexpcs_is_not_abstract():
    assert not inspect.isabstract(SwitchAltExpCS)


def test_switchaltexpcs_constructor_exists():
    assert callable(SwitchAltExpCS.__init__)


def test_switchaltexpcs_constructor_args():
    sig = inspect.signature(SwitchAltExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeloopexpcs_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExpCS)


def test_imperativeloopexpcs_constructor_exists():
    assert callable(ImperativeLoopExpCS.__init__)


def test_imperativeloopexpcs_constructor_args():
    sig = inspect.signature(ImperativeLoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_imperativeiterateexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ImperativeIterateExpCS)


def test_qvtoperational_cst_imperativeiterateexpcs_constructor_exists():
    assert callable(qvtoperational_cst_ImperativeIterateExpCS.__init__)


def test_qvtoperational_cst_imperativeiterateexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ImperativeIterateExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_forexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ForExpCS)


def test_qvtoperational_cst_forexpcs_constructor_exists():
    assert callable(qvtoperational_cst_ForExpCS.__init__)


def test_qvtoperational_cst_forexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ForExpCS.__init__)
    params = list(sig.parameters.keys())



def test_cst_statementcs_is_not_abstract():
    assert not inspect.isabstract(cst_StatementCS)


def test_cst_statementcs_constructor_exists():
    assert callable(cst_StatementCS.__init__)


def test_cst_statementcs_constructor_args():
    sig = inspect.signature(cst_StatementCS.__init__)
    params = list(sig.parameters.keys())



def test_cst_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(cst_LoopExpCS)


def test_cst_loopexpcs_constructor_exists():
    assert callable(cst_LoopExpCS.__init__)


def test_cst_loopexpcs_constructor_args():
    sig = inspect.signature(cst_LoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_imperativeloopexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ImperativeLoopExpCS)


def test_qvtoperational_cst_imperativeloopexpcs_constructor_exists():
    assert callable(qvtoperational_cst_ImperativeLoopExpCS.__init__)


def test_qvtoperational_cst_imperativeloopexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ImperativeLoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_variablecs_is_not_abstract():
    assert not inspect.isabstract(VariableCS)


def test_variablecs_constructor_exists():
    assert callable(VariableCS.__init__)


def test_variablecs_constructor_args():
    sig = inspect.signature(VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_statementcs_is_not_abstract():
    assert not inspect.isabstract(StatementCS)


def test_statementcs_constructor_exists():
    assert callable(StatementCS.__init__)


def test_statementcs_constructor_args():
    sig = inspect.signature(StatementCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_whileexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_WhileExpCS)


def test_qvtoperational_cst_whileexpcs_constructor_exists():
    assert callable(qvtoperational_cst_WhileExpCS.__init__)


def test_qvtoperational_cst_whileexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_WhileExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_assignstatementcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_AssignStatementCS)


def test_qvtoperational_cst_assignstatementcs_constructor_exists():
    assert callable(qvtoperational_cst_AssignStatementCS.__init__)


def test_qvtoperational_cst_assignstatementcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_AssignStatementCS.__init__)
    params = list(sig.parameters.keys())
    assert "incremental" in params, "Missing parameter 'incremental'"

def test_qvtoperational_cst_assignstatementcs_has_incremental():
    assert hasattr(qvtoperational_cst_AssignStatementCS, "incremental")
    descriptor = None
    for klass in qvtoperational_cst_AssignStatementCS.__mro__:
        if "incremental" in klass.__dict__:
            descriptor = klass.__dict__["incremental"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_cst_expressionstatementcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ExpressionStatementCS)


def test_qvtoperational_cst_expressionstatementcs_constructor_exists():
    assert callable(qvtoperational_cst_ExpressionStatementCS.__init__)


def test_qvtoperational_cst_expressionstatementcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ExpressionStatementCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_assertexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_AssertExpCS)


def test_qvtoperational_cst_assertexpcs_constructor_exists():
    assert callable(qvtoperational_cst_AssertExpCS.__init__)


def test_qvtoperational_cst_assertexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_AssertExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_continueexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ContinueExpCS)


def test_qvtoperational_cst_continueexpcs_constructor_exists():
    assert callable(qvtoperational_cst_ContinueExpCS.__init__)


def test_qvtoperational_cst_continueexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ContinueExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_variableinitializationcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_VariableInitializationCS)


def test_qvtoperational_cst_variableinitializationcs_constructor_exists():
    assert callable(qvtoperational_cst_VariableInitializationCS.__init__)


def test_qvtoperational_cst_variableinitializationcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_VariableInitializationCS.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_qvtoperational_cst_variableinitializationcs_has_withResult():
    assert hasattr(qvtoperational_cst_VariableInitializationCS, "withResult")
    descriptor = None
    for klass in qvtoperational_cst_VariableInitializationCS.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_cst_switchaltexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_SwitchAltExpCS)


def test_qvtoperational_cst_switchaltexpcs_constructor_exists():
    assert callable(qvtoperational_cst_SwitchAltExpCS.__init__)


def test_qvtoperational_cst_switchaltexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_SwitchAltExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_switchexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_SwitchExpCS)


def test_qvtoperational_cst_switchexpcs_constructor_exists():
    assert callable(qvtoperational_cst_SwitchExpCS.__init__)


def test_qvtoperational_cst_switchexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_SwitchExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_returnexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ReturnExpCS)


def test_qvtoperational_cst_returnexpcs_constructor_exists():
    assert callable(qvtoperational_cst_ReturnExpCS.__init__)


def test_qvtoperational_cst_returnexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ReturnExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_computeexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ComputeExpCS)


def test_qvtoperational_cst_computeexpcs_constructor_exists():
    assert callable(qvtoperational_cst_ComputeExpCS.__init__)


def test_qvtoperational_cst_computeexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ComputeExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_breakexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_BreakExpCS)


def test_qvtoperational_cst_breakexpcs_constructor_exists():
    assert callable(qvtoperational_cst_BreakExpCS.__init__)


def test_qvtoperational_cst_breakexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_BreakExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_instantiationexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_InstantiationExpCS)


def test_qvtoperational_cst_instantiationexpcs_constructor_exists():
    assert callable(qvtoperational_cst_InstantiationExpCS.__init__)


def test_qvtoperational_cst_instantiationexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_InstantiationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_blockexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_BlockExpCS)


def test_qvtoperational_cst_blockexpcs_constructor_exists():
    assert callable(qvtoperational_cst_BlockExpCS.__init__)


def test_qvtoperational_cst_blockexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_BlockExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingendcs_is_not_abstract():
    assert not inspect.isabstract(MappingEndCS)


def test_mappingendcs_constructor_exists():
    assert callable(MappingEndCS.__init__)


def test_mappingendcs_constructor_args():
    sig = inspect.signature(MappingEndCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingbodycs_is_not_abstract():
    assert not inspect.isabstract(MappingBodyCS)


def test_mappingbodycs_constructor_exists():
    assert callable(MappingBodyCS.__init__)


def test_mappingbodycs_constructor_args():
    sig = inspect.signature(MappingBodyCS.__init__)
    params = list(sig.parameters.keys())



def test_mappinginitcs_is_not_abstract():
    assert not inspect.isabstract(MappingInitCS)


def test_mappinginitcs_constructor_exists():
    assert callable(MappingInitCS.__init__)


def test_mappinginitcs_constructor_args():
    sig = inspect.signature(MappingInitCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingsectioncs_is_not_abstract():
    assert not inspect.isabstract(MappingSectionCS)


def test_mappingsectioncs_constructor_exists():
    assert callable(MappingSectionCS.__init__)


def test_mappingsectioncs_constructor_args():
    sig = inspect.signature(MappingSectionCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_mappingendcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_MappingEndCS)


def test_qvtoperational_cst_mappingendcs_constructor_exists():
    assert callable(qvtoperational_cst_MappingEndCS.__init__)


def test_qvtoperational_cst_mappingendcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_MappingEndCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_mappingbodycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_MappingBodyCS)


def test_qvtoperational_cst_mappingbodycs_constructor_exists():
    assert callable(qvtoperational_cst_MappingBodyCS.__init__)


def test_qvtoperational_cst_mappingbodycs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_MappingBodyCS.__init__)
    params = list(sig.parameters.keys())
    assert "hasPopulationKeyword" in params, "Missing parameter 'hasPopulationKeyword'"

def test_qvtoperational_cst_mappingbodycs_has_hasPopulationKeyword():
    assert hasattr(qvtoperational_cst_MappingBodyCS, "hasPopulationKeyword")
    descriptor = None
    for klass in qvtoperational_cst_MappingBodyCS.__mro__:
        if "hasPopulationKeyword" in klass.__dict__:
            descriptor = klass.__dict__["hasPopulationKeyword"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_cst_mappinginitcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_MappingInitCS)


def test_qvtoperational_cst_mappinginitcs_constructor_exists():
    assert callable(qvtoperational_cst_MappingInitCS.__init__)


def test_qvtoperational_cst_mappinginitcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_MappingInitCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingrulecs_is_not_abstract():
    assert not inspect.isabstract(MappingRuleCS)


def test_mappingrulecs_constructor_exists():
    assert callable(MappingRuleCS.__init__)


def test_mappingrulecs_constructor_args():
    sig = inspect.signature(MappingRuleCS.__init__)
    params = list(sig.parameters.keys())



def test_cst_elementwithbody_is_not_abstract():
    assert not inspect.isabstract(cst_ElementWithBody)


def test_cst_elementwithbody_constructor_exists():
    assert callable(cst_ElementWithBody.__init__)


def test_cst_elementwithbody_constructor_args():
    sig = inspect.signature(cst_ElementWithBody.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_objectexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ObjectExpCS)


def test_qvtoperational_cst_objectexpcs_constructor_exists():
    assert callable(qvtoperational_cst_ObjectExpCS.__init__)


def test_qvtoperational_cst_objectexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ObjectExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "isImplicit" in params, "Missing parameter 'isImplicit'"

def test_qvtoperational_cst_objectexpcs_has_isImplicit():
    assert hasattr(qvtoperational_cst_ObjectExpCS, "isImplicit")
    descriptor = None
    for klass in qvtoperational_cst_ObjectExpCS.__mro__:
        if "isImplicit" in klass.__dict__:
            descriptor = klass.__dict__["isImplicit"]
            break
    assert isinstance(descriptor, property)



def test_cst_cstnode_is_not_abstract():
    assert not inspect.isabstract(cst_CSTNode)


def test_cst_cstnode_constructor_exists():
    assert callable(cst_CSTNode.__init__)


def test_cst_cstnode_constructor_args():
    sig = inspect.signature(cst_CSTNode.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_modeltypecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ModelTypeCS)


def test_qvtoperational_cst_modeltypecs_constructor_exists():
    assert callable(qvtoperational_cst_ModelTypeCS.__init__)


def test_qvtoperational_cst_modeltypecs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ModelTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_mappingsectioncs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_MappingSectionCS)


def test_qvtoperational_cst_mappingsectioncs_constructor_exists():
    assert callable(qvtoperational_cst_MappingSectionCS.__init__)


def test_qvtoperational_cst_mappingsectioncs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_MappingSectionCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingsectionscs_is_not_abstract():
    assert not inspect.isabstract(MappingSectionsCS)


def test_mappingsectionscs_constructor_exists():
    assert callable(MappingSectionsCS.__init__)


def test_mappingsectionscs_constructor_args():
    sig = inspect.signature(MappingSectionsCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingdeclarationcs_is_not_abstract():
    assert not inspect.isabstract(MappingDeclarationCS)


def test_mappingdeclarationcs_constructor_exists():
    assert callable(MappingDeclarationCS.__init__)


def test_mappingdeclarationcs_constructor_args():
    sig = inspect.signature(MappingDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_simplesignaturecs_is_not_abstract():
    assert not inspect.isabstract(SimpleSignatureCS)


def test_simplesignaturecs_constructor_exists():
    assert callable(SimpleSignatureCS.__init__)


def test_simplesignaturecs_constructor_args():
    sig = inspect.signature(SimpleSignatureCS.__init__)
    params = list(sig.parameters.keys())



def test_typespeccs_is_not_abstract():
    assert not inspect.isabstract(TypeSpecCS)


def test_typespeccs_constructor_exists():
    assert callable(TypeSpecCS.__init__)


def test_typespeccs_constructor_args():
    sig = inspect.signature(TypeSpecCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingextensioncs_is_not_abstract():
    assert not inspect.isabstract(MappingExtensionCS)


def test_mappingextensioncs_constructor_exists():
    assert callable(MappingExtensionCS.__init__)


def test_mappingextensioncs_constructor_args():
    sig = inspect.signature(MappingExtensionCS.__init__)
    params = list(sig.parameters.keys())



def test_directionkindcs_is_not_abstract():
    assert not inspect.isabstract(DirectionKindCS)


def test_directionkindcs_constructor_exists():
    assert callable(DirectionKindCS.__init__)


def test_directionkindcs_constructor_args():
    sig = inspect.signature(DirectionKindCS.__init__)
    params = list(sig.parameters.keys())



def test_parameterdeclarationcs_is_not_abstract():
    assert not inspect.isabstract(ParameterDeclarationCS)


def test_parameterdeclarationcs_constructor_exists():
    assert callable(ParameterDeclarationCS.__init__)


def test_parameterdeclarationcs_constructor_args():
    sig = inspect.signature(ParameterDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExpCS)


def test_primitiveliteralexpcs_constructor_exists():
    assert callable(PrimitiveLiteralExpCS.__init__)


def test_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_oppositepropertycs_is_not_abstract():
    assert not inspect.isabstract(OppositePropertyCS)


def test_oppositepropertycs_constructor_exists():
    assert callable(OppositePropertyCS.__init__)


def test_oppositepropertycs_constructor_args():
    sig = inspect.signature(OppositePropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_multiplicitydefcs_is_not_abstract():
    assert not inspect.isabstract(MultiplicityDefCS)


def test_multiplicitydefcs_constructor_exists():
    assert callable(MultiplicityDefCS.__init__)


def test_multiplicitydefcs_constructor_args():
    sig = inspect.signature(MultiplicityDefCS.__init__)
    params = list(sig.parameters.keys())



def test_localpropertycs_is_not_abstract():
    assert not inspect.isabstract(LocalPropertyCS)


def test_localpropertycs_constructor_exists():
    assert callable(LocalPropertyCS.__init__)


def test_localpropertycs_constructor_args():
    sig = inspect.signature(LocalPropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_classifierpropertycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ClassifierPropertyCS)


def test_qvtoperational_cst_classifierpropertycs_constructor_exists():
    assert callable(qvtoperational_cst_ClassifierPropertyCS.__init__)


def test_qvtoperational_cst_classifierpropertycs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ClassifierPropertyCS.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_qvtoperational_cst_classifierpropertycs_has_isOrdered():
    assert hasattr(qvtoperational_cst_ClassifierPropertyCS, "isOrdered")
    descriptor = None
    for klass in qvtoperational_cst_ClassifierPropertyCS.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(OCLExpressionCS)


def test_oclexpressioncs_constructor_exists():
    assert callable(OCLExpressionCS.__init__)


def test_oclexpressioncs_constructor_args():
    sig = inspect.signature(OCLExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_statementcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_StatementCS)


def test_qvtoperational_cst_statementcs_constructor_exists():
    assert callable(qvtoperational_cst_StatementCS.__init__)


def test_qvtoperational_cst_statementcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_StatementCS.__init__)
    params = list(sig.parameters.keys())



def test_stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(StringLiteralExpCS)


def test_stringliteralexpcs_constructor_exists():
    assert callable(StringLiteralExpCS.__init__)


def test_stringliteralexpcs_constructor_args():
    sig = inspect.signature(StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_simplenamecs_is_not_abstract():
    assert not inspect.isabstract(SimpleNameCS)


def test_simplenamecs_constructor_exists():
    assert callable(SimpleNameCS.__init__)


def test_simplenamecs_constructor_args():
    sig = inspect.signature(SimpleNameCS.__init__)
    params = list(sig.parameters.keys())



def test_typecs_is_not_abstract():
    assert not inspect.isabstract(TypeCS)


def test_typecs_constructor_exists():
    assert callable(TypeCS.__init__)


def test_typecs_constructor_args():
    sig = inspect.signature(TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_listtypecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ListTypeCS)


def test_qvtoperational_cst_listtypecs_constructor_exists():
    assert callable(qvtoperational_cst_ListTypeCS.__init__)


def test_qvtoperational_cst_listtypecs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ListTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_dictionarytypecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_DictionaryTypeCS)


def test_qvtoperational_cst_dictionarytypecs_constructor_exists():
    assert callable(qvtoperational_cst_DictionaryTypeCS.__init__)


def test_qvtoperational_cst_dictionarytypecs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_DictionaryTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(PathNameCS)


def test_pathnamecs_constructor_exists():
    assert callable(PathNameCS.__init__)


def test_pathnamecs_constructor_args():
    sig = inspect.signature(PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingmodulecs_is_not_abstract():
    assert not inspect.isabstract(MappingModuleCS)


def test_mappingmodulecs_constructor_exists():
    assert callable(MappingModuleCS.__init__)


def test_mappingmodulecs_constructor_args():
    sig = inspect.signature(MappingModuleCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_librarycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_LibraryCS)


def test_qvtoperational_cst_librarycs_constructor_exists():
    assert callable(qvtoperational_cst_LibraryCS.__init__)


def test_qvtoperational_cst_librarycs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_LibraryCS.__init__)
    params = list(sig.parameters.keys())



def test_tagcs_is_not_abstract():
    assert not inspect.isabstract(TagCS)


def test_tagcs_constructor_exists():
    assert callable(TagCS.__init__)


def test_tagcs_constructor_args():
    sig = inspect.signature(TagCS.__init__)
    params = list(sig.parameters.keys())



def test_classifierdefcs_is_not_abstract():
    assert not inspect.isabstract(ClassifierDefCS)


def test_classifierdefcs_constructor_exists():
    assert callable(ClassifierDefCS.__init__)


def test_classifierdefcs_constructor_args():
    sig = inspect.signature(ClassifierDefCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingmethodcs_is_not_abstract():
    assert not inspect.isabstract(MappingMethodCS)


def test_mappingmethodcs_constructor_exists():
    assert callable(MappingMethodCS.__init__)


def test_mappingmethodcs_constructor_args():
    sig = inspect.signature(MappingMethodCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_mappingrulecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_MappingRuleCS)


def test_qvtoperational_cst_mappingrulecs_constructor_exists():
    assert callable(qvtoperational_cst_MappingRuleCS.__init__)


def test_qvtoperational_cst_mappingrulecs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_MappingRuleCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_mappingquerycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_MappingQueryCS)


def test_qvtoperational_cst_mappingquerycs_constructor_exists():
    assert callable(qvtoperational_cst_MappingQueryCS.__init__)


def test_qvtoperational_cst_mappingquerycs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_MappingQueryCS.__init__)
    params = list(sig.parameters.keys())
    assert "isSimpleDefinition" in params, "Missing parameter 'isSimpleDefinition'"

def test_qvtoperational_cst_mappingquerycs_has_isSimpleDefinition():
    assert hasattr(qvtoperational_cst_MappingQueryCS, "isSimpleDefinition")
    descriptor = None
    for klass in qvtoperational_cst_MappingQueryCS.__mro__:
        if "isSimpleDefinition" in klass.__dict__:
            descriptor = klass.__dict__["isSimpleDefinition"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_cst_constructorcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ConstructorCS)


def test_qvtoperational_cst_constructorcs_constructor_exists():
    assert callable(qvtoperational_cst_ConstructorCS.__init__)


def test_qvtoperational_cst_constructorcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ConstructorCS.__init__)
    params = list(sig.parameters.keys())



def test_modulepropertycs_is_not_abstract():
    assert not inspect.isabstract(ModulePropertyCS)


def test_modulepropertycs_constructor_exists():
    assert callable(ModulePropertyCS.__init__)


def test_modulepropertycs_constructor_args():
    sig = inspect.signature(ModulePropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_localpropertycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_LocalPropertyCS)


def test_qvtoperational_cst_localpropertycs_constructor_exists():
    assert callable(qvtoperational_cst_LocalPropertyCS.__init__)


def test_qvtoperational_cst_localpropertycs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_LocalPropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_configpropertycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ConfigPropertyCS)


def test_qvtoperational_cst_configpropertycs_constructor_exists():
    assert callable(qvtoperational_cst_ConfigPropertyCS.__init__)


def test_qvtoperational_cst_configpropertycs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ConfigPropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_contextualpropertycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ContextualPropertyCS)


def test_qvtoperational_cst_contextualpropertycs_constructor_exists():
    assert callable(qvtoperational_cst_ContextualPropertyCS.__init__)


def test_qvtoperational_cst_contextualpropertycs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ContextualPropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_modeltypecs_is_not_abstract():
    assert not inspect.isabstract(ModelTypeCS)


def test_modeltypecs_constructor_exists():
    assert callable(ModelTypeCS.__init__)


def test_modeltypecs_constructor_args():
    sig = inspect.signature(ModelTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_importcs_is_not_abstract():
    assert not inspect.isabstract(ImportCS)


def test_importcs_constructor_exists():
    assert callable(ImportCS.__init__)


def test_importcs_constructor_args():
    sig = inspect.signature(ImportCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_libraryimportcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_LibraryImportCS)


def test_qvtoperational_cst_libraryimportcs_constructor_exists():
    assert callable(qvtoperational_cst_LibraryImportCS.__init__)


def test_qvtoperational_cst_libraryimportcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_LibraryImportCS.__init__)
    params = list(sig.parameters.keys())



def test_transformationheadercs_is_not_abstract():
    assert not inspect.isabstract(TransformationHeaderCS)


def test_transformationheadercs_constructor_exists():
    assert callable(TransformationHeaderCS.__init__)


def test_transformationheadercs_constructor_args():
    sig = inspect.signature(TransformationHeaderCS.__init__)
    params = list(sig.parameters.keys())



def test_cstnode_is_not_abstract():
    assert not inspect.isabstract(CSTNode)


def test_cstnode_constructor_exists():
    assert callable(CSTNode.__init__)


def test_cstnode_constructor_args():
    sig = inspect.signature(CSTNode.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_multiplicitydefcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_MultiplicityDefCS)


def test_qvtoperational_cst_multiplicitydefcs_constructor_exists():
    assert callable(qvtoperational_cst_MultiplicityDefCS.__init__)


def test_qvtoperational_cst_multiplicitydefcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_MultiplicityDefCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_mappingmethodcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_MappingMethodCS)


def test_qvtoperational_cst_mappingmethodcs_constructor_exists():
    assert callable(qvtoperational_cst_MappingMethodCS.__init__)


def test_qvtoperational_cst_mappingmethodcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_MappingMethodCS.__init__)
    params = list(sig.parameters.keys())
    assert "blackBox" in params, "Missing parameter 'blackBox'"

def test_qvtoperational_cst_mappingmethodcs_has_blackBox():
    assert hasattr(qvtoperational_cst_MappingMethodCS, "blackBox")
    descriptor = None
    for klass in qvtoperational_cst_MappingMethodCS.__mro__:
        if "blackBox" in klass.__dict__:
            descriptor = klass.__dict__["blackBox"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_cst_completesignaturecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_CompleteSignatureCS)


def test_qvtoperational_cst_completesignaturecs_constructor_exists():
    assert callable(qvtoperational_cst_CompleteSignatureCS.__init__)


def test_qvtoperational_cst_completesignaturecs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_CompleteSignatureCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_modulepropertycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ModulePropertyCS)


def test_qvtoperational_cst_modulepropertycs_constructor_exists():
    assert callable(qvtoperational_cst_ModulePropertyCS.__init__)


def test_qvtoperational_cst_modulepropertycs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ModulePropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_simplesignaturecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_SimpleSignatureCS)


def test_qvtoperational_cst_simplesignaturecs_constructor_exists():
    assert callable(qvtoperational_cst_SimpleSignatureCS.__init__)


def test_qvtoperational_cst_simplesignaturecs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_SimpleSignatureCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_renamecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_RenameCS)


def test_qvtoperational_cst_renamecs_constructor_exists():
    assert callable(qvtoperational_cst_RenameCS.__init__)


def test_qvtoperational_cst_renamecs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_RenameCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_mappingdeclarationcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_MappingDeclarationCS)


def test_qvtoperational_cst_mappingdeclarationcs_constructor_exists():
    assert callable(qvtoperational_cst_MappingDeclarationCS.__init__)


def test_qvtoperational_cst_mappingdeclarationcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_MappingDeclarationCS.__init__)
    params = list(sig.parameters.keys())
    assert "isQuery" in params, "Missing parameter 'isQuery'"
    assert "qualifiers" in params, "Missing parameter 'qualifiers'"

def test_qvtoperational_cst_mappingdeclarationcs_has_isQuery():
    assert hasattr(qvtoperational_cst_MappingDeclarationCS, "isQuery")
    descriptor = None
    for klass in qvtoperational_cst_MappingDeclarationCS.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational_cst_mappingdeclarationcs_has_qualifiers():
    assert hasattr(qvtoperational_cst_MappingDeclarationCS, "qualifiers")
    descriptor = None
    for klass in qvtoperational_cst_MappingDeclarationCS.__mro__:
        if "qualifiers" in klass.__dict__:
            descriptor = klass.__dict__["qualifiers"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_cst_transformationheadercs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_TransformationHeaderCS)


def test_qvtoperational_cst_transformationheadercs_constructor_exists():
    assert callable(qvtoperational_cst_TransformationHeaderCS.__init__)


def test_qvtoperational_cst_transformationheadercs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_TransformationHeaderCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_mappingextensioncs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_MappingExtensionCS)


def test_qvtoperational_cst_mappingextensioncs_constructor_exists():
    assert callable(qvtoperational_cst_MappingExtensionCS.__init__)


def test_qvtoperational_cst_mappingextensioncs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_MappingExtensionCS.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_qvtoperational_cst_mappingextensioncs_has_kind():
    assert hasattr(qvtoperational_cst_MappingExtensionCS, "kind")
    descriptor = None
    for klass in qvtoperational_cst_MappingExtensionCS.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_cst_classifierdefcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ClassifierDefCS)


def test_qvtoperational_cst_classifierdefcs_constructor_exists():
    assert callable(qvtoperational_cst_ClassifierDefCS.__init__)


def test_qvtoperational_cst_classifierdefcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ClassifierDefCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_transformationrefinecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_TransformationRefineCS)


def test_qvtoperational_cst_transformationrefinecs_constructor_exists():
    assert callable(qvtoperational_cst_TransformationRefineCS.__init__)


def test_qvtoperational_cst_transformationrefinecs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_TransformationRefineCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_typespeccs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_TypeSpecCS)


def test_qvtoperational_cst_typespeccs_constructor_exists():
    assert callable(qvtoperational_cst_TypeSpecCS.__init__)


def test_qvtoperational_cst_typespeccs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_TypeSpecCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_modulekindcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ModuleKindCS)


def test_qvtoperational_cst_modulekindcs_constructor_exists():
    assert callable(qvtoperational_cst_ModuleKindCS.__init__)


def test_qvtoperational_cst_modulekindcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ModuleKindCS.__init__)
    params = list(sig.parameters.keys())
    assert "moduleKind" in params, "Missing parameter 'moduleKind'"

def test_qvtoperational_cst_modulekindcs_has_moduleKind():
    assert hasattr(qvtoperational_cst_ModuleKindCS, "moduleKind")
    descriptor = None
    for klass in qvtoperational_cst_ModuleKindCS.__mro__:
        if "moduleKind" in klass.__dict__:
            descriptor = klass.__dict__["moduleKind"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_cst_resolveopargsexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ResolveOpArgsExpCS)


def test_qvtoperational_cst_resolveopargsexpcs_constructor_exists():
    assert callable(qvtoperational_cst_ResolveOpArgsExpCS.__init__)


def test_qvtoperational_cst_resolveopargsexpcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ResolveOpArgsExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_tagcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_TagCS)


def test_qvtoperational_cst_tagcs_constructor_exists():
    assert callable(qvtoperational_cst_TagCS.__init__)


def test_qvtoperational_cst_tagcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_TagCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_unitcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_UnitCS)


def test_qvtoperational_cst_unitcs_constructor_exists():
    assert callable(qvtoperational_cst_UnitCS.__init__)


def test_qvtoperational_cst_unitcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_UnitCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_mappingsectionscs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_MappingSectionsCS)


def test_qvtoperational_cst_mappingsectionscs_constructor_exists():
    assert callable(qvtoperational_cst_MappingSectionsCS.__init__)


def test_qvtoperational_cst_mappingsectionscs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_MappingSectionsCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_parameterdeclarationcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ParameterDeclarationCS)


def test_qvtoperational_cst_parameterdeclarationcs_constructor_exists():
    assert callable(qvtoperational_cst_ParameterDeclarationCS.__init__)


def test_qvtoperational_cst_parameterdeclarationcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ParameterDeclarationCS.__init__)
    params = list(sig.parameters.keys())
    assert "directionKind" in params, "Missing parameter 'directionKind'"

def test_qvtoperational_cst_parameterdeclarationcs_has_directionKind():
    assert hasattr(qvtoperational_cst_ParameterDeclarationCS, "directionKind")
    descriptor = None
    for klass in qvtoperational_cst_ParameterDeclarationCS.__mro__:
        if "directionKind" in klass.__dict__:
            descriptor = klass.__dict__["directionKind"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_cst_importcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ImportCS)


def test_qvtoperational_cst_importcs_constructor_exists():
    assert callable(qvtoperational_cst_ImportCS.__init__)


def test_qvtoperational_cst_importcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ImportCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_modulerefcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ModuleRefCS)


def test_qvtoperational_cst_modulerefcs_constructor_exists():
    assert callable(qvtoperational_cst_ModuleRefCS.__init__)


def test_qvtoperational_cst_modulerefcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ModuleRefCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_oppositepropertycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_OppositePropertyCS)


def test_qvtoperational_cst_oppositepropertycs_constructor_exists():
    assert callable(qvtoperational_cst_OppositePropertyCS.__init__)


def test_qvtoperational_cst_oppositepropertycs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_OppositePropertyCS.__init__)
    params = list(sig.parameters.keys())
    assert "isNavigable" in params, "Missing parameter 'isNavigable'"

def test_qvtoperational_cst_oppositepropertycs_has_isNavigable():
    assert hasattr(qvtoperational_cst_OppositePropertyCS, "isNavigable")
    descriptor = None
    for klass in qvtoperational_cst_OppositePropertyCS.__mro__:
        if "isNavigable" in klass.__dict__:
            descriptor = klass.__dict__["isNavigable"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_cst_moduleusagecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ModuleUsageCS)


def test_qvtoperational_cst_moduleusagecs_constructor_exists():
    assert callable(qvtoperational_cst_ModuleUsageCS.__init__)


def test_qvtoperational_cst_moduleusagecs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ModuleUsageCS.__init__)
    params = list(sig.parameters.keys())
    assert "importKind" in params, "Missing parameter 'importKind'"

def test_qvtoperational_cst_moduleusagecs_has_importKind():
    assert hasattr(qvtoperational_cst_ModuleUsageCS, "importKind")
    descriptor = None
    for klass in qvtoperational_cst_ModuleUsageCS.__mro__:
        if "importKind" in klass.__dict__:
            descriptor = klass.__dict__["importKind"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_cst_packagerefcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_PackageRefCS)


def test_qvtoperational_cst_packagerefcs_constructor_exists():
    assert callable(qvtoperational_cst_PackageRefCS.__init__)


def test_qvtoperational_cst_packagerefcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_PackageRefCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_dictliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_DictLiteralPartCS)


def test_qvtoperational_cst_dictliteralpartcs_constructor_exists():
    assert callable(qvtoperational_cst_DictLiteralPartCS.__init__)


def test_qvtoperational_cst_dictliteralpartcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_DictLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational_cst_directionkindcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_DirectionKindCS)


def test_qvtoperational_cst_directionkindcs_constructor_exists():
    assert callable(qvtoperational_cst_DirectionKindCS.__init__)


def test_qvtoperational_cst_directionkindcs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_DirectionKindCS.__init__)
    params = list(sig.parameters.keys())
    assert "directionKind" in params, "Missing parameter 'directionKind'"

def test_qvtoperational_cst_directionkindcs_has_directionKind():
    assert hasattr(qvtoperational_cst_DirectionKindCS, "directionKind")
    descriptor = None
    for klass in qvtoperational_cst_DirectionKindCS.__mro__:
        if "directionKind" in klass.__dict__:
            descriptor = klass.__dict__["directionKind"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_cst_scopednamecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_ScopedNameCS)


def test_qvtoperational_cst_scopednamecs_constructor_exists():
    assert callable(qvtoperational_cst_ScopedNameCS.__init__)


def test_qvtoperational_cst_scopednamecs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_ScopedNameCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qvtoperational_cst_scopednamecs_has_name():
    assert hasattr(qvtoperational_cst_ScopedNameCS, "name")
    descriptor = None
    for klass in qvtoperational_cst_ScopedNameCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational_cst_mappingmodulecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational_cst_MappingModuleCS)


def test_qvtoperational_cst_mappingmodulecs_constructor_exists():
    assert callable(qvtoperational_cst_MappingModuleCS.__init__)


def test_qvtoperational_cst_mappingmodulecs_constructor_args():
    sig = inspect.signature(qvtoperational_cst_MappingModuleCS.__init__)
    params = list(sig.parameters.keys())

def test_modulekindenum_exists():
    # Check that the Enumeration exists
    assert ModuleKindEnum is not None

def test_modulekindenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModuleKindEnum]
    expected_literals = [
        "transformation",
        "library",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModuleKindEnum"

def test_qualifierkindcs_exists():
    # Check that the Enumeration exists
    assert QualifierKindCS is not None

def test_qualifierkindcs_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in QualifierKindCS]
    expected_literals = [
        "blackbox",
        "static",
        "abstract",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in QualifierKindCS"

def test_directionkindenum_exists():
    # Check that the Enumeration exists
    assert DirectionKindEnum is not None

def test_directionkindenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionKindEnum]
    expected_literals = [
        "out",
        "DEFAULT",
        "inout",
        "in_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionKindEnum"

def test_importkindenum_exists():
    # Check that the Enumeration exists
    assert ImportKindEnum is not None

def test_importkindenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImportKindEnum]
    expected_literals = [
        "access",
        "extension",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImportKindEnum"

def test_mappingextensionkindcs_exists():
    # Check that the Enumeration exists
    assert MappingExtensionKindCS is not None

def test_mappingextensionkindcs_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MappingExtensionKindCS]
    expected_literals = [
        "merges",
        "inherits",
        "disjuncts",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MappingExtensionKindCS"


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
RenameCS_strategy = st.builds(
    RenameCS,
)
ClassifierPropertyCS_strategy = st.builds(
    ClassifierPropertyCS,
)
ScopedNameCS_strategy = st.builds(
    ScopedNameCS,
)
DictLiteralPartCS_strategy = st.builds(
    DictLiteralPartCS,
)
CollectionLiteralPartCS_strategy = st.builds(
    CollectionLiteralPartCS,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
qvtoperational_cst_DictLiteralExpCS_strategy = st.builds(
    qvtoperational_cst_DictLiteralExpCS,
)
qvtoperational_cst_ListLiteralExpCS_strategy = st.builds(
    qvtoperational_cst_ListLiteralExpCS,
)
ModuleRefCS_strategy = st.builds(
    ModuleRefCS,
)
ModuleKindCS_strategy = st.builds(
    ModuleKindCS,
)
LogExpCS_strategy = st.builds(
    LogExpCS,
)
TransformationRefineCS_strategy = st.builds(
    TransformationRefineCS,
)
ModuleUsageCS_strategy = st.builds(
    ModuleUsageCS,
)
PackageRefCS_strategy = st.builds(
    PackageRefCS,
)
ResolveExpCS_strategy = st.builds(
    ResolveExpCS,
)
qvtoperational_cst_ResolveInExpCS_strategy = st.builds(
    qvtoperational_cst_ResolveInExpCS,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
qvtoperational_cst_ResolveExpCS_strategy = st.builds(
    qvtoperational_cst_ResolveExpCS,
    isDeferred=
        st.booleans(),
    isInverse=
        st.booleans(),
    one=
        st.booleans()
)
qvtoperational_cst_ElementWithBody_strategy = st.builds(
    qvtoperational_cst_ElementWithBody,
    bodyEndLocation=
        st.integers(),
    bodyStartLocation=
        st.integers()
)
OperationCallExpCS_strategy = st.builds(
    OperationCallExpCS,
)
qvtoperational_cst_LogExpCS_strategy = st.builds(
    qvtoperational_cst_LogExpCS,
)
qvtoperational_cst_ImperativeOperationCallExpCS_strategy = st.builds(
    qvtoperational_cst_ImperativeOperationCallExpCS,
)
ImperativeOperationCallExpCS_strategy = st.builds(
    ImperativeOperationCallExpCS,
)
qvtoperational_cst_MappingCallExpCS_strategy = st.builds(
    qvtoperational_cst_MappingCallExpCS,
    strict=
        st.booleans()
)
cst_InstantiationExpCS_strategy = st.builds(
    cst_InstantiationExpCS,
)
SwitchAltExpCS_strategy = st.builds(
    SwitchAltExpCS,
)
ImperativeLoopExpCS_strategy = st.builds(
    ImperativeLoopExpCS,
)
qvtoperational_cst_ImperativeIterateExpCS_strategy = st.builds(
    qvtoperational_cst_ImperativeIterateExpCS,
)
qvtoperational_cst_ForExpCS_strategy = st.builds(
    qvtoperational_cst_ForExpCS,
)
cst_StatementCS_strategy = st.builds(
    cst_StatementCS,
)
cst_LoopExpCS_strategy = st.builds(
    cst_LoopExpCS,
)
qvtoperational_cst_ImperativeLoopExpCS_strategy = st.builds(
    qvtoperational_cst_ImperativeLoopExpCS,
)
VariableCS_strategy = st.builds(
    VariableCS,
)
StatementCS_strategy = st.builds(
    StatementCS,
)
qvtoperational_cst_WhileExpCS_strategy = st.builds(
    qvtoperational_cst_WhileExpCS,
)
qvtoperational_cst_AssignStatementCS_strategy = st.builds(
    qvtoperational_cst_AssignStatementCS,
    incremental=
        st.booleans()
)
qvtoperational_cst_ExpressionStatementCS_strategy = st.builds(
    qvtoperational_cst_ExpressionStatementCS,
)
qvtoperational_cst_AssertExpCS_strategy = st.builds(
    qvtoperational_cst_AssertExpCS,
)
qvtoperational_cst_ContinueExpCS_strategy = st.builds(
    qvtoperational_cst_ContinueExpCS,
)
qvtoperational_cst_VariableInitializationCS_strategy = st.builds(
    qvtoperational_cst_VariableInitializationCS,
    withResult=
        st.booleans()
)
qvtoperational_cst_SwitchAltExpCS_strategy = st.builds(
    qvtoperational_cst_SwitchAltExpCS,
)
qvtoperational_cst_SwitchExpCS_strategy = st.builds(
    qvtoperational_cst_SwitchExpCS,
)
qvtoperational_cst_ReturnExpCS_strategy = st.builds(
    qvtoperational_cst_ReturnExpCS,
)
qvtoperational_cst_ComputeExpCS_strategy = st.builds(
    qvtoperational_cst_ComputeExpCS,
)
qvtoperational_cst_BreakExpCS_strategy = st.builds(
    qvtoperational_cst_BreakExpCS,
)
qvtoperational_cst_InstantiationExpCS_strategy = st.builds(
    qvtoperational_cst_InstantiationExpCS,
)
qvtoperational_cst_BlockExpCS_strategy = st.builds(
    qvtoperational_cst_BlockExpCS,
)
MappingEndCS_strategy = st.builds(
    MappingEndCS,
)
MappingBodyCS_strategy = st.builds(
    MappingBodyCS,
)
MappingInitCS_strategy = st.builds(
    MappingInitCS,
)
MappingSectionCS_strategy = st.builds(
    MappingSectionCS,
)
qvtoperational_cst_MappingEndCS_strategy = st.builds(
    qvtoperational_cst_MappingEndCS,
)
qvtoperational_cst_MappingBodyCS_strategy = st.builds(
    qvtoperational_cst_MappingBodyCS,
    hasPopulationKeyword=
        st.booleans()
)
qvtoperational_cst_MappingInitCS_strategy = st.builds(
    qvtoperational_cst_MappingInitCS,
)
MappingRuleCS_strategy = st.builds(
    MappingRuleCS,
)
cst_ElementWithBody_strategy = st.builds(
    cst_ElementWithBody,
)
qvtoperational_cst_ObjectExpCS_strategy = st.builds(
    qvtoperational_cst_ObjectExpCS,
    isImplicit=
        st.booleans()
)
cst_CSTNode_strategy = st.builds(
    cst_CSTNode,
)
qvtoperational_cst_ModelTypeCS_strategy = st.builds(
    qvtoperational_cst_ModelTypeCS,
)
qvtoperational_cst_MappingSectionCS_strategy = st.builds(
    qvtoperational_cst_MappingSectionCS,
)
MappingSectionsCS_strategy = st.builds(
    MappingSectionsCS,
)
MappingDeclarationCS_strategy = st.builds(
    MappingDeclarationCS,
)
SimpleSignatureCS_strategy = st.builds(
    SimpleSignatureCS,
)
TypeSpecCS_strategy = st.builds(
    TypeSpecCS,
)
MappingExtensionCS_strategy = st.builds(
    MappingExtensionCS,
)
DirectionKindCS_strategy = st.builds(
    DirectionKindCS,
)
ParameterDeclarationCS_strategy = st.builds(
    ParameterDeclarationCS,
)
PrimitiveLiteralExpCS_strategy = st.builds(
    PrimitiveLiteralExpCS,
)
OppositePropertyCS_strategy = st.builds(
    OppositePropertyCS,
)
MultiplicityDefCS_strategy = st.builds(
    MultiplicityDefCS,
)
LocalPropertyCS_strategy = st.builds(
    LocalPropertyCS,
)
qvtoperational_cst_ClassifierPropertyCS_strategy = st.builds(
    qvtoperational_cst_ClassifierPropertyCS,
    isOrdered=
        st.booleans()
)
OCLExpressionCS_strategy = st.builds(
    OCLExpressionCS,
)
qvtoperational_cst_StatementCS_strategy = st.builds(
    qvtoperational_cst_StatementCS,
)
StringLiteralExpCS_strategy = st.builds(
    StringLiteralExpCS,
)
SimpleNameCS_strategy = st.builds(
    SimpleNameCS,
)
TypeCS_strategy = st.builds(
    TypeCS,
)
qvtoperational_cst_ListTypeCS_strategy = st.builds(
    qvtoperational_cst_ListTypeCS,
)
qvtoperational_cst_DictionaryTypeCS_strategy = st.builds(
    qvtoperational_cst_DictionaryTypeCS,
)
PathNameCS_strategy = st.builds(
    PathNameCS,
)
MappingModuleCS_strategy = st.builds(
    MappingModuleCS,
)
qvtoperational_cst_LibraryCS_strategy = st.builds(
    qvtoperational_cst_LibraryCS,
)
TagCS_strategy = st.builds(
    TagCS,
)
ClassifierDefCS_strategy = st.builds(
    ClassifierDefCS,
)
MappingMethodCS_strategy = st.builds(
    MappingMethodCS,
)
qvtoperational_cst_MappingRuleCS_strategy = st.builds(
    qvtoperational_cst_MappingRuleCS,
)
qvtoperational_cst_MappingQueryCS_strategy = st.builds(
    qvtoperational_cst_MappingQueryCS,
    isSimpleDefinition=
        st.booleans()
)
qvtoperational_cst_ConstructorCS_strategy = st.builds(
    qvtoperational_cst_ConstructorCS,
)
ModulePropertyCS_strategy = st.builds(
    ModulePropertyCS,
)
qvtoperational_cst_LocalPropertyCS_strategy = st.builds(
    qvtoperational_cst_LocalPropertyCS,
)
qvtoperational_cst_ConfigPropertyCS_strategy = st.builds(
    qvtoperational_cst_ConfigPropertyCS,
)
qvtoperational_cst_ContextualPropertyCS_strategy = st.builds(
    qvtoperational_cst_ContextualPropertyCS,
)
ModelTypeCS_strategy = st.builds(
    ModelTypeCS,
)
ImportCS_strategy = st.builds(
    ImportCS,
)
qvtoperational_cst_LibraryImportCS_strategy = st.builds(
    qvtoperational_cst_LibraryImportCS,
)
TransformationHeaderCS_strategy = st.builds(
    TransformationHeaderCS,
)
CSTNode_strategy = st.builds(
    CSTNode,
)
qvtoperational_cst_MultiplicityDefCS_strategy = st.builds(
    qvtoperational_cst_MultiplicityDefCS,
)
qvtoperational_cst_MappingMethodCS_strategy = st.builds(
    qvtoperational_cst_MappingMethodCS,
    blackBox=
        st.booleans()
)
qvtoperational_cst_CompleteSignatureCS_strategy = st.builds(
    qvtoperational_cst_CompleteSignatureCS,
)
qvtoperational_cst_ModulePropertyCS_strategy = st.builds(
    qvtoperational_cst_ModulePropertyCS,
)
qvtoperational_cst_SimpleSignatureCS_strategy = st.builds(
    qvtoperational_cst_SimpleSignatureCS,
)
qvtoperational_cst_RenameCS_strategy = st.builds(
    qvtoperational_cst_RenameCS,
)
qvtoperational_cst_MappingDeclarationCS_strategy = st.builds(
    qvtoperational_cst_MappingDeclarationCS,
    isQuery=
        st.booleans(),
    qualifiers=
        safe_text
)
qvtoperational_cst_TransformationHeaderCS_strategy = st.builds(
    qvtoperational_cst_TransformationHeaderCS,
)
qvtoperational_cst_MappingExtensionCS_strategy = st.builds(
    qvtoperational_cst_MappingExtensionCS,
    kind=
        safe_text
)
qvtoperational_cst_ClassifierDefCS_strategy = st.builds(
    qvtoperational_cst_ClassifierDefCS,
)
qvtoperational_cst_TransformationRefineCS_strategy = st.builds(
    qvtoperational_cst_TransformationRefineCS,
)
qvtoperational_cst_TypeSpecCS_strategy = st.builds(
    qvtoperational_cst_TypeSpecCS,
)
qvtoperational_cst_ModuleKindCS_strategy = st.builds(
    qvtoperational_cst_ModuleKindCS,
    moduleKind=
        safe_text
)
qvtoperational_cst_ResolveOpArgsExpCS_strategy = st.builds(
    qvtoperational_cst_ResolveOpArgsExpCS,
)
qvtoperational_cst_TagCS_strategy = st.builds(
    qvtoperational_cst_TagCS,
)
qvtoperational_cst_UnitCS_strategy = st.builds(
    qvtoperational_cst_UnitCS,
)
qvtoperational_cst_MappingSectionsCS_strategy = st.builds(
    qvtoperational_cst_MappingSectionsCS,
)
qvtoperational_cst_ParameterDeclarationCS_strategy = st.builds(
    qvtoperational_cst_ParameterDeclarationCS,
    directionKind=
        safe_text
)
qvtoperational_cst_ImportCS_strategy = st.builds(
    qvtoperational_cst_ImportCS,
)
qvtoperational_cst_ModuleRefCS_strategy = st.builds(
    qvtoperational_cst_ModuleRefCS,
)
qvtoperational_cst_OppositePropertyCS_strategy = st.builds(
    qvtoperational_cst_OppositePropertyCS,
    isNavigable=
        st.booleans()
)
qvtoperational_cst_ModuleUsageCS_strategy = st.builds(
    qvtoperational_cst_ModuleUsageCS,
    importKind=
        safe_text
)
qvtoperational_cst_PackageRefCS_strategy = st.builds(
    qvtoperational_cst_PackageRefCS,
)
qvtoperational_cst_DictLiteralPartCS_strategy = st.builds(
    qvtoperational_cst_DictLiteralPartCS,
)
qvtoperational_cst_DirectionKindCS_strategy = st.builds(
    qvtoperational_cst_DirectionKindCS,
    directionKind=
        safe_text
)
qvtoperational_cst_ScopedNameCS_strategy = st.builds(
    qvtoperational_cst_ScopedNameCS,
    name=
        safe_text
)
qvtoperational_cst_MappingModuleCS_strategy = st.builds(
    qvtoperational_cst_MappingModuleCS,
)

@given(instance=RenameCS_strategy)
@settings(max_examples=50)
def test_renamecs_instantiation(instance):
    assert isinstance(instance, RenameCS)

@given(instance=ClassifierPropertyCS_strategy)
@settings(max_examples=50)
def test_classifierpropertycs_instantiation(instance):
    assert isinstance(instance, ClassifierPropertyCS)

@given(instance=ScopedNameCS_strategy)
@settings(max_examples=50)
def test_scopednamecs_instantiation(instance):
    assert isinstance(instance, ScopedNameCS)

@given(instance=DictLiteralPartCS_strategy)
@settings(max_examples=50)
def test_dictliteralpartcs_instantiation(instance):
    assert isinstance(instance, DictLiteralPartCS)

@given(instance=CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPartCS)

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=qvtoperational_cst_DictLiteralExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_dictliteralexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_DictLiteralExpCS)

@given(instance=qvtoperational_cst_ListLiteralExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_listliteralexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ListLiteralExpCS)

@given(instance=ModuleRefCS_strategy)
@settings(max_examples=50)
def test_modulerefcs_instantiation(instance):
    assert isinstance(instance, ModuleRefCS)

@given(instance=ModuleKindCS_strategy)
@settings(max_examples=50)
def test_modulekindcs_instantiation(instance):
    assert isinstance(instance, ModuleKindCS)

@given(instance=LogExpCS_strategy)
@settings(max_examples=50)
def test_logexpcs_instantiation(instance):
    assert isinstance(instance, LogExpCS)

@given(instance=TransformationRefineCS_strategy)
@settings(max_examples=50)
def test_transformationrefinecs_instantiation(instance):
    assert isinstance(instance, TransformationRefineCS)

@given(instance=ModuleUsageCS_strategy)
@settings(max_examples=50)
def test_moduleusagecs_instantiation(instance):
    assert isinstance(instance, ModuleUsageCS)

@given(instance=PackageRefCS_strategy)
@settings(max_examples=50)
def test_packagerefcs_instantiation(instance):
    assert isinstance(instance, PackageRefCS)

@given(instance=ResolveExpCS_strategy)
@settings(max_examples=50)
def test_resolveexpcs_instantiation(instance):
    assert isinstance(instance, ResolveExpCS)

@given(instance=qvtoperational_cst_ResolveInExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_resolveinexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ResolveInExpCS)

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=qvtoperational_cst_ResolveExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_resolveexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ResolveExpCS)



@given(instance=qvtoperational_cst_ResolveExpCS_strategy)
def test_qvtoperational_cst_resolveexpcs_isDeferred_setter(instance):
    original = instance.isDeferred
    instance.isDeferred = original
    assert instance.isDeferred == original



@given(instance=qvtoperational_cst_ResolveExpCS_strategy)
def test_qvtoperational_cst_resolveexpcs_isInverse_setter(instance):
    original = instance.isInverse
    instance.isInverse = original
    assert instance.isInverse == original



@given(instance=qvtoperational_cst_ResolveExpCS_strategy)
def test_qvtoperational_cst_resolveexpcs_one_setter(instance):
    original = instance.one
    instance.one = original
    assert instance.one == original

@given(instance=qvtoperational_cst_ElementWithBody_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_elementwithbody_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ElementWithBody)



@given(instance=qvtoperational_cst_ElementWithBody_strategy)
def test_qvtoperational_cst_elementwithbody_bodyEndLocation_setter(instance):
    original = instance.bodyEndLocation
    instance.bodyEndLocation = original
    assert instance.bodyEndLocation == original



@given(instance=qvtoperational_cst_ElementWithBody_strategy)
def test_qvtoperational_cst_elementwithbody_bodyStartLocation_setter(instance):
    original = instance.bodyStartLocation
    instance.bodyStartLocation = original
    assert instance.bodyStartLocation == original

@given(instance=OperationCallExpCS_strategy)
@settings(max_examples=50)
def test_operationcallexpcs_instantiation(instance):
    assert isinstance(instance, OperationCallExpCS)

@given(instance=qvtoperational_cst_LogExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_logexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_LogExpCS)

@given(instance=qvtoperational_cst_ImperativeOperationCallExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_imperativeoperationcallexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ImperativeOperationCallExpCS)

@given(instance=ImperativeOperationCallExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoperationcallexpcs_instantiation(instance):
    assert isinstance(instance, ImperativeOperationCallExpCS)

@given(instance=qvtoperational_cst_MappingCallExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_mappingcallexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_MappingCallExpCS)



@given(instance=qvtoperational_cst_MappingCallExpCS_strategy)
def test_qvtoperational_cst_mappingcallexpcs_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original

@given(instance=cst_InstantiationExpCS_strategy)
@settings(max_examples=50)
def test_cst_instantiationexpcs_instantiation(instance):
    assert isinstance(instance, cst_InstantiationExpCS)

@given(instance=SwitchAltExpCS_strategy)
@settings(max_examples=50)
def test_switchaltexpcs_instantiation(instance):
    assert isinstance(instance, SwitchAltExpCS)

@given(instance=ImperativeLoopExpCS_strategy)
@settings(max_examples=50)
def test_imperativeloopexpcs_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExpCS)

@given(instance=qvtoperational_cst_ImperativeIterateExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_imperativeiterateexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ImperativeIterateExpCS)

@given(instance=qvtoperational_cst_ForExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_forexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ForExpCS)

@given(instance=cst_StatementCS_strategy)
@settings(max_examples=50)
def test_cst_statementcs_instantiation(instance):
    assert isinstance(instance, cst_StatementCS)

@given(instance=cst_LoopExpCS_strategy)
@settings(max_examples=50)
def test_cst_loopexpcs_instantiation(instance):
    assert isinstance(instance, cst_LoopExpCS)

@given(instance=qvtoperational_cst_ImperativeLoopExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_imperativeloopexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ImperativeLoopExpCS)

@given(instance=VariableCS_strategy)
@settings(max_examples=50)
def test_variablecs_instantiation(instance):
    assert isinstance(instance, VariableCS)

@given(instance=StatementCS_strategy)
@settings(max_examples=50)
def test_statementcs_instantiation(instance):
    assert isinstance(instance, StatementCS)

@given(instance=qvtoperational_cst_WhileExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_whileexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_WhileExpCS)

@given(instance=qvtoperational_cst_AssignStatementCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_assignstatementcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_AssignStatementCS)



@given(instance=qvtoperational_cst_AssignStatementCS_strategy)
def test_qvtoperational_cst_assignstatementcs_incremental_setter(instance):
    original = instance.incremental
    instance.incremental = original
    assert instance.incremental == original

@given(instance=qvtoperational_cst_ExpressionStatementCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_expressionstatementcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ExpressionStatementCS)

@given(instance=qvtoperational_cst_AssertExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_assertexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_AssertExpCS)

@given(instance=qvtoperational_cst_ContinueExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_continueexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ContinueExpCS)

@given(instance=qvtoperational_cst_VariableInitializationCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_variableinitializationcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_VariableInitializationCS)



@given(instance=qvtoperational_cst_VariableInitializationCS_strategy)
def test_qvtoperational_cst_variableinitializationcs_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=qvtoperational_cst_SwitchAltExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_switchaltexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_SwitchAltExpCS)

@given(instance=qvtoperational_cst_SwitchExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_switchexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_SwitchExpCS)

@given(instance=qvtoperational_cst_ReturnExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_returnexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ReturnExpCS)

@given(instance=qvtoperational_cst_ComputeExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_computeexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ComputeExpCS)

@given(instance=qvtoperational_cst_BreakExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_breakexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_BreakExpCS)

@given(instance=qvtoperational_cst_InstantiationExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_instantiationexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_InstantiationExpCS)

@given(instance=qvtoperational_cst_BlockExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_blockexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_BlockExpCS)

@given(instance=MappingEndCS_strategy)
@settings(max_examples=50)
def test_mappingendcs_instantiation(instance):
    assert isinstance(instance, MappingEndCS)

@given(instance=MappingBodyCS_strategy)
@settings(max_examples=50)
def test_mappingbodycs_instantiation(instance):
    assert isinstance(instance, MappingBodyCS)

@given(instance=MappingInitCS_strategy)
@settings(max_examples=50)
def test_mappinginitcs_instantiation(instance):
    assert isinstance(instance, MappingInitCS)

@given(instance=MappingSectionCS_strategy)
@settings(max_examples=50)
def test_mappingsectioncs_instantiation(instance):
    assert isinstance(instance, MappingSectionCS)

@given(instance=qvtoperational_cst_MappingEndCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_mappingendcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_MappingEndCS)

@given(instance=qvtoperational_cst_MappingBodyCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_mappingbodycs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_MappingBodyCS)



@given(instance=qvtoperational_cst_MappingBodyCS_strategy)
def test_qvtoperational_cst_mappingbodycs_hasPopulationKeyword_setter(instance):
    original = instance.hasPopulationKeyword
    instance.hasPopulationKeyword = original
    assert instance.hasPopulationKeyword == original

@given(instance=qvtoperational_cst_MappingInitCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_mappinginitcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_MappingInitCS)

@given(instance=MappingRuleCS_strategy)
@settings(max_examples=50)
def test_mappingrulecs_instantiation(instance):
    assert isinstance(instance, MappingRuleCS)

@given(instance=cst_ElementWithBody_strategy)
@settings(max_examples=50)
def test_cst_elementwithbody_instantiation(instance):
    assert isinstance(instance, cst_ElementWithBody)

@given(instance=qvtoperational_cst_ObjectExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_objectexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ObjectExpCS)



@given(instance=qvtoperational_cst_ObjectExpCS_strategy)
def test_qvtoperational_cst_objectexpcs_isImplicit_setter(instance):
    original = instance.isImplicit
    instance.isImplicit = original
    assert instance.isImplicit == original

@given(instance=cst_CSTNode_strategy)
@settings(max_examples=50)
def test_cst_cstnode_instantiation(instance):
    assert isinstance(instance, cst_CSTNode)

@given(instance=qvtoperational_cst_ModelTypeCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_modeltypecs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ModelTypeCS)

@given(instance=qvtoperational_cst_MappingSectionCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_mappingsectioncs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_MappingSectionCS)

@given(instance=MappingSectionsCS_strategy)
@settings(max_examples=50)
def test_mappingsectionscs_instantiation(instance):
    assert isinstance(instance, MappingSectionsCS)

@given(instance=MappingDeclarationCS_strategy)
@settings(max_examples=50)
def test_mappingdeclarationcs_instantiation(instance):
    assert isinstance(instance, MappingDeclarationCS)

@given(instance=SimpleSignatureCS_strategy)
@settings(max_examples=50)
def test_simplesignaturecs_instantiation(instance):
    assert isinstance(instance, SimpleSignatureCS)

@given(instance=TypeSpecCS_strategy)
@settings(max_examples=50)
def test_typespeccs_instantiation(instance):
    assert isinstance(instance, TypeSpecCS)

@given(instance=MappingExtensionCS_strategy)
@settings(max_examples=50)
def test_mappingextensioncs_instantiation(instance):
    assert isinstance(instance, MappingExtensionCS)

@given(instance=DirectionKindCS_strategy)
@settings(max_examples=50)
def test_directionkindcs_instantiation(instance):
    assert isinstance(instance, DirectionKindCS)

@given(instance=ParameterDeclarationCS_strategy)
@settings(max_examples=50)
def test_parameterdeclarationcs_instantiation(instance):
    assert isinstance(instance, ParameterDeclarationCS)

@given(instance=PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExpCS)

@given(instance=OppositePropertyCS_strategy)
@settings(max_examples=50)
def test_oppositepropertycs_instantiation(instance):
    assert isinstance(instance, OppositePropertyCS)

@given(instance=MultiplicityDefCS_strategy)
@settings(max_examples=50)
def test_multiplicitydefcs_instantiation(instance):
    assert isinstance(instance, MultiplicityDefCS)

@given(instance=LocalPropertyCS_strategy)
@settings(max_examples=50)
def test_localpropertycs_instantiation(instance):
    assert isinstance(instance, LocalPropertyCS)

@given(instance=qvtoperational_cst_ClassifierPropertyCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_classifierpropertycs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ClassifierPropertyCS)



@given(instance=qvtoperational_cst_ClassifierPropertyCS_strategy)
def test_qvtoperational_cst_classifierpropertycs_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=OCLExpressionCS_strategy)
@settings(max_examples=50)
def test_oclexpressioncs_instantiation(instance):
    assert isinstance(instance, OCLExpressionCS)

@given(instance=qvtoperational_cst_StatementCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_statementcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_StatementCS)

@given(instance=StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, StringLiteralExpCS)

@given(instance=SimpleNameCS_strategy)
@settings(max_examples=50)
def test_simplenamecs_instantiation(instance):
    assert isinstance(instance, SimpleNameCS)

@given(instance=TypeCS_strategy)
@settings(max_examples=50)
def test_typecs_instantiation(instance):
    assert isinstance(instance, TypeCS)

@given(instance=qvtoperational_cst_ListTypeCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_listtypecs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ListTypeCS)

@given(instance=qvtoperational_cst_DictionaryTypeCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_dictionarytypecs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_DictionaryTypeCS)

@given(instance=PathNameCS_strategy)
@settings(max_examples=50)
def test_pathnamecs_instantiation(instance):
    assert isinstance(instance, PathNameCS)

@given(instance=MappingModuleCS_strategy)
@settings(max_examples=50)
def test_mappingmodulecs_instantiation(instance):
    assert isinstance(instance, MappingModuleCS)

@given(instance=qvtoperational_cst_LibraryCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_librarycs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_LibraryCS)

@given(instance=TagCS_strategy)
@settings(max_examples=50)
def test_tagcs_instantiation(instance):
    assert isinstance(instance, TagCS)

@given(instance=ClassifierDefCS_strategy)
@settings(max_examples=50)
def test_classifierdefcs_instantiation(instance):
    assert isinstance(instance, ClassifierDefCS)

@given(instance=MappingMethodCS_strategy)
@settings(max_examples=50)
def test_mappingmethodcs_instantiation(instance):
    assert isinstance(instance, MappingMethodCS)

@given(instance=qvtoperational_cst_MappingRuleCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_mappingrulecs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_MappingRuleCS)

@given(instance=qvtoperational_cst_MappingQueryCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_mappingquerycs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_MappingQueryCS)



@given(instance=qvtoperational_cst_MappingQueryCS_strategy)
def test_qvtoperational_cst_mappingquerycs_isSimpleDefinition_setter(instance):
    original = instance.isSimpleDefinition
    instance.isSimpleDefinition = original
    assert instance.isSimpleDefinition == original

@given(instance=qvtoperational_cst_ConstructorCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_constructorcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ConstructorCS)

@given(instance=ModulePropertyCS_strategy)
@settings(max_examples=50)
def test_modulepropertycs_instantiation(instance):
    assert isinstance(instance, ModulePropertyCS)

@given(instance=qvtoperational_cst_LocalPropertyCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_localpropertycs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_LocalPropertyCS)

@given(instance=qvtoperational_cst_ConfigPropertyCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_configpropertycs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ConfigPropertyCS)

@given(instance=qvtoperational_cst_ContextualPropertyCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_contextualpropertycs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ContextualPropertyCS)

@given(instance=ModelTypeCS_strategy)
@settings(max_examples=50)
def test_modeltypecs_instantiation(instance):
    assert isinstance(instance, ModelTypeCS)

@given(instance=ImportCS_strategy)
@settings(max_examples=50)
def test_importcs_instantiation(instance):
    assert isinstance(instance, ImportCS)

@given(instance=qvtoperational_cst_LibraryImportCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_libraryimportcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_LibraryImportCS)

@given(instance=TransformationHeaderCS_strategy)
@settings(max_examples=50)
def test_transformationheadercs_instantiation(instance):
    assert isinstance(instance, TransformationHeaderCS)

@given(instance=CSTNode_strategy)
@settings(max_examples=50)
def test_cstnode_instantiation(instance):
    assert isinstance(instance, CSTNode)

@given(instance=qvtoperational_cst_MultiplicityDefCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_multiplicitydefcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_MultiplicityDefCS)

@given(instance=qvtoperational_cst_MappingMethodCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_mappingmethodcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_MappingMethodCS)



@given(instance=qvtoperational_cst_MappingMethodCS_strategy)
def test_qvtoperational_cst_mappingmethodcs_blackBox_setter(instance):
    original = instance.blackBox
    instance.blackBox = original
    assert instance.blackBox == original

@given(instance=qvtoperational_cst_CompleteSignatureCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_completesignaturecs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_CompleteSignatureCS)

@given(instance=qvtoperational_cst_ModulePropertyCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_modulepropertycs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ModulePropertyCS)

@given(instance=qvtoperational_cst_SimpleSignatureCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_simplesignaturecs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_SimpleSignatureCS)

@given(instance=qvtoperational_cst_RenameCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_renamecs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_RenameCS)

@given(instance=qvtoperational_cst_MappingDeclarationCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_mappingdeclarationcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_MappingDeclarationCS)



@given(instance=qvtoperational_cst_MappingDeclarationCS_strategy)
def test_qvtoperational_cst_mappingdeclarationcs_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original



@given(instance=qvtoperational_cst_MappingDeclarationCS_strategy)
def test_qvtoperational_cst_mappingdeclarationcs_qualifiers_setter(instance):
    original = instance.qualifiers
    instance.qualifiers = original
    assert instance.qualifiers == original

@given(instance=qvtoperational_cst_TransformationHeaderCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_transformationheadercs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_TransformationHeaderCS)

@given(instance=qvtoperational_cst_MappingExtensionCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_mappingextensioncs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_MappingExtensionCS)



@given(instance=qvtoperational_cst_MappingExtensionCS_strategy)
def test_qvtoperational_cst_mappingextensioncs_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=qvtoperational_cst_ClassifierDefCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_classifierdefcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ClassifierDefCS)

@given(instance=qvtoperational_cst_TransformationRefineCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_transformationrefinecs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_TransformationRefineCS)

@given(instance=qvtoperational_cst_TypeSpecCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_typespeccs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_TypeSpecCS)

@given(instance=qvtoperational_cst_ModuleKindCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_modulekindcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ModuleKindCS)



@given(instance=qvtoperational_cst_ModuleKindCS_strategy)
def test_qvtoperational_cst_modulekindcs_moduleKind_setter(instance):
    original = instance.moduleKind
    instance.moduleKind = original
    assert instance.moduleKind == original

@given(instance=qvtoperational_cst_ResolveOpArgsExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_resolveopargsexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ResolveOpArgsExpCS)

@given(instance=qvtoperational_cst_TagCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_tagcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_TagCS)

@given(instance=qvtoperational_cst_UnitCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_unitcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_UnitCS)

@given(instance=qvtoperational_cst_MappingSectionsCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_mappingsectionscs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_MappingSectionsCS)

@given(instance=qvtoperational_cst_ParameterDeclarationCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_parameterdeclarationcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ParameterDeclarationCS)



@given(instance=qvtoperational_cst_ParameterDeclarationCS_strategy)
def test_qvtoperational_cst_parameterdeclarationcs_directionKind_setter(instance):
    original = instance.directionKind
    instance.directionKind = original
    assert instance.directionKind == original

@given(instance=qvtoperational_cst_ImportCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_importcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ImportCS)

@given(instance=qvtoperational_cst_ModuleRefCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_modulerefcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ModuleRefCS)

@given(instance=qvtoperational_cst_OppositePropertyCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_oppositepropertycs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_OppositePropertyCS)



@given(instance=qvtoperational_cst_OppositePropertyCS_strategy)
def test_qvtoperational_cst_oppositepropertycs_isNavigable_setter(instance):
    original = instance.isNavigable
    instance.isNavigable = original
    assert instance.isNavigable == original

@given(instance=qvtoperational_cst_ModuleUsageCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_moduleusagecs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ModuleUsageCS)



@given(instance=qvtoperational_cst_ModuleUsageCS_strategy)
def test_qvtoperational_cst_moduleusagecs_importKind_setter(instance):
    original = instance.importKind
    instance.importKind = original
    assert instance.importKind == original

@given(instance=qvtoperational_cst_PackageRefCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_packagerefcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_PackageRefCS)

@given(instance=qvtoperational_cst_DictLiteralPartCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_dictliteralpartcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_DictLiteralPartCS)

@given(instance=qvtoperational_cst_DirectionKindCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_directionkindcs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_DirectionKindCS)



@given(instance=qvtoperational_cst_DirectionKindCS_strategy)
def test_qvtoperational_cst_directionkindcs_directionKind_setter(instance):
    original = instance.directionKind
    instance.directionKind = original
    assert instance.directionKind == original

@given(instance=qvtoperational_cst_ScopedNameCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_scopednamecs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_ScopedNameCS)



@given(instance=qvtoperational_cst_ScopedNameCS_strategy)
def test_qvtoperational_cst_scopednamecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=qvtoperational_cst_MappingModuleCS_strategy)
@settings(max_examples=50)
def test_qvtoperational_cst_mappingmodulecs_instantiation(instance):
    assert isinstance(instance, qvtoperational_cst_MappingModuleCS)
