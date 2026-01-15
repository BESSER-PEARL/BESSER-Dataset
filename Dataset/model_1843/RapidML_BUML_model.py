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
HTTPMethods: Enumeration = Enumeration(
    name="HTTPMethods",
    literals={
            EnumerationLiteral(name="GET"),
			EnumerationLiteral(name="PUT"),
			EnumerationLiteral(name="POST"),
			EnumerationLiteral(name="DELETE"),
			EnumerationLiteral(name="HEAD"),
			EnumerationLiteral(name="PATCH"),
			EnumerationLiteral(name="TRACE"),
			EnumerationLiteral(name="OPTIONS"),
			EnumerationLiteral(name="CONNECT")
    }
)

ReferenceRealizationEnum: Enumeration = Enumeration(
    name="ReferenceRealizationEnum",
    literals={
            EnumerationLiteral(name="EMBED"),
			EnumerationLiteral(name="LINK")
    }
)

HttpMessageParameterLocation: Enumeration = Enumeration(
    name="HttpMessageParameterLocation",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="QUERY"),
			EnumerationLiteral(name="HEADER")
    }
)

CollectionRealizationEnum: Enumeration = Enumeration(
    name="CollectionRealizationEnum",
    literals={
            EnumerationLiteral(name="EMBEDDED_OBJECT_LIST"),
			EnumerationLiteral(name="REFERENCE_LINK_LIST")
    }
)

AuthenticationTypes: Enumeration = Enumeration(
    name="AuthenticationTypes",
    literals={
            EnumerationLiteral(name="BASIC"),
			EnumerationLiteral(name="OAUTH2"),
			EnumerationLiteral(name="CUSTOM")
    }
)

AuthenticationFlows: Enumeration = Enumeration(
    name="AuthenticationFlows",
    literals={
            EnumerationLiteral(name="IMPLICIT"),
			EnumerationLiteral(name="PASSWORD"),
			EnumerationLiteral(name="APPLICATION"),
			EnumerationLiteral(name="ACCESS_CODE")
    }
)

CollectionRealizationLevelEnum: Enumeration = Enumeration(
    name="CollectionRealizationLevelEnum",
    literals={
            EnumerationLiteral(name="ITEM_LEVEL"),
			EnumerationLiteral(name="COLLECTION_LEVEL")
    }
)

# Classes
rapidml_TypedMessage = Class(name="rapidml::TypedMessage", is_abstract=True)
RealizationContainer = Class(name="RealizationContainer")
rapidml_ResourceDefinition = Class(name="rapidml::ResourceDefinition", is_abstract=True)
RESTElement = Class(name="RESTElement")
WithExamples = Class(name="WithExamples")
HasSecurityValue = Class(name="HasSecurityValue")
rapidml_Method = Class(name="rapidml::Method")
rapidml_MediaType = Class(name="rapidml::MediaType")
rapidml_URI = Class(name="rapidml::URI")
rapidml_MessageParameter = Class(name="rapidml::MessageParameter")
Extensible = Class(name="Extensible")
rapidml_TypedRequest = Class(name="rapidml::TypedRequest")
rapidml_TypedResponse = Class(name="rapidml::TypedResponse")
rapidml_Parameter = Class(name="rapidml::Parameter", is_abstract=True)
rapidml_SourceReference = Class(name="rapidml::SourceReference", is_abstract=True)
rapidml_RESTElement = Class(name="rapidml::RESTElement")
Documentable = Class(name="Documentable")
rapidml_Documentation = Class(name="rapidml::Documentation")
rapidml_Documentable = Class(name="rapidml::Documentable")
rapidml_CollectionResource = Class(name="rapidml::CollectionResource")
ServiceDataResource = Class(name="ServiceDataResource")
rapidml_CollectionParameter = Class(name="rapidml::CollectionParameter")
rapidml_CollectionReferenceElement = Class(name="rapidml::CollectionReferenceElement")
TypedMessage = Class(name="TypedMessage")
rapidml_URIParameter = Class(name="rapidml::URIParameter", is_abstract=True)
Parameter_ = Class(name="Parameter")
rapidml_URISegmentWithParameter = Class(name="rapidml::URISegmentWithParameter")
rapidml_MatrixParameter = Class(name="rapidml::MatrixParameter")
URIParameter = Class(name="URIParameter")
rapidml_TemplateParameter = Class(name="rapidml::TemplateParameter")
rapidml_ResourceAPI = Class(name="rapidml::ResourceAPI")
rapidml_ObjectResource = Class(name="rapidml::ObjectResource")
rapidml_PropertyReference = Class(name="rapidml::PropertyReference")
SourceReference = Class(name="SourceReference")
rapidml_PrimitiveProperty = Class(name="rapidml::PrimitiveProperty")
rapidml_ZenModel = Class(name="rapidml::ZenModel")
HasTitle = Class(name="HasTitle")
rapidml_LinkRelation = Class(name="rapidml::LinkRelation")
rapidml_ReferenceRealization = Class(name="rapidml::ReferenceRealization")
rapidml_DataModel = Class(name="rapidml::DataModel")
rapidml_MediaTypesLibrary = Class(name="rapidml::MediaTypesLibrary")
rapidml_LinkRelationsLibrary = Class(name="rapidml::LinkRelationsLibrary")
rapidml_PrimitiveTypesLibrary = Class(name="rapidml::PrimitiveTypesLibrary")
rapidml_ImportDeclaration = Class(name="rapidml::ImportDeclaration")
rapidml_SecuritySchemeLibrary = Class(name="rapidml::SecuritySchemeLibrary")
rapidml_RealizationModelLocation = Class(name="rapidml::RealizationModelLocation")
rapidml_ServiceDataResource = Class(name="rapidml::ServiceDataResource")
ResourceDefinition = Class(name="ResourceDefinition")
rapidml_NamedLinkDescriptor = Class(name="rapidml::NamedLinkDescriptor")
rapidml_ReferenceTreatment = Class(name="rapidml::ReferenceTreatment")
rapidml_ReferenceElement = Class(name="rapidml::ReferenceElement", is_abstract=True)
rapidml_PathSegment = Class(name="rapidml::PathSegment", is_abstract=True)
rapidml_PrimitiveTypeSourceReference = Class(name="rapidml::PrimitiveTypeSourceReference")
rapidml_ReferenceLink = Class(name="rapidml::ReferenceLink")
ReferenceTreatment = Class(name="ReferenceTreatment")
rapidml_ReferenceEmbed = Class(name="rapidml::ReferenceEmbed")
ObjectRealization = Class(name="ObjectRealization")
rapidml_PrimitiveType = Class(name="rapidml::PrimitiveType")
HasStringValue = Class(name="HasStringValue")
rapidml_URISegment = Class(name="rapidml::URISegment")
URISegment = Class(name="URISegment")
rapidml_PropertyRealization = Class(name="rapidml::PropertyRealization")
ConstrainableType = Class(name="ConstrainableType")
rapidml_InlineExample = Class(name="rapidml::InlineExample")
Example = Class(name="Example")
rapidml_Feature = Class(name="rapidml::Feature", is_abstract=True)
rapidml_WithExamples = Class(name="rapidml::WithExamples", is_abstract=True)
rapidml_Example = Class(name="rapidml::Example", is_abstract=True)
rapidml_HasStringValue = Class(name="rapidml::HasStringValue", is_abstract=True)
rapidml_ExternalExample = Class(name="rapidml::ExternalExample")
rapidml_SecurityScope = Class(name="rapidml::SecurityScope")
rapidml_SecuritySchemeParameter = Class(name="rapidml::SecuritySchemeParameter")
rapidml_ObjectRealization = Class(name="rapidml::ObjectRealization")
rapidml_RealizationContainer = Class(name="rapidml::RealizationContainer", is_abstract=True)
ReferenceElement = Class(name="ReferenceElement")
rapidml_HasSecurityValue = Class(name="rapidml::HasSecurityValue", is_abstract=True)
rapidml_AuthenticationMethod = Class(name="rapidml::AuthenticationMethod")
rapidml_SecurityScheme = Class(name="rapidml::SecurityScheme")
rapidml_Structure = Class(name="rapidml::Structure")
rapidml_Extensible = Class(name="rapidml::Extensible", is_abstract=True)
rapidml_Extension = Class(name="rapidml::Extension")
rapidml_HasTitle = Class(name="rapidml::HasTitle", is_abstract=True)
rapidml_Operation = Class(name="rapidml::Operation")
Element = Class(name="Element")
rapidml_ReferenceProperty = Class(name="rapidml::ReferenceProperty")
Feature = Class(name="Feature")
rapidml_DataType = Class(name="rapidml::DataType", is_abstract=True)
rapidml_SingleValueType = Class(name="rapidml::SingleValueType", is_abstract=True)
DataType = Class(name="DataType")
WithDataExamples = Class(name="WithDataExamples")
Inheritable = Class(name="Inheritable")
rapidml_Inheritable = Class(name="rapidml::Inheritable", is_abstract=True)
rapidml_SimpleType = Class(name="rapidml::SimpleType", is_abstract=True)
rapidml_WithDataExamples = Class(name="rapidml::WithDataExamples", is_abstract=True)
rapidml_DataExample = Class(name="rapidml::DataExample", is_abstract=True)
rapidml_InlineDataExample = Class(name="rapidml::InlineDataExample")
DataExample = Class(name="DataExample")
rapidml_Constraint = Class(name="rapidml::Constraint", is_abstract=True)
rapidml_Enumeration = Class(name="rapidml::Enumeration")
SingleValueType = Class(name="SingleValueType")
rapidml_EnumConstant = Class(name="rapidml::EnumConstant")
rapidml_UserDefinedType = Class(name="rapidml::UserDefinedType")
SimpleType = Class(name="SimpleType")
rapidml_Element = Class(name="rapidml::Element", is_abstract=True)
rapidml_LengthConstraint = Class(name="rapidml::LengthConstraint")
Constraint = Class(name="Constraint")
rapidml_RegExConstraint = Class(name="rapidml::RegExConstraint")
rapidml_ValueRangeConstraint = Class(name="rapidml::ValueRangeConstraint")
rapidml_ConstrainableType = Class(name="rapidml::ConstrainableType", is_abstract=True)

# rapidml_TypedMessage class attributes and methods
rapidml_TypedMessage_useParentTypeReference: Property = Property(name="useParentTypeReference", type=BooleanType)
rapidml_TypedMessage_m_getAllExamples: Method = Method(name="getAllExamples", parameters={}, type=StringType)
rapidml_TypedMessage_m_isIncluded: Method = Method(name="isIncluded", parameters={Parameter(name='feature')}, type=BooleanType)
rapidml_TypedMessage_m_getIncludedProperties: Method = Method(name="getIncludedProperties", parameters={}, type=StringType)
rapidml_TypedMessage_m_getActualType: Method = Method(name="getActualType", parameters={}, type=StringType)
rapidml_TypedMessage_m_getReferenceLinks: Method = Method(name="getReferenceLinks", parameters={}, type=StringType)
rapidml_TypedMessage.attributes={rapidml_TypedMessage_useParentTypeReference}
rapidml_TypedMessage.methods={rapidml_TypedMessage_m_isIncluded, rapidml_TypedMessage_m_getReferenceLinks, rapidml_TypedMessage_m_getIncludedProperties, rapidml_TypedMessage_m_getActualType, rapidml_TypedMessage_m_getAllExamples}

# RealizationContainer class attributes and methods

# rapidml_ResourceDefinition class attributes and methods
rapidml_ResourceDefinition_name: Property = Property(name="name", type=StringType)
rapidml_ResourceDefinition.attributes={rapidml_ResourceDefinition_name}

# RESTElement class attributes and methods

# WithExamples class attributes and methods

# HasSecurityValue class attributes and methods

# rapidml_Method class attributes and methods
rapidml_Method_id: Property = Property(name="id", type=StringType)
rapidml_Method_httpMethod: Property = Property(name="httpMethod", type=StringType)
rapidml_Method_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
rapidml_Method.attributes={rapidml_Method_id, rapidml_Method_httpMethod}
rapidml_Method.methods={rapidml_Method_m_getName}

# rapidml_MediaType class attributes and methods
rapidml_MediaType_name: Property = Property(name="name", type=StringType)
rapidml_MediaType_specURL: Property = Property(name="specURL", type=StringType)
rapidml_MediaType_m_hashCode: Method = Method(name="hashCode", parameters={}, type=IntegerType)
rapidml_MediaType_m_equals: Method = Method(name="equals", parameters={Parameter(name='other')}, type=BooleanType)
rapidml_MediaType.attributes={rapidml_MediaType_specURL, rapidml_MediaType_name}
rapidml_MediaType.methods={rapidml_MediaType_m_hashCode, rapidml_MediaType_m_equals}

# rapidml_URI class attributes and methods

# rapidml_MessageParameter class attributes and methods
rapidml_MessageParameter_httpLocation: Property = Property(name="httpLocation", type=StringType)
rapidml_MessageParameter.attributes={rapidml_MessageParameter_httpLocation}

# Extensible class attributes and methods

# rapidml_TypedRequest class attributes and methods

# rapidml_TypedResponse class attributes and methods
rapidml_TypedResponse_statusCode: Property = Property(name="statusCode", type=IntegerType)
rapidml_TypedResponse.attributes={rapidml_TypedResponse_statusCode}

# rapidml_Parameter class attributes and methods
rapidml_Parameter_name: Property = Property(name="name", type=StringType)
rapidml_Parameter_required: Property = Property(name="required", type=BooleanType)
rapidml_Parameter_default: Property = Property(name="default", type=StringType)
rapidml_Parameter_fixed: Property = Property(name="fixed", type=StringType)
rapidml_Parameter_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
rapidml_Parameter_m_getPrimitiveType: Method = Method(name="getPrimitiveType", parameters={}, type=StringType)
rapidml_Parameter_m_getConstraints: Method = Method(name="getConstraints", parameters={}, type=StringType)
rapidml_Parameter.attributes={rapidml_Parameter_required, rapidml_Parameter_default, rapidml_Parameter_name, rapidml_Parameter_fixed}
rapidml_Parameter.methods={rapidml_Parameter_m_getType, rapidml_Parameter_m_getPrimitiveType, rapidml_Parameter_m_getConstraints}

# rapidml_SourceReference class attributes and methods
rapidml_SourceReference_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
rapidml_SourceReference_m_getConstraints: Method = Method(name="getConstraints", parameters={}, type=StringType)
rapidml_SourceReference_m_getPrimitiveType: Method = Method(name="getPrimitiveType", parameters={}, type=StringType)
rapidml_SourceReference.methods={rapidml_SourceReference_m_getPrimitiveType, rapidml_SourceReference_m_getType, rapidml_SourceReference_m_getConstraints}

# rapidml_RESTElement class attributes and methods

# Documentable class attributes and methods

# rapidml_Documentation class attributes and methods
rapidml_Documentation_text: Property = Property(name="text", type=StringType)
rapidml_Documentation.attributes={rapidml_Documentation_text}

# rapidml_Documentable class attributes and methods

# rapidml_CollectionResource class attributes and methods
rapidml_CollectionResource_resourceRealizationKind: Property = Property(name="resourceRealizationKind", type=StringType)
rapidml_CollectionResource.attributes={rapidml_CollectionResource_resourceRealizationKind}

# ServiceDataResource class attributes and methods

# rapidml_CollectionParameter class attributes and methods

# rapidml_CollectionReferenceElement class attributes and methods
rapidml_CollectionReferenceElement_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
rapidml_CollectionReferenceElement.methods={rapidml_CollectionReferenceElement_m_getName}

# TypedMessage class attributes and methods

# rapidml_URIParameter class attributes and methods
rapidml_URIParameter_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
rapidml_URIParameter.methods={rapidml_URIParameter_m_getName}

# Parameter class attributes and methods

# rapidml_URISegmentWithParameter class attributes and methods

# rapidml_MatrixParameter class attributes and methods

# URIParameter class attributes and methods

# rapidml_TemplateParameter class attributes and methods

# rapidml_ResourceAPI class attributes and methods
rapidml_ResourceAPI_name: Property = Property(name="name", type=StringType)
rapidml_ResourceAPI_version: Property = Property(name="version", type=StringType)
rapidml_ResourceAPI_baseURI: Property = Property(name="baseURI", type=StringType)
rapidml_ResourceAPI.attributes={rapidml_ResourceAPI_name, rapidml_ResourceAPI_baseURI, rapidml_ResourceAPI_version}

# rapidml_ObjectResource class attributes and methods

# rapidml_PropertyReference class attributes and methods
rapidml_PropertyReference_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
rapidml_PropertyReference_m_getConstraints: Method = Method(name="getConstraints", parameters={}, type=StringType)
rapidml_PropertyReference.methods={rapidml_PropertyReference_m_getType, rapidml_PropertyReference_m_getConstraints}

# SourceReference class attributes and methods

# rapidml_PrimitiveProperty class attributes and methods
rapidml_PrimitiveProperty_m_getPrimitiveType: Method = Method(name="getPrimitiveType", parameters={}, type=StringType)
rapidml_PrimitiveProperty.methods={rapidml_PrimitiveProperty_m_getPrimitiveType}

# rapidml_ZenModel class attributes and methods
rapidml_ZenModel_name: Property = Property(name="name", type=StringType)
rapidml_ZenModel_namespace: Property = Property(name="namespace", type=StringType)
rapidml_ZenModel.attributes={rapidml_ZenModel_name, rapidml_ZenModel_namespace}

# HasTitle class attributes and methods

# rapidml_LinkRelation class attributes and methods
rapidml_LinkRelation_name: Property = Property(name="name", type=StringType)
rapidml_LinkRelation_specURL: Property = Property(name="specURL", type=StringType)
rapidml_LinkRelation.attributes={rapidml_LinkRelation_specURL, rapidml_LinkRelation_name}

# rapidml_ReferenceRealization class attributes and methods
rapidml_ReferenceRealization_realizationType: Property = Property(name="realizationType", type=StringType)
rapidml_ReferenceRealization_multiValued: Property = Property(name="multiValued", type=BooleanType)
rapidml_ReferenceRealization_m_getLinkDescriptor: Method = Method(name="getLinkDescriptor", parameters={}, type=StringType)
rapidml_ReferenceRealization.attributes={rapidml_ReferenceRealization_realizationType, rapidml_ReferenceRealization_multiValued}
rapidml_ReferenceRealization.methods={rapidml_ReferenceRealization_m_getLinkDescriptor}

# rapidml_DataModel class attributes and methods
rapidml_DataModel_name: Property = Property(name="name", type=StringType)
rapidml_DataModel.attributes={rapidml_DataModel_name}

# rapidml_MediaTypesLibrary class attributes and methods

# rapidml_LinkRelationsLibrary class attributes and methods
rapidml_LinkRelationsLibrary_name: Property = Property(name="name", type=StringType)
rapidml_LinkRelationsLibrary.attributes={rapidml_LinkRelationsLibrary_name}

# rapidml_PrimitiveTypesLibrary class attributes and methods
rapidml_PrimitiveTypesLibrary_name: Property = Property(name="name", type=StringType)
rapidml_PrimitiveTypesLibrary.attributes={rapidml_PrimitiveTypesLibrary_name}

# rapidml_ImportDeclaration class attributes and methods
rapidml_ImportDeclaration_importURI: Property = Property(name="importURI", type=StringType)
rapidml_ImportDeclaration_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
rapidml_ImportDeclaration_alias: Property = Property(name="alias", type=StringType)
rapidml_ImportDeclaration.attributes={rapidml_ImportDeclaration_importURI, rapidml_ImportDeclaration_importedNamespace, rapidml_ImportDeclaration_alias}

# rapidml_SecuritySchemeLibrary class attributes and methods
rapidml_SecuritySchemeLibrary_name: Property = Property(name="name", type=StringType)
rapidml_SecuritySchemeLibrary.attributes={rapidml_SecuritySchemeLibrary_name}

# rapidml_RealizationModelLocation class attributes and methods
rapidml_RealizationModelLocation_uri: Property = Property(name="uri", type=StringType)
rapidml_RealizationModelLocation_m_getRealizationModel: Method = Method(name="getRealizationModel", parameters={}, type=StringType)
rapidml_RealizationModelLocation.attributes={rapidml_RealizationModelLocation_uri}
rapidml_RealizationModelLocation.methods={rapidml_RealizationModelLocation_m_getRealizationModel}

# rapidml_ServiceDataResource class attributes and methods
rapidml_ServiceDataResource_default: Property = Property(name="default", type=BooleanType)
rapidml_ServiceDataResource_m_getDefaultLinkDescriptor: Method = Method(name="getDefaultLinkDescriptor", parameters={}, type=StringType)
rapidml_ServiceDataResource_m_isIncluded: Method = Method(name="isIncluded", parameters={Parameter(name='feature')}, type=BooleanType)
rapidml_ServiceDataResource_m_getReferenceLinks: Method = Method(name="getReferenceLinks", parameters={}, type=StringType)
rapidml_ServiceDataResource_m_getAllReferenceTreatments: Method = Method(name="getAllReferenceTreatments", parameters={}, type=StringType)
rapidml_ServiceDataResource_m_getIncludedProperties: Method = Method(name="getIncludedProperties", parameters={}, type=StringType)
rapidml_ServiceDataResource.attributes={rapidml_ServiceDataResource_default}
rapidml_ServiceDataResource.methods={rapidml_ServiceDataResource_m_isIncluded, rapidml_ServiceDataResource_m_getReferenceLinks, rapidml_ServiceDataResource_m_getIncludedProperties, rapidml_ServiceDataResource_m_getAllReferenceTreatments, rapidml_ServiceDataResource_m_getDefaultLinkDescriptor}

# ResourceDefinition class attributes and methods

# rapidml_NamedLinkDescriptor class attributes and methods
rapidml_NamedLinkDescriptor_default: Property = Property(name="default", type=BooleanType)
rapidml_NamedLinkDescriptor_name: Property = Property(name="name", type=StringType)
rapidml_NamedLinkDescriptor.attributes={rapidml_NamedLinkDescriptor_default, rapidml_NamedLinkDescriptor_name}

# rapidml_ReferenceTreatment class attributes and methods
rapidml_ReferenceTreatment_m_getEmbedHierarchy: Method = Method(name="getEmbedHierarchy", parameters={}, type=StringType)
rapidml_ReferenceTreatment_m_getLinkDescriptor: Method = Method(name="getLinkDescriptor", parameters={}, type=StringType)
rapidml_ReferenceTreatment.methods={rapidml_ReferenceTreatment_m_getEmbedHierarchy, rapidml_ReferenceTreatment_m_getLinkDescriptor}

# rapidml_ReferenceElement class attributes and methods
rapidml_ReferenceElement_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
rapidml_ReferenceElement.methods={rapidml_ReferenceElement_m_getName}

# rapidml_PathSegment class attributes and methods

# rapidml_PrimitiveTypeSourceReference class attributes and methods
rapidml_PrimitiveTypeSourceReference_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
rapidml_PrimitiveTypeSourceReference_m_getConstraints: Method = Method(name="getConstraints", parameters={}, type=StringType)
rapidml_PrimitiveTypeSourceReference.methods={rapidml_PrimitiveTypeSourceReference_m_getType, rapidml_PrimitiveTypeSourceReference_m_getConstraints}

# rapidml_ReferenceLink class attributes and methods
rapidml_ReferenceLink_name: Property = Property(name="name", type=StringType)
rapidml_ReferenceLink_collectionRealizationLevel: Property = Property(name="collectionRealizationLevel", type=StringType)
rapidml_ReferenceLink_m_getTargetResource: Method = Method(name="getTargetResource", parameters={}, type=ResourceDefinition)
rapidml_ReferenceLink.attributes={rapidml_ReferenceLink_name, rapidml_ReferenceLink_collectionRealizationLevel}
rapidml_ReferenceLink.methods={rapidml_ReferenceLink_m_getTargetResource}

# ReferenceTreatment class attributes and methods

# rapidml_ReferenceEmbed class attributes and methods
rapidml_ReferenceEmbed_m_getAllNestedReferenceTreatments: Method = Method(name="getAllNestedReferenceTreatments", parameters={}, type=ReferenceTreatment)
rapidml_ReferenceEmbed_m_getNestedReferenceTreatments: Method = Method(name="getNestedReferenceTreatments", parameters={}, type=ReferenceTreatment)
rapidml_ReferenceEmbed.methods={rapidml_ReferenceEmbed_m_getNestedReferenceTreatments, rapidml_ReferenceEmbed_m_getAllNestedReferenceTreatments}

# ObjectRealization class attributes and methods

# rapidml_PrimitiveType class attributes and methods
rapidml_PrimitiveType_m_getPrimitiveType: Method = Method(name="getPrimitiveType", parameters={}, type=StringType)
rapidml_PrimitiveType.methods={rapidml_PrimitiveType_m_getPrimitiveType}

# HasStringValue class attributes and methods

# rapidml_URISegment class attributes and methods
rapidml_URISegment_name: Property = Property(name="name", type=StringType)
rapidml_URISegment.attributes={rapidml_URISegment_name}

# URISegment class attributes and methods

# rapidml_PropertyRealization class attributes and methods
rapidml_PropertyRealization_cardinality: Property = Property(name="cardinality", type=StringType)
rapidml_PropertyRealization_m_getPrimitiveType: Method = Method(name="getPrimitiveType", parameters={}, type=StringType)
rapidml_PropertyRealization_m_getMinOccurs: Method = Method(name="getMinOccurs", parameters={}, type=IntegerType)
rapidml_PropertyRealization_m_getMaxOccurs: Method = Method(name="getMaxOccurs", parameters={}, type=IntegerType)
rapidml_PropertyRealization.attributes={rapidml_PropertyRealization_cardinality}
rapidml_PropertyRealization.methods={rapidml_PropertyRealization_m_getMaxOccurs, rapidml_PropertyRealization_m_getPrimitiveType, rapidml_PropertyRealization_m_getMinOccurs}

# ConstrainableType class attributes and methods

# rapidml_InlineExample class attributes and methods
rapidml_InlineExample_body: Property = Property(name="body", type=StringType)
rapidml_InlineExample.attributes={rapidml_InlineExample_body}

# Example class attributes and methods

# rapidml_Feature class attributes and methods
rapidml_Feature_name: Property = Property(name="name", type=StringType)
rapidml_Feature_restriction: Property = Property(name="restriction", type=BooleanType)
rapidml_Feature_readOnly: Property = Property(name="readOnly", type=BooleanType)
rapidml_Feature_key: Property = Property(name="key", type=BooleanType)
rapidml_Feature_m_getMinOccurs: Method = Method(name="getMinOccurs", parameters={}, type=IntegerType)
rapidml_Feature_m_getMaxOccurs: Method = Method(name="getMaxOccurs", parameters={}, type=IntegerType)
rapidml_Feature.attributes={rapidml_Feature_readOnly, rapidml_Feature_restriction, rapidml_Feature_key, rapidml_Feature_name}
rapidml_Feature.methods={rapidml_Feature_m_getMaxOccurs, rapidml_Feature_m_getMinOccurs}

# rapidml_WithExamples class attributes and methods

# rapidml_Example class attributes and methods
rapidml_Example_m_getBody: Method = Method(name="getBody", parameters={}, type=StringType)
rapidml_Example.methods={rapidml_Example_m_getBody}

# rapidml_HasStringValue class attributes and methods
rapidml_HasStringValue_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
rapidml_HasStringValue.methods={rapidml_HasStringValue_m_toString}

# rapidml_ExternalExample class attributes and methods
rapidml_ExternalExample_path: Property = Property(name="path", type=StringType)
rapidml_ExternalExample_m_getBody: Method = Method(name="getBody", parameters={}, type=StringType)
rapidml_ExternalExample.attributes={rapidml_ExternalExample_path}
rapidml_ExternalExample.methods={rapidml_ExternalExample_m_getBody}

# rapidml_SecurityScope class attributes and methods
rapidml_SecurityScope_name: Property = Property(name="name", type=StringType)
rapidml_SecurityScope.attributes={rapidml_SecurityScope_name}

# rapidml_SecuritySchemeParameter class attributes and methods
rapidml_SecuritySchemeParameter_name: Property = Property(name="name", type=StringType)
rapidml_SecuritySchemeParameter_value: Property = Property(name="value", type=StringType)
rapidml_SecuritySchemeParameter.attributes={rapidml_SecuritySchemeParameter_name, rapidml_SecuritySchemeParameter_value}

# rapidml_ObjectRealization class attributes and methods
rapidml_ObjectRealization_m_getDataType: Method = Method(name="getDataType", parameters={}, type=StringType)
rapidml_ObjectRealization_m_getAllIncludedProperties: Method = Method(name="getAllIncludedProperties", parameters={}, type=StringType)
rapidml_ObjectRealization.methods={rapidml_ObjectRealization_m_getDataType, rapidml_ObjectRealization_m_getAllIncludedProperties}

# rapidml_RealizationContainer class attributes and methods
rapidml_RealizationContainer_withDefaultRealization: Property = Property(name="withDefaultRealization", type=BooleanType)
rapidml_RealizationContainer_realizationName: Property = Property(name="realizationName", type=StringType)
rapidml_RealizationContainer_effectiveRealization: Property = Property(name="effectiveRealization", type=StringType)
rapidml_RealizationContainer_m_getActualType: Method = Method(name="getActualType", parameters={}, type=StringType)
rapidml_RealizationContainer.attributes={rapidml_RealizationContainer_withDefaultRealization, rapidml_RealizationContainer_realizationName, rapidml_RealizationContainer_effectiveRealization}
rapidml_RealizationContainer.methods={rapidml_RealizationContainer_m_getActualType}

# ReferenceElement class attributes and methods

# rapidml_HasSecurityValue class attributes and methods

# rapidml_AuthenticationMethod class attributes and methods

# rapidml_SecurityScheme class attributes and methods
rapidml_SecurityScheme_name: Property = Property(name="name", type=StringType)
rapidml_SecurityScheme_type: Property = Property(name="type", type=StringType)
rapidml_SecurityScheme_flow: Property = Property(name="flow", type=StringType)
rapidml_SecurityScheme.attributes={rapidml_SecurityScheme_type, rapidml_SecurityScheme_name, rapidml_SecurityScheme_flow}

# rapidml_Structure class attributes and methods
rapidml_Structure_m_getReferenceProperties: Method = Method(name="getReferenceProperties", parameters={}, type=StringType)
rapidml_Structure_m_getPrimitiveProperties: Method = Method(name="getPrimitiveProperties", parameters={}, type=StringType)
rapidml_Structure_m_getAllPrimitiveProperties: Method = Method(name="getAllPrimitiveProperties", parameters={}, type=StringType)
rapidml_Structure.methods={rapidml_Structure_m_getAllPrimitiveProperties, rapidml_Structure_m_getPrimitiveProperties, rapidml_Structure_m_getReferenceProperties}

# rapidml_Extensible class attributes and methods

# rapidml_Extension class attributes and methods
rapidml_Extension_name: Property = Property(name="name", type=StringType)
rapidml_Extension_value: Property = Property(name="value", type=StringType)
rapidml_Extension.attributes={rapidml_Extension_name, rapidml_Extension_value}

# rapidml_HasTitle class attributes and methods
rapidml_HasTitle_title: Property = Property(name="title", type=StringType)
rapidml_HasTitle.attributes={rapidml_HasTitle_title}

# rapidml_Operation class attributes and methods
rapidml_Operation_name: Property = Property(name="name", type=StringType)
rapidml_Operation.attributes={rapidml_Operation_name}

# Element class attributes and methods

# rapidml_ReferenceProperty class attributes and methods
rapidml_ReferenceProperty_containment: Property = Property(name="containment", type=BooleanType)
rapidml_ReferenceProperty_container: Property = Property(name="container", type=BooleanType)
rapidml_ReferenceProperty.attributes={rapidml_ReferenceProperty_container, rapidml_ReferenceProperty_containment}

# Feature class attributes and methods

# rapidml_DataType class attributes and methods
rapidml_DataType_name: Property = Property(name="name", type=StringType)
rapidml_DataType.attributes={rapidml_DataType_name}

# rapidml_SingleValueType class attributes and methods
rapidml_SingleValueType_m_getPrimitiveType: Method = Method(name="getPrimitiveType", parameters={}, type=StringType)
rapidml_SingleValueType.methods={rapidml_SingleValueType_m_getPrimitiveType}

# DataType class attributes and methods

# WithDataExamples class attributes and methods

# Inheritable class attributes and methods

# rapidml_Inheritable class attributes and methods

# rapidml_SimpleType class attributes and methods

# rapidml_WithDataExamples class attributes and methods

# rapidml_DataExample class attributes and methods

# rapidml_InlineDataExample class attributes and methods
rapidml_InlineDataExample_body: Property = Property(name="body", type=StringType)
rapidml_InlineDataExample.attributes={rapidml_InlineDataExample_body}

# DataExample class attributes and methods

# rapidml_Constraint class attributes and methods
rapidml_Constraint_m_supports: Method = Method(name="supports", parameters={Parameter(name='type')}, type=BooleanType)
rapidml_Constraint.methods={rapidml_Constraint_m_supports}

# rapidml_Enumeration class attributes and methods
rapidml_Enumeration_m_getPrimitiveType: Method = Method(name="getPrimitiveType", parameters={}, type=StringType)
rapidml_Enumeration.methods={rapidml_Enumeration_m_getPrimitiveType}

# SingleValueType class attributes and methods

# rapidml_EnumConstant class attributes and methods
rapidml_EnumConstant_name: Property = Property(name="name", type=StringType)
rapidml_EnumConstant_integerValue: Property = Property(name="integerValue", type=IntegerType)
rapidml_EnumConstant_literalValue: Property = Property(name="literalValue", type=StringType)
rapidml_EnumConstant_m_getImplicitIntegerValue: Method = Method(name="getImplicitIntegerValue", parameters={}, type=IntegerType)
rapidml_EnumConstant.attributes={rapidml_EnumConstant_name, rapidml_EnumConstant_integerValue, rapidml_EnumConstant_literalValue}
rapidml_EnumConstant.methods={rapidml_EnumConstant_m_getImplicitIntegerValue}

# rapidml_UserDefinedType class attributes and methods
rapidml_UserDefinedType_m_getPrimitiveType: Method = Method(name="getPrimitiveType", parameters={}, type=StringType)
rapidml_UserDefinedType.methods={rapidml_UserDefinedType_m_getPrimitiveType}

# SimpleType class attributes and methods

# rapidml_Element class attributes and methods
rapidml_Element_cardinality: Property = Property(name="cardinality", type=StringType)
rapidml_Element_m_isMultiValued: Method = Method(name="isMultiValued", parameters={}, type=BooleanType)
rapidml_Element_m_getMinOccurs: Method = Method(name="getMinOccurs", parameters={}, type=IntegerType)
rapidml_Element_m_getMaxOccurs: Method = Method(name="getMaxOccurs", parameters={}, type=IntegerType)
rapidml_Element_m_getDataType: Method = Method(name="getDataType", parameters={}, type=StringType)
rapidml_Element.attributes={rapidml_Element_cardinality}
rapidml_Element.methods={rapidml_Element_m_getDataType, rapidml_Element_m_isMultiValued, rapidml_Element_m_getMaxOccurs, rapidml_Element_m_getMinOccurs}

# rapidml_LengthConstraint class attributes and methods
rapidml_LengthConstraint_minLength: Property = Property(name="minLength", type=IntegerType)
rapidml_LengthConstraint_maxLength: Property = Property(name="maxLength", type=IntegerType)
rapidml_LengthConstraint_length: Property = Property(name="length", type=IntegerType)
rapidml_LengthConstraint.attributes={rapidml_LengthConstraint_maxLength, rapidml_LengthConstraint_length, rapidml_LengthConstraint_minLength}

# Constraint class attributes and methods

# rapidml_RegExConstraint class attributes and methods
rapidml_RegExConstraint_pattern: Property = Property(name="pattern", type=StringType)
rapidml_RegExConstraint.attributes={rapidml_RegExConstraint_pattern}

# rapidml_ValueRangeConstraint class attributes and methods
rapidml_ValueRangeConstraint_minValue: Property = Property(name="minValue", type=StringType)
rapidml_ValueRangeConstraint_minValueExclusive: Property = Property(name="minValueExclusive", type=BooleanType)
rapidml_ValueRangeConstraint_maxValue: Property = Property(name="maxValue", type=StringType)
rapidml_ValueRangeConstraint_maxValueExclusive: Property = Property(name="maxValueExclusive", type=BooleanType)
rapidml_ValueRangeConstraint.attributes={rapidml_ValueRangeConstraint_maxValueExclusive, rapidml_ValueRangeConstraint_minValueExclusive, rapidml_ValueRangeConstraint_minValue, rapidml_ValueRangeConstraint_maxValue}

# rapidml_ConstrainableType class attributes and methods
rapidml_ConstrainableType_m_getConstrainableParent: Method = Method(name="getConstrainableParent", parameters={}, type=ConstrainableType)
rapidml_ConstrainableType_m_getAllConstraints: Method = Method(name="getAllConstraints", parameters={}, type=Constraint)
rapidml_ConstrainableType.methods={rapidml_ConstrainableType_m_getAllConstraints, rapidml_ConstrainableType_m_getConstrainableParent}

# Relationships
methods0: BinaryAssociation = BinaryAssociation(
    name="methods0",
    ends={
        Property(name="Method", type=rapidml_ResourceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="containingResourceDefinition", type=rapidml_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mediaTypes1: BinaryAssociation = BinaryAssociation(
    name="mediaTypes1",
    ends={
        Property(name="rapidml_MediaType", type=rapidml_ResourceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ResourceDefinition", type=rapidml_MediaType, multiplicity=Multiplicity(0, 9999))
    }
)
allMediaTypes2: BinaryAssociation = BinaryAssociation(
    name="allMediaTypes2",
    ends={
        Property(name="rapidml_MediaType4", type=rapidml_ResourceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ResourceDefinition3", type=rapidml_MediaType, multiplicity=Multiplicity(0, 9999))
    }
)
URI5: BinaryAssociation = BinaryAssociation(
    name="URI5",
    ends={
        Property(name="rapidml_URI", type=rapidml_ResourceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ResourceDefinition6", type=rapidml_URI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters7: BinaryAssociation = BinaryAssociation(
    name="parameters7",
    ends={
        Property(name="MessageParameter", type=rapidml_TypedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="containingMessage", type=rapidml_MessageParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceType8: BinaryAssociation = BinaryAssociation(
    name="resourceType8",
    ends={
        Property(name="rapidml_ResourceDefinition9", type=rapidml_TypedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_TypedMessage", type=rapidml_ResourceDefinition, multiplicity=Multiplicity(0, 1))
    }
)
mediaTypes10: BinaryAssociation = BinaryAssociation(
    name="mediaTypes10",
    ends={
        Property(name="rapidml_MediaType12", type=rapidml_TypedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_TypedMessage11", type=rapidml_MediaType, multiplicity=Multiplicity(0, 9999))
    }
)
request13: BinaryAssociation = BinaryAssociation(
    name="request13",
    ends={
        Property(name="TypedRequest", type=rapidml_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="containingMethod", type=rapidml_TypedRequest, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
responses14: BinaryAssociation = BinaryAssociation(
    name="responses14",
    ends={
        Property(name="TypedResponse", type=rapidml_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="containingMethod15", type=rapidml_TypedResponse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containingResourceDefinition16: BinaryAssociation = BinaryAssociation(
    name="containingResourceDefinition16",
    ends={
        Property(name="ResourceDefinition", type=rapidml_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=rapidml_ResourceDefinition, multiplicity=Multiplicity(0, 1))
    }
)
sourceReference17: BinaryAssociation = BinaryAssociation(
    name="sourceReference17",
    ends={
        Property(name="SourceReference", type=rapidml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="containingParameter", type=rapidml_SourceReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
documentation18: BinaryAssociation = BinaryAssociation(
    name="documentation18",
    ends={
        Property(name="rapidml_Documentation", type=rapidml_Documentable, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_Documentable", type=rapidml_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collectionParameters28: BinaryAssociation = BinaryAssociation(
    name="collectionParameters28",
    ends={
        Property(name="CollectionParameter", type=rapidml_CollectionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="containingResourceDefinition29", type=rapidml_CollectionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
derivedFrom20: BinaryAssociation = BinaryAssociation(
    name="derivedFrom20",
    ends={
        Property(name="rapidml_MediaType21", type=rapidml_MediaType, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_MediaType19", type=rapidml_MediaType, multiplicity=Multiplicity(0, 9999))
    }
)
containingMethod22: BinaryAssociation = BinaryAssociation(
    name="containingMethod22",
    ends={
        Property(name="Method23", type=rapidml_TypedRequest, multiplicity=Multiplicity(1, 1)),
        Property(name="request", type=rapidml_Method, multiplicity=Multiplicity(0, 1))
    }
)
containingMethod24: BinaryAssociation = BinaryAssociation(
    name="containingMethod24",
    ends={
        Property(name="Method25", type=rapidml_TypedResponse, multiplicity=Multiplicity(1, 1)),
        Property(name="responses", type=rapidml_Method, multiplicity=Multiplicity(0, 1))
    }
)
uriSegment26: BinaryAssociation = BinaryAssociation(
    name="uriSegment26",
    ends={
        Property(name="rapidml_URISegmentWithParameter", type=rapidml_URIParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_URIParameter", type=rapidml_URISegmentWithParameter, multiplicity=Multiplicity(0, 1))
    }
)
containingURI27: BinaryAssociation = BinaryAssociation(
    name="containingURI27",
    ends={
        Property(name="URI", type=rapidml_URIParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uriParameters", type=rapidml_URI, multiplicity=Multiplicity(0, 1))
    }
)
resourceAPIs35: BinaryAssociation = BinaryAssociation(
    name="resourceAPIs35",
    ends={
        Property(name="rapidml_ResourceAPI", type=rapidml_ZenModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ZenModel", type=rapidml_ResourceAPI, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenceElements30: BinaryAssociation = BinaryAssociation(
    name="referenceElements30",
    ends={
        Property(name="rapidml_CollectionReferenceElement", type=rapidml_CollectionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_CollectionResource", type=rapidml_CollectionReferenceElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containingResourceDefinition31: BinaryAssociation = BinaryAssociation(
    name="containingResourceDefinition31",
    ends={
        Property(name="CollectionResource", type=rapidml_CollectionParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionParameters", type=rapidml_CollectionResource, multiplicity=Multiplicity(0, 1))
    }
)
conceptualFeature32: BinaryAssociation = BinaryAssociation(
    name="conceptualFeature32",
    ends={
        Property(name="rapidml_PrimitiveProperty", type=rapidml_PropertyReference, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_PropertyReference", type=rapidml_PrimitiveProperty, multiplicity=Multiplicity(0, 1))
    }
)
containingParameter33: BinaryAssociation = BinaryAssociation(
    name="containingParameter33",
    ends={
        Property(name="Parameter", type=rapidml_SourceReference, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceReference", type=rapidml_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
containingMessage34: BinaryAssociation = BinaryAssociation(
    name="containingMessage34",
    ends={
        Property(name="TypedMessage", type=rapidml_MessageParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=rapidml_TypedMessage, multiplicity=Multiplicity(0, 1))
    }
)
definedMediaTypes57: BinaryAssociation = BinaryAssociation(
    name="definedMediaTypes57",
    ends={
        Property(name="rapidml_ResourceAPI58", type=rapidml_MediaType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="rapidml_MediaType59", type=rapidml_ResourceAPI, multiplicity=Multiplicity(1, 1))
    }
)
definedLinkRelations60: BinaryAssociation = BinaryAssociation(
    name="definedLinkRelations60",
    ends={
        Property(name="rapidml_LinkRelation", type=rapidml_ResourceAPI, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ResourceAPI61", type=rapidml_LinkRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultReferenceRealizations62: BinaryAssociation = BinaryAssociation(
    name="defaultReferenceRealizations62",
    ends={
        Property(name="rapidml_ReferenceRealization", type=rapidml_ResourceAPI, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ResourceAPI63", type=rapidml_ReferenceRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataModels36: BinaryAssociation = BinaryAssociation(
    name="dataModels36",
    ends={
        Property(name="rapidml_DataModel", type=rapidml_ZenModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ZenModel37", type=rapidml_DataModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mediaTypesLibrary38: BinaryAssociation = BinaryAssociation(
    name="mediaTypesLibrary38",
    ends={
        Property(name="rapidml_MediaTypesLibrary", type=rapidml_ZenModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ZenModel39", type=rapidml_MediaTypesLibrary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
linkRelationsLibrary40: BinaryAssociation = BinaryAssociation(
    name="linkRelationsLibrary40",
    ends={
        Property(name="rapidml_LinkRelationsLibrary", type=rapidml_ZenModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ZenModel41", type=rapidml_LinkRelationsLibrary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primitiveTypesLibrary42: BinaryAssociation = BinaryAssociation(
    name="primitiveTypesLibrary42",
    ends={
        Property(name="rapidml_PrimitiveTypesLibrary", type=rapidml_ZenModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ZenModel43", type=rapidml_PrimitiveTypesLibrary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports44: BinaryAssociation = BinaryAssociation(
    name="imports44",
    ends={
        Property(name="rapidml_ImportDeclaration", type=rapidml_ZenModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ZenModel45", type=rapidml_ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
securitySchemesLibrary46: BinaryAssociation = BinaryAssociation(
    name="securitySchemesLibrary46",
    ends={
        Property(name="rapidml_SecuritySchemeLibrary", type=rapidml_ZenModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ZenModel47", type=rapidml_SecuritySchemeLibrary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedResourceDefinitions48: BinaryAssociation = BinaryAssociation(
    name="ownedResourceDefinitions48",
    ends={
        Property(name="rapidml_ResourceDefinition50", type=rapidml_ResourceAPI, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ResourceAPI49", type=rapidml_ResourceDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceDataModels51: BinaryAssociation = BinaryAssociation(
    name="serviceDataModels51",
    ends={
        Property(name="rapidml_DataModel53", type=rapidml_ResourceAPI, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ResourceAPI52", type=rapidml_DataModel, multiplicity=Multiplicity(0, 9999))
    }
)
formats54: BinaryAssociation = BinaryAssociation(
    name="formats54",
    ends={
        Property(name="rapidml_MediaType56", type=rapidml_ResourceAPI, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ResourceAPI55", type=rapidml_MediaType, multiplicity=Multiplicity(0, 9999))
    }
)
referenceElement67: BinaryAssociation = BinaryAssociation(
    name="referenceElement67",
    ends={
        Property(name="rapidml_ReferenceTreatment", type=rapidml_ReferenceElement, multiplicity=Multiplicity(0, 1)),
        Property(name="rapidml_ReferenceElement", type=rapidml_ReferenceTreatment, multiplicity=Multiplicity(1, 1))
    }
)
referenceRealization68: BinaryAssociation = BinaryAssociation(
    name="referenceRealization68",
    ends={
        Property(name="rapidml_ReferenceRealization70", type=rapidml_ReferenceTreatment, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ReferenceTreatment69", type=rapidml_ReferenceRealization, multiplicity=Multiplicity(0, 1))
    }
)
ownedReferenceRealization71: BinaryAssociation = BinaryAssociation(
    name="ownedReferenceRealization71",
    ends={
        Property(name="rapidml_ReferenceRealization73", type=rapidml_ReferenceTreatment, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ReferenceTreatment72", type=rapidml_ReferenceRealization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
autoRealizations64: BinaryAssociation = BinaryAssociation(
    name="autoRealizations64",
    ends={
        Property(name="rapidml_RealizationModelLocation", type=rapidml_ResourceAPI, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ResourceAPI65", type=rapidml_RealizationModelLocation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definedLinkDescriptors66: BinaryAssociation = BinaryAssociation(
    name="definedLinkDescriptors66",
    ends={
        Property(name="rapidml_NamedLinkDescriptor", type=rapidml_ServiceDataResource, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ServiceDataResource", type=rapidml_NamedLinkDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenceElement79: BinaryAssociation = BinaryAssociation(
    name="referenceElement79",
    ends={
        Property(name="rapidml_ReferenceElement80", type=rapidml_PathSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_PathSegment", type=rapidml_ReferenceElement, multiplicity=Multiplicity(0, 1))
    }
)
targetResource74: BinaryAssociation = BinaryAssociation(
    name="targetResource74",
    ends={
        Property(name="rapidml_ResourceDefinition76", type=rapidml_ReferenceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ReferenceRealization75", type=rapidml_ResourceDefinition, multiplicity=Multiplicity(0, 1))
    }
)
linkRelation77: BinaryAssociation = BinaryAssociation(
    name="linkRelation77",
    ends={
        Property(name="rapidml_LinkRelation78", type=rapidml_ReferenceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ReferenceLink", type=rapidml_LinkRelation, multiplicity=Multiplicity(0, 1))
    }
)
simpleType81: BinaryAssociation = BinaryAssociation(
    name="simpleType81",
    ends={
        Property(name="rapidml_PrimitiveType", type=rapidml_PrimitiveTypeSourceReference, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_PrimitiveTypeSourceReference", type=rapidml_PrimitiveType, multiplicity=Multiplicity(0, 1))
    }
)
segments82: BinaryAssociation = BinaryAssociation(
    name="segments82",
    ends={
        Property(name="rapidml_URISegment", type=rapidml_URI, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_URI83", type=rapidml_URISegment, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
uriParameters84: BinaryAssociation = BinaryAssociation(
    name="uriParameters84",
    ends={
        Property(name="URIParameter", type=rapidml_URI, multiplicity=Multiplicity(1, 1)),
        Property(name="containingURI", type=rapidml_URIParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseProperty85: BinaryAssociation = BinaryAssociation(
    name="baseProperty85",
    ends={
        Property(name="rapidml_Feature", type=rapidml_PropertyRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_PropertyRealization", type=rapidml_Feature, multiplicity=Multiplicity(1, 1))
    }
)
examples86: BinaryAssociation = BinaryAssociation(
    name="examples86",
    ends={
        Property(name="rapidml_Example", type=rapidml_WithExamples, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_WithExamples", type=rapidml_Example, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopes100: BinaryAssociation = BinaryAssociation(
    name="scopes100",
    ends={
        Property(name="rapidml_SecurityScope", type=rapidml_SecurityScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_SecurityScheme", type=rapidml_SecurityScope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
settings101: BinaryAssociation = BinaryAssociation(
    name="settings101",
    ends={
        Property(name="rapidml_SecuritySchemeParameter", type=rapidml_SecurityScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_SecurityScheme102", type=rapidml_SecuritySchemeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters103: BinaryAssociation = BinaryAssociation(
    name="parameters103",
    ends={
        Property(name="rapidml_MessageParameter", type=rapidml_SecurityScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_SecurityScheme104", type=rapidml_MessageParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedModel87: BinaryAssociation = BinaryAssociation(
    name="importedModel87",
    ends={
        Property(name="rapidml_ZenModel89", type=rapidml_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ImportDeclaration88", type=rapidml_ZenModel, multiplicity=Multiplicity(0, 1))
    }
)
exclusivePropertyList90: BinaryAssociation = BinaryAssociation(
    name="exclusivePropertyList90",
    ends={
        Property(name="rapidml_PropertyRealization91", type=rapidml_ObjectRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ObjectRealization", type=rapidml_PropertyRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
overriddenPropertyList92: BinaryAssociation = BinaryAssociation(
    name="overriddenPropertyList92",
    ends={
        Property(name="rapidml_PropertyRealization94", type=rapidml_ObjectRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ObjectRealization93", type=rapidml_PropertyRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
excludedProperties95: BinaryAssociation = BinaryAssociation(
    name="excludedProperties95",
    ends={
        Property(name="rapidml_Feature97", type=rapidml_ObjectRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ObjectRealization96", type=rapidml_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
realizationContainer98: BinaryAssociation = BinaryAssociation(
    name="realizationContainer98",
    ends={
        Property(name="RealizationContainer", type=rapidml_ObjectRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="inlineObjectRealization", type=rapidml_RealizationContainer, multiplicity=Multiplicity(0, 1))
    }
)
securedBy99: BinaryAssociation = BinaryAssociation(
    name="securedBy99",
    ends={
        Property(name="rapidml_AuthenticationMethod", type=rapidml_HasSecurityValue, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_HasSecurityValue", type=rapidml_AuthenticationMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inlineObjectRealization116: BinaryAssociation = BinaryAssociation(
    name="inlineObjectRealization116",
    ends={
        Property(name="ObjectRealization", type=rapidml_RealizationContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="realizationContainer", type=rapidml_ObjectRealization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties117: BinaryAssociation = BinaryAssociation(
    name="properties117",
    ends={
        Property(name="rapidml_ObjectRealization118", type=rapidml_RealizationContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_RealizationContainer", type=rapidml_ObjectRealization, multiplicity=Multiplicity(0, 1))
    }
)
errorResponses105: BinaryAssociation = BinaryAssociation(
    name="errorResponses105",
    ends={
        Property(name="rapidml_TypedResponse", type=rapidml_SecurityScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_SecurityScheme106", type=rapidml_TypedResponse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scheme107: BinaryAssociation = BinaryAssociation(
    name="scheme107",
    ends={
        Property(name="rapidml_SecurityScheme109", type=rapidml_AuthenticationMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_AuthenticationMethod108", type=rapidml_SecurityScheme, multiplicity=Multiplicity(1, 1))
    }
)
scopes110: BinaryAssociation = BinaryAssociation(
    name="scopes110",
    ends={
        Property(name="rapidml_SecurityScope112", type=rapidml_AuthenticationMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_AuthenticationMethod111", type=rapidml_SecurityScope, multiplicity=Multiplicity(0, 9999))
    }
)
securitySchemes113: BinaryAssociation = BinaryAssociation(
    name="securitySchemes113",
    ends={
        Property(name="rapidml_SecurityScheme115", type=rapidml_SecuritySchemeLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_SecuritySchemeLibrary114", type=rapidml_SecurityScheme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definedLinkRelations128: BinaryAssociation = BinaryAssociation(
    name="definedLinkRelations128",
    ends={
        Property(name="rapidml_LinkRelation130", type=rapidml_LinkRelationsLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_LinkRelationsLibrary129", type=rapidml_LinkRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenceTreatments119: BinaryAssociation = BinaryAssociation(
    name="referenceTreatments119",
    ends={
        Property(name="rapidml_ReferenceTreatment121", type=rapidml_RealizationContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_RealizationContainer120", type=rapidml_ReferenceTreatment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType122: BinaryAssociation = BinaryAssociation(
    name="dataType122",
    ends={
        Property(name="rapidml_Structure", type=rapidml_RealizationContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_RealizationContainer123", type=rapidml_Structure, multiplicity=Multiplicity(0, 1))
    }
)
extensions124: BinaryAssociation = BinaryAssociation(
    name="extensions124",
    ends={
        Property(name="rapidml_Extension", type=rapidml_Extensible, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_Extensible", type=rapidml_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mediaTypes125: BinaryAssociation = BinaryAssociation(
    name="mediaTypes125",
    ends={
        Property(name="rapidml_MediaType127", type=rapidml_MediaTypesLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_MediaTypesLibrary126", type=rapidml_MediaType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inverse138: BinaryAssociation = BinaryAssociation(
    name="inverse138",
    ends={
        Property(name="rapidml_ReferenceProperty139", type=rapidml_ReferenceProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ReferenceProperty137", type=rapidml_ReferenceProperty, multiplicity=Multiplicity(0, 1))
    }
)
primitiveTypes131: BinaryAssociation = BinaryAssociation(
    name="primitiveTypes131",
    ends={
        Property(name="rapidml_PrimitiveType133", type=rapidml_PrimitiveTypesLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_PrimitiveTypesLibrary132", type=rapidml_PrimitiveType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containingDataType134: BinaryAssociation = BinaryAssociation(
    name="containingDataType134",
    ends={
        Property(name="Structure", type=rapidml_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedFeatures", type=rapidml_Structure, multiplicity=Multiplicity(0, 1))
    }
)
type135: BinaryAssociation = BinaryAssociation(
    name="type135",
    ends={
        Property(name="rapidml_Structure136", type=rapidml_ReferenceProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ReferenceProperty", type=rapidml_Structure, multiplicity=Multiplicity(1, 1))
    }
)
allSupertypes150: BinaryAssociation = BinaryAssociation(
    name="allSupertypes150",
    ends={
        Property(name="rapidml_Inheritable152", type=rapidml_Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_Structure151", type=rapidml_Inheritable, multiplicity=Multiplicity(0, 9999))
    }
)
ownedDataTypes153: BinaryAssociation = BinaryAssociation(
    name="ownedDataTypes153",
    ends={
        Property(name="rapidml_DataType", type=rapidml_DataModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_DataModel154", type=rapidml_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type140: BinaryAssociation = BinaryAssociation(
    name="type140",
    ends={
        Property(name="rapidml_SingleValueType", type=rapidml_PrimitiveProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_PrimitiveProperty141", type=rapidml_SingleValueType, multiplicity=Multiplicity(1, 1))
    }
)
ownedFeatures142: BinaryAssociation = BinaryAssociation(
    name="ownedFeatures142",
    ends={
        Property(name="Feature", type=rapidml_Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="containingDataType", type=rapidml_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElements144: BinaryAssociation = BinaryAssociation(
    name="ownedElements144",
    ends={
        Property(name="rapidml_Structure145", type=rapidml_Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_Structure143", type=rapidml_Structure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperations146: BinaryAssociation = BinaryAssociation(
    name="ownedOperations146",
    ends={
        Property(name="rapidml_Operation", type=rapidml_Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_Structure147", type=rapidml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supertypes148: BinaryAssociation = BinaryAssociation(
    name="supertypes148",
    ends={
        Property(name="rapidml_Inheritable", type=rapidml_Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_Structure149", type=rapidml_Inheritable, multiplicity=Multiplicity(0, 9999))
    }
)
dataExamples155: BinaryAssociation = BinaryAssociation(
    name="dataExamples155",
    ends={
        Property(name="rapidml_DataExample", type=rapidml_WithDataExamples, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_WithDataExamples", type=rapidml_DataExample, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumConstants156: BinaryAssociation = BinaryAssociation(
    name="enumConstants156",
    ends={
        Property(name="EnumConstant", type=rapidml_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=rapidml_EnumConstant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseType157: BinaryAssociation = BinaryAssociation(
    name="baseType157",
    ends={
        Property(name="rapidml_PrimitiveType158", type=rapidml_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_Enumeration", type=rapidml_PrimitiveType, multiplicity=Multiplicity(1, 1))
    }
)
dataType161: BinaryAssociation = BinaryAssociation(
    name="dataType161",
    ends={
        Property(name="rapidml_Structure163", type=rapidml_ReferenceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ReferenceElement162", type=rapidml_Structure, multiplicity=Multiplicity(0, 1))
    }
)
enumeration159: BinaryAssociation = BinaryAssociation(
    name="enumeration159",
    ends={
        Property(name="Enumeration", type=rapidml_EnumConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="enumConstants", type=rapidml_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
baseType160: BinaryAssociation = BinaryAssociation(
    name="baseType160",
    ends={
        Property(name="rapidml_SimpleType", type=rapidml_UserDefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_UserDefinedType", type=rapidml_SimpleType, multiplicity=Multiplicity(1, 1))
    }
)
constraints164: BinaryAssociation = BinaryAssociation(
    name="constraints164",
    ends={
        Property(name="rapidml_Constraint", type=rapidml_ConstrainableType, multiplicity=Multiplicity(1, 1)),
        Property(name="rapidml_ConstrainableType", type=rapidml_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_rapidml_TypedMessage_RealizationContainer = Generalization(general=RealizationContainer, specific=rapidml_TypedMessage)
gen_rapidml_TypedMessage_RESTElement = Generalization(general=RESTElement, specific=rapidml_TypedMessage)
gen_rapidml_TypedMessage_WithExamples = Generalization(general=WithExamples, specific=rapidml_TypedMessage)
gen_rapidml_ResourceDefinition_RESTElement = Generalization(general=RESTElement, specific=rapidml_ResourceDefinition)
gen_rapidml_ResourceDefinition_WithExamples = Generalization(general=WithExamples, specific=rapidml_ResourceDefinition)
gen_rapidml_ResourceDefinition_HasSecurityValue = Generalization(general=HasSecurityValue, specific=rapidml_ResourceDefinition)
gen_rapidml_Method_RESTElement = Generalization(general=RESTElement, specific=rapidml_Method)
gen_rapidml_Method_HasSecurityValue = Generalization(general=HasSecurityValue, specific=rapidml_Method)
gen_rapidml_Method_Extensible = Generalization(general=Extensible, specific=rapidml_Method)
gen_rapidml_MediaType_RESTElement = Generalization(general=RESTElement, specific=rapidml_MediaType)
gen_rapidml_Parameter_RESTElement = Generalization(general=RESTElement, specific=rapidml_Parameter)
gen_rapidml_Parameter_Extensible = Generalization(general=Extensible, specific=rapidml_Parameter)
gen_rapidml_RESTElement_Documentable = Generalization(general=Documentable, specific=rapidml_RESTElement)
gen_rapidml_RESTElement_Extensible = Generalization(general=Extensible, specific=rapidml_RESTElement)
gen_rapidml_CollectionResource_ServiceDataResource = Generalization(general=ServiceDataResource, specific=rapidml_CollectionResource)
gen_rapidml_TypedRequest_TypedMessage = Generalization(general=TypedMessage, specific=rapidml_TypedRequest)
gen_rapidml_TypedResponse_TypedMessage = Generalization(general=TypedMessage, specific=rapidml_TypedResponse)
gen_rapidml_URIParameter_Parameter = Generalization(general=Parameter_, specific=rapidml_URIParameter)
gen_rapidml_MatrixParameter_URIParameter = Generalization(general=URIParameter, specific=rapidml_MatrixParameter)
gen_rapidml_TemplateParameter_URIParameter = Generalization(general=URIParameter, specific=rapidml_TemplateParameter)
gen_rapidml_ObjectResource_ServiceDataResource = Generalization(general=ServiceDataResource, specific=rapidml_ObjectResource)
gen_rapidml_CollectionParameter_Parameter = Generalization(general=Parameter_, specific=rapidml_CollectionParameter)
gen_rapidml_PropertyReference_SourceReference = Generalization(general=SourceReference, specific=rapidml_PropertyReference)
gen_rapidml_MessageParameter_Parameter = Generalization(general=Parameter_, specific=rapidml_MessageParameter)
gen_rapidml_ZenModel_Documentable = Generalization(general=Documentable, specific=rapidml_ZenModel)
gen_rapidml_ZenModel_Extensible = Generalization(general=Extensible, specific=rapidml_ZenModel)
gen_rapidml_ZenModel_HasTitle = Generalization(general=HasTitle, specific=rapidml_ZenModel)
gen_rapidml_ResourceAPI_RESTElement = Generalization(general=RESTElement, specific=rapidml_ResourceAPI)
gen_rapidml_ResourceAPI_HasSecurityValue = Generalization(general=HasSecurityValue, specific=rapidml_ResourceAPI)
gen_rapidml_ResourceAPI_HasTitle = Generalization(general=HasTitle, specific=rapidml_ResourceAPI)
gen_rapidml_ServiceDataResource_RealizationContainer = Generalization(general=RealizationContainer, specific=rapidml_ServiceDataResource)
gen_rapidml_ServiceDataResource_ResourceDefinition = Generalization(general=ResourceDefinition, specific=rapidml_ServiceDataResource)
gen_rapidml_ReferenceTreatment_Extensible = Generalization(general=Extensible, specific=rapidml_ReferenceTreatment)
gen_rapidml_PrimitiveTypeSourceReference_SourceReference = Generalization(general=SourceReference, specific=rapidml_PrimitiveTypeSourceReference)
gen_rapidml_ReferenceRealization_RealizationContainer = Generalization(general=RealizationContainer, specific=rapidml_ReferenceRealization)
gen_rapidml_ReferenceLink_ReferenceTreatment = Generalization(general=ReferenceTreatment, specific=rapidml_ReferenceLink)
gen_rapidml_ReferenceEmbed_ReferenceTreatment = Generalization(general=ReferenceTreatment, specific=rapidml_ReferenceEmbed)
gen_rapidml_NamedLinkDescriptor_ObjectRealization = Generalization(general=ObjectRealization, specific=rapidml_NamedLinkDescriptor)
gen_rapidml_URI_HasStringValue = Generalization(general=HasStringValue, specific=rapidml_URI)
gen_rapidml_URISegment_HasStringValue = Generalization(general=HasStringValue, specific=rapidml_URISegment)
gen_rapidml_URISegmentWithParameter_URISegment = Generalization(general=URISegment, specific=rapidml_URISegmentWithParameter)
gen_rapidml_PropertyRealization_ConstrainableType = Generalization(general=ConstrainableType, specific=rapidml_PropertyRealization)
gen_rapidml_InlineExample_Example = Generalization(general=Example, specific=rapidml_InlineExample)
gen_rapidml_LinkRelation_Documentable = Generalization(general=Documentable, specific=rapidml_LinkRelation)
gen_rapidml_ExternalExample_Example = Generalization(general=Example, specific=rapidml_ExternalExample)
gen_rapidml_ObjectRealization_Extensible = Generalization(general=Extensible, specific=rapidml_ObjectRealization)
gen_rapidml_CollectionReferenceElement_ReferenceElement = Generalization(general=ReferenceElement, specific=rapidml_CollectionReferenceElement)
gen_rapidml_SecurityScheme_Documentable = Generalization(general=Documentable, specific=rapidml_SecurityScheme)
gen_rapidml_SecurityScheme_RESTElement = Generalization(general=RESTElement, specific=rapidml_SecurityScheme)
gen_rapidml_SecurityScope_Documentable = Generalization(general=Documentable, specific=rapidml_SecurityScope)
gen_rapidml_SecuritySchemeParameter_Documentable = Generalization(general=Documentable, specific=rapidml_SecuritySchemeParameter)
gen_rapidml_SecuritySchemeLibrary_Documentable = Generalization(general=Documentable, specific=rapidml_SecuritySchemeLibrary)
gen_rapidml_RealizationContainer_Extensible = Generalization(general=Extensible, specific=rapidml_RealizationContainer)
gen_rapidml_PrimitiveProperty_Feature = Generalization(general=Feature, specific=rapidml_PrimitiveProperty)
gen_rapidml_PrimitiveProperty_HasStringValue = Generalization(general=HasStringValue, specific=rapidml_PrimitiveProperty)
gen_rapidml_PrimitiveProperty_ConstrainableType = Generalization(general=ConstrainableType, specific=rapidml_PrimitiveProperty)
gen_rapidml_Operation_Documentable = Generalization(general=Documentable, specific=rapidml_Operation)
gen_rapidml_Feature_Documentable = Generalization(general=Documentable, specific=rapidml_Feature)
gen_rapidml_Feature_Element = Generalization(general=Element, specific=rapidml_Feature)
gen_rapidml_Feature_Extensible = Generalization(general=Extensible, specific=rapidml_Feature)
gen_rapidml_ReferenceProperty_Feature = Generalization(general=Feature, specific=rapidml_ReferenceProperty)
gen_rapidml_ReferenceProperty_ReferenceElement = Generalization(general=ReferenceElement, specific=rapidml_ReferenceProperty)
gen_rapidml_DataModel_Documentable = Generalization(general=Documentable, specific=rapidml_DataModel)
gen_rapidml_DataModel_HasTitle = Generalization(general=HasTitle, specific=rapidml_DataModel)
gen_rapidml_Structure_DataType = Generalization(general=DataType, specific=rapidml_Structure)
gen_rapidml_Structure_WithDataExamples = Generalization(general=WithDataExamples, specific=rapidml_Structure)
gen_rapidml_Structure_Inheritable = Generalization(general=Inheritable, specific=rapidml_Structure)
gen_rapidml_SimpleType_SingleValueType = Generalization(general=SingleValueType, specific=rapidml_SimpleType)
gen_rapidml_EnumConstant_Documentable = Generalization(general=Documentable, specific=rapidml_EnumConstant)
gen_rapidml_InlineDataExample_DataExample = Generalization(general=DataExample, specific=rapidml_InlineDataExample)
gen_rapidml_Constraint_Extensible = Generalization(general=Extensible, specific=rapidml_Constraint)
gen_rapidml_Enumeration_SingleValueType = Generalization(general=SingleValueType, specific=rapidml_Enumeration)
gen_rapidml_ReferenceElement_Element = Generalization(general=Element, specific=rapidml_ReferenceElement)
gen_rapidml_UserDefinedType_SimpleType = Generalization(general=SimpleType, specific=rapidml_UserDefinedType)
gen_rapidml_UserDefinedType_ConstrainableType = Generalization(general=ConstrainableType, specific=rapidml_UserDefinedType)
gen_rapidml_PrimitiveType_SimpleType = Generalization(general=SimpleType, specific=rapidml_PrimitiveType)
gen_rapidml_DataType_Documentable = Generalization(general=Documentable, specific=rapidml_DataType)
gen_rapidml_DataType_Extensible = Generalization(general=Extensible, specific=rapidml_DataType)
gen_rapidml_SingleValueType_DataType = Generalization(general=DataType, specific=rapidml_SingleValueType)
gen_rapidml_LengthConstraint_Constraint = Generalization(general=Constraint, specific=rapidml_LengthConstraint)
gen_rapidml_RegExConstraint_Constraint = Generalization(general=Constraint, specific=rapidml_RegExConstraint)
gen_rapidml_ValueRangeConstraint_Constraint = Generalization(general=Constraint, specific=rapidml_ValueRangeConstraint)
gen_rapidml_ConstrainableType_Extensible = Generalization(general=Extensible, specific=rapidml_ConstrainableType)

# Domain Model
domain_model = DomainModel(
    name="rapidml",
    types={rapidml_TypedMessage, RealizationContainer, rapidml_ResourceDefinition, RESTElement, WithExamples, HasSecurityValue, rapidml_Method, rapidml_MediaType, rapidml_URI, rapidml_MessageParameter, Extensible, rapidml_TypedRequest, rapidml_TypedResponse, rapidml_Parameter, rapidml_SourceReference, rapidml_RESTElement, Documentable, rapidml_Documentation, rapidml_Documentable, rapidml_CollectionResource, ServiceDataResource, rapidml_CollectionParameter, rapidml_CollectionReferenceElement, TypedMessage, rapidml_URIParameter, Parameter_, rapidml_URISegmentWithParameter, rapidml_MatrixParameter, URIParameter, rapidml_TemplateParameter, rapidml_ResourceAPI, rapidml_ObjectResource, rapidml_PropertyReference, SourceReference, rapidml_PrimitiveProperty, rapidml_ZenModel, HasTitle, rapidml_LinkRelation, rapidml_ReferenceRealization, rapidml_DataModel, rapidml_MediaTypesLibrary, rapidml_LinkRelationsLibrary, rapidml_PrimitiveTypesLibrary, rapidml_ImportDeclaration, rapidml_SecuritySchemeLibrary, rapidml_RealizationModelLocation, rapidml_ServiceDataResource, ResourceDefinition, rapidml_NamedLinkDescriptor, rapidml_ReferenceTreatment, rapidml_ReferenceElement, rapidml_PathSegment, rapidml_PrimitiveTypeSourceReference, rapidml_ReferenceLink, ReferenceTreatment, rapidml_ReferenceEmbed, ObjectRealization, rapidml_PrimitiveType, HasStringValue, rapidml_URISegment, URISegment, rapidml_PropertyRealization, ConstrainableType, rapidml_InlineExample, Example, rapidml_Feature, rapidml_WithExamples, rapidml_Example, rapidml_HasStringValue, rapidml_ExternalExample, rapidml_SecurityScope, rapidml_SecuritySchemeParameter, rapidml_ObjectRealization, rapidml_RealizationContainer, ReferenceElement, rapidml_HasSecurityValue, rapidml_AuthenticationMethod, rapidml_SecurityScheme, rapidml_Structure, rapidml_Extensible, rapidml_Extension, rapidml_HasTitle, rapidml_Operation, Element, rapidml_ReferenceProperty, Feature, rapidml_DataType, rapidml_SingleValueType, DataType, WithDataExamples, Inheritable, rapidml_Inheritable, rapidml_SimpleType, rapidml_WithDataExamples, rapidml_DataExample, rapidml_InlineDataExample, DataExample, rapidml_Constraint, rapidml_Enumeration, SingleValueType, rapidml_EnumConstant, rapidml_UserDefinedType, SimpleType, rapidml_Element, rapidml_LengthConstraint, Constraint, rapidml_RegExConstraint, rapidml_ValueRangeConstraint, rapidml_ConstrainableType, HTTPMethods, ReferenceRealizationEnum, HttpMessageParameterLocation, CollectionRealizationEnum, AuthenticationTypes, AuthenticationFlows, CollectionRealizationLevelEnum},
    associations={methods0, mediaTypes1, allMediaTypes2, URI5, parameters7, resourceType8, mediaTypes10, request13, responses14, containingResourceDefinition16, sourceReference17, documentation18, collectionParameters28, derivedFrom20, containingMethod22, containingMethod24, uriSegment26, containingURI27, resourceAPIs35, referenceElements30, containingResourceDefinition31, conceptualFeature32, containingParameter33, containingMessage34, definedMediaTypes57, definedLinkRelations60, defaultReferenceRealizations62, dataModels36, mediaTypesLibrary38, linkRelationsLibrary40, primitiveTypesLibrary42, imports44, securitySchemesLibrary46, ownedResourceDefinitions48, serviceDataModels51, formats54, referenceElement67, referenceRealization68, ownedReferenceRealization71, autoRealizations64, definedLinkDescriptors66, referenceElement79, targetResource74, linkRelation77, simpleType81, segments82, uriParameters84, baseProperty85, examples86, scopes100, settings101, parameters103, importedModel87, exclusivePropertyList90, overriddenPropertyList92, excludedProperties95, realizationContainer98, securedBy99, inlineObjectRealization116, properties117, errorResponses105, scheme107, scopes110, securitySchemes113, definedLinkRelations128, referenceTreatments119, dataType122, extensions124, mediaTypes125, inverse138, primitiveTypes131, containingDataType134, type135, allSupertypes150, ownedDataTypes153, type140, ownedFeatures142, ownedElements144, ownedOperations146, supertypes148, dataExamples155, enumConstants156, baseType157, dataType161, enumeration159, baseType160, constraints164},
    generalizations={gen_rapidml_TypedMessage_RealizationContainer, gen_rapidml_TypedMessage_RESTElement, gen_rapidml_TypedMessage_WithExamples, gen_rapidml_ResourceDefinition_RESTElement, gen_rapidml_ResourceDefinition_WithExamples, gen_rapidml_ResourceDefinition_HasSecurityValue, gen_rapidml_Method_RESTElement, gen_rapidml_Method_HasSecurityValue, gen_rapidml_Method_Extensible, gen_rapidml_MediaType_RESTElement, gen_rapidml_Parameter_RESTElement, gen_rapidml_Parameter_Extensible, gen_rapidml_RESTElement_Documentable, gen_rapidml_RESTElement_Extensible, gen_rapidml_CollectionResource_ServiceDataResource, gen_rapidml_TypedRequest_TypedMessage, gen_rapidml_TypedResponse_TypedMessage, gen_rapidml_URIParameter_Parameter, gen_rapidml_MatrixParameter_URIParameter, gen_rapidml_TemplateParameter_URIParameter, gen_rapidml_ObjectResource_ServiceDataResource, gen_rapidml_CollectionParameter_Parameter, gen_rapidml_PropertyReference_SourceReference, gen_rapidml_MessageParameter_Parameter, gen_rapidml_ZenModel_Documentable, gen_rapidml_ZenModel_Extensible, gen_rapidml_ZenModel_HasTitle, gen_rapidml_ResourceAPI_RESTElement, gen_rapidml_ResourceAPI_HasSecurityValue, gen_rapidml_ResourceAPI_HasTitle, gen_rapidml_ServiceDataResource_RealizationContainer, gen_rapidml_ServiceDataResource_ResourceDefinition, gen_rapidml_ReferenceTreatment_Extensible, gen_rapidml_PrimitiveTypeSourceReference_SourceReference, gen_rapidml_ReferenceRealization_RealizationContainer, gen_rapidml_ReferenceLink_ReferenceTreatment, gen_rapidml_ReferenceEmbed_ReferenceTreatment, gen_rapidml_NamedLinkDescriptor_ObjectRealization, gen_rapidml_URI_HasStringValue, gen_rapidml_URISegment_HasStringValue, gen_rapidml_URISegmentWithParameter_URISegment, gen_rapidml_PropertyRealization_ConstrainableType, gen_rapidml_InlineExample_Example, gen_rapidml_LinkRelation_Documentable, gen_rapidml_ExternalExample_Example, gen_rapidml_ObjectRealization_Extensible, gen_rapidml_CollectionReferenceElement_ReferenceElement, gen_rapidml_SecurityScheme_Documentable, gen_rapidml_SecurityScheme_RESTElement, gen_rapidml_SecurityScope_Documentable, gen_rapidml_SecuritySchemeParameter_Documentable, gen_rapidml_SecuritySchemeLibrary_Documentable, gen_rapidml_RealizationContainer_Extensible, gen_rapidml_PrimitiveProperty_Feature, gen_rapidml_PrimitiveProperty_HasStringValue, gen_rapidml_PrimitiveProperty_ConstrainableType, gen_rapidml_Operation_Documentable, gen_rapidml_Feature_Documentable, gen_rapidml_Feature_Element, gen_rapidml_Feature_Extensible, gen_rapidml_ReferenceProperty_Feature, gen_rapidml_ReferenceProperty_ReferenceElement, gen_rapidml_DataModel_Documentable, gen_rapidml_DataModel_HasTitle, gen_rapidml_Structure_DataType, gen_rapidml_Structure_WithDataExamples, gen_rapidml_Structure_Inheritable, gen_rapidml_SimpleType_SingleValueType, gen_rapidml_EnumConstant_Documentable, gen_rapidml_InlineDataExample_DataExample, gen_rapidml_Constraint_Extensible, gen_rapidml_Enumeration_SingleValueType, gen_rapidml_ReferenceElement_Element, gen_rapidml_UserDefinedType_SimpleType, gen_rapidml_UserDefinedType_ConstrainableType, gen_rapidml_PrimitiveType_SimpleType, gen_rapidml_DataType_Documentable, gen_rapidml_DataType_Extensible, gen_rapidml_SingleValueType_DataType, gen_rapidml_LengthConstraint_Constraint, gen_rapidml_RegExConstraint_Constraint, gen_rapidml_ValueRangeConstraint_Constraint, gen_rapidml_ConstrainableType_Extensible},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)