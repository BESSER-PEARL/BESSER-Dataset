import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CollectionExp,
    superimposed_SetExp,
    superimposed_OclModel,
    OclType,
    superimposed_OclModelElement,
    NumericExp,
    superimposed_IntegerExp,
    superimposed_RealExp,
    PrimitiveExp,
    superimposed_NumericExp,
    superimposed_BooleanExp,
    superimposed_StringExp,
    VariableDeclaration,
    superimposed_Iterator,
    LoopExp,
    superimposed_IteratorExp,
    OperatorCallExp,
    superimposed_UnaryOperatorCallExp,
    superimposed_BinaryOperatorCallExp,
    OperationCallExp,
    superimposed_CollectionOperationCallExp,
    PropertyCallExp,
    superimposed_LoopExp,
    superimposed_NavigationCallExp,
    superimposed_OperationCallExp,
    OclExpression,
    superimposed_CollectionExp,
    superimposed_PrimitiveExp,
    superimposed_OperatorCallExp,
    superimposed_IfExp,
    superimposed_LetExp,
    superimposed_OclUndefinedExp,
    superimposed_PropertyCallExp,
    superimposed_VariableExp,
    superimposed_OclType,
    superimposed_VariableDeclaration,
    superimposed_OclExpression,
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



def test_superimposed_setexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_SetExp)


def test_superimposed_setexp_constructor_exists():
    assert callable(superimposed_SetExp.__init__)


def test_superimposed_setexp_constructor_args():
    sig = inspect.signature(superimposed_SetExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed_oclmodel_is_not_abstract():
    assert not inspect.isabstract(superimposed_OclModel)


def test_superimposed_oclmodel_constructor_exists():
    assert callable(superimposed_OclModel.__init__)


def test_superimposed_oclmodel_constructor_args():
    sig = inspect.signature(superimposed_OclModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_superimposed_oclmodel_has_name():
    assert hasattr(superimposed_OclModel, "name")
    descriptor = None
    for klass in superimposed_OclModel.__mro__:
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



def test_superimposed_oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(superimposed_OclModelElement)


def test_superimposed_oclmodelelement_constructor_exists():
    assert callable(superimposed_OclModelElement.__init__)


def test_superimposed_oclmodelelement_constructor_args():
    sig = inspect.signature(superimposed_OclModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_superimposed_oclmodelelement_has_name():
    assert hasattr(superimposed_OclModelElement, "name")
    descriptor = None
    for klass in superimposed_OclModelElement.__mro__:
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



def test_superimposed_integerexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_IntegerExp)


def test_superimposed_integerexp_constructor_exists():
    assert callable(superimposed_IntegerExp.__init__)


def test_superimposed_integerexp_constructor_args():
    sig = inspect.signature(superimposed_IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_superimposed_integerexp_has_integerSymbol():
    assert hasattr(superimposed_IntegerExp, "integerSymbol")
    descriptor = None
    for klass in superimposed_IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_superimposed_realexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_RealExp)


def test_superimposed_realexp_constructor_exists():
    assert callable(superimposed_RealExp.__init__)


def test_superimposed_realexp_constructor_args():
    sig = inspect.signature(superimposed_RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_superimposed_realexp_has_realSymbol():
    assert hasattr(superimposed_RealExp, "realSymbol")
    descriptor = None
    for klass in superimposed_RealExp.__mro__:
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



def test_superimposed_numericexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_NumericExp)


def test_superimposed_numericexp_constructor_exists():
    assert callable(superimposed_NumericExp.__init__)


def test_superimposed_numericexp_constructor_args():
    sig = inspect.signature(superimposed_NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed_booleanexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_BooleanExp)


def test_superimposed_booleanexp_constructor_exists():
    assert callable(superimposed_BooleanExp.__init__)


def test_superimposed_booleanexp_constructor_args():
    sig = inspect.signature(superimposed_BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_superimposed_booleanexp_has_booleanSymbol():
    assert hasattr(superimposed_BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in superimposed_BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_superimposed_stringexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_StringExp)


def test_superimposed_stringexp_constructor_exists():
    assert callable(superimposed_StringExp.__init__)


def test_superimposed_stringexp_constructor_args():
    sig = inspect.signature(superimposed_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_superimposed_stringexp_has_stringSymbol():
    assert hasattr(superimposed_StringExp, "stringSymbol")
    descriptor = None
    for klass in superimposed_StringExp.__mro__:
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



def test_superimposed_iterator_is_not_abstract():
    assert not inspect.isabstract(superimposed_Iterator)


def test_superimposed_iterator_constructor_exists():
    assert callable(superimposed_Iterator.__init__)


def test_superimposed_iterator_constructor_args():
    sig = inspect.signature(superimposed_Iterator.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_IteratorExp)


def test_superimposed_iteratorexp_constructor_exists():
    assert callable(superimposed_IteratorExp.__init__)


def test_superimposed_iteratorexp_constructor_args():
    sig = inspect.signature(superimposed_IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_superimposed_iteratorexp_has_name():
    assert hasattr(superimposed_IteratorExp, "name")
    descriptor = None
    for klass in superimposed_IteratorExp.__mro__:
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



def test_superimposed_unaryoperatorcallexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_UnaryOperatorCallExp)


def test_superimposed_unaryoperatorcallexp_constructor_exists():
    assert callable(superimposed_UnaryOperatorCallExp.__init__)


def test_superimposed_unaryoperatorcallexp_constructor_args():
    sig = inspect.signature(superimposed_UnaryOperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed_binaryoperatorcallexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_BinaryOperatorCallExp)


def test_superimposed_binaryoperatorcallexp_constructor_exists():
    assert callable(superimposed_BinaryOperatorCallExp.__init__)


def test_superimposed_binaryoperatorcallexp_constructor_args():
    sig = inspect.signature(superimposed_BinaryOperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed_collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_CollectionOperationCallExp)


def test_superimposed_collectionoperationcallexp_constructor_exists():
    assert callable(superimposed_CollectionOperationCallExp.__init__)


def test_superimposed_collectionoperationcallexp_constructor_args():
    sig = inspect.signature(superimposed_CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed_loopexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_LoopExp)


def test_superimposed_loopexp_constructor_exists():
    assert callable(superimposed_LoopExp.__init__)


def test_superimposed_loopexp_constructor_args():
    sig = inspect.signature(superimposed_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_NavigationCallExp)


def test_superimposed_navigationcallexp_constructor_exists():
    assert callable(superimposed_NavigationCallExp.__init__)


def test_superimposed_navigationcallexp_constructor_args():
    sig = inspect.signature(superimposed_NavigationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_superimposed_navigationcallexp_has_name():
    assert hasattr(superimposed_NavigationCallExp, "name")
    descriptor = None
    for klass in superimposed_NavigationCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_superimposed_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_OperationCallExp)


def test_superimposed_operationcallexp_constructor_exists():
    assert callable(superimposed_OperationCallExp.__init__)


def test_superimposed_operationcallexp_constructor_args():
    sig = inspect.signature(superimposed_OperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_superimposed_operationcallexp_has_name():
    assert hasattr(superimposed_OperationCallExp, "name")
    descriptor = None
    for klass in superimposed_OperationCallExp.__mro__:
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



def test_superimposed_collectionexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_CollectionExp)


def test_superimposed_collectionexp_constructor_exists():
    assert callable(superimposed_CollectionExp.__init__)


def test_superimposed_collectionexp_constructor_args():
    sig = inspect.signature(superimposed_CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_PrimitiveExp)


def test_superimposed_primitiveexp_constructor_exists():
    assert callable(superimposed_PrimitiveExp.__init__)


def test_superimposed_primitiveexp_constructor_args():
    sig = inspect.signature(superimposed_PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_OperatorCallExp)


def test_superimposed_operatorcallexp_constructor_exists():
    assert callable(superimposed_OperatorCallExp.__init__)


def test_superimposed_operatorcallexp_constructor_args():
    sig = inspect.signature(superimposed_OperatorCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_superimposed_operatorcallexp_has_name():
    assert hasattr(superimposed_OperatorCallExp, "name")
    descriptor = None
    for klass in superimposed_OperatorCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_superimposed_ifexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_IfExp)


def test_superimposed_ifexp_constructor_exists():
    assert callable(superimposed_IfExp.__init__)


def test_superimposed_ifexp_constructor_args():
    sig = inspect.signature(superimposed_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed_letexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_LetExp)


def test_superimposed_letexp_constructor_exists():
    assert callable(superimposed_LetExp.__init__)


def test_superimposed_letexp_constructor_args():
    sig = inspect.signature(superimposed_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed_oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_OclUndefinedExp)


def test_superimposed_oclundefinedexp_constructor_exists():
    assert callable(superimposed_OclUndefinedExp.__init__)


def test_superimposed_oclundefinedexp_constructor_args():
    sig = inspect.signature(superimposed_OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_PropertyCallExp)


def test_superimposed_propertycallexp_constructor_exists():
    assert callable(superimposed_PropertyCallExp.__init__)


def test_superimposed_propertycallexp_constructor_args():
    sig = inspect.signature(superimposed_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed_variableexp_is_not_abstract():
    assert not inspect.isabstract(superimposed_VariableExp)


def test_superimposed_variableexp_constructor_exists():
    assert callable(superimposed_VariableExp.__init__)


def test_superimposed_variableexp_constructor_args():
    sig = inspect.signature(superimposed_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_superimposed_ocltype_is_not_abstract():
    assert not inspect.isabstract(superimposed_OclType)


def test_superimposed_ocltype_constructor_exists():
    assert callable(superimposed_OclType.__init__)


def test_superimposed_ocltype_constructor_args():
    sig = inspect.signature(superimposed_OclType.__init__)
    params = list(sig.parameters.keys())



def test_superimposed_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(superimposed_VariableDeclaration)


def test_superimposed_variabledeclaration_constructor_exists():
    assert callable(superimposed_VariableDeclaration.__init__)


def test_superimposed_variabledeclaration_constructor_args():
    sig = inspect.signature(superimposed_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_superimposed_variabledeclaration_has_name():
    assert hasattr(superimposed_VariableDeclaration, "name")
    descriptor = None
    for klass in superimposed_VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_superimposed_oclexpression_is_not_abstract():
    assert not inspect.isabstract(superimposed_OclExpression)


def test_superimposed_oclexpression_constructor_exists():
    assert callable(superimposed_OclExpression.__init__)


def test_superimposed_oclexpression_constructor_args():
    sig = inspect.signature(superimposed_OclExpression.__init__)
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
superimposed_SetExp_strategy = st.builds(
    superimposed_SetExp,
)
superimposed_OclModel_strategy = st.builds(
    superimposed_OclModel,
    name=
        safe_text
)
OclType_strategy = st.builds(
    OclType,
)
superimposed_OclModelElement_strategy = st.builds(
    superimposed_OclModelElement,
    name=
        safe_text
)
NumericExp_strategy = st.builds(
    NumericExp,
)
superimposed_IntegerExp_strategy = st.builds(
    superimposed_IntegerExp,
    integerSymbol=
        safe_text
)
superimposed_RealExp_strategy = st.builds(
    superimposed_RealExp,
    realSymbol=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
superimposed_NumericExp_strategy = st.builds(
    superimposed_NumericExp,
)
superimposed_BooleanExp_strategy = st.builds(
    superimposed_BooleanExp,
    booleanSymbol=
        safe_text
)
superimposed_StringExp_strategy = st.builds(
    superimposed_StringExp,
    stringSymbol=
        safe_text
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
superimposed_Iterator_strategy = st.builds(
    superimposed_Iterator,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
superimposed_IteratorExp_strategy = st.builds(
    superimposed_IteratorExp,
    name=
        safe_text
)
OperatorCallExp_strategy = st.builds(
    OperatorCallExp,
)
superimposed_UnaryOperatorCallExp_strategy = st.builds(
    superimposed_UnaryOperatorCallExp,
)
superimposed_BinaryOperatorCallExp_strategy = st.builds(
    superimposed_BinaryOperatorCallExp,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
superimposed_CollectionOperationCallExp_strategy = st.builds(
    superimposed_CollectionOperationCallExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
superimposed_LoopExp_strategy = st.builds(
    superimposed_LoopExp,
)
superimposed_NavigationCallExp_strategy = st.builds(
    superimposed_NavigationCallExp,
    name=
        safe_text
)
superimposed_OperationCallExp_strategy = st.builds(
    superimposed_OperationCallExp,
    name=
        safe_text
)
OclExpression_strategy = st.builds(
    OclExpression,
)
superimposed_CollectionExp_strategy = st.builds(
    superimposed_CollectionExp,
)
superimposed_PrimitiveExp_strategy = st.builds(
    superimposed_PrimitiveExp,
)
superimposed_OperatorCallExp_strategy = st.builds(
    superimposed_OperatorCallExp,
    name=
        safe_text
)
superimposed_IfExp_strategy = st.builds(
    superimposed_IfExp,
)
superimposed_LetExp_strategy = st.builds(
    superimposed_LetExp,
)
superimposed_OclUndefinedExp_strategy = st.builds(
    superimposed_OclUndefinedExp,
)
superimposed_PropertyCallExp_strategy = st.builds(
    superimposed_PropertyCallExp,
)
superimposed_VariableExp_strategy = st.builds(
    superimposed_VariableExp,
)
superimposed_OclType_strategy = st.builds(
    superimposed_OclType,
)
superimposed_VariableDeclaration_strategy = st.builds(
    superimposed_VariableDeclaration,
    name=
        safe_text
)
superimposed_OclExpression_strategy = st.builds(
    superimposed_OclExpression,
)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=superimposed_SetExp_strategy)
@settings(max_examples=50)
def test_superimposed_setexp_instantiation(instance):
    assert isinstance(instance, superimposed_SetExp)

@given(instance=superimposed_OclModel_strategy)
@settings(max_examples=50)
def test_superimposed_oclmodel_instantiation(instance):
    assert isinstance(instance, superimposed_OclModel)



@given(instance=superimposed_OclModel_strategy)
def test_superimposed_oclmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=superimposed_OclModelElement_strategy)
@settings(max_examples=50)
def test_superimposed_oclmodelelement_instantiation(instance):
    assert isinstance(instance, superimposed_OclModelElement)



@given(instance=superimposed_OclModelElement_strategy)
def test_superimposed_oclmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=superimposed_IntegerExp_strategy)
@settings(max_examples=50)
def test_superimposed_integerexp_instantiation(instance):
    assert isinstance(instance, superimposed_IntegerExp)



@given(instance=superimposed_IntegerExp_strategy)
def test_superimposed_integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=superimposed_RealExp_strategy)
@settings(max_examples=50)
def test_superimposed_realexp_instantiation(instance):
    assert isinstance(instance, superimposed_RealExp)



@given(instance=superimposed_RealExp_strategy)
def test_superimposed_realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=superimposed_NumericExp_strategy)
@settings(max_examples=50)
def test_superimposed_numericexp_instantiation(instance):
    assert isinstance(instance, superimposed_NumericExp)

@given(instance=superimposed_BooleanExp_strategy)
@settings(max_examples=50)
def test_superimposed_booleanexp_instantiation(instance):
    assert isinstance(instance, superimposed_BooleanExp)



@given(instance=superimposed_BooleanExp_strategy)
def test_superimposed_booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=superimposed_StringExp_strategy)
@settings(max_examples=50)
def test_superimposed_stringexp_instantiation(instance):
    assert isinstance(instance, superimposed_StringExp)



@given(instance=superimposed_StringExp_strategy)
def test_superimposed_stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=superimposed_Iterator_strategy)
@settings(max_examples=50)
def test_superimposed_iterator_instantiation(instance):
    assert isinstance(instance, superimposed_Iterator)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=superimposed_IteratorExp_strategy)
@settings(max_examples=50)
def test_superimposed_iteratorexp_instantiation(instance):
    assert isinstance(instance, superimposed_IteratorExp)



@given(instance=superimposed_IteratorExp_strategy)
def test_superimposed_iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OperatorCallExp_strategy)
@settings(max_examples=50)
def test_operatorcallexp_instantiation(instance):
    assert isinstance(instance, OperatorCallExp)

@given(instance=superimposed_UnaryOperatorCallExp_strategy)
@settings(max_examples=50)
def test_superimposed_unaryoperatorcallexp_instantiation(instance):
    assert isinstance(instance, superimposed_UnaryOperatorCallExp)

@given(instance=superimposed_BinaryOperatorCallExp_strategy)
@settings(max_examples=50)
def test_superimposed_binaryoperatorcallexp_instantiation(instance):
    assert isinstance(instance, superimposed_BinaryOperatorCallExp)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=superimposed_CollectionOperationCallExp_strategy)
@settings(max_examples=50)
def test_superimposed_collectionoperationcallexp_instantiation(instance):
    assert isinstance(instance, superimposed_CollectionOperationCallExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=superimposed_LoopExp_strategy)
@settings(max_examples=50)
def test_superimposed_loopexp_instantiation(instance):
    assert isinstance(instance, superimposed_LoopExp)

@given(instance=superimposed_NavigationCallExp_strategy)
@settings(max_examples=50)
def test_superimposed_navigationcallexp_instantiation(instance):
    assert isinstance(instance, superimposed_NavigationCallExp)



@given(instance=superimposed_NavigationCallExp_strategy)
def test_superimposed_navigationcallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=superimposed_OperationCallExp_strategy)
@settings(max_examples=50)
def test_superimposed_operationcallexp_instantiation(instance):
    assert isinstance(instance, superimposed_OperationCallExp)



@given(instance=superimposed_OperationCallExp_strategy)
def test_superimposed_operationcallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=superimposed_CollectionExp_strategy)
@settings(max_examples=50)
def test_superimposed_collectionexp_instantiation(instance):
    assert isinstance(instance, superimposed_CollectionExp)

@given(instance=superimposed_PrimitiveExp_strategy)
@settings(max_examples=50)
def test_superimposed_primitiveexp_instantiation(instance):
    assert isinstance(instance, superimposed_PrimitiveExp)

@given(instance=superimposed_OperatorCallExp_strategy)
@settings(max_examples=50)
def test_superimposed_operatorcallexp_instantiation(instance):
    assert isinstance(instance, superimposed_OperatorCallExp)



@given(instance=superimposed_OperatorCallExp_strategy)
def test_superimposed_operatorcallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=superimposed_IfExp_strategy)
@settings(max_examples=50)
def test_superimposed_ifexp_instantiation(instance):
    assert isinstance(instance, superimposed_IfExp)

@given(instance=superimposed_LetExp_strategy)
@settings(max_examples=50)
def test_superimposed_letexp_instantiation(instance):
    assert isinstance(instance, superimposed_LetExp)

@given(instance=superimposed_OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_superimposed_oclundefinedexp_instantiation(instance):
    assert isinstance(instance, superimposed_OclUndefinedExp)

@given(instance=superimposed_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_superimposed_propertycallexp_instantiation(instance):
    assert isinstance(instance, superimposed_PropertyCallExp)

@given(instance=superimposed_VariableExp_strategy)
@settings(max_examples=50)
def test_superimposed_variableexp_instantiation(instance):
    assert isinstance(instance, superimposed_VariableExp)

@given(instance=superimposed_OclType_strategy)
@settings(max_examples=50)
def test_superimposed_ocltype_instantiation(instance):
    assert isinstance(instance, superimposed_OclType)

@given(instance=superimposed_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_superimposed_variabledeclaration_instantiation(instance):
    assert isinstance(instance, superimposed_VariableDeclaration)



@given(instance=superimposed_VariableDeclaration_strategy)
def test_superimposed_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=superimposed_OclExpression_strategy)
@settings(max_examples=50)
def test_superimposed_oclexpression_instantiation(instance):
    assert isinstance(instance, superimposed_OclExpression)
