import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OclInstanceModel,
    OclModelElement,
    TupleType,
    OclFeatureDefinition,
    OclFeature,
    QualityMetamodel::QMM::OCL::Attribute,
    TupleTypeAttribute,
    CollectionType,
    MapType,
    QualityMetamodel::QMM::OCL::SetType,
    QualityMetamodel::QMM::OCL::SequenceType,
    QualityMetamodel::QMM::OCL::OrderedSetType,
    QualityMetamodel::QMM::OCL::BagType,
    NumericType,
    QualityMetamodel::QMM::OCL::RealType,
    QualityMetamodel::QMM::OCL::IntegerType,
    Primitive,
    QualityMetamodel::QMM::OCL::BooleanType,
    QualityMetamodel::QMM::OCL::NumericType,
    QualityMetamodel::QMM::OCL::StringType,
    OclModel,
    QualityMetamodel::QMM::OCL::OclMetamodel,
    LambdaType,
    OclContextDefinition,
    IterateExp,
    Iterator,
    PropertyCall,
    QualityMetamodel::QMM::OCL::LoopExp,
    VariableExp,
    QualityMetamodel::QMM::OCL::LambdaCallExp,
    QualityMetamodel::QMM::OCL::OperationCall,
    QualityMetamodel::QMM::OCL::NavigationOrAttributeCall,
    MapExp,
    Parameter,
    QualityMetamodel::QMM::OCL::Operation,
    QualityMetamodel::QMM::OCL::OclInstanceModel,
    MapElement,
    TupleExp,
    StaticPropertyCallExp,
    StaticPropertyCall,
    QualityMetamodel::QMM::OCL::StaticNavigationOrAttributeCall,
    QualityMetamodel::QMM::OCL::StaticOperationCall,
    NumericExp,
    QualityMetamodel::QMM::OCL::IntegerExp,
    QualityMetamodel::QMM::OCL::RealExp,
    PrimitiveExp,
    QualityMetamodel::QMM::OCL::NumericExp,
    QualityMetamodel::QMM::OCL::BooleanExp,
    QualityMetamodel::QMM::OCL::StringExp,
    TuplePart,
    CollectionExp,
    QualityMetamodel::QMM::OCL::OrderedSetExp,
    QualityMetamodel::QMM::OCL::BagExp,
    QualityMetamodel::QMM::OCL::SequenceExp,
    QualityMetamodel::QMM::OCL::SetExp,
    CollectionPart,
    QualityMetamodel::QMM::OCL::CollectionRange,
    QualityMetamodel::QMM::OCL::CollectionItem,
    LocalVariable,
    QualityMetamodel::QMM::OCL::TuplePart,
    OperatorCallExp,
    QualityMetamodel::QMM::OCL::EqOpCallExp,
    QualityMetamodel::QMM::OCL::IntOpCallExp,
    QualityMetamodel::QMM::OCL::NotOpCallExp,
    QualityMetamodel::QMM::OCL::AddOpCallExp,
    QualityMetamodel::QMM::OCL::RelOpCallExp,
    QualityMetamodel::QMM::OCL::MulOpCallExp,
    Attribute,
    Operation,
    ModuleElement,
    QualityMetamodel::QMM::OCL::OclFeatureDefinition,
    OperationCall,
    QualityMetamodel::QMM::OCL::CollectionOperationCall,
    LoopExp,
    QualityMetamodel::QMM::OCL::IteratorExp,
    QualityMetamodel::QMM::OCL::IterateExp,
    LetExp,
    PropertyCallExp,
    IfExp,
    OclType,
    QualityMetamodel::QMM::OCL::Primitive,
    QualityMetamodel::QMM::OCL::EnvType,
    QualityMetamodel::QMM::OCL::TupleType,
    QualityMetamodel::QMM::OCL::OclModelElement,
    QualityMetamodel::QMM::OCL::OclAnyType,
    QualityMetamodel::QMM::OCL::CollectionType,
    QualityMetamodel::QMM::OCL::MapType,
    QualityMetamodel::QMM::OCL::LambdaType,
    ValueType,
    QualityMetamodel::RangeValueType,
    QualityMetamodel::AggregatedValueMetric,
    QualityMetamodel::TextValueType,
    Import,
    OclMetamodel,
    NamedElement,
    QualityMetamodel::QMM::OCL::Import,
    QualityMetamodel::QMM::OCL::OclFeature,
    QualityMetamodel::QMM::OCL::OclModel,
    QualityMetamodel::QMM::OCL::Module,
    LocatedElement,
    QualityMetamodel::QMM::OCL::MapElement,
    QualityMetamodel::QMM::OCL::VariableDeclaration,
    QualityMetamodel::QMM::OCL::OclType,
    QualityMetamodel::QMM::OCL::CollectionPart,
    QualityMetamodel::QMM::OCL::OclContextDefinition,
    QualityMetamodel::QMM::OCL::ModuleElement,
    QualityMetamodel::QMM::OCL::OclExpression,
    QualityMetamodel::QMM::OCL::TupleTypeAttribute,
    QualityMetamodel::QMM::OCL::StaticPropertyCall,
    QualityMetamodel::QMM::OCL::PropertyCall,
    QualityMetamodel::QMM::OCL::NamedElement,
    QualityMetamodel::QMM::OCL::LocatedElement,
    QualityMetamodel::ListValue,
    QualityMetamodel::IntegerValueType,
    QualityMetamodel::BooleanValueType,
    QualityMetamodel::RealValueType,
    QualityMetamodel::EnumerationItem,
    QualityMetamodel::EnumerationMetric,
    QualityMetamodel::MetricProvider,
    Module,
    QualityMetamodel::QualityModel,
    OclExpression,
    QualityMetamodel::QMM::OCL::TupleExp,
    QualityMetamodel::QMM::OCL::CollectionExp,
    QualityMetamodel::QMM::OCL::BraceExp,
    QualityMetamodel::QMM::OCL::OclUndefinedExp,
    QualityMetamodel::QMM::OCL::LetExp,
    QualityMetamodel::QMM::OCL::EnumLiteralExp,
    QualityMetamodel::QMM::OCL::PrimitiveExp,
    QualityMetamodel::QMM::OCL::IfExp,
    QualityMetamodel::QMM::OCL::VariableExp,
    QualityMetamodel::QMM::OCL::OclModelElementExp,
    QualityMetamodel::QMM::OCL::PropertyCallExp,
    QualityMetamodel::QMM::OCL::EnvExp,
    QualityMetamodel::QMM::OCL::MapExp,
    QualityMetamodel::QMM::OCL::StaticPropertyCallExp,
    QualityMetamodel::QMM::OCL::OperatorCallExp,
    QualityMetamodel::QMM::OCL::SelfExp,
    QualityMetamodel::QMM::OCL::SuperExp,
    QualityMetamodel::Operation,
    Value,
    QualityMetamodel::AggregatedValue,
    QualityMetamodel::SingleValue,
    VariableDeclaration,
    QualityMetamodel::QMM::OCL::Iterator,
    QualityMetamodel::QMM::OCL::Parameter,
    QualityMetamodel::QMM::OCL::LocalVariable,
    QualityMetamodel::Value,
    QualityMetamodel::QualityAttribute,
    QualityMetamodel::ValueType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_tupletype_is_not_abstract():
    assert not inspect.isabstract(TupleType)


def test_tupletype_constructor_exists():
    assert callable(TupleType.__init__)


def test_tupletype_constructor_args():
    sig = inspect.signature(TupleType.__init__)
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



def test_qualitymetamodel::qmm::ocl::attribute_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::Attribute)


def test_qualitymetamodel::qmm::ocl::attribute_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::Attribute.__init__)


def test_qualitymetamodel::qmm::ocl::attribute_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::Attribute.__init__)
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



def test_maptype_is_not_abstract():
    assert not inspect.isabstract(MapType)


def test_maptype_constructor_exists():
    assert callable(MapType.__init__)


def test_maptype_constructor_args():
    sig = inspect.signature(MapType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::settype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::SetType)


def test_qualitymetamodel::qmm::ocl::settype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::SetType.__init__)


def test_qualitymetamodel::qmm::ocl::settype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::SetType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::SequenceType)


def test_qualitymetamodel::qmm::ocl::sequencetype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::SequenceType.__init__)


def test_qualitymetamodel::qmm::ocl::sequencetype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OrderedSetType)


def test_qualitymetamodel::qmm::ocl::orderedsettype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OrderedSetType.__init__)


def test_qualitymetamodel::qmm::ocl::orderedsettype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::BagType)


def test_qualitymetamodel::qmm::ocl::bagtype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::BagType.__init__)


def test_qualitymetamodel::qmm::ocl::bagtype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::BagType.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::realtype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::RealType)


def test_qualitymetamodel::qmm::ocl::realtype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::RealType.__init__)


def test_qualitymetamodel::qmm::ocl::realtype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::RealType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::integertype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::IntegerType)


def test_qualitymetamodel::qmm::ocl::integertype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::IntegerType.__init__)


def test_qualitymetamodel::qmm::ocl::integertype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::booleantype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::BooleanType)


def test_qualitymetamodel::qmm::ocl::booleantype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::BooleanType.__init__)


def test_qualitymetamodel::qmm::ocl::booleantype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::numerictype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::NumericType)


def test_qualitymetamodel::qmm::ocl::numerictype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::NumericType.__init__)


def test_qualitymetamodel::qmm::ocl::numerictype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::NumericType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::stringtype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::StringType)


def test_qualitymetamodel::qmm::ocl::stringtype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::StringType.__init__)


def test_qualitymetamodel::qmm::ocl::stringtype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::StringType.__init__)
    params = list(sig.parameters.keys())



def test_oclmodel_is_not_abstract():
    assert not inspect.isabstract(OclModel)


def test_oclmodel_constructor_exists():
    assert callable(OclModel.__init__)


def test_oclmodel_constructor_args():
    sig = inspect.signature(OclModel.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::oclmetamodel_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OclMetamodel)


def test_qualitymetamodel::qmm::ocl::oclmetamodel_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OclMetamodel.__init__)


def test_qualitymetamodel::qmm::ocl::oclmetamodel_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OclMetamodel.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_qualitymetamodel::qmm::ocl::oclmetamodel_has_uri():
    assert hasattr(QualityMetamodel::QMM::OCL::OclMetamodel, "uri")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::OclMetamodel.__mro__:
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



def test_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OclContextDefinition)


def test_oclcontextdefinition_constructor_exists():
    assert callable(OclContextDefinition.__init__)


def test_oclcontextdefinition_constructor_args():
    sig = inspect.signature(OclContextDefinition.__init__)
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



def test_propertycall_is_not_abstract():
    assert not inspect.isabstract(PropertyCall)


def test_propertycall_constructor_exists():
    assert callable(PropertyCall.__init__)


def test_propertycall_constructor_args():
    sig = inspect.signature(PropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::LoopExp)


def test_qualitymetamodel::qmm::ocl::loopexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::LoopExp.__init__)


def test_qualitymetamodel::qmm::ocl::loopexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_variableexp_is_not_abstract():
    assert not inspect.isabstract(VariableExp)


def test_variableexp_constructor_exists():
    assert callable(VariableExp.__init__)


def test_variableexp_constructor_args():
    sig = inspect.signature(VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::lambdacallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::LambdaCallExp)


def test_qualitymetamodel::qmm::ocl::lambdacallexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::LambdaCallExp.__init__)


def test_qualitymetamodel::qmm::ocl::lambdacallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::LambdaCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::operationcall_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OperationCall)


def test_qualitymetamodel::qmm::ocl::operationcall_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OperationCall.__init__)


def test_qualitymetamodel::qmm::ocl::operationcall_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_qualitymetamodel::qmm::ocl::operationcall_has_operationName():
    assert hasattr(QualityMetamodel::QMM::OCL::OperationCall, "operationName")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::OperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qmm::ocl::navigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::NavigationOrAttributeCall)


def test_qualitymetamodel::qmm::ocl::navigationorattributecall_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::NavigationOrAttributeCall.__init__)


def test_qualitymetamodel::qmm::ocl::navigationorattributecall_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::NavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel::qmm::ocl::navigationorattributecall_has_name():
    assert hasattr(QualityMetamodel::QMM::OCL::NavigationOrAttributeCall, "name")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::NavigationOrAttributeCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mapexp_is_not_abstract():
    assert not inspect.isabstract(MapExp)


def test_mapexp_constructor_exists():
    assert callable(MapExp.__init__)


def test_mapexp_constructor_args():
    sig = inspect.signature(MapExp.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::operation_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::Operation)


def test_qualitymetamodel::qmm::ocl::operation_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::Operation.__init__)


def test_qualitymetamodel::qmm::ocl::operation_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::Operation.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::oclinstancemodel_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OclInstanceModel)


def test_qualitymetamodel::qmm::ocl::oclinstancemodel_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OclInstanceModel.__init__)


def test_qualitymetamodel::qmm::ocl::oclinstancemodel_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OclInstanceModel.__init__)
    params = list(sig.parameters.keys())



def test_mapelement_is_not_abstract():
    assert not inspect.isabstract(MapElement)


def test_mapelement_constructor_exists():
    assert callable(MapElement.__init__)


def test_mapelement_constructor_args():
    sig = inspect.signature(MapElement.__init__)
    params = list(sig.parameters.keys())



def test_tupleexp_is_not_abstract():
    assert not inspect.isabstract(TupleExp)


def test_tupleexp_constructor_exists():
    assert callable(TupleExp.__init__)


def test_tupleexp_constructor_args():
    sig = inspect.signature(TupleExp.__init__)
    params = list(sig.parameters.keys())



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



def test_qualitymetamodel::qmm::ocl::staticnavigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::StaticNavigationOrAttributeCall)


def test_qualitymetamodel::qmm::ocl::staticnavigationorattributecall_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::StaticNavigationOrAttributeCall.__init__)


def test_qualitymetamodel::qmm::ocl::staticnavigationorattributecall_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::StaticNavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel::qmm::ocl::staticnavigationorattributecall_has_name():
    assert hasattr(QualityMetamodel::QMM::OCL::StaticNavigationOrAttributeCall, "name")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::StaticNavigationOrAttributeCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qmm::ocl::staticoperationcall_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::StaticOperationCall)


def test_qualitymetamodel::qmm::ocl::staticoperationcall_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::StaticOperationCall.__init__)


def test_qualitymetamodel::qmm::ocl::staticoperationcall_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::StaticOperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_qualitymetamodel::qmm::ocl::staticoperationcall_has_operationName():
    assert hasattr(QualityMetamodel::QMM::OCL::StaticOperationCall, "operationName")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::StaticOperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::integerexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::IntegerExp)


def test_qualitymetamodel::qmm::ocl::integerexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::IntegerExp.__init__)


def test_qualitymetamodel::qmm::ocl::integerexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_qualitymetamodel::qmm::ocl::integerexp_has_integerSymbol():
    assert hasattr(QualityMetamodel::QMM::OCL::IntegerExp, "integerSymbol")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qmm::ocl::realexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::RealExp)


def test_qualitymetamodel::qmm::ocl::realexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::RealExp.__init__)


def test_qualitymetamodel::qmm::ocl::realexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_qualitymetamodel::qmm::ocl::realexp_has_realSymbol():
    assert hasattr(QualityMetamodel::QMM::OCL::RealExp, "realSymbol")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::RealExp.__mro__:
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



def test_qualitymetamodel::qmm::ocl::numericexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::NumericExp)


def test_qualitymetamodel::qmm::ocl::numericexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::NumericExp.__init__)


def test_qualitymetamodel::qmm::ocl::numericexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::booleanexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::BooleanExp)


def test_qualitymetamodel::qmm::ocl::booleanexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::BooleanExp.__init__)


def test_qualitymetamodel::qmm::ocl::booleanexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_qualitymetamodel::qmm::ocl::booleanexp_has_booleanSymbol():
    assert hasattr(QualityMetamodel::QMM::OCL::BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qmm::ocl::stringexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::StringExp)


def test_qualitymetamodel::qmm::ocl::stringexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::StringExp.__init__)


def test_qualitymetamodel::qmm::ocl::stringexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_qualitymetamodel::qmm::ocl::stringexp_has_stringSymbol():
    assert hasattr(QualityMetamodel::QMM::OCL::StringExp, "stringSymbol")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::StringExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



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



def test_qualitymetamodel::qmm::ocl::orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OrderedSetExp)


def test_qualitymetamodel::qmm::ocl::orderedsetexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OrderedSetExp.__init__)


def test_qualitymetamodel::qmm::ocl::orderedsetexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::bagexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::BagExp)


def test_qualitymetamodel::qmm::ocl::bagexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::BagExp.__init__)


def test_qualitymetamodel::qmm::ocl::bagexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::BagExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::sequenceexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::SequenceExp)


def test_qualitymetamodel::qmm::ocl::sequenceexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::SequenceExp.__init__)


def test_qualitymetamodel::qmm::ocl::sequenceexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::setexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::SetExp)


def test_qualitymetamodel::qmm::ocl::setexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::SetExp.__init__)


def test_qualitymetamodel::qmm::ocl::setexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::SetExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionpart_is_not_abstract():
    assert not inspect.isabstract(CollectionPart)


def test_collectionpart_constructor_exists():
    assert callable(CollectionPart.__init__)


def test_collectionpart_constructor_args():
    sig = inspect.signature(CollectionPart.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::collectionrange_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::CollectionRange)


def test_qualitymetamodel::qmm::ocl::collectionrange_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::CollectionRange.__init__)


def test_qualitymetamodel::qmm::ocl::collectionrange_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::collectionitem_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::CollectionItem)


def test_qualitymetamodel::qmm::ocl::collectionitem_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::CollectionItem.__init__)


def test_qualitymetamodel::qmm::ocl::collectionitem_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_localvariable_is_not_abstract():
    assert not inspect.isabstract(LocalVariable)


def test_localvariable_constructor_exists():
    assert callable(LocalVariable.__init__)


def test_localvariable_constructor_args():
    sig = inspect.signature(LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::tuplepart_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::TuplePart)


def test_qualitymetamodel::qmm::ocl::tuplepart_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::TuplePart.__init__)


def test_qualitymetamodel::qmm::ocl::tuplepart_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OperatorCallExp)


def test_operatorcallexp_constructor_exists():
    assert callable(OperatorCallExp.__init__)


def test_operatorcallexp_constructor_args():
    sig = inspect.signature(OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::eqopcallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::EqOpCallExp)


def test_qualitymetamodel::qmm::ocl::eqopcallexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::EqOpCallExp.__init__)


def test_qualitymetamodel::qmm::ocl::eqopcallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::EqOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::intopcallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::IntOpCallExp)


def test_qualitymetamodel::qmm::ocl::intopcallexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::IntOpCallExp.__init__)


def test_qualitymetamodel::qmm::ocl::intopcallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::IntOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::notopcallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::NotOpCallExp)


def test_qualitymetamodel::qmm::ocl::notopcallexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::NotOpCallExp.__init__)


def test_qualitymetamodel::qmm::ocl::notopcallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::NotOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::addopcallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::AddOpCallExp)


def test_qualitymetamodel::qmm::ocl::addopcallexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::AddOpCallExp.__init__)


def test_qualitymetamodel::qmm::ocl::addopcallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::AddOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::relopcallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::RelOpCallExp)


def test_qualitymetamodel::qmm::ocl::relopcallexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::RelOpCallExp.__init__)


def test_qualitymetamodel::qmm::ocl::relopcallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::RelOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::mulopcallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::MulOpCallExp)


def test_qualitymetamodel::qmm::ocl::mulopcallexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::MulOpCallExp.__init__)


def test_qualitymetamodel::qmm::ocl::mulopcallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::MulOpCallExp.__init__)
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



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OclFeatureDefinition)


def test_qualitymetamodel::qmm::ocl::oclfeaturedefinition_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OclFeatureDefinition.__init__)


def test_qualitymetamodel::qmm::ocl::oclfeaturedefinition_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_qualitymetamodel::qmm::ocl::oclfeaturedefinition_has_static():
    assert hasattr(QualityMetamodel::QMM::OCL::OclFeatureDefinition, "static")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::OclFeatureDefinition.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_operationcall_is_not_abstract():
    assert not inspect.isabstract(OperationCall)


def test_operationcall_constructor_exists():
    assert callable(OperationCall.__init__)


def test_operationcall_constructor_args():
    sig = inspect.signature(OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::collectionoperationcall_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::CollectionOperationCall)


def test_qualitymetamodel::qmm::ocl::collectionoperationcall_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::CollectionOperationCall.__init__)


def test_qualitymetamodel::qmm::ocl::collectionoperationcall_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::CollectionOperationCall.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::IteratorExp)


def test_qualitymetamodel::qmm::ocl::iteratorexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::IteratorExp.__init__)


def test_qualitymetamodel::qmm::ocl::iteratorexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel::qmm::ocl::iteratorexp_has_name():
    assert hasattr(QualityMetamodel::QMM::OCL::IteratorExp, "name")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qmm::ocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::IterateExp)


def test_qualitymetamodel::qmm::ocl::iterateexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::IterateExp.__init__)


def test_qualitymetamodel::qmm::ocl::iterateexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::IterateExp.__init__)
    params = list(sig.parameters.keys())



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



def test_qualitymetamodel::qmm::ocl::primitive_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::Primitive)


def test_qualitymetamodel::qmm::ocl::primitive_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::Primitive.__init__)


def test_qualitymetamodel::qmm::ocl::primitive_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::envtype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::EnvType)


def test_qualitymetamodel::qmm::ocl::envtype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::EnvType.__init__)


def test_qualitymetamodel::qmm::ocl::envtype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::EnvType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::TupleType)


def test_qualitymetamodel::qmm::ocl::tupletype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::TupleType.__init__)


def test_qualitymetamodel::qmm::ocl::tupletype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OclModelElement)


def test_qualitymetamodel::qmm::ocl::oclmodelelement_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OclModelElement.__init__)


def test_qualitymetamodel::qmm::ocl::oclmodelelement_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::oclanytype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OclAnyType)


def test_qualitymetamodel::qmm::ocl::oclanytype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OclAnyType.__init__)


def test_qualitymetamodel::qmm::ocl::oclanytype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::CollectionType)


def test_qualitymetamodel::qmm::ocl::collectiontype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::CollectionType.__init__)


def test_qualitymetamodel::qmm::ocl::collectiontype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::maptype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::MapType)


def test_qualitymetamodel::qmm::ocl::maptype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::MapType.__init__)


def test_qualitymetamodel::qmm::ocl::maptype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::MapType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::lambdatype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::LambdaType)


def test_qualitymetamodel::qmm::ocl::lambdatype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::LambdaType.__init__)


def test_qualitymetamodel::qmm::ocl::lambdatype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::LambdaType.__init__)
    params = list(sig.parameters.keys())



def test_valuetype_is_not_abstract():
    assert not inspect.isabstract(ValueType)


def test_valuetype_constructor_exists():
    assert callable(ValueType.__init__)


def test_valuetype_constructor_args():
    sig = inspect.signature(ValueType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::rangevaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::RangeValueType)


def test_qualitymetamodel::rangevaluetype_constructor_exists():
    assert callable(QualityMetamodel::RangeValueType.__init__)


def test_qualitymetamodel::rangevaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel::RangeValueType.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_qualitymetamodel::rangevaluetype_has_min():
    assert hasattr(QualityMetamodel::RangeValueType, "min")
    descriptor = None
    for klass in QualityMetamodel::RangeValueType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::rangevaluetype_has_max():
    assert hasattr(QualityMetamodel::RangeValueType, "max")
    descriptor = None
    for klass in QualityMetamodel::RangeValueType.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::aggregatedvaluemetric_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::AggregatedValueMetric)


def test_qualitymetamodel::aggregatedvaluemetric_constructor_exists():
    assert callable(QualityMetamodel::AggregatedValueMetric.__init__)


def test_qualitymetamodel::aggregatedvaluemetric_constructor_args():
    sig = inspect.signature(QualityMetamodel::AggregatedValueMetric.__init__)
    params = list(sig.parameters.keys())
    assert "average" in params, "Missing parameter 'average'"
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "maximum" in params, "Missing parameter 'maximum'"
    assert "median" in params, "Missing parameter 'median'"
    assert "standardDeviation" in params, "Missing parameter 'standardDeviation'"

def test_qualitymetamodel::aggregatedvaluemetric_has_average():
    assert hasattr(QualityMetamodel::AggregatedValueMetric, "average")
    descriptor = None
    for klass in QualityMetamodel::AggregatedValueMetric.__mro__:
        if "average" in klass.__dict__:
            descriptor = klass.__dict__["average"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::aggregatedvaluemetric_has_minimum():
    assert hasattr(QualityMetamodel::AggregatedValueMetric, "minimum")
    descriptor = None
    for klass in QualityMetamodel::AggregatedValueMetric.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::aggregatedvaluemetric_has_maximum():
    assert hasattr(QualityMetamodel::AggregatedValueMetric, "maximum")
    descriptor = None
    for klass in QualityMetamodel::AggregatedValueMetric.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::aggregatedvaluemetric_has_median():
    assert hasattr(QualityMetamodel::AggregatedValueMetric, "median")
    descriptor = None
    for klass in QualityMetamodel::AggregatedValueMetric.__mro__:
        if "median" in klass.__dict__:
            descriptor = klass.__dict__["median"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::aggregatedvaluemetric_has_standardDeviation():
    assert hasattr(QualityMetamodel::AggregatedValueMetric, "standardDeviation")
    descriptor = None
    for klass in QualityMetamodel::AggregatedValueMetric.__mro__:
        if "standardDeviation" in klass.__dict__:
            descriptor = klass.__dict__["standardDeviation"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::textvaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::TextValueType)


def test_qualitymetamodel::textvaluetype_constructor_exists():
    assert callable(QualityMetamodel::TextValueType.__init__)


def test_qualitymetamodel::textvaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel::TextValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel::textvaluetype_has_value():
    assert hasattr(QualityMetamodel::TextValueType, "value")
    descriptor = None
    for klass in QualityMetamodel::TextValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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



def test_qualitymetamodel::qmm::ocl::import_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::Import)


def test_qualitymetamodel::qmm::ocl::import_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::Import.__init__)


def test_qualitymetamodel::qmm::ocl::import_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::Import.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::oclfeature_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OclFeature)


def test_qualitymetamodel::qmm::ocl::oclfeature_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OclFeature.__init__)


def test_qualitymetamodel::qmm::ocl::oclfeature_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OclFeature.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_qualitymetamodel::qmm::ocl::oclfeature_has_eq():
    assert hasattr(QualityMetamodel::QMM::OCL::OclFeature, "eq")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::OclFeature.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qmm::ocl::oclmodel_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OclModel)


def test_qualitymetamodel::qmm::ocl::oclmodel_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OclModel.__init__)


def test_qualitymetamodel::qmm::ocl::oclmodel_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OclModel.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::module_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::Module)


def test_qualitymetamodel::qmm::ocl::module_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::Module.__init__)


def test_qualitymetamodel::qmm::ocl::module_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::Module.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::mapelement_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::MapElement)


def test_qualitymetamodel::qmm::ocl::mapelement_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::MapElement.__init__)


def test_qualitymetamodel::qmm::ocl::mapelement_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::MapElement.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::VariableDeclaration)


def test_qualitymetamodel::qmm::ocl::variabledeclaration_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::VariableDeclaration.__init__)


def test_qualitymetamodel::qmm::ocl::variabledeclaration_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_qualitymetamodel::qmm::ocl::variabledeclaration_has_varName():
    assert hasattr(QualityMetamodel::QMM::OCL::VariableDeclaration, "varName")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qmm::ocl::ocltype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OclType)


def test_qualitymetamodel::qmm::ocl::ocltype_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OclType.__init__)


def test_qualitymetamodel::qmm::ocl::ocltype_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel::qmm::ocl::ocltype_has_name():
    assert hasattr(QualityMetamodel::QMM::OCL::OclType, "name")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qmm::ocl::collectionpart_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::CollectionPart)


def test_qualitymetamodel::qmm::ocl::collectionpart_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::CollectionPart.__init__)


def test_qualitymetamodel::qmm::ocl::collectionpart_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::CollectionPart.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OclContextDefinition)


def test_qualitymetamodel::qmm::ocl::oclcontextdefinition_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OclContextDefinition.__init__)


def test_qualitymetamodel::qmm::ocl::oclcontextdefinition_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::moduleelement_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::ModuleElement)


def test_qualitymetamodel::qmm::ocl::moduleelement_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::ModuleElement.__init__)


def test_qualitymetamodel::qmm::ocl::moduleelement_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OclExpression)


def test_qualitymetamodel::qmm::ocl::oclexpression_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OclExpression.__init__)


def test_qualitymetamodel::qmm::ocl::oclexpression_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::TupleTypeAttribute)


def test_qualitymetamodel::qmm::ocl::tupletypeattribute_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::TupleTypeAttribute.__init__)


def test_qualitymetamodel::qmm::ocl::tupletypeattribute_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel::qmm::ocl::tupletypeattribute_has_name():
    assert hasattr(QualityMetamodel::QMM::OCL::TupleTypeAttribute, "name")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qmm::ocl::staticpropertycall_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::StaticPropertyCall)


def test_qualitymetamodel::qmm::ocl::staticpropertycall_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::StaticPropertyCall.__init__)


def test_qualitymetamodel::qmm::ocl::staticpropertycall_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::StaticPropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::propertycall_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::PropertyCall)


def test_qualitymetamodel::qmm::ocl::propertycall_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::PropertyCall.__init__)


def test_qualitymetamodel::qmm::ocl::propertycall_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::PropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::namedelement_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::NamedElement)


def test_qualitymetamodel::qmm::ocl::namedelement_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::NamedElement.__init__)


def test_qualitymetamodel::qmm::ocl::namedelement_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel::qmm::ocl::namedelement_has_name():
    assert hasattr(QualityMetamodel::QMM::OCL::NamedElement, "name")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qmm::ocl::locatedelement_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::LocatedElement)


def test_qualitymetamodel::qmm::ocl::locatedelement_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::LocatedElement.__init__)


def test_qualitymetamodel::qmm::ocl::locatedelement_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "line" in params, "Missing parameter 'line'"
    assert "charEnd" in params, "Missing parameter 'charEnd'"
    assert "column" in params, "Missing parameter 'column'"
    assert "charStart" in params, "Missing parameter 'charStart'"

def test_qualitymetamodel::qmm::ocl::locatedelement_has_line():
    assert hasattr(QualityMetamodel::QMM::OCL::LocatedElement, "line")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::LocatedElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::qmm::ocl::locatedelement_has_charEnd():
    assert hasattr(QualityMetamodel::QMM::OCL::LocatedElement, "charEnd")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::LocatedElement.__mro__:
        if "charEnd" in klass.__dict__:
            descriptor = klass.__dict__["charEnd"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::qmm::ocl::locatedelement_has_column():
    assert hasattr(QualityMetamodel::QMM::OCL::LocatedElement, "column")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::LocatedElement.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::qmm::ocl::locatedelement_has_charStart():
    assert hasattr(QualityMetamodel::QMM::OCL::LocatedElement, "charStart")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::LocatedElement.__mro__:
        if "charStart" in klass.__dict__:
            descriptor = klass.__dict__["charStart"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::listvalue_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::ListValue)


def test_qualitymetamodel::listvalue_constructor_exists():
    assert callable(QualityMetamodel::ListValue.__init__)


def test_qualitymetamodel::listvalue_constructor_args():
    sig = inspect.signature(QualityMetamodel::ListValue.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::integervaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::IntegerValueType)


def test_qualitymetamodel::integervaluetype_constructor_exists():
    assert callable(QualityMetamodel::IntegerValueType.__init__)


def test_qualitymetamodel::integervaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel::IntegerValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel::integervaluetype_has_value():
    assert hasattr(QualityMetamodel::IntegerValueType, "value")
    descriptor = None
    for klass in QualityMetamodel::IntegerValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::booleanvaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::BooleanValueType)


def test_qualitymetamodel::booleanvaluetype_constructor_exists():
    assert callable(QualityMetamodel::BooleanValueType.__init__)


def test_qualitymetamodel::booleanvaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel::BooleanValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel::booleanvaluetype_has_value():
    assert hasattr(QualityMetamodel::BooleanValueType, "value")
    descriptor = None
    for klass in QualityMetamodel::BooleanValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::realvaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::RealValueType)


def test_qualitymetamodel::realvaluetype_constructor_exists():
    assert callable(QualityMetamodel::RealValueType.__init__)


def test_qualitymetamodel::realvaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel::RealValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel::realvaluetype_has_value():
    assert hasattr(QualityMetamodel::RealValueType, "value")
    descriptor = None
    for klass in QualityMetamodel::RealValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::enumerationitem_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::EnumerationItem)


def test_qualitymetamodel::enumerationitem_constructor_exists():
    assert callable(QualityMetamodel::EnumerationItem.__init__)


def test_qualitymetamodel::enumerationitem_constructor_args():
    sig = inspect.signature(QualityMetamodel::EnumerationItem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel::enumerationitem_has_name():
    assert hasattr(QualityMetamodel::EnumerationItem, "name")
    descriptor = None
    for klass in QualityMetamodel::EnumerationItem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::enumerationmetric_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::EnumerationMetric)


def test_qualitymetamodel::enumerationmetric_constructor_exists():
    assert callable(QualityMetamodel::EnumerationMetric.__init__)


def test_qualitymetamodel::enumerationmetric_constructor_args():
    sig = inspect.signature(QualityMetamodel::EnumerationMetric.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::metricprovider_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::MetricProvider)


def test_qualitymetamodel::metricprovider_constructor_exists():
    assert callable(QualityMetamodel::MetricProvider.__init__)


def test_qualitymetamodel::metricprovider_constructor_args():
    sig = inspect.signature(QualityMetamodel::MetricProvider.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"

def test_qualitymetamodel::metricprovider_has_name():
    assert hasattr(QualityMetamodel::MetricProvider, "name")
    descriptor = None
    for klass in QualityMetamodel::MetricProvider.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::metricprovider_has_id():
    assert hasattr(QualityMetamodel::MetricProvider, "id")
    descriptor = None
    for klass in QualityMetamodel::MetricProvider.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::metricprovider_has_description():
    assert hasattr(QualityMetamodel::MetricProvider, "description")
    descriptor = None
    for klass in QualityMetamodel::MetricProvider.__mro__:
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



def test_qualitymetamodel::qualitymodel_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QualityModel)


def test_qualitymetamodel::qualitymodel_constructor_exists():
    assert callable(QualityMetamodel::QualityModel.__init__)


def test_qualitymetamodel::qualitymodel_constructor_args():
    sig = inspect.signature(QualityMetamodel::QualityModel.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::tupleexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::TupleExp)


def test_qualitymetamodel::qmm::ocl::tupleexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::TupleExp.__init__)


def test_qualitymetamodel::qmm::ocl::tupleexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::collectionexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::CollectionExp)


def test_qualitymetamodel::qmm::ocl::collectionexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::CollectionExp.__init__)


def test_qualitymetamodel::qmm::ocl::collectionexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::braceexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::BraceExp)


def test_qualitymetamodel::qmm::ocl::braceexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::BraceExp.__init__)


def test_qualitymetamodel::qmm::ocl::braceexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::BraceExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OclUndefinedExp)


def test_qualitymetamodel::qmm::ocl::oclundefinedexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OclUndefinedExp.__init__)


def test_qualitymetamodel::qmm::ocl::oclundefinedexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::letexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::LetExp)


def test_qualitymetamodel::qmm::ocl::letexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::LetExp.__init__)


def test_qualitymetamodel::qmm::ocl::letexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::EnumLiteralExp)


def test_qualitymetamodel::qmm::ocl::enumliteralexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::EnumLiteralExp.__init__)


def test_qualitymetamodel::qmm::ocl::enumliteralexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel::qmm::ocl::enumliteralexp_has_name():
    assert hasattr(QualityMetamodel::QMM::OCL::EnumLiteralExp, "name")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qmm::ocl::primitiveexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::PrimitiveExp)


def test_qualitymetamodel::qmm::ocl::primitiveexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::PrimitiveExp.__init__)


def test_qualitymetamodel::qmm::ocl::primitiveexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::IfExp)


def test_qualitymetamodel::qmm::ocl::ifexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::IfExp.__init__)


def test_qualitymetamodel::qmm::ocl::ifexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::VariableExp)


def test_qualitymetamodel::qmm::ocl::variableexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::VariableExp.__init__)


def test_qualitymetamodel::qmm::ocl::variableexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::oclmodelelementexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OclModelElementExp)


def test_qualitymetamodel::qmm::ocl::oclmodelelementexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OclModelElementExp.__init__)


def test_qualitymetamodel::qmm::ocl::oclmodelelementexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OclModelElementExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel::qmm::ocl::oclmodelelementexp_has_name():
    assert hasattr(QualityMetamodel::QMM::OCL::OclModelElementExp, "name")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::OclModelElementExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qmm::ocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::PropertyCallExp)


def test_qualitymetamodel::qmm::ocl::propertycallexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::PropertyCallExp.__init__)


def test_qualitymetamodel::qmm::ocl::propertycallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::envexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::EnvExp)


def test_qualitymetamodel::qmm::ocl::envexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::EnvExp.__init__)


def test_qualitymetamodel::qmm::ocl::envexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::EnvExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::mapexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::MapExp)


def test_qualitymetamodel::qmm::ocl::mapexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::MapExp.__init__)


def test_qualitymetamodel::qmm::ocl::mapexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::MapExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::staticpropertycallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::StaticPropertyCallExp)


def test_qualitymetamodel::qmm::ocl::staticpropertycallexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::StaticPropertyCallExp.__init__)


def test_qualitymetamodel::qmm::ocl::staticpropertycallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::StaticPropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::OperatorCallExp)


def test_qualitymetamodel::qmm::ocl::operatorcallexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::OperatorCallExp.__init__)


def test_qualitymetamodel::qmm::ocl::operatorcallexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_qualitymetamodel::qmm::ocl::operatorcallexp_has_operationName():
    assert hasattr(QualityMetamodel::QMM::OCL::OperatorCallExp, "operationName")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::OperatorCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qmm::ocl::selfexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::SelfExp)


def test_qualitymetamodel::qmm::ocl::selfexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::SelfExp.__init__)


def test_qualitymetamodel::qmm::ocl::selfexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::superexp_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::SuperExp)


def test_qualitymetamodel::qmm::ocl::superexp_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::SuperExp.__init__)


def test_qualitymetamodel::qmm::ocl::superexp_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::operation_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::Operation)


def test_qualitymetamodel::operation_constructor_exists():
    assert callable(QualityMetamodel::Operation.__init__)


def test_qualitymetamodel::operation_constructor_args():
    sig = inspect.signature(QualityMetamodel::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "body" in params, "Missing parameter 'body'"

def test_qualitymetamodel::operation_has_name():
    assert hasattr(QualityMetamodel::Operation, "name")
    descriptor = None
    for klass in QualityMetamodel::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::operation_has_body():
    assert hasattr(QualityMetamodel::Operation, "body")
    descriptor = None
    for klass in QualityMetamodel::Operation.__mro__:
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



def test_qualitymetamodel::aggregatedvalue_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::AggregatedValue)


def test_qualitymetamodel::aggregatedvalue_constructor_exists():
    assert callable(QualityMetamodel::AggregatedValue.__init__)


def test_qualitymetamodel::aggregatedvalue_constructor_args():
    sig = inspect.signature(QualityMetamodel::AggregatedValue.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::singlevalue_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::SingleValue)


def test_qualitymetamodel::singlevalue_constructor_exists():
    assert callable(QualityMetamodel::SingleValue.__init__)


def test_qualitymetamodel::singlevalue_constructor_args():
    sig = inspect.signature(QualityMetamodel::SingleValue.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::iterator_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::Iterator)


def test_qualitymetamodel::qmm::ocl::iterator_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::Iterator.__init__)


def test_qualitymetamodel::qmm::ocl::iterator_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::parameter_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::Parameter)


def test_qualitymetamodel::qmm::ocl::parameter_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::Parameter.__init__)


def test_qualitymetamodel::qmm::ocl::parameter_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::qmm::ocl::localvariable_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QMM::OCL::LocalVariable)


def test_qualitymetamodel::qmm::ocl::localvariable_constructor_exists():
    assert callable(QualityMetamodel::QMM::OCL::LocalVariable.__init__)


def test_qualitymetamodel::qmm::ocl::localvariable_constructor_args():
    sig = inspect.signature(QualityMetamodel::QMM::OCL::LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_qualitymetamodel::qmm::ocl::localvariable_has_eq():
    assert hasattr(QualityMetamodel::QMM::OCL::LocalVariable, "eq")
    descriptor = None
    for klass in QualityMetamodel::QMM::OCL::LocalVariable.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::value_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::Value)


def test_qualitymetamodel::value_constructor_exists():
    assert callable(QualityMetamodel::Value.__init__)


def test_qualitymetamodel::value_constructor_args():
    sig = inspect.signature(QualityMetamodel::Value.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_qualitymetamodel::value_has_description():
    assert hasattr(QualityMetamodel::Value, "description")
    descriptor = None
    for klass in QualityMetamodel::Value.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qualityattribute_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QualityAttribute)


def test_qualitymetamodel::qualityattribute_constructor_exists():
    assert callable(QualityMetamodel::QualityAttribute.__init__)


def test_qualitymetamodel::qualityattribute_constructor_args():
    sig = inspect.signature(QualityMetamodel::QualityAttribute.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::valuetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::ValueType)


def test_qualitymetamodel::valuetype_constructor_exists():
    assert callable(QualityMetamodel::ValueType.__init__)


def test_qualitymetamodel::valuetype_constructor_args():
    sig = inspect.signature(QualityMetamodel::ValueType.__init__)
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
OclInstanceModel_strategy = st.builds(
    OclInstanceModel,
)
OclModelElement_strategy = st.builds(
    OclModelElement,
)
TupleType_strategy = st.builds(
    TupleType,
)
OclFeatureDefinition_strategy = st.builds(
    OclFeatureDefinition,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
QualityMetamodel::QMM::OCL::Attribute_strategy = st.builds(
    QualityMetamodel::QMM::OCL::Attribute,
)
TupleTypeAttribute_strategy = st.builds(
    TupleTypeAttribute,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
MapType_strategy = st.builds(
    MapType,
)
QualityMetamodel::QMM::OCL::SetType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::SetType,
)
QualityMetamodel::QMM::OCL::SequenceType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::SequenceType,
)
QualityMetamodel::QMM::OCL::OrderedSetType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OrderedSetType,
)
QualityMetamodel::QMM::OCL::BagType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::BagType,
)
NumericType_strategy = st.builds(
    NumericType,
)
QualityMetamodel::QMM::OCL::RealType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::RealType,
)
QualityMetamodel::QMM::OCL::IntegerType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::IntegerType,
)
Primitive_strategy = st.builds(
    Primitive,
)
QualityMetamodel::QMM::OCL::BooleanType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::BooleanType,
)
QualityMetamodel::QMM::OCL::NumericType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::NumericType,
)
QualityMetamodel::QMM::OCL::StringType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::StringType,
)
OclModel_strategy = st.builds(
    OclModel,
)
QualityMetamodel::QMM::OCL::OclMetamodel_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OclMetamodel,
    uri=
        safe_text
)
LambdaType_strategy = st.builds(
    LambdaType,
)
OclContextDefinition_strategy = st.builds(
    OclContextDefinition,
)
IterateExp_strategy = st.builds(
    IterateExp,
)
Iterator_strategy = st.builds(
    Iterator,
)
PropertyCall_strategy = st.builds(
    PropertyCall,
)
QualityMetamodel::QMM::OCL::LoopExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::LoopExp,
)
VariableExp_strategy = st.builds(
    VariableExp,
)
QualityMetamodel::QMM::OCL::LambdaCallExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::LambdaCallExp,
)
QualityMetamodel::QMM::OCL::OperationCall_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OperationCall,
    operationName=
        safe_text
)
QualityMetamodel::QMM::OCL::NavigationOrAttributeCall_strategy = st.builds(
    QualityMetamodel::QMM::OCL::NavigationOrAttributeCall,
    name=
        safe_text
)
MapExp_strategy = st.builds(
    MapExp,
)
Parameter_strategy = st.builds(
    Parameter,
)
QualityMetamodel::QMM::OCL::Operation_strategy = st.builds(
    QualityMetamodel::QMM::OCL::Operation,
)
QualityMetamodel::QMM::OCL::OclInstanceModel_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OclInstanceModel,
)
MapElement_strategy = st.builds(
    MapElement,
)
TupleExp_strategy = st.builds(
    TupleExp,
)
StaticPropertyCallExp_strategy = st.builds(
    StaticPropertyCallExp,
)
StaticPropertyCall_strategy = st.builds(
    StaticPropertyCall,
)
QualityMetamodel::QMM::OCL::StaticNavigationOrAttributeCall_strategy = st.builds(
    QualityMetamodel::QMM::OCL::StaticNavigationOrAttributeCall,
    name=
        safe_text
)
QualityMetamodel::QMM::OCL::StaticOperationCall_strategy = st.builds(
    QualityMetamodel::QMM::OCL::StaticOperationCall,
    operationName=
        safe_text
)
NumericExp_strategy = st.builds(
    NumericExp,
)
QualityMetamodel::QMM::OCL::IntegerExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::IntegerExp,
    integerSymbol=
        safe_text
)
QualityMetamodel::QMM::OCL::RealExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::RealExp,
    realSymbol=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
QualityMetamodel::QMM::OCL::NumericExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::NumericExp,
)
QualityMetamodel::QMM::OCL::BooleanExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::BooleanExp,
    booleanSymbol=
        safe_text
)
QualityMetamodel::QMM::OCL::StringExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::StringExp,
    stringSymbol=
        safe_text
)
TuplePart_strategy = st.builds(
    TuplePart,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
QualityMetamodel::QMM::OCL::OrderedSetExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OrderedSetExp,
)
QualityMetamodel::QMM::OCL::BagExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::BagExp,
)
QualityMetamodel::QMM::OCL::SequenceExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::SequenceExp,
)
QualityMetamodel::QMM::OCL::SetExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::SetExp,
)
CollectionPart_strategy = st.builds(
    CollectionPart,
)
QualityMetamodel::QMM::OCL::CollectionRange_strategy = st.builds(
    QualityMetamodel::QMM::OCL::CollectionRange,
)
QualityMetamodel::QMM::OCL::CollectionItem_strategy = st.builds(
    QualityMetamodel::QMM::OCL::CollectionItem,
)
LocalVariable_strategy = st.builds(
    LocalVariable,
)
QualityMetamodel::QMM::OCL::TuplePart_strategy = st.builds(
    QualityMetamodel::QMM::OCL::TuplePart,
)
OperatorCallExp_strategy = st.builds(
    OperatorCallExp,
)
QualityMetamodel::QMM::OCL::EqOpCallExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::EqOpCallExp,
)
QualityMetamodel::QMM::OCL::IntOpCallExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::IntOpCallExp,
)
QualityMetamodel::QMM::OCL::NotOpCallExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::NotOpCallExp,
)
QualityMetamodel::QMM::OCL::AddOpCallExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::AddOpCallExp,
)
QualityMetamodel::QMM::OCL::RelOpCallExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::RelOpCallExp,
)
QualityMetamodel::QMM::OCL::MulOpCallExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::MulOpCallExp,
)
Attribute_strategy = st.builds(
    Attribute,
)
Operation_strategy = st.builds(
    Operation,
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
QualityMetamodel::QMM::OCL::OclFeatureDefinition_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OclFeatureDefinition,
    static=
        safe_text
)
OperationCall_strategy = st.builds(
    OperationCall,
)
QualityMetamodel::QMM::OCL::CollectionOperationCall_strategy = st.builds(
    QualityMetamodel::QMM::OCL::CollectionOperationCall,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
QualityMetamodel::QMM::OCL::IteratorExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::IteratorExp,
    name=
        safe_text
)
QualityMetamodel::QMM::OCL::IterateExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::IterateExp,
)
LetExp_strategy = st.builds(
    LetExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
IfExp_strategy = st.builds(
    IfExp,
)
OclType_strategy = st.builds(
    OclType,
)
QualityMetamodel::QMM::OCL::Primitive_strategy = st.builds(
    QualityMetamodel::QMM::OCL::Primitive,
)
QualityMetamodel::QMM::OCL::EnvType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::EnvType,
)
QualityMetamodel::QMM::OCL::TupleType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::TupleType,
)
QualityMetamodel::QMM::OCL::OclModelElement_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OclModelElement,
)
QualityMetamodel::QMM::OCL::OclAnyType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OclAnyType,
)
QualityMetamodel::QMM::OCL::CollectionType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::CollectionType,
)
QualityMetamodel::QMM::OCL::MapType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::MapType,
)
QualityMetamodel::QMM::OCL::LambdaType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::LambdaType,
)
ValueType_strategy = st.builds(
    ValueType,
)
QualityMetamodel::RangeValueType_strategy = st.builds(
    QualityMetamodel::RangeValueType,
    min=
        safe_text,
    max=
        safe_text
)
QualityMetamodel::AggregatedValueMetric_strategy = st.builds(
    QualityMetamodel::AggregatedValueMetric,
    average=
        safe_text,
    minimum=
        safe_text,
    maximum=
        safe_text,
    median=
        safe_text,
    standardDeviation=
        safe_text
)
QualityMetamodel::TextValueType_strategy = st.builds(
    QualityMetamodel::TextValueType,
    value=
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
QualityMetamodel::QMM::OCL::Import_strategy = st.builds(
    QualityMetamodel::QMM::OCL::Import,
)
QualityMetamodel::QMM::OCL::OclFeature_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OclFeature,
    eq=
        safe_text
)
QualityMetamodel::QMM::OCL::OclModel_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OclModel,
)
QualityMetamodel::QMM::OCL::Module_strategy = st.builds(
    QualityMetamodel::QMM::OCL::Module,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
QualityMetamodel::QMM::OCL::MapElement_strategy = st.builds(
    QualityMetamodel::QMM::OCL::MapElement,
)
QualityMetamodel::QMM::OCL::VariableDeclaration_strategy = st.builds(
    QualityMetamodel::QMM::OCL::VariableDeclaration,
    varName=
        safe_text
)
QualityMetamodel::QMM::OCL::OclType_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OclType,
    name=
        safe_text
)
QualityMetamodel::QMM::OCL::CollectionPart_strategy = st.builds(
    QualityMetamodel::QMM::OCL::CollectionPart,
)
QualityMetamodel::QMM::OCL::OclContextDefinition_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OclContextDefinition,
)
QualityMetamodel::QMM::OCL::ModuleElement_strategy = st.builds(
    QualityMetamodel::QMM::OCL::ModuleElement,
)
QualityMetamodel::QMM::OCL::OclExpression_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OclExpression,
)
QualityMetamodel::QMM::OCL::TupleTypeAttribute_strategy = st.builds(
    QualityMetamodel::QMM::OCL::TupleTypeAttribute,
    name=
        safe_text
)
QualityMetamodel::QMM::OCL::StaticPropertyCall_strategy = st.builds(
    QualityMetamodel::QMM::OCL::StaticPropertyCall,
)
QualityMetamodel::QMM::OCL::PropertyCall_strategy = st.builds(
    QualityMetamodel::QMM::OCL::PropertyCall,
)
QualityMetamodel::QMM::OCL::NamedElement_strategy = st.builds(
    QualityMetamodel::QMM::OCL::NamedElement,
    name=
        safe_text
)
QualityMetamodel::QMM::OCL::LocatedElement_strategy = st.builds(
    QualityMetamodel::QMM::OCL::LocatedElement,
    line=
        safe_text,
    charEnd=
        safe_text,
    column=
        safe_text,
    charStart=
        safe_text
)
QualityMetamodel::ListValue_strategy = st.builds(
    QualityMetamodel::ListValue,
)
QualityMetamodel::IntegerValueType_strategy = st.builds(
    QualityMetamodel::IntegerValueType,
    value=
        safe_text
)
QualityMetamodel::BooleanValueType_strategy = st.builds(
    QualityMetamodel::BooleanValueType,
    value=
        safe_text
)
QualityMetamodel::RealValueType_strategy = st.builds(
    QualityMetamodel::RealValueType,
    value=
        safe_text
)
QualityMetamodel::EnumerationItem_strategy = st.builds(
    QualityMetamodel::EnumerationItem,
    name=
        safe_text
)
QualityMetamodel::EnumerationMetric_strategy = st.builds(
    QualityMetamodel::EnumerationMetric,
)
QualityMetamodel::MetricProvider_strategy = st.builds(
    QualityMetamodel::MetricProvider,
    name=
        safe_text,
    id=
        safe_text,
    description=
        safe_text
)
Module_strategy = st.builds(
    Module,
)
QualityMetamodel::QualityModel_strategy = st.builds(
    QualityMetamodel::QualityModel,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
QualityMetamodel::QMM::OCL::TupleExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::TupleExp,
)
QualityMetamodel::QMM::OCL::CollectionExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::CollectionExp,
)
QualityMetamodel::QMM::OCL::BraceExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::BraceExp,
)
QualityMetamodel::QMM::OCL::OclUndefinedExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OclUndefinedExp,
)
QualityMetamodel::QMM::OCL::LetExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::LetExp,
)
QualityMetamodel::QMM::OCL::EnumLiteralExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::EnumLiteralExp,
    name=
        safe_text
)
QualityMetamodel::QMM::OCL::PrimitiveExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::PrimitiveExp,
)
QualityMetamodel::QMM::OCL::IfExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::IfExp,
)
QualityMetamodel::QMM::OCL::VariableExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::VariableExp,
)
QualityMetamodel::QMM::OCL::OclModelElementExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OclModelElementExp,
    name=
        safe_text
)
QualityMetamodel::QMM::OCL::PropertyCallExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::PropertyCallExp,
)
QualityMetamodel::QMM::OCL::EnvExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::EnvExp,
)
QualityMetamodel::QMM::OCL::MapExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::MapExp,
)
QualityMetamodel::QMM::OCL::StaticPropertyCallExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::StaticPropertyCallExp,
)
QualityMetamodel::QMM::OCL::OperatorCallExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::OperatorCallExp,
    operationName=
        safe_text
)
QualityMetamodel::QMM::OCL::SelfExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::SelfExp,
)
QualityMetamodel::QMM::OCL::SuperExp_strategy = st.builds(
    QualityMetamodel::QMM::OCL::SuperExp,
)
QualityMetamodel::Operation_strategy = st.builds(
    QualityMetamodel::Operation,
    name=
        safe_text,
    body=
        safe_text
)
Value_strategy = st.builds(
    Value,
)
QualityMetamodel::AggregatedValue_strategy = st.builds(
    QualityMetamodel::AggregatedValue,
)
QualityMetamodel::SingleValue_strategy = st.builds(
    QualityMetamodel::SingleValue,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
QualityMetamodel::QMM::OCL::Iterator_strategy = st.builds(
    QualityMetamodel::QMM::OCL::Iterator,
)
QualityMetamodel::QMM::OCL::Parameter_strategy = st.builds(
    QualityMetamodel::QMM::OCL::Parameter,
)
QualityMetamodel::QMM::OCL::LocalVariable_strategy = st.builds(
    QualityMetamodel::QMM::OCL::LocalVariable,
    eq=
        safe_text
)
QualityMetamodel::Value_strategy = st.builds(
    QualityMetamodel::Value,
    description=
        safe_text
)
QualityMetamodel::QualityAttribute_strategy = st.builds(
    QualityMetamodel::QualityAttribute,
)
QualityMetamodel::ValueType_strategy = st.builds(
    QualityMetamodel::ValueType,
)

@given(instance=OclInstanceModel_strategy)
@settings(max_examples=50)
def test_oclinstancemodel_instantiation(instance):
    assert isinstance(instance, OclInstanceModel)

@given(instance=OclModelElement_strategy)
@settings(max_examples=50)
def test_oclmodelelement_instantiation(instance):
    assert isinstance(instance, OclModelElement)

@given(instance=TupleType_strategy)
@settings(max_examples=50)
def test_tupletype_instantiation(instance):
    assert isinstance(instance, TupleType)

@given(instance=OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, OclFeatureDefinition)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=QualityMetamodel::QMM::OCL::Attribute_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::attribute_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::Attribute)

@given(instance=TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, TupleTypeAttribute)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=MapType_strategy)
@settings(max_examples=50)
def test_maptype_instantiation(instance):
    assert isinstance(instance, MapType)

@given(instance=QualityMetamodel::QMM::OCL::SetType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::settype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::SetType)

@given(instance=QualityMetamodel::QMM::OCL::SequenceType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::sequencetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::SequenceType)

@given(instance=QualityMetamodel::QMM::OCL::OrderedSetType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OrderedSetType)

@given(instance=QualityMetamodel::QMM::OCL::BagType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::bagtype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::BagType)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=QualityMetamodel::QMM::OCL::RealType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::realtype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::RealType)

@given(instance=QualityMetamodel::QMM::OCL::IntegerType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::integertype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::IntegerType)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=QualityMetamodel::QMM::OCL::BooleanType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::booleantype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::BooleanType)

@given(instance=QualityMetamodel::QMM::OCL::NumericType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::numerictype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::NumericType)

@given(instance=QualityMetamodel::QMM::OCL::StringType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::stringtype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::StringType)

@given(instance=OclModel_strategy)
@settings(max_examples=50)
def test_oclmodel_instantiation(instance):
    assert isinstance(instance, OclModel)

@given(instance=QualityMetamodel::QMM::OCL::OclMetamodel_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::oclmetamodel_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OclMetamodel)

@given(instance=QualityMetamodel::QMM::OCL::OclMetamodel_strategy)
def test_qualitymetamodel::qmm::ocl::oclmetamodel_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=QualityMetamodel::QMM::OCL::OclMetamodel_strategy)
def test_qualitymetamodel::qmm::ocl::oclmetamodel_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=LambdaType_strategy)
@settings(max_examples=50)
def test_lambdatype_instantiation(instance):
    assert isinstance(instance, LambdaType)

@given(instance=OclContextDefinition_strategy)
@settings(max_examples=50)
def test_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OclContextDefinition)

@given(instance=IterateExp_strategy)
@settings(max_examples=50)
def test_iterateexp_instantiation(instance):
    assert isinstance(instance, IterateExp)

@given(instance=Iterator_strategy)
@settings(max_examples=50)
def test_iterator_instantiation(instance):
    assert isinstance(instance, Iterator)

@given(instance=PropertyCall_strategy)
@settings(max_examples=50)
def test_propertycall_instantiation(instance):
    assert isinstance(instance, PropertyCall)

@given(instance=QualityMetamodel::QMM::OCL::LoopExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::loopexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::LoopExp)

@given(instance=VariableExp_strategy)
@settings(max_examples=50)
def test_variableexp_instantiation(instance):
    assert isinstance(instance, VariableExp)

@given(instance=QualityMetamodel::QMM::OCL::LambdaCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::lambdacallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::LambdaCallExp)

@given(instance=QualityMetamodel::QMM::OCL::OperationCall_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::operationcall_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OperationCall)

@given(instance=QualityMetamodel::QMM::OCL::OperationCall_strategy)
def test_qualitymetamodel::qmm::ocl::operationcall_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=QualityMetamodel::QMM::OCL::OperationCall_strategy)
def test_qualitymetamodel::qmm::ocl::operationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=QualityMetamodel::QMM::OCL::NavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::navigationorattributecall_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::NavigationOrAttributeCall)

@given(instance=QualityMetamodel::QMM::OCL::NavigationOrAttributeCall_strategy)
def test_qualitymetamodel::qmm::ocl::navigationorattributecall_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::QMM::OCL::NavigationOrAttributeCall_strategy)
def test_qualitymetamodel::qmm::ocl::navigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MapExp_strategy)
@settings(max_examples=50)
def test_mapexp_instantiation(instance):
    assert isinstance(instance, MapExp)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=QualityMetamodel::QMM::OCL::Operation_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::operation_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::Operation)

@given(instance=QualityMetamodel::QMM::OCL::OclInstanceModel_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::oclinstancemodel_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OclInstanceModel)

@given(instance=MapElement_strategy)
@settings(max_examples=50)
def test_mapelement_instantiation(instance):
    assert isinstance(instance, MapElement)

@given(instance=TupleExp_strategy)
@settings(max_examples=50)
def test_tupleexp_instantiation(instance):
    assert isinstance(instance, TupleExp)

@given(instance=StaticPropertyCallExp_strategy)
@settings(max_examples=50)
def test_staticpropertycallexp_instantiation(instance):
    assert isinstance(instance, StaticPropertyCallExp)

@given(instance=StaticPropertyCall_strategy)
@settings(max_examples=50)
def test_staticpropertycall_instantiation(instance):
    assert isinstance(instance, StaticPropertyCall)

@given(instance=QualityMetamodel::QMM::OCL::StaticNavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::staticnavigationorattributecall_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::StaticNavigationOrAttributeCall)

@given(instance=QualityMetamodel::QMM::OCL::StaticNavigationOrAttributeCall_strategy)
def test_qualitymetamodel::qmm::ocl::staticnavigationorattributecall_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::QMM::OCL::StaticNavigationOrAttributeCall_strategy)
def test_qualitymetamodel::qmm::ocl::staticnavigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::QMM::OCL::StaticOperationCall_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::staticoperationcall_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::StaticOperationCall)

@given(instance=QualityMetamodel::QMM::OCL::StaticOperationCall_strategy)
def test_qualitymetamodel::qmm::ocl::staticoperationcall_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=QualityMetamodel::QMM::OCL::StaticOperationCall_strategy)
def test_qualitymetamodel::qmm::ocl::staticoperationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=QualityMetamodel::QMM::OCL::IntegerExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::integerexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::IntegerExp)

@given(instance=QualityMetamodel::QMM::OCL::IntegerExp_strategy)
def test_qualitymetamodel::qmm::ocl::integerexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=QualityMetamodel::QMM::OCL::IntegerExp_strategy)
def test_qualitymetamodel::qmm::ocl::integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=QualityMetamodel::QMM::OCL::RealExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::realexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::RealExp)

@given(instance=QualityMetamodel::QMM::OCL::RealExp_strategy)
def test_qualitymetamodel::qmm::ocl::realexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=QualityMetamodel::QMM::OCL::RealExp_strategy)
def test_qualitymetamodel::qmm::ocl::realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=QualityMetamodel::QMM::OCL::NumericExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::numericexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::NumericExp)

@given(instance=QualityMetamodel::QMM::OCL::BooleanExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::booleanexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::BooleanExp)

@given(instance=QualityMetamodel::QMM::OCL::BooleanExp_strategy)
def test_qualitymetamodel::qmm::ocl::booleanexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=QualityMetamodel::QMM::OCL::BooleanExp_strategy)
def test_qualitymetamodel::qmm::ocl::booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=QualityMetamodel::QMM::OCL::StringExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::stringexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::StringExp)

@given(instance=QualityMetamodel::QMM::OCL::StringExp_strategy)
def test_qualitymetamodel::qmm::ocl::stringexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=QualityMetamodel::QMM::OCL::StringExp_strategy)
def test_qualitymetamodel::qmm::ocl::stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=TuplePart_strategy)
@settings(max_examples=50)
def test_tuplepart_instantiation(instance):
    assert isinstance(instance, TuplePart)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=QualityMetamodel::QMM::OCL::OrderedSetExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::orderedsetexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OrderedSetExp)

@given(instance=QualityMetamodel::QMM::OCL::BagExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::bagexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::BagExp)

@given(instance=QualityMetamodel::QMM::OCL::SequenceExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::sequenceexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::SequenceExp)

@given(instance=QualityMetamodel::QMM::OCL::SetExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::setexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::SetExp)

@given(instance=CollectionPart_strategy)
@settings(max_examples=50)
def test_collectionpart_instantiation(instance):
    assert isinstance(instance, CollectionPart)

@given(instance=QualityMetamodel::QMM::OCL::CollectionRange_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::collectionrange_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::CollectionRange)

@given(instance=QualityMetamodel::QMM::OCL::CollectionItem_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::collectionitem_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::CollectionItem)

@given(instance=LocalVariable_strategy)
@settings(max_examples=50)
def test_localvariable_instantiation(instance):
    assert isinstance(instance, LocalVariable)

@given(instance=QualityMetamodel::QMM::OCL::TuplePart_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::tuplepart_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::TuplePart)

@given(instance=OperatorCallExp_strategy)
@settings(max_examples=50)
def test_operatorcallexp_instantiation(instance):
    assert isinstance(instance, OperatorCallExp)

@given(instance=QualityMetamodel::QMM::OCL::EqOpCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::eqopcallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::EqOpCallExp)

@given(instance=QualityMetamodel::QMM::OCL::IntOpCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::intopcallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::IntOpCallExp)

@given(instance=QualityMetamodel::QMM::OCL::NotOpCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::notopcallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::NotOpCallExp)

@given(instance=QualityMetamodel::QMM::OCL::AddOpCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::addopcallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::AddOpCallExp)

@given(instance=QualityMetamodel::QMM::OCL::RelOpCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::relopcallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::RelOpCallExp)

@given(instance=QualityMetamodel::QMM::OCL::MulOpCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::mulopcallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::MulOpCallExp)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=QualityMetamodel::QMM::OCL::OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OclFeatureDefinition)

@given(instance=QualityMetamodel::QMM::OCL::OclFeatureDefinition_strategy)
def test_qualitymetamodel::qmm::ocl::oclfeaturedefinition_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=QualityMetamodel::QMM::OCL::OclFeatureDefinition_strategy)
def test_qualitymetamodel::qmm::ocl::oclfeaturedefinition_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=OperationCall_strategy)
@settings(max_examples=50)
def test_operationcall_instantiation(instance):
    assert isinstance(instance, OperationCall)

@given(instance=QualityMetamodel::QMM::OCL::CollectionOperationCall_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::collectionoperationcall_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::CollectionOperationCall)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=QualityMetamodel::QMM::OCL::IteratorExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::IteratorExp)

@given(instance=QualityMetamodel::QMM::OCL::IteratorExp_strategy)
def test_qualitymetamodel::qmm::ocl::iteratorexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::QMM::OCL::IteratorExp_strategy)
def test_qualitymetamodel::qmm::ocl::iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::QMM::OCL::IterateExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::iterateexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::IterateExp)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=IfExp_strategy)
@settings(max_examples=50)
def test_ifexp_instantiation(instance):
    assert isinstance(instance, IfExp)

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=QualityMetamodel::QMM::OCL::Primitive_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::primitive_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::Primitive)

@given(instance=QualityMetamodel::QMM::OCL::EnvType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::envtype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::EnvType)

@given(instance=QualityMetamodel::QMM::OCL::TupleType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::tupletype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::TupleType)

@given(instance=QualityMetamodel::QMM::OCL::OclModelElement_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::oclmodelelement_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OclModelElement)

@given(instance=QualityMetamodel::QMM::OCL::OclAnyType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::oclanytype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OclAnyType)

@given(instance=QualityMetamodel::QMM::OCL::CollectionType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::collectiontype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::CollectionType)

@given(instance=QualityMetamodel::QMM::OCL::MapType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::maptype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::MapType)

@given(instance=QualityMetamodel::QMM::OCL::LambdaType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::lambdatype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::LambdaType)

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=QualityMetamodel::RangeValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::rangevaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::RangeValueType)

@given(instance=QualityMetamodel::RangeValueType_strategy)
def test_qualitymetamodel::rangevaluetype_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=QualityMetamodel::RangeValueType_strategy)
def test_qualitymetamodel::rangevaluetype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=QualityMetamodel::RangeValueType_strategy)
def test_qualitymetamodel::rangevaluetype_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=QualityMetamodel::RangeValueType_strategy)
def test_qualitymetamodel::rangevaluetype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::aggregatedvaluemetric_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::AggregatedValueMetric)

@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_average_type(instance):
    assert isinstance(instance.average, str)


@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_average_setter(instance):
    original = instance.average
    instance.average = original
    assert instance.average == original

@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_minimum_type(instance):
    assert isinstance(instance.minimum, str)


@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original

@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_maximum_type(instance):
    assert isinstance(instance.maximum, str)


@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original

@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_median_type(instance):
    assert isinstance(instance.median, str)


@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_median_setter(instance):
    original = instance.median
    instance.median = original
    assert instance.median == original

@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_standardDeviation_type(instance):
    assert isinstance(instance.standardDeviation, str)


@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_standardDeviation_setter(instance):
    original = instance.standardDeviation
    instance.standardDeviation = original
    assert instance.standardDeviation == original

@given(instance=QualityMetamodel::TextValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::textvaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::TextValueType)

@given(instance=QualityMetamodel::TextValueType_strategy)
def test_qualitymetamodel::textvaluetype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=QualityMetamodel::TextValueType_strategy)
def test_qualitymetamodel::textvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

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

@given(instance=QualityMetamodel::QMM::OCL::Import_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::import_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::Import)

@given(instance=QualityMetamodel::QMM::OCL::OclFeature_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::oclfeature_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OclFeature)

@given(instance=QualityMetamodel::QMM::OCL::OclFeature_strategy)
def test_qualitymetamodel::qmm::ocl::oclfeature_eq_type(instance):
    assert isinstance(instance.eq, str)


@given(instance=QualityMetamodel::QMM::OCL::OclFeature_strategy)
def test_qualitymetamodel::qmm::ocl::oclfeature_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=QualityMetamodel::QMM::OCL::OclModel_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::oclmodel_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OclModel)

@given(instance=QualityMetamodel::QMM::OCL::Module_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::module_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::Module)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=QualityMetamodel::QMM::OCL::MapElement_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::mapelement_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::MapElement)

@given(instance=QualityMetamodel::QMM::OCL::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::variabledeclaration_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::VariableDeclaration)

@given(instance=QualityMetamodel::QMM::OCL::VariableDeclaration_strategy)
def test_qualitymetamodel::qmm::ocl::variabledeclaration_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=QualityMetamodel::QMM::OCL::VariableDeclaration_strategy)
def test_qualitymetamodel::qmm::ocl::variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=QualityMetamodel::QMM::OCL::OclType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::ocltype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OclType)

@given(instance=QualityMetamodel::QMM::OCL::OclType_strategy)
def test_qualitymetamodel::qmm::ocl::ocltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::QMM::OCL::OclType_strategy)
def test_qualitymetamodel::qmm::ocl::ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::QMM::OCL::CollectionPart_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::collectionpart_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::CollectionPart)

@given(instance=QualityMetamodel::QMM::OCL::OclContextDefinition_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OclContextDefinition)

@given(instance=QualityMetamodel::QMM::OCL::ModuleElement_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::moduleelement_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::ModuleElement)

@given(instance=QualityMetamodel::QMM::OCL::OclExpression_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::oclexpression_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OclExpression)

@given(instance=QualityMetamodel::QMM::OCL::TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::tupletypeattribute_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::TupleTypeAttribute)

@given(instance=QualityMetamodel::QMM::OCL::TupleTypeAttribute_strategy)
def test_qualitymetamodel::qmm::ocl::tupletypeattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::QMM::OCL::TupleTypeAttribute_strategy)
def test_qualitymetamodel::qmm::ocl::tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::QMM::OCL::StaticPropertyCall_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::staticpropertycall_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::StaticPropertyCall)

@given(instance=QualityMetamodel::QMM::OCL::PropertyCall_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::propertycall_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::PropertyCall)

@given(instance=QualityMetamodel::QMM::OCL::NamedElement_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::namedelement_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::NamedElement)

@given(instance=QualityMetamodel::QMM::OCL::NamedElement_strategy)
def test_qualitymetamodel::qmm::ocl::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::QMM::OCL::NamedElement_strategy)
def test_qualitymetamodel::qmm::ocl::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::QMM::OCL::LocatedElement_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::locatedelement_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::LocatedElement)

@given(instance=QualityMetamodel::QMM::OCL::LocatedElement_strategy)
def test_qualitymetamodel::qmm::ocl::locatedelement_line_type(instance):
    assert isinstance(instance.line, str)


@given(instance=QualityMetamodel::QMM::OCL::LocatedElement_strategy)
def test_qualitymetamodel::qmm::ocl::locatedelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=QualityMetamodel::QMM::OCL::LocatedElement_strategy)
def test_qualitymetamodel::qmm::ocl::locatedelement_charEnd_type(instance):
    assert isinstance(instance.charEnd, str)


@given(instance=QualityMetamodel::QMM::OCL::LocatedElement_strategy)
def test_qualitymetamodel::qmm::ocl::locatedelement_charEnd_setter(instance):
    original = instance.charEnd
    instance.charEnd = original
    assert instance.charEnd == original

@given(instance=QualityMetamodel::QMM::OCL::LocatedElement_strategy)
def test_qualitymetamodel::qmm::ocl::locatedelement_column_type(instance):
    assert isinstance(instance.column, str)


@given(instance=QualityMetamodel::QMM::OCL::LocatedElement_strategy)
def test_qualitymetamodel::qmm::ocl::locatedelement_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=QualityMetamodel::QMM::OCL::LocatedElement_strategy)
def test_qualitymetamodel::qmm::ocl::locatedelement_charStart_type(instance):
    assert isinstance(instance.charStart, str)


@given(instance=QualityMetamodel::QMM::OCL::LocatedElement_strategy)
def test_qualitymetamodel::qmm::ocl::locatedelement_charStart_setter(instance):
    original = instance.charStart
    instance.charStart = original
    assert instance.charStart == original

@given(instance=QualityMetamodel::ListValue_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::listvalue_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::ListValue)

@given(instance=QualityMetamodel::IntegerValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::integervaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::IntegerValueType)

@given(instance=QualityMetamodel::IntegerValueType_strategy)
def test_qualitymetamodel::integervaluetype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=QualityMetamodel::IntegerValueType_strategy)
def test_qualitymetamodel::integervaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=QualityMetamodel::BooleanValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::booleanvaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::BooleanValueType)

@given(instance=QualityMetamodel::BooleanValueType_strategy)
def test_qualitymetamodel::booleanvaluetype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=QualityMetamodel::BooleanValueType_strategy)
def test_qualitymetamodel::booleanvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=QualityMetamodel::RealValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::realvaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::RealValueType)

@given(instance=QualityMetamodel::RealValueType_strategy)
def test_qualitymetamodel::realvaluetype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=QualityMetamodel::RealValueType_strategy)
def test_qualitymetamodel::realvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=QualityMetamodel::EnumerationItem_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::enumerationitem_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::EnumerationItem)

@given(instance=QualityMetamodel::EnumerationItem_strategy)
def test_qualitymetamodel::enumerationitem_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::EnumerationItem_strategy)
def test_qualitymetamodel::enumerationitem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::EnumerationMetric_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::enumerationmetric_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::EnumerationMetric)

@given(instance=QualityMetamodel::MetricProvider_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::metricprovider_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::MetricProvider)

@given(instance=QualityMetamodel::MetricProvider_strategy)
def test_qualitymetamodel::metricprovider_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::MetricProvider_strategy)
def test_qualitymetamodel::metricprovider_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::MetricProvider_strategy)
def test_qualitymetamodel::metricprovider_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=QualityMetamodel::MetricProvider_strategy)
def test_qualitymetamodel::metricprovider_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=QualityMetamodel::MetricProvider_strategy)
def test_qualitymetamodel::metricprovider_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=QualityMetamodel::MetricProvider_strategy)
def test_qualitymetamodel::metricprovider_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=QualityMetamodel::QualityModel_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qualitymodel_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QualityModel)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=QualityMetamodel::QMM::OCL::TupleExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::tupleexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::TupleExp)

@given(instance=QualityMetamodel::QMM::OCL::CollectionExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::collectionexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::CollectionExp)

@given(instance=QualityMetamodel::QMM::OCL::BraceExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::braceexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::BraceExp)

@given(instance=QualityMetamodel::QMM::OCL::OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::oclundefinedexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OclUndefinedExp)

@given(instance=QualityMetamodel::QMM::OCL::LetExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::letexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::LetExp)

@given(instance=QualityMetamodel::QMM::OCL::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::EnumLiteralExp)

@given(instance=QualityMetamodel::QMM::OCL::EnumLiteralExp_strategy)
def test_qualitymetamodel::qmm::ocl::enumliteralexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::QMM::OCL::EnumLiteralExp_strategy)
def test_qualitymetamodel::qmm::ocl::enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::QMM::OCL::PrimitiveExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::primitiveexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::PrimitiveExp)

@given(instance=QualityMetamodel::QMM::OCL::IfExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::ifexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::IfExp)

@given(instance=QualityMetamodel::QMM::OCL::VariableExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::variableexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::VariableExp)

@given(instance=QualityMetamodel::QMM::OCL::OclModelElementExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::oclmodelelementexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OclModelElementExp)

@given(instance=QualityMetamodel::QMM::OCL::OclModelElementExp_strategy)
def test_qualitymetamodel::qmm::ocl::oclmodelelementexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::QMM::OCL::OclModelElementExp_strategy)
def test_qualitymetamodel::qmm::ocl::oclmodelelementexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::QMM::OCL::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::PropertyCallExp)

@given(instance=QualityMetamodel::QMM::OCL::EnvExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::envexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::EnvExp)

@given(instance=QualityMetamodel::QMM::OCL::MapExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::mapexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::MapExp)

@given(instance=QualityMetamodel::QMM::OCL::StaticPropertyCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::staticpropertycallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::StaticPropertyCallExp)

@given(instance=QualityMetamodel::QMM::OCL::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::operatorcallexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::OperatorCallExp)

@given(instance=QualityMetamodel::QMM::OCL::OperatorCallExp_strategy)
def test_qualitymetamodel::qmm::ocl::operatorcallexp_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=QualityMetamodel::QMM::OCL::OperatorCallExp_strategy)
def test_qualitymetamodel::qmm::ocl::operatorcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=QualityMetamodel::QMM::OCL::SelfExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::selfexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::SelfExp)

@given(instance=QualityMetamodel::QMM::OCL::SuperExp_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::superexp_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::SuperExp)

@given(instance=QualityMetamodel::Operation_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::operation_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::Operation)

@given(instance=QualityMetamodel::Operation_strategy)
def test_qualitymetamodel::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::Operation_strategy)
def test_qualitymetamodel::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::Operation_strategy)
def test_qualitymetamodel::operation_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=QualityMetamodel::Operation_strategy)
def test_qualitymetamodel::operation_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=QualityMetamodel::AggregatedValue_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::aggregatedvalue_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::AggregatedValue)

@given(instance=QualityMetamodel::SingleValue_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::singlevalue_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::SingleValue)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=QualityMetamodel::QMM::OCL::Iterator_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::iterator_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::Iterator)

@given(instance=QualityMetamodel::QMM::OCL::Parameter_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::parameter_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::Parameter)

@given(instance=QualityMetamodel::QMM::OCL::LocalVariable_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qmm::ocl::localvariable_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QMM::OCL::LocalVariable)

@given(instance=QualityMetamodel::QMM::OCL::LocalVariable_strategy)
def test_qualitymetamodel::qmm::ocl::localvariable_eq_type(instance):
    assert isinstance(instance.eq, str)


@given(instance=QualityMetamodel::QMM::OCL::LocalVariable_strategy)
def test_qualitymetamodel::qmm::ocl::localvariable_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=QualityMetamodel::Value_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::value_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::Value)

@given(instance=QualityMetamodel::Value_strategy)
def test_qualitymetamodel::value_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=QualityMetamodel::Value_strategy)
def test_qualitymetamodel::value_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=QualityMetamodel::QualityAttribute_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qualityattribute_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QualityAttribute)

@given(instance=QualityMetamodel::ValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::valuetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::ValueType)
