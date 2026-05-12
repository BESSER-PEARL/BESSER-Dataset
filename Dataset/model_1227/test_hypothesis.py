import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    imperativeoclcs_CollectionLiteralPartCS,
    ImperativeLoopExpCS,
    imperativeoclcs_ImperativeIterateExpCS,
    imperativeoclcs_VariableCS,
    ExpressionBlockCS,
    imperativeoclcs_TryExpCS,
    imperativeoclcs_WhileExpCS,
    imperativeoclcs_ComputeExpCS,
    imperativeoclcs_TypedRefCS,
    TypedRefCS,
    imperativeoclcs_DictTypeCS,
    imperativeoclcs_PrimitiveLiteralExpCS,
    ElementCS,
    imperativeoclcs_DictLiteralPartCS,
    ExpCS,
    imperativeoclcs_StatementCS,
    imperativeoclcs_ListLiteralExpCS,
    imperativeoclcs_ReturnExpCS,
    imperativeoclcs_DictLiteralExpCS,
    imperativeoclcs_ListTypeCS,
    imperativeoclcs_ForExpCS,
    imperativeoclcs_ExpressionBlockCS,
    imperativeoclcs_Type,
    imperativeoclcs_ExceptCS,
    imperativeoclcs_DoExpCS,
    imperativeoclcs_TypeCS,
    CallExpCS,
    imperativeoclcs_LogExpCS,
    imperativeoclcs_ExpCS,
    StatementCS,
    imperativeoclcs_InstantiationExpCS,
    imperativeoclcs_AssignStatementCS,
    imperativeoclcs_ExpressionStatementCS,
    imperativeoclcs_VariableInitializationCS,
    imperativeoclcs_QuitExpCS,
    imperativeoclcs_BlockExpCS,
    imperativeoclcs_SwitchAltCS,
    imperativeoclcs_RaiseExpCS,
    imperativeoclcs_SwitchExpCS,
    imperativeoclcs_ImperativeLoopExpCS,
    imperativeoclcs_AssertExpCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_imperativeoclcs_collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_CollectionLiteralPartCS)


def test_imperativeoclcs_collectionliteralpartcs_constructor_exists():
    assert callable(imperativeoclcs_CollectionLiteralPartCS.__init__)


def test_imperativeoclcs_collectionliteralpartcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeloopexpcs_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExpCS)


def test_imperativeloopexpcs_constructor_exists():
    assert callable(ImperativeLoopExpCS.__init__)


def test_imperativeloopexpcs_constructor_args():
    sig = inspect.signature(ImperativeLoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_imperativeiterateexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_ImperativeIterateExpCS)


def test_imperativeoclcs_imperativeiterateexpcs_constructor_exists():
    assert callable(imperativeoclcs_ImperativeIterateExpCS.__init__)


def test_imperativeoclcs_imperativeiterateexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_ImperativeIterateExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_variablecs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_VariableCS)


def test_imperativeoclcs_variablecs_constructor_exists():
    assert callable(imperativeoclcs_VariableCS.__init__)


def test_imperativeoclcs_variablecs_constructor_args():
    sig = inspect.signature(imperativeoclcs_VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_expressionblockcs_is_not_abstract():
    assert not inspect.isabstract(ExpressionBlockCS)


def test_expressionblockcs_constructor_exists():
    assert callable(ExpressionBlockCS.__init__)


def test_expressionblockcs_constructor_args():
    sig = inspect.signature(ExpressionBlockCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_tryexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_TryExpCS)


def test_imperativeoclcs_tryexpcs_constructor_exists():
    assert callable(imperativeoclcs_TryExpCS.__init__)


def test_imperativeoclcs_tryexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_TryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_whileexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_WhileExpCS)


def test_imperativeoclcs_whileexpcs_constructor_exists():
    assert callable(imperativeoclcs_WhileExpCS.__init__)


def test_imperativeoclcs_whileexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_WhileExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_computeexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_ComputeExpCS)


def test_imperativeoclcs_computeexpcs_constructor_exists():
    assert callable(imperativeoclcs_ComputeExpCS.__init__)


def test_imperativeoclcs_computeexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_ComputeExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_TypedRefCS)


def test_imperativeoclcs_typedrefcs_constructor_exists():
    assert callable(imperativeoclcs_TypedRefCS.__init__)


def test_imperativeoclcs_typedrefcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(TypedRefCS)


def test_typedrefcs_constructor_exists():
    assert callable(TypedRefCS.__init__)


def test_typedrefcs_constructor_args():
    sig = inspect.signature(TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_dicttypecs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_DictTypeCS)


def test_imperativeoclcs_dicttypecs_constructor_exists():
    assert callable(imperativeoclcs_DictTypeCS.__init__)


def test_imperativeoclcs_dicttypecs_constructor_args():
    sig = inspect.signature(imperativeoclcs_DictTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_PrimitiveLiteralExpCS)


def test_imperativeoclcs_primitiveliteralexpcs_constructor_exists():
    assert callable(imperativeoclcs_PrimitiveLiteralExpCS.__init__)


def test_imperativeoclcs_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_elementcs_is_not_abstract():
    assert not inspect.isabstract(ElementCS)


def test_elementcs_constructor_exists():
    assert callable(ElementCS.__init__)


def test_elementcs_constructor_args():
    sig = inspect.signature(ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_dictliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_DictLiteralPartCS)


def test_imperativeoclcs_dictliteralpartcs_constructor_exists():
    assert callable(imperativeoclcs_DictLiteralPartCS.__init__)


def test_imperativeoclcs_dictliteralpartcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_DictLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_statementcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_StatementCS)


def test_imperativeoclcs_statementcs_constructor_exists():
    assert callable(imperativeoclcs_StatementCS.__init__)


def test_imperativeoclcs_statementcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_StatementCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_listliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_ListLiteralExpCS)


def test_imperativeoclcs_listliteralexpcs_constructor_exists():
    assert callable(imperativeoclcs_ListLiteralExpCS.__init__)


def test_imperativeoclcs_listliteralexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_ListLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_returnexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_ReturnExpCS)


def test_imperativeoclcs_returnexpcs_constructor_exists():
    assert callable(imperativeoclcs_ReturnExpCS.__init__)


def test_imperativeoclcs_returnexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_ReturnExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_dictliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_DictLiteralExpCS)


def test_imperativeoclcs_dictliteralexpcs_constructor_exists():
    assert callable(imperativeoclcs_DictLiteralExpCS.__init__)


def test_imperativeoclcs_dictliteralexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_DictLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_listtypecs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_ListTypeCS)


def test_imperativeoclcs_listtypecs_constructor_exists():
    assert callable(imperativeoclcs_ListTypeCS.__init__)


def test_imperativeoclcs_listtypecs_constructor_args():
    sig = inspect.signature(imperativeoclcs_ListTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_forexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_ForExpCS)


def test_imperativeoclcs_forexpcs_constructor_exists():
    assert callable(imperativeoclcs_ForExpCS.__init__)


def test_imperativeoclcs_forexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_ForExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_expressionblockcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_ExpressionBlockCS)


def test_imperativeoclcs_expressionblockcs_constructor_exists():
    assert callable(imperativeoclcs_ExpressionBlockCS.__init__)


def test_imperativeoclcs_expressionblockcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_ExpressionBlockCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_type_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_Type)


def test_imperativeoclcs_type_constructor_exists():
    assert callable(imperativeoclcs_Type.__init__)


def test_imperativeoclcs_type_constructor_args():
    sig = inspect.signature(imperativeoclcs_Type.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_exceptcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_ExceptCS)


def test_imperativeoclcs_exceptcs_constructor_exists():
    assert callable(imperativeoclcs_ExceptCS.__init__)


def test_imperativeoclcs_exceptcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_ExceptCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_doexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_DoExpCS)


def test_imperativeoclcs_doexpcs_constructor_exists():
    assert callable(imperativeoclcs_DoExpCS.__init__)


def test_imperativeoclcs_doexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_DoExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_typecs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_TypeCS)


def test_imperativeoclcs_typecs_constructor_exists():
    assert callable(imperativeoclcs_TypeCS.__init__)


def test_imperativeoclcs_typecs_constructor_args():
    sig = inspect.signature(imperativeoclcs_TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_logexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_LogExpCS)


def test_imperativeoclcs_logexpcs_constructor_exists():
    assert callable(imperativeoclcs_LogExpCS.__init__)


def test_imperativeoclcs_logexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_LogExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_expcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_ExpCS)


def test_imperativeoclcs_expcs_constructor_exists():
    assert callable(imperativeoclcs_ExpCS.__init__)


def test_imperativeoclcs_expcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_statementcs_is_not_abstract():
    assert not inspect.isabstract(StatementCS)


def test_statementcs_constructor_exists():
    assert callable(StatementCS.__init__)


def test_statementcs_constructor_args():
    sig = inspect.signature(StatementCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_instantiationexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_InstantiationExpCS)


def test_imperativeoclcs_instantiationexpcs_constructor_exists():
    assert callable(imperativeoclcs_InstantiationExpCS.__init__)


def test_imperativeoclcs_instantiationexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_InstantiationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_assignstatementcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_AssignStatementCS)


def test_imperativeoclcs_assignstatementcs_constructor_exists():
    assert callable(imperativeoclcs_AssignStatementCS.__init__)


def test_imperativeoclcs_assignstatementcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_AssignStatementCS.__init__)
    params = list(sig.parameters.keys())
    assert "incremental" in params, "Missing parameter 'incremental'"

def test_imperativeoclcs_assignstatementcs_has_incremental():
    assert hasattr(imperativeoclcs_AssignStatementCS, "incremental")
    descriptor = None
    for klass in imperativeoclcs_AssignStatementCS.__mro__:
        if "incremental" in klass.__dict__:
            descriptor = klass.__dict__["incremental"]
            break
    assert isinstance(descriptor, property)



def test_imperativeoclcs_expressionstatementcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_ExpressionStatementCS)


def test_imperativeoclcs_expressionstatementcs_constructor_exists():
    assert callable(imperativeoclcs_ExpressionStatementCS.__init__)


def test_imperativeoclcs_expressionstatementcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_ExpressionStatementCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_variableinitializationcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_VariableInitializationCS)


def test_imperativeoclcs_variableinitializationcs_constructor_exists():
    assert callable(imperativeoclcs_VariableInitializationCS.__init__)


def test_imperativeoclcs_variableinitializationcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_VariableInitializationCS.__init__)
    params = list(sig.parameters.keys())
    assert "simpleNameCS" in params, "Missing parameter 'simpleNameCS'"
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_imperativeoclcs_variableinitializationcs_has_simpleNameCS():
    assert hasattr(imperativeoclcs_VariableInitializationCS, "simpleNameCS")
    descriptor = None
    for klass in imperativeoclcs_VariableInitializationCS.__mro__:
        if "simpleNameCS" in klass.__dict__:
            descriptor = klass.__dict__["simpleNameCS"]
            break
    assert isinstance(descriptor, property)

def test_imperativeoclcs_variableinitializationcs_has_withResult():
    assert hasattr(imperativeoclcs_VariableInitializationCS, "withResult")
    descriptor = None
    for klass in imperativeoclcs_VariableInitializationCS.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_imperativeoclcs_quitexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_QuitExpCS)


def test_imperativeoclcs_quitexpcs_constructor_exists():
    assert callable(imperativeoclcs_QuitExpCS.__init__)


def test_imperativeoclcs_quitexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_QuitExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_imperativeoclcs_quitexpcs_has_keyword():
    assert hasattr(imperativeoclcs_QuitExpCS, "keyword")
    descriptor = None
    for klass in imperativeoclcs_QuitExpCS.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_imperativeoclcs_blockexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_BlockExpCS)


def test_imperativeoclcs_blockexpcs_constructor_exists():
    assert callable(imperativeoclcs_BlockExpCS.__init__)


def test_imperativeoclcs_blockexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_BlockExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_switchaltcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_SwitchAltCS)


def test_imperativeoclcs_switchaltcs_constructor_exists():
    assert callable(imperativeoclcs_SwitchAltCS.__init__)


def test_imperativeoclcs_switchaltcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_SwitchAltCS.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_imperativeoclcs_switchaltcs_has_keyword():
    assert hasattr(imperativeoclcs_SwitchAltCS, "keyword")
    descriptor = None
    for klass in imperativeoclcs_SwitchAltCS.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_imperativeoclcs_raiseexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_RaiseExpCS)


def test_imperativeoclcs_raiseexpcs_constructor_exists():
    assert callable(imperativeoclcs_RaiseExpCS.__init__)


def test_imperativeoclcs_raiseexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_RaiseExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_switchexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_SwitchExpCS)


def test_imperativeoclcs_switchexpcs_constructor_exists():
    assert callable(imperativeoclcs_SwitchExpCS.__init__)


def test_imperativeoclcs_switchexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_SwitchExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_imperativeloopexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_ImperativeLoopExpCS)


def test_imperativeoclcs_imperativeloopexpcs_constructor_exists():
    assert callable(imperativeoclcs_ImperativeLoopExpCS.__init__)


def test_imperativeoclcs_imperativeloopexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_ImperativeLoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs_assertexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs_AssertExpCS)


def test_imperativeoclcs_assertexpcs_constructor_exists():
    assert callable(imperativeoclcs_AssertExpCS.__init__)


def test_imperativeoclcs_assertexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs_AssertExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_imperativeoclcs_assertexpcs_has_severity():
    assert hasattr(imperativeoclcs_AssertExpCS, "severity")
    descriptor = None
    for klass in imperativeoclcs_AssertExpCS.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
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
imperativeoclcs_CollectionLiteralPartCS_strategy = st.builds(
    imperativeoclcs_CollectionLiteralPartCS,
)
ImperativeLoopExpCS_strategy = st.builds(
    ImperativeLoopExpCS,
)
imperativeoclcs_ImperativeIterateExpCS_strategy = st.builds(
    imperativeoclcs_ImperativeIterateExpCS,
)
imperativeoclcs_VariableCS_strategy = st.builds(
    imperativeoclcs_VariableCS,
)
ExpressionBlockCS_strategy = st.builds(
    ExpressionBlockCS,
)
imperativeoclcs_TryExpCS_strategy = st.builds(
    imperativeoclcs_TryExpCS,
)
imperativeoclcs_WhileExpCS_strategy = st.builds(
    imperativeoclcs_WhileExpCS,
)
imperativeoclcs_ComputeExpCS_strategy = st.builds(
    imperativeoclcs_ComputeExpCS,
)
imperativeoclcs_TypedRefCS_strategy = st.builds(
    imperativeoclcs_TypedRefCS,
)
TypedRefCS_strategy = st.builds(
    TypedRefCS,
)
imperativeoclcs_DictTypeCS_strategy = st.builds(
    imperativeoclcs_DictTypeCS,
)
imperativeoclcs_PrimitiveLiteralExpCS_strategy = st.builds(
    imperativeoclcs_PrimitiveLiteralExpCS,
)
ElementCS_strategy = st.builds(
    ElementCS,
)
imperativeoclcs_DictLiteralPartCS_strategy = st.builds(
    imperativeoclcs_DictLiteralPartCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
imperativeoclcs_StatementCS_strategy = st.builds(
    imperativeoclcs_StatementCS,
)
imperativeoclcs_ListLiteralExpCS_strategy = st.builds(
    imperativeoclcs_ListLiteralExpCS,
)
imperativeoclcs_ReturnExpCS_strategy = st.builds(
    imperativeoclcs_ReturnExpCS,
)
imperativeoclcs_DictLiteralExpCS_strategy = st.builds(
    imperativeoclcs_DictLiteralExpCS,
)
imperativeoclcs_ListTypeCS_strategy = st.builds(
    imperativeoclcs_ListTypeCS,
)
imperativeoclcs_ForExpCS_strategy = st.builds(
    imperativeoclcs_ForExpCS,
)
imperativeoclcs_ExpressionBlockCS_strategy = st.builds(
    imperativeoclcs_ExpressionBlockCS,
)
imperativeoclcs_Type_strategy = st.builds(
    imperativeoclcs_Type,
)
imperativeoclcs_ExceptCS_strategy = st.builds(
    imperativeoclcs_ExceptCS,
)
imperativeoclcs_DoExpCS_strategy = st.builds(
    imperativeoclcs_DoExpCS,
)
imperativeoclcs_TypeCS_strategy = st.builds(
    imperativeoclcs_TypeCS,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
imperativeoclcs_LogExpCS_strategy = st.builds(
    imperativeoclcs_LogExpCS,
)
imperativeoclcs_ExpCS_strategy = st.builds(
    imperativeoclcs_ExpCS,
)
StatementCS_strategy = st.builds(
    StatementCS,
)
imperativeoclcs_InstantiationExpCS_strategy = st.builds(
    imperativeoclcs_InstantiationExpCS,
)
imperativeoclcs_AssignStatementCS_strategy = st.builds(
    imperativeoclcs_AssignStatementCS,
    incremental=
        st.booleans()
)
imperativeoclcs_ExpressionStatementCS_strategy = st.builds(
    imperativeoclcs_ExpressionStatementCS,
)
imperativeoclcs_VariableInitializationCS_strategy = st.builds(
    imperativeoclcs_VariableInitializationCS,
    simpleNameCS=
        safe_text,
    withResult=
        st.booleans()
)
imperativeoclcs_QuitExpCS_strategy = st.builds(
    imperativeoclcs_QuitExpCS,
    keyword=
        safe_text
)
imperativeoclcs_BlockExpCS_strategy = st.builds(
    imperativeoclcs_BlockExpCS,
)
imperativeoclcs_SwitchAltCS_strategy = st.builds(
    imperativeoclcs_SwitchAltCS,
    keyword=
        safe_text
)
imperativeoclcs_RaiseExpCS_strategy = st.builds(
    imperativeoclcs_RaiseExpCS,
)
imperativeoclcs_SwitchExpCS_strategy = st.builds(
    imperativeoclcs_SwitchExpCS,
)
imperativeoclcs_ImperativeLoopExpCS_strategy = st.builds(
    imperativeoclcs_ImperativeLoopExpCS,
)
imperativeoclcs_AssertExpCS_strategy = st.builds(
    imperativeoclcs_AssertExpCS,
    severity=
        safe_text
)

@given(instance=imperativeoclcs_CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_CollectionLiteralPartCS)

@given(instance=ImperativeLoopExpCS_strategy)
@settings(max_examples=50)
def test_imperativeloopexpcs_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExpCS)

@given(instance=imperativeoclcs_ImperativeIterateExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_imperativeiterateexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_ImperativeIterateExpCS)

@given(instance=imperativeoclcs_VariableCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_variablecs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_VariableCS)

@given(instance=ExpressionBlockCS_strategy)
@settings(max_examples=50)
def test_expressionblockcs_instantiation(instance):
    assert isinstance(instance, ExpressionBlockCS)

@given(instance=imperativeoclcs_TryExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_tryexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_TryExpCS)

@given(instance=imperativeoclcs_WhileExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_whileexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_WhileExpCS)

@given(instance=imperativeoclcs_ComputeExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_computeexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_ComputeExpCS)

@given(instance=imperativeoclcs_TypedRefCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_typedrefcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_TypedRefCS)

@given(instance=TypedRefCS_strategy)
@settings(max_examples=50)
def test_typedrefcs_instantiation(instance):
    assert isinstance(instance, TypedRefCS)

@given(instance=imperativeoclcs_DictTypeCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_dicttypecs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_DictTypeCS)

@given(instance=imperativeoclcs_PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_PrimitiveLiteralExpCS)

@given(instance=ElementCS_strategy)
@settings(max_examples=50)
def test_elementcs_instantiation(instance):
    assert isinstance(instance, ElementCS)

@given(instance=imperativeoclcs_DictLiteralPartCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_dictliteralpartcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_DictLiteralPartCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=imperativeoclcs_StatementCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_statementcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_StatementCS)

@given(instance=imperativeoclcs_ListLiteralExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_listliteralexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_ListLiteralExpCS)

@given(instance=imperativeoclcs_ReturnExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_returnexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_ReturnExpCS)

@given(instance=imperativeoclcs_DictLiteralExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_dictliteralexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_DictLiteralExpCS)

@given(instance=imperativeoclcs_ListTypeCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_listtypecs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_ListTypeCS)

@given(instance=imperativeoclcs_ForExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_forexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_ForExpCS)

@given(instance=imperativeoclcs_ExpressionBlockCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_expressionblockcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_ExpressionBlockCS)

@given(instance=imperativeoclcs_Type_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_type_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_Type)

@given(instance=imperativeoclcs_ExceptCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_exceptcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_ExceptCS)

@given(instance=imperativeoclcs_DoExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_doexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_DoExpCS)

@given(instance=imperativeoclcs_TypeCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_typecs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_TypeCS)

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=imperativeoclcs_LogExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_logexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_LogExpCS)

@given(instance=imperativeoclcs_ExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_expcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_ExpCS)

@given(instance=StatementCS_strategy)
@settings(max_examples=50)
def test_statementcs_instantiation(instance):
    assert isinstance(instance, StatementCS)

@given(instance=imperativeoclcs_InstantiationExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_instantiationexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_InstantiationExpCS)

@given(instance=imperativeoclcs_AssignStatementCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_assignstatementcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_AssignStatementCS)



@given(instance=imperativeoclcs_AssignStatementCS_strategy)
def test_imperativeoclcs_assignstatementcs_incremental_setter(instance):
    original = instance.incremental
    instance.incremental = original
    assert instance.incremental == original

@given(instance=imperativeoclcs_ExpressionStatementCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_expressionstatementcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_ExpressionStatementCS)

@given(instance=imperativeoclcs_VariableInitializationCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_variableinitializationcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_VariableInitializationCS)



@given(instance=imperativeoclcs_VariableInitializationCS_strategy)
def test_imperativeoclcs_variableinitializationcs_simpleNameCS_setter(instance):
    original = instance.simpleNameCS
    instance.simpleNameCS = original
    assert instance.simpleNameCS == original



@given(instance=imperativeoclcs_VariableInitializationCS_strategy)
def test_imperativeoclcs_variableinitializationcs_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=imperativeoclcs_QuitExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_quitexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_QuitExpCS)



@given(instance=imperativeoclcs_QuitExpCS_strategy)
def test_imperativeoclcs_quitexpcs_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=imperativeoclcs_BlockExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_blockexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_BlockExpCS)

@given(instance=imperativeoclcs_SwitchAltCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_switchaltcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_SwitchAltCS)



@given(instance=imperativeoclcs_SwitchAltCS_strategy)
def test_imperativeoclcs_switchaltcs_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=imperativeoclcs_RaiseExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_raiseexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_RaiseExpCS)

@given(instance=imperativeoclcs_SwitchExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_switchexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_SwitchExpCS)

@given(instance=imperativeoclcs_ImperativeLoopExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_imperativeloopexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_ImperativeLoopExpCS)

@given(instance=imperativeoclcs_AssertExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs_assertexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs_AssertExpCS)



@given(instance=imperativeoclcs_AssertExpCS_strategy)
def test_imperativeoclcs_assertexpcs_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original
