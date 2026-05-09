import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CollectionExp,
    ACG::SequenceExp,
    LiteralExp,
    ACG::StringExp,
    ACG::BooleanExp,
    ACG::CollectionExp,
    ACG::IntegerExp,
    ACG::OclUndefinedExp,
    OperationCallExp,
    ACG::OperatorCallExp,
    PropertyCallExp,
    ACG::IteratorExp,
    ACG::OperationCallExp,
    ACG::NavigationExp,
    EmitWithLabelRefStat,
    ACG::GotoStat,
    ACG::IfStat,
    LabelStat,
    EmitWithOperandStat,
    ACG::LoadStat,
    ACG::SuperCallStat,
    ACG::StoreStat,
    ACG::PushIStat,
    ACG::GetStat,
    ACG::PCallStat,
    ACG::CallStat,
    ACG::PushDStat,
    ACG::SetStat,
    ACG::PushStat,
    EmitStat,
    ACG::IterateStat,
    ACG::DupStat,
    ACG::EndIterateStat,
    ACG::GetAsmStat,
    ACG::DeleteStat,
    ACG::EmitWithOperandStat,
    ACG::SwapStat,
    ACG::NewStat,
    ACG::PushFStat,
    ACG::EmitWithLabelRefStat,
    ACG::FindMEStat,
    ACG::PopStat,
    ACG::DupX1Stat,
    ACG::NewinStat,
    ACG::PushTStat,
    ACG::LabelStat,
    StatementBlock,
    CompoundStat,
    ACG::ConditionalStat,
    ACG::VariableStat,
    ACG::LetStat,
    ACG::OnceStat,
    ACG::OperationStat,
    ACG::AnalyzeStat,
    ACG::ForEachStat,
    Statement,
    ACG::FieldStat,
    ACG::ReportStat,
    ACG::ParamStat,
    ACG::EmitStat,
    ACG::CompoundStat,
    Node,
    ACG::CodeNode,
    ACG::SimpleNode,
    ACG::ASMNode,
    VariableDecl,
    ACG::Parameter,
    Expression,
    ACG::LiteralExp,
    ACG::PropertyCallExp,
    ACG::LetExp,
    ACG::SelfExp,
    ACG::VariableExp,
    ACG::LastExp,
    ACG::IsAExp,
    ACG::IfExp,
    Parameter,
    ACG,
    ACGElement,
    ACG::Function,
    ACG::Attribute,
    ACG::Node,
    LocatedElement,
    ACG::StatementBlock,
    ACG::VariableDecl,
    ACG::ACGElement,
    ACG::Statement,
    ACG::Expression,
    ACG::ACG,
    ACG::LocatedElement,
    Severity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_acg::sequenceexp_is_not_abstract():
    assert not inspect.isabstract(ACG::SequenceExp)


def test_acg::sequenceexp_constructor_exists():
    assert callable(ACG::SequenceExp.__init__)


def test_acg::sequenceexp_constructor_args():
    sig = inspect.signature(ACG::SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_acg::stringexp_is_not_abstract():
    assert not inspect.isabstract(ACG::StringExp)


def test_acg::stringexp_constructor_exists():
    assert callable(ACG::StringExp.__init__)


def test_acg::stringexp_constructor_args():
    sig = inspect.signature(ACG::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_acg::stringexp_has_value():
    assert hasattr(ACG::StringExp, "value")
    descriptor = None
    for klass in ACG::StringExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_acg::booleanexp_is_not_abstract():
    assert not inspect.isabstract(ACG::BooleanExp)


def test_acg::booleanexp_constructor_exists():
    assert callable(ACG::BooleanExp.__init__)


def test_acg::booleanexp_constructor_args():
    sig = inspect.signature(ACG::BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_acg::booleanexp_has_value():
    assert hasattr(ACG::BooleanExp, "value")
    descriptor = None
    for klass in ACG::BooleanExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_acg::collectionexp_is_not_abstract():
    assert not inspect.isabstract(ACG::CollectionExp)


def test_acg::collectionexp_constructor_exists():
    assert callable(ACG::CollectionExp.__init__)


def test_acg::collectionexp_constructor_args():
    sig = inspect.signature(ACG::CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_acg::integerexp_is_not_abstract():
    assert not inspect.isabstract(ACG::IntegerExp)


def test_acg::integerexp_constructor_exists():
    assert callable(ACG::IntegerExp.__init__)


def test_acg::integerexp_constructor_args():
    sig = inspect.signature(ACG::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_acg::integerexp_has_value():
    assert hasattr(ACG::IntegerExp, "value")
    descriptor = None
    for klass in ACG::IntegerExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_acg::oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(ACG::OclUndefinedExp)


def test_acg::oclundefinedexp_constructor_exists():
    assert callable(ACG::OclUndefinedExp.__init__)


def test_acg::oclundefinedexp_constructor_args():
    sig = inspect.signature(ACG::OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_acg::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(ACG::OperatorCallExp)


def test_acg::operatorcallexp_constructor_exists():
    assert callable(ACG::OperatorCallExp.__init__)


def test_acg::operatorcallexp_constructor_args():
    sig = inspect.signature(ACG::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_acg::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(ACG::IteratorExp)


def test_acg::iteratorexp_constructor_exists():
    assert callable(ACG::IteratorExp.__init__)


def test_acg::iteratorexp_constructor_args():
    sig = inspect.signature(ACG::IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_acg::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(ACG::OperationCallExp)


def test_acg::operationcallexp_constructor_exists():
    assert callable(ACG::OperationCallExp.__init__)


def test_acg::operationcallexp_constructor_args():
    sig = inspect.signature(ACG::OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_acg::navigationexp_is_not_abstract():
    assert not inspect.isabstract(ACG::NavigationExp)


def test_acg::navigationexp_constructor_exists():
    assert callable(ACG::NavigationExp.__init__)


def test_acg::navigationexp_constructor_args():
    sig = inspect.signature(ACG::NavigationExp.__init__)
    params = list(sig.parameters.keys())



def test_emitwithlabelrefstat_is_not_abstract():
    assert not inspect.isabstract(EmitWithLabelRefStat)


def test_emitwithlabelrefstat_constructor_exists():
    assert callable(EmitWithLabelRefStat.__init__)


def test_emitwithlabelrefstat_constructor_args():
    sig = inspect.signature(EmitWithLabelRefStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::gotostat_is_not_abstract():
    assert not inspect.isabstract(ACG::GotoStat)


def test_acg::gotostat_constructor_exists():
    assert callable(ACG::GotoStat.__init__)


def test_acg::gotostat_constructor_args():
    sig = inspect.signature(ACG::GotoStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::ifstat_is_not_abstract():
    assert not inspect.isabstract(ACG::IfStat)


def test_acg::ifstat_constructor_exists():
    assert callable(ACG::IfStat.__init__)


def test_acg::ifstat_constructor_args():
    sig = inspect.signature(ACG::IfStat.__init__)
    params = list(sig.parameters.keys())



def test_labelstat_is_not_abstract():
    assert not inspect.isabstract(LabelStat)


def test_labelstat_constructor_exists():
    assert callable(LabelStat.__init__)


def test_labelstat_constructor_args():
    sig = inspect.signature(LabelStat.__init__)
    params = list(sig.parameters.keys())



def test_emitwithoperandstat_is_not_abstract():
    assert not inspect.isabstract(EmitWithOperandStat)


def test_emitwithoperandstat_constructor_exists():
    assert callable(EmitWithOperandStat.__init__)


def test_emitwithoperandstat_constructor_args():
    sig = inspect.signature(EmitWithOperandStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::loadstat_is_not_abstract():
    assert not inspect.isabstract(ACG::LoadStat)


def test_acg::loadstat_constructor_exists():
    assert callable(ACG::LoadStat.__init__)


def test_acg::loadstat_constructor_args():
    sig = inspect.signature(ACG::LoadStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::supercallstat_is_not_abstract():
    assert not inspect.isabstract(ACG::SuperCallStat)


def test_acg::supercallstat_constructor_exists():
    assert callable(ACG::SuperCallStat.__init__)


def test_acg::supercallstat_constructor_args():
    sig = inspect.signature(ACG::SuperCallStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::storestat_is_not_abstract():
    assert not inspect.isabstract(ACG::StoreStat)


def test_acg::storestat_constructor_exists():
    assert callable(ACG::StoreStat.__init__)


def test_acg::storestat_constructor_args():
    sig = inspect.signature(ACG::StoreStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::pushistat_is_not_abstract():
    assert not inspect.isabstract(ACG::PushIStat)


def test_acg::pushistat_constructor_exists():
    assert callable(ACG::PushIStat.__init__)


def test_acg::pushistat_constructor_args():
    sig = inspect.signature(ACG::PushIStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::getstat_is_not_abstract():
    assert not inspect.isabstract(ACG::GetStat)


def test_acg::getstat_constructor_exists():
    assert callable(ACG::GetStat.__init__)


def test_acg::getstat_constructor_args():
    sig = inspect.signature(ACG::GetStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::pcallstat_is_not_abstract():
    assert not inspect.isabstract(ACG::PCallStat)


def test_acg::pcallstat_constructor_exists():
    assert callable(ACG::PCallStat.__init__)


def test_acg::pcallstat_constructor_args():
    sig = inspect.signature(ACG::PCallStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::callstat_is_not_abstract():
    assert not inspect.isabstract(ACG::CallStat)


def test_acg::callstat_constructor_exists():
    assert callable(ACG::CallStat.__init__)


def test_acg::callstat_constructor_args():
    sig = inspect.signature(ACG::CallStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::pushdstat_is_not_abstract():
    assert not inspect.isabstract(ACG::PushDStat)


def test_acg::pushdstat_constructor_exists():
    assert callable(ACG::PushDStat.__init__)


def test_acg::pushdstat_constructor_args():
    sig = inspect.signature(ACG::PushDStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::setstat_is_not_abstract():
    assert not inspect.isabstract(ACG::SetStat)


def test_acg::setstat_constructor_exists():
    assert callable(ACG::SetStat.__init__)


def test_acg::setstat_constructor_args():
    sig = inspect.signature(ACG::SetStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::pushstat_is_not_abstract():
    assert not inspect.isabstract(ACG::PushStat)


def test_acg::pushstat_constructor_exists():
    assert callable(ACG::PushStat.__init__)


def test_acg::pushstat_constructor_args():
    sig = inspect.signature(ACG::PushStat.__init__)
    params = list(sig.parameters.keys())



def test_emitstat_is_not_abstract():
    assert not inspect.isabstract(EmitStat)


def test_emitstat_constructor_exists():
    assert callable(EmitStat.__init__)


def test_emitstat_constructor_args():
    sig = inspect.signature(EmitStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::iteratestat_is_not_abstract():
    assert not inspect.isabstract(ACG::IterateStat)


def test_acg::iteratestat_constructor_exists():
    assert callable(ACG::IterateStat.__init__)


def test_acg::iteratestat_constructor_args():
    sig = inspect.signature(ACG::IterateStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::dupstat_is_not_abstract():
    assert not inspect.isabstract(ACG::DupStat)


def test_acg::dupstat_constructor_exists():
    assert callable(ACG::DupStat.__init__)


def test_acg::dupstat_constructor_args():
    sig = inspect.signature(ACG::DupStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::enditeratestat_is_not_abstract():
    assert not inspect.isabstract(ACG::EndIterateStat)


def test_acg::enditeratestat_constructor_exists():
    assert callable(ACG::EndIterateStat.__init__)


def test_acg::enditeratestat_constructor_args():
    sig = inspect.signature(ACG::EndIterateStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::getasmstat_is_not_abstract():
    assert not inspect.isabstract(ACG::GetAsmStat)


def test_acg::getasmstat_constructor_exists():
    assert callable(ACG::GetAsmStat.__init__)


def test_acg::getasmstat_constructor_args():
    sig = inspect.signature(ACG::GetAsmStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::deletestat_is_not_abstract():
    assert not inspect.isabstract(ACG::DeleteStat)


def test_acg::deletestat_constructor_exists():
    assert callable(ACG::DeleteStat.__init__)


def test_acg::deletestat_constructor_args():
    sig = inspect.signature(ACG::DeleteStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::emitwithoperandstat_is_not_abstract():
    assert not inspect.isabstract(ACG::EmitWithOperandStat)


def test_acg::emitwithoperandstat_constructor_exists():
    assert callable(ACG::EmitWithOperandStat.__init__)


def test_acg::emitwithoperandstat_constructor_args():
    sig = inspect.signature(ACG::EmitWithOperandStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::swapstat_is_not_abstract():
    assert not inspect.isabstract(ACG::SwapStat)


def test_acg::swapstat_constructor_exists():
    assert callable(ACG::SwapStat.__init__)


def test_acg::swapstat_constructor_args():
    sig = inspect.signature(ACG::SwapStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::newstat_is_not_abstract():
    assert not inspect.isabstract(ACG::NewStat)


def test_acg::newstat_constructor_exists():
    assert callable(ACG::NewStat.__init__)


def test_acg::newstat_constructor_args():
    sig = inspect.signature(ACG::NewStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::pushfstat_is_not_abstract():
    assert not inspect.isabstract(ACG::PushFStat)


def test_acg::pushfstat_constructor_exists():
    assert callable(ACG::PushFStat.__init__)


def test_acg::pushfstat_constructor_args():
    sig = inspect.signature(ACG::PushFStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::emitwithlabelrefstat_is_not_abstract():
    assert not inspect.isabstract(ACG::EmitWithLabelRefStat)


def test_acg::emitwithlabelrefstat_constructor_exists():
    assert callable(ACG::EmitWithLabelRefStat.__init__)


def test_acg::emitwithlabelrefstat_constructor_args():
    sig = inspect.signature(ACG::EmitWithLabelRefStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::findmestat_is_not_abstract():
    assert not inspect.isabstract(ACG::FindMEStat)


def test_acg::findmestat_constructor_exists():
    assert callable(ACG::FindMEStat.__init__)


def test_acg::findmestat_constructor_args():
    sig = inspect.signature(ACG::FindMEStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::popstat_is_not_abstract():
    assert not inspect.isabstract(ACG::PopStat)


def test_acg::popstat_constructor_exists():
    assert callable(ACG::PopStat.__init__)


def test_acg::popstat_constructor_args():
    sig = inspect.signature(ACG::PopStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::dupx1stat_is_not_abstract():
    assert not inspect.isabstract(ACG::DupX1Stat)


def test_acg::dupx1stat_constructor_exists():
    assert callable(ACG::DupX1Stat.__init__)


def test_acg::dupx1stat_constructor_args():
    sig = inspect.signature(ACG::DupX1Stat.__init__)
    params = list(sig.parameters.keys())



def test_acg::newinstat_is_not_abstract():
    assert not inspect.isabstract(ACG::NewinStat)


def test_acg::newinstat_constructor_exists():
    assert callable(ACG::NewinStat.__init__)


def test_acg::newinstat_constructor_args():
    sig = inspect.signature(ACG::NewinStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::pushtstat_is_not_abstract():
    assert not inspect.isabstract(ACG::PushTStat)


def test_acg::pushtstat_constructor_exists():
    assert callable(ACG::PushTStat.__init__)


def test_acg::pushtstat_constructor_args():
    sig = inspect.signature(ACG::PushTStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::labelstat_is_not_abstract():
    assert not inspect.isabstract(ACG::LabelStat)


def test_acg::labelstat_constructor_exists():
    assert callable(ACG::LabelStat.__init__)


def test_acg::labelstat_constructor_args():
    sig = inspect.signature(ACG::LabelStat.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_acg::labelstat_has_name():
    assert hasattr(ACG::LabelStat, "name")
    descriptor = None
    for klass in ACG::LabelStat.__mro__:
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



def test_acg::conditionalstat_is_not_abstract():
    assert not inspect.isabstract(ACG::ConditionalStat)


def test_acg::conditionalstat_constructor_exists():
    assert callable(ACG::ConditionalStat.__init__)


def test_acg::conditionalstat_constructor_args():
    sig = inspect.signature(ACG::ConditionalStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::variablestat_is_not_abstract():
    assert not inspect.isabstract(ACG::VariableStat)


def test_acg::variablestat_constructor_exists():
    assert callable(ACG::VariableStat.__init__)


def test_acg::variablestat_constructor_args():
    sig = inspect.signature(ACG::VariableStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::letstat_is_not_abstract():
    assert not inspect.isabstract(ACG::LetStat)


def test_acg::letstat_constructor_exists():
    assert callable(ACG::LetStat.__init__)


def test_acg::letstat_constructor_args():
    sig = inspect.signature(ACG::LetStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::oncestat_is_not_abstract():
    assert not inspect.isabstract(ACG::OnceStat)


def test_acg::oncestat_constructor_exists():
    assert callable(ACG::OnceStat.__init__)


def test_acg::oncestat_constructor_args():
    sig = inspect.signature(ACG::OnceStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::operationstat_is_not_abstract():
    assert not inspect.isabstract(ACG::OperationStat)


def test_acg::operationstat_constructor_exists():
    assert callable(ACG::OperationStat.__init__)


def test_acg::operationstat_constructor_args():
    sig = inspect.signature(ACG::OperationStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::analyzestat_is_not_abstract():
    assert not inspect.isabstract(ACG::AnalyzeStat)


def test_acg::analyzestat_constructor_exists():
    assert callable(ACG::AnalyzeStat.__init__)


def test_acg::analyzestat_constructor_args():
    sig = inspect.signature(ACG::AnalyzeStat.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_acg::analyzestat_has_mode():
    assert hasattr(ACG::AnalyzeStat, "mode")
    descriptor = None
    for klass in ACG::AnalyzeStat.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_acg::foreachstat_is_not_abstract():
    assert not inspect.isabstract(ACG::ForEachStat)


def test_acg::foreachstat_constructor_exists():
    assert callable(ACG::ForEachStat.__init__)


def test_acg::foreachstat_constructor_args():
    sig = inspect.signature(ACG::ForEachStat.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_acg::fieldstat_is_not_abstract():
    assert not inspect.isabstract(ACG::FieldStat)


def test_acg::fieldstat_constructor_exists():
    assert callable(ACG::FieldStat.__init__)


def test_acg::fieldstat_constructor_args():
    sig = inspect.signature(ACG::FieldStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::reportstat_is_not_abstract():
    assert not inspect.isabstract(ACG::ReportStat)


def test_acg::reportstat_constructor_exists():
    assert callable(ACG::ReportStat.__init__)


def test_acg::reportstat_constructor_args():
    sig = inspect.signature(ACG::ReportStat.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_acg::reportstat_has_severity():
    assert hasattr(ACG::ReportStat, "severity")
    descriptor = None
    for klass in ACG::ReportStat.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_acg::paramstat_is_not_abstract():
    assert not inspect.isabstract(ACG::ParamStat)


def test_acg::paramstat_constructor_exists():
    assert callable(ACG::ParamStat.__init__)


def test_acg::paramstat_constructor_args():
    sig = inspect.signature(ACG::ParamStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::emitstat_is_not_abstract():
    assert not inspect.isabstract(ACG::EmitStat)


def test_acg::emitstat_constructor_exists():
    assert callable(ACG::EmitStat.__init__)


def test_acg::emitstat_constructor_args():
    sig = inspect.signature(ACG::EmitStat.__init__)
    params = list(sig.parameters.keys())



def test_acg::compoundstat_is_not_abstract():
    assert not inspect.isabstract(ACG::CompoundStat)


def test_acg::compoundstat_constructor_exists():
    assert callable(ACG::CompoundStat.__init__)


def test_acg::compoundstat_constructor_args():
    sig = inspect.signature(ACG::CompoundStat.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_acg::codenode_is_not_abstract():
    assert not inspect.isabstract(ACG::CodeNode)


def test_acg::codenode_constructor_exists():
    assert callable(ACG::CodeNode.__init__)


def test_acg::codenode_constructor_args():
    sig = inspect.signature(ACG::CodeNode.__init__)
    params = list(sig.parameters.keys())



def test_acg::simplenode_is_not_abstract():
    assert not inspect.isabstract(ACG::SimpleNode)


def test_acg::simplenode_constructor_exists():
    assert callable(ACG::SimpleNode.__init__)


def test_acg::simplenode_constructor_args():
    sig = inspect.signature(ACG::SimpleNode.__init__)
    params = list(sig.parameters.keys())



def test_acg::asmnode_is_not_abstract():
    assert not inspect.isabstract(ACG::ASMNode)


def test_acg::asmnode_constructor_exists():
    assert callable(ACG::ASMNode.__init__)


def test_acg::asmnode_constructor_args():
    sig = inspect.signature(ACG::ASMNode.__init__)
    params = list(sig.parameters.keys())



def test_variabledecl_is_not_abstract():
    assert not inspect.isabstract(VariableDecl)


def test_variabledecl_constructor_exists():
    assert callable(VariableDecl.__init__)


def test_variabledecl_constructor_args():
    sig = inspect.signature(VariableDecl.__init__)
    params = list(sig.parameters.keys())



def test_acg::parameter_is_not_abstract():
    assert not inspect.isabstract(ACG::Parameter)


def test_acg::parameter_constructor_exists():
    assert callable(ACG::Parameter.__init__)


def test_acg::parameter_constructor_args():
    sig = inspect.signature(ACG::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_acg::literalexp_is_not_abstract():
    assert not inspect.isabstract(ACG::LiteralExp)


def test_acg::literalexp_constructor_exists():
    assert callable(ACG::LiteralExp.__init__)


def test_acg::literalexp_constructor_args():
    sig = inspect.signature(ACG::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_acg::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(ACG::PropertyCallExp)


def test_acg::propertycallexp_constructor_exists():
    assert callable(ACG::PropertyCallExp.__init__)


def test_acg::propertycallexp_constructor_args():
    sig = inspect.signature(ACG::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_acg::propertycallexp_has_name():
    assert hasattr(ACG::PropertyCallExp, "name")
    descriptor = None
    for klass in ACG::PropertyCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_acg::letexp_is_not_abstract():
    assert not inspect.isabstract(ACG::LetExp)


def test_acg::letexp_constructor_exists():
    assert callable(ACG::LetExp.__init__)


def test_acg::letexp_constructor_args():
    sig = inspect.signature(ACG::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_acg::selfexp_is_not_abstract():
    assert not inspect.isabstract(ACG::SelfExp)


def test_acg::selfexp_constructor_exists():
    assert callable(ACG::SelfExp.__init__)


def test_acg::selfexp_constructor_args():
    sig = inspect.signature(ACG::SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_acg::variableexp_is_not_abstract():
    assert not inspect.isabstract(ACG::VariableExp)


def test_acg::variableexp_constructor_exists():
    assert callable(ACG::VariableExp.__init__)


def test_acg::variableexp_constructor_args():
    sig = inspect.signature(ACG::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_acg::lastexp_is_not_abstract():
    assert not inspect.isabstract(ACG::LastExp)


def test_acg::lastexp_constructor_exists():
    assert callable(ACG::LastExp.__init__)


def test_acg::lastexp_constructor_args():
    sig = inspect.signature(ACG::LastExp.__init__)
    params = list(sig.parameters.keys())



def test_acg::isaexp_is_not_abstract():
    assert not inspect.isabstract(ACG::IsAExp)


def test_acg::isaexp_constructor_exists():
    assert callable(ACG::IsAExp.__init__)


def test_acg::isaexp_constructor_args():
    sig = inspect.signature(ACG::IsAExp.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_acg::isaexp_has_type():
    assert hasattr(ACG::IsAExp, "type")
    descriptor = None
    for klass in ACG::IsAExp.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_acg::ifexp_is_not_abstract():
    assert not inspect.isabstract(ACG::IfExp)


def test_acg::ifexp_constructor_exists():
    assert callable(ACG::IfExp.__init__)


def test_acg::ifexp_constructor_args():
    sig = inspect.signature(ACG::IfExp.__init__)
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



def test_acg::function_is_not_abstract():
    assert not inspect.isabstract(ACG::Function)


def test_acg::function_constructor_exists():
    assert callable(ACG::Function.__init__)


def test_acg::function_constructor_args():
    sig = inspect.signature(ACG::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "context" in params, "Missing parameter 'context'"

def test_acg::function_has_name():
    assert hasattr(ACG::Function, "name")
    descriptor = None
    for klass in ACG::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_acg::function_has_context():
    assert hasattr(ACG::Function, "context")
    descriptor = None
    for klass in ACG::Function.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



def test_acg::attribute_is_not_abstract():
    assert not inspect.isabstract(ACG::Attribute)


def test_acg::attribute_constructor_exists():
    assert callable(ACG::Attribute.__init__)


def test_acg::attribute_constructor_args():
    sig = inspect.signature(ACG::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "context" in params, "Missing parameter 'context'"

def test_acg::attribute_has_name():
    assert hasattr(ACG::Attribute, "name")
    descriptor = None
    for klass in ACG::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_acg::attribute_has_context():
    assert hasattr(ACG::Attribute, "context")
    descriptor = None
    for klass in ACG::Attribute.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



def test_acg::node_is_not_abstract():
    assert not inspect.isabstract(ACG::Node)


def test_acg::node_constructor_exists():
    assert callable(ACG::Node.__init__)


def test_acg::node_constructor_args():
    sig = inspect.signature(ACG::Node.__init__)
    params = list(sig.parameters.keys())
    assert "element" in params, "Missing parameter 'element'"
    assert "mode" in params, "Missing parameter 'mode'"

def test_acg::node_has_element():
    assert hasattr(ACG::Node, "element")
    descriptor = None
    for klass in ACG::Node.__mro__:
        if "element" in klass.__dict__:
            descriptor = klass.__dict__["element"]
            break
    assert isinstance(descriptor, property)

def test_acg::node_has_mode():
    assert hasattr(ACG::Node, "mode")
    descriptor = None
    for klass in ACG::Node.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_acg::statementblock_is_not_abstract():
    assert not inspect.isabstract(ACG::StatementBlock)


def test_acg::statementblock_constructor_exists():
    assert callable(ACG::StatementBlock.__init__)


def test_acg::statementblock_constructor_args():
    sig = inspect.signature(ACG::StatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_acg::variabledecl_is_not_abstract():
    assert not inspect.isabstract(ACG::VariableDecl)


def test_acg::variabledecl_constructor_exists():
    assert callable(ACG::VariableDecl.__init__)


def test_acg::variabledecl_constructor_args():
    sig = inspect.signature(ACG::VariableDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_acg::variabledecl_has_name():
    assert hasattr(ACG::VariableDecl, "name")
    descriptor = None
    for klass in ACG::VariableDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_acg::acgelement_is_not_abstract():
    assert not inspect.isabstract(ACG::ACGElement)


def test_acg::acgelement_constructor_exists():
    assert callable(ACG::ACGElement.__init__)


def test_acg::acgelement_constructor_args():
    sig = inspect.signature(ACG::ACGElement.__init__)
    params = list(sig.parameters.keys())



def test_acg::statement_is_not_abstract():
    assert not inspect.isabstract(ACG::Statement)


def test_acg::statement_constructor_exists():
    assert callable(ACG::Statement.__init__)


def test_acg::statement_constructor_args():
    sig = inspect.signature(ACG::Statement.__init__)
    params = list(sig.parameters.keys())



def test_acg::expression_is_not_abstract():
    assert not inspect.isabstract(ACG::Expression)


def test_acg::expression_constructor_exists():
    assert callable(ACG::Expression.__init__)


def test_acg::expression_constructor_args():
    sig = inspect.signature(ACG::Expression.__init__)
    params = list(sig.parameters.keys())



def test_acg::acg_is_not_abstract():
    assert not inspect.isabstract(ACG::ACG)


def test_acg::acg_constructor_exists():
    assert callable(ACG::ACG.__init__)


def test_acg::acg_constructor_args():
    sig = inspect.signature(ACG::ACG.__init__)
    params = list(sig.parameters.keys())
    assert "startsWith" in params, "Missing parameter 'startsWith'"
    assert "metamodel" in params, "Missing parameter 'metamodel'"

def test_acg::acg_has_startsWith():
    assert hasattr(ACG::ACG, "startsWith")
    descriptor = None
    for klass in ACG::ACG.__mro__:
        if "startsWith" in klass.__dict__:
            descriptor = klass.__dict__["startsWith"]
            break
    assert isinstance(descriptor, property)

def test_acg::acg_has_metamodel():
    assert hasattr(ACG::ACG, "metamodel")
    descriptor = None
    for klass in ACG::ACG.__mro__:
        if "metamodel" in klass.__dict__:
            descriptor = klass.__dict__["metamodel"]
            break
    assert isinstance(descriptor, property)



def test_acg::locatedelement_is_not_abstract():
    assert not inspect.isabstract(ACG::LocatedElement)


def test_acg::locatedelement_constructor_exists():
    assert callable(ACG::LocatedElement.__init__)


def test_acg::locatedelement_constructor_args():
    sig = inspect.signature(ACG::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"

def test_acg::locatedelement_has_commentsAfter():
    assert hasattr(ACG::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in ACG::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_acg::locatedelement_has_location():
    assert hasattr(ACG::LocatedElement, "location")
    descriptor = None
    for klass in ACG::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_acg::locatedelement_has_commentsBefore():
    assert hasattr(ACG::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in ACG::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_severity_exists():
    # Check that the Enumeration exists
    assert Severity is not None

def test_severity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Severity]
    expected_literals = [
        "error",
        "warning",
        "critic",
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
CollectionExp_strategy = st.builds(
    CollectionExp,
)
ACG::SequenceExp_strategy = st.builds(
    ACG::SequenceExp,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
ACG::StringExp_strategy = st.builds(
    ACG::StringExp,
    value=
        safe_text
)
ACG::BooleanExp_strategy = st.builds(
    ACG::BooleanExp,
    value=
        safe_text
)
ACG::CollectionExp_strategy = st.builds(
    ACG::CollectionExp,
)
ACG::IntegerExp_strategy = st.builds(
    ACG::IntegerExp,
    value=
        safe_text
)
ACG::OclUndefinedExp_strategy = st.builds(
    ACG::OclUndefinedExp,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
ACG::OperatorCallExp_strategy = st.builds(
    ACG::OperatorCallExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
ACG::IteratorExp_strategy = st.builds(
    ACG::IteratorExp,
)
ACG::OperationCallExp_strategy = st.builds(
    ACG::OperationCallExp,
)
ACG::NavigationExp_strategy = st.builds(
    ACG::NavigationExp,
)
EmitWithLabelRefStat_strategy = st.builds(
    EmitWithLabelRefStat,
)
ACG::GotoStat_strategy = st.builds(
    ACG::GotoStat,
)
ACG::IfStat_strategy = st.builds(
    ACG::IfStat,
)
LabelStat_strategy = st.builds(
    LabelStat,
)
EmitWithOperandStat_strategy = st.builds(
    EmitWithOperandStat,
)
ACG::LoadStat_strategy = st.builds(
    ACG::LoadStat,
)
ACG::SuperCallStat_strategy = st.builds(
    ACG::SuperCallStat,
)
ACG::StoreStat_strategy = st.builds(
    ACG::StoreStat,
)
ACG::PushIStat_strategy = st.builds(
    ACG::PushIStat,
)
ACG::GetStat_strategy = st.builds(
    ACG::GetStat,
)
ACG::PCallStat_strategy = st.builds(
    ACG::PCallStat,
)
ACG::CallStat_strategy = st.builds(
    ACG::CallStat,
)
ACG::PushDStat_strategy = st.builds(
    ACG::PushDStat,
)
ACG::SetStat_strategy = st.builds(
    ACG::SetStat,
)
ACG::PushStat_strategy = st.builds(
    ACG::PushStat,
)
EmitStat_strategy = st.builds(
    EmitStat,
)
ACG::IterateStat_strategy = st.builds(
    ACG::IterateStat,
)
ACG::DupStat_strategy = st.builds(
    ACG::DupStat,
)
ACG::EndIterateStat_strategy = st.builds(
    ACG::EndIterateStat,
)
ACG::GetAsmStat_strategy = st.builds(
    ACG::GetAsmStat,
)
ACG::DeleteStat_strategy = st.builds(
    ACG::DeleteStat,
)
ACG::EmitWithOperandStat_strategy = st.builds(
    ACG::EmitWithOperandStat,
)
ACG::SwapStat_strategy = st.builds(
    ACG::SwapStat,
)
ACG::NewStat_strategy = st.builds(
    ACG::NewStat,
)
ACG::PushFStat_strategy = st.builds(
    ACG::PushFStat,
)
ACG::EmitWithLabelRefStat_strategy = st.builds(
    ACG::EmitWithLabelRefStat,
)
ACG::FindMEStat_strategy = st.builds(
    ACG::FindMEStat,
)
ACG::PopStat_strategy = st.builds(
    ACG::PopStat,
)
ACG::DupX1Stat_strategy = st.builds(
    ACG::DupX1Stat,
)
ACG::NewinStat_strategy = st.builds(
    ACG::NewinStat,
)
ACG::PushTStat_strategy = st.builds(
    ACG::PushTStat,
)
ACG::LabelStat_strategy = st.builds(
    ACG::LabelStat,
    name=
        safe_text
)
StatementBlock_strategy = st.builds(
    StatementBlock,
)
CompoundStat_strategy = st.builds(
    CompoundStat,
)
ACG::ConditionalStat_strategy = st.builds(
    ACG::ConditionalStat,
)
ACG::VariableStat_strategy = st.builds(
    ACG::VariableStat,
)
ACG::LetStat_strategy = st.builds(
    ACG::LetStat,
)
ACG::OnceStat_strategy = st.builds(
    ACG::OnceStat,
)
ACG::OperationStat_strategy = st.builds(
    ACG::OperationStat,
)
ACG::AnalyzeStat_strategy = st.builds(
    ACG::AnalyzeStat,
    mode=
        safe_text
)
ACG::ForEachStat_strategy = st.builds(
    ACG::ForEachStat,
)
Statement_strategy = st.builds(
    Statement,
)
ACG::FieldStat_strategy = st.builds(
    ACG::FieldStat,
)
ACG::ReportStat_strategy = st.builds(
    ACG::ReportStat,
    severity=
        safe_text
)
ACG::ParamStat_strategy = st.builds(
    ACG::ParamStat,
)
ACG::EmitStat_strategy = st.builds(
    ACG::EmitStat,
)
ACG::CompoundStat_strategy = st.builds(
    ACG::CompoundStat,
)
Node_strategy = st.builds(
    Node,
)
ACG::CodeNode_strategy = st.builds(
    ACG::CodeNode,
)
ACG::SimpleNode_strategy = st.builds(
    ACG::SimpleNode,
)
ACG::ASMNode_strategy = st.builds(
    ACG::ASMNode,
)
VariableDecl_strategy = st.builds(
    VariableDecl,
)
ACG::Parameter_strategy = st.builds(
    ACG::Parameter,
)
Expression_strategy = st.builds(
    Expression,
)
ACG::LiteralExp_strategy = st.builds(
    ACG::LiteralExp,
)
ACG::PropertyCallExp_strategy = st.builds(
    ACG::PropertyCallExp,
    name=
        safe_text
)
ACG::LetExp_strategy = st.builds(
    ACG::LetExp,
)
ACG::SelfExp_strategy = st.builds(
    ACG::SelfExp,
)
ACG::VariableExp_strategy = st.builds(
    ACG::VariableExp,
)
ACG::LastExp_strategy = st.builds(
    ACG::LastExp,
)
ACG::IsAExp_strategy = st.builds(
    ACG::IsAExp,
    type=
        safe_text
)
ACG::IfExp_strategy = st.builds(
    ACG::IfExp,
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
ACG::Function_strategy = st.builds(
    ACG::Function,
    name=
        safe_text,
    context=
        safe_text
)
ACG::Attribute_strategy = st.builds(
    ACG::Attribute,
    name=
        safe_text,
    context=
        safe_text
)
ACG::Node_strategy = st.builds(
    ACG::Node,
    element=
        safe_text,
    mode=
        safe_text
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
ACG::StatementBlock_strategy = st.builds(
    ACG::StatementBlock,
)
ACG::VariableDecl_strategy = st.builds(
    ACG::VariableDecl,
    name=
        safe_text
)
ACG::ACGElement_strategy = st.builds(
    ACG::ACGElement,
)
ACG::Statement_strategy = st.builds(
    ACG::Statement,
)
ACG::Expression_strategy = st.builds(
    ACG::Expression,
)
ACG::ACG_strategy = st.builds(
    ACG::ACG,
    startsWith=
        safe_text,
    metamodel=
        safe_text
)
ACG::LocatedElement_strategy = st.builds(
    ACG::LocatedElement,
    commentsAfter=
        safe_text,
    location=
        safe_text,
    commentsBefore=
        safe_text
)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=ACG::SequenceExp_strategy)
@settings(max_examples=50)
def test_acg::sequenceexp_instantiation(instance):
    assert isinstance(instance, ACG::SequenceExp)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=ACG::StringExp_strategy)
@settings(max_examples=50)
def test_acg::stringexp_instantiation(instance):
    assert isinstance(instance, ACG::StringExp)

@given(instance=ACG::StringExp_strategy)
def test_acg::stringexp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ACG::StringExp_strategy)
def test_acg::stringexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ACG::BooleanExp_strategy)
@settings(max_examples=50)
def test_acg::booleanexp_instantiation(instance):
    assert isinstance(instance, ACG::BooleanExp)

@given(instance=ACG::BooleanExp_strategy)
def test_acg::booleanexp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ACG::BooleanExp_strategy)
def test_acg::booleanexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ACG::CollectionExp_strategy)
@settings(max_examples=50)
def test_acg::collectionexp_instantiation(instance):
    assert isinstance(instance, ACG::CollectionExp)

@given(instance=ACG::IntegerExp_strategy)
@settings(max_examples=50)
def test_acg::integerexp_instantiation(instance):
    assert isinstance(instance, ACG::IntegerExp)

@given(instance=ACG::IntegerExp_strategy)
def test_acg::integerexp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ACG::IntegerExp_strategy)
def test_acg::integerexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ACG::OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_acg::oclundefinedexp_instantiation(instance):
    assert isinstance(instance, ACG::OclUndefinedExp)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=ACG::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_acg::operatorcallexp_instantiation(instance):
    assert isinstance(instance, ACG::OperatorCallExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=ACG::IteratorExp_strategy)
@settings(max_examples=50)
def test_acg::iteratorexp_instantiation(instance):
    assert isinstance(instance, ACG::IteratorExp)

@given(instance=ACG::OperationCallExp_strategy)
@settings(max_examples=50)
def test_acg::operationcallexp_instantiation(instance):
    assert isinstance(instance, ACG::OperationCallExp)

@given(instance=ACG::NavigationExp_strategy)
@settings(max_examples=50)
def test_acg::navigationexp_instantiation(instance):
    assert isinstance(instance, ACG::NavigationExp)

@given(instance=EmitWithLabelRefStat_strategy)
@settings(max_examples=50)
def test_emitwithlabelrefstat_instantiation(instance):
    assert isinstance(instance, EmitWithLabelRefStat)

@given(instance=ACG::GotoStat_strategy)
@settings(max_examples=50)
def test_acg::gotostat_instantiation(instance):
    assert isinstance(instance, ACG::GotoStat)

@given(instance=ACG::IfStat_strategy)
@settings(max_examples=50)
def test_acg::ifstat_instantiation(instance):
    assert isinstance(instance, ACG::IfStat)

@given(instance=LabelStat_strategy)
@settings(max_examples=50)
def test_labelstat_instantiation(instance):
    assert isinstance(instance, LabelStat)

@given(instance=EmitWithOperandStat_strategy)
@settings(max_examples=50)
def test_emitwithoperandstat_instantiation(instance):
    assert isinstance(instance, EmitWithOperandStat)

@given(instance=ACG::LoadStat_strategy)
@settings(max_examples=50)
def test_acg::loadstat_instantiation(instance):
    assert isinstance(instance, ACG::LoadStat)

@given(instance=ACG::SuperCallStat_strategy)
@settings(max_examples=50)
def test_acg::supercallstat_instantiation(instance):
    assert isinstance(instance, ACG::SuperCallStat)

@given(instance=ACG::StoreStat_strategy)
@settings(max_examples=50)
def test_acg::storestat_instantiation(instance):
    assert isinstance(instance, ACG::StoreStat)

@given(instance=ACG::PushIStat_strategy)
@settings(max_examples=50)
def test_acg::pushistat_instantiation(instance):
    assert isinstance(instance, ACG::PushIStat)

@given(instance=ACG::GetStat_strategy)
@settings(max_examples=50)
def test_acg::getstat_instantiation(instance):
    assert isinstance(instance, ACG::GetStat)

@given(instance=ACG::PCallStat_strategy)
@settings(max_examples=50)
def test_acg::pcallstat_instantiation(instance):
    assert isinstance(instance, ACG::PCallStat)

@given(instance=ACG::CallStat_strategy)
@settings(max_examples=50)
def test_acg::callstat_instantiation(instance):
    assert isinstance(instance, ACG::CallStat)

@given(instance=ACG::PushDStat_strategy)
@settings(max_examples=50)
def test_acg::pushdstat_instantiation(instance):
    assert isinstance(instance, ACG::PushDStat)

@given(instance=ACG::SetStat_strategy)
@settings(max_examples=50)
def test_acg::setstat_instantiation(instance):
    assert isinstance(instance, ACG::SetStat)

@given(instance=ACG::PushStat_strategy)
@settings(max_examples=50)
def test_acg::pushstat_instantiation(instance):
    assert isinstance(instance, ACG::PushStat)

@given(instance=EmitStat_strategy)
@settings(max_examples=50)
def test_emitstat_instantiation(instance):
    assert isinstance(instance, EmitStat)

@given(instance=ACG::IterateStat_strategy)
@settings(max_examples=50)
def test_acg::iteratestat_instantiation(instance):
    assert isinstance(instance, ACG::IterateStat)

@given(instance=ACG::DupStat_strategy)
@settings(max_examples=50)
def test_acg::dupstat_instantiation(instance):
    assert isinstance(instance, ACG::DupStat)

@given(instance=ACG::EndIterateStat_strategy)
@settings(max_examples=50)
def test_acg::enditeratestat_instantiation(instance):
    assert isinstance(instance, ACG::EndIterateStat)

@given(instance=ACG::GetAsmStat_strategy)
@settings(max_examples=50)
def test_acg::getasmstat_instantiation(instance):
    assert isinstance(instance, ACG::GetAsmStat)

@given(instance=ACG::DeleteStat_strategy)
@settings(max_examples=50)
def test_acg::deletestat_instantiation(instance):
    assert isinstance(instance, ACG::DeleteStat)

@given(instance=ACG::EmitWithOperandStat_strategy)
@settings(max_examples=50)
def test_acg::emitwithoperandstat_instantiation(instance):
    assert isinstance(instance, ACG::EmitWithOperandStat)

@given(instance=ACG::SwapStat_strategy)
@settings(max_examples=50)
def test_acg::swapstat_instantiation(instance):
    assert isinstance(instance, ACG::SwapStat)

@given(instance=ACG::NewStat_strategy)
@settings(max_examples=50)
def test_acg::newstat_instantiation(instance):
    assert isinstance(instance, ACG::NewStat)

@given(instance=ACG::PushFStat_strategy)
@settings(max_examples=50)
def test_acg::pushfstat_instantiation(instance):
    assert isinstance(instance, ACG::PushFStat)

@given(instance=ACG::EmitWithLabelRefStat_strategy)
@settings(max_examples=50)
def test_acg::emitwithlabelrefstat_instantiation(instance):
    assert isinstance(instance, ACG::EmitWithLabelRefStat)

@given(instance=ACG::FindMEStat_strategy)
@settings(max_examples=50)
def test_acg::findmestat_instantiation(instance):
    assert isinstance(instance, ACG::FindMEStat)

@given(instance=ACG::PopStat_strategy)
@settings(max_examples=50)
def test_acg::popstat_instantiation(instance):
    assert isinstance(instance, ACG::PopStat)

@given(instance=ACG::DupX1Stat_strategy)
@settings(max_examples=50)
def test_acg::dupx1stat_instantiation(instance):
    assert isinstance(instance, ACG::DupX1Stat)

@given(instance=ACG::NewinStat_strategy)
@settings(max_examples=50)
def test_acg::newinstat_instantiation(instance):
    assert isinstance(instance, ACG::NewinStat)

@given(instance=ACG::PushTStat_strategy)
@settings(max_examples=50)
def test_acg::pushtstat_instantiation(instance):
    assert isinstance(instance, ACG::PushTStat)

@given(instance=ACG::LabelStat_strategy)
@settings(max_examples=50)
def test_acg::labelstat_instantiation(instance):
    assert isinstance(instance, ACG::LabelStat)

@given(instance=ACG::LabelStat_strategy)
def test_acg::labelstat_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ACG::LabelStat_strategy)
def test_acg::labelstat_name_setter(instance):
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

@given(instance=ACG::ConditionalStat_strategy)
@settings(max_examples=50)
def test_acg::conditionalstat_instantiation(instance):
    assert isinstance(instance, ACG::ConditionalStat)

@given(instance=ACG::VariableStat_strategy)
@settings(max_examples=50)
def test_acg::variablestat_instantiation(instance):
    assert isinstance(instance, ACG::VariableStat)

@given(instance=ACG::LetStat_strategy)
@settings(max_examples=50)
def test_acg::letstat_instantiation(instance):
    assert isinstance(instance, ACG::LetStat)

@given(instance=ACG::OnceStat_strategy)
@settings(max_examples=50)
def test_acg::oncestat_instantiation(instance):
    assert isinstance(instance, ACG::OnceStat)

@given(instance=ACG::OperationStat_strategy)
@settings(max_examples=50)
def test_acg::operationstat_instantiation(instance):
    assert isinstance(instance, ACG::OperationStat)

@given(instance=ACG::AnalyzeStat_strategy)
@settings(max_examples=50)
def test_acg::analyzestat_instantiation(instance):
    assert isinstance(instance, ACG::AnalyzeStat)

@given(instance=ACG::AnalyzeStat_strategy)
def test_acg::analyzestat_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=ACG::AnalyzeStat_strategy)
def test_acg::analyzestat_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=ACG::ForEachStat_strategy)
@settings(max_examples=50)
def test_acg::foreachstat_instantiation(instance):
    assert isinstance(instance, ACG::ForEachStat)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=ACG::FieldStat_strategy)
@settings(max_examples=50)
def test_acg::fieldstat_instantiation(instance):
    assert isinstance(instance, ACG::FieldStat)

@given(instance=ACG::ReportStat_strategy)
@settings(max_examples=50)
def test_acg::reportstat_instantiation(instance):
    assert isinstance(instance, ACG::ReportStat)

@given(instance=ACG::ReportStat_strategy)
def test_acg::reportstat_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=ACG::ReportStat_strategy)
def test_acg::reportstat_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=ACG::ParamStat_strategy)
@settings(max_examples=50)
def test_acg::paramstat_instantiation(instance):
    assert isinstance(instance, ACG::ParamStat)

@given(instance=ACG::EmitStat_strategy)
@settings(max_examples=50)
def test_acg::emitstat_instantiation(instance):
    assert isinstance(instance, ACG::EmitStat)

@given(instance=ACG::CompoundStat_strategy)
@settings(max_examples=50)
def test_acg::compoundstat_instantiation(instance):
    assert isinstance(instance, ACG::CompoundStat)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=ACG::CodeNode_strategy)
@settings(max_examples=50)
def test_acg::codenode_instantiation(instance):
    assert isinstance(instance, ACG::CodeNode)

@given(instance=ACG::SimpleNode_strategy)
@settings(max_examples=50)
def test_acg::simplenode_instantiation(instance):
    assert isinstance(instance, ACG::SimpleNode)

@given(instance=ACG::ASMNode_strategy)
@settings(max_examples=50)
def test_acg::asmnode_instantiation(instance):
    assert isinstance(instance, ACG::ASMNode)

@given(instance=VariableDecl_strategy)
@settings(max_examples=50)
def test_variabledecl_instantiation(instance):
    assert isinstance(instance, VariableDecl)

@given(instance=ACG::Parameter_strategy)
@settings(max_examples=50)
def test_acg::parameter_instantiation(instance):
    assert isinstance(instance, ACG::Parameter)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ACG::LiteralExp_strategy)
@settings(max_examples=50)
def test_acg::literalexp_instantiation(instance):
    assert isinstance(instance, ACG::LiteralExp)

@given(instance=ACG::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_acg::propertycallexp_instantiation(instance):
    assert isinstance(instance, ACG::PropertyCallExp)

@given(instance=ACG::PropertyCallExp_strategy)
def test_acg::propertycallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ACG::PropertyCallExp_strategy)
def test_acg::propertycallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ACG::LetExp_strategy)
@settings(max_examples=50)
def test_acg::letexp_instantiation(instance):
    assert isinstance(instance, ACG::LetExp)

@given(instance=ACG::SelfExp_strategy)
@settings(max_examples=50)
def test_acg::selfexp_instantiation(instance):
    assert isinstance(instance, ACG::SelfExp)

@given(instance=ACG::VariableExp_strategy)
@settings(max_examples=50)
def test_acg::variableexp_instantiation(instance):
    assert isinstance(instance, ACG::VariableExp)

@given(instance=ACG::LastExp_strategy)
@settings(max_examples=50)
def test_acg::lastexp_instantiation(instance):
    assert isinstance(instance, ACG::LastExp)

@given(instance=ACG::IsAExp_strategy)
@settings(max_examples=50)
def test_acg::isaexp_instantiation(instance):
    assert isinstance(instance, ACG::IsAExp)

@given(instance=ACG::IsAExp_strategy)
def test_acg::isaexp_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ACG::IsAExp_strategy)
def test_acg::isaexp_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ACG::IfExp_strategy)
@settings(max_examples=50)
def test_acg::ifexp_instantiation(instance):
    assert isinstance(instance, ACG::IfExp)

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

@given(instance=ACG::Function_strategy)
@settings(max_examples=50)
def test_acg::function_instantiation(instance):
    assert isinstance(instance, ACG::Function)

@given(instance=ACG::Function_strategy)
def test_acg::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ACG::Function_strategy)
def test_acg::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ACG::Function_strategy)
def test_acg::function_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=ACG::Function_strategy)
def test_acg::function_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=ACG::Attribute_strategy)
@settings(max_examples=50)
def test_acg::attribute_instantiation(instance):
    assert isinstance(instance, ACG::Attribute)

@given(instance=ACG::Attribute_strategy)
def test_acg::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ACG::Attribute_strategy)
def test_acg::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ACG::Attribute_strategy)
def test_acg::attribute_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=ACG::Attribute_strategy)
def test_acg::attribute_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=ACG::Node_strategy)
@settings(max_examples=50)
def test_acg::node_instantiation(instance):
    assert isinstance(instance, ACG::Node)

@given(instance=ACG::Node_strategy)
def test_acg::node_element_type(instance):
    assert isinstance(instance.element, str)


@given(instance=ACG::Node_strategy)
def test_acg::node_element_setter(instance):
    original = instance.element
    instance.element = original
    assert instance.element == original

@given(instance=ACG::Node_strategy)
def test_acg::node_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=ACG::Node_strategy)
def test_acg::node_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=ACG::StatementBlock_strategy)
@settings(max_examples=50)
def test_acg::statementblock_instantiation(instance):
    assert isinstance(instance, ACG::StatementBlock)

@given(instance=ACG::VariableDecl_strategy)
@settings(max_examples=50)
def test_acg::variabledecl_instantiation(instance):
    assert isinstance(instance, ACG::VariableDecl)

@given(instance=ACG::VariableDecl_strategy)
def test_acg::variabledecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ACG::VariableDecl_strategy)
def test_acg::variabledecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ACG::ACGElement_strategy)
@settings(max_examples=50)
def test_acg::acgelement_instantiation(instance):
    assert isinstance(instance, ACG::ACGElement)

@given(instance=ACG::Statement_strategy)
@settings(max_examples=50)
def test_acg::statement_instantiation(instance):
    assert isinstance(instance, ACG::Statement)

@given(instance=ACG::Expression_strategy)
@settings(max_examples=50)
def test_acg::expression_instantiation(instance):
    assert isinstance(instance, ACG::Expression)

@given(instance=ACG::ACG_strategy)
@settings(max_examples=50)
def test_acg::acg_instantiation(instance):
    assert isinstance(instance, ACG::ACG)

@given(instance=ACG::ACG_strategy)
def test_acg::acg_startsWith_type(instance):
    assert isinstance(instance.startsWith, str)


@given(instance=ACG::ACG_strategy)
def test_acg::acg_startsWith_setter(instance):
    original = instance.startsWith
    instance.startsWith = original
    assert instance.startsWith == original

@given(instance=ACG::ACG_strategy)
def test_acg::acg_metamodel_type(instance):
    assert isinstance(instance.metamodel, str)


@given(instance=ACG::ACG_strategy)
def test_acg::acg_metamodel_setter(instance):
    original = instance.metamodel
    instance.metamodel = original
    assert instance.metamodel == original

@given(instance=ACG::LocatedElement_strategy)
@settings(max_examples=50)
def test_acg::locatedelement_instantiation(instance):
    assert isinstance(instance, ACG::LocatedElement)

@given(instance=ACG::LocatedElement_strategy)
def test_acg::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=ACG::LocatedElement_strategy)
def test_acg::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=ACG::LocatedElement_strategy)
def test_acg::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=ACG::LocatedElement_strategy)
def test_acg::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=ACG::LocatedElement_strategy)
def test_acg::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=ACG::LocatedElement_strategy)
def test_acg::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original
