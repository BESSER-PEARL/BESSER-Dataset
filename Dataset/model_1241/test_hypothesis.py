import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    imperativeocl::Typedef,
    imperativeocl::OrderedTupleType,
    imperativeocl::OrderedTupleLiteralPart,
    OrderedTupleLiteralPart,
    imperativeocl::OrderedTupleLiteralExp,
    imperativeocl::LogExp,
    imperativeocl::ListType,
    CatchExp,
    imperativeocl::TemplateParameterType,
    AltExp,
    imperativeocl::SwitchExp,
    imperativeocl::DictLiteralExp,
    imperativeocl::ImperativeLoopExp,
    imperativeocl::ImperativeExpression,
    ImperativeLoopExp,
    imperativeocl::ImperativeIterateExp,
    imperativeocl::ForExp,
    imperativeocl::DictionaryType,
    imperativeocl::DictLiteralPart,
    DictLiteralPart,
    LogExp,
    ImperativeExpression,
    imperativeocl::ComputeExp,
    imperativeocl::UnlinkExp,
    imperativeocl::ReturnExp,
    imperativeocl::BlockExp,
    imperativeocl::UnpackExp,
    imperativeocl::ContinueExp,
    imperativeocl::WhileExp,
    imperativeocl::AssertExp,
    imperativeocl::InstantiationExp,
    imperativeocl::TryExp,
    imperativeocl::CatchExp,
    imperativeocl::AssignExp,
    imperativeocl::BreakExp,
    imperativeocl::VariableInitExp,
    imperativeocl::RaiseExp,
    imperativeocl::AltExp,
    SeverityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_imperativeocl::typedef_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::Typedef)


def test_imperativeocl::typedef_constructor_exists():
    assert callable(imperativeocl::Typedef.__init__)


def test_imperativeocl::typedef_constructor_args():
    sig = inspect.signature(imperativeocl::Typedef.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::orderedtupletype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::OrderedTupleType)


def test_imperativeocl::orderedtupletype_constructor_exists():
    assert callable(imperativeocl::OrderedTupleType.__init__)


def test_imperativeocl::orderedtupletype_constructor_args():
    sig = inspect.signature(imperativeocl::OrderedTupleType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::orderedtupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::OrderedTupleLiteralPart)


def test_imperativeocl::orderedtupleliteralpart_constructor_exists():
    assert callable(imperativeocl::OrderedTupleLiteralPart.__init__)


def test_imperativeocl::orderedtupleliteralpart_constructor_args():
    sig = inspect.signature(imperativeocl::OrderedTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_orderedtupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(OrderedTupleLiteralPart)


def test_orderedtupleliteralpart_constructor_exists():
    assert callable(OrderedTupleLiteralPart.__init__)


def test_orderedtupleliteralpart_constructor_args():
    sig = inspect.signature(OrderedTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::orderedtupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::OrderedTupleLiteralExp)


def test_imperativeocl::orderedtupleliteralexp_constructor_exists():
    assert callable(imperativeocl::OrderedTupleLiteralExp.__init__)


def test_imperativeocl::orderedtupleliteralexp_constructor_args():
    sig = inspect.signature(imperativeocl::OrderedTupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::logexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::LogExp)


def test_imperativeocl::logexp_constructor_exists():
    assert callable(imperativeocl::LogExp.__init__)


def test_imperativeocl::logexp_constructor_args():
    sig = inspect.signature(imperativeocl::LogExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::listtype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ListType)


def test_imperativeocl::listtype_constructor_exists():
    assert callable(imperativeocl::ListType.__init__)


def test_imperativeocl::listtype_constructor_args():
    sig = inspect.signature(imperativeocl::ListType.__init__)
    params = list(sig.parameters.keys())



def test_catchexp_is_not_abstract():
    assert not inspect.isabstract(CatchExp)


def test_catchexp_constructor_exists():
    assert callable(CatchExp.__init__)


def test_catchexp_constructor_args():
    sig = inspect.signature(CatchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::templateparametertype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::TemplateParameterType)


def test_imperativeocl::templateparametertype_constructor_exists():
    assert callable(imperativeocl::TemplateParameterType.__init__)


def test_imperativeocl::templateparametertype_constructor_args():
    sig = inspect.signature(imperativeocl::TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_imperativeocl::templateparametertype_has_specification():
    assert hasattr(imperativeocl::TemplateParameterType, "specification")
    descriptor = None
    for klass in imperativeocl::TemplateParameterType.__mro__:
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



def test_imperativeocl::switchexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::SwitchExp)


def test_imperativeocl::switchexp_constructor_exists():
    assert callable(imperativeocl::SwitchExp.__init__)


def test_imperativeocl::switchexp_constructor_args():
    sig = inspect.signature(imperativeocl::SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::DictLiteralExp)


def test_imperativeocl::dictliteralexp_constructor_exists():
    assert callable(imperativeocl::DictLiteralExp.__init__)


def test_imperativeocl::dictliteralexp_constructor_args():
    sig = inspect.signature(imperativeocl::DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ImperativeLoopExp)


def test_imperativeocl::imperativeloopexp_constructor_exists():
    assert callable(imperativeocl::ImperativeLoopExp.__init__)


def test_imperativeocl::imperativeloopexp_constructor_args():
    sig = inspect.signature(imperativeocl::ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ImperativeExpression)


def test_imperativeocl::imperativeexpression_constructor_exists():
    assert callable(imperativeocl::ImperativeExpression.__init__)


def test_imperativeocl::imperativeexpression_constructor_args():
    sig = inspect.signature(imperativeocl::ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExp)


def test_imperativeloopexp_constructor_exists():
    assert callable(ImperativeLoopExp.__init__)


def test_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::imperativeiterateexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ImperativeIterateExp)


def test_imperativeocl::imperativeiterateexp_constructor_exists():
    assert callable(imperativeocl::ImperativeIterateExp.__init__)


def test_imperativeocl::imperativeiterateexp_constructor_args():
    sig = inspect.signature(imperativeocl::ImperativeIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::forexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ForExp)


def test_imperativeocl::forexp_constructor_exists():
    assert callable(imperativeocl::ForExp.__init__)


def test_imperativeocl::forexp_constructor_args():
    sig = inspect.signature(imperativeocl::ForExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::dictionarytype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::DictionaryType)


def test_imperativeocl::dictionarytype_constructor_exists():
    assert callable(imperativeocl::DictionaryType.__init__)


def test_imperativeocl::dictionarytype_constructor_args():
    sig = inspect.signature(imperativeocl::DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::DictLiteralPart)


def test_imperativeocl::dictliteralpart_constructor_exists():
    assert callable(imperativeocl::DictLiteralPart.__init__)


def test_imperativeocl::dictliteralpart_constructor_args():
    sig = inspect.signature(imperativeocl::DictLiteralPart.__init__)
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



def test_imperativeocl::computeexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ComputeExp)


def test_imperativeocl::computeexp_constructor_exists():
    assert callable(imperativeocl::ComputeExp.__init__)


def test_imperativeocl::computeexp_constructor_args():
    sig = inspect.signature(imperativeocl::ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::unlinkexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::UnlinkExp)


def test_imperativeocl::unlinkexp_constructor_exists():
    assert callable(imperativeocl::UnlinkExp.__init__)


def test_imperativeocl::unlinkexp_constructor_args():
    sig = inspect.signature(imperativeocl::UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::returnexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ReturnExp)


def test_imperativeocl::returnexp_constructor_exists():
    assert callable(imperativeocl::ReturnExp.__init__)


def test_imperativeocl::returnexp_constructor_args():
    sig = inspect.signature(imperativeocl::ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::blockexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::BlockExp)


def test_imperativeocl::blockexp_constructor_exists():
    assert callable(imperativeocl::BlockExp.__init__)


def test_imperativeocl::blockexp_constructor_args():
    sig = inspect.signature(imperativeocl::BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::unpackexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::UnpackExp)


def test_imperativeocl::unpackexp_constructor_exists():
    assert callable(imperativeocl::UnpackExp.__init__)


def test_imperativeocl::unpackexp_constructor_args():
    sig = inspect.signature(imperativeocl::UnpackExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::continueexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ContinueExp)


def test_imperativeocl::continueexp_constructor_exists():
    assert callable(imperativeocl::ContinueExp.__init__)


def test_imperativeocl::continueexp_constructor_args():
    sig = inspect.signature(imperativeocl::ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::whileexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::WhileExp)


def test_imperativeocl::whileexp_constructor_exists():
    assert callable(imperativeocl::WhileExp.__init__)


def test_imperativeocl::whileexp_constructor_args():
    sig = inspect.signature(imperativeocl::WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::assertexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::AssertExp)


def test_imperativeocl::assertexp_constructor_exists():
    assert callable(imperativeocl::AssertExp.__init__)


def test_imperativeocl::assertexp_constructor_args():
    sig = inspect.signature(imperativeocl::AssertExp.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_imperativeocl::assertexp_has_severity():
    assert hasattr(imperativeocl::AssertExp, "severity")
    descriptor = None
    for klass in imperativeocl::AssertExp.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::instantiationexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::InstantiationExp)


def test_imperativeocl::instantiationexp_constructor_exists():
    assert callable(imperativeocl::InstantiationExp.__init__)


def test_imperativeocl::instantiationexp_constructor_args():
    sig = inspect.signature(imperativeocl::InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::tryexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::TryExp)


def test_imperativeocl::tryexp_constructor_exists():
    assert callable(imperativeocl::TryExp.__init__)


def test_imperativeocl::tryexp_constructor_args():
    sig = inspect.signature(imperativeocl::TryExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::catchexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::CatchExp)


def test_imperativeocl::catchexp_constructor_exists():
    assert callable(imperativeocl::CatchExp.__init__)


def test_imperativeocl::catchexp_constructor_args():
    sig = inspect.signature(imperativeocl::CatchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::assignexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::AssignExp)


def test_imperativeocl::assignexp_constructor_exists():
    assert callable(imperativeocl::AssignExp.__init__)


def test_imperativeocl::assignexp_constructor_args():
    sig = inspect.signature(imperativeocl::AssignExp.__init__)
    params = list(sig.parameters.keys())
    assert "isReset" in params, "Missing parameter 'isReset'"

def test_imperativeocl::assignexp_has_isReset():
    assert hasattr(imperativeocl::AssignExp, "isReset")
    descriptor = None
    for klass in imperativeocl::AssignExp.__mro__:
        if "isReset" in klass.__dict__:
            descriptor = klass.__dict__["isReset"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::breakexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::BreakExp)


def test_imperativeocl::breakexp_constructor_exists():
    assert callable(imperativeocl::BreakExp.__init__)


def test_imperativeocl::breakexp_constructor_args():
    sig = inspect.signature(imperativeocl::BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::variableinitexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::VariableInitExp)


def test_imperativeocl::variableinitexp_constructor_exists():
    assert callable(imperativeocl::VariableInitExp.__init__)


def test_imperativeocl::variableinitexp_constructor_args():
    sig = inspect.signature(imperativeocl::VariableInitExp.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_imperativeocl::variableinitexp_has_withResult():
    assert hasattr(imperativeocl::VariableInitExp, "withResult")
    descriptor = None
    for klass in imperativeocl::VariableInitExp.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::raiseexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::RaiseExp)


def test_imperativeocl::raiseexp_constructor_exists():
    assert callable(imperativeocl::RaiseExp.__init__)


def test_imperativeocl::raiseexp_constructor_args():
    sig = inspect.signature(imperativeocl::RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::altexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::AltExp)


def test_imperativeocl::altexp_constructor_exists():
    assert callable(imperativeocl::AltExp.__init__)


def test_imperativeocl::altexp_constructor_args():
    sig = inspect.signature(imperativeocl::AltExp.__init__)
    params = list(sig.parameters.keys())

def test_severitykind_exists():
    # Check that the Enumeration exists
    assert SeverityKind is not None

def test_severitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SeverityKind]
    expected_literals = [
        "fatal",
        "warning",
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
imperativeocl::Typedef_strategy = st.builds(
    imperativeocl::Typedef,
)
imperativeocl::OrderedTupleType_strategy = st.builds(
    imperativeocl::OrderedTupleType,
)
imperativeocl::OrderedTupleLiteralPart_strategy = st.builds(
    imperativeocl::OrderedTupleLiteralPart,
)
OrderedTupleLiteralPart_strategy = st.builds(
    OrderedTupleLiteralPart,
)
imperativeocl::OrderedTupleLiteralExp_strategy = st.builds(
    imperativeocl::OrderedTupleLiteralExp,
)
imperativeocl::LogExp_strategy = st.builds(
    imperativeocl::LogExp,
)
imperativeocl::ListType_strategy = st.builds(
    imperativeocl::ListType,
)
CatchExp_strategy = st.builds(
    CatchExp,
)
imperativeocl::TemplateParameterType_strategy = st.builds(
    imperativeocl::TemplateParameterType,
    specification=
        safe_text
)
AltExp_strategy = st.builds(
    AltExp,
)
imperativeocl::SwitchExp_strategy = st.builds(
    imperativeocl::SwitchExp,
)
imperativeocl::DictLiteralExp_strategy = st.builds(
    imperativeocl::DictLiteralExp,
)
imperativeocl::ImperativeLoopExp_strategy = st.builds(
    imperativeocl::ImperativeLoopExp,
)
imperativeocl::ImperativeExpression_strategy = st.builds(
    imperativeocl::ImperativeExpression,
)
ImperativeLoopExp_strategy = st.builds(
    ImperativeLoopExp,
)
imperativeocl::ImperativeIterateExp_strategy = st.builds(
    imperativeocl::ImperativeIterateExp,
)
imperativeocl::ForExp_strategy = st.builds(
    imperativeocl::ForExp,
)
imperativeocl::DictionaryType_strategy = st.builds(
    imperativeocl::DictionaryType,
)
imperativeocl::DictLiteralPart_strategy = st.builds(
    imperativeocl::DictLiteralPart,
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
imperativeocl::ComputeExp_strategy = st.builds(
    imperativeocl::ComputeExp,
)
imperativeocl::UnlinkExp_strategy = st.builds(
    imperativeocl::UnlinkExp,
)
imperativeocl::ReturnExp_strategy = st.builds(
    imperativeocl::ReturnExp,
)
imperativeocl::BlockExp_strategy = st.builds(
    imperativeocl::BlockExp,
)
imperativeocl::UnpackExp_strategy = st.builds(
    imperativeocl::UnpackExp,
)
imperativeocl::ContinueExp_strategy = st.builds(
    imperativeocl::ContinueExp,
)
imperativeocl::WhileExp_strategy = st.builds(
    imperativeocl::WhileExp,
)
imperativeocl::AssertExp_strategy = st.builds(
    imperativeocl::AssertExp,
    severity=
        safe_text
)
imperativeocl::InstantiationExp_strategy = st.builds(
    imperativeocl::InstantiationExp,
)
imperativeocl::TryExp_strategy = st.builds(
    imperativeocl::TryExp,
)
imperativeocl::CatchExp_strategy = st.builds(
    imperativeocl::CatchExp,
)
imperativeocl::AssignExp_strategy = st.builds(
    imperativeocl::AssignExp,
    isReset=
        safe_text
)
imperativeocl::BreakExp_strategy = st.builds(
    imperativeocl::BreakExp,
)
imperativeocl::VariableInitExp_strategy = st.builds(
    imperativeocl::VariableInitExp,
    withResult=
        safe_text
)
imperativeocl::RaiseExp_strategy = st.builds(
    imperativeocl::RaiseExp,
)
imperativeocl::AltExp_strategy = st.builds(
    imperativeocl::AltExp,
)

@given(instance=imperativeocl::Typedef_strategy)
@settings(max_examples=50)
def test_imperativeocl::typedef_instantiation(instance):
    assert isinstance(instance, imperativeocl::Typedef)

@given(instance=imperativeocl::OrderedTupleType_strategy)
@settings(max_examples=50)
def test_imperativeocl::orderedtupletype_instantiation(instance):
    assert isinstance(instance, imperativeocl::OrderedTupleType)

@given(instance=imperativeocl::OrderedTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl::orderedtupleliteralpart_instantiation(instance):
    assert isinstance(instance, imperativeocl::OrderedTupleLiteralPart)

@given(instance=OrderedTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_orderedtupleliteralpart_instantiation(instance):
    assert isinstance(instance, OrderedTupleLiteralPart)

@given(instance=imperativeocl::OrderedTupleLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::orderedtupleliteralexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::OrderedTupleLiteralExp)

@given(instance=imperativeocl::LogExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::logexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::LogExp)

@given(instance=imperativeocl::ListType_strategy)
@settings(max_examples=50)
def test_imperativeocl::listtype_instantiation(instance):
    assert isinstance(instance, imperativeocl::ListType)

@given(instance=CatchExp_strategy)
@settings(max_examples=50)
def test_catchexp_instantiation(instance):
    assert isinstance(instance, CatchExp)

@given(instance=imperativeocl::TemplateParameterType_strategy)
@settings(max_examples=50)
def test_imperativeocl::templateparametertype_instantiation(instance):
    assert isinstance(instance, imperativeocl::TemplateParameterType)

@given(instance=imperativeocl::TemplateParameterType_strategy)
def test_imperativeocl::templateparametertype_specification_type(instance):
    assert isinstance(instance.specification, str)


@given(instance=imperativeocl::TemplateParameterType_strategy)
def test_imperativeocl::templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=AltExp_strategy)
@settings(max_examples=50)
def test_altexp_instantiation(instance):
    assert isinstance(instance, AltExp)

@given(instance=imperativeocl::SwitchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::switchexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::SwitchExp)

@given(instance=imperativeocl::DictLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::dictliteralexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::DictLiteralExp)

@given(instance=imperativeocl::ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeloopexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ImperativeLoopExp)

@given(instance=imperativeocl::ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeexpression_instantiation(instance):
    assert isinstance(instance, imperativeocl::ImperativeExpression)

@given(instance=ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExp)

@given(instance=imperativeocl::ImperativeIterateExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeiterateexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ImperativeIterateExp)

@given(instance=imperativeocl::ForExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::forexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ForExp)

@given(instance=imperativeocl::DictionaryType_strategy)
@settings(max_examples=50)
def test_imperativeocl::dictionarytype_instantiation(instance):
    assert isinstance(instance, imperativeocl::DictionaryType)

@given(instance=imperativeocl::DictLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl::dictliteralpart_instantiation(instance):
    assert isinstance(instance, imperativeocl::DictLiteralPart)

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

@given(instance=imperativeocl::ComputeExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::computeexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ComputeExp)

@given(instance=imperativeocl::UnlinkExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::unlinkexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::UnlinkExp)

@given(instance=imperativeocl::ReturnExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::returnexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ReturnExp)

@given(instance=imperativeocl::BlockExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::blockexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::BlockExp)

@given(instance=imperativeocl::UnpackExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::unpackexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::UnpackExp)

@given(instance=imperativeocl::ContinueExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::continueexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ContinueExp)

@given(instance=imperativeocl::WhileExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::whileexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::WhileExp)

@given(instance=imperativeocl::AssertExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::assertexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::AssertExp)

@given(instance=imperativeocl::AssertExp_strategy)
def test_imperativeocl::assertexp_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=imperativeocl::AssertExp_strategy)
def test_imperativeocl::assertexp_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=imperativeocl::InstantiationExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::instantiationexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::InstantiationExp)

@given(instance=imperativeocl::TryExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::tryexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::TryExp)

@given(instance=imperativeocl::CatchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::catchexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::CatchExp)

@given(instance=imperativeocl::AssignExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::assignexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::AssignExp)

@given(instance=imperativeocl::AssignExp_strategy)
def test_imperativeocl::assignexp_isReset_type(instance):
    assert isinstance(instance.isReset, str)


@given(instance=imperativeocl::AssignExp_strategy)
def test_imperativeocl::assignexp_isReset_setter(instance):
    original = instance.isReset
    instance.isReset = original
    assert instance.isReset == original

@given(instance=imperativeocl::BreakExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::breakexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::BreakExp)

@given(instance=imperativeocl::VariableInitExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::variableinitexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::VariableInitExp)

@given(instance=imperativeocl::VariableInitExp_strategy)
def test_imperativeocl::variableinitexp_withResult_type(instance):
    assert isinstance(instance.withResult, str)


@given(instance=imperativeocl::VariableInitExp_strategy)
def test_imperativeocl::variableinitexp_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=imperativeocl::RaiseExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::raiseexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::RaiseExp)

@given(instance=imperativeocl::AltExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::altexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::AltExp)
