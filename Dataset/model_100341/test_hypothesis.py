import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Constant,
    AsmL::StringConstant,
    AsmL::NullConstant,
    AsmL::IntegerConstant,
    AsmL::BooleanConstant,
    SequenceTerm,
    AsmL::RangeSequence,
    AsmL::EnumerateSequence,
    SetTerm,
    AsmL::RangeSet,
    AsmL::AlgorithmSet,
    AsmL::EnumerateSet,
    PredicateTerm,
    AsmL::ExistsTerm,
    AsmL::AnyIn,
    AsmL::ForAllTerm,
    ConditionalRule,
    AsmL::ElseIf,
    ElseIf,
    UpdateRule,
    AsmL::UpdateMapRule,
    AsmL::UpdateFieldRule,
    AsmL::UpdateVarRule,
    MethodCallTerm,
    AsmL::NewInstance,
    InWhereHolds,
    StepExpression,
    AsmL::StepUntil,
    AsmL::StepWhile,
    Step,
    AsmL::StepExpression,
    AsmL::StepForEach,
    AsmL::StepUntilFixPoint,
    Method,
    VarTerm,
    Initially,
    Body,
    Parameter,
    Function,
    AsmL::Main,
    Class,
    Enumerator,
    Structure,
    VarDeclaration,
    Type,
    AsmL::SequenceType,
    AsmL::TupletType,
    AsmL::NamedType,
    AsmL::SetType,
    AsmL::MapType,
    VarOrMethod,
    AsmL::Method,
    VarOrCase,
    AsmL::Case,
    AsmLFile,
    Main,
    AsmLElement,
    AsmL::Class,
    AsmL::Function,
    AsmL::Structure,
    AsmL::VarDeclaration,
    AsmL::Type,
    AsmL::Namespace,
    AsmL::Enumeration,
    Term,
    AsmL::VarTerm,
    AsmL::SequenceTerm,
    AsmL::TulpletTerm,
    AsmL::PredicateTerm,
    AsmL::Constant,
    AsmL::SetTerm,
    AsmL::MapTerm,
    AsmL::Operator,
    AsmL::MethodCallTerm,
    Rule,
    AsmL::RemoveRule,
    AsmL::MethodInvocation,
    AsmL::ReturnRule,
    AsmL::ConditionalRule,
    AsmL::AddRule,
    AsmL::ChooseRule,
    AsmL::ForallRule,
    AsmL::UpdateRule,
    AsmL::SkipRule,
    AsmL::Step,
    LocatedElement,
    AsmL::VarOrCase,
    AsmL::AsmLFile,
    AsmL::InWhereHolds,
    AsmL::Initially,
    AsmL::Enumerator,
    AsmL::Term,
    AsmL::Rule,
    AsmL::VarOrMethod,
    AsmL::AsmLElement,
    AsmL::Parameter,
    AsmL::Body,
    AsmL::LocatedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_constant_is_not_abstract():
    assert not inspect.isabstract(Constant)


def test_constant_constructor_exists():
    assert callable(Constant.__init__)


def test_constant_constructor_args():
    sig = inspect.signature(Constant.__init__)
    params = list(sig.parameters.keys())



def test_asml::stringconstant_is_not_abstract():
    assert not inspect.isabstract(AsmL::StringConstant)


def test_asml::stringconstant_constructor_exists():
    assert callable(AsmL::StringConstant.__init__)


def test_asml::stringconstant_constructor_args():
    sig = inspect.signature(AsmL::StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_asml::stringconstant_has_val():
    assert hasattr(AsmL::StringConstant, "val")
    descriptor = None
    for klass in AsmL::StringConstant.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_asml::nullconstant_is_not_abstract():
    assert not inspect.isabstract(AsmL::NullConstant)


def test_asml::nullconstant_constructor_exists():
    assert callable(AsmL::NullConstant.__init__)


def test_asml::nullconstant_constructor_args():
    sig = inspect.signature(AsmL::NullConstant.__init__)
    params = list(sig.parameters.keys())



def test_asml::integerconstant_is_not_abstract():
    assert not inspect.isabstract(AsmL::IntegerConstant)


def test_asml::integerconstant_constructor_exists():
    assert callable(AsmL::IntegerConstant.__init__)


def test_asml::integerconstant_constructor_args():
    sig = inspect.signature(AsmL::IntegerConstant.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_asml::integerconstant_has_val():
    assert hasattr(AsmL::IntegerConstant, "val")
    descriptor = None
    for klass in AsmL::IntegerConstant.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_asml::booleanconstant_is_not_abstract():
    assert not inspect.isabstract(AsmL::BooleanConstant)


def test_asml::booleanconstant_constructor_exists():
    assert callable(AsmL::BooleanConstant.__init__)


def test_asml::booleanconstant_constructor_args():
    sig = inspect.signature(AsmL::BooleanConstant.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_asml::booleanconstant_has_val():
    assert hasattr(AsmL::BooleanConstant, "val")
    descriptor = None
    for klass in AsmL::BooleanConstant.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_sequenceterm_is_not_abstract():
    assert not inspect.isabstract(SequenceTerm)


def test_sequenceterm_constructor_exists():
    assert callable(SequenceTerm.__init__)


def test_sequenceterm_constructor_args():
    sig = inspect.signature(SequenceTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml::rangesequence_is_not_abstract():
    assert not inspect.isabstract(AsmL::RangeSequence)


def test_asml::rangesequence_constructor_exists():
    assert callable(AsmL::RangeSequence.__init__)


def test_asml::rangesequence_constructor_args():
    sig = inspect.signature(AsmL::RangeSequence.__init__)
    params = list(sig.parameters.keys())



def test_asml::enumeratesequence_is_not_abstract():
    assert not inspect.isabstract(AsmL::EnumerateSequence)


def test_asml::enumeratesequence_constructor_exists():
    assert callable(AsmL::EnumerateSequence.__init__)


def test_asml::enumeratesequence_constructor_args():
    sig = inspect.signature(AsmL::EnumerateSequence.__init__)
    params = list(sig.parameters.keys())



def test_setterm_is_not_abstract():
    assert not inspect.isabstract(SetTerm)


def test_setterm_constructor_exists():
    assert callable(SetTerm.__init__)


def test_setterm_constructor_args():
    sig = inspect.signature(SetTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml::rangeset_is_not_abstract():
    assert not inspect.isabstract(AsmL::RangeSet)


def test_asml::rangeset_constructor_exists():
    assert callable(AsmL::RangeSet.__init__)


def test_asml::rangeset_constructor_args():
    sig = inspect.signature(AsmL::RangeSet.__init__)
    params = list(sig.parameters.keys())



def test_asml::algorithmset_is_not_abstract():
    assert not inspect.isabstract(AsmL::AlgorithmSet)


def test_asml::algorithmset_constructor_exists():
    assert callable(AsmL::AlgorithmSet.__init__)


def test_asml::algorithmset_constructor_args():
    sig = inspect.signature(AsmL::AlgorithmSet.__init__)
    params = list(sig.parameters.keys())



def test_asml::enumerateset_is_not_abstract():
    assert not inspect.isabstract(AsmL::EnumerateSet)


def test_asml::enumerateset_constructor_exists():
    assert callable(AsmL::EnumerateSet.__init__)


def test_asml::enumerateset_constructor_args():
    sig = inspect.signature(AsmL::EnumerateSet.__init__)
    params = list(sig.parameters.keys())



def test_predicateterm_is_not_abstract():
    assert not inspect.isabstract(PredicateTerm)


def test_predicateterm_constructor_exists():
    assert callable(PredicateTerm.__init__)


def test_predicateterm_constructor_args():
    sig = inspect.signature(PredicateTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml::existsterm_is_not_abstract():
    assert not inspect.isabstract(AsmL::ExistsTerm)


def test_asml::existsterm_constructor_exists():
    assert callable(AsmL::ExistsTerm.__init__)


def test_asml::existsterm_constructor_args():
    sig = inspect.signature(AsmL::ExistsTerm.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_asml::existsterm_has_isUnique():
    assert hasattr(AsmL::ExistsTerm, "isUnique")
    descriptor = None
    for klass in AsmL::ExistsTerm.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_asml::anyin_is_not_abstract():
    assert not inspect.isabstract(AsmL::AnyIn)


def test_asml::anyin_constructor_exists():
    assert callable(AsmL::AnyIn.__init__)


def test_asml::anyin_constructor_args():
    sig = inspect.signature(AsmL::AnyIn.__init__)
    params = list(sig.parameters.keys())



def test_asml::forallterm_is_not_abstract():
    assert not inspect.isabstract(AsmL::ForAllTerm)


def test_asml::forallterm_constructor_exists():
    assert callable(AsmL::ForAllTerm.__init__)


def test_asml::forallterm_constructor_args():
    sig = inspect.signature(AsmL::ForAllTerm.__init__)
    params = list(sig.parameters.keys())



def test_conditionalrule_is_not_abstract():
    assert not inspect.isabstract(ConditionalRule)


def test_conditionalrule_constructor_exists():
    assert callable(ConditionalRule.__init__)


def test_conditionalrule_constructor_args():
    sig = inspect.signature(ConditionalRule.__init__)
    params = list(sig.parameters.keys())



def test_asml::elseif_is_not_abstract():
    assert not inspect.isabstract(AsmL::ElseIf)


def test_asml::elseif_constructor_exists():
    assert callable(AsmL::ElseIf.__init__)


def test_asml::elseif_constructor_args():
    sig = inspect.signature(AsmL::ElseIf.__init__)
    params = list(sig.parameters.keys())



def test_elseif_is_not_abstract():
    assert not inspect.isabstract(ElseIf)


def test_elseif_constructor_exists():
    assert callable(ElseIf.__init__)


def test_elseif_constructor_args():
    sig = inspect.signature(ElseIf.__init__)
    params = list(sig.parameters.keys())



def test_updaterule_is_not_abstract():
    assert not inspect.isabstract(UpdateRule)


def test_updaterule_constructor_exists():
    assert callable(UpdateRule.__init__)


def test_updaterule_constructor_args():
    sig = inspect.signature(UpdateRule.__init__)
    params = list(sig.parameters.keys())



def test_asml::updatemaprule_is_not_abstract():
    assert not inspect.isabstract(AsmL::UpdateMapRule)


def test_asml::updatemaprule_constructor_exists():
    assert callable(AsmL::UpdateMapRule.__init__)


def test_asml::updatemaprule_constructor_args():
    sig = inspect.signature(AsmL::UpdateMapRule.__init__)
    params = list(sig.parameters.keys())



def test_asml::updatefieldrule_is_not_abstract():
    assert not inspect.isabstract(AsmL::UpdateFieldRule)


def test_asml::updatefieldrule_constructor_exists():
    assert callable(AsmL::UpdateFieldRule.__init__)


def test_asml::updatefieldrule_constructor_args():
    sig = inspect.signature(AsmL::UpdateFieldRule.__init__)
    params = list(sig.parameters.keys())



def test_asml::updatevarrule_is_not_abstract():
    assert not inspect.isabstract(AsmL::UpdateVarRule)


def test_asml::updatevarrule_constructor_exists():
    assert callable(AsmL::UpdateVarRule.__init__)


def test_asml::updatevarrule_constructor_args():
    sig = inspect.signature(AsmL::UpdateVarRule.__init__)
    params = list(sig.parameters.keys())



def test_methodcallterm_is_not_abstract():
    assert not inspect.isabstract(MethodCallTerm)


def test_methodcallterm_constructor_exists():
    assert callable(MethodCallTerm.__init__)


def test_methodcallterm_constructor_args():
    sig = inspect.signature(MethodCallTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml::newinstance_is_not_abstract():
    assert not inspect.isabstract(AsmL::NewInstance)


def test_asml::newinstance_constructor_exists():
    assert callable(AsmL::NewInstance.__init__)


def test_asml::newinstance_constructor_args():
    sig = inspect.signature(AsmL::NewInstance.__init__)
    params = list(sig.parameters.keys())



def test_inwhereholds_is_not_abstract():
    assert not inspect.isabstract(InWhereHolds)


def test_inwhereholds_constructor_exists():
    assert callable(InWhereHolds.__init__)


def test_inwhereholds_constructor_args():
    sig = inspect.signature(InWhereHolds.__init__)
    params = list(sig.parameters.keys())



def test_stepexpression_is_not_abstract():
    assert not inspect.isabstract(StepExpression)


def test_stepexpression_constructor_exists():
    assert callable(StepExpression.__init__)


def test_stepexpression_constructor_args():
    sig = inspect.signature(StepExpression.__init__)
    params = list(sig.parameters.keys())



def test_asml::stepuntil_is_not_abstract():
    assert not inspect.isabstract(AsmL::StepUntil)


def test_asml::stepuntil_constructor_exists():
    assert callable(AsmL::StepUntil.__init__)


def test_asml::stepuntil_constructor_args():
    sig = inspect.signature(AsmL::StepUntil.__init__)
    params = list(sig.parameters.keys())



def test_asml::stepwhile_is_not_abstract():
    assert not inspect.isabstract(AsmL::StepWhile)


def test_asml::stepwhile_constructor_exists():
    assert callable(AsmL::StepWhile.__init__)


def test_asml::stepwhile_constructor_args():
    sig = inspect.signature(AsmL::StepWhile.__init__)
    params = list(sig.parameters.keys())



def test_step_is_not_abstract():
    assert not inspect.isabstract(Step)


def test_step_constructor_exists():
    assert callable(Step.__init__)


def test_step_constructor_args():
    sig = inspect.signature(Step.__init__)
    params = list(sig.parameters.keys())



def test_asml::stepexpression_is_not_abstract():
    assert not inspect.isabstract(AsmL::StepExpression)


def test_asml::stepexpression_constructor_exists():
    assert callable(AsmL::StepExpression.__init__)


def test_asml::stepexpression_constructor_args():
    sig = inspect.signature(AsmL::StepExpression.__init__)
    params = list(sig.parameters.keys())



def test_asml::stepforeach_is_not_abstract():
    assert not inspect.isabstract(AsmL::StepForEach)


def test_asml::stepforeach_constructor_exists():
    assert callable(AsmL::StepForEach.__init__)


def test_asml::stepforeach_constructor_args():
    sig = inspect.signature(AsmL::StepForEach.__init__)
    params = list(sig.parameters.keys())



def test_asml::stepuntilfixpoint_is_not_abstract():
    assert not inspect.isabstract(AsmL::StepUntilFixPoint)


def test_asml::stepuntilfixpoint_constructor_exists():
    assert callable(AsmL::StepUntilFixPoint.__init__)


def test_asml::stepuntilfixpoint_constructor_args():
    sig = inspect.signature(AsmL::StepUntilFixPoint.__init__)
    params = list(sig.parameters.keys())



def test_method_is_not_abstract():
    assert not inspect.isabstract(Method)


def test_method_constructor_exists():
    assert callable(Method.__init__)


def test_method_constructor_args():
    sig = inspect.signature(Method.__init__)
    params = list(sig.parameters.keys())



def test_varterm_is_not_abstract():
    assert not inspect.isabstract(VarTerm)


def test_varterm_constructor_exists():
    assert callable(VarTerm.__init__)


def test_varterm_constructor_args():
    sig = inspect.signature(VarTerm.__init__)
    params = list(sig.parameters.keys())



def test_initially_is_not_abstract():
    assert not inspect.isabstract(Initially)


def test_initially_constructor_exists():
    assert callable(Initially.__init__)


def test_initially_constructor_args():
    sig = inspect.signature(Initially.__init__)
    params = list(sig.parameters.keys())



def test_body_is_not_abstract():
    assert not inspect.isabstract(Body)


def test_body_constructor_exists():
    assert callable(Body.__init__)


def test_body_constructor_args():
    sig = inspect.signature(Body.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_asml::main_is_not_abstract():
    assert not inspect.isabstract(AsmL::Main)


def test_asml::main_constructor_exists():
    assert callable(AsmL::Main.__init__)


def test_asml::main_constructor_args():
    sig = inspect.signature(AsmL::Main.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_enumerator_is_not_abstract():
    assert not inspect.isabstract(Enumerator)


def test_enumerator_constructor_exists():
    assert callable(Enumerator.__init__)


def test_enumerator_constructor_args():
    sig = inspect.signature(Enumerator.__init__)
    params = list(sig.parameters.keys())



def test_structure_is_not_abstract():
    assert not inspect.isabstract(Structure)


def test_structure_constructor_exists():
    assert callable(Structure.__init__)


def test_structure_constructor_args():
    sig = inspect.signature(Structure.__init__)
    params = list(sig.parameters.keys())



def test_vardeclaration_is_not_abstract():
    assert not inspect.isabstract(VarDeclaration)


def test_vardeclaration_constructor_exists():
    assert callable(VarDeclaration.__init__)


def test_vardeclaration_constructor_args():
    sig = inspect.signature(VarDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_asml::sequencetype_is_not_abstract():
    assert not inspect.isabstract(AsmL::SequenceType)


def test_asml::sequencetype_constructor_exists():
    assert callable(AsmL::SequenceType.__init__)


def test_asml::sequencetype_constructor_args():
    sig = inspect.signature(AsmL::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_asml::tuplettype_is_not_abstract():
    assert not inspect.isabstract(AsmL::TupletType)


def test_asml::tuplettype_constructor_exists():
    assert callable(AsmL::TupletType.__init__)


def test_asml::tuplettype_constructor_args():
    sig = inspect.signature(AsmL::TupletType.__init__)
    params = list(sig.parameters.keys())



def test_asml::namedtype_is_not_abstract():
    assert not inspect.isabstract(AsmL::NamedType)


def test_asml::namedtype_constructor_exists():
    assert callable(AsmL::NamedType.__init__)


def test_asml::namedtype_constructor_args():
    sig = inspect.signature(AsmL::NamedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml::namedtype_has_name():
    assert hasattr(AsmL::NamedType, "name")
    descriptor = None
    for klass in AsmL::NamedType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asml::settype_is_not_abstract():
    assert not inspect.isabstract(AsmL::SetType)


def test_asml::settype_constructor_exists():
    assert callable(AsmL::SetType.__init__)


def test_asml::settype_constructor_args():
    sig = inspect.signature(AsmL::SetType.__init__)
    params = list(sig.parameters.keys())



def test_asml::maptype_is_not_abstract():
    assert not inspect.isabstract(AsmL::MapType)


def test_asml::maptype_constructor_exists():
    assert callable(AsmL::MapType.__init__)


def test_asml::maptype_constructor_args():
    sig = inspect.signature(AsmL::MapType.__init__)
    params = list(sig.parameters.keys())



def test_varormethod_is_not_abstract():
    assert not inspect.isabstract(VarOrMethod)


def test_varormethod_constructor_exists():
    assert callable(VarOrMethod.__init__)


def test_varormethod_constructor_args():
    sig = inspect.signature(VarOrMethod.__init__)
    params = list(sig.parameters.keys())



def test_asml::method_is_not_abstract():
    assert not inspect.isabstract(AsmL::Method)


def test_asml::method_constructor_exists():
    assert callable(AsmL::Method.__init__)


def test_asml::method_constructor_args():
    sig = inspect.signature(AsmL::Method.__init__)
    params = list(sig.parameters.keys())
    assert "isOverride" in params, "Missing parameter 'isOverride'"
    assert "isShared" in params, "Missing parameter 'isShared'"
    assert "isEntryPoint" in params, "Missing parameter 'isEntryPoint'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_asml::method_has_isOverride():
    assert hasattr(AsmL::Method, "isOverride")
    descriptor = None
    for klass in AsmL::Method.__mro__:
        if "isOverride" in klass.__dict__:
            descriptor = klass.__dict__["isOverride"]
            break
    assert isinstance(descriptor, property)

def test_asml::method_has_isShared():
    assert hasattr(AsmL::Method, "isShared")
    descriptor = None
    for klass in AsmL::Method.__mro__:
        if "isShared" in klass.__dict__:
            descriptor = klass.__dict__["isShared"]
            break
    assert isinstance(descriptor, property)

def test_asml::method_has_isEntryPoint():
    assert hasattr(AsmL::Method, "isEntryPoint")
    descriptor = None
    for klass in AsmL::Method.__mro__:
        if "isEntryPoint" in klass.__dict__:
            descriptor = klass.__dict__["isEntryPoint"]
            break
    assert isinstance(descriptor, property)

def test_asml::method_has_isAbstract():
    assert hasattr(AsmL::Method, "isAbstract")
    descriptor = None
    for klass in AsmL::Method.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_varorcase_is_not_abstract():
    assert not inspect.isabstract(VarOrCase)


def test_varorcase_constructor_exists():
    assert callable(VarOrCase.__init__)


def test_varorcase_constructor_args():
    sig = inspect.signature(VarOrCase.__init__)
    params = list(sig.parameters.keys())



def test_asml::case_is_not_abstract():
    assert not inspect.isabstract(AsmL::Case)


def test_asml::case_constructor_exists():
    assert callable(AsmL::Case.__init__)


def test_asml::case_constructor_args():
    sig = inspect.signature(AsmL::Case.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml::case_has_name():
    assert hasattr(AsmL::Case, "name")
    descriptor = None
    for klass in AsmL::Case.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asmlfile_is_not_abstract():
    assert not inspect.isabstract(AsmLFile)


def test_asmlfile_constructor_exists():
    assert callable(AsmLFile.__init__)


def test_asmlfile_constructor_args():
    sig = inspect.signature(AsmLFile.__init__)
    params = list(sig.parameters.keys())



def test_main_is_not_abstract():
    assert not inspect.isabstract(Main)


def test_main_constructor_exists():
    assert callable(Main.__init__)


def test_main_constructor_args():
    sig = inspect.signature(Main.__init__)
    params = list(sig.parameters.keys())



def test_asmlelement_is_not_abstract():
    assert not inspect.isabstract(AsmLElement)


def test_asmlelement_constructor_exists():
    assert callable(AsmLElement.__init__)


def test_asmlelement_constructor_args():
    sig = inspect.signature(AsmLElement.__init__)
    params = list(sig.parameters.keys())



def test_asml::class_is_not_abstract():
    assert not inspect.isabstract(AsmL::Class)


def test_asml::class_constructor_exists():
    assert callable(AsmL::Class.__init__)


def test_asml::class_constructor_args():
    sig = inspect.signature(AsmL::Class.__init__)
    params = list(sig.parameters.keys())
    assert "superClassName" in params, "Missing parameter 'superClassName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_asml::class_has_superClassName():
    assert hasattr(AsmL::Class, "superClassName")
    descriptor = None
    for klass in AsmL::Class.__mro__:
        if "superClassName" in klass.__dict__:
            descriptor = klass.__dict__["superClassName"]
            break
    assert isinstance(descriptor, property)

def test_asml::class_has_name():
    assert hasattr(AsmL::Class, "name")
    descriptor = None
    for klass in AsmL::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_asml::class_has_isAbstract():
    assert hasattr(AsmL::Class, "isAbstract")
    descriptor = None
    for klass in AsmL::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_asml::function_is_not_abstract():
    assert not inspect.isabstract(AsmL::Function)


def test_asml::function_constructor_exists():
    assert callable(AsmL::Function.__init__)


def test_asml::function_constructor_args():
    sig = inspect.signature(AsmL::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml::function_has_name():
    assert hasattr(AsmL::Function, "name")
    descriptor = None
    for klass in AsmL::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asml::structure_is_not_abstract():
    assert not inspect.isabstract(AsmL::Structure)


def test_asml::structure_constructor_exists():
    assert callable(AsmL::Structure.__init__)


def test_asml::structure_constructor_args():
    sig = inspect.signature(AsmL::Structure.__init__)
    params = list(sig.parameters.keys())
    assert "superStructureName" in params, "Missing parameter 'superStructureName'"
    assert "name" in params, "Missing parameter 'name'"

def test_asml::structure_has_superStructureName():
    assert hasattr(AsmL::Structure, "superStructureName")
    descriptor = None
    for klass in AsmL::Structure.__mro__:
        if "superStructureName" in klass.__dict__:
            descriptor = klass.__dict__["superStructureName"]
            break
    assert isinstance(descriptor, property)

def test_asml::structure_has_name():
    assert hasattr(AsmL::Structure, "name")
    descriptor = None
    for klass in AsmL::Structure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asml::vardeclaration_is_not_abstract():
    assert not inspect.isabstract(AsmL::VarDeclaration)


def test_asml::vardeclaration_constructor_exists():
    assert callable(AsmL::VarDeclaration.__init__)


def test_asml::vardeclaration_constructor_args():
    sig = inspect.signature(AsmL::VarDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isLocal" in params, "Missing parameter 'isLocal'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isDeclaration" in params, "Missing parameter 'isDeclaration'"
    assert "isConstant" in params, "Missing parameter 'isConstant'"

def test_asml::vardeclaration_has_isLocal():
    assert hasattr(AsmL::VarDeclaration, "isLocal")
    descriptor = None
    for klass in AsmL::VarDeclaration.__mro__:
        if "isLocal" in klass.__dict__:
            descriptor = klass.__dict__["isLocal"]
            break
    assert isinstance(descriptor, property)

def test_asml::vardeclaration_has_name():
    assert hasattr(AsmL::VarDeclaration, "name")
    descriptor = None
    for klass in AsmL::VarDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_asml::vardeclaration_has_isDeclaration():
    assert hasattr(AsmL::VarDeclaration, "isDeclaration")
    descriptor = None
    for klass in AsmL::VarDeclaration.__mro__:
        if "isDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["isDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_asml::vardeclaration_has_isConstant():
    assert hasattr(AsmL::VarDeclaration, "isConstant")
    descriptor = None
    for klass in AsmL::VarDeclaration.__mro__:
        if "isConstant" in klass.__dict__:
            descriptor = klass.__dict__["isConstant"]
            break
    assert isinstance(descriptor, property)



def test_asml::type_is_not_abstract():
    assert not inspect.isabstract(AsmL::Type)


def test_asml::type_constructor_exists():
    assert callable(AsmL::Type.__init__)


def test_asml::type_constructor_args():
    sig = inspect.signature(AsmL::Type.__init__)
    params = list(sig.parameters.keys())
    assert "withNull" in params, "Missing parameter 'withNull'"

def test_asml::type_has_withNull():
    assert hasattr(AsmL::Type, "withNull")
    descriptor = None
    for klass in AsmL::Type.__mro__:
        if "withNull" in klass.__dict__:
            descriptor = klass.__dict__["withNull"]
            break
    assert isinstance(descriptor, property)



def test_asml::namespace_is_not_abstract():
    assert not inspect.isabstract(AsmL::Namespace)


def test_asml::namespace_constructor_exists():
    assert callable(AsmL::Namespace.__init__)


def test_asml::namespace_constructor_args():
    sig = inspect.signature(AsmL::Namespace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml::namespace_has_name():
    assert hasattr(AsmL::Namespace, "name")
    descriptor = None
    for klass in AsmL::Namespace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asml::enumeration_is_not_abstract():
    assert not inspect.isabstract(AsmL::Enumeration)


def test_asml::enumeration_constructor_exists():
    assert callable(AsmL::Enumeration.__init__)


def test_asml::enumeration_constructor_args():
    sig = inspect.signature(AsmL::Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml::enumeration_has_name():
    assert hasattr(AsmL::Enumeration, "name")
    descriptor = None
    for klass in AsmL::Enumeration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_asml::varterm_is_not_abstract():
    assert not inspect.isabstract(AsmL::VarTerm)


def test_asml::varterm_constructor_exists():
    assert callable(AsmL::VarTerm.__init__)


def test_asml::varterm_constructor_args():
    sig = inspect.signature(AsmL::VarTerm.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml::varterm_has_name():
    assert hasattr(AsmL::VarTerm, "name")
    descriptor = None
    for klass in AsmL::VarTerm.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asml::sequenceterm_is_not_abstract():
    assert not inspect.isabstract(AsmL::SequenceTerm)


def test_asml::sequenceterm_constructor_exists():
    assert callable(AsmL::SequenceTerm.__init__)


def test_asml::sequenceterm_constructor_args():
    sig = inspect.signature(AsmL::SequenceTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml::tulpletterm_is_not_abstract():
    assert not inspect.isabstract(AsmL::TulpletTerm)


def test_asml::tulpletterm_constructor_exists():
    assert callable(AsmL::TulpletTerm.__init__)


def test_asml::tulpletterm_constructor_args():
    sig = inspect.signature(AsmL::TulpletTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml::predicateterm_is_not_abstract():
    assert not inspect.isabstract(AsmL::PredicateTerm)


def test_asml::predicateterm_constructor_exists():
    assert callable(AsmL::PredicateTerm.__init__)


def test_asml::predicateterm_constructor_args():
    sig = inspect.signature(AsmL::PredicateTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml::constant_is_not_abstract():
    assert not inspect.isabstract(AsmL::Constant)


def test_asml::constant_constructor_exists():
    assert callable(AsmL::Constant.__init__)


def test_asml::constant_constructor_args():
    sig = inspect.signature(AsmL::Constant.__init__)
    params = list(sig.parameters.keys())



def test_asml::setterm_is_not_abstract():
    assert not inspect.isabstract(AsmL::SetTerm)


def test_asml::setterm_constructor_exists():
    assert callable(AsmL::SetTerm.__init__)


def test_asml::setterm_constructor_args():
    sig = inspect.signature(AsmL::SetTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml::mapterm_is_not_abstract():
    assert not inspect.isabstract(AsmL::MapTerm)


def test_asml::mapterm_constructor_exists():
    assert callable(AsmL::MapTerm.__init__)


def test_asml::mapterm_constructor_args():
    sig = inspect.signature(AsmL::MapTerm.__init__)
    params = list(sig.parameters.keys())
    assert "separator" in params, "Missing parameter 'separator'"

def test_asml::mapterm_has_separator():
    assert hasattr(AsmL::MapTerm, "separator")
    descriptor = None
    for klass in AsmL::MapTerm.__mro__:
        if "separator" in klass.__dict__:
            descriptor = klass.__dict__["separator"]
            break
    assert isinstance(descriptor, property)



def test_asml::operator_is_not_abstract():
    assert not inspect.isabstract(AsmL::Operator)


def test_asml::operator_constructor_exists():
    assert callable(AsmL::Operator.__init__)


def test_asml::operator_constructor_args():
    sig = inspect.signature(AsmL::Operator.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_asml::operator_has_opName():
    assert hasattr(AsmL::Operator, "opName")
    descriptor = None
    for klass in AsmL::Operator.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_asml::methodcallterm_is_not_abstract():
    assert not inspect.isabstract(AsmL::MethodCallTerm)


def test_asml::methodcallterm_constructor_exists():
    assert callable(AsmL::MethodCallTerm.__init__)


def test_asml::methodcallterm_constructor_args():
    sig = inspect.signature(AsmL::MethodCallTerm.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml::methodcallterm_has_name():
    assert hasattr(AsmL::MethodCallTerm, "name")
    descriptor = None
    for klass in AsmL::MethodCallTerm.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_asml::removerule_is_not_abstract():
    assert not inspect.isabstract(AsmL::RemoveRule)


def test_asml::removerule_constructor_exists():
    assert callable(AsmL::RemoveRule.__init__)


def test_asml::removerule_constructor_args():
    sig = inspect.signature(AsmL::RemoveRule.__init__)
    params = list(sig.parameters.keys())



def test_asml::methodinvocation_is_not_abstract():
    assert not inspect.isabstract(AsmL::MethodInvocation)


def test_asml::methodinvocation_constructor_exists():
    assert callable(AsmL::MethodInvocation.__init__)


def test_asml::methodinvocation_constructor_args():
    sig = inspect.signature(AsmL::MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_asml::returnrule_is_not_abstract():
    assert not inspect.isabstract(AsmL::ReturnRule)


def test_asml::returnrule_constructor_exists():
    assert callable(AsmL::ReturnRule.__init__)


def test_asml::returnrule_constructor_args():
    sig = inspect.signature(AsmL::ReturnRule.__init__)
    params = list(sig.parameters.keys())



def test_asml::conditionalrule_is_not_abstract():
    assert not inspect.isabstract(AsmL::ConditionalRule)


def test_asml::conditionalrule_constructor_exists():
    assert callable(AsmL::ConditionalRule.__init__)


def test_asml::conditionalrule_constructor_args():
    sig = inspect.signature(AsmL::ConditionalRule.__init__)
    params = list(sig.parameters.keys())



def test_asml::addrule_is_not_abstract():
    assert not inspect.isabstract(AsmL::AddRule)


def test_asml::addrule_constructor_exists():
    assert callable(AsmL::AddRule.__init__)


def test_asml::addrule_constructor_args():
    sig = inspect.signature(AsmL::AddRule.__init__)
    params = list(sig.parameters.keys())



def test_asml::chooserule_is_not_abstract():
    assert not inspect.isabstract(AsmL::ChooseRule)


def test_asml::chooserule_constructor_exists():
    assert callable(AsmL::ChooseRule.__init__)


def test_asml::chooserule_constructor_args():
    sig = inspect.signature(AsmL::ChooseRule.__init__)
    params = list(sig.parameters.keys())



def test_asml::forallrule_is_not_abstract():
    assert not inspect.isabstract(AsmL::ForallRule)


def test_asml::forallrule_constructor_exists():
    assert callable(AsmL::ForallRule.__init__)


def test_asml::forallrule_constructor_args():
    sig = inspect.signature(AsmL::ForallRule.__init__)
    params = list(sig.parameters.keys())



def test_asml::updaterule_is_not_abstract():
    assert not inspect.isabstract(AsmL::UpdateRule)


def test_asml::updaterule_constructor_exists():
    assert callable(AsmL::UpdateRule.__init__)


def test_asml::updaterule_constructor_args():
    sig = inspect.signature(AsmL::UpdateRule.__init__)
    params = list(sig.parameters.keys())



def test_asml::skiprule_is_not_abstract():
    assert not inspect.isabstract(AsmL::SkipRule)


def test_asml::skiprule_constructor_exists():
    assert callable(AsmL::SkipRule.__init__)


def test_asml::skiprule_constructor_args():
    sig = inspect.signature(AsmL::SkipRule.__init__)
    params = list(sig.parameters.keys())



def test_asml::step_is_not_abstract():
    assert not inspect.isabstract(AsmL::Step)


def test_asml::step_constructor_exists():
    assert callable(AsmL::Step.__init__)


def test_asml::step_constructor_args():
    sig = inspect.signature(AsmL::Step.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml::step_has_name():
    assert hasattr(AsmL::Step, "name")
    descriptor = None
    for klass in AsmL::Step.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_asml::varorcase_is_not_abstract():
    assert not inspect.isabstract(AsmL::VarOrCase)


def test_asml::varorcase_constructor_exists():
    assert callable(AsmL::VarOrCase.__init__)


def test_asml::varorcase_constructor_args():
    sig = inspect.signature(AsmL::VarOrCase.__init__)
    params = list(sig.parameters.keys())



def test_asml::asmlfile_is_not_abstract():
    assert not inspect.isabstract(AsmL::AsmLFile)


def test_asml::asmlfile_constructor_exists():
    assert callable(AsmL::AsmLFile.__init__)


def test_asml::asmlfile_constructor_args():
    sig = inspect.signature(AsmL::AsmLFile.__init__)
    params = list(sig.parameters.keys())



def test_asml::inwhereholds_is_not_abstract():
    assert not inspect.isabstract(AsmL::InWhereHolds)


def test_asml::inwhereholds_constructor_exists():
    assert callable(AsmL::InWhereHolds.__init__)


def test_asml::inwhereholds_constructor_args():
    sig = inspect.signature(AsmL::InWhereHolds.__init__)
    params = list(sig.parameters.keys())



def test_asml::initially_is_not_abstract():
    assert not inspect.isabstract(AsmL::Initially)


def test_asml::initially_constructor_exists():
    assert callable(AsmL::Initially.__init__)


def test_asml::initially_constructor_args():
    sig = inspect.signature(AsmL::Initially.__init__)
    params = list(sig.parameters.keys())



def test_asml::enumerator_is_not_abstract():
    assert not inspect.isabstract(AsmL::Enumerator)


def test_asml::enumerator_constructor_exists():
    assert callable(AsmL::Enumerator.__init__)


def test_asml::enumerator_constructor_args():
    sig = inspect.signature(AsmL::Enumerator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml::enumerator_has_name():
    assert hasattr(AsmL::Enumerator, "name")
    descriptor = None
    for klass in AsmL::Enumerator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asml::term_is_not_abstract():
    assert not inspect.isabstract(AsmL::Term)


def test_asml::term_constructor_exists():
    assert callable(AsmL::Term.__init__)


def test_asml::term_constructor_args():
    sig = inspect.signature(AsmL::Term.__init__)
    params = list(sig.parameters.keys())



def test_asml::rule_is_not_abstract():
    assert not inspect.isabstract(AsmL::Rule)


def test_asml::rule_constructor_exists():
    assert callable(AsmL::Rule.__init__)


def test_asml::rule_constructor_args():
    sig = inspect.signature(AsmL::Rule.__init__)
    params = list(sig.parameters.keys())



def test_asml::varormethod_is_not_abstract():
    assert not inspect.isabstract(AsmL::VarOrMethod)


def test_asml::varormethod_constructor_exists():
    assert callable(AsmL::VarOrMethod.__init__)


def test_asml::varormethod_constructor_args():
    sig = inspect.signature(AsmL::VarOrMethod.__init__)
    params = list(sig.parameters.keys())



def test_asml::asmlelement_is_not_abstract():
    assert not inspect.isabstract(AsmL::AsmLElement)


def test_asml::asmlelement_constructor_exists():
    assert callable(AsmL::AsmLElement.__init__)


def test_asml::asmlelement_constructor_args():
    sig = inspect.signature(AsmL::AsmLElement.__init__)
    params = list(sig.parameters.keys())



def test_asml::parameter_is_not_abstract():
    assert not inspect.isabstract(AsmL::Parameter)


def test_asml::parameter_constructor_exists():
    assert callable(AsmL::Parameter.__init__)


def test_asml::parameter_constructor_args():
    sig = inspect.signature(AsmL::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml::parameter_has_name():
    assert hasattr(AsmL::Parameter, "name")
    descriptor = None
    for klass in AsmL::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asml::body_is_not_abstract():
    assert not inspect.isabstract(AsmL::Body)


def test_asml::body_constructor_exists():
    assert callable(AsmL::Body.__init__)


def test_asml::body_constructor_args():
    sig = inspect.signature(AsmL::Body.__init__)
    params = list(sig.parameters.keys())



def test_asml::locatedelement_is_not_abstract():
    assert not inspect.isabstract(AsmL::LocatedElement)


def test_asml::locatedelement_constructor_exists():
    assert callable(AsmL::LocatedElement.__init__)


def test_asml::locatedelement_constructor_args():
    sig = inspect.signature(AsmL::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"

def test_asml::locatedelement_has_location():
    assert hasattr(AsmL::LocatedElement, "location")
    descriptor = None
    for klass in AsmL::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_asml::locatedelement_has_commentsAfter():
    assert hasattr(AsmL::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in AsmL::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_asml::locatedelement_has_commentsBefore():
    assert hasattr(AsmL::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in AsmL::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
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
Constant_strategy = st.builds(
    Constant,
)
AsmL::StringConstant_strategy = st.builds(
    AsmL::StringConstant,
    val=
        safe_text
)
AsmL::NullConstant_strategy = st.builds(
    AsmL::NullConstant,
)
AsmL::IntegerConstant_strategy = st.builds(
    AsmL::IntegerConstant,
    val=
        safe_text
)
AsmL::BooleanConstant_strategy = st.builds(
    AsmL::BooleanConstant,
    val=
        safe_text
)
SequenceTerm_strategy = st.builds(
    SequenceTerm,
)
AsmL::RangeSequence_strategy = st.builds(
    AsmL::RangeSequence,
)
AsmL::EnumerateSequence_strategy = st.builds(
    AsmL::EnumerateSequence,
)
SetTerm_strategy = st.builds(
    SetTerm,
)
AsmL::RangeSet_strategy = st.builds(
    AsmL::RangeSet,
)
AsmL::AlgorithmSet_strategy = st.builds(
    AsmL::AlgorithmSet,
)
AsmL::EnumerateSet_strategy = st.builds(
    AsmL::EnumerateSet,
)
PredicateTerm_strategy = st.builds(
    PredicateTerm,
)
AsmL::ExistsTerm_strategy = st.builds(
    AsmL::ExistsTerm,
    isUnique=
        safe_text
)
AsmL::AnyIn_strategy = st.builds(
    AsmL::AnyIn,
)
AsmL::ForAllTerm_strategy = st.builds(
    AsmL::ForAllTerm,
)
ConditionalRule_strategy = st.builds(
    ConditionalRule,
)
AsmL::ElseIf_strategy = st.builds(
    AsmL::ElseIf,
)
ElseIf_strategy = st.builds(
    ElseIf,
)
UpdateRule_strategy = st.builds(
    UpdateRule,
)
AsmL::UpdateMapRule_strategy = st.builds(
    AsmL::UpdateMapRule,
)
AsmL::UpdateFieldRule_strategy = st.builds(
    AsmL::UpdateFieldRule,
)
AsmL::UpdateVarRule_strategy = st.builds(
    AsmL::UpdateVarRule,
)
MethodCallTerm_strategy = st.builds(
    MethodCallTerm,
)
AsmL::NewInstance_strategy = st.builds(
    AsmL::NewInstance,
)
InWhereHolds_strategy = st.builds(
    InWhereHolds,
)
StepExpression_strategy = st.builds(
    StepExpression,
)
AsmL::StepUntil_strategy = st.builds(
    AsmL::StepUntil,
)
AsmL::StepWhile_strategy = st.builds(
    AsmL::StepWhile,
)
Step_strategy = st.builds(
    Step,
)
AsmL::StepExpression_strategy = st.builds(
    AsmL::StepExpression,
)
AsmL::StepForEach_strategy = st.builds(
    AsmL::StepForEach,
)
AsmL::StepUntilFixPoint_strategy = st.builds(
    AsmL::StepUntilFixPoint,
)
Method_strategy = st.builds(
    Method,
)
VarTerm_strategy = st.builds(
    VarTerm,
)
Initially_strategy = st.builds(
    Initially,
)
Body_strategy = st.builds(
    Body,
)
Parameter_strategy = st.builds(
    Parameter,
)
Function_strategy = st.builds(
    Function,
)
AsmL::Main_strategy = st.builds(
    AsmL::Main,
)
Class_strategy = st.builds(
    Class,
)
Enumerator_strategy = st.builds(
    Enumerator,
)
Structure_strategy = st.builds(
    Structure,
)
VarDeclaration_strategy = st.builds(
    VarDeclaration,
)
Type_strategy = st.builds(
    Type,
)
AsmL::SequenceType_strategy = st.builds(
    AsmL::SequenceType,
)
AsmL::TupletType_strategy = st.builds(
    AsmL::TupletType,
)
AsmL::NamedType_strategy = st.builds(
    AsmL::NamedType,
    name=
        safe_text
)
AsmL::SetType_strategy = st.builds(
    AsmL::SetType,
)
AsmL::MapType_strategy = st.builds(
    AsmL::MapType,
)
VarOrMethod_strategy = st.builds(
    VarOrMethod,
)
AsmL::Method_strategy = st.builds(
    AsmL::Method,
    isOverride=
        safe_text,
    isShared=
        safe_text,
    isEntryPoint=
        safe_text,
    isAbstract=
        safe_text
)
VarOrCase_strategy = st.builds(
    VarOrCase,
)
AsmL::Case_strategy = st.builds(
    AsmL::Case,
    name=
        safe_text
)
AsmLFile_strategy = st.builds(
    AsmLFile,
)
Main_strategy = st.builds(
    Main,
)
AsmLElement_strategy = st.builds(
    AsmLElement,
)
AsmL::Class_strategy = st.builds(
    AsmL::Class,
    superClassName=
        safe_text,
    name=
        safe_text,
    isAbstract=
        safe_text
)
AsmL::Function_strategy = st.builds(
    AsmL::Function,
    name=
        safe_text
)
AsmL::Structure_strategy = st.builds(
    AsmL::Structure,
    superStructureName=
        safe_text,
    name=
        safe_text
)
AsmL::VarDeclaration_strategy = st.builds(
    AsmL::VarDeclaration,
    isLocal=
        safe_text,
    name=
        safe_text,
    isDeclaration=
        safe_text,
    isConstant=
        safe_text
)
AsmL::Type_strategy = st.builds(
    AsmL::Type,
    withNull=
        safe_text
)
AsmL::Namespace_strategy = st.builds(
    AsmL::Namespace,
    name=
        safe_text
)
AsmL::Enumeration_strategy = st.builds(
    AsmL::Enumeration,
    name=
        safe_text
)
Term_strategy = st.builds(
    Term,
)
AsmL::VarTerm_strategy = st.builds(
    AsmL::VarTerm,
    name=
        safe_text
)
AsmL::SequenceTerm_strategy = st.builds(
    AsmL::SequenceTerm,
)
AsmL::TulpletTerm_strategy = st.builds(
    AsmL::TulpletTerm,
)
AsmL::PredicateTerm_strategy = st.builds(
    AsmL::PredicateTerm,
)
AsmL::Constant_strategy = st.builds(
    AsmL::Constant,
)
AsmL::SetTerm_strategy = st.builds(
    AsmL::SetTerm,
)
AsmL::MapTerm_strategy = st.builds(
    AsmL::MapTerm,
    separator=
        safe_text
)
AsmL::Operator_strategy = st.builds(
    AsmL::Operator,
    opName=
        safe_text
)
AsmL::MethodCallTerm_strategy = st.builds(
    AsmL::MethodCallTerm,
    name=
        safe_text
)
Rule_strategy = st.builds(
    Rule,
)
AsmL::RemoveRule_strategy = st.builds(
    AsmL::RemoveRule,
)
AsmL::MethodInvocation_strategy = st.builds(
    AsmL::MethodInvocation,
)
AsmL::ReturnRule_strategy = st.builds(
    AsmL::ReturnRule,
)
AsmL::ConditionalRule_strategy = st.builds(
    AsmL::ConditionalRule,
)
AsmL::AddRule_strategy = st.builds(
    AsmL::AddRule,
)
AsmL::ChooseRule_strategy = st.builds(
    AsmL::ChooseRule,
)
AsmL::ForallRule_strategy = st.builds(
    AsmL::ForallRule,
)
AsmL::UpdateRule_strategy = st.builds(
    AsmL::UpdateRule,
)
AsmL::SkipRule_strategy = st.builds(
    AsmL::SkipRule,
)
AsmL::Step_strategy = st.builds(
    AsmL::Step,
    name=
        safe_text
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
AsmL::VarOrCase_strategy = st.builds(
    AsmL::VarOrCase,
)
AsmL::AsmLFile_strategy = st.builds(
    AsmL::AsmLFile,
)
AsmL::InWhereHolds_strategy = st.builds(
    AsmL::InWhereHolds,
)
AsmL::Initially_strategy = st.builds(
    AsmL::Initially,
)
AsmL::Enumerator_strategy = st.builds(
    AsmL::Enumerator,
    name=
        safe_text
)
AsmL::Term_strategy = st.builds(
    AsmL::Term,
)
AsmL::Rule_strategy = st.builds(
    AsmL::Rule,
)
AsmL::VarOrMethod_strategy = st.builds(
    AsmL::VarOrMethod,
)
AsmL::AsmLElement_strategy = st.builds(
    AsmL::AsmLElement,
)
AsmL::Parameter_strategy = st.builds(
    AsmL::Parameter,
    name=
        safe_text
)
AsmL::Body_strategy = st.builds(
    AsmL::Body,
)
AsmL::LocatedElement_strategy = st.builds(
    AsmL::LocatedElement,
    location=
        safe_text,
    commentsAfter=
        safe_text,
    commentsBefore=
        safe_text
)

@given(instance=Constant_strategy)
@settings(max_examples=50)
def test_constant_instantiation(instance):
    assert isinstance(instance, Constant)

@given(instance=AsmL::StringConstant_strategy)
@settings(max_examples=50)
def test_asml::stringconstant_instantiation(instance):
    assert isinstance(instance, AsmL::StringConstant)

@given(instance=AsmL::StringConstant_strategy)
def test_asml::stringconstant_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=AsmL::StringConstant_strategy)
def test_asml::stringconstant_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=AsmL::NullConstant_strategy)
@settings(max_examples=50)
def test_asml::nullconstant_instantiation(instance):
    assert isinstance(instance, AsmL::NullConstant)

@given(instance=AsmL::IntegerConstant_strategy)
@settings(max_examples=50)
def test_asml::integerconstant_instantiation(instance):
    assert isinstance(instance, AsmL::IntegerConstant)

@given(instance=AsmL::IntegerConstant_strategy)
def test_asml::integerconstant_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=AsmL::IntegerConstant_strategy)
def test_asml::integerconstant_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=AsmL::BooleanConstant_strategy)
@settings(max_examples=50)
def test_asml::booleanconstant_instantiation(instance):
    assert isinstance(instance, AsmL::BooleanConstant)

@given(instance=AsmL::BooleanConstant_strategy)
def test_asml::booleanconstant_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=AsmL::BooleanConstant_strategy)
def test_asml::booleanconstant_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=SequenceTerm_strategy)
@settings(max_examples=50)
def test_sequenceterm_instantiation(instance):
    assert isinstance(instance, SequenceTerm)

@given(instance=AsmL::RangeSequence_strategy)
@settings(max_examples=50)
def test_asml::rangesequence_instantiation(instance):
    assert isinstance(instance, AsmL::RangeSequence)

@given(instance=AsmL::EnumerateSequence_strategy)
@settings(max_examples=50)
def test_asml::enumeratesequence_instantiation(instance):
    assert isinstance(instance, AsmL::EnumerateSequence)

@given(instance=SetTerm_strategy)
@settings(max_examples=50)
def test_setterm_instantiation(instance):
    assert isinstance(instance, SetTerm)

@given(instance=AsmL::RangeSet_strategy)
@settings(max_examples=50)
def test_asml::rangeset_instantiation(instance):
    assert isinstance(instance, AsmL::RangeSet)

@given(instance=AsmL::AlgorithmSet_strategy)
@settings(max_examples=50)
def test_asml::algorithmset_instantiation(instance):
    assert isinstance(instance, AsmL::AlgorithmSet)

@given(instance=AsmL::EnumerateSet_strategy)
@settings(max_examples=50)
def test_asml::enumerateset_instantiation(instance):
    assert isinstance(instance, AsmL::EnumerateSet)

@given(instance=PredicateTerm_strategy)
@settings(max_examples=50)
def test_predicateterm_instantiation(instance):
    assert isinstance(instance, PredicateTerm)

@given(instance=AsmL::ExistsTerm_strategy)
@settings(max_examples=50)
def test_asml::existsterm_instantiation(instance):
    assert isinstance(instance, AsmL::ExistsTerm)

@given(instance=AsmL::ExistsTerm_strategy)
def test_asml::existsterm_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=AsmL::ExistsTerm_strategy)
def test_asml::existsterm_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=AsmL::AnyIn_strategy)
@settings(max_examples=50)
def test_asml::anyin_instantiation(instance):
    assert isinstance(instance, AsmL::AnyIn)

@given(instance=AsmL::ForAllTerm_strategy)
@settings(max_examples=50)
def test_asml::forallterm_instantiation(instance):
    assert isinstance(instance, AsmL::ForAllTerm)

@given(instance=ConditionalRule_strategy)
@settings(max_examples=50)
def test_conditionalrule_instantiation(instance):
    assert isinstance(instance, ConditionalRule)

@given(instance=AsmL::ElseIf_strategy)
@settings(max_examples=50)
def test_asml::elseif_instantiation(instance):
    assert isinstance(instance, AsmL::ElseIf)

@given(instance=ElseIf_strategy)
@settings(max_examples=50)
def test_elseif_instantiation(instance):
    assert isinstance(instance, ElseIf)

@given(instance=UpdateRule_strategy)
@settings(max_examples=50)
def test_updaterule_instantiation(instance):
    assert isinstance(instance, UpdateRule)

@given(instance=AsmL::UpdateMapRule_strategy)
@settings(max_examples=50)
def test_asml::updatemaprule_instantiation(instance):
    assert isinstance(instance, AsmL::UpdateMapRule)

@given(instance=AsmL::UpdateFieldRule_strategy)
@settings(max_examples=50)
def test_asml::updatefieldrule_instantiation(instance):
    assert isinstance(instance, AsmL::UpdateFieldRule)

@given(instance=AsmL::UpdateVarRule_strategy)
@settings(max_examples=50)
def test_asml::updatevarrule_instantiation(instance):
    assert isinstance(instance, AsmL::UpdateVarRule)

@given(instance=MethodCallTerm_strategy)
@settings(max_examples=50)
def test_methodcallterm_instantiation(instance):
    assert isinstance(instance, MethodCallTerm)

@given(instance=AsmL::NewInstance_strategy)
@settings(max_examples=50)
def test_asml::newinstance_instantiation(instance):
    assert isinstance(instance, AsmL::NewInstance)

@given(instance=InWhereHolds_strategy)
@settings(max_examples=50)
def test_inwhereholds_instantiation(instance):
    assert isinstance(instance, InWhereHolds)

@given(instance=StepExpression_strategy)
@settings(max_examples=50)
def test_stepexpression_instantiation(instance):
    assert isinstance(instance, StepExpression)

@given(instance=AsmL::StepUntil_strategy)
@settings(max_examples=50)
def test_asml::stepuntil_instantiation(instance):
    assert isinstance(instance, AsmL::StepUntil)

@given(instance=AsmL::StepWhile_strategy)
@settings(max_examples=50)
def test_asml::stepwhile_instantiation(instance):
    assert isinstance(instance, AsmL::StepWhile)

@given(instance=Step_strategy)
@settings(max_examples=50)
def test_step_instantiation(instance):
    assert isinstance(instance, Step)

@given(instance=AsmL::StepExpression_strategy)
@settings(max_examples=50)
def test_asml::stepexpression_instantiation(instance):
    assert isinstance(instance, AsmL::StepExpression)

@given(instance=AsmL::StepForEach_strategy)
@settings(max_examples=50)
def test_asml::stepforeach_instantiation(instance):
    assert isinstance(instance, AsmL::StepForEach)

@given(instance=AsmL::StepUntilFixPoint_strategy)
@settings(max_examples=50)
def test_asml::stepuntilfixpoint_instantiation(instance):
    assert isinstance(instance, AsmL::StepUntilFixPoint)

@given(instance=Method_strategy)
@settings(max_examples=50)
def test_method_instantiation(instance):
    assert isinstance(instance, Method)

@given(instance=VarTerm_strategy)
@settings(max_examples=50)
def test_varterm_instantiation(instance):
    assert isinstance(instance, VarTerm)

@given(instance=Initially_strategy)
@settings(max_examples=50)
def test_initially_instantiation(instance):
    assert isinstance(instance, Initially)

@given(instance=Body_strategy)
@settings(max_examples=50)
def test_body_instantiation(instance):
    assert isinstance(instance, Body)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=AsmL::Main_strategy)
@settings(max_examples=50)
def test_asml::main_instantiation(instance):
    assert isinstance(instance, AsmL::Main)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Enumerator_strategy)
@settings(max_examples=50)
def test_enumerator_instantiation(instance):
    assert isinstance(instance, Enumerator)

@given(instance=Structure_strategy)
@settings(max_examples=50)
def test_structure_instantiation(instance):
    assert isinstance(instance, Structure)

@given(instance=VarDeclaration_strategy)
@settings(max_examples=50)
def test_vardeclaration_instantiation(instance):
    assert isinstance(instance, VarDeclaration)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=AsmL::SequenceType_strategy)
@settings(max_examples=50)
def test_asml::sequencetype_instantiation(instance):
    assert isinstance(instance, AsmL::SequenceType)

@given(instance=AsmL::TupletType_strategy)
@settings(max_examples=50)
def test_asml::tuplettype_instantiation(instance):
    assert isinstance(instance, AsmL::TupletType)

@given(instance=AsmL::NamedType_strategy)
@settings(max_examples=50)
def test_asml::namedtype_instantiation(instance):
    assert isinstance(instance, AsmL::NamedType)

@given(instance=AsmL::NamedType_strategy)
def test_asml::namedtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AsmL::NamedType_strategy)
def test_asml::namedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmL::SetType_strategy)
@settings(max_examples=50)
def test_asml::settype_instantiation(instance):
    assert isinstance(instance, AsmL::SetType)

@given(instance=AsmL::MapType_strategy)
@settings(max_examples=50)
def test_asml::maptype_instantiation(instance):
    assert isinstance(instance, AsmL::MapType)

@given(instance=VarOrMethod_strategy)
@settings(max_examples=50)
def test_varormethod_instantiation(instance):
    assert isinstance(instance, VarOrMethod)

@given(instance=AsmL::Method_strategy)
@settings(max_examples=50)
def test_asml::method_instantiation(instance):
    assert isinstance(instance, AsmL::Method)

@given(instance=AsmL::Method_strategy)
def test_asml::method_isOverride_type(instance):
    assert isinstance(instance.isOverride, str)


@given(instance=AsmL::Method_strategy)
def test_asml::method_isOverride_setter(instance):
    original = instance.isOverride
    instance.isOverride = original
    assert instance.isOverride == original

@given(instance=AsmL::Method_strategy)
def test_asml::method_isShared_type(instance):
    assert isinstance(instance.isShared, str)


@given(instance=AsmL::Method_strategy)
def test_asml::method_isShared_setter(instance):
    original = instance.isShared
    instance.isShared = original
    assert instance.isShared == original

@given(instance=AsmL::Method_strategy)
def test_asml::method_isEntryPoint_type(instance):
    assert isinstance(instance.isEntryPoint, str)


@given(instance=AsmL::Method_strategy)
def test_asml::method_isEntryPoint_setter(instance):
    original = instance.isEntryPoint
    instance.isEntryPoint = original
    assert instance.isEntryPoint == original

@given(instance=AsmL::Method_strategy)
def test_asml::method_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=AsmL::Method_strategy)
def test_asml::method_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=VarOrCase_strategy)
@settings(max_examples=50)
def test_varorcase_instantiation(instance):
    assert isinstance(instance, VarOrCase)

@given(instance=AsmL::Case_strategy)
@settings(max_examples=50)
def test_asml::case_instantiation(instance):
    assert isinstance(instance, AsmL::Case)

@given(instance=AsmL::Case_strategy)
def test_asml::case_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AsmL::Case_strategy)
def test_asml::case_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmLFile_strategy)
@settings(max_examples=50)
def test_asmlfile_instantiation(instance):
    assert isinstance(instance, AsmLFile)

@given(instance=Main_strategy)
@settings(max_examples=50)
def test_main_instantiation(instance):
    assert isinstance(instance, Main)

@given(instance=AsmLElement_strategy)
@settings(max_examples=50)
def test_asmlelement_instantiation(instance):
    assert isinstance(instance, AsmLElement)

@given(instance=AsmL::Class_strategy)
@settings(max_examples=50)
def test_asml::class_instantiation(instance):
    assert isinstance(instance, AsmL::Class)

@given(instance=AsmL::Class_strategy)
def test_asml::class_superClassName_type(instance):
    assert isinstance(instance.superClassName, str)


@given(instance=AsmL::Class_strategy)
def test_asml::class_superClassName_setter(instance):
    original = instance.superClassName
    instance.superClassName = original
    assert instance.superClassName == original

@given(instance=AsmL::Class_strategy)
def test_asml::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AsmL::Class_strategy)
def test_asml::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmL::Class_strategy)
def test_asml::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=AsmL::Class_strategy)
def test_asml::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=AsmL::Function_strategy)
@settings(max_examples=50)
def test_asml::function_instantiation(instance):
    assert isinstance(instance, AsmL::Function)

@given(instance=AsmL::Function_strategy)
def test_asml::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AsmL::Function_strategy)
def test_asml::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmL::Structure_strategy)
@settings(max_examples=50)
def test_asml::structure_instantiation(instance):
    assert isinstance(instance, AsmL::Structure)

@given(instance=AsmL::Structure_strategy)
def test_asml::structure_superStructureName_type(instance):
    assert isinstance(instance.superStructureName, str)


@given(instance=AsmL::Structure_strategy)
def test_asml::structure_superStructureName_setter(instance):
    original = instance.superStructureName
    instance.superStructureName = original
    assert instance.superStructureName == original

@given(instance=AsmL::Structure_strategy)
def test_asml::structure_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AsmL::Structure_strategy)
def test_asml::structure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmL::VarDeclaration_strategy)
@settings(max_examples=50)
def test_asml::vardeclaration_instantiation(instance):
    assert isinstance(instance, AsmL::VarDeclaration)

@given(instance=AsmL::VarDeclaration_strategy)
def test_asml::vardeclaration_isLocal_type(instance):
    assert isinstance(instance.isLocal, str)


@given(instance=AsmL::VarDeclaration_strategy)
def test_asml::vardeclaration_isLocal_setter(instance):
    original = instance.isLocal
    instance.isLocal = original
    assert instance.isLocal == original

@given(instance=AsmL::VarDeclaration_strategy)
def test_asml::vardeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AsmL::VarDeclaration_strategy)
def test_asml::vardeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmL::VarDeclaration_strategy)
def test_asml::vardeclaration_isDeclaration_type(instance):
    assert isinstance(instance.isDeclaration, str)


@given(instance=AsmL::VarDeclaration_strategy)
def test_asml::vardeclaration_isDeclaration_setter(instance):
    original = instance.isDeclaration
    instance.isDeclaration = original
    assert instance.isDeclaration == original

@given(instance=AsmL::VarDeclaration_strategy)
def test_asml::vardeclaration_isConstant_type(instance):
    assert isinstance(instance.isConstant, str)


@given(instance=AsmL::VarDeclaration_strategy)
def test_asml::vardeclaration_isConstant_setter(instance):
    original = instance.isConstant
    instance.isConstant = original
    assert instance.isConstant == original

@given(instance=AsmL::Type_strategy)
@settings(max_examples=50)
def test_asml::type_instantiation(instance):
    assert isinstance(instance, AsmL::Type)

@given(instance=AsmL::Type_strategy)
def test_asml::type_withNull_type(instance):
    assert isinstance(instance.withNull, str)


@given(instance=AsmL::Type_strategy)
def test_asml::type_withNull_setter(instance):
    original = instance.withNull
    instance.withNull = original
    assert instance.withNull == original

@given(instance=AsmL::Namespace_strategy)
@settings(max_examples=50)
def test_asml::namespace_instantiation(instance):
    assert isinstance(instance, AsmL::Namespace)

@given(instance=AsmL::Namespace_strategy)
def test_asml::namespace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AsmL::Namespace_strategy)
def test_asml::namespace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmL::Enumeration_strategy)
@settings(max_examples=50)
def test_asml::enumeration_instantiation(instance):
    assert isinstance(instance, AsmL::Enumeration)

@given(instance=AsmL::Enumeration_strategy)
def test_asml::enumeration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AsmL::Enumeration_strategy)
def test_asml::enumeration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=AsmL::VarTerm_strategy)
@settings(max_examples=50)
def test_asml::varterm_instantiation(instance):
    assert isinstance(instance, AsmL::VarTerm)

@given(instance=AsmL::VarTerm_strategy)
def test_asml::varterm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AsmL::VarTerm_strategy)
def test_asml::varterm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmL::SequenceTerm_strategy)
@settings(max_examples=50)
def test_asml::sequenceterm_instantiation(instance):
    assert isinstance(instance, AsmL::SequenceTerm)

@given(instance=AsmL::TulpletTerm_strategy)
@settings(max_examples=50)
def test_asml::tulpletterm_instantiation(instance):
    assert isinstance(instance, AsmL::TulpletTerm)

@given(instance=AsmL::PredicateTerm_strategy)
@settings(max_examples=50)
def test_asml::predicateterm_instantiation(instance):
    assert isinstance(instance, AsmL::PredicateTerm)

@given(instance=AsmL::Constant_strategy)
@settings(max_examples=50)
def test_asml::constant_instantiation(instance):
    assert isinstance(instance, AsmL::Constant)

@given(instance=AsmL::SetTerm_strategy)
@settings(max_examples=50)
def test_asml::setterm_instantiation(instance):
    assert isinstance(instance, AsmL::SetTerm)

@given(instance=AsmL::MapTerm_strategy)
@settings(max_examples=50)
def test_asml::mapterm_instantiation(instance):
    assert isinstance(instance, AsmL::MapTerm)

@given(instance=AsmL::MapTerm_strategy)
def test_asml::mapterm_separator_type(instance):
    assert isinstance(instance.separator, str)


@given(instance=AsmL::MapTerm_strategy)
def test_asml::mapterm_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original

@given(instance=AsmL::Operator_strategy)
@settings(max_examples=50)
def test_asml::operator_instantiation(instance):
    assert isinstance(instance, AsmL::Operator)

@given(instance=AsmL::Operator_strategy)
def test_asml::operator_opName_type(instance):
    assert isinstance(instance.opName, str)


@given(instance=AsmL::Operator_strategy)
def test_asml::operator_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=AsmL::MethodCallTerm_strategy)
@settings(max_examples=50)
def test_asml::methodcallterm_instantiation(instance):
    assert isinstance(instance, AsmL::MethodCallTerm)

@given(instance=AsmL::MethodCallTerm_strategy)
def test_asml::methodcallterm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AsmL::MethodCallTerm_strategy)
def test_asml::methodcallterm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=AsmL::RemoveRule_strategy)
@settings(max_examples=50)
def test_asml::removerule_instantiation(instance):
    assert isinstance(instance, AsmL::RemoveRule)

@given(instance=AsmL::MethodInvocation_strategy)
@settings(max_examples=50)
def test_asml::methodinvocation_instantiation(instance):
    assert isinstance(instance, AsmL::MethodInvocation)

@given(instance=AsmL::ReturnRule_strategy)
@settings(max_examples=50)
def test_asml::returnrule_instantiation(instance):
    assert isinstance(instance, AsmL::ReturnRule)

@given(instance=AsmL::ConditionalRule_strategy)
@settings(max_examples=50)
def test_asml::conditionalrule_instantiation(instance):
    assert isinstance(instance, AsmL::ConditionalRule)

@given(instance=AsmL::AddRule_strategy)
@settings(max_examples=50)
def test_asml::addrule_instantiation(instance):
    assert isinstance(instance, AsmL::AddRule)

@given(instance=AsmL::ChooseRule_strategy)
@settings(max_examples=50)
def test_asml::chooserule_instantiation(instance):
    assert isinstance(instance, AsmL::ChooseRule)

@given(instance=AsmL::ForallRule_strategy)
@settings(max_examples=50)
def test_asml::forallrule_instantiation(instance):
    assert isinstance(instance, AsmL::ForallRule)

@given(instance=AsmL::UpdateRule_strategy)
@settings(max_examples=50)
def test_asml::updaterule_instantiation(instance):
    assert isinstance(instance, AsmL::UpdateRule)

@given(instance=AsmL::SkipRule_strategy)
@settings(max_examples=50)
def test_asml::skiprule_instantiation(instance):
    assert isinstance(instance, AsmL::SkipRule)

@given(instance=AsmL::Step_strategy)
@settings(max_examples=50)
def test_asml::step_instantiation(instance):
    assert isinstance(instance, AsmL::Step)

@given(instance=AsmL::Step_strategy)
def test_asml::step_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AsmL::Step_strategy)
def test_asml::step_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=AsmL::VarOrCase_strategy)
@settings(max_examples=50)
def test_asml::varorcase_instantiation(instance):
    assert isinstance(instance, AsmL::VarOrCase)

@given(instance=AsmL::AsmLFile_strategy)
@settings(max_examples=50)
def test_asml::asmlfile_instantiation(instance):
    assert isinstance(instance, AsmL::AsmLFile)

@given(instance=AsmL::InWhereHolds_strategy)
@settings(max_examples=50)
def test_asml::inwhereholds_instantiation(instance):
    assert isinstance(instance, AsmL::InWhereHolds)

@given(instance=AsmL::Initially_strategy)
@settings(max_examples=50)
def test_asml::initially_instantiation(instance):
    assert isinstance(instance, AsmL::Initially)

@given(instance=AsmL::Enumerator_strategy)
@settings(max_examples=50)
def test_asml::enumerator_instantiation(instance):
    assert isinstance(instance, AsmL::Enumerator)

@given(instance=AsmL::Enumerator_strategy)
def test_asml::enumerator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AsmL::Enumerator_strategy)
def test_asml::enumerator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmL::Term_strategy)
@settings(max_examples=50)
def test_asml::term_instantiation(instance):
    assert isinstance(instance, AsmL::Term)

@given(instance=AsmL::Rule_strategy)
@settings(max_examples=50)
def test_asml::rule_instantiation(instance):
    assert isinstance(instance, AsmL::Rule)

@given(instance=AsmL::VarOrMethod_strategy)
@settings(max_examples=50)
def test_asml::varormethod_instantiation(instance):
    assert isinstance(instance, AsmL::VarOrMethod)

@given(instance=AsmL::AsmLElement_strategy)
@settings(max_examples=50)
def test_asml::asmlelement_instantiation(instance):
    assert isinstance(instance, AsmL::AsmLElement)

@given(instance=AsmL::Parameter_strategy)
@settings(max_examples=50)
def test_asml::parameter_instantiation(instance):
    assert isinstance(instance, AsmL::Parameter)

@given(instance=AsmL::Parameter_strategy)
def test_asml::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AsmL::Parameter_strategy)
def test_asml::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmL::Body_strategy)
@settings(max_examples=50)
def test_asml::body_instantiation(instance):
    assert isinstance(instance, AsmL::Body)

@given(instance=AsmL::LocatedElement_strategy)
@settings(max_examples=50)
def test_asml::locatedelement_instantiation(instance):
    assert isinstance(instance, AsmL::LocatedElement)

@given(instance=AsmL::LocatedElement_strategy)
def test_asml::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=AsmL::LocatedElement_strategy)
def test_asml::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=AsmL::LocatedElement_strategy)
def test_asml::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=AsmL::LocatedElement_strategy)
def test_asml::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=AsmL::LocatedElement_strategy)
def test_asml::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=AsmL::LocatedElement_strategy)
def test_asml::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original
