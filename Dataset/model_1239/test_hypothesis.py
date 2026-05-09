import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CatchExp,
    AltExp,
    OperationCallExp,
    Operation,
    Class,
    ImperativeOCL::Typedef,
    ImperativeLoopExp,
    ImperativeOCL::ImperativeIterateExp,
    ImperativeOCL::ForExp,
    CollectionType,
    ImperativeOCL::ListType,
    ImperativeOCL::DictionaryType,
    DictLiteralExp,
    Element,
    ImperativeOCL::DictLiteralPart,
    DictLiteralPart,
    LiteralExp,
    ImperativeOCL::ListLiteralExp,
    ImperativeOCL::DictLiteralExp,
    Type,
    Variable,
    LoopExp,
    OclExpression,
    ImperativeOCL::ImperativeExpression,
    ImperativeExpression,
    ImperativeOCL::VariableInitExp,
    ImperativeOCL::ContinueExp,
    ImperativeOCL::UnlinkExp,
    ImperativeOCL::RaiseExp,
    ImperativeOCL::BreakExp,
    ImperativeOCL::TryExp,
    ImperativeOCL::SwitchExp,
    ImperativeOCL::InstantiationExp,
    ImperativeOCL::ComputeExp,
    ImperativeOCL::AssignExp,
    ImperativeOCL::LogExp,
    ImperativeOCL::AssertExp,
    ImperativeOCL::BlockExp,
    ImperativeOCL::ReturnExp,
    ImperativeOCL::WhileExp,
    ImperativeOCL::CatchExp,
    ImperativeOCL::ImperativeLoopExp,
    ImperativeOCL::AltExp,
    LogExp,
    SeverityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::typedef_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::Typedef)


def test_imperativeocl::typedef_constructor_exists():
    assert callable(ImperativeOCL::Typedef.__init__)


def test_imperativeocl::typedef_constructor_args():
    sig = inspect.signature(ImperativeOCL::Typedef.__init__)
    params = list(sig.parameters.keys())



def test_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExp)


def test_imperativeloopexp_constructor_exists():
    assert callable(ImperativeLoopExp.__init__)


def test_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::imperativeiterateexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ImperativeIterateExp)


def test_imperativeocl::imperativeiterateexp_constructor_exists():
    assert callable(ImperativeOCL::ImperativeIterateExp.__init__)


def test_imperativeocl::imperativeiterateexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::ImperativeIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::forexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ForExp)


def test_imperativeocl::forexp_constructor_exists():
    assert callable(ImperativeOCL::ForExp.__init__)


def test_imperativeocl::forexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::ForExp.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::listtype_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ListType)


def test_imperativeocl::listtype_constructor_exists():
    assert callable(ImperativeOCL::ListType.__init__)


def test_imperativeocl::listtype_constructor_args():
    sig = inspect.signature(ImperativeOCL::ListType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::dictionarytype_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::DictionaryType)


def test_imperativeocl::dictionarytype_constructor_exists():
    assert callable(ImperativeOCL::DictionaryType.__init__)


def test_imperativeocl::dictionarytype_constructor_args():
    sig = inspect.signature(ImperativeOCL::DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(DictLiteralExp)


def test_dictliteralexp_constructor_exists():
    assert callable(DictLiteralExp.__init__)


def test_dictliteralexp_constructor_args():
    sig = inspect.signature(DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::DictLiteralPart)


def test_imperativeocl::dictliteralpart_constructor_exists():
    assert callable(ImperativeOCL::DictLiteralPart.__init__)


def test_imperativeocl::dictliteralpart_constructor_args():
    sig = inspect.signature(ImperativeOCL::DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPart)


def test_dictliteralpart_constructor_exists():
    assert callable(DictLiteralPart.__init__)


def test_dictliteralpart_constructor_args():
    sig = inspect.signature(DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::listliteralexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ListLiteralExp)


def test_imperativeocl::listliteralexp_constructor_exists():
    assert callable(ImperativeOCL::ListLiteralExp.__init__)


def test_imperativeocl::listliteralexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::ListLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::DictLiteralExp)


def test_imperativeocl::dictliteralexp_constructor_exists():
    assert callable(ImperativeOCL::DictLiteralExp.__init__)


def test_imperativeocl::dictliteralexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ImperativeExpression)


def test_imperativeocl::imperativeexpression_constructor_exists():
    assert callable(ImperativeOCL::ImperativeExpression.__init__)


def test_imperativeocl::imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeOCL::ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeExpression)


def test_imperativeexpression_constructor_exists():
    assert callable(ImperativeExpression.__init__)


def test_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::variableinitexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::VariableInitExp)


def test_imperativeocl::variableinitexp_constructor_exists():
    assert callable(ImperativeOCL::VariableInitExp.__init__)


def test_imperativeocl::variableinitexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::VariableInitExp.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_imperativeocl::variableinitexp_has_withResult():
    assert hasattr(ImperativeOCL::VariableInitExp, "withResult")
    descriptor = None
    for klass in ImperativeOCL::VariableInitExp.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::continueexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ContinueExp)


def test_imperativeocl::continueexp_constructor_exists():
    assert callable(ImperativeOCL::ContinueExp.__init__)


def test_imperativeocl::continueexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::unlinkexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::UnlinkExp)


def test_imperativeocl::unlinkexp_constructor_exists():
    assert callable(ImperativeOCL::UnlinkExp.__init__)


def test_imperativeocl::unlinkexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::raiseexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::RaiseExp)


def test_imperativeocl::raiseexp_constructor_exists():
    assert callable(ImperativeOCL::RaiseExp.__init__)


def test_imperativeocl::raiseexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::breakexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::BreakExp)


def test_imperativeocl::breakexp_constructor_exists():
    assert callable(ImperativeOCL::BreakExp.__init__)


def test_imperativeocl::breakexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::tryexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::TryExp)


def test_imperativeocl::tryexp_constructor_exists():
    assert callable(ImperativeOCL::TryExp.__init__)


def test_imperativeocl::tryexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::TryExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::switchexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::SwitchExp)


def test_imperativeocl::switchexp_constructor_exists():
    assert callable(ImperativeOCL::SwitchExp.__init__)


def test_imperativeocl::switchexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::instantiationexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::InstantiationExp)


def test_imperativeocl::instantiationexp_constructor_exists():
    assert callable(ImperativeOCL::InstantiationExp.__init__)


def test_imperativeocl::instantiationexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::computeexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ComputeExp)


def test_imperativeocl::computeexp_constructor_exists():
    assert callable(ImperativeOCL::ComputeExp.__init__)


def test_imperativeocl::computeexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::assignexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::AssignExp)


def test_imperativeocl::assignexp_constructor_exists():
    assert callable(ImperativeOCL::AssignExp.__init__)


def test_imperativeocl::assignexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::AssignExp.__init__)
    params = list(sig.parameters.keys())
    assert "isReset" in params, "Missing parameter 'isReset'"

def test_imperativeocl::assignexp_has_isReset():
    assert hasattr(ImperativeOCL::AssignExp, "isReset")
    descriptor = None
    for klass in ImperativeOCL::AssignExp.__mro__:
        if "isReset" in klass.__dict__:
            descriptor = klass.__dict__["isReset"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::logexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::LogExp)


def test_imperativeocl::logexp_constructor_exists():
    assert callable(ImperativeOCL::LogExp.__init__)


def test_imperativeocl::logexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::LogExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::assertexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::AssertExp)


def test_imperativeocl::assertexp_constructor_exists():
    assert callable(ImperativeOCL::AssertExp.__init__)


def test_imperativeocl::assertexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::AssertExp.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_imperativeocl::assertexp_has_severity():
    assert hasattr(ImperativeOCL::AssertExp, "severity")
    descriptor = None
    for klass in ImperativeOCL::AssertExp.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::blockexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::BlockExp)


def test_imperativeocl::blockexp_constructor_exists():
    assert callable(ImperativeOCL::BlockExp.__init__)


def test_imperativeocl::blockexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::returnexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ReturnExp)


def test_imperativeocl::returnexp_constructor_exists():
    assert callable(ImperativeOCL::ReturnExp.__init__)


def test_imperativeocl::returnexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::whileexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::WhileExp)


def test_imperativeocl::whileexp_constructor_exists():
    assert callable(ImperativeOCL::WhileExp.__init__)


def test_imperativeocl::whileexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::catchexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::CatchExp)


def test_imperativeocl::catchexp_constructor_exists():
    assert callable(ImperativeOCL::CatchExp.__init__)


def test_imperativeocl::catchexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::CatchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ImperativeLoopExp)


def test_imperativeocl::imperativeloopexp_constructor_exists():
    assert callable(ImperativeOCL::ImperativeLoopExp.__init__)


def test_imperativeocl::imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::altexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::AltExp)


def test_imperativeocl::altexp_constructor_exists():
    assert callable(ImperativeOCL::AltExp.__init__)


def test_imperativeocl::altexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::AltExp.__init__)
    params = list(sig.parameters.keys())



def test_logexp_is_not_abstract():
    assert not inspect.isabstract(LogExp)


def test_logexp_constructor_exists():
    assert callable(LogExp.__init__)


def test_logexp_constructor_args():
    sig = inspect.signature(LogExp.__init__)
    params = list(sig.parameters.keys())

def test_severitykind_exists():
    # Check that the Enumeration exists
    assert SeverityKind is not None

def test_severitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SeverityKind]
    expected_literals = [
        "error",
        "fatal",
        "warning",
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
CatchExp_strategy = st.builds(
    CatchExp,
)
AltExp_strategy = st.builds(
    AltExp,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
Operation_strategy = st.builds(
    Operation,
)
Class_strategy = st.builds(
    Class,
)
ImperativeOCL::Typedef_strategy = st.builds(
    ImperativeOCL::Typedef,
)
ImperativeLoopExp_strategy = st.builds(
    ImperativeLoopExp,
)
ImperativeOCL::ImperativeIterateExp_strategy = st.builds(
    ImperativeOCL::ImperativeIterateExp,
)
ImperativeOCL::ForExp_strategy = st.builds(
    ImperativeOCL::ForExp,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
ImperativeOCL::ListType_strategy = st.builds(
    ImperativeOCL::ListType,
)
ImperativeOCL::DictionaryType_strategy = st.builds(
    ImperativeOCL::DictionaryType,
)
DictLiteralExp_strategy = st.builds(
    DictLiteralExp,
)
Element_strategy = st.builds(
    Element,
)
ImperativeOCL::DictLiteralPart_strategy = st.builds(
    ImperativeOCL::DictLiteralPart,
)
DictLiteralPart_strategy = st.builds(
    DictLiteralPart,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
ImperativeOCL::ListLiteralExp_strategy = st.builds(
    ImperativeOCL::ListLiteralExp,
)
ImperativeOCL::DictLiteralExp_strategy = st.builds(
    ImperativeOCL::DictLiteralExp,
)
Type_strategy = st.builds(
    Type,
)
Variable_strategy = st.builds(
    Variable,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
ImperativeOCL::ImperativeExpression_strategy = st.builds(
    ImperativeOCL::ImperativeExpression,
)
ImperativeExpression_strategy = st.builds(
    ImperativeExpression,
)
ImperativeOCL::VariableInitExp_strategy = st.builds(
    ImperativeOCL::VariableInitExp,
    withResult=
        safe_text
)
ImperativeOCL::ContinueExp_strategy = st.builds(
    ImperativeOCL::ContinueExp,
)
ImperativeOCL::UnlinkExp_strategy = st.builds(
    ImperativeOCL::UnlinkExp,
)
ImperativeOCL::RaiseExp_strategy = st.builds(
    ImperativeOCL::RaiseExp,
)
ImperativeOCL::BreakExp_strategy = st.builds(
    ImperativeOCL::BreakExp,
)
ImperativeOCL::TryExp_strategy = st.builds(
    ImperativeOCL::TryExp,
)
ImperativeOCL::SwitchExp_strategy = st.builds(
    ImperativeOCL::SwitchExp,
)
ImperativeOCL::InstantiationExp_strategy = st.builds(
    ImperativeOCL::InstantiationExp,
)
ImperativeOCL::ComputeExp_strategy = st.builds(
    ImperativeOCL::ComputeExp,
)
ImperativeOCL::AssignExp_strategy = st.builds(
    ImperativeOCL::AssignExp,
    isReset=
        safe_text
)
ImperativeOCL::LogExp_strategy = st.builds(
    ImperativeOCL::LogExp,
)
ImperativeOCL::AssertExp_strategy = st.builds(
    ImperativeOCL::AssertExp,
    severity=
        safe_text
)
ImperativeOCL::BlockExp_strategy = st.builds(
    ImperativeOCL::BlockExp,
)
ImperativeOCL::ReturnExp_strategy = st.builds(
    ImperativeOCL::ReturnExp,
)
ImperativeOCL::WhileExp_strategy = st.builds(
    ImperativeOCL::WhileExp,
)
ImperativeOCL::CatchExp_strategy = st.builds(
    ImperativeOCL::CatchExp,
)
ImperativeOCL::ImperativeLoopExp_strategy = st.builds(
    ImperativeOCL::ImperativeLoopExp,
)
ImperativeOCL::AltExp_strategy = st.builds(
    ImperativeOCL::AltExp,
)
LogExp_strategy = st.builds(
    LogExp,
)

@given(instance=CatchExp_strategy)
@settings(max_examples=50)
def test_catchexp_instantiation(instance):
    assert isinstance(instance, CatchExp)

@given(instance=AltExp_strategy)
@settings(max_examples=50)
def test_altexp_instantiation(instance):
    assert isinstance(instance, AltExp)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=ImperativeOCL::Typedef_strategy)
@settings(max_examples=50)
def test_imperativeocl::typedef_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::Typedef)

@given(instance=ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExp)

@given(instance=ImperativeOCL::ImperativeIterateExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeiterateexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ImperativeIterateExp)

@given(instance=ImperativeOCL::ForExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::forexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ForExp)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=ImperativeOCL::ListType_strategy)
@settings(max_examples=50)
def test_imperativeocl::listtype_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ListType)

@given(instance=ImperativeOCL::DictionaryType_strategy)
@settings(max_examples=50)
def test_imperativeocl::dictionarytype_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::DictionaryType)

@given(instance=DictLiteralExp_strategy)
@settings(max_examples=50)
def test_dictliteralexp_instantiation(instance):
    assert isinstance(instance, DictLiteralExp)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=ImperativeOCL::DictLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl::dictliteralpart_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::DictLiteralPart)

@given(instance=DictLiteralPart_strategy)
@settings(max_examples=50)
def test_dictliteralpart_instantiation(instance):
    assert isinstance(instance, DictLiteralPart)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=ImperativeOCL::ListLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::listliteralexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ListLiteralExp)

@given(instance=ImperativeOCL::DictLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::dictliteralexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::DictLiteralExp)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=ImperativeOCL::ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ImperativeExpression)

@given(instance=ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeExpression)

@given(instance=ImperativeOCL::VariableInitExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::variableinitexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::VariableInitExp)

@given(instance=ImperativeOCL::VariableInitExp_strategy)
def test_imperativeocl::variableinitexp_withResult_type(instance):
    assert isinstance(instance.withResult, str)


@given(instance=ImperativeOCL::VariableInitExp_strategy)
def test_imperativeocl::variableinitexp_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=ImperativeOCL::ContinueExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::continueexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ContinueExp)

@given(instance=ImperativeOCL::UnlinkExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::unlinkexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::UnlinkExp)

@given(instance=ImperativeOCL::RaiseExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::raiseexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::RaiseExp)

@given(instance=ImperativeOCL::BreakExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::breakexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::BreakExp)

@given(instance=ImperativeOCL::TryExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::tryexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::TryExp)

@given(instance=ImperativeOCL::SwitchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::switchexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::SwitchExp)

@given(instance=ImperativeOCL::InstantiationExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::instantiationexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::InstantiationExp)

@given(instance=ImperativeOCL::ComputeExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::computeexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ComputeExp)

@given(instance=ImperativeOCL::AssignExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::assignexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::AssignExp)

@given(instance=ImperativeOCL::AssignExp_strategy)
def test_imperativeocl::assignexp_isReset_type(instance):
    assert isinstance(instance.isReset, str)


@given(instance=ImperativeOCL::AssignExp_strategy)
def test_imperativeocl::assignexp_isReset_setter(instance):
    original = instance.isReset
    instance.isReset = original
    assert instance.isReset == original

@given(instance=ImperativeOCL::LogExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::logexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::LogExp)

@given(instance=ImperativeOCL::AssertExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::assertexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::AssertExp)

@given(instance=ImperativeOCL::AssertExp_strategy)
def test_imperativeocl::assertexp_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=ImperativeOCL::AssertExp_strategy)
def test_imperativeocl::assertexp_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=ImperativeOCL::BlockExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::blockexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::BlockExp)

@given(instance=ImperativeOCL::ReturnExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::returnexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ReturnExp)

@given(instance=ImperativeOCL::WhileExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::whileexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::WhileExp)

@given(instance=ImperativeOCL::CatchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::catchexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::CatchExp)

@given(instance=ImperativeOCL::ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ImperativeLoopExp)

@given(instance=ImperativeOCL::AltExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::altexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::AltExp)

@given(instance=LogExp_strategy)
@settings(max_examples=50)
def test_logexp_instantiation(instance):
    assert isinstance(instance, LogExp)
