import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UnaryExpression,
    prolog_expressions_BitwiseNegation,
    prolog_expressions_PositiveNumber,
    prolog_expressions_NegativeNumber,
    prolog_expressions_NotProvable,
    prolog_directives_PredicateIndicator,
    PredicateIndicator,
    BinaryExpression,
    prolog_expressions_Xor,
    prolog_expressions_StructuralEquivalence,
    prolog_expressions_BinaryOr,
    prolog_expressions_ParticalUnification,
    prolog_expressions_Unification,
    prolog_expressions_Division,
    prolog_expressions_Minus,
    prolog_expressions_StandardOrderBefore,
    prolog_expressions_Univ,
    prolog_expressions_GreaterThan,
    prolog_expressions_Div,
    prolog_expressions_Equivalence,
    prolog_expressions_GreaterOrEqual,
    prolog_expressions_SoftCut,
    prolog_expressions_BinaryAnd,
    prolog_expressions_LogicalAnd,
    prolog_expressions_EqualOrStandardOrderAfter,
    prolog_expressions_Rem,
    prolog_expressions_LessThan,
    prolog_expressions_IntegerDivision,
    prolog_expressions_Power,
    prolog_expressions_Mod,
    prolog_expressions_Is,
    prolog_expressions_NonEqualNumber,
    prolog_expressions_StructuralEquivalenceNotProvable,
    prolog_expressions_Multiplication,
    prolog_expressions_ModuleCall,
    prolog_expressions_LessOrEqual,
    prolog_expressions_BitwiseShiftLeft,
    prolog_expressions_StandardOrderAfter,
    prolog_expressions_Plus,
    prolog_expressions_NotUnifiable,
    prolog_expressions_EqualOrStandardOrderBefore,
    prolog_expressions_Rdiv,
    prolog_expressions_SubDict,
    prolog_expressions_As,
    prolog_expressions_Disequality,
    prolog_expressions_Condition,
    prolog_expressions_NumberEqual,
    prolog_expressions_LogicalOr,
    prolog_expressions_Expression,
    Directive,
    prolog_directives_Discontiguous,
    prolog_directives_Multifile,
    prolog_directives_Volatile,
    prolog_directives_Dynamic,
    prolog_directives_Public,
    Term,
    prolog_AtomicNumber,
    ControlPredicate,
    prolog_False,
    prolog_Cut,
    prolog_Fail,
    prolog_True,
    prolog_ControlPredicate,
    prolog_List,
    prolog_AtomicQuotedString,
    Expression,
    prolog_expressions_UnaryExpression,
    prolog_expressions_BinaryExpression,
    prolog_Term,
    Clause,
    prolog_CompoundTerm,
    prolog_Rule,
    prolog_directives_Directive,
    prolog_Fact,
    prolog_directives_Table,
    prolog_Comment,
    prolog_Clause,
    prolog_Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_bitwisenegation_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_BitwiseNegation)


def test_prolog_expressions_bitwisenegation_constructor_exists():
    assert callable(prolog_expressions_BitwiseNegation.__init__)


def test_prolog_expressions_bitwisenegation_constructor_args():
    sig = inspect.signature(prolog_expressions_BitwiseNegation.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_positivenumber_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_PositiveNumber)


def test_prolog_expressions_positivenumber_constructor_exists():
    assert callable(prolog_expressions_PositiveNumber.__init__)


def test_prolog_expressions_positivenumber_constructor_args():
    sig = inspect.signature(prolog_expressions_PositiveNumber.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_negativenumber_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_NegativeNumber)


def test_prolog_expressions_negativenumber_constructor_exists():
    assert callable(prolog_expressions_NegativeNumber.__init__)


def test_prolog_expressions_negativenumber_constructor_args():
    sig = inspect.signature(prolog_expressions_NegativeNumber.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_notprovable_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_NotProvable)


def test_prolog_expressions_notprovable_constructor_exists():
    assert callable(prolog_expressions_NotProvable.__init__)


def test_prolog_expressions_notprovable_constructor_args():
    sig = inspect.signature(prolog_expressions_NotProvable.__init__)
    params = list(sig.parameters.keys())



def test_prolog_directives_predicateindicator_is_not_abstract():
    assert not inspect.isabstract(prolog_directives_PredicateIndicator)


def test_prolog_directives_predicateindicator_constructor_exists():
    assert callable(prolog_directives_PredicateIndicator.__init__)


def test_prolog_directives_predicateindicator_constructor_args():
    sig = inspect.signature(prolog_directives_PredicateIndicator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "arity" in params, "Missing parameter 'arity'"

def test_prolog_directives_predicateindicator_has_name():
    assert hasattr(prolog_directives_PredicateIndicator, "name")
    descriptor = None
    for klass in prolog_directives_PredicateIndicator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_prolog_directives_predicateindicator_has_arity():
    assert hasattr(prolog_directives_PredicateIndicator, "arity")
    descriptor = None
    for klass in prolog_directives_PredicateIndicator.__mro__:
        if "arity" in klass.__dict__:
            descriptor = klass.__dict__["arity"]
            break
    assert isinstance(descriptor, property)



def test_predicateindicator_is_not_abstract():
    assert not inspect.isabstract(PredicateIndicator)


def test_predicateindicator_constructor_exists():
    assert callable(PredicateIndicator.__init__)


def test_predicateindicator_constructor_args():
    sig = inspect.signature(PredicateIndicator.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_xor_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Xor)


def test_prolog_expressions_xor_constructor_exists():
    assert callable(prolog_expressions_Xor.__init__)


def test_prolog_expressions_xor_constructor_args():
    sig = inspect.signature(prolog_expressions_Xor.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_structuralequivalence_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_StructuralEquivalence)


def test_prolog_expressions_structuralequivalence_constructor_exists():
    assert callable(prolog_expressions_StructuralEquivalence.__init__)


def test_prolog_expressions_structuralequivalence_constructor_args():
    sig = inspect.signature(prolog_expressions_StructuralEquivalence.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_binaryor_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_BinaryOr)


def test_prolog_expressions_binaryor_constructor_exists():
    assert callable(prolog_expressions_BinaryOr.__init__)


def test_prolog_expressions_binaryor_constructor_args():
    sig = inspect.signature(prolog_expressions_BinaryOr.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_particalunification_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_ParticalUnification)


def test_prolog_expressions_particalunification_constructor_exists():
    assert callable(prolog_expressions_ParticalUnification.__init__)


def test_prolog_expressions_particalunification_constructor_args():
    sig = inspect.signature(prolog_expressions_ParticalUnification.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_unification_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Unification)


def test_prolog_expressions_unification_constructor_exists():
    assert callable(prolog_expressions_Unification.__init__)


def test_prolog_expressions_unification_constructor_args():
    sig = inspect.signature(prolog_expressions_Unification.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_division_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Division)


def test_prolog_expressions_division_constructor_exists():
    assert callable(prolog_expressions_Division.__init__)


def test_prolog_expressions_division_constructor_args():
    sig = inspect.signature(prolog_expressions_Division.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_minus_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Minus)


def test_prolog_expressions_minus_constructor_exists():
    assert callable(prolog_expressions_Minus.__init__)


def test_prolog_expressions_minus_constructor_args():
    sig = inspect.signature(prolog_expressions_Minus.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_standardorderbefore_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_StandardOrderBefore)


def test_prolog_expressions_standardorderbefore_constructor_exists():
    assert callable(prolog_expressions_StandardOrderBefore.__init__)


def test_prolog_expressions_standardorderbefore_constructor_args():
    sig = inspect.signature(prolog_expressions_StandardOrderBefore.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_univ_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Univ)


def test_prolog_expressions_univ_constructor_exists():
    assert callable(prolog_expressions_Univ.__init__)


def test_prolog_expressions_univ_constructor_args():
    sig = inspect.signature(prolog_expressions_Univ.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_greaterthan_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_GreaterThan)


def test_prolog_expressions_greaterthan_constructor_exists():
    assert callable(prolog_expressions_GreaterThan.__init__)


def test_prolog_expressions_greaterthan_constructor_args():
    sig = inspect.signature(prolog_expressions_GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_div_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Div)


def test_prolog_expressions_div_constructor_exists():
    assert callable(prolog_expressions_Div.__init__)


def test_prolog_expressions_div_constructor_args():
    sig = inspect.signature(prolog_expressions_Div.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_equivalence_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Equivalence)


def test_prolog_expressions_equivalence_constructor_exists():
    assert callable(prolog_expressions_Equivalence.__init__)


def test_prolog_expressions_equivalence_constructor_args():
    sig = inspect.signature(prolog_expressions_Equivalence.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_greaterorequal_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_GreaterOrEqual)


def test_prolog_expressions_greaterorequal_constructor_exists():
    assert callable(prolog_expressions_GreaterOrEqual.__init__)


def test_prolog_expressions_greaterorequal_constructor_args():
    sig = inspect.signature(prolog_expressions_GreaterOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_softcut_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_SoftCut)


def test_prolog_expressions_softcut_constructor_exists():
    assert callable(prolog_expressions_SoftCut.__init__)


def test_prolog_expressions_softcut_constructor_args():
    sig = inspect.signature(prolog_expressions_SoftCut.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_binaryand_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_BinaryAnd)


def test_prolog_expressions_binaryand_constructor_exists():
    assert callable(prolog_expressions_BinaryAnd.__init__)


def test_prolog_expressions_binaryand_constructor_args():
    sig = inspect.signature(prolog_expressions_BinaryAnd.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_logicaland_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_LogicalAnd)


def test_prolog_expressions_logicaland_constructor_exists():
    assert callable(prolog_expressions_LogicalAnd.__init__)


def test_prolog_expressions_logicaland_constructor_args():
    sig = inspect.signature(prolog_expressions_LogicalAnd.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_equalorstandardorderafter_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_EqualOrStandardOrderAfter)


def test_prolog_expressions_equalorstandardorderafter_constructor_exists():
    assert callable(prolog_expressions_EqualOrStandardOrderAfter.__init__)


def test_prolog_expressions_equalorstandardorderafter_constructor_args():
    sig = inspect.signature(prolog_expressions_EqualOrStandardOrderAfter.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_rem_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Rem)


def test_prolog_expressions_rem_constructor_exists():
    assert callable(prolog_expressions_Rem.__init__)


def test_prolog_expressions_rem_constructor_args():
    sig = inspect.signature(prolog_expressions_Rem.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_lessthan_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_LessThan)


def test_prolog_expressions_lessthan_constructor_exists():
    assert callable(prolog_expressions_LessThan.__init__)


def test_prolog_expressions_lessthan_constructor_args():
    sig = inspect.signature(prolog_expressions_LessThan.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_integerdivision_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_IntegerDivision)


def test_prolog_expressions_integerdivision_constructor_exists():
    assert callable(prolog_expressions_IntegerDivision.__init__)


def test_prolog_expressions_integerdivision_constructor_args():
    sig = inspect.signature(prolog_expressions_IntegerDivision.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_power_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Power)


def test_prolog_expressions_power_constructor_exists():
    assert callable(prolog_expressions_Power.__init__)


def test_prolog_expressions_power_constructor_args():
    sig = inspect.signature(prolog_expressions_Power.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_mod_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Mod)


def test_prolog_expressions_mod_constructor_exists():
    assert callable(prolog_expressions_Mod.__init__)


def test_prolog_expressions_mod_constructor_args():
    sig = inspect.signature(prolog_expressions_Mod.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_is_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Is)


def test_prolog_expressions_is_constructor_exists():
    assert callable(prolog_expressions_Is.__init__)


def test_prolog_expressions_is_constructor_args():
    sig = inspect.signature(prolog_expressions_Is.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_nonequalnumber_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_NonEqualNumber)


def test_prolog_expressions_nonequalnumber_constructor_exists():
    assert callable(prolog_expressions_NonEqualNumber.__init__)


def test_prolog_expressions_nonequalnumber_constructor_args():
    sig = inspect.signature(prolog_expressions_NonEqualNumber.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_structuralequivalencenotprovable_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_StructuralEquivalenceNotProvable)


def test_prolog_expressions_structuralequivalencenotprovable_constructor_exists():
    assert callable(prolog_expressions_StructuralEquivalenceNotProvable.__init__)


def test_prolog_expressions_structuralequivalencenotprovable_constructor_args():
    sig = inspect.signature(prolog_expressions_StructuralEquivalenceNotProvable.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_multiplication_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Multiplication)


def test_prolog_expressions_multiplication_constructor_exists():
    assert callable(prolog_expressions_Multiplication.__init__)


def test_prolog_expressions_multiplication_constructor_args():
    sig = inspect.signature(prolog_expressions_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_modulecall_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_ModuleCall)


def test_prolog_expressions_modulecall_constructor_exists():
    assert callable(prolog_expressions_ModuleCall.__init__)


def test_prolog_expressions_modulecall_constructor_args():
    sig = inspect.signature(prolog_expressions_ModuleCall.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_lessorequal_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_LessOrEqual)


def test_prolog_expressions_lessorequal_constructor_exists():
    assert callable(prolog_expressions_LessOrEqual.__init__)


def test_prolog_expressions_lessorequal_constructor_args():
    sig = inspect.signature(prolog_expressions_LessOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_bitwiseshiftleft_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_BitwiseShiftLeft)


def test_prolog_expressions_bitwiseshiftleft_constructor_exists():
    assert callable(prolog_expressions_BitwiseShiftLeft.__init__)


def test_prolog_expressions_bitwiseshiftleft_constructor_args():
    sig = inspect.signature(prolog_expressions_BitwiseShiftLeft.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_standardorderafter_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_StandardOrderAfter)


def test_prolog_expressions_standardorderafter_constructor_exists():
    assert callable(prolog_expressions_StandardOrderAfter.__init__)


def test_prolog_expressions_standardorderafter_constructor_args():
    sig = inspect.signature(prolog_expressions_StandardOrderAfter.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_plus_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Plus)


def test_prolog_expressions_plus_constructor_exists():
    assert callable(prolog_expressions_Plus.__init__)


def test_prolog_expressions_plus_constructor_args():
    sig = inspect.signature(prolog_expressions_Plus.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_notunifiable_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_NotUnifiable)


def test_prolog_expressions_notunifiable_constructor_exists():
    assert callable(prolog_expressions_NotUnifiable.__init__)


def test_prolog_expressions_notunifiable_constructor_args():
    sig = inspect.signature(prolog_expressions_NotUnifiable.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_equalorstandardorderbefore_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_EqualOrStandardOrderBefore)


def test_prolog_expressions_equalorstandardorderbefore_constructor_exists():
    assert callable(prolog_expressions_EqualOrStandardOrderBefore.__init__)


def test_prolog_expressions_equalorstandardorderbefore_constructor_args():
    sig = inspect.signature(prolog_expressions_EqualOrStandardOrderBefore.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_rdiv_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Rdiv)


def test_prolog_expressions_rdiv_constructor_exists():
    assert callable(prolog_expressions_Rdiv.__init__)


def test_prolog_expressions_rdiv_constructor_args():
    sig = inspect.signature(prolog_expressions_Rdiv.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_subdict_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_SubDict)


def test_prolog_expressions_subdict_constructor_exists():
    assert callable(prolog_expressions_SubDict.__init__)


def test_prolog_expressions_subdict_constructor_args():
    sig = inspect.signature(prolog_expressions_SubDict.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_as_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_As)


def test_prolog_expressions_as_constructor_exists():
    assert callable(prolog_expressions_As.__init__)


def test_prolog_expressions_as_constructor_args():
    sig = inspect.signature(prolog_expressions_As.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_disequality_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Disequality)


def test_prolog_expressions_disequality_constructor_exists():
    assert callable(prolog_expressions_Disequality.__init__)


def test_prolog_expressions_disequality_constructor_args():
    sig = inspect.signature(prolog_expressions_Disequality.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_condition_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Condition)


def test_prolog_expressions_condition_constructor_exists():
    assert callable(prolog_expressions_Condition.__init__)


def test_prolog_expressions_condition_constructor_args():
    sig = inspect.signature(prolog_expressions_Condition.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_numberequal_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_NumberEqual)


def test_prolog_expressions_numberequal_constructor_exists():
    assert callable(prolog_expressions_NumberEqual.__init__)


def test_prolog_expressions_numberequal_constructor_args():
    sig = inspect.signature(prolog_expressions_NumberEqual.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_logicalor_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_LogicalOr)


def test_prolog_expressions_logicalor_constructor_exists():
    assert callable(prolog_expressions_LogicalOr.__init__)


def test_prolog_expressions_logicalor_constructor_args():
    sig = inspect.signature(prolog_expressions_LogicalOr.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_Expression)


def test_prolog_expressions_expression_constructor_exists():
    assert callable(prolog_expressions_Expression.__init__)


def test_prolog_expressions_expression_constructor_args():
    sig = inspect.signature(prolog_expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_directive_is_not_abstract():
    assert not inspect.isabstract(Directive)


def test_directive_constructor_exists():
    assert callable(Directive.__init__)


def test_directive_constructor_args():
    sig = inspect.signature(Directive.__init__)
    params = list(sig.parameters.keys())



def test_prolog_directives_discontiguous_is_not_abstract():
    assert not inspect.isabstract(prolog_directives_Discontiguous)


def test_prolog_directives_discontiguous_constructor_exists():
    assert callable(prolog_directives_Discontiguous.__init__)


def test_prolog_directives_discontiguous_constructor_args():
    sig = inspect.signature(prolog_directives_Discontiguous.__init__)
    params = list(sig.parameters.keys())



def test_prolog_directives_multifile_is_not_abstract():
    assert not inspect.isabstract(prolog_directives_Multifile)


def test_prolog_directives_multifile_constructor_exists():
    assert callable(prolog_directives_Multifile.__init__)


def test_prolog_directives_multifile_constructor_args():
    sig = inspect.signature(prolog_directives_Multifile.__init__)
    params = list(sig.parameters.keys())



def test_prolog_directives_volatile_is_not_abstract():
    assert not inspect.isabstract(prolog_directives_Volatile)


def test_prolog_directives_volatile_constructor_exists():
    assert callable(prolog_directives_Volatile.__init__)


def test_prolog_directives_volatile_constructor_args():
    sig = inspect.signature(prolog_directives_Volatile.__init__)
    params = list(sig.parameters.keys())



def test_prolog_directives_dynamic_is_not_abstract():
    assert not inspect.isabstract(prolog_directives_Dynamic)


def test_prolog_directives_dynamic_constructor_exists():
    assert callable(prolog_directives_Dynamic.__init__)


def test_prolog_directives_dynamic_constructor_args():
    sig = inspect.signature(prolog_directives_Dynamic.__init__)
    params = list(sig.parameters.keys())



def test_prolog_directives_public_is_not_abstract():
    assert not inspect.isabstract(prolog_directives_Public)


def test_prolog_directives_public_constructor_exists():
    assert callable(prolog_directives_Public.__init__)


def test_prolog_directives_public_constructor_args():
    sig = inspect.signature(prolog_directives_Public.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_prolog_atomicnumber_is_not_abstract():
    assert not inspect.isabstract(prolog_AtomicNumber)


def test_prolog_atomicnumber_constructor_exists():
    assert callable(prolog_AtomicNumber.__init__)


def test_prolog_atomicnumber_constructor_args():
    sig = inspect.signature(prolog_AtomicNumber.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_prolog_atomicnumber_has_value():
    assert hasattr(prolog_AtomicNumber, "value")
    descriptor = None
    for klass in prolog_AtomicNumber.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_controlpredicate_is_not_abstract():
    assert not inspect.isabstract(ControlPredicate)


def test_controlpredicate_constructor_exists():
    assert callable(ControlPredicate.__init__)


def test_controlpredicate_constructor_args():
    sig = inspect.signature(ControlPredicate.__init__)
    params = list(sig.parameters.keys())



def test_prolog_false_is_not_abstract():
    assert not inspect.isabstract(prolog_False)


def test_prolog_false_constructor_exists():
    assert callable(prolog_False.__init__)


def test_prolog_false_constructor_args():
    sig = inspect.signature(prolog_False.__init__)
    params = list(sig.parameters.keys())



def test_prolog_cut_is_not_abstract():
    assert not inspect.isabstract(prolog_Cut)


def test_prolog_cut_constructor_exists():
    assert callable(prolog_Cut.__init__)


def test_prolog_cut_constructor_args():
    sig = inspect.signature(prolog_Cut.__init__)
    params = list(sig.parameters.keys())



def test_prolog_fail_is_not_abstract():
    assert not inspect.isabstract(prolog_Fail)


def test_prolog_fail_constructor_exists():
    assert callable(prolog_Fail.__init__)


def test_prolog_fail_constructor_args():
    sig = inspect.signature(prolog_Fail.__init__)
    params = list(sig.parameters.keys())



def test_prolog_true_is_not_abstract():
    assert not inspect.isabstract(prolog_True)


def test_prolog_true_constructor_exists():
    assert callable(prolog_True.__init__)


def test_prolog_true_constructor_args():
    sig = inspect.signature(prolog_True.__init__)
    params = list(sig.parameters.keys())



def test_prolog_controlpredicate_is_not_abstract():
    assert not inspect.isabstract(prolog_ControlPredicate)


def test_prolog_controlpredicate_constructor_exists():
    assert callable(prolog_ControlPredicate.__init__)


def test_prolog_controlpredicate_constructor_args():
    sig = inspect.signature(prolog_ControlPredicate.__init__)
    params = list(sig.parameters.keys())



def test_prolog_list_is_not_abstract():
    assert not inspect.isabstract(prolog_List)


def test_prolog_list_constructor_exists():
    assert callable(prolog_List.__init__)


def test_prolog_list_constructor_args():
    sig = inspect.signature(prolog_List.__init__)
    params = list(sig.parameters.keys())



def test_prolog_atomicquotedstring_is_not_abstract():
    assert not inspect.isabstract(prolog_AtomicQuotedString)


def test_prolog_atomicquotedstring_constructor_exists():
    assert callable(prolog_AtomicQuotedString.__init__)


def test_prolog_atomicquotedstring_constructor_args():
    sig = inspect.signature(prolog_AtomicQuotedString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_prolog_atomicquotedstring_has_value():
    assert hasattr(prolog_AtomicQuotedString, "value")
    descriptor = None
    for klass in prolog_AtomicQuotedString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_UnaryExpression)


def test_prolog_expressions_unaryexpression_constructor_exists():
    assert callable(prolog_expressions_UnaryExpression.__init__)


def test_prolog_expressions_unaryexpression_constructor_args():
    sig = inspect.signature(prolog_expressions_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_prolog_expressions_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(prolog_expressions_BinaryExpression)


def test_prolog_expressions_binaryexpression_constructor_exists():
    assert callable(prolog_expressions_BinaryExpression.__init__)


def test_prolog_expressions_binaryexpression_constructor_args():
    sig = inspect.signature(prolog_expressions_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_prolog_term_is_not_abstract():
    assert not inspect.isabstract(prolog_Term)


def test_prolog_term_constructor_exists():
    assert callable(prolog_Term.__init__)


def test_prolog_term_constructor_args():
    sig = inspect.signature(prolog_Term.__init__)
    params = list(sig.parameters.keys())



def test_clause_is_not_abstract():
    assert not inspect.isabstract(Clause)


def test_clause_constructor_exists():
    assert callable(Clause.__init__)


def test_clause_constructor_args():
    sig = inspect.signature(Clause.__init__)
    params = list(sig.parameters.keys())



def test_prolog_compoundterm_is_not_abstract():
    assert not inspect.isabstract(prolog_CompoundTerm)


def test_prolog_compoundterm_constructor_exists():
    assert callable(prolog_CompoundTerm.__init__)


def test_prolog_compoundterm_constructor_args():
    sig = inspect.signature(prolog_CompoundTerm.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_prolog_compoundterm_has_value():
    assert hasattr(prolog_CompoundTerm, "value")
    descriptor = None
    for klass in prolog_CompoundTerm.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_prolog_rule_is_not_abstract():
    assert not inspect.isabstract(prolog_Rule)


def test_prolog_rule_constructor_exists():
    assert callable(prolog_Rule.__init__)


def test_prolog_rule_constructor_args():
    sig = inspect.signature(prolog_Rule.__init__)
    params = list(sig.parameters.keys())



def test_prolog_directives_directive_is_not_abstract():
    assert not inspect.isabstract(prolog_directives_Directive)


def test_prolog_directives_directive_constructor_exists():
    assert callable(prolog_directives_Directive.__init__)


def test_prolog_directives_directive_constructor_args():
    sig = inspect.signature(prolog_directives_Directive.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_prolog_directives_directive_has_name():
    assert hasattr(prolog_directives_Directive, "name")
    descriptor = None
    for klass in prolog_directives_Directive.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prolog_fact_is_not_abstract():
    assert not inspect.isabstract(prolog_Fact)


def test_prolog_fact_constructor_exists():
    assert callable(prolog_Fact.__init__)


def test_prolog_fact_constructor_args():
    sig = inspect.signature(prolog_Fact.__init__)
    params = list(sig.parameters.keys())



def test_prolog_directives_table_is_not_abstract():
    assert not inspect.isabstract(prolog_directives_Table)


def test_prolog_directives_table_constructor_exists():
    assert callable(prolog_directives_Table.__init__)


def test_prolog_directives_table_constructor_args():
    sig = inspect.signature(prolog_directives_Table.__init__)
    params = list(sig.parameters.keys())



def test_prolog_comment_is_not_abstract():
    assert not inspect.isabstract(prolog_Comment)


def test_prolog_comment_constructor_exists():
    assert callable(prolog_Comment.__init__)


def test_prolog_comment_constructor_args():
    sig = inspect.signature(prolog_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_prolog_comment_has_value():
    assert hasattr(prolog_Comment, "value")
    descriptor = None
    for klass in prolog_Comment.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_prolog_clause_is_not_abstract():
    assert not inspect.isabstract(prolog_Clause)


def test_prolog_clause_constructor_exists():
    assert callable(prolog_Clause.__init__)


def test_prolog_clause_constructor_args():
    sig = inspect.signature(prolog_Clause.__init__)
    params = list(sig.parameters.keys())



def test_prolog_program_is_not_abstract():
    assert not inspect.isabstract(prolog_Program)


def test_prolog_program_constructor_exists():
    assert callable(prolog_Program.__init__)


def test_prolog_program_constructor_args():
    sig = inspect.signature(prolog_Program.__init__)
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
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
prolog_expressions_BitwiseNegation_strategy = st.builds(
    prolog_expressions_BitwiseNegation,
)
prolog_expressions_PositiveNumber_strategy = st.builds(
    prolog_expressions_PositiveNumber,
)
prolog_expressions_NegativeNumber_strategy = st.builds(
    prolog_expressions_NegativeNumber,
)
prolog_expressions_NotProvable_strategy = st.builds(
    prolog_expressions_NotProvable,
)
prolog_directives_PredicateIndicator_strategy = st.builds(
    prolog_directives_PredicateIndicator,
    name=
        safe_text,
    arity=
        st.integers()
)
PredicateIndicator_strategy = st.builds(
    PredicateIndicator,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
prolog_expressions_Xor_strategy = st.builds(
    prolog_expressions_Xor,
)
prolog_expressions_StructuralEquivalence_strategy = st.builds(
    prolog_expressions_StructuralEquivalence,
)
prolog_expressions_BinaryOr_strategy = st.builds(
    prolog_expressions_BinaryOr,
)
prolog_expressions_ParticalUnification_strategy = st.builds(
    prolog_expressions_ParticalUnification,
)
prolog_expressions_Unification_strategy = st.builds(
    prolog_expressions_Unification,
)
prolog_expressions_Division_strategy = st.builds(
    prolog_expressions_Division,
)
prolog_expressions_Minus_strategy = st.builds(
    prolog_expressions_Minus,
)
prolog_expressions_StandardOrderBefore_strategy = st.builds(
    prolog_expressions_StandardOrderBefore,
)
prolog_expressions_Univ_strategy = st.builds(
    prolog_expressions_Univ,
)
prolog_expressions_GreaterThan_strategy = st.builds(
    prolog_expressions_GreaterThan,
)
prolog_expressions_Div_strategy = st.builds(
    prolog_expressions_Div,
)
prolog_expressions_Equivalence_strategy = st.builds(
    prolog_expressions_Equivalence,
)
prolog_expressions_GreaterOrEqual_strategy = st.builds(
    prolog_expressions_GreaterOrEqual,
)
prolog_expressions_SoftCut_strategy = st.builds(
    prolog_expressions_SoftCut,
)
prolog_expressions_BinaryAnd_strategy = st.builds(
    prolog_expressions_BinaryAnd,
)
prolog_expressions_LogicalAnd_strategy = st.builds(
    prolog_expressions_LogicalAnd,
)
prolog_expressions_EqualOrStandardOrderAfter_strategy = st.builds(
    prolog_expressions_EqualOrStandardOrderAfter,
)
prolog_expressions_Rem_strategy = st.builds(
    prolog_expressions_Rem,
)
prolog_expressions_LessThan_strategy = st.builds(
    prolog_expressions_LessThan,
)
prolog_expressions_IntegerDivision_strategy = st.builds(
    prolog_expressions_IntegerDivision,
)
prolog_expressions_Power_strategy = st.builds(
    prolog_expressions_Power,
)
prolog_expressions_Mod_strategy = st.builds(
    prolog_expressions_Mod,
)
prolog_expressions_Is_strategy = st.builds(
    prolog_expressions_Is,
)
prolog_expressions_NonEqualNumber_strategy = st.builds(
    prolog_expressions_NonEqualNumber,
)
prolog_expressions_StructuralEquivalenceNotProvable_strategy = st.builds(
    prolog_expressions_StructuralEquivalenceNotProvable,
)
prolog_expressions_Multiplication_strategy = st.builds(
    prolog_expressions_Multiplication,
)
prolog_expressions_ModuleCall_strategy = st.builds(
    prolog_expressions_ModuleCall,
)
prolog_expressions_LessOrEqual_strategy = st.builds(
    prolog_expressions_LessOrEqual,
)
prolog_expressions_BitwiseShiftLeft_strategy = st.builds(
    prolog_expressions_BitwiseShiftLeft,
)
prolog_expressions_StandardOrderAfter_strategy = st.builds(
    prolog_expressions_StandardOrderAfter,
)
prolog_expressions_Plus_strategy = st.builds(
    prolog_expressions_Plus,
)
prolog_expressions_NotUnifiable_strategy = st.builds(
    prolog_expressions_NotUnifiable,
)
prolog_expressions_EqualOrStandardOrderBefore_strategy = st.builds(
    prolog_expressions_EqualOrStandardOrderBefore,
)
prolog_expressions_Rdiv_strategy = st.builds(
    prolog_expressions_Rdiv,
)
prolog_expressions_SubDict_strategy = st.builds(
    prolog_expressions_SubDict,
)
prolog_expressions_As_strategy = st.builds(
    prolog_expressions_As,
)
prolog_expressions_Disequality_strategy = st.builds(
    prolog_expressions_Disequality,
)
prolog_expressions_Condition_strategy = st.builds(
    prolog_expressions_Condition,
)
prolog_expressions_NumberEqual_strategy = st.builds(
    prolog_expressions_NumberEqual,
)
prolog_expressions_LogicalOr_strategy = st.builds(
    prolog_expressions_LogicalOr,
)
prolog_expressions_Expression_strategy = st.builds(
    prolog_expressions_Expression,
)
Directive_strategy = st.builds(
    Directive,
)
prolog_directives_Discontiguous_strategy = st.builds(
    prolog_directives_Discontiguous,
)
prolog_directives_Multifile_strategy = st.builds(
    prolog_directives_Multifile,
)
prolog_directives_Volatile_strategy = st.builds(
    prolog_directives_Volatile,
)
prolog_directives_Dynamic_strategy = st.builds(
    prolog_directives_Dynamic,
)
prolog_directives_Public_strategy = st.builds(
    prolog_directives_Public,
)
Term_strategy = st.builds(
    Term,
)
prolog_AtomicNumber_strategy = st.builds(
    prolog_AtomicNumber,
    value=
        st.integers()
)
ControlPredicate_strategy = st.builds(
    ControlPredicate,
)
prolog_False_strategy = st.builds(
    prolog_False,
)
prolog_Cut_strategy = st.builds(
    prolog_Cut,
)
prolog_Fail_strategy = st.builds(
    prolog_Fail,
)
prolog_True_strategy = st.builds(
    prolog_True,
)
prolog_ControlPredicate_strategy = st.builds(
    prolog_ControlPredicate,
)
prolog_List_strategy = st.builds(
    prolog_List,
)
prolog_AtomicQuotedString_strategy = st.builds(
    prolog_AtomicQuotedString,
    value=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
prolog_expressions_UnaryExpression_strategy = st.builds(
    prolog_expressions_UnaryExpression,
)
prolog_expressions_BinaryExpression_strategy = st.builds(
    prolog_expressions_BinaryExpression,
)
prolog_Term_strategy = st.builds(
    prolog_Term,
)
Clause_strategy = st.builds(
    Clause,
)
prolog_CompoundTerm_strategy = st.builds(
    prolog_CompoundTerm,
    value=
        safe_text
)
prolog_Rule_strategy = st.builds(
    prolog_Rule,
)
prolog_directives_Directive_strategy = st.builds(
    prolog_directives_Directive,
    name=
        safe_text
)
prolog_Fact_strategy = st.builds(
    prolog_Fact,
)
prolog_directives_Table_strategy = st.builds(
    prolog_directives_Table,
)
prolog_Comment_strategy = st.builds(
    prolog_Comment,
    value=
        safe_text
)
prolog_Clause_strategy = st.builds(
    prolog_Clause,
)
prolog_Program_strategy = st.builds(
    prolog_Program,
)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=prolog_expressions_BitwiseNegation_strategy)
@settings(max_examples=50)
def test_prolog_expressions_bitwisenegation_instantiation(instance):
    assert isinstance(instance, prolog_expressions_BitwiseNegation)

@given(instance=prolog_expressions_PositiveNumber_strategy)
@settings(max_examples=50)
def test_prolog_expressions_positivenumber_instantiation(instance):
    assert isinstance(instance, prolog_expressions_PositiveNumber)

@given(instance=prolog_expressions_NegativeNumber_strategy)
@settings(max_examples=50)
def test_prolog_expressions_negativenumber_instantiation(instance):
    assert isinstance(instance, prolog_expressions_NegativeNumber)

@given(instance=prolog_expressions_NotProvable_strategy)
@settings(max_examples=50)
def test_prolog_expressions_notprovable_instantiation(instance):
    assert isinstance(instance, prolog_expressions_NotProvable)

@given(instance=prolog_directives_PredicateIndicator_strategy)
@settings(max_examples=50)
def test_prolog_directives_predicateindicator_instantiation(instance):
    assert isinstance(instance, prolog_directives_PredicateIndicator)



@given(instance=prolog_directives_PredicateIndicator_strategy)
def test_prolog_directives_predicateindicator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=prolog_directives_PredicateIndicator_strategy)
def test_prolog_directives_predicateindicator_arity_setter(instance):
    original = instance.arity
    instance.arity = original
    assert instance.arity == original

@given(instance=PredicateIndicator_strategy)
@settings(max_examples=50)
def test_predicateindicator_instantiation(instance):
    assert isinstance(instance, PredicateIndicator)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=prolog_expressions_Xor_strategy)
@settings(max_examples=50)
def test_prolog_expressions_xor_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Xor)

@given(instance=prolog_expressions_StructuralEquivalence_strategy)
@settings(max_examples=50)
def test_prolog_expressions_structuralequivalence_instantiation(instance):
    assert isinstance(instance, prolog_expressions_StructuralEquivalence)

@given(instance=prolog_expressions_BinaryOr_strategy)
@settings(max_examples=50)
def test_prolog_expressions_binaryor_instantiation(instance):
    assert isinstance(instance, prolog_expressions_BinaryOr)

@given(instance=prolog_expressions_ParticalUnification_strategy)
@settings(max_examples=50)
def test_prolog_expressions_particalunification_instantiation(instance):
    assert isinstance(instance, prolog_expressions_ParticalUnification)

@given(instance=prolog_expressions_Unification_strategy)
@settings(max_examples=50)
def test_prolog_expressions_unification_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Unification)

@given(instance=prolog_expressions_Division_strategy)
@settings(max_examples=50)
def test_prolog_expressions_division_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Division)

@given(instance=prolog_expressions_Minus_strategy)
@settings(max_examples=50)
def test_prolog_expressions_minus_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Minus)

@given(instance=prolog_expressions_StandardOrderBefore_strategy)
@settings(max_examples=50)
def test_prolog_expressions_standardorderbefore_instantiation(instance):
    assert isinstance(instance, prolog_expressions_StandardOrderBefore)

@given(instance=prolog_expressions_Univ_strategy)
@settings(max_examples=50)
def test_prolog_expressions_univ_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Univ)

@given(instance=prolog_expressions_GreaterThan_strategy)
@settings(max_examples=50)
def test_prolog_expressions_greaterthan_instantiation(instance):
    assert isinstance(instance, prolog_expressions_GreaterThan)

@given(instance=prolog_expressions_Div_strategy)
@settings(max_examples=50)
def test_prolog_expressions_div_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Div)

@given(instance=prolog_expressions_Equivalence_strategy)
@settings(max_examples=50)
def test_prolog_expressions_equivalence_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Equivalence)

@given(instance=prolog_expressions_GreaterOrEqual_strategy)
@settings(max_examples=50)
def test_prolog_expressions_greaterorequal_instantiation(instance):
    assert isinstance(instance, prolog_expressions_GreaterOrEqual)

@given(instance=prolog_expressions_SoftCut_strategy)
@settings(max_examples=50)
def test_prolog_expressions_softcut_instantiation(instance):
    assert isinstance(instance, prolog_expressions_SoftCut)

@given(instance=prolog_expressions_BinaryAnd_strategy)
@settings(max_examples=50)
def test_prolog_expressions_binaryand_instantiation(instance):
    assert isinstance(instance, prolog_expressions_BinaryAnd)

@given(instance=prolog_expressions_LogicalAnd_strategy)
@settings(max_examples=50)
def test_prolog_expressions_logicaland_instantiation(instance):
    assert isinstance(instance, prolog_expressions_LogicalAnd)

@given(instance=prolog_expressions_EqualOrStandardOrderAfter_strategy)
@settings(max_examples=50)
def test_prolog_expressions_equalorstandardorderafter_instantiation(instance):
    assert isinstance(instance, prolog_expressions_EqualOrStandardOrderAfter)

@given(instance=prolog_expressions_Rem_strategy)
@settings(max_examples=50)
def test_prolog_expressions_rem_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Rem)

@given(instance=prolog_expressions_LessThan_strategy)
@settings(max_examples=50)
def test_prolog_expressions_lessthan_instantiation(instance):
    assert isinstance(instance, prolog_expressions_LessThan)

@given(instance=prolog_expressions_IntegerDivision_strategy)
@settings(max_examples=50)
def test_prolog_expressions_integerdivision_instantiation(instance):
    assert isinstance(instance, prolog_expressions_IntegerDivision)

@given(instance=prolog_expressions_Power_strategy)
@settings(max_examples=50)
def test_prolog_expressions_power_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Power)

@given(instance=prolog_expressions_Mod_strategy)
@settings(max_examples=50)
def test_prolog_expressions_mod_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Mod)

@given(instance=prolog_expressions_Is_strategy)
@settings(max_examples=50)
def test_prolog_expressions_is_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Is)

@given(instance=prolog_expressions_NonEqualNumber_strategy)
@settings(max_examples=50)
def test_prolog_expressions_nonequalnumber_instantiation(instance):
    assert isinstance(instance, prolog_expressions_NonEqualNumber)

@given(instance=prolog_expressions_StructuralEquivalenceNotProvable_strategy)
@settings(max_examples=50)
def test_prolog_expressions_structuralequivalencenotprovable_instantiation(instance):
    assert isinstance(instance, prolog_expressions_StructuralEquivalenceNotProvable)

@given(instance=prolog_expressions_Multiplication_strategy)
@settings(max_examples=50)
def test_prolog_expressions_multiplication_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Multiplication)

@given(instance=prolog_expressions_ModuleCall_strategy)
@settings(max_examples=50)
def test_prolog_expressions_modulecall_instantiation(instance):
    assert isinstance(instance, prolog_expressions_ModuleCall)

@given(instance=prolog_expressions_LessOrEqual_strategy)
@settings(max_examples=50)
def test_prolog_expressions_lessorequal_instantiation(instance):
    assert isinstance(instance, prolog_expressions_LessOrEqual)

@given(instance=prolog_expressions_BitwiseShiftLeft_strategy)
@settings(max_examples=50)
def test_prolog_expressions_bitwiseshiftleft_instantiation(instance):
    assert isinstance(instance, prolog_expressions_BitwiseShiftLeft)

@given(instance=prolog_expressions_StandardOrderAfter_strategy)
@settings(max_examples=50)
def test_prolog_expressions_standardorderafter_instantiation(instance):
    assert isinstance(instance, prolog_expressions_StandardOrderAfter)

@given(instance=prolog_expressions_Plus_strategy)
@settings(max_examples=50)
def test_prolog_expressions_plus_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Plus)

@given(instance=prolog_expressions_NotUnifiable_strategy)
@settings(max_examples=50)
def test_prolog_expressions_notunifiable_instantiation(instance):
    assert isinstance(instance, prolog_expressions_NotUnifiable)

@given(instance=prolog_expressions_EqualOrStandardOrderBefore_strategy)
@settings(max_examples=50)
def test_prolog_expressions_equalorstandardorderbefore_instantiation(instance):
    assert isinstance(instance, prolog_expressions_EqualOrStandardOrderBefore)

@given(instance=prolog_expressions_Rdiv_strategy)
@settings(max_examples=50)
def test_prolog_expressions_rdiv_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Rdiv)

@given(instance=prolog_expressions_SubDict_strategy)
@settings(max_examples=50)
def test_prolog_expressions_subdict_instantiation(instance):
    assert isinstance(instance, prolog_expressions_SubDict)

@given(instance=prolog_expressions_As_strategy)
@settings(max_examples=50)
def test_prolog_expressions_as_instantiation(instance):
    assert isinstance(instance, prolog_expressions_As)

@given(instance=prolog_expressions_Disequality_strategy)
@settings(max_examples=50)
def test_prolog_expressions_disequality_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Disequality)

@given(instance=prolog_expressions_Condition_strategy)
@settings(max_examples=50)
def test_prolog_expressions_condition_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Condition)

@given(instance=prolog_expressions_NumberEqual_strategy)
@settings(max_examples=50)
def test_prolog_expressions_numberequal_instantiation(instance):
    assert isinstance(instance, prolog_expressions_NumberEqual)

@given(instance=prolog_expressions_LogicalOr_strategy)
@settings(max_examples=50)
def test_prolog_expressions_logicalor_instantiation(instance):
    assert isinstance(instance, prolog_expressions_LogicalOr)

@given(instance=prolog_expressions_Expression_strategy)
@settings(max_examples=50)
def test_prolog_expressions_expression_instantiation(instance):
    assert isinstance(instance, prolog_expressions_Expression)

@given(instance=Directive_strategy)
@settings(max_examples=50)
def test_directive_instantiation(instance):
    assert isinstance(instance, Directive)

@given(instance=prolog_directives_Discontiguous_strategy)
@settings(max_examples=50)
def test_prolog_directives_discontiguous_instantiation(instance):
    assert isinstance(instance, prolog_directives_Discontiguous)

@given(instance=prolog_directives_Multifile_strategy)
@settings(max_examples=50)
def test_prolog_directives_multifile_instantiation(instance):
    assert isinstance(instance, prolog_directives_Multifile)

@given(instance=prolog_directives_Volatile_strategy)
@settings(max_examples=50)
def test_prolog_directives_volatile_instantiation(instance):
    assert isinstance(instance, prolog_directives_Volatile)

@given(instance=prolog_directives_Dynamic_strategy)
@settings(max_examples=50)
def test_prolog_directives_dynamic_instantiation(instance):
    assert isinstance(instance, prolog_directives_Dynamic)

@given(instance=prolog_directives_Public_strategy)
@settings(max_examples=50)
def test_prolog_directives_public_instantiation(instance):
    assert isinstance(instance, prolog_directives_Public)

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=prolog_AtomicNumber_strategy)
@settings(max_examples=50)
def test_prolog_atomicnumber_instantiation(instance):
    assert isinstance(instance, prolog_AtomicNumber)



@given(instance=prolog_AtomicNumber_strategy)
def test_prolog_atomicnumber_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ControlPredicate_strategy)
@settings(max_examples=50)
def test_controlpredicate_instantiation(instance):
    assert isinstance(instance, ControlPredicate)

@given(instance=prolog_False_strategy)
@settings(max_examples=50)
def test_prolog_false_instantiation(instance):
    assert isinstance(instance, prolog_False)

@given(instance=prolog_Cut_strategy)
@settings(max_examples=50)
def test_prolog_cut_instantiation(instance):
    assert isinstance(instance, prolog_Cut)

@given(instance=prolog_Fail_strategy)
@settings(max_examples=50)
def test_prolog_fail_instantiation(instance):
    assert isinstance(instance, prolog_Fail)

@given(instance=prolog_True_strategy)
@settings(max_examples=50)
def test_prolog_true_instantiation(instance):
    assert isinstance(instance, prolog_True)

@given(instance=prolog_ControlPredicate_strategy)
@settings(max_examples=50)
def test_prolog_controlpredicate_instantiation(instance):
    assert isinstance(instance, prolog_ControlPredicate)

@given(instance=prolog_List_strategy)
@settings(max_examples=50)
def test_prolog_list_instantiation(instance):
    assert isinstance(instance, prolog_List)

@given(instance=prolog_AtomicQuotedString_strategy)
@settings(max_examples=50)
def test_prolog_atomicquotedstring_instantiation(instance):
    assert isinstance(instance, prolog_AtomicQuotedString)



@given(instance=prolog_AtomicQuotedString_strategy)
def test_prolog_atomicquotedstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=prolog_expressions_UnaryExpression_strategy)
@settings(max_examples=50)
def test_prolog_expressions_unaryexpression_instantiation(instance):
    assert isinstance(instance, prolog_expressions_UnaryExpression)

@given(instance=prolog_expressions_BinaryExpression_strategy)
@settings(max_examples=50)
def test_prolog_expressions_binaryexpression_instantiation(instance):
    assert isinstance(instance, prolog_expressions_BinaryExpression)

@given(instance=prolog_Term_strategy)
@settings(max_examples=50)
def test_prolog_term_instantiation(instance):
    assert isinstance(instance, prolog_Term)

@given(instance=Clause_strategy)
@settings(max_examples=50)
def test_clause_instantiation(instance):
    assert isinstance(instance, Clause)

@given(instance=prolog_CompoundTerm_strategy)
@settings(max_examples=50)
def test_prolog_compoundterm_instantiation(instance):
    assert isinstance(instance, prolog_CompoundTerm)



@given(instance=prolog_CompoundTerm_strategy)
def test_prolog_compoundterm_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=prolog_Rule_strategy)
@settings(max_examples=50)
def test_prolog_rule_instantiation(instance):
    assert isinstance(instance, prolog_Rule)

@given(instance=prolog_directives_Directive_strategy)
@settings(max_examples=50)
def test_prolog_directives_directive_instantiation(instance):
    assert isinstance(instance, prolog_directives_Directive)



@given(instance=prolog_directives_Directive_strategy)
def test_prolog_directives_directive_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prolog_Fact_strategy)
@settings(max_examples=50)
def test_prolog_fact_instantiation(instance):
    assert isinstance(instance, prolog_Fact)

@given(instance=prolog_directives_Table_strategy)
@settings(max_examples=50)
def test_prolog_directives_table_instantiation(instance):
    assert isinstance(instance, prolog_directives_Table)

@given(instance=prolog_Comment_strategy)
@settings(max_examples=50)
def test_prolog_comment_instantiation(instance):
    assert isinstance(instance, prolog_Comment)



@given(instance=prolog_Comment_strategy)
def test_prolog_comment_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=prolog_Clause_strategy)
@settings(max_examples=50)
def test_prolog_clause_instantiation(instance):
    assert isinstance(instance, prolog_Clause)

@given(instance=prolog_Program_strategy)
@settings(max_examples=50)
def test_prolog_program_instantiation(instance):
    assert isinstance(instance, prolog_Program)
