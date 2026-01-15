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
ServiceType: Enumeration = Enumeration(
    name="ServiceType",
    literals={
            EnumerationLiteral(name="internal"),
			EnumerationLiteral(name="external")
    }
)

ServiceImpLanguage: Enumeration = Enumeration(
    name="ServiceImpLanguage",
    literals={
            EnumerationLiteral(name="Java_EJB"),
			EnumerationLiteral(name="Java_JSP")
    }
)

StyleEncoding: Enumeration = Enumeration(
    name="StyleEncoding",
    literals={
            EnumerationLiteral(name="Document_Literal"),
			EnumerationLiteral(name="RPC_Encoded")
    }
)

TransportProtocol: Enumeration = Enumeration(
    name="TransportProtocol",
    literals={
            EnumerationLiteral(name="SOAP"),
			EnumerationLiteral(name="HTTP"),
			EnumerationLiteral(name="MIME")
    }
)

ContainerType: Enumeration = Enumeration(
    name="ContainerType",
    literals={
            EnumerationLiteral(name="axis")
    }
)

# Classes
service_ServiceProvider = Class(name="service::ServiceProvider", is_abstract=True)
Agent = Class(name="Agent")
service_ServiceImplemetation = Class(name="service::ServiceImplemetation")
service_ServiceConsumer = Class(name="service::ServiceConsumer")
service_Service = Class(name="service::Service")
Endpoint = Class(name="Endpoint")
InterfaceDescription = Class(name="InterfaceDescription")
ServiceProfile = Class(name="ServiceProfile")
ServiceGrounding = Class(name="ServiceGrounding")
ProcessModel = Class(name="ProcessModel")
GroundTemplate = Class(name="GroundTemplate")
syntax_service_SchemaType = Class(name="syntax::service::SchemaType")
service_syntax_OperationDescription = Class(name="service::syntax::OperationDescription")
Message = Class(name="Message")
service_syntax_Message = Class(name="service::syntax::Message")
syntax_service_TopLevelComplexType = Class(name="syntax::service::TopLevelComplexType")
service_SL = Class(name="service::SL")
ServiceFramework = Class(name="ServiceFramework")
service_syntax_InterfaceDescription = Class(name="service::syntax::InterfaceDescription")
OperationDescription = Class(name="OperationDescription")
Binding = Class(name="Binding")
syntax_service_TopLevelElement = Class(name="syntax::service::TopLevelElement")
service_syntax_Endpoint = Class(name="service::syntax::Endpoint")
syntax_service_ServiceImplemetation = Class(name="syntax::service::ServiceImplemetation")
DeployedService = Class(name="DeployedService")
service_syntax_Binding = Class(name="service::syntax::Binding")
ServiceResult = Class(name="ServiceResult")
ServiceCondition = Class(name="ServiceCondition")
service_semantics_ServiceGrounding = Class(name="service::semantics::ServiceGrounding")
service_semantics_ServiceProfile = Class(name="service::semantics::ServiceProfile")
semantics_service_Service = Class(name="semantics::service::Service")
ServiceCategory = Class(name="ServiceCategory")
ServiceInput = Class(name="ServiceInput")
ServiceOutput = Class(name="ServiceOutput")
service_semantics_ServiceResult = Class(name="service::semantics::ServiceResult")
semantics_service_Consequent = Class(name="semantics::service::Consequent")
service_semantics_IOEP = Class(name="service::semantics::IOEP", is_abstract=True)
service_semantics_ProcessModel = Class(name="service::semantics::ProcessModel")
IOEP = Class(name="IOEP")
service_semantics_ServiceCategory = Class(name="service::semantics::ServiceCategory")
service_semantics_ServiceParameter = Class(name="service::semantics::ServiceParameter", is_abstract=True)
semantics_service_EObject = Class(name="semantics::service::EObject")
service_semantics_ServiceInput = Class(name="service::semantics::ServiceInput")
ServiceParameter = Class(name="ServiceParameter")
service_semantics_ServiceOutput = Class(name="service::semantics::ServiceOutput")
service_semantics_ServiceCondition = Class(name="service::semantics::ServiceCondition")
semantics_service_Antecedent = Class(name="semantics::service::Antecedent")
template_service_Service = Class(name="template::service::Service")
service_template_AbstractProcessModel = Class(name="service::template::AbstractProcessModel")
service_template_BoundTemplateParameter = Class(name="service::template::BoundTemplateParameter")
service_template_BoundProcessModel = Class(name="service::template::BoundProcessModel")
service_template_TemplateConstraint = Class(name="service::template::TemplateConstraint")
service_template_ServiceTemplate = Class(name="service::template::ServiceTemplate")
template_service_Antecedent = Class(name="template::service::Antecedent")
TemplateFlow = Class(name="TemplateFlow")
service_template_ControlConstruct = Class(name="service::template::ControlConstruct", is_abstract=True)
AbstractProcessModel = Class(name="AbstractProcessModel")
TemplateConstraint = Class(name="TemplateConstraint")
service_template_TemplateFlow = Class(name="service::template::TemplateFlow")
ControlConstruct = Class(name="ControlConstruct")
service_template_GroundTemplate = Class(name="service::template::GroundTemplate")
ServiceTemplate = Class(name="ServiceTemplate")
BoundTemplateParameter = Class(name="BoundTemplateParameter")
BoundProcessModel = Class(name="BoundProcessModel")
service_template_Iterate = Class(name="service::template::Iterate", is_abstract=True)
service_template_Perform = Class(name="service::template::Perform")
service_template_RepeatUntil = Class(name="service::template::RepeatUntil")
Iterate = Class(name="Iterate")
service_template_RepeatWhile = Class(name="service::template::RepeatWhile")
IntervalThing = Class(name="IntervalThing")
service_template_AnyOrder = Class(name="service::template::AnyOrder")
ControlConstructBag = Class(name="ControlConstructBag")
service_template_Choice = Class(name="service::template::Choice")
service_template_IfThenElse = Class(name="service::template::IfThenElse")
service_template_ControlConstructBag = Class(name="service::template::ControlConstructBag")
service_template_IntervalThing = Class(name="service::template::IntervalThing")
service_architecture_ServiceFramework = Class(name="service::architecture::ServiceFramework")
ServiceTemplateMatchmaker = Class(name="ServiceTemplateMatchmaker")
ExecutionFramework = Class(name="ExecutionFramework")
ServiceDirectory = Class(name="ServiceDirectory")
TemplateRepository = Class(name="TemplateRepository")
service_template_Sequence = Class(name="service::template::Sequence")
ControlConstructList = Class(name="ControlConstructList")
service_template_Split = Class(name="service::template::Split")
service_template_SplitJoin = Class(name="service::template::SplitJoin")
service_template_ControlConstructList = Class(name="service::template::ControlConstructList")
service_architecture_ExecutionFramework = Class(name="service::architecture::ExecutionFramework")
service_architecture_DeployedService = Class(name="service::architecture::DeployedService")
service_architecture_TemplateRepository = Class(name="service::architecture::TemplateRepository")
service_architecture_TemplateMatchmaker = Class(name="service::architecture::TemplateMatchmaker")
service_architecture_ServiceMatchmaker = Class(name="service::architecture::ServiceMatchmaker")
service_architecture_ServiceTemplateMatchmaker = Class(name="service::architecture::ServiceTemplateMatchmaker")
architecture_ServiceMatchmaker = Class(name="architecture::ServiceMatchmaker")
architecture_TemplateMatchmaker = Class(name="architecture::TemplateMatchmaker")
service_architecture_ServiceDirectory = Class(name="service::architecture::ServiceDirectory")

# service_ServiceProvider class attributes and methods
service_ServiceProvider_isType: Property = Property(name="isType", type=StringType)
service_ServiceProvider.attributes={service_ServiceProvider_isType}

# Agent class attributes and methods

# service_ServiceImplemetation class attributes and methods
service_ServiceImplemetation_language: Property = Property(name="language", type=StringType)
service_ServiceImplemetation_uri: Property = Property(name="uri", type=StringType)
service_ServiceImplemetation.attributes={service_ServiceImplemetation_language, service_ServiceImplemetation_uri}

# service_ServiceConsumer class attributes and methods
service_ServiceConsumer_isType: Property = Property(name="isType", type=StringType)
service_ServiceConsumer.attributes={service_ServiceConsumer_isType}

# service_Service class attributes and methods
service_Service_name: Property = Property(name="name", type=StringType)
service_Service_namespace: Property = Property(name="namespace", type=StringType)
service_Service_description: Property = Property(name="description", type=StringType)
service_Service.attributes={service_Service_name, service_Service_description, service_Service_namespace}

# Endpoint class attributes and methods

# InterfaceDescription class attributes and methods

# ServiceProfile class attributes and methods

# ServiceGrounding class attributes and methods

# ProcessModel class attributes and methods

# GroundTemplate class attributes and methods

# syntax_service_SchemaType class attributes and methods

# service_syntax_OperationDescription class attributes and methods
service_syntax_OperationDescription_name: Property = Property(name="name", type=StringType)
service_syntax_OperationDescription.attributes={service_syntax_OperationDescription_name}

# Message class attributes and methods

# service_syntax_Message class attributes and methods
service_syntax_Message_name: Property = Property(name="name", type=StringType)
service_syntax_Message.attributes={service_syntax_Message_name}

# syntax_service_TopLevelComplexType class attributes and methods

# service_SL class attributes and methods

# ServiceFramework class attributes and methods

# service_syntax_InterfaceDescription class attributes and methods
service_syntax_InterfaceDescription_name: Property = Property(name="name", type=StringType)
service_syntax_InterfaceDescription.attributes={service_syntax_InterfaceDescription_name}

# OperationDescription class attributes and methods

# Binding class attributes and methods

# syntax_service_TopLevelElement class attributes and methods

# service_syntax_Endpoint class attributes and methods
service_syntax_Endpoint_name: Property = Property(name="name", type=StringType)
service_syntax_Endpoint_location: Property = Property(name="location", type=StringType)
service_syntax_Endpoint.attributes={service_syntax_Endpoint_name, service_syntax_Endpoint_location}

# syntax_service_ServiceImplemetation class attributes and methods

# DeployedService class attributes and methods

# service_syntax_Binding class attributes and methods
service_syntax_Binding_transport: Property = Property(name="transport", type=StringType)
service_syntax_Binding_style: Property = Property(name="style", type=StringType)
service_syntax_Binding_name: Property = Property(name="name", type=StringType)
service_syntax_Binding.attributes={service_syntax_Binding_name, service_syntax_Binding_style, service_syntax_Binding_transport}

# ServiceResult class attributes and methods

# ServiceCondition class attributes and methods

# service_semantics_ServiceGrounding class attributes and methods
service_semantics_ServiceGrounding_name: Property = Property(name="name", type=StringType)
service_semantics_ServiceGrounding_bindParams: Property = Property(name="bindParams", type=StringType)
service_semantics_ServiceGrounding.attributes={service_semantics_ServiceGrounding_name, service_semantics_ServiceGrounding_bindParams}

# service_semantics_ServiceProfile class attributes and methods
service_semantics_ServiceProfile_serviceClassification: Property = Property(name="serviceClassification", type=StringType)
service_semantics_ServiceProfile_name: Property = Property(name="name", type=StringType)
service_semantics_ServiceProfile.attributes={service_semantics_ServiceProfile_name, service_semantics_ServiceProfile_serviceClassification}

# semantics_service_Service class attributes and methods

# ServiceCategory class attributes and methods

# ServiceInput class attributes and methods

# ServiceOutput class attributes and methods

# service_semantics_ServiceResult class attributes and methods

# semantics_service_Consequent class attributes and methods

# service_semantics_IOEP class attributes and methods

# service_semantics_ProcessModel class attributes and methods
service_semantics_ProcessModel_name: Property = Property(name="name", type=StringType)
service_semantics_ProcessModel.attributes={service_semantics_ProcessModel_name}

# IOEP class attributes and methods

# service_semantics_ServiceCategory class attributes and methods
service_semantics_ServiceCategory_taxonomy: Property = Property(name="taxonomy", type=StringType)
service_semantics_ServiceCategory_value: Property = Property(name="value", type=StringType)
service_semantics_ServiceCategory_name: Property = Property(name="name", type=StringType)
service_semantics_ServiceCategory_code: Property = Property(name="code", type=StringType)
service_semantics_ServiceCategory.attributes={service_semantics_ServiceCategory_taxonomy, service_semantics_ServiceCategory_value, service_semantics_ServiceCategory_name, service_semantics_ServiceCategory_code}

# service_semantics_ServiceParameter class attributes and methods
service_semantics_ServiceParameter_name: Property = Property(name="name", type=StringType)
service_semantics_ServiceParameter.attributes={service_semantics_ServiceParameter_name}

# semantics_service_EObject class attributes and methods

# service_semantics_ServiceInput class attributes and methods

# ServiceParameter class attributes and methods

# service_semantics_ServiceOutput class attributes and methods

# service_semantics_ServiceCondition class attributes and methods

# semantics_service_Antecedent class attributes and methods

# template_service_Service class attributes and methods

# service_template_AbstractProcessModel class attributes and methods
service_template_AbstractProcessModel_name: Property = Property(name="name", type=StringType)
service_template_AbstractProcessModel.attributes={service_template_AbstractProcessModel_name}

# service_template_BoundTemplateParameter class attributes and methods

# service_template_BoundProcessModel class attributes and methods

# service_template_TemplateConstraint class attributes and methods

# service_template_ServiceTemplate class attributes and methods
service_template_ServiceTemplate_URI: Property = Property(name="URI", type=StringType)
service_template_ServiceTemplate.attributes={service_template_ServiceTemplate_URI}

# template_service_Antecedent class attributes and methods

# TemplateFlow class attributes and methods

# service_template_ControlConstruct class attributes and methods

# AbstractProcessModel class attributes and methods

# TemplateConstraint class attributes and methods

# service_template_TemplateFlow class attributes and methods

# ControlConstruct class attributes and methods

# service_template_GroundTemplate class attributes and methods
service_template_GroundTemplate_name: Property = Property(name="name", type=StringType)
service_template_GroundTemplate.attributes={service_template_GroundTemplate_name}

# ServiceTemplate class attributes and methods

# BoundTemplateParameter class attributes and methods

# BoundProcessModel class attributes and methods

# service_template_Iterate class attributes and methods

# service_template_Perform class attributes and methods

# service_template_RepeatUntil class attributes and methods

# Iterate class attributes and methods

# service_template_RepeatWhile class attributes and methods

# IntervalThing class attributes and methods

# service_template_AnyOrder class attributes and methods

# ControlConstructBag class attributes and methods

# service_template_Choice class attributes and methods

# service_template_IfThenElse class attributes and methods

# service_template_ControlConstructBag class attributes and methods

# service_template_IntervalThing class attributes and methods

# service_architecture_ServiceFramework class attributes and methods

# ServiceTemplateMatchmaker class attributes and methods

# ExecutionFramework class attributes and methods

# ServiceDirectory class attributes and methods

# TemplateRepository class attributes and methods

# service_template_Sequence class attributes and methods

# ControlConstructList class attributes and methods

# service_template_Split class attributes and methods

# service_template_SplitJoin class attributes and methods

# service_template_ControlConstructList class attributes and methods

# service_architecture_ExecutionFramework class attributes and methods
service_architecture_ExecutionFramework_container: Property = Property(name="container", type=StringType)
service_architecture_ExecutionFramework.attributes={service_architecture_ExecutionFramework_container}

# service_architecture_DeployedService class attributes and methods
service_architecture_DeployedService_artifact: Property = Property(name="artifact", type=StringType)
service_architecture_DeployedService.attributes={service_architecture_DeployedService_artifact}

# service_architecture_TemplateRepository class attributes and methods

# service_architecture_TemplateMatchmaker class attributes and methods

# service_architecture_ServiceMatchmaker class attributes and methods

# service_architecture_ServiceTemplateMatchmaker class attributes and methods

# architecture_ServiceMatchmaker class attributes and methods

# architecture_TemplateMatchmaker class attributes and methods

# service_architecture_ServiceDirectory class attributes and methods

# Relationships
exposes9: BinaryAssociation = BinaryAssociation(
    name="exposes9",
    ends={
        Property(name="service_Service10", type=service_ServiceProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="service_ServiceProvider", type=service_Service, multiplicity=Multiplicity(1, 9999))
    }
)
implementation11: BinaryAssociation = BinaryAssociation(
    name="implementation11",
    ends={
        Property(name="service_ServiceImplemetation", type=service_ServiceProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="service_ServiceProvider12", type=service_ServiceImplemetation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invokes13: BinaryAssociation = BinaryAssociation(
    name="invokes13",
    ends={
        Property(name="service_Service14", type=service_ServiceConsumer, multiplicity=Multiplicity(1, 1)),
        Property(name="service_ServiceConsumer", type=service_Service, multiplicity=Multiplicity(1, 9999))
    }
)
endpoint0: BinaryAssociation = BinaryAssociation(
    name="endpoint0",
    ends={
        Property(name="Endpoint", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Service", type=Endpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface1: BinaryAssociation = BinaryAssociation(
    name="interface1",
    ends={
        Property(name="InterfaceDescription", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Service2", type=InterfaceDescription, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
presents3: BinaryAssociation = BinaryAssociation(
    name="presents3",
    ends={
        Property(name="semantics", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="ServiceProfile", type=ServiceProfile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
supports4: BinaryAssociation = BinaryAssociation(
    name="supports4",
    ends={
        Property(name="semantics5", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="ServiceGrounding", type=ServiceGrounding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedBy6: BinaryAssociation = BinaryAssociation(
    name="describedBy6",
    ends={
        Property(name="semantics7", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessModel", type=ProcessModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
adaptedBy8: BinaryAssociation = BinaryAssociation(
    name="adaptedBy8",
    ends={
        Property(name="template", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="GroundTemplate", type=GroundTemplate, multiplicity=Multiplicity(0, 1))
    }
)
inLineSchema27: BinaryAssociation = BinaryAssociation(
    name="inLineSchema27",
    ends={
        Property(name="syntax_service_SchemaType", type=service_syntax_InterfaceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_InterfaceDescription28", type=syntax_service_SchemaType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outLineSchema29: BinaryAssociation = BinaryAssociation(
    name="outLineSchema29",
    ends={
        Property(name="syntax_service_SchemaType31", type=service_syntax_InterfaceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_InterfaceDescription30", type=syntax_service_SchemaType, multiplicity=Multiplicity(0, 9999))
    }
)
input32: BinaryAssociation = BinaryAssociation(
    name="input32",
    ends={
        Property(name="Message", type=service_syntax_OperationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_OperationDescription", type=Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fault33: BinaryAssociation = BinaryAssociation(
    name="fault33",
    ends={
        Property(name="Message35", type=service_syntax_OperationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_OperationDescription34", type=Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output36: BinaryAssociation = BinaryAssociation(
    name="output36",
    ends={
        Property(name="Message38", type=service_syntax_OperationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_OperationDescription37", type=Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type39: BinaryAssociation = BinaryAssociation(
    name="type39",
    ends={
        Property(name="syntax_service_TopLevelComplexType", type=service_syntax_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_Message", type=syntax_service_TopLevelComplexType, multiplicity=Multiplicity(0, 1))
    }
)
services15: BinaryAssociation = BinaryAssociation(
    name="services15",
    ends={
        Property(name="service_Service16", type=service_SL, multiplicity=Multiplicity(1, 1)),
        Property(name="service_SL", type=service_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providers17: BinaryAssociation = BinaryAssociation(
    name="providers17",
    ends={
        Property(name="service_ServiceProvider19", type=service_SL, multiplicity=Multiplicity(1, 1)),
        Property(name="service_SL18", type=service_ServiceProvider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
consumers20: BinaryAssociation = BinaryAssociation(
    name="consumers20",
    ends={
        Property(name="service_ServiceConsumer22", type=service_SL, multiplicity=Multiplicity(1, 1)),
        Property(name="service_SL21", type=service_ServiceConsumer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
framework23: BinaryAssociation = BinaryAssociation(
    name="framework23",
    ends={
        Property(name="ServiceFramework", type=service_SL, multiplicity=Multiplicity(1, 1)),
        Property(name="service_SL24", type=ServiceFramework, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation25: BinaryAssociation = BinaryAssociation(
    name="operation25",
    ends={
        Property(name="OperationDescription", type=service_syntax_InterfaceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_InterfaceDescription", type=OperationDescription, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
binding26: BinaryAssociation = BinaryAssociation(
    name="binding26",
    ends={
        Property(name="syntax", type=service_syntax_InterfaceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="Binding", type=Binding, multiplicity=Multiplicity(0, 9999))
    }
)
type48: BinaryAssociation = BinaryAssociation(
    name="type48",
    ends={
        Property(name="syntax50", type=service_syntax_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="InterfaceDescription49", type=InterfaceDescription, multiplicity=Multiplicity(1, 1))
    }
)
element40: BinaryAssociation = BinaryAssociation(
    name="element40",
    ends={
        Property(name="syntax_service_TopLevelElement", type=service_syntax_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_Message41", type=syntax_service_TopLevelElement, multiplicity=Multiplicity(0, 1))
    }
)
binding42: BinaryAssociation = BinaryAssociation(
    name="binding42",
    ends={
        Property(name="Binding43", type=service_syntax_Endpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_Endpoint", type=Binding, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
implementation44: BinaryAssociation = BinaryAssociation(
    name="implementation44",
    ends={
        Property(name="syntax_service_ServiceImplemetation", type=service_syntax_Endpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_Endpoint45", type=syntax_service_ServiceImplemetation, multiplicity=Multiplicity(0, 1))
    }
)
deployedService46: BinaryAssociation = BinaryAssociation(
    name="deployedService46",
    ends={
        Property(name="DeployedService", type=service_syntax_Endpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_Endpoint47", type=DeployedService, multiplicity=Multiplicity(0, 1))
    }
)
hasOutput58: BinaryAssociation = BinaryAssociation(
    name="hasOutput58",
    ends={
        Property(name="ServiceOutput", type=service_semantics_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceProfile59", type=ServiceOutput, multiplicity=Multiplicity(0, 9999))
    }
)
hasResult60: BinaryAssociation = BinaryAssociation(
    name="hasResult60",
    ends={
        Property(name="ServiceResult", type=service_semantics_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceProfile61", type=ServiceResult, multiplicity=Multiplicity(0, 9999))
    }
)
hasCondition62: BinaryAssociation = BinaryAssociation(
    name="hasCondition62",
    ends={
        Property(name="ServiceCondition", type=service_semantics_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceProfile63", type=ServiceCondition, multiplicity=Multiplicity(0, 9999))
    }
)
supportedBy64: BinaryAssociation = BinaryAssociation(
    name="supportedBy64",
    ends={
        Property(name="Service65", type=service_semantics_ServiceGrounding, multiplicity=Multiplicity(1, 1)),
        Property(name="supports", type=semantics_service_Service, multiplicity=Multiplicity(0, 1))
    }
)
processModel66: BinaryAssociation = BinaryAssociation(
    name="processModel66",
    ends={
        Property(name="ProcessModel67", type=service_semantics_ServiceGrounding, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceGrounding", type=ProcessModel, multiplicity=Multiplicity(0, 1))
    }
)
interface68: BinaryAssociation = BinaryAssociation(
    name="interface68",
    ends={
        Property(name="InterfaceDescription70", type=service_semantics_ServiceGrounding, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceGrounding69", type=InterfaceDescription, multiplicity=Multiplicity(0, 1))
    }
)
presentedBy51: BinaryAssociation = BinaryAssociation(
    name="presentedBy51",
    ends={
        Property(name="Service", type=service_semantics_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="presents", type=semantics_service_Service, multiplicity=Multiplicity(0, 1))
    }
)
hasProcess52: BinaryAssociation = BinaryAssociation(
    name="hasProcess52",
    ends={
        Property(name="ProcessModel53", type=service_semantics_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceProfile", type=ProcessModel, multiplicity=Multiplicity(0, 1))
    }
)
serviceCategory54: BinaryAssociation = BinaryAssociation(
    name="serviceCategory54",
    ends={
        Property(name="ServiceCategory", type=service_semantics_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceProfile55", type=ServiceCategory, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hasInput56: BinaryAssociation = BinaryAssociation(
    name="hasInput56",
    ends={
        Property(name="ServiceInput", type=service_semantics_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceProfile57", type=ServiceInput, multiplicity=Multiplicity(0, 9999))
    }
)
expression74: BinaryAssociation = BinaryAssociation(
    name="expression74",
    ends={
        Property(name="semantics_service_Antecedent", type=service_semantics_ServiceCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceCondition", type=semantics_service_Antecedent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression75: BinaryAssociation = BinaryAssociation(
    name="expression75",
    ends={
        Property(name="semantics_service_Antecedent76", type=service_semantics_ServiceResult, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceResult", type=semantics_service_Antecedent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result77: BinaryAssociation = BinaryAssociation(
    name="result77",
    ends={
        Property(name="semantics_service_Consequent", type=service_semantics_ServiceResult, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceResult78", type=semantics_service_Consequent, multiplicity=Multiplicity(0, 1))
    }
)
hasInput79: BinaryAssociation = BinaryAssociation(
    name="hasInput79",
    ends={
        Property(name="ServiceInput80", type=service_semantics_IOEP, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_IOEP", type=ServiceInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasCondition81: BinaryAssociation = BinaryAssociation(
    name="hasCondition81",
    ends={
        Property(name="ServiceCondition83", type=service_semantics_IOEP, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_IOEP82", type=ServiceCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasOutput84: BinaryAssociation = BinaryAssociation(
    name="hasOutput84",
    ends={
        Property(name="ServiceOutput86", type=service_semantics_IOEP, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_IOEP85", type=ServiceOutput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasResult87: BinaryAssociation = BinaryAssociation(
    name="hasResult87",
    ends={
        Property(name="ServiceResult89", type=service_semantics_IOEP, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_IOEP88", type=ServiceResult, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describes71: BinaryAssociation = BinaryAssociation(
    name="describes71",
    ends={
        Property(name="Service72", type=service_semantics_ProcessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="describedBy", type=semantics_service_Service, multiplicity=Multiplicity(0, 1))
    }
)
type73: BinaryAssociation = BinaryAssociation(
    name="type73",
    ends={
        Property(name="semantics_service_EObject", type=service_semantics_ServiceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceParameter", type=semantics_service_EObject, multiplicity=Multiplicity(0, 1))
    }
)
expose103: BinaryAssociation = BinaryAssociation(
    name="expose103",
    ends={
        Property(name="Service104", type=service_template_GroundTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="adaptedBy", type=template_service_Service, multiplicity=Multiplicity(1, 1))
    }
)
abstract105: BinaryAssociation = BinaryAssociation(
    name="abstract105",
    ends={
        Property(name="ServiceParameter106", type=service_template_BoundTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_BoundTemplateParameter", type=ServiceParameter, multiplicity=Multiplicity(1, 1))
    }
)
concrete107: BinaryAssociation = BinaryAssociation(
    name="concrete107",
    ends={
        Property(name="ServiceParameter109", type=service_template_BoundTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_BoundTemplateParameter108", type=ServiceParameter, multiplicity=Multiplicity(1, 1))
    }
)
abstract110: BinaryAssociation = BinaryAssociation(
    name="abstract110",
    ends={
        Property(name="AbstractProcessModel111", type=service_template_BoundProcessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_BoundProcessModel", type=AbstractProcessModel, multiplicity=Multiplicity(1, 1))
    }
)
concrete112: BinaryAssociation = BinaryAssociation(
    name="concrete112",
    ends={
        Property(name="ProcessModel114", type=service_template_BoundProcessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_BoundProcessModel113", type=ProcessModel, multiplicity=Multiplicity(1, 1))
    }
)
body115: BinaryAssociation = BinaryAssociation(
    name="body115",
    ends={
        Property(name="template_service_Antecedent", type=service_template_TemplateConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_TemplateConstraint", type=template_service_Antecedent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flow90: BinaryAssociation = BinaryAssociation(
    name="flow90",
    ends={
        Property(name="TemplateFlow", type=service_template_ServiceTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ServiceTemplate", type=TemplateFlow, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateParameter91: BinaryAssociation = BinaryAssociation(
    name="templateParameter91",
    ends={
        Property(name="ServiceParameter", type=service_template_ServiceTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ServiceTemplate92", type=ServiceParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expose93: BinaryAssociation = BinaryAssociation(
    name="expose93",
    ends={
        Property(name="AbstractProcessModel", type=service_template_ServiceTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ServiceTemplate94", type=AbstractProcessModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraints95: BinaryAssociation = BinaryAssociation(
    name="constraints95",
    ends={
        Property(name="TemplateConstraint", type=service_template_ServiceTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ServiceTemplate96", type=TemplateConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
composedOf97: BinaryAssociation = BinaryAssociation(
    name="composedOf97",
    ends={
        Property(name="ControlConstruct", type=service_template_TemplateFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_TemplateFlow", type=ControlConstruct, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implement98: BinaryAssociation = BinaryAssociation(
    name="implement98",
    ends={
        Property(name="ServiceTemplate", type=service_template_GroundTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_GroundTemplate", type=ServiceTemplate, multiplicity=Multiplicity(0, 1))
    }
)
bindTemplateParameter99: BinaryAssociation = BinaryAssociation(
    name="bindTemplateParameter99",
    ends={
        Property(name="BoundTemplateParameter", type=service_template_GroundTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_GroundTemplate100", type=BoundTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindProcessModel101: BinaryAssociation = BinaryAssociation(
    name="bindProcessModel101",
    ends={
        Property(name="BoundProcessModel", type=service_template_GroundTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_GroundTemplate102", type=BoundProcessModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partnerProcess128: BinaryAssociation = BinaryAssociation(
    name="partnerProcess128",
    ends={
        Property(name="AbstractProcessModel129", type=service_template_Perform, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_Perform", type=AbstractProcessModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
hasDataFromProcess130: BinaryAssociation = BinaryAssociation(
    name="hasDataFromProcess130",
    ends={
        Property(name="AbstractProcessModel132", type=service_template_Perform, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_Perform131", type=AbstractProcessModel, multiplicity=Multiplicity(0, 1))
    }
)
valueData133: BinaryAssociation = BinaryAssociation(
    name="valueData133",
    ends={
        Property(name="ServiceParameter135", type=service_template_Perform, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_Perform134", type=ServiceParameter, multiplicity=Multiplicity(0, 1))
    }
)
hasDataFromTemplate136: BinaryAssociation = BinaryAssociation(
    name="hasDataFromTemplate136",
    ends={
        Property(name="ServiceTemplate138", type=service_template_Perform, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_Perform137", type=ServiceTemplate, multiplicity=Multiplicity(0, 1))
    }
)
untilCondition139: BinaryAssociation = BinaryAssociation(
    name="untilCondition139",
    ends={
        Property(name="template_service_Antecedent140", type=service_template_RepeatUntil, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_RepeatUntil", type=template_service_Antecedent, multiplicity=Multiplicity(1, 1))
    }
)
untilProcess141: BinaryAssociation = BinaryAssociation(
    name="untilProcess141",
    ends={
        Property(name="ControlConstruct143", type=service_template_RepeatUntil, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_RepeatUntil142", type=ControlConstruct, multiplicity=Multiplicity(1, 1))
    }
)
whileCondition144: BinaryAssociation = BinaryAssociation(
    name="whileCondition144",
    ends={
        Property(name="template_service_Antecedent145", type=service_template_RepeatWhile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_RepeatWhile", type=template_service_Antecedent, multiplicity=Multiplicity(1, 1))
    }
)
timeout116: BinaryAssociation = BinaryAssociation(
    name="timeout116",
    ends={
        Property(name="IntervalThing", type=service_template_ControlConstruct, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ControlConstruct", type=IntervalThing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
components117: BinaryAssociation = BinaryAssociation(
    name="components117",
    ends={
        Property(name="ControlConstructBag", type=service_template_AnyOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_AnyOrder", type=ControlConstructBag, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
components118: BinaryAssociation = BinaryAssociation(
    name="components118",
    ends={
        Property(name="ControlConstructBag119", type=service_template_Choice, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_Choice", type=ControlConstructBag, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifCondition120: BinaryAssociation = BinaryAssociation(
    name="ifCondition120",
    ends={
        Property(name="template_service_Antecedent121", type=service_template_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_IfThenElse", type=template_service_Antecedent, multiplicity=Multiplicity(1, 1))
    }
)
then122: BinaryAssociation = BinaryAssociation(
    name="then122",
    ends={
        Property(name="ControlConstruct124", type=service_template_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_IfThenElse123", type=ControlConstruct, multiplicity=Multiplicity(1, 1))
    }
)
else125: BinaryAssociation = BinaryAssociation(
    name="else125",
    ends={
        Property(name="ControlConstruct127", type=service_template_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_IfThenElse126", type=ControlConstruct, multiplicity=Multiplicity(0, 1))
    }
)
rest156: BinaryAssociation = BinaryAssociation(
    name="rest156",
    ends={
        Property(name="ControlConstructList158", type=service_template_ControlConstructList, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ControlConstructList157", type=ControlConstructList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first159: BinaryAssociation = BinaryAssociation(
    name="first159",
    ends={
        Property(name="ControlConstruct160", type=service_template_ControlConstructBag, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ControlConstructBag", type=ControlConstruct, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest161: BinaryAssociation = BinaryAssociation(
    name="rest161",
    ends={
        Property(name="ControlConstructBag163", type=service_template_ControlConstructBag, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ControlConstructBag162", type=ControlConstructBag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
matchmaker164: BinaryAssociation = BinaryAssociation(
    name="matchmaker164",
    ends={
        Property(name="ServiceTemplateMatchmaker", type=service_architecture_ServiceFramework, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceFramework", type=ServiceTemplateMatchmaker, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
execution165: BinaryAssociation = BinaryAssociation(
    name="execution165",
    ends={
        Property(name="ExecutionFramework", type=service_architecture_ServiceFramework, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceFramework166", type=ExecutionFramework, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceDirectory167: BinaryAssociation = BinaryAssociation(
    name="serviceDirectory167",
    ends={
        Property(name="ServiceDirectory", type=service_architecture_ServiceFramework, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceFramework168", type=ServiceDirectory, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
templateRepository169: BinaryAssociation = BinaryAssociation(
    name="templateRepository169",
    ends={
        Property(name="TemplateRepository", type=service_architecture_ServiceFramework, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceFramework170", type=TemplateRepository, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whileProcess146: BinaryAssociation = BinaryAssociation(
    name="whileProcess146",
    ends={
        Property(name="ControlConstruct148", type=service_template_RepeatWhile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_RepeatWhile147", type=ControlConstruct, multiplicity=Multiplicity(1, 1))
    }
)
components149: BinaryAssociation = BinaryAssociation(
    name="components149",
    ends={
        Property(name="ControlConstructList", type=service_template_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_Sequence", type=ControlConstructList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
components150: BinaryAssociation = BinaryAssociation(
    name="components150",
    ends={
        Property(name="ControlConstructBag151", type=service_template_Split, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_Split", type=ControlConstructBag, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
components152: BinaryAssociation = BinaryAssociation(
    name="components152",
    ends={
        Property(name="ControlConstructBag153", type=service_template_SplitJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_SplitJoin", type=ControlConstructBag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first154: BinaryAssociation = BinaryAssociation(
    name="first154",
    ends={
        Property(name="ControlConstruct155", type=service_template_ControlConstructList, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ControlConstructList", type=ControlConstruct, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interface185: BinaryAssociation = BinaryAssociation(
    name="interface185",
    ends={
        Property(name="InterfaceDescription187", type=service_architecture_ServiceDirectory, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceDirectory186", type=InterfaceDescription, multiplicity=Multiplicity(0, 9999))
    }
)
deployedService188: BinaryAssociation = BinaryAssociation(
    name="deployedService188",
    ends={
        Property(name="architecture", type=service_architecture_ExecutionFramework, multiplicity=Multiplicity(1, 1)),
        Property(name="DeployedService189", type=DeployedService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deploy190: BinaryAssociation = BinaryAssociation(
    name="deploy190",
    ends={
        Property(name="architecture192", type=service_architecture_DeployedService, multiplicity=Multiplicity(1, 1)),
        Property(name="ExecutionFramework191", type=ExecutionFramework, multiplicity=Multiplicity(1, 1))
    }
)
template171: BinaryAssociation = BinaryAssociation(
    name="template171",
    ends={
        Property(name="ServiceTemplate172", type=service_architecture_TemplateRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_TemplateRepository", type=ServiceTemplate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groundTemplate173: BinaryAssociation = BinaryAssociation(
    name="groundTemplate173",
    ends={
        Property(name="GroundTemplate175", type=service_architecture_TemplateRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_TemplateRepository174", type=GroundTemplate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templateRepository176: BinaryAssociation = BinaryAssociation(
    name="templateRepository176",
    ends={
        Property(name="TemplateRepository177", type=service_architecture_TemplateMatchmaker, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_TemplateMatchmaker", type=TemplateRepository, multiplicity=Multiplicity(1, 1))
    }
)
serviceDirectory178: BinaryAssociation = BinaryAssociation(
    name="serviceDirectory178",
    ends={
        Property(name="ServiceDirectory179", type=service_architecture_ServiceMatchmaker, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceMatchmaker", type=ServiceDirectory, multiplicity=Multiplicity(1, 9999))
    }
)
endpoint180: BinaryAssociation = BinaryAssociation(
    name="endpoint180",
    ends={
        Property(name="Endpoint181", type=service_architecture_ServiceDirectory, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceDirectory", type=Endpoint, multiplicity=Multiplicity(0, 9999))
    }
)
semantic182: BinaryAssociation = BinaryAssociation(
    name="semantic182",
    ends={
        Property(name="ServiceProfile184", type=service_architecture_ServiceDirectory, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceDirectory183", type=ServiceProfile, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_service_ServiceProvider_Agent = Generalization(general=Agent, specific=service_ServiceProvider)
gen_service_ServiceConsumer_Agent = Generalization(general=Agent, specific=service_ServiceConsumer)
gen_service_semantics_ProcessModel_IOEP = Generalization(general=IOEP, specific=service_semantics_ProcessModel)
gen_service_semantics_ServiceInput_ServiceParameter = Generalization(general=ServiceParameter, specific=service_semantics_ServiceInput)
gen_service_semantics_ServiceOutput_ServiceParameter = Generalization(general=ServiceParameter, specific=service_semantics_ServiceOutput)
gen_service_template_AbstractProcessModel_IOEP = Generalization(general=IOEP, specific=service_template_AbstractProcessModel)
gen_service_template_Iterate_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_Iterate)
gen_service_template_Perform_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_Perform)
gen_service_template_RepeatUntil_Iterate = Generalization(general=Iterate, specific=service_template_RepeatUntil)
gen_service_template_RepeatWhile_Iterate = Generalization(general=Iterate, specific=service_template_RepeatWhile)
gen_service_template_AnyOrder_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_AnyOrder)
gen_service_template_Choice_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_Choice)
gen_service_template_IfThenElse_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_IfThenElse)
gen_service_template_Sequence_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_Sequence)
gen_service_template_Split_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_Split)
gen_service_template_SplitJoin_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_SplitJoin)
gen_service_architecture_ServiceTemplateMatchmaker_architecture_ServiceMatchmaker = Generalization(general=architecture_ServiceMatchmaker, specific=service_architecture_ServiceTemplateMatchmaker)
gen_service_architecture_ServiceTemplateMatchmaker_architecture_TemplateMatchmaker = Generalization(general=architecture_TemplateMatchmaker, specific=service_architecture_ServiceTemplateMatchmaker)

# Domain Model
domain_model = DomainModel(
    name="service",
    types={service_ServiceProvider, Agent, service_ServiceImplemetation, service_ServiceConsumer, service_Service, Endpoint, InterfaceDescription, ServiceProfile, ServiceGrounding, ProcessModel, GroundTemplate, syntax_service_SchemaType, service_syntax_OperationDescription, Message, service_syntax_Message, syntax_service_TopLevelComplexType, service_SL, ServiceFramework, service_syntax_InterfaceDescription, OperationDescription, Binding, syntax_service_TopLevelElement, service_syntax_Endpoint, syntax_service_ServiceImplemetation, DeployedService, service_syntax_Binding, ServiceResult, ServiceCondition, service_semantics_ServiceGrounding, service_semantics_ServiceProfile, semantics_service_Service, ServiceCategory, ServiceInput, ServiceOutput, service_semantics_ServiceResult, semantics_service_Consequent, service_semantics_IOEP, service_semantics_ProcessModel, IOEP, service_semantics_ServiceCategory, service_semantics_ServiceParameter, semantics_service_EObject, service_semantics_ServiceInput, ServiceParameter, service_semantics_ServiceOutput, service_semantics_ServiceCondition, semantics_service_Antecedent, template_service_Service, service_template_AbstractProcessModel, service_template_BoundTemplateParameter, service_template_BoundProcessModel, service_template_TemplateConstraint, service_template_ServiceTemplate, template_service_Antecedent, TemplateFlow, service_template_ControlConstruct, AbstractProcessModel, TemplateConstraint, service_template_TemplateFlow, ControlConstruct, service_template_GroundTemplate, ServiceTemplate, BoundTemplateParameter, BoundProcessModel, service_template_Iterate, service_template_Perform, service_template_RepeatUntil, Iterate, service_template_RepeatWhile, IntervalThing, service_template_AnyOrder, ControlConstructBag, service_template_Choice, service_template_IfThenElse, service_template_ControlConstructBag, service_template_IntervalThing, service_architecture_ServiceFramework, ServiceTemplateMatchmaker, ExecutionFramework, ServiceDirectory, TemplateRepository, service_template_Sequence, ControlConstructList, service_template_Split, service_template_SplitJoin, service_template_ControlConstructList, service_architecture_ExecutionFramework, service_architecture_DeployedService, service_architecture_TemplateRepository, service_architecture_TemplateMatchmaker, service_architecture_ServiceMatchmaker, service_architecture_ServiceTemplateMatchmaker, architecture_ServiceMatchmaker, architecture_TemplateMatchmaker, service_architecture_ServiceDirectory, ServiceType, ServiceImpLanguage, StyleEncoding, TransportProtocol, ContainerType},
    associations={exposes9, implementation11, invokes13, endpoint0, interface1, presents3, supports4, describedBy6, adaptedBy8, inLineSchema27, outLineSchema29, input32, fault33, output36, type39, services15, providers17, consumers20, framework23, operation25, binding26, type48, element40, binding42, implementation44, deployedService46, hasOutput58, hasResult60, hasCondition62, supportedBy64, processModel66, interface68, presentedBy51, hasProcess52, serviceCategory54, hasInput56, expression74, expression75, result77, hasInput79, hasCondition81, hasOutput84, hasResult87, describes71, type73, expose103, abstract105, concrete107, abstract110, concrete112, body115, flow90, templateParameter91, expose93, constraints95, composedOf97, implement98, bindTemplateParameter99, bindProcessModel101, partnerProcess128, hasDataFromProcess130, valueData133, hasDataFromTemplate136, untilCondition139, untilProcess141, whileCondition144, timeout116, components117, components118, ifCondition120, then122, else125, rest156, first159, rest161, matchmaker164, execution165, serviceDirectory167, templateRepository169, whileProcess146, components149, components150, components152, first154, interface185, deployedService188, deploy190, template171, groundTemplate173, templateRepository176, serviceDirectory178, endpoint180, semantic182},
    generalizations={gen_service_ServiceProvider_Agent, gen_service_ServiceConsumer_Agent, gen_service_semantics_ProcessModel_IOEP, gen_service_semantics_ServiceInput_ServiceParameter, gen_service_semantics_ServiceOutput_ServiceParameter, gen_service_template_AbstractProcessModel_IOEP, gen_service_template_Iterate_ControlConstruct, gen_service_template_Perform_ControlConstruct, gen_service_template_RepeatUntil_Iterate, gen_service_template_RepeatWhile_Iterate, gen_service_template_AnyOrder_ControlConstruct, gen_service_template_Choice_ControlConstruct, gen_service_template_IfThenElse_ControlConstruct, gen_service_template_Sequence_ControlConstruct, gen_service_template_Split_ControlConstruct, gen_service_template_SplitJoin_ControlConstruct, gen_service_architecture_ServiceTemplateMatchmaker_architecture_ServiceMatchmaker, gen_service_architecture_ServiceTemplateMatchmaker_architecture_TemplateMatchmaker},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)