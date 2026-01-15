####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
FileFormat: Enumeration = Enumeration(
    name="FileFormat",
    literals={
            EnumerationLiteral(name="ZIP"),
			EnumerationLiteral(name="HDF5")
    }
)

Connectivity: Enumeration = Enumeration(
    name="Connectivity",
    literals={
            EnumerationLiteral(name="DIRECTIONAL"),
			EnumerationLiteral(name="BIDIRECTIONAL"),
			EnumerationLiteral(name="NON_DIRECTIONAL")
    }
)

ImageFormat: Enumeration = Enumeration(
    name="ImageFormat",
    literals={
            EnumerationLiteral(name="PNG"),
			EnumerationLiteral(name="JPEG"),
			EnumerationLiteral(name="IIP"),
			EnumerationLiteral(name="DCM"),
			EnumerationLiteral(name="NIFTI"),
			EnumerationLiteral(name="TIFF"),
			EnumerationLiteral(name="DZI"),
			EnumerationLiteral(name="GOOGLE_MAP")
    }
)

BooleanOperator: Enumeration = Enumeration(
    name="BooleanOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="NAND"),
			EnumerationLiteral(name="OR")
    }
)

# Classes
model_GeppettoLibrary = Class(name="model::GeppettoLibrary")
model_Tag = Class(name="model::Tag")
DataSource = Class(name="DataSource")
Query = Class(name="Query")
model_Node = Class(name="model::Node", is_abstract=True)
ISynchable = Class(name="ISynchable")
Node = Class(name="Node")
model_GeppettoModel = Class(name="model::GeppettoModel")
Variable = Class(name="Variable")
Pointer = Class(name="Pointer")
Value = Class(name="Value")
model_DomainModel = Class(name="model::DomainModel")
model_ModelFormat = Class(name="model::ModelFormat")
model_ExternalDomainModel = Class(name="model::ExternalDomainModel")
DomainModel = Class(name="DomainModel")
model_StringToStringMap = Class(name="model::StringToStringMap")
model_ISynchable = Class(name="model::ISynchable", is_abstract=True)
model_types_Type = Class(name="model::types::Type", is_abstract=True)
Type = Class(name="Type")
model_LibraryManager = Class(name="model::LibraryManager")
model_ExperimentState = Class(name="model::ExperimentState")
model_VariableValue = Class(name="model::VariableValue")
model_types_VisualType = Class(name="model::types::VisualType")
VisualValue = Class(name="VisualValue")
model_types_ImportType = Class(name="model::types::ImportType")
model_types_CompositeType = Class(name="model::types::CompositeType")
Composite = Class(name="Composite")
model_types_PointerType = Class(name="model::types::PointerType")
model_types_QuantityType = Class(name="model::types::QuantityType")
Quantity = Class(name="Quantity")
model_types_ParameterType = Class(name="model::types::ParameterType")
model_types_StateVariableType = Class(name="model::types::StateVariableType")
VisualType = Class(name="VisualType")
types_model_DomainModel = Class(name="types::model::DomainModel")
model_types_JSONType = Class(name="model::types::JSONType")
JSON = Class(name="JSON")
model_types_TextType = Class(name="model::types::TextType")
Text = Class(name="Text")
model_types_URLType = Class(name="model::types::URLType")
URL = Class(name="URL")
model_types_PointType = Class(name="model::types::PointType")
Point = Class(name="Point")
model_types_ArrayType = Class(name="model::types::ArrayType")
ArrayValue = Class(name="ArrayValue")
model_types_CompositeVisualType = Class(name="model::types::CompositeVisualType")
VisualGroup = Class(name="VisualGroup")
model_types_DynamicsType = Class(name="model::types::DynamicsType")
Dynamics = Class(name="Dynamics")
model_types_ArgumentType = Class(name="model::types::ArgumentType")
Argument = Class(name="Argument")
model_types_ExpressionType = Class(name="model::types::ExpressionType")
Expression = Class(name="Expression")
model_types_HTMLType = Class(name="model::types::HTMLType")
HTML = Class(name="HTML")
model_types_MetadataType = Class(name="model::types::MetadataType")
model_values_Value = Class(name="model::values::Value", is_abstract=True)
model_values_Composite = Class(name="model::values::Composite")
StringToValueMap = Class(name="StringToValueMap")
model_values_StringToValueMap = Class(name="model::values::StringToValueMap")
model_values_Quantity = Class(name="model::values::Quantity")
model_values_PhysicalQuantity = Class(name="model::values::PhysicalQuantity")
Unit = Class(name="Unit")
model_values_Unit = Class(name="model::values::Unit")
model_values_TimeSeries = Class(name="model::values::TimeSeries")
model_values_MDTimeSeries = Class(name="model::values::MDTimeSeries")
model_types_ConnectionType = Class(name="model::types::ConnectionType")
model_types_SimpleType = Class(name="model::types::SimpleType")
model_types_ImageType = Class(name="model::types::ImageType")
Image = Class(name="Image")
model_types_SimpleArrayType = Class(name="model::types::SimpleArrayType")
AArrayValue = Class(name="AArrayValue")
model_values_PointerElement = Class(name="model::values::PointerElement")
model_values_Point = Class(name="model::values::Point")
model_values_Dynamics = Class(name="model::values::Dynamics")
PhysicalQuantity = Class(name="PhysicalQuantity")
Function = Class(name="Function")
model_values_FunctionPlot = Class(name="model::values::FunctionPlot")
model_values_MetadataValue = Class(name="model::values::MetadataValue", is_abstract=True)
model_values_Text = Class(name="model::values::Text")
MetadataValue = Class(name="MetadataValue")
model_values_URL = Class(name="model::values::URL")
model_values_HTML = Class(name="model::values::HTML")
model_values_Pointer = Class(name="model::values::Pointer")
PointerElement = Class(name="PointerElement")
model_values_VisualValue = Class(name="model::values::VisualValue", is_abstract=True)
VisualGroupElement = Class(name="VisualGroupElement")
model_values_Collada = Class(name="model::values::Collada")
model_values_OBJ = Class(name="model::values::OBJ")
model_values_Sphere = Class(name="model::values::Sphere")
model_values_Cylinder = Class(name="model::values::Cylinder")
model_values_Particles = Class(name="model::values::Particles")
model_values_SkeletonAnimation = Class(name="model::values::SkeletonAnimation")
model_values_Function = Class(name="model::values::Function")
FunctionPlot = Class(name="FunctionPlot")
model_values_Argument = Class(name="model::values::Argument")
model_values_Expression = Class(name="model::values::Expression")
model_values_ArrayElement = Class(name="model::values::ArrayElement")
model_values_ArrayValue = Class(name="model::values::ArrayValue")
ArrayElement = Class(name="ArrayElement")
model_values_Image = Class(name="model::values::Image")
SkeletonTransformation = Class(name="SkeletonTransformation")
model_values_SkeletonTransformation = Class(name="model::values::SkeletonTransformation")
model_values_VisualGroupElement = Class(name="model::values::VisualGroupElement")
model_values_VisualGroup = Class(name="model::values::VisualGroup")
model_values_Connection = Class(name="model::values::Connection")
model_values_StringArray = Class(name="model::values::StringArray")
model_values_IntArray = Class(name="model::values::IntArray")
model_values_DoubleArray = Class(name="model::values::DoubleArray")
model_values_AArrayValue = Class(name="model::values::AArrayValue", is_abstract=True)
model_variables_Variable = Class(name="model::variables::Variable")
TypeToValueMap = Class(name="TypeToValueMap")
model_variables_TypeToValueMap = Class(name="model::variables::TypeToValueMap")
model_values_ImportValue = Class(name="model::values::ImportValue")
model_values_Metadata = Class(name="model::values::Metadata")
model_values_JSON = Class(name="model::values::JSON")
model_values_GenericArray = Class(name="model::values::GenericArray")
datasources_model_GeppettoLibrary = Class(name="datasources::model::GeppettoLibrary")
model_datasources_DataSourceLibraryConfiguration = Class(name="model::datasources::DataSourceLibraryConfiguration")
model_datasources_Query = Class(name="model::datasources::Query", is_abstract=True)
QueryMatchingCriteria = Class(name="QueryMatchingCriteria")
model_datasources_ProcessQuery = Class(name="model::datasources::ProcessQuery")
datasources_model_StringToStringMap = Class(name="datasources::model::StringToStringMap")
model_datasources_DataSource = Class(name="model::datasources::DataSource")
DataSourceLibraryConfiguration = Class(name="DataSourceLibraryConfiguration")
model_datasources_QueryResults = Class(name="model::datasources::QueryResults")
AQueryResult = Class(name="AQueryResult")
model_datasources_RunnableQuery = Class(name="model::datasources::RunnableQuery")
model_datasources_AQueryResult = Class(name="model::datasources::AQueryResult", is_abstract=True)
model_datasources_QueryResult = Class(name="model::datasources::QueryResult")
model_datasources_SerializableQueryResult = Class(name="model::datasources::SerializableQueryResult")
model_datasources_QueryMatchingCriteria = Class(name="model::datasources::QueryMatchingCriteria")
model_datasources_SimpleQuery = Class(name="model::datasources::SimpleQuery")
model_datasources_CompoundQuery = Class(name="model::datasources::CompoundQuery")
model_datasources_CompoundRefQuery = Class(name="model::datasources::CompoundRefQuery")

# model_GeppettoLibrary class attributes and methods
model_GeppettoLibrary_m_getTypeById: Method = Method(name="getTypeById", parameters={}, type=StringType)
model_GeppettoLibrary.methods={model_GeppettoLibrary_m_getTypeById}

# model_Tag class attributes and methods
model_Tag_name: Property = Property(name="name", type=StringType)
model_Tag.attributes={model_Tag_name}

# DataSource class attributes and methods

# Query class attributes and methods

# model_Node class attributes and methods
model_Node_id: Property = Property(name="id", type=StringType)
model_Node_name: Property = Property(name="name", type=StringType)
model_Node_m_getPath: Method = Method(name="getPath", parameters={}, type=StringType)
model_Node.attributes={model_Node_id, model_Node_name}
model_Node.methods={model_Node_m_getPath}

# ISynchable class attributes and methods

# Node class attributes and methods

# model_GeppettoModel class attributes and methods
model_GeppettoModel_id: Property = Property(name="id", type=StringType)
model_GeppettoModel_name: Property = Property(name="name", type=StringType)
model_GeppettoModel.attributes={model_GeppettoModel_id, model_GeppettoModel_name}

# Variable class attributes and methods

# Pointer class attributes and methods

# Value class attributes and methods

# model_DomainModel class attributes and methods
model_DomainModel_domainModel: Property = Property(name="domainModel", type=StringType)
model_DomainModel.attributes={model_DomainModel_domainModel}

# model_ModelFormat class attributes and methods
model_ModelFormat_modelFormat: Property = Property(name="modelFormat", type=StringType)
model_ModelFormat.attributes={model_ModelFormat_modelFormat}

# model_ExternalDomainModel class attributes and methods
model_ExternalDomainModel_fileFormat: Property = Property(name="fileFormat", type=StringType)
model_ExternalDomainModel.attributes={model_ExternalDomainModel_fileFormat}

# DomainModel class attributes and methods

# model_StringToStringMap class attributes and methods
model_StringToStringMap_key: Property = Property(name="key", type=StringType)
model_StringToStringMap_value: Property = Property(name="value", type=StringType)
model_StringToStringMap.attributes={model_StringToStringMap_key, model_StringToStringMap_value}

# model_ISynchable class attributes and methods
model_ISynchable_synched: Property = Property(name="synched", type=StringType)
model_ISynchable.attributes={model_ISynchable_synched}

# model_types_Type class attributes and methods
model_types_Type_abstract: Property = Property(name="abstract", type=StringType)
model_types_Type_m_getDefaultValue: Method = Method(name="getDefaultValue", parameters={}, type=StringType)
model_types_Type_m_extendsType: Method = Method(name="extendsType", parameters={Parameter(name='type')}, type=StringType)
model_types_Type.attributes={model_types_Type_abstract}
model_types_Type.methods={model_types_Type_m_extendsType, model_types_Type_m_getDefaultValue}

# Type class attributes and methods

# model_LibraryManager class attributes and methods

# model_ExperimentState class attributes and methods
model_ExperimentState_experimentId: Property = Property(name="experimentId", type=StringType)
model_ExperimentState_projectId: Property = Property(name="projectId", type=StringType)
model_ExperimentState.attributes={model_ExperimentState_experimentId, model_ExperimentState_projectId}

# model_VariableValue class attributes and methods

# model_types_VisualType class attributes and methods

# VisualValue class attributes and methods

# model_types_ImportType class attributes and methods
model_types_ImportType_url: Property = Property(name="url", type=StringType)
model_types_ImportType_referenceURL: Property = Property(name="referenceURL", type=StringType)
model_types_ImportType_modelInterpreterId: Property = Property(name="modelInterpreterId", type=StringType)
model_types_ImportType_autoresolve: Property = Property(name="autoresolve", type=StringType)
model_types_ImportType.attributes={model_types_ImportType_url, model_types_ImportType_referenceURL, model_types_ImportType_autoresolve, model_types_ImportType_modelInterpreterId}

# model_types_CompositeType class attributes and methods

# Composite class attributes and methods

# model_types_PointerType class attributes and methods

# model_types_QuantityType class attributes and methods

# Quantity class attributes and methods

# model_types_ParameterType class attributes and methods

# model_types_StateVariableType class attributes and methods

# VisualType class attributes and methods

# types_model_DomainModel class attributes and methods

# model_types_JSONType class attributes and methods

# JSON class attributes and methods

# model_types_TextType class attributes and methods

# Text class attributes and methods

# model_types_URLType class attributes and methods

# URL class attributes and methods

# model_types_PointType class attributes and methods

# Point class attributes and methods

# model_types_ArrayType class attributes and methods
model_types_ArrayType_size: Property = Property(name="size", type=StringType)
model_types_ArrayType.attributes={model_types_ArrayType_size}

# ArrayValue class attributes and methods

# model_types_CompositeVisualType class attributes and methods

# VisualGroup class attributes and methods

# model_types_DynamicsType class attributes and methods

# Dynamics class attributes and methods

# model_types_ArgumentType class attributes and methods

# Argument class attributes and methods

# model_types_ExpressionType class attributes and methods

# Expression class attributes and methods

# model_types_HTMLType class attributes and methods

# HTML class attributes and methods

# model_types_MetadataType class attributes and methods

# model_values_Value class attributes and methods

# model_values_Composite class attributes and methods

# StringToValueMap class attributes and methods

# model_values_StringToValueMap class attributes and methods
model_values_StringToValueMap_key: Property = Property(name="key", type=StringType)
model_values_StringToValueMap.attributes={model_values_StringToValueMap_key}

# model_values_Quantity class attributes and methods
model_values_Quantity_scalingFactor: Property = Property(name="scalingFactor", type=StringType)
model_values_Quantity_value: Property = Property(name="value", type=StringType)
model_values_Quantity.attributes={model_values_Quantity_value, model_values_Quantity_scalingFactor}

# model_values_PhysicalQuantity class attributes and methods

# Unit class attributes and methods

# model_values_Unit class attributes and methods
model_values_Unit_unit: Property = Property(name="unit", type=StringType)
model_values_Unit.attributes={model_values_Unit_unit}

# model_values_TimeSeries class attributes and methods
model_values_TimeSeries_scalingFactor: Property = Property(name="scalingFactor", type=StringType)
model_values_TimeSeries_value: Property = Property(name="value", type=StringType)
model_values_TimeSeries.attributes={model_values_TimeSeries_value, model_values_TimeSeries_scalingFactor}

# model_values_MDTimeSeries class attributes and methods

# model_types_ConnectionType class attributes and methods

# model_types_SimpleType class attributes and methods

# model_types_ImageType class attributes and methods

# Image class attributes and methods

# model_types_SimpleArrayType class attributes and methods

# AArrayValue class attributes and methods

# model_values_PointerElement class attributes and methods
model_values_PointerElement_index: Property = Property(name="index", type=StringType)
model_values_PointerElement.attributes={model_values_PointerElement_index}

# model_values_Point class attributes and methods
model_values_Point_x: Property = Property(name="x", type=StringType)
model_values_Point_y: Property = Property(name="y", type=StringType)
model_values_Point_z: Property = Property(name="z", type=StringType)
model_values_Point.attributes={model_values_Point_z, model_values_Point_y, model_values_Point_x}

# model_values_Dynamics class attributes and methods

# PhysicalQuantity class attributes and methods

# Function class attributes and methods

# model_values_FunctionPlot class attributes and methods
model_values_FunctionPlot_title: Property = Property(name="title", type=StringType)
model_values_FunctionPlot_xAxisLabel: Property = Property(name="xAxisLabel", type=StringType)
model_values_FunctionPlot_yAxisLabel: Property = Property(name="yAxisLabel", type=StringType)
model_values_FunctionPlot_initialValue: Property = Property(name="initialValue", type=StringType)
model_values_FunctionPlot_finalValue: Property = Property(name="finalValue", type=StringType)
model_values_FunctionPlot_stepValue: Property = Property(name="stepValue", type=StringType)
model_values_FunctionPlot.attributes={model_values_FunctionPlot_xAxisLabel, model_values_FunctionPlot_stepValue, model_values_FunctionPlot_title, model_values_FunctionPlot_initialValue, model_values_FunctionPlot_yAxisLabel, model_values_FunctionPlot_finalValue}

# model_values_MetadataValue class attributes and methods

# model_values_Text class attributes and methods
model_values_Text_text: Property = Property(name="text", type=StringType)
model_values_Text.attributes={model_values_Text_text}

# MetadataValue class attributes and methods

# model_values_URL class attributes and methods
model_values_URL_url: Property = Property(name="url", type=StringType)
model_values_URL.attributes={model_values_URL_url}

# model_values_HTML class attributes and methods
model_values_HTML_html: Property = Property(name="html", type=StringType)
model_values_HTML.attributes={model_values_HTML_html}

# model_values_Pointer class attributes and methods
model_values_Pointer_path: Property = Property(name="path", type=StringType)
model_values_Pointer_m_getInstancePath: Method = Method(name="getInstancePath", parameters={}, type=StringType)
model_values_Pointer.attributes={model_values_Pointer_path}
model_values_Pointer.methods={model_values_Pointer_m_getInstancePath}

# PointerElement class attributes and methods

# model_values_VisualValue class attributes and methods

# VisualGroupElement class attributes and methods

# model_values_Collada class attributes and methods
model_values_Collada_collada: Property = Property(name="collada", type=StringType)
model_values_Collada.attributes={model_values_Collada_collada}

# model_values_OBJ class attributes and methods
model_values_OBJ_obj: Property = Property(name="obj", type=StringType)
model_values_OBJ.attributes={model_values_OBJ_obj}

# model_values_Sphere class attributes and methods
model_values_Sphere_radius: Property = Property(name="radius", type=StringType)
model_values_Sphere.attributes={model_values_Sphere_radius}

# model_values_Cylinder class attributes and methods
model_values_Cylinder_bottomRadius: Property = Property(name="bottomRadius", type=StringType)
model_values_Cylinder_topRadius: Property = Property(name="topRadius", type=StringType)
model_values_Cylinder_height: Property = Property(name="height", type=StringType)
model_values_Cylinder.attributes={model_values_Cylinder_bottomRadius, model_values_Cylinder_height, model_values_Cylinder_topRadius}

# model_values_Particles class attributes and methods

# model_values_SkeletonAnimation class attributes and methods

# model_values_Function class attributes and methods

# FunctionPlot class attributes and methods

# model_values_Argument class attributes and methods
model_values_Argument_argument: Property = Property(name="argument", type=StringType)
model_values_Argument.attributes={model_values_Argument_argument}

# model_values_Expression class attributes and methods
model_values_Expression_expression: Property = Property(name="expression", type=StringType)
model_values_Expression.attributes={model_values_Expression_expression}

# model_values_ArrayElement class attributes and methods
model_values_ArrayElement_index: Property = Property(name="index", type=StringType)
model_values_ArrayElement.attributes={model_values_ArrayElement_index}

# model_values_ArrayValue class attributes and methods

# ArrayElement class attributes and methods

# model_values_Image class attributes and methods
model_values_Image_data: Property = Property(name="data", type=StringType)
model_values_Image_name: Property = Property(name="name", type=StringType)
model_values_Image_reference: Property = Property(name="reference", type=StringType)
model_values_Image_format: Property = Property(name="format", type=StringType)
model_values_Image.attributes={model_values_Image_reference, model_values_Image_data, model_values_Image_name, model_values_Image_format}

# SkeletonTransformation class attributes and methods

# model_values_SkeletonTransformation class attributes and methods
model_values_SkeletonTransformation_skeletonTransformation: Property = Property(name="skeletonTransformation", type=StringType)
model_values_SkeletonTransformation.attributes={model_values_SkeletonTransformation_skeletonTransformation}

# model_values_VisualGroupElement class attributes and methods
model_values_VisualGroupElement_defaultColor: Property = Property(name="defaultColor", type=StringType)
model_values_VisualGroupElement.attributes={model_values_VisualGroupElement_defaultColor}

# model_values_VisualGroup class attributes and methods
model_values_VisualGroup_lowSpectrumColor: Property = Property(name="lowSpectrumColor", type=StringType)
model_values_VisualGroup_highSpectrumColor: Property = Property(name="highSpectrumColor", type=StringType)
model_values_VisualGroup_type: Property = Property(name="type", type=StringType)
model_values_VisualGroup.attributes={model_values_VisualGroup_highSpectrumColor, model_values_VisualGroup_type, model_values_VisualGroup_lowSpectrumColor}

# model_values_Connection class attributes and methods
model_values_Connection_connectivity: Property = Property(name="connectivity", type=StringType)
model_values_Connection.attributes={model_values_Connection_connectivity}

# model_values_StringArray class attributes and methods
model_values_StringArray_elements: Property = Property(name="elements", type=StringType)
model_values_StringArray.attributes={model_values_StringArray_elements}

# model_values_IntArray class attributes and methods
model_values_IntArray_elements: Property = Property(name="elements", type=StringType)
model_values_IntArray.attributes={model_values_IntArray_elements}

# model_values_DoubleArray class attributes and methods
model_values_DoubleArray_elements: Property = Property(name="elements", type=StringType)
model_values_DoubleArray.attributes={model_values_DoubleArray_elements}

# model_values_AArrayValue class attributes and methods

# model_variables_Variable class attributes and methods
model_variables_Variable_static: Property = Property(name="static", type=StringType)
model_variables_Variable.attributes={model_variables_Variable_static}

# TypeToValueMap class attributes and methods

# model_variables_TypeToValueMap class attributes and methods

# model_values_ImportValue class attributes and methods
model_values_ImportValue_modelInterpreterId: Property = Property(name="modelInterpreterId", type=StringType)
model_values_ImportValue.attributes={model_values_ImportValue_modelInterpreterId}

# model_values_Metadata class attributes and methods

# model_values_JSON class attributes and methods
model_values_JSON_json: Property = Property(name="json", type=StringType)
model_values_JSON.attributes={model_values_JSON_json}

# model_values_GenericArray class attributes and methods

# datasources_model_GeppettoLibrary class attributes and methods

# model_datasources_DataSourceLibraryConfiguration class attributes and methods
model_datasources_DataSourceLibraryConfiguration_modelInterpreterId: Property = Property(name="modelInterpreterId", type=StringType)
model_datasources_DataSourceLibraryConfiguration_format: Property = Property(name="format", type=StringType)
model_datasources_DataSourceLibraryConfiguration.attributes={model_datasources_DataSourceLibraryConfiguration_format, model_datasources_DataSourceLibraryConfiguration_modelInterpreterId}

# model_datasources_Query class attributes and methods
model_datasources_Query_description: Property = Property(name="description", type=StringType)
model_datasources_Query_runForCount: Property = Property(name="runForCount", type=StringType)
model_datasources_Query.attributes={model_datasources_Query_runForCount, model_datasources_Query_description}

# QueryMatchingCriteria class attributes and methods

# model_datasources_ProcessQuery class attributes and methods
model_datasources_ProcessQuery_queryProcessorId: Property = Property(name="queryProcessorId", type=StringType)
model_datasources_ProcessQuery.attributes={model_datasources_ProcessQuery_queryProcessorId}

# datasources_model_StringToStringMap class attributes and methods

# model_datasources_DataSource class attributes and methods
model_datasources_DataSource_url: Property = Property(name="url", type=StringType)
model_datasources_DataSource_dataSourceService: Property = Property(name="dataSourceService", type=StringType)
model_datasources_DataSource.attributes={model_datasources_DataSource_url, model_datasources_DataSource_dataSourceService}

# DataSourceLibraryConfiguration class attributes and methods

# model_datasources_QueryResults class attributes and methods
model_datasources_QueryResults_id: Property = Property(name="id", type=StringType)
model_datasources_QueryResults_header: Property = Property(name="header", type=StringType)
model_datasources_QueryResults_m_getValue: Method = Method(name="getValue", parameters={Parameter(name='field'), Parameter(name='row')}, type=StringType)
model_datasources_QueryResults.attributes={model_datasources_QueryResults_header, model_datasources_QueryResults_id}
model_datasources_QueryResults.methods={model_datasources_QueryResults_m_getValue}

# AQueryResult class attributes and methods

# model_datasources_RunnableQuery class attributes and methods
model_datasources_RunnableQuery_targetVariablePath: Property = Property(name="targetVariablePath", type=StringType)
model_datasources_RunnableQuery_queryPath: Property = Property(name="queryPath", type=StringType)
model_datasources_RunnableQuery_booleanOperator: Property = Property(name="booleanOperator", type=StringType)
model_datasources_RunnableQuery.attributes={model_datasources_RunnableQuery_booleanOperator, model_datasources_RunnableQuery_targetVariablePath, model_datasources_RunnableQuery_queryPath}

# model_datasources_AQueryResult class attributes and methods

# model_datasources_QueryResult class attributes and methods
model_datasources_QueryResult_values: Property = Property(name="values", type=StringType)
model_datasources_QueryResult.attributes={model_datasources_QueryResult_values}

# model_datasources_SerializableQueryResult class attributes and methods
model_datasources_SerializableQueryResult_values: Property = Property(name="values", type=StringType)
model_datasources_SerializableQueryResult.attributes={model_datasources_SerializableQueryResult_values}

# model_datasources_QueryMatchingCriteria class attributes and methods

# model_datasources_SimpleQuery class attributes and methods
model_datasources_SimpleQuery_query: Property = Property(name="query", type=StringType)
model_datasources_SimpleQuery_countQuery: Property = Property(name="countQuery", type=StringType)
model_datasources_SimpleQuery.attributes={model_datasources_SimpleQuery_query, model_datasources_SimpleQuery_countQuery}

# model_datasources_CompoundQuery class attributes and methods

# model_datasources_CompoundRefQuery class attributes and methods

# Relationships
libraries1: BinaryAssociation = BinaryAssociation(
    name="libraries1",
    ends={
        Property(name="model_GeppettoLibrary", type=model_GeppettoModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_GeppettoModel2", type=model_GeppettoLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tags3: BinaryAssociation = BinaryAssociation(
    name="tags3",
    ends={
        Property(name="model_Tag", type=model_GeppettoModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_GeppettoModel4", type=model_Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataSources5: BinaryAssociation = BinaryAssociation(
    name="dataSources5",
    ends={
        Property(name="DataSource", type=model_GeppettoModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_GeppettoModel6", type=DataSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
queries7: BinaryAssociation = BinaryAssociation(
    name="queries7",
    ends={
        Property(name="Query", type=model_GeppettoModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_GeppettoModel8", type=Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tags9: BinaryAssociation = BinaryAssociation(
    name="tags9",
    ends={
        Property(name="model_Tag10", type=model_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Node", type=model_Tag, multiplicity=Multiplicity(0, 9999))
    }
)
variables0: BinaryAssociation = BinaryAssociation(
    name="variables0",
    ends={
        Property(name="Variable", type=model_GeppettoModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_GeppettoModel", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pointer22: BinaryAssociation = BinaryAssociation(
    name="pointer22",
    ends={
        Property(name="Pointer", type=model_VariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_VariableValue23", type=Pointer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value24: BinaryAssociation = BinaryAssociation(
    name="value24",
    ends={
        Property(name="Value", type=model_VariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_VariableValue25", type=Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tags27: BinaryAssociation = BinaryAssociation(
    name="tags27",
    ends={
        Property(name="model_Tag28", type=model_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Tag26", type=model_Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
format29: BinaryAssociation = BinaryAssociation(
    name="format29",
    ends={
        Property(name="model_ModelFormat", type=model_DomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DomainModel", type=model_ModelFormat, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types11: BinaryAssociation = BinaryAssociation(
    name="types11",
    ends={
        Property(name="Type", type=model_GeppettoLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="model_GeppettoLibrary12", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sharedTypes13: BinaryAssociation = BinaryAssociation(
    name="sharedTypes13",
    ends={
        Property(name="Type15", type=model_GeppettoLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="model_GeppettoLibrary14", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
libraries16: BinaryAssociation = BinaryAssociation(
    name="libraries16",
    ends={
        Property(name="model_GeppettoLibrary17", type=model_LibraryManager, multiplicity=Multiplicity(1, 1)),
        Property(name="model_LibraryManager", type=model_GeppettoLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
recordedVariables18: BinaryAssociation = BinaryAssociation(
    name="recordedVariables18",
    ends={
        Property(name="model_VariableValue", type=model_ExperimentState, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ExperimentState", type=model_VariableValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
setParameters19: BinaryAssociation = BinaryAssociation(
    name="setParameters19",
    ends={
        Property(name="model_VariableValue21", type=model_ExperimentState, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ExperimentState20", type=model_VariableValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultValue38: BinaryAssociation = BinaryAssociation(
    name="defaultValue38",
    ends={
        Property(name="VisualValue", type=model_types_VisualType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_VisualType", type=VisualValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables39: BinaryAssociation = BinaryAssociation(
    name="variables39",
    ends={
        Property(name="Variable40", type=model_types_CompositeType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_CompositeType", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultValue41: BinaryAssociation = BinaryAssociation(
    name="defaultValue41",
    ends={
        Property(name="Composite", type=model_types_CompositeType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_CompositeType42", type=Composite, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue43: BinaryAssociation = BinaryAssociation(
    name="defaultValue43",
    ends={
        Property(name="Pointer44", type=model_types_PointerType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_PointerType", type=Pointer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue45: BinaryAssociation = BinaryAssociation(
    name="defaultValue45",
    ends={
        Property(name="Quantity", type=model_types_QuantityType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_QuantityType", type=Quantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue46: BinaryAssociation = BinaryAssociation(
    name="defaultValue46",
    ends={
        Property(name="Quantity47", type=model_types_ParameterType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_ParameterType", type=Quantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue48: BinaryAssociation = BinaryAssociation(
    name="defaultValue48",
    ends={
        Property(name="Quantity49", type=model_types_StateVariableType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_StateVariableType", type=Quantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superType30: BinaryAssociation = BinaryAssociation(
    name="superType30",
    ends={
        Property(name="Type31", type=model_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_Type", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
visualType32: BinaryAssociation = BinaryAssociation(
    name="visualType32",
    ends={
        Property(name="VisualType", type=model_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_Type33", type=VisualType, multiplicity=Multiplicity(0, 1))
    }
)
referencedVariables34: BinaryAssociation = BinaryAssociation(
    name="referencedVariables34",
    ends={
        Property(name="variables", type=model_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable35", type=Variable, multiplicity=Multiplicity(0, 9999))
    }
)
domainModel36: BinaryAssociation = BinaryAssociation(
    name="domainModel36",
    ends={
        Property(name="types_model_DomainModel", type=model_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_Type37", type=types_model_DomainModel, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue54: BinaryAssociation = BinaryAssociation(
    name="defaultValue54",
    ends={
        Property(name="JSON", type=model_types_JSONType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JSONType", type=JSON, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue55: BinaryAssociation = BinaryAssociation(
    name="defaultValue55",
    ends={
        Property(name="Text", type=model_types_TextType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_TextType", type=Text, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue56: BinaryAssociation = BinaryAssociation(
    name="defaultValue56",
    ends={
        Property(name="URL", type=model_types_URLType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_URLType", type=URL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue57: BinaryAssociation = BinaryAssociation(
    name="defaultValue57",
    ends={
        Property(name="Point", type=model_types_PointType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_PointType", type=Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayType58: BinaryAssociation = BinaryAssociation(
    name="arrayType58",
    ends={
        Property(name="Type59", type=model_types_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_ArrayType", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
defaultValue60: BinaryAssociation = BinaryAssociation(
    name="defaultValue60",
    ends={
        Property(name="ArrayValue", type=model_types_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_ArrayType61", type=ArrayValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables62: BinaryAssociation = BinaryAssociation(
    name="variables62",
    ends={
        Property(name="Variable63", type=model_types_CompositeVisualType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_CompositeVisualType", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
visualGroups64: BinaryAssociation = BinaryAssociation(
    name="visualGroups64",
    ends={
        Property(name="VisualGroup", type=model_types_CompositeVisualType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_CompositeVisualType65", type=VisualGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultValue50: BinaryAssociation = BinaryAssociation(
    name="defaultValue50",
    ends={
        Property(name="Dynamics", type=model_types_DynamicsType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_DynamicsType", type=Dynamics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue51: BinaryAssociation = BinaryAssociation(
    name="defaultValue51",
    ends={
        Property(name="Argument", type=model_types_ArgumentType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_ArgumentType", type=Argument, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue52: BinaryAssociation = BinaryAssociation(
    name="defaultValue52",
    ends={
        Property(name="Expression", type=model_types_ExpressionType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_ExpressionType", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue53: BinaryAssociation = BinaryAssociation(
    name="defaultValue53",
    ends={
        Property(name="HTML", type=model_types_HTMLType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_HTMLType", type=HTML, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value73: BinaryAssociation = BinaryAssociation(
    name="value73",
    ends={
        Property(name="StringToValueMap", type=model_values_Composite, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_Composite", type=StringToValueMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value74: BinaryAssociation = BinaryAssociation(
    name="value74",
    ends={
        Property(name="Value75", type=model_values_StringToValueMap, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_StringToValueMap", type=Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unit76: BinaryAssociation = BinaryAssociation(
    name="unit76",
    ends={
        Property(name="Unit", type=model_values_PhysicalQuantity, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_PhysicalQuantity", type=Unit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unit77: BinaryAssociation = BinaryAssociation(
    name="unit77",
    ends={
        Property(name="Unit78", type=model_values_TimeSeries, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_TimeSeries", type=Unit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables66: BinaryAssociation = BinaryAssociation(
    name="variables66",
    ends={
        Property(name="Variable67", type=model_types_ConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_ConnectionType", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultValue68: BinaryAssociation = BinaryAssociation(
    name="defaultValue68",
    ends={
        Property(name="Composite70", type=model_types_ConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_ConnectionType69", type=Composite, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue71: BinaryAssociation = BinaryAssociation(
    name="defaultValue71",
    ends={
        Property(name="Image", type=model_types_ImageType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_ImageType", type=Image, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue72: BinaryAssociation = BinaryAssociation(
    name="defaultValue72",
    ends={
        Property(name="AArrayValue", type=model_types_SimpleArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_SimpleArrayType", type=AArrayValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
point82: BinaryAssociation = BinaryAssociation(
    name="point82",
    ends={
        Property(name="Point84", type=model_values_Pointer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_Pointer83", type=Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable85: BinaryAssociation = BinaryAssociation(
    name="variable85",
    ends={
        Property(name="Variable86", type=model_values_PointerElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_PointerElement", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
type87: BinaryAssociation = BinaryAssociation(
    name="type87",
    ends={
        Property(name="Type89", type=model_values_PointerElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_PointerElement88", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
initialCondition90: BinaryAssociation = BinaryAssociation(
    name="initialCondition90",
    ends={
        Property(name="PhysicalQuantity", type=model_values_Dynamics, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_Dynamics", type=PhysicalQuantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dynamics91: BinaryAssociation = BinaryAssociation(
    name="dynamics91",
    ends={
        Property(name="Function", type=model_values_Dynamics, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_Dynamics92", type=Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value79: BinaryAssociation = BinaryAssociation(
    name="value79",
    ends={
        Property(name="Value80", type=model_values_MDTimeSeries, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_MDTimeSeries", type=Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements81: BinaryAssociation = BinaryAssociation(
    name="elements81",
    ends={
        Property(name="PointerElement", type=model_values_Pointer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_Pointer", type=PointerElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupElements100: BinaryAssociation = BinaryAssociation(
    name="groupElements100",
    ends={
        Property(name="VisualGroupElement", type=model_values_VisualValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_VisualValue", type=VisualGroupElement, multiplicity=Multiplicity(0, 9999))
    }
)
position101: BinaryAssociation = BinaryAssociation(
    name="position101",
    ends={
        Property(name="Point103", type=model_values_VisualValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_VisualValue102", type=Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
distal104: BinaryAssociation = BinaryAssociation(
    name="distal104",
    ends={
        Property(name="Point105", type=model_values_Cylinder, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_Cylinder", type=Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
particles106: BinaryAssociation = BinaryAssociation(
    name="particles106",
    ends={
        Property(name="Point107", type=model_values_Particles, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_Particles", type=Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments93: BinaryAssociation = BinaryAssociation(
    name="arguments93",
    ends={
        Property(name="Argument94", type=model_values_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_Function", type=Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression95: BinaryAssociation = BinaryAssociation(
    name="expression95",
    ends={
        Property(name="Expression97", type=model_values_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_Function96", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
functionPlot98: BinaryAssociation = BinaryAssociation(
    name="functionPlot98",
    ends={
        Property(name="FunctionPlot", type=model_values_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_Function99", type=FunctionPlot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
a113: BinaryAssociation = BinaryAssociation(
    name="a113",
    ends={
        Property(name="Pointer114", type=model_values_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_Connection", type=Pointer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
b115: BinaryAssociation = BinaryAssociation(
    name="b115",
    ends={
        Property(name="Pointer117", type=model_values_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_Connection116", type=Pointer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
position118: BinaryAssociation = BinaryAssociation(
    name="position118",
    ends={
        Property(name="Point119", type=model_values_ArrayElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_ArrayElement", type=Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue120: BinaryAssociation = BinaryAssociation(
    name="initialValue120",
    ends={
        Property(name="Value122", type=model_values_ArrayElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_ArrayElement121", type=Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements123: BinaryAssociation = BinaryAssociation(
    name="elements123",
    ends={
        Property(name="ArrayElement", type=model_values_ArrayValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_ArrayValue", type=ArrayElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
skeletonTransformationSeries108: BinaryAssociation = BinaryAssociation(
    name="skeletonTransformationSeries108",
    ends={
        Property(name="SkeletonTransformation", type=model_values_SkeletonAnimation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_SkeletonAnimation", type=SkeletonTransformation, multiplicity=Multiplicity(0, 9999))
    }
)
parameter109: BinaryAssociation = BinaryAssociation(
    name="parameter109",
    ends={
        Property(name="Quantity110", type=model_values_VisualGroupElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_VisualGroupElement", type=Quantity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
visualGroupElements111: BinaryAssociation = BinaryAssociation(
    name="visualGroupElements111",
    ends={
        Property(name="VisualGroupElement112", type=model_values_VisualGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_VisualGroup", type=VisualGroupElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements126: BinaryAssociation = BinaryAssociation(
    name="elements126",
    ends={
        Property(name="Value127", type=model_values_GenericArray, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_GenericArray", type=Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousTypes128: BinaryAssociation = BinaryAssociation(
    name="anonymousTypes128",
    ends={
        Property(name="Type129", type=model_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_variables_Variable", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types130: BinaryAssociation = BinaryAssociation(
    name="types130",
    ends={
        Property(name="types", type=model_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="Type131", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
initialValues132: BinaryAssociation = BinaryAssociation(
    name="initialValues132",
    ends={
        Property(name="TypeToValueMap", type=model_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_variables_Variable133", type=TypeToValueMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position134: BinaryAssociation = BinaryAssociation(
    name="position134",
    ends={
        Property(name="Point136", type=model_variables_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_variables_Variable135", type=Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key137: BinaryAssociation = BinaryAssociation(
    name="key137",
    ends={
        Property(name="Type138", type=model_variables_TypeToValueMap, multiplicity=Multiplicity(1, 1)),
        Property(name="model_variables_TypeToValueMap", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
value124: BinaryAssociation = BinaryAssociation(
    name="value124",
    ends={
        Property(name="StringToValueMap125", type=model_values_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="model_values_Metadata", type=StringToValueMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
queries143: BinaryAssociation = BinaryAssociation(
    name="queries143",
    ends={
        Property(name="Query145", type=model_datasources_DataSource, multiplicity=Multiplicity(1, 1)),
        Property(name="model_datasources_DataSource144", type=Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependenciesLibrary146: BinaryAssociation = BinaryAssociation(
    name="dependenciesLibrary146",
    ends={
        Property(name="datasources_model_GeppettoLibrary", type=model_datasources_DataSource, multiplicity=Multiplicity(1, 1)),
        Property(name="model_datasources_DataSource147", type=datasources_model_GeppettoLibrary, multiplicity=Multiplicity(0, 9999))
    }
)
targetLibrary148: BinaryAssociation = BinaryAssociation(
    name="targetLibrary148",
    ends={
        Property(name="datasources_model_GeppettoLibrary150", type=model_datasources_DataSource, multiplicity=Multiplicity(1, 1)),
        Property(name="model_datasources_DataSource149", type=datasources_model_GeppettoLibrary, multiplicity=Multiplicity(1, 1))
    }
)
fetchVariableQuery151: BinaryAssociation = BinaryAssociation(
    name="fetchVariableQuery151",
    ends={
        Property(name="Query153", type=model_datasources_DataSource, multiplicity=Multiplicity(1, 1)),
        Property(name="model_datasources_DataSource152", type=Query, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
library154: BinaryAssociation = BinaryAssociation(
    name="library154",
    ends={
        Property(name="datasources_model_GeppettoLibrary155", type=model_datasources_DataSourceLibraryConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_datasources_DataSourceLibraryConfiguration", type=datasources_model_GeppettoLibrary, multiplicity=Multiplicity(1, 1))
    }
)
matchingCriteria156: BinaryAssociation = BinaryAssociation(
    name="matchingCriteria156",
    ends={
        Property(name="QueryMatchingCriteria", type=model_datasources_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="model_datasources_Query", type=QueryMatchingCriteria, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType157: BinaryAssociation = BinaryAssociation(
    name="returnType157",
    ends={
        Property(name="Type159", type=model_datasources_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="model_datasources_Query158", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
parameters160: BinaryAssociation = BinaryAssociation(
    name="parameters160",
    ends={
        Property(name="datasources_model_StringToStringMap", type=model_datasources_ProcessQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="model_datasources_ProcessQuery", type=datasources_model_StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value139: BinaryAssociation = BinaryAssociation(
    name="value139",
    ends={
        Property(name="Value141", type=model_variables_TypeToValueMap, multiplicity=Multiplicity(1, 1)),
        Property(name="model_variables_TypeToValueMap140", type=Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
libraryConfigurations142: BinaryAssociation = BinaryAssociation(
    name="libraryConfigurations142",
    ends={
        Property(name="DataSourceLibraryConfiguration", type=model_datasources_DataSource, multiplicity=Multiplicity(1, 1)),
        Property(name="model_datasources_DataSource", type=DataSourceLibraryConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
queryChain163: BinaryAssociation = BinaryAssociation(
    name="queryChain163",
    ends={
        Property(name="Query164", type=model_datasources_CompoundRefQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="model_datasources_CompoundRefQuery", type=Query, multiplicity=Multiplicity(1, 9999))
    }
)
results165: BinaryAssociation = BinaryAssociation(
    name="results165",
    ends={
        Property(name="AQueryResult", type=model_datasources_QueryResults, multiplicity=Multiplicity(1, 1)),
        Property(name="model_datasources_QueryResults", type=AQueryResult, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type166: BinaryAssociation = BinaryAssociation(
    name="type166",
    ends={
        Property(name="Type167", type=model_datasources_QueryMatchingCriteria, multiplicity=Multiplicity(1, 1)),
        Property(name="model_datasources_QueryMatchingCriteria", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
queryChain161: BinaryAssociation = BinaryAssociation(
    name="queryChain161",
    ends={
        Property(name="Query162", type=model_datasources_CompoundQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="model_datasources_CompoundQuery", type=Query, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_model_Node_ISynchable = Generalization(general=ISynchable, specific=model_Node)
gen_model_GeppettoLibrary_Node = Generalization(general=Node, specific=model_GeppettoLibrary)
gen_model_Tag_ISynchable = Generalization(general=ISynchable, specific=model_Tag)
gen_model_ExternalDomainModel_DomainModel = Generalization(general=DomainModel, specific=model_ExternalDomainModel)
gen_model_types_Type_Node = Generalization(general=Node, specific=model_types_Type)
gen_model_types_VisualType_Type = Generalization(general=Type, specific=model_types_VisualType)
gen_model_types_ImportType_Type = Generalization(general=Type, specific=model_types_ImportType)
gen_model_types_CompositeType_Type = Generalization(general=Type, specific=model_types_CompositeType)
gen_model_types_PointerType_Type = Generalization(general=Type, specific=model_types_PointerType)
gen_model_types_QuantityType_Type = Generalization(general=Type, specific=model_types_QuantityType)
gen_model_types_ParameterType_Type = Generalization(general=Type, specific=model_types_ParameterType)
gen_model_types_StateVariableType_Type = Generalization(general=Type, specific=model_types_StateVariableType)
gen_model_types_JSONType_Type = Generalization(general=Type, specific=model_types_JSONType)
gen_model_types_TextType_Type = Generalization(general=Type, specific=model_types_TextType)
gen_model_types_URLType_Type = Generalization(general=Type, specific=model_types_URLType)
gen_model_types_PointType_Type = Generalization(general=Type, specific=model_types_PointType)
gen_model_types_ArrayType_Type = Generalization(general=Type, specific=model_types_ArrayType)
gen_model_types_CompositeVisualType_VisualType = Generalization(general=VisualType, specific=model_types_CompositeVisualType)
gen_model_types_DynamicsType_Type = Generalization(general=Type, specific=model_types_DynamicsType)
gen_model_types_ArgumentType_Type = Generalization(general=Type, specific=model_types_ArgumentType)
gen_model_types_ExpressionType_Type = Generalization(general=Type, specific=model_types_ExpressionType)
gen_model_types_HTMLType_Type = Generalization(general=Type, specific=model_types_HTMLType)
gen_model_types_MetadataType_Type = Generalization(general=Type, specific=model_types_MetadataType)
gen_model_values_Value_ISynchable = Generalization(general=ISynchable, specific=model_values_Value)
gen_model_values_Composite_Value = Generalization(general=Value, specific=model_values_Composite)
gen_model_values_Quantity_Value = Generalization(general=Value, specific=model_values_Quantity)
gen_model_values_PhysicalQuantity_Quantity = Generalization(general=Quantity, specific=model_values_PhysicalQuantity)
gen_model_values_Unit_Value = Generalization(general=Value, specific=model_values_Unit)
gen_model_values_TimeSeries_Value = Generalization(general=Value, specific=model_values_TimeSeries)
gen_model_values_MDTimeSeries_Value = Generalization(general=Value, specific=model_values_MDTimeSeries)
gen_model_types_ConnectionType_Type = Generalization(general=Type, specific=model_types_ConnectionType)
gen_model_types_SimpleType_Type = Generalization(general=Type, specific=model_types_SimpleType)
gen_model_types_ImageType_Type = Generalization(general=Type, specific=model_types_ImageType)
gen_model_types_SimpleArrayType_Type = Generalization(general=Type, specific=model_types_SimpleArrayType)
gen_model_values_Point_Value = Generalization(general=Value, specific=model_values_Point)
gen_model_values_Dynamics_Value = Generalization(general=Value, specific=model_values_Dynamics)
gen_model_values_MetadataValue_Value = Generalization(general=Value, specific=model_values_MetadataValue)
gen_model_values_Text_MetadataValue = Generalization(general=MetadataValue, specific=model_values_Text)
gen_model_values_URL_MetadataValue = Generalization(general=MetadataValue, specific=model_values_URL)
gen_model_values_HTML_MetadataValue = Generalization(general=MetadataValue, specific=model_values_HTML)
gen_model_values_Pointer_Value = Generalization(general=Value, specific=model_values_Pointer)
gen_model_values_VisualValue_Value = Generalization(general=Value, specific=model_values_VisualValue)
gen_model_values_Collada_VisualValue = Generalization(general=VisualValue, specific=model_values_Collada)
gen_model_values_OBJ_VisualValue = Generalization(general=VisualValue, specific=model_values_OBJ)
gen_model_values_Sphere_VisualValue = Generalization(general=VisualValue, specific=model_values_Sphere)
gen_model_values_Cylinder_VisualValue = Generalization(general=VisualValue, specific=model_values_Cylinder)
gen_model_values_Particles_Value = Generalization(general=Value, specific=model_values_Particles)
gen_model_values_SkeletonAnimation_VisualValue = Generalization(general=VisualValue, specific=model_values_SkeletonAnimation)
gen_model_values_Function_Value = Generalization(general=Value, specific=model_values_Function)
gen_model_values_Argument_Value = Generalization(general=Value, specific=model_values_Argument)
gen_model_values_Expression_Value = Generalization(general=Value, specific=model_values_Expression)
gen_model_values_Connection_Value = Generalization(general=Value, specific=model_values_Connection)
gen_model_values_ArrayElement_Value = Generalization(general=Value, specific=model_values_ArrayElement)
gen_model_values_ArrayValue_Value = Generalization(general=Value, specific=model_values_ArrayValue)
gen_model_values_Image_Value = Generalization(general=Value, specific=model_values_Image)
gen_model_values_VisualGroupElement_Node = Generalization(general=Node, specific=model_values_VisualGroupElement)
gen_model_values_VisualGroup_Node = Generalization(general=Node, specific=model_values_VisualGroup)
gen_model_values_StringArray_AArrayValue = Generalization(general=AArrayValue, specific=model_values_StringArray)
gen_model_values_IntArray_AArrayValue = Generalization(general=AArrayValue, specific=model_values_IntArray)
gen_model_values_DoubleArray_AArrayValue = Generalization(general=AArrayValue, specific=model_values_DoubleArray)
gen_model_values_AArrayValue_Value = Generalization(general=Value, specific=model_values_AArrayValue)
gen_model_variables_Variable_Node = Generalization(general=Node, specific=model_variables_Variable)
gen_model_values_ImportValue_Value = Generalization(general=Value, specific=model_values_ImportValue)
gen_model_values_Metadata_MetadataValue = Generalization(general=MetadataValue, specific=model_values_Metadata)
gen_model_values_JSON_MetadataValue = Generalization(general=MetadataValue, specific=model_values_JSON)
gen_model_values_GenericArray_AArrayValue = Generalization(general=AArrayValue, specific=model_values_GenericArray)
gen_model_datasources_Query_Node = Generalization(general=Node, specific=model_datasources_Query)
gen_model_datasources_ProcessQuery_Query = Generalization(general=Query, specific=model_datasources_ProcessQuery)
gen_model_datasources_DataSource_Node = Generalization(general=Node, specific=model_datasources_DataSource)
gen_model_datasources_QueryResult_AQueryResult = Generalization(general=AQueryResult, specific=model_datasources_QueryResult)
gen_model_datasources_SerializableQueryResult_AQueryResult = Generalization(general=AQueryResult, specific=model_datasources_SerializableQueryResult)
gen_model_datasources_SimpleQuery_Query = Generalization(general=Query, specific=model_datasources_SimpleQuery)
gen_model_datasources_CompoundQuery_Query = Generalization(general=Query, specific=model_datasources_CompoundQuery)
gen_model_datasources_CompoundRefQuery_Query = Generalization(general=Query, specific=model_datasources_CompoundRefQuery)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_GeppettoLibrary, model_Tag, DataSource, Query, model_Node, ISynchable, Node, model_GeppettoModel, Variable, Pointer, Value, model_DomainModel, model_ModelFormat, model_ExternalDomainModel, DomainModel, model_StringToStringMap, model_ISynchable, model_types_Type, Type, model_LibraryManager, model_ExperimentState, model_VariableValue, model_types_VisualType, VisualValue, model_types_ImportType, model_types_CompositeType, Composite, model_types_PointerType, model_types_QuantityType, Quantity, model_types_ParameterType, model_types_StateVariableType, VisualType, types_model_DomainModel, model_types_JSONType, JSON, model_types_TextType, Text, model_types_URLType, URL, model_types_PointType, Point, model_types_ArrayType, ArrayValue, model_types_CompositeVisualType, VisualGroup, model_types_DynamicsType, Dynamics, model_types_ArgumentType, Argument, model_types_ExpressionType, Expression, model_types_HTMLType, HTML, model_types_MetadataType, model_values_Value, model_values_Composite, StringToValueMap, model_values_StringToValueMap, model_values_Quantity, model_values_PhysicalQuantity, Unit, model_values_Unit, model_values_TimeSeries, model_values_MDTimeSeries, model_types_ConnectionType, model_types_SimpleType, model_types_ImageType, Image, model_types_SimpleArrayType, AArrayValue, model_values_PointerElement, model_values_Point, model_values_Dynamics, PhysicalQuantity, Function, model_values_FunctionPlot, model_values_MetadataValue, model_values_Text, MetadataValue, model_values_URL, model_values_HTML, model_values_Pointer, PointerElement, model_values_VisualValue, VisualGroupElement, model_values_Collada, model_values_OBJ, model_values_Sphere, model_values_Cylinder, model_values_Particles, model_values_SkeletonAnimation, model_values_Function, FunctionPlot, model_values_Argument, model_values_Expression, model_values_ArrayElement, model_values_ArrayValue, ArrayElement, model_values_Image, SkeletonTransformation, model_values_SkeletonTransformation, model_values_VisualGroupElement, model_values_VisualGroup, model_values_Connection, model_values_StringArray, model_values_IntArray, model_values_DoubleArray, model_values_AArrayValue, model_variables_Variable, TypeToValueMap, model_variables_TypeToValueMap, model_values_ImportValue, model_values_Metadata, model_values_JSON, model_values_GenericArray, datasources_model_GeppettoLibrary, model_datasources_DataSourceLibraryConfiguration, model_datasources_Query, QueryMatchingCriteria, model_datasources_ProcessQuery, datasources_model_StringToStringMap, model_datasources_DataSource, DataSourceLibraryConfiguration, model_datasources_QueryResults, AQueryResult, model_datasources_RunnableQuery, model_datasources_AQueryResult, model_datasources_QueryResult, model_datasources_SerializableQueryResult, model_datasources_QueryMatchingCriteria, model_datasources_SimpleQuery, model_datasources_CompoundQuery, model_datasources_CompoundRefQuery, FileFormat, Connectivity, ImageFormat, BooleanOperator},
    associations={libraries1, tags3, dataSources5, queries7, tags9, variables0, pointer22, value24, tags27, format29, types11, sharedTypes13, libraries16, recordedVariables18, setParameters19, defaultValue38, variables39, defaultValue41, defaultValue43, defaultValue45, defaultValue46, defaultValue48, superType30, visualType32, referencedVariables34, domainModel36, defaultValue54, defaultValue55, defaultValue56, defaultValue57, arrayType58, defaultValue60, variables62, visualGroups64, defaultValue50, defaultValue51, defaultValue52, defaultValue53, value73, value74, unit76, unit77, variables66, defaultValue68, defaultValue71, defaultValue72, point82, variable85, type87, initialCondition90, dynamics91, value79, elements81, groupElements100, position101, distal104, particles106, arguments93, expression95, functionPlot98, a113, b115, position118, initialValue120, elements123, skeletonTransformationSeries108, parameter109, visualGroupElements111, elements126, anonymousTypes128, types130, initialValues132, position134, key137, value124, queries143, dependenciesLibrary146, targetLibrary148, fetchVariableQuery151, library154, matchingCriteria156, returnType157, parameters160, value139, libraryConfigurations142, queryChain163, results165, type166, queryChain161},
    generalizations={gen_model_Node_ISynchable, gen_model_GeppettoLibrary_Node, gen_model_Tag_ISynchable, gen_model_ExternalDomainModel_DomainModel, gen_model_types_Type_Node, gen_model_types_VisualType_Type, gen_model_types_ImportType_Type, gen_model_types_CompositeType_Type, gen_model_types_PointerType_Type, gen_model_types_QuantityType_Type, gen_model_types_ParameterType_Type, gen_model_types_StateVariableType_Type, gen_model_types_JSONType_Type, gen_model_types_TextType_Type, gen_model_types_URLType_Type, gen_model_types_PointType_Type, gen_model_types_ArrayType_Type, gen_model_types_CompositeVisualType_VisualType, gen_model_types_DynamicsType_Type, gen_model_types_ArgumentType_Type, gen_model_types_ExpressionType_Type, gen_model_types_HTMLType_Type, gen_model_types_MetadataType_Type, gen_model_values_Value_ISynchable, gen_model_values_Composite_Value, gen_model_values_Quantity_Value, gen_model_values_PhysicalQuantity_Quantity, gen_model_values_Unit_Value, gen_model_values_TimeSeries_Value, gen_model_values_MDTimeSeries_Value, gen_model_types_ConnectionType_Type, gen_model_types_SimpleType_Type, gen_model_types_ImageType_Type, gen_model_types_SimpleArrayType_Type, gen_model_values_Point_Value, gen_model_values_Dynamics_Value, gen_model_values_MetadataValue_Value, gen_model_values_Text_MetadataValue, gen_model_values_URL_MetadataValue, gen_model_values_HTML_MetadataValue, gen_model_values_Pointer_Value, gen_model_values_VisualValue_Value, gen_model_values_Collada_VisualValue, gen_model_values_OBJ_VisualValue, gen_model_values_Sphere_VisualValue, gen_model_values_Cylinder_VisualValue, gen_model_values_Particles_Value, gen_model_values_SkeletonAnimation_VisualValue, gen_model_values_Function_Value, gen_model_values_Argument_Value, gen_model_values_Expression_Value, gen_model_values_Connection_Value, gen_model_values_ArrayElement_Value, gen_model_values_ArrayValue_Value, gen_model_values_Image_Value, gen_model_values_VisualGroupElement_Node, gen_model_values_VisualGroup_Node, gen_model_values_StringArray_AArrayValue, gen_model_values_IntArray_AArrayValue, gen_model_values_DoubleArray_AArrayValue, gen_model_values_AArrayValue_Value, gen_model_variables_Variable_Node, gen_model_values_ImportValue_Value, gen_model_values_Metadata_MetadataValue, gen_model_values_JSON_MetadataValue, gen_model_values_GenericArray_AArrayValue, gen_model_datasources_Query_Node, gen_model_datasources_ProcessQuery_Query, gen_model_datasources_DataSource_Node, gen_model_datasources_QueryResult_AQueryResult, gen_model_datasources_SerializableQueryResult_AQueryResult, gen_model_datasources_SimpleQuery_Query, gen_model_datasources_CompoundQuery_Query, gen_model_datasources_CompoundRefQuery_Query},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)