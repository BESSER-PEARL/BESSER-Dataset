import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    OclModel,
    simpleocl_OclInstanceModel,
    OclFeature,
    ModuleElement,
    simpleocl_OclFeatureDefinition,
    CollectionType,
    simpleocl_SetType,
    simpleocl_OrderedSetType,
    simpleocl_SequenceType,
    simpleocl_BagType,
    NumericType,
    simpleocl_RealType,
    simpleocl_IntegerType,
    Primitive,
    simpleocl_NumericType,
    simpleocl_BooleanType,
    simpleocl_StringType,
    VariableDeclaration,
    simpleocl_Parameter,
    OclType,
    simpleocl_TupleType,
    simpleocl_MapType,
    simpleocl_EnvType,
    simpleocl_Primitive,
    simpleocl_OclModelElement,
    simpleocl_OclAnyType,
    simpleocl_LambdaType,
    simpleocl_CollectionType,
    LoopExp,
    simpleocl_IteratorExp,
    simpleocl_IterateExp,
    simpleocl_Iterator,
    OperationCall,
    simpleocl_CollectionOperationCall,
    VariableExp,
    simpleocl_LambdaCallExp,
    OperatorCallExp,
    simpleocl_AddOpCallExp,
    simpleocl_IntOpCallExp,
    simpleocl_RelOpCallExp,
    simpleocl_MulOpCallExp,
    simpleocl_EqOpCallExp,
    simpleocl_NotOpCallExp,
    PropertyCall,
    simpleocl_NavigationOrAttributeCall,
    StaticPropertyCall,
    simpleocl_StaticOperationCall,
    simpleocl_StaticNavigationOrAttributeCall,
    LocalVariable,
    simpleocl_TuplePart,
    CollectionExp,
    simpleocl_SetExp,
    simpleocl_OrderedSetExp,
    simpleocl_SequenceExp,
    simpleocl_BagExp,
    CollectionPart,
    simpleocl_CollectionItem,
    simpleocl_CollectionRange,
    PrimitiveExp,
    simpleocl_BooleanExp,
    simpleocl_StringExp,
    OclExpression,
    simpleocl_PrimitiveExp,
    simpleocl_BraceExp,
    simpleocl_OclModelElementExp,
    simpleocl_EnumLiteralExp,
    simpleocl_CollectionExp,
    simpleocl_SuperExp,
    simpleocl_MapExp,
    simpleocl_TupleExp,
    simpleocl_StaticPropertyCallExp,
    simpleocl_OclUndefinedExp,
    simpleocl_SelfExp,
    simpleocl_EnvExp,
    simpleocl_VariableExp,
    simpleocl_OperatorCallExp,
    simpleocl_Attribute,
    NumericExp,
    simpleocl_IntegerExp,
    simpleocl_RealExp,
    simpleocl_NumericExp,
    simpleocl_Operation,
    simpleocl_LocalVariable,
    simpleocl_OperationCall,
    simpleocl_LoopExp,
    simpleocl_LetExp,
    simpleocl_PropertyCallExp,
    simpleocl_IfExp,
    simpleocl_OclMetamodel,
    NamedElement,
    simpleocl_OclFeature,
    simpleocl_OclModel,
    simpleocl_Module,
    LocatedElement,
    simpleocl_PropertyCall,
    simpleocl_OclType,
    simpleocl_OclContextDefinition,
    simpleocl_OclExpression,
    simpleocl_VariableDeclaration,
    simpleocl_TupleTypeAttribute,
    simpleocl_MapElement,
    simpleocl_StaticPropertyCall,
    simpleocl_ModuleElement,
    simpleocl_CollectionPart,
    simpleocl_NamedElement,
    simpleocl_LocatedElement,
    simpleocl_Import,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclmodel_is_not_abstract():
    assert not inspect.isabstract(OclModel)


def test_oclmodel_constructor_exists():
    assert callable(OclModel.__init__)


def test_oclmodel_constructor_args():
    sig = inspect.signature(OclModel.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_oclinstancemodel_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OclInstanceModel)


def test_simpleocl_oclinstancemodel_constructor_exists():
    assert callable(simpleocl_OclInstanceModel.__init__)


def test_simpleocl_oclinstancemodel_constructor_args():
    sig = inspect.signature(simpleocl_OclInstanceModel.__init__)
    params = list(sig.parameters.keys())



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OclFeatureDefinition)


def test_simpleocl_oclfeaturedefinition_constructor_exists():
    assert callable(simpleocl_OclFeatureDefinition.__init__)


def test_simpleocl_oclfeaturedefinition_constructor_args():
    sig = inspect.signature(simpleocl_OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_simpleocl_oclfeaturedefinition_has_static():
    assert hasattr(simpleocl_OclFeatureDefinition, "static")
    descriptor = None
    for klass in simpleocl_OclFeatureDefinition.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_settype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_SetType)


def test_simpleocl_settype_constructor_exists():
    assert callable(simpleocl_SetType.__init__)


def test_simpleocl_settype_constructor_args():
    sig = inspect.signature(simpleocl_SetType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OrderedSetType)


def test_simpleocl_orderedsettype_constructor_exists():
    assert callable(simpleocl_OrderedSetType.__init__)


def test_simpleocl_orderedsettype_constructor_args():
    sig = inspect.signature(simpleocl_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_sequencetype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_SequenceType)


def test_simpleocl_sequencetype_constructor_exists():
    assert callable(simpleocl_SequenceType.__init__)


def test_simpleocl_sequencetype_constructor_args():
    sig = inspect.signature(simpleocl_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_bagtype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_BagType)


def test_simpleocl_bagtype_constructor_exists():
    assert callable(simpleocl_BagType.__init__)


def test_simpleocl_bagtype_constructor_args():
    sig = inspect.signature(simpleocl_BagType.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_realtype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_RealType)


def test_simpleocl_realtype_constructor_exists():
    assert callable(simpleocl_RealType.__init__)


def test_simpleocl_realtype_constructor_args():
    sig = inspect.signature(simpleocl_RealType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_integertype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_IntegerType)


def test_simpleocl_integertype_constructor_exists():
    assert callable(simpleocl_IntegerType.__init__)


def test_simpleocl_integertype_constructor_args():
    sig = inspect.signature(simpleocl_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_numerictype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_NumericType)


def test_simpleocl_numerictype_constructor_exists():
    assert callable(simpleocl_NumericType.__init__)


def test_simpleocl_numerictype_constructor_args():
    sig = inspect.signature(simpleocl_NumericType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_booleantype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_BooleanType)


def test_simpleocl_booleantype_constructor_exists():
    assert callable(simpleocl_BooleanType.__init__)


def test_simpleocl_booleantype_constructor_args():
    sig = inspect.signature(simpleocl_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_stringtype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_StringType)


def test_simpleocl_stringtype_constructor_exists():
    assert callable(simpleocl_StringType.__init__)


def test_simpleocl_stringtype_constructor_args():
    sig = inspect.signature(simpleocl_StringType.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_parameter_is_not_abstract():
    assert not inspect.isabstract(simpleocl_Parameter)


def test_simpleocl_parameter_constructor_exists():
    assert callable(simpleocl_Parameter.__init__)


def test_simpleocl_parameter_constructor_args():
    sig = inspect.signature(simpleocl_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_ocltype_is_not_abstract():
    assert not inspect.isabstract(OclType)


def test_ocltype_constructor_exists():
    assert callable(OclType.__init__)


def test_ocltype_constructor_args():
    sig = inspect.signature(OclType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_tupletype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_TupleType)


def test_simpleocl_tupletype_constructor_exists():
    assert callable(simpleocl_TupleType.__init__)


def test_simpleocl_tupletype_constructor_args():
    sig = inspect.signature(simpleocl_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_maptype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_MapType)


def test_simpleocl_maptype_constructor_exists():
    assert callable(simpleocl_MapType.__init__)


def test_simpleocl_maptype_constructor_args():
    sig = inspect.signature(simpleocl_MapType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_envtype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_EnvType)


def test_simpleocl_envtype_constructor_exists():
    assert callable(simpleocl_EnvType.__init__)


def test_simpleocl_envtype_constructor_args():
    sig = inspect.signature(simpleocl_EnvType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_primitive_is_not_abstract():
    assert not inspect.isabstract(simpleocl_Primitive)


def test_simpleocl_primitive_constructor_exists():
    assert callable(simpleocl_Primitive.__init__)


def test_simpleocl_primitive_constructor_args():
    sig = inspect.signature(simpleocl_Primitive.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OclModelElement)


def test_simpleocl_oclmodelelement_constructor_exists():
    assert callable(simpleocl_OclModelElement.__init__)


def test_simpleocl_oclmodelelement_constructor_args():
    sig = inspect.signature(simpleocl_OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_oclanytype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OclAnyType)


def test_simpleocl_oclanytype_constructor_exists():
    assert callable(simpleocl_OclAnyType.__init__)


def test_simpleocl_oclanytype_constructor_args():
    sig = inspect.signature(simpleocl_OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_lambdatype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_LambdaType)


def test_simpleocl_lambdatype_constructor_exists():
    assert callable(simpleocl_LambdaType.__init__)


def test_simpleocl_lambdatype_constructor_args():
    sig = inspect.signature(simpleocl_LambdaType.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_collectiontype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_CollectionType)


def test_simpleocl_collectiontype_constructor_exists():
    assert callable(simpleocl_CollectionType.__init__)


def test_simpleocl_collectiontype_constructor_args():
    sig = inspect.signature(simpleocl_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_IteratorExp)


def test_simpleocl_iteratorexp_constructor_exists():
    assert callable(simpleocl_IteratorExp.__init__)


def test_simpleocl_iteratorexp_constructor_args():
    sig = inspect.signature(simpleocl_IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl_iteratorexp_has_name():
    assert hasattr(simpleocl_IteratorExp, "name")
    descriptor = None
    for klass in simpleocl_IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_iterateexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_IterateExp)


def test_simpleocl_iterateexp_constructor_exists():
    assert callable(simpleocl_IterateExp.__init__)


def test_simpleocl_iterateexp_constructor_args():
    sig = inspect.signature(simpleocl_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_iterator_is_not_abstract():
    assert not inspect.isabstract(simpleocl_Iterator)


def test_simpleocl_iterator_constructor_exists():
    assert callable(simpleocl_Iterator.__init__)


def test_simpleocl_iterator_constructor_args():
    sig = inspect.signature(simpleocl_Iterator.__init__)
    params = list(sig.parameters.keys())



def test_operationcall_is_not_abstract():
    assert not inspect.isabstract(OperationCall)


def test_operationcall_constructor_exists():
    assert callable(OperationCall.__init__)


def test_operationcall_constructor_args():
    sig = inspect.signature(OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_collectionoperationcall_is_not_abstract():
    assert not inspect.isabstract(simpleocl_CollectionOperationCall)


def test_simpleocl_collectionoperationcall_constructor_exists():
    assert callable(simpleocl_CollectionOperationCall.__init__)


def test_simpleocl_collectionoperationcall_constructor_args():
    sig = inspect.signature(simpleocl_CollectionOperationCall.__init__)
    params = list(sig.parameters.keys())



def test_variableexp_is_not_abstract():
    assert not inspect.isabstract(VariableExp)


def test_variableexp_constructor_exists():
    assert callable(VariableExp.__init__)


def test_variableexp_constructor_args():
    sig = inspect.signature(VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_lambdacallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_LambdaCallExp)


def test_simpleocl_lambdacallexp_constructor_exists():
    assert callable(simpleocl_LambdaCallExp.__init__)


def test_simpleocl_lambdacallexp_constructor_args():
    sig = inspect.signature(simpleocl_LambdaCallExp.__init__)
    params = list(sig.parameters.keys())



def test_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OperatorCallExp)


def test_operatorcallexp_constructor_exists():
    assert callable(OperatorCallExp.__init__)


def test_operatorcallexp_constructor_args():
    sig = inspect.signature(OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_addopcallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_AddOpCallExp)


def test_simpleocl_addopcallexp_constructor_exists():
    assert callable(simpleocl_AddOpCallExp.__init__)


def test_simpleocl_addopcallexp_constructor_args():
    sig = inspect.signature(simpleocl_AddOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_intopcallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_IntOpCallExp)


def test_simpleocl_intopcallexp_constructor_exists():
    assert callable(simpleocl_IntOpCallExp.__init__)


def test_simpleocl_intopcallexp_constructor_args():
    sig = inspect.signature(simpleocl_IntOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_relopcallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_RelOpCallExp)


def test_simpleocl_relopcallexp_constructor_exists():
    assert callable(simpleocl_RelOpCallExp.__init__)


def test_simpleocl_relopcallexp_constructor_args():
    sig = inspect.signature(simpleocl_RelOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_mulopcallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_MulOpCallExp)


def test_simpleocl_mulopcallexp_constructor_exists():
    assert callable(simpleocl_MulOpCallExp.__init__)


def test_simpleocl_mulopcallexp_constructor_args():
    sig = inspect.signature(simpleocl_MulOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_eqopcallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_EqOpCallExp)


def test_simpleocl_eqopcallexp_constructor_exists():
    assert callable(simpleocl_EqOpCallExp.__init__)


def test_simpleocl_eqopcallexp_constructor_args():
    sig = inspect.signature(simpleocl_EqOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_notopcallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_NotOpCallExp)


def test_simpleocl_notopcallexp_constructor_exists():
    assert callable(simpleocl_NotOpCallExp.__init__)


def test_simpleocl_notopcallexp_constructor_args():
    sig = inspect.signature(simpleocl_NotOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycall_is_not_abstract():
    assert not inspect.isabstract(PropertyCall)


def test_propertycall_constructor_exists():
    assert callable(PropertyCall.__init__)


def test_propertycall_constructor_args():
    sig = inspect.signature(PropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_navigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(simpleocl_NavigationOrAttributeCall)


def test_simpleocl_navigationorattributecall_constructor_exists():
    assert callable(simpleocl_NavigationOrAttributeCall.__init__)


def test_simpleocl_navigationorattributecall_constructor_args():
    sig = inspect.signature(simpleocl_NavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl_navigationorattributecall_has_name():
    assert hasattr(simpleocl_NavigationOrAttributeCall, "name")
    descriptor = None
    for klass in simpleocl_NavigationOrAttributeCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_staticpropertycall_is_not_abstract():
    assert not inspect.isabstract(StaticPropertyCall)


def test_staticpropertycall_constructor_exists():
    assert callable(StaticPropertyCall.__init__)


def test_staticpropertycall_constructor_args():
    sig = inspect.signature(StaticPropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_staticoperationcall_is_not_abstract():
    assert not inspect.isabstract(simpleocl_StaticOperationCall)


def test_simpleocl_staticoperationcall_constructor_exists():
    assert callable(simpleocl_StaticOperationCall.__init__)


def test_simpleocl_staticoperationcall_constructor_args():
    sig = inspect.signature(simpleocl_StaticOperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_simpleocl_staticoperationcall_has_operationName():
    assert hasattr(simpleocl_StaticOperationCall, "operationName")
    descriptor = None
    for klass in simpleocl_StaticOperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_staticnavigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(simpleocl_StaticNavigationOrAttributeCall)


def test_simpleocl_staticnavigationorattributecall_constructor_exists():
    assert callable(simpleocl_StaticNavigationOrAttributeCall.__init__)


def test_simpleocl_staticnavigationorattributecall_constructor_args():
    sig = inspect.signature(simpleocl_StaticNavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl_staticnavigationorattributecall_has_name():
    assert hasattr(simpleocl_StaticNavigationOrAttributeCall, "name")
    descriptor = None
    for klass in simpleocl_StaticNavigationOrAttributeCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_localvariable_is_not_abstract():
    assert not inspect.isabstract(LocalVariable)


def test_localvariable_constructor_exists():
    assert callable(LocalVariable.__init__)


def test_localvariable_constructor_args():
    sig = inspect.signature(LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_tuplepart_is_not_abstract():
    assert not inspect.isabstract(simpleocl_TuplePart)


def test_simpleocl_tuplepart_constructor_exists():
    assert callable(simpleocl_TuplePart.__init__)


def test_simpleocl_tuplepart_constructor_args():
    sig = inspect.signature(simpleocl_TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_setexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_SetExp)


def test_simpleocl_setexp_constructor_exists():
    assert callable(simpleocl_SetExp.__init__)


def test_simpleocl_setexp_constructor_args():
    sig = inspect.signature(simpleocl_SetExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OrderedSetExp)


def test_simpleocl_orderedsetexp_constructor_exists():
    assert callable(simpleocl_OrderedSetExp.__init__)


def test_simpleocl_orderedsetexp_constructor_args():
    sig = inspect.signature(simpleocl_OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_sequenceexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_SequenceExp)


def test_simpleocl_sequenceexp_constructor_exists():
    assert callable(simpleocl_SequenceExp.__init__)


def test_simpleocl_sequenceexp_constructor_args():
    sig = inspect.signature(simpleocl_SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_bagexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_BagExp)


def test_simpleocl_bagexp_constructor_exists():
    assert callable(simpleocl_BagExp.__init__)


def test_simpleocl_bagexp_constructor_args():
    sig = inspect.signature(simpleocl_BagExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionpart_is_not_abstract():
    assert not inspect.isabstract(CollectionPart)


def test_collectionpart_constructor_exists():
    assert callable(CollectionPart.__init__)


def test_collectionpart_constructor_args():
    sig = inspect.signature(CollectionPart.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_collectionitem_is_not_abstract():
    assert not inspect.isabstract(simpleocl_CollectionItem)


def test_simpleocl_collectionitem_constructor_exists():
    assert callable(simpleocl_CollectionItem.__init__)


def test_simpleocl_collectionitem_constructor_args():
    sig = inspect.signature(simpleocl_CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_collectionrange_is_not_abstract():
    assert not inspect.isabstract(simpleocl_CollectionRange)


def test_simpleocl_collectionrange_constructor_exists():
    assert callable(simpleocl_CollectionRange.__init__)


def test_simpleocl_collectionrange_constructor_args():
    sig = inspect.signature(simpleocl_CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_booleanexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_BooleanExp)


def test_simpleocl_booleanexp_constructor_exists():
    assert callable(simpleocl_BooleanExp.__init__)


def test_simpleocl_booleanexp_constructor_args():
    sig = inspect.signature(simpleocl_BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_simpleocl_booleanexp_has_booleanSymbol():
    assert hasattr(simpleocl_BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in simpleocl_BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_stringexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_StringExp)


def test_simpleocl_stringexp_constructor_exists():
    assert callable(simpleocl_StringExp.__init__)


def test_simpleocl_stringexp_constructor_args():
    sig = inspect.signature(simpleocl_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_simpleocl_stringexp_has_stringSymbol():
    assert hasattr(simpleocl_StringExp, "stringSymbol")
    descriptor = None
    for klass in simpleocl_StringExp.__mro__:
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



def test_simpleocl_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_PrimitiveExp)


def test_simpleocl_primitiveexp_constructor_exists():
    assert callable(simpleocl_PrimitiveExp.__init__)


def test_simpleocl_primitiveexp_constructor_args():
    sig = inspect.signature(simpleocl_PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_braceexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_BraceExp)


def test_simpleocl_braceexp_constructor_exists():
    assert callable(simpleocl_BraceExp.__init__)


def test_simpleocl_braceexp_constructor_args():
    sig = inspect.signature(simpleocl_BraceExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_oclmodelelementexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OclModelElementExp)


def test_simpleocl_oclmodelelementexp_constructor_exists():
    assert callable(simpleocl_OclModelElementExp.__init__)


def test_simpleocl_oclmodelelementexp_constructor_args():
    sig = inspect.signature(simpleocl_OclModelElementExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl_oclmodelelementexp_has_name():
    assert hasattr(simpleocl_OclModelElementExp, "name")
    descriptor = None
    for klass in simpleocl_OclModelElementExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_EnumLiteralExp)


def test_simpleocl_enumliteralexp_constructor_exists():
    assert callable(simpleocl_EnumLiteralExp.__init__)


def test_simpleocl_enumliteralexp_constructor_args():
    sig = inspect.signature(simpleocl_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl_enumliteralexp_has_name():
    assert hasattr(simpleocl_EnumLiteralExp, "name")
    descriptor = None
    for klass in simpleocl_EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_collectionexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_CollectionExp)


def test_simpleocl_collectionexp_constructor_exists():
    assert callable(simpleocl_CollectionExp.__init__)


def test_simpleocl_collectionexp_constructor_args():
    sig = inspect.signature(simpleocl_CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_superexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_SuperExp)


def test_simpleocl_superexp_constructor_exists():
    assert callable(simpleocl_SuperExp.__init__)


def test_simpleocl_superexp_constructor_args():
    sig = inspect.signature(simpleocl_SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_mapexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_MapExp)


def test_simpleocl_mapexp_constructor_exists():
    assert callable(simpleocl_MapExp.__init__)


def test_simpleocl_mapexp_constructor_args():
    sig = inspect.signature(simpleocl_MapExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_tupleexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_TupleExp)


def test_simpleocl_tupleexp_constructor_exists():
    assert callable(simpleocl_TupleExp.__init__)


def test_simpleocl_tupleexp_constructor_args():
    sig = inspect.signature(simpleocl_TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_staticpropertycallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_StaticPropertyCallExp)


def test_simpleocl_staticpropertycallexp_constructor_exists():
    assert callable(simpleocl_StaticPropertyCallExp.__init__)


def test_simpleocl_staticpropertycallexp_constructor_args():
    sig = inspect.signature(simpleocl_StaticPropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OclUndefinedExp)


def test_simpleocl_oclundefinedexp_constructor_exists():
    assert callable(simpleocl_OclUndefinedExp.__init__)


def test_simpleocl_oclundefinedexp_constructor_args():
    sig = inspect.signature(simpleocl_OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_selfexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_SelfExp)


def test_simpleocl_selfexp_constructor_exists():
    assert callable(simpleocl_SelfExp.__init__)


def test_simpleocl_selfexp_constructor_args():
    sig = inspect.signature(simpleocl_SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_envexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_EnvExp)


def test_simpleocl_envexp_constructor_exists():
    assert callable(simpleocl_EnvExp.__init__)


def test_simpleocl_envexp_constructor_args():
    sig = inspect.signature(simpleocl_EnvExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_variableexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_VariableExp)


def test_simpleocl_variableexp_constructor_exists():
    assert callable(simpleocl_VariableExp.__init__)


def test_simpleocl_variableexp_constructor_args():
    sig = inspect.signature(simpleocl_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OperatorCallExp)


def test_simpleocl_operatorcallexp_constructor_exists():
    assert callable(simpleocl_OperatorCallExp.__init__)


def test_simpleocl_operatorcallexp_constructor_args():
    sig = inspect.signature(simpleocl_OperatorCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_simpleocl_operatorcallexp_has_operationName():
    assert hasattr(simpleocl_OperatorCallExp, "operationName")
    descriptor = None
    for klass in simpleocl_OperatorCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_attribute_is_not_abstract():
    assert not inspect.isabstract(simpleocl_Attribute)


def test_simpleocl_attribute_constructor_exists():
    assert callable(simpleocl_Attribute.__init__)


def test_simpleocl_attribute_constructor_args():
    sig = inspect.signature(simpleocl_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_integerexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_IntegerExp)


def test_simpleocl_integerexp_constructor_exists():
    assert callable(simpleocl_IntegerExp.__init__)


def test_simpleocl_integerexp_constructor_args():
    sig = inspect.signature(simpleocl_IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_simpleocl_integerexp_has_integerSymbol():
    assert hasattr(simpleocl_IntegerExp, "integerSymbol")
    descriptor = None
    for klass in simpleocl_IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_realexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_RealExp)


def test_simpleocl_realexp_constructor_exists():
    assert callable(simpleocl_RealExp.__init__)


def test_simpleocl_realexp_constructor_args():
    sig = inspect.signature(simpleocl_RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_simpleocl_realexp_has_realSymbol():
    assert hasattr(simpleocl_RealExp, "realSymbol")
    descriptor = None
    for klass in simpleocl_RealExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_numericexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_NumericExp)


def test_simpleocl_numericexp_constructor_exists():
    assert callable(simpleocl_NumericExp.__init__)


def test_simpleocl_numericexp_constructor_args():
    sig = inspect.signature(simpleocl_NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_operation_is_not_abstract():
    assert not inspect.isabstract(simpleocl_Operation)


def test_simpleocl_operation_constructor_exists():
    assert callable(simpleocl_Operation.__init__)


def test_simpleocl_operation_constructor_args():
    sig = inspect.signature(simpleocl_Operation.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_localvariable_is_not_abstract():
    assert not inspect.isabstract(simpleocl_LocalVariable)


def test_simpleocl_localvariable_constructor_exists():
    assert callable(simpleocl_LocalVariable.__init__)


def test_simpleocl_localvariable_constructor_args():
    sig = inspect.signature(simpleocl_LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_simpleocl_localvariable_has_eq():
    assert hasattr(simpleocl_LocalVariable, "eq")
    descriptor = None
    for klass in simpleocl_LocalVariable.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_operationcall_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OperationCall)


def test_simpleocl_operationcall_constructor_exists():
    assert callable(simpleocl_OperationCall.__init__)


def test_simpleocl_operationcall_constructor_args():
    sig = inspect.signature(simpleocl_OperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_simpleocl_operationcall_has_operationName():
    assert hasattr(simpleocl_OperationCall, "operationName")
    descriptor = None
    for klass in simpleocl_OperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_LoopExp)


def test_simpleocl_loopexp_constructor_exists():
    assert callable(simpleocl_LoopExp.__init__)


def test_simpleocl_loopexp_constructor_args():
    sig = inspect.signature(simpleocl_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_letexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_LetExp)


def test_simpleocl_letexp_constructor_exists():
    assert callable(simpleocl_LetExp.__init__)


def test_simpleocl_letexp_constructor_args():
    sig = inspect.signature(simpleocl_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_PropertyCallExp)


def test_simpleocl_propertycallexp_constructor_exists():
    assert callable(simpleocl_PropertyCallExp.__init__)


def test_simpleocl_propertycallexp_constructor_args():
    sig = inspect.signature(simpleocl_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_ifexp_is_not_abstract():
    assert not inspect.isabstract(simpleocl_IfExp)


def test_simpleocl_ifexp_constructor_exists():
    assert callable(simpleocl_IfExp.__init__)


def test_simpleocl_ifexp_constructor_args():
    sig = inspect.signature(simpleocl_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_oclmetamodel_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OclMetamodel)


def test_simpleocl_oclmetamodel_constructor_exists():
    assert callable(simpleocl_OclMetamodel.__init__)


def test_simpleocl_oclmetamodel_constructor_args():
    sig = inspect.signature(simpleocl_OclMetamodel.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_simpleocl_oclmetamodel_has_uri():
    assert hasattr(simpleocl_OclMetamodel, "uri")
    descriptor = None
    for klass in simpleocl_OclMetamodel.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_oclfeature_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OclFeature)


def test_simpleocl_oclfeature_constructor_exists():
    assert callable(simpleocl_OclFeature.__init__)


def test_simpleocl_oclfeature_constructor_args():
    sig = inspect.signature(simpleocl_OclFeature.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_simpleocl_oclfeature_has_eq():
    assert hasattr(simpleocl_OclFeature, "eq")
    descriptor = None
    for klass in simpleocl_OclFeature.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_oclmodel_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OclModel)


def test_simpleocl_oclmodel_constructor_exists():
    assert callable(simpleocl_OclModel.__init__)


def test_simpleocl_oclmodel_constructor_args():
    sig = inspect.signature(simpleocl_OclModel.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_module_is_not_abstract():
    assert not inspect.isabstract(simpleocl_Module)


def test_simpleocl_module_constructor_exists():
    assert callable(simpleocl_Module.__init__)


def test_simpleocl_module_constructor_args():
    sig = inspect.signature(simpleocl_Module.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_propertycall_is_not_abstract():
    assert not inspect.isabstract(simpleocl_PropertyCall)


def test_simpleocl_propertycall_constructor_exists():
    assert callable(simpleocl_PropertyCall.__init__)


def test_simpleocl_propertycall_constructor_args():
    sig = inspect.signature(simpleocl_PropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_ocltype_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OclType)


def test_simpleocl_ocltype_constructor_exists():
    assert callable(simpleocl_OclType.__init__)


def test_simpleocl_ocltype_constructor_args():
    sig = inspect.signature(simpleocl_OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl_ocltype_has_name():
    assert hasattr(simpleocl_OclType, "name")
    descriptor = None
    for klass in simpleocl_OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OclContextDefinition)


def test_simpleocl_oclcontextdefinition_constructor_exists():
    assert callable(simpleocl_OclContextDefinition.__init__)


def test_simpleocl_oclcontextdefinition_constructor_args():
    sig = inspect.signature(simpleocl_OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(simpleocl_OclExpression)


def test_simpleocl_oclexpression_constructor_exists():
    assert callable(simpleocl_OclExpression.__init__)


def test_simpleocl_oclexpression_constructor_args():
    sig = inspect.signature(simpleocl_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(simpleocl_VariableDeclaration)


def test_simpleocl_variabledeclaration_constructor_exists():
    assert callable(simpleocl_VariableDeclaration.__init__)


def test_simpleocl_variabledeclaration_constructor_args():
    sig = inspect.signature(simpleocl_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_simpleocl_variabledeclaration_has_varName():
    assert hasattr(simpleocl_VariableDeclaration, "varName")
    descriptor = None
    for klass in simpleocl_VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(simpleocl_TupleTypeAttribute)


def test_simpleocl_tupletypeattribute_constructor_exists():
    assert callable(simpleocl_TupleTypeAttribute.__init__)


def test_simpleocl_tupletypeattribute_constructor_args():
    sig = inspect.signature(simpleocl_TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl_tupletypeattribute_has_name():
    assert hasattr(simpleocl_TupleTypeAttribute, "name")
    descriptor = None
    for klass in simpleocl_TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_mapelement_is_not_abstract():
    assert not inspect.isabstract(simpleocl_MapElement)


def test_simpleocl_mapelement_constructor_exists():
    assert callable(simpleocl_MapElement.__init__)


def test_simpleocl_mapelement_constructor_args():
    sig = inspect.signature(simpleocl_MapElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_staticpropertycall_is_not_abstract():
    assert not inspect.isabstract(simpleocl_StaticPropertyCall)


def test_simpleocl_staticpropertycall_constructor_exists():
    assert callable(simpleocl_StaticPropertyCall.__init__)


def test_simpleocl_staticpropertycall_constructor_args():
    sig = inspect.signature(simpleocl_StaticPropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_moduleelement_is_not_abstract():
    assert not inspect.isabstract(simpleocl_ModuleElement)


def test_simpleocl_moduleelement_constructor_exists():
    assert callable(simpleocl_ModuleElement.__init__)


def test_simpleocl_moduleelement_constructor_args():
    sig = inspect.signature(simpleocl_ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_collectionpart_is_not_abstract():
    assert not inspect.isabstract(simpleocl_CollectionPart)


def test_simpleocl_collectionpart_constructor_exists():
    assert callable(simpleocl_CollectionPart.__init__)


def test_simpleocl_collectionpart_constructor_args():
    sig = inspect.signature(simpleocl_CollectionPart.__init__)
    params = list(sig.parameters.keys())



def test_simpleocl_namedelement_is_not_abstract():
    assert not inspect.isabstract(simpleocl_NamedElement)


def test_simpleocl_namedelement_constructor_exists():
    assert callable(simpleocl_NamedElement.__init__)


def test_simpleocl_namedelement_constructor_args():
    sig = inspect.signature(simpleocl_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleocl_namedelement_has_name():
    assert hasattr(simpleocl_NamedElement, "name")
    descriptor = None
    for klass in simpleocl_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_locatedelement_is_not_abstract():
    assert not inspect.isabstract(simpleocl_LocatedElement)


def test_simpleocl_locatedelement_constructor_exists():
    assert callable(simpleocl_LocatedElement.__init__)


def test_simpleocl_locatedelement_constructor_args():
    sig = inspect.signature(simpleocl_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"
    assert "charStart" in params, "Missing parameter 'charStart'"
    assert "line" in params, "Missing parameter 'line'"
    assert "charEnd" in params, "Missing parameter 'charEnd'"

def test_simpleocl_locatedelement_has_column():
    assert hasattr(simpleocl_LocatedElement, "column")
    descriptor = None
    for klass in simpleocl_LocatedElement.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)

def test_simpleocl_locatedelement_has_charStart():
    assert hasattr(simpleocl_LocatedElement, "charStart")
    descriptor = None
    for klass in simpleocl_LocatedElement.__mro__:
        if "charStart" in klass.__dict__:
            descriptor = klass.__dict__["charStart"]
            break
    assert isinstance(descriptor, property)

def test_simpleocl_locatedelement_has_line():
    assert hasattr(simpleocl_LocatedElement, "line")
    descriptor = None
    for klass in simpleocl_LocatedElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_simpleocl_locatedelement_has_charEnd():
    assert hasattr(simpleocl_LocatedElement, "charEnd")
    descriptor = None
    for klass in simpleocl_LocatedElement.__mro__:
        if "charEnd" in klass.__dict__:
            descriptor = klass.__dict__["charEnd"]
            break
    assert isinstance(descriptor, property)



def test_simpleocl_import_is_not_abstract():
    assert not inspect.isabstract(simpleocl_Import)


def test_simpleocl_import_constructor_exists():
    assert callable(simpleocl_Import.__init__)


def test_simpleocl_import_constructor_args():
    sig = inspect.signature(simpleocl_Import.__init__)
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
OclModel_strategy = st.builds(
    OclModel,
)
simpleocl_OclInstanceModel_strategy = st.builds(
    simpleocl_OclInstanceModel,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
simpleocl_OclFeatureDefinition_strategy = st.builds(
    simpleocl_OclFeatureDefinition,
    static=
        safe_text
)
CollectionType_strategy = st.builds(
    CollectionType,
)
simpleocl_SetType_strategy = st.builds(
    simpleocl_SetType,
)
simpleocl_OrderedSetType_strategy = st.builds(
    simpleocl_OrderedSetType,
)
simpleocl_SequenceType_strategy = st.builds(
    simpleocl_SequenceType,
)
simpleocl_BagType_strategy = st.builds(
    simpleocl_BagType,
)
NumericType_strategy = st.builds(
    NumericType,
)
simpleocl_RealType_strategy = st.builds(
    simpleocl_RealType,
)
simpleocl_IntegerType_strategy = st.builds(
    simpleocl_IntegerType,
)
Primitive_strategy = st.builds(
    Primitive,
)
simpleocl_NumericType_strategy = st.builds(
    simpleocl_NumericType,
)
simpleocl_BooleanType_strategy = st.builds(
    simpleocl_BooleanType,
)
simpleocl_StringType_strategy = st.builds(
    simpleocl_StringType,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
simpleocl_Parameter_strategy = st.builds(
    simpleocl_Parameter,
)
OclType_strategy = st.builds(
    OclType,
)
simpleocl_TupleType_strategy = st.builds(
    simpleocl_TupleType,
)
simpleocl_MapType_strategy = st.builds(
    simpleocl_MapType,
)
simpleocl_EnvType_strategy = st.builds(
    simpleocl_EnvType,
)
simpleocl_Primitive_strategy = st.builds(
    simpleocl_Primitive,
)
simpleocl_OclModelElement_strategy = st.builds(
    simpleocl_OclModelElement,
)
simpleocl_OclAnyType_strategy = st.builds(
    simpleocl_OclAnyType,
)
simpleocl_LambdaType_strategy = st.builds(
    simpleocl_LambdaType,
)
simpleocl_CollectionType_strategy = st.builds(
    simpleocl_CollectionType,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
simpleocl_IteratorExp_strategy = st.builds(
    simpleocl_IteratorExp,
    name=
        safe_text
)
simpleocl_IterateExp_strategy = st.builds(
    simpleocl_IterateExp,
)
simpleocl_Iterator_strategy = st.builds(
    simpleocl_Iterator,
)
OperationCall_strategy = st.builds(
    OperationCall,
)
simpleocl_CollectionOperationCall_strategy = st.builds(
    simpleocl_CollectionOperationCall,
)
VariableExp_strategy = st.builds(
    VariableExp,
)
simpleocl_LambdaCallExp_strategy = st.builds(
    simpleocl_LambdaCallExp,
)
OperatorCallExp_strategy = st.builds(
    OperatorCallExp,
)
simpleocl_AddOpCallExp_strategy = st.builds(
    simpleocl_AddOpCallExp,
)
simpleocl_IntOpCallExp_strategy = st.builds(
    simpleocl_IntOpCallExp,
)
simpleocl_RelOpCallExp_strategy = st.builds(
    simpleocl_RelOpCallExp,
)
simpleocl_MulOpCallExp_strategy = st.builds(
    simpleocl_MulOpCallExp,
)
simpleocl_EqOpCallExp_strategy = st.builds(
    simpleocl_EqOpCallExp,
)
simpleocl_NotOpCallExp_strategy = st.builds(
    simpleocl_NotOpCallExp,
)
PropertyCall_strategy = st.builds(
    PropertyCall,
)
simpleocl_NavigationOrAttributeCall_strategy = st.builds(
    simpleocl_NavigationOrAttributeCall,
    name=
        safe_text
)
StaticPropertyCall_strategy = st.builds(
    StaticPropertyCall,
)
simpleocl_StaticOperationCall_strategy = st.builds(
    simpleocl_StaticOperationCall,
    operationName=
        safe_text
)
simpleocl_StaticNavigationOrAttributeCall_strategy = st.builds(
    simpleocl_StaticNavigationOrAttributeCall,
    name=
        safe_text
)
LocalVariable_strategy = st.builds(
    LocalVariable,
)
simpleocl_TuplePart_strategy = st.builds(
    simpleocl_TuplePart,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
simpleocl_SetExp_strategy = st.builds(
    simpleocl_SetExp,
)
simpleocl_OrderedSetExp_strategy = st.builds(
    simpleocl_OrderedSetExp,
)
simpleocl_SequenceExp_strategy = st.builds(
    simpleocl_SequenceExp,
)
simpleocl_BagExp_strategy = st.builds(
    simpleocl_BagExp,
)
CollectionPart_strategy = st.builds(
    CollectionPart,
)
simpleocl_CollectionItem_strategy = st.builds(
    simpleocl_CollectionItem,
)
simpleocl_CollectionRange_strategy = st.builds(
    simpleocl_CollectionRange,
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
simpleocl_BooleanExp_strategy = st.builds(
    simpleocl_BooleanExp,
    booleanSymbol=
        safe_text
)
simpleocl_StringExp_strategy = st.builds(
    simpleocl_StringExp,
    stringSymbol=
        safe_text
)
OclExpression_strategy = st.builds(
    OclExpression,
)
simpleocl_PrimitiveExp_strategy = st.builds(
    simpleocl_PrimitiveExp,
)
simpleocl_BraceExp_strategy = st.builds(
    simpleocl_BraceExp,
)
simpleocl_OclModelElementExp_strategy = st.builds(
    simpleocl_OclModelElementExp,
    name=
        safe_text
)
simpleocl_EnumLiteralExp_strategy = st.builds(
    simpleocl_EnumLiteralExp,
    name=
        safe_text
)
simpleocl_CollectionExp_strategy = st.builds(
    simpleocl_CollectionExp,
)
simpleocl_SuperExp_strategy = st.builds(
    simpleocl_SuperExp,
)
simpleocl_MapExp_strategy = st.builds(
    simpleocl_MapExp,
)
simpleocl_TupleExp_strategy = st.builds(
    simpleocl_TupleExp,
)
simpleocl_StaticPropertyCallExp_strategy = st.builds(
    simpleocl_StaticPropertyCallExp,
)
simpleocl_OclUndefinedExp_strategy = st.builds(
    simpleocl_OclUndefinedExp,
)
simpleocl_SelfExp_strategy = st.builds(
    simpleocl_SelfExp,
)
simpleocl_EnvExp_strategy = st.builds(
    simpleocl_EnvExp,
)
simpleocl_VariableExp_strategy = st.builds(
    simpleocl_VariableExp,
)
simpleocl_OperatorCallExp_strategy = st.builds(
    simpleocl_OperatorCallExp,
    operationName=
        safe_text
)
simpleocl_Attribute_strategy = st.builds(
    simpleocl_Attribute,
)
NumericExp_strategy = st.builds(
    NumericExp,
)
simpleocl_IntegerExp_strategy = st.builds(
    simpleocl_IntegerExp,
    integerSymbol=
        safe_text
)
simpleocl_RealExp_strategy = st.builds(
    simpleocl_RealExp,
    realSymbol=
        safe_text
)
simpleocl_NumericExp_strategy = st.builds(
    simpleocl_NumericExp,
)
simpleocl_Operation_strategy = st.builds(
    simpleocl_Operation,
)
simpleocl_LocalVariable_strategy = st.builds(
    simpleocl_LocalVariable,
    eq=
        safe_text
)
simpleocl_OperationCall_strategy = st.builds(
    simpleocl_OperationCall,
    operationName=
        safe_text
)
simpleocl_LoopExp_strategy = st.builds(
    simpleocl_LoopExp,
)
simpleocl_LetExp_strategy = st.builds(
    simpleocl_LetExp,
)
simpleocl_PropertyCallExp_strategy = st.builds(
    simpleocl_PropertyCallExp,
)
simpleocl_IfExp_strategy = st.builds(
    simpleocl_IfExp,
)
simpleocl_OclMetamodel_strategy = st.builds(
    simpleocl_OclMetamodel,
    uri=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
simpleocl_OclFeature_strategy = st.builds(
    simpleocl_OclFeature,
    eq=
        safe_text
)
simpleocl_OclModel_strategy = st.builds(
    simpleocl_OclModel,
)
simpleocl_Module_strategy = st.builds(
    simpleocl_Module,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
simpleocl_PropertyCall_strategy = st.builds(
    simpleocl_PropertyCall,
)
simpleocl_OclType_strategy = st.builds(
    simpleocl_OclType,
    name=
        safe_text
)
simpleocl_OclContextDefinition_strategy = st.builds(
    simpleocl_OclContextDefinition,
)
simpleocl_OclExpression_strategy = st.builds(
    simpleocl_OclExpression,
)
simpleocl_VariableDeclaration_strategy = st.builds(
    simpleocl_VariableDeclaration,
    varName=
        safe_text
)
simpleocl_TupleTypeAttribute_strategy = st.builds(
    simpleocl_TupleTypeAttribute,
    name=
        safe_text
)
simpleocl_MapElement_strategy = st.builds(
    simpleocl_MapElement,
)
simpleocl_StaticPropertyCall_strategy = st.builds(
    simpleocl_StaticPropertyCall,
)
simpleocl_ModuleElement_strategy = st.builds(
    simpleocl_ModuleElement,
)
simpleocl_CollectionPart_strategy = st.builds(
    simpleocl_CollectionPart,
)
simpleocl_NamedElement_strategy = st.builds(
    simpleocl_NamedElement,
    name=
        safe_text
)
simpleocl_LocatedElement_strategy = st.builds(
    simpleocl_LocatedElement,
    column=
        safe_text,
    charStart=
        safe_text,
    line=
        safe_text,
    charEnd=
        safe_text
)
simpleocl_Import_strategy = st.builds(
    simpleocl_Import,
)

@given(instance=OclModel_strategy)
@settings(max_examples=50)
def test_oclmodel_instantiation(instance):
    assert isinstance(instance, OclModel)

@given(instance=simpleocl_OclInstanceModel_strategy)
@settings(max_examples=50)
def test_simpleocl_oclinstancemodel_instantiation(instance):
    assert isinstance(instance, simpleocl_OclInstanceModel)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=simpleocl_OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_simpleocl_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, simpleocl_OclFeatureDefinition)



@given(instance=simpleocl_OclFeatureDefinition_strategy)
def test_simpleocl_oclfeaturedefinition_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=simpleocl_SetType_strategy)
@settings(max_examples=50)
def test_simpleocl_settype_instantiation(instance):
    assert isinstance(instance, simpleocl_SetType)

@given(instance=simpleocl_OrderedSetType_strategy)
@settings(max_examples=50)
def test_simpleocl_orderedsettype_instantiation(instance):
    assert isinstance(instance, simpleocl_OrderedSetType)

@given(instance=simpleocl_SequenceType_strategy)
@settings(max_examples=50)
def test_simpleocl_sequencetype_instantiation(instance):
    assert isinstance(instance, simpleocl_SequenceType)

@given(instance=simpleocl_BagType_strategy)
@settings(max_examples=50)
def test_simpleocl_bagtype_instantiation(instance):
    assert isinstance(instance, simpleocl_BagType)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=simpleocl_RealType_strategy)
@settings(max_examples=50)
def test_simpleocl_realtype_instantiation(instance):
    assert isinstance(instance, simpleocl_RealType)

@given(instance=simpleocl_IntegerType_strategy)
@settings(max_examples=50)
def test_simpleocl_integertype_instantiation(instance):
    assert isinstance(instance, simpleocl_IntegerType)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=simpleocl_NumericType_strategy)
@settings(max_examples=50)
def test_simpleocl_numerictype_instantiation(instance):
    assert isinstance(instance, simpleocl_NumericType)

@given(instance=simpleocl_BooleanType_strategy)
@settings(max_examples=50)
def test_simpleocl_booleantype_instantiation(instance):
    assert isinstance(instance, simpleocl_BooleanType)

@given(instance=simpleocl_StringType_strategy)
@settings(max_examples=50)
def test_simpleocl_stringtype_instantiation(instance):
    assert isinstance(instance, simpleocl_StringType)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=simpleocl_Parameter_strategy)
@settings(max_examples=50)
def test_simpleocl_parameter_instantiation(instance):
    assert isinstance(instance, simpleocl_Parameter)

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=simpleocl_TupleType_strategy)
@settings(max_examples=50)
def test_simpleocl_tupletype_instantiation(instance):
    assert isinstance(instance, simpleocl_TupleType)

@given(instance=simpleocl_MapType_strategy)
@settings(max_examples=50)
def test_simpleocl_maptype_instantiation(instance):
    assert isinstance(instance, simpleocl_MapType)

@given(instance=simpleocl_EnvType_strategy)
@settings(max_examples=50)
def test_simpleocl_envtype_instantiation(instance):
    assert isinstance(instance, simpleocl_EnvType)

@given(instance=simpleocl_Primitive_strategy)
@settings(max_examples=50)
def test_simpleocl_primitive_instantiation(instance):
    assert isinstance(instance, simpleocl_Primitive)

@given(instance=simpleocl_OclModelElement_strategy)
@settings(max_examples=50)
def test_simpleocl_oclmodelelement_instantiation(instance):
    assert isinstance(instance, simpleocl_OclModelElement)

@given(instance=simpleocl_OclAnyType_strategy)
@settings(max_examples=50)
def test_simpleocl_oclanytype_instantiation(instance):
    assert isinstance(instance, simpleocl_OclAnyType)

@given(instance=simpleocl_LambdaType_strategy)
@settings(max_examples=50)
def test_simpleocl_lambdatype_instantiation(instance):
    assert isinstance(instance, simpleocl_LambdaType)

@given(instance=simpleocl_CollectionType_strategy)
@settings(max_examples=50)
def test_simpleocl_collectiontype_instantiation(instance):
    assert isinstance(instance, simpleocl_CollectionType)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=simpleocl_IteratorExp_strategy)
@settings(max_examples=50)
def test_simpleocl_iteratorexp_instantiation(instance):
    assert isinstance(instance, simpleocl_IteratorExp)



@given(instance=simpleocl_IteratorExp_strategy)
def test_simpleocl_iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleocl_IterateExp_strategy)
@settings(max_examples=50)
def test_simpleocl_iterateexp_instantiation(instance):
    assert isinstance(instance, simpleocl_IterateExp)

@given(instance=simpleocl_Iterator_strategy)
@settings(max_examples=50)
def test_simpleocl_iterator_instantiation(instance):
    assert isinstance(instance, simpleocl_Iterator)

@given(instance=OperationCall_strategy)
@settings(max_examples=50)
def test_operationcall_instantiation(instance):
    assert isinstance(instance, OperationCall)

@given(instance=simpleocl_CollectionOperationCall_strategy)
@settings(max_examples=50)
def test_simpleocl_collectionoperationcall_instantiation(instance):
    assert isinstance(instance, simpleocl_CollectionOperationCall)

@given(instance=VariableExp_strategy)
@settings(max_examples=50)
def test_variableexp_instantiation(instance):
    assert isinstance(instance, VariableExp)

@given(instance=simpleocl_LambdaCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl_lambdacallexp_instantiation(instance):
    assert isinstance(instance, simpleocl_LambdaCallExp)

@given(instance=OperatorCallExp_strategy)
@settings(max_examples=50)
def test_operatorcallexp_instantiation(instance):
    assert isinstance(instance, OperatorCallExp)

@given(instance=simpleocl_AddOpCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl_addopcallexp_instantiation(instance):
    assert isinstance(instance, simpleocl_AddOpCallExp)

@given(instance=simpleocl_IntOpCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl_intopcallexp_instantiation(instance):
    assert isinstance(instance, simpleocl_IntOpCallExp)

@given(instance=simpleocl_RelOpCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl_relopcallexp_instantiation(instance):
    assert isinstance(instance, simpleocl_RelOpCallExp)

@given(instance=simpleocl_MulOpCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl_mulopcallexp_instantiation(instance):
    assert isinstance(instance, simpleocl_MulOpCallExp)

@given(instance=simpleocl_EqOpCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl_eqopcallexp_instantiation(instance):
    assert isinstance(instance, simpleocl_EqOpCallExp)

@given(instance=simpleocl_NotOpCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl_notopcallexp_instantiation(instance):
    assert isinstance(instance, simpleocl_NotOpCallExp)

@given(instance=PropertyCall_strategy)
@settings(max_examples=50)
def test_propertycall_instantiation(instance):
    assert isinstance(instance, PropertyCall)

@given(instance=simpleocl_NavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_simpleocl_navigationorattributecall_instantiation(instance):
    assert isinstance(instance, simpleocl_NavigationOrAttributeCall)



@given(instance=simpleocl_NavigationOrAttributeCall_strategy)
def test_simpleocl_navigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StaticPropertyCall_strategy)
@settings(max_examples=50)
def test_staticpropertycall_instantiation(instance):
    assert isinstance(instance, StaticPropertyCall)

@given(instance=simpleocl_StaticOperationCall_strategy)
@settings(max_examples=50)
def test_simpleocl_staticoperationcall_instantiation(instance):
    assert isinstance(instance, simpleocl_StaticOperationCall)



@given(instance=simpleocl_StaticOperationCall_strategy)
def test_simpleocl_staticoperationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=simpleocl_StaticNavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_simpleocl_staticnavigationorattributecall_instantiation(instance):
    assert isinstance(instance, simpleocl_StaticNavigationOrAttributeCall)



@given(instance=simpleocl_StaticNavigationOrAttributeCall_strategy)
def test_simpleocl_staticnavigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LocalVariable_strategy)
@settings(max_examples=50)
def test_localvariable_instantiation(instance):
    assert isinstance(instance, LocalVariable)

@given(instance=simpleocl_TuplePart_strategy)
@settings(max_examples=50)
def test_simpleocl_tuplepart_instantiation(instance):
    assert isinstance(instance, simpleocl_TuplePart)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=simpleocl_SetExp_strategy)
@settings(max_examples=50)
def test_simpleocl_setexp_instantiation(instance):
    assert isinstance(instance, simpleocl_SetExp)

@given(instance=simpleocl_OrderedSetExp_strategy)
@settings(max_examples=50)
def test_simpleocl_orderedsetexp_instantiation(instance):
    assert isinstance(instance, simpleocl_OrderedSetExp)

@given(instance=simpleocl_SequenceExp_strategy)
@settings(max_examples=50)
def test_simpleocl_sequenceexp_instantiation(instance):
    assert isinstance(instance, simpleocl_SequenceExp)

@given(instance=simpleocl_BagExp_strategy)
@settings(max_examples=50)
def test_simpleocl_bagexp_instantiation(instance):
    assert isinstance(instance, simpleocl_BagExp)

@given(instance=CollectionPart_strategy)
@settings(max_examples=50)
def test_collectionpart_instantiation(instance):
    assert isinstance(instance, CollectionPart)

@given(instance=simpleocl_CollectionItem_strategy)
@settings(max_examples=50)
def test_simpleocl_collectionitem_instantiation(instance):
    assert isinstance(instance, simpleocl_CollectionItem)

@given(instance=simpleocl_CollectionRange_strategy)
@settings(max_examples=50)
def test_simpleocl_collectionrange_instantiation(instance):
    assert isinstance(instance, simpleocl_CollectionRange)

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=simpleocl_BooleanExp_strategy)
@settings(max_examples=50)
def test_simpleocl_booleanexp_instantiation(instance):
    assert isinstance(instance, simpleocl_BooleanExp)



@given(instance=simpleocl_BooleanExp_strategy)
def test_simpleocl_booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=simpleocl_StringExp_strategy)
@settings(max_examples=50)
def test_simpleocl_stringexp_instantiation(instance):
    assert isinstance(instance, simpleocl_StringExp)



@given(instance=simpleocl_StringExp_strategy)
def test_simpleocl_stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=simpleocl_PrimitiveExp_strategy)
@settings(max_examples=50)
def test_simpleocl_primitiveexp_instantiation(instance):
    assert isinstance(instance, simpleocl_PrimitiveExp)

@given(instance=simpleocl_BraceExp_strategy)
@settings(max_examples=50)
def test_simpleocl_braceexp_instantiation(instance):
    assert isinstance(instance, simpleocl_BraceExp)

@given(instance=simpleocl_OclModelElementExp_strategy)
@settings(max_examples=50)
def test_simpleocl_oclmodelelementexp_instantiation(instance):
    assert isinstance(instance, simpleocl_OclModelElementExp)



@given(instance=simpleocl_OclModelElementExp_strategy)
def test_simpleocl_oclmodelelementexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleocl_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_simpleocl_enumliteralexp_instantiation(instance):
    assert isinstance(instance, simpleocl_EnumLiteralExp)



@given(instance=simpleocl_EnumLiteralExp_strategy)
def test_simpleocl_enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleocl_CollectionExp_strategy)
@settings(max_examples=50)
def test_simpleocl_collectionexp_instantiation(instance):
    assert isinstance(instance, simpleocl_CollectionExp)

@given(instance=simpleocl_SuperExp_strategy)
@settings(max_examples=50)
def test_simpleocl_superexp_instantiation(instance):
    assert isinstance(instance, simpleocl_SuperExp)

@given(instance=simpleocl_MapExp_strategy)
@settings(max_examples=50)
def test_simpleocl_mapexp_instantiation(instance):
    assert isinstance(instance, simpleocl_MapExp)

@given(instance=simpleocl_TupleExp_strategy)
@settings(max_examples=50)
def test_simpleocl_tupleexp_instantiation(instance):
    assert isinstance(instance, simpleocl_TupleExp)

@given(instance=simpleocl_StaticPropertyCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl_staticpropertycallexp_instantiation(instance):
    assert isinstance(instance, simpleocl_StaticPropertyCallExp)

@given(instance=simpleocl_OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_simpleocl_oclundefinedexp_instantiation(instance):
    assert isinstance(instance, simpleocl_OclUndefinedExp)

@given(instance=simpleocl_SelfExp_strategy)
@settings(max_examples=50)
def test_simpleocl_selfexp_instantiation(instance):
    assert isinstance(instance, simpleocl_SelfExp)

@given(instance=simpleocl_EnvExp_strategy)
@settings(max_examples=50)
def test_simpleocl_envexp_instantiation(instance):
    assert isinstance(instance, simpleocl_EnvExp)

@given(instance=simpleocl_VariableExp_strategy)
@settings(max_examples=50)
def test_simpleocl_variableexp_instantiation(instance):
    assert isinstance(instance, simpleocl_VariableExp)

@given(instance=simpleocl_OperatorCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl_operatorcallexp_instantiation(instance):
    assert isinstance(instance, simpleocl_OperatorCallExp)



@given(instance=simpleocl_OperatorCallExp_strategy)
def test_simpleocl_operatorcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=simpleocl_Attribute_strategy)
@settings(max_examples=50)
def test_simpleocl_attribute_instantiation(instance):
    assert isinstance(instance, simpleocl_Attribute)

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=simpleocl_IntegerExp_strategy)
@settings(max_examples=50)
def test_simpleocl_integerexp_instantiation(instance):
    assert isinstance(instance, simpleocl_IntegerExp)



@given(instance=simpleocl_IntegerExp_strategy)
def test_simpleocl_integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=simpleocl_RealExp_strategy)
@settings(max_examples=50)
def test_simpleocl_realexp_instantiation(instance):
    assert isinstance(instance, simpleocl_RealExp)



@given(instance=simpleocl_RealExp_strategy)
def test_simpleocl_realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=simpleocl_NumericExp_strategy)
@settings(max_examples=50)
def test_simpleocl_numericexp_instantiation(instance):
    assert isinstance(instance, simpleocl_NumericExp)

@given(instance=simpleocl_Operation_strategy)
@settings(max_examples=50)
def test_simpleocl_operation_instantiation(instance):
    assert isinstance(instance, simpleocl_Operation)

@given(instance=simpleocl_LocalVariable_strategy)
@settings(max_examples=50)
def test_simpleocl_localvariable_instantiation(instance):
    assert isinstance(instance, simpleocl_LocalVariable)



@given(instance=simpleocl_LocalVariable_strategy)
def test_simpleocl_localvariable_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=simpleocl_OperationCall_strategy)
@settings(max_examples=50)
def test_simpleocl_operationcall_instantiation(instance):
    assert isinstance(instance, simpleocl_OperationCall)



@given(instance=simpleocl_OperationCall_strategy)
def test_simpleocl_operationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=simpleocl_LoopExp_strategy)
@settings(max_examples=50)
def test_simpleocl_loopexp_instantiation(instance):
    assert isinstance(instance, simpleocl_LoopExp)

@given(instance=simpleocl_LetExp_strategy)
@settings(max_examples=50)
def test_simpleocl_letexp_instantiation(instance):
    assert isinstance(instance, simpleocl_LetExp)

@given(instance=simpleocl_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_simpleocl_propertycallexp_instantiation(instance):
    assert isinstance(instance, simpleocl_PropertyCallExp)

@given(instance=simpleocl_IfExp_strategy)
@settings(max_examples=50)
def test_simpleocl_ifexp_instantiation(instance):
    assert isinstance(instance, simpleocl_IfExp)

@given(instance=simpleocl_OclMetamodel_strategy)
@settings(max_examples=50)
def test_simpleocl_oclmetamodel_instantiation(instance):
    assert isinstance(instance, simpleocl_OclMetamodel)



@given(instance=simpleocl_OclMetamodel_strategy)
def test_simpleocl_oclmetamodel_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simpleocl_OclFeature_strategy)
@settings(max_examples=50)
def test_simpleocl_oclfeature_instantiation(instance):
    assert isinstance(instance, simpleocl_OclFeature)



@given(instance=simpleocl_OclFeature_strategy)
def test_simpleocl_oclfeature_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=simpleocl_OclModel_strategy)
@settings(max_examples=50)
def test_simpleocl_oclmodel_instantiation(instance):
    assert isinstance(instance, simpleocl_OclModel)

@given(instance=simpleocl_Module_strategy)
@settings(max_examples=50)
def test_simpleocl_module_instantiation(instance):
    assert isinstance(instance, simpleocl_Module)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=simpleocl_PropertyCall_strategy)
@settings(max_examples=50)
def test_simpleocl_propertycall_instantiation(instance):
    assert isinstance(instance, simpleocl_PropertyCall)

@given(instance=simpleocl_OclType_strategy)
@settings(max_examples=50)
def test_simpleocl_ocltype_instantiation(instance):
    assert isinstance(instance, simpleocl_OclType)



@given(instance=simpleocl_OclType_strategy)
def test_simpleocl_ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleocl_OclContextDefinition_strategy)
@settings(max_examples=50)
def test_simpleocl_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, simpleocl_OclContextDefinition)

@given(instance=simpleocl_OclExpression_strategy)
@settings(max_examples=50)
def test_simpleocl_oclexpression_instantiation(instance):
    assert isinstance(instance, simpleocl_OclExpression)

@given(instance=simpleocl_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_simpleocl_variabledeclaration_instantiation(instance):
    assert isinstance(instance, simpleocl_VariableDeclaration)



@given(instance=simpleocl_VariableDeclaration_strategy)
def test_simpleocl_variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=simpleocl_TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_simpleocl_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, simpleocl_TupleTypeAttribute)



@given(instance=simpleocl_TupleTypeAttribute_strategy)
def test_simpleocl_tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleocl_MapElement_strategy)
@settings(max_examples=50)
def test_simpleocl_mapelement_instantiation(instance):
    assert isinstance(instance, simpleocl_MapElement)

@given(instance=simpleocl_StaticPropertyCall_strategy)
@settings(max_examples=50)
def test_simpleocl_staticpropertycall_instantiation(instance):
    assert isinstance(instance, simpleocl_StaticPropertyCall)

@given(instance=simpleocl_ModuleElement_strategy)
@settings(max_examples=50)
def test_simpleocl_moduleelement_instantiation(instance):
    assert isinstance(instance, simpleocl_ModuleElement)

@given(instance=simpleocl_CollectionPart_strategy)
@settings(max_examples=50)
def test_simpleocl_collectionpart_instantiation(instance):
    assert isinstance(instance, simpleocl_CollectionPart)

@given(instance=simpleocl_NamedElement_strategy)
@settings(max_examples=50)
def test_simpleocl_namedelement_instantiation(instance):
    assert isinstance(instance, simpleocl_NamedElement)



@given(instance=simpleocl_NamedElement_strategy)
def test_simpleocl_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleocl_LocatedElement_strategy)
@settings(max_examples=50)
def test_simpleocl_locatedelement_instantiation(instance):
    assert isinstance(instance, simpleocl_LocatedElement)



@given(instance=simpleocl_LocatedElement_strategy)
def test_simpleocl_locatedelement_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original



@given(instance=simpleocl_LocatedElement_strategy)
def test_simpleocl_locatedelement_charStart_setter(instance):
    original = instance.charStart
    instance.charStart = original
    assert instance.charStart == original



@given(instance=simpleocl_LocatedElement_strategy)
def test_simpleocl_locatedelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original



@given(instance=simpleocl_LocatedElement_strategy)
def test_simpleocl_locatedelement_charEnd_setter(instance):
    original = instance.charEnd
    instance.charEnd = original
    assert instance.charEnd == original

@given(instance=simpleocl_Import_strategy)
@settings(max_examples=50)
def test_simpleocl_import_instantiation(instance):
    assert isinstance(instance, simpleocl_Import)
