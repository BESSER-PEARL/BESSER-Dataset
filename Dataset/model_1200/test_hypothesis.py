import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PrimitiveExp,
    oCLlite_StringLiteralExp,
    oCLlite_UnlimitedNaturalLiteralExp,
    oCLlite_InvalidLiteralExp,
    oCLlite_BooleanLiteralExp,
    oCLlite_NumberLiteralExp,
    oCLlite_TuplePart,
    oCLlite_MapElement,
    CollectionExp,
    oCLlite_OrderedSetExp,
    oCLlite_SequenceExp,
    oCLlite_SetExp,
    oCLlite_BagExp,
    OclLExpression,
    oCLlite_PrimitiveExp,
    oCLlite_ComOpCallExp,
    oCLlite_IterateExp,
    oCLlite_IteratorExp,
    oCLlite_LambdaExp,
    oCLlite_TupleExp,
    oCLlite_OperationCall,
    oCLlite_ElseIfThenExp,
    oCLlite_NavigationOrAttributeCall,
    oCLlite_BoolOpCallExp,
    oCLlite_NavigationExp,
    oCLlite_NestedExp,
    oCLlite_MulOpCallExp,
    oCLlite_SelfExp,
    oCLlite_EqOpCallExp,
    oCLlite_MapExp,
    oCLlite_AddOpCallExp,
    oCLlite_CollectionOpCallExp,
    oCLlite_CollectionExp,
    OclLType,
    oCLlite_IntegerType,
    oCLlite_BooleanType,
    oCLlite_MapType,
    oCLlite_BagType,
    oCLlite_LambdaType,
    oCLlite_StringType,
    oCLlite_SequenceType,
    oCLlite_RealType,
    oCLlite_EnvType,
    oCLlite_OclLAnyType,
    oCLlite_TupleType,
    oCLlite_OrderedSetType,
    oCLlite_SetType,
    oCLlite_OclLModelElementExp,
    oCLlite_IfExp,
    oCLlite_NullLiteralExp,
    oCLlite_OclLExpression,
    ModuleElement,
    oCLlite_Query,
    oCLlite_URI_,
    oCLlite_ModuleElement,
    oCLlite_Import,
    oCLlite_OclLModel,
    oCLlite_Module,
    oCLlite_OclLType,
    oCLlite_Iterator,
    oCLlite_LocalVariable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_StringLiteralExp)


def test_ocllite_stringliteralexp_constructor_exists():
    assert callable(oCLlite_StringLiteralExp.__init__)


def test_ocllite_stringliteralexp_constructor_args():
    sig = inspect.signature(oCLlite_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "segments" in params, "Missing parameter 'segments'"

def test_ocllite_stringliteralexp_has_segments():
    assert hasattr(oCLlite_StringLiteralExp, "segments")
    descriptor = None
    for klass in oCLlite_StringLiteralExp.__mro__:
        if "segments" in klass.__dict__:
            descriptor = klass.__dict__["segments"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_unlimitednaturalliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_UnlimitedNaturalLiteralExp)


def test_ocllite_unlimitednaturalliteralexp_constructor_exists():
    assert callable(oCLlite_UnlimitedNaturalLiteralExp.__init__)


def test_ocllite_unlimitednaturalliteralexp_constructor_args():
    sig = inspect.signature(oCLlite_UnlimitedNaturalLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_InvalidLiteralExp)


def test_ocllite_invalidliteralexp_constructor_exists():
    assert callable(oCLlite_InvalidLiteralExp.__init__)


def test_ocllite_invalidliteralexp_constructor_args():
    sig = inspect.signature(oCLlite_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_BooleanLiteralExp)


def test_ocllite_booleanliteralexp_constructor_exists():
    assert callable(oCLlite_BooleanLiteralExp.__init__)


def test_ocllite_booleanliteralexp_constructor_args():
    sig = inspect.signature(oCLlite_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_ocllite_booleanliteralexp_has_symbol():
    assert hasattr(oCLlite_BooleanLiteralExp, "symbol")
    descriptor = None
    for klass in oCLlite_BooleanLiteralExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_numberliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_NumberLiteralExp)


def test_ocllite_numberliteralexp_constructor_exists():
    assert callable(oCLlite_NumberLiteralExp.__init__)


def test_ocllite_numberliteralexp_constructor_args():
    sig = inspect.signature(oCLlite_NumberLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_ocllite_numberliteralexp_has_symbol():
    assert hasattr(oCLlite_NumberLiteralExp, "symbol")
    descriptor = None
    for klass in oCLlite_NumberLiteralExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_tuplepart_is_not_abstract():
    assert not inspect.isabstract(oCLlite_TuplePart)


def test_ocllite_tuplepart_constructor_exists():
    assert callable(oCLlite_TuplePart.__init__)


def test_ocllite_tuplepart_constructor_args():
    sig = inspect.signature(oCLlite_TuplePart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_tuplepart_has_name():
    assert hasattr(oCLlite_TuplePart, "name")
    descriptor = None
    for klass in oCLlite_TuplePart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_mapelement_is_not_abstract():
    assert not inspect.isabstract(oCLlite_MapElement)


def test_ocllite_mapelement_constructor_exists():
    assert callable(oCLlite_MapElement.__init__)


def test_ocllite_mapelement_constructor_args():
    sig = inspect.signature(oCLlite_MapElement.__init__)
    params = list(sig.parameters.keys())



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OrderedSetExp)


def test_ocllite_orderedsetexp_constructor_exists():
    assert callable(oCLlite_OrderedSetExp.__init__)


def test_ocllite_orderedsetexp_constructor_args():
    sig = inspect.signature(oCLlite_OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_sequenceexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_SequenceExp)


def test_ocllite_sequenceexp_constructor_exists():
    assert callable(oCLlite_SequenceExp.__init__)


def test_ocllite_sequenceexp_constructor_args():
    sig = inspect.signature(oCLlite_SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_setexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_SetExp)


def test_ocllite_setexp_constructor_exists():
    assert callable(oCLlite_SetExp.__init__)


def test_ocllite_setexp_constructor_args():
    sig = inspect.signature(oCLlite_SetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_bagexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_BagExp)


def test_ocllite_bagexp_constructor_exists():
    assert callable(oCLlite_BagExp.__init__)


def test_ocllite_bagexp_constructor_args():
    sig = inspect.signature(oCLlite_BagExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllexpression_is_not_abstract():
    assert not inspect.isabstract(OclLExpression)


def test_ocllexpression_constructor_exists():
    assert callable(OclLExpression.__init__)


def test_ocllexpression_constructor_args():
    sig = inspect.signature(OclLExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_PrimitiveExp)


def test_ocllite_primitiveexp_constructor_exists():
    assert callable(oCLlite_PrimitiveExp.__init__)


def test_ocllite_primitiveexp_constructor_args():
    sig = inspect.signature(oCLlite_PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_comopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_ComOpCallExp)


def test_ocllite_comopcallexp_constructor_exists():
    assert callable(oCLlite_ComOpCallExp.__init__)


def test_ocllite_comopcallexp_constructor_args():
    sig = inspect.signature(oCLlite_ComOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_iterateexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_IterateExp)


def test_ocllite_iterateexp_constructor_exists():
    assert callable(oCLlite_IterateExp.__init__)


def test_ocllite_iterateexp_constructor_args():
    sig = inspect.signature(oCLlite_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_IteratorExp)


def test_ocllite_iteratorexp_constructor_exists():
    assert callable(oCLlite_IteratorExp.__init__)


def test_ocllite_iteratorexp_constructor_args():
    sig = inspect.signature(oCLlite_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_lambdaexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_LambdaExp)


def test_ocllite_lambdaexp_constructor_exists():
    assert callable(oCLlite_LambdaExp.__init__)


def test_ocllite_lambdaexp_constructor_args():
    sig = inspect.signature(oCLlite_LambdaExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_tupleexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_TupleExp)


def test_ocllite_tupleexp_constructor_exists():
    assert callable(oCLlite_TupleExp.__init__)


def test_ocllite_tupleexp_constructor_args():
    sig = inspect.signature(oCLlite_TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_operationcall_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OperationCall)


def test_ocllite_operationcall_constructor_exists():
    assert callable(oCLlite_OperationCall.__init__)


def test_ocllite_operationcall_constructor_args():
    sig = inspect.signature(oCLlite_OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_elseifthenexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_ElseIfThenExp)


def test_ocllite_elseifthenexp_constructor_exists():
    assert callable(oCLlite_ElseIfThenExp.__init__)


def test_ocllite_elseifthenexp_constructor_args():
    sig = inspect.signature(oCLlite_ElseIfThenExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_navigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(oCLlite_NavigationOrAttributeCall)


def test_ocllite_navigationorattributecall_constructor_exists():
    assert callable(oCLlite_NavigationOrAttributeCall.__init__)


def test_ocllite_navigationorattributecall_constructor_args():
    sig = inspect.signature(oCLlite_NavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"

def test_ocllite_navigationorattributecall_has_feature():
    assert hasattr(oCLlite_NavigationOrAttributeCall, "feature")
    descriptor = None
    for klass in oCLlite_NavigationOrAttributeCall.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_boolopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_BoolOpCallExp)


def test_ocllite_boolopcallexp_constructor_exists():
    assert callable(oCLlite_BoolOpCallExp.__init__)


def test_ocllite_boolopcallexp_constructor_args():
    sig = inspect.signature(oCLlite_BoolOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_navigationexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_NavigationExp)


def test_ocllite_navigationexp_constructor_exists():
    assert callable(oCLlite_NavigationExp.__init__)


def test_ocllite_navigationexp_constructor_args():
    sig = inspect.signature(oCLlite_NavigationExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_nestedexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_NestedExp)


def test_ocllite_nestedexp_constructor_exists():
    assert callable(oCLlite_NestedExp.__init__)


def test_ocllite_nestedexp_constructor_args():
    sig = inspect.signature(oCLlite_NestedExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_mulopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_MulOpCallExp)


def test_ocllite_mulopcallexp_constructor_exists():
    assert callable(oCLlite_MulOpCallExp.__init__)


def test_ocllite_mulopcallexp_constructor_args():
    sig = inspect.signature(oCLlite_MulOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_selfexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_SelfExp)


def test_ocllite_selfexp_constructor_exists():
    assert callable(oCLlite_SelfExp.__init__)


def test_ocllite_selfexp_constructor_args():
    sig = inspect.signature(oCLlite_SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_eqopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_EqOpCallExp)


def test_ocllite_eqopcallexp_constructor_exists():
    assert callable(oCLlite_EqOpCallExp.__init__)


def test_ocllite_eqopcallexp_constructor_args():
    sig = inspect.signature(oCLlite_EqOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_mapexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_MapExp)


def test_ocllite_mapexp_constructor_exists():
    assert callable(oCLlite_MapExp.__init__)


def test_ocllite_mapexp_constructor_args():
    sig = inspect.signature(oCLlite_MapExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_addopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_AddOpCallExp)


def test_ocllite_addopcallexp_constructor_exists():
    assert callable(oCLlite_AddOpCallExp.__init__)


def test_ocllite_addopcallexp_constructor_args():
    sig = inspect.signature(oCLlite_AddOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_collectionopcallexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_CollectionOpCallExp)


def test_ocllite_collectionopcallexp_constructor_exists():
    assert callable(oCLlite_CollectionOpCallExp.__init__)


def test_ocllite_collectionopcallexp_constructor_args():
    sig = inspect.signature(oCLlite_CollectionOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_collectionexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_CollectionExp)


def test_ocllite_collectionexp_constructor_exists():
    assert callable(oCLlite_CollectionExp.__init__)


def test_ocllite_collectionexp_constructor_args():
    sig = inspect.signature(oCLlite_CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_oclltype_is_not_abstract():
    assert not inspect.isabstract(OclLType)


def test_oclltype_constructor_exists():
    assert callable(OclLType.__init__)


def test_oclltype_constructor_args():
    sig = inspect.signature(OclLType.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_integertype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_IntegerType)


def test_ocllite_integertype_constructor_exists():
    assert callable(oCLlite_IntegerType.__init__)


def test_ocllite_integertype_constructor_args():
    sig = inspect.signature(oCLlite_IntegerType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_integertype_has_name():
    assert hasattr(oCLlite_IntegerType, "name")
    descriptor = None
    for klass in oCLlite_IntegerType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_booleantype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_BooleanType)


def test_ocllite_booleantype_constructor_exists():
    assert callable(oCLlite_BooleanType.__init__)


def test_ocllite_booleantype_constructor_args():
    sig = inspect.signature(oCLlite_BooleanType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_booleantype_has_name():
    assert hasattr(oCLlite_BooleanType, "name")
    descriptor = None
    for klass in oCLlite_BooleanType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_maptype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_MapType)


def test_ocllite_maptype_constructor_exists():
    assert callable(oCLlite_MapType.__init__)


def test_ocllite_maptype_constructor_args():
    sig = inspect.signature(oCLlite_MapType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_maptype_has_name():
    assert hasattr(oCLlite_MapType, "name")
    descriptor = None
    for klass in oCLlite_MapType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_bagtype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_BagType)


def test_ocllite_bagtype_constructor_exists():
    assert callable(oCLlite_BagType.__init__)


def test_ocllite_bagtype_constructor_args():
    sig = inspect.signature(oCLlite_BagType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_bagtype_has_name():
    assert hasattr(oCLlite_BagType, "name")
    descriptor = None
    for klass in oCLlite_BagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_lambdatype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_LambdaType)


def test_ocllite_lambdatype_constructor_exists():
    assert callable(oCLlite_LambdaType.__init__)


def test_ocllite_lambdatype_constructor_args():
    sig = inspect.signature(oCLlite_LambdaType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_lambdatype_has_name():
    assert hasattr(oCLlite_LambdaType, "name")
    descriptor = None
    for klass in oCLlite_LambdaType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_stringtype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_StringType)


def test_ocllite_stringtype_constructor_exists():
    assert callable(oCLlite_StringType.__init__)


def test_ocllite_stringtype_constructor_args():
    sig = inspect.signature(oCLlite_StringType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_stringtype_has_name():
    assert hasattr(oCLlite_StringType, "name")
    descriptor = None
    for klass in oCLlite_StringType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_sequencetype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_SequenceType)


def test_ocllite_sequencetype_constructor_exists():
    assert callable(oCLlite_SequenceType.__init__)


def test_ocllite_sequencetype_constructor_args():
    sig = inspect.signature(oCLlite_SequenceType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_sequencetype_has_name():
    assert hasattr(oCLlite_SequenceType, "name")
    descriptor = None
    for klass in oCLlite_SequenceType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_realtype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_RealType)


def test_ocllite_realtype_constructor_exists():
    assert callable(oCLlite_RealType.__init__)


def test_ocllite_realtype_constructor_args():
    sig = inspect.signature(oCLlite_RealType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_realtype_has_name():
    assert hasattr(oCLlite_RealType, "name")
    descriptor = None
    for klass in oCLlite_RealType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_envtype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_EnvType)


def test_ocllite_envtype_constructor_exists():
    assert callable(oCLlite_EnvType.__init__)


def test_ocllite_envtype_constructor_args():
    sig = inspect.signature(oCLlite_EnvType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_envtype_has_name():
    assert hasattr(oCLlite_EnvType, "name")
    descriptor = None
    for klass in oCLlite_EnvType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_ocllanytype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OclLAnyType)


def test_ocllite_ocllanytype_constructor_exists():
    assert callable(oCLlite_OclLAnyType.__init__)


def test_ocllite_ocllanytype_constructor_args():
    sig = inspect.signature(oCLlite_OclLAnyType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_ocllanytype_has_name():
    assert hasattr(oCLlite_OclLAnyType, "name")
    descriptor = None
    for klass in oCLlite_OclLAnyType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_tupletype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_TupleType)


def test_ocllite_tupletype_constructor_exists():
    assert callable(oCLlite_TupleType.__init__)


def test_ocllite_tupletype_constructor_args():
    sig = inspect.signature(oCLlite_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OrderedSetType)


def test_ocllite_orderedsettype_constructor_exists():
    assert callable(oCLlite_OrderedSetType.__init__)


def test_ocllite_orderedsettype_constructor_args():
    sig = inspect.signature(oCLlite_OrderedSetType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_orderedsettype_has_name():
    assert hasattr(oCLlite_OrderedSetType, "name")
    descriptor = None
    for klass in oCLlite_OrderedSetType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_settype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_SetType)


def test_ocllite_settype_constructor_exists():
    assert callable(oCLlite_SetType.__init__)


def test_ocllite_settype_constructor_args():
    sig = inspect.signature(oCLlite_SetType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_settype_has_name():
    assert hasattr(oCLlite_SetType, "name")
    descriptor = None
    for klass in oCLlite_SetType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_ocllmodelelementexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OclLModelElementExp)


def test_ocllite_ocllmodelelementexp_constructor_exists():
    assert callable(oCLlite_OclLModelElementExp.__init__)


def test_ocllite_ocllmodelelementexp_constructor_args():
    sig = inspect.signature(oCLlite_OclLModelElementExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_ocllmodelelementexp_has_name():
    assert hasattr(oCLlite_OclLModelElementExp, "name")
    descriptor = None
    for klass in oCLlite_OclLModelElementExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_ifexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_IfExp)


def test_ocllite_ifexp_constructor_exists():
    assert callable(oCLlite_IfExp.__init__)


def test_ocllite_ifexp_constructor_args():
    sig = inspect.signature(oCLlite_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(oCLlite_NullLiteralExp)


def test_ocllite_nullliteralexp_constructor_exists():
    assert callable(oCLlite_NullLiteralExp.__init__)


def test_ocllite_nullliteralexp_constructor_args():
    sig = inspect.signature(oCLlite_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_ocllexpression_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OclLExpression)


def test_ocllite_ocllexpression_constructor_exists():
    assert callable(oCLlite_OclLExpression.__init__)


def test_ocllite_ocllexpression_constructor_args():
    sig = inspect.signature(oCLlite_OclLExpression.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_ocllexpression_has_elements():
    assert hasattr(oCLlite_OclLExpression, "elements")
    descriptor = None
    for klass in oCLlite_OclLExpression.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)

def test_ocllite_ocllexpression_has_name():
    assert hasattr(oCLlite_OclLExpression, "name")
    descriptor = None
    for klass in oCLlite_OclLExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_query_is_not_abstract():
    assert not inspect.isabstract(oCLlite_Query)


def test_ocllite_query_constructor_exists():
    assert callable(oCLlite_Query.__init__)


def test_ocllite_query_constructor_args():
    sig = inspect.signature(oCLlite_Query.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_query_has_name():
    assert hasattr(oCLlite_Query, "name")
    descriptor = None
    for klass in oCLlite_Query.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_uri__is_not_abstract():
    assert not inspect.isabstract(oCLlite_URI_)


def test_ocllite_uri__constructor_exists():
    assert callable(oCLlite_URI_.__init__)


def test_ocllite_uri__constructor_args():
    sig = inspect.signature(oCLlite_URI_.__init__)
    params = list(sig.parameters.keys())
    assert "authority" in params, "Missing parameter 'authority'"
    assert "fragment_" in params, "Missing parameter 'fragment_'"
    assert "scheme" in params, "Missing parameter 'scheme'"

def test_ocllite_uri__has_authority():
    assert hasattr(oCLlite_URI_, "authority")
    descriptor = None
    for klass in oCLlite_URI_.__mro__:
        if "authority" in klass.__dict__:
            descriptor = klass.__dict__["authority"]
            break
    assert isinstance(descriptor, property)

def test_ocllite_uri__has_fragment_():
    assert hasattr(oCLlite_URI_, "fragment_")
    descriptor = None
    for klass in oCLlite_URI_.__mro__:
        if "fragment_" in klass.__dict__:
            descriptor = klass.__dict__["fragment_"]
            break
    assert isinstance(descriptor, property)

def test_ocllite_uri__has_scheme():
    assert hasattr(oCLlite_URI_, "scheme")
    descriptor = None
    for klass in oCLlite_URI_.__mro__:
        if "scheme" in klass.__dict__:
            descriptor = klass.__dict__["scheme"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_moduleelement_is_not_abstract():
    assert not inspect.isabstract(oCLlite_ModuleElement)


def test_ocllite_moduleelement_constructor_exists():
    assert callable(oCLlite_ModuleElement.__init__)


def test_ocllite_moduleelement_constructor_args():
    sig = inspect.signature(oCLlite_ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_import_is_not_abstract():
    assert not inspect.isabstract(oCLlite_Import)


def test_ocllite_import_constructor_exists():
    assert callable(oCLlite_Import.__init__)


def test_ocllite_import_constructor_args():
    sig = inspect.signature(oCLlite_Import.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_import_has_name():
    assert hasattr(oCLlite_Import, "name")
    descriptor = None
    for klass in oCLlite_Import.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_ocllmodel_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OclLModel)


def test_ocllite_ocllmodel_constructor_exists():
    assert callable(oCLlite_OclLModel.__init__)


def test_ocllite_ocllmodel_constructor_args():
    sig = inspect.signature(oCLlite_OclLModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_ocllmodel_has_name():
    assert hasattr(oCLlite_OclLModel, "name")
    descriptor = None
    for klass in oCLlite_OclLModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_module_is_not_abstract():
    assert not inspect.isabstract(oCLlite_Module)


def test_ocllite_module_constructor_exists():
    assert callable(oCLlite_Module.__init__)


def test_ocllite_module_constructor_args():
    sig = inspect.signature(oCLlite_Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_module_has_name():
    assert hasattr(oCLlite_Module, "name")
    descriptor = None
    for klass in oCLlite_Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_oclltype_is_not_abstract():
    assert not inspect.isabstract(oCLlite_OclLType)


def test_ocllite_oclltype_constructor_exists():
    assert callable(oCLlite_OclLType.__init__)


def test_ocllite_oclltype_constructor_args():
    sig = inspect.signature(oCLlite_OclLType.__init__)
    params = list(sig.parameters.keys())



def test_ocllite_iterator_is_not_abstract():
    assert not inspect.isabstract(oCLlite_Iterator)


def test_ocllite_iterator_constructor_exists():
    assert callable(oCLlite_Iterator.__init__)


def test_ocllite_iterator_constructor_args():
    sig = inspect.signature(oCLlite_Iterator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_iterator_has_name():
    assert hasattr(oCLlite_Iterator, "name")
    descriptor = None
    for klass in oCLlite_Iterator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocllite_localvariable_is_not_abstract():
    assert not inspect.isabstract(oCLlite_LocalVariable)


def test_ocllite_localvariable_constructor_exists():
    assert callable(oCLlite_LocalVariable.__init__)


def test_ocllite_localvariable_constructor_args():
    sig = inspect.signature(oCLlite_LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocllite_localvariable_has_name():
    assert hasattr(oCLlite_LocalVariable, "name")
    descriptor = None
    for klass in oCLlite_LocalVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
oCLlite_StringLiteralExp_strategy = st.builds(
    oCLlite_StringLiteralExp,
    segments=
        safe_text
)
oCLlite_UnlimitedNaturalLiteralExp_strategy = st.builds(
    oCLlite_UnlimitedNaturalLiteralExp,
)
oCLlite_InvalidLiteralExp_strategy = st.builds(
    oCLlite_InvalidLiteralExp,
)
oCLlite_BooleanLiteralExp_strategy = st.builds(
    oCLlite_BooleanLiteralExp,
    symbol=
        safe_text
)
oCLlite_NumberLiteralExp_strategy = st.builds(
    oCLlite_NumberLiteralExp,
    symbol=
        st.integers()
)
oCLlite_TuplePart_strategy = st.builds(
    oCLlite_TuplePart,
    name=
        safe_text
)
oCLlite_MapElement_strategy = st.builds(
    oCLlite_MapElement,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
oCLlite_OrderedSetExp_strategy = st.builds(
    oCLlite_OrderedSetExp,
)
oCLlite_SequenceExp_strategy = st.builds(
    oCLlite_SequenceExp,
)
oCLlite_SetExp_strategy = st.builds(
    oCLlite_SetExp,
)
oCLlite_BagExp_strategy = st.builds(
    oCLlite_BagExp,
)
OclLExpression_strategy = st.builds(
    OclLExpression,
)
oCLlite_PrimitiveExp_strategy = st.builds(
    oCLlite_PrimitiveExp,
)
oCLlite_ComOpCallExp_strategy = st.builds(
    oCLlite_ComOpCallExp,
)
oCLlite_IterateExp_strategy = st.builds(
    oCLlite_IterateExp,
)
oCLlite_IteratorExp_strategy = st.builds(
    oCLlite_IteratorExp,
)
oCLlite_LambdaExp_strategy = st.builds(
    oCLlite_LambdaExp,
)
oCLlite_TupleExp_strategy = st.builds(
    oCLlite_TupleExp,
)
oCLlite_OperationCall_strategy = st.builds(
    oCLlite_OperationCall,
)
oCLlite_ElseIfThenExp_strategy = st.builds(
    oCLlite_ElseIfThenExp,
)
oCLlite_NavigationOrAttributeCall_strategy = st.builds(
    oCLlite_NavigationOrAttributeCall,
    feature=
        safe_text
)
oCLlite_BoolOpCallExp_strategy = st.builds(
    oCLlite_BoolOpCallExp,
)
oCLlite_NavigationExp_strategy = st.builds(
    oCLlite_NavigationExp,
)
oCLlite_NestedExp_strategy = st.builds(
    oCLlite_NestedExp,
)
oCLlite_MulOpCallExp_strategy = st.builds(
    oCLlite_MulOpCallExp,
)
oCLlite_SelfExp_strategy = st.builds(
    oCLlite_SelfExp,
)
oCLlite_EqOpCallExp_strategy = st.builds(
    oCLlite_EqOpCallExp,
)
oCLlite_MapExp_strategy = st.builds(
    oCLlite_MapExp,
)
oCLlite_AddOpCallExp_strategy = st.builds(
    oCLlite_AddOpCallExp,
)
oCLlite_CollectionOpCallExp_strategy = st.builds(
    oCLlite_CollectionOpCallExp,
)
oCLlite_CollectionExp_strategy = st.builds(
    oCLlite_CollectionExp,
)
OclLType_strategy = st.builds(
    OclLType,
)
oCLlite_IntegerType_strategy = st.builds(
    oCLlite_IntegerType,
    name=
        safe_text
)
oCLlite_BooleanType_strategy = st.builds(
    oCLlite_BooleanType,
    name=
        safe_text
)
oCLlite_MapType_strategy = st.builds(
    oCLlite_MapType,
    name=
        safe_text
)
oCLlite_BagType_strategy = st.builds(
    oCLlite_BagType,
    name=
        safe_text
)
oCLlite_LambdaType_strategy = st.builds(
    oCLlite_LambdaType,
    name=
        safe_text
)
oCLlite_StringType_strategy = st.builds(
    oCLlite_StringType,
    name=
        safe_text
)
oCLlite_SequenceType_strategy = st.builds(
    oCLlite_SequenceType,
    name=
        safe_text
)
oCLlite_RealType_strategy = st.builds(
    oCLlite_RealType,
    name=
        safe_text
)
oCLlite_EnvType_strategy = st.builds(
    oCLlite_EnvType,
    name=
        safe_text
)
oCLlite_OclLAnyType_strategy = st.builds(
    oCLlite_OclLAnyType,
    name=
        safe_text
)
oCLlite_TupleType_strategy = st.builds(
    oCLlite_TupleType,
)
oCLlite_OrderedSetType_strategy = st.builds(
    oCLlite_OrderedSetType,
    name=
        safe_text
)
oCLlite_SetType_strategy = st.builds(
    oCLlite_SetType,
    name=
        safe_text
)
oCLlite_OclLModelElementExp_strategy = st.builds(
    oCLlite_OclLModelElementExp,
    name=
        safe_text
)
oCLlite_IfExp_strategy = st.builds(
    oCLlite_IfExp,
)
oCLlite_NullLiteralExp_strategy = st.builds(
    oCLlite_NullLiteralExp,
)
oCLlite_OclLExpression_strategy = st.builds(
    oCLlite_OclLExpression,
    elements=
        safe_text,
    name=
        safe_text
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
oCLlite_Query_strategy = st.builds(
    oCLlite_Query,
    name=
        safe_text
)
oCLlite_URI__strategy = st.builds(
    oCLlite_URI_,
    authority=
        safe_text,
    fragment_=
        safe_text,
    scheme=
        safe_text
)
oCLlite_ModuleElement_strategy = st.builds(
    oCLlite_ModuleElement,
)
oCLlite_Import_strategy = st.builds(
    oCLlite_Import,
    name=
        safe_text
)
oCLlite_OclLModel_strategy = st.builds(
    oCLlite_OclLModel,
    name=
        safe_text
)
oCLlite_Module_strategy = st.builds(
    oCLlite_Module,
    name=
        safe_text
)
oCLlite_OclLType_strategy = st.builds(
    oCLlite_OclLType,
)
oCLlite_Iterator_strategy = st.builds(
    oCLlite_Iterator,
    name=
        safe_text
)
oCLlite_LocalVariable_strategy = st.builds(
    oCLlite_LocalVariable,
    name=
        safe_text
)

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=oCLlite_StringLiteralExp_strategy)
@settings(max_examples=50)
def test_ocllite_stringliteralexp_instantiation(instance):
    assert isinstance(instance, oCLlite_StringLiteralExp)



@given(instance=oCLlite_StringLiteralExp_strategy)
def test_ocllite_stringliteralexp_segments_setter(instance):
    original = instance.segments
    instance.segments = original
    assert instance.segments == original

@given(instance=oCLlite_UnlimitedNaturalLiteralExp_strategy)
@settings(max_examples=50)
def test_ocllite_unlimitednaturalliteralexp_instantiation(instance):
    assert isinstance(instance, oCLlite_UnlimitedNaturalLiteralExp)

@given(instance=oCLlite_InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_ocllite_invalidliteralexp_instantiation(instance):
    assert isinstance(instance, oCLlite_InvalidLiteralExp)

@given(instance=oCLlite_BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_ocllite_booleanliteralexp_instantiation(instance):
    assert isinstance(instance, oCLlite_BooleanLiteralExp)



@given(instance=oCLlite_BooleanLiteralExp_strategy)
def test_ocllite_booleanliteralexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=oCLlite_NumberLiteralExp_strategy)
@settings(max_examples=50)
def test_ocllite_numberliteralexp_instantiation(instance):
    assert isinstance(instance, oCLlite_NumberLiteralExp)



@given(instance=oCLlite_NumberLiteralExp_strategy)
def test_ocllite_numberliteralexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=oCLlite_TuplePart_strategy)
@settings(max_examples=50)
def test_ocllite_tuplepart_instantiation(instance):
    assert isinstance(instance, oCLlite_TuplePart)



@given(instance=oCLlite_TuplePart_strategy)
def test_ocllite_tuplepart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_MapElement_strategy)
@settings(max_examples=50)
def test_ocllite_mapelement_instantiation(instance):
    assert isinstance(instance, oCLlite_MapElement)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=oCLlite_OrderedSetExp_strategy)
@settings(max_examples=50)
def test_ocllite_orderedsetexp_instantiation(instance):
    assert isinstance(instance, oCLlite_OrderedSetExp)

@given(instance=oCLlite_SequenceExp_strategy)
@settings(max_examples=50)
def test_ocllite_sequenceexp_instantiation(instance):
    assert isinstance(instance, oCLlite_SequenceExp)

@given(instance=oCLlite_SetExp_strategy)
@settings(max_examples=50)
def test_ocllite_setexp_instantiation(instance):
    assert isinstance(instance, oCLlite_SetExp)

@given(instance=oCLlite_BagExp_strategy)
@settings(max_examples=50)
def test_ocllite_bagexp_instantiation(instance):
    assert isinstance(instance, oCLlite_BagExp)

@given(instance=OclLExpression_strategy)
@settings(max_examples=50)
def test_ocllexpression_instantiation(instance):
    assert isinstance(instance, OclLExpression)

@given(instance=oCLlite_PrimitiveExp_strategy)
@settings(max_examples=50)
def test_ocllite_primitiveexp_instantiation(instance):
    assert isinstance(instance, oCLlite_PrimitiveExp)

@given(instance=oCLlite_ComOpCallExp_strategy)
@settings(max_examples=50)
def test_ocllite_comopcallexp_instantiation(instance):
    assert isinstance(instance, oCLlite_ComOpCallExp)

@given(instance=oCLlite_IterateExp_strategy)
@settings(max_examples=50)
def test_ocllite_iterateexp_instantiation(instance):
    assert isinstance(instance, oCLlite_IterateExp)

@given(instance=oCLlite_IteratorExp_strategy)
@settings(max_examples=50)
def test_ocllite_iteratorexp_instantiation(instance):
    assert isinstance(instance, oCLlite_IteratorExp)

@given(instance=oCLlite_LambdaExp_strategy)
@settings(max_examples=50)
def test_ocllite_lambdaexp_instantiation(instance):
    assert isinstance(instance, oCLlite_LambdaExp)

@given(instance=oCLlite_TupleExp_strategy)
@settings(max_examples=50)
def test_ocllite_tupleexp_instantiation(instance):
    assert isinstance(instance, oCLlite_TupleExp)

@given(instance=oCLlite_OperationCall_strategy)
@settings(max_examples=50)
def test_ocllite_operationcall_instantiation(instance):
    assert isinstance(instance, oCLlite_OperationCall)

@given(instance=oCLlite_ElseIfThenExp_strategy)
@settings(max_examples=50)
def test_ocllite_elseifthenexp_instantiation(instance):
    assert isinstance(instance, oCLlite_ElseIfThenExp)

@given(instance=oCLlite_NavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_ocllite_navigationorattributecall_instantiation(instance):
    assert isinstance(instance, oCLlite_NavigationOrAttributeCall)



@given(instance=oCLlite_NavigationOrAttributeCall_strategy)
def test_ocllite_navigationorattributecall_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=oCLlite_BoolOpCallExp_strategy)
@settings(max_examples=50)
def test_ocllite_boolopcallexp_instantiation(instance):
    assert isinstance(instance, oCLlite_BoolOpCallExp)

@given(instance=oCLlite_NavigationExp_strategy)
@settings(max_examples=50)
def test_ocllite_navigationexp_instantiation(instance):
    assert isinstance(instance, oCLlite_NavigationExp)

@given(instance=oCLlite_NestedExp_strategy)
@settings(max_examples=50)
def test_ocllite_nestedexp_instantiation(instance):
    assert isinstance(instance, oCLlite_NestedExp)

@given(instance=oCLlite_MulOpCallExp_strategy)
@settings(max_examples=50)
def test_ocllite_mulopcallexp_instantiation(instance):
    assert isinstance(instance, oCLlite_MulOpCallExp)

@given(instance=oCLlite_SelfExp_strategy)
@settings(max_examples=50)
def test_ocllite_selfexp_instantiation(instance):
    assert isinstance(instance, oCLlite_SelfExp)

@given(instance=oCLlite_EqOpCallExp_strategy)
@settings(max_examples=50)
def test_ocllite_eqopcallexp_instantiation(instance):
    assert isinstance(instance, oCLlite_EqOpCallExp)

@given(instance=oCLlite_MapExp_strategy)
@settings(max_examples=50)
def test_ocllite_mapexp_instantiation(instance):
    assert isinstance(instance, oCLlite_MapExp)

@given(instance=oCLlite_AddOpCallExp_strategy)
@settings(max_examples=50)
def test_ocllite_addopcallexp_instantiation(instance):
    assert isinstance(instance, oCLlite_AddOpCallExp)

@given(instance=oCLlite_CollectionOpCallExp_strategy)
@settings(max_examples=50)
def test_ocllite_collectionopcallexp_instantiation(instance):
    assert isinstance(instance, oCLlite_CollectionOpCallExp)

@given(instance=oCLlite_CollectionExp_strategy)
@settings(max_examples=50)
def test_ocllite_collectionexp_instantiation(instance):
    assert isinstance(instance, oCLlite_CollectionExp)

@given(instance=OclLType_strategy)
@settings(max_examples=50)
def test_oclltype_instantiation(instance):
    assert isinstance(instance, OclLType)

@given(instance=oCLlite_IntegerType_strategy)
@settings(max_examples=50)
def test_ocllite_integertype_instantiation(instance):
    assert isinstance(instance, oCLlite_IntegerType)



@given(instance=oCLlite_IntegerType_strategy)
def test_ocllite_integertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_BooleanType_strategy)
@settings(max_examples=50)
def test_ocllite_booleantype_instantiation(instance):
    assert isinstance(instance, oCLlite_BooleanType)



@given(instance=oCLlite_BooleanType_strategy)
def test_ocllite_booleantype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_MapType_strategy)
@settings(max_examples=50)
def test_ocllite_maptype_instantiation(instance):
    assert isinstance(instance, oCLlite_MapType)



@given(instance=oCLlite_MapType_strategy)
def test_ocllite_maptype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_BagType_strategy)
@settings(max_examples=50)
def test_ocllite_bagtype_instantiation(instance):
    assert isinstance(instance, oCLlite_BagType)



@given(instance=oCLlite_BagType_strategy)
def test_ocllite_bagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_LambdaType_strategy)
@settings(max_examples=50)
def test_ocllite_lambdatype_instantiation(instance):
    assert isinstance(instance, oCLlite_LambdaType)



@given(instance=oCLlite_LambdaType_strategy)
def test_ocllite_lambdatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_StringType_strategy)
@settings(max_examples=50)
def test_ocllite_stringtype_instantiation(instance):
    assert isinstance(instance, oCLlite_StringType)



@given(instance=oCLlite_StringType_strategy)
def test_ocllite_stringtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_SequenceType_strategy)
@settings(max_examples=50)
def test_ocllite_sequencetype_instantiation(instance):
    assert isinstance(instance, oCLlite_SequenceType)



@given(instance=oCLlite_SequenceType_strategy)
def test_ocllite_sequencetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_RealType_strategy)
@settings(max_examples=50)
def test_ocllite_realtype_instantiation(instance):
    assert isinstance(instance, oCLlite_RealType)



@given(instance=oCLlite_RealType_strategy)
def test_ocllite_realtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_EnvType_strategy)
@settings(max_examples=50)
def test_ocllite_envtype_instantiation(instance):
    assert isinstance(instance, oCLlite_EnvType)



@given(instance=oCLlite_EnvType_strategy)
def test_ocllite_envtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_OclLAnyType_strategy)
@settings(max_examples=50)
def test_ocllite_ocllanytype_instantiation(instance):
    assert isinstance(instance, oCLlite_OclLAnyType)



@given(instance=oCLlite_OclLAnyType_strategy)
def test_ocllite_ocllanytype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_TupleType_strategy)
@settings(max_examples=50)
def test_ocllite_tupletype_instantiation(instance):
    assert isinstance(instance, oCLlite_TupleType)

@given(instance=oCLlite_OrderedSetType_strategy)
@settings(max_examples=50)
def test_ocllite_orderedsettype_instantiation(instance):
    assert isinstance(instance, oCLlite_OrderedSetType)



@given(instance=oCLlite_OrderedSetType_strategy)
def test_ocllite_orderedsettype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_SetType_strategy)
@settings(max_examples=50)
def test_ocllite_settype_instantiation(instance):
    assert isinstance(instance, oCLlite_SetType)



@given(instance=oCLlite_SetType_strategy)
def test_ocllite_settype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_OclLModelElementExp_strategy)
@settings(max_examples=50)
def test_ocllite_ocllmodelelementexp_instantiation(instance):
    assert isinstance(instance, oCLlite_OclLModelElementExp)



@given(instance=oCLlite_OclLModelElementExp_strategy)
def test_ocllite_ocllmodelelementexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_IfExp_strategy)
@settings(max_examples=50)
def test_ocllite_ifexp_instantiation(instance):
    assert isinstance(instance, oCLlite_IfExp)

@given(instance=oCLlite_NullLiteralExp_strategy)
@settings(max_examples=50)
def test_ocllite_nullliteralexp_instantiation(instance):
    assert isinstance(instance, oCLlite_NullLiteralExp)

@given(instance=oCLlite_OclLExpression_strategy)
@settings(max_examples=50)
def test_ocllite_ocllexpression_instantiation(instance):
    assert isinstance(instance, oCLlite_OclLExpression)



@given(instance=oCLlite_OclLExpression_strategy)
def test_ocllite_ocllexpression_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original



@given(instance=oCLlite_OclLExpression_strategy)
def test_ocllite_ocllexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=oCLlite_Query_strategy)
@settings(max_examples=50)
def test_ocllite_query_instantiation(instance):
    assert isinstance(instance, oCLlite_Query)



@given(instance=oCLlite_Query_strategy)
def test_ocllite_query_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_URI__strategy)
@settings(max_examples=50)
def test_ocllite_uri__instantiation(instance):
    assert isinstance(instance, oCLlite_URI_)



@given(instance=oCLlite_URI__strategy)
def test_ocllite_uri__authority_setter(instance):
    original = instance.authority
    instance.authority = original
    assert instance.authority == original



@given(instance=oCLlite_URI__strategy)
def test_ocllite_uri__fragment__setter(instance):
    original = instance.fragment_
    instance.fragment_ = original
    assert instance.fragment_ == original



@given(instance=oCLlite_URI__strategy)
def test_ocllite_uri__scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original

@given(instance=oCLlite_ModuleElement_strategy)
@settings(max_examples=50)
def test_ocllite_moduleelement_instantiation(instance):
    assert isinstance(instance, oCLlite_ModuleElement)

@given(instance=oCLlite_Import_strategy)
@settings(max_examples=50)
def test_ocllite_import_instantiation(instance):
    assert isinstance(instance, oCLlite_Import)



@given(instance=oCLlite_Import_strategy)
def test_ocllite_import_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_OclLModel_strategy)
@settings(max_examples=50)
def test_ocllite_ocllmodel_instantiation(instance):
    assert isinstance(instance, oCLlite_OclLModel)



@given(instance=oCLlite_OclLModel_strategy)
def test_ocllite_ocllmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_Module_strategy)
@settings(max_examples=50)
def test_ocllite_module_instantiation(instance):
    assert isinstance(instance, oCLlite_Module)



@given(instance=oCLlite_Module_strategy)
def test_ocllite_module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_OclLType_strategy)
@settings(max_examples=50)
def test_ocllite_oclltype_instantiation(instance):
    assert isinstance(instance, oCLlite_OclLType)

@given(instance=oCLlite_Iterator_strategy)
@settings(max_examples=50)
def test_ocllite_iterator_instantiation(instance):
    assert isinstance(instance, oCLlite_Iterator)



@given(instance=oCLlite_Iterator_strategy)
def test_ocllite_iterator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oCLlite_LocalVariable_strategy)
@settings(max_examples=50)
def test_ocllite_localvariable_instantiation(instance):
    assert isinstance(instance, oCLlite_LocalVariable)



@given(instance=oCLlite_LocalVariable_strategy)
def test_ocllite_localvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
