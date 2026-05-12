import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ImperativeOCL_Typedef,
    CatchExp,
    AltExp,
    ImperativeOCL_OrderedTupleType,
    ImperativeOCL_OrderedTupleLiteralPart,
    OrderedTupleLiteralPart,
    ImperativeOCL_OrderedTupleLiteralExp,
    ImperativeOCL_LogExp,
    ImperativeOCL_ListType,
    ImperativeOCL_ListLiteralExp,
    ImperativeOCL_ImperativeLoopExp,
    ImperativeOCL_ImperativeExpression,
    ImperativeLoopExp,
    ImperativeOCL_ImperativeIterateExp,
    ImperativeOCL_ForExp,
    ImperativeOCL_DictionaryType,
    ImperativeOCL_DictLiteralPart,
    DictLiteralPart,
    ImperativeOCL_DictLiteralExp,
    LogExp,
    ImperativeExpression,
    ImperativeOCL_ContinueExp,
    ImperativeOCL_InstantiationExp,
    ImperativeOCL_ReturnExp,
    ImperativeOCL_ComputeExp,
    ImperativeOCL_UnlinkExp,
    ImperativeOCL_BreakExp,
    ImperativeOCL_RaiseExp,
    ImperativeOCL_UnpackExp,
    ImperativeOCL_VariableInitExp,
    ImperativeOCL_AssignExp,
    ImperativeOCL_TryExp,
    ImperativeOCL_CatchExp,
    ImperativeOCL_AssertExp,
    ImperativeOCL_WhileExp,
    ImperativeOCL_SwitchExp,
    ImperativeOCL_BlockExp,
    ImperativeOCL_AltExp,
    SeverityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_imperativeocl_typedef_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_Typedef)


def test_imperativeocl_typedef_constructor_exists():
    assert callable(ImperativeOCL_Typedef.__init__)


def test_imperativeocl_typedef_constructor_args():
    sig = inspect.signature(ImperativeOCL_Typedef.__init__)
    params = list(sig.parameters.keys())



def test_catchexp_is_not_abstract():
    assert not inspect.isabstract(CatchExp)


def test_catchexp_constructor_exists():
    assert callable(CatchExp.__init__)


def test_catchexp_constructor_args():
    sig = inspect.signature(CatchExp.__init__)
    params = list(sig.parameters.keys())



def test_altexp_is_not_abstract():
    assert not inspect.isabstract(AltExp)


def test_altexp_constructor_exists():
    assert callable(AltExp.__init__)


def test_altexp_constructor_args():
    sig = inspect.signature(AltExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_orderedtupletype_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_OrderedTupleType)


def test_imperativeocl_orderedtupletype_constructor_exists():
    assert callable(ImperativeOCL_OrderedTupleType.__init__)


def test_imperativeocl_orderedtupletype_constructor_args():
    sig = inspect.signature(ImperativeOCL_OrderedTupleType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_orderedtupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_OrderedTupleLiteralPart)


def test_imperativeocl_orderedtupleliteralpart_constructor_exists():
    assert callable(ImperativeOCL_OrderedTupleLiteralPart.__init__)


def test_imperativeocl_orderedtupleliteralpart_constructor_args():
    sig = inspect.signature(ImperativeOCL_OrderedTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_orderedtupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(OrderedTupleLiteralPart)


def test_orderedtupleliteralpart_constructor_exists():
    assert callable(OrderedTupleLiteralPart.__init__)


def test_orderedtupleliteralpart_constructor_args():
    sig = inspect.signature(OrderedTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_orderedtupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_OrderedTupleLiteralExp)


def test_imperativeocl_orderedtupleliteralexp_constructor_exists():
    assert callable(ImperativeOCL_OrderedTupleLiteralExp.__init__)


def test_imperativeocl_orderedtupleliteralexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_OrderedTupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_logexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_LogExp)


def test_imperativeocl_logexp_constructor_exists():
    assert callable(ImperativeOCL_LogExp.__init__)


def test_imperativeocl_logexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_LogExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_listtype_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ListType)


def test_imperativeocl_listtype_constructor_exists():
    assert callable(ImperativeOCL_ListType.__init__)


def test_imperativeocl_listtype_constructor_args():
    sig = inspect.signature(ImperativeOCL_ListType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_listliteralexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ListLiteralExp)


def test_imperativeocl_listliteralexp_constructor_exists():
    assert callable(ImperativeOCL_ListLiteralExp.__init__)


def test_imperativeocl_listliteralexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_ListLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ImperativeLoopExp)


def test_imperativeocl_imperativeloopexp_constructor_exists():
    assert callable(ImperativeOCL_ImperativeLoopExp.__init__)


def test_imperativeocl_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ImperativeExpression)


def test_imperativeocl_imperativeexpression_constructor_exists():
    assert callable(ImperativeOCL_ImperativeExpression.__init__)


def test_imperativeocl_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeOCL_ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExp)


def test_imperativeloopexp_constructor_exists():
    assert callable(ImperativeLoopExp.__init__)


def test_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_imperativeiterateexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ImperativeIterateExp)


def test_imperativeocl_imperativeiterateexp_constructor_exists():
    assert callable(ImperativeOCL_ImperativeIterateExp.__init__)


def test_imperativeocl_imperativeiterateexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_ImperativeIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_forexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ForExp)


def test_imperativeocl_forexp_constructor_exists():
    assert callable(ImperativeOCL_ForExp.__init__)


def test_imperativeocl_forexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_ForExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_dictionarytype_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_DictionaryType)


def test_imperativeocl_dictionarytype_constructor_exists():
    assert callable(ImperativeOCL_DictionaryType.__init__)


def test_imperativeocl_dictionarytype_constructor_args():
    sig = inspect.signature(ImperativeOCL_DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_DictLiteralPart)


def test_imperativeocl_dictliteralpart_constructor_exists():
    assert callable(ImperativeOCL_DictLiteralPart.__init__)


def test_imperativeocl_dictliteralpart_constructor_args():
    sig = inspect.signature(ImperativeOCL_DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPart)


def test_dictliteralpart_constructor_exists():
    assert callable(DictLiteralPart.__init__)


def test_dictliteralpart_constructor_args():
    sig = inspect.signature(DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_DictLiteralExp)


def test_imperativeocl_dictliteralexp_constructor_exists():
    assert callable(ImperativeOCL_DictLiteralExp.__init__)


def test_imperativeocl_dictliteralexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_logexp_is_not_abstract():
    assert not inspect.isabstract(LogExp)


def test_logexp_constructor_exists():
    assert callable(LogExp.__init__)


def test_logexp_constructor_args():
    sig = inspect.signature(LogExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeExpression)


def test_imperativeexpression_constructor_exists():
    assert callable(ImperativeExpression.__init__)


def test_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_continueexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ContinueExp)


def test_imperativeocl_continueexp_constructor_exists():
    assert callable(ImperativeOCL_ContinueExp.__init__)


def test_imperativeocl_continueexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_instantiationexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_InstantiationExp)


def test_imperativeocl_instantiationexp_constructor_exists():
    assert callable(ImperativeOCL_InstantiationExp.__init__)


def test_imperativeocl_instantiationexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_returnexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ReturnExp)


def test_imperativeocl_returnexp_constructor_exists():
    assert callable(ImperativeOCL_ReturnExp.__init__)


def test_imperativeocl_returnexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_computeexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_ComputeExp)


def test_imperativeocl_computeexp_constructor_exists():
    assert callable(ImperativeOCL_ComputeExp.__init__)


def test_imperativeocl_computeexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_unlinkexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_UnlinkExp)


def test_imperativeocl_unlinkexp_constructor_exists():
    assert callable(ImperativeOCL_UnlinkExp.__init__)


def test_imperativeocl_unlinkexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_breakexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_BreakExp)


def test_imperativeocl_breakexp_constructor_exists():
    assert callable(ImperativeOCL_BreakExp.__init__)


def test_imperativeocl_breakexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_raiseexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_RaiseExp)


def test_imperativeocl_raiseexp_constructor_exists():
    assert callable(ImperativeOCL_RaiseExp.__init__)


def test_imperativeocl_raiseexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_unpackexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_UnpackExp)


def test_imperativeocl_unpackexp_constructor_exists():
    assert callable(ImperativeOCL_UnpackExp.__init__)


def test_imperativeocl_unpackexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_UnpackExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_variableinitexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_VariableInitExp)


def test_imperativeocl_variableinitexp_constructor_exists():
    assert callable(ImperativeOCL_VariableInitExp.__init__)


def test_imperativeocl_variableinitexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_VariableInitExp.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_imperativeocl_variableinitexp_has_withResult():
    assert hasattr(ImperativeOCL_VariableInitExp, "withResult")
    descriptor = None
    for klass in ImperativeOCL_VariableInitExp.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl_assignexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_AssignExp)


def test_imperativeocl_assignexp_constructor_exists():
    assert callable(ImperativeOCL_AssignExp.__init__)


def test_imperativeocl_assignexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_AssignExp.__init__)
    params = list(sig.parameters.keys())
    assert "isReset" in params, "Missing parameter 'isReset'"

def test_imperativeocl_assignexp_has_isReset():
    assert hasattr(ImperativeOCL_AssignExp, "isReset")
    descriptor = None
    for klass in ImperativeOCL_AssignExp.__mro__:
        if "isReset" in klass.__dict__:
            descriptor = klass.__dict__["isReset"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl_tryexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_TryExp)


def test_imperativeocl_tryexp_constructor_exists():
    assert callable(ImperativeOCL_TryExp.__init__)


def test_imperativeocl_tryexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_TryExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_catchexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_CatchExp)


def test_imperativeocl_catchexp_constructor_exists():
    assert callable(ImperativeOCL_CatchExp.__init__)


def test_imperativeocl_catchexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_CatchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_assertexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_AssertExp)


def test_imperativeocl_assertexp_constructor_exists():
    assert callable(ImperativeOCL_AssertExp.__init__)


def test_imperativeocl_assertexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_AssertExp.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_imperativeocl_assertexp_has_severity():
    assert hasattr(ImperativeOCL_AssertExp, "severity")
    descriptor = None
    for klass in ImperativeOCL_AssertExp.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl_whileexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_WhileExp)


def test_imperativeocl_whileexp_constructor_exists():
    assert callable(ImperativeOCL_WhileExp.__init__)


def test_imperativeocl_whileexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_switchexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_SwitchExp)


def test_imperativeocl_switchexp_constructor_exists():
    assert callable(ImperativeOCL_SwitchExp.__init__)


def test_imperativeocl_switchexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_blockexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_BlockExp)


def test_imperativeocl_blockexp_constructor_exists():
    assert callable(ImperativeOCL_BlockExp.__init__)


def test_imperativeocl_blockexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_altexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL_AltExp)


def test_imperativeocl_altexp_constructor_exists():
    assert callable(ImperativeOCL_AltExp.__init__)


def test_imperativeocl_altexp_constructor_args():
    sig = inspect.signature(ImperativeOCL_AltExp.__init__)
    params = list(sig.parameters.keys())

def test_severitykind_exists():
    # Check that the Enumeration exists
    assert SeverityKind is not None

def test_severitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SeverityKind]
    expected_literals = [
        "error",
        "warning",
        "fatal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SeverityKind"


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
ImperativeOCL_Typedef_strategy = st.builds(
    ImperativeOCL_Typedef,
)
CatchExp_strategy = st.builds(
    CatchExp,
)
AltExp_strategy = st.builds(
    AltExp,
)
ImperativeOCL_OrderedTupleType_strategy = st.builds(
    ImperativeOCL_OrderedTupleType,
)
ImperativeOCL_OrderedTupleLiteralPart_strategy = st.builds(
    ImperativeOCL_OrderedTupleLiteralPart,
)
OrderedTupleLiteralPart_strategy = st.builds(
    OrderedTupleLiteralPart,
)
ImperativeOCL_OrderedTupleLiteralExp_strategy = st.builds(
    ImperativeOCL_OrderedTupleLiteralExp,
)
ImperativeOCL_LogExp_strategy = st.builds(
    ImperativeOCL_LogExp,
)
ImperativeOCL_ListType_strategy = st.builds(
    ImperativeOCL_ListType,
)
ImperativeOCL_ListLiteralExp_strategy = st.builds(
    ImperativeOCL_ListLiteralExp,
)
ImperativeOCL_ImperativeLoopExp_strategy = st.builds(
    ImperativeOCL_ImperativeLoopExp,
)
ImperativeOCL_ImperativeExpression_strategy = st.builds(
    ImperativeOCL_ImperativeExpression,
)
ImperativeLoopExp_strategy = st.builds(
    ImperativeLoopExp,
)
ImperativeOCL_ImperativeIterateExp_strategy = st.builds(
    ImperativeOCL_ImperativeIterateExp,
)
ImperativeOCL_ForExp_strategy = st.builds(
    ImperativeOCL_ForExp,
)
ImperativeOCL_DictionaryType_strategy = st.builds(
    ImperativeOCL_DictionaryType,
)
ImperativeOCL_DictLiteralPart_strategy = st.builds(
    ImperativeOCL_DictLiteralPart,
)
DictLiteralPart_strategy = st.builds(
    DictLiteralPart,
)
ImperativeOCL_DictLiteralExp_strategy = st.builds(
    ImperativeOCL_DictLiteralExp,
)
LogExp_strategy = st.builds(
    LogExp,
)
ImperativeExpression_strategy = st.builds(
    ImperativeExpression,
)
ImperativeOCL_ContinueExp_strategy = st.builds(
    ImperativeOCL_ContinueExp,
)
ImperativeOCL_InstantiationExp_strategy = st.builds(
    ImperativeOCL_InstantiationExp,
)
ImperativeOCL_ReturnExp_strategy = st.builds(
    ImperativeOCL_ReturnExp,
)
ImperativeOCL_ComputeExp_strategy = st.builds(
    ImperativeOCL_ComputeExp,
)
ImperativeOCL_UnlinkExp_strategy = st.builds(
    ImperativeOCL_UnlinkExp,
)
ImperativeOCL_BreakExp_strategy = st.builds(
    ImperativeOCL_BreakExp,
)
ImperativeOCL_RaiseExp_strategy = st.builds(
    ImperativeOCL_RaiseExp,
)
ImperativeOCL_UnpackExp_strategy = st.builds(
    ImperativeOCL_UnpackExp,
)
ImperativeOCL_VariableInitExp_strategy = st.builds(
    ImperativeOCL_VariableInitExp,
    withResult=
        safe_text
)
ImperativeOCL_AssignExp_strategy = st.builds(
    ImperativeOCL_AssignExp,
    isReset=
        safe_text
)
ImperativeOCL_TryExp_strategy = st.builds(
    ImperativeOCL_TryExp,
)
ImperativeOCL_CatchExp_strategy = st.builds(
    ImperativeOCL_CatchExp,
)
ImperativeOCL_AssertExp_strategy = st.builds(
    ImperativeOCL_AssertExp,
    severity=
        safe_text
)
ImperativeOCL_WhileExp_strategy = st.builds(
    ImperativeOCL_WhileExp,
)
ImperativeOCL_SwitchExp_strategy = st.builds(
    ImperativeOCL_SwitchExp,
)
ImperativeOCL_BlockExp_strategy = st.builds(
    ImperativeOCL_BlockExp,
)
ImperativeOCL_AltExp_strategy = st.builds(
    ImperativeOCL_AltExp,
)

@given(instance=ImperativeOCL_Typedef_strategy)
@settings(max_examples=50)
def test_imperativeocl_typedef_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_Typedef)

@given(instance=CatchExp_strategy)
@settings(max_examples=50)
def test_catchexp_instantiation(instance):
    assert isinstance(instance, CatchExp)

@given(instance=AltExp_strategy)
@settings(max_examples=50)
def test_altexp_instantiation(instance):
    assert isinstance(instance, AltExp)

@given(instance=ImperativeOCL_OrderedTupleType_strategy)
@settings(max_examples=50)
def test_imperativeocl_orderedtupletype_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_OrderedTupleType)

@given(instance=ImperativeOCL_OrderedTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl_orderedtupleliteralpart_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_OrderedTupleLiteralPart)

@given(instance=OrderedTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_orderedtupleliteralpart_instantiation(instance):
    assert isinstance(instance, OrderedTupleLiteralPart)

@given(instance=ImperativeOCL_OrderedTupleLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_orderedtupleliteralexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_OrderedTupleLiteralExp)

@given(instance=ImperativeOCL_LogExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_logexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_LogExp)

@given(instance=ImperativeOCL_ListType_strategy)
@settings(max_examples=50)
def test_imperativeocl_listtype_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ListType)

@given(instance=ImperativeOCL_ListLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_listliteralexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ListLiteralExp)

@given(instance=ImperativeOCL_ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ImperativeLoopExp)

@given(instance=ImperativeOCL_ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeocl_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ImperativeExpression)

@given(instance=ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExp)

@given(instance=ImperativeOCL_ImperativeIterateExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_imperativeiterateexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ImperativeIterateExp)

@given(instance=ImperativeOCL_ForExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_forexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ForExp)

@given(instance=ImperativeOCL_DictionaryType_strategy)
@settings(max_examples=50)
def test_imperativeocl_dictionarytype_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_DictionaryType)

@given(instance=ImperativeOCL_DictLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl_dictliteralpart_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_DictLiteralPart)

@given(instance=DictLiteralPart_strategy)
@settings(max_examples=50)
def test_dictliteralpart_instantiation(instance):
    assert isinstance(instance, DictLiteralPart)

@given(instance=ImperativeOCL_DictLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_dictliteralexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_DictLiteralExp)

@given(instance=LogExp_strategy)
@settings(max_examples=50)
def test_logexp_instantiation(instance):
    assert isinstance(instance, LogExp)

@given(instance=ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeExpression)

@given(instance=ImperativeOCL_ContinueExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_continueexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ContinueExp)

@given(instance=ImperativeOCL_InstantiationExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_instantiationexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_InstantiationExp)

@given(instance=ImperativeOCL_ReturnExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_returnexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ReturnExp)

@given(instance=ImperativeOCL_ComputeExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_computeexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_ComputeExp)

@given(instance=ImperativeOCL_UnlinkExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_unlinkexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_UnlinkExp)

@given(instance=ImperativeOCL_BreakExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_breakexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_BreakExp)

@given(instance=ImperativeOCL_RaiseExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_raiseexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_RaiseExp)

@given(instance=ImperativeOCL_UnpackExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_unpackexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_UnpackExp)

@given(instance=ImperativeOCL_VariableInitExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_variableinitexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_VariableInitExp)



@given(instance=ImperativeOCL_VariableInitExp_strategy)
def test_imperativeocl_variableinitexp_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=ImperativeOCL_AssignExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_assignexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_AssignExp)



@given(instance=ImperativeOCL_AssignExp_strategy)
def test_imperativeocl_assignexp_isReset_setter(instance):
    original = instance.isReset
    instance.isReset = original
    assert instance.isReset == original

@given(instance=ImperativeOCL_TryExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_tryexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_TryExp)

@given(instance=ImperativeOCL_CatchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_catchexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_CatchExp)

@given(instance=ImperativeOCL_AssertExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_assertexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_AssertExp)



@given(instance=ImperativeOCL_AssertExp_strategy)
def test_imperativeocl_assertexp_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=ImperativeOCL_WhileExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_whileexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_WhileExp)

@given(instance=ImperativeOCL_SwitchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_switchexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_SwitchExp)

@given(instance=ImperativeOCL_BlockExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_blockexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_BlockExp)

@given(instance=ImperativeOCL_AltExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_altexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL_AltExp)
