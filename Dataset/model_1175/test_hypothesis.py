import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    OperationCallExp,
    OCLinEmig_CollectionOperationCallExp,
    OCLinEmig_OperatorCallExp,
    VariableDeclaration,
    OCLinEmig_TuplePart,
    CollectionExp,
    OCLinEmig_SequenceExp,
    OCLinEmig_SetExp,
    OCLinEmig_OrderedSetExp,
    OCLinEmig_BagExp,
    PropertyCallExp,
    OCLinEmig_NavigationOrAttributeCallExp,
    PrimitiveExp,
    OCLinEmig_StringExp,
    OclExpression,
    OCLinEmig_MapExp,
    OCLinEmig_SuperExp,
    OCLinEmig_OclUndefinedExp,
    OCLinEmig_EnumLiteralExp,
    OCLinEmig_TupleExp,
    OCLinEmig_PrimitiveExp,
    OCLinEmig_VariableExp,
    OCLinEmig_OperationCallExp,
    OCLinEmig_LoopExp,
    OCLinEmig_LetExp,
    NumericExp,
    OCLinEmig_IntegerExp,
    OCLinEmig_RealExp,
    OCLinEmig_NumericExp,
    OCLinEmig_BooleanExp,
    LocatedElement,
    OCLinEmig_VariableDeclaration,
    OCLinEmig_MapElement,
    OCLinEmig_OclExpression,
    OCLinEmig_CollectionExp,
    OCLinEmig_PropertyCallExp,
    OCLinEmig_IfExp,
    OCLinEmig_OclType,
    OCLinEmig_Module,
    OCLinEmig_LocatedElement,
    OclFeature,
    OCLinEmig_Operation,
    OCLinEmig_Attribute,
    OCLinEmig_OclFeature,
    OCLinEmig_OclFeatureDefinition,
    CollectionType,
    OCLinEmig_OrderedSetType,
    OCLinEmig_SequenceType,
    OCLinEmig_SetType,
    OCLinEmig_BagType,
    NumericType,
    OCLinEmig_RealType,
    OCLinEmig_IntegerType,
    Primitive,
    OCLinEmig_BooleanType,
    OCLinEmig_NumericType,
    OCLinEmig_StringType,
    OCLinEmig_TupleTypeAttribute,
    OCLinEmig_OclModel,
    OclType,
    OCLinEmig_OclAnyType,
    OCLinEmig_Primitive,
    OCLinEmig_TupleType,
    OCLinEmig_OclModelElement,
    OCLinEmig_CollectionType,
    OCLinEmig_Parameter,
    OCLinEmig_MapType,
    OCLinEmig_OclContextDefinition,
    LoopExp,
    OCLinEmig_IteratorExp,
    OCLinEmig_IterateExp,
    OCLinEmig_Iterator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_CollectionOperationCallExp)


def test_oclinemig_collectionoperationcallexp_constructor_exists():
    assert callable(OCLinEmig_CollectionOperationCallExp.__init__)


def test_oclinemig_collectionoperationcallexp_constructor_args():
    sig = inspect.signature(OCLinEmig_CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_OperatorCallExp)


def test_oclinemig_operatorcallexp_constructor_exists():
    assert callable(OCLinEmig_OperatorCallExp.__init__)


def test_oclinemig_operatorcallexp_constructor_args():
    sig = inspect.signature(OCLinEmig_OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_tuplepart_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_TuplePart)


def test_oclinemig_tuplepart_constructor_exists():
    assert callable(OCLinEmig_TuplePart.__init__)


def test_oclinemig_tuplepart_constructor_args():
    sig = inspect.signature(OCLinEmig_TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_sequenceexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_SequenceExp)


def test_oclinemig_sequenceexp_constructor_exists():
    assert callable(OCLinEmig_SequenceExp.__init__)


def test_oclinemig_sequenceexp_constructor_args():
    sig = inspect.signature(OCLinEmig_SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_setexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_SetExp)


def test_oclinemig_setexp_constructor_exists():
    assert callable(OCLinEmig_SetExp.__init__)


def test_oclinemig_setexp_constructor_args():
    sig = inspect.signature(OCLinEmig_SetExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_OrderedSetExp)


def test_oclinemig_orderedsetexp_constructor_exists():
    assert callable(OCLinEmig_OrderedSetExp.__init__)


def test_oclinemig_orderedsetexp_constructor_args():
    sig = inspect.signature(OCLinEmig_OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_bagexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_BagExp)


def test_oclinemig_bagexp_constructor_exists():
    assert callable(OCLinEmig_BagExp.__init__)


def test_oclinemig_bagexp_constructor_args():
    sig = inspect.signature(OCLinEmig_BagExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_navigationorattributecallexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_NavigationOrAttributeCallExp)


def test_oclinemig_navigationorattributecallexp_constructor_exists():
    assert callable(OCLinEmig_NavigationOrAttributeCallExp.__init__)


def test_oclinemig_navigationorattributecallexp_constructor_args():
    sig = inspect.signature(OCLinEmig_NavigationOrAttributeCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig_navigationorattributecallexp_has_name():
    assert hasattr(OCLinEmig_NavigationOrAttributeCallExp, "name")
    descriptor = None
    for klass in OCLinEmig_NavigationOrAttributeCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_stringexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_StringExp)


def test_oclinemig_stringexp_constructor_exists():
    assert callable(OCLinEmig_StringExp.__init__)


def test_oclinemig_stringexp_constructor_args():
    sig = inspect.signature(OCLinEmig_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_oclinemig_stringexp_has_stringSymbol():
    assert hasattr(OCLinEmig_StringExp, "stringSymbol")
    descriptor = None
    for klass in OCLinEmig_StringExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_mapexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_MapExp)


def test_oclinemig_mapexp_constructor_exists():
    assert callable(OCLinEmig_MapExp.__init__)


def test_oclinemig_mapexp_constructor_args():
    sig = inspect.signature(OCLinEmig_MapExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_superexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_SuperExp)


def test_oclinemig_superexp_constructor_exists():
    assert callable(OCLinEmig_SuperExp.__init__)


def test_oclinemig_superexp_constructor_args():
    sig = inspect.signature(OCLinEmig_SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_OclUndefinedExp)


def test_oclinemig_oclundefinedexp_constructor_exists():
    assert callable(OCLinEmig_OclUndefinedExp.__init__)


def test_oclinemig_oclundefinedexp_constructor_args():
    sig = inspect.signature(OCLinEmig_OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_EnumLiteralExp)


def test_oclinemig_enumliteralexp_constructor_exists():
    assert callable(OCLinEmig_EnumLiteralExp.__init__)


def test_oclinemig_enumliteralexp_constructor_args():
    sig = inspect.signature(OCLinEmig_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig_enumliteralexp_has_name():
    assert hasattr(OCLinEmig_EnumLiteralExp, "name")
    descriptor = None
    for klass in OCLinEmig_EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig_tupleexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_TupleExp)


def test_oclinemig_tupleexp_constructor_exists():
    assert callable(OCLinEmig_TupleExp.__init__)


def test_oclinemig_tupleexp_constructor_args():
    sig = inspect.signature(OCLinEmig_TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_PrimitiveExp)


def test_oclinemig_primitiveexp_constructor_exists():
    assert callable(OCLinEmig_PrimitiveExp.__init__)


def test_oclinemig_primitiveexp_constructor_args():
    sig = inspect.signature(OCLinEmig_PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_variableexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_VariableExp)


def test_oclinemig_variableexp_constructor_exists():
    assert callable(OCLinEmig_VariableExp.__init__)


def test_oclinemig_variableexp_constructor_args():
    sig = inspect.signature(OCLinEmig_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_OperationCallExp)


def test_oclinemig_operationcallexp_constructor_exists():
    assert callable(OCLinEmig_OperationCallExp.__init__)


def test_oclinemig_operationcallexp_constructor_args():
    sig = inspect.signature(OCLinEmig_OperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_oclinemig_operationcallexp_has_operationName():
    assert hasattr(OCLinEmig_OperationCallExp, "operationName")
    descriptor = None
    for klass in OCLinEmig_OperationCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig_loopexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_LoopExp)


def test_oclinemig_loopexp_constructor_exists():
    assert callable(OCLinEmig_LoopExp.__init__)


def test_oclinemig_loopexp_constructor_args():
    sig = inspect.signature(OCLinEmig_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_letexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_LetExp)


def test_oclinemig_letexp_constructor_exists():
    assert callable(OCLinEmig_LetExp.__init__)


def test_oclinemig_letexp_constructor_args():
    sig = inspect.signature(OCLinEmig_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_integerexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_IntegerExp)


def test_oclinemig_integerexp_constructor_exists():
    assert callable(OCLinEmig_IntegerExp.__init__)


def test_oclinemig_integerexp_constructor_args():
    sig = inspect.signature(OCLinEmig_IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_oclinemig_integerexp_has_integerSymbol():
    assert hasattr(OCLinEmig_IntegerExp, "integerSymbol")
    descriptor = None
    for klass in OCLinEmig_IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig_realexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_RealExp)


def test_oclinemig_realexp_constructor_exists():
    assert callable(OCLinEmig_RealExp.__init__)


def test_oclinemig_realexp_constructor_args():
    sig = inspect.signature(OCLinEmig_RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_oclinemig_realexp_has_realSymbol():
    assert hasattr(OCLinEmig_RealExp, "realSymbol")
    descriptor = None
    for klass in OCLinEmig_RealExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig_numericexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_NumericExp)


def test_oclinemig_numericexp_constructor_exists():
    assert callable(OCLinEmig_NumericExp.__init__)


def test_oclinemig_numericexp_constructor_args():
    sig = inspect.signature(OCLinEmig_NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_booleanexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_BooleanExp)


def test_oclinemig_booleanexp_constructor_exists():
    assert callable(OCLinEmig_BooleanExp.__init__)


def test_oclinemig_booleanexp_constructor_args():
    sig = inspect.signature(OCLinEmig_BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_oclinemig_booleanexp_has_booleanSymbol():
    assert hasattr(OCLinEmig_BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in OCLinEmig_BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_VariableDeclaration)


def test_oclinemig_variabledeclaration_constructor_exists():
    assert callable(OCLinEmig_VariableDeclaration.__init__)


def test_oclinemig_variabledeclaration_constructor_args():
    sig = inspect.signature(OCLinEmig_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "varName" in params, "Missing parameter 'varName'"

def test_oclinemig_variabledeclaration_has_id():
    assert hasattr(OCLinEmig_VariableDeclaration, "id")
    descriptor = None
    for klass in OCLinEmig_VariableDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_oclinemig_variabledeclaration_has_varName():
    assert hasattr(OCLinEmig_VariableDeclaration, "varName")
    descriptor = None
    for klass in OCLinEmig_VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig_mapelement_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_MapElement)


def test_oclinemig_mapelement_constructor_exists():
    assert callable(OCLinEmig_MapElement.__init__)


def test_oclinemig_mapelement_constructor_args():
    sig = inspect.signature(OCLinEmig_MapElement.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_OclExpression)


def test_oclinemig_oclexpression_constructor_exists():
    assert callable(OCLinEmig_OclExpression.__init__)


def test_oclinemig_oclexpression_constructor_args():
    sig = inspect.signature(OCLinEmig_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_collectionexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_CollectionExp)


def test_oclinemig_collectionexp_constructor_exists():
    assert callable(OCLinEmig_CollectionExp.__init__)


def test_oclinemig_collectionexp_constructor_args():
    sig = inspect.signature(OCLinEmig_CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_PropertyCallExp)


def test_oclinemig_propertycallexp_constructor_exists():
    assert callable(OCLinEmig_PropertyCallExp.__init__)


def test_oclinemig_propertycallexp_constructor_args():
    sig = inspect.signature(OCLinEmig_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_ifexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_IfExp)


def test_oclinemig_ifexp_constructor_exists():
    assert callable(OCLinEmig_IfExp.__init__)


def test_oclinemig_ifexp_constructor_args():
    sig = inspect.signature(OCLinEmig_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_ocltype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_OclType)


def test_oclinemig_ocltype_constructor_exists():
    assert callable(OCLinEmig_OclType.__init__)


def test_oclinemig_ocltype_constructor_args():
    sig = inspect.signature(OCLinEmig_OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig_ocltype_has_name():
    assert hasattr(OCLinEmig_OclType, "name")
    descriptor = None
    for klass in OCLinEmig_OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig_module_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_Module)


def test_oclinemig_module_constructor_exists():
    assert callable(OCLinEmig_Module.__init__)


def test_oclinemig_module_constructor_args():
    sig = inspect.signature(OCLinEmig_Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig_module_has_name():
    assert hasattr(OCLinEmig_Module, "name")
    descriptor = None
    for klass in OCLinEmig_Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig_locatedelement_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_LocatedElement)


def test_oclinemig_locatedelement_constructor_exists():
    assert callable(OCLinEmig_LocatedElement.__init__)


def test_oclinemig_locatedelement_constructor_args():
    sig = inspect.signature(OCLinEmig_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "location" in params, "Missing parameter 'location'"

def test_oclinemig_locatedelement_has_commentsBefore():
    assert hasattr(OCLinEmig_LocatedElement, "commentsBefore")
    descriptor = None
    for klass in OCLinEmig_LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_oclinemig_locatedelement_has_commentsAfter():
    assert hasattr(OCLinEmig_LocatedElement, "commentsAfter")
    descriptor = None
    for klass in OCLinEmig_LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_oclinemig_locatedelement_has_location():
    assert hasattr(OCLinEmig_LocatedElement, "location")
    descriptor = None
    for klass in OCLinEmig_LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_operation_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_Operation)


def test_oclinemig_operation_constructor_exists():
    assert callable(OCLinEmig_Operation.__init__)


def test_oclinemig_operation_constructor_args():
    sig = inspect.signature(OCLinEmig_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig_operation_has_name():
    assert hasattr(OCLinEmig_Operation, "name")
    descriptor = None
    for klass in OCLinEmig_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig_attribute_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_Attribute)


def test_oclinemig_attribute_constructor_exists():
    assert callable(OCLinEmig_Attribute.__init__)


def test_oclinemig_attribute_constructor_args():
    sig = inspect.signature(OCLinEmig_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig_attribute_has_name():
    assert hasattr(OCLinEmig_Attribute, "name")
    descriptor = None
    for klass in OCLinEmig_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_OclFeature)


def test_oclinemig_oclfeature_constructor_exists():
    assert callable(OCLinEmig_OclFeature.__init__)


def test_oclinemig_oclfeature_constructor_args():
    sig = inspect.signature(OCLinEmig_OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_OclFeatureDefinition)


def test_oclinemig_oclfeaturedefinition_constructor_exists():
    assert callable(OCLinEmig_OclFeatureDefinition.__init__)


def test_oclinemig_oclfeaturedefinition_constructor_args():
    sig = inspect.signature(OCLinEmig_OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_OrderedSetType)


def test_oclinemig_orderedsettype_constructor_exists():
    assert callable(OCLinEmig_OrderedSetType.__init__)


def test_oclinemig_orderedsettype_constructor_args():
    sig = inspect.signature(OCLinEmig_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_sequencetype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_SequenceType)


def test_oclinemig_sequencetype_constructor_exists():
    assert callable(OCLinEmig_SequenceType.__init__)


def test_oclinemig_sequencetype_constructor_args():
    sig = inspect.signature(OCLinEmig_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_settype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_SetType)


def test_oclinemig_settype_constructor_exists():
    assert callable(OCLinEmig_SetType.__init__)


def test_oclinemig_settype_constructor_args():
    sig = inspect.signature(OCLinEmig_SetType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_bagtype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_BagType)


def test_oclinemig_bagtype_constructor_exists():
    assert callable(OCLinEmig_BagType.__init__)


def test_oclinemig_bagtype_constructor_args():
    sig = inspect.signature(OCLinEmig_BagType.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_realtype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_RealType)


def test_oclinemig_realtype_constructor_exists():
    assert callable(OCLinEmig_RealType.__init__)


def test_oclinemig_realtype_constructor_args():
    sig = inspect.signature(OCLinEmig_RealType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_integertype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_IntegerType)


def test_oclinemig_integertype_constructor_exists():
    assert callable(OCLinEmig_IntegerType.__init__)


def test_oclinemig_integertype_constructor_args():
    sig = inspect.signature(OCLinEmig_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_booleantype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_BooleanType)


def test_oclinemig_booleantype_constructor_exists():
    assert callable(OCLinEmig_BooleanType.__init__)


def test_oclinemig_booleantype_constructor_args():
    sig = inspect.signature(OCLinEmig_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_numerictype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_NumericType)


def test_oclinemig_numerictype_constructor_exists():
    assert callable(OCLinEmig_NumericType.__init__)


def test_oclinemig_numerictype_constructor_args():
    sig = inspect.signature(OCLinEmig_NumericType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_stringtype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_StringType)


def test_oclinemig_stringtype_constructor_exists():
    assert callable(OCLinEmig_StringType.__init__)


def test_oclinemig_stringtype_constructor_args():
    sig = inspect.signature(OCLinEmig_StringType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_TupleTypeAttribute)


def test_oclinemig_tupletypeattribute_constructor_exists():
    assert callable(OCLinEmig_TupleTypeAttribute.__init__)


def test_oclinemig_tupletypeattribute_constructor_args():
    sig = inspect.signature(OCLinEmig_TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig_tupletypeattribute_has_name():
    assert hasattr(OCLinEmig_TupleTypeAttribute, "name")
    descriptor = None
    for klass in OCLinEmig_TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig_oclmodel_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_OclModel)


def test_oclinemig_oclmodel_constructor_exists():
    assert callable(OCLinEmig_OclModel.__init__)


def test_oclinemig_oclmodel_constructor_args():
    sig = inspect.signature(OCLinEmig_OclModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig_oclmodel_has_name():
    assert hasattr(OCLinEmig_OclModel, "name")
    descriptor = None
    for klass in OCLinEmig_OclModel.__mro__:
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



def test_oclinemig_oclanytype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_OclAnyType)


def test_oclinemig_oclanytype_constructor_exists():
    assert callable(OCLinEmig_OclAnyType.__init__)


def test_oclinemig_oclanytype_constructor_args():
    sig = inspect.signature(OCLinEmig_OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_primitive_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_Primitive)


def test_oclinemig_primitive_constructor_exists():
    assert callable(OCLinEmig_Primitive.__init__)


def test_oclinemig_primitive_constructor_args():
    sig = inspect.signature(OCLinEmig_Primitive.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_tupletype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_TupleType)


def test_oclinemig_tupletype_constructor_exists():
    assert callable(OCLinEmig_TupleType.__init__)


def test_oclinemig_tupletype_constructor_args():
    sig = inspect.signature(OCLinEmig_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_OclModelElement)


def test_oclinemig_oclmodelelement_constructor_exists():
    assert callable(OCLinEmig_OclModelElement.__init__)


def test_oclinemig_oclmodelelement_constructor_args():
    sig = inspect.signature(OCLinEmig_OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_collectiontype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_CollectionType)


def test_oclinemig_collectiontype_constructor_exists():
    assert callable(OCLinEmig_CollectionType.__init__)


def test_oclinemig_collectiontype_constructor_args():
    sig = inspect.signature(OCLinEmig_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_parameter_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_Parameter)


def test_oclinemig_parameter_constructor_exists():
    assert callable(OCLinEmig_Parameter.__init__)


def test_oclinemig_parameter_constructor_args():
    sig = inspect.signature(OCLinEmig_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_maptype_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_MapType)


def test_oclinemig_maptype_constructor_exists():
    assert callable(OCLinEmig_MapType.__init__)


def test_oclinemig_maptype_constructor_args():
    sig = inspect.signature(OCLinEmig_MapType.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_OclContextDefinition)


def test_oclinemig_oclcontextdefinition_constructor_exists():
    assert callable(OCLinEmig_OclContextDefinition.__init__)


def test_oclinemig_oclcontextdefinition_constructor_args():
    sig = inspect.signature(OCLinEmig_OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_IteratorExp)


def test_oclinemig_iteratorexp_constructor_exists():
    assert callable(OCLinEmig_IteratorExp.__init__)


def test_oclinemig_iteratorexp_constructor_args():
    sig = inspect.signature(OCLinEmig_IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinemig_iteratorexp_has_name():
    assert hasattr(OCLinEmig_IteratorExp, "name")
    descriptor = None
    for klass in OCLinEmig_IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinemig_iterateexp_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_IterateExp)


def test_oclinemig_iterateexp_constructor_exists():
    assert callable(OCLinEmig_IterateExp.__init__)


def test_oclinemig_iterateexp_constructor_args():
    sig = inspect.signature(OCLinEmig_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_oclinemig_iterator_is_not_abstract():
    assert not inspect.isabstract(OCLinEmig_Iterator)


def test_oclinemig_iterator_constructor_exists():
    assert callable(OCLinEmig_Iterator.__init__)


def test_oclinemig_iterator_constructor_args():
    sig = inspect.signature(OCLinEmig_Iterator.__init__)
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
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
OCLinEmig_CollectionOperationCallExp_strategy = st.builds(
    OCLinEmig_CollectionOperationCallExp,
)
OCLinEmig_OperatorCallExp_strategy = st.builds(
    OCLinEmig_OperatorCallExp,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
OCLinEmig_TuplePart_strategy = st.builds(
    OCLinEmig_TuplePart,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
OCLinEmig_SequenceExp_strategy = st.builds(
    OCLinEmig_SequenceExp,
)
OCLinEmig_SetExp_strategy = st.builds(
    OCLinEmig_SetExp,
)
OCLinEmig_OrderedSetExp_strategy = st.builds(
    OCLinEmig_OrderedSetExp,
)
OCLinEmig_BagExp_strategy = st.builds(
    OCLinEmig_BagExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
OCLinEmig_NavigationOrAttributeCallExp_strategy = st.builds(
    OCLinEmig_NavigationOrAttributeCallExp,
    name=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
OCLinEmig_StringExp_strategy = st.builds(
    OCLinEmig_StringExp,
    stringSymbol=
        safe_text
)
OclExpression_strategy = st.builds(
    OclExpression,
)
OCLinEmig_MapExp_strategy = st.builds(
    OCLinEmig_MapExp,
)
OCLinEmig_SuperExp_strategy = st.builds(
    OCLinEmig_SuperExp,
)
OCLinEmig_OclUndefinedExp_strategy = st.builds(
    OCLinEmig_OclUndefinedExp,
)
OCLinEmig_EnumLiteralExp_strategy = st.builds(
    OCLinEmig_EnumLiteralExp,
    name=
        safe_text
)
OCLinEmig_TupleExp_strategy = st.builds(
    OCLinEmig_TupleExp,
)
OCLinEmig_PrimitiveExp_strategy = st.builds(
    OCLinEmig_PrimitiveExp,
)
OCLinEmig_VariableExp_strategy = st.builds(
    OCLinEmig_VariableExp,
)
OCLinEmig_OperationCallExp_strategy = st.builds(
    OCLinEmig_OperationCallExp,
    operationName=
        safe_text
)
OCLinEmig_LoopExp_strategy = st.builds(
    OCLinEmig_LoopExp,
)
OCLinEmig_LetExp_strategy = st.builds(
    OCLinEmig_LetExp,
)
NumericExp_strategy = st.builds(
    NumericExp,
)
OCLinEmig_IntegerExp_strategy = st.builds(
    OCLinEmig_IntegerExp,
    integerSymbol=
        safe_text
)
OCLinEmig_RealExp_strategy = st.builds(
    OCLinEmig_RealExp,
    realSymbol=
        safe_text
)
OCLinEmig_NumericExp_strategy = st.builds(
    OCLinEmig_NumericExp,
)
OCLinEmig_BooleanExp_strategy = st.builds(
    OCLinEmig_BooleanExp,
    booleanSymbol=
        safe_text
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
OCLinEmig_VariableDeclaration_strategy = st.builds(
    OCLinEmig_VariableDeclaration,
    id=
        safe_text,
    varName=
        safe_text
)
OCLinEmig_MapElement_strategy = st.builds(
    OCLinEmig_MapElement,
)
OCLinEmig_OclExpression_strategy = st.builds(
    OCLinEmig_OclExpression,
)
OCLinEmig_CollectionExp_strategy = st.builds(
    OCLinEmig_CollectionExp,
)
OCLinEmig_PropertyCallExp_strategy = st.builds(
    OCLinEmig_PropertyCallExp,
)
OCLinEmig_IfExp_strategy = st.builds(
    OCLinEmig_IfExp,
)
OCLinEmig_OclType_strategy = st.builds(
    OCLinEmig_OclType,
    name=
        safe_text
)
OCLinEmig_Module_strategy = st.builds(
    OCLinEmig_Module,
    name=
        safe_text
)
OCLinEmig_LocatedElement_strategy = st.builds(
    OCLinEmig_LocatedElement,
    commentsBefore=
        safe_text,
    commentsAfter=
        safe_text,
    location=
        safe_text
)
OclFeature_strategy = st.builds(
    OclFeature,
)
OCLinEmig_Operation_strategy = st.builds(
    OCLinEmig_Operation,
    name=
        safe_text
)
OCLinEmig_Attribute_strategy = st.builds(
    OCLinEmig_Attribute,
    name=
        safe_text
)
OCLinEmig_OclFeature_strategy = st.builds(
    OCLinEmig_OclFeature,
)
OCLinEmig_OclFeatureDefinition_strategy = st.builds(
    OCLinEmig_OclFeatureDefinition,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
OCLinEmig_OrderedSetType_strategy = st.builds(
    OCLinEmig_OrderedSetType,
)
OCLinEmig_SequenceType_strategy = st.builds(
    OCLinEmig_SequenceType,
)
OCLinEmig_SetType_strategy = st.builds(
    OCLinEmig_SetType,
)
OCLinEmig_BagType_strategy = st.builds(
    OCLinEmig_BagType,
)
NumericType_strategy = st.builds(
    NumericType,
)
OCLinEmig_RealType_strategy = st.builds(
    OCLinEmig_RealType,
)
OCLinEmig_IntegerType_strategy = st.builds(
    OCLinEmig_IntegerType,
)
Primitive_strategy = st.builds(
    Primitive,
)
OCLinEmig_BooleanType_strategy = st.builds(
    OCLinEmig_BooleanType,
)
OCLinEmig_NumericType_strategy = st.builds(
    OCLinEmig_NumericType,
)
OCLinEmig_StringType_strategy = st.builds(
    OCLinEmig_StringType,
)
OCLinEmig_TupleTypeAttribute_strategy = st.builds(
    OCLinEmig_TupleTypeAttribute,
    name=
        safe_text
)
OCLinEmig_OclModel_strategy = st.builds(
    OCLinEmig_OclModel,
    name=
        safe_text
)
OclType_strategy = st.builds(
    OclType,
)
OCLinEmig_OclAnyType_strategy = st.builds(
    OCLinEmig_OclAnyType,
)
OCLinEmig_Primitive_strategy = st.builds(
    OCLinEmig_Primitive,
)
OCLinEmig_TupleType_strategy = st.builds(
    OCLinEmig_TupleType,
)
OCLinEmig_OclModelElement_strategy = st.builds(
    OCLinEmig_OclModelElement,
)
OCLinEmig_CollectionType_strategy = st.builds(
    OCLinEmig_CollectionType,
)
OCLinEmig_Parameter_strategy = st.builds(
    OCLinEmig_Parameter,
)
OCLinEmig_MapType_strategy = st.builds(
    OCLinEmig_MapType,
)
OCLinEmig_OclContextDefinition_strategy = st.builds(
    OCLinEmig_OclContextDefinition,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
OCLinEmig_IteratorExp_strategy = st.builds(
    OCLinEmig_IteratorExp,
    name=
        safe_text
)
OCLinEmig_IterateExp_strategy = st.builds(
    OCLinEmig_IterateExp,
)
OCLinEmig_Iterator_strategy = st.builds(
    OCLinEmig_Iterator,
)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=OCLinEmig_CollectionOperationCallExp_strategy)
@settings(max_examples=50)
def test_oclinemig_collectionoperationcallexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_CollectionOperationCallExp)

@given(instance=OCLinEmig_OperatorCallExp_strategy)
@settings(max_examples=50)
def test_oclinemig_operatorcallexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_OperatorCallExp)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=OCLinEmig_TuplePart_strategy)
@settings(max_examples=50)
def test_oclinemig_tuplepart_instantiation(instance):
    assert isinstance(instance, OCLinEmig_TuplePart)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=OCLinEmig_SequenceExp_strategy)
@settings(max_examples=50)
def test_oclinemig_sequenceexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_SequenceExp)

@given(instance=OCLinEmig_SetExp_strategy)
@settings(max_examples=50)
def test_oclinemig_setexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_SetExp)

@given(instance=OCLinEmig_OrderedSetExp_strategy)
@settings(max_examples=50)
def test_oclinemig_orderedsetexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_OrderedSetExp)

@given(instance=OCLinEmig_BagExp_strategy)
@settings(max_examples=50)
def test_oclinemig_bagexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_BagExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=OCLinEmig_NavigationOrAttributeCallExp_strategy)
@settings(max_examples=50)
def test_oclinemig_navigationorattributecallexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_NavigationOrAttributeCallExp)



@given(instance=OCLinEmig_NavigationOrAttributeCallExp_strategy)
def test_oclinemig_navigationorattributecallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=OCLinEmig_StringExp_strategy)
@settings(max_examples=50)
def test_oclinemig_stringexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_StringExp)



@given(instance=OCLinEmig_StringExp_strategy)
def test_oclinemig_stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=OCLinEmig_MapExp_strategy)
@settings(max_examples=50)
def test_oclinemig_mapexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_MapExp)

@given(instance=OCLinEmig_SuperExp_strategy)
@settings(max_examples=50)
def test_oclinemig_superexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_SuperExp)

@given(instance=OCLinEmig_OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_oclinemig_oclundefinedexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_OclUndefinedExp)

@given(instance=OCLinEmig_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_oclinemig_enumliteralexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_EnumLiteralExp)



@given(instance=OCLinEmig_EnumLiteralExp_strategy)
def test_oclinemig_enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCLinEmig_TupleExp_strategy)
@settings(max_examples=50)
def test_oclinemig_tupleexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_TupleExp)

@given(instance=OCLinEmig_PrimitiveExp_strategy)
@settings(max_examples=50)
def test_oclinemig_primitiveexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_PrimitiveExp)

@given(instance=OCLinEmig_VariableExp_strategy)
@settings(max_examples=50)
def test_oclinemig_variableexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_VariableExp)

@given(instance=OCLinEmig_OperationCallExp_strategy)
@settings(max_examples=50)
def test_oclinemig_operationcallexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_OperationCallExp)



@given(instance=OCLinEmig_OperationCallExp_strategy)
def test_oclinemig_operationcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=OCLinEmig_LoopExp_strategy)
@settings(max_examples=50)
def test_oclinemig_loopexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_LoopExp)

@given(instance=OCLinEmig_LetExp_strategy)
@settings(max_examples=50)
def test_oclinemig_letexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_LetExp)

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=OCLinEmig_IntegerExp_strategy)
@settings(max_examples=50)
def test_oclinemig_integerexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_IntegerExp)



@given(instance=OCLinEmig_IntegerExp_strategy)
def test_oclinemig_integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=OCLinEmig_RealExp_strategy)
@settings(max_examples=50)
def test_oclinemig_realexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_RealExp)



@given(instance=OCLinEmig_RealExp_strategy)
def test_oclinemig_realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=OCLinEmig_NumericExp_strategy)
@settings(max_examples=50)
def test_oclinemig_numericexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_NumericExp)

@given(instance=OCLinEmig_BooleanExp_strategy)
@settings(max_examples=50)
def test_oclinemig_booleanexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_BooleanExp)



@given(instance=OCLinEmig_BooleanExp_strategy)
def test_oclinemig_booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=OCLinEmig_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_oclinemig_variabledeclaration_instantiation(instance):
    assert isinstance(instance, OCLinEmig_VariableDeclaration)



@given(instance=OCLinEmig_VariableDeclaration_strategy)
def test_oclinemig_variabledeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=OCLinEmig_VariableDeclaration_strategy)
def test_oclinemig_variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=OCLinEmig_MapElement_strategy)
@settings(max_examples=50)
def test_oclinemig_mapelement_instantiation(instance):
    assert isinstance(instance, OCLinEmig_MapElement)

@given(instance=OCLinEmig_OclExpression_strategy)
@settings(max_examples=50)
def test_oclinemig_oclexpression_instantiation(instance):
    assert isinstance(instance, OCLinEmig_OclExpression)

@given(instance=OCLinEmig_CollectionExp_strategy)
@settings(max_examples=50)
def test_oclinemig_collectionexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_CollectionExp)

@given(instance=OCLinEmig_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_oclinemig_propertycallexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_PropertyCallExp)

@given(instance=OCLinEmig_IfExp_strategy)
@settings(max_examples=50)
def test_oclinemig_ifexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_IfExp)

@given(instance=OCLinEmig_OclType_strategy)
@settings(max_examples=50)
def test_oclinemig_ocltype_instantiation(instance):
    assert isinstance(instance, OCLinEmig_OclType)



@given(instance=OCLinEmig_OclType_strategy)
def test_oclinemig_ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCLinEmig_Module_strategy)
@settings(max_examples=50)
def test_oclinemig_module_instantiation(instance):
    assert isinstance(instance, OCLinEmig_Module)



@given(instance=OCLinEmig_Module_strategy)
def test_oclinemig_module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCLinEmig_LocatedElement_strategy)
@settings(max_examples=50)
def test_oclinemig_locatedelement_instantiation(instance):
    assert isinstance(instance, OCLinEmig_LocatedElement)



@given(instance=OCLinEmig_LocatedElement_strategy)
def test_oclinemig_locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original



@given(instance=OCLinEmig_LocatedElement_strategy)
def test_oclinemig_locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original



@given(instance=OCLinEmig_LocatedElement_strategy)
def test_oclinemig_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=OCLinEmig_Operation_strategy)
@settings(max_examples=50)
def test_oclinemig_operation_instantiation(instance):
    assert isinstance(instance, OCLinEmig_Operation)



@given(instance=OCLinEmig_Operation_strategy)
def test_oclinemig_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCLinEmig_Attribute_strategy)
@settings(max_examples=50)
def test_oclinemig_attribute_instantiation(instance):
    assert isinstance(instance, OCLinEmig_Attribute)



@given(instance=OCLinEmig_Attribute_strategy)
def test_oclinemig_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCLinEmig_OclFeature_strategy)
@settings(max_examples=50)
def test_oclinemig_oclfeature_instantiation(instance):
    assert isinstance(instance, OCLinEmig_OclFeature)

@given(instance=OCLinEmig_OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_oclinemig_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, OCLinEmig_OclFeatureDefinition)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=OCLinEmig_OrderedSetType_strategy)
@settings(max_examples=50)
def test_oclinemig_orderedsettype_instantiation(instance):
    assert isinstance(instance, OCLinEmig_OrderedSetType)

@given(instance=OCLinEmig_SequenceType_strategy)
@settings(max_examples=50)
def test_oclinemig_sequencetype_instantiation(instance):
    assert isinstance(instance, OCLinEmig_SequenceType)

@given(instance=OCLinEmig_SetType_strategy)
@settings(max_examples=50)
def test_oclinemig_settype_instantiation(instance):
    assert isinstance(instance, OCLinEmig_SetType)

@given(instance=OCLinEmig_BagType_strategy)
@settings(max_examples=50)
def test_oclinemig_bagtype_instantiation(instance):
    assert isinstance(instance, OCLinEmig_BagType)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=OCLinEmig_RealType_strategy)
@settings(max_examples=50)
def test_oclinemig_realtype_instantiation(instance):
    assert isinstance(instance, OCLinEmig_RealType)

@given(instance=OCLinEmig_IntegerType_strategy)
@settings(max_examples=50)
def test_oclinemig_integertype_instantiation(instance):
    assert isinstance(instance, OCLinEmig_IntegerType)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=OCLinEmig_BooleanType_strategy)
@settings(max_examples=50)
def test_oclinemig_booleantype_instantiation(instance):
    assert isinstance(instance, OCLinEmig_BooleanType)

@given(instance=OCLinEmig_NumericType_strategy)
@settings(max_examples=50)
def test_oclinemig_numerictype_instantiation(instance):
    assert isinstance(instance, OCLinEmig_NumericType)

@given(instance=OCLinEmig_StringType_strategy)
@settings(max_examples=50)
def test_oclinemig_stringtype_instantiation(instance):
    assert isinstance(instance, OCLinEmig_StringType)

@given(instance=OCLinEmig_TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_oclinemig_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, OCLinEmig_TupleTypeAttribute)



@given(instance=OCLinEmig_TupleTypeAttribute_strategy)
def test_oclinemig_tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCLinEmig_OclModel_strategy)
@settings(max_examples=50)
def test_oclinemig_oclmodel_instantiation(instance):
    assert isinstance(instance, OCLinEmig_OclModel)



@given(instance=OCLinEmig_OclModel_strategy)
def test_oclinemig_oclmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=OCLinEmig_OclAnyType_strategy)
@settings(max_examples=50)
def test_oclinemig_oclanytype_instantiation(instance):
    assert isinstance(instance, OCLinEmig_OclAnyType)

@given(instance=OCLinEmig_Primitive_strategy)
@settings(max_examples=50)
def test_oclinemig_primitive_instantiation(instance):
    assert isinstance(instance, OCLinEmig_Primitive)

@given(instance=OCLinEmig_TupleType_strategy)
@settings(max_examples=50)
def test_oclinemig_tupletype_instantiation(instance):
    assert isinstance(instance, OCLinEmig_TupleType)

@given(instance=OCLinEmig_OclModelElement_strategy)
@settings(max_examples=50)
def test_oclinemig_oclmodelelement_instantiation(instance):
    assert isinstance(instance, OCLinEmig_OclModelElement)

@given(instance=OCLinEmig_CollectionType_strategy)
@settings(max_examples=50)
def test_oclinemig_collectiontype_instantiation(instance):
    assert isinstance(instance, OCLinEmig_CollectionType)

@given(instance=OCLinEmig_Parameter_strategy)
@settings(max_examples=50)
def test_oclinemig_parameter_instantiation(instance):
    assert isinstance(instance, OCLinEmig_Parameter)

@given(instance=OCLinEmig_MapType_strategy)
@settings(max_examples=50)
def test_oclinemig_maptype_instantiation(instance):
    assert isinstance(instance, OCLinEmig_MapType)

@given(instance=OCLinEmig_OclContextDefinition_strategy)
@settings(max_examples=50)
def test_oclinemig_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OCLinEmig_OclContextDefinition)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=OCLinEmig_IteratorExp_strategy)
@settings(max_examples=50)
def test_oclinemig_iteratorexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_IteratorExp)



@given(instance=OCLinEmig_IteratorExp_strategy)
def test_oclinemig_iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCLinEmig_IterateExp_strategy)
@settings(max_examples=50)
def test_oclinemig_iterateexp_instantiation(instance):
    assert isinstance(instance, OCLinEmig_IterateExp)

@given(instance=OCLinEmig_Iterator_strategy)
@settings(max_examples=50)
def test_oclinemig_iterator_instantiation(instance):
    assert isinstance(instance, OCLinEmig_Iterator)
