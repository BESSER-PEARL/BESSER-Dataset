import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SequenceTerm,
    AsmL_EnumerateSequence,
    SetTerm,
    AsmL_AlgorithmSet,
    AsmL_RangeSet,
    AsmL_EnumerateSet,
    PredicateTerm,
    AsmL_AnyIn,
    AsmL_ExistsTerm,
    AsmL_ForAllTerm,
    ConditionalRule,
    AsmL_ElseIf,
    ElseIf,
    UpdateRule,
    AsmL_UpdateMapRule,
    AsmL_UpdateFieldRule,
    AsmL_UpdateVarRule,
    MethodCallTerm,
    AsmL_NewInstance,
    InWhereHolds,
    StepExpression,
    AsmL_StepUntil,
    AsmL_StepWhile,
    Step,
    AsmL_StepForEach,
    AsmL_StepExpression,
    AsmL_StepUntilFixPoint,
    Method,
    VarTerm,
    Initially,
    Body,
    Parameter,
    Function,
    AsmL_Main,
    Class,
    Enumerator,
    Structure,
    VarDeclaration,
    Type,
    AsmL_TupletType,
    AsmL_SequenceType,
    AsmL_SetType,
    AsmL_MapType,
    AsmL_NamedType,
    VarOrMethod,
    AsmL_Method,
    VarOrCase,
    AsmL_Case,
    AsmLFile,
    Main,
    AsmLElement,
    AsmL_Function,
    AsmL_Type,
    AsmL_Namespace,
    AsmL_Class,
    AsmL_Structure,
    AsmL_VarDeclaration,
    AsmL_Enumeration,
    Term,
    AsmL_MapTerm,
    AsmL_PredicateTerm,
    AsmL_SetTerm,
    AsmL_Operator,
    AsmL_VarTerm,
    AsmL_SequenceTerm,
    AsmL_TulpletTerm,
    AsmL_MethodCallTerm,
    Rule,
    AsmL_AddRule,
    AsmL_RemoveRule,
    AsmL_ChooseRule,
    AsmL_ForallRule,
    AsmL_ConditionalRule,
    AsmL_MethodInvocation,
    AsmL_ReturnRule,
    AsmL_UpdateRule,
    AsmL_SkipRule,
    AsmL_Step,
    LocatedElement,
    AsmL_InWhereHolds,
    AsmL_Parameter,
    AsmL_AsmLFile,
    AsmL_VarOrCase,
    AsmL_Enumerator,
    AsmL_Initially,
    AsmL_VarOrMethod,
    AsmL_Rule,
    AsmL_AsmLElement,
    AsmL_Term,
    AsmL_Body,
    AsmL_LocatedElement,
    Constant,
    AsmL_IntegerConstant,
    AsmL_StringConstant,
    AsmL_NullConstant,
    AsmL_BooleanConstant,
    AsmL_Constant,
    AsmL_RangeSequence,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sequenceterm_is_not_abstract():
    assert not inspect.isabstract(SequenceTerm)


def test_sequenceterm_constructor_exists():
    assert callable(SequenceTerm.__init__)


def test_sequenceterm_constructor_args():
    sig = inspect.signature(SequenceTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml_enumeratesequence_is_not_abstract():
    assert not inspect.isabstract(AsmL_EnumerateSequence)


def test_asml_enumeratesequence_constructor_exists():
    assert callable(AsmL_EnumerateSequence.__init__)


def test_asml_enumeratesequence_constructor_args():
    sig = inspect.signature(AsmL_EnumerateSequence.__init__)
    params = list(sig.parameters.keys())



def test_setterm_is_not_abstract():
    assert not inspect.isabstract(SetTerm)


def test_setterm_constructor_exists():
    assert callable(SetTerm.__init__)


def test_setterm_constructor_args():
    sig = inspect.signature(SetTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml_algorithmset_is_not_abstract():
    assert not inspect.isabstract(AsmL_AlgorithmSet)


def test_asml_algorithmset_constructor_exists():
    assert callable(AsmL_AlgorithmSet.__init__)


def test_asml_algorithmset_constructor_args():
    sig = inspect.signature(AsmL_AlgorithmSet.__init__)
    params = list(sig.parameters.keys())



def test_asml_rangeset_is_not_abstract():
    assert not inspect.isabstract(AsmL_RangeSet)


def test_asml_rangeset_constructor_exists():
    assert callable(AsmL_RangeSet.__init__)


def test_asml_rangeset_constructor_args():
    sig = inspect.signature(AsmL_RangeSet.__init__)
    params = list(sig.parameters.keys())



def test_asml_enumerateset_is_not_abstract():
    assert not inspect.isabstract(AsmL_EnumerateSet)


def test_asml_enumerateset_constructor_exists():
    assert callable(AsmL_EnumerateSet.__init__)


def test_asml_enumerateset_constructor_args():
    sig = inspect.signature(AsmL_EnumerateSet.__init__)
    params = list(sig.parameters.keys())



def test_predicateterm_is_not_abstract():
    assert not inspect.isabstract(PredicateTerm)


def test_predicateterm_constructor_exists():
    assert callable(PredicateTerm.__init__)


def test_predicateterm_constructor_args():
    sig = inspect.signature(PredicateTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml_anyin_is_not_abstract():
    assert not inspect.isabstract(AsmL_AnyIn)


def test_asml_anyin_constructor_exists():
    assert callable(AsmL_AnyIn.__init__)


def test_asml_anyin_constructor_args():
    sig = inspect.signature(AsmL_AnyIn.__init__)
    params = list(sig.parameters.keys())



def test_asml_existsterm_is_not_abstract():
    assert not inspect.isabstract(AsmL_ExistsTerm)


def test_asml_existsterm_constructor_exists():
    assert callable(AsmL_ExistsTerm.__init__)


def test_asml_existsterm_constructor_args():
    sig = inspect.signature(AsmL_ExistsTerm.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_asml_existsterm_has_isUnique():
    assert hasattr(AsmL_ExistsTerm, "isUnique")
    descriptor = None
    for klass in AsmL_ExistsTerm.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_asml_forallterm_is_not_abstract():
    assert not inspect.isabstract(AsmL_ForAllTerm)


def test_asml_forallterm_constructor_exists():
    assert callable(AsmL_ForAllTerm.__init__)


def test_asml_forallterm_constructor_args():
    sig = inspect.signature(AsmL_ForAllTerm.__init__)
    params = list(sig.parameters.keys())



def test_conditionalrule_is_not_abstract():
    assert not inspect.isabstract(ConditionalRule)


def test_conditionalrule_constructor_exists():
    assert callable(ConditionalRule.__init__)


def test_conditionalrule_constructor_args():
    sig = inspect.signature(ConditionalRule.__init__)
    params = list(sig.parameters.keys())



def test_asml_elseif_is_not_abstract():
    assert not inspect.isabstract(AsmL_ElseIf)


def test_asml_elseif_constructor_exists():
    assert callable(AsmL_ElseIf.__init__)


def test_asml_elseif_constructor_args():
    sig = inspect.signature(AsmL_ElseIf.__init__)
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



def test_asml_updatemaprule_is_not_abstract():
    assert not inspect.isabstract(AsmL_UpdateMapRule)


def test_asml_updatemaprule_constructor_exists():
    assert callable(AsmL_UpdateMapRule.__init__)


def test_asml_updatemaprule_constructor_args():
    sig = inspect.signature(AsmL_UpdateMapRule.__init__)
    params = list(sig.parameters.keys())



def test_asml_updatefieldrule_is_not_abstract():
    assert not inspect.isabstract(AsmL_UpdateFieldRule)


def test_asml_updatefieldrule_constructor_exists():
    assert callable(AsmL_UpdateFieldRule.__init__)


def test_asml_updatefieldrule_constructor_args():
    sig = inspect.signature(AsmL_UpdateFieldRule.__init__)
    params = list(sig.parameters.keys())



def test_asml_updatevarrule_is_not_abstract():
    assert not inspect.isabstract(AsmL_UpdateVarRule)


def test_asml_updatevarrule_constructor_exists():
    assert callable(AsmL_UpdateVarRule.__init__)


def test_asml_updatevarrule_constructor_args():
    sig = inspect.signature(AsmL_UpdateVarRule.__init__)
    params = list(sig.parameters.keys())



def test_methodcallterm_is_not_abstract():
    assert not inspect.isabstract(MethodCallTerm)


def test_methodcallterm_constructor_exists():
    assert callable(MethodCallTerm.__init__)


def test_methodcallterm_constructor_args():
    sig = inspect.signature(MethodCallTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml_newinstance_is_not_abstract():
    assert not inspect.isabstract(AsmL_NewInstance)


def test_asml_newinstance_constructor_exists():
    assert callable(AsmL_NewInstance.__init__)


def test_asml_newinstance_constructor_args():
    sig = inspect.signature(AsmL_NewInstance.__init__)
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



def test_asml_stepuntil_is_not_abstract():
    assert not inspect.isabstract(AsmL_StepUntil)


def test_asml_stepuntil_constructor_exists():
    assert callable(AsmL_StepUntil.__init__)


def test_asml_stepuntil_constructor_args():
    sig = inspect.signature(AsmL_StepUntil.__init__)
    params = list(sig.parameters.keys())



def test_asml_stepwhile_is_not_abstract():
    assert not inspect.isabstract(AsmL_StepWhile)


def test_asml_stepwhile_constructor_exists():
    assert callable(AsmL_StepWhile.__init__)


def test_asml_stepwhile_constructor_args():
    sig = inspect.signature(AsmL_StepWhile.__init__)
    params = list(sig.parameters.keys())



def test_step_is_not_abstract():
    assert not inspect.isabstract(Step)


def test_step_constructor_exists():
    assert callable(Step.__init__)


def test_step_constructor_args():
    sig = inspect.signature(Step.__init__)
    params = list(sig.parameters.keys())



def test_asml_stepforeach_is_not_abstract():
    assert not inspect.isabstract(AsmL_StepForEach)


def test_asml_stepforeach_constructor_exists():
    assert callable(AsmL_StepForEach.__init__)


def test_asml_stepforeach_constructor_args():
    sig = inspect.signature(AsmL_StepForEach.__init__)
    params = list(sig.parameters.keys())



def test_asml_stepexpression_is_not_abstract():
    assert not inspect.isabstract(AsmL_StepExpression)


def test_asml_stepexpression_constructor_exists():
    assert callable(AsmL_StepExpression.__init__)


def test_asml_stepexpression_constructor_args():
    sig = inspect.signature(AsmL_StepExpression.__init__)
    params = list(sig.parameters.keys())



def test_asml_stepuntilfixpoint_is_not_abstract():
    assert not inspect.isabstract(AsmL_StepUntilFixPoint)


def test_asml_stepuntilfixpoint_constructor_exists():
    assert callable(AsmL_StepUntilFixPoint.__init__)


def test_asml_stepuntilfixpoint_constructor_args():
    sig = inspect.signature(AsmL_StepUntilFixPoint.__init__)
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



def test_asml_main_is_not_abstract():
    assert not inspect.isabstract(AsmL_Main)


def test_asml_main_constructor_exists():
    assert callable(AsmL_Main.__init__)


def test_asml_main_constructor_args():
    sig = inspect.signature(AsmL_Main.__init__)
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



def test_asml_tuplettype_is_not_abstract():
    assert not inspect.isabstract(AsmL_TupletType)


def test_asml_tuplettype_constructor_exists():
    assert callable(AsmL_TupletType.__init__)


def test_asml_tuplettype_constructor_args():
    sig = inspect.signature(AsmL_TupletType.__init__)
    params = list(sig.parameters.keys())



def test_asml_sequencetype_is_not_abstract():
    assert not inspect.isabstract(AsmL_SequenceType)


def test_asml_sequencetype_constructor_exists():
    assert callable(AsmL_SequenceType.__init__)


def test_asml_sequencetype_constructor_args():
    sig = inspect.signature(AsmL_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_asml_settype_is_not_abstract():
    assert not inspect.isabstract(AsmL_SetType)


def test_asml_settype_constructor_exists():
    assert callable(AsmL_SetType.__init__)


def test_asml_settype_constructor_args():
    sig = inspect.signature(AsmL_SetType.__init__)
    params = list(sig.parameters.keys())



def test_asml_maptype_is_not_abstract():
    assert not inspect.isabstract(AsmL_MapType)


def test_asml_maptype_constructor_exists():
    assert callable(AsmL_MapType.__init__)


def test_asml_maptype_constructor_args():
    sig = inspect.signature(AsmL_MapType.__init__)
    params = list(sig.parameters.keys())



def test_asml_namedtype_is_not_abstract():
    assert not inspect.isabstract(AsmL_NamedType)


def test_asml_namedtype_constructor_exists():
    assert callable(AsmL_NamedType.__init__)


def test_asml_namedtype_constructor_args():
    sig = inspect.signature(AsmL_NamedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml_namedtype_has_name():
    assert hasattr(AsmL_NamedType, "name")
    descriptor = None
    for klass in AsmL_NamedType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_varormethod_is_not_abstract():
    assert not inspect.isabstract(VarOrMethod)


def test_varormethod_constructor_exists():
    assert callable(VarOrMethod.__init__)


def test_varormethod_constructor_args():
    sig = inspect.signature(VarOrMethod.__init__)
    params = list(sig.parameters.keys())



def test_asml_method_is_not_abstract():
    assert not inspect.isabstract(AsmL_Method)


def test_asml_method_constructor_exists():
    assert callable(AsmL_Method.__init__)


def test_asml_method_constructor_args():
    sig = inspect.signature(AsmL_Method.__init__)
    params = list(sig.parameters.keys())
    assert "isEntryPoint" in params, "Missing parameter 'isEntryPoint'"
    assert "isShared" in params, "Missing parameter 'isShared'"
    assert "isOverride" in params, "Missing parameter 'isOverride'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_asml_method_has_isEntryPoint():
    assert hasattr(AsmL_Method, "isEntryPoint")
    descriptor = None
    for klass in AsmL_Method.__mro__:
        if "isEntryPoint" in klass.__dict__:
            descriptor = klass.__dict__["isEntryPoint"]
            break
    assert isinstance(descriptor, property)

def test_asml_method_has_isShared():
    assert hasattr(AsmL_Method, "isShared")
    descriptor = None
    for klass in AsmL_Method.__mro__:
        if "isShared" in klass.__dict__:
            descriptor = klass.__dict__["isShared"]
            break
    assert isinstance(descriptor, property)

def test_asml_method_has_isOverride():
    assert hasattr(AsmL_Method, "isOverride")
    descriptor = None
    for klass in AsmL_Method.__mro__:
        if "isOverride" in klass.__dict__:
            descriptor = klass.__dict__["isOverride"]
            break
    assert isinstance(descriptor, property)

def test_asml_method_has_isAbstract():
    assert hasattr(AsmL_Method, "isAbstract")
    descriptor = None
    for klass in AsmL_Method.__mro__:
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



def test_asml_case_is_not_abstract():
    assert not inspect.isabstract(AsmL_Case)


def test_asml_case_constructor_exists():
    assert callable(AsmL_Case.__init__)


def test_asml_case_constructor_args():
    sig = inspect.signature(AsmL_Case.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml_case_has_name():
    assert hasattr(AsmL_Case, "name")
    descriptor = None
    for klass in AsmL_Case.__mro__:
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



def test_asml_function_is_not_abstract():
    assert not inspect.isabstract(AsmL_Function)


def test_asml_function_constructor_exists():
    assert callable(AsmL_Function.__init__)


def test_asml_function_constructor_args():
    sig = inspect.signature(AsmL_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml_function_has_name():
    assert hasattr(AsmL_Function, "name")
    descriptor = None
    for klass in AsmL_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asml_type_is_not_abstract():
    assert not inspect.isabstract(AsmL_Type)


def test_asml_type_constructor_exists():
    assert callable(AsmL_Type.__init__)


def test_asml_type_constructor_args():
    sig = inspect.signature(AsmL_Type.__init__)
    params = list(sig.parameters.keys())
    assert "withNull" in params, "Missing parameter 'withNull'"

def test_asml_type_has_withNull():
    assert hasattr(AsmL_Type, "withNull")
    descriptor = None
    for klass in AsmL_Type.__mro__:
        if "withNull" in klass.__dict__:
            descriptor = klass.__dict__["withNull"]
            break
    assert isinstance(descriptor, property)



def test_asml_namespace_is_not_abstract():
    assert not inspect.isabstract(AsmL_Namespace)


def test_asml_namespace_constructor_exists():
    assert callable(AsmL_Namespace.__init__)


def test_asml_namespace_constructor_args():
    sig = inspect.signature(AsmL_Namespace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml_namespace_has_name():
    assert hasattr(AsmL_Namespace, "name")
    descriptor = None
    for klass in AsmL_Namespace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asml_class_is_not_abstract():
    assert not inspect.isabstract(AsmL_Class)


def test_asml_class_constructor_exists():
    assert callable(AsmL_Class.__init__)


def test_asml_class_constructor_args():
    sig = inspect.signature(AsmL_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "name" in params, "Missing parameter 'name'"
    assert "superClassName" in params, "Missing parameter 'superClassName'"

def test_asml_class_has_isAbstract():
    assert hasattr(AsmL_Class, "isAbstract")
    descriptor = None
    for klass in AsmL_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_asml_class_has_name():
    assert hasattr(AsmL_Class, "name")
    descriptor = None
    for klass in AsmL_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_asml_class_has_superClassName():
    assert hasattr(AsmL_Class, "superClassName")
    descriptor = None
    for klass in AsmL_Class.__mro__:
        if "superClassName" in klass.__dict__:
            descriptor = klass.__dict__["superClassName"]
            break
    assert isinstance(descriptor, property)



def test_asml_structure_is_not_abstract():
    assert not inspect.isabstract(AsmL_Structure)


def test_asml_structure_constructor_exists():
    assert callable(AsmL_Structure.__init__)


def test_asml_structure_constructor_args():
    sig = inspect.signature(AsmL_Structure.__init__)
    params = list(sig.parameters.keys())
    assert "superStructureName" in params, "Missing parameter 'superStructureName'"
    assert "name" in params, "Missing parameter 'name'"

def test_asml_structure_has_superStructureName():
    assert hasattr(AsmL_Structure, "superStructureName")
    descriptor = None
    for klass in AsmL_Structure.__mro__:
        if "superStructureName" in klass.__dict__:
            descriptor = klass.__dict__["superStructureName"]
            break
    assert isinstance(descriptor, property)

def test_asml_structure_has_name():
    assert hasattr(AsmL_Structure, "name")
    descriptor = None
    for klass in AsmL_Structure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asml_vardeclaration_is_not_abstract():
    assert not inspect.isabstract(AsmL_VarDeclaration)


def test_asml_vardeclaration_constructor_exists():
    assert callable(AsmL_VarDeclaration.__init__)


def test_asml_vardeclaration_constructor_args():
    sig = inspect.signature(AsmL_VarDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isConstant" in params, "Missing parameter 'isConstant'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isDeclaration" in params, "Missing parameter 'isDeclaration'"
    assert "isLocal" in params, "Missing parameter 'isLocal'"

def test_asml_vardeclaration_has_isConstant():
    assert hasattr(AsmL_VarDeclaration, "isConstant")
    descriptor = None
    for klass in AsmL_VarDeclaration.__mro__:
        if "isConstant" in klass.__dict__:
            descriptor = klass.__dict__["isConstant"]
            break
    assert isinstance(descriptor, property)

def test_asml_vardeclaration_has_name():
    assert hasattr(AsmL_VarDeclaration, "name")
    descriptor = None
    for klass in AsmL_VarDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_asml_vardeclaration_has_isDeclaration():
    assert hasattr(AsmL_VarDeclaration, "isDeclaration")
    descriptor = None
    for klass in AsmL_VarDeclaration.__mro__:
        if "isDeclaration" in klass.__dict__:
            descriptor = klass.__dict__["isDeclaration"]
            break
    assert isinstance(descriptor, property)

def test_asml_vardeclaration_has_isLocal():
    assert hasattr(AsmL_VarDeclaration, "isLocal")
    descriptor = None
    for klass in AsmL_VarDeclaration.__mro__:
        if "isLocal" in klass.__dict__:
            descriptor = klass.__dict__["isLocal"]
            break
    assert isinstance(descriptor, property)



def test_asml_enumeration_is_not_abstract():
    assert not inspect.isabstract(AsmL_Enumeration)


def test_asml_enumeration_constructor_exists():
    assert callable(AsmL_Enumeration.__init__)


def test_asml_enumeration_constructor_args():
    sig = inspect.signature(AsmL_Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml_enumeration_has_name():
    assert hasattr(AsmL_Enumeration, "name")
    descriptor = None
    for klass in AsmL_Enumeration.__mro__:
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



def test_asml_mapterm_is_not_abstract():
    assert not inspect.isabstract(AsmL_MapTerm)


def test_asml_mapterm_constructor_exists():
    assert callable(AsmL_MapTerm.__init__)


def test_asml_mapterm_constructor_args():
    sig = inspect.signature(AsmL_MapTerm.__init__)
    params = list(sig.parameters.keys())
    assert "separator" in params, "Missing parameter 'separator'"

def test_asml_mapterm_has_separator():
    assert hasattr(AsmL_MapTerm, "separator")
    descriptor = None
    for klass in AsmL_MapTerm.__mro__:
        if "separator" in klass.__dict__:
            descriptor = klass.__dict__["separator"]
            break
    assert isinstance(descriptor, property)



def test_asml_predicateterm_is_not_abstract():
    assert not inspect.isabstract(AsmL_PredicateTerm)


def test_asml_predicateterm_constructor_exists():
    assert callable(AsmL_PredicateTerm.__init__)


def test_asml_predicateterm_constructor_args():
    sig = inspect.signature(AsmL_PredicateTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml_setterm_is_not_abstract():
    assert not inspect.isabstract(AsmL_SetTerm)


def test_asml_setterm_constructor_exists():
    assert callable(AsmL_SetTerm.__init__)


def test_asml_setterm_constructor_args():
    sig = inspect.signature(AsmL_SetTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml_operator_is_not_abstract():
    assert not inspect.isabstract(AsmL_Operator)


def test_asml_operator_constructor_exists():
    assert callable(AsmL_Operator.__init__)


def test_asml_operator_constructor_args():
    sig = inspect.signature(AsmL_Operator.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_asml_operator_has_opName():
    assert hasattr(AsmL_Operator, "opName")
    descriptor = None
    for klass in AsmL_Operator.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_asml_varterm_is_not_abstract():
    assert not inspect.isabstract(AsmL_VarTerm)


def test_asml_varterm_constructor_exists():
    assert callable(AsmL_VarTerm.__init__)


def test_asml_varterm_constructor_args():
    sig = inspect.signature(AsmL_VarTerm.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml_varterm_has_name():
    assert hasattr(AsmL_VarTerm, "name")
    descriptor = None
    for klass in AsmL_VarTerm.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asml_sequenceterm_is_not_abstract():
    assert not inspect.isabstract(AsmL_SequenceTerm)


def test_asml_sequenceterm_constructor_exists():
    assert callable(AsmL_SequenceTerm.__init__)


def test_asml_sequenceterm_constructor_args():
    sig = inspect.signature(AsmL_SequenceTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml_tulpletterm_is_not_abstract():
    assert not inspect.isabstract(AsmL_TulpletTerm)


def test_asml_tulpletterm_constructor_exists():
    assert callable(AsmL_TulpletTerm.__init__)


def test_asml_tulpletterm_constructor_args():
    sig = inspect.signature(AsmL_TulpletTerm.__init__)
    params = list(sig.parameters.keys())



def test_asml_methodcallterm_is_not_abstract():
    assert not inspect.isabstract(AsmL_MethodCallTerm)


def test_asml_methodcallterm_constructor_exists():
    assert callable(AsmL_MethodCallTerm.__init__)


def test_asml_methodcallterm_constructor_args():
    sig = inspect.signature(AsmL_MethodCallTerm.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml_methodcallterm_has_name():
    assert hasattr(AsmL_MethodCallTerm, "name")
    descriptor = None
    for klass in AsmL_MethodCallTerm.__mro__:
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



def test_asml_addrule_is_not_abstract():
    assert not inspect.isabstract(AsmL_AddRule)


def test_asml_addrule_constructor_exists():
    assert callable(AsmL_AddRule.__init__)


def test_asml_addrule_constructor_args():
    sig = inspect.signature(AsmL_AddRule.__init__)
    params = list(sig.parameters.keys())



def test_asml_removerule_is_not_abstract():
    assert not inspect.isabstract(AsmL_RemoveRule)


def test_asml_removerule_constructor_exists():
    assert callable(AsmL_RemoveRule.__init__)


def test_asml_removerule_constructor_args():
    sig = inspect.signature(AsmL_RemoveRule.__init__)
    params = list(sig.parameters.keys())



def test_asml_chooserule_is_not_abstract():
    assert not inspect.isabstract(AsmL_ChooseRule)


def test_asml_chooserule_constructor_exists():
    assert callable(AsmL_ChooseRule.__init__)


def test_asml_chooserule_constructor_args():
    sig = inspect.signature(AsmL_ChooseRule.__init__)
    params = list(sig.parameters.keys())



def test_asml_forallrule_is_not_abstract():
    assert not inspect.isabstract(AsmL_ForallRule)


def test_asml_forallrule_constructor_exists():
    assert callable(AsmL_ForallRule.__init__)


def test_asml_forallrule_constructor_args():
    sig = inspect.signature(AsmL_ForallRule.__init__)
    params = list(sig.parameters.keys())



def test_asml_conditionalrule_is_not_abstract():
    assert not inspect.isabstract(AsmL_ConditionalRule)


def test_asml_conditionalrule_constructor_exists():
    assert callable(AsmL_ConditionalRule.__init__)


def test_asml_conditionalrule_constructor_args():
    sig = inspect.signature(AsmL_ConditionalRule.__init__)
    params = list(sig.parameters.keys())



def test_asml_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(AsmL_MethodInvocation)


def test_asml_methodinvocation_constructor_exists():
    assert callable(AsmL_MethodInvocation.__init__)


def test_asml_methodinvocation_constructor_args():
    sig = inspect.signature(AsmL_MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_asml_returnrule_is_not_abstract():
    assert not inspect.isabstract(AsmL_ReturnRule)


def test_asml_returnrule_constructor_exists():
    assert callable(AsmL_ReturnRule.__init__)


def test_asml_returnrule_constructor_args():
    sig = inspect.signature(AsmL_ReturnRule.__init__)
    params = list(sig.parameters.keys())



def test_asml_updaterule_is_not_abstract():
    assert not inspect.isabstract(AsmL_UpdateRule)


def test_asml_updaterule_constructor_exists():
    assert callable(AsmL_UpdateRule.__init__)


def test_asml_updaterule_constructor_args():
    sig = inspect.signature(AsmL_UpdateRule.__init__)
    params = list(sig.parameters.keys())



def test_asml_skiprule_is_not_abstract():
    assert not inspect.isabstract(AsmL_SkipRule)


def test_asml_skiprule_constructor_exists():
    assert callable(AsmL_SkipRule.__init__)


def test_asml_skiprule_constructor_args():
    sig = inspect.signature(AsmL_SkipRule.__init__)
    params = list(sig.parameters.keys())



def test_asml_step_is_not_abstract():
    assert not inspect.isabstract(AsmL_Step)


def test_asml_step_constructor_exists():
    assert callable(AsmL_Step.__init__)


def test_asml_step_constructor_args():
    sig = inspect.signature(AsmL_Step.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml_step_has_name():
    assert hasattr(AsmL_Step, "name")
    descriptor = None
    for klass in AsmL_Step.__mro__:
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



def test_asml_inwhereholds_is_not_abstract():
    assert not inspect.isabstract(AsmL_InWhereHolds)


def test_asml_inwhereholds_constructor_exists():
    assert callable(AsmL_InWhereHolds.__init__)


def test_asml_inwhereholds_constructor_args():
    sig = inspect.signature(AsmL_InWhereHolds.__init__)
    params = list(sig.parameters.keys())



def test_asml_parameter_is_not_abstract():
    assert not inspect.isabstract(AsmL_Parameter)


def test_asml_parameter_constructor_exists():
    assert callable(AsmL_Parameter.__init__)


def test_asml_parameter_constructor_args():
    sig = inspect.signature(AsmL_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml_parameter_has_name():
    assert hasattr(AsmL_Parameter, "name")
    descriptor = None
    for klass in AsmL_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asml_asmlfile_is_not_abstract():
    assert not inspect.isabstract(AsmL_AsmLFile)


def test_asml_asmlfile_constructor_exists():
    assert callable(AsmL_AsmLFile.__init__)


def test_asml_asmlfile_constructor_args():
    sig = inspect.signature(AsmL_AsmLFile.__init__)
    params = list(sig.parameters.keys())



def test_asml_varorcase_is_not_abstract():
    assert not inspect.isabstract(AsmL_VarOrCase)


def test_asml_varorcase_constructor_exists():
    assert callable(AsmL_VarOrCase.__init__)


def test_asml_varorcase_constructor_args():
    sig = inspect.signature(AsmL_VarOrCase.__init__)
    params = list(sig.parameters.keys())



def test_asml_enumerator_is_not_abstract():
    assert not inspect.isabstract(AsmL_Enumerator)


def test_asml_enumerator_constructor_exists():
    assert callable(AsmL_Enumerator.__init__)


def test_asml_enumerator_constructor_args():
    sig = inspect.signature(AsmL_Enumerator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asml_enumerator_has_name():
    assert hasattr(AsmL_Enumerator, "name")
    descriptor = None
    for klass in AsmL_Enumerator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asml_initially_is_not_abstract():
    assert not inspect.isabstract(AsmL_Initially)


def test_asml_initially_constructor_exists():
    assert callable(AsmL_Initially.__init__)


def test_asml_initially_constructor_args():
    sig = inspect.signature(AsmL_Initially.__init__)
    params = list(sig.parameters.keys())



def test_asml_varormethod_is_not_abstract():
    assert not inspect.isabstract(AsmL_VarOrMethod)


def test_asml_varormethod_constructor_exists():
    assert callable(AsmL_VarOrMethod.__init__)


def test_asml_varormethod_constructor_args():
    sig = inspect.signature(AsmL_VarOrMethod.__init__)
    params = list(sig.parameters.keys())



def test_asml_rule_is_not_abstract():
    assert not inspect.isabstract(AsmL_Rule)


def test_asml_rule_constructor_exists():
    assert callable(AsmL_Rule.__init__)


def test_asml_rule_constructor_args():
    sig = inspect.signature(AsmL_Rule.__init__)
    params = list(sig.parameters.keys())



def test_asml_asmlelement_is_not_abstract():
    assert not inspect.isabstract(AsmL_AsmLElement)


def test_asml_asmlelement_constructor_exists():
    assert callable(AsmL_AsmLElement.__init__)


def test_asml_asmlelement_constructor_args():
    sig = inspect.signature(AsmL_AsmLElement.__init__)
    params = list(sig.parameters.keys())



def test_asml_term_is_not_abstract():
    assert not inspect.isabstract(AsmL_Term)


def test_asml_term_constructor_exists():
    assert callable(AsmL_Term.__init__)


def test_asml_term_constructor_args():
    sig = inspect.signature(AsmL_Term.__init__)
    params = list(sig.parameters.keys())



def test_asml_body_is_not_abstract():
    assert not inspect.isabstract(AsmL_Body)


def test_asml_body_constructor_exists():
    assert callable(AsmL_Body.__init__)


def test_asml_body_constructor_args():
    sig = inspect.signature(AsmL_Body.__init__)
    params = list(sig.parameters.keys())



def test_asml_locatedelement_is_not_abstract():
    assert not inspect.isabstract(AsmL_LocatedElement)


def test_asml_locatedelement_constructor_exists():
    assert callable(AsmL_LocatedElement.__init__)


def test_asml_locatedelement_constructor_args():
    sig = inspect.signature(AsmL_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"

def test_asml_locatedelement_has_location():
    assert hasattr(AsmL_LocatedElement, "location")
    descriptor = None
    for klass in AsmL_LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_asml_locatedelement_has_commentsBefore():
    assert hasattr(AsmL_LocatedElement, "commentsBefore")
    descriptor = None
    for klass in AsmL_LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_asml_locatedelement_has_commentsAfter():
    assert hasattr(AsmL_LocatedElement, "commentsAfter")
    descriptor = None
    for klass in AsmL_LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)



def test_constant_is_not_abstract():
    assert not inspect.isabstract(Constant)


def test_constant_constructor_exists():
    assert callable(Constant.__init__)


def test_constant_constructor_args():
    sig = inspect.signature(Constant.__init__)
    params = list(sig.parameters.keys())



def test_asml_integerconstant_is_not_abstract():
    assert not inspect.isabstract(AsmL_IntegerConstant)


def test_asml_integerconstant_constructor_exists():
    assert callable(AsmL_IntegerConstant.__init__)


def test_asml_integerconstant_constructor_args():
    sig = inspect.signature(AsmL_IntegerConstant.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_asml_integerconstant_has_val():
    assert hasattr(AsmL_IntegerConstant, "val")
    descriptor = None
    for klass in AsmL_IntegerConstant.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_asml_stringconstant_is_not_abstract():
    assert not inspect.isabstract(AsmL_StringConstant)


def test_asml_stringconstant_constructor_exists():
    assert callable(AsmL_StringConstant.__init__)


def test_asml_stringconstant_constructor_args():
    sig = inspect.signature(AsmL_StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_asml_stringconstant_has_val():
    assert hasattr(AsmL_StringConstant, "val")
    descriptor = None
    for klass in AsmL_StringConstant.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_asml_nullconstant_is_not_abstract():
    assert not inspect.isabstract(AsmL_NullConstant)


def test_asml_nullconstant_constructor_exists():
    assert callable(AsmL_NullConstant.__init__)


def test_asml_nullconstant_constructor_args():
    sig = inspect.signature(AsmL_NullConstant.__init__)
    params = list(sig.parameters.keys())



def test_asml_booleanconstant_is_not_abstract():
    assert not inspect.isabstract(AsmL_BooleanConstant)


def test_asml_booleanconstant_constructor_exists():
    assert callable(AsmL_BooleanConstant.__init__)


def test_asml_booleanconstant_constructor_args():
    sig = inspect.signature(AsmL_BooleanConstant.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_asml_booleanconstant_has_val():
    assert hasattr(AsmL_BooleanConstant, "val")
    descriptor = None
    for klass in AsmL_BooleanConstant.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_asml_constant_is_not_abstract():
    assert not inspect.isabstract(AsmL_Constant)


def test_asml_constant_constructor_exists():
    assert callable(AsmL_Constant.__init__)


def test_asml_constant_constructor_args():
    sig = inspect.signature(AsmL_Constant.__init__)
    params = list(sig.parameters.keys())



def test_asml_rangesequence_is_not_abstract():
    assert not inspect.isabstract(AsmL_RangeSequence)


def test_asml_rangesequence_constructor_exists():
    assert callable(AsmL_RangeSequence.__init__)


def test_asml_rangesequence_constructor_args():
    sig = inspect.signature(AsmL_RangeSequence.__init__)
    params = list(sig.parameters.keys())


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
SequenceTerm_strategy = st.builds(
    SequenceTerm,
)
AsmL_EnumerateSequence_strategy = st.builds(
    AsmL_EnumerateSequence,
)
SetTerm_strategy = st.builds(
    SetTerm,
)
AsmL_AlgorithmSet_strategy = st.builds(
    AsmL_AlgorithmSet,
)
AsmL_RangeSet_strategy = st.builds(
    AsmL_RangeSet,
)
AsmL_EnumerateSet_strategy = st.builds(
    AsmL_EnumerateSet,
)
PredicateTerm_strategy = st.builds(
    PredicateTerm,
)
AsmL_AnyIn_strategy = st.builds(
    AsmL_AnyIn,
)
AsmL_ExistsTerm_strategy = st.builds(
    AsmL_ExistsTerm,
    isUnique=
        safe_text
)
AsmL_ForAllTerm_strategy = st.builds(
    AsmL_ForAllTerm,
)
ConditionalRule_strategy = st.builds(
    ConditionalRule,
)
AsmL_ElseIf_strategy = st.builds(
    AsmL_ElseIf,
)
ElseIf_strategy = st.builds(
    ElseIf,
)
UpdateRule_strategy = st.builds(
    UpdateRule,
)
AsmL_UpdateMapRule_strategy = st.builds(
    AsmL_UpdateMapRule,
)
AsmL_UpdateFieldRule_strategy = st.builds(
    AsmL_UpdateFieldRule,
)
AsmL_UpdateVarRule_strategy = st.builds(
    AsmL_UpdateVarRule,
)
MethodCallTerm_strategy = st.builds(
    MethodCallTerm,
)
AsmL_NewInstance_strategy = st.builds(
    AsmL_NewInstance,
)
InWhereHolds_strategy = st.builds(
    InWhereHolds,
)
StepExpression_strategy = st.builds(
    StepExpression,
)
AsmL_StepUntil_strategy = st.builds(
    AsmL_StepUntil,
)
AsmL_StepWhile_strategy = st.builds(
    AsmL_StepWhile,
)
Step_strategy = st.builds(
    Step,
)
AsmL_StepForEach_strategy = st.builds(
    AsmL_StepForEach,
)
AsmL_StepExpression_strategy = st.builds(
    AsmL_StepExpression,
)
AsmL_StepUntilFixPoint_strategy = st.builds(
    AsmL_StepUntilFixPoint,
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
AsmL_Main_strategy = st.builds(
    AsmL_Main,
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
AsmL_TupletType_strategy = st.builds(
    AsmL_TupletType,
)
AsmL_SequenceType_strategy = st.builds(
    AsmL_SequenceType,
)
AsmL_SetType_strategy = st.builds(
    AsmL_SetType,
)
AsmL_MapType_strategy = st.builds(
    AsmL_MapType,
)
AsmL_NamedType_strategy = st.builds(
    AsmL_NamedType,
    name=
        safe_text
)
VarOrMethod_strategy = st.builds(
    VarOrMethod,
)
AsmL_Method_strategy = st.builds(
    AsmL_Method,
    isEntryPoint=
        safe_text,
    isShared=
        safe_text,
    isOverride=
        safe_text,
    isAbstract=
        safe_text
)
VarOrCase_strategy = st.builds(
    VarOrCase,
)
AsmL_Case_strategy = st.builds(
    AsmL_Case,
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
AsmL_Function_strategy = st.builds(
    AsmL_Function,
    name=
        safe_text
)
AsmL_Type_strategy = st.builds(
    AsmL_Type,
    withNull=
        safe_text
)
AsmL_Namespace_strategy = st.builds(
    AsmL_Namespace,
    name=
        safe_text
)
AsmL_Class_strategy = st.builds(
    AsmL_Class,
    isAbstract=
        safe_text,
    name=
        safe_text,
    superClassName=
        safe_text
)
AsmL_Structure_strategy = st.builds(
    AsmL_Structure,
    superStructureName=
        safe_text,
    name=
        safe_text
)
AsmL_VarDeclaration_strategy = st.builds(
    AsmL_VarDeclaration,
    isConstant=
        safe_text,
    name=
        safe_text,
    isDeclaration=
        safe_text,
    isLocal=
        safe_text
)
AsmL_Enumeration_strategy = st.builds(
    AsmL_Enumeration,
    name=
        safe_text
)
Term_strategy = st.builds(
    Term,
)
AsmL_MapTerm_strategy = st.builds(
    AsmL_MapTerm,
    separator=
        safe_text
)
AsmL_PredicateTerm_strategy = st.builds(
    AsmL_PredicateTerm,
)
AsmL_SetTerm_strategy = st.builds(
    AsmL_SetTerm,
)
AsmL_Operator_strategy = st.builds(
    AsmL_Operator,
    opName=
        safe_text
)
AsmL_VarTerm_strategy = st.builds(
    AsmL_VarTerm,
    name=
        safe_text
)
AsmL_SequenceTerm_strategy = st.builds(
    AsmL_SequenceTerm,
)
AsmL_TulpletTerm_strategy = st.builds(
    AsmL_TulpletTerm,
)
AsmL_MethodCallTerm_strategy = st.builds(
    AsmL_MethodCallTerm,
    name=
        safe_text
)
Rule_strategy = st.builds(
    Rule,
)
AsmL_AddRule_strategy = st.builds(
    AsmL_AddRule,
)
AsmL_RemoveRule_strategy = st.builds(
    AsmL_RemoveRule,
)
AsmL_ChooseRule_strategy = st.builds(
    AsmL_ChooseRule,
)
AsmL_ForallRule_strategy = st.builds(
    AsmL_ForallRule,
)
AsmL_ConditionalRule_strategy = st.builds(
    AsmL_ConditionalRule,
)
AsmL_MethodInvocation_strategy = st.builds(
    AsmL_MethodInvocation,
)
AsmL_ReturnRule_strategy = st.builds(
    AsmL_ReturnRule,
)
AsmL_UpdateRule_strategy = st.builds(
    AsmL_UpdateRule,
)
AsmL_SkipRule_strategy = st.builds(
    AsmL_SkipRule,
)
AsmL_Step_strategy = st.builds(
    AsmL_Step,
    name=
        safe_text
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
AsmL_InWhereHolds_strategy = st.builds(
    AsmL_InWhereHolds,
)
AsmL_Parameter_strategy = st.builds(
    AsmL_Parameter,
    name=
        safe_text
)
AsmL_AsmLFile_strategy = st.builds(
    AsmL_AsmLFile,
)
AsmL_VarOrCase_strategy = st.builds(
    AsmL_VarOrCase,
)
AsmL_Enumerator_strategy = st.builds(
    AsmL_Enumerator,
    name=
        safe_text
)
AsmL_Initially_strategy = st.builds(
    AsmL_Initially,
)
AsmL_VarOrMethod_strategy = st.builds(
    AsmL_VarOrMethod,
)
AsmL_Rule_strategy = st.builds(
    AsmL_Rule,
)
AsmL_AsmLElement_strategy = st.builds(
    AsmL_AsmLElement,
)
AsmL_Term_strategy = st.builds(
    AsmL_Term,
)
AsmL_Body_strategy = st.builds(
    AsmL_Body,
)
AsmL_LocatedElement_strategy = st.builds(
    AsmL_LocatedElement,
    location=
        safe_text,
    commentsBefore=
        safe_text,
    commentsAfter=
        safe_text
)
Constant_strategy = st.builds(
    Constant,
)
AsmL_IntegerConstant_strategy = st.builds(
    AsmL_IntegerConstant,
    val=
        safe_text
)
AsmL_StringConstant_strategy = st.builds(
    AsmL_StringConstant,
    val=
        safe_text
)
AsmL_NullConstant_strategy = st.builds(
    AsmL_NullConstant,
)
AsmL_BooleanConstant_strategy = st.builds(
    AsmL_BooleanConstant,
    val=
        safe_text
)
AsmL_Constant_strategy = st.builds(
    AsmL_Constant,
)
AsmL_RangeSequence_strategy = st.builds(
    AsmL_RangeSequence,
)

@given(instance=SequenceTerm_strategy)
@settings(max_examples=50)
def test_sequenceterm_instantiation(instance):
    assert isinstance(instance, SequenceTerm)

@given(instance=AsmL_EnumerateSequence_strategy)
@settings(max_examples=50)
def test_asml_enumeratesequence_instantiation(instance):
    assert isinstance(instance, AsmL_EnumerateSequence)

@given(instance=SetTerm_strategy)
@settings(max_examples=50)
def test_setterm_instantiation(instance):
    assert isinstance(instance, SetTerm)

@given(instance=AsmL_AlgorithmSet_strategy)
@settings(max_examples=50)
def test_asml_algorithmset_instantiation(instance):
    assert isinstance(instance, AsmL_AlgorithmSet)

@given(instance=AsmL_RangeSet_strategy)
@settings(max_examples=50)
def test_asml_rangeset_instantiation(instance):
    assert isinstance(instance, AsmL_RangeSet)

@given(instance=AsmL_EnumerateSet_strategy)
@settings(max_examples=50)
def test_asml_enumerateset_instantiation(instance):
    assert isinstance(instance, AsmL_EnumerateSet)

@given(instance=PredicateTerm_strategy)
@settings(max_examples=50)
def test_predicateterm_instantiation(instance):
    assert isinstance(instance, PredicateTerm)

@given(instance=AsmL_AnyIn_strategy)
@settings(max_examples=50)
def test_asml_anyin_instantiation(instance):
    assert isinstance(instance, AsmL_AnyIn)

@given(instance=AsmL_ExistsTerm_strategy)
@settings(max_examples=50)
def test_asml_existsterm_instantiation(instance):
    assert isinstance(instance, AsmL_ExistsTerm)



@given(instance=AsmL_ExistsTerm_strategy)
def test_asml_existsterm_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=AsmL_ForAllTerm_strategy)
@settings(max_examples=50)
def test_asml_forallterm_instantiation(instance):
    assert isinstance(instance, AsmL_ForAllTerm)

@given(instance=ConditionalRule_strategy)
@settings(max_examples=50)
def test_conditionalrule_instantiation(instance):
    assert isinstance(instance, ConditionalRule)

@given(instance=AsmL_ElseIf_strategy)
@settings(max_examples=50)
def test_asml_elseif_instantiation(instance):
    assert isinstance(instance, AsmL_ElseIf)

@given(instance=ElseIf_strategy)
@settings(max_examples=50)
def test_elseif_instantiation(instance):
    assert isinstance(instance, ElseIf)

@given(instance=UpdateRule_strategy)
@settings(max_examples=50)
def test_updaterule_instantiation(instance):
    assert isinstance(instance, UpdateRule)

@given(instance=AsmL_UpdateMapRule_strategy)
@settings(max_examples=50)
def test_asml_updatemaprule_instantiation(instance):
    assert isinstance(instance, AsmL_UpdateMapRule)

@given(instance=AsmL_UpdateFieldRule_strategy)
@settings(max_examples=50)
def test_asml_updatefieldrule_instantiation(instance):
    assert isinstance(instance, AsmL_UpdateFieldRule)

@given(instance=AsmL_UpdateVarRule_strategy)
@settings(max_examples=50)
def test_asml_updatevarrule_instantiation(instance):
    assert isinstance(instance, AsmL_UpdateVarRule)

@given(instance=MethodCallTerm_strategy)
@settings(max_examples=50)
def test_methodcallterm_instantiation(instance):
    assert isinstance(instance, MethodCallTerm)

@given(instance=AsmL_NewInstance_strategy)
@settings(max_examples=50)
def test_asml_newinstance_instantiation(instance):
    assert isinstance(instance, AsmL_NewInstance)

@given(instance=InWhereHolds_strategy)
@settings(max_examples=50)
def test_inwhereholds_instantiation(instance):
    assert isinstance(instance, InWhereHolds)

@given(instance=StepExpression_strategy)
@settings(max_examples=50)
def test_stepexpression_instantiation(instance):
    assert isinstance(instance, StepExpression)

@given(instance=AsmL_StepUntil_strategy)
@settings(max_examples=50)
def test_asml_stepuntil_instantiation(instance):
    assert isinstance(instance, AsmL_StepUntil)

@given(instance=AsmL_StepWhile_strategy)
@settings(max_examples=50)
def test_asml_stepwhile_instantiation(instance):
    assert isinstance(instance, AsmL_StepWhile)

@given(instance=Step_strategy)
@settings(max_examples=50)
def test_step_instantiation(instance):
    assert isinstance(instance, Step)

@given(instance=AsmL_StepForEach_strategy)
@settings(max_examples=50)
def test_asml_stepforeach_instantiation(instance):
    assert isinstance(instance, AsmL_StepForEach)

@given(instance=AsmL_StepExpression_strategy)
@settings(max_examples=50)
def test_asml_stepexpression_instantiation(instance):
    assert isinstance(instance, AsmL_StepExpression)

@given(instance=AsmL_StepUntilFixPoint_strategy)
@settings(max_examples=50)
def test_asml_stepuntilfixpoint_instantiation(instance):
    assert isinstance(instance, AsmL_StepUntilFixPoint)

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

@given(instance=AsmL_Main_strategy)
@settings(max_examples=50)
def test_asml_main_instantiation(instance):
    assert isinstance(instance, AsmL_Main)

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

@given(instance=AsmL_TupletType_strategy)
@settings(max_examples=50)
def test_asml_tuplettype_instantiation(instance):
    assert isinstance(instance, AsmL_TupletType)

@given(instance=AsmL_SequenceType_strategy)
@settings(max_examples=50)
def test_asml_sequencetype_instantiation(instance):
    assert isinstance(instance, AsmL_SequenceType)

@given(instance=AsmL_SetType_strategy)
@settings(max_examples=50)
def test_asml_settype_instantiation(instance):
    assert isinstance(instance, AsmL_SetType)

@given(instance=AsmL_MapType_strategy)
@settings(max_examples=50)
def test_asml_maptype_instantiation(instance):
    assert isinstance(instance, AsmL_MapType)

@given(instance=AsmL_NamedType_strategy)
@settings(max_examples=50)
def test_asml_namedtype_instantiation(instance):
    assert isinstance(instance, AsmL_NamedType)



@given(instance=AsmL_NamedType_strategy)
def test_asml_namedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=VarOrMethod_strategy)
@settings(max_examples=50)
def test_varormethod_instantiation(instance):
    assert isinstance(instance, VarOrMethod)

@given(instance=AsmL_Method_strategy)
@settings(max_examples=50)
def test_asml_method_instantiation(instance):
    assert isinstance(instance, AsmL_Method)



@given(instance=AsmL_Method_strategy)
def test_asml_method_isEntryPoint_setter(instance):
    original = instance.isEntryPoint
    instance.isEntryPoint = original
    assert instance.isEntryPoint == original



@given(instance=AsmL_Method_strategy)
def test_asml_method_isShared_setter(instance):
    original = instance.isShared
    instance.isShared = original
    assert instance.isShared == original



@given(instance=AsmL_Method_strategy)
def test_asml_method_isOverride_setter(instance):
    original = instance.isOverride
    instance.isOverride = original
    assert instance.isOverride == original



@given(instance=AsmL_Method_strategy)
def test_asml_method_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=VarOrCase_strategy)
@settings(max_examples=50)
def test_varorcase_instantiation(instance):
    assert isinstance(instance, VarOrCase)

@given(instance=AsmL_Case_strategy)
@settings(max_examples=50)
def test_asml_case_instantiation(instance):
    assert isinstance(instance, AsmL_Case)



@given(instance=AsmL_Case_strategy)
def test_asml_case_name_setter(instance):
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

@given(instance=AsmL_Function_strategy)
@settings(max_examples=50)
def test_asml_function_instantiation(instance):
    assert isinstance(instance, AsmL_Function)



@given(instance=AsmL_Function_strategy)
def test_asml_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmL_Type_strategy)
@settings(max_examples=50)
def test_asml_type_instantiation(instance):
    assert isinstance(instance, AsmL_Type)



@given(instance=AsmL_Type_strategy)
def test_asml_type_withNull_setter(instance):
    original = instance.withNull
    instance.withNull = original
    assert instance.withNull == original

@given(instance=AsmL_Namespace_strategy)
@settings(max_examples=50)
def test_asml_namespace_instantiation(instance):
    assert isinstance(instance, AsmL_Namespace)



@given(instance=AsmL_Namespace_strategy)
def test_asml_namespace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmL_Class_strategy)
@settings(max_examples=50)
def test_asml_class_instantiation(instance):
    assert isinstance(instance, AsmL_Class)



@given(instance=AsmL_Class_strategy)
def test_asml_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=AsmL_Class_strategy)
def test_asml_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=AsmL_Class_strategy)
def test_asml_class_superClassName_setter(instance):
    original = instance.superClassName
    instance.superClassName = original
    assert instance.superClassName == original

@given(instance=AsmL_Structure_strategy)
@settings(max_examples=50)
def test_asml_structure_instantiation(instance):
    assert isinstance(instance, AsmL_Structure)



@given(instance=AsmL_Structure_strategy)
def test_asml_structure_superStructureName_setter(instance):
    original = instance.superStructureName
    instance.superStructureName = original
    assert instance.superStructureName == original



@given(instance=AsmL_Structure_strategy)
def test_asml_structure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmL_VarDeclaration_strategy)
@settings(max_examples=50)
def test_asml_vardeclaration_instantiation(instance):
    assert isinstance(instance, AsmL_VarDeclaration)



@given(instance=AsmL_VarDeclaration_strategy)
def test_asml_vardeclaration_isConstant_setter(instance):
    original = instance.isConstant
    instance.isConstant = original
    assert instance.isConstant == original



@given(instance=AsmL_VarDeclaration_strategy)
def test_asml_vardeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=AsmL_VarDeclaration_strategy)
def test_asml_vardeclaration_isDeclaration_setter(instance):
    original = instance.isDeclaration
    instance.isDeclaration = original
    assert instance.isDeclaration == original



@given(instance=AsmL_VarDeclaration_strategy)
def test_asml_vardeclaration_isLocal_setter(instance):
    original = instance.isLocal
    instance.isLocal = original
    assert instance.isLocal == original

@given(instance=AsmL_Enumeration_strategy)
@settings(max_examples=50)
def test_asml_enumeration_instantiation(instance):
    assert isinstance(instance, AsmL_Enumeration)



@given(instance=AsmL_Enumeration_strategy)
def test_asml_enumeration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=AsmL_MapTerm_strategy)
@settings(max_examples=50)
def test_asml_mapterm_instantiation(instance):
    assert isinstance(instance, AsmL_MapTerm)



@given(instance=AsmL_MapTerm_strategy)
def test_asml_mapterm_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original

@given(instance=AsmL_PredicateTerm_strategy)
@settings(max_examples=50)
def test_asml_predicateterm_instantiation(instance):
    assert isinstance(instance, AsmL_PredicateTerm)

@given(instance=AsmL_SetTerm_strategy)
@settings(max_examples=50)
def test_asml_setterm_instantiation(instance):
    assert isinstance(instance, AsmL_SetTerm)

@given(instance=AsmL_Operator_strategy)
@settings(max_examples=50)
def test_asml_operator_instantiation(instance):
    assert isinstance(instance, AsmL_Operator)



@given(instance=AsmL_Operator_strategy)
def test_asml_operator_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=AsmL_VarTerm_strategy)
@settings(max_examples=50)
def test_asml_varterm_instantiation(instance):
    assert isinstance(instance, AsmL_VarTerm)



@given(instance=AsmL_VarTerm_strategy)
def test_asml_varterm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmL_SequenceTerm_strategy)
@settings(max_examples=50)
def test_asml_sequenceterm_instantiation(instance):
    assert isinstance(instance, AsmL_SequenceTerm)

@given(instance=AsmL_TulpletTerm_strategy)
@settings(max_examples=50)
def test_asml_tulpletterm_instantiation(instance):
    assert isinstance(instance, AsmL_TulpletTerm)

@given(instance=AsmL_MethodCallTerm_strategy)
@settings(max_examples=50)
def test_asml_methodcallterm_instantiation(instance):
    assert isinstance(instance, AsmL_MethodCallTerm)



@given(instance=AsmL_MethodCallTerm_strategy)
def test_asml_methodcallterm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=AsmL_AddRule_strategy)
@settings(max_examples=50)
def test_asml_addrule_instantiation(instance):
    assert isinstance(instance, AsmL_AddRule)

@given(instance=AsmL_RemoveRule_strategy)
@settings(max_examples=50)
def test_asml_removerule_instantiation(instance):
    assert isinstance(instance, AsmL_RemoveRule)

@given(instance=AsmL_ChooseRule_strategy)
@settings(max_examples=50)
def test_asml_chooserule_instantiation(instance):
    assert isinstance(instance, AsmL_ChooseRule)

@given(instance=AsmL_ForallRule_strategy)
@settings(max_examples=50)
def test_asml_forallrule_instantiation(instance):
    assert isinstance(instance, AsmL_ForallRule)

@given(instance=AsmL_ConditionalRule_strategy)
@settings(max_examples=50)
def test_asml_conditionalrule_instantiation(instance):
    assert isinstance(instance, AsmL_ConditionalRule)

@given(instance=AsmL_MethodInvocation_strategy)
@settings(max_examples=50)
def test_asml_methodinvocation_instantiation(instance):
    assert isinstance(instance, AsmL_MethodInvocation)

@given(instance=AsmL_ReturnRule_strategy)
@settings(max_examples=50)
def test_asml_returnrule_instantiation(instance):
    assert isinstance(instance, AsmL_ReturnRule)

@given(instance=AsmL_UpdateRule_strategy)
@settings(max_examples=50)
def test_asml_updaterule_instantiation(instance):
    assert isinstance(instance, AsmL_UpdateRule)

@given(instance=AsmL_SkipRule_strategy)
@settings(max_examples=50)
def test_asml_skiprule_instantiation(instance):
    assert isinstance(instance, AsmL_SkipRule)

@given(instance=AsmL_Step_strategy)
@settings(max_examples=50)
def test_asml_step_instantiation(instance):
    assert isinstance(instance, AsmL_Step)



@given(instance=AsmL_Step_strategy)
def test_asml_step_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=AsmL_InWhereHolds_strategy)
@settings(max_examples=50)
def test_asml_inwhereholds_instantiation(instance):
    assert isinstance(instance, AsmL_InWhereHolds)

@given(instance=AsmL_Parameter_strategy)
@settings(max_examples=50)
def test_asml_parameter_instantiation(instance):
    assert isinstance(instance, AsmL_Parameter)



@given(instance=AsmL_Parameter_strategy)
def test_asml_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmL_AsmLFile_strategy)
@settings(max_examples=50)
def test_asml_asmlfile_instantiation(instance):
    assert isinstance(instance, AsmL_AsmLFile)

@given(instance=AsmL_VarOrCase_strategy)
@settings(max_examples=50)
def test_asml_varorcase_instantiation(instance):
    assert isinstance(instance, AsmL_VarOrCase)

@given(instance=AsmL_Enumerator_strategy)
@settings(max_examples=50)
def test_asml_enumerator_instantiation(instance):
    assert isinstance(instance, AsmL_Enumerator)



@given(instance=AsmL_Enumerator_strategy)
def test_asml_enumerator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AsmL_Initially_strategy)
@settings(max_examples=50)
def test_asml_initially_instantiation(instance):
    assert isinstance(instance, AsmL_Initially)

@given(instance=AsmL_VarOrMethod_strategy)
@settings(max_examples=50)
def test_asml_varormethod_instantiation(instance):
    assert isinstance(instance, AsmL_VarOrMethod)

@given(instance=AsmL_Rule_strategy)
@settings(max_examples=50)
def test_asml_rule_instantiation(instance):
    assert isinstance(instance, AsmL_Rule)

@given(instance=AsmL_AsmLElement_strategy)
@settings(max_examples=50)
def test_asml_asmlelement_instantiation(instance):
    assert isinstance(instance, AsmL_AsmLElement)

@given(instance=AsmL_Term_strategy)
@settings(max_examples=50)
def test_asml_term_instantiation(instance):
    assert isinstance(instance, AsmL_Term)

@given(instance=AsmL_Body_strategy)
@settings(max_examples=50)
def test_asml_body_instantiation(instance):
    assert isinstance(instance, AsmL_Body)

@given(instance=AsmL_LocatedElement_strategy)
@settings(max_examples=50)
def test_asml_locatedelement_instantiation(instance):
    assert isinstance(instance, AsmL_LocatedElement)



@given(instance=AsmL_LocatedElement_strategy)
def test_asml_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=AsmL_LocatedElement_strategy)
def test_asml_locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original



@given(instance=AsmL_LocatedElement_strategy)
def test_asml_locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=Constant_strategy)
@settings(max_examples=50)
def test_constant_instantiation(instance):
    assert isinstance(instance, Constant)

@given(instance=AsmL_IntegerConstant_strategy)
@settings(max_examples=50)
def test_asml_integerconstant_instantiation(instance):
    assert isinstance(instance, AsmL_IntegerConstant)



@given(instance=AsmL_IntegerConstant_strategy)
def test_asml_integerconstant_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=AsmL_StringConstant_strategy)
@settings(max_examples=50)
def test_asml_stringconstant_instantiation(instance):
    assert isinstance(instance, AsmL_StringConstant)



@given(instance=AsmL_StringConstant_strategy)
def test_asml_stringconstant_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=AsmL_NullConstant_strategy)
@settings(max_examples=50)
def test_asml_nullconstant_instantiation(instance):
    assert isinstance(instance, AsmL_NullConstant)

@given(instance=AsmL_BooleanConstant_strategy)
@settings(max_examples=50)
def test_asml_booleanconstant_instantiation(instance):
    assert isinstance(instance, AsmL_BooleanConstant)



@given(instance=AsmL_BooleanConstant_strategy)
def test_asml_booleanconstant_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=AsmL_Constant_strategy)
@settings(max_examples=50)
def test_asml_constant_instantiation(instance):
    assert isinstance(instance, AsmL_Constant)

@given(instance=AsmL_RangeSequence_strategy)
@settings(max_examples=50)
def test_asml_rangesequence_instantiation(instance):
    assert isinstance(instance, AsmL_RangeSequence)
