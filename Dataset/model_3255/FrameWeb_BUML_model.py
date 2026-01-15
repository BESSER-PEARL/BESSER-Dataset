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
DateTimePrecision: Enumeration = Enumeration(
    name="DateTimePrecision",
    literals={
            EnumerationLiteral(name="timestamp"),
			EnumerationLiteral(name="time"),
			EnumerationLiteral(name="date")
    }
)

Generation: Enumeration = Enumeration(
    name="Generation",
    literals={
            EnumerationLiteral(name="auto"),
			EnumerationLiteral(name="identity"),
			EnumerationLiteral(name="sequence"),
			EnumerationLiteral(name="none"),
			EnumerationLiteral(name="table")
    }
)

Collection: Enumeration = Enumeration(
    name="Collection",
    literals={
            EnumerationLiteral(name="set"),
			EnumerationLiteral(name="bag"),
			EnumerationLiteral(name="list"),
			EnumerationLiteral(name="map")
    }
)

Order: Enumeration = Enumeration(
    name="Order",
    literals={
            EnumerationLiteral(name="natural"),
			EnumerationLiteral(name="columnNameAsc"),
			EnumerationLiteral(name="columnNameDesc")
    }
)

Cascade: Enumeration = Enumeration(
    name="Cascade",
    literals={
            EnumerationLiteral(name="remove"),
			EnumerationLiteral(name="merge"),
			EnumerationLiteral(name="refresh"),
			EnumerationLiteral(name="persist"),
			EnumerationLiteral(name="none"),
			EnumerationLiteral(name="all")
    }
)

Fetch: Enumeration = Enumeration(
    name="Fetch",
    literals={
            EnumerationLiteral(name="lazy"),
			EnumerationLiteral(name="eager")
    }
)

ConstantNameList: Enumeration = Enumeration(
    name="ConstantNameList",
    literals={
            EnumerationLiteral(name="DAO"),
			EnumerationLiteral(name="interface"),
			EnumerationLiteral(name="base"),
			EnumerationLiteral(name="class"),
			EnumerationLiteral(name="impl"),
			EnumerationLiteral(name="Controller"),
			EnumerationLiteral(name="Domain"),
			EnumerationLiteral(name="Persistence"),
			EnumerationLiteral(name="Application"),
			EnumerationLiteral(name="View")
    }
)

FrameworkCategoryList: Enumeration = Enumeration(
    name="FrameworkCategoryList",
    literals={
            EnumerationLiteral(name="FrontController"),
			EnumerationLiteral(name="DependencyInjection"),
			EnumerationLiteral(name="ObjetoRelacional")
    }
)

InheritanceMapping: Enumeration = Enumeration(
    name="InheritanceMapping",
    literals={
            EnumerationLiteral(name="singletable"),
			EnumerationLiteral(name="union"),
			EnumerationLiteral(name="join")
    }
)

FrameworkKindList: Enumeration = Enumeration(
    name="FrameworkKindList",
    literals={
            EnumerationLiteral(name="FrameworkSpecification"),
			EnumerationLiteral(name="FrameworkImplementation"),
			EnumerationLiteral(name="Custom"),
			EnumerationLiteral(name="StandardSpecification")
    }
)

# Classes
frameweb_FramewebProject = Class(name="frameweb::FramewebProject")
Profile = Class(name="Profile")
frameweb_EntityModel = Class(name="frameweb::EntityModel")
FramewebModel = Class(name="FramewebModel")
frameweb_NavigationModel = Class(name="frameweb::NavigationModel")
frameweb_ApplicationModel = Class(name="frameweb::ApplicationModel")
frameweb_PersistenceModel = Class(name="frameweb::PersistenceModel")
frameweb_DomainAssociation = Class(name="frameweb::DomainAssociation")
Association = Class(name="Association")
frameweb_FramewebModel = Class(name="frameweb::FramewebModel", is_abstract=True)
frameweb_FrameworkProfile = Class(name="frameweb::FrameworkProfile")
Model = Class(name="Model")
DomainAttribute = Class(name="DomainAttribute")
frameweb_IdAttribute = Class(name="frameweb::IdAttribute")
frameweb_LOBAttribute = Class(name="frameweb::LOBAttribute")
frameweb_EmbeddedAttribute = Class(name="frameweb::EmbeddedAttribute")
frameweb_DecimalAttribute = Class(name="frameweb::DecimalAttribute")
frameweb_DateTimeAttribute = Class(name="frameweb::DateTimeAttribute")
frameweb_DomainAttribute = Class(name="frameweb::DomainAttribute")
Property_ = Class(name="Property")
frameweb_VersionAttribute = Class(name="frameweb::VersionAttribute")
frameweb_Page = Class(name="frameweb::Page")
NavigationClass = Class(name="NavigationClass")
frameweb_TagLib = Class(name="frameweb::TagLib")
frameweb_Template = Class(name="frameweb::Template")
frameweb_DAOInterface = Class(name="frameweb::DAOInterface")
Interface = Class(name="Interface")
frameweb_DAOClass = Class(name="frameweb::DAOClass")
Class_ = Class(name="Class")
frameweb_DAORealization = Class(name="frameweb::DAORealization")
InterfaceRealization = Class(name="InterfaceRealization")
frameweb_FrontControllerClass = Class(name="frameweb::FrontControllerClass")
frameweb_IOParameter = Class(name="frameweb::IOParameter")
NavigationAttribute = Class(name="NavigationAttribute")
frameweb_Result = Class(name="frameweb::Result")
frameweb_FrontControllerMethod = Class(name="frameweb::FrontControllerMethod")
frameweb_ResultConstraint = Class(name="frameweb::ResultConstraint")
frameweb_NavigationAssociation = Class(name="frameweb::NavigationAssociation")
Operation = Class(name="Operation")
frameweb_ServiceClass = Class(name="frameweb::ServiceClass")
frameweb_ServiceInterface = Class(name="frameweb::ServiceInterface")
frameweb_ServiceGeneralization = Class(name="frameweb::ServiceGeneralization")
Generalization = Class(name="Generalization")
frameweb_ServiceControllerAssociation = Class(name="frameweb::ServiceControllerAssociation")
ServiceAssociation = Class(name="ServiceAssociation")
frameweb_DomainClass = Class(name="frameweb::DomainClass")
frameweb_UIComponentField = Class(name="frameweb::UIComponentField")
frameweb_ResultDependency = Class(name="frameweb::ResultDependency")
NavigationDependency = Class(name="NavigationDependency")
frameweb_MethodCosntraint = Class(name="frameweb::MethodCosntraint")
frameweb_PageDependency = Class(name="frameweb::PageDependency")
frameweb_PageConstraint = Class(name="frameweb::PageConstraint")
frameweb_ChainingDependency = Class(name="frameweb::ChainingDependency")
frameweb_ChainingConstraint = Class(name="frameweb::ChainingConstraint")
frameweb_DAOServiceAssociation = Class(name="frameweb::DAOServiceAssociation")
frameweb_NavigationAttribute = Class(name="frameweb::NavigationAttribute", is_abstract=True)
frameweb_NavigationClass = Class(name="frameweb::NavigationClass", is_abstract=True)
frameweb_DomainMethod = Class(name="frameweb::DomainMethod")
frameweb_FrontControllerDependency = Class(name="frameweb::FrontControllerDependency")
frameweb_PersistencePackage = Class(name="frameweb::PersistencePackage")
frameweb_ApplicationPackage = Class(name="frameweb::ApplicationPackage")
frameweb_UIComponent = Class(name="frameweb::UIComponent")
frameweb_ResultType = Class(name="frameweb::ResultType")
Stereotype = Class(name="Stereotype")
frameweb_NavigationPackage = Class(name="frameweb::NavigationPackage", is_abstract=True)
frameweb_DomainGeneralization = Class(name="frameweb::DomainGeneralization")
frameweb_Tag = Class(name="frameweb::Tag")
frameweb_NavigationCompositionPart = Class(name="frameweb::NavigationCompositionPart")
NavigationProperty = Class(name="NavigationProperty")
frameweb_NavigationCompositionWhole = Class(name="frameweb::NavigationCompositionWhole")
frameweb_NavigationProperty = Class(name="frameweb::NavigationProperty", is_abstract=True)
frameweb_ResultSet = Class(name="frameweb::ResultSet")
frameweb_NavigationConstraint = Class(name="frameweb::NavigationConstraint", is_abstract=True)
Constraint = Class(name="Constraint")
NavigationConstraint = Class(name="NavigationConstraint")
frameweb_NavigationGeneralization = Class(name="frameweb::NavigationGeneralization")
frameweb_DomainConstraints = Class(name="frameweb::DomainConstraints")
frameweb_DomainProperty = Class(name="frameweb::DomainProperty")
frameweb_DAOAttribute = Class(name="frameweb::DAOAttribute")
frameweb_ServiceMethod = Class(name="frameweb::ServiceMethod")
frameweb_ServiceAttribute = Class(name="frameweb::ServiceAttribute")
frameweb_ServiceAssociation = Class(name="frameweb::ServiceAssociation", is_abstract=True)
frameweb_NavigationDependency = Class(name="frameweb::NavigationDependency", is_abstract=True)
Dependency = Class(name="Dependency")
frameweb_DAOMethod = Class(name="frameweb::DAOMethod")
frameweb_DomainPackage = Class(name="frameweb::DomainPackage")
Package = Class(name="Package")
frameweb_ViewPackage = Class(name="frameweb::ViewPackage")
NavigationPackage = Class(name="NavigationPackage")
frameweb_ControllerPackage = Class(name="frameweb::ControllerPackage")
frameweb_ControllerExtension = Class(name="frameweb::ControllerExtension")
frameweb_Controller = Class(name="frameweb::Controller")
frameweb_ControllerSet = Class(name="frameweb::ControllerSet")
frameweb_ResultExtension = Class(name="frameweb::ResultExtension")
frameweb_ClassMappingExtension = Class(name="frameweb::ClassMappingExtension")
DomainExtension = Class(name="DomainExtension")
frameweb_AttributeMappingExtension = Class(name="frameweb::AttributeMappingExtension")
frameweb_ControllerExtensionEnd = Class(name="frameweb::ControllerExtensionEnd")
ExtensionEnd = Class(name="ExtensionEnd")
frameweb_TagExtensionEnd = Class(name="frameweb::TagExtensionEnd")
frameweb_ResultExtensionEnd = Class(name="frameweb::ResultExtensionEnd")
frameweb_ClassMappingExtensionEnd = Class(name="frameweb::ClassMappingExtensionEnd")
frameweb_AttributeMappingExtensionEnd = Class(name="frameweb::AttributeMappingExtensionEnd")
frameweb_ControllerProperty = Class(name="frameweb::ControllerProperty")
frameweb_TagProperty = Class(name="frameweb::TagProperty")
frameweb_DAOGeneralization = Class(name="frameweb::DAOGeneralization")
frameweb_MappingLib = Class(name="frameweb::MappingLib")
frameweb_ClassMapping = Class(name="frameweb::ClassMapping")
frameweb_AttributeMapping = Class(name="frameweb::AttributeMapping")
frameweb_DomainGeneralizationSet = Class(name="frameweb::DomainGeneralizationSet")
GeneralizationSet = Class(name="GeneralizationSet")
frameweb_FrameworkExtension = Class(name="frameweb::FrameworkExtension", is_abstract=True)
Extension = Class(name="Extension")
frameweb_TagExtension = Class(name="frameweb::TagExtension")
NavigationExtension = Class(name="NavigationExtension")
frameweb_SeviceRealization = Class(name="frameweb::SeviceRealization")
frameweb_FrameworkApplication = Class(name="frameweb::FrameworkApplication")
ProfileApplication = Class(name="ProfileApplication")
frameweb_NavigationExtension = Class(name="frameweb::NavigationExtension", is_abstract=True)
FrameworkExtension = Class(name="FrameworkExtension")
frameweb_DomainExtension = Class(name="frameweb::DomainExtension", is_abstract=True)
frameweb_NavigationGeneralizationSet = Class(name="frameweb::NavigationGeneralizationSet")
frameweb_DAOGeneralizationSet = Class(name="frameweb::DAOGeneralizationSet")
frameweb_ServiceGeneralizationSet = Class(name="frameweb::ServiceGeneralizationSet")
frameweb_SemanticPackage = Class(name="frameweb::SemanticPackage")
frameweb_IRI = Class(name="frameweb::IRI")
frameweb_ResultProperty = Class(name="frameweb::ResultProperty")
frameweb_ClassMappingPropery = Class(name="frameweb::ClassMappingPropery")
frameweb_AttributeMappingProperty = Class(name="frameweb::AttributeMappingProperty")
frameweb_Axiom = Class(name="frameweb::Axiom")
frameweb_Annotation = Class(name="frameweb::Annotation")
frameweb_VocabularyModel = Class(name="frameweb::VocabularyModel")
frameweb_Vocabulary = Class(name="frameweb::Vocabulary")
frameweb_VocabularyConstraints = Class(name="frameweb::VocabularyConstraints")
frameweb_Property = Class(name="frameweb::Property")
StructuralFeature = Class(name="StructuralFeature")
ConnectableElement = Class(name="ConnectableElement")
DeploymentTarget = Class(name="DeploymentTarget")
frameweb_DataType = Class(name="frameweb::DataType")
frameweb_Interface = Class(name="frameweb::Interface")
frameweb_Association = Class(name="frameweb::Association")
frameweb_Class = Class(name="frameweb::Class")
frameweb_ValueSpecification = Class(name="frameweb::ValueSpecification")
Classifier = Class(name="Classifier")
Relationship = Class(name="Relationship")
frameweb_Type = Class(name="frameweb::Type")
frameweb_Individual = Class(name="frameweb::Individual", is_abstract=True)
frameweb_VocabularyLiteral = Class(name="frameweb::VocabularyLiteral")
LiteralString = Class(name="LiteralString")
frameweb_VocabularyAssociation = Class(name="frameweb::VocabularyAssociation")
frameweb_VocabularyProperty = Class(name="frameweb::VocabularyProperty")
frameweb_VocabularyEntity = Class(name="frameweb::VocabularyEntity", is_abstract=True)
frameweb_ObjectProperty = Class(name="frameweb::ObjectProperty")
VocabularyEntity = Class(name="VocabularyEntity")
VocabularyAssociation = Class(name="VocabularyAssociation")
frameweb_DataProperty = Class(name="frameweb::DataProperty")
frameweb_AnnotationProperty = Class(name="frameweb::AnnotationProperty")
frameweb_VocabularyDataType = Class(name="frameweb::VocabularyDataType")
DataType = Class(name="DataType")
frameweb_NamedIndividual = Class(name="frameweb::NamedIndividual")
Individual = Class(name="Individual")
frameweb_VocabularyClassExpression = Class(name="frameweb::VocabularyClassExpression", is_abstract=True)
frameweb_VocabularyClass = Class(name="frameweb::VocabularyClass")
VocabularyClassExpression = Class(name="VocabularyClassExpression")
frameweb_AnonymousIndividual = Class(name="frameweb::AnonymousIndividual")

# frameweb_FramewebProject class attributes and methods

# Profile class attributes and methods

# frameweb_EntityModel class attributes and methods

# FramewebModel class attributes and methods

# frameweb_NavigationModel class attributes and methods

# frameweb_ApplicationModel class attributes and methods

# frameweb_PersistenceModel class attributes and methods

# frameweb_DomainAssociation class attributes and methods
frameweb_DomainAssociation_collection: Property = Property(name="collection", type=StringType)
frameweb_DomainAssociation_cascade: Property = Property(name="cascade", type=StringType)
frameweb_DomainAssociation_fetch: Property = Property(name="fetch", type=StringType)
frameweb_DomainAssociation_order: Property = Property(name="order", type=StringType)
frameweb_DomainAssociation.attributes={frameweb_DomainAssociation_fetch, frameweb_DomainAssociation_cascade, frameweb_DomainAssociation_order, frameweb_DomainAssociation_collection}

# Association class attributes and methods

# frameweb_FramewebModel class attributes and methods

# frameweb_FrameworkProfile class attributes and methods
frameweb_FrameworkProfile_category: Property = Property(name="category", type=StringType)
frameweb_FrameworkProfile_kind: Property = Property(name="kind", type=StringType)
frameweb_FrameworkProfile.attributes={frameweb_FrameworkProfile_kind, frameweb_FrameworkProfile_category}

# Model class attributes and methods

# DomainAttribute class attributes and methods

# frameweb_IdAttribute class attributes and methods
frameweb_IdAttribute_generation: Property = Property(name="generation", type=StringType)
frameweb_IdAttribute.attributes={frameweb_IdAttribute_generation}

# frameweb_LOBAttribute class attributes and methods

# frameweb_EmbeddedAttribute class attributes and methods

# frameweb_DecimalAttribute class attributes and methods
frameweb_DecimalAttribute_decimalPrecision: Property = Property(name="decimalPrecision", type=StringType)
frameweb_DecimalAttribute_decimalScale: Property = Property(name="decimalScale", type=StringType)
frameweb_DecimalAttribute.attributes={frameweb_DecimalAttribute_decimalScale, frameweb_DecimalAttribute_decimalPrecision}

# frameweb_DateTimeAttribute class attributes and methods
frameweb_DateTimeAttribute_dateTimePrecision: Property = Property(name="dateTimePrecision", type=StringType)
frameweb_DateTimeAttribute.attributes={frameweb_DateTimeAttribute_dateTimePrecision}

# frameweb_DomainAttribute class attributes and methods
frameweb_DomainAttribute_size: Property = Property(name="size", type=StringType)
frameweb_DomainAttribute_isNull: Property = Property(name="isNull", type=BooleanType)
frameweb_DomainAttribute_isPersistent: Property = Property(name="isPersistent", type=BooleanType)
frameweb_DomainAttribute.attributes={frameweb_DomainAttribute_isPersistent, frameweb_DomainAttribute_isNull, frameweb_DomainAttribute_size}

# Property class attributes and methods

# frameweb_VersionAttribute class attributes and methods

# frameweb_Page class attributes and methods

# NavigationClass class attributes and methods

# frameweb_TagLib class attributes and methods
frameweb_TagLib_prefix: Property = Property(name="prefix", type=StringType)
frameweb_TagLib.attributes={frameweb_TagLib_prefix}

# frameweb_Template class attributes and methods

# frameweb_DAOInterface class attributes and methods
frameweb_DAOInterface_infix: Property = Property(name="infix", type=StringType)
frameweb_DAOInterface_sufix: Property = Property(name="sufix", type=StringType)
frameweb_DAOInterface.attributes={frameweb_DAOInterface_sufix, frameweb_DAOInterface_infix}

# Interface class attributes and methods

# frameweb_DAOClass class attributes and methods
frameweb_DAOClass_sufix: Property = Property(name="sufix", type=StringType)
frameweb_DAOClass_infix: Property = Property(name="infix", type=StringType)
frameweb_DAOClass_prefix: Property = Property(name="prefix", type=StringType)
frameweb_DAOClass.attributes={frameweb_DAOClass_prefix, frameweb_DAOClass_sufix, frameweb_DAOClass_infix}

# Class class attributes and methods

# frameweb_DAORealization class attributes and methods

# InterfaceRealization class attributes and methods

# frameweb_FrontControllerClass class attributes and methods

# frameweb_IOParameter class attributes and methods

# NavigationAttribute class attributes and methods

# frameweb_Result class attributes and methods

# frameweb_FrontControllerMethod class attributes and methods
frameweb_FrontControllerMethod_isDefault: Property = Property(name="isDefault", type=BooleanType)
frameweb_FrontControllerMethod.attributes={frameweb_FrontControllerMethod_isDefault}

# frameweb_ResultConstraint class attributes and methods

# frameweb_NavigationAssociation class attributes and methods

# Operation class attributes and methods

# frameweb_ServiceClass class attributes and methods

# frameweb_ServiceInterface class attributes and methods

# frameweb_ServiceGeneralization class attributes and methods

# Generalization class attributes and methods

# frameweb_ServiceControllerAssociation class attributes and methods

# ServiceAssociation class attributes and methods

# frameweb_DomainClass class attributes and methods
frameweb_DomainClass_table: Property = Property(name="table", type=StringType)
frameweb_DomainClass.attributes={frameweb_DomainClass_table}

# frameweb_UIComponentField class attributes and methods

# frameweb_ResultDependency class attributes and methods
frameweb_ResultDependency_render: Property = Property(name="render", type=StringType)
frameweb_ResultDependency_execute: Property = Property(name="execute", type=StringType)
frameweb_ResultDependency_ajax: Property = Property(name="ajax", type=BooleanType)
frameweb_ResultDependency.attributes={frameweb_ResultDependency_render, frameweb_ResultDependency_ajax, frameweb_ResultDependency_execute}

# NavigationDependency class attributes and methods

# frameweb_MethodCosntraint class attributes and methods

# frameweb_PageDependency class attributes and methods

# frameweb_PageConstraint class attributes and methods

# frameweb_ChainingDependency class attributes and methods

# frameweb_ChainingConstraint class attributes and methods

# frameweb_DAOServiceAssociation class attributes and methods

# frameweb_NavigationAttribute class attributes and methods

# frameweb_NavigationClass class attributes and methods

# frameweb_DomainMethod class attributes and methods

# frameweb_FrontControllerDependency class attributes and methods

# frameweb_PersistencePackage class attributes and methods

# frameweb_ApplicationPackage class attributes and methods

# frameweb_UIComponent class attributes and methods

# frameweb_ResultType class attributes and methods

# Stereotype class attributes and methods

# frameweb_NavigationPackage class attributes and methods

# frameweb_DomainGeneralization class attributes and methods

# frameweb_Tag class attributes and methods

# frameweb_NavigationCompositionPart class attributes and methods

# NavigationProperty class attributes and methods

# frameweb_NavigationCompositionWhole class attributes and methods

# frameweb_NavigationProperty class attributes and methods

# frameweb_ResultSet class attributes and methods

# frameweb_NavigationConstraint class attributes and methods

# Constraint class attributes and methods

# NavigationConstraint class attributes and methods

# frameweb_NavigationGeneralization class attributes and methods

# frameweb_DomainConstraints class attributes and methods

# frameweb_DomainProperty class attributes and methods

# frameweb_DAOAttribute class attributes and methods

# frameweb_ServiceMethod class attributes and methods

# frameweb_ServiceAttribute class attributes and methods

# frameweb_ServiceAssociation class attributes and methods

# frameweb_NavigationDependency class attributes and methods

# Dependency class attributes and methods

# frameweb_DAOMethod class attributes and methods

# frameweb_DomainPackage class attributes and methods

# Package class attributes and methods

# frameweb_ViewPackage class attributes and methods

# NavigationPackage class attributes and methods

# frameweb_ControllerPackage class attributes and methods

# frameweb_ControllerExtension class attributes and methods

# frameweb_Controller class attributes and methods

# frameweb_ControllerSet class attributes and methods

# frameweb_ResultExtension class attributes and methods

# frameweb_ClassMappingExtension class attributes and methods

# DomainExtension class attributes and methods

# frameweb_AttributeMappingExtension class attributes and methods

# frameweb_ControllerExtensionEnd class attributes and methods

# ExtensionEnd class attributes and methods

# frameweb_TagExtensionEnd class attributes and methods

# frameweb_ResultExtensionEnd class attributes and methods

# frameweb_ClassMappingExtensionEnd class attributes and methods

# frameweb_AttributeMappingExtensionEnd class attributes and methods

# frameweb_ControllerProperty class attributes and methods

# frameweb_TagProperty class attributes and methods

# frameweb_DAOGeneralization class attributes and methods

# frameweb_MappingLib class attributes and methods

# frameweb_ClassMapping class attributes and methods

# frameweb_AttributeMapping class attributes and methods

# frameweb_DomainGeneralizationSet class attributes and methods
frameweb_DomainGeneralizationSet_mapping: Property = Property(name="mapping", type=StringType)
frameweb_DomainGeneralizationSet.attributes={frameweb_DomainGeneralizationSet_mapping}

# GeneralizationSet class attributes and methods

# frameweb_FrameworkExtension class attributes and methods

# Extension class attributes and methods

# frameweb_TagExtension class attributes and methods

# NavigationExtension class attributes and methods

# frameweb_SeviceRealization class attributes and methods

# frameweb_FrameworkApplication class attributes and methods

# ProfileApplication class attributes and methods

# frameweb_NavigationExtension class attributes and methods

# FrameworkExtension class attributes and methods

# frameweb_DomainExtension class attributes and methods

# frameweb_NavigationGeneralizationSet class attributes and methods

# frameweb_DAOGeneralizationSet class attributes and methods

# frameweb_ServiceGeneralizationSet class attributes and methods

# frameweb_SemanticPackage class attributes and methods

# frameweb_IRI class attributes and methods
frameweb_IRI_iri: Property = Property(name="iri", type=StringType)
frameweb_IRI_iriVersion: Property = Property(name="iriVersion", type=StringType)
frameweb_IRI.attributes={frameweb_IRI_iriVersion, frameweb_IRI_iri}

# frameweb_ResultProperty class attributes and methods

# frameweb_ClassMappingPropery class attributes and methods

# frameweb_AttributeMappingProperty class attributes and methods

# frameweb_Axiom class attributes and methods

# frameweb_Annotation class attributes and methods

# frameweb_VocabularyModel class attributes and methods

# frameweb_Vocabulary class attributes and methods
frameweb_Vocabulary_vocabularyDocument: Property = Property(name="vocabularyDocument", type=StringType)
frameweb_Vocabulary.attributes={frameweb_Vocabulary_vocabularyDocument}

# frameweb_VocabularyConstraints class attributes and methods

# frameweb_Property class attributes and methods
frameweb_Property_isID: Property = Property(name="isID", type=StringType)
frameweb_Property_default: Property = Property(name="default", type=StringType)
frameweb_Property_aggregation: Property = Property(name="aggregation", type=StringType)
frameweb_Property_isComposite: Property = Property(name="isComposite", type=StringType)
frameweb_Property_isDerived: Property = Property(name="isDerived", type=StringType)
frameweb_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=StringType)
frameweb_Property_m_subsetting_context_conforms: Method = Method(name="subsetting_context_conforms", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
frameweb_Property_m_derived_union_is_read_only: Method = Method(name="derived_union_is_read_only", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
frameweb_Property_m_multiplicity_of_composite: Method = Method(name="multiplicity_of_composite", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
frameweb_Property_m_subsetting_rules: Method = Method(name="subsetting_rules", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
frameweb_Property_m_binding_to_attribute: Method = Method(name="binding_to_attribute", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
frameweb_Property_m_redefined_property_inherited: Method = Method(name="redefined_property_inherited", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
frameweb_Property_m_derived_union_is_derived: Method = Method(name="derived_union_is_derived", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
frameweb_Property_m_deployment_target: Method = Method(name="deployment_target", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
frameweb_Property_m_subsetted_property_names: Method = Method(name="subsetted_property_names", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
frameweb_Property_m_getDefault: Method = Method(name="getDefault", parameters={}, type=StringType)
frameweb_Property_m_getOtherEnd: Method = Method(name="getOtherEnd", parameters={}, type=Property_)
frameweb_Property_m_isSetDefault: Method = Method(name="isSetDefault", parameters={}, type=StringType)
frameweb_Property_m_setBooleanDefaultValue: Method = Method(name="setBooleanDefaultValue", parameters={Parameter(name='value')})
frameweb_Property_m_setDefault: Method = Method(name="setDefault", parameters={Parameter(name='newDefault')})
frameweb_Property_m_setIntegerDefaultValue: Method = Method(name="setIntegerDefaultValue", parameters={Parameter(name='value')})
frameweb_Property_m_setIsComposite: Method = Method(name="setIsComposite", parameters={Parameter(name='newIsComposite')})
frameweb_Property_m_setIsNavigable: Method = Method(name="setIsNavigable", parameters={Parameter(name='isNavigable')})
frameweb_Property_m_setNullDefaultValue: Method = Method(name="setNullDefaultValue", parameters={})
frameweb_Property_m_setOpposite: Method = Method(name="setOpposite", parameters={Parameter(name='newOpposite')})
frameweb_Property_m_type_of_opposite_end: Method = Method(name="type_of_opposite_end", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
frameweb_Property_m_qualified_is_association_end: Method = Method(name="qualified_is_association_end", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
frameweb_Property_m_setUnlimitedNaturalDefaultValue: Method = Method(name="setUnlimitedNaturalDefaultValue", parameters={Parameter(name='value')})
frameweb_Property_m_unsetDefault: Method = Method(name="unsetDefault", parameters={})
frameweb_Property_m_isAttribute: Method = Method(name="isAttribute", parameters={}, type=StringType)
frameweb_Property_m_isComposite: Method = Method(name="isComposite", parameters={}, type=StringType)
frameweb_Property_m_isNavigable: Method = Method(name="isNavigable", parameters={}, type=StringType)
frameweb_Property_m_getOpposite: Method = Method(name="getOpposite", parameters={}, type=Property_)
frameweb_Property_m_subsettingContext: Method = Method(name="subsettingContext", parameters={}, type=StringType)
frameweb_Property_m_setRealDefaultValue: Method = Method(name="setRealDefaultValue", parameters={Parameter(name='value')})
frameweb_Property_m_setStringDefaultValue: Method = Method(name="setStringDefaultValue", parameters={Parameter(name='value')})
frameweb_Property.attributes={frameweb_Property_isComposite, frameweb_Property_aggregation, frameweb_Property_isDerived, frameweb_Property_isDerivedUnion, frameweb_Property_default, frameweb_Property_isID}
frameweb_Property.methods={frameweb_Property_m_derived_union_is_derived, frameweb_Property_m_subsetting_context_conforms, frameweb_Property_m_redefined_property_inherited, frameweb_Property_m_isSetDefault, frameweb_Property_m_qualified_is_association_end, frameweb_Property_m_setIntegerDefaultValue, frameweb_Property_m_subsetting_rules, frameweb_Property_m_setNullDefaultValue, frameweb_Property_m_setDefault, frameweb_Property_m_getOpposite, frameweb_Property_m_deployment_target, frameweb_Property_m_getDefault, frameweb_Property_m_binding_to_attribute, frameweb_Property_m_setOpposite, frameweb_Property_m_setIsComposite, frameweb_Property_m_isAttribute, frameweb_Property_m_getOtherEnd, frameweb_Property_m_setRealDefaultValue, frameweb_Property_m_subsettingContext, frameweb_Property_m_type_of_opposite_end, frameweb_Property_m_isComposite, frameweb_Property_m_isNavigable, frameweb_Property_m_derived_union_is_read_only, frameweb_Property_m_setStringDefaultValue, frameweb_Property_m_setBooleanDefaultValue, frameweb_Property_m_setIsNavigable, frameweb_Property_m_unsetDefault, frameweb_Property_m_setUnlimitedNaturalDefaultValue, frameweb_Property_m_multiplicity_of_composite, frameweb_Property_m_subsetted_property_names}

# StructuralFeature class attributes and methods

# ConnectableElement class attributes and methods

# DeploymentTarget class attributes and methods

# frameweb_DataType class attributes and methods

# frameweb_Interface class attributes and methods

# frameweb_Association class attributes and methods
frameweb_Association_isDerived: Property = Property(name="isDerived", type=StringType)
frameweb_Association_m_association_ends: Method = Method(name="association_ends", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
frameweb_Association_m_ends_must_be_typed: Method = Method(name="ends_must_be_typed", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
frameweb_Association_m_isBinary: Method = Method(name="isBinary", parameters={}, type=StringType)
frameweb_Association_m_getEndTypes: Method = Method(name="getEndTypes", parameters={}, type=StringType)
frameweb_Association_m_specialized_end_number: Method = Method(name="specialized_end_number", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
frameweb_Association_m_specialized_end_types: Method = Method(name="specialized_end_types", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
frameweb_Association_m_binary_associations: Method = Method(name="binary_associations", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
frameweb_Association.attributes={frameweb_Association_isDerived}
frameweb_Association.methods={frameweb_Association_m_association_ends, frameweb_Association_m_getEndTypes, frameweb_Association_m_ends_must_be_typed, frameweb_Association_m_isBinary, frameweb_Association_m_specialized_end_types, frameweb_Association_m_binary_associations, frameweb_Association_m_specialized_end_number}

# frameweb_Class class attributes and methods

# frameweb_ValueSpecification class attributes and methods

# Classifier class attributes and methods

# Relationship class attributes and methods

# frameweb_Type class attributes and methods

# frameweb_Individual class attributes and methods

# frameweb_VocabularyLiteral class attributes and methods

# LiteralString class attributes and methods

# frameweb_VocabularyAssociation class attributes and methods

# frameweb_VocabularyProperty class attributes and methods

# frameweb_VocabularyEntity class attributes and methods

# frameweb_ObjectProperty class attributes and methods

# VocabularyEntity class attributes and methods

# VocabularyAssociation class attributes and methods

# frameweb_DataProperty class attributes and methods

# frameweb_AnnotationProperty class attributes and methods

# frameweb_VocabularyDataType class attributes and methods

# DataType class attributes and methods

# frameweb_NamedIndividual class attributes and methods

# Individual class attributes and methods

# frameweb_VocabularyClassExpression class attributes and methods

# frameweb_VocabularyClass class attributes and methods

# VocabularyClassExpression class attributes and methods

# frameweb_AnonymousIndividual class attributes and methods

# Relationships
compose0: BinaryAssociation = BinaryAssociation(
    name="compose0",
    ends={
        Property(name="frameweb_FramewebModel", type=frameweb_FramewebProject, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_FramewebProject", type=frameweb_FramewebModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configures1: BinaryAssociation = BinaryAssociation(
    name="configures1",
    ends={
        Property(name="frameweb_FrameworkProfile", type=frameweb_FramewebProject, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_FramewebProject2", type=frameweb_FrameworkProfile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pageTagLib3: BinaryAssociation = BinaryAssociation(
    name="pageTagLib3",
    ends={
        Property(name="frameweb_TagLib", type=frameweb_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_Page", type=frameweb_TagLib, multiplicity=Multiplicity(0, 9999))
    }
)
templateTagLib4: BinaryAssociation = BinaryAssociation(
    name="templateTagLib4",
    ends={
        Property(name="frameweb_TagLib5", type=frameweb_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_Template", type=frameweb_TagLib, multiplicity=Multiplicity(0, 9999))
    }
)
resultResult7: BinaryAssociation = BinaryAssociation(
    name="resultResult7",
    ends={
        Property(name="frameweb_Result", type=frameweb_ResultDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_ResultDependency", type=frameweb_Result, multiplicity=Multiplicity(0, 9999))
    }
)
resultMethod8: BinaryAssociation = BinaryAssociation(
    name="resultMethod8",
    ends={
        Property(name="frameweb_FrontControllerMethod", type=frameweb_ResultDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_ResultDependency9", type=frameweb_FrontControllerMethod, multiplicity=Multiplicity(0, 1))
    }
)
resultDependendencyCosntraint10: BinaryAssociation = BinaryAssociation(
    name="resultDependendencyCosntraint10",
    ends={
        Property(name="frameweb_ResultConstraint", type=frameweb_ResultDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_ResultDependency11", type=frameweb_ResultConstraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
display6: BinaryAssociation = BinaryAssociation(
    name="display6",
    ends={
        Property(name="UIComponentField", type=frameweb_IOParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="inject", type=frameweb_UIComponentField, multiplicity=Multiplicity(0, 9999))
    }
)
methodDependendencyConstraint14: BinaryAssociation = BinaryAssociation(
    name="methodDependendencyConstraint14",
    ends={
        Property(name="frameweb_MethodCosntraint", type=frameweb_FrontControllerDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_FrontControllerDependency15", type=frameweb_MethodCosntraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pageDependencyCosntraint16: BinaryAssociation = BinaryAssociation(
    name="pageDependencyCosntraint16",
    ends={
        Property(name="frameweb_PageConstraint", type=frameweb_PageDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_PageDependency", type=frameweb_PageConstraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outMethod17: BinaryAssociation = BinaryAssociation(
    name="outMethod17",
    ends={
        Property(name="frameweb_FrontControllerMethod18", type=frameweb_ChainingDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_ChainingDependency", type=frameweb_FrontControllerMethod, multiplicity=Multiplicity(0, 1))
    }
)
inMethod19: BinaryAssociation = BinaryAssociation(
    name="inMethod19",
    ends={
        Property(name="frameweb_FrontControllerMethod21", type=frameweb_ChainingDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_ChainingDependency20", type=frameweb_FrontControllerMethod, multiplicity=Multiplicity(0, 1))
    }
)
chainingDependendencyConstraint22: BinaryAssociation = BinaryAssociation(
    name="chainingDependendencyConstraint22",
    ends={
        Property(name="frameweb_ChainingConstraint", type=frameweb_ChainingDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_ChainingDependency23", type=frameweb_ChainingConstraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
method12: BinaryAssociation = BinaryAssociation(
    name="method12",
    ends={
        Property(name="frameweb_FrontControllerMethod13", type=frameweb_FrontControllerDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_FrontControllerDependency", type=frameweb_FrontControllerMethod, multiplicity=Multiplicity(0, 1))
    }
)
inject24: BinaryAssociation = BinaryAssociation(
    name="inject24",
    ends={
        Property(name="IOParameter", type=frameweb_UIComponentField, multiplicity=Multiplicity(1, 1)),
        Property(name="display", type=frameweb_IOParameter, multiplicity=Multiplicity(0, 1))
    }
)
directlyImportsDocuments25: BinaryAssociation = BinaryAssociation(
    name="directlyImportsDocuments25",
    ends={
        Property(name="frameweb_IRI", type=frameweb_Vocabulary, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_Vocabulary", type=frameweb_IRI, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vocabularyIRI26: BinaryAssociation = BinaryAssociation(
    name="vocabularyIRI26",
    ends={
        Property(name="frameweb_IRI28", type=frameweb_Vocabulary, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_Vocabulary27", type=frameweb_IRI, multiplicity=Multiplicity(1, 1))
    }
)
axioms29: BinaryAssociation = BinaryAssociation(
    name="axioms29",
    ends={
        Property(name="frameweb_Axiom", type=frameweb_Vocabulary, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_Vocabulary30", type=frameweb_Axiom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations31: BinaryAssociation = BinaryAssociation(
    name="annotations31",
    ends={
        Property(name="frameweb_Annotation", type=frameweb_Vocabulary, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_Vocabulary32", type=frameweb_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype33: BinaryAssociation = BinaryAssociation(
    name="datatype33",
    ends={
        Property(name="frameweb_DataType", type=frameweb_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_Property", type=frameweb_DataType, multiplicity=Multiplicity(0, 1))
    }
)
interface34: BinaryAssociation = BinaryAssociation(
    name="interface34",
    ends={
        Property(name="frameweb_Interface", type=frameweb_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_Property35", type=frameweb_Interface, multiplicity=Multiplicity(0, 1))
    }
)
associationEnd37: BinaryAssociation = BinaryAssociation(
    name="associationEnd37",
    ends={
        Property(name="Property", type=frameweb_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifier", type=frameweb_Property, multiplicity=Multiplicity(0, 1))
    }
)
qualifier39: BinaryAssociation = BinaryAssociation(
    name="qualifier39",
    ends={
        Property(name="Property40", type=frameweb_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnd", type=frameweb_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opposite46: BinaryAssociation = BinaryAssociation(
    name="opposite46",
    ends={
        Property(name="frameweb_Property47", type=frameweb_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_Property45", type=frameweb_Property, multiplicity=Multiplicity(0, 1))
    }
)
owningAssociation48: BinaryAssociation = BinaryAssociation(
    name="owningAssociation48",
    ends={
        Property(name="Association", type=frameweb_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=frameweb_Association, multiplicity=Multiplicity(0, 1))
    }
)
redefinedProperty50: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty50",
    ends={
        Property(name="frameweb_Property51", type=frameweb_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_Property49", type=frameweb_Property, multiplicity=Multiplicity(0, 9999))
    }
)
subsettedProperty53: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty53",
    ends={
        Property(name="frameweb_Property54", type=frameweb_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_Property52", type=frameweb_Property, multiplicity=Multiplicity(0, 9999))
    }
)
association55: BinaryAssociation = BinaryAssociation(
    name="association55",
    ends={
        Property(name="Association56", type=frameweb_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=frameweb_Association, multiplicity=Multiplicity(0, 1))
    }
)
class41: BinaryAssociation = BinaryAssociation(
    name="class41",
    ends={
        Property(name="frameweb_Class", type=frameweb_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_Property42", type=frameweb_Class, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue43: BinaryAssociation = BinaryAssociation(
    name="defaultValue43",
    ends={
        Property(name="frameweb_ValueSpecification", type=frameweb_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_Property44", type=frameweb_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberEnd58: BinaryAssociation = BinaryAssociation(
    name="memberEnd58",
    ends={
        Property(name="Property59", type=frameweb_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=frameweb_Property, multiplicity=Multiplicity(2, 9999))
    }
)
ownedEnd60: BinaryAssociation = BinaryAssociation(
    name="ownedEnd60",
    ends={
        Property(name="Property61", type=frameweb_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=frameweb_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
navigableOwnedEnd62: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd62",
    ends={
        Property(name="frameweb_Property64", type=frameweb_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_Association63", type=frameweb_Property, multiplicity=Multiplicity(0, 9999))
    }
)
endType57: BinaryAssociation = BinaryAssociation(
    name="endType57",
    ends={
        Property(name="frameweb_Type", type=frameweb_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_Association", type=frameweb_Type, multiplicity=Multiplicity(1, 9999))
    }
)
entityIRI65: BinaryAssociation = BinaryAssociation(
    name="entityIRI65",
    ends={
        Property(name="frameweb_IRI66", type=frameweb_VocabularyEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_VocabularyEntity", type=frameweb_IRI, multiplicity=Multiplicity(1, 1))
    }
)
vocabularyproperty67: BinaryAssociation = BinaryAssociation(
    name="vocabularyproperty67",
    ends={
        Property(name="frameweb_VocabularyProperty", type=frameweb_VocabularyClass, multiplicity=Multiplicity(1, 1)),
        Property(name="frameweb_VocabularyClass", type=frameweb_VocabularyProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_frameweb_FrameworkProfile_Profile = Generalization(general=Profile, specific=frameweb_FrameworkProfile)
gen_frameweb_EntityModel_FramewebModel = Generalization(general=FramewebModel, specific=frameweb_EntityModel)
gen_frameweb_NavigationModel_FramewebModel = Generalization(general=FramewebModel, specific=frameweb_NavigationModel)
gen_frameweb_ApplicationModel_FramewebModel = Generalization(general=FramewebModel, specific=frameweb_ApplicationModel)
gen_frameweb_PersistenceModel_FramewebModel = Generalization(general=FramewebModel, specific=frameweb_PersistenceModel)
gen_frameweb_DomainAssociation_Association = Generalization(general=Association, specific=frameweb_DomainAssociation)
gen_frameweb_FramewebModel_Model = Generalization(general=Model, specific=frameweb_FramewebModel)
gen_frameweb_VersionAttribute_DomainAttribute = Generalization(general=DomainAttribute, specific=frameweb_VersionAttribute)
gen_frameweb_IdAttribute_DomainAttribute = Generalization(general=DomainAttribute, specific=frameweb_IdAttribute)
gen_frameweb_LOBAttribute_DomainAttribute = Generalization(general=DomainAttribute, specific=frameweb_LOBAttribute)
gen_frameweb_EmbeddedAttribute_DomainAttribute = Generalization(general=DomainAttribute, specific=frameweb_EmbeddedAttribute)
gen_frameweb_DecimalAttribute_DomainAttribute = Generalization(general=DomainAttribute, specific=frameweb_DecimalAttribute)
gen_frameweb_DateTimeAttribute_DomainAttribute = Generalization(general=DomainAttribute, specific=frameweb_DateTimeAttribute)
gen_frameweb_DomainAttribute_Property = Generalization(general=Property_, specific=frameweb_DomainAttribute)
gen_frameweb_Page_NavigationClass = Generalization(general=NavigationClass, specific=frameweb_Page)
gen_frameweb_Template_NavigationClass = Generalization(general=NavigationClass, specific=frameweb_Template)
gen_frameweb_DAOInterface_Interface = Generalization(general=Interface, specific=frameweb_DAOInterface)
gen_frameweb_DAOClass_Class = Generalization(general=Class_, specific=frameweb_DAOClass)
gen_frameweb_DAORealization_InterfaceRealization = Generalization(general=InterfaceRealization, specific=frameweb_DAORealization)
gen_frameweb_FrontControllerClass_Class = Generalization(general=Class_, specific=frameweb_FrontControllerClass)
gen_frameweb_IOParameter_NavigationAttribute = Generalization(general=NavigationAttribute, specific=frameweb_IOParameter)
gen_frameweb_NavigationAssociation_Association = Generalization(general=Association, specific=frameweb_NavigationAssociation)
gen_frameweb_FrontControllerMethod_Operation = Generalization(general=Operation, specific=frameweb_FrontControllerMethod)
gen_frameweb_ServiceClass_Class = Generalization(general=Class_, specific=frameweb_ServiceClass)
gen_frameweb_ServiceInterface_Interface = Generalization(general=Interface, specific=frameweb_ServiceInterface)
gen_frameweb_ServiceGeneralization_Generalization = Generalization(general=Generalization, specific=frameweb_ServiceGeneralization)
gen_frameweb_ServiceControllerAssociation_ServiceAssociation = Generalization(general=ServiceAssociation, specific=frameweb_ServiceControllerAssociation)
gen_frameweb_DomainClass_Class = Generalization(general=Class_, specific=frameweb_DomainClass)
gen_frameweb_ResultDependency_NavigationDependency = Generalization(general=NavigationDependency, specific=frameweb_ResultDependency)
gen_frameweb_PageDependency_NavigationDependency = Generalization(general=NavigationDependency, specific=frameweb_PageDependency)
gen_frameweb_ChainingDependency_NavigationDependency = Generalization(general=NavigationDependency, specific=frameweb_ChainingDependency)
gen_frameweb_DAOServiceAssociation_ServiceAssociation = Generalization(general=ServiceAssociation, specific=frameweb_DAOServiceAssociation)
gen_frameweb_NavigationAttribute_Property = Generalization(general=Property_, specific=frameweb_NavigationAttribute)
gen_frameweb_NavigationClass_Class = Generalization(general=Class_, specific=frameweb_NavigationClass)
gen_frameweb_DomainMethod_Operation = Generalization(general=Operation, specific=frameweb_DomainMethod)
gen_frameweb_Result_Class = Generalization(general=Class_, specific=frameweb_Result)
gen_frameweb_FrontControllerDependency_NavigationDependency = Generalization(general=NavigationDependency, specific=frameweb_FrontControllerDependency)
gen_frameweb_PersistencePackage_Package = Generalization(general=Package, specific=frameweb_PersistencePackage)
gen_frameweb_ApplicationPackage_Package = Generalization(general=Package, specific=frameweb_ApplicationPackage)
gen_frameweb_UIComponent_NavigationClass = Generalization(general=NavigationClass, specific=frameweb_UIComponent)
gen_frameweb_ResultType_Stereotype = Generalization(general=Stereotype, specific=frameweb_ResultType)
gen_frameweb_NavigationPackage_Package = Generalization(general=Package, specific=frameweb_NavigationPackage)
gen_frameweb_DomainGeneralization_Generalization = Generalization(general=Generalization, specific=frameweb_DomainGeneralization)
gen_frameweb_UIComponentField_NavigationAttribute = Generalization(general=NavigationAttribute, specific=frameweb_UIComponentField)
gen_frameweb_TagLib_Package = Generalization(general=Package, specific=frameweb_TagLib)
gen_frameweb_Tag_Stereotype = Generalization(general=Stereotype, specific=frameweb_Tag)
gen_frameweb_NavigationCompositionPart_NavigationProperty = Generalization(general=NavigationProperty, specific=frameweb_NavigationCompositionPart)
gen_frameweb_NavigationCompositionWhole_NavigationProperty = Generalization(general=NavigationProperty, specific=frameweb_NavigationCompositionWhole)
gen_frameweb_NavigationProperty_Property = Generalization(general=Property_, specific=frameweb_NavigationProperty)
gen_frameweb_ResultSet_Package = Generalization(general=Package, specific=frameweb_ResultSet)
gen_frameweb_NavigationConstraint_Constraint = Generalization(general=Constraint, specific=frameweb_NavigationConstraint)
gen_frameweb_PageConstraint_NavigationConstraint = Generalization(general=NavigationConstraint, specific=frameweb_PageConstraint)
gen_frameweb_ResultConstraint_NavigationConstraint = Generalization(general=NavigationConstraint, specific=frameweb_ResultConstraint)
gen_frameweb_MethodCosntraint_NavigationConstraint = Generalization(general=NavigationConstraint, specific=frameweb_MethodCosntraint)
gen_frameweb_ChainingConstraint_NavigationConstraint = Generalization(general=NavigationConstraint, specific=frameweb_ChainingConstraint)
gen_frameweb_NavigationGeneralization_Generalization = Generalization(general=Generalization, specific=frameweb_NavigationGeneralization)
gen_frameweb_DomainConstraints_Constraint = Generalization(general=Constraint, specific=frameweb_DomainConstraints)
gen_frameweb_DomainProperty_Property = Generalization(general=Property_, specific=frameweb_DomainProperty)
gen_frameweb_DAOAttribute_Property = Generalization(general=Property_, specific=frameweb_DAOAttribute)
gen_frameweb_ServiceMethod_Operation = Generalization(general=Operation, specific=frameweb_ServiceMethod)
gen_frameweb_ServiceAttribute_Property = Generalization(general=Property_, specific=frameweb_ServiceAttribute)
gen_frameweb_ServiceAssociation_Association = Generalization(general=Association, specific=frameweb_ServiceAssociation)
gen_frameweb_NavigationDependency_Dependency = Generalization(general=Dependency, specific=frameweb_NavigationDependency)
gen_frameweb_DAOMethod_Operation = Generalization(general=Operation, specific=frameweb_DAOMethod)
gen_frameweb_DomainPackage_Package = Generalization(general=Package, specific=frameweb_DomainPackage)
gen_frameweb_ViewPackage_NavigationPackage = Generalization(general=NavigationPackage, specific=frameweb_ViewPackage)
gen_frameweb_ControllerPackage_NavigationPackage = Generalization(general=NavigationPackage, specific=frameweb_ControllerPackage)
gen_frameweb_ControllerExtension_NavigationExtension = Generalization(general=NavigationExtension, specific=frameweb_ControllerExtension)
gen_frameweb_Controller_Stereotype = Generalization(general=Stereotype, specific=frameweb_Controller)
gen_frameweb_ControllerSet_Package = Generalization(general=Package, specific=frameweb_ControllerSet)
gen_frameweb_ResultExtension_NavigationExtension = Generalization(general=NavigationExtension, specific=frameweb_ResultExtension)
gen_frameweb_ClassMappingExtension_DomainExtension = Generalization(general=DomainExtension, specific=frameweb_ClassMappingExtension)
gen_frameweb_AttributeMappingExtension_DomainExtension = Generalization(general=DomainExtension, specific=frameweb_AttributeMappingExtension)
gen_frameweb_ControllerExtensionEnd_ExtensionEnd = Generalization(general=ExtensionEnd, specific=frameweb_ControllerExtensionEnd)
gen_frameweb_TagExtensionEnd_ExtensionEnd = Generalization(general=ExtensionEnd, specific=frameweb_TagExtensionEnd)
gen_frameweb_ResultExtensionEnd_ExtensionEnd = Generalization(general=ExtensionEnd, specific=frameweb_ResultExtensionEnd)
gen_frameweb_ClassMappingExtensionEnd_ExtensionEnd = Generalization(general=ExtensionEnd, specific=frameweb_ClassMappingExtensionEnd)
gen_frameweb_AttributeMappingExtensionEnd_ExtensionEnd = Generalization(general=ExtensionEnd, specific=frameweb_AttributeMappingExtensionEnd)
gen_frameweb_ControllerProperty_Property = Generalization(general=Property_, specific=frameweb_ControllerProperty)
gen_frameweb_TagProperty_Property = Generalization(general=Property_, specific=frameweb_TagProperty)
gen_frameweb_DAOGeneralization_Generalization = Generalization(general=Generalization, specific=frameweb_DAOGeneralization)
gen_frameweb_MappingLib_Package = Generalization(general=Package, specific=frameweb_MappingLib)
gen_frameweb_ClassMapping_Stereotype = Generalization(general=Stereotype, specific=frameweb_ClassMapping)
gen_frameweb_AttributeMapping_Stereotype = Generalization(general=Stereotype, specific=frameweb_AttributeMapping)
gen_frameweb_DomainGeneralizationSet_GeneralizationSet = Generalization(general=GeneralizationSet, specific=frameweb_DomainGeneralizationSet)
gen_frameweb_FrameworkExtension_Extension = Generalization(general=Extension, specific=frameweb_FrameworkExtension)
gen_frameweb_TagExtension_NavigationExtension = Generalization(general=NavigationExtension, specific=frameweb_TagExtension)
gen_frameweb_FrameworkApplication_ProfileApplication = Generalization(general=ProfileApplication, specific=frameweb_FrameworkApplication)
gen_frameweb_SeviceRealization_InterfaceRealization = Generalization(general=InterfaceRealization, specific=frameweb_SeviceRealization)
gen_frameweb_NavigationExtension_FrameworkExtension = Generalization(general=FrameworkExtension, specific=frameweb_NavigationExtension)
gen_frameweb_DomainExtension_FrameworkExtension = Generalization(general=FrameworkExtension, specific=frameweb_DomainExtension)
gen_frameweb_NavigationGeneralizationSet_GeneralizationSet = Generalization(general=GeneralizationSet, specific=frameweb_NavigationGeneralizationSet)
gen_frameweb_DAOGeneralizationSet_GeneralizationSet = Generalization(general=GeneralizationSet, specific=frameweb_DAOGeneralizationSet)
gen_frameweb_ServiceGeneralizationSet_GeneralizationSet = Generalization(general=GeneralizationSet, specific=frameweb_ServiceGeneralizationSet)
gen_frameweb_SemanticPackage_Package = Generalization(general=Package, specific=frameweb_SemanticPackage)
gen_frameweb_IRI_Property = Generalization(general=Property_, specific=frameweb_IRI)
gen_frameweb_ResultProperty_Property = Generalization(general=Property_, specific=frameweb_ResultProperty)
gen_frameweb_ClassMappingPropery_Property = Generalization(general=Property_, specific=frameweb_ClassMappingPropery)
gen_frameweb_AttributeMappingProperty_Property = Generalization(general=Property_, specific=frameweb_AttributeMappingProperty)
gen_frameweb_Axiom_Class = Generalization(general=Class_, specific=frameweb_Axiom)
gen_frameweb_Annotation_Class = Generalization(general=Class_, specific=frameweb_Annotation)
gen_frameweb_VocabularyModel_FramewebModel = Generalization(general=FramewebModel, specific=frameweb_VocabularyModel)
gen_frameweb_Vocabulary_Package = Generalization(general=Package, specific=frameweb_Vocabulary)
gen_frameweb_VocabularyConstraints_Constraint = Generalization(general=Constraint, specific=frameweb_VocabularyConstraints)
gen_frameweb_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=frameweb_Property)
gen_frameweb_Property_ConnectableElement = Generalization(general=ConnectableElement, specific=frameweb_Property)
gen_frameweb_Property_DeploymentTarget = Generalization(general=DeploymentTarget, specific=frameweb_Property)
gen_frameweb_Association_Classifier = Generalization(general=Classifier, specific=frameweb_Association)
gen_frameweb_Association_Relationship = Generalization(general=Relationship, specific=frameweb_Association)
gen_frameweb_Individual_Property = Generalization(general=Property_, specific=frameweb_Individual)
gen_frameweb_VocabularyLiteral_LiteralString = Generalization(general=LiteralString, specific=frameweb_VocabularyLiteral)
gen_frameweb_VocabularyAssociation_Association = Generalization(general=Association, specific=frameweb_VocabularyAssociation)
gen_frameweb_VocabularyProperty_Property = Generalization(general=Property_, specific=frameweb_VocabularyProperty)
gen_frameweb_VocabularyEntity_Classifier = Generalization(general=Classifier, specific=frameweb_VocabularyEntity)
gen_frameweb_ObjectProperty_VocabularyEntity = Generalization(general=VocabularyEntity, specific=frameweb_ObjectProperty)
gen_frameweb_ObjectProperty_VocabularyAssociation = Generalization(general=VocabularyAssociation, specific=frameweb_ObjectProperty)
gen_frameweb_DataProperty_VocabularyEntity = Generalization(general=VocabularyEntity, specific=frameweb_DataProperty)
gen_frameweb_DataProperty_VocabularyAssociation = Generalization(general=VocabularyAssociation, specific=frameweb_DataProperty)
gen_frameweb_AnnotationProperty_VocabularyEntity = Generalization(general=VocabularyEntity, specific=frameweb_AnnotationProperty)
gen_frameweb_AnnotationProperty_VocabularyAssociation = Generalization(general=VocabularyAssociation, specific=frameweb_AnnotationProperty)
gen_frameweb_VocabularyDataType_VocabularyEntity = Generalization(general=VocabularyEntity, specific=frameweb_VocabularyDataType)
gen_frameweb_VocabularyDataType_DataType = Generalization(general=DataType, specific=frameweb_VocabularyDataType)
gen_frameweb_NamedIndividual_VocabularyEntity = Generalization(general=VocabularyEntity, specific=frameweb_NamedIndividual)
gen_frameweb_NamedIndividual_Individual = Generalization(general=Individual, specific=frameweb_NamedIndividual)
gen_frameweb_VocabularyClassExpression_Class = Generalization(general=Class_, specific=frameweb_VocabularyClassExpression)
gen_frameweb_VocabularyClass_VocabularyEntity = Generalization(general=VocabularyEntity, specific=frameweb_VocabularyClass)
gen_frameweb_VocabularyClass_VocabularyClassExpression = Generalization(general=VocabularyClassExpression, specific=frameweb_VocabularyClass)
gen_frameweb_AnonymousIndividual_Individual = Generalization(general=Individual, specific=frameweb_AnonymousIndividual)

# Domain Model
domain_model = DomainModel(
    name="frameweb",
    types={frameweb_FramewebProject, Profile, frameweb_EntityModel, FramewebModel, frameweb_NavigationModel, frameweb_ApplicationModel, frameweb_PersistenceModel, frameweb_DomainAssociation, Association, frameweb_FramewebModel, frameweb_FrameworkProfile, Model, DomainAttribute, frameweb_IdAttribute, frameweb_LOBAttribute, frameweb_EmbeddedAttribute, frameweb_DecimalAttribute, frameweb_DateTimeAttribute, frameweb_DomainAttribute, Property_, frameweb_VersionAttribute, frameweb_Page, NavigationClass, frameweb_TagLib, frameweb_Template, frameweb_DAOInterface, Interface, frameweb_DAOClass, Class_, frameweb_DAORealization, InterfaceRealization, frameweb_FrontControllerClass, frameweb_IOParameter, NavigationAttribute, frameweb_Result, frameweb_FrontControllerMethod, frameweb_ResultConstraint, frameweb_NavigationAssociation, Operation, frameweb_ServiceClass, frameweb_ServiceInterface, frameweb_ServiceGeneralization, Generalization, frameweb_ServiceControllerAssociation, ServiceAssociation, frameweb_DomainClass, frameweb_UIComponentField, frameweb_ResultDependency, NavigationDependency, frameweb_MethodCosntraint, frameweb_PageDependency, frameweb_PageConstraint, frameweb_ChainingDependency, frameweb_ChainingConstraint, frameweb_DAOServiceAssociation, frameweb_NavigationAttribute, frameweb_NavigationClass, frameweb_DomainMethod, frameweb_FrontControllerDependency, frameweb_PersistencePackage, frameweb_ApplicationPackage, frameweb_UIComponent, frameweb_ResultType, Stereotype, frameweb_NavigationPackage, frameweb_DomainGeneralization, frameweb_Tag, frameweb_NavigationCompositionPart, NavigationProperty, frameweb_NavigationCompositionWhole, frameweb_NavigationProperty, frameweb_ResultSet, frameweb_NavigationConstraint, Constraint, NavigationConstraint, frameweb_NavigationGeneralization, frameweb_DomainConstraints, frameweb_DomainProperty, frameweb_DAOAttribute, frameweb_ServiceMethod, frameweb_ServiceAttribute, frameweb_ServiceAssociation, frameweb_NavigationDependency, Dependency, frameweb_DAOMethod, frameweb_DomainPackage, Package, frameweb_ViewPackage, NavigationPackage, frameweb_ControllerPackage, frameweb_ControllerExtension, frameweb_Controller, frameweb_ControllerSet, frameweb_ResultExtension, frameweb_ClassMappingExtension, DomainExtension, frameweb_AttributeMappingExtension, frameweb_ControllerExtensionEnd, ExtensionEnd, frameweb_TagExtensionEnd, frameweb_ResultExtensionEnd, frameweb_ClassMappingExtensionEnd, frameweb_AttributeMappingExtensionEnd, frameweb_ControllerProperty, frameweb_TagProperty, frameweb_DAOGeneralization, frameweb_MappingLib, frameweb_ClassMapping, frameweb_AttributeMapping, frameweb_DomainGeneralizationSet, GeneralizationSet, frameweb_FrameworkExtension, Extension, frameweb_TagExtension, NavigationExtension, frameweb_SeviceRealization, frameweb_FrameworkApplication, ProfileApplication, frameweb_NavigationExtension, FrameworkExtension, frameweb_DomainExtension, frameweb_NavigationGeneralizationSet, frameweb_DAOGeneralizationSet, frameweb_ServiceGeneralizationSet, frameweb_SemanticPackage, frameweb_IRI, frameweb_ResultProperty, frameweb_ClassMappingPropery, frameweb_AttributeMappingProperty, frameweb_Axiom, frameweb_Annotation, frameweb_VocabularyModel, frameweb_Vocabulary, frameweb_VocabularyConstraints, frameweb_Property, StructuralFeature, ConnectableElement, DeploymentTarget, frameweb_DataType, frameweb_Interface, frameweb_Association, frameweb_Class, frameweb_ValueSpecification, Classifier, Relationship, frameweb_Type, frameweb_Individual, frameweb_VocabularyLiteral, LiteralString, frameweb_VocabularyAssociation, frameweb_VocabularyProperty, frameweb_VocabularyEntity, frameweb_ObjectProperty, VocabularyEntity, VocabularyAssociation, frameweb_DataProperty, frameweb_AnnotationProperty, frameweb_VocabularyDataType, DataType, frameweb_NamedIndividual, Individual, frameweb_VocabularyClassExpression, frameweb_VocabularyClass, VocabularyClassExpression, frameweb_AnonymousIndividual, DateTimePrecision, Generation, Collection, Order, Cascade, Fetch, ConstantNameList, FrameworkCategoryList, InheritanceMapping, FrameworkKindList},
    associations={compose0, configures1, pageTagLib3, templateTagLib4, resultResult7, resultMethod8, resultDependendencyCosntraint10, display6, methodDependendencyConstraint14, pageDependencyCosntraint16, outMethod17, inMethod19, chainingDependendencyConstraint22, method12, inject24, directlyImportsDocuments25, vocabularyIRI26, axioms29, annotations31, datatype33, interface34, associationEnd37, qualifier39, opposite46, owningAssociation48, redefinedProperty50, subsettedProperty53, association55, class41, defaultValue43, memberEnd58, ownedEnd60, navigableOwnedEnd62, endType57, entityIRI65, vocabularyproperty67},
    generalizations={gen_frameweb_FrameworkProfile_Profile, gen_frameweb_EntityModel_FramewebModel, gen_frameweb_NavigationModel_FramewebModel, gen_frameweb_ApplicationModel_FramewebModel, gen_frameweb_PersistenceModel_FramewebModel, gen_frameweb_DomainAssociation_Association, gen_frameweb_FramewebModel_Model, gen_frameweb_VersionAttribute_DomainAttribute, gen_frameweb_IdAttribute_DomainAttribute, gen_frameweb_LOBAttribute_DomainAttribute, gen_frameweb_EmbeddedAttribute_DomainAttribute, gen_frameweb_DecimalAttribute_DomainAttribute, gen_frameweb_DateTimeAttribute_DomainAttribute, gen_frameweb_DomainAttribute_Property, gen_frameweb_Page_NavigationClass, gen_frameweb_Template_NavigationClass, gen_frameweb_DAOInterface_Interface, gen_frameweb_DAOClass_Class, gen_frameweb_DAORealization_InterfaceRealization, gen_frameweb_FrontControllerClass_Class, gen_frameweb_IOParameter_NavigationAttribute, gen_frameweb_NavigationAssociation_Association, gen_frameweb_FrontControllerMethod_Operation, gen_frameweb_ServiceClass_Class, gen_frameweb_ServiceInterface_Interface, gen_frameweb_ServiceGeneralization_Generalization, gen_frameweb_ServiceControllerAssociation_ServiceAssociation, gen_frameweb_DomainClass_Class, gen_frameweb_ResultDependency_NavigationDependency, gen_frameweb_PageDependency_NavigationDependency, gen_frameweb_ChainingDependency_NavigationDependency, gen_frameweb_DAOServiceAssociation_ServiceAssociation, gen_frameweb_NavigationAttribute_Property, gen_frameweb_NavigationClass_Class, gen_frameweb_DomainMethod_Operation, gen_frameweb_Result_Class, gen_frameweb_FrontControllerDependency_NavigationDependency, gen_frameweb_PersistencePackage_Package, gen_frameweb_ApplicationPackage_Package, gen_frameweb_UIComponent_NavigationClass, gen_frameweb_ResultType_Stereotype, gen_frameweb_NavigationPackage_Package, gen_frameweb_DomainGeneralization_Generalization, gen_frameweb_UIComponentField_NavigationAttribute, gen_frameweb_TagLib_Package, gen_frameweb_Tag_Stereotype, gen_frameweb_NavigationCompositionPart_NavigationProperty, gen_frameweb_NavigationCompositionWhole_NavigationProperty, gen_frameweb_NavigationProperty_Property, gen_frameweb_ResultSet_Package, gen_frameweb_NavigationConstraint_Constraint, gen_frameweb_PageConstraint_NavigationConstraint, gen_frameweb_ResultConstraint_NavigationConstraint, gen_frameweb_MethodCosntraint_NavigationConstraint, gen_frameweb_ChainingConstraint_NavigationConstraint, gen_frameweb_NavigationGeneralization_Generalization, gen_frameweb_DomainConstraints_Constraint, gen_frameweb_DomainProperty_Property, gen_frameweb_DAOAttribute_Property, gen_frameweb_ServiceMethod_Operation, gen_frameweb_ServiceAttribute_Property, gen_frameweb_ServiceAssociation_Association, gen_frameweb_NavigationDependency_Dependency, gen_frameweb_DAOMethod_Operation, gen_frameweb_DomainPackage_Package, gen_frameweb_ViewPackage_NavigationPackage, gen_frameweb_ControllerPackage_NavigationPackage, gen_frameweb_ControllerExtension_NavigationExtension, gen_frameweb_Controller_Stereotype, gen_frameweb_ControllerSet_Package, gen_frameweb_ResultExtension_NavigationExtension, gen_frameweb_ClassMappingExtension_DomainExtension, gen_frameweb_AttributeMappingExtension_DomainExtension, gen_frameweb_ControllerExtensionEnd_ExtensionEnd, gen_frameweb_TagExtensionEnd_ExtensionEnd, gen_frameweb_ResultExtensionEnd_ExtensionEnd, gen_frameweb_ClassMappingExtensionEnd_ExtensionEnd, gen_frameweb_AttributeMappingExtensionEnd_ExtensionEnd, gen_frameweb_ControllerProperty_Property, gen_frameweb_TagProperty_Property, gen_frameweb_DAOGeneralization_Generalization, gen_frameweb_MappingLib_Package, gen_frameweb_ClassMapping_Stereotype, gen_frameweb_AttributeMapping_Stereotype, gen_frameweb_DomainGeneralizationSet_GeneralizationSet, gen_frameweb_FrameworkExtension_Extension, gen_frameweb_TagExtension_NavigationExtension, gen_frameweb_FrameworkApplication_ProfileApplication, gen_frameweb_SeviceRealization_InterfaceRealization, gen_frameweb_NavigationExtension_FrameworkExtension, gen_frameweb_DomainExtension_FrameworkExtension, gen_frameweb_NavigationGeneralizationSet_GeneralizationSet, gen_frameweb_DAOGeneralizationSet_GeneralizationSet, gen_frameweb_ServiceGeneralizationSet_GeneralizationSet, gen_frameweb_SemanticPackage_Package, gen_frameweb_IRI_Property, gen_frameweb_ResultProperty_Property, gen_frameweb_ClassMappingPropery_Property, gen_frameweb_AttributeMappingProperty_Property, gen_frameweb_Axiom_Class, gen_frameweb_Annotation_Class, gen_frameweb_VocabularyModel_FramewebModel, gen_frameweb_Vocabulary_Package, gen_frameweb_VocabularyConstraints_Constraint, gen_frameweb_Property_StructuralFeature, gen_frameweb_Property_ConnectableElement, gen_frameweb_Property_DeploymentTarget, gen_frameweb_Association_Classifier, gen_frameweb_Association_Relationship, gen_frameweb_Individual_Property, gen_frameweb_VocabularyLiteral_LiteralString, gen_frameweb_VocabularyAssociation_Association, gen_frameweb_VocabularyProperty_Property, gen_frameweb_VocabularyEntity_Classifier, gen_frameweb_ObjectProperty_VocabularyEntity, gen_frameweb_ObjectProperty_VocabularyAssociation, gen_frameweb_DataProperty_VocabularyEntity, gen_frameweb_DataProperty_VocabularyAssociation, gen_frameweb_AnnotationProperty_VocabularyEntity, gen_frameweb_AnnotationProperty_VocabularyAssociation, gen_frameweb_VocabularyDataType_VocabularyEntity, gen_frameweb_VocabularyDataType_DataType, gen_frameweb_NamedIndividual_VocabularyEntity, gen_frameweb_NamedIndividual_Individual, gen_frameweb_VocabularyClassExpression_Class, gen_frameweb_VocabularyClass_VocabularyEntity, gen_frameweb_VocabularyClass_VocabularyClassExpression, gen_frameweb_AnonymousIndividual_Individual},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)