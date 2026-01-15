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
XMessageKind: Enumeration = Enumeration(
    name="XMessageKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inout")
    }
)

# Classes
executablemodelingprofile_XOperation = Class(name="executablemodelingprofile::XOperation", is_abstract=True)
XFeature = Class(name="XFeature")
XNamespace = Class(name="XNamespace")
executablemodelingprofile_Operation = Class(name="executablemodelingprofile::Operation")
executablemodelingprofile_XNamespace = Class(name="executablemodelingprofile::XNamespace", is_abstract=True)
XNamedElement = Class(name="XNamedElement")
executablemodelingprofile_Namespace = Class(name="executablemodelingprofile::Namespace")
executablemodelingprofile_XNamedElement = Class(name="executablemodelingprofile::XNamedElement", is_abstract=True)
executablemodelingprofile_Association = Class(name="executablemodelingprofile::Association")
executablemodelingprofile_XClassifier = Class(name="executablemodelingprofile::XClassifier", is_abstract=True)
executablemodelingprofile_NamedElement = Class(name="executablemodelingprofile::NamedElement")
executablemodelingprofile_XFeature = Class(name="executablemodelingprofile::XFeature", is_abstract=True)
executablemodelingprofile_Feature = Class(name="executablemodelingprofile::Feature")
executablemodelingprofile_XAssociation = Class(name="executablemodelingprofile::XAssociation", is_abstract=True)
executablemodelingprofile_Behavior = Class(name="executablemodelingprofile::Behavior")
executablemodelingprofile_XEncapsulatedClassifier = Class(name="executablemodelingprofile::XEncapsulatedClassifier", is_abstract=True)
XClassifier = Class(name="XClassifier")
executablemodelingprofile_Classifier = Class(name="executablemodelingprofile::Classifier")
executablemodelingprofile_XBehavior = Class(name="executablemodelingprofile::XBehavior", is_abstract=True)
executablemodelingprofile_BehavioredClassifier = Class(name="executablemodelingprofile::BehavioredClassifier")
executablemodelingprofile_XSignal = Class(name="executablemodelingprofile::XSignal", is_abstract=True)
executablemodelingprofile_EncapsulatedClassifier = Class(name="executablemodelingprofile::EncapsulatedClassifier")
executablemodelingprofile_XProtocol = Class(name="executablemodelingprofile::XProtocol", is_abstract=True)
executablemodelingprofile_XParameter = Class(name="executablemodelingprofile::XParameter", is_abstract=True)
XTypedElement = Class(name="XTypedElement")
executablemodelingprofile_Parameter = Class(name="executablemodelingprofile::Parameter")
executablemodelingprofile_XTypedElement = Class(name="executablemodelingprofile::XTypedElement", is_abstract=True)
executablemodelingprofile_TypedElement = Class(name="executablemodelingprofile::TypedElement")
executablemodelingprofile_XProperty = Class(name="executablemodelingprofile::XProperty", is_abstract=True)
XMultiplicityElement = Class(name="XMultiplicityElement")
executablemodelingprofile_Property = Class(name="executablemodelingprofile::Property")
executablemodelingprofile_XMultiplicityElement = Class(name="executablemodelingprofile::XMultiplicityElement", is_abstract=True)
executablemodelingprofile_Signal = Class(name="executablemodelingprofile::Signal")
executablemodelingprofile_XDataType = Class(name="executablemodelingprofile::XDataType", is_abstract=True)
executablemodelingprofile_DataType = Class(name="executablemodelingprofile::DataType")
executablemodelingprofile_Reception = Class(name="executablemodelingprofile::Reception")
executablemodelingprofile_XPart = Class(name="executablemodelingprofile::XPart", is_abstract=True)
executablemodelingprofile_XPort = Class(name="executablemodelingprofile::XPort", is_abstract=True)
executablemodelingprofile_MultiplicityElement = Class(name="executablemodelingprofile::MultiplicityElement")
executablemodelingprofile_XReception = Class(name="executablemodelingprofile::XReception", is_abstract=True)
executablemodelingprofile_Port = Class(name="executablemodelingprofile::Port")
executablemodelingprofile_XConnector = Class(name="executablemodelingprofile::XConnector", is_abstract=True)
executablemodelingprofile_Package = Class(name="executablemodelingprofile::Package")
executablemodelingprofile_XMessageSet = Class(name="executablemodelingprofile::XMessageSet", is_abstract=True)
executablemodelingprofile_Connector = Class(name="executablemodelingprofile::Connector")
executablemodelingprofile_XProtocolContainer = Class(name="executablemodelingprofile::XProtocolContainer", is_abstract=True)
executablemodelingprofile_Enumeration = Class(name="executablemodelingprofile::Enumeration")
executablemodelingprofile_XAssociationClass = Class(name="executablemodelingprofile::XAssociationClass", is_abstract=True)
XAssociation = Class(name="XAssociation")
executablemodelingprofile_AssociationClass = Class(name="executablemodelingprofile::AssociationClass")
executablemodelingprofile_XTrigger = Class(name="executablemodelingprofile::XTrigger", is_abstract=True)
executablemodelingprofile_Interface = Class(name="executablemodelingprofile::Interface")
executablemodelingprofile_XEnumeration = Class(name="executablemodelingprofile::XEnumeration", is_abstract=True)
XDataType = Class(name="XDataType")
executablemodelingprofile_Trigger = Class(name="executablemodelingprofile::Trigger")
executablemodelingprofile_XStateMachine = Class(name="executablemodelingprofile::XStateMachine", is_abstract=True)
XBehavior = Class(name="XBehavior")
executablemodelingprofile_StateMachine = Class(name="executablemodelingprofile::StateMachine")
executablemodelingprofile_Region = Class(name="executablemodelingprofile::Region")
executablemodelingprofile_XState = Class(name="executablemodelingprofile::XState", is_abstract=True)
XVertex = Class(name="XVertex")
executablemodelingprofile_XRegion = Class(name="executablemodelingprofile::XRegion", is_abstract=True)
executablemodelingprofile_State = Class(name="executablemodelingprofile::State")
executablemodelingprofile_XVertex = Class(name="executablemodelingprofile::XVertex", is_abstract=True)
executablemodelingprofile_Vertex = Class(name="executablemodelingprofile::Vertex")
executablemodelingprofile_XPseudostate = Class(name="executablemodelingprofile::XPseudostate", is_abstract=True)
executablemodelingprofile_Pseudostate = Class(name="executablemodelingprofile::Pseudostate")
executablemodelingprofile_XTransition = Class(name="executablemodelingprofile::XTransition", is_abstract=True)
executablemodelingprofile_Activity = Class(name="executablemodelingprofile::Activity")
executablemodelingprofile_XActionBehavior = Class(name="executablemodelingprofile::XActionBehavior", is_abstract=True)
executablemodelingprofile_XConstraint = Class(name="executablemodelingprofile::XConstraint", is_abstract=True)
executablemodelingprofile_Transition = Class(name="executablemodelingprofile::Transition")
executablemodelingprofile_XActivity = Class(name="executablemodelingprofile::XActivity", is_abstract=True)
XActionBehavior = Class(name="XActionBehavior")
executablemodelingprofile_OpaqueBehavior = Class(name="executablemodelingprofile::OpaqueBehavior")
executablemodelingprofile_XConstrainedType = Class(name="executablemodelingprofile::XConstrainedType", is_abstract=True)
executablemodelingprofile_Constraint = Class(name="executablemodelingprofile::Constraint")
executablemodelingprofile_XOpaqueBehavior = Class(name="executablemodelingprofile::XOpaqueBehavior", is_abstract=True)
executablemodelingprofile_Generalization = Class(name="executablemodelingprofile::Generalization")
executablemodelingprofile_XGeneralizationSet = Class(name="executablemodelingprofile::XGeneralizationSet", is_abstract=True)
executablemodelingprofile_GeneralizationSet = Class(name="executablemodelingprofile::GeneralizationSet")
executablemodelingprofile_XClass = Class(name="executablemodelingprofile::XClass", is_abstract=True)
executablemodelingprofile_PrimitiveType = Class(name="executablemodelingprofile::PrimitiveType")
executablemodelingprofile_LiteralSpecification = Class(name="executablemodelingprofile::LiteralSpecification")
executablemodelingprofile_XGeneralization = Class(name="executablemodelingprofile::XGeneralization", is_abstract=True)
executablemodelingprofile_XConnectorEnd = Class(name="executablemodelingprofile::XConnectorEnd", is_abstract=True)
executablemodelingprofile_ConnectorEnd = Class(name="executablemodelingprofile::ConnectorEnd")
executablemodelingprofile_Class = Class(name="executablemodelingprofile::Class")

# executablemodelingprofile_XOperation class attributes and methods
executablemodelingprofile_XOperation_m_xOperationParameters: Method = Method(name="xOperationParameters", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XOperation_m_xOperationOneMethod: Method = Method(name="xOperationOneMethod", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XOperation_m_xOperationMethods: Method = Method(name="xOperationMethods", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XOperation_m_xOperationConstraints: Method = Method(name="xOperationConstraints", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XOperation_m_xOperationImports: Method = Method(name="xOperationImports", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XOperation_m_xOperationOwnedRules: Method = Method(name="xOperationOwnedRules", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XOperation.methods={executablemodelingprofile_XOperation_m_xOperationParameters, executablemodelingprofile_XOperation_m_xOperationMethods, executablemodelingprofile_XOperation_m_xOperationImports, executablemodelingprofile_XOperation_m_xOperationOneMethod, executablemodelingprofile_XOperation_m_xOperationConstraints, executablemodelingprofile_XOperation_m_xOperationOwnedRules}

# XFeature class attributes and methods

# XNamespace class attributes and methods

# executablemodelingprofile_Operation class attributes and methods

# executablemodelingprofile_XNamespace class attributes and methods

# XNamedElement class attributes and methods

# executablemodelingprofile_Namespace class attributes and methods

# executablemodelingprofile_XNamedElement class attributes and methods
executablemodelingprofile_XNamedElement_m_xNamedElementName: Method = Method(name="xNamedElementName", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XNamedElement.methods={executablemodelingprofile_XNamedElement_m_xNamedElementName}

# executablemodelingprofile_Association class attributes and methods

# executablemodelingprofile_XClassifier class attributes and methods
executablemodelingprofile_XClassifier_m_xClassifierFeatures: Method = Method(name="xClassifierFeatures", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XClassifier_m_xClassifierNestedClassifiers: Method = Method(name="xClassifierNestedClassifiers", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XClassifier_m_xClassifierGenerals: Method = Method(name="xClassifierGenerals", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XClassifier_m_xClassifierConstraints: Method = Method(name="xClassifierConstraints", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XClassifier.methods={executablemodelingprofile_XClassifier_m_xClassifierConstraints, executablemodelingprofile_XClassifier_m_xClassifierNestedClassifiers, executablemodelingprofile_XClassifier_m_xClassifierFeatures, executablemodelingprofile_XClassifier_m_xClassifierGenerals}

# executablemodelingprofile_NamedElement class attributes and methods

# executablemodelingprofile_XFeature class attributes and methods
executablemodelingprofile_XFeature_m_xFeatureClassifier: Method = Method(name="xFeatureClassifier", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XFeature.methods={executablemodelingprofile_XFeature_m_xFeatureClassifier}

# executablemodelingprofile_Feature class attributes and methods

# executablemodelingprofile_XAssociation class attributes and methods
executablemodelingprofile_XAssociation_m_xAssociationIsBinary: Method = Method(name="xAssociationIsBinary", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XAssociation.methods={executablemodelingprofile_XAssociation_m_xAssociationIsBinary}

# executablemodelingprofile_Behavior class attributes and methods

# executablemodelingprofile_XEncapsulatedClassifier class attributes and methods
executablemodelingprofile_XEncapsulatedClassifier_isExternal: Property = Property(name="isExternal", type=StringType)
executablemodelingprofile_XEncapsulatedClassifier_m_xEncapsulatedClassifierPorts: Method = Method(name="xEncapsulatedClassifierPorts", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XEncapsulatedClassifier_m_xEncapsulatedClassifierconnectors: Method = Method(name="xEncapsulatedClassifierconnectors", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XEncapsulatedClassifier_m_xEncapsulatedClassifierExternal: Method = Method(name="xEncapsulatedClassifierExternal", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XEncapsulatedClassifier.attributes={executablemodelingprofile_XEncapsulatedClassifier_isExternal}
executablemodelingprofile_XEncapsulatedClassifier.methods={executablemodelingprofile_XEncapsulatedClassifier_m_xEncapsulatedClassifierExternal, executablemodelingprofile_XEncapsulatedClassifier_m_xEncapsulatedClassifierPorts, executablemodelingprofile_XEncapsulatedClassifier_m_xEncapsulatedClassifierconnectors}

# XClassifier class attributes and methods

# executablemodelingprofile_Classifier class attributes and methods

# executablemodelingprofile_XBehavior class attributes and methods
executablemodelingprofile_XBehavior_m_xBehaviorNoParameterSets: Method = Method(name="xBehaviorNoParameterSets", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XBehavior.methods={executablemodelingprofile_XBehavior_m_xBehaviorNoParameterSets}

# executablemodelingprofile_BehavioredClassifier class attributes and methods

# executablemodelingprofile_XSignal class attributes and methods
executablemodelingprofile_XSignal_m_xSignalVisibility: Method = Method(name="xSignalVisibility", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XSignal.methods={executablemodelingprofile_XSignal_m_xSignalVisibility}

# executablemodelingprofile_EncapsulatedClassifier class attributes and methods

# executablemodelingprofile_XProtocol class attributes and methods
executablemodelingprofile_XProtocol_m_xProtocolProtocolContainer: Method = Method(name="xProtocolProtocolContainer", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XProtocol_m_xProtocolOutgoingInterface: Method = Method(name="xProtocolOutgoingInterface", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XProtocol_m_xProtocolSymmetricInterface: Method = Method(name="xProtocolSymmetricInterface", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XProtocol_m_xProtocolIncomingInterface: Method = Method(name="xProtocolIncomingInterface", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XProtocol.methods={executablemodelingprofile_XProtocol_m_xProtocolOutgoingInterface, executablemodelingprofile_XProtocol_m_xProtocolSymmetricInterface, executablemodelingprofile_XProtocol_m_xProtocolIncomingInterface, executablemodelingprofile_XProtocol_m_xProtocolProtocolContainer}

# executablemodelingprofile_XParameter class attributes and methods

# XTypedElement class attributes and methods

# executablemodelingprofile_Parameter class attributes and methods

# executablemodelingprofile_XTypedElement class attributes and methods
executablemodelingprofile_XTypedElement_m_xTypedElementType: Method = Method(name="xTypedElementType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XTypedElement.methods={executablemodelingprofile_XTypedElement_m_xTypedElementType}

# executablemodelingprofile_TypedElement class attributes and methods

# executablemodelingprofile_XProperty class attributes and methods

# XMultiplicityElement class attributes and methods

# executablemodelingprofile_Property class attributes and methods

# executablemodelingprofile_XMultiplicityElement class attributes and methods
executablemodelingprofile_XMultiplicityElement_isOrderedByValue: Property = Property(name="isOrderedByValue", type=StringType)
executablemodelingprofile_XMultiplicityElement_isDescending: Property = Property(name="isDescending", type=StringType)
executablemodelingprofile_XMultiplicityElement_m_xMultiplicityElementIsOrderedByValue: Method = Method(name="xMultiplicityElementIsOrderedByValue", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XMultiplicityElement_m_xMultiplicityElementKeys: Method = Method(name="xMultiplicityElementKeys", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XMultiplicityElement.attributes={executablemodelingprofile_XMultiplicityElement_isDescending, executablemodelingprofile_XMultiplicityElement_isOrderedByValue}
executablemodelingprofile_XMultiplicityElement.methods={executablemodelingprofile_XMultiplicityElement_m_xMultiplicityElementIsOrderedByValue, executablemodelingprofile_XMultiplicityElement_m_xMultiplicityElementKeys}

# executablemodelingprofile_Signal class attributes and methods

# executablemodelingprofile_XDataType class attributes and methods
executablemodelingprofile_XDataType_m_xDataTypeOperations: Method = Method(name="xDataTypeOperations", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XDataType.methods={executablemodelingprofile_XDataType_m_xDataTypeOperations}

# executablemodelingprofile_DataType class attributes and methods

# executablemodelingprofile_Reception class attributes and methods

# executablemodelingprofile_XPart class attributes and methods
executablemodelingprofile_XPart_m_xPartClassifier: Method = Method(name="xPartClassifier", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XPart.methods={executablemodelingprofile_XPart_m_xPartClassifier}

# executablemodelingprofile_XPort class attributes and methods
executablemodelingprofile_XPort_m_xPortClassifier: Method = Method(name="xPortClassifier", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XPort_m_xPortBehaviorPort: Method = Method(name="xPortBehaviorPort", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XPort_m_xPortVisibility: Method = Method(name="xPortVisibility", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XPort_m_xPortOrderingUniqueness: Method = Method(name="xPortOrderingUniqueness", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XPort_m_xPortType: Method = Method(name="xPortType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XPort.methods={executablemodelingprofile_XPort_m_xPortType, executablemodelingprofile_XPort_m_xPortOrderingUniqueness, executablemodelingprofile_XPort_m_xPortClassifier, executablemodelingprofile_XPort_m_xPortBehaviorPort, executablemodelingprofile_XPort_m_xPortVisibility}

# executablemodelingprofile_MultiplicityElement class attributes and methods

# executablemodelingprofile_XReception class attributes and methods
executablemodelingprofile_XReception_m_xReceptionSignal: Method = Method(name="xReceptionSignal", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XReception.methods={executablemodelingprofile_XReception_m_xReceptionSignal}

# executablemodelingprofile_Port class attributes and methods

# executablemodelingprofile_XConnector class attributes and methods
executablemodelingprofile_XConnector_m_xConnectorClassifier: Method = Method(name="xConnectorClassifier", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XConnector_m_xConnectorEnds: Method = Method(name="xConnectorEnds", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XConnector_m_xtConnectorType: Method = Method(name="xtConnectorType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XConnector.methods={executablemodelingprofile_XConnector_m_xtConnectorType, executablemodelingprofile_XConnector_m_xConnectorClassifier, executablemodelingprofile_XConnector_m_xConnectorEnds}

# executablemodelingprofile_Package class attributes and methods

# executablemodelingprofile_XMessageSet class attributes and methods
executablemodelingprofile_XMessageSet_messageKind: Property = Property(name="messageKind", type=StringType)
executablemodelingprofile_XMessageSet_m_xMessageSetIncoming: Method = Method(name="xMessageSetIncoming", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XMessageSet_m_xMessageSetOutgoing: Method = Method(name="xMessageSetOutgoing", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XMessageSet_m_xMessageSetSymmetric: Method = Method(name="xMessageSetSymmetric", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XMessageSet.attributes={executablemodelingprofile_XMessageSet_messageKind}
executablemodelingprofile_XMessageSet.methods={executablemodelingprofile_XMessageSet_m_xMessageSetOutgoing, executablemodelingprofile_XMessageSet_m_xMessageSetSymmetric, executablemodelingprofile_XMessageSet_m_xMessageSetIncoming}

# executablemodelingprofile_Connector class attributes and methods

# executablemodelingprofile_XProtocolContainer class attributes and methods
executablemodelingprofile_XProtocolContainer_m_xProtocolContainerProtocol: Method = Method(name="xProtocolContainerProtocol", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XProtocolContainer.methods={executablemodelingprofile_XProtocolContainer_m_xProtocolContainerProtocol}

# executablemodelingprofile_Enumeration class attributes and methods

# executablemodelingprofile_XAssociationClass class attributes and methods

# XAssociation class attributes and methods

# executablemodelingprofile_AssociationClass class attributes and methods

# executablemodelingprofile_XTrigger class attributes and methods
executablemodelingprofile_XTrigger_m_xTriggerSignalReception: Method = Method(name="xTriggerSignalReception", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XTrigger_m_xTriggerEvents: Method = Method(name="xTriggerEvents", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XTrigger_m_xTriggerCalledOperation: Method = Method(name="xTriggerCalledOperation", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XTrigger.methods={executablemodelingprofile_XTrigger_m_xTriggerCalledOperation, executablemodelingprofile_XTrigger_m_xTriggerSignalReception, executablemodelingprofile_XTrigger_m_xTriggerEvents}

# executablemodelingprofile_Interface class attributes and methods

# executablemodelingprofile_XEnumeration class attributes and methods
executablemodelingprofile_XEnumeration_m_xEnumerationAttributes: Method = Method(name="xEnumerationAttributes", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XEnumeration.methods={executablemodelingprofile_XEnumeration_m_xEnumerationAttributes}

# XDataType class attributes and methods

# executablemodelingprofile_Trigger class attributes and methods

# executablemodelingprofile_XStateMachine class attributes and methods
executablemodelingprofile_XStateMachine_m_xStateMachineOneRegion: Method = Method(name="xStateMachineOneRegion", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XStateMachine_m_xStateMachineNoParameters: Method = Method(name="xStateMachineNoParameters", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XStateMachine_m_xStateMachineRegions: Method = Method(name="xStateMachineRegions", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XStateMachine_m_xStateMachineInitialState: Method = Method(name="xStateMachineInitialState", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XStateMachine_m_xStateMachineContext: Method = Method(name="xStateMachineContext", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XStateMachine.methods={executablemodelingprofile_XStateMachine_m_xStateMachineContext, executablemodelingprofile_XStateMachine_m_xStateMachineOneRegion, executablemodelingprofile_XStateMachine_m_xStateMachineNoParameters, executablemodelingprofile_XStateMachine_m_xStateMachineRegions, executablemodelingprofile_XStateMachine_m_xStateMachineInitialState}

# XBehavior class attributes and methods

# executablemodelingprofile_StateMachine class attributes and methods

# executablemodelingprofile_Region class attributes and methods

# executablemodelingprofile_XState class attributes and methods
executablemodelingprofile_XState_m_xStateBehaviors: Method = Method(name="xStateBehaviors", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XState_m_xStateNoDoActivity: Method = Method(name="xStateNoDoActivity", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XState_m_xStateOneRegion: Method = Method(name="xStateOneRegion", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XState_m_xStateNoSubmachine: Method = Method(name="xStateNoSubmachine", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XState_m_xStateRegions: Method = Method(name="xStateRegions", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XState.methods={executablemodelingprofile_XState_m_xStateNoSubmachine, executablemodelingprofile_XState_m_xStateNoDoActivity, executablemodelingprofile_XState_m_xStateRegions, executablemodelingprofile_XState_m_xStateBehaviors, executablemodelingprofile_XState_m_xStateOneRegion}

# XVertex class attributes and methods

# executablemodelingprofile_XRegion class attributes and methods
executablemodelingprofile_XRegion_m_xRegionSubvertexes: Method = Method(name="xRegionSubvertexes", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XRegion_m_xRegionTransitions: Method = Method(name="xRegionTransitions", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XRegion.methods={executablemodelingprofile_XRegion_m_xRegionTransitions, executablemodelingprofile_XRegion_m_xRegionSubvertexes}

# executablemodelingprofile_State class attributes and methods

# executablemodelingprofile_XVertex class attributes and methods

# executablemodelingprofile_Vertex class attributes and methods

# executablemodelingprofile_XPseudostate class attributes and methods
executablemodelingprofile_XPseudostate_m_xPsuedostateKind: Method = Method(name="xPsuedostateKind", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XPseudostate.methods={executablemodelingprofile_XPseudostate_m_xPsuedostateKind}

# executablemodelingprofile_Pseudostate class attributes and methods

# executablemodelingprofile_XTransition class attributes and methods
executablemodelingprofile_XTransition_m_xTransitionTrigger: Method = Method(name="xTransitionTrigger", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XTransition_m_xTransitionGuard: Method = Method(name="xTransitionGuard", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XTransition_m_xTransitionEffect: Method = Method(name="xTransitionEffect", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XTransition.methods={executablemodelingprofile_XTransition_m_xTransitionTrigger, executablemodelingprofile_XTransition_m_xTransitionEffect, executablemodelingprofile_XTransition_m_xTransitionGuard}

# executablemodelingprofile_Activity class attributes and methods

# executablemodelingprofile_XActionBehavior class attributes and methods

# executablemodelingprofile_XConstraint class attributes and methods
executablemodelingprofile_XConstraint_m_xConstraintSpecification: Method = Method(name="xConstraintSpecification", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XConstraint_m_xConstraintBehavior: Method = Method(name="xConstraintBehavior", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XConstraint.methods={executablemodelingprofile_XConstraint_m_xConstraintSpecification, executablemodelingprofile_XConstraint_m_xConstraintBehavior}

# executablemodelingprofile_Transition class attributes and methods

# executablemodelingprofile_XActivity class attributes and methods
executablemodelingprofile_XActivity_m_xActivityParameters: Method = Method(name="xActivityParameters", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XActivity_m_xActivityTextualRepresentation: Method = Method(name="xActivityTextualRepresentation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XActivity.methods={executablemodelingprofile_XActivity_m_xActivityParameters, executablemodelingprofile_XActivity_m_xActivityTextualRepresentation}

# XActionBehavior class attributes and methods

# executablemodelingprofile_OpaqueBehavior class attributes and methods

# executablemodelingprofile_XConstrainedType class attributes and methods
executablemodelingprofile_XConstrainedType_isLowerBoundExclusive: Property = Property(name="isLowerBoundExclusive", type=StringType)
executablemodelingprofile_XConstrainedType_isUpperBoundExclusive: Property = Property(name="isUpperBoundExclusive", type=StringType)
executablemodelingprofile_XConstrainedType_m_xConstrainedTypePrimitiveType: Method = Method(name="xConstrainedTypePrimitiveType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XConstrainedType_m_xConstrainedTypeBounds: Method = Method(name="xConstrainedTypeBounds", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XConstrainedType.attributes={executablemodelingprofile_XConstrainedType_isUpperBoundExclusive, executablemodelingprofile_XConstrainedType_isLowerBoundExclusive}
executablemodelingprofile_XConstrainedType.methods={executablemodelingprofile_XConstrainedType_m_xConstrainedTypeBounds, executablemodelingprofile_XConstrainedType_m_xConstrainedTypePrimitiveType}

# executablemodelingprofile_Constraint class attributes and methods

# executablemodelingprofile_XOpaqueBehavior class attributes and methods
executablemodelingprofile_XOpaqueBehavior_isExternal: Property = Property(name="isExternal", type=StringType)
executablemodelingprofile_XOpaqueBehavior_m_xOpaqueBehaviorExternal: Method = Method(name="xOpaqueBehaviorExternal", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XOpaqueBehavior.attributes={executablemodelingprofile_XOpaqueBehavior_isExternal}
executablemodelingprofile_XOpaqueBehavior.methods={executablemodelingprofile_XOpaqueBehavior_m_xOpaqueBehaviorExternal}

# executablemodelingprofile_Generalization class attributes and methods

# executablemodelingprofile_XGeneralizationSet class attributes and methods

# executablemodelingprofile_GeneralizationSet class attributes and methods

# executablemodelingprofile_XClass class attributes and methods
executablemodelingprofile_XClass_isExternal: Property = Property(name="isExternal", type=StringType)
executablemodelingprofile_XClass_m_xClassMetaclass: Method = Method(name="xClassMetaclass", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XClass_m_xClassNestedClassifiers: Method = Method(name="xClassNestedClassifiers", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XClass_m_xClassExternal: Method = Method(name="xClassExternal", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XClass.attributes={executablemodelingprofile_XClass_isExternal}
executablemodelingprofile_XClass.methods={executablemodelingprofile_XClass_m_xClassExternal, executablemodelingprofile_XClass_m_xClassNestedClassifiers, executablemodelingprofile_XClass_m_xClassMetaclass}

# executablemodelingprofile_PrimitiveType class attributes and methods

# executablemodelingprofile_LiteralSpecification class attributes and methods

# executablemodelingprofile_XGeneralization class attributes and methods
executablemodelingprofile_XGeneralization_m_xGeneralizationClassifiers: Method = Method(name="xGeneralizationClassifiers", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XGeneralization_m_xGeneralizationGeneralizationSet: Method = Method(name="xGeneralizationGeneralizationSet", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XGeneralization.methods={executablemodelingprofile_XGeneralization_m_xGeneralizationGeneralizationSet, executablemodelingprofile_XGeneralization_m_xGeneralizationClassifiers}

# executablemodelingprofile_XConnectorEnd class attributes and methods
executablemodelingprofile_XConnectorEnd_m_xConnectorEndConnector: Method = Method(name="xConnectorEndConnector", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XConnectorEnd_m_xConnectorEndRole: Method = Method(name="xConnectorEndRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
executablemodelingprofile_XConnectorEnd_m_xConnectorEndUniqueness: Method = Method(name="xConnectorEndUniqueness", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
executablemodelingprofile_XConnectorEnd.methods={executablemodelingprofile_XConnectorEnd_m_xConnectorEndUniqueness, executablemodelingprofile_XConnectorEnd_m_xConnectorEndConnector, executablemodelingprofile_XConnectorEnd_m_xConnectorEndRole}

# executablemodelingprofile_ConnectorEnd class attributes and methods

# executablemodelingprofile_Class class attributes and methods

# Relationships
base_Operation0: BinaryAssociation = BinaryAssociation(
    name="base_Operation0",
    ends={
        Property(name="executablemodelingprofile_Operation", type=executablemodelingprofile_XOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XOperation", type=executablemodelingprofile_Operation, multiplicity=Multiplicity(1, 1))
    }
)
base_Namespace1: BinaryAssociation = BinaryAssociation(
    name="base_Namespace1",
    ends={
        Property(name="executablemodelingprofile_Namespace", type=executablemodelingprofile_XNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XNamespace", type=executablemodelingprofile_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
base_Association4: BinaryAssociation = BinaryAssociation(
    name="base_Association4",
    ends={
        Property(name="executablemodelingprofile_Association", type=executablemodelingprofile_XAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XAssociation", type=executablemodelingprofile_Association, multiplicity=Multiplicity(1, 1))
    }
)
base_NamedElement2: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement2",
    ends={
        Property(name="executablemodelingprofile_NamedElement", type=executablemodelingprofile_XNamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XNamedElement", type=executablemodelingprofile_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
base_Feature3: BinaryAssociation = BinaryAssociation(
    name="base_Feature3",
    ends={
        Property(name="executablemodelingprofile_Feature", type=executablemodelingprofile_XFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XFeature", type=executablemodelingprofile_Feature, multiplicity=Multiplicity(1, 1))
    }
)
base_Behavior6: BinaryAssociation = BinaryAssociation(
    name="base_Behavior6",
    ends={
        Property(name="executablemodelingprofile_Behavior", type=executablemodelingprofile_XBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XBehavior", type=executablemodelingprofile_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
base_Classifier5: BinaryAssociation = BinaryAssociation(
    name="base_Classifier5",
    ends={
        Property(name="executablemodelingprofile_Classifier", type=executablemodelingprofile_XClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XClassifier", type=executablemodelingprofile_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioredClassifier8: BinaryAssociation = BinaryAssociation(
    name="base_BehavioredClassifier8",
    ends={
        Property(name="executablemodelingprofile_BehavioredClassifier", type=executablemodelingprofile_XProtocol, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XProtocol", type=executablemodelingprofile_BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
base_EncapsulatedClassifier7: BinaryAssociation = BinaryAssociation(
    name="base_EncapsulatedClassifier7",
    ends={
        Property(name="executablemodelingprofile_EncapsulatedClassifier", type=executablemodelingprofile_XEncapsulatedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XEncapsulatedClassifier", type=executablemodelingprofile_EncapsulatedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
base_Parameter11: BinaryAssociation = BinaryAssociation(
    name="base_Parameter11",
    ends={
        Property(name="executablemodelingprofile_Parameter", type=executablemodelingprofile_XParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XParameter", type=executablemodelingprofile_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
base_TypedElement12: BinaryAssociation = BinaryAssociation(
    name="base_TypedElement12",
    ends={
        Property(name="executablemodelingprofile_TypedElement", type=executablemodelingprofile_XTypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XTypedElement", type=executablemodelingprofile_TypedElement, multiplicity=Multiplicity(1, 1))
    }
)
base_Property13: BinaryAssociation = BinaryAssociation(
    name="base_Property13",
    ends={
        Property(name="executablemodelingprofile_Property", type=executablemodelingprofile_XProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XProperty", type=executablemodelingprofile_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_Signal9: BinaryAssociation = BinaryAssociation(
    name="base_Signal9",
    ends={
        Property(name="executablemodelingprofile_Signal", type=executablemodelingprofile_XSignal, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XSignal", type=executablemodelingprofile_Signal, multiplicity=Multiplicity(1, 1))
    }
)
base_DataType10: BinaryAssociation = BinaryAssociation(
    name="base_DataType10",
    ends={
        Property(name="executablemodelingprofile_DataType", type=executablemodelingprofile_XDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XDataType", type=executablemodelingprofile_DataType, multiplicity=Multiplicity(1, 1))
    }
)
base_Reception18: BinaryAssociation = BinaryAssociation(
    name="base_Reception18",
    ends={
        Property(name="executablemodelingprofile_Reception", type=executablemodelingprofile_XReception, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XReception", type=executablemodelingprofile_Reception, multiplicity=Multiplicity(1, 1))
    }
)
base_Property19: BinaryAssociation = BinaryAssociation(
    name="base_Property19",
    ends={
        Property(name="executablemodelingprofile_Property20", type=executablemodelingprofile_XPart, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XPart", type=executablemodelingprofile_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_MultiplicityElement14: BinaryAssociation = BinaryAssociation(
    name="base_MultiplicityElement14",
    ends={
        Property(name="executablemodelingprofile_MultiplicityElement", type=executablemodelingprofile_XMultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XMultiplicityElement", type=executablemodelingprofile_MultiplicityElement, multiplicity=Multiplicity(1, 1))
    }
)
key15: BinaryAssociation = BinaryAssociation(
    name="key15",
    ends={
        Property(name="executablemodelingprofile_Property17", type=executablemodelingprofile_XMultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XMultiplicityElement16", type=executablemodelingprofile_Property, multiplicity=Multiplicity(0, 9999))
    }
)
base_Port21: BinaryAssociation = BinaryAssociation(
    name="base_Port21",
    ends={
        Property(name="executablemodelingprofile_Port", type=executablemodelingprofile_XPort, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XPort", type=executablemodelingprofile_Port, multiplicity=Multiplicity(1, 1))
    }
)
base_Package23: BinaryAssociation = BinaryAssociation(
    name="base_Package23",
    ends={
        Property(name="executablemodelingprofile_Package", type=executablemodelingprofile_XProtocolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XProtocolContainer", type=executablemodelingprofile_Package, multiplicity=Multiplicity(1, 1))
    }
)
base_Connector22: BinaryAssociation = BinaryAssociation(
    name="base_Connector22",
    ends={
        Property(name="executablemodelingprofile_Connector", type=executablemodelingprofile_XConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XConnector", type=executablemodelingprofile_Connector, multiplicity=Multiplicity(1, 1))
    }
)
base_Enumeration25: BinaryAssociation = BinaryAssociation(
    name="base_Enumeration25",
    ends={
        Property(name="executablemodelingprofile_Enumeration", type=executablemodelingprofile_XEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XEnumeration", type=executablemodelingprofile_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
base_AssociationClass26: BinaryAssociation = BinaryAssociation(
    name="base_AssociationClass26",
    ends={
        Property(name="executablemodelingprofile_AssociationClass", type=executablemodelingprofile_XAssociationClass, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XAssociationClass", type=executablemodelingprofile_AssociationClass, multiplicity=Multiplicity(1, 1))
    }
)
base_Interface24: BinaryAssociation = BinaryAssociation(
    name="base_Interface24",
    ends={
        Property(name="executablemodelingprofile_Interface", type=executablemodelingprofile_XMessageSet, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XMessageSet", type=executablemodelingprofile_Interface, multiplicity=Multiplicity(1, 1))
    }
)
base_Trigger27: BinaryAssociation = BinaryAssociation(
    name="base_Trigger27",
    ends={
        Property(name="executablemodelingprofile_Trigger", type=executablemodelingprofile_XTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XTrigger", type=executablemodelingprofile_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
base_Region29: BinaryAssociation = BinaryAssociation(
    name="base_Region29",
    ends={
        Property(name="executablemodelingprofile_Region", type=executablemodelingprofile_XRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XRegion", type=executablemodelingprofile_Region, multiplicity=Multiplicity(1, 1))
    }
)
base_StateMachine28: BinaryAssociation = BinaryAssociation(
    name="base_StateMachine28",
    ends={
        Property(name="executablemodelingprofile_StateMachine", type=executablemodelingprofile_XStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XStateMachine", type=executablemodelingprofile_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
base_State30: BinaryAssociation = BinaryAssociation(
    name="base_State30",
    ends={
        Property(name="executablemodelingprofile_State", type=executablemodelingprofile_XState, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XState", type=executablemodelingprofile_State, multiplicity=Multiplicity(1, 1))
    }
)
base_Vertex31: BinaryAssociation = BinaryAssociation(
    name="base_Vertex31",
    ends={
        Property(name="executablemodelingprofile_Vertex", type=executablemodelingprofile_XVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XVertex", type=executablemodelingprofile_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
base_Pseudostate32: BinaryAssociation = BinaryAssociation(
    name="base_Pseudostate32",
    ends={
        Property(name="executablemodelingprofile_Pseudostate", type=executablemodelingprofile_XPseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XPseudostate", type=executablemodelingprofile_Pseudostate, multiplicity=Multiplicity(1, 1))
    }
)
base_Activity34: BinaryAssociation = BinaryAssociation(
    name="base_Activity34",
    ends={
        Property(name="executablemodelingprofile_Activity", type=executablemodelingprofile_XActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XActivity", type=executablemodelingprofile_Activity, multiplicity=Multiplicity(1, 1))
    }
)
base_Transition33: BinaryAssociation = BinaryAssociation(
    name="base_Transition33",
    ends={
        Property(name="executablemodelingprofile_Transition", type=executablemodelingprofile_XTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XTransition", type=executablemodelingprofile_Transition, multiplicity=Multiplicity(1, 1))
    }
)
base_OpaqueBehavior36: BinaryAssociation = BinaryAssociation(
    name="base_OpaqueBehavior36",
    ends={
        Property(name="executablemodelingprofile_OpaqueBehavior", type=executablemodelingprofile_XOpaqueBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XOpaqueBehavior", type=executablemodelingprofile_OpaqueBehavior, multiplicity=Multiplicity(1, 1))
    }
)
base_Constraint35: BinaryAssociation = BinaryAssociation(
    name="base_Constraint35",
    ends={
        Property(name="executablemodelingprofile_Constraint", type=executablemodelingprofile_XConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XConstraint", type=executablemodelingprofile_Constraint, multiplicity=Multiplicity(1, 1))
    }
)
base_Generalization43: BinaryAssociation = BinaryAssociation(
    name="base_Generalization43",
    ends={
        Property(name="executablemodelingprofile_Generalization", type=executablemodelingprofile_XGeneralization, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XGeneralization", type=executablemodelingprofile_Generalization, multiplicity=Multiplicity(1, 1))
    }
)
base_GeneralizationSet44: BinaryAssociation = BinaryAssociation(
    name="base_GeneralizationSet44",
    ends={
        Property(name="executablemodelingprofile_GeneralizationSet", type=executablemodelingprofile_XGeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XGeneralizationSet", type=executablemodelingprofile_GeneralizationSet, multiplicity=Multiplicity(1, 1))
    }
)
base_PrimitiveType37: BinaryAssociation = BinaryAssociation(
    name="base_PrimitiveType37",
    ends={
        Property(name="executablemodelingprofile_PrimitiveType", type=executablemodelingprofile_XConstrainedType, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XConstrainedType", type=executablemodelingprofile_PrimitiveType, multiplicity=Multiplicity(1, 1))
    }
)
lowerBound38: BinaryAssociation = BinaryAssociation(
    name="lowerBound38",
    ends={
        Property(name="executablemodelingprofile_LiteralSpecification", type=executablemodelingprofile_XConstrainedType, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XConstrainedType39", type=executablemodelingprofile_LiteralSpecification, multiplicity=Multiplicity(0, 1))
    }
)
upperBound40: BinaryAssociation = BinaryAssociation(
    name="upperBound40",
    ends={
        Property(name="executablemodelingprofile_LiteralSpecification42", type=executablemodelingprofile_XConstrainedType, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XConstrainedType41", type=executablemodelingprofile_LiteralSpecification, multiplicity=Multiplicity(0, 1))
    }
)
base_ConnectorEnd46: BinaryAssociation = BinaryAssociation(
    name="base_ConnectorEnd46",
    ends={
        Property(name="executablemodelingprofile_ConnectorEnd", type=executablemodelingprofile_XConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XConnectorEnd", type=executablemodelingprofile_ConnectorEnd, multiplicity=Multiplicity(1, 1))
    }
)
base_Class45: BinaryAssociation = BinaryAssociation(
    name="base_Class45",
    ends={
        Property(name="executablemodelingprofile_Class", type=executablemodelingprofile_XClass, multiplicity=Multiplicity(1, 1)),
        Property(name="executablemodelingprofile_XClass", type=executablemodelingprofile_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_executablemodelingprofile_XOperation_XFeature = Generalization(general=XFeature, specific=executablemodelingprofile_XOperation)
gen_executablemodelingprofile_XOperation_XNamespace = Generalization(general=XNamespace, specific=executablemodelingprofile_XOperation)
gen_executablemodelingprofile_XNamespace_XNamedElement = Generalization(general=XNamedElement, specific=executablemodelingprofile_XNamespace)
gen_executablemodelingprofile_XClassifier_XNamespace = Generalization(general=XNamespace, specific=executablemodelingprofile_XClassifier)
gen_executablemodelingprofile_XFeature_XNamedElement = Generalization(general=XNamedElement, specific=executablemodelingprofile_XFeature)
gen_executablemodelingprofile_XEncapsulatedClassifier_XClassifier = Generalization(general=XClassifier, specific=executablemodelingprofile_XEncapsulatedClassifier)
gen_executablemodelingprofile_XBehavior_XNamespace = Generalization(general=XNamespace, specific=executablemodelingprofile_XBehavior)
gen_executablemodelingprofile_XSignal_XClassifier = Generalization(general=XClassifier, specific=executablemodelingprofile_XSignal)
gen_executablemodelingprofile_XProtocol_XClassifier = Generalization(general=XClassifier, specific=executablemodelingprofile_XProtocol)
gen_executablemodelingprofile_XParameter_XTypedElement = Generalization(general=XTypedElement, specific=executablemodelingprofile_XParameter)
gen_executablemodelingprofile_XProperty_XMultiplicityElement = Generalization(general=XMultiplicityElement, specific=executablemodelingprofile_XProperty)
gen_executablemodelingprofile_XProperty_XFeature = Generalization(general=XFeature, specific=executablemodelingprofile_XProperty)
gen_executablemodelingprofile_XProperty_XTypedElement = Generalization(general=XTypedElement, specific=executablemodelingprofile_XProperty)
gen_executablemodelingprofile_XDataType_XClassifier = Generalization(general=XClassifier, specific=executablemodelingprofile_XDataType)
gen_executablemodelingprofile_XPart_XFeature = Generalization(general=XFeature, specific=executablemodelingprofile_XPart)
gen_executablemodelingprofile_XPart_XTypedElement = Generalization(general=XTypedElement, specific=executablemodelingprofile_XPart)
gen_executablemodelingprofile_XPort_XFeature = Generalization(general=XFeature, specific=executablemodelingprofile_XPort)
gen_executablemodelingprofile_XReception_XFeature = Generalization(general=XFeature, specific=executablemodelingprofile_XReception)
gen_executablemodelingprofile_XConnector_XFeature = Generalization(general=XFeature, specific=executablemodelingprofile_XConnector)
gen_executablemodelingprofile_XMessageSet_XClassifier = Generalization(general=XClassifier, specific=executablemodelingprofile_XMessageSet)
gen_executablemodelingprofile_XAssociationClass_XClassifier = Generalization(general=XClassifier, specific=executablemodelingprofile_XAssociationClass)
gen_executablemodelingprofile_XAssociationClass_XAssociation = Generalization(general=XAssociation, specific=executablemodelingprofile_XAssociationClass)
gen_executablemodelingprofile_XEnumeration_XDataType = Generalization(general=XDataType, specific=executablemodelingprofile_XEnumeration)
gen_executablemodelingprofile_XStateMachine_XBehavior = Generalization(general=XBehavior, specific=executablemodelingprofile_XStateMachine)
gen_executablemodelingprofile_XState_XVertex = Generalization(general=XVertex, specific=executablemodelingprofile_XState)
gen_executablemodelingprofile_XPseudostate_XVertex = Generalization(general=XVertex, specific=executablemodelingprofile_XPseudostate)
gen_executablemodelingprofile_XActionBehavior_XBehavior = Generalization(general=XBehavior, specific=executablemodelingprofile_XActionBehavior)
gen_executablemodelingprofile_XConstraint_XNamedElement = Generalization(general=XNamedElement, specific=executablemodelingprofile_XConstraint)
gen_executablemodelingprofile_XActivity_XActionBehavior = Generalization(general=XActionBehavior, specific=executablemodelingprofile_XActivity)
gen_executablemodelingprofile_XConstrainedType_XClassifier = Generalization(general=XClassifier, specific=executablemodelingprofile_XConstrainedType)
gen_executablemodelingprofile_XOpaqueBehavior_XActionBehavior = Generalization(general=XActionBehavior, specific=executablemodelingprofile_XOpaqueBehavior)
gen_executablemodelingprofile_XClass_XClassifier = Generalization(general=XClassifier, specific=executablemodelingprofile_XClass)

# Domain Model
domain_model = DomainModel(
    name="executablemodelingprofile",
    types={executablemodelingprofile_XOperation, XFeature, XNamespace, executablemodelingprofile_Operation, executablemodelingprofile_XNamespace, XNamedElement, executablemodelingprofile_Namespace, executablemodelingprofile_XNamedElement, executablemodelingprofile_Association, executablemodelingprofile_XClassifier, executablemodelingprofile_NamedElement, executablemodelingprofile_XFeature, executablemodelingprofile_Feature, executablemodelingprofile_XAssociation, executablemodelingprofile_Behavior, executablemodelingprofile_XEncapsulatedClassifier, XClassifier, executablemodelingprofile_Classifier, executablemodelingprofile_XBehavior, executablemodelingprofile_BehavioredClassifier, executablemodelingprofile_XSignal, executablemodelingprofile_EncapsulatedClassifier, executablemodelingprofile_XProtocol, executablemodelingprofile_XParameter, XTypedElement, executablemodelingprofile_Parameter, executablemodelingprofile_XTypedElement, executablemodelingprofile_TypedElement, executablemodelingprofile_XProperty, XMultiplicityElement, executablemodelingprofile_Property, executablemodelingprofile_XMultiplicityElement, executablemodelingprofile_Signal, executablemodelingprofile_XDataType, executablemodelingprofile_DataType, executablemodelingprofile_Reception, executablemodelingprofile_XPart, executablemodelingprofile_XPort, executablemodelingprofile_MultiplicityElement, executablemodelingprofile_XReception, executablemodelingprofile_Port, executablemodelingprofile_XConnector, executablemodelingprofile_Package, executablemodelingprofile_XMessageSet, executablemodelingprofile_Connector, executablemodelingprofile_XProtocolContainer, executablemodelingprofile_Enumeration, executablemodelingprofile_XAssociationClass, XAssociation, executablemodelingprofile_AssociationClass, executablemodelingprofile_XTrigger, executablemodelingprofile_Interface, executablemodelingprofile_XEnumeration, XDataType, executablemodelingprofile_Trigger, executablemodelingprofile_XStateMachine, XBehavior, executablemodelingprofile_StateMachine, executablemodelingprofile_Region, executablemodelingprofile_XState, XVertex, executablemodelingprofile_XRegion, executablemodelingprofile_State, executablemodelingprofile_XVertex, executablemodelingprofile_Vertex, executablemodelingprofile_XPseudostate, executablemodelingprofile_Pseudostate, executablemodelingprofile_XTransition, executablemodelingprofile_Activity, executablemodelingprofile_XActionBehavior, executablemodelingprofile_XConstraint, executablemodelingprofile_Transition, executablemodelingprofile_XActivity, XActionBehavior, executablemodelingprofile_OpaqueBehavior, executablemodelingprofile_XConstrainedType, executablemodelingprofile_Constraint, executablemodelingprofile_XOpaqueBehavior, executablemodelingprofile_Generalization, executablemodelingprofile_XGeneralizationSet, executablemodelingprofile_GeneralizationSet, executablemodelingprofile_XClass, executablemodelingprofile_PrimitiveType, executablemodelingprofile_LiteralSpecification, executablemodelingprofile_XGeneralization, executablemodelingprofile_XConnectorEnd, executablemodelingprofile_ConnectorEnd, executablemodelingprofile_Class, XMessageKind},
    associations={base_Operation0, base_Namespace1, base_Association4, base_NamedElement2, base_Feature3, base_Behavior6, base_Classifier5, base_BehavioredClassifier8, base_EncapsulatedClassifier7, base_Parameter11, base_TypedElement12, base_Property13, base_Signal9, base_DataType10, base_Reception18, base_Property19, base_MultiplicityElement14, key15, base_Port21, base_Package23, base_Connector22, base_Enumeration25, base_AssociationClass26, base_Interface24, base_Trigger27, base_Region29, base_StateMachine28, base_State30, base_Vertex31, base_Pseudostate32, base_Activity34, base_Transition33, base_OpaqueBehavior36, base_Constraint35, base_Generalization43, base_GeneralizationSet44, base_PrimitiveType37, lowerBound38, upperBound40, base_ConnectorEnd46, base_Class45},
    generalizations={gen_executablemodelingprofile_XOperation_XFeature, gen_executablemodelingprofile_XOperation_XNamespace, gen_executablemodelingprofile_XNamespace_XNamedElement, gen_executablemodelingprofile_XClassifier_XNamespace, gen_executablemodelingprofile_XFeature_XNamedElement, gen_executablemodelingprofile_XEncapsulatedClassifier_XClassifier, gen_executablemodelingprofile_XBehavior_XNamespace, gen_executablemodelingprofile_XSignal_XClassifier, gen_executablemodelingprofile_XProtocol_XClassifier, gen_executablemodelingprofile_XParameter_XTypedElement, gen_executablemodelingprofile_XProperty_XMultiplicityElement, gen_executablemodelingprofile_XProperty_XFeature, gen_executablemodelingprofile_XProperty_XTypedElement, gen_executablemodelingprofile_XDataType_XClassifier, gen_executablemodelingprofile_XPart_XFeature, gen_executablemodelingprofile_XPart_XTypedElement, gen_executablemodelingprofile_XPort_XFeature, gen_executablemodelingprofile_XReception_XFeature, gen_executablemodelingprofile_XConnector_XFeature, gen_executablemodelingprofile_XMessageSet_XClassifier, gen_executablemodelingprofile_XAssociationClass_XClassifier, gen_executablemodelingprofile_XAssociationClass_XAssociation, gen_executablemodelingprofile_XEnumeration_XDataType, gen_executablemodelingprofile_XStateMachine_XBehavior, gen_executablemodelingprofile_XState_XVertex, gen_executablemodelingprofile_XPseudostate_XVertex, gen_executablemodelingprofile_XActionBehavior_XBehavior, gen_executablemodelingprofile_XConstraint_XNamedElement, gen_executablemodelingprofile_XActivity_XActionBehavior, gen_executablemodelingprofile_XConstrainedType_XClassifier, gen_executablemodelingprofile_XOpaqueBehavior_XActionBehavior, gen_executablemodelingprofile_XClass_XClassifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)