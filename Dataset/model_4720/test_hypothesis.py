import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rule::CellularAutomata,
    UnaryExpression,
    rule::UMinus,
    rule::Not,
    IntegerExpression,
    rule::CurrentCellPopulation,
    rule::NeighborsExpression,
    rule::IntegerLiteral,
    rule::Conditional,
    rule::BinaryExpression,
    rule::UnaryExpression,
    BinaryExpression,
    rule::Div,
    rule::Lower,
    rule::Equal,
    rule::Mult,
    rule::And,
    rule::Greater,
    rule::Or,
    rule::Mod,
    rule::Minus,
    rule::Add,
    NeighborsExpression,
    rule::Min,
    rule::Size,
    rule::Sum,
    rule::Max,
    rule::PopulationRange,
    rule::IntegerExpression,
    rule::Rule,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rule::cellularautomata_is_not_abstract():
    assert not inspect.isabstract(rule::CellularAutomata)


def test_rule::cellularautomata_constructor_exists():
    assert callable(rule::CellularAutomata.__init__)


def test_rule::cellularautomata_constructor_args():
    sig = inspect.signature(rule::CellularAutomata.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_rule::uminus_is_not_abstract():
    assert not inspect.isabstract(rule::UMinus)


def test_rule::uminus_constructor_exists():
    assert callable(rule::UMinus.__init__)


def test_rule::uminus_constructor_args():
    sig = inspect.signature(rule::UMinus.__init__)
    params = list(sig.parameters.keys())



def test_rule::not_is_not_abstract():
    assert not inspect.isabstract(rule::Not)


def test_rule::not_constructor_exists():
    assert callable(rule::Not.__init__)


def test_rule::not_constructor_args():
    sig = inspect.signature(rule::Not.__init__)
    params = list(sig.parameters.keys())



def test_integerexpression_is_not_abstract():
    assert not inspect.isabstract(IntegerExpression)


def test_integerexpression_constructor_exists():
    assert callable(IntegerExpression.__init__)


def test_integerexpression_constructor_args():
    sig = inspect.signature(IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_rule::currentcellpopulation_is_not_abstract():
    assert not inspect.isabstract(rule::CurrentCellPopulation)


def test_rule::currentcellpopulation_constructor_exists():
    assert callable(rule::CurrentCellPopulation.__init__)


def test_rule::currentcellpopulation_constructor_args():
    sig = inspect.signature(rule::CurrentCellPopulation.__init__)
    params = list(sig.parameters.keys())



def test_rule::neighborsexpression_is_not_abstract():
    assert not inspect.isabstract(rule::NeighborsExpression)


def test_rule::neighborsexpression_constructor_exists():
    assert callable(rule::NeighborsExpression.__init__)


def test_rule::neighborsexpression_constructor_args():
    sig = inspect.signature(rule::NeighborsExpression.__init__)
    params = list(sig.parameters.keys())



def test_rule::integerliteral_is_not_abstract():
    assert not inspect.isabstract(rule::IntegerLiteral)


def test_rule::integerliteral_constructor_exists():
    assert callable(rule::IntegerLiteral.__init__)


def test_rule::integerliteral_constructor_args():
    sig = inspect.signature(rule::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_rule::integerliteral_has_val():
    assert hasattr(rule::IntegerLiteral, "val")
    descriptor = None
    for klass in rule::IntegerLiteral.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_rule::conditional_is_not_abstract():
    assert not inspect.isabstract(rule::Conditional)


def test_rule::conditional_constructor_exists():
    assert callable(rule::Conditional.__init__)


def test_rule::conditional_constructor_args():
    sig = inspect.signature(rule::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_rule::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(rule::BinaryExpression)


def test_rule::binaryexpression_constructor_exists():
    assert callable(rule::BinaryExpression.__init__)


def test_rule::binaryexpression_constructor_args():
    sig = inspect.signature(rule::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_rule::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(rule::UnaryExpression)


def test_rule::unaryexpression_constructor_exists():
    assert callable(rule::UnaryExpression.__init__)


def test_rule::unaryexpression_constructor_args():
    sig = inspect.signature(rule::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_rule::div_is_not_abstract():
    assert not inspect.isabstract(rule::Div)


def test_rule::div_constructor_exists():
    assert callable(rule::Div.__init__)


def test_rule::div_constructor_args():
    sig = inspect.signature(rule::Div.__init__)
    params = list(sig.parameters.keys())



def test_rule::lower_is_not_abstract():
    assert not inspect.isabstract(rule::Lower)


def test_rule::lower_constructor_exists():
    assert callable(rule::Lower.__init__)


def test_rule::lower_constructor_args():
    sig = inspect.signature(rule::Lower.__init__)
    params = list(sig.parameters.keys())



def test_rule::equal_is_not_abstract():
    assert not inspect.isabstract(rule::Equal)


def test_rule::equal_constructor_exists():
    assert callable(rule::Equal.__init__)


def test_rule::equal_constructor_args():
    sig = inspect.signature(rule::Equal.__init__)
    params = list(sig.parameters.keys())



def test_rule::mult_is_not_abstract():
    assert not inspect.isabstract(rule::Mult)


def test_rule::mult_constructor_exists():
    assert callable(rule::Mult.__init__)


def test_rule::mult_constructor_args():
    sig = inspect.signature(rule::Mult.__init__)
    params = list(sig.parameters.keys())



def test_rule::and_is_not_abstract():
    assert not inspect.isabstract(rule::And)


def test_rule::and_constructor_exists():
    assert callable(rule::And.__init__)


def test_rule::and_constructor_args():
    sig = inspect.signature(rule::And.__init__)
    params = list(sig.parameters.keys())



def test_rule::greater_is_not_abstract():
    assert not inspect.isabstract(rule::Greater)


def test_rule::greater_constructor_exists():
    assert callable(rule::Greater.__init__)


def test_rule::greater_constructor_args():
    sig = inspect.signature(rule::Greater.__init__)
    params = list(sig.parameters.keys())



def test_rule::or_is_not_abstract():
    assert not inspect.isabstract(rule::Or)


def test_rule::or_constructor_exists():
    assert callable(rule::Or.__init__)


def test_rule::or_constructor_args():
    sig = inspect.signature(rule::Or.__init__)
    params = list(sig.parameters.keys())



def test_rule::mod_is_not_abstract():
    assert not inspect.isabstract(rule::Mod)


def test_rule::mod_constructor_exists():
    assert callable(rule::Mod.__init__)


def test_rule::mod_constructor_args():
    sig = inspect.signature(rule::Mod.__init__)
    params = list(sig.parameters.keys())



def test_rule::minus_is_not_abstract():
    assert not inspect.isabstract(rule::Minus)


def test_rule::minus_constructor_exists():
    assert callable(rule::Minus.__init__)


def test_rule::minus_constructor_args():
    sig = inspect.signature(rule::Minus.__init__)
    params = list(sig.parameters.keys())



def test_rule::add_is_not_abstract():
    assert not inspect.isabstract(rule::Add)


def test_rule::add_constructor_exists():
    assert callable(rule::Add.__init__)


def test_rule::add_constructor_args():
    sig = inspect.signature(rule::Add.__init__)
    params = list(sig.parameters.keys())



def test_neighborsexpression_is_not_abstract():
    assert not inspect.isabstract(NeighborsExpression)


def test_neighborsexpression_constructor_exists():
    assert callable(NeighborsExpression.__init__)


def test_neighborsexpression_constructor_args():
    sig = inspect.signature(NeighborsExpression.__init__)
    params = list(sig.parameters.keys())



def test_rule::min_is_not_abstract():
    assert not inspect.isabstract(rule::Min)


def test_rule::min_constructor_exists():
    assert callable(rule::Min.__init__)


def test_rule::min_constructor_args():
    sig = inspect.signature(rule::Min.__init__)
    params = list(sig.parameters.keys())



def test_rule::size_is_not_abstract():
    assert not inspect.isabstract(rule::Size)


def test_rule::size_constructor_exists():
    assert callable(rule::Size.__init__)


def test_rule::size_constructor_args():
    sig = inspect.signature(rule::Size.__init__)
    params = list(sig.parameters.keys())



def test_rule::sum_is_not_abstract():
    assert not inspect.isabstract(rule::Sum)


def test_rule::sum_constructor_exists():
    assert callable(rule::Sum.__init__)


def test_rule::sum_constructor_args():
    sig = inspect.signature(rule::Sum.__init__)
    params = list(sig.parameters.keys())



def test_rule::max_is_not_abstract():
    assert not inspect.isabstract(rule::Max)


def test_rule::max_constructor_exists():
    assert callable(rule::Max.__init__)


def test_rule::max_constructor_args():
    sig = inspect.signature(rule::Max.__init__)
    params = list(sig.parameters.keys())



def test_rule::populationrange_is_not_abstract():
    assert not inspect.isabstract(rule::PopulationRange)


def test_rule::populationrange_constructor_exists():
    assert callable(rule::PopulationRange.__init__)


def test_rule::populationrange_constructor_args():
    sig = inspect.signature(rule::PopulationRange.__init__)
    params = list(sig.parameters.keys())
    assert "upperRange" in params, "Missing parameter 'upperRange'"
    assert "lowerRange" in params, "Missing parameter 'lowerRange'"

def test_rule::populationrange_has_upperRange():
    assert hasattr(rule::PopulationRange, "upperRange")
    descriptor = None
    for klass in rule::PopulationRange.__mro__:
        if "upperRange" in klass.__dict__:
            descriptor = klass.__dict__["upperRange"]
            break
    assert isinstance(descriptor, property)

def test_rule::populationrange_has_lowerRange():
    assert hasattr(rule::PopulationRange, "lowerRange")
    descriptor = None
    for klass in rule::PopulationRange.__mro__:
        if "lowerRange" in klass.__dict__:
            descriptor = klass.__dict__["lowerRange"]
            break
    assert isinstance(descriptor, property)



def test_rule::integerexpression_is_not_abstract():
    assert not inspect.isabstract(rule::IntegerExpression)


def test_rule::integerexpression_constructor_exists():
    assert callable(rule::IntegerExpression.__init__)


def test_rule::integerexpression_constructor_args():
    sig = inspect.signature(rule::IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_rule::rule_is_not_abstract():
    assert not inspect.isabstract(rule::Rule)


def test_rule::rule_constructor_exists():
    assert callable(rule::Rule.__init__)


def test_rule::rule_constructor_args():
    sig = inspect.signature(rule::Rule.__init__)
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
rule::CellularAutomata_strategy = st.builds(
    rule::CellularAutomata,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
rule::UMinus_strategy = st.builds(
    rule::UMinus,
)
rule::Not_strategy = st.builds(
    rule::Not,
)
IntegerExpression_strategy = st.builds(
    IntegerExpression,
)
rule::CurrentCellPopulation_strategy = st.builds(
    rule::CurrentCellPopulation,
)
rule::NeighborsExpression_strategy = st.builds(
    rule::NeighborsExpression,
)
rule::IntegerLiteral_strategy = st.builds(
    rule::IntegerLiteral,
    val=
        st.integers()
)
rule::Conditional_strategy = st.builds(
    rule::Conditional,
)
rule::BinaryExpression_strategy = st.builds(
    rule::BinaryExpression,
)
rule::UnaryExpression_strategy = st.builds(
    rule::UnaryExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
rule::Div_strategy = st.builds(
    rule::Div,
)
rule::Lower_strategy = st.builds(
    rule::Lower,
)
rule::Equal_strategy = st.builds(
    rule::Equal,
)
rule::Mult_strategy = st.builds(
    rule::Mult,
)
rule::And_strategy = st.builds(
    rule::And,
)
rule::Greater_strategy = st.builds(
    rule::Greater,
)
rule::Or_strategy = st.builds(
    rule::Or,
)
rule::Mod_strategy = st.builds(
    rule::Mod,
)
rule::Minus_strategy = st.builds(
    rule::Minus,
)
rule::Add_strategy = st.builds(
    rule::Add,
)
NeighborsExpression_strategy = st.builds(
    NeighborsExpression,
)
rule::Min_strategy = st.builds(
    rule::Min,
)
rule::Size_strategy = st.builds(
    rule::Size,
)
rule::Sum_strategy = st.builds(
    rule::Sum,
)
rule::Max_strategy = st.builds(
    rule::Max,
)
rule::PopulationRange_strategy = st.builds(
    rule::PopulationRange,
    upperRange=
        st.integers(),
    lowerRange=
        st.integers()
)
rule::IntegerExpression_strategy = st.builds(
    rule::IntegerExpression,
)
rule::Rule_strategy = st.builds(
    rule::Rule,
)

@given(instance=rule::CellularAutomata_strategy)
@settings(max_examples=50)
def test_rule::cellularautomata_instantiation(instance):
    assert isinstance(instance, rule::CellularAutomata)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=rule::UMinus_strategy)
@settings(max_examples=50)
def test_rule::uminus_instantiation(instance):
    assert isinstance(instance, rule::UMinus)

@given(instance=rule::Not_strategy)
@settings(max_examples=50)
def test_rule::not_instantiation(instance):
    assert isinstance(instance, rule::Not)

@given(instance=IntegerExpression_strategy)
@settings(max_examples=50)
def test_integerexpression_instantiation(instance):
    assert isinstance(instance, IntegerExpression)

@given(instance=rule::CurrentCellPopulation_strategy)
@settings(max_examples=50)
def test_rule::currentcellpopulation_instantiation(instance):
    assert isinstance(instance, rule::CurrentCellPopulation)

@given(instance=rule::NeighborsExpression_strategy)
@settings(max_examples=50)
def test_rule::neighborsexpression_instantiation(instance):
    assert isinstance(instance, rule::NeighborsExpression)

@given(instance=rule::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_rule::integerliteral_instantiation(instance):
    assert isinstance(instance, rule::IntegerLiteral)

@given(instance=rule::IntegerLiteral_strategy)
def test_rule::integerliteral_val_type(instance):
    assert isinstance(instance.val, int)


@given(instance=rule::IntegerLiteral_strategy)
def test_rule::integerliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=rule::Conditional_strategy)
@settings(max_examples=50)
def test_rule::conditional_instantiation(instance):
    assert isinstance(instance, rule::Conditional)

@given(instance=rule::BinaryExpression_strategy)
@settings(max_examples=50)
def test_rule::binaryexpression_instantiation(instance):
    assert isinstance(instance, rule::BinaryExpression)

@given(instance=rule::UnaryExpression_strategy)
@settings(max_examples=50)
def test_rule::unaryexpression_instantiation(instance):
    assert isinstance(instance, rule::UnaryExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=rule::Div_strategy)
@settings(max_examples=50)
def test_rule::div_instantiation(instance):
    assert isinstance(instance, rule::Div)

@given(instance=rule::Lower_strategy)
@settings(max_examples=50)
def test_rule::lower_instantiation(instance):
    assert isinstance(instance, rule::Lower)

@given(instance=rule::Equal_strategy)
@settings(max_examples=50)
def test_rule::equal_instantiation(instance):
    assert isinstance(instance, rule::Equal)

@given(instance=rule::Mult_strategy)
@settings(max_examples=50)
def test_rule::mult_instantiation(instance):
    assert isinstance(instance, rule::Mult)

@given(instance=rule::And_strategy)
@settings(max_examples=50)
def test_rule::and_instantiation(instance):
    assert isinstance(instance, rule::And)

@given(instance=rule::Greater_strategy)
@settings(max_examples=50)
def test_rule::greater_instantiation(instance):
    assert isinstance(instance, rule::Greater)

@given(instance=rule::Or_strategy)
@settings(max_examples=50)
def test_rule::or_instantiation(instance):
    assert isinstance(instance, rule::Or)

@given(instance=rule::Mod_strategy)
@settings(max_examples=50)
def test_rule::mod_instantiation(instance):
    assert isinstance(instance, rule::Mod)

@given(instance=rule::Minus_strategy)
@settings(max_examples=50)
def test_rule::minus_instantiation(instance):
    assert isinstance(instance, rule::Minus)

@given(instance=rule::Add_strategy)
@settings(max_examples=50)
def test_rule::add_instantiation(instance):
    assert isinstance(instance, rule::Add)

@given(instance=NeighborsExpression_strategy)
@settings(max_examples=50)
def test_neighborsexpression_instantiation(instance):
    assert isinstance(instance, NeighborsExpression)

@given(instance=rule::Min_strategy)
@settings(max_examples=50)
def test_rule::min_instantiation(instance):
    assert isinstance(instance, rule::Min)

@given(instance=rule::Size_strategy)
@settings(max_examples=50)
def test_rule::size_instantiation(instance):
    assert isinstance(instance, rule::Size)

@given(instance=rule::Sum_strategy)
@settings(max_examples=50)
def test_rule::sum_instantiation(instance):
    assert isinstance(instance, rule::Sum)

@given(instance=rule::Max_strategy)
@settings(max_examples=50)
def test_rule::max_instantiation(instance):
    assert isinstance(instance, rule::Max)

@given(instance=rule::PopulationRange_strategy)
@settings(max_examples=50)
def test_rule::populationrange_instantiation(instance):
    assert isinstance(instance, rule::PopulationRange)

@given(instance=rule::PopulationRange_strategy)
def test_rule::populationrange_upperRange_type(instance):
    assert isinstance(instance.upperRange, int)


@given(instance=rule::PopulationRange_strategy)
def test_rule::populationrange_upperRange_setter(instance):
    original = instance.upperRange
    instance.upperRange = original
    assert instance.upperRange == original

@given(instance=rule::PopulationRange_strategy)
def test_rule::populationrange_lowerRange_type(instance):
    assert isinstance(instance.lowerRange, int)


@given(instance=rule::PopulationRange_strategy)
def test_rule::populationrange_lowerRange_setter(instance):
    original = instance.lowerRange
    instance.lowerRange = original
    assert instance.lowerRange == original

@given(instance=rule::IntegerExpression_strategy)
@settings(max_examples=50)
def test_rule::integerexpression_instantiation(instance):
    assert isinstance(instance, rule::IntegerExpression)

@given(instance=rule::Rule_strategy)
@settings(max_examples=50)
def test_rule::rule_instantiation(instance):
    assert isinstance(instance, rule::Rule)
