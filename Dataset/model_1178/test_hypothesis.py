import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Parameter,
    OclInstanceModel,
    OclModelElement,
    OclFeatureDefinition,
    OclFeature,
    QualityMetamodel_QMM_OCL_Attribute,
    QualityMetamodel_QMM_OCL_Operation,
    NumericType,
    QualityMetamodel_QMM_OCL_RealType,
    QualityMetamodel_QMM_OCL_IntegerType,
    TupleType,
    OclContextDefinition,
    Primitive,
    QualityMetamodel_QMM_OCL_NumericType,
    QualityMetamodel_QMM_OCL_BooleanType,
    QualityMetamodel_QMM_OCL_StringType,
    OclModel,
    QualityMetamodel_QMM_OCL_OclInstanceModel,
    QualityMetamodel_QMM_OCL_OclMetamodel,
    LambdaType,
    TupleTypeAttribute,
    CollectionType,
    QualityMetamodel_QMM_OCL_SequenceType,
    QualityMetamodel_QMM_OCL_BagType,
    QualityMetamodel_QMM_OCL_OrderedSetType,
    QualityMetamodel_QMM_OCL_SetType,
    MapType,
    IterateExp,
    Iterator,
    VariableExp,
    QualityMetamodel_QMM_OCL_LambdaCallExp,
    MapExp,
    MapElement,
    PropertyCall,
    QualityMetamodel_QMM_OCL_OperationCall,
    QualityMetamodel_QMM_OCL_LoopExp,
    QualityMetamodel_QMM_OCL_NavigationOrAttributeCall,
    StaticPropertyCallExp,
    StaticPropertyCall,
    QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall,
    QualityMetamodel_QMM_OCL_StaticOperationCall,
    PrimitiveExp,
    QualityMetamodel_QMM_OCL_StringExp,
    TupleExp,
    TuplePart,
    CollectionExp,
    QualityMetamodel_QMM_OCL_SetExp,
    QualityMetamodel_QMM_OCL_OrderedSetExp,
    QualityMetamodel_QMM_OCL_SequenceExp,
    QualityMetamodel_QMM_OCL_BagExp,
    CollectionPart,
    QualityMetamodel_QMM_OCL_CollectionItem,
    QualityMetamodel_QMM_OCL_CollectionRange,
    NumericExp,
    QualityMetamodel_QMM_OCL_IntegerExp,
    QualityMetamodel_QMM_OCL_RealExp,
    ValueType,
    QualityMetamodel_TextValueType,
    OclExpression,
    QualityMetamodel_QMM_OCL_MapExp,
    QualityMetamodel_QMM_OCL_LetExp,
    QualityMetamodel_QMM_OCL_TupleExp,
    QualityMetamodel_QMM_OCL_EnumLiteralExp,
    QualityMetamodel_QMM_OCL_PrimitiveExp,
    QualityMetamodel_QMM_OCL_OclUndefinedExp,
    QualityMetamodel_QMM_OCL_SuperExp,
    QualityMetamodel_QMM_OCL_OperatorCallExp,
    QualityMetamodel_QMM_OCL_SelfExp,
    QualityMetamodel_QMM_OCL_IfExp,
    QualityMetamodel_QMM_OCL_BraceExp,
    QualityMetamodel_QMM_OCL_CollectionExp,
    QualityMetamodel_QMM_OCL_StaticPropertyCallExp,
    QualityMetamodel_QMM_OCL_OclModelElementExp,
    QualityMetamodel_QMM_OCL_PropertyCallExp,
    QualityMetamodel_QMM_OCL_EnvExp,
    QualityMetamodel_Operation,
    Value,
    QualityMetamodel_AggregatedValue,
    QualityMetamodel_SingleValue,
    QualityMetamodel_MetricProvider,
    Module,
    QualityMetamodel_QualityModel,
    QualityMetamodel_QMM_OCL_NumericExp,
    QualityMetamodel_QMM_OCL_BooleanExp,
    IfExp,
    OclType,
    QualityMetamodel_QMM_OCL_MapType,
    QualityMetamodel_QMM_OCL_LambdaType,
    QualityMetamodel_QMM_OCL_CollectionType,
    QualityMetamodel_QMM_OCL_EnvType,
    QualityMetamodel_QMM_OCL_OclModelElement,
    QualityMetamodel_QMM_OCL_OclAnyType,
    QualityMetamodel_QMM_OCL_TupleType,
    QualityMetamodel_QMM_OCL_Primitive,
    QualityMetamodel_QMM_OCL_VariableExp,
    OperatorCallExp,
    QualityMetamodel_QMM_OCL_AddOpCallExp,
    QualityMetamodel_QMM_OCL_IntOpCallExp,
    QualityMetamodel_QMM_OCL_NotOpCallExp,
    QualityMetamodel_QMM_OCL_EqOpCallExp,
    QualityMetamodel_QMM_OCL_MulOpCallExp,
    QualityMetamodel_QMM_OCL_RelOpCallExp,
    Attribute,
    Operation,
    LocalVariable,
    QualityMetamodel_QMM_OCL_TuplePart,
    OperationCall,
    QualityMetamodel_QMM_OCL_CollectionOperationCall,
    LoopExp,
    QualityMetamodel_QMM_OCL_IterateExp,
    QualityMetamodel_QMM_OCL_IteratorExp,
    LetExp,
    PropertyCallExp,
    QualityMetamodel_EnumerationItem,
    QualityMetamodel_EnumerationMetric,
    ModuleElement,
    QualityMetamodel_QMM_OCL_OclFeatureDefinition,
    Import,
    OclMetamodel,
    NamedElement,
    QualityMetamodel_QMM_OCL_OclModel,
    QualityMetamodel_QMM_OCL_OclFeature,
    QualityMetamodel_QMM_OCL_Import,
    QualityMetamodel_QMM_OCL_Module,
    LocatedElement,
    QualityMetamodel_QMM_OCL_CollectionPart,
    QualityMetamodel_QMM_OCL_PropertyCall,
    QualityMetamodel_QMM_OCL_OclContextDefinition,
    QualityMetamodel_QMM_OCL_VariableDeclaration,
    QualityMetamodel_QMM_OCL_StaticPropertyCall,
    QualityMetamodel_QMM_OCL_MapElement,
    QualityMetamodel_QMM_OCL_ModuleElement,
    QualityMetamodel_QMM_OCL_OclType,
    QualityMetamodel_QMM_OCL_TupleTypeAttribute,
    QualityMetamodel_QMM_OCL_OclExpression,
    QualityMetamodel_QMM_OCL_NamedElement,
    QualityMetamodel_QMM_OCL_LocatedElement,
    QualityMetamodel_IntegerValueType,
    QualityMetamodel_BooleanValueType,
    QualityMetamodel_RealValueType,
    VariableDeclaration,
    QualityMetamodel_QMM_OCL_Iterator,
    QualityMetamodel_QualityAttribute,
    QualityMetamodel_ValueType,
    QualityMetamodel_QMM_OCL_Parameter,
    QualityMetamodel_QMM_OCL_LocalVariable,
    QualityMetamodel_Value,
    QualityMetamodel_AggregatedValueMetric,
    QualityMetamodel_RangeValueType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_oclinstancemodel_is_not_abstract():
    assert not inspect.isabstract(OclInstanceModel)


def test_oclinstancemodel_constructor_exists():
    assert callable(OclInstanceModel.__init__)


def test_oclinstancemodel_constructor_args():
    sig = inspect.signature(OclInstanceModel.__init__)
    params = list(sig.parameters.keys())



def test_oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(OclModelElement)


def test_oclmodelelement_constructor_exists():
    assert callable(OclModelElement.__init__)


def test_oclmodelelement_constructor_args():
    sig = inspect.signature(OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(OclFeatureDefinition)


def test_oclfeaturedefinition_constructor_exists():
    assert callable(OclFeatureDefinition.__init__)


def test_oclfeaturedefinition_constructor_args():
    sig = inspect.signature(OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_attribute_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_Attribute)


def test_qualitymetamodel_qmm_ocl_attribute_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_Attribute.__init__)


def test_qualitymetamodel_qmm_ocl_attribute_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_operation_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_Operation)


def test_qualitymetamodel_qmm_ocl_operation_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_Operation.__init__)


def test_qualitymetamodel_qmm_ocl_operation_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_Operation.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_realtype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_RealType)


def test_qualitymetamodel_qmm_ocl_realtype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_RealType.__init__)


def test_qualitymetamodel_qmm_ocl_realtype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_RealType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_integertype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_IntegerType)


def test_qualitymetamodel_qmm_ocl_integertype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_IntegerType.__init__)


def test_qualitymetamodel_qmm_ocl_integertype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_tupletype_is_not_abstract():
    assert not inspect.isabstract(TupleType)


def test_tupletype_constructor_exists():
    assert callable(TupleType.__init__)


def test_tupletype_constructor_args():
    sig = inspect.signature(TupleType.__init__)
    params = list(sig.parameters.keys())



def test_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OclContextDefinition)


def test_oclcontextdefinition_constructor_exists():
    assert callable(OclContextDefinition.__init__)


def test_oclcontextdefinition_constructor_args():
    sig = inspect.signature(OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_numerictype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_NumericType)


def test_qualitymetamodel_qmm_ocl_numerictype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_NumericType.__init__)


def test_qualitymetamodel_qmm_ocl_numerictype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_NumericType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_booleantype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_BooleanType)


def test_qualitymetamodel_qmm_ocl_booleantype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_BooleanType.__init__)


def test_qualitymetamodel_qmm_ocl_booleantype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_stringtype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_StringType)


def test_qualitymetamodel_qmm_ocl_stringtype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_StringType.__init__)


def test_qualitymetamodel_qmm_ocl_stringtype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_StringType.__init__)
    params = list(sig.parameters.keys())



def test_oclmodel_is_not_abstract():
    assert not inspect.isabstract(OclModel)


def test_oclmodel_constructor_exists():
    assert callable(OclModel.__init__)


def test_oclmodel_constructor_args():
    sig = inspect.signature(OclModel.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_oclinstancemodel_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OclInstanceModel)


def test_qualitymetamodel_qmm_ocl_oclinstancemodel_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OclInstanceModel.__init__)


def test_qualitymetamodel_qmm_ocl_oclinstancemodel_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OclInstanceModel.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_oclmetamodel_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OclMetamodel)


def test_qualitymetamodel_qmm_ocl_oclmetamodel_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OclMetamodel.__init__)


def test_qualitymetamodel_qmm_ocl_oclmetamodel_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OclMetamodel.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_qualitymetamodel_qmm_ocl_oclmetamodel_has_uri():
    assert hasattr(QualityMetamodel_QMM_OCL_OclMetamodel, "uri")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_OclMetamodel.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_lambdatype_is_not_abstract():
    assert not inspect.isabstract(LambdaType)


def test_lambdatype_constructor_exists():
    assert callable(LambdaType.__init__)


def test_lambdatype_constructor_args():
    sig = inspect.signature(LambdaType.__init__)
    params = list(sig.parameters.keys())



def test_tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(TupleTypeAttribute)


def test_tupletypeattribute_constructor_exists():
    assert callable(TupleTypeAttribute.__init__)


def test_tupletypeattribute_constructor_args():
    sig = inspect.signature(TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_sequencetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_SequenceType)


def test_qualitymetamodel_qmm_ocl_sequencetype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_SequenceType.__init__)


def test_qualitymetamodel_qmm_ocl_sequencetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_bagtype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_BagType)


def test_qualitymetamodel_qmm_ocl_bagtype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_BagType.__init__)


def test_qualitymetamodel_qmm_ocl_bagtype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_BagType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OrderedSetType)


def test_qualitymetamodel_qmm_ocl_orderedsettype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OrderedSetType.__init__)


def test_qualitymetamodel_qmm_ocl_orderedsettype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_settype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_SetType)


def test_qualitymetamodel_qmm_ocl_settype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_SetType.__init__)


def test_qualitymetamodel_qmm_ocl_settype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_SetType.__init__)
    params = list(sig.parameters.keys())



def test_maptype_is_not_abstract():
    assert not inspect.isabstract(MapType)


def test_maptype_constructor_exists():
    assert callable(MapType.__init__)


def test_maptype_constructor_args():
    sig = inspect.signature(MapType.__init__)
    params = list(sig.parameters.keys())



def test_iterateexp_is_not_abstract():
    assert not inspect.isabstract(IterateExp)


def test_iterateexp_constructor_exists():
    assert callable(IterateExp.__init__)


def test_iterateexp_constructor_args():
    sig = inspect.signature(IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_iterator_is_not_abstract():
    assert not inspect.isabstract(Iterator)


def test_iterator_constructor_exists():
    assert callable(Iterator.__init__)


def test_iterator_constructor_args():
    sig = inspect.signature(Iterator.__init__)
    params = list(sig.parameters.keys())



def test_variableexp_is_not_abstract():
    assert not inspect.isabstract(VariableExp)


def test_variableexp_constructor_exists():
    assert callable(VariableExp.__init__)


def test_variableexp_constructor_args():
    sig = inspect.signature(VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_lambdacallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_LambdaCallExp)


def test_qualitymetamodel_qmm_ocl_lambdacallexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_LambdaCallExp.__init__)


def test_qualitymetamodel_qmm_ocl_lambdacallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_LambdaCallExp.__init__)
    params = list(sig.parameters.keys())



def test_mapexp_is_not_abstract():
    assert not inspect.isabstract(MapExp)


def test_mapexp_constructor_exists():
    assert callable(MapExp.__init__)


def test_mapexp_constructor_args():
    sig = inspect.signature(MapExp.__init__)
    params = list(sig.parameters.keys())



def test_mapelement_is_not_abstract():
    assert not inspect.isabstract(MapElement)


def test_mapelement_constructor_exists():
    assert callable(MapElement.__init__)


def test_mapelement_constructor_args():
    sig = inspect.signature(MapElement.__init__)
    params = list(sig.parameters.keys())



def test_propertycall_is_not_abstract():
    assert not inspect.isabstract(PropertyCall)


def test_propertycall_constructor_exists():
    assert callable(PropertyCall.__init__)


def test_propertycall_constructor_args():
    sig = inspect.signature(PropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_operationcall_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OperationCall)


def test_qualitymetamodel_qmm_ocl_operationcall_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OperationCall.__init__)


def test_qualitymetamodel_qmm_ocl_operationcall_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_qualitymetamodel_qmm_ocl_operationcall_has_operationName():
    assert hasattr(QualityMetamodel_QMM_OCL_OperationCall, "operationName")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_OperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_qmm_ocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_LoopExp)


def test_qualitymetamodel_qmm_ocl_loopexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_LoopExp.__init__)


def test_qualitymetamodel_qmm_ocl_loopexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_navigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_NavigationOrAttributeCall)


def test_qualitymetamodel_qmm_ocl_navigationorattributecall_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_NavigationOrAttributeCall.__init__)


def test_qualitymetamodel_qmm_ocl_navigationorattributecall_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_NavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel_qmm_ocl_navigationorattributecall_has_name():
    assert hasattr(QualityMetamodel_QMM_OCL_NavigationOrAttributeCall, "name")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_NavigationOrAttributeCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_staticpropertycallexp_is_not_abstract():
    assert not inspect.isabstract(StaticPropertyCallExp)


def test_staticpropertycallexp_constructor_exists():
    assert callable(StaticPropertyCallExp.__init__)


def test_staticpropertycallexp_constructor_args():
    sig = inspect.signature(StaticPropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_staticpropertycall_is_not_abstract():
    assert not inspect.isabstract(StaticPropertyCall)


def test_staticpropertycall_constructor_exists():
    assert callable(StaticPropertyCall.__init__)


def test_staticpropertycall_constructor_args():
    sig = inspect.signature(StaticPropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_staticnavigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall)


def test_qualitymetamodel_qmm_ocl_staticnavigationorattributecall_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall.__init__)


def test_qualitymetamodel_qmm_ocl_staticnavigationorattributecall_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel_qmm_ocl_staticnavigationorattributecall_has_name():
    assert hasattr(QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall, "name")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_qmm_ocl_staticoperationcall_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_StaticOperationCall)


def test_qualitymetamodel_qmm_ocl_staticoperationcall_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_StaticOperationCall.__init__)


def test_qualitymetamodel_qmm_ocl_staticoperationcall_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_StaticOperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_qualitymetamodel_qmm_ocl_staticoperationcall_has_operationName():
    assert hasattr(QualityMetamodel_QMM_OCL_StaticOperationCall, "operationName")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_StaticOperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_stringexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_StringExp)


def test_qualitymetamodel_qmm_ocl_stringexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_StringExp.__init__)


def test_qualitymetamodel_qmm_ocl_stringexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_qualitymetamodel_qmm_ocl_stringexp_has_stringSymbol():
    assert hasattr(QualityMetamodel_QMM_OCL_StringExp, "stringSymbol")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_StringExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_tupleexp_is_not_abstract():
    assert not inspect.isabstract(TupleExp)


def test_tupleexp_constructor_exists():
    assert callable(TupleExp.__init__)


def test_tupleexp_constructor_args():
    sig = inspect.signature(TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_tuplepart_is_not_abstract():
    assert not inspect.isabstract(TuplePart)


def test_tuplepart_constructor_exists():
    assert callable(TuplePart.__init__)


def test_tuplepart_constructor_args():
    sig = inspect.signature(TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_setexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_SetExp)


def test_qualitymetamodel_qmm_ocl_setexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_SetExp.__init__)


def test_qualitymetamodel_qmm_ocl_setexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_SetExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OrderedSetExp)


def test_qualitymetamodel_qmm_ocl_orderedsetexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OrderedSetExp.__init__)


def test_qualitymetamodel_qmm_ocl_orderedsetexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_sequenceexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_SequenceExp)


def test_qualitymetamodel_qmm_ocl_sequenceexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_SequenceExp.__init__)


def test_qualitymetamodel_qmm_ocl_sequenceexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_bagexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_BagExp)


def test_qualitymetamodel_qmm_ocl_bagexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_BagExp.__init__)


def test_qualitymetamodel_qmm_ocl_bagexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_BagExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionpart_is_not_abstract():
    assert not inspect.isabstract(CollectionPart)


def test_collectionpart_constructor_exists():
    assert callable(CollectionPart.__init__)


def test_collectionpart_constructor_args():
    sig = inspect.signature(CollectionPart.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_collectionitem_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_CollectionItem)


def test_qualitymetamodel_qmm_ocl_collectionitem_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_CollectionItem.__init__)


def test_qualitymetamodel_qmm_ocl_collectionitem_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_collectionrange_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_CollectionRange)


def test_qualitymetamodel_qmm_ocl_collectionrange_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_CollectionRange.__init__)


def test_qualitymetamodel_qmm_ocl_collectionrange_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_integerexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_IntegerExp)


def test_qualitymetamodel_qmm_ocl_integerexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_IntegerExp.__init__)


def test_qualitymetamodel_qmm_ocl_integerexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_qualitymetamodel_qmm_ocl_integerexp_has_integerSymbol():
    assert hasattr(QualityMetamodel_QMM_OCL_IntegerExp, "integerSymbol")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_qmm_ocl_realexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_RealExp)


def test_qualitymetamodel_qmm_ocl_realexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_RealExp.__init__)


def test_qualitymetamodel_qmm_ocl_realexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_qualitymetamodel_qmm_ocl_realexp_has_realSymbol():
    assert hasattr(QualityMetamodel_QMM_OCL_RealExp, "realSymbol")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_RealExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_valuetype_is_not_abstract():
    assert not inspect.isabstract(ValueType)


def test_valuetype_constructor_exists():
    assert callable(ValueType.__init__)


def test_valuetype_constructor_args():
    sig = inspect.signature(ValueType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_textvaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_TextValueType)


def test_qualitymetamodel_textvaluetype_constructor_exists():
    assert callable(QualityMetamodel_TextValueType.__init__)


def test_qualitymetamodel_textvaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_TextValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel_textvaluetype_has_value():
    assert hasattr(QualityMetamodel_TextValueType, "value")
    descriptor = None
    for klass in QualityMetamodel_TextValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_mapexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_MapExp)


def test_qualitymetamodel_qmm_ocl_mapexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_MapExp.__init__)


def test_qualitymetamodel_qmm_ocl_mapexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_MapExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_letexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_LetExp)


def test_qualitymetamodel_qmm_ocl_letexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_LetExp.__init__)


def test_qualitymetamodel_qmm_ocl_letexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_tupleexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_TupleExp)


def test_qualitymetamodel_qmm_ocl_tupleexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_TupleExp.__init__)


def test_qualitymetamodel_qmm_ocl_tupleexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_EnumLiteralExp)


def test_qualitymetamodel_qmm_ocl_enumliteralexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_EnumLiteralExp.__init__)


def test_qualitymetamodel_qmm_ocl_enumliteralexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel_qmm_ocl_enumliteralexp_has_name():
    assert hasattr(QualityMetamodel_QMM_OCL_EnumLiteralExp, "name")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_qmm_ocl_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_PrimitiveExp)


def test_qualitymetamodel_qmm_ocl_primitiveexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_PrimitiveExp.__init__)


def test_qualitymetamodel_qmm_ocl_primitiveexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OclUndefinedExp)


def test_qualitymetamodel_qmm_ocl_oclundefinedexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OclUndefinedExp.__init__)


def test_qualitymetamodel_qmm_ocl_oclundefinedexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_superexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_SuperExp)


def test_qualitymetamodel_qmm_ocl_superexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_SuperExp.__init__)


def test_qualitymetamodel_qmm_ocl_superexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OperatorCallExp)


def test_qualitymetamodel_qmm_ocl_operatorcallexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OperatorCallExp.__init__)


def test_qualitymetamodel_qmm_ocl_operatorcallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OperatorCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_qualitymetamodel_qmm_ocl_operatorcallexp_has_operationName():
    assert hasattr(QualityMetamodel_QMM_OCL_OperatorCallExp, "operationName")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_OperatorCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_qmm_ocl_selfexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_SelfExp)


def test_qualitymetamodel_qmm_ocl_selfexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_SelfExp.__init__)


def test_qualitymetamodel_qmm_ocl_selfexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_ifexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_IfExp)


def test_qualitymetamodel_qmm_ocl_ifexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_IfExp.__init__)


def test_qualitymetamodel_qmm_ocl_ifexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_braceexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_BraceExp)


def test_qualitymetamodel_qmm_ocl_braceexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_BraceExp.__init__)


def test_qualitymetamodel_qmm_ocl_braceexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_BraceExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_collectionexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_CollectionExp)


def test_qualitymetamodel_qmm_ocl_collectionexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_CollectionExp.__init__)


def test_qualitymetamodel_qmm_ocl_collectionexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_staticpropertycallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_StaticPropertyCallExp)


def test_qualitymetamodel_qmm_ocl_staticpropertycallexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_StaticPropertyCallExp.__init__)


def test_qualitymetamodel_qmm_ocl_staticpropertycallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_StaticPropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_oclmodelelementexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OclModelElementExp)


def test_qualitymetamodel_qmm_ocl_oclmodelelementexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OclModelElementExp.__init__)


def test_qualitymetamodel_qmm_ocl_oclmodelelementexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OclModelElementExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel_qmm_ocl_oclmodelelementexp_has_name():
    assert hasattr(QualityMetamodel_QMM_OCL_OclModelElementExp, "name")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_OclModelElementExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_qmm_ocl_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_PropertyCallExp)


def test_qualitymetamodel_qmm_ocl_propertycallexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_PropertyCallExp.__init__)


def test_qualitymetamodel_qmm_ocl_propertycallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_envexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_EnvExp)


def test_qualitymetamodel_qmm_ocl_envexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_EnvExp.__init__)


def test_qualitymetamodel_qmm_ocl_envexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_EnvExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_operation_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_Operation)


def test_qualitymetamodel_operation_constructor_exists():
    assert callable(QualityMetamodel_Operation.__init__)


def test_qualitymetamodel_operation_constructor_args():
    sig = inspect.signature(QualityMetamodel_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "body" in params, "Missing parameter 'body'"

def test_qualitymetamodel_operation_has_name():
    assert hasattr(QualityMetamodel_Operation, "name")
    descriptor = None
    for klass in QualityMetamodel_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_operation_has_body():
    assert hasattr(QualityMetamodel_Operation, "body")
    descriptor = None
    for klass in QualityMetamodel_Operation.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_aggregatedvalue_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_AggregatedValue)


def test_qualitymetamodel_aggregatedvalue_constructor_exists():
    assert callable(QualityMetamodel_AggregatedValue.__init__)


def test_qualitymetamodel_aggregatedvalue_constructor_args():
    sig = inspect.signature(QualityMetamodel_AggregatedValue.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_singlevalue_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_SingleValue)


def test_qualitymetamodel_singlevalue_constructor_exists():
    assert callable(QualityMetamodel_SingleValue.__init__)


def test_qualitymetamodel_singlevalue_constructor_args():
    sig = inspect.signature(QualityMetamodel_SingleValue.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_metricprovider_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_MetricProvider)


def test_qualitymetamodel_metricprovider_constructor_exists():
    assert callable(QualityMetamodel_MetricProvider.__init__)


def test_qualitymetamodel_metricprovider_constructor_args():
    sig = inspect.signature(QualityMetamodel_MetricProvider.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_qualitymetamodel_metricprovider_has_id():
    assert hasattr(QualityMetamodel_MetricProvider, "id")
    descriptor = None
    for klass in QualityMetamodel_MetricProvider.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_metricprovider_has_name():
    assert hasattr(QualityMetamodel_MetricProvider, "name")
    descriptor = None
    for klass in QualityMetamodel_MetricProvider.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_metricprovider_has_description():
    assert hasattr(QualityMetamodel_MetricProvider, "description")
    descriptor = None
    for klass in QualityMetamodel_MetricProvider.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qualitymodel_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QualityModel)


def test_qualitymetamodel_qualitymodel_constructor_exists():
    assert callable(QualityMetamodel_QualityModel.__init__)


def test_qualitymetamodel_qualitymodel_constructor_args():
    sig = inspect.signature(QualityMetamodel_QualityModel.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_numericexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_NumericExp)


def test_qualitymetamodel_qmm_ocl_numericexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_NumericExp.__init__)


def test_qualitymetamodel_qmm_ocl_numericexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_booleanexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_BooleanExp)


def test_qualitymetamodel_qmm_ocl_booleanexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_BooleanExp.__init__)


def test_qualitymetamodel_qmm_ocl_booleanexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_qualitymetamodel_qmm_ocl_booleanexp_has_booleanSymbol():
    assert hasattr(QualityMetamodel_QMM_OCL_BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ifexp_is_not_abstract():
    assert not inspect.isabstract(IfExp)


def test_ifexp_constructor_exists():
    assert callable(IfExp.__init__)


def test_ifexp_constructor_args():
    sig = inspect.signature(IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocltype_is_not_abstract():
    assert not inspect.isabstract(OclType)


def test_ocltype_constructor_exists():
    assert callable(OclType.__init__)


def test_ocltype_constructor_args():
    sig = inspect.signature(OclType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_maptype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_MapType)


def test_qualitymetamodel_qmm_ocl_maptype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_MapType.__init__)


def test_qualitymetamodel_qmm_ocl_maptype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_MapType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_lambdatype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_LambdaType)


def test_qualitymetamodel_qmm_ocl_lambdatype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_LambdaType.__init__)


def test_qualitymetamodel_qmm_ocl_lambdatype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_LambdaType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_collectiontype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_CollectionType)


def test_qualitymetamodel_qmm_ocl_collectiontype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_CollectionType.__init__)


def test_qualitymetamodel_qmm_ocl_collectiontype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_envtype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_EnvType)


def test_qualitymetamodel_qmm_ocl_envtype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_EnvType.__init__)


def test_qualitymetamodel_qmm_ocl_envtype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_EnvType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OclModelElement)


def test_qualitymetamodel_qmm_ocl_oclmodelelement_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OclModelElement.__init__)


def test_qualitymetamodel_qmm_ocl_oclmodelelement_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_oclanytype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OclAnyType)


def test_qualitymetamodel_qmm_ocl_oclanytype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OclAnyType.__init__)


def test_qualitymetamodel_qmm_ocl_oclanytype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_tupletype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_TupleType)


def test_qualitymetamodel_qmm_ocl_tupletype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_TupleType.__init__)


def test_qualitymetamodel_qmm_ocl_tupletype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_primitive_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_Primitive)


def test_qualitymetamodel_qmm_ocl_primitive_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_Primitive.__init__)


def test_qualitymetamodel_qmm_ocl_primitive_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_Primitive.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_variableexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_VariableExp)


def test_qualitymetamodel_qmm_ocl_variableexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_VariableExp.__init__)


def test_qualitymetamodel_qmm_ocl_variableexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OperatorCallExp)


def test_operatorcallexp_constructor_exists():
    assert callable(OperatorCallExp.__init__)


def test_operatorcallexp_constructor_args():
    sig = inspect.signature(OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_addopcallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_AddOpCallExp)


def test_qualitymetamodel_qmm_ocl_addopcallexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_AddOpCallExp.__init__)


def test_qualitymetamodel_qmm_ocl_addopcallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_AddOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_intopcallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_IntOpCallExp)


def test_qualitymetamodel_qmm_ocl_intopcallexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_IntOpCallExp.__init__)


def test_qualitymetamodel_qmm_ocl_intopcallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_IntOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_notopcallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_NotOpCallExp)


def test_qualitymetamodel_qmm_ocl_notopcallexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_NotOpCallExp.__init__)


def test_qualitymetamodel_qmm_ocl_notopcallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_NotOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_eqopcallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_EqOpCallExp)


def test_qualitymetamodel_qmm_ocl_eqopcallexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_EqOpCallExp.__init__)


def test_qualitymetamodel_qmm_ocl_eqopcallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_EqOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_mulopcallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_MulOpCallExp)


def test_qualitymetamodel_qmm_ocl_mulopcallexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_MulOpCallExp.__init__)


def test_qualitymetamodel_qmm_ocl_mulopcallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_MulOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_relopcallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_RelOpCallExp)


def test_qualitymetamodel_qmm_ocl_relopcallexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_RelOpCallExp.__init__)


def test_qualitymetamodel_qmm_ocl_relopcallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_RelOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_localvariable_is_not_abstract():
    assert not inspect.isabstract(LocalVariable)


def test_localvariable_constructor_exists():
    assert callable(LocalVariable.__init__)


def test_localvariable_constructor_args():
    sig = inspect.signature(LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_tuplepart_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_TuplePart)


def test_qualitymetamodel_qmm_ocl_tuplepart_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_TuplePart.__init__)


def test_qualitymetamodel_qmm_ocl_tuplepart_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_operationcall_is_not_abstract():
    assert not inspect.isabstract(OperationCall)


def test_operationcall_constructor_exists():
    assert callable(OperationCall.__init__)


def test_operationcall_constructor_args():
    sig = inspect.signature(OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_collectionoperationcall_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_CollectionOperationCall)


def test_qualitymetamodel_qmm_ocl_collectionoperationcall_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_CollectionOperationCall.__init__)


def test_qualitymetamodel_qmm_ocl_collectionoperationcall_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_CollectionOperationCall.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_iterateexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_IterateExp)


def test_qualitymetamodel_qmm_ocl_iterateexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_IterateExp.__init__)


def test_qualitymetamodel_qmm_ocl_iterateexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_IteratorExp)


def test_qualitymetamodel_qmm_ocl_iteratorexp_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_IteratorExp.__init__)


def test_qualitymetamodel_qmm_ocl_iteratorexp_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel_qmm_ocl_iteratorexp_has_name():
    assert hasattr(QualityMetamodel_QMM_OCL_IteratorExp, "name")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_letexp_is_not_abstract():
    assert not inspect.isabstract(LetExp)


def test_letexp_constructor_exists():
    assert callable(LetExp.__init__)


def test_letexp_constructor_args():
    sig = inspect.signature(LetExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_enumerationitem_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_EnumerationItem)


def test_qualitymetamodel_enumerationitem_constructor_exists():
    assert callable(QualityMetamodel_EnumerationItem.__init__)


def test_qualitymetamodel_enumerationitem_constructor_args():
    sig = inspect.signature(QualityMetamodel_EnumerationItem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel_enumerationitem_has_name():
    assert hasattr(QualityMetamodel_EnumerationItem, "name")
    descriptor = None
    for klass in QualityMetamodel_EnumerationItem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_enumerationmetric_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_EnumerationMetric)


def test_qualitymetamodel_enumerationmetric_constructor_exists():
    assert callable(QualityMetamodel_EnumerationMetric.__init__)


def test_qualitymetamodel_enumerationmetric_constructor_args():
    sig = inspect.signature(QualityMetamodel_EnumerationMetric.__init__)
    params = list(sig.parameters.keys())



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OclFeatureDefinition)


def test_qualitymetamodel_qmm_ocl_oclfeaturedefinition_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OclFeatureDefinition.__init__)


def test_qualitymetamodel_qmm_ocl_oclfeaturedefinition_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_qualitymetamodel_qmm_ocl_oclfeaturedefinition_has_static():
    assert hasattr(QualityMetamodel_QMM_OCL_OclFeatureDefinition, "static")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_OclFeatureDefinition.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_import_is_not_abstract():
    assert not inspect.isabstract(Import)


def test_import_constructor_exists():
    assert callable(Import.__init__)


def test_import_constructor_args():
    sig = inspect.signature(Import.__init__)
    params = list(sig.parameters.keys())



def test_oclmetamodel_is_not_abstract():
    assert not inspect.isabstract(OclMetamodel)


def test_oclmetamodel_constructor_exists():
    assert callable(OclMetamodel.__init__)


def test_oclmetamodel_constructor_args():
    sig = inspect.signature(OclMetamodel.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_oclmodel_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OclModel)


def test_qualitymetamodel_qmm_ocl_oclmodel_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OclModel.__init__)


def test_qualitymetamodel_qmm_ocl_oclmodel_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OclModel.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_oclfeature_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OclFeature)


def test_qualitymetamodel_qmm_ocl_oclfeature_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OclFeature.__init__)


def test_qualitymetamodel_qmm_ocl_oclfeature_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OclFeature.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_qualitymetamodel_qmm_ocl_oclfeature_has_eq():
    assert hasattr(QualityMetamodel_QMM_OCL_OclFeature, "eq")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_OclFeature.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_qmm_ocl_import_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_Import)


def test_qualitymetamodel_qmm_ocl_import_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_Import.__init__)


def test_qualitymetamodel_qmm_ocl_import_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_Import.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_module_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_Module)


def test_qualitymetamodel_qmm_ocl_module_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_Module.__init__)


def test_qualitymetamodel_qmm_ocl_module_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_Module.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_collectionpart_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_CollectionPart)


def test_qualitymetamodel_qmm_ocl_collectionpart_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_CollectionPart.__init__)


def test_qualitymetamodel_qmm_ocl_collectionpart_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_CollectionPart.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_propertycall_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_PropertyCall)


def test_qualitymetamodel_qmm_ocl_propertycall_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_PropertyCall.__init__)


def test_qualitymetamodel_qmm_ocl_propertycall_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_PropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OclContextDefinition)


def test_qualitymetamodel_qmm_ocl_oclcontextdefinition_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OclContextDefinition.__init__)


def test_qualitymetamodel_qmm_ocl_oclcontextdefinition_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_VariableDeclaration)


def test_qualitymetamodel_qmm_ocl_variabledeclaration_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_VariableDeclaration.__init__)


def test_qualitymetamodel_qmm_ocl_variabledeclaration_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_qualitymetamodel_qmm_ocl_variabledeclaration_has_varName():
    assert hasattr(QualityMetamodel_QMM_OCL_VariableDeclaration, "varName")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_qmm_ocl_staticpropertycall_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_StaticPropertyCall)


def test_qualitymetamodel_qmm_ocl_staticpropertycall_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_StaticPropertyCall.__init__)


def test_qualitymetamodel_qmm_ocl_staticpropertycall_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_StaticPropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_mapelement_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_MapElement)


def test_qualitymetamodel_qmm_ocl_mapelement_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_MapElement.__init__)


def test_qualitymetamodel_qmm_ocl_mapelement_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_MapElement.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_moduleelement_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_ModuleElement)


def test_qualitymetamodel_qmm_ocl_moduleelement_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_ModuleElement.__init__)


def test_qualitymetamodel_qmm_ocl_moduleelement_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_ocltype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OclType)


def test_qualitymetamodel_qmm_ocl_ocltype_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OclType.__init__)


def test_qualitymetamodel_qmm_ocl_ocltype_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel_qmm_ocl_ocltype_has_name():
    assert hasattr(QualityMetamodel_QMM_OCL_OclType, "name")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_qmm_ocl_tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_TupleTypeAttribute)


def test_qualitymetamodel_qmm_ocl_tupletypeattribute_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_TupleTypeAttribute.__init__)


def test_qualitymetamodel_qmm_ocl_tupletypeattribute_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel_qmm_ocl_tupletypeattribute_has_name():
    assert hasattr(QualityMetamodel_QMM_OCL_TupleTypeAttribute, "name")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_qmm_ocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_OclExpression)


def test_qualitymetamodel_qmm_ocl_oclexpression_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_OclExpression.__init__)


def test_qualitymetamodel_qmm_ocl_oclexpression_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_namedelement_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_NamedElement)


def test_qualitymetamodel_qmm_ocl_namedelement_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_NamedElement.__init__)


def test_qualitymetamodel_qmm_ocl_namedelement_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel_qmm_ocl_namedelement_has_name():
    assert hasattr(QualityMetamodel_QMM_OCL_NamedElement, "name")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_qmm_ocl_locatedelement_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_LocatedElement)


def test_qualitymetamodel_qmm_ocl_locatedelement_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_LocatedElement.__init__)


def test_qualitymetamodel_qmm_ocl_locatedelement_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "charStart" in params, "Missing parameter 'charStart'"
    assert "charEnd" in params, "Missing parameter 'charEnd'"
    assert "column" in params, "Missing parameter 'column'"
    assert "line" in params, "Missing parameter 'line'"

def test_qualitymetamodel_qmm_ocl_locatedelement_has_charStart():
    assert hasattr(QualityMetamodel_QMM_OCL_LocatedElement, "charStart")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_LocatedElement.__mro__:
        if "charStart" in klass.__dict__:
            descriptor = klass.__dict__["charStart"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_qmm_ocl_locatedelement_has_charEnd():
    assert hasattr(QualityMetamodel_QMM_OCL_LocatedElement, "charEnd")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_LocatedElement.__mro__:
        if "charEnd" in klass.__dict__:
            descriptor = klass.__dict__["charEnd"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_qmm_ocl_locatedelement_has_column():
    assert hasattr(QualityMetamodel_QMM_OCL_LocatedElement, "column")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_LocatedElement.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_qmm_ocl_locatedelement_has_line():
    assert hasattr(QualityMetamodel_QMM_OCL_LocatedElement, "line")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_LocatedElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_integervaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_IntegerValueType)


def test_qualitymetamodel_integervaluetype_constructor_exists():
    assert callable(QualityMetamodel_IntegerValueType.__init__)


def test_qualitymetamodel_integervaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_IntegerValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel_integervaluetype_has_value():
    assert hasattr(QualityMetamodel_IntegerValueType, "value")
    descriptor = None
    for klass in QualityMetamodel_IntegerValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_booleanvaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_BooleanValueType)


def test_qualitymetamodel_booleanvaluetype_constructor_exists():
    assert callable(QualityMetamodel_BooleanValueType.__init__)


def test_qualitymetamodel_booleanvaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_BooleanValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel_booleanvaluetype_has_value():
    assert hasattr(QualityMetamodel_BooleanValueType, "value")
    descriptor = None
    for klass in QualityMetamodel_BooleanValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_realvaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_RealValueType)


def test_qualitymetamodel_realvaluetype_constructor_exists():
    assert callable(QualityMetamodel_RealValueType.__init__)


def test_qualitymetamodel_realvaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_RealValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel_realvaluetype_has_value():
    assert hasattr(QualityMetamodel_RealValueType, "value")
    descriptor = None
    for klass in QualityMetamodel_RealValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_iterator_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_Iterator)


def test_qualitymetamodel_qmm_ocl_iterator_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_Iterator.__init__)


def test_qualitymetamodel_qmm_ocl_iterator_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_Iterator.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qualityattribute_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QualityAttribute)


def test_qualitymetamodel_qualityattribute_constructor_exists():
    assert callable(QualityMetamodel_QualityAttribute.__init__)


def test_qualitymetamodel_qualityattribute_constructor_args():
    sig = inspect.signature(QualityMetamodel_QualityAttribute.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_valuetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_ValueType)


def test_qualitymetamodel_valuetype_constructor_exists():
    assert callable(QualityMetamodel_ValueType.__init__)


def test_qualitymetamodel_valuetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_ValueType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_parameter_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_Parameter)


def test_qualitymetamodel_qmm_ocl_parameter_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_Parameter.__init__)


def test_qualitymetamodel_qmm_ocl_parameter_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_qmm_ocl_localvariable_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QMM_OCL_LocalVariable)


def test_qualitymetamodel_qmm_ocl_localvariable_constructor_exists():
    assert callable(QualityMetamodel_QMM_OCL_LocalVariable.__init__)


def test_qualitymetamodel_qmm_ocl_localvariable_constructor_args():
    sig = inspect.signature(QualityMetamodel_QMM_OCL_LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_qualitymetamodel_qmm_ocl_localvariable_has_eq():
    assert hasattr(QualityMetamodel_QMM_OCL_LocalVariable, "eq")
    descriptor = None
    for klass in QualityMetamodel_QMM_OCL_LocalVariable.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_value_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_Value)


def test_qualitymetamodel_value_constructor_exists():
    assert callable(QualityMetamodel_Value.__init__)


def test_qualitymetamodel_value_constructor_args():
    sig = inspect.signature(QualityMetamodel_Value.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_qualitymetamodel_value_has_description():
    assert hasattr(QualityMetamodel_Value, "description")
    descriptor = None
    for klass in QualityMetamodel_Value.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_aggregatedvaluemetric_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_AggregatedValueMetric)


def test_qualitymetamodel_aggregatedvaluemetric_constructor_exists():
    assert callable(QualityMetamodel_AggregatedValueMetric.__init__)


def test_qualitymetamodel_aggregatedvaluemetric_constructor_args():
    sig = inspect.signature(QualityMetamodel_AggregatedValueMetric.__init__)
    params = list(sig.parameters.keys())
    assert "maximum" in params, "Missing parameter 'maximum'"
    assert "standardDeviation" in params, "Missing parameter 'standardDeviation'"
    assert "average" in params, "Missing parameter 'average'"
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "median" in params, "Missing parameter 'median'"

def test_qualitymetamodel_aggregatedvaluemetric_has_maximum():
    assert hasattr(QualityMetamodel_AggregatedValueMetric, "maximum")
    descriptor = None
    for klass in QualityMetamodel_AggregatedValueMetric.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_aggregatedvaluemetric_has_standardDeviation():
    assert hasattr(QualityMetamodel_AggregatedValueMetric, "standardDeviation")
    descriptor = None
    for klass in QualityMetamodel_AggregatedValueMetric.__mro__:
        if "standardDeviation" in klass.__dict__:
            descriptor = klass.__dict__["standardDeviation"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_aggregatedvaluemetric_has_average():
    assert hasattr(QualityMetamodel_AggregatedValueMetric, "average")
    descriptor = None
    for klass in QualityMetamodel_AggregatedValueMetric.__mro__:
        if "average" in klass.__dict__:
            descriptor = klass.__dict__["average"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_aggregatedvaluemetric_has_minimum():
    assert hasattr(QualityMetamodel_AggregatedValueMetric, "minimum")
    descriptor = None
    for klass in QualityMetamodel_AggregatedValueMetric.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_aggregatedvaluemetric_has_median():
    assert hasattr(QualityMetamodel_AggregatedValueMetric, "median")
    descriptor = None
    for klass in QualityMetamodel_AggregatedValueMetric.__mro__:
        if "median" in klass.__dict__:
            descriptor = klass.__dict__["median"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_rangevaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_RangeValueType)


def test_qualitymetamodel_rangevaluetype_constructor_exists():
    assert callable(QualityMetamodel_RangeValueType.__init__)


def test_qualitymetamodel_rangevaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_RangeValueType.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_qualitymetamodel_rangevaluetype_has_min():
    assert hasattr(QualityMetamodel_RangeValueType, "min")
    descriptor = None
    for klass in QualityMetamodel_RangeValueType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_rangevaluetype_has_max():
    assert hasattr(QualityMetamodel_RangeValueType, "max")
    descriptor = None
    for klass in QualityMetamodel_RangeValueType.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
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
Parameter_strategy = st.builds(
    Parameter,
)
OclInstanceModel_strategy = st.builds(
    OclInstanceModel,
)
OclModelElement_strategy = st.builds(
    OclModelElement,
)
OclFeatureDefinition_strategy = st.builds(
    OclFeatureDefinition,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
QualityMetamodel_QMM_OCL_Attribute_strategy = st.builds(
    QualityMetamodel_QMM_OCL_Attribute,
)
QualityMetamodel_QMM_OCL_Operation_strategy = st.builds(
    QualityMetamodel_QMM_OCL_Operation,
)
NumericType_strategy = st.builds(
    NumericType,
)
QualityMetamodel_QMM_OCL_RealType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_RealType,
)
QualityMetamodel_QMM_OCL_IntegerType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_IntegerType,
)
TupleType_strategy = st.builds(
    TupleType,
)
OclContextDefinition_strategy = st.builds(
    OclContextDefinition,
)
Primitive_strategy = st.builds(
    Primitive,
)
QualityMetamodel_QMM_OCL_NumericType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_NumericType,
)
QualityMetamodel_QMM_OCL_BooleanType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_BooleanType,
)
QualityMetamodel_QMM_OCL_StringType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_StringType,
)
OclModel_strategy = st.builds(
    OclModel,
)
QualityMetamodel_QMM_OCL_OclInstanceModel_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OclInstanceModel,
)
QualityMetamodel_QMM_OCL_OclMetamodel_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OclMetamodel,
    uri=
        safe_text
)
LambdaType_strategy = st.builds(
    LambdaType,
)
TupleTypeAttribute_strategy = st.builds(
    TupleTypeAttribute,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
QualityMetamodel_QMM_OCL_SequenceType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_SequenceType,
)
QualityMetamodel_QMM_OCL_BagType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_BagType,
)
QualityMetamodel_QMM_OCL_OrderedSetType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OrderedSetType,
)
QualityMetamodel_QMM_OCL_SetType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_SetType,
)
MapType_strategy = st.builds(
    MapType,
)
IterateExp_strategy = st.builds(
    IterateExp,
)
Iterator_strategy = st.builds(
    Iterator,
)
VariableExp_strategy = st.builds(
    VariableExp,
)
QualityMetamodel_QMM_OCL_LambdaCallExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_LambdaCallExp,
)
MapExp_strategy = st.builds(
    MapExp,
)
MapElement_strategy = st.builds(
    MapElement,
)
PropertyCall_strategy = st.builds(
    PropertyCall,
)
QualityMetamodel_QMM_OCL_OperationCall_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OperationCall,
    operationName=
        safe_text
)
QualityMetamodel_QMM_OCL_LoopExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_LoopExp,
)
QualityMetamodel_QMM_OCL_NavigationOrAttributeCall_strategy = st.builds(
    QualityMetamodel_QMM_OCL_NavigationOrAttributeCall,
    name=
        safe_text
)
StaticPropertyCallExp_strategy = st.builds(
    StaticPropertyCallExp,
)
StaticPropertyCall_strategy = st.builds(
    StaticPropertyCall,
)
QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall_strategy = st.builds(
    QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall,
    name=
        safe_text
)
QualityMetamodel_QMM_OCL_StaticOperationCall_strategy = st.builds(
    QualityMetamodel_QMM_OCL_StaticOperationCall,
    operationName=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
QualityMetamodel_QMM_OCL_StringExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_StringExp,
    stringSymbol=
        safe_text
)
TupleExp_strategy = st.builds(
    TupleExp,
)
TuplePart_strategy = st.builds(
    TuplePart,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
QualityMetamodel_QMM_OCL_SetExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_SetExp,
)
QualityMetamodel_QMM_OCL_OrderedSetExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OrderedSetExp,
)
QualityMetamodel_QMM_OCL_SequenceExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_SequenceExp,
)
QualityMetamodel_QMM_OCL_BagExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_BagExp,
)
CollectionPart_strategy = st.builds(
    CollectionPart,
)
QualityMetamodel_QMM_OCL_CollectionItem_strategy = st.builds(
    QualityMetamodel_QMM_OCL_CollectionItem,
)
QualityMetamodel_QMM_OCL_CollectionRange_strategy = st.builds(
    QualityMetamodel_QMM_OCL_CollectionRange,
)
NumericExp_strategy = st.builds(
    NumericExp,
)
QualityMetamodel_QMM_OCL_IntegerExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_IntegerExp,
    integerSymbol=
        safe_text
)
QualityMetamodel_QMM_OCL_RealExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_RealExp,
    realSymbol=
        safe_text
)
ValueType_strategy = st.builds(
    ValueType,
)
QualityMetamodel_TextValueType_strategy = st.builds(
    QualityMetamodel_TextValueType,
    value=
        safe_text
)
OclExpression_strategy = st.builds(
    OclExpression,
)
QualityMetamodel_QMM_OCL_MapExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_MapExp,
)
QualityMetamodel_QMM_OCL_LetExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_LetExp,
)
QualityMetamodel_QMM_OCL_TupleExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_TupleExp,
)
QualityMetamodel_QMM_OCL_EnumLiteralExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_EnumLiteralExp,
    name=
        safe_text
)
QualityMetamodel_QMM_OCL_PrimitiveExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_PrimitiveExp,
)
QualityMetamodel_QMM_OCL_OclUndefinedExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OclUndefinedExp,
)
QualityMetamodel_QMM_OCL_SuperExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_SuperExp,
)
QualityMetamodel_QMM_OCL_OperatorCallExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OperatorCallExp,
    operationName=
        safe_text
)
QualityMetamodel_QMM_OCL_SelfExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_SelfExp,
)
QualityMetamodel_QMM_OCL_IfExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_IfExp,
)
QualityMetamodel_QMM_OCL_BraceExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_BraceExp,
)
QualityMetamodel_QMM_OCL_CollectionExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_CollectionExp,
)
QualityMetamodel_QMM_OCL_StaticPropertyCallExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_StaticPropertyCallExp,
)
QualityMetamodel_QMM_OCL_OclModelElementExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OclModelElementExp,
    name=
        safe_text
)
QualityMetamodel_QMM_OCL_PropertyCallExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_PropertyCallExp,
)
QualityMetamodel_QMM_OCL_EnvExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_EnvExp,
)
QualityMetamodel_Operation_strategy = st.builds(
    QualityMetamodel_Operation,
    name=
        safe_text,
    body=
        safe_text
)
Value_strategy = st.builds(
    Value,
)
QualityMetamodel_AggregatedValue_strategy = st.builds(
    QualityMetamodel_AggregatedValue,
)
QualityMetamodel_SingleValue_strategy = st.builds(
    QualityMetamodel_SingleValue,
)
QualityMetamodel_MetricProvider_strategy = st.builds(
    QualityMetamodel_MetricProvider,
    id=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
Module_strategy = st.builds(
    Module,
)
QualityMetamodel_QualityModel_strategy = st.builds(
    QualityMetamodel_QualityModel,
)
QualityMetamodel_QMM_OCL_NumericExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_NumericExp,
)
QualityMetamodel_QMM_OCL_BooleanExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_BooleanExp,
    booleanSymbol=
        safe_text
)
IfExp_strategy = st.builds(
    IfExp,
)
OclType_strategy = st.builds(
    OclType,
)
QualityMetamodel_QMM_OCL_MapType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_MapType,
)
QualityMetamodel_QMM_OCL_LambdaType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_LambdaType,
)
QualityMetamodel_QMM_OCL_CollectionType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_CollectionType,
)
QualityMetamodel_QMM_OCL_EnvType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_EnvType,
)
QualityMetamodel_QMM_OCL_OclModelElement_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OclModelElement,
)
QualityMetamodel_QMM_OCL_OclAnyType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OclAnyType,
)
QualityMetamodel_QMM_OCL_TupleType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_TupleType,
)
QualityMetamodel_QMM_OCL_Primitive_strategy = st.builds(
    QualityMetamodel_QMM_OCL_Primitive,
)
QualityMetamodel_QMM_OCL_VariableExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_VariableExp,
)
OperatorCallExp_strategy = st.builds(
    OperatorCallExp,
)
QualityMetamodel_QMM_OCL_AddOpCallExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_AddOpCallExp,
)
QualityMetamodel_QMM_OCL_IntOpCallExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_IntOpCallExp,
)
QualityMetamodel_QMM_OCL_NotOpCallExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_NotOpCallExp,
)
QualityMetamodel_QMM_OCL_EqOpCallExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_EqOpCallExp,
)
QualityMetamodel_QMM_OCL_MulOpCallExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_MulOpCallExp,
)
QualityMetamodel_QMM_OCL_RelOpCallExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_RelOpCallExp,
)
Attribute_strategy = st.builds(
    Attribute,
)
Operation_strategy = st.builds(
    Operation,
)
LocalVariable_strategy = st.builds(
    LocalVariable,
)
QualityMetamodel_QMM_OCL_TuplePart_strategy = st.builds(
    QualityMetamodel_QMM_OCL_TuplePart,
)
OperationCall_strategy = st.builds(
    OperationCall,
)
QualityMetamodel_QMM_OCL_CollectionOperationCall_strategy = st.builds(
    QualityMetamodel_QMM_OCL_CollectionOperationCall,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
QualityMetamodel_QMM_OCL_IterateExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_IterateExp,
)
QualityMetamodel_QMM_OCL_IteratorExp_strategy = st.builds(
    QualityMetamodel_QMM_OCL_IteratorExp,
    name=
        safe_text
)
LetExp_strategy = st.builds(
    LetExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
QualityMetamodel_EnumerationItem_strategy = st.builds(
    QualityMetamodel_EnumerationItem,
    name=
        safe_text
)
QualityMetamodel_EnumerationMetric_strategy = st.builds(
    QualityMetamodel_EnumerationMetric,
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
QualityMetamodel_QMM_OCL_OclFeatureDefinition_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OclFeatureDefinition,
    static=
        safe_text
)
Import_strategy = st.builds(
    Import,
)
OclMetamodel_strategy = st.builds(
    OclMetamodel,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
QualityMetamodel_QMM_OCL_OclModel_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OclModel,
)
QualityMetamodel_QMM_OCL_OclFeature_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OclFeature,
    eq=
        safe_text
)
QualityMetamodel_QMM_OCL_Import_strategy = st.builds(
    QualityMetamodel_QMM_OCL_Import,
)
QualityMetamodel_QMM_OCL_Module_strategy = st.builds(
    QualityMetamodel_QMM_OCL_Module,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
QualityMetamodel_QMM_OCL_CollectionPart_strategy = st.builds(
    QualityMetamodel_QMM_OCL_CollectionPart,
)
QualityMetamodel_QMM_OCL_PropertyCall_strategy = st.builds(
    QualityMetamodel_QMM_OCL_PropertyCall,
)
QualityMetamodel_QMM_OCL_OclContextDefinition_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OclContextDefinition,
)
QualityMetamodel_QMM_OCL_VariableDeclaration_strategy = st.builds(
    QualityMetamodel_QMM_OCL_VariableDeclaration,
    varName=
        safe_text
)
QualityMetamodel_QMM_OCL_StaticPropertyCall_strategy = st.builds(
    QualityMetamodel_QMM_OCL_StaticPropertyCall,
)
QualityMetamodel_QMM_OCL_MapElement_strategy = st.builds(
    QualityMetamodel_QMM_OCL_MapElement,
)
QualityMetamodel_QMM_OCL_ModuleElement_strategy = st.builds(
    QualityMetamodel_QMM_OCL_ModuleElement,
)
QualityMetamodel_QMM_OCL_OclType_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OclType,
    name=
        safe_text
)
QualityMetamodel_QMM_OCL_TupleTypeAttribute_strategy = st.builds(
    QualityMetamodel_QMM_OCL_TupleTypeAttribute,
    name=
        safe_text
)
QualityMetamodel_QMM_OCL_OclExpression_strategy = st.builds(
    QualityMetamodel_QMM_OCL_OclExpression,
)
QualityMetamodel_QMM_OCL_NamedElement_strategy = st.builds(
    QualityMetamodel_QMM_OCL_NamedElement,
    name=
        safe_text
)
QualityMetamodel_QMM_OCL_LocatedElement_strategy = st.builds(
    QualityMetamodel_QMM_OCL_LocatedElement,
    charStart=
        safe_text,
    charEnd=
        safe_text,
    column=
        safe_text,
    line=
        safe_text
)
QualityMetamodel_IntegerValueType_strategy = st.builds(
    QualityMetamodel_IntegerValueType,
    value=
        safe_text
)
QualityMetamodel_BooleanValueType_strategy = st.builds(
    QualityMetamodel_BooleanValueType,
    value=
        safe_text
)
QualityMetamodel_RealValueType_strategy = st.builds(
    QualityMetamodel_RealValueType,
    value=
        safe_text
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
QualityMetamodel_QMM_OCL_Iterator_strategy = st.builds(
    QualityMetamodel_QMM_OCL_Iterator,
)
QualityMetamodel_QualityAttribute_strategy = st.builds(
    QualityMetamodel_QualityAttribute,
)
QualityMetamodel_ValueType_strategy = st.builds(
    QualityMetamodel_ValueType,
)
QualityMetamodel_QMM_OCL_Parameter_strategy = st.builds(
    QualityMetamodel_QMM_OCL_Parameter,
)
QualityMetamodel_QMM_OCL_LocalVariable_strategy = st.builds(
    QualityMetamodel_QMM_OCL_LocalVariable,
    eq=
        safe_text
)
QualityMetamodel_Value_strategy = st.builds(
    QualityMetamodel_Value,
    description=
        safe_text
)
QualityMetamodel_AggregatedValueMetric_strategy = st.builds(
    QualityMetamodel_AggregatedValueMetric,
    maximum=
        safe_text,
    standardDeviation=
        safe_text,
    average=
        safe_text,
    minimum=
        safe_text,
    median=
        safe_text
)
QualityMetamodel_RangeValueType_strategy = st.builds(
    QualityMetamodel_RangeValueType,
    min=
        safe_text,
    max=
        safe_text
)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=OclInstanceModel_strategy)
@settings(max_examples=50)
def test_oclinstancemodel_instantiation(instance):
    assert isinstance(instance, OclInstanceModel)

@given(instance=OclModelElement_strategy)
@settings(max_examples=50)
def test_oclmodelelement_instantiation(instance):
    assert isinstance(instance, OclModelElement)

@given(instance=OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, OclFeatureDefinition)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=QualityMetamodel_QMM_OCL_Attribute_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_attribute_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_Attribute)

@given(instance=QualityMetamodel_QMM_OCL_Operation_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_operation_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_Operation)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=QualityMetamodel_QMM_OCL_RealType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_realtype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_RealType)

@given(instance=QualityMetamodel_QMM_OCL_IntegerType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_integertype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_IntegerType)

@given(instance=TupleType_strategy)
@settings(max_examples=50)
def test_tupletype_instantiation(instance):
    assert isinstance(instance, TupleType)

@given(instance=OclContextDefinition_strategy)
@settings(max_examples=50)
def test_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OclContextDefinition)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=QualityMetamodel_QMM_OCL_NumericType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_numerictype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_NumericType)

@given(instance=QualityMetamodel_QMM_OCL_BooleanType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_booleantype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_BooleanType)

@given(instance=QualityMetamodel_QMM_OCL_StringType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_stringtype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_StringType)

@given(instance=OclModel_strategy)
@settings(max_examples=50)
def test_oclmodel_instantiation(instance):
    assert isinstance(instance, OclModel)

@given(instance=QualityMetamodel_QMM_OCL_OclInstanceModel_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_oclinstancemodel_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OclInstanceModel)

@given(instance=QualityMetamodel_QMM_OCL_OclMetamodel_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_oclmetamodel_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OclMetamodel)



@given(instance=QualityMetamodel_QMM_OCL_OclMetamodel_strategy)
def test_qualitymetamodel_qmm_ocl_oclmetamodel_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=LambdaType_strategy)
@settings(max_examples=50)
def test_lambdatype_instantiation(instance):
    assert isinstance(instance, LambdaType)

@given(instance=TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, TupleTypeAttribute)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=QualityMetamodel_QMM_OCL_SequenceType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_sequencetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_SequenceType)

@given(instance=QualityMetamodel_QMM_OCL_BagType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_bagtype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_BagType)

@given(instance=QualityMetamodel_QMM_OCL_OrderedSetType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_orderedsettype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OrderedSetType)

@given(instance=QualityMetamodel_QMM_OCL_SetType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_settype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_SetType)

@given(instance=MapType_strategy)
@settings(max_examples=50)
def test_maptype_instantiation(instance):
    assert isinstance(instance, MapType)

@given(instance=IterateExp_strategy)
@settings(max_examples=50)
def test_iterateexp_instantiation(instance):
    assert isinstance(instance, IterateExp)

@given(instance=Iterator_strategy)
@settings(max_examples=50)
def test_iterator_instantiation(instance):
    assert isinstance(instance, Iterator)

@given(instance=VariableExp_strategy)
@settings(max_examples=50)
def test_variableexp_instantiation(instance):
    assert isinstance(instance, VariableExp)

@given(instance=QualityMetamodel_QMM_OCL_LambdaCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_lambdacallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_LambdaCallExp)

@given(instance=MapExp_strategy)
@settings(max_examples=50)
def test_mapexp_instantiation(instance):
    assert isinstance(instance, MapExp)

@given(instance=MapElement_strategy)
@settings(max_examples=50)
def test_mapelement_instantiation(instance):
    assert isinstance(instance, MapElement)

@given(instance=PropertyCall_strategy)
@settings(max_examples=50)
def test_propertycall_instantiation(instance):
    assert isinstance(instance, PropertyCall)

@given(instance=QualityMetamodel_QMM_OCL_OperationCall_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_operationcall_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OperationCall)



@given(instance=QualityMetamodel_QMM_OCL_OperationCall_strategy)
def test_qualitymetamodel_qmm_ocl_operationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=QualityMetamodel_QMM_OCL_LoopExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_loopexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_LoopExp)

@given(instance=QualityMetamodel_QMM_OCL_NavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_navigationorattributecall_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_NavigationOrAttributeCall)



@given(instance=QualityMetamodel_QMM_OCL_NavigationOrAttributeCall_strategy)
def test_qualitymetamodel_qmm_ocl_navigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StaticPropertyCallExp_strategy)
@settings(max_examples=50)
def test_staticpropertycallexp_instantiation(instance):
    assert isinstance(instance, StaticPropertyCallExp)

@given(instance=StaticPropertyCall_strategy)
@settings(max_examples=50)
def test_staticpropertycall_instantiation(instance):
    assert isinstance(instance, StaticPropertyCall)

@given(instance=QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_staticnavigationorattributecall_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall)



@given(instance=QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall_strategy)
def test_qualitymetamodel_qmm_ocl_staticnavigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel_QMM_OCL_StaticOperationCall_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_staticoperationcall_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_StaticOperationCall)



@given(instance=QualityMetamodel_QMM_OCL_StaticOperationCall_strategy)
def test_qualitymetamodel_qmm_ocl_staticoperationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=QualityMetamodel_QMM_OCL_StringExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_stringexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_StringExp)



@given(instance=QualityMetamodel_QMM_OCL_StringExp_strategy)
def test_qualitymetamodel_qmm_ocl_stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=TupleExp_strategy)
@settings(max_examples=50)
def test_tupleexp_instantiation(instance):
    assert isinstance(instance, TupleExp)

@given(instance=TuplePart_strategy)
@settings(max_examples=50)
def test_tuplepart_instantiation(instance):
    assert isinstance(instance, TuplePart)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=QualityMetamodel_QMM_OCL_SetExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_setexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_SetExp)

@given(instance=QualityMetamodel_QMM_OCL_OrderedSetExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_orderedsetexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OrderedSetExp)

@given(instance=QualityMetamodel_QMM_OCL_SequenceExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_sequenceexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_SequenceExp)

@given(instance=QualityMetamodel_QMM_OCL_BagExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_bagexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_BagExp)

@given(instance=CollectionPart_strategy)
@settings(max_examples=50)
def test_collectionpart_instantiation(instance):
    assert isinstance(instance, CollectionPart)

@given(instance=QualityMetamodel_QMM_OCL_CollectionItem_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_collectionitem_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_CollectionItem)

@given(instance=QualityMetamodel_QMM_OCL_CollectionRange_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_collectionrange_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_CollectionRange)

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=QualityMetamodel_QMM_OCL_IntegerExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_integerexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_IntegerExp)



@given(instance=QualityMetamodel_QMM_OCL_IntegerExp_strategy)
def test_qualitymetamodel_qmm_ocl_integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=QualityMetamodel_QMM_OCL_RealExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_realexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_RealExp)



@given(instance=QualityMetamodel_QMM_OCL_RealExp_strategy)
def test_qualitymetamodel_qmm_ocl_realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=QualityMetamodel_TextValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_textvaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_TextValueType)



@given(instance=QualityMetamodel_TextValueType_strategy)
def test_qualitymetamodel_textvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=QualityMetamodel_QMM_OCL_MapExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_mapexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_MapExp)

@given(instance=QualityMetamodel_QMM_OCL_LetExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_letexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_LetExp)

@given(instance=QualityMetamodel_QMM_OCL_TupleExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_tupleexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_TupleExp)

@given(instance=QualityMetamodel_QMM_OCL_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_enumliteralexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_EnumLiteralExp)



@given(instance=QualityMetamodel_QMM_OCL_EnumLiteralExp_strategy)
def test_qualitymetamodel_qmm_ocl_enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel_QMM_OCL_PrimitiveExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_primitiveexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_PrimitiveExp)

@given(instance=QualityMetamodel_QMM_OCL_OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_oclundefinedexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OclUndefinedExp)

@given(instance=QualityMetamodel_QMM_OCL_SuperExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_superexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_SuperExp)

@given(instance=QualityMetamodel_QMM_OCL_OperatorCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_operatorcallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OperatorCallExp)



@given(instance=QualityMetamodel_QMM_OCL_OperatorCallExp_strategy)
def test_qualitymetamodel_qmm_ocl_operatorcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=QualityMetamodel_QMM_OCL_SelfExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_selfexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_SelfExp)

@given(instance=QualityMetamodel_QMM_OCL_IfExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_ifexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_IfExp)

@given(instance=QualityMetamodel_QMM_OCL_BraceExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_braceexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_BraceExp)

@given(instance=QualityMetamodel_QMM_OCL_CollectionExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_collectionexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_CollectionExp)

@given(instance=QualityMetamodel_QMM_OCL_StaticPropertyCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_staticpropertycallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_StaticPropertyCallExp)

@given(instance=QualityMetamodel_QMM_OCL_OclModelElementExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_oclmodelelementexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OclModelElementExp)



@given(instance=QualityMetamodel_QMM_OCL_OclModelElementExp_strategy)
def test_qualitymetamodel_qmm_ocl_oclmodelelementexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel_QMM_OCL_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_propertycallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_PropertyCallExp)

@given(instance=QualityMetamodel_QMM_OCL_EnvExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_envexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_EnvExp)

@given(instance=QualityMetamodel_Operation_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_operation_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_Operation)



@given(instance=QualityMetamodel_Operation_strategy)
def test_qualitymetamodel_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=QualityMetamodel_Operation_strategy)
def test_qualitymetamodel_operation_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=QualityMetamodel_AggregatedValue_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_aggregatedvalue_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_AggregatedValue)

@given(instance=QualityMetamodel_SingleValue_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_singlevalue_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_SingleValue)

@given(instance=QualityMetamodel_MetricProvider_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_metricprovider_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_MetricProvider)



@given(instance=QualityMetamodel_MetricProvider_strategy)
def test_qualitymetamodel_metricprovider_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=QualityMetamodel_MetricProvider_strategy)
def test_qualitymetamodel_metricprovider_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=QualityMetamodel_MetricProvider_strategy)
def test_qualitymetamodel_metricprovider_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=QualityMetamodel_QualityModel_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qualitymodel_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QualityModel)

@given(instance=QualityMetamodel_QMM_OCL_NumericExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_numericexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_NumericExp)

@given(instance=QualityMetamodel_QMM_OCL_BooleanExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_booleanexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_BooleanExp)



@given(instance=QualityMetamodel_QMM_OCL_BooleanExp_strategy)
def test_qualitymetamodel_qmm_ocl_booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=IfExp_strategy)
@settings(max_examples=50)
def test_ifexp_instantiation(instance):
    assert isinstance(instance, IfExp)

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=QualityMetamodel_QMM_OCL_MapType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_maptype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_MapType)

@given(instance=QualityMetamodel_QMM_OCL_LambdaType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_lambdatype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_LambdaType)

@given(instance=QualityMetamodel_QMM_OCL_CollectionType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_collectiontype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_CollectionType)

@given(instance=QualityMetamodel_QMM_OCL_EnvType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_envtype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_EnvType)

@given(instance=QualityMetamodel_QMM_OCL_OclModelElement_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_oclmodelelement_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OclModelElement)

@given(instance=QualityMetamodel_QMM_OCL_OclAnyType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_oclanytype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OclAnyType)

@given(instance=QualityMetamodel_QMM_OCL_TupleType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_tupletype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_TupleType)

@given(instance=QualityMetamodel_QMM_OCL_Primitive_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_primitive_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_Primitive)

@given(instance=QualityMetamodel_QMM_OCL_VariableExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_variableexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_VariableExp)

@given(instance=OperatorCallExp_strategy)
@settings(max_examples=50)
def test_operatorcallexp_instantiation(instance):
    assert isinstance(instance, OperatorCallExp)

@given(instance=QualityMetamodel_QMM_OCL_AddOpCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_addopcallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_AddOpCallExp)

@given(instance=QualityMetamodel_QMM_OCL_IntOpCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_intopcallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_IntOpCallExp)

@given(instance=QualityMetamodel_QMM_OCL_NotOpCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_notopcallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_NotOpCallExp)

@given(instance=QualityMetamodel_QMM_OCL_EqOpCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_eqopcallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_EqOpCallExp)

@given(instance=QualityMetamodel_QMM_OCL_MulOpCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_mulopcallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_MulOpCallExp)

@given(instance=QualityMetamodel_QMM_OCL_RelOpCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_relopcallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_RelOpCallExp)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=LocalVariable_strategy)
@settings(max_examples=50)
def test_localvariable_instantiation(instance):
    assert isinstance(instance, LocalVariable)

@given(instance=QualityMetamodel_QMM_OCL_TuplePart_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_tuplepart_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_TuplePart)

@given(instance=OperationCall_strategy)
@settings(max_examples=50)
def test_operationcall_instantiation(instance):
    assert isinstance(instance, OperationCall)

@given(instance=QualityMetamodel_QMM_OCL_CollectionOperationCall_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_collectionoperationcall_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_CollectionOperationCall)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=QualityMetamodel_QMM_OCL_IterateExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_iterateexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_IterateExp)

@given(instance=QualityMetamodel_QMM_OCL_IteratorExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_iteratorexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_IteratorExp)



@given(instance=QualityMetamodel_QMM_OCL_IteratorExp_strategy)
def test_qualitymetamodel_qmm_ocl_iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=QualityMetamodel_EnumerationItem_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_enumerationitem_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_EnumerationItem)



@given(instance=QualityMetamodel_EnumerationItem_strategy)
def test_qualitymetamodel_enumerationitem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel_EnumerationMetric_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_enumerationmetric_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_EnumerationMetric)

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=QualityMetamodel_QMM_OCL_OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OclFeatureDefinition)



@given(instance=QualityMetamodel_QMM_OCL_OclFeatureDefinition_strategy)
def test_qualitymetamodel_qmm_ocl_oclfeaturedefinition_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=Import_strategy)
@settings(max_examples=50)
def test_import_instantiation(instance):
    assert isinstance(instance, Import)

@given(instance=OclMetamodel_strategy)
@settings(max_examples=50)
def test_oclmetamodel_instantiation(instance):
    assert isinstance(instance, OclMetamodel)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=QualityMetamodel_QMM_OCL_OclModel_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_oclmodel_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OclModel)

@given(instance=QualityMetamodel_QMM_OCL_OclFeature_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_oclfeature_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OclFeature)



@given(instance=QualityMetamodel_QMM_OCL_OclFeature_strategy)
def test_qualitymetamodel_qmm_ocl_oclfeature_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=QualityMetamodel_QMM_OCL_Import_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_import_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_Import)

@given(instance=QualityMetamodel_QMM_OCL_Module_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_module_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_Module)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=QualityMetamodel_QMM_OCL_CollectionPart_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_collectionpart_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_CollectionPart)

@given(instance=QualityMetamodel_QMM_OCL_PropertyCall_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_propertycall_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_PropertyCall)

@given(instance=QualityMetamodel_QMM_OCL_OclContextDefinition_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OclContextDefinition)

@given(instance=QualityMetamodel_QMM_OCL_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_variabledeclaration_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_VariableDeclaration)



@given(instance=QualityMetamodel_QMM_OCL_VariableDeclaration_strategy)
def test_qualitymetamodel_qmm_ocl_variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=QualityMetamodel_QMM_OCL_StaticPropertyCall_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_staticpropertycall_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_StaticPropertyCall)

@given(instance=QualityMetamodel_QMM_OCL_MapElement_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_mapelement_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_MapElement)

@given(instance=QualityMetamodel_QMM_OCL_ModuleElement_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_moduleelement_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_ModuleElement)

@given(instance=QualityMetamodel_QMM_OCL_OclType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_ocltype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OclType)



@given(instance=QualityMetamodel_QMM_OCL_OclType_strategy)
def test_qualitymetamodel_qmm_ocl_ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel_QMM_OCL_TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_TupleTypeAttribute)



@given(instance=QualityMetamodel_QMM_OCL_TupleTypeAttribute_strategy)
def test_qualitymetamodel_qmm_ocl_tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel_QMM_OCL_OclExpression_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_oclexpression_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_OclExpression)

@given(instance=QualityMetamodel_QMM_OCL_NamedElement_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_namedelement_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_NamedElement)



@given(instance=QualityMetamodel_QMM_OCL_NamedElement_strategy)
def test_qualitymetamodel_qmm_ocl_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel_QMM_OCL_LocatedElement_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_locatedelement_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_LocatedElement)



@given(instance=QualityMetamodel_QMM_OCL_LocatedElement_strategy)
def test_qualitymetamodel_qmm_ocl_locatedelement_charStart_setter(instance):
    original = instance.charStart
    instance.charStart = original
    assert instance.charStart == original



@given(instance=QualityMetamodel_QMM_OCL_LocatedElement_strategy)
def test_qualitymetamodel_qmm_ocl_locatedelement_charEnd_setter(instance):
    original = instance.charEnd
    instance.charEnd = original
    assert instance.charEnd == original



@given(instance=QualityMetamodel_QMM_OCL_LocatedElement_strategy)
def test_qualitymetamodel_qmm_ocl_locatedelement_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original



@given(instance=QualityMetamodel_QMM_OCL_LocatedElement_strategy)
def test_qualitymetamodel_qmm_ocl_locatedelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=QualityMetamodel_IntegerValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_integervaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_IntegerValueType)



@given(instance=QualityMetamodel_IntegerValueType_strategy)
def test_qualitymetamodel_integervaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=QualityMetamodel_BooleanValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_booleanvaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_BooleanValueType)



@given(instance=QualityMetamodel_BooleanValueType_strategy)
def test_qualitymetamodel_booleanvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=QualityMetamodel_RealValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_realvaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_RealValueType)



@given(instance=QualityMetamodel_RealValueType_strategy)
def test_qualitymetamodel_realvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=QualityMetamodel_QMM_OCL_Iterator_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_iterator_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_Iterator)

@given(instance=QualityMetamodel_QualityAttribute_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qualityattribute_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QualityAttribute)

@given(instance=QualityMetamodel_ValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_valuetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_ValueType)

@given(instance=QualityMetamodel_QMM_OCL_Parameter_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_parameter_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_Parameter)

@given(instance=QualityMetamodel_QMM_OCL_LocalVariable_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qmm_ocl_localvariable_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QMM_OCL_LocalVariable)



@given(instance=QualityMetamodel_QMM_OCL_LocalVariable_strategy)
def test_qualitymetamodel_qmm_ocl_localvariable_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=QualityMetamodel_Value_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_value_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_Value)



@given(instance=QualityMetamodel_Value_strategy)
def test_qualitymetamodel_value_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_aggregatedvaluemetric_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_AggregatedValueMetric)



@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
def test_qualitymetamodel_aggregatedvaluemetric_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original



@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
def test_qualitymetamodel_aggregatedvaluemetric_standardDeviation_setter(instance):
    original = instance.standardDeviation
    instance.standardDeviation = original
    assert instance.standardDeviation == original



@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
def test_qualitymetamodel_aggregatedvaluemetric_average_setter(instance):
    original = instance.average
    instance.average = original
    assert instance.average == original



@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
def test_qualitymetamodel_aggregatedvaluemetric_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original



@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
def test_qualitymetamodel_aggregatedvaluemetric_median_setter(instance):
    original = instance.median
    instance.median = original
    assert instance.median == original

@given(instance=QualityMetamodel_RangeValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_rangevaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_RangeValueType)



@given(instance=QualityMetamodel_RangeValueType_strategy)
def test_qualitymetamodel_rangevaluetype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=QualityMetamodel_RangeValueType_strategy)
def test_qualitymetamodel_rangevaluetype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original
