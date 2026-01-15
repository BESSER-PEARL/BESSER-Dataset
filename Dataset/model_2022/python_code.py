from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ecore_umlTrace_EAnnotation:

    pass
class umlTrace_ecore_TracedEModelElement(ABC):

    pass
class uml_umlTrace_CentralBufferNode:

    pass
class uml_umlTrace_UnmarshallAction:

    pass
class uml_umlTrace_BehaviorExecutionSpecification:

    pass
class uml_umlTrace_Actor:

    pass
class TracedArtifact:

    pass
class umlTrace_uml_TracedDeploymentSpecification(TracedArtifact):

    pass
class TracedOpaqueBehavior:

    pass
class umlTrace_uml_TracedFunctionBehavior(TracedOpaqueBehavior):

    pass
class uml_umlTrace_OpaqueExpression:

    pass
class uml_umlTrace_ClearStructuralFeatureAction:

    pass
class uml_umlTrace_TemplateBinding:

    pass
class TracedAcceptEventAction:

    pass
class umlTrace_uml_TracedAcceptCallAction(TracedAcceptEventAction):

    pass
class uml_umlTrace_ReadSelfAction:

    pass
class uml_umlTrace_ActionExecutionSpecification:

    pass
class TracedExecutionSpecification:

    pass
class umlTrace_uml_TracedBehaviorExecutionSpecification(TracedExecutionSpecification):

    pass
class umlTrace_uml_TracedActionExecutionSpecification(TracedExecutionSpecification):

    pass
class uml_umlTrace_ConnectionPointReference:

    pass
class uml_umlTrace_ReclassifyObjectAction:

    pass
class uml_umlTrace_CallBehaviorAction:

    pass
class uml_umlTrace_GeneralOrdering:

    pass
class uml_umlTrace_Gate:

    pass
class TracedMessageEnd:

    pass
class umlTrace_uml_TracedGate(TracedMessageEnd):

    pass
class uml_umlTrace_RemoveVariableValueAction:

    pass
class uml_umlTrace_LiteralReal:

    pass
class uml_umlTrace_StateInvariant:

    pass
class uml_umlTrace_Association:

    pass
class uml_umlTrace_InteractionUse:

    pass
class uml_umlTrace_Variable:

    pass
class uml_umlTrace_ExceptionHandler:

    pass
class uml_TracedExecutionSpecification:

    pass
class TracedOccurrenceSpecification:

    pass
class umlTrace_uml_TracedExecutionOccurrenceSpecification(TracedOccurrenceSpecification):

    pass
class uml_umlTrace_PackageImport:

    pass
class uml_umlTrace_Operation:

    pass
class uml_umlTrace_ControlFlow:

    pass
class uml_umlTrace_TestIdentityAction:

    pass
class uml_TracedObjectNode:

    pass
class uml_umlTrace_ClearAssociationAction:

    pass
class uml_umlTrace_AddVariableValueAction:

    pass
class TracedWriteVariableAction:

    pass
class umlTrace_uml_TracedRemoveVariableValueAction(TracedWriteVariableAction):

    pass
class umlTrace_uml_TracedAddVariableValueAction(TracedWriteVariableAction):

    pass
class uml_umlTrace_RaiseExceptionAction:

    pass
class uml_umlTrace_Reception:

    pass
class TracedBehavioralFeature:

    pass
class umlTrace_uml_TracedReception(TracedBehavioralFeature):

    pass
class uml_umlTrace_ExpansionNode:

    pass
class uml_umlTrace_LiteralNull:

    pass
class uml_umlTrace_Comment:

    pass
class uml_umlTrace_Signal:

    pass
class uml_umlTrace_ForkNode:

    pass
class uml_umlTrace_DestroyObjectAction:

    pass
class uml_umlTrace_ChangeEvent:

    pass
class TracedActivityEdge:

    pass
class umlTrace_uml_TracedControlFlow(TracedActivityEdge):

    pass
class umlTrace_uml_TracedObjectFlow(TracedActivityEdge):

    pass
class uml_umlTrace_PackageMerge:

    pass
class uml_umlTrace_LinkEndData:

    pass
class uml_umlTrace_ObjectFlow:

    pass
class uml_umlTrace_Transition:

    pass
class uml_umlTrace_ReadExtentAction:

    pass
class uml_umlTrace_TimeExpression:

    pass
class uml_umlTrace_Dependency:

    pass
class uml_umlTrace_InstanceValue:

    pass
class uml_umlTrace_Clause:

    pass
class uml_umlTrace_CombinedFragment:

    pass
class uml_umlTrace_ReplyAction:

    pass
class uml_umlTrace_UseCase:

    pass
class TracedBehavioredClassifier:

    pass
class umlTrace_uml_TracedActor(TracedBehavioredClassifier):

    pass
class umlTrace_uml_TracedUseCase(TracedBehavioredClassifier):

    pass
class TracedActivityNode:

    pass
class umlTrace_uml_TracedExecutableNode(TracedActivityNode):

    pass
class umlTrace_uml_TracedControlNode(TracedActivityNode):

    pass
class uml_umlTrace_Pseudostate:

    pass
class TracedVertex:

    pass
class umlTrace_uml_TracedConnectionPointReference(TracedVertex):

    pass
class umlTrace_uml_TracedPseudostate(TracedVertex):

    pass
class uml_umlTrace_InformationFlow:

    pass
class uml_TracedRelationship:

    pass
class uml_umlTrace_InteractionOperand:

    pass
class TracedState:

    pass
class umlTrace_uml_TracedFinalState(TracedState):

    pass
class uml_umlTrace_DestroyLinkAction:

    pass
class uml_umlTrace_InterruptibleActivityRegion:

    pass
class uml_umlTrace_Region:

    pass
class TracedStateMachine:

    pass
class umlTrace_uml_TracedProtocolStateMachine(TracedStateMachine):

    pass
class uml_umlTrace_ValueSpecificationAction:

    pass
class uml_umlTrace_DecisionNode:

    pass
class uml_umlTrace_OutputPin:

    pass
class uml_umlTrace_ReadIsClassifiedObjectAction:

    pass
class uml_umlTrace_InstanceSpecification:

    pass
class uml_TracedEvent:

    pass
class uml_umlTrace_Interval:

    pass
class TracedPackage:

    pass
class umlTrace_uml_TracedModel(TracedPackage):

    pass
class umlTrace_uml_TracedProfile(TracedPackage):

    pass
class uml_umlTrace_CallOperationAction:

    pass
class uml_umlTrace_Trigger:

    pass
class uml_umlTrace_ConnectorEnd:

    pass
class TracedInputPin:

    pass
class umlTrace_uml_TracedValuePin(TracedInputPin):

    pass
class umlTrace_uml_TracedActionInputPin(TracedInputPin):

    pass
class uml_umlTrace_Parameter:

    pass
class TracedStructuredClassifier:

    pass
class umlTrace_uml_TracedEncapsulatedClassifier(TracedStructuredClassifier):

    pass
class uml_umlTrace_Image:

    pass
class uml_umlTrace_ProfileApplication:

    pass
class TracedMultiplicityElement:

    pass
class umlTrace_uml_TracedConnectorEnd(TracedMultiplicityElement):

    pass
class uml_umlTrace_TemplateParameter:

    pass
class uml_umlTrace_LiteralBoolean:

    pass
class uml_umlTrace_Message:

    pass
class uml_umlTrace_ClearVariableAction:

    pass
class uml_umlTrace_LiteralInteger:

    pass
class uml_umlTrace_InitialNode:

    pass
class uml_umlTrace_QualifierValue:

    pass
class uml_TracedMessageEnd:

    pass
class uml_umlTrace_ReadVariableAction:

    pass
class uml_umlTrace_Extend:

    pass
class uml_umlTrace_TemplateParameterSubstitution:

    pass
class uml_umlTrace_ReadLinkObjectEndQualifierAction:

    pass
class TracedInteractionUse:

    pass
class umlTrace_uml_TracedPartDecomposition(TracedInteractionUse):

    pass
class uml_umlTrace_Generalization:

    pass
class uml_umlTrace_CreateLinkAction:

    pass
class TracedWriteLinkAction:

    pass
class umlTrace_uml_TracedDestroyLinkAction(TracedWriteLinkAction):

    pass
class umlTrace_uml_TracedCreateLinkAction(TracedWriteLinkAction):

    pass
class uml_umlTrace_MergeNode:

    pass
class uml_umlTrace_ReadStructuralFeatureAction:

    pass
class uml_umlTrace_StructuredActivityNode:

    pass
class uml_TracedEncapsulatedClassifier:

    pass
class uml_umlTrace_Duration:

    pass
class uml_umlTrace_LiteralUnlimitedNatural:

    pass
class uml_umlTrace_Class:

    pass
class uml_TracedObservation:

    pass
class uml_umlTrace_ParameterSet:

    pass
class uml_umlTrace_ActivityParameterNode:

    pass
class TracedObjectNode:

    pass
class umlTrace_uml_TracedExpansionNode(TracedObjectNode):

    pass
class umlTrace_uml_TracedCentralBufferNode(TracedObjectNode):

    pass
class umlTrace_uml_TracedActivityParameterNode(TracedObjectNode):

    pass
class uml_umlTrace_State:

    pass
class uml_TracedBehavioralFeature:

    pass
class uml_TracedVertex:

    pass
class TracedMessageOccurrenceSpecification:

    pass
class umlTrace_uml_TracedDestructionOccurrenceSpecification(TracedMessageOccurrenceSpecification):

    pass
class uml_TracedActivityGroup:

    pass
class ActivityContent:

    pass
class uml_umlTrace_Include:

    pass
class uml_umlTrace_CollaborationUse:

    pass
class uml_TracedDirectedRelationship:

    pass
class TracedLinkEndData:

    pass
class umlTrace_uml_TracedLinkEndCreationData(TracedLinkEndData):

    pass
class umlTrace_uml_TracedLinkEndDestructionData(TracedLinkEndData):

    pass
class uml_umlTrace_ActivityPartition:

    pass
class TracedActivityGroup:

    pass
class umlTrace_uml_TracedInterruptibleActivityRegion(TracedActivityGroup):

    pass
class umlTrace_uml_TracedActivityPartition(TracedActivityGroup):

    pass
class uml_umlTrace_ProtocolConformance:

    pass
class TracedDataType:

    pass
class umlTrace_uml_TracedEnumeration(TracedDataType):

    pass
class umlTrace_uml_TracedPrimitiveType(TracedDataType):

    pass
class TracedCreateLinkAction:

    pass
class umlTrace_uml_TracedCreateLinkObjectAction(TracedCreateLinkAction):

    pass
class uml_umlTrace_TimeObservation:

    pass
class TracedVariableAction:

    pass
class umlTrace_uml_TracedClearVariableAction(TracedVariableAction):

    pass
class umlTrace_uml_TracedReadVariableAction(TracedVariableAction):

    pass
class umlTrace_uml_TracedWriteVariableAction(TracedVariableAction):

    pass
class uml_umlTrace_SendObjectAction:

    pass
class uml_umlTrace_Lifeline:

    pass
class uml_TracedAction:

    pass
class TracedTemplateParameter:

    pass
class umlTrace_uml_TracedClassifierTemplateParameter(TracedTemplateParameter):

    pass
class umlTrace_uml_TracedOperationTemplateParameter(TracedTemplateParameter):

    pass
class umlTrace_uml_TracedConnectableElementTemplateParameter(TracedTemplateParameter):

    pass
class uml_umlTrace_CallEvent:

    pass
class uml_umlTrace_StartClassifierBehaviorAction:

    pass
class TracedAbstraction:

    pass
class umlTrace_uml_TracedManifestation(TracedAbstraction):

    pass
class umlTrace_uml_TracedRealization(TracedAbstraction):

    pass
class uml_umlTrace_LiteralString:

    pass
class TracedLiteralSpecification:

    pass
class umlTrace_uml_TracedLiteralBoolean(TracedLiteralSpecification):

    pass
class umlTrace_uml_TracedLiteralUnlimitedNatural(TracedLiteralSpecification):

    pass
class umlTrace_uml_TracedLiteralReal(TracedLiteralSpecification):

    pass
class umlTrace_uml_TracedLiteralInteger(TracedLiteralSpecification):

    pass
class umlTrace_uml_TracedLiteralNull(TracedLiteralSpecification):

    pass
class umlTrace_uml_TracedLiteralString(TracedLiteralSpecification):

    pass
class uml_TracedInteractionFragment:

    pass
class uml_umlTrace_AnyReceiveEvent:

    pass
class uml_umlTrace_ReadLinkObjectEndAction:

    pass
class TracedClass:

    pass
class umlTrace_uml_TracedComponent(TracedClass):

    pass
class umlTrace_uml_TracedBehavior(TracedClass):

    pass
class umlTrace_uml_TracedStereotype(TracedClass):

    pass
class uml_umlTrace_Interface:

    pass
class TracedDirectedRelationship:

    pass
class umlTrace_uml_TracedPackageMerge(TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedProfileApplication(TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedTemplateBinding(TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedPackageImport(TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedProtocolConformance(TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedGeneralization(TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedElementImport(TracedDirectedRelationship):

    pass
class uml_umlTrace_OccurrenceSpecification:

    pass
class TracedNode:

    pass
class umlTrace_uml_TracedDevice(TracedNode):

    pass
class umlTrace_uml_TracedExecutionEnvironment(TracedNode):

    pass
class uml_umlTrace_CreateObjectAction:

    pass
class uml_umlTrace_ElementImport:

    pass
class uml_umlTrace_StartObjectBehaviorAction:

    pass
class TracedCallAction:

    pass
class umlTrace_uml_TracedCallBehaviorAction(TracedCallAction):

    pass
class umlTrace_uml_TracedCallOperationAction(TracedCallAction):

    pass
class umlTrace_uml_TracedStartObjectBehaviorAction(TracedCallAction):

    pass
class uml_umlTrace_JoinNode:

    pass
class TracedControlNode:

    pass
class umlTrace_uml_TracedFinalNode(TracedControlNode):

    pass
class umlTrace_uml_TracedDecisionNode(TracedControlNode):

    pass
class umlTrace_uml_TracedForkNode(TracedControlNode):

    pass
class umlTrace_uml_TracedMergeNode(TracedControlNode):

    pass
class umlTrace_uml_TracedInitialNode(TracedControlNode):

    pass
class umlTrace_uml_TracedJoinNode(TracedControlNode):

    pass
class uml_umlTrace_ExtensionPoint:

    pass
class uml_umlTrace_SignalEvent:

    pass
class TracedMessageEvent:

    pass
class umlTrace_uml_TracedCallEvent(TracedMessageEvent):

    pass
class umlTrace_uml_TracedAnyReceiveEvent(TracedMessageEvent):

    pass
class umlTrace_uml_TracedSignalEvent(TracedMessageEvent):

    pass
class uml_umlTrace_Slot:

    pass
class TracedStructuralFeatureAction:

    pass
class umlTrace_uml_TracedClearStructuralFeatureAction(TracedStructuralFeatureAction):

    pass
class umlTrace_uml_TracedReadStructuralFeatureAction(TracedStructuralFeatureAction):

    pass
class umlTrace_uml_TracedWriteStructuralFeatureAction(TracedStructuralFeatureAction):

    pass
class TracedEModelElement:

    pass
class umlTrace_uml_TracedElement(TracedEModelElement):

    pass
class uml_umlTrace_GeneralizationSet:

    pass
class TracedConstraint:

    pass
class umlTrace_uml_TracedIntervalConstraint(TracedConstraint):

    pass
class umlTrace_uml_TracedInteractionConstraint(TracedConstraint):

    pass
class TracedRedefinableElement:

    pass
class umlTrace_uml_TracedActivityEdge(TracedRedefinableElement):

    pass
class umlTrace_uml_TracedExtensionPoint(TracedRedefinableElement):

    pass
class umlTrace_uml_TracedFeature(TracedRedefinableElement):

    pass
class uml_TracedExecutableNode:

    pass
class TracedStructuredActivityNode:

    pass
class umlTrace_uml_TracedExpansionRegion(TracedStructuredActivityNode):

    pass
class umlTrace_uml_TracedConditionalNode(TracedStructuredActivityNode):

    pass
class umlTrace_uml_TracedLoopNode(TracedStructuredActivityNode):

    pass
class umlTrace_uml_TracedSequenceNode(TracedStructuredActivityNode):

    pass
class uml_umlTrace_InputPin:

    pass
class TracedPin:

    pass
class umlTrace_uml_TracedOutputPin(TracedPin):

    pass
class umlTrace_uml_TracedInputPin(TracedPin):

    pass
class uml_umlTrace_ReduceAction:

    pass
class uml_umlTrace_Constraint:

    pass
class uml_umlTrace_Package:

    pass
class uml_TracedPackageableElement:

    pass
class umlTrace_uml_TracedDependency(uml_TracedDirectedRelationship, uml_TracedPackageableElement):

    pass
class umlTrace_uml_TracedInformationFlow(uml_TracedDirectedRelationship, uml_TracedPackageableElement):

    pass
class TracedTransition:

    pass
class umlTrace_uml_TracedProtocolTransition(TracedTransition):

    pass
class TracedPackageableElement:

    pass
class umlTrace_uml_TracedGeneralizationSet(TracedPackageableElement):

    pass
class umlTrace_uml_TracedEvent(TracedPackageableElement):

    pass
class umlTrace_uml_TracedObservation(TracedPackageableElement):

    pass
class umlTrace_uml_TracedConstraint(TracedPackageableElement):

    pass
class umlTrace_uml_TracedType(TracedPackageableElement):

    pass
class uml_TracedParameterableElement:

    pass
class uml_umlTrace_TimeEvent:

    pass
class TracedEvent:

    pass
class umlTrace_uml_TracedChangeEvent(TracedEvent):

    pass
class umlTrace_uml_TracedMessageEvent(TracedEvent):

    pass
class umlTrace_uml_TracedTimeEvent(TracedEvent):

    pass
class TracedRelationship:

    pass
class umlTrace_uml_TracedDirectedRelationship(TracedRelationship):

    pass
class TracedExecutableNode:

    pass
class umlTrace_uml_TracedAction(TracedExecutableNode):

    pass
class TracedInterval:

    pass
class umlTrace_uml_TracedDurationInterval(TracedInterval):

    pass
class umlTrace_uml_TracedTimeInterval(TracedInterval):

    pass
class TracedProperty:

    pass
class umlTrace_uml_TracedExtensionEnd(TracedProperty):

    pass
class umlTrace_uml_TracedPort(TracedProperty):

    pass
class TracedDependency:

    pass
class umlTrace_uml_TracedUsage(TracedDependency):

    pass
class umlTrace_uml_TracedAbstraction(TracedDependency):

    pass
class umlTrace_uml_TracedDeployment(TracedDependency):

    pass
class uml_umlTrace_BroadcastSignalAction:

    pass
class uml_umlTrace_TemplateSignature:

    pass
class TracedElement:

    pass
class umlTrace_uml_TracedParameterableElement(TracedElement):

    pass
class umlTrace_uml_TracedNamedElement(TracedElement):

    pass
class umlTrace_uml_TracedLinkEndData(TracedElement):

    pass
class umlTrace_uml_TracedMultiplicityElement(TracedElement):

    pass
class umlTrace_uml_TracedTemplateParameter(TracedElement):

    pass
class umlTrace_uml_TracedExceptionHandler(TracedElement):

    pass
class umlTrace_uml_TracedClause(TracedElement):

    pass
class umlTrace_uml_TracedRelationship(TracedElement):

    pass
class umlTrace_uml_TracedImage(TracedElement):

    pass
class umlTrace_uml_TracedTemplateableElement(TracedElement):

    pass
class umlTrace_uml_TracedSlot(TracedElement):

    pass
class umlTrace_uml_TracedQualifierValue(TracedElement):

    pass
class umlTrace_uml_TracedTemplateParameterSubstitution(TracedElement):

    pass
class umlTrace_uml_TracedComment(TracedElement):

    pass
class umlTrace_uml_TracedTemplateSignature(TracedElement):

    pass
class uml_umlTrace_Collaboration:

    pass
class uml_TracedStructuredClassifier:

    pass
class uml_umlTrace_InformationItem:

    pass
class uml_TracedTemplateableElement:

    pass
class umlTrace_uml_TracedOperation(uml_TracedTemplateableElement, uml_TracedParameterableElement, uml_TracedBehavioralFeature):

    pass
class uml_TracedType:

    pass
class uml_TracedRedefinableElement:

    pass
class umlTrace_uml_TracedActivityNode(uml_TracedRedefinableElement, ActivityContent):

    pass
class uml_TracedNamespace:

    pass
class umlTrace_uml_TracedPackage(uml_TracedPackageableElement, uml_TracedTemplateableElement, uml_TracedNamespace):

    pass
class umlTrace_uml_TracedStructuredActivityNode(uml_TracedAction, uml_TracedActivityGroup, uml_TracedNamespace):

    pass
class umlTrace_uml_TracedTransition(uml_TracedRedefinableElement, uml_TracedNamespace):

    pass
class umlTrace_uml_TracedState(uml_TracedRedefinableElement, uml_TracedVertex, uml_TracedNamespace):

    pass
class umlTrace_uml_TracedInteractionOperand(uml_TracedInteractionFragment, uml_TracedNamespace):

    pass
class umlTrace_uml_TracedRegion(uml_TracedRedefinableElement, uml_TracedNamespace):

    pass
class uml_umlTrace_ReadLinkAction:

    pass
class TracedLinkAction:

    pass
class umlTrace_uml_TracedWriteLinkAction(TracedLinkAction):

    pass
class umlTrace_uml_TracedReadLinkAction(TracedLinkAction):

    pass
class umlTrace_uml_TracedClassifier(uml_TracedRedefinableElement, uml_TracedType, uml_TracedTemplateableElement, uml_TracedNamespace):

    pass
class TracedNamedElement:

    pass
class umlTrace_uml_TracedLifeline(TracedNamedElement):

    pass
class umlTrace_uml_TracedVertex(TracedNamedElement):

    pass
class umlTrace_uml_TracedDeployedArtifact(TracedNamedElement):

    pass
class umlTrace_uml_TracedCollaborationUse(TracedNamedElement):

    pass
class umlTrace_uml_TracedGeneralOrdering(TracedNamedElement):

    pass
class umlTrace_uml_TracedRedefinableElement(TracedNamedElement):

    pass
class umlTrace_uml_TracedTrigger(TracedNamedElement):

    pass
class umlTrace_uml_TracedDeploymentTarget(TracedNamedElement):

    pass
class umlTrace_uml_TracedTypedElement(TracedNamedElement):

    pass
class umlTrace_uml_TracedMessage(TracedNamedElement):

    pass
class umlTrace_uml_TracedMessageEnd(TracedNamedElement):

    pass
class umlTrace_uml_TracedNamespace(TracedNamedElement):

    pass
class umlTrace_uml_TracedParameterSet(TracedNamedElement):

    pass
class umlTrace_uml_TracedInteractionFragment(TracedNamedElement):

    pass
class uml_umlTrace_FlowFinalNode:

    pass
class TracedCentralBufferNode:

    pass
class umlTrace_uml_TracedDataStoreNode(TracedCentralBufferNode):

    pass
class TracedCombinedFragment:

    pass
class umlTrace_uml_TracedConsiderIgnoreFragment(TracedCombinedFragment):

    pass
class uml_umlTrace_Expression:

    pass
class TracedValueSpecification:

    pass
class umlTrace_uml_TracedLiteralSpecification(TracedValueSpecification):

    pass
class umlTrace_uml_TracedInstanceValue(TracedValueSpecification):

    pass
class umlTrace_uml_TracedInterval(TracedValueSpecification):

    pass
class umlTrace_uml_TracedOpaqueExpression(TracedValueSpecification):

    pass
class umlTrace_uml_TracedDuration(TracedValueSpecification):

    pass
class umlTrace_uml_TracedTimeExpression(TracedValueSpecification):

    pass
class umlTrace_uml_TracedExpression(TracedValueSpecification):

    pass
class uml_umlTrace_AddStructuralFeatureValueAction:

    pass
class TracedInstanceSpecification:

    pass
class umlTrace_uml_TracedEnumerationLiteral(TracedInstanceSpecification):

    pass
class uml_umlTrace_AcceptEventAction:

    pass
class uml_umlTrace_DurationObservation:

    pass
class uml_TracedNamedElement:

    pass
class umlTrace_uml_TracedExtend(uml_TracedDirectedRelationship, uml_TracedNamedElement):

    pass
class umlTrace_uml_TracedActivityGroup(uml_TracedNamedElement, ActivityContent):

    pass
class umlTrace_uml_TracedInclude(uml_TracedDirectedRelationship, uml_TracedNamedElement):

    pass
class umlTrace_uml_TracedPackageableElement(uml_TracedParameterableElement, uml_TracedNamedElement):

    pass
class TracedObservation:

    pass
class umlTrace_uml_TracedTimeObservation(TracedObservation):

    pass
class umlTrace_uml_TracedDurationObservation(TracedObservation):

    pass
class uml_umlTrace_ActivityFinalNode:

    pass
class TracedFinalNode:

    pass
class umlTrace_uml_TracedFlowFinalNode(TracedFinalNode):

    pass
class umlTrace_uml_TracedActivityFinalNode(TracedFinalNode):

    pass
class uml_umlTrace_SendSignalAction:

    pass
class uml_TracedBehavioredClassifier:

    pass
class umlTrace_uml_TracedClass(uml_TracedEncapsulatedClassifier, uml_TracedBehavioredClassifier):

    pass
class umlTrace_uml_TracedCollaboration(uml_TracedStructuredClassifier, uml_TracedBehavioredClassifier):

    pass
class TracedRealization:

    pass
class umlTrace_uml_TracedSubstitution(TracedRealization):

    pass
class umlTrace_uml_TracedComponentRealization(TracedRealization):

    pass
class umlTrace_uml_TracedInterfaceRealization(TracedRealization):

    pass
class TracedIntervalConstraint:

    pass
class umlTrace_uml_TracedDurationConstraint(TracedIntervalConstraint):

    pass
class umlTrace_uml_TracedTimeConstraint(TracedIntervalConstraint):

    pass
class uml_umlTrace_Artifact:

    pass
class uml_TracedDeployedArtifact:

    pass
class uml_TracedClassifier:

    pass
class umlTrace_uml_TracedAssociation(uml_TracedClassifier, uml_TracedRelationship):

    pass
class umlTrace_uml_TracedArtifact(uml_TracedClassifier, uml_TracedDeployedArtifact):

    pass
class TracedBehavior:

    pass
class umlTrace_uml_TracedStateMachine(TracedBehavior):

    pass
class umlTrace_uml_TracedActivity(TracedBehavior):

    pass
class umlTrace_uml_TracedOpaqueBehavior(TracedBehavior):

    pass
class TracedInvocationAction:

    pass
class umlTrace_uml_TracedCallAction(TracedInvocationAction):

    pass
class umlTrace_uml_TracedBroadcastSignalAction(TracedInvocationAction):

    pass
class umlTrace_uml_TracedSendObjectAction(TracedInvocationAction):

    pass
class umlTrace_uml_TracedSendSignalAction(TracedInvocationAction):

    pass
class uml_umlTrace_RemoveStructuralFeatureValueAction:

    pass
class TracedWriteStructuralFeatureAction:

    pass
class umlTrace_uml_TracedAddStructuralFeatureValueAction(TracedWriteStructuralFeatureAction):

    pass
class umlTrace_uml_TracedRemoveStructuralFeatureValueAction(TracedWriteStructuralFeatureAction):

    pass
class uml_umlTrace_Continuation:

    pass
class TracedInteractionFragment:

    pass
class umlTrace_uml_TracedCombinedFragment(TracedInteractionFragment):

    pass
class umlTrace_uml_TracedStateInvariant(TracedInteractionFragment):

    pass
class umlTrace_uml_TracedInteractionUse(TracedInteractionFragment):

    pass
class umlTrace_uml_TracedOccurrenceSpecification(TracedInteractionFragment):

    pass
class umlTrace_uml_TracedExecutionSpecification(TracedInteractionFragment):

    pass
class umlTrace_uml_TracedContinuation(TracedInteractionFragment):

    pass
class uml_umlTrace_Property:

    pass
class uml_umlTrace_OpaqueAction:

    pass
class uml_TracedDeploymentTarget:

    pass
class umlTrace_uml_TracedInstanceSpecification(uml_TracedPackageableElement, uml_TracedDeployedArtifact, uml_TracedDeploymentTarget):

    pass
class uml_TracedConnectableElement:

    pass
class TracedAssociation:

    pass
class umlTrace_uml_TracedExtension(TracedAssociation):

    pass
class umlTrace_uml_TracedCommunicationPath(TracedAssociation):

    pass
class uml_umlTrace_DataType:

    pass
class TracedClassifier:

    pass
class umlTrace_uml_TracedInterface(TracedClassifier):

    pass
class umlTrace_uml_TracedBehavioredClassifier(TracedClassifier):

    pass
class umlTrace_uml_TracedStructuredClassifier(TracedClassifier):

    pass
class umlTrace_uml_TracedInformationItem(TracedClassifier):

    pass
class umlTrace_uml_TracedSignal(TracedClassifier):

    pass
class umlTrace_uml_TracedDataType(TracedClassifier):

    pass
class TracedOpaqueBehaviorExecution:

    pass
class umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution(TracedOpaqueBehaviorExecution):

    pass
class umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution(TracedOpaqueBehaviorExecution):

    pass
class TracedAction:

    pass
class umlTrace_uml_TracedReadExtentAction(TracedAction):

    pass
class umlTrace_uml_TracedVariableAction(TracedAction):

    pass
class umlTrace_uml_TracedReplyAction(TracedAction):

    pass
class umlTrace_uml_TracedReadLinkObjectEndQualifierAction(TracedAction):

    pass
class umlTrace_uml_TracedLinkAction(TracedAction):

    pass
class umlTrace_uml_TracedStartClassifierBehaviorAction(TracedAction):

    pass
class umlTrace_uml_TracedTestIdentityAction(TracedAction):

    pass
class umlTrace_uml_TracedReduceAction(TracedAction):

    pass
class umlTrace_uml_TracedValueSpecificationAction(TracedAction):

    pass
class umlTrace_uml_TracedCreateObjectAction(TracedAction):

    pass
class umlTrace_uml_TracedReadLinkObjectEndAction(TracedAction):

    pass
class umlTrace_uml_TracedStructuralFeatureAction(TracedAction):

    pass
class umlTrace_uml_TracedReclassifyObjectAction(TracedAction):

    pass
class umlTrace_uml_TracedClearAssociationAction(TracedAction):

    pass
class umlTrace_uml_TracedReadSelfAction(TracedAction):

    pass
class umlTrace_uml_TracedInvocationAction(TracedAction):

    pass
class umlTrace_uml_TracedAcceptEventAction(TracedAction):

    pass
class umlTrace_uml_TracedUnmarshallAction(TracedAction):

    pass
class umlTrace_uml_TracedReadIsClassifiedObjectAction(TracedAction):

    pass
class umlTrace_uml_TracedRaiseExceptionAction(TracedAction):

    pass
class umlTrace_uml_TracedDestroyObjectAction(TracedAction):

    pass
class umlTrace_uml_TracedOpaqueAction(TracedAction):

    pass
class uml_umlTrace_Connector:

    pass
class uml_TracedBehavior:

    pass
class umlTrace_uml_TracedInteraction(uml_TracedInteractionFragment, uml_TracedBehavior):

    pass
class TracedFeature:

    pass
class umlTrace_uml_TracedConnector(TracedFeature):

    pass
class uml_TracedMultiplicityElement:

    pass
class umlTrace_uml_TracedVariable(uml_TracedMultiplicityElement, uml_TracedConnectableElement):

    pass
class umlTrace_uml_TracedPin(uml_TracedObjectNode, uml_TracedMultiplicityElement):

    pass
class umlTrace_uml_TracedParameter(uml_TracedMultiplicityElement, uml_TracedConnectableElement):

    pass
class uml_TracedTypedElement:

    pass
class umlTrace_uml_TracedConnectableElement(uml_TracedTypedElement, uml_TracedParameterableElement):

    pass
class umlTrace_uml_TracedValueSpecification(uml_TracedTypedElement, uml_TracedPackageableElement):

    pass
class uml_TracedFeature:

    pass
class umlTrace_uml_TracedBehavioralFeature(uml_TracedFeature, uml_TracedNamespace):

    pass
class umlTrace_uml_TracedStructuralFeature(uml_TracedTypedElement, uml_TracedMultiplicityElement, uml_TracedFeature):

    pass
class umlTrace_Input_TracedInputParameterValues:

    pass
class umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution(TracedOpaqueBehaviorExecution):

    pass
class TracedActionActivation:

    pass
class umlTrace_BasicActions_TracedInvocationActionActivation(TracedActionActivation):

    pass
class umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation(TracedActionActivation):

    pass
class umlTrace_Loci_TracedExecutionEnvironment:

    pass
class TracedInvocationActionActivation:

    pass
class umlTrace_BasicActions_TracedCallActionActivation(TracedInvocationActionActivation):

    pass
class umlTrace_BasicActions_TracedOpaqueActionActivation(TracedActionActivation):

    pass
class TracedCallActionActivation:

    pass
class umlTrace_BasicActions_TracedCallBehaviorActionActivation(TracedCallActionActivation):

    pass
class TracedPinActivation:

    pass
class umlTrace_BasicActions_TracedInputPinActivation(TracedPinActivation):

    pass
class umlTrace_BasicActions_TracedOutputPinActivation(TracedPinActivation):

    pass
class umlTrace_IntermediateActions_TracedCreateObjectActionActivation(TracedActionActivation):

    pass
class TracedWriteStructuralFeatureActionActivation:

    pass
class umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation(TracedWriteStructuralFeatureActionActivation):

    pass
class TracedStructuralFeatureActionActivation:

    pass
class umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation(TracedStructuralFeatureActionActivation):

    pass
class umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation(TracedStructuralFeatureActionActivation):

    pass
class umlTrace_IntermediateActions_TracedValueSpecificationActionActivation(TracedActionActivation):

    pass
class umlTrace_Loci_TracedExecutor:

    pass
class umlTrace_Loci_TracedSemanticVisitor:

    pass
class umlTrace_Loci_TracedLocus:

    pass
class umlTrace_Loci_TracedExecutionFactory:

    pass
class umlTrace_IntermediateActivities_TracedToken:

    pass
class umlTrace_IntermediateActivities_TracedActivityEdgeInstance:

    pass
class TracedObjectNodeActivation:

    pass
class umlTrace_BasicActions_TracedPinActivation(TracedObjectNodeActivation):

    pass
class umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation(TracedObjectNodeActivation):

    pass
class umlTrace_IntermediateActivities_TracedOffer:

    pass
class umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup:

    pass
class TracedActivityNodeActivation:

    pass
class umlTrace_IntermediateActivities_TracedControlNodeActivation(TracedActivityNodeActivation):

    pass
class umlTrace_BasicActions_TracedActionActivation(TracedActivityNodeActivation):

    pass
class umlTrace_IntermediateActivities_TracedObjectNodeActivation(TracedActivityNodeActivation):

    pass
class TracedControlNodeActivation:

    pass
class umlTrace_IntermediateActivities_TracedMergeNodeActivation(TracedControlNodeActivation):

    pass
class umlTrace_IntermediateActivities_TracedDecisionNodeActivation(TracedControlNodeActivation):

    pass
class umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation(TracedControlNodeActivation):

    pass
class umlTrace_IntermediateActivities_TracedForkNodeActivation(TracedControlNodeActivation):

    pass
class umlTrace_IntermediateActivities_TracedInitialNodeActivation(TracedControlNodeActivation):

    pass
class umlTrace_IntermediateActivities_TracedJoinNodeActivation(TracedControlNodeActivation):

    pass
class TracedToken:

    pass
class umlTrace_IntermediateActivities_TracedControlToken(TracedToken):

    pass
class umlTrace_IntermediateActivities_TracedObjectToken(TracedToken):

    pass
class umlTrace_IntermediateActivities_TracedForkedToken(TracedToken):

    pass
class TracedObject:

    pass
class umlTrace_BasicBehaviors_TracedExecution(TracedObject):

    pass
class umlTrace_BasicBehaviors_TracedParameterValue:

    pass
class TracedExecution:

    pass
class umlTrace_IntermediateActivities_TracedActivityExecution(TracedExecution):

    pass
class umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution(TracedExecution):

    pass
class TracedCompoundValue:

    pass
class umlTrace_Kernel_TracedExtensionalValue(TracedCompoundValue):

    pass
class umlTrace_Kernel_TracedFeatureValue(ABC):

    pass
class TracedStructuredValue:

    pass
class umlTrace_Kernel_TracedCompoundValue(TracedStructuredValue):

    pass
class umlTrace_Kernel_TracedReference(TracedStructuredValue):

    pass
class TracedLiteralEvaluation:

    pass
class umlTrace_Kernel_TracedLiteralIntegerEvaluation(TracedLiteralEvaluation):

    pass
class umlTrace_Kernel_TracedLiteralBooleanEvaluation(TracedLiteralEvaluation):

    pass
class TracedValue:

    pass
class umlTrace_Kernel_TracedStructuredValue(TracedValue):

    pass
class umlTrace_Kernel_TracedPrimitiveValue(TracedValue):

    pass
class TracedSemanticVisitor:

    pass
class umlTrace_IntermediateActivities_TracedActivityNodeActivation(TracedSemanticVisitor):

    pass
class umlTrace_Kernel_TracedEvaluation(TracedSemanticVisitor):

    pass
class umlTrace_Kernel_TracedValue(TracedSemanticVisitor):

    pass
class TracedEvaluation:

    pass
class umlTrace_Kernel_TracedLiteralEvaluation(TracedEvaluation):

    pass
class TracedPrimitiveValue:

    pass
class umlTrace_Kernel_TracedBooleanValue(TracedPrimitiveValue):

    pass
class umlTrace_Kernel_TracedIntegerValue(TracedPrimitiveValue):

    pass
class uml_TracedActor:

    pass
class TracedExtensionalValue:

    pass
class umlTrace_Kernel_TracedObject(TracedExtensionalValue):

    pass
class uml_TracedCentralBufferNode:

    pass
class uml_TracedUnmarshallAction:

    pass
class uml_TracedBehaviorExecutionSpecification:

    pass
class uml_TracedDeploymentSpecification:

    pass
class uml_TracedFunctionBehavior:

    pass
class uml_TracedOpaqueExpression:

    pass
class Kernel_TracedLiteralIntegerEvaluation:

    pass
class uml_TracedLinkEndCreationData:

    pass
class uml_TracedClearStructuralFeatureAction:

    pass
class uml_TracedTemplateBinding:

    pass
class uml_TracedActivity:

    pass
class uml_TracedAcceptCallAction:

    pass
class uml_TracedReadSelfAction:

    pass
class uml_TracedActionExecutionSpecification:

    pass
class uml_TracedConnectionPointReference:

    pass
class uml_TracedSubstitution:

    pass
class uml_TracedDevice:

    pass
class uml_TracedReclassifyObjectAction:

    pass
class uml_TracedCallBehaviorAction:

    pass
class uml_TracedGeneralOrdering:

    pass
class uml_TracedGate:

    pass
class uml_TracedInteractionUse:

    pass
class uml_TracedRemoveVariableValueAction:

    pass
class uml_TracedLiteralReal:

    pass
class uml_TracedStateInvariant:

    pass
class uml_TracedAssociation:

    pass
class uml_TracedControlFlow:

    pass
class uml_TracedVariable:

    pass
class uml_TracedExceptionHandler:

    pass
class uml_TracedExecutionOccurrenceSpecification:

    pass
class uml_TracedPackageImport:

    pass
class uml_TracedOperation:

    pass
class uml_TracedReception:

    pass
class uml_TracedTestIdentityAction:

    pass
class uml_TracedClearAssociationAction:

    pass
class uml_TracedAddVariableValueAction:

    pass
class uml_TracedRaiseExceptionAction:

    pass
class uml_TracedDestroyObjectAction:

    pass
class uml_TracedExpansionNode:

    pass
class uml_TracedLiteralNull:

    pass
class uml_TracedComment:

    pass
class uml_TracedSignal:

    pass
class uml_TracedForkNode:

    pass
class uml_TracedChangeEvent:

    pass
class uml_TracedObjectFlow:

    pass
class uml_TracedModel:

    pass
class uml_TracedPackageMerge:

    pass
class uml_TracedNode:

    pass
class uml_TracedLinkEndData:

    pass
class uml_TracedTransition:

    pass
class BasicActions_TracedInputPinActivation:

    pass
class uml_TracedReadExtentAction:

    pass
class uml_TracedManifestation:

    pass
class IntermediateActions_TracedCreateObjectActionActivation:

    pass
class uml_TracedTimeExpression:

    pass
class uml_TracedDependency:

    pass
class uml_TracedInstanceValue:

    pass
class uml_TracedClause:

    pass
class uml_TracedCombinedFragment:

    pass
class IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution:

    pass
class uml_TracedFinalState:

    pass
class uml_TracedReplyAction:

    pass
class uml_TracedUseCase:

    pass
class uml_TracedPseudostate:

    pass
class uml_TracedInformationFlow:

    pass
class uml_TracedInteractionOperand:

    pass
class IntermediateActivities_TracedActivityParameterNodeActivation:

    pass
class uml_TracedDestroyLinkAction:

    pass
class uml_TracedInterruptibleActivityRegion:

    pass
class uml_TracedRegion:

    pass
class uml_TracedValueSpecificationAction:

    pass
class uml_TracedDecisionNode:

    pass
class uml_TracedValuePin:

    pass
class uml_TracedOutputPin:

    pass
class uml_TracedProtocolStateMachine:

    pass
class uml_TracedReadIsClassifiedObjectAction:

    pass
class IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution:

    pass
class uml_TracedCallOperationAction:

    pass
class uml_TracedInstanceSpecification:

    pass
class uml_TracedIntervalConstraint:

    pass
class IntermediateActivities_TracedForkNodeActivation:

    pass
class uml_TracedInterval:

    pass
class uml_TracedProfile:

    pass
class uml_TracedConnectorEnd:

    pass
class uml_TracedTrigger:

    pass
class uml_TracedActionInputPin:

    pass
class uml_TracedImage:

    pass
class uml_TracedDurationConstraint:

    pass
class uml_TracedMessageOccurrenceSpecification:

    pass
class uml_TracedQualifierValue:

    pass
class uml_TracedLiteralBoolean:

    pass
class uml_TracedTemplateParameter:

    pass
class uml_TracedProfileApplication:

    pass
class IntermediateActivities_TracedDecisionNodeActivation:

    pass
class uml_TracedClearVariableAction:

    pass
class uml_TracedLiteralInteger:

    pass
class uml_TracedInitialNode:

    pass
class uml_TracedOperationTemplateParameter:

    pass
class uml_TracedMessage:

    pass
class uml_TracedReadVariableAction:

    pass
class uml_TracedExtend:

    pass
class uml_TracedTemplateParameterSubstitution:

    pass
class uml_TracedReadLinkObjectEndQualifierAction:

    pass
class Kernel_TracedLiteralBooleanEvaluation:

    pass
class uml_TracedPartDecomposition:

    pass
class uml_TracedGeneralization:

    pass
class uml_TracedCreateLinkAction:

    pass
class uml_TracedRedefinableTemplateSignature:

    pass
class uml_TracedMergeNode:

    pass
class uml_TracedReadStructuralFeatureAction:

    pass
class uml_TracedParameterSet:

    pass
class BasicActions_TracedOpaqueActionActivation:

    pass
class uml_TracedAbstraction:

    pass
class uml_TracedStructuredActivityNode:

    pass
class uml_TracedLiteralUnlimitedNatural:

    pass
class uml_TracedUsage:

    pass
class uml_TracedDuration:

    pass
class uml_TracedDestructionOccurrenceSpecification:

    pass
class uml_TracedInclude:

    pass
class IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution:

    pass
class uml_TracedActivityParameterNode:

    pass
class uml_TracedClassifierTemplateParameter:

    pass
class IntermediateActions_TracedAddStructuralFeatureValueActionActivation:

    pass
class BasicActions_TracedCallBehaviorActionActivation:

    pass
class uml_TracedState:

    pass
class uml_TracedLoopNode:

    pass
class uml_TracedDurationInterval:

    pass
class uml_TracedLinkEndDestructionData:

    pass
class uml_TracedActivityPartition:

    pass
class uml_TracedCollaborationUse:

    pass
class uml_TracedEnumeration:

    pass
class uml_TracedProtocolConformance:

    pass
class uml_TracedCallEvent:

    pass
class uml_TracedStartClassifierBehaviorAction:

    pass
class uml_TracedExpansionRegion:

    pass
class uml_TracedCreateLinkObjectAction:

    pass
class IntermediateActivities_TracedControlToken:

    pass
class uml_TracedTimeObservation:

    pass
class uml_TracedLifeline:

    pass
class uml_TracedSendObjectAction:

    pass
class uml_TracedConnectableElementTemplateParameter:

    pass
class uml_TracedAnyReceiveEvent:

    pass
class uml_TracedReadLinkObjectEndAction:

    pass
class uml_TracedRealization:

    pass
class uml_TracedLiteralString:

    pass
class uml_TracedInteraction:

    pass
class IntermediateActivities_TracedMergeNodeActivation:

    pass
class uml_TracedStateMachine:

    pass
class uml_TracedExtensionEnd:

    pass
class uml_TracedComponent:

    pass
class uml_TracedOccurrenceSpecification:

    pass
class umlTrace_uml_TracedMessageOccurrenceSpecification(uml_TracedOccurrenceSpecification, uml_TracedMessageEnd):

    pass
class uml_TracedExecutionEnvironment:

    pass
class uml_TracedConditionalNode:

    pass
class uml_TracedInterface:

    pass
class uml_TracedStereotype:

    pass
class IntermediateActions_TracedReadStructuralFeatureActionActivation:

    pass
class uml_TracedStringExpression:

    pass
class IntermediateActions_TracedValueSpecificationActionActivation:

    pass
class uml_TracedComponentRealization:

    pass
class uml_TracedInteractionConstraint:

    pass
class uml_TracedCreateObjectAction:

    pass
class uml_TracedElementImport:

    pass
class uml_TracedStartObjectBehaviorAction:

    pass
class BasicActions_TracedOutputPinActivation:

    pass
class uml_TracedJoinNode:

    pass
class uml_TracedExtensionPoint:

    pass
class uml_TracedSignalEvent:

    pass
class uml_TracedSlot:

    pass
class uml_TracedAssociationClass:

    pass
class uml_TracedTimeEvent:

    pass
class uml_TracedSequenceNode:

    pass
class uml_TracedInputPin:

    pass
class uml_TracedReduceAction:

    pass
class uml_TracedGeneralizationSet:

    pass
class uml_TracedConstraint:

    pass
class uml_TracedPackage:

    pass
class IntermediateActivities_TracedActivityFinalNodeActivation:

    pass
class uml_TracedProtocolTransition:

    pass
class uml_TracedExpression:

    pass
class umlTrace_uml_TracedStringExpression(uml_TracedTemplateableElement, uml_TracedExpression):

    pass
class uml_TracedReadLinkAction:

    pass
class uml_TracedExtension:

    pass
class uml_TracedTimeInterval:

    pass
class uml_TracedPort:

    pass
class uml_TracedDeployment:

    pass
class uml_TracedBroadcastSignalAction:

    pass
class uml_TracedTemplateSignature:

    pass
class umlTrace_uml_TracedRedefinableTemplateSignature(uml_TracedRedefinableElement, uml_TracedTemplateSignature):

    pass
class uml_TracedCollaboration:

    pass
class uml_TracedInformationItem:

    pass
class uml_TracedFlowFinalNode:

    pass
class uml_TracedDataStoreNode:

    pass
class uml_TracedConsiderIgnoreFragment:

    pass
class uml_TracedOpaqueBehavior:

    pass
class uml_TracedAddStructuralFeatureValueAction:

    pass
class uml_TracedEnumerationLiteral:

    pass
class uml_TracedAcceptEventAction:

    pass
class IntermediateActivities_TracedInitialNodeActivation:

    pass
class uml_TracedDurationObservation:

    pass
class uml_TracedActivityFinalNode:

    pass
class uml_TracedInterfaceRealization:

    pass
class uml_TracedTimeConstraint:

    pass
class IntermediateActivities_TracedJoinNodeActivation:

    pass
class uml_TracedArtifact:

    pass
class Loci_TracedExecutionEnvironment:

    pass
class uml_TracedSendSignalAction:

    pass
class uml_TracedRemoveStructuralFeatureValueAction:

    pass
class uml_TracedContinuation:

    pass
class uml_TracedProperty:

    pass
class uml_TracedCommunicationPath:

    pass
class uml_TracedDataType:

    pass
class uml_TracedOpaqueAction:

    pass
class uml_TracedConnector:

    pass
class umlTrace_Traced_TracedObjects:

    pass
class umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value:

    pass
class umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value:

    pass
class umlTrace_Values_ActivityExecution_activationGroup_Value:

    pass
class umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value:

    pass
class umlTrace_Values_ActivityNodeActivation_running_Value:

    def __init__(self, running: bool, fumlConfiguration417: "IntermediateActivities_TracedActivityNodeActivation" = None, activityNodeActivation_running_Values: set["Values_umlTrace_State"] = None):
        self.running = running
        self.fumlConfiguration417 = fumlConfiguration417
        self.activityNodeActivation_running_Values = activityNodeActivation_running_Values if activityNodeActivation_running_Values is not None else set()
        
    @property
    def running(self) -> bool:
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running

    @property
    def activityNodeActivation_running_Values(self):
        return self.__activityNodeActivation_running_Values

    @activityNodeActivation_running_Values.setter
    def activityNodeActivation_running_Values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_ActivityNodeActivation_running_Value__activityNodeActivation_running_Values", None)
        self.__activityNodeActivation_running_Values = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State420"):
                    opp_val = getattr(item, "State420", None)
                    
                    if opp_val == self:
                        setattr(item, "State420", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State420"):
                    opp_val = getattr(item, "State420", None)
                    
                    setattr(item, "State420", self)
                    

    @property
    def fumlConfiguration417(self):
        return self.__fumlConfiguration417

    @fumlConfiguration417.setter
    def fumlConfiguration417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_ActivityNodeActivation_running_Value__fumlConfiguration417", None)
        self.__fumlConfiguration417 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced418"):
                opp_val = getattr(old_value, "Traced418", None)
                if opp_val == self:
                    setattr(old_value, "Traced418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced418"):
                opp_val = getattr(value, "Traced418", None)
                setattr(value, "Traced418", self)

class umlTrace_Values_ActivityNodeActivation_incomingEdges_Value:

    pass
class umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value:

    pass
class umlTrace_Values_ActivityNodeActivation_isRunning_Value:

    def __init__(self, isRunning: bool, fumlConfiguration422: "IntermediateActivities_TracedActivityNodeActivation" = None, activityNodeActivation_isRunning_Values: set["Values_umlTrace_State"] = None):
        self.isRunning = isRunning
        self.fumlConfiguration422 = fumlConfiguration422
        self.activityNodeActivation_isRunning_Values = activityNodeActivation_isRunning_Values if activityNodeActivation_isRunning_Values is not None else set()
        
    @property
    def isRunning(self) -> bool:
        return self.__isRunning

    @isRunning.setter
    def isRunning(self, isRunning: bool):
        self.__isRunning = isRunning

    @property
    def activityNodeActivation_isRunning_Values(self):
        return self.__activityNodeActivation_isRunning_Values

    @activityNodeActivation_isRunning_Values.setter
    def activityNodeActivation_isRunning_Values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_ActivityNodeActivation_isRunning_Value__activityNodeActivation_isRunning_Values", None)
        self.__activityNodeActivation_isRunning_Values = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State425"):
                    opp_val = getattr(item, "State425", None)
                    
                    if opp_val == self:
                        setattr(item, "State425", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State425"):
                    opp_val = getattr(item, "State425", None)
                    
                    setattr(item, "State425", self)
                    

    @property
    def fumlConfiguration422(self):
        return self.__fumlConfiguration422

    @fumlConfiguration422.setter
    def fumlConfiguration422(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_ActivityNodeActivation_isRunning_Value__fumlConfiguration422", None)
        self.__fumlConfiguration422 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced423"):
                opp_val = getattr(old_value, "Traced423", None)
                if opp_val == self:
                    setattr(old_value, "Traced423", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced423"):
                opp_val = getattr(value, "Traced423", None)
                setattr(value, "Traced423", self)

class Input_TracedInputParameterValues:

    pass
class umlTrace_Values_InputParameterValues_name_Value:

    def __init__(self, name: str, fumlConfiguration392: "Input_TracedInputParameterValues" = None, inputParameterValues_name_Values: set["Values_umlTrace_State"] = None):
        self.name = name
        self.fumlConfiguration392 = fumlConfiguration392
        self.inputParameterValues_name_Values = inputParameterValues_name_Values if inputParameterValues_name_Values is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def inputParameterValues_name_Values(self):
        return self.__inputParameterValues_name_Values

    @inputParameterValues_name_Values.setter
    def inputParameterValues_name_Values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_InputParameterValues_name_Value__inputParameterValues_name_Values", None)
        self.__inputParameterValues_name_Values = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State395"):
                    opp_val = getattr(item, "State395", None)
                    
                    if opp_val == self:
                        setattr(item, "State395", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State395"):
                    opp_val = getattr(item, "State395", None)
                    
                    setattr(item, "State395", self)
                    

    @property
    def fumlConfiguration392(self):
        return self.__fumlConfiguration392

    @fumlConfiguration392.setter
    def fumlConfiguration392(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_InputParameterValues_name_Value__fumlConfiguration392", None)
        self.__fumlConfiguration392 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced393"):
                opp_val = getattr(old_value, "Traced393", None)
                if opp_val == self:
                    setattr(old_value, "Traced393", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced393"):
                opp_val = getattr(value, "Traced393", None)
                setattr(value, "Traced393", self)

class uml_TracedActivityNode:

    pass
class umlTrace_uml_TracedObjectNode(uml_TracedTypedElement, uml_TracedActivityNode):

    pass
class umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value:

    pass
class umlTrace_Values_ActivityNodeActivation_heldTokens_Value:

    pass
class umlTrace_Values_InputParameterValues_parameterValues_Value:

    pass
class umlTrace_Values_ActivityEdgeInstance_source_Value:

    pass
class uml_TracedActivityEdge:

    pass
class umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value:

    pass
class umlTrace_Values_ActivityEdgeInstance_target_Value:

    pass
class umlTrace_Values_PinActivation_actionActivation_Value:

    pass
class umlTrace_Values_ActivityEdgeInstance_offers_Value:

    pass
class umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value:

    pass
class umlTrace_Values_PinActivation_count_temp_Value:

    def __init__(self, count_temp: int, fumlConfiguration355: "BasicActions_TracedPinActivation" = None, pinActivation_count_temp_Values: set["Values_umlTrace_State"] = None):
        self.count_temp = count_temp
        self.fumlConfiguration355 = fumlConfiguration355
        self.pinActivation_count_temp_Values = pinActivation_count_temp_Values if pinActivation_count_temp_Values is not None else set()
        
    @property
    def count_temp(self) -> int:
        return self.__count_temp

    @count_temp.setter
    def count_temp(self, count_temp: int):
        self.__count_temp = count_temp

    @property
    def pinActivation_count_temp_Values(self):
        return self.__pinActivation_count_temp_Values

    @pinActivation_count_temp_Values.setter
    def pinActivation_count_temp_Values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_PinActivation_count_temp_Value__pinActivation_count_temp_Values", None)
        self.__pinActivation_count_temp_Values = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State358"):
                    opp_val = getattr(item, "State358", None)
                    
                    if opp_val == self:
                        setattr(item, "State358", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State358"):
                    opp_val = getattr(item, "State358", None)
                    
                    setattr(item, "State358", self)
                    

    @property
    def fumlConfiguration355(self):
        return self.__fumlConfiguration355

    @fumlConfiguration355.setter
    def fumlConfiguration355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_PinActivation_count_temp_Value__fumlConfiguration355", None)
        self.__fumlConfiguration355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced356"):
                opp_val = getattr(old_value, "Traced356", None)
                if opp_val == self:
                    setattr(old_value, "Traced356", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced356"):
                opp_val = getattr(value, "Traced356", None)
                setattr(value, "Traced356", self)

class umlTrace_Values_Offer_offeredTokens_Value:

    pass
class umlTrace_Values_FeatureValue_position_Value:

    def __init__(self, position: int, fumlConfiguration344: "Kernel_TracedFeatureValue" = None, featureValue_position_Values: set["Values_umlTrace_State"] = None):
        self.position = position
        self.fumlConfiguration344 = fumlConfiguration344
        self.featureValue_position_Values = featureValue_position_Values if featureValue_position_Values is not None else set()
        
    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def fumlConfiguration344(self):
        return self.__fumlConfiguration344

    @fumlConfiguration344.setter
    def fumlConfiguration344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_FeatureValue_position_Value__fumlConfiguration344", None)
        self.__fumlConfiguration344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced345"):
                opp_val = getattr(old_value, "Traced345", None)
                if opp_val == self:
                    setattr(old_value, "Traced345", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced345"):
                opp_val = getattr(value, "Traced345", None)
                setattr(value, "Traced345", self)

    @property
    def featureValue_position_Values(self):
        return self.__featureValue_position_Values

    @featureValue_position_Values.setter
    def featureValue_position_Values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_FeatureValue_position_Value__featureValue_position_Values", None)
        self.__featureValue_position_Values = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State347"):
                    opp_val = getattr(item, "State347", None)
                    
                    if opp_val == self:
                        setattr(item, "State347", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State347"):
                    opp_val = getattr(item, "State347", None)
                    
                    setattr(item, "State347", self)
                    

class uml_TracedStructuralFeature:

    pass
class umlTrace_uml_TracedProperty(uml_TracedStructuralFeature, uml_TracedConnectableElement, uml_TracedDeploymentTarget):

    pass
class umlTrace_Values_FeatureValue_feature_Value:

    pass
class umlTrace_Values_FeatureValue_values_FeatureValue_Value:

    pass
class IntermediateActivities_TracedOffer:

    pass
class umlTrace_Values_ObjectToken_value_Value:

    pass
class umlTrace_Values_Token_holder_Value:

    pass
class Kernel_TracedCompoundValue:

    pass
class Kernel_TracedFeatureValue:

    pass
class umlTrace_Values_CompoundValue_featureValues_Value:

    pass
class BasicActions_TracedCallActionActivation:

    pass
class umlTrace_Values_CallActionActivation_callExecutions_Value:

    pass
class IntermediateActivities_TracedObjectToken:

    pass
class umlTrace_Values_PrimitiveValue_type_Value:

    pass
class Kernel_TracedBooleanValue:

    pass
class umlTrace_Values_BooleanValue_value_BooleanValue_Value:

    def __init__(self, value_BooleanValue: bool, fumlConfiguration293: "Kernel_TracedBooleanValue" = None, booleanValue_value_BooleanValue_Values: set["Values_umlTrace_State"] = None):
        self.value_BooleanValue = value_BooleanValue
        self.fumlConfiguration293 = fumlConfiguration293
        self.booleanValue_value_BooleanValue_Values = booleanValue_value_BooleanValue_Values if booleanValue_value_BooleanValue_Values is not None else set()
        
    @property
    def value_BooleanValue(self) -> bool:
        return self.__value_BooleanValue

    @value_BooleanValue.setter
    def value_BooleanValue(self, value_BooleanValue: bool):
        self.__value_BooleanValue = value_BooleanValue

    @property
    def booleanValue_value_BooleanValue_Values(self):
        return self.__booleanValue_value_BooleanValue_Values

    @booleanValue_value_BooleanValue_Values.setter
    def booleanValue_value_BooleanValue_Values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_BooleanValue_value_BooleanValue_Value__booleanValue_value_BooleanValue_Values", None)
        self.__booleanValue_value_BooleanValue_Values = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State296"):
                    opp_val = getattr(item, "State296", None)
                    
                    if opp_val == self:
                        setattr(item, "State296", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State296"):
                    opp_val = getattr(item, "State296", None)
                    
                    setattr(item, "State296", self)
                    

    @property
    def fumlConfiguration293(self):
        return self.__fumlConfiguration293

    @fumlConfiguration293.setter
    def fumlConfiguration293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_BooleanValue_value_BooleanValue_Value__fumlConfiguration293", None)
        self.__fumlConfiguration293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced294"):
                opp_val = getattr(old_value, "Traced294", None)
                if opp_val == self:
                    setattr(old_value, "Traced294", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced294"):
                opp_val = getattr(value, "Traced294", None)
                setattr(value, "Traced294", self)

class umlTrace_Values_Evaluation_locus_Evaluation_Value:

    pass
class Kernel_TracedEvaluation:

    pass
class uml_TracedValueSpecification:

    pass
class umlTrace_Values_Evaluation_specification_Evaluation_Value:

    pass
class Kernel_TracedPrimitiveValue:

    pass
class IntermediateActivities_TracedActivityNodeActivation:

    pass
class umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value:

    pass
class umlTrace_Values_Executor_locus_Executor_Value:

    pass
class IntermediateActivities_TracedActivityEdgeInstance:

    pass
class umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value:

    pass
class IntermediateActivities_TracedActivityExecution:

    pass
class umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value:

    pass
class IntermediateActivities_TracedActivityNodeActivationGroup:

    pass
class umlTrace_Values_ActionActivation_firing_Value:

    def __init__(self, firing: bool, fumlConfiguration225: "BasicActions_TracedActionActivation" = None, actionActivation_firing_Values: set["Values_umlTrace_State"] = None):
        self.firing = firing
        self.fumlConfiguration225 = fumlConfiguration225
        self.actionActivation_firing_Values = actionActivation_firing_Values if actionActivation_firing_Values is not None else set()
        
    @property
    def firing(self) -> bool:
        return self.__firing

    @firing.setter
    def firing(self, firing: bool):
        self.__firing = firing

    @property
    def actionActivation_firing_Values(self):
        return self.__actionActivation_firing_Values

    @actionActivation_firing_Values.setter
    def actionActivation_firing_Values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_ActionActivation_firing_Value__actionActivation_firing_Values", None)
        self.__actionActivation_firing_Values = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State228"):
                    opp_val = getattr(item, "State228", None)
                    
                    if opp_val == self:
                        setattr(item, "State228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State228"):
                    opp_val = getattr(item, "State228", None)
                    
                    setattr(item, "State228", self)
                    

    @property
    def fumlConfiguration225(self):
        return self.__fumlConfiguration225

    @fumlConfiguration225.setter
    def fumlConfiguration225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_ActionActivation_firing_Value__fumlConfiguration225", None)
        self.__fumlConfiguration225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced226"):
                opp_val = getattr(old_value, "Traced226", None)
                if opp_val == self:
                    setattr(old_value, "Traced226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced226"):
                opp_val = getattr(value, "Traced226", None)
                setattr(value, "Traced226", self)

class umlTrace_Values_Element_semanticVisitor_Value:

    pass
class umlTrace_Values_Execution_context_Value:

    pass
class BasicBehaviors_TracedExecution:

    pass
class umlTrace_Values_Execution_parameterValues_Value:

    pass
class Loci_TracedSemanticVisitor:

    pass
class BasicActions_TracedActionActivation:

    pass
class BasicActions_TracedPinActivation:

    pass
class umlTrace_Values_ActionActivation_pinActivations_Value:

    pass
class uml_TracedParameter:

    pass
class umlTrace_Values_ParameterValue_parameter_ParameterValue_Value:

    pass
class BasicBehaviors_TracedParameterValue:

    pass
class Kernel_TracedValue:

    pass
class umlTrace_Values_ParameterValue_values_ParameterValue_Value:

    pass
class uml_TracedElement:

    pass
class umlTrace_Values_SemanticVisitor_runtimeModelElement_Value:

    pass
class IntermediateActivities_TracedObjectNodeActivation:

    pass
class umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value:

    def __init__(self, offeredTokenCount: int, fumlConfiguration196: "IntermediateActivities_TracedObjectNodeActivation" = None, objectNodeActivation_offeredTokenCount_Values: set["Values_umlTrace_State"] = None):
        self.offeredTokenCount = offeredTokenCount
        self.fumlConfiguration196 = fumlConfiguration196
        self.objectNodeActivation_offeredTokenCount_Values = objectNodeActivation_offeredTokenCount_Values if objectNodeActivation_offeredTokenCount_Values is not None else set()
        
    @property
    def offeredTokenCount(self) -> int:
        return self.__offeredTokenCount

    @offeredTokenCount.setter
    def offeredTokenCount(self, offeredTokenCount: int):
        self.__offeredTokenCount = offeredTokenCount

    @property
    def objectNodeActivation_offeredTokenCount_Values(self):
        return self.__objectNodeActivation_offeredTokenCount_Values

    @objectNodeActivation_offeredTokenCount_Values.setter
    def objectNodeActivation_offeredTokenCount_Values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value__objectNodeActivation_offeredTokenCount_Values", None)
        self.__objectNodeActivation_offeredTokenCount_Values = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State199"):
                    opp_val = getattr(item, "State199", None)
                    
                    if opp_val == self:
                        setattr(item, "State199", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State199"):
                    opp_val = getattr(item, "State199", None)
                    
                    setattr(item, "State199", self)
                    

    @property
    def fumlConfiguration196(self):
        return self.__fumlConfiguration196

    @fumlConfiguration196.setter
    def fumlConfiguration196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value__fumlConfiguration196", None)
        self.__fumlConfiguration196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced197"):
                opp_val = getattr(old_value, "Traced197", None)
                if opp_val == self:
                    setattr(old_value, "Traced197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced197"):
                opp_val = getattr(value, "Traced197", None)
                setattr(value, "Traced197", self)

class Loci_TracedExecutor:

    pass
class umlTrace_Values_Locus_executor_Value:

    pass
class Kernel_TracedExtensionalValue:

    pass
class umlTrace_Values_Locus_extensionalValues_Value:

    pass
class umlTrace_Values_Locus_factory_Value:

    pass
class Loci_TracedLocus:

    pass
class umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value:

    pass
class BasicBehaviors_TracedOpaqueBehaviorExecution:

    pass
class umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value:

    pass
class Loci_TracedExecutionFactory:

    pass
class uml_TracedPrimitiveType:

    pass
class umlTrace_Values_ExecutionFactory_builtInTypes_Value:

    pass
class Kernel_TracedReference:

    pass
class umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value:

    def __init__(self, baseTokenIsWithdrawn: bool, forkedToken_baseTokenIsWithdrawn_Values: set["Values_umlTrace_State"] = None, fumlConfiguration155: "IntermediateActivities_TracedForkedToken" = None):
        self.baseTokenIsWithdrawn = baseTokenIsWithdrawn
        self.forkedToken_baseTokenIsWithdrawn_Values = forkedToken_baseTokenIsWithdrawn_Values if forkedToken_baseTokenIsWithdrawn_Values is not None else set()
        self.fumlConfiguration155 = fumlConfiguration155
        
    @property
    def baseTokenIsWithdrawn(self) -> bool:
        return self.__baseTokenIsWithdrawn

    @baseTokenIsWithdrawn.setter
    def baseTokenIsWithdrawn(self, baseTokenIsWithdrawn: bool):
        self.__baseTokenIsWithdrawn = baseTokenIsWithdrawn

    @property
    def fumlConfiguration155(self):
        return self.__fumlConfiguration155

    @fumlConfiguration155.setter
    def fumlConfiguration155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value__fumlConfiguration155", None)
        self.__fumlConfiguration155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced156"):
                opp_val = getattr(old_value, "Traced156", None)
                if opp_val == self:
                    setattr(old_value, "Traced156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced156"):
                opp_val = getattr(value, "Traced156", None)
                setattr(value, "Traced156", self)

    @property
    def forkedToken_baseTokenIsWithdrawn_Values(self):
        return self.__forkedToken_baseTokenIsWithdrawn_Values

    @forkedToken_baseTokenIsWithdrawn_Values.setter
    def forkedToken_baseTokenIsWithdrawn_Values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value__forkedToken_baseTokenIsWithdrawn_Values", None)
        self.__forkedToken_baseTokenIsWithdrawn_Values = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State158"):
                    opp_val = getattr(item, "State158", None)
                    
                    if opp_val == self:
                        setattr(item, "State158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State158"):
                    opp_val = getattr(item, "State158", None)
                    
                    setattr(item, "State158", self)
                    

class IntermediateActivities_TracedToken:

    pass
class umlTrace_Values_ForkedToken_baseToken_Value:

    pass
class IntermediateActivities_TracedForkedToken:

    pass
class umlTrace_Values_ForkedToken_remainingOffersCount_Value:

    def __init__(self, remainingOffersCount: int, fumlConfiguration144: "IntermediateActivities_TracedForkedToken" = None, forkedToken_remainingOffersCount_Values: set["Values_umlTrace_State"] = None):
        self.remainingOffersCount = remainingOffersCount
        self.fumlConfiguration144 = fumlConfiguration144
        self.forkedToken_remainingOffersCount_Values = forkedToken_remainingOffersCount_Values if forkedToken_remainingOffersCount_Values is not None else set()
        
    @property
    def remainingOffersCount(self) -> int:
        return self.__remainingOffersCount

    @remainingOffersCount.setter
    def remainingOffersCount(self, remainingOffersCount: int):
        self.__remainingOffersCount = remainingOffersCount

    @property
    def forkedToken_remainingOffersCount_Values(self):
        return self.__forkedToken_remainingOffersCount_Values

    @forkedToken_remainingOffersCount_Values.setter
    def forkedToken_remainingOffersCount_Values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_ForkedToken_remainingOffersCount_Value__forkedToken_remainingOffersCount_Values", None)
        self.__forkedToken_remainingOffersCount_Values = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State147"):
                    opp_val = getattr(item, "State147", None)
                    
                    if opp_val == self:
                        setattr(item, "State147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State147"):
                    opp_val = getattr(item, "State147", None)
                    
                    setattr(item, "State147", self)
                    

    @property
    def fumlConfiguration144(self):
        return self.__fumlConfiguration144

    @fumlConfiguration144.setter
    def fumlConfiguration144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_ForkedToken_remainingOffersCount_Value__fumlConfiguration144", None)
        self.__fumlConfiguration144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced145"):
                opp_val = getattr(old_value, "Traced145", None)
                if opp_val == self:
                    setattr(old_value, "Traced145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced145"):
                opp_val = getattr(value, "Traced145", None)
                setattr(value, "Traced145", self)

class Kernel_TracedIntegerValue:

    pass
class umlTrace_Values_IntegerValue_value_IntegerValue_Value:

    def __init__(self, value_IntegerValue: int, fumlConfiguration139: "Kernel_TracedIntegerValue" = None, integerValue_value_IntegerValue_Values: set["Values_umlTrace_State"] = None):
        self.value_IntegerValue = value_IntegerValue
        self.fumlConfiguration139 = fumlConfiguration139
        self.integerValue_value_IntegerValue_Values = integerValue_value_IntegerValue_Values if integerValue_value_IntegerValue_Values is not None else set()
        
    @property
    def value_IntegerValue(self) -> int:
        return self.__value_IntegerValue

    @value_IntegerValue.setter
    def value_IntegerValue(self, value_IntegerValue: int):
        self.__value_IntegerValue = value_IntegerValue

    @property
    def fumlConfiguration139(self):
        return self.__fumlConfiguration139

    @fumlConfiguration139.setter
    def fumlConfiguration139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_IntegerValue_value_IntegerValue_Value__fumlConfiguration139", None)
        self.__fumlConfiguration139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced140"):
                opp_val = getattr(old_value, "Traced140", None)
                if opp_val == self:
                    setattr(old_value, "Traced140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced140"):
                opp_val = getattr(value, "Traced140", None)
                setattr(value, "Traced140", self)

    @property
    def integerValue_value_IntegerValue_Values(self):
        return self.__integerValue_value_IntegerValue_Values

    @integerValue_value_IntegerValue_Values.setter
    def integerValue_value_IntegerValue_Values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_IntegerValue_value_IntegerValue_Value__integerValue_value_IntegerValue_Values", None)
        self.__integerValue_value_IntegerValue_Values = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State142"):
                    opp_val = getattr(item, "State142", None)
                    
                    if opp_val == self:
                        setattr(item, "State142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State142"):
                    opp_val = getattr(item, "State142", None)
                    
                    setattr(item, "State142", self)
                    

class umlTrace_Values_Reference_referent_Value:

    pass
class Values_umlTrace_State:

    pass
class Kernel_TracedObject:

    pass
class uml_TracedClass:

    pass
class umlTrace_uml_TracedNode(uml_TracedDeploymentTarget, uml_TracedClass):

    pass
class umlTrace_uml_TracedAssociationClass(uml_TracedAssociation, uml_TracedClass):

    pass
class umlTrace_Values_Object_types_Value:

    pass
class umlTrace_Steps_BigStep(ABC):

    pass
class umlTrace_Steps_Steps:

    pass
class Steps_umlTrace_State:

    pass
class umlTrace_Steps_SmallStep(ABC):

    pass
class ExecutionEnvironment_locus_ExecutionEnvironment_Value:

    pass
class ActivityExecution_activationGroup_Value:

    pass
class ActivityEdgeInstance_source_Value:

    pass
class ActivityEdgeInstance_edge_ActivityEdgeInstance_Value:

    pass
class ExtensionalValue_locus_ExtensionalValue_Value:

    pass
class ActivityNodeActivation_group_ActivityNodeActivation_Value:

    pass
class ActivityNodeActivation_incomingEdges_Value:

    pass
class ActivityNodeActivation_outgoingEdges_Value:

    pass
class ActivityNodeActivation_isRunning_Value:

    pass
class ActivityNodeActivation_running_Value:

    pass
class ActivityNodeActivation_node_ActivityNodeActivation_Value:

    pass
class ActivityNodeActivation_heldTokens_Value:

    pass
class InputParameterValues_parameterValues_Value:

    pass
class InputParameterValues_name_Value:

    pass
class CompoundValue_featureValues_Value:

    pass
class CallActionActivation_callExecutions_Value:

    pass
class ObjectToken_value_Value:

    pass
class ActivityEdgeInstance_target_Value:

    pass
class ActivityEdgeInstance_offers_Value:

    pass
class ActivityEdgeInstance_group_ActivityEdgeInstance_Value:

    pass
class PinActivation_count_temp_Value:

    pass
class PinActivation_actionActivation_Value:

    pass
class FeatureValue_position_Value:

    pass
class FeatureValue_feature_Value:

    pass
class FeatureValue_values_FeatureValue_Value:

    pass
class Offer_offeredTokens_Value:

    pass
class Token_holder_Value:

    pass
class ActionActivation_firing_Value:

    pass
class ActionActivation_pinActivations_Value:

    pass
class ParameterValue_parameter_ParameterValue_Value:

    pass
class BooleanValue_value_BooleanValue_Value:

    pass
class Evaluation_locus_Evaluation_Value:

    pass
class Evaluation_specification_Evaluation_Value:

    pass
class PrimitiveValue_type_Value:

    pass
class Executor_locus_Executor_Value:

    pass
class ActivityNodeActivationGroup_edgeInstances_Value:

    pass
class ActivityNodeActivationGroup_activityExecution_Value:

    pass
class ActivityNodeActivationGroup_nodeActivations_Value:

    pass
class Element_semanticVisitor_Value:

    pass
class Execution_context_Value:

    pass
class Execution_parameterValues_Value:

    pass
class Reference_referent_Value:

    pass
class Object_types_Value:

    pass
class ParameterValue_values_ParameterValue_Value:

    pass
class SemanticVisitor_runtimeModelElement_Value:

    pass
class ObjectNodeActivation_offeredTokenCount_Value:

    pass
class Locus_executor_Value:

    pass
class Locus_extensionalValues_Value:

    pass
class Locus_factory_Value:

    pass
class ExecutionFactory_locus_ExecutionFactory_Value:

    pass
class ExecutionFactory_primitiveBehaviorPrototypes_Value:

    pass
class ExecutionFactory_builtInTypes_Value:

    pass
class ForkedToken_baseTokenIsWithdrawn_Value:

    pass
class ForkedToken_baseToken_Value:

    pass
class ForkedToken_remainingOffersCount_Value:

    pass
class IntegerValue_value_IntegerValue_Value:

    pass
class BigStep:

    pass
class SmallStep:

    pass
class TracedObjects:

    pass
class Steps:

    pass
class umlTrace_State:

    pass
class umlTrace_Trace:

    pass