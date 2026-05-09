import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CollectionExp,
    superimposed::SetExp,
    superimposed::OclModel,
    OclType,
    superimposed::OclModelElement,
    NumericExp,
    superimposed::IntegerExp,
    superimposed::RealExp,
    PrimitiveExp,
    superimposed::BooleanExp,
    superimposed::NumericExp,
    superimposed::StringExp,
    VariableDeclaration,
    superimposed::Iterator,
    LoopExp,
    superimposed::IteratorExp,
    OperatorCallExp,
    superimposed::UnaryOperatorCallExp,
    superimposed::BinaryOperatorCallExp,
    OperationCallExp,
    superimposed::CollectionOperationCallExp,
    PropertyCallExp,
    superimposed::LoopExp,
    superimposed::NavigationCallExp,
    superimposed::OperationCallExp,
    OclExpression,
    superimposed::IfExp,
    superimposed::LetExp,
    superimposed::OclUndefinedExp,
    superimposed::PrimitiveExp,
    superimposed::CollectionExp,
    superimposed::OperatorCallExp,
    superimposed::PropertyCallExp,
    superimposed::VariableExp,
    superimposed::OclType,
    superimposed::VariableDeclaration,
    superimposed::OclExpression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::setexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::SetExp)


def test_superimposed::setexp_constructor_exists():
    assert callable(superimposed::SetExp.__init__)


def test_superimposed::setexp_constructor_args():
    sig = inspect.signature(superimposed::SetExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::oclmodel_is_not_abstract():
    assert not inspect.isabstract(superimposed::OclModel)


def test_superimposed::oclmodel_constructor_exists():
    assert callable(superimposed::OclModel.__init__)


def test_superimposed::oclmodel_constructor_args():
    sig = inspect.signature(superimposed::OclModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_superimposed::oclmodel_has_name():
    assert hasattr(superimposed::OclModel, "name")
    descriptor = None
    for klass in superimposed::OclModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocltype_is_not_abstract():
    assert not inspect.isabstract(OclType)


def test_ocltype_constructor_exists():
    assert callable(OclType.__init__)


def test_ocltype_constructor_args():
    sig = inspect.signature(OclType.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(superimposed::OclModelElement)


def test_superimposed::oclmodelelement_constructor_exists():
    assert callable(superimposed::OclModelElement.__init__)


def test_superimposed::oclmodelelement_constructor_args():
    sig = inspect.signature(superimposed::OclModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_superimposed::oclmodelelement_has_name():
    assert hasattr(superimposed::OclModelElement, "name")
    descriptor = None
    for klass in superimposed::OclModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::integerexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::IntegerExp)


def test_superimposed::integerexp_constructor_exists():
    assert callable(superimposed::IntegerExp.__init__)


def test_superimposed::integerexp_constructor_args():
    sig = inspect.signature(superimposed::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_superimposed::integerexp_has_integerSymbol():
    assert hasattr(superimposed::IntegerExp, "integerSymbol")
    descriptor = None
    for klass in superimposed::IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_superimposed::realexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::RealExp)


def test_superimposed::realexp_constructor_exists():
    assert callable(superimposed::RealExp.__init__)


def test_superimposed::realexp_constructor_args():
    sig = inspect.signature(superimposed::RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_superimposed::realexp_has_realSymbol():
    assert hasattr(superimposed::RealExp, "realSymbol")
    descriptor = None
    for klass in superimposed::RealExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::booleanexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::BooleanExp)


def test_superimposed::booleanexp_constructor_exists():
    assert callable(superimposed::BooleanExp.__init__)


def test_superimposed::booleanexp_constructor_args():
    sig = inspect.signature(superimposed::BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_superimposed::booleanexp_has_booleanSymbol():
    assert hasattr(superimposed::BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in superimposed::BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_superimposed::numericexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::NumericExp)


def test_superimposed::numericexp_constructor_exists():
    assert callable(superimposed::NumericExp.__init__)


def test_superimposed::numericexp_constructor_args():
    sig = inspect.signature(superimposed::NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::stringexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::StringExp)


def test_superimposed::stringexp_constructor_exists():
    assert callable(superimposed::StringExp.__init__)


def test_superimposed::stringexp_constructor_args():
    sig = inspect.signature(superimposed::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_superimposed::stringexp_has_stringSymbol():
    assert hasattr(superimposed::StringExp, "stringSymbol")
    descriptor = None
    for klass in superimposed::StringExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::iterator_is_not_abstract():
    assert not inspect.isabstract(superimposed::Iterator)


def test_superimposed::iterator_constructor_exists():
    assert callable(superimposed::Iterator.__init__)


def test_superimposed::iterator_constructor_args():
    sig = inspect.signature(superimposed::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::IteratorExp)


def test_superimposed::iteratorexp_constructor_exists():
    assert callable(superimposed::IteratorExp.__init__)


def test_superimposed::iteratorexp_constructor_args():
    sig = inspect.signature(superimposed::IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_superimposed::iteratorexp_has_name():
    assert hasattr(superimposed::IteratorExp, "name")
    descriptor = None
    for klass in superimposed::IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OperatorCallExp)


def test_operatorcallexp_constructor_exists():
    assert callable(OperatorCallExp.__init__)


def test_operatorcallexp_constructor_args():
    sig = inspect.signature(OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::unaryoperatorcallexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::UnaryOperatorCallExp)


def test_superimposed::unaryoperatorcallexp_constructor_exists():
    assert callable(superimposed::UnaryOperatorCallExp.__init__)


def test_superimposed::unaryoperatorcallexp_constructor_args():
    sig = inspect.signature(superimposed::UnaryOperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::binaryoperatorcallexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::BinaryOperatorCallExp)


def test_superimposed::binaryoperatorcallexp_constructor_exists():
    assert callable(superimposed::BinaryOperatorCallExp.__init__)


def test_superimposed::binaryoperatorcallexp_constructor_args():
    sig = inspect.signature(superimposed::BinaryOperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::CollectionOperationCallExp)


def test_superimposed::collectionoperationcallexp_constructor_exists():
    assert callable(superimposed::CollectionOperationCallExp.__init__)


def test_superimposed::collectionoperationcallexp_constructor_args():
    sig = inspect.signature(superimposed::CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::loopexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::LoopExp)


def test_superimposed::loopexp_constructor_exists():
    assert callable(superimposed::LoopExp.__init__)


def test_superimposed::loopexp_constructor_args():
    sig = inspect.signature(superimposed::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::NavigationCallExp)


def test_superimposed::navigationcallexp_constructor_exists():
    assert callable(superimposed::NavigationCallExp.__init__)


def test_superimposed::navigationcallexp_constructor_args():
    sig = inspect.signature(superimposed::NavigationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_superimposed::navigationcallexp_has_name():
    assert hasattr(superimposed::NavigationCallExp, "name")
    descriptor = None
    for klass in superimposed::NavigationCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_superimposed::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::OperationCallExp)


def test_superimposed::operationcallexp_constructor_exists():
    assert callable(superimposed::OperationCallExp.__init__)


def test_superimposed::operationcallexp_constructor_args():
    sig = inspect.signature(superimposed::OperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_superimposed::operationcallexp_has_name():
    assert hasattr(superimposed::OperationCallExp, "name")
    descriptor = None
    for klass in superimposed::OperationCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::ifexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::IfExp)


def test_superimposed::ifexp_constructor_exists():
    assert callable(superimposed::IfExp.__init__)


def test_superimposed::ifexp_constructor_args():
    sig = inspect.signature(superimposed::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::letexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::LetExp)


def test_superimposed::letexp_constructor_exists():
    assert callable(superimposed::LetExp.__init__)


def test_superimposed::letexp_constructor_args():
    sig = inspect.signature(superimposed::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::OclUndefinedExp)


def test_superimposed::oclundefinedexp_constructor_exists():
    assert callable(superimposed::OclUndefinedExp.__init__)


def test_superimposed::oclundefinedexp_constructor_args():
    sig = inspect.signature(superimposed::OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::primitiveexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::PrimitiveExp)


def test_superimposed::primitiveexp_constructor_exists():
    assert callable(superimposed::PrimitiveExp.__init__)


def test_superimposed::primitiveexp_constructor_args():
    sig = inspect.signature(superimposed::PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::collectionexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::CollectionExp)


def test_superimposed::collectionexp_constructor_exists():
    assert callable(superimposed::CollectionExp.__init__)


def test_superimposed::collectionexp_constructor_args():
    sig = inspect.signature(superimposed::CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::OperatorCallExp)


def test_superimposed::operatorcallexp_constructor_exists():
    assert callable(superimposed::OperatorCallExp.__init__)


def test_superimposed::operatorcallexp_constructor_args():
    sig = inspect.signature(superimposed::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_superimposed::operatorcallexp_has_name():
    assert hasattr(superimposed::OperatorCallExp, "name")
    descriptor = None
    for klass in superimposed::OperatorCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_superimposed::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::PropertyCallExp)


def test_superimposed::propertycallexp_constructor_exists():
    assert callable(superimposed::PropertyCallExp.__init__)


def test_superimposed::propertycallexp_constructor_args():
    sig = inspect.signature(superimposed::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::variableexp_is_not_abstract():
    assert not inspect.isabstract(superimposed::VariableExp)


def test_superimposed::variableexp_constructor_exists():
    assert callable(superimposed::VariableExp.__init__)


def test_superimposed::variableexp_constructor_args():
    sig = inspect.signature(superimposed::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::ocltype_is_not_abstract():
    assert not inspect.isabstract(superimposed::OclType)


def test_superimposed::ocltype_constructor_exists():
    assert callable(superimposed::OclType.__init__)


def test_superimposed::ocltype_constructor_args():
    sig = inspect.signature(superimposed::OclType.__init__)
    params = list(sig.parameters.keys())



def test_superimposed::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(superimposed::VariableDeclaration)


def test_superimposed::variabledeclaration_constructor_exists():
    assert callable(superimposed::VariableDeclaration.__init__)


def test_superimposed::variabledeclaration_constructor_args():
    sig = inspect.signature(superimposed::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_superimposed::variabledeclaration_has_name():
    assert hasattr(superimposed::VariableDeclaration, "name")
    descriptor = None
    for klass in superimposed::VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_superimposed::oclexpression_is_not_abstract():
    assert not inspect.isabstract(superimposed::OclExpression)


def test_superimposed::oclexpression_constructor_exists():
    assert callable(superimposed::OclExpression.__init__)


def test_superimposed::oclexpression_constructor_args():
    sig = inspect.signature(superimposed::OclExpression.__init__)
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
CollectionExp_strategy = st.builds(
    CollectionExp,
)
superimposed::SetExp_strategy = st.builds(
    superimposed::SetExp,
)
superimposed::OclModel_strategy = st.builds(
    superimposed::OclModel,
    name=
        safe_text
)
OclType_strategy = st.builds(
    OclType,
)
superimposed::OclModelElement_strategy = st.builds(
    superimposed::OclModelElement,
    name=
        safe_text
)
NumericExp_strategy = st.builds(
    NumericExp,
)
superimposed::IntegerExp_strategy = st.builds(
    superimposed::IntegerExp,
    integerSymbol=
        safe_text
)
superimposed::RealExp_strategy = st.builds(
    superimposed::RealExp,
    realSymbol=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
superimposed::BooleanExp_strategy = st.builds(
    superimposed::BooleanExp,
    booleanSymbol=
        safe_text
)
superimposed::NumericExp_strategy = st.builds(
    superimposed::NumericExp,
)
superimposed::StringExp_strategy = st.builds(
    superimposed::StringExp,
    stringSymbol=
        safe_text
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
superimposed::Iterator_strategy = st.builds(
    superimposed::Iterator,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
superimposed::IteratorExp_strategy = st.builds(
    superimposed::IteratorExp,
    name=
        safe_text
)
OperatorCallExp_strategy = st.builds(
    OperatorCallExp,
)
superimposed::UnaryOperatorCallExp_strategy = st.builds(
    superimposed::UnaryOperatorCallExp,
)
superimposed::BinaryOperatorCallExp_strategy = st.builds(
    superimposed::BinaryOperatorCallExp,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
superimposed::CollectionOperationCallExp_strategy = st.builds(
    superimposed::CollectionOperationCallExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
superimposed::LoopExp_strategy = st.builds(
    superimposed::LoopExp,
)
superimposed::NavigationCallExp_strategy = st.builds(
    superimposed::NavigationCallExp,
    name=
        safe_text
)
superimposed::OperationCallExp_strategy = st.builds(
    superimposed::OperationCallExp,
    name=
        safe_text
)
OclExpression_strategy = st.builds(
    OclExpression,
)
superimposed::IfExp_strategy = st.builds(
    superimposed::IfExp,
)
superimposed::LetExp_strategy = st.builds(
    superimposed::LetExp,
)
superimposed::OclUndefinedExp_strategy = st.builds(
    superimposed::OclUndefinedExp,
)
superimposed::PrimitiveExp_strategy = st.builds(
    superimposed::PrimitiveExp,
)
superimposed::CollectionExp_strategy = st.builds(
    superimposed::CollectionExp,
)
superimposed::OperatorCallExp_strategy = st.builds(
    superimposed::OperatorCallExp,
    name=
        safe_text
)
superimposed::PropertyCallExp_strategy = st.builds(
    superimposed::PropertyCallExp,
)
superimposed::VariableExp_strategy = st.builds(
    superimposed::VariableExp,
)
superimposed::OclType_strategy = st.builds(
    superimposed::OclType,
)
superimposed::VariableDeclaration_strategy = st.builds(
    superimposed::VariableDeclaration,
    name=
        safe_text
)
superimposed::OclExpression_strategy = st.builds(
    superimposed::OclExpression,
)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=superimposed::SetExp_strategy)
@settings(max_examples=50)
def test_superimposed::setexp_instantiation(instance):
    assert isinstance(instance, superimposed::SetExp)

@given(instance=superimposed::OclModel_strategy)
@settings(max_examples=50)
def test_superimposed::oclmodel_instantiation(instance):
    assert isinstance(instance, superimposed::OclModel)

@given(instance=superimposed::OclModel_strategy)
def test_superimposed::oclmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=superimposed::OclModel_strategy)
def test_superimposed::oclmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=superimposed::OclModelElement_strategy)
@settings(max_examples=50)
def test_superimposed::oclmodelelement_instantiation(instance):
    assert isinstance(instance, superimposed::OclModelElement)

@given(instance=superimposed::OclModelElement_strategy)
def test_superimposed::oclmodelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=superimposed::OclModelElement_strategy)
def test_superimposed::oclmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=superimposed::IntegerExp_strategy)
@settings(max_examples=50)
def test_superimposed::integerexp_instantiation(instance):
    assert isinstance(instance, superimposed::IntegerExp)

@given(instance=superimposed::IntegerExp_strategy)
def test_superimposed::integerexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=superimposed::IntegerExp_strategy)
def test_superimposed::integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=superimposed::RealExp_strategy)
@settings(max_examples=50)
def test_superimposed::realexp_instantiation(instance):
    assert isinstance(instance, superimposed::RealExp)

@given(instance=superimposed::RealExp_strategy)
def test_superimposed::realexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=superimposed::RealExp_strategy)
def test_superimposed::realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=superimposed::BooleanExp_strategy)
@settings(max_examples=50)
def test_superimposed::booleanexp_instantiation(instance):
    assert isinstance(instance, superimposed::BooleanExp)

@given(instance=superimposed::BooleanExp_strategy)
def test_superimposed::booleanexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=superimposed::BooleanExp_strategy)
def test_superimposed::booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=superimposed::NumericExp_strategy)
@settings(max_examples=50)
def test_superimposed::numericexp_instantiation(instance):
    assert isinstance(instance, superimposed::NumericExp)

@given(instance=superimposed::StringExp_strategy)
@settings(max_examples=50)
def test_superimposed::stringexp_instantiation(instance):
    assert isinstance(instance, superimposed::StringExp)

@given(instance=superimposed::StringExp_strategy)
def test_superimposed::stringexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=superimposed::StringExp_strategy)
def test_superimposed::stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=superimposed::Iterator_strategy)
@settings(max_examples=50)
def test_superimposed::iterator_instantiation(instance):
    assert isinstance(instance, superimposed::Iterator)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=superimposed::IteratorExp_strategy)
@settings(max_examples=50)
def test_superimposed::iteratorexp_instantiation(instance):
    assert isinstance(instance, superimposed::IteratorExp)

@given(instance=superimposed::IteratorExp_strategy)
def test_superimposed::iteratorexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=superimposed::IteratorExp_strategy)
def test_superimposed::iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OperatorCallExp_strategy)
@settings(max_examples=50)
def test_operatorcallexp_instantiation(instance):
    assert isinstance(instance, OperatorCallExp)

@given(instance=superimposed::UnaryOperatorCallExp_strategy)
@settings(max_examples=50)
def test_superimposed::unaryoperatorcallexp_instantiation(instance):
    assert isinstance(instance, superimposed::UnaryOperatorCallExp)

@given(instance=superimposed::BinaryOperatorCallExp_strategy)
@settings(max_examples=50)
def test_superimposed::binaryoperatorcallexp_instantiation(instance):
    assert isinstance(instance, superimposed::BinaryOperatorCallExp)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=superimposed::CollectionOperationCallExp_strategy)
@settings(max_examples=50)
def test_superimposed::collectionoperationcallexp_instantiation(instance):
    assert isinstance(instance, superimposed::CollectionOperationCallExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=superimposed::LoopExp_strategy)
@settings(max_examples=50)
def test_superimposed::loopexp_instantiation(instance):
    assert isinstance(instance, superimposed::LoopExp)

@given(instance=superimposed::NavigationCallExp_strategy)
@settings(max_examples=50)
def test_superimposed::navigationcallexp_instantiation(instance):
    assert isinstance(instance, superimposed::NavigationCallExp)

@given(instance=superimposed::NavigationCallExp_strategy)
def test_superimposed::navigationcallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=superimposed::NavigationCallExp_strategy)
def test_superimposed::navigationcallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=superimposed::OperationCallExp_strategy)
@settings(max_examples=50)
def test_superimposed::operationcallexp_instantiation(instance):
    assert isinstance(instance, superimposed::OperationCallExp)

@given(instance=superimposed::OperationCallExp_strategy)
def test_superimposed::operationcallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=superimposed::OperationCallExp_strategy)
def test_superimposed::operationcallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=superimposed::IfExp_strategy)
@settings(max_examples=50)
def test_superimposed::ifexp_instantiation(instance):
    assert isinstance(instance, superimposed::IfExp)

@given(instance=superimposed::LetExp_strategy)
@settings(max_examples=50)
def test_superimposed::letexp_instantiation(instance):
    assert isinstance(instance, superimposed::LetExp)

@given(instance=superimposed::OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_superimposed::oclundefinedexp_instantiation(instance):
    assert isinstance(instance, superimposed::OclUndefinedExp)

@given(instance=superimposed::PrimitiveExp_strategy)
@settings(max_examples=50)
def test_superimposed::primitiveexp_instantiation(instance):
    assert isinstance(instance, superimposed::PrimitiveExp)

@given(instance=superimposed::CollectionExp_strategy)
@settings(max_examples=50)
def test_superimposed::collectionexp_instantiation(instance):
    assert isinstance(instance, superimposed::CollectionExp)

@given(instance=superimposed::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_superimposed::operatorcallexp_instantiation(instance):
    assert isinstance(instance, superimposed::OperatorCallExp)

@given(instance=superimposed::OperatorCallExp_strategy)
def test_superimposed::operatorcallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=superimposed::OperatorCallExp_strategy)
def test_superimposed::operatorcallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=superimposed::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_superimposed::propertycallexp_instantiation(instance):
    assert isinstance(instance, superimposed::PropertyCallExp)

@given(instance=superimposed::VariableExp_strategy)
@settings(max_examples=50)
def test_superimposed::variableexp_instantiation(instance):
    assert isinstance(instance, superimposed::VariableExp)

@given(instance=superimposed::OclType_strategy)
@settings(max_examples=50)
def test_superimposed::ocltype_instantiation(instance):
    assert isinstance(instance, superimposed::OclType)

@given(instance=superimposed::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_superimposed::variabledeclaration_instantiation(instance):
    assert isinstance(instance, superimposed::VariableDeclaration)

@given(instance=superimposed::VariableDeclaration_strategy)
def test_superimposed::variabledeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=superimposed::VariableDeclaration_strategy)
def test_superimposed::variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=superimposed::OclExpression_strategy)
@settings(max_examples=50)
def test_superimposed::oclexpression_instantiation(instance):
    assert isinstance(instance, superimposed::OclExpression)
