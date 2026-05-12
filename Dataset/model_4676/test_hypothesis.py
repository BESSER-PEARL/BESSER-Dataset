import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RenMapping,
    Maude_OpTypedMapping,
    Maude_OpMapping,
    Maude_SortMapping,
    ViewMapping,
    Maude_TermMapping,
    Maude_ViewMapping,
    Maude_LabelMapping,
    Term,
    Maude_Variable,
    Maude_Constant,
    EquationalCond,
    Maude_MatchingCond,
    Maude_EqualCond,
    Maude_BooleanCond,
    Maude_MembershipCond,
    Condition,
    Maude_RewriteCond,
    Maude_EquationalCond,
    Maude_RecTerm,
    Maude_Term,
    Statement,
    Maude_Rule,
    Maude_Membership,
    Maude_Condition,
    Maude_Equation,
    Maude_Type,
    ModElement,
    Maude_SubsortRel,
    Maude_Statement,
    Maude_Operation,
    Maude_ModImportation,
    Module,
    Maude_SModule,
    Maude_FModule,
    Theory,
    Maude_STheory,
    Maude_FTheory,
    Maude_ModElement,
    MaudeTopEl,
    Type,
    Maude_Kind,
    Maude_Sort,
    Maude_Theory,
    Maude_Module,
    Maude_RenMapping,
    Maude_View,
    ModExpression,
    Maude_TheoryIdModExp,
    Maude_RenModExp,
    Maude_CompModExp,
    Maude_ModuleIdModExp,
    Maude_InstModExp,
    Maude_ModExpression,
    Maude_MaudeTopEl,
    Maude_MaudeSpec,
    Maude_Parameter,
    ImportationMode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_renmapping_is_not_abstract():
    assert not inspect.isabstract(RenMapping)


def test_renmapping_constructor_exists():
    assert callable(RenMapping.__init__)


def test_renmapping_constructor_args():
    sig = inspect.signature(RenMapping.__init__)
    params = list(sig.parameters.keys())



def test_maude_optypedmapping_is_not_abstract():
    assert not inspect.isabstract(Maude_OpTypedMapping)


def test_maude_optypedmapping_constructor_exists():
    assert callable(Maude_OpTypedMapping.__init__)


def test_maude_optypedmapping_constructor_args():
    sig = inspect.signature(Maude_OpTypedMapping.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"
    assert "atts" in params, "Missing parameter 'atts'"

def test_maude_optypedmapping_has_to():
    assert hasattr(Maude_OpTypedMapping, "to")
    descriptor = None
    for klass in Maude_OpTypedMapping.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_maude_optypedmapping_has_atts():
    assert hasattr(Maude_OpTypedMapping, "atts")
    descriptor = None
    for klass in Maude_OpTypedMapping.__mro__:
        if "atts" in klass.__dict__:
            descriptor = klass.__dict__["atts"]
            break
    assert isinstance(descriptor, property)



def test_maude_opmapping_is_not_abstract():
    assert not inspect.isabstract(Maude_OpMapping)


def test_maude_opmapping_constructor_exists():
    assert callable(Maude_OpMapping.__init__)


def test_maude_opmapping_constructor_args():
    sig = inspect.signature(Maude_OpMapping.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"

def test_maude_opmapping_has_to():
    assert hasattr(Maude_OpMapping, "to")
    descriptor = None
    for klass in Maude_OpMapping.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_maude_sortmapping_is_not_abstract():
    assert not inspect.isabstract(Maude_SortMapping)


def test_maude_sortmapping_constructor_exists():
    assert callable(Maude_SortMapping.__init__)


def test_maude_sortmapping_constructor_args():
    sig = inspect.signature(Maude_SortMapping.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"

def test_maude_sortmapping_has_to():
    assert hasattr(Maude_SortMapping, "to")
    descriptor = None
    for klass in Maude_SortMapping.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_viewmapping_is_not_abstract():
    assert not inspect.isabstract(ViewMapping)


def test_viewmapping_constructor_exists():
    assert callable(ViewMapping.__init__)


def test_viewmapping_constructor_args():
    sig = inspect.signature(ViewMapping.__init__)
    params = list(sig.parameters.keys())



def test_maude_termmapping_is_not_abstract():
    assert not inspect.isabstract(Maude_TermMapping)


def test_maude_termmapping_constructor_exists():
    assert callable(Maude_TermMapping.__init__)


def test_maude_termmapping_constructor_args():
    sig = inspect.signature(Maude_TermMapping.__init__)
    params = list(sig.parameters.keys())



def test_maude_viewmapping_is_not_abstract():
    assert not inspect.isabstract(Maude_ViewMapping)


def test_maude_viewmapping_constructor_exists():
    assert callable(Maude_ViewMapping.__init__)


def test_maude_viewmapping_constructor_args():
    sig = inspect.signature(Maude_ViewMapping.__init__)
    params = list(sig.parameters.keys())



def test_maude_labelmapping_is_not_abstract():
    assert not inspect.isabstract(Maude_LabelMapping)


def test_maude_labelmapping_constructor_exists():
    assert callable(Maude_LabelMapping.__init__)


def test_maude_labelmapping_constructor_args():
    sig = inspect.signature(Maude_LabelMapping.__init__)
    params = list(sig.parameters.keys())
    assert "from_" in params, "Missing parameter 'from_'"
    assert "to" in params, "Missing parameter 'to'"

def test_maude_labelmapping_has_from_():
    assert hasattr(Maude_LabelMapping, "from_")
    descriptor = None
    for klass in Maude_LabelMapping.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_maude_labelmapping_has_to():
    assert hasattr(Maude_LabelMapping, "to")
    descriptor = None
    for klass in Maude_LabelMapping.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_maude_variable_is_not_abstract():
    assert not inspect.isabstract(Maude_Variable)


def test_maude_variable_constructor_exists():
    assert callable(Maude_Variable.__init__)


def test_maude_variable_constructor_args():
    sig = inspect.signature(Maude_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_maude_variable_has_name():
    assert hasattr(Maude_Variable, "name")
    descriptor = None
    for klass in Maude_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_maude_constant_is_not_abstract():
    assert not inspect.isabstract(Maude_Constant)


def test_maude_constant_constructor_exists():
    assert callable(Maude_Constant.__init__)


def test_maude_constant_constructor_args():
    sig = inspect.signature(Maude_Constant.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_maude_constant_has_op():
    assert hasattr(Maude_Constant, "op")
    descriptor = None
    for klass in Maude_Constant.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_equationalcond_is_not_abstract():
    assert not inspect.isabstract(EquationalCond)


def test_equationalcond_constructor_exists():
    assert callable(EquationalCond.__init__)


def test_equationalcond_constructor_args():
    sig = inspect.signature(EquationalCond.__init__)
    params = list(sig.parameters.keys())



def test_maude_matchingcond_is_not_abstract():
    assert not inspect.isabstract(Maude_MatchingCond)


def test_maude_matchingcond_constructor_exists():
    assert callable(Maude_MatchingCond.__init__)


def test_maude_matchingcond_constructor_args():
    sig = inspect.signature(Maude_MatchingCond.__init__)
    params = list(sig.parameters.keys())



def test_maude_equalcond_is_not_abstract():
    assert not inspect.isabstract(Maude_EqualCond)


def test_maude_equalcond_constructor_exists():
    assert callable(Maude_EqualCond.__init__)


def test_maude_equalcond_constructor_args():
    sig = inspect.signature(Maude_EqualCond.__init__)
    params = list(sig.parameters.keys())



def test_maude_booleancond_is_not_abstract():
    assert not inspect.isabstract(Maude_BooleanCond)


def test_maude_booleancond_constructor_exists():
    assert callable(Maude_BooleanCond.__init__)


def test_maude_booleancond_constructor_args():
    sig = inspect.signature(Maude_BooleanCond.__init__)
    params = list(sig.parameters.keys())



def test_maude_membershipcond_is_not_abstract():
    assert not inspect.isabstract(Maude_MembershipCond)


def test_maude_membershipcond_constructor_exists():
    assert callable(Maude_MembershipCond.__init__)


def test_maude_membershipcond_constructor_args():
    sig = inspect.signature(Maude_MembershipCond.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_maude_rewritecond_is_not_abstract():
    assert not inspect.isabstract(Maude_RewriteCond)


def test_maude_rewritecond_constructor_exists():
    assert callable(Maude_RewriteCond.__init__)


def test_maude_rewritecond_constructor_args():
    sig = inspect.signature(Maude_RewriteCond.__init__)
    params = list(sig.parameters.keys())



def test_maude_equationalcond_is_not_abstract():
    assert not inspect.isabstract(Maude_EquationalCond)


def test_maude_equationalcond_constructor_exists():
    assert callable(Maude_EquationalCond.__init__)


def test_maude_equationalcond_constructor_args():
    sig = inspect.signature(Maude_EquationalCond.__init__)
    params = list(sig.parameters.keys())



def test_maude_recterm_is_not_abstract():
    assert not inspect.isabstract(Maude_RecTerm)


def test_maude_recterm_constructor_exists():
    assert callable(Maude_RecTerm.__init__)


def test_maude_recterm_constructor_args():
    sig = inspect.signature(Maude_RecTerm.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_maude_recterm_has_op():
    assert hasattr(Maude_RecTerm, "op")
    descriptor = None
    for klass in Maude_RecTerm.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_maude_term_is_not_abstract():
    assert not inspect.isabstract(Maude_Term)


def test_maude_term_constructor_exists():
    assert callable(Maude_Term.__init__)


def test_maude_term_constructor_args():
    sig = inspect.signature(Maude_Term.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_maude_rule_is_not_abstract():
    assert not inspect.isabstract(Maude_Rule)


def test_maude_rule_constructor_exists():
    assert callable(Maude_Rule.__init__)


def test_maude_rule_constructor_args():
    sig = inspect.signature(Maude_Rule.__init__)
    params = list(sig.parameters.keys())



def test_maude_membership_is_not_abstract():
    assert not inspect.isabstract(Maude_Membership)


def test_maude_membership_constructor_exists():
    assert callable(Maude_Membership.__init__)


def test_maude_membership_constructor_args():
    sig = inspect.signature(Maude_Membership.__init__)
    params = list(sig.parameters.keys())



def test_maude_condition_is_not_abstract():
    assert not inspect.isabstract(Maude_Condition)


def test_maude_condition_constructor_exists():
    assert callable(Maude_Condition.__init__)


def test_maude_condition_constructor_args():
    sig = inspect.signature(Maude_Condition.__init__)
    params = list(sig.parameters.keys())



def test_maude_equation_is_not_abstract():
    assert not inspect.isabstract(Maude_Equation)


def test_maude_equation_constructor_exists():
    assert callable(Maude_Equation.__init__)


def test_maude_equation_constructor_args():
    sig = inspect.signature(Maude_Equation.__init__)
    params = list(sig.parameters.keys())



def test_maude_type_is_not_abstract():
    assert not inspect.isabstract(Maude_Type)


def test_maude_type_constructor_exists():
    assert callable(Maude_Type.__init__)


def test_maude_type_constructor_args():
    sig = inspect.signature(Maude_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_maude_type_has_name():
    assert hasattr(Maude_Type, "name")
    descriptor = None
    for klass in Maude_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_modelement_is_not_abstract():
    assert not inspect.isabstract(ModElement)


def test_modelement_constructor_exists():
    assert callable(ModElement.__init__)


def test_modelement_constructor_args():
    sig = inspect.signature(ModElement.__init__)
    params = list(sig.parameters.keys())



def test_maude_subsortrel_is_not_abstract():
    assert not inspect.isabstract(Maude_SubsortRel)


def test_maude_subsortrel_constructor_exists():
    assert callable(Maude_SubsortRel.__init__)


def test_maude_subsortrel_constructor_args():
    sig = inspect.signature(Maude_SubsortRel.__init__)
    params = list(sig.parameters.keys())



def test_maude_statement_is_not_abstract():
    assert not inspect.isabstract(Maude_Statement)


def test_maude_statement_constructor_exists():
    assert callable(Maude_Statement.__init__)


def test_maude_statement_constructor_args():
    sig = inspect.signature(Maude_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "atts" in params, "Missing parameter 'atts'"
    assert "label" in params, "Missing parameter 'label'"

def test_maude_statement_has_atts():
    assert hasattr(Maude_Statement, "atts")
    descriptor = None
    for klass in Maude_Statement.__mro__:
        if "atts" in klass.__dict__:
            descriptor = klass.__dict__["atts"]
            break
    assert isinstance(descriptor, property)

def test_maude_statement_has_label():
    assert hasattr(Maude_Statement, "label")
    descriptor = None
    for klass in Maude_Statement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_maude_operation_is_not_abstract():
    assert not inspect.isabstract(Maude_Operation)


def test_maude_operation_constructor_exists():
    assert callable(Maude_Operation.__init__)


def test_maude_operation_constructor_args():
    sig = inspect.signature(Maude_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "atts" in params, "Missing parameter 'atts'"

def test_maude_operation_has_name():
    assert hasattr(Maude_Operation, "name")
    descriptor = None
    for klass in Maude_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_maude_operation_has_atts():
    assert hasattr(Maude_Operation, "atts")
    descriptor = None
    for klass in Maude_Operation.__mro__:
        if "atts" in klass.__dict__:
            descriptor = klass.__dict__["atts"]
            break
    assert isinstance(descriptor, property)



def test_maude_modimportation_is_not_abstract():
    assert not inspect.isabstract(Maude_ModImportation)


def test_maude_modimportation_constructor_exists():
    assert callable(Maude_ModImportation.__init__)


def test_maude_modimportation_constructor_args():
    sig = inspect.signature(Maude_ModImportation.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_maude_modimportation_has_mode():
    assert hasattr(Maude_ModImportation, "mode")
    descriptor = None
    for klass in Maude_ModImportation.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_maude_smodule_is_not_abstract():
    assert not inspect.isabstract(Maude_SModule)


def test_maude_smodule_constructor_exists():
    assert callable(Maude_SModule.__init__)


def test_maude_smodule_constructor_args():
    sig = inspect.signature(Maude_SModule.__init__)
    params = list(sig.parameters.keys())



def test_maude_fmodule_is_not_abstract():
    assert not inspect.isabstract(Maude_FModule)


def test_maude_fmodule_constructor_exists():
    assert callable(Maude_FModule.__init__)


def test_maude_fmodule_constructor_args():
    sig = inspect.signature(Maude_FModule.__init__)
    params = list(sig.parameters.keys())



def test_theory_is_not_abstract():
    assert not inspect.isabstract(Theory)


def test_theory_constructor_exists():
    assert callable(Theory.__init__)


def test_theory_constructor_args():
    sig = inspect.signature(Theory.__init__)
    params = list(sig.parameters.keys())



def test_maude_stheory_is_not_abstract():
    assert not inspect.isabstract(Maude_STheory)


def test_maude_stheory_constructor_exists():
    assert callable(Maude_STheory.__init__)


def test_maude_stheory_constructor_args():
    sig = inspect.signature(Maude_STheory.__init__)
    params = list(sig.parameters.keys())



def test_maude_ftheory_is_not_abstract():
    assert not inspect.isabstract(Maude_FTheory)


def test_maude_ftheory_constructor_exists():
    assert callable(Maude_FTheory.__init__)


def test_maude_ftheory_constructor_args():
    sig = inspect.signature(Maude_FTheory.__init__)
    params = list(sig.parameters.keys())



def test_maude_modelement_is_not_abstract():
    assert not inspect.isabstract(Maude_ModElement)


def test_maude_modelement_constructor_exists():
    assert callable(Maude_ModElement.__init__)


def test_maude_modelement_constructor_args():
    sig = inspect.signature(Maude_ModElement.__init__)
    params = list(sig.parameters.keys())



def test_maudetopel_is_not_abstract():
    assert not inspect.isabstract(MaudeTopEl)


def test_maudetopel_constructor_exists():
    assert callable(MaudeTopEl.__init__)


def test_maudetopel_constructor_args():
    sig = inspect.signature(MaudeTopEl.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_maude_kind_is_not_abstract():
    assert not inspect.isabstract(Maude_Kind)


def test_maude_kind_constructor_exists():
    assert callable(Maude_Kind.__init__)


def test_maude_kind_constructor_args():
    sig = inspect.signature(Maude_Kind.__init__)
    params = list(sig.parameters.keys())



def test_maude_sort_is_not_abstract():
    assert not inspect.isabstract(Maude_Sort)


def test_maude_sort_constructor_exists():
    assert callable(Maude_Sort.__init__)


def test_maude_sort_constructor_args():
    sig = inspect.signature(Maude_Sort.__init__)
    params = list(sig.parameters.keys())



def test_maude_theory_is_not_abstract():
    assert not inspect.isabstract(Maude_Theory)


def test_maude_theory_constructor_exists():
    assert callable(Maude_Theory.__init__)


def test_maude_theory_constructor_args():
    sig = inspect.signature(Maude_Theory.__init__)
    params = list(sig.parameters.keys())



def test_maude_module_is_not_abstract():
    assert not inspect.isabstract(Maude_Module)


def test_maude_module_constructor_exists():
    assert callable(Maude_Module.__init__)


def test_maude_module_constructor_args():
    sig = inspect.signature(Maude_Module.__init__)
    params = list(sig.parameters.keys())



def test_maude_renmapping_is_not_abstract():
    assert not inspect.isabstract(Maude_RenMapping)


def test_maude_renmapping_constructor_exists():
    assert callable(Maude_RenMapping.__init__)


def test_maude_renmapping_constructor_args():
    sig = inspect.signature(Maude_RenMapping.__init__)
    params = list(sig.parameters.keys())



def test_maude_view_is_not_abstract():
    assert not inspect.isabstract(Maude_View)


def test_maude_view_constructor_exists():
    assert callable(Maude_View.__init__)


def test_maude_view_constructor_args():
    sig = inspect.signature(Maude_View.__init__)
    params = list(sig.parameters.keys())



def test_modexpression_is_not_abstract():
    assert not inspect.isabstract(ModExpression)


def test_modexpression_constructor_exists():
    assert callable(ModExpression.__init__)


def test_modexpression_constructor_args():
    sig = inspect.signature(ModExpression.__init__)
    params = list(sig.parameters.keys())



def test_maude_theoryidmodexp_is_not_abstract():
    assert not inspect.isabstract(Maude_TheoryIdModExp)


def test_maude_theoryidmodexp_constructor_exists():
    assert callable(Maude_TheoryIdModExp.__init__)


def test_maude_theoryidmodexp_constructor_args():
    sig = inspect.signature(Maude_TheoryIdModExp.__init__)
    params = list(sig.parameters.keys())



def test_maude_renmodexp_is_not_abstract():
    assert not inspect.isabstract(Maude_RenModExp)


def test_maude_renmodexp_constructor_exists():
    assert callable(Maude_RenModExp.__init__)


def test_maude_renmodexp_constructor_args():
    sig = inspect.signature(Maude_RenModExp.__init__)
    params = list(sig.parameters.keys())



def test_maude_compmodexp_is_not_abstract():
    assert not inspect.isabstract(Maude_CompModExp)


def test_maude_compmodexp_constructor_exists():
    assert callable(Maude_CompModExp.__init__)


def test_maude_compmodexp_constructor_args():
    sig = inspect.signature(Maude_CompModExp.__init__)
    params = list(sig.parameters.keys())



def test_maude_moduleidmodexp_is_not_abstract():
    assert not inspect.isabstract(Maude_ModuleIdModExp)


def test_maude_moduleidmodexp_constructor_exists():
    assert callable(Maude_ModuleIdModExp.__init__)


def test_maude_moduleidmodexp_constructor_args():
    sig = inspect.signature(Maude_ModuleIdModExp.__init__)
    params = list(sig.parameters.keys())



def test_maude_instmodexp_is_not_abstract():
    assert not inspect.isabstract(Maude_InstModExp)


def test_maude_instmodexp_constructor_exists():
    assert callable(Maude_InstModExp.__init__)


def test_maude_instmodexp_constructor_args():
    sig = inspect.signature(Maude_InstModExp.__init__)
    params = list(sig.parameters.keys())



def test_maude_modexpression_is_not_abstract():
    assert not inspect.isabstract(Maude_ModExpression)


def test_maude_modexpression_constructor_exists():
    assert callable(Maude_ModExpression.__init__)


def test_maude_modexpression_constructor_args():
    sig = inspect.signature(Maude_ModExpression.__init__)
    params = list(sig.parameters.keys())



def test_maude_maudetopel_is_not_abstract():
    assert not inspect.isabstract(Maude_MaudeTopEl)


def test_maude_maudetopel_constructor_exists():
    assert callable(Maude_MaudeTopEl.__init__)


def test_maude_maudetopel_constructor_args():
    sig = inspect.signature(Maude_MaudeTopEl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_maude_maudetopel_has_name():
    assert hasattr(Maude_MaudeTopEl, "name")
    descriptor = None
    for klass in Maude_MaudeTopEl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_maude_maudespec_is_not_abstract():
    assert not inspect.isabstract(Maude_MaudeSpec)


def test_maude_maudespec_constructor_exists():
    assert callable(Maude_MaudeSpec.__init__)


def test_maude_maudespec_constructor_args():
    sig = inspect.signature(Maude_MaudeSpec.__init__)
    params = list(sig.parameters.keys())



def test_maude_parameter_is_not_abstract():
    assert not inspect.isabstract(Maude_Parameter)


def test_maude_parameter_constructor_exists():
    assert callable(Maude_Parameter.__init__)


def test_maude_parameter_constructor_args():
    sig = inspect.signature(Maude_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_maude_parameter_has_label():
    assert hasattr(Maude_Parameter, "label")
    descriptor = None
    for klass in Maude_Parameter.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_importationmode_exists():
    # Check that the Enumeration exists
    assert ImportationMode is not None

def test_importationmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImportationMode]
    expected_literals = [
        "extending",
        "including",
        "protecting",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImportationMode"


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
RenMapping_strategy = st.builds(
    RenMapping,
)
Maude_OpTypedMapping_strategy = st.builds(
    Maude_OpTypedMapping,
    to=
        safe_text,
    atts=
        safe_text
)
Maude_OpMapping_strategy = st.builds(
    Maude_OpMapping,
    to=
        safe_text
)
Maude_SortMapping_strategy = st.builds(
    Maude_SortMapping,
    to=
        safe_text
)
ViewMapping_strategy = st.builds(
    ViewMapping,
)
Maude_TermMapping_strategy = st.builds(
    Maude_TermMapping,
)
Maude_ViewMapping_strategy = st.builds(
    Maude_ViewMapping,
)
Maude_LabelMapping_strategy = st.builds(
    Maude_LabelMapping,
    from_=
        safe_text,
    to=
        safe_text
)
Term_strategy = st.builds(
    Term,
)
Maude_Variable_strategy = st.builds(
    Maude_Variable,
    name=
        safe_text
)
Maude_Constant_strategy = st.builds(
    Maude_Constant,
    op=
        safe_text
)
EquationalCond_strategy = st.builds(
    EquationalCond,
)
Maude_MatchingCond_strategy = st.builds(
    Maude_MatchingCond,
)
Maude_EqualCond_strategy = st.builds(
    Maude_EqualCond,
)
Maude_BooleanCond_strategy = st.builds(
    Maude_BooleanCond,
)
Maude_MembershipCond_strategy = st.builds(
    Maude_MembershipCond,
)
Condition_strategy = st.builds(
    Condition,
)
Maude_RewriteCond_strategy = st.builds(
    Maude_RewriteCond,
)
Maude_EquationalCond_strategy = st.builds(
    Maude_EquationalCond,
)
Maude_RecTerm_strategy = st.builds(
    Maude_RecTerm,
    op=
        safe_text
)
Maude_Term_strategy = st.builds(
    Maude_Term,
)
Statement_strategy = st.builds(
    Statement,
)
Maude_Rule_strategy = st.builds(
    Maude_Rule,
)
Maude_Membership_strategy = st.builds(
    Maude_Membership,
)
Maude_Condition_strategy = st.builds(
    Maude_Condition,
)
Maude_Equation_strategy = st.builds(
    Maude_Equation,
)
Maude_Type_strategy = st.builds(
    Maude_Type,
    name=
        safe_text
)
ModElement_strategy = st.builds(
    ModElement,
)
Maude_SubsortRel_strategy = st.builds(
    Maude_SubsortRel,
)
Maude_Statement_strategy = st.builds(
    Maude_Statement,
    atts=
        safe_text,
    label=
        safe_text
)
Maude_Operation_strategy = st.builds(
    Maude_Operation,
    name=
        safe_text,
    atts=
        safe_text
)
Maude_ModImportation_strategy = st.builds(
    Maude_ModImportation,
    mode=
        safe_text
)
Module_strategy = st.builds(
    Module,
)
Maude_SModule_strategy = st.builds(
    Maude_SModule,
)
Maude_FModule_strategy = st.builds(
    Maude_FModule,
)
Theory_strategy = st.builds(
    Theory,
)
Maude_STheory_strategy = st.builds(
    Maude_STheory,
)
Maude_FTheory_strategy = st.builds(
    Maude_FTheory,
)
Maude_ModElement_strategy = st.builds(
    Maude_ModElement,
)
MaudeTopEl_strategy = st.builds(
    MaudeTopEl,
)
Type_strategy = st.builds(
    Type,
)
Maude_Kind_strategy = st.builds(
    Maude_Kind,
)
Maude_Sort_strategy = st.builds(
    Maude_Sort,
)
Maude_Theory_strategy = st.builds(
    Maude_Theory,
)
Maude_Module_strategy = st.builds(
    Maude_Module,
)
Maude_RenMapping_strategy = st.builds(
    Maude_RenMapping,
)
Maude_View_strategy = st.builds(
    Maude_View,
)
ModExpression_strategy = st.builds(
    ModExpression,
)
Maude_TheoryIdModExp_strategy = st.builds(
    Maude_TheoryIdModExp,
)
Maude_RenModExp_strategy = st.builds(
    Maude_RenModExp,
)
Maude_CompModExp_strategy = st.builds(
    Maude_CompModExp,
)
Maude_ModuleIdModExp_strategy = st.builds(
    Maude_ModuleIdModExp,
)
Maude_InstModExp_strategy = st.builds(
    Maude_InstModExp,
)
Maude_ModExpression_strategy = st.builds(
    Maude_ModExpression,
)
Maude_MaudeTopEl_strategy = st.builds(
    Maude_MaudeTopEl,
    name=
        safe_text
)
Maude_MaudeSpec_strategy = st.builds(
    Maude_MaudeSpec,
)
Maude_Parameter_strategy = st.builds(
    Maude_Parameter,
    label=
        safe_text
)

@given(instance=RenMapping_strategy)
@settings(max_examples=50)
def test_renmapping_instantiation(instance):
    assert isinstance(instance, RenMapping)

@given(instance=Maude_OpTypedMapping_strategy)
@settings(max_examples=50)
def test_maude_optypedmapping_instantiation(instance):
    assert isinstance(instance, Maude_OpTypedMapping)



@given(instance=Maude_OpTypedMapping_strategy)
def test_maude_optypedmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=Maude_OpTypedMapping_strategy)
def test_maude_optypedmapping_atts_setter(instance):
    original = instance.atts
    instance.atts = original
    assert instance.atts == original

@given(instance=Maude_OpMapping_strategy)
@settings(max_examples=50)
def test_maude_opmapping_instantiation(instance):
    assert isinstance(instance, Maude_OpMapping)



@given(instance=Maude_OpMapping_strategy)
def test_maude_opmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=Maude_SortMapping_strategy)
@settings(max_examples=50)
def test_maude_sortmapping_instantiation(instance):
    assert isinstance(instance, Maude_SortMapping)



@given(instance=Maude_SortMapping_strategy)
def test_maude_sortmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=ViewMapping_strategy)
@settings(max_examples=50)
def test_viewmapping_instantiation(instance):
    assert isinstance(instance, ViewMapping)

@given(instance=Maude_TermMapping_strategy)
@settings(max_examples=50)
def test_maude_termmapping_instantiation(instance):
    assert isinstance(instance, Maude_TermMapping)

@given(instance=Maude_ViewMapping_strategy)
@settings(max_examples=50)
def test_maude_viewmapping_instantiation(instance):
    assert isinstance(instance, Maude_ViewMapping)

@given(instance=Maude_LabelMapping_strategy)
@settings(max_examples=50)
def test_maude_labelmapping_instantiation(instance):
    assert isinstance(instance, Maude_LabelMapping)



@given(instance=Maude_LabelMapping_strategy)
def test_maude_labelmapping_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original



@given(instance=Maude_LabelMapping_strategy)
def test_maude_labelmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=Maude_Variable_strategy)
@settings(max_examples=50)
def test_maude_variable_instantiation(instance):
    assert isinstance(instance, Maude_Variable)



@given(instance=Maude_Variable_strategy)
def test_maude_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Maude_Constant_strategy)
@settings(max_examples=50)
def test_maude_constant_instantiation(instance):
    assert isinstance(instance, Maude_Constant)



@given(instance=Maude_Constant_strategy)
def test_maude_constant_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=EquationalCond_strategy)
@settings(max_examples=50)
def test_equationalcond_instantiation(instance):
    assert isinstance(instance, EquationalCond)

@given(instance=Maude_MatchingCond_strategy)
@settings(max_examples=50)
def test_maude_matchingcond_instantiation(instance):
    assert isinstance(instance, Maude_MatchingCond)

@given(instance=Maude_EqualCond_strategy)
@settings(max_examples=50)
def test_maude_equalcond_instantiation(instance):
    assert isinstance(instance, Maude_EqualCond)

@given(instance=Maude_BooleanCond_strategy)
@settings(max_examples=50)
def test_maude_booleancond_instantiation(instance):
    assert isinstance(instance, Maude_BooleanCond)

@given(instance=Maude_MembershipCond_strategy)
@settings(max_examples=50)
def test_maude_membershipcond_instantiation(instance):
    assert isinstance(instance, Maude_MembershipCond)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=Maude_RewriteCond_strategy)
@settings(max_examples=50)
def test_maude_rewritecond_instantiation(instance):
    assert isinstance(instance, Maude_RewriteCond)

@given(instance=Maude_EquationalCond_strategy)
@settings(max_examples=50)
def test_maude_equationalcond_instantiation(instance):
    assert isinstance(instance, Maude_EquationalCond)

@given(instance=Maude_RecTerm_strategy)
@settings(max_examples=50)
def test_maude_recterm_instantiation(instance):
    assert isinstance(instance, Maude_RecTerm)



@given(instance=Maude_RecTerm_strategy)
def test_maude_recterm_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=Maude_Term_strategy)
@settings(max_examples=50)
def test_maude_term_instantiation(instance):
    assert isinstance(instance, Maude_Term)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=Maude_Rule_strategy)
@settings(max_examples=50)
def test_maude_rule_instantiation(instance):
    assert isinstance(instance, Maude_Rule)

@given(instance=Maude_Membership_strategy)
@settings(max_examples=50)
def test_maude_membership_instantiation(instance):
    assert isinstance(instance, Maude_Membership)

@given(instance=Maude_Condition_strategy)
@settings(max_examples=50)
def test_maude_condition_instantiation(instance):
    assert isinstance(instance, Maude_Condition)

@given(instance=Maude_Equation_strategy)
@settings(max_examples=50)
def test_maude_equation_instantiation(instance):
    assert isinstance(instance, Maude_Equation)

@given(instance=Maude_Type_strategy)
@settings(max_examples=50)
def test_maude_type_instantiation(instance):
    assert isinstance(instance, Maude_Type)



@given(instance=Maude_Type_strategy)
def test_maude_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ModElement_strategy)
@settings(max_examples=50)
def test_modelement_instantiation(instance):
    assert isinstance(instance, ModElement)

@given(instance=Maude_SubsortRel_strategy)
@settings(max_examples=50)
def test_maude_subsortrel_instantiation(instance):
    assert isinstance(instance, Maude_SubsortRel)

@given(instance=Maude_Statement_strategy)
@settings(max_examples=50)
def test_maude_statement_instantiation(instance):
    assert isinstance(instance, Maude_Statement)



@given(instance=Maude_Statement_strategy)
def test_maude_statement_atts_setter(instance):
    original = instance.atts
    instance.atts = original
    assert instance.atts == original



@given(instance=Maude_Statement_strategy)
def test_maude_statement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Maude_Operation_strategy)
@settings(max_examples=50)
def test_maude_operation_instantiation(instance):
    assert isinstance(instance, Maude_Operation)



@given(instance=Maude_Operation_strategy)
def test_maude_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Maude_Operation_strategy)
def test_maude_operation_atts_setter(instance):
    original = instance.atts
    instance.atts = original
    assert instance.atts == original

@given(instance=Maude_ModImportation_strategy)
@settings(max_examples=50)
def test_maude_modimportation_instantiation(instance):
    assert isinstance(instance, Maude_ModImportation)



@given(instance=Maude_ModImportation_strategy)
def test_maude_modimportation_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=Maude_SModule_strategy)
@settings(max_examples=50)
def test_maude_smodule_instantiation(instance):
    assert isinstance(instance, Maude_SModule)

@given(instance=Maude_FModule_strategy)
@settings(max_examples=50)
def test_maude_fmodule_instantiation(instance):
    assert isinstance(instance, Maude_FModule)

@given(instance=Theory_strategy)
@settings(max_examples=50)
def test_theory_instantiation(instance):
    assert isinstance(instance, Theory)

@given(instance=Maude_STheory_strategy)
@settings(max_examples=50)
def test_maude_stheory_instantiation(instance):
    assert isinstance(instance, Maude_STheory)

@given(instance=Maude_FTheory_strategy)
@settings(max_examples=50)
def test_maude_ftheory_instantiation(instance):
    assert isinstance(instance, Maude_FTheory)

@given(instance=Maude_ModElement_strategy)
@settings(max_examples=50)
def test_maude_modelement_instantiation(instance):
    assert isinstance(instance, Maude_ModElement)

@given(instance=MaudeTopEl_strategy)
@settings(max_examples=50)
def test_maudetopel_instantiation(instance):
    assert isinstance(instance, MaudeTopEl)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=Maude_Kind_strategy)
@settings(max_examples=50)
def test_maude_kind_instantiation(instance):
    assert isinstance(instance, Maude_Kind)

@given(instance=Maude_Sort_strategy)
@settings(max_examples=50)
def test_maude_sort_instantiation(instance):
    assert isinstance(instance, Maude_Sort)

@given(instance=Maude_Theory_strategy)
@settings(max_examples=50)
def test_maude_theory_instantiation(instance):
    assert isinstance(instance, Maude_Theory)

@given(instance=Maude_Module_strategy)
@settings(max_examples=50)
def test_maude_module_instantiation(instance):
    assert isinstance(instance, Maude_Module)

@given(instance=Maude_RenMapping_strategy)
@settings(max_examples=50)
def test_maude_renmapping_instantiation(instance):
    assert isinstance(instance, Maude_RenMapping)

@given(instance=Maude_View_strategy)
@settings(max_examples=50)
def test_maude_view_instantiation(instance):
    assert isinstance(instance, Maude_View)

@given(instance=ModExpression_strategy)
@settings(max_examples=50)
def test_modexpression_instantiation(instance):
    assert isinstance(instance, ModExpression)

@given(instance=Maude_TheoryIdModExp_strategy)
@settings(max_examples=50)
def test_maude_theoryidmodexp_instantiation(instance):
    assert isinstance(instance, Maude_TheoryIdModExp)

@given(instance=Maude_RenModExp_strategy)
@settings(max_examples=50)
def test_maude_renmodexp_instantiation(instance):
    assert isinstance(instance, Maude_RenModExp)

@given(instance=Maude_CompModExp_strategy)
@settings(max_examples=50)
def test_maude_compmodexp_instantiation(instance):
    assert isinstance(instance, Maude_CompModExp)

@given(instance=Maude_ModuleIdModExp_strategy)
@settings(max_examples=50)
def test_maude_moduleidmodexp_instantiation(instance):
    assert isinstance(instance, Maude_ModuleIdModExp)

@given(instance=Maude_InstModExp_strategy)
@settings(max_examples=50)
def test_maude_instmodexp_instantiation(instance):
    assert isinstance(instance, Maude_InstModExp)

@given(instance=Maude_ModExpression_strategy)
@settings(max_examples=50)
def test_maude_modexpression_instantiation(instance):
    assert isinstance(instance, Maude_ModExpression)

@given(instance=Maude_MaudeTopEl_strategy)
@settings(max_examples=50)
def test_maude_maudetopel_instantiation(instance):
    assert isinstance(instance, Maude_MaudeTopEl)



@given(instance=Maude_MaudeTopEl_strategy)
def test_maude_maudetopel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Maude_MaudeSpec_strategy)
@settings(max_examples=50)
def test_maude_maudespec_instantiation(instance):
    assert isinstance(instance, Maude_MaudeSpec)

@given(instance=Maude_Parameter_strategy)
@settings(max_examples=50)
def test_maude_parameter_instantiation(instance):
    assert isinstance(instance, Maude_Parameter)



@given(instance=Maude_Parameter_strategy)
def test_maude_parameter_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original
