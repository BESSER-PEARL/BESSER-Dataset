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
service_Service = Class(name="service_Service")
Endpoint = Class(name="Endpoint")
service_ServiceImplemetation = Class(name="service_ServiceImplemetation")
service_ServiceConsumer = Class(name="service_ServiceConsumer")
service_SL = Class(name="service_SL")
InterfaceDescription = Class(name="InterfaceDescription")
ServiceProfile = Class(name="ServiceProfile")
ServiceGrounding = Class(name="ServiceGrounding")
ProcessModel = Class(name="ProcessModel")
GroundTemplate = Class(name="GroundTemplate")
service_ServiceProvider = Class(name="service_ServiceProvider", is_abstract=True)
Agent = Class(name="Agent")
syntax_service_SchemaType = Class(name="syntax_service_SchemaType")
service_syntax_OperationDescription = Class(name="service_syntax_OperationDescription")
Message = Class(name="Message")
service_syntax_Message = Class(name="service_syntax_Message")
syntax_service_TopLevelComplexType = Class(name="syntax_service_TopLevelComplexType")
syntax_service_TopLevelElement = Class(name="syntax_service_TopLevelElement")
ServiceFramework = Class(name="ServiceFramework")
service_syntax_InterfaceDescription = Class(name="service_syntax_InterfaceDescription")
OperationDescription = Class(name="OperationDescription")
Binding = Class(name="Binding")
service_semantics_ServiceProfile = Class(name="service_semantics_ServiceProfile")
semantics_service_Service = Class(name="semantics_service_Service")
ServiceCategory = Class(name="ServiceCategory")
ServiceInput = Class(name="ServiceInput")
ServiceOutput = Class(name="ServiceOutput")
ServiceResult = Class(name="ServiceResult")
ServiceCondition = Class(name="ServiceCondition")
service_syntax_Endpoint = Class(name="service_syntax_Endpoint")
syntax_service_ServiceImplemetation = Class(name="syntax_service_ServiceImplemetation")
DeployedService = Class(name="DeployedService")
service_syntax_Binding = Class(name="service_syntax_Binding")
service_semantics_ServiceInput = Class(name="service_semantics_ServiceInput")
ServiceParameter = Class(name="ServiceParameter")
service_semantics_ServiceOutput = Class(name="service_semantics_ServiceOutput")
service_semantics_ServiceCondition = Class(name="service_semantics_ServiceCondition")
semantics_service_Antecedent = Class(name="semantics_service_Antecedent")
service_semantics_ServiceResult = Class(name="service_semantics_ServiceResult")
semantics_service_Consequent = Class(name="semantics_service_Consequent")
service_semantics_IOEP = Class(name="service_semantics_IOEP", is_abstract=True)
service_semantics_ServiceGrounding = Class(name="service_semantics_ServiceGrounding")
service_template_ServiceTemplate = Class(name="service_template_ServiceTemplate")
TemplateFlow = Class(name="TemplateFlow")
service_semantics_ProcessModel = Class(name="service_semantics_ProcessModel")
IOEP = Class(name="IOEP")
AbstractProcessModel = Class(name="AbstractProcessModel")
TemplateConstraint = Class(name="TemplateConstraint")
service_semantics_ServiceCategory = Class(name="service_semantics_ServiceCategory")
service_template_TemplateFlow = Class(name="service_template_TemplateFlow")
ControlConstruct = Class(name="ControlConstruct")
service_semantics_ServiceParameter = Class(name="service_semantics_ServiceParameter", is_abstract=True)
semantics_service_EObject = Class(name="semantics_service_EObject")
BoundTemplateParameter = Class(name="BoundTemplateParameter")
BoundProcessModel = Class(name="BoundProcessModel")
template_service_Service = Class(name="template_service_Service")
service_template_AbstractProcessModel = Class(name="service_template_AbstractProcessModel")
service_template_BoundTemplateParameter = Class(name="service_template_BoundTemplateParameter")
service_template_BoundProcessModel = Class(name="service_template_BoundProcessModel")
service_template_TemplateConstraint = Class(name="service_template_TemplateConstraint")
template_service_Antecedent = Class(name="template_service_Antecedent")
service_template_ControlConstruct = Class(name="service_template_ControlConstruct", is_abstract=True)
IntervalThing = Class(name="IntervalThing")
service_template_AnyOrder = Class(name="service_template_AnyOrder")
ControlConstructBag = Class(name="ControlConstructBag")
service_template_Choice = Class(name="service_template_Choice")
service_template_GroundTemplate = Class(name="service_template_GroundTemplate")
ServiceTemplate = Class(name="ServiceTemplate")
service_template_Iterate = Class(name="service_template_Iterate", is_abstract=True)
service_template_Perform = Class(name="service_template_Perform")
service_template_RepeatUntil = Class(name="service_template_RepeatUntil")
Iterate = Class(name="Iterate")
service_template_RepeatWhile = Class(name="service_template_RepeatWhile")
service_template_Sequence = Class(name="service_template_Sequence")
ControlConstructList = Class(name="ControlConstructList")
service_template_Split = Class(name="service_template_Split")
service_template_IfThenElse = Class(name="service_template_IfThenElse")
service_template_SplitJoin = Class(name="service_template_SplitJoin")
service_template_ControlConstructList = Class(name="service_template_ControlConstructList")
service_template_ControlConstructBag = Class(name="service_template_ControlConstructBag")
service_template_IntervalThing = Class(name="service_template_IntervalThing")
service_architecture_ServiceFramework = Class(name="service_architecture_ServiceFramework")
ServiceTemplateMatchmaker = Class(name="ServiceTemplateMatchmaker")
ExecutionFramework = Class(name="ExecutionFramework")
ServiceDirectory = Class(name="ServiceDirectory")
TemplateRepository = Class(name="TemplateRepository")
service_architecture_TemplateRepository = Class(name="service_architecture_TemplateRepository")
service_architecture_TemplateMatchmaker = Class(name="service_architecture_TemplateMatchmaker")
service_architecture_ServiceMatchmaker = Class(name="service_architecture_ServiceMatchmaker")
service_architecture_ServiceTemplateMatchmaker = Class(name="service_architecture_ServiceTemplateMatchmaker")
architecture_ServiceMatchmaker = Class(name="architecture_ServiceMatchmaker")
architecture_TemplateMatchmaker = Class(name="architecture_TemplateMatchmaker")
service_architecture_ServiceDirectory = Class(name="service_architecture_ServiceDirectory")
service_architecture_ExecutionFramework = Class(name="service_architecture_ExecutionFramework")
service_architecture_DeployedService = Class(name="service_architecture_DeployedService")

# service_Service class attributes and methods
service_Service_name: Property = Property(name="name", type=StringType)
service_Service_namespace: Property = Property(name="namespace", type=StringType)
service_Service_description: Property = Property(name="description", type=StringType)
service_Service.attributes={service_Service_name, service_Service_namespace, service_Service_description}

# Endpoint class attributes and methods

# service_ServiceImplemetation class attributes and methods
service_ServiceImplemetation_language: Property = Property(name="language", type=StringType)
service_ServiceImplemetation_uri: Property = Property(name="uri", type=StringType)
service_ServiceImplemetation.attributes={service_ServiceImplemetation_language, service_ServiceImplemetation_uri}

# service_ServiceConsumer class attributes and methods
service_ServiceConsumer_isType: Property = Property(name="isType", type=StringType)
service_ServiceConsumer.attributes={service_ServiceConsumer_isType}

# service_SL class attributes and methods

# InterfaceDescription class attributes and methods

# ServiceProfile class attributes and methods

# ServiceGrounding class attributes and methods

# ProcessModel class attributes and methods

# GroundTemplate class attributes and methods

# service_ServiceProvider class attributes and methods
service_ServiceProvider_isType: Property = Property(name="isType", type=StringType)
service_ServiceProvider.attributes={service_ServiceProvider_isType}

# Agent class attributes and methods

# syntax_service_SchemaType class attributes and methods

# service_syntax_OperationDescription class attributes and methods
service_syntax_OperationDescription_name: Property = Property(name="name", type=StringType)
service_syntax_OperationDescription.attributes={service_syntax_OperationDescription_name}

# Message class attributes and methods

# service_syntax_Message class attributes and methods
service_syntax_Message_name: Property = Property(name="name", type=StringType)
service_syntax_Message.attributes={service_syntax_Message_name}

# syntax_service_TopLevelComplexType class attributes and methods

# syntax_service_TopLevelElement class attributes and methods

# ServiceFramework class attributes and methods

# service_syntax_InterfaceDescription class attributes and methods
service_syntax_InterfaceDescription_name: Property = Property(name="name", type=StringType)
service_syntax_InterfaceDescription.attributes={service_syntax_InterfaceDescription_name}

# OperationDescription class attributes and methods

# Binding class attributes and methods

# service_semantics_ServiceProfile class attributes and methods
service_semantics_ServiceProfile_name: Property = Property(name="name", type=StringType)
service_semantics_ServiceProfile_serviceClassification: Property = Property(name="serviceClassification", type=StringType)
service_semantics_ServiceProfile.attributes={service_semantics_ServiceProfile_serviceClassification, service_semantics_ServiceProfile_name}

# semantics_service_Service class attributes and methods

# ServiceCategory class attributes and methods

# ServiceInput class attributes and methods

# ServiceOutput class attributes and methods

# ServiceResult class attributes and methods

# ServiceCondition class attributes and methods

# service_syntax_Endpoint class attributes and methods
service_syntax_Endpoint_name: Property = Property(name="name", type=StringType)
service_syntax_Endpoint_location: Property = Property(name="location", type=StringType)
service_syntax_Endpoint.attributes={service_syntax_Endpoint_location, service_syntax_Endpoint_name}

# syntax_service_ServiceImplemetation class attributes and methods

# DeployedService class attributes and methods

# service_syntax_Binding class attributes and methods
service_syntax_Binding_name: Property = Property(name="name", type=StringType)
service_syntax_Binding_transport: Property = Property(name="transport", type=StringType)
service_syntax_Binding_style: Property = Property(name="style", type=StringType)
service_syntax_Binding.attributes={service_syntax_Binding_style, service_syntax_Binding_transport, service_syntax_Binding_name}

# service_semantics_ServiceInput class attributes and methods

# ServiceParameter class attributes and methods

# service_semantics_ServiceOutput class attributes and methods

# service_semantics_ServiceCondition class attributes and methods

# semantics_service_Antecedent class attributes and methods

# service_semantics_ServiceResult class attributes and methods

# semantics_service_Consequent class attributes and methods

# service_semantics_IOEP class attributes and methods

# service_semantics_ServiceGrounding class attributes and methods
service_semantics_ServiceGrounding_name: Property = Property(name="name", type=StringType)
service_semantics_ServiceGrounding_bindParams: Property = Property(name="bindParams", type=StringType)
service_semantics_ServiceGrounding.attributes={service_semantics_ServiceGrounding_name, service_semantics_ServiceGrounding_bindParams}

# service_template_ServiceTemplate class attributes and methods
service_template_ServiceTemplate_URI: Property = Property(name="URI", type=StringType)
service_template_ServiceTemplate.attributes={service_template_ServiceTemplate_URI}

# TemplateFlow class attributes and methods

# service_semantics_ProcessModel class attributes and methods
service_semantics_ProcessModel_name: Property = Property(name="name", type=StringType)
service_semantics_ProcessModel.attributes={service_semantics_ProcessModel_name}

# IOEP class attributes and methods

# AbstractProcessModel class attributes and methods

# TemplateConstraint class attributes and methods

# service_semantics_ServiceCategory class attributes and methods
service_semantics_ServiceCategory_taxonomy: Property = Property(name="taxonomy", type=StringType)
service_semantics_ServiceCategory_value: Property = Property(name="value", type=StringType)
service_semantics_ServiceCategory_name: Property = Property(name="name", type=StringType)
service_semantics_ServiceCategory_code: Property = Property(name="code", type=StringType)
service_semantics_ServiceCategory.attributes={service_semantics_ServiceCategory_name, service_semantics_ServiceCategory_value, service_semantics_ServiceCategory_code, service_semantics_ServiceCategory_taxonomy}

# service_template_TemplateFlow class attributes and methods

# ControlConstruct class attributes and methods

# service_semantics_ServiceParameter class attributes and methods
service_semantics_ServiceParameter_name: Property = Property(name="name", type=StringType)
service_semantics_ServiceParameter.attributes={service_semantics_ServiceParameter_name}

# semantics_service_EObject class attributes and methods

# BoundTemplateParameter class attributes and methods

# BoundProcessModel class attributes and methods

# template_service_Service class attributes and methods

# service_template_AbstractProcessModel class attributes and methods
service_template_AbstractProcessModel_name: Property = Property(name="name", type=StringType)
service_template_AbstractProcessModel.attributes={service_template_AbstractProcessModel_name}

# service_template_BoundTemplateParameter class attributes and methods

# service_template_BoundProcessModel class attributes and methods

# service_template_TemplateConstraint class attributes and methods

# template_service_Antecedent class attributes and methods

# service_template_ControlConstruct class attributes and methods

# IntervalThing class attributes and methods

# service_template_AnyOrder class attributes and methods

# ControlConstructBag class attributes and methods

# service_template_Choice class attributes and methods

# service_template_GroundTemplate class attributes and methods
service_template_GroundTemplate_name: Property = Property(name="name", type=StringType)
service_template_GroundTemplate.attributes={service_template_GroundTemplate_name}

# ServiceTemplate class attributes and methods

# service_template_Iterate class attributes and methods

# service_template_Perform class attributes and methods

# service_template_RepeatUntil class attributes and methods

# Iterate class attributes and methods

# service_template_RepeatWhile class attributes and methods

# service_template_Sequence class attributes and methods

# ControlConstructList class attributes and methods

# service_template_Split class attributes and methods

# service_template_IfThenElse class attributes and methods

# service_template_SplitJoin class attributes and methods

# service_template_ControlConstructList class attributes and methods

# service_template_ControlConstructBag class attributes and methods

# service_template_IntervalThing class attributes and methods

# service_architecture_ServiceFramework class attributes and methods

# ServiceTemplateMatchmaker class attributes and methods

# ExecutionFramework class attributes and methods

# ServiceDirectory class attributes and methods

# TemplateRepository class attributes and methods

# service_architecture_TemplateRepository class attributes and methods

# service_architecture_TemplateMatchmaker class attributes and methods

# service_architecture_ServiceMatchmaker class attributes and methods

# service_architecture_ServiceTemplateMatchmaker class attributes and methods

# architecture_ServiceMatchmaker class attributes and methods

# architecture_TemplateMatchmaker class attributes and methods

# service_architecture_ServiceDirectory class attributes and methods

# service_architecture_ExecutionFramework class attributes and methods
service_architecture_ExecutionFramework_container: Property = Property(name="container", type=StringType)
service_architecture_ExecutionFramework.attributes={service_architecture_ExecutionFramework_container}

# service_architecture_DeployedService class attributes and methods
service_architecture_DeployedService_artifact: Property = Property(name="artifact", type=StringType)
service_architecture_DeployedService.attributes={service_architecture_DeployedService_artifact}

# Relationships
endpoint0: BinaryAssociation = BinaryAssociation(
    name="endpoint0",
    ends={
        Property(name="Endpoint", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Service", type=Endpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exposes7: BinaryAssociation = BinaryAssociation(
    name="exposes7",
    ends={
        Property(name="service_Service8", type=service_ServiceProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="service_ServiceProvider", type=service_Service, multiplicity=Multiplicity(1, 9999))
    }
)
implementation9: BinaryAssociation = BinaryAssociation(
    name="implementation9",
    ends={
        Property(name="service_ServiceImplemetation", type=service_ServiceProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="service_ServiceProvider10", type=service_ServiceImplemetation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invokes11: BinaryAssociation = BinaryAssociation(
    name="invokes11",
    ends={
        Property(name="service_Service12", type=service_ServiceConsumer, multiplicity=Multiplicity(1, 1)),
        Property(name="service_ServiceConsumer", type=service_Service, multiplicity=Multiplicity(1, 9999))
    }
)
services13: BinaryAssociation = BinaryAssociation(
    name="services13",
    ends={
        Property(name="service_Service14", type=service_SL, multiplicity=Multiplicity(1, 1)),
        Property(name="service_SL", type=service_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="ServiceProfile", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="presentedBy", type=ServiceProfile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
supports4: BinaryAssociation = BinaryAssociation(
    name="supports4",
    ends={
        Property(name="ServiceGrounding", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="supportedBy", type=ServiceGrounding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedBy5: BinaryAssociation = BinaryAssociation(
    name="describedBy5",
    ends={
        Property(name="ProcessModel", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="describes", type=ProcessModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
adaptedBy6: BinaryAssociation = BinaryAssociation(
    name="adaptedBy6",
    ends={
        Property(name="GroundTemplate", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="expose", type=GroundTemplate, multiplicity=Multiplicity(0, 1))
    }
)
inLineSchema25: BinaryAssociation = BinaryAssociation(
    name="inLineSchema25",
    ends={
        Property(name="syntax_service_SchemaType", type=service_syntax_InterfaceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_InterfaceDescription26", type=syntax_service_SchemaType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outLineSchema27: BinaryAssociation = BinaryAssociation(
    name="outLineSchema27",
    ends={
        Property(name="syntax_service_SchemaType29", type=service_syntax_InterfaceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_InterfaceDescription28", type=syntax_service_SchemaType, multiplicity=Multiplicity(0, 9999))
    }
)
input30: BinaryAssociation = BinaryAssociation(
    name="input30",
    ends={
        Property(name="Message", type=service_syntax_OperationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_OperationDescription", type=Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fault31: BinaryAssociation = BinaryAssociation(
    name="fault31",
    ends={
        Property(name="Message33", type=service_syntax_OperationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_OperationDescription32", type=Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output34: BinaryAssociation = BinaryAssociation(
    name="output34",
    ends={
        Property(name="Message36", type=service_syntax_OperationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_OperationDescription35", type=Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type37: BinaryAssociation = BinaryAssociation(
    name="type37",
    ends={
        Property(name="syntax_service_TopLevelComplexType", type=service_syntax_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_Message", type=syntax_service_TopLevelComplexType, multiplicity=Multiplicity(0, 1))
    }
)
element38: BinaryAssociation = BinaryAssociation(
    name="element38",
    ends={
        Property(name="syntax_service_TopLevelElement", type=service_syntax_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_Message39", type=syntax_service_TopLevelElement, multiplicity=Multiplicity(0, 1))
    }
)
providers15: BinaryAssociation = BinaryAssociation(
    name="providers15",
    ends={
        Property(name="service_ServiceProvider17", type=service_SL, multiplicity=Multiplicity(1, 1)),
        Property(name="service_SL16", type=service_ServiceProvider, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
consumers18: BinaryAssociation = BinaryAssociation(
    name="consumers18",
    ends={
        Property(name="service_ServiceConsumer20", type=service_SL, multiplicity=Multiplicity(1, 1)),
        Property(name="service_SL19", type=service_ServiceConsumer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
framework21: BinaryAssociation = BinaryAssociation(
    name="framework21",
    ends={
        Property(name="ServiceFramework", type=service_SL, multiplicity=Multiplicity(1, 1)),
        Property(name="service_SL22", type=ServiceFramework, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation23: BinaryAssociation = BinaryAssociation(
    name="operation23",
    ends={
        Property(name="OperationDescription", type=service_syntax_InterfaceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_InterfaceDescription", type=OperationDescription, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
binding24: BinaryAssociation = BinaryAssociation(
    name="binding24",
    ends={
        Property(name="Binding", type=service_syntax_InterfaceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=Binding, multiplicity=Multiplicity(0, 9999))
    }
)
presentedBy48: BinaryAssociation = BinaryAssociation(
    name="presentedBy48",
    ends={
        Property(name="Service", type=service_semantics_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="presents", type=semantics_service_Service, multiplicity=Multiplicity(0, 1))
    }
)
hasProcess49: BinaryAssociation = BinaryAssociation(
    name="hasProcess49",
    ends={
        Property(name="ProcessModel50", type=service_semantics_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceProfile", type=ProcessModel, multiplicity=Multiplicity(0, 1))
    }
)
serviceCategory51: BinaryAssociation = BinaryAssociation(
    name="serviceCategory51",
    ends={
        Property(name="ServiceCategory", type=service_semantics_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceProfile52", type=ServiceCategory, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hasInput53: BinaryAssociation = BinaryAssociation(
    name="hasInput53",
    ends={
        Property(name="ServiceInput", type=service_semantics_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceProfile54", type=ServiceInput, multiplicity=Multiplicity(0, 9999))
    }
)
hasOutput55: BinaryAssociation = BinaryAssociation(
    name="hasOutput55",
    ends={
        Property(name="ServiceOutput", type=service_semantics_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceProfile56", type=ServiceOutput, multiplicity=Multiplicity(0, 9999))
    }
)
hasResult57: BinaryAssociation = BinaryAssociation(
    name="hasResult57",
    ends={
        Property(name="ServiceResult", type=service_semantics_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceProfile58", type=ServiceResult, multiplicity=Multiplicity(0, 9999))
    }
)
hasCondition59: BinaryAssociation = BinaryAssociation(
    name="hasCondition59",
    ends={
        Property(name="ServiceCondition", type=service_semantics_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceProfile60", type=ServiceCondition, multiplicity=Multiplicity(0, 9999))
    }
)
binding40: BinaryAssociation = BinaryAssociation(
    name="binding40",
    ends={
        Property(name="Binding41", type=service_syntax_Endpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_Endpoint", type=Binding, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
implementation42: BinaryAssociation = BinaryAssociation(
    name="implementation42",
    ends={
        Property(name="syntax_service_ServiceImplemetation", type=service_syntax_Endpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_Endpoint43", type=syntax_service_ServiceImplemetation, multiplicity=Multiplicity(0, 1))
    }
)
deployedService44: BinaryAssociation = BinaryAssociation(
    name="deployedService44",
    ends={
        Property(name="DeployedService", type=service_syntax_Endpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="service_syntax_Endpoint45", type=DeployedService, multiplicity=Multiplicity(0, 1))
    }
)
type46: BinaryAssociation = BinaryAssociation(
    name="type46",
    ends={
        Property(name="InterfaceDescription47", type=service_syntax_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="binding", type=InterfaceDescription, multiplicity=Multiplicity(1, 1))
    }
)
type70: BinaryAssociation = BinaryAssociation(
    name="type70",
    ends={
        Property(name="semantics_service_EObject", type=service_semantics_ServiceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceParameter", type=semantics_service_EObject, multiplicity=Multiplicity(0, 1))
    }
)
expression71: BinaryAssociation = BinaryAssociation(
    name="expression71",
    ends={
        Property(name="semantics_service_Antecedent", type=service_semantics_ServiceCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceCondition", type=semantics_service_Antecedent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression72: BinaryAssociation = BinaryAssociation(
    name="expression72",
    ends={
        Property(name="semantics_service_Antecedent73", type=service_semantics_ServiceResult, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceResult", type=semantics_service_Antecedent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result74: BinaryAssociation = BinaryAssociation(
    name="result74",
    ends={
        Property(name="semantics_service_Consequent", type=service_semantics_ServiceResult, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceResult75", type=semantics_service_Consequent, multiplicity=Multiplicity(0, 1))
    }
)
hasInput76: BinaryAssociation = BinaryAssociation(
    name="hasInput76",
    ends={
        Property(name="ServiceInput77", type=service_semantics_IOEP, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_IOEP", type=ServiceInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasCondition78: BinaryAssociation = BinaryAssociation(
    name="hasCondition78",
    ends={
        Property(name="ServiceCondition80", type=service_semantics_IOEP, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_IOEP79", type=ServiceCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasOutput81: BinaryAssociation = BinaryAssociation(
    name="hasOutput81",
    ends={
        Property(name="ServiceOutput83", type=service_semantics_IOEP, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_IOEP82", type=ServiceOutput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supportedBy61: BinaryAssociation = BinaryAssociation(
    name="supportedBy61",
    ends={
        Property(name="Service62", type=service_semantics_ServiceGrounding, multiplicity=Multiplicity(1, 1)),
        Property(name="supports", type=semantics_service_Service, multiplicity=Multiplicity(0, 1))
    }
)
hasResult84: BinaryAssociation = BinaryAssociation(
    name="hasResult84",
    ends={
        Property(name="ServiceResult86", type=service_semantics_IOEP, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_IOEP85", type=ServiceResult, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processModel63: BinaryAssociation = BinaryAssociation(
    name="processModel63",
    ends={
        Property(name="ProcessModel64", type=service_semantics_ServiceGrounding, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceGrounding", type=ProcessModel, multiplicity=Multiplicity(0, 1))
    }
)
interface65: BinaryAssociation = BinaryAssociation(
    name="interface65",
    ends={
        Property(name="InterfaceDescription67", type=service_semantics_ServiceGrounding, multiplicity=Multiplicity(1, 1)),
        Property(name="service_semantics_ServiceGrounding66", type=InterfaceDescription, multiplicity=Multiplicity(0, 1))
    }
)
flow87: BinaryAssociation = BinaryAssociation(
    name="flow87",
    ends={
        Property(name="TemplateFlow", type=service_template_ServiceTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ServiceTemplate", type=TemplateFlow, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateParameter88: BinaryAssociation = BinaryAssociation(
    name="templateParameter88",
    ends={
        Property(name="ServiceParameter", type=service_template_ServiceTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ServiceTemplate89", type=ServiceParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expose90: BinaryAssociation = BinaryAssociation(
    name="expose90",
    ends={
        Property(name="AbstractProcessModel", type=service_template_ServiceTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ServiceTemplate91", type=AbstractProcessModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
describes68: BinaryAssociation = BinaryAssociation(
    name="describes68",
    ends={
        Property(name="Service69", type=service_semantics_ProcessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="describedBy", type=semantics_service_Service, multiplicity=Multiplicity(0, 1))
    }
)
constraints92: BinaryAssociation = BinaryAssociation(
    name="constraints92",
    ends={
        Property(name="TemplateConstraint", type=service_template_ServiceTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ServiceTemplate93", type=TemplateConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
composedOf94: BinaryAssociation = BinaryAssociation(
    name="composedOf94",
    ends={
        Property(name="ControlConstruct", type=service_template_TemplateFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_TemplateFlow", type=ControlConstruct, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implement95: BinaryAssociation = BinaryAssociation(
    name="implement95",
    ends={
        Property(name="ServiceTemplate", type=service_template_GroundTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_GroundTemplate", type=ServiceTemplate, multiplicity=Multiplicity(0, 1))
    }
)
bindTemplateParameter96: BinaryAssociation = BinaryAssociation(
    name="bindTemplateParameter96",
    ends={
        Property(name="BoundTemplateParameter", type=service_template_GroundTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_GroundTemplate97", type=BoundTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindProcessModel98: BinaryAssociation = BinaryAssociation(
    name="bindProcessModel98",
    ends={
        Property(name="BoundProcessModel", type=service_template_GroundTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_GroundTemplate99", type=BoundProcessModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expose100: BinaryAssociation = BinaryAssociation(
    name="expose100",
    ends={
        Property(name="Service101", type=service_template_GroundTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="adaptedBy", type=template_service_Service, multiplicity=Multiplicity(1, 1))
    }
)
abstract102: BinaryAssociation = BinaryAssociation(
    name="abstract102",
    ends={
        Property(name="ServiceParameter103", type=service_template_BoundTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_BoundTemplateParameter", type=ServiceParameter, multiplicity=Multiplicity(1, 1))
    }
)
concrete104: BinaryAssociation = BinaryAssociation(
    name="concrete104",
    ends={
        Property(name="ServiceParameter106", type=service_template_BoundTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_BoundTemplateParameter105", type=ServiceParameter, multiplicity=Multiplicity(1, 1))
    }
)
abstract107: BinaryAssociation = BinaryAssociation(
    name="abstract107",
    ends={
        Property(name="AbstractProcessModel108", type=service_template_BoundProcessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_BoundProcessModel", type=AbstractProcessModel, multiplicity=Multiplicity(1, 1))
    }
)
concrete109: BinaryAssociation = BinaryAssociation(
    name="concrete109",
    ends={
        Property(name="ProcessModel111", type=service_template_BoundProcessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_BoundProcessModel110", type=ProcessModel, multiplicity=Multiplicity(1, 1))
    }
)
body112: BinaryAssociation = BinaryAssociation(
    name="body112",
    ends={
        Property(name="template_service_Antecedent", type=service_template_TemplateConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_TemplateConstraint", type=template_service_Antecedent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timeout113: BinaryAssociation = BinaryAssociation(
    name="timeout113",
    ends={
        Property(name="IntervalThing", type=service_template_ControlConstruct, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ControlConstruct", type=IntervalThing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
components114: BinaryAssociation = BinaryAssociation(
    name="components114",
    ends={
        Property(name="ControlConstructBag", type=service_template_AnyOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_AnyOrder", type=ControlConstructBag, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
components115: BinaryAssociation = BinaryAssociation(
    name="components115",
    ends={
        Property(name="ControlConstructBag116", type=service_template_Choice, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_Choice", type=ControlConstructBag, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifCondition117: BinaryAssociation = BinaryAssociation(
    name="ifCondition117",
    ends={
        Property(name="template_service_Antecedent118", type=service_template_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_IfThenElse", type=template_service_Antecedent, multiplicity=Multiplicity(1, 1))
    }
)
then119: BinaryAssociation = BinaryAssociation(
    name="then119",
    ends={
        Property(name="ControlConstruct121", type=service_template_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_IfThenElse120", type=ControlConstruct, multiplicity=Multiplicity(1, 1))
    }
)
else_122: BinaryAssociation = BinaryAssociation(
    name="else_122",
    ends={
        Property(name="ControlConstruct124", type=service_template_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_IfThenElse123", type=ControlConstruct, multiplicity=Multiplicity(0, 1))
    }
)
partnerProcess125: BinaryAssociation = BinaryAssociation(
    name="partnerProcess125",
    ends={
        Property(name="AbstractProcessModel126", type=service_template_Perform, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_Perform", type=AbstractProcessModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
hasDataFromProcess127: BinaryAssociation = BinaryAssociation(
    name="hasDataFromProcess127",
    ends={
        Property(name="AbstractProcessModel129", type=service_template_Perform, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_Perform128", type=AbstractProcessModel, multiplicity=Multiplicity(0, 1))
    }
)
valueData130: BinaryAssociation = BinaryAssociation(
    name="valueData130",
    ends={
        Property(name="ServiceParameter132", type=service_template_Perform, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_Perform131", type=ServiceParameter, multiplicity=Multiplicity(0, 1))
    }
)
hasDataFromTemplate133: BinaryAssociation = BinaryAssociation(
    name="hasDataFromTemplate133",
    ends={
        Property(name="ServiceTemplate135", type=service_template_Perform, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_Perform134", type=ServiceTemplate, multiplicity=Multiplicity(0, 1))
    }
)
untilCondition136: BinaryAssociation = BinaryAssociation(
    name="untilCondition136",
    ends={
        Property(name="template_service_Antecedent137", type=service_template_RepeatUntil, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_RepeatUntil", type=template_service_Antecedent, multiplicity=Multiplicity(1, 1))
    }
)
untilProcess138: BinaryAssociation = BinaryAssociation(
    name="untilProcess138",
    ends={
        Property(name="ControlConstruct140", type=service_template_RepeatUntil, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_RepeatUntil139", type=ControlConstruct, multiplicity=Multiplicity(1, 1))
    }
)
whileCondition141: BinaryAssociation = BinaryAssociation(
    name="whileCondition141",
    ends={
        Property(name="template_service_Antecedent142", type=service_template_RepeatWhile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_RepeatWhile", type=template_service_Antecedent, multiplicity=Multiplicity(1, 1))
    }
)
whileProcess143: BinaryAssociation = BinaryAssociation(
    name="whileProcess143",
    ends={
        Property(name="ControlConstruct145", type=service_template_RepeatWhile, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_RepeatWhile144", type=ControlConstruct, multiplicity=Multiplicity(1, 1))
    }
)
components146: BinaryAssociation = BinaryAssociation(
    name="components146",
    ends={
        Property(name="ControlConstructList", type=service_template_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_Sequence", type=ControlConstructList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
components147: BinaryAssociation = BinaryAssociation(
    name="components147",
    ends={
        Property(name="ControlConstructBag148", type=service_template_Split, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_Split", type=ControlConstructBag, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
components149: BinaryAssociation = BinaryAssociation(
    name="components149",
    ends={
        Property(name="ControlConstructBag150", type=service_template_SplitJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_SplitJoin", type=ControlConstructBag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first151: BinaryAssociation = BinaryAssociation(
    name="first151",
    ends={
        Property(name="ControlConstruct152", type=service_template_ControlConstructList, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ControlConstructList", type=ControlConstruct, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest153: BinaryAssociation = BinaryAssociation(
    name="rest153",
    ends={
        Property(name="ControlConstructList155", type=service_template_ControlConstructList, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ControlConstructList154", type=ControlConstructList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first156: BinaryAssociation = BinaryAssociation(
    name="first156",
    ends={
        Property(name="ControlConstruct157", type=service_template_ControlConstructBag, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ControlConstructBag", type=ControlConstruct, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rest158: BinaryAssociation = BinaryAssociation(
    name="rest158",
    ends={
        Property(name="ControlConstructBag160", type=service_template_ControlConstructBag, multiplicity=Multiplicity(1, 1)),
        Property(name="service_template_ControlConstructBag159", type=ControlConstructBag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
matchmaker161: BinaryAssociation = BinaryAssociation(
    name="matchmaker161",
    ends={
        Property(name="ServiceTemplateMatchmaker", type=service_architecture_ServiceFramework, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceFramework", type=ServiceTemplateMatchmaker, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
execution162: BinaryAssociation = BinaryAssociation(
    name="execution162",
    ends={
        Property(name="ExecutionFramework", type=service_architecture_ServiceFramework, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceFramework163", type=ExecutionFramework, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceDirectory164: BinaryAssociation = BinaryAssociation(
    name="serviceDirectory164",
    ends={
        Property(name="ServiceDirectory", type=service_architecture_ServiceFramework, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceFramework165", type=ServiceDirectory, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
templateRepository166: BinaryAssociation = BinaryAssociation(
    name="templateRepository166",
    ends={
        Property(name="TemplateRepository", type=service_architecture_ServiceFramework, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceFramework167", type=TemplateRepository, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
template168: BinaryAssociation = BinaryAssociation(
    name="template168",
    ends={
        Property(name="ServiceTemplate169", type=service_architecture_TemplateRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_TemplateRepository", type=ServiceTemplate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groundTemplate170: BinaryAssociation = BinaryAssociation(
    name="groundTemplate170",
    ends={
        Property(name="GroundTemplate172", type=service_architecture_TemplateRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_TemplateRepository171", type=GroundTemplate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templateRepository173: BinaryAssociation = BinaryAssociation(
    name="templateRepository173",
    ends={
        Property(name="service_architecture_TemplateMatchmaker", type=TemplateRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="TemplateRepository174", type=service_architecture_TemplateMatchmaker, multiplicity=Multiplicity(1, 1))
    }
)
serviceDirectory175: BinaryAssociation = BinaryAssociation(
    name="serviceDirectory175",
    ends={
        Property(name="ServiceDirectory176", type=service_architecture_ServiceMatchmaker, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceMatchmaker", type=ServiceDirectory, multiplicity=Multiplicity(1, 9999))
    }
)
endpoint177: BinaryAssociation = BinaryAssociation(
    name="endpoint177",
    ends={
        Property(name="Endpoint178", type=service_architecture_ServiceDirectory, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceDirectory", type=Endpoint, multiplicity=Multiplicity(0, 9999))
    }
)
semantic179: BinaryAssociation = BinaryAssociation(
    name="semantic179",
    ends={
        Property(name="ServiceProfile181", type=service_architecture_ServiceDirectory, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceDirectory180", type=ServiceProfile, multiplicity=Multiplicity(0, 1))
    }
)
interface182: BinaryAssociation = BinaryAssociation(
    name="interface182",
    ends={
        Property(name="InterfaceDescription184", type=service_architecture_ServiceDirectory, multiplicity=Multiplicity(1, 1)),
        Property(name="service_architecture_ServiceDirectory183", type=InterfaceDescription, multiplicity=Multiplicity(0, 9999))
    }
)
deployedService185: BinaryAssociation = BinaryAssociation(
    name="deployedService185",
    ends={
        Property(name="DeployedService186", type=service_architecture_ExecutionFramework, multiplicity=Multiplicity(1, 1)),
        Property(name="deploy", type=DeployedService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deploy187: BinaryAssociation = BinaryAssociation(
    name="deploy187",
    ends={
        Property(name="ExecutionFramework188", type=service_architecture_DeployedService, multiplicity=Multiplicity(1, 1)),
        Property(name="deployedService", type=ExecutionFramework, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_service_ServiceConsumer_Agent = Generalization(general=Agent, specific=service_ServiceConsumer)
gen_service_ServiceProvider_Agent = Generalization(general=Agent, specific=service_ServiceProvider)
gen_service_semantics_ServiceInput_ServiceParameter = Generalization(general=ServiceParameter, specific=service_semantics_ServiceInput)
gen_service_semantics_ServiceOutput_ServiceParameter = Generalization(general=ServiceParameter, specific=service_semantics_ServiceOutput)
gen_service_semantics_ProcessModel_IOEP = Generalization(general=IOEP, specific=service_semantics_ProcessModel)
gen_service_template_AbstractProcessModel_IOEP = Generalization(general=IOEP, specific=service_template_AbstractProcessModel)
gen_service_template_AnyOrder_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_AnyOrder)
gen_service_template_Choice_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_Choice)
gen_service_template_Iterate_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_Iterate)
gen_service_template_Perform_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_Perform)
gen_service_template_RepeatUntil_Iterate = Generalization(general=Iterate, specific=service_template_RepeatUntil)
gen_service_template_RepeatWhile_Iterate = Generalization(general=Iterate, specific=service_template_RepeatWhile)
gen_service_template_Sequence_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_Sequence)
gen_service_template_Split_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_Split)
gen_service_template_IfThenElse_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_IfThenElse)
gen_service_template_SplitJoin_ControlConstruct = Generalization(general=ControlConstruct, specific=service_template_SplitJoin)
gen_service_architecture_ServiceTemplateMatchmaker_architecture_ServiceMatchmaker = Generalization(general=architecture_ServiceMatchmaker, specific=service_architecture_ServiceTemplateMatchmaker)
gen_service_architecture_ServiceTemplateMatchmaker_architecture_TemplateMatchmaker = Generalization(general=architecture_TemplateMatchmaker, specific=service_architecture_ServiceTemplateMatchmaker)

# Domain Model
domain_model = DomainModel(
    name="service",
    types={service_Service, Endpoint, service_ServiceImplemetation, service_ServiceConsumer, service_SL, InterfaceDescription, ServiceProfile, ServiceGrounding, ProcessModel, GroundTemplate, service_ServiceProvider, Agent, syntax_service_SchemaType, service_syntax_OperationDescription, Message, service_syntax_Message, syntax_service_TopLevelComplexType, syntax_service_TopLevelElement, ServiceFramework, service_syntax_InterfaceDescription, OperationDescription, Binding, service_semantics_ServiceProfile, semantics_service_Service, ServiceCategory, ServiceInput, ServiceOutput, ServiceResult, ServiceCondition, service_syntax_Endpoint, syntax_service_ServiceImplemetation, DeployedService, service_syntax_Binding, service_semantics_ServiceInput, ServiceParameter, service_semantics_ServiceOutput, service_semantics_ServiceCondition, semantics_service_Antecedent, service_semantics_ServiceResult, semantics_service_Consequent, service_semantics_IOEP, service_semantics_ServiceGrounding, service_template_ServiceTemplate, TemplateFlow, service_semantics_ProcessModel, IOEP, AbstractProcessModel, TemplateConstraint, service_semantics_ServiceCategory, service_template_TemplateFlow, ControlConstruct, service_semantics_ServiceParameter, semantics_service_EObject, BoundTemplateParameter, BoundProcessModel, template_service_Service, service_template_AbstractProcessModel, service_template_BoundTemplateParameter, service_template_BoundProcessModel, service_template_TemplateConstraint, template_service_Antecedent, service_template_ControlConstruct, IntervalThing, service_template_AnyOrder, ControlConstructBag, service_template_Choice, service_template_GroundTemplate, ServiceTemplate, service_template_Iterate, service_template_Perform, service_template_RepeatUntil, Iterate, service_template_RepeatWhile, service_template_Sequence, ControlConstructList, service_template_Split, service_template_IfThenElse, service_template_SplitJoin, service_template_ControlConstructList, service_template_ControlConstructBag, service_template_IntervalThing, service_architecture_ServiceFramework, ServiceTemplateMatchmaker, ExecutionFramework, ServiceDirectory, TemplateRepository, service_architecture_TemplateRepository, service_architecture_TemplateMatchmaker, service_architecture_ServiceMatchmaker, service_architecture_ServiceTemplateMatchmaker, architecture_ServiceMatchmaker, architecture_TemplateMatchmaker, service_architecture_ServiceDirectory, service_architecture_ExecutionFramework, service_architecture_DeployedService, ServiceType, ServiceImpLanguage, StyleEncoding, TransportProtocol, ContainerType},
    associations={endpoint0, exposes7, implementation9, invokes11, services13, interface1, presents3, supports4, describedBy5, adaptedBy6, inLineSchema25, outLineSchema27, input30, fault31, output34, type37, element38, providers15, consumers18, framework21, operation23, binding24, presentedBy48, hasProcess49, serviceCategory51, hasInput53, hasOutput55, hasResult57, hasCondition59, binding40, implementation42, deployedService44, type46, type70, expression71, expression72, result74, hasInput76, hasCondition78, hasOutput81, supportedBy61, hasResult84, processModel63, interface65, flow87, templateParameter88, expose90, describes68, constraints92, composedOf94, implement95, bindTemplateParameter96, bindProcessModel98, expose100, abstract102, concrete104, abstract107, concrete109, body112, timeout113, components114, components115, ifCondition117, then119, else_122, partnerProcess125, hasDataFromProcess127, valueData130, hasDataFromTemplate133, untilCondition136, untilProcess138, whileCondition141, whileProcess143, components146, components147, components149, first151, rest153, first156, rest158, matchmaker161, execution162, serviceDirectory164, templateRepository166, template168, groundTemplate170, templateRepository173, serviceDirectory175, endpoint177, semantic179, interface182, deployedService185, deploy187},
    generalizations={gen_service_ServiceConsumer_Agent, gen_service_ServiceProvider_Agent, gen_service_semantics_ServiceInput_ServiceParameter, gen_service_semantics_ServiceOutput_ServiceParameter, gen_service_semantics_ProcessModel_IOEP, gen_service_template_AbstractProcessModel_IOEP, gen_service_template_AnyOrder_ControlConstruct, gen_service_template_Choice_ControlConstruct, gen_service_template_Iterate_ControlConstruct, gen_service_template_Perform_ControlConstruct, gen_service_template_RepeatUntil_Iterate, gen_service_template_RepeatWhile_Iterate, gen_service_template_Sequence_ControlConstruct, gen_service_template_Split_ControlConstruct, gen_service_template_IfThenElse_ControlConstruct, gen_service_template_SplitJoin_ControlConstruct, gen_service_architecture_ServiceTemplateMatchmaker_architecture_ServiceMatchmaker, gen_service_architecture_ServiceTemplateMatchmaker_architecture_TemplateMatchmaker},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)