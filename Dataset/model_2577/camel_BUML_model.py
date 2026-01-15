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
ActionType: Enumeration = Enumeration(
    name="ActionType",
    literals={
            EnumerationLiteral(name="EVENT_CREATION"),
			EnumerationLiteral(name="SCALE_IN"),
			EnumerationLiteral(name="SCALE_OUT"),
			EnumerationLiteral(name="SCALE_UP"),
			EnumerationLiteral(name="SCALE_DOWN"),
			EnumerationLiteral(name="READ"),
			EnumerationLiteral(name="WRITE")
    }
)

LayerType: Enumeration = Enumeration(
    name="LayerType",
    literals={
            EnumerationLiteral(name="SaaS"),
			EnumerationLiteral(name="PaaS"),
			EnumerationLiteral(name="IaaS"),
			EnumerationLiteral(name="BPM"),
			EnumerationLiteral(name="SCC")
    }
)

CommunicationType: Enumeration = Enumeration(
    name="CommunicationType",
    literals={
            EnumerationLiteral(name="ANY"),
			EnumerationLiteral(name="LOCAL"),
			EnumerationLiteral(name="REMOTE")
    }
)

ComparisonOperatorType: Enumeration = Enumeration(
    name="ComparisonOperatorType",
    literals={
            EnumerationLiteral(name="GREATER_THAN"),
			EnumerationLiteral(name="GREATER_EQUAL_THAN"),
			EnumerationLiteral(name="LESS_THAN"),
			EnumerationLiteral(name="LESS_EQUAL_THAN"),
			EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="NOT_EQUAL")
    }
)

MetricFunctionArityType: Enumeration = Enumeration(
    name="MetricFunctionArityType",
    literals={
            EnumerationLiteral(name="UNARY"),
			EnumerationLiteral(name="BINARY"),
			EnumerationLiteral(name="N_ARY")
    }
)

MetricFunctionType: Enumeration = Enumeration(
    name="MetricFunctionType",
    literals={
            EnumerationLiteral(name="MEDIAN"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="TIMES"),
			EnumerationLiteral(name="DIV"),
			EnumerationLiteral(name="MODULO"),
			EnumerationLiteral(name="MEAN"),
			EnumerationLiteral(name="STD"),
			EnumerationLiteral(name="COUNT"),
			EnumerationLiteral(name="MIN"),
			EnumerationLiteral(name="MAX"),
			EnumerationLiteral(name="PERCENTILE"),
			EnumerationLiteral(name="DERIVATIVE"),
			EnumerationLiteral(name="MODE")
    }
)

ScheduleType: Enumeration = Enumeration(
    name="ScheduleType",
    literals={
            EnumerationLiteral(name="FIXED_RATE"),
			EnumerationLiteral(name="FIXED_DELAY"),
			EnumerationLiteral(name="SINGLE_EVENT")
    }
)

PropertyType: Enumeration = Enumeration(
    name="PropertyType",
    literals={
            EnumerationLiteral(name="ABSTRACT"),
			EnumerationLiteral(name="MEASURABLE")
    }
)

QuantifierType: Enumeration = Enumeration(
    name="QuantifierType",
    literals={
            EnumerationLiteral(name="ANY"),
			EnumerationLiteral(name="ALL"),
			EnumerationLiteral(name="SOME")
    }
)

WindowSizeType: Enumeration = Enumeration(
    name="WindowSizeType",
    literals={
            EnumerationLiteral(name="MEASUREMENTS_ONLY"),
			EnumerationLiteral(name="TIME_ONLY"),
			EnumerationLiteral(name="FIRST_MATCH"),
			EnumerationLiteral(name="BOTH_MATCH")
    }
)

WindowType: Enumeration = Enumeration(
    name="WindowType",
    literals={
            EnumerationLiteral(name="FIXED"),
			EnumerationLiteral(name="SLIDING")
    }
)

FunctionPatternType: Enumeration = Enumeration(
    name="FunctionPatternType",
    literals={
            EnumerationLiteral(name="MAP"),
			EnumerationLiteral(name="REDUCE")
    }
)

ResourcePattern: Enumeration = Enumeration(
    name="ResourcePattern",
    literals={
            EnumerationLiteral(name="EXACT"),
			EnumerationLiteral(name="TREE")
    }
)

SecurityLevel: Enumeration = Enumeration(
    name="SecurityLevel",
    literals={
            EnumerationLiteral(name="LOW"),
			EnumerationLiteral(name="MEDIUM"),
			EnumerationLiteral(name="HIGH")
    }
)

Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="select"),
			EnumerationLiteral(name="add"),
			EnumerationLiteral(name="remove"),
			EnumerationLiteral(name="multiply"),
			EnumerationLiteral(name="divide")
    }
)

RequirementOperatorType: Enumeration = Enumeration(
    name="RequirementOperatorType",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="XOR")
    }
)

OptimisationFunctionType: Enumeration = Enumeration(
    name="OptimisationFunctionType",
    literals={
            EnumerationLiteral(name="MINIMISE"),
			EnumerationLiteral(name="MAXIMISE")
    }
)

BinaryPatternOperatorType: Enumeration = Enumeration(
    name="BinaryPatternOperatorType",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="PRECEDES"),
			EnumerationLiteral(name="REPEAT_UNTIL")
    }
)

TimerType: Enumeration = Enumeration(
    name="TimerType",
    literals={
            EnumerationLiteral(name="WITHIN"),
			EnumerationLiteral(name="WITHIN_MAX"),
			EnumerationLiteral(name="INTERVAL")
    }
)

UnaryPatternOperatorType: Enumeration = Enumeration(
    name="UnaryPatternOperatorType",
    literals={
            EnumerationLiteral(name="EVERY"),
			EnumerationLiteral(name="NOT"),
			EnumerationLiteral(name="REPEAT"),
			EnumerationLiteral(name="WHEN")
    }
)

StatusType: Enumeration = Enumeration(
    name="StatusType",
    literals={
            EnumerationLiteral(name="WARNING"),
			EnumerationLiteral(name="SUCCESS"),
			EnumerationLiteral(name="FATAL"),
			EnumerationLiteral(name="CRITICAL")
    }
)

TypeEnum: Enumeration = Enumeration(
    name="TypeEnum",
    literals={
            EnumerationLiteral(name="IntType"),
			EnumerationLiteral(name="StringType"),
			EnumerationLiteral(name="BooleanType"),
			EnumerationLiteral(name="FloatType"),
			EnumerationLiteral(name="DoubleType")
    }
)

UnitDimensionType: Enumeration = Enumeration(
    name="UnitDimensionType",
    literals={
            EnumerationLiteral(name="TIME_INTERVAL"),
			EnumerationLiteral(name="STORAGE"),
			EnumerationLiteral(name="COST"),
			EnumerationLiteral(name="THROUGHPUT"),
			EnumerationLiteral(name="REQUEST_NUM"),
			EnumerationLiteral(name="TRANSACTION_NUM"),
			EnumerationLiteral(name="DIMENSIONLESS"),
			EnumerationLiteral(name="CORE_NUM")
    }
)

UnitType: Enumeration = Enumeration(
    name="UnitType",
    literals={
            EnumerationLiteral(name="KILOBYTES"),
			EnumerationLiteral(name="MEGABYTES"),
			EnumerationLiteral(name="GIGABYTES"),
			EnumerationLiteral(name="MILLISECONDS"),
			EnumerationLiteral(name="SECONDS"),
			EnumerationLiteral(name="MINUTES"),
			EnumerationLiteral(name="HOURS"),
			EnumerationLiteral(name="DAYS"),
			EnumerationLiteral(name="WEEKS"),
			EnumerationLiteral(name="MONTHS"),
			EnumerationLiteral(name="REQUESTS"),
			EnumerationLiteral(name="REQUESTS_PER_SECOND"),
			EnumerationLiteral(name="TRANSACTIONS"),
			EnumerationLiteral(name="TRANSACTIONS_PER_SECOND"),
			EnumerationLiteral(name="CORES"),
			EnumerationLiteral(name="PERCENTAGE"),
			EnumerationLiteral(name="EUROS"),
			EnumerationLiteral(name="POUNDS"),
			EnumerationLiteral(name="DOLLARS"),
			EnumerationLiteral(name="BYTES"),
			EnumerationLiteral(name="BYTES_PER_SECOND")
    }
)

# Classes
camel_Model = Class(name="camel::Model", is_abstract=True)
camel_CamelModel = Class(name="camel::CamelModel")
Model = Class(name="Model")
camel_Action = Class(name="camel::Action")
camel_Application = Class(name="camel::Application")
ExecutionModel = Class(name="ExecutionModel")
LocationModel = Class(name="LocationModel")
MetricModel = Class(name="MetricModel")
OrganisationModel = Class(name="OrganisationModel")
ProviderModel = Class(name="ProviderModel")
RequirementModel = Class(name="RequirementModel")
ScalabilityModel = Class(name="ScalabilityModel")
SecurityModel = Class(name="SecurityModel")
DeploymentModel = Class(name="DeploymentModel")
TypeModel = Class(name="TypeModel")
UnitModel = Class(name="UnitModel")
VM = Class(name="VM")
Entity = Class(name="Entity")
VMInstance = Class(name="VMInstance")
Communication = Class(name="Communication")
CommunicationInstance = Class(name="CommunicationInstance")
camel_deployment_DeploymentElement = Class(name="camel::deployment::DeploymentElement", is_abstract=True)
camel_deployment_DeploymentModel = Class(name="camel::deployment::DeploymentModel")
InternalComponent = Class(name="InternalComponent")
InternalComponentInstance = Class(name="InternalComponentInstance")
camel_deployment_InternalComponent = Class(name="camel::deployment::InternalComponent")
Component = Class(name="Component")
Hosting = Class(name="Hosting")
RequiredCommunication = Class(name="RequiredCommunication")
HostingInstance = Class(name="HostingInstance")
VMRequirementSet = Class(name="VMRequirementSet")
camel_deployment_Component = Class(name="camel::deployment::Component", is_abstract=True)
DeploymentElement = Class(name="DeploymentElement")
ProvidedCommunication = Class(name="ProvidedCommunication")
ProvidedHost = Class(name="ProvidedHost")
Configuration = Class(name="Configuration")
LocationRequirement = Class(name="LocationRequirement")
ProviderRequirement = Class(name="ProviderRequirement")
QualitativeHardwareRequirement = Class(name="QualitativeHardwareRequirement")
QuantitativeHardwareRequirement = Class(name="QuantitativeHardwareRequirement")
OSOrImageRequirement = Class(name="OSOrImageRequirement")
RequiredHost = Class(name="RequiredHost")
camel_deployment_VM = Class(name="camel::deployment::VM")
camel_deployment_VMRequirementSet = Class(name="camel::deployment::VMRequirementSet")
camel_deployment_CommunicationPort = Class(name="camel::deployment::CommunicationPort", is_abstract=True)
camel_deployment_ProvidedCommunication = Class(name="camel::deployment::ProvidedCommunication")
CommunicationPort = Class(name="CommunicationPort")
camel_deployment_RequiredCommunication = Class(name="camel::deployment::RequiredCommunication")
camel_deployment_Hosting = Class(name="camel::deployment::Hosting")
camel_deployment_HostingPort = Class(name="camel::deployment::HostingPort", is_abstract=True)
camel_deployment_ProvidedHost = Class(name="camel::deployment::ProvidedHost")
camel_deployment_Configuration = Class(name="camel::deployment::Configuration")
HostingPort = Class(name="HostingPort")
camel_deployment_RequiredHost = Class(name="camel::deployment::RequiredHost")
camel_deployment_Communication = Class(name="camel::deployment::Communication")
camel_deployment_InternalComponentInstance = Class(name="camel::deployment::InternalComponentInstance")
ComponentInstance = Class(name="ComponentInstance")
RequiredCommunicationInstance = Class(name="RequiredCommunicationInstance")
RequiredHostInstance = Class(name="RequiredHostInstance")
camel_deployment_VMInstance = Class(name="camel::deployment::VMInstance")
camel_deployment_ComponentInstance = Class(name="camel::deployment::ComponentInstance", is_abstract=True)
ProvidedCommunicationInstance = Class(name="ProvidedCommunicationInstance")
ProvidedHostInstance = Class(name="ProvidedHostInstance")
camel_deployment_CommunicationPortInstance = Class(name="camel::deployment::CommunicationPortInstance")
camel_deployment_ProvidedCommunicationInstance = Class(name="camel::deployment::ProvidedCommunicationInstance")
CommunicationPortInstance = Class(name="CommunicationPortInstance")
camel_deployment_RequiredCommunicationInstance = Class(name="camel::deployment::RequiredCommunicationInstance")
camel_deployment_HostingInstance = Class(name="camel::deployment::HostingInstance")
camel_deployment_HostingPortInstance = Class(name="camel::deployment::HostingPortInstance", is_abstract=True)
camel_deployment_ProvidedHostInstance = Class(name="camel::deployment::ProvidedHostInstance")
HostingPortInstance = Class(name="HostingPortInstance")
camel_deployment_RequiredHostInstance = Class(name="camel::deployment::RequiredHostInstance")
Attribute = Class(name="Attribute")
SingleValue = Class(name="SingleValue")
camel_deployment_CommunicationInstance = Class(name="camel::deployment::CommunicationInstance")
camel_execution_ExecutionContext = Class(name="camel::execution::ExecutionContext")
execution_camel_Application = Class(name="execution::camel::Application")
MonetaryUnit = Class(name="MonetaryUnit")
RequirementGroup = Class(name="RequirementGroup")
camel_execution_Measurement = Class(name="camel::execution::Measurement")
camel_execution_ExecutionModel = Class(name="camel::execution::ExecutionModel")
ActionRealisation = Class(name="ActionRealisation")
EventInstance = Class(name="EventInstance")
ExecutionContext = Class(name="ExecutionContext")
Measurement = Class(name="Measurement")
SLOAssessment = Class(name="SLOAssessment")
RuleTrigger = Class(name="RuleTrigger")
camel_execution_ActionRealisation = Class(name="camel::execution::ActionRealisation")
execution_camel_Action = Class(name="execution::camel::Action")
camel_execution_InternalComponentMeasurement = Class(name="camel::execution::InternalComponentMeasurement")
camel_execution_CommunicationMeasurement = Class(name="camel::execution::CommunicationMeasurement")
camel_execution_VMMeasurement = Class(name="camel::execution::VMMeasurement")
camel_execution_SLOAssessment = Class(name="camel::execution::SLOAssessment")
MetricInstance = Class(name="MetricInstance")
ServiceLevelObjective = Class(name="ServiceLevelObjective")
camel_execution_ApplicationMeasurement = Class(name="camel::execution::ApplicationMeasurement")
ScalabilityRule = Class(name="ScalabilityRule")
camel_location_LocationModel = Class(name="camel::location::LocationModel")
CloudLocation = Class(name="CloudLocation")
Country = Class(name="Country")
camel_execution_RuleTrigger = Class(name="camel::execution::RuleTrigger")
camel_location_GeographicalRegion = Class(name="camel::location::GeographicalRegion")
camel_location_Country = Class(name="camel::location::Country")
GeographicalRegion = Class(name="GeographicalRegion")
camel_location_Location = Class(name="camel::location::Location", is_abstract=True)
camel_location_CloudLocation = Class(name="camel::location::CloudLocation")
Location = Class(name="Location")
MetricContext = Class(name="MetricContext")
camel_metric_PropertyCondition = Class(name="camel::metric::PropertyCondition")
PropertyContext = Class(name="PropertyContext")
TimeIntervalUnit = Class(name="TimeIntervalUnit")
camel_metric_MetricInstance = Class(name="camel::metric::MetricInstance", is_abstract=True)
camel_metric_Condition = Class(name="camel::metric::Condition", is_abstract=True)
camel_metric_MetricCondition = Class(name="camel::metric::MetricCondition")
Condition = Class(name="Condition")
MetricObjectBinding = Class(name="MetricObjectBinding")
camel_metric_CompositeMetricInstance = Class(name="camel::metric::CompositeMetricInstance")
camel_metric_RawMetricInstance = Class(name="camel::metric::RawMetricInstance")
Sensor = Class(name="Sensor")
camel_metric_MetricFormulaParameter = Class(name="camel::metric::MetricFormulaParameter")
Metric = Class(name="Metric")
Schedule = Class(name="Schedule")
Window = Class(name="Window")
ValueType = Class(name="ValueType")
Unit = Class(name="Unit")
Property_ = Class(name="Property")
camel_metric_CompositeMetric = Class(name="camel::metric::CompositeMetric")
camel_metric_MetricFormula = Class(name="camel::metric::MetricFormula")
MetricFormulaParameter = Class(name="MetricFormulaParameter")
camel_metric_Metric = Class(name="camel::metric::Metric", is_abstract=True)
camel_metric_MetricObjectBinding = Class(name="camel::metric::MetricObjectBinding", is_abstract=True)
camel_metric_MetricApplicationBinding = Class(name="camel::metric::MetricApplicationBinding")
camel_metric_MetricComponentBinding = Class(name="camel::metric::MetricComponentBinding")
camel_metric_MetricVMBinding = Class(name="camel::metric::MetricVMBinding")
camel_metric_Property = Class(name="camel::metric::Property")
MetricFormula = Class(name="MetricFormula")
camel_metric_RawMetric = Class(name="camel::metric::RawMetric")
camel_metric_Sensor = Class(name="camel::metric::Sensor")
camel_metric_Window = Class(name="camel::metric::Window")
camel_metric_Schedule = Class(name="camel::metric::Schedule")
metric_camel_Application = Class(name="metric::camel::Application")
camel_metric_MetricModel = Class(name="camel::metric::MetricModel")
ConditionContext = Class(name="ConditionContext")
camel_metric_ConditionContext = Class(name="camel::metric::ConditionContext", is_abstract=True)
camel_metric_CompositeMetricContext = Class(name="camel::metric::CompositeMetricContext")
camel_metric_RawMetricContext = Class(name="camel::metric::RawMetricContext")
camel_metric_PropertyContext = Class(name="camel::metric::PropertyContext")
camel_metric_MetricContext = Class(name="camel::metric::MetricContext", is_abstract=True)
DataCenter = Class(name="DataCenter")
Role = Class(name="Role")
RoleAssignment = Class(name="RoleAssignment")
Permission = Class(name="Permission")
ResourceFilter = Class(name="ResourceFilter")
camel_organisation_Credentials = Class(name="camel::organisation::Credentials", is_abstract=True)
camel_organisation_CloudCredentials = Class(name="camel::organisation::CloudCredentials")
Credentials = Class(name="Credentials")
camel_organisation_OrganisationModel = Class(name="camel::organisation::OrganisationModel")
Organisation = Class(name="Organisation")
CloudProvider = Class(name="CloudProvider")
ExternalIdentifier = Class(name="ExternalIdentifier")
User = Class(name="User")
UserGroup = Class(name="UserGroup")
SecurityCapability = Class(name="SecurityCapability")
camel_organisation_User = Class(name="camel::organisation::User")
CloudCredentials = Class(name="CloudCredentials")
PaaSageCredentials = Class(name="PaaSageCredentials")
camel_organisation_ExternalIdentifier = Class(name="camel::organisation::ExternalIdentifier")
camel_organisation_DataCenter = Class(name="camel::organisation::DataCenter")
camel_organisation_Entity = Class(name="camel::organisation::Entity")
camel_organisation_Organisation = Class(name="camel::organisation::Organisation")
camel_organisation_CloudProvider = Class(name="camel::organisation::CloudProvider")
camel_organisation_ResourceFilter = Class(name="camel::organisation::ResourceFilter", is_abstract=True)
camel_organisation_InformationResourceFilter = Class(name="camel::organisation::InformationResourceFilter")
camel_organisation_ServiceResourceFilter = Class(name="camel::organisation::ServiceResourceFilter")
camel_organisation_Role = Class(name="camel::organisation::Role")
camel_organisation_RoleAssignment = Class(name="camel::organisation::RoleAssignment")
camel_organisation_Permission = Class(name="camel::organisation::Permission")
camel_provider_ProviderModel = Class(name="camel::provider::ProviderModel")
Constraint = Class(name="Constraint")
Feature = Class(name="Feature")
camel_provider_Attribute = Class(name="camel::provider::Attribute")
camel_organisation_UserGroup = Class(name="camel::organisation::UserGroup")
camel_organisation_PaaSageCredentials = Class(name="camel::organisation::PaaSageCredentials")
camel_provider_FeatCardinality = Class(name="camel::provider::FeatCardinality")
Cardinality = Class(name="Cardinality")
camel_provider_GroupCardinality = Class(name="camel::provider::GroupCardinality")
camel_provider_Clone = Class(name="camel::provider::Clone")
Clone = Class(name="Clone")
camel_provider_Constraint = Class(name="camel::provider::Constraint", is_abstract=True)
camel_provider_AttributeConstraint = Class(name="camel::provider::AttributeConstraint")
camel_provider_Cardinality = Class(name="camel::provider::Cardinality", is_abstract=True)
Scope = Class(name="Scope")
FeatCardinality = Class(name="FeatCardinality")
camel_provider_Functional = Class(name="camel::provider::Functional")
Requires = Class(name="Requires")
camel_provider_Feature = Class(name="camel::provider::Feature")
AttributeConstraint = Class(name="AttributeConstraint")
camel_provider_Excludes = Class(name="camel::provider::Excludes")
camel_provider_Implies = Class(name="camel::provider::Implies")
camel_provider_Requires = Class(name="camel::provider::Requires")
camel_provider_Exclusive = Class(name="camel::provider::Exclusive")
Alternative = Class(name="Alternative")
camel_provider_Scope = Class(name="camel::provider::Scope", is_abstract=True)
camel_provider_Instance = Class(name="camel::provider::Instance")
camel_provider_Product = Class(name="camel::provider::Product")
camel_requirement_RequirementModel = Class(name="camel::requirement::RequirementModel")
Requirement = Class(name="Requirement")
camel_requirement_Requirement = Class(name="camel::requirement::Requirement", is_abstract=True)
camel_requirement_RequirementGroup = Class(name="camel::requirement::RequirementGroup")
camel_provider_Alternative = Class(name="camel::provider::Alternative")
GroupCardinality = Class(name="GroupCardinality")
camel_requirement_HardRequirement = Class(name="camel::requirement::HardRequirement", is_abstract=True)
camel_requirement_SoftRequirement = Class(name="camel::requirement::SoftRequirement", is_abstract=True)
requirement_camel_Application = Class(name="requirement::camel::Application")
camel_requirement_ServiceLevelObjective = Class(name="camel::requirement::ServiceLevelObjective")
HardRequirement = Class(name="HardRequirement")
camel_requirement_OptimisationRequirement = Class(name="camel::requirement::OptimisationRequirement")
SoftRequirement = Class(name="SoftRequirement")
camel_requirement_HardwareRequirement = Class(name="camel::requirement::HardwareRequirement", is_abstract=True)
camel_requirement_QualitativeHardwareRequirement = Class(name="camel::requirement::QualitativeHardwareRequirement")
HardwareRequirement = Class(name="HardwareRequirement")
camel_requirement_QuantitativeHardwareRequirement = Class(name="camel::requirement::QuantitativeHardwareRequirement")
camel_requirement_ProviderRequirement = Class(name="camel::requirement::ProviderRequirement")
camel_requirement_OSOrImageRequirement = Class(name="camel::requirement::OSOrImageRequirement", is_abstract=True)
camel_requirement_OSRequirement = Class(name="camel::requirement::OSRequirement")
camel_requirement_SecurityRequirement = Class(name="camel::requirement::SecurityRequirement")
SecurityControl = Class(name="SecurityControl")
camel_requirement_LocationRequirement = Class(name="camel::requirement::LocationRequirement")
camel_requirement_ScaleRequirement = Class(name="camel::requirement::ScaleRequirement", is_abstract=True)
camel_requirement_HorizontalScaleRequirement = Class(name="camel::requirement::HorizontalScaleRequirement")
camel_requirement_ImageRequirement = Class(name="camel::requirement::ImageRequirement")
camel_requirement_VerticalScaleRequirement = Class(name="camel::requirement::VerticalScaleRequirement")
ScaleRequirement = Class(name="ScaleRequirement")
camel_scalability_ScalabilityModel = Class(name="camel::scalability::ScalabilityModel")
Event = Class(name="Event")
ScalingAction = Class(name="ScalingAction")
camel_scalability_Event = Class(name="camel::scalability::Event")
camel_scalability_EventPattern = Class(name="camel::scalability::EventPattern", is_abstract=True)
EventPattern = Class(name="EventPattern")
Timer = Class(name="Timer")
camel_scalability_UnaryEventPattern = Class(name="camel::scalability::UnaryEventPattern")
camel_scalability_BinaryEventPattern = Class(name="camel::scalability::BinaryEventPattern")
MetricCondition = Class(name="MetricCondition")
camel_scalability_EventInstance = Class(name="camel::scalability::EventInstance")
camel_scalability_SimpleEvent = Class(name="camel::scalability::SimpleEvent")
camel_scalability_FunctionalEvent = Class(name="camel::scalability::FunctionalEvent")
SimpleEvent = Class(name="SimpleEvent")
camel_scalability_NonFunctionalEvent = Class(name="camel::scalability::NonFunctionalEvent")
scalability_camel_Action = Class(name="scalability::camel::Action")
camel_scalability_ScalingAction = Class(name="camel::scalability::ScalingAction", is_abstract=True)
Action = Class(name="Action")
camel_scalability_HorizontalScalingAction = Class(name="camel::scalability::HorizontalScalingAction")
camel_scalability_ScalabilityRule = Class(name="camel::scalability::ScalabilityRule")
camel_scalability_Timer = Class(name="camel::scalability::Timer")
camel_scalability_VerticalScalingAction = Class(name="camel::scalability::VerticalScalingAction")
camel_security_SecurityModel = Class(name="camel::security::SecurityModel")
SecurityRequirement = Class(name="SecurityRequirement")
SecurityProperty = Class(name="SecurityProperty")
RawSecurityMetric = Class(name="RawSecurityMetric")
CompositeSecurityMetricInstance = Class(name="CompositeSecurityMetricInstance")
SecurityDomain = Class(name="SecurityDomain")
SecuritySLO = Class(name="SecuritySLO")
camel_security_SecurityDomain = Class(name="camel::security::SecurityDomain")
CompositeSecurityMetric = Class(name="CompositeSecurityMetric")
RawSecurityMetricInstance = Class(name="RawSecurityMetricInstance")
camel_security_RawSecurityMetricInstance = Class(name="camel::security::RawSecurityMetricInstance")
RawMetricInstance = Class(name="RawMetricInstance")
camel_security_RawSecurityMetric = Class(name="camel::security::RawSecurityMetric")
RawMetric = Class(name="RawMetric")
camel_security_SecurityProperty = Class(name="camel::security::SecurityProperty")
camel_security_Certifiable = Class(name="camel::security::Certifiable")
camel_security_SecuritySLO = Class(name="camel::security::SecuritySLO")
camel_security_SecurityCapability = Class(name="camel::security::SecurityCapability")
camel_security_SecurityControl = Class(name="camel::security::SecurityControl")
camel_type_TypeModel = Class(name="camel::type::TypeModel")
camel_type_Limit = Class(name="camel::type::Limit")
NumericValue = Class(name="NumericValue")
camel_type_SingleValue = Class(name="camel::type::SingleValue", is_abstract=True)
camel_type_BoolValue = Class(name="camel::type::BoolValue")
camel_type_EnumerateValue = Class(name="camel::type::EnumerateValue")
camel_type_NumericValue = Class(name="camel::type::NumericValue", is_abstract=True)
camel_type_IntegerValue = Class(name="camel::type::IntegerValue")
camel_type_FloatsValue = Class(name="camel::type::FloatsValue")
camel_security_CompositeSecurityMetric = Class(name="camel::security::CompositeSecurityMetric")
CompositeMetric = Class(name="CompositeMetric")
camel_security_CompositeSecurityMetricInstance = Class(name="camel::security::CompositeSecurityMetricInstance")
CompositeMetricInstance = Class(name="CompositeMetricInstance")
camel_type_Enumeration = Class(name="camel::type::Enumeration")
EnumerateValue = Class(name="EnumerateValue")
camel_type_List = Class(name="camel::type::List")
camel_type_Range = Class(name="camel::type::Range")
camel_type_DoublePrecisionValue = Class(name="camel::type::DoublePrecisionValue")
camel_type_NegativeInf = Class(name="camel::type::NegativeInf")
camel_type_PositiveInf = Class(name="camel::type::PositiveInf")
camel_type_ValueToIncrease = Class(name="camel::type::ValueToIncrease")
camel_type_StringsValue = Class(name="camel::type::StringsValue")
camel_type_ValueType = Class(name="camel::type::ValueType", is_abstract=True)
camel_type_BooleanValueType = Class(name="camel::type::BooleanValueType")
camel_type_RangeUnion = Class(name="camel::type::RangeUnion")
Range = Class(name="Range")
camel_type_StringValueType = Class(name="camel::type::StringValueType")
camel_unit_Unit = Class(name="camel::unit::Unit", is_abstract=True)
Limit = Class(name="Limit")
camel_unit_UnitModel = Class(name="camel::unit::UnitModel")
camel_unit_CoreUnit = Class(name="camel::unit::CoreUnit")
camel_unit_Dimensionless = Class(name="camel::unit::Dimensionless")
camel_unit_MonetaryUnit = Class(name="camel::unit::MonetaryUnit")
camel_unit_RequestUnit = Class(name="camel::unit::RequestUnit")
camel_unit_StorageUnit = Class(name="camel::unit::StorageUnit")
camel_unit_ThroughputUnit = Class(name="camel::unit::ThroughputUnit")
camel_unit_TimeIntervalUnit = Class(name="camel::unit::TimeIntervalUnit")
camel_unit_TransactionUnit = Class(name="camel::unit::TransactionUnit")

# camel_Model class attributes and methods
camel_Model_name: Property = Property(name="name", type=StringType)
camel_Model_importURI: Property = Property(name="importURI", type=StringType)
camel_Model.attributes={camel_Model_importURI, camel_Model_name}

# camel_CamelModel class attributes and methods

# Model class attributes and methods

# camel_Action class attributes and methods
camel_Action_name: Property = Property(name="name", type=StringType)
camel_Action_type: Property = Property(name="type", type=StringType)
camel_Action.attributes={camel_Action_name, camel_Action_type}

# camel_Application class attributes and methods
camel_Application_name: Property = Property(name="name", type=StringType)
camel_Application_version: Property = Property(name="version", type=StringType)
camel_Application_description: Property = Property(name="description", type=StringType)
camel_Application.attributes={camel_Application_description, camel_Application_version, camel_Application_name}

# ExecutionModel class attributes and methods

# LocationModel class attributes and methods

# MetricModel class attributes and methods

# OrganisationModel class attributes and methods

# ProviderModel class attributes and methods

# RequirementModel class attributes and methods

# ScalabilityModel class attributes and methods

# SecurityModel class attributes and methods

# DeploymentModel class attributes and methods

# TypeModel class attributes and methods

# UnitModel class attributes and methods

# VM class attributes and methods

# Entity class attributes and methods

# VMInstance class attributes and methods

# Communication class attributes and methods

# CommunicationInstance class attributes and methods

# camel_deployment_DeploymentElement class attributes and methods
camel_deployment_DeploymentElement_name: Property = Property(name="name", type=StringType)
camel_deployment_DeploymentElement.attributes={camel_deployment_DeploymentElement_name}

# camel_deployment_DeploymentModel class attributes and methods

# InternalComponent class attributes and methods

# InternalComponentInstance class attributes and methods

# camel_deployment_InternalComponent class attributes and methods
camel_deployment_InternalComponent_version: Property = Property(name="version", type=StringType)
camel_deployment_InternalComponent_m_contains: Method = Method(name="contains", parameters={Parameter(name='ic'), Parameter(name='rc')}, type=BooleanType)
camel_deployment_InternalComponent.attributes={camel_deployment_InternalComponent_version}
camel_deployment_InternalComponent.methods={camel_deployment_InternalComponent_m_contains}

# Component class attributes and methods

# Hosting class attributes and methods

# RequiredCommunication class attributes and methods

# HostingInstance class attributes and methods

# VMRequirementSet class attributes and methods

# camel_deployment_Component class attributes and methods

# DeploymentElement class attributes and methods

# ProvidedCommunication class attributes and methods

# ProvidedHost class attributes and methods

# Configuration class attributes and methods

# LocationRequirement class attributes and methods

# ProviderRequirement class attributes and methods

# QualitativeHardwareRequirement class attributes and methods

# QuantitativeHardwareRequirement class attributes and methods

# OSOrImageRequirement class attributes and methods

# RequiredHost class attributes and methods

# camel_deployment_VM class attributes and methods

# camel_deployment_VMRequirementSet class attributes and methods
camel_deployment_VMRequirementSet_name: Property = Property(name="name", type=StringType)
camel_deployment_VMRequirementSet.attributes={camel_deployment_VMRequirementSet_name}

# camel_deployment_CommunicationPort class attributes and methods
camel_deployment_CommunicationPort_portNumber: Property = Property(name="portNumber", type=IntegerType)
camel_deployment_CommunicationPort.attributes={camel_deployment_CommunicationPort_portNumber}

# camel_deployment_ProvidedCommunication class attributes and methods

# CommunicationPort class attributes and methods

# camel_deployment_RequiredCommunication class attributes and methods
camel_deployment_RequiredCommunication_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
camel_deployment_RequiredCommunication.attributes={camel_deployment_RequiredCommunication_isMandatory}

# camel_deployment_Hosting class attributes and methods

# camel_deployment_HostingPort class attributes and methods

# camel_deployment_ProvidedHost class attributes and methods

# camel_deployment_Configuration class attributes and methods
camel_deployment_Configuration_downloadCommand: Property = Property(name="downloadCommand", type=StringType)
camel_deployment_Configuration_uploadCommand: Property = Property(name="uploadCommand", type=StringType)
camel_deployment_Configuration_installCommand: Property = Property(name="installCommand", type=StringType)
camel_deployment_Configuration_configureCommand: Property = Property(name="configureCommand", type=StringType)
camel_deployment_Configuration_startCommand: Property = Property(name="startCommand", type=StringType)
camel_deployment_Configuration_stopCommand: Property = Property(name="stopCommand", type=StringType)
camel_deployment_Configuration.attributes={camel_deployment_Configuration_downloadCommand, camel_deployment_Configuration_configureCommand, camel_deployment_Configuration_uploadCommand, camel_deployment_Configuration_startCommand, camel_deployment_Configuration_stopCommand, camel_deployment_Configuration_installCommand}

# HostingPort class attributes and methods

# camel_deployment_RequiredHost class attributes and methods

# camel_deployment_Communication class attributes and methods
camel_deployment_Communication_type: Property = Property(name="type", type=StringType)
camel_deployment_Communication.attributes={camel_deployment_Communication_type}

# camel_deployment_InternalComponentInstance class attributes and methods

# ComponentInstance class attributes and methods

# RequiredCommunicationInstance class attributes and methods

# RequiredHostInstance class attributes and methods

# camel_deployment_VMInstance class attributes and methods
camel_deployment_VMInstance_ip: Property = Property(name="ip", type=StringType)
camel_deployment_VMInstance_m_checkDates: Method = Method(name="checkDates", parameters={Parameter(name='vm')}, type=BooleanType)
camel_deployment_VMInstance.attributes={camel_deployment_VMInstance_ip}
camel_deployment_VMInstance.methods={camel_deployment_VMInstance_m_checkDates}

# camel_deployment_ComponentInstance class attributes and methods
camel_deployment_ComponentInstance_instantiatedOn: Property = Property(name="instantiatedOn", type=DateType)
camel_deployment_ComponentInstance_destroyedOn: Property = Property(name="destroyedOn", type=DateType)
camel_deployment_ComponentInstance.attributes={camel_deployment_ComponentInstance_destroyedOn, camel_deployment_ComponentInstance_instantiatedOn}

# ProvidedCommunicationInstance class attributes and methods

# ProvidedHostInstance class attributes and methods

# camel_deployment_CommunicationPortInstance class attributes and methods

# camel_deployment_ProvidedCommunicationInstance class attributes and methods

# CommunicationPortInstance class attributes and methods

# camel_deployment_RequiredCommunicationInstance class attributes and methods

# camel_deployment_HostingInstance class attributes and methods

# camel_deployment_HostingPortInstance class attributes and methods

# camel_deployment_ProvidedHostInstance class attributes and methods

# HostingPortInstance class attributes and methods

# camel_deployment_RequiredHostInstance class attributes and methods

# Attribute class attributes and methods

# SingleValue class attributes and methods

# camel_deployment_CommunicationInstance class attributes and methods

# camel_execution_ExecutionContext class attributes and methods
camel_execution_ExecutionContext_name: Property = Property(name="name", type=StringType)
camel_execution_ExecutionContext_startTime: Property = Property(name="startTime", type=DateType)
camel_execution_ExecutionContext_endTime: Property = Property(name="endTime", type=DateType)
camel_execution_ExecutionContext_totalCost: Property = Property(name="totalCost", type=FloatType)
camel_execution_ExecutionContext.attributes={camel_execution_ExecutionContext_endTime, camel_execution_ExecutionContext_totalCost, camel_execution_ExecutionContext_name, camel_execution_ExecutionContext_startTime}

# execution_camel_Application class attributes and methods

# MonetaryUnit class attributes and methods

# RequirementGroup class attributes and methods

# camel_execution_Measurement class attributes and methods
camel_execution_Measurement_name: Property = Property(name="name", type=StringType)
camel_execution_Measurement_value: Property = Property(name="value", type=FloatType)
camel_execution_Measurement_rawData: Property = Property(name="rawData", type=StringType)
camel_execution_Measurement_measurementTime: Property = Property(name="measurementTime", type=DateType)
camel_execution_Measurement.attributes={camel_execution_Measurement_value, camel_execution_Measurement_name, camel_execution_Measurement_rawData, camel_execution_Measurement_measurementTime}

# camel_execution_ExecutionModel class attributes and methods

# ActionRealisation class attributes and methods

# EventInstance class attributes and methods

# ExecutionContext class attributes and methods

# Measurement class attributes and methods

# SLOAssessment class attributes and methods

# RuleTrigger class attributes and methods

# camel_execution_ActionRealisation class attributes and methods
camel_execution_ActionRealisation_lowLevelActions: Property = Property(name="lowLevelActions", type=StringType)
camel_execution_ActionRealisation_name: Property = Property(name="name", type=StringType)
camel_execution_ActionRealisation_startTime: Property = Property(name="startTime", type=DateType)
camel_execution_ActionRealisation_endTime: Property = Property(name="endTime", type=DateType)
camel_execution_ActionRealisation.attributes={camel_execution_ActionRealisation_name, camel_execution_ActionRealisation_lowLevelActions, camel_execution_ActionRealisation_startTime, camel_execution_ActionRealisation_endTime}

# execution_camel_Action class attributes and methods

# camel_execution_InternalComponentMeasurement class attributes and methods

# camel_execution_CommunicationMeasurement class attributes and methods

# camel_execution_VMMeasurement class attributes and methods

# camel_execution_SLOAssessment class attributes and methods
camel_execution_SLOAssessment_name: Property = Property(name="name", type=StringType)
camel_execution_SLOAssessment_assessment: Property = Property(name="assessment", type=BooleanType)
camel_execution_SLOAssessment_assessmentTime: Property = Property(name="assessmentTime", type=DateType)
camel_execution_SLOAssessment.attributes={camel_execution_SLOAssessment_name, camel_execution_SLOAssessment_assessment, camel_execution_SLOAssessment_assessmentTime}

# MetricInstance class attributes and methods

# ServiceLevelObjective class attributes and methods

# camel_execution_ApplicationMeasurement class attributes and methods

# ScalabilityRule class attributes and methods

# camel_location_LocationModel class attributes and methods

# CloudLocation class attributes and methods

# Country class attributes and methods

# camel_execution_RuleTrigger class attributes and methods
camel_execution_RuleTrigger_name: Property = Property(name="name", type=StringType)
camel_execution_RuleTrigger_trigerringTime: Property = Property(name="trigerringTime", type=DateType)
camel_execution_RuleTrigger.attributes={camel_execution_RuleTrigger_name, camel_execution_RuleTrigger_trigerringTime}

# camel_location_GeographicalRegion class attributes and methods
camel_location_GeographicalRegion_name: Property = Property(name="name", type=StringType)
camel_location_GeographicalRegion_alternativeNames: Property = Property(name="alternativeNames", type=StringType)
camel_location_GeographicalRegion.attributes={camel_location_GeographicalRegion_name, camel_location_GeographicalRegion_alternativeNames}

# camel_location_Country class attributes and methods

# GeographicalRegion class attributes and methods

# camel_location_Location class attributes and methods
camel_location_Location_id: Property = Property(name="id", type=StringType)
camel_location_Location.attributes={camel_location_Location_id}

# camel_location_CloudLocation class attributes and methods
camel_location_CloudLocation_isAssignable: Property = Property(name="isAssignable", type=BooleanType)
camel_location_CloudLocation_m_checkRecursiveness: Method = Method(name="checkRecursiveness", parameters={Parameter(name='cl2'), Parameter(name='cl1')}, type=BooleanType)
camel_location_CloudLocation.attributes={camel_location_CloudLocation_isAssignable}
camel_location_CloudLocation.methods={camel_location_CloudLocation_m_checkRecursiveness}

# Location class attributes and methods

# MetricContext class attributes and methods

# camel_metric_PropertyCondition class attributes and methods

# PropertyContext class attributes and methods

# TimeIntervalUnit class attributes and methods

# camel_metric_MetricInstance class attributes and methods
camel_metric_MetricInstance_name: Property = Property(name="name", type=StringType)
camel_metric_MetricInstance_m_checkRecursiveness: Method = Method(name="checkRecursiveness", parameters={Parameter(name='m1'), Parameter(name='m2')}, type=BooleanType)
camel_metric_MetricInstance.attributes={camel_metric_MetricInstance_name}
camel_metric_MetricInstance.methods={camel_metric_MetricInstance_m_checkRecursiveness}

# camel_metric_Condition class attributes and methods
camel_metric_Condition_name: Property = Property(name="name", type=StringType)
camel_metric_Condition_comparisonOperator: Property = Property(name="comparisonOperator", type=StringType)
camel_metric_Condition_threshold: Property = Property(name="threshold", type=FloatType)
camel_metric_Condition_validity: Property = Property(name="validity", type=DateType)
camel_metric_Condition.attributes={camel_metric_Condition_name, camel_metric_Condition_comparisonOperator, camel_metric_Condition_validity, camel_metric_Condition_threshold}

# camel_metric_MetricCondition class attributes and methods

# Condition class attributes and methods

# MetricObjectBinding class attributes and methods

# camel_metric_CompositeMetricInstance class attributes and methods

# camel_metric_RawMetricInstance class attributes and methods

# Sensor class attributes and methods

# camel_metric_MetricFormulaParameter class attributes and methods
camel_metric_MetricFormulaParameter_name: Property = Property(name="name", type=StringType)
camel_metric_MetricFormulaParameter.attributes={camel_metric_MetricFormulaParameter_name}

# Metric class attributes and methods

# Schedule class attributes and methods

# Window class attributes and methods

# ValueType class attributes and methods

# Unit class attributes and methods

# Property class attributes and methods

# camel_metric_CompositeMetric class attributes and methods
camel_metric_CompositeMetric_m_greaterEqualThanLayer: Method = Method(name="greaterEqualThanLayer", parameters={Parameter(name='l1'), Parameter(name='l2')}, type=BooleanType)
camel_metric_CompositeMetric.methods={camel_metric_CompositeMetric_m_greaterEqualThanLayer}

# camel_metric_MetricFormula class attributes and methods
camel_metric_MetricFormula_function: Property = Property(name="function", type=StringType)
camel_metric_MetricFormula_functionArity: Property = Property(name="functionArity", type=StringType)
camel_metric_MetricFormula_functionPattern: Property = Property(name="functionPattern", type=StringType)
camel_metric_MetricFormula_m_containsMetric: Method = Method(name="containsMetric", parameters={Parameter(name='m')}, type=BooleanType)
camel_metric_MetricFormula_m_hasMetric: Method = Method(name="hasMetric", parameters={}, type=BooleanType)
camel_metric_MetricFormula.attributes={camel_metric_MetricFormula_function, camel_metric_MetricFormula_functionArity, camel_metric_MetricFormula_functionPattern}
camel_metric_MetricFormula.methods={camel_metric_MetricFormula_m_containsMetric, camel_metric_MetricFormula_m_hasMetric}

# MetricFormulaParameter class attributes and methods

# camel_metric_Metric class attributes and methods
camel_metric_Metric_description: Property = Property(name="description", type=StringType)
camel_metric_Metric_valueDirection: Property = Property(name="valueDirection", type=StringType)
camel_metric_Metric_layer: Property = Property(name="layer", type=StringType)
camel_metric_Metric_isVariable: Property = Property(name="isVariable", type=BooleanType)
camel_metric_Metric_m_checkRecursiveness: Method = Method(name="checkRecursiveness", parameters={Parameter(name='mt2'), Parameter(name='mt1')}, type=BooleanType)
camel_metric_Metric.attributes={camel_metric_Metric_valueDirection, camel_metric_Metric_isVariable, camel_metric_Metric_layer, camel_metric_Metric_description}
camel_metric_Metric.methods={camel_metric_Metric_m_checkRecursiveness}

# camel_metric_MetricObjectBinding class attributes and methods
camel_metric_MetricObjectBinding_name: Property = Property(name="name", type=StringType)
camel_metric_MetricObjectBinding.attributes={camel_metric_MetricObjectBinding_name}

# camel_metric_MetricApplicationBinding class attributes and methods

# camel_metric_MetricComponentBinding class attributes and methods

# camel_metric_MetricVMBinding class attributes and methods

# camel_metric_Property class attributes and methods
camel_metric_Property_name: Property = Property(name="name", type=StringType)
camel_metric_Property_description: Property = Property(name="description", type=StringType)
camel_metric_Property_type: Property = Property(name="type", type=StringType)
camel_metric_Property.attributes={camel_metric_Property_description, camel_metric_Property_type, camel_metric_Property_name}

# MetricFormula class attributes and methods

# camel_metric_RawMetric class attributes and methods

# camel_metric_Sensor class attributes and methods
camel_metric_Sensor_name: Property = Property(name="name", type=StringType)
camel_metric_Sensor_configuration: Property = Property(name="configuration", type=StringType)
camel_metric_Sensor_isPush: Property = Property(name="isPush", type=BooleanType)
camel_metric_Sensor.attributes={camel_metric_Sensor_isPush, camel_metric_Sensor_configuration, camel_metric_Sensor_name}

# camel_metric_Window class attributes and methods
camel_metric_Window_name: Property = Property(name="name", type=StringType)
camel_metric_Window_windowType: Property = Property(name="windowType", type=StringType)
camel_metric_Window_sizeType: Property = Property(name="sizeType", type=StringType)
camel_metric_Window_measurementSize: Property = Property(name="measurementSize", type=StringType)
camel_metric_Window_timeSize: Property = Property(name="timeSize", type=StringType)
camel_metric_Window.attributes={camel_metric_Window_windowType, camel_metric_Window_timeSize, camel_metric_Window_sizeType, camel_metric_Window_measurementSize, camel_metric_Window_name}

# camel_metric_Schedule class attributes and methods
camel_metric_Schedule_start: Property = Property(name="start", type=DateType)
camel_metric_Schedule_end: Property = Property(name="end", type=DateType)
camel_metric_Schedule_type: Property = Property(name="type", type=StringType)
camel_metric_Schedule_repetitions: Property = Property(name="repetitions", type=IntegerType)
camel_metric_Schedule_interval: Property = Property(name="interval", type=StringType)
camel_metric_Schedule_name: Property = Property(name="name", type=StringType)
camel_metric_Schedule_m_checkStartEndDates: Method = Method(name="checkStartEndDates", parameters={Parameter(name='this')}, type=BooleanType)
camel_metric_Schedule_m_checkIntervalRepetitions: Method = Method(name="checkIntervalRepetitions", parameters={Parameter(name='s')}, type=BooleanType)
camel_metric_Schedule.attributes={camel_metric_Schedule_type, camel_metric_Schedule_repetitions, camel_metric_Schedule_name, camel_metric_Schedule_interval, camel_metric_Schedule_start, camel_metric_Schedule_end}
camel_metric_Schedule.methods={camel_metric_Schedule_m_checkStartEndDates, camel_metric_Schedule_m_checkIntervalRepetitions}

# metric_camel_Application class attributes and methods

# camel_metric_MetricModel class attributes and methods

# ConditionContext class attributes and methods

# camel_metric_ConditionContext class attributes and methods
camel_metric_ConditionContext_quantifier: Property = Property(name="quantifier", type=StringType)
camel_metric_ConditionContext_minQuantity: Property = Property(name="minQuantity", type=FloatType)
camel_metric_ConditionContext_maxQuantity: Property = Property(name="maxQuantity", type=FloatType)
camel_metric_ConditionContext_isRelative: Property = Property(name="isRelative", type=BooleanType)
camel_metric_ConditionContext_name: Property = Property(name="name", type=StringType)
camel_metric_ConditionContext.attributes={camel_metric_ConditionContext_maxQuantity, camel_metric_ConditionContext_quantifier, camel_metric_ConditionContext_name, camel_metric_ConditionContext_isRelative, camel_metric_ConditionContext_minQuantity}

# camel_metric_CompositeMetricContext class attributes and methods

# camel_metric_RawMetricContext class attributes and methods

# camel_metric_PropertyContext class attributes and methods

# camel_metric_MetricContext class attributes and methods

# DataCenter class attributes and methods

# Role class attributes and methods

# RoleAssignment class attributes and methods

# Permission class attributes and methods

# ResourceFilter class attributes and methods

# camel_organisation_Credentials class attributes and methods

# camel_organisation_CloudCredentials class attributes and methods
camel_organisation_CloudCredentials_name: Property = Property(name="name", type=StringType)
camel_organisation_CloudCredentials_securityGroup: Property = Property(name="securityGroup", type=StringType)
camel_organisation_CloudCredentials_publicSSHKey: Property = Property(name="publicSSHKey", type=StringType)
camel_organisation_CloudCredentials_privateSSHKey: Property = Property(name="privateSSHKey", type=StringType)
camel_organisation_CloudCredentials_username: Property = Property(name="username", type=StringType)
camel_organisation_CloudCredentials_password: Property = Property(name="password", type=StringType)
camel_organisation_CloudCredentials.attributes={camel_organisation_CloudCredentials_publicSSHKey, camel_organisation_CloudCredentials_privateSSHKey, camel_organisation_CloudCredentials_username, camel_organisation_CloudCredentials_password, camel_organisation_CloudCredentials_securityGroup, camel_organisation_CloudCredentials_name}

# Credentials class attributes and methods

# camel_organisation_OrganisationModel class attributes and methods
camel_organisation_OrganisationModel_securityLevel: Property = Property(name="securityLevel", type=StringType)
camel_organisation_OrganisationModel.attributes={camel_organisation_OrganisationModel_securityLevel}

# Organisation class attributes and methods

# CloudProvider class attributes and methods

# ExternalIdentifier class attributes and methods

# User class attributes and methods

# UserGroup class attributes and methods

# SecurityCapability class attributes and methods

# camel_organisation_User class attributes and methods
camel_organisation_User_name: Property = Property(name="name", type=StringType)
camel_organisation_User_email: Property = Property(name="email", type=StringType)
camel_organisation_User_firstName: Property = Property(name="firstName", type=StringType)
camel_organisation_User_lastName: Property = Property(name="lastName", type=StringType)
camel_organisation_User_www: Property = Property(name="www", type=StringType)
camel_organisation_User.attributes={camel_organisation_User_firstName, camel_organisation_User_lastName, camel_organisation_User_name, camel_organisation_User_email, camel_organisation_User_www}

# CloudCredentials class attributes and methods

# PaaSageCredentials class attributes and methods

# camel_organisation_ExternalIdentifier class attributes and methods
camel_organisation_ExternalIdentifier_identifier: Property = Property(name="identifier", type=StringType)
camel_organisation_ExternalIdentifier_description: Property = Property(name="description", type=StringType)
camel_organisation_ExternalIdentifier.attributes={camel_organisation_ExternalIdentifier_identifier, camel_organisation_ExternalIdentifier_description}

# camel_organisation_DataCenter class attributes and methods
camel_organisation_DataCenter_name: Property = Property(name="name", type=StringType)
camel_organisation_DataCenter_codeName: Property = Property(name="codeName", type=StringType)
camel_organisation_DataCenter.attributes={camel_organisation_DataCenter_codeName, camel_organisation_DataCenter_name}

# camel_organisation_Entity class attributes and methods

# camel_organisation_Organisation class attributes and methods
camel_organisation_Organisation_name: Property = Property(name="name", type=StringType)
camel_organisation_Organisation_www: Property = Property(name="www", type=StringType)
camel_organisation_Organisation_postalAddress: Property = Property(name="postalAddress", type=StringType)
camel_organisation_Organisation_email: Property = Property(name="email", type=StringType)
camel_organisation_Organisation.attributes={camel_organisation_Organisation_email, camel_organisation_Organisation_name, camel_organisation_Organisation_www, camel_organisation_Organisation_postalAddress}

# camel_organisation_CloudProvider class attributes and methods
camel_organisation_CloudProvider_PaaS: Property = Property(name="PaaS", type=BooleanType)
camel_organisation_CloudProvider_IaaS: Property = Property(name="IaaS", type=BooleanType)
camel_organisation_CloudProvider_public: Property = Property(name="public", type=BooleanType)
camel_organisation_CloudProvider_SaaS: Property = Property(name="SaaS", type=BooleanType)
camel_organisation_CloudProvider.attributes={camel_organisation_CloudProvider_IaaS, camel_organisation_CloudProvider_SaaS, camel_organisation_CloudProvider_public, camel_organisation_CloudProvider_PaaS}

# camel_organisation_ResourceFilter class attributes and methods
camel_organisation_ResourceFilter_name: Property = Property(name="name", type=StringType)
camel_organisation_ResourceFilter_resourcePattern: Property = Property(name="resourcePattern", type=StringType)
camel_organisation_ResourceFilter.attributes={camel_organisation_ResourceFilter_resourcePattern, camel_organisation_ResourceFilter_name}

# camel_organisation_InformationResourceFilter class attributes and methods
camel_organisation_InformationResourceFilter_informationResourcePath: Property = Property(name="informationResourcePath", type=StringType)
camel_organisation_InformationResourceFilter_everyInformationResource: Property = Property(name="everyInformationResource", type=BooleanType)
camel_organisation_InformationResourceFilter.attributes={camel_organisation_InformationResourceFilter_informationResourcePath, camel_organisation_InformationResourceFilter_everyInformationResource}

# camel_organisation_ServiceResourceFilter class attributes and methods
camel_organisation_ServiceResourceFilter_serviceURL: Property = Property(name="serviceURL", type=StringType)
camel_organisation_ServiceResourceFilter_everyService: Property = Property(name="everyService", type=BooleanType)
camel_organisation_ServiceResourceFilter.attributes={camel_organisation_ServiceResourceFilter_serviceURL, camel_organisation_ServiceResourceFilter_everyService}

# camel_organisation_Role class attributes and methods
camel_organisation_Role_name: Property = Property(name="name", type=StringType)
camel_organisation_Role.attributes={camel_organisation_Role_name}

# camel_organisation_RoleAssignment class attributes and methods
camel_organisation_RoleAssignment_name: Property = Property(name="name", type=StringType)
camel_organisation_RoleAssignment_startTime: Property = Property(name="startTime", type=DateType)
camel_organisation_RoleAssignment_endTime: Property = Property(name="endTime", type=DateType)
camel_organisation_RoleAssignment_assignmentTime: Property = Property(name="assignmentTime", type=DateType)
camel_organisation_RoleAssignment_m_checkAssignedOnDates: Method = Method(name="checkAssignedOnDates", parameters={Parameter(name='this')}, type=BooleanType)
camel_organisation_RoleAssignment_m_checkStartEndDates: Method = Method(name="checkStartEndDates", parameters={Parameter(name='this')}, type=BooleanType)
camel_organisation_RoleAssignment.attributes={camel_organisation_RoleAssignment_startTime, camel_organisation_RoleAssignment_endTime, camel_organisation_RoleAssignment_assignmentTime, camel_organisation_RoleAssignment_name}
camel_organisation_RoleAssignment.methods={camel_organisation_RoleAssignment_m_checkStartEndDates, camel_organisation_RoleAssignment_m_checkAssignedOnDates}

# camel_organisation_Permission class attributes and methods
camel_organisation_Permission_name: Property = Property(name="name", type=StringType)
camel_organisation_Permission_startTime: Property = Property(name="startTime", type=DateType)
camel_organisation_Permission_endTime: Property = Property(name="endTime", type=DateType)
camel_organisation_Permission_action: Property = Property(name="action", type=StringType)
camel_organisation_Permission_m_checkStartEndDates: Method = Method(name="checkStartEndDates", parameters={Parameter(name='this')}, type=BooleanType)
camel_organisation_Permission.attributes={camel_organisation_Permission_action, camel_organisation_Permission_name, camel_organisation_Permission_startTime, camel_organisation_Permission_endTime}
camel_organisation_Permission.methods={camel_organisation_Permission_m_checkStartEndDates}

# camel_provider_ProviderModel class attributes and methods

# Constraint class attributes and methods

# Feature class attributes and methods

# camel_provider_Attribute class attributes and methods
camel_provider_Attribute_name: Property = Property(name="name", type=StringType)
camel_provider_Attribute_unitType: Property = Property(name="unitType", type=StringType)
camel_provider_Attribute_m_checkValue: Method = Method(name="checkValue", parameters={Parameter(name='v'), Parameter(name='diff')}, type=BooleanType)
camel_provider_Attribute.attributes={camel_provider_Attribute_unitType, camel_provider_Attribute_name}
camel_provider_Attribute.methods={camel_provider_Attribute_m_checkValue}

# camel_organisation_UserGroup class attributes and methods
camel_organisation_UserGroup_name: Property = Property(name="name", type=StringType)
camel_organisation_UserGroup.attributes={camel_organisation_UserGroup_name}

# camel_organisation_PaaSageCredentials class attributes and methods
camel_organisation_PaaSageCredentials_password: Property = Property(name="password", type=StringType)
camel_organisation_PaaSageCredentials.attributes={camel_organisation_PaaSageCredentials_password}

# camel_provider_FeatCardinality class attributes and methods
camel_provider_FeatCardinality_value: Property = Property(name="value", type=IntegerType)
camel_provider_FeatCardinality.attributes={camel_provider_FeatCardinality_value}

# Cardinality class attributes and methods

# camel_provider_GroupCardinality class attributes and methods

# camel_provider_Clone class attributes and methods
camel_provider_Clone_name: Property = Property(name="name", type=StringType)
camel_provider_Clone.attributes={camel_provider_Clone_name}

# Clone class attributes and methods

# camel_provider_Constraint class attributes and methods
camel_provider_Constraint_name: Property = Property(name="name", type=StringType)
camel_provider_Constraint.attributes={camel_provider_Constraint_name}

# camel_provider_AttributeConstraint class attributes and methods
camel_provider_AttributeConstraint_name: Property = Property(name="name", type=StringType)
camel_provider_AttributeConstraint.attributes={camel_provider_AttributeConstraint_name}

# camel_provider_Cardinality class attributes and methods
camel_provider_Cardinality_cardinalityMin: Property = Property(name="cardinalityMin", type=IntegerType)
camel_provider_Cardinality_cardinalityMax: Property = Property(name="cardinalityMax", type=IntegerType)
camel_provider_Cardinality.attributes={camel_provider_Cardinality_cardinalityMin, camel_provider_Cardinality_cardinalityMax}

# Scope class attributes and methods

# FeatCardinality class attributes and methods

# camel_provider_Functional class attributes and methods
camel_provider_Functional_type: Property = Property(name="type", type=StringType)
camel_provider_Functional_order: Property = Property(name="order", type=IntegerType)
camel_provider_Functional_value: Property = Property(name="value", type=IntegerType)
camel_provider_Functional.attributes={camel_provider_Functional_type, camel_provider_Functional_order, camel_provider_Functional_value}

# Requires class attributes and methods

# camel_provider_Feature class attributes and methods
camel_provider_Feature_name: Property = Property(name="name", type=StringType)
camel_provider_Feature.attributes={camel_provider_Feature_name}

# AttributeConstraint class attributes and methods

# camel_provider_Excludes class attributes and methods

# camel_provider_Implies class attributes and methods

# camel_provider_Requires class attributes and methods

# camel_provider_Exclusive class attributes and methods

# Alternative class attributes and methods

# camel_provider_Scope class attributes and methods

# camel_provider_Instance class attributes and methods

# camel_provider_Product class attributes and methods

# camel_requirement_RequirementModel class attributes and methods

# Requirement class attributes and methods

# camel_requirement_Requirement class attributes and methods
camel_requirement_Requirement_name: Property = Property(name="name", type=StringType)
camel_requirement_Requirement.attributes={camel_requirement_Requirement_name}

# camel_requirement_RequirementGroup class attributes and methods
camel_requirement_RequirementGroup_requirementOperator: Property = Property(name="requirementOperator", type=StringType)
camel_requirement_RequirementGroup_m_checkRecursiveness: Method = Method(name="checkRecursiveness", parameters={Parameter(name='context'), Parameter(name='rg1'), Parameter(name='r'), Parameter(name='resources')}, type=BooleanType)
camel_requirement_RequirementGroup.attributes={camel_requirement_RequirementGroup_requirementOperator}
camel_requirement_RequirementGroup.methods={camel_requirement_RequirementGroup_m_checkRecursiveness}

# camel_provider_Alternative class attributes and methods

# GroupCardinality class attributes and methods

# camel_requirement_HardRequirement class attributes and methods

# camel_requirement_SoftRequirement class attributes and methods
camel_requirement_SoftRequirement_priority: Property = Property(name="priority", type=FloatType)
camel_requirement_SoftRequirement.attributes={camel_requirement_SoftRequirement_priority}

# requirement_camel_Application class attributes and methods

# camel_requirement_ServiceLevelObjective class attributes and methods

# HardRequirement class attributes and methods

# camel_requirement_OptimisationRequirement class attributes and methods
camel_requirement_OptimisationRequirement_optimisationFunction: Property = Property(name="optimisationFunction", type=StringType)
camel_requirement_OptimisationRequirement.attributes={camel_requirement_OptimisationRequirement_optimisationFunction}

# SoftRequirement class attributes and methods

# camel_requirement_HardwareRequirement class attributes and methods

# camel_requirement_QualitativeHardwareRequirement class attributes and methods
camel_requirement_QualitativeHardwareRequirement_minBenchmark: Property = Property(name="minBenchmark", type=FloatType)
camel_requirement_QualitativeHardwareRequirement_maxBenchmark: Property = Property(name="maxBenchmark", type=FloatType)
camel_requirement_QualitativeHardwareRequirement.attributes={camel_requirement_QualitativeHardwareRequirement_maxBenchmark, camel_requirement_QualitativeHardwareRequirement_minBenchmark}

# HardwareRequirement class attributes and methods

# camel_requirement_QuantitativeHardwareRequirement class attributes and methods
camel_requirement_QuantitativeHardwareRequirement_minRAM: Property = Property(name="minRAM", type=IntegerType)
camel_requirement_QuantitativeHardwareRequirement_maxRAM: Property = Property(name="maxRAM", type=IntegerType)
camel_requirement_QuantitativeHardwareRequirement_minStorage: Property = Property(name="minStorage", type=IntegerType)
camel_requirement_QuantitativeHardwareRequirement_maxStorage: Property = Property(name="maxStorage", type=IntegerType)
camel_requirement_QuantitativeHardwareRequirement_minCPU: Property = Property(name="minCPU", type=FloatType)
camel_requirement_QuantitativeHardwareRequirement_maxCPU: Property = Property(name="maxCPU", type=FloatType)
camel_requirement_QuantitativeHardwareRequirement_minCores: Property = Property(name="minCores", type=IntegerType)
camel_requirement_QuantitativeHardwareRequirement_maxCores: Property = Property(name="maxCores", type=IntegerType)
camel_requirement_QuantitativeHardwareRequirement.attributes={camel_requirement_QuantitativeHardwareRequirement_minCores, camel_requirement_QuantitativeHardwareRequirement_maxRAM, camel_requirement_QuantitativeHardwareRequirement_minCPU, camel_requirement_QuantitativeHardwareRequirement_maxCores, camel_requirement_QuantitativeHardwareRequirement_maxCPU, camel_requirement_QuantitativeHardwareRequirement_minStorage, camel_requirement_QuantitativeHardwareRequirement_maxStorage, camel_requirement_QuantitativeHardwareRequirement_minRAM}

# camel_requirement_ProviderRequirement class attributes and methods

# camel_requirement_OSOrImageRequirement class attributes and methods

# camel_requirement_OSRequirement class attributes and methods
camel_requirement_OSRequirement_os: Property = Property(name="os", type=StringType)
camel_requirement_OSRequirement_is64os: Property = Property(name="is64os", type=BooleanType)
camel_requirement_OSRequirement.attributes={camel_requirement_OSRequirement_os, camel_requirement_OSRequirement_is64os}

# camel_requirement_SecurityRequirement class attributes and methods

# SecurityControl class attributes and methods

# camel_requirement_LocationRequirement class attributes and methods

# camel_requirement_ScaleRequirement class attributes and methods

# camel_requirement_HorizontalScaleRequirement class attributes and methods
camel_requirement_HorizontalScaleRequirement_minInstances: Property = Property(name="minInstances", type=IntegerType)
camel_requirement_HorizontalScaleRequirement_maxInstances: Property = Property(name="maxInstances", type=IntegerType)
camel_requirement_HorizontalScaleRequirement.attributes={camel_requirement_HorizontalScaleRequirement_maxInstances, camel_requirement_HorizontalScaleRequirement_minInstances}

# camel_requirement_ImageRequirement class attributes and methods
camel_requirement_ImageRequirement_imageId: Property = Property(name="imageId", type=StringType)
camel_requirement_ImageRequirement.attributes={camel_requirement_ImageRequirement_imageId}

# camel_requirement_VerticalScaleRequirement class attributes and methods
camel_requirement_VerticalScaleRequirement_minCPU: Property = Property(name="minCPU", type=FloatType)
camel_requirement_VerticalScaleRequirement_maxCPU: Property = Property(name="maxCPU", type=FloatType)
camel_requirement_VerticalScaleRequirement_minCores: Property = Property(name="minCores", type=IntegerType)
camel_requirement_VerticalScaleRequirement_maxCores: Property = Property(name="maxCores", type=IntegerType)
camel_requirement_VerticalScaleRequirement_minRAM: Property = Property(name="minRAM", type=IntegerType)
camel_requirement_VerticalScaleRequirement_maxRAM: Property = Property(name="maxRAM", type=IntegerType)
camel_requirement_VerticalScaleRequirement_minStorage: Property = Property(name="minStorage", type=IntegerType)
camel_requirement_VerticalScaleRequirement_maxStorage: Property = Property(name="maxStorage", type=IntegerType)
camel_requirement_VerticalScaleRequirement.attributes={camel_requirement_VerticalScaleRequirement_minStorage, camel_requirement_VerticalScaleRequirement_minRAM, camel_requirement_VerticalScaleRequirement_maxRAM, camel_requirement_VerticalScaleRequirement_maxCores, camel_requirement_VerticalScaleRequirement_maxCPU, camel_requirement_VerticalScaleRequirement_maxStorage, camel_requirement_VerticalScaleRequirement_minCores, camel_requirement_VerticalScaleRequirement_minCPU}

# ScaleRequirement class attributes and methods

# camel_scalability_ScalabilityModel class attributes and methods

# Event class attributes and methods

# ScalingAction class attributes and methods

# camel_scalability_Event class attributes and methods
camel_scalability_Event_name: Property = Property(name="name", type=StringType)
camel_scalability_Event.attributes={camel_scalability_Event_name}

# camel_scalability_EventPattern class attributes and methods
camel_scalability_EventPattern_m_includesEvent: Method = Method(name="includesEvent", parameters={Parameter(name='e')}, type=BooleanType)
camel_scalability_EventPattern_m_includesLeftEvent: Method = Method(name="includesLeftEvent", parameters={Parameter(name='e')}, type=BooleanType)
camel_scalability_EventPattern_m_includesRightEvent: Method = Method(name="includesRightEvent", parameters={Parameter(name='e')}, type=BooleanType)
camel_scalability_EventPattern.methods={camel_scalability_EventPattern_m_includesRightEvent, camel_scalability_EventPattern_m_includesLeftEvent, camel_scalability_EventPattern_m_includesEvent}

# EventPattern class attributes and methods

# Timer class attributes and methods

# camel_scalability_UnaryEventPattern class attributes and methods
camel_scalability_UnaryEventPattern_occurrenceNum: Property = Property(name="occurrenceNum", type=IntegerType)
camel_scalability_UnaryEventPattern_operator: Property = Property(name="operator", type=StringType)
camel_scalability_UnaryEventPattern.attributes={camel_scalability_UnaryEventPattern_occurrenceNum, camel_scalability_UnaryEventPattern_operator}

# camel_scalability_BinaryEventPattern class attributes and methods
camel_scalability_BinaryEventPattern_lowerOccurrenceBound: Property = Property(name="lowerOccurrenceBound", type=IntegerType)
camel_scalability_BinaryEventPattern_upperOccurrenceBound: Property = Property(name="upperOccurrenceBound", type=IntegerType)
camel_scalability_BinaryEventPattern_operator: Property = Property(name="operator", type=StringType)
camel_scalability_BinaryEventPattern.attributes={camel_scalability_BinaryEventPattern_lowerOccurrenceBound, camel_scalability_BinaryEventPattern_upperOccurrenceBound, camel_scalability_BinaryEventPattern_operator}

# MetricCondition class attributes and methods

# camel_scalability_EventInstance class attributes and methods
camel_scalability_EventInstance_name: Property = Property(name="name", type=StringType)
camel_scalability_EventInstance_status: Property = Property(name="status", type=StringType)
camel_scalability_EventInstance_layer: Property = Property(name="layer", type=StringType)
camel_scalability_EventInstance_m_equalLayer: Method = Method(name="equalLayer", parameters={Parameter(name='l1'), Parameter(name='l2')}, type=BooleanType)
camel_scalability_EventInstance.attributes={camel_scalability_EventInstance_name, camel_scalability_EventInstance_status, camel_scalability_EventInstance_layer}
camel_scalability_EventInstance.methods={camel_scalability_EventInstance_m_equalLayer}

# camel_scalability_SimpleEvent class attributes and methods

# camel_scalability_FunctionalEvent class attributes and methods
camel_scalability_FunctionalEvent_functionalType: Property = Property(name="functionalType", type=StringType)
camel_scalability_FunctionalEvent.attributes={camel_scalability_FunctionalEvent_functionalType}

# SimpleEvent class attributes and methods

# camel_scalability_NonFunctionalEvent class attributes and methods
camel_scalability_NonFunctionalEvent_isViolation: Property = Property(name="isViolation", type=BooleanType)
camel_scalability_NonFunctionalEvent.attributes={camel_scalability_NonFunctionalEvent_isViolation}

# scalability_camel_Action class attributes and methods

# camel_scalability_ScalingAction class attributes and methods

# Action class attributes and methods

# camel_scalability_HorizontalScalingAction class attributes and methods
camel_scalability_HorizontalScalingAction_count: Property = Property(name="count", type=IntegerType)
camel_scalability_HorizontalScalingAction.attributes={camel_scalability_HorizontalScalingAction_count}

# camel_scalability_ScalabilityRule class attributes and methods
camel_scalability_ScalabilityRule_name: Property = Property(name="name", type=StringType)
camel_scalability_ScalabilityRule.attributes={camel_scalability_ScalabilityRule_name}

# camel_scalability_Timer class attributes and methods
camel_scalability_Timer_name: Property = Property(name="name", type=StringType)
camel_scalability_Timer_type: Property = Property(name="type", type=StringType)
camel_scalability_Timer_timeValue: Property = Property(name="timeValue", type=IntegerType)
camel_scalability_Timer_maxOccurrenceNum: Property = Property(name="maxOccurrenceNum", type=IntegerType)
camel_scalability_Timer.attributes={camel_scalability_Timer_name, camel_scalability_Timer_timeValue, camel_scalability_Timer_maxOccurrenceNum, camel_scalability_Timer_type}

# camel_scalability_VerticalScalingAction class attributes and methods
camel_scalability_VerticalScalingAction_memoryUpdate: Property = Property(name="memoryUpdate", type=IntegerType)
camel_scalability_VerticalScalingAction_CPUUpdate: Property = Property(name="CPUUpdate", type=FloatType)
camel_scalability_VerticalScalingAction_coreUpdate: Property = Property(name="coreUpdate", type=IntegerType)
camel_scalability_VerticalScalingAction_storageUpdate: Property = Property(name="storageUpdate", type=IntegerType)
camel_scalability_VerticalScalingAction_ioUpdate: Property = Property(name="ioUpdate", type=IntegerType)
camel_scalability_VerticalScalingAction_networkUpdate: Property = Property(name="networkUpdate", type=IntegerType)
camel_scalability_VerticalScalingAction.attributes={camel_scalability_VerticalScalingAction_ioUpdate, camel_scalability_VerticalScalingAction_networkUpdate, camel_scalability_VerticalScalingAction_memoryUpdate, camel_scalability_VerticalScalingAction_coreUpdate, camel_scalability_VerticalScalingAction_storageUpdate, camel_scalability_VerticalScalingAction_CPUUpdate}

# camel_security_SecurityModel class attributes and methods

# SecurityRequirement class attributes and methods

# SecurityProperty class attributes and methods

# RawSecurityMetric class attributes and methods

# CompositeSecurityMetricInstance class attributes and methods

# SecurityDomain class attributes and methods

# SecuritySLO class attributes and methods

# camel_security_SecurityDomain class attributes and methods
camel_security_SecurityDomain_id: Property = Property(name="id", type=StringType)
camel_security_SecurityDomain_name: Property = Property(name="name", type=StringType)
camel_security_SecurityDomain.attributes={camel_security_SecurityDomain_id, camel_security_SecurityDomain_name}

# CompositeSecurityMetric class attributes and methods

# RawSecurityMetricInstance class attributes and methods

# camel_security_RawSecurityMetricInstance class attributes and methods

# RawMetricInstance class attributes and methods

# camel_security_RawSecurityMetric class attributes and methods

# RawMetric class attributes and methods

# camel_security_SecurityProperty class attributes and methods

# camel_security_Certifiable class attributes and methods

# camel_security_SecuritySLO class attributes and methods

# camel_security_SecurityCapability class attributes and methods
camel_security_SecurityCapability_name: Property = Property(name="name", type=StringType)
camel_security_SecurityCapability.attributes={camel_security_SecurityCapability_name}

# camel_security_SecurityControl class attributes and methods
camel_security_SecurityControl_name: Property = Property(name="name", type=StringType)
camel_security_SecurityControl_specification: Property = Property(name="specification", type=StringType)
camel_security_SecurityControl.attributes={camel_security_SecurityControl_name, camel_security_SecurityControl_specification}

# camel_type_TypeModel class attributes and methods

# camel_type_Limit class attributes and methods
camel_type_Limit_included: Property = Property(name="included", type=BooleanType)
camel_type_Limit.attributes={camel_type_Limit_included}

# NumericValue class attributes and methods

# camel_type_SingleValue class attributes and methods
camel_type_SingleValue_m_valueEquals: Method = Method(name="valueEquals", parameters={Parameter(name='v')}, type=BooleanType)
camel_type_SingleValue.methods={camel_type_SingleValue_m_valueEquals}

# camel_type_BoolValue class attributes and methods
camel_type_BoolValue_value: Property = Property(name="value", type=BooleanType)
camel_type_BoolValue.attributes={camel_type_BoolValue_value}

# camel_type_EnumerateValue class attributes and methods
camel_type_EnumerateValue_name: Property = Property(name="name", type=StringType)
camel_type_EnumerateValue_value: Property = Property(name="value", type=IntegerType)
camel_type_EnumerateValue.attributes={camel_type_EnumerateValue_name, camel_type_EnumerateValue_value}

# camel_type_NumericValue class attributes and methods

# camel_type_IntegerValue class attributes and methods
camel_type_IntegerValue_value: Property = Property(name="value", type=IntegerType)
camel_type_IntegerValue.attributes={camel_type_IntegerValue_value}

# camel_type_FloatsValue class attributes and methods
camel_type_FloatsValue_value: Property = Property(name="value", type=FloatType)
camel_type_FloatsValue.attributes={camel_type_FloatsValue_value}

# camel_security_CompositeSecurityMetric class attributes and methods

# CompositeMetric class attributes and methods

# camel_security_CompositeSecurityMetricInstance class attributes and methods

# CompositeMetricInstance class attributes and methods

# camel_type_Enumeration class attributes and methods
camel_type_Enumeration_m_includesName: Method = Method(name="includesName", parameters={Parameter(name='name')}, type=BooleanType)
camel_type_Enumeration_m_includesValue: Method = Method(name="includesValue", parameters={Parameter(name='value')}, type=BooleanType)
camel_type_Enumeration.methods={camel_type_Enumeration_m_includesName, camel_type_Enumeration_m_includesValue}

# EnumerateValue class attributes and methods

# camel_type_List class attributes and methods
camel_type_List_primitiveType: Property = Property(name="primitiveType", type=StringType)
camel_type_List_m_includesValue: Method = Method(name="includesValue", parameters={Parameter(name='v')}, type=BooleanType)
camel_type_List_m_checkValueType: Method = Method(name="checkValueType", parameters={Parameter(name='p')}, type=BooleanType)
camel_type_List.attributes={camel_type_List_primitiveType}
camel_type_List.methods={camel_type_List_m_includesValue, camel_type_List_m_checkValueType}

# camel_type_Range class attributes and methods
camel_type_Range_primitiveType: Property = Property(name="primitiveType", type=StringType)
camel_type_Range_m_checkType: Method = Method(name="checkType", parameters={Parameter(name='lower'), Parameter(name='type'), Parameter(name='l')}, type=BooleanType)
camel_type_Range_m_includesValue: Method = Method(name="includesValue", parameters={Parameter(name='n')}, type=BooleanType)
camel_type_Range.attributes={camel_type_Range_primitiveType}
camel_type_Range.methods={camel_type_Range_m_checkType, camel_type_Range_m_includesValue}

# camel_type_DoublePrecisionValue class attributes and methods
camel_type_DoublePrecisionValue_value: Property = Property(name="value", type=FloatType)
camel_type_DoublePrecisionValue.attributes={camel_type_DoublePrecisionValue_value}

# camel_type_NegativeInf class attributes and methods

# camel_type_PositiveInf class attributes and methods

# camel_type_ValueToIncrease class attributes and methods

# camel_type_StringsValue class attributes and methods
camel_type_StringsValue_value: Property = Property(name="value", type=StringType)
camel_type_StringsValue.attributes={camel_type_StringsValue_value}

# camel_type_ValueType class attributes and methods
camel_type_ValueType_name: Property = Property(name="name", type=StringType)
camel_type_ValueType.attributes={camel_type_ValueType_name}

# camel_type_BooleanValueType class attributes and methods
camel_type_BooleanValueType_primitiveType: Property = Property(name="primitiveType", type=StringType)
camel_type_BooleanValueType.attributes={camel_type_BooleanValueType_primitiveType}

# camel_type_RangeUnion class attributes and methods
camel_type_RangeUnion_primitiveType: Property = Property(name="primitiveType", type=StringType)
camel_type_RangeUnion_m_includesValue: Method = Method(name="includesValue", parameters={Parameter(name='n')}, type=BooleanType)
camel_type_RangeUnion_m_invalidRangeSequence: Method = Method(name="invalidRangeSequence", parameters={Parameter(name='ru')}, type=BooleanType)
camel_type_RangeUnion.attributes={camel_type_RangeUnion_primitiveType}
camel_type_RangeUnion.methods={camel_type_RangeUnion_m_includesValue, camel_type_RangeUnion_m_invalidRangeSequence}

# Range class attributes and methods

# camel_type_StringValueType class attributes and methods
camel_type_StringValueType_primitiveType: Property = Property(name="primitiveType", type=StringType)
camel_type_StringValueType.attributes={camel_type_StringValueType_primitiveType}

# camel_unit_Unit class attributes and methods
camel_unit_Unit_name: Property = Property(name="name", type=StringType)
camel_unit_Unit_unit: Property = Property(name="unit", type=StringType)
camel_unit_Unit_m_checkUnit: Method = Method(name="checkUnit", parameters={}, type=BooleanType)
camel_unit_Unit.attributes={camel_unit_Unit_unit, camel_unit_Unit_name}
camel_unit_Unit.methods={camel_unit_Unit_m_checkUnit}

# Limit class attributes and methods

# camel_unit_UnitModel class attributes and methods

# camel_unit_CoreUnit class attributes and methods

# camel_unit_Dimensionless class attributes and methods

# camel_unit_MonetaryUnit class attributes and methods

# camel_unit_RequestUnit class attributes and methods

# camel_unit_StorageUnit class attributes and methods

# camel_unit_ThroughputUnit class attributes and methods

# camel_unit_TimeIntervalUnit class attributes and methods

# camel_unit_TransactionUnit class attributes and methods

# Relationships
actions0: BinaryAssociation = BinaryAssociation(
    name="actions0",
    ends={
        Property(name="camel_Action", type=camel_CamelModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_CamelModel", type=camel_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executionModels5: BinaryAssociation = BinaryAssociation(
    name="executionModels5",
    ends={
        Property(name="ExecutionModel", type=camel_CamelModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_CamelModel6", type=ExecutionModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locationModels7: BinaryAssociation = BinaryAssociation(
    name="locationModels7",
    ends={
        Property(name="LocationModel", type=camel_CamelModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_CamelModel8", type=LocationModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricModels9: BinaryAssociation = BinaryAssociation(
    name="metricModels9",
    ends={
        Property(name="MetricModel", type=camel_CamelModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_CamelModel10", type=MetricModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
organisationModels11: BinaryAssociation = BinaryAssociation(
    name="organisationModels11",
    ends={
        Property(name="OrganisationModel", type=camel_CamelModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_CamelModel12", type=OrganisationModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providerModels13: BinaryAssociation = BinaryAssociation(
    name="providerModels13",
    ends={
        Property(name="ProviderModel", type=camel_CamelModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_CamelModel14", type=ProviderModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requirementModels15: BinaryAssociation = BinaryAssociation(
    name="requirementModels15",
    ends={
        Property(name="RequirementModel", type=camel_CamelModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_CamelModel16", type=RequirementModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applications1: BinaryAssociation = BinaryAssociation(
    name="applications1",
    ends={
        Property(name="camel_Application", type=camel_CamelModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_CamelModel2", type=camel_Application, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scalabilityModels17: BinaryAssociation = BinaryAssociation(
    name="scalabilityModels17",
    ends={
        Property(name="ScalabilityModel", type=camel_CamelModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_CamelModel18", type=ScalabilityModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
securityModels19: BinaryAssociation = BinaryAssociation(
    name="securityModels19",
    ends={
        Property(name="SecurityModel", type=camel_CamelModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_CamelModel20", type=SecurityModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deploymentModels3: BinaryAssociation = BinaryAssociation(
    name="deploymentModels3",
    ends={
        Property(name="DeploymentModel", type=camel_CamelModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_CamelModel4", type=DeploymentModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unitModels23: BinaryAssociation = BinaryAssociation(
    name="unitModels23",
    ends={
        Property(name="UnitModel", type=camel_CamelModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_CamelModel24", type=UnitModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeModels21: BinaryAssociation = BinaryAssociation(
    name="typeModels21",
    ends={
        Property(name="TypeModel", type=camel_CamelModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_CamelModel22", type=TypeModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vms33: BinaryAssociation = BinaryAssociation(
    name="vms33",
    ends={
        Property(name="VM", type=camel_deployment_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_DeploymentModel34", type=VM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner25: BinaryAssociation = BinaryAssociation(
    name="owner25",
    ends={
        Property(name="Entity", type=camel_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_Application26", type=Entity, multiplicity=Multiplicity(1, 1))
    }
)
vmInstances35: BinaryAssociation = BinaryAssociation(
    name="vmInstances35",
    ends={
        Property(name="VMInstance", type=camel_deployment_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_DeploymentModel36", type=VMInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
communications37: BinaryAssociation = BinaryAssociation(
    name="communications37",
    ends={
        Property(name="Communication", type=camel_deployment_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_DeploymentModel38", type=Communication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deploymentModels27: BinaryAssociation = BinaryAssociation(
    name="deploymentModels27",
    ends={
        Property(name="DeploymentModel29", type=camel_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_Application28", type=DeploymentModel, multiplicity=Multiplicity(0, 9999))
    }
)
communicationInstances39: BinaryAssociation = BinaryAssociation(
    name="communicationInstances39",
    ends={
        Property(name="CommunicationInstance", type=camel_deployment_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_DeploymentModel40", type=CommunicationInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
internalComponents30: BinaryAssociation = BinaryAssociation(
    name="internalComponents30",
    ends={
        Property(name="InternalComponent", type=camel_deployment_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_DeploymentModel", type=InternalComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
internalComponentInstances31: BinaryAssociation = BinaryAssociation(
    name="internalComponentInstances31",
    ends={
        Property(name="InternalComponentInstance", type=camel_deployment_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_DeploymentModel32", type=InternalComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compositeInternalComponents55: BinaryAssociation = BinaryAssociation(
    name="compositeInternalComponents55",
    ends={
        Property(name="InternalComponent56", type=camel_deployment_InternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_InternalComponent", type=InternalComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hostings41: BinaryAssociation = BinaryAssociation(
    name="hostings41",
    ends={
        Property(name="Hosting", type=camel_deployment_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_DeploymentModel42", type=Hosting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCommunications57: BinaryAssociation = BinaryAssociation(
    name="requiredCommunications57",
    ends={
        Property(name="RequiredCommunication", type=camel_deployment_InternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_InternalComponent58", type=RequiredCommunication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hostingInstances43: BinaryAssociation = BinaryAssociation(
    name="hostingInstances43",
    ends={
        Property(name="HostingInstance", type=camel_deployment_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_DeploymentModel44", type=HostingInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vmRequirementSets45: BinaryAssociation = BinaryAssociation(
    name="vmRequirementSets45",
    ends={
        Property(name="VMRequirementSet", type=camel_deployment_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_DeploymentModel46", type=VMRequirementSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalVMRequirementSet47: BinaryAssociation = BinaryAssociation(
    name="globalVMRequirementSet47",
    ends={
        Property(name="VMRequirementSet49", type=camel_deployment_DeploymentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_DeploymentModel48", type=VMRequirementSet, multiplicity=Multiplicity(0, 1))
    }
)
providedCommunications50: BinaryAssociation = BinaryAssociation(
    name="providedCommunications50",
    ends={
        Property(name="ProvidedCommunication", type=camel_deployment_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_Component", type=ProvidedCommunication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedHosts51: BinaryAssociation = BinaryAssociation(
    name="providedHosts51",
    ends={
        Property(name="ProvidedHost", type=camel_deployment_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_Component52", type=ProvidedHost, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configurations53: BinaryAssociation = BinaryAssociation(
    name="configurations53",
    ends={
        Property(name="Configuration", type=camel_deployment_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_Component54", type=Configuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locationRequirement63: BinaryAssociation = BinaryAssociation(
    name="locationRequirement63",
    ends={
        Property(name="LocationRequirement", type=camel_deployment_VMRequirementSet, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_VMRequirementSet", type=LocationRequirement, multiplicity=Multiplicity(0, 1))
    }
)
providerRequirement64: BinaryAssociation = BinaryAssociation(
    name="providerRequirement64",
    ends={
        Property(name="ProviderRequirement", type=camel_deployment_VMRequirementSet, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_VMRequirementSet65", type=ProviderRequirement, multiplicity=Multiplicity(0, 1))
    }
)
qualitativeHardwareRequirement66: BinaryAssociation = BinaryAssociation(
    name="qualitativeHardwareRequirement66",
    ends={
        Property(name="QualitativeHardwareRequirement", type=camel_deployment_VMRequirementSet, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_VMRequirementSet67", type=QualitativeHardwareRequirement, multiplicity=Multiplicity(0, 1))
    }
)
quantitativeHardwareRequirement68: BinaryAssociation = BinaryAssociation(
    name="quantitativeHardwareRequirement68",
    ends={
        Property(name="QuantitativeHardwareRequirement", type=camel_deployment_VMRequirementSet, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_VMRequirementSet69", type=QuantitativeHardwareRequirement, multiplicity=Multiplicity(0, 1))
    }
)
requiredHost59: BinaryAssociation = BinaryAssociation(
    name="requiredHost59",
    ends={
        Property(name="RequiredHost", type=camel_deployment_InternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_InternalComponent60", type=RequiredHost, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vmRequirementSet61: BinaryAssociation = BinaryAssociation(
    name="vmRequirementSet61",
    ends={
        Property(name="VMRequirementSet62", type=camel_deployment_VM, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_VM", type=VMRequirementSet, multiplicity=Multiplicity(0, 1))
    }
)
requiredPortConfiguration80: BinaryAssociation = BinaryAssociation(
    name="requiredPortConfiguration80",
    ends={
        Property(name="Configuration82", type=camel_deployment_Communication, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_Communication81", type=Configuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
providedHost83: BinaryAssociation = BinaryAssociation(
    name="providedHost83",
    ends={
        Property(name="ProvidedHost84", type=camel_deployment_Hosting, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_Hosting", type=ProvidedHost, multiplicity=Multiplicity(1, 1))
    }
)
requiredHost85: BinaryAssociation = BinaryAssociation(
    name="requiredHost85",
    ends={
        Property(name="RequiredHost87", type=camel_deployment_Hosting, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_Hosting86", type=RequiredHost, multiplicity=Multiplicity(1, 1))
    }
)
providedHostConfiguration88: BinaryAssociation = BinaryAssociation(
    name="providedHostConfiguration88",
    ends={
        Property(name="Configuration90", type=camel_deployment_Hosting, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_Hosting89", type=Configuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredHostConfiguration91: BinaryAssociation = BinaryAssociation(
    name="requiredHostConfiguration91",
    ends={
        Property(name="Configuration93", type=camel_deployment_Hosting, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_Hosting92", type=Configuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
osOrImageRequirement70: BinaryAssociation = BinaryAssociation(
    name="osOrImageRequirement70",
    ends={
        Property(name="OSOrImageRequirement", type=camel_deployment_VMRequirementSet, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_VMRequirementSet71", type=OSOrImageRequirement, multiplicity=Multiplicity(0, 1))
    }
)
providedCommunication72: BinaryAssociation = BinaryAssociation(
    name="providedCommunication72",
    ends={
        Property(name="ProvidedCommunication73", type=camel_deployment_Communication, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_Communication", type=ProvidedCommunication, multiplicity=Multiplicity(1, 1))
    }
)
requiredCommunication74: BinaryAssociation = BinaryAssociation(
    name="requiredCommunication74",
    ends={
        Property(name="RequiredCommunication76", type=camel_deployment_Communication, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_Communication75", type=RequiredCommunication, multiplicity=Multiplicity(1, 1))
    }
)
providedPortConfiguration77: BinaryAssociation = BinaryAssociation(
    name="providedPortConfiguration77",
    ends={
        Property(name="Configuration79", type=camel_deployment_Communication, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_Communication78", type=Configuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredCommunicationInstances99: BinaryAssociation = BinaryAssociation(
    name="requiredCommunicationInstances99",
    ends={
        Property(name="RequiredCommunicationInstance", type=camel_deployment_InternalComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_InternalComponentInstance", type=RequiredCommunicationInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredHostInstance100: BinaryAssociation = BinaryAssociation(
    name="requiredHostInstance100",
    ends={
        Property(name="RequiredHostInstance", type=camel_deployment_InternalComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_InternalComponentInstance101", type=RequiredHostInstance, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type94: BinaryAssociation = BinaryAssociation(
    name="type94",
    ends={
        Property(name="Component", type=camel_deployment_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_ComponentInstance", type=Component, multiplicity=Multiplicity(1, 1))
    }
)
providedCommunicationInstances95: BinaryAssociation = BinaryAssociation(
    name="providedCommunicationInstances95",
    ends={
        Property(name="ProvidedCommunicationInstance", type=camel_deployment_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_ComponentInstance96", type=ProvidedCommunicationInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type105: BinaryAssociation = BinaryAssociation(
    name="type105",
    ends={
        Property(name="Communication106", type=camel_deployment_CommunicationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_CommunicationInstance", type=Communication, multiplicity=Multiplicity(1, 1))
    }
)
providedHostInstances97: BinaryAssociation = BinaryAssociation(
    name="providedHostInstances97",
    ends={
        Property(name="ProvidedHostInstance", type=camel_deployment_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_ComponentInstance98", type=ProvidedHostInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedCommunicationInstance107: BinaryAssociation = BinaryAssociation(
    name="providedCommunicationInstance107",
    ends={
        Property(name="ProvidedCommunicationInstance109", type=camel_deployment_CommunicationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_CommunicationInstance108", type=ProvidedCommunicationInstance, multiplicity=Multiplicity(1, 1))
    }
)
requiredCommunicationInstance110: BinaryAssociation = BinaryAssociation(
    name="requiredCommunicationInstance110",
    ends={
        Property(name="RequiredCommunicationInstance112", type=camel_deployment_CommunicationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_CommunicationInstance111", type=RequiredCommunicationInstance, multiplicity=Multiplicity(1, 1))
    }
)
type113: BinaryAssociation = BinaryAssociation(
    name="type113",
    ends={
        Property(name="CommunicationPort", type=camel_deployment_CommunicationPortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_CommunicationPortInstance", type=CommunicationPort, multiplicity=Multiplicity(1, 1))
    }
)
type114: BinaryAssociation = BinaryAssociation(
    name="type114",
    ends={
        Property(name="Hosting115", type=camel_deployment_HostingInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_HostingInstance", type=Hosting, multiplicity=Multiplicity(1, 1))
    }
)
providedHostInstance116: BinaryAssociation = BinaryAssociation(
    name="providedHostInstance116",
    ends={
        Property(name="ProvidedHostInstance118", type=camel_deployment_HostingInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_HostingInstance117", type=ProvidedHostInstance, multiplicity=Multiplicity(1, 1))
    }
)
requiredHostInstance119: BinaryAssociation = BinaryAssociation(
    name="requiredHostInstance119",
    ends={
        Property(name="RequiredHostInstance121", type=camel_deployment_HostingInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_HostingInstance120", type=RequiredHostInstance, multiplicity=Multiplicity(1, 1))
    }
)
type122: BinaryAssociation = BinaryAssociation(
    name="type122",
    ends={
        Property(name="HostingPort", type=camel_deployment_HostingPortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_HostingPortInstance", type=HostingPort, multiplicity=Multiplicity(1, 1))
    }
)
vmType102: BinaryAssociation = BinaryAssociation(
    name="vmType102",
    ends={
        Property(name="Attribute", type=camel_deployment_VMInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_VMInstance", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
vmTypeValue103: BinaryAssociation = BinaryAssociation(
    name="vmTypeValue103",
    ends={
        Property(name="SingleValue", type=camel_deployment_VMInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_deployment_VMInstance104", type=SingleValue, multiplicity=Multiplicity(0, 1))
    }
)
application135: BinaryAssociation = BinaryAssociation(
    name="application135",
    ends={
        Property(name="execution_camel_Application", type=camel_execution_ExecutionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_ExecutionContext", type=execution_camel_Application, multiplicity=Multiplicity(1, 1))
    }
)
costUnit136: BinaryAssociation = BinaryAssociation(
    name="costUnit136",
    ends={
        Property(name="MonetaryUnit", type=camel_execution_ExecutionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_ExecutionContext137", type=MonetaryUnit, multiplicity=Multiplicity(0, 1))
    }
)
deploymentModel138: BinaryAssociation = BinaryAssociation(
    name="deploymentModel138",
    ends={
        Property(name="DeploymentModel140", type=camel_execution_ExecutionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_ExecutionContext139", type=DeploymentModel, multiplicity=Multiplicity(1, 1))
    }
)
requirementGroup141: BinaryAssociation = BinaryAssociation(
    name="requirementGroup141",
    ends={
        Property(name="RequirementGroup", type=camel_execution_ExecutionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_ExecutionContext142", type=RequirementGroup, multiplicity=Multiplicity(1, 1))
    }
)
executionContext143: BinaryAssociation = BinaryAssociation(
    name="executionContext143",
    ends={
        Property(name="ExecutionContext144", type=camel_execution_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_Measurement", type=ExecutionContext, multiplicity=Multiplicity(1, 1))
    }
)
actionRealisations123: BinaryAssociation = BinaryAssociation(
    name="actionRealisations123",
    ends={
        Property(name="ActionRealisation", type=camel_execution_ExecutionModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_ExecutionModel", type=ActionRealisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventInstances124: BinaryAssociation = BinaryAssociation(
    name="eventInstances124",
    ends={
        Property(name="EventInstance", type=camel_execution_ExecutionModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_ExecutionModel125", type=EventInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executionContexts126: BinaryAssociation = BinaryAssociation(
    name="executionContexts126",
    ends={
        Property(name="ExecutionContext", type=camel_execution_ExecutionModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_ExecutionModel127", type=ExecutionContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measurements128: BinaryAssociation = BinaryAssociation(
    name="measurements128",
    ends={
        Property(name="Measurement", type=camel_execution_ExecutionModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_ExecutionModel129", type=Measurement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sloAssessessments130: BinaryAssociation = BinaryAssociation(
    name="sloAssessessments130",
    ends={
        Property(name="SLOAssessment", type=camel_execution_ExecutionModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_ExecutionModel131", type=SLOAssessment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ruleTriggers132: BinaryAssociation = BinaryAssociation(
    name="ruleTriggers132",
    ends={
        Property(name="RuleTrigger", type=camel_execution_ExecutionModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_ExecutionModel133", type=RuleTrigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action134: BinaryAssociation = BinaryAssociation(
    name="action134",
    ends={
        Property(name="execution_camel_Action", type=camel_execution_ActionRealisation, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_ActionRealisation", type=execution_camel_Action, multiplicity=Multiplicity(1, 1))
    }
)
internalComponentInstance154: BinaryAssociation = BinaryAssociation(
    name="internalComponentInstance154",
    ends={
        Property(name="InternalComponentInstance155", type=camel_execution_InternalComponentMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_InternalComponentMeasurement", type=InternalComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
sourceVMInstance156: BinaryAssociation = BinaryAssociation(
    name="sourceVMInstance156",
    ends={
        Property(name="VMInstance157", type=camel_execution_CommunicationMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_CommunicationMeasurement", type=VMInstance, multiplicity=Multiplicity(1, 1))
    }
)
destinationVMInstance158: BinaryAssociation = BinaryAssociation(
    name="destinationVMInstance158",
    ends={
        Property(name="VMInstance160", type=camel_execution_CommunicationMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_CommunicationMeasurement159", type=VMInstance, multiplicity=Multiplicity(1, 1))
    }
)
vmInstance161: BinaryAssociation = BinaryAssociation(
    name="vmInstance161",
    ends={
        Property(name="VMInstance162", type=camel_execution_VMMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_VMMeasurement", type=VMInstance, multiplicity=Multiplicity(1, 1))
    }
)
slo163: BinaryAssociation = BinaryAssociation(
    name="slo163",
    ends={
        Property(name="ServiceLevelObjective164", type=camel_execution_SLOAssessment, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_SLOAssessment", type=ServiceLevelObjective, multiplicity=Multiplicity(1, 1))
    }
)
metricInstance145: BinaryAssociation = BinaryAssociation(
    name="metricInstance145",
    ends={
        Property(name="MetricInstance", type=camel_execution_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_Measurement146", type=MetricInstance, multiplicity=Multiplicity(1, 1))
    }
)
slo147: BinaryAssociation = BinaryAssociation(
    name="slo147",
    ends={
        Property(name="ServiceLevelObjective", type=camel_execution_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_Measurement148", type=ServiceLevelObjective, multiplicity=Multiplicity(0, 1))
    }
)
eventInstance149: BinaryAssociation = BinaryAssociation(
    name="eventInstance149",
    ends={
        Property(name="EventInstance151", type=camel_execution_Measurement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_Measurement150", type=EventInstance, multiplicity=Multiplicity(0, 1))
    }
)
application152: BinaryAssociation = BinaryAssociation(
    name="application152",
    ends={
        Property(name="execution_camel_Application153", type=camel_execution_ApplicationMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_ApplicationMeasurement", type=execution_camel_Application, multiplicity=Multiplicity(1, 1))
    }
)
scalabilityRule171: BinaryAssociation = BinaryAssociation(
    name="scalabilityRule171",
    ends={
        Property(name="ScalabilityRule", type=camel_execution_RuleTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_RuleTrigger", type=ScalabilityRule, multiplicity=Multiplicity(1, 1))
    }
)
eventInstances172: BinaryAssociation = BinaryAssociation(
    name="eventInstances172",
    ends={
        Property(name="EventInstance174", type=camel_execution_RuleTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_RuleTrigger173", type=EventInstance, multiplicity=Multiplicity(1, 9999))
    }
)
actionRealisations175: BinaryAssociation = BinaryAssociation(
    name="actionRealisations175",
    ends={
        Property(name="ActionRealisation177", type=camel_execution_RuleTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_RuleTrigger176", type=ActionRealisation, multiplicity=Multiplicity(1, 9999))
    }
)
executionContext178: BinaryAssociation = BinaryAssociation(
    name="executionContext178",
    ends={
        Property(name="ExecutionContext180", type=camel_execution_RuleTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_RuleTrigger179", type=ExecutionContext, multiplicity=Multiplicity(1, 1))
    }
)
cloudLocations181: BinaryAssociation = BinaryAssociation(
    name="cloudLocations181",
    ends={
        Property(name="CloudLocation", type=camel_location_LocationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_location_LocationModel", type=CloudLocation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
countries182: BinaryAssociation = BinaryAssociation(
    name="countries182",
    ends={
        Property(name="Country", type=camel_location_LocationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_location_LocationModel183", type=Country, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executionContext165: BinaryAssociation = BinaryAssociation(
    name="executionContext165",
    ends={
        Property(name="ExecutionContext167", type=camel_execution_SLOAssessment, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_SLOAssessment166", type=ExecutionContext, multiplicity=Multiplicity(1, 1))
    }
)
measurement168: BinaryAssociation = BinaryAssociation(
    name="measurement168",
    ends={
        Property(name="Measurement170", type=camel_execution_SLOAssessment, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_execution_SLOAssessment169", type=Measurement, multiplicity=Multiplicity(1, 1))
    }
)
subLocations186: BinaryAssociation = BinaryAssociation(
    name="subLocations186",
    ends={
        Property(name="CloudLocation187", type=camel_location_CloudLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_location_CloudLocation", type=CloudLocation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent188: BinaryAssociation = BinaryAssociation(
    name="parent188",
    ends={
        Property(name="CloudLocation190", type=camel_location_CloudLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_location_CloudLocation189", type=CloudLocation, multiplicity=Multiplicity(0, 1))
    }
)
geographicalRegion191: BinaryAssociation = BinaryAssociation(
    name="geographicalRegion191",
    ends={
        Property(name="GeographicalRegion193", type=camel_location_CloudLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_location_CloudLocation192", type=GeographicalRegion, multiplicity=Multiplicity(0, 1))
    }
)
parentRegions194: BinaryAssociation = BinaryAssociation(
    name="parentRegions194",
    ends={
        Property(name="GeographicalRegion195", type=camel_location_GeographicalRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_location_GeographicalRegion", type=GeographicalRegion, multiplicity=Multiplicity(0, 9999))
    }
)
regions184: BinaryAssociation = BinaryAssociation(
    name="regions184",
    ends={
        Property(name="GeographicalRegion", type=camel_location_LocationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_location_LocationModel185", type=GeographicalRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricContext196: BinaryAssociation = BinaryAssociation(
    name="metricContext196",
    ends={
        Property(name="MetricContext", type=camel_metric_MetricCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricCondition", type=MetricContext, multiplicity=Multiplicity(1, 1))
    }
)
propertyContext197: BinaryAssociation = BinaryAssociation(
    name="propertyContext197",
    ends={
        Property(name="PropertyContext", type=camel_metric_PropertyCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_PropertyCondition", type=PropertyContext, multiplicity=Multiplicity(1, 1))
    }
)
unit198: BinaryAssociation = BinaryAssociation(
    name="unit198",
    ends={
        Property(name="MonetaryUnit200", type=camel_metric_PropertyCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_PropertyCondition199", type=MonetaryUnit, multiplicity=Multiplicity(0, 1))
    }
)
timeUnit201: BinaryAssociation = BinaryAssociation(
    name="timeUnit201",
    ends={
        Property(name="TimeIntervalUnit", type=camel_metric_PropertyCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_PropertyCondition202", type=TimeIntervalUnit, multiplicity=Multiplicity(0, 1))
    }
)
window206: BinaryAssociation = BinaryAssociation(
    name="window206",
    ends={
        Property(name="Window", type=camel_metric_MetricInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricInstance207", type=Window, multiplicity=Multiplicity(0, 1))
    }
)
objectBinding208: BinaryAssociation = BinaryAssociation(
    name="objectBinding208",
    ends={
        Property(name="MetricObjectBinding", type=camel_metric_MetricInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricInstance209", type=MetricObjectBinding, multiplicity=Multiplicity(1, 1))
    }
)
metricContext210: BinaryAssociation = BinaryAssociation(
    name="metricContext210",
    ends={
        Property(name="MetricContext212", type=camel_metric_MetricInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricInstance211", type=MetricContext, multiplicity=Multiplicity(0, 1))
    }
)
composingMetricInstances213: BinaryAssociation = BinaryAssociation(
    name="composingMetricInstances213",
    ends={
        Property(name="MetricInstance214", type=camel_metric_CompositeMetricInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_CompositeMetricInstance", type=MetricInstance, multiplicity=Multiplicity(1, 9999))
    }
)
sensor215: BinaryAssociation = BinaryAssociation(
    name="sensor215",
    ends={
        Property(name="Sensor", type=camel_metric_RawMetricInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_RawMetricInstance", type=Sensor, multiplicity=Multiplicity(1, 1))
    }
)
value216: BinaryAssociation = BinaryAssociation(
    name="value216",
    ends={
        Property(name="SingleValue217", type=camel_metric_MetricFormulaParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricFormulaParameter", type=SingleValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metric203: BinaryAssociation = BinaryAssociation(
    name="metric203",
    ends={
        Property(name="Metric", type=camel_metric_MetricInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricInstance", type=Metric, multiplicity=Multiplicity(1, 1))
    }
)
schedule204: BinaryAssociation = BinaryAssociation(
    name="schedule204",
    ends={
        Property(name="Schedule", type=camel_metric_MetricInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricInstance205", type=Schedule, multiplicity=Multiplicity(0, 1))
    }
)
valueType219: BinaryAssociation = BinaryAssociation(
    name="valueType219",
    ends={
        Property(name="ValueType", type=camel_metric_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_Metric", type=ValueType, multiplicity=Multiplicity(0, 1))
    }
)
unit220: BinaryAssociation = BinaryAssociation(
    name="unit220",
    ends={
        Property(name="Unit", type=camel_metric_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_Metric221", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
property222: BinaryAssociation = BinaryAssociation(
    name="property222",
    ends={
        Property(name="Property", type=camel_metric_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_Metric223", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
parameters218: BinaryAssociation = BinaryAssociation(
    name="parameters218",
    ends={
        Property(name="MetricFormulaParameter", type=camel_metric_MetricFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricFormula", type=MetricFormulaParameter, multiplicity=Multiplicity(1, 9999))
    }
)
executionContext225: BinaryAssociation = BinaryAssociation(
    name="executionContext225",
    ends={
        Property(name="ExecutionContext226", type=camel_metric_MetricObjectBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricObjectBinding", type=ExecutionContext, multiplicity=Multiplicity(1, 1))
    }
)
vmInstance227: BinaryAssociation = BinaryAssociation(
    name="vmInstance227",
    ends={
        Property(name="VMInstance228", type=camel_metric_MetricComponentBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricComponentBinding", type=VMInstance, multiplicity=Multiplicity(0, 1))
    }
)
componentInstance229: BinaryAssociation = BinaryAssociation(
    name="componentInstance229",
    ends={
        Property(name="ComponentInstance", type=camel_metric_MetricComponentBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricComponentBinding230", type=ComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
vmInstance231: BinaryAssociation = BinaryAssociation(
    name="vmInstance231",
    ends={
        Property(name="VMInstance232", type=camel_metric_MetricVMBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricVMBinding", type=VMInstance, multiplicity=Multiplicity(1, 1))
    }
)
formula224: BinaryAssociation = BinaryAssociation(
    name="formula224",
    ends={
        Property(name="MetricFormula", type=camel_metric_CompositeMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_CompositeMetric", type=MetricFormula, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unit238: BinaryAssociation = BinaryAssociation(
    name="unit238",
    ends={
        Property(name="TimeIntervalUnit239", type=camel_metric_Schedule, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_Schedule", type=TimeIntervalUnit, multiplicity=Multiplicity(1, 1))
    }
)
subProperties233: BinaryAssociation = BinaryAssociation(
    name="subProperties233",
    ends={
        Property(name="Property234", type=camel_metric_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_Property", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
sensors235: BinaryAssociation = BinaryAssociation(
    name="sensors235",
    ends={
        Property(name="Sensor237", type=camel_metric_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_Property236", type=Sensor, multiplicity=Multiplicity(0, 9999))
    }
)
component242: BinaryAssociation = BinaryAssociation(
    name="component242",
    ends={
        Property(name="Component243", type=camel_metric_ConditionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_ConditionContext", type=Component, multiplicity=Multiplicity(0, 1))
    }
)
application244: BinaryAssociation = BinaryAssociation(
    name="application244",
    ends={
        Property(name="metric_camel_Application", type=camel_metric_ConditionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_ConditionContext245", type=metric_camel_Application, multiplicity=Multiplicity(0, 1))
    }
)
contexts246: BinaryAssociation = BinaryAssociation(
    name="contexts246",
    ends={
        Property(name="ConditionContext", type=camel_metric_MetricModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricModel", type=ConditionContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metrics247: BinaryAssociation = BinaryAssociation(
    name="metrics247",
    ends={
        Property(name="Metric249", type=camel_metric_MetricModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricModel248", type=Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricInstances250: BinaryAssociation = BinaryAssociation(
    name="metricInstances250",
    ends={
        Property(name="MetricInstance252", type=camel_metric_MetricModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricModel251", type=MetricInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditions253: BinaryAssociation = BinaryAssociation(
    name="conditions253",
    ends={
        Property(name="Condition", type=camel_metric_MetricModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricModel254", type=Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unit240: BinaryAssociation = BinaryAssociation(
    name="unit240",
    ends={
        Property(name="TimeIntervalUnit241", type=camel_metric_Window, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_Window", type=TimeIntervalUnit, multiplicity=Multiplicity(0, 1))
    }
)
metric276: BinaryAssociation = BinaryAssociation(
    name="metric276",
    ends={
        Property(name="Metric277", type=camel_metric_MetricContext, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricContext", type=Metric, multiplicity=Multiplicity(1, 1))
    }
)
window278: BinaryAssociation = BinaryAssociation(
    name="window278",
    ends={
        Property(name="Window280", type=camel_metric_MetricContext, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricContext279", type=Window, multiplicity=Multiplicity(0, 1))
    }
)
schedule281: BinaryAssociation = BinaryAssociation(
    name="schedule281",
    ends={
        Property(name="Schedule283", type=camel_metric_MetricContext, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricContext282", type=Schedule, multiplicity=Multiplicity(0, 1))
    }
)
composingMetricContexts284: BinaryAssociation = BinaryAssociation(
    name="composingMetricContexts284",
    ends={
        Property(name="MetricContext285", type=camel_metric_CompositeMetricContext, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_CompositeMetricContext", type=MetricContext, multiplicity=Multiplicity(0, 9999))
    }
)
sensor286: BinaryAssociation = BinaryAssociation(
    name="sensor286",
    ends={
        Property(name="Sensor287", type=camel_metric_RawMetricContext, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_RawMetricContext", type=Sensor, multiplicity=Multiplicity(1, 1))
    }
)
property288: BinaryAssociation = BinaryAssociation(
    name="property288",
    ends={
        Property(name="Property289", type=camel_metric_PropertyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_PropertyContext", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
properties255: BinaryAssociation = BinaryAssociation(
    name="properties255",
    ends={
        Property(name="Property257", type=camel_metric_MetricModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricModel256", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings258: BinaryAssociation = BinaryAssociation(
    name="bindings258",
    ends={
        Property(name="MetricObjectBinding260", type=camel_metric_MetricModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricModel259", type=MetricObjectBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
windows261: BinaryAssociation = BinaryAssociation(
    name="windows261",
    ends={
        Property(name="Window263", type=camel_metric_MetricModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricModel262", type=Window, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedules264: BinaryAssociation = BinaryAssociation(
    name="schedules264",
    ends={
        Property(name="Schedule266", type=camel_metric_MetricModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricModel265", type=Schedule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters267: BinaryAssociation = BinaryAssociation(
    name="parameters267",
    ends={
        Property(name="MetricFormulaParameter269", type=camel_metric_MetricModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricModel268", type=MetricFormulaParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensors270: BinaryAssociation = BinaryAssociation(
    name="sensors270",
    ends={
        Property(name="Sensor272", type=camel_metric_MetricModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricModel271", type=Sensor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units273: BinaryAssociation = BinaryAssociation(
    name="units273",
    ends={
        Property(name="Unit275", type=camel_metric_MetricModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_metric_MetricModel274", type=Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataCentres299: BinaryAssociation = BinaryAssociation(
    name="dataCentres299",
    ends={
        Property(name="DataCenter", type=camel_organisation_OrganisationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_OrganisationModel300", type=DataCenter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roles301: BinaryAssociation = BinaryAssociation(
    name="roles301",
    ends={
        Property(name="Role", type=camel_organisation_OrganisationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_OrganisationModel302", type=Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roleAssigments303: BinaryAssociation = BinaryAssociation(
    name="roleAssigments303",
    ends={
        Property(name="RoleAssignment", type=camel_organisation_OrganisationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_OrganisationModel304", type=RoleAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
permissions305: BinaryAssociation = BinaryAssociation(
    name="permissions305",
    ends={
        Property(name="Permission", type=camel_organisation_OrganisationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_OrganisationModel306", type=Permission, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceFilters307: BinaryAssociation = BinaryAssociation(
    name="resourceFilters307",
    ends={
        Property(name="ResourceFilter", type=camel_organisation_OrganisationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_OrganisationModel308", type=ResourceFilter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cloudProvider309: BinaryAssociation = BinaryAssociation(
    name="cloudProvider309",
    ends={
        Property(name="CloudProvider310", type=camel_organisation_CloudCredentials, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_CloudCredentials", type=CloudProvider, multiplicity=Multiplicity(1, 1))
    }
)
organisation290: BinaryAssociation = BinaryAssociation(
    name="organisation290",
    ends={
        Property(name="Organisation", type=camel_organisation_OrganisationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_OrganisationModel", type=Organisation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
provider291: BinaryAssociation = BinaryAssociation(
    name="provider291",
    ends={
        Property(name="CloudProvider", type=camel_organisation_OrganisationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_OrganisationModel292", type=CloudProvider, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalIdentifiers293: BinaryAssociation = BinaryAssociation(
    name="externalIdentifiers293",
    ends={
        Property(name="ExternalIdentifier", type=camel_organisation_OrganisationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_OrganisationModel294", type=ExternalIdentifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
users295: BinaryAssociation = BinaryAssociation(
    name="users295",
    ends={
        Property(name="User", type=camel_organisation_OrganisationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_OrganisationModel296", type=User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userGroups297: BinaryAssociation = BinaryAssociation(
    name="userGroups297",
    ends={
        Property(name="UserGroup", type=camel_organisation_OrganisationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_OrganisationModel298", type=UserGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providerModel312: BinaryAssociation = BinaryAssociation(
    name="providerModel312",
    ends={
        Property(name="ProviderModel313", type=camel_organisation_CloudProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_CloudProvider", type=ProviderModel, multiplicity=Multiplicity(0, 1))
    }
)
securityCapability314: BinaryAssociation = BinaryAssociation(
    name="securityCapability314",
    ends={
        Property(name="SecurityCapability", type=camel_organisation_CloudProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_CloudProvider315", type=SecurityCapability, multiplicity=Multiplicity(0, 9999))
    }
)
externalIdentifiers316: BinaryAssociation = BinaryAssociation(
    name="externalIdentifiers316",
    ends={
        Property(name="ExternalIdentifier317", type=camel_organisation_User, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_User", type=ExternalIdentifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requirementModels318: BinaryAssociation = BinaryAssociation(
    name="requirementModels318",
    ends={
        Property(name="RequirementModel320", type=camel_organisation_User, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_User319", type=RequirementModel, multiplicity=Multiplicity(0, 9999))
    }
)
cloudCredentials321: BinaryAssociation = BinaryAssociation(
    name="cloudCredentials321",
    ends={
        Property(name="CloudCredentials", type=camel_organisation_User, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_User322", type=CloudCredentials, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deploymentModels323: BinaryAssociation = BinaryAssociation(
    name="deploymentModels323",
    ends={
        Property(name="DeploymentModel325", type=camel_organisation_User, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_User324", type=DeploymentModel, multiplicity=Multiplicity(0, 9999))
    }
)
paasageCredentials326: BinaryAssociation = BinaryAssociation(
    name="paasageCredentials326",
    ends={
        Property(name="PaaSageCredentials", type=camel_organisation_User, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_User327", type=PaaSageCredentials, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
location311: BinaryAssociation = BinaryAssociation(
    name="location311",
    ends={
        Property(name="Location", type=camel_organisation_DataCenter, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_DataCenter", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
role328: BinaryAssociation = BinaryAssociation(
    name="role328",
    ends={
        Property(name="Role329", type=camel_organisation_Permission, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_Permission", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
resourceFilter330: BinaryAssociation = BinaryAssociation(
    name="resourceFilter330",
    ends={
        Property(name="ResourceFilter332", type=camel_organisation_Permission, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_Permission331", type=ResourceFilter, multiplicity=Multiplicity(1, 1))
    }
)
constraints343: BinaryAssociation = BinaryAssociation(
    name="constraints343",
    ends={
        Property(name="Constraint", type=camel_provider_ProviderModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_ProviderModel", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootFeature344: BinaryAssociation = BinaryAssociation(
    name="rootFeature344",
    ends={
        Property(name="Feature", type=camel_provider_ProviderModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_ProviderModel345", type=Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value346: BinaryAssociation = BinaryAssociation(
    name="value346",
    ends={
        Property(name="SingleValue347", type=camel_provider_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Attribute", type=SingleValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueType348: BinaryAssociation = BinaryAssociation(
    name="valueType348",
    ends={
        Property(name="ValueType350", type=camel_provider_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Attribute349", type=ValueType, multiplicity=Multiplicity(0, 1))
    }
)
user333: BinaryAssociation = BinaryAssociation(
    name="user333",
    ends={
        Property(name="User334", type=camel_organisation_RoleAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_RoleAssignment", type=User, multiplicity=Multiplicity(0, 1))
    }
)
role335: BinaryAssociation = BinaryAssociation(
    name="role335",
    ends={
        Property(name="Role337", type=camel_organisation_RoleAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_RoleAssignment336", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
userGroup338: BinaryAssociation = BinaryAssociation(
    name="userGroup338",
    ends={
        Property(name="UserGroup340", type=camel_organisation_RoleAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_RoleAssignment339", type=UserGroup, multiplicity=Multiplicity(0, 1))
    }
)
users341: BinaryAssociation = BinaryAssociation(
    name="users341",
    ends={
        Property(name="User342", type=camel_organisation_UserGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_organisation_UserGroup", type=User, multiplicity=Multiplicity(1, 9999))
    }
)
subClones362: BinaryAssociation = BinaryAssociation(
    name="subClones362",
    ends={
        Property(name="Clone", type=camel_provider_Clone, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Clone", type=Clone, multiplicity=Multiplicity(0, 9999))
    }
)
from351: BinaryAssociation = BinaryAssociation(
    name="from351",
    ends={
        Property(name="Attribute352", type=camel_provider_AttributeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_AttributeConstraint", type=Attribute, multiplicity=Multiplicity(1, 1))
    }
)
to353: BinaryAssociation = BinaryAssociation(
    name="to353",
    ends={
        Property(name="Attribute355", type=camel_provider_AttributeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_AttributeConstraint354", type=Attribute, multiplicity=Multiplicity(1, 1))
    }
)
fromValue356: BinaryAssociation = BinaryAssociation(
    name="fromValue356",
    ends={
        Property(name="SingleValue358", type=camel_provider_AttributeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_AttributeConstraint357", type=SingleValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
toValue359: BinaryAssociation = BinaryAssociation(
    name="toValue359",
    ends={
        Property(name="SingleValue361", type=camel_provider_AttributeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_AttributeConstraint360", type=SingleValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
scopeFrom370: BinaryAssociation = BinaryAssociation(
    name="scopeFrom370",
    ends={
        Property(name="Scope", type=camel_provider_Requires, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Requires", type=Scope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scopeTo371: BinaryAssociation = BinaryAssociation(
    name="scopeTo371",
    ends={
        Property(name="Scope373", type=camel_provider_Requires, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Requires372", type=Scope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cardFrom374: BinaryAssociation = BinaryAssociation(
    name="cardFrom374",
    ends={
        Property(name="FeatCardinality", type=camel_provider_Requires, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Requires375", type=FeatCardinality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cardTo376: BinaryAssociation = BinaryAssociation(
    name="cardTo376",
    ends={
        Property(name="FeatCardinality378", type=camel_provider_Requires, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Requires377", type=FeatCardinality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from363: BinaryAssociation = BinaryAssociation(
    name="from363",
    ends={
        Property(name="Feature364", type=camel_provider_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Constraint", type=Feature, multiplicity=Multiplicity(1, 1))
    }
)
to365: BinaryAssociation = BinaryAssociation(
    name="to365",
    ends={
        Property(name="Feature367", type=camel_provider_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Constraint366", type=Feature, multiplicity=Multiplicity(1, 1))
    }
)
attributeConstraints368: BinaryAssociation = BinaryAssociation(
    name="attributeConstraints368",
    ends={
        Property(name="AttributeConstraint", type=camel_provider_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Constraint369", type=AttributeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variants391: BinaryAssociation = BinaryAssociation(
    name="variants391",
    ends={
        Property(name="Feature393", type=camel_provider_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Alternative392", type=Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
feature394: BinaryAssociation = BinaryAssociation(
    name="feature394",
    ends={
        Property(name="Feature395", type=camel_provider_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Instance", type=Feature, multiplicity=Multiplicity(1, 1))
    }
)
requirements396: BinaryAssociation = BinaryAssociation(
    name="requirements396",
    ends={
        Property(name="Requirement", type=camel_requirement_RequirementModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_requirement_RequirementModel", type=Requirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes379: BinaryAssociation = BinaryAssociation(
    name="attributes379",
    ends={
        Property(name="Attribute380", type=camel_provider_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Feature", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subFeatures381: BinaryAssociation = BinaryAssociation(
    name="subFeatures381",
    ends={
        Property(name="Feature383", type=camel_provider_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Feature382", type=Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureCardinality384: BinaryAssociation = BinaryAssociation(
    name="featureCardinality384",
    ends={
        Property(name="FeatCardinality386", type=camel_provider_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Feature385", type=FeatCardinality, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
clones387: BinaryAssociation = BinaryAssociation(
    name="clones387",
    ends={
        Property(name="Clone389", type=camel_provider_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Feature388", type=Clone, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupCardinality390: BinaryAssociation = BinaryAssociation(
    name="groupCardinality390",
    ends={
        Property(name="GroupCardinality", type=camel_provider_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_provider_Alternative", type=GroupCardinality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requirements397: BinaryAssociation = BinaryAssociation(
    name="requirements397",
    ends={
        Property(name="Requirement398", type=camel_requirement_RequirementGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_requirement_RequirementGroup", type=Requirement, multiplicity=Multiplicity(1, 9999))
    }
)
application399: BinaryAssociation = BinaryAssociation(
    name="application399",
    ends={
        Property(name="requirement_camel_Application", type=camel_requirement_RequirementGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_requirement_RequirementGroup400", type=requirement_camel_Application, multiplicity=Multiplicity(0, 9999))
    }
)
customServiceLevel401: BinaryAssociation = BinaryAssociation(
    name="customServiceLevel401",
    ends={
        Property(name="Condition402", type=camel_requirement_ServiceLevelObjective, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_requirement_ServiceLevelObjective", type=Condition, multiplicity=Multiplicity(1, 1))
    }
)
metric403: BinaryAssociation = BinaryAssociation(
    name="metric403",
    ends={
        Property(name="Metric404", type=camel_requirement_OptimisationRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_requirement_OptimisationRequirement", type=Metric, multiplicity=Multiplicity(0, 1))
    }
)
metricContext414: BinaryAssociation = BinaryAssociation(
    name="metricContext414",
    ends={
        Property(name="MetricContext416", type=camel_requirement_OptimisationRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_requirement_OptimisationRequirement415", type=MetricContext, multiplicity=Multiplicity(0, 1))
    }
)
property405: BinaryAssociation = BinaryAssociation(
    name="property405",
    ends={
        Property(name="Property407", type=camel_requirement_OptimisationRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_requirement_OptimisationRequirement406", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
application408: BinaryAssociation = BinaryAssociation(
    name="application408",
    ends={
        Property(name="requirement_camel_Application410", type=camel_requirement_OptimisationRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_requirement_OptimisationRequirement409", type=requirement_camel_Application, multiplicity=Multiplicity(0, 1))
    }
)
component411: BinaryAssociation = BinaryAssociation(
    name="component411",
    ends={
        Property(name="Component413", type=camel_requirement_OptimisationRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_requirement_OptimisationRequirement412", type=Component, multiplicity=Multiplicity(0, 1))
    }
)
providers417: BinaryAssociation = BinaryAssociation(
    name="providers417",
    ends={
        Property(name="CloudProvider418", type=camel_requirement_ProviderRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_requirement_ProviderRequirement", type=CloudProvider, multiplicity=Multiplicity(1, 9999))
    }
)
securityControls419: BinaryAssociation = BinaryAssociation(
    name="securityControls419",
    ends={
        Property(name="SecurityControl", type=camel_requirement_SecurityRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_requirement_SecurityRequirement", type=SecurityControl, multiplicity=Multiplicity(1, 9999))
    }
)
application420: BinaryAssociation = BinaryAssociation(
    name="application420",
    ends={
        Property(name="requirement_camel_Application422", type=camel_requirement_SecurityRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_requirement_SecurityRequirement421", type=requirement_camel_Application, multiplicity=Multiplicity(0, 1))
    }
)
component423: BinaryAssociation = BinaryAssociation(
    name="component423",
    ends={
        Property(name="InternalComponent425", type=camel_requirement_SecurityRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_requirement_SecurityRequirement424", type=InternalComponent, multiplicity=Multiplicity(0, 1))
    }
)
locations426: BinaryAssociation = BinaryAssociation(
    name="locations426",
    ends={
        Property(name="Location427", type=camel_requirement_LocationRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_requirement_LocationRequirement", type=Location, multiplicity=Multiplicity(1, 9999))
    }
)
component428: BinaryAssociation = BinaryAssociation(
    name="component428",
    ends={
        Property(name="camel_requirement_HorizontalScaleRequirement", type=InternalComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalComponent429", type=camel_requirement_HorizontalScaleRequirement, multiplicity=Multiplicity(1, 1))
    }
)
rules432: BinaryAssociation = BinaryAssociation(
    name="rules432",
    ends={
        Property(name="ScalabilityRule433", type=camel_scalability_ScalabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_ScalabilityModel", type=ScalabilityRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events434: BinaryAssociation = BinaryAssociation(
    name="events434",
    ends={
        Property(name="Event", type=camel_scalability_ScalabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_ScalabilityModel435", type=Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventInstances436: BinaryAssociation = BinaryAssociation(
    name="eventInstances436",
    ends={
        Property(name="EventInstance438", type=camel_scalability_ScalabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_ScalabilityModel437", type=EventInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions439: BinaryAssociation = BinaryAssociation(
    name="actions439",
    ends={
        Property(name="ScalingAction", type=camel_scalability_ScalabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_ScalabilityModel440", type=ScalingAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vm430: BinaryAssociation = BinaryAssociation(
    name="vm430",
    ends={
        Property(name="VM431", type=camel_requirement_VerticalScaleRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_requirement_VerticalScaleRequirement", type=VM, multiplicity=Multiplicity(1, 1))
    }
)
patterns441: BinaryAssociation = BinaryAssociation(
    name="patterns441",
    ends={
        Property(name="EventPattern", type=camel_scalability_ScalabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_ScalabilityModel442", type=EventPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timers443: BinaryAssociation = BinaryAssociation(
    name="timers443",
    ends={
        Property(name="Timer", type=camel_scalability_ScalabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_ScalabilityModel444", type=Timer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scaleRequirements445: BinaryAssociation = BinaryAssociation(
    name="scaleRequirements445",
    ends={
        Property(name="ScaleRequirement", type=camel_scalability_ScalabilityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_ScalabilityModel446", type=ScaleRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftEvent449: BinaryAssociation = BinaryAssociation(
    name="leftEvent449",
    ends={
        Property(name="Event450", type=camel_scalability_BinaryEventPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_BinaryEventPattern", type=Event, multiplicity=Multiplicity(0, 1))
    }
)
rightEvent451: BinaryAssociation = BinaryAssociation(
    name="rightEvent451",
    ends={
        Property(name="Event453", type=camel_scalability_BinaryEventPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_BinaryEventPattern452", type=Event, multiplicity=Multiplicity(0, 1))
    }
)
event454: BinaryAssociation = BinaryAssociation(
    name="event454",
    ends={
        Property(name="Event455", type=camel_scalability_UnaryEventPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_UnaryEventPattern", type=Event, multiplicity=Multiplicity(1, 1))
    }
)
timer447: BinaryAssociation = BinaryAssociation(
    name="timer447",
    ends={
        Property(name="Timer448", type=camel_scalability_EventPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_EventPattern", type=Timer, multiplicity=Multiplicity(0, 1))
    }
)
metricCondition456: BinaryAssociation = BinaryAssociation(
    name="metricCondition456",
    ends={
        Property(name="MetricCondition", type=camel_scalability_NonFunctionalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_NonFunctionalEvent", type=MetricCondition, multiplicity=Multiplicity(1, 1))
    }
)
event461: BinaryAssociation = BinaryAssociation(
    name="event461",
    ends={
        Property(name="Event462", type=camel_scalability_ScalabilityRule, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_ScalabilityRule", type=Event, multiplicity=Multiplicity(1, 1))
    }
)
actions463: BinaryAssociation = BinaryAssociation(
    name="actions463",
    ends={
        Property(name="scalability_camel_Action", type=camel_scalability_ScalabilityRule, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_ScalabilityRule464", type=scalability_camel_Action, multiplicity=Multiplicity(1, 9999))
    }
)
entity465: BinaryAssociation = BinaryAssociation(
    name="entity465",
    ends={
        Property(name="Entity467", type=camel_scalability_ScalabilityRule, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_ScalabilityRule466", type=Entity, multiplicity=Multiplicity(0, 9999))
    }
)
scaleRequirements468: BinaryAssociation = BinaryAssociation(
    name="scaleRequirements468",
    ends={
        Property(name="ScaleRequirement470", type=camel_scalability_ScalabilityRule, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_ScalabilityRule469", type=ScaleRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
vm471: BinaryAssociation = BinaryAssociation(
    name="vm471",
    ends={
        Property(name="VM472", type=camel_scalability_ScalingAction, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_ScalingAction", type=VM, multiplicity=Multiplicity(1, 1))
    }
)
event457: BinaryAssociation = BinaryAssociation(
    name="event457",
    ends={
        Property(name="SimpleEvent", type=camel_scalability_EventInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_EventInstance", type=SimpleEvent, multiplicity=Multiplicity(1, 1))
    }
)
metricInstance458: BinaryAssociation = BinaryAssociation(
    name="metricInstance458",
    ends={
        Property(name="MetricInstance460", type=camel_scalability_EventInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_EventInstance459", type=MetricInstance, multiplicity=Multiplicity(0, 1))
    }
)
unit475: BinaryAssociation = BinaryAssociation(
    name="unit475",
    ends={
        Property(name="TimeIntervalUnit476", type=camel_scalability_Timer, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_Timer", type=TimeIntervalUnit, multiplicity=Multiplicity(1, 1))
    }
)
internalComponent473: BinaryAssociation = BinaryAssociation(
    name="internalComponent473",
    ends={
        Property(name="InternalComponent474", type=camel_scalability_HorizontalScalingAction, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_scalability_HorizontalScalingAction", type=InternalComponent, multiplicity=Multiplicity(1, 1))
    }
)
securityControls477: BinaryAssociation = BinaryAssociation(
    name="securityControls477",
    ends={
        Property(name="SecurityControl478", type=camel_security_SecurityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityModel", type=SecurityControl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
securityRequirements479: BinaryAssociation = BinaryAssociation(
    name="securityRequirements479",
    ends={
        Property(name="SecurityRequirement", type=camel_security_SecurityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityModel480", type=SecurityRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
securityProperties481: BinaryAssociation = BinaryAssociation(
    name="securityProperties481",
    ends={
        Property(name="SecurityProperty", type=camel_security_SecurityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityModel482", type=SecurityProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rawSecurityMetrics483: BinaryAssociation = BinaryAssociation(
    name="rawSecurityMetrics483",
    ends={
        Property(name="RawSecurityMetric", type=camel_security_SecurityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityModel484", type=RawSecurityMetric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compositeSecurityMetricInstances489: BinaryAssociation = BinaryAssociation(
    name="compositeSecurityMetricInstances489",
    ends={
        Property(name="CompositeSecurityMetricInstance", type=camel_security_SecurityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityModel490", type=CompositeSecurityMetricInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
securityDomains491: BinaryAssociation = BinaryAssociation(
    name="securityDomains491",
    ends={
        Property(name="SecurityDomain", type=camel_security_SecurityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityModel492", type=SecurityDomain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
securityCapabilities493: BinaryAssociation = BinaryAssociation(
    name="securityCapabilities493",
    ends={
        Property(name="SecurityCapability495", type=camel_security_SecurityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityModel494", type=SecurityCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
securitySLOs496: BinaryAssociation = BinaryAssociation(
    name="securitySLOs496",
    ends={
        Property(name="SecuritySLO", type=camel_security_SecurityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityModel497", type=SecuritySLO, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compositeSecurityMetrics485: BinaryAssociation = BinaryAssociation(
    name="compositeSecurityMetrics485",
    ends={
        Property(name="CompositeSecurityMetric", type=camel_security_SecurityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityModel486", type=CompositeSecurityMetric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rawSecurityMetricInstances487: BinaryAssociation = BinaryAssociation(
    name="rawSecurityMetricInstances487",
    ends={
        Property(name="RawSecurityMetricInstance", type=camel_security_SecurityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityModel488", type=RawSecurityMetricInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
securityProperties505: BinaryAssociation = BinaryAssociation(
    name="securityProperties505",
    ends={
        Property(name="SecurityProperty507", type=camel_security_SecurityControl, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityControl506", type=SecurityProperty, multiplicity=Multiplicity(0, 9999))
    }
)
rawSecurityMetrics508: BinaryAssociation = BinaryAssociation(
    name="rawSecurityMetrics508",
    ends={
        Property(name="RawSecurityMetric510", type=camel_security_SecurityControl, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityControl509", type=RawSecurityMetric, multiplicity=Multiplicity(0, 9999))
    }
)
compositeSecurityMetrics511: BinaryAssociation = BinaryAssociation(
    name="compositeSecurityMetrics511",
    ends={
        Property(name="CompositeSecurityMetric513", type=camel_security_SecurityControl, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityControl512", type=CompositeSecurityMetric, multiplicity=Multiplicity(0, 9999))
    }
)
domain514: BinaryAssociation = BinaryAssociation(
    name="domain514",
    ends={
        Property(name="SecurityDomain515", type=camel_security_SecurityProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityProperty", type=SecurityDomain, multiplicity=Multiplicity(1, 1))
    }
)
securityControls516: BinaryAssociation = BinaryAssociation(
    name="securityControls516",
    ends={
        Property(name="SecurityControl517", type=camel_security_SecurityCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityCapability", type=SecurityControl, multiplicity=Multiplicity(1, 9999))
    }
)
subDomain498: BinaryAssociation = BinaryAssociation(
    name="subDomain498",
    ends={
        Property(name="SecurityDomain499", type=camel_security_SecurityDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityDomain", type=SecurityDomain, multiplicity=Multiplicity(0, 9999))
    }
)
domain500: BinaryAssociation = BinaryAssociation(
    name="domain500",
    ends={
        Property(name="SecurityDomain501", type=camel_security_SecurityControl, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityControl", type=SecurityDomain, multiplicity=Multiplicity(1, 1))
    }
)
subDomain502: BinaryAssociation = BinaryAssociation(
    name="subDomain502",
    ends={
        Property(name="SecurityDomain504", type=camel_security_SecurityControl, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityControl503", type=SecurityDomain, multiplicity=Multiplicity(1, 1))
    }
)
dataTypes521: BinaryAssociation = BinaryAssociation(
    name="dataTypes521",
    ends={
        Property(name="ValueType522", type=camel_type_TypeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_type_TypeModel", type=ValueType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values523: BinaryAssociation = BinaryAssociation(
    name="values523",
    ends={
        Property(name="SingleValue525", type=camel_type_TypeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_type_TypeModel524", type=SingleValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value526: BinaryAssociation = BinaryAssociation(
    name="value526",
    ends={
        Property(name="NumericValue", type=camel_type_Limit, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_type_Limit", type=NumericValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataCenter518: BinaryAssociation = BinaryAssociation(
    name="dataCenter518",
    ends={
        Property(name="DataCenter520", type=camel_security_SecurityCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_security_SecurityCapability519", type=DataCenter, multiplicity=Multiplicity(0, 1))
    }
)
values529: BinaryAssociation = BinaryAssociation(
    name="values529",
    ends={
        Property(name="EnumerateValue", type=camel_type_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_type_Enumeration", type=EnumerateValue, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
values530: BinaryAssociation = BinaryAssociation(
    name="values530",
    ends={
        Property(name="SingleValue531", type=camel_type_List, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_type_List", type=SingleValue, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type532: BinaryAssociation = BinaryAssociation(
    name="type532",
    ends={
        Property(name="ValueType534", type=camel_type_List, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_type_List533", type=ValueType, multiplicity=Multiplicity(0, 1))
    }
)
value527: BinaryAssociation = BinaryAssociation(
    name="value527",
    ends={
        Property(name="NumericValue528", type=camel_type_ValueToIncrease, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_type_ValueToIncrease", type=NumericValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
upperLimit536: BinaryAssociation = BinaryAssociation(
    name="upperLimit536",
    ends={
        Property(name="camel_type_Range537", type=Limit, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Limit538", type=camel_type_Range, multiplicity=Multiplicity(1, 1))
    }
)
ranges539: BinaryAssociation = BinaryAssociation(
    name="ranges539",
    ends={
        Property(name="Range", type=camel_type_RangeUnion, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_type_RangeUnion", type=Range, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
lowerLimit535: BinaryAssociation = BinaryAssociation(
    name="lowerLimit535",
    ends={
        Property(name="Limit", type=camel_type_Range, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_type_Range", type=Limit, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
units540: BinaryAssociation = BinaryAssociation(
    name="units540",
    ends={
        Property(name="Unit541", type=camel_unit_UnitModel, multiplicity=Multiplicity(1, 1)),
        Property(name="camel_unit_UnitModel", type=Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_camel_CamelModel_Model = Generalization(general=Model, specific=camel_CamelModel)
gen_camel_deployment_DeploymentModel_Model = Generalization(general=Model, specific=camel_deployment_DeploymentModel)
gen_camel_deployment_InternalComponent_Component = Generalization(general=Component, specific=camel_deployment_InternalComponent)
gen_camel_deployment_Component_DeploymentElement = Generalization(general=DeploymentElement, specific=camel_deployment_Component)
gen_camel_deployment_VM_Component = Generalization(general=Component, specific=camel_deployment_VM)
gen_camel_deployment_CommunicationPort_DeploymentElement = Generalization(general=DeploymentElement, specific=camel_deployment_CommunicationPort)
gen_camel_deployment_ProvidedCommunication_CommunicationPort = Generalization(general=CommunicationPort, specific=camel_deployment_ProvidedCommunication)
gen_camel_deployment_RequiredCommunication_CommunicationPort = Generalization(general=CommunicationPort, specific=camel_deployment_RequiredCommunication)
gen_camel_deployment_Hosting_DeploymentElement = Generalization(general=DeploymentElement, specific=camel_deployment_Hosting)
gen_camel_deployment_HostingPort_DeploymentElement = Generalization(general=DeploymentElement, specific=camel_deployment_HostingPort)
gen_camel_deployment_Configuration_DeploymentElement = Generalization(general=DeploymentElement, specific=camel_deployment_Configuration)
gen_camel_deployment_ProvidedHost_HostingPort = Generalization(general=HostingPort, specific=camel_deployment_ProvidedHost)
gen_camel_deployment_RequiredHost_HostingPort = Generalization(general=HostingPort, specific=camel_deployment_RequiredHost)
gen_camel_deployment_Communication_DeploymentElement = Generalization(general=DeploymentElement, specific=camel_deployment_Communication)
gen_camel_deployment_InternalComponentInstance_ComponentInstance = Generalization(general=ComponentInstance, specific=camel_deployment_InternalComponentInstance)
gen_camel_deployment_VMInstance_ComponentInstance = Generalization(general=ComponentInstance, specific=camel_deployment_VMInstance)
gen_camel_deployment_ComponentInstance_DeploymentElement = Generalization(general=DeploymentElement, specific=camel_deployment_ComponentInstance)
gen_camel_deployment_CommunicationPortInstance_DeploymentElement = Generalization(general=DeploymentElement, specific=camel_deployment_CommunicationPortInstance)
gen_camel_deployment_ProvidedCommunicationInstance_CommunicationPortInstance = Generalization(general=CommunicationPortInstance, specific=camel_deployment_ProvidedCommunicationInstance)
gen_camel_deployment_RequiredCommunicationInstance_CommunicationPortInstance = Generalization(general=CommunicationPortInstance, specific=camel_deployment_RequiredCommunicationInstance)
gen_camel_deployment_HostingInstance_DeploymentElement = Generalization(general=DeploymentElement, specific=camel_deployment_HostingInstance)
gen_camel_deployment_HostingPortInstance_DeploymentElement = Generalization(general=DeploymentElement, specific=camel_deployment_HostingPortInstance)
gen_camel_deployment_ProvidedHostInstance_HostingPortInstance = Generalization(general=HostingPortInstance, specific=camel_deployment_ProvidedHostInstance)
gen_camel_deployment_RequiredHostInstance_HostingPortInstance = Generalization(general=HostingPortInstance, specific=camel_deployment_RequiredHostInstance)
gen_camel_deployment_CommunicationInstance_DeploymentElement = Generalization(general=DeploymentElement, specific=camel_deployment_CommunicationInstance)
gen_camel_execution_ExecutionModel_Model = Generalization(general=Model, specific=camel_execution_ExecutionModel)
gen_camel_execution_InternalComponentMeasurement_Measurement = Generalization(general=Measurement, specific=camel_execution_InternalComponentMeasurement)
gen_camel_execution_CommunicationMeasurement_Measurement = Generalization(general=Measurement, specific=camel_execution_CommunicationMeasurement)
gen_camel_execution_VMMeasurement_Measurement = Generalization(general=Measurement, specific=camel_execution_VMMeasurement)
gen_camel_execution_ApplicationMeasurement_Measurement = Generalization(general=Measurement, specific=camel_execution_ApplicationMeasurement)
gen_camel_location_LocationModel_Model = Generalization(general=Model, specific=camel_location_LocationModel)
gen_camel_location_GeographicalRegion_Location = Generalization(general=Location, specific=camel_location_GeographicalRegion)
gen_camel_location_Country_GeographicalRegion = Generalization(general=GeographicalRegion, specific=camel_location_Country)
gen_camel_location_CloudLocation_Location = Generalization(general=Location, specific=camel_location_CloudLocation)
gen_camel_metric_PropertyCondition_Condition = Generalization(general=Condition, specific=camel_metric_PropertyCondition)
gen_camel_metric_MetricCondition_Condition = Generalization(general=Condition, specific=camel_metric_MetricCondition)
gen_camel_metric_CompositeMetricInstance_MetricInstance = Generalization(general=MetricInstance, specific=camel_metric_CompositeMetricInstance)
gen_camel_metric_RawMetricInstance_MetricInstance = Generalization(general=MetricInstance, specific=camel_metric_RawMetricInstance)
gen_camel_metric_CompositeMetric_Metric = Generalization(general=Metric, specific=camel_metric_CompositeMetric)
gen_camel_metric_MetricFormula_MetricFormulaParameter = Generalization(general=MetricFormulaParameter, specific=camel_metric_MetricFormula)
gen_camel_metric_Metric_MetricFormulaParameter = Generalization(general=MetricFormulaParameter, specific=camel_metric_Metric)
gen_camel_metric_MetricApplicationBinding_MetricObjectBinding = Generalization(general=MetricObjectBinding, specific=camel_metric_MetricApplicationBinding)
gen_camel_metric_MetricComponentBinding_MetricObjectBinding = Generalization(general=MetricObjectBinding, specific=camel_metric_MetricComponentBinding)
gen_camel_metric_MetricVMBinding_MetricObjectBinding = Generalization(general=MetricObjectBinding, specific=camel_metric_MetricVMBinding)
gen_camel_metric_RawMetric_Metric = Generalization(general=Metric, specific=camel_metric_RawMetric)
gen_camel_metric_MetricModel_Model = Generalization(general=Model, specific=camel_metric_MetricModel)
gen_camel_metric_CompositeMetricContext_MetricContext = Generalization(general=MetricContext, specific=camel_metric_CompositeMetricContext)
gen_camel_metric_RawMetricContext_MetricContext = Generalization(general=MetricContext, specific=camel_metric_RawMetricContext)
gen_camel_metric_PropertyContext_ConditionContext = Generalization(general=ConditionContext, specific=camel_metric_PropertyContext)
gen_camel_metric_MetricContext_ConditionContext = Generalization(general=ConditionContext, specific=camel_metric_MetricContext)
gen_camel_organisation_CloudCredentials_Credentials = Generalization(general=Credentials, specific=camel_organisation_CloudCredentials)
gen_camel_organisation_OrganisationModel_Model = Generalization(general=Model, specific=camel_organisation_OrganisationModel)
gen_camel_organisation_User_Entity = Generalization(general=Entity, specific=camel_organisation_User)
gen_camel_organisation_Organisation_Entity = Generalization(general=Entity, specific=camel_organisation_Organisation)
gen_camel_organisation_CloudProvider_Organisation = Generalization(general=Organisation, specific=camel_organisation_CloudProvider)
gen_camel_organisation_InformationResourceFilter_ResourceFilter = Generalization(general=ResourceFilter, specific=camel_organisation_InformationResourceFilter)
gen_camel_organisation_ServiceResourceFilter_ResourceFilter = Generalization(general=ResourceFilter, specific=camel_organisation_ServiceResourceFilter)
gen_camel_provider_ProviderModel_Model = Generalization(general=Model, specific=camel_provider_ProviderModel)
gen_camel_organisation_PaaSageCredentials_Credentials = Generalization(general=Credentials, specific=camel_organisation_PaaSageCredentials)
gen_camel_provider_FeatCardinality_Cardinality = Generalization(general=Cardinality, specific=camel_provider_FeatCardinality)
gen_camel_provider_GroupCardinality_Cardinality = Generalization(general=Cardinality, specific=camel_provider_GroupCardinality)
gen_camel_provider_Functional_Requires = Generalization(general=Requires, specific=camel_provider_Functional)
gen_camel_provider_Excludes_Constraint = Generalization(general=Constraint, specific=camel_provider_Excludes)
gen_camel_provider_Implies_Constraint = Generalization(general=Constraint, specific=camel_provider_Implies)
gen_camel_provider_Requires_Constraint = Generalization(general=Constraint, specific=camel_provider_Requires)
gen_camel_provider_Exclusive_Alternative = Generalization(general=Alternative, specific=camel_provider_Exclusive)
gen_camel_provider_Instance_Scope = Generalization(general=Scope, specific=camel_provider_Instance)
gen_camel_provider_Product_Scope = Generalization(general=Scope, specific=camel_provider_Product)
gen_camel_requirement_RequirementModel_Model = Generalization(general=Model, specific=camel_requirement_RequirementModel)
gen_camel_provider_Alternative_Feature = Generalization(general=Feature, specific=camel_provider_Alternative)
gen_camel_requirement_RequirementGroup_Requirement = Generalization(general=Requirement, specific=camel_requirement_RequirementGroup)
gen_camel_requirement_HardRequirement_Requirement = Generalization(general=Requirement, specific=camel_requirement_HardRequirement)
gen_camel_requirement_SoftRequirement_Requirement = Generalization(general=Requirement, specific=camel_requirement_SoftRequirement)
gen_camel_requirement_ServiceLevelObjective_HardRequirement = Generalization(general=HardRequirement, specific=camel_requirement_ServiceLevelObjective)
gen_camel_requirement_OptimisationRequirement_SoftRequirement = Generalization(general=SoftRequirement, specific=camel_requirement_OptimisationRequirement)
gen_camel_requirement_HardwareRequirement_HardRequirement = Generalization(general=HardRequirement, specific=camel_requirement_HardwareRequirement)
gen_camel_requirement_QualitativeHardwareRequirement_HardwareRequirement = Generalization(general=HardwareRequirement, specific=camel_requirement_QualitativeHardwareRequirement)
gen_camel_requirement_QuantitativeHardwareRequirement_HardwareRequirement = Generalization(general=HardwareRequirement, specific=camel_requirement_QuantitativeHardwareRequirement)
gen_camel_requirement_ProviderRequirement_HardRequirement = Generalization(general=HardRequirement, specific=camel_requirement_ProviderRequirement)
gen_camel_requirement_OSOrImageRequirement_HardRequirement = Generalization(general=HardRequirement, specific=camel_requirement_OSOrImageRequirement)
gen_camel_requirement_OSRequirement_OSOrImageRequirement = Generalization(general=OSOrImageRequirement, specific=camel_requirement_OSRequirement)
gen_camel_requirement_SecurityRequirement_HardRequirement = Generalization(general=HardRequirement, specific=camel_requirement_SecurityRequirement)
gen_camel_requirement_LocationRequirement_HardRequirement = Generalization(general=HardRequirement, specific=camel_requirement_LocationRequirement)
gen_camel_requirement_ScaleRequirement_HardRequirement = Generalization(general=HardRequirement, specific=camel_requirement_ScaleRequirement)
gen_camel_requirement_ImageRequirement_OSOrImageRequirement = Generalization(general=OSOrImageRequirement, specific=camel_requirement_ImageRequirement)
gen_camel_requirement_VerticalScaleRequirement_ScaleRequirement = Generalization(general=ScaleRequirement, specific=camel_requirement_VerticalScaleRequirement)
gen_camel_requirement_HorizontalScaleRequirement_ScaleRequirement = Generalization(general=ScaleRequirement, specific=camel_requirement_HorizontalScaleRequirement)
gen_camel_scalability_ScalabilityModel_Model = Generalization(general=Model, specific=camel_scalability_ScalabilityModel)
gen_camel_scalability_EventPattern_Event = Generalization(general=Event, specific=camel_scalability_EventPattern)
gen_camel_scalability_UnaryEventPattern_EventPattern = Generalization(general=EventPattern, specific=camel_scalability_UnaryEventPattern)
gen_camel_scalability_BinaryEventPattern_EventPattern = Generalization(general=EventPattern, specific=camel_scalability_BinaryEventPattern)
gen_camel_scalability_NonFunctionalEvent_SimpleEvent = Generalization(general=SimpleEvent, specific=camel_scalability_NonFunctionalEvent)
gen_camel_scalability_SimpleEvent_Event = Generalization(general=Event, specific=camel_scalability_SimpleEvent)
gen_camel_scalability_FunctionalEvent_SimpleEvent = Generalization(general=SimpleEvent, specific=camel_scalability_FunctionalEvent)
gen_camel_scalability_ScalingAction_Action = Generalization(general=Action, specific=camel_scalability_ScalingAction)
gen_camel_scalability_HorizontalScalingAction_ScalingAction = Generalization(general=ScalingAction, specific=camel_scalability_HorizontalScalingAction)
gen_camel_scalability_VerticalScalingAction_ScalingAction = Generalization(general=ScalingAction, specific=camel_scalability_VerticalScalingAction)
gen_camel_security_SecurityModel_Model = Generalization(general=Model, specific=camel_security_SecurityModel)
gen_camel_security_RawSecurityMetricInstance_RawMetricInstance = Generalization(general=RawMetricInstance, specific=camel_security_RawSecurityMetricInstance)
gen_camel_security_RawSecurityMetric_RawMetric = Generalization(general=RawMetric, specific=camel_security_RawSecurityMetric)
gen_camel_security_SecurityProperty_Property = Generalization(general=Property_, specific=camel_security_SecurityProperty)
gen_camel_security_Certifiable_SecurityProperty = Generalization(general=SecurityProperty, specific=camel_security_Certifiable)
gen_camel_security_SecuritySLO_ServiceLevelObjective = Generalization(general=ServiceLevelObjective, specific=camel_security_SecuritySLO)
gen_camel_type_TypeModel_Model = Generalization(general=Model, specific=camel_type_TypeModel)
gen_camel_type_BoolValue_SingleValue = Generalization(general=SingleValue, specific=camel_type_BoolValue)
gen_camel_type_EnumerateValue_SingleValue = Generalization(general=SingleValue, specific=camel_type_EnumerateValue)
gen_camel_type_NumericValue_SingleValue = Generalization(general=SingleValue, specific=camel_type_NumericValue)
gen_camel_type_IntegerValue_NumericValue = Generalization(general=NumericValue, specific=camel_type_IntegerValue)
gen_camel_type_FloatsValue_NumericValue = Generalization(general=NumericValue, specific=camel_type_FloatsValue)
gen_camel_security_CompositeSecurityMetric_CompositeMetric = Generalization(general=CompositeMetric, specific=camel_security_CompositeSecurityMetric)
gen_camel_security_CompositeSecurityMetricInstance_CompositeMetricInstance = Generalization(general=CompositeMetricInstance, specific=camel_security_CompositeSecurityMetricInstance)
gen_camel_type_Enumeration_ValueType = Generalization(general=ValueType, specific=camel_type_Enumeration)
gen_camel_type_List_ValueType = Generalization(general=ValueType, specific=camel_type_List)
gen_camel_type_Range_ValueType = Generalization(general=ValueType, specific=camel_type_Range)
gen_camel_type_DoublePrecisionValue_NumericValue = Generalization(general=NumericValue, specific=camel_type_DoublePrecisionValue)
gen_camel_type_NegativeInf_NumericValue = Generalization(general=NumericValue, specific=camel_type_NegativeInf)
gen_camel_type_PositiveInf_NumericValue = Generalization(general=NumericValue, specific=camel_type_PositiveInf)
gen_camel_type_ValueToIncrease_NumericValue = Generalization(general=NumericValue, specific=camel_type_ValueToIncrease)
gen_camel_type_StringsValue_SingleValue = Generalization(general=SingleValue, specific=camel_type_StringsValue)
gen_camel_type_BooleanValueType_ValueType = Generalization(general=ValueType, specific=camel_type_BooleanValueType)
gen_camel_type_RangeUnion_ValueType = Generalization(general=ValueType, specific=camel_type_RangeUnion)
gen_camel_type_StringValueType_ValueType = Generalization(general=ValueType, specific=camel_type_StringValueType)
gen_camel_unit_UnitModel_Model = Generalization(general=Model, specific=camel_unit_UnitModel)
gen_camel_unit_CoreUnit_Unit = Generalization(general=Unit, specific=camel_unit_CoreUnit)
gen_camel_unit_Dimensionless_Unit = Generalization(general=Unit, specific=camel_unit_Dimensionless)
gen_camel_unit_MonetaryUnit_Unit = Generalization(general=Unit, specific=camel_unit_MonetaryUnit)
gen_camel_unit_RequestUnit_Unit = Generalization(general=Unit, specific=camel_unit_RequestUnit)
gen_camel_unit_StorageUnit_Unit = Generalization(general=Unit, specific=camel_unit_StorageUnit)
gen_camel_unit_ThroughputUnit_Unit = Generalization(general=Unit, specific=camel_unit_ThroughputUnit)
gen_camel_unit_TimeIntervalUnit_Unit = Generalization(general=Unit, specific=camel_unit_TimeIntervalUnit)
gen_camel_unit_TransactionUnit_Unit = Generalization(general=Unit, specific=camel_unit_TransactionUnit)

# Domain Model
domain_model = DomainModel(
    name="camel",
    types={camel_Model, camel_CamelModel, Model, camel_Action, camel_Application, ExecutionModel, LocationModel, MetricModel, OrganisationModel, ProviderModel, RequirementModel, ScalabilityModel, SecurityModel, DeploymentModel, TypeModel, UnitModel, VM, Entity, VMInstance, Communication, CommunicationInstance, camel_deployment_DeploymentElement, camel_deployment_DeploymentModel, InternalComponent, InternalComponentInstance, camel_deployment_InternalComponent, Component, Hosting, RequiredCommunication, HostingInstance, VMRequirementSet, camel_deployment_Component, DeploymentElement, ProvidedCommunication, ProvidedHost, Configuration, LocationRequirement, ProviderRequirement, QualitativeHardwareRequirement, QuantitativeHardwareRequirement, OSOrImageRequirement, RequiredHost, camel_deployment_VM, camel_deployment_VMRequirementSet, camel_deployment_CommunicationPort, camel_deployment_ProvidedCommunication, CommunicationPort, camel_deployment_RequiredCommunication, camel_deployment_Hosting, camel_deployment_HostingPort, camel_deployment_ProvidedHost, camel_deployment_Configuration, HostingPort, camel_deployment_RequiredHost, camel_deployment_Communication, camel_deployment_InternalComponentInstance, ComponentInstance, RequiredCommunicationInstance, RequiredHostInstance, camel_deployment_VMInstance, camel_deployment_ComponentInstance, ProvidedCommunicationInstance, ProvidedHostInstance, camel_deployment_CommunicationPortInstance, camel_deployment_ProvidedCommunicationInstance, CommunicationPortInstance, camel_deployment_RequiredCommunicationInstance, camel_deployment_HostingInstance, camel_deployment_HostingPortInstance, camel_deployment_ProvidedHostInstance, HostingPortInstance, camel_deployment_RequiredHostInstance, Attribute, SingleValue, camel_deployment_CommunicationInstance, camel_execution_ExecutionContext, execution_camel_Application, MonetaryUnit, RequirementGroup, camel_execution_Measurement, camel_execution_ExecutionModel, ActionRealisation, EventInstance, ExecutionContext, Measurement, SLOAssessment, RuleTrigger, camel_execution_ActionRealisation, execution_camel_Action, camel_execution_InternalComponentMeasurement, camel_execution_CommunicationMeasurement, camel_execution_VMMeasurement, camel_execution_SLOAssessment, MetricInstance, ServiceLevelObjective, camel_execution_ApplicationMeasurement, ScalabilityRule, camel_location_LocationModel, CloudLocation, Country, camel_execution_RuleTrigger, camel_location_GeographicalRegion, camel_location_Country, GeographicalRegion, camel_location_Location, camel_location_CloudLocation, Location, MetricContext, camel_metric_PropertyCondition, PropertyContext, TimeIntervalUnit, camel_metric_MetricInstance, camel_metric_Condition, camel_metric_MetricCondition, Condition, MetricObjectBinding, camel_metric_CompositeMetricInstance, camel_metric_RawMetricInstance, Sensor, camel_metric_MetricFormulaParameter, Metric, Schedule, Window, ValueType, Unit, Property_, camel_metric_CompositeMetric, camel_metric_MetricFormula, MetricFormulaParameter, camel_metric_Metric, camel_metric_MetricObjectBinding, camel_metric_MetricApplicationBinding, camel_metric_MetricComponentBinding, camel_metric_MetricVMBinding, camel_metric_Property, MetricFormula, camel_metric_RawMetric, camel_metric_Sensor, camel_metric_Window, camel_metric_Schedule, metric_camel_Application, camel_metric_MetricModel, ConditionContext, camel_metric_ConditionContext, camel_metric_CompositeMetricContext, camel_metric_RawMetricContext, camel_metric_PropertyContext, camel_metric_MetricContext, DataCenter, Role, RoleAssignment, Permission, ResourceFilter, camel_organisation_Credentials, camel_organisation_CloudCredentials, Credentials, camel_organisation_OrganisationModel, Organisation, CloudProvider, ExternalIdentifier, User, UserGroup, SecurityCapability, camel_organisation_User, CloudCredentials, PaaSageCredentials, camel_organisation_ExternalIdentifier, camel_organisation_DataCenter, camel_organisation_Entity, camel_organisation_Organisation, camel_organisation_CloudProvider, camel_organisation_ResourceFilter, camel_organisation_InformationResourceFilter, camel_organisation_ServiceResourceFilter, camel_organisation_Role, camel_organisation_RoleAssignment, camel_organisation_Permission, camel_provider_ProviderModel, Constraint, Feature, camel_provider_Attribute, camel_organisation_UserGroup, camel_organisation_PaaSageCredentials, camel_provider_FeatCardinality, Cardinality, camel_provider_GroupCardinality, camel_provider_Clone, Clone, camel_provider_Constraint, camel_provider_AttributeConstraint, camel_provider_Cardinality, Scope, FeatCardinality, camel_provider_Functional, Requires, camel_provider_Feature, AttributeConstraint, camel_provider_Excludes, camel_provider_Implies, camel_provider_Requires, camel_provider_Exclusive, Alternative, camel_provider_Scope, camel_provider_Instance, camel_provider_Product, camel_requirement_RequirementModel, Requirement, camel_requirement_Requirement, camel_requirement_RequirementGroup, camel_provider_Alternative, GroupCardinality, camel_requirement_HardRequirement, camel_requirement_SoftRequirement, requirement_camel_Application, camel_requirement_ServiceLevelObjective, HardRequirement, camel_requirement_OptimisationRequirement, SoftRequirement, camel_requirement_HardwareRequirement, camel_requirement_QualitativeHardwareRequirement, HardwareRequirement, camel_requirement_QuantitativeHardwareRequirement, camel_requirement_ProviderRequirement, camel_requirement_OSOrImageRequirement, camel_requirement_OSRequirement, camel_requirement_SecurityRequirement, SecurityControl, camel_requirement_LocationRequirement, camel_requirement_ScaleRequirement, camel_requirement_HorizontalScaleRequirement, camel_requirement_ImageRequirement, camel_requirement_VerticalScaleRequirement, ScaleRequirement, camel_scalability_ScalabilityModel, Event, ScalingAction, camel_scalability_Event, camel_scalability_EventPattern, EventPattern, Timer, camel_scalability_UnaryEventPattern, camel_scalability_BinaryEventPattern, MetricCondition, camel_scalability_EventInstance, camel_scalability_SimpleEvent, camel_scalability_FunctionalEvent, SimpleEvent, camel_scalability_NonFunctionalEvent, scalability_camel_Action, camel_scalability_ScalingAction, Action, camel_scalability_HorizontalScalingAction, camel_scalability_ScalabilityRule, camel_scalability_Timer, camel_scalability_VerticalScalingAction, camel_security_SecurityModel, SecurityRequirement, SecurityProperty, RawSecurityMetric, CompositeSecurityMetricInstance, SecurityDomain, SecuritySLO, camel_security_SecurityDomain, CompositeSecurityMetric, RawSecurityMetricInstance, camel_security_RawSecurityMetricInstance, RawMetricInstance, camel_security_RawSecurityMetric, RawMetric, camel_security_SecurityProperty, camel_security_Certifiable, camel_security_SecuritySLO, camel_security_SecurityCapability, camel_security_SecurityControl, camel_type_TypeModel, camel_type_Limit, NumericValue, camel_type_SingleValue, camel_type_BoolValue, camel_type_EnumerateValue, camel_type_NumericValue, camel_type_IntegerValue, camel_type_FloatsValue, camel_security_CompositeSecurityMetric, CompositeMetric, camel_security_CompositeSecurityMetricInstance, CompositeMetricInstance, camel_type_Enumeration, EnumerateValue, camel_type_List, camel_type_Range, camel_type_DoublePrecisionValue, camel_type_NegativeInf, camel_type_PositiveInf, camel_type_ValueToIncrease, camel_type_StringsValue, camel_type_ValueType, camel_type_BooleanValueType, camel_type_RangeUnion, Range, camel_type_StringValueType, camel_unit_Unit, Limit, camel_unit_UnitModel, camel_unit_CoreUnit, camel_unit_Dimensionless, camel_unit_MonetaryUnit, camel_unit_RequestUnit, camel_unit_StorageUnit, camel_unit_ThroughputUnit, camel_unit_TimeIntervalUnit, camel_unit_TransactionUnit, ActionType, LayerType, CommunicationType, ComparisonOperatorType, MetricFunctionArityType, MetricFunctionType, ScheduleType, PropertyType, QuantifierType, WindowSizeType, WindowType, FunctionPatternType, ResourcePattern, SecurityLevel, Operator, RequirementOperatorType, OptimisationFunctionType, BinaryPatternOperatorType, TimerType, UnaryPatternOperatorType, StatusType, TypeEnum, UnitDimensionType, UnitType},
    associations={actions0, executionModels5, locationModels7, metricModels9, organisationModels11, providerModels13, requirementModels15, applications1, scalabilityModels17, securityModels19, deploymentModels3, unitModels23, typeModels21, vms33, owner25, vmInstances35, communications37, deploymentModels27, communicationInstances39, internalComponents30, internalComponentInstances31, compositeInternalComponents55, hostings41, requiredCommunications57, hostingInstances43, vmRequirementSets45, globalVMRequirementSet47, providedCommunications50, providedHosts51, configurations53, locationRequirement63, providerRequirement64, qualitativeHardwareRequirement66, quantitativeHardwareRequirement68, requiredHost59, vmRequirementSet61, requiredPortConfiguration80, providedHost83, requiredHost85, providedHostConfiguration88, requiredHostConfiguration91, osOrImageRequirement70, providedCommunication72, requiredCommunication74, providedPortConfiguration77, requiredCommunicationInstances99, requiredHostInstance100, type94, providedCommunicationInstances95, type105, providedHostInstances97, providedCommunicationInstance107, requiredCommunicationInstance110, type113, type114, providedHostInstance116, requiredHostInstance119, type122, vmType102, vmTypeValue103, application135, costUnit136, deploymentModel138, requirementGroup141, executionContext143, actionRealisations123, eventInstances124, executionContexts126, measurements128, sloAssessessments130, ruleTriggers132, action134, internalComponentInstance154, sourceVMInstance156, destinationVMInstance158, vmInstance161, slo163, metricInstance145, slo147, eventInstance149, application152, scalabilityRule171, eventInstances172, actionRealisations175, executionContext178, cloudLocations181, countries182, executionContext165, measurement168, subLocations186, parent188, geographicalRegion191, parentRegions194, regions184, metricContext196, propertyContext197, unit198, timeUnit201, window206, objectBinding208, metricContext210, composingMetricInstances213, sensor215, value216, metric203, schedule204, valueType219, unit220, property222, parameters218, executionContext225, vmInstance227, componentInstance229, vmInstance231, formula224, unit238, subProperties233, sensors235, component242, application244, contexts246, metrics247, metricInstances250, conditions253, unit240, metric276, window278, schedule281, composingMetricContexts284, sensor286, property288, properties255, bindings258, windows261, schedules264, parameters267, sensors270, units273, dataCentres299, roles301, roleAssigments303, permissions305, resourceFilters307, cloudProvider309, organisation290, provider291, externalIdentifiers293, users295, userGroups297, providerModel312, securityCapability314, externalIdentifiers316, requirementModels318, cloudCredentials321, deploymentModels323, paasageCredentials326, location311, role328, resourceFilter330, constraints343, rootFeature344, value346, valueType348, user333, role335, userGroup338, users341, subClones362, from351, to353, fromValue356, toValue359, scopeFrom370, scopeTo371, cardFrom374, cardTo376, from363, to365, attributeConstraints368, variants391, feature394, requirements396, attributes379, subFeatures381, featureCardinality384, clones387, groupCardinality390, requirements397, application399, customServiceLevel401, metric403, metricContext414, property405, application408, component411, providers417, securityControls419, application420, component423, locations426, component428, rules432, events434, eventInstances436, actions439, vm430, patterns441, timers443, scaleRequirements445, leftEvent449, rightEvent451, event454, timer447, metricCondition456, event461, actions463, entity465, scaleRequirements468, vm471, event457, metricInstance458, unit475, internalComponent473, securityControls477, securityRequirements479, securityProperties481, rawSecurityMetrics483, compositeSecurityMetricInstances489, securityDomains491, securityCapabilities493, securitySLOs496, compositeSecurityMetrics485, rawSecurityMetricInstances487, securityProperties505, rawSecurityMetrics508, compositeSecurityMetrics511, domain514, securityControls516, subDomain498, domain500, subDomain502, dataTypes521, values523, value526, dataCenter518, values529, values530, type532, value527, upperLimit536, ranges539, lowerLimit535, units540},
    generalizations={gen_camel_CamelModel_Model, gen_camel_deployment_DeploymentModel_Model, gen_camel_deployment_InternalComponent_Component, gen_camel_deployment_Component_DeploymentElement, gen_camel_deployment_VM_Component, gen_camel_deployment_CommunicationPort_DeploymentElement, gen_camel_deployment_ProvidedCommunication_CommunicationPort, gen_camel_deployment_RequiredCommunication_CommunicationPort, gen_camel_deployment_Hosting_DeploymentElement, gen_camel_deployment_HostingPort_DeploymentElement, gen_camel_deployment_Configuration_DeploymentElement, gen_camel_deployment_ProvidedHost_HostingPort, gen_camel_deployment_RequiredHost_HostingPort, gen_camel_deployment_Communication_DeploymentElement, gen_camel_deployment_InternalComponentInstance_ComponentInstance, gen_camel_deployment_VMInstance_ComponentInstance, gen_camel_deployment_ComponentInstance_DeploymentElement, gen_camel_deployment_CommunicationPortInstance_DeploymentElement, gen_camel_deployment_ProvidedCommunicationInstance_CommunicationPortInstance, gen_camel_deployment_RequiredCommunicationInstance_CommunicationPortInstance, gen_camel_deployment_HostingInstance_DeploymentElement, gen_camel_deployment_HostingPortInstance_DeploymentElement, gen_camel_deployment_ProvidedHostInstance_HostingPortInstance, gen_camel_deployment_RequiredHostInstance_HostingPortInstance, gen_camel_deployment_CommunicationInstance_DeploymentElement, gen_camel_execution_ExecutionModel_Model, gen_camel_execution_InternalComponentMeasurement_Measurement, gen_camel_execution_CommunicationMeasurement_Measurement, gen_camel_execution_VMMeasurement_Measurement, gen_camel_execution_ApplicationMeasurement_Measurement, gen_camel_location_LocationModel_Model, gen_camel_location_GeographicalRegion_Location, gen_camel_location_Country_GeographicalRegion, gen_camel_location_CloudLocation_Location, gen_camel_metric_PropertyCondition_Condition, gen_camel_metric_MetricCondition_Condition, gen_camel_metric_CompositeMetricInstance_MetricInstance, gen_camel_metric_RawMetricInstance_MetricInstance, gen_camel_metric_CompositeMetric_Metric, gen_camel_metric_MetricFormula_MetricFormulaParameter, gen_camel_metric_Metric_MetricFormulaParameter, gen_camel_metric_MetricApplicationBinding_MetricObjectBinding, gen_camel_metric_MetricComponentBinding_MetricObjectBinding, gen_camel_metric_MetricVMBinding_MetricObjectBinding, gen_camel_metric_RawMetric_Metric, gen_camel_metric_MetricModel_Model, gen_camel_metric_CompositeMetricContext_MetricContext, gen_camel_metric_RawMetricContext_MetricContext, gen_camel_metric_PropertyContext_ConditionContext, gen_camel_metric_MetricContext_ConditionContext, gen_camel_organisation_CloudCredentials_Credentials, gen_camel_organisation_OrganisationModel_Model, gen_camel_organisation_User_Entity, gen_camel_organisation_Organisation_Entity, gen_camel_organisation_CloudProvider_Organisation, gen_camel_organisation_InformationResourceFilter_ResourceFilter, gen_camel_organisation_ServiceResourceFilter_ResourceFilter, gen_camel_provider_ProviderModel_Model, gen_camel_organisation_PaaSageCredentials_Credentials, gen_camel_provider_FeatCardinality_Cardinality, gen_camel_provider_GroupCardinality_Cardinality, gen_camel_provider_Functional_Requires, gen_camel_provider_Excludes_Constraint, gen_camel_provider_Implies_Constraint, gen_camel_provider_Requires_Constraint, gen_camel_provider_Exclusive_Alternative, gen_camel_provider_Instance_Scope, gen_camel_provider_Product_Scope, gen_camel_requirement_RequirementModel_Model, gen_camel_provider_Alternative_Feature, gen_camel_requirement_RequirementGroup_Requirement, gen_camel_requirement_HardRequirement_Requirement, gen_camel_requirement_SoftRequirement_Requirement, gen_camel_requirement_ServiceLevelObjective_HardRequirement, gen_camel_requirement_OptimisationRequirement_SoftRequirement, gen_camel_requirement_HardwareRequirement_HardRequirement, gen_camel_requirement_QualitativeHardwareRequirement_HardwareRequirement, gen_camel_requirement_QuantitativeHardwareRequirement_HardwareRequirement, gen_camel_requirement_ProviderRequirement_HardRequirement, gen_camel_requirement_OSOrImageRequirement_HardRequirement, gen_camel_requirement_OSRequirement_OSOrImageRequirement, gen_camel_requirement_SecurityRequirement_HardRequirement, gen_camel_requirement_LocationRequirement_HardRequirement, gen_camel_requirement_ScaleRequirement_HardRequirement, gen_camel_requirement_ImageRequirement_OSOrImageRequirement, gen_camel_requirement_VerticalScaleRequirement_ScaleRequirement, gen_camel_requirement_HorizontalScaleRequirement_ScaleRequirement, gen_camel_scalability_ScalabilityModel_Model, gen_camel_scalability_EventPattern_Event, gen_camel_scalability_UnaryEventPattern_EventPattern, gen_camel_scalability_BinaryEventPattern_EventPattern, gen_camel_scalability_NonFunctionalEvent_SimpleEvent, gen_camel_scalability_SimpleEvent_Event, gen_camel_scalability_FunctionalEvent_SimpleEvent, gen_camel_scalability_ScalingAction_Action, gen_camel_scalability_HorizontalScalingAction_ScalingAction, gen_camel_scalability_VerticalScalingAction_ScalingAction, gen_camel_security_SecurityModel_Model, gen_camel_security_RawSecurityMetricInstance_RawMetricInstance, gen_camel_security_RawSecurityMetric_RawMetric, gen_camel_security_SecurityProperty_Property, gen_camel_security_Certifiable_SecurityProperty, gen_camel_security_SecuritySLO_ServiceLevelObjective, gen_camel_type_TypeModel_Model, gen_camel_type_BoolValue_SingleValue, gen_camel_type_EnumerateValue_SingleValue, gen_camel_type_NumericValue_SingleValue, gen_camel_type_IntegerValue_NumericValue, gen_camel_type_FloatsValue_NumericValue, gen_camel_security_CompositeSecurityMetric_CompositeMetric, gen_camel_security_CompositeSecurityMetricInstance_CompositeMetricInstance, gen_camel_type_Enumeration_ValueType, gen_camel_type_List_ValueType, gen_camel_type_Range_ValueType, gen_camel_type_DoublePrecisionValue_NumericValue, gen_camel_type_NegativeInf_NumericValue, gen_camel_type_PositiveInf_NumericValue, gen_camel_type_ValueToIncrease_NumericValue, gen_camel_type_StringsValue_SingleValue, gen_camel_type_BooleanValueType_ValueType, gen_camel_type_RangeUnion_ValueType, gen_camel_type_StringValueType_ValueType, gen_camel_unit_UnitModel_Model, gen_camel_unit_CoreUnit_Unit, gen_camel_unit_Dimensionless_Unit, gen_camel_unit_MonetaryUnit_Unit, gen_camel_unit_RequestUnit_Unit, gen_camel_unit_StorageUnit_Unit, gen_camel_unit_ThroughputUnit_Unit, gen_camel_unit_TimeIntervalUnit_Unit, gen_camel_unit_TransactionUnit_Unit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)