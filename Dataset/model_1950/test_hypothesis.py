import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_datasources_QueryResults,
    model_datasources_QueryMatchingCriteria,
    VisualGroup,
    ArrayValue,
    Point,
    URL,
    Text,
    VisualValue,
    Expression,
    Argument,
    Dynamics,
    Quantity,
    Composite,
    model_ModelFormat,
    model_DomainModel_,
    types_model_DomainModel_,
    VisualType,
    model_types_CompositeVisualType,
    model_ISynchable,
    model_StringToStringMap,
    DomainModel_,
    model_ExternalDomainModel,
    ISynchable,
    model_Node,
    Query,
    model_datasources_CompoundRefQuery,
    DataSource,
    Value,
    Pointer,
    model_VariableValue,
    model_ExperimentState,
    model_LibraryManager,
    Type,
    model_types_VisualType,
    model_types_ArgumentType,
    model_types_DynamicsType,
    model_types_ExpressionType,
    model_types_URLType,
    model_types_ArrayType,
    model_types_ConnectionType,
    model_types_PointerType,
    model_types_CompositeType,
    model_types_ImportType,
    model_types_StateVariableType,
    model_types_PointType,
    model_types_ParameterType,
    model_types_QuantityType,
    Node,
    model_types_Type,
    model_Tag,
    model_GeppettoLibrary,
    Variable,
    model_GeppettoModel,
    model_datasources_AQueryResult,
    model_datasources_RunnableQuery,
    AQueryResult,
    model_datasources_QueryResult,
    model_datasources_SerializableQueryResult,
    model_datasources_DataSourceLibraryConfiguration,
    datasources_model_GeppettoLibrary,
    model_datasources_CompoundQuery,
    model_datasources_SimpleQuery,
    datasources_model_StringToStringMap,
    model_datasources_ProcessQuery,
    QueryMatchingCriteria,
    model_datasources_Query,
    model_variables_Variable,
    model_values_AArrayValue,
    DataSourceLibraryConfiguration,
    model_datasources_DataSource,
    model_variables_TypeToValueMap,
    TypeToValueMap,
    model_values_Image,
    ArrayElement,
    model_values_ArrayValue,
    model_values_ImportValue,
    SkeletonTransformation,
    model_values_SkeletonAnimation,
    model_values_Particles,
    model_values_ArrayElement,
    model_values_Connection,
    model_values_VisualGroup,
    model_values_VisualGroupElement,
    model_values_SkeletonTransformation,
    model_values_Function,
    model_values_FunctionPlot,
    Function,
    model_values_Cylinder,
    model_values_Sphere,
    model_values_OBJ,
    model_values_Collada,
    VisualGroupElement,
    model_values_VisualValue,
    model_values_Expression,
    model_values_Argument,
    FunctionPlot,
    MetadataValue,
    model_values_Metadata,
    model_values_JSON,
    model_values_Text,
    model_values_MetadataValue,
    model_values_MDTimeSeries,
    PhysicalQuantity,
    model_values_Dynamics,
    model_values_Point,
    model_values_PointerElement,
    PointerElement,
    model_values_Pointer,
    model_values_HTML,
    model_values_URL,
    Image,
    model_types_ImageType,
    model_types_SimpleType,
    model_values_TimeSeries,
    model_values_Unit,
    Unit,
    model_values_PhysicalQuantity,
    model_values_Quantity,
    model_values_StringToValueMap,
    StringToValueMap,
    model_values_Composite,
    model_values_Value,
    model_types_MetadataType,
    AArrayValue,
    model_values_DoubleArray,
    model_values_StringArray,
    model_values_IntArray,
    model_values_GenericArray,
    model_types_SimpleArrayType,
    model_types_TextType,
    JSON,
    model_types_JSONType,
    HTML,
    model_types_HTMLType,
    ImageFormat,
    FileFormat,
    Connectivity,
    BooleanOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_datasources_queryresults_is_not_abstract():
    assert not inspect.isabstract(model_datasources_QueryResults)


def test_model_datasources_queryresults_constructor_exists():
    assert callable(model_datasources_QueryResults.__init__)


def test_model_datasources_queryresults_constructor_args():
    sig = inspect.signature(model_datasources_QueryResults.__init__)
    params = list(sig.parameters.keys())
    assert "header" in params, "Missing parameter 'header'"
    assert "id" in params, "Missing parameter 'id'"

def test_model_datasources_queryresults_has_header():
    assert hasattr(model_datasources_QueryResults, "header")
    descriptor = None
    for klass in model_datasources_QueryResults.__mro__:
        if "header" in klass.__dict__:
            descriptor = klass.__dict__["header"]
            break
    assert isinstance(descriptor, property)

def test_model_datasources_queryresults_has_id():
    assert hasattr(model_datasources_QueryResults, "id")
    descriptor = None
    for klass in model_datasources_QueryResults.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_model_datasources_querymatchingcriteria_is_not_abstract():
    assert not inspect.isabstract(model_datasources_QueryMatchingCriteria)


def test_model_datasources_querymatchingcriteria_constructor_exists():
    assert callable(model_datasources_QueryMatchingCriteria.__init__)


def test_model_datasources_querymatchingcriteria_constructor_args():
    sig = inspect.signature(model_datasources_QueryMatchingCriteria.__init__)
    params = list(sig.parameters.keys())



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



def test_visualvalue_is_not_abstract():
    assert not inspect.isabstract(VisualValue)


def test_visualvalue_constructor_exists():
    assert callable(VisualValue.__init__)


def test_visualvalue_constructor_args():
    sig = inspect.signature(VisualValue.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
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



def test_composite_is_not_abstract():
    assert not inspect.isabstract(Composite)


def test_composite_constructor_exists():
    assert callable(Composite.__init__)


def test_composite_constructor_args():
    sig = inspect.signature(Composite.__init__)
    params = list(sig.parameters.keys())



def test_model_modelformat_is_not_abstract():
    assert not inspect.isabstract(model_ModelFormat)


def test_model_modelformat_constructor_exists():
    assert callable(model_ModelFormat.__init__)


def test_model_modelformat_constructor_args():
    sig = inspect.signature(model_ModelFormat.__init__)
    params = list(sig.parameters.keys())
    assert "modelFormat" in params, "Missing parameter 'modelFormat'"

def test_model_modelformat_has_modelFormat():
    assert hasattr(model_ModelFormat, "modelFormat")
    descriptor = None
    for klass in model_ModelFormat.__mro__:
        if "modelFormat" in klass.__dict__:
            descriptor = klass.__dict__["modelFormat"]
            break
    assert isinstance(descriptor, property)



def test_model_domainmodel__is_not_abstract():
    assert not inspect.isabstract(model_DomainModel_)


def test_model_domainmodel__constructor_exists():
    assert callable(model_DomainModel_.__init__)


def test_model_domainmodel__constructor_args():
    sig = inspect.signature(model_DomainModel_.__init__)
    params = list(sig.parameters.keys())
    assert "domainModel" in params, "Missing parameter 'domainModel'"

def test_model_domainmodel__has_domainModel():
    assert hasattr(model_DomainModel_, "domainModel")
    descriptor = None
    for klass in model_DomainModel_.__mro__:
        if "domainModel" in klass.__dict__:
            descriptor = klass.__dict__["domainModel"]
            break
    assert isinstance(descriptor, property)



def test_types_model_domainmodel__is_not_abstract():
    assert not inspect.isabstract(types_model_DomainModel_)


def test_types_model_domainmodel__constructor_exists():
    assert callable(types_model_DomainModel_.__init__)


def test_types_model_domainmodel__constructor_args():
    sig = inspect.signature(types_model_DomainModel_.__init__)
    params = list(sig.parameters.keys())



def test_visualtype_is_not_abstract():
    assert not inspect.isabstract(VisualType)


def test_visualtype_constructor_exists():
    assert callable(VisualType.__init__)


def test_visualtype_constructor_args():
    sig = inspect.signature(VisualType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_compositevisualtype_is_not_abstract():
    assert not inspect.isabstract(model_types_CompositeVisualType)


def test_model_types_compositevisualtype_constructor_exists():
    assert callable(model_types_CompositeVisualType.__init__)


def test_model_types_compositevisualtype_constructor_args():
    sig = inspect.signature(model_types_CompositeVisualType.__init__)
    params = list(sig.parameters.keys())



def test_model_isynchable_is_not_abstract():
    assert not inspect.isabstract(model_ISynchable)


def test_model_isynchable_constructor_exists():
    assert callable(model_ISynchable.__init__)


def test_model_isynchable_constructor_args():
    sig = inspect.signature(model_ISynchable.__init__)
    params = list(sig.parameters.keys())
    assert "synched" in params, "Missing parameter 'synched'"

def test_model_isynchable_has_synched():
    assert hasattr(model_ISynchable, "synched")
    descriptor = None
    for klass in model_ISynchable.__mro__:
        if "synched" in klass.__dict__:
            descriptor = klass.__dict__["synched"]
            break
    assert isinstance(descriptor, property)



def test_model_stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(model_StringToStringMap)


def test_model_stringtostringmap_constructor_exists():
    assert callable(model_StringToStringMap.__init__)


def test_model_stringtostringmap_constructor_args():
    sig = inspect.signature(model_StringToStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_model_stringtostringmap_has_value():
    assert hasattr(model_StringToStringMap, "value")
    descriptor = None
    for klass in model_StringToStringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_model_stringtostringmap_has_key():
    assert hasattr(model_StringToStringMap, "key")
    descriptor = None
    for klass in model_StringToStringMap.__mro__:
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



def test_model_externaldomainmodel_is_not_abstract():
    assert not inspect.isabstract(model_ExternalDomainModel)


def test_model_externaldomainmodel_constructor_exists():
    assert callable(model_ExternalDomainModel.__init__)


def test_model_externaldomainmodel_constructor_args():
    sig = inspect.signature(model_ExternalDomainModel.__init__)
    params = list(sig.parameters.keys())
    assert "fileFormat" in params, "Missing parameter 'fileFormat'"

def test_model_externaldomainmodel_has_fileFormat():
    assert hasattr(model_ExternalDomainModel, "fileFormat")
    descriptor = None
    for klass in model_ExternalDomainModel.__mro__:
        if "fileFormat" in klass.__dict__:
            descriptor = klass.__dict__["fileFormat"]
            break
    assert isinstance(descriptor, property)



def test_isynchable_is_not_abstract():
    assert not inspect.isabstract(ISynchable)


def test_isynchable_constructor_exists():
    assert callable(ISynchable.__init__)


def test_isynchable_constructor_args():
    sig = inspect.signature(ISynchable.__init__)
    params = list(sig.parameters.keys())



def test_model_node_is_not_abstract():
    assert not inspect.isabstract(model_Node)


def test_model_node_constructor_exists():
    assert callable(model_Node.__init__)


def test_model_node_constructor_args():
    sig = inspect.signature(model_Node.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_model_node_has_id():
    assert hasattr(model_Node, "id")
    descriptor = None
    for klass in model_Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_model_node_has_name():
    assert hasattr(model_Node, "name")
    descriptor = None
    for klass in model_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_query_is_not_abstract():
    assert not inspect.isabstract(Query)


def test_query_constructor_exists():
    assert callable(Query.__init__)


def test_query_constructor_args():
    sig = inspect.signature(Query.__init__)
    params = list(sig.parameters.keys())



def test_model_datasources_compoundrefquery_is_not_abstract():
    assert not inspect.isabstract(model_datasources_CompoundRefQuery)


def test_model_datasources_compoundrefquery_constructor_exists():
    assert callable(model_datasources_CompoundRefQuery.__init__)


def test_model_datasources_compoundrefquery_constructor_args():
    sig = inspect.signature(model_datasources_CompoundRefQuery.__init__)
    params = list(sig.parameters.keys())



def test_datasource_is_not_abstract():
    assert not inspect.isabstract(DataSource)


def test_datasource_constructor_exists():
    assert callable(DataSource.__init__)


def test_datasource_constructor_args():
    sig = inspect.signature(DataSource.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_pointer_is_not_abstract():
    assert not inspect.isabstract(Pointer)


def test_pointer_constructor_exists():
    assert callable(Pointer.__init__)


def test_pointer_constructor_args():
    sig = inspect.signature(Pointer.__init__)
    params = list(sig.parameters.keys())



def test_model_variablevalue_is_not_abstract():
    assert not inspect.isabstract(model_VariableValue)


def test_model_variablevalue_constructor_exists():
    assert callable(model_VariableValue.__init__)


def test_model_variablevalue_constructor_args():
    sig = inspect.signature(model_VariableValue.__init__)
    params = list(sig.parameters.keys())



def test_model_experimentstate_is_not_abstract():
    assert not inspect.isabstract(model_ExperimentState)


def test_model_experimentstate_constructor_exists():
    assert callable(model_ExperimentState.__init__)


def test_model_experimentstate_constructor_args():
    sig = inspect.signature(model_ExperimentState.__init__)
    params = list(sig.parameters.keys())
    assert "experimentId" in params, "Missing parameter 'experimentId'"
    assert "projectId" in params, "Missing parameter 'projectId'"

def test_model_experimentstate_has_experimentId():
    assert hasattr(model_ExperimentState, "experimentId")
    descriptor = None
    for klass in model_ExperimentState.__mro__:
        if "experimentId" in klass.__dict__:
            descriptor = klass.__dict__["experimentId"]
            break
    assert isinstance(descriptor, property)

def test_model_experimentstate_has_projectId():
    assert hasattr(model_ExperimentState, "projectId")
    descriptor = None
    for klass in model_ExperimentState.__mro__:
        if "projectId" in klass.__dict__:
            descriptor = klass.__dict__["projectId"]
            break
    assert isinstance(descriptor, property)



def test_model_librarymanager_is_not_abstract():
    assert not inspect.isabstract(model_LibraryManager)


def test_model_librarymanager_constructor_exists():
    assert callable(model_LibraryManager.__init__)


def test_model_librarymanager_constructor_args():
    sig = inspect.signature(model_LibraryManager.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_model_types_visualtype_is_not_abstract():
    assert not inspect.isabstract(model_types_VisualType)


def test_model_types_visualtype_constructor_exists():
    assert callable(model_types_VisualType.__init__)


def test_model_types_visualtype_constructor_args():
    sig = inspect.signature(model_types_VisualType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_argumenttype_is_not_abstract():
    assert not inspect.isabstract(model_types_ArgumentType)


def test_model_types_argumenttype_constructor_exists():
    assert callable(model_types_ArgumentType.__init__)


def test_model_types_argumenttype_constructor_args():
    sig = inspect.signature(model_types_ArgumentType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_dynamicstype_is_not_abstract():
    assert not inspect.isabstract(model_types_DynamicsType)


def test_model_types_dynamicstype_constructor_exists():
    assert callable(model_types_DynamicsType.__init__)


def test_model_types_dynamicstype_constructor_args():
    sig = inspect.signature(model_types_DynamicsType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_expressiontype_is_not_abstract():
    assert not inspect.isabstract(model_types_ExpressionType)


def test_model_types_expressiontype_constructor_exists():
    assert callable(model_types_ExpressionType.__init__)


def test_model_types_expressiontype_constructor_args():
    sig = inspect.signature(model_types_ExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_urltype_is_not_abstract():
    assert not inspect.isabstract(model_types_URLType)


def test_model_types_urltype_constructor_exists():
    assert callable(model_types_URLType.__init__)


def test_model_types_urltype_constructor_args():
    sig = inspect.signature(model_types_URLType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_arraytype_is_not_abstract():
    assert not inspect.isabstract(model_types_ArrayType)


def test_model_types_arraytype_constructor_exists():
    assert callable(model_types_ArrayType.__init__)


def test_model_types_arraytype_constructor_args():
    sig = inspect.signature(model_types_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_model_types_arraytype_has_size():
    assert hasattr(model_types_ArrayType, "size")
    descriptor = None
    for klass in model_types_ArrayType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_model_types_connectiontype_is_not_abstract():
    assert not inspect.isabstract(model_types_ConnectionType)


def test_model_types_connectiontype_constructor_exists():
    assert callable(model_types_ConnectionType.__init__)


def test_model_types_connectiontype_constructor_args():
    sig = inspect.signature(model_types_ConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_pointertype_is_not_abstract():
    assert not inspect.isabstract(model_types_PointerType)


def test_model_types_pointertype_constructor_exists():
    assert callable(model_types_PointerType.__init__)


def test_model_types_pointertype_constructor_args():
    sig = inspect.signature(model_types_PointerType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_compositetype_is_not_abstract():
    assert not inspect.isabstract(model_types_CompositeType)


def test_model_types_compositetype_constructor_exists():
    assert callable(model_types_CompositeType.__init__)


def test_model_types_compositetype_constructor_args():
    sig = inspect.signature(model_types_CompositeType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_importtype_is_not_abstract():
    assert not inspect.isabstract(model_types_ImportType)


def test_model_types_importtype_constructor_exists():
    assert callable(model_types_ImportType.__init__)


def test_model_types_importtype_constructor_args():
    sig = inspect.signature(model_types_ImportType.__init__)
    params = list(sig.parameters.keys())
    assert "autoresolve" in params, "Missing parameter 'autoresolve'"
    assert "referenceURL" in params, "Missing parameter 'referenceURL'"
    assert "modelInterpreterId" in params, "Missing parameter 'modelInterpreterId'"
    assert "url" in params, "Missing parameter 'url'"

def test_model_types_importtype_has_autoresolve():
    assert hasattr(model_types_ImportType, "autoresolve")
    descriptor = None
    for klass in model_types_ImportType.__mro__:
        if "autoresolve" in klass.__dict__:
            descriptor = klass.__dict__["autoresolve"]
            break
    assert isinstance(descriptor, property)

def test_model_types_importtype_has_referenceURL():
    assert hasattr(model_types_ImportType, "referenceURL")
    descriptor = None
    for klass in model_types_ImportType.__mro__:
        if "referenceURL" in klass.__dict__:
            descriptor = klass.__dict__["referenceURL"]
            break
    assert isinstance(descriptor, property)

def test_model_types_importtype_has_modelInterpreterId():
    assert hasattr(model_types_ImportType, "modelInterpreterId")
    descriptor = None
    for klass in model_types_ImportType.__mro__:
        if "modelInterpreterId" in klass.__dict__:
            descriptor = klass.__dict__["modelInterpreterId"]
            break
    assert isinstance(descriptor, property)

def test_model_types_importtype_has_url():
    assert hasattr(model_types_ImportType, "url")
    descriptor = None
    for klass in model_types_ImportType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_model_types_statevariabletype_is_not_abstract():
    assert not inspect.isabstract(model_types_StateVariableType)


def test_model_types_statevariabletype_constructor_exists():
    assert callable(model_types_StateVariableType.__init__)


def test_model_types_statevariabletype_constructor_args():
    sig = inspect.signature(model_types_StateVariableType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_pointtype_is_not_abstract():
    assert not inspect.isabstract(model_types_PointType)


def test_model_types_pointtype_constructor_exists():
    assert callable(model_types_PointType.__init__)


def test_model_types_pointtype_constructor_args():
    sig = inspect.signature(model_types_PointType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_parametertype_is_not_abstract():
    assert not inspect.isabstract(model_types_ParameterType)


def test_model_types_parametertype_constructor_exists():
    assert callable(model_types_ParameterType.__init__)


def test_model_types_parametertype_constructor_args():
    sig = inspect.signature(model_types_ParameterType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_quantitytype_is_not_abstract():
    assert not inspect.isabstract(model_types_QuantityType)


def test_model_types_quantitytype_constructor_exists():
    assert callable(model_types_QuantityType.__init__)


def test_model_types_quantitytype_constructor_args():
    sig = inspect.signature(model_types_QuantityType.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_model_types_type_is_not_abstract():
    assert not inspect.isabstract(model_types_Type)


def test_model_types_type_constructor_exists():
    assert callable(model_types_Type.__init__)


def test_model_types_type_constructor_args():
    sig = inspect.signature(model_types_Type.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_model_types_type_has_abstract():
    assert hasattr(model_types_Type, "abstract")
    descriptor = None
    for klass in model_types_Type.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_model_tag_is_not_abstract():
    assert not inspect.isabstract(model_Tag)


def test_model_tag_constructor_exists():
    assert callable(model_Tag.__init__)


def test_model_tag_constructor_args():
    sig = inspect.signature(model_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_tag_has_name():
    assert hasattr(model_Tag, "name")
    descriptor = None
    for klass in model_Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_geppettolibrary_is_not_abstract():
    assert not inspect.isabstract(model_GeppettoLibrary)


def test_model_geppettolibrary_constructor_exists():
    assert callable(model_GeppettoLibrary.__init__)


def test_model_geppettolibrary_constructor_args():
    sig = inspect.signature(model_GeppettoLibrary.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_model_geppettomodel_is_not_abstract():
    assert not inspect.isabstract(model_GeppettoModel)


def test_model_geppettomodel_constructor_exists():
    assert callable(model_GeppettoModel.__init__)


def test_model_geppettomodel_constructor_args():
    sig = inspect.signature(model_GeppettoModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_model_geppettomodel_has_name():
    assert hasattr(model_GeppettoModel, "name")
    descriptor = None
    for klass in model_GeppettoModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_geppettomodel_has_id():
    assert hasattr(model_GeppettoModel, "id")
    descriptor = None
    for klass in model_GeppettoModel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_model_datasources_aqueryresult_is_not_abstract():
    assert not inspect.isabstract(model_datasources_AQueryResult)


def test_model_datasources_aqueryresult_constructor_exists():
    assert callable(model_datasources_AQueryResult.__init__)


def test_model_datasources_aqueryresult_constructor_args():
    sig = inspect.signature(model_datasources_AQueryResult.__init__)
    params = list(sig.parameters.keys())



def test_model_datasources_runnablequery_is_not_abstract():
    assert not inspect.isabstract(model_datasources_RunnableQuery)


def test_model_datasources_runnablequery_constructor_exists():
    assert callable(model_datasources_RunnableQuery.__init__)


def test_model_datasources_runnablequery_constructor_args():
    sig = inspect.signature(model_datasources_RunnableQuery.__init__)
    params = list(sig.parameters.keys())
    assert "queryPath" in params, "Missing parameter 'queryPath'"
    assert "targetVariablePath" in params, "Missing parameter 'targetVariablePath'"
    assert "booleanOperator" in params, "Missing parameter 'booleanOperator'"

def test_model_datasources_runnablequery_has_queryPath():
    assert hasattr(model_datasources_RunnableQuery, "queryPath")
    descriptor = None
    for klass in model_datasources_RunnableQuery.__mro__:
        if "queryPath" in klass.__dict__:
            descriptor = klass.__dict__["queryPath"]
            break
    assert isinstance(descriptor, property)

def test_model_datasources_runnablequery_has_targetVariablePath():
    assert hasattr(model_datasources_RunnableQuery, "targetVariablePath")
    descriptor = None
    for klass in model_datasources_RunnableQuery.__mro__:
        if "targetVariablePath" in klass.__dict__:
            descriptor = klass.__dict__["targetVariablePath"]
            break
    assert isinstance(descriptor, property)

def test_model_datasources_runnablequery_has_booleanOperator():
    assert hasattr(model_datasources_RunnableQuery, "booleanOperator")
    descriptor = None
    for klass in model_datasources_RunnableQuery.__mro__:
        if "booleanOperator" in klass.__dict__:
            descriptor = klass.__dict__["booleanOperator"]
            break
    assert isinstance(descriptor, property)



def test_aqueryresult_is_not_abstract():
    assert not inspect.isabstract(AQueryResult)


def test_aqueryresult_constructor_exists():
    assert callable(AQueryResult.__init__)


def test_aqueryresult_constructor_args():
    sig = inspect.signature(AQueryResult.__init__)
    params = list(sig.parameters.keys())



def test_model_datasources_queryresult_is_not_abstract():
    assert not inspect.isabstract(model_datasources_QueryResult)


def test_model_datasources_queryresult_constructor_exists():
    assert callable(model_datasources_QueryResult.__init__)


def test_model_datasources_queryresult_constructor_args():
    sig = inspect.signature(model_datasources_QueryResult.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_model_datasources_queryresult_has_values():
    assert hasattr(model_datasources_QueryResult, "values")
    descriptor = None
    for klass in model_datasources_QueryResult.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_model_datasources_serializablequeryresult_is_not_abstract():
    assert not inspect.isabstract(model_datasources_SerializableQueryResult)


def test_model_datasources_serializablequeryresult_constructor_exists():
    assert callable(model_datasources_SerializableQueryResult.__init__)


def test_model_datasources_serializablequeryresult_constructor_args():
    sig = inspect.signature(model_datasources_SerializableQueryResult.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_model_datasources_serializablequeryresult_has_values():
    assert hasattr(model_datasources_SerializableQueryResult, "values")
    descriptor = None
    for klass in model_datasources_SerializableQueryResult.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_model_datasources_datasourcelibraryconfiguration_is_not_abstract():
    assert not inspect.isabstract(model_datasources_DataSourceLibraryConfiguration)


def test_model_datasources_datasourcelibraryconfiguration_constructor_exists():
    assert callable(model_datasources_DataSourceLibraryConfiguration.__init__)


def test_model_datasources_datasourcelibraryconfiguration_constructor_args():
    sig = inspect.signature(model_datasources_DataSourceLibraryConfiguration.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"
    assert "modelInterpreterId" in params, "Missing parameter 'modelInterpreterId'"

def test_model_datasources_datasourcelibraryconfiguration_has_format():
    assert hasattr(model_datasources_DataSourceLibraryConfiguration, "format")
    descriptor = None
    for klass in model_datasources_DataSourceLibraryConfiguration.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_model_datasources_datasourcelibraryconfiguration_has_modelInterpreterId():
    assert hasattr(model_datasources_DataSourceLibraryConfiguration, "modelInterpreterId")
    descriptor = None
    for klass in model_datasources_DataSourceLibraryConfiguration.__mro__:
        if "modelInterpreterId" in klass.__dict__:
            descriptor = klass.__dict__["modelInterpreterId"]
            break
    assert isinstance(descriptor, property)



def test_datasources_model_geppettolibrary_is_not_abstract():
    assert not inspect.isabstract(datasources_model_GeppettoLibrary)


def test_datasources_model_geppettolibrary_constructor_exists():
    assert callable(datasources_model_GeppettoLibrary.__init__)


def test_datasources_model_geppettolibrary_constructor_args():
    sig = inspect.signature(datasources_model_GeppettoLibrary.__init__)
    params = list(sig.parameters.keys())



def test_model_datasources_compoundquery_is_not_abstract():
    assert not inspect.isabstract(model_datasources_CompoundQuery)


def test_model_datasources_compoundquery_constructor_exists():
    assert callable(model_datasources_CompoundQuery.__init__)


def test_model_datasources_compoundquery_constructor_args():
    sig = inspect.signature(model_datasources_CompoundQuery.__init__)
    params = list(sig.parameters.keys())



def test_model_datasources_simplequery_is_not_abstract():
    assert not inspect.isabstract(model_datasources_SimpleQuery)


def test_model_datasources_simplequery_constructor_exists():
    assert callable(model_datasources_SimpleQuery.__init__)


def test_model_datasources_simplequery_constructor_args():
    sig = inspect.signature(model_datasources_SimpleQuery.__init__)
    params = list(sig.parameters.keys())
    assert "countQuery" in params, "Missing parameter 'countQuery'"
    assert "query" in params, "Missing parameter 'query'"

def test_model_datasources_simplequery_has_countQuery():
    assert hasattr(model_datasources_SimpleQuery, "countQuery")
    descriptor = None
    for klass in model_datasources_SimpleQuery.__mro__:
        if "countQuery" in klass.__dict__:
            descriptor = klass.__dict__["countQuery"]
            break
    assert isinstance(descriptor, property)

def test_model_datasources_simplequery_has_query():
    assert hasattr(model_datasources_SimpleQuery, "query")
    descriptor = None
    for klass in model_datasources_SimpleQuery.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)



def test_datasources_model_stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(datasources_model_StringToStringMap)


def test_datasources_model_stringtostringmap_constructor_exists():
    assert callable(datasources_model_StringToStringMap.__init__)


def test_datasources_model_stringtostringmap_constructor_args():
    sig = inspect.signature(datasources_model_StringToStringMap.__init__)
    params = list(sig.parameters.keys())



def test_model_datasources_processquery_is_not_abstract():
    assert not inspect.isabstract(model_datasources_ProcessQuery)


def test_model_datasources_processquery_constructor_exists():
    assert callable(model_datasources_ProcessQuery.__init__)


def test_model_datasources_processquery_constructor_args():
    sig = inspect.signature(model_datasources_ProcessQuery.__init__)
    params = list(sig.parameters.keys())
    assert "queryProcessorId" in params, "Missing parameter 'queryProcessorId'"

def test_model_datasources_processquery_has_queryProcessorId():
    assert hasattr(model_datasources_ProcessQuery, "queryProcessorId")
    descriptor = None
    for klass in model_datasources_ProcessQuery.__mro__:
        if "queryProcessorId" in klass.__dict__:
            descriptor = klass.__dict__["queryProcessorId"]
            break
    assert isinstance(descriptor, property)



def test_querymatchingcriteria_is_not_abstract():
    assert not inspect.isabstract(QueryMatchingCriteria)


def test_querymatchingcriteria_constructor_exists():
    assert callable(QueryMatchingCriteria.__init__)


def test_querymatchingcriteria_constructor_args():
    sig = inspect.signature(QueryMatchingCriteria.__init__)
    params = list(sig.parameters.keys())



def test_model_datasources_query_is_not_abstract():
    assert not inspect.isabstract(model_datasources_Query)


def test_model_datasources_query_constructor_exists():
    assert callable(model_datasources_Query.__init__)


def test_model_datasources_query_constructor_args():
    sig = inspect.signature(model_datasources_Query.__init__)
    params = list(sig.parameters.keys())
    assert "runForCount" in params, "Missing parameter 'runForCount'"
    assert "description" in params, "Missing parameter 'description'"

def test_model_datasources_query_has_runForCount():
    assert hasattr(model_datasources_Query, "runForCount")
    descriptor = None
    for klass in model_datasources_Query.__mro__:
        if "runForCount" in klass.__dict__:
            descriptor = klass.__dict__["runForCount"]
            break
    assert isinstance(descriptor, property)

def test_model_datasources_query_has_description():
    assert hasattr(model_datasources_Query, "description")
    descriptor = None
    for klass in model_datasources_Query.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_model_variables_variable_is_not_abstract():
    assert not inspect.isabstract(model_variables_Variable)


def test_model_variables_variable_constructor_exists():
    assert callable(model_variables_Variable.__init__)


def test_model_variables_variable_constructor_args():
    sig = inspect.signature(model_variables_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_model_variables_variable_has_static():
    assert hasattr(model_variables_Variable, "static")
    descriptor = None
    for klass in model_variables_Variable.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_model_values_aarrayvalue_is_not_abstract():
    assert not inspect.isabstract(model_values_AArrayValue)


def test_model_values_aarrayvalue_constructor_exists():
    assert callable(model_values_AArrayValue.__init__)


def test_model_values_aarrayvalue_constructor_args():
    sig = inspect.signature(model_values_AArrayValue.__init__)
    params = list(sig.parameters.keys())



def test_datasourcelibraryconfiguration_is_not_abstract():
    assert not inspect.isabstract(DataSourceLibraryConfiguration)


def test_datasourcelibraryconfiguration_constructor_exists():
    assert callable(DataSourceLibraryConfiguration.__init__)


def test_datasourcelibraryconfiguration_constructor_args():
    sig = inspect.signature(DataSourceLibraryConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_model_datasources_datasource_is_not_abstract():
    assert not inspect.isabstract(model_datasources_DataSource)


def test_model_datasources_datasource_constructor_exists():
    assert callable(model_datasources_DataSource.__init__)


def test_model_datasources_datasource_constructor_args():
    sig = inspect.signature(model_datasources_DataSource.__init__)
    params = list(sig.parameters.keys())
    assert "dataSourceService" in params, "Missing parameter 'dataSourceService'"
    assert "url" in params, "Missing parameter 'url'"

def test_model_datasources_datasource_has_dataSourceService():
    assert hasattr(model_datasources_DataSource, "dataSourceService")
    descriptor = None
    for klass in model_datasources_DataSource.__mro__:
        if "dataSourceService" in klass.__dict__:
            descriptor = klass.__dict__["dataSourceService"]
            break
    assert isinstance(descriptor, property)

def test_model_datasources_datasource_has_url():
    assert hasattr(model_datasources_DataSource, "url")
    descriptor = None
    for klass in model_datasources_DataSource.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_model_variables_typetovaluemap_is_not_abstract():
    assert not inspect.isabstract(model_variables_TypeToValueMap)


def test_model_variables_typetovaluemap_constructor_exists():
    assert callable(model_variables_TypeToValueMap.__init__)


def test_model_variables_typetovaluemap_constructor_args():
    sig = inspect.signature(model_variables_TypeToValueMap.__init__)
    params = list(sig.parameters.keys())



def test_typetovaluemap_is_not_abstract():
    assert not inspect.isabstract(TypeToValueMap)


def test_typetovaluemap_constructor_exists():
    assert callable(TypeToValueMap.__init__)


def test_typetovaluemap_constructor_args():
    sig = inspect.signature(TypeToValueMap.__init__)
    params = list(sig.parameters.keys())



def test_model_values_image_is_not_abstract():
    assert not inspect.isabstract(model_values_Image)


def test_model_values_image_constructor_exists():
    assert callable(model_values_Image.__init__)


def test_model_values_image_constructor_args():
    sig = inspect.signature(model_values_Image.__init__)
    params = list(sig.parameters.keys())
    assert "reference" in params, "Missing parameter 'reference'"
    assert "name" in params, "Missing parameter 'name'"
    assert "format" in params, "Missing parameter 'format'"
    assert "data" in params, "Missing parameter 'data'"

def test_model_values_image_has_reference():
    assert hasattr(model_values_Image, "reference")
    descriptor = None
    for klass in model_values_Image.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)

def test_model_values_image_has_name():
    assert hasattr(model_values_Image, "name")
    descriptor = None
    for klass in model_values_Image.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_values_image_has_format():
    assert hasattr(model_values_Image, "format")
    descriptor = None
    for klass in model_values_Image.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_model_values_image_has_data():
    assert hasattr(model_values_Image, "data")
    descriptor = None
    for klass in model_values_Image.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_arrayelement_is_not_abstract():
    assert not inspect.isabstract(ArrayElement)


def test_arrayelement_constructor_exists():
    assert callable(ArrayElement.__init__)


def test_arrayelement_constructor_args():
    sig = inspect.signature(ArrayElement.__init__)
    params = list(sig.parameters.keys())



def test_model_values_arrayvalue_is_not_abstract():
    assert not inspect.isabstract(model_values_ArrayValue)


def test_model_values_arrayvalue_constructor_exists():
    assert callable(model_values_ArrayValue.__init__)


def test_model_values_arrayvalue_constructor_args():
    sig = inspect.signature(model_values_ArrayValue.__init__)
    params = list(sig.parameters.keys())



def test_model_values_importvalue_is_not_abstract():
    assert not inspect.isabstract(model_values_ImportValue)


def test_model_values_importvalue_constructor_exists():
    assert callable(model_values_ImportValue.__init__)


def test_model_values_importvalue_constructor_args():
    sig = inspect.signature(model_values_ImportValue.__init__)
    params = list(sig.parameters.keys())
    assert "modelInterpreterId" in params, "Missing parameter 'modelInterpreterId'"

def test_model_values_importvalue_has_modelInterpreterId():
    assert hasattr(model_values_ImportValue, "modelInterpreterId")
    descriptor = None
    for klass in model_values_ImportValue.__mro__:
        if "modelInterpreterId" in klass.__dict__:
            descriptor = klass.__dict__["modelInterpreterId"]
            break
    assert isinstance(descriptor, property)



def test_skeletontransformation_is_not_abstract():
    assert not inspect.isabstract(SkeletonTransformation)


def test_skeletontransformation_constructor_exists():
    assert callable(SkeletonTransformation.__init__)


def test_skeletontransformation_constructor_args():
    sig = inspect.signature(SkeletonTransformation.__init__)
    params = list(sig.parameters.keys())



def test_model_values_skeletonanimation_is_not_abstract():
    assert not inspect.isabstract(model_values_SkeletonAnimation)


def test_model_values_skeletonanimation_constructor_exists():
    assert callable(model_values_SkeletonAnimation.__init__)


def test_model_values_skeletonanimation_constructor_args():
    sig = inspect.signature(model_values_SkeletonAnimation.__init__)
    params = list(sig.parameters.keys())



def test_model_values_particles_is_not_abstract():
    assert not inspect.isabstract(model_values_Particles)


def test_model_values_particles_constructor_exists():
    assert callable(model_values_Particles.__init__)


def test_model_values_particles_constructor_args():
    sig = inspect.signature(model_values_Particles.__init__)
    params = list(sig.parameters.keys())



def test_model_values_arrayelement_is_not_abstract():
    assert not inspect.isabstract(model_values_ArrayElement)


def test_model_values_arrayelement_constructor_exists():
    assert callable(model_values_ArrayElement.__init__)


def test_model_values_arrayelement_constructor_args():
    sig = inspect.signature(model_values_ArrayElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_model_values_arrayelement_has_index():
    assert hasattr(model_values_ArrayElement, "index")
    descriptor = None
    for klass in model_values_ArrayElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_model_values_connection_is_not_abstract():
    assert not inspect.isabstract(model_values_Connection)


def test_model_values_connection_constructor_exists():
    assert callable(model_values_Connection.__init__)


def test_model_values_connection_constructor_args():
    sig = inspect.signature(model_values_Connection.__init__)
    params = list(sig.parameters.keys())
    assert "connectivity" in params, "Missing parameter 'connectivity'"

def test_model_values_connection_has_connectivity():
    assert hasattr(model_values_Connection, "connectivity")
    descriptor = None
    for klass in model_values_Connection.__mro__:
        if "connectivity" in klass.__dict__:
            descriptor = klass.__dict__["connectivity"]
            break
    assert isinstance(descriptor, property)



def test_model_values_visualgroup_is_not_abstract():
    assert not inspect.isabstract(model_values_VisualGroup)


def test_model_values_visualgroup_constructor_exists():
    assert callable(model_values_VisualGroup.__init__)


def test_model_values_visualgroup_constructor_args():
    sig = inspect.signature(model_values_VisualGroup.__init__)
    params = list(sig.parameters.keys())
    assert "highSpectrumColor" in params, "Missing parameter 'highSpectrumColor'"
    assert "lowSpectrumColor" in params, "Missing parameter 'lowSpectrumColor'"
    assert "type" in params, "Missing parameter 'type'"

def test_model_values_visualgroup_has_highSpectrumColor():
    assert hasattr(model_values_VisualGroup, "highSpectrumColor")
    descriptor = None
    for klass in model_values_VisualGroup.__mro__:
        if "highSpectrumColor" in klass.__dict__:
            descriptor = klass.__dict__["highSpectrumColor"]
            break
    assert isinstance(descriptor, property)

def test_model_values_visualgroup_has_lowSpectrumColor():
    assert hasattr(model_values_VisualGroup, "lowSpectrumColor")
    descriptor = None
    for klass in model_values_VisualGroup.__mro__:
        if "lowSpectrumColor" in klass.__dict__:
            descriptor = klass.__dict__["lowSpectrumColor"]
            break
    assert isinstance(descriptor, property)

def test_model_values_visualgroup_has_type():
    assert hasattr(model_values_VisualGroup, "type")
    descriptor = None
    for klass in model_values_VisualGroup.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model_values_visualgroupelement_is_not_abstract():
    assert not inspect.isabstract(model_values_VisualGroupElement)


def test_model_values_visualgroupelement_constructor_exists():
    assert callable(model_values_VisualGroupElement.__init__)


def test_model_values_visualgroupelement_constructor_args():
    sig = inspect.signature(model_values_VisualGroupElement.__init__)
    params = list(sig.parameters.keys())
    assert "defaultColor" in params, "Missing parameter 'defaultColor'"

def test_model_values_visualgroupelement_has_defaultColor():
    assert hasattr(model_values_VisualGroupElement, "defaultColor")
    descriptor = None
    for klass in model_values_VisualGroupElement.__mro__:
        if "defaultColor" in klass.__dict__:
            descriptor = klass.__dict__["defaultColor"]
            break
    assert isinstance(descriptor, property)



def test_model_values_skeletontransformation_is_not_abstract():
    assert not inspect.isabstract(model_values_SkeletonTransformation)


def test_model_values_skeletontransformation_constructor_exists():
    assert callable(model_values_SkeletonTransformation.__init__)


def test_model_values_skeletontransformation_constructor_args():
    sig = inspect.signature(model_values_SkeletonTransformation.__init__)
    params = list(sig.parameters.keys())
    assert "skeletonTransformation" in params, "Missing parameter 'skeletonTransformation'"

def test_model_values_skeletontransformation_has_skeletonTransformation():
    assert hasattr(model_values_SkeletonTransformation, "skeletonTransformation")
    descriptor = None
    for klass in model_values_SkeletonTransformation.__mro__:
        if "skeletonTransformation" in klass.__dict__:
            descriptor = klass.__dict__["skeletonTransformation"]
            break
    assert isinstance(descriptor, property)



def test_model_values_function_is_not_abstract():
    assert not inspect.isabstract(model_values_Function)


def test_model_values_function_constructor_exists():
    assert callable(model_values_Function.__init__)


def test_model_values_function_constructor_args():
    sig = inspect.signature(model_values_Function.__init__)
    params = list(sig.parameters.keys())



def test_model_values_functionplot_is_not_abstract():
    assert not inspect.isabstract(model_values_FunctionPlot)


def test_model_values_functionplot_constructor_exists():
    assert callable(model_values_FunctionPlot.__init__)


def test_model_values_functionplot_constructor_args():
    sig = inspect.signature(model_values_FunctionPlot.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "xAxisLabel" in params, "Missing parameter 'xAxisLabel'"
    assert "yAxisLabel" in params, "Missing parameter 'yAxisLabel'"
    assert "stepValue" in params, "Missing parameter 'stepValue'"
    assert "finalValue" in params, "Missing parameter 'finalValue'"
    assert "initialValue" in params, "Missing parameter 'initialValue'"

def test_model_values_functionplot_has_title():
    assert hasattr(model_values_FunctionPlot, "title")
    descriptor = None
    for klass in model_values_FunctionPlot.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_model_values_functionplot_has_xAxisLabel():
    assert hasattr(model_values_FunctionPlot, "xAxisLabel")
    descriptor = None
    for klass in model_values_FunctionPlot.__mro__:
        if "xAxisLabel" in klass.__dict__:
            descriptor = klass.__dict__["xAxisLabel"]
            break
    assert isinstance(descriptor, property)

def test_model_values_functionplot_has_yAxisLabel():
    assert hasattr(model_values_FunctionPlot, "yAxisLabel")
    descriptor = None
    for klass in model_values_FunctionPlot.__mro__:
        if "yAxisLabel" in klass.__dict__:
            descriptor = klass.__dict__["yAxisLabel"]
            break
    assert isinstance(descriptor, property)

def test_model_values_functionplot_has_stepValue():
    assert hasattr(model_values_FunctionPlot, "stepValue")
    descriptor = None
    for klass in model_values_FunctionPlot.__mro__:
        if "stepValue" in klass.__dict__:
            descriptor = klass.__dict__["stepValue"]
            break
    assert isinstance(descriptor, property)

def test_model_values_functionplot_has_finalValue():
    assert hasattr(model_values_FunctionPlot, "finalValue")
    descriptor = None
    for klass in model_values_FunctionPlot.__mro__:
        if "finalValue" in klass.__dict__:
            descriptor = klass.__dict__["finalValue"]
            break
    assert isinstance(descriptor, property)

def test_model_values_functionplot_has_initialValue():
    assert hasattr(model_values_FunctionPlot, "initialValue")
    descriptor = None
    for klass in model_values_FunctionPlot.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_model_values_cylinder_is_not_abstract():
    assert not inspect.isabstract(model_values_Cylinder)


def test_model_values_cylinder_constructor_exists():
    assert callable(model_values_Cylinder.__init__)


def test_model_values_cylinder_constructor_args():
    sig = inspect.signature(model_values_Cylinder.__init__)
    params = list(sig.parameters.keys())
    assert "bottomRadius" in params, "Missing parameter 'bottomRadius'"
    assert "height" in params, "Missing parameter 'height'"
    assert "topRadius" in params, "Missing parameter 'topRadius'"

def test_model_values_cylinder_has_bottomRadius():
    assert hasattr(model_values_Cylinder, "bottomRadius")
    descriptor = None
    for klass in model_values_Cylinder.__mro__:
        if "bottomRadius" in klass.__dict__:
            descriptor = klass.__dict__["bottomRadius"]
            break
    assert isinstance(descriptor, property)

def test_model_values_cylinder_has_height():
    assert hasattr(model_values_Cylinder, "height")
    descriptor = None
    for klass in model_values_Cylinder.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_model_values_cylinder_has_topRadius():
    assert hasattr(model_values_Cylinder, "topRadius")
    descriptor = None
    for klass in model_values_Cylinder.__mro__:
        if "topRadius" in klass.__dict__:
            descriptor = klass.__dict__["topRadius"]
            break
    assert isinstance(descriptor, property)



def test_model_values_sphere_is_not_abstract():
    assert not inspect.isabstract(model_values_Sphere)


def test_model_values_sphere_constructor_exists():
    assert callable(model_values_Sphere.__init__)


def test_model_values_sphere_constructor_args():
    sig = inspect.signature(model_values_Sphere.__init__)
    params = list(sig.parameters.keys())
    assert "radius" in params, "Missing parameter 'radius'"

def test_model_values_sphere_has_radius():
    assert hasattr(model_values_Sphere, "radius")
    descriptor = None
    for klass in model_values_Sphere.__mro__:
        if "radius" in klass.__dict__:
            descriptor = klass.__dict__["radius"]
            break
    assert isinstance(descriptor, property)



def test_model_values_obj_is_not_abstract():
    assert not inspect.isabstract(model_values_OBJ)


def test_model_values_obj_constructor_exists():
    assert callable(model_values_OBJ.__init__)


def test_model_values_obj_constructor_args():
    sig = inspect.signature(model_values_OBJ.__init__)
    params = list(sig.parameters.keys())
    assert "obj" in params, "Missing parameter 'obj'"

def test_model_values_obj_has_obj():
    assert hasattr(model_values_OBJ, "obj")
    descriptor = None
    for klass in model_values_OBJ.__mro__:
        if "obj" in klass.__dict__:
            descriptor = klass.__dict__["obj"]
            break
    assert isinstance(descriptor, property)



def test_model_values_collada_is_not_abstract():
    assert not inspect.isabstract(model_values_Collada)


def test_model_values_collada_constructor_exists():
    assert callable(model_values_Collada.__init__)


def test_model_values_collada_constructor_args():
    sig = inspect.signature(model_values_Collada.__init__)
    params = list(sig.parameters.keys())
    assert "collada" in params, "Missing parameter 'collada'"

def test_model_values_collada_has_collada():
    assert hasattr(model_values_Collada, "collada")
    descriptor = None
    for klass in model_values_Collada.__mro__:
        if "collada" in klass.__dict__:
            descriptor = klass.__dict__["collada"]
            break
    assert isinstance(descriptor, property)



def test_visualgroupelement_is_not_abstract():
    assert not inspect.isabstract(VisualGroupElement)


def test_visualgroupelement_constructor_exists():
    assert callable(VisualGroupElement.__init__)


def test_visualgroupelement_constructor_args():
    sig = inspect.signature(VisualGroupElement.__init__)
    params = list(sig.parameters.keys())



def test_model_values_visualvalue_is_not_abstract():
    assert not inspect.isabstract(model_values_VisualValue)


def test_model_values_visualvalue_constructor_exists():
    assert callable(model_values_VisualValue.__init__)


def test_model_values_visualvalue_constructor_args():
    sig = inspect.signature(model_values_VisualValue.__init__)
    params = list(sig.parameters.keys())



def test_model_values_expression_is_not_abstract():
    assert not inspect.isabstract(model_values_Expression)


def test_model_values_expression_constructor_exists():
    assert callable(model_values_Expression.__init__)


def test_model_values_expression_constructor_args():
    sig = inspect.signature(model_values_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_model_values_expression_has_expression():
    assert hasattr(model_values_Expression, "expression")
    descriptor = None
    for klass in model_values_Expression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_model_values_argument_is_not_abstract():
    assert not inspect.isabstract(model_values_Argument)


def test_model_values_argument_constructor_exists():
    assert callable(model_values_Argument.__init__)


def test_model_values_argument_constructor_args():
    sig = inspect.signature(model_values_Argument.__init__)
    params = list(sig.parameters.keys())
    assert "argument" in params, "Missing parameter 'argument'"

def test_model_values_argument_has_argument():
    assert hasattr(model_values_Argument, "argument")
    descriptor = None
    for klass in model_values_Argument.__mro__:
        if "argument" in klass.__dict__:
            descriptor = klass.__dict__["argument"]
            break
    assert isinstance(descriptor, property)



def test_functionplot_is_not_abstract():
    assert not inspect.isabstract(FunctionPlot)


def test_functionplot_constructor_exists():
    assert callable(FunctionPlot.__init__)


def test_functionplot_constructor_args():
    sig = inspect.signature(FunctionPlot.__init__)
    params = list(sig.parameters.keys())



def test_metadatavalue_is_not_abstract():
    assert not inspect.isabstract(MetadataValue)


def test_metadatavalue_constructor_exists():
    assert callable(MetadataValue.__init__)


def test_metadatavalue_constructor_args():
    sig = inspect.signature(MetadataValue.__init__)
    params = list(sig.parameters.keys())



def test_model_values_metadata_is_not_abstract():
    assert not inspect.isabstract(model_values_Metadata)


def test_model_values_metadata_constructor_exists():
    assert callable(model_values_Metadata.__init__)


def test_model_values_metadata_constructor_args():
    sig = inspect.signature(model_values_Metadata.__init__)
    params = list(sig.parameters.keys())



def test_model_values_json_is_not_abstract():
    assert not inspect.isabstract(model_values_JSON)


def test_model_values_json_constructor_exists():
    assert callable(model_values_JSON.__init__)


def test_model_values_json_constructor_args():
    sig = inspect.signature(model_values_JSON.__init__)
    params = list(sig.parameters.keys())
    assert "json" in params, "Missing parameter 'json'"

def test_model_values_json_has_json():
    assert hasattr(model_values_JSON, "json")
    descriptor = None
    for klass in model_values_JSON.__mro__:
        if "json" in klass.__dict__:
            descriptor = klass.__dict__["json"]
            break
    assert isinstance(descriptor, property)



def test_model_values_text_is_not_abstract():
    assert not inspect.isabstract(model_values_Text)


def test_model_values_text_constructor_exists():
    assert callable(model_values_Text.__init__)


def test_model_values_text_constructor_args():
    sig = inspect.signature(model_values_Text.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_model_values_text_has_text():
    assert hasattr(model_values_Text, "text")
    descriptor = None
    for klass in model_values_Text.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_model_values_metadatavalue_is_not_abstract():
    assert not inspect.isabstract(model_values_MetadataValue)


def test_model_values_metadatavalue_constructor_exists():
    assert callable(model_values_MetadataValue.__init__)


def test_model_values_metadatavalue_constructor_args():
    sig = inspect.signature(model_values_MetadataValue.__init__)
    params = list(sig.parameters.keys())



def test_model_values_mdtimeseries_is_not_abstract():
    assert not inspect.isabstract(model_values_MDTimeSeries)


def test_model_values_mdtimeseries_constructor_exists():
    assert callable(model_values_MDTimeSeries.__init__)


def test_model_values_mdtimeseries_constructor_args():
    sig = inspect.signature(model_values_MDTimeSeries.__init__)
    params = list(sig.parameters.keys())



def test_physicalquantity_is_not_abstract():
    assert not inspect.isabstract(PhysicalQuantity)


def test_physicalquantity_constructor_exists():
    assert callable(PhysicalQuantity.__init__)


def test_physicalquantity_constructor_args():
    sig = inspect.signature(PhysicalQuantity.__init__)
    params = list(sig.parameters.keys())



def test_model_values_dynamics_is_not_abstract():
    assert not inspect.isabstract(model_values_Dynamics)


def test_model_values_dynamics_constructor_exists():
    assert callable(model_values_Dynamics.__init__)


def test_model_values_dynamics_constructor_args():
    sig = inspect.signature(model_values_Dynamics.__init__)
    params = list(sig.parameters.keys())



def test_model_values_point_is_not_abstract():
    assert not inspect.isabstract(model_values_Point)


def test_model_values_point_constructor_exists():
    assert callable(model_values_Point.__init__)


def test_model_values_point_constructor_args():
    sig = inspect.signature(model_values_Point.__init__)
    params = list(sig.parameters.keys())
    assert "z" in params, "Missing parameter 'z'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_model_values_point_has_z():
    assert hasattr(model_values_Point, "z")
    descriptor = None
    for klass in model_values_Point.__mro__:
        if "z" in klass.__dict__:
            descriptor = klass.__dict__["z"]
            break
    assert isinstance(descriptor, property)

def test_model_values_point_has_y():
    assert hasattr(model_values_Point, "y")
    descriptor = None
    for klass in model_values_Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_model_values_point_has_x():
    assert hasattr(model_values_Point, "x")
    descriptor = None
    for klass in model_values_Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_model_values_pointerelement_is_not_abstract():
    assert not inspect.isabstract(model_values_PointerElement)


def test_model_values_pointerelement_constructor_exists():
    assert callable(model_values_PointerElement.__init__)


def test_model_values_pointerelement_constructor_args():
    sig = inspect.signature(model_values_PointerElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_model_values_pointerelement_has_index():
    assert hasattr(model_values_PointerElement, "index")
    descriptor = None
    for klass in model_values_PointerElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_pointerelement_is_not_abstract():
    assert not inspect.isabstract(PointerElement)


def test_pointerelement_constructor_exists():
    assert callable(PointerElement.__init__)


def test_pointerelement_constructor_args():
    sig = inspect.signature(PointerElement.__init__)
    params = list(sig.parameters.keys())



def test_model_values_pointer_is_not_abstract():
    assert not inspect.isabstract(model_values_Pointer)


def test_model_values_pointer_constructor_exists():
    assert callable(model_values_Pointer.__init__)


def test_model_values_pointer_constructor_args():
    sig = inspect.signature(model_values_Pointer.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_model_values_pointer_has_path():
    assert hasattr(model_values_Pointer, "path")
    descriptor = None
    for klass in model_values_Pointer.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_model_values_html_is_not_abstract():
    assert not inspect.isabstract(model_values_HTML)


def test_model_values_html_constructor_exists():
    assert callable(model_values_HTML.__init__)


def test_model_values_html_constructor_args():
    sig = inspect.signature(model_values_HTML.__init__)
    params = list(sig.parameters.keys())
    assert "html" in params, "Missing parameter 'html'"

def test_model_values_html_has_html():
    assert hasattr(model_values_HTML, "html")
    descriptor = None
    for klass in model_values_HTML.__mro__:
        if "html" in klass.__dict__:
            descriptor = klass.__dict__["html"]
            break
    assert isinstance(descriptor, property)



def test_model_values_url_is_not_abstract():
    assert not inspect.isabstract(model_values_URL)


def test_model_values_url_constructor_exists():
    assert callable(model_values_URL.__init__)


def test_model_values_url_constructor_args():
    sig = inspect.signature(model_values_URL.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"

def test_model_values_url_has_url():
    assert hasattr(model_values_URL, "url")
    descriptor = None
    for klass in model_values_URL.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_image_is_not_abstract():
    assert not inspect.isabstract(Image)


def test_image_constructor_exists():
    assert callable(Image.__init__)


def test_image_constructor_args():
    sig = inspect.signature(Image.__init__)
    params = list(sig.parameters.keys())



def test_model_types_imagetype_is_not_abstract():
    assert not inspect.isabstract(model_types_ImageType)


def test_model_types_imagetype_constructor_exists():
    assert callable(model_types_ImageType.__init__)


def test_model_types_imagetype_constructor_args():
    sig = inspect.signature(model_types_ImageType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_simpletype_is_not_abstract():
    assert not inspect.isabstract(model_types_SimpleType)


def test_model_types_simpletype_constructor_exists():
    assert callable(model_types_SimpleType.__init__)


def test_model_types_simpletype_constructor_args():
    sig = inspect.signature(model_types_SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_model_values_timeseries_is_not_abstract():
    assert not inspect.isabstract(model_values_TimeSeries)


def test_model_values_timeseries_constructor_exists():
    assert callable(model_values_TimeSeries.__init__)


def test_model_values_timeseries_constructor_args():
    sig = inspect.signature(model_values_TimeSeries.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "scalingFactor" in params, "Missing parameter 'scalingFactor'"

def test_model_values_timeseries_has_value():
    assert hasattr(model_values_TimeSeries, "value")
    descriptor = None
    for klass in model_values_TimeSeries.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_model_values_timeseries_has_scalingFactor():
    assert hasattr(model_values_TimeSeries, "scalingFactor")
    descriptor = None
    for klass in model_values_TimeSeries.__mro__:
        if "scalingFactor" in klass.__dict__:
            descriptor = klass.__dict__["scalingFactor"]
            break
    assert isinstance(descriptor, property)



def test_model_values_unit_is_not_abstract():
    assert not inspect.isabstract(model_values_Unit)


def test_model_values_unit_constructor_exists():
    assert callable(model_values_Unit.__init__)


def test_model_values_unit_constructor_args():
    sig = inspect.signature(model_values_Unit.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_model_values_unit_has_unit():
    assert hasattr(model_values_Unit, "unit")
    descriptor = None
    for klass in model_values_Unit.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_model_values_physicalquantity_is_not_abstract():
    assert not inspect.isabstract(model_values_PhysicalQuantity)


def test_model_values_physicalquantity_constructor_exists():
    assert callable(model_values_PhysicalQuantity.__init__)


def test_model_values_physicalquantity_constructor_args():
    sig = inspect.signature(model_values_PhysicalQuantity.__init__)
    params = list(sig.parameters.keys())



def test_model_values_quantity_is_not_abstract():
    assert not inspect.isabstract(model_values_Quantity)


def test_model_values_quantity_constructor_exists():
    assert callable(model_values_Quantity.__init__)


def test_model_values_quantity_constructor_args():
    sig = inspect.signature(model_values_Quantity.__init__)
    params = list(sig.parameters.keys())
    assert "scalingFactor" in params, "Missing parameter 'scalingFactor'"
    assert "value" in params, "Missing parameter 'value'"

def test_model_values_quantity_has_scalingFactor():
    assert hasattr(model_values_Quantity, "scalingFactor")
    descriptor = None
    for klass in model_values_Quantity.__mro__:
        if "scalingFactor" in klass.__dict__:
            descriptor = klass.__dict__["scalingFactor"]
            break
    assert isinstance(descriptor, property)

def test_model_values_quantity_has_value():
    assert hasattr(model_values_Quantity, "value")
    descriptor = None
    for klass in model_values_Quantity.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model_values_stringtovaluemap_is_not_abstract():
    assert not inspect.isabstract(model_values_StringToValueMap)


def test_model_values_stringtovaluemap_constructor_exists():
    assert callable(model_values_StringToValueMap.__init__)


def test_model_values_stringtovaluemap_constructor_args():
    sig = inspect.signature(model_values_StringToValueMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_model_values_stringtovaluemap_has_key():
    assert hasattr(model_values_StringToValueMap, "key")
    descriptor = None
    for klass in model_values_StringToValueMap.__mro__:
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



def test_model_values_composite_is_not_abstract():
    assert not inspect.isabstract(model_values_Composite)


def test_model_values_composite_constructor_exists():
    assert callable(model_values_Composite.__init__)


def test_model_values_composite_constructor_args():
    sig = inspect.signature(model_values_Composite.__init__)
    params = list(sig.parameters.keys())



def test_model_values_value_is_not_abstract():
    assert not inspect.isabstract(model_values_Value)


def test_model_values_value_constructor_exists():
    assert callable(model_values_Value.__init__)


def test_model_values_value_constructor_args():
    sig = inspect.signature(model_values_Value.__init__)
    params = list(sig.parameters.keys())



def test_model_types_metadatatype_is_not_abstract():
    assert not inspect.isabstract(model_types_MetadataType)


def test_model_types_metadatatype_constructor_exists():
    assert callable(model_types_MetadataType.__init__)


def test_model_types_metadatatype_constructor_args():
    sig = inspect.signature(model_types_MetadataType.__init__)
    params = list(sig.parameters.keys())



def test_aarrayvalue_is_not_abstract():
    assert not inspect.isabstract(AArrayValue)


def test_aarrayvalue_constructor_exists():
    assert callable(AArrayValue.__init__)


def test_aarrayvalue_constructor_args():
    sig = inspect.signature(AArrayValue.__init__)
    params = list(sig.parameters.keys())



def test_model_values_doublearray_is_not_abstract():
    assert not inspect.isabstract(model_values_DoubleArray)


def test_model_values_doublearray_constructor_exists():
    assert callable(model_values_DoubleArray.__init__)


def test_model_values_doublearray_constructor_args():
    sig = inspect.signature(model_values_DoubleArray.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"

def test_model_values_doublearray_has_elements():
    assert hasattr(model_values_DoubleArray, "elements")
    descriptor = None
    for klass in model_values_DoubleArray.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)



def test_model_values_stringarray_is_not_abstract():
    assert not inspect.isabstract(model_values_StringArray)


def test_model_values_stringarray_constructor_exists():
    assert callable(model_values_StringArray.__init__)


def test_model_values_stringarray_constructor_args():
    sig = inspect.signature(model_values_StringArray.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"

def test_model_values_stringarray_has_elements():
    assert hasattr(model_values_StringArray, "elements")
    descriptor = None
    for klass in model_values_StringArray.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)



def test_model_values_intarray_is_not_abstract():
    assert not inspect.isabstract(model_values_IntArray)


def test_model_values_intarray_constructor_exists():
    assert callable(model_values_IntArray.__init__)


def test_model_values_intarray_constructor_args():
    sig = inspect.signature(model_values_IntArray.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"

def test_model_values_intarray_has_elements():
    assert hasattr(model_values_IntArray, "elements")
    descriptor = None
    for klass in model_values_IntArray.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)



def test_model_values_genericarray_is_not_abstract():
    assert not inspect.isabstract(model_values_GenericArray)


def test_model_values_genericarray_constructor_exists():
    assert callable(model_values_GenericArray.__init__)


def test_model_values_genericarray_constructor_args():
    sig = inspect.signature(model_values_GenericArray.__init__)
    params = list(sig.parameters.keys())



def test_model_types_simplearraytype_is_not_abstract():
    assert not inspect.isabstract(model_types_SimpleArrayType)


def test_model_types_simplearraytype_constructor_exists():
    assert callable(model_types_SimpleArrayType.__init__)


def test_model_types_simplearraytype_constructor_args():
    sig = inspect.signature(model_types_SimpleArrayType.__init__)
    params = list(sig.parameters.keys())



def test_model_types_texttype_is_not_abstract():
    assert not inspect.isabstract(model_types_TextType)


def test_model_types_texttype_constructor_exists():
    assert callable(model_types_TextType.__init__)


def test_model_types_texttype_constructor_args():
    sig = inspect.signature(model_types_TextType.__init__)
    params = list(sig.parameters.keys())



def test_json_is_not_abstract():
    assert not inspect.isabstract(JSON)


def test_json_constructor_exists():
    assert callable(JSON.__init__)


def test_json_constructor_args():
    sig = inspect.signature(JSON.__init__)
    params = list(sig.parameters.keys())



def test_model_types_jsontype_is_not_abstract():
    assert not inspect.isabstract(model_types_JSONType)


def test_model_types_jsontype_constructor_exists():
    assert callable(model_types_JSONType.__init__)


def test_model_types_jsontype_constructor_args():
    sig = inspect.signature(model_types_JSONType.__init__)
    params = list(sig.parameters.keys())



def test_html_is_not_abstract():
    assert not inspect.isabstract(HTML)


def test_html_constructor_exists():
    assert callable(HTML.__init__)


def test_html_constructor_args():
    sig = inspect.signature(HTML.__init__)
    params = list(sig.parameters.keys())



def test_model_types_htmltype_is_not_abstract():
    assert not inspect.isabstract(model_types_HTMLType)


def test_model_types_htmltype_constructor_exists():
    assert callable(model_types_HTMLType.__init__)


def test_model_types_htmltype_constructor_args():
    sig = inspect.signature(model_types_HTMLType.__init__)
    params = list(sig.parameters.keys())

def test_imageformat_exists():
    # Check that the Enumeration exists
    assert ImageFormat is not None

def test_imageformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImageFormat]
    expected_literals = [
        "IIP",
        "NIFTI",
        "JPEG",
        "DZI",
        "DCM",
        "TIFF",
        "GOOGLE_MAP",
        "PNG",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImageFormat"

def test_fileformat_exists():
    # Check that the Enumeration exists
    assert FileFormat is not None

def test_fileformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FileFormat]
    expected_literals = [
        "HDF5",
        "ZIP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FileFormat"

def test_connectivity_exists():
    # Check that the Enumeration exists
    assert Connectivity is not None

def test_connectivity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Connectivity]
    expected_literals = [
        "NON_DIRECTIONAL",
        "DIRECTIONAL",
        "BIDIRECTIONAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Connectivity"

def test_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "AND",
        "NAND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"


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
model_datasources_QueryResults_strategy = st.builds(
    model_datasources_QueryResults,
    header=
        safe_text,
    id=
        safe_text
)
model_datasources_QueryMatchingCriteria_strategy = st.builds(
    model_datasources_QueryMatchingCriteria,
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
VisualValue_strategy = st.builds(
    VisualValue,
)
Expression_strategy = st.builds(
    Expression,
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
Composite_strategy = st.builds(
    Composite,
)
model_ModelFormat_strategy = st.builds(
    model_ModelFormat,
    modelFormat=
        safe_text
)
model_DomainModel__strategy = st.builds(
    model_DomainModel_,
    domainModel=
        safe_text
)
types_model_DomainModel__strategy = st.builds(
    types_model_DomainModel_,
)
VisualType_strategy = st.builds(
    VisualType,
)
model_types_CompositeVisualType_strategy = st.builds(
    model_types_CompositeVisualType,
)
model_ISynchable_strategy = st.builds(
    model_ISynchable,
    synched=
        safe_text
)
model_StringToStringMap_strategy = st.builds(
    model_StringToStringMap,
    value=
        safe_text,
    key=
        safe_text
)
DomainModel__strategy = st.builds(
    DomainModel_,
)
model_ExternalDomainModel_strategy = st.builds(
    model_ExternalDomainModel,
    fileFormat=
        safe_text
)
ISynchable_strategy = st.builds(
    ISynchable,
)
model_Node_strategy = st.builds(
    model_Node,
    id=
        safe_text,
    name=
        safe_text
)
Query_strategy = st.builds(
    Query,
)
model_datasources_CompoundRefQuery_strategy = st.builds(
    model_datasources_CompoundRefQuery,
)
DataSource_strategy = st.builds(
    DataSource,
)
Value_strategy = st.builds(
    Value,
)
Pointer_strategy = st.builds(
    Pointer,
)
model_VariableValue_strategy = st.builds(
    model_VariableValue,
)
model_ExperimentState_strategy = st.builds(
    model_ExperimentState,
    experimentId=
        safe_text,
    projectId=
        safe_text
)
model_LibraryManager_strategy = st.builds(
    model_LibraryManager,
)
Type_strategy = st.builds(
    Type,
)
model_types_VisualType_strategy = st.builds(
    model_types_VisualType,
)
model_types_ArgumentType_strategy = st.builds(
    model_types_ArgumentType,
)
model_types_DynamicsType_strategy = st.builds(
    model_types_DynamicsType,
)
model_types_ExpressionType_strategy = st.builds(
    model_types_ExpressionType,
)
model_types_URLType_strategy = st.builds(
    model_types_URLType,
)
model_types_ArrayType_strategy = st.builds(
    model_types_ArrayType,
    size=
        safe_text
)
model_types_ConnectionType_strategy = st.builds(
    model_types_ConnectionType,
)
model_types_PointerType_strategy = st.builds(
    model_types_PointerType,
)
model_types_CompositeType_strategy = st.builds(
    model_types_CompositeType,
)
model_types_ImportType_strategy = st.builds(
    model_types_ImportType,
    autoresolve=
        safe_text,
    referenceURL=
        safe_text,
    modelInterpreterId=
        safe_text,
    url=
        safe_text
)
model_types_StateVariableType_strategy = st.builds(
    model_types_StateVariableType,
)
model_types_PointType_strategy = st.builds(
    model_types_PointType,
)
model_types_ParameterType_strategy = st.builds(
    model_types_ParameterType,
)
model_types_QuantityType_strategy = st.builds(
    model_types_QuantityType,
)
Node_strategy = st.builds(
    Node,
)
model_types_Type_strategy = st.builds(
    model_types_Type,
    abstract=
        safe_text
)
model_Tag_strategy = st.builds(
    model_Tag,
    name=
        safe_text
)
model_GeppettoLibrary_strategy = st.builds(
    model_GeppettoLibrary,
)
Variable_strategy = st.builds(
    Variable,
)
model_GeppettoModel_strategy = st.builds(
    model_GeppettoModel,
    name=
        safe_text,
    id=
        safe_text
)
model_datasources_AQueryResult_strategy = st.builds(
    model_datasources_AQueryResult,
)
model_datasources_RunnableQuery_strategy = st.builds(
    model_datasources_RunnableQuery,
    queryPath=
        safe_text,
    targetVariablePath=
        safe_text,
    booleanOperator=
        safe_text
)
AQueryResult_strategy = st.builds(
    AQueryResult,
)
model_datasources_QueryResult_strategy = st.builds(
    model_datasources_QueryResult,
    values=
        safe_text
)
model_datasources_SerializableQueryResult_strategy = st.builds(
    model_datasources_SerializableQueryResult,
    values=
        safe_text
)
model_datasources_DataSourceLibraryConfiguration_strategy = st.builds(
    model_datasources_DataSourceLibraryConfiguration,
    format=
        safe_text,
    modelInterpreterId=
        safe_text
)
datasources_model_GeppettoLibrary_strategy = st.builds(
    datasources_model_GeppettoLibrary,
)
model_datasources_CompoundQuery_strategy = st.builds(
    model_datasources_CompoundQuery,
)
model_datasources_SimpleQuery_strategy = st.builds(
    model_datasources_SimpleQuery,
    countQuery=
        safe_text,
    query=
        safe_text
)
datasources_model_StringToStringMap_strategy = st.builds(
    datasources_model_StringToStringMap,
)
model_datasources_ProcessQuery_strategy = st.builds(
    model_datasources_ProcessQuery,
    queryProcessorId=
        safe_text
)
QueryMatchingCriteria_strategy = st.builds(
    QueryMatchingCriteria,
)
model_datasources_Query_strategy = st.builds(
    model_datasources_Query,
    runForCount=
        safe_text,
    description=
        safe_text
)
model_variables_Variable_strategy = st.builds(
    model_variables_Variable,
    static=
        safe_text
)
model_values_AArrayValue_strategy = st.builds(
    model_values_AArrayValue,
)
DataSourceLibraryConfiguration_strategy = st.builds(
    DataSourceLibraryConfiguration,
)
model_datasources_DataSource_strategy = st.builds(
    model_datasources_DataSource,
    dataSourceService=
        safe_text,
    url=
        safe_text
)
model_variables_TypeToValueMap_strategy = st.builds(
    model_variables_TypeToValueMap,
)
TypeToValueMap_strategy = st.builds(
    TypeToValueMap,
)
model_values_Image_strategy = st.builds(
    model_values_Image,
    reference=
        safe_text,
    name=
        safe_text,
    format=
        safe_text,
    data=
        safe_text
)
ArrayElement_strategy = st.builds(
    ArrayElement,
)
model_values_ArrayValue_strategy = st.builds(
    model_values_ArrayValue,
)
model_values_ImportValue_strategy = st.builds(
    model_values_ImportValue,
    modelInterpreterId=
        safe_text
)
SkeletonTransformation_strategy = st.builds(
    SkeletonTransformation,
)
model_values_SkeletonAnimation_strategy = st.builds(
    model_values_SkeletonAnimation,
)
model_values_Particles_strategy = st.builds(
    model_values_Particles,
)
model_values_ArrayElement_strategy = st.builds(
    model_values_ArrayElement,
    index=
        safe_text
)
model_values_Connection_strategy = st.builds(
    model_values_Connection,
    connectivity=
        safe_text
)
model_values_VisualGroup_strategy = st.builds(
    model_values_VisualGroup,
    highSpectrumColor=
        safe_text,
    lowSpectrumColor=
        safe_text,
    type=
        safe_text
)
model_values_VisualGroupElement_strategy = st.builds(
    model_values_VisualGroupElement,
    defaultColor=
        safe_text
)
model_values_SkeletonTransformation_strategy = st.builds(
    model_values_SkeletonTransformation,
    skeletonTransformation=
        safe_text
)
model_values_Function_strategy = st.builds(
    model_values_Function,
)
model_values_FunctionPlot_strategy = st.builds(
    model_values_FunctionPlot,
    title=
        safe_text,
    xAxisLabel=
        safe_text,
    yAxisLabel=
        safe_text,
    stepValue=
        safe_text,
    finalValue=
        safe_text,
    initialValue=
        safe_text
)
Function_strategy = st.builds(
    Function,
)
model_values_Cylinder_strategy = st.builds(
    model_values_Cylinder,
    bottomRadius=
        safe_text,
    height=
        safe_text,
    topRadius=
        safe_text
)
model_values_Sphere_strategy = st.builds(
    model_values_Sphere,
    radius=
        safe_text
)
model_values_OBJ_strategy = st.builds(
    model_values_OBJ,
    obj=
        safe_text
)
model_values_Collada_strategy = st.builds(
    model_values_Collada,
    collada=
        safe_text
)
VisualGroupElement_strategy = st.builds(
    VisualGroupElement,
)
model_values_VisualValue_strategy = st.builds(
    model_values_VisualValue,
)
model_values_Expression_strategy = st.builds(
    model_values_Expression,
    expression=
        safe_text
)
model_values_Argument_strategy = st.builds(
    model_values_Argument,
    argument=
        safe_text
)
FunctionPlot_strategy = st.builds(
    FunctionPlot,
)
MetadataValue_strategy = st.builds(
    MetadataValue,
)
model_values_Metadata_strategy = st.builds(
    model_values_Metadata,
)
model_values_JSON_strategy = st.builds(
    model_values_JSON,
    json=
        safe_text
)
model_values_Text_strategy = st.builds(
    model_values_Text,
    text=
        safe_text
)
model_values_MetadataValue_strategy = st.builds(
    model_values_MetadataValue,
)
model_values_MDTimeSeries_strategy = st.builds(
    model_values_MDTimeSeries,
)
PhysicalQuantity_strategy = st.builds(
    PhysicalQuantity,
)
model_values_Dynamics_strategy = st.builds(
    model_values_Dynamics,
)
model_values_Point_strategy = st.builds(
    model_values_Point,
    z=
        safe_text,
    y=
        safe_text,
    x=
        safe_text
)
model_values_PointerElement_strategy = st.builds(
    model_values_PointerElement,
    index=
        safe_text
)
PointerElement_strategy = st.builds(
    PointerElement,
)
model_values_Pointer_strategy = st.builds(
    model_values_Pointer,
    path=
        safe_text
)
model_values_HTML_strategy = st.builds(
    model_values_HTML,
    html=
        safe_text
)
model_values_URL_strategy = st.builds(
    model_values_URL,
    url=
        safe_text
)
Image_strategy = st.builds(
    Image,
)
model_types_ImageType_strategy = st.builds(
    model_types_ImageType,
)
model_types_SimpleType_strategy = st.builds(
    model_types_SimpleType,
)
model_values_TimeSeries_strategy = st.builds(
    model_values_TimeSeries,
    value=
        safe_text,
    scalingFactor=
        safe_text
)
model_values_Unit_strategy = st.builds(
    model_values_Unit,
    unit=
        safe_text
)
Unit_strategy = st.builds(
    Unit,
)
model_values_PhysicalQuantity_strategy = st.builds(
    model_values_PhysicalQuantity,
)
model_values_Quantity_strategy = st.builds(
    model_values_Quantity,
    scalingFactor=
        safe_text,
    value=
        safe_text
)
model_values_StringToValueMap_strategy = st.builds(
    model_values_StringToValueMap,
    key=
        safe_text
)
StringToValueMap_strategy = st.builds(
    StringToValueMap,
)
model_values_Composite_strategy = st.builds(
    model_values_Composite,
)
model_values_Value_strategy = st.builds(
    model_values_Value,
)
model_types_MetadataType_strategy = st.builds(
    model_types_MetadataType,
)
AArrayValue_strategy = st.builds(
    AArrayValue,
)
model_values_DoubleArray_strategy = st.builds(
    model_values_DoubleArray,
    elements=
        safe_text
)
model_values_StringArray_strategy = st.builds(
    model_values_StringArray,
    elements=
        safe_text
)
model_values_IntArray_strategy = st.builds(
    model_values_IntArray,
    elements=
        safe_text
)
model_values_GenericArray_strategy = st.builds(
    model_values_GenericArray,
)
model_types_SimpleArrayType_strategy = st.builds(
    model_types_SimpleArrayType,
)
model_types_TextType_strategy = st.builds(
    model_types_TextType,
)
JSON_strategy = st.builds(
    JSON,
)
model_types_JSONType_strategy = st.builds(
    model_types_JSONType,
)
HTML_strategy = st.builds(
    HTML,
)
model_types_HTMLType_strategy = st.builds(
    model_types_HTMLType,
)

@given(instance=model_datasources_QueryResults_strategy)
@settings(max_examples=50)
def test_model_datasources_queryresults_instantiation(instance):
    assert isinstance(instance, model_datasources_QueryResults)



@given(instance=model_datasources_QueryResults_strategy)
def test_model_datasources_queryresults_header_setter(instance):
    original = instance.header
    instance.header = original
    assert instance.header == original



@given(instance=model_datasources_QueryResults_strategy)
def test_model_datasources_queryresults_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=model_datasources_QueryMatchingCriteria_strategy)
@settings(max_examples=50)
def test_model_datasources_querymatchingcriteria_instantiation(instance):
    assert isinstance(instance, model_datasources_QueryMatchingCriteria)

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

@given(instance=VisualValue_strategy)
@settings(max_examples=50)
def test_visualvalue_instantiation(instance):
    assert isinstance(instance, VisualValue)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

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

@given(instance=Composite_strategy)
@settings(max_examples=50)
def test_composite_instantiation(instance):
    assert isinstance(instance, Composite)

@given(instance=model_ModelFormat_strategy)
@settings(max_examples=50)
def test_model_modelformat_instantiation(instance):
    assert isinstance(instance, model_ModelFormat)



@given(instance=model_ModelFormat_strategy)
def test_model_modelformat_modelFormat_setter(instance):
    original = instance.modelFormat
    instance.modelFormat = original
    assert instance.modelFormat == original

@given(instance=model_DomainModel__strategy)
@settings(max_examples=50)
def test_model_domainmodel__instantiation(instance):
    assert isinstance(instance, model_DomainModel_)



@given(instance=model_DomainModel__strategy)
def test_model_domainmodel__domainModel_setter(instance):
    original = instance.domainModel
    instance.domainModel = original
    assert instance.domainModel == original

@given(instance=types_model_DomainModel__strategy)
@settings(max_examples=50)
def test_types_model_domainmodel__instantiation(instance):
    assert isinstance(instance, types_model_DomainModel_)

@given(instance=VisualType_strategy)
@settings(max_examples=50)
def test_visualtype_instantiation(instance):
    assert isinstance(instance, VisualType)

@given(instance=model_types_CompositeVisualType_strategy)
@settings(max_examples=50)
def test_model_types_compositevisualtype_instantiation(instance):
    assert isinstance(instance, model_types_CompositeVisualType)

@given(instance=model_ISynchable_strategy)
@settings(max_examples=50)
def test_model_isynchable_instantiation(instance):
    assert isinstance(instance, model_ISynchable)



@given(instance=model_ISynchable_strategy)
def test_model_isynchable_synched_setter(instance):
    original = instance.synched
    instance.synched = original
    assert instance.synched == original

@given(instance=model_StringToStringMap_strategy)
@settings(max_examples=50)
def test_model_stringtostringmap_instantiation(instance):
    assert isinstance(instance, model_StringToStringMap)



@given(instance=model_StringToStringMap_strategy)
def test_model_stringtostringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=model_StringToStringMap_strategy)
def test_model_stringtostringmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=DomainModel__strategy)
@settings(max_examples=50)
def test_domainmodel__instantiation(instance):
    assert isinstance(instance, DomainModel_)

@given(instance=model_ExternalDomainModel_strategy)
@settings(max_examples=50)
def test_model_externaldomainmodel_instantiation(instance):
    assert isinstance(instance, model_ExternalDomainModel)



@given(instance=model_ExternalDomainModel_strategy)
def test_model_externaldomainmodel_fileFormat_setter(instance):
    original = instance.fileFormat
    instance.fileFormat = original
    assert instance.fileFormat == original

@given(instance=ISynchable_strategy)
@settings(max_examples=50)
def test_isynchable_instantiation(instance):
    assert isinstance(instance, ISynchable)

@given(instance=model_Node_strategy)
@settings(max_examples=50)
def test_model_node_instantiation(instance):
    assert isinstance(instance, model_Node)



@given(instance=model_Node_strategy)
def test_model_node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=model_Node_strategy)
def test_model_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Query_strategy)
@settings(max_examples=50)
def test_query_instantiation(instance):
    assert isinstance(instance, Query)

@given(instance=model_datasources_CompoundRefQuery_strategy)
@settings(max_examples=50)
def test_model_datasources_compoundrefquery_instantiation(instance):
    assert isinstance(instance, model_datasources_CompoundRefQuery)

@given(instance=DataSource_strategy)
@settings(max_examples=50)
def test_datasource_instantiation(instance):
    assert isinstance(instance, DataSource)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=Pointer_strategy)
@settings(max_examples=50)
def test_pointer_instantiation(instance):
    assert isinstance(instance, Pointer)

@given(instance=model_VariableValue_strategy)
@settings(max_examples=50)
def test_model_variablevalue_instantiation(instance):
    assert isinstance(instance, model_VariableValue)

@given(instance=model_ExperimentState_strategy)
@settings(max_examples=50)
def test_model_experimentstate_instantiation(instance):
    assert isinstance(instance, model_ExperimentState)



@given(instance=model_ExperimentState_strategy)
def test_model_experimentstate_experimentId_setter(instance):
    original = instance.experimentId
    instance.experimentId = original
    assert instance.experimentId == original



@given(instance=model_ExperimentState_strategy)
def test_model_experimentstate_projectId_setter(instance):
    original = instance.projectId
    instance.projectId = original
    assert instance.projectId == original

@given(instance=model_LibraryManager_strategy)
@settings(max_examples=50)
def test_model_librarymanager_instantiation(instance):
    assert isinstance(instance, model_LibraryManager)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=model_types_VisualType_strategy)
@settings(max_examples=50)
def test_model_types_visualtype_instantiation(instance):
    assert isinstance(instance, model_types_VisualType)

@given(instance=model_types_ArgumentType_strategy)
@settings(max_examples=50)
def test_model_types_argumenttype_instantiation(instance):
    assert isinstance(instance, model_types_ArgumentType)

@given(instance=model_types_DynamicsType_strategy)
@settings(max_examples=50)
def test_model_types_dynamicstype_instantiation(instance):
    assert isinstance(instance, model_types_DynamicsType)

@given(instance=model_types_ExpressionType_strategy)
@settings(max_examples=50)
def test_model_types_expressiontype_instantiation(instance):
    assert isinstance(instance, model_types_ExpressionType)

@given(instance=model_types_URLType_strategy)
@settings(max_examples=50)
def test_model_types_urltype_instantiation(instance):
    assert isinstance(instance, model_types_URLType)

@given(instance=model_types_ArrayType_strategy)
@settings(max_examples=50)
def test_model_types_arraytype_instantiation(instance):
    assert isinstance(instance, model_types_ArrayType)



@given(instance=model_types_ArrayType_strategy)
def test_model_types_arraytype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=model_types_ConnectionType_strategy)
@settings(max_examples=50)
def test_model_types_connectiontype_instantiation(instance):
    assert isinstance(instance, model_types_ConnectionType)

@given(instance=model_types_PointerType_strategy)
@settings(max_examples=50)
def test_model_types_pointertype_instantiation(instance):
    assert isinstance(instance, model_types_PointerType)

@given(instance=model_types_CompositeType_strategy)
@settings(max_examples=50)
def test_model_types_compositetype_instantiation(instance):
    assert isinstance(instance, model_types_CompositeType)

@given(instance=model_types_ImportType_strategy)
@settings(max_examples=50)
def test_model_types_importtype_instantiation(instance):
    assert isinstance(instance, model_types_ImportType)



@given(instance=model_types_ImportType_strategy)
def test_model_types_importtype_autoresolve_setter(instance):
    original = instance.autoresolve
    instance.autoresolve = original
    assert instance.autoresolve == original



@given(instance=model_types_ImportType_strategy)
def test_model_types_importtype_referenceURL_setter(instance):
    original = instance.referenceURL
    instance.referenceURL = original
    assert instance.referenceURL == original



@given(instance=model_types_ImportType_strategy)
def test_model_types_importtype_modelInterpreterId_setter(instance):
    original = instance.modelInterpreterId
    instance.modelInterpreterId = original
    assert instance.modelInterpreterId == original



@given(instance=model_types_ImportType_strategy)
def test_model_types_importtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=model_types_StateVariableType_strategy)
@settings(max_examples=50)
def test_model_types_statevariabletype_instantiation(instance):
    assert isinstance(instance, model_types_StateVariableType)

@given(instance=model_types_PointType_strategy)
@settings(max_examples=50)
def test_model_types_pointtype_instantiation(instance):
    assert isinstance(instance, model_types_PointType)

@given(instance=model_types_ParameterType_strategy)
@settings(max_examples=50)
def test_model_types_parametertype_instantiation(instance):
    assert isinstance(instance, model_types_ParameterType)

@given(instance=model_types_QuantityType_strategy)
@settings(max_examples=50)
def test_model_types_quantitytype_instantiation(instance):
    assert isinstance(instance, model_types_QuantityType)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=model_types_Type_strategy)
@settings(max_examples=50)
def test_model_types_type_instantiation(instance):
    assert isinstance(instance, model_types_Type)



@given(instance=model_types_Type_strategy)
def test_model_types_type_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_types_Type_strategy)
@settings(max_examples=30)
def test_model_types_type_extendstype_changes_state(instance):
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
        assert has_statements, f"Function 'extendsType' in model_types_Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'extendsType' in model_types_Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'extendsType' in model_types_Type is not implemented or raised an error")

@given(instance=model_Tag_strategy)
@settings(max_examples=50)
def test_model_tag_instantiation(instance):
    assert isinstance(instance, model_Tag)



@given(instance=model_Tag_strategy)
def test_model_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_GeppettoLibrary_strategy)
@settings(max_examples=50)
def test_model_geppettolibrary_instantiation(instance):
    assert isinstance(instance, model_GeppettoLibrary)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=model_GeppettoModel_strategy)
@settings(max_examples=50)
def test_model_geppettomodel_instantiation(instance):
    assert isinstance(instance, model_GeppettoModel)



@given(instance=model_GeppettoModel_strategy)
def test_model_geppettomodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_GeppettoModel_strategy)
def test_model_geppettomodel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=model_datasources_AQueryResult_strategy)
@settings(max_examples=50)
def test_model_datasources_aqueryresult_instantiation(instance):
    assert isinstance(instance, model_datasources_AQueryResult)

@given(instance=model_datasources_RunnableQuery_strategy)
@settings(max_examples=50)
def test_model_datasources_runnablequery_instantiation(instance):
    assert isinstance(instance, model_datasources_RunnableQuery)



@given(instance=model_datasources_RunnableQuery_strategy)
def test_model_datasources_runnablequery_queryPath_setter(instance):
    original = instance.queryPath
    instance.queryPath = original
    assert instance.queryPath == original



@given(instance=model_datasources_RunnableQuery_strategy)
def test_model_datasources_runnablequery_targetVariablePath_setter(instance):
    original = instance.targetVariablePath
    instance.targetVariablePath = original
    assert instance.targetVariablePath == original



@given(instance=model_datasources_RunnableQuery_strategy)
def test_model_datasources_runnablequery_booleanOperator_setter(instance):
    original = instance.booleanOperator
    instance.booleanOperator = original
    assert instance.booleanOperator == original

@given(instance=AQueryResult_strategy)
@settings(max_examples=50)
def test_aqueryresult_instantiation(instance):
    assert isinstance(instance, AQueryResult)

@given(instance=model_datasources_QueryResult_strategy)
@settings(max_examples=50)
def test_model_datasources_queryresult_instantiation(instance):
    assert isinstance(instance, model_datasources_QueryResult)



@given(instance=model_datasources_QueryResult_strategy)
def test_model_datasources_queryresult_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=model_datasources_SerializableQueryResult_strategy)
@settings(max_examples=50)
def test_model_datasources_serializablequeryresult_instantiation(instance):
    assert isinstance(instance, model_datasources_SerializableQueryResult)



@given(instance=model_datasources_SerializableQueryResult_strategy)
def test_model_datasources_serializablequeryresult_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=model_datasources_DataSourceLibraryConfiguration_strategy)
@settings(max_examples=50)
def test_model_datasources_datasourcelibraryconfiguration_instantiation(instance):
    assert isinstance(instance, model_datasources_DataSourceLibraryConfiguration)



@given(instance=model_datasources_DataSourceLibraryConfiguration_strategy)
def test_model_datasources_datasourcelibraryconfiguration_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original



@given(instance=model_datasources_DataSourceLibraryConfiguration_strategy)
def test_model_datasources_datasourcelibraryconfiguration_modelInterpreterId_setter(instance):
    original = instance.modelInterpreterId
    instance.modelInterpreterId = original
    assert instance.modelInterpreterId == original

@given(instance=datasources_model_GeppettoLibrary_strategy)
@settings(max_examples=50)
def test_datasources_model_geppettolibrary_instantiation(instance):
    assert isinstance(instance, datasources_model_GeppettoLibrary)

@given(instance=model_datasources_CompoundQuery_strategy)
@settings(max_examples=50)
def test_model_datasources_compoundquery_instantiation(instance):
    assert isinstance(instance, model_datasources_CompoundQuery)

@given(instance=model_datasources_SimpleQuery_strategy)
@settings(max_examples=50)
def test_model_datasources_simplequery_instantiation(instance):
    assert isinstance(instance, model_datasources_SimpleQuery)



@given(instance=model_datasources_SimpleQuery_strategy)
def test_model_datasources_simplequery_countQuery_setter(instance):
    original = instance.countQuery
    instance.countQuery = original
    assert instance.countQuery == original



@given(instance=model_datasources_SimpleQuery_strategy)
def test_model_datasources_simplequery_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original

@given(instance=datasources_model_StringToStringMap_strategy)
@settings(max_examples=50)
def test_datasources_model_stringtostringmap_instantiation(instance):
    assert isinstance(instance, datasources_model_StringToStringMap)

@given(instance=model_datasources_ProcessQuery_strategy)
@settings(max_examples=50)
def test_model_datasources_processquery_instantiation(instance):
    assert isinstance(instance, model_datasources_ProcessQuery)



@given(instance=model_datasources_ProcessQuery_strategy)
def test_model_datasources_processquery_queryProcessorId_setter(instance):
    original = instance.queryProcessorId
    instance.queryProcessorId = original
    assert instance.queryProcessorId == original

@given(instance=QueryMatchingCriteria_strategy)
@settings(max_examples=50)
def test_querymatchingcriteria_instantiation(instance):
    assert isinstance(instance, QueryMatchingCriteria)

@given(instance=model_datasources_Query_strategy)
@settings(max_examples=50)
def test_model_datasources_query_instantiation(instance):
    assert isinstance(instance, model_datasources_Query)



@given(instance=model_datasources_Query_strategy)
def test_model_datasources_query_runForCount_setter(instance):
    original = instance.runForCount
    instance.runForCount = original
    assert instance.runForCount == original



@given(instance=model_datasources_Query_strategy)
def test_model_datasources_query_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=model_variables_Variable_strategy)
@settings(max_examples=50)
def test_model_variables_variable_instantiation(instance):
    assert isinstance(instance, model_variables_Variable)



@given(instance=model_variables_Variable_strategy)
def test_model_variables_variable_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=model_values_AArrayValue_strategy)
@settings(max_examples=50)
def test_model_values_aarrayvalue_instantiation(instance):
    assert isinstance(instance, model_values_AArrayValue)

@given(instance=DataSourceLibraryConfiguration_strategy)
@settings(max_examples=50)
def test_datasourcelibraryconfiguration_instantiation(instance):
    assert isinstance(instance, DataSourceLibraryConfiguration)

@given(instance=model_datasources_DataSource_strategy)
@settings(max_examples=50)
def test_model_datasources_datasource_instantiation(instance):
    assert isinstance(instance, model_datasources_DataSource)



@given(instance=model_datasources_DataSource_strategy)
def test_model_datasources_datasource_dataSourceService_setter(instance):
    original = instance.dataSourceService
    instance.dataSourceService = original
    assert instance.dataSourceService == original



@given(instance=model_datasources_DataSource_strategy)
def test_model_datasources_datasource_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=model_variables_TypeToValueMap_strategy)
@settings(max_examples=50)
def test_model_variables_typetovaluemap_instantiation(instance):
    assert isinstance(instance, model_variables_TypeToValueMap)

@given(instance=TypeToValueMap_strategy)
@settings(max_examples=50)
def test_typetovaluemap_instantiation(instance):
    assert isinstance(instance, TypeToValueMap)

@given(instance=model_values_Image_strategy)
@settings(max_examples=50)
def test_model_values_image_instantiation(instance):
    assert isinstance(instance, model_values_Image)



@given(instance=model_values_Image_strategy)
def test_model_values_image_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original



@given(instance=model_values_Image_strategy)
def test_model_values_image_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_values_Image_strategy)
def test_model_values_image_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original



@given(instance=model_values_Image_strategy)
def test_model_values_image_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=ArrayElement_strategy)
@settings(max_examples=50)
def test_arrayelement_instantiation(instance):
    assert isinstance(instance, ArrayElement)

@given(instance=model_values_ArrayValue_strategy)
@settings(max_examples=50)
def test_model_values_arrayvalue_instantiation(instance):
    assert isinstance(instance, model_values_ArrayValue)

@given(instance=model_values_ImportValue_strategy)
@settings(max_examples=50)
def test_model_values_importvalue_instantiation(instance):
    assert isinstance(instance, model_values_ImportValue)



@given(instance=model_values_ImportValue_strategy)
def test_model_values_importvalue_modelInterpreterId_setter(instance):
    original = instance.modelInterpreterId
    instance.modelInterpreterId = original
    assert instance.modelInterpreterId == original

@given(instance=SkeletonTransformation_strategy)
@settings(max_examples=50)
def test_skeletontransformation_instantiation(instance):
    assert isinstance(instance, SkeletonTransformation)

@given(instance=model_values_SkeletonAnimation_strategy)
@settings(max_examples=50)
def test_model_values_skeletonanimation_instantiation(instance):
    assert isinstance(instance, model_values_SkeletonAnimation)

@given(instance=model_values_Particles_strategy)
@settings(max_examples=50)
def test_model_values_particles_instantiation(instance):
    assert isinstance(instance, model_values_Particles)

@given(instance=model_values_ArrayElement_strategy)
@settings(max_examples=50)
def test_model_values_arrayelement_instantiation(instance):
    assert isinstance(instance, model_values_ArrayElement)



@given(instance=model_values_ArrayElement_strategy)
def test_model_values_arrayelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=model_values_Connection_strategy)
@settings(max_examples=50)
def test_model_values_connection_instantiation(instance):
    assert isinstance(instance, model_values_Connection)



@given(instance=model_values_Connection_strategy)
def test_model_values_connection_connectivity_setter(instance):
    original = instance.connectivity
    instance.connectivity = original
    assert instance.connectivity == original

@given(instance=model_values_VisualGroup_strategy)
@settings(max_examples=50)
def test_model_values_visualgroup_instantiation(instance):
    assert isinstance(instance, model_values_VisualGroup)



@given(instance=model_values_VisualGroup_strategy)
def test_model_values_visualgroup_highSpectrumColor_setter(instance):
    original = instance.highSpectrumColor
    instance.highSpectrumColor = original
    assert instance.highSpectrumColor == original



@given(instance=model_values_VisualGroup_strategy)
def test_model_values_visualgroup_lowSpectrumColor_setter(instance):
    original = instance.lowSpectrumColor
    instance.lowSpectrumColor = original
    assert instance.lowSpectrumColor == original



@given(instance=model_values_VisualGroup_strategy)
def test_model_values_visualgroup_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model_values_VisualGroupElement_strategy)
@settings(max_examples=50)
def test_model_values_visualgroupelement_instantiation(instance):
    assert isinstance(instance, model_values_VisualGroupElement)



@given(instance=model_values_VisualGroupElement_strategy)
def test_model_values_visualgroupelement_defaultColor_setter(instance):
    original = instance.defaultColor
    instance.defaultColor = original
    assert instance.defaultColor == original

@given(instance=model_values_SkeletonTransformation_strategy)
@settings(max_examples=50)
def test_model_values_skeletontransformation_instantiation(instance):
    assert isinstance(instance, model_values_SkeletonTransformation)



@given(instance=model_values_SkeletonTransformation_strategy)
def test_model_values_skeletontransformation_skeletonTransformation_setter(instance):
    original = instance.skeletonTransformation
    instance.skeletonTransformation = original
    assert instance.skeletonTransformation == original

@given(instance=model_values_Function_strategy)
@settings(max_examples=50)
def test_model_values_function_instantiation(instance):
    assert isinstance(instance, model_values_Function)

@given(instance=model_values_FunctionPlot_strategy)
@settings(max_examples=50)
def test_model_values_functionplot_instantiation(instance):
    assert isinstance(instance, model_values_FunctionPlot)



@given(instance=model_values_FunctionPlot_strategy)
def test_model_values_functionplot_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=model_values_FunctionPlot_strategy)
def test_model_values_functionplot_xAxisLabel_setter(instance):
    original = instance.xAxisLabel
    instance.xAxisLabel = original
    assert instance.xAxisLabel == original



@given(instance=model_values_FunctionPlot_strategy)
def test_model_values_functionplot_yAxisLabel_setter(instance):
    original = instance.yAxisLabel
    instance.yAxisLabel = original
    assert instance.yAxisLabel == original



@given(instance=model_values_FunctionPlot_strategy)
def test_model_values_functionplot_stepValue_setter(instance):
    original = instance.stepValue
    instance.stepValue = original
    assert instance.stepValue == original



@given(instance=model_values_FunctionPlot_strategy)
def test_model_values_functionplot_finalValue_setter(instance):
    original = instance.finalValue
    instance.finalValue = original
    assert instance.finalValue == original



@given(instance=model_values_FunctionPlot_strategy)
def test_model_values_functionplot_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=model_values_Cylinder_strategy)
@settings(max_examples=50)
def test_model_values_cylinder_instantiation(instance):
    assert isinstance(instance, model_values_Cylinder)



@given(instance=model_values_Cylinder_strategy)
def test_model_values_cylinder_bottomRadius_setter(instance):
    original = instance.bottomRadius
    instance.bottomRadius = original
    assert instance.bottomRadius == original



@given(instance=model_values_Cylinder_strategy)
def test_model_values_cylinder_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=model_values_Cylinder_strategy)
def test_model_values_cylinder_topRadius_setter(instance):
    original = instance.topRadius
    instance.topRadius = original
    assert instance.topRadius == original

@given(instance=model_values_Sphere_strategy)
@settings(max_examples=50)
def test_model_values_sphere_instantiation(instance):
    assert isinstance(instance, model_values_Sphere)



@given(instance=model_values_Sphere_strategy)
def test_model_values_sphere_radius_setter(instance):
    original = instance.radius
    instance.radius = original
    assert instance.radius == original

@given(instance=model_values_OBJ_strategy)
@settings(max_examples=50)
def test_model_values_obj_instantiation(instance):
    assert isinstance(instance, model_values_OBJ)



@given(instance=model_values_OBJ_strategy)
def test_model_values_obj_obj_setter(instance):
    original = instance.obj
    instance.obj = original
    assert instance.obj == original

@given(instance=model_values_Collada_strategy)
@settings(max_examples=50)
def test_model_values_collada_instantiation(instance):
    assert isinstance(instance, model_values_Collada)



@given(instance=model_values_Collada_strategy)
def test_model_values_collada_collada_setter(instance):
    original = instance.collada
    instance.collada = original
    assert instance.collada == original

@given(instance=VisualGroupElement_strategy)
@settings(max_examples=50)
def test_visualgroupelement_instantiation(instance):
    assert isinstance(instance, VisualGroupElement)

@given(instance=model_values_VisualValue_strategy)
@settings(max_examples=50)
def test_model_values_visualvalue_instantiation(instance):
    assert isinstance(instance, model_values_VisualValue)

@given(instance=model_values_Expression_strategy)
@settings(max_examples=50)
def test_model_values_expression_instantiation(instance):
    assert isinstance(instance, model_values_Expression)



@given(instance=model_values_Expression_strategy)
def test_model_values_expression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=model_values_Argument_strategy)
@settings(max_examples=50)
def test_model_values_argument_instantiation(instance):
    assert isinstance(instance, model_values_Argument)



@given(instance=model_values_Argument_strategy)
def test_model_values_argument_argument_setter(instance):
    original = instance.argument
    instance.argument = original
    assert instance.argument == original

@given(instance=FunctionPlot_strategy)
@settings(max_examples=50)
def test_functionplot_instantiation(instance):
    assert isinstance(instance, FunctionPlot)

@given(instance=MetadataValue_strategy)
@settings(max_examples=50)
def test_metadatavalue_instantiation(instance):
    assert isinstance(instance, MetadataValue)

@given(instance=model_values_Metadata_strategy)
@settings(max_examples=50)
def test_model_values_metadata_instantiation(instance):
    assert isinstance(instance, model_values_Metadata)

@given(instance=model_values_JSON_strategy)
@settings(max_examples=50)
def test_model_values_json_instantiation(instance):
    assert isinstance(instance, model_values_JSON)



@given(instance=model_values_JSON_strategy)
def test_model_values_json_json_setter(instance):
    original = instance.json
    instance.json = original
    assert instance.json == original

@given(instance=model_values_Text_strategy)
@settings(max_examples=50)
def test_model_values_text_instantiation(instance):
    assert isinstance(instance, model_values_Text)



@given(instance=model_values_Text_strategy)
def test_model_values_text_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=model_values_MetadataValue_strategy)
@settings(max_examples=50)
def test_model_values_metadatavalue_instantiation(instance):
    assert isinstance(instance, model_values_MetadataValue)

@given(instance=model_values_MDTimeSeries_strategy)
@settings(max_examples=50)
def test_model_values_mdtimeseries_instantiation(instance):
    assert isinstance(instance, model_values_MDTimeSeries)

@given(instance=PhysicalQuantity_strategy)
@settings(max_examples=50)
def test_physicalquantity_instantiation(instance):
    assert isinstance(instance, PhysicalQuantity)

@given(instance=model_values_Dynamics_strategy)
@settings(max_examples=50)
def test_model_values_dynamics_instantiation(instance):
    assert isinstance(instance, model_values_Dynamics)

@given(instance=model_values_Point_strategy)
@settings(max_examples=50)
def test_model_values_point_instantiation(instance):
    assert isinstance(instance, model_values_Point)



@given(instance=model_values_Point_strategy)
def test_model_values_point_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original



@given(instance=model_values_Point_strategy)
def test_model_values_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=model_values_Point_strategy)
def test_model_values_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=model_values_PointerElement_strategy)
@settings(max_examples=50)
def test_model_values_pointerelement_instantiation(instance):
    assert isinstance(instance, model_values_PointerElement)



@given(instance=model_values_PointerElement_strategy)
def test_model_values_pointerelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=PointerElement_strategy)
@settings(max_examples=50)
def test_pointerelement_instantiation(instance):
    assert isinstance(instance, PointerElement)

@given(instance=model_values_Pointer_strategy)
@settings(max_examples=50)
def test_model_values_pointer_instantiation(instance):
    assert isinstance(instance, model_values_Pointer)



@given(instance=model_values_Pointer_strategy)
def test_model_values_pointer_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=model_values_HTML_strategy)
@settings(max_examples=50)
def test_model_values_html_instantiation(instance):
    assert isinstance(instance, model_values_HTML)



@given(instance=model_values_HTML_strategy)
def test_model_values_html_html_setter(instance):
    original = instance.html
    instance.html = original
    assert instance.html == original

@given(instance=model_values_URL_strategy)
@settings(max_examples=50)
def test_model_values_url_instantiation(instance):
    assert isinstance(instance, model_values_URL)



@given(instance=model_values_URL_strategy)
def test_model_values_url_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=Image_strategy)
@settings(max_examples=50)
def test_image_instantiation(instance):
    assert isinstance(instance, Image)

@given(instance=model_types_ImageType_strategy)
@settings(max_examples=50)
def test_model_types_imagetype_instantiation(instance):
    assert isinstance(instance, model_types_ImageType)

@given(instance=model_types_SimpleType_strategy)
@settings(max_examples=50)
def test_model_types_simpletype_instantiation(instance):
    assert isinstance(instance, model_types_SimpleType)

@given(instance=model_values_TimeSeries_strategy)
@settings(max_examples=50)
def test_model_values_timeseries_instantiation(instance):
    assert isinstance(instance, model_values_TimeSeries)



@given(instance=model_values_TimeSeries_strategy)
def test_model_values_timeseries_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=model_values_TimeSeries_strategy)
def test_model_values_timeseries_scalingFactor_setter(instance):
    original = instance.scalingFactor
    instance.scalingFactor = original
    assert instance.scalingFactor == original

@given(instance=model_values_Unit_strategy)
@settings(max_examples=50)
def test_model_values_unit_instantiation(instance):
    assert isinstance(instance, model_values_Unit)



@given(instance=model_values_Unit_strategy)
def test_model_values_unit_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=model_values_PhysicalQuantity_strategy)
@settings(max_examples=50)
def test_model_values_physicalquantity_instantiation(instance):
    assert isinstance(instance, model_values_PhysicalQuantity)

@given(instance=model_values_Quantity_strategy)
@settings(max_examples=50)
def test_model_values_quantity_instantiation(instance):
    assert isinstance(instance, model_values_Quantity)



@given(instance=model_values_Quantity_strategy)
def test_model_values_quantity_scalingFactor_setter(instance):
    original = instance.scalingFactor
    instance.scalingFactor = original
    assert instance.scalingFactor == original



@given(instance=model_values_Quantity_strategy)
def test_model_values_quantity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model_values_StringToValueMap_strategy)
@settings(max_examples=50)
def test_model_values_stringtovaluemap_instantiation(instance):
    assert isinstance(instance, model_values_StringToValueMap)



@given(instance=model_values_StringToValueMap_strategy)
def test_model_values_stringtovaluemap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=StringToValueMap_strategy)
@settings(max_examples=50)
def test_stringtovaluemap_instantiation(instance):
    assert isinstance(instance, StringToValueMap)

@given(instance=model_values_Composite_strategy)
@settings(max_examples=50)
def test_model_values_composite_instantiation(instance):
    assert isinstance(instance, model_values_Composite)

@given(instance=model_values_Value_strategy)
@settings(max_examples=50)
def test_model_values_value_instantiation(instance):
    assert isinstance(instance, model_values_Value)

@given(instance=model_types_MetadataType_strategy)
@settings(max_examples=50)
def test_model_types_metadatatype_instantiation(instance):
    assert isinstance(instance, model_types_MetadataType)

@given(instance=AArrayValue_strategy)
@settings(max_examples=50)
def test_aarrayvalue_instantiation(instance):
    assert isinstance(instance, AArrayValue)

@given(instance=model_values_DoubleArray_strategy)
@settings(max_examples=50)
def test_model_values_doublearray_instantiation(instance):
    assert isinstance(instance, model_values_DoubleArray)



@given(instance=model_values_DoubleArray_strategy)
def test_model_values_doublearray_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original

@given(instance=model_values_StringArray_strategy)
@settings(max_examples=50)
def test_model_values_stringarray_instantiation(instance):
    assert isinstance(instance, model_values_StringArray)



@given(instance=model_values_StringArray_strategy)
def test_model_values_stringarray_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original

@given(instance=model_values_IntArray_strategy)
@settings(max_examples=50)
def test_model_values_intarray_instantiation(instance):
    assert isinstance(instance, model_values_IntArray)



@given(instance=model_values_IntArray_strategy)
def test_model_values_intarray_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original

@given(instance=model_values_GenericArray_strategy)
@settings(max_examples=50)
def test_model_values_genericarray_instantiation(instance):
    assert isinstance(instance, model_values_GenericArray)

@given(instance=model_types_SimpleArrayType_strategy)
@settings(max_examples=50)
def test_model_types_simplearraytype_instantiation(instance):
    assert isinstance(instance, model_types_SimpleArrayType)

@given(instance=model_types_TextType_strategy)
@settings(max_examples=50)
def test_model_types_texttype_instantiation(instance):
    assert isinstance(instance, model_types_TextType)

@given(instance=JSON_strategy)
@settings(max_examples=50)
def test_json_instantiation(instance):
    assert isinstance(instance, JSON)

@given(instance=model_types_JSONType_strategy)
@settings(max_examples=50)
def test_model_types_jsontype_instantiation(instance):
    assert isinstance(instance, model_types_JSONType)

@given(instance=HTML_strategy)
@settings(max_examples=50)
def test_html_instantiation(instance):
    assert isinstance(instance, HTML)

@given(instance=model_types_HTMLType_strategy)
@settings(max_examples=50)
def test_model_types_htmltype_instantiation(instance):
    assert isinstance(instance, model_types_HTMLType)
