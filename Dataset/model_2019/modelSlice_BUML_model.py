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

# Classes
umlTrace_State = Class(name="umlTrace::State")
Values_ActionActivation_firing_Value = Class(name="Values::ActionActivation::firing::Value")
Values_SemanticVisitor_runtimeModelElement_Value = Class(name="Values::SemanticVisitor::runtimeModelElement::Value")
umlTrace_Trace = Class(name="umlTrace::Trace")
State = Class(name="State")
Traced_TracedObjects = Class(name="Traced::TracedObjects")
umlTrace_Traced_TracedObjects = Class(name="umlTrace::Traced::TracedObjects")
uml_TracedCombinedFragment = Class(name="uml::TracedCombinedFragment")
uml_TracedCreateLinkObjectAction = Class(name="uml::TracedCreateLinkObjectAction")
uml_TracedInitialNode = Class(name="uml::TracedInitialNode")
uml_TracedFlowFinalNode = Class(name="uml::TracedFlowFinalNode")
uml_TracedExpansionRegion = Class(name="uml::TracedExpansionRegion")
uml_TracedSendObjectAction = Class(name="uml::TracedSendObjectAction")
uml_TracedPackageImport = Class(name="uml::TracedPackageImport")
uml_TracedClass = Class(name="uml::TracedClass")
uml_TracedInteractionUse = Class(name="uml::TracedInteractionUse")
uml_TracedGeneralizationSet = Class(name="uml::TracedGeneralizationSet")
uml_TracedChangeEvent = Class(name="uml::TracedChangeEvent")
uml_TracedDependency = Class(name="uml::TracedDependency")
uml_TracedPort = Class(name="uml::TracedPort")
IntermediateActivities_TracedInitialNodeActivation = Class(name="IntermediateActivities::TracedInitialNodeActivation")
uml_TracedCollaborationUse = Class(name="uml::TracedCollaborationUse")
IntermediateActivities_TracedActivityExecution = Class(name="IntermediateActivities::TracedActivityExecution")
uml_TracedCreateObjectAction = Class(name="uml::TracedCreateObjectAction")
uml_TracedLifeline = Class(name="uml::TracedLifeline")
IntermediateActivities_TracedForkNodeActivation = Class(name="IntermediateActivities::TracedForkNodeActivation")
uml_TracedDurationConstraint = Class(name="uml::TracedDurationConstraint")
uml_TracedDestructionOccurrenceSpecification = Class(name="uml::TracedDestructionOccurrenceSpecification")
uml_TracedConnector = Class(name="uml::TracedConnector")
uml_TracedExtend = Class(name="uml::TracedExtend")
IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution = Class(name="IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution")
uml_TracedExtension = Class(name="uml::TracedExtension")
uml_TracedStructuredActivityNode = Class(name="uml::TracedStructuredActivityNode")
uml_TracedExecutionEnvironment = Class(name="uml::TracedExecutionEnvironment")
uml_TracedIntervalConstraint = Class(name="uml::TracedIntervalConstraint")
uml_TracedConsiderIgnoreFragment = Class(name="uml::TracedConsiderIgnoreFragment")
uml_TracedContinuation = Class(name="uml::TracedContinuation")
uml_TracedTimeConstraint = Class(name="uml::TracedTimeConstraint")
uml_TracedInputPin = Class(name="uml::TracedInputPin")
uml_TracedValuePin = Class(name="uml::TracedValuePin")
uml_TracedNode = Class(name="uml::TracedNode")
uml_TracedExceptionHandler = Class(name="uml::TracedExceptionHandler")
uml_TracedSequenceNode = Class(name="uml::TracedSequenceNode")
uml_TracedStartClassifierBehaviorAction = Class(name="uml::TracedStartClassifierBehaviorAction")
uml_TracedParameter = Class(name="uml::TracedParameter")
uml_TracedOpaqueExpression = Class(name="uml::TracedOpaqueExpression")
uml_TracedLiteralString = Class(name="uml::TracedLiteralString")
BasicActions_TracedInputPinActivation = Class(name="BasicActions::TracedInputPinActivation")
uml_TracedStateInvariant = Class(name="uml::TracedStateInvariant")
IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution = Class(name="IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution")
uml_TracedInstanceSpecification = Class(name="uml::TracedInstanceSpecification")
uml_TracedAcceptCallAction = Class(name="uml::TracedAcceptCallAction")
uml_TracedClearVariableAction = Class(name="uml::TracedClearVariableAction")
uml_TracedConstraint = Class(name="uml::TracedConstraint")
uml_TracedBroadcastSignalAction = Class(name="uml::TracedBroadcastSignalAction")
uml_TracedInteraction = Class(name="uml::TracedInteraction")
IntermediateActivities_TracedActivityNodeActivation = Class(name="IntermediateActivities::TracedActivityNodeActivation")
uml_TracedDestroyObjectAction = Class(name="uml::TracedDestroyObjectAction")
BasicActions_TracedCallBehaviorActionActivation = Class(name="BasicActions::TracedCallBehaviorActionActivation")
IntermediateActivities_TracedActivityParameterNodeActivation = Class(name="IntermediateActivities::TracedActivityParameterNodeActivation")
uml_TracedActivityPartition = Class(name="uml::TracedActivityPartition")
uml_TracedStateMachine = Class(name="uml::TracedStateMachine")
uml_TracedMessage = Class(name="uml::TracedMessage")
uml_TracedDeployment = Class(name="uml::TracedDeployment")
uml_TracedStereotype = Class(name="uml::TracedStereotype")
uml_TracedEnumerationLiteral = Class(name="uml::TracedEnumerationLiteral")
uml_TracedSubstitution = Class(name="uml::TracedSubstitution")
uml_TracedInformationFlow = Class(name="uml::TracedInformationFlow")
uml_TracedAssociationClass = Class(name="uml::TracedAssociationClass")
uml_TracedReclassifyObjectAction = Class(name="uml::TracedReclassifyObjectAction")
uml_TracedUseCase = Class(name="uml::TracedUseCase")
IntermediateActivities_TracedJoinNodeActivation = Class(name="IntermediateActivities::TracedJoinNodeActivation")
Kernel_TracedObject = Class(name="Kernel::TracedObject")
Loci_TracedSemanticVisitor = Class(name="Loci::TracedSemanticVisitor")
uml_TracedTimeEvent = Class(name="uml::TracedTimeEvent")
uml_TracedActivity = Class(name="uml::TracedActivity")
uml_TracedForkNode = Class(name="uml::TracedForkNode")
Kernel_TracedReference = Class(name="Kernel::TracedReference")
IntermediateActions_TracedAddStructuralFeatureValueActionActivation = Class(name="IntermediateActions::TracedAddStructuralFeatureValueActionActivation")
uml_TracedGeneralization = Class(name="uml::TracedGeneralization")
uml_TracedInstanceValue = Class(name="uml::TracedInstanceValue")
uml_TracedRemoveStructuralFeatureValueAction = Class(name="uml::TracedRemoveStructuralFeatureValueAction")
uml_TracedInterval = Class(name="uml::TracedInterval")
Kernel_TracedIntegerValue = Class(name="Kernel::TracedIntegerValue")
uml_TracedAnyReceiveEvent = Class(name="uml::TracedAnyReceiveEvent")
uml_TracedReadStructuralFeatureAction = Class(name="uml::TracedReadStructuralFeatureAction")
uml_TracedDataStoreNode = Class(name="uml::TracedDataStoreNode")
uml_TracedPartDecomposition = Class(name="uml::TracedPartDecomposition")
uml_TracedInterruptibleActivityRegion = Class(name="uml::TracedInterruptibleActivityRegion")
uml_TracedProtocolTransition = Class(name="uml::TracedProtocolTransition")
uml_TracedInteractionOperand = Class(name="uml::TracedInteractionOperand")
uml_TracedDeploymentSpecification = Class(name="uml::TracedDeploymentSpecification")
uml_TracedUsage = Class(name="uml::TracedUsage")
uml_TracedActionInputPin = Class(name="uml::TracedActionInputPin")
uml_TracedReadVariableAction = Class(name="uml::TracedReadVariableAction")
IntermediateActivities_TracedActivityFinalNodeActivation = Class(name="IntermediateActivities::TracedActivityFinalNodeActivation")
uml_TracedDestroyLinkAction = Class(name="uml::TracedDestroyLinkAction")
uml_TracedLiteralInteger = Class(name="uml::TracedLiteralInteger")
uml_TracedProtocolStateMachine = Class(name="uml::TracedProtocolStateMachine")
uml_TracedReception = Class(name="uml::TracedReception")
uml_TracedMessageOccurrenceSpecification = Class(name="uml::TracedMessageOccurrenceSpecification")
uml_TracedTemplateBinding = Class(name="uml::TracedTemplateBinding")
uml_TracedConnectionPointReference = Class(name="uml::TracedConnectionPointReference")
uml_TracedRealization = Class(name="uml::TracedRealization")
uml_TracedReadLinkObjectEndQualifierAction = Class(name="uml::TracedReadLinkObjectEndQualifierAction")
BasicActions_TracedOpaqueActionActivation = Class(name="BasicActions::TracedOpaqueActionActivation")
uml_TracedJoinNode = Class(name="uml::TracedJoinNode")
uml_TracedRedefinableTemplateSignature = Class(name="uml::TracedRedefinableTemplateSignature")
uml_TracedModel = Class(name="uml::TracedModel")
uml_TracedSignalEvent = Class(name="uml::TracedSignalEvent")
Kernel_TracedBooleanValue = Class(name="Kernel::TracedBooleanValue")
uml_TracedConditionalNode = Class(name="uml::TracedConditionalNode")
uml_TracedExtensionPoint = Class(name="uml::TracedExtensionPoint")
uml_TracedSignal = Class(name="uml::TracedSignal")
uml_TracedExecutionOccurrenceSpecification = Class(name="uml::TracedExecutionOccurrenceSpecification")
uml_TracedTimeInterval = Class(name="uml::TracedTimeInterval")
uml_TracedInteractionConstraint = Class(name="uml::TracedInteractionConstraint")
IntermediateActivities_TracedDecisionNodeActivation = Class(name="IntermediateActivities::TracedDecisionNodeActivation")
uml_TracedCentralBufferNode = Class(name="uml::TracedCentralBufferNode")
Kernel_TracedLiteralIntegerEvaluation = Class(name="Kernel::TracedLiteralIntegerEvaluation")
uml_TracedCreateLinkAction = Class(name="uml::TracedCreateLinkAction")
uml_TracedPackage = Class(name="uml::TracedPackage")
uml_TracedCallEvent = Class(name="uml::TracedCallEvent")
uml_TracedLoopNode = Class(name="uml::TracedLoopNode")
uml_TracedComment = Class(name="uml::TracedComment")
uml_TracedDataType = Class(name="uml::TracedDataType")
uml_TracedComponentRealization = Class(name="uml::TracedComponentRealization")
uml_TracedInterface = Class(name="uml::TracedInterface")
uml_TracedOpaqueBehavior = Class(name="uml::TracedOpaqueBehavior")
uml_TracedProtocolConformance = Class(name="uml::TracedProtocolConformance")
uml_TracedObjectFlow = Class(name="uml::TracedObjectFlow")
uml_TracedOperation = Class(name="uml::TracedOperation")
uml_TracedReadSelfAction = Class(name="uml::TracedReadSelfAction")
IntermediateActions_TracedReadStructuralFeatureActionActivation = Class(name="IntermediateActions::TracedReadStructuralFeatureActionActivation")
uml_TracedDecisionNode = Class(name="uml::TracedDecisionNode")
uml_TracedPackageMerge = Class(name="uml::TracedPackageMerge")
uml_TracedAcceptEventAction = Class(name="uml::TracedAcceptEventAction")
uml_TracedOccurrenceSpecification = Class(name="uml::TracedOccurrenceSpecification")
uml_TracedParameterSet = Class(name="uml::TracedParameterSet")
uml_TracedTransition = Class(name="uml::TracedTransition")
uml_TracedDurationInterval = Class(name="uml::TracedDurationInterval")
uml_TracedLinkEndData = Class(name="uml::TracedLinkEndData")
uml_TracedConnectableElementTemplateParameter = Class(name="uml::TracedConnectableElementTemplateParameter")
uml_TracedOperationTemplateParameter = Class(name="uml::TracedOperationTemplateParameter")
uml_TracedClause = Class(name="uml::TracedClause")
uml_TracedReplyAction = Class(name="uml::TracedReplyAction")
uml_TracedTrigger = Class(name="uml::TracedTrigger")
uml_TracedTemplateParameterSubstitution = Class(name="uml::TracedTemplateParameterSubstitution")
uml_TracedDuration = Class(name="uml::TracedDuration")
uml_TracedReduceAction = Class(name="uml::TracedReduceAction")
uml_TracedFinalState = Class(name="uml::TracedFinalState")
uml_TracedOpaqueAction = Class(name="uml::TracedOpaqueAction")
uml_TracedInformationItem = Class(name="uml::TracedInformationItem")
uml_TracedActionExecutionSpecification = Class(name="uml::TracedActionExecutionSpecification")
uml_TracedOutputPin = Class(name="uml::TracedOutputPin")
uml_TracedImage = Class(name="uml::TracedImage")
uml_TracedQualifierValue = Class(name="uml::TracedQualifierValue")
uml_TracedAddStructuralFeatureValueAction = Class(name="uml::TracedAddStructuralFeatureValueAction")
uml_TracedExpansionNode = Class(name="uml::TracedExpansionNode")
uml_TracedActivityParameterNode = Class(name="uml::TracedActivityParameterNode")
uml_TracedDevice = Class(name="uml::TracedDevice")
uml_TracedProperty = Class(name="uml::TracedProperty")
uml_TracedExtensionEnd = Class(name="uml::TracedExtensionEnd")
uml_TracedProfileApplication = Class(name="uml::TracedProfileApplication")
uml_TracedCallOperationAction = Class(name="uml::TracedCallOperationAction")
uml_TracedArtifact = Class(name="uml::TracedArtifact")
uml_TracedConnectorEnd = Class(name="uml::TracedConnectorEnd")
uml_TracedVariable = Class(name="uml::TracedVariable")
uml_TracedBehaviorExecutionSpecification = Class(name="uml::TracedBehaviorExecutionSpecification")
uml_TracedDurationObservation = Class(name="uml::TracedDurationObservation")
uml_TracedLiteralUnlimitedNatural = Class(name="uml::TracedLiteralUnlimitedNatural")
uml_TracedTemplateSignature = Class(name="uml::TracedTemplateSignature")
BasicActions_TracedOutputPinActivation = Class(name="BasicActions::TracedOutputPinActivation")
uml_TracedReadExtentAction = Class(name="uml::TracedReadExtentAction")
uml_TracedCallBehaviorAction = Class(name="uml::TracedCallBehaviorAction")
uml_TracedReadLinkObjectEndAction = Class(name="uml::TracedReadLinkObjectEndAction")
uml_TracedEnumeration = Class(name="uml::TracedEnumeration")
Kernel_TracedLiteralBooleanEvaluation = Class(name="Kernel::TracedLiteralBooleanEvaluation")
uml_TracedCommunicationPath = Class(name="uml::TracedCommunicationPath")
uml_TracedRaiseExceptionAction = Class(name="uml::TracedRaiseExceptionAction")
uml_TracedReadLinkAction = Class(name="uml::TracedReadLinkAction")
uml_TracedLinkEndDestructionData = Class(name="uml::TracedLinkEndDestructionData")
uml_TracedStringExpression = Class(name="uml::TracedStringExpression")
uml_TracedPrimitiveType = Class(name="uml::TracedPrimitiveType")
uml_TracedLiteralNull = Class(name="uml::TracedLiteralNull")
uml_TracedState = Class(name="uml::TracedState")
uml_TracedRegion = Class(name="uml::TracedRegion")
uml_TracedInclude = Class(name="uml::TracedInclude")
uml_TracedLiteralBoolean = Class(name="uml::TracedLiteralBoolean")
uml_TracedStartObjectBehaviorAction = Class(name="uml::TracedStartObjectBehaviorAction")
IntermediateActions_TracedValueSpecificationActionActivation = Class(name="IntermediateActions::TracedValueSpecificationActionActivation")
uml_TracedAddVariableValueAction = Class(name="uml::TracedAddVariableValueAction")
uml_TracedClearStructuralFeatureAction = Class(name="uml::TracedClearStructuralFeatureAction")
uml_TracedAssociation = Class(name="uml::TracedAssociation")
uml_TracedExpression = Class(name="uml::TracedExpression")
uml_TracedLiteralReal = Class(name="uml::TracedLiteralReal")
IntermediateActions_TracedCreateObjectActionActivation = Class(name="IntermediateActions::TracedCreateObjectActionActivation")
uml_TracedCollaboration = Class(name="uml::TracedCollaboration")
uml_TracedTestIdentityAction = Class(name="uml::TracedTestIdentityAction")
uml_TracedProfile = Class(name="uml::TracedProfile")
uml_TracedUnmarshallAction = Class(name="uml::TracedUnmarshallAction")
uml_TracedSlot = Class(name="uml::TracedSlot")
uml_TracedInterfaceRealization = Class(name="uml::TracedInterfaceRealization")
uml_TracedSendSignalAction = Class(name="uml::TracedSendSignalAction")
uml_TracedFunctionBehavior = Class(name="uml::TracedFunctionBehavior")
uml_TracedValueSpecificationAction = Class(name="uml::TracedValueSpecificationAction")
uml_TracedRemoveVariableValueAction = Class(name="uml::TracedRemoveVariableValueAction")
uml_TracedActor = Class(name="uml::TracedActor")
uml_TracedManifestation = Class(name="uml::TracedManifestation")
uml_TracedReadIsClassifiedObjectAction = Class(name="uml::TracedReadIsClassifiedObjectAction")
uml_TracedTemplateParameter = Class(name="uml::TracedTemplateParameter")
IntermediateActivities_TracedMergeNodeActivation = Class(name="IntermediateActivities::TracedMergeNodeActivation")
uml_TracedTimeExpression = Class(name="uml::TracedTimeExpression")
uml_TracedAbstraction = Class(name="uml::TracedAbstraction")
uml_TracedClearAssociationAction = Class(name="uml::TracedClearAssociationAction")
uml_TracedMergeNode = Class(name="uml::TracedMergeNode")
uml_TracedElementImport = Class(name="uml::TracedElementImport")
IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution = Class(name="IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution")
uml_TracedPseudostate = Class(name="uml::TracedPseudostate")
uml_TracedLinkEndCreationData = Class(name="uml::TracedLinkEndCreationData")
uml_TracedGate = Class(name="uml::TracedGate")
uml_TracedTimeObservation = Class(name="uml::TracedTimeObservation")
uml_TracedControlFlow = Class(name="uml::TracedControlFlow")
uml_TracedGeneralOrdering = Class(name="uml::TracedGeneralOrdering")
uml_TracedComponent = Class(name="uml::TracedComponent")
uml_TracedClassifierTemplateParameter = Class(name="uml::TracedClassifierTemplateParameter")
uml_TracedActivityFinalNode = Class(name="uml::TracedActivityFinalNode")
umlTrace_uml_TracedRedefinableElement = Class(name="umlTrace::uml::TracedRedefinableElement", is_abstract=True)
umlTrace_uml_TracedNamespace = Class(name="umlTrace::uml::TracedNamespace", is_abstract=True)
umlTrace_uml_TracedActivityGroup = Class(name="umlTrace::uml::TracedActivityGroup", is_abstract=True)
uml_TracedNamedElement = Class(name="uml::TracedNamedElement")
umlTrace_uml_TracedCreateLinkObjectAction = Class(name="umlTrace::uml::TracedCreateLinkObjectAction")
TracedCreateLinkAction = Class(name="TracedCreateLinkAction")
umlTrace_uml_TracedCreateLinkAction = Class(name="umlTrace::uml::TracedCreateLinkAction")
TracedWriteLinkAction = Class(name="TracedWriteLinkAction")
umlTrace_uml_TracedWriteLinkAction = Class(name="umlTrace::uml::TracedWriteLinkAction", is_abstract=True)
TracedLinkAction = Class(name="TracedLinkAction")
umlTrace_uml_TracedLinkAction = Class(name="umlTrace::uml::TracedLinkAction", is_abstract=True)
TracedAction = Class(name="TracedAction")
umlTrace_uml_TracedInitialNode = Class(name="umlTrace::uml::TracedInitialNode")
TracedControlNode = Class(name="TracedControlNode")
umlTrace_uml_TracedControlNode = Class(name="umlTrace::uml::TracedControlNode", is_abstract=True)
umlTrace_uml_TracedFlowFinalNode = Class(name="umlTrace::uml::TracedFlowFinalNode")
TracedFinalNode = Class(name="TracedFinalNode")
umlTrace_uml_TracedFinalNode = Class(name="umlTrace::uml::TracedFinalNode", is_abstract=True)
umlTrace_uml_TracedExpansionRegion = Class(name="umlTrace::uml::TracedExpansionRegion")
umlTrace_uml_TracedCreateObjectAction = Class(name="umlTrace::uml::TracedCreateObjectAction")
umlTrace_uml_TracedLifeline = Class(name="umlTrace::uml::TracedLifeline")
umlTrace_uml_TracedDurationConstraint = Class(name="umlTrace::uml::TracedDurationConstraint")
TracedIntervalConstraint = Class(name="TracedIntervalConstraint")
umlTrace_uml_TracedIntervalConstraint = Class(name="umlTrace::uml::TracedIntervalConstraint")
TracedConstraint = Class(name="TracedConstraint")
umlTrace_uml_TracedConstraint = Class(name="umlTrace::uml::TracedConstraint")
TracedPackageableElement = Class(name="TracedPackageableElement")
umlTrace_uml_TracedCombinedFragment = Class(name="umlTrace::uml::TracedCombinedFragment")
TracedInteractionFragment = Class(name="TracedInteractionFragment")
umlTrace_uml_TracedInteractionFragment = Class(name="umlTrace::uml::TracedInteractionFragment", is_abstract=True)
TracedNamedElement = Class(name="TracedNamedElement")
umlTrace_uml_TracedNamedElement = Class(name="umlTrace::uml::TracedNamedElement", is_abstract=True)
TracedElement = Class(name="TracedElement")
umlTrace_uml_TracedElement = Class(name="umlTrace::uml::TracedElement", is_abstract=True)
TracedEModelElement = Class(name="TracedEModelElement")
umlTrace_uml_TracedConditionalNode = Class(name="umlTrace::uml::TracedConditionalNode")
TracedStructuredActivityNode = Class(name="TracedStructuredActivityNode")
umlTrace_uml_TracedStructuredActivityNode = Class(name="umlTrace::uml::TracedStructuredActivityNode")
uml_TracedAction = Class(name="uml::TracedAction")
uml_TracedNamespace = Class(name="uml::TracedNamespace")
uml_TracedActivityGroup = Class(name="uml::TracedActivityGroup")
umlTrace_uml_TracedAction = Class(name="umlTrace::uml::TracedAction", is_abstract=True)
TracedExecutableNode = Class(name="TracedExecutableNode")
umlTrace_uml_TracedExecutableNode = Class(name="umlTrace::uml::TracedExecutableNode", is_abstract=True)
TracedActivityNode = Class(name="TracedActivityNode")
umlTrace_uml_TracedActivityNode = Class(name="umlTrace::uml::TracedActivityNode", is_abstract=True)
uml_TracedRedefinableElement = Class(name="uml::TracedRedefinableElement")
ActivityContent = Class(name="ActivityContent")
umlTrace_uml_TracedInvocationAction = Class(name="umlTrace::uml::TracedInvocationAction", is_abstract=True)
umlTrace_uml_TracedOpaqueAction = Class(name="umlTrace::uml::TracedOpaqueAction")
umlTrace_uml_TracedProtocolConformance = Class(name="umlTrace::uml::TracedProtocolConformance")
TracedDirectedRelationship = Class(name="TracedDirectedRelationship")
umlTrace_uml_TracedDirectedRelationship = Class(name="umlTrace::uml::TracedDirectedRelationship", is_abstract=True)
TracedRelationship = Class(name="TracedRelationship")
umlTrace_uml_TracedRelationship = Class(name="umlTrace::uml::TracedRelationship", is_abstract=True)
umlTrace_uml_TracedCallBehaviorAction = Class(name="umlTrace::uml::TracedCallBehaviorAction")
TracedCallAction = Class(name="TracedCallAction")
umlTrace_uml_TracedCallAction = Class(name="umlTrace::uml::TracedCallAction", is_abstract=True)
umlTrace_uml_TracedPackageImport = Class(name="umlTrace::uml::TracedPackageImport")
umlTrace_uml_TracedClass = Class(name="umlTrace::uml::TracedClass")
uml_TracedEncapsulatedClassifier = Class(name="uml::TracedEncapsulatedClassifier")
uml_TracedBehavioredClassifier = Class(name="uml::TracedBehavioredClassifier")
umlTrace_uml_TracedEncapsulatedClassifier = Class(name="umlTrace::uml::TracedEncapsulatedClassifier", is_abstract=True)
TracedStructuredClassifier = Class(name="TracedStructuredClassifier")
umlTrace_uml_TracedStructuredClassifier = Class(name="umlTrace::uml::TracedStructuredClassifier", is_abstract=True)
TracedClassifier = Class(name="TracedClassifier")
umlTrace_uml_TracedClassifier = Class(name="umlTrace::uml::TracedClassifier", is_abstract=True)
uml_TracedType = Class(name="uml::TracedType")
umlTrace_uml_TracedType = Class(name="umlTrace::uml::TracedType", is_abstract=True)
umlTrace_uml_TracedBehavioredClassifier = Class(name="umlTrace::uml::TracedBehavioredClassifier", is_abstract=True)
umlTrace_uml_TracedActivityFinalNode = Class(name="umlTrace::uml::TracedActivityFinalNode")
umlTrace_uml_TracedObservation = Class(name="umlTrace::uml::TracedObservation", is_abstract=True)
umlTrace_uml_TracedInteractionUse = Class(name="umlTrace::uml::TracedInteractionUse")
umlTrace_uml_TracedLoopNode = Class(name="umlTrace::uml::TracedLoopNode")
umlTrace_uml_TracedSignal = Class(name="umlTrace::uml::TracedSignal")
umlTrace_uml_TracedPackageableElement = Class(name="umlTrace::uml::TracedPackageableElement", is_abstract=True)
uml_TracedParameterableElement = Class(name="uml::TracedParameterableElement")
umlTrace_uml_TracedParameterableElement = Class(name="umlTrace::uml::TracedParameterableElement", is_abstract=True)
umlTrace_uml_TracedPseudostate = Class(name="umlTrace::uml::TracedPseudostate")
TracedVertex = Class(name="TracedVertex")
umlTrace_uml_TracedVertex = Class(name="umlTrace::uml::TracedVertex", is_abstract=True)
umlTrace_uml_TracedDestructionOccurrenceSpecification = Class(name="umlTrace::uml::TracedDestructionOccurrenceSpecification")
TracedMessageOccurrenceSpecification = Class(name="TracedMessageOccurrenceSpecification")
umlTrace_uml_TracedMessageOccurrenceSpecification = Class(name="umlTrace::uml::TracedMessageOccurrenceSpecification")
uml_TracedMessageEnd = Class(name="uml::TracedMessageEnd")
umlTrace_uml_TracedOccurrenceSpecification = Class(name="umlTrace::uml::TracedOccurrenceSpecification")
umlTrace_uml_TracedMessageEnd = Class(name="umlTrace::uml::TracedMessageEnd", is_abstract=True)
umlTrace_uml_TracedPackage = Class(name="umlTrace::uml::TracedPackage")
uml_TracedPackageableElement = Class(name="uml::TracedPackageableElement")
uml_TracedTemplateableElement = Class(name="uml::TracedTemplateableElement")
umlTrace_uml_TracedTemplateableElement = Class(name="umlTrace::uml::TracedTemplateableElement", is_abstract=True)
umlTrace_uml_TracedConnector = Class(name="umlTrace::uml::TracedConnector")
TracedFeature = Class(name="TracedFeature")
umlTrace_uml_TracedFeature = Class(name="umlTrace::uml::TracedFeature", is_abstract=True)
TracedRedefinableElement = Class(name="TracedRedefinableElement")
umlTrace_uml_TracedSendObjectAction = Class(name="umlTrace::uml::TracedSendObjectAction")
TracedInvocationAction = Class(name="TracedInvocationAction")
umlTrace_uml_TracedInputPin = Class(name="umlTrace::uml::TracedInputPin")
TracedPin = Class(name="TracedPin")
umlTrace_uml_TracedPin = Class(name="umlTrace::uml::TracedPin", is_abstract=True)
uml_TracedObjectNode = Class(name="uml::TracedObjectNode")
umlTrace_uml_TracedObjectNode = Class(name="umlTrace::uml::TracedObjectNode", is_abstract=True)
uml_TracedActivityNode = Class(name="uml::TracedActivityNode")
umlTrace_uml_TracedDeploymentSpecification = Class(name="umlTrace::uml::TracedDeploymentSpecification")
TracedArtifact = Class(name="TracedArtifact")
umlTrace_uml_TracedArtifact = Class(name="umlTrace::uml::TracedArtifact")
uml_TracedClassifier = Class(name="uml::TracedClassifier")
uml_TracedDeployedArtifact = Class(name="uml::TracedDeployedArtifact")
umlTrace_uml_TracedDeployedArtifact = Class(name="umlTrace::uml::TracedDeployedArtifact", is_abstract=True)
umlTrace_uml_TracedTransition = Class(name="umlTrace::uml::TracedTransition")
umlTrace_uml_TracedNode = Class(name="umlTrace::uml::TracedNode")
umlTrace_uml_TracedExceptionHandler = Class(name="umlTrace::uml::TracedExceptionHandler")
umlTrace_uml_TracedSequenceNode = Class(name="umlTrace::uml::TracedSequenceNode")
umlTrace_uml_TracedUseCase = Class(name="umlTrace::uml::TracedUseCase")
TracedBehavioredClassifier = Class(name="TracedBehavioredClassifier")
umlTrace_uml_TracedStartClassifierBehaviorAction = Class(name="umlTrace::uml::TracedStartClassifierBehaviorAction")
umlTrace_uml_TracedExtend = Class(name="umlTrace::uml::TracedExtend")
umlTrace_uml_TracedRemoveStructuralFeatureValueAction = Class(name="umlTrace::uml::TracedRemoveStructuralFeatureValueAction")
TracedWriteStructuralFeatureAction = Class(name="TracedWriteStructuralFeatureAction")
umlTrace_uml_TracedWriteStructuralFeatureAction = Class(name="umlTrace::uml::TracedWriteStructuralFeatureAction", is_abstract=True)
TracedStructuralFeatureAction = Class(name="TracedStructuralFeatureAction")
umlTrace_uml_TracedStructuralFeatureAction = Class(name="umlTrace::uml::TracedStructuralFeatureAction", is_abstract=True)
umlTrace_uml_TracedReadLinkAction = Class(name="umlTrace::uml::TracedReadLinkAction")
umlTrace_uml_TracedGeneralizationSet = Class(name="umlTrace::uml::TracedGeneralizationSet")
umlTrace_uml_TracedChangeEvent = Class(name="umlTrace::uml::TracedChangeEvent")
TracedEvent = Class(name="TracedEvent")
umlTrace_uml_TracedEvent = Class(name="umlTrace::uml::TracedEvent", is_abstract=True)
umlTrace_uml_TracedDependency = Class(name="umlTrace::uml::TracedDependency")
uml_TracedDirectedRelationship = Class(name="uml::TracedDirectedRelationship")
umlTrace_uml_TracedPort = Class(name="umlTrace::uml::TracedPort")
TracedProperty = Class(name="TracedProperty")
umlTrace_uml_TracedProperty = Class(name="umlTrace::uml::TracedProperty")
uml_TracedStructuralFeature = Class(name="uml::TracedStructuralFeature")
uml_TracedConnectableElement = Class(name="uml::TracedConnectableElement")
uml_TracedDeploymentTarget = Class(name="uml::TracedDeploymentTarget")
umlTrace_uml_TracedStructuralFeature = Class(name="umlTrace::uml::TracedStructuralFeature", is_abstract=True)
uml_TracedFeature = Class(name="uml::TracedFeature")
uml_TracedTypedElement = Class(name="uml::TracedTypedElement")
uml_TracedMultiplicityElement = Class(name="uml::TracedMultiplicityElement")
umlTrace_uml_TracedTypedElement = Class(name="umlTrace::uml::TracedTypedElement", is_abstract=True)
umlTrace_uml_TracedMultiplicityElement = Class(name="umlTrace::uml::TracedMultiplicityElement", is_abstract=True)
umlTrace_uml_TracedConnectableElement = Class(name="umlTrace::uml::TracedConnectableElement", is_abstract=True)
umlTrace_uml_TracedDeploymentTarget = Class(name="umlTrace::uml::TracedDeploymentTarget", is_abstract=True)
umlTrace_uml_TracedCollaborationUse = Class(name="umlTrace::uml::TracedCollaborationUse")
umlTrace_uml_TracedValuePin = Class(name="umlTrace::uml::TracedValuePin")
TracedInputPin = Class(name="TracedInputPin")
umlTrace_uml_TracedBehavior = Class(name="umlTrace::uml::TracedBehavior", is_abstract=True)
TracedClass = Class(name="TracedClass")
umlTrace_uml_TracedSlot = Class(name="umlTrace::uml::TracedSlot")
umlTrace_uml_TracedLiteralNull = Class(name="umlTrace::uml::TracedLiteralNull")
umlTrace_uml_TracedParameter = Class(name="umlTrace::uml::TracedParameter")
umlTrace_uml_TracedOpaqueExpression = Class(name="umlTrace::uml::TracedOpaqueExpression")
umlTrace_uml_TracedTrigger = Class(name="umlTrace::uml::TracedTrigger")
umlTrace_uml_TracedStateInvariant = Class(name="umlTrace::uml::TracedStateInvariant")
umlTrace_uml_TracedAssociationClass = Class(name="umlTrace::uml::TracedAssociationClass")
umlTrace_uml_TracedInstanceSpecification = Class(name="umlTrace::uml::TracedInstanceSpecification")
umlTrace_uml_TracedTemplateSignature = Class(name="umlTrace::uml::TracedTemplateSignature")
umlTrace_uml_TracedLinkEndDestructionData = Class(name="umlTrace::uml::TracedLinkEndDestructionData")
TracedLinkEndData = Class(name="TracedLinkEndData")
umlTrace_uml_TracedLinkEndData = Class(name="umlTrace::uml::TracedLinkEndData")
umlTrace_uml_TracedAcceptCallAction = Class(name="umlTrace::uml::TracedAcceptCallAction")
TracedAcceptEventAction = Class(name="TracedAcceptEventAction")
umlTrace_uml_TracedAcceptEventAction = Class(name="umlTrace::uml::TracedAcceptEventAction")
umlTrace_uml_TracedReduceAction = Class(name="umlTrace::uml::TracedReduceAction")
umlTrace_uml_TracedRaiseExceptionAction = Class(name="umlTrace::uml::TracedRaiseExceptionAction")
umlTrace_uml_TracedStereotype = Class(name="umlTrace::uml::TracedStereotype")
umlTrace_uml_TracedClearAssociationAction = Class(name="umlTrace::uml::TracedClearAssociationAction")
umlTrace_uml_TracedEnumerationLiteral = Class(name="umlTrace::uml::TracedEnumerationLiteral")
TracedInstanceSpecification = Class(name="TracedInstanceSpecification")
umlTrace_uml_TracedSubstitution = Class(name="umlTrace::uml::TracedSubstitution")
TracedRealization = Class(name="TracedRealization")
umlTrace_uml_TracedExtension = Class(name="umlTrace::uml::TracedExtension")
TracedAssociation = Class(name="TracedAssociation")
umlTrace_uml_TracedAssociation = Class(name="umlTrace::uml::TracedAssociation")
uml_TracedRelationship = Class(name="uml::TracedRelationship")
umlTrace_uml_TracedExecutionEnvironment = Class(name="umlTrace::uml::TracedExecutionEnvironment")
TracedNode = Class(name="TracedNode")
umlTrace_uml_TracedConsiderIgnoreFragment = Class(name="umlTrace::uml::TracedConsiderIgnoreFragment")
TracedCombinedFragment = Class(name="TracedCombinedFragment")
umlTrace_uml_TracedContinuation = Class(name="umlTrace::uml::TracedContinuation")
umlTrace_uml_TracedCallOperationAction = Class(name="umlTrace::uml::TracedCallOperationAction")
umlTrace_uml_TracedTimeConstraint = Class(name="umlTrace::uml::TracedTimeConstraint")
umlTrace_uml_TracedClearVariableAction = Class(name="umlTrace::uml::TracedClearVariableAction")
TracedVariableAction = Class(name="TracedVariableAction")
umlTrace_uml_TracedVariableAction = Class(name="umlTrace::uml::TracedVariableAction", is_abstract=True)
umlTrace_uml_TracedReadSelfAction = Class(name="umlTrace::uml::TracedReadSelfAction")
umlTrace_uml_TracedLiteralString = Class(name="umlTrace::uml::TracedLiteralString")
TracedLiteralSpecification = Class(name="TracedLiteralSpecification")
umlTrace_uml_TracedLiteralSpecification = Class(name="umlTrace::uml::TracedLiteralSpecification", is_abstract=True)
TracedValueSpecification = Class(name="TracedValueSpecification")
umlTrace_uml_TracedValueSpecification = Class(name="umlTrace::uml::TracedValueSpecification", is_abstract=True)
umlTrace_uml_TracedBroadcastSignalAction = Class(name="umlTrace::uml::TracedBroadcastSignalAction")
umlTrace_uml_TracedInteraction = Class(name="umlTrace::uml::TracedInteraction")
uml_TracedBehavior = Class(name="uml::TracedBehavior")
uml_TracedInteractionFragment = Class(name="uml::TracedInteractionFragment")
umlTrace_uml_TracedActivityEdge = Class(name="umlTrace::uml::TracedActivityEdge", is_abstract=True)
umlTrace_uml_TracedTestIdentityAction = Class(name="umlTrace::uml::TracedTestIdentityAction")
umlTrace_uml_TracedInstanceValue = Class(name="umlTrace::uml::TracedInstanceValue")
umlTrace_uml_TracedLiteralUnlimitedNatural = Class(name="umlTrace::uml::TracedLiteralUnlimitedNatural")
umlTrace_uml_TracedReclassifyObjectAction = Class(name="umlTrace::uml::TracedReclassifyObjectAction")
umlTrace_uml_TracedTimeEvent = Class(name="umlTrace::uml::TracedTimeEvent")
umlTrace_uml_TracedPartDecomposition = Class(name="umlTrace::uml::TracedPartDecomposition")
TracedInteractionUse = Class(name="TracedInteractionUse")
umlTrace_uml_TracedInterruptibleActivityRegion = Class(name="umlTrace::uml::TracedInterruptibleActivityRegion")
umlTrace_uml_TracedAddVariableValueAction = Class(name="umlTrace::uml::TracedAddVariableValueAction")
TracedWriteVariableAction = Class(name="TracedWriteVariableAction")
umlTrace_uml_TracedWriteVariableAction = Class(name="umlTrace::uml::TracedWriteVariableAction", is_abstract=True)
umlTrace_uml_TracedProtocolTransition = Class(name="umlTrace::uml::TracedProtocolTransition")
TracedTransition = Class(name="TracedTransition")
umlTrace_uml_TracedImage = Class(name="umlTrace::uml::TracedImage")
umlTrace_uml_TracedLiteralReal = Class(name="umlTrace::uml::TracedLiteralReal")
umlTrace_uml_TracedInteractionOperand = Class(name="umlTrace::uml::TracedInteractionOperand")
umlTrace_uml_TracedGeneralization = Class(name="umlTrace::uml::TracedGeneralization")
umlTrace_uml_TracedInformationItem = Class(name="umlTrace::uml::TracedInformationItem")
umlTrace_uml_TracedModel = Class(name="umlTrace::uml::TracedModel")
TracedPackage = Class(name="TracedPackage")
umlTrace_uml_TracedClassifierTemplateParameter = Class(name="umlTrace::uml::TracedClassifierTemplateParameter")
TracedTemplateParameter = Class(name="TracedTemplateParameter")
umlTrace_uml_TracedTemplateParameter = Class(name="umlTrace::uml::TracedTemplateParameter")
umlTrace_uml_TracedOperation = Class(name="umlTrace::uml::TracedOperation")
umlTrace_uml_TracedRealization = Class(name="umlTrace::uml::TracedRealization")
TracedAbstraction = Class(name="TracedAbstraction")
umlTrace_uml_TracedAbstraction = Class(name="umlTrace::uml::TracedAbstraction")
TracedDependency = Class(name="TracedDependency")
umlTrace_uml_TracedExecutionSpecification = Class(name="umlTrace::uml::TracedExecutionSpecification", is_abstract=True)
umlTrace_uml_TracedReplyAction = Class(name="umlTrace::uml::TracedReplyAction")
umlTrace_uml_TracedActor = Class(name="umlTrace::uml::TracedActor")
umlTrace_uml_TracedInformationFlow = Class(name="umlTrace::uml::TracedInformationFlow")
umlTrace_uml_TracedDestroyObjectAction = Class(name="umlTrace::uml::TracedDestroyObjectAction")
umlTrace_uml_TracedActivityPartition = Class(name="umlTrace::uml::TracedActivityPartition")
TracedActivityGroup = Class(name="TracedActivityGroup")
umlTrace_uml_TracedStateMachine = Class(name="umlTrace::uml::TracedStateMachine")
TracedBehavior = Class(name="TracedBehavior")
umlTrace_uml_TracedMessage = Class(name="umlTrace::uml::TracedMessage")
umlTrace_uml_TracedReadLinkObjectEndQualifierAction = Class(name="umlTrace::uml::TracedReadLinkObjectEndQualifierAction")
umlTrace_uml_TracedDeployment = Class(name="umlTrace::uml::TracedDeployment")
umlTrace_uml_TracedActivity = Class(name="umlTrace::uml::TracedActivity")
umlTrace_uml_TracedForkNode = Class(name="umlTrace::uml::TracedForkNode")
umlTrace_uml_TracedProtocolStateMachine = Class(name="umlTrace::uml::TracedProtocolStateMachine")
TracedStateMachine = Class(name="TracedStateMachine")
umlTrace_uml_TracedInterval = Class(name="umlTrace::uml::TracedInterval")
umlTrace_uml_TracedClearStructuralFeatureAction = Class(name="umlTrace::uml::TracedClearStructuralFeatureAction")
umlTrace_uml_TracedObjectFlow = Class(name="umlTrace::uml::TracedObjectFlow")
TracedActivityEdge = Class(name="TracedActivityEdge")
umlTrace_uml_TracedLiteralInteger = Class(name="umlTrace::uml::TracedLiteralInteger")
umlTrace_uml_TracedSignalEvent = Class(name="umlTrace::uml::TracedSignalEvent")
umlTrace_uml_TracedReadLinkObjectEndAction = Class(name="umlTrace::uml::TracedReadLinkObjectEndAction")
umlTrace_uml_TracedTimeInterval = Class(name="umlTrace::uml::TracedTimeInterval")
TracedInterval = Class(name="TracedInterval")
umlTrace_uml_TracedOperationTemplateParameter = Class(name="umlTrace::uml::TracedOperationTemplateParameter")
umlTrace_uml_TracedDurationObservation = Class(name="umlTrace::uml::TracedDurationObservation")
TracedObservation = Class(name="TracedObservation")
umlTrace_uml_TracedConnectionPointReference = Class(name="umlTrace::uml::TracedConnectionPointReference")
umlTrace_uml_TracedTimeExpression = Class(name="umlTrace::uml::TracedTimeExpression")
umlTrace_uml_TracedQualifierValue = Class(name="umlTrace::uml::TracedQualifierValue")
umlTrace_uml_TracedDurationInterval = Class(name="umlTrace::uml::TracedDurationInterval")
umlTrace_uml_TracedFunctionBehavior = Class(name="umlTrace::uml::TracedFunctionBehavior")
TracedOpaqueBehavior = Class(name="TracedOpaqueBehavior")
umlTrace_uml_TracedOpaqueBehavior = Class(name="umlTrace::uml::TracedOpaqueBehavior")
umlTrace_uml_TracedInterfaceRealization = Class(name="umlTrace::uml::TracedInterfaceRealization")
umlTrace_uml_TracedDevice = Class(name="umlTrace::uml::TracedDevice")
umlTrace_uml_TracedTemplateParameterSubstitution = Class(name="umlTrace::uml::TracedTemplateParameterSubstitution")
umlTrace_uml_TracedJoinNode = Class(name="umlTrace::uml::TracedJoinNode")
umlTrace_uml_TracedRedefinableTemplateSignature = Class(name="umlTrace::uml::TracedRedefinableTemplateSignature")
umlTrace_uml_TracedReadIsClassifiedObjectAction = Class(name="umlTrace::uml::TracedReadIsClassifiedObjectAction")
umlTrace_uml_TracedTimeObservation = Class(name="umlTrace::uml::TracedTimeObservation")
umlTrace_uml_TracedDecisionNode = Class(name="umlTrace::uml::TracedDecisionNode")
umlTrace_uml_TracedElementImport = Class(name="umlTrace::uml::TracedElementImport")
uml_TracedBehavioralFeature = Class(name="uml::TracedBehavioralFeature")
umlTrace_uml_TracedBehavioralFeature = Class(name="umlTrace::uml::TracedBehavioralFeature", is_abstract=True)
umlTrace_uml_TracedAnyReceiveEvent = Class(name="umlTrace::uml::TracedAnyReceiveEvent")
TracedMessageEvent = Class(name="TracedMessageEvent")
umlTrace_uml_TracedMessageEvent = Class(name="umlTrace::uml::TracedMessageEvent", is_abstract=True)
umlTrace_uml_TracedPrimitiveType = Class(name="umlTrace::uml::TracedPrimitiveType")
TracedDataType = Class(name="TracedDataType")
umlTrace_uml_TracedDataType = Class(name="umlTrace::uml::TracedDataType")
umlTrace_uml_TracedReadStructuralFeatureAction = Class(name="umlTrace::uml::TracedReadStructuralFeatureAction")
umlTrace_uml_TracedParameterSet = Class(name="umlTrace::uml::TracedParameterSet")
umlTrace_uml_TracedDataStoreNode = Class(name="umlTrace::uml::TracedDataStoreNode")
TracedCentralBufferNode = Class(name="TracedCentralBufferNode")
umlTrace_uml_TracedCentralBufferNode = Class(name="umlTrace::uml::TracedCentralBufferNode")
TracedObjectNode = Class(name="TracedObjectNode")
umlTrace_uml_TracedSendSignalAction = Class(name="umlTrace::uml::TracedSendSignalAction")
umlTrace_uml_TracedReception = Class(name="umlTrace::uml::TracedReception")
TracedBehavioralFeature = Class(name="TracedBehavioralFeature")
umlTrace_uml_TracedTemplateBinding = Class(name="umlTrace::uml::TracedTemplateBinding")
umlTrace_uml_TracedUsage = Class(name="umlTrace::uml::TracedUsage")
umlTrace_uml_TracedActionInputPin = Class(name="umlTrace::uml::TracedActionInputPin")
umlTrace_uml_TracedReadVariableAction = Class(name="umlTrace::uml::TracedReadVariableAction")
umlTrace_uml_TracedDestroyLinkAction = Class(name="umlTrace::uml::TracedDestroyLinkAction")
umlTrace_uml_TracedOutputPin = Class(name="umlTrace::uml::TracedOutputPin")
umlTrace_uml_TracedDuration = Class(name="umlTrace::uml::TracedDuration")
umlTrace_uml_TracedUnmarshallAction = Class(name="umlTrace::uml::TracedUnmarshallAction")
umlTrace_uml_TracedProfile = Class(name="umlTrace::uml::TracedProfile")
umlTrace_uml_TracedExtensionEnd = Class(name="umlTrace::uml::TracedExtensionEnd")
umlTrace_uml_TracedExpansionNode = Class(name="umlTrace::uml::TracedExpansionNode")
umlTrace_uml_TracedActivityParameterNode = Class(name="umlTrace::uml::TracedActivityParameterNode")
umlTrace_uml_TracedProfileApplication = Class(name="umlTrace::uml::TracedProfileApplication")
umlTrace_uml_TracedConnectorEnd = Class(name="umlTrace::uml::TracedConnectorEnd")
TracedMultiplicityElement = Class(name="TracedMultiplicityElement")
umlTrace_uml_TracedEnumeration = Class(name="umlTrace::uml::TracedEnumeration")
umlTrace_uml_TracedCollaboration = Class(name="umlTrace::uml::TracedCollaboration")
uml_TracedStructuredClassifier = Class(name="uml::TracedStructuredClassifier")
umlTrace_uml_TracedVariable = Class(name="umlTrace::uml::TracedVariable")
umlTrace_uml_TracedValueSpecificationAction = Class(name="umlTrace::uml::TracedValueSpecificationAction")
umlTrace_uml_TracedReadExtentAction = Class(name="umlTrace::uml::TracedReadExtentAction")
umlTrace_uml_TracedStringExpression = Class(name="umlTrace::uml::TracedStringExpression")
umlTrace_uml_TracedExpression = Class(name="umlTrace::uml::TracedExpression")
umlTrace_uml_TracedGeneralOrdering = Class(name="umlTrace::uml::TracedGeneralOrdering")
umlTrace_uml_TracedLiteralBoolean = Class(name="umlTrace::uml::TracedLiteralBoolean")
umlTrace_uml_TracedStartObjectBehaviorAction = Class(name="umlTrace::uml::TracedStartObjectBehaviorAction")
umlTrace_uml_TracedRegion = Class(name="umlTrace::uml::TracedRegion")
umlTrace_uml_TracedExtensionPoint = Class(name="umlTrace::uml::TracedExtensionPoint")
umlTrace_uml_TracedExecutionOccurrenceSpecification = Class(name="umlTrace::uml::TracedExecutionOccurrenceSpecification")
TracedOccurrenceSpecification = Class(name="TracedOccurrenceSpecification")
umlTrace_uml_TracedInteractionConstraint = Class(name="umlTrace::uml::TracedInteractionConstraint")
umlTrace_uml_TracedAddStructuralFeatureValueAction = Class(name="umlTrace::uml::TracedAddStructuralFeatureValueAction")
umlTrace_uml_TracedInterface = Class(name="umlTrace::uml::TracedInterface")
umlTrace_uml_TracedComponent = Class(name="umlTrace::uml::TracedComponent")
umlTrace_uml_TracedCallEvent = Class(name="umlTrace::uml::TracedCallEvent")
umlTrace_uml_TracedComment = Class(name="umlTrace::uml::TracedComment")
umlTrace_uml_TracedBehaviorExecutionSpecification = Class(name="umlTrace::uml::TracedBehaviorExecutionSpecification")
TracedExecutionSpecification = Class(name="TracedExecutionSpecification")
umlTrace_uml_TracedComponentRealization = Class(name="umlTrace::uml::TracedComponentRealization")
umlTrace_uml_TracedCommunicationPath = Class(name="umlTrace::uml::TracedCommunicationPath")
umlTrace_uml_TracedPackageMerge = Class(name="umlTrace::uml::TracedPackageMerge")
umlTrace_uml_TracedClause = Class(name="umlTrace::uml::TracedClause")
umlTrace_uml_TracedFinalState = Class(name="umlTrace::uml::TracedFinalState")
TracedState = Class(name="TracedState")
umlTrace_uml_TracedState = Class(name="umlTrace::uml::TracedState")
uml_TracedVertex = Class(name="uml::TracedVertex")
umlTrace_uml_TracedConnectableElementTemplateParameter = Class(name="umlTrace::uml::TracedConnectableElementTemplateParameter")
umlTrace_uml_TracedActionExecutionSpecification = Class(name="umlTrace::uml::TracedActionExecutionSpecification")
umlTrace_IntermediateActivities_TracedObjectNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedObjectNodeActivation", is_abstract=True)
umlTrace_IntermediateActivities_TracedInitialNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedInitialNodeActivation")
umlTrace_IntermediateActivities_TracedActivityExecution = Class(name="umlTrace::IntermediateActivities::TracedActivityExecution")
TracedExecution = Class(name="TracedExecution")
umlTrace_IntermediateActivities_TracedMergeNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedMergeNodeActivation")
umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedActivityParameterNodeActivation")
TracedObjectNodeActivation = Class(name="TracedObjectNodeActivation")
umlTrace_IntermediateActivities_TracedJoinNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedJoinNodeActivation")
umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedActivityFinalNodeActivation")
umlTrace_IntermediateActivities_TracedDecisionNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedDecisionNodeActivation")
umlTrace_Loci_TracedSemanticVisitor = Class(name="umlTrace::Loci::TracedSemanticVisitor")
umlTrace_BasicActions_TracedPinActivation = Class(name="umlTrace::BasicActions::TracedPinActivation", is_abstract=True)
umlTrace_BasicActions_TracedActionActivation = Class(name="umlTrace::BasicActions::TracedActionActivation", is_abstract=True)
umlTrace_uml_TracedInclude = Class(name="umlTrace::uml::TracedInclude")
umlTrace_uml_TracedControlFlow = Class(name="umlTrace::uml::TracedControlFlow")
umlTrace_uml_TracedGate = Class(name="umlTrace::uml::TracedGate")
TracedMessageEnd = Class(name="TracedMessageEnd")
umlTrace_uml_TracedRemoveVariableValueAction = Class(name="umlTrace::uml::TracedRemoveVariableValueAction")
umlTrace_uml_TracedManifestation = Class(name="umlTrace::uml::TracedManifestation")
umlTrace_uml_TracedLinkEndCreationData = Class(name="umlTrace::uml::TracedLinkEndCreationData")
umlTrace_uml_TracedMergeNode = Class(name="umlTrace::uml::TracedMergeNode")
umlTrace_ecore_TracedEModelElement = Class(name="umlTrace::ecore::TracedEModelElement", is_abstract=True)
umlTrace_IntermediateActivities_TracedForkNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedForkNodeActivation")
TracedControlNodeActivation = Class(name="TracedControlNodeActivation")
umlTrace_IntermediateActivities_TracedControlNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedControlNodeActivation", is_abstract=True)
TracedActivityNodeActivation = Class(name="TracedActivityNodeActivation")
umlTrace_IntermediateActivities_TracedActivityNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedActivityNodeActivation")
TracedSemanticVisitor = Class(name="TracedSemanticVisitor")
umlTrace_IntermediateActions_TracedCreateObjectActionActivation = Class(name="umlTrace::IntermediateActions::TracedCreateObjectActionActivation")
umlTrace_BasicBehaviors_TracedExecution = Class(name="umlTrace::BasicBehaviors::TracedExecution", is_abstract=True)
TracedObject = Class(name="TracedObject")
umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution = Class(name="umlTrace::BasicBehaviors::TracedOpaqueBehaviorExecution", is_abstract=True)
umlTrace_Kernel_TracedObject = Class(name="umlTrace::Kernel::TracedObject")
TracedExtensionalValue = Class(name="TracedExtensionalValue")
umlTrace_Kernel_TracedExtensionalValue = Class(name="umlTrace::Kernel::TracedExtensionalValue", is_abstract=True)
TracedCompoundValue = Class(name="TracedCompoundValue")
umlTrace_Kernel_TracedCompoundValue = Class(name="umlTrace::Kernel::TracedCompoundValue", is_abstract=True)
TracedStructuredValue = Class(name="TracedStructuredValue")
umlTrace_Kernel_TracedStructuredValue = Class(name="umlTrace::Kernel::TracedStructuredValue", is_abstract=True)
TracedValue = Class(name="TracedValue")
umlTrace_Kernel_TracedValue = Class(name="umlTrace::Kernel::TracedValue", is_abstract=True)
umlTrace_Kernel_TracedReference = Class(name="umlTrace::Kernel::TracedReference")
umlTrace_Kernel_TracedLiteralEvaluation = Class(name="umlTrace::Kernel::TracedLiteralEvaluation", is_abstract=True)
TracedEvaluation = Class(name="TracedEvaluation")
umlTrace_Kernel_TracedEvaluation = Class(name="umlTrace::Kernel::TracedEvaluation", is_abstract=True)
umlTrace_Kernel_TracedIntegerValue = Class(name="umlTrace::Kernel::TracedIntegerValue")
TracedPrimitiveValue = Class(name="TracedPrimitiveValue")
umlTrace_BasicActions_TracedInvocationActionActivation = Class(name="umlTrace::BasicActions::TracedInvocationActionActivation", is_abstract=True)
TracedActionActivation = Class(name="TracedActionActivation")
umlTrace_BasicActions_TracedCallActionActivation = Class(name="umlTrace::BasicActions::TracedCallActionActivation", is_abstract=True)
TracedInvocationActionActivation = Class(name="TracedInvocationActionActivation")
umlTrace_BasicActions_TracedOpaqueActionActivation = Class(name="umlTrace::BasicActions::TracedOpaqueActionActivation")
umlTrace_BasicActions_TracedInputPinActivation = Class(name="umlTrace::BasicActions::TracedInputPinActivation")
TracedPinActivation = Class(name="TracedPinActivation")
umlTrace_BasicActions_TracedCallBehaviorActionActivation = Class(name="umlTrace::BasicActions::TracedCallBehaviorActionActivation")
TracedCallActionActivation = Class(name="TracedCallActionActivation")
umlTrace_BasicActions_TracedOutputPinActivation = Class(name="umlTrace::BasicActions::TracedOutputPinActivation")
umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation = Class(name="umlTrace::IntermediateActions::TracedStructuralFeatureActionActivation", is_abstract=True)
umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation = Class(name="umlTrace::IntermediateActions::TracedReadStructuralFeatureActionActivation")
TracedStructuralFeatureActionActivation = Class(name="TracedStructuralFeatureActionActivation")
umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation = Class(name="umlTrace::IntermediateActions::TracedAddStructuralFeatureValueActionActivation")
TracedWriteStructuralFeatureActionActivation = Class(name="TracedWriteStructuralFeatureActionActivation")
umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation = Class(name="umlTrace::IntermediateActions::TracedWriteStructuralFeatureActionActivation", is_abstract=True)
umlTrace_IntermediateActions_TracedValueSpecificationActionActivation = Class(name="umlTrace::IntermediateActions::TracedValueSpecificationActionActivation")
umlTrace_Values_ActionActivation_firing_Value = Class(name="umlTrace::Values::ActionActivation::firing::Value")
BasicActions_TracedActionActivation = Class(name="BasicActions::TracedActionActivation")
uml_ActivityContent = Class(name="uml::ActivityContent", is_abstract=True)
umlTrace_Kernel_TracedPrimitiveValue = Class(name="umlTrace::Kernel::TracedPrimitiveValue", is_abstract=True)
umlTrace_Kernel_TracedLiteralBooleanEvaluation = Class(name="umlTrace::Kernel::TracedLiteralBooleanEvaluation")
TracedLiteralEvaluation = Class(name="TracedLiteralEvaluation")
umlTrace_Kernel_TracedBooleanValue = Class(name="umlTrace::Kernel::TracedBooleanValue")
umlTrace_Kernel_TracedLiteralIntegerEvaluation = Class(name="umlTrace::Kernel::TracedLiteralIntegerEvaluation")
umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution = Class(name="umlTrace::IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution")
TracedOpaqueBehaviorExecution = Class(name="TracedOpaqueBehaviorExecution")
umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution = Class(name="umlTrace::IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution")
umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution = Class(name="umlTrace::IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution")
umlTrace_Values_SemanticVisitor_runtimeModelElement_Value = Class(name="umlTrace::Values::SemanticVisitor::runtimeModelElement::Value")
uml_TracedElement = Class(name="uml::TracedElement")

# umlTrace_State class attributes and methods

# Values_ActionActivation_firing_Value class attributes and methods

# Values_SemanticVisitor_runtimeModelElement_Value class attributes and methods

# umlTrace_Trace class attributes and methods

# State class attributes and methods

# Traced_TracedObjects class attributes and methods

# umlTrace_Traced_TracedObjects class attributes and methods

# uml_TracedCombinedFragment class attributes and methods

# uml_TracedCreateLinkObjectAction class attributes and methods

# uml_TracedInitialNode class attributes and methods

# uml_TracedFlowFinalNode class attributes and methods

# uml_TracedExpansionRegion class attributes and methods

# uml_TracedSendObjectAction class attributes and methods

# uml_TracedPackageImport class attributes and methods

# uml_TracedClass class attributes and methods

# uml_TracedInteractionUse class attributes and methods

# uml_TracedGeneralizationSet class attributes and methods

# uml_TracedChangeEvent class attributes and methods

# uml_TracedDependency class attributes and methods

# uml_TracedPort class attributes and methods

# IntermediateActivities_TracedInitialNodeActivation class attributes and methods

# uml_TracedCollaborationUse class attributes and methods

# IntermediateActivities_TracedActivityExecution class attributes and methods

# uml_TracedCreateObjectAction class attributes and methods

# uml_TracedLifeline class attributes and methods

# IntermediateActivities_TracedForkNodeActivation class attributes and methods

# uml_TracedDurationConstraint class attributes and methods

# uml_TracedDestructionOccurrenceSpecification class attributes and methods

# uml_TracedConnector class attributes and methods

# uml_TracedExtend class attributes and methods

# IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution class attributes and methods

# uml_TracedExtension class attributes and methods

# uml_TracedStructuredActivityNode class attributes and methods

# uml_TracedExecutionEnvironment class attributes and methods

# uml_TracedIntervalConstraint class attributes and methods

# uml_TracedConsiderIgnoreFragment class attributes and methods

# uml_TracedContinuation class attributes and methods

# uml_TracedTimeConstraint class attributes and methods

# uml_TracedInputPin class attributes and methods

# uml_TracedValuePin class attributes and methods

# uml_TracedNode class attributes and methods

# uml_TracedExceptionHandler class attributes and methods

# uml_TracedSequenceNode class attributes and methods

# uml_TracedStartClassifierBehaviorAction class attributes and methods

# uml_TracedParameter class attributes and methods

# uml_TracedOpaqueExpression class attributes and methods

# uml_TracedLiteralString class attributes and methods

# BasicActions_TracedInputPinActivation class attributes and methods

# uml_TracedStateInvariant class attributes and methods

# IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution class attributes and methods

# uml_TracedInstanceSpecification class attributes and methods

# uml_TracedAcceptCallAction class attributes and methods

# uml_TracedClearVariableAction class attributes and methods

# uml_TracedConstraint class attributes and methods

# uml_TracedBroadcastSignalAction class attributes and methods

# uml_TracedInteraction class attributes and methods

# IntermediateActivities_TracedActivityNodeActivation class attributes and methods

# uml_TracedDestroyObjectAction class attributes and methods

# BasicActions_TracedCallBehaviorActionActivation class attributes and methods

# IntermediateActivities_TracedActivityParameterNodeActivation class attributes and methods

# uml_TracedActivityPartition class attributes and methods

# uml_TracedStateMachine class attributes and methods

# uml_TracedMessage class attributes and methods

# uml_TracedDeployment class attributes and methods

# uml_TracedStereotype class attributes and methods

# uml_TracedEnumerationLiteral class attributes and methods

# uml_TracedSubstitution class attributes and methods

# uml_TracedInformationFlow class attributes and methods

# uml_TracedAssociationClass class attributes and methods

# uml_TracedReclassifyObjectAction class attributes and methods

# uml_TracedUseCase class attributes and methods

# IntermediateActivities_TracedJoinNodeActivation class attributes and methods

# Kernel_TracedObject class attributes and methods

# Loci_TracedSemanticVisitor class attributes and methods

# uml_TracedTimeEvent class attributes and methods

# uml_TracedActivity class attributes and methods

# uml_TracedForkNode class attributes and methods

# Kernel_TracedReference class attributes and methods

# IntermediateActions_TracedAddStructuralFeatureValueActionActivation class attributes and methods

# uml_TracedGeneralization class attributes and methods

# uml_TracedInstanceValue class attributes and methods

# uml_TracedRemoveStructuralFeatureValueAction class attributes and methods

# uml_TracedInterval class attributes and methods

# Kernel_TracedIntegerValue class attributes and methods

# uml_TracedAnyReceiveEvent class attributes and methods

# uml_TracedReadStructuralFeatureAction class attributes and methods

# uml_TracedDataStoreNode class attributes and methods

# uml_TracedPartDecomposition class attributes and methods

# uml_TracedInterruptibleActivityRegion class attributes and methods

# uml_TracedProtocolTransition class attributes and methods

# uml_TracedInteractionOperand class attributes and methods

# uml_TracedDeploymentSpecification class attributes and methods

# uml_TracedUsage class attributes and methods

# uml_TracedActionInputPin class attributes and methods

# uml_TracedReadVariableAction class attributes and methods

# IntermediateActivities_TracedActivityFinalNodeActivation class attributes and methods

# uml_TracedDestroyLinkAction class attributes and methods

# uml_TracedLiteralInteger class attributes and methods

# uml_TracedProtocolStateMachine class attributes and methods

# uml_TracedReception class attributes and methods

# uml_TracedMessageOccurrenceSpecification class attributes and methods

# uml_TracedTemplateBinding class attributes and methods

# uml_TracedConnectionPointReference class attributes and methods

# uml_TracedRealization class attributes and methods

# uml_TracedReadLinkObjectEndQualifierAction class attributes and methods

# BasicActions_TracedOpaqueActionActivation class attributes and methods

# uml_TracedJoinNode class attributes and methods

# uml_TracedRedefinableTemplateSignature class attributes and methods

# uml_TracedModel class attributes and methods

# uml_TracedSignalEvent class attributes and methods

# Kernel_TracedBooleanValue class attributes and methods

# uml_TracedConditionalNode class attributes and methods

# uml_TracedExtensionPoint class attributes and methods

# uml_TracedSignal class attributes and methods

# uml_TracedExecutionOccurrenceSpecification class attributes and methods

# uml_TracedTimeInterval class attributes and methods

# uml_TracedInteractionConstraint class attributes and methods

# IntermediateActivities_TracedDecisionNodeActivation class attributes and methods

# uml_TracedCentralBufferNode class attributes and methods

# Kernel_TracedLiteralIntegerEvaluation class attributes and methods

# uml_TracedCreateLinkAction class attributes and methods

# uml_TracedPackage class attributes and methods

# uml_TracedCallEvent class attributes and methods

# uml_TracedLoopNode class attributes and methods

# uml_TracedComment class attributes and methods

# uml_TracedDataType class attributes and methods

# uml_TracedComponentRealization class attributes and methods

# uml_TracedInterface class attributes and methods

# uml_TracedOpaqueBehavior class attributes and methods

# uml_TracedProtocolConformance class attributes and methods

# uml_TracedObjectFlow class attributes and methods

# uml_TracedOperation class attributes and methods

# uml_TracedReadSelfAction class attributes and methods

# IntermediateActions_TracedReadStructuralFeatureActionActivation class attributes and methods

# uml_TracedDecisionNode class attributes and methods

# uml_TracedPackageMerge class attributes and methods

# uml_TracedAcceptEventAction class attributes and methods

# uml_TracedOccurrenceSpecification class attributes and methods

# uml_TracedParameterSet class attributes and methods

# uml_TracedTransition class attributes and methods

# uml_TracedDurationInterval class attributes and methods

# uml_TracedLinkEndData class attributes and methods

# uml_TracedConnectableElementTemplateParameter class attributes and methods

# uml_TracedOperationTemplateParameter class attributes and methods

# uml_TracedClause class attributes and methods

# uml_TracedReplyAction class attributes and methods

# uml_TracedTrigger class attributes and methods

# uml_TracedTemplateParameterSubstitution class attributes and methods

# uml_TracedDuration class attributes and methods

# uml_TracedReduceAction class attributes and methods

# uml_TracedFinalState class attributes and methods

# uml_TracedOpaqueAction class attributes and methods

# uml_TracedInformationItem class attributes and methods

# uml_TracedActionExecutionSpecification class attributes and methods

# uml_TracedOutputPin class attributes and methods

# uml_TracedImage class attributes and methods

# uml_TracedQualifierValue class attributes and methods

# uml_TracedAddStructuralFeatureValueAction class attributes and methods

# uml_TracedExpansionNode class attributes and methods

# uml_TracedActivityParameterNode class attributes and methods

# uml_TracedDevice class attributes and methods

# uml_TracedProperty class attributes and methods

# uml_TracedExtensionEnd class attributes and methods

# uml_TracedProfileApplication class attributes and methods

# uml_TracedCallOperationAction class attributes and methods

# uml_TracedArtifact class attributes and methods

# uml_TracedConnectorEnd class attributes and methods

# uml_TracedVariable class attributes and methods

# uml_TracedBehaviorExecutionSpecification class attributes and methods

# uml_TracedDurationObservation class attributes and methods

# uml_TracedLiteralUnlimitedNatural class attributes and methods

# uml_TracedTemplateSignature class attributes and methods

# BasicActions_TracedOutputPinActivation class attributes and methods

# uml_TracedReadExtentAction class attributes and methods

# uml_TracedCallBehaviorAction class attributes and methods

# uml_TracedReadLinkObjectEndAction class attributes and methods

# uml_TracedEnumeration class attributes and methods

# Kernel_TracedLiteralBooleanEvaluation class attributes and methods

# uml_TracedCommunicationPath class attributes and methods

# uml_TracedRaiseExceptionAction class attributes and methods

# uml_TracedReadLinkAction class attributes and methods

# uml_TracedLinkEndDestructionData class attributes and methods

# uml_TracedStringExpression class attributes and methods

# uml_TracedPrimitiveType class attributes and methods

# uml_TracedLiteralNull class attributes and methods

# uml_TracedState class attributes and methods

# uml_TracedRegion class attributes and methods

# uml_TracedInclude class attributes and methods

# uml_TracedLiteralBoolean class attributes and methods

# uml_TracedStartObjectBehaviorAction class attributes and methods

# IntermediateActions_TracedValueSpecificationActionActivation class attributes and methods

# uml_TracedAddVariableValueAction class attributes and methods

# uml_TracedClearStructuralFeatureAction class attributes and methods

# uml_TracedAssociation class attributes and methods

# uml_TracedExpression class attributes and methods

# uml_TracedLiteralReal class attributes and methods

# IntermediateActions_TracedCreateObjectActionActivation class attributes and methods

# uml_TracedCollaboration class attributes and methods

# uml_TracedTestIdentityAction class attributes and methods

# uml_TracedProfile class attributes and methods

# uml_TracedUnmarshallAction class attributes and methods

# uml_TracedSlot class attributes and methods

# uml_TracedInterfaceRealization class attributes and methods

# uml_TracedSendSignalAction class attributes and methods

# uml_TracedFunctionBehavior class attributes and methods

# uml_TracedValueSpecificationAction class attributes and methods

# uml_TracedRemoveVariableValueAction class attributes and methods

# uml_TracedActor class attributes and methods

# uml_TracedManifestation class attributes and methods

# uml_TracedReadIsClassifiedObjectAction class attributes and methods

# uml_TracedTemplateParameter class attributes and methods

# IntermediateActivities_TracedMergeNodeActivation class attributes and methods

# uml_TracedTimeExpression class attributes and methods

# uml_TracedAbstraction class attributes and methods

# uml_TracedClearAssociationAction class attributes and methods

# uml_TracedMergeNode class attributes and methods

# uml_TracedElementImport class attributes and methods

# IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution class attributes and methods

# uml_TracedPseudostate class attributes and methods

# uml_TracedLinkEndCreationData class attributes and methods

# uml_TracedGate class attributes and methods

# uml_TracedTimeObservation class attributes and methods

# uml_TracedControlFlow class attributes and methods

# uml_TracedGeneralOrdering class attributes and methods

# uml_TracedComponent class attributes and methods

# uml_TracedClassifierTemplateParameter class attributes and methods

# uml_TracedActivityFinalNode class attributes and methods

# umlTrace_uml_TracedRedefinableElement class attributes and methods

# umlTrace_uml_TracedNamespace class attributes and methods

# umlTrace_uml_TracedActivityGroup class attributes and methods

# uml_TracedNamedElement class attributes and methods

# umlTrace_uml_TracedCreateLinkObjectAction class attributes and methods

# TracedCreateLinkAction class attributes and methods

# umlTrace_uml_TracedCreateLinkAction class attributes and methods

# TracedWriteLinkAction class attributes and methods

# umlTrace_uml_TracedWriteLinkAction class attributes and methods

# TracedLinkAction class attributes and methods

# umlTrace_uml_TracedLinkAction class attributes and methods

# TracedAction class attributes and methods

# umlTrace_uml_TracedInitialNode class attributes and methods

# TracedControlNode class attributes and methods

# umlTrace_uml_TracedControlNode class attributes and methods

# umlTrace_uml_TracedFlowFinalNode class attributes and methods

# TracedFinalNode class attributes and methods

# umlTrace_uml_TracedFinalNode class attributes and methods

# umlTrace_uml_TracedExpansionRegion class attributes and methods

# umlTrace_uml_TracedCreateObjectAction class attributes and methods

# umlTrace_uml_TracedLifeline class attributes and methods

# umlTrace_uml_TracedDurationConstraint class attributes and methods

# TracedIntervalConstraint class attributes and methods

# umlTrace_uml_TracedIntervalConstraint class attributes and methods

# TracedConstraint class attributes and methods

# umlTrace_uml_TracedConstraint class attributes and methods

# TracedPackageableElement class attributes and methods

# umlTrace_uml_TracedCombinedFragment class attributes and methods

# TracedInteractionFragment class attributes and methods

# umlTrace_uml_TracedInteractionFragment class attributes and methods

# TracedNamedElement class attributes and methods

# umlTrace_uml_TracedNamedElement class attributes and methods

# TracedElement class attributes and methods

# umlTrace_uml_TracedElement class attributes and methods

# TracedEModelElement class attributes and methods

# umlTrace_uml_TracedConditionalNode class attributes and methods

# TracedStructuredActivityNode class attributes and methods

# umlTrace_uml_TracedStructuredActivityNode class attributes and methods

# uml_TracedAction class attributes and methods

# uml_TracedNamespace class attributes and methods

# uml_TracedActivityGroup class attributes and methods

# umlTrace_uml_TracedAction class attributes and methods

# TracedExecutableNode class attributes and methods

# umlTrace_uml_TracedExecutableNode class attributes and methods

# TracedActivityNode class attributes and methods

# umlTrace_uml_TracedActivityNode class attributes and methods

# uml_TracedRedefinableElement class attributes and methods

# ActivityContent class attributes and methods

# umlTrace_uml_TracedInvocationAction class attributes and methods

# umlTrace_uml_TracedOpaqueAction class attributes and methods

# umlTrace_uml_TracedProtocolConformance class attributes and methods

# TracedDirectedRelationship class attributes and methods

# umlTrace_uml_TracedDirectedRelationship class attributes and methods

# TracedRelationship class attributes and methods

# umlTrace_uml_TracedRelationship class attributes and methods

# umlTrace_uml_TracedCallBehaviorAction class attributes and methods

# TracedCallAction class attributes and methods

# umlTrace_uml_TracedCallAction class attributes and methods

# umlTrace_uml_TracedPackageImport class attributes and methods

# umlTrace_uml_TracedClass class attributes and methods

# uml_TracedEncapsulatedClassifier class attributes and methods

# uml_TracedBehavioredClassifier class attributes and methods

# umlTrace_uml_TracedEncapsulatedClassifier class attributes and methods

# TracedStructuredClassifier class attributes and methods

# umlTrace_uml_TracedStructuredClassifier class attributes and methods

# TracedClassifier class attributes and methods

# umlTrace_uml_TracedClassifier class attributes and methods

# uml_TracedType class attributes and methods

# umlTrace_uml_TracedType class attributes and methods

# umlTrace_uml_TracedBehavioredClassifier class attributes and methods

# umlTrace_uml_TracedActivityFinalNode class attributes and methods

# umlTrace_uml_TracedObservation class attributes and methods

# umlTrace_uml_TracedInteractionUse class attributes and methods

# umlTrace_uml_TracedLoopNode class attributes and methods

# umlTrace_uml_TracedSignal class attributes and methods

# umlTrace_uml_TracedPackageableElement class attributes and methods

# uml_TracedParameterableElement class attributes and methods

# umlTrace_uml_TracedParameterableElement class attributes and methods

# umlTrace_uml_TracedPseudostate class attributes and methods

# TracedVertex class attributes and methods

# umlTrace_uml_TracedVertex class attributes and methods

# umlTrace_uml_TracedDestructionOccurrenceSpecification class attributes and methods

# TracedMessageOccurrenceSpecification class attributes and methods

# umlTrace_uml_TracedMessageOccurrenceSpecification class attributes and methods

# uml_TracedMessageEnd class attributes and methods

# umlTrace_uml_TracedOccurrenceSpecification class attributes and methods

# umlTrace_uml_TracedMessageEnd class attributes and methods

# umlTrace_uml_TracedPackage class attributes and methods

# uml_TracedPackageableElement class attributes and methods

# uml_TracedTemplateableElement class attributes and methods

# umlTrace_uml_TracedTemplateableElement class attributes and methods

# umlTrace_uml_TracedConnector class attributes and methods

# TracedFeature class attributes and methods

# umlTrace_uml_TracedFeature class attributes and methods

# TracedRedefinableElement class attributes and methods

# umlTrace_uml_TracedSendObjectAction class attributes and methods

# TracedInvocationAction class attributes and methods

# umlTrace_uml_TracedInputPin class attributes and methods

# TracedPin class attributes and methods

# umlTrace_uml_TracedPin class attributes and methods

# uml_TracedObjectNode class attributes and methods

# umlTrace_uml_TracedObjectNode class attributes and methods

# uml_TracedActivityNode class attributes and methods

# umlTrace_uml_TracedDeploymentSpecification class attributes and methods

# TracedArtifact class attributes and methods

# umlTrace_uml_TracedArtifact class attributes and methods

# uml_TracedClassifier class attributes and methods

# uml_TracedDeployedArtifact class attributes and methods

# umlTrace_uml_TracedDeployedArtifact class attributes and methods

# umlTrace_uml_TracedTransition class attributes and methods

# umlTrace_uml_TracedNode class attributes and methods

# umlTrace_uml_TracedExceptionHandler class attributes and methods

# umlTrace_uml_TracedSequenceNode class attributes and methods

# umlTrace_uml_TracedUseCase class attributes and methods

# TracedBehavioredClassifier class attributes and methods

# umlTrace_uml_TracedStartClassifierBehaviorAction class attributes and methods

# umlTrace_uml_TracedExtend class attributes and methods

# umlTrace_uml_TracedRemoveStructuralFeatureValueAction class attributes and methods

# TracedWriteStructuralFeatureAction class attributes and methods

# umlTrace_uml_TracedWriteStructuralFeatureAction class attributes and methods

# TracedStructuralFeatureAction class attributes and methods

# umlTrace_uml_TracedStructuralFeatureAction class attributes and methods

# umlTrace_uml_TracedReadLinkAction class attributes and methods

# umlTrace_uml_TracedGeneralizationSet class attributes and methods

# umlTrace_uml_TracedChangeEvent class attributes and methods

# TracedEvent class attributes and methods

# umlTrace_uml_TracedEvent class attributes and methods

# umlTrace_uml_TracedDependency class attributes and methods

# uml_TracedDirectedRelationship class attributes and methods

# umlTrace_uml_TracedPort class attributes and methods

# TracedProperty class attributes and methods

# umlTrace_uml_TracedProperty class attributes and methods

# uml_TracedStructuralFeature class attributes and methods

# uml_TracedConnectableElement class attributes and methods

# uml_TracedDeploymentTarget class attributes and methods

# umlTrace_uml_TracedStructuralFeature class attributes and methods

# uml_TracedFeature class attributes and methods

# uml_TracedTypedElement class attributes and methods

# uml_TracedMultiplicityElement class attributes and methods

# umlTrace_uml_TracedTypedElement class attributes and methods

# umlTrace_uml_TracedMultiplicityElement class attributes and methods

# umlTrace_uml_TracedConnectableElement class attributes and methods

# umlTrace_uml_TracedDeploymentTarget class attributes and methods

# umlTrace_uml_TracedCollaborationUse class attributes and methods

# umlTrace_uml_TracedValuePin class attributes and methods

# TracedInputPin class attributes and methods

# umlTrace_uml_TracedBehavior class attributes and methods

# TracedClass class attributes and methods

# umlTrace_uml_TracedSlot class attributes and methods

# umlTrace_uml_TracedLiteralNull class attributes and methods

# umlTrace_uml_TracedParameter class attributes and methods

# umlTrace_uml_TracedOpaqueExpression class attributes and methods

# umlTrace_uml_TracedTrigger class attributes and methods

# umlTrace_uml_TracedStateInvariant class attributes and methods

# umlTrace_uml_TracedAssociationClass class attributes and methods

# umlTrace_uml_TracedInstanceSpecification class attributes and methods

# umlTrace_uml_TracedTemplateSignature class attributes and methods

# umlTrace_uml_TracedLinkEndDestructionData class attributes and methods

# TracedLinkEndData class attributes and methods

# umlTrace_uml_TracedLinkEndData class attributes and methods

# umlTrace_uml_TracedAcceptCallAction class attributes and methods

# TracedAcceptEventAction class attributes and methods

# umlTrace_uml_TracedAcceptEventAction class attributes and methods

# umlTrace_uml_TracedReduceAction class attributes and methods

# umlTrace_uml_TracedRaiseExceptionAction class attributes and methods

# umlTrace_uml_TracedStereotype class attributes and methods

# umlTrace_uml_TracedClearAssociationAction class attributes and methods

# umlTrace_uml_TracedEnumerationLiteral class attributes and methods

# TracedInstanceSpecification class attributes and methods

# umlTrace_uml_TracedSubstitution class attributes and methods

# TracedRealization class attributes and methods

# umlTrace_uml_TracedExtension class attributes and methods

# TracedAssociation class attributes and methods

# umlTrace_uml_TracedAssociation class attributes and methods

# uml_TracedRelationship class attributes and methods

# umlTrace_uml_TracedExecutionEnvironment class attributes and methods

# TracedNode class attributes and methods

# umlTrace_uml_TracedConsiderIgnoreFragment class attributes and methods

# TracedCombinedFragment class attributes and methods

# umlTrace_uml_TracedContinuation class attributes and methods

# umlTrace_uml_TracedCallOperationAction class attributes and methods

# umlTrace_uml_TracedTimeConstraint class attributes and methods

# umlTrace_uml_TracedClearVariableAction class attributes and methods

# TracedVariableAction class attributes and methods

# umlTrace_uml_TracedVariableAction class attributes and methods

# umlTrace_uml_TracedReadSelfAction class attributes and methods

# umlTrace_uml_TracedLiteralString class attributes and methods

# TracedLiteralSpecification class attributes and methods

# umlTrace_uml_TracedLiteralSpecification class attributes and methods

# TracedValueSpecification class attributes and methods

# umlTrace_uml_TracedValueSpecification class attributes and methods

# umlTrace_uml_TracedBroadcastSignalAction class attributes and methods

# umlTrace_uml_TracedInteraction class attributes and methods

# uml_TracedBehavior class attributes and methods

# uml_TracedInteractionFragment class attributes and methods

# umlTrace_uml_TracedActivityEdge class attributes and methods

# umlTrace_uml_TracedTestIdentityAction class attributes and methods

# umlTrace_uml_TracedInstanceValue class attributes and methods

# umlTrace_uml_TracedLiteralUnlimitedNatural class attributes and methods

# umlTrace_uml_TracedReclassifyObjectAction class attributes and methods

# umlTrace_uml_TracedTimeEvent class attributes and methods

# umlTrace_uml_TracedPartDecomposition class attributes and methods

# TracedInteractionUse class attributes and methods

# umlTrace_uml_TracedInterruptibleActivityRegion class attributes and methods

# umlTrace_uml_TracedAddVariableValueAction class attributes and methods

# TracedWriteVariableAction class attributes and methods

# umlTrace_uml_TracedWriteVariableAction class attributes and methods

# umlTrace_uml_TracedProtocolTransition class attributes and methods

# TracedTransition class attributes and methods

# umlTrace_uml_TracedImage class attributes and methods

# umlTrace_uml_TracedLiteralReal class attributes and methods

# umlTrace_uml_TracedInteractionOperand class attributes and methods

# umlTrace_uml_TracedGeneralization class attributes and methods

# umlTrace_uml_TracedInformationItem class attributes and methods

# umlTrace_uml_TracedModel class attributes and methods

# TracedPackage class attributes and methods

# umlTrace_uml_TracedClassifierTemplateParameter class attributes and methods

# TracedTemplateParameter class attributes and methods

# umlTrace_uml_TracedTemplateParameter class attributes and methods

# umlTrace_uml_TracedOperation class attributes and methods

# umlTrace_uml_TracedRealization class attributes and methods

# TracedAbstraction class attributes and methods

# umlTrace_uml_TracedAbstraction class attributes and methods

# TracedDependency class attributes and methods

# umlTrace_uml_TracedExecutionSpecification class attributes and methods

# umlTrace_uml_TracedReplyAction class attributes and methods

# umlTrace_uml_TracedActor class attributes and methods

# umlTrace_uml_TracedInformationFlow class attributes and methods

# umlTrace_uml_TracedDestroyObjectAction class attributes and methods

# umlTrace_uml_TracedActivityPartition class attributes and methods

# TracedActivityGroup class attributes and methods

# umlTrace_uml_TracedStateMachine class attributes and methods

# TracedBehavior class attributes and methods

# umlTrace_uml_TracedMessage class attributes and methods

# umlTrace_uml_TracedReadLinkObjectEndQualifierAction class attributes and methods

# umlTrace_uml_TracedDeployment class attributes and methods

# umlTrace_uml_TracedActivity class attributes and methods

# umlTrace_uml_TracedForkNode class attributes and methods

# umlTrace_uml_TracedProtocolStateMachine class attributes and methods

# TracedStateMachine class attributes and methods

# umlTrace_uml_TracedInterval class attributes and methods

# umlTrace_uml_TracedClearStructuralFeatureAction class attributes and methods

# umlTrace_uml_TracedObjectFlow class attributes and methods

# TracedActivityEdge class attributes and methods

# umlTrace_uml_TracedLiteralInteger class attributes and methods

# umlTrace_uml_TracedSignalEvent class attributes and methods

# umlTrace_uml_TracedReadLinkObjectEndAction class attributes and methods

# umlTrace_uml_TracedTimeInterval class attributes and methods

# TracedInterval class attributes and methods

# umlTrace_uml_TracedOperationTemplateParameter class attributes and methods

# umlTrace_uml_TracedDurationObservation class attributes and methods

# TracedObservation class attributes and methods

# umlTrace_uml_TracedConnectionPointReference class attributes and methods

# umlTrace_uml_TracedTimeExpression class attributes and methods

# umlTrace_uml_TracedQualifierValue class attributes and methods

# umlTrace_uml_TracedDurationInterval class attributes and methods

# umlTrace_uml_TracedFunctionBehavior class attributes and methods

# TracedOpaqueBehavior class attributes and methods

# umlTrace_uml_TracedOpaqueBehavior class attributes and methods

# umlTrace_uml_TracedInterfaceRealization class attributes and methods

# umlTrace_uml_TracedDevice class attributes and methods

# umlTrace_uml_TracedTemplateParameterSubstitution class attributes and methods

# umlTrace_uml_TracedJoinNode class attributes and methods

# umlTrace_uml_TracedRedefinableTemplateSignature class attributes and methods

# umlTrace_uml_TracedReadIsClassifiedObjectAction class attributes and methods

# umlTrace_uml_TracedTimeObservation class attributes and methods

# umlTrace_uml_TracedDecisionNode class attributes and methods

# umlTrace_uml_TracedElementImport class attributes and methods

# uml_TracedBehavioralFeature class attributes and methods

# umlTrace_uml_TracedBehavioralFeature class attributes and methods

# umlTrace_uml_TracedAnyReceiveEvent class attributes and methods

# TracedMessageEvent class attributes and methods

# umlTrace_uml_TracedMessageEvent class attributes and methods

# umlTrace_uml_TracedPrimitiveType class attributes and methods

# TracedDataType class attributes and methods

# umlTrace_uml_TracedDataType class attributes and methods

# umlTrace_uml_TracedReadStructuralFeatureAction class attributes and methods

# umlTrace_uml_TracedParameterSet class attributes and methods

# umlTrace_uml_TracedDataStoreNode class attributes and methods

# TracedCentralBufferNode class attributes and methods

# umlTrace_uml_TracedCentralBufferNode class attributes and methods

# TracedObjectNode class attributes and methods

# umlTrace_uml_TracedSendSignalAction class attributes and methods

# umlTrace_uml_TracedReception class attributes and methods

# TracedBehavioralFeature class attributes and methods

# umlTrace_uml_TracedTemplateBinding class attributes and methods

# umlTrace_uml_TracedUsage class attributes and methods

# umlTrace_uml_TracedActionInputPin class attributes and methods

# umlTrace_uml_TracedReadVariableAction class attributes and methods

# umlTrace_uml_TracedDestroyLinkAction class attributes and methods

# umlTrace_uml_TracedOutputPin class attributes and methods

# umlTrace_uml_TracedDuration class attributes and methods

# umlTrace_uml_TracedUnmarshallAction class attributes and methods

# umlTrace_uml_TracedProfile class attributes and methods

# umlTrace_uml_TracedExtensionEnd class attributes and methods

# umlTrace_uml_TracedExpansionNode class attributes and methods

# umlTrace_uml_TracedActivityParameterNode class attributes and methods

# umlTrace_uml_TracedProfileApplication class attributes and methods

# umlTrace_uml_TracedConnectorEnd class attributes and methods

# TracedMultiplicityElement class attributes and methods

# umlTrace_uml_TracedEnumeration class attributes and methods

# umlTrace_uml_TracedCollaboration class attributes and methods

# uml_TracedStructuredClassifier class attributes and methods

# umlTrace_uml_TracedVariable class attributes and methods

# umlTrace_uml_TracedValueSpecificationAction class attributes and methods

# umlTrace_uml_TracedReadExtentAction class attributes and methods

# umlTrace_uml_TracedStringExpression class attributes and methods

# umlTrace_uml_TracedExpression class attributes and methods

# umlTrace_uml_TracedGeneralOrdering class attributes and methods

# umlTrace_uml_TracedLiteralBoolean class attributes and methods

# umlTrace_uml_TracedStartObjectBehaviorAction class attributes and methods

# umlTrace_uml_TracedRegion class attributes and methods

# umlTrace_uml_TracedExtensionPoint class attributes and methods

# umlTrace_uml_TracedExecutionOccurrenceSpecification class attributes and methods

# TracedOccurrenceSpecification class attributes and methods

# umlTrace_uml_TracedInteractionConstraint class attributes and methods

# umlTrace_uml_TracedAddStructuralFeatureValueAction class attributes and methods

# umlTrace_uml_TracedInterface class attributes and methods

# umlTrace_uml_TracedComponent class attributes and methods

# umlTrace_uml_TracedCallEvent class attributes and methods

# umlTrace_uml_TracedComment class attributes and methods

# umlTrace_uml_TracedBehaviorExecutionSpecification class attributes and methods

# TracedExecutionSpecification class attributes and methods

# umlTrace_uml_TracedComponentRealization class attributes and methods

# umlTrace_uml_TracedCommunicationPath class attributes and methods

# umlTrace_uml_TracedPackageMerge class attributes and methods

# umlTrace_uml_TracedClause class attributes and methods

# umlTrace_uml_TracedFinalState class attributes and methods

# TracedState class attributes and methods

# umlTrace_uml_TracedState class attributes and methods

# uml_TracedVertex class attributes and methods

# umlTrace_uml_TracedConnectableElementTemplateParameter class attributes and methods

# umlTrace_uml_TracedActionExecutionSpecification class attributes and methods

# umlTrace_IntermediateActivities_TracedObjectNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedInitialNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityExecution class attributes and methods

# TracedExecution class attributes and methods

# umlTrace_IntermediateActivities_TracedMergeNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation class attributes and methods

# TracedObjectNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedJoinNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedDecisionNodeActivation class attributes and methods

# umlTrace_Loci_TracedSemanticVisitor class attributes and methods

# umlTrace_BasicActions_TracedPinActivation class attributes and methods

# umlTrace_BasicActions_TracedActionActivation class attributes and methods

# umlTrace_uml_TracedInclude class attributes and methods

# umlTrace_uml_TracedControlFlow class attributes and methods

# umlTrace_uml_TracedGate class attributes and methods

# TracedMessageEnd class attributes and methods

# umlTrace_uml_TracedRemoveVariableValueAction class attributes and methods

# umlTrace_uml_TracedManifestation class attributes and methods

# umlTrace_uml_TracedLinkEndCreationData class attributes and methods

# umlTrace_uml_TracedMergeNode class attributes and methods

# umlTrace_ecore_TracedEModelElement class attributes and methods

# umlTrace_IntermediateActivities_TracedForkNodeActivation class attributes and methods

# TracedControlNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedControlNodeActivation class attributes and methods

# TracedActivityNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityNodeActivation class attributes and methods

# TracedSemanticVisitor class attributes and methods

# umlTrace_IntermediateActions_TracedCreateObjectActionActivation class attributes and methods

# umlTrace_BasicBehaviors_TracedExecution class attributes and methods

# TracedObject class attributes and methods

# umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution class attributes and methods

# umlTrace_Kernel_TracedObject class attributes and methods

# TracedExtensionalValue class attributes and methods

# umlTrace_Kernel_TracedExtensionalValue class attributes and methods

# TracedCompoundValue class attributes and methods

# umlTrace_Kernel_TracedCompoundValue class attributes and methods

# TracedStructuredValue class attributes and methods

# umlTrace_Kernel_TracedStructuredValue class attributes and methods

# TracedValue class attributes and methods

# umlTrace_Kernel_TracedValue class attributes and methods

# umlTrace_Kernel_TracedReference class attributes and methods

# umlTrace_Kernel_TracedLiteralEvaluation class attributes and methods

# TracedEvaluation class attributes and methods

# umlTrace_Kernel_TracedEvaluation class attributes and methods

# umlTrace_Kernel_TracedIntegerValue class attributes and methods

# TracedPrimitiveValue class attributes and methods

# umlTrace_BasicActions_TracedInvocationActionActivation class attributes and methods

# TracedActionActivation class attributes and methods

# umlTrace_BasicActions_TracedCallActionActivation class attributes and methods

# TracedInvocationActionActivation class attributes and methods

# umlTrace_BasicActions_TracedOpaqueActionActivation class attributes and methods

# umlTrace_BasicActions_TracedInputPinActivation class attributes and methods

# TracedPinActivation class attributes and methods

# umlTrace_BasicActions_TracedCallBehaviorActionActivation class attributes and methods

# TracedCallActionActivation class attributes and methods

# umlTrace_BasicActions_TracedOutputPinActivation class attributes and methods

# umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation class attributes and methods

# umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation class attributes and methods

# TracedStructuralFeatureActionActivation class attributes and methods

# umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation class attributes and methods

# TracedWriteStructuralFeatureActionActivation class attributes and methods

# umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation class attributes and methods

# umlTrace_IntermediateActions_TracedValueSpecificationActionActivation class attributes and methods

# umlTrace_Values_ActionActivation_firing_Value class attributes and methods
umlTrace_Values_ActionActivation_firing_Value_firing: Property = Property(name="firing", type=StringType)
umlTrace_Values_ActionActivation_firing_Value.attributes={umlTrace_Values_ActionActivation_firing_Value_firing}

# BasicActions_TracedActionActivation class attributes and methods

# uml_ActivityContent class attributes and methods

# umlTrace_Kernel_TracedPrimitiveValue class attributes and methods

# umlTrace_Kernel_TracedLiteralBooleanEvaluation class attributes and methods

# TracedLiteralEvaluation class attributes and methods

# umlTrace_Kernel_TracedBooleanValue class attributes and methods

# umlTrace_Kernel_TracedLiteralIntegerEvaluation class attributes and methods

# umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution class attributes and methods

# TracedOpaqueBehaviorExecution class attributes and methods

# umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution class attributes and methods

# umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution class attributes and methods

# umlTrace_Values_SemanticVisitor_runtimeModelElement_Value class attributes and methods

# uml_TracedElement class attributes and methods

# Relationships
actionActivation_firing_Values0: BinaryAssociation = BinaryAssociation(
    name="actionActivation_firing_Values0",
    ends={
        Property(name="", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=Values_ActionActivation_firing_Value, multiplicity=Multiplicity(0, 9999))
    }
)
semanticVisitor_runtimeModelElement_Values1: BinaryAssociation = BinaryAssociation(
    name="semanticVisitor_runtimeModelElement_Values1",
    ends={
        Property(name="3", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="02", type=Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(0, 9999))
    }
)
statesTrace4: BinaryAssociation = BinaryAssociation(
    name="statesTrace4",
    ends={
        Property(name="State", type=umlTrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Trace", type=State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tracedObjects5: BinaryAssociation = BinaryAssociation(
    name="tracedObjects5",
    ends={
        Property(name="Traced_TracedObjects", type=umlTrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Trace6", type=Traced_TracedObjects, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
uml_tracedCombinedFragments7: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCombinedFragments7",
    ends={
        Property(name="uml_TracedCombinedFragment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects", type=uml_TracedCombinedFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCreateLinkObjectActions8: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCreateLinkObjectActions8",
    ends={
        Property(name="uml_TracedCreateLinkObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects9", type=uml_TracedCreateLinkObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInitialNodes10: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInitialNodes10",
    ends={
        Property(name="uml_TracedInitialNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects11", type=uml_TracedInitialNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedFlowFinalNodes12: BinaryAssociation = BinaryAssociation(
    name="uml_tracedFlowFinalNodes12",
    ends={
        Property(name="uml_TracedFlowFinalNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects13", type=uml_TracedFlowFinalNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectors26: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectors26",
    ends={
        Property(name="uml_TracedConnector", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects27", type=uml_TracedConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSendObjectActions28: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSendObjectActions28",
    ends={
        Property(name="uml_TracedSendObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects29", type=uml_TracedSendObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPackageImports30: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPackageImports30",
    ends={
        Property(name="uml_TracedPackageImport", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects31", type=uml_TracedPackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClasss32: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClasss32",
    ends={
        Property(name="uml_TracedClass", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects33", type=uml_TracedClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractionUses34: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractionUses34",
    ends={
        Property(name="uml_TracedInteractionUse", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects35", type=uml_TracedInteractionUse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGeneralizationSets36: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGeneralizationSets36",
    ends={
        Property(name="uml_TracedGeneralizationSet", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects37", type=uml_TracedGeneralizationSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedChangeEvents38: BinaryAssociation = BinaryAssociation(
    name="uml_tracedChangeEvents38",
    ends={
        Property(name="uml_TracedChangeEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects39", type=uml_TracedChangeEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDependencys40: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDependencys40",
    ends={
        Property(name="uml_TracedDependency", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects41", type=uml_TracedDependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPorts42: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPorts42",
    ends={
        Property(name="uml_TracedPort", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects43", type=uml_TracedPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedInitialNodeActivations44: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedInitialNodeActivations44",
    ends={
        Property(name="IntermediateActivities_TracedInitialNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects45", type=IntermediateActivities_TracedInitialNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCollaborationUses46: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCollaborationUses46",
    ends={
        Property(name="uml_TracedCollaborationUse", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects47", type=uml_TracedCollaborationUse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityExecutions48: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityExecutions48",
    ends={
        Property(name="IntermediateActivities_TracedActivityExecution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects49", type=IntermediateActivities_TracedActivityExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExpansionRegions14: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExpansionRegions14",
    ends={
        Property(name="uml_TracedExpansionRegion", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects15", type=uml_TracedExpansionRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCreateObjectActions16: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCreateObjectActions16",
    ends={
        Property(name="uml_TracedCreateObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects17", type=uml_TracedCreateObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLifelines18: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLifelines18",
    ends={
        Property(name="uml_TracedLifeline", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects19", type=uml_TracedLifeline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedForkNodeActivations20: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedForkNodeActivations20",
    ends={
        Property(name="IntermediateActivities_TracedForkNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects21", type=IntermediateActivities_TracedForkNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurationConstraints22: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurationConstraints22",
    ends={
        Property(name="uml_TracedDurationConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects23", type=uml_TracedDurationConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDestructionOccurrenceSpecifications24: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDestructionOccurrenceSpecifications24",
    ends={
        Property(name="uml_TracedDestructionOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects25", type=uml_TracedDestructionOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtends60: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtends60",
    ends={
        Property(name="uml_TracedExtend", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects61", type=uml_TracedExtend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integerFunctions_tracedIntegerPlusFunctionBehaviorExecutions62: BinaryAssociation = BinaryAssociation(
    name="integerFunctions_tracedIntegerPlusFunctionBehaviorExecutions62",
    ends={
        Property(name="IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects63", type=IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtensions64: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtensions64",
    ends={
        Property(name="uml_TracedExtension", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects65", type=uml_TracedExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStructuredActivityNodes66: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStructuredActivityNodes66",
    ends={
        Property(name="uml_TracedStructuredActivityNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects67", type=uml_TracedStructuredActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExecutionEnvironments68: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExecutionEnvironments68",
    ends={
        Property(name="uml_TracedExecutionEnvironment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects69", type=uml_TracedExecutionEnvironment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedIntervalConstraints70: BinaryAssociation = BinaryAssociation(
    name="uml_tracedIntervalConstraints70",
    ends={
        Property(name="uml_TracedIntervalConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects71", type=uml_TracedIntervalConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConsiderIgnoreFragments72: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConsiderIgnoreFragments72",
    ends={
        Property(name="uml_TracedConsiderIgnoreFragment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects73", type=uml_TracedConsiderIgnoreFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedContinuations74: BinaryAssociation = BinaryAssociation(
    name="uml_tracedContinuations74",
    ends={
        Property(name="uml_TracedContinuation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects75", type=uml_TracedContinuation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeConstraints76: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeConstraints76",
    ends={
        Property(name="uml_TracedTimeConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects77", type=uml_TracedTimeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInputPins78: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInputPins78",
    ends={
        Property(name="uml_TracedInputPin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects79", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedValuePins50: BinaryAssociation = BinaryAssociation(
    name="uml_tracedValuePins50",
    ends={
        Property(name="uml_TracedValuePin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects51", type=uml_TracedValuePin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedNodes52: BinaryAssociation = BinaryAssociation(
    name="uml_tracedNodes52",
    ends={
        Property(name="uml_TracedNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects53", type=uml_TracedNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExceptionHandlers54: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExceptionHandlers54",
    ends={
        Property(name="uml_TracedExceptionHandler", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects55", type=uml_TracedExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSequenceNodes56: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSequenceNodes56",
    ends={
        Property(name="uml_TracedSequenceNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects57", type=uml_TracedSequenceNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStartClassifierBehaviorActions58: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStartClassifierBehaviorActions58",
    ends={
        Property(name="uml_TracedStartClassifierBehaviorAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects59", type=uml_TracedStartClassifierBehaviorAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityNodeActivations88: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityNodeActivations88",
    ends={
        Property(name="umlTrace_Traced_TracedObjects89", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="IntermediateActivities_TracedActivityNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1))
    }
)
uml_tracedParameters90: BinaryAssociation = BinaryAssociation(
    name="uml_tracedParameters90",
    ends={
        Property(name="uml_TracedParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects91", type=uml_TracedParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOpaqueExpressions92: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOpaqueExpressions92",
    ends={
        Property(name="uml_TracedOpaqueExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects93", type=uml_TracedOpaqueExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralStrings94: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralStrings94",
    ends={
        Property(name="uml_TracedLiteralString", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects95", type=uml_TracedLiteralString, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedInputPinActivations96: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedInputPinActivations96",
    ends={
        Property(name="BasicActions_TracedInputPinActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects97", type=BasicActions_TracedInputPinActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStateInvariants98: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStateInvariants98",
    ends={
        Property(name="uml_TracedStateInvariant", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects99", type=uml_TracedStateInvariant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integerFunctions_tracedIntegerLessFunctionBehaviorExecutions100: BinaryAssociation = BinaryAssociation(
    name="integerFunctions_tracedIntegerLessFunctionBehaviorExecutions100",
    ends={
        Property(name="IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects101", type=IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInstanceSpecifications102: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInstanceSpecifications102",
    ends={
        Property(name="uml_TracedInstanceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects103", type=uml_TracedInstanceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAcceptCallActions104: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAcceptCallActions104",
    ends={
        Property(name="uml_TracedAcceptCallAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects105", type=uml_TracedAcceptCallAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClearVariableActions80: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClearVariableActions80",
    ends={
        Property(name="uml_TracedClearVariableAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects81", type=uml_TracedClearVariableAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConstraints82: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConstraints82",
    ends={
        Property(name="uml_TracedConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects83", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedBroadcastSignalActions84: BinaryAssociation = BinaryAssociation(
    name="uml_tracedBroadcastSignalActions84",
    ends={
        Property(name="uml_TracedBroadcastSignalAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects85", type=uml_TracedBroadcastSignalAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractions86: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractions86",
    ends={
        Property(name="uml_TracedInteraction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects87", type=uml_TracedInteraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAssociationClasss114: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAssociationClasss114",
    ends={
        Property(name="uml_TracedAssociationClass", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects115", type=uml_TracedAssociationClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDestroyObjectActions116: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDestroyObjectActions116",
    ends={
        Property(name="uml_TracedDestroyObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects117", type=uml_TracedDestroyObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedCallBehaviorActionActivations118: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedCallBehaviorActionActivations118",
    ends={
        Property(name="BasicActions_TracedCallBehaviorActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects119", type=BasicActions_TracedCallBehaviorActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityParameterNodeActivations120: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityParameterNodeActivations120",
    ends={
        Property(name="IntermediateActivities_TracedActivityParameterNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects121", type=IntermediateActivities_TracedActivityParameterNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActivityPartitions122: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivityPartitions122",
    ends={
        Property(name="uml_TracedActivityPartition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects123", type=uml_TracedActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStateMachines124: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStateMachines124",
    ends={
        Property(name="uml_TracedStateMachine", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects125", type=uml_TracedStateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedMessages126: BinaryAssociation = BinaryAssociation(
    name="uml_tracedMessages126",
    ends={
        Property(name="uml_TracedMessage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects127", type=uml_TracedMessage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDeployments128: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDeployments128",
    ends={
        Property(name="uml_TracedDeployment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects129", type=uml_TracedDeployment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStereotypes106: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStereotypes106",
    ends={
        Property(name="uml_TracedStereotype", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects107", type=uml_TracedStereotype, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedEnumerationLiterals108: BinaryAssociation = BinaryAssociation(
    name="uml_tracedEnumerationLiterals108",
    ends={
        Property(name="uml_TracedEnumerationLiteral", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects109", type=uml_TracedEnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSubstitutions110: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSubstitutions110",
    ends={
        Property(name="uml_TracedSubstitution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects111", type=uml_TracedSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInformationFlows112: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInformationFlows112",
    ends={
        Property(name="uml_TracedInformationFlow", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects113", type=uml_TracedInformationFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReclassifyObjectActions140: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReclassifyObjectActions140",
    ends={
        Property(name="uml_TracedReclassifyObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects141", type=uml_TracedReclassifyObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedUseCases142: BinaryAssociation = BinaryAssociation(
    name="uml_tracedUseCases142",
    ends={
        Property(name="uml_TracedUseCase", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects143", type=uml_TracedUseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedJoinNodeActivations144: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedJoinNodeActivations144",
    ends={
        Property(name="IntermediateActivities_TracedJoinNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects145", type=IntermediateActivities_TracedJoinNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedObjects146: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedObjects146",
    ends={
        Property(name="Kernel_TracedObject", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects147", type=Kernel_TracedObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loci_tracedSemanticVisitors148: BinaryAssociation = BinaryAssociation(
    name="loci_tracedSemanticVisitors148",
    ends={
        Property(name="Loci_TracedSemanticVisitor", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects149", type=Loci_TracedSemanticVisitor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeEvents150: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeEvents150",
    ends={
        Property(name="uml_TracedTimeEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects151", type=uml_TracedTimeEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActivitys130: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivitys130",
    ends={
        Property(name="uml_TracedActivity", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects131", type=uml_TracedActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedForkNodes132: BinaryAssociation = BinaryAssociation(
    name="uml_tracedForkNodes132",
    ends={
        Property(name="uml_TracedForkNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects133", type=uml_TracedForkNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedReferences134: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedReferences134",
    ends={
        Property(name="Kernel_TracedReference", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects135", type=Kernel_TracedReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedAddStructuralFeatureValueActionActivations136: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedAddStructuralFeatureValueActionActivations136",
    ends={
        Property(name="IntermediateActions_TracedAddStructuralFeatureValueActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects137", type=IntermediateActions_TracedAddStructuralFeatureValueActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGeneralizations160: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGeneralizations160",
    ends={
        Property(name="uml_TracedGeneralization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects161", type=uml_TracedGeneralization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInstanceValues138: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInstanceValues138",
    ends={
        Property(name="uml_TracedInstanceValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects139", type=uml_TracedInstanceValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRemoveStructuralFeatureValueActions162: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRemoveStructuralFeatureValueActions162",
    ends={
        Property(name="uml_TracedRemoveStructuralFeatureValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects163", type=uml_TracedRemoveStructuralFeatureValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedIntervals164: BinaryAssociation = BinaryAssociation(
    name="uml_tracedIntervals164",
    ends={
        Property(name="uml_TracedInterval", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects165", type=uml_TracedInterval, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedIntegerValues166: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedIntegerValues166",
    ends={
        Property(name="Kernel_TracedIntegerValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects167", type=Kernel_TracedIntegerValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAnyReceiveEvents168: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAnyReceiveEvents168",
    ends={
        Property(name="uml_TracedAnyReceiveEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects169", type=uml_TracedAnyReceiveEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadStructuralFeatureActions170: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadStructuralFeatureActions170",
    ends={
        Property(name="uml_TracedReadStructuralFeatureAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects171", type=uml_TracedReadStructuralFeatureAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDataStoreNodes172: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDataStoreNodes172",
    ends={
        Property(name="uml_TracedDataStoreNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects173", type=uml_TracedDataStoreNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPartDecompositions152: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPartDecompositions152",
    ends={
        Property(name="uml_TracedPartDecomposition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects153", type=uml_TracedPartDecomposition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInterruptibleActivityRegions154: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInterruptibleActivityRegions154",
    ends={
        Property(name="uml_TracedInterruptibleActivityRegion", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects155", type=uml_TracedInterruptibleActivityRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProtocolTransitions156: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProtocolTransitions156",
    ends={
        Property(name="uml_TracedProtocolTransition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects157", type=uml_TracedProtocolTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractionOperands158: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractionOperands158",
    ends={
        Property(name="uml_TracedInteractionOperand", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects159", type=uml_TracedInteractionOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDeploymentSpecifications182: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDeploymentSpecifications182",
    ends={
        Property(name="uml_TracedDeploymentSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects183", type=uml_TracedDeploymentSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedUsages184: BinaryAssociation = BinaryAssociation(
    name="uml_tracedUsages184",
    ends={
        Property(name="uml_TracedUsage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects185", type=uml_TracedUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActionInputPins186: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActionInputPins186",
    ends={
        Property(name="uml_TracedActionInputPin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects187", type=uml_TracedActionInputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadVariableActions188: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadVariableActions188",
    ends={
        Property(name="uml_TracedReadVariableAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects189", type=uml_TracedReadVariableAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityFinalNodeActivations190: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityFinalNodeActivations190",
    ends={
        Property(name="IntermediateActivities_TracedActivityFinalNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects191", type=IntermediateActivities_TracedActivityFinalNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDestroyLinkActions192: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDestroyLinkActions192",
    ends={
        Property(name="uml_TracedDestroyLinkAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects193", type=uml_TracedDestroyLinkAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProtocolStateMachines174: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProtocolStateMachines174",
    ends={
        Property(name="uml_TracedProtocolStateMachine", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects175", type=uml_TracedProtocolStateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReceptions176: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReceptions176",
    ends={
        Property(name="uml_TracedReception", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects177", type=uml_TracedReception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedMessageOccurrenceSpecifications178: BinaryAssociation = BinaryAssociation(
    name="uml_tracedMessageOccurrenceSpecifications178",
    ends={
        Property(name="uml_TracedMessageOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects179", type=uml_TracedMessageOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateBindings180: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateBindings180",
    ends={
        Property(name="uml_TracedTemplateBinding", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects181", type=uml_TracedTemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectionPointReferences202: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectionPointReferences202",
    ends={
        Property(name="uml_TracedConnectionPointReference", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects203", type=uml_TracedConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRealizations204: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRealizations204",
    ends={
        Property(name="uml_TracedRealization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects205", type=uml_TracedRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadLinkObjectEndQualifierActions206: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadLinkObjectEndQualifierActions206",
    ends={
        Property(name="uml_TracedReadLinkObjectEndQualifierAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects207", type=uml_TracedReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedOpaqueActionActivations208: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedOpaqueActionActivations208",
    ends={
        Property(name="BasicActions_TracedOpaqueActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects209", type=BasicActions_TracedOpaqueActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedJoinNodes210: BinaryAssociation = BinaryAssociation(
    name="uml_tracedJoinNodes210",
    ends={
        Property(name="uml_TracedJoinNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects211", type=uml_TracedJoinNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRedefinableTemplateSignatures212: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRedefinableTemplateSignatures212",
    ends={
        Property(name="uml_TracedRedefinableTemplateSignature", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects213", type=uml_TracedRedefinableTemplateSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralIntegers194: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralIntegers194",
    ends={
        Property(name="uml_TracedLiteralInteger", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects195", type=uml_TracedLiteralInteger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSignalEvents196: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSignalEvents196",
    ends={
        Property(name="uml_TracedSignalEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects197", type=uml_TracedSignalEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedBooleanValues198: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedBooleanValues198",
    ends={
        Property(name="Kernel_TracedBooleanValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects199", type=Kernel_TracedBooleanValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConditionalNodes200: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConditionalNodes200",
    ends={
        Property(name="uml_TracedConditionalNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects201", type=uml_TracedConditionalNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtensionPoints222: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtensionPoints222",
    ends={
        Property(name="uml_TracedExtensionPoint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects223", type=uml_TracedExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSignals224: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSignals224",
    ends={
        Property(name="uml_TracedSignal", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects225", type=uml_TracedSignal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExecutionOccurrenceSpecifications226: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExecutionOccurrenceSpecifications226",
    ends={
        Property(name="uml_TracedExecutionOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects227", type=uml_TracedExecutionOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeIntervals228: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeIntervals228",
    ends={
        Property(name="uml_TracedTimeInterval", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects229", type=uml_TracedTimeInterval, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractionConstraints230: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractionConstraints230",
    ends={
        Property(name="uml_TracedInteractionConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects231", type=uml_TracedInteractionConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedDecisionNodeActivations232: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedDecisionNodeActivations232",
    ends={
        Property(name="IntermediateActivities_TracedDecisionNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects233", type=IntermediateActivities_TracedDecisionNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedModels214: BinaryAssociation = BinaryAssociation(
    name="uml_tracedModels214",
    ends={
        Property(name="uml_TracedModel", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects215", type=uml_TracedModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCentralBufferNodes216: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCentralBufferNodes216",
    ends={
        Property(name="uml_TracedCentralBufferNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects217", type=uml_TracedCentralBufferNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedLiteralIntegerEvaluations218: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedLiteralIntegerEvaluations218",
    ends={
        Property(name="Kernel_TracedLiteralIntegerEvaluation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects219", type=Kernel_TracedLiteralIntegerEvaluation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCreateLinkActions220: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCreateLinkActions220",
    ends={
        Property(name="uml_TracedCreateLinkAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects221", type=uml_TracedCreateLinkAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPackages240: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPackages240",
    ends={
        Property(name="uml_TracedPackage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects241", type=uml_TracedPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCallEvents242: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCallEvents242",
    ends={
        Property(name="uml_TracedCallEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects243", type=uml_TracedCallEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLoopNodes244: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLoopNodes244",
    ends={
        Property(name="uml_TracedLoopNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects245", type=uml_TracedLoopNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedComments246: BinaryAssociation = BinaryAssociation(
    name="uml_tracedComments246",
    ends={
        Property(name="uml_TracedComment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects247", type=uml_TracedComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDataTypes248: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDataTypes248",
    ends={
        Property(name="uml_TracedDataType", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects249", type=uml_TracedDataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedComponentRealizations250: BinaryAssociation = BinaryAssociation(
    name="uml_tracedComponentRealizations250",
    ends={
        Property(name="uml_TracedComponentRealization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects251", type=uml_TracedComponentRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInterfaces234: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInterfaces234",
    ends={
        Property(name="uml_TracedInterface", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects235", type=uml_TracedInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOpaqueBehaviors236: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOpaqueBehaviors236",
    ends={
        Property(name="uml_TracedOpaqueBehavior", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects237", type=uml_TracedOpaqueBehavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProtocolConformances238: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProtocolConformances238",
    ends={
        Property(name="uml_TracedProtocolConformance", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects239", type=uml_TracedProtocolConformance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedObjectFlows258: BinaryAssociation = BinaryAssociation(
    name="uml_tracedObjectFlows258",
    ends={
        Property(name="uml_TracedObjectFlow", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects259", type=uml_TracedObjectFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOperations260: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOperations260",
    ends={
        Property(name="uml_TracedOperation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects261", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadSelfActions262: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadSelfActions262",
    ends={
        Property(name="uml_TracedReadSelfAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects263", type=uml_TracedReadSelfAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedReadStructuralFeatureActionActivations264: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedReadStructuralFeatureActionActivations264",
    ends={
        Property(name="IntermediateActions_TracedReadStructuralFeatureActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects265", type=IntermediateActions_TracedReadStructuralFeatureActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDecisionNodes266: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDecisionNodes266",
    ends={
        Property(name="uml_TracedDecisionNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects267", type=uml_TracedDecisionNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAcceptEventActions252: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAcceptEventActions252",
    ends={
        Property(name="uml_TracedAcceptEventAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects253", type=uml_TracedAcceptEventAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOccurrenceSpecifications254: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOccurrenceSpecifications254",
    ends={
        Property(name="uml_TracedOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects255", type=uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedParameterSets256: BinaryAssociation = BinaryAssociation(
    name="uml_tracedParameterSets256",
    ends={
        Property(name="uml_TracedParameterSet", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects257", type=uml_TracedParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTransitions276: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTransitions276",
    ends={
        Property(name="uml_TracedTransition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects277", type=uml_TracedTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurationIntervals278: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurationIntervals278",
    ends={
        Property(name="uml_TracedDurationInterval", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects279", type=uml_TracedDurationInterval, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLinkEndDatas280: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLinkEndDatas280",
    ends={
        Property(name="uml_TracedLinkEndData", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects281", type=uml_TracedLinkEndData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectableElementTemplateParameters282: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectableElementTemplateParameters282",
    ends={
        Property(name="uml_TracedConnectableElementTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects283", type=uml_TracedConnectableElementTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOperationTemplateParameters284: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOperationTemplateParameters284",
    ends={
        Property(name="uml_TracedOperationTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects285", type=uml_TracedOperationTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPackageMerges268: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPackageMerges268",
    ends={
        Property(name="uml_TracedPackageMerge", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects269", type=uml_TracedPackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClauses270: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClauses270",
    ends={
        Property(name="uml_TracedClause", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects271", type=uml_TracedClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReplyActions272: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReplyActions272",
    ends={
        Property(name="uml_TracedReplyAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects273", type=uml_TracedReplyAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTriggers274: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTriggers274",
    ends={
        Property(name="uml_TracedTrigger", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects275", type=uml_TracedTrigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateParameterSubstitutions292: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateParameterSubstitutions292",
    ends={
        Property(name="uml_TracedTemplateParameterSubstitution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects293", type=uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurations294: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurations294",
    ends={
        Property(name="uml_TracedDuration", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects295", type=uml_TracedDuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReduceActions296: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReduceActions296",
    ends={
        Property(name="uml_TracedReduceAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects297", type=uml_TracedReduceAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedFinalStates298: BinaryAssociation = BinaryAssociation(
    name="uml_tracedFinalStates298",
    ends={
        Property(name="uml_TracedFinalState", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects299", type=uml_TracedFinalState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOpaqueActions300: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOpaqueActions300",
    ends={
        Property(name="uml_TracedOpaqueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects301", type=uml_TracedOpaqueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInformationItems286: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInformationItems286",
    ends={
        Property(name="uml_TracedInformationItem", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects287", type=uml_TracedInformationItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActionExecutionSpecifications288: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActionExecutionSpecifications288",
    ends={
        Property(name="uml_TracedActionExecutionSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects289", type=uml_TracedActionExecutionSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOutputPins290: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOutputPins290",
    ends={
        Property(name="uml_TracedOutputPin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects291", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedImages308: BinaryAssociation = BinaryAssociation(
    name="uml_tracedImages308",
    ends={
        Property(name="uml_TracedImage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects309", type=uml_TracedImage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedQualifierValues310: BinaryAssociation = BinaryAssociation(
    name="uml_tracedQualifierValues310",
    ends={
        Property(name="uml_TracedQualifierValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects311", type=uml_TracedQualifierValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAddStructuralFeatureValueActions312: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAddStructuralFeatureValueActions312",
    ends={
        Property(name="uml_TracedAddStructuralFeatureValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects313", type=uml_TracedAddStructuralFeatureValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExpansionNodes314: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExpansionNodes314",
    ends={
        Property(name="uml_TracedExpansionNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects315", type=uml_TracedExpansionNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDevices302: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDevices302",
    ends={
        Property(name="uml_TracedDevice", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects303", type=uml_TracedDevice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPropertys304: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPropertys304",
    ends={
        Property(name="uml_TracedProperty", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects305", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtensionEnds306: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtensionEnds306",
    ends={
        Property(name="uml_TracedExtensionEnd", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects307", type=uml_TracedExtensionEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProfileApplications322: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProfileApplications322",
    ends={
        Property(name="uml_TracedProfileApplication", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects323", type=uml_TracedProfileApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCallOperationActions324: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCallOperationActions324",
    ends={
        Property(name="uml_TracedCallOperationAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects325", type=uml_TracedCallOperationAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedArtifacts326: BinaryAssociation = BinaryAssociation(
    name="uml_tracedArtifacts326",
    ends={
        Property(name="uml_TracedArtifact", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects327", type=uml_TracedArtifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectorEnds328: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectorEnds328",
    ends={
        Property(name="uml_TracedConnectorEnd", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects329", type=uml_TracedConnectorEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedVariables330: BinaryAssociation = BinaryAssociation(
    name="uml_tracedVariables330",
    ends={
        Property(name="uml_TracedVariable", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects331", type=uml_TracedVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActivityParameterNodes316: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivityParameterNodes316",
    ends={
        Property(name="uml_TracedActivityParameterNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects317", type=uml_TracedActivityParameterNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedBehaviorExecutionSpecifications318: BinaryAssociation = BinaryAssociation(
    name="uml_tracedBehaviorExecutionSpecifications318",
    ends={
        Property(name="uml_TracedBehaviorExecutionSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects319", type=uml_TracedBehaviorExecutionSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurationObservations320: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurationObservations320",
    ends={
        Property(name="uml_TracedDurationObservation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects321", type=uml_TracedDurationObservation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralUnlimitedNaturals338: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralUnlimitedNaturals338",
    ends={
        Property(name="uml_TracedLiteralUnlimitedNatural", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects339", type=uml_TracedLiteralUnlimitedNatural, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateSignatures340: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateSignatures340",
    ends={
        Property(name="uml_TracedTemplateSignature", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects341", type=uml_TracedTemplateSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedOutputPinActivations342: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedOutputPinActivations342",
    ends={
        Property(name="BasicActions_TracedOutputPinActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects343", type=BasicActions_TracedOutputPinActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadExtentActions344: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadExtentActions344",
    ends={
        Property(name="uml_TracedReadExtentAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects345", type=uml_TracedReadExtentAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCallBehaviorActions332: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCallBehaviorActions332",
    ends={
        Property(name="uml_TracedCallBehaviorAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects333", type=uml_TracedCallBehaviorAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadLinkObjectEndActions334: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadLinkObjectEndActions334",
    ends={
        Property(name="uml_TracedReadLinkObjectEndAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects335", type=uml_TracedReadLinkObjectEndAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedEnumerations336: BinaryAssociation = BinaryAssociation(
    name="uml_tracedEnumerations336",
    ends={
        Property(name="uml_TracedEnumeration", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects337", type=uml_TracedEnumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedLiteralBooleanEvaluations352: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedLiteralBooleanEvaluations352",
    ends={
        Property(name="Kernel_TracedLiteralBooleanEvaluation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects353", type=Kernel_TracedLiteralBooleanEvaluation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCommunicationPaths354: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCommunicationPaths354",
    ends={
        Property(name="uml_TracedCommunicationPath", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects355", type=uml_TracedCommunicationPath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRaiseExceptionActions356: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRaiseExceptionActions356",
    ends={
        Property(name="uml_TracedRaiseExceptionAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects357", type=uml_TracedRaiseExceptionAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadLinkActions358: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadLinkActions358",
    ends={
        Property(name="uml_TracedReadLinkAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects359", type=uml_TracedReadLinkAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLinkEndDestructionDatas346: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLinkEndDestructionDatas346",
    ends={
        Property(name="uml_TracedLinkEndDestructionData", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects347", type=uml_TracedLinkEndDestructionData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStringExpressions348: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStringExpressions348",
    ends={
        Property(name="uml_TracedStringExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects349", type=uml_TracedStringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPrimitiveTypes350: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPrimitiveTypes350",
    ends={
        Property(name="uml_TracedPrimitiveType", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects351", type=uml_TracedPrimitiveType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralNulls366: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralNulls366",
    ends={
        Property(name="uml_TracedLiteralNull", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects367", type=uml_TracedLiteralNull, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStates368: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStates368",
    ends={
        Property(name="uml_TracedState", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects369", type=uml_TracedState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRegions370: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRegions370",
    ends={
        Property(name="uml_TracedRegion", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects371", type=uml_TracedRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedIncludes372: BinaryAssociation = BinaryAssociation(
    name="uml_tracedIncludes372",
    ends={
        Property(name="uml_TracedInclude", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects373", type=uml_TracedInclude, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralBooleans360: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralBooleans360",
    ends={
        Property(name="uml_TracedLiteralBoolean", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects361", type=uml_TracedLiteralBoolean, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStartObjectBehaviorActions362: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStartObjectBehaviorActions362",
    ends={
        Property(name="uml_TracedStartObjectBehaviorAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects363", type=uml_TracedStartObjectBehaviorAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedValueSpecificationActionActivations364: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedValueSpecificationActionActivations364",
    ends={
        Property(name="IntermediateActions_TracedValueSpecificationActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects365", type=IntermediateActions_TracedValueSpecificationActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAddVariableValueActions376: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAddVariableValueActions376",
    ends={
        Property(name="uml_TracedAddVariableValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects377", type=uml_TracedAddVariableValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClearStructuralFeatureActions378: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClearStructuralFeatureActions378",
    ends={
        Property(name="uml_TracedClearStructuralFeatureAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects379", type=uml_TracedClearStructuralFeatureAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAssociations380: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAssociations380",
    ends={
        Property(name="uml_TracedAssociation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects381", type=uml_TracedAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExpressions382: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExpressions382",
    ends={
        Property(name="uml_TracedExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects383", type=uml_TracedExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralReals374: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralReals374",
    ends={
        Property(name="uml_TracedLiteralReal", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects375", type=uml_TracedLiteralReal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedCreateObjectActionActivations388: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedCreateObjectActionActivations388",
    ends={
        Property(name="IntermediateActions_TracedCreateObjectActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects389", type=IntermediateActions_TracedCreateObjectActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCollaborations390: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCollaborations390",
    ends={
        Property(name="uml_TracedCollaboration", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects391", type=uml_TracedCollaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTestIdentityActions392: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTestIdentityActions392",
    ends={
        Property(name="uml_TracedTestIdentityAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects393", type=uml_TracedTestIdentityAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProfiles394: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProfiles394",
    ends={
        Property(name="uml_TracedProfile", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects395", type=uml_TracedProfile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedUnmarshallActions384: BinaryAssociation = BinaryAssociation(
    name="uml_tracedUnmarshallActions384",
    ends={
        Property(name="uml_TracedUnmarshallAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects385", type=uml_TracedUnmarshallAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSlots386: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSlots386",
    ends={
        Property(name="uml_TracedSlot", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects387", type=uml_TracedSlot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInterfaceRealizations402: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInterfaceRealizations402",
    ends={
        Property(name="uml_TracedInterfaceRealization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects403", type=uml_TracedInterfaceRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSendSignalActions404: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSendSignalActions404",
    ends={
        Property(name="uml_TracedSendSignalAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects405", type=uml_TracedSendSignalAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedFunctionBehaviors406: BinaryAssociation = BinaryAssociation(
    name="uml_tracedFunctionBehaviors406",
    ends={
        Property(name="uml_TracedFunctionBehavior", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects407", type=uml_TracedFunctionBehavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRemoveVariableValueActions396: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRemoveVariableValueActions396",
    ends={
        Property(name="uml_TracedRemoveVariableValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects397", type=uml_TracedRemoveVariableValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActors398: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActors398",
    ends={
        Property(name="uml_TracedActor", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects399", type=uml_TracedActor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedManifestations400: BinaryAssociation = BinaryAssociation(
    name="uml_tracedManifestations400",
    ends={
        Property(name="uml_TracedManifestation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects401", type=uml_TracedManifestation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadIsClassifiedObjectActions414: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadIsClassifiedObjectActions414",
    ends={
        Property(name="uml_TracedReadIsClassifiedObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects415", type=uml_TracedReadIsClassifiedObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateParameters416: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateParameters416",
    ends={
        Property(name="uml_TracedTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects417", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedMergeNodeActivations418: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedMergeNodeActivations418",
    ends={
        Property(name="IntermediateActivities_TracedMergeNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects419", type=IntermediateActivities_TracedMergeNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedValueSpecificationActions408: BinaryAssociation = BinaryAssociation(
    name="uml_tracedValueSpecificationActions408",
    ends={
        Property(name="uml_TracedValueSpecificationAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects409", type=uml_TracedValueSpecificationAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeExpressions410: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeExpressions410",
    ends={
        Property(name="uml_TracedTimeExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects411", type=uml_TracedTimeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAbstractions412: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAbstractions412",
    ends={
        Property(name="uml_TracedAbstraction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects413", type=uml_TracedAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClearAssociationActions426: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClearAssociationActions426",
    ends={
        Property(name="uml_TracedClearAssociationAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects427", type=uml_TracedClearAssociationAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedMergeNodes428: BinaryAssociation = BinaryAssociation(
    name="uml_tracedMergeNodes428",
    ends={
        Property(name="uml_TracedMergeNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects429", type=uml_TracedMergeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedElementImports430: BinaryAssociation = BinaryAssociation(
    name="uml_tracedElementImports430",
    ends={
        Property(name="uml_TracedElementImport", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects431", type=uml_TracedElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integerFunctions_tracedIntegerGreaterFunctionBehaviorExecutions420: BinaryAssociation = BinaryAssociation(
    name="integerFunctions_tracedIntegerGreaterFunctionBehaviorExecutions420",
    ends={
        Property(name="IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects421", type=IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPseudostates422: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPseudostates422",
    ends={
        Property(name="uml_TracedPseudostate", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects423", type=uml_TracedPseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLinkEndCreationDatas424: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLinkEndCreationDatas424",
    ends={
        Property(name="uml_TracedLinkEndCreationData", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects425", type=uml_TracedLinkEndCreationData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGates438: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGates438",
    ends={
        Property(name="uml_TracedGate", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects439", type=uml_TracedGate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeObservations440: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeObservations440",
    ends={
        Property(name="uml_TracedTimeObservation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects441", type=uml_TracedTimeObservation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedControlFlows442: BinaryAssociation = BinaryAssociation(
    name="uml_tracedControlFlows442",
    ends={
        Property(name="uml_TracedControlFlow", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects443", type=uml_TracedControlFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGeneralOrderings444: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGeneralOrderings444",
    ends={
        Property(name="uml_TracedGeneralOrdering", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects445", type=uml_TracedGeneralOrdering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedComponents432: BinaryAssociation = BinaryAssociation(
    name="uml_tracedComponents432",
    ends={
        Property(name="uml_TracedComponent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects433", type=uml_TracedComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClassifierTemplateParameters434: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClassifierTemplateParameters434",
    ends={
        Property(name="uml_TracedClassifierTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects435", type=uml_TracedClassifierTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActivityFinalNodes436: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivityFinalNodes436",
    ends={
        Property(name="uml_TracedActivityFinalNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects437", type=uml_TracedActivityFinalNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
runtimeModelElementTrace446: BinaryAssociation = BinaryAssociation(
    name="runtimeModelElementTrace446",
    ends={
        Property(name="448", type=umlTrace_Loci_TracedSemanticVisitor, multiplicity=Multiplicity(1, 1)),
        Property(name="0447", type=Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firingTrace449: BinaryAssociation = BinaryAssociation(
    name="firingTrace449",
    ends={
        Property(name="451", type=umlTrace_BasicActions_TracedActionActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="0450", type=Values_ActionActivation_firing_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent453: BinaryAssociation = BinaryAssociation(
    name="parent453",
    ends={
        Property(name="455", type=umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="0454", type=Loci_TracedSemanticVisitor, multiplicity=Multiplicity(1, 1))
    }
)
states456: BinaryAssociation = BinaryAssociation(
    name="states456",
    ends={
        Property(name="458", type=umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="0457", type=State, multiplicity=Multiplicity(1, 9999))
    }
)
states459: BinaryAssociation = BinaryAssociation(
    name="states459",
    ends={
        Property(name="461", type=umlTrace_Values_ActionActivation_firing_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="0460", type=State, multiplicity=Multiplicity(1, 9999))
    }
)
parent462: BinaryAssociation = BinaryAssociation(
    name="parent462",
    ends={
        Property(name="464", type=umlTrace_Values_ActionActivation_firing_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="0463", type=BasicActions_TracedActionActivation, multiplicity=Multiplicity(1, 1))
    }
)
runtimeModelElement452: BinaryAssociation = BinaryAssociation(
    name="runtimeModelElement452",
    ends={
        Property(name="uml_TracedElement", type=umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_SemanticVisitor_runtimeModelElement_Value", type=uml_TracedElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_umlTrace_uml_TracedRedefinableElement_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedRedefinableElement)
gen_umlTrace_uml_TracedNamespace_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedNamespace)
gen_umlTrace_uml_TracedActivityGroup_uml_TracedNamedElement = Generalization(general=uml_TracedNamedElement, specific=umlTrace_uml_TracedActivityGroup)
gen_umlTrace_uml_TracedActivityGroup_ActivityContent = Generalization(general=ActivityContent, specific=umlTrace_uml_TracedActivityGroup)
gen_umlTrace_uml_TracedCreateLinkObjectAction_TracedCreateLinkAction = Generalization(general=TracedCreateLinkAction, specific=umlTrace_uml_TracedCreateLinkObjectAction)
gen_umlTrace_uml_TracedCreateLinkAction_TracedWriteLinkAction = Generalization(general=TracedWriteLinkAction, specific=umlTrace_uml_TracedCreateLinkAction)
gen_umlTrace_uml_TracedWriteLinkAction_TracedLinkAction = Generalization(general=TracedLinkAction, specific=umlTrace_uml_TracedWriteLinkAction)
gen_umlTrace_uml_TracedLinkAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedLinkAction)
gen_umlTrace_uml_TracedInitialNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedInitialNode)
gen_umlTrace_uml_TracedControlNode_TracedActivityNode = Generalization(general=TracedActivityNode, specific=umlTrace_uml_TracedControlNode)
gen_umlTrace_uml_TracedFlowFinalNode_TracedFinalNode = Generalization(general=TracedFinalNode, specific=umlTrace_uml_TracedFlowFinalNode)
gen_umlTrace_uml_TracedFinalNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedFinalNode)
gen_umlTrace_uml_TracedExpansionRegion_TracedStructuredActivityNode = Generalization(general=TracedStructuredActivityNode, specific=umlTrace_uml_TracedExpansionRegion)
gen_umlTrace_uml_TracedCreateObjectAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedCreateObjectAction)
gen_umlTrace_uml_TracedLifeline_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedLifeline)
gen_umlTrace_uml_TracedDurationConstraint_TracedIntervalConstraint = Generalization(general=TracedIntervalConstraint, specific=umlTrace_uml_TracedDurationConstraint)
gen_umlTrace_uml_TracedIntervalConstraint_TracedConstraint = Generalization(general=TracedConstraint, specific=umlTrace_uml_TracedIntervalConstraint)
gen_umlTrace_uml_TracedCombinedFragment_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedCombinedFragment)
gen_umlTrace_uml_TracedInteractionFragment_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedInteractionFragment)
gen_umlTrace_uml_TracedNamedElement_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedNamedElement)
gen_umlTrace_uml_TracedElement_TracedEModelElement = Generalization(general=TracedEModelElement, specific=umlTrace_uml_TracedElement)
gen_umlTrace_uml_TracedConditionalNode_TracedStructuredActivityNode = Generalization(general=TracedStructuredActivityNode, specific=umlTrace_uml_TracedConditionalNode)
gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedAction = Generalization(general=uml_TracedAction, specific=umlTrace_uml_TracedStructuredActivityNode)
gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedStructuredActivityNode)
gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedActivityGroup = Generalization(general=uml_TracedActivityGroup, specific=umlTrace_uml_TracedStructuredActivityNode)
gen_umlTrace_uml_TracedAction_TracedExecutableNode = Generalization(general=TracedExecutableNode, specific=umlTrace_uml_TracedAction)
gen_umlTrace_uml_TracedExecutableNode_TracedActivityNode = Generalization(general=TracedActivityNode, specific=umlTrace_uml_TracedExecutableNode)
gen_umlTrace_uml_TracedActivityNode_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedActivityNode)
gen_umlTrace_uml_TracedActivityNode_ActivityContent = Generalization(general=ActivityContent, specific=umlTrace_uml_TracedActivityNode)
gen_umlTrace_uml_TracedInvocationAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedInvocationAction)
gen_umlTrace_uml_TracedOpaqueAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedOpaqueAction)
gen_umlTrace_uml_TracedProtocolConformance_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedProtocolConformance)
gen_umlTrace_uml_TracedDirectedRelationship_TracedRelationship = Generalization(general=TracedRelationship, specific=umlTrace_uml_TracedDirectedRelationship)
gen_umlTrace_uml_TracedRelationship_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedRelationship)
gen_umlTrace_uml_TracedCallBehaviorAction_TracedCallAction = Generalization(general=TracedCallAction, specific=umlTrace_uml_TracedCallBehaviorAction)
gen_umlTrace_uml_TracedCallAction_TracedInvocationAction = Generalization(general=TracedInvocationAction, specific=umlTrace_uml_TracedCallAction)
gen_umlTrace_uml_TracedPackageImport_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedPackageImport)
gen_umlTrace_uml_TracedClass_uml_TracedEncapsulatedClassifier = Generalization(general=uml_TracedEncapsulatedClassifier, specific=umlTrace_uml_TracedClass)
gen_umlTrace_uml_TracedClass_uml_TracedBehavioredClassifier = Generalization(general=uml_TracedBehavioredClassifier, specific=umlTrace_uml_TracedClass)
gen_umlTrace_uml_TracedEncapsulatedClassifier_TracedStructuredClassifier = Generalization(general=TracedStructuredClassifier, specific=umlTrace_uml_TracedEncapsulatedClassifier)
gen_umlTrace_uml_TracedStructuredClassifier_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedStructuredClassifier)
gen_umlTrace_uml_TracedClassifier_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedClassifier)
gen_umlTrace_uml_TracedClassifier_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedClassifier)
gen_umlTrace_uml_TracedClassifier_uml_TracedType = Generalization(general=uml_TracedType, specific=umlTrace_uml_TracedClassifier)
gen_umlTrace_uml_TracedClassifier_uml_TracedTemplateableElement = Generalization(general=uml_TracedTemplateableElement, specific=umlTrace_uml_TracedClassifier)
gen_umlTrace_uml_TracedType_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedType)
gen_umlTrace_uml_TracedBehavioredClassifier_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedBehavioredClassifier)
gen_umlTrace_uml_TracedActivityFinalNode_TracedFinalNode = Generalization(general=TracedFinalNode, specific=umlTrace_uml_TracedActivityFinalNode)
gen_umlTrace_uml_TracedObservation_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedObservation)
gen_umlTrace_uml_TracedInteractionUse_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedInteractionUse)
gen_umlTrace_uml_TracedLoopNode_TracedStructuredActivityNode = Generalization(general=TracedStructuredActivityNode, specific=umlTrace_uml_TracedLoopNode)
gen_umlTrace_uml_TracedConstraint_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedConstraint)
gen_umlTrace_uml_TracedPackageableElement_uml_TracedNamedElement = Generalization(general=uml_TracedNamedElement, specific=umlTrace_uml_TracedPackageableElement)
gen_umlTrace_uml_TracedPackageableElement_uml_TracedParameterableElement = Generalization(general=uml_TracedParameterableElement, specific=umlTrace_uml_TracedPackageableElement)
gen_umlTrace_uml_TracedParameterableElement_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedParameterableElement)
gen_umlTrace_uml_TracedPseudostate_TracedVertex = Generalization(general=TracedVertex, specific=umlTrace_uml_TracedPseudostate)
gen_umlTrace_uml_TracedVertex_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedVertex)
gen_umlTrace_uml_TracedDestructionOccurrenceSpecification_TracedMessageOccurrenceSpecification = Generalization(general=TracedMessageOccurrenceSpecification, specific=umlTrace_uml_TracedDestructionOccurrenceSpecification)
gen_umlTrace_uml_TracedMessageOccurrenceSpecification_uml_TracedOccurrenceSpecification = Generalization(general=uml_TracedOccurrenceSpecification, specific=umlTrace_uml_TracedMessageOccurrenceSpecification)
gen_umlTrace_uml_TracedMessageOccurrenceSpecification_uml_TracedMessageEnd = Generalization(general=uml_TracedMessageEnd, specific=umlTrace_uml_TracedMessageOccurrenceSpecification)
gen_umlTrace_uml_TracedOccurrenceSpecification_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedOccurrenceSpecification)
gen_umlTrace_uml_TracedMessageEnd_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedMessageEnd)
gen_umlTrace_uml_TracedPackage_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedPackage)
gen_umlTrace_uml_TracedPackage_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedPackage)
gen_umlTrace_uml_TracedPackage_uml_TracedTemplateableElement = Generalization(general=uml_TracedTemplateableElement, specific=umlTrace_uml_TracedPackage)
gen_umlTrace_uml_TracedTemplateableElement_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedTemplateableElement)
gen_umlTrace_uml_TracedConnector_TracedFeature = Generalization(general=TracedFeature, specific=umlTrace_uml_TracedConnector)
gen_umlTrace_uml_TracedFeature_TracedRedefinableElement = Generalization(general=TracedRedefinableElement, specific=umlTrace_uml_TracedFeature)
gen_umlTrace_uml_TracedSendObjectAction_TracedInvocationAction = Generalization(general=TracedInvocationAction, specific=umlTrace_uml_TracedSendObjectAction)
gen_umlTrace_uml_TracedInputPin_TracedPin = Generalization(general=TracedPin, specific=umlTrace_uml_TracedInputPin)
gen_umlTrace_uml_TracedPin_uml_TracedObjectNode = Generalization(general=uml_TracedObjectNode, specific=umlTrace_uml_TracedPin)
gen_umlTrace_uml_TracedPin_uml_TracedMultiplicityElement = Generalization(general=uml_TracedMultiplicityElement, specific=umlTrace_uml_TracedPin)
gen_umlTrace_uml_TracedObjectNode_uml_TracedActivityNode = Generalization(general=uml_TracedActivityNode, specific=umlTrace_uml_TracedObjectNode)
gen_umlTrace_uml_TracedObjectNode_uml_TracedTypedElement = Generalization(general=uml_TracedTypedElement, specific=umlTrace_uml_TracedObjectNode)
gen_umlTrace_uml_TracedDeploymentSpecification_TracedArtifact = Generalization(general=TracedArtifact, specific=umlTrace_uml_TracedDeploymentSpecification)
gen_umlTrace_uml_TracedArtifact_uml_TracedClassifier = Generalization(general=uml_TracedClassifier, specific=umlTrace_uml_TracedArtifact)
gen_umlTrace_uml_TracedArtifact_uml_TracedDeployedArtifact = Generalization(general=uml_TracedDeployedArtifact, specific=umlTrace_uml_TracedArtifact)
gen_umlTrace_uml_TracedDeployedArtifact_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedDeployedArtifact)
gen_umlTrace_uml_TracedTransition_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedTransition)
gen_umlTrace_uml_TracedTransition_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedTransition)
gen_umlTrace_uml_TracedNode_uml_TracedClass = Generalization(general=uml_TracedClass, specific=umlTrace_uml_TracedNode)
gen_umlTrace_uml_TracedNode_uml_TracedDeploymentTarget = Generalization(general=uml_TracedDeploymentTarget, specific=umlTrace_uml_TracedNode)
gen_umlTrace_uml_TracedExceptionHandler_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedExceptionHandler)
gen_umlTrace_uml_TracedSequenceNode_TracedStructuredActivityNode = Generalization(general=TracedStructuredActivityNode, specific=umlTrace_uml_TracedSequenceNode)
gen_umlTrace_uml_TracedUseCase_TracedBehavioredClassifier = Generalization(general=TracedBehavioredClassifier, specific=umlTrace_uml_TracedUseCase)
gen_umlTrace_uml_TracedStartClassifierBehaviorAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedStartClassifierBehaviorAction)
gen_umlTrace_uml_TracedExtend_uml_TracedNamedElement = Generalization(general=uml_TracedNamedElement, specific=umlTrace_uml_TracedExtend)
gen_umlTrace_uml_TracedExtend_uml_TracedDirectedRelationship = Generalization(general=uml_TracedDirectedRelationship, specific=umlTrace_uml_TracedExtend)
gen_umlTrace_uml_TracedRemoveStructuralFeatureValueAction_TracedWriteStructuralFeatureAction = Generalization(general=TracedWriteStructuralFeatureAction, specific=umlTrace_uml_TracedRemoveStructuralFeatureValueAction)
gen_umlTrace_uml_TracedWriteStructuralFeatureAction_TracedStructuralFeatureAction = Generalization(general=TracedStructuralFeatureAction, specific=umlTrace_uml_TracedWriteStructuralFeatureAction)
gen_umlTrace_uml_TracedStructuralFeatureAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedStructuralFeatureAction)
gen_umlTrace_uml_TracedSignal_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedSignal)
gen_umlTrace_uml_TracedGeneralizationSet_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedGeneralizationSet)
gen_umlTrace_uml_TracedChangeEvent_TracedEvent = Generalization(general=TracedEvent, specific=umlTrace_uml_TracedChangeEvent)
gen_umlTrace_uml_TracedEvent_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedEvent)
gen_umlTrace_uml_TracedDependency_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedDependency)
gen_umlTrace_uml_TracedDependency_uml_TracedDirectedRelationship = Generalization(general=uml_TracedDirectedRelationship, specific=umlTrace_uml_TracedDependency)
gen_umlTrace_uml_TracedPort_TracedProperty = Generalization(general=TracedProperty, specific=umlTrace_uml_TracedPort)
gen_umlTrace_uml_TracedProperty_uml_TracedStructuralFeature = Generalization(general=uml_TracedStructuralFeature, specific=umlTrace_uml_TracedProperty)
gen_umlTrace_uml_TracedProperty_uml_TracedConnectableElement = Generalization(general=uml_TracedConnectableElement, specific=umlTrace_uml_TracedProperty)
gen_umlTrace_uml_TracedProperty_uml_TracedDeploymentTarget = Generalization(general=uml_TracedDeploymentTarget, specific=umlTrace_uml_TracedProperty)
gen_umlTrace_uml_TracedStructuralFeature_uml_TracedFeature = Generalization(general=uml_TracedFeature, specific=umlTrace_uml_TracedStructuralFeature)
gen_umlTrace_uml_TracedStructuralFeature_uml_TracedTypedElement = Generalization(general=uml_TracedTypedElement, specific=umlTrace_uml_TracedStructuralFeature)
gen_umlTrace_uml_TracedStructuralFeature_uml_TracedMultiplicityElement = Generalization(general=uml_TracedMultiplicityElement, specific=umlTrace_uml_TracedStructuralFeature)
gen_umlTrace_uml_TracedTypedElement_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedTypedElement)
gen_umlTrace_uml_TracedMultiplicityElement_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedMultiplicityElement)
gen_umlTrace_uml_TracedConnectableElement_uml_TracedTypedElement = Generalization(general=uml_TracedTypedElement, specific=umlTrace_uml_TracedConnectableElement)
gen_umlTrace_uml_TracedConnectableElement_uml_TracedParameterableElement = Generalization(general=uml_TracedParameterableElement, specific=umlTrace_uml_TracedConnectableElement)
gen_umlTrace_uml_TracedDeploymentTarget_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedDeploymentTarget)
gen_umlTrace_uml_TracedCollaborationUse_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedCollaborationUse)
gen_umlTrace_uml_TracedValuePin_TracedInputPin = Generalization(general=TracedInputPin, specific=umlTrace_uml_TracedValuePin)
gen_umlTrace_uml_TracedBehavior_TracedClass = Generalization(general=TracedClass, specific=umlTrace_uml_TracedBehavior)
gen_umlTrace_uml_TracedSlot_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedSlot)
gen_umlTrace_uml_TracedLiteralNull_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralNull)
gen_umlTrace_uml_TracedParameter_uml_TracedConnectableElement = Generalization(general=uml_TracedConnectableElement, specific=umlTrace_uml_TracedParameter)
gen_umlTrace_uml_TracedParameter_uml_TracedMultiplicityElement = Generalization(general=uml_TracedMultiplicityElement, specific=umlTrace_uml_TracedParameter)
gen_umlTrace_uml_TracedOpaqueExpression_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedOpaqueExpression)
gen_umlTrace_uml_TracedTrigger_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedTrigger)
gen_umlTrace_uml_TracedStateInvariant_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedStateInvariant)
gen_umlTrace_uml_TracedAssociationClass_uml_TracedClass = Generalization(general=uml_TracedClass, specific=umlTrace_uml_TracedAssociationClass)
gen_umlTrace_uml_TracedAssociationClass_uml_TracedAssociation = Generalization(general=uml_TracedAssociation, specific=umlTrace_uml_TracedAssociationClass)
gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedDeploymentTarget = Generalization(general=uml_TracedDeploymentTarget, specific=umlTrace_uml_TracedInstanceSpecification)
gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedInstanceSpecification)
gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedDeployedArtifact = Generalization(general=uml_TracedDeployedArtifact, specific=umlTrace_uml_TracedInstanceSpecification)
gen_umlTrace_uml_TracedTemplateSignature_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedTemplateSignature)
gen_umlTrace_uml_TracedLinkEndDestructionData_TracedLinkEndData = Generalization(general=TracedLinkEndData, specific=umlTrace_uml_TracedLinkEndDestructionData)
gen_umlTrace_uml_TracedLinkEndData_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedLinkEndData)
gen_umlTrace_uml_TracedAcceptCallAction_TracedAcceptEventAction = Generalization(general=TracedAcceptEventAction, specific=umlTrace_uml_TracedAcceptCallAction)
gen_umlTrace_uml_TracedAcceptEventAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedAcceptEventAction)
gen_umlTrace_uml_TracedReduceAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReduceAction)
gen_umlTrace_uml_TracedRaiseExceptionAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedRaiseExceptionAction)
gen_umlTrace_uml_TracedStereotype_TracedClass = Generalization(general=TracedClass, specific=umlTrace_uml_TracedStereotype)
gen_umlTrace_uml_TracedClearAssociationAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedClearAssociationAction)
gen_umlTrace_uml_TracedEnumerationLiteral_TracedInstanceSpecification = Generalization(general=TracedInstanceSpecification, specific=umlTrace_uml_TracedEnumerationLiteral)
gen_umlTrace_uml_TracedSubstitution_TracedRealization = Generalization(general=TracedRealization, specific=umlTrace_uml_TracedSubstitution)
gen_umlTrace_uml_TracedReadLinkAction_TracedLinkAction = Generalization(general=TracedLinkAction, specific=umlTrace_uml_TracedReadLinkAction)
gen_umlTrace_uml_TracedExtension_TracedAssociation = Generalization(general=TracedAssociation, specific=umlTrace_uml_TracedExtension)
gen_umlTrace_uml_TracedAssociation_uml_TracedClassifier = Generalization(general=uml_TracedClassifier, specific=umlTrace_uml_TracedAssociation)
gen_umlTrace_uml_TracedAssociation_uml_TracedRelationship = Generalization(general=uml_TracedRelationship, specific=umlTrace_uml_TracedAssociation)
gen_umlTrace_uml_TracedExecutionEnvironment_TracedNode = Generalization(general=TracedNode, specific=umlTrace_uml_TracedExecutionEnvironment)
gen_umlTrace_uml_TracedConsiderIgnoreFragment_TracedCombinedFragment = Generalization(general=TracedCombinedFragment, specific=umlTrace_uml_TracedConsiderIgnoreFragment)
gen_umlTrace_uml_TracedContinuation_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedContinuation)
gen_umlTrace_uml_TracedCallOperationAction_TracedCallAction = Generalization(general=TracedCallAction, specific=umlTrace_uml_TracedCallOperationAction)
gen_umlTrace_uml_TracedTimeConstraint_TracedIntervalConstraint = Generalization(general=TracedIntervalConstraint, specific=umlTrace_uml_TracedTimeConstraint)
gen_umlTrace_uml_TracedClearVariableAction_TracedVariableAction = Generalization(general=TracedVariableAction, specific=umlTrace_uml_TracedClearVariableAction)
gen_umlTrace_uml_TracedVariableAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedVariableAction)
gen_umlTrace_uml_TracedReadSelfAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadSelfAction)
gen_umlTrace_uml_TracedLiteralString_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralString)
gen_umlTrace_uml_TracedLiteralSpecification_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedLiteralSpecification)
gen_umlTrace_uml_TracedValueSpecification_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedValueSpecification)
gen_umlTrace_uml_TracedValueSpecification_uml_TracedTypedElement = Generalization(general=uml_TracedTypedElement, specific=umlTrace_uml_TracedValueSpecification)
gen_umlTrace_uml_TracedBroadcastSignalAction_TracedInvocationAction = Generalization(general=TracedInvocationAction, specific=umlTrace_uml_TracedBroadcastSignalAction)
gen_umlTrace_uml_TracedInteraction_uml_TracedBehavior = Generalization(general=uml_TracedBehavior, specific=umlTrace_uml_TracedInteraction)
gen_umlTrace_uml_TracedInteraction_uml_TracedInteractionFragment = Generalization(general=uml_TracedInteractionFragment, specific=umlTrace_uml_TracedInteraction)
gen_umlTrace_uml_TracedActivityEdge_TracedRedefinableElement = Generalization(general=TracedRedefinableElement, specific=umlTrace_uml_TracedActivityEdge)
gen_umlTrace_uml_TracedTestIdentityAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedTestIdentityAction)
gen_umlTrace_uml_TracedInstanceValue_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedInstanceValue)
gen_umlTrace_uml_TracedLiteralUnlimitedNatural_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralUnlimitedNatural)
gen_umlTrace_uml_TracedReclassifyObjectAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReclassifyObjectAction)
gen_umlTrace_uml_TracedTimeEvent_TracedEvent = Generalization(general=TracedEvent, specific=umlTrace_uml_TracedTimeEvent)
gen_umlTrace_uml_TracedPartDecomposition_TracedInteractionUse = Generalization(general=TracedInteractionUse, specific=umlTrace_uml_TracedPartDecomposition)
gen_umlTrace_uml_TracedInterruptibleActivityRegion_TracedActivityGroup = Generalization(general=TracedActivityGroup, specific=umlTrace_uml_TracedInterruptibleActivityRegion)
gen_umlTrace_uml_TracedAddVariableValueAction_TracedWriteVariableAction = Generalization(general=TracedWriteVariableAction, specific=umlTrace_uml_TracedAddVariableValueAction)
gen_umlTrace_uml_TracedWriteVariableAction_TracedVariableAction = Generalization(general=TracedVariableAction, specific=umlTrace_uml_TracedWriteVariableAction)
gen_umlTrace_uml_TracedProtocolTransition_TracedTransition = Generalization(general=TracedTransition, specific=umlTrace_uml_TracedProtocolTransition)
gen_umlTrace_uml_TracedImage_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedImage)
gen_umlTrace_uml_TracedLiteralReal_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralReal)
gen_umlTrace_uml_TracedInteractionOperand_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedInteractionOperand)
gen_umlTrace_uml_TracedInteractionOperand_uml_TracedInteractionFragment = Generalization(general=uml_TracedInteractionFragment, specific=umlTrace_uml_TracedInteractionOperand)
gen_umlTrace_uml_TracedGeneralization_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedGeneralization)
gen_umlTrace_uml_TracedInformationItem_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedInformationItem)
gen_umlTrace_uml_TracedModel_TracedPackage = Generalization(general=TracedPackage, specific=umlTrace_uml_TracedModel)
gen_umlTrace_uml_TracedClassifierTemplateParameter_TracedTemplateParameter = Generalization(general=TracedTemplateParameter, specific=umlTrace_uml_TracedClassifierTemplateParameter)
gen_umlTrace_uml_TracedTemplateParameter_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedTemplateParameter)
gen_umlTrace_uml_TracedRealization_TracedAbstraction = Generalization(general=TracedAbstraction, specific=umlTrace_uml_TracedRealization)
gen_umlTrace_uml_TracedAbstraction_TracedDependency = Generalization(general=TracedDependency, specific=umlTrace_uml_TracedAbstraction)
gen_umlTrace_uml_TracedExecutionSpecification_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedExecutionSpecification)
gen_umlTrace_uml_TracedReplyAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReplyAction)
gen_umlTrace_uml_TracedActor_TracedBehavioredClassifier = Generalization(general=TracedBehavioredClassifier, specific=umlTrace_uml_TracedActor)
gen_umlTrace_uml_TracedInformationFlow_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedInformationFlow)
gen_umlTrace_uml_TracedInformationFlow_uml_TracedDirectedRelationship = Generalization(general=uml_TracedDirectedRelationship, specific=umlTrace_uml_TracedInformationFlow)
gen_umlTrace_uml_TracedDestroyObjectAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedDestroyObjectAction)
gen_umlTrace_uml_TracedActivityPartition_TracedActivityGroup = Generalization(general=TracedActivityGroup, specific=umlTrace_uml_TracedActivityPartition)
gen_umlTrace_uml_TracedStateMachine_TracedBehavior = Generalization(general=TracedBehavior, specific=umlTrace_uml_TracedStateMachine)
gen_umlTrace_uml_TracedMessage_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedMessage)
gen_umlTrace_uml_TracedReadLinkObjectEndQualifierAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadLinkObjectEndQualifierAction)
gen_umlTrace_uml_TracedDeployment_TracedDependency = Generalization(general=TracedDependency, specific=umlTrace_uml_TracedDeployment)
gen_umlTrace_uml_TracedActivity_TracedBehavior = Generalization(general=TracedBehavior, specific=umlTrace_uml_TracedActivity)
gen_umlTrace_uml_TracedForkNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedForkNode)
gen_umlTrace_uml_TracedProtocolStateMachine_TracedStateMachine = Generalization(general=TracedStateMachine, specific=umlTrace_uml_TracedProtocolStateMachine)
gen_umlTrace_uml_TracedInterval_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedInterval)
gen_umlTrace_uml_TracedClearStructuralFeatureAction_TracedStructuralFeatureAction = Generalization(general=TracedStructuralFeatureAction, specific=umlTrace_uml_TracedClearStructuralFeatureAction)
gen_umlTrace_uml_TracedObjectFlow_TracedActivityEdge = Generalization(general=TracedActivityEdge, specific=umlTrace_uml_TracedObjectFlow)
gen_umlTrace_uml_TracedLiteralInteger_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralInteger)
gen_umlTrace_uml_TracedSignalEvent_TracedMessageEvent = Generalization(general=TracedMessageEvent, specific=umlTrace_uml_TracedSignalEvent)
gen_umlTrace_uml_TracedReadLinkObjectEndAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadLinkObjectEndAction)
gen_umlTrace_uml_TracedTimeInterval_TracedInterval = Generalization(general=TracedInterval, specific=umlTrace_uml_TracedTimeInterval)
gen_umlTrace_uml_TracedOperationTemplateParameter_TracedTemplateParameter = Generalization(general=TracedTemplateParameter, specific=umlTrace_uml_TracedOperationTemplateParameter)
gen_umlTrace_uml_TracedDurationObservation_TracedObservation = Generalization(general=TracedObservation, specific=umlTrace_uml_TracedDurationObservation)
gen_umlTrace_uml_TracedConnectionPointReference_TracedVertex = Generalization(general=TracedVertex, specific=umlTrace_uml_TracedConnectionPointReference)
gen_umlTrace_uml_TracedTimeExpression_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedTimeExpression)
gen_umlTrace_uml_TracedQualifierValue_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedQualifierValue)
gen_umlTrace_uml_TracedDurationInterval_TracedInterval = Generalization(general=TracedInterval, specific=umlTrace_uml_TracedDurationInterval)
gen_umlTrace_uml_TracedFunctionBehavior_TracedOpaqueBehavior = Generalization(general=TracedOpaqueBehavior, specific=umlTrace_uml_TracedFunctionBehavior)
gen_umlTrace_uml_TracedOpaqueBehavior_TracedBehavior = Generalization(general=TracedBehavior, specific=umlTrace_uml_TracedOpaqueBehavior)
gen_umlTrace_uml_TracedInterfaceRealization_TracedRealization = Generalization(general=TracedRealization, specific=umlTrace_uml_TracedInterfaceRealization)
gen_umlTrace_uml_TracedDevice_TracedNode = Generalization(general=TracedNode, specific=umlTrace_uml_TracedDevice)
gen_umlTrace_uml_TracedTemplateParameterSubstitution_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedTemplateParameterSubstitution)
gen_umlTrace_uml_TracedJoinNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedJoinNode)
gen_umlTrace_uml_TracedRedefinableTemplateSignature_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedRedefinableTemplateSignature)
gen_umlTrace_uml_TracedRedefinableTemplateSignature_uml_TracedTemplateSignature = Generalization(general=uml_TracedTemplateSignature, specific=umlTrace_uml_TracedRedefinableTemplateSignature)
gen_umlTrace_uml_TracedReadIsClassifiedObjectAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadIsClassifiedObjectAction)
gen_umlTrace_uml_TracedTimeObservation_TracedObservation = Generalization(general=TracedObservation, specific=umlTrace_uml_TracedTimeObservation)
gen_umlTrace_uml_TracedDecisionNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedDecisionNode)
gen_umlTrace_uml_TracedElementImport_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedElementImport)
gen_umlTrace_uml_TracedOperation_uml_TracedBehavioralFeature = Generalization(general=uml_TracedBehavioralFeature, specific=umlTrace_uml_TracedOperation)
gen_umlTrace_uml_TracedOperation_uml_TracedParameterableElement = Generalization(general=uml_TracedParameterableElement, specific=umlTrace_uml_TracedOperation)
gen_umlTrace_uml_TracedOperation_uml_TracedTemplateableElement = Generalization(general=uml_TracedTemplateableElement, specific=umlTrace_uml_TracedOperation)
gen_umlTrace_uml_TracedBehavioralFeature_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedBehavioralFeature)
gen_umlTrace_uml_TracedBehavioralFeature_uml_TracedFeature = Generalization(general=uml_TracedFeature, specific=umlTrace_uml_TracedBehavioralFeature)
gen_umlTrace_uml_TracedAnyReceiveEvent_TracedMessageEvent = Generalization(general=TracedMessageEvent, specific=umlTrace_uml_TracedAnyReceiveEvent)
gen_umlTrace_uml_TracedMessageEvent_TracedEvent = Generalization(general=TracedEvent, specific=umlTrace_uml_TracedMessageEvent)
gen_umlTrace_uml_TracedPrimitiveType_TracedDataType = Generalization(general=TracedDataType, specific=umlTrace_uml_TracedPrimitiveType)
gen_umlTrace_uml_TracedDataType_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedDataType)
gen_umlTrace_uml_TracedReadStructuralFeatureAction_TracedStructuralFeatureAction = Generalization(general=TracedStructuralFeatureAction, specific=umlTrace_uml_TracedReadStructuralFeatureAction)
gen_umlTrace_uml_TracedParameterSet_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedParameterSet)
gen_umlTrace_uml_TracedDataStoreNode_TracedCentralBufferNode = Generalization(general=TracedCentralBufferNode, specific=umlTrace_uml_TracedDataStoreNode)
gen_umlTrace_uml_TracedCentralBufferNode_TracedObjectNode = Generalization(general=TracedObjectNode, specific=umlTrace_uml_TracedCentralBufferNode)
gen_umlTrace_uml_TracedSendSignalAction_TracedInvocationAction = Generalization(general=TracedInvocationAction, specific=umlTrace_uml_TracedSendSignalAction)
gen_umlTrace_uml_TracedReception_TracedBehavioralFeature = Generalization(general=TracedBehavioralFeature, specific=umlTrace_uml_TracedReception)
gen_umlTrace_uml_TracedTemplateBinding_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedTemplateBinding)
gen_umlTrace_uml_TracedUsage_TracedDependency = Generalization(general=TracedDependency, specific=umlTrace_uml_TracedUsage)
gen_umlTrace_uml_TracedActionInputPin_TracedInputPin = Generalization(general=TracedInputPin, specific=umlTrace_uml_TracedActionInputPin)
gen_umlTrace_uml_TracedReadVariableAction_TracedVariableAction = Generalization(general=TracedVariableAction, specific=umlTrace_uml_TracedReadVariableAction)
gen_umlTrace_uml_TracedDestroyLinkAction_TracedWriteLinkAction = Generalization(general=TracedWriteLinkAction, specific=umlTrace_uml_TracedDestroyLinkAction)
gen_umlTrace_uml_TracedOutputPin_TracedPin = Generalization(general=TracedPin, specific=umlTrace_uml_TracedOutputPin)
gen_umlTrace_uml_TracedDuration_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedDuration)
gen_umlTrace_uml_TracedUnmarshallAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedUnmarshallAction)
gen_umlTrace_uml_TracedProfile_TracedPackage = Generalization(general=TracedPackage, specific=umlTrace_uml_TracedProfile)
gen_umlTrace_uml_TracedExtensionEnd_TracedProperty = Generalization(general=TracedProperty, specific=umlTrace_uml_TracedExtensionEnd)
gen_umlTrace_uml_TracedExpansionNode_TracedObjectNode = Generalization(general=TracedObjectNode, specific=umlTrace_uml_TracedExpansionNode)
gen_umlTrace_uml_TracedActivityParameterNode_TracedObjectNode = Generalization(general=TracedObjectNode, specific=umlTrace_uml_TracedActivityParameterNode)
gen_umlTrace_uml_TracedProfileApplication_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedProfileApplication)
gen_umlTrace_uml_TracedConnectorEnd_TracedMultiplicityElement = Generalization(general=TracedMultiplicityElement, specific=umlTrace_uml_TracedConnectorEnd)
gen_umlTrace_uml_TracedEnumeration_TracedDataType = Generalization(general=TracedDataType, specific=umlTrace_uml_TracedEnumeration)
gen_umlTrace_uml_TracedCollaboration_uml_TracedStructuredClassifier = Generalization(general=uml_TracedStructuredClassifier, specific=umlTrace_uml_TracedCollaboration)
gen_umlTrace_uml_TracedCollaboration_uml_TracedBehavioredClassifier = Generalization(general=uml_TracedBehavioredClassifier, specific=umlTrace_uml_TracedCollaboration)
gen_umlTrace_uml_TracedVariable_uml_TracedConnectableElement = Generalization(general=uml_TracedConnectableElement, specific=umlTrace_uml_TracedVariable)
gen_umlTrace_uml_TracedVariable_uml_TracedMultiplicityElement = Generalization(general=uml_TracedMultiplicityElement, specific=umlTrace_uml_TracedVariable)
gen_umlTrace_uml_TracedValueSpecificationAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedValueSpecificationAction)
gen_umlTrace_uml_TracedReadExtentAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadExtentAction)
gen_umlTrace_uml_TracedStringExpression_uml_TracedExpression = Generalization(general=uml_TracedExpression, specific=umlTrace_uml_TracedStringExpression)
gen_umlTrace_uml_TracedStringExpression_uml_TracedTemplateableElement = Generalization(general=uml_TracedTemplateableElement, specific=umlTrace_uml_TracedStringExpression)
gen_umlTrace_uml_TracedExpression_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedExpression)
gen_umlTrace_uml_TracedGeneralOrdering_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedGeneralOrdering)
gen_umlTrace_uml_TracedLiteralBoolean_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralBoolean)
gen_umlTrace_uml_TracedStartObjectBehaviorAction_TracedCallAction = Generalization(general=TracedCallAction, specific=umlTrace_uml_TracedStartObjectBehaviorAction)
gen_umlTrace_uml_TracedRegion_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedRegion)
gen_umlTrace_uml_TracedRegion_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedRegion)
gen_umlTrace_uml_TracedExtensionPoint_TracedRedefinableElement = Generalization(general=TracedRedefinableElement, specific=umlTrace_uml_TracedExtensionPoint)
gen_umlTrace_uml_TracedExecutionOccurrenceSpecification_TracedOccurrenceSpecification = Generalization(general=TracedOccurrenceSpecification, specific=umlTrace_uml_TracedExecutionOccurrenceSpecification)
gen_umlTrace_uml_TracedInteractionConstraint_TracedConstraint = Generalization(general=TracedConstraint, specific=umlTrace_uml_TracedInteractionConstraint)
gen_umlTrace_uml_TracedAddStructuralFeatureValueAction_TracedWriteStructuralFeatureAction = Generalization(general=TracedWriteStructuralFeatureAction, specific=umlTrace_uml_TracedAddStructuralFeatureValueAction)
gen_umlTrace_uml_TracedInterface_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedInterface)
gen_umlTrace_uml_TracedComponent_TracedClass = Generalization(general=TracedClass, specific=umlTrace_uml_TracedComponent)
gen_umlTrace_uml_TracedCallEvent_TracedMessageEvent = Generalization(general=TracedMessageEvent, specific=umlTrace_uml_TracedCallEvent)
gen_umlTrace_uml_TracedComment_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedComment)
gen_umlTrace_uml_TracedBehaviorExecutionSpecification_TracedExecutionSpecification = Generalization(general=TracedExecutionSpecification, specific=umlTrace_uml_TracedBehaviorExecutionSpecification)
gen_umlTrace_uml_TracedComponentRealization_TracedRealization = Generalization(general=TracedRealization, specific=umlTrace_uml_TracedComponentRealization)
gen_umlTrace_uml_TracedCommunicationPath_TracedAssociation = Generalization(general=TracedAssociation, specific=umlTrace_uml_TracedCommunicationPath)
gen_umlTrace_uml_TracedPackageMerge_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedPackageMerge)
gen_umlTrace_uml_TracedClause_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedClause)
gen_umlTrace_uml_TracedFinalState_TracedState = Generalization(general=TracedState, specific=umlTrace_uml_TracedFinalState)
gen_umlTrace_uml_TracedState_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedState)
gen_umlTrace_uml_TracedState_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedState)
gen_umlTrace_uml_TracedState_uml_TracedVertex = Generalization(general=uml_TracedVertex, specific=umlTrace_uml_TracedState)
gen_umlTrace_uml_TracedConnectableElementTemplateParameter_TracedTemplateParameter = Generalization(general=TracedTemplateParameter, specific=umlTrace_uml_TracedConnectableElementTemplateParameter)
gen_umlTrace_uml_TracedActionExecutionSpecification_TracedExecutionSpecification = Generalization(general=TracedExecutionSpecification, specific=umlTrace_uml_TracedActionExecutionSpecification)
gen_umlTrace_IntermediateActivities_TracedObjectNodeActivation_TracedActivityNodeActivation = Generalization(general=TracedActivityNodeActivation, specific=umlTrace_IntermediateActivities_TracedObjectNodeActivation)
gen_umlTrace_IntermediateActivities_TracedInitialNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedInitialNodeActivation)
gen_umlTrace_IntermediateActivities_TracedActivityExecution_TracedExecution = Generalization(general=TracedExecution, specific=umlTrace_IntermediateActivities_TracedActivityExecution)
gen_umlTrace_IntermediateActivities_TracedMergeNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedMergeNodeActivation)
gen_umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation_TracedObjectNodeActivation = Generalization(general=TracedObjectNodeActivation, specific=umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation)
gen_umlTrace_IntermediateActivities_TracedJoinNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedJoinNodeActivation)
gen_umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation)
gen_umlTrace_IntermediateActivities_TracedDecisionNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedDecisionNodeActivation)
gen_umlTrace_BasicActions_TracedPinActivation_TracedObjectNodeActivation = Generalization(general=TracedObjectNodeActivation, specific=umlTrace_BasicActions_TracedPinActivation)
gen_umlTrace_BasicActions_TracedActionActivation_TracedActivityNodeActivation = Generalization(general=TracedActivityNodeActivation, specific=umlTrace_BasicActions_TracedActionActivation)
gen_umlTrace_uml_TracedInclude_uml_TracedNamedElement = Generalization(general=uml_TracedNamedElement, specific=umlTrace_uml_TracedInclude)
gen_umlTrace_uml_TracedInclude_uml_TracedDirectedRelationship = Generalization(general=uml_TracedDirectedRelationship, specific=umlTrace_uml_TracedInclude)
gen_umlTrace_uml_TracedControlFlow_TracedActivityEdge = Generalization(general=TracedActivityEdge, specific=umlTrace_uml_TracedControlFlow)
gen_umlTrace_uml_TracedGate_TracedMessageEnd = Generalization(general=TracedMessageEnd, specific=umlTrace_uml_TracedGate)
gen_umlTrace_uml_TracedRemoveVariableValueAction_TracedWriteVariableAction = Generalization(general=TracedWriteVariableAction, specific=umlTrace_uml_TracedRemoveVariableValueAction)
gen_umlTrace_uml_TracedManifestation_TracedAbstraction = Generalization(general=TracedAbstraction, specific=umlTrace_uml_TracedManifestation)
gen_umlTrace_uml_TracedLinkEndCreationData_TracedLinkEndData = Generalization(general=TracedLinkEndData, specific=umlTrace_uml_TracedLinkEndCreationData)
gen_umlTrace_uml_TracedMergeNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedMergeNode)
gen_umlTrace_IntermediateActivities_TracedForkNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedForkNodeActivation)
gen_umlTrace_IntermediateActivities_TracedControlNodeActivation_TracedActivityNodeActivation = Generalization(general=TracedActivityNodeActivation, specific=umlTrace_IntermediateActivities_TracedControlNodeActivation)
gen_umlTrace_IntermediateActivities_TracedActivityNodeActivation_TracedSemanticVisitor = Generalization(general=TracedSemanticVisitor, specific=umlTrace_IntermediateActivities_TracedActivityNodeActivation)
gen_umlTrace_IntermediateActions_TracedCreateObjectActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_IntermediateActions_TracedCreateObjectActionActivation)
gen_umlTrace_BasicBehaviors_TracedExecution_TracedObject = Generalization(general=TracedObject, specific=umlTrace_BasicBehaviors_TracedExecution)
gen_umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution_TracedExecution = Generalization(general=TracedExecution, specific=umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution)
gen_umlTrace_Kernel_TracedObject_TracedExtensionalValue = Generalization(general=TracedExtensionalValue, specific=umlTrace_Kernel_TracedObject)
gen_umlTrace_Kernel_TracedExtensionalValue_TracedCompoundValue = Generalization(general=TracedCompoundValue, specific=umlTrace_Kernel_TracedExtensionalValue)
gen_umlTrace_Kernel_TracedCompoundValue_TracedStructuredValue = Generalization(general=TracedStructuredValue, specific=umlTrace_Kernel_TracedCompoundValue)
gen_umlTrace_Kernel_TracedStructuredValue_TracedValue = Generalization(general=TracedValue, specific=umlTrace_Kernel_TracedStructuredValue)
gen_umlTrace_Kernel_TracedValue_TracedSemanticVisitor = Generalization(general=TracedSemanticVisitor, specific=umlTrace_Kernel_TracedValue)
gen_umlTrace_Kernel_TracedReference_TracedStructuredValue = Generalization(general=TracedStructuredValue, specific=umlTrace_Kernel_TracedReference)
gen_umlTrace_Kernel_TracedLiteralEvaluation_TracedEvaluation = Generalization(general=TracedEvaluation, specific=umlTrace_Kernel_TracedLiteralEvaluation)
gen_umlTrace_Kernel_TracedEvaluation_TracedSemanticVisitor = Generalization(general=TracedSemanticVisitor, specific=umlTrace_Kernel_TracedEvaluation)
gen_umlTrace_BasicActions_TracedInvocationActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_BasicActions_TracedInvocationActionActivation)
gen_umlTrace_BasicActions_TracedCallActionActivation_TracedInvocationActionActivation = Generalization(general=TracedInvocationActionActivation, specific=umlTrace_BasicActions_TracedCallActionActivation)
gen_umlTrace_BasicActions_TracedOpaqueActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_BasicActions_TracedOpaqueActionActivation)
gen_umlTrace_BasicActions_TracedInputPinActivation_TracedPinActivation = Generalization(general=TracedPinActivation, specific=umlTrace_BasicActions_TracedInputPinActivation)
gen_umlTrace_BasicActions_TracedCallBehaviorActionActivation_TracedCallActionActivation = Generalization(general=TracedCallActionActivation, specific=umlTrace_BasicActions_TracedCallBehaviorActionActivation)
gen_umlTrace_BasicActions_TracedOutputPinActivation_TracedPinActivation = Generalization(general=TracedPinActivation, specific=umlTrace_BasicActions_TracedOutputPinActivation)
gen_umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation)
gen_umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation = Generalization(general=TracedStructuralFeatureActionActivation, specific=umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation)
gen_umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation_TracedWriteStructuralFeatureActionActivation = Generalization(general=TracedWriteStructuralFeatureActionActivation, specific=umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation)
gen_umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation = Generalization(general=TracedStructuralFeatureActionActivation, specific=umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation)
gen_umlTrace_IntermediateActions_TracedValueSpecificationActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_IntermediateActions_TracedValueSpecificationActionActivation)
gen_umlTrace_Kernel_TracedIntegerValue_TracedPrimitiveValue = Generalization(general=TracedPrimitiveValue, specific=umlTrace_Kernel_TracedIntegerValue)
gen_umlTrace_Kernel_TracedPrimitiveValue_TracedValue = Generalization(general=TracedValue, specific=umlTrace_Kernel_TracedPrimitiveValue)
gen_umlTrace_Kernel_TracedLiteralBooleanEvaluation_TracedLiteralEvaluation = Generalization(general=TracedLiteralEvaluation, specific=umlTrace_Kernel_TracedLiteralBooleanEvaluation)
gen_umlTrace_Kernel_TracedBooleanValue_TracedPrimitiveValue = Generalization(general=TracedPrimitiveValue, specific=umlTrace_Kernel_TracedBooleanValue)
gen_umlTrace_Kernel_TracedLiteralIntegerEvaluation_TracedLiteralEvaluation = Generalization(general=TracedLiteralEvaluation, specific=umlTrace_Kernel_TracedLiteralIntegerEvaluation)
gen_umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_TracedOpaqueBehaviorExecution = Generalization(general=TracedOpaqueBehaviorExecution, specific=umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution)
gen_umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_TracedOpaqueBehaviorExecution = Generalization(general=TracedOpaqueBehaviorExecution, specific=umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution)
gen_umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_TracedOpaqueBehaviorExecution = Generalization(general=TracedOpaqueBehaviorExecution, specific=umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution)

# Domain Model
domain_model = DomainModel(
    name="ecore",
    types={umlTrace_State, Values_ActionActivation_firing_Value, Values_SemanticVisitor_runtimeModelElement_Value, umlTrace_Trace, State, Traced_TracedObjects, umlTrace_Traced_TracedObjects, uml_TracedCombinedFragment, uml_TracedCreateLinkObjectAction, uml_TracedInitialNode, uml_TracedFlowFinalNode, uml_TracedExpansionRegion, uml_TracedSendObjectAction, uml_TracedPackageImport, uml_TracedClass, uml_TracedInteractionUse, uml_TracedGeneralizationSet, uml_TracedChangeEvent, uml_TracedDependency, uml_TracedPort, IntermediateActivities_TracedInitialNodeActivation, uml_TracedCollaborationUse, IntermediateActivities_TracedActivityExecution, uml_TracedCreateObjectAction, uml_TracedLifeline, IntermediateActivities_TracedForkNodeActivation, uml_TracedDurationConstraint, uml_TracedDestructionOccurrenceSpecification, uml_TracedConnector, uml_TracedExtend, IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution, uml_TracedExtension, uml_TracedStructuredActivityNode, uml_TracedExecutionEnvironment, uml_TracedIntervalConstraint, uml_TracedConsiderIgnoreFragment, uml_TracedContinuation, uml_TracedTimeConstraint, uml_TracedInputPin, uml_TracedValuePin, uml_TracedNode, uml_TracedExceptionHandler, uml_TracedSequenceNode, uml_TracedStartClassifierBehaviorAction, uml_TracedParameter, uml_TracedOpaqueExpression, uml_TracedLiteralString, BasicActions_TracedInputPinActivation, uml_TracedStateInvariant, IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution, uml_TracedInstanceSpecification, uml_TracedAcceptCallAction, uml_TracedClearVariableAction, uml_TracedConstraint, uml_TracedBroadcastSignalAction, uml_TracedInteraction, IntermediateActivities_TracedActivityNodeActivation, uml_TracedDestroyObjectAction, BasicActions_TracedCallBehaviorActionActivation, IntermediateActivities_TracedActivityParameterNodeActivation, uml_TracedActivityPartition, uml_TracedStateMachine, uml_TracedMessage, uml_TracedDeployment, uml_TracedStereotype, uml_TracedEnumerationLiteral, uml_TracedSubstitution, uml_TracedInformationFlow, uml_TracedAssociationClass, uml_TracedReclassifyObjectAction, uml_TracedUseCase, IntermediateActivities_TracedJoinNodeActivation, Kernel_TracedObject, Loci_TracedSemanticVisitor, uml_TracedTimeEvent, uml_TracedActivity, uml_TracedForkNode, Kernel_TracedReference, IntermediateActions_TracedAddStructuralFeatureValueActionActivation, uml_TracedGeneralization, uml_TracedInstanceValue, uml_TracedRemoveStructuralFeatureValueAction, uml_TracedInterval, Kernel_TracedIntegerValue, uml_TracedAnyReceiveEvent, uml_TracedReadStructuralFeatureAction, uml_TracedDataStoreNode, uml_TracedPartDecomposition, uml_TracedInterruptibleActivityRegion, uml_TracedProtocolTransition, uml_TracedInteractionOperand, uml_TracedDeploymentSpecification, uml_TracedUsage, uml_TracedActionInputPin, uml_TracedReadVariableAction, IntermediateActivities_TracedActivityFinalNodeActivation, uml_TracedDestroyLinkAction, uml_TracedLiteralInteger, uml_TracedProtocolStateMachine, uml_TracedReception, uml_TracedMessageOccurrenceSpecification, uml_TracedTemplateBinding, uml_TracedConnectionPointReference, uml_TracedRealization, uml_TracedReadLinkObjectEndQualifierAction, BasicActions_TracedOpaqueActionActivation, uml_TracedJoinNode, uml_TracedRedefinableTemplateSignature, uml_TracedModel, uml_TracedSignalEvent, Kernel_TracedBooleanValue, uml_TracedConditionalNode, uml_TracedExtensionPoint, uml_TracedSignal, uml_TracedExecutionOccurrenceSpecification, uml_TracedTimeInterval, uml_TracedInteractionConstraint, IntermediateActivities_TracedDecisionNodeActivation, uml_TracedCentralBufferNode, Kernel_TracedLiteralIntegerEvaluation, uml_TracedCreateLinkAction, uml_TracedPackage, uml_TracedCallEvent, uml_TracedLoopNode, uml_TracedComment, uml_TracedDataType, uml_TracedComponentRealization, uml_TracedInterface, uml_TracedOpaqueBehavior, uml_TracedProtocolConformance, uml_TracedObjectFlow, uml_TracedOperation, uml_TracedReadSelfAction, IntermediateActions_TracedReadStructuralFeatureActionActivation, uml_TracedDecisionNode, uml_TracedPackageMerge, uml_TracedAcceptEventAction, uml_TracedOccurrenceSpecification, uml_TracedParameterSet, uml_TracedTransition, uml_TracedDurationInterval, uml_TracedLinkEndData, uml_TracedConnectableElementTemplateParameter, uml_TracedOperationTemplateParameter, uml_TracedClause, uml_TracedReplyAction, uml_TracedTrigger, uml_TracedTemplateParameterSubstitution, uml_TracedDuration, uml_TracedReduceAction, uml_TracedFinalState, uml_TracedOpaqueAction, uml_TracedInformationItem, uml_TracedActionExecutionSpecification, uml_TracedOutputPin, uml_TracedImage, uml_TracedQualifierValue, uml_TracedAddStructuralFeatureValueAction, uml_TracedExpansionNode, uml_TracedActivityParameterNode, uml_TracedDevice, uml_TracedProperty, uml_TracedExtensionEnd, uml_TracedProfileApplication, uml_TracedCallOperationAction, uml_TracedArtifact, uml_TracedConnectorEnd, uml_TracedVariable, uml_TracedBehaviorExecutionSpecification, uml_TracedDurationObservation, uml_TracedLiteralUnlimitedNatural, uml_TracedTemplateSignature, BasicActions_TracedOutputPinActivation, uml_TracedReadExtentAction, uml_TracedCallBehaviorAction, uml_TracedReadLinkObjectEndAction, uml_TracedEnumeration, Kernel_TracedLiteralBooleanEvaluation, uml_TracedCommunicationPath, uml_TracedRaiseExceptionAction, uml_TracedReadLinkAction, uml_TracedLinkEndDestructionData, uml_TracedStringExpression, uml_TracedPrimitiveType, uml_TracedLiteralNull, uml_TracedState, uml_TracedRegion, uml_TracedInclude, uml_TracedLiteralBoolean, uml_TracedStartObjectBehaviorAction, IntermediateActions_TracedValueSpecificationActionActivation, uml_TracedAddVariableValueAction, uml_TracedClearStructuralFeatureAction, uml_TracedAssociation, uml_TracedExpression, uml_TracedLiteralReal, IntermediateActions_TracedCreateObjectActionActivation, uml_TracedCollaboration, uml_TracedTestIdentityAction, uml_TracedProfile, uml_TracedUnmarshallAction, uml_TracedSlot, uml_TracedInterfaceRealization, uml_TracedSendSignalAction, uml_TracedFunctionBehavior, uml_TracedValueSpecificationAction, uml_TracedRemoveVariableValueAction, uml_TracedActor, uml_TracedManifestation, uml_TracedReadIsClassifiedObjectAction, uml_TracedTemplateParameter, IntermediateActivities_TracedMergeNodeActivation, uml_TracedTimeExpression, uml_TracedAbstraction, uml_TracedClearAssociationAction, uml_TracedMergeNode, uml_TracedElementImport, IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution, uml_TracedPseudostate, uml_TracedLinkEndCreationData, uml_TracedGate, uml_TracedTimeObservation, uml_TracedControlFlow, uml_TracedGeneralOrdering, uml_TracedComponent, uml_TracedClassifierTemplateParameter, uml_TracedActivityFinalNode, umlTrace_uml_TracedRedefinableElement, umlTrace_uml_TracedNamespace, umlTrace_uml_TracedActivityGroup, uml_TracedNamedElement, umlTrace_uml_TracedCreateLinkObjectAction, TracedCreateLinkAction, umlTrace_uml_TracedCreateLinkAction, TracedWriteLinkAction, umlTrace_uml_TracedWriteLinkAction, TracedLinkAction, umlTrace_uml_TracedLinkAction, TracedAction, umlTrace_uml_TracedInitialNode, TracedControlNode, umlTrace_uml_TracedControlNode, umlTrace_uml_TracedFlowFinalNode, TracedFinalNode, umlTrace_uml_TracedFinalNode, umlTrace_uml_TracedExpansionRegion, umlTrace_uml_TracedCreateObjectAction, umlTrace_uml_TracedLifeline, umlTrace_uml_TracedDurationConstraint, TracedIntervalConstraint, umlTrace_uml_TracedIntervalConstraint, TracedConstraint, umlTrace_uml_TracedConstraint, TracedPackageableElement, umlTrace_uml_TracedCombinedFragment, TracedInteractionFragment, umlTrace_uml_TracedInteractionFragment, TracedNamedElement, umlTrace_uml_TracedNamedElement, TracedElement, umlTrace_uml_TracedElement, TracedEModelElement, umlTrace_uml_TracedConditionalNode, TracedStructuredActivityNode, umlTrace_uml_TracedStructuredActivityNode, uml_TracedAction, uml_TracedNamespace, uml_TracedActivityGroup, umlTrace_uml_TracedAction, TracedExecutableNode, umlTrace_uml_TracedExecutableNode, TracedActivityNode, umlTrace_uml_TracedActivityNode, uml_TracedRedefinableElement, ActivityContent, umlTrace_uml_TracedInvocationAction, umlTrace_uml_TracedOpaqueAction, umlTrace_uml_TracedProtocolConformance, TracedDirectedRelationship, umlTrace_uml_TracedDirectedRelationship, TracedRelationship, umlTrace_uml_TracedRelationship, umlTrace_uml_TracedCallBehaviorAction, TracedCallAction, umlTrace_uml_TracedCallAction, umlTrace_uml_TracedPackageImport, umlTrace_uml_TracedClass, uml_TracedEncapsulatedClassifier, uml_TracedBehavioredClassifier, umlTrace_uml_TracedEncapsulatedClassifier, TracedStructuredClassifier, umlTrace_uml_TracedStructuredClassifier, TracedClassifier, umlTrace_uml_TracedClassifier, uml_TracedType, umlTrace_uml_TracedType, umlTrace_uml_TracedBehavioredClassifier, umlTrace_uml_TracedActivityFinalNode, umlTrace_uml_TracedObservation, umlTrace_uml_TracedInteractionUse, umlTrace_uml_TracedLoopNode, umlTrace_uml_TracedSignal, umlTrace_uml_TracedPackageableElement, uml_TracedParameterableElement, umlTrace_uml_TracedParameterableElement, umlTrace_uml_TracedPseudostate, TracedVertex, umlTrace_uml_TracedVertex, umlTrace_uml_TracedDestructionOccurrenceSpecification, TracedMessageOccurrenceSpecification, umlTrace_uml_TracedMessageOccurrenceSpecification, uml_TracedMessageEnd, umlTrace_uml_TracedOccurrenceSpecification, umlTrace_uml_TracedMessageEnd, umlTrace_uml_TracedPackage, uml_TracedPackageableElement, uml_TracedTemplateableElement, umlTrace_uml_TracedTemplateableElement, umlTrace_uml_TracedConnector, TracedFeature, umlTrace_uml_TracedFeature, TracedRedefinableElement, umlTrace_uml_TracedSendObjectAction, TracedInvocationAction, umlTrace_uml_TracedInputPin, TracedPin, umlTrace_uml_TracedPin, uml_TracedObjectNode, umlTrace_uml_TracedObjectNode, uml_TracedActivityNode, umlTrace_uml_TracedDeploymentSpecification, TracedArtifact, umlTrace_uml_TracedArtifact, uml_TracedClassifier, uml_TracedDeployedArtifact, umlTrace_uml_TracedDeployedArtifact, umlTrace_uml_TracedTransition, umlTrace_uml_TracedNode, umlTrace_uml_TracedExceptionHandler, umlTrace_uml_TracedSequenceNode, umlTrace_uml_TracedUseCase, TracedBehavioredClassifier, umlTrace_uml_TracedStartClassifierBehaviorAction, umlTrace_uml_TracedExtend, umlTrace_uml_TracedRemoveStructuralFeatureValueAction, TracedWriteStructuralFeatureAction, umlTrace_uml_TracedWriteStructuralFeatureAction, TracedStructuralFeatureAction, umlTrace_uml_TracedStructuralFeatureAction, umlTrace_uml_TracedReadLinkAction, umlTrace_uml_TracedGeneralizationSet, umlTrace_uml_TracedChangeEvent, TracedEvent, umlTrace_uml_TracedEvent, umlTrace_uml_TracedDependency, uml_TracedDirectedRelationship, umlTrace_uml_TracedPort, TracedProperty, umlTrace_uml_TracedProperty, uml_TracedStructuralFeature, uml_TracedConnectableElement, uml_TracedDeploymentTarget, umlTrace_uml_TracedStructuralFeature, uml_TracedFeature, uml_TracedTypedElement, uml_TracedMultiplicityElement, umlTrace_uml_TracedTypedElement, umlTrace_uml_TracedMultiplicityElement, umlTrace_uml_TracedConnectableElement, umlTrace_uml_TracedDeploymentTarget, umlTrace_uml_TracedCollaborationUse, umlTrace_uml_TracedValuePin, TracedInputPin, umlTrace_uml_TracedBehavior, TracedClass, umlTrace_uml_TracedSlot, umlTrace_uml_TracedLiteralNull, umlTrace_uml_TracedParameter, umlTrace_uml_TracedOpaqueExpression, umlTrace_uml_TracedTrigger, umlTrace_uml_TracedStateInvariant, umlTrace_uml_TracedAssociationClass, umlTrace_uml_TracedInstanceSpecification, umlTrace_uml_TracedTemplateSignature, umlTrace_uml_TracedLinkEndDestructionData, TracedLinkEndData, umlTrace_uml_TracedLinkEndData, umlTrace_uml_TracedAcceptCallAction, TracedAcceptEventAction, umlTrace_uml_TracedAcceptEventAction, umlTrace_uml_TracedReduceAction, umlTrace_uml_TracedRaiseExceptionAction, umlTrace_uml_TracedStereotype, umlTrace_uml_TracedClearAssociationAction, umlTrace_uml_TracedEnumerationLiteral, TracedInstanceSpecification, umlTrace_uml_TracedSubstitution, TracedRealization, umlTrace_uml_TracedExtension, TracedAssociation, umlTrace_uml_TracedAssociation, uml_TracedRelationship, umlTrace_uml_TracedExecutionEnvironment, TracedNode, umlTrace_uml_TracedConsiderIgnoreFragment, TracedCombinedFragment, umlTrace_uml_TracedContinuation, umlTrace_uml_TracedCallOperationAction, umlTrace_uml_TracedTimeConstraint, umlTrace_uml_TracedClearVariableAction, TracedVariableAction, umlTrace_uml_TracedVariableAction, umlTrace_uml_TracedReadSelfAction, umlTrace_uml_TracedLiteralString, TracedLiteralSpecification, umlTrace_uml_TracedLiteralSpecification, TracedValueSpecification, umlTrace_uml_TracedValueSpecification, umlTrace_uml_TracedBroadcastSignalAction, umlTrace_uml_TracedInteraction, uml_TracedBehavior, uml_TracedInteractionFragment, umlTrace_uml_TracedActivityEdge, umlTrace_uml_TracedTestIdentityAction, umlTrace_uml_TracedInstanceValue, umlTrace_uml_TracedLiteralUnlimitedNatural, umlTrace_uml_TracedReclassifyObjectAction, umlTrace_uml_TracedTimeEvent, umlTrace_uml_TracedPartDecomposition, TracedInteractionUse, umlTrace_uml_TracedInterruptibleActivityRegion, umlTrace_uml_TracedAddVariableValueAction, TracedWriteVariableAction, umlTrace_uml_TracedWriteVariableAction, umlTrace_uml_TracedProtocolTransition, TracedTransition, umlTrace_uml_TracedImage, umlTrace_uml_TracedLiteralReal, umlTrace_uml_TracedInteractionOperand, umlTrace_uml_TracedGeneralization, umlTrace_uml_TracedInformationItem, umlTrace_uml_TracedModel, TracedPackage, umlTrace_uml_TracedClassifierTemplateParameter, TracedTemplateParameter, umlTrace_uml_TracedTemplateParameter, umlTrace_uml_TracedOperation, umlTrace_uml_TracedRealization, TracedAbstraction, umlTrace_uml_TracedAbstraction, TracedDependency, umlTrace_uml_TracedExecutionSpecification, umlTrace_uml_TracedReplyAction, umlTrace_uml_TracedActor, umlTrace_uml_TracedInformationFlow, umlTrace_uml_TracedDestroyObjectAction, umlTrace_uml_TracedActivityPartition, TracedActivityGroup, umlTrace_uml_TracedStateMachine, TracedBehavior, umlTrace_uml_TracedMessage, umlTrace_uml_TracedReadLinkObjectEndQualifierAction, umlTrace_uml_TracedDeployment, umlTrace_uml_TracedActivity, umlTrace_uml_TracedForkNode, umlTrace_uml_TracedProtocolStateMachine, TracedStateMachine, umlTrace_uml_TracedInterval, umlTrace_uml_TracedClearStructuralFeatureAction, umlTrace_uml_TracedObjectFlow, TracedActivityEdge, umlTrace_uml_TracedLiteralInteger, umlTrace_uml_TracedSignalEvent, umlTrace_uml_TracedReadLinkObjectEndAction, umlTrace_uml_TracedTimeInterval, TracedInterval, umlTrace_uml_TracedOperationTemplateParameter, umlTrace_uml_TracedDurationObservation, TracedObservation, umlTrace_uml_TracedConnectionPointReference, umlTrace_uml_TracedTimeExpression, umlTrace_uml_TracedQualifierValue, umlTrace_uml_TracedDurationInterval, umlTrace_uml_TracedFunctionBehavior, TracedOpaqueBehavior, umlTrace_uml_TracedOpaqueBehavior, umlTrace_uml_TracedInterfaceRealization, umlTrace_uml_TracedDevice, umlTrace_uml_TracedTemplateParameterSubstitution, umlTrace_uml_TracedJoinNode, umlTrace_uml_TracedRedefinableTemplateSignature, umlTrace_uml_TracedReadIsClassifiedObjectAction, umlTrace_uml_TracedTimeObservation, umlTrace_uml_TracedDecisionNode, umlTrace_uml_TracedElementImport, uml_TracedBehavioralFeature, umlTrace_uml_TracedBehavioralFeature, umlTrace_uml_TracedAnyReceiveEvent, TracedMessageEvent, umlTrace_uml_TracedMessageEvent, umlTrace_uml_TracedPrimitiveType, TracedDataType, umlTrace_uml_TracedDataType, umlTrace_uml_TracedReadStructuralFeatureAction, umlTrace_uml_TracedParameterSet, umlTrace_uml_TracedDataStoreNode, TracedCentralBufferNode, umlTrace_uml_TracedCentralBufferNode, TracedObjectNode, umlTrace_uml_TracedSendSignalAction, umlTrace_uml_TracedReception, TracedBehavioralFeature, umlTrace_uml_TracedTemplateBinding, umlTrace_uml_TracedUsage, umlTrace_uml_TracedActionInputPin, umlTrace_uml_TracedReadVariableAction, umlTrace_uml_TracedDestroyLinkAction, umlTrace_uml_TracedOutputPin, umlTrace_uml_TracedDuration, umlTrace_uml_TracedUnmarshallAction, umlTrace_uml_TracedProfile, umlTrace_uml_TracedExtensionEnd, umlTrace_uml_TracedExpansionNode, umlTrace_uml_TracedActivityParameterNode, umlTrace_uml_TracedProfileApplication, umlTrace_uml_TracedConnectorEnd, TracedMultiplicityElement, umlTrace_uml_TracedEnumeration, umlTrace_uml_TracedCollaboration, uml_TracedStructuredClassifier, umlTrace_uml_TracedVariable, umlTrace_uml_TracedValueSpecificationAction, umlTrace_uml_TracedReadExtentAction, umlTrace_uml_TracedStringExpression, umlTrace_uml_TracedExpression, umlTrace_uml_TracedGeneralOrdering, umlTrace_uml_TracedLiteralBoolean, umlTrace_uml_TracedStartObjectBehaviorAction, umlTrace_uml_TracedRegion, umlTrace_uml_TracedExtensionPoint, umlTrace_uml_TracedExecutionOccurrenceSpecification, TracedOccurrenceSpecification, umlTrace_uml_TracedInteractionConstraint, umlTrace_uml_TracedAddStructuralFeatureValueAction, umlTrace_uml_TracedInterface, umlTrace_uml_TracedComponent, umlTrace_uml_TracedCallEvent, umlTrace_uml_TracedComment, umlTrace_uml_TracedBehaviorExecutionSpecification, TracedExecutionSpecification, umlTrace_uml_TracedComponentRealization, umlTrace_uml_TracedCommunicationPath, umlTrace_uml_TracedPackageMerge, umlTrace_uml_TracedClause, umlTrace_uml_TracedFinalState, TracedState, umlTrace_uml_TracedState, uml_TracedVertex, umlTrace_uml_TracedConnectableElementTemplateParameter, umlTrace_uml_TracedActionExecutionSpecification, umlTrace_IntermediateActivities_TracedObjectNodeActivation, umlTrace_IntermediateActivities_TracedInitialNodeActivation, umlTrace_IntermediateActivities_TracedActivityExecution, TracedExecution, umlTrace_IntermediateActivities_TracedMergeNodeActivation, umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation, TracedObjectNodeActivation, umlTrace_IntermediateActivities_TracedJoinNodeActivation, umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation, umlTrace_IntermediateActivities_TracedDecisionNodeActivation, umlTrace_Loci_TracedSemanticVisitor, umlTrace_BasicActions_TracedPinActivation, umlTrace_BasicActions_TracedActionActivation, umlTrace_uml_TracedInclude, umlTrace_uml_TracedControlFlow, umlTrace_uml_TracedGate, TracedMessageEnd, umlTrace_uml_TracedRemoveVariableValueAction, umlTrace_uml_TracedManifestation, umlTrace_uml_TracedLinkEndCreationData, umlTrace_uml_TracedMergeNode, umlTrace_ecore_TracedEModelElement, umlTrace_IntermediateActivities_TracedForkNodeActivation, TracedControlNodeActivation, umlTrace_IntermediateActivities_TracedControlNodeActivation, TracedActivityNodeActivation, umlTrace_IntermediateActivities_TracedActivityNodeActivation, TracedSemanticVisitor, umlTrace_IntermediateActions_TracedCreateObjectActionActivation, umlTrace_BasicBehaviors_TracedExecution, TracedObject, umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution, umlTrace_Kernel_TracedObject, TracedExtensionalValue, umlTrace_Kernel_TracedExtensionalValue, TracedCompoundValue, umlTrace_Kernel_TracedCompoundValue, TracedStructuredValue, umlTrace_Kernel_TracedStructuredValue, TracedValue, umlTrace_Kernel_TracedValue, umlTrace_Kernel_TracedReference, umlTrace_Kernel_TracedLiteralEvaluation, TracedEvaluation, umlTrace_Kernel_TracedEvaluation, umlTrace_Kernel_TracedIntegerValue, TracedPrimitiveValue, umlTrace_BasicActions_TracedInvocationActionActivation, TracedActionActivation, umlTrace_BasicActions_TracedCallActionActivation, TracedInvocationActionActivation, umlTrace_BasicActions_TracedOpaqueActionActivation, umlTrace_BasicActions_TracedInputPinActivation, TracedPinActivation, umlTrace_BasicActions_TracedCallBehaviorActionActivation, TracedCallActionActivation, umlTrace_BasicActions_TracedOutputPinActivation, umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation, umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation, TracedStructuralFeatureActionActivation, umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation, TracedWriteStructuralFeatureActionActivation, umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation, umlTrace_IntermediateActions_TracedValueSpecificationActionActivation, umlTrace_Values_ActionActivation_firing_Value, BasicActions_TracedActionActivation, uml_ActivityContent, umlTrace_Kernel_TracedPrimitiveValue, umlTrace_Kernel_TracedLiteralBooleanEvaluation, TracedLiteralEvaluation, umlTrace_Kernel_TracedBooleanValue, umlTrace_Kernel_TracedLiteralIntegerEvaluation, umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution, TracedOpaqueBehaviorExecution, umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution, umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution, umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, uml_TracedElement},
    associations={actionActivation_firing_Values0, semanticVisitor_runtimeModelElement_Values1, statesTrace4, tracedObjects5, uml_tracedCombinedFragments7, uml_tracedCreateLinkObjectActions8, uml_tracedInitialNodes10, uml_tracedFlowFinalNodes12, uml_tracedConnectors26, uml_tracedSendObjectActions28, uml_tracedPackageImports30, uml_tracedClasss32, uml_tracedInteractionUses34, uml_tracedGeneralizationSets36, uml_tracedChangeEvents38, uml_tracedDependencys40, uml_tracedPorts42, intermediateActivities_tracedInitialNodeActivations44, uml_tracedCollaborationUses46, intermediateActivities_tracedActivityExecutions48, uml_tracedExpansionRegions14, uml_tracedCreateObjectActions16, uml_tracedLifelines18, intermediateActivities_tracedForkNodeActivations20, uml_tracedDurationConstraints22, uml_tracedDestructionOccurrenceSpecifications24, uml_tracedExtends60, integerFunctions_tracedIntegerPlusFunctionBehaviorExecutions62, uml_tracedExtensions64, uml_tracedStructuredActivityNodes66, uml_tracedExecutionEnvironments68, uml_tracedIntervalConstraints70, uml_tracedConsiderIgnoreFragments72, uml_tracedContinuations74, uml_tracedTimeConstraints76, uml_tracedInputPins78, uml_tracedValuePins50, uml_tracedNodes52, uml_tracedExceptionHandlers54, uml_tracedSequenceNodes56, uml_tracedStartClassifierBehaviorActions58, intermediateActivities_tracedActivityNodeActivations88, uml_tracedParameters90, uml_tracedOpaqueExpressions92, uml_tracedLiteralStrings94, basicActions_tracedInputPinActivations96, uml_tracedStateInvariants98, integerFunctions_tracedIntegerLessFunctionBehaviorExecutions100, uml_tracedInstanceSpecifications102, uml_tracedAcceptCallActions104, uml_tracedClearVariableActions80, uml_tracedConstraints82, uml_tracedBroadcastSignalActions84, uml_tracedInteractions86, uml_tracedAssociationClasss114, uml_tracedDestroyObjectActions116, basicActions_tracedCallBehaviorActionActivations118, intermediateActivities_tracedActivityParameterNodeActivations120, uml_tracedActivityPartitions122, uml_tracedStateMachines124, uml_tracedMessages126, uml_tracedDeployments128, uml_tracedStereotypes106, uml_tracedEnumerationLiterals108, uml_tracedSubstitutions110, uml_tracedInformationFlows112, uml_tracedReclassifyObjectActions140, uml_tracedUseCases142, intermediateActivities_tracedJoinNodeActivations144, kernel_tracedObjects146, loci_tracedSemanticVisitors148, uml_tracedTimeEvents150, uml_tracedActivitys130, uml_tracedForkNodes132, kernel_tracedReferences134, intermediateActions_tracedAddStructuralFeatureValueActionActivations136, uml_tracedGeneralizations160, uml_tracedInstanceValues138, uml_tracedRemoveStructuralFeatureValueActions162, uml_tracedIntervals164, kernel_tracedIntegerValues166, uml_tracedAnyReceiveEvents168, uml_tracedReadStructuralFeatureActions170, uml_tracedDataStoreNodes172, uml_tracedPartDecompositions152, uml_tracedInterruptibleActivityRegions154, uml_tracedProtocolTransitions156, uml_tracedInteractionOperands158, uml_tracedDeploymentSpecifications182, uml_tracedUsages184, uml_tracedActionInputPins186, uml_tracedReadVariableActions188, intermediateActivities_tracedActivityFinalNodeActivations190, uml_tracedDestroyLinkActions192, uml_tracedProtocolStateMachines174, uml_tracedReceptions176, uml_tracedMessageOccurrenceSpecifications178, uml_tracedTemplateBindings180, uml_tracedConnectionPointReferences202, uml_tracedRealizations204, uml_tracedReadLinkObjectEndQualifierActions206, basicActions_tracedOpaqueActionActivations208, uml_tracedJoinNodes210, uml_tracedRedefinableTemplateSignatures212, uml_tracedLiteralIntegers194, uml_tracedSignalEvents196, kernel_tracedBooleanValues198, uml_tracedConditionalNodes200, uml_tracedExtensionPoints222, uml_tracedSignals224, uml_tracedExecutionOccurrenceSpecifications226, uml_tracedTimeIntervals228, uml_tracedInteractionConstraints230, intermediateActivities_tracedDecisionNodeActivations232, uml_tracedModels214, uml_tracedCentralBufferNodes216, kernel_tracedLiteralIntegerEvaluations218, uml_tracedCreateLinkActions220, uml_tracedPackages240, uml_tracedCallEvents242, uml_tracedLoopNodes244, uml_tracedComments246, uml_tracedDataTypes248, uml_tracedComponentRealizations250, uml_tracedInterfaces234, uml_tracedOpaqueBehaviors236, uml_tracedProtocolConformances238, uml_tracedObjectFlows258, uml_tracedOperations260, uml_tracedReadSelfActions262, intermediateActions_tracedReadStructuralFeatureActionActivations264, uml_tracedDecisionNodes266, uml_tracedAcceptEventActions252, uml_tracedOccurrenceSpecifications254, uml_tracedParameterSets256, uml_tracedTransitions276, uml_tracedDurationIntervals278, uml_tracedLinkEndDatas280, uml_tracedConnectableElementTemplateParameters282, uml_tracedOperationTemplateParameters284, uml_tracedPackageMerges268, uml_tracedClauses270, uml_tracedReplyActions272, uml_tracedTriggers274, uml_tracedTemplateParameterSubstitutions292, uml_tracedDurations294, uml_tracedReduceActions296, uml_tracedFinalStates298, uml_tracedOpaqueActions300, uml_tracedInformationItems286, uml_tracedActionExecutionSpecifications288, uml_tracedOutputPins290, uml_tracedImages308, uml_tracedQualifierValues310, uml_tracedAddStructuralFeatureValueActions312, uml_tracedExpansionNodes314, uml_tracedDevices302, uml_tracedPropertys304, uml_tracedExtensionEnds306, uml_tracedProfileApplications322, uml_tracedCallOperationActions324, uml_tracedArtifacts326, uml_tracedConnectorEnds328, uml_tracedVariables330, uml_tracedActivityParameterNodes316, uml_tracedBehaviorExecutionSpecifications318, uml_tracedDurationObservations320, uml_tracedLiteralUnlimitedNaturals338, uml_tracedTemplateSignatures340, basicActions_tracedOutputPinActivations342, uml_tracedReadExtentActions344, uml_tracedCallBehaviorActions332, uml_tracedReadLinkObjectEndActions334, uml_tracedEnumerations336, kernel_tracedLiteralBooleanEvaluations352, uml_tracedCommunicationPaths354, uml_tracedRaiseExceptionActions356, uml_tracedReadLinkActions358, uml_tracedLinkEndDestructionDatas346, uml_tracedStringExpressions348, uml_tracedPrimitiveTypes350, uml_tracedLiteralNulls366, uml_tracedStates368, uml_tracedRegions370, uml_tracedIncludes372, uml_tracedLiteralBooleans360, uml_tracedStartObjectBehaviorActions362, intermediateActions_tracedValueSpecificationActionActivations364, uml_tracedAddVariableValueActions376, uml_tracedClearStructuralFeatureActions378, uml_tracedAssociations380, uml_tracedExpressions382, uml_tracedLiteralReals374, intermediateActions_tracedCreateObjectActionActivations388, uml_tracedCollaborations390, uml_tracedTestIdentityActions392, uml_tracedProfiles394, uml_tracedUnmarshallActions384, uml_tracedSlots386, uml_tracedInterfaceRealizations402, uml_tracedSendSignalActions404, uml_tracedFunctionBehaviors406, uml_tracedRemoveVariableValueActions396, uml_tracedActors398, uml_tracedManifestations400, uml_tracedReadIsClassifiedObjectActions414, uml_tracedTemplateParameters416, intermediateActivities_tracedMergeNodeActivations418, uml_tracedValueSpecificationActions408, uml_tracedTimeExpressions410, uml_tracedAbstractions412, uml_tracedClearAssociationActions426, uml_tracedMergeNodes428, uml_tracedElementImports430, integerFunctions_tracedIntegerGreaterFunctionBehaviorExecutions420, uml_tracedPseudostates422, uml_tracedLinkEndCreationDatas424, uml_tracedGates438, uml_tracedTimeObservations440, uml_tracedControlFlows442, uml_tracedGeneralOrderings444, uml_tracedComponents432, uml_tracedClassifierTemplateParameters434, uml_tracedActivityFinalNodes436, runtimeModelElementTrace446, firingTrace449, parent453, states456, states459, parent462, runtimeModelElement452},
    generalizations={gen_umlTrace_uml_TracedRedefinableElement_TracedNamedElement, gen_umlTrace_uml_TracedNamespace_TracedNamedElement, gen_umlTrace_uml_TracedActivityGroup_uml_TracedNamedElement, gen_umlTrace_uml_TracedActivityGroup_ActivityContent, gen_umlTrace_uml_TracedCreateLinkObjectAction_TracedCreateLinkAction, gen_umlTrace_uml_TracedCreateLinkAction_TracedWriteLinkAction, gen_umlTrace_uml_TracedWriteLinkAction_TracedLinkAction, gen_umlTrace_uml_TracedLinkAction_TracedAction, gen_umlTrace_uml_TracedInitialNode_TracedControlNode, gen_umlTrace_uml_TracedControlNode_TracedActivityNode, gen_umlTrace_uml_TracedFlowFinalNode_TracedFinalNode, gen_umlTrace_uml_TracedFinalNode_TracedControlNode, gen_umlTrace_uml_TracedExpansionRegion_TracedStructuredActivityNode, gen_umlTrace_uml_TracedCreateObjectAction_TracedAction, gen_umlTrace_uml_TracedLifeline_TracedNamedElement, gen_umlTrace_uml_TracedDurationConstraint_TracedIntervalConstraint, gen_umlTrace_uml_TracedIntervalConstraint_TracedConstraint, gen_umlTrace_uml_TracedCombinedFragment_TracedInteractionFragment, gen_umlTrace_uml_TracedInteractionFragment_TracedNamedElement, gen_umlTrace_uml_TracedNamedElement_TracedElement, gen_umlTrace_uml_TracedElement_TracedEModelElement, gen_umlTrace_uml_TracedConditionalNode_TracedStructuredActivityNode, gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedAction, gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedNamespace, gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedActivityGroup, gen_umlTrace_uml_TracedAction_TracedExecutableNode, gen_umlTrace_uml_TracedExecutableNode_TracedActivityNode, gen_umlTrace_uml_TracedActivityNode_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedActivityNode_ActivityContent, gen_umlTrace_uml_TracedInvocationAction_TracedAction, gen_umlTrace_uml_TracedOpaqueAction_TracedAction, gen_umlTrace_uml_TracedProtocolConformance_TracedDirectedRelationship, gen_umlTrace_uml_TracedDirectedRelationship_TracedRelationship, gen_umlTrace_uml_TracedRelationship_TracedElement, gen_umlTrace_uml_TracedCallBehaviorAction_TracedCallAction, gen_umlTrace_uml_TracedCallAction_TracedInvocationAction, gen_umlTrace_uml_TracedPackageImport_TracedDirectedRelationship, gen_umlTrace_uml_TracedClass_uml_TracedEncapsulatedClassifier, gen_umlTrace_uml_TracedClass_uml_TracedBehavioredClassifier, gen_umlTrace_uml_TracedEncapsulatedClassifier_TracedStructuredClassifier, gen_umlTrace_uml_TracedStructuredClassifier_TracedClassifier, gen_umlTrace_uml_TracedClassifier_uml_TracedNamespace, gen_umlTrace_uml_TracedClassifier_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedClassifier_uml_TracedType, gen_umlTrace_uml_TracedClassifier_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedType_TracedPackageableElement, gen_umlTrace_uml_TracedBehavioredClassifier_TracedClassifier, gen_umlTrace_uml_TracedActivityFinalNode_TracedFinalNode, gen_umlTrace_uml_TracedObservation_TracedPackageableElement, gen_umlTrace_uml_TracedInteractionUse_TracedInteractionFragment, gen_umlTrace_uml_TracedLoopNode_TracedStructuredActivityNode, gen_umlTrace_uml_TracedConstraint_TracedPackageableElement, gen_umlTrace_uml_TracedPackageableElement_uml_TracedNamedElement, gen_umlTrace_uml_TracedPackageableElement_uml_TracedParameterableElement, gen_umlTrace_uml_TracedParameterableElement_TracedElement, gen_umlTrace_uml_TracedPseudostate_TracedVertex, gen_umlTrace_uml_TracedVertex_TracedNamedElement, gen_umlTrace_uml_TracedDestructionOccurrenceSpecification_TracedMessageOccurrenceSpecification, gen_umlTrace_uml_TracedMessageOccurrenceSpecification_uml_TracedOccurrenceSpecification, gen_umlTrace_uml_TracedMessageOccurrenceSpecification_uml_TracedMessageEnd, gen_umlTrace_uml_TracedOccurrenceSpecification_TracedInteractionFragment, gen_umlTrace_uml_TracedMessageEnd_TracedNamedElement, gen_umlTrace_uml_TracedPackage_uml_TracedNamespace, gen_umlTrace_uml_TracedPackage_uml_TracedPackageableElement, gen_umlTrace_uml_TracedPackage_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedTemplateableElement_TracedElement, gen_umlTrace_uml_TracedConnector_TracedFeature, gen_umlTrace_uml_TracedFeature_TracedRedefinableElement, gen_umlTrace_uml_TracedSendObjectAction_TracedInvocationAction, gen_umlTrace_uml_TracedInputPin_TracedPin, gen_umlTrace_uml_TracedPin_uml_TracedObjectNode, gen_umlTrace_uml_TracedPin_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedObjectNode_uml_TracedActivityNode, gen_umlTrace_uml_TracedObjectNode_uml_TracedTypedElement, gen_umlTrace_uml_TracedDeploymentSpecification_TracedArtifact, gen_umlTrace_uml_TracedArtifact_uml_TracedClassifier, gen_umlTrace_uml_TracedArtifact_uml_TracedDeployedArtifact, gen_umlTrace_uml_TracedDeployedArtifact_TracedNamedElement, gen_umlTrace_uml_TracedTransition_uml_TracedNamespace, gen_umlTrace_uml_TracedTransition_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedNode_uml_TracedClass, gen_umlTrace_uml_TracedNode_uml_TracedDeploymentTarget, gen_umlTrace_uml_TracedExceptionHandler_TracedElement, gen_umlTrace_uml_TracedSequenceNode_TracedStructuredActivityNode, gen_umlTrace_uml_TracedUseCase_TracedBehavioredClassifier, gen_umlTrace_uml_TracedStartClassifierBehaviorAction_TracedAction, gen_umlTrace_uml_TracedExtend_uml_TracedNamedElement, gen_umlTrace_uml_TracedExtend_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedRemoveStructuralFeatureValueAction_TracedWriteStructuralFeatureAction, gen_umlTrace_uml_TracedWriteStructuralFeatureAction_TracedStructuralFeatureAction, gen_umlTrace_uml_TracedStructuralFeatureAction_TracedAction, gen_umlTrace_uml_TracedSignal_TracedClassifier, gen_umlTrace_uml_TracedGeneralizationSet_TracedPackageableElement, gen_umlTrace_uml_TracedChangeEvent_TracedEvent, gen_umlTrace_uml_TracedEvent_TracedPackageableElement, gen_umlTrace_uml_TracedDependency_uml_TracedPackageableElement, gen_umlTrace_uml_TracedDependency_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedPort_TracedProperty, gen_umlTrace_uml_TracedProperty_uml_TracedStructuralFeature, gen_umlTrace_uml_TracedProperty_uml_TracedConnectableElement, gen_umlTrace_uml_TracedProperty_uml_TracedDeploymentTarget, gen_umlTrace_uml_TracedStructuralFeature_uml_TracedFeature, gen_umlTrace_uml_TracedStructuralFeature_uml_TracedTypedElement, gen_umlTrace_uml_TracedStructuralFeature_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedTypedElement_TracedNamedElement, gen_umlTrace_uml_TracedMultiplicityElement_TracedElement, gen_umlTrace_uml_TracedConnectableElement_uml_TracedTypedElement, gen_umlTrace_uml_TracedConnectableElement_uml_TracedParameterableElement, gen_umlTrace_uml_TracedDeploymentTarget_TracedNamedElement, gen_umlTrace_uml_TracedCollaborationUse_TracedNamedElement, gen_umlTrace_uml_TracedValuePin_TracedInputPin, gen_umlTrace_uml_TracedBehavior_TracedClass, gen_umlTrace_uml_TracedSlot_TracedElement, gen_umlTrace_uml_TracedLiteralNull_TracedLiteralSpecification, gen_umlTrace_uml_TracedParameter_uml_TracedConnectableElement, gen_umlTrace_uml_TracedParameter_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedOpaqueExpression_TracedValueSpecification, gen_umlTrace_uml_TracedTrigger_TracedNamedElement, gen_umlTrace_uml_TracedStateInvariant_TracedInteractionFragment, gen_umlTrace_uml_TracedAssociationClass_uml_TracedClass, gen_umlTrace_uml_TracedAssociationClass_uml_TracedAssociation, gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedDeploymentTarget, gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedPackageableElement, gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedDeployedArtifact, gen_umlTrace_uml_TracedTemplateSignature_TracedElement, gen_umlTrace_uml_TracedLinkEndDestructionData_TracedLinkEndData, gen_umlTrace_uml_TracedLinkEndData_TracedElement, gen_umlTrace_uml_TracedAcceptCallAction_TracedAcceptEventAction, gen_umlTrace_uml_TracedAcceptEventAction_TracedAction, gen_umlTrace_uml_TracedReduceAction_TracedAction, gen_umlTrace_uml_TracedRaiseExceptionAction_TracedAction, gen_umlTrace_uml_TracedStereotype_TracedClass, gen_umlTrace_uml_TracedClearAssociationAction_TracedAction, gen_umlTrace_uml_TracedEnumerationLiteral_TracedInstanceSpecification, gen_umlTrace_uml_TracedSubstitution_TracedRealization, gen_umlTrace_uml_TracedReadLinkAction_TracedLinkAction, gen_umlTrace_uml_TracedExtension_TracedAssociation, gen_umlTrace_uml_TracedAssociation_uml_TracedClassifier, gen_umlTrace_uml_TracedAssociation_uml_TracedRelationship, gen_umlTrace_uml_TracedExecutionEnvironment_TracedNode, gen_umlTrace_uml_TracedConsiderIgnoreFragment_TracedCombinedFragment, gen_umlTrace_uml_TracedContinuation_TracedInteractionFragment, gen_umlTrace_uml_TracedCallOperationAction_TracedCallAction, gen_umlTrace_uml_TracedTimeConstraint_TracedIntervalConstraint, gen_umlTrace_uml_TracedClearVariableAction_TracedVariableAction, gen_umlTrace_uml_TracedVariableAction_TracedAction, gen_umlTrace_uml_TracedReadSelfAction_TracedAction, gen_umlTrace_uml_TracedLiteralString_TracedLiteralSpecification, gen_umlTrace_uml_TracedLiteralSpecification_TracedValueSpecification, gen_umlTrace_uml_TracedValueSpecification_uml_TracedPackageableElement, gen_umlTrace_uml_TracedValueSpecification_uml_TracedTypedElement, gen_umlTrace_uml_TracedBroadcastSignalAction_TracedInvocationAction, gen_umlTrace_uml_TracedInteraction_uml_TracedBehavior, gen_umlTrace_uml_TracedInteraction_uml_TracedInteractionFragment, gen_umlTrace_uml_TracedActivityEdge_TracedRedefinableElement, gen_umlTrace_uml_TracedTestIdentityAction_TracedAction, gen_umlTrace_uml_TracedInstanceValue_TracedValueSpecification, gen_umlTrace_uml_TracedLiteralUnlimitedNatural_TracedLiteralSpecification, gen_umlTrace_uml_TracedReclassifyObjectAction_TracedAction, gen_umlTrace_uml_TracedTimeEvent_TracedEvent, gen_umlTrace_uml_TracedPartDecomposition_TracedInteractionUse, gen_umlTrace_uml_TracedInterruptibleActivityRegion_TracedActivityGroup, gen_umlTrace_uml_TracedAddVariableValueAction_TracedWriteVariableAction, gen_umlTrace_uml_TracedWriteVariableAction_TracedVariableAction, gen_umlTrace_uml_TracedProtocolTransition_TracedTransition, gen_umlTrace_uml_TracedImage_TracedElement, gen_umlTrace_uml_TracedLiteralReal_TracedLiteralSpecification, gen_umlTrace_uml_TracedInteractionOperand_uml_TracedNamespace, gen_umlTrace_uml_TracedInteractionOperand_uml_TracedInteractionFragment, gen_umlTrace_uml_TracedGeneralization_TracedDirectedRelationship, gen_umlTrace_uml_TracedInformationItem_TracedClassifier, gen_umlTrace_uml_TracedModel_TracedPackage, gen_umlTrace_uml_TracedClassifierTemplateParameter_TracedTemplateParameter, gen_umlTrace_uml_TracedTemplateParameter_TracedElement, gen_umlTrace_uml_TracedRealization_TracedAbstraction, gen_umlTrace_uml_TracedAbstraction_TracedDependency, gen_umlTrace_uml_TracedExecutionSpecification_TracedInteractionFragment, gen_umlTrace_uml_TracedReplyAction_TracedAction, gen_umlTrace_uml_TracedActor_TracedBehavioredClassifier, gen_umlTrace_uml_TracedInformationFlow_uml_TracedPackageableElement, gen_umlTrace_uml_TracedInformationFlow_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedDestroyObjectAction_TracedAction, gen_umlTrace_uml_TracedActivityPartition_TracedActivityGroup, gen_umlTrace_uml_TracedStateMachine_TracedBehavior, gen_umlTrace_uml_TracedMessage_TracedNamedElement, gen_umlTrace_uml_TracedReadLinkObjectEndQualifierAction_TracedAction, gen_umlTrace_uml_TracedDeployment_TracedDependency, gen_umlTrace_uml_TracedActivity_TracedBehavior, gen_umlTrace_uml_TracedForkNode_TracedControlNode, gen_umlTrace_uml_TracedProtocolStateMachine_TracedStateMachine, gen_umlTrace_uml_TracedInterval_TracedValueSpecification, gen_umlTrace_uml_TracedClearStructuralFeatureAction_TracedStructuralFeatureAction, gen_umlTrace_uml_TracedObjectFlow_TracedActivityEdge, gen_umlTrace_uml_TracedLiteralInteger_TracedLiteralSpecification, gen_umlTrace_uml_TracedSignalEvent_TracedMessageEvent, gen_umlTrace_uml_TracedReadLinkObjectEndAction_TracedAction, gen_umlTrace_uml_TracedTimeInterval_TracedInterval, gen_umlTrace_uml_TracedOperationTemplateParameter_TracedTemplateParameter, gen_umlTrace_uml_TracedDurationObservation_TracedObservation, gen_umlTrace_uml_TracedConnectionPointReference_TracedVertex, gen_umlTrace_uml_TracedTimeExpression_TracedValueSpecification, gen_umlTrace_uml_TracedQualifierValue_TracedElement, gen_umlTrace_uml_TracedDurationInterval_TracedInterval, gen_umlTrace_uml_TracedFunctionBehavior_TracedOpaqueBehavior, gen_umlTrace_uml_TracedOpaqueBehavior_TracedBehavior, gen_umlTrace_uml_TracedInterfaceRealization_TracedRealization, gen_umlTrace_uml_TracedDevice_TracedNode, gen_umlTrace_uml_TracedTemplateParameterSubstitution_TracedElement, gen_umlTrace_uml_TracedJoinNode_TracedControlNode, gen_umlTrace_uml_TracedRedefinableTemplateSignature_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedRedefinableTemplateSignature_uml_TracedTemplateSignature, gen_umlTrace_uml_TracedReadIsClassifiedObjectAction_TracedAction, gen_umlTrace_uml_TracedTimeObservation_TracedObservation, gen_umlTrace_uml_TracedDecisionNode_TracedControlNode, gen_umlTrace_uml_TracedElementImport_TracedDirectedRelationship, gen_umlTrace_uml_TracedOperation_uml_TracedBehavioralFeature, gen_umlTrace_uml_TracedOperation_uml_TracedParameterableElement, gen_umlTrace_uml_TracedOperation_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedBehavioralFeature_uml_TracedNamespace, gen_umlTrace_uml_TracedBehavioralFeature_uml_TracedFeature, gen_umlTrace_uml_TracedAnyReceiveEvent_TracedMessageEvent, gen_umlTrace_uml_TracedMessageEvent_TracedEvent, gen_umlTrace_uml_TracedPrimitiveType_TracedDataType, gen_umlTrace_uml_TracedDataType_TracedClassifier, gen_umlTrace_uml_TracedReadStructuralFeatureAction_TracedStructuralFeatureAction, gen_umlTrace_uml_TracedParameterSet_TracedNamedElement, gen_umlTrace_uml_TracedDataStoreNode_TracedCentralBufferNode, gen_umlTrace_uml_TracedCentralBufferNode_TracedObjectNode, gen_umlTrace_uml_TracedSendSignalAction_TracedInvocationAction, gen_umlTrace_uml_TracedReception_TracedBehavioralFeature, gen_umlTrace_uml_TracedTemplateBinding_TracedDirectedRelationship, gen_umlTrace_uml_TracedUsage_TracedDependency, gen_umlTrace_uml_TracedActionInputPin_TracedInputPin, gen_umlTrace_uml_TracedReadVariableAction_TracedVariableAction, gen_umlTrace_uml_TracedDestroyLinkAction_TracedWriteLinkAction, gen_umlTrace_uml_TracedOutputPin_TracedPin, gen_umlTrace_uml_TracedDuration_TracedValueSpecification, gen_umlTrace_uml_TracedUnmarshallAction_TracedAction, gen_umlTrace_uml_TracedProfile_TracedPackage, gen_umlTrace_uml_TracedExtensionEnd_TracedProperty, gen_umlTrace_uml_TracedExpansionNode_TracedObjectNode, gen_umlTrace_uml_TracedActivityParameterNode_TracedObjectNode, gen_umlTrace_uml_TracedProfileApplication_TracedDirectedRelationship, gen_umlTrace_uml_TracedConnectorEnd_TracedMultiplicityElement, gen_umlTrace_uml_TracedEnumeration_TracedDataType, gen_umlTrace_uml_TracedCollaboration_uml_TracedStructuredClassifier, gen_umlTrace_uml_TracedCollaboration_uml_TracedBehavioredClassifier, gen_umlTrace_uml_TracedVariable_uml_TracedConnectableElement, gen_umlTrace_uml_TracedVariable_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedValueSpecificationAction_TracedAction, gen_umlTrace_uml_TracedReadExtentAction_TracedAction, gen_umlTrace_uml_TracedStringExpression_uml_TracedExpression, gen_umlTrace_uml_TracedStringExpression_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedExpression_TracedValueSpecification, gen_umlTrace_uml_TracedGeneralOrdering_TracedNamedElement, gen_umlTrace_uml_TracedLiteralBoolean_TracedLiteralSpecification, gen_umlTrace_uml_TracedStartObjectBehaviorAction_TracedCallAction, gen_umlTrace_uml_TracedRegion_uml_TracedNamespace, gen_umlTrace_uml_TracedRegion_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedExtensionPoint_TracedRedefinableElement, gen_umlTrace_uml_TracedExecutionOccurrenceSpecification_TracedOccurrenceSpecification, gen_umlTrace_uml_TracedInteractionConstraint_TracedConstraint, gen_umlTrace_uml_TracedAddStructuralFeatureValueAction_TracedWriteStructuralFeatureAction, gen_umlTrace_uml_TracedInterface_TracedClassifier, gen_umlTrace_uml_TracedComponent_TracedClass, gen_umlTrace_uml_TracedCallEvent_TracedMessageEvent, gen_umlTrace_uml_TracedComment_TracedElement, gen_umlTrace_uml_TracedBehaviorExecutionSpecification_TracedExecutionSpecification, gen_umlTrace_uml_TracedComponentRealization_TracedRealization, gen_umlTrace_uml_TracedCommunicationPath_TracedAssociation, gen_umlTrace_uml_TracedPackageMerge_TracedDirectedRelationship, gen_umlTrace_uml_TracedClause_TracedElement, gen_umlTrace_uml_TracedFinalState_TracedState, gen_umlTrace_uml_TracedState_uml_TracedNamespace, gen_umlTrace_uml_TracedState_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedState_uml_TracedVertex, gen_umlTrace_uml_TracedConnectableElementTemplateParameter_TracedTemplateParameter, gen_umlTrace_uml_TracedActionExecutionSpecification_TracedExecutionSpecification, gen_umlTrace_IntermediateActivities_TracedObjectNodeActivation_TracedActivityNodeActivation, gen_umlTrace_IntermediateActivities_TracedInitialNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedActivityExecution_TracedExecution, gen_umlTrace_IntermediateActivities_TracedMergeNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation_TracedObjectNodeActivation, gen_umlTrace_IntermediateActivities_TracedJoinNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedDecisionNodeActivation_TracedControlNodeActivation, gen_umlTrace_BasicActions_TracedPinActivation_TracedObjectNodeActivation, gen_umlTrace_BasicActions_TracedActionActivation_TracedActivityNodeActivation, gen_umlTrace_uml_TracedInclude_uml_TracedNamedElement, gen_umlTrace_uml_TracedInclude_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedControlFlow_TracedActivityEdge, gen_umlTrace_uml_TracedGate_TracedMessageEnd, gen_umlTrace_uml_TracedRemoveVariableValueAction_TracedWriteVariableAction, gen_umlTrace_uml_TracedManifestation_TracedAbstraction, gen_umlTrace_uml_TracedLinkEndCreationData_TracedLinkEndData, gen_umlTrace_uml_TracedMergeNode_TracedControlNode, gen_umlTrace_IntermediateActivities_TracedForkNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedControlNodeActivation_TracedActivityNodeActivation, gen_umlTrace_IntermediateActivities_TracedActivityNodeActivation_TracedSemanticVisitor, gen_umlTrace_IntermediateActions_TracedCreateObjectActionActivation_TracedActionActivation, gen_umlTrace_BasicBehaviors_TracedExecution_TracedObject, gen_umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution_TracedExecution, gen_umlTrace_Kernel_TracedObject_TracedExtensionalValue, gen_umlTrace_Kernel_TracedExtensionalValue_TracedCompoundValue, gen_umlTrace_Kernel_TracedCompoundValue_TracedStructuredValue, gen_umlTrace_Kernel_TracedStructuredValue_TracedValue, gen_umlTrace_Kernel_TracedValue_TracedSemanticVisitor, gen_umlTrace_Kernel_TracedReference_TracedStructuredValue, gen_umlTrace_Kernel_TracedLiteralEvaluation_TracedEvaluation, gen_umlTrace_Kernel_TracedEvaluation_TracedSemanticVisitor, gen_umlTrace_BasicActions_TracedInvocationActionActivation_TracedActionActivation, gen_umlTrace_BasicActions_TracedCallActionActivation_TracedInvocationActionActivation, gen_umlTrace_BasicActions_TracedOpaqueActionActivation_TracedActionActivation, gen_umlTrace_BasicActions_TracedInputPinActivation_TracedPinActivation, gen_umlTrace_BasicActions_TracedCallBehaviorActionActivation_TracedCallActionActivation, gen_umlTrace_BasicActions_TracedOutputPinActivation_TracedPinActivation, gen_umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation_TracedActionActivation, gen_umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation, gen_umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation_TracedWriteStructuralFeatureActionActivation, gen_umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation, gen_umlTrace_IntermediateActions_TracedValueSpecificationActionActivation_TracedActionActivation, gen_umlTrace_Kernel_TracedIntegerValue_TracedPrimitiveValue, gen_umlTrace_Kernel_TracedPrimitiveValue_TracedValue, gen_umlTrace_Kernel_TracedLiteralBooleanEvaluation_TracedLiteralEvaluation, gen_umlTrace_Kernel_TracedBooleanValue_TracedPrimitiveValue, gen_umlTrace_Kernel_TracedLiteralIntegerEvaluation_TracedLiteralEvaluation, gen_umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_TracedOpaqueBehaviorExecution, gen_umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_TracedOpaqueBehaviorExecution, gen_umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_TracedOpaqueBehaviorExecution},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)