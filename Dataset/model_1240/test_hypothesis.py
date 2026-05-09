import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OperationCallExp,
    Type,
    imperativeocl::TemplateParameterType,
    Element,
    imperativeocl::OrderedTupleLiteralPart,
    imperativeocl::DictLiteralPart,
    LiteralExp,
    imperativeocl::OrderedTupleLiteralExp,
    imperativeocl::DictLiteralExp,
    OclExpression,
    imperativeocl::ImperativeExpression,
    LoopExp,
    imperativeocl::Type,
    CollectionType,
    imperativeocl::ListType,
    imperativeocl::DictionaryType,
    imperativeocl::Class,
    Class,
    imperativeocl::OrderedTupleType,
    imperativeocl::Typedef,
    ImperativeLoopExp,
    imperativeocl::ImperativeIterateExp,
    imperativeocl::ForExp,
    CallExp,
    imperativeocl::OclExpression,
    ImperativeExpression,
    imperativeocl::AltExp,
    imperativeocl::TryExp,
    imperativeocl::CatchExp,
    imperativeocl::UnpackExp,
    imperativeocl::UnlinkExp,
    imperativeocl::InstantiationExp,
    imperativeocl::BreakExp,
    imperativeocl::ReturnExp,
    imperativeocl::ImperativeLoopExp,
    imperativeocl::AssertExp,
    imperativeocl::LogExp,
    imperativeocl::RaiseExp,
    imperativeocl::SwitchExp,
    imperativeocl::ContinueExp,
    imperativeocl::BlockExp,
    imperativeocl::AssignExp,
    imperativeocl::ComputeExp,
    imperativeocl::WhileExp,
    imperativeocl::Variable,
    imperativeocl::VariableInitExp,
    SeverityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
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



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::orderedtupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::OrderedTupleLiteralPart)


def test_imperativeocl::orderedtupleliteralpart_constructor_exists():
    assert callable(imperativeocl::OrderedTupleLiteralPart.__init__)


def test_imperativeocl::orderedtupleliteralpart_constructor_args():
    sig = inspect.signature(imperativeocl::OrderedTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::DictLiteralPart)


def test_imperativeocl::dictliteralpart_constructor_exists():
    assert callable(imperativeocl::DictLiteralPart.__init__)


def test_imperativeocl::dictliteralpart_constructor_args():
    sig = inspect.signature(imperativeocl::DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::orderedtupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::OrderedTupleLiteralExp)


def test_imperativeocl::orderedtupleliteralexp_constructor_exists():
    assert callable(imperativeocl::OrderedTupleLiteralExp.__init__)


def test_imperativeocl::orderedtupleliteralexp_constructor_args():
    sig = inspect.signature(imperativeocl::OrderedTupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::DictLiteralExp)


def test_imperativeocl::dictliteralexp_constructor_exists():
    assert callable(imperativeocl::DictLiteralExp.__init__)


def test_imperativeocl::dictliteralexp_constructor_args():
    sig = inspect.signature(imperativeocl::DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ImperativeExpression)


def test_imperativeocl::imperativeexpression_constructor_exists():
    assert callable(imperativeocl::ImperativeExpression.__init__)


def test_imperativeocl::imperativeexpression_constructor_args():
    sig = inspect.signature(imperativeocl::ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::type_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::Type)


def test_imperativeocl::type_constructor_exists():
    assert callable(imperativeocl::Type.__init__)


def test_imperativeocl::type_constructor_args():
    sig = inspect.signature(imperativeocl::Type.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::listtype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ListType)


def test_imperativeocl::listtype_constructor_exists():
    assert callable(imperativeocl::ListType.__init__)


def test_imperativeocl::listtype_constructor_args():
    sig = inspect.signature(imperativeocl::ListType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::dictionarytype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::DictionaryType)


def test_imperativeocl::dictionarytype_constructor_exists():
    assert callable(imperativeocl::DictionaryType.__init__)


def test_imperativeocl::dictionarytype_constructor_args():
    sig = inspect.signature(imperativeocl::DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::class_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::Class)


def test_imperativeocl::class_constructor_exists():
    assert callable(imperativeocl::Class.__init__)


def test_imperativeocl::class_constructor_args():
    sig = inspect.signature(imperativeocl::Class.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::orderedtupletype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::OrderedTupleType)


def test_imperativeocl::orderedtupletype_constructor_exists():
    assert callable(imperativeocl::OrderedTupleType.__init__)


def test_imperativeocl::orderedtupletype_constructor_args():
    sig = inspect.signature(imperativeocl::OrderedTupleType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::typedef_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::Typedef)


def test_imperativeocl::typedef_constructor_exists():
    assert callable(imperativeocl::Typedef.__init__)


def test_imperativeocl::typedef_constructor_args():
    sig = inspect.signature(imperativeocl::Typedef.__init__)
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



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::OclExpression)


def test_imperativeocl::oclexpression_constructor_exists():
    assert callable(imperativeocl::OclExpression.__init__)


def test_imperativeocl::oclexpression_constructor_args():
    sig = inspect.signature(imperativeocl::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeExpression)


def test_imperativeexpression_constructor_exists():
    assert callable(ImperativeExpression.__init__)


def test_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::altexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::AltExp)


def test_imperativeocl::altexp_constructor_exists():
    assert callable(imperativeocl::AltExp.__init__)


def test_imperativeocl::altexp_constructor_args():
    sig = inspect.signature(imperativeocl::AltExp.__init__)
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



def test_imperativeocl::unpackexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::UnpackExp)


def test_imperativeocl::unpackexp_constructor_exists():
    assert callable(imperativeocl::UnpackExp.__init__)


def test_imperativeocl::unpackexp_constructor_args():
    sig = inspect.signature(imperativeocl::UnpackExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::unlinkexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::UnlinkExp)


def test_imperativeocl::unlinkexp_constructor_exists():
    assert callable(imperativeocl::UnlinkExp.__init__)


def test_imperativeocl::unlinkexp_constructor_args():
    sig = inspect.signature(imperativeocl::UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::instantiationexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::InstantiationExp)


def test_imperativeocl::instantiationexp_constructor_exists():
    assert callable(imperativeocl::InstantiationExp.__init__)


def test_imperativeocl::instantiationexp_constructor_args():
    sig = inspect.signature(imperativeocl::InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::breakexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::BreakExp)


def test_imperativeocl::breakexp_constructor_exists():
    assert callable(imperativeocl::BreakExp.__init__)


def test_imperativeocl::breakexp_constructor_args():
    sig = inspect.signature(imperativeocl::BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::returnexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ReturnExp)


def test_imperativeocl::returnexp_constructor_exists():
    assert callable(imperativeocl::ReturnExp.__init__)


def test_imperativeocl::returnexp_constructor_args():
    sig = inspect.signature(imperativeocl::ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ImperativeLoopExp)


def test_imperativeocl::imperativeloopexp_constructor_exists():
    assert callable(imperativeocl::ImperativeLoopExp.__init__)


def test_imperativeocl::imperativeloopexp_constructor_args():
    sig = inspect.signature(imperativeocl::ImperativeLoopExp.__init__)
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



def test_imperativeocl::logexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::LogExp)


def test_imperativeocl::logexp_constructor_exists():
    assert callable(imperativeocl::LogExp.__init__)


def test_imperativeocl::logexp_constructor_args():
    sig = inspect.signature(imperativeocl::LogExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::raiseexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::RaiseExp)


def test_imperativeocl::raiseexp_constructor_exists():
    assert callable(imperativeocl::RaiseExp.__init__)


def test_imperativeocl::raiseexp_constructor_args():
    sig = inspect.signature(imperativeocl::RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::switchexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::SwitchExp)


def test_imperativeocl::switchexp_constructor_exists():
    assert callable(imperativeocl::SwitchExp.__init__)


def test_imperativeocl::switchexp_constructor_args():
    sig = inspect.signature(imperativeocl::SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::continueexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ContinueExp)


def test_imperativeocl::continueexp_constructor_exists():
    assert callable(imperativeocl::ContinueExp.__init__)


def test_imperativeocl::continueexp_constructor_args():
    sig = inspect.signature(imperativeocl::ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::blockexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::BlockExp)


def test_imperativeocl::blockexp_constructor_exists():
    assert callable(imperativeocl::BlockExp.__init__)


def test_imperativeocl::blockexp_constructor_args():
    sig = inspect.signature(imperativeocl::BlockExp.__init__)
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



def test_imperativeocl::computeexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ComputeExp)


def test_imperativeocl::computeexp_constructor_exists():
    assert callable(imperativeocl::ComputeExp.__init__)


def test_imperativeocl::computeexp_constructor_args():
    sig = inspect.signature(imperativeocl::ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::whileexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::WhileExp)


def test_imperativeocl::whileexp_constructor_exists():
    assert callable(imperativeocl::WhileExp.__init__)


def test_imperativeocl::whileexp_constructor_args():
    sig = inspect.signature(imperativeocl::WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::variable_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::Variable)


def test_imperativeocl::variable_constructor_exists():
    assert callable(imperativeocl::Variable.__init__)


def test_imperativeocl::variable_constructor_args():
    sig = inspect.signature(imperativeocl::Variable.__init__)
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
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
Type_strategy = st.builds(
    Type,
)
imperativeocl::TemplateParameterType_strategy = st.builds(
    imperativeocl::TemplateParameterType,
    specification=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
imperativeocl::OrderedTupleLiteralPart_strategy = st.builds(
    imperativeocl::OrderedTupleLiteralPart,
)
imperativeocl::DictLiteralPart_strategy = st.builds(
    imperativeocl::DictLiteralPart,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
imperativeocl::OrderedTupleLiteralExp_strategy = st.builds(
    imperativeocl::OrderedTupleLiteralExp,
)
imperativeocl::DictLiteralExp_strategy = st.builds(
    imperativeocl::DictLiteralExp,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
imperativeocl::ImperativeExpression_strategy = st.builds(
    imperativeocl::ImperativeExpression,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
imperativeocl::Type_strategy = st.builds(
    imperativeocl::Type,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
imperativeocl::ListType_strategy = st.builds(
    imperativeocl::ListType,
)
imperativeocl::DictionaryType_strategy = st.builds(
    imperativeocl::DictionaryType,
)
imperativeocl::Class_strategy = st.builds(
    imperativeocl::Class,
)
Class_strategy = st.builds(
    Class,
)
imperativeocl::OrderedTupleType_strategy = st.builds(
    imperativeocl::OrderedTupleType,
)
imperativeocl::Typedef_strategy = st.builds(
    imperativeocl::Typedef,
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
CallExp_strategy = st.builds(
    CallExp,
)
imperativeocl::OclExpression_strategy = st.builds(
    imperativeocl::OclExpression,
)
ImperativeExpression_strategy = st.builds(
    ImperativeExpression,
)
imperativeocl::AltExp_strategy = st.builds(
    imperativeocl::AltExp,
)
imperativeocl::TryExp_strategy = st.builds(
    imperativeocl::TryExp,
)
imperativeocl::CatchExp_strategy = st.builds(
    imperativeocl::CatchExp,
)
imperativeocl::UnpackExp_strategy = st.builds(
    imperativeocl::UnpackExp,
)
imperativeocl::UnlinkExp_strategy = st.builds(
    imperativeocl::UnlinkExp,
)
imperativeocl::InstantiationExp_strategy = st.builds(
    imperativeocl::InstantiationExp,
)
imperativeocl::BreakExp_strategy = st.builds(
    imperativeocl::BreakExp,
)
imperativeocl::ReturnExp_strategy = st.builds(
    imperativeocl::ReturnExp,
)
imperativeocl::ImperativeLoopExp_strategy = st.builds(
    imperativeocl::ImperativeLoopExp,
)
imperativeocl::AssertExp_strategy = st.builds(
    imperativeocl::AssertExp,
    severity=
        safe_text
)
imperativeocl::LogExp_strategy = st.builds(
    imperativeocl::LogExp,
)
imperativeocl::RaiseExp_strategy = st.builds(
    imperativeocl::RaiseExp,
)
imperativeocl::SwitchExp_strategy = st.builds(
    imperativeocl::SwitchExp,
)
imperativeocl::ContinueExp_strategy = st.builds(
    imperativeocl::ContinueExp,
)
imperativeocl::BlockExp_strategy = st.builds(
    imperativeocl::BlockExp,
)
imperativeocl::AssignExp_strategy = st.builds(
    imperativeocl::AssignExp,
    isReset=
        safe_text
)
imperativeocl::ComputeExp_strategy = st.builds(
    imperativeocl::ComputeExp,
)
imperativeocl::WhileExp_strategy = st.builds(
    imperativeocl::WhileExp,
)
imperativeocl::Variable_strategy = st.builds(
    imperativeocl::Variable,
)
imperativeocl::VariableInitExp_strategy = st.builds(
    imperativeocl::VariableInitExp,
    withResult=
        safe_text
)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

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

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=imperativeocl::OrderedTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl::orderedtupleliteralpart_instantiation(instance):
    assert isinstance(instance, imperativeocl::OrderedTupleLiteralPart)

@given(instance=imperativeocl::DictLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl::dictliteralpart_instantiation(instance):
    assert isinstance(instance, imperativeocl::DictLiteralPart)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=imperativeocl::OrderedTupleLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::orderedtupleliteralexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::OrderedTupleLiteralExp)

@given(instance=imperativeocl::DictLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::dictliteralexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::DictLiteralExp)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=imperativeocl::ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeexpression_instantiation(instance):
    assert isinstance(instance, imperativeocl::ImperativeExpression)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=imperativeocl::Type_strategy)
@settings(max_examples=50)
def test_imperativeocl::type_instantiation(instance):
    assert isinstance(instance, imperativeocl::Type)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=imperativeocl::ListType_strategy)
@settings(max_examples=50)
def test_imperativeocl::listtype_instantiation(instance):
    assert isinstance(instance, imperativeocl::ListType)

@given(instance=imperativeocl::DictionaryType_strategy)
@settings(max_examples=50)
def test_imperativeocl::dictionarytype_instantiation(instance):
    assert isinstance(instance, imperativeocl::DictionaryType)

@given(instance=imperativeocl::Class_strategy)
@settings(max_examples=50)
def test_imperativeocl::class_instantiation(instance):
    assert isinstance(instance, imperativeocl::Class)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=imperativeocl::OrderedTupleType_strategy)
@settings(max_examples=50)
def test_imperativeocl::orderedtupletype_instantiation(instance):
    assert isinstance(instance, imperativeocl::OrderedTupleType)

@given(instance=imperativeocl::Typedef_strategy)
@settings(max_examples=50)
def test_imperativeocl::typedef_instantiation(instance):
    assert isinstance(instance, imperativeocl::Typedef)

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

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=imperativeocl::OclExpression_strategy)
@settings(max_examples=50)
def test_imperativeocl::oclexpression_instantiation(instance):
    assert isinstance(instance, imperativeocl::OclExpression)

@given(instance=ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeExpression)

@given(instance=imperativeocl::AltExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::altexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::AltExp)

@given(instance=imperativeocl::TryExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::tryexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::TryExp)

@given(instance=imperativeocl::CatchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::catchexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::CatchExp)

@given(instance=imperativeocl::UnpackExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::unpackexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::UnpackExp)

@given(instance=imperativeocl::UnlinkExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::unlinkexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::UnlinkExp)

@given(instance=imperativeocl::InstantiationExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::instantiationexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::InstantiationExp)

@given(instance=imperativeocl::BreakExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::breakexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::BreakExp)

@given(instance=imperativeocl::ReturnExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::returnexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ReturnExp)

@given(instance=imperativeocl::ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeloopexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ImperativeLoopExp)

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

@given(instance=imperativeocl::LogExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::logexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::LogExp)

@given(instance=imperativeocl::RaiseExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::raiseexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::RaiseExp)

@given(instance=imperativeocl::SwitchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::switchexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::SwitchExp)

@given(instance=imperativeocl::ContinueExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::continueexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ContinueExp)

@given(instance=imperativeocl::BlockExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::blockexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::BlockExp)

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

@given(instance=imperativeocl::ComputeExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::computeexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ComputeExp)

@given(instance=imperativeocl::WhileExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::whileexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::WhileExp)

@given(instance=imperativeocl::Variable_strategy)
@settings(max_examples=50)
def test_imperativeocl::variable_instantiation(instance):
    assert isinstance(instance, imperativeocl::Variable)

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
