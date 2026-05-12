import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    EmitStat,
    ACG_NewStat,
    ACG_SwapStat,
    ACG_NewinStat,
    ACG_DupX1Stat,
    ACG_DupStat,
    ACG_DeleteStat,
    ACG_LabelStat,
    StatementBlock,
    CompoundStat,
    ACG_OnceStat,
    ACG_OperationStat,
    ACG_LetStat,
    ACG_ConditionalStat,
    ACG_AnalyzeStat,
    ACG_VariableStat,
    ACG_ForEachStat,
    Statement,
    ACG_EmitStat,
    ACG_CompoundStat,
    ACG_ParamStat,
    ACG_ReportStat,
    ACG_FieldStat,
    Node,
    ACG_SimpleNode,
    ACG_CodeNode,
    CollectionExp,
    ACG_SequenceExp,
    LiteralExp,
    ACG_StringExp,
    ACG_IntegerExp,
    ACG_CollectionExp,
    ACG_BooleanExp,
    ACG_OclUndefinedExp,
    OperationCallExp,
    ACG_OperatorCallExp,
    PropertyCallExp,
    ACG_IteratorExp,
    ACG_OperationCallExp,
    ACG_NavigationExp,
    ACG_PopStat,
    EmitWithLabelRefStat,
    ACG_GotoStat,
    ACG_IfStat,
    LabelStat,
    ACG_EmitWithLabelRefStat,
    EmitWithOperandStat,
    ACG_LoadStat,
    ACG_PushDStat,
    ACG_PCallStat,
    ACG_CallStat,
    ACG_StoreStat,
    ACG_SetStat,
    ACG_SuperCallStat,
    ACG_PushIStat,
    ACG_GetStat,
    ACG_PushStat,
    ACG_EmitWithOperandStat,
    ACG_PushFStat,
    ACG_PushTStat,
    ACG_FindMEStat,
    ACG_GetAsmStat,
    ACG_EndIterateStat,
    ACG_IterateStat,
    ACG_ASMNode,
    VariableDecl,
    ACG_Parameter,
    Expression,
    ACG_SelfExp,
    ACG_LastExp,
    ACG_LetExp,
    ACG_IsAExp,
    ACG_VariableExp,
    ACG_IfExp,
    ACG_PropertyCallExp,
    ACG_LiteralExp,
    Parameter,
    ACG,
    ACGElement,
    ACG_Attribute,
    ACG_Node,
    ACG_Function,
    LocatedElement,
    ACG_VariableDecl,
    ACG_Statement,
    ACG_ACGElement,
    ACG_StatementBlock,
    ACG_Expression,
    ACG_ACG,
    ACG_LocatedElement,
    Severity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_emitstat_is_not_abstract():
    assert not inspect.isabstract(EmitStat)


def test_emitstat_constructor_exists():
    assert callable(EmitStat.__init__)


def test_emitstat_constructor_args():
    sig = inspect.signature(EmitStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_newstat_is_not_abstract():
    assert not inspect.isabstract(ACG_NewStat)


def test_acg_newstat_constructor_exists():
    assert callable(ACG_NewStat.__init__)


def test_acg_newstat_constructor_args():
    sig = inspect.signature(ACG_NewStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_swapstat_is_not_abstract():
    assert not inspect.isabstract(ACG_SwapStat)


def test_acg_swapstat_constructor_exists():
    assert callable(ACG_SwapStat.__init__)


def test_acg_swapstat_constructor_args():
    sig = inspect.signature(ACG_SwapStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_newinstat_is_not_abstract():
    assert not inspect.isabstract(ACG_NewinStat)


def test_acg_newinstat_constructor_exists():
    assert callable(ACG_NewinStat.__init__)


def test_acg_newinstat_constructor_args():
    sig = inspect.signature(ACG_NewinStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_dupx1stat_is_not_abstract():
    assert not inspect.isabstract(ACG_DupX1Stat)


def test_acg_dupx1stat_constructor_exists():
    assert callable(ACG_DupX1Stat.__init__)


def test_acg_dupx1stat_constructor_args():
    sig = inspect.signature(ACG_DupX1Stat.__init__)
    params = list(sig.parameters.keys())



def test_acg_dupstat_is_not_abstract():
    assert not inspect.isabstract(ACG_DupStat)


def test_acg_dupstat_constructor_exists():
    assert callable(ACG_DupStat.__init__)


def test_acg_dupstat_constructor_args():
    sig = inspect.signature(ACG_DupStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_deletestat_is_not_abstract():
    assert not inspect.isabstract(ACG_DeleteStat)


def test_acg_deletestat_constructor_exists():
    assert callable(ACG_DeleteStat.__init__)


def test_acg_deletestat_constructor_args():
    sig = inspect.signature(ACG_DeleteStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_labelstat_is_not_abstract():
    assert not inspect.isabstract(ACG_LabelStat)


def test_acg_labelstat_constructor_exists():
    assert callable(ACG_LabelStat.__init__)


def test_acg_labelstat_constructor_args():
    sig = inspect.signature(ACG_LabelStat.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_acg_labelstat_has_name():
    assert hasattr(ACG_LabelStat, "name")
    descriptor = None
    for klass in ACG_LabelStat.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statementblock_is_not_abstract():
    assert not inspect.isabstract(StatementBlock)


def test_statementblock_constructor_exists():
    assert callable(StatementBlock.__init__)


def test_statementblock_constructor_args():
    sig = inspect.signature(StatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_compoundstat_is_not_abstract():
    assert not inspect.isabstract(CompoundStat)


def test_compoundstat_constructor_exists():
    assert callable(CompoundStat.__init__)


def test_compoundstat_constructor_args():
    sig = inspect.signature(CompoundStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_oncestat_is_not_abstract():
    assert not inspect.isabstract(ACG_OnceStat)


def test_acg_oncestat_constructor_exists():
    assert callable(ACG_OnceStat.__init__)


def test_acg_oncestat_constructor_args():
    sig = inspect.signature(ACG_OnceStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_operationstat_is_not_abstract():
    assert not inspect.isabstract(ACG_OperationStat)


def test_acg_operationstat_constructor_exists():
    assert callable(ACG_OperationStat.__init__)


def test_acg_operationstat_constructor_args():
    sig = inspect.signature(ACG_OperationStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_letstat_is_not_abstract():
    assert not inspect.isabstract(ACG_LetStat)


def test_acg_letstat_constructor_exists():
    assert callable(ACG_LetStat.__init__)


def test_acg_letstat_constructor_args():
    sig = inspect.signature(ACG_LetStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_conditionalstat_is_not_abstract():
    assert not inspect.isabstract(ACG_ConditionalStat)


def test_acg_conditionalstat_constructor_exists():
    assert callable(ACG_ConditionalStat.__init__)


def test_acg_conditionalstat_constructor_args():
    sig = inspect.signature(ACG_ConditionalStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_analyzestat_is_not_abstract():
    assert not inspect.isabstract(ACG_AnalyzeStat)


def test_acg_analyzestat_constructor_exists():
    assert callable(ACG_AnalyzeStat.__init__)


def test_acg_analyzestat_constructor_args():
    sig = inspect.signature(ACG_AnalyzeStat.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_acg_analyzestat_has_mode():
    assert hasattr(ACG_AnalyzeStat, "mode")
    descriptor = None
    for klass in ACG_AnalyzeStat.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_acg_variablestat_is_not_abstract():
    assert not inspect.isabstract(ACG_VariableStat)


def test_acg_variablestat_constructor_exists():
    assert callable(ACG_VariableStat.__init__)


def test_acg_variablestat_constructor_args():
    sig = inspect.signature(ACG_VariableStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_foreachstat_is_not_abstract():
    assert not inspect.isabstract(ACG_ForEachStat)


def test_acg_foreachstat_constructor_exists():
    assert callable(ACG_ForEachStat.__init__)


def test_acg_foreachstat_constructor_args():
    sig = inspect.signature(ACG_ForEachStat.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_acg_emitstat_is_not_abstract():
    assert not inspect.isabstract(ACG_EmitStat)


def test_acg_emitstat_constructor_exists():
    assert callable(ACG_EmitStat.__init__)


def test_acg_emitstat_constructor_args():
    sig = inspect.signature(ACG_EmitStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_compoundstat_is_not_abstract():
    assert not inspect.isabstract(ACG_CompoundStat)


def test_acg_compoundstat_constructor_exists():
    assert callable(ACG_CompoundStat.__init__)


def test_acg_compoundstat_constructor_args():
    sig = inspect.signature(ACG_CompoundStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_paramstat_is_not_abstract():
    assert not inspect.isabstract(ACG_ParamStat)


def test_acg_paramstat_constructor_exists():
    assert callable(ACG_ParamStat.__init__)


def test_acg_paramstat_constructor_args():
    sig = inspect.signature(ACG_ParamStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_reportstat_is_not_abstract():
    assert not inspect.isabstract(ACG_ReportStat)


def test_acg_reportstat_constructor_exists():
    assert callable(ACG_ReportStat.__init__)


def test_acg_reportstat_constructor_args():
    sig = inspect.signature(ACG_ReportStat.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_acg_reportstat_has_severity():
    assert hasattr(ACG_ReportStat, "severity")
    descriptor = None
    for klass in ACG_ReportStat.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_acg_fieldstat_is_not_abstract():
    assert not inspect.isabstract(ACG_FieldStat)


def test_acg_fieldstat_constructor_exists():
    assert callable(ACG_FieldStat.__init__)


def test_acg_fieldstat_constructor_args():
    sig = inspect.signature(ACG_FieldStat.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_acg_simplenode_is_not_abstract():
    assert not inspect.isabstract(ACG_SimpleNode)


def test_acg_simplenode_constructor_exists():
    assert callable(ACG_SimpleNode.__init__)


def test_acg_simplenode_constructor_args():
    sig = inspect.signature(ACG_SimpleNode.__init__)
    params = list(sig.parameters.keys())



def test_acg_codenode_is_not_abstract():
    assert not inspect.isabstract(ACG_CodeNode)


def test_acg_codenode_constructor_exists():
    assert callable(ACG_CodeNode.__init__)


def test_acg_codenode_constructor_args():
    sig = inspect.signature(ACG_CodeNode.__init__)
    params = list(sig.parameters.keys())



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_acg_sequenceexp_is_not_abstract():
    assert not inspect.isabstract(ACG_SequenceExp)


def test_acg_sequenceexp_constructor_exists():
    assert callable(ACG_SequenceExp.__init__)


def test_acg_sequenceexp_constructor_args():
    sig = inspect.signature(ACG_SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_acg_stringexp_is_not_abstract():
    assert not inspect.isabstract(ACG_StringExp)


def test_acg_stringexp_constructor_exists():
    assert callable(ACG_StringExp.__init__)


def test_acg_stringexp_constructor_args():
    sig = inspect.signature(ACG_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_acg_stringexp_has_value():
    assert hasattr(ACG_StringExp, "value")
    descriptor = None
    for klass in ACG_StringExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_acg_integerexp_is_not_abstract():
    assert not inspect.isabstract(ACG_IntegerExp)


def test_acg_integerexp_constructor_exists():
    assert callable(ACG_IntegerExp.__init__)


def test_acg_integerexp_constructor_args():
    sig = inspect.signature(ACG_IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_acg_integerexp_has_value():
    assert hasattr(ACG_IntegerExp, "value")
    descriptor = None
    for klass in ACG_IntegerExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_acg_collectionexp_is_not_abstract():
    assert not inspect.isabstract(ACG_CollectionExp)


def test_acg_collectionexp_constructor_exists():
    assert callable(ACG_CollectionExp.__init__)


def test_acg_collectionexp_constructor_args():
    sig = inspect.signature(ACG_CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_acg_booleanexp_is_not_abstract():
    assert not inspect.isabstract(ACG_BooleanExp)


def test_acg_booleanexp_constructor_exists():
    assert callable(ACG_BooleanExp.__init__)


def test_acg_booleanexp_constructor_args():
    sig = inspect.signature(ACG_BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_acg_booleanexp_has_value():
    assert hasattr(ACG_BooleanExp, "value")
    descriptor = None
    for klass in ACG_BooleanExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_acg_oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(ACG_OclUndefinedExp)


def test_acg_oclundefinedexp_constructor_exists():
    assert callable(ACG_OclUndefinedExp.__init__)


def test_acg_oclundefinedexp_constructor_args():
    sig = inspect.signature(ACG_OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_acg_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(ACG_OperatorCallExp)


def test_acg_operatorcallexp_constructor_exists():
    assert callable(ACG_OperatorCallExp.__init__)


def test_acg_operatorcallexp_constructor_args():
    sig = inspect.signature(ACG_OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_acg_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(ACG_IteratorExp)


def test_acg_iteratorexp_constructor_exists():
    assert callable(ACG_IteratorExp.__init__)


def test_acg_iteratorexp_constructor_args():
    sig = inspect.signature(ACG_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_acg_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(ACG_OperationCallExp)


def test_acg_operationcallexp_constructor_exists():
    assert callable(ACG_OperationCallExp.__init__)


def test_acg_operationcallexp_constructor_args():
    sig = inspect.signature(ACG_OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_acg_navigationexp_is_not_abstract():
    assert not inspect.isabstract(ACG_NavigationExp)


def test_acg_navigationexp_constructor_exists():
    assert callable(ACG_NavigationExp.__init__)


def test_acg_navigationexp_constructor_args():
    sig = inspect.signature(ACG_NavigationExp.__init__)
    params = list(sig.parameters.keys())



def test_acg_popstat_is_not_abstract():
    assert not inspect.isabstract(ACG_PopStat)


def test_acg_popstat_constructor_exists():
    assert callable(ACG_PopStat.__init__)


def test_acg_popstat_constructor_args():
    sig = inspect.signature(ACG_PopStat.__init__)
    params = list(sig.parameters.keys())



def test_emitwithlabelrefstat_is_not_abstract():
    assert not inspect.isabstract(EmitWithLabelRefStat)


def test_emitwithlabelrefstat_constructor_exists():
    assert callable(EmitWithLabelRefStat.__init__)


def test_emitwithlabelrefstat_constructor_args():
    sig = inspect.signature(EmitWithLabelRefStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_gotostat_is_not_abstract():
    assert not inspect.isabstract(ACG_GotoStat)


def test_acg_gotostat_constructor_exists():
    assert callable(ACG_GotoStat.__init__)


def test_acg_gotostat_constructor_args():
    sig = inspect.signature(ACG_GotoStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_ifstat_is_not_abstract():
    assert not inspect.isabstract(ACG_IfStat)


def test_acg_ifstat_constructor_exists():
    assert callable(ACG_IfStat.__init__)


def test_acg_ifstat_constructor_args():
    sig = inspect.signature(ACG_IfStat.__init__)
    params = list(sig.parameters.keys())



def test_labelstat_is_not_abstract():
    assert not inspect.isabstract(LabelStat)


def test_labelstat_constructor_exists():
    assert callable(LabelStat.__init__)


def test_labelstat_constructor_args():
    sig = inspect.signature(LabelStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_emitwithlabelrefstat_is_not_abstract():
    assert not inspect.isabstract(ACG_EmitWithLabelRefStat)


def test_acg_emitwithlabelrefstat_constructor_exists():
    assert callable(ACG_EmitWithLabelRefStat.__init__)


def test_acg_emitwithlabelrefstat_constructor_args():
    sig = inspect.signature(ACG_EmitWithLabelRefStat.__init__)
    params = list(sig.parameters.keys())



def test_emitwithoperandstat_is_not_abstract():
    assert not inspect.isabstract(EmitWithOperandStat)


def test_emitwithoperandstat_constructor_exists():
    assert callable(EmitWithOperandStat.__init__)


def test_emitwithoperandstat_constructor_args():
    sig = inspect.signature(EmitWithOperandStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_loadstat_is_not_abstract():
    assert not inspect.isabstract(ACG_LoadStat)


def test_acg_loadstat_constructor_exists():
    assert callable(ACG_LoadStat.__init__)


def test_acg_loadstat_constructor_args():
    sig = inspect.signature(ACG_LoadStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_pushdstat_is_not_abstract():
    assert not inspect.isabstract(ACG_PushDStat)


def test_acg_pushdstat_constructor_exists():
    assert callable(ACG_PushDStat.__init__)


def test_acg_pushdstat_constructor_args():
    sig = inspect.signature(ACG_PushDStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_pcallstat_is_not_abstract():
    assert not inspect.isabstract(ACG_PCallStat)


def test_acg_pcallstat_constructor_exists():
    assert callable(ACG_PCallStat.__init__)


def test_acg_pcallstat_constructor_args():
    sig = inspect.signature(ACG_PCallStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_callstat_is_not_abstract():
    assert not inspect.isabstract(ACG_CallStat)


def test_acg_callstat_constructor_exists():
    assert callable(ACG_CallStat.__init__)


def test_acg_callstat_constructor_args():
    sig = inspect.signature(ACG_CallStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_storestat_is_not_abstract():
    assert not inspect.isabstract(ACG_StoreStat)


def test_acg_storestat_constructor_exists():
    assert callable(ACG_StoreStat.__init__)


def test_acg_storestat_constructor_args():
    sig = inspect.signature(ACG_StoreStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_setstat_is_not_abstract():
    assert not inspect.isabstract(ACG_SetStat)


def test_acg_setstat_constructor_exists():
    assert callable(ACG_SetStat.__init__)


def test_acg_setstat_constructor_args():
    sig = inspect.signature(ACG_SetStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_supercallstat_is_not_abstract():
    assert not inspect.isabstract(ACG_SuperCallStat)


def test_acg_supercallstat_constructor_exists():
    assert callable(ACG_SuperCallStat.__init__)


def test_acg_supercallstat_constructor_args():
    sig = inspect.signature(ACG_SuperCallStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_pushistat_is_not_abstract():
    assert not inspect.isabstract(ACG_PushIStat)


def test_acg_pushistat_constructor_exists():
    assert callable(ACG_PushIStat.__init__)


def test_acg_pushistat_constructor_args():
    sig = inspect.signature(ACG_PushIStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_getstat_is_not_abstract():
    assert not inspect.isabstract(ACG_GetStat)


def test_acg_getstat_constructor_exists():
    assert callable(ACG_GetStat.__init__)


def test_acg_getstat_constructor_args():
    sig = inspect.signature(ACG_GetStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_pushstat_is_not_abstract():
    assert not inspect.isabstract(ACG_PushStat)


def test_acg_pushstat_constructor_exists():
    assert callable(ACG_PushStat.__init__)


def test_acg_pushstat_constructor_args():
    sig = inspect.signature(ACG_PushStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_emitwithoperandstat_is_not_abstract():
    assert not inspect.isabstract(ACG_EmitWithOperandStat)


def test_acg_emitwithoperandstat_constructor_exists():
    assert callable(ACG_EmitWithOperandStat.__init__)


def test_acg_emitwithoperandstat_constructor_args():
    sig = inspect.signature(ACG_EmitWithOperandStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_pushfstat_is_not_abstract():
    assert not inspect.isabstract(ACG_PushFStat)


def test_acg_pushfstat_constructor_exists():
    assert callable(ACG_PushFStat.__init__)


def test_acg_pushfstat_constructor_args():
    sig = inspect.signature(ACG_PushFStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_pushtstat_is_not_abstract():
    assert not inspect.isabstract(ACG_PushTStat)


def test_acg_pushtstat_constructor_exists():
    assert callable(ACG_PushTStat.__init__)


def test_acg_pushtstat_constructor_args():
    sig = inspect.signature(ACG_PushTStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_findmestat_is_not_abstract():
    assert not inspect.isabstract(ACG_FindMEStat)


def test_acg_findmestat_constructor_exists():
    assert callable(ACG_FindMEStat.__init__)


def test_acg_findmestat_constructor_args():
    sig = inspect.signature(ACG_FindMEStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_getasmstat_is_not_abstract():
    assert not inspect.isabstract(ACG_GetAsmStat)


def test_acg_getasmstat_constructor_exists():
    assert callable(ACG_GetAsmStat.__init__)


def test_acg_getasmstat_constructor_args():
    sig = inspect.signature(ACG_GetAsmStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_enditeratestat_is_not_abstract():
    assert not inspect.isabstract(ACG_EndIterateStat)


def test_acg_enditeratestat_constructor_exists():
    assert callable(ACG_EndIterateStat.__init__)


def test_acg_enditeratestat_constructor_args():
    sig = inspect.signature(ACG_EndIterateStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_iteratestat_is_not_abstract():
    assert not inspect.isabstract(ACG_IterateStat)


def test_acg_iteratestat_constructor_exists():
    assert callable(ACG_IterateStat.__init__)


def test_acg_iteratestat_constructor_args():
    sig = inspect.signature(ACG_IterateStat.__init__)
    params = list(sig.parameters.keys())



def test_acg_asmnode_is_not_abstract():
    assert not inspect.isabstract(ACG_ASMNode)


def test_acg_asmnode_constructor_exists():
    assert callable(ACG_ASMNode.__init__)


def test_acg_asmnode_constructor_args():
    sig = inspect.signature(ACG_ASMNode.__init__)
    params = list(sig.parameters.keys())



def test_variabledecl_is_not_abstract():
    assert not inspect.isabstract(VariableDecl)


def test_variabledecl_constructor_exists():
    assert callable(VariableDecl.__init__)


def test_variabledecl_constructor_args():
    sig = inspect.signature(VariableDecl.__init__)
    params = list(sig.parameters.keys())



def test_acg_parameter_is_not_abstract():
    assert not inspect.isabstract(ACG_Parameter)


def test_acg_parameter_constructor_exists():
    assert callable(ACG_Parameter.__init__)


def test_acg_parameter_constructor_args():
    sig = inspect.signature(ACG_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_acg_selfexp_is_not_abstract():
    assert not inspect.isabstract(ACG_SelfExp)


def test_acg_selfexp_constructor_exists():
    assert callable(ACG_SelfExp.__init__)


def test_acg_selfexp_constructor_args():
    sig = inspect.signature(ACG_SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_acg_lastexp_is_not_abstract():
    assert not inspect.isabstract(ACG_LastExp)


def test_acg_lastexp_constructor_exists():
    assert callable(ACG_LastExp.__init__)


def test_acg_lastexp_constructor_args():
    sig = inspect.signature(ACG_LastExp.__init__)
    params = list(sig.parameters.keys())



def test_acg_letexp_is_not_abstract():
    assert not inspect.isabstract(ACG_LetExp)


def test_acg_letexp_constructor_exists():
    assert callable(ACG_LetExp.__init__)


def test_acg_letexp_constructor_args():
    sig = inspect.signature(ACG_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_acg_isaexp_is_not_abstract():
    assert not inspect.isabstract(ACG_IsAExp)


def test_acg_isaexp_constructor_exists():
    assert callable(ACG_IsAExp.__init__)


def test_acg_isaexp_constructor_args():
    sig = inspect.signature(ACG_IsAExp.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_acg_isaexp_has_type():
    assert hasattr(ACG_IsAExp, "type")
    descriptor = None
    for klass in ACG_IsAExp.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_acg_variableexp_is_not_abstract():
    assert not inspect.isabstract(ACG_VariableExp)


def test_acg_variableexp_constructor_exists():
    assert callable(ACG_VariableExp.__init__)


def test_acg_variableexp_constructor_args():
    sig = inspect.signature(ACG_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_acg_ifexp_is_not_abstract():
    assert not inspect.isabstract(ACG_IfExp)


def test_acg_ifexp_constructor_exists():
    assert callable(ACG_IfExp.__init__)


def test_acg_ifexp_constructor_args():
    sig = inspect.signature(ACG_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_acg_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(ACG_PropertyCallExp)


def test_acg_propertycallexp_constructor_exists():
    assert callable(ACG_PropertyCallExp.__init__)


def test_acg_propertycallexp_constructor_args():
    sig = inspect.signature(ACG_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_acg_propertycallexp_has_name():
    assert hasattr(ACG_PropertyCallExp, "name")
    descriptor = None
    for klass in ACG_PropertyCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_acg_literalexp_is_not_abstract():
    assert not inspect.isabstract(ACG_LiteralExp)


def test_acg_literalexp_constructor_exists():
    assert callable(ACG_LiteralExp.__init__)


def test_acg_literalexp_constructor_args():
    sig = inspect.signature(ACG_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_acg_is_not_abstract():
    assert not inspect.isabstract(ACG)


def test_acg_constructor_exists():
    assert callable(ACG.__init__)


def test_acg_constructor_args():
    sig = inspect.signature(ACG.__init__)
    params = list(sig.parameters.keys())



def test_acgelement_is_not_abstract():
    assert not inspect.isabstract(ACGElement)


def test_acgelement_constructor_exists():
    assert callable(ACGElement.__init__)


def test_acgelement_constructor_args():
    sig = inspect.signature(ACGElement.__init__)
    params = list(sig.parameters.keys())



def test_acg_attribute_is_not_abstract():
    assert not inspect.isabstract(ACG_Attribute)


def test_acg_attribute_constructor_exists():
    assert callable(ACG_Attribute.__init__)


def test_acg_attribute_constructor_args():
    sig = inspect.signature(ACG_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "context" in params, "Missing parameter 'context'"

def test_acg_attribute_has_name():
    assert hasattr(ACG_Attribute, "name")
    descriptor = None
    for klass in ACG_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_acg_attribute_has_context():
    assert hasattr(ACG_Attribute, "context")
    descriptor = None
    for klass in ACG_Attribute.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



def test_acg_node_is_not_abstract():
    assert not inspect.isabstract(ACG_Node)


def test_acg_node_constructor_exists():
    assert callable(ACG_Node.__init__)


def test_acg_node_constructor_args():
    sig = inspect.signature(ACG_Node.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"
    assert "element" in params, "Missing parameter 'element'"

def test_acg_node_has_mode():
    assert hasattr(ACG_Node, "mode")
    descriptor = None
    for klass in ACG_Node.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_acg_node_has_element():
    assert hasattr(ACG_Node, "element")
    descriptor = None
    for klass in ACG_Node.__mro__:
        if "element" in klass.__dict__:
            descriptor = klass.__dict__["element"]
            break
    assert isinstance(descriptor, property)



def test_acg_function_is_not_abstract():
    assert not inspect.isabstract(ACG_Function)


def test_acg_function_constructor_exists():
    assert callable(ACG_Function.__init__)


def test_acg_function_constructor_args():
    sig = inspect.signature(ACG_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "context" in params, "Missing parameter 'context'"

def test_acg_function_has_name():
    assert hasattr(ACG_Function, "name")
    descriptor = None
    for klass in ACG_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_acg_function_has_context():
    assert hasattr(ACG_Function, "context")
    descriptor = None
    for klass in ACG_Function.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_acg_variabledecl_is_not_abstract():
    assert not inspect.isabstract(ACG_VariableDecl)


def test_acg_variabledecl_constructor_exists():
    assert callable(ACG_VariableDecl.__init__)


def test_acg_variabledecl_constructor_args():
    sig = inspect.signature(ACG_VariableDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_acg_variabledecl_has_name():
    assert hasattr(ACG_VariableDecl, "name")
    descriptor = None
    for klass in ACG_VariableDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_acg_statement_is_not_abstract():
    assert not inspect.isabstract(ACG_Statement)


def test_acg_statement_constructor_exists():
    assert callable(ACG_Statement.__init__)


def test_acg_statement_constructor_args():
    sig = inspect.signature(ACG_Statement.__init__)
    params = list(sig.parameters.keys())



def test_acg_acgelement_is_not_abstract():
    assert not inspect.isabstract(ACG_ACGElement)


def test_acg_acgelement_constructor_exists():
    assert callable(ACG_ACGElement.__init__)


def test_acg_acgelement_constructor_args():
    sig = inspect.signature(ACG_ACGElement.__init__)
    params = list(sig.parameters.keys())



def test_acg_statementblock_is_not_abstract():
    assert not inspect.isabstract(ACG_StatementBlock)


def test_acg_statementblock_constructor_exists():
    assert callable(ACG_StatementBlock.__init__)


def test_acg_statementblock_constructor_args():
    sig = inspect.signature(ACG_StatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_acg_expression_is_not_abstract():
    assert not inspect.isabstract(ACG_Expression)


def test_acg_expression_constructor_exists():
    assert callable(ACG_Expression.__init__)


def test_acg_expression_constructor_args():
    sig = inspect.signature(ACG_Expression.__init__)
    params = list(sig.parameters.keys())



def test_acg_acg_is_not_abstract():
    assert not inspect.isabstract(ACG_ACG)


def test_acg_acg_constructor_exists():
    assert callable(ACG_ACG.__init__)


def test_acg_acg_constructor_args():
    sig = inspect.signature(ACG_ACG.__init__)
    params = list(sig.parameters.keys())
    assert "metamodel" in params, "Missing parameter 'metamodel'"
    assert "startsWith" in params, "Missing parameter 'startsWith'"

def test_acg_acg_has_metamodel():
    assert hasattr(ACG_ACG, "metamodel")
    descriptor = None
    for klass in ACG_ACG.__mro__:
        if "metamodel" in klass.__dict__:
            descriptor = klass.__dict__["metamodel"]
            break
    assert isinstance(descriptor, property)

def test_acg_acg_has_startsWith():
    assert hasattr(ACG_ACG, "startsWith")
    descriptor = None
    for klass in ACG_ACG.__mro__:
        if "startsWith" in klass.__dict__:
            descriptor = klass.__dict__["startsWith"]
            break
    assert isinstance(descriptor, property)



def test_acg_locatedelement_is_not_abstract():
    assert not inspect.isabstract(ACG_LocatedElement)


def test_acg_locatedelement_constructor_exists():
    assert callable(ACG_LocatedElement.__init__)


def test_acg_locatedelement_constructor_args():
    sig = inspect.signature(ACG_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"

def test_acg_locatedelement_has_commentsBefore():
    assert hasattr(ACG_LocatedElement, "commentsBefore")
    descriptor = None
    for klass in ACG_LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_acg_locatedelement_has_location():
    assert hasattr(ACG_LocatedElement, "location")
    descriptor = None
    for klass in ACG_LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_acg_locatedelement_has_commentsAfter():
    assert hasattr(ACG_LocatedElement, "commentsAfter")
    descriptor = None
    for klass in ACG_LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_severity_exists():
    # Check that the Enumeration exists
    assert Severity is not None

def test_severity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Severity]
    expected_literals = [
        "critic",
        "error",
        "warning",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Severity"


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
EmitStat_strategy = st.builds(
    EmitStat,
)
ACG_NewStat_strategy = st.builds(
    ACG_NewStat,
)
ACG_SwapStat_strategy = st.builds(
    ACG_SwapStat,
)
ACG_NewinStat_strategy = st.builds(
    ACG_NewinStat,
)
ACG_DupX1Stat_strategy = st.builds(
    ACG_DupX1Stat,
)
ACG_DupStat_strategy = st.builds(
    ACG_DupStat,
)
ACG_DeleteStat_strategy = st.builds(
    ACG_DeleteStat,
)
ACG_LabelStat_strategy = st.builds(
    ACG_LabelStat,
    name=
        safe_text
)
StatementBlock_strategy = st.builds(
    StatementBlock,
)
CompoundStat_strategy = st.builds(
    CompoundStat,
)
ACG_OnceStat_strategy = st.builds(
    ACG_OnceStat,
)
ACG_OperationStat_strategy = st.builds(
    ACG_OperationStat,
)
ACG_LetStat_strategy = st.builds(
    ACG_LetStat,
)
ACG_ConditionalStat_strategy = st.builds(
    ACG_ConditionalStat,
)
ACG_AnalyzeStat_strategy = st.builds(
    ACG_AnalyzeStat,
    mode=
        safe_text
)
ACG_VariableStat_strategy = st.builds(
    ACG_VariableStat,
)
ACG_ForEachStat_strategy = st.builds(
    ACG_ForEachStat,
)
Statement_strategy = st.builds(
    Statement,
)
ACG_EmitStat_strategy = st.builds(
    ACG_EmitStat,
)
ACG_CompoundStat_strategy = st.builds(
    ACG_CompoundStat,
)
ACG_ParamStat_strategy = st.builds(
    ACG_ParamStat,
)
ACG_ReportStat_strategy = st.builds(
    ACG_ReportStat,
    severity=
        safe_text
)
ACG_FieldStat_strategy = st.builds(
    ACG_FieldStat,
)
Node_strategy = st.builds(
    Node,
)
ACG_SimpleNode_strategy = st.builds(
    ACG_SimpleNode,
)
ACG_CodeNode_strategy = st.builds(
    ACG_CodeNode,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
ACG_SequenceExp_strategy = st.builds(
    ACG_SequenceExp,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
ACG_StringExp_strategy = st.builds(
    ACG_StringExp,
    value=
        safe_text
)
ACG_IntegerExp_strategy = st.builds(
    ACG_IntegerExp,
    value=
        safe_text
)
ACG_CollectionExp_strategy = st.builds(
    ACG_CollectionExp,
)
ACG_BooleanExp_strategy = st.builds(
    ACG_BooleanExp,
    value=
        safe_text
)
ACG_OclUndefinedExp_strategy = st.builds(
    ACG_OclUndefinedExp,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
ACG_OperatorCallExp_strategy = st.builds(
    ACG_OperatorCallExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
ACG_IteratorExp_strategy = st.builds(
    ACG_IteratorExp,
)
ACG_OperationCallExp_strategy = st.builds(
    ACG_OperationCallExp,
)
ACG_NavigationExp_strategy = st.builds(
    ACG_NavigationExp,
)
ACG_PopStat_strategy = st.builds(
    ACG_PopStat,
)
EmitWithLabelRefStat_strategy = st.builds(
    EmitWithLabelRefStat,
)
ACG_GotoStat_strategy = st.builds(
    ACG_GotoStat,
)
ACG_IfStat_strategy = st.builds(
    ACG_IfStat,
)
LabelStat_strategy = st.builds(
    LabelStat,
)
ACG_EmitWithLabelRefStat_strategy = st.builds(
    ACG_EmitWithLabelRefStat,
)
EmitWithOperandStat_strategy = st.builds(
    EmitWithOperandStat,
)
ACG_LoadStat_strategy = st.builds(
    ACG_LoadStat,
)
ACG_PushDStat_strategy = st.builds(
    ACG_PushDStat,
)
ACG_PCallStat_strategy = st.builds(
    ACG_PCallStat,
)
ACG_CallStat_strategy = st.builds(
    ACG_CallStat,
)
ACG_StoreStat_strategy = st.builds(
    ACG_StoreStat,
)
ACG_SetStat_strategy = st.builds(
    ACG_SetStat,
)
ACG_SuperCallStat_strategy = st.builds(
    ACG_SuperCallStat,
)
ACG_PushIStat_strategy = st.builds(
    ACG_PushIStat,
)
ACG_GetStat_strategy = st.builds(
    ACG_GetStat,
)
ACG_PushStat_strategy = st.builds(
    ACG_PushStat,
)
ACG_EmitWithOperandStat_strategy = st.builds(
    ACG_EmitWithOperandStat,
)
ACG_PushFStat_strategy = st.builds(
    ACG_PushFStat,
)
ACG_PushTStat_strategy = st.builds(
    ACG_PushTStat,
)
ACG_FindMEStat_strategy = st.builds(
    ACG_FindMEStat,
)
ACG_GetAsmStat_strategy = st.builds(
    ACG_GetAsmStat,
)
ACG_EndIterateStat_strategy = st.builds(
    ACG_EndIterateStat,
)
ACG_IterateStat_strategy = st.builds(
    ACG_IterateStat,
)
ACG_ASMNode_strategy = st.builds(
    ACG_ASMNode,
)
VariableDecl_strategy = st.builds(
    VariableDecl,
)
ACG_Parameter_strategy = st.builds(
    ACG_Parameter,
)
Expression_strategy = st.builds(
    Expression,
)
ACG_SelfExp_strategy = st.builds(
    ACG_SelfExp,
)
ACG_LastExp_strategy = st.builds(
    ACG_LastExp,
)
ACG_LetExp_strategy = st.builds(
    ACG_LetExp,
)
ACG_IsAExp_strategy = st.builds(
    ACG_IsAExp,
    type=
        safe_text
)
ACG_VariableExp_strategy = st.builds(
    ACG_VariableExp,
)
ACG_IfExp_strategy = st.builds(
    ACG_IfExp,
)
ACG_PropertyCallExp_strategy = st.builds(
    ACG_PropertyCallExp,
    name=
        safe_text
)
ACG_LiteralExp_strategy = st.builds(
    ACG_LiteralExp,
)
Parameter_strategy = st.builds(
    Parameter,
)
ACG_strategy = st.builds(
    ACG,
)
ACGElement_strategy = st.builds(
    ACGElement,
)
ACG_Attribute_strategy = st.builds(
    ACG_Attribute,
    name=
        safe_text,
    context=
        safe_text
)
ACG_Node_strategy = st.builds(
    ACG_Node,
    mode=
        safe_text,
    element=
        safe_text
)
ACG_Function_strategy = st.builds(
    ACG_Function,
    name=
        safe_text,
    context=
        safe_text
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
ACG_VariableDecl_strategy = st.builds(
    ACG_VariableDecl,
    name=
        safe_text
)
ACG_Statement_strategy = st.builds(
    ACG_Statement,
)
ACG_ACGElement_strategy = st.builds(
    ACG_ACGElement,
)
ACG_StatementBlock_strategy = st.builds(
    ACG_StatementBlock,
)
ACG_Expression_strategy = st.builds(
    ACG_Expression,
)
ACG_ACG_strategy = st.builds(
    ACG_ACG,
    metamodel=
        safe_text,
    startsWith=
        safe_text
)
ACG_LocatedElement_strategy = st.builds(
    ACG_LocatedElement,
    commentsBefore=
        safe_text,
    location=
        safe_text,
    commentsAfter=
        safe_text
)

@given(instance=EmitStat_strategy)
@settings(max_examples=50)
def test_emitstat_instantiation(instance):
    assert isinstance(instance, EmitStat)

@given(instance=ACG_NewStat_strategy)
@settings(max_examples=50)
def test_acg_newstat_instantiation(instance):
    assert isinstance(instance, ACG_NewStat)

@given(instance=ACG_SwapStat_strategy)
@settings(max_examples=50)
def test_acg_swapstat_instantiation(instance):
    assert isinstance(instance, ACG_SwapStat)

@given(instance=ACG_NewinStat_strategy)
@settings(max_examples=50)
def test_acg_newinstat_instantiation(instance):
    assert isinstance(instance, ACG_NewinStat)

@given(instance=ACG_DupX1Stat_strategy)
@settings(max_examples=50)
def test_acg_dupx1stat_instantiation(instance):
    assert isinstance(instance, ACG_DupX1Stat)

@given(instance=ACG_DupStat_strategy)
@settings(max_examples=50)
def test_acg_dupstat_instantiation(instance):
    assert isinstance(instance, ACG_DupStat)

@given(instance=ACG_DeleteStat_strategy)
@settings(max_examples=50)
def test_acg_deletestat_instantiation(instance):
    assert isinstance(instance, ACG_DeleteStat)

@given(instance=ACG_LabelStat_strategy)
@settings(max_examples=50)
def test_acg_labelstat_instantiation(instance):
    assert isinstance(instance, ACG_LabelStat)



@given(instance=ACG_LabelStat_strategy)
def test_acg_labelstat_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StatementBlock_strategy)
@settings(max_examples=50)
def test_statementblock_instantiation(instance):
    assert isinstance(instance, StatementBlock)

@given(instance=CompoundStat_strategy)
@settings(max_examples=50)
def test_compoundstat_instantiation(instance):
    assert isinstance(instance, CompoundStat)

@given(instance=ACG_OnceStat_strategy)
@settings(max_examples=50)
def test_acg_oncestat_instantiation(instance):
    assert isinstance(instance, ACG_OnceStat)

@given(instance=ACG_OperationStat_strategy)
@settings(max_examples=50)
def test_acg_operationstat_instantiation(instance):
    assert isinstance(instance, ACG_OperationStat)

@given(instance=ACG_LetStat_strategy)
@settings(max_examples=50)
def test_acg_letstat_instantiation(instance):
    assert isinstance(instance, ACG_LetStat)

@given(instance=ACG_ConditionalStat_strategy)
@settings(max_examples=50)
def test_acg_conditionalstat_instantiation(instance):
    assert isinstance(instance, ACG_ConditionalStat)

@given(instance=ACG_AnalyzeStat_strategy)
@settings(max_examples=50)
def test_acg_analyzestat_instantiation(instance):
    assert isinstance(instance, ACG_AnalyzeStat)



@given(instance=ACG_AnalyzeStat_strategy)
def test_acg_analyzestat_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=ACG_VariableStat_strategy)
@settings(max_examples=50)
def test_acg_variablestat_instantiation(instance):
    assert isinstance(instance, ACG_VariableStat)

@given(instance=ACG_ForEachStat_strategy)
@settings(max_examples=50)
def test_acg_foreachstat_instantiation(instance):
    assert isinstance(instance, ACG_ForEachStat)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=ACG_EmitStat_strategy)
@settings(max_examples=50)
def test_acg_emitstat_instantiation(instance):
    assert isinstance(instance, ACG_EmitStat)

@given(instance=ACG_CompoundStat_strategy)
@settings(max_examples=50)
def test_acg_compoundstat_instantiation(instance):
    assert isinstance(instance, ACG_CompoundStat)

@given(instance=ACG_ParamStat_strategy)
@settings(max_examples=50)
def test_acg_paramstat_instantiation(instance):
    assert isinstance(instance, ACG_ParamStat)

@given(instance=ACG_ReportStat_strategy)
@settings(max_examples=50)
def test_acg_reportstat_instantiation(instance):
    assert isinstance(instance, ACG_ReportStat)



@given(instance=ACG_ReportStat_strategy)
def test_acg_reportstat_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=ACG_FieldStat_strategy)
@settings(max_examples=50)
def test_acg_fieldstat_instantiation(instance):
    assert isinstance(instance, ACG_FieldStat)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=ACG_SimpleNode_strategy)
@settings(max_examples=50)
def test_acg_simplenode_instantiation(instance):
    assert isinstance(instance, ACG_SimpleNode)

@given(instance=ACG_CodeNode_strategy)
@settings(max_examples=50)
def test_acg_codenode_instantiation(instance):
    assert isinstance(instance, ACG_CodeNode)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=ACG_SequenceExp_strategy)
@settings(max_examples=50)
def test_acg_sequenceexp_instantiation(instance):
    assert isinstance(instance, ACG_SequenceExp)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=ACG_StringExp_strategy)
@settings(max_examples=50)
def test_acg_stringexp_instantiation(instance):
    assert isinstance(instance, ACG_StringExp)



@given(instance=ACG_StringExp_strategy)
def test_acg_stringexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ACG_IntegerExp_strategy)
@settings(max_examples=50)
def test_acg_integerexp_instantiation(instance):
    assert isinstance(instance, ACG_IntegerExp)



@given(instance=ACG_IntegerExp_strategy)
def test_acg_integerexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ACG_CollectionExp_strategy)
@settings(max_examples=50)
def test_acg_collectionexp_instantiation(instance):
    assert isinstance(instance, ACG_CollectionExp)

@given(instance=ACG_BooleanExp_strategy)
@settings(max_examples=50)
def test_acg_booleanexp_instantiation(instance):
    assert isinstance(instance, ACG_BooleanExp)



@given(instance=ACG_BooleanExp_strategy)
def test_acg_booleanexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ACG_OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_acg_oclundefinedexp_instantiation(instance):
    assert isinstance(instance, ACG_OclUndefinedExp)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=ACG_OperatorCallExp_strategy)
@settings(max_examples=50)
def test_acg_operatorcallexp_instantiation(instance):
    assert isinstance(instance, ACG_OperatorCallExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=ACG_IteratorExp_strategy)
@settings(max_examples=50)
def test_acg_iteratorexp_instantiation(instance):
    assert isinstance(instance, ACG_IteratorExp)

@given(instance=ACG_OperationCallExp_strategy)
@settings(max_examples=50)
def test_acg_operationcallexp_instantiation(instance):
    assert isinstance(instance, ACG_OperationCallExp)

@given(instance=ACG_NavigationExp_strategy)
@settings(max_examples=50)
def test_acg_navigationexp_instantiation(instance):
    assert isinstance(instance, ACG_NavigationExp)

@given(instance=ACG_PopStat_strategy)
@settings(max_examples=50)
def test_acg_popstat_instantiation(instance):
    assert isinstance(instance, ACG_PopStat)

@given(instance=EmitWithLabelRefStat_strategy)
@settings(max_examples=50)
def test_emitwithlabelrefstat_instantiation(instance):
    assert isinstance(instance, EmitWithLabelRefStat)

@given(instance=ACG_GotoStat_strategy)
@settings(max_examples=50)
def test_acg_gotostat_instantiation(instance):
    assert isinstance(instance, ACG_GotoStat)

@given(instance=ACG_IfStat_strategy)
@settings(max_examples=50)
def test_acg_ifstat_instantiation(instance):
    assert isinstance(instance, ACG_IfStat)

@given(instance=LabelStat_strategy)
@settings(max_examples=50)
def test_labelstat_instantiation(instance):
    assert isinstance(instance, LabelStat)

@given(instance=ACG_EmitWithLabelRefStat_strategy)
@settings(max_examples=50)
def test_acg_emitwithlabelrefstat_instantiation(instance):
    assert isinstance(instance, ACG_EmitWithLabelRefStat)

@given(instance=EmitWithOperandStat_strategy)
@settings(max_examples=50)
def test_emitwithoperandstat_instantiation(instance):
    assert isinstance(instance, EmitWithOperandStat)

@given(instance=ACG_LoadStat_strategy)
@settings(max_examples=50)
def test_acg_loadstat_instantiation(instance):
    assert isinstance(instance, ACG_LoadStat)

@given(instance=ACG_PushDStat_strategy)
@settings(max_examples=50)
def test_acg_pushdstat_instantiation(instance):
    assert isinstance(instance, ACG_PushDStat)

@given(instance=ACG_PCallStat_strategy)
@settings(max_examples=50)
def test_acg_pcallstat_instantiation(instance):
    assert isinstance(instance, ACG_PCallStat)

@given(instance=ACG_CallStat_strategy)
@settings(max_examples=50)
def test_acg_callstat_instantiation(instance):
    assert isinstance(instance, ACG_CallStat)

@given(instance=ACG_StoreStat_strategy)
@settings(max_examples=50)
def test_acg_storestat_instantiation(instance):
    assert isinstance(instance, ACG_StoreStat)

@given(instance=ACG_SetStat_strategy)
@settings(max_examples=50)
def test_acg_setstat_instantiation(instance):
    assert isinstance(instance, ACG_SetStat)

@given(instance=ACG_SuperCallStat_strategy)
@settings(max_examples=50)
def test_acg_supercallstat_instantiation(instance):
    assert isinstance(instance, ACG_SuperCallStat)

@given(instance=ACG_PushIStat_strategy)
@settings(max_examples=50)
def test_acg_pushistat_instantiation(instance):
    assert isinstance(instance, ACG_PushIStat)

@given(instance=ACG_GetStat_strategy)
@settings(max_examples=50)
def test_acg_getstat_instantiation(instance):
    assert isinstance(instance, ACG_GetStat)

@given(instance=ACG_PushStat_strategy)
@settings(max_examples=50)
def test_acg_pushstat_instantiation(instance):
    assert isinstance(instance, ACG_PushStat)

@given(instance=ACG_EmitWithOperandStat_strategy)
@settings(max_examples=50)
def test_acg_emitwithoperandstat_instantiation(instance):
    assert isinstance(instance, ACG_EmitWithOperandStat)

@given(instance=ACG_PushFStat_strategy)
@settings(max_examples=50)
def test_acg_pushfstat_instantiation(instance):
    assert isinstance(instance, ACG_PushFStat)

@given(instance=ACG_PushTStat_strategy)
@settings(max_examples=50)
def test_acg_pushtstat_instantiation(instance):
    assert isinstance(instance, ACG_PushTStat)

@given(instance=ACG_FindMEStat_strategy)
@settings(max_examples=50)
def test_acg_findmestat_instantiation(instance):
    assert isinstance(instance, ACG_FindMEStat)

@given(instance=ACG_GetAsmStat_strategy)
@settings(max_examples=50)
def test_acg_getasmstat_instantiation(instance):
    assert isinstance(instance, ACG_GetAsmStat)

@given(instance=ACG_EndIterateStat_strategy)
@settings(max_examples=50)
def test_acg_enditeratestat_instantiation(instance):
    assert isinstance(instance, ACG_EndIterateStat)

@given(instance=ACG_IterateStat_strategy)
@settings(max_examples=50)
def test_acg_iteratestat_instantiation(instance):
    assert isinstance(instance, ACG_IterateStat)

@given(instance=ACG_ASMNode_strategy)
@settings(max_examples=50)
def test_acg_asmnode_instantiation(instance):
    assert isinstance(instance, ACG_ASMNode)

@given(instance=VariableDecl_strategy)
@settings(max_examples=50)
def test_variabledecl_instantiation(instance):
    assert isinstance(instance, VariableDecl)

@given(instance=ACG_Parameter_strategy)
@settings(max_examples=50)
def test_acg_parameter_instantiation(instance):
    assert isinstance(instance, ACG_Parameter)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ACG_SelfExp_strategy)
@settings(max_examples=50)
def test_acg_selfexp_instantiation(instance):
    assert isinstance(instance, ACG_SelfExp)

@given(instance=ACG_LastExp_strategy)
@settings(max_examples=50)
def test_acg_lastexp_instantiation(instance):
    assert isinstance(instance, ACG_LastExp)

@given(instance=ACG_LetExp_strategy)
@settings(max_examples=50)
def test_acg_letexp_instantiation(instance):
    assert isinstance(instance, ACG_LetExp)

@given(instance=ACG_IsAExp_strategy)
@settings(max_examples=50)
def test_acg_isaexp_instantiation(instance):
    assert isinstance(instance, ACG_IsAExp)



@given(instance=ACG_IsAExp_strategy)
def test_acg_isaexp_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ACG_VariableExp_strategy)
@settings(max_examples=50)
def test_acg_variableexp_instantiation(instance):
    assert isinstance(instance, ACG_VariableExp)

@given(instance=ACG_IfExp_strategy)
@settings(max_examples=50)
def test_acg_ifexp_instantiation(instance):
    assert isinstance(instance, ACG_IfExp)

@given(instance=ACG_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_acg_propertycallexp_instantiation(instance):
    assert isinstance(instance, ACG_PropertyCallExp)



@given(instance=ACG_PropertyCallExp_strategy)
def test_acg_propertycallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ACG_LiteralExp_strategy)
@settings(max_examples=50)
def test_acg_literalexp_instantiation(instance):
    assert isinstance(instance, ACG_LiteralExp)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=ACG_strategy)
@settings(max_examples=50)
def test_acg_instantiation(instance):
    assert isinstance(instance, ACG)

@given(instance=ACGElement_strategy)
@settings(max_examples=50)
def test_acgelement_instantiation(instance):
    assert isinstance(instance, ACGElement)

@given(instance=ACG_Attribute_strategy)
@settings(max_examples=50)
def test_acg_attribute_instantiation(instance):
    assert isinstance(instance, ACG_Attribute)



@given(instance=ACG_Attribute_strategy)
def test_acg_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ACG_Attribute_strategy)
def test_acg_attribute_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=ACG_Node_strategy)
@settings(max_examples=50)
def test_acg_node_instantiation(instance):
    assert isinstance(instance, ACG_Node)



@given(instance=ACG_Node_strategy)
def test_acg_node_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original



@given(instance=ACG_Node_strategy)
def test_acg_node_element_setter(instance):
    original = instance.element
    instance.element = original
    assert instance.element == original

@given(instance=ACG_Function_strategy)
@settings(max_examples=50)
def test_acg_function_instantiation(instance):
    assert isinstance(instance, ACG_Function)



@given(instance=ACG_Function_strategy)
def test_acg_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ACG_Function_strategy)
def test_acg_function_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=ACG_VariableDecl_strategy)
@settings(max_examples=50)
def test_acg_variabledecl_instantiation(instance):
    assert isinstance(instance, ACG_VariableDecl)



@given(instance=ACG_VariableDecl_strategy)
def test_acg_variabledecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ACG_Statement_strategy)
@settings(max_examples=50)
def test_acg_statement_instantiation(instance):
    assert isinstance(instance, ACG_Statement)

@given(instance=ACG_ACGElement_strategy)
@settings(max_examples=50)
def test_acg_acgelement_instantiation(instance):
    assert isinstance(instance, ACG_ACGElement)

@given(instance=ACG_StatementBlock_strategy)
@settings(max_examples=50)
def test_acg_statementblock_instantiation(instance):
    assert isinstance(instance, ACG_StatementBlock)

@given(instance=ACG_Expression_strategy)
@settings(max_examples=50)
def test_acg_expression_instantiation(instance):
    assert isinstance(instance, ACG_Expression)

@given(instance=ACG_ACG_strategy)
@settings(max_examples=50)
def test_acg_acg_instantiation(instance):
    assert isinstance(instance, ACG_ACG)



@given(instance=ACG_ACG_strategy)
def test_acg_acg_metamodel_setter(instance):
    original = instance.metamodel
    instance.metamodel = original
    assert instance.metamodel == original



@given(instance=ACG_ACG_strategy)
def test_acg_acg_startsWith_setter(instance):
    original = instance.startsWith
    instance.startsWith = original
    assert instance.startsWith == original

@given(instance=ACG_LocatedElement_strategy)
@settings(max_examples=50)
def test_acg_locatedelement_instantiation(instance):
    assert isinstance(instance, ACG_LocatedElement)



@given(instance=ACG_LocatedElement_strategy)
def test_acg_locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original



@given(instance=ACG_LocatedElement_strategy)
def test_acg_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=ACG_LocatedElement_strategy)
def test_acg_locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original
