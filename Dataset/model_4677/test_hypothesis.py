import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ModExpression,
    Maude::RenModExp,
    Maude::InstModExp,
    Maude::ModExpression,
    Maude::MaudeTopEl,
    Maude::MaudeSpec,
    Maude::Parameter,
    Maude::TheoryIdModExp,
    Maude::ModuleIdModExp,
    Maude::CompModExp,
    RenMapping,
    Maude::SortMapping,
    ViewMapping,
    Maude::RenMapping,
    Maude::TermMapping,
    Maude::ViewMapping,
    Maude::LabelMapping,
    Maude::OpMapping,
    Maude::OpTypedMapping,
    EquationalCond,
    Maude::BooleanCond,
    Maude::MembershipCond,
    Condition,
    Maude::RewriteCond,
    Maude::EquationalCond,
    Term,
    Maude::RecTerm,
    Maude::Variable,
    Maude::Constant,
    Maude::EqualCond,
    Maude::MatchingCond,
    Maude::Term,
    Statement,
    Maude::Equation,
    Maude::Rule,
    Maude::Membership,
    Maude::Condition,
    ModElement,
    Maude::Statement,
    Maude::Operation,
    Maude::ModImportation,
    Module,
    Maude::SModule,
    Maude::FModule,
    Theory,
    Maude::STheory,
    Maude::FTheory,
    Maude::ModElement,
    MaudeTopEl,
    Maude::Theory,
    Maude::View,
    Maude::Module,
    Maude::SubsortRel,
    Type,
    Maude::Kind,
    Maude::Sort,
    Maude::Type,
    ImportationMode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_modexpression_is_not_abstract():
    assert not inspect.isabstract(ModExpression)


def test_modexpression_constructor_exists():
    assert callable(ModExpression.__init__)


def test_modexpression_constructor_args():
    sig = inspect.signature(ModExpression.__init__)
    params = list(sig.parameters.keys())



def test_maude::renmodexp_is_not_abstract():
    assert not inspect.isabstract(Maude::RenModExp)


def test_maude::renmodexp_constructor_exists():
    assert callable(Maude::RenModExp.__init__)


def test_maude::renmodexp_constructor_args():
    sig = inspect.signature(Maude::RenModExp.__init__)
    params = list(sig.parameters.keys())



def test_maude::instmodexp_is_not_abstract():
    assert not inspect.isabstract(Maude::InstModExp)


def test_maude::instmodexp_constructor_exists():
    assert callable(Maude::InstModExp.__init__)


def test_maude::instmodexp_constructor_args():
    sig = inspect.signature(Maude::InstModExp.__init__)
    params = list(sig.parameters.keys())



def test_maude::modexpression_is_not_abstract():
    assert not inspect.isabstract(Maude::ModExpression)


def test_maude::modexpression_constructor_exists():
    assert callable(Maude::ModExpression.__init__)


def test_maude::modexpression_constructor_args():
    sig = inspect.signature(Maude::ModExpression.__init__)
    params = list(sig.parameters.keys())



def test_maude::maudetopel_is_not_abstract():
    assert not inspect.isabstract(Maude::MaudeTopEl)


def test_maude::maudetopel_constructor_exists():
    assert callable(Maude::MaudeTopEl.__init__)


def test_maude::maudetopel_constructor_args():
    sig = inspect.signature(Maude::MaudeTopEl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_maude::maudetopel_has_name():
    assert hasattr(Maude::MaudeTopEl, "name")
    descriptor = None
    for klass in Maude::MaudeTopEl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_maude::maudespec_is_not_abstract():
    assert not inspect.isabstract(Maude::MaudeSpec)


def test_maude::maudespec_constructor_exists():
    assert callable(Maude::MaudeSpec.__init__)


def test_maude::maudespec_constructor_args():
    sig = inspect.signature(Maude::MaudeSpec.__init__)
    params = list(sig.parameters.keys())



def test_maude::parameter_is_not_abstract():
    assert not inspect.isabstract(Maude::Parameter)


def test_maude::parameter_constructor_exists():
    assert callable(Maude::Parameter.__init__)


def test_maude::parameter_constructor_args():
    sig = inspect.signature(Maude::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_maude::parameter_has_label():
    assert hasattr(Maude::Parameter, "label")
    descriptor = None
    for klass in Maude::Parameter.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_maude::theoryidmodexp_is_not_abstract():
    assert not inspect.isabstract(Maude::TheoryIdModExp)


def test_maude::theoryidmodexp_constructor_exists():
    assert callable(Maude::TheoryIdModExp.__init__)


def test_maude::theoryidmodexp_constructor_args():
    sig = inspect.signature(Maude::TheoryIdModExp.__init__)
    params = list(sig.parameters.keys())



def test_maude::moduleidmodexp_is_not_abstract():
    assert not inspect.isabstract(Maude::ModuleIdModExp)


def test_maude::moduleidmodexp_constructor_exists():
    assert callable(Maude::ModuleIdModExp.__init__)


def test_maude::moduleidmodexp_constructor_args():
    sig = inspect.signature(Maude::ModuleIdModExp.__init__)
    params = list(sig.parameters.keys())



def test_maude::compmodexp_is_not_abstract():
    assert not inspect.isabstract(Maude::CompModExp)


def test_maude::compmodexp_constructor_exists():
    assert callable(Maude::CompModExp.__init__)


def test_maude::compmodexp_constructor_args():
    sig = inspect.signature(Maude::CompModExp.__init__)
    params = list(sig.parameters.keys())



def test_renmapping_is_not_abstract():
    assert not inspect.isabstract(RenMapping)


def test_renmapping_constructor_exists():
    assert callable(RenMapping.__init__)


def test_renmapping_constructor_args():
    sig = inspect.signature(RenMapping.__init__)
    params = list(sig.parameters.keys())



def test_maude::sortmapping_is_not_abstract():
    assert not inspect.isabstract(Maude::SortMapping)


def test_maude::sortmapping_constructor_exists():
    assert callable(Maude::SortMapping.__init__)


def test_maude::sortmapping_constructor_args():
    sig = inspect.signature(Maude::SortMapping.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"

def test_maude::sortmapping_has_to():
    assert hasattr(Maude::SortMapping, "to")
    descriptor = None
    for klass in Maude::SortMapping.__mro__:
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



def test_maude::renmapping_is_not_abstract():
    assert not inspect.isabstract(Maude::RenMapping)


def test_maude::renmapping_constructor_exists():
    assert callable(Maude::RenMapping.__init__)


def test_maude::renmapping_constructor_args():
    sig = inspect.signature(Maude::RenMapping.__init__)
    params = list(sig.parameters.keys())



def test_maude::termmapping_is_not_abstract():
    assert not inspect.isabstract(Maude::TermMapping)


def test_maude::termmapping_constructor_exists():
    assert callable(Maude::TermMapping.__init__)


def test_maude::termmapping_constructor_args():
    sig = inspect.signature(Maude::TermMapping.__init__)
    params = list(sig.parameters.keys())



def test_maude::viewmapping_is_not_abstract():
    assert not inspect.isabstract(Maude::ViewMapping)


def test_maude::viewmapping_constructor_exists():
    assert callable(Maude::ViewMapping.__init__)


def test_maude::viewmapping_constructor_args():
    sig = inspect.signature(Maude::ViewMapping.__init__)
    params = list(sig.parameters.keys())



def test_maude::labelmapping_is_not_abstract():
    assert not inspect.isabstract(Maude::LabelMapping)


def test_maude::labelmapping_constructor_exists():
    assert callable(Maude::LabelMapping.__init__)


def test_maude::labelmapping_constructor_args():
    sig = inspect.signature(Maude::LabelMapping.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"
    assert "from_" in params, "Missing parameter 'from_'"

def test_maude::labelmapping_has_to():
    assert hasattr(Maude::LabelMapping, "to")
    descriptor = None
    for klass in Maude::LabelMapping.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_maude::labelmapping_has_from_():
    assert hasattr(Maude::LabelMapping, "from_")
    descriptor = None
    for klass in Maude::LabelMapping.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)



def test_maude::opmapping_is_not_abstract():
    assert not inspect.isabstract(Maude::OpMapping)


def test_maude::opmapping_constructor_exists():
    assert callable(Maude::OpMapping.__init__)


def test_maude::opmapping_constructor_args():
    sig = inspect.signature(Maude::OpMapping.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"

def test_maude::opmapping_has_to():
    assert hasattr(Maude::OpMapping, "to")
    descriptor = None
    for klass in Maude::OpMapping.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_maude::optypedmapping_is_not_abstract():
    assert not inspect.isabstract(Maude::OpTypedMapping)


def test_maude::optypedmapping_constructor_exists():
    assert callable(Maude::OpTypedMapping.__init__)


def test_maude::optypedmapping_constructor_args():
    sig = inspect.signature(Maude::OpTypedMapping.__init__)
    params = list(sig.parameters.keys())
    assert "atts" in params, "Missing parameter 'atts'"
    assert "to" in params, "Missing parameter 'to'"

def test_maude::optypedmapping_has_atts():
    assert hasattr(Maude::OpTypedMapping, "atts")
    descriptor = None
    for klass in Maude::OpTypedMapping.__mro__:
        if "atts" in klass.__dict__:
            descriptor = klass.__dict__["atts"]
            break
    assert isinstance(descriptor, property)

def test_maude::optypedmapping_has_to():
    assert hasattr(Maude::OpTypedMapping, "to")
    descriptor = None
    for klass in Maude::OpTypedMapping.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_equationalcond_is_not_abstract():
    assert not inspect.isabstract(EquationalCond)


def test_equationalcond_constructor_exists():
    assert callable(EquationalCond.__init__)


def test_equationalcond_constructor_args():
    sig = inspect.signature(EquationalCond.__init__)
    params = list(sig.parameters.keys())



def test_maude::booleancond_is_not_abstract():
    assert not inspect.isabstract(Maude::BooleanCond)


def test_maude::booleancond_constructor_exists():
    assert callable(Maude::BooleanCond.__init__)


def test_maude::booleancond_constructor_args():
    sig = inspect.signature(Maude::BooleanCond.__init__)
    params = list(sig.parameters.keys())



def test_maude::membershipcond_is_not_abstract():
    assert not inspect.isabstract(Maude::MembershipCond)


def test_maude::membershipcond_constructor_exists():
    assert callable(Maude::MembershipCond.__init__)


def test_maude::membershipcond_constructor_args():
    sig = inspect.signature(Maude::MembershipCond.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_maude::rewritecond_is_not_abstract():
    assert not inspect.isabstract(Maude::RewriteCond)


def test_maude::rewritecond_constructor_exists():
    assert callable(Maude::RewriteCond.__init__)


def test_maude::rewritecond_constructor_args():
    sig = inspect.signature(Maude::RewriteCond.__init__)
    params = list(sig.parameters.keys())



def test_maude::equationalcond_is_not_abstract():
    assert not inspect.isabstract(Maude::EquationalCond)


def test_maude::equationalcond_constructor_exists():
    assert callable(Maude::EquationalCond.__init__)


def test_maude::equationalcond_constructor_args():
    sig = inspect.signature(Maude::EquationalCond.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_maude::recterm_is_not_abstract():
    assert not inspect.isabstract(Maude::RecTerm)


def test_maude::recterm_constructor_exists():
    assert callable(Maude::RecTerm.__init__)


def test_maude::recterm_constructor_args():
    sig = inspect.signature(Maude::RecTerm.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_maude::recterm_has_op():
    assert hasattr(Maude::RecTerm, "op")
    descriptor = None
    for klass in Maude::RecTerm.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_maude::variable_is_not_abstract():
    assert not inspect.isabstract(Maude::Variable)


def test_maude::variable_constructor_exists():
    assert callable(Maude::Variable.__init__)


def test_maude::variable_constructor_args():
    sig = inspect.signature(Maude::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_maude::variable_has_name():
    assert hasattr(Maude::Variable, "name")
    descriptor = None
    for klass in Maude::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_maude::constant_is_not_abstract():
    assert not inspect.isabstract(Maude::Constant)


def test_maude::constant_constructor_exists():
    assert callable(Maude::Constant.__init__)


def test_maude::constant_constructor_args():
    sig = inspect.signature(Maude::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_maude::constant_has_op():
    assert hasattr(Maude::Constant, "op")
    descriptor = None
    for klass in Maude::Constant.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_maude::equalcond_is_not_abstract():
    assert not inspect.isabstract(Maude::EqualCond)


def test_maude::equalcond_constructor_exists():
    assert callable(Maude::EqualCond.__init__)


def test_maude::equalcond_constructor_args():
    sig = inspect.signature(Maude::EqualCond.__init__)
    params = list(sig.parameters.keys())



def test_maude::matchingcond_is_not_abstract():
    assert not inspect.isabstract(Maude::MatchingCond)


def test_maude::matchingcond_constructor_exists():
    assert callable(Maude::MatchingCond.__init__)


def test_maude::matchingcond_constructor_args():
    sig = inspect.signature(Maude::MatchingCond.__init__)
    params = list(sig.parameters.keys())



def test_maude::term_is_not_abstract():
    assert not inspect.isabstract(Maude::Term)


def test_maude::term_constructor_exists():
    assert callable(Maude::Term.__init__)


def test_maude::term_constructor_args():
    sig = inspect.signature(Maude::Term.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_maude::equation_is_not_abstract():
    assert not inspect.isabstract(Maude::Equation)


def test_maude::equation_constructor_exists():
    assert callable(Maude::Equation.__init__)


def test_maude::equation_constructor_args():
    sig = inspect.signature(Maude::Equation.__init__)
    params = list(sig.parameters.keys())



def test_maude::rule_is_not_abstract():
    assert not inspect.isabstract(Maude::Rule)


def test_maude::rule_constructor_exists():
    assert callable(Maude::Rule.__init__)


def test_maude::rule_constructor_args():
    sig = inspect.signature(Maude::Rule.__init__)
    params = list(sig.parameters.keys())



def test_maude::membership_is_not_abstract():
    assert not inspect.isabstract(Maude::Membership)


def test_maude::membership_constructor_exists():
    assert callable(Maude::Membership.__init__)


def test_maude::membership_constructor_args():
    sig = inspect.signature(Maude::Membership.__init__)
    params = list(sig.parameters.keys())



def test_maude::condition_is_not_abstract():
    assert not inspect.isabstract(Maude::Condition)


def test_maude::condition_constructor_exists():
    assert callable(Maude::Condition.__init__)


def test_maude::condition_constructor_args():
    sig = inspect.signature(Maude::Condition.__init__)
    params = list(sig.parameters.keys())



def test_modelement_is_not_abstract():
    assert not inspect.isabstract(ModElement)


def test_modelement_constructor_exists():
    assert callable(ModElement.__init__)


def test_modelement_constructor_args():
    sig = inspect.signature(ModElement.__init__)
    params = list(sig.parameters.keys())



def test_maude::statement_is_not_abstract():
    assert not inspect.isabstract(Maude::Statement)


def test_maude::statement_constructor_exists():
    assert callable(Maude::Statement.__init__)


def test_maude::statement_constructor_args():
    sig = inspect.signature(Maude::Statement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "atts" in params, "Missing parameter 'atts'"

def test_maude::statement_has_label():
    assert hasattr(Maude::Statement, "label")
    descriptor = None
    for klass in Maude::Statement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_maude::statement_has_atts():
    assert hasattr(Maude::Statement, "atts")
    descriptor = None
    for klass in Maude::Statement.__mro__:
        if "atts" in klass.__dict__:
            descriptor = klass.__dict__["atts"]
            break
    assert isinstance(descriptor, property)



def test_maude::operation_is_not_abstract():
    assert not inspect.isabstract(Maude::Operation)


def test_maude::operation_constructor_exists():
    assert callable(Maude::Operation.__init__)


def test_maude::operation_constructor_args():
    sig = inspect.signature(Maude::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "atts" in params, "Missing parameter 'atts'"
    assert "name" in params, "Missing parameter 'name'"

def test_maude::operation_has_atts():
    assert hasattr(Maude::Operation, "atts")
    descriptor = None
    for klass in Maude::Operation.__mro__:
        if "atts" in klass.__dict__:
            descriptor = klass.__dict__["atts"]
            break
    assert isinstance(descriptor, property)

def test_maude::operation_has_name():
    assert hasattr(Maude::Operation, "name")
    descriptor = None
    for klass in Maude::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_maude::modimportation_is_not_abstract():
    assert not inspect.isabstract(Maude::ModImportation)


def test_maude::modimportation_constructor_exists():
    assert callable(Maude::ModImportation.__init__)


def test_maude::modimportation_constructor_args():
    sig = inspect.signature(Maude::ModImportation.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_maude::modimportation_has_mode():
    assert hasattr(Maude::ModImportation, "mode")
    descriptor = None
    for klass in Maude::ModImportation.__mro__:
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



def test_maude::smodule_is_not_abstract():
    assert not inspect.isabstract(Maude::SModule)


def test_maude::smodule_constructor_exists():
    assert callable(Maude::SModule.__init__)


def test_maude::smodule_constructor_args():
    sig = inspect.signature(Maude::SModule.__init__)
    params = list(sig.parameters.keys())



def test_maude::fmodule_is_not_abstract():
    assert not inspect.isabstract(Maude::FModule)


def test_maude::fmodule_constructor_exists():
    assert callable(Maude::FModule.__init__)


def test_maude::fmodule_constructor_args():
    sig = inspect.signature(Maude::FModule.__init__)
    params = list(sig.parameters.keys())



def test_theory_is_not_abstract():
    assert not inspect.isabstract(Theory)


def test_theory_constructor_exists():
    assert callable(Theory.__init__)


def test_theory_constructor_args():
    sig = inspect.signature(Theory.__init__)
    params = list(sig.parameters.keys())



def test_maude::stheory_is_not_abstract():
    assert not inspect.isabstract(Maude::STheory)


def test_maude::stheory_constructor_exists():
    assert callable(Maude::STheory.__init__)


def test_maude::stheory_constructor_args():
    sig = inspect.signature(Maude::STheory.__init__)
    params = list(sig.parameters.keys())



def test_maude::ftheory_is_not_abstract():
    assert not inspect.isabstract(Maude::FTheory)


def test_maude::ftheory_constructor_exists():
    assert callable(Maude::FTheory.__init__)


def test_maude::ftheory_constructor_args():
    sig = inspect.signature(Maude::FTheory.__init__)
    params = list(sig.parameters.keys())



def test_maude::modelement_is_not_abstract():
    assert not inspect.isabstract(Maude::ModElement)


def test_maude::modelement_constructor_exists():
    assert callable(Maude::ModElement.__init__)


def test_maude::modelement_constructor_args():
    sig = inspect.signature(Maude::ModElement.__init__)
    params = list(sig.parameters.keys())



def test_maudetopel_is_not_abstract():
    assert not inspect.isabstract(MaudeTopEl)


def test_maudetopel_constructor_exists():
    assert callable(MaudeTopEl.__init__)


def test_maudetopel_constructor_args():
    sig = inspect.signature(MaudeTopEl.__init__)
    params = list(sig.parameters.keys())



def test_maude::theory_is_not_abstract():
    assert not inspect.isabstract(Maude::Theory)


def test_maude::theory_constructor_exists():
    assert callable(Maude::Theory.__init__)


def test_maude::theory_constructor_args():
    sig = inspect.signature(Maude::Theory.__init__)
    params = list(sig.parameters.keys())



def test_maude::view_is_not_abstract():
    assert not inspect.isabstract(Maude::View)


def test_maude::view_constructor_exists():
    assert callable(Maude::View.__init__)


def test_maude::view_constructor_args():
    sig = inspect.signature(Maude::View.__init__)
    params = list(sig.parameters.keys())



def test_maude::module_is_not_abstract():
    assert not inspect.isabstract(Maude::Module)


def test_maude::module_constructor_exists():
    assert callable(Maude::Module.__init__)


def test_maude::module_constructor_args():
    sig = inspect.signature(Maude::Module.__init__)
    params = list(sig.parameters.keys())



def test_maude::subsortrel_is_not_abstract():
    assert not inspect.isabstract(Maude::SubsortRel)


def test_maude::subsortrel_constructor_exists():
    assert callable(Maude::SubsortRel.__init__)


def test_maude::subsortrel_constructor_args():
    sig = inspect.signature(Maude::SubsortRel.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_maude::kind_is_not_abstract():
    assert not inspect.isabstract(Maude::Kind)


def test_maude::kind_constructor_exists():
    assert callable(Maude::Kind.__init__)


def test_maude::kind_constructor_args():
    sig = inspect.signature(Maude::Kind.__init__)
    params = list(sig.parameters.keys())



def test_maude::sort_is_not_abstract():
    assert not inspect.isabstract(Maude::Sort)


def test_maude::sort_constructor_exists():
    assert callable(Maude::Sort.__init__)


def test_maude::sort_constructor_args():
    sig = inspect.signature(Maude::Sort.__init__)
    params = list(sig.parameters.keys())



def test_maude::type_is_not_abstract():
    assert not inspect.isabstract(Maude::Type)


def test_maude::type_constructor_exists():
    assert callable(Maude::Type.__init__)


def test_maude::type_constructor_args():
    sig = inspect.signature(Maude::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_maude::type_has_name():
    assert hasattr(Maude::Type, "name")
    descriptor = None
    for klass in Maude::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
ModExpression_strategy = st.builds(
    ModExpression,
)
Maude::RenModExp_strategy = st.builds(
    Maude::RenModExp,
)
Maude::InstModExp_strategy = st.builds(
    Maude::InstModExp,
)
Maude::ModExpression_strategy = st.builds(
    Maude::ModExpression,
)
Maude::MaudeTopEl_strategy = st.builds(
    Maude::MaudeTopEl,
    name=
        safe_text
)
Maude::MaudeSpec_strategy = st.builds(
    Maude::MaudeSpec,
)
Maude::Parameter_strategy = st.builds(
    Maude::Parameter,
    label=
        safe_text
)
Maude::TheoryIdModExp_strategy = st.builds(
    Maude::TheoryIdModExp,
)
Maude::ModuleIdModExp_strategy = st.builds(
    Maude::ModuleIdModExp,
)
Maude::CompModExp_strategy = st.builds(
    Maude::CompModExp,
)
RenMapping_strategy = st.builds(
    RenMapping,
)
Maude::SortMapping_strategy = st.builds(
    Maude::SortMapping,
    to=
        safe_text
)
ViewMapping_strategy = st.builds(
    ViewMapping,
)
Maude::RenMapping_strategy = st.builds(
    Maude::RenMapping,
)
Maude::TermMapping_strategy = st.builds(
    Maude::TermMapping,
)
Maude::ViewMapping_strategy = st.builds(
    Maude::ViewMapping,
)
Maude::LabelMapping_strategy = st.builds(
    Maude::LabelMapping,
    to=
        safe_text,
    from_=
        safe_text
)
Maude::OpMapping_strategy = st.builds(
    Maude::OpMapping,
    to=
        safe_text
)
Maude::OpTypedMapping_strategy = st.builds(
    Maude::OpTypedMapping,
    atts=
        safe_text,
    to=
        safe_text
)
EquationalCond_strategy = st.builds(
    EquationalCond,
)
Maude::BooleanCond_strategy = st.builds(
    Maude::BooleanCond,
)
Maude::MembershipCond_strategy = st.builds(
    Maude::MembershipCond,
)
Condition_strategy = st.builds(
    Condition,
)
Maude::RewriteCond_strategy = st.builds(
    Maude::RewriteCond,
)
Maude::EquationalCond_strategy = st.builds(
    Maude::EquationalCond,
)
Term_strategy = st.builds(
    Term,
)
Maude::RecTerm_strategy = st.builds(
    Maude::RecTerm,
    op=
        safe_text
)
Maude::Variable_strategy = st.builds(
    Maude::Variable,
    name=
        safe_text
)
Maude::Constant_strategy = st.builds(
    Maude::Constant,
    op=
        safe_text
)
Maude::EqualCond_strategy = st.builds(
    Maude::EqualCond,
)
Maude::MatchingCond_strategy = st.builds(
    Maude::MatchingCond,
)
Maude::Term_strategy = st.builds(
    Maude::Term,
)
Statement_strategy = st.builds(
    Statement,
)
Maude::Equation_strategy = st.builds(
    Maude::Equation,
)
Maude::Rule_strategy = st.builds(
    Maude::Rule,
)
Maude::Membership_strategy = st.builds(
    Maude::Membership,
)
Maude::Condition_strategy = st.builds(
    Maude::Condition,
)
ModElement_strategy = st.builds(
    ModElement,
)
Maude::Statement_strategy = st.builds(
    Maude::Statement,
    label=
        safe_text,
    atts=
        safe_text
)
Maude::Operation_strategy = st.builds(
    Maude::Operation,
    atts=
        safe_text,
    name=
        safe_text
)
Maude::ModImportation_strategy = st.builds(
    Maude::ModImportation,
    mode=
        safe_text
)
Module_strategy = st.builds(
    Module,
)
Maude::SModule_strategy = st.builds(
    Maude::SModule,
)
Maude::FModule_strategy = st.builds(
    Maude::FModule,
)
Theory_strategy = st.builds(
    Theory,
)
Maude::STheory_strategy = st.builds(
    Maude::STheory,
)
Maude::FTheory_strategy = st.builds(
    Maude::FTheory,
)
Maude::ModElement_strategy = st.builds(
    Maude::ModElement,
)
MaudeTopEl_strategy = st.builds(
    MaudeTopEl,
)
Maude::Theory_strategy = st.builds(
    Maude::Theory,
)
Maude::View_strategy = st.builds(
    Maude::View,
)
Maude::Module_strategy = st.builds(
    Maude::Module,
)
Maude::SubsortRel_strategy = st.builds(
    Maude::SubsortRel,
)
Type_strategy = st.builds(
    Type,
)
Maude::Kind_strategy = st.builds(
    Maude::Kind,
)
Maude::Sort_strategy = st.builds(
    Maude::Sort,
)
Maude::Type_strategy = st.builds(
    Maude::Type,
    name=
        safe_text
)

@given(instance=ModExpression_strategy)
@settings(max_examples=50)
def test_modexpression_instantiation(instance):
    assert isinstance(instance, ModExpression)

@given(instance=Maude::RenModExp_strategy)
@settings(max_examples=50)
def test_maude::renmodexp_instantiation(instance):
    assert isinstance(instance, Maude::RenModExp)

@given(instance=Maude::InstModExp_strategy)
@settings(max_examples=50)
def test_maude::instmodexp_instantiation(instance):
    assert isinstance(instance, Maude::InstModExp)

@given(instance=Maude::ModExpression_strategy)
@settings(max_examples=50)
def test_maude::modexpression_instantiation(instance):
    assert isinstance(instance, Maude::ModExpression)

@given(instance=Maude::MaudeTopEl_strategy)
@settings(max_examples=50)
def test_maude::maudetopel_instantiation(instance):
    assert isinstance(instance, Maude::MaudeTopEl)

@given(instance=Maude::MaudeTopEl_strategy)
def test_maude::maudetopel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Maude::MaudeTopEl_strategy)
def test_maude::maudetopel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Maude::MaudeSpec_strategy)
@settings(max_examples=50)
def test_maude::maudespec_instantiation(instance):
    assert isinstance(instance, Maude::MaudeSpec)

@given(instance=Maude::Parameter_strategy)
@settings(max_examples=50)
def test_maude::parameter_instantiation(instance):
    assert isinstance(instance, Maude::Parameter)

@given(instance=Maude::Parameter_strategy)
def test_maude::parameter_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=Maude::Parameter_strategy)
def test_maude::parameter_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Maude::TheoryIdModExp_strategy)
@settings(max_examples=50)
def test_maude::theoryidmodexp_instantiation(instance):
    assert isinstance(instance, Maude::TheoryIdModExp)

@given(instance=Maude::ModuleIdModExp_strategy)
@settings(max_examples=50)
def test_maude::moduleidmodexp_instantiation(instance):
    assert isinstance(instance, Maude::ModuleIdModExp)

@given(instance=Maude::CompModExp_strategy)
@settings(max_examples=50)
def test_maude::compmodexp_instantiation(instance):
    assert isinstance(instance, Maude::CompModExp)

@given(instance=RenMapping_strategy)
@settings(max_examples=50)
def test_renmapping_instantiation(instance):
    assert isinstance(instance, RenMapping)

@given(instance=Maude::SortMapping_strategy)
@settings(max_examples=50)
def test_maude::sortmapping_instantiation(instance):
    assert isinstance(instance, Maude::SortMapping)

@given(instance=Maude::SortMapping_strategy)
def test_maude::sortmapping_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=Maude::SortMapping_strategy)
def test_maude::sortmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=ViewMapping_strategy)
@settings(max_examples=50)
def test_viewmapping_instantiation(instance):
    assert isinstance(instance, ViewMapping)

@given(instance=Maude::RenMapping_strategy)
@settings(max_examples=50)
def test_maude::renmapping_instantiation(instance):
    assert isinstance(instance, Maude::RenMapping)

@given(instance=Maude::TermMapping_strategy)
@settings(max_examples=50)
def test_maude::termmapping_instantiation(instance):
    assert isinstance(instance, Maude::TermMapping)

@given(instance=Maude::ViewMapping_strategy)
@settings(max_examples=50)
def test_maude::viewmapping_instantiation(instance):
    assert isinstance(instance, Maude::ViewMapping)

@given(instance=Maude::LabelMapping_strategy)
@settings(max_examples=50)
def test_maude::labelmapping_instantiation(instance):
    assert isinstance(instance, Maude::LabelMapping)

@given(instance=Maude::LabelMapping_strategy)
def test_maude::labelmapping_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=Maude::LabelMapping_strategy)
def test_maude::labelmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=Maude::LabelMapping_strategy)
def test_maude::labelmapping_from__type(instance):
    assert isinstance(instance.from_, str)


@given(instance=Maude::LabelMapping_strategy)
def test_maude::labelmapping_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=Maude::OpMapping_strategy)
@settings(max_examples=50)
def test_maude::opmapping_instantiation(instance):
    assert isinstance(instance, Maude::OpMapping)

@given(instance=Maude::OpMapping_strategy)
def test_maude::opmapping_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=Maude::OpMapping_strategy)
def test_maude::opmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=Maude::OpTypedMapping_strategy)
@settings(max_examples=50)
def test_maude::optypedmapping_instantiation(instance):
    assert isinstance(instance, Maude::OpTypedMapping)

@given(instance=Maude::OpTypedMapping_strategy)
def test_maude::optypedmapping_atts_type(instance):
    assert isinstance(instance.atts, str)


@given(instance=Maude::OpTypedMapping_strategy)
def test_maude::optypedmapping_atts_setter(instance):
    original = instance.atts
    instance.atts = original
    assert instance.atts == original

@given(instance=Maude::OpTypedMapping_strategy)
def test_maude::optypedmapping_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=Maude::OpTypedMapping_strategy)
def test_maude::optypedmapping_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=EquationalCond_strategy)
@settings(max_examples=50)
def test_equationalcond_instantiation(instance):
    assert isinstance(instance, EquationalCond)

@given(instance=Maude::BooleanCond_strategy)
@settings(max_examples=50)
def test_maude::booleancond_instantiation(instance):
    assert isinstance(instance, Maude::BooleanCond)

@given(instance=Maude::MembershipCond_strategy)
@settings(max_examples=50)
def test_maude::membershipcond_instantiation(instance):
    assert isinstance(instance, Maude::MembershipCond)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=Maude::RewriteCond_strategy)
@settings(max_examples=50)
def test_maude::rewritecond_instantiation(instance):
    assert isinstance(instance, Maude::RewriteCond)

@given(instance=Maude::EquationalCond_strategy)
@settings(max_examples=50)
def test_maude::equationalcond_instantiation(instance):
    assert isinstance(instance, Maude::EquationalCond)

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=Maude::RecTerm_strategy)
@settings(max_examples=50)
def test_maude::recterm_instantiation(instance):
    assert isinstance(instance, Maude::RecTerm)

@given(instance=Maude::RecTerm_strategy)
def test_maude::recterm_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=Maude::RecTerm_strategy)
def test_maude::recterm_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=Maude::Variable_strategy)
@settings(max_examples=50)
def test_maude::variable_instantiation(instance):
    assert isinstance(instance, Maude::Variable)

@given(instance=Maude::Variable_strategy)
def test_maude::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Maude::Variable_strategy)
def test_maude::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Maude::Constant_strategy)
@settings(max_examples=50)
def test_maude::constant_instantiation(instance):
    assert isinstance(instance, Maude::Constant)

@given(instance=Maude::Constant_strategy)
def test_maude::constant_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=Maude::Constant_strategy)
def test_maude::constant_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=Maude::EqualCond_strategy)
@settings(max_examples=50)
def test_maude::equalcond_instantiation(instance):
    assert isinstance(instance, Maude::EqualCond)

@given(instance=Maude::MatchingCond_strategy)
@settings(max_examples=50)
def test_maude::matchingcond_instantiation(instance):
    assert isinstance(instance, Maude::MatchingCond)

@given(instance=Maude::Term_strategy)
@settings(max_examples=50)
def test_maude::term_instantiation(instance):
    assert isinstance(instance, Maude::Term)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=Maude::Equation_strategy)
@settings(max_examples=50)
def test_maude::equation_instantiation(instance):
    assert isinstance(instance, Maude::Equation)

@given(instance=Maude::Rule_strategy)
@settings(max_examples=50)
def test_maude::rule_instantiation(instance):
    assert isinstance(instance, Maude::Rule)

@given(instance=Maude::Membership_strategy)
@settings(max_examples=50)
def test_maude::membership_instantiation(instance):
    assert isinstance(instance, Maude::Membership)

@given(instance=Maude::Condition_strategy)
@settings(max_examples=50)
def test_maude::condition_instantiation(instance):
    assert isinstance(instance, Maude::Condition)

@given(instance=ModElement_strategy)
@settings(max_examples=50)
def test_modelement_instantiation(instance):
    assert isinstance(instance, ModElement)

@given(instance=Maude::Statement_strategy)
@settings(max_examples=50)
def test_maude::statement_instantiation(instance):
    assert isinstance(instance, Maude::Statement)

@given(instance=Maude::Statement_strategy)
def test_maude::statement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=Maude::Statement_strategy)
def test_maude::statement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Maude::Statement_strategy)
def test_maude::statement_atts_type(instance):
    assert isinstance(instance.atts, str)


@given(instance=Maude::Statement_strategy)
def test_maude::statement_atts_setter(instance):
    original = instance.atts
    instance.atts = original
    assert instance.atts == original

@given(instance=Maude::Operation_strategy)
@settings(max_examples=50)
def test_maude::operation_instantiation(instance):
    assert isinstance(instance, Maude::Operation)

@given(instance=Maude::Operation_strategy)
def test_maude::operation_atts_type(instance):
    assert isinstance(instance.atts, str)


@given(instance=Maude::Operation_strategy)
def test_maude::operation_atts_setter(instance):
    original = instance.atts
    instance.atts = original
    assert instance.atts == original

@given(instance=Maude::Operation_strategy)
def test_maude::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Maude::Operation_strategy)
def test_maude::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Maude::ModImportation_strategy)
@settings(max_examples=50)
def test_maude::modimportation_instantiation(instance):
    assert isinstance(instance, Maude::ModImportation)

@given(instance=Maude::ModImportation_strategy)
def test_maude::modimportation_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=Maude::ModImportation_strategy)
def test_maude::modimportation_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=Maude::SModule_strategy)
@settings(max_examples=50)
def test_maude::smodule_instantiation(instance):
    assert isinstance(instance, Maude::SModule)

@given(instance=Maude::FModule_strategy)
@settings(max_examples=50)
def test_maude::fmodule_instantiation(instance):
    assert isinstance(instance, Maude::FModule)

@given(instance=Theory_strategy)
@settings(max_examples=50)
def test_theory_instantiation(instance):
    assert isinstance(instance, Theory)

@given(instance=Maude::STheory_strategy)
@settings(max_examples=50)
def test_maude::stheory_instantiation(instance):
    assert isinstance(instance, Maude::STheory)

@given(instance=Maude::FTheory_strategy)
@settings(max_examples=50)
def test_maude::ftheory_instantiation(instance):
    assert isinstance(instance, Maude::FTheory)

@given(instance=Maude::ModElement_strategy)
@settings(max_examples=50)
def test_maude::modelement_instantiation(instance):
    assert isinstance(instance, Maude::ModElement)

@given(instance=MaudeTopEl_strategy)
@settings(max_examples=50)
def test_maudetopel_instantiation(instance):
    assert isinstance(instance, MaudeTopEl)

@given(instance=Maude::Theory_strategy)
@settings(max_examples=50)
def test_maude::theory_instantiation(instance):
    assert isinstance(instance, Maude::Theory)

@given(instance=Maude::View_strategy)
@settings(max_examples=50)
def test_maude::view_instantiation(instance):
    assert isinstance(instance, Maude::View)

@given(instance=Maude::Module_strategy)
@settings(max_examples=50)
def test_maude::module_instantiation(instance):
    assert isinstance(instance, Maude::Module)

@given(instance=Maude::SubsortRel_strategy)
@settings(max_examples=50)
def test_maude::subsortrel_instantiation(instance):
    assert isinstance(instance, Maude::SubsortRel)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=Maude::Kind_strategy)
@settings(max_examples=50)
def test_maude::kind_instantiation(instance):
    assert isinstance(instance, Maude::Kind)

@given(instance=Maude::Sort_strategy)
@settings(max_examples=50)
def test_maude::sort_instantiation(instance):
    assert isinstance(instance, Maude::Sort)

@given(instance=Maude::Type_strategy)
@settings(max_examples=50)
def test_maude::type_instantiation(instance):
    assert isinstance(instance, Maude::Type)

@given(instance=Maude::Type_strategy)
def test_maude::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Maude::Type_strategy)
def test_maude::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
