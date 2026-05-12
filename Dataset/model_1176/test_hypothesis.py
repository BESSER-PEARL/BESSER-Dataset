import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    OclFeature,
    CollectionType,
    EmigOcl_SetType,
    EmigOcl_OrderedSetType,
    EmigOcl_SequenceType,
    EmigOcl_BagType,
    NumericType,
    EmigOcl_RealType,
    EmigOcl_IntegerType,
    Primitive,
    EmigOcl_BooleanType,
    EmigOcl_NumericType,
    EmigOcl_StringType,
    OclType,
    EmigOcl_Primitive,
    EmigOcl_OclAnyType,
    EmigOcl_MapType,
    EmigOcl_OclModelElement,
    EmigOcl_TupleType,
    EmigOcl_LambdaType,
    EmigOcl_CollectionType,
    VariableDeclaration,
    EmigOcl_Parameter,
    LoopExp,
    EmigOcl_IteratorExp,
    EmigOcl_Iterator,
    EmigOcl_IterateExp,
    OperationCall,
    EmigOcl_CollectionOperationCall,
    VariableExp,
    EmigOcl_LambdaCallExp,
    OperatorCallExp,
    EmigOcl_IntOpCallExp,
    EmigOcl_RelOpCallExp,
    EmigOcl_EqOpCallExp,
    EmigOcl_MulOpCallExp,
    EmigOcl_AddOpCallExp,
    EmigOcl_NotOpCallExp,
    PropertyCallExp,
    EmigOcl_OperatorCallExp,
    PropertyCall,
    EmigOcl_NavigationOrAttributeCall,
    EmigOcl_PropertyCall,
    StaticPropertyCall,
    EmigOcl_StaticOperationCall,
    EmigOcl_StaticNavigationOrAttributeCall,
    EmigOcl_StaticPropertyCall,
    LocalVariable,
    EmigOcl_TuplePart,
    NumericExp,
    EmigOcl_IntegerExp,
    EmigOcl_RealExp,
    PrimitiveExp,
    EmigOcl_BooleanExp,
    EmigOcl_NumericExp,
    EmigOcl_StringExp,
    OclExpression,
    EmigOcl_BraceExp,
    EmigOcl_OclUndefinedExp,
    EmigOcl_OclModelElementExp,
    EmigOcl_StaticPropertyCallExp,
    EmigOcl_EnumLiteralExp,
    EmigOcl_TupleExp,
    EmigOcl_MapExp,
    EmigOcl_PrimitiveExp,
    EmigOcl_SelfExp,
    EmigOcl_SuperExp,
    EmigOcl_VariableExp,
    EmigOcl_Attribute,
    EmigOcl_Operation,
    EmigOcl_LocalVariable,
    EmigOcl_OperationCall,
    EmigOcl_LoopExp,
    CollectionExp,
    EmigOcl_SequenceExp,
    EmigOcl_OrderedSetExp,
    EmigOcl_SetExp,
    EmigOcl_BagExp,
    EmigOcl_CollectionExp,
    EmigOcl_PropertyCallExp,
    EmigOcl_IfExp,
    LocatedElement,
    EmigOcl_TupleTypeAttribute,
    EmigOcl_OclExpression,
    EmigOcl_VariableDeclaration,
    EmigOcl_OclFeature,
    EmigOcl_OclModel,
    EmigOcl_OclFeatureDefinition,
    EmigOcl_MapElement,
    EmigOcl_OclContextDefinition,
    EmigOcl_OclType,
    EmigOcl_Module,
    EmigOcl_LocatedElement,
    EmigOcl_LetExp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_settype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_SetType)


def test_emigocl_settype_constructor_exists():
    assert callable(EmigOcl_SetType.__init__)


def test_emigocl_settype_constructor_args():
    sig = inspect.signature(EmigOcl_SetType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_OrderedSetType)


def test_emigocl_orderedsettype_constructor_exists():
    assert callable(EmigOcl_OrderedSetType.__init__)


def test_emigocl_orderedsettype_constructor_args():
    sig = inspect.signature(EmigOcl_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_sequencetype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_SequenceType)


def test_emigocl_sequencetype_constructor_exists():
    assert callable(EmigOcl_SequenceType.__init__)


def test_emigocl_sequencetype_constructor_args():
    sig = inspect.signature(EmigOcl_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_bagtype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_BagType)


def test_emigocl_bagtype_constructor_exists():
    assert callable(EmigOcl_BagType.__init__)


def test_emigocl_bagtype_constructor_args():
    sig = inspect.signature(EmigOcl_BagType.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_realtype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_RealType)


def test_emigocl_realtype_constructor_exists():
    assert callable(EmigOcl_RealType.__init__)


def test_emigocl_realtype_constructor_args():
    sig = inspect.signature(EmigOcl_RealType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_integertype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_IntegerType)


def test_emigocl_integertype_constructor_exists():
    assert callable(EmigOcl_IntegerType.__init__)


def test_emigocl_integertype_constructor_args():
    sig = inspect.signature(EmigOcl_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_booleantype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_BooleanType)


def test_emigocl_booleantype_constructor_exists():
    assert callable(EmigOcl_BooleanType.__init__)


def test_emigocl_booleantype_constructor_args():
    sig = inspect.signature(EmigOcl_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_numerictype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_NumericType)


def test_emigocl_numerictype_constructor_exists():
    assert callable(EmigOcl_NumericType.__init__)


def test_emigocl_numerictype_constructor_args():
    sig = inspect.signature(EmigOcl_NumericType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_stringtype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_StringType)


def test_emigocl_stringtype_constructor_exists():
    assert callable(EmigOcl_StringType.__init__)


def test_emigocl_stringtype_constructor_args():
    sig = inspect.signature(EmigOcl_StringType.__init__)
    params = list(sig.parameters.keys())



def test_ocltype_is_not_abstract():
    assert not inspect.isabstract(OclType)


def test_ocltype_constructor_exists():
    assert callable(OclType.__init__)


def test_ocltype_constructor_args():
    sig = inspect.signature(OclType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_primitive_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_Primitive)


def test_emigocl_primitive_constructor_exists():
    assert callable(EmigOcl_Primitive.__init__)


def test_emigocl_primitive_constructor_args():
    sig = inspect.signature(EmigOcl_Primitive.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_oclanytype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_OclAnyType)


def test_emigocl_oclanytype_constructor_exists():
    assert callable(EmigOcl_OclAnyType.__init__)


def test_emigocl_oclanytype_constructor_args():
    sig = inspect.signature(EmigOcl_OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_maptype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_MapType)


def test_emigocl_maptype_constructor_exists():
    assert callable(EmigOcl_MapType.__init__)


def test_emigocl_maptype_constructor_args():
    sig = inspect.signature(EmigOcl_MapType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_OclModelElement)


def test_emigocl_oclmodelelement_constructor_exists():
    assert callable(EmigOcl_OclModelElement.__init__)


def test_emigocl_oclmodelelement_constructor_args():
    sig = inspect.signature(EmigOcl_OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_tupletype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_TupleType)


def test_emigocl_tupletype_constructor_exists():
    assert callable(EmigOcl_TupleType.__init__)


def test_emigocl_tupletype_constructor_args():
    sig = inspect.signature(EmigOcl_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_lambdatype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_LambdaType)


def test_emigocl_lambdatype_constructor_exists():
    assert callable(EmigOcl_LambdaType.__init__)


def test_emigocl_lambdatype_constructor_args():
    sig = inspect.signature(EmigOcl_LambdaType.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_collectiontype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_CollectionType)


def test_emigocl_collectiontype_constructor_exists():
    assert callable(EmigOcl_CollectionType.__init__)


def test_emigocl_collectiontype_constructor_args():
    sig = inspect.signature(EmigOcl_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_parameter_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_Parameter)


def test_emigocl_parameter_constructor_exists():
    assert callable(EmigOcl_Parameter.__init__)


def test_emigocl_parameter_constructor_args():
    sig = inspect.signature(EmigOcl_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_IteratorExp)


def test_emigocl_iteratorexp_constructor_exists():
    assert callable(EmigOcl_IteratorExp.__init__)


def test_emigocl_iteratorexp_constructor_args():
    sig = inspect.signature(EmigOcl_IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl_iteratorexp_has_name():
    assert hasattr(EmigOcl_IteratorExp, "name")
    descriptor = None
    for klass in EmigOcl_IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_iterator_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_Iterator)


def test_emigocl_iterator_constructor_exists():
    assert callable(EmigOcl_Iterator.__init__)


def test_emigocl_iterator_constructor_args():
    sig = inspect.signature(EmigOcl_Iterator.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_iterateexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_IterateExp)


def test_emigocl_iterateexp_constructor_exists():
    assert callable(EmigOcl_IterateExp.__init__)


def test_emigocl_iterateexp_constructor_args():
    sig = inspect.signature(EmigOcl_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_operationcall_is_not_abstract():
    assert not inspect.isabstract(OperationCall)


def test_operationcall_constructor_exists():
    assert callable(OperationCall.__init__)


def test_operationcall_constructor_args():
    sig = inspect.signature(OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_collectionoperationcall_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_CollectionOperationCall)


def test_emigocl_collectionoperationcall_constructor_exists():
    assert callable(EmigOcl_CollectionOperationCall.__init__)


def test_emigocl_collectionoperationcall_constructor_args():
    sig = inspect.signature(EmigOcl_CollectionOperationCall.__init__)
    params = list(sig.parameters.keys())



def test_variableexp_is_not_abstract():
    assert not inspect.isabstract(VariableExp)


def test_variableexp_constructor_exists():
    assert callable(VariableExp.__init__)


def test_variableexp_constructor_args():
    sig = inspect.signature(VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_lambdacallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_LambdaCallExp)


def test_emigocl_lambdacallexp_constructor_exists():
    assert callable(EmigOcl_LambdaCallExp.__init__)


def test_emigocl_lambdacallexp_constructor_args():
    sig = inspect.signature(EmigOcl_LambdaCallExp.__init__)
    params = list(sig.parameters.keys())



def test_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OperatorCallExp)


def test_operatorcallexp_constructor_exists():
    assert callable(OperatorCallExp.__init__)


def test_operatorcallexp_constructor_args():
    sig = inspect.signature(OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_intopcallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_IntOpCallExp)


def test_emigocl_intopcallexp_constructor_exists():
    assert callable(EmigOcl_IntOpCallExp.__init__)


def test_emigocl_intopcallexp_constructor_args():
    sig = inspect.signature(EmigOcl_IntOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_relopcallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_RelOpCallExp)


def test_emigocl_relopcallexp_constructor_exists():
    assert callable(EmigOcl_RelOpCallExp.__init__)


def test_emigocl_relopcallexp_constructor_args():
    sig = inspect.signature(EmigOcl_RelOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_eqopcallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_EqOpCallExp)


def test_emigocl_eqopcallexp_constructor_exists():
    assert callable(EmigOcl_EqOpCallExp.__init__)


def test_emigocl_eqopcallexp_constructor_args():
    sig = inspect.signature(EmigOcl_EqOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_mulopcallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_MulOpCallExp)


def test_emigocl_mulopcallexp_constructor_exists():
    assert callable(EmigOcl_MulOpCallExp.__init__)


def test_emigocl_mulopcallexp_constructor_args():
    sig = inspect.signature(EmigOcl_MulOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_addopcallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_AddOpCallExp)


def test_emigocl_addopcallexp_constructor_exists():
    assert callable(EmigOcl_AddOpCallExp.__init__)


def test_emigocl_addopcallexp_constructor_args():
    sig = inspect.signature(EmigOcl_AddOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_notopcallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_NotOpCallExp)


def test_emigocl_notopcallexp_constructor_exists():
    assert callable(EmigOcl_NotOpCallExp.__init__)


def test_emigocl_notopcallexp_constructor_args():
    sig = inspect.signature(EmigOcl_NotOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_OperatorCallExp)


def test_emigocl_operatorcallexp_constructor_exists():
    assert callable(EmigOcl_OperatorCallExp.__init__)


def test_emigocl_operatorcallexp_constructor_args():
    sig = inspect.signature(EmigOcl_OperatorCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_emigocl_operatorcallexp_has_operationName():
    assert hasattr(EmigOcl_OperatorCallExp, "operationName")
    descriptor = None
    for klass in EmigOcl_OperatorCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_propertycall_is_not_abstract():
    assert not inspect.isabstract(PropertyCall)


def test_propertycall_constructor_exists():
    assert callable(PropertyCall.__init__)


def test_propertycall_constructor_args():
    sig = inspect.signature(PropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_navigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_NavigationOrAttributeCall)


def test_emigocl_navigationorattributecall_constructor_exists():
    assert callable(EmigOcl_NavigationOrAttributeCall.__init__)


def test_emigocl_navigationorattributecall_constructor_args():
    sig = inspect.signature(EmigOcl_NavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl_navigationorattributecall_has_name():
    assert hasattr(EmigOcl_NavigationOrAttributeCall, "name")
    descriptor = None
    for klass in EmigOcl_NavigationOrAttributeCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_propertycall_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_PropertyCall)


def test_emigocl_propertycall_constructor_exists():
    assert callable(EmigOcl_PropertyCall.__init__)


def test_emigocl_propertycall_constructor_args():
    sig = inspect.signature(EmigOcl_PropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_staticpropertycall_is_not_abstract():
    assert not inspect.isabstract(StaticPropertyCall)


def test_staticpropertycall_constructor_exists():
    assert callable(StaticPropertyCall.__init__)


def test_staticpropertycall_constructor_args():
    sig = inspect.signature(StaticPropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_staticoperationcall_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_StaticOperationCall)


def test_emigocl_staticoperationcall_constructor_exists():
    assert callable(EmigOcl_StaticOperationCall.__init__)


def test_emigocl_staticoperationcall_constructor_args():
    sig = inspect.signature(EmigOcl_StaticOperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_emigocl_staticoperationcall_has_operationName():
    assert hasattr(EmigOcl_StaticOperationCall, "operationName")
    descriptor = None
    for klass in EmigOcl_StaticOperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_staticnavigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_StaticNavigationOrAttributeCall)


def test_emigocl_staticnavigationorattributecall_constructor_exists():
    assert callable(EmigOcl_StaticNavigationOrAttributeCall.__init__)


def test_emigocl_staticnavigationorattributecall_constructor_args():
    sig = inspect.signature(EmigOcl_StaticNavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl_staticnavigationorattributecall_has_name():
    assert hasattr(EmigOcl_StaticNavigationOrAttributeCall, "name")
    descriptor = None
    for klass in EmigOcl_StaticNavigationOrAttributeCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_staticpropertycall_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_StaticPropertyCall)


def test_emigocl_staticpropertycall_constructor_exists():
    assert callable(EmigOcl_StaticPropertyCall.__init__)


def test_emigocl_staticpropertycall_constructor_args():
    sig = inspect.signature(EmigOcl_StaticPropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_localvariable_is_not_abstract():
    assert not inspect.isabstract(LocalVariable)


def test_localvariable_constructor_exists():
    assert callable(LocalVariable.__init__)


def test_localvariable_constructor_args():
    sig = inspect.signature(LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_tuplepart_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_TuplePart)


def test_emigocl_tuplepart_constructor_exists():
    assert callable(EmigOcl_TuplePart.__init__)


def test_emigocl_tuplepart_constructor_args():
    sig = inspect.signature(EmigOcl_TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_integerexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_IntegerExp)


def test_emigocl_integerexp_constructor_exists():
    assert callable(EmigOcl_IntegerExp.__init__)


def test_emigocl_integerexp_constructor_args():
    sig = inspect.signature(EmigOcl_IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_emigocl_integerexp_has_integerSymbol():
    assert hasattr(EmigOcl_IntegerExp, "integerSymbol")
    descriptor = None
    for klass in EmigOcl_IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_realexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_RealExp)


def test_emigocl_realexp_constructor_exists():
    assert callable(EmigOcl_RealExp.__init__)


def test_emigocl_realexp_constructor_args():
    sig = inspect.signature(EmigOcl_RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_emigocl_realexp_has_realSymbol():
    assert hasattr(EmigOcl_RealExp, "realSymbol")
    descriptor = None
    for klass in EmigOcl_RealExp.__mro__:
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



def test_emigocl_booleanexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_BooleanExp)


def test_emigocl_booleanexp_constructor_exists():
    assert callable(EmigOcl_BooleanExp.__init__)


def test_emigocl_booleanexp_constructor_args():
    sig = inspect.signature(EmigOcl_BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_emigocl_booleanexp_has_booleanSymbol():
    assert hasattr(EmigOcl_BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in EmigOcl_BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_numericexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_NumericExp)


def test_emigocl_numericexp_constructor_exists():
    assert callable(EmigOcl_NumericExp.__init__)


def test_emigocl_numericexp_constructor_args():
    sig = inspect.signature(EmigOcl_NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_stringexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_StringExp)


def test_emigocl_stringexp_constructor_exists():
    assert callable(EmigOcl_StringExp.__init__)


def test_emigocl_stringexp_constructor_args():
    sig = inspect.signature(EmigOcl_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_emigocl_stringexp_has_stringSymbol():
    assert hasattr(EmigOcl_StringExp, "stringSymbol")
    descriptor = None
    for klass in EmigOcl_StringExp.__mro__:
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



def test_emigocl_braceexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_BraceExp)


def test_emigocl_braceexp_constructor_exists():
    assert callable(EmigOcl_BraceExp.__init__)


def test_emigocl_braceexp_constructor_args():
    sig = inspect.signature(EmigOcl_BraceExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_OclUndefinedExp)


def test_emigocl_oclundefinedexp_constructor_exists():
    assert callable(EmigOcl_OclUndefinedExp.__init__)


def test_emigocl_oclundefinedexp_constructor_args():
    sig = inspect.signature(EmigOcl_OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_oclmodelelementexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_OclModelElementExp)


def test_emigocl_oclmodelelementexp_constructor_exists():
    assert callable(EmigOcl_OclModelElementExp.__init__)


def test_emigocl_oclmodelelementexp_constructor_args():
    sig = inspect.signature(EmigOcl_OclModelElementExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl_oclmodelelementexp_has_name():
    assert hasattr(EmigOcl_OclModelElementExp, "name")
    descriptor = None
    for klass in EmigOcl_OclModelElementExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_staticpropertycallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_StaticPropertyCallExp)


def test_emigocl_staticpropertycallexp_constructor_exists():
    assert callable(EmigOcl_StaticPropertyCallExp.__init__)


def test_emigocl_staticpropertycallexp_constructor_args():
    sig = inspect.signature(EmigOcl_StaticPropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_EnumLiteralExp)


def test_emigocl_enumliteralexp_constructor_exists():
    assert callable(EmigOcl_EnumLiteralExp.__init__)


def test_emigocl_enumliteralexp_constructor_args():
    sig = inspect.signature(EmigOcl_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl_enumliteralexp_has_name():
    assert hasattr(EmigOcl_EnumLiteralExp, "name")
    descriptor = None
    for klass in EmigOcl_EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_tupleexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_TupleExp)


def test_emigocl_tupleexp_constructor_exists():
    assert callable(EmigOcl_TupleExp.__init__)


def test_emigocl_tupleexp_constructor_args():
    sig = inspect.signature(EmigOcl_TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_mapexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_MapExp)


def test_emigocl_mapexp_constructor_exists():
    assert callable(EmigOcl_MapExp.__init__)


def test_emigocl_mapexp_constructor_args():
    sig = inspect.signature(EmigOcl_MapExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_PrimitiveExp)


def test_emigocl_primitiveexp_constructor_exists():
    assert callable(EmigOcl_PrimitiveExp.__init__)


def test_emigocl_primitiveexp_constructor_args():
    sig = inspect.signature(EmigOcl_PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_selfexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_SelfExp)


def test_emigocl_selfexp_constructor_exists():
    assert callable(EmigOcl_SelfExp.__init__)


def test_emigocl_selfexp_constructor_args():
    sig = inspect.signature(EmigOcl_SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_superexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_SuperExp)


def test_emigocl_superexp_constructor_exists():
    assert callable(EmigOcl_SuperExp.__init__)


def test_emigocl_superexp_constructor_args():
    sig = inspect.signature(EmigOcl_SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_variableexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_VariableExp)


def test_emigocl_variableexp_constructor_exists():
    assert callable(EmigOcl_VariableExp.__init__)


def test_emigocl_variableexp_constructor_args():
    sig = inspect.signature(EmigOcl_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_attribute_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_Attribute)


def test_emigocl_attribute_constructor_exists():
    assert callable(EmigOcl_Attribute.__init__)


def test_emigocl_attribute_constructor_args():
    sig = inspect.signature(EmigOcl_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl_attribute_has_name():
    assert hasattr(EmigOcl_Attribute, "name")
    descriptor = None
    for klass in EmigOcl_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_operation_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_Operation)


def test_emigocl_operation_constructor_exists():
    assert callable(EmigOcl_Operation.__init__)


def test_emigocl_operation_constructor_args():
    sig = inspect.signature(EmigOcl_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl_operation_has_name():
    assert hasattr(EmigOcl_Operation, "name")
    descriptor = None
    for klass in EmigOcl_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_localvariable_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_LocalVariable)


def test_emigocl_localvariable_constructor_exists():
    assert callable(EmigOcl_LocalVariable.__init__)


def test_emigocl_localvariable_constructor_args():
    sig = inspect.signature(EmigOcl_LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_emigocl_localvariable_has_eq():
    assert hasattr(EmigOcl_LocalVariable, "eq")
    descriptor = None
    for klass in EmigOcl_LocalVariable.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_operationcall_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_OperationCall)


def test_emigocl_operationcall_constructor_exists():
    assert callable(EmigOcl_OperationCall.__init__)


def test_emigocl_operationcall_constructor_args():
    sig = inspect.signature(EmigOcl_OperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_emigocl_operationcall_has_operationName():
    assert hasattr(EmigOcl_OperationCall, "operationName")
    descriptor = None
    for klass in EmigOcl_OperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_LoopExp)


def test_emigocl_loopexp_constructor_exists():
    assert callable(EmigOcl_LoopExp.__init__)


def test_emigocl_loopexp_constructor_args():
    sig = inspect.signature(EmigOcl_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_sequenceexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_SequenceExp)


def test_emigocl_sequenceexp_constructor_exists():
    assert callable(EmigOcl_SequenceExp.__init__)


def test_emigocl_sequenceexp_constructor_args():
    sig = inspect.signature(EmigOcl_SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_OrderedSetExp)


def test_emigocl_orderedsetexp_constructor_exists():
    assert callable(EmigOcl_OrderedSetExp.__init__)


def test_emigocl_orderedsetexp_constructor_args():
    sig = inspect.signature(EmigOcl_OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_setexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_SetExp)


def test_emigocl_setexp_constructor_exists():
    assert callable(EmigOcl_SetExp.__init__)


def test_emigocl_setexp_constructor_args():
    sig = inspect.signature(EmigOcl_SetExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_bagexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_BagExp)


def test_emigocl_bagexp_constructor_exists():
    assert callable(EmigOcl_BagExp.__init__)


def test_emigocl_bagexp_constructor_args():
    sig = inspect.signature(EmigOcl_BagExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_collectionexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_CollectionExp)


def test_emigocl_collectionexp_constructor_exists():
    assert callable(EmigOcl_CollectionExp.__init__)


def test_emigocl_collectionexp_constructor_args():
    sig = inspect.signature(EmigOcl_CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_PropertyCallExp)


def test_emigocl_propertycallexp_constructor_exists():
    assert callable(EmigOcl_PropertyCallExp.__init__)


def test_emigocl_propertycallexp_constructor_args():
    sig = inspect.signature(EmigOcl_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_ifexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_IfExp)


def test_emigocl_ifexp_constructor_exists():
    assert callable(EmigOcl_IfExp.__init__)


def test_emigocl_ifexp_constructor_args():
    sig = inspect.signature(EmigOcl_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_TupleTypeAttribute)


def test_emigocl_tupletypeattribute_constructor_exists():
    assert callable(EmigOcl_TupleTypeAttribute.__init__)


def test_emigocl_tupletypeattribute_constructor_args():
    sig = inspect.signature(EmigOcl_TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl_tupletypeattribute_has_name():
    assert hasattr(EmigOcl_TupleTypeAttribute, "name")
    descriptor = None
    for klass in EmigOcl_TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_OclExpression)


def test_emigocl_oclexpression_constructor_exists():
    assert callable(EmigOcl_OclExpression.__init__)


def test_emigocl_oclexpression_constructor_args():
    sig = inspect.signature(EmigOcl_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_VariableDeclaration)


def test_emigocl_variabledeclaration_constructor_exists():
    assert callable(EmigOcl_VariableDeclaration.__init__)


def test_emigocl_variabledeclaration_constructor_args():
    sig = inspect.signature(EmigOcl_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_emigocl_variabledeclaration_has_varName():
    assert hasattr(EmigOcl_VariableDeclaration, "varName")
    descriptor = None
    for klass in EmigOcl_VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_oclfeature_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_OclFeature)


def test_emigocl_oclfeature_constructor_exists():
    assert callable(EmigOcl_OclFeature.__init__)


def test_emigocl_oclfeature_constructor_args():
    sig = inspect.signature(EmigOcl_OclFeature.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_emigocl_oclfeature_has_eq():
    assert hasattr(EmigOcl_OclFeature, "eq")
    descriptor = None
    for klass in EmigOcl_OclFeature.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_oclmodel_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_OclModel)


def test_emigocl_oclmodel_constructor_exists():
    assert callable(EmigOcl_OclModel.__init__)


def test_emigocl_oclmodel_constructor_args():
    sig = inspect.signature(EmigOcl_OclModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl_oclmodel_has_name():
    assert hasattr(EmigOcl_OclModel, "name")
    descriptor = None
    for klass in EmigOcl_OclModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_OclFeatureDefinition)


def test_emigocl_oclfeaturedefinition_constructor_exists():
    assert callable(EmigOcl_OclFeatureDefinition.__init__)


def test_emigocl_oclfeaturedefinition_constructor_args():
    sig = inspect.signature(EmigOcl_OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_emigocl_oclfeaturedefinition_has_static():
    assert hasattr(EmigOcl_OclFeatureDefinition, "static")
    descriptor = None
    for klass in EmigOcl_OclFeatureDefinition.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_mapelement_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_MapElement)


def test_emigocl_mapelement_constructor_exists():
    assert callable(EmigOcl_MapElement.__init__)


def test_emigocl_mapelement_constructor_args():
    sig = inspect.signature(EmigOcl_MapElement.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_OclContextDefinition)


def test_emigocl_oclcontextdefinition_constructor_exists():
    assert callable(EmigOcl_OclContextDefinition.__init__)


def test_emigocl_oclcontextdefinition_constructor_args():
    sig = inspect.signature(EmigOcl_OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_emigocl_ocltype_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_OclType)


def test_emigocl_ocltype_constructor_exists():
    assert callable(EmigOcl_OclType.__init__)


def test_emigocl_ocltype_constructor_args():
    sig = inspect.signature(EmigOcl_OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl_ocltype_has_name():
    assert hasattr(EmigOcl_OclType, "name")
    descriptor = None
    for klass in EmigOcl_OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_module_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_Module)


def test_emigocl_module_constructor_exists():
    assert callable(EmigOcl_Module.__init__)


def test_emigocl_module_constructor_args():
    sig = inspect.signature(EmigOcl_Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emigocl_module_has_name():
    assert hasattr(EmigOcl_Module, "name")
    descriptor = None
    for klass in EmigOcl_Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_locatedelement_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_LocatedElement)


def test_emigocl_locatedelement_constructor_exists():
    assert callable(EmigOcl_LocatedElement.__init__)


def test_emigocl_locatedelement_constructor_args():
    sig = inspect.signature(EmigOcl_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "charEnd" in params, "Missing parameter 'charEnd'"
    assert "line" in params, "Missing parameter 'line'"
    assert "column" in params, "Missing parameter 'column'"
    assert "charStart" in params, "Missing parameter 'charStart'"

def test_emigocl_locatedelement_has_charEnd():
    assert hasattr(EmigOcl_LocatedElement, "charEnd")
    descriptor = None
    for klass in EmigOcl_LocatedElement.__mro__:
        if "charEnd" in klass.__dict__:
            descriptor = klass.__dict__["charEnd"]
            break
    assert isinstance(descriptor, property)

def test_emigocl_locatedelement_has_line():
    assert hasattr(EmigOcl_LocatedElement, "line")
    descriptor = None
    for klass in EmigOcl_LocatedElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_emigocl_locatedelement_has_column():
    assert hasattr(EmigOcl_LocatedElement, "column")
    descriptor = None
    for klass in EmigOcl_LocatedElement.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)

def test_emigocl_locatedelement_has_charStart():
    assert hasattr(EmigOcl_LocatedElement, "charStart")
    descriptor = None
    for klass in EmigOcl_LocatedElement.__mro__:
        if "charStart" in klass.__dict__:
            descriptor = klass.__dict__["charStart"]
            break
    assert isinstance(descriptor, property)



def test_emigocl_letexp_is_not_abstract():
    assert not inspect.isabstract(EmigOcl_LetExp)


def test_emigocl_letexp_constructor_exists():
    assert callable(EmigOcl_LetExp.__init__)


def test_emigocl_letexp_constructor_args():
    sig = inspect.signature(EmigOcl_LetExp.__init__)
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
OclFeature_strategy = st.builds(
    OclFeature,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
EmigOcl_SetType_strategy = st.builds(
    EmigOcl_SetType,
)
EmigOcl_OrderedSetType_strategy = st.builds(
    EmigOcl_OrderedSetType,
)
EmigOcl_SequenceType_strategy = st.builds(
    EmigOcl_SequenceType,
)
EmigOcl_BagType_strategy = st.builds(
    EmigOcl_BagType,
)
NumericType_strategy = st.builds(
    NumericType,
)
EmigOcl_RealType_strategy = st.builds(
    EmigOcl_RealType,
)
EmigOcl_IntegerType_strategy = st.builds(
    EmigOcl_IntegerType,
)
Primitive_strategy = st.builds(
    Primitive,
)
EmigOcl_BooleanType_strategy = st.builds(
    EmigOcl_BooleanType,
)
EmigOcl_NumericType_strategy = st.builds(
    EmigOcl_NumericType,
)
EmigOcl_StringType_strategy = st.builds(
    EmigOcl_StringType,
)
OclType_strategy = st.builds(
    OclType,
)
EmigOcl_Primitive_strategy = st.builds(
    EmigOcl_Primitive,
)
EmigOcl_OclAnyType_strategy = st.builds(
    EmigOcl_OclAnyType,
)
EmigOcl_MapType_strategy = st.builds(
    EmigOcl_MapType,
)
EmigOcl_OclModelElement_strategy = st.builds(
    EmigOcl_OclModelElement,
)
EmigOcl_TupleType_strategy = st.builds(
    EmigOcl_TupleType,
)
EmigOcl_LambdaType_strategy = st.builds(
    EmigOcl_LambdaType,
)
EmigOcl_CollectionType_strategy = st.builds(
    EmigOcl_CollectionType,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
EmigOcl_Parameter_strategy = st.builds(
    EmigOcl_Parameter,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
EmigOcl_IteratorExp_strategy = st.builds(
    EmigOcl_IteratorExp,
    name=
        safe_text
)
EmigOcl_Iterator_strategy = st.builds(
    EmigOcl_Iterator,
)
EmigOcl_IterateExp_strategy = st.builds(
    EmigOcl_IterateExp,
)
OperationCall_strategy = st.builds(
    OperationCall,
)
EmigOcl_CollectionOperationCall_strategy = st.builds(
    EmigOcl_CollectionOperationCall,
)
VariableExp_strategy = st.builds(
    VariableExp,
)
EmigOcl_LambdaCallExp_strategy = st.builds(
    EmigOcl_LambdaCallExp,
)
OperatorCallExp_strategy = st.builds(
    OperatorCallExp,
)
EmigOcl_IntOpCallExp_strategy = st.builds(
    EmigOcl_IntOpCallExp,
)
EmigOcl_RelOpCallExp_strategy = st.builds(
    EmigOcl_RelOpCallExp,
)
EmigOcl_EqOpCallExp_strategy = st.builds(
    EmigOcl_EqOpCallExp,
)
EmigOcl_MulOpCallExp_strategy = st.builds(
    EmigOcl_MulOpCallExp,
)
EmigOcl_AddOpCallExp_strategy = st.builds(
    EmigOcl_AddOpCallExp,
)
EmigOcl_NotOpCallExp_strategy = st.builds(
    EmigOcl_NotOpCallExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
EmigOcl_OperatorCallExp_strategy = st.builds(
    EmigOcl_OperatorCallExp,
    operationName=
        safe_text
)
PropertyCall_strategy = st.builds(
    PropertyCall,
)
EmigOcl_NavigationOrAttributeCall_strategy = st.builds(
    EmigOcl_NavigationOrAttributeCall,
    name=
        safe_text
)
EmigOcl_PropertyCall_strategy = st.builds(
    EmigOcl_PropertyCall,
)
StaticPropertyCall_strategy = st.builds(
    StaticPropertyCall,
)
EmigOcl_StaticOperationCall_strategy = st.builds(
    EmigOcl_StaticOperationCall,
    operationName=
        safe_text
)
EmigOcl_StaticNavigationOrAttributeCall_strategy = st.builds(
    EmigOcl_StaticNavigationOrAttributeCall,
    name=
        safe_text
)
EmigOcl_StaticPropertyCall_strategy = st.builds(
    EmigOcl_StaticPropertyCall,
)
LocalVariable_strategy = st.builds(
    LocalVariable,
)
EmigOcl_TuplePart_strategy = st.builds(
    EmigOcl_TuplePart,
)
NumericExp_strategy = st.builds(
    NumericExp,
)
EmigOcl_IntegerExp_strategy = st.builds(
    EmigOcl_IntegerExp,
    integerSymbol=
        safe_text
)
EmigOcl_RealExp_strategy = st.builds(
    EmigOcl_RealExp,
    realSymbol=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
EmigOcl_BooleanExp_strategy = st.builds(
    EmigOcl_BooleanExp,
    booleanSymbol=
        safe_text
)
EmigOcl_NumericExp_strategy = st.builds(
    EmigOcl_NumericExp,
)
EmigOcl_StringExp_strategy = st.builds(
    EmigOcl_StringExp,
    stringSymbol=
        safe_text
)
OclExpression_strategy = st.builds(
    OclExpression,
)
EmigOcl_BraceExp_strategy = st.builds(
    EmigOcl_BraceExp,
)
EmigOcl_OclUndefinedExp_strategy = st.builds(
    EmigOcl_OclUndefinedExp,
)
EmigOcl_OclModelElementExp_strategy = st.builds(
    EmigOcl_OclModelElementExp,
    name=
        safe_text
)
EmigOcl_StaticPropertyCallExp_strategy = st.builds(
    EmigOcl_StaticPropertyCallExp,
)
EmigOcl_EnumLiteralExp_strategy = st.builds(
    EmigOcl_EnumLiteralExp,
    name=
        safe_text
)
EmigOcl_TupleExp_strategy = st.builds(
    EmigOcl_TupleExp,
)
EmigOcl_MapExp_strategy = st.builds(
    EmigOcl_MapExp,
)
EmigOcl_PrimitiveExp_strategy = st.builds(
    EmigOcl_PrimitiveExp,
)
EmigOcl_SelfExp_strategy = st.builds(
    EmigOcl_SelfExp,
)
EmigOcl_SuperExp_strategy = st.builds(
    EmigOcl_SuperExp,
)
EmigOcl_VariableExp_strategy = st.builds(
    EmigOcl_VariableExp,
)
EmigOcl_Attribute_strategy = st.builds(
    EmigOcl_Attribute,
    name=
        safe_text
)
EmigOcl_Operation_strategy = st.builds(
    EmigOcl_Operation,
    name=
        safe_text
)
EmigOcl_LocalVariable_strategy = st.builds(
    EmigOcl_LocalVariable,
    eq=
        safe_text
)
EmigOcl_OperationCall_strategy = st.builds(
    EmigOcl_OperationCall,
    operationName=
        safe_text
)
EmigOcl_LoopExp_strategy = st.builds(
    EmigOcl_LoopExp,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
EmigOcl_SequenceExp_strategy = st.builds(
    EmigOcl_SequenceExp,
)
EmigOcl_OrderedSetExp_strategy = st.builds(
    EmigOcl_OrderedSetExp,
)
EmigOcl_SetExp_strategy = st.builds(
    EmigOcl_SetExp,
)
EmigOcl_BagExp_strategy = st.builds(
    EmigOcl_BagExp,
)
EmigOcl_CollectionExp_strategy = st.builds(
    EmigOcl_CollectionExp,
)
EmigOcl_PropertyCallExp_strategy = st.builds(
    EmigOcl_PropertyCallExp,
)
EmigOcl_IfExp_strategy = st.builds(
    EmigOcl_IfExp,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
EmigOcl_TupleTypeAttribute_strategy = st.builds(
    EmigOcl_TupleTypeAttribute,
    name=
        safe_text
)
EmigOcl_OclExpression_strategy = st.builds(
    EmigOcl_OclExpression,
)
EmigOcl_VariableDeclaration_strategy = st.builds(
    EmigOcl_VariableDeclaration,
    varName=
        safe_text
)
EmigOcl_OclFeature_strategy = st.builds(
    EmigOcl_OclFeature,
    eq=
        safe_text
)
EmigOcl_OclModel_strategy = st.builds(
    EmigOcl_OclModel,
    name=
        safe_text
)
EmigOcl_OclFeatureDefinition_strategy = st.builds(
    EmigOcl_OclFeatureDefinition,
    static=
        safe_text
)
EmigOcl_MapElement_strategy = st.builds(
    EmigOcl_MapElement,
)
EmigOcl_OclContextDefinition_strategy = st.builds(
    EmigOcl_OclContextDefinition,
)
EmigOcl_OclType_strategy = st.builds(
    EmigOcl_OclType,
    name=
        safe_text
)
EmigOcl_Module_strategy = st.builds(
    EmigOcl_Module,
    name=
        safe_text
)
EmigOcl_LocatedElement_strategy = st.builds(
    EmigOcl_LocatedElement,
    charEnd=
        safe_text,
    line=
        safe_text,
    column=
        safe_text,
    charStart=
        safe_text
)
EmigOcl_LetExp_strategy = st.builds(
    EmigOcl_LetExp,
)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=EmigOcl_SetType_strategy)
@settings(max_examples=50)
def test_emigocl_settype_instantiation(instance):
    assert isinstance(instance, EmigOcl_SetType)

@given(instance=EmigOcl_OrderedSetType_strategy)
@settings(max_examples=50)
def test_emigocl_orderedsettype_instantiation(instance):
    assert isinstance(instance, EmigOcl_OrderedSetType)

@given(instance=EmigOcl_SequenceType_strategy)
@settings(max_examples=50)
def test_emigocl_sequencetype_instantiation(instance):
    assert isinstance(instance, EmigOcl_SequenceType)

@given(instance=EmigOcl_BagType_strategy)
@settings(max_examples=50)
def test_emigocl_bagtype_instantiation(instance):
    assert isinstance(instance, EmigOcl_BagType)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=EmigOcl_RealType_strategy)
@settings(max_examples=50)
def test_emigocl_realtype_instantiation(instance):
    assert isinstance(instance, EmigOcl_RealType)

@given(instance=EmigOcl_IntegerType_strategy)
@settings(max_examples=50)
def test_emigocl_integertype_instantiation(instance):
    assert isinstance(instance, EmigOcl_IntegerType)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=EmigOcl_BooleanType_strategy)
@settings(max_examples=50)
def test_emigocl_booleantype_instantiation(instance):
    assert isinstance(instance, EmigOcl_BooleanType)

@given(instance=EmigOcl_NumericType_strategy)
@settings(max_examples=50)
def test_emigocl_numerictype_instantiation(instance):
    assert isinstance(instance, EmigOcl_NumericType)

@given(instance=EmigOcl_StringType_strategy)
@settings(max_examples=50)
def test_emigocl_stringtype_instantiation(instance):
    assert isinstance(instance, EmigOcl_StringType)

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=EmigOcl_Primitive_strategy)
@settings(max_examples=50)
def test_emigocl_primitive_instantiation(instance):
    assert isinstance(instance, EmigOcl_Primitive)

@given(instance=EmigOcl_OclAnyType_strategy)
@settings(max_examples=50)
def test_emigocl_oclanytype_instantiation(instance):
    assert isinstance(instance, EmigOcl_OclAnyType)

@given(instance=EmigOcl_MapType_strategy)
@settings(max_examples=50)
def test_emigocl_maptype_instantiation(instance):
    assert isinstance(instance, EmigOcl_MapType)

@given(instance=EmigOcl_OclModelElement_strategy)
@settings(max_examples=50)
def test_emigocl_oclmodelelement_instantiation(instance):
    assert isinstance(instance, EmigOcl_OclModelElement)

@given(instance=EmigOcl_TupleType_strategy)
@settings(max_examples=50)
def test_emigocl_tupletype_instantiation(instance):
    assert isinstance(instance, EmigOcl_TupleType)

@given(instance=EmigOcl_LambdaType_strategy)
@settings(max_examples=50)
def test_emigocl_lambdatype_instantiation(instance):
    assert isinstance(instance, EmigOcl_LambdaType)

@given(instance=EmigOcl_CollectionType_strategy)
@settings(max_examples=50)
def test_emigocl_collectiontype_instantiation(instance):
    assert isinstance(instance, EmigOcl_CollectionType)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=EmigOcl_Parameter_strategy)
@settings(max_examples=50)
def test_emigocl_parameter_instantiation(instance):
    assert isinstance(instance, EmigOcl_Parameter)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=EmigOcl_IteratorExp_strategy)
@settings(max_examples=50)
def test_emigocl_iteratorexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_IteratorExp)



@given(instance=EmigOcl_IteratorExp_strategy)
def test_emigocl_iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl_Iterator_strategy)
@settings(max_examples=50)
def test_emigocl_iterator_instantiation(instance):
    assert isinstance(instance, EmigOcl_Iterator)

@given(instance=EmigOcl_IterateExp_strategy)
@settings(max_examples=50)
def test_emigocl_iterateexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_IterateExp)

@given(instance=OperationCall_strategy)
@settings(max_examples=50)
def test_operationcall_instantiation(instance):
    assert isinstance(instance, OperationCall)

@given(instance=EmigOcl_CollectionOperationCall_strategy)
@settings(max_examples=50)
def test_emigocl_collectionoperationcall_instantiation(instance):
    assert isinstance(instance, EmigOcl_CollectionOperationCall)

@given(instance=VariableExp_strategy)
@settings(max_examples=50)
def test_variableexp_instantiation(instance):
    assert isinstance(instance, VariableExp)

@given(instance=EmigOcl_LambdaCallExp_strategy)
@settings(max_examples=50)
def test_emigocl_lambdacallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_LambdaCallExp)

@given(instance=OperatorCallExp_strategy)
@settings(max_examples=50)
def test_operatorcallexp_instantiation(instance):
    assert isinstance(instance, OperatorCallExp)

@given(instance=EmigOcl_IntOpCallExp_strategy)
@settings(max_examples=50)
def test_emigocl_intopcallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_IntOpCallExp)

@given(instance=EmigOcl_RelOpCallExp_strategy)
@settings(max_examples=50)
def test_emigocl_relopcallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_RelOpCallExp)

@given(instance=EmigOcl_EqOpCallExp_strategy)
@settings(max_examples=50)
def test_emigocl_eqopcallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_EqOpCallExp)

@given(instance=EmigOcl_MulOpCallExp_strategy)
@settings(max_examples=50)
def test_emigocl_mulopcallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_MulOpCallExp)

@given(instance=EmigOcl_AddOpCallExp_strategy)
@settings(max_examples=50)
def test_emigocl_addopcallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_AddOpCallExp)

@given(instance=EmigOcl_NotOpCallExp_strategy)
@settings(max_examples=50)
def test_emigocl_notopcallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_NotOpCallExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=EmigOcl_OperatorCallExp_strategy)
@settings(max_examples=50)
def test_emigocl_operatorcallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_OperatorCallExp)



@given(instance=EmigOcl_OperatorCallExp_strategy)
def test_emigocl_operatorcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=PropertyCall_strategy)
@settings(max_examples=50)
def test_propertycall_instantiation(instance):
    assert isinstance(instance, PropertyCall)

@given(instance=EmigOcl_NavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_emigocl_navigationorattributecall_instantiation(instance):
    assert isinstance(instance, EmigOcl_NavigationOrAttributeCall)



@given(instance=EmigOcl_NavigationOrAttributeCall_strategy)
def test_emigocl_navigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl_PropertyCall_strategy)
@settings(max_examples=50)
def test_emigocl_propertycall_instantiation(instance):
    assert isinstance(instance, EmigOcl_PropertyCall)

@given(instance=StaticPropertyCall_strategy)
@settings(max_examples=50)
def test_staticpropertycall_instantiation(instance):
    assert isinstance(instance, StaticPropertyCall)

@given(instance=EmigOcl_StaticOperationCall_strategy)
@settings(max_examples=50)
def test_emigocl_staticoperationcall_instantiation(instance):
    assert isinstance(instance, EmigOcl_StaticOperationCall)



@given(instance=EmigOcl_StaticOperationCall_strategy)
def test_emigocl_staticoperationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=EmigOcl_StaticNavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_emigocl_staticnavigationorattributecall_instantiation(instance):
    assert isinstance(instance, EmigOcl_StaticNavigationOrAttributeCall)



@given(instance=EmigOcl_StaticNavigationOrAttributeCall_strategy)
def test_emigocl_staticnavigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl_StaticPropertyCall_strategy)
@settings(max_examples=50)
def test_emigocl_staticpropertycall_instantiation(instance):
    assert isinstance(instance, EmigOcl_StaticPropertyCall)

@given(instance=LocalVariable_strategy)
@settings(max_examples=50)
def test_localvariable_instantiation(instance):
    assert isinstance(instance, LocalVariable)

@given(instance=EmigOcl_TuplePart_strategy)
@settings(max_examples=50)
def test_emigocl_tuplepart_instantiation(instance):
    assert isinstance(instance, EmigOcl_TuplePart)

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=EmigOcl_IntegerExp_strategy)
@settings(max_examples=50)
def test_emigocl_integerexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_IntegerExp)



@given(instance=EmigOcl_IntegerExp_strategy)
def test_emigocl_integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=EmigOcl_RealExp_strategy)
@settings(max_examples=50)
def test_emigocl_realexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_RealExp)



@given(instance=EmigOcl_RealExp_strategy)
def test_emigocl_realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=EmigOcl_BooleanExp_strategy)
@settings(max_examples=50)
def test_emigocl_booleanexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_BooleanExp)



@given(instance=EmigOcl_BooleanExp_strategy)
def test_emigocl_booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=EmigOcl_NumericExp_strategy)
@settings(max_examples=50)
def test_emigocl_numericexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_NumericExp)

@given(instance=EmigOcl_StringExp_strategy)
@settings(max_examples=50)
def test_emigocl_stringexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_StringExp)



@given(instance=EmigOcl_StringExp_strategy)
def test_emigocl_stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=EmigOcl_BraceExp_strategy)
@settings(max_examples=50)
def test_emigocl_braceexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_BraceExp)

@given(instance=EmigOcl_OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_emigocl_oclundefinedexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_OclUndefinedExp)

@given(instance=EmigOcl_OclModelElementExp_strategy)
@settings(max_examples=50)
def test_emigocl_oclmodelelementexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_OclModelElementExp)



@given(instance=EmigOcl_OclModelElementExp_strategy)
def test_emigocl_oclmodelelementexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl_StaticPropertyCallExp_strategy)
@settings(max_examples=50)
def test_emigocl_staticpropertycallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_StaticPropertyCallExp)

@given(instance=EmigOcl_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_emigocl_enumliteralexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_EnumLiteralExp)



@given(instance=EmigOcl_EnumLiteralExp_strategy)
def test_emigocl_enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl_TupleExp_strategy)
@settings(max_examples=50)
def test_emigocl_tupleexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_TupleExp)

@given(instance=EmigOcl_MapExp_strategy)
@settings(max_examples=50)
def test_emigocl_mapexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_MapExp)

@given(instance=EmigOcl_PrimitiveExp_strategy)
@settings(max_examples=50)
def test_emigocl_primitiveexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_PrimitiveExp)

@given(instance=EmigOcl_SelfExp_strategy)
@settings(max_examples=50)
def test_emigocl_selfexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_SelfExp)

@given(instance=EmigOcl_SuperExp_strategy)
@settings(max_examples=50)
def test_emigocl_superexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_SuperExp)

@given(instance=EmigOcl_VariableExp_strategy)
@settings(max_examples=50)
def test_emigocl_variableexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_VariableExp)

@given(instance=EmigOcl_Attribute_strategy)
@settings(max_examples=50)
def test_emigocl_attribute_instantiation(instance):
    assert isinstance(instance, EmigOcl_Attribute)



@given(instance=EmigOcl_Attribute_strategy)
def test_emigocl_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl_Operation_strategy)
@settings(max_examples=50)
def test_emigocl_operation_instantiation(instance):
    assert isinstance(instance, EmigOcl_Operation)



@given(instance=EmigOcl_Operation_strategy)
def test_emigocl_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl_LocalVariable_strategy)
@settings(max_examples=50)
def test_emigocl_localvariable_instantiation(instance):
    assert isinstance(instance, EmigOcl_LocalVariable)



@given(instance=EmigOcl_LocalVariable_strategy)
def test_emigocl_localvariable_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=EmigOcl_OperationCall_strategy)
@settings(max_examples=50)
def test_emigocl_operationcall_instantiation(instance):
    assert isinstance(instance, EmigOcl_OperationCall)



@given(instance=EmigOcl_OperationCall_strategy)
def test_emigocl_operationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=EmigOcl_LoopExp_strategy)
@settings(max_examples=50)
def test_emigocl_loopexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_LoopExp)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=EmigOcl_SequenceExp_strategy)
@settings(max_examples=50)
def test_emigocl_sequenceexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_SequenceExp)

@given(instance=EmigOcl_OrderedSetExp_strategy)
@settings(max_examples=50)
def test_emigocl_orderedsetexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_OrderedSetExp)

@given(instance=EmigOcl_SetExp_strategy)
@settings(max_examples=50)
def test_emigocl_setexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_SetExp)

@given(instance=EmigOcl_BagExp_strategy)
@settings(max_examples=50)
def test_emigocl_bagexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_BagExp)

@given(instance=EmigOcl_CollectionExp_strategy)
@settings(max_examples=50)
def test_emigocl_collectionexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_CollectionExp)

@given(instance=EmigOcl_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_emigocl_propertycallexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_PropertyCallExp)

@given(instance=EmigOcl_IfExp_strategy)
@settings(max_examples=50)
def test_emigocl_ifexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_IfExp)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=EmigOcl_TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_emigocl_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, EmigOcl_TupleTypeAttribute)



@given(instance=EmigOcl_TupleTypeAttribute_strategy)
def test_emigocl_tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl_OclExpression_strategy)
@settings(max_examples=50)
def test_emigocl_oclexpression_instantiation(instance):
    assert isinstance(instance, EmigOcl_OclExpression)

@given(instance=EmigOcl_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_emigocl_variabledeclaration_instantiation(instance):
    assert isinstance(instance, EmigOcl_VariableDeclaration)



@given(instance=EmigOcl_VariableDeclaration_strategy)
def test_emigocl_variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=EmigOcl_OclFeature_strategy)
@settings(max_examples=50)
def test_emigocl_oclfeature_instantiation(instance):
    assert isinstance(instance, EmigOcl_OclFeature)



@given(instance=EmigOcl_OclFeature_strategy)
def test_emigocl_oclfeature_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=EmigOcl_OclModel_strategy)
@settings(max_examples=50)
def test_emigocl_oclmodel_instantiation(instance):
    assert isinstance(instance, EmigOcl_OclModel)



@given(instance=EmigOcl_OclModel_strategy)
def test_emigocl_oclmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl_OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_emigocl_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, EmigOcl_OclFeatureDefinition)



@given(instance=EmigOcl_OclFeatureDefinition_strategy)
def test_emigocl_oclfeaturedefinition_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=EmigOcl_MapElement_strategy)
@settings(max_examples=50)
def test_emigocl_mapelement_instantiation(instance):
    assert isinstance(instance, EmigOcl_MapElement)

@given(instance=EmigOcl_OclContextDefinition_strategy)
@settings(max_examples=50)
def test_emigocl_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, EmigOcl_OclContextDefinition)

@given(instance=EmigOcl_OclType_strategy)
@settings(max_examples=50)
def test_emigocl_ocltype_instantiation(instance):
    assert isinstance(instance, EmigOcl_OclType)



@given(instance=EmigOcl_OclType_strategy)
def test_emigocl_ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl_Module_strategy)
@settings(max_examples=50)
def test_emigocl_module_instantiation(instance):
    assert isinstance(instance, EmigOcl_Module)



@given(instance=EmigOcl_Module_strategy)
def test_emigocl_module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EmigOcl_LocatedElement_strategy)
@settings(max_examples=50)
def test_emigocl_locatedelement_instantiation(instance):
    assert isinstance(instance, EmigOcl_LocatedElement)



@given(instance=EmigOcl_LocatedElement_strategy)
def test_emigocl_locatedelement_charEnd_setter(instance):
    original = instance.charEnd
    instance.charEnd = original
    assert instance.charEnd == original



@given(instance=EmigOcl_LocatedElement_strategy)
def test_emigocl_locatedelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original



@given(instance=EmigOcl_LocatedElement_strategy)
def test_emigocl_locatedelement_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original



@given(instance=EmigOcl_LocatedElement_strategy)
def test_emigocl_locatedelement_charStart_setter(instance):
    original = instance.charStart
    instance.charStart = original
    assert instance.charStart == original

@given(instance=EmigOcl_LetExp_strategy)
@settings(max_examples=50)
def test_emigocl_letexp_instantiation(instance):
    assert isinstance(instance, EmigOcl_LetExp)
