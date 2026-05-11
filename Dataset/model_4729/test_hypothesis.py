import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UnaryExpression,
    prolog::expressions::NegativeNumber,
    prolog::expressions::BitwiseNegation,
    prolog::expressions::PositiveNumber,
    prolog::expressions::NotProvable,
    prolog::directives::PredicateIndicator,
    PredicateIndicator,
    BinaryExpression,
    prolog::expressions::NumberEqual,
    prolog::expressions::GreaterThan,
    prolog::expressions::Division,
    prolog::expressions::Disequality,
    prolog::expressions::EqualOrStandardOrderAfter,
    prolog::expressions::SubDict,
    prolog::expressions::ModuleCall,
    prolog::expressions::NonEqualNumber,
    prolog::expressions::Rem,
    prolog::expressions::BinaryOr,
    prolog::expressions::Mod,
    prolog::expressions::Minus,
    prolog::expressions::Equivalence,
    prolog::expressions::Condition,
    prolog::expressions::Rdiv,
    prolog::expressions::ParticalUnification,
    prolog::expressions::Univ,
    prolog::expressions::BinaryAnd,
    prolog::expressions::EqualOrStandardOrderBefore,
    prolog::expressions::Plus,
    prolog::expressions::Xor,
    prolog::expressions::StandardOrderBefore,
    prolog::expressions::StructuralEquivalenceNotProvable,
    prolog::expressions::NotUnifiable,
    prolog::expressions::IntegerDivision,
    prolog::expressions::As,
    prolog::expressions::StructuralEquivalence,
    prolog::expressions::BitwiseShiftLeft,
    prolog::expressions::LessOrEqual,
    prolog::expressions::LogicalAnd,
    prolog::expressions::Power,
    prolog::expressions::Is,
    prolog::expressions::StandardOrderAfter,
    prolog::expressions::SoftCut,
    prolog::expressions::Multiplication,
    prolog::expressions::Div,
    prolog::expressions::LessThan,
    prolog::expressions::Unification,
    prolog::expressions::GreaterOrEqual,
    prolog::expressions::LogicalOr,
    prolog::expressions::Expression,
    Directive,
    prolog::directives::Public,
    prolog::directives::Volatile,
    prolog::directives::Dynamic,
    prolog::directives::Multifile,
    prolog::directives::Discontiguous,
    Term,
    prolog::AtomicNumber,
    ControlPredicate,
    prolog::Cut,
    prolog::Fail,
    prolog::False,
    prolog::True,
    prolog::ControlPredicate,
    prolog::List,
    prolog::AtomicQuotedString,
    Expression,
    prolog::expressions::UnaryExpression,
    prolog::expressions::BinaryExpression,
    prolog::Term,
    Clause,
    prolog::Fact,
    prolog::directives::Table,
    prolog::Rule,
    prolog::directives::Directive,
    prolog::CompoundTerm,
    prolog::Comment,
    prolog::Clause,
    prolog::Program,
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



def test_prolog::expressions::negativenumber_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::NegativeNumber)


def test_prolog::expressions::negativenumber_constructor_exists():
    assert callable(prolog::expressions::NegativeNumber.__init__)


def test_prolog::expressions::negativenumber_constructor_args():
    sig = inspect.signature(prolog::expressions::NegativeNumber.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::bitwisenegation_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::BitwiseNegation)


def test_prolog::expressions::bitwisenegation_constructor_exists():
    assert callable(prolog::expressions::BitwiseNegation.__init__)


def test_prolog::expressions::bitwisenegation_constructor_args():
    sig = inspect.signature(prolog::expressions::BitwiseNegation.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::positivenumber_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::PositiveNumber)


def test_prolog::expressions::positivenumber_constructor_exists():
    assert callable(prolog::expressions::PositiveNumber.__init__)


def test_prolog::expressions::positivenumber_constructor_args():
    sig = inspect.signature(prolog::expressions::PositiveNumber.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::notprovable_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::NotProvable)


def test_prolog::expressions::notprovable_constructor_exists():
    assert callable(prolog::expressions::NotProvable.__init__)


def test_prolog::expressions::notprovable_constructor_args():
    sig = inspect.signature(prolog::expressions::NotProvable.__init__)
    params = list(sig.parameters.keys())



def test_prolog::directives::predicateindicator_is_not_abstract():
    assert not inspect.isabstract(prolog::directives::PredicateIndicator)


def test_prolog::directives::predicateindicator_constructor_exists():
    assert callable(prolog::directives::PredicateIndicator.__init__)


def test_prolog::directives::predicateindicator_constructor_args():
    sig = inspect.signature(prolog::directives::PredicateIndicator.__init__)
    params = list(sig.parameters.keys())
    assert "arity" in params, "Missing parameter 'arity'"
    assert "name" in params, "Missing parameter 'name'"

def test_prolog::directives::predicateindicator_has_arity():
    assert hasattr(prolog::directives::PredicateIndicator, "arity")
    descriptor = None
    for klass in prolog::directives::PredicateIndicator.__mro__:
        if "arity" in klass.__dict__:
            descriptor = klass.__dict__["arity"]
            break
    assert isinstance(descriptor, property)

def test_prolog::directives::predicateindicator_has_name():
    assert hasattr(prolog::directives::PredicateIndicator, "name")
    descriptor = None
    for klass in prolog::directives::PredicateIndicator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_prolog::expressions::numberequal_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::NumberEqual)


def test_prolog::expressions::numberequal_constructor_exists():
    assert callable(prolog::expressions::NumberEqual.__init__)


def test_prolog::expressions::numberequal_constructor_args():
    sig = inspect.signature(prolog::expressions::NumberEqual.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::greaterthan_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::GreaterThan)


def test_prolog::expressions::greaterthan_constructor_exists():
    assert callable(prolog::expressions::GreaterThan.__init__)


def test_prolog::expressions::greaterthan_constructor_args():
    sig = inspect.signature(prolog::expressions::GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::division_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Division)


def test_prolog::expressions::division_constructor_exists():
    assert callable(prolog::expressions::Division.__init__)


def test_prolog::expressions::division_constructor_args():
    sig = inspect.signature(prolog::expressions::Division.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::disequality_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Disequality)


def test_prolog::expressions::disequality_constructor_exists():
    assert callable(prolog::expressions::Disequality.__init__)


def test_prolog::expressions::disequality_constructor_args():
    sig = inspect.signature(prolog::expressions::Disequality.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::equalorstandardorderafter_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::EqualOrStandardOrderAfter)


def test_prolog::expressions::equalorstandardorderafter_constructor_exists():
    assert callable(prolog::expressions::EqualOrStandardOrderAfter.__init__)


def test_prolog::expressions::equalorstandardorderafter_constructor_args():
    sig = inspect.signature(prolog::expressions::EqualOrStandardOrderAfter.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::subdict_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::SubDict)


def test_prolog::expressions::subdict_constructor_exists():
    assert callable(prolog::expressions::SubDict.__init__)


def test_prolog::expressions::subdict_constructor_args():
    sig = inspect.signature(prolog::expressions::SubDict.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::modulecall_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::ModuleCall)


def test_prolog::expressions::modulecall_constructor_exists():
    assert callable(prolog::expressions::ModuleCall.__init__)


def test_prolog::expressions::modulecall_constructor_args():
    sig = inspect.signature(prolog::expressions::ModuleCall.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::nonequalnumber_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::NonEqualNumber)


def test_prolog::expressions::nonequalnumber_constructor_exists():
    assert callable(prolog::expressions::NonEqualNumber.__init__)


def test_prolog::expressions::nonequalnumber_constructor_args():
    sig = inspect.signature(prolog::expressions::NonEqualNumber.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::rem_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Rem)


def test_prolog::expressions::rem_constructor_exists():
    assert callable(prolog::expressions::Rem.__init__)


def test_prolog::expressions::rem_constructor_args():
    sig = inspect.signature(prolog::expressions::Rem.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::binaryor_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::BinaryOr)


def test_prolog::expressions::binaryor_constructor_exists():
    assert callable(prolog::expressions::BinaryOr.__init__)


def test_prolog::expressions::binaryor_constructor_args():
    sig = inspect.signature(prolog::expressions::BinaryOr.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::mod_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Mod)


def test_prolog::expressions::mod_constructor_exists():
    assert callable(prolog::expressions::Mod.__init__)


def test_prolog::expressions::mod_constructor_args():
    sig = inspect.signature(prolog::expressions::Mod.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::minus_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Minus)


def test_prolog::expressions::minus_constructor_exists():
    assert callable(prolog::expressions::Minus.__init__)


def test_prolog::expressions::minus_constructor_args():
    sig = inspect.signature(prolog::expressions::Minus.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::equivalence_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Equivalence)


def test_prolog::expressions::equivalence_constructor_exists():
    assert callable(prolog::expressions::Equivalence.__init__)


def test_prolog::expressions::equivalence_constructor_args():
    sig = inspect.signature(prolog::expressions::Equivalence.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::condition_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Condition)


def test_prolog::expressions::condition_constructor_exists():
    assert callable(prolog::expressions::Condition.__init__)


def test_prolog::expressions::condition_constructor_args():
    sig = inspect.signature(prolog::expressions::Condition.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::rdiv_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Rdiv)


def test_prolog::expressions::rdiv_constructor_exists():
    assert callable(prolog::expressions::Rdiv.__init__)


def test_prolog::expressions::rdiv_constructor_args():
    sig = inspect.signature(prolog::expressions::Rdiv.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::particalunification_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::ParticalUnification)


def test_prolog::expressions::particalunification_constructor_exists():
    assert callable(prolog::expressions::ParticalUnification.__init__)


def test_prolog::expressions::particalunification_constructor_args():
    sig = inspect.signature(prolog::expressions::ParticalUnification.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::univ_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Univ)


def test_prolog::expressions::univ_constructor_exists():
    assert callable(prolog::expressions::Univ.__init__)


def test_prolog::expressions::univ_constructor_args():
    sig = inspect.signature(prolog::expressions::Univ.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::binaryand_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::BinaryAnd)


def test_prolog::expressions::binaryand_constructor_exists():
    assert callable(prolog::expressions::BinaryAnd.__init__)


def test_prolog::expressions::binaryand_constructor_args():
    sig = inspect.signature(prolog::expressions::BinaryAnd.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::equalorstandardorderbefore_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::EqualOrStandardOrderBefore)


def test_prolog::expressions::equalorstandardorderbefore_constructor_exists():
    assert callable(prolog::expressions::EqualOrStandardOrderBefore.__init__)


def test_prolog::expressions::equalorstandardorderbefore_constructor_args():
    sig = inspect.signature(prolog::expressions::EqualOrStandardOrderBefore.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::plus_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Plus)


def test_prolog::expressions::plus_constructor_exists():
    assert callable(prolog::expressions::Plus.__init__)


def test_prolog::expressions::plus_constructor_args():
    sig = inspect.signature(prolog::expressions::Plus.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::xor_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Xor)


def test_prolog::expressions::xor_constructor_exists():
    assert callable(prolog::expressions::Xor.__init__)


def test_prolog::expressions::xor_constructor_args():
    sig = inspect.signature(prolog::expressions::Xor.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::standardorderbefore_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::StandardOrderBefore)


def test_prolog::expressions::standardorderbefore_constructor_exists():
    assert callable(prolog::expressions::StandardOrderBefore.__init__)


def test_prolog::expressions::standardorderbefore_constructor_args():
    sig = inspect.signature(prolog::expressions::StandardOrderBefore.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::structuralequivalencenotprovable_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::StructuralEquivalenceNotProvable)


def test_prolog::expressions::structuralequivalencenotprovable_constructor_exists():
    assert callable(prolog::expressions::StructuralEquivalenceNotProvable.__init__)


def test_prolog::expressions::structuralequivalencenotprovable_constructor_args():
    sig = inspect.signature(prolog::expressions::StructuralEquivalenceNotProvable.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::notunifiable_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::NotUnifiable)


def test_prolog::expressions::notunifiable_constructor_exists():
    assert callable(prolog::expressions::NotUnifiable.__init__)


def test_prolog::expressions::notunifiable_constructor_args():
    sig = inspect.signature(prolog::expressions::NotUnifiable.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::integerdivision_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::IntegerDivision)


def test_prolog::expressions::integerdivision_constructor_exists():
    assert callable(prolog::expressions::IntegerDivision.__init__)


def test_prolog::expressions::integerdivision_constructor_args():
    sig = inspect.signature(prolog::expressions::IntegerDivision.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::as_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::As)


def test_prolog::expressions::as_constructor_exists():
    assert callable(prolog::expressions::As.__init__)


def test_prolog::expressions::as_constructor_args():
    sig = inspect.signature(prolog::expressions::As.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::structuralequivalence_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::StructuralEquivalence)


def test_prolog::expressions::structuralequivalence_constructor_exists():
    assert callable(prolog::expressions::StructuralEquivalence.__init__)


def test_prolog::expressions::structuralequivalence_constructor_args():
    sig = inspect.signature(prolog::expressions::StructuralEquivalence.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::bitwiseshiftleft_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::BitwiseShiftLeft)


def test_prolog::expressions::bitwiseshiftleft_constructor_exists():
    assert callable(prolog::expressions::BitwiseShiftLeft.__init__)


def test_prolog::expressions::bitwiseshiftleft_constructor_args():
    sig = inspect.signature(prolog::expressions::BitwiseShiftLeft.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::lessorequal_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::LessOrEqual)


def test_prolog::expressions::lessorequal_constructor_exists():
    assert callable(prolog::expressions::LessOrEqual.__init__)


def test_prolog::expressions::lessorequal_constructor_args():
    sig = inspect.signature(prolog::expressions::LessOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::logicaland_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::LogicalAnd)


def test_prolog::expressions::logicaland_constructor_exists():
    assert callable(prolog::expressions::LogicalAnd.__init__)


def test_prolog::expressions::logicaland_constructor_args():
    sig = inspect.signature(prolog::expressions::LogicalAnd.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::power_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Power)


def test_prolog::expressions::power_constructor_exists():
    assert callable(prolog::expressions::Power.__init__)


def test_prolog::expressions::power_constructor_args():
    sig = inspect.signature(prolog::expressions::Power.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::is_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Is)


def test_prolog::expressions::is_constructor_exists():
    assert callable(prolog::expressions::Is.__init__)


def test_prolog::expressions::is_constructor_args():
    sig = inspect.signature(prolog::expressions::Is.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::standardorderafter_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::StandardOrderAfter)


def test_prolog::expressions::standardorderafter_constructor_exists():
    assert callable(prolog::expressions::StandardOrderAfter.__init__)


def test_prolog::expressions::standardorderafter_constructor_args():
    sig = inspect.signature(prolog::expressions::StandardOrderAfter.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::softcut_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::SoftCut)


def test_prolog::expressions::softcut_constructor_exists():
    assert callable(prolog::expressions::SoftCut.__init__)


def test_prolog::expressions::softcut_constructor_args():
    sig = inspect.signature(prolog::expressions::SoftCut.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::multiplication_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Multiplication)


def test_prolog::expressions::multiplication_constructor_exists():
    assert callable(prolog::expressions::Multiplication.__init__)


def test_prolog::expressions::multiplication_constructor_args():
    sig = inspect.signature(prolog::expressions::Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::div_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Div)


def test_prolog::expressions::div_constructor_exists():
    assert callable(prolog::expressions::Div.__init__)


def test_prolog::expressions::div_constructor_args():
    sig = inspect.signature(prolog::expressions::Div.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::lessthan_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::LessThan)


def test_prolog::expressions::lessthan_constructor_exists():
    assert callable(prolog::expressions::LessThan.__init__)


def test_prolog::expressions::lessthan_constructor_args():
    sig = inspect.signature(prolog::expressions::LessThan.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::unification_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Unification)


def test_prolog::expressions::unification_constructor_exists():
    assert callable(prolog::expressions::Unification.__init__)


def test_prolog::expressions::unification_constructor_args():
    sig = inspect.signature(prolog::expressions::Unification.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::greaterorequal_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::GreaterOrEqual)


def test_prolog::expressions::greaterorequal_constructor_exists():
    assert callable(prolog::expressions::GreaterOrEqual.__init__)


def test_prolog::expressions::greaterorequal_constructor_args():
    sig = inspect.signature(prolog::expressions::GreaterOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::logicalor_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::LogicalOr)


def test_prolog::expressions::logicalor_constructor_exists():
    assert callable(prolog::expressions::LogicalOr.__init__)


def test_prolog::expressions::logicalor_constructor_args():
    sig = inspect.signature(prolog::expressions::LogicalOr.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::expression_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::Expression)


def test_prolog::expressions::expression_constructor_exists():
    assert callable(prolog::expressions::Expression.__init__)


def test_prolog::expressions::expression_constructor_args():
    sig = inspect.signature(prolog::expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_directive_is_not_abstract():
    assert not inspect.isabstract(Directive)


def test_directive_constructor_exists():
    assert callable(Directive.__init__)


def test_directive_constructor_args():
    sig = inspect.signature(Directive.__init__)
    params = list(sig.parameters.keys())



def test_prolog::directives::public_is_not_abstract():
    assert not inspect.isabstract(prolog::directives::Public)


def test_prolog::directives::public_constructor_exists():
    assert callable(prolog::directives::Public.__init__)


def test_prolog::directives::public_constructor_args():
    sig = inspect.signature(prolog::directives::Public.__init__)
    params = list(sig.parameters.keys())



def test_prolog::directives::volatile_is_not_abstract():
    assert not inspect.isabstract(prolog::directives::Volatile)


def test_prolog::directives::volatile_constructor_exists():
    assert callable(prolog::directives::Volatile.__init__)


def test_prolog::directives::volatile_constructor_args():
    sig = inspect.signature(prolog::directives::Volatile.__init__)
    params = list(sig.parameters.keys())



def test_prolog::directives::dynamic_is_not_abstract():
    assert not inspect.isabstract(prolog::directives::Dynamic)


def test_prolog::directives::dynamic_constructor_exists():
    assert callable(prolog::directives::Dynamic.__init__)


def test_prolog::directives::dynamic_constructor_args():
    sig = inspect.signature(prolog::directives::Dynamic.__init__)
    params = list(sig.parameters.keys())



def test_prolog::directives::multifile_is_not_abstract():
    assert not inspect.isabstract(prolog::directives::Multifile)


def test_prolog::directives::multifile_constructor_exists():
    assert callable(prolog::directives::Multifile.__init__)


def test_prolog::directives::multifile_constructor_args():
    sig = inspect.signature(prolog::directives::Multifile.__init__)
    params = list(sig.parameters.keys())



def test_prolog::directives::discontiguous_is_not_abstract():
    assert not inspect.isabstract(prolog::directives::Discontiguous)


def test_prolog::directives::discontiguous_constructor_exists():
    assert callable(prolog::directives::Discontiguous.__init__)


def test_prolog::directives::discontiguous_constructor_args():
    sig = inspect.signature(prolog::directives::Discontiguous.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_prolog::atomicnumber_is_not_abstract():
    assert not inspect.isabstract(prolog::AtomicNumber)


def test_prolog::atomicnumber_constructor_exists():
    assert callable(prolog::AtomicNumber.__init__)


def test_prolog::atomicnumber_constructor_args():
    sig = inspect.signature(prolog::AtomicNumber.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_prolog::atomicnumber_has_value():
    assert hasattr(prolog::AtomicNumber, "value")
    descriptor = None
    for klass in prolog::AtomicNumber.__mro__:
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



def test_prolog::cut_is_not_abstract():
    assert not inspect.isabstract(prolog::Cut)


def test_prolog::cut_constructor_exists():
    assert callable(prolog::Cut.__init__)


def test_prolog::cut_constructor_args():
    sig = inspect.signature(prolog::Cut.__init__)
    params = list(sig.parameters.keys())



def test_prolog::fail_is_not_abstract():
    assert not inspect.isabstract(prolog::Fail)


def test_prolog::fail_constructor_exists():
    assert callable(prolog::Fail.__init__)


def test_prolog::fail_constructor_args():
    sig = inspect.signature(prolog::Fail.__init__)
    params = list(sig.parameters.keys())



def test_prolog::false_is_not_abstract():
    assert not inspect.isabstract(prolog::False)


def test_prolog::false_constructor_exists():
    assert callable(prolog::False.__init__)


def test_prolog::false_constructor_args():
    sig = inspect.signature(prolog::False.__init__)
    params = list(sig.parameters.keys())



def test_prolog::true_is_not_abstract():
    assert not inspect.isabstract(prolog::True)


def test_prolog::true_constructor_exists():
    assert callable(prolog::True.__init__)


def test_prolog::true_constructor_args():
    sig = inspect.signature(prolog::True.__init__)
    params = list(sig.parameters.keys())



def test_prolog::controlpredicate_is_not_abstract():
    assert not inspect.isabstract(prolog::ControlPredicate)


def test_prolog::controlpredicate_constructor_exists():
    assert callable(prolog::ControlPredicate.__init__)


def test_prolog::controlpredicate_constructor_args():
    sig = inspect.signature(prolog::ControlPredicate.__init__)
    params = list(sig.parameters.keys())



def test_prolog::list_is_not_abstract():
    assert not inspect.isabstract(prolog::List)


def test_prolog::list_constructor_exists():
    assert callable(prolog::List.__init__)


def test_prolog::list_constructor_args():
    sig = inspect.signature(prolog::List.__init__)
    params = list(sig.parameters.keys())



def test_prolog::atomicquotedstring_is_not_abstract():
    assert not inspect.isabstract(prolog::AtomicQuotedString)


def test_prolog::atomicquotedstring_constructor_exists():
    assert callable(prolog::AtomicQuotedString.__init__)


def test_prolog::atomicquotedstring_constructor_args():
    sig = inspect.signature(prolog::AtomicQuotedString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_prolog::atomicquotedstring_has_value():
    assert hasattr(prolog::AtomicQuotedString, "value")
    descriptor = None
    for klass in prolog::AtomicQuotedString.__mro__:
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



def test_prolog::expressions::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::UnaryExpression)


def test_prolog::expressions::unaryexpression_constructor_exists():
    assert callable(prolog::expressions::UnaryExpression.__init__)


def test_prolog::expressions::unaryexpression_constructor_args():
    sig = inspect.signature(prolog::expressions::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_prolog::expressions::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(prolog::expressions::BinaryExpression)


def test_prolog::expressions::binaryexpression_constructor_exists():
    assert callable(prolog::expressions::BinaryExpression.__init__)


def test_prolog::expressions::binaryexpression_constructor_args():
    sig = inspect.signature(prolog::expressions::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_prolog::term_is_not_abstract():
    assert not inspect.isabstract(prolog::Term)


def test_prolog::term_constructor_exists():
    assert callable(prolog::Term.__init__)


def test_prolog::term_constructor_args():
    sig = inspect.signature(prolog::Term.__init__)
    params = list(sig.parameters.keys())



def test_clause_is_not_abstract():
    assert not inspect.isabstract(Clause)


def test_clause_constructor_exists():
    assert callable(Clause.__init__)


def test_clause_constructor_args():
    sig = inspect.signature(Clause.__init__)
    params = list(sig.parameters.keys())



def test_prolog::fact_is_not_abstract():
    assert not inspect.isabstract(prolog::Fact)


def test_prolog::fact_constructor_exists():
    assert callable(prolog::Fact.__init__)


def test_prolog::fact_constructor_args():
    sig = inspect.signature(prolog::Fact.__init__)
    params = list(sig.parameters.keys())



def test_prolog::directives::table_is_not_abstract():
    assert not inspect.isabstract(prolog::directives::Table)


def test_prolog::directives::table_constructor_exists():
    assert callable(prolog::directives::Table.__init__)


def test_prolog::directives::table_constructor_args():
    sig = inspect.signature(prolog::directives::Table.__init__)
    params = list(sig.parameters.keys())



def test_prolog::rule_is_not_abstract():
    assert not inspect.isabstract(prolog::Rule)


def test_prolog::rule_constructor_exists():
    assert callable(prolog::Rule.__init__)


def test_prolog::rule_constructor_args():
    sig = inspect.signature(prolog::Rule.__init__)
    params = list(sig.parameters.keys())



def test_prolog::directives::directive_is_not_abstract():
    assert not inspect.isabstract(prolog::directives::Directive)


def test_prolog::directives::directive_constructor_exists():
    assert callable(prolog::directives::Directive.__init__)


def test_prolog::directives::directive_constructor_args():
    sig = inspect.signature(prolog::directives::Directive.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_prolog::directives::directive_has_name():
    assert hasattr(prolog::directives::Directive, "name")
    descriptor = None
    for klass in prolog::directives::Directive.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prolog::compoundterm_is_not_abstract():
    assert not inspect.isabstract(prolog::CompoundTerm)


def test_prolog::compoundterm_constructor_exists():
    assert callable(prolog::CompoundTerm.__init__)


def test_prolog::compoundterm_constructor_args():
    sig = inspect.signature(prolog::CompoundTerm.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_prolog::compoundterm_has_value():
    assert hasattr(prolog::CompoundTerm, "value")
    descriptor = None
    for klass in prolog::CompoundTerm.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_prolog::comment_is_not_abstract():
    assert not inspect.isabstract(prolog::Comment)


def test_prolog::comment_constructor_exists():
    assert callable(prolog::Comment.__init__)


def test_prolog::comment_constructor_args():
    sig = inspect.signature(prolog::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_prolog::comment_has_value():
    assert hasattr(prolog::Comment, "value")
    descriptor = None
    for klass in prolog::Comment.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_prolog::clause_is_not_abstract():
    assert not inspect.isabstract(prolog::Clause)


def test_prolog::clause_constructor_exists():
    assert callable(prolog::Clause.__init__)


def test_prolog::clause_constructor_args():
    sig = inspect.signature(prolog::Clause.__init__)
    params = list(sig.parameters.keys())



def test_prolog::program_is_not_abstract():
    assert not inspect.isabstract(prolog::Program)


def test_prolog::program_constructor_exists():
    assert callable(prolog::Program.__init__)


def test_prolog::program_constructor_args():
    sig = inspect.signature(prolog::Program.__init__)
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
prolog::expressions::NegativeNumber_strategy = st.builds(
    prolog::expressions::NegativeNumber,
)
prolog::expressions::BitwiseNegation_strategy = st.builds(
    prolog::expressions::BitwiseNegation,
)
prolog::expressions::PositiveNumber_strategy = st.builds(
    prolog::expressions::PositiveNumber,
)
prolog::expressions::NotProvable_strategy = st.builds(
    prolog::expressions::NotProvable,
)
prolog::directives::PredicateIndicator_strategy = st.builds(
    prolog::directives::PredicateIndicator,
    arity=
        st.integers(),
    name=
        safe_text
)
PredicateIndicator_strategy = st.builds(
    PredicateIndicator,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
prolog::expressions::NumberEqual_strategy = st.builds(
    prolog::expressions::NumberEqual,
)
prolog::expressions::GreaterThan_strategy = st.builds(
    prolog::expressions::GreaterThan,
)
prolog::expressions::Division_strategy = st.builds(
    prolog::expressions::Division,
)
prolog::expressions::Disequality_strategy = st.builds(
    prolog::expressions::Disequality,
)
prolog::expressions::EqualOrStandardOrderAfter_strategy = st.builds(
    prolog::expressions::EqualOrStandardOrderAfter,
)
prolog::expressions::SubDict_strategy = st.builds(
    prolog::expressions::SubDict,
)
prolog::expressions::ModuleCall_strategy = st.builds(
    prolog::expressions::ModuleCall,
)
prolog::expressions::NonEqualNumber_strategy = st.builds(
    prolog::expressions::NonEqualNumber,
)
prolog::expressions::Rem_strategy = st.builds(
    prolog::expressions::Rem,
)
prolog::expressions::BinaryOr_strategy = st.builds(
    prolog::expressions::BinaryOr,
)
prolog::expressions::Mod_strategy = st.builds(
    prolog::expressions::Mod,
)
prolog::expressions::Minus_strategy = st.builds(
    prolog::expressions::Minus,
)
prolog::expressions::Equivalence_strategy = st.builds(
    prolog::expressions::Equivalence,
)
prolog::expressions::Condition_strategy = st.builds(
    prolog::expressions::Condition,
)
prolog::expressions::Rdiv_strategy = st.builds(
    prolog::expressions::Rdiv,
)
prolog::expressions::ParticalUnification_strategy = st.builds(
    prolog::expressions::ParticalUnification,
)
prolog::expressions::Univ_strategy = st.builds(
    prolog::expressions::Univ,
)
prolog::expressions::BinaryAnd_strategy = st.builds(
    prolog::expressions::BinaryAnd,
)
prolog::expressions::EqualOrStandardOrderBefore_strategy = st.builds(
    prolog::expressions::EqualOrStandardOrderBefore,
)
prolog::expressions::Plus_strategy = st.builds(
    prolog::expressions::Plus,
)
prolog::expressions::Xor_strategy = st.builds(
    prolog::expressions::Xor,
)
prolog::expressions::StandardOrderBefore_strategy = st.builds(
    prolog::expressions::StandardOrderBefore,
)
prolog::expressions::StructuralEquivalenceNotProvable_strategy = st.builds(
    prolog::expressions::StructuralEquivalenceNotProvable,
)
prolog::expressions::NotUnifiable_strategy = st.builds(
    prolog::expressions::NotUnifiable,
)
prolog::expressions::IntegerDivision_strategy = st.builds(
    prolog::expressions::IntegerDivision,
)
prolog::expressions::As_strategy = st.builds(
    prolog::expressions::As,
)
prolog::expressions::StructuralEquivalence_strategy = st.builds(
    prolog::expressions::StructuralEquivalence,
)
prolog::expressions::BitwiseShiftLeft_strategy = st.builds(
    prolog::expressions::BitwiseShiftLeft,
)
prolog::expressions::LessOrEqual_strategy = st.builds(
    prolog::expressions::LessOrEqual,
)
prolog::expressions::LogicalAnd_strategy = st.builds(
    prolog::expressions::LogicalAnd,
)
prolog::expressions::Power_strategy = st.builds(
    prolog::expressions::Power,
)
prolog::expressions::Is_strategy = st.builds(
    prolog::expressions::Is,
)
prolog::expressions::StandardOrderAfter_strategy = st.builds(
    prolog::expressions::StandardOrderAfter,
)
prolog::expressions::SoftCut_strategy = st.builds(
    prolog::expressions::SoftCut,
)
prolog::expressions::Multiplication_strategy = st.builds(
    prolog::expressions::Multiplication,
)
prolog::expressions::Div_strategy = st.builds(
    prolog::expressions::Div,
)
prolog::expressions::LessThan_strategy = st.builds(
    prolog::expressions::LessThan,
)
prolog::expressions::Unification_strategy = st.builds(
    prolog::expressions::Unification,
)
prolog::expressions::GreaterOrEqual_strategy = st.builds(
    prolog::expressions::GreaterOrEqual,
)
prolog::expressions::LogicalOr_strategy = st.builds(
    prolog::expressions::LogicalOr,
)
prolog::expressions::Expression_strategy = st.builds(
    prolog::expressions::Expression,
)
Directive_strategy = st.builds(
    Directive,
)
prolog::directives::Public_strategy = st.builds(
    prolog::directives::Public,
)
prolog::directives::Volatile_strategy = st.builds(
    prolog::directives::Volatile,
)
prolog::directives::Dynamic_strategy = st.builds(
    prolog::directives::Dynamic,
)
prolog::directives::Multifile_strategy = st.builds(
    prolog::directives::Multifile,
)
prolog::directives::Discontiguous_strategy = st.builds(
    prolog::directives::Discontiguous,
)
Term_strategy = st.builds(
    Term,
)
prolog::AtomicNumber_strategy = st.builds(
    prolog::AtomicNumber,
    value=
        st.integers()
)
ControlPredicate_strategy = st.builds(
    ControlPredicate,
)
prolog::Cut_strategy = st.builds(
    prolog::Cut,
)
prolog::Fail_strategy = st.builds(
    prolog::Fail,
)
prolog::False_strategy = st.builds(
    prolog::False,
)
prolog::True_strategy = st.builds(
    prolog::True,
)
prolog::ControlPredicate_strategy = st.builds(
    prolog::ControlPredicate,
)
prolog::List_strategy = st.builds(
    prolog::List,
)
prolog::AtomicQuotedString_strategy = st.builds(
    prolog::AtomicQuotedString,
    value=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
prolog::expressions::UnaryExpression_strategy = st.builds(
    prolog::expressions::UnaryExpression,
)
prolog::expressions::BinaryExpression_strategy = st.builds(
    prolog::expressions::BinaryExpression,
)
prolog::Term_strategy = st.builds(
    prolog::Term,
)
Clause_strategy = st.builds(
    Clause,
)
prolog::Fact_strategy = st.builds(
    prolog::Fact,
)
prolog::directives::Table_strategy = st.builds(
    prolog::directives::Table,
)
prolog::Rule_strategy = st.builds(
    prolog::Rule,
)
prolog::directives::Directive_strategy = st.builds(
    prolog::directives::Directive,
    name=
        safe_text
)
prolog::CompoundTerm_strategy = st.builds(
    prolog::CompoundTerm,
    value=
        safe_text
)
prolog::Comment_strategy = st.builds(
    prolog::Comment,
    value=
        safe_text
)
prolog::Clause_strategy = st.builds(
    prolog::Clause,
)
prolog::Program_strategy = st.builds(
    prolog::Program,
)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=prolog::expressions::NegativeNumber_strategy)
@settings(max_examples=50)
def test_prolog::expressions::negativenumber_instantiation(instance):
    assert isinstance(instance, prolog::expressions::NegativeNumber)

@given(instance=prolog::expressions::BitwiseNegation_strategy)
@settings(max_examples=50)
def test_prolog::expressions::bitwisenegation_instantiation(instance):
    assert isinstance(instance, prolog::expressions::BitwiseNegation)

@given(instance=prolog::expressions::PositiveNumber_strategy)
@settings(max_examples=50)
def test_prolog::expressions::positivenumber_instantiation(instance):
    assert isinstance(instance, prolog::expressions::PositiveNumber)

@given(instance=prolog::expressions::NotProvable_strategy)
@settings(max_examples=50)
def test_prolog::expressions::notprovable_instantiation(instance):
    assert isinstance(instance, prolog::expressions::NotProvable)

@given(instance=prolog::directives::PredicateIndicator_strategy)
@settings(max_examples=50)
def test_prolog::directives::predicateindicator_instantiation(instance):
    assert isinstance(instance, prolog::directives::PredicateIndicator)

@given(instance=prolog::directives::PredicateIndicator_strategy)
def test_prolog::directives::predicateindicator_arity_type(instance):
    assert isinstance(instance.arity, int)


@given(instance=prolog::directives::PredicateIndicator_strategy)
def test_prolog::directives::predicateindicator_arity_setter(instance):
    original = instance.arity
    instance.arity = original
    assert instance.arity == original

@given(instance=prolog::directives::PredicateIndicator_strategy)
def test_prolog::directives::predicateindicator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=prolog::directives::PredicateIndicator_strategy)
def test_prolog::directives::predicateindicator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PredicateIndicator_strategy)
@settings(max_examples=50)
def test_predicateindicator_instantiation(instance):
    assert isinstance(instance, PredicateIndicator)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=prolog::expressions::NumberEqual_strategy)
@settings(max_examples=50)
def test_prolog::expressions::numberequal_instantiation(instance):
    assert isinstance(instance, prolog::expressions::NumberEqual)

@given(instance=prolog::expressions::GreaterThan_strategy)
@settings(max_examples=50)
def test_prolog::expressions::greaterthan_instantiation(instance):
    assert isinstance(instance, prolog::expressions::GreaterThan)

@given(instance=prolog::expressions::Division_strategy)
@settings(max_examples=50)
def test_prolog::expressions::division_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Division)

@given(instance=prolog::expressions::Disequality_strategy)
@settings(max_examples=50)
def test_prolog::expressions::disequality_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Disequality)

@given(instance=prolog::expressions::EqualOrStandardOrderAfter_strategy)
@settings(max_examples=50)
def test_prolog::expressions::equalorstandardorderafter_instantiation(instance):
    assert isinstance(instance, prolog::expressions::EqualOrStandardOrderAfter)

@given(instance=prolog::expressions::SubDict_strategy)
@settings(max_examples=50)
def test_prolog::expressions::subdict_instantiation(instance):
    assert isinstance(instance, prolog::expressions::SubDict)

@given(instance=prolog::expressions::ModuleCall_strategy)
@settings(max_examples=50)
def test_prolog::expressions::modulecall_instantiation(instance):
    assert isinstance(instance, prolog::expressions::ModuleCall)

@given(instance=prolog::expressions::NonEqualNumber_strategy)
@settings(max_examples=50)
def test_prolog::expressions::nonequalnumber_instantiation(instance):
    assert isinstance(instance, prolog::expressions::NonEqualNumber)

@given(instance=prolog::expressions::Rem_strategy)
@settings(max_examples=50)
def test_prolog::expressions::rem_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Rem)

@given(instance=prolog::expressions::BinaryOr_strategy)
@settings(max_examples=50)
def test_prolog::expressions::binaryor_instantiation(instance):
    assert isinstance(instance, prolog::expressions::BinaryOr)

@given(instance=prolog::expressions::Mod_strategy)
@settings(max_examples=50)
def test_prolog::expressions::mod_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Mod)

@given(instance=prolog::expressions::Minus_strategy)
@settings(max_examples=50)
def test_prolog::expressions::minus_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Minus)

@given(instance=prolog::expressions::Equivalence_strategy)
@settings(max_examples=50)
def test_prolog::expressions::equivalence_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Equivalence)

@given(instance=prolog::expressions::Condition_strategy)
@settings(max_examples=50)
def test_prolog::expressions::condition_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Condition)

@given(instance=prolog::expressions::Rdiv_strategy)
@settings(max_examples=50)
def test_prolog::expressions::rdiv_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Rdiv)

@given(instance=prolog::expressions::ParticalUnification_strategy)
@settings(max_examples=50)
def test_prolog::expressions::particalunification_instantiation(instance):
    assert isinstance(instance, prolog::expressions::ParticalUnification)

@given(instance=prolog::expressions::Univ_strategy)
@settings(max_examples=50)
def test_prolog::expressions::univ_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Univ)

@given(instance=prolog::expressions::BinaryAnd_strategy)
@settings(max_examples=50)
def test_prolog::expressions::binaryand_instantiation(instance):
    assert isinstance(instance, prolog::expressions::BinaryAnd)

@given(instance=prolog::expressions::EqualOrStandardOrderBefore_strategy)
@settings(max_examples=50)
def test_prolog::expressions::equalorstandardorderbefore_instantiation(instance):
    assert isinstance(instance, prolog::expressions::EqualOrStandardOrderBefore)

@given(instance=prolog::expressions::Plus_strategy)
@settings(max_examples=50)
def test_prolog::expressions::plus_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Plus)

@given(instance=prolog::expressions::Xor_strategy)
@settings(max_examples=50)
def test_prolog::expressions::xor_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Xor)

@given(instance=prolog::expressions::StandardOrderBefore_strategy)
@settings(max_examples=50)
def test_prolog::expressions::standardorderbefore_instantiation(instance):
    assert isinstance(instance, prolog::expressions::StandardOrderBefore)

@given(instance=prolog::expressions::StructuralEquivalenceNotProvable_strategy)
@settings(max_examples=50)
def test_prolog::expressions::structuralequivalencenotprovable_instantiation(instance):
    assert isinstance(instance, prolog::expressions::StructuralEquivalenceNotProvable)

@given(instance=prolog::expressions::NotUnifiable_strategy)
@settings(max_examples=50)
def test_prolog::expressions::notunifiable_instantiation(instance):
    assert isinstance(instance, prolog::expressions::NotUnifiable)

@given(instance=prolog::expressions::IntegerDivision_strategy)
@settings(max_examples=50)
def test_prolog::expressions::integerdivision_instantiation(instance):
    assert isinstance(instance, prolog::expressions::IntegerDivision)

@given(instance=prolog::expressions::As_strategy)
@settings(max_examples=50)
def test_prolog::expressions::as_instantiation(instance):
    assert isinstance(instance, prolog::expressions::As)

@given(instance=prolog::expressions::StructuralEquivalence_strategy)
@settings(max_examples=50)
def test_prolog::expressions::structuralequivalence_instantiation(instance):
    assert isinstance(instance, prolog::expressions::StructuralEquivalence)

@given(instance=prolog::expressions::BitwiseShiftLeft_strategy)
@settings(max_examples=50)
def test_prolog::expressions::bitwiseshiftleft_instantiation(instance):
    assert isinstance(instance, prolog::expressions::BitwiseShiftLeft)

@given(instance=prolog::expressions::LessOrEqual_strategy)
@settings(max_examples=50)
def test_prolog::expressions::lessorequal_instantiation(instance):
    assert isinstance(instance, prolog::expressions::LessOrEqual)

@given(instance=prolog::expressions::LogicalAnd_strategy)
@settings(max_examples=50)
def test_prolog::expressions::logicaland_instantiation(instance):
    assert isinstance(instance, prolog::expressions::LogicalAnd)

@given(instance=prolog::expressions::Power_strategy)
@settings(max_examples=50)
def test_prolog::expressions::power_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Power)

@given(instance=prolog::expressions::Is_strategy)
@settings(max_examples=50)
def test_prolog::expressions::is_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Is)

@given(instance=prolog::expressions::StandardOrderAfter_strategy)
@settings(max_examples=50)
def test_prolog::expressions::standardorderafter_instantiation(instance):
    assert isinstance(instance, prolog::expressions::StandardOrderAfter)

@given(instance=prolog::expressions::SoftCut_strategy)
@settings(max_examples=50)
def test_prolog::expressions::softcut_instantiation(instance):
    assert isinstance(instance, prolog::expressions::SoftCut)

@given(instance=prolog::expressions::Multiplication_strategy)
@settings(max_examples=50)
def test_prolog::expressions::multiplication_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Multiplication)

@given(instance=prolog::expressions::Div_strategy)
@settings(max_examples=50)
def test_prolog::expressions::div_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Div)

@given(instance=prolog::expressions::LessThan_strategy)
@settings(max_examples=50)
def test_prolog::expressions::lessthan_instantiation(instance):
    assert isinstance(instance, prolog::expressions::LessThan)

@given(instance=prolog::expressions::Unification_strategy)
@settings(max_examples=50)
def test_prolog::expressions::unification_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Unification)

@given(instance=prolog::expressions::GreaterOrEqual_strategy)
@settings(max_examples=50)
def test_prolog::expressions::greaterorequal_instantiation(instance):
    assert isinstance(instance, prolog::expressions::GreaterOrEqual)

@given(instance=prolog::expressions::LogicalOr_strategy)
@settings(max_examples=50)
def test_prolog::expressions::logicalor_instantiation(instance):
    assert isinstance(instance, prolog::expressions::LogicalOr)

@given(instance=prolog::expressions::Expression_strategy)
@settings(max_examples=50)
def test_prolog::expressions::expression_instantiation(instance):
    assert isinstance(instance, prolog::expressions::Expression)

@given(instance=Directive_strategy)
@settings(max_examples=50)
def test_directive_instantiation(instance):
    assert isinstance(instance, Directive)

@given(instance=prolog::directives::Public_strategy)
@settings(max_examples=50)
def test_prolog::directives::public_instantiation(instance):
    assert isinstance(instance, prolog::directives::Public)

@given(instance=prolog::directives::Volatile_strategy)
@settings(max_examples=50)
def test_prolog::directives::volatile_instantiation(instance):
    assert isinstance(instance, prolog::directives::Volatile)

@given(instance=prolog::directives::Dynamic_strategy)
@settings(max_examples=50)
def test_prolog::directives::dynamic_instantiation(instance):
    assert isinstance(instance, prolog::directives::Dynamic)

@given(instance=prolog::directives::Multifile_strategy)
@settings(max_examples=50)
def test_prolog::directives::multifile_instantiation(instance):
    assert isinstance(instance, prolog::directives::Multifile)

@given(instance=prolog::directives::Discontiguous_strategy)
@settings(max_examples=50)
def test_prolog::directives::discontiguous_instantiation(instance):
    assert isinstance(instance, prolog::directives::Discontiguous)

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=prolog::AtomicNumber_strategy)
@settings(max_examples=50)
def test_prolog::atomicnumber_instantiation(instance):
    assert isinstance(instance, prolog::AtomicNumber)

@given(instance=prolog::AtomicNumber_strategy)
def test_prolog::atomicnumber_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=prolog::AtomicNumber_strategy)
def test_prolog::atomicnumber_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ControlPredicate_strategy)
@settings(max_examples=50)
def test_controlpredicate_instantiation(instance):
    assert isinstance(instance, ControlPredicate)

@given(instance=prolog::Cut_strategy)
@settings(max_examples=50)
def test_prolog::cut_instantiation(instance):
    assert isinstance(instance, prolog::Cut)

@given(instance=prolog::Fail_strategy)
@settings(max_examples=50)
def test_prolog::fail_instantiation(instance):
    assert isinstance(instance, prolog::Fail)

@given(instance=prolog::False_strategy)
@settings(max_examples=50)
def test_prolog::false_instantiation(instance):
    assert isinstance(instance, prolog::False)

@given(instance=prolog::True_strategy)
@settings(max_examples=50)
def test_prolog::true_instantiation(instance):
    assert isinstance(instance, prolog::True)

@given(instance=prolog::ControlPredicate_strategy)
@settings(max_examples=50)
def test_prolog::controlpredicate_instantiation(instance):
    assert isinstance(instance, prolog::ControlPredicate)

@given(instance=prolog::List_strategy)
@settings(max_examples=50)
def test_prolog::list_instantiation(instance):
    assert isinstance(instance, prolog::List)

@given(instance=prolog::AtomicQuotedString_strategy)
@settings(max_examples=50)
def test_prolog::atomicquotedstring_instantiation(instance):
    assert isinstance(instance, prolog::AtomicQuotedString)

@given(instance=prolog::AtomicQuotedString_strategy)
def test_prolog::atomicquotedstring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=prolog::AtomicQuotedString_strategy)
def test_prolog::atomicquotedstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=prolog::expressions::UnaryExpression_strategy)
@settings(max_examples=50)
def test_prolog::expressions::unaryexpression_instantiation(instance):
    assert isinstance(instance, prolog::expressions::UnaryExpression)

@given(instance=prolog::expressions::BinaryExpression_strategy)
@settings(max_examples=50)
def test_prolog::expressions::binaryexpression_instantiation(instance):
    assert isinstance(instance, prolog::expressions::BinaryExpression)

@given(instance=prolog::Term_strategy)
@settings(max_examples=50)
def test_prolog::term_instantiation(instance):
    assert isinstance(instance, prolog::Term)

@given(instance=Clause_strategy)
@settings(max_examples=50)
def test_clause_instantiation(instance):
    assert isinstance(instance, Clause)

@given(instance=prolog::Fact_strategy)
@settings(max_examples=50)
def test_prolog::fact_instantiation(instance):
    assert isinstance(instance, prolog::Fact)

@given(instance=prolog::directives::Table_strategy)
@settings(max_examples=50)
def test_prolog::directives::table_instantiation(instance):
    assert isinstance(instance, prolog::directives::Table)

@given(instance=prolog::Rule_strategy)
@settings(max_examples=50)
def test_prolog::rule_instantiation(instance):
    assert isinstance(instance, prolog::Rule)

@given(instance=prolog::directives::Directive_strategy)
@settings(max_examples=50)
def test_prolog::directives::directive_instantiation(instance):
    assert isinstance(instance, prolog::directives::Directive)

@given(instance=prolog::directives::Directive_strategy)
def test_prolog::directives::directive_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=prolog::directives::Directive_strategy)
def test_prolog::directives::directive_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prolog::CompoundTerm_strategy)
@settings(max_examples=50)
def test_prolog::compoundterm_instantiation(instance):
    assert isinstance(instance, prolog::CompoundTerm)

@given(instance=prolog::CompoundTerm_strategy)
def test_prolog::compoundterm_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=prolog::CompoundTerm_strategy)
def test_prolog::compoundterm_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=prolog::Comment_strategy)
@settings(max_examples=50)
def test_prolog::comment_instantiation(instance):
    assert isinstance(instance, prolog::Comment)

@given(instance=prolog::Comment_strategy)
def test_prolog::comment_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=prolog::Comment_strategy)
def test_prolog::comment_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=prolog::Clause_strategy)
@settings(max_examples=50)
def test_prolog::clause_instantiation(instance):
    assert isinstance(instance, prolog::Clause)

@given(instance=prolog::Program_strategy)
@settings(max_examples=50)
def test_prolog::program_instantiation(instance):
    assert isinstance(instance, prolog::Program)
