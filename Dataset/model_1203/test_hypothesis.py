import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    OclExpression,
    docl_PrimitiveExp,
    docl_TuplePart,
    docl_OclType,
    docl_Iterator,
    docl_LocalVariable,
    OclType,
    docl_OclModelElementExp,
    ModuleElement,
    docl_Query,
    docl_URI_,
    docl_ModuleElement,
    docl_Import,
    docl_OclExpression,
    docl_OclModel,
    docl_Module,
    docl_NestedExp,
    docl_SelfExp,
    docl_ElseIfThenExp,
    docl_TupleExp,
    docl_LambdaExp,
    docl_OperationCall,
    docl_NavigationOrAttributeCall,
    docl_IterateExp,
    docl_CollectionOpCallExp,
    docl_NavigationExp,
    docl_MulOpCallExp,
    docl_AddOpCallExp,
    docl_IteratorExp,
    docl_BoolOpCallExp,
    docl_StringType,
    docl_BooleanType,
    docl_IntegerType,
    docl_RealType,
    docl_BagType,
    docl_OrderedSetType,
    docl_SequenceType,
    docl_SetType,
    docl_OclAnyType,
    docl_TupleType,
    docl_MapType,
    docl_LambdaType,
    docl_EnvType,
    docl_ComOpCallExp,
    docl_EqOpCallExp,
    docl_IfExp,
    PrimitiveExp,
    docl_StringLiteralExp,
    docl_InvalidLiteralExp,
    docl_NullLiteralExp,
    docl_BooleanLiteralExp,
    docl_NumberLiteralExp,
    docl_UnlimitedNaturalLiteralExp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_docl_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(docl_PrimitiveExp)


def test_docl_primitiveexp_constructor_exists():
    assert callable(docl_PrimitiveExp.__init__)


def test_docl_primitiveexp_constructor_args():
    sig = inspect.signature(docl_PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_tuplepart_is_not_abstract():
    assert not inspect.isabstract(docl_TuplePart)


def test_docl_tuplepart_constructor_exists():
    assert callable(docl_TuplePart.__init__)


def test_docl_tuplepart_constructor_args():
    sig = inspect.signature(docl_TuplePart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_tuplepart_has_name():
    assert hasattr(docl_TuplePart, "name")
    descriptor = None
    for klass in docl_TuplePart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_ocltype_is_not_abstract():
    assert not inspect.isabstract(docl_OclType)


def test_docl_ocltype_constructor_exists():
    assert callable(docl_OclType.__init__)


def test_docl_ocltype_constructor_args():
    sig = inspect.signature(docl_OclType.__init__)
    params = list(sig.parameters.keys())



def test_docl_iterator_is_not_abstract():
    assert not inspect.isabstract(docl_Iterator)


def test_docl_iterator_constructor_exists():
    assert callable(docl_Iterator.__init__)


def test_docl_iterator_constructor_args():
    sig = inspect.signature(docl_Iterator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_iterator_has_name():
    assert hasattr(docl_Iterator, "name")
    descriptor = None
    for klass in docl_Iterator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_localvariable_is_not_abstract():
    assert not inspect.isabstract(docl_LocalVariable)


def test_docl_localvariable_constructor_exists():
    assert callable(docl_LocalVariable.__init__)


def test_docl_localvariable_constructor_args():
    sig = inspect.signature(docl_LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_localvariable_has_name():
    assert hasattr(docl_LocalVariable, "name")
    descriptor = None
    for klass in docl_LocalVariable.__mro__:
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



def test_docl_oclmodelelementexp_is_not_abstract():
    assert not inspect.isabstract(docl_OclModelElementExp)


def test_docl_oclmodelelementexp_constructor_exists():
    assert callable(docl_OclModelElementExp.__init__)


def test_docl_oclmodelelementexp_constructor_args():
    sig = inspect.signature(docl_OclModelElementExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_oclmodelelementexp_has_name():
    assert hasattr(docl_OclModelElementExp, "name")
    descriptor = None
    for klass in docl_OclModelElementExp.__mro__:
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



def test_docl_query_is_not_abstract():
    assert not inspect.isabstract(docl_Query)


def test_docl_query_constructor_exists():
    assert callable(docl_Query.__init__)


def test_docl_query_constructor_args():
    sig = inspect.signature(docl_Query.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_query_has_name():
    assert hasattr(docl_Query, "name")
    descriptor = None
    for klass in docl_Query.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_uri__is_not_abstract():
    assert not inspect.isabstract(docl_URI_)


def test_docl_uri__constructor_exists():
    assert callable(docl_URI_.__init__)


def test_docl_uri__constructor_args():
    sig = inspect.signature(docl_URI_.__init__)
    params = list(sig.parameters.keys())
    assert "authority" in params, "Missing parameter 'authority'"
    assert "fragment_" in params, "Missing parameter 'fragment_'"
    assert "scheme" in params, "Missing parameter 'scheme'"

def test_docl_uri__has_authority():
    assert hasattr(docl_URI_, "authority")
    descriptor = None
    for klass in docl_URI_.__mro__:
        if "authority" in klass.__dict__:
            descriptor = klass.__dict__["authority"]
            break
    assert isinstance(descriptor, property)

def test_docl_uri__has_fragment_():
    assert hasattr(docl_URI_, "fragment_")
    descriptor = None
    for klass in docl_URI_.__mro__:
        if "fragment_" in klass.__dict__:
            descriptor = klass.__dict__["fragment_"]
            break
    assert isinstance(descriptor, property)

def test_docl_uri__has_scheme():
    assert hasattr(docl_URI_, "scheme")
    descriptor = None
    for klass in docl_URI_.__mro__:
        if "scheme" in klass.__dict__:
            descriptor = klass.__dict__["scheme"]
            break
    assert isinstance(descriptor, property)



def test_docl_moduleelement_is_not_abstract():
    assert not inspect.isabstract(docl_ModuleElement)


def test_docl_moduleelement_constructor_exists():
    assert callable(docl_ModuleElement.__init__)


def test_docl_moduleelement_constructor_args():
    sig = inspect.signature(docl_ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_docl_import_is_not_abstract():
    assert not inspect.isabstract(docl_Import)


def test_docl_import_constructor_exists():
    assert callable(docl_Import.__init__)


def test_docl_import_constructor_args():
    sig = inspect.signature(docl_Import.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_import_has_name():
    assert hasattr(docl_Import, "name")
    descriptor = None
    for klass in docl_Import.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(docl_OclExpression)


def test_docl_oclexpression_constructor_exists():
    assert callable(docl_OclExpression.__init__)


def test_docl_oclexpression_constructor_args():
    sig = inspect.signature(docl_OclExpression.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"
    assert "name" in params, "Missing parameter 'name'"

def test_docl_oclexpression_has_elements():
    assert hasattr(docl_OclExpression, "elements")
    descriptor = None
    for klass in docl_OclExpression.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)

def test_docl_oclexpression_has_name():
    assert hasattr(docl_OclExpression, "name")
    descriptor = None
    for klass in docl_OclExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_oclmodel_is_not_abstract():
    assert not inspect.isabstract(docl_OclModel)


def test_docl_oclmodel_constructor_exists():
    assert callable(docl_OclModel.__init__)


def test_docl_oclmodel_constructor_args():
    sig = inspect.signature(docl_OclModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_oclmodel_has_name():
    assert hasattr(docl_OclModel, "name")
    descriptor = None
    for klass in docl_OclModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_module_is_not_abstract():
    assert not inspect.isabstract(docl_Module)


def test_docl_module_constructor_exists():
    assert callable(docl_Module.__init__)


def test_docl_module_constructor_args():
    sig = inspect.signature(docl_Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_module_has_name():
    assert hasattr(docl_Module, "name")
    descriptor = None
    for klass in docl_Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_nestedexp_is_not_abstract():
    assert not inspect.isabstract(docl_NestedExp)


def test_docl_nestedexp_constructor_exists():
    assert callable(docl_NestedExp.__init__)


def test_docl_nestedexp_constructor_args():
    sig = inspect.signature(docl_NestedExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_selfexp_is_not_abstract():
    assert not inspect.isabstract(docl_SelfExp)


def test_docl_selfexp_constructor_exists():
    assert callable(docl_SelfExp.__init__)


def test_docl_selfexp_constructor_args():
    sig = inspect.signature(docl_SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_elseifthenexp_is_not_abstract():
    assert not inspect.isabstract(docl_ElseIfThenExp)


def test_docl_elseifthenexp_constructor_exists():
    assert callable(docl_ElseIfThenExp.__init__)


def test_docl_elseifthenexp_constructor_args():
    sig = inspect.signature(docl_ElseIfThenExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_tupleexp_is_not_abstract():
    assert not inspect.isabstract(docl_TupleExp)


def test_docl_tupleexp_constructor_exists():
    assert callable(docl_TupleExp.__init__)


def test_docl_tupleexp_constructor_args():
    sig = inspect.signature(docl_TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_lambdaexp_is_not_abstract():
    assert not inspect.isabstract(docl_LambdaExp)


def test_docl_lambdaexp_constructor_exists():
    assert callable(docl_LambdaExp.__init__)


def test_docl_lambdaexp_constructor_args():
    sig = inspect.signature(docl_LambdaExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_operationcall_is_not_abstract():
    assert not inspect.isabstract(docl_OperationCall)


def test_docl_operationcall_constructor_exists():
    assert callable(docl_OperationCall.__init__)


def test_docl_operationcall_constructor_args():
    sig = inspect.signature(docl_OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_docl_navigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(docl_NavigationOrAttributeCall)


def test_docl_navigationorattributecall_constructor_exists():
    assert callable(docl_NavigationOrAttributeCall.__init__)


def test_docl_navigationorattributecall_constructor_args():
    sig = inspect.signature(docl_NavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"

def test_docl_navigationorattributecall_has_feature():
    assert hasattr(docl_NavigationOrAttributeCall, "feature")
    descriptor = None
    for klass in docl_NavigationOrAttributeCall.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_docl_iterateexp_is_not_abstract():
    assert not inspect.isabstract(docl_IterateExp)


def test_docl_iterateexp_constructor_exists():
    assert callable(docl_IterateExp.__init__)


def test_docl_iterateexp_constructor_args():
    sig = inspect.signature(docl_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_collectionopcallexp_is_not_abstract():
    assert not inspect.isabstract(docl_CollectionOpCallExp)


def test_docl_collectionopcallexp_constructor_exists():
    assert callable(docl_CollectionOpCallExp.__init__)


def test_docl_collectionopcallexp_constructor_args():
    sig = inspect.signature(docl_CollectionOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_navigationexp_is_not_abstract():
    assert not inspect.isabstract(docl_NavigationExp)


def test_docl_navigationexp_constructor_exists():
    assert callable(docl_NavigationExp.__init__)


def test_docl_navigationexp_constructor_args():
    sig = inspect.signature(docl_NavigationExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_mulopcallexp_is_not_abstract():
    assert not inspect.isabstract(docl_MulOpCallExp)


def test_docl_mulopcallexp_constructor_exists():
    assert callable(docl_MulOpCallExp.__init__)


def test_docl_mulopcallexp_constructor_args():
    sig = inspect.signature(docl_MulOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_addopcallexp_is_not_abstract():
    assert not inspect.isabstract(docl_AddOpCallExp)


def test_docl_addopcallexp_constructor_exists():
    assert callable(docl_AddOpCallExp.__init__)


def test_docl_addopcallexp_constructor_args():
    sig = inspect.signature(docl_AddOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(docl_IteratorExp)


def test_docl_iteratorexp_constructor_exists():
    assert callable(docl_IteratorExp.__init__)


def test_docl_iteratorexp_constructor_args():
    sig = inspect.signature(docl_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_boolopcallexp_is_not_abstract():
    assert not inspect.isabstract(docl_BoolOpCallExp)


def test_docl_boolopcallexp_constructor_exists():
    assert callable(docl_BoolOpCallExp.__init__)


def test_docl_boolopcallexp_constructor_args():
    sig = inspect.signature(docl_BoolOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_stringtype_is_not_abstract():
    assert not inspect.isabstract(docl_StringType)


def test_docl_stringtype_constructor_exists():
    assert callable(docl_StringType.__init__)


def test_docl_stringtype_constructor_args():
    sig = inspect.signature(docl_StringType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_stringtype_has_name():
    assert hasattr(docl_StringType, "name")
    descriptor = None
    for klass in docl_StringType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_booleantype_is_not_abstract():
    assert not inspect.isabstract(docl_BooleanType)


def test_docl_booleantype_constructor_exists():
    assert callable(docl_BooleanType.__init__)


def test_docl_booleantype_constructor_args():
    sig = inspect.signature(docl_BooleanType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_booleantype_has_name():
    assert hasattr(docl_BooleanType, "name")
    descriptor = None
    for klass in docl_BooleanType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_integertype_is_not_abstract():
    assert not inspect.isabstract(docl_IntegerType)


def test_docl_integertype_constructor_exists():
    assert callable(docl_IntegerType.__init__)


def test_docl_integertype_constructor_args():
    sig = inspect.signature(docl_IntegerType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_integertype_has_name():
    assert hasattr(docl_IntegerType, "name")
    descriptor = None
    for klass in docl_IntegerType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_realtype_is_not_abstract():
    assert not inspect.isabstract(docl_RealType)


def test_docl_realtype_constructor_exists():
    assert callable(docl_RealType.__init__)


def test_docl_realtype_constructor_args():
    sig = inspect.signature(docl_RealType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_realtype_has_name():
    assert hasattr(docl_RealType, "name")
    descriptor = None
    for klass in docl_RealType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_bagtype_is_not_abstract():
    assert not inspect.isabstract(docl_BagType)


def test_docl_bagtype_constructor_exists():
    assert callable(docl_BagType.__init__)


def test_docl_bagtype_constructor_args():
    sig = inspect.signature(docl_BagType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_bagtype_has_name():
    assert hasattr(docl_BagType, "name")
    descriptor = None
    for klass in docl_BagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(docl_OrderedSetType)


def test_docl_orderedsettype_constructor_exists():
    assert callable(docl_OrderedSetType.__init__)


def test_docl_orderedsettype_constructor_args():
    sig = inspect.signature(docl_OrderedSetType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_orderedsettype_has_name():
    assert hasattr(docl_OrderedSetType, "name")
    descriptor = None
    for klass in docl_OrderedSetType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_sequencetype_is_not_abstract():
    assert not inspect.isabstract(docl_SequenceType)


def test_docl_sequencetype_constructor_exists():
    assert callable(docl_SequenceType.__init__)


def test_docl_sequencetype_constructor_args():
    sig = inspect.signature(docl_SequenceType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_sequencetype_has_name():
    assert hasattr(docl_SequenceType, "name")
    descriptor = None
    for klass in docl_SequenceType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_settype_is_not_abstract():
    assert not inspect.isabstract(docl_SetType)


def test_docl_settype_constructor_exists():
    assert callable(docl_SetType.__init__)


def test_docl_settype_constructor_args():
    sig = inspect.signature(docl_SetType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_settype_has_name():
    assert hasattr(docl_SetType, "name")
    descriptor = None
    for klass in docl_SetType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_oclanytype_is_not_abstract():
    assert not inspect.isabstract(docl_OclAnyType)


def test_docl_oclanytype_constructor_exists():
    assert callable(docl_OclAnyType.__init__)


def test_docl_oclanytype_constructor_args():
    sig = inspect.signature(docl_OclAnyType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_oclanytype_has_name():
    assert hasattr(docl_OclAnyType, "name")
    descriptor = None
    for klass in docl_OclAnyType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_tupletype_is_not_abstract():
    assert not inspect.isabstract(docl_TupleType)


def test_docl_tupletype_constructor_exists():
    assert callable(docl_TupleType.__init__)


def test_docl_tupletype_constructor_args():
    sig = inspect.signature(docl_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_docl_maptype_is_not_abstract():
    assert not inspect.isabstract(docl_MapType)


def test_docl_maptype_constructor_exists():
    assert callable(docl_MapType.__init__)


def test_docl_maptype_constructor_args():
    sig = inspect.signature(docl_MapType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_maptype_has_name():
    assert hasattr(docl_MapType, "name")
    descriptor = None
    for klass in docl_MapType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_lambdatype_is_not_abstract():
    assert not inspect.isabstract(docl_LambdaType)


def test_docl_lambdatype_constructor_exists():
    assert callable(docl_LambdaType.__init__)


def test_docl_lambdatype_constructor_args():
    sig = inspect.signature(docl_LambdaType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_lambdatype_has_name():
    assert hasattr(docl_LambdaType, "name")
    descriptor = None
    for klass in docl_LambdaType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_envtype_is_not_abstract():
    assert not inspect.isabstract(docl_EnvType)


def test_docl_envtype_constructor_exists():
    assert callable(docl_EnvType.__init__)


def test_docl_envtype_constructor_args():
    sig = inspect.signature(docl_EnvType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl_envtype_has_name():
    assert hasattr(docl_EnvType, "name")
    descriptor = None
    for klass in docl_EnvType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl_comopcallexp_is_not_abstract():
    assert not inspect.isabstract(docl_ComOpCallExp)


def test_docl_comopcallexp_constructor_exists():
    assert callable(docl_ComOpCallExp.__init__)


def test_docl_comopcallexp_constructor_args():
    sig = inspect.signature(docl_ComOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_eqopcallexp_is_not_abstract():
    assert not inspect.isabstract(docl_EqOpCallExp)


def test_docl_eqopcallexp_constructor_exists():
    assert callable(docl_EqOpCallExp.__init__)


def test_docl_eqopcallexp_constructor_args():
    sig = inspect.signature(docl_EqOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_ifexp_is_not_abstract():
    assert not inspect.isabstract(docl_IfExp)


def test_docl_ifexp_constructor_exists():
    assert callable(docl_IfExp.__init__)


def test_docl_ifexp_constructor_args():
    sig = inspect.signature(docl_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(docl_StringLiteralExp)


def test_docl_stringliteralexp_constructor_exists():
    assert callable(docl_StringLiteralExp.__init__)


def test_docl_stringliteralexp_constructor_args():
    sig = inspect.signature(docl_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "segments" in params, "Missing parameter 'segments'"

def test_docl_stringliteralexp_has_segments():
    assert hasattr(docl_StringLiteralExp, "segments")
    descriptor = None
    for klass in docl_StringLiteralExp.__mro__:
        if "segments" in klass.__dict__:
            descriptor = klass.__dict__["segments"]
            break
    assert isinstance(descriptor, property)



def test_docl_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(docl_InvalidLiteralExp)


def test_docl_invalidliteralexp_constructor_exists():
    assert callable(docl_InvalidLiteralExp.__init__)


def test_docl_invalidliteralexp_constructor_args():
    sig = inspect.signature(docl_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(docl_NullLiteralExp)


def test_docl_nullliteralexp_constructor_exists():
    assert callable(docl_NullLiteralExp.__init__)


def test_docl_nullliteralexp_constructor_args():
    sig = inspect.signature(docl_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_docl_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(docl_BooleanLiteralExp)


def test_docl_booleanliteralexp_constructor_exists():
    assert callable(docl_BooleanLiteralExp.__init__)


def test_docl_booleanliteralexp_constructor_args():
    sig = inspect.signature(docl_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_docl_booleanliteralexp_has_symbol():
    assert hasattr(docl_BooleanLiteralExp, "symbol")
    descriptor = None
    for klass in docl_BooleanLiteralExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_docl_numberliteralexp_is_not_abstract():
    assert not inspect.isabstract(docl_NumberLiteralExp)


def test_docl_numberliteralexp_constructor_exists():
    assert callable(docl_NumberLiteralExp.__init__)


def test_docl_numberliteralexp_constructor_args():
    sig = inspect.signature(docl_NumberLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_docl_numberliteralexp_has_symbol():
    assert hasattr(docl_NumberLiteralExp, "symbol")
    descriptor = None
    for klass in docl_NumberLiteralExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_docl_unlimitednaturalliteralexp_is_not_abstract():
    assert not inspect.isabstract(docl_UnlimitedNaturalLiteralExp)


def test_docl_unlimitednaturalliteralexp_constructor_exists():
    assert callable(docl_UnlimitedNaturalLiteralExp.__init__)


def test_docl_unlimitednaturalliteralexp_constructor_args():
    sig = inspect.signature(docl_UnlimitedNaturalLiteralExp.__init__)
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
OclExpression_strategy = st.builds(
    OclExpression,
)
docl_PrimitiveExp_strategy = st.builds(
    docl_PrimitiveExp,
)
docl_TuplePart_strategy = st.builds(
    docl_TuplePart,
    name=
        safe_text
)
docl_OclType_strategy = st.builds(
    docl_OclType,
)
docl_Iterator_strategy = st.builds(
    docl_Iterator,
    name=
        safe_text
)
docl_LocalVariable_strategy = st.builds(
    docl_LocalVariable,
    name=
        safe_text
)
OclType_strategy = st.builds(
    OclType,
)
docl_OclModelElementExp_strategy = st.builds(
    docl_OclModelElementExp,
    name=
        safe_text
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
docl_Query_strategy = st.builds(
    docl_Query,
    name=
        safe_text
)
docl_URI__strategy = st.builds(
    docl_URI_,
    authority=
        safe_text,
    fragment_=
        safe_text,
    scheme=
        safe_text
)
docl_ModuleElement_strategy = st.builds(
    docl_ModuleElement,
)
docl_Import_strategy = st.builds(
    docl_Import,
    name=
        safe_text
)
docl_OclExpression_strategy = st.builds(
    docl_OclExpression,
    elements=
        safe_text,
    name=
        safe_text
)
docl_OclModel_strategy = st.builds(
    docl_OclModel,
    name=
        safe_text
)
docl_Module_strategy = st.builds(
    docl_Module,
    name=
        safe_text
)
docl_NestedExp_strategy = st.builds(
    docl_NestedExp,
)
docl_SelfExp_strategy = st.builds(
    docl_SelfExp,
)
docl_ElseIfThenExp_strategy = st.builds(
    docl_ElseIfThenExp,
)
docl_TupleExp_strategy = st.builds(
    docl_TupleExp,
)
docl_LambdaExp_strategy = st.builds(
    docl_LambdaExp,
)
docl_OperationCall_strategy = st.builds(
    docl_OperationCall,
)
docl_NavigationOrAttributeCall_strategy = st.builds(
    docl_NavigationOrAttributeCall,
    feature=
        safe_text
)
docl_IterateExp_strategy = st.builds(
    docl_IterateExp,
)
docl_CollectionOpCallExp_strategy = st.builds(
    docl_CollectionOpCallExp,
)
docl_NavigationExp_strategy = st.builds(
    docl_NavigationExp,
)
docl_MulOpCallExp_strategy = st.builds(
    docl_MulOpCallExp,
)
docl_AddOpCallExp_strategy = st.builds(
    docl_AddOpCallExp,
)
docl_IteratorExp_strategy = st.builds(
    docl_IteratorExp,
)
docl_BoolOpCallExp_strategy = st.builds(
    docl_BoolOpCallExp,
)
docl_StringType_strategy = st.builds(
    docl_StringType,
    name=
        safe_text
)
docl_BooleanType_strategy = st.builds(
    docl_BooleanType,
    name=
        safe_text
)
docl_IntegerType_strategy = st.builds(
    docl_IntegerType,
    name=
        safe_text
)
docl_RealType_strategy = st.builds(
    docl_RealType,
    name=
        safe_text
)
docl_BagType_strategy = st.builds(
    docl_BagType,
    name=
        safe_text
)
docl_OrderedSetType_strategy = st.builds(
    docl_OrderedSetType,
    name=
        safe_text
)
docl_SequenceType_strategy = st.builds(
    docl_SequenceType,
    name=
        safe_text
)
docl_SetType_strategy = st.builds(
    docl_SetType,
    name=
        safe_text
)
docl_OclAnyType_strategy = st.builds(
    docl_OclAnyType,
    name=
        safe_text
)
docl_TupleType_strategy = st.builds(
    docl_TupleType,
)
docl_MapType_strategy = st.builds(
    docl_MapType,
    name=
        safe_text
)
docl_LambdaType_strategy = st.builds(
    docl_LambdaType,
    name=
        safe_text
)
docl_EnvType_strategy = st.builds(
    docl_EnvType,
    name=
        safe_text
)
docl_ComOpCallExp_strategy = st.builds(
    docl_ComOpCallExp,
)
docl_EqOpCallExp_strategy = st.builds(
    docl_EqOpCallExp,
)
docl_IfExp_strategy = st.builds(
    docl_IfExp,
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
docl_StringLiteralExp_strategy = st.builds(
    docl_StringLiteralExp,
    segments=
        safe_text
)
docl_InvalidLiteralExp_strategy = st.builds(
    docl_InvalidLiteralExp,
)
docl_NullLiteralExp_strategy = st.builds(
    docl_NullLiteralExp,
)
docl_BooleanLiteralExp_strategy = st.builds(
    docl_BooleanLiteralExp,
    symbol=
        safe_text
)
docl_NumberLiteralExp_strategy = st.builds(
    docl_NumberLiteralExp,
    symbol=
        st.integers()
)
docl_UnlimitedNaturalLiteralExp_strategy = st.builds(
    docl_UnlimitedNaturalLiteralExp,
)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=docl_PrimitiveExp_strategy)
@settings(max_examples=50)
def test_docl_primitiveexp_instantiation(instance):
    assert isinstance(instance, docl_PrimitiveExp)

@given(instance=docl_TuplePart_strategy)
@settings(max_examples=50)
def test_docl_tuplepart_instantiation(instance):
    assert isinstance(instance, docl_TuplePart)



@given(instance=docl_TuplePart_strategy)
def test_docl_tuplepart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_OclType_strategy)
@settings(max_examples=50)
def test_docl_ocltype_instantiation(instance):
    assert isinstance(instance, docl_OclType)

@given(instance=docl_Iterator_strategy)
@settings(max_examples=50)
def test_docl_iterator_instantiation(instance):
    assert isinstance(instance, docl_Iterator)



@given(instance=docl_Iterator_strategy)
def test_docl_iterator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_LocalVariable_strategy)
@settings(max_examples=50)
def test_docl_localvariable_instantiation(instance):
    assert isinstance(instance, docl_LocalVariable)



@given(instance=docl_LocalVariable_strategy)
def test_docl_localvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=docl_OclModelElementExp_strategy)
@settings(max_examples=50)
def test_docl_oclmodelelementexp_instantiation(instance):
    assert isinstance(instance, docl_OclModelElementExp)



@given(instance=docl_OclModelElementExp_strategy)
def test_docl_oclmodelelementexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=docl_Query_strategy)
@settings(max_examples=50)
def test_docl_query_instantiation(instance):
    assert isinstance(instance, docl_Query)



@given(instance=docl_Query_strategy)
def test_docl_query_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_URI__strategy)
@settings(max_examples=50)
def test_docl_uri__instantiation(instance):
    assert isinstance(instance, docl_URI_)



@given(instance=docl_URI__strategy)
def test_docl_uri__authority_setter(instance):
    original = instance.authority
    instance.authority = original
    assert instance.authority == original



@given(instance=docl_URI__strategy)
def test_docl_uri__fragment__setter(instance):
    original = instance.fragment_
    instance.fragment_ = original
    assert instance.fragment_ == original



@given(instance=docl_URI__strategy)
def test_docl_uri__scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original

@given(instance=docl_ModuleElement_strategy)
@settings(max_examples=50)
def test_docl_moduleelement_instantiation(instance):
    assert isinstance(instance, docl_ModuleElement)

@given(instance=docl_Import_strategy)
@settings(max_examples=50)
def test_docl_import_instantiation(instance):
    assert isinstance(instance, docl_Import)



@given(instance=docl_Import_strategy)
def test_docl_import_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_OclExpression_strategy)
@settings(max_examples=50)
def test_docl_oclexpression_instantiation(instance):
    assert isinstance(instance, docl_OclExpression)



@given(instance=docl_OclExpression_strategy)
def test_docl_oclexpression_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original



@given(instance=docl_OclExpression_strategy)
def test_docl_oclexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_OclModel_strategy)
@settings(max_examples=50)
def test_docl_oclmodel_instantiation(instance):
    assert isinstance(instance, docl_OclModel)



@given(instance=docl_OclModel_strategy)
def test_docl_oclmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_Module_strategy)
@settings(max_examples=50)
def test_docl_module_instantiation(instance):
    assert isinstance(instance, docl_Module)



@given(instance=docl_Module_strategy)
def test_docl_module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_NestedExp_strategy)
@settings(max_examples=50)
def test_docl_nestedexp_instantiation(instance):
    assert isinstance(instance, docl_NestedExp)

@given(instance=docl_SelfExp_strategy)
@settings(max_examples=50)
def test_docl_selfexp_instantiation(instance):
    assert isinstance(instance, docl_SelfExp)

@given(instance=docl_ElseIfThenExp_strategy)
@settings(max_examples=50)
def test_docl_elseifthenexp_instantiation(instance):
    assert isinstance(instance, docl_ElseIfThenExp)

@given(instance=docl_TupleExp_strategy)
@settings(max_examples=50)
def test_docl_tupleexp_instantiation(instance):
    assert isinstance(instance, docl_TupleExp)

@given(instance=docl_LambdaExp_strategy)
@settings(max_examples=50)
def test_docl_lambdaexp_instantiation(instance):
    assert isinstance(instance, docl_LambdaExp)

@given(instance=docl_OperationCall_strategy)
@settings(max_examples=50)
def test_docl_operationcall_instantiation(instance):
    assert isinstance(instance, docl_OperationCall)

@given(instance=docl_NavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_docl_navigationorattributecall_instantiation(instance):
    assert isinstance(instance, docl_NavigationOrAttributeCall)



@given(instance=docl_NavigationOrAttributeCall_strategy)
def test_docl_navigationorattributecall_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=docl_IterateExp_strategy)
@settings(max_examples=50)
def test_docl_iterateexp_instantiation(instance):
    assert isinstance(instance, docl_IterateExp)

@given(instance=docl_CollectionOpCallExp_strategy)
@settings(max_examples=50)
def test_docl_collectionopcallexp_instantiation(instance):
    assert isinstance(instance, docl_CollectionOpCallExp)

@given(instance=docl_NavigationExp_strategy)
@settings(max_examples=50)
def test_docl_navigationexp_instantiation(instance):
    assert isinstance(instance, docl_NavigationExp)

@given(instance=docl_MulOpCallExp_strategy)
@settings(max_examples=50)
def test_docl_mulopcallexp_instantiation(instance):
    assert isinstance(instance, docl_MulOpCallExp)

@given(instance=docl_AddOpCallExp_strategy)
@settings(max_examples=50)
def test_docl_addopcallexp_instantiation(instance):
    assert isinstance(instance, docl_AddOpCallExp)

@given(instance=docl_IteratorExp_strategy)
@settings(max_examples=50)
def test_docl_iteratorexp_instantiation(instance):
    assert isinstance(instance, docl_IteratorExp)

@given(instance=docl_BoolOpCallExp_strategy)
@settings(max_examples=50)
def test_docl_boolopcallexp_instantiation(instance):
    assert isinstance(instance, docl_BoolOpCallExp)

@given(instance=docl_StringType_strategy)
@settings(max_examples=50)
def test_docl_stringtype_instantiation(instance):
    assert isinstance(instance, docl_StringType)



@given(instance=docl_StringType_strategy)
def test_docl_stringtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_BooleanType_strategy)
@settings(max_examples=50)
def test_docl_booleantype_instantiation(instance):
    assert isinstance(instance, docl_BooleanType)



@given(instance=docl_BooleanType_strategy)
def test_docl_booleantype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_IntegerType_strategy)
@settings(max_examples=50)
def test_docl_integertype_instantiation(instance):
    assert isinstance(instance, docl_IntegerType)



@given(instance=docl_IntegerType_strategy)
def test_docl_integertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_RealType_strategy)
@settings(max_examples=50)
def test_docl_realtype_instantiation(instance):
    assert isinstance(instance, docl_RealType)



@given(instance=docl_RealType_strategy)
def test_docl_realtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_BagType_strategy)
@settings(max_examples=50)
def test_docl_bagtype_instantiation(instance):
    assert isinstance(instance, docl_BagType)



@given(instance=docl_BagType_strategy)
def test_docl_bagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_OrderedSetType_strategy)
@settings(max_examples=50)
def test_docl_orderedsettype_instantiation(instance):
    assert isinstance(instance, docl_OrderedSetType)



@given(instance=docl_OrderedSetType_strategy)
def test_docl_orderedsettype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_SequenceType_strategy)
@settings(max_examples=50)
def test_docl_sequencetype_instantiation(instance):
    assert isinstance(instance, docl_SequenceType)



@given(instance=docl_SequenceType_strategy)
def test_docl_sequencetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_SetType_strategy)
@settings(max_examples=50)
def test_docl_settype_instantiation(instance):
    assert isinstance(instance, docl_SetType)



@given(instance=docl_SetType_strategy)
def test_docl_settype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_OclAnyType_strategy)
@settings(max_examples=50)
def test_docl_oclanytype_instantiation(instance):
    assert isinstance(instance, docl_OclAnyType)



@given(instance=docl_OclAnyType_strategy)
def test_docl_oclanytype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_TupleType_strategy)
@settings(max_examples=50)
def test_docl_tupletype_instantiation(instance):
    assert isinstance(instance, docl_TupleType)

@given(instance=docl_MapType_strategy)
@settings(max_examples=50)
def test_docl_maptype_instantiation(instance):
    assert isinstance(instance, docl_MapType)



@given(instance=docl_MapType_strategy)
def test_docl_maptype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_LambdaType_strategy)
@settings(max_examples=50)
def test_docl_lambdatype_instantiation(instance):
    assert isinstance(instance, docl_LambdaType)



@given(instance=docl_LambdaType_strategy)
def test_docl_lambdatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_EnvType_strategy)
@settings(max_examples=50)
def test_docl_envtype_instantiation(instance):
    assert isinstance(instance, docl_EnvType)



@given(instance=docl_EnvType_strategy)
def test_docl_envtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl_ComOpCallExp_strategy)
@settings(max_examples=50)
def test_docl_comopcallexp_instantiation(instance):
    assert isinstance(instance, docl_ComOpCallExp)

@given(instance=docl_EqOpCallExp_strategy)
@settings(max_examples=50)
def test_docl_eqopcallexp_instantiation(instance):
    assert isinstance(instance, docl_EqOpCallExp)

@given(instance=docl_IfExp_strategy)
@settings(max_examples=50)
def test_docl_ifexp_instantiation(instance):
    assert isinstance(instance, docl_IfExp)

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=docl_StringLiteralExp_strategy)
@settings(max_examples=50)
def test_docl_stringliteralexp_instantiation(instance):
    assert isinstance(instance, docl_StringLiteralExp)



@given(instance=docl_StringLiteralExp_strategy)
def test_docl_stringliteralexp_segments_setter(instance):
    original = instance.segments
    instance.segments = original
    assert instance.segments == original

@given(instance=docl_InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_docl_invalidliteralexp_instantiation(instance):
    assert isinstance(instance, docl_InvalidLiteralExp)

@given(instance=docl_NullLiteralExp_strategy)
@settings(max_examples=50)
def test_docl_nullliteralexp_instantiation(instance):
    assert isinstance(instance, docl_NullLiteralExp)

@given(instance=docl_BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_docl_booleanliteralexp_instantiation(instance):
    assert isinstance(instance, docl_BooleanLiteralExp)



@given(instance=docl_BooleanLiteralExp_strategy)
def test_docl_booleanliteralexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=docl_NumberLiteralExp_strategy)
@settings(max_examples=50)
def test_docl_numberliteralexp_instantiation(instance):
    assert isinstance(instance, docl_NumberLiteralExp)



@given(instance=docl_NumberLiteralExp_strategy)
def test_docl_numberliteralexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=docl_UnlimitedNaturalLiteralExp_strategy)
@settings(max_examples=50)
def test_docl_unlimitednaturalliteralexp_instantiation(instance):
    assert isinstance(instance, docl_UnlimitedNaturalLiteralExp)
