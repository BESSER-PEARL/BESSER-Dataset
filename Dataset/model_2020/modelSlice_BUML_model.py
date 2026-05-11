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
umlTrace_State = Class(name="umlTrace_State")
Values_ActionActivation_firing_Value = Class(name="Values_ActionActivation_firing_Value")
Values_SemanticVisitor_runtimeModelElement_Value = Class(name="Values_SemanticVisitor_runtimeModelElement_Value")
umlTrace_Trace = Class(name="umlTrace_Trace")
State = Class(name="State")
Traced_TracedObjects = Class(name="Traced_TracedObjects")
umlTrace_Traced_TracedObjects = Class(name="umlTrace_Traced_TracedObjects")
uml_TracedCombinedFragment = Class(name="uml_TracedCombinedFragment")
uml_TracedCreateLinkObjectAction = Class(name="uml_TracedCreateLinkObjectAction")
uml_TracedInitialNode = Class(name="uml_TracedInitialNode")
uml_TracedFlowFinalNode = Class(name="uml_TracedFlowFinalNode")
uml_TracedExpansionRegion = Class(name="uml_TracedExpansionRegion")
uml_TracedCreateObjectAction = Class(name="uml_TracedCreateObjectAction")
uml_TracedLifeline = Class(name="uml_TracedLifeline")
IntermediateActivities_TracedForkNodeActivation = Class(name="IntermediateActivities_TracedForkNodeActivation")
uml_TracedDurationConstraint = Class(name="uml_TracedDurationConstraint")
uml_TracedDestructionOccurrenceSpecification = Class(name="uml_TracedDestructionOccurrenceSpecification")
uml_TracedConnector = Class(name="uml_TracedConnector")
uml_TracedSendObjectAction = Class(name="uml_TracedSendObjectAction")
uml_TracedPackageImport = Class(name="uml_TracedPackageImport")
uml_TracedClass = Class(name="uml_TracedClass")
uml_TracedInteractionUse = Class(name="uml_TracedInteractionUse")
uml_TracedGeneralizationSet = Class(name="uml_TracedGeneralizationSet")
uml_TracedChangeEvent = Class(name="uml_TracedChangeEvent")
uml_TracedDependency = Class(name="uml_TracedDependency")
uml_TracedPort = Class(name="uml_TracedPort")
IntermediateActivities_TracedInitialNodeActivation = Class(name="IntermediateActivities_TracedInitialNodeActivation")
uml_TracedCollaborationUse = Class(name="uml_TracedCollaborationUse")
IntermediateActivities_TracedActivityExecution = Class(name="IntermediateActivities_TracedActivityExecution")
uml_TracedValuePin = Class(name="uml_TracedValuePin")
uml_TracedNode = Class(name="uml_TracedNode")
uml_TracedExceptionHandler = Class(name="uml_TracedExceptionHandler")
uml_TracedSequenceNode = Class(name="uml_TracedSequenceNode")
uml_TracedStartClassifierBehaviorAction = Class(name="uml_TracedStartClassifierBehaviorAction")
uml_TracedExtend = Class(name="uml_TracedExtend")
IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution = Class(name="IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution")
uml_TracedExtension = Class(name="uml_TracedExtension")
uml_TracedStructuredActivityNode = Class(name="uml_TracedStructuredActivityNode")
uml_TracedExecutionEnvironment = Class(name="uml_TracedExecutionEnvironment")
uml_TracedIntervalConstraint = Class(name="uml_TracedIntervalConstraint")
uml_TracedConsiderIgnoreFragment = Class(name="uml_TracedConsiderIgnoreFragment")
uml_TracedContinuation = Class(name="uml_TracedContinuation")
uml_TracedTimeConstraint = Class(name="uml_TracedTimeConstraint")
uml_TracedInputPin = Class(name="uml_TracedInputPin")
uml_TracedClearVariableAction = Class(name="uml_TracedClearVariableAction")
uml_TracedConstraint = Class(name="uml_TracedConstraint")
uml_TracedBroadcastSignalAction = Class(name="uml_TracedBroadcastSignalAction")
uml_TracedInteraction = Class(name="uml_TracedInteraction")
IntermediateActivities_TracedActivityNodeActivation = Class(name="IntermediateActivities_TracedActivityNodeActivation")
uml_TracedParameter = Class(name="uml_TracedParameter")
uml_TracedOpaqueExpression = Class(name="uml_TracedOpaqueExpression")
uml_TracedLiteralString = Class(name="uml_TracedLiteralString")
BasicActions_TracedInputPinActivation = Class(name="BasicActions_TracedInputPinActivation")
uml_TracedStateInvariant = Class(name="uml_TracedStateInvariant")
IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution = Class(name="IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution")
uml_TracedInstanceSpecification = Class(name="uml_TracedInstanceSpecification")
uml_TracedAcceptCallAction = Class(name="uml_TracedAcceptCallAction")
uml_TracedStereotype = Class(name="uml_TracedStereotype")
uml_TracedEnumerationLiteral = Class(name="uml_TracedEnumerationLiteral")
uml_TracedSubstitution = Class(name="uml_TracedSubstitution")
uml_TracedInformationFlow = Class(name="uml_TracedInformationFlow")
uml_TracedAssociationClass = Class(name="uml_TracedAssociationClass")
uml_TracedDestroyObjectAction = Class(name="uml_TracedDestroyObjectAction")
BasicActions_TracedCallBehaviorActionActivation = Class(name="BasicActions_TracedCallBehaviorActionActivation")
IntermediateActivities_TracedActivityParameterNodeActivation = Class(name="IntermediateActivities_TracedActivityParameterNodeActivation")
uml_TracedActivityPartition = Class(name="uml_TracedActivityPartition")
uml_TracedStateMachine = Class(name="uml_TracedStateMachine")
uml_TracedMessage = Class(name="uml_TracedMessage")
uml_TracedActivity = Class(name="uml_TracedActivity")
uml_TracedForkNode = Class(name="uml_TracedForkNode")
Kernel_TracedReference = Class(name="Kernel_TracedReference")
IntermediateActions_TracedAddStructuralFeatureValueActionActivation = Class(name="IntermediateActions_TracedAddStructuralFeatureValueActionActivation")
uml_TracedInstanceValue = Class(name="uml_TracedInstanceValue")
uml_TracedReclassifyObjectAction = Class(name="uml_TracedReclassifyObjectAction")
uml_TracedUseCase = Class(name="uml_TracedUseCase")
IntermediateActivities_TracedJoinNodeActivation = Class(name="IntermediateActivities_TracedJoinNodeActivation")
Kernel_TracedObject = Class(name="Kernel_TracedObject")
Loci_TracedSemanticVisitor = Class(name="Loci_TracedSemanticVisitor")
uml_TracedDeployment = Class(name="uml_TracedDeployment")
uml_TracedTimeEvent = Class(name="uml_TracedTimeEvent")
uml_TracedPartDecomposition = Class(name="uml_TracedPartDecomposition")
uml_TracedInterruptibleActivityRegion = Class(name="uml_TracedInterruptibleActivityRegion")
uml_TracedProtocolTransition = Class(name="uml_TracedProtocolTransition")
uml_TracedInteractionOperand = Class(name="uml_TracedInteractionOperand")
uml_TracedGeneralization = Class(name="uml_TracedGeneralization")
uml_TracedRemoveStructuralFeatureValueAction = Class(name="uml_TracedRemoveStructuralFeatureValueAction")
uml_TracedInterval = Class(name="uml_TracedInterval")
Kernel_TracedIntegerValue = Class(name="Kernel_TracedIntegerValue")
uml_TracedAnyReceiveEvent = Class(name="uml_TracedAnyReceiveEvent")
uml_TracedReadStructuralFeatureAction = Class(name="uml_TracedReadStructuralFeatureAction")
uml_TracedDataStoreNode = Class(name="uml_TracedDataStoreNode")
uml_TracedProtocolStateMachine = Class(name="uml_TracedProtocolStateMachine")
uml_TracedReception = Class(name="uml_TracedReception")
uml_TracedMessageOccurrenceSpecification = Class(name="uml_TracedMessageOccurrenceSpecification")
uml_TracedTemplateBinding = Class(name="uml_TracedTemplateBinding")
uml_TracedDeploymentSpecification = Class(name="uml_TracedDeploymentSpecification")
uml_TracedUsage = Class(name="uml_TracedUsage")
uml_TracedActionInputPin = Class(name="uml_TracedActionInputPin")
uml_TracedReadVariableAction = Class(name="uml_TracedReadVariableAction")
IntermediateActivities_TracedActivityFinalNodeActivation = Class(name="IntermediateActivities_TracedActivityFinalNodeActivation")
uml_TracedDestroyLinkAction = Class(name="uml_TracedDestroyLinkAction")
uml_TracedLiteralInteger = Class(name="uml_TracedLiteralInteger")
uml_TracedSignalEvent = Class(name="uml_TracedSignalEvent")
Kernel_TracedBooleanValue = Class(name="Kernel_TracedBooleanValue")
uml_TracedConditionalNode = Class(name="uml_TracedConditionalNode")
uml_TracedConnectionPointReference = Class(name="uml_TracedConnectionPointReference")
uml_TracedRealization = Class(name="uml_TracedRealization")
uml_TracedReadLinkObjectEndQualifierAction = Class(name="uml_TracedReadLinkObjectEndQualifierAction")
BasicActions_TracedOpaqueActionActivation = Class(name="BasicActions_TracedOpaqueActionActivation")
uml_TracedJoinNode = Class(name="uml_TracedJoinNode")
uml_TracedRedefinableTemplateSignature = Class(name="uml_TracedRedefinableTemplateSignature")
uml_TracedModel = Class(name="uml_TracedModel")
uml_TracedCentralBufferNode = Class(name="uml_TracedCentralBufferNode")
Kernel_TracedLiteralIntegerEvaluation = Class(name="Kernel_TracedLiteralIntegerEvaluation")
uml_TracedCreateLinkAction = Class(name="uml_TracedCreateLinkAction")
uml_TracedExtensionPoint = Class(name="uml_TracedExtensionPoint")
uml_TracedSignal = Class(name="uml_TracedSignal")
uml_TracedExecutionOccurrenceSpecification = Class(name="uml_TracedExecutionOccurrenceSpecification")
uml_TracedTimeInterval = Class(name="uml_TracedTimeInterval")
uml_TracedInteractionConstraint = Class(name="uml_TracedInteractionConstraint")
IntermediateActivities_TracedDecisionNodeActivation = Class(name="IntermediateActivities_TracedDecisionNodeActivation")
uml_TracedInterface = Class(name="uml_TracedInterface")
uml_TracedOpaqueBehavior = Class(name="uml_TracedOpaqueBehavior")
uml_TracedProtocolConformance = Class(name="uml_TracedProtocolConformance")
uml_TracedPackage = Class(name="uml_TracedPackage")
uml_TracedCallEvent = Class(name="uml_TracedCallEvent")
uml_TracedLoopNode = Class(name="uml_TracedLoopNode")
uml_TracedComment = Class(name="uml_TracedComment")
uml_TracedDataType = Class(name="uml_TracedDataType")
uml_TracedComponentRealization = Class(name="uml_TracedComponentRealization")
uml_TracedAcceptEventAction = Class(name="uml_TracedAcceptEventAction")
uml_TracedOccurrenceSpecification = Class(name="uml_TracedOccurrenceSpecification")
uml_TracedParameterSet = Class(name="uml_TracedParameterSet")
uml_TracedObjectFlow = Class(name="uml_TracedObjectFlow")
uml_TracedOperation = Class(name="uml_TracedOperation")
uml_TracedReadSelfAction = Class(name="uml_TracedReadSelfAction")
IntermediateActions_TracedReadStructuralFeatureActionActivation = Class(name="IntermediateActions_TracedReadStructuralFeatureActionActivation")
uml_TracedDecisionNode = Class(name="uml_TracedDecisionNode")
uml_TracedPackageMerge = Class(name="uml_TracedPackageMerge")
uml_TracedClause = Class(name="uml_TracedClause")
uml_TracedReplyAction = Class(name="uml_TracedReplyAction")
uml_TracedTrigger = Class(name="uml_TracedTrigger")
uml_TracedTransition = Class(name="uml_TracedTransition")
uml_TracedDurationInterval = Class(name="uml_TracedDurationInterval")
uml_TracedLinkEndData = Class(name="uml_TracedLinkEndData")
uml_TracedConnectableElementTemplateParameter = Class(name="uml_TracedConnectableElementTemplateParameter")
uml_TracedOperationTemplateParameter = Class(name="uml_TracedOperationTemplateParameter")
uml_TracedInformationItem = Class(name="uml_TracedInformationItem")
uml_TracedActionExecutionSpecification = Class(name="uml_TracedActionExecutionSpecification")
uml_TracedOutputPin = Class(name="uml_TracedOutputPin")
uml_TracedTemplateParameterSubstitution = Class(name="uml_TracedTemplateParameterSubstitution")
uml_TracedDuration = Class(name="uml_TracedDuration")
uml_TracedReduceAction = Class(name="uml_TracedReduceAction")
uml_TracedFinalState = Class(name="uml_TracedFinalState")
uml_TracedOpaqueAction = Class(name="uml_TracedOpaqueAction")
uml_TracedDevice = Class(name="uml_TracedDevice")
uml_TracedProperty = Class(name="uml_TracedProperty")
uml_TracedExtensionEnd = Class(name="uml_TracedExtensionEnd")
uml_TracedImage = Class(name="uml_TracedImage")
uml_TracedQualifierValue = Class(name="uml_TracedQualifierValue")
uml_TracedAddStructuralFeatureValueAction = Class(name="uml_TracedAddStructuralFeatureValueAction")
uml_TracedProfileApplication = Class(name="uml_TracedProfileApplication")
uml_TracedExpansionNode = Class(name="uml_TracedExpansionNode")
uml_TracedActivityParameterNode = Class(name="uml_TracedActivityParameterNode")
uml_TracedBehaviorExecutionSpecification = Class(name="uml_TracedBehaviorExecutionSpecification")
uml_TracedDurationObservation = Class(name="uml_TracedDurationObservation")
uml_TracedLiteralUnlimitedNatural = Class(name="uml_TracedLiteralUnlimitedNatural")
uml_TracedCallOperationAction = Class(name="uml_TracedCallOperationAction")
uml_TracedArtifact = Class(name="uml_TracedArtifact")
uml_TracedConnectorEnd = Class(name="uml_TracedConnectorEnd")
uml_TracedVariable = Class(name="uml_TracedVariable")
uml_TracedCallBehaviorAction = Class(name="uml_TracedCallBehaviorAction")
uml_TracedReadLinkObjectEndAction = Class(name="uml_TracedReadLinkObjectEndAction")
uml_TracedEnumeration = Class(name="uml_TracedEnumeration")
Kernel_TracedLiteralBooleanEvaluation = Class(name="Kernel_TracedLiteralBooleanEvaluation")
uml_TracedCommunicationPath = Class(name="uml_TracedCommunicationPath")
uml_TracedRaiseExceptionAction = Class(name="uml_TracedRaiseExceptionAction")
uml_TracedTemplateSignature = Class(name="uml_TracedTemplateSignature")
BasicActions_TracedOutputPinActivation = Class(name="BasicActions_TracedOutputPinActivation")
uml_TracedReadExtentAction = Class(name="uml_TracedReadExtentAction")
uml_TracedLinkEndDestructionData = Class(name="uml_TracedLinkEndDestructionData")
uml_TracedStringExpression = Class(name="uml_TracedStringExpression")
uml_TracedPrimitiveType = Class(name="uml_TracedPrimitiveType")
uml_TracedState = Class(name="uml_TracedState")
uml_TracedRegion = Class(name="uml_TracedRegion")
uml_TracedInclude = Class(name="uml_TracedInclude")
uml_TracedReadLinkAction = Class(name="uml_TracedReadLinkAction")
uml_TracedLiteralBoolean = Class(name="uml_TracedLiteralBoolean")
uml_TracedStartObjectBehaviorAction = Class(name="uml_TracedStartObjectBehaviorAction")
IntermediateActions_TracedValueSpecificationActionActivation = Class(name="IntermediateActions_TracedValueSpecificationActionActivation")
uml_TracedLiteralNull = Class(name="uml_TracedLiteralNull")
uml_TracedSlot = Class(name="uml_TracedSlot")
IntermediateActions_TracedCreateObjectActionActivation = Class(name="IntermediateActions_TracedCreateObjectActionActivation")
uml_TracedLiteralReal = Class(name="uml_TracedLiteralReal")
uml_TracedAddVariableValueAction = Class(name="uml_TracedAddVariableValueAction")
uml_TracedClearStructuralFeatureAction = Class(name="uml_TracedClearStructuralFeatureAction")
uml_TracedAssociation = Class(name="uml_TracedAssociation")
uml_TracedExpression = Class(name="uml_TracedExpression")
uml_TracedUnmarshallAction = Class(name="uml_TracedUnmarshallAction")
uml_TracedInterfaceRealization = Class(name="uml_TracedInterfaceRealization")
uml_TracedSendSignalAction = Class(name="uml_TracedSendSignalAction")
uml_TracedCollaboration = Class(name="uml_TracedCollaboration")
uml_TracedTestIdentityAction = Class(name="uml_TracedTestIdentityAction")
uml_TracedProfile = Class(name="uml_TracedProfile")
uml_TracedRemoveVariableValueAction = Class(name="uml_TracedRemoveVariableValueAction")
uml_TracedActor = Class(name="uml_TracedActor")
uml_TracedManifestation = Class(name="uml_TracedManifestation")
uml_TracedTemplateParameter = Class(name="uml_TracedTemplateParameter")
IntermediateActivities_TracedMergeNodeActivation = Class(name="IntermediateActivities_TracedMergeNodeActivation")
IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution = Class(name="IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution")
uml_TracedFunctionBehavior = Class(name="uml_TracedFunctionBehavior")
uml_TracedValueSpecificationAction = Class(name="uml_TracedValueSpecificationAction")
uml_TracedTimeExpression = Class(name="uml_TracedTimeExpression")
uml_TracedAbstraction = Class(name="uml_TracedAbstraction")
uml_TracedReadIsClassifiedObjectAction = Class(name="uml_TracedReadIsClassifiedObjectAction")
uml_TracedComponent = Class(name="uml_TracedComponent")
uml_TracedPseudostate = Class(name="uml_TracedPseudostate")
uml_TracedLinkEndCreationData = Class(name="uml_TracedLinkEndCreationData")
uml_TracedClearAssociationAction = Class(name="uml_TracedClearAssociationAction")
uml_TracedMergeNode = Class(name="uml_TracedMergeNode")
uml_TracedElementImport = Class(name="uml_TracedElementImport")
uml_TracedGeneralOrdering = Class(name="uml_TracedGeneralOrdering")
umlTrace_uml_TracedCombinedFragment = Class(name="umlTrace_uml_TracedCombinedFragment")
TracedInteractionFragment = Class(name="TracedInteractionFragment")
uml_TracedClassifierTemplateParameter = Class(name="uml_TracedClassifierTemplateParameter")
uml_TracedActivityFinalNode = Class(name="uml_TracedActivityFinalNode")
uml_TracedGate = Class(name="uml_TracedGate")
uml_TracedTimeObservation = Class(name="uml_TracedTimeObservation")
uml_TracedControlFlow = Class(name="uml_TracedControlFlow")
umlTrace_uml_TracedDurationConstraint = Class(name="umlTrace_uml_TracedDurationConstraint")
TracedIntervalConstraint = Class(name="TracedIntervalConstraint")
umlTrace_uml_TracedIntervalConstraint = Class(name="umlTrace_uml_TracedIntervalConstraint")
TracedConstraint = Class(name="TracedConstraint")
umlTrace_uml_TracedConstraint = Class(name="umlTrace_uml_TracedConstraint")
TracedPackageableElement = Class(name="TracedPackageableElement")
umlTrace_uml_TracedPackageableElement = Class(name="umlTrace_uml_TracedPackageableElement", is_abstract=True)
uml_TracedParameterableElement = Class(name="uml_TracedParameterableElement")
umlTrace_uml_TracedParameterableElement = Class(name="umlTrace_uml_TracedParameterableElement", is_abstract=True)
umlTrace_uml_TracedPseudostate = Class(name="umlTrace_uml_TracedPseudostate")
TracedVertex = Class(name="TracedVertex")
umlTrace_uml_TracedVertex = Class(name="umlTrace_uml_TracedVertex", is_abstract=True)
umlTrace_uml_TracedDestructionOccurrenceSpecification = Class(name="umlTrace_uml_TracedDestructionOccurrenceSpecification")
TracedMessageOccurrenceSpecification = Class(name="TracedMessageOccurrenceSpecification")
umlTrace_uml_TracedMessageOccurrenceSpecification = Class(name="umlTrace_uml_TracedMessageOccurrenceSpecification")
uml_TracedMessageEnd = Class(name="uml_TracedMessageEnd")
umlTrace_uml_TracedOccurrenceSpecification = Class(name="umlTrace_uml_TracedOccurrenceSpecification")
umlTrace_uml_TracedInteractionFragment = Class(name="umlTrace_uml_TracedInteractionFragment", is_abstract=True)
TracedNamedElement = Class(name="TracedNamedElement")
umlTrace_uml_TracedNamedElement = Class(name="umlTrace_uml_TracedNamedElement", is_abstract=True)
TracedElement = Class(name="TracedElement")
umlTrace_uml_TracedElement = Class(name="umlTrace_uml_TracedElement", is_abstract=True)
TracedEModelElement = Class(name="TracedEModelElement")
umlTrace_uml_TracedConditionalNode = Class(name="umlTrace_uml_TracedConditionalNode")
TracedStructuredActivityNode = Class(name="TracedStructuredActivityNode")
umlTrace_uml_TracedStructuredActivityNode = Class(name="umlTrace_uml_TracedStructuredActivityNode")
uml_TracedAction = Class(name="uml_TracedAction")
uml_TracedNamespace = Class(name="uml_TracedNamespace")
uml_TracedActivityGroup = Class(name="uml_TracedActivityGroup")
umlTrace_uml_TracedAction = Class(name="umlTrace_uml_TracedAction", is_abstract=True)
TracedExecutableNode = Class(name="TracedExecutableNode")
umlTrace_uml_TracedExecutableNode = Class(name="umlTrace_uml_TracedExecutableNode", is_abstract=True)
TracedActivityNode = Class(name="TracedActivityNode")
umlTrace_uml_TracedActivityNode = Class(name="umlTrace_uml_TracedActivityNode", is_abstract=True)
uml_TracedRedefinableElement = Class(name="uml_TracedRedefinableElement")
ActivityContent = Class(name="ActivityContent")
umlTrace_uml_TracedRedefinableElement = Class(name="umlTrace_uml_TracedRedefinableElement", is_abstract=True)
umlTrace_uml_TracedNamespace = Class(name="umlTrace_uml_TracedNamespace", is_abstract=True)
umlTrace_uml_TracedActivityGroup = Class(name="umlTrace_uml_TracedActivityGroup", is_abstract=True)
uml_TracedNamedElement = Class(name="uml_TracedNamedElement")
umlTrace_uml_TracedCreateLinkObjectAction = Class(name="umlTrace_uml_TracedCreateLinkObjectAction")
TracedCreateLinkAction = Class(name="TracedCreateLinkAction")
umlTrace_uml_TracedCreateLinkAction = Class(name="umlTrace_uml_TracedCreateLinkAction")
TracedWriteLinkAction = Class(name="TracedWriteLinkAction")
umlTrace_uml_TracedWriteLinkAction = Class(name="umlTrace_uml_TracedWriteLinkAction", is_abstract=True)
TracedLinkAction = Class(name="TracedLinkAction")
umlTrace_uml_TracedLinkAction = Class(name="umlTrace_uml_TracedLinkAction", is_abstract=True)
TracedAction = Class(name="TracedAction")
umlTrace_uml_TracedInitialNode = Class(name="umlTrace_uml_TracedInitialNode")
TracedControlNode = Class(name="TracedControlNode")
umlTrace_uml_TracedControlNode = Class(name="umlTrace_uml_TracedControlNode", is_abstract=True)
umlTrace_uml_TracedFlowFinalNode = Class(name="umlTrace_uml_TracedFlowFinalNode")
TracedFinalNode = Class(name="TracedFinalNode")
umlTrace_uml_TracedFinalNode = Class(name="umlTrace_uml_TracedFinalNode", is_abstract=True)
umlTrace_uml_TracedExpansionRegion = Class(name="umlTrace_uml_TracedExpansionRegion")
umlTrace_uml_TracedCreateObjectAction = Class(name="umlTrace_uml_TracedCreateObjectAction")
umlTrace_uml_TracedLifeline = Class(name="umlTrace_uml_TracedLifeline")
umlTrace_uml_TracedObservation = Class(name="umlTrace_uml_TracedObservation", is_abstract=True)
umlTrace_uml_TracedInteractionUse = Class(name="umlTrace_uml_TracedInteractionUse")
umlTrace_uml_TracedLoopNode = Class(name="umlTrace_uml_TracedLoopNode")
umlTrace_uml_TracedSignal = Class(name="umlTrace_uml_TracedSignal")
umlTrace_uml_TracedGeneralizationSet = Class(name="umlTrace_uml_TracedGeneralizationSet")
umlTrace_uml_TracedChangeEvent = Class(name="umlTrace_uml_TracedChangeEvent")
TracedEvent = Class(name="TracedEvent")
umlTrace_uml_TracedEvent = Class(name="umlTrace_uml_TracedEvent", is_abstract=True)
umlTrace_uml_TracedDependency = Class(name="umlTrace_uml_TracedDependency")
uml_TracedDirectedRelationship = Class(name="uml_TracedDirectedRelationship")
umlTrace_uml_TracedPort = Class(name="umlTrace_uml_TracedPort")
TracedProperty = Class(name="TracedProperty")
umlTrace_uml_TracedProperty = Class(name="umlTrace_uml_TracedProperty")
uml_TracedStructuralFeature = Class(name="uml_TracedStructuralFeature")
uml_TracedConnectableElement = Class(name="uml_TracedConnectableElement")
uml_TracedDeploymentTarget = Class(name="uml_TracedDeploymentTarget")
umlTrace_uml_TracedMessageEnd = Class(name="umlTrace_uml_TracedMessageEnd", is_abstract=True)
umlTrace_uml_TracedPackage = Class(name="umlTrace_uml_TracedPackage")
uml_TracedPackageableElement = Class(name="uml_TracedPackageableElement")
uml_TracedTemplateableElement = Class(name="uml_TracedTemplateableElement")
umlTrace_uml_TracedTemplateableElement = Class(name="umlTrace_uml_TracedTemplateableElement", is_abstract=True)
umlTrace_uml_TracedConnector = Class(name="umlTrace_uml_TracedConnector")
TracedFeature = Class(name="TracedFeature")
umlTrace_uml_TracedFeature = Class(name="umlTrace_uml_TracedFeature", is_abstract=True)
TracedRedefinableElement = Class(name="TracedRedefinableElement")
umlTrace_uml_TracedSendObjectAction = Class(name="umlTrace_uml_TracedSendObjectAction")
TracedInvocationAction = Class(name="TracedInvocationAction")
umlTrace_uml_TracedInvocationAction = Class(name="umlTrace_uml_TracedInvocationAction", is_abstract=True)
umlTrace_uml_TracedOpaqueAction = Class(name="umlTrace_uml_TracedOpaqueAction")
umlTrace_uml_TracedProtocolConformance = Class(name="umlTrace_uml_TracedProtocolConformance")
TracedDirectedRelationship = Class(name="TracedDirectedRelationship")
umlTrace_uml_TracedDirectedRelationship = Class(name="umlTrace_uml_TracedDirectedRelationship", is_abstract=True)
TracedRelationship = Class(name="TracedRelationship")
umlTrace_uml_TracedRelationship = Class(name="umlTrace_uml_TracedRelationship", is_abstract=True)
umlTrace_uml_TracedCallBehaviorAction = Class(name="umlTrace_uml_TracedCallBehaviorAction")
TracedCallAction = Class(name="TracedCallAction")
umlTrace_uml_TracedCallAction = Class(name="umlTrace_uml_TracedCallAction", is_abstract=True)
umlTrace_uml_TracedPackageImport = Class(name="umlTrace_uml_TracedPackageImport")
umlTrace_uml_TracedClass = Class(name="umlTrace_uml_TracedClass")
uml_TracedEncapsulatedClassifier = Class(name="uml_TracedEncapsulatedClassifier")
uml_TracedBehavioredClassifier = Class(name="uml_TracedBehavioredClassifier")
umlTrace_uml_TracedEncapsulatedClassifier = Class(name="umlTrace_uml_TracedEncapsulatedClassifier", is_abstract=True)
TracedStructuredClassifier = Class(name="TracedStructuredClassifier")
umlTrace_uml_TracedStructuredClassifier = Class(name="umlTrace_uml_TracedStructuredClassifier", is_abstract=True)
TracedClassifier = Class(name="TracedClassifier")
umlTrace_uml_TracedClassifier = Class(name="umlTrace_uml_TracedClassifier", is_abstract=True)
uml_TracedType = Class(name="uml_TracedType")
umlTrace_uml_TracedType = Class(name="umlTrace_uml_TracedType", is_abstract=True)
umlTrace_uml_TracedBehavioredClassifier = Class(name="umlTrace_uml_TracedBehavioredClassifier", is_abstract=True)
umlTrace_uml_TracedActivityFinalNode = Class(name="umlTrace_uml_TracedActivityFinalNode")
TracedNode = Class(name="TracedNode")
umlTrace_uml_TracedConsiderIgnoreFragment = Class(name="umlTrace_uml_TracedConsiderIgnoreFragment")
TracedCombinedFragment = Class(name="TracedCombinedFragment")
umlTrace_uml_TracedContinuation = Class(name="umlTrace_uml_TracedContinuation")
umlTrace_uml_TracedCallOperationAction = Class(name="umlTrace_uml_TracedCallOperationAction")
umlTrace_uml_TracedTimeConstraint = Class(name="umlTrace_uml_TracedTimeConstraint")
umlTrace_uml_TracedClearVariableAction = Class(name="umlTrace_uml_TracedClearVariableAction")
TracedVariableAction = Class(name="TracedVariableAction")
umlTrace_uml_TracedVariableAction = Class(name="umlTrace_uml_TracedVariableAction", is_abstract=True)
umlTrace_uml_TracedReadSelfAction = Class(name="umlTrace_uml_TracedReadSelfAction")
umlTrace_uml_TracedLiteralString = Class(name="umlTrace_uml_TracedLiteralString")
TracedLiteralSpecification = Class(name="TracedLiteralSpecification")
umlTrace_uml_TracedLiteralSpecification = Class(name="umlTrace_uml_TracedLiteralSpecification", is_abstract=True)
TracedValueSpecification = Class(name="TracedValueSpecification")
umlTrace_uml_TracedValueSpecification = Class(name="umlTrace_uml_TracedValueSpecification", is_abstract=True)
umlTrace_uml_TracedBroadcastSignalAction = Class(name="umlTrace_uml_TracedBroadcastSignalAction")
umlTrace_uml_TracedStructuralFeature = Class(name="umlTrace_uml_TracedStructuralFeature", is_abstract=True)
uml_TracedFeature = Class(name="uml_TracedFeature")
uml_TracedTypedElement = Class(name="uml_TracedTypedElement")
uml_TracedMultiplicityElement = Class(name="uml_TracedMultiplicityElement")
umlTrace_uml_TracedTypedElement = Class(name="umlTrace_uml_TracedTypedElement", is_abstract=True)
umlTrace_uml_TracedMultiplicityElement = Class(name="umlTrace_uml_TracedMultiplicityElement", is_abstract=True)
umlTrace_uml_TracedConnectableElement = Class(name="umlTrace_uml_TracedConnectableElement", is_abstract=True)
umlTrace_uml_TracedDeploymentTarget = Class(name="umlTrace_uml_TracedDeploymentTarget", is_abstract=True)
umlTrace_uml_TracedCollaborationUse = Class(name="umlTrace_uml_TracedCollaborationUse")
umlTrace_uml_TracedValuePin = Class(name="umlTrace_uml_TracedValuePin")
TracedInputPin = Class(name="TracedInputPin")
umlTrace_uml_TracedInputPin = Class(name="umlTrace_uml_TracedInputPin")
TracedPin = Class(name="TracedPin")
umlTrace_uml_TracedPin = Class(name="umlTrace_uml_TracedPin", is_abstract=True)
uml_TracedObjectNode = Class(name="uml_TracedObjectNode")
umlTrace_uml_TracedObjectNode = Class(name="umlTrace_uml_TracedObjectNode", is_abstract=True)
uml_TracedActivityNode = Class(name="uml_TracedActivityNode")
umlTrace_uml_TracedDeploymentSpecification = Class(name="umlTrace_uml_TracedDeploymentSpecification")
TracedArtifact = Class(name="TracedArtifact")
umlTrace_uml_TracedArtifact = Class(name="umlTrace_uml_TracedArtifact")
uml_TracedClassifier = Class(name="uml_TracedClassifier")
uml_TracedDeployedArtifact = Class(name="uml_TracedDeployedArtifact")
umlTrace_uml_TracedDeployedArtifact = Class(name="umlTrace_uml_TracedDeployedArtifact", is_abstract=True)
umlTrace_uml_TracedTransition = Class(name="umlTrace_uml_TracedTransition")
umlTrace_uml_TracedNode = Class(name="umlTrace_uml_TracedNode")
umlTrace_uml_TracedExceptionHandler = Class(name="umlTrace_uml_TracedExceptionHandler")
umlTrace_uml_TracedSequenceNode = Class(name="umlTrace_uml_TracedSequenceNode")
umlTrace_uml_TracedUseCase = Class(name="umlTrace_uml_TracedUseCase")
TracedBehavioredClassifier = Class(name="TracedBehavioredClassifier")
umlTrace_uml_TracedStartClassifierBehaviorAction = Class(name="umlTrace_uml_TracedStartClassifierBehaviorAction")
umlTrace_uml_TracedExtend = Class(name="umlTrace_uml_TracedExtend")
umlTrace_uml_TracedRemoveStructuralFeatureValueAction = Class(name="umlTrace_uml_TracedRemoveStructuralFeatureValueAction")
TracedWriteStructuralFeatureAction = Class(name="TracedWriteStructuralFeatureAction")
umlTrace_uml_TracedWriteStructuralFeatureAction = Class(name="umlTrace_uml_TracedWriteStructuralFeatureAction", is_abstract=True)
TracedStructuralFeatureAction = Class(name="TracedStructuralFeatureAction")
umlTrace_uml_TracedStructuralFeatureAction = Class(name="umlTrace_uml_TracedStructuralFeatureAction", is_abstract=True)
umlTrace_uml_TracedReadLinkAction = Class(name="umlTrace_uml_TracedReadLinkAction")
umlTrace_uml_TracedExtension = Class(name="umlTrace_uml_TracedExtension")
TracedAssociation = Class(name="TracedAssociation")
umlTrace_uml_TracedAssociation = Class(name="umlTrace_uml_TracedAssociation")
uml_TracedRelationship = Class(name="uml_TracedRelationship")
umlTrace_uml_TracedExecutionEnvironment = Class(name="umlTrace_uml_TracedExecutionEnvironment")
umlTrace_uml_TracedInformationFlow = Class(name="umlTrace_uml_TracedInformationFlow")
umlTrace_uml_TracedDestroyObjectAction = Class(name="umlTrace_uml_TracedDestroyObjectAction")
umlTrace_uml_TracedActivityPartition = Class(name="umlTrace_uml_TracedActivityPartition")
TracedActivityGroup = Class(name="TracedActivityGroup")
umlTrace_uml_TracedStateMachine = Class(name="umlTrace_uml_TracedStateMachine")
TracedBehavior = Class(name="TracedBehavior")
umlTrace_uml_TracedMessage = Class(name="umlTrace_uml_TracedMessage")
umlTrace_uml_TracedReadLinkObjectEndQualifierAction = Class(name="umlTrace_uml_TracedReadLinkObjectEndQualifierAction")
umlTrace_uml_TracedDeployment = Class(name="umlTrace_uml_TracedDeployment")
umlTrace_uml_TracedActivity = Class(name="umlTrace_uml_TracedActivity")
umlTrace_uml_TracedForkNode = Class(name="umlTrace_uml_TracedForkNode")
umlTrace_uml_TracedProtocolStateMachine = Class(name="umlTrace_uml_TracedProtocolStateMachine")
TracedStateMachine = Class(name="TracedStateMachine")
umlTrace_uml_TracedInterval = Class(name="umlTrace_uml_TracedInterval")
umlTrace_uml_TracedClearStructuralFeatureAction = Class(name="umlTrace_uml_TracedClearStructuralFeatureAction")
umlTrace_uml_TracedObjectFlow = Class(name="umlTrace_uml_TracedObjectFlow")
TracedActivityEdge = Class(name="TracedActivityEdge")
umlTrace_uml_TracedInteraction = Class(name="umlTrace_uml_TracedInteraction")
uml_TracedBehavior = Class(name="uml_TracedBehavior")
uml_TracedInteractionFragment = Class(name="uml_TracedInteractionFragment")
umlTrace_uml_TracedBehavior = Class(name="umlTrace_uml_TracedBehavior", is_abstract=True)
TracedClass = Class(name="TracedClass")
umlTrace_uml_TracedSlot = Class(name="umlTrace_uml_TracedSlot")
umlTrace_uml_TracedLiteralNull = Class(name="umlTrace_uml_TracedLiteralNull")
umlTrace_uml_TracedParameter = Class(name="umlTrace_uml_TracedParameter")
umlTrace_uml_TracedOpaqueExpression = Class(name="umlTrace_uml_TracedOpaqueExpression")
umlTrace_uml_TracedTrigger = Class(name="umlTrace_uml_TracedTrigger")
umlTrace_uml_TracedStateInvariant = Class(name="umlTrace_uml_TracedStateInvariant")
umlTrace_uml_TracedAssociationClass = Class(name="umlTrace_uml_TracedAssociationClass")
umlTrace_uml_TracedInstanceSpecification = Class(name="umlTrace_uml_TracedInstanceSpecification")
umlTrace_uml_TracedTemplateSignature = Class(name="umlTrace_uml_TracedTemplateSignature")
umlTrace_uml_TracedLinkEndDestructionData = Class(name="umlTrace_uml_TracedLinkEndDestructionData")
TracedLinkEndData = Class(name="TracedLinkEndData")
umlTrace_uml_TracedLinkEndData = Class(name="umlTrace_uml_TracedLinkEndData")
umlTrace_uml_TracedAcceptCallAction = Class(name="umlTrace_uml_TracedAcceptCallAction")
TracedAcceptEventAction = Class(name="TracedAcceptEventAction")
umlTrace_uml_TracedAcceptEventAction = Class(name="umlTrace_uml_TracedAcceptEventAction")
umlTrace_uml_TracedReduceAction = Class(name="umlTrace_uml_TracedReduceAction")
umlTrace_uml_TracedRaiseExceptionAction = Class(name="umlTrace_uml_TracedRaiseExceptionAction")
umlTrace_uml_TracedStereotype = Class(name="umlTrace_uml_TracedStereotype")
umlTrace_uml_TracedClearAssociationAction = Class(name="umlTrace_uml_TracedClearAssociationAction")
umlTrace_uml_TracedEnumerationLiteral = Class(name="umlTrace_uml_TracedEnumerationLiteral")
TracedInstanceSpecification = Class(name="TracedInstanceSpecification")
umlTrace_uml_TracedSubstitution = Class(name="umlTrace_uml_TracedSubstitution")
TracedRealization = Class(name="TracedRealization")
umlTrace_uml_TracedRealization = Class(name="umlTrace_uml_TracedRealization")
TracedAbstraction = Class(name="TracedAbstraction")
umlTrace_uml_TracedAbstraction = Class(name="umlTrace_uml_TracedAbstraction")
TracedDependency = Class(name="TracedDependency")
umlTrace_uml_TracedExecutionSpecification = Class(name="umlTrace_uml_TracedExecutionSpecification", is_abstract=True)
umlTrace_uml_TracedReplyAction = Class(name="umlTrace_uml_TracedReplyAction")
umlTrace_uml_TracedActor = Class(name="umlTrace_uml_TracedActor")
umlTrace_uml_TracedReception = Class(name="umlTrace_uml_TracedReception")
TracedBehavioralFeature = Class(name="TracedBehavioralFeature")
umlTrace_uml_TracedTemplateBinding = Class(name="umlTrace_uml_TracedTemplateBinding")
umlTrace_uml_TracedUsage = Class(name="umlTrace_uml_TracedUsage")
umlTrace_uml_TracedActionInputPin = Class(name="umlTrace_uml_TracedActionInputPin")
umlTrace_uml_TracedReadVariableAction = Class(name="umlTrace_uml_TracedReadVariableAction")
umlTrace_uml_TracedDestroyLinkAction = Class(name="umlTrace_uml_TracedDestroyLinkAction")
umlTrace_uml_TracedLiteralInteger = Class(name="umlTrace_uml_TracedLiteralInteger")
umlTrace_uml_TracedSignalEvent = Class(name="umlTrace_uml_TracedSignalEvent")
umlTrace_uml_TracedReadLinkObjectEndAction = Class(name="umlTrace_uml_TracedReadLinkObjectEndAction")
umlTrace_uml_TracedTimeInterval = Class(name="umlTrace_uml_TracedTimeInterval")
TracedInterval = Class(name="TracedInterval")
umlTrace_uml_TracedOperationTemplateParameter = Class(name="umlTrace_uml_TracedOperationTemplateParameter")
umlTrace_uml_TracedDurationObservation = Class(name="umlTrace_uml_TracedDurationObservation")
TracedObservation = Class(name="TracedObservation")
umlTrace_uml_TracedActivityEdge = Class(name="umlTrace_uml_TracedActivityEdge", is_abstract=True)
umlTrace_uml_TracedTestIdentityAction = Class(name="umlTrace_uml_TracedTestIdentityAction")
umlTrace_uml_TracedInstanceValue = Class(name="umlTrace_uml_TracedInstanceValue")
umlTrace_uml_TracedLiteralUnlimitedNatural = Class(name="umlTrace_uml_TracedLiteralUnlimitedNatural")
umlTrace_uml_TracedReclassifyObjectAction = Class(name="umlTrace_uml_TracedReclassifyObjectAction")
umlTrace_uml_TracedTimeEvent = Class(name="umlTrace_uml_TracedTimeEvent")
umlTrace_uml_TracedPartDecomposition = Class(name="umlTrace_uml_TracedPartDecomposition")
TracedInteractionUse = Class(name="TracedInteractionUse")
umlTrace_uml_TracedInterruptibleActivityRegion = Class(name="umlTrace_uml_TracedInterruptibleActivityRegion")
umlTrace_uml_TracedAddVariableValueAction = Class(name="umlTrace_uml_TracedAddVariableValueAction")
TracedWriteVariableAction = Class(name="TracedWriteVariableAction")
umlTrace_uml_TracedWriteVariableAction = Class(name="umlTrace_uml_TracedWriteVariableAction", is_abstract=True)
umlTrace_uml_TracedProtocolTransition = Class(name="umlTrace_uml_TracedProtocolTransition")
TracedTransition = Class(name="TracedTransition")
umlTrace_uml_TracedImage = Class(name="umlTrace_uml_TracedImage")
umlTrace_uml_TracedLiteralReal = Class(name="umlTrace_uml_TracedLiteralReal")
umlTrace_uml_TracedInteractionOperand = Class(name="umlTrace_uml_TracedInteractionOperand")
umlTrace_uml_TracedGeneralization = Class(name="umlTrace_uml_TracedGeneralization")
umlTrace_uml_TracedInformationItem = Class(name="umlTrace_uml_TracedInformationItem")
umlTrace_uml_TracedModel = Class(name="umlTrace_uml_TracedModel")
TracedPackage = Class(name="TracedPackage")
umlTrace_uml_TracedClassifierTemplateParameter = Class(name="umlTrace_uml_TracedClassifierTemplateParameter")
TracedTemplateParameter = Class(name="TracedTemplateParameter")
umlTrace_uml_TracedTemplateParameter = Class(name="umlTrace_uml_TracedTemplateParameter")
umlTrace_uml_TracedOperation = Class(name="umlTrace_uml_TracedOperation")
uml_TracedBehavioralFeature = Class(name="uml_TracedBehavioralFeature")
umlTrace_uml_TracedBehavioralFeature = Class(name="umlTrace_uml_TracedBehavioralFeature", is_abstract=True)
umlTrace_uml_TracedAnyReceiveEvent = Class(name="umlTrace_uml_TracedAnyReceiveEvent")
TracedMessageEvent = Class(name="TracedMessageEvent")
umlTrace_uml_TracedMessageEvent = Class(name="umlTrace_uml_TracedMessageEvent", is_abstract=True)
umlTrace_uml_TracedPrimitiveType = Class(name="umlTrace_uml_TracedPrimitiveType")
TracedDataType = Class(name="TracedDataType")
umlTrace_uml_TracedDataType = Class(name="umlTrace_uml_TracedDataType")
umlTrace_uml_TracedReadStructuralFeatureAction = Class(name="umlTrace_uml_TracedReadStructuralFeatureAction")
umlTrace_uml_TracedParameterSet = Class(name="umlTrace_uml_TracedParameterSet")
umlTrace_uml_TracedDataStoreNode = Class(name="umlTrace_uml_TracedDataStoreNode")
TracedCentralBufferNode = Class(name="TracedCentralBufferNode")
umlTrace_uml_TracedCentralBufferNode = Class(name="umlTrace_uml_TracedCentralBufferNode")
TracedObjectNode = Class(name="TracedObjectNode")
umlTrace_uml_TracedSendSignalAction = Class(name="umlTrace_uml_TracedSendSignalAction")
umlTrace_uml_TracedConnectableElementTemplateParameter = Class(name="umlTrace_uml_TracedConnectableElementTemplateParameter")
umlTrace_uml_TracedActionExecutionSpecification = Class(name="umlTrace_uml_TracedActionExecutionSpecification")
umlTrace_uml_TracedOutputPin = Class(name="umlTrace_uml_TracedOutputPin")
umlTrace_uml_TracedDuration = Class(name="umlTrace_uml_TracedDuration")
umlTrace_uml_TracedUnmarshallAction = Class(name="umlTrace_uml_TracedUnmarshallAction")
umlTrace_uml_TracedProfile = Class(name="umlTrace_uml_TracedProfile")
umlTrace_uml_TracedExtensionEnd = Class(name="umlTrace_uml_TracedExtensionEnd")
umlTrace_uml_TracedExpansionNode = Class(name="umlTrace_uml_TracedExpansionNode")
umlTrace_uml_TracedActivityParameterNode = Class(name="umlTrace_uml_TracedActivityParameterNode")
umlTrace_uml_TracedProfileApplication = Class(name="umlTrace_uml_TracedProfileApplication")
umlTrace_uml_TracedConnectorEnd = Class(name="umlTrace_uml_TracedConnectorEnd")
TracedMultiplicityElement = Class(name="TracedMultiplicityElement")
umlTrace_uml_TracedEnumeration = Class(name="umlTrace_uml_TracedEnumeration")
umlTrace_uml_TracedCollaboration = Class(name="umlTrace_uml_TracedCollaboration")
uml_TracedStructuredClassifier = Class(name="uml_TracedStructuredClassifier")
umlTrace_uml_TracedVariable = Class(name="umlTrace_uml_TracedVariable")
umlTrace_uml_TracedConnectionPointReference = Class(name="umlTrace_uml_TracedConnectionPointReference")
umlTrace_uml_TracedTimeExpression = Class(name="umlTrace_uml_TracedTimeExpression")
umlTrace_uml_TracedQualifierValue = Class(name="umlTrace_uml_TracedQualifierValue")
umlTrace_uml_TracedDurationInterval = Class(name="umlTrace_uml_TracedDurationInterval")
umlTrace_uml_TracedFunctionBehavior = Class(name="umlTrace_uml_TracedFunctionBehavior")
TracedOpaqueBehavior = Class(name="TracedOpaqueBehavior")
umlTrace_uml_TracedOpaqueBehavior = Class(name="umlTrace_uml_TracedOpaqueBehavior")
umlTrace_uml_TracedInterfaceRealization = Class(name="umlTrace_uml_TracedInterfaceRealization")
umlTrace_uml_TracedDevice = Class(name="umlTrace_uml_TracedDevice")
umlTrace_uml_TracedTemplateParameterSubstitution = Class(name="umlTrace_uml_TracedTemplateParameterSubstitution")
umlTrace_uml_TracedJoinNode = Class(name="umlTrace_uml_TracedJoinNode")
umlTrace_uml_TracedRedefinableTemplateSignature = Class(name="umlTrace_uml_TracedRedefinableTemplateSignature")
umlTrace_uml_TracedReadIsClassifiedObjectAction = Class(name="umlTrace_uml_TracedReadIsClassifiedObjectAction")
umlTrace_uml_TracedTimeObservation = Class(name="umlTrace_uml_TracedTimeObservation")
umlTrace_uml_TracedDecisionNode = Class(name="umlTrace_uml_TracedDecisionNode")
umlTrace_uml_TracedElementImport = Class(name="umlTrace_uml_TracedElementImport")
umlTrace_uml_TracedExtensionPoint = Class(name="umlTrace_uml_TracedExtensionPoint")
umlTrace_uml_TracedExecutionOccurrenceSpecification = Class(name="umlTrace_uml_TracedExecutionOccurrenceSpecification")
TracedOccurrenceSpecification = Class(name="TracedOccurrenceSpecification")
umlTrace_uml_TracedInteractionConstraint = Class(name="umlTrace_uml_TracedInteractionConstraint")
umlTrace_uml_TracedAddStructuralFeatureValueAction = Class(name="umlTrace_uml_TracedAddStructuralFeatureValueAction")
umlTrace_uml_TracedInterface = Class(name="umlTrace_uml_TracedInterface")
umlTrace_uml_TracedComponent = Class(name="umlTrace_uml_TracedComponent")
umlTrace_uml_TracedCallEvent = Class(name="umlTrace_uml_TracedCallEvent")
umlTrace_uml_TracedComment = Class(name="umlTrace_uml_TracedComment")
umlTrace_uml_TracedBehaviorExecutionSpecification = Class(name="umlTrace_uml_TracedBehaviorExecutionSpecification")
TracedExecutionSpecification = Class(name="TracedExecutionSpecification")
umlTrace_uml_TracedComponentRealization = Class(name="umlTrace_uml_TracedComponentRealization")
umlTrace_uml_TracedCommunicationPath = Class(name="umlTrace_uml_TracedCommunicationPath")
umlTrace_uml_TracedPackageMerge = Class(name="umlTrace_uml_TracedPackageMerge")
umlTrace_uml_TracedClause = Class(name="umlTrace_uml_TracedClause")
umlTrace_uml_TracedFinalState = Class(name="umlTrace_uml_TracedFinalState")
TracedState = Class(name="TracedState")
umlTrace_uml_TracedState = Class(name="umlTrace_uml_TracedState")
uml_TracedVertex = Class(name="uml_TracedVertex")
umlTrace_IntermediateActivities_TracedForkNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedForkNodeActivation")
TracedControlNodeActivation = Class(name="TracedControlNodeActivation")
umlTrace_IntermediateActivities_TracedControlNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedControlNodeActivation", is_abstract=True)
TracedActivityNodeActivation = Class(name="TracedActivityNodeActivation")
umlTrace_IntermediateActivities_TracedActivityNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedActivityNodeActivation")
TracedSemanticVisitor = Class(name="TracedSemanticVisitor")
umlTrace_IntermediateActivities_TracedObjectNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedObjectNodeActivation", is_abstract=True)
umlTrace_IntermediateActivities_TracedInitialNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedInitialNodeActivation")
umlTrace_IntermediateActivities_TracedActivityExecution = Class(name="umlTrace_IntermediateActivities_TracedActivityExecution")
TracedExecution = Class(name="TracedExecution")
umlTrace_IntermediateActivities_TracedMergeNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedMergeNodeActivation")
umlTrace_uml_TracedValueSpecificationAction = Class(name="umlTrace_uml_TracedValueSpecificationAction")
umlTrace_uml_TracedReadExtentAction = Class(name="umlTrace_uml_TracedReadExtentAction")
umlTrace_uml_TracedStringExpression = Class(name="umlTrace_uml_TracedStringExpression")
umlTrace_uml_TracedExpression = Class(name="umlTrace_uml_TracedExpression")
umlTrace_uml_TracedGeneralOrdering = Class(name="umlTrace_uml_TracedGeneralOrdering")
umlTrace_uml_TracedLiteralBoolean = Class(name="umlTrace_uml_TracedLiteralBoolean")
umlTrace_uml_TracedStartObjectBehaviorAction = Class(name="umlTrace_uml_TracedStartObjectBehaviorAction")
umlTrace_uml_TracedRegion = Class(name="umlTrace_uml_TracedRegion")
umlTrace_uml_TracedInclude = Class(name="umlTrace_uml_TracedInclude")
umlTrace_uml_TracedControlFlow = Class(name="umlTrace_uml_TracedControlFlow")
umlTrace_uml_TracedGate = Class(name="umlTrace_uml_TracedGate")
TracedMessageEnd = Class(name="TracedMessageEnd")
umlTrace_uml_TracedRemoveVariableValueAction = Class(name="umlTrace_uml_TracedRemoveVariableValueAction")
umlTrace_uml_TracedManifestation = Class(name="umlTrace_uml_TracedManifestation")
umlTrace_uml_TracedLinkEndCreationData = Class(name="umlTrace_uml_TracedLinkEndCreationData")
umlTrace_uml_TracedMergeNode = Class(name="umlTrace_uml_TracedMergeNode")
umlTrace_ecore_TracedEModelElement = Class(name="umlTrace_ecore_TracedEModelElement", is_abstract=True)
umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation = Class(name="umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation", is_abstract=True)
umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation = Class(name="umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation")
TracedStructuralFeatureActionActivation = Class(name="TracedStructuralFeatureActionActivation")
umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation = Class(name="umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation")
TracedWriteStructuralFeatureActionActivation = Class(name="TracedWriteStructuralFeatureActionActivation")
umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation = Class(name="umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation", is_abstract=True)
umlTrace_IntermediateActions_TracedValueSpecificationActionActivation = Class(name="umlTrace_IntermediateActions_TracedValueSpecificationActionActivation")
umlTrace_IntermediateActions_TracedCreateObjectActionActivation = Class(name="umlTrace_IntermediateActions_TracedCreateObjectActionActivation")
umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation")
TracedObjectNodeActivation = Class(name="TracedObjectNodeActivation")
umlTrace_IntermediateActivities_TracedJoinNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedJoinNodeActivation")
umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation")
umlTrace_IntermediateActivities_TracedDecisionNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedDecisionNodeActivation")
umlTrace_Loci_TracedSemanticVisitor = Class(name="umlTrace_Loci_TracedSemanticVisitor")
umlTrace_BasicActions_TracedPinActivation = Class(name="umlTrace_BasicActions_TracedPinActivation", is_abstract=True)
umlTrace_BasicActions_TracedActionActivation = Class(name="umlTrace_BasicActions_TracedActionActivation", is_abstract=True)
umlTrace_BasicActions_TracedInvocationActionActivation = Class(name="umlTrace_BasicActions_TracedInvocationActionActivation", is_abstract=True)
TracedActionActivation = Class(name="TracedActionActivation")
umlTrace_BasicActions_TracedCallActionActivation = Class(name="umlTrace_BasicActions_TracedCallActionActivation", is_abstract=True)
TracedInvocationActionActivation = Class(name="TracedInvocationActionActivation")
umlTrace_BasicActions_TracedOpaqueActionActivation = Class(name="umlTrace_BasicActions_TracedOpaqueActionActivation")
umlTrace_BasicActions_TracedInputPinActivation = Class(name="umlTrace_BasicActions_TracedInputPinActivation")
TracedPinActivation = Class(name="TracedPinActivation")
umlTrace_BasicActions_TracedCallBehaviorActionActivation = Class(name="umlTrace_BasicActions_TracedCallBehaviorActionActivation")
TracedCallActionActivation = Class(name="TracedCallActionActivation")
umlTrace_BasicActions_TracedOutputPinActivation = Class(name="umlTrace_BasicActions_TracedOutputPinActivation")
umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution = Class(name="umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution")
TracedOpaqueBehaviorExecution = Class(name="TracedOpaqueBehaviorExecution")
umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution = Class(name="umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution")
umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution = Class(name="umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution")
umlTrace_Values_SemanticVisitor_runtimeModelElement_Value = Class(name="umlTrace_Values_SemanticVisitor_runtimeModelElement_Value")
uml_TracedElement = Class(name="uml_TracedElement")
umlTrace_BasicBehaviors_TracedExecution = Class(name="umlTrace_BasicBehaviors_TracedExecution", is_abstract=True)
TracedObject = Class(name="TracedObject")
umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution = Class(name="umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution", is_abstract=True)
umlTrace_Kernel_TracedObject = Class(name="umlTrace_Kernel_TracedObject")
TracedExtensionalValue = Class(name="TracedExtensionalValue")
umlTrace_Kernel_TracedExtensionalValue = Class(name="umlTrace_Kernel_TracedExtensionalValue", is_abstract=True)
TracedCompoundValue = Class(name="TracedCompoundValue")
umlTrace_Kernel_TracedCompoundValue = Class(name="umlTrace_Kernel_TracedCompoundValue", is_abstract=True)
TracedStructuredValue = Class(name="TracedStructuredValue")
umlTrace_Kernel_TracedStructuredValue = Class(name="umlTrace_Kernel_TracedStructuredValue", is_abstract=True)
TracedValue = Class(name="TracedValue")
umlTrace_Kernel_TracedValue = Class(name="umlTrace_Kernel_TracedValue", is_abstract=True)
umlTrace_Kernel_TracedReference = Class(name="umlTrace_Kernel_TracedReference")
umlTrace_Kernel_TracedLiteralEvaluation = Class(name="umlTrace_Kernel_TracedLiteralEvaluation", is_abstract=True)
TracedEvaluation = Class(name="TracedEvaluation")
umlTrace_Kernel_TracedEvaluation = Class(name="umlTrace_Kernel_TracedEvaluation", is_abstract=True)
umlTrace_Kernel_TracedIntegerValue = Class(name="umlTrace_Kernel_TracedIntegerValue")
TracedPrimitiveValue = Class(name="TracedPrimitiveValue")
umlTrace_Kernel_TracedPrimitiveValue = Class(name="umlTrace_Kernel_TracedPrimitiveValue", is_abstract=True)
umlTrace_Kernel_TracedLiteralBooleanEvaluation = Class(name="umlTrace_Kernel_TracedLiteralBooleanEvaluation")
TracedLiteralEvaluation = Class(name="TracedLiteralEvaluation")
umlTrace_Kernel_TracedBooleanValue = Class(name="umlTrace_Kernel_TracedBooleanValue")
umlTrace_Kernel_TracedLiteralIntegerEvaluation = Class(name="umlTrace_Kernel_TracedLiteralIntegerEvaluation")
umlTrace_Values_ActionActivation_firing_Value = Class(name="umlTrace_Values_ActionActivation_firing_Value")
BasicActions_TracedActionActivation = Class(name="BasicActions_TracedActionActivation")
uml_ActivityContent = Class(name="uml_ActivityContent", is_abstract=True)

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

# uml_TracedCreateObjectAction class attributes and methods

# uml_TracedLifeline class attributes and methods

# IntermediateActivities_TracedForkNodeActivation class attributes and methods

# uml_TracedDurationConstraint class attributes and methods

# uml_TracedDestructionOccurrenceSpecification class attributes and methods

# uml_TracedConnector class attributes and methods

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

# uml_TracedValuePin class attributes and methods

# uml_TracedNode class attributes and methods

# uml_TracedExceptionHandler class attributes and methods

# uml_TracedSequenceNode class attributes and methods

# uml_TracedStartClassifierBehaviorAction class attributes and methods

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

# uml_TracedClearVariableAction class attributes and methods

# uml_TracedConstraint class attributes and methods

# uml_TracedBroadcastSignalAction class attributes and methods

# uml_TracedInteraction class attributes and methods

# IntermediateActivities_TracedActivityNodeActivation class attributes and methods

# uml_TracedParameter class attributes and methods

# uml_TracedOpaqueExpression class attributes and methods

# uml_TracedLiteralString class attributes and methods

# BasicActions_TracedInputPinActivation class attributes and methods

# uml_TracedStateInvariant class attributes and methods

# IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution class attributes and methods

# uml_TracedInstanceSpecification class attributes and methods

# uml_TracedAcceptCallAction class attributes and methods

# uml_TracedStereotype class attributes and methods

# uml_TracedEnumerationLiteral class attributes and methods

# uml_TracedSubstitution class attributes and methods

# uml_TracedInformationFlow class attributes and methods

# uml_TracedAssociationClass class attributes and methods

# uml_TracedDestroyObjectAction class attributes and methods

# BasicActions_TracedCallBehaviorActionActivation class attributes and methods

# IntermediateActivities_TracedActivityParameterNodeActivation class attributes and methods

# uml_TracedActivityPartition class attributes and methods

# uml_TracedStateMachine class attributes and methods

# uml_TracedMessage class attributes and methods

# uml_TracedActivity class attributes and methods

# uml_TracedForkNode class attributes and methods

# Kernel_TracedReference class attributes and methods

# IntermediateActions_TracedAddStructuralFeatureValueActionActivation class attributes and methods

# uml_TracedInstanceValue class attributes and methods

# uml_TracedReclassifyObjectAction class attributes and methods

# uml_TracedUseCase class attributes and methods

# IntermediateActivities_TracedJoinNodeActivation class attributes and methods

# Kernel_TracedObject class attributes and methods

# Loci_TracedSemanticVisitor class attributes and methods

# uml_TracedDeployment class attributes and methods

# uml_TracedTimeEvent class attributes and methods

# uml_TracedPartDecomposition class attributes and methods

# uml_TracedInterruptibleActivityRegion class attributes and methods

# uml_TracedProtocolTransition class attributes and methods

# uml_TracedInteractionOperand class attributes and methods

# uml_TracedGeneralization class attributes and methods

# uml_TracedRemoveStructuralFeatureValueAction class attributes and methods

# uml_TracedInterval class attributes and methods

# Kernel_TracedIntegerValue class attributes and methods

# uml_TracedAnyReceiveEvent class attributes and methods

# uml_TracedReadStructuralFeatureAction class attributes and methods

# uml_TracedDataStoreNode class attributes and methods

# uml_TracedProtocolStateMachine class attributes and methods

# uml_TracedReception class attributes and methods

# uml_TracedMessageOccurrenceSpecification class attributes and methods

# uml_TracedTemplateBinding class attributes and methods

# uml_TracedDeploymentSpecification class attributes and methods

# uml_TracedUsage class attributes and methods

# uml_TracedActionInputPin class attributes and methods

# uml_TracedReadVariableAction class attributes and methods

# IntermediateActivities_TracedActivityFinalNodeActivation class attributes and methods

# uml_TracedDestroyLinkAction class attributes and methods

# uml_TracedLiteralInteger class attributes and methods

# uml_TracedSignalEvent class attributes and methods

# Kernel_TracedBooleanValue class attributes and methods

# uml_TracedConditionalNode class attributes and methods

# uml_TracedConnectionPointReference class attributes and methods

# uml_TracedRealization class attributes and methods

# uml_TracedReadLinkObjectEndQualifierAction class attributes and methods

# BasicActions_TracedOpaqueActionActivation class attributes and methods

# uml_TracedJoinNode class attributes and methods

# uml_TracedRedefinableTemplateSignature class attributes and methods

# uml_TracedModel class attributes and methods

# uml_TracedCentralBufferNode class attributes and methods

# Kernel_TracedLiteralIntegerEvaluation class attributes and methods

# uml_TracedCreateLinkAction class attributes and methods

# uml_TracedExtensionPoint class attributes and methods

# uml_TracedSignal class attributes and methods

# uml_TracedExecutionOccurrenceSpecification class attributes and methods

# uml_TracedTimeInterval class attributes and methods

# uml_TracedInteractionConstraint class attributes and methods

# IntermediateActivities_TracedDecisionNodeActivation class attributes and methods

# uml_TracedInterface class attributes and methods

# uml_TracedOpaqueBehavior class attributes and methods

# uml_TracedProtocolConformance class attributes and methods

# uml_TracedPackage class attributes and methods

# uml_TracedCallEvent class attributes and methods

# uml_TracedLoopNode class attributes and methods

# uml_TracedComment class attributes and methods

# uml_TracedDataType class attributes and methods

# uml_TracedComponentRealization class attributes and methods

# uml_TracedAcceptEventAction class attributes and methods

# uml_TracedOccurrenceSpecification class attributes and methods

# uml_TracedParameterSet class attributes and methods

# uml_TracedObjectFlow class attributes and methods

# uml_TracedOperation class attributes and methods

# uml_TracedReadSelfAction class attributes and methods

# IntermediateActions_TracedReadStructuralFeatureActionActivation class attributes and methods

# uml_TracedDecisionNode class attributes and methods

# uml_TracedPackageMerge class attributes and methods

# uml_TracedClause class attributes and methods

# uml_TracedReplyAction class attributes and methods

# uml_TracedTrigger class attributes and methods

# uml_TracedTransition class attributes and methods

# uml_TracedDurationInterval class attributes and methods

# uml_TracedLinkEndData class attributes and methods

# uml_TracedConnectableElementTemplateParameter class attributes and methods

# uml_TracedOperationTemplateParameter class attributes and methods

# uml_TracedInformationItem class attributes and methods

# uml_TracedActionExecutionSpecification class attributes and methods

# uml_TracedOutputPin class attributes and methods

# uml_TracedTemplateParameterSubstitution class attributes and methods

# uml_TracedDuration class attributes and methods

# uml_TracedReduceAction class attributes and methods

# uml_TracedFinalState class attributes and methods

# uml_TracedOpaqueAction class attributes and methods

# uml_TracedDevice class attributes and methods

# uml_TracedProperty class attributes and methods

# uml_TracedExtensionEnd class attributes and methods

# uml_TracedImage class attributes and methods

# uml_TracedQualifierValue class attributes and methods

# uml_TracedAddStructuralFeatureValueAction class attributes and methods

# uml_TracedProfileApplication class attributes and methods

# uml_TracedExpansionNode class attributes and methods

# uml_TracedActivityParameterNode class attributes and methods

# uml_TracedBehaviorExecutionSpecification class attributes and methods

# uml_TracedDurationObservation class attributes and methods

# uml_TracedLiteralUnlimitedNatural class attributes and methods

# uml_TracedCallOperationAction class attributes and methods

# uml_TracedArtifact class attributes and methods

# uml_TracedConnectorEnd class attributes and methods

# uml_TracedVariable class attributes and methods

# uml_TracedCallBehaviorAction class attributes and methods

# uml_TracedReadLinkObjectEndAction class attributes and methods

# uml_TracedEnumeration class attributes and methods

# Kernel_TracedLiteralBooleanEvaluation class attributes and methods

# uml_TracedCommunicationPath class attributes and methods

# uml_TracedRaiseExceptionAction class attributes and methods

# uml_TracedTemplateSignature class attributes and methods

# BasicActions_TracedOutputPinActivation class attributes and methods

# uml_TracedReadExtentAction class attributes and methods

# uml_TracedLinkEndDestructionData class attributes and methods

# uml_TracedStringExpression class attributes and methods

# uml_TracedPrimitiveType class attributes and methods

# uml_TracedState class attributes and methods

# uml_TracedRegion class attributes and methods

# uml_TracedInclude class attributes and methods

# uml_TracedReadLinkAction class attributes and methods

# uml_TracedLiteralBoolean class attributes and methods

# uml_TracedStartObjectBehaviorAction class attributes and methods

# IntermediateActions_TracedValueSpecificationActionActivation class attributes and methods

# uml_TracedLiteralNull class attributes and methods

# uml_TracedSlot class attributes and methods

# IntermediateActions_TracedCreateObjectActionActivation class attributes and methods

# uml_TracedLiteralReal class attributes and methods

# uml_TracedAddVariableValueAction class attributes and methods

# uml_TracedClearStructuralFeatureAction class attributes and methods

# uml_TracedAssociation class attributes and methods

# uml_TracedExpression class attributes and methods

# uml_TracedUnmarshallAction class attributes and methods

# uml_TracedInterfaceRealization class attributes and methods

# uml_TracedSendSignalAction class attributes and methods

# uml_TracedCollaboration class attributes and methods

# uml_TracedTestIdentityAction class attributes and methods

# uml_TracedProfile class attributes and methods

# uml_TracedRemoveVariableValueAction class attributes and methods

# uml_TracedActor class attributes and methods

# uml_TracedManifestation class attributes and methods

# uml_TracedTemplateParameter class attributes and methods

# IntermediateActivities_TracedMergeNodeActivation class attributes and methods

# IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution class attributes and methods

# uml_TracedFunctionBehavior class attributes and methods

# uml_TracedValueSpecificationAction class attributes and methods

# uml_TracedTimeExpression class attributes and methods

# uml_TracedAbstraction class attributes and methods

# uml_TracedReadIsClassifiedObjectAction class attributes and methods

# uml_TracedComponent class attributes and methods

# uml_TracedPseudostate class attributes and methods

# uml_TracedLinkEndCreationData class attributes and methods

# uml_TracedClearAssociationAction class attributes and methods

# uml_TracedMergeNode class attributes and methods

# uml_TracedElementImport class attributes and methods

# uml_TracedGeneralOrdering class attributes and methods

# umlTrace_uml_TracedCombinedFragment class attributes and methods

# TracedInteractionFragment class attributes and methods

# uml_TracedClassifierTemplateParameter class attributes and methods

# uml_TracedActivityFinalNode class attributes and methods

# uml_TracedGate class attributes and methods

# uml_TracedTimeObservation class attributes and methods

# uml_TracedControlFlow class attributes and methods

# umlTrace_uml_TracedDurationConstraint class attributes and methods

# TracedIntervalConstraint class attributes and methods

# umlTrace_uml_TracedIntervalConstraint class attributes and methods

# TracedConstraint class attributes and methods

# umlTrace_uml_TracedConstraint class attributes and methods

# TracedPackageableElement class attributes and methods

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

# umlTrace_uml_TracedObservation class attributes and methods

# umlTrace_uml_TracedInteractionUse class attributes and methods

# umlTrace_uml_TracedLoopNode class attributes and methods

# umlTrace_uml_TracedSignal class attributes and methods

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

# umlTrace_uml_TracedExtension class attributes and methods

# TracedAssociation class attributes and methods

# umlTrace_uml_TracedAssociation class attributes and methods

# uml_TracedRelationship class attributes and methods

# umlTrace_uml_TracedExecutionEnvironment class attributes and methods

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

# umlTrace_uml_TracedInteraction class attributes and methods

# uml_TracedBehavior class attributes and methods

# uml_TracedInteractionFragment class attributes and methods

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

# umlTrace_uml_TracedRealization class attributes and methods

# TracedAbstraction class attributes and methods

# umlTrace_uml_TracedAbstraction class attributes and methods

# TracedDependency class attributes and methods

# umlTrace_uml_TracedExecutionSpecification class attributes and methods

# umlTrace_uml_TracedReplyAction class attributes and methods

# umlTrace_uml_TracedActor class attributes and methods

# umlTrace_uml_TracedReception class attributes and methods

# TracedBehavioralFeature class attributes and methods

# umlTrace_uml_TracedTemplateBinding class attributes and methods

# umlTrace_uml_TracedUsage class attributes and methods

# umlTrace_uml_TracedActionInputPin class attributes and methods

# umlTrace_uml_TracedReadVariableAction class attributes and methods

# umlTrace_uml_TracedDestroyLinkAction class attributes and methods

# umlTrace_uml_TracedLiteralInteger class attributes and methods

# umlTrace_uml_TracedSignalEvent class attributes and methods

# umlTrace_uml_TracedReadLinkObjectEndAction class attributes and methods

# umlTrace_uml_TracedTimeInterval class attributes and methods

# TracedInterval class attributes and methods

# umlTrace_uml_TracedOperationTemplateParameter class attributes and methods

# umlTrace_uml_TracedDurationObservation class attributes and methods

# TracedObservation class attributes and methods

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

# umlTrace_uml_TracedConnectableElementTemplateParameter class attributes and methods

# umlTrace_uml_TracedActionExecutionSpecification class attributes and methods

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

# umlTrace_IntermediateActivities_TracedForkNodeActivation class attributes and methods

# TracedControlNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedControlNodeActivation class attributes and methods

# TracedActivityNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityNodeActivation class attributes and methods

# TracedSemanticVisitor class attributes and methods

# umlTrace_IntermediateActivities_TracedObjectNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedInitialNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityExecution class attributes and methods

# TracedExecution class attributes and methods

# umlTrace_IntermediateActivities_TracedMergeNodeActivation class attributes and methods

# umlTrace_uml_TracedValueSpecificationAction class attributes and methods

# umlTrace_uml_TracedReadExtentAction class attributes and methods

# umlTrace_uml_TracedStringExpression class attributes and methods

# umlTrace_uml_TracedExpression class attributes and methods

# umlTrace_uml_TracedGeneralOrdering class attributes and methods

# umlTrace_uml_TracedLiteralBoolean class attributes and methods

# umlTrace_uml_TracedStartObjectBehaviorAction class attributes and methods

# umlTrace_uml_TracedRegion class attributes and methods

# umlTrace_uml_TracedInclude class attributes and methods

# umlTrace_uml_TracedControlFlow class attributes and methods

# umlTrace_uml_TracedGate class attributes and methods

# TracedMessageEnd class attributes and methods

# umlTrace_uml_TracedRemoveVariableValueAction class attributes and methods

# umlTrace_uml_TracedManifestation class attributes and methods

# umlTrace_uml_TracedLinkEndCreationData class attributes and methods

# umlTrace_uml_TracedMergeNode class attributes and methods

# umlTrace_ecore_TracedEModelElement class attributes and methods

# umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation class attributes and methods

# umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation class attributes and methods

# TracedStructuralFeatureActionActivation class attributes and methods

# umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation class attributes and methods

# TracedWriteStructuralFeatureActionActivation class attributes and methods

# umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation class attributes and methods

# umlTrace_IntermediateActions_TracedValueSpecificationActionActivation class attributes and methods

# umlTrace_IntermediateActions_TracedCreateObjectActionActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation class attributes and methods

# TracedObjectNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedJoinNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedDecisionNodeActivation class attributes and methods

# umlTrace_Loci_TracedSemanticVisitor class attributes and methods

# umlTrace_BasicActions_TracedPinActivation class attributes and methods

# umlTrace_BasicActions_TracedActionActivation class attributes and methods

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

# umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution class attributes and methods

# TracedOpaqueBehaviorExecution class attributes and methods

# umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution class attributes and methods

# umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution class attributes and methods

# umlTrace_Values_SemanticVisitor_runtimeModelElement_Value class attributes and methods

# uml_TracedElement class attributes and methods

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

# umlTrace_Kernel_TracedPrimitiveValue class attributes and methods

# umlTrace_Kernel_TracedLiteralBooleanEvaluation class attributes and methods

# TracedLiteralEvaluation class attributes and methods

# umlTrace_Kernel_TracedBooleanValue class attributes and methods

# umlTrace_Kernel_TracedLiteralIntegerEvaluation class attributes and methods

# umlTrace_Values_ActionActivation_firing_Value class attributes and methods
umlTrace_Values_ActionActivation_firing_Value_firing: Property = Property(name="firing", type=StringType)
umlTrace_Values_ActionActivation_firing_Value.attributes={umlTrace_Values_ActionActivation_firing_Value_firing}

# BasicActions_TracedActionActivation class attributes and methods

# uml_ActivityContent class attributes and methods

# Relationships
actionActivation_firing_Values0: BinaryAssociation = BinaryAssociation(
    name="actionActivation_firing_Values0",
    ends={
        Property(name="ActionActivation_firing_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=Values_ActionActivation_firing_Value, multiplicity=Multiplicity(0, 9999))
    }
)
semanticVisitor_runtimeModelElement_Values1: BinaryAssociation = BinaryAssociation(
    name="semanticVisitor_runtimeModelElement_Values1",
    ends={
        Property(name="SemanticVisitor_runtimeModelElement_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states2", type=Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(0, 9999))
    }
)
statesTrace3: BinaryAssociation = BinaryAssociation(
    name="statesTrace3",
    ends={
        Property(name="State", type=umlTrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Trace", type=State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tracedObjects4: BinaryAssociation = BinaryAssociation(
    name="tracedObjects4",
    ends={
        Property(name="Traced_TracedObjects", type=umlTrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Trace5", type=Traced_TracedObjects, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
uml_tracedCombinedFragments6: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCombinedFragments6",
    ends={
        Property(name="uml_TracedCombinedFragment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects", type=uml_TracedCombinedFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCreateLinkObjectActions7: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCreateLinkObjectActions7",
    ends={
        Property(name="uml_TracedCreateLinkObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects8", type=uml_TracedCreateLinkObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInitialNodes9: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInitialNodes9",
    ends={
        Property(name="uml_TracedInitialNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects10", type=uml_TracedInitialNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedFlowFinalNodes11: BinaryAssociation = BinaryAssociation(
    name="uml_tracedFlowFinalNodes11",
    ends={
        Property(name="uml_TracedFlowFinalNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects12", type=uml_TracedFlowFinalNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExpansionRegions13: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExpansionRegions13",
    ends={
        Property(name="uml_TracedExpansionRegion", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects14", type=uml_TracedExpansionRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCreateObjectActions15: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCreateObjectActions15",
    ends={
        Property(name="uml_TracedCreateObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects16", type=uml_TracedCreateObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLifelines17: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLifelines17",
    ends={
        Property(name="uml_TracedLifeline", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects18", type=uml_TracedLifeline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurationConstraints21: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurationConstraints21",
    ends={
        Property(name="uml_TracedDurationConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects22", type=uml_TracedDurationConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDestructionOccurrenceSpecifications23: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDestructionOccurrenceSpecifications23",
    ends={
        Property(name="uml_TracedDestructionOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects24", type=uml_TracedDestructionOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectors25: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectors25",
    ends={
        Property(name="uml_TracedConnector", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects26", type=uml_TracedConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSendObjectActions27: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSendObjectActions27",
    ends={
        Property(name="uml_TracedSendObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects28", type=uml_TracedSendObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPackageImports29: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPackageImports29",
    ends={
        Property(name="uml_TracedPackageImport", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects30", type=uml_TracedPackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClasss31: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClasss31",
    ends={
        Property(name="uml_TracedClass", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects32", type=uml_TracedClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractionUses33: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractionUses33",
    ends={
        Property(name="uml_TracedInteractionUse", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects34", type=uml_TracedInteractionUse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGeneralizationSets35: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGeneralizationSets35",
    ends={
        Property(name="uml_TracedGeneralizationSet", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects36", type=uml_TracedGeneralizationSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedChangeEvents37: BinaryAssociation = BinaryAssociation(
    name="uml_tracedChangeEvents37",
    ends={
        Property(name="uml_TracedChangeEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects38", type=uml_TracedChangeEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDependencys39: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDependencys39",
    ends={
        Property(name="uml_TracedDependency", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects40", type=uml_TracedDependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPorts41: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPorts41",
    ends={
        Property(name="uml_TracedPort", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects42", type=uml_TracedPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedInitialNodeActivations43: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedInitialNodeActivations43",
    ends={
        Property(name="IntermediateActivities_TracedInitialNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects44", type=IntermediateActivities_TracedInitialNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCollaborationUses45: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCollaborationUses45",
    ends={
        Property(name="uml_TracedCollaborationUse", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects46", type=uml_TracedCollaborationUse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityExecutions47: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityExecutions47",
    ends={
        Property(name="IntermediateActivities_TracedActivityExecution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects48", type=IntermediateActivities_TracedActivityExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedValuePins49: BinaryAssociation = BinaryAssociation(
    name="uml_tracedValuePins49",
    ends={
        Property(name="uml_TracedValuePin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects50", type=uml_TracedValuePin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedNodes51: BinaryAssociation = BinaryAssociation(
    name="uml_tracedNodes51",
    ends={
        Property(name="uml_TracedNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects52", type=uml_TracedNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExceptionHandlers53: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExceptionHandlers53",
    ends={
        Property(name="uml_TracedExceptionHandler", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects54", type=uml_TracedExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSequenceNodes55: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSequenceNodes55",
    ends={
        Property(name="uml_TracedSequenceNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects56", type=uml_TracedSequenceNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStartClassifierBehaviorActions57: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStartClassifierBehaviorActions57",
    ends={
        Property(name="uml_TracedStartClassifierBehaviorAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects58", type=uml_TracedStartClassifierBehaviorAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedForkNodeActivations19: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedForkNodeActivations19",
    ends={
        Property(name="IntermediateActivities_TracedForkNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects20", type=IntermediateActivities_TracedForkNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integerFunctions_tracedIntegerPlusFunctionBehaviorExecutions61: BinaryAssociation = BinaryAssociation(
    name="integerFunctions_tracedIntegerPlusFunctionBehaviorExecutions61",
    ends={
        Property(name="IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects62", type=IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtensions63: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtensions63",
    ends={
        Property(name="uml_TracedExtension", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects64", type=uml_TracedExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStructuredActivityNodes65: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStructuredActivityNodes65",
    ends={
        Property(name="uml_TracedStructuredActivityNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects66", type=uml_TracedStructuredActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExecutionEnvironments67: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExecutionEnvironments67",
    ends={
        Property(name="uml_TracedExecutionEnvironment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects68", type=uml_TracedExecutionEnvironment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedIntervalConstraints69: BinaryAssociation = BinaryAssociation(
    name="uml_tracedIntervalConstraints69",
    ends={
        Property(name="uml_TracedIntervalConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects70", type=uml_TracedIntervalConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConsiderIgnoreFragments71: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConsiderIgnoreFragments71",
    ends={
        Property(name="uml_TracedConsiderIgnoreFragment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects72", type=uml_TracedConsiderIgnoreFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedContinuations73: BinaryAssociation = BinaryAssociation(
    name="uml_tracedContinuations73",
    ends={
        Property(name="uml_TracedContinuation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects74", type=uml_TracedContinuation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeConstraints75: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeConstraints75",
    ends={
        Property(name="uml_TracedTimeConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects76", type=uml_TracedTimeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInputPins77: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInputPins77",
    ends={
        Property(name="uml_TracedInputPin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects78", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClearVariableActions79: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClearVariableActions79",
    ends={
        Property(name="uml_TracedClearVariableAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects80", type=uml_TracedClearVariableAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConstraints81: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConstraints81",
    ends={
        Property(name="uml_TracedConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects82", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedBroadcastSignalActions83: BinaryAssociation = BinaryAssociation(
    name="uml_tracedBroadcastSignalActions83",
    ends={
        Property(name="uml_TracedBroadcastSignalAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects84", type=uml_TracedBroadcastSignalAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractions85: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractions85",
    ends={
        Property(name="uml_TracedInteraction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects86", type=uml_TracedInteraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityNodeActivations87: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityNodeActivations87",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects88", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedParameters89: BinaryAssociation = BinaryAssociation(
    name="uml_tracedParameters89",
    ends={
        Property(name="uml_TracedParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects90", type=uml_TracedParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOpaqueExpressions91: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOpaqueExpressions91",
    ends={
        Property(name="uml_TracedOpaqueExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects92", type=uml_TracedOpaqueExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralStrings93: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralStrings93",
    ends={
        Property(name="uml_TracedLiteralString", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects94", type=uml_TracedLiteralString, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtends59: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtends59",
    ends={
        Property(name="uml_TracedExtend", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects60", type=uml_TracedExtend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedInputPinActivations95: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedInputPinActivations95",
    ends={
        Property(name="BasicActions_TracedInputPinActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects96", type=BasicActions_TracedInputPinActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStateInvariants97: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStateInvariants97",
    ends={
        Property(name="uml_TracedStateInvariant", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects98", type=uml_TracedStateInvariant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integerFunctions_tracedIntegerLessFunctionBehaviorExecutions99: BinaryAssociation = BinaryAssociation(
    name="integerFunctions_tracedIntegerLessFunctionBehaviorExecutions99",
    ends={
        Property(name="IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects100", type=IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInstanceSpecifications101: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInstanceSpecifications101",
    ends={
        Property(name="uml_TracedInstanceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects102", type=uml_TracedInstanceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAcceptCallActions103: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAcceptCallActions103",
    ends={
        Property(name="uml_TracedAcceptCallAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects104", type=uml_TracedAcceptCallAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStereotypes105: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStereotypes105",
    ends={
        Property(name="uml_TracedStereotype", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects106", type=uml_TracedStereotype, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedEnumerationLiterals107: BinaryAssociation = BinaryAssociation(
    name="uml_tracedEnumerationLiterals107",
    ends={
        Property(name="uml_TracedEnumerationLiteral", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects108", type=uml_TracedEnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSubstitutions109: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSubstitutions109",
    ends={
        Property(name="uml_TracedSubstitution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects110", type=uml_TracedSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInformationFlows111: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInformationFlows111",
    ends={
        Property(name="uml_TracedInformationFlow", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects112", type=uml_TracedInformationFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAssociationClasss113: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAssociationClasss113",
    ends={
        Property(name="uml_TracedAssociationClass", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects114", type=uml_TracedAssociationClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDestroyObjectActions115: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDestroyObjectActions115",
    ends={
        Property(name="uml_TracedDestroyObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects116", type=uml_TracedDestroyObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedCallBehaviorActionActivations117: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedCallBehaviorActionActivations117",
    ends={
        Property(name="BasicActions_TracedCallBehaviorActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects118", type=BasicActions_TracedCallBehaviorActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityParameterNodeActivations119: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityParameterNodeActivations119",
    ends={
        Property(name="IntermediateActivities_TracedActivityParameterNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects120", type=IntermediateActivities_TracedActivityParameterNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActivityPartitions121: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivityPartitions121",
    ends={
        Property(name="uml_TracedActivityPartition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects122", type=uml_TracedActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStateMachines123: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStateMachines123",
    ends={
        Property(name="uml_TracedStateMachine", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects124", type=uml_TracedStateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedMessages125: BinaryAssociation = BinaryAssociation(
    name="uml_tracedMessages125",
    ends={
        Property(name="uml_TracedMessage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects126", type=uml_TracedMessage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDeployments127: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDeployments127",
    ends={
        Property(name="umlTrace_Traced_TracedObjects128", type=uml_TracedDeployment, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="uml_TracedDeployment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1))
    }
)
uml_tracedActivitys129: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivitys129",
    ends={
        Property(name="uml_TracedActivity", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects130", type=uml_TracedActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedForkNodes131: BinaryAssociation = BinaryAssociation(
    name="uml_tracedForkNodes131",
    ends={
        Property(name="uml_TracedForkNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects132", type=uml_TracedForkNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedReferences133: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedReferences133",
    ends={
        Property(name="Kernel_TracedReference", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects134", type=Kernel_TracedReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedAddStructuralFeatureValueActionActivations135: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedAddStructuralFeatureValueActionActivations135",
    ends={
        Property(name="IntermediateActions_TracedAddStructuralFeatureValueActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects136", type=IntermediateActions_TracedAddStructuralFeatureValueActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInstanceValues137: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInstanceValues137",
    ends={
        Property(name="uml_TracedInstanceValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects138", type=uml_TracedInstanceValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReclassifyObjectActions139: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReclassifyObjectActions139",
    ends={
        Property(name="uml_TracedReclassifyObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects140", type=uml_TracedReclassifyObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedUseCases141: BinaryAssociation = BinaryAssociation(
    name="uml_tracedUseCases141",
    ends={
        Property(name="uml_TracedUseCase", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects142", type=uml_TracedUseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedJoinNodeActivations143: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedJoinNodeActivations143",
    ends={
        Property(name="IntermediateActivities_TracedJoinNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects144", type=IntermediateActivities_TracedJoinNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedObjects145: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedObjects145",
    ends={
        Property(name="Kernel_TracedObject", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects146", type=Kernel_TracedObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loci_tracedSemanticVisitors147: BinaryAssociation = BinaryAssociation(
    name="loci_tracedSemanticVisitors147",
    ends={
        Property(name="Loci_TracedSemanticVisitor", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects148", type=Loci_TracedSemanticVisitor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeEvents149: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeEvents149",
    ends={
        Property(name="uml_TracedTimeEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects150", type=uml_TracedTimeEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPartDecompositions151: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPartDecompositions151",
    ends={
        Property(name="uml_TracedPartDecomposition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects152", type=uml_TracedPartDecomposition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInterruptibleActivityRegions153: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInterruptibleActivityRegions153",
    ends={
        Property(name="uml_TracedInterruptibleActivityRegion", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects154", type=uml_TracedInterruptibleActivityRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProtocolTransitions155: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProtocolTransitions155",
    ends={
        Property(name="uml_TracedProtocolTransition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects156", type=uml_TracedProtocolTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractionOperands157: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractionOperands157",
    ends={
        Property(name="uml_TracedInteractionOperand", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects158", type=uml_TracedInteractionOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGeneralizations159: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGeneralizations159",
    ends={
        Property(name="uml_TracedGeneralization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects160", type=uml_TracedGeneralization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRemoveStructuralFeatureValueActions161: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRemoveStructuralFeatureValueActions161",
    ends={
        Property(name="uml_TracedRemoveStructuralFeatureValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects162", type=uml_TracedRemoveStructuralFeatureValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedIntervals163: BinaryAssociation = BinaryAssociation(
    name="uml_tracedIntervals163",
    ends={
        Property(name="uml_TracedInterval", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects164", type=uml_TracedInterval, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedIntegerValues165: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedIntegerValues165",
    ends={
        Property(name="Kernel_TracedIntegerValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects166", type=Kernel_TracedIntegerValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAnyReceiveEvents167: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAnyReceiveEvents167",
    ends={
        Property(name="uml_TracedAnyReceiveEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects168", type=uml_TracedAnyReceiveEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadStructuralFeatureActions169: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadStructuralFeatureActions169",
    ends={
        Property(name="uml_TracedReadStructuralFeatureAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects170", type=uml_TracedReadStructuralFeatureAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDataStoreNodes171: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDataStoreNodes171",
    ends={
        Property(name="uml_TracedDataStoreNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects172", type=uml_TracedDataStoreNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProtocolStateMachines173: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProtocolStateMachines173",
    ends={
        Property(name="uml_TracedProtocolStateMachine", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects174", type=uml_TracedProtocolStateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReceptions175: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReceptions175",
    ends={
        Property(name="uml_TracedReception", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects176", type=uml_TracedReception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedMessageOccurrenceSpecifications177: BinaryAssociation = BinaryAssociation(
    name="uml_tracedMessageOccurrenceSpecifications177",
    ends={
        Property(name="uml_TracedMessageOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects178", type=uml_TracedMessageOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateBindings179: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateBindings179",
    ends={
        Property(name="uml_TracedTemplateBinding", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects180", type=uml_TracedTemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDeploymentSpecifications181: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDeploymentSpecifications181",
    ends={
        Property(name="uml_TracedDeploymentSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects182", type=uml_TracedDeploymentSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedUsages183: BinaryAssociation = BinaryAssociation(
    name="uml_tracedUsages183",
    ends={
        Property(name="uml_TracedUsage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects184", type=uml_TracedUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActionInputPins185: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActionInputPins185",
    ends={
        Property(name="uml_TracedActionInputPin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects186", type=uml_TracedActionInputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadVariableActions187: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadVariableActions187",
    ends={
        Property(name="uml_TracedReadVariableAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects188", type=uml_TracedReadVariableAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityFinalNodeActivations189: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityFinalNodeActivations189",
    ends={
        Property(name="IntermediateActivities_TracedActivityFinalNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects190", type=IntermediateActivities_TracedActivityFinalNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDestroyLinkActions191: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDestroyLinkActions191",
    ends={
        Property(name="uml_TracedDestroyLinkAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects192", type=uml_TracedDestroyLinkAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralIntegers193: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralIntegers193",
    ends={
        Property(name="uml_TracedLiteralInteger", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects194", type=uml_TracedLiteralInteger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSignalEvents195: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSignalEvents195",
    ends={
        Property(name="uml_TracedSignalEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects196", type=uml_TracedSignalEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedBooleanValues197: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedBooleanValues197",
    ends={
        Property(name="Kernel_TracedBooleanValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects198", type=Kernel_TracedBooleanValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConditionalNodes199: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConditionalNodes199",
    ends={
        Property(name="uml_TracedConditionalNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects200", type=uml_TracedConditionalNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectionPointReferences201: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectionPointReferences201",
    ends={
        Property(name="uml_TracedConnectionPointReference", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects202", type=uml_TracedConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRealizations203: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRealizations203",
    ends={
        Property(name="uml_TracedRealization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects204", type=uml_TracedRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadLinkObjectEndQualifierActions205: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadLinkObjectEndQualifierActions205",
    ends={
        Property(name="uml_TracedReadLinkObjectEndQualifierAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects206", type=uml_TracedReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedOpaqueActionActivations207: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedOpaqueActionActivations207",
    ends={
        Property(name="BasicActions_TracedOpaqueActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects208", type=BasicActions_TracedOpaqueActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedJoinNodes209: BinaryAssociation = BinaryAssociation(
    name="uml_tracedJoinNodes209",
    ends={
        Property(name="uml_TracedJoinNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects210", type=uml_TracedJoinNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRedefinableTemplateSignatures211: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRedefinableTemplateSignatures211",
    ends={
        Property(name="uml_TracedRedefinableTemplateSignature", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects212", type=uml_TracedRedefinableTemplateSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedModels213: BinaryAssociation = BinaryAssociation(
    name="uml_tracedModels213",
    ends={
        Property(name="uml_TracedModel", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects214", type=uml_TracedModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCentralBufferNodes215: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCentralBufferNodes215",
    ends={
        Property(name="uml_TracedCentralBufferNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects216", type=uml_TracedCentralBufferNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedLiteralIntegerEvaluations217: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedLiteralIntegerEvaluations217",
    ends={
        Property(name="Kernel_TracedLiteralIntegerEvaluation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects218", type=Kernel_TracedLiteralIntegerEvaluation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCreateLinkActions219: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCreateLinkActions219",
    ends={
        Property(name="uml_TracedCreateLinkAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects220", type=uml_TracedCreateLinkAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtensionPoints221: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtensionPoints221",
    ends={
        Property(name="uml_TracedExtensionPoint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects222", type=uml_TracedExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSignals223: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSignals223",
    ends={
        Property(name="uml_TracedSignal", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects224", type=uml_TracedSignal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExecutionOccurrenceSpecifications225: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExecutionOccurrenceSpecifications225",
    ends={
        Property(name="uml_TracedExecutionOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects226", type=uml_TracedExecutionOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeIntervals227: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeIntervals227",
    ends={
        Property(name="uml_TracedTimeInterval", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects228", type=uml_TracedTimeInterval, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractionConstraints229: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractionConstraints229",
    ends={
        Property(name="uml_TracedInteractionConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects230", type=uml_TracedInteractionConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedDecisionNodeActivations231: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedDecisionNodeActivations231",
    ends={
        Property(name="IntermediateActivities_TracedDecisionNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects232", type=IntermediateActivities_TracedDecisionNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInterfaces233: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInterfaces233",
    ends={
        Property(name="uml_TracedInterface", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects234", type=uml_TracedInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOpaqueBehaviors235: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOpaqueBehaviors235",
    ends={
        Property(name="uml_TracedOpaqueBehavior", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects236", type=uml_TracedOpaqueBehavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProtocolConformances237: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProtocolConformances237",
    ends={
        Property(name="uml_TracedProtocolConformance", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects238", type=uml_TracedProtocolConformance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPackages239: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPackages239",
    ends={
        Property(name="uml_TracedPackage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects240", type=uml_TracedPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCallEvents241: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCallEvents241",
    ends={
        Property(name="uml_TracedCallEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects242", type=uml_TracedCallEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLoopNodes243: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLoopNodes243",
    ends={
        Property(name="uml_TracedLoopNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects244", type=uml_TracedLoopNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedComments245: BinaryAssociation = BinaryAssociation(
    name="uml_tracedComments245",
    ends={
        Property(name="uml_TracedComment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects246", type=uml_TracedComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDataTypes247: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDataTypes247",
    ends={
        Property(name="uml_TracedDataType", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects248", type=uml_TracedDataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedComponentRealizations249: BinaryAssociation = BinaryAssociation(
    name="uml_tracedComponentRealizations249",
    ends={
        Property(name="uml_TracedComponentRealization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects250", type=uml_TracedComponentRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAcceptEventActions251: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAcceptEventActions251",
    ends={
        Property(name="uml_TracedAcceptEventAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects252", type=uml_TracedAcceptEventAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOccurrenceSpecifications253: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOccurrenceSpecifications253",
    ends={
        Property(name="uml_TracedOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects254", type=uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedParameterSets255: BinaryAssociation = BinaryAssociation(
    name="uml_tracedParameterSets255",
    ends={
        Property(name="uml_TracedParameterSet", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects256", type=uml_TracedParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedObjectFlows257: BinaryAssociation = BinaryAssociation(
    name="uml_tracedObjectFlows257",
    ends={
        Property(name="uml_TracedObjectFlow", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects258", type=uml_TracedObjectFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOperations259: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOperations259",
    ends={
        Property(name="uml_TracedOperation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects260", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadSelfActions261: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadSelfActions261",
    ends={
        Property(name="uml_TracedReadSelfAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects262", type=uml_TracedReadSelfAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedReadStructuralFeatureActionActivations263: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedReadStructuralFeatureActionActivations263",
    ends={
        Property(name="IntermediateActions_TracedReadStructuralFeatureActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects264", type=IntermediateActions_TracedReadStructuralFeatureActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDecisionNodes265: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDecisionNodes265",
    ends={
        Property(name="uml_TracedDecisionNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects266", type=uml_TracedDecisionNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPackageMerges267: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPackageMerges267",
    ends={
        Property(name="uml_TracedPackageMerge", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects268", type=uml_TracedPackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClauses269: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClauses269",
    ends={
        Property(name="uml_TracedClause", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects270", type=uml_TracedClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReplyActions271: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReplyActions271",
    ends={
        Property(name="uml_TracedReplyAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects272", type=uml_TracedReplyAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTriggers273: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTriggers273",
    ends={
        Property(name="uml_TracedTrigger", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects274", type=uml_TracedTrigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTransitions275: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTransitions275",
    ends={
        Property(name="uml_TracedTransition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects276", type=uml_TracedTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurationIntervals277: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurationIntervals277",
    ends={
        Property(name="uml_TracedDurationInterval", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects278", type=uml_TracedDurationInterval, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLinkEndDatas279: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLinkEndDatas279",
    ends={
        Property(name="uml_TracedLinkEndData", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects280", type=uml_TracedLinkEndData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectableElementTemplateParameters281: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectableElementTemplateParameters281",
    ends={
        Property(name="uml_TracedConnectableElementTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects282", type=uml_TracedConnectableElementTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOperationTemplateParameters283: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOperationTemplateParameters283",
    ends={
        Property(name="uml_TracedOperationTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects284", type=uml_TracedOperationTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInformationItems285: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInformationItems285",
    ends={
        Property(name="uml_TracedInformationItem", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects286", type=uml_TracedInformationItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActionExecutionSpecifications287: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActionExecutionSpecifications287",
    ends={
        Property(name="uml_TracedActionExecutionSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects288", type=uml_TracedActionExecutionSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOutputPins289: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOutputPins289",
    ends={
        Property(name="uml_TracedOutputPin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects290", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateParameterSubstitutions291: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateParameterSubstitutions291",
    ends={
        Property(name="uml_TracedTemplateParameterSubstitution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects292", type=uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurations293: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurations293",
    ends={
        Property(name="uml_TracedDuration", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects294", type=uml_TracedDuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReduceActions295: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReduceActions295",
    ends={
        Property(name="uml_TracedReduceAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects296", type=uml_TracedReduceAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedFinalStates297: BinaryAssociation = BinaryAssociation(
    name="uml_tracedFinalStates297",
    ends={
        Property(name="uml_TracedFinalState", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects298", type=uml_TracedFinalState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOpaqueActions299: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOpaqueActions299",
    ends={
        Property(name="uml_TracedOpaqueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects300", type=uml_TracedOpaqueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDevices301: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDevices301",
    ends={
        Property(name="uml_TracedDevice", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects302", type=uml_TracedDevice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPropertys303: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPropertys303",
    ends={
        Property(name="uml_TracedProperty", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects304", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtensionEnds305: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtensionEnds305",
    ends={
        Property(name="uml_TracedExtensionEnd", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects306", type=uml_TracedExtensionEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedImages307: BinaryAssociation = BinaryAssociation(
    name="uml_tracedImages307",
    ends={
        Property(name="uml_TracedImage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects308", type=uml_TracedImage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedQualifierValues309: BinaryAssociation = BinaryAssociation(
    name="uml_tracedQualifierValues309",
    ends={
        Property(name="uml_TracedQualifierValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects310", type=uml_TracedQualifierValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAddStructuralFeatureValueActions311: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAddStructuralFeatureValueActions311",
    ends={
        Property(name="uml_TracedAddStructuralFeatureValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects312", type=uml_TracedAddStructuralFeatureValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProfileApplications321: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProfileApplications321",
    ends={
        Property(name="uml_TracedProfileApplication", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects322", type=uml_TracedProfileApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExpansionNodes313: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExpansionNodes313",
    ends={
        Property(name="uml_TracedExpansionNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects314", type=uml_TracedExpansionNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActivityParameterNodes315: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivityParameterNodes315",
    ends={
        Property(name="uml_TracedActivityParameterNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects316", type=uml_TracedActivityParameterNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedBehaviorExecutionSpecifications317: BinaryAssociation = BinaryAssociation(
    name="uml_tracedBehaviorExecutionSpecifications317",
    ends={
        Property(name="uml_TracedBehaviorExecutionSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects318", type=uml_TracedBehaviorExecutionSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurationObservations319: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurationObservations319",
    ends={
        Property(name="uml_TracedDurationObservation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects320", type=uml_TracedDurationObservation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedEnumerations335: BinaryAssociation = BinaryAssociation(
    name="uml_tracedEnumerations335",
    ends={
        Property(name="umlTrace_Traced_TracedObjects336", type=uml_TracedEnumeration, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="uml_TracedEnumeration", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1))
    }
)
uml_tracedLiteralUnlimitedNaturals337: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralUnlimitedNaturals337",
    ends={
        Property(name="uml_TracedLiteralUnlimitedNatural", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects338", type=uml_TracedLiteralUnlimitedNatural, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCallOperationActions323: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCallOperationActions323",
    ends={
        Property(name="uml_TracedCallOperationAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects324", type=uml_TracedCallOperationAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedArtifacts325: BinaryAssociation = BinaryAssociation(
    name="uml_tracedArtifacts325",
    ends={
        Property(name="uml_TracedArtifact", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects326", type=uml_TracedArtifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectorEnds327: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectorEnds327",
    ends={
        Property(name="uml_TracedConnectorEnd", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects328", type=uml_TracedConnectorEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedVariables329: BinaryAssociation = BinaryAssociation(
    name="uml_tracedVariables329",
    ends={
        Property(name="uml_TracedVariable", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects330", type=uml_TracedVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCallBehaviorActions331: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCallBehaviorActions331",
    ends={
        Property(name="uml_TracedCallBehaviorAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects332", type=uml_TracedCallBehaviorAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadLinkObjectEndActions333: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadLinkObjectEndActions333",
    ends={
        Property(name="uml_TracedReadLinkObjectEndAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects334", type=uml_TracedReadLinkObjectEndAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedLiteralBooleanEvaluations351: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedLiteralBooleanEvaluations351",
    ends={
        Property(name="Kernel_TracedLiteralBooleanEvaluation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects352", type=Kernel_TracedLiteralBooleanEvaluation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCommunicationPaths353: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCommunicationPaths353",
    ends={
        Property(name="uml_TracedCommunicationPath", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects354", type=uml_TracedCommunicationPath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRaiseExceptionActions355: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRaiseExceptionActions355",
    ends={
        Property(name="uml_TracedRaiseExceptionAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects356", type=uml_TracedRaiseExceptionAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateSignatures339: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateSignatures339",
    ends={
        Property(name="uml_TracedTemplateSignature", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects340", type=uml_TracedTemplateSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedOutputPinActivations341: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedOutputPinActivations341",
    ends={
        Property(name="BasicActions_TracedOutputPinActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects342", type=BasicActions_TracedOutputPinActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadExtentActions343: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadExtentActions343",
    ends={
        Property(name="uml_TracedReadExtentAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects344", type=uml_TracedReadExtentAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLinkEndDestructionDatas345: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLinkEndDestructionDatas345",
    ends={
        Property(name="uml_TracedLinkEndDestructionData", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects346", type=uml_TracedLinkEndDestructionData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStringExpressions347: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStringExpressions347",
    ends={
        Property(name="uml_TracedStringExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects348", type=uml_TracedStringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPrimitiveTypes349: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPrimitiveTypes349",
    ends={
        Property(name="uml_TracedPrimitiveType", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects350", type=uml_TracedPrimitiveType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStates367: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStates367",
    ends={
        Property(name="uml_TracedState", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects368", type=uml_TracedState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRegions369: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRegions369",
    ends={
        Property(name="uml_TracedRegion", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects370", type=uml_TracedRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedIncludes371: BinaryAssociation = BinaryAssociation(
    name="uml_tracedIncludes371",
    ends={
        Property(name="uml_TracedInclude", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects372", type=uml_TracedInclude, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadLinkActions357: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadLinkActions357",
    ends={
        Property(name="uml_TracedReadLinkAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects358", type=uml_TracedReadLinkAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralBooleans359: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralBooleans359",
    ends={
        Property(name="uml_TracedLiteralBoolean", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects360", type=uml_TracedLiteralBoolean, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStartObjectBehaviorActions361: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStartObjectBehaviorActions361",
    ends={
        Property(name="uml_TracedStartObjectBehaviorAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects362", type=uml_TracedStartObjectBehaviorAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedValueSpecificationActionActivations363: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedValueSpecificationActionActivations363",
    ends={
        Property(name="IntermediateActions_TracedValueSpecificationActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects364", type=IntermediateActions_TracedValueSpecificationActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralNulls365: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralNulls365",
    ends={
        Property(name="uml_TracedLiteralNull", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects366", type=uml_TracedLiteralNull, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSlots385: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSlots385",
    ends={
        Property(name="uml_TracedSlot", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects386", type=uml_TracedSlot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedCreateObjectActionActivations387: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedCreateObjectActionActivations387",
    ends={
        Property(name="IntermediateActions_TracedCreateObjectActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects388", type=IntermediateActions_TracedCreateObjectActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralReals373: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralReals373",
    ends={
        Property(name="uml_TracedLiteralReal", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects374", type=uml_TracedLiteralReal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAddVariableValueActions375: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAddVariableValueActions375",
    ends={
        Property(name="uml_TracedAddVariableValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects376", type=uml_TracedAddVariableValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClearStructuralFeatureActions377: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClearStructuralFeatureActions377",
    ends={
        Property(name="uml_TracedClearStructuralFeatureAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects378", type=uml_TracedClearStructuralFeatureAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAssociations379: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAssociations379",
    ends={
        Property(name="uml_TracedAssociation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects380", type=uml_TracedAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExpressions381: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExpressions381",
    ends={
        Property(name="uml_TracedExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects382", type=uml_TracedExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedUnmarshallActions383: BinaryAssociation = BinaryAssociation(
    name="uml_tracedUnmarshallActions383",
    ends={
        Property(name="uml_TracedUnmarshallAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects384", type=uml_TracedUnmarshallAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInterfaceRealizations401: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInterfaceRealizations401",
    ends={
        Property(name="uml_TracedInterfaceRealization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects402", type=uml_TracedInterfaceRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSendSignalActions403: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSendSignalActions403",
    ends={
        Property(name="uml_TracedSendSignalAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects404", type=uml_TracedSendSignalAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCollaborations389: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCollaborations389",
    ends={
        Property(name="uml_TracedCollaboration", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects390", type=uml_TracedCollaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTestIdentityActions391: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTestIdentityActions391",
    ends={
        Property(name="uml_TracedTestIdentityAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects392", type=uml_TracedTestIdentityAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProfiles393: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProfiles393",
    ends={
        Property(name="uml_TracedProfile", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects394", type=uml_TracedProfile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRemoveVariableValueActions395: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRemoveVariableValueActions395",
    ends={
        Property(name="uml_TracedRemoveVariableValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects396", type=uml_TracedRemoveVariableValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActors397: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActors397",
    ends={
        Property(name="uml_TracedActor", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects398", type=uml_TracedActor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedManifestations399: BinaryAssociation = BinaryAssociation(
    name="uml_tracedManifestations399",
    ends={
        Property(name="uml_TracedManifestation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects400", type=uml_TracedManifestation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateParameters415: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateParameters415",
    ends={
        Property(name="uml_TracedTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects416", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedMergeNodeActivations417: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedMergeNodeActivations417",
    ends={
        Property(name="IntermediateActivities_TracedMergeNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects418", type=IntermediateActivities_TracedMergeNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integerFunctions_tracedIntegerGreaterFunctionBehaviorExecutions419: BinaryAssociation = BinaryAssociation(
    name="integerFunctions_tracedIntegerGreaterFunctionBehaviorExecutions419",
    ends={
        Property(name="IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects420", type=IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedFunctionBehaviors405: BinaryAssociation = BinaryAssociation(
    name="uml_tracedFunctionBehaviors405",
    ends={
        Property(name="uml_TracedFunctionBehavior", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects406", type=uml_TracedFunctionBehavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedValueSpecificationActions407: BinaryAssociation = BinaryAssociation(
    name="uml_tracedValueSpecificationActions407",
    ends={
        Property(name="uml_TracedValueSpecificationAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects408", type=uml_TracedValueSpecificationAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeExpressions409: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeExpressions409",
    ends={
        Property(name="uml_TracedTimeExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects410", type=uml_TracedTimeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAbstractions411: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAbstractions411",
    ends={
        Property(name="uml_TracedAbstraction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects412", type=uml_TracedAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadIsClassifiedObjectActions413: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadIsClassifiedObjectActions413",
    ends={
        Property(name="uml_TracedReadIsClassifiedObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects414", type=uml_TracedReadIsClassifiedObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedComponents431: BinaryAssociation = BinaryAssociation(
    name="uml_tracedComponents431",
    ends={
        Property(name="uml_TracedComponent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects432", type=uml_TracedComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPseudostates421: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPseudostates421",
    ends={
        Property(name="uml_TracedPseudostate", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects422", type=uml_TracedPseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLinkEndCreationDatas423: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLinkEndCreationDatas423",
    ends={
        Property(name="uml_TracedLinkEndCreationData", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects424", type=uml_TracedLinkEndCreationData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClearAssociationActions425: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClearAssociationActions425",
    ends={
        Property(name="uml_TracedClearAssociationAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects426", type=uml_TracedClearAssociationAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedMergeNodes427: BinaryAssociation = BinaryAssociation(
    name="uml_tracedMergeNodes427",
    ends={
        Property(name="uml_TracedMergeNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects428", type=uml_TracedMergeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedElementImports429: BinaryAssociation = BinaryAssociation(
    name="uml_tracedElementImports429",
    ends={
        Property(name="uml_TracedElementImport", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects430", type=uml_TracedElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedControlFlows441: BinaryAssociation = BinaryAssociation(
    name="uml_tracedControlFlows441",
    ends={
        Property(name="uml_TracedControlFlow", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects442", type=uml_TracedControlFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGeneralOrderings443: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGeneralOrderings443",
    ends={
        Property(name="uml_TracedGeneralOrdering", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects444", type=uml_TracedGeneralOrdering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClassifierTemplateParameters433: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClassifierTemplateParameters433",
    ends={
        Property(name="uml_TracedClassifierTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects434", type=uml_TracedClassifierTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActivityFinalNodes435: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivityFinalNodes435",
    ends={
        Property(name="uml_TracedActivityFinalNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects436", type=uml_TracedActivityFinalNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGates437: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGates437",
    ends={
        Property(name="uml_TracedGate", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects438", type=uml_TracedGate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeObservations439: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeObservations439",
    ends={
        Property(name="uml_TracedTimeObservation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects440", type=uml_TracedTimeObservation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
runtimeModelElementTrace445: BinaryAssociation = BinaryAssociation(
    name="runtimeModelElementTrace445",
    ends={
        Property(name="SemanticVisitor_runtimeModelElement_Value446", type=umlTrace_Loci_TracedSemanticVisitor, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firingTrace447: BinaryAssociation = BinaryAssociation(
    name="firingTrace447",
    ends={
        Property(name="ActionActivation_firing_Value449", type=umlTrace_BasicActions_TracedActionActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent448", type=Values_ActionActivation_firing_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
runtimeModelElement450: BinaryAssociation = BinaryAssociation(
    name="runtimeModelElement450",
    ends={
        Property(name="uml_TracedElement", type=umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_SemanticVisitor_runtimeModelElement_Value", type=uml_TracedElement, multiplicity=Multiplicity(0, 1))
    }
)
parent451: BinaryAssociation = BinaryAssociation(
    name="parent451",
    ends={
        Property(name="TracedSemanticVisitor", type=umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="runtimeModelElementTrace", type=Loci_TracedSemanticVisitor, multiplicity=Multiplicity(1, 1))
    }
)
states452: BinaryAssociation = BinaryAssociation(
    name="states452",
    ends={
        Property(name="State453", type=umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="semanticVisitor_runtimeModelElement_Values", type=State, multiplicity=Multiplicity(1, 9999))
    }
)
states454: BinaryAssociation = BinaryAssociation(
    name="states454",
    ends={
        Property(name="State455", type=umlTrace_Values_ActionActivation_firing_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="actionActivation_firing_Values", type=State, multiplicity=Multiplicity(1, 9999))
    }
)
parent456: BinaryAssociation = BinaryAssociation(
    name="parent456",
    ends={
        Property(name="TracedActionActivation", type=umlTrace_Values_ActionActivation_firing_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="firingTrace", type=BasicActions_TracedActionActivation, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_umlTrace_uml_TracedCombinedFragment_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedCombinedFragment)
gen_umlTrace_uml_TracedDurationConstraint_TracedIntervalConstraint = Generalization(general=TracedIntervalConstraint, specific=umlTrace_uml_TracedDurationConstraint)
gen_umlTrace_uml_TracedIntervalConstraint_TracedConstraint = Generalization(general=TracedConstraint, specific=umlTrace_uml_TracedIntervalConstraint)
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
gen_umlTrace_uml_TracedObservation_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedObservation)
gen_umlTrace_uml_TracedInteractionUse_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedInteractionUse)
gen_umlTrace_uml_TracedLoopNode_TracedStructuredActivityNode = Generalization(general=TracedStructuredActivityNode, specific=umlTrace_uml_TracedLoopNode)
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
gen_umlTrace_uml_TracedMessageEnd_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedMessageEnd)
gen_umlTrace_uml_TracedPackage_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedPackage)
gen_umlTrace_uml_TracedPackage_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedPackage)
gen_umlTrace_uml_TracedPackage_uml_TracedTemplateableElement = Generalization(general=uml_TracedTemplateableElement, specific=umlTrace_uml_TracedPackage)
gen_umlTrace_uml_TracedTemplateableElement_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedTemplateableElement)
gen_umlTrace_uml_TracedConnector_TracedFeature = Generalization(general=TracedFeature, specific=umlTrace_uml_TracedConnector)
gen_umlTrace_uml_TracedFeature_TracedRedefinableElement = Generalization(general=TracedRedefinableElement, specific=umlTrace_uml_TracedFeature)
gen_umlTrace_uml_TracedSendObjectAction_TracedInvocationAction = Generalization(general=TracedInvocationAction, specific=umlTrace_uml_TracedSendObjectAction)
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
gen_umlTrace_uml_TracedReadLinkAction_TracedLinkAction = Generalization(general=TracedLinkAction, specific=umlTrace_uml_TracedReadLinkAction)
gen_umlTrace_uml_TracedExtension_TracedAssociation = Generalization(general=TracedAssociation, specific=umlTrace_uml_TracedExtension)
gen_umlTrace_uml_TracedAssociation_uml_TracedClassifier = Generalization(general=uml_TracedClassifier, specific=umlTrace_uml_TracedAssociation)
gen_umlTrace_uml_TracedAssociation_uml_TracedRelationship = Generalization(general=uml_TracedRelationship, specific=umlTrace_uml_TracedAssociation)
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
gen_umlTrace_uml_TracedInteraction_uml_TracedBehavior = Generalization(general=uml_TracedBehavior, specific=umlTrace_uml_TracedInteraction)
gen_umlTrace_uml_TracedInteraction_uml_TracedInteractionFragment = Generalization(general=uml_TracedInteractionFragment, specific=umlTrace_uml_TracedInteraction)
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
gen_umlTrace_uml_TracedRealization_TracedAbstraction = Generalization(general=TracedAbstraction, specific=umlTrace_uml_TracedRealization)
gen_umlTrace_uml_TracedAbstraction_TracedDependency = Generalization(general=TracedDependency, specific=umlTrace_uml_TracedAbstraction)
gen_umlTrace_uml_TracedExecutionSpecification_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedExecutionSpecification)
gen_umlTrace_uml_TracedReplyAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReplyAction)
gen_umlTrace_uml_TracedActor_TracedBehavioredClassifier = Generalization(general=TracedBehavioredClassifier, specific=umlTrace_uml_TracedActor)
gen_umlTrace_uml_TracedReception_TracedBehavioralFeature = Generalization(general=TracedBehavioralFeature, specific=umlTrace_uml_TracedReception)
gen_umlTrace_uml_TracedTemplateBinding_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedTemplateBinding)
gen_umlTrace_uml_TracedUsage_TracedDependency = Generalization(general=TracedDependency, specific=umlTrace_uml_TracedUsage)
gen_umlTrace_uml_TracedActionInputPin_TracedInputPin = Generalization(general=TracedInputPin, specific=umlTrace_uml_TracedActionInputPin)
gen_umlTrace_uml_TracedReadVariableAction_TracedVariableAction = Generalization(general=TracedVariableAction, specific=umlTrace_uml_TracedReadVariableAction)
gen_umlTrace_uml_TracedDestroyLinkAction_TracedWriteLinkAction = Generalization(general=TracedWriteLinkAction, specific=umlTrace_uml_TracedDestroyLinkAction)
gen_umlTrace_uml_TracedLiteralInteger_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralInteger)
gen_umlTrace_uml_TracedSignalEvent_TracedMessageEvent = Generalization(general=TracedMessageEvent, specific=umlTrace_uml_TracedSignalEvent)
gen_umlTrace_uml_TracedReadLinkObjectEndAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadLinkObjectEndAction)
gen_umlTrace_uml_TracedTimeInterval_TracedInterval = Generalization(general=TracedInterval, specific=umlTrace_uml_TracedTimeInterval)
gen_umlTrace_uml_TracedOperationTemplateParameter_TracedTemplateParameter = Generalization(general=TracedTemplateParameter, specific=umlTrace_uml_TracedOperationTemplateParameter)
gen_umlTrace_uml_TracedDurationObservation_TracedObservation = Generalization(general=TracedObservation, specific=umlTrace_uml_TracedDurationObservation)
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
gen_umlTrace_uml_TracedConnectableElementTemplateParameter_TracedTemplateParameter = Generalization(general=TracedTemplateParameter, specific=umlTrace_uml_TracedConnectableElementTemplateParameter)
gen_umlTrace_uml_TracedActionExecutionSpecification_TracedExecutionSpecification = Generalization(general=TracedExecutionSpecification, specific=umlTrace_uml_TracedActionExecutionSpecification)
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
gen_umlTrace_IntermediateActivities_TracedForkNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedForkNodeActivation)
gen_umlTrace_IntermediateActivities_TracedControlNodeActivation_TracedActivityNodeActivation = Generalization(general=TracedActivityNodeActivation, specific=umlTrace_IntermediateActivities_TracedControlNodeActivation)
gen_umlTrace_IntermediateActivities_TracedActivityNodeActivation_TracedSemanticVisitor = Generalization(general=TracedSemanticVisitor, specific=umlTrace_IntermediateActivities_TracedActivityNodeActivation)
gen_umlTrace_IntermediateActivities_TracedObjectNodeActivation_TracedActivityNodeActivation = Generalization(general=TracedActivityNodeActivation, specific=umlTrace_IntermediateActivities_TracedObjectNodeActivation)
gen_umlTrace_IntermediateActivities_TracedInitialNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedInitialNodeActivation)
gen_umlTrace_IntermediateActivities_TracedActivityExecution_TracedExecution = Generalization(general=TracedExecution, specific=umlTrace_IntermediateActivities_TracedActivityExecution)
gen_umlTrace_IntermediateActivities_TracedMergeNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedMergeNodeActivation)
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
gen_umlTrace_uml_TracedInclude_uml_TracedNamedElement = Generalization(general=uml_TracedNamedElement, specific=umlTrace_uml_TracedInclude)
gen_umlTrace_uml_TracedInclude_uml_TracedDirectedRelationship = Generalization(general=uml_TracedDirectedRelationship, specific=umlTrace_uml_TracedInclude)
gen_umlTrace_uml_TracedControlFlow_TracedActivityEdge = Generalization(general=TracedActivityEdge, specific=umlTrace_uml_TracedControlFlow)
gen_umlTrace_uml_TracedGate_TracedMessageEnd = Generalization(general=TracedMessageEnd, specific=umlTrace_uml_TracedGate)
gen_umlTrace_uml_TracedRemoveVariableValueAction_TracedWriteVariableAction = Generalization(general=TracedWriteVariableAction, specific=umlTrace_uml_TracedRemoveVariableValueAction)
gen_umlTrace_uml_TracedManifestation_TracedAbstraction = Generalization(general=TracedAbstraction, specific=umlTrace_uml_TracedManifestation)
gen_umlTrace_uml_TracedLinkEndCreationData_TracedLinkEndData = Generalization(general=TracedLinkEndData, specific=umlTrace_uml_TracedLinkEndCreationData)
gen_umlTrace_uml_TracedMergeNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedMergeNode)
gen_umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation)
gen_umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation = Generalization(general=TracedStructuralFeatureActionActivation, specific=umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation)
gen_umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation_TracedWriteStructuralFeatureActionActivation = Generalization(general=TracedWriteStructuralFeatureActionActivation, specific=umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation)
gen_umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation = Generalization(general=TracedStructuralFeatureActionActivation, specific=umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation)
gen_umlTrace_IntermediateActions_TracedValueSpecificationActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_IntermediateActions_TracedValueSpecificationActionActivation)
gen_umlTrace_IntermediateActions_TracedCreateObjectActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_IntermediateActions_TracedCreateObjectActionActivation)
gen_umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation_TracedObjectNodeActivation = Generalization(general=TracedObjectNodeActivation, specific=umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation)
gen_umlTrace_IntermediateActivities_TracedJoinNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedJoinNodeActivation)
gen_umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation)
gen_umlTrace_IntermediateActivities_TracedDecisionNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedDecisionNodeActivation)
gen_umlTrace_BasicActions_TracedPinActivation_TracedObjectNodeActivation = Generalization(general=TracedObjectNodeActivation, specific=umlTrace_BasicActions_TracedPinActivation)
gen_umlTrace_BasicActions_TracedActionActivation_TracedActivityNodeActivation = Generalization(general=TracedActivityNodeActivation, specific=umlTrace_BasicActions_TracedActionActivation)
gen_umlTrace_BasicActions_TracedInvocationActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_BasicActions_TracedInvocationActionActivation)
gen_umlTrace_BasicActions_TracedCallActionActivation_TracedInvocationActionActivation = Generalization(general=TracedInvocationActionActivation, specific=umlTrace_BasicActions_TracedCallActionActivation)
gen_umlTrace_BasicActions_TracedOpaqueActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_BasicActions_TracedOpaqueActionActivation)
gen_umlTrace_BasicActions_TracedInputPinActivation_TracedPinActivation = Generalization(general=TracedPinActivation, specific=umlTrace_BasicActions_TracedInputPinActivation)
gen_umlTrace_BasicActions_TracedCallBehaviorActionActivation_TracedCallActionActivation = Generalization(general=TracedCallActionActivation, specific=umlTrace_BasicActions_TracedCallBehaviorActionActivation)
gen_umlTrace_BasicActions_TracedOutputPinActivation_TracedPinActivation = Generalization(general=TracedPinActivation, specific=umlTrace_BasicActions_TracedOutputPinActivation)
gen_umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_TracedOpaqueBehaviorExecution = Generalization(general=TracedOpaqueBehaviorExecution, specific=umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution)
gen_umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_TracedOpaqueBehaviorExecution = Generalization(general=TracedOpaqueBehaviorExecution, specific=umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution)
gen_umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_TracedOpaqueBehaviorExecution = Generalization(general=TracedOpaqueBehaviorExecution, specific=umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution)
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
gen_umlTrace_Kernel_TracedIntegerValue_TracedPrimitiveValue = Generalization(general=TracedPrimitiveValue, specific=umlTrace_Kernel_TracedIntegerValue)
gen_umlTrace_Kernel_TracedPrimitiveValue_TracedValue = Generalization(general=TracedValue, specific=umlTrace_Kernel_TracedPrimitiveValue)
gen_umlTrace_Kernel_TracedLiteralBooleanEvaluation_TracedLiteralEvaluation = Generalization(general=TracedLiteralEvaluation, specific=umlTrace_Kernel_TracedLiteralBooleanEvaluation)
gen_umlTrace_Kernel_TracedBooleanValue_TracedPrimitiveValue = Generalization(general=TracedPrimitiveValue, specific=umlTrace_Kernel_TracedBooleanValue)
gen_umlTrace_Kernel_TracedLiteralIntegerEvaluation_TracedLiteralEvaluation = Generalization(general=TracedLiteralEvaluation, specific=umlTrace_Kernel_TracedLiteralIntegerEvaluation)

# Domain Model
domain_model = DomainModel(
    name="ecore",
    types={umlTrace_State, Values_ActionActivation_firing_Value, Values_SemanticVisitor_runtimeModelElement_Value, umlTrace_Trace, State, Traced_TracedObjects, umlTrace_Traced_TracedObjects, uml_TracedCombinedFragment, uml_TracedCreateLinkObjectAction, uml_TracedInitialNode, uml_TracedFlowFinalNode, uml_TracedExpansionRegion, uml_TracedCreateObjectAction, uml_TracedLifeline, IntermediateActivities_TracedForkNodeActivation, uml_TracedDurationConstraint, uml_TracedDestructionOccurrenceSpecification, uml_TracedConnector, uml_TracedSendObjectAction, uml_TracedPackageImport, uml_TracedClass, uml_TracedInteractionUse, uml_TracedGeneralizationSet, uml_TracedChangeEvent, uml_TracedDependency, uml_TracedPort, IntermediateActivities_TracedInitialNodeActivation, uml_TracedCollaborationUse, IntermediateActivities_TracedActivityExecution, uml_TracedValuePin, uml_TracedNode, uml_TracedExceptionHandler, uml_TracedSequenceNode, uml_TracedStartClassifierBehaviorAction, uml_TracedExtend, IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution, uml_TracedExtension, uml_TracedStructuredActivityNode, uml_TracedExecutionEnvironment, uml_TracedIntervalConstraint, uml_TracedConsiderIgnoreFragment, uml_TracedContinuation, uml_TracedTimeConstraint, uml_TracedInputPin, uml_TracedClearVariableAction, uml_TracedConstraint, uml_TracedBroadcastSignalAction, uml_TracedInteraction, IntermediateActivities_TracedActivityNodeActivation, uml_TracedParameter, uml_TracedOpaqueExpression, uml_TracedLiteralString, BasicActions_TracedInputPinActivation, uml_TracedStateInvariant, IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution, uml_TracedInstanceSpecification, uml_TracedAcceptCallAction, uml_TracedStereotype, uml_TracedEnumerationLiteral, uml_TracedSubstitution, uml_TracedInformationFlow, uml_TracedAssociationClass, uml_TracedDestroyObjectAction, BasicActions_TracedCallBehaviorActionActivation, IntermediateActivities_TracedActivityParameterNodeActivation, uml_TracedActivityPartition, uml_TracedStateMachine, uml_TracedMessage, uml_TracedActivity, uml_TracedForkNode, Kernel_TracedReference, IntermediateActions_TracedAddStructuralFeatureValueActionActivation, uml_TracedInstanceValue, uml_TracedReclassifyObjectAction, uml_TracedUseCase, IntermediateActivities_TracedJoinNodeActivation, Kernel_TracedObject, Loci_TracedSemanticVisitor, uml_TracedDeployment, uml_TracedTimeEvent, uml_TracedPartDecomposition, uml_TracedInterruptibleActivityRegion, uml_TracedProtocolTransition, uml_TracedInteractionOperand, uml_TracedGeneralization, uml_TracedRemoveStructuralFeatureValueAction, uml_TracedInterval, Kernel_TracedIntegerValue, uml_TracedAnyReceiveEvent, uml_TracedReadStructuralFeatureAction, uml_TracedDataStoreNode, uml_TracedProtocolStateMachine, uml_TracedReception, uml_TracedMessageOccurrenceSpecification, uml_TracedTemplateBinding, uml_TracedDeploymentSpecification, uml_TracedUsage, uml_TracedActionInputPin, uml_TracedReadVariableAction, IntermediateActivities_TracedActivityFinalNodeActivation, uml_TracedDestroyLinkAction, uml_TracedLiteralInteger, uml_TracedSignalEvent, Kernel_TracedBooleanValue, uml_TracedConditionalNode, uml_TracedConnectionPointReference, uml_TracedRealization, uml_TracedReadLinkObjectEndQualifierAction, BasicActions_TracedOpaqueActionActivation, uml_TracedJoinNode, uml_TracedRedefinableTemplateSignature, uml_TracedModel, uml_TracedCentralBufferNode, Kernel_TracedLiteralIntegerEvaluation, uml_TracedCreateLinkAction, uml_TracedExtensionPoint, uml_TracedSignal, uml_TracedExecutionOccurrenceSpecification, uml_TracedTimeInterval, uml_TracedInteractionConstraint, IntermediateActivities_TracedDecisionNodeActivation, uml_TracedInterface, uml_TracedOpaqueBehavior, uml_TracedProtocolConformance, uml_TracedPackage, uml_TracedCallEvent, uml_TracedLoopNode, uml_TracedComment, uml_TracedDataType, uml_TracedComponentRealization, uml_TracedAcceptEventAction, uml_TracedOccurrenceSpecification, uml_TracedParameterSet, uml_TracedObjectFlow, uml_TracedOperation, uml_TracedReadSelfAction, IntermediateActions_TracedReadStructuralFeatureActionActivation, uml_TracedDecisionNode, uml_TracedPackageMerge, uml_TracedClause, uml_TracedReplyAction, uml_TracedTrigger, uml_TracedTransition, uml_TracedDurationInterval, uml_TracedLinkEndData, uml_TracedConnectableElementTemplateParameter, uml_TracedOperationTemplateParameter, uml_TracedInformationItem, uml_TracedActionExecutionSpecification, uml_TracedOutputPin, uml_TracedTemplateParameterSubstitution, uml_TracedDuration, uml_TracedReduceAction, uml_TracedFinalState, uml_TracedOpaqueAction, uml_TracedDevice, uml_TracedProperty, uml_TracedExtensionEnd, uml_TracedImage, uml_TracedQualifierValue, uml_TracedAddStructuralFeatureValueAction, uml_TracedProfileApplication, uml_TracedExpansionNode, uml_TracedActivityParameterNode, uml_TracedBehaviorExecutionSpecification, uml_TracedDurationObservation, uml_TracedLiteralUnlimitedNatural, uml_TracedCallOperationAction, uml_TracedArtifact, uml_TracedConnectorEnd, uml_TracedVariable, uml_TracedCallBehaviorAction, uml_TracedReadLinkObjectEndAction, uml_TracedEnumeration, Kernel_TracedLiteralBooleanEvaluation, uml_TracedCommunicationPath, uml_TracedRaiseExceptionAction, uml_TracedTemplateSignature, BasicActions_TracedOutputPinActivation, uml_TracedReadExtentAction, uml_TracedLinkEndDestructionData, uml_TracedStringExpression, uml_TracedPrimitiveType, uml_TracedState, uml_TracedRegion, uml_TracedInclude, uml_TracedReadLinkAction, uml_TracedLiteralBoolean, uml_TracedStartObjectBehaviorAction, IntermediateActions_TracedValueSpecificationActionActivation, uml_TracedLiteralNull, uml_TracedSlot, IntermediateActions_TracedCreateObjectActionActivation, uml_TracedLiteralReal, uml_TracedAddVariableValueAction, uml_TracedClearStructuralFeatureAction, uml_TracedAssociation, uml_TracedExpression, uml_TracedUnmarshallAction, uml_TracedInterfaceRealization, uml_TracedSendSignalAction, uml_TracedCollaboration, uml_TracedTestIdentityAction, uml_TracedProfile, uml_TracedRemoveVariableValueAction, uml_TracedActor, uml_TracedManifestation, uml_TracedTemplateParameter, IntermediateActivities_TracedMergeNodeActivation, IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution, uml_TracedFunctionBehavior, uml_TracedValueSpecificationAction, uml_TracedTimeExpression, uml_TracedAbstraction, uml_TracedReadIsClassifiedObjectAction, uml_TracedComponent, uml_TracedPseudostate, uml_TracedLinkEndCreationData, uml_TracedClearAssociationAction, uml_TracedMergeNode, uml_TracedElementImport, uml_TracedGeneralOrdering, umlTrace_uml_TracedCombinedFragment, TracedInteractionFragment, uml_TracedClassifierTemplateParameter, uml_TracedActivityFinalNode, uml_TracedGate, uml_TracedTimeObservation, uml_TracedControlFlow, umlTrace_uml_TracedDurationConstraint, TracedIntervalConstraint, umlTrace_uml_TracedIntervalConstraint, TracedConstraint, umlTrace_uml_TracedConstraint, TracedPackageableElement, umlTrace_uml_TracedPackageableElement, uml_TracedParameterableElement, umlTrace_uml_TracedParameterableElement, umlTrace_uml_TracedPseudostate, TracedVertex, umlTrace_uml_TracedVertex, umlTrace_uml_TracedDestructionOccurrenceSpecification, TracedMessageOccurrenceSpecification, umlTrace_uml_TracedMessageOccurrenceSpecification, uml_TracedMessageEnd, umlTrace_uml_TracedOccurrenceSpecification, umlTrace_uml_TracedInteractionFragment, TracedNamedElement, umlTrace_uml_TracedNamedElement, TracedElement, umlTrace_uml_TracedElement, TracedEModelElement, umlTrace_uml_TracedConditionalNode, TracedStructuredActivityNode, umlTrace_uml_TracedStructuredActivityNode, uml_TracedAction, uml_TracedNamespace, uml_TracedActivityGroup, umlTrace_uml_TracedAction, TracedExecutableNode, umlTrace_uml_TracedExecutableNode, TracedActivityNode, umlTrace_uml_TracedActivityNode, uml_TracedRedefinableElement, ActivityContent, umlTrace_uml_TracedRedefinableElement, umlTrace_uml_TracedNamespace, umlTrace_uml_TracedActivityGroup, uml_TracedNamedElement, umlTrace_uml_TracedCreateLinkObjectAction, TracedCreateLinkAction, umlTrace_uml_TracedCreateLinkAction, TracedWriteLinkAction, umlTrace_uml_TracedWriteLinkAction, TracedLinkAction, umlTrace_uml_TracedLinkAction, TracedAction, umlTrace_uml_TracedInitialNode, TracedControlNode, umlTrace_uml_TracedControlNode, umlTrace_uml_TracedFlowFinalNode, TracedFinalNode, umlTrace_uml_TracedFinalNode, umlTrace_uml_TracedExpansionRegion, umlTrace_uml_TracedCreateObjectAction, umlTrace_uml_TracedLifeline, umlTrace_uml_TracedObservation, umlTrace_uml_TracedInteractionUse, umlTrace_uml_TracedLoopNode, umlTrace_uml_TracedSignal, umlTrace_uml_TracedGeneralizationSet, umlTrace_uml_TracedChangeEvent, TracedEvent, umlTrace_uml_TracedEvent, umlTrace_uml_TracedDependency, uml_TracedDirectedRelationship, umlTrace_uml_TracedPort, TracedProperty, umlTrace_uml_TracedProperty, uml_TracedStructuralFeature, uml_TracedConnectableElement, uml_TracedDeploymentTarget, umlTrace_uml_TracedMessageEnd, umlTrace_uml_TracedPackage, uml_TracedPackageableElement, uml_TracedTemplateableElement, umlTrace_uml_TracedTemplateableElement, umlTrace_uml_TracedConnector, TracedFeature, umlTrace_uml_TracedFeature, TracedRedefinableElement, umlTrace_uml_TracedSendObjectAction, TracedInvocationAction, umlTrace_uml_TracedInvocationAction, umlTrace_uml_TracedOpaqueAction, umlTrace_uml_TracedProtocolConformance, TracedDirectedRelationship, umlTrace_uml_TracedDirectedRelationship, TracedRelationship, umlTrace_uml_TracedRelationship, umlTrace_uml_TracedCallBehaviorAction, TracedCallAction, umlTrace_uml_TracedCallAction, umlTrace_uml_TracedPackageImport, umlTrace_uml_TracedClass, uml_TracedEncapsulatedClassifier, uml_TracedBehavioredClassifier, umlTrace_uml_TracedEncapsulatedClassifier, TracedStructuredClassifier, umlTrace_uml_TracedStructuredClassifier, TracedClassifier, umlTrace_uml_TracedClassifier, uml_TracedType, umlTrace_uml_TracedType, umlTrace_uml_TracedBehavioredClassifier, umlTrace_uml_TracedActivityFinalNode, TracedNode, umlTrace_uml_TracedConsiderIgnoreFragment, TracedCombinedFragment, umlTrace_uml_TracedContinuation, umlTrace_uml_TracedCallOperationAction, umlTrace_uml_TracedTimeConstraint, umlTrace_uml_TracedClearVariableAction, TracedVariableAction, umlTrace_uml_TracedVariableAction, umlTrace_uml_TracedReadSelfAction, umlTrace_uml_TracedLiteralString, TracedLiteralSpecification, umlTrace_uml_TracedLiteralSpecification, TracedValueSpecification, umlTrace_uml_TracedValueSpecification, umlTrace_uml_TracedBroadcastSignalAction, umlTrace_uml_TracedStructuralFeature, uml_TracedFeature, uml_TracedTypedElement, uml_TracedMultiplicityElement, umlTrace_uml_TracedTypedElement, umlTrace_uml_TracedMultiplicityElement, umlTrace_uml_TracedConnectableElement, umlTrace_uml_TracedDeploymentTarget, umlTrace_uml_TracedCollaborationUse, umlTrace_uml_TracedValuePin, TracedInputPin, umlTrace_uml_TracedInputPin, TracedPin, umlTrace_uml_TracedPin, uml_TracedObjectNode, umlTrace_uml_TracedObjectNode, uml_TracedActivityNode, umlTrace_uml_TracedDeploymentSpecification, TracedArtifact, umlTrace_uml_TracedArtifact, uml_TracedClassifier, uml_TracedDeployedArtifact, umlTrace_uml_TracedDeployedArtifact, umlTrace_uml_TracedTransition, umlTrace_uml_TracedNode, umlTrace_uml_TracedExceptionHandler, umlTrace_uml_TracedSequenceNode, umlTrace_uml_TracedUseCase, TracedBehavioredClassifier, umlTrace_uml_TracedStartClassifierBehaviorAction, umlTrace_uml_TracedExtend, umlTrace_uml_TracedRemoveStructuralFeatureValueAction, TracedWriteStructuralFeatureAction, umlTrace_uml_TracedWriteStructuralFeatureAction, TracedStructuralFeatureAction, umlTrace_uml_TracedStructuralFeatureAction, umlTrace_uml_TracedReadLinkAction, umlTrace_uml_TracedExtension, TracedAssociation, umlTrace_uml_TracedAssociation, uml_TracedRelationship, umlTrace_uml_TracedExecutionEnvironment, umlTrace_uml_TracedInformationFlow, umlTrace_uml_TracedDestroyObjectAction, umlTrace_uml_TracedActivityPartition, TracedActivityGroup, umlTrace_uml_TracedStateMachine, TracedBehavior, umlTrace_uml_TracedMessage, umlTrace_uml_TracedReadLinkObjectEndQualifierAction, umlTrace_uml_TracedDeployment, umlTrace_uml_TracedActivity, umlTrace_uml_TracedForkNode, umlTrace_uml_TracedProtocolStateMachine, TracedStateMachine, umlTrace_uml_TracedInterval, umlTrace_uml_TracedClearStructuralFeatureAction, umlTrace_uml_TracedObjectFlow, TracedActivityEdge, umlTrace_uml_TracedInteraction, uml_TracedBehavior, uml_TracedInteractionFragment, umlTrace_uml_TracedBehavior, TracedClass, umlTrace_uml_TracedSlot, umlTrace_uml_TracedLiteralNull, umlTrace_uml_TracedParameter, umlTrace_uml_TracedOpaqueExpression, umlTrace_uml_TracedTrigger, umlTrace_uml_TracedStateInvariant, umlTrace_uml_TracedAssociationClass, umlTrace_uml_TracedInstanceSpecification, umlTrace_uml_TracedTemplateSignature, umlTrace_uml_TracedLinkEndDestructionData, TracedLinkEndData, umlTrace_uml_TracedLinkEndData, umlTrace_uml_TracedAcceptCallAction, TracedAcceptEventAction, umlTrace_uml_TracedAcceptEventAction, umlTrace_uml_TracedReduceAction, umlTrace_uml_TracedRaiseExceptionAction, umlTrace_uml_TracedStereotype, umlTrace_uml_TracedClearAssociationAction, umlTrace_uml_TracedEnumerationLiteral, TracedInstanceSpecification, umlTrace_uml_TracedSubstitution, TracedRealization, umlTrace_uml_TracedRealization, TracedAbstraction, umlTrace_uml_TracedAbstraction, TracedDependency, umlTrace_uml_TracedExecutionSpecification, umlTrace_uml_TracedReplyAction, umlTrace_uml_TracedActor, umlTrace_uml_TracedReception, TracedBehavioralFeature, umlTrace_uml_TracedTemplateBinding, umlTrace_uml_TracedUsage, umlTrace_uml_TracedActionInputPin, umlTrace_uml_TracedReadVariableAction, umlTrace_uml_TracedDestroyLinkAction, umlTrace_uml_TracedLiteralInteger, umlTrace_uml_TracedSignalEvent, umlTrace_uml_TracedReadLinkObjectEndAction, umlTrace_uml_TracedTimeInterval, TracedInterval, umlTrace_uml_TracedOperationTemplateParameter, umlTrace_uml_TracedDurationObservation, TracedObservation, umlTrace_uml_TracedActivityEdge, umlTrace_uml_TracedTestIdentityAction, umlTrace_uml_TracedInstanceValue, umlTrace_uml_TracedLiteralUnlimitedNatural, umlTrace_uml_TracedReclassifyObjectAction, umlTrace_uml_TracedTimeEvent, umlTrace_uml_TracedPartDecomposition, TracedInteractionUse, umlTrace_uml_TracedInterruptibleActivityRegion, umlTrace_uml_TracedAddVariableValueAction, TracedWriteVariableAction, umlTrace_uml_TracedWriteVariableAction, umlTrace_uml_TracedProtocolTransition, TracedTransition, umlTrace_uml_TracedImage, umlTrace_uml_TracedLiteralReal, umlTrace_uml_TracedInteractionOperand, umlTrace_uml_TracedGeneralization, umlTrace_uml_TracedInformationItem, umlTrace_uml_TracedModel, TracedPackage, umlTrace_uml_TracedClassifierTemplateParameter, TracedTemplateParameter, umlTrace_uml_TracedTemplateParameter, umlTrace_uml_TracedOperation, uml_TracedBehavioralFeature, umlTrace_uml_TracedBehavioralFeature, umlTrace_uml_TracedAnyReceiveEvent, TracedMessageEvent, umlTrace_uml_TracedMessageEvent, umlTrace_uml_TracedPrimitiveType, TracedDataType, umlTrace_uml_TracedDataType, umlTrace_uml_TracedReadStructuralFeatureAction, umlTrace_uml_TracedParameterSet, umlTrace_uml_TracedDataStoreNode, TracedCentralBufferNode, umlTrace_uml_TracedCentralBufferNode, TracedObjectNode, umlTrace_uml_TracedSendSignalAction, umlTrace_uml_TracedConnectableElementTemplateParameter, umlTrace_uml_TracedActionExecutionSpecification, umlTrace_uml_TracedOutputPin, umlTrace_uml_TracedDuration, umlTrace_uml_TracedUnmarshallAction, umlTrace_uml_TracedProfile, umlTrace_uml_TracedExtensionEnd, umlTrace_uml_TracedExpansionNode, umlTrace_uml_TracedActivityParameterNode, umlTrace_uml_TracedProfileApplication, umlTrace_uml_TracedConnectorEnd, TracedMultiplicityElement, umlTrace_uml_TracedEnumeration, umlTrace_uml_TracedCollaboration, uml_TracedStructuredClassifier, umlTrace_uml_TracedVariable, umlTrace_uml_TracedConnectionPointReference, umlTrace_uml_TracedTimeExpression, umlTrace_uml_TracedQualifierValue, umlTrace_uml_TracedDurationInterval, umlTrace_uml_TracedFunctionBehavior, TracedOpaqueBehavior, umlTrace_uml_TracedOpaqueBehavior, umlTrace_uml_TracedInterfaceRealization, umlTrace_uml_TracedDevice, umlTrace_uml_TracedTemplateParameterSubstitution, umlTrace_uml_TracedJoinNode, umlTrace_uml_TracedRedefinableTemplateSignature, umlTrace_uml_TracedReadIsClassifiedObjectAction, umlTrace_uml_TracedTimeObservation, umlTrace_uml_TracedDecisionNode, umlTrace_uml_TracedElementImport, umlTrace_uml_TracedExtensionPoint, umlTrace_uml_TracedExecutionOccurrenceSpecification, TracedOccurrenceSpecification, umlTrace_uml_TracedInteractionConstraint, umlTrace_uml_TracedAddStructuralFeatureValueAction, umlTrace_uml_TracedInterface, umlTrace_uml_TracedComponent, umlTrace_uml_TracedCallEvent, umlTrace_uml_TracedComment, umlTrace_uml_TracedBehaviorExecutionSpecification, TracedExecutionSpecification, umlTrace_uml_TracedComponentRealization, umlTrace_uml_TracedCommunicationPath, umlTrace_uml_TracedPackageMerge, umlTrace_uml_TracedClause, umlTrace_uml_TracedFinalState, TracedState, umlTrace_uml_TracedState, uml_TracedVertex, umlTrace_IntermediateActivities_TracedForkNodeActivation, TracedControlNodeActivation, umlTrace_IntermediateActivities_TracedControlNodeActivation, TracedActivityNodeActivation, umlTrace_IntermediateActivities_TracedActivityNodeActivation, TracedSemanticVisitor, umlTrace_IntermediateActivities_TracedObjectNodeActivation, umlTrace_IntermediateActivities_TracedInitialNodeActivation, umlTrace_IntermediateActivities_TracedActivityExecution, TracedExecution, umlTrace_IntermediateActivities_TracedMergeNodeActivation, umlTrace_uml_TracedValueSpecificationAction, umlTrace_uml_TracedReadExtentAction, umlTrace_uml_TracedStringExpression, umlTrace_uml_TracedExpression, umlTrace_uml_TracedGeneralOrdering, umlTrace_uml_TracedLiteralBoolean, umlTrace_uml_TracedStartObjectBehaviorAction, umlTrace_uml_TracedRegion, umlTrace_uml_TracedInclude, umlTrace_uml_TracedControlFlow, umlTrace_uml_TracedGate, TracedMessageEnd, umlTrace_uml_TracedRemoveVariableValueAction, umlTrace_uml_TracedManifestation, umlTrace_uml_TracedLinkEndCreationData, umlTrace_uml_TracedMergeNode, umlTrace_ecore_TracedEModelElement, umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation, umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation, TracedStructuralFeatureActionActivation, umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation, TracedWriteStructuralFeatureActionActivation, umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation, umlTrace_IntermediateActions_TracedValueSpecificationActionActivation, umlTrace_IntermediateActions_TracedCreateObjectActionActivation, umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation, TracedObjectNodeActivation, umlTrace_IntermediateActivities_TracedJoinNodeActivation, umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation, umlTrace_IntermediateActivities_TracedDecisionNodeActivation, umlTrace_Loci_TracedSemanticVisitor, umlTrace_BasicActions_TracedPinActivation, umlTrace_BasicActions_TracedActionActivation, umlTrace_BasicActions_TracedInvocationActionActivation, TracedActionActivation, umlTrace_BasicActions_TracedCallActionActivation, TracedInvocationActionActivation, umlTrace_BasicActions_TracedOpaqueActionActivation, umlTrace_BasicActions_TracedInputPinActivation, TracedPinActivation, umlTrace_BasicActions_TracedCallBehaviorActionActivation, TracedCallActionActivation, umlTrace_BasicActions_TracedOutputPinActivation, umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution, TracedOpaqueBehaviorExecution, umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution, umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution, umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, uml_TracedElement, umlTrace_BasicBehaviors_TracedExecution, TracedObject, umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution, umlTrace_Kernel_TracedObject, TracedExtensionalValue, umlTrace_Kernel_TracedExtensionalValue, TracedCompoundValue, umlTrace_Kernel_TracedCompoundValue, TracedStructuredValue, umlTrace_Kernel_TracedStructuredValue, TracedValue, umlTrace_Kernel_TracedValue, umlTrace_Kernel_TracedReference, umlTrace_Kernel_TracedLiteralEvaluation, TracedEvaluation, umlTrace_Kernel_TracedEvaluation, umlTrace_Kernel_TracedIntegerValue, TracedPrimitiveValue, umlTrace_Kernel_TracedPrimitiveValue, umlTrace_Kernel_TracedLiteralBooleanEvaluation, TracedLiteralEvaluation, umlTrace_Kernel_TracedBooleanValue, umlTrace_Kernel_TracedLiteralIntegerEvaluation, umlTrace_Values_ActionActivation_firing_Value, BasicActions_TracedActionActivation, uml_ActivityContent},
    associations={actionActivation_firing_Values0, semanticVisitor_runtimeModelElement_Values1, statesTrace3, tracedObjects4, uml_tracedCombinedFragments6, uml_tracedCreateLinkObjectActions7, uml_tracedInitialNodes9, uml_tracedFlowFinalNodes11, uml_tracedExpansionRegions13, uml_tracedCreateObjectActions15, uml_tracedLifelines17, uml_tracedDurationConstraints21, uml_tracedDestructionOccurrenceSpecifications23, uml_tracedConnectors25, uml_tracedSendObjectActions27, uml_tracedPackageImports29, uml_tracedClasss31, uml_tracedInteractionUses33, uml_tracedGeneralizationSets35, uml_tracedChangeEvents37, uml_tracedDependencys39, uml_tracedPorts41, intermediateActivities_tracedInitialNodeActivations43, uml_tracedCollaborationUses45, intermediateActivities_tracedActivityExecutions47, uml_tracedValuePins49, uml_tracedNodes51, uml_tracedExceptionHandlers53, uml_tracedSequenceNodes55, uml_tracedStartClassifierBehaviorActions57, intermediateActivities_tracedForkNodeActivations19, integerFunctions_tracedIntegerPlusFunctionBehaviorExecutions61, uml_tracedExtensions63, uml_tracedStructuredActivityNodes65, uml_tracedExecutionEnvironments67, uml_tracedIntervalConstraints69, uml_tracedConsiderIgnoreFragments71, uml_tracedContinuations73, uml_tracedTimeConstraints75, uml_tracedInputPins77, uml_tracedClearVariableActions79, uml_tracedConstraints81, uml_tracedBroadcastSignalActions83, uml_tracedInteractions85, intermediateActivities_tracedActivityNodeActivations87, uml_tracedParameters89, uml_tracedOpaqueExpressions91, uml_tracedLiteralStrings93, uml_tracedExtends59, basicActions_tracedInputPinActivations95, uml_tracedStateInvariants97, integerFunctions_tracedIntegerLessFunctionBehaviorExecutions99, uml_tracedInstanceSpecifications101, uml_tracedAcceptCallActions103, uml_tracedStereotypes105, uml_tracedEnumerationLiterals107, uml_tracedSubstitutions109, uml_tracedInformationFlows111, uml_tracedAssociationClasss113, uml_tracedDestroyObjectActions115, basicActions_tracedCallBehaviorActionActivations117, intermediateActivities_tracedActivityParameterNodeActivations119, uml_tracedActivityPartitions121, uml_tracedStateMachines123, uml_tracedMessages125, uml_tracedDeployments127, uml_tracedActivitys129, uml_tracedForkNodes131, kernel_tracedReferences133, intermediateActions_tracedAddStructuralFeatureValueActionActivations135, uml_tracedInstanceValues137, uml_tracedReclassifyObjectActions139, uml_tracedUseCases141, intermediateActivities_tracedJoinNodeActivations143, kernel_tracedObjects145, loci_tracedSemanticVisitors147, uml_tracedTimeEvents149, uml_tracedPartDecompositions151, uml_tracedInterruptibleActivityRegions153, uml_tracedProtocolTransitions155, uml_tracedInteractionOperands157, uml_tracedGeneralizations159, uml_tracedRemoveStructuralFeatureValueActions161, uml_tracedIntervals163, kernel_tracedIntegerValues165, uml_tracedAnyReceiveEvents167, uml_tracedReadStructuralFeatureActions169, uml_tracedDataStoreNodes171, uml_tracedProtocolStateMachines173, uml_tracedReceptions175, uml_tracedMessageOccurrenceSpecifications177, uml_tracedTemplateBindings179, uml_tracedDeploymentSpecifications181, uml_tracedUsages183, uml_tracedActionInputPins185, uml_tracedReadVariableActions187, intermediateActivities_tracedActivityFinalNodeActivations189, uml_tracedDestroyLinkActions191, uml_tracedLiteralIntegers193, uml_tracedSignalEvents195, kernel_tracedBooleanValues197, uml_tracedConditionalNodes199, uml_tracedConnectionPointReferences201, uml_tracedRealizations203, uml_tracedReadLinkObjectEndQualifierActions205, basicActions_tracedOpaqueActionActivations207, uml_tracedJoinNodes209, uml_tracedRedefinableTemplateSignatures211, uml_tracedModels213, uml_tracedCentralBufferNodes215, kernel_tracedLiteralIntegerEvaluations217, uml_tracedCreateLinkActions219, uml_tracedExtensionPoints221, uml_tracedSignals223, uml_tracedExecutionOccurrenceSpecifications225, uml_tracedTimeIntervals227, uml_tracedInteractionConstraints229, intermediateActivities_tracedDecisionNodeActivations231, uml_tracedInterfaces233, uml_tracedOpaqueBehaviors235, uml_tracedProtocolConformances237, uml_tracedPackages239, uml_tracedCallEvents241, uml_tracedLoopNodes243, uml_tracedComments245, uml_tracedDataTypes247, uml_tracedComponentRealizations249, uml_tracedAcceptEventActions251, uml_tracedOccurrenceSpecifications253, uml_tracedParameterSets255, uml_tracedObjectFlows257, uml_tracedOperations259, uml_tracedReadSelfActions261, intermediateActions_tracedReadStructuralFeatureActionActivations263, uml_tracedDecisionNodes265, uml_tracedPackageMerges267, uml_tracedClauses269, uml_tracedReplyActions271, uml_tracedTriggers273, uml_tracedTransitions275, uml_tracedDurationIntervals277, uml_tracedLinkEndDatas279, uml_tracedConnectableElementTemplateParameters281, uml_tracedOperationTemplateParameters283, uml_tracedInformationItems285, uml_tracedActionExecutionSpecifications287, uml_tracedOutputPins289, uml_tracedTemplateParameterSubstitutions291, uml_tracedDurations293, uml_tracedReduceActions295, uml_tracedFinalStates297, uml_tracedOpaqueActions299, uml_tracedDevices301, uml_tracedPropertys303, uml_tracedExtensionEnds305, uml_tracedImages307, uml_tracedQualifierValues309, uml_tracedAddStructuralFeatureValueActions311, uml_tracedProfileApplications321, uml_tracedExpansionNodes313, uml_tracedActivityParameterNodes315, uml_tracedBehaviorExecutionSpecifications317, uml_tracedDurationObservations319, uml_tracedEnumerations335, uml_tracedLiteralUnlimitedNaturals337, uml_tracedCallOperationActions323, uml_tracedArtifacts325, uml_tracedConnectorEnds327, uml_tracedVariables329, uml_tracedCallBehaviorActions331, uml_tracedReadLinkObjectEndActions333, kernel_tracedLiteralBooleanEvaluations351, uml_tracedCommunicationPaths353, uml_tracedRaiseExceptionActions355, uml_tracedTemplateSignatures339, basicActions_tracedOutputPinActivations341, uml_tracedReadExtentActions343, uml_tracedLinkEndDestructionDatas345, uml_tracedStringExpressions347, uml_tracedPrimitiveTypes349, uml_tracedStates367, uml_tracedRegions369, uml_tracedIncludes371, uml_tracedReadLinkActions357, uml_tracedLiteralBooleans359, uml_tracedStartObjectBehaviorActions361, intermediateActions_tracedValueSpecificationActionActivations363, uml_tracedLiteralNulls365, uml_tracedSlots385, intermediateActions_tracedCreateObjectActionActivations387, uml_tracedLiteralReals373, uml_tracedAddVariableValueActions375, uml_tracedClearStructuralFeatureActions377, uml_tracedAssociations379, uml_tracedExpressions381, uml_tracedUnmarshallActions383, uml_tracedInterfaceRealizations401, uml_tracedSendSignalActions403, uml_tracedCollaborations389, uml_tracedTestIdentityActions391, uml_tracedProfiles393, uml_tracedRemoveVariableValueActions395, uml_tracedActors397, uml_tracedManifestations399, uml_tracedTemplateParameters415, intermediateActivities_tracedMergeNodeActivations417, integerFunctions_tracedIntegerGreaterFunctionBehaviorExecutions419, uml_tracedFunctionBehaviors405, uml_tracedValueSpecificationActions407, uml_tracedTimeExpressions409, uml_tracedAbstractions411, uml_tracedReadIsClassifiedObjectActions413, uml_tracedComponents431, uml_tracedPseudostates421, uml_tracedLinkEndCreationDatas423, uml_tracedClearAssociationActions425, uml_tracedMergeNodes427, uml_tracedElementImports429, uml_tracedControlFlows441, uml_tracedGeneralOrderings443, uml_tracedClassifierTemplateParameters433, uml_tracedActivityFinalNodes435, uml_tracedGates437, uml_tracedTimeObservations439, runtimeModelElementTrace445, firingTrace447, runtimeModelElement450, parent451, states452, states454, parent456},
    generalizations={gen_umlTrace_uml_TracedCombinedFragment_TracedInteractionFragment, gen_umlTrace_uml_TracedDurationConstraint_TracedIntervalConstraint, gen_umlTrace_uml_TracedIntervalConstraint_TracedConstraint, gen_umlTrace_uml_TracedConstraint_TracedPackageableElement, gen_umlTrace_uml_TracedPackageableElement_uml_TracedNamedElement, gen_umlTrace_uml_TracedPackageableElement_uml_TracedParameterableElement, gen_umlTrace_uml_TracedParameterableElement_TracedElement, gen_umlTrace_uml_TracedPseudostate_TracedVertex, gen_umlTrace_uml_TracedVertex_TracedNamedElement, gen_umlTrace_uml_TracedDestructionOccurrenceSpecification_TracedMessageOccurrenceSpecification, gen_umlTrace_uml_TracedMessageOccurrenceSpecification_uml_TracedOccurrenceSpecification, gen_umlTrace_uml_TracedMessageOccurrenceSpecification_uml_TracedMessageEnd, gen_umlTrace_uml_TracedOccurrenceSpecification_TracedInteractionFragment, gen_umlTrace_uml_TracedInteractionFragment_TracedNamedElement, gen_umlTrace_uml_TracedNamedElement_TracedElement, gen_umlTrace_uml_TracedElement_TracedEModelElement, gen_umlTrace_uml_TracedConditionalNode_TracedStructuredActivityNode, gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedAction, gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedNamespace, gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedActivityGroup, gen_umlTrace_uml_TracedAction_TracedExecutableNode, gen_umlTrace_uml_TracedExecutableNode_TracedActivityNode, gen_umlTrace_uml_TracedActivityNode_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedActivityNode_ActivityContent, gen_umlTrace_uml_TracedRedefinableElement_TracedNamedElement, gen_umlTrace_uml_TracedNamespace_TracedNamedElement, gen_umlTrace_uml_TracedActivityGroup_uml_TracedNamedElement, gen_umlTrace_uml_TracedActivityGroup_ActivityContent, gen_umlTrace_uml_TracedCreateLinkObjectAction_TracedCreateLinkAction, gen_umlTrace_uml_TracedCreateLinkAction_TracedWriteLinkAction, gen_umlTrace_uml_TracedWriteLinkAction_TracedLinkAction, gen_umlTrace_uml_TracedLinkAction_TracedAction, gen_umlTrace_uml_TracedInitialNode_TracedControlNode, gen_umlTrace_uml_TracedControlNode_TracedActivityNode, gen_umlTrace_uml_TracedFlowFinalNode_TracedFinalNode, gen_umlTrace_uml_TracedFinalNode_TracedControlNode, gen_umlTrace_uml_TracedExpansionRegion_TracedStructuredActivityNode, gen_umlTrace_uml_TracedCreateObjectAction_TracedAction, gen_umlTrace_uml_TracedLifeline_TracedNamedElement, gen_umlTrace_uml_TracedObservation_TracedPackageableElement, gen_umlTrace_uml_TracedInteractionUse_TracedInteractionFragment, gen_umlTrace_uml_TracedLoopNode_TracedStructuredActivityNode, gen_umlTrace_uml_TracedSignal_TracedClassifier, gen_umlTrace_uml_TracedGeneralizationSet_TracedPackageableElement, gen_umlTrace_uml_TracedChangeEvent_TracedEvent, gen_umlTrace_uml_TracedEvent_TracedPackageableElement, gen_umlTrace_uml_TracedDependency_uml_TracedPackageableElement, gen_umlTrace_uml_TracedDependency_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedPort_TracedProperty, gen_umlTrace_uml_TracedProperty_uml_TracedStructuralFeature, gen_umlTrace_uml_TracedProperty_uml_TracedConnectableElement, gen_umlTrace_uml_TracedProperty_uml_TracedDeploymentTarget, gen_umlTrace_uml_TracedMessageEnd_TracedNamedElement, gen_umlTrace_uml_TracedPackage_uml_TracedNamespace, gen_umlTrace_uml_TracedPackage_uml_TracedPackageableElement, gen_umlTrace_uml_TracedPackage_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedTemplateableElement_TracedElement, gen_umlTrace_uml_TracedConnector_TracedFeature, gen_umlTrace_uml_TracedFeature_TracedRedefinableElement, gen_umlTrace_uml_TracedSendObjectAction_TracedInvocationAction, gen_umlTrace_uml_TracedInvocationAction_TracedAction, gen_umlTrace_uml_TracedOpaqueAction_TracedAction, gen_umlTrace_uml_TracedProtocolConformance_TracedDirectedRelationship, gen_umlTrace_uml_TracedDirectedRelationship_TracedRelationship, gen_umlTrace_uml_TracedRelationship_TracedElement, gen_umlTrace_uml_TracedCallBehaviorAction_TracedCallAction, gen_umlTrace_uml_TracedCallAction_TracedInvocationAction, gen_umlTrace_uml_TracedPackageImport_TracedDirectedRelationship, gen_umlTrace_uml_TracedClass_uml_TracedEncapsulatedClassifier, gen_umlTrace_uml_TracedClass_uml_TracedBehavioredClassifier, gen_umlTrace_uml_TracedEncapsulatedClassifier_TracedStructuredClassifier, gen_umlTrace_uml_TracedStructuredClassifier_TracedClassifier, gen_umlTrace_uml_TracedClassifier_uml_TracedNamespace, gen_umlTrace_uml_TracedClassifier_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedClassifier_uml_TracedType, gen_umlTrace_uml_TracedClassifier_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedType_TracedPackageableElement, gen_umlTrace_uml_TracedBehavioredClassifier_TracedClassifier, gen_umlTrace_uml_TracedActivityFinalNode_TracedFinalNode, gen_umlTrace_uml_TracedExecutionEnvironment_TracedNode, gen_umlTrace_uml_TracedConsiderIgnoreFragment_TracedCombinedFragment, gen_umlTrace_uml_TracedContinuation_TracedInteractionFragment, gen_umlTrace_uml_TracedCallOperationAction_TracedCallAction, gen_umlTrace_uml_TracedTimeConstraint_TracedIntervalConstraint, gen_umlTrace_uml_TracedClearVariableAction_TracedVariableAction, gen_umlTrace_uml_TracedVariableAction_TracedAction, gen_umlTrace_uml_TracedReadSelfAction_TracedAction, gen_umlTrace_uml_TracedLiteralString_TracedLiteralSpecification, gen_umlTrace_uml_TracedLiteralSpecification_TracedValueSpecification, gen_umlTrace_uml_TracedValueSpecification_uml_TracedPackageableElement, gen_umlTrace_uml_TracedValueSpecification_uml_TracedTypedElement, gen_umlTrace_uml_TracedBroadcastSignalAction_TracedInvocationAction, gen_umlTrace_uml_TracedStructuralFeature_uml_TracedFeature, gen_umlTrace_uml_TracedStructuralFeature_uml_TracedTypedElement, gen_umlTrace_uml_TracedStructuralFeature_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedTypedElement_TracedNamedElement, gen_umlTrace_uml_TracedMultiplicityElement_TracedElement, gen_umlTrace_uml_TracedConnectableElement_uml_TracedTypedElement, gen_umlTrace_uml_TracedConnectableElement_uml_TracedParameterableElement, gen_umlTrace_uml_TracedDeploymentTarget_TracedNamedElement, gen_umlTrace_uml_TracedCollaborationUse_TracedNamedElement, gen_umlTrace_uml_TracedValuePin_TracedInputPin, gen_umlTrace_uml_TracedInputPin_TracedPin, gen_umlTrace_uml_TracedPin_uml_TracedObjectNode, gen_umlTrace_uml_TracedPin_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedObjectNode_uml_TracedActivityNode, gen_umlTrace_uml_TracedObjectNode_uml_TracedTypedElement, gen_umlTrace_uml_TracedDeploymentSpecification_TracedArtifact, gen_umlTrace_uml_TracedArtifact_uml_TracedClassifier, gen_umlTrace_uml_TracedArtifact_uml_TracedDeployedArtifact, gen_umlTrace_uml_TracedDeployedArtifact_TracedNamedElement, gen_umlTrace_uml_TracedTransition_uml_TracedNamespace, gen_umlTrace_uml_TracedTransition_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedNode_uml_TracedClass, gen_umlTrace_uml_TracedNode_uml_TracedDeploymentTarget, gen_umlTrace_uml_TracedExceptionHandler_TracedElement, gen_umlTrace_uml_TracedSequenceNode_TracedStructuredActivityNode, gen_umlTrace_uml_TracedUseCase_TracedBehavioredClassifier, gen_umlTrace_uml_TracedStartClassifierBehaviorAction_TracedAction, gen_umlTrace_uml_TracedExtend_uml_TracedNamedElement, gen_umlTrace_uml_TracedExtend_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedRemoveStructuralFeatureValueAction_TracedWriteStructuralFeatureAction, gen_umlTrace_uml_TracedWriteStructuralFeatureAction_TracedStructuralFeatureAction, gen_umlTrace_uml_TracedStructuralFeatureAction_TracedAction, gen_umlTrace_uml_TracedReadLinkAction_TracedLinkAction, gen_umlTrace_uml_TracedExtension_TracedAssociation, gen_umlTrace_uml_TracedAssociation_uml_TracedClassifier, gen_umlTrace_uml_TracedAssociation_uml_TracedRelationship, gen_umlTrace_uml_TracedInformationFlow_uml_TracedPackageableElement, gen_umlTrace_uml_TracedInformationFlow_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedDestroyObjectAction_TracedAction, gen_umlTrace_uml_TracedActivityPartition_TracedActivityGroup, gen_umlTrace_uml_TracedStateMachine_TracedBehavior, gen_umlTrace_uml_TracedMessage_TracedNamedElement, gen_umlTrace_uml_TracedReadLinkObjectEndQualifierAction_TracedAction, gen_umlTrace_uml_TracedDeployment_TracedDependency, gen_umlTrace_uml_TracedActivity_TracedBehavior, gen_umlTrace_uml_TracedForkNode_TracedControlNode, gen_umlTrace_uml_TracedProtocolStateMachine_TracedStateMachine, gen_umlTrace_uml_TracedInterval_TracedValueSpecification, gen_umlTrace_uml_TracedClearStructuralFeatureAction_TracedStructuralFeatureAction, gen_umlTrace_uml_TracedObjectFlow_TracedActivityEdge, gen_umlTrace_uml_TracedInteraction_uml_TracedBehavior, gen_umlTrace_uml_TracedInteraction_uml_TracedInteractionFragment, gen_umlTrace_uml_TracedBehavior_TracedClass, gen_umlTrace_uml_TracedSlot_TracedElement, gen_umlTrace_uml_TracedLiteralNull_TracedLiteralSpecification, gen_umlTrace_uml_TracedParameter_uml_TracedConnectableElement, gen_umlTrace_uml_TracedParameter_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedOpaqueExpression_TracedValueSpecification, gen_umlTrace_uml_TracedTrigger_TracedNamedElement, gen_umlTrace_uml_TracedStateInvariant_TracedInteractionFragment, gen_umlTrace_uml_TracedAssociationClass_uml_TracedClass, gen_umlTrace_uml_TracedAssociationClass_uml_TracedAssociation, gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedDeploymentTarget, gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedPackageableElement, gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedDeployedArtifact, gen_umlTrace_uml_TracedTemplateSignature_TracedElement, gen_umlTrace_uml_TracedLinkEndDestructionData_TracedLinkEndData, gen_umlTrace_uml_TracedLinkEndData_TracedElement, gen_umlTrace_uml_TracedAcceptCallAction_TracedAcceptEventAction, gen_umlTrace_uml_TracedAcceptEventAction_TracedAction, gen_umlTrace_uml_TracedReduceAction_TracedAction, gen_umlTrace_uml_TracedRaiseExceptionAction_TracedAction, gen_umlTrace_uml_TracedStereotype_TracedClass, gen_umlTrace_uml_TracedClearAssociationAction_TracedAction, gen_umlTrace_uml_TracedEnumerationLiteral_TracedInstanceSpecification, gen_umlTrace_uml_TracedSubstitution_TracedRealization, gen_umlTrace_uml_TracedRealization_TracedAbstraction, gen_umlTrace_uml_TracedAbstraction_TracedDependency, gen_umlTrace_uml_TracedExecutionSpecification_TracedInteractionFragment, gen_umlTrace_uml_TracedReplyAction_TracedAction, gen_umlTrace_uml_TracedActor_TracedBehavioredClassifier, gen_umlTrace_uml_TracedReception_TracedBehavioralFeature, gen_umlTrace_uml_TracedTemplateBinding_TracedDirectedRelationship, gen_umlTrace_uml_TracedUsage_TracedDependency, gen_umlTrace_uml_TracedActionInputPin_TracedInputPin, gen_umlTrace_uml_TracedReadVariableAction_TracedVariableAction, gen_umlTrace_uml_TracedDestroyLinkAction_TracedWriteLinkAction, gen_umlTrace_uml_TracedLiteralInteger_TracedLiteralSpecification, gen_umlTrace_uml_TracedSignalEvent_TracedMessageEvent, gen_umlTrace_uml_TracedReadLinkObjectEndAction_TracedAction, gen_umlTrace_uml_TracedTimeInterval_TracedInterval, gen_umlTrace_uml_TracedOperationTemplateParameter_TracedTemplateParameter, gen_umlTrace_uml_TracedDurationObservation_TracedObservation, gen_umlTrace_uml_TracedActivityEdge_TracedRedefinableElement, gen_umlTrace_uml_TracedTestIdentityAction_TracedAction, gen_umlTrace_uml_TracedInstanceValue_TracedValueSpecification, gen_umlTrace_uml_TracedLiteralUnlimitedNatural_TracedLiteralSpecification, gen_umlTrace_uml_TracedReclassifyObjectAction_TracedAction, gen_umlTrace_uml_TracedTimeEvent_TracedEvent, gen_umlTrace_uml_TracedPartDecomposition_TracedInteractionUse, gen_umlTrace_uml_TracedInterruptibleActivityRegion_TracedActivityGroup, gen_umlTrace_uml_TracedAddVariableValueAction_TracedWriteVariableAction, gen_umlTrace_uml_TracedWriteVariableAction_TracedVariableAction, gen_umlTrace_uml_TracedProtocolTransition_TracedTransition, gen_umlTrace_uml_TracedImage_TracedElement, gen_umlTrace_uml_TracedLiteralReal_TracedLiteralSpecification, gen_umlTrace_uml_TracedInteractionOperand_uml_TracedNamespace, gen_umlTrace_uml_TracedInteractionOperand_uml_TracedInteractionFragment, gen_umlTrace_uml_TracedGeneralization_TracedDirectedRelationship, gen_umlTrace_uml_TracedInformationItem_TracedClassifier, gen_umlTrace_uml_TracedModel_TracedPackage, gen_umlTrace_uml_TracedClassifierTemplateParameter_TracedTemplateParameter, gen_umlTrace_uml_TracedTemplateParameter_TracedElement, gen_umlTrace_uml_TracedOperation_uml_TracedBehavioralFeature, gen_umlTrace_uml_TracedOperation_uml_TracedParameterableElement, gen_umlTrace_uml_TracedOperation_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedBehavioralFeature_uml_TracedNamespace, gen_umlTrace_uml_TracedBehavioralFeature_uml_TracedFeature, gen_umlTrace_uml_TracedAnyReceiveEvent_TracedMessageEvent, gen_umlTrace_uml_TracedMessageEvent_TracedEvent, gen_umlTrace_uml_TracedPrimitiveType_TracedDataType, gen_umlTrace_uml_TracedDataType_TracedClassifier, gen_umlTrace_uml_TracedReadStructuralFeatureAction_TracedStructuralFeatureAction, gen_umlTrace_uml_TracedParameterSet_TracedNamedElement, gen_umlTrace_uml_TracedDataStoreNode_TracedCentralBufferNode, gen_umlTrace_uml_TracedCentralBufferNode_TracedObjectNode, gen_umlTrace_uml_TracedSendSignalAction_TracedInvocationAction, gen_umlTrace_uml_TracedConnectableElementTemplateParameter_TracedTemplateParameter, gen_umlTrace_uml_TracedActionExecutionSpecification_TracedExecutionSpecification, gen_umlTrace_uml_TracedOutputPin_TracedPin, gen_umlTrace_uml_TracedDuration_TracedValueSpecification, gen_umlTrace_uml_TracedUnmarshallAction_TracedAction, gen_umlTrace_uml_TracedProfile_TracedPackage, gen_umlTrace_uml_TracedExtensionEnd_TracedProperty, gen_umlTrace_uml_TracedExpansionNode_TracedObjectNode, gen_umlTrace_uml_TracedActivityParameterNode_TracedObjectNode, gen_umlTrace_uml_TracedProfileApplication_TracedDirectedRelationship, gen_umlTrace_uml_TracedConnectorEnd_TracedMultiplicityElement, gen_umlTrace_uml_TracedEnumeration_TracedDataType, gen_umlTrace_uml_TracedCollaboration_uml_TracedStructuredClassifier, gen_umlTrace_uml_TracedCollaboration_uml_TracedBehavioredClassifier, gen_umlTrace_uml_TracedConnectionPointReference_TracedVertex, gen_umlTrace_uml_TracedTimeExpression_TracedValueSpecification, gen_umlTrace_uml_TracedQualifierValue_TracedElement, gen_umlTrace_uml_TracedDurationInterval_TracedInterval, gen_umlTrace_uml_TracedFunctionBehavior_TracedOpaqueBehavior, gen_umlTrace_uml_TracedOpaqueBehavior_TracedBehavior, gen_umlTrace_uml_TracedInterfaceRealization_TracedRealization, gen_umlTrace_uml_TracedDevice_TracedNode, gen_umlTrace_uml_TracedTemplateParameterSubstitution_TracedElement, gen_umlTrace_uml_TracedJoinNode_TracedControlNode, gen_umlTrace_uml_TracedRedefinableTemplateSignature_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedRedefinableTemplateSignature_uml_TracedTemplateSignature, gen_umlTrace_uml_TracedReadIsClassifiedObjectAction_TracedAction, gen_umlTrace_uml_TracedTimeObservation_TracedObservation, gen_umlTrace_uml_TracedDecisionNode_TracedControlNode, gen_umlTrace_uml_TracedElementImport_TracedDirectedRelationship, gen_umlTrace_uml_TracedExtensionPoint_TracedRedefinableElement, gen_umlTrace_uml_TracedExecutionOccurrenceSpecification_TracedOccurrenceSpecification, gen_umlTrace_uml_TracedInteractionConstraint_TracedConstraint, gen_umlTrace_uml_TracedAddStructuralFeatureValueAction_TracedWriteStructuralFeatureAction, gen_umlTrace_uml_TracedInterface_TracedClassifier, gen_umlTrace_uml_TracedComponent_TracedClass, gen_umlTrace_uml_TracedCallEvent_TracedMessageEvent, gen_umlTrace_uml_TracedComment_TracedElement, gen_umlTrace_uml_TracedBehaviorExecutionSpecification_TracedExecutionSpecification, gen_umlTrace_uml_TracedComponentRealization_TracedRealization, gen_umlTrace_uml_TracedCommunicationPath_TracedAssociation, gen_umlTrace_uml_TracedPackageMerge_TracedDirectedRelationship, gen_umlTrace_uml_TracedClause_TracedElement, gen_umlTrace_uml_TracedFinalState_TracedState, gen_umlTrace_uml_TracedState_uml_TracedNamespace, gen_umlTrace_uml_TracedState_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedState_uml_TracedVertex, gen_umlTrace_IntermediateActivities_TracedForkNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedControlNodeActivation_TracedActivityNodeActivation, gen_umlTrace_IntermediateActivities_TracedActivityNodeActivation_TracedSemanticVisitor, gen_umlTrace_IntermediateActivities_TracedObjectNodeActivation_TracedActivityNodeActivation, gen_umlTrace_IntermediateActivities_TracedInitialNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedActivityExecution_TracedExecution, gen_umlTrace_IntermediateActivities_TracedMergeNodeActivation_TracedControlNodeActivation, gen_umlTrace_uml_TracedVariable_uml_TracedConnectableElement, gen_umlTrace_uml_TracedVariable_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedValueSpecificationAction_TracedAction, gen_umlTrace_uml_TracedReadExtentAction_TracedAction, gen_umlTrace_uml_TracedStringExpression_uml_TracedExpression, gen_umlTrace_uml_TracedStringExpression_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedExpression_TracedValueSpecification, gen_umlTrace_uml_TracedGeneralOrdering_TracedNamedElement, gen_umlTrace_uml_TracedLiteralBoolean_TracedLiteralSpecification, gen_umlTrace_uml_TracedStartObjectBehaviorAction_TracedCallAction, gen_umlTrace_uml_TracedRegion_uml_TracedNamespace, gen_umlTrace_uml_TracedRegion_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedInclude_uml_TracedNamedElement, gen_umlTrace_uml_TracedInclude_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedControlFlow_TracedActivityEdge, gen_umlTrace_uml_TracedGate_TracedMessageEnd, gen_umlTrace_uml_TracedRemoveVariableValueAction_TracedWriteVariableAction, gen_umlTrace_uml_TracedManifestation_TracedAbstraction, gen_umlTrace_uml_TracedLinkEndCreationData_TracedLinkEndData, gen_umlTrace_uml_TracedMergeNode_TracedControlNode, gen_umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation_TracedActionActivation, gen_umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation, gen_umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation_TracedWriteStructuralFeatureActionActivation, gen_umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation, gen_umlTrace_IntermediateActions_TracedValueSpecificationActionActivation_TracedActionActivation, gen_umlTrace_IntermediateActions_TracedCreateObjectActionActivation_TracedActionActivation, gen_umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation_TracedObjectNodeActivation, gen_umlTrace_IntermediateActivities_TracedJoinNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedDecisionNodeActivation_TracedControlNodeActivation, gen_umlTrace_BasicActions_TracedPinActivation_TracedObjectNodeActivation, gen_umlTrace_BasicActions_TracedActionActivation_TracedActivityNodeActivation, gen_umlTrace_BasicActions_TracedInvocationActionActivation_TracedActionActivation, gen_umlTrace_BasicActions_TracedCallActionActivation_TracedInvocationActionActivation, gen_umlTrace_BasicActions_TracedOpaqueActionActivation_TracedActionActivation, gen_umlTrace_BasicActions_TracedInputPinActivation_TracedPinActivation, gen_umlTrace_BasicActions_TracedCallBehaviorActionActivation_TracedCallActionActivation, gen_umlTrace_BasicActions_TracedOutputPinActivation_TracedPinActivation, gen_umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_TracedOpaqueBehaviorExecution, gen_umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_TracedOpaqueBehaviorExecution, gen_umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_TracedOpaqueBehaviorExecution, gen_umlTrace_BasicBehaviors_TracedExecution_TracedObject, gen_umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution_TracedExecution, gen_umlTrace_Kernel_TracedObject_TracedExtensionalValue, gen_umlTrace_Kernel_TracedExtensionalValue_TracedCompoundValue, gen_umlTrace_Kernel_TracedCompoundValue_TracedStructuredValue, gen_umlTrace_Kernel_TracedStructuredValue_TracedValue, gen_umlTrace_Kernel_TracedValue_TracedSemanticVisitor, gen_umlTrace_Kernel_TracedReference_TracedStructuredValue, gen_umlTrace_Kernel_TracedLiteralEvaluation_TracedEvaluation, gen_umlTrace_Kernel_TracedEvaluation_TracedSemanticVisitor, gen_umlTrace_Kernel_TracedIntegerValue_TracedPrimitiveValue, gen_umlTrace_Kernel_TracedPrimitiveValue_TracedValue, gen_umlTrace_Kernel_TracedLiteralBooleanEvaluation_TracedLiteralEvaluation, gen_umlTrace_Kernel_TracedBooleanValue_TracedPrimitiveValue, gen_umlTrace_Kernel_TracedLiteralIntegerEvaluation_TracedLiteralEvaluation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)