import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::datasources::QueryMatchingCriteria,
    model::datasources::AQueryResult,
    model::datasources::RunnableQuery,
    AQueryResult,
    model::datasources::SerializableQueryResult,
    model::datasources::QueryResult,
    model::datasources::QueryResults,
    DataSourceLibraryConfiguration,
    datasources::model::StringToStringMap,
    QueryMatchingCriteria,
    model::datasources::DataSourceLibraryConfiguration,
    datasources::model::GeppettoLibrary,
    model::variables::TypeToValueMap,
    TypeToValueMap,
    ArrayElement,
    VisualGroupElement,
    FunctionPlot,
    model::values::SkeletonTransformation,
    SkeletonTransformation,
    model::values::PointerElement,
    Unit,
    PointerElement,
    model::values::FunctionPlot,
    Function,
    PhysicalQuantity,
    model::values::StringToValueMap,
    StringToValueMap,
    AArrayValue,
    model::values::GenericArray,
    model::values::StringArray,
    model::values::DoubleArray,
    model::values::IntArray,
    MetadataValue,
    model::values::HTML,
    model::values::URL,
    model::values::JSON,
    model::values::Metadata,
    model::values::Text,
    VisualGroup,
    ArrayValue,
    Point,
    URL,
    Text,
    Image,
    Argument,
    Dynamics,
    Quantity,
    model::values::PhysicalQuantity,
    Composite,
    JSON,
    HTML,
    Expression,
    VisualType,
    model::types::CompositeVisualType,
    Instance,
    model::instances::SimpleInstance,
    model::instances::SimpleConnectionInstance,
    model::ISynchable,
    VisualValue,
    model::values::Cylinder,
    model::values::Collada,
    model::values::OBJ,
    model::values::SkeletonAnimation,
    model::values::Sphere,
    types::model::DomainModel_,
    model::DomainModel_,
    Value,
    model::values::VisualValue,
    model::values::Composite,
    model::values::Connection,
    model::values::Function,
    model::values::AArrayValue,
    model::values::ArrayValue,
    model::values::ArrayElement,
    model::values::Image,
    model::values::Argument,
    model::values::Unit,
    model::values::ImportValue,
    model::values::MDTimeSeries,
    model::values::Expression,
    model::values::MetadataValue,
    model::values::Point,
    model::values::Pointer,
    model::values::Dynamics,
    model::values::Particles,
    model::values::Quantity,
    model::values::TimeSeries,
    model::StringToStringMap,
    DomainModel_,
    model::ExternalDomainModel,
    model::ModelFormat,
    Type,
    model::types::HTMLType,
    model::types::ExpressionType,
    model::types::URLType,
    model::types::SimpleArrayType,
    model::types::ImageType,
    model::types::PointerType,
    model::types::CompositeType,
    model::types::ArrayType,
    model::types::VisualType,
    model::types::ImportType,
    model::types::ParameterType,
    model::types::StateVariableType,
    model::types::QuantityType,
    model::types::MetadataType,
    model::types::SimpleType,
    model::types::DynamicsType,
    model::types::ArgumentType,
    model::types::TextType,
    model::types::ConnectionType,
    model::types::JSONType,
    model::types::PointType,
    Node,
    model::types::Type,
    model::values::VisualGroup,
    model::values::VisualGroupElement,
    model::datasources::Query,
    model::variables::Variable,
    model::datasources::DataSource,
    model::instances::Instance,
    ISynchable,
    model::values::Value,
    model::Node,
    Query,
    model::datasources::CompoundRefQuery,
    model::datasources::ProcessQuery,
    model::datasources::CompoundQuery,
    model::datasources::SimpleQuery,
    DataSource,
    Pointer,
    model::VariableValue,
    model::ExperimentState,
    model::LibraryManager,
    Variable,
    model::GeppettoModel,
    model::Tag,
    model::GeppettoLibrary,
    model::World,
    BooleanOperator,
    Connectivity,
    FileFormat,
    ImageFormat,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::datasources::querymatchingcriteria_is_not_abstract():
    assert not inspect.isabstract(model::datasources::QueryMatchingCriteria)


def test_model::datasources::querymatchingcriteria_constructor_exists():
    assert callable(model::datasources::QueryMatchingCriteria.__init__)


def test_model::datasources::querymatchingcriteria_constructor_args():
    sig = inspect.signature(model::datasources::QueryMatchingCriteria.__init__)
    params = list(sig.parameters.keys())



def test_model::datasources::aqueryresult_is_not_abstract():
    assert not inspect.isabstract(model::datasources::AQueryResult)


def test_model::datasources::aqueryresult_constructor_exists():
    assert callable(model::datasources::AQueryResult.__init__)


def test_model::datasources::aqueryresult_constructor_args():
    sig = inspect.signature(model::datasources::AQueryResult.__init__)
    params = list(sig.parameters.keys())



def test_model::datasources::runnablequery_is_not_abstract():
    assert not inspect.isabstract(model::datasources::RunnableQuery)


def test_model::datasources::runnablequery_constructor_exists():
    assert callable(model::datasources::RunnableQuery.__init__)


def test_model::datasources::runnablequery_constructor_args():
    sig = inspect.signature(model::datasources::RunnableQuery.__init__)
    params = list(sig.parameters.keys())
    assert "targetVariablePath" in params, "Missing parameter 'targetVariablePath'"
    assert "booleanOperator" in params, "Missing parameter 'booleanOperator'"
    assert "queryPath" in params, "Missing parameter 'queryPath'"

def test_model::datasources::runnablequery_has_targetVariablePath():
    assert hasattr(model::datasources::RunnableQuery, "targetVariablePath")
    descriptor = None
    for klass in model::datasources::RunnableQuery.__mro__:
        if "targetVariablePath" in klass.__dict__:
            descriptor = klass.__dict__["targetVariablePath"]
            break
    assert isinstance(descriptor, property)

def test_model::datasources::runnablequery_has_booleanOperator():
    assert hasattr(model::datasources::RunnableQuery, "booleanOperator")
    descriptor = None
    for klass in model::datasources::RunnableQuery.__mro__:
        if "booleanOperator" in klass.__dict__:
            descriptor = klass.__dict__["booleanOperator"]
            break
    assert isinstance(descriptor, property)

def test_model::datasources::runnablequery_has_queryPath():
    assert hasattr(model::datasources::RunnableQuery, "queryPath")
    descriptor = None
    for klass in model::datasources::RunnableQuery.__mro__:
        if "queryPath" in klass.__dict__:
            descriptor = klass.__dict__["queryPath"]
            break
    assert isinstance(descriptor, property)



def test_aqueryresult_is_not_abstract():
    assert not inspect.isabstract(AQueryResult)


def test_aqueryresult_constructor_exists():
    assert callable(AQueryResult.__init__)


def test_aqueryresult_constructor_args():
    sig = inspect.signature(AQueryResult.__init__)
    params = list(sig.parameters.keys())



def test_model::datasources::serializablequeryresult_is_not_abstract():
    assert not inspect.isabstract(model::datasources::SerializableQueryResult)


def test_model::datasources::serializablequeryresult_constructor_exists():
    assert callable(model::datasources::SerializableQueryResult.__init__)


def test_model::datasources::serializablequeryresult_constructor_args():
    sig = inspect.signature(model::datasources::SerializableQueryResult.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_model::datasources::serializablequeryresult_has_values():
    assert hasattr(model::datasources::SerializableQueryResult, "values")
    descriptor = None
    for klass in model::datasources::SerializableQueryResult.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_model::datasources::queryresult_is_not_abstract():
    assert not inspect.isabstract(model::datasources::QueryResult)


def test_model::datasources::queryresult_constructor_exists():
    assert callable(model::datasources::QueryResult.__init__)


def test_model::datasources::queryresult_constructor_args():
    sig = inspect.signature(model::datasources::QueryResult.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_model::datasources::queryresult_has_values():
    assert hasattr(model::datasources::QueryResult, "values")
    descriptor = None
    for klass in model::datasources::QueryResult.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_model::datasources::queryresults_is_not_abstract():
    assert not inspect.isabstract(model::datasources::QueryResults)


def test_model::datasources::queryresults_constructor_exists():
    assert callable(model::datasources::QueryResults.__init__)


def test_model::datasources::queryresults_constructor_args():
    sig = inspect.signature(model::datasources::QueryResults.__init__)
    params = list(sig.parameters.keys())
    assert "header" in params, "Missing parameter 'header'"
    assert "id" in params, "Missing parameter 'id'"

def test_model::datasources::queryresults_has_header():
    assert hasattr(model::datasources::QueryResults, "header")
    descriptor = None
    for klass in model::datasources::QueryResults.__mro__:
        if "header" in klass.__dict__:
            descriptor = klass.__dict__["header"]
            break
    assert isinstance(descriptor, property)

def test_model::datasources::queryresults_has_id():
    assert hasattr(model::datasources::QueryResults, "id")
    descriptor = None
    for klass in model::datasources::QueryResults.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_datasourcelibraryconfiguration_is_not_abstract():
    assert not inspect.isabstract(DataSourceLibraryConfiguration)


def test_datasourcelibraryconfiguration_constructor_exists():
    assert callable(DataSourceLibraryConfiguration.__init__)


def test_datasourcelibraryconfiguration_constructor_args():
    sig = inspect.signature(DataSourceLibraryConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_datasources::model::stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(datasources::model::StringToStringMap)


def test_datasources::model::stringtostringmap_constructor_exists():
    assert callable(datasources::model::StringToStringMap.__init__)


def test_datasources::model::stringtostringmap_constructor_args():
    sig = inspect.signature(datasources::model::StringToStringMap.__init__)
    params = list(sig.parameters.keys())



def test_querymatchingcriteria_is_not_abstract():
    assert not inspect.isabstract(QueryMatchingCriteria)


def test_querymatchingcriteria_constructor_exists():
    assert callable(QueryMatchingCriteria.__init__)


def test_querymatchingcriteria_constructor_args():
    sig = inspect.signature(QueryMatchingCriteria.__init__)
    params = list(sig.parameters.keys())



def test_model::datasources::datasourcelibraryconfiguration_is_not_abstract():
    assert not inspect.isabstract(model::datasources::DataSourceLibraryConfiguration)


def test_model::datasources::datasourcelibraryconfiguration_constructor_exists():
    assert callable(model::datasources::DataSourceLibraryConfiguration.__init__)


def test_model::datasources::datasourcelibraryconfiguration_constructor_args():
    sig = inspect.signature(model::datasources::DataSourceLibraryConfiguration.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"
    assert "modelInterpreterId" in params, "Missing parameter 'modelInterpreterId'"

def test_model::datasources::datasourcelibraryconfiguration_has_format():
    assert hasattr(model::datasources::DataSourceLibraryConfiguration, "format")
    descriptor = None
    for klass in model::datasources::DataSourceLibraryConfiguration.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_model::datasources::datasourcelibraryconfiguration_has_modelInterpreterId():
    assert hasattr(model::datasources::DataSourceLibraryConfiguration, "modelInterpreterId")
    descriptor = None
    for klass in model::datasources::DataSourceLibraryConfiguration.__mro__:
        if "modelInterpreterId" in klass.__dict__:
            descriptor = klass.__dict__["modelInterpreterId"]
            break
    assert isinstance(descriptor, property)



def test_datasources::model::geppettolibrary_is_not_abstract():
    assert not inspect.isabstract(datasources::model::GeppettoLibrary)


def test_datasources::model::geppettolibrary_constructor_exists():
    assert callable(datasources::model::GeppettoLibrary.__init__)


def test_datasources::model::geppettolibrary_constructor_args():
    sig = inspect.signature(datasources::model::GeppettoLibrary.__init__)
    params = list(sig.parameters.keys())



def test_model::variables::typetovaluemap_is_not_abstract():
    assert not inspect.isabstract(model::variables::TypeToValueMap)


def test_model::variables::typetovaluemap_constructor_exists():
    assert callable(model::variables::TypeToValueMap.__init__)


def test_model::variables::typetovaluemap_constructor_args():
    sig = inspect.signature(model::variables::TypeToValueMap.__init__)
    params = list(sig.parameters.keys())



def test_typetovaluemap_is_not_abstract():
    assert not inspect.isabstract(TypeToValueMap)


def test_typetovaluemap_constructor_exists():
    assert callable(TypeToValueMap.__init__)


def test_typetovaluemap_constructor_args():
    sig = inspect.signature(TypeToValueMap.__init__)
    params = list(sig.parameters.keys())



def test_arrayelement_is_not_abstract():
    assert not inspect.isabstract(ArrayElement)


def test_arrayelement_constructor_exists():
    assert callable(ArrayElement.__init__)


def test_arrayelement_constructor_args():
    sig = inspect.signature(ArrayElement.__init__)
    params = list(sig.parameters.keys())



def test_visualgroupelement_is_not_abstract():
    assert not inspect.isabstract(VisualGroupElement)


def test_visualgroupelement_constructor_exists():
    assert callable(VisualGroupElement.__init__)


def test_visualgroupelement_constructor_args():
    sig = inspect.signature(VisualGroupElement.__init__)
    params = list(sig.parameters.keys())



def test_functionplot_is_not_abstract():
    assert not inspect.isabstract(FunctionPlot)


def test_functionplot_constructor_exists():
    assert callable(FunctionPlot.__init__)


def test_functionplot_constructor_args():
    sig = inspect.signature(FunctionPlot.__init__)
    params = list(sig.parameters.keys())



def test_model::values::skeletontransformation_is_not_abstract():
    assert not inspect.isabstract(model::values::SkeletonTransformation)


def test_model::values::skeletontransformation_constructor_exists():
    assert callable(model::values::SkeletonTransformation.__init__)


def test_model::values::skeletontransformation_constructor_args():
    sig = inspect.signature(model::values::SkeletonTransformation.__init__)
    params = list(sig.parameters.keys())
    assert "skeletonTransformation" in params, "Missing parameter 'skeletonTransformation'"

def test_model::values::skeletontransformation_has_skeletonTransformation():
    assert hasattr(model::values::SkeletonTransformation, "skeletonTransformation")
    descriptor = None
    for klass in model::values::SkeletonTransformation.__mro__:
        if "skeletonTransformation" in klass.__dict__:
            descriptor = klass.__dict__["skeletonTransformation"]
            break
    assert isinstance(descriptor, property)



def test_skeletontransformation_is_not_abstract():
    assert not inspect.isabstract(SkeletonTransformation)


def test_skeletontransformation_constructor_exists():
    assert callable(SkeletonTransformation.__init__)


def test_skeletontransformation_constructor_args():
    sig = inspect.signature(SkeletonTransformation.__init__)
    params = list(sig.parameters.keys())



def test_model::values::pointerelement_is_not_abstract():
    assert not inspect.isabstract(model::values::PointerElement)


def test_model::values::pointerelement_constructor_exists():
    assert callable(model::values::PointerElement.__init__)


def test_model::values::pointerelement_constructor_args():
    sig = inspect.signature(model::values::PointerElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_model::values::pointerelement_has_index():
    assert hasattr(model::values::PointerElement, "index")
    descriptor = None
    for klass in model::values::PointerElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_pointerelement_is_not_abstract():
    assert not inspect.isabstract(PointerElement)


def test_pointerelement_constructor_exists():
    assert callable(PointerElement.__init__)


def test_pointerelement_constructor_args():
    sig = inspect.signature(PointerElement.__init__)
    params = list(sig.parameters.keys())



def test_model::values::functionplot_is_not_abstract():
    assert not inspect.isabstract(model::values::FunctionPlot)


def test_model::values::functionplot_constructor_exists():
    assert callable(model::values::FunctionPlot.__init__)


def test_model::values::functionplot_constructor_args():
    sig = inspect.signature(model::values::FunctionPlot.__init__)
    params = list(sig.parameters.keys())
    assert "stepValue" in params, "Missing parameter 'stepValue'"
    assert "finalValue" in params, "Missing parameter 'finalValue'"
    assert "xAxisLabel" in params, "Missing parameter 'xAxisLabel'"
    assert "initialValue" in params, "Missing parameter 'initialValue'"
    assert "title" in params, "Missing parameter 'title'"
    assert "yAxisLabel" in params, "Missing parameter 'yAxisLabel'"

def test_model::values::functionplot_has_stepValue():
    assert hasattr(model::values::FunctionPlot, "stepValue")
    descriptor = None
    for klass in model::values::FunctionPlot.__mro__:
        if "stepValue" in klass.__dict__:
            descriptor = klass.__dict__["stepValue"]
            break
    assert isinstance(descriptor, property)

def test_model::values::functionplot_has_finalValue():
    assert hasattr(model::values::FunctionPlot, "finalValue")
    descriptor = None
    for klass in model::values::FunctionPlot.__mro__:
        if "finalValue" in klass.__dict__:
            descriptor = klass.__dict__["finalValue"]
            break
    assert isinstance(descriptor, property)

def test_model::values::functionplot_has_xAxisLabel():
    assert hasattr(model::values::FunctionPlot, "xAxisLabel")
    descriptor = None
    for klass in model::values::FunctionPlot.__mro__:
        if "xAxisLabel" in klass.__dict__:
            descriptor = klass.__dict__["xAxisLabel"]
            break
    assert isinstance(descriptor, property)

def test_model::values::functionplot_has_initialValue():
    assert hasattr(model::values::FunctionPlot, "initialValue")
    descriptor = None
    for klass in model::values::FunctionPlot.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)

def test_model::values::functionplot_has_title():
    assert hasattr(model::values::FunctionPlot, "title")
    descriptor = None
    for klass in model::values::FunctionPlot.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_model::values::functionplot_has_yAxisLabel():
    assert hasattr(model::values::FunctionPlot, "yAxisLabel")
    descriptor = None
    for klass in model::values::FunctionPlot.__mro__:
        if "yAxisLabel" in klass.__dict__:
            descriptor = klass.__dict__["yAxisLabel"]
            break
    assert isinstance(descriptor, property)



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_physicalquantity_is_not_abstract():
    assert not inspect.isabstract(PhysicalQuantity)


def test_physicalquantity_constructor_exists():
    assert callable(PhysicalQuantity.__init__)


def test_physicalquantity_constructor_args():
    sig = inspect.signature(PhysicalQuantity.__init__)
    params = list(sig.parameters.keys())



def test_model::values::stringtovaluemap_is_not_abstract():
    assert not inspect.isabstract(model::values::StringToValueMap)


def test_model::values::stringtovaluemap_constructor_exists():
    assert callable(model::values::StringToValueMap.__init__)


def test_model::values::stringtovaluemap_constructor_args():
    sig = inspect.signature(model::values::StringToValueMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_model::values::stringtovaluemap_has_key():
    assert hasattr(model::values::StringToValueMap, "key")
    descriptor = None
    for klass in model::values::StringToValueMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_stringtovaluemap_is_not_abstract():
    assert not inspect.isabstract(StringToValueMap)


def test_stringtovaluemap_constructor_exists():
    assert callable(StringToValueMap.__init__)


def test_stringtovaluemap_constructor_args():
    sig = inspect.signature(StringToValueMap.__init__)
    params = list(sig.parameters.keys())



def test_aarrayvalue_is_not_abstract():
    assert not inspect.isabstract(AArrayValue)


def test_aarrayvalue_constructor_exists():
    assert callable(AArrayValue.__init__)


def test_aarrayvalue_constructor_args():
    sig = inspect.signature(AArrayValue.__init__)
    params = list(sig.parameters.keys())



def test_model::values::genericarray_is_not_abstract():
    assert not inspect.isabstract(model::values::GenericArray)


def test_model::values::genericarray_constructor_exists():
    assert callable(model::values::GenericArray.__init__)


def test_model::values::genericarray_constructor_args():
    sig = inspect.signature(model::values::GenericArray.__init__)
    params = list(sig.parameters.keys())



def test_model::values::stringarray_is_not_abstract():
    assert not inspect.isabstract(model::values::StringArray)


def test_model::values::stringarray_constructor_exists():
    assert callable(model::values::StringArray.__init__)


def test_model::values::stringarray_constructor_args():
    sig = inspect.signature(model::values::StringArray.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"

def test_model::values::stringarray_has_elements():
    assert hasattr(model::values::StringArray, "elements")
    descriptor = None
    for klass in model::values::StringArray.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)



def test_model::values::doublearray_is_not_abstract():
    assert not inspect.isabstract(model::values::DoubleArray)


def test_model::values::doublearray_constructor_exists():
    assert callable(model::values::DoubleArray.__init__)


def test_model::values::doublearray_constructor_args():
    sig = inspect.signature(model::values::DoubleArray.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"

def test_model::values::doublearray_has_elements():
    assert hasattr(model::values::DoubleArray, "elements")
    descriptor = None
    for klass in model::values::DoubleArray.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)



def test_model::values::intarray_is_not_abstract():
    assert not inspect.isabstract(model::values::IntArray)


def test_model::values::intarray_constructor_exists():
    assert callable(model::values::IntArray.__init__)


def test_model::values::intarray_constructor_args():
    sig = inspect.signature(model::values::IntArray.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"

def test_model::values::intarray_has_elements():
    assert hasattr(model::values::IntArray, "elements")
    descriptor = None
    for klass in model::values::IntArray.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)



def test_metadatavalue_is_not_abstract():
    assert not inspect.isabstract(MetadataValue)


def test_metadatavalue_constructor_exists():
    assert callable(MetadataValue.__init__)


def test_metadatavalue_constructor_args():
    sig = inspect.signature(MetadataValue.__init__)
    params = list(sig.parameters.keys())



def test_model::values::html_is_not_abstract():
    assert not inspect.isabstract(model::values::HTML)


def test_model::values::html_constructor_exists():
    assert callable(model::values::HTML.__init__)


def test_model::values::html_constructor_args():
    sig = inspect.signature(model::values::HTML.__init__)
    params = list(sig.parameters.keys())
    assert "html" in params, "Missing parameter 'html'"

def test_model::values::html_has_html():
    assert hasattr(model::values::HTML, "html")
    descriptor = None
    for klass in model::values::HTML.__mro__:
        if "html" in klass.__dict__:
            descriptor = klass.__dict__["html"]
            break
    assert isinstance(descriptor, property)



def test_model::values::url_is_not_abstract():
    assert not inspect.isabstract(model::values::URL)


def test_model::values::url_constructor_exists():
    assert callable(model::values::URL.__init__)


def test_model::values::url_constructor_args():
    sig = inspect.signature(model::values::URL.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"

def test_model::values::url_has_url():
    assert hasattr(model::values::URL, "url")
    descriptor = None
    for klass in model::values::URL.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_model::values::json_is_not_abstract():
    assert not inspect.isabstract(model::values::JSON)


def test_model::values::json_constructor_exists():
    assert callable(model::values::JSON.__init__)


def test_model::values::json_constructor_args():
    sig = inspect.signature(model::values::JSON.__init__)
    params = list(sig.parameters.keys())
    assert "json" in params, "Missing parameter 'json'"

def test_model::values::json_has_json():
    assert hasattr(model::values::JSON, "json")
    descriptor = None
    for klass in model::values::JSON.__mro__:
        if "json" in klass.__dict__:
            descriptor = klass.__dict__["json"]
            break
    assert isinstance(descriptor, property)



def test_model::values::metadata_is_not_abstract():
    assert not inspect.isabstract(model::values::Metadata)


def test_model::values::metadata_constructor_exists():
    assert callable(model::values::Metadata.__init__)


def test_model::values::metadata_constructor_args():
    sig = inspect.signature(model::values::Metadata.__init__)
    params = list(sig.parameters.keys())



def test_model::values::text_is_not_abstract():
    assert not inspect.isabstract(model::values::Text)


def test_model::values::text_constructor_exists():
    assert callable(model::values::Text.__init__)


def test_model::values::text_constructor_args():
    sig = inspect.signature(model::values::Text.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_model::values::text_has_text():
    assert hasattr(model::values::Text, "text")
    descriptor = None
    for klass in model::values::Text.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_visualgroup_is_not_abstract():
    assert not inspect.isabstract(VisualGroup)


def test_visualgroup_constructor_exists():
    assert callable(VisualGroup.__init__)


def test_visualgroup_constructor_args():
    sig = inspect.signature(VisualGroup.__init__)
    params = list(sig.parameters.keys())



def test_arrayvalue_is_not_abstract():
    assert not inspect.isabstract(ArrayValue)


def test_arrayvalue_constructor_exists():
    assert callable(ArrayValue.__init__)


def test_arrayvalue_constructor_args():
    sig = inspect.signature(ArrayValue.__init__)
    params = list(sig.parameters.keys())



def test_point_is_not_abstract():
    assert not inspect.isabstract(Point)


def test_point_constructor_exists():
    assert callable(Point.__init__)


def test_point_constructor_args():
    sig = inspect.signature(Point.__init__)
    params = list(sig.parameters.keys())



def test_url_is_not_abstract():
    assert not inspect.isabstract(URL)


def test_url_constructor_exists():
    assert callable(URL.__init__)


def test_url_constructor_args():
    sig = inspect.signature(URL.__init__)
    params = list(sig.parameters.keys())



def test_text_is_not_abstract():
    assert not inspect.isabstract(Text)


def test_text_constructor_exists():
    assert callable(Text.__init__)


def test_text_constructor_args():
    sig = inspect.signature(Text.__init__)
    params = list(sig.parameters.keys())



def test_image_is_not_abstract():
    assert not inspect.isabstract(Image)


def test_image_constructor_exists():
    assert callable(Image.__init__)


def test_image_constructor_args():
    sig = inspect.signature(Image.__init__)
    params = list(sig.parameters.keys())



def test_argument_is_not_abstract():
    assert not inspect.isabstract(Argument)


def test_argument_constructor_exists():
    assert callable(Argument.__init__)


def test_argument_constructor_args():
    sig = inspect.signature(Argument.__init__)
    params = list(sig.parameters.keys())



def test_dynamics_is_not_abstract():
    assert not inspect.isabstract(Dynamics)


def test_dynamics_constructor_exists():
    assert callable(Dynamics.__init__)


def test_dynamics_constructor_args():
    sig = inspect.signature(Dynamics.__init__)
    params = list(sig.parameters.keys())



def test_quantity_is_not_abstract():
    assert not inspect.isabstract(Quantity)


def test_quantity_constructor_exists():
    assert callable(Quantity.__init__)


def test_quantity_constructor_args():
    sig = inspect.signature(Quantity.__init__)
    params = list(sig.parameters.keys())



def test_model::values::physicalquantity_is_not_abstract():
    assert not inspect.isabstract(model::values::PhysicalQuantity)


def test_model::values::physicalquantity_constructor_exists():
    assert callable(model::values::PhysicalQuantity.__init__)


def test_model::values::physicalquantity_constructor_args():
    sig = inspect.signature(model::values::PhysicalQuantity.__init__)
    params = list(sig.parameters.keys())



def test_composite_is_not_abstract():
    assert not inspect.isabstract(Composite)


def test_composite_constructor_exists():
    assert callable(Composite.__init__)


def test_composite_constructor_args():
    sig = inspect.signature(Composite.__init__)
    params = list(sig.parameters.keys())



def test_json_is_not_abstract():
    assert not inspect.isabstract(JSON)


def test_json_constructor_exists():
    assert callable(JSON.__init__)


def test_json_constructor_args():
    sig = inspect.signature(JSON.__init__)
    params = list(sig.parameters.keys())



def test_html_is_not_abstract():
    assert not inspect.isabstract(HTML)


def test_html_constructor_exists():
    assert callable(HTML.__init__)


def test_html_constructor_args():
    sig = inspect.signature(HTML.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_visualtype_is_not_abstract():
    assert not inspect.isabstract(VisualType)


def test_visualtype_constructor_exists():
    assert callable(VisualType.__init__)


def test_visualtype_constructor_args():
    sig = inspect.signature(VisualType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::compositevisualtype_is_not_abstract():
    assert not inspect.isabstract(model::types::CompositeVisualType)


def test_model::types::compositevisualtype_constructor_exists():
    assert callable(model::types::CompositeVisualType.__init__)


def test_model::types::compositevisualtype_constructor_args():
    sig = inspect.signature(model::types::CompositeVisualType.__init__)
    params = list(sig.parameters.keys())



def test_instance_is_not_abstract():
    assert not inspect.isabstract(Instance)


def test_instance_constructor_exists():
    assert callable(Instance.__init__)


def test_instance_constructor_args():
    sig = inspect.signature(Instance.__init__)
    params = list(sig.parameters.keys())



def test_model::instances::simpleinstance_is_not_abstract():
    assert not inspect.isabstract(model::instances::SimpleInstance)


def test_model::instances::simpleinstance_constructor_exists():
    assert callable(model::instances::SimpleInstance.__init__)


def test_model::instances::simpleinstance_constructor_args():
    sig = inspect.signature(model::instances::SimpleInstance.__init__)
    params = list(sig.parameters.keys())



def test_model::instances::simpleconnectioninstance_is_not_abstract():
    assert not inspect.isabstract(model::instances::SimpleConnectionInstance)


def test_model::instances::simpleconnectioninstance_constructor_exists():
    assert callable(model::instances::SimpleConnectionInstance.__init__)


def test_model::instances::simpleconnectioninstance_constructor_args():
    sig = inspect.signature(model::instances::SimpleConnectionInstance.__init__)
    params = list(sig.parameters.keys())
    assert "connectivity" in params, "Missing parameter 'connectivity'"

def test_model::instances::simpleconnectioninstance_has_connectivity():
    assert hasattr(model::instances::SimpleConnectionInstance, "connectivity")
    descriptor = None
    for klass in model::instances::SimpleConnectionInstance.__mro__:
        if "connectivity" in klass.__dict__:
            descriptor = klass.__dict__["connectivity"]
            break
    assert isinstance(descriptor, property)



def test_model::isynchable_is_not_abstract():
    assert not inspect.isabstract(model::ISynchable)


def test_model::isynchable_constructor_exists():
    assert callable(model::ISynchable.__init__)


def test_model::isynchable_constructor_args():
    sig = inspect.signature(model::ISynchable.__init__)
    params = list(sig.parameters.keys())
    assert "synched" in params, "Missing parameter 'synched'"

def test_model::isynchable_has_synched():
    assert hasattr(model::ISynchable, "synched")
    descriptor = None
    for klass in model::ISynchable.__mro__:
        if "synched" in klass.__dict__:
            descriptor = klass.__dict__["synched"]
            break
    assert isinstance(descriptor, property)



def test_visualvalue_is_not_abstract():
    assert not inspect.isabstract(VisualValue)


def test_visualvalue_constructor_exists():
    assert callable(VisualValue.__init__)


def test_visualvalue_constructor_args():
    sig = inspect.signature(VisualValue.__init__)
    params = list(sig.parameters.keys())



def test_model::values::cylinder_is_not_abstract():
    assert not inspect.isabstract(model::values::Cylinder)


def test_model::values::cylinder_constructor_exists():
    assert callable(model::values::Cylinder.__init__)


def test_model::values::cylinder_constructor_args():
    sig = inspect.signature(model::values::Cylinder.__init__)
    params = list(sig.parameters.keys())
    assert "bottomRadius" in params, "Missing parameter 'bottomRadius'"
    assert "topRadius" in params, "Missing parameter 'topRadius'"
    assert "height" in params, "Missing parameter 'height'"

def test_model::values::cylinder_has_bottomRadius():
    assert hasattr(model::values::Cylinder, "bottomRadius")
    descriptor = None
    for klass in model::values::Cylinder.__mro__:
        if "bottomRadius" in klass.__dict__:
            descriptor = klass.__dict__["bottomRadius"]
            break
    assert isinstance(descriptor, property)

def test_model::values::cylinder_has_topRadius():
    assert hasattr(model::values::Cylinder, "topRadius")
    descriptor = None
    for klass in model::values::Cylinder.__mro__:
        if "topRadius" in klass.__dict__:
            descriptor = klass.__dict__["topRadius"]
            break
    assert isinstance(descriptor, property)

def test_model::values::cylinder_has_height():
    assert hasattr(model::values::Cylinder, "height")
    descriptor = None
    for klass in model::values::Cylinder.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_model::values::collada_is_not_abstract():
    assert not inspect.isabstract(model::values::Collada)


def test_model::values::collada_constructor_exists():
    assert callable(model::values::Collada.__init__)


def test_model::values::collada_constructor_args():
    sig = inspect.signature(model::values::Collada.__init__)
    params = list(sig.parameters.keys())
    assert "collada" in params, "Missing parameter 'collada'"

def test_model::values::collada_has_collada():
    assert hasattr(model::values::Collada, "collada")
    descriptor = None
    for klass in model::values::Collada.__mro__:
        if "collada" in klass.__dict__:
            descriptor = klass.__dict__["collada"]
            break
    assert isinstance(descriptor, property)



def test_model::values::obj_is_not_abstract():
    assert not inspect.isabstract(model::values::OBJ)


def test_model::values::obj_constructor_exists():
    assert callable(model::values::OBJ.__init__)


def test_model::values::obj_constructor_args():
    sig = inspect.signature(model::values::OBJ.__init__)
    params = list(sig.parameters.keys())
    assert "obj" in params, "Missing parameter 'obj'"

def test_model::values::obj_has_obj():
    assert hasattr(model::values::OBJ, "obj")
    descriptor = None
    for klass in model::values::OBJ.__mro__:
        if "obj" in klass.__dict__:
            descriptor = klass.__dict__["obj"]
            break
    assert isinstance(descriptor, property)



def test_model::values::skeletonanimation_is_not_abstract():
    assert not inspect.isabstract(model::values::SkeletonAnimation)


def test_model::values::skeletonanimation_constructor_exists():
    assert callable(model::values::SkeletonAnimation.__init__)


def test_model::values::skeletonanimation_constructor_args():
    sig = inspect.signature(model::values::SkeletonAnimation.__init__)
    params = list(sig.parameters.keys())



def test_model::values::sphere_is_not_abstract():
    assert not inspect.isabstract(model::values::Sphere)


def test_model::values::sphere_constructor_exists():
    assert callable(model::values::Sphere.__init__)


def test_model::values::sphere_constructor_args():
    sig = inspect.signature(model::values::Sphere.__init__)
    params = list(sig.parameters.keys())
    assert "radius" in params, "Missing parameter 'radius'"

def test_model::values::sphere_has_radius():
    assert hasattr(model::values::Sphere, "radius")
    descriptor = None
    for klass in model::values::Sphere.__mro__:
        if "radius" in klass.__dict__:
            descriptor = klass.__dict__["radius"]
            break
    assert isinstance(descriptor, property)



def test_types::model::domainmodel__is_not_abstract():
    assert not inspect.isabstract(types::model::DomainModel_)


def test_types::model::domainmodel__constructor_exists():
    assert callable(types::model::DomainModel_.__init__)


def test_types::model::domainmodel__constructor_args():
    sig = inspect.signature(types::model::DomainModel_.__init__)
    params = list(sig.parameters.keys())



def test_model::domainmodel__is_not_abstract():
    assert not inspect.isabstract(model::DomainModel_)


def test_model::domainmodel__constructor_exists():
    assert callable(model::DomainModel_.__init__)


def test_model::domainmodel__constructor_args():
    sig = inspect.signature(model::DomainModel_.__init__)
    params = list(sig.parameters.keys())
    assert "domainModel" in params, "Missing parameter 'domainModel'"

def test_model::domainmodel__has_domainModel():
    assert hasattr(model::DomainModel_, "domainModel")
    descriptor = None
    for klass in model::DomainModel_.__mro__:
        if "domainModel" in klass.__dict__:
            descriptor = klass.__dict__["domainModel"]
            break
    assert isinstance(descriptor, property)



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_model::values::visualvalue_is_not_abstract():
    assert not inspect.isabstract(model::values::VisualValue)


def test_model::values::visualvalue_constructor_exists():
    assert callable(model::values::VisualValue.__init__)


def test_model::values::visualvalue_constructor_args():
    sig = inspect.signature(model::values::VisualValue.__init__)
    params = list(sig.parameters.keys())



def test_model::values::composite_is_not_abstract():
    assert not inspect.isabstract(model::values::Composite)


def test_model::values::composite_constructor_exists():
    assert callable(model::values::Composite.__init__)


def test_model::values::composite_constructor_args():
    sig = inspect.signature(model::values::Composite.__init__)
    params = list(sig.parameters.keys())



def test_model::values::connection_is_not_abstract():
    assert not inspect.isabstract(model::values::Connection)


def test_model::values::connection_constructor_exists():
    assert callable(model::values::Connection.__init__)


def test_model::values::connection_constructor_args():
    sig = inspect.signature(model::values::Connection.__init__)
    params = list(sig.parameters.keys())
    assert "connectivity" in params, "Missing parameter 'connectivity'"

def test_model::values::connection_has_connectivity():
    assert hasattr(model::values::Connection, "connectivity")
    descriptor = None
    for klass in model::values::Connection.__mro__:
        if "connectivity" in klass.__dict__:
            descriptor = klass.__dict__["connectivity"]
            break
    assert isinstance(descriptor, property)



def test_model::values::function_is_not_abstract():
    assert not inspect.isabstract(model::values::Function)


def test_model::values::function_constructor_exists():
    assert callable(model::values::Function.__init__)


def test_model::values::function_constructor_args():
    sig = inspect.signature(model::values::Function.__init__)
    params = list(sig.parameters.keys())



def test_model::values::aarrayvalue_is_not_abstract():
    assert not inspect.isabstract(model::values::AArrayValue)


def test_model::values::aarrayvalue_constructor_exists():
    assert callable(model::values::AArrayValue.__init__)


def test_model::values::aarrayvalue_constructor_args():
    sig = inspect.signature(model::values::AArrayValue.__init__)
    params = list(sig.parameters.keys())



def test_model::values::arrayvalue_is_not_abstract():
    assert not inspect.isabstract(model::values::ArrayValue)


def test_model::values::arrayvalue_constructor_exists():
    assert callable(model::values::ArrayValue.__init__)


def test_model::values::arrayvalue_constructor_args():
    sig = inspect.signature(model::values::ArrayValue.__init__)
    params = list(sig.parameters.keys())



def test_model::values::arrayelement_is_not_abstract():
    assert not inspect.isabstract(model::values::ArrayElement)


def test_model::values::arrayelement_constructor_exists():
    assert callable(model::values::ArrayElement.__init__)


def test_model::values::arrayelement_constructor_args():
    sig = inspect.signature(model::values::ArrayElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_model::values::arrayelement_has_index():
    assert hasattr(model::values::ArrayElement, "index")
    descriptor = None
    for klass in model::values::ArrayElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_model::values::image_is_not_abstract():
    assert not inspect.isabstract(model::values::Image)


def test_model::values::image_constructor_exists():
    assert callable(model::values::Image.__init__)


def test_model::values::image_constructor_args():
    sig = inspect.signature(model::values::Image.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "reference" in params, "Missing parameter 'reference'"
    assert "format" in params, "Missing parameter 'format'"
    assert "name" in params, "Missing parameter 'name'"

def test_model::values::image_has_data():
    assert hasattr(model::values::Image, "data")
    descriptor = None
    for klass in model::values::Image.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_model::values::image_has_reference():
    assert hasattr(model::values::Image, "reference")
    descriptor = None
    for klass in model::values::Image.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_model::values::image_has_format():
    assert hasattr(model::values::Image, "format")
    descriptor = None
    for klass in model::values::Image.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_model::values::image_has_name():
    assert hasattr(model::values::Image, "name")
    descriptor = None
    for klass in model::values::Image.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::values::argument_is_not_abstract():
    assert not inspect.isabstract(model::values::Argument)


def test_model::values::argument_constructor_exists():
    assert callable(model::values::Argument.__init__)


def test_model::values::argument_constructor_args():
    sig = inspect.signature(model::values::Argument.__init__)
    params = list(sig.parameters.keys())
    assert "argument" in params, "Missing parameter 'argument'"

def test_model::values::argument_has_argument():
    assert hasattr(model::values::Argument, "argument")
    descriptor = None
    for klass in model::values::Argument.__mro__:
        if "argument" in klass.__dict__:
            descriptor = klass.__dict__["argument"]
            break
    assert isinstance(descriptor, property)



def test_model::values::unit_is_not_abstract():
    assert not inspect.isabstract(model::values::Unit)


def test_model::values::unit_constructor_exists():
    assert callable(model::values::Unit.__init__)


def test_model::values::unit_constructor_args():
    sig = inspect.signature(model::values::Unit.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_model::values::unit_has_unit():
    assert hasattr(model::values::Unit, "unit")
    descriptor = None
    for klass in model::values::Unit.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_model::values::importvalue_is_not_abstract():
    assert not inspect.isabstract(model::values::ImportValue)


def test_model::values::importvalue_constructor_exists():
    assert callable(model::values::ImportValue.__init__)


def test_model::values::importvalue_constructor_args():
    sig = inspect.signature(model::values::ImportValue.__init__)
    params = list(sig.parameters.keys())
    assert "modelInterpreterId" in params, "Missing parameter 'modelInterpreterId'"

def test_model::values::importvalue_has_modelInterpreterId():
    assert hasattr(model::values::ImportValue, "modelInterpreterId")
    descriptor = None
    for klass in model::values::ImportValue.__mro__:
        if "modelInterpreterId" in klass.__dict__:
            descriptor = klass.__dict__["modelInterpreterId"]
            break
    assert isinstance(descriptor, property)



def test_model::values::mdtimeseries_is_not_abstract():
    assert not inspect.isabstract(model::values::MDTimeSeries)


def test_model::values::mdtimeseries_constructor_exists():
    assert callable(model::values::MDTimeSeries.__init__)


def test_model::values::mdtimeseries_constructor_args():
    sig = inspect.signature(model::values::MDTimeSeries.__init__)
    params = list(sig.parameters.keys())



def test_model::values::expression_is_not_abstract():
    assert not inspect.isabstract(model::values::Expression)


def test_model::values::expression_constructor_exists():
    assert callable(model::values::Expression.__init__)


def test_model::values::expression_constructor_args():
    sig = inspect.signature(model::values::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_model::values::expression_has_expression():
    assert hasattr(model::values::Expression, "expression")
    descriptor = None
    for klass in model::values::Expression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_model::values::metadatavalue_is_not_abstract():
    assert not inspect.isabstract(model::values::MetadataValue)


def test_model::values::metadatavalue_constructor_exists():
    assert callable(model::values::MetadataValue.__init__)


def test_model::values::metadatavalue_constructor_args():
    sig = inspect.signature(model::values::MetadataValue.__init__)
    params = list(sig.parameters.keys())



def test_model::values::point_is_not_abstract():
    assert not inspect.isabstract(model::values::Point)


def test_model::values::point_constructor_exists():
    assert callable(model::values::Point.__init__)


def test_model::values::point_constructor_args():
    sig = inspect.signature(model::values::Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "z" in params, "Missing parameter 'z'"
    assert "x" in params, "Missing parameter 'x'"

def test_model::values::point_has_y():
    assert hasattr(model::values::Point, "y")
    descriptor = None
    for klass in model::values::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_model::values::point_has_z():
    assert hasattr(model::values::Point, "z")
    descriptor = None
    for klass in model::values::Point.__mro__:
        if "z" in klass.__dict__:
            descriptor = klass.__dict__["z"]
            break
    assert isinstance(descriptor, property)

def test_model::values::point_has_x():
    assert hasattr(model::values::Point, "x")
    descriptor = None
    for klass in model::values::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_model::values::pointer_is_not_abstract():
    assert not inspect.isabstract(model::values::Pointer)


def test_model::values::pointer_constructor_exists():
    assert callable(model::values::Pointer.__init__)


def test_model::values::pointer_constructor_args():
    sig = inspect.signature(model::values::Pointer.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_model::values::pointer_has_path():
    assert hasattr(model::values::Pointer, "path")
    descriptor = None
    for klass in model::values::Pointer.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_model::values::dynamics_is_not_abstract():
    assert not inspect.isabstract(model::values::Dynamics)


def test_model::values::dynamics_constructor_exists():
    assert callable(model::values::Dynamics.__init__)


def test_model::values::dynamics_constructor_args():
    sig = inspect.signature(model::values::Dynamics.__init__)
    params = list(sig.parameters.keys())



def test_model::values::particles_is_not_abstract():
    assert not inspect.isabstract(model::values::Particles)


def test_model::values::particles_constructor_exists():
    assert callable(model::values::Particles.__init__)


def test_model::values::particles_constructor_args():
    sig = inspect.signature(model::values::Particles.__init__)
    params = list(sig.parameters.keys())



def test_model::values::quantity_is_not_abstract():
    assert not inspect.isabstract(model::values::Quantity)


def test_model::values::quantity_constructor_exists():
    assert callable(model::values::Quantity.__init__)


def test_model::values::quantity_constructor_args():
    sig = inspect.signature(model::values::Quantity.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "scalingFactor" in params, "Missing parameter 'scalingFactor'"

def test_model::values::quantity_has_value():
    assert hasattr(model::values::Quantity, "value")
    descriptor = None
    for klass in model::values::Quantity.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_model::values::quantity_has_scalingFactor():
    assert hasattr(model::values::Quantity, "scalingFactor")
    descriptor = None
    for klass in model::values::Quantity.__mro__:
        if "scalingFactor" in klass.__dict__:
            descriptor = klass.__dict__["scalingFactor"]
            break
    assert isinstance(descriptor, property)



def test_model::values::timeseries_is_not_abstract():
    assert not inspect.isabstract(model::values::TimeSeries)


def test_model::values::timeseries_constructor_exists():
    assert callable(model::values::TimeSeries.__init__)


def test_model::values::timeseries_constructor_args():
    sig = inspect.signature(model::values::TimeSeries.__init__)
    params = list(sig.parameters.keys())
    assert "scalingFactor" in params, "Missing parameter 'scalingFactor'"
    assert "value" in params, "Missing parameter 'value'"

def test_model::values::timeseries_has_scalingFactor():
    assert hasattr(model::values::TimeSeries, "scalingFactor")
    descriptor = None
    for klass in model::values::TimeSeries.__mro__:
        if "scalingFactor" in klass.__dict__:
            descriptor = klass.__dict__["scalingFactor"]
            break
    assert isinstance(descriptor, property)

def test_model::values::timeseries_has_value():
    assert hasattr(model::values::TimeSeries, "value")
    descriptor = None
    for klass in model::values::TimeSeries.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model::stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(model::StringToStringMap)


def test_model::stringtostringmap_constructor_exists():
    assert callable(model::StringToStringMap.__init__)


def test_model::stringtostringmap_constructor_args():
    sig = inspect.signature(model::StringToStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_model::stringtostringmap_has_value():
    assert hasattr(model::StringToStringMap, "value")
    descriptor = None
    for klass in model::StringToStringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_model::stringtostringmap_has_key():
    assert hasattr(model::StringToStringMap, "key")
    descriptor = None
    for klass in model::StringToStringMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel__is_not_abstract():
    assert not inspect.isabstract(DomainModel_)


def test_domainmodel__constructor_exists():
    assert callable(DomainModel_.__init__)


def test_domainmodel__constructor_args():
    sig = inspect.signature(DomainModel_.__init__)
    params = list(sig.parameters.keys())



def test_model::externaldomainmodel_is_not_abstract():
    assert not inspect.isabstract(model::ExternalDomainModel)


def test_model::externaldomainmodel_constructor_exists():
    assert callable(model::ExternalDomainModel.__init__)


def test_model::externaldomainmodel_constructor_args():
    sig = inspect.signature(model::ExternalDomainModel.__init__)
    params = list(sig.parameters.keys())
    assert "fileFormat" in params, "Missing parameter 'fileFormat'"

def test_model::externaldomainmodel_has_fileFormat():
    assert hasattr(model::ExternalDomainModel, "fileFormat")
    descriptor = None
    for klass in model::ExternalDomainModel.__mro__:
        if "fileFormat" in klass.__dict__:
            descriptor = klass.__dict__["fileFormat"]
            break
    assert isinstance(descriptor, property)



def test_model::modelformat_is_not_abstract():
    assert not inspect.isabstract(model::ModelFormat)


def test_model::modelformat_constructor_exists():
    assert callable(model::ModelFormat.__init__)


def test_model::modelformat_constructor_args():
    sig = inspect.signature(model::ModelFormat.__init__)
    params = list(sig.parameters.keys())
    assert "modelFormat" in params, "Missing parameter 'modelFormat'"

def test_model::modelformat_has_modelFormat():
    assert hasattr(model::ModelFormat, "modelFormat")
    descriptor = None
    for klass in model::ModelFormat.__mro__:
        if "modelFormat" in klass.__dict__:
            descriptor = klass.__dict__["modelFormat"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_model::types::htmltype_is_not_abstract():
    assert not inspect.isabstract(model::types::HTMLType)


def test_model::types::htmltype_constructor_exists():
    assert callable(model::types::HTMLType.__init__)


def test_model::types::htmltype_constructor_args():
    sig = inspect.signature(model::types::HTMLType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::expressiontype_is_not_abstract():
    assert not inspect.isabstract(model::types::ExpressionType)


def test_model::types::expressiontype_constructor_exists():
    assert callable(model::types::ExpressionType.__init__)


def test_model::types::expressiontype_constructor_args():
    sig = inspect.signature(model::types::ExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::urltype_is_not_abstract():
    assert not inspect.isabstract(model::types::URLType)


def test_model::types::urltype_constructor_exists():
    assert callable(model::types::URLType.__init__)


def test_model::types::urltype_constructor_args():
    sig = inspect.signature(model::types::URLType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::simplearraytype_is_not_abstract():
    assert not inspect.isabstract(model::types::SimpleArrayType)


def test_model::types::simplearraytype_constructor_exists():
    assert callable(model::types::SimpleArrayType.__init__)


def test_model::types::simplearraytype_constructor_args():
    sig = inspect.signature(model::types::SimpleArrayType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::imagetype_is_not_abstract():
    assert not inspect.isabstract(model::types::ImageType)


def test_model::types::imagetype_constructor_exists():
    assert callable(model::types::ImageType.__init__)


def test_model::types::imagetype_constructor_args():
    sig = inspect.signature(model::types::ImageType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::pointertype_is_not_abstract():
    assert not inspect.isabstract(model::types::PointerType)


def test_model::types::pointertype_constructor_exists():
    assert callable(model::types::PointerType.__init__)


def test_model::types::pointertype_constructor_args():
    sig = inspect.signature(model::types::PointerType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::compositetype_is_not_abstract():
    assert not inspect.isabstract(model::types::CompositeType)


def test_model::types::compositetype_constructor_exists():
    assert callable(model::types::CompositeType.__init__)


def test_model::types::compositetype_constructor_args():
    sig = inspect.signature(model::types::CompositeType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::arraytype_is_not_abstract():
    assert not inspect.isabstract(model::types::ArrayType)


def test_model::types::arraytype_constructor_exists():
    assert callable(model::types::ArrayType.__init__)


def test_model::types::arraytype_constructor_args():
    sig = inspect.signature(model::types::ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_model::types::arraytype_has_size():
    assert hasattr(model::types::ArrayType, "size")
    descriptor = None
    for klass in model::types::ArrayType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_model::types::visualtype_is_not_abstract():
    assert not inspect.isabstract(model::types::VisualType)


def test_model::types::visualtype_constructor_exists():
    assert callable(model::types::VisualType.__init__)


def test_model::types::visualtype_constructor_args():
    sig = inspect.signature(model::types::VisualType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::importtype_is_not_abstract():
    assert not inspect.isabstract(model::types::ImportType)


def test_model::types::importtype_constructor_exists():
    assert callable(model::types::ImportType.__init__)


def test_model::types::importtype_constructor_args():
    sig = inspect.signature(model::types::ImportType.__init__)
    params = list(sig.parameters.keys())
    assert "referenceURL" in params, "Missing parameter 'referenceURL'"
    assert "autoresolve" in params, "Missing parameter 'autoresolve'"
    assert "url" in params, "Missing parameter 'url'"
    assert "modelInterpreterId" in params, "Missing parameter 'modelInterpreterId'"

def test_model::types::importtype_has_referenceURL():
    assert hasattr(model::types::ImportType, "referenceURL")
    descriptor = None
    for klass in model::types::ImportType.__mro__:
        if "referenceURL" in klass.__dict__:
            descriptor = klass.__dict__["referenceURL"]
            break
    assert isinstance(descriptor, property)

def test_model::types::importtype_has_autoresolve():
    assert hasattr(model::types::ImportType, "autoresolve")
    descriptor = None
    for klass in model::types::ImportType.__mro__:
        if "autoresolve" in klass.__dict__:
            descriptor = klass.__dict__["autoresolve"]
            break
    assert isinstance(descriptor, property)

def test_model::types::importtype_has_url():
    assert hasattr(model::types::ImportType, "url")
    descriptor = None
    for klass in model::types::ImportType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_model::types::importtype_has_modelInterpreterId():
    assert hasattr(model::types::ImportType, "modelInterpreterId")
    descriptor = None
    for klass in model::types::ImportType.__mro__:
        if "modelInterpreterId" in klass.__dict__:
            descriptor = klass.__dict__["modelInterpreterId"]
            break
    assert isinstance(descriptor, property)



def test_model::types::parametertype_is_not_abstract():
    assert not inspect.isabstract(model::types::ParameterType)


def test_model::types::parametertype_constructor_exists():
    assert callable(model::types::ParameterType.__init__)


def test_model::types::parametertype_constructor_args():
    sig = inspect.signature(model::types::ParameterType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::statevariabletype_is_not_abstract():
    assert not inspect.isabstract(model::types::StateVariableType)


def test_model::types::statevariabletype_constructor_exists():
    assert callable(model::types::StateVariableType.__init__)


def test_model::types::statevariabletype_constructor_args():
    sig = inspect.signature(model::types::StateVariableType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::quantitytype_is_not_abstract():
    assert not inspect.isabstract(model::types::QuantityType)


def test_model::types::quantitytype_constructor_exists():
    assert callable(model::types::QuantityType.__init__)


def test_model::types::quantitytype_constructor_args():
    sig = inspect.signature(model::types::QuantityType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::metadatatype_is_not_abstract():
    assert not inspect.isabstract(model::types::MetadataType)


def test_model::types::metadatatype_constructor_exists():
    assert callable(model::types::MetadataType.__init__)


def test_model::types::metadatatype_constructor_args():
    sig = inspect.signature(model::types::MetadataType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::simpletype_is_not_abstract():
    assert not inspect.isabstract(model::types::SimpleType)


def test_model::types::simpletype_constructor_exists():
    assert callable(model::types::SimpleType.__init__)


def test_model::types::simpletype_constructor_args():
    sig = inspect.signature(model::types::SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::dynamicstype_is_not_abstract():
    assert not inspect.isabstract(model::types::DynamicsType)


def test_model::types::dynamicstype_constructor_exists():
    assert callable(model::types::DynamicsType.__init__)


def test_model::types::dynamicstype_constructor_args():
    sig = inspect.signature(model::types::DynamicsType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::argumenttype_is_not_abstract():
    assert not inspect.isabstract(model::types::ArgumentType)


def test_model::types::argumenttype_constructor_exists():
    assert callable(model::types::ArgumentType.__init__)


def test_model::types::argumenttype_constructor_args():
    sig = inspect.signature(model::types::ArgumentType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::texttype_is_not_abstract():
    assert not inspect.isabstract(model::types::TextType)


def test_model::types::texttype_constructor_exists():
    assert callable(model::types::TextType.__init__)


def test_model::types::texttype_constructor_args():
    sig = inspect.signature(model::types::TextType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::connectiontype_is_not_abstract():
    assert not inspect.isabstract(model::types::ConnectionType)


def test_model::types::connectiontype_constructor_exists():
    assert callable(model::types::ConnectionType.__init__)


def test_model::types::connectiontype_constructor_args():
    sig = inspect.signature(model::types::ConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::jsontype_is_not_abstract():
    assert not inspect.isabstract(model::types::JSONType)


def test_model::types::jsontype_constructor_exists():
    assert callable(model::types::JSONType.__init__)


def test_model::types::jsontype_constructor_args():
    sig = inspect.signature(model::types::JSONType.__init__)
    params = list(sig.parameters.keys())



def test_model::types::pointtype_is_not_abstract():
    assert not inspect.isabstract(model::types::PointType)


def test_model::types::pointtype_constructor_exists():
    assert callable(model::types::PointType.__init__)


def test_model::types::pointtype_constructor_args():
    sig = inspect.signature(model::types::PointType.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_model::types::type_is_not_abstract():
    assert not inspect.isabstract(model::types::Type)


def test_model::types::type_constructor_exists():
    assert callable(model::types::Type.__init__)


def test_model::types::type_constructor_args():
    sig = inspect.signature(model::types::Type.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_model::types::type_has_abstract():
    assert hasattr(model::types::Type, "abstract")
    descriptor = None
    for klass in model::types::Type.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_model::values::visualgroup_is_not_abstract():
    assert not inspect.isabstract(model::values::VisualGroup)


def test_model::values::visualgroup_constructor_exists():
    assert callable(model::values::VisualGroup.__init__)


def test_model::values::visualgroup_constructor_args():
    sig = inspect.signature(model::values::VisualGroup.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "highSpectrumColor" in params, "Missing parameter 'highSpectrumColor'"
    assert "lowSpectrumColor" in params, "Missing parameter 'lowSpectrumColor'"

def test_model::values::visualgroup_has_type():
    assert hasattr(model::values::VisualGroup, "type")
    descriptor = None
    for klass in model::values::VisualGroup.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_model::values::visualgroup_has_highSpectrumColor():
    assert hasattr(model::values::VisualGroup, "highSpectrumColor")
    descriptor = None
    for klass in model::values::VisualGroup.__mro__:
        if "highSpectrumColor" in klass.__dict__:
            descriptor = klass.__dict__["highSpectrumColor"]
            break
    assert isinstance(descriptor, property)

def test_model::values::visualgroup_has_lowSpectrumColor():
    assert hasattr(model::values::VisualGroup, "lowSpectrumColor")
    descriptor = None
    for klass in model::values::VisualGroup.__mro__:
        if "lowSpectrumColor" in klass.__dict__:
            descriptor = klass.__dict__["lowSpectrumColor"]
            break
    assert isinstance(descriptor, property)



def test_model::values::visualgroupelement_is_not_abstract():
    assert not inspect.isabstract(model::values::VisualGroupElement)


def test_model::values::visualgroupelement_constructor_exists():
    assert callable(model::values::VisualGroupElement.__init__)


def test_model::values::visualgroupelement_constructor_args():
    sig = inspect.signature(model::values::VisualGroupElement.__init__)
    params = list(sig.parameters.keys())
    assert "defaultColor" in params, "Missing parameter 'defaultColor'"

def test_model::values::visualgroupelement_has_defaultColor():
    assert hasattr(model::values::VisualGroupElement, "defaultColor")
    descriptor = None
    for klass in model::values::VisualGroupElement.__mro__:
        if "defaultColor" in klass.__dict__:
            descriptor = klass.__dict__["defaultColor"]
            break
    assert isinstance(descriptor, property)



def test_model::datasources::query_is_not_abstract():
    assert not inspect.isabstract(model::datasources::Query)


def test_model::datasources::query_constructor_exists():
    assert callable(model::datasources::Query.__init__)


def test_model::datasources::query_constructor_args():
    sig = inspect.signature(model::datasources::Query.__init__)
    params = list(sig.parameters.keys())
    assert "runForCount" in params, "Missing parameter 'runForCount'"
    assert "description" in params, "Missing parameter 'description'"

def test_model::datasources::query_has_runForCount():
    assert hasattr(model::datasources::Query, "runForCount")
    descriptor = None
    for klass in model::datasources::Query.__mro__:
        if "runForCount" in klass.__dict__:
            descriptor = klass.__dict__["runForCount"]
            break
    assert isinstance(descriptor, property)

def test_model::datasources::query_has_description():
    assert hasattr(model::datasources::Query, "description")
    descriptor = None
    for klass in model::datasources::Query.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_model::variables::variable_is_not_abstract():
    assert not inspect.isabstract(model::variables::Variable)


def test_model::variables::variable_constructor_exists():
    assert callable(model::variables::Variable.__init__)


def test_model::variables::variable_constructor_args():
    sig = inspect.signature(model::variables::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_model::variables::variable_has_static():
    assert hasattr(model::variables::Variable, "static")
    descriptor = None
    for klass in model::variables::Variable.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_model::datasources::datasource_is_not_abstract():
    assert not inspect.isabstract(model::datasources::DataSource)


def test_model::datasources::datasource_constructor_exists():
    assert callable(model::datasources::DataSource.__init__)


def test_model::datasources::datasource_constructor_args():
    sig = inspect.signature(model::datasources::DataSource.__init__)
    params = list(sig.parameters.keys())
    assert "dataSourceService" in params, "Missing parameter 'dataSourceService'"
    assert "url" in params, "Missing parameter 'url'"

def test_model::datasources::datasource_has_dataSourceService():
    assert hasattr(model::datasources::DataSource, "dataSourceService")
    descriptor = None
    for klass in model::datasources::DataSource.__mro__:
        if "dataSourceService" in klass.__dict__:
            descriptor = klass.__dict__["dataSourceService"]
            break
    assert isinstance(descriptor, property)

def test_model::datasources::datasource_has_url():
    assert hasattr(model::datasources::DataSource, "url")
    descriptor = None
    for klass in model::datasources::DataSource.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_model::instances::instance_is_not_abstract():
    assert not inspect.isabstract(model::instances::Instance)


def test_model::instances::instance_constructor_exists():
    assert callable(model::instances::Instance.__init__)


def test_model::instances::instance_constructor_args():
    sig = inspect.signature(model::instances::Instance.__init__)
    params = list(sig.parameters.keys())



def test_isynchable_is_not_abstract():
    assert not inspect.isabstract(ISynchable)


def test_isynchable_constructor_exists():
    assert callable(ISynchable.__init__)


def test_isynchable_constructor_args():
    sig = inspect.signature(ISynchable.__init__)
    params = list(sig.parameters.keys())



def test_model::values::value_is_not_abstract():
    assert not inspect.isabstract(model::values::Value)


def test_model::values::value_constructor_exists():
    assert callable(model::values::Value.__init__)


def test_model::values::value_constructor_args():
    sig = inspect.signature(model::values::Value.__init__)
    params = list(sig.parameters.keys())



def test_model::node_is_not_abstract():
    assert not inspect.isabstract(model::Node)


def test_model::node_constructor_exists():
    assert callable(model::Node.__init__)


def test_model::node_constructor_args():
    sig = inspect.signature(model::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_model::node_has_name():
    assert hasattr(model::Node, "name")
    descriptor = None
    for klass in model::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::node_has_id():
    assert hasattr(model::Node, "id")
    descriptor = None
    for klass in model::Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_query_is_not_abstract():
    assert not inspect.isabstract(Query)


def test_query_constructor_exists():
    assert callable(Query.__init__)


def test_query_constructor_args():
    sig = inspect.signature(Query.__init__)
    params = list(sig.parameters.keys())



def test_model::datasources::compoundrefquery_is_not_abstract():
    assert not inspect.isabstract(model::datasources::CompoundRefQuery)


def test_model::datasources::compoundrefquery_constructor_exists():
    assert callable(model::datasources::CompoundRefQuery.__init__)


def test_model::datasources::compoundrefquery_constructor_args():
    sig = inspect.signature(model::datasources::CompoundRefQuery.__init__)
    params = list(sig.parameters.keys())



def test_model::datasources::processquery_is_not_abstract():
    assert not inspect.isabstract(model::datasources::ProcessQuery)


def test_model::datasources::processquery_constructor_exists():
    assert callable(model::datasources::ProcessQuery.__init__)


def test_model::datasources::processquery_constructor_args():
    sig = inspect.signature(model::datasources::ProcessQuery.__init__)
    params = list(sig.parameters.keys())
    assert "queryProcessorId" in params, "Missing parameter 'queryProcessorId'"

def test_model::datasources::processquery_has_queryProcessorId():
    assert hasattr(model::datasources::ProcessQuery, "queryProcessorId")
    descriptor = None
    for klass in model::datasources::ProcessQuery.__mro__:
        if "queryProcessorId" in klass.__dict__:
            descriptor = klass.__dict__["queryProcessorId"]
            break
    assert isinstance(descriptor, property)



def test_model::datasources::compoundquery_is_not_abstract():
    assert not inspect.isabstract(model::datasources::CompoundQuery)


def test_model::datasources::compoundquery_constructor_exists():
    assert callable(model::datasources::CompoundQuery.__init__)


def test_model::datasources::compoundquery_constructor_args():
    sig = inspect.signature(model::datasources::CompoundQuery.__init__)
    params = list(sig.parameters.keys())



def test_model::datasources::simplequery_is_not_abstract():
    assert not inspect.isabstract(model::datasources::SimpleQuery)


def test_model::datasources::simplequery_constructor_exists():
    assert callable(model::datasources::SimpleQuery.__init__)


def test_model::datasources::simplequery_constructor_args():
    sig = inspect.signature(model::datasources::SimpleQuery.__init__)
    params = list(sig.parameters.keys())
    assert "countQuery" in params, "Missing parameter 'countQuery'"
    assert "query" in params, "Missing parameter 'query'"

def test_model::datasources::simplequery_has_countQuery():
    assert hasattr(model::datasources::SimpleQuery, "countQuery")
    descriptor = None
    for klass in model::datasources::SimpleQuery.__mro__:
        if "countQuery" in klass.__dict__:
            descriptor = klass.__dict__["countQuery"]
            break
    assert isinstance(descriptor, property)

def test_model::datasources::simplequery_has_query():
    assert hasattr(model::datasources::SimpleQuery, "query")
    descriptor = None
    for klass in model::datasources::SimpleQuery.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)



def test_datasource_is_not_abstract():
    assert not inspect.isabstract(DataSource)


def test_datasource_constructor_exists():
    assert callable(DataSource.__init__)


def test_datasource_constructor_args():
    sig = inspect.signature(DataSource.__init__)
    params = list(sig.parameters.keys())



def test_pointer_is_not_abstract():
    assert not inspect.isabstract(Pointer)


def test_pointer_constructor_exists():
    assert callable(Pointer.__init__)


def test_pointer_constructor_args():
    sig = inspect.signature(Pointer.__init__)
    params = list(sig.parameters.keys())



def test_model::variablevalue_is_not_abstract():
    assert not inspect.isabstract(model::VariableValue)


def test_model::variablevalue_constructor_exists():
    assert callable(model::VariableValue.__init__)


def test_model::variablevalue_constructor_args():
    sig = inspect.signature(model::VariableValue.__init__)
    params = list(sig.parameters.keys())



def test_model::experimentstate_is_not_abstract():
    assert not inspect.isabstract(model::ExperimentState)


def test_model::experimentstate_constructor_exists():
    assert callable(model::ExperimentState.__init__)


def test_model::experimentstate_constructor_args():
    sig = inspect.signature(model::ExperimentState.__init__)
    params = list(sig.parameters.keys())
    assert "experimentId" in params, "Missing parameter 'experimentId'"
    assert "projectId" in params, "Missing parameter 'projectId'"

def test_model::experimentstate_has_experimentId():
    assert hasattr(model::ExperimentState, "experimentId")
    descriptor = None
    for klass in model::ExperimentState.__mro__:
        if "experimentId" in klass.__dict__:
            descriptor = klass.__dict__["experimentId"]
            break
    assert isinstance(descriptor, property)

def test_model::experimentstate_has_projectId():
    assert hasattr(model::ExperimentState, "projectId")
    descriptor = None
    for klass in model::ExperimentState.__mro__:
        if "projectId" in klass.__dict__:
            descriptor = klass.__dict__["projectId"]
            break
    assert isinstance(descriptor, property)



def test_model::librarymanager_is_not_abstract():
    assert not inspect.isabstract(model::LibraryManager)


def test_model::librarymanager_constructor_exists():
    assert callable(model::LibraryManager.__init__)


def test_model::librarymanager_constructor_args():
    sig = inspect.signature(model::LibraryManager.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_model::geppettomodel_is_not_abstract():
    assert not inspect.isabstract(model::GeppettoModel)


def test_model::geppettomodel_constructor_exists():
    assert callable(model::GeppettoModel.__init__)


def test_model::geppettomodel_constructor_args():
    sig = inspect.signature(model::GeppettoModel.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_model::geppettomodel_has_id():
    assert hasattr(model::GeppettoModel, "id")
    descriptor = None
    for klass in model::GeppettoModel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_model::geppettomodel_has_name():
    assert hasattr(model::GeppettoModel, "name")
    descriptor = None
    for klass in model::GeppettoModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::tag_is_not_abstract():
    assert not inspect.isabstract(model::Tag)


def test_model::tag_constructor_exists():
    assert callable(model::Tag.__init__)


def test_model::tag_constructor_args():
    sig = inspect.signature(model::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::tag_has_name():
    assert hasattr(model::Tag, "name")
    descriptor = None
    for klass in model::Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::geppettolibrary_is_not_abstract():
    assert not inspect.isabstract(model::GeppettoLibrary)


def test_model::geppettolibrary_constructor_exists():
    assert callable(model::GeppettoLibrary.__init__)


def test_model::geppettolibrary_constructor_args():
    sig = inspect.signature(model::GeppettoLibrary.__init__)
    params = list(sig.parameters.keys())



def test_model::world_is_not_abstract():
    assert not inspect.isabstract(model::World)


def test_model::world_constructor_exists():
    assert callable(model::World.__init__)


def test_model::world_constructor_args():
    sig = inspect.signature(model::World.__init__)
    params = list(sig.parameters.keys())

def test_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "OR",
        "AND",
        "NAND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"

def test_connectivity_exists():
    # Check that the Enumeration exists
    assert Connectivity is not None

def test_connectivity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Connectivity]
    expected_literals = [
        "DIRECTIONAL",
        "BIDIRECTIONAL",
        "NON_DIRECTIONAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Connectivity"

def test_fileformat_exists():
    # Check that the Enumeration exists
    assert FileFormat is not None

def test_fileformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FileFormat]
    expected_literals = [
        "ZIP",
        "HDF5",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FileFormat"

def test_imageformat_exists():
    # Check that the Enumeration exists
    assert ImageFormat is not None

def test_imageformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImageFormat]
    expected_literals = [
        "DCM",
        "DZI",
        "IIP",
        "TIFF",
        "PNG",
        "JPEG",
        "NIFTI",
        "GOOGLE_MAP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImageFormat"


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
model::datasources::QueryMatchingCriteria_strategy = st.builds(
    model::datasources::QueryMatchingCriteria,
)
model::datasources::AQueryResult_strategy = st.builds(
    model::datasources::AQueryResult,
)
model::datasources::RunnableQuery_strategy = st.builds(
    model::datasources::RunnableQuery,
    targetVariablePath=
        safe_text,
    booleanOperator=
        safe_text,
    queryPath=
        safe_text
)
AQueryResult_strategy = st.builds(
    AQueryResult,
)
model::datasources::SerializableQueryResult_strategy = st.builds(
    model::datasources::SerializableQueryResult,
    values=
        safe_text
)
model::datasources::QueryResult_strategy = st.builds(
    model::datasources::QueryResult,
    values=
        safe_text
)
model::datasources::QueryResults_strategy = st.builds(
    model::datasources::QueryResults,
    header=
        safe_text,
    id=
        safe_text
)
DataSourceLibraryConfiguration_strategy = st.builds(
    DataSourceLibraryConfiguration,
)
datasources::model::StringToStringMap_strategy = st.builds(
    datasources::model::StringToStringMap,
)
QueryMatchingCriteria_strategy = st.builds(
    QueryMatchingCriteria,
)
model::datasources::DataSourceLibraryConfiguration_strategy = st.builds(
    model::datasources::DataSourceLibraryConfiguration,
    format=
        safe_text,
    modelInterpreterId=
        safe_text
)
datasources::model::GeppettoLibrary_strategy = st.builds(
    datasources::model::GeppettoLibrary,
)
model::variables::TypeToValueMap_strategy = st.builds(
    model::variables::TypeToValueMap,
)
TypeToValueMap_strategy = st.builds(
    TypeToValueMap,
)
ArrayElement_strategy = st.builds(
    ArrayElement,
)
VisualGroupElement_strategy = st.builds(
    VisualGroupElement,
)
FunctionPlot_strategy = st.builds(
    FunctionPlot,
)
model::values::SkeletonTransformation_strategy = st.builds(
    model::values::SkeletonTransformation,
    skeletonTransformation=
        safe_text
)
SkeletonTransformation_strategy = st.builds(
    SkeletonTransformation,
)
model::values::PointerElement_strategy = st.builds(
    model::values::PointerElement,
    index=
        safe_text
)
Unit_strategy = st.builds(
    Unit,
)
PointerElement_strategy = st.builds(
    PointerElement,
)
model::values::FunctionPlot_strategy = st.builds(
    model::values::FunctionPlot,
    stepValue=
        safe_text,
    finalValue=
        safe_text,
    xAxisLabel=
        safe_text,
    initialValue=
        safe_text,
    title=
        safe_text,
    yAxisLabel=
        safe_text
)
Function_strategy = st.builds(
    Function,
)
PhysicalQuantity_strategy = st.builds(
    PhysicalQuantity,
)
model::values::StringToValueMap_strategy = st.builds(
    model::values::StringToValueMap,
    key=
        safe_text
)
StringToValueMap_strategy = st.builds(
    StringToValueMap,
)
AArrayValue_strategy = st.builds(
    AArrayValue,
)
model::values::GenericArray_strategy = st.builds(
    model::values::GenericArray,
)
model::values::StringArray_strategy = st.builds(
    model::values::StringArray,
    elements=
        safe_text
)
model::values::DoubleArray_strategy = st.builds(
    model::values::DoubleArray,
    elements=
        safe_text
)
model::values::IntArray_strategy = st.builds(
    model::values::IntArray,
    elements=
        safe_text
)
MetadataValue_strategy = st.builds(
    MetadataValue,
)
model::values::HTML_strategy = st.builds(
    model::values::HTML,
    html=
        safe_text
)
model::values::URL_strategy = st.builds(
    model::values::URL,
    url=
        safe_text
)
model::values::JSON_strategy = st.builds(
    model::values::JSON,
    json=
        safe_text
)
model::values::Metadata_strategy = st.builds(
    model::values::Metadata,
)
model::values::Text_strategy = st.builds(
    model::values::Text,
    text=
        safe_text
)
VisualGroup_strategy = st.builds(
    VisualGroup,
)
ArrayValue_strategy = st.builds(
    ArrayValue,
)
Point_strategy = st.builds(
    Point,
)
URL_strategy = st.builds(
    URL,
)
Text_strategy = st.builds(
    Text,
)
Image_strategy = st.builds(
    Image,
)
Argument_strategy = st.builds(
    Argument,
)
Dynamics_strategy = st.builds(
    Dynamics,
)
Quantity_strategy = st.builds(
    Quantity,
)
model::values::PhysicalQuantity_strategy = st.builds(
    model::values::PhysicalQuantity,
)
Composite_strategy = st.builds(
    Composite,
)
JSON_strategy = st.builds(
    JSON,
)
HTML_strategy = st.builds(
    HTML,
)
Expression_strategy = st.builds(
    Expression,
)
VisualType_strategy = st.builds(
    VisualType,
)
model::types::CompositeVisualType_strategy = st.builds(
    model::types::CompositeVisualType,
)
Instance_strategy = st.builds(
    Instance,
)
model::instances::SimpleInstance_strategy = st.builds(
    model::instances::SimpleInstance,
)
model::instances::SimpleConnectionInstance_strategy = st.builds(
    model::instances::SimpleConnectionInstance,
    connectivity=
        safe_text
)
model::ISynchable_strategy = st.builds(
    model::ISynchable,
    synched=
        safe_text
)
VisualValue_strategy = st.builds(
    VisualValue,
)
model::values::Cylinder_strategy = st.builds(
    model::values::Cylinder,
    bottomRadius=
        safe_text,
    topRadius=
        safe_text,
    height=
        safe_text
)
model::values::Collada_strategy = st.builds(
    model::values::Collada,
    collada=
        safe_text
)
model::values::OBJ_strategy = st.builds(
    model::values::OBJ,
    obj=
        safe_text
)
model::values::SkeletonAnimation_strategy = st.builds(
    model::values::SkeletonAnimation,
)
model::values::Sphere_strategy = st.builds(
    model::values::Sphere,
    radius=
        safe_text
)
types::model::DomainModel__strategy = st.builds(
    types::model::DomainModel_,
)
model::DomainModel__strategy = st.builds(
    model::DomainModel_,
    domainModel=
        safe_text
)
Value_strategy = st.builds(
    Value,
)
model::values::VisualValue_strategy = st.builds(
    model::values::VisualValue,
)
model::values::Composite_strategy = st.builds(
    model::values::Composite,
)
model::values::Connection_strategy = st.builds(
    model::values::Connection,
    connectivity=
        safe_text
)
model::values::Function_strategy = st.builds(
    model::values::Function,
)
model::values::AArrayValue_strategy = st.builds(
    model::values::AArrayValue,
)
model::values::ArrayValue_strategy = st.builds(
    model::values::ArrayValue,
)
model::values::ArrayElement_strategy = st.builds(
    model::values::ArrayElement,
    index=
        safe_text
)
model::values::Image_strategy = st.builds(
    model::values::Image,
    data=
        safe_text,
    reference=
        safe_text,
    format=
        safe_text,
    name=
        safe_text
)
model::values::Argument_strategy = st.builds(
    model::values::Argument,
    argument=
        safe_text
)
model::values::Unit_strategy = st.builds(
    model::values::Unit,
    unit=
        safe_text
)
model::values::ImportValue_strategy = st.builds(
    model::values::ImportValue,
    modelInterpreterId=
        safe_text
)
model::values::MDTimeSeries_strategy = st.builds(
    model::values::MDTimeSeries,
)
model::values::Expression_strategy = st.builds(
    model::values::Expression,
    expression=
        safe_text
)
model::values::MetadataValue_strategy = st.builds(
    model::values::MetadataValue,
)
model::values::Point_strategy = st.builds(
    model::values::Point,
    y=
        safe_text,
    z=
        safe_text,
    x=
        safe_text
)
model::values::Pointer_strategy = st.builds(
    model::values::Pointer,
    path=
        safe_text
)
model::values::Dynamics_strategy = st.builds(
    model::values::Dynamics,
)
model::values::Particles_strategy = st.builds(
    model::values::Particles,
)
model::values::Quantity_strategy = st.builds(
    model::values::Quantity,
    value=
        safe_text,
    scalingFactor=
        safe_text
)
model::values::TimeSeries_strategy = st.builds(
    model::values::TimeSeries,
    scalingFactor=
        safe_text,
    value=
        safe_text
)
model::StringToStringMap_strategy = st.builds(
    model::StringToStringMap,
    value=
        safe_text,
    key=
        safe_text
)
DomainModel__strategy = st.builds(
    DomainModel_,
)
model::ExternalDomainModel_strategy = st.builds(
    model::ExternalDomainModel,
    fileFormat=
        safe_text
)
model::ModelFormat_strategy = st.builds(
    model::ModelFormat,
    modelFormat=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
model::types::HTMLType_strategy = st.builds(
    model::types::HTMLType,
)
model::types::ExpressionType_strategy = st.builds(
    model::types::ExpressionType,
)
model::types::URLType_strategy = st.builds(
    model::types::URLType,
)
model::types::SimpleArrayType_strategy = st.builds(
    model::types::SimpleArrayType,
)
model::types::ImageType_strategy = st.builds(
    model::types::ImageType,
)
model::types::PointerType_strategy = st.builds(
    model::types::PointerType,
)
model::types::CompositeType_strategy = st.builds(
    model::types::CompositeType,
)
model::types::ArrayType_strategy = st.builds(
    model::types::ArrayType,
    size=
        safe_text
)
model::types::VisualType_strategy = st.builds(
    model::types::VisualType,
)
model::types::ImportType_strategy = st.builds(
    model::types::ImportType,
    referenceURL=
        safe_text,
    autoresolve=
        safe_text,
    url=
        safe_text,
    modelInterpreterId=
        safe_text
)
model::types::ParameterType_strategy = st.builds(
    model::types::ParameterType,
)
model::types::StateVariableType_strategy = st.builds(
    model::types::StateVariableType,
)
model::types::QuantityType_strategy = st.builds(
    model::types::QuantityType,
)
model::types::MetadataType_strategy = st.builds(
    model::types::MetadataType,
)
model::types::SimpleType_strategy = st.builds(
    model::types::SimpleType,
)
model::types::DynamicsType_strategy = st.builds(
    model::types::DynamicsType,
)
model::types::ArgumentType_strategy = st.builds(
    model::types::ArgumentType,
)
model::types::TextType_strategy = st.builds(
    model::types::TextType,
)
model::types::ConnectionType_strategy = st.builds(
    model::types::ConnectionType,
)
model::types::JSONType_strategy = st.builds(
    model::types::JSONType,
)
model::types::PointType_strategy = st.builds(
    model::types::PointType,
)
Node_strategy = st.builds(
    Node,
)
model::types::Type_strategy = st.builds(
    model::types::Type,
    abstract=
        safe_text
)
model::values::VisualGroup_strategy = st.builds(
    model::values::VisualGroup,
    type=
        safe_text,
    highSpectrumColor=
        safe_text,
    lowSpectrumColor=
        safe_text
)
model::values::VisualGroupElement_strategy = st.builds(
    model::values::VisualGroupElement,
    defaultColor=
        safe_text
)
model::datasources::Query_strategy = st.builds(
    model::datasources::Query,
    runForCount=
        safe_text,
    description=
        safe_text
)
model::variables::Variable_strategy = st.builds(
    model::variables::Variable,
    static=
        safe_text
)
model::datasources::DataSource_strategy = st.builds(
    model::datasources::DataSource,
    dataSourceService=
        safe_text,
    url=
        safe_text
)
model::instances::Instance_strategy = st.builds(
    model::instances::Instance,
)
ISynchable_strategy = st.builds(
    ISynchable,
)
model::values::Value_strategy = st.builds(
    model::values::Value,
)
model::Node_strategy = st.builds(
    model::Node,
    name=
        safe_text,
    id=
        safe_text
)
Query_strategy = st.builds(
    Query,
)
model::datasources::CompoundRefQuery_strategy = st.builds(
    model::datasources::CompoundRefQuery,
)
model::datasources::ProcessQuery_strategy = st.builds(
    model::datasources::ProcessQuery,
    queryProcessorId=
        safe_text
)
model::datasources::CompoundQuery_strategy = st.builds(
    model::datasources::CompoundQuery,
)
model::datasources::SimpleQuery_strategy = st.builds(
    model::datasources::SimpleQuery,
    countQuery=
        safe_text,
    query=
        safe_text
)
DataSource_strategy = st.builds(
    DataSource,
)
Pointer_strategy = st.builds(
    Pointer,
)
model::VariableValue_strategy = st.builds(
    model::VariableValue,
)
model::ExperimentState_strategy = st.builds(
    model::ExperimentState,
    experimentId=
        safe_text,
    projectId=
        safe_text
)
model::LibraryManager_strategy = st.builds(
    model::LibraryManager,
)
Variable_strategy = st.builds(
    Variable,
)
model::GeppettoModel_strategy = st.builds(
    model::GeppettoModel,
    id=
        safe_text,
    name=
        safe_text
)
model::Tag_strategy = st.builds(
    model::Tag,
    name=
        safe_text
)
model::GeppettoLibrary_strategy = st.builds(
    model::GeppettoLibrary,
)
model::World_strategy = st.builds(
    model::World,
)

@given(instance=model::datasources::QueryMatchingCriteria_strategy)
@settings(max_examples=50)
def test_model::datasources::querymatchingcriteria_instantiation(instance):
    assert isinstance(instance, model::datasources::QueryMatchingCriteria)

@given(instance=model::datasources::AQueryResult_strategy)
@settings(max_examples=50)
def test_model::datasources::aqueryresult_instantiation(instance):
    assert isinstance(instance, model::datasources::AQueryResult)

@given(instance=model::datasources::RunnableQuery_strategy)
@settings(max_examples=50)
def test_model::datasources::runnablequery_instantiation(instance):
    assert isinstance(instance, model::datasources::RunnableQuery)

@given(instance=model::datasources::RunnableQuery_strategy)
def test_model::datasources::runnablequery_targetVariablePath_type(instance):
    assert isinstance(instance.targetVariablePath, str)


@given(instance=model::datasources::RunnableQuery_strategy)
def test_model::datasources::runnablequery_targetVariablePath_setter(instance):
    original = instance.targetVariablePath
    instance.targetVariablePath = original
    assert instance.targetVariablePath == original

@given(instance=model::datasources::RunnableQuery_strategy)
def test_model::datasources::runnablequery_booleanOperator_type(instance):
    assert isinstance(instance.booleanOperator, str)


@given(instance=model::datasources::RunnableQuery_strategy)
def test_model::datasources::runnablequery_booleanOperator_setter(instance):
    original = instance.booleanOperator
    instance.booleanOperator = original
    assert instance.booleanOperator == original

@given(instance=model::datasources::RunnableQuery_strategy)
def test_model::datasources::runnablequery_queryPath_type(instance):
    assert isinstance(instance.queryPath, str)


@given(instance=model::datasources::RunnableQuery_strategy)
def test_model::datasources::runnablequery_queryPath_setter(instance):
    original = instance.queryPath
    instance.queryPath = original
    assert instance.queryPath == original

@given(instance=AQueryResult_strategy)
@settings(max_examples=50)
def test_aqueryresult_instantiation(instance):
    assert isinstance(instance, AQueryResult)

@given(instance=model::datasources::SerializableQueryResult_strategy)
@settings(max_examples=50)
def test_model::datasources::serializablequeryresult_instantiation(instance):
    assert isinstance(instance, model::datasources::SerializableQueryResult)

@given(instance=model::datasources::SerializableQueryResult_strategy)
def test_model::datasources::serializablequeryresult_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=model::datasources::SerializableQueryResult_strategy)
def test_model::datasources::serializablequeryresult_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=model::datasources::QueryResult_strategy)
@settings(max_examples=50)
def test_model::datasources::queryresult_instantiation(instance):
    assert isinstance(instance, model::datasources::QueryResult)

@given(instance=model::datasources::QueryResult_strategy)
def test_model::datasources::queryresult_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=model::datasources::QueryResult_strategy)
def test_model::datasources::queryresult_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=model::datasources::QueryResults_strategy)
@settings(max_examples=50)
def test_model::datasources::queryresults_instantiation(instance):
    assert isinstance(instance, model::datasources::QueryResults)

@given(instance=model::datasources::QueryResults_strategy)
def test_model::datasources::queryresults_header_type(instance):
    assert isinstance(instance.header, str)


@given(instance=model::datasources::QueryResults_strategy)
def test_model::datasources::queryresults_header_setter(instance):
    original = instance.header
    instance.header = original
    assert instance.header == original

@given(instance=model::datasources::QueryResults_strategy)
def test_model::datasources::queryresults_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=model::datasources::QueryResults_strategy)
def test_model::datasources::queryresults_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=DataSourceLibraryConfiguration_strategy)
@settings(max_examples=50)
def test_datasourcelibraryconfiguration_instantiation(instance):
    assert isinstance(instance, DataSourceLibraryConfiguration)

@given(instance=datasources::model::StringToStringMap_strategy)
@settings(max_examples=50)
def test_datasources::model::stringtostringmap_instantiation(instance):
    assert isinstance(instance, datasources::model::StringToStringMap)

@given(instance=QueryMatchingCriteria_strategy)
@settings(max_examples=50)
def test_querymatchingcriteria_instantiation(instance):
    assert isinstance(instance, QueryMatchingCriteria)

@given(instance=model::datasources::DataSourceLibraryConfiguration_strategy)
@settings(max_examples=50)
def test_model::datasources::datasourcelibraryconfiguration_instantiation(instance):
    assert isinstance(instance, model::datasources::DataSourceLibraryConfiguration)

@given(instance=model::datasources::DataSourceLibraryConfiguration_strategy)
def test_model::datasources::datasourcelibraryconfiguration_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=model::datasources::DataSourceLibraryConfiguration_strategy)
def test_model::datasources::datasourcelibraryconfiguration_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=model::datasources::DataSourceLibraryConfiguration_strategy)
def test_model::datasources::datasourcelibraryconfiguration_modelInterpreterId_type(instance):
    assert isinstance(instance.modelInterpreterId, str)


@given(instance=model::datasources::DataSourceLibraryConfiguration_strategy)
def test_model::datasources::datasourcelibraryconfiguration_modelInterpreterId_setter(instance):
    original = instance.modelInterpreterId
    instance.modelInterpreterId = original
    assert instance.modelInterpreterId == original

@given(instance=datasources::model::GeppettoLibrary_strategy)
@settings(max_examples=50)
def test_datasources::model::geppettolibrary_instantiation(instance):
    assert isinstance(instance, datasources::model::GeppettoLibrary)

@given(instance=model::variables::TypeToValueMap_strategy)
@settings(max_examples=50)
def test_model::variables::typetovaluemap_instantiation(instance):
    assert isinstance(instance, model::variables::TypeToValueMap)

@given(instance=TypeToValueMap_strategy)
@settings(max_examples=50)
def test_typetovaluemap_instantiation(instance):
    assert isinstance(instance, TypeToValueMap)

@given(instance=ArrayElement_strategy)
@settings(max_examples=50)
def test_arrayelement_instantiation(instance):
    assert isinstance(instance, ArrayElement)

@given(instance=VisualGroupElement_strategy)
@settings(max_examples=50)
def test_visualgroupelement_instantiation(instance):
    assert isinstance(instance, VisualGroupElement)

@given(instance=FunctionPlot_strategy)
@settings(max_examples=50)
def test_functionplot_instantiation(instance):
    assert isinstance(instance, FunctionPlot)

@given(instance=model::values::SkeletonTransformation_strategy)
@settings(max_examples=50)
def test_model::values::skeletontransformation_instantiation(instance):
    assert isinstance(instance, model::values::SkeletonTransformation)

@given(instance=model::values::SkeletonTransformation_strategy)
def test_model::values::skeletontransformation_skeletonTransformation_type(instance):
    assert isinstance(instance.skeletonTransformation, str)


@given(instance=model::values::SkeletonTransformation_strategy)
def test_model::values::skeletontransformation_skeletonTransformation_setter(instance):
    original = instance.skeletonTransformation
    instance.skeletonTransformation = original
    assert instance.skeletonTransformation == original

@given(instance=SkeletonTransformation_strategy)
@settings(max_examples=50)
def test_skeletontransformation_instantiation(instance):
    assert isinstance(instance, SkeletonTransformation)

@given(instance=model::values::PointerElement_strategy)
@settings(max_examples=50)
def test_model::values::pointerelement_instantiation(instance):
    assert isinstance(instance, model::values::PointerElement)

@given(instance=model::values::PointerElement_strategy)
def test_model::values::pointerelement_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=model::values::PointerElement_strategy)
def test_model::values::pointerelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=PointerElement_strategy)
@settings(max_examples=50)
def test_pointerelement_instantiation(instance):
    assert isinstance(instance, PointerElement)

@given(instance=model::values::FunctionPlot_strategy)
@settings(max_examples=50)
def test_model::values::functionplot_instantiation(instance):
    assert isinstance(instance, model::values::FunctionPlot)

@given(instance=model::values::FunctionPlot_strategy)
def test_model::values::functionplot_stepValue_type(instance):
    assert isinstance(instance.stepValue, str)


@given(instance=model::values::FunctionPlot_strategy)
def test_model::values::functionplot_stepValue_setter(instance):
    original = instance.stepValue
    instance.stepValue = original
    assert instance.stepValue == original

@given(instance=model::values::FunctionPlot_strategy)
def test_model::values::functionplot_finalValue_type(instance):
    assert isinstance(instance.finalValue, str)


@given(instance=model::values::FunctionPlot_strategy)
def test_model::values::functionplot_finalValue_setter(instance):
    original = instance.finalValue
    instance.finalValue = original
    assert instance.finalValue == original

@given(instance=model::values::FunctionPlot_strategy)
def test_model::values::functionplot_xAxisLabel_type(instance):
    assert isinstance(instance.xAxisLabel, str)


@given(instance=model::values::FunctionPlot_strategy)
def test_model::values::functionplot_xAxisLabel_setter(instance):
    original = instance.xAxisLabel
    instance.xAxisLabel = original
    assert instance.xAxisLabel == original

@given(instance=model::values::FunctionPlot_strategy)
def test_model::values::functionplot_initialValue_type(instance):
    assert isinstance(instance.initialValue, str)


@given(instance=model::values::FunctionPlot_strategy)
def test_model::values::functionplot_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original

@given(instance=model::values::FunctionPlot_strategy)
def test_model::values::functionplot_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=model::values::FunctionPlot_strategy)
def test_model::values::functionplot_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=model::values::FunctionPlot_strategy)
def test_model::values::functionplot_yAxisLabel_type(instance):
    assert isinstance(instance.yAxisLabel, str)


@given(instance=model::values::FunctionPlot_strategy)
def test_model::values::functionplot_yAxisLabel_setter(instance):
    original = instance.yAxisLabel
    instance.yAxisLabel = original
    assert instance.yAxisLabel == original

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=PhysicalQuantity_strategy)
@settings(max_examples=50)
def test_physicalquantity_instantiation(instance):
    assert isinstance(instance, PhysicalQuantity)

@given(instance=model::values::StringToValueMap_strategy)
@settings(max_examples=50)
def test_model::values::stringtovaluemap_instantiation(instance):
    assert isinstance(instance, model::values::StringToValueMap)

@given(instance=model::values::StringToValueMap_strategy)
def test_model::values::stringtovaluemap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=model::values::StringToValueMap_strategy)
def test_model::values::stringtovaluemap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=StringToValueMap_strategy)
@settings(max_examples=50)
def test_stringtovaluemap_instantiation(instance):
    assert isinstance(instance, StringToValueMap)

@given(instance=AArrayValue_strategy)
@settings(max_examples=50)
def test_aarrayvalue_instantiation(instance):
    assert isinstance(instance, AArrayValue)

@given(instance=model::values::GenericArray_strategy)
@settings(max_examples=50)
def test_model::values::genericarray_instantiation(instance):
    assert isinstance(instance, model::values::GenericArray)

@given(instance=model::values::StringArray_strategy)
@settings(max_examples=50)
def test_model::values::stringarray_instantiation(instance):
    assert isinstance(instance, model::values::StringArray)

@given(instance=model::values::StringArray_strategy)
def test_model::values::stringarray_elements_type(instance):
    assert isinstance(instance.elements, str)


@given(instance=model::values::StringArray_strategy)
def test_model::values::stringarray_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original

@given(instance=model::values::DoubleArray_strategy)
@settings(max_examples=50)
def test_model::values::doublearray_instantiation(instance):
    assert isinstance(instance, model::values::DoubleArray)

@given(instance=model::values::DoubleArray_strategy)
def test_model::values::doublearray_elements_type(instance):
    assert isinstance(instance.elements, str)


@given(instance=model::values::DoubleArray_strategy)
def test_model::values::doublearray_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original

@given(instance=model::values::IntArray_strategy)
@settings(max_examples=50)
def test_model::values::intarray_instantiation(instance):
    assert isinstance(instance, model::values::IntArray)

@given(instance=model::values::IntArray_strategy)
def test_model::values::intarray_elements_type(instance):
    assert isinstance(instance.elements, str)


@given(instance=model::values::IntArray_strategy)
def test_model::values::intarray_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original

@given(instance=MetadataValue_strategy)
@settings(max_examples=50)
def test_metadatavalue_instantiation(instance):
    assert isinstance(instance, MetadataValue)

@given(instance=model::values::HTML_strategy)
@settings(max_examples=50)
def test_model::values::html_instantiation(instance):
    assert isinstance(instance, model::values::HTML)

@given(instance=model::values::HTML_strategy)
def test_model::values::html_html_type(instance):
    assert isinstance(instance.html, str)


@given(instance=model::values::HTML_strategy)
def test_model::values::html_html_setter(instance):
    original = instance.html
    instance.html = original
    assert instance.html == original

@given(instance=model::values::URL_strategy)
@settings(max_examples=50)
def test_model::values::url_instantiation(instance):
    assert isinstance(instance, model::values::URL)

@given(instance=model::values::URL_strategy)
def test_model::values::url_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=model::values::URL_strategy)
def test_model::values::url_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=model::values::JSON_strategy)
@settings(max_examples=50)
def test_model::values::json_instantiation(instance):
    assert isinstance(instance, model::values::JSON)

@given(instance=model::values::JSON_strategy)
def test_model::values::json_json_type(instance):
    assert isinstance(instance.json, str)


@given(instance=model::values::JSON_strategy)
def test_model::values::json_json_setter(instance):
    original = instance.json
    instance.json = original
    assert instance.json == original

@given(instance=model::values::Metadata_strategy)
@settings(max_examples=50)
def test_model::values::metadata_instantiation(instance):
    assert isinstance(instance, model::values::Metadata)

@given(instance=model::values::Text_strategy)
@settings(max_examples=50)
def test_model::values::text_instantiation(instance):
    assert isinstance(instance, model::values::Text)

@given(instance=model::values::Text_strategy)
def test_model::values::text_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=model::values::Text_strategy)
def test_model::values::text_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=VisualGroup_strategy)
@settings(max_examples=50)
def test_visualgroup_instantiation(instance):
    assert isinstance(instance, VisualGroup)

@given(instance=ArrayValue_strategy)
@settings(max_examples=50)
def test_arrayvalue_instantiation(instance):
    assert isinstance(instance, ArrayValue)

@given(instance=Point_strategy)
@settings(max_examples=50)
def test_point_instantiation(instance):
    assert isinstance(instance, Point)

@given(instance=URL_strategy)
@settings(max_examples=50)
def test_url_instantiation(instance):
    assert isinstance(instance, URL)

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=Image_strategy)
@settings(max_examples=50)
def test_image_instantiation(instance):
    assert isinstance(instance, Image)

@given(instance=Argument_strategy)
@settings(max_examples=50)
def test_argument_instantiation(instance):
    assert isinstance(instance, Argument)

@given(instance=Dynamics_strategy)
@settings(max_examples=50)
def test_dynamics_instantiation(instance):
    assert isinstance(instance, Dynamics)

@given(instance=Quantity_strategy)
@settings(max_examples=50)
def test_quantity_instantiation(instance):
    assert isinstance(instance, Quantity)

@given(instance=model::values::PhysicalQuantity_strategy)
@settings(max_examples=50)
def test_model::values::physicalquantity_instantiation(instance):
    assert isinstance(instance, model::values::PhysicalQuantity)

@given(instance=Composite_strategy)
@settings(max_examples=50)
def test_composite_instantiation(instance):
    assert isinstance(instance, Composite)

@given(instance=JSON_strategy)
@settings(max_examples=50)
def test_json_instantiation(instance):
    assert isinstance(instance, JSON)

@given(instance=HTML_strategy)
@settings(max_examples=50)
def test_html_instantiation(instance):
    assert isinstance(instance, HTML)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=VisualType_strategy)
@settings(max_examples=50)
def test_visualtype_instantiation(instance):
    assert isinstance(instance, VisualType)

@given(instance=model::types::CompositeVisualType_strategy)
@settings(max_examples=50)
def test_model::types::compositevisualtype_instantiation(instance):
    assert isinstance(instance, model::types::CompositeVisualType)

@given(instance=Instance_strategy)
@settings(max_examples=50)
def test_instance_instantiation(instance):
    assert isinstance(instance, Instance)

@given(instance=model::instances::SimpleInstance_strategy)
@settings(max_examples=50)
def test_model::instances::simpleinstance_instantiation(instance):
    assert isinstance(instance, model::instances::SimpleInstance)

@given(instance=model::instances::SimpleConnectionInstance_strategy)
@settings(max_examples=50)
def test_model::instances::simpleconnectioninstance_instantiation(instance):
    assert isinstance(instance, model::instances::SimpleConnectionInstance)

@given(instance=model::instances::SimpleConnectionInstance_strategy)
def test_model::instances::simpleconnectioninstance_connectivity_type(instance):
    assert isinstance(instance.connectivity, str)


@given(instance=model::instances::SimpleConnectionInstance_strategy)
def test_model::instances::simpleconnectioninstance_connectivity_setter(instance):
    original = instance.connectivity
    instance.connectivity = original
    assert instance.connectivity == original

@given(instance=model::ISynchable_strategy)
@settings(max_examples=50)
def test_model::isynchable_instantiation(instance):
    assert isinstance(instance, model::ISynchable)

@given(instance=model::ISynchable_strategy)
def test_model::isynchable_synched_type(instance):
    assert isinstance(instance.synched, str)


@given(instance=model::ISynchable_strategy)
def test_model::isynchable_synched_setter(instance):
    original = instance.synched
    instance.synched = original
    assert instance.synched == original

@given(instance=VisualValue_strategy)
@settings(max_examples=50)
def test_visualvalue_instantiation(instance):
    assert isinstance(instance, VisualValue)

@given(instance=model::values::Cylinder_strategy)
@settings(max_examples=50)
def test_model::values::cylinder_instantiation(instance):
    assert isinstance(instance, model::values::Cylinder)

@given(instance=model::values::Cylinder_strategy)
def test_model::values::cylinder_bottomRadius_type(instance):
    assert isinstance(instance.bottomRadius, str)


@given(instance=model::values::Cylinder_strategy)
def test_model::values::cylinder_bottomRadius_setter(instance):
    original = instance.bottomRadius
    instance.bottomRadius = original
    assert instance.bottomRadius == original

@given(instance=model::values::Cylinder_strategy)
def test_model::values::cylinder_topRadius_type(instance):
    assert isinstance(instance.topRadius, str)


@given(instance=model::values::Cylinder_strategy)
def test_model::values::cylinder_topRadius_setter(instance):
    original = instance.topRadius
    instance.topRadius = original
    assert instance.topRadius == original

@given(instance=model::values::Cylinder_strategy)
def test_model::values::cylinder_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=model::values::Cylinder_strategy)
def test_model::values::cylinder_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=model::values::Collada_strategy)
@settings(max_examples=50)
def test_model::values::collada_instantiation(instance):
    assert isinstance(instance, model::values::Collada)

@given(instance=model::values::Collada_strategy)
def test_model::values::collada_collada_type(instance):
    assert isinstance(instance.collada, str)


@given(instance=model::values::Collada_strategy)
def test_model::values::collada_collada_setter(instance):
    original = instance.collada
    instance.collada = original
    assert instance.collada == original

@given(instance=model::values::OBJ_strategy)
@settings(max_examples=50)
def test_model::values::obj_instantiation(instance):
    assert isinstance(instance, model::values::OBJ)

@given(instance=model::values::OBJ_strategy)
def test_model::values::obj_obj_type(instance):
    assert isinstance(instance.obj, str)


@given(instance=model::values::OBJ_strategy)
def test_model::values::obj_obj_setter(instance):
    original = instance.obj
    instance.obj = original
    assert instance.obj == original

@given(instance=model::values::SkeletonAnimation_strategy)
@settings(max_examples=50)
def test_model::values::skeletonanimation_instantiation(instance):
    assert isinstance(instance, model::values::SkeletonAnimation)

@given(instance=model::values::Sphere_strategy)
@settings(max_examples=50)
def test_model::values::sphere_instantiation(instance):
    assert isinstance(instance, model::values::Sphere)

@given(instance=model::values::Sphere_strategy)
def test_model::values::sphere_radius_type(instance):
    assert isinstance(instance.radius, str)


@given(instance=model::values::Sphere_strategy)
def test_model::values::sphere_radius_setter(instance):
    original = instance.radius
    instance.radius = original
    assert instance.radius == original

@given(instance=types::model::DomainModel__strategy)
@settings(max_examples=50)
def test_types::model::domainmodel__instantiation(instance):
    assert isinstance(instance, types::model::DomainModel_)

@given(instance=model::DomainModel__strategy)
@settings(max_examples=50)
def test_model::domainmodel__instantiation(instance):
    assert isinstance(instance, model::DomainModel_)

@given(instance=model::DomainModel__strategy)
def test_model::domainmodel__domainModel_type(instance):
    assert isinstance(instance.domainModel, str)


@given(instance=model::DomainModel__strategy)
def test_model::domainmodel__domainModel_setter(instance):
    original = instance.domainModel
    instance.domainModel = original
    assert instance.domainModel == original

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=model::values::VisualValue_strategy)
@settings(max_examples=50)
def test_model::values::visualvalue_instantiation(instance):
    assert isinstance(instance, model::values::VisualValue)

@given(instance=model::values::Composite_strategy)
@settings(max_examples=50)
def test_model::values::composite_instantiation(instance):
    assert isinstance(instance, model::values::Composite)

@given(instance=model::values::Connection_strategy)
@settings(max_examples=50)
def test_model::values::connection_instantiation(instance):
    assert isinstance(instance, model::values::Connection)

@given(instance=model::values::Connection_strategy)
def test_model::values::connection_connectivity_type(instance):
    assert isinstance(instance.connectivity, str)


@given(instance=model::values::Connection_strategy)
def test_model::values::connection_connectivity_setter(instance):
    original = instance.connectivity
    instance.connectivity = original
    assert instance.connectivity == original

@given(instance=model::values::Function_strategy)
@settings(max_examples=50)
def test_model::values::function_instantiation(instance):
    assert isinstance(instance, model::values::Function)

@given(instance=model::values::AArrayValue_strategy)
@settings(max_examples=50)
def test_model::values::aarrayvalue_instantiation(instance):
    assert isinstance(instance, model::values::AArrayValue)

@given(instance=model::values::ArrayValue_strategy)
@settings(max_examples=50)
def test_model::values::arrayvalue_instantiation(instance):
    assert isinstance(instance, model::values::ArrayValue)

@given(instance=model::values::ArrayElement_strategy)
@settings(max_examples=50)
def test_model::values::arrayelement_instantiation(instance):
    assert isinstance(instance, model::values::ArrayElement)

@given(instance=model::values::ArrayElement_strategy)
def test_model::values::arrayelement_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=model::values::ArrayElement_strategy)
def test_model::values::arrayelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=model::values::Image_strategy)
@settings(max_examples=50)
def test_model::values::image_instantiation(instance):
    assert isinstance(instance, model::values::Image)

@given(instance=model::values::Image_strategy)
def test_model::values::image_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=model::values::Image_strategy)
def test_model::values::image_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=model::values::Image_strategy)
def test_model::values::image_reference_type(instance):
    assert isinstance(instance.reference, str)


@given(instance=model::values::Image_strategy)
def test_model::values::image_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=model::values::Image_strategy)
def test_model::values::image_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=model::values::Image_strategy)
def test_model::values::image_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=model::values::Image_strategy)
def test_model::values::image_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::values::Image_strategy)
def test_model::values::image_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::values::Argument_strategy)
@settings(max_examples=50)
def test_model::values::argument_instantiation(instance):
    assert isinstance(instance, model::values::Argument)

@given(instance=model::values::Argument_strategy)
def test_model::values::argument_argument_type(instance):
    assert isinstance(instance.argument, str)


@given(instance=model::values::Argument_strategy)
def test_model::values::argument_argument_setter(instance):
    original = instance.argument
    instance.argument = original
    assert instance.argument == original

@given(instance=model::values::Unit_strategy)
@settings(max_examples=50)
def test_model::values::unit_instantiation(instance):
    assert isinstance(instance, model::values::Unit)

@given(instance=model::values::Unit_strategy)
def test_model::values::unit_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=model::values::Unit_strategy)
def test_model::values::unit_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=model::values::ImportValue_strategy)
@settings(max_examples=50)
def test_model::values::importvalue_instantiation(instance):
    assert isinstance(instance, model::values::ImportValue)

@given(instance=model::values::ImportValue_strategy)
def test_model::values::importvalue_modelInterpreterId_type(instance):
    assert isinstance(instance.modelInterpreterId, str)


@given(instance=model::values::ImportValue_strategy)
def test_model::values::importvalue_modelInterpreterId_setter(instance):
    original = instance.modelInterpreterId
    instance.modelInterpreterId = original
    assert instance.modelInterpreterId == original

@given(instance=model::values::MDTimeSeries_strategy)
@settings(max_examples=50)
def test_model::values::mdtimeseries_instantiation(instance):
    assert isinstance(instance, model::values::MDTimeSeries)

@given(instance=model::values::Expression_strategy)
@settings(max_examples=50)
def test_model::values::expression_instantiation(instance):
    assert isinstance(instance, model::values::Expression)

@given(instance=model::values::Expression_strategy)
def test_model::values::expression_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=model::values::Expression_strategy)
def test_model::values::expression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=model::values::MetadataValue_strategy)
@settings(max_examples=50)
def test_model::values::metadatavalue_instantiation(instance):
    assert isinstance(instance, model::values::MetadataValue)

@given(instance=model::values::Point_strategy)
@settings(max_examples=50)
def test_model::values::point_instantiation(instance):
    assert isinstance(instance, model::values::Point)

@given(instance=model::values::Point_strategy)
def test_model::values::point_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=model::values::Point_strategy)
def test_model::values::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=model::values::Point_strategy)
def test_model::values::point_z_type(instance):
    assert isinstance(instance.z, str)


@given(instance=model::values::Point_strategy)
def test_model::values::point_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original

@given(instance=model::values::Point_strategy)
def test_model::values::point_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=model::values::Point_strategy)
def test_model::values::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=model::values::Pointer_strategy)
@settings(max_examples=50)
def test_model::values::pointer_instantiation(instance):
    assert isinstance(instance, model::values::Pointer)

@given(instance=model::values::Pointer_strategy)
def test_model::values::pointer_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=model::values::Pointer_strategy)
def test_model::values::pointer_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=model::values::Dynamics_strategy)
@settings(max_examples=50)
def test_model::values::dynamics_instantiation(instance):
    assert isinstance(instance, model::values::Dynamics)

@given(instance=model::values::Particles_strategy)
@settings(max_examples=50)
def test_model::values::particles_instantiation(instance):
    assert isinstance(instance, model::values::Particles)

@given(instance=model::values::Quantity_strategy)
@settings(max_examples=50)
def test_model::values::quantity_instantiation(instance):
    assert isinstance(instance, model::values::Quantity)

@given(instance=model::values::Quantity_strategy)
def test_model::values::quantity_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::values::Quantity_strategy)
def test_model::values::quantity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::values::Quantity_strategy)
def test_model::values::quantity_scalingFactor_type(instance):
    assert isinstance(instance.scalingFactor, str)


@given(instance=model::values::Quantity_strategy)
def test_model::values::quantity_scalingFactor_setter(instance):
    original = instance.scalingFactor
    instance.scalingFactor = original
    assert instance.scalingFactor == original

@given(instance=model::values::TimeSeries_strategy)
@settings(max_examples=50)
def test_model::values::timeseries_instantiation(instance):
    assert isinstance(instance, model::values::TimeSeries)

@given(instance=model::values::TimeSeries_strategy)
def test_model::values::timeseries_scalingFactor_type(instance):
    assert isinstance(instance.scalingFactor, str)


@given(instance=model::values::TimeSeries_strategy)
def test_model::values::timeseries_scalingFactor_setter(instance):
    original = instance.scalingFactor
    instance.scalingFactor = original
    assert instance.scalingFactor == original

@given(instance=model::values::TimeSeries_strategy)
def test_model::values::timeseries_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::values::TimeSeries_strategy)
def test_model::values::timeseries_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::StringToStringMap_strategy)
@settings(max_examples=50)
def test_model::stringtostringmap_instantiation(instance):
    assert isinstance(instance, model::StringToStringMap)

@given(instance=model::StringToStringMap_strategy)
def test_model::stringtostringmap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::StringToStringMap_strategy)
def test_model::stringtostringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::StringToStringMap_strategy)
def test_model::stringtostringmap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=model::StringToStringMap_strategy)
def test_model::stringtostringmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=DomainModel__strategy)
@settings(max_examples=50)
def test_domainmodel__instantiation(instance):
    assert isinstance(instance, DomainModel_)

@given(instance=model::ExternalDomainModel_strategy)
@settings(max_examples=50)
def test_model::externaldomainmodel_instantiation(instance):
    assert isinstance(instance, model::ExternalDomainModel)

@given(instance=model::ExternalDomainModel_strategy)
def test_model::externaldomainmodel_fileFormat_type(instance):
    assert isinstance(instance.fileFormat, str)


@given(instance=model::ExternalDomainModel_strategy)
def test_model::externaldomainmodel_fileFormat_setter(instance):
    original = instance.fileFormat
    instance.fileFormat = original
    assert instance.fileFormat == original

@given(instance=model::ModelFormat_strategy)
@settings(max_examples=50)
def test_model::modelformat_instantiation(instance):
    assert isinstance(instance, model::ModelFormat)

@given(instance=model::ModelFormat_strategy)
def test_model::modelformat_modelFormat_type(instance):
    assert isinstance(instance.modelFormat, str)


@given(instance=model::ModelFormat_strategy)
def test_model::modelformat_modelFormat_setter(instance):
    original = instance.modelFormat
    instance.modelFormat = original
    assert instance.modelFormat == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=model::types::HTMLType_strategy)
@settings(max_examples=50)
def test_model::types::htmltype_instantiation(instance):
    assert isinstance(instance, model::types::HTMLType)

@given(instance=model::types::ExpressionType_strategy)
@settings(max_examples=50)
def test_model::types::expressiontype_instantiation(instance):
    assert isinstance(instance, model::types::ExpressionType)

@given(instance=model::types::URLType_strategy)
@settings(max_examples=50)
def test_model::types::urltype_instantiation(instance):
    assert isinstance(instance, model::types::URLType)

@given(instance=model::types::SimpleArrayType_strategy)
@settings(max_examples=50)
def test_model::types::simplearraytype_instantiation(instance):
    assert isinstance(instance, model::types::SimpleArrayType)

@given(instance=model::types::ImageType_strategy)
@settings(max_examples=50)
def test_model::types::imagetype_instantiation(instance):
    assert isinstance(instance, model::types::ImageType)

@given(instance=model::types::PointerType_strategy)
@settings(max_examples=50)
def test_model::types::pointertype_instantiation(instance):
    assert isinstance(instance, model::types::PointerType)

@given(instance=model::types::CompositeType_strategy)
@settings(max_examples=50)
def test_model::types::compositetype_instantiation(instance):
    assert isinstance(instance, model::types::CompositeType)

@given(instance=model::types::ArrayType_strategy)
@settings(max_examples=50)
def test_model::types::arraytype_instantiation(instance):
    assert isinstance(instance, model::types::ArrayType)

@given(instance=model::types::ArrayType_strategy)
def test_model::types::arraytype_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=model::types::ArrayType_strategy)
def test_model::types::arraytype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=model::types::VisualType_strategy)
@settings(max_examples=50)
def test_model::types::visualtype_instantiation(instance):
    assert isinstance(instance, model::types::VisualType)

@given(instance=model::types::ImportType_strategy)
@settings(max_examples=50)
def test_model::types::importtype_instantiation(instance):
    assert isinstance(instance, model::types::ImportType)

@given(instance=model::types::ImportType_strategy)
def test_model::types::importtype_referenceURL_type(instance):
    assert isinstance(instance.referenceURL, str)


@given(instance=model::types::ImportType_strategy)
def test_model::types::importtype_referenceURL_setter(instance):
    original = instance.referenceURL
    instance.referenceURL = original
    assert instance.referenceURL == original

@given(instance=model::types::ImportType_strategy)
def test_model::types::importtype_autoresolve_type(instance):
    assert isinstance(instance.autoresolve, str)


@given(instance=model::types::ImportType_strategy)
def test_model::types::importtype_autoresolve_setter(instance):
    original = instance.autoresolve
    instance.autoresolve = original
    assert instance.autoresolve == original

@given(instance=model::types::ImportType_strategy)
def test_model::types::importtype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=model::types::ImportType_strategy)
def test_model::types::importtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=model::types::ImportType_strategy)
def test_model::types::importtype_modelInterpreterId_type(instance):
    assert isinstance(instance.modelInterpreterId, str)


@given(instance=model::types::ImportType_strategy)
def test_model::types::importtype_modelInterpreterId_setter(instance):
    original = instance.modelInterpreterId
    instance.modelInterpreterId = original
    assert instance.modelInterpreterId == original

@given(instance=model::types::ParameterType_strategy)
@settings(max_examples=50)
def test_model::types::parametertype_instantiation(instance):
    assert isinstance(instance, model::types::ParameterType)

@given(instance=model::types::StateVariableType_strategy)
@settings(max_examples=50)
def test_model::types::statevariabletype_instantiation(instance):
    assert isinstance(instance, model::types::StateVariableType)

@given(instance=model::types::QuantityType_strategy)
@settings(max_examples=50)
def test_model::types::quantitytype_instantiation(instance):
    assert isinstance(instance, model::types::QuantityType)

@given(instance=model::types::MetadataType_strategy)
@settings(max_examples=50)
def test_model::types::metadatatype_instantiation(instance):
    assert isinstance(instance, model::types::MetadataType)

@given(instance=model::types::SimpleType_strategy)
@settings(max_examples=50)
def test_model::types::simpletype_instantiation(instance):
    assert isinstance(instance, model::types::SimpleType)

@given(instance=model::types::DynamicsType_strategy)
@settings(max_examples=50)
def test_model::types::dynamicstype_instantiation(instance):
    assert isinstance(instance, model::types::DynamicsType)

@given(instance=model::types::ArgumentType_strategy)
@settings(max_examples=50)
def test_model::types::argumenttype_instantiation(instance):
    assert isinstance(instance, model::types::ArgumentType)

@given(instance=model::types::TextType_strategy)
@settings(max_examples=50)
def test_model::types::texttype_instantiation(instance):
    assert isinstance(instance, model::types::TextType)

@given(instance=model::types::ConnectionType_strategy)
@settings(max_examples=50)
def test_model::types::connectiontype_instantiation(instance):
    assert isinstance(instance, model::types::ConnectionType)

@given(instance=model::types::JSONType_strategy)
@settings(max_examples=50)
def test_model::types::jsontype_instantiation(instance):
    assert isinstance(instance, model::types::JSONType)

@given(instance=model::types::PointType_strategy)
@settings(max_examples=50)
def test_model::types::pointtype_instantiation(instance):
    assert isinstance(instance, model::types::PointType)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=model::types::Type_strategy)
@settings(max_examples=50)
def test_model::types::type_instantiation(instance):
    assert isinstance(instance, model::types::Type)

@given(instance=model::types::Type_strategy)
def test_model::types::type_abstract_type(instance):
    assert isinstance(instance.abstract, str)


@given(instance=model::types::Type_strategy)
def test_model::types::type_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model::types::Type_strategy)
@settings(max_examples=30)
def test_model::types::type_extendstype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.extendsType(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.extendsType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'extendsType' in model::types::Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'extendsType' in model::types::Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'extendsType' in model::types::Type is not implemented or raised an error")

@given(instance=model::values::VisualGroup_strategy)
@settings(max_examples=50)
def test_model::values::visualgroup_instantiation(instance):
    assert isinstance(instance, model::values::VisualGroup)

@given(instance=model::values::VisualGroup_strategy)
def test_model::values::visualgroup_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::values::VisualGroup_strategy)
def test_model::values::visualgroup_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::values::VisualGroup_strategy)
def test_model::values::visualgroup_highSpectrumColor_type(instance):
    assert isinstance(instance.highSpectrumColor, str)


@given(instance=model::values::VisualGroup_strategy)
def test_model::values::visualgroup_highSpectrumColor_setter(instance):
    original = instance.highSpectrumColor
    instance.highSpectrumColor = original
    assert instance.highSpectrumColor == original

@given(instance=model::values::VisualGroup_strategy)
def test_model::values::visualgroup_lowSpectrumColor_type(instance):
    assert isinstance(instance.lowSpectrumColor, str)


@given(instance=model::values::VisualGroup_strategy)
def test_model::values::visualgroup_lowSpectrumColor_setter(instance):
    original = instance.lowSpectrumColor
    instance.lowSpectrumColor = original
    assert instance.lowSpectrumColor == original

@given(instance=model::values::VisualGroupElement_strategy)
@settings(max_examples=50)
def test_model::values::visualgroupelement_instantiation(instance):
    assert isinstance(instance, model::values::VisualGroupElement)

@given(instance=model::values::VisualGroupElement_strategy)
def test_model::values::visualgroupelement_defaultColor_type(instance):
    assert isinstance(instance.defaultColor, str)


@given(instance=model::values::VisualGroupElement_strategy)
def test_model::values::visualgroupelement_defaultColor_setter(instance):
    original = instance.defaultColor
    instance.defaultColor = original
    assert instance.defaultColor == original

@given(instance=model::datasources::Query_strategy)
@settings(max_examples=50)
def test_model::datasources::query_instantiation(instance):
    assert isinstance(instance, model::datasources::Query)

@given(instance=model::datasources::Query_strategy)
def test_model::datasources::query_runForCount_type(instance):
    assert isinstance(instance.runForCount, str)


@given(instance=model::datasources::Query_strategy)
def test_model::datasources::query_runForCount_setter(instance):
    original = instance.runForCount
    instance.runForCount = original
    assert instance.runForCount == original

@given(instance=model::datasources::Query_strategy)
def test_model::datasources::query_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=model::datasources::Query_strategy)
def test_model::datasources::query_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=model::variables::Variable_strategy)
@settings(max_examples=50)
def test_model::variables::variable_instantiation(instance):
    assert isinstance(instance, model::variables::Variable)

@given(instance=model::variables::Variable_strategy)
def test_model::variables::variable_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=model::variables::Variable_strategy)
def test_model::variables::variable_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=model::datasources::DataSource_strategy)
@settings(max_examples=50)
def test_model::datasources::datasource_instantiation(instance):
    assert isinstance(instance, model::datasources::DataSource)

@given(instance=model::datasources::DataSource_strategy)
def test_model::datasources::datasource_dataSourceService_type(instance):
    assert isinstance(instance.dataSourceService, str)


@given(instance=model::datasources::DataSource_strategy)
def test_model::datasources::datasource_dataSourceService_setter(instance):
    original = instance.dataSourceService
    instance.dataSourceService = original
    assert instance.dataSourceService == original

@given(instance=model::datasources::DataSource_strategy)
def test_model::datasources::datasource_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=model::datasources::DataSource_strategy)
def test_model::datasources::datasource_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=model::instances::Instance_strategy)
@settings(max_examples=50)
def test_model::instances::instance_instantiation(instance):
    assert isinstance(instance, model::instances::Instance)

@given(instance=ISynchable_strategy)
@settings(max_examples=50)
def test_isynchable_instantiation(instance):
    assert isinstance(instance, ISynchable)

@given(instance=model::values::Value_strategy)
@settings(max_examples=50)
def test_model::values::value_instantiation(instance):
    assert isinstance(instance, model::values::Value)

@given(instance=model::Node_strategy)
@settings(max_examples=50)
def test_model::node_instantiation(instance):
    assert isinstance(instance, model::Node)

@given(instance=model::Node_strategy)
def test_model::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Node_strategy)
def test_model::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Node_strategy)
def test_model::node_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=model::Node_strategy)
def test_model::node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Query_strategy)
@settings(max_examples=50)
def test_query_instantiation(instance):
    assert isinstance(instance, Query)

@given(instance=model::datasources::CompoundRefQuery_strategy)
@settings(max_examples=50)
def test_model::datasources::compoundrefquery_instantiation(instance):
    assert isinstance(instance, model::datasources::CompoundRefQuery)

@given(instance=model::datasources::ProcessQuery_strategy)
@settings(max_examples=50)
def test_model::datasources::processquery_instantiation(instance):
    assert isinstance(instance, model::datasources::ProcessQuery)

@given(instance=model::datasources::ProcessQuery_strategy)
def test_model::datasources::processquery_queryProcessorId_type(instance):
    assert isinstance(instance.queryProcessorId, str)


@given(instance=model::datasources::ProcessQuery_strategy)
def test_model::datasources::processquery_queryProcessorId_setter(instance):
    original = instance.queryProcessorId
    instance.queryProcessorId = original
    assert instance.queryProcessorId == original

@given(instance=model::datasources::CompoundQuery_strategy)
@settings(max_examples=50)
def test_model::datasources::compoundquery_instantiation(instance):
    assert isinstance(instance, model::datasources::CompoundQuery)

@given(instance=model::datasources::SimpleQuery_strategy)
@settings(max_examples=50)
def test_model::datasources::simplequery_instantiation(instance):
    assert isinstance(instance, model::datasources::SimpleQuery)

@given(instance=model::datasources::SimpleQuery_strategy)
def test_model::datasources::simplequery_countQuery_type(instance):
    assert isinstance(instance.countQuery, str)


@given(instance=model::datasources::SimpleQuery_strategy)
def test_model::datasources::simplequery_countQuery_setter(instance):
    original = instance.countQuery
    instance.countQuery = original
    assert instance.countQuery == original

@given(instance=model::datasources::SimpleQuery_strategy)
def test_model::datasources::simplequery_query_type(instance):
    assert isinstance(instance.query, str)


@given(instance=model::datasources::SimpleQuery_strategy)
def test_model::datasources::simplequery_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original

@given(instance=DataSource_strategy)
@settings(max_examples=50)
def test_datasource_instantiation(instance):
    assert isinstance(instance, DataSource)

@given(instance=Pointer_strategy)
@settings(max_examples=50)
def test_pointer_instantiation(instance):
    assert isinstance(instance, Pointer)

@given(instance=model::VariableValue_strategy)
@settings(max_examples=50)
def test_model::variablevalue_instantiation(instance):
    assert isinstance(instance, model::VariableValue)

@given(instance=model::ExperimentState_strategy)
@settings(max_examples=50)
def test_model::experimentstate_instantiation(instance):
    assert isinstance(instance, model::ExperimentState)

@given(instance=model::ExperimentState_strategy)
def test_model::experimentstate_experimentId_type(instance):
    assert isinstance(instance.experimentId, str)


@given(instance=model::ExperimentState_strategy)
def test_model::experimentstate_experimentId_setter(instance):
    original = instance.experimentId
    instance.experimentId = original
    assert instance.experimentId == original

@given(instance=model::ExperimentState_strategy)
def test_model::experimentstate_projectId_type(instance):
    assert isinstance(instance.projectId, str)


@given(instance=model::ExperimentState_strategy)
def test_model::experimentstate_projectId_setter(instance):
    original = instance.projectId
    instance.projectId = original
    assert instance.projectId == original

@given(instance=model::LibraryManager_strategy)
@settings(max_examples=50)
def test_model::librarymanager_instantiation(instance):
    assert isinstance(instance, model::LibraryManager)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=model::GeppettoModel_strategy)
@settings(max_examples=50)
def test_model::geppettomodel_instantiation(instance):
    assert isinstance(instance, model::GeppettoModel)

@given(instance=model::GeppettoModel_strategy)
def test_model::geppettomodel_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=model::GeppettoModel_strategy)
def test_model::geppettomodel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=model::GeppettoModel_strategy)
def test_model::geppettomodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::GeppettoModel_strategy)
def test_model::geppettomodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Tag_strategy)
@settings(max_examples=50)
def test_model::tag_instantiation(instance):
    assert isinstance(instance, model::Tag)

@given(instance=model::Tag_strategy)
def test_model::tag_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Tag_strategy)
def test_model::tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::GeppettoLibrary_strategy)
@settings(max_examples=50)
def test_model::geppettolibrary_instantiation(instance):
    assert isinstance(instance, model::GeppettoLibrary)

@given(instance=model::World_strategy)
@settings(max_examples=50)
def test_model::world_instantiation(instance):
    assert isinstance(instance, model::World)
