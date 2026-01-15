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
CorrelationPattern: Enumeration = Enumeration(
    name="CorrelationPattern",
    literals={
            EnumerationLiteral(name="request"),
			EnumerationLiteral(name="response"),
			EnumerationLiteral(name="requestresponse")
    }
)

EndpointReferenceRole: Enumeration = Enumeration(
    name="EndpointReferenceRole",
    literals={
            EnumerationLiteral(name="myRole"),
			EnumerationLiteral(name="partnerRole")
    }
)

XSDConstraint: Enumeration = Enumeration(
    name="XSDConstraint",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="fixed")
    }
)

XSDContentTypeCategory: Enumeration = Enumeration(
    name="XSDContentTypeCategory",
    literals={
            EnumerationLiteral(name="empty"),
			EnumerationLiteral(name="simple"),
			EnumerationLiteral(name="mixed"),
			EnumerationLiteral(name="elementOnly")
    }
)

XSDDerivationMethod: Enumeration = Enumeration(
    name="XSDDerivationMethod",
    literals={
            EnumerationLiteral(name="extension"),
			EnumerationLiteral(name="restriction")
    }
)

XSDAttributeUseCategory: Enumeration = Enumeration(
    name="XSDAttributeUseCategory",
    literals={
            EnumerationLiteral(name="optional"),
			EnumerationLiteral(name="prohibited"),
			EnumerationLiteral(name="required")
    }
)

XSDCardinality: Enumeration = Enumeration(
    name="XSDCardinality",
    literals={
            EnumerationLiteral(name="finite"),
			EnumerationLiteral(name="countablyInfinite")
    }
)

XSDComplexFinal: Enumeration = Enumeration(
    name="XSDComplexFinal",
    literals={
            EnumerationLiteral(name="extension"),
			EnumerationLiteral(name="restriction"),
			EnumerationLiteral(name="all")
    }
)

XSDCompositor: Enumeration = Enumeration(
    name="XSDCompositor",
    literals={
            EnumerationLiteral(name="sequence"),
			EnumerationLiteral(name="all"),
			EnumerationLiteral(name="choice")
    }
)

XSDXPathVariety: Enumeration = Enumeration(
    name="XSDXPathVariety",
    literals={
            EnumerationLiteral(name="selector"),
			EnumerationLiteral(name="field")
    }
)

XSDDiagnosticSeverity: Enumeration = Enumeration(
    name="XSDDiagnosticSeverity",
    literals={
            EnumerationLiteral(name="fatal"),
			EnumerationLiteral(name="error"),
			EnumerationLiteral(name="warning"),
			EnumerationLiteral(name="information")
    }
)

XSDDisallowedSubstitutions: Enumeration = Enumeration(
    name="XSDDisallowedSubstitutions",
    literals={
            EnumerationLiteral(name="substitution"),
			EnumerationLiteral(name="extension"),
			EnumerationLiteral(name="restriction"),
			EnumerationLiteral(name="all")
    }
)

XSDForm: Enumeration = Enumeration(
    name="XSDForm",
    literals={
            EnumerationLiteral(name="qualified"),
			EnumerationLiteral(name="unqualified")
    }
)

XSDIdentityConstraintCategory: Enumeration = Enumeration(
    name="XSDIdentityConstraintCategory",
    literals={
            EnumerationLiteral(name="key"),
			EnumerationLiteral(name="keyref"),
			EnumerationLiteral(name="unique")
    }
)

XSDNamespaceConstraintCategory: Enumeration = Enumeration(
    name="XSDNamespaceConstraintCategory",
    literals={
            EnumerationLiteral(name="any"),
			EnumerationLiteral(name="not"),
			EnumerationLiteral(name="set")
    }
)

XSDOrdered: Enumeration = Enumeration(
    name="XSDOrdered",
    literals={
            EnumerationLiteral(name="false"),
			EnumerationLiteral(name="partial"),
			EnumerationLiteral(name="total")
    }
)

XSDProcessContents: Enumeration = Enumeration(
    name="XSDProcessContents",
    literals={
            EnumerationLiteral(name="strict"),
			EnumerationLiteral(name="lax"),
			EnumerationLiteral(name="skip")
    }
)

XSDProhibitedSubstitutions: Enumeration = Enumeration(
    name="XSDProhibitedSubstitutions",
    literals={
            EnumerationLiteral(name="extension"),
			EnumerationLiteral(name="restriction"),
			EnumerationLiteral(name="all")
    }
)

XSDSimpleFinal: Enumeration = Enumeration(
    name="XSDSimpleFinal",
    literals={
            EnumerationLiteral(name="list"),
			EnumerationLiteral(name="restriction"),
			EnumerationLiteral(name="union"),
			EnumerationLiteral(name="all")
    }
)

XSDSubstitutionGroupExclusions: Enumeration = Enumeration(
    name="XSDSubstitutionGroupExclusions",
    literals={
            EnumerationLiteral(name="extension"),
			EnumerationLiteral(name="restriction")
    }
)

XSDVariety: Enumeration = Enumeration(
    name="XSDVariety",
    literals={
            EnumerationLiteral(name="atomic"),
			EnumerationLiteral(name="list"),
			EnumerationLiteral(name="union")
    }
)

XSDWhiteSpace: Enumeration = Enumeration(
    name="XSDWhiteSpace",
    literals={
            EnumerationLiteral(name="replace"),
			EnumerationLiteral(name="collapse"),
			EnumerationLiteral(name="preserve")
    }
)

# Classes
model_Process = Class(name="model::Process")
BPELExtensibleElement = Class(name="BPELExtensibleElement")
model_MessageExchanges = Class(name="model::MessageExchanges")
model_PartnerLinks = Class(name="model::PartnerLinks")
model_Variables = Class(name="model::Variables")
model_Activity = Class(name="model::Activity")
model_FaultHandler = Class(name="model::FaultHandler")
model_EventHandler = Class(name="model::EventHandler")
model_CorrelationSets = Class(name="model::CorrelationSets")
model_Import = Class(name="model::Import")
model_Extensions = Class(name="model::Extensions")
model_PartnerLink = Class(name="model::PartnerLink")
Role = Class(name="Role")
PartnerLinkType = Class(name="PartnerLinkType")
model_Catch = Class(name="model::Catch")
model_CatchAll = Class(name="model::CatchAll")
model_ToParts = Class(name="model::ToParts")
model_Link = Class(name="model::Link")
model_Targets = Class(name="model::Targets")
model_Sources = Class(name="model::Sources")
model_CorrelationSet = Class(name="model::CorrelationSet")
Property_ = Class(name="Property")
model_Invoke = Class(name="model::Invoke")
PartnerActivity = Class(name="PartnerActivity")
model_Variable = Class(name="model::Variable")
model_CompensationHandler = Class(name="model::CompensationHandler")
model_FromParts = Class(name="model::FromParts")
PortType = Class(name="PortType")
model_Source = Class(name="model::Source")
model_Target = Class(name="model::Target")
Message = Class(name="Message")
XSDElementDeclaration = Class(name="XSDElementDeclaration")
model_Reply = Class(name="model::Reply")
Activity = Class(name="Activity")
model_MessageExchange = Class(name="model::MessageExchange")
model_PartnerActivity = Class(name="model::PartnerActivity")
model_Pick = Class(name="model::Pick")
model_Correlations = Class(name="model::Correlations")
Operation = Class(name="Operation")
model_Receive = Class(name="model::Receive")
model_Exit = Class(name="model::Exit")
model_Throw = Class(name="model::Throw")
model_Wait = Class(name="model::Wait")
model_Expression = Class(name="model::Expression")
model_Empty = Class(name="model::Empty")
model_Sequence = Class(name="model::Sequence")
model_While = Class(name="model::While")
model_Condition = Class(name="model::Condition")
model_Extension = Class(name="model::Extension")
model_OnMessage = Class(name="model::OnMessage")
model_OnAlarm = Class(name="model::OnAlarm")
model_Flow = Class(name="model::Flow")
model_Links = Class(name="model::Links")
model_CompletionCondition = Class(name="model::CompletionCondition")
model_Assign = Class(name="model::Assign")
model_Copy = Class(name="model::Copy")
model_To = Class(name="model::To")
model_From = Class(name="model::From")
Part = Class(name="Part")
model_Scope = Class(name="model::Scope")
model_TerminationHandler = Class(name="model::TerminationHandler")
model_CompensateScope = Class(name="model::CompensateScope")
model_AbstractAssignBound = Class(name="model::AbstractAssignBound", is_abstract=True)
model_Query = Class(name="model::Query")
AbstractAssignBound = Class(name="AbstractAssignBound")
model_ServiceRef = Class(name="model::ServiceRef")
XSDTypeDefinition = Class(name="XSDTypeDefinition")
ExtensibilityElement = Class(name="ExtensibilityElement")
model_BooleanExpression = Class(name="model::BooleanExpression")
Expression = Class(name="Expression")
model_Correlation = Class(name="model::Correlation")
model_OnEvent = Class(name="model::OnEvent")
model_UnknownExtensibilityAttribute = Class(name="model::UnknownExtensibilityAttribute")
UnknownExtensibilityElement = Class(name="UnknownExtensibilityElement")
model_Rethrow = Class(name="model::Rethrow")
WSDLElement = Class(name="WSDLElement")
ExtensibleElement = Class(name="ExtensibleElement")
model_ExtensionActivity = Class(name="model::ExtensionActivity")
model_FromPart = Class(name="model::FromPart")
model_ToPart = Class(name="model::ToPart")
model_OpaqueActivity = Class(name="model::OpaqueActivity")
model_ForEach = Class(name="model::ForEach")
model_RepeatUntil = Class(name="model::RepeatUntil")
model_Validate = Class(name="model::Validate")
model_If = Class(name="model::If")
model_ElseIf = Class(name="model::ElseIf")
model_Else = Class(name="model::Else")
model_Branches = Class(name="model::Branches")
model_BPELExtensibleElement = Class(name="model::BPELExtensibleElement")
model_Documentation = Class(name="model::Documentation")
model_Compensate = Class(name="model::Compensate")
model_wsdl_WSDLElement = Class(name="model::wsdl::WSDLElement", is_abstract=True)
model_wsdl_PortType = Class(name="model::wsdl::PortType")
wsdl_ExtensibleElement = Class(name="wsdl::ExtensibleElement")
wsdl_IPortType = Class(name="wsdl::IPortType")
model_wsdl_Operation = Class(name="model::wsdl::Operation")
wsdl_IOperation = Class(name="wsdl::IOperation")
Input = Class(name="Input")
Output = Class(name="Output")
Fault = Class(name="Fault")
model_wsdl_Message = Class(name="model::wsdl::Message")
wsdl_IMessage = Class(name="wsdl::IMessage")
model_wsdl_Part = Class(name="model::wsdl::Part")
wsdl_IPart = Class(name="wsdl::IPart")
model_wsdl_Binding = Class(name="model::wsdl::Binding")
wsdl_IBinding = Class(name="wsdl::IBinding")
model_wsdl_Definition = Class(name="model::wsdl::Definition")
BindingOperation = Class(name="BindingOperation")
model_wsdl_BindingOperation = Class(name="model::wsdl::BindingOperation")
wsdl_IBindingOperation = Class(name="wsdl::IBindingOperation")
BindingInput = Class(name="BindingInput")
BindingOutput = Class(name="BindingOutput")
BindingFault = Class(name="BindingFault")
model_wsdl_Service = Class(name="model::wsdl::Service")
wsdl_IService = Class(name="wsdl::IService")
Port = Class(name="Port")
model_wsdl_Port = Class(name="model::wsdl::Port")
wsdl_IPort = Class(name="wsdl::IPort")
Binding = Class(name="Binding")
model_wsdl_ExtensibilityElement = Class(name="model::wsdl::ExtensibilityElement")
wsdl_WSDLElement = Class(name="wsdl::WSDLElement")
wsdl_IExtensibilityElement = Class(name="wsdl::IExtensibilityElement")
wsdl_IElementExtensible = Class(name="wsdl::IElementExtensible")
wsdl_IAttributeExtensible = Class(name="wsdl::IAttributeExtensible")
wsdl_IDefinition = Class(name="wsdl::IDefinition")
model_wsdl_Input = Class(name="model::wsdl::Input")
wsdl_MessageReference = Class(name="wsdl::MessageReference")
wsdl_IInput = Class(name="wsdl::IInput")
Import = Class(name="Import")
Types = Class(name="Types")
Service = Class(name="Service")
Namespace = Class(name="Namespace")
model_wsdl_Import = Class(name="model::wsdl::Import")
wsdl_IImport = Class(name="wsdl::IImport")
Definition = Class(name="Definition")
XSDSchema = Class(name="XSDSchema")
model_wsdl_ExtensibleElement = Class(name="model::wsdl::ExtensibleElement", is_abstract=True)
model_wsdl_Namespace = Class(name="model::wsdl::Namespace")
model_wsdl_Output = Class(name="model::wsdl::Output")
wsdl_IOutput = Class(name="wsdl::IOutput")
model_wsdl_Fault = Class(name="model::wsdl::Fault")
wsdl_IFault = Class(name="wsdl::IFault")
model_wsdl_BindingInput = Class(name="model::wsdl::BindingInput")
wsdl_IBindingInput = Class(name="wsdl::IBindingInput")
model_wsdl_BindingOutput = Class(name="model::wsdl::BindingOutput")
wsdl_IBindingOutput = Class(name="wsdl::IBindingOutput")
model_wsdl_BindingFault = Class(name="model::wsdl::BindingFault")
wsdl_IBindingFault = Class(name="wsdl::IBindingFault")
model_wsdl_IMessage = Class(name="model::wsdl::IMessage", is_abstract=True)
model_wsdl_IPortType = Class(name="model::wsdl::IPortType", is_abstract=True)
IAttributeExtensible = Class(name="IAttributeExtensible")
model_wsdl_IOperation = Class(name="model::wsdl::IOperation", is_abstract=True)
IElementExtensible = Class(name="IElementExtensible")
model_wsdl_IInput = Class(name="model::wsdl::IInput", is_abstract=True)
model_wsdl_IOutput = Class(name="model::wsdl::IOutput", is_abstract=True)
model_wsdl_IFault = Class(name="model::wsdl::IFault", is_abstract=True)
model_wsdl_IBindingInput = Class(name="model::wsdl::IBindingInput", is_abstract=True)
model_wsdl_IPart = Class(name="model::wsdl::IPart", is_abstract=True)
model_wsdl_IService = Class(name="model::wsdl::IService", is_abstract=True)
model_wsdl_IPort = Class(name="model::wsdl::IPort", is_abstract=True)
model_wsdl_IBinding = Class(name="model::wsdl::IBinding", is_abstract=True)
model_wsdl_IBindingOperation = Class(name="model::wsdl::IBindingOperation", is_abstract=True)
model_wsdl_IBindingOutput = Class(name="model::wsdl::IBindingOutput", is_abstract=True)
model_wsdl_IBindingFault = Class(name="model::wsdl::IBindingFault", is_abstract=True)
model_wsdl_IExtensibilityElement = Class(name="model::wsdl::IExtensibilityElement", is_abstract=True)
model_wsdl_IDefinition = Class(name="model::wsdl::IDefinition", is_abstract=True)
model_wsdl_UnknownExtensibilityElement = Class(name="model::wsdl::UnknownExtensibilityElement")
model_wsdl_XSDSchemaExtensibilityElement = Class(name="model::wsdl::XSDSchemaExtensibilityElement")
wsdl_ExtensibilityElement = Class(name="wsdl::ExtensibilityElement")
wsdl_ISchema = Class(name="wsdl::ISchema")
model_wsdl_IImport = Class(name="model::wsdl::IImport", is_abstract=True)
model_wsdl_IList = Class(name="model::wsdl::IList", is_abstract=True)
model_wsdl_IMap = Class(name="model::wsdl::IMap", is_abstract=True)
model_wsdl_IURL = Class(name="model::wsdl::IURL", is_abstract=True)
model_wsdl_IExtensionRegistry = Class(name="model::wsdl::IExtensionRegistry", is_abstract=True)
model_wsdl_Types = Class(name="model::wsdl::Types")
wsdl_ITypes = Class(name="wsdl::ITypes")
model_wsdl_IIterator = Class(name="model::wsdl::IIterator", is_abstract=True)
model_wsdl_ITypes = Class(name="model::wsdl::ITypes", is_abstract=True)
XSDSimpleTypeDefinition = Class(name="XSDSimpleTypeDefinition")
XSDAttributeDeclaration = Class(name="XSDAttributeDeclaration")
model_wsdl_MessageReference = Class(name="model::wsdl::MessageReference", is_abstract=True)
model_wsdl_IElementExtensible = Class(name="model::wsdl::IElementExtensible", is_abstract=True)
model_wsdl_IAttributeExtensible = Class(name="model::wsdl::IAttributeExtensible", is_abstract=True)
model_wsdl_IObject = Class(name="model::wsdl::IObject", is_abstract=True)
model_wsdl_ISchema = Class(name="model::wsdl::ISchema", is_abstract=True)
IExtensibilityElement = Class(name="IExtensibilityElement")
model_xsd_XSDAnnotation = Class(name="model::xsd::XSDAnnotation")
xsd_XSDComponent = Class(name="xsd::XSDComponent")
xsd_XSDRedefineContent = Class(name="xsd::XSDRedefineContent")
model_xsd_XSDAttributeDeclaration = Class(name="model::xsd::XSDAttributeDeclaration")
xsd_XSDFeature = Class(name="xsd::XSDFeature")
xsd_XSDSchemaContent = Class(name="xsd::XSDSchemaContent")
XSDAnnotation = Class(name="XSDAnnotation")
XSDFundamentalFacet = Class(name="XSDFundamentalFacet")
model_xsd_XSDCardinalityFacet = Class(name="model::xsd::XSDCardinalityFacet")
model_xsd_XSDComplexTypeContent = Class(name="model::xsd::XSDComplexTypeContent", is_abstract=True)
XSDComponent = Class(name="XSDComponent")
model_xsd_XSDComplexTypeDefinition = Class(name="model::xsd::XSDComplexTypeDefinition")
xsd_XSDTypeDefinition = Class(name="xsd::XSDTypeDefinition")
model_xsd_XSDAttributeGroupContent = Class(name="model::xsd::XSDAttributeGroupContent", is_abstract=True)
XSDConcreteComponent = Class(name="XSDConcreteComponent")
model_xsd_XSDAttributeGroupDefinition = Class(name="model::xsd::XSDAttributeGroupDefinition")
xsd_XSDRedefinableComponent = Class(name="xsd::XSDRedefinableComponent")
xsd_XSDAttributeGroupContent = Class(name="xsd::XSDAttributeGroupContent")
XSDAttributeGroupContent = Class(name="XSDAttributeGroupContent")
XSDAttributeUse = Class(name="XSDAttributeUse")
XSDWildcard = Class(name="XSDWildcard")
XSDAttributeGroupDefinition = Class(name="XSDAttributeGroupDefinition")
model_xsd_XSDAttributeUse = Class(name="model::xsd::XSDAttributeUse")
model_xsd_XSDBoundedFacet = Class(name="model::xsd::XSDBoundedFacet")
XSDParticle = Class(name="XSDParticle")
xsd_XSDScope = Class(name="xsd::XSDScope")
XSDComplexTypeContent = Class(name="XSDComplexTypeContent")
xsd_XSDTerm = Class(name="xsd::XSDTerm")
model_xsd_XSDComponent = Class(name="model::xsd::XSDComponent", is_abstract=True)
model_xsd_XSDConcreteComponent = Class(name="model::xsd::XSDConcreteComponent", is_abstract=True)
XSDDiagnostic = Class(name="XSDDiagnostic")
model_xsd_XSDConstrainingFacet = Class(name="model::xsd::XSDConstrainingFacet", is_abstract=True)
XSDFacet = Class(name="XSDFacet")
model_xsd_XSDDiagnostic = Class(name="model::xsd::XSDDiagnostic")
model_xsd_XSDElementDeclaration = Class(name="model::xsd::XSDElementDeclaration")
XSDIdentityConstraintDefinition = Class(name="XSDIdentityConstraintDefinition")
model_xsd_XSDEnumerationFacet = Class(name="model::xsd::XSDEnumerationFacet")
XSDRepeatableFacet = Class(name="XSDRepeatableFacet")
model_xsd_XSDFacet = Class(name="model::xsd::XSDFacet", is_abstract=True)
model_xsd_XSDFeature = Class(name="model::xsd::XSDFeature", is_abstract=True)
XSDNamedComponent = Class(name="XSDNamedComponent")
model_xsd_XSDMaxExclusiveFacet = Class(name="model::xsd::XSDMaxExclusiveFacet")
XSDMaxFacet = Class(name="XSDMaxFacet")
model_xsd_XSDMaxFacet = Class(name="model::xsd::XSDMaxFacet", is_abstract=True)
XSDScope = Class(name="XSDScope")
XSDFeature = Class(name="XSDFeature")
model_xsd_XSDFixedFacet = Class(name="model::xsd::XSDFixedFacet", is_abstract=True)
XSDConstrainingFacet = Class(name="XSDConstrainingFacet")
model_xsd_XSDFractionDigitsFacet = Class(name="model::xsd::XSDFractionDigitsFacet")
XSDFixedFacet = Class(name="XSDFixedFacet")
model_xsd_XSDFundamentalFacet = Class(name="model::xsd::XSDFundamentalFacet", is_abstract=True)
model_xsd_XSDIdentityConstraintDefinition = Class(name="model::xsd::XSDIdentityConstraintDefinition")
XSDXPathDefinition = Class(name="XSDXPathDefinition")
model_xsd_XSDImport = Class(name="model::xsd::XSDImport")
XSDSchemaDirective = Class(name="XSDSchemaDirective")
model_xsd_XSDInclude = Class(name="model::xsd::XSDInclude")
XSDSchemaCompositor = Class(name="XSDSchemaCompositor")
model_xsd_XSDLengthFacet = Class(name="model::xsd::XSDLengthFacet")
model_xsd_XSDNotationDeclaration = Class(name="model::xsd::XSDNotationDeclaration")
xsd_XSDNamedComponent = Class(name="xsd::XSDNamedComponent")
model_xsd_XSDMaxInclusiveFacet = Class(name="model::xsd::XSDMaxInclusiveFacet")
model_xsd_XSDMaxLengthFacet = Class(name="model::xsd::XSDMaxLengthFacet")
model_xsd_XSDMinExclusiveFacet = Class(name="model::xsd::XSDMinExclusiveFacet")
XSDMinFacet = Class(name="XSDMinFacet")
model_xsd_XSDMinFacet = Class(name="model::xsd::XSDMinFacet", is_abstract=True)
model_xsd_XSDMinInclusiveFacet = Class(name="model::xsd::XSDMinInclusiveFacet")
model_xsd_XSDMinLengthFacet = Class(name="model::xsd::XSDMinLengthFacet")
model_xsd_XSDModelGroup = Class(name="model::xsd::XSDModelGroup")
XSDTerm = Class(name="XSDTerm")
model_xsd_XSDModelGroupDefinition = Class(name="model::xsd::XSDModelGroupDefinition")
xsd_XSDParticleContent = Class(name="xsd::XSDParticleContent")
XSDModelGroup = Class(name="XSDModelGroup")
XSDModelGroupDefinition = Class(name="XSDModelGroupDefinition")
model_xsd_XSDNamedComponent = Class(name="model::xsd::XSDNamedComponent", is_abstract=True)
model_xsd_XSDSchema = Class(name="model::xsd::XSDSchema")
model_xsd_XSDNumericFacet = Class(name="model::xsd::XSDNumericFacet")
model_xsd_XSDOrderedFacet = Class(name="model::xsd::XSDOrderedFacet")
model_xsd_XSDParticle = Class(name="model::xsd::XSDParticle")
XSDParticleContent = Class(name="XSDParticleContent")
model_xsd_XSDParticleContent = Class(name="model::xsd::XSDParticleContent", is_abstract=True)
model_xsd_XSDPatternFacet = Class(name="model::xsd::XSDPatternFacet")
model_xsd_XSDRedefinableComponent = Class(name="model::xsd::XSDRedefinableComponent", is_abstract=True)
model_xsd_XSDRedefineContent = Class(name="model::xsd::XSDRedefineContent", is_abstract=True)
XSDSchemaContent = Class(name="XSDSchemaContent")
model_xsd_XSDRedefine = Class(name="model::xsd::XSDRedefine")
XSDRedefineContent = Class(name="XSDRedefineContent")
model_xsd_XSDRepeatableFacet = Class(name="model::xsd::XSDRepeatableFacet", is_abstract=True)
XSDNotationDeclaration = Class(name="XSDNotationDeclaration")
model_xsd_XSDSchemaCompositor = Class(name="model::xsd::XSDSchemaCompositor", is_abstract=True)
model_xsd_XSDSchemaContent = Class(name="model::xsd::XSDSchemaContent", is_abstract=True)
model_xsd_XSDSchemaDirective = Class(name="model::xsd::XSDSchemaDirective", is_abstract=True)
model_xsd_XSDScope = Class(name="model::xsd::XSDScope", is_abstract=True)
model_xsd_XSDSimpleTypeDefinition = Class(name="model::xsd::XSDSimpleTypeDefinition")
xsd_XSDComplexTypeContent = Class(name="xsd::XSDComplexTypeContent")
XSDPatternFacet = Class(name="XSDPatternFacet")
XSDCardinalityFacet = Class(name="XSDCardinalityFacet")
XSDMaxInclusiveFacet = Class(name="XSDMaxInclusiveFacet")
XSDMinInclusiveFacet = Class(name="XSDMinInclusiveFacet")
XSDMinExclusiveFacet = Class(name="XSDMinExclusiveFacet")
XSDMaxExclusiveFacet = Class(name="XSDMaxExclusiveFacet")
XSDLengthFacet = Class(name="XSDLengthFacet")
XSDWhiteSpaceFacet = Class(name="XSDWhiteSpaceFacet")
XSDEnumerationFacet = Class(name="XSDEnumerationFacet")
XSDNumericFacet = Class(name="XSDNumericFacet")
XSDMaxLengthFacet = Class(name="XSDMaxLengthFacet")
XSDMinLengthFacet = Class(name="XSDMinLengthFacet")
XSDTotalDigitsFacet = Class(name="XSDTotalDigitsFacet")
XSDFractionDigitsFacet = Class(name="XSDFractionDigitsFacet")
XSDOrderedFacet = Class(name="XSDOrderedFacet")
XSDBoundedFacet = Class(name="XSDBoundedFacet")
model_xsd_XSDTerm = Class(name="model::xsd::XSDTerm", is_abstract=True)
model_xsd_XSDTotalDigitsFacet = Class(name="model::xsd::XSDTotalDigitsFacet")
model_xsd_XSDTypeDefinition = Class(name="model::xsd::XSDTypeDefinition", is_abstract=True)
model_xsd_XSDWhiteSpaceFacet = Class(name="model::xsd::XSDWhiteSpaceFacet")
model_xsd_XSDWildcard = Class(name="model::xsd::XSDWildcard")
model_xsd_XSDXPathDefinition = Class(name="model::xsd::XSDXPathDefinition")
model_partnerlinktype_Role = Class(name="model::partnerlinktype::Role")
model_messageproperties_Property = Class(name="model::messageproperties::Property")
model_messageproperties_PropertyAlias = Class(name="model::messageproperties::PropertyAlias")
Query = Class(name="Query")
model_messageproperties_Query = Class(name="model::messageproperties::Query")
model_partnerlinktype_PartnerLinkType = Class(name="model::partnerlinktype::PartnerLinkType")

# model_Process class attributes and methods
model_Process_name: Property = Property(name="name", type=StringType)
model_Process_targetNamespace: Property = Property(name="targetNamespace", type=StringType)
model_Process_queryLanguage: Property = Property(name="queryLanguage", type=StringType)
model_Process_exitOnStandardFault: Property = Property(name="exitOnStandardFault", type=StringType)
model_Process_expressionLanguage: Property = Property(name="expressionLanguage", type=StringType)
model_Process_suppressJoinFailure: Property = Property(name="suppressJoinFailure", type=StringType)
model_Process_variableAccessSerializable: Property = Property(name="variableAccessSerializable", type=StringType)
model_Process_abstractProcessProfile: Property = Property(name="abstractProcessProfile", type=StringType)
model_Process.attributes={model_Process_targetNamespace, model_Process_expressionLanguage, model_Process_queryLanguage, model_Process_abstractProcessProfile, model_Process_suppressJoinFailure, model_Process_name, model_Process_exitOnStandardFault, model_Process_variableAccessSerializable}

# BPELExtensibleElement class attributes and methods

# model_MessageExchanges class attributes and methods

# model_PartnerLinks class attributes and methods

# model_Variables class attributes and methods

# model_Activity class attributes and methods
model_Activity_name: Property = Property(name="name", type=StringType)
model_Activity_suppressJoinFailure: Property = Property(name="suppressJoinFailure", type=StringType)
model_Activity.attributes={model_Activity_name, model_Activity_suppressJoinFailure}

# model_FaultHandler class attributes and methods

# model_EventHandler class attributes and methods

# model_CorrelationSets class attributes and methods

# model_Import class attributes and methods
model_Import_namespace: Property = Property(name="namespace", type=StringType)
model_Import_location: Property = Property(name="location", type=StringType)
model_Import_importType: Property = Property(name="importType", type=StringType)
model_Import.attributes={model_Import_location, model_Import_namespace, model_Import_importType}

# model_Extensions class attributes and methods

# model_PartnerLink class attributes and methods
model_PartnerLink_name: Property = Property(name="name", type=StringType)
model_PartnerLink_initializePartnerRole: Property = Property(name="initializePartnerRole", type=StringType)
model_PartnerLink.attributes={model_PartnerLink_initializePartnerRole, model_PartnerLink_name}

# Role class attributes and methods

# PartnerLinkType class attributes and methods

# model_Catch class attributes and methods
model_Catch_faultName: Property = Property(name="faultName", type=StringType)
model_Catch.attributes={model_Catch_faultName}

# model_CatchAll class attributes and methods

# model_ToParts class attributes and methods

# model_Link class attributes and methods
model_Link_name: Property = Property(name="name", type=StringType)
model_Link.attributes={model_Link_name}

# model_Targets class attributes and methods

# model_Sources class attributes and methods

# model_CorrelationSet class attributes and methods
model_CorrelationSet_name: Property = Property(name="name", type=StringType)
model_CorrelationSet.attributes={model_CorrelationSet_name}

# Property class attributes and methods

# model_Invoke class attributes and methods

# PartnerActivity class attributes and methods

# model_Variable class attributes and methods
model_Variable_name: Property = Property(name="name", type=StringType)
model_Variable.attributes={model_Variable_name}

# model_CompensationHandler class attributes and methods

# model_FromParts class attributes and methods

# PortType class attributes and methods

# model_Source class attributes and methods

# model_Target class attributes and methods

# Message class attributes and methods

# XSDElementDeclaration class attributes and methods

# model_Reply class attributes and methods
model_Reply_faultName: Property = Property(name="faultName", type=StringType)
model_Reply.attributes={model_Reply_faultName}

# Activity class attributes and methods

# model_MessageExchange class attributes and methods
model_MessageExchange_name: Property = Property(name="name", type=StringType)
model_MessageExchange.attributes={model_MessageExchange_name}

# model_PartnerActivity class attributes and methods

# model_Pick class attributes and methods
model_Pick_createInstance: Property = Property(name="createInstance", type=StringType)
model_Pick.attributes={model_Pick_createInstance}

# model_Correlations class attributes and methods

# Operation class attributes and methods

# model_Receive class attributes and methods
model_Receive_createInstance: Property = Property(name="createInstance", type=StringType)
model_Receive.attributes={model_Receive_createInstance}

# model_Exit class attributes and methods

# model_Throw class attributes and methods
model_Throw_faultName: Property = Property(name="faultName", type=StringType)
model_Throw.attributes={model_Throw_faultName}

# model_Wait class attributes and methods

# model_Expression class attributes and methods
model_Expression_body: Property = Property(name="body", type=StringType)
model_Expression_expressionLanguage: Property = Property(name="expressionLanguage", type=StringType)
model_Expression_opaque: Property = Property(name="opaque", type=StringType)
model_Expression.attributes={model_Expression_opaque, model_Expression_body, model_Expression_expressionLanguage}

# model_Empty class attributes and methods

# model_Sequence class attributes and methods

# model_While class attributes and methods

# model_Condition class attributes and methods

# model_Extension class attributes and methods
model_Extension_namespace: Property = Property(name="namespace", type=StringType)
model_Extension_mustUnderstand: Property = Property(name="mustUnderstand", type=StringType)
model_Extension.attributes={model_Extension_namespace, model_Extension_mustUnderstand}

# model_OnMessage class attributes and methods

# model_OnAlarm class attributes and methods

# model_Flow class attributes and methods

# model_Links class attributes and methods

# model_CompletionCondition class attributes and methods

# model_Assign class attributes and methods
model_Assign_validate: Property = Property(name="validate", type=StringType)
model_Assign.attributes={model_Assign_validate}

# model_Copy class attributes and methods
model_Copy_keepSrcElementName: Property = Property(name="keepSrcElementName", type=StringType)
model_Copy_ignoreMissingFromData: Property = Property(name="ignoreMissingFromData", type=StringType)
model_Copy.attributes={model_Copy_keepSrcElementName, model_Copy_ignoreMissingFromData}

# model_To class attributes and methods

# model_From class attributes and methods
model_From_opaque: Property = Property(name="opaque", type=StringType)
model_From_endpointReference: Property = Property(name="endpointReference", type=StringType)
model_From_literal: Property = Property(name="literal", type=StringType)
model_From_unsafeLiteral: Property = Property(name="unsafeLiteral", type=StringType)
model_From.attributes={model_From_opaque, model_From_endpointReference, model_From_literal, model_From_unsafeLiteral}

# Part class attributes and methods

# model_Scope class attributes and methods
model_Scope_isolated: Property = Property(name="isolated", type=StringType)
model_Scope_exitOnStandardFault: Property = Property(name="exitOnStandardFault", type=StringType)
model_Scope.attributes={model_Scope_exitOnStandardFault, model_Scope_isolated}

# model_TerminationHandler class attributes and methods

# model_CompensateScope class attributes and methods

# model_AbstractAssignBound class attributes and methods

# model_Query class attributes and methods
model_Query_value: Property = Property(name="value", type=StringType)
model_Query_queryLanguage: Property = Property(name="queryLanguage", type=StringType)
model_Query.attributes={model_Query_queryLanguage, model_Query_value}

# AbstractAssignBound class attributes and methods

# model_ServiceRef class attributes and methods
model_ServiceRef_referenceScheme: Property = Property(name="referenceScheme", type=StringType)
model_ServiceRef_value: Property = Property(name="value", type=StringType)
model_ServiceRef.attributes={model_ServiceRef_value, model_ServiceRef_referenceScheme}

# XSDTypeDefinition class attributes and methods

# ExtensibilityElement class attributes and methods

# model_BooleanExpression class attributes and methods

# Expression class attributes and methods

# model_Correlation class attributes and methods
model_Correlation_initiate: Property = Property(name="initiate", type=StringType)
model_Correlation_pattern: Property = Property(name="pattern", type=StringType)
model_Correlation.attributes={model_Correlation_pattern, model_Correlation_initiate}

# model_OnEvent class attributes and methods

# model_UnknownExtensibilityAttribute class attributes and methods

# UnknownExtensibilityElement class attributes and methods

# model_Rethrow class attributes and methods

# WSDLElement class attributes and methods

# ExtensibleElement class attributes and methods

# model_ExtensionActivity class attributes and methods

# model_FromPart class attributes and methods

# model_ToPart class attributes and methods

# model_OpaqueActivity class attributes and methods

# model_ForEach class attributes and methods
model_ForEach_parallel: Property = Property(name="parallel", type=StringType)
model_ForEach.attributes={model_ForEach_parallel}

# model_RepeatUntil class attributes and methods

# model_Validate class attributes and methods

# model_If class attributes and methods

# model_ElseIf class attributes and methods

# model_Else class attributes and methods

# model_Branches class attributes and methods
model_Branches_countCompletedBranchesOnly: Property = Property(name="countCompletedBranchesOnly", type=StringType)
model_Branches.attributes={model_Branches_countCompletedBranchesOnly}

# model_BPELExtensibleElement class attributes and methods

# model_Documentation class attributes and methods
model_Documentation_lang: Property = Property(name="lang", type=StringType)
model_Documentation_source: Property = Property(name="source", type=StringType)
model_Documentation_value: Property = Property(name="value", type=StringType)
model_Documentation.attributes={model_Documentation_value, model_Documentation_source, model_Documentation_lang}

# model_Compensate class attributes and methods

# model_wsdl_WSDLElement class attributes and methods
model_wsdl_WSDLElement_documentationElement: Property = Property(name="documentationElement", type=StringType)
model_wsdl_WSDLElement_element: Property = Property(name="element", type=StringType)
model_wsdl_WSDLElement_m_getEnclosingDefinition: Method = Method(name="getEnclosingDefinition", parameters={}, type=StringType)
model_wsdl_WSDLElement_m_setEnclosingDefinition: Method = Method(name="setEnclosingDefinition", parameters={Parameter(name='definition')})
model_wsdl_WSDLElement.attributes={model_wsdl_WSDLElement_element, model_wsdl_WSDLElement_documentationElement}
model_wsdl_WSDLElement.methods={model_wsdl_WSDLElement_m_getEnclosingDefinition, model_wsdl_WSDLElement_m_setEnclosingDefinition}

# model_wsdl_PortType class attributes and methods
model_wsdl_PortType_qName: Property = Property(name="qName", type=StringType)
model_wsdl_PortType_undefined: Property = Property(name="undefined", type=BooleanType)
model_wsdl_PortType.attributes={model_wsdl_PortType_undefined, model_wsdl_PortType_qName}

# wsdl_ExtensibleElement class attributes and methods

# wsdl_IPortType class attributes and methods

# model_wsdl_Operation class attributes and methods
model_wsdl_Operation_style: Property = Property(name="style", type=StringType)
model_wsdl_Operation_name: Property = Property(name="name", type=StringType)
model_wsdl_Operation_undefined: Property = Property(name="undefined", type=BooleanType)
model_wsdl_Operation.attributes={model_wsdl_Operation_undefined, model_wsdl_Operation_style, model_wsdl_Operation_name}

# wsdl_IOperation class attributes and methods

# Input class attributes and methods

# Output class attributes and methods

# Fault class attributes and methods

# model_wsdl_Message class attributes and methods
model_wsdl_Message_qName: Property = Property(name="qName", type=StringType)
model_wsdl_Message_undefined: Property = Property(name="undefined", type=BooleanType)
model_wsdl_Message.attributes={model_wsdl_Message_qName, model_wsdl_Message_undefined}

# wsdl_IMessage class attributes and methods

# model_wsdl_Part class attributes and methods
model_wsdl_Part_name: Property = Property(name="name", type=StringType)
model_wsdl_Part_elementName: Property = Property(name="elementName", type=StringType)
model_wsdl_Part_typeName: Property = Property(name="typeName", type=StringType)
model_wsdl_Part.attributes={model_wsdl_Part_elementName, model_wsdl_Part_typeName, model_wsdl_Part_name}

# wsdl_IPart class attributes and methods

# model_wsdl_Binding class attributes and methods
model_wsdl_Binding_qName: Property = Property(name="qName", type=StringType)
model_wsdl_Binding_undefined: Property = Property(name="undefined", type=BooleanType)
model_wsdl_Binding.attributes={model_wsdl_Binding_undefined, model_wsdl_Binding_qName}

# wsdl_IBinding class attributes and methods

# model_wsdl_Definition class attributes and methods
model_wsdl_Definition_targetNamespace: Property = Property(name="targetNamespace", type=StringType)
model_wsdl_Definition_location: Property = Property(name="location", type=StringType)
model_wsdl_Definition_qName: Property = Property(name="qName", type=StringType)
model_wsdl_Definition_encoding: Property = Property(name="encoding", type=StringType)
model_wsdl_Definition_m_getDocument: Method = Method(name="getDocument", parameters={}, type=StringType)
model_wsdl_Definition_m_setDocument: Method = Method(name="setDocument", parameters={Parameter(name='document')})
model_wsdl_Definition.attributes={model_wsdl_Definition_encoding, model_wsdl_Definition_qName, model_wsdl_Definition_targetNamespace, model_wsdl_Definition_location}
model_wsdl_Definition.methods={model_wsdl_Definition_m_setDocument, model_wsdl_Definition_m_getDocument}

# BindingOperation class attributes and methods

# model_wsdl_BindingOperation class attributes and methods
model_wsdl_BindingOperation_name: Property = Property(name="name", type=StringType)
model_wsdl_BindingOperation.attributes={model_wsdl_BindingOperation_name}

# wsdl_IBindingOperation class attributes and methods

# BindingInput class attributes and methods

# BindingOutput class attributes and methods

# BindingFault class attributes and methods

# model_wsdl_Service class attributes and methods
model_wsdl_Service_qName: Property = Property(name="qName", type=StringType)
model_wsdl_Service_undefined: Property = Property(name="undefined", type=BooleanType)
model_wsdl_Service.attributes={model_wsdl_Service_qName, model_wsdl_Service_undefined}

# wsdl_IService class attributes and methods

# Port class attributes and methods

# model_wsdl_Port class attributes and methods
model_wsdl_Port_name: Property = Property(name="name", type=StringType)
model_wsdl_Port.attributes={model_wsdl_Port_name}

# wsdl_IPort class attributes and methods

# Binding class attributes and methods

# model_wsdl_ExtensibilityElement class attributes and methods
model_wsdl_ExtensibilityElement_required: Property = Property(name="required", type=BooleanType)
model_wsdl_ExtensibilityElement_elementType: Property = Property(name="elementType", type=StringType)
model_wsdl_ExtensibilityElement.attributes={model_wsdl_ExtensibilityElement_elementType, model_wsdl_ExtensibilityElement_required}

# wsdl_WSDLElement class attributes and methods

# wsdl_IExtensibilityElement class attributes and methods

# wsdl_IElementExtensible class attributes and methods

# wsdl_IAttributeExtensible class attributes and methods

# wsdl_IDefinition class attributes and methods

# model_wsdl_Input class attributes and methods

# wsdl_MessageReference class attributes and methods

# wsdl_IInput class attributes and methods

# Import class attributes and methods

# Types class attributes and methods

# Service class attributes and methods

# Namespace class attributes and methods

# model_wsdl_Import class attributes and methods
model_wsdl_Import_namespaceURI: Property = Property(name="namespaceURI", type=StringType)
model_wsdl_Import_locationURI: Property = Property(name="locationURI", type=StringType)
model_wsdl_Import_m_getSchema: Method = Method(name="getSchema", parameters={}, type=StringType)
model_wsdl_Import_m_setSchema: Method = Method(name="setSchema", parameters={Parameter(name='schema')})
model_wsdl_Import.attributes={model_wsdl_Import_namespaceURI, model_wsdl_Import_locationURI}
model_wsdl_Import.methods={model_wsdl_Import_m_setSchema, model_wsdl_Import_m_getSchema}

# wsdl_IImport class attributes and methods

# Definition class attributes and methods

# XSDSchema class attributes and methods

# model_wsdl_ExtensibleElement class attributes and methods

# model_wsdl_Namespace class attributes and methods
model_wsdl_Namespace_URI: Property = Property(name="URI", type=StringType)
model_wsdl_Namespace_prefix: Property = Property(name="prefix", type=StringType)
model_wsdl_Namespace.attributes={model_wsdl_Namespace_URI, model_wsdl_Namespace_prefix}

# model_wsdl_Output class attributes and methods

# wsdl_IOutput class attributes and methods

# model_wsdl_Fault class attributes and methods

# wsdl_IFault class attributes and methods

# model_wsdl_BindingInput class attributes and methods
model_wsdl_BindingInput_name: Property = Property(name="name", type=StringType)
model_wsdl_BindingInput_m_getInput: Method = Method(name="getInput", parameters={}, type=StringType)
model_wsdl_BindingInput_m_setInput: Method = Method(name="setInput", parameters={Parameter(name='input')})
model_wsdl_BindingInput.attributes={model_wsdl_BindingInput_name}
model_wsdl_BindingInput.methods={model_wsdl_BindingInput_m_setInput, model_wsdl_BindingInput_m_getInput}

# wsdl_IBindingInput class attributes and methods

# model_wsdl_BindingOutput class attributes and methods
model_wsdl_BindingOutput_name: Property = Property(name="name", type=StringType)
model_wsdl_BindingOutput_m_getOutput: Method = Method(name="getOutput", parameters={}, type=StringType)
model_wsdl_BindingOutput_m_setOutput: Method = Method(name="setOutput", parameters={Parameter(name='output')})
model_wsdl_BindingOutput.attributes={model_wsdl_BindingOutput_name}
model_wsdl_BindingOutput.methods={model_wsdl_BindingOutput_m_getOutput, model_wsdl_BindingOutput_m_setOutput}

# wsdl_IBindingOutput class attributes and methods

# model_wsdl_BindingFault class attributes and methods
model_wsdl_BindingFault_name: Property = Property(name="name", type=StringType)
model_wsdl_BindingFault_m_getFault: Method = Method(name="getFault", parameters={}, type=StringType)
model_wsdl_BindingFault_m_setFault: Method = Method(name="setFault", parameters={Parameter(name='fault')})
model_wsdl_BindingFault.attributes={model_wsdl_BindingFault_name}
model_wsdl_BindingFault.methods={model_wsdl_BindingFault_m_setFault, model_wsdl_BindingFault_m_getFault}

# wsdl_IBindingFault class attributes and methods

# model_wsdl_IMessage class attributes and methods
model_wsdl_IMessage_m_addPart: Method = Method(name="addPart", parameters={Parameter(name='part')})
model_wsdl_IMessage_m_getPart: Method = Method(name="getPart", parameters={Parameter(name='name')}, type=StringType)
model_wsdl_IMessage_m_getParts: Method = Method(name="getParts", parameters={}, type=StringType)
model_wsdl_IMessage_m_getOrderedParts: Method = Method(name="getOrderedParts", parameters={Parameter(name='partOrder')}, type=StringType)
model_wsdl_IMessage.methods={model_wsdl_IMessage_m_getPart, model_wsdl_IMessage_m_getOrderedParts, model_wsdl_IMessage_m_getParts, model_wsdl_IMessage_m_addPart}

# model_wsdl_IPortType class attributes and methods
model_wsdl_IPortType_m_addOperation: Method = Method(name="addOperation", parameters={Parameter(name='operation')})
model_wsdl_IPortType_m_getOperation: Method = Method(name="getOperation", parameters={Parameter(name='outputName'), Parameter(name='inputName'), Parameter(name='name')}, type=StringType)
model_wsdl_IPortType_m_getOperations: Method = Method(name="getOperations", parameters={}, type=StringType)
model_wsdl_IPortType.methods={model_wsdl_IPortType_m_addOperation, model_wsdl_IPortType_m_getOperations, model_wsdl_IPortType_m_getOperation}

# IAttributeExtensible class attributes and methods

# model_wsdl_IOperation class attributes and methods
model_wsdl_IOperation_m_addFault: Method = Method(name="addFault", parameters={Parameter(name='fault')})
model_wsdl_IOperation_m_getFault: Method = Method(name="getFault", parameters={Parameter(name='name')}, type=StringType)
model_wsdl_IOperation_m_getFaults: Method = Method(name="getFaults", parameters={}, type=StringType)
model_wsdl_IOperation_m_getParameterOrdering: Method = Method(name="getParameterOrdering", parameters={}, type=StringType)
model_wsdl_IOperation_m_setParameterOrdering: Method = Method(name="setParameterOrdering", parameters={Parameter(name='parameterOrder')})
model_wsdl_IOperation_m_getInput: Method = Method(name="getInput", parameters={}, type=StringType)
model_wsdl_IOperation_m_setInput: Method = Method(name="setInput", parameters={Parameter(name='input')})
model_wsdl_IOperation_m_getOutput: Method = Method(name="getOutput", parameters={}, type=StringType)
model_wsdl_IOperation_m_setOutput: Method = Method(name="setOutput", parameters={Parameter(name='output')})
model_wsdl_IOperation.methods={model_wsdl_IOperation_m_getInput, model_wsdl_IOperation_m_getFault, model_wsdl_IOperation_m_addFault, model_wsdl_IOperation_m_setInput, model_wsdl_IOperation_m_getOutput, model_wsdl_IOperation_m_getFaults, model_wsdl_IOperation_m_setOutput, model_wsdl_IOperation_m_getParameterOrdering, model_wsdl_IOperation_m_setParameterOrdering}

# IElementExtensible class attributes and methods

# model_wsdl_IInput class attributes and methods
model_wsdl_IInput_m_getMessage: Method = Method(name="getMessage", parameters={}, type=StringType)
model_wsdl_IInput_m_setMessage: Method = Method(name="setMessage", parameters={Parameter(name='message')})
model_wsdl_IInput.methods={model_wsdl_IInput_m_getMessage, model_wsdl_IInput_m_setMessage}

# model_wsdl_IOutput class attributes and methods
model_wsdl_IOutput_m_getMessage: Method = Method(name="getMessage", parameters={}, type=StringType)
model_wsdl_IOutput_m_setMessage: Method = Method(name="setMessage", parameters={Parameter(name='message')})
model_wsdl_IOutput.methods={model_wsdl_IOutput_m_setMessage, model_wsdl_IOutput_m_getMessage}

# model_wsdl_IFault class attributes and methods
model_wsdl_IFault_m_getMessage: Method = Method(name="getMessage", parameters={}, type=StringType)
model_wsdl_IFault_m_setMessage: Method = Method(name="setMessage", parameters={Parameter(name='message')})
model_wsdl_IFault.methods={model_wsdl_IFault_m_setMessage, model_wsdl_IFault_m_getMessage}

# model_wsdl_IBindingInput class attributes and methods

# model_wsdl_IPart class attributes and methods

# model_wsdl_IService class attributes and methods
model_wsdl_IService_m_addPort: Method = Method(name="addPort", parameters={Parameter(name='port')})
model_wsdl_IService_m_getPorts: Method = Method(name="getPorts", parameters={}, type=StringType)
model_wsdl_IService_m_getPort: Method = Method(name="getPort", parameters={Parameter(name='name')}, type=StringType)
model_wsdl_IService.methods={model_wsdl_IService_m_addPort, model_wsdl_IService_m_getPort, model_wsdl_IService_m_getPorts}

# model_wsdl_IPort class attributes and methods
model_wsdl_IPort_m_getBinding: Method = Method(name="getBinding", parameters={}, type=StringType)
model_wsdl_IPort_m_setBinding: Method = Method(name="setBinding", parameters={Parameter(name='binding')})
model_wsdl_IPort.methods={model_wsdl_IPort_m_setBinding, model_wsdl_IPort_m_getBinding}

# model_wsdl_IBinding class attributes and methods
model_wsdl_IBinding_m_addBindingOperation: Method = Method(name="addBindingOperation", parameters={Parameter(name='bindingOperation')})
model_wsdl_IBinding_m_getBindingOperation: Method = Method(name="getBindingOperation", parameters={Parameter(name='name'), Parameter(name='outputName'), Parameter(name='inputName')}, type=StringType)
model_wsdl_IBinding_m_getBindingOperations: Method = Method(name="getBindingOperations", parameters={}, type=StringType)
model_wsdl_IBinding_m_getPortType: Method = Method(name="getPortType", parameters={}, type=StringType)
model_wsdl_IBinding_m_setPortType: Method = Method(name="setPortType", parameters={Parameter(name='portType')})
model_wsdl_IBinding.methods={model_wsdl_IBinding_m_getBindingOperations, model_wsdl_IBinding_m_getPortType, model_wsdl_IBinding_m_setPortType, model_wsdl_IBinding_m_getBindingOperation, model_wsdl_IBinding_m_addBindingOperation}

# model_wsdl_IBindingOperation class attributes and methods
model_wsdl_IBindingOperation_m_setOperation: Method = Method(name="setOperation", parameters={Parameter(name='operation')})
model_wsdl_IBindingOperation_m_getBindingInput: Method = Method(name="getBindingInput", parameters={}, type=StringType)
model_wsdl_IBindingOperation_m_setBindingInput: Method = Method(name="setBindingInput", parameters={Parameter(name='bindingInput')})
model_wsdl_IBindingOperation_m_getBindingOutput: Method = Method(name="getBindingOutput", parameters={}, type=StringType)
model_wsdl_IBindingOperation_m_setBindingOutput: Method = Method(name="setBindingOutput", parameters={Parameter(name='bindingOutput')})
model_wsdl_IBindingOperation_m_addBindingFault: Method = Method(name="addBindingFault", parameters={Parameter(name='bindingFault')})
model_wsdl_IBindingOperation_m_getBindingFault: Method = Method(name="getBindingFault", parameters={Parameter(name='name')}, type=StringType)
model_wsdl_IBindingOperation_m_getBindingFaults: Method = Method(name="getBindingFaults", parameters={}, type=StringType)
model_wsdl_IBindingOperation_m_getOperation: Method = Method(name="getOperation", parameters={}, type=StringType)
model_wsdl_IBindingOperation.methods={model_wsdl_IBindingOperation_m_getBindingOutput, model_wsdl_IBindingOperation_m_setBindingInput, model_wsdl_IBindingOperation_m_getBindingFault, model_wsdl_IBindingOperation_m_setOperation, model_wsdl_IBindingOperation_m_getBindingInput, model_wsdl_IBindingOperation_m_getOperation, model_wsdl_IBindingOperation_m_addBindingFault, model_wsdl_IBindingOperation_m_setBindingOutput, model_wsdl_IBindingOperation_m_getBindingFaults}

# model_wsdl_IBindingOutput class attributes and methods

# model_wsdl_IBindingFault class attributes and methods

# model_wsdl_IExtensibilityElement class attributes and methods

# model_wsdl_IDefinition class attributes and methods
model_wsdl_IDefinition_m_addBinding: Method = Method(name="addBinding", parameters={Parameter(name='binding')})
model_wsdl_IDefinition_m_addImport: Method = Method(name="addImport", parameters={Parameter(name='importDef')})
model_wsdl_IDefinition_m_addMessage: Method = Method(name="addMessage", parameters={Parameter(name='message')})
model_wsdl_IDefinition_m_addNamespace: Method = Method(name="addNamespace", parameters={Parameter(name='prefix'), Parameter(name='namespaceURI')})
model_wsdl_IDefinition_m_addPortType: Method = Method(name="addPortType", parameters={Parameter(name='portType')})
model_wsdl_IDefinition_m_addService: Method = Method(name="addService", parameters={Parameter(name='service')})
model_wsdl_IDefinition_m_createBindingFault: Method = Method(name="createBindingFault", parameters={}, type=StringType)
model_wsdl_IDefinition_m_createBindingInput: Method = Method(name="createBindingInput", parameters={}, type=StringType)
model_wsdl_IDefinition_m_createBindingOutput: Method = Method(name="createBindingOutput", parameters={}, type=StringType)
model_wsdl_IDefinition_m_createBindingOperation: Method = Method(name="createBindingOperation", parameters={}, type=StringType)
model_wsdl_IDefinition_m_createBinding: Method = Method(name="createBinding", parameters={}, type=StringType)
model_wsdl_IDefinition_m_createFault: Method = Method(name="createFault", parameters={}, type=StringType)
model_wsdl_IDefinition_m_getServices: Method = Method(name="getServices", parameters={}, type=StringType)
model_wsdl_IDefinition_m_getExtensionRegistry: Method = Method(name="getExtensionRegistry", parameters={}, type=StringType)
model_wsdl_IDefinition_m_createImport: Method = Method(name="createImport", parameters={}, type=StringType)
model_wsdl_IDefinition_m_createInput: Method = Method(name="createInput", parameters={}, type=StringType)
model_wsdl_IDefinition_m_createMessage: Method = Method(name="createMessage", parameters={}, type=StringType)
model_wsdl_IDefinition_m_createOperation: Method = Method(name="createOperation", parameters={}, type=StringType)
model_wsdl_IDefinition_m_createOutput: Method = Method(name="createOutput", parameters={}, type=StringType)
model_wsdl_IDefinition_m_createPart: Method = Method(name="createPart", parameters={}, type=StringType)
model_wsdl_IDefinition_m_createPort: Method = Method(name="createPort", parameters={}, type=StringType)
model_wsdl_IDefinition_m_createPortType: Method = Method(name="createPortType", parameters={}, type=StringType)
model_wsdl_IDefinition_m_createService: Method = Method(name="createService", parameters={}, type=StringType)
model_wsdl_IDefinition_m_getBinding: Method = Method(name="getBinding", parameters={Parameter(name='name')}, type=StringType)
model_wsdl_IDefinition_m_getBindings: Method = Method(name="getBindings", parameters={}, type=StringType)
model_wsdl_IDefinition_m_getImports: Method = Method(name="getImports", parameters={}, type=StringType)
model_wsdl_IDefinition_m_getImports: Method = Method(name="getImports", parameters={Parameter(name='namespaceURI')}, type=StringType)
model_wsdl_IDefinition_m_getMessage: Method = Method(name="getMessage", parameters={Parameter(name='name')}, type=StringType)
model_wsdl_IDefinition_m_getMessages: Method = Method(name="getMessages", parameters={}, type=StringType)
model_wsdl_IDefinition_m_getNamespace: Method = Method(name="getNamespace", parameters={Parameter(name='prefix')}, type=StringType)
model_wsdl_IDefinition_m_getNamespaces: Method = Method(name="getNamespaces", parameters={}, type=StringType)
model_wsdl_IDefinition_m_getPortType: Method = Method(name="getPortType", parameters={Parameter(name='name')}, type=StringType)
model_wsdl_IDefinition_m_getPortTypes: Method = Method(name="getPortTypes", parameters={}, type=StringType)
model_wsdl_IDefinition_m_getPrefix: Method = Method(name="getPrefix", parameters={Parameter(name='namespaceURI')}, type=StringType)
model_wsdl_IDefinition_m_getService: Method = Method(name="getService", parameters={Parameter(name='name')}, type=StringType)
model_wsdl_IDefinition_m_setExtensionRegistry: Method = Method(name="setExtensionRegistry", parameters={Parameter(name='extensionRegistry')})
model_wsdl_IDefinition_m_getDocumentBaseURI: Method = Method(name="getDocumentBaseURI", parameters={}, type=StringType)
model_wsdl_IDefinition_m_setDocumentBaseURI: Method = Method(name="setDocumentBaseURI", parameters={Parameter(name='documentBase')})
model_wsdl_IDefinition_m_createTypes: Method = Method(name="createTypes", parameters={}, type=StringType)
model_wsdl_IDefinition_m_removeService: Method = Method(name="removeService", parameters={Parameter(name='name')}, type=StringType)
model_wsdl_IDefinition_m_removeBinding: Method = Method(name="removeBinding", parameters={Parameter(name='name')}, type=StringType)
model_wsdl_IDefinition_m_removePortType: Method = Method(name="removePortType", parameters={Parameter(name='name')}, type=StringType)
model_wsdl_IDefinition_m_removeMessage: Method = Method(name="removeMessage", parameters={Parameter(name='name')}, type=StringType)
model_wsdl_IDefinition_m_getTypes: Method = Method(name="getTypes", parameters={}, type=StringType)
model_wsdl_IDefinition_m_setTypes: Method = Method(name="setTypes", parameters={Parameter(name='types')})
model_wsdl_IDefinition.methods={model_wsdl_IDefinition_m_removePortType, model_wsdl_IDefinition_m_addBinding, model_wsdl_IDefinition_m_getImports, model_wsdl_IDefinition_m_getBindings, model_wsdl_IDefinition_m_addImport, model_wsdl_IDefinition_m_createBindingOutput, model_wsdl_IDefinition_m_removeMessage, model_wsdl_IDefinition_m_addService, model_wsdl_IDefinition_m_createOperation, model_wsdl_IDefinition_m_removeBinding, model_wsdl_IDefinition_m_getNamespaces, model_wsdl_IDefinition_m_addNamespace, model_wsdl_IDefinition_m_createPortType, model_wsdl_IDefinition_m_createImport, model_wsdl_IDefinition_m_createTypes, model_wsdl_IDefinition_m_getPrefix, model_wsdl_IDefinition_m_getDocumentBaseURI, model_wsdl_IDefinition_m_addMessage, model_wsdl_IDefinition_m_createPort, model_wsdl_IDefinition_m_getNamespace, model_wsdl_IDefinition_m_getMessages, model_wsdl_IDefinition_m_addPortType, model_wsdl_IDefinition_m_getPortTypes, model_wsdl_IDefinition_m_createService, model_wsdl_IDefinition_m_createMessage, model_wsdl_IDefinition_m_getMessage, model_wsdl_IDefinition_m_createBindingInput, model_wsdl_IDefinition_m_getImports, model_wsdl_IDefinition_m_getTypes, model_wsdl_IDefinition_m_createBinding, model_wsdl_IDefinition_m_createInput, model_wsdl_IDefinition_m_setExtensionRegistry, model_wsdl_IDefinition_m_createBindingFault, model_wsdl_IDefinition_m_getPortType, model_wsdl_IDefinition_m_createPart, model_wsdl_IDefinition_m_removeService, model_wsdl_IDefinition_m_setDocumentBaseURI, model_wsdl_IDefinition_m_getService, model_wsdl_IDefinition_m_createFault, model_wsdl_IDefinition_m_createBindingOperation, model_wsdl_IDefinition_m_setTypes, model_wsdl_IDefinition_m_getBinding, model_wsdl_IDefinition_m_createOutput, model_wsdl_IDefinition_m_getExtensionRegistry, model_wsdl_IDefinition_m_getServices}

# model_wsdl_UnknownExtensibilityElement class attributes and methods

# model_wsdl_XSDSchemaExtensibilityElement class attributes and methods
model_wsdl_XSDSchemaExtensibilityElement_documentBaseURI: Property = Property(name="documentBaseURI", type=StringType)
model_wsdl_XSDSchemaExtensibilityElement.attributes={model_wsdl_XSDSchemaExtensibilityElement_documentBaseURI}

# wsdl_ExtensibilityElement class attributes and methods

# wsdl_ISchema class attributes and methods

# model_wsdl_IImport class attributes and methods

# model_wsdl_IList class attributes and methods

# model_wsdl_IMap class attributes and methods

# model_wsdl_IURL class attributes and methods

# model_wsdl_IExtensionRegistry class attributes and methods

# model_wsdl_Types class attributes and methods
model_wsdl_Types_m_getSchemas: Method = Method(name="getSchemas", parameters={}, type=StringType)
model_wsdl_Types_m_getSchemas: Method = Method(name="getSchemas", parameters={Parameter(name='namespaceURI')}, type=StringType)
model_wsdl_Types.methods={model_wsdl_Types_m_getSchemas, model_wsdl_Types_m_getSchemas}

# wsdl_ITypes class attributes and methods

# model_wsdl_IIterator class attributes and methods

# model_wsdl_ITypes class attributes and methods

# XSDSimpleTypeDefinition class attributes and methods

# XSDAttributeDeclaration class attributes and methods

# model_wsdl_MessageReference class attributes and methods
model_wsdl_MessageReference_name: Property = Property(name="name", type=StringType)
model_wsdl_MessageReference.attributes={model_wsdl_MessageReference_name}

# model_wsdl_IElementExtensible class attributes and methods
model_wsdl_IElementExtensible_m_getExtensibilityElements: Method = Method(name="getExtensibilityElements", parameters={}, type=StringType)
model_wsdl_IElementExtensible_m_addExtensibilityElement: Method = Method(name="addExtensibilityElement", parameters={Parameter(name='extElement')})
model_wsdl_IElementExtensible.methods={model_wsdl_IElementExtensible_m_addExtensibilityElement, model_wsdl_IElementExtensible_m_getExtensibilityElements}

# model_wsdl_IAttributeExtensible class attributes and methods
model_wsdl_IAttributeExtensible_m_getExtensionAttribute: Method = Method(name="getExtensionAttribute", parameters={Parameter(name='name')}, type=StringType)
model_wsdl_IAttributeExtensible_m_setExtensionAttribute: Method = Method(name="setExtensionAttribute", parameters={Parameter(name='name'), Parameter(name='value')})
model_wsdl_IAttributeExtensible_m_getExtensionAttributes: Method = Method(name="getExtensionAttributes", parameters={}, type=StringType)
model_wsdl_IAttributeExtensible_m_getNativeAttributeNames: Method = Method(name="getNativeAttributeNames", parameters={}, type=StringType)
model_wsdl_IAttributeExtensible.methods={model_wsdl_IAttributeExtensible_m_getNativeAttributeNames, model_wsdl_IAttributeExtensible_m_getExtensionAttribute, model_wsdl_IAttributeExtensible_m_setExtensionAttribute, model_wsdl_IAttributeExtensible_m_getExtensionAttributes}

# model_wsdl_IObject class attributes and methods

# model_wsdl_ISchema class attributes and methods

# IExtensibilityElement class attributes and methods

# model_xsd_XSDAnnotation class attributes and methods
model_xsd_XSDAnnotation_applicationInformation: Property = Property(name="applicationInformation", type=StringType)
model_xsd_XSDAnnotation_userInformation: Property = Property(name="userInformation", type=StringType)
model_xsd_XSDAnnotation_attributes: Property = Property(name="attributes", type=StringType)
model_xsd_XSDAnnotation.attributes={model_xsd_XSDAnnotation_userInformation, model_xsd_XSDAnnotation_attributes, model_xsd_XSDAnnotation_applicationInformation}

# xsd_XSDComponent class attributes and methods

# xsd_XSDRedefineContent class attributes and methods

# model_xsd_XSDAttributeDeclaration class attributes and methods
model_xsd_XSDAttributeDeclaration_attributeDeclarationReference: Property = Property(name="attributeDeclarationReference", type=BooleanType)
model_xsd_XSDAttributeDeclaration.attributes={model_xsd_XSDAttributeDeclaration_attributeDeclarationReference}

# xsd_XSDFeature class attributes and methods

# xsd_XSDSchemaContent class attributes and methods

# XSDAnnotation class attributes and methods

# XSDFundamentalFacet class attributes and methods

# model_xsd_XSDCardinalityFacet class attributes and methods
model_xsd_XSDCardinalityFacet_value: Property = Property(name="value", type=StringType)
model_xsd_XSDCardinalityFacet.attributes={model_xsd_XSDCardinalityFacet_value}

# model_xsd_XSDComplexTypeContent class attributes and methods

# XSDComponent class attributes and methods

# model_xsd_XSDComplexTypeDefinition class attributes and methods
model_xsd_XSDComplexTypeDefinition_derivationMethod: Property = Property(name="derivationMethod", type=StringType)
model_xsd_XSDComplexTypeDefinition_final: Property = Property(name="final", type=StringType)
model_xsd_XSDComplexTypeDefinition_abstract: Property = Property(name="abstract", type=BooleanType)
model_xsd_XSDComplexTypeDefinition_contentTypeCategory: Property = Property(name="contentTypeCategory", type=StringType)
model_xsd_XSDComplexTypeDefinition_prohibitedSubstitutions: Property = Property(name="prohibitedSubstitutions", type=StringType)
model_xsd_XSDComplexTypeDefinition_lexicalFinal: Property = Property(name="lexicalFinal", type=StringType)
model_xsd_XSDComplexTypeDefinition_block: Property = Property(name="block", type=StringType)
model_xsd_XSDComplexTypeDefinition_mixed: Property = Property(name="mixed", type=BooleanType)
model_xsd_XSDComplexTypeDefinition.attributes={model_xsd_XSDComplexTypeDefinition_derivationMethod, model_xsd_XSDComplexTypeDefinition_contentTypeCategory, model_xsd_XSDComplexTypeDefinition_prohibitedSubstitutions, model_xsd_XSDComplexTypeDefinition_lexicalFinal, model_xsd_XSDComplexTypeDefinition_final, model_xsd_XSDComplexTypeDefinition_abstract, model_xsd_XSDComplexTypeDefinition_mixed, model_xsd_XSDComplexTypeDefinition_block}

# xsd_XSDTypeDefinition class attributes and methods

# model_xsd_XSDAttributeGroupContent class attributes and methods

# XSDConcreteComponent class attributes and methods

# model_xsd_XSDAttributeGroupDefinition class attributes and methods
model_xsd_XSDAttributeGroupDefinition_attributeGroupDefinitionReference: Property = Property(name="attributeGroupDefinitionReference", type=BooleanType)
model_xsd_XSDAttributeGroupDefinition.attributes={model_xsd_XSDAttributeGroupDefinition_attributeGroupDefinitionReference}

# xsd_XSDRedefinableComponent class attributes and methods

# xsd_XSDAttributeGroupContent class attributes and methods

# XSDAttributeGroupContent class attributes and methods

# XSDAttributeUse class attributes and methods

# XSDWildcard class attributes and methods

# XSDAttributeGroupDefinition class attributes and methods

# model_xsd_XSDAttributeUse class attributes and methods
model_xsd_XSDAttributeUse_required: Property = Property(name="required", type=BooleanType)
model_xsd_XSDAttributeUse_value: Property = Property(name="value", type=StringType)
model_xsd_XSDAttributeUse_constraint: Property = Property(name="constraint", type=StringType)
model_xsd_XSDAttributeUse_use: Property = Property(name="use", type=StringType)
model_xsd_XSDAttributeUse_lexicalValue: Property = Property(name="lexicalValue", type=StringType)
model_xsd_XSDAttributeUse.attributes={model_xsd_XSDAttributeUse_required, model_xsd_XSDAttributeUse_use, model_xsd_XSDAttributeUse_constraint, model_xsd_XSDAttributeUse_value, model_xsd_XSDAttributeUse_lexicalValue}

# model_xsd_XSDBoundedFacet class attributes and methods
model_xsd_XSDBoundedFacet_value: Property = Property(name="value", type=BooleanType)
model_xsd_XSDBoundedFacet.attributes={model_xsd_XSDBoundedFacet_value}

# XSDParticle class attributes and methods

# xsd_XSDScope class attributes and methods

# XSDComplexTypeContent class attributes and methods

# xsd_XSDTerm class attributes and methods

# model_xsd_XSDComponent class attributes and methods

# model_xsd_XSDConcreteComponent class attributes and methods
model_xsd_XSDConcreteComponent_element: Property = Property(name="element", type=StringType)
model_xsd_XSDConcreteComponent.attributes={model_xsd_XSDConcreteComponent_element}

# XSDDiagnostic class attributes and methods

# model_xsd_XSDConstrainingFacet class attributes and methods

# XSDFacet class attributes and methods

# model_xsd_XSDDiagnostic class attributes and methods
model_xsd_XSDDiagnostic_severity: Property = Property(name="severity", type=StringType)
model_xsd_XSDDiagnostic_message: Property = Property(name="message", type=StringType)
model_xsd_XSDDiagnostic_locationURI: Property = Property(name="locationURI", type=StringType)
model_xsd_XSDDiagnostic_line: Property = Property(name="line", type=IntegerType)
model_xsd_XSDDiagnostic_column: Property = Property(name="column", type=IntegerType)
model_xsd_XSDDiagnostic_node: Property = Property(name="node", type=StringType)
model_xsd_XSDDiagnostic_annotationURI: Property = Property(name="annotationURI", type=StringType)
model_xsd_XSDDiagnostic_key: Property = Property(name="key", type=StringType)
model_xsd_XSDDiagnostic_substitutions: Property = Property(name="substitutions", type=StringType)
model_xsd_XSDDiagnostic.attributes={model_xsd_XSDDiagnostic_line, model_xsd_XSDDiagnostic_message, model_xsd_XSDDiagnostic_severity, model_xsd_XSDDiagnostic_key, model_xsd_XSDDiagnostic_column, model_xsd_XSDDiagnostic_annotationURI, model_xsd_XSDDiagnostic_locationURI, model_xsd_XSDDiagnostic_substitutions, model_xsd_XSDDiagnostic_node}

# model_xsd_XSDElementDeclaration class attributes and methods
model_xsd_XSDElementDeclaration_nillable: Property = Property(name="nillable", type=BooleanType)
model_xsd_XSDElementDeclaration_disallowedSubstitutions: Property = Property(name="disallowedSubstitutions", type=StringType)
model_xsd_XSDElementDeclaration_substitutionGroupExclusions: Property = Property(name="substitutionGroupExclusions", type=StringType)
model_xsd_XSDElementDeclaration_abstract: Property = Property(name="abstract", type=BooleanType)
model_xsd_XSDElementDeclaration_lexicalFinal: Property = Property(name="lexicalFinal", type=StringType)
model_xsd_XSDElementDeclaration_block: Property = Property(name="block", type=StringType)
model_xsd_XSDElementDeclaration_elementDeclarationReference: Property = Property(name="elementDeclarationReference", type=BooleanType)
model_xsd_XSDElementDeclaration_circular: Property = Property(name="circular", type=BooleanType)
model_xsd_XSDElementDeclaration.attributes={model_xsd_XSDElementDeclaration_lexicalFinal, model_xsd_XSDElementDeclaration_block, model_xsd_XSDElementDeclaration_substitutionGroupExclusions, model_xsd_XSDElementDeclaration_nillable, model_xsd_XSDElementDeclaration_elementDeclarationReference, model_xsd_XSDElementDeclaration_circular, model_xsd_XSDElementDeclaration_disallowedSubstitutions, model_xsd_XSDElementDeclaration_abstract}

# XSDIdentityConstraintDefinition class attributes and methods

# model_xsd_XSDEnumerationFacet class attributes and methods
model_xsd_XSDEnumerationFacet_value: Property = Property(name="value", type=StringType)
model_xsd_XSDEnumerationFacet.attributes={model_xsd_XSDEnumerationFacet_value}

# XSDRepeatableFacet class attributes and methods

# model_xsd_XSDFacet class attributes and methods
model_xsd_XSDFacet_lexicalValue: Property = Property(name="lexicalValue", type=StringType)
model_xsd_XSDFacet_facetName: Property = Property(name="facetName", type=StringType)
model_xsd_XSDFacet_effectiveValue: Property = Property(name="effectiveValue", type=StringType)
model_xsd_XSDFacet.attributes={model_xsd_XSDFacet_facetName, model_xsd_XSDFacet_effectiveValue, model_xsd_XSDFacet_lexicalValue}

# model_xsd_XSDFeature class attributes and methods
model_xsd_XSDFeature_value: Property = Property(name="value", type=StringType)
model_xsd_XSDFeature_constraint: Property = Property(name="constraint", type=StringType)
model_xsd_XSDFeature_form: Property = Property(name="form", type=StringType)
model_xsd_XSDFeature_lexicalValue: Property = Property(name="lexicalValue", type=StringType)
model_xsd_XSDFeature_global: Property = Property(name="global", type=BooleanType)
model_xsd_XSDFeature_featureReference: Property = Property(name="featureReference", type=BooleanType)
model_xsd_XSDFeature.attributes={model_xsd_XSDFeature_form, model_xsd_XSDFeature_featureReference, model_xsd_XSDFeature_global, model_xsd_XSDFeature_constraint, model_xsd_XSDFeature_value, model_xsd_XSDFeature_lexicalValue}

# XSDNamedComponent class attributes and methods

# model_xsd_XSDMaxExclusiveFacet class attributes and methods

# XSDMaxFacet class attributes and methods

# model_xsd_XSDMaxFacet class attributes and methods
model_xsd_XSDMaxFacet_value: Property = Property(name="value", type=StringType)
model_xsd_XSDMaxFacet_inclusive: Property = Property(name="inclusive", type=BooleanType)
model_xsd_XSDMaxFacet_exclusive: Property = Property(name="exclusive", type=BooleanType)
model_xsd_XSDMaxFacet.attributes={model_xsd_XSDMaxFacet_exclusive, model_xsd_XSDMaxFacet_value, model_xsd_XSDMaxFacet_inclusive}

# XSDScope class attributes and methods

# XSDFeature class attributes and methods

# model_xsd_XSDFixedFacet class attributes and methods
model_xsd_XSDFixedFacet_fixed: Property = Property(name="fixed", type=BooleanType)
model_xsd_XSDFixedFacet.attributes={model_xsd_XSDFixedFacet_fixed}

# XSDConstrainingFacet class attributes and methods

# model_xsd_XSDFractionDigitsFacet class attributes and methods
model_xsd_XSDFractionDigitsFacet_value: Property = Property(name="value", type=IntegerType)
model_xsd_XSDFractionDigitsFacet.attributes={model_xsd_XSDFractionDigitsFacet_value}

# XSDFixedFacet class attributes and methods

# model_xsd_XSDFundamentalFacet class attributes and methods

# model_xsd_XSDIdentityConstraintDefinition class attributes and methods
model_xsd_XSDIdentityConstraintDefinition_identityConstraintCategory: Property = Property(name="identityConstraintCategory", type=StringType)
model_xsd_XSDIdentityConstraintDefinition.attributes={model_xsd_XSDIdentityConstraintDefinition_identityConstraintCategory}

# XSDXPathDefinition class attributes and methods

# model_xsd_XSDImport class attributes and methods
model_xsd_XSDImport_namespace: Property = Property(name="namespace", type=StringType)
model_xsd_XSDImport.attributes={model_xsd_XSDImport_namespace}

# XSDSchemaDirective class attributes and methods

# model_xsd_XSDInclude class attributes and methods

# XSDSchemaCompositor class attributes and methods

# model_xsd_XSDLengthFacet class attributes and methods
model_xsd_XSDLengthFacet_value: Property = Property(name="value", type=IntegerType)
model_xsd_XSDLengthFacet.attributes={model_xsd_XSDLengthFacet_value}

# model_xsd_XSDNotationDeclaration class attributes and methods
model_xsd_XSDNotationDeclaration_systemIdentifier: Property = Property(name="systemIdentifier", type=StringType)
model_xsd_XSDNotationDeclaration_publicIdentifier: Property = Property(name="publicIdentifier", type=StringType)
model_xsd_XSDNotationDeclaration.attributes={model_xsd_XSDNotationDeclaration_publicIdentifier, model_xsd_XSDNotationDeclaration_systemIdentifier}

# xsd_XSDNamedComponent class attributes and methods

# model_xsd_XSDMaxInclusiveFacet class attributes and methods

# model_xsd_XSDMaxLengthFacet class attributes and methods
model_xsd_XSDMaxLengthFacet_value: Property = Property(name="value", type=IntegerType)
model_xsd_XSDMaxLengthFacet.attributes={model_xsd_XSDMaxLengthFacet_value}

# model_xsd_XSDMinExclusiveFacet class attributes and methods

# XSDMinFacet class attributes and methods

# model_xsd_XSDMinFacet class attributes and methods
model_xsd_XSDMinFacet_value: Property = Property(name="value", type=StringType)
model_xsd_XSDMinFacet_inclusive: Property = Property(name="inclusive", type=BooleanType)
model_xsd_XSDMinFacet_exclusive: Property = Property(name="exclusive", type=BooleanType)
model_xsd_XSDMinFacet.attributes={model_xsd_XSDMinFacet_value, model_xsd_XSDMinFacet_inclusive, model_xsd_XSDMinFacet_exclusive}

# model_xsd_XSDMinInclusiveFacet class attributes and methods

# model_xsd_XSDMinLengthFacet class attributes and methods
model_xsd_XSDMinLengthFacet_value: Property = Property(name="value", type=IntegerType)
model_xsd_XSDMinLengthFacet.attributes={model_xsd_XSDMinLengthFacet_value}

# model_xsd_XSDModelGroup class attributes and methods
model_xsd_XSDModelGroup_compositor: Property = Property(name="compositor", type=StringType)
model_xsd_XSDModelGroup.attributes={model_xsd_XSDModelGroup_compositor}

# XSDTerm class attributes and methods

# model_xsd_XSDModelGroupDefinition class attributes and methods
model_xsd_XSDModelGroupDefinition_modelGroupDefinitionReference: Property = Property(name="modelGroupDefinitionReference", type=BooleanType)
model_xsd_XSDModelGroupDefinition.attributes={model_xsd_XSDModelGroupDefinition_modelGroupDefinitionReference}

# xsd_XSDParticleContent class attributes and methods

# XSDModelGroup class attributes and methods

# XSDModelGroupDefinition class attributes and methods

# model_xsd_XSDNamedComponent class attributes and methods
model_xsd_XSDNamedComponent_targetNamespace: Property = Property(name="targetNamespace", type=StringType)
model_xsd_XSDNamedComponent_aliasName: Property = Property(name="aliasName", type=StringType)
model_xsd_XSDNamedComponent_uRI: Property = Property(name="uRI", type=StringType)
model_xsd_XSDNamedComponent_aliasURI: Property = Property(name="aliasURI", type=StringType)
model_xsd_XSDNamedComponent_qName: Property = Property(name="qName", type=StringType)
model_xsd_XSDNamedComponent_name: Property = Property(name="name", type=StringType)
model_xsd_XSDNamedComponent.attributes={model_xsd_XSDNamedComponent_aliasURI, model_xsd_XSDNamedComponent_targetNamespace, model_xsd_XSDNamedComponent_name, model_xsd_XSDNamedComponent_aliasName, model_xsd_XSDNamedComponent_uRI, model_xsd_XSDNamedComponent_qName}

# model_xsd_XSDSchema class attributes and methods
model_xsd_XSDSchema_document: Property = Property(name="document", type=StringType)
model_xsd_XSDSchema_schemaLocation: Property = Property(name="schemaLocation", type=StringType)
model_xsd_XSDSchema_targetNamespace: Property = Property(name="targetNamespace", type=StringType)
model_xsd_XSDSchema_attributeFormDefault: Property = Property(name="attributeFormDefault", type=StringType)
model_xsd_XSDSchema_elementFormDefault: Property = Property(name="elementFormDefault", type=StringType)
model_xsd_XSDSchema_finalDefault: Property = Property(name="finalDefault", type=StringType)
model_xsd_XSDSchema_blockDefault: Property = Property(name="blockDefault", type=StringType)
model_xsd_XSDSchema_version: Property = Property(name="version", type=StringType)
model_xsd_XSDSchema.attributes={model_xsd_XSDSchema_version, model_xsd_XSDSchema_blockDefault, model_xsd_XSDSchema_targetNamespace, model_xsd_XSDSchema_finalDefault, model_xsd_XSDSchema_elementFormDefault, model_xsd_XSDSchema_document, model_xsd_XSDSchema_attributeFormDefault, model_xsd_XSDSchema_schemaLocation}

# model_xsd_XSDNumericFacet class attributes and methods
model_xsd_XSDNumericFacet_value: Property = Property(name="value", type=BooleanType)
model_xsd_XSDNumericFacet.attributes={model_xsd_XSDNumericFacet_value}

# model_xsd_XSDOrderedFacet class attributes and methods
model_xsd_XSDOrderedFacet_value: Property = Property(name="value", type=StringType)
model_xsd_XSDOrderedFacet.attributes={model_xsd_XSDOrderedFacet_value}

# model_xsd_XSDParticle class attributes and methods
model_xsd_XSDParticle_minOccurs: Property = Property(name="minOccurs", type=IntegerType)
model_xsd_XSDParticle_maxOccurs: Property = Property(name="maxOccurs", type=IntegerType)
model_xsd_XSDParticle.attributes={model_xsd_XSDParticle_maxOccurs, model_xsd_XSDParticle_minOccurs}

# XSDParticleContent class attributes and methods

# model_xsd_XSDParticleContent class attributes and methods

# model_xsd_XSDPatternFacet class attributes and methods
model_xsd_XSDPatternFacet_value: Property = Property(name="value", type=StringType)
model_xsd_XSDPatternFacet.attributes={model_xsd_XSDPatternFacet_value}

# model_xsd_XSDRedefinableComponent class attributes and methods
model_xsd_XSDRedefinableComponent_circular: Property = Property(name="circular", type=BooleanType)
model_xsd_XSDRedefinableComponent.attributes={model_xsd_XSDRedefinableComponent_circular}

# model_xsd_XSDRedefineContent class attributes and methods

# XSDSchemaContent class attributes and methods

# model_xsd_XSDRedefine class attributes and methods

# XSDRedefineContent class attributes and methods

# model_xsd_XSDRepeatableFacet class attributes and methods

# XSDNotationDeclaration class attributes and methods

# model_xsd_XSDSchemaCompositor class attributes and methods

# model_xsd_XSDSchemaContent class attributes and methods

# model_xsd_XSDSchemaDirective class attributes and methods
model_xsd_XSDSchemaDirective_schemaLocation: Property = Property(name="schemaLocation", type=StringType)
model_xsd_XSDSchemaDirective.attributes={model_xsd_XSDSchemaDirective_schemaLocation}

# model_xsd_XSDScope class attributes and methods

# model_xsd_XSDSimpleTypeDefinition class attributes and methods
model_xsd_XSDSimpleTypeDefinition_variety: Property = Property(name="variety", type=StringType)
model_xsd_XSDSimpleTypeDefinition_final: Property = Property(name="final", type=StringType)
model_xsd_XSDSimpleTypeDefinition_lexicalFinal: Property = Property(name="lexicalFinal", type=StringType)
model_xsd_XSDSimpleTypeDefinition_validFacets: Property = Property(name="validFacets", type=StringType)
model_xsd_XSDSimpleTypeDefinition.attributes={model_xsd_XSDSimpleTypeDefinition_final, model_xsd_XSDSimpleTypeDefinition_variety, model_xsd_XSDSimpleTypeDefinition_validFacets, model_xsd_XSDSimpleTypeDefinition_lexicalFinal}

# xsd_XSDComplexTypeContent class attributes and methods

# XSDPatternFacet class attributes and methods

# XSDCardinalityFacet class attributes and methods

# XSDMaxInclusiveFacet class attributes and methods

# XSDMinInclusiveFacet class attributes and methods

# XSDMinExclusiveFacet class attributes and methods

# XSDMaxExclusiveFacet class attributes and methods

# XSDLengthFacet class attributes and methods

# XSDWhiteSpaceFacet class attributes and methods

# XSDEnumerationFacet class attributes and methods

# XSDNumericFacet class attributes and methods

# XSDMaxLengthFacet class attributes and methods

# XSDMinLengthFacet class attributes and methods

# XSDTotalDigitsFacet class attributes and methods

# XSDFractionDigitsFacet class attributes and methods

# XSDOrderedFacet class attributes and methods

# XSDBoundedFacet class attributes and methods

# model_xsd_XSDTerm class attributes and methods

# model_xsd_XSDTotalDigitsFacet class attributes and methods
model_xsd_XSDTotalDigitsFacet_value: Property = Property(name="value", type=IntegerType)
model_xsd_XSDTotalDigitsFacet.attributes={model_xsd_XSDTotalDigitsFacet_value}

# model_xsd_XSDTypeDefinition class attributes and methods

# model_xsd_XSDWhiteSpaceFacet class attributes and methods
model_xsd_XSDWhiteSpaceFacet_value: Property = Property(name="value", type=StringType)
model_xsd_XSDWhiteSpaceFacet.attributes={model_xsd_XSDWhiteSpaceFacet_value}

# model_xsd_XSDWildcard class attributes and methods
model_xsd_XSDWildcard_namespaceConstraintCategory: Property = Property(name="namespaceConstraintCategory", type=StringType)
model_xsd_XSDWildcard_namespaceConstraint: Property = Property(name="namespaceConstraint", type=StringType)
model_xsd_XSDWildcard_processContents: Property = Property(name="processContents", type=StringType)
model_xsd_XSDWildcard_lexicalNamespaceConstraint: Property = Property(name="lexicalNamespaceConstraint", type=StringType)
model_xsd_XSDWildcard.attributes={model_xsd_XSDWildcard_lexicalNamespaceConstraint, model_xsd_XSDWildcard_namespaceConstraintCategory, model_xsd_XSDWildcard_processContents, model_xsd_XSDWildcard_namespaceConstraint}

# model_xsd_XSDXPathDefinition class attributes and methods
model_xsd_XSDXPathDefinition_variety: Property = Property(name="variety", type=StringType)
model_xsd_XSDXPathDefinition_value: Property = Property(name="value", type=StringType)
model_xsd_XSDXPathDefinition.attributes={model_xsd_XSDXPathDefinition_value, model_xsd_XSDXPathDefinition_variety}

# model_partnerlinktype_Role class attributes and methods
model_partnerlinktype_Role_ID: Property = Property(name="ID", type=StringType)
model_partnerlinktype_Role_name: Property = Property(name="name", type=StringType)
model_partnerlinktype_Role_portType: Property = Property(name="portType", type=StringType)
model_partnerlinktype_Role.attributes={model_partnerlinktype_Role_name, model_partnerlinktype_Role_ID, model_partnerlinktype_Role_portType}

# model_messageproperties_Property class attributes and methods
model_messageproperties_Property_qName: Property = Property(name="qName", type=StringType)
model_messageproperties_Property_name: Property = Property(name="name", type=StringType)
model_messageproperties_Property_type: Property = Property(name="type", type=StringType)
model_messageproperties_Property_ID: Property = Property(name="ID", type=StringType)
model_messageproperties_Property.attributes={model_messageproperties_Property_ID, model_messageproperties_Property_qName, model_messageproperties_Property_name, model_messageproperties_Property_type}

# model_messageproperties_PropertyAlias class attributes and methods
model_messageproperties_PropertyAlias_messageType: Property = Property(name="messageType", type=StringType)
model_messageproperties_PropertyAlias_part: Property = Property(name="part", type=StringType)
model_messageproperties_PropertyAlias_propertyName: Property = Property(name="propertyName", type=StringType)
model_messageproperties_PropertyAlias_ID: Property = Property(name="ID", type=StringType)
model_messageproperties_PropertyAlias_type: Property = Property(name="type", type=StringType)
model_messageproperties_PropertyAlias_XSDElement: Property = Property(name="XSDElement", type=StringType)
model_messageproperties_PropertyAlias.attributes={model_messageproperties_PropertyAlias_type, model_messageproperties_PropertyAlias_ID, model_messageproperties_PropertyAlias_propertyName, model_messageproperties_PropertyAlias_messageType, model_messageproperties_PropertyAlias_part, model_messageproperties_PropertyAlias_XSDElement}

# Query class attributes and methods

# model_messageproperties_Query class attributes and methods
model_messageproperties_Query_queryLanguage: Property = Property(name="queryLanguage", type=StringType)
model_messageproperties_Query_value: Property = Property(name="value", type=StringType)
model_messageproperties_Query.attributes={model_messageproperties_Query_queryLanguage, model_messageproperties_Query_value}

# model_partnerlinktype_PartnerLinkType class attributes and methods
model_partnerlinktype_PartnerLinkType_name: Property = Property(name="name", type=StringType)
model_partnerlinktype_PartnerLinkType_ID: Property = Property(name="ID", type=StringType)
model_partnerlinktype_PartnerLinkType.attributes={model_partnerlinktype_PartnerLinkType_name, model_partnerlinktype_PartnerLinkType_ID}

# Relationships
extensions13: BinaryAssociation = BinaryAssociation(
    name="extensions13",
    ends={
        Property(name="model_Extensions", type=model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Process14", type=model_Extensions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageExchanges15: BinaryAssociation = BinaryAssociation(
    name="messageExchanges15",
    ends={
        Property(name="model_MessageExchanges", type=model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Process16", type=model_MessageExchanges, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
partnerLinks0: BinaryAssociation = BinaryAssociation(
    name="partnerLinks0",
    ends={
        Property(name="model_PartnerLinks", type=model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Process", type=model_PartnerLinks, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables1: BinaryAssociation = BinaryAssociation(
    name="variables1",
    ends={
        Property(name="model_Variables", type=model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Process2", type=model_Variables, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activity3: BinaryAssociation = BinaryAssociation(
    name="activity3",
    ends={
        Property(name="model_Activity", type=model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Process4", type=model_Activity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
faultHandlers5: BinaryAssociation = BinaryAssociation(
    name="faultHandlers5",
    ends={
        Property(name="model_FaultHandler", type=model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Process6", type=model_FaultHandler, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventHandlers7: BinaryAssociation = BinaryAssociation(
    name="eventHandlers7",
    ends={
        Property(name="model_EventHandler", type=model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Process8", type=model_EventHandler, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
correlationSets9: BinaryAssociation = BinaryAssociation(
    name="correlationSets9",
    ends={
        Property(name="model_CorrelationSets", type=model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Process10", type=model_CorrelationSets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports11: BinaryAssociation = BinaryAssociation(
    name="imports11",
    ends={
        Property(name="model_Import", type=model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Process12", type=model_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
myRole17: BinaryAssociation = BinaryAssociation(
    name="myRole17",
    ends={
        Property(name="Role", type=model_PartnerLink, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PartnerLink", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
partnerRole18: BinaryAssociation = BinaryAssociation(
    name="partnerRole18",
    ends={
        Property(name="Role20", type=model_PartnerLink, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PartnerLink19", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
PartnerLinkType21: BinaryAssociation = BinaryAssociation(
    name="PartnerLinkType21",
    ends={
        Property(name="PartnerLinkType", type=model_PartnerLink, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PartnerLink22", type=PartnerLinkType, multiplicity=Multiplicity(0, 1))
    }
)
catch23: BinaryAssociation = BinaryAssociation(
    name="catch23",
    ends={
        Property(name="model_Catch", type=model_FaultHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FaultHandler24", type=model_Catch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catchAll25: BinaryAssociation = BinaryAssociation(
    name="catchAll25",
    ends={
        Property(name="model_CatchAll", type=model_FaultHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FaultHandler26", type=model_CatchAll, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toParts43: BinaryAssociation = BinaryAssociation(
    name="toParts43",
    ends={
        Property(name="model_ToParts", type=model_Invoke, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Invoke44", type=model_ToParts, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targets27: BinaryAssociation = BinaryAssociation(
    name="targets27",
    ends={
        Property(name="model_Targets", type=model_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Activity28", type=model_Targets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sources29: BinaryAssociation = BinaryAssociation(
    name="sources29",
    ends={
        Property(name="model_Sources", type=model_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Activity30", type=model_Sources, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties31: BinaryAssociation = BinaryAssociation(
    name="properties31",
    ends={
        Property(name="Property", type=model_CorrelationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CorrelationSet", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
outputVariable32: BinaryAssociation = BinaryAssociation(
    name="outputVariable32",
    ends={
        Property(name="model_Variable", type=model_Invoke, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Invoke", type=model_Variable, multiplicity=Multiplicity(0, 1))
    }
)
inputVariable33: BinaryAssociation = BinaryAssociation(
    name="inputVariable33",
    ends={
        Property(name="model_Variable35", type=model_Invoke, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Invoke34", type=model_Variable, multiplicity=Multiplicity(0, 1))
    }
)
compensationHandler36: BinaryAssociation = BinaryAssociation(
    name="compensationHandler36",
    ends={
        Property(name="model_CompensationHandler", type=model_Invoke, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Invoke37", type=model_CompensationHandler, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
faultHandler38: BinaryAssociation = BinaryAssociation(
    name="faultHandler38",
    ends={
        Property(name="model_FaultHandler40", type=model_Invoke, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Invoke39", type=model_FaultHandler, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromParts41: BinaryAssociation = BinaryAssociation(
    name="fromParts41",
    ends={
        Property(name="model_FromParts", type=model_Invoke, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Invoke42", type=model_FromParts, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
correlations67: BinaryAssociation = BinaryAssociation(
    name="correlations67",
    ends={
        Property(name="model_Correlations", type=model_PartnerActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PartnerActivity68", type=model_Correlations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
portType69: BinaryAssociation = BinaryAssociation(
    name="portType69",
    ends={
        Property(name="PortType", type=model_PartnerActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PartnerActivity70", type=PortType, multiplicity=Multiplicity(1, 1))
    }
)
sources45: BinaryAssociation = BinaryAssociation(
    name="sources45",
    ends={
        Property(name="Source", type=model_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="Link", type=model_Source, multiplicity=Multiplicity(0, 9999))
    }
)
targets46: BinaryAssociation = BinaryAssociation(
    name="targets46",
    ends={
        Property(name="Target", type=model_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="Link47", type=model_Target, multiplicity=Multiplicity(0, 9999))
    }
)
faultVariable48: BinaryAssociation = BinaryAssociation(
    name="faultVariable48",
    ends={
        Property(name="model_Variable50", type=model_Catch, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Catch49", type=model_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activity51: BinaryAssociation = BinaryAssociation(
    name="activity51",
    ends={
        Property(name="model_Activity53", type=model_Catch, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Catch52", type=model_Activity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
faultMessageType54: BinaryAssociation = BinaryAssociation(
    name="faultMessageType54",
    ends={
        Property(name="Message", type=model_Catch, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Catch55", type=Message, multiplicity=Multiplicity(0, 1))
    }
)
faultElement56: BinaryAssociation = BinaryAssociation(
    name="faultElement56",
    ends={
        Property(name="XSDElementDeclaration", type=model_Catch, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Catch57", type=XSDElementDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
variable58: BinaryAssociation = BinaryAssociation(
    name="variable58",
    ends={
        Property(name="model_Variable59", type=model_Reply, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Reply", type=model_Variable, multiplicity=Multiplicity(0, 1))
    }
)
toParts60: BinaryAssociation = BinaryAssociation(
    name="toParts60",
    ends={
        Property(name="model_ToParts62", type=model_Reply, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Reply61", type=model_ToParts, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageExchange63: BinaryAssociation = BinaryAssociation(
    name="messageExchange63",
    ends={
        Property(name="model_MessageExchange", type=model_Reply, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Reply64", type=model_MessageExchange, multiplicity=Multiplicity(1, 1))
    }
)
partnerLink65: BinaryAssociation = BinaryAssociation(
    name="partnerLink65",
    ends={
        Property(name="model_PartnerLink66", type=model_PartnerActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PartnerActivity", type=model_PartnerLink, multiplicity=Multiplicity(1, 1))
    }
)
operation71: BinaryAssociation = BinaryAssociation(
    name="operation71",
    ends={
        Property(name="Operation", type=model_PartnerActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PartnerActivity72", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
variable73: BinaryAssociation = BinaryAssociation(
    name="variable73",
    ends={
        Property(name="model_Variable74", type=model_Receive, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Receive", type=model_Variable, multiplicity=Multiplicity(1, 1))
    }
)
fromParts75: BinaryAssociation = BinaryAssociation(
    name="fromParts75",
    ends={
        Property(name="model_FromParts77", type=model_Receive, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Receive76", type=model_FromParts, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageExchange78: BinaryAssociation = BinaryAssociation(
    name="messageExchange78",
    ends={
        Property(name="model_MessageExchange80", type=model_Receive, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Receive79", type=model_MessageExchange, multiplicity=Multiplicity(1, 1))
    }
)
faultVariable81: BinaryAssociation = BinaryAssociation(
    name="faultVariable81",
    ends={
        Property(name="model_Variable82", type=model_Throw, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Throw", type=model_Variable, multiplicity=Multiplicity(0, 1))
    }
)
for83: BinaryAssociation = BinaryAssociation(
    name="for83",
    ends={
        Property(name="model_Expression", type=model_Wait, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Wait", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
until84: BinaryAssociation = BinaryAssociation(
    name="until84",
    ends={
        Property(name="model_Expression86", type=model_Wait, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Wait85", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activities87: BinaryAssociation = BinaryAssociation(
    name="activities87",
    ends={
        Property(name="model_Activity88", type=model_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Sequence", type=model_Activity, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
activity89: BinaryAssociation = BinaryAssociation(
    name="activity89",
    ends={
        Property(name="model_Activity90", type=model_While, multiplicity=Multiplicity(1, 1)),
        Property(name="model_While", type=model_Activity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition91: BinaryAssociation = BinaryAssociation(
    name="condition91",
    ends={
        Property(name="model_Condition", type=model_While, multiplicity=Multiplicity(1, 1)),
        Property(name="model_While92", type=model_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
messages93: BinaryAssociation = BinaryAssociation(
    name="messages93",
    ends={
        Property(name="model_OnMessage", type=model_Pick, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Pick", type=model_OnMessage, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
alarm94: BinaryAssociation = BinaryAssociation(
    name="alarm94",
    ends={
        Property(name="model_OnAlarm", type=model_Pick, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Pick95", type=model_OnAlarm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activities96: BinaryAssociation = BinaryAssociation(
    name="activities96",
    ends={
        Property(name="model_Activity97", type=model_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Flow", type=model_Activity, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
links98: BinaryAssociation = BinaryAssociation(
    name="links98",
    ends={
        Property(name="model_Links", type=model_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Flow99", type=model_Links, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
completionCondition100: BinaryAssociation = BinaryAssociation(
    name="completionCondition100",
    ends={
        Property(name="model_CompletionCondition", type=model_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Flow101", type=model_CompletionCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activity102: BinaryAssociation = BinaryAssociation(
    name="activity102",
    ends={
        Property(name="model_Activity104", type=model_OnAlarm, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnAlarm103", type=model_Activity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
for105: BinaryAssociation = BinaryAssociation(
    name="for105",
    ends={
        Property(name="model_Expression107", type=model_OnAlarm, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnAlarm106", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
until108: BinaryAssociation = BinaryAssociation(
    name="until108",
    ends={
        Property(name="model_Expression110", type=model_OnAlarm, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnAlarm109", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
repeatEvery111: BinaryAssociation = BinaryAssociation(
    name="repeatEvery111",
    ends={
        Property(name="model_Expression113", type=model_OnAlarm, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnAlarm112", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
copy114: BinaryAssociation = BinaryAssociation(
    name="copy114",
    ends={
        Property(name="model_Copy", type=model_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Assign", type=model_Copy, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
to115: BinaryAssociation = BinaryAssociation(
    name="to115",
    ends={
        Property(name="model_To", type=model_Copy, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Copy116", type=model_To, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from117: BinaryAssociation = BinaryAssociation(
    name="from117",
    ends={
        Property(name="model_From", type=model_Copy, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Copy118", type=model_From, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part151: BinaryAssociation = BinaryAssociation(
    name="part151",
    ends={
        Property(name="Part", type=model_AbstractAssignBound, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AbstractAssignBound152", type=Part, multiplicity=Multiplicity(0, 1))
    }
)
partnerLink153: BinaryAssociation = BinaryAssociation(
    name="partnerLink153",
    ends={
        Property(name="model_PartnerLink155", type=model_AbstractAssignBound, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AbstractAssignBound154", type=model_PartnerLink, multiplicity=Multiplicity(0, 1))
    }
)
faultHandlers119: BinaryAssociation = BinaryAssociation(
    name="faultHandlers119",
    ends={
        Property(name="model_FaultHandler120", type=model_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Scope", type=model_FaultHandler, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compensationHandler121: BinaryAssociation = BinaryAssociation(
    name="compensationHandler121",
    ends={
        Property(name="model_CompensationHandler123", type=model_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Scope122", type=model_CompensationHandler, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activity124: BinaryAssociation = BinaryAssociation(
    name="activity124",
    ends={
        Property(name="model_Activity126", type=model_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Scope125", type=model_Activity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variables127: BinaryAssociation = BinaryAssociation(
    name="variables127",
    ends={
        Property(name="model_Variables129", type=model_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Scope128", type=model_Variables, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
correlationSets130: BinaryAssociation = BinaryAssociation(
    name="correlationSets130",
    ends={
        Property(name="model_CorrelationSets132", type=model_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Scope131", type=model_CorrelationSets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventHandlers133: BinaryAssociation = BinaryAssociation(
    name="eventHandlers133",
    ends={
        Property(name="model_EventHandler135", type=model_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Scope134", type=model_EventHandler, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
partnerLinks136: BinaryAssociation = BinaryAssociation(
    name="partnerLinks136",
    ends={
        Property(name="model_PartnerLinks138", type=model_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Scope137", type=model_PartnerLinks, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
terminationHandler139: BinaryAssociation = BinaryAssociation(
    name="terminationHandler139",
    ends={
        Property(name="model_TerminationHandler", type=model_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Scope140", type=model_TerminationHandler, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageExchanges141: BinaryAssociation = BinaryAssociation(
    name="messageExchanges141",
    ends={
        Property(name="model_MessageExchanges143", type=model_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Scope142", type=model_MessageExchanges, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target144: BinaryAssociation = BinaryAssociation(
    name="target144",
    ends={
        Property(name="model_Activity145", type=model_CompensateScope, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CompensateScope", type=model_Activity, multiplicity=Multiplicity(0, 1))
    }
)
activity146: BinaryAssociation = BinaryAssociation(
    name="activity146",
    ends={
        Property(name="model_Activity148", type=model_CompensationHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CompensationHandler147", type=model_Activity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable149: BinaryAssociation = BinaryAssociation(
    name="variable149",
    ends={
        Property(name="model_Variable150", type=model_AbstractAssignBound, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AbstractAssignBound", type=model_Variable, multiplicity=Multiplicity(0, 1))
    }
)
messageExchange189: BinaryAssociation = BinaryAssociation(
    name="messageExchange189",
    ends={
        Property(name="model_MessageExchange191", type=model_OnMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnMessage190", type=model_MessageExchange, multiplicity=Multiplicity(1, 1))
    }
)
property156: BinaryAssociation = BinaryAssociation(
    name="property156",
    ends={
        Property(name="Property158", type=model_AbstractAssignBound, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AbstractAssignBound157", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
query159: BinaryAssociation = BinaryAssociation(
    name="query159",
    ends={
        Property(name="model_Query", type=model_AbstractAssignBound, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AbstractAssignBound160", type=model_Query, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression161: BinaryAssociation = BinaryAssociation(
    name="expression161",
    ends={
        Property(name="model_Expression163", type=model_AbstractAssignBound, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AbstractAssignBound162", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceRef164: BinaryAssociation = BinaryAssociation(
    name="serviceRef164",
    ends={
        Property(name="model_ServiceRef", type=model_From, multiplicity=Multiplicity(1, 1)),
        Property(name="model_From165", type=model_ServiceRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type166: BinaryAssociation = BinaryAssociation(
    name="type166",
    ends={
        Property(name="XSDTypeDefinition", type=model_From, multiplicity=Multiplicity(1, 1)),
        Property(name="model_From167", type=XSDTypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
variable168: BinaryAssociation = BinaryAssociation(
    name="variable168",
    ends={
        Property(name="model_Variable170", type=model_OnMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnMessage169", type=model_Variable, multiplicity=Multiplicity(0, 1))
    }
)
activity171: BinaryAssociation = BinaryAssociation(
    name="activity171",
    ends={
        Property(name="model_Activity173", type=model_OnMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnMessage172", type=model_Activity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
portType174: BinaryAssociation = BinaryAssociation(
    name="portType174",
    ends={
        Property(name="PortType176", type=model_OnMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnMessage175", type=PortType, multiplicity=Multiplicity(1, 1))
    }
)
partnerLink177: BinaryAssociation = BinaryAssociation(
    name="partnerLink177",
    ends={
        Property(name="model_PartnerLink179", type=model_OnMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnMessage178", type=model_PartnerLink, multiplicity=Multiplicity(1, 1))
    }
)
correlations180: BinaryAssociation = BinaryAssociation(
    name="correlations180",
    ends={
        Property(name="model_Correlations182", type=model_OnMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnMessage181", type=model_Correlations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation183: BinaryAssociation = BinaryAssociation(
    name="operation183",
    ends={
        Property(name="Operation185", type=model_OnMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnMessage184", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
fromParts186: BinaryAssociation = BinaryAssociation(
    name="fromParts186",
    ends={
        Property(name="model_FromParts188", type=model_OnMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnMessage187", type=model_FromParts, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
set192: BinaryAssociation = BinaryAssociation(
    name="set192",
    ends={
        Property(name="model_CorrelationSet193", type=model_Correlation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Correlation", type=model_CorrelationSet, multiplicity=Multiplicity(1, 1))
    }
)
alarm194: BinaryAssociation = BinaryAssociation(
    name="alarm194",
    ends={
        Property(name="model_OnAlarm196", type=model_EventHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="model_EventHandler195", type=model_OnAlarm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events197: BinaryAssociation = BinaryAssociation(
    name="events197",
    ends={
        Property(name="model_OnEvent", type=model_EventHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="model_EventHandler198", type=model_OnEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Link199: BinaryAssociation = BinaryAssociation(
    name="Link199",
    ends={
        Property(name="Link200", type=model_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="sources", type=model_Link, multiplicity=Multiplicity(1, 1))
    }
)
activity201: BinaryAssociation = BinaryAssociation(
    name="activity201",
    ends={
        Property(name="model_Activity202", type=model_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Source", type=model_Activity, multiplicity=Multiplicity(1, 1))
    }
)
transitionCondition203: BinaryAssociation = BinaryAssociation(
    name="transitionCondition203",
    ends={
        Property(name="model_Condition205", type=model_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Source204", type=model_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Link206: BinaryAssociation = BinaryAssociation(
    name="Link206",
    ends={
        Property(name="Link207", type=model_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="targets", type=model_Link, multiplicity=Multiplicity(1, 1))
    }
)
activity208: BinaryAssociation = BinaryAssociation(
    name="activity208",
    ends={
        Property(name="model_Activity209", type=model_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Target", type=model_Activity, multiplicity=Multiplicity(1, 1))
    }
)
XSDElement233: BinaryAssociation = BinaryAssociation(
    name="XSDElement233",
    ends={
        Property(name="XSDElementDeclaration235", type=model_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Variable234", type=XSDElementDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
children210: BinaryAssociation = BinaryAssociation(
    name="children210",
    ends={
        Property(name="model_PartnerLink212", type=model_PartnerLinks, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PartnerLinks211", type=model_PartnerLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children213: BinaryAssociation = BinaryAssociation(
    name="children213",
    ends={
        Property(name="model_MessageExchange215", type=model_MessageExchanges, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MessageExchanges214", type=model_MessageExchange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children216: BinaryAssociation = BinaryAssociation(
    name="children216",
    ends={
        Property(name="model_Variable218", type=model_Variables, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Variables217", type=model_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children219: BinaryAssociation = BinaryAssociation(
    name="children219",
    ends={
        Property(name="model_CorrelationSet221", type=model_CorrelationSets, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CorrelationSets220", type=model_CorrelationSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children222: BinaryAssociation = BinaryAssociation(
    name="children222",
    ends={
        Property(name="model_Link", type=model_Links, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Links223", type=model_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activity224: BinaryAssociation = BinaryAssociation(
    name="activity224",
    ends={
        Property(name="model_Activity226", type=model_CatchAll, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CatchAll225", type=model_Activity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children227: BinaryAssociation = BinaryAssociation(
    name="children227",
    ends={
        Property(name="model_Correlation229", type=model_Correlations, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Correlations228", type=model_Correlation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageType230: BinaryAssociation = BinaryAssociation(
    name="messageType230",
    ends={
        Property(name="Message232", type=model_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Variable231", type=Message, multiplicity=Multiplicity(0, 1))
    }
)
children275: BinaryAssociation = BinaryAssociation(
    name="children275",
    ends={
        Property(name="model_Target277", type=model_Targets, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Targets276", type=model_Target, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type236: BinaryAssociation = BinaryAssociation(
    name="type236",
    ends={
        Property(name="XSDTypeDefinition238", type=model_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Variable237", type=XSDTypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
from239: BinaryAssociation = BinaryAssociation(
    name="from239",
    ends={
        Property(name="model_From241", type=model_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Variable240", type=model_From, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activity242: BinaryAssociation = BinaryAssociation(
    name="activity242",
    ends={
        Property(name="model_Activity244", type=model_OnEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnEvent243", type=model_Activity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable245: BinaryAssociation = BinaryAssociation(
    name="variable245",
    ends={
        Property(name="model_Variable247", type=model_OnEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnEvent246", type=model_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
partnerLink248: BinaryAssociation = BinaryAssociation(
    name="partnerLink248",
    ends={
        Property(name="model_PartnerLink250", type=model_OnEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnEvent249", type=model_PartnerLink, multiplicity=Multiplicity(1, 1))
    }
)
correlations251: BinaryAssociation = BinaryAssociation(
    name="correlations251",
    ends={
        Property(name="model_Correlations253", type=model_OnEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnEvent252", type=model_Correlations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation254: BinaryAssociation = BinaryAssociation(
    name="operation254",
    ends={
        Property(name="Operation256", type=model_OnEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnEvent255", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
portType257: BinaryAssociation = BinaryAssociation(
    name="portType257",
    ends={
        Property(name="PortType259", type=model_OnEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnEvent258", type=PortType, multiplicity=Multiplicity(1, 1))
    }
)
messageType260: BinaryAssociation = BinaryAssociation(
    name="messageType260",
    ends={
        Property(name="Message262", type=model_OnEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnEvent261", type=Message, multiplicity=Multiplicity(0, 1))
    }
)
XSDElement263: BinaryAssociation = BinaryAssociation(
    name="XSDElement263",
    ends={
        Property(name="XSDElementDeclaration265", type=model_OnEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnEvent264", type=XSDElementDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
correlationSets266: BinaryAssociation = BinaryAssociation(
    name="correlationSets266",
    ends={
        Property(name="model_CorrelationSets268", type=model_OnEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnEvent267", type=model_CorrelationSets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromParts269: BinaryAssociation = BinaryAssociation(
    name="fromParts269",
    ends={
        Property(name="model_FromParts271", type=model_OnEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnEvent270", type=model_FromParts, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageExchange272: BinaryAssociation = BinaryAssociation(
    name="messageExchange272",
    ends={
        Property(name="model_MessageExchange274", type=model_OnEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OnEvent273", type=model_MessageExchange, multiplicity=Multiplicity(1, 1))
    }
)
counterName301: BinaryAssociation = BinaryAssociation(
    name="counterName301",
    ends={
        Property(name="model_Variable303", type=model_ForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ForEach302", type=model_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
joinCondition278: BinaryAssociation = BinaryAssociation(
    name="joinCondition278",
    ends={
        Property(name="model_Condition280", type=model_Targets, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Targets279", type=model_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children281: BinaryAssociation = BinaryAssociation(
    name="children281",
    ends={
        Property(name="model_Source283", type=model_Sources, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Sources282", type=model_Source, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children284: BinaryAssociation = BinaryAssociation(
    name="children284",
    ends={
        Property(name="model_Extension", type=model_Extensions, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Extensions285", type=model_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toVariable286: BinaryAssociation = BinaryAssociation(
    name="toVariable286",
    ends={
        Property(name="model_Variable287", type=model_FromPart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FromPart", type=model_Variable, multiplicity=Multiplicity(0, 1))
    }
)
part288: BinaryAssociation = BinaryAssociation(
    name="part288",
    ends={
        Property(name="Part290", type=model_FromPart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FromPart289", type=Part, multiplicity=Multiplicity(0, 1))
    }
)
fromVariable291: BinaryAssociation = BinaryAssociation(
    name="fromVariable291",
    ends={
        Property(name="model_Variable292", type=model_ToPart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ToPart", type=model_Variable, multiplicity=Multiplicity(0, 1))
    }
)
part293: BinaryAssociation = BinaryAssociation(
    name="part293",
    ends={
        Property(name="Part295", type=model_ToPart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ToPart294", type=Part, multiplicity=Multiplicity(0, 1))
    }
)
startCounterValue296: BinaryAssociation = BinaryAssociation(
    name="startCounterValue296",
    ends={
        Property(name="model_Expression297", type=model_ForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ForEach", type=model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finalCounterValue298: BinaryAssociation = BinaryAssociation(
    name="finalCounterValue298",
    ends={
        Property(name="model_Expression300", type=model_ForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ForEach299", type=model_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
activity335: BinaryAssociation = BinaryAssociation(
    name="activity335",
    ends={
        Property(name="model_Activity337", type=model_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Else336", type=model_Activity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
completionCondition304: BinaryAssociation = BinaryAssociation(
    name="completionCondition304",
    ends={
        Property(name="model_CompletionCondition306", type=model_ForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ForEach305", type=model_CompletionCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activity307: BinaryAssociation = BinaryAssociation(
    name="activity307",
    ends={
        Property(name="model_Activity309", type=model_ForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ForEach308", type=model_Activity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
activity310: BinaryAssociation = BinaryAssociation(
    name="activity310",
    ends={
        Property(name="model_Activity311", type=model_RepeatUntil, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RepeatUntil", type=model_Activity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition312: BinaryAssociation = BinaryAssociation(
    name="condition312",
    ends={
        Property(name="model_Condition314", type=model_RepeatUntil, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RepeatUntil313", type=model_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
activity315: BinaryAssociation = BinaryAssociation(
    name="activity315",
    ends={
        Property(name="model_Activity317", type=model_TerminationHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TerminationHandler316", type=model_Activity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables318: BinaryAssociation = BinaryAssociation(
    name="variables318",
    ends={
        Property(name="model_Variable319", type=model_Validate, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Validate", type=model_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
condition320: BinaryAssociation = BinaryAssociation(
    name="condition320",
    ends={
        Property(name="model_Condition321", type=model_If, multiplicity=Multiplicity(1, 1)),
        Property(name="model_If", type=model_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIf322: BinaryAssociation = BinaryAssociation(
    name="elseIf322",
    ends={
        Property(name="model_ElseIf", type=model_If, multiplicity=Multiplicity(1, 1)),
        Property(name="model_If323", type=model_ElseIf, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else324: BinaryAssociation = BinaryAssociation(
    name="else324",
    ends={
        Property(name="model_Else", type=model_If, multiplicity=Multiplicity(1, 1)),
        Property(name="model_If325", type=model_Else, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activity326: BinaryAssociation = BinaryAssociation(
    name="activity326",
    ends={
        Property(name="model_Activity328", type=model_If, multiplicity=Multiplicity(1, 1)),
        Property(name="model_If327", type=model_Activity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition329: BinaryAssociation = BinaryAssociation(
    name="condition329",
    ends={
        Property(name="model_Condition331", type=model_ElseIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ElseIf330", type=model_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activity332: BinaryAssociation = BinaryAssociation(
    name="activity332",
    ends={
        Property(name="model_Activity334", type=model_ElseIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ElseIf333", type=model_Activity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
eOperations347: BinaryAssociation = BinaryAssociation(
    name="eOperations347",
    ends={
        Property(name="Operation348", type=model_wsdl_PortType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_PortType", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branches338: BinaryAssociation = BinaryAssociation(
    name="branches338",
    ends={
        Property(name="model_Branches", type=model_CompletionCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CompletionCondition339", type=model_Branches, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
documentation340: BinaryAssociation = BinaryAssociation(
    name="documentation340",
    ends={
        Property(name="model_Documentation", type=model_BPELExtensibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BPELExtensibleElement", type=model_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children341: BinaryAssociation = BinaryAssociation(
    name="children341",
    ends={
        Property(name="model_FromPart343", type=model_FromParts, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FromParts342", type=model_FromPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children344: BinaryAssociation = BinaryAssociation(
    name="children344",
    ends={
        Property(name="model_ToPart346", type=model_ToParts, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ToParts345", type=model_ToPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eInput349: BinaryAssociation = BinaryAssociation(
    name="eInput349",
    ends={
        Property(name="Input", type=model_wsdl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Operation", type=Input, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eOutput350: BinaryAssociation = BinaryAssociation(
    name="eOutput350",
    ends={
        Property(name="Output", type=model_wsdl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Operation351", type=Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eFaults352: BinaryAssociation = BinaryAssociation(
    name="eFaults352",
    ends={
        Property(name="Fault", type=model_wsdl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Operation353", type=Fault, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameterOrdering354: BinaryAssociation = BinaryAssociation(
    name="eParameterOrdering354",
    ends={
        Property(name="Part356", type=model_wsdl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Operation355", type=Part, multiplicity=Multiplicity(0, 9999))
    }
)
eParts357: BinaryAssociation = BinaryAssociation(
    name="eParts357",
    ends={
        Property(name="Part358", type=model_wsdl_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Message", type=Part, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDefinition359: BinaryAssociation = BinaryAssociation(
    name="typeDefinition359",
    ends={
        Property(name="XSDTypeDefinition360", type=model_wsdl_Part, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Part", type=XSDTypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
elementDeclaration361: BinaryAssociation = BinaryAssociation(
    name="elementDeclaration361",
    ends={
        Property(name="XSDElementDeclaration363", type=model_wsdl_Part, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Part362", type=XSDElementDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
eMessage364: BinaryAssociation = BinaryAssociation(
    name="eMessage364",
    ends={
        Property(name="Message366", type=model_wsdl_Part, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Part365", type=Message, multiplicity=Multiplicity(0, 1))
    }
)
ePortType367: BinaryAssociation = BinaryAssociation(
    name="ePortType367",
    ends={
        Property(name="PortType368", type=model_wsdl_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Binding", type=PortType, multiplicity=Multiplicity(1, 1))
    }
)
eBindingOperations369: BinaryAssociation = BinaryAssociation(
    name="eBindingOperations369",
    ends={
        Property(name="BindingOperation", type=model_wsdl_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Binding370", type=BindingOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eOperation371: BinaryAssociation = BinaryAssociation(
    name="eOperation371",
    ends={
        Property(name="Operation372", type=model_wsdl_BindingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_BindingOperation", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
eBindingInput373: BinaryAssociation = BinaryAssociation(
    name="eBindingInput373",
    ends={
        Property(name="BindingInput", type=model_wsdl_BindingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_BindingOperation374", type=BindingInput, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eBindingOutput375: BinaryAssociation = BinaryAssociation(
    name="eBindingOutput375",
    ends={
        Property(name="BindingOutput", type=model_wsdl_BindingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_BindingOperation376", type=BindingOutput, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eBindingFaults377: BinaryAssociation = BinaryAssociation(
    name="eBindingFaults377",
    ends={
        Property(name="BindingFault", type=model_wsdl_BindingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_BindingOperation378", type=BindingFault, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePorts379: BinaryAssociation = BinaryAssociation(
    name="ePorts379",
    ends={
        Property(name="Port", type=model_wsdl_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Service", type=Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eBinding380: BinaryAssociation = BinaryAssociation(
    name="eBinding380",
    ends={
        Property(name="Binding", type=model_wsdl_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Port", type=Binding, multiplicity=Multiplicity(1, 1))
    }
)
eExtensibilityElements400: BinaryAssociation = BinaryAssociation(
    name="eExtensibilityElements400",
    ends={
        Property(name="ExtensibilityElement", type=model_wsdl_ExtensibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_ExtensibleElement", type=ExtensibilityElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eImports381: BinaryAssociation = BinaryAssociation(
    name="eImports381",
    ends={
        Property(name="Import", type=model_wsdl_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Definition", type=Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eTypes382: BinaryAssociation = BinaryAssociation(
    name="eTypes382",
    ends={
        Property(name="Types", type=model_wsdl_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Definition383", type=Types, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eMessages384: BinaryAssociation = BinaryAssociation(
    name="eMessages384",
    ends={
        Property(name="Message386", type=model_wsdl_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Definition385", type=Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePortTypes387: BinaryAssociation = BinaryAssociation(
    name="ePortTypes387",
    ends={
        Property(name="PortType389", type=model_wsdl_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Definition388", type=PortType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eBindings390: BinaryAssociation = BinaryAssociation(
    name="eBindings390",
    ends={
        Property(name="Binding392", type=model_wsdl_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Definition391", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eServices393: BinaryAssociation = BinaryAssociation(
    name="eServices393",
    ends={
        Property(name="Service", type=model_wsdl_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Definition394", type=Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eNamespaces395: BinaryAssociation = BinaryAssociation(
    name="eNamespaces395",
    ends={
        Property(name="Namespace", type=model_wsdl_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Definition396", type=Namespace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eDefinition397: BinaryAssociation = BinaryAssociation(
    name="eDefinition397",
    ends={
        Property(name="Definition", type=model_wsdl_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Import", type=Definition, multiplicity=Multiplicity(0, 1))
    }
)
eSchema398: BinaryAssociation = BinaryAssociation(
    name="eSchema398",
    ends={
        Property(name="XSDSchema", type=model_wsdl_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_Import399", type=XSDSchema, multiplicity=Multiplicity(0, 1))
    }
)
eInput401: BinaryAssociation = BinaryAssociation(
    name="eInput401",
    ends={
        Property(name="Input402", type=model_wsdl_BindingInput, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_BindingInput", type=Input, multiplicity=Multiplicity(1, 1))
    }
)
eOutput403: BinaryAssociation = BinaryAssociation(
    name="eOutput403",
    ends={
        Property(name="Output404", type=model_wsdl_BindingOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_BindingOutput", type=Output, multiplicity=Multiplicity(1, 1))
    }
)
eFault405: BinaryAssociation = BinaryAssociation(
    name="eFault405",
    ends={
        Property(name="Fault406", type=model_wsdl_BindingFault, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_BindingFault", type=Fault, multiplicity=Multiplicity(1, 1))
    }
)
children407: BinaryAssociation = BinaryAssociation(
    name="children407",
    ends={
        Property(name="UnknownExtensibilityElement", type=model_wsdl_UnknownExtensibilityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_UnknownExtensibilityElement", type=UnknownExtensibilityElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation412: BinaryAssociation = BinaryAssociation(
    name="annotation412",
    ends={
        Property(name="XSDAnnotation", type=model_xsd_XSDAttributeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDAttributeDeclaration", type=XSDAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anonymousTypeDefinition413: BinaryAssociation = BinaryAssociation(
    name="anonymousTypeDefinition413",
    ends={
        Property(name="XSDSimpleTypeDefinition", type=model_xsd_XSDAttributeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDAttributeDeclaration414", type=XSDSimpleTypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDefinition415: BinaryAssociation = BinaryAssociation(
    name="typeDefinition415",
    ends={
        Property(name="XSDSimpleTypeDefinition417", type=model_xsd_XSDAttributeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDAttributeDeclaration416", type=XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
schema408: BinaryAssociation = BinaryAssociation(
    name="schema408",
    ends={
        Property(name="XSDSchema409", type=model_wsdl_XSDSchemaExtensibilityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_XSDSchemaExtensibilityElement", type=XSDSchema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eMessage410: BinaryAssociation = BinaryAssociation(
    name="eMessage410",
    ends={
        Property(name="Message411", type=model_wsdl_MessageReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_wsdl_MessageReference", type=Message, multiplicity=Multiplicity(1, 1))
    }
)
resolvedAttributeDeclaration418: BinaryAssociation = BinaryAssociation(
    name="resolvedAttributeDeclaration418",
    ends={
        Property(name="XSDAttributeDeclaration", type=model_xsd_XSDAttributeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDAttributeDeclaration419", type=XSDAttributeDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
annotation420: BinaryAssociation = BinaryAssociation(
    name="annotation420",
    ends={
        Property(name="XSDAnnotation421", type=model_xsd_XSDAttributeGroupDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDAttributeGroupDefinition", type=XSDAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contents422: BinaryAssociation = BinaryAssociation(
    name="contents422",
    ends={
        Property(name="XSDAttributeGroupContent", type=model_xsd_XSDAttributeGroupDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDAttributeGroupDefinition423", type=XSDAttributeGroupContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeUses424: BinaryAssociation = BinaryAssociation(
    name="attributeUses424",
    ends={
        Property(name="XSDAttributeUse", type=model_xsd_XSDAttributeGroupDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDAttributeGroupDefinition425", type=XSDAttributeUse, multiplicity=Multiplicity(0, 9999))
    }
)
attributeWildcardContent426: BinaryAssociation = BinaryAssociation(
    name="attributeWildcardContent426",
    ends={
        Property(name="XSDWildcard", type=model_xsd_XSDAttributeGroupDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDAttributeGroupDefinition427", type=XSDWildcard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributeWildcard428: BinaryAssociation = BinaryAssociation(
    name="attributeWildcard428",
    ends={
        Property(name="XSDWildcard430", type=model_xsd_XSDAttributeGroupDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDAttributeGroupDefinition429", type=XSDWildcard, multiplicity=Multiplicity(0, 1))
    }
)
resolvedAttributeGroupDefinition431: BinaryAssociation = BinaryAssociation(
    name="resolvedAttributeGroupDefinition431",
    ends={
        Property(name="XSDAttributeGroupDefinition", type=model_xsd_XSDAttributeGroupDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDAttributeGroupDefinition432", type=XSDAttributeGroupDefinition, multiplicity=Multiplicity(1, 1))
    }
)
syntheticWildcard433: BinaryAssociation = BinaryAssociation(
    name="syntheticWildcard433",
    ends={
        Property(name="XSDWildcard435", type=model_xsd_XSDAttributeGroupDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDAttributeGroupDefinition434", type=XSDWildcard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributeDeclaration436: BinaryAssociation = BinaryAssociation(
    name="attributeDeclaration436",
    ends={
        Property(name="XSDAttributeDeclaration437", type=model_xsd_XSDAttributeUse, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDAttributeUse", type=XSDAttributeDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
content438: BinaryAssociation = BinaryAssociation(
    name="content438",
    ends={
        Property(name="XSDAttributeDeclaration440", type=model_xsd_XSDAttributeUse, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDAttributeUse439", type=XSDAttributeDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributeWildcardContent460: BinaryAssociation = BinaryAssociation(
    name="attributeWildcardContent460",
    ends={
        Property(name="XSDWildcard462", type=model_xsd_XSDComplexTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDComplexTypeDefinition461", type=XSDWildcard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rootTypeDefinition463: BinaryAssociation = BinaryAssociation(
    name="rootTypeDefinition463",
    ends={
        Property(name="XSDTypeDefinition465", type=model_xsd_XSDComplexTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDComplexTypeDefinition464", type=XSDTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
syntheticParticle466: BinaryAssociation = BinaryAssociation(
    name="syntheticParticle466",
    ends={
        Property(name="XSDParticle", type=model_xsd_XSDComplexTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDComplexTypeDefinition467", type=XSDParticle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contentAnnotation441: BinaryAssociation = BinaryAssociation(
    name="contentAnnotation441",
    ends={
        Property(name="XSDAnnotation442", type=model_xsd_XSDComplexTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDComplexTypeDefinition", type=XSDAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseTypeDefinition443: BinaryAssociation = BinaryAssociation(
    name="baseTypeDefinition443",
    ends={
        Property(name="XSDTypeDefinition445", type=model_xsd_XSDComplexTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDComplexTypeDefinition444", type=XSDTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
content446: BinaryAssociation = BinaryAssociation(
    name="content446",
    ends={
        Property(name="XSDComplexTypeContent", type=model_xsd_XSDComplexTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDComplexTypeDefinition447", type=XSDComplexTypeContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contentType448: BinaryAssociation = BinaryAssociation(
    name="contentType448",
    ends={
        Property(name="XSDComplexTypeContent450", type=model_xsd_XSDComplexTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDComplexTypeDefinition449", type=XSDComplexTypeContent, multiplicity=Multiplicity(0, 1))
    }
)
attributeUses451: BinaryAssociation = BinaryAssociation(
    name="attributeUses451",
    ends={
        Property(name="XSDAttributeUse453", type=model_xsd_XSDComplexTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDComplexTypeDefinition452", type=XSDAttributeUse, multiplicity=Multiplicity(0, 9999))
    }
)
attributeContents454: BinaryAssociation = BinaryAssociation(
    name="attributeContents454",
    ends={
        Property(name="XSDAttributeGroupContent456", type=model_xsd_XSDComplexTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDComplexTypeDefinition455", type=XSDAttributeGroupContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeWildcard457: BinaryAssociation = BinaryAssociation(
    name="attributeWildcard457",
    ends={
        Property(name="XSDWildcard459", type=model_xsd_XSDComplexTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDComplexTypeDefinition458", type=XSDWildcard, multiplicity=Multiplicity(0, 1))
    }
)
syntheticWildcard468: BinaryAssociation = BinaryAssociation(
    name="syntheticWildcard468",
    ends={
        Property(name="XSDWildcard470", type=model_xsd_XSDComplexTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDComplexTypeDefinition469", type=XSDWildcard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container471: BinaryAssociation = BinaryAssociation(
    name="container471",
    ends={
        Property(name="XSDConcreteComponent", type=model_xsd_XSDConcreteComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDConcreteComponent", type=XSDConcreteComponent, multiplicity=Multiplicity(0, 1))
    }
)
rootContainer472: BinaryAssociation = BinaryAssociation(
    name="rootContainer472",
    ends={
        Property(name="XSDConcreteComponent474", type=model_xsd_XSDConcreteComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDConcreteComponent473", type=XSDConcreteComponent, multiplicity=Multiplicity(1, 1))
    }
)
schema475: BinaryAssociation = BinaryAssociation(
    name="schema475",
    ends={
        Property(name="XSDSchema477", type=model_xsd_XSDConcreteComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDConcreteComponent476", type=XSDSchema, multiplicity=Multiplicity(0, 1))
    }
)
diagnostics478: BinaryAssociation = BinaryAssociation(
    name="diagnostics478",
    ends={
        Property(name="XSDDiagnostic", type=model_xsd_XSDConcreteComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDConcreteComponent479", type=XSDDiagnostic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components480: BinaryAssociation = BinaryAssociation(
    name="components480",
    ends={
        Property(name="XSDConcreteComponent481", type=model_xsd_XSDDiagnostic, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDDiagnostic", type=XSDConcreteComponent, multiplicity=Multiplicity(1, 9999))
    }
)
primaryComponent482: BinaryAssociation = BinaryAssociation(
    name="primaryComponent482",
    ends={
        Property(name="XSDConcreteComponent484", type=model_xsd_XSDDiagnostic, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDDiagnostic483", type=XSDConcreteComponent, multiplicity=Multiplicity(1, 1))
    }
)
annotation485: BinaryAssociation = BinaryAssociation(
    name="annotation485",
    ends={
        Property(name="XSDAnnotation486", type=model_xsd_XSDElementDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDElementDeclaration", type=XSDAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anonymousTypeDefinition487: BinaryAssociation = BinaryAssociation(
    name="anonymousTypeDefinition487",
    ends={
        Property(name="XSDTypeDefinition489", type=model_xsd_XSDElementDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDElementDeclaration488", type=XSDTypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDefinition490: BinaryAssociation = BinaryAssociation(
    name="typeDefinition490",
    ends={
        Property(name="XSDTypeDefinition492", type=model_xsd_XSDElementDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDElementDeclaration491", type=XSDTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
identityConstraintDefinitions493: BinaryAssociation = BinaryAssociation(
    name="identityConstraintDefinitions493",
    ends={
        Property(name="XSDIdentityConstraintDefinition", type=model_xsd_XSDElementDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDElementDeclaration494", type=XSDIdentityConstraintDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resolvedElementDeclaration495: BinaryAssociation = BinaryAssociation(
    name="resolvedElementDeclaration495",
    ends={
        Property(name="XSDElementDeclaration497", type=model_xsd_XSDElementDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDElementDeclaration496", type=XSDElementDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
substitutionGroupAffiliation498: BinaryAssociation = BinaryAssociation(
    name="substitutionGroupAffiliation498",
    ends={
        Property(name="XSDElementDeclaration500", type=model_xsd_XSDElementDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDElementDeclaration499", type=XSDElementDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
substitutionGroup501: BinaryAssociation = BinaryAssociation(
    name="substitutionGroup501",
    ends={
        Property(name="XSDElementDeclaration503", type=model_xsd_XSDElementDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDElementDeclaration502", type=XSDElementDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
annotation504: BinaryAssociation = BinaryAssociation(
    name="annotation504",
    ends={
        Property(name="XSDAnnotation505", type=model_xsd_XSDFacet, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDFacet", type=XSDAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleTypeDefinition506: BinaryAssociation = BinaryAssociation(
    name="simpleTypeDefinition506",
    ends={
        Property(name="XSDSimpleTypeDefinition508", type=model_xsd_XSDFacet, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDFacet507", type=XSDSimpleTypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
scope509: BinaryAssociation = BinaryAssociation(
    name="scope509",
    ends={
        Property(name="XSDScope", type=model_xsd_XSDFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDFeature", type=XSDScope, multiplicity=Multiplicity(0, 1))
    }
)
resolvedFeature510: BinaryAssociation = BinaryAssociation(
    name="resolvedFeature510",
    ends={
        Property(name="XSDFeature", type=model_xsd_XSDFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDFeature511", type=XSDFeature, multiplicity=Multiplicity(1, 1))
    }
)
type512: BinaryAssociation = BinaryAssociation(
    name="type512",
    ends={
        Property(name="XSDTypeDefinition514", type=model_xsd_XSDFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDFeature513", type=XSDTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
annotation515: BinaryAssociation = BinaryAssociation(
    name="annotation515",
    ends={
        Property(name="XSDAnnotation516", type=model_xsd_XSDIdentityConstraintDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDIdentityConstraintDefinition", type=XSDAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedKey517: BinaryAssociation = BinaryAssociation(
    name="referencedKey517",
    ends={
        Property(name="XSDIdentityConstraintDefinition519", type=model_xsd_XSDIdentityConstraintDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDIdentityConstraintDefinition518", type=XSDIdentityConstraintDefinition, multiplicity=Multiplicity(0, 1))
    }
)
selector520: BinaryAssociation = BinaryAssociation(
    name="selector520",
    ends={
        Property(name="XSDXPathDefinition", type=model_xsd_XSDIdentityConstraintDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDIdentityConstraintDefinition521", type=XSDXPathDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fields522: BinaryAssociation = BinaryAssociation(
    name="fields522",
    ends={
        Property(name="XSDXPathDefinition524", type=model_xsd_XSDIdentityConstraintDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDIdentityConstraintDefinition523", type=XSDXPathDefinition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
annotation525: BinaryAssociation = BinaryAssociation(
    name="annotation525",
    ends={
        Property(name="XSDAnnotation526", type=model_xsd_XSDImport, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDImport", type=XSDAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotation527: BinaryAssociation = BinaryAssociation(
    name="annotation527",
    ends={
        Property(name="XSDAnnotation528", type=model_xsd_XSDInclude, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDInclude", type=XSDAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotation529: BinaryAssociation = BinaryAssociation(
    name="annotation529",
    ends={
        Property(name="XSDAnnotation530", type=model_xsd_XSDModelGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDModelGroup", type=XSDAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contents531: BinaryAssociation = BinaryAssociation(
    name="contents531",
    ends={
        Property(name="XSDParticle533", type=model_xsd_XSDModelGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDModelGroup532", type=XSDParticle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
particles534: BinaryAssociation = BinaryAssociation(
    name="particles534",
    ends={
        Property(name="XSDParticle536", type=model_xsd_XSDModelGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDModelGroup535", type=XSDParticle, multiplicity=Multiplicity(1, 9999))
    }
)
annotation537: BinaryAssociation = BinaryAssociation(
    name="annotation537",
    ends={
        Property(name="XSDAnnotation538", type=model_xsd_XSDModelGroupDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDModelGroupDefinition", type=XSDAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelGroup539: BinaryAssociation = BinaryAssociation(
    name="modelGroup539",
    ends={
        Property(name="XSDModelGroup", type=model_xsd_XSDModelGroupDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDModelGroupDefinition540", type=XSDModelGroup, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolvedModelGroupDefinition541: BinaryAssociation = BinaryAssociation(
    name="resolvedModelGroupDefinition541",
    ends={
        Property(name="XSDModelGroupDefinition", type=model_xsd_XSDModelGroupDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDModelGroupDefinition542", type=XSDModelGroupDefinition, multiplicity=Multiplicity(1, 1))
    }
)
annotations552: BinaryAssociation = BinaryAssociation(
    name="annotations552",
    ends={
        Property(name="XSDAnnotation553", type=model_xsd_XSDRepeatableFacet, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDRepeatableFacet", type=XSDAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)
annotation543: BinaryAssociation = BinaryAssociation(
    name="annotation543",
    ends={
        Property(name="XSDAnnotation544", type=model_xsd_XSDNotationDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDNotationDeclaration", type=XSDAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content545: BinaryAssociation = BinaryAssociation(
    name="content545",
    ends={
        Property(name="XSDParticleContent", type=model_xsd_XSDParticle, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDParticle", type=XSDParticleContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term546: BinaryAssociation = BinaryAssociation(
    name="term546",
    ends={
        Property(name="XSDTerm", type=model_xsd_XSDParticle, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDParticle547", type=XSDTerm, multiplicity=Multiplicity(1, 1))
    }
)
annotations548: BinaryAssociation = BinaryAssociation(
    name="annotations548",
    ends={
        Property(name="XSDAnnotation549", type=model_xsd_XSDRedefine, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDRedefine", type=XSDAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)
contents550: BinaryAssociation = BinaryAssociation(
    name="contents550",
    ends={
        Property(name="XSDRedefineContent", type=model_xsd_XSDRedefine, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDRedefine551", type=XSDRedefineContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalVersion586: BinaryAssociation = BinaryAssociation(
    name="originalVersion586",
    ends={
        Property(name="XSDSchema588", type=model_xsd_XSDSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchema587", type=XSDSchema, multiplicity=Multiplicity(0, 1))
    }
)
contents554: BinaryAssociation = BinaryAssociation(
    name="contents554",
    ends={
        Property(name="XSDSchemaContent", type=model_xsd_XSDSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchema", type=XSDSchemaContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementDeclarations555: BinaryAssociation = BinaryAssociation(
    name="elementDeclarations555",
    ends={
        Property(name="XSDElementDeclaration557", type=model_xsd_XSDSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchema556", type=XSDElementDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
attributeDeclarations558: BinaryAssociation = BinaryAssociation(
    name="attributeDeclarations558",
    ends={
        Property(name="XSDAttributeDeclaration560", type=model_xsd_XSDSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchema559", type=XSDAttributeDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
attributeGroupDefinitions561: BinaryAssociation = BinaryAssociation(
    name="attributeGroupDefinitions561",
    ends={
        Property(name="XSDAttributeGroupDefinition563", type=model_xsd_XSDSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchema562", type=XSDAttributeGroupDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
typeDefinitions564: BinaryAssociation = BinaryAssociation(
    name="typeDefinitions564",
    ends={
        Property(name="XSDTypeDefinition566", type=model_xsd_XSDSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchema565", type=XSDTypeDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
modelGroupDefinitions567: BinaryAssociation = BinaryAssociation(
    name="modelGroupDefinitions567",
    ends={
        Property(name="XSDModelGroupDefinition569", type=model_xsd_XSDSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchema568", type=XSDModelGroupDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
identityConstraintDefinitions570: BinaryAssociation = BinaryAssociation(
    name="identityConstraintDefinitions570",
    ends={
        Property(name="XSDIdentityConstraintDefinition572", type=model_xsd_XSDSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchema571", type=XSDIdentityConstraintDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
notationDeclarations573: BinaryAssociation = BinaryAssociation(
    name="notationDeclarations573",
    ends={
        Property(name="XSDNotationDeclaration", type=model_xsd_XSDSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchema574", type=XSDNotationDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
annotations575: BinaryAssociation = BinaryAssociation(
    name="annotations575",
    ends={
        Property(name="XSDAnnotation577", type=model_xsd_XSDSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchema576", type=XSDAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)
allDiagnostics578: BinaryAssociation = BinaryAssociation(
    name="allDiagnostics578",
    ends={
        Property(name="XSDDiagnostic580", type=model_xsd_XSDSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchema579", type=XSDDiagnostic, multiplicity=Multiplicity(0, 9999))
    }
)
referencingDirectives581: BinaryAssociation = BinaryAssociation(
    name="referencingDirectives581",
    ends={
        Property(name="XSDSchemaDirective", type=model_xsd_XSDSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchema582", type=XSDSchemaDirective, multiplicity=Multiplicity(0, 9999))
    }
)
fundamentalFacets609: BinaryAssociation = BinaryAssociation(
    name="fundamentalFacets609",
    ends={
        Property(name="XSDFundamentalFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition610", type=XSDFundamentalFacet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rootVersion583: BinaryAssociation = BinaryAssociation(
    name="rootVersion583",
    ends={
        Property(name="XSDSchema585", type=model_xsd_XSDSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchema584", type=XSDSchema, multiplicity=Multiplicity(1, 1))
    }
)
baseTypeDefinition611: BinaryAssociation = BinaryAssociation(
    name="baseTypeDefinition611",
    ends={
        Property(name="XSDSimpleTypeDefinition613", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition612", type=XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
primitiveTypeDefinition614: BinaryAssociation = BinaryAssociation(
    name="primitiveTypeDefinition614",
    ends={
        Property(name="XSDSimpleTypeDefinition616", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition615", type=XSDSimpleTypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
incorporatedVersions589: BinaryAssociation = BinaryAssociation(
    name="incorporatedVersions589",
    ends={
        Property(name="XSDSchema591", type=model_xsd_XSDSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchema590", type=XSDSchema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schemaForSchema592: BinaryAssociation = BinaryAssociation(
    name="schemaForSchema592",
    ends={
        Property(name="XSDSchema594", type=model_xsd_XSDSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchema593", type=XSDSchema, multiplicity=Multiplicity(1, 1))
    }
)
incorporatedSchema595: BinaryAssociation = BinaryAssociation(
    name="incorporatedSchema595",
    ends={
        Property(name="XSDSchema596", type=model_xsd_XSDSchemaCompositor, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchemaCompositor", type=XSDSchema, multiplicity=Multiplicity(0, 1))
    }
)
resolvedSchema597: BinaryAssociation = BinaryAssociation(
    name="resolvedSchema597",
    ends={
        Property(name="XSDSchema598", type=model_xsd_XSDSchemaDirective, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSchemaDirective", type=XSDSchema, multiplicity=Multiplicity(0, 1))
    }
)
contents599: BinaryAssociation = BinaryAssociation(
    name="contents599",
    ends={
        Property(name="XSDSimpleTypeDefinition600", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition", type=XSDSimpleTypeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
facetContents601: BinaryAssociation = BinaryAssociation(
    name="facetContents601",
    ends={
        Property(name="XSDConstrainingFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition602", type=XSDConstrainingFacet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
facets603: BinaryAssociation = BinaryAssociation(
    name="facets603",
    ends={
        Property(name="XSDConstrainingFacet605", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition604", type=XSDConstrainingFacet, multiplicity=Multiplicity(0, 9999))
    }
)
memberTypeDefinitions606: BinaryAssociation = BinaryAssociation(
    name="memberTypeDefinitions606",
    ends={
        Property(name="XSDSimpleTypeDefinition608", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition607", type=XSDSimpleTypeDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
enumerationFacets639: BinaryAssociation = BinaryAssociation(
    name="enumerationFacets639",
    ends={
        Property(name="XSDEnumerationFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition640", type=XSDEnumerationFacet, multiplicity=Multiplicity(0, 9999))
    }
)
patternFacets641: BinaryAssociation = BinaryAssociation(
    name="patternFacets641",
    ends={
        Property(name="XSDPatternFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition642", type=XSDPatternFacet, multiplicity=Multiplicity(0, 9999))
    }
)
cardinalityFacet643: BinaryAssociation = BinaryAssociation(
    name="cardinalityFacet643",
    ends={
        Property(name="XSDCardinalityFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition644", type=XSDCardinalityFacet, multiplicity=Multiplicity(1, 1))
    }
)
itemTypeDefinition617: BinaryAssociation = BinaryAssociation(
    name="itemTypeDefinition617",
    ends={
        Property(name="XSDSimpleTypeDefinition619", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition618", type=XSDSimpleTypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
rootTypeDefinition620: BinaryAssociation = BinaryAssociation(
    name="rootTypeDefinition620",
    ends={
        Property(name="XSDSimpleTypeDefinition622", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition621", type=XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
minFacet623: BinaryAssociation = BinaryAssociation(
    name="minFacet623",
    ends={
        Property(name="XSDMinFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition624", type=XSDMinFacet, multiplicity=Multiplicity(0, 1))
    }
)
maxFacet625: BinaryAssociation = BinaryAssociation(
    name="maxFacet625",
    ends={
        Property(name="XSDMaxFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition626", type=XSDMaxFacet, multiplicity=Multiplicity(0, 1))
    }
)
maxInclusiveFacet627: BinaryAssociation = BinaryAssociation(
    name="maxInclusiveFacet627",
    ends={
        Property(name="XSDMaxInclusiveFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition628", type=XSDMaxInclusiveFacet, multiplicity=Multiplicity(0, 1))
    }
)
minInclusiveFacet629: BinaryAssociation = BinaryAssociation(
    name="minInclusiveFacet629",
    ends={
        Property(name="XSDMinInclusiveFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition630", type=XSDMinInclusiveFacet, multiplicity=Multiplicity(0, 1))
    }
)
minExclusiveFacet631: BinaryAssociation = BinaryAssociation(
    name="minExclusiveFacet631",
    ends={
        Property(name="XSDMinExclusiveFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition632", type=XSDMinExclusiveFacet, multiplicity=Multiplicity(0, 1))
    }
)
maxExclusiveFacet633: BinaryAssociation = BinaryAssociation(
    name="maxExclusiveFacet633",
    ends={
        Property(name="XSDMaxExclusiveFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition634", type=XSDMaxExclusiveFacet, multiplicity=Multiplicity(0, 1))
    }
)
lengthFacet635: BinaryAssociation = BinaryAssociation(
    name="lengthFacet635",
    ends={
        Property(name="XSDLengthFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition636", type=XSDLengthFacet, multiplicity=Multiplicity(0, 1))
    }
)
whiteSpaceFacet637: BinaryAssociation = BinaryAssociation(
    name="whiteSpaceFacet637",
    ends={
        Property(name="XSDWhiteSpaceFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition638", type=XSDWhiteSpaceFacet, multiplicity=Multiplicity(0, 1))
    }
)
effectiveFractionDigitsFacet668: BinaryAssociation = BinaryAssociation(
    name="effectiveFractionDigitsFacet668",
    ends={
        Property(name="XSDFractionDigitsFacet670", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition669", type=XSDFractionDigitsFacet, multiplicity=Multiplicity(0, 1))
    }
)
effectivePatternFacet671: BinaryAssociation = BinaryAssociation(
    name="effectivePatternFacet671",
    ends={
        Property(name="XSDPatternFacet673", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition672", type=XSDPatternFacet, multiplicity=Multiplicity(0, 1))
    }
)
effectiveEnumerationFacet674: BinaryAssociation = BinaryAssociation(
    name="effectiveEnumerationFacet674",
    ends={
        Property(name="XSDEnumerationFacet676", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition675", type=XSDEnumerationFacet, multiplicity=Multiplicity(0, 1))
    }
)
numericFacet645: BinaryAssociation = BinaryAssociation(
    name="numericFacet645",
    ends={
        Property(name="XSDNumericFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition646", type=XSDNumericFacet, multiplicity=Multiplicity(1, 1))
    }
)
maxLengthFacet647: BinaryAssociation = BinaryAssociation(
    name="maxLengthFacet647",
    ends={
        Property(name="XSDMaxLengthFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition648", type=XSDMaxLengthFacet, multiplicity=Multiplicity(0, 1))
    }
)
minLengthFacet649: BinaryAssociation = BinaryAssociation(
    name="minLengthFacet649",
    ends={
        Property(name="XSDMinLengthFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition650", type=XSDMinLengthFacet, multiplicity=Multiplicity(0, 1))
    }
)
totalDigitsFacet651: BinaryAssociation = BinaryAssociation(
    name="totalDigitsFacet651",
    ends={
        Property(name="XSDTotalDigitsFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition652", type=XSDTotalDigitsFacet, multiplicity=Multiplicity(0, 1))
    }
)
fractionDigitsFacet653: BinaryAssociation = BinaryAssociation(
    name="fractionDigitsFacet653",
    ends={
        Property(name="XSDFractionDigitsFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition654", type=XSDFractionDigitsFacet, multiplicity=Multiplicity(0, 1))
    }
)
orderedFacet655: BinaryAssociation = BinaryAssociation(
    name="orderedFacet655",
    ends={
        Property(name="XSDOrderedFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition656", type=XSDOrderedFacet, multiplicity=Multiplicity(1, 1))
    }
)
boundedFacet657: BinaryAssociation = BinaryAssociation(
    name="boundedFacet657",
    ends={
        Property(name="XSDBoundedFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition658", type=XSDBoundedFacet, multiplicity=Multiplicity(1, 1))
    }
)
effectiveMaxFacet659: BinaryAssociation = BinaryAssociation(
    name="effectiveMaxFacet659",
    ends={
        Property(name="XSDMaxFacet661", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition660", type=XSDMaxFacet, multiplicity=Multiplicity(0, 1))
    }
)
effectiveWhiteSpaceFacet662: BinaryAssociation = BinaryAssociation(
    name="effectiveWhiteSpaceFacet662",
    ends={
        Property(name="XSDWhiteSpaceFacet664", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition663", type=XSDWhiteSpaceFacet, multiplicity=Multiplicity(0, 1))
    }
)
effectiveMaxLengthFacet665: BinaryAssociation = BinaryAssociation(
    name="effectiveMaxLengthFacet665",
    ends={
        Property(name="XSDMaxLengthFacet667", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition666", type=XSDMaxLengthFacet, multiplicity=Multiplicity(0, 1))
    }
)
baseType702: BinaryAssociation = BinaryAssociation(
    name="baseType702",
    ends={
        Property(name="XSDTypeDefinition704", type=model_xsd_XSDTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDTypeDefinition703", type=XSDTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
simpleType705: BinaryAssociation = BinaryAssociation(
    name="simpleType705",
    ends={
        Property(name="XSDSimpleTypeDefinition707", type=model_xsd_XSDTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDTypeDefinition706", type=XSDSimpleTypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
effectiveTotalDigitsFacet677: BinaryAssociation = BinaryAssociation(
    name="effectiveTotalDigitsFacet677",
    ends={
        Property(name="XSDTotalDigitsFacet679", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition678", type=XSDTotalDigitsFacet, multiplicity=Multiplicity(0, 1))
    }
)
effectiveMinLengthFacet680: BinaryAssociation = BinaryAssociation(
    name="effectiveMinLengthFacet680",
    ends={
        Property(name="XSDMinLengthFacet682", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition681", type=XSDMinLengthFacet, multiplicity=Multiplicity(0, 1))
    }
)
effectiveLengthFacet683: BinaryAssociation = BinaryAssociation(
    name="effectiveLengthFacet683",
    ends={
        Property(name="XSDLengthFacet685", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition684", type=XSDLengthFacet, multiplicity=Multiplicity(0, 1))
    }
)
effectiveMinFacet686: BinaryAssociation = BinaryAssociation(
    name="effectiveMinFacet686",
    ends={
        Property(name="XSDMinFacet688", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition687", type=XSDMinFacet, multiplicity=Multiplicity(0, 1))
    }
)
syntheticFacets689: BinaryAssociation = BinaryAssociation(
    name="syntheticFacets689",
    ends={
        Property(name="XSDFacet", type=model_xsd_XSDSimpleTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDSimpleTypeDefinition690", type=XSDFacet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation691: BinaryAssociation = BinaryAssociation(
    name="annotation691",
    ends={
        Property(name="XSDAnnotation692", type=model_xsd_XSDTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDTypeDefinition", type=XSDAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
derivationAnnotation693: BinaryAssociation = BinaryAssociation(
    name="derivationAnnotation693",
    ends={
        Property(name="XSDAnnotation695", type=model_xsd_XSDTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDTypeDefinition694", type=XSDAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations696: BinaryAssociation = BinaryAssociation(
    name="annotations696",
    ends={
        Property(name="XSDAnnotation698", type=model_xsd_XSDTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDTypeDefinition697", type=XSDAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)
rootType699: BinaryAssociation = BinaryAssociation(
    name="rootType699",
    ends={
        Property(name="XSDTypeDefinition701", type=model_xsd_XSDTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDTypeDefinition700", type=XSDTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
complexType708: BinaryAssociation = BinaryAssociation(
    name="complexType708",
    ends={
        Property(name="XSDParticle710", type=model_xsd_XSDTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDTypeDefinition709", type=XSDParticle, multiplicity=Multiplicity(0, 1))
    }
)
annotation711: BinaryAssociation = BinaryAssociation(
    name="annotation711",
    ends={
        Property(name="XSDAnnotation712", type=model_xsd_XSDWildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDWildcard", type=XSDAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations713: BinaryAssociation = BinaryAssociation(
    name="annotations713",
    ends={
        Property(name="XSDAnnotation715", type=model_xsd_XSDWildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDWildcard714", type=XSDAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)
annotation716: BinaryAssociation = BinaryAssociation(
    name="annotation716",
    ends={
        Property(name="XSDAnnotation717", type=model_xsd_XSDXPathDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xsd_XSDXPathDefinition", type=XSDAnnotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wsdlPart718: BinaryAssociation = BinaryAssociation(
    name="wsdlPart718",
    ends={
        Property(name="Part719", type=model_messageproperties_PropertyAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="model_messageproperties_PropertyAlias", type=Part, multiplicity=Multiplicity(1, 1))
    }
)
query720: BinaryAssociation = BinaryAssociation(
    name="query720",
    ends={
        Property(name="Query", type=model_messageproperties_PropertyAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="model_messageproperties_PropertyAlias721", type=Query, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
role722: BinaryAssociation = BinaryAssociation(
    name="role722",
    ends={
        Property(name="Role723", type=model_partnerlinktype_PartnerLinkType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_partnerlinktype_PartnerLinkType", type=Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_model_Process_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Process)
gen_model_PartnerLink_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_PartnerLink)
gen_model_FaultHandler_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_FaultHandler)
gen_model_Activity_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Activity)
gen_model_Link_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Link)
gen_model_CorrelationSet_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_CorrelationSet)
gen_model_Invoke_PartnerActivity = Generalization(general=PartnerActivity, specific=model_Invoke)
gen_model_Catch_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Catch)
gen_model_Reply_PartnerActivity = Generalization(general=PartnerActivity, specific=model_Reply)
gen_model_Reply_Activity = Generalization(general=Activity, specific=model_Reply)
gen_model_PartnerActivity_Activity = Generalization(general=Activity, specific=model_PartnerActivity)
gen_model_Pick_Activity = Generalization(general=Activity, specific=model_Pick)
gen_model_Receive_PartnerActivity = Generalization(general=PartnerActivity, specific=model_Receive)
gen_model_Exit_Activity = Generalization(general=Activity, specific=model_Exit)
gen_model_Throw_Activity = Generalization(general=Activity, specific=model_Throw)
gen_model_Wait_Activity = Generalization(general=Activity, specific=model_Wait)
gen_model_Empty_Activity = Generalization(general=Activity, specific=model_Empty)
gen_model_Sequence_Activity = Generalization(general=Activity, specific=model_Sequence)
gen_model_While_Activity = Generalization(general=Activity, specific=model_While)
gen_model_Extension_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Extension)
gen_model_Flow_Activity = Generalization(general=Activity, specific=model_Flow)
gen_model_OnAlarm_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_OnAlarm)
gen_model_Assign_Activity = Generalization(general=Activity, specific=model_Assign)
gen_model_Copy_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Copy)
gen_model_Scope_Activity = Generalization(general=Activity, specific=model_Scope)
gen_model_CompensateScope_Activity = Generalization(general=Activity, specific=model_CompensateScope)
gen_model_CompensationHandler_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_CompensationHandler)
gen_model_To_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_To)
gen_model_To_AbstractAssignBound = Generalization(general=AbstractAssignBound, specific=model_To)
gen_model_From_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_From)
gen_model_From_AbstractAssignBound = Generalization(general=AbstractAssignBound, specific=model_From)
gen_model_OnMessage_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_OnMessage)
gen_model_PartnerLinks_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_PartnerLinks)
gen_model_Expression_ExtensibilityElement = Generalization(general=ExtensibilityElement, specific=model_Expression)
gen_model_BooleanExpression_Expression = Generalization(general=Expression, specific=model_BooleanExpression)
gen_model_Correlation_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Correlation)
gen_model_MessageExchange_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_MessageExchange)
gen_model_EventHandler_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_EventHandler)
gen_model_Source_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Source)
gen_model_Target_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Target)
gen_model_MessageExchanges_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_MessageExchanges)
gen_model_Variables_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Variables)
gen_model_CorrelationSets_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_CorrelationSets)
gen_model_Links_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Links)
gen_model_CatchAll_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_CatchAll)
gen_model_Correlations_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Correlations)
gen_model_Variable_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Variable)
gen_model_Targets_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Targets)
gen_model_UnknownExtensibilityAttribute_UnknownExtensibilityElement = Generalization(general=UnknownExtensibilityElement, specific=model_UnknownExtensibilityAttribute)
gen_model_OnEvent_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_OnEvent)
gen_model_Import_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Import)
gen_model_Rethrow_Activity = Generalization(general=Activity, specific=model_Rethrow)
gen_model_Condition_Expression = Generalization(general=Expression, specific=model_Condition)
gen_model_Sources_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Sources)
gen_model_Query_WSDLElement = Generalization(general=WSDLElement, specific=model_Query)
gen_model_ServiceRef_ExtensibleElement = Generalization(general=ExtensibleElement, specific=model_ServiceRef)
gen_model_Extensions_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Extensions)
gen_model_ExtensionActivity_Activity = Generalization(general=Activity, specific=model_ExtensionActivity)
gen_model_FromPart_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_FromPart)
gen_model_ToPart_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_ToPart)
gen_model_OpaqueActivity_Activity = Generalization(general=Activity, specific=model_OpaqueActivity)
gen_model_ForEach_Activity = Generalization(general=Activity, specific=model_ForEach)
gen_model_Else_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Else)
gen_model_RepeatUntil_Activity = Generalization(general=Activity, specific=model_RepeatUntil)
gen_model_TerminationHandler_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_TerminationHandler)
gen_model_Validate_Activity = Generalization(general=Activity, specific=model_Validate)
gen_model_If_Activity = Generalization(general=Activity, specific=model_If)
gen_model_ElseIf_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_ElseIf)
gen_model_CompletionCondition_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_CompletionCondition)
gen_model_Branches_Expression = Generalization(general=Expression, specific=model_Branches)
gen_model_BPELExtensibleElement_ExtensibleElement = Generalization(general=ExtensibleElement, specific=model_BPELExtensibleElement)
gen_model_Documentation_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_Documentation)
gen_model_Compensate_Activity = Generalization(general=Activity, specific=model_Compensate)
gen_model_FromParts_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_FromParts)
gen_model_ToParts_BPELExtensibleElement = Generalization(general=BPELExtensibleElement, specific=model_ToParts)
gen_model_wsdl_PortType_wsdl_ExtensibleElement = Generalization(general=wsdl_ExtensibleElement, specific=model_wsdl_PortType)
gen_model_wsdl_PortType_wsdl_IPortType = Generalization(general=wsdl_IPortType, specific=model_wsdl_PortType)
gen_model_wsdl_Operation_wsdl_ExtensibleElement = Generalization(general=wsdl_ExtensibleElement, specific=model_wsdl_Operation)
gen_model_wsdl_Operation_wsdl_IOperation = Generalization(general=wsdl_IOperation, specific=model_wsdl_Operation)
gen_model_wsdl_Message_wsdl_ExtensibleElement = Generalization(general=wsdl_ExtensibleElement, specific=model_wsdl_Message)
gen_model_wsdl_Message_wsdl_IMessage = Generalization(general=wsdl_IMessage, specific=model_wsdl_Message)
gen_model_wsdl_Part_wsdl_ExtensibleElement = Generalization(general=wsdl_ExtensibleElement, specific=model_wsdl_Part)
gen_model_wsdl_Part_wsdl_IPart = Generalization(general=wsdl_IPart, specific=model_wsdl_Part)
gen_model_wsdl_Binding_wsdl_ExtensibleElement = Generalization(general=wsdl_ExtensibleElement, specific=model_wsdl_Binding)
gen_model_wsdl_Binding_wsdl_IBinding = Generalization(general=wsdl_IBinding, specific=model_wsdl_Binding)
gen_model_wsdl_BindingOperation_wsdl_ExtensibleElement = Generalization(general=wsdl_ExtensibleElement, specific=model_wsdl_BindingOperation)
gen_model_wsdl_BindingOperation_wsdl_IBindingOperation = Generalization(general=wsdl_IBindingOperation, specific=model_wsdl_BindingOperation)
gen_model_wsdl_Service_wsdl_ExtensibleElement = Generalization(general=wsdl_ExtensibleElement, specific=model_wsdl_Service)
gen_model_wsdl_Service_wsdl_IService = Generalization(general=wsdl_IService, specific=model_wsdl_Service)
gen_model_wsdl_Port_wsdl_ExtensibleElement = Generalization(general=wsdl_ExtensibleElement, specific=model_wsdl_Port)
gen_model_wsdl_Port_wsdl_IPort = Generalization(general=wsdl_IPort, specific=model_wsdl_Port)
gen_model_wsdl_ExtensibilityElement_wsdl_WSDLElement = Generalization(general=wsdl_WSDLElement, specific=model_wsdl_ExtensibilityElement)
gen_model_wsdl_ExtensibilityElement_wsdl_IExtensibilityElement = Generalization(general=wsdl_IExtensibilityElement, specific=model_wsdl_ExtensibilityElement)
gen_model_wsdl_ExtensibleElement_wsdl_WSDLElement = Generalization(general=wsdl_WSDLElement, specific=model_wsdl_ExtensibleElement)
gen_model_wsdl_ExtensibleElement_wsdl_IElementExtensible = Generalization(general=wsdl_IElementExtensible, specific=model_wsdl_ExtensibleElement)
gen_model_wsdl_ExtensibleElement_wsdl_IAttributeExtensible = Generalization(general=wsdl_IAttributeExtensible, specific=model_wsdl_ExtensibleElement)
gen_model_wsdl_Definition_wsdl_ExtensibleElement = Generalization(general=wsdl_ExtensibleElement, specific=model_wsdl_Definition)
gen_model_wsdl_Definition_wsdl_IDefinition = Generalization(general=wsdl_IDefinition, specific=model_wsdl_Definition)
gen_model_wsdl_Input_wsdl_MessageReference = Generalization(general=wsdl_MessageReference, specific=model_wsdl_Input)
gen_model_wsdl_Input_wsdl_IInput = Generalization(general=wsdl_IInput, specific=model_wsdl_Input)
gen_model_wsdl_Import_wsdl_ExtensibleElement = Generalization(general=wsdl_ExtensibleElement, specific=model_wsdl_Import)
gen_model_wsdl_Import_wsdl_IImport = Generalization(general=wsdl_IImport, specific=model_wsdl_Import)
gen_model_wsdl_Output_wsdl_MessageReference = Generalization(general=wsdl_MessageReference, specific=model_wsdl_Output)
gen_model_wsdl_Output_wsdl_IOutput = Generalization(general=wsdl_IOutput, specific=model_wsdl_Output)
gen_model_wsdl_Fault_wsdl_MessageReference = Generalization(general=wsdl_MessageReference, specific=model_wsdl_Fault)
gen_model_wsdl_Fault_wsdl_IFault = Generalization(general=wsdl_IFault, specific=model_wsdl_Fault)
gen_model_wsdl_BindingInput_wsdl_ExtensibleElement = Generalization(general=wsdl_ExtensibleElement, specific=model_wsdl_BindingInput)
gen_model_wsdl_BindingInput_wsdl_IBindingInput = Generalization(general=wsdl_IBindingInput, specific=model_wsdl_BindingInput)
gen_model_wsdl_BindingOutput_wsdl_ExtensibleElement = Generalization(general=wsdl_ExtensibleElement, specific=model_wsdl_BindingOutput)
gen_model_wsdl_BindingOutput_wsdl_IBindingOutput = Generalization(general=wsdl_IBindingOutput, specific=model_wsdl_BindingOutput)
gen_model_wsdl_BindingFault_wsdl_ExtensibleElement = Generalization(general=wsdl_ExtensibleElement, specific=model_wsdl_BindingFault)
gen_model_wsdl_BindingFault_wsdl_IBindingFault = Generalization(general=wsdl_IBindingFault, specific=model_wsdl_BindingFault)
gen_model_wsdl_IMessage_IElementExtensible = Generalization(general=IElementExtensible, specific=model_wsdl_IMessage)
gen_model_wsdl_IPortType_IAttributeExtensible = Generalization(general=IAttributeExtensible, specific=model_wsdl_IPortType)
gen_model_wsdl_IOperation_IElementExtensible = Generalization(general=IElementExtensible, specific=model_wsdl_IOperation)
gen_model_wsdl_IInput_IAttributeExtensible = Generalization(general=IAttributeExtensible, specific=model_wsdl_IInput)
gen_model_wsdl_IOutput_IAttributeExtensible = Generalization(general=IAttributeExtensible, specific=model_wsdl_IOutput)
gen_model_wsdl_IFault_IAttributeExtensible = Generalization(general=IAttributeExtensible, specific=model_wsdl_IFault)
gen_model_wsdl_IBindingInput_IElementExtensible = Generalization(general=IElementExtensible, specific=model_wsdl_IBindingInput)
gen_model_wsdl_IPart_IAttributeExtensible = Generalization(general=IAttributeExtensible, specific=model_wsdl_IPart)
gen_model_wsdl_IService_IElementExtensible = Generalization(general=IElementExtensible, specific=model_wsdl_IService)
gen_model_wsdl_IPort_IElementExtensible = Generalization(general=IElementExtensible, specific=model_wsdl_IPort)
gen_model_wsdl_IBinding_IElementExtensible = Generalization(general=IElementExtensible, specific=model_wsdl_IBinding)
gen_model_wsdl_IBindingOperation_IElementExtensible = Generalization(general=IElementExtensible, specific=model_wsdl_IBindingOperation)
gen_model_wsdl_IBindingOutput_IElementExtensible = Generalization(general=IElementExtensible, specific=model_wsdl_IBindingOutput)
gen_model_wsdl_IBindingFault_IElementExtensible = Generalization(general=IElementExtensible, specific=model_wsdl_IBindingFault)
gen_model_wsdl_IDefinition_IElementExtensible = Generalization(general=IElementExtensible, specific=model_wsdl_IDefinition)
gen_model_wsdl_UnknownExtensibilityElement_ExtensibilityElement = Generalization(general=ExtensibilityElement, specific=model_wsdl_UnknownExtensibilityElement)
gen_model_wsdl_XSDSchemaExtensibilityElement_wsdl_ExtensibilityElement = Generalization(general=wsdl_ExtensibilityElement, specific=model_wsdl_XSDSchemaExtensibilityElement)
gen_model_wsdl_XSDSchemaExtensibilityElement_wsdl_ISchema = Generalization(general=wsdl_ISchema, specific=model_wsdl_XSDSchemaExtensibilityElement)
gen_model_wsdl_IImport_IAttributeExtensible = Generalization(general=IAttributeExtensible, specific=model_wsdl_IImport)
gen_model_wsdl_Types_wsdl_ExtensibleElement = Generalization(general=wsdl_ExtensibleElement, specific=model_wsdl_Types)
gen_model_wsdl_Types_wsdl_ITypes = Generalization(general=wsdl_ITypes, specific=model_wsdl_Types)
gen_model_wsdl_MessageReference_ExtensibleElement = Generalization(general=ExtensibleElement, specific=model_wsdl_MessageReference)
gen_model_wsdl_ISchema_IExtensibilityElement = Generalization(general=IExtensibilityElement, specific=model_wsdl_ISchema)
gen_model_xsd_XSDAnnotation_xsd_XSDComponent = Generalization(general=xsd_XSDComponent, specific=model_xsd_XSDAnnotation)
gen_model_xsd_XSDAnnotation_xsd_XSDRedefineContent = Generalization(general=xsd_XSDRedefineContent, specific=model_xsd_XSDAnnotation)
gen_model_xsd_XSDAttributeDeclaration_xsd_XSDFeature = Generalization(general=xsd_XSDFeature, specific=model_xsd_XSDAttributeDeclaration)
gen_model_xsd_XSDAttributeDeclaration_xsd_XSDSchemaContent = Generalization(general=xsd_XSDSchemaContent, specific=model_xsd_XSDAttributeDeclaration)
gen_model_xsd_XSDBoundedFacet_XSDFundamentalFacet = Generalization(general=XSDFundamentalFacet, specific=model_xsd_XSDBoundedFacet)
gen_model_xsd_XSDCardinalityFacet_XSDFundamentalFacet = Generalization(general=XSDFundamentalFacet, specific=model_xsd_XSDCardinalityFacet)
gen_model_xsd_XSDComplexTypeContent_XSDComponent = Generalization(general=XSDComponent, specific=model_xsd_XSDComplexTypeContent)
gen_model_xsd_XSDComplexTypeDefinition_xsd_XSDTypeDefinition = Generalization(general=xsd_XSDTypeDefinition, specific=model_xsd_XSDComplexTypeDefinition)
gen_model_xsd_XSDAttributeGroupContent_XSDConcreteComponent = Generalization(general=XSDConcreteComponent, specific=model_xsd_XSDAttributeGroupContent)
gen_model_xsd_XSDAttributeGroupDefinition_xsd_XSDRedefinableComponent = Generalization(general=xsd_XSDRedefinableComponent, specific=model_xsd_XSDAttributeGroupDefinition)
gen_model_xsd_XSDAttributeGroupDefinition_xsd_XSDAttributeGroupContent = Generalization(general=xsd_XSDAttributeGroupContent, specific=model_xsd_XSDAttributeGroupDefinition)
gen_model_xsd_XSDAttributeGroupDefinition_xsd_XSDRedefineContent = Generalization(general=xsd_XSDRedefineContent, specific=model_xsd_XSDAttributeGroupDefinition)
gen_model_xsd_XSDAttributeUse_xsd_XSDComponent = Generalization(general=xsd_XSDComponent, specific=model_xsd_XSDAttributeUse)
gen_model_xsd_XSDAttributeUse_xsd_XSDAttributeGroupContent = Generalization(general=xsd_XSDAttributeGroupContent, specific=model_xsd_XSDAttributeUse)
gen_model_xsd_XSDComplexTypeDefinition_xsd_XSDScope = Generalization(general=xsd_XSDScope, specific=model_xsd_XSDComplexTypeDefinition)
gen_model_xsd_XSDElementDeclaration_xsd_XSDSchemaContent = Generalization(general=xsd_XSDSchemaContent, specific=model_xsd_XSDElementDeclaration)
gen_model_xsd_XSDElementDeclaration_xsd_XSDTerm = Generalization(general=xsd_XSDTerm, specific=model_xsd_XSDElementDeclaration)
gen_model_xsd_XSDComponent_XSDConcreteComponent = Generalization(general=XSDConcreteComponent, specific=model_xsd_XSDComponent)
gen_model_xsd_XSDConstrainingFacet_XSDFacet = Generalization(general=XSDFacet, specific=model_xsd_XSDConstrainingFacet)
gen_model_xsd_XSDDiagnostic_XSDConcreteComponent = Generalization(general=XSDConcreteComponent, specific=model_xsd_XSDDiagnostic)
gen_model_xsd_XSDElementDeclaration_xsd_XSDFeature = Generalization(general=xsd_XSDFeature, specific=model_xsd_XSDElementDeclaration)
gen_model_xsd_XSDFeature_XSDNamedComponent = Generalization(general=XSDNamedComponent, specific=model_xsd_XSDFeature)
gen_model_xsd_XSDEnumerationFacet_XSDRepeatableFacet = Generalization(general=XSDRepeatableFacet, specific=model_xsd_XSDEnumerationFacet)
gen_model_xsd_XSDFacet_XSDComponent = Generalization(general=XSDComponent, specific=model_xsd_XSDFacet)
gen_model_xsd_XSDMaxExclusiveFacet_XSDMaxFacet = Generalization(general=XSDMaxFacet, specific=model_xsd_XSDMaxExclusiveFacet)
gen_model_xsd_XSDMaxFacet_XSDFixedFacet = Generalization(general=XSDFixedFacet, specific=model_xsd_XSDMaxFacet)
gen_model_xsd_XSDFixedFacet_XSDConstrainingFacet = Generalization(general=XSDConstrainingFacet, specific=model_xsd_XSDFixedFacet)
gen_model_xsd_XSDFractionDigitsFacet_XSDFixedFacet = Generalization(general=XSDFixedFacet, specific=model_xsd_XSDFractionDigitsFacet)
gen_model_xsd_XSDFundamentalFacet_XSDFacet = Generalization(general=XSDFacet, specific=model_xsd_XSDFundamentalFacet)
gen_model_xsd_XSDIdentityConstraintDefinition_XSDNamedComponent = Generalization(general=XSDNamedComponent, specific=model_xsd_XSDIdentityConstraintDefinition)
gen_model_xsd_XSDImport_XSDSchemaDirective = Generalization(general=XSDSchemaDirective, specific=model_xsd_XSDImport)
gen_model_xsd_XSDInclude_XSDSchemaCompositor = Generalization(general=XSDSchemaCompositor, specific=model_xsd_XSDInclude)
gen_model_xsd_XSDLengthFacet_XSDFixedFacet = Generalization(general=XSDFixedFacet, specific=model_xsd_XSDLengthFacet)
gen_model_xsd_XSDNotationDeclaration_xsd_XSDNamedComponent = Generalization(general=xsd_XSDNamedComponent, specific=model_xsd_XSDNotationDeclaration)
gen_model_xsd_XSDMaxInclusiveFacet_XSDMaxFacet = Generalization(general=XSDMaxFacet, specific=model_xsd_XSDMaxInclusiveFacet)
gen_model_xsd_XSDMaxLengthFacet_XSDFixedFacet = Generalization(general=XSDFixedFacet, specific=model_xsd_XSDMaxLengthFacet)
gen_model_xsd_XSDMinExclusiveFacet_XSDMinFacet = Generalization(general=XSDMinFacet, specific=model_xsd_XSDMinExclusiveFacet)
gen_model_xsd_XSDMinFacet_XSDFixedFacet = Generalization(general=XSDFixedFacet, specific=model_xsd_XSDMinFacet)
gen_model_xsd_XSDMinInclusiveFacet_XSDMinFacet = Generalization(general=XSDMinFacet, specific=model_xsd_XSDMinInclusiveFacet)
gen_model_xsd_XSDMinLengthFacet_XSDFixedFacet = Generalization(general=XSDFixedFacet, specific=model_xsd_XSDMinLengthFacet)
gen_model_xsd_XSDModelGroup_XSDTerm = Generalization(general=XSDTerm, specific=model_xsd_XSDModelGroup)
gen_model_xsd_XSDModelGroupDefinition_xsd_XSDRedefinableComponent = Generalization(general=xsd_XSDRedefinableComponent, specific=model_xsd_XSDModelGroupDefinition)
gen_model_xsd_XSDModelGroupDefinition_xsd_XSDParticleContent = Generalization(general=xsd_XSDParticleContent, specific=model_xsd_XSDModelGroupDefinition)
gen_model_xsd_XSDModelGroupDefinition_xsd_XSDRedefineContent = Generalization(general=xsd_XSDRedefineContent, specific=model_xsd_XSDModelGroupDefinition)
gen_model_xsd_XSDNamedComponent_XSDComponent = Generalization(general=XSDComponent, specific=model_xsd_XSDNamedComponent)
gen_model_xsd_XSDSchema_XSDScope = Generalization(general=XSDScope, specific=model_xsd_XSDSchema)
gen_model_xsd_XSDNotationDeclaration_xsd_XSDSchemaContent = Generalization(general=xsd_XSDSchemaContent, specific=model_xsd_XSDNotationDeclaration)
gen_model_xsd_XSDNumericFacet_XSDFundamentalFacet = Generalization(general=XSDFundamentalFacet, specific=model_xsd_XSDNumericFacet)
gen_model_xsd_XSDOrderedFacet_XSDFundamentalFacet = Generalization(general=XSDFundamentalFacet, specific=model_xsd_XSDOrderedFacet)
gen_model_xsd_XSDParticle_XSDComplexTypeContent = Generalization(general=XSDComplexTypeContent, specific=model_xsd_XSDParticle)
gen_model_xsd_XSDParticleContent_XSDConcreteComponent = Generalization(general=XSDConcreteComponent, specific=model_xsd_XSDParticleContent)
gen_model_xsd_XSDPatternFacet_XSDRepeatableFacet = Generalization(general=XSDRepeatableFacet, specific=model_xsd_XSDPatternFacet)
gen_model_xsd_XSDRedefinableComponent_xsd_XSDNamedComponent = Generalization(general=xsd_XSDNamedComponent, specific=model_xsd_XSDRedefinableComponent)
gen_model_xsd_XSDRedefinableComponent_xsd_XSDRedefineContent = Generalization(general=xsd_XSDRedefineContent, specific=model_xsd_XSDRedefinableComponent)
gen_model_xsd_XSDRedefineContent_XSDSchemaContent = Generalization(general=XSDSchemaContent, specific=model_xsd_XSDRedefineContent)
gen_model_xsd_XSDRedefine_XSDSchemaCompositor = Generalization(general=XSDSchemaCompositor, specific=model_xsd_XSDRedefine)
gen_model_xsd_XSDRepeatableFacet_XSDConstrainingFacet = Generalization(general=XSDConstrainingFacet, specific=model_xsd_XSDRepeatableFacet)
gen_model_xsd_XSDSchemaCompositor_XSDSchemaDirective = Generalization(general=XSDSchemaDirective, specific=model_xsd_XSDSchemaCompositor)
gen_model_xsd_XSDSchemaContent_XSDConcreteComponent = Generalization(general=XSDConcreteComponent, specific=model_xsd_XSDSchemaContent)
gen_model_xsd_XSDSchemaDirective_XSDSchemaContent = Generalization(general=XSDSchemaContent, specific=model_xsd_XSDSchemaDirective)
gen_model_xsd_XSDScope_XSDComponent = Generalization(general=XSDComponent, specific=model_xsd_XSDScope)
gen_model_xsd_XSDSimpleTypeDefinition_xsd_XSDTypeDefinition = Generalization(general=xsd_XSDTypeDefinition, specific=model_xsd_XSDSimpleTypeDefinition)
gen_model_xsd_XSDSimpleTypeDefinition_xsd_XSDComplexTypeContent = Generalization(general=xsd_XSDComplexTypeContent, specific=model_xsd_XSDSimpleTypeDefinition)
gen_model_xsd_XSDTerm_xsd_XSDComponent = Generalization(general=xsd_XSDComponent, specific=model_xsd_XSDTerm)
gen_model_xsd_XSDTerm_xsd_XSDParticleContent = Generalization(general=xsd_XSDParticleContent, specific=model_xsd_XSDTerm)
gen_model_xsd_XSDTotalDigitsFacet_XSDFixedFacet = Generalization(general=XSDFixedFacet, specific=model_xsd_XSDTotalDigitsFacet)
gen_model_xsd_XSDTypeDefinition_xsd_XSDRedefinableComponent = Generalization(general=xsd_XSDRedefinableComponent, specific=model_xsd_XSDTypeDefinition)
gen_model_xsd_XSDTypeDefinition_xsd_XSDRedefineContent = Generalization(general=xsd_XSDRedefineContent, specific=model_xsd_XSDTypeDefinition)
gen_model_xsd_XSDWhiteSpaceFacet_XSDFixedFacet = Generalization(general=XSDFixedFacet, specific=model_xsd_XSDWhiteSpaceFacet)
gen_model_xsd_XSDWildcard_XSDTerm = Generalization(general=XSDTerm, specific=model_xsd_XSDWildcard)
gen_model_xsd_XSDXPathDefinition_XSDComponent = Generalization(general=XSDComponent, specific=model_xsd_XSDXPathDefinition)
gen_model_partnerlinktype_Role_ExtensibilityElement = Generalization(general=ExtensibilityElement, specific=model_partnerlinktype_Role)
gen_model_messageproperties_Property_ExtensibilityElement = Generalization(general=ExtensibilityElement, specific=model_messageproperties_Property)
gen_model_messageproperties_PropertyAlias_ExtensibilityElement = Generalization(general=ExtensibilityElement, specific=model_messageproperties_PropertyAlias)
gen_model_messageproperties_Query_ExtensibilityElement = Generalization(general=ExtensibilityElement, specific=model_messageproperties_Query)
gen_model_partnerlinktype_PartnerLinkType_ExtensibilityElement = Generalization(general=ExtensibilityElement, specific=model_partnerlinktype_PartnerLinkType)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Process, BPELExtensibleElement, model_MessageExchanges, model_PartnerLinks, model_Variables, model_Activity, model_FaultHandler, model_EventHandler, model_CorrelationSets, model_Import, model_Extensions, model_PartnerLink, Role, PartnerLinkType, model_Catch, model_CatchAll, model_ToParts, model_Link, model_Targets, model_Sources, model_CorrelationSet, Property_, model_Invoke, PartnerActivity, model_Variable, model_CompensationHandler, model_FromParts, PortType, model_Source, model_Target, Message, XSDElementDeclaration, model_Reply, Activity, model_MessageExchange, model_PartnerActivity, model_Pick, model_Correlations, Operation, model_Receive, model_Exit, model_Throw, model_Wait, model_Expression, model_Empty, model_Sequence, model_While, model_Condition, model_Extension, model_OnMessage, model_OnAlarm, model_Flow, model_Links, model_CompletionCondition, model_Assign, model_Copy, model_To, model_From, Part, model_Scope, model_TerminationHandler, model_CompensateScope, model_AbstractAssignBound, model_Query, AbstractAssignBound, model_ServiceRef, XSDTypeDefinition, ExtensibilityElement, model_BooleanExpression, Expression, model_Correlation, model_OnEvent, model_UnknownExtensibilityAttribute, UnknownExtensibilityElement, model_Rethrow, WSDLElement, ExtensibleElement, model_ExtensionActivity, model_FromPart, model_ToPart, model_OpaqueActivity, model_ForEach, model_RepeatUntil, model_Validate, model_If, model_ElseIf, model_Else, model_Branches, model_BPELExtensibleElement, model_Documentation, model_Compensate, model_wsdl_WSDLElement, model_wsdl_PortType, wsdl_ExtensibleElement, wsdl_IPortType, model_wsdl_Operation, wsdl_IOperation, Input, Output, Fault, model_wsdl_Message, wsdl_IMessage, model_wsdl_Part, wsdl_IPart, model_wsdl_Binding, wsdl_IBinding, model_wsdl_Definition, BindingOperation, model_wsdl_BindingOperation, wsdl_IBindingOperation, BindingInput, BindingOutput, BindingFault, model_wsdl_Service, wsdl_IService, Port, model_wsdl_Port, wsdl_IPort, Binding, model_wsdl_ExtensibilityElement, wsdl_WSDLElement, wsdl_IExtensibilityElement, wsdl_IElementExtensible, wsdl_IAttributeExtensible, wsdl_IDefinition, model_wsdl_Input, wsdl_MessageReference, wsdl_IInput, Import, Types, Service, Namespace, model_wsdl_Import, wsdl_IImport, Definition, XSDSchema, model_wsdl_ExtensibleElement, model_wsdl_Namespace, model_wsdl_Output, wsdl_IOutput, model_wsdl_Fault, wsdl_IFault, model_wsdl_BindingInput, wsdl_IBindingInput, model_wsdl_BindingOutput, wsdl_IBindingOutput, model_wsdl_BindingFault, wsdl_IBindingFault, model_wsdl_IMessage, model_wsdl_IPortType, IAttributeExtensible, model_wsdl_IOperation, IElementExtensible, model_wsdl_IInput, model_wsdl_IOutput, model_wsdl_IFault, model_wsdl_IBindingInput, model_wsdl_IPart, model_wsdl_IService, model_wsdl_IPort, model_wsdl_IBinding, model_wsdl_IBindingOperation, model_wsdl_IBindingOutput, model_wsdl_IBindingFault, model_wsdl_IExtensibilityElement, model_wsdl_IDefinition, model_wsdl_UnknownExtensibilityElement, model_wsdl_XSDSchemaExtensibilityElement, wsdl_ExtensibilityElement, wsdl_ISchema, model_wsdl_IImport, model_wsdl_IList, model_wsdl_IMap, model_wsdl_IURL, model_wsdl_IExtensionRegistry, model_wsdl_Types, wsdl_ITypes, model_wsdl_IIterator, model_wsdl_ITypes, XSDSimpleTypeDefinition, XSDAttributeDeclaration, model_wsdl_MessageReference, model_wsdl_IElementExtensible, model_wsdl_IAttributeExtensible, model_wsdl_IObject, model_wsdl_ISchema, IExtensibilityElement, model_xsd_XSDAnnotation, xsd_XSDComponent, xsd_XSDRedefineContent, model_xsd_XSDAttributeDeclaration, xsd_XSDFeature, xsd_XSDSchemaContent, XSDAnnotation, XSDFundamentalFacet, model_xsd_XSDCardinalityFacet, model_xsd_XSDComplexTypeContent, XSDComponent, model_xsd_XSDComplexTypeDefinition, xsd_XSDTypeDefinition, model_xsd_XSDAttributeGroupContent, XSDConcreteComponent, model_xsd_XSDAttributeGroupDefinition, xsd_XSDRedefinableComponent, xsd_XSDAttributeGroupContent, XSDAttributeGroupContent, XSDAttributeUse, XSDWildcard, XSDAttributeGroupDefinition, model_xsd_XSDAttributeUse, model_xsd_XSDBoundedFacet, XSDParticle, xsd_XSDScope, XSDComplexTypeContent, xsd_XSDTerm, model_xsd_XSDComponent, model_xsd_XSDConcreteComponent, XSDDiagnostic, model_xsd_XSDConstrainingFacet, XSDFacet, model_xsd_XSDDiagnostic, model_xsd_XSDElementDeclaration, XSDIdentityConstraintDefinition, model_xsd_XSDEnumerationFacet, XSDRepeatableFacet, model_xsd_XSDFacet, model_xsd_XSDFeature, XSDNamedComponent, model_xsd_XSDMaxExclusiveFacet, XSDMaxFacet, model_xsd_XSDMaxFacet, XSDScope, XSDFeature, model_xsd_XSDFixedFacet, XSDConstrainingFacet, model_xsd_XSDFractionDigitsFacet, XSDFixedFacet, model_xsd_XSDFundamentalFacet, model_xsd_XSDIdentityConstraintDefinition, XSDXPathDefinition, model_xsd_XSDImport, XSDSchemaDirective, model_xsd_XSDInclude, XSDSchemaCompositor, model_xsd_XSDLengthFacet, model_xsd_XSDNotationDeclaration, xsd_XSDNamedComponent, model_xsd_XSDMaxInclusiveFacet, model_xsd_XSDMaxLengthFacet, model_xsd_XSDMinExclusiveFacet, XSDMinFacet, model_xsd_XSDMinFacet, model_xsd_XSDMinInclusiveFacet, model_xsd_XSDMinLengthFacet, model_xsd_XSDModelGroup, XSDTerm, model_xsd_XSDModelGroupDefinition, xsd_XSDParticleContent, XSDModelGroup, XSDModelGroupDefinition, model_xsd_XSDNamedComponent, model_xsd_XSDSchema, model_xsd_XSDNumericFacet, model_xsd_XSDOrderedFacet, model_xsd_XSDParticle, XSDParticleContent, model_xsd_XSDParticleContent, model_xsd_XSDPatternFacet, model_xsd_XSDRedefinableComponent, model_xsd_XSDRedefineContent, XSDSchemaContent, model_xsd_XSDRedefine, XSDRedefineContent, model_xsd_XSDRepeatableFacet, XSDNotationDeclaration, model_xsd_XSDSchemaCompositor, model_xsd_XSDSchemaContent, model_xsd_XSDSchemaDirective, model_xsd_XSDScope, model_xsd_XSDSimpleTypeDefinition, xsd_XSDComplexTypeContent, XSDPatternFacet, XSDCardinalityFacet, XSDMaxInclusiveFacet, XSDMinInclusiveFacet, XSDMinExclusiveFacet, XSDMaxExclusiveFacet, XSDLengthFacet, XSDWhiteSpaceFacet, XSDEnumerationFacet, XSDNumericFacet, XSDMaxLengthFacet, XSDMinLengthFacet, XSDTotalDigitsFacet, XSDFractionDigitsFacet, XSDOrderedFacet, XSDBoundedFacet, model_xsd_XSDTerm, model_xsd_XSDTotalDigitsFacet, model_xsd_XSDTypeDefinition, model_xsd_XSDWhiteSpaceFacet, model_xsd_XSDWildcard, model_xsd_XSDXPathDefinition, model_partnerlinktype_Role, model_messageproperties_Property, model_messageproperties_PropertyAlias, Query, model_messageproperties_Query, model_partnerlinktype_PartnerLinkType, CorrelationPattern, EndpointReferenceRole, XSDConstraint, XSDContentTypeCategory, XSDDerivationMethod, XSDAttributeUseCategory, XSDCardinality, XSDComplexFinal, XSDCompositor, XSDXPathVariety, XSDDiagnosticSeverity, XSDDisallowedSubstitutions, XSDForm, XSDIdentityConstraintCategory, XSDNamespaceConstraintCategory, XSDOrdered, XSDProcessContents, XSDProhibitedSubstitutions, XSDSimpleFinal, XSDSubstitutionGroupExclusions, XSDVariety, XSDWhiteSpace},
    associations={extensions13, messageExchanges15, partnerLinks0, variables1, activity3, faultHandlers5, eventHandlers7, correlationSets9, imports11, myRole17, partnerRole18, PartnerLinkType21, catch23, catchAll25, toParts43, targets27, sources29, properties31, outputVariable32, inputVariable33, compensationHandler36, faultHandler38, fromParts41, correlations67, portType69, sources45, targets46, faultVariable48, activity51, faultMessageType54, faultElement56, variable58, toParts60, messageExchange63, partnerLink65, operation71, variable73, fromParts75, messageExchange78, faultVariable81, for83, until84, activities87, activity89, condition91, messages93, alarm94, activities96, links98, completionCondition100, activity102, for105, until108, repeatEvery111, copy114, to115, from117, part151, partnerLink153, faultHandlers119, compensationHandler121, activity124, variables127, correlationSets130, eventHandlers133, partnerLinks136, terminationHandler139, messageExchanges141, target144, activity146, variable149, messageExchange189, property156, query159, expression161, serviceRef164, type166, variable168, activity171, portType174, partnerLink177, correlations180, operation183, fromParts186, set192, alarm194, events197, Link199, activity201, transitionCondition203, Link206, activity208, XSDElement233, children210, children213, children216, children219, children222, activity224, children227, messageType230, children275, type236, from239, activity242, variable245, partnerLink248, correlations251, operation254, portType257, messageType260, XSDElement263, correlationSets266, fromParts269, messageExchange272, counterName301, joinCondition278, children281, children284, toVariable286, part288, fromVariable291, part293, startCounterValue296, finalCounterValue298, activity335, completionCondition304, activity307, activity310, condition312, activity315, variables318, condition320, elseIf322, else324, activity326, condition329, activity332, eOperations347, branches338, documentation340, children341, children344, eInput349, eOutput350, eFaults352, eParameterOrdering354, eParts357, typeDefinition359, elementDeclaration361, eMessage364, ePortType367, eBindingOperations369, eOperation371, eBindingInput373, eBindingOutput375, eBindingFaults377, ePorts379, eBinding380, eExtensibilityElements400, eImports381, eTypes382, eMessages384, ePortTypes387, eBindings390, eServices393, eNamespaces395, eDefinition397, eSchema398, eInput401, eOutput403, eFault405, children407, annotation412, anonymousTypeDefinition413, typeDefinition415, schema408, eMessage410, resolvedAttributeDeclaration418, annotation420, contents422, attributeUses424, attributeWildcardContent426, attributeWildcard428, resolvedAttributeGroupDefinition431, syntheticWildcard433, attributeDeclaration436, content438, attributeWildcardContent460, rootTypeDefinition463, syntheticParticle466, contentAnnotation441, baseTypeDefinition443, content446, contentType448, attributeUses451, attributeContents454, attributeWildcard457, syntheticWildcard468, container471, rootContainer472, schema475, diagnostics478, components480, primaryComponent482, annotation485, anonymousTypeDefinition487, typeDefinition490, identityConstraintDefinitions493, resolvedElementDeclaration495, substitutionGroupAffiliation498, substitutionGroup501, annotation504, simpleTypeDefinition506, scope509, resolvedFeature510, type512, annotation515, referencedKey517, selector520, fields522, annotation525, annotation527, annotation529, contents531, particles534, annotation537, modelGroup539, resolvedModelGroupDefinition541, annotations552, annotation543, content545, term546, annotations548, contents550, originalVersion586, contents554, elementDeclarations555, attributeDeclarations558, attributeGroupDefinitions561, typeDefinitions564, modelGroupDefinitions567, identityConstraintDefinitions570, notationDeclarations573, annotations575, allDiagnostics578, referencingDirectives581, fundamentalFacets609, rootVersion583, baseTypeDefinition611, primitiveTypeDefinition614, incorporatedVersions589, schemaForSchema592, incorporatedSchema595, resolvedSchema597, contents599, facetContents601, facets603, memberTypeDefinitions606, enumerationFacets639, patternFacets641, cardinalityFacet643, itemTypeDefinition617, rootTypeDefinition620, minFacet623, maxFacet625, maxInclusiveFacet627, minInclusiveFacet629, minExclusiveFacet631, maxExclusiveFacet633, lengthFacet635, whiteSpaceFacet637, effectiveFractionDigitsFacet668, effectivePatternFacet671, effectiveEnumerationFacet674, numericFacet645, maxLengthFacet647, minLengthFacet649, totalDigitsFacet651, fractionDigitsFacet653, orderedFacet655, boundedFacet657, effectiveMaxFacet659, effectiveWhiteSpaceFacet662, effectiveMaxLengthFacet665, baseType702, simpleType705, effectiveTotalDigitsFacet677, effectiveMinLengthFacet680, effectiveLengthFacet683, effectiveMinFacet686, syntheticFacets689, annotation691, derivationAnnotation693, annotations696, rootType699, complexType708, annotation711, annotations713, annotation716, wsdlPart718, query720, role722},
    generalizations={gen_model_Process_BPELExtensibleElement, gen_model_PartnerLink_BPELExtensibleElement, gen_model_FaultHandler_BPELExtensibleElement, gen_model_Activity_BPELExtensibleElement, gen_model_Link_BPELExtensibleElement, gen_model_CorrelationSet_BPELExtensibleElement, gen_model_Invoke_PartnerActivity, gen_model_Catch_BPELExtensibleElement, gen_model_Reply_PartnerActivity, gen_model_Reply_Activity, gen_model_PartnerActivity_Activity, gen_model_Pick_Activity, gen_model_Receive_PartnerActivity, gen_model_Exit_Activity, gen_model_Throw_Activity, gen_model_Wait_Activity, gen_model_Empty_Activity, gen_model_Sequence_Activity, gen_model_While_Activity, gen_model_Extension_BPELExtensibleElement, gen_model_Flow_Activity, gen_model_OnAlarm_BPELExtensibleElement, gen_model_Assign_Activity, gen_model_Copy_BPELExtensibleElement, gen_model_Scope_Activity, gen_model_CompensateScope_Activity, gen_model_CompensationHandler_BPELExtensibleElement, gen_model_To_BPELExtensibleElement, gen_model_To_AbstractAssignBound, gen_model_From_BPELExtensibleElement, gen_model_From_AbstractAssignBound, gen_model_OnMessage_BPELExtensibleElement, gen_model_PartnerLinks_BPELExtensibleElement, gen_model_Expression_ExtensibilityElement, gen_model_BooleanExpression_Expression, gen_model_Correlation_BPELExtensibleElement, gen_model_MessageExchange_BPELExtensibleElement, gen_model_EventHandler_BPELExtensibleElement, gen_model_Source_BPELExtensibleElement, gen_model_Target_BPELExtensibleElement, gen_model_MessageExchanges_BPELExtensibleElement, gen_model_Variables_BPELExtensibleElement, gen_model_CorrelationSets_BPELExtensibleElement, gen_model_Links_BPELExtensibleElement, gen_model_CatchAll_BPELExtensibleElement, gen_model_Correlations_BPELExtensibleElement, gen_model_Variable_BPELExtensibleElement, gen_model_Targets_BPELExtensibleElement, gen_model_UnknownExtensibilityAttribute_UnknownExtensibilityElement, gen_model_OnEvent_BPELExtensibleElement, gen_model_Import_BPELExtensibleElement, gen_model_Rethrow_Activity, gen_model_Condition_Expression, gen_model_Sources_BPELExtensibleElement, gen_model_Query_WSDLElement, gen_model_ServiceRef_ExtensibleElement, gen_model_Extensions_BPELExtensibleElement, gen_model_ExtensionActivity_Activity, gen_model_FromPart_BPELExtensibleElement, gen_model_ToPart_BPELExtensibleElement, gen_model_OpaqueActivity_Activity, gen_model_ForEach_Activity, gen_model_Else_BPELExtensibleElement, gen_model_RepeatUntil_Activity, gen_model_TerminationHandler_BPELExtensibleElement, gen_model_Validate_Activity, gen_model_If_Activity, gen_model_ElseIf_BPELExtensibleElement, gen_model_CompletionCondition_BPELExtensibleElement, gen_model_Branches_Expression, gen_model_BPELExtensibleElement_ExtensibleElement, gen_model_Documentation_BPELExtensibleElement, gen_model_Compensate_Activity, gen_model_FromParts_BPELExtensibleElement, gen_model_ToParts_BPELExtensibleElement, gen_model_wsdl_PortType_wsdl_ExtensibleElement, gen_model_wsdl_PortType_wsdl_IPortType, gen_model_wsdl_Operation_wsdl_ExtensibleElement, gen_model_wsdl_Operation_wsdl_IOperation, gen_model_wsdl_Message_wsdl_ExtensibleElement, gen_model_wsdl_Message_wsdl_IMessage, gen_model_wsdl_Part_wsdl_ExtensibleElement, gen_model_wsdl_Part_wsdl_IPart, gen_model_wsdl_Binding_wsdl_ExtensibleElement, gen_model_wsdl_Binding_wsdl_IBinding, gen_model_wsdl_BindingOperation_wsdl_ExtensibleElement, gen_model_wsdl_BindingOperation_wsdl_IBindingOperation, gen_model_wsdl_Service_wsdl_ExtensibleElement, gen_model_wsdl_Service_wsdl_IService, gen_model_wsdl_Port_wsdl_ExtensibleElement, gen_model_wsdl_Port_wsdl_IPort, gen_model_wsdl_ExtensibilityElement_wsdl_WSDLElement, gen_model_wsdl_ExtensibilityElement_wsdl_IExtensibilityElement, gen_model_wsdl_ExtensibleElement_wsdl_WSDLElement, gen_model_wsdl_ExtensibleElement_wsdl_IElementExtensible, gen_model_wsdl_ExtensibleElement_wsdl_IAttributeExtensible, gen_model_wsdl_Definition_wsdl_ExtensibleElement, gen_model_wsdl_Definition_wsdl_IDefinition, gen_model_wsdl_Input_wsdl_MessageReference, gen_model_wsdl_Input_wsdl_IInput, gen_model_wsdl_Import_wsdl_ExtensibleElement, gen_model_wsdl_Import_wsdl_IImport, gen_model_wsdl_Output_wsdl_MessageReference, gen_model_wsdl_Output_wsdl_IOutput, gen_model_wsdl_Fault_wsdl_MessageReference, gen_model_wsdl_Fault_wsdl_IFault, gen_model_wsdl_BindingInput_wsdl_ExtensibleElement, gen_model_wsdl_BindingInput_wsdl_IBindingInput, gen_model_wsdl_BindingOutput_wsdl_ExtensibleElement, gen_model_wsdl_BindingOutput_wsdl_IBindingOutput, gen_model_wsdl_BindingFault_wsdl_ExtensibleElement, gen_model_wsdl_BindingFault_wsdl_IBindingFault, gen_model_wsdl_IMessage_IElementExtensible, gen_model_wsdl_IPortType_IAttributeExtensible, gen_model_wsdl_IOperation_IElementExtensible, gen_model_wsdl_IInput_IAttributeExtensible, gen_model_wsdl_IOutput_IAttributeExtensible, gen_model_wsdl_IFault_IAttributeExtensible, gen_model_wsdl_IBindingInput_IElementExtensible, gen_model_wsdl_IPart_IAttributeExtensible, gen_model_wsdl_IService_IElementExtensible, gen_model_wsdl_IPort_IElementExtensible, gen_model_wsdl_IBinding_IElementExtensible, gen_model_wsdl_IBindingOperation_IElementExtensible, gen_model_wsdl_IBindingOutput_IElementExtensible, gen_model_wsdl_IBindingFault_IElementExtensible, gen_model_wsdl_IDefinition_IElementExtensible, gen_model_wsdl_UnknownExtensibilityElement_ExtensibilityElement, gen_model_wsdl_XSDSchemaExtensibilityElement_wsdl_ExtensibilityElement, gen_model_wsdl_XSDSchemaExtensibilityElement_wsdl_ISchema, gen_model_wsdl_IImport_IAttributeExtensible, gen_model_wsdl_Types_wsdl_ExtensibleElement, gen_model_wsdl_Types_wsdl_ITypes, gen_model_wsdl_MessageReference_ExtensibleElement, gen_model_wsdl_ISchema_IExtensibilityElement, gen_model_xsd_XSDAnnotation_xsd_XSDComponent, gen_model_xsd_XSDAnnotation_xsd_XSDRedefineContent, gen_model_xsd_XSDAttributeDeclaration_xsd_XSDFeature, gen_model_xsd_XSDAttributeDeclaration_xsd_XSDSchemaContent, gen_model_xsd_XSDBoundedFacet_XSDFundamentalFacet, gen_model_xsd_XSDCardinalityFacet_XSDFundamentalFacet, gen_model_xsd_XSDComplexTypeContent_XSDComponent, gen_model_xsd_XSDComplexTypeDefinition_xsd_XSDTypeDefinition, gen_model_xsd_XSDAttributeGroupContent_XSDConcreteComponent, gen_model_xsd_XSDAttributeGroupDefinition_xsd_XSDRedefinableComponent, gen_model_xsd_XSDAttributeGroupDefinition_xsd_XSDAttributeGroupContent, gen_model_xsd_XSDAttributeGroupDefinition_xsd_XSDRedefineContent, gen_model_xsd_XSDAttributeUse_xsd_XSDComponent, gen_model_xsd_XSDAttributeUse_xsd_XSDAttributeGroupContent, gen_model_xsd_XSDComplexTypeDefinition_xsd_XSDScope, gen_model_xsd_XSDElementDeclaration_xsd_XSDSchemaContent, gen_model_xsd_XSDElementDeclaration_xsd_XSDTerm, gen_model_xsd_XSDComponent_XSDConcreteComponent, gen_model_xsd_XSDConstrainingFacet_XSDFacet, gen_model_xsd_XSDDiagnostic_XSDConcreteComponent, gen_model_xsd_XSDElementDeclaration_xsd_XSDFeature, gen_model_xsd_XSDFeature_XSDNamedComponent, gen_model_xsd_XSDEnumerationFacet_XSDRepeatableFacet, gen_model_xsd_XSDFacet_XSDComponent, gen_model_xsd_XSDMaxExclusiveFacet_XSDMaxFacet, gen_model_xsd_XSDMaxFacet_XSDFixedFacet, gen_model_xsd_XSDFixedFacet_XSDConstrainingFacet, gen_model_xsd_XSDFractionDigitsFacet_XSDFixedFacet, gen_model_xsd_XSDFundamentalFacet_XSDFacet, gen_model_xsd_XSDIdentityConstraintDefinition_XSDNamedComponent, gen_model_xsd_XSDImport_XSDSchemaDirective, gen_model_xsd_XSDInclude_XSDSchemaCompositor, gen_model_xsd_XSDLengthFacet_XSDFixedFacet, gen_model_xsd_XSDNotationDeclaration_xsd_XSDNamedComponent, gen_model_xsd_XSDMaxInclusiveFacet_XSDMaxFacet, gen_model_xsd_XSDMaxLengthFacet_XSDFixedFacet, gen_model_xsd_XSDMinExclusiveFacet_XSDMinFacet, gen_model_xsd_XSDMinFacet_XSDFixedFacet, gen_model_xsd_XSDMinInclusiveFacet_XSDMinFacet, gen_model_xsd_XSDMinLengthFacet_XSDFixedFacet, gen_model_xsd_XSDModelGroup_XSDTerm, gen_model_xsd_XSDModelGroupDefinition_xsd_XSDRedefinableComponent, gen_model_xsd_XSDModelGroupDefinition_xsd_XSDParticleContent, gen_model_xsd_XSDModelGroupDefinition_xsd_XSDRedefineContent, gen_model_xsd_XSDNamedComponent_XSDComponent, gen_model_xsd_XSDSchema_XSDScope, gen_model_xsd_XSDNotationDeclaration_xsd_XSDSchemaContent, gen_model_xsd_XSDNumericFacet_XSDFundamentalFacet, gen_model_xsd_XSDOrderedFacet_XSDFundamentalFacet, gen_model_xsd_XSDParticle_XSDComplexTypeContent, gen_model_xsd_XSDParticleContent_XSDConcreteComponent, gen_model_xsd_XSDPatternFacet_XSDRepeatableFacet, gen_model_xsd_XSDRedefinableComponent_xsd_XSDNamedComponent, gen_model_xsd_XSDRedefinableComponent_xsd_XSDRedefineContent, gen_model_xsd_XSDRedefineContent_XSDSchemaContent, gen_model_xsd_XSDRedefine_XSDSchemaCompositor, gen_model_xsd_XSDRepeatableFacet_XSDConstrainingFacet, gen_model_xsd_XSDSchemaCompositor_XSDSchemaDirective, gen_model_xsd_XSDSchemaContent_XSDConcreteComponent, gen_model_xsd_XSDSchemaDirective_XSDSchemaContent, gen_model_xsd_XSDScope_XSDComponent, gen_model_xsd_XSDSimpleTypeDefinition_xsd_XSDTypeDefinition, gen_model_xsd_XSDSimpleTypeDefinition_xsd_XSDComplexTypeContent, gen_model_xsd_XSDTerm_xsd_XSDComponent, gen_model_xsd_XSDTerm_xsd_XSDParticleContent, gen_model_xsd_XSDTotalDigitsFacet_XSDFixedFacet, gen_model_xsd_XSDTypeDefinition_xsd_XSDRedefinableComponent, gen_model_xsd_XSDTypeDefinition_xsd_XSDRedefineContent, gen_model_xsd_XSDWhiteSpaceFacet_XSDFixedFacet, gen_model_xsd_XSDWildcard_XSDTerm, gen_model_xsd_XSDXPathDefinition_XSDComponent, gen_model_partnerlinktype_Role_ExtensibilityElement, gen_model_messageproperties_Property_ExtensibilityElement, gen_model_messageproperties_PropertyAlias_ExtensibilityElement, gen_model_messageproperties_Query_ExtensibilityElement, gen_model_partnerlinktype_PartnerLinkType_ExtensibilityElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)