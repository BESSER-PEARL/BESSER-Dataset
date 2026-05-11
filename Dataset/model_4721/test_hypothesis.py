import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ca::rule::CellularAutomata,
    UnaryExpression,
    ca::rule::UMinus,
    ca::rule::Not,
    IntegerExpression,
    ca::rule::IntegerLiteral,
    ca::rule::CurrentCellPopulation,
    ca::rule::BinaryExpression,
    ca::rule::Conditional,
    ca::rule::NeighborsExpression,
    ca::rule::UnaryExpression,
    BinaryExpression,
    ca::rule::Equal,
    ca::rule::Greater,
    ca::rule::Or,
    ca::rule::Minus,
    ca::rule::Lower,
    ca::rule::Mult,
    ca::rule::And,
    ca::rule::Mod,
    ca::rule::Div,
    ca::rule::Add,
    NeighborsExpression,
    ca::rule::Size,
    ca::rule::Min,
    ca::rule::Sum,
    ca::rule::Max,
    ca::rule::PopulationRange,
    ca::rule::IntegerExpression,
    ca::rule::Rule,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ca::rule::cellularautomata_is_not_abstract():
    assert not inspect.isabstract(ca::rule::CellularAutomata)


def test_ca::rule::cellularautomata_constructor_exists():
    assert callable(ca::rule::CellularAutomata.__init__)


def test_ca::rule::cellularautomata_constructor_args():
    sig = inspect.signature(ca::rule::CellularAutomata.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::uminus_is_not_abstract():
    assert not inspect.isabstract(ca::rule::UMinus)


def test_ca::rule::uminus_constructor_exists():
    assert callable(ca::rule::UMinus.__init__)


def test_ca::rule::uminus_constructor_args():
    sig = inspect.signature(ca::rule::UMinus.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::not_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Not)


def test_ca::rule::not_constructor_exists():
    assert callable(ca::rule::Not.__init__)


def test_ca::rule::not_constructor_args():
    sig = inspect.signature(ca::rule::Not.__init__)
    params = list(sig.parameters.keys())



def test_integerexpression_is_not_abstract():
    assert not inspect.isabstract(IntegerExpression)


def test_integerexpression_constructor_exists():
    assert callable(IntegerExpression.__init__)


def test_integerexpression_constructor_args():
    sig = inspect.signature(IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::integerliteral_is_not_abstract():
    assert not inspect.isabstract(ca::rule::IntegerLiteral)


def test_ca::rule::integerliteral_constructor_exists():
    assert callable(ca::rule::IntegerLiteral.__init__)


def test_ca::rule::integerliteral_constructor_args():
    sig = inspect.signature(ca::rule::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ca::rule::integerliteral_has_value():
    assert hasattr(ca::rule::IntegerLiteral, "value")
    descriptor = None
    for klass in ca::rule::IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ca::rule::currentcellpopulation_is_not_abstract():
    assert not inspect.isabstract(ca::rule::CurrentCellPopulation)


def test_ca::rule::currentcellpopulation_constructor_exists():
    assert callable(ca::rule::CurrentCellPopulation.__init__)


def test_ca::rule::currentcellpopulation_constructor_args():
    sig = inspect.signature(ca::rule::CurrentCellPopulation.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(ca::rule::BinaryExpression)


def test_ca::rule::binaryexpression_constructor_exists():
    assert callable(ca::rule::BinaryExpression.__init__)


def test_ca::rule::binaryexpression_constructor_args():
    sig = inspect.signature(ca::rule::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::conditional_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Conditional)


def test_ca::rule::conditional_constructor_exists():
    assert callable(ca::rule::Conditional.__init__)


def test_ca::rule::conditional_constructor_args():
    sig = inspect.signature(ca::rule::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::neighborsexpression_is_not_abstract():
    assert not inspect.isabstract(ca::rule::NeighborsExpression)


def test_ca::rule::neighborsexpression_constructor_exists():
    assert callable(ca::rule::NeighborsExpression.__init__)


def test_ca::rule::neighborsexpression_constructor_args():
    sig = inspect.signature(ca::rule::NeighborsExpression.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(ca::rule::UnaryExpression)


def test_ca::rule::unaryexpression_constructor_exists():
    assert callable(ca::rule::UnaryExpression.__init__)


def test_ca::rule::unaryexpression_constructor_args():
    sig = inspect.signature(ca::rule::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::equal_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Equal)


def test_ca::rule::equal_constructor_exists():
    assert callable(ca::rule::Equal.__init__)


def test_ca::rule::equal_constructor_args():
    sig = inspect.signature(ca::rule::Equal.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::greater_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Greater)


def test_ca::rule::greater_constructor_exists():
    assert callable(ca::rule::Greater.__init__)


def test_ca::rule::greater_constructor_args():
    sig = inspect.signature(ca::rule::Greater.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::or_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Or)


def test_ca::rule::or_constructor_exists():
    assert callable(ca::rule::Or.__init__)


def test_ca::rule::or_constructor_args():
    sig = inspect.signature(ca::rule::Or.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::minus_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Minus)


def test_ca::rule::minus_constructor_exists():
    assert callable(ca::rule::Minus.__init__)


def test_ca::rule::minus_constructor_args():
    sig = inspect.signature(ca::rule::Minus.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::lower_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Lower)


def test_ca::rule::lower_constructor_exists():
    assert callable(ca::rule::Lower.__init__)


def test_ca::rule::lower_constructor_args():
    sig = inspect.signature(ca::rule::Lower.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::mult_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Mult)


def test_ca::rule::mult_constructor_exists():
    assert callable(ca::rule::Mult.__init__)


def test_ca::rule::mult_constructor_args():
    sig = inspect.signature(ca::rule::Mult.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::and_is_not_abstract():
    assert not inspect.isabstract(ca::rule::And)


def test_ca::rule::and_constructor_exists():
    assert callable(ca::rule::And.__init__)


def test_ca::rule::and_constructor_args():
    sig = inspect.signature(ca::rule::And.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::mod_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Mod)


def test_ca::rule::mod_constructor_exists():
    assert callable(ca::rule::Mod.__init__)


def test_ca::rule::mod_constructor_args():
    sig = inspect.signature(ca::rule::Mod.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::div_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Div)


def test_ca::rule::div_constructor_exists():
    assert callable(ca::rule::Div.__init__)


def test_ca::rule::div_constructor_args():
    sig = inspect.signature(ca::rule::Div.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::add_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Add)


def test_ca::rule::add_constructor_exists():
    assert callable(ca::rule::Add.__init__)


def test_ca::rule::add_constructor_args():
    sig = inspect.signature(ca::rule::Add.__init__)
    params = list(sig.parameters.keys())



def test_neighborsexpression_is_not_abstract():
    assert not inspect.isabstract(NeighborsExpression)


def test_neighborsexpression_constructor_exists():
    assert callable(NeighborsExpression.__init__)


def test_neighborsexpression_constructor_args():
    sig = inspect.signature(NeighborsExpression.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::size_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Size)


def test_ca::rule::size_constructor_exists():
    assert callable(ca::rule::Size.__init__)


def test_ca::rule::size_constructor_args():
    sig = inspect.signature(ca::rule::Size.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::min_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Min)


def test_ca::rule::min_constructor_exists():
    assert callable(ca::rule::Min.__init__)


def test_ca::rule::min_constructor_args():
    sig = inspect.signature(ca::rule::Min.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::sum_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Sum)


def test_ca::rule::sum_constructor_exists():
    assert callable(ca::rule::Sum.__init__)


def test_ca::rule::sum_constructor_args():
    sig = inspect.signature(ca::rule::Sum.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::max_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Max)


def test_ca::rule::max_constructor_exists():
    assert callable(ca::rule::Max.__init__)


def test_ca::rule::max_constructor_args():
    sig = inspect.signature(ca::rule::Max.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::populationrange_is_not_abstract():
    assert not inspect.isabstract(ca::rule::PopulationRange)


def test_ca::rule::populationrange_constructor_exists():
    assert callable(ca::rule::PopulationRange.__init__)


def test_ca::rule::populationrange_constructor_args():
    sig = inspect.signature(ca::rule::PopulationRange.__init__)
    params = list(sig.parameters.keys())
    assert "upperRange" in params, "Missing parameter 'upperRange'"
    assert "lowerRange" in params, "Missing parameter 'lowerRange'"

def test_ca::rule::populationrange_has_upperRange():
    assert hasattr(ca::rule::PopulationRange, "upperRange")
    descriptor = None
    for klass in ca::rule::PopulationRange.__mro__:
        if "upperRange" in klass.__dict__:
            descriptor = klass.__dict__["upperRange"]
            break
    assert isinstance(descriptor, property)

def test_ca::rule::populationrange_has_lowerRange():
    assert hasattr(ca::rule::PopulationRange, "lowerRange")
    descriptor = None
    for klass in ca::rule::PopulationRange.__mro__:
        if "lowerRange" in klass.__dict__:
            descriptor = klass.__dict__["lowerRange"]
            break
    assert isinstance(descriptor, property)



def test_ca::rule::integerexpression_is_not_abstract():
    assert not inspect.isabstract(ca::rule::IntegerExpression)


def test_ca::rule::integerexpression_constructor_exists():
    assert callable(ca::rule::IntegerExpression.__init__)


def test_ca::rule::integerexpression_constructor_args():
    sig = inspect.signature(ca::rule::IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_ca::rule::rule_is_not_abstract():
    assert not inspect.isabstract(ca::rule::Rule)


def test_ca::rule::rule_constructor_exists():
    assert callable(ca::rule::Rule.__init__)


def test_ca::rule::rule_constructor_args():
    sig = inspect.signature(ca::rule::Rule.__init__)
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
ca::rule::CellularAutomata_strategy = st.builds(
    ca::rule::CellularAutomata,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
ca::rule::UMinus_strategy = st.builds(
    ca::rule::UMinus,
)
ca::rule::Not_strategy = st.builds(
    ca::rule::Not,
)
IntegerExpression_strategy = st.builds(
    IntegerExpression,
)
ca::rule::IntegerLiteral_strategy = st.builds(
    ca::rule::IntegerLiteral,
    value=
        st.integers()
)
ca::rule::CurrentCellPopulation_strategy = st.builds(
    ca::rule::CurrentCellPopulation,
)
ca::rule::BinaryExpression_strategy = st.builds(
    ca::rule::BinaryExpression,
)
ca::rule::Conditional_strategy = st.builds(
    ca::rule::Conditional,
)
ca::rule::NeighborsExpression_strategy = st.builds(
    ca::rule::NeighborsExpression,
)
ca::rule::UnaryExpression_strategy = st.builds(
    ca::rule::UnaryExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
ca::rule::Equal_strategy = st.builds(
    ca::rule::Equal,
)
ca::rule::Greater_strategy = st.builds(
    ca::rule::Greater,
)
ca::rule::Or_strategy = st.builds(
    ca::rule::Or,
)
ca::rule::Minus_strategy = st.builds(
    ca::rule::Minus,
)
ca::rule::Lower_strategy = st.builds(
    ca::rule::Lower,
)
ca::rule::Mult_strategy = st.builds(
    ca::rule::Mult,
)
ca::rule::And_strategy = st.builds(
    ca::rule::And,
)
ca::rule::Mod_strategy = st.builds(
    ca::rule::Mod,
)
ca::rule::Div_strategy = st.builds(
    ca::rule::Div,
)
ca::rule::Add_strategy = st.builds(
    ca::rule::Add,
)
NeighborsExpression_strategy = st.builds(
    NeighborsExpression,
)
ca::rule::Size_strategy = st.builds(
    ca::rule::Size,
)
ca::rule::Min_strategy = st.builds(
    ca::rule::Min,
)
ca::rule::Sum_strategy = st.builds(
    ca::rule::Sum,
)
ca::rule::Max_strategy = st.builds(
    ca::rule::Max,
)
ca::rule::PopulationRange_strategy = st.builds(
    ca::rule::PopulationRange,
    upperRange=
        st.integers(),
    lowerRange=
        st.integers()
)
ca::rule::IntegerExpression_strategy = st.builds(
    ca::rule::IntegerExpression,
)
ca::rule::Rule_strategy = st.builds(
    ca::rule::Rule,
)

@given(instance=ca::rule::CellularAutomata_strategy)
@settings(max_examples=50)
def test_ca::rule::cellularautomata_instantiation(instance):
    assert isinstance(instance, ca::rule::CellularAutomata)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=ca::rule::UMinus_strategy)
@settings(max_examples=50)
def test_ca::rule::uminus_instantiation(instance):
    assert isinstance(instance, ca::rule::UMinus)

@given(instance=ca::rule::Not_strategy)
@settings(max_examples=50)
def test_ca::rule::not_instantiation(instance):
    assert isinstance(instance, ca::rule::Not)

@given(instance=IntegerExpression_strategy)
@settings(max_examples=50)
def test_integerexpression_instantiation(instance):
    assert isinstance(instance, IntegerExpression)

@given(instance=ca::rule::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_ca::rule::integerliteral_instantiation(instance):
    assert isinstance(instance, ca::rule::IntegerLiteral)

@given(instance=ca::rule::IntegerLiteral_strategy)
def test_ca::rule::integerliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=ca::rule::IntegerLiteral_strategy)
def test_ca::rule::integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ca::rule::CurrentCellPopulation_strategy)
@settings(max_examples=50)
def test_ca::rule::currentcellpopulation_instantiation(instance):
    assert isinstance(instance, ca::rule::CurrentCellPopulation)

@given(instance=ca::rule::BinaryExpression_strategy)
@settings(max_examples=50)
def test_ca::rule::binaryexpression_instantiation(instance):
    assert isinstance(instance, ca::rule::BinaryExpression)

@given(instance=ca::rule::Conditional_strategy)
@settings(max_examples=50)
def test_ca::rule::conditional_instantiation(instance):
    assert isinstance(instance, ca::rule::Conditional)

@given(instance=ca::rule::NeighborsExpression_strategy)
@settings(max_examples=50)
def test_ca::rule::neighborsexpression_instantiation(instance):
    assert isinstance(instance, ca::rule::NeighborsExpression)

@given(instance=ca::rule::UnaryExpression_strategy)
@settings(max_examples=50)
def test_ca::rule::unaryexpression_instantiation(instance):
    assert isinstance(instance, ca::rule::UnaryExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=ca::rule::Equal_strategy)
@settings(max_examples=50)
def test_ca::rule::equal_instantiation(instance):
    assert isinstance(instance, ca::rule::Equal)

@given(instance=ca::rule::Greater_strategy)
@settings(max_examples=50)
def test_ca::rule::greater_instantiation(instance):
    assert isinstance(instance, ca::rule::Greater)

@given(instance=ca::rule::Or_strategy)
@settings(max_examples=50)
def test_ca::rule::or_instantiation(instance):
    assert isinstance(instance, ca::rule::Or)

@given(instance=ca::rule::Minus_strategy)
@settings(max_examples=50)
def test_ca::rule::minus_instantiation(instance):
    assert isinstance(instance, ca::rule::Minus)

@given(instance=ca::rule::Lower_strategy)
@settings(max_examples=50)
def test_ca::rule::lower_instantiation(instance):
    assert isinstance(instance, ca::rule::Lower)

@given(instance=ca::rule::Mult_strategy)
@settings(max_examples=50)
def test_ca::rule::mult_instantiation(instance):
    assert isinstance(instance, ca::rule::Mult)

@given(instance=ca::rule::And_strategy)
@settings(max_examples=50)
def test_ca::rule::and_instantiation(instance):
    assert isinstance(instance, ca::rule::And)

@given(instance=ca::rule::Mod_strategy)
@settings(max_examples=50)
def test_ca::rule::mod_instantiation(instance):
    assert isinstance(instance, ca::rule::Mod)

@given(instance=ca::rule::Div_strategy)
@settings(max_examples=50)
def test_ca::rule::div_instantiation(instance):
    assert isinstance(instance, ca::rule::Div)

@given(instance=ca::rule::Add_strategy)
@settings(max_examples=50)
def test_ca::rule::add_instantiation(instance):
    assert isinstance(instance, ca::rule::Add)

@given(instance=NeighborsExpression_strategy)
@settings(max_examples=50)
def test_neighborsexpression_instantiation(instance):
    assert isinstance(instance, NeighborsExpression)

@given(instance=ca::rule::Size_strategy)
@settings(max_examples=50)
def test_ca::rule::size_instantiation(instance):
    assert isinstance(instance, ca::rule::Size)

@given(instance=ca::rule::Min_strategy)
@settings(max_examples=50)
def test_ca::rule::min_instantiation(instance):
    assert isinstance(instance, ca::rule::Min)

@given(instance=ca::rule::Sum_strategy)
@settings(max_examples=50)
def test_ca::rule::sum_instantiation(instance):
    assert isinstance(instance, ca::rule::Sum)

@given(instance=ca::rule::Max_strategy)
@settings(max_examples=50)
def test_ca::rule::max_instantiation(instance):
    assert isinstance(instance, ca::rule::Max)

@given(instance=ca::rule::PopulationRange_strategy)
@settings(max_examples=50)
def test_ca::rule::populationrange_instantiation(instance):
    assert isinstance(instance, ca::rule::PopulationRange)

@given(instance=ca::rule::PopulationRange_strategy)
def test_ca::rule::populationrange_upperRange_type(instance):
    assert isinstance(instance.upperRange, int)


@given(instance=ca::rule::PopulationRange_strategy)
def test_ca::rule::populationrange_upperRange_setter(instance):
    original = instance.upperRange
    instance.upperRange = original
    assert instance.upperRange == original

@given(instance=ca::rule::PopulationRange_strategy)
def test_ca::rule::populationrange_lowerRange_type(instance):
    assert isinstance(instance.lowerRange, int)


@given(instance=ca::rule::PopulationRange_strategy)
def test_ca::rule::populationrange_lowerRange_setter(instance):
    original = instance.lowerRange
    instance.lowerRange = original
    assert instance.lowerRange == original

@given(instance=ca::rule::IntegerExpression_strategy)
@settings(max_examples=50)
def test_ca::rule::integerexpression_instantiation(instance):
    assert isinstance(instance, ca::rule::IntegerExpression)

@given(instance=ca::rule::Rule_strategy)
@settings(max_examples=50)
def test_ca::rule::rule_instantiation(instance):
    assert isinstance(instance, ca::rule::Rule)
