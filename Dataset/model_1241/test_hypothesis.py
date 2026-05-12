import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    imperativeocl_Typedef,
    imperativeocl_OrderedTupleLiteralExp,
    imperativeocl_LogExp,
    imperativeocl_ListType,
    CatchExp,
    imperativeocl_TemplateParameterType,
    AltExp,
    imperativeocl_SwitchExp,
    imperativeocl_DictLiteralExp,
    imperativeocl_ImperativeLoopExp,
    imperativeocl_ImperativeExpression,
    ImperativeLoopExp,
    imperativeocl_ImperativeIterateExp,
    imperativeocl_ForExp,
    imperativeocl_DictionaryType,
    imperativeocl_DictLiteralPart,
    DictLiteralPart,
    LogExp,
    ImperativeExpression,
    imperativeocl_AssignExp,
    imperativeocl_AssertExp,
    imperativeocl_ReturnExp,
    imperativeocl_ComputeExp,
    imperativeocl_VariableInitExp,
    imperativeocl_UnlinkExp,
    imperativeocl_UnpackExp,
    imperativeocl_TryExp,
    imperativeocl_CatchExp,
    imperativeocl_InstantiationExp,
    imperativeocl_RaiseExp,
    imperativeocl_BlockExp,
    imperativeocl_ContinueExp,
    imperativeocl_BreakExp,
    imperativeocl_AltExp,
    imperativeocl_WhileExp,
    imperativeocl_OrderedTupleType,
    imperativeocl_OrderedTupleLiteralPart,
    OrderedTupleLiteralPart,
    SeverityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_imperativeocl_typedef_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_Typedef)


def test_imperativeocl_typedef_constructor_exists():
    assert callable(imperativeocl_Typedef.__init__)


def test_imperativeocl_typedef_constructor_args():
    sig = inspect.signature(imperativeocl_Typedef.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_orderedtupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_OrderedTupleLiteralExp)


def test_imperativeocl_orderedtupleliteralexp_constructor_exists():
    assert callable(imperativeocl_OrderedTupleLiteralExp.__init__)


def test_imperativeocl_orderedtupleliteralexp_constructor_args():
    sig = inspect.signature(imperativeocl_OrderedTupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_logexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_LogExp)


def test_imperativeocl_logexp_constructor_exists():
    assert callable(imperativeocl_LogExp.__init__)


def test_imperativeocl_logexp_constructor_args():
    sig = inspect.signature(imperativeocl_LogExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_listtype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ListType)


def test_imperativeocl_listtype_constructor_exists():
    assert callable(imperativeocl_ListType.__init__)


def test_imperativeocl_listtype_constructor_args():
    sig = inspect.signature(imperativeocl_ListType.__init__)
    params = list(sig.parameters.keys())



def test_catchexp_is_not_abstract():
    assert not inspect.isabstract(CatchExp)


def test_catchexp_constructor_exists():
    assert callable(CatchExp.__init__)


def test_catchexp_constructor_args():
    sig = inspect.signature(CatchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_templateparametertype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_TemplateParameterType)


def test_imperativeocl_templateparametertype_constructor_exists():
    assert callable(imperativeocl_TemplateParameterType.__init__)


def test_imperativeocl_templateparametertype_constructor_args():
    sig = inspect.signature(imperativeocl_TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_imperativeocl_templateparametertype_has_specification():
    assert hasattr(imperativeocl_TemplateParameterType, "specification")
    descriptor = None
    for klass in imperativeocl_TemplateParameterType.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_altexp_is_not_abstract():
    assert not inspect.isabstract(AltExp)


def test_altexp_constructor_exists():
    assert callable(AltExp.__init__)


def test_altexp_constructor_args():
    sig = inspect.signature(AltExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_switchexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_SwitchExp)


def test_imperativeocl_switchexp_constructor_exists():
    assert callable(imperativeocl_SwitchExp.__init__)


def test_imperativeocl_switchexp_constructor_args():
    sig = inspect.signature(imperativeocl_SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_DictLiteralExp)


def test_imperativeocl_dictliteralexp_constructor_exists():
    assert callable(imperativeocl_DictLiteralExp.__init__)


def test_imperativeocl_dictliteralexp_constructor_args():
    sig = inspect.signature(imperativeocl_DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ImperativeLoopExp)


def test_imperativeocl_imperativeloopexp_constructor_exists():
    assert callable(imperativeocl_ImperativeLoopExp.__init__)


def test_imperativeocl_imperativeloopexp_constructor_args():
    sig = inspect.signature(imperativeocl_ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ImperativeExpression)


def test_imperativeocl_imperativeexpression_constructor_exists():
    assert callable(imperativeocl_ImperativeExpression.__init__)


def test_imperativeocl_imperativeexpression_constructor_args():
    sig = inspect.signature(imperativeocl_ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExp)


def test_imperativeloopexp_constructor_exists():
    assert callable(ImperativeLoopExp.__init__)


def test_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_imperativeiterateexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ImperativeIterateExp)


def test_imperativeocl_imperativeiterateexp_constructor_exists():
    assert callable(imperativeocl_ImperativeIterateExp.__init__)


def test_imperativeocl_imperativeiterateexp_constructor_args():
    sig = inspect.signature(imperativeocl_ImperativeIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_forexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ForExp)


def test_imperativeocl_forexp_constructor_exists():
    assert callable(imperativeocl_ForExp.__init__)


def test_imperativeocl_forexp_constructor_args():
    sig = inspect.signature(imperativeocl_ForExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_dictionarytype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_DictionaryType)


def test_imperativeocl_dictionarytype_constructor_exists():
    assert callable(imperativeocl_DictionaryType.__init__)


def test_imperativeocl_dictionarytype_constructor_args():
    sig = inspect.signature(imperativeocl_DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_DictLiteralPart)


def test_imperativeocl_dictliteralpart_constructor_exists():
    assert callable(imperativeocl_DictLiteralPart.__init__)


def test_imperativeocl_dictliteralpart_constructor_args():
    sig = inspect.signature(imperativeocl_DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPart)


def test_dictliteralpart_constructor_exists():
    assert callable(DictLiteralPart.__init__)


def test_dictliteralpart_constructor_args():
    sig = inspect.signature(DictLiteralPart.__init__)
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



def test_imperativeocl_assignexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_AssignExp)


def test_imperativeocl_assignexp_constructor_exists():
    assert callable(imperativeocl_AssignExp.__init__)


def test_imperativeocl_assignexp_constructor_args():
    sig = inspect.signature(imperativeocl_AssignExp.__init__)
    params = list(sig.parameters.keys())
    assert "isReset" in params, "Missing parameter 'isReset'"

def test_imperativeocl_assignexp_has_isReset():
    assert hasattr(imperativeocl_AssignExp, "isReset")
    descriptor = None
    for klass in imperativeocl_AssignExp.__mro__:
        if "isReset" in klass.__dict__:
            descriptor = klass.__dict__["isReset"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl_assertexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_AssertExp)


def test_imperativeocl_assertexp_constructor_exists():
    assert callable(imperativeocl_AssertExp.__init__)


def test_imperativeocl_assertexp_constructor_args():
    sig = inspect.signature(imperativeocl_AssertExp.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_imperativeocl_assertexp_has_severity():
    assert hasattr(imperativeocl_AssertExp, "severity")
    descriptor = None
    for klass in imperativeocl_AssertExp.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl_returnexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ReturnExp)


def test_imperativeocl_returnexp_constructor_exists():
    assert callable(imperativeocl_ReturnExp.__init__)


def test_imperativeocl_returnexp_constructor_args():
    sig = inspect.signature(imperativeocl_ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_computeexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ComputeExp)


def test_imperativeocl_computeexp_constructor_exists():
    assert callable(imperativeocl_ComputeExp.__init__)


def test_imperativeocl_computeexp_constructor_args():
    sig = inspect.signature(imperativeocl_ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_variableinitexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_VariableInitExp)


def test_imperativeocl_variableinitexp_constructor_exists():
    assert callable(imperativeocl_VariableInitExp.__init__)


def test_imperativeocl_variableinitexp_constructor_args():
    sig = inspect.signature(imperativeocl_VariableInitExp.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_imperativeocl_variableinitexp_has_withResult():
    assert hasattr(imperativeocl_VariableInitExp, "withResult")
    descriptor = None
    for klass in imperativeocl_VariableInitExp.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl_unlinkexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_UnlinkExp)


def test_imperativeocl_unlinkexp_constructor_exists():
    assert callable(imperativeocl_UnlinkExp.__init__)


def test_imperativeocl_unlinkexp_constructor_args():
    sig = inspect.signature(imperativeocl_UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_unpackexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_UnpackExp)


def test_imperativeocl_unpackexp_constructor_exists():
    assert callable(imperativeocl_UnpackExp.__init__)


def test_imperativeocl_unpackexp_constructor_args():
    sig = inspect.signature(imperativeocl_UnpackExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_tryexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_TryExp)


def test_imperativeocl_tryexp_constructor_exists():
    assert callable(imperativeocl_TryExp.__init__)


def test_imperativeocl_tryexp_constructor_args():
    sig = inspect.signature(imperativeocl_TryExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_catchexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_CatchExp)


def test_imperativeocl_catchexp_constructor_exists():
    assert callable(imperativeocl_CatchExp.__init__)


def test_imperativeocl_catchexp_constructor_args():
    sig = inspect.signature(imperativeocl_CatchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_instantiationexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_InstantiationExp)


def test_imperativeocl_instantiationexp_constructor_exists():
    assert callable(imperativeocl_InstantiationExp.__init__)


def test_imperativeocl_instantiationexp_constructor_args():
    sig = inspect.signature(imperativeocl_InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_raiseexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_RaiseExp)


def test_imperativeocl_raiseexp_constructor_exists():
    assert callable(imperativeocl_RaiseExp.__init__)


def test_imperativeocl_raiseexp_constructor_args():
    sig = inspect.signature(imperativeocl_RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_blockexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_BlockExp)


def test_imperativeocl_blockexp_constructor_exists():
    assert callable(imperativeocl_BlockExp.__init__)


def test_imperativeocl_blockexp_constructor_args():
    sig = inspect.signature(imperativeocl_BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_continueexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_ContinueExp)


def test_imperativeocl_continueexp_constructor_exists():
    assert callable(imperativeocl_ContinueExp.__init__)


def test_imperativeocl_continueexp_constructor_args():
    sig = inspect.signature(imperativeocl_ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_breakexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_BreakExp)


def test_imperativeocl_breakexp_constructor_exists():
    assert callable(imperativeocl_BreakExp.__init__)


def test_imperativeocl_breakexp_constructor_args():
    sig = inspect.signature(imperativeocl_BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_altexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_AltExp)


def test_imperativeocl_altexp_constructor_exists():
    assert callable(imperativeocl_AltExp.__init__)


def test_imperativeocl_altexp_constructor_args():
    sig = inspect.signature(imperativeocl_AltExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_whileexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_WhileExp)


def test_imperativeocl_whileexp_constructor_exists():
    assert callable(imperativeocl_WhileExp.__init__)


def test_imperativeocl_whileexp_constructor_args():
    sig = inspect.signature(imperativeocl_WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_orderedtupletype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_OrderedTupleType)


def test_imperativeocl_orderedtupletype_constructor_exists():
    assert callable(imperativeocl_OrderedTupleType.__init__)


def test_imperativeocl_orderedtupletype_constructor_args():
    sig = inspect.signature(imperativeocl_OrderedTupleType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl_orderedtupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(imperativeocl_OrderedTupleLiteralPart)


def test_imperativeocl_orderedtupleliteralpart_constructor_exists():
    assert callable(imperativeocl_OrderedTupleLiteralPart.__init__)


def test_imperativeocl_orderedtupleliteralpart_constructor_args():
    sig = inspect.signature(imperativeocl_OrderedTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_orderedtupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(OrderedTupleLiteralPart)


def test_orderedtupleliteralpart_constructor_exists():
    assert callable(OrderedTupleLiteralPart.__init__)


def test_orderedtupleliteralpart_constructor_args():
    sig = inspect.signature(OrderedTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())

def test_severitykind_exists():
    # Check that the Enumeration exists
    assert SeverityKind is not None

def test_severitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SeverityKind]
    expected_literals = [
        "warning",
        "fatal",
        "error",
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
imperativeocl_Typedef_strategy = st.builds(
    imperativeocl_Typedef,
)
imperativeocl_OrderedTupleLiteralExp_strategy = st.builds(
    imperativeocl_OrderedTupleLiteralExp,
)
imperativeocl_LogExp_strategy = st.builds(
    imperativeocl_LogExp,
)
imperativeocl_ListType_strategy = st.builds(
    imperativeocl_ListType,
)
CatchExp_strategy = st.builds(
    CatchExp,
)
imperativeocl_TemplateParameterType_strategy = st.builds(
    imperativeocl_TemplateParameterType,
    specification=
        safe_text
)
AltExp_strategy = st.builds(
    AltExp,
)
imperativeocl_SwitchExp_strategy = st.builds(
    imperativeocl_SwitchExp,
)
imperativeocl_DictLiteralExp_strategy = st.builds(
    imperativeocl_DictLiteralExp,
)
imperativeocl_ImperativeLoopExp_strategy = st.builds(
    imperativeocl_ImperativeLoopExp,
)
imperativeocl_ImperativeExpression_strategy = st.builds(
    imperativeocl_ImperativeExpression,
)
ImperativeLoopExp_strategy = st.builds(
    ImperativeLoopExp,
)
imperativeocl_ImperativeIterateExp_strategy = st.builds(
    imperativeocl_ImperativeIterateExp,
)
imperativeocl_ForExp_strategy = st.builds(
    imperativeocl_ForExp,
)
imperativeocl_DictionaryType_strategy = st.builds(
    imperativeocl_DictionaryType,
)
imperativeocl_DictLiteralPart_strategy = st.builds(
    imperativeocl_DictLiteralPart,
)
DictLiteralPart_strategy = st.builds(
    DictLiteralPart,
)
LogExp_strategy = st.builds(
    LogExp,
)
ImperativeExpression_strategy = st.builds(
    ImperativeExpression,
)
imperativeocl_AssignExp_strategy = st.builds(
    imperativeocl_AssignExp,
    isReset=
        safe_text
)
imperativeocl_AssertExp_strategy = st.builds(
    imperativeocl_AssertExp,
    severity=
        safe_text
)
imperativeocl_ReturnExp_strategy = st.builds(
    imperativeocl_ReturnExp,
)
imperativeocl_ComputeExp_strategy = st.builds(
    imperativeocl_ComputeExp,
)
imperativeocl_VariableInitExp_strategy = st.builds(
    imperativeocl_VariableInitExp,
    withResult=
        safe_text
)
imperativeocl_UnlinkExp_strategy = st.builds(
    imperativeocl_UnlinkExp,
)
imperativeocl_UnpackExp_strategy = st.builds(
    imperativeocl_UnpackExp,
)
imperativeocl_TryExp_strategy = st.builds(
    imperativeocl_TryExp,
)
imperativeocl_CatchExp_strategy = st.builds(
    imperativeocl_CatchExp,
)
imperativeocl_InstantiationExp_strategy = st.builds(
    imperativeocl_InstantiationExp,
)
imperativeocl_RaiseExp_strategy = st.builds(
    imperativeocl_RaiseExp,
)
imperativeocl_BlockExp_strategy = st.builds(
    imperativeocl_BlockExp,
)
imperativeocl_ContinueExp_strategy = st.builds(
    imperativeocl_ContinueExp,
)
imperativeocl_BreakExp_strategy = st.builds(
    imperativeocl_BreakExp,
)
imperativeocl_AltExp_strategy = st.builds(
    imperativeocl_AltExp,
)
imperativeocl_WhileExp_strategy = st.builds(
    imperativeocl_WhileExp,
)
imperativeocl_OrderedTupleType_strategy = st.builds(
    imperativeocl_OrderedTupleType,
)
imperativeocl_OrderedTupleLiteralPart_strategy = st.builds(
    imperativeocl_OrderedTupleLiteralPart,
)
OrderedTupleLiteralPart_strategy = st.builds(
    OrderedTupleLiteralPart,
)

@given(instance=imperativeocl_Typedef_strategy)
@settings(max_examples=50)
def test_imperativeocl_typedef_instantiation(instance):
    assert isinstance(instance, imperativeocl_Typedef)

@given(instance=imperativeocl_OrderedTupleLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_orderedtupleliteralexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_OrderedTupleLiteralExp)

@given(instance=imperativeocl_LogExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_logexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_LogExp)

@given(instance=imperativeocl_ListType_strategy)
@settings(max_examples=50)
def test_imperativeocl_listtype_instantiation(instance):
    assert isinstance(instance, imperativeocl_ListType)

@given(instance=CatchExp_strategy)
@settings(max_examples=50)
def test_catchexp_instantiation(instance):
    assert isinstance(instance, CatchExp)

@given(instance=imperativeocl_TemplateParameterType_strategy)
@settings(max_examples=50)
def test_imperativeocl_templateparametertype_instantiation(instance):
    assert isinstance(instance, imperativeocl_TemplateParameterType)



@given(instance=imperativeocl_TemplateParameterType_strategy)
def test_imperativeocl_templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=AltExp_strategy)
@settings(max_examples=50)
def test_altexp_instantiation(instance):
    assert isinstance(instance, AltExp)

@given(instance=imperativeocl_SwitchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_switchexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_SwitchExp)

@given(instance=imperativeocl_DictLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_dictliteralexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_DictLiteralExp)

@given(instance=imperativeocl_ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_ImperativeLoopExp)

@given(instance=imperativeocl_ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeocl_imperativeexpression_instantiation(instance):
    assert isinstance(instance, imperativeocl_ImperativeExpression)

@given(instance=ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExp)

@given(instance=imperativeocl_ImperativeIterateExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_imperativeiterateexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_ImperativeIterateExp)

@given(instance=imperativeocl_ForExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_forexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_ForExp)

@given(instance=imperativeocl_DictionaryType_strategy)
@settings(max_examples=50)
def test_imperativeocl_dictionarytype_instantiation(instance):
    assert isinstance(instance, imperativeocl_DictionaryType)

@given(instance=imperativeocl_DictLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl_dictliteralpart_instantiation(instance):
    assert isinstance(instance, imperativeocl_DictLiteralPart)

@given(instance=DictLiteralPart_strategy)
@settings(max_examples=50)
def test_dictliteralpart_instantiation(instance):
    assert isinstance(instance, DictLiteralPart)

@given(instance=LogExp_strategy)
@settings(max_examples=50)
def test_logexp_instantiation(instance):
    assert isinstance(instance, LogExp)

@given(instance=ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeExpression)

@given(instance=imperativeocl_AssignExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_assignexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_AssignExp)



@given(instance=imperativeocl_AssignExp_strategy)
def test_imperativeocl_assignexp_isReset_setter(instance):
    original = instance.isReset
    instance.isReset = original
    assert instance.isReset == original

@given(instance=imperativeocl_AssertExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_assertexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_AssertExp)



@given(instance=imperativeocl_AssertExp_strategy)
def test_imperativeocl_assertexp_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=imperativeocl_ReturnExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_returnexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_ReturnExp)

@given(instance=imperativeocl_ComputeExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_computeexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_ComputeExp)

@given(instance=imperativeocl_VariableInitExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_variableinitexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_VariableInitExp)



@given(instance=imperativeocl_VariableInitExp_strategy)
def test_imperativeocl_variableinitexp_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=imperativeocl_UnlinkExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_unlinkexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_UnlinkExp)

@given(instance=imperativeocl_UnpackExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_unpackexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_UnpackExp)

@given(instance=imperativeocl_TryExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_tryexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_TryExp)

@given(instance=imperativeocl_CatchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_catchexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_CatchExp)

@given(instance=imperativeocl_InstantiationExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_instantiationexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_InstantiationExp)

@given(instance=imperativeocl_RaiseExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_raiseexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_RaiseExp)

@given(instance=imperativeocl_BlockExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_blockexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_BlockExp)

@given(instance=imperativeocl_ContinueExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_continueexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_ContinueExp)

@given(instance=imperativeocl_BreakExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_breakexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_BreakExp)

@given(instance=imperativeocl_AltExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_altexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_AltExp)

@given(instance=imperativeocl_WhileExp_strategy)
@settings(max_examples=50)
def test_imperativeocl_whileexp_instantiation(instance):
    assert isinstance(instance, imperativeocl_WhileExp)

@given(instance=imperativeocl_OrderedTupleType_strategy)
@settings(max_examples=50)
def test_imperativeocl_orderedtupletype_instantiation(instance):
    assert isinstance(instance, imperativeocl_OrderedTupleType)

@given(instance=imperativeocl_OrderedTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl_orderedtupleliteralpart_instantiation(instance):
    assert isinstance(instance, imperativeocl_OrderedTupleLiteralPart)

@given(instance=OrderedTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_orderedtupleliteralpart_instantiation(instance):
    assert isinstance(instance, OrderedTupleLiteralPart)
