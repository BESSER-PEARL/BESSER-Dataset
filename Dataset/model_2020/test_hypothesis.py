import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TracedExecution,
    umlTrace_IntermediateActivities_TracedActivityExecution,
    TracedSemanticVisitor,
    umlTrace_IntermediateActivities_TracedActivityNodeActivation,
    TracedActivityNodeActivation,
    umlTrace_IntermediateActivities_TracedObjectNodeActivation,
    umlTrace_IntermediateActivities_TracedControlNodeActivation,
    TracedControlNodeActivation,
    umlTrace_IntermediateActivities_TracedInitialNodeActivation,
    umlTrace_IntermediateActivities_TracedMergeNodeActivation,
    umlTrace_IntermediateActivities_TracedForkNodeActivation,
    uml_TracedVertex,
    TracedState,
    umlTrace_uml_TracedFinalState,
    TracedExecutionSpecification,
    umlTrace_uml_TracedBehaviorExecutionSpecification,
    TracedOccurrenceSpecification,
    umlTrace_uml_TracedExecutionOccurrenceSpecification,
    TracedOpaqueBehavior,
    umlTrace_uml_TracedFunctionBehavior,
    uml_TracedStructuredClassifier,
    TracedMultiplicityElement,
    umlTrace_uml_TracedConnectorEnd,
    umlTrace_uml_TracedActionExecutionSpecification,
    TracedObjectNode,
    umlTrace_uml_TracedExpansionNode,
    umlTrace_uml_TracedActivityParameterNode,
    umlTrace_uml_TracedCentralBufferNode,
    TracedCentralBufferNode,
    umlTrace_uml_TracedDataStoreNode,
    TracedDataType,
    umlTrace_uml_TracedEnumeration,
    umlTrace_uml_TracedPrimitiveType,
    TracedMessageEvent,
    umlTrace_uml_TracedCallEvent,
    uml_ActivityContent,
    BasicActions_TracedActionActivation,
    umlTrace_Values_ActionActivation_firing_Value,
    TracedLiteralEvaluation,
    umlTrace_Kernel_TracedLiteralIntegerEvaluation,
    umlTrace_Kernel_TracedLiteralBooleanEvaluation,
    TracedPrimitiveValue,
    umlTrace_Kernel_TracedBooleanValue,
    umlTrace_Kernel_TracedIntegerValue,
    umlTrace_Kernel_TracedEvaluation,
    TracedEvaluation,
    umlTrace_Kernel_TracedLiteralEvaluation,
    umlTrace_Kernel_TracedValue,
    TracedValue,
    umlTrace_Kernel_TracedPrimitiveValue,
    umlTrace_Kernel_TracedStructuredValue,
    TracedStructuredValue,
    umlTrace_Kernel_TracedReference,
    umlTrace_Kernel_TracedCompoundValue,
    TracedCompoundValue,
    umlTrace_Kernel_TracedExtensionalValue,
    TracedExtensionalValue,
    umlTrace_Kernel_TracedObject,
    umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution,
    TracedObject,
    umlTrace_BasicBehaviors_TracedExecution,
    uml_TracedElement,
    umlTrace_Values_SemanticVisitor_runtimeModelElement_Value,
    TracedOpaqueBehaviorExecution,
    umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution,
    umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution,
    umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution,
    TracedCallActionActivation,
    umlTrace_BasicActions_TracedCallBehaviorActionActivation,
    TracedPinActivation,
    umlTrace_BasicActions_TracedOutputPinActivation,
    umlTrace_BasicActions_TracedInputPinActivation,
    TracedInvocationActionActivation,
    umlTrace_BasicActions_TracedCallActionActivation,
    TracedActionActivation,
    umlTrace_BasicActions_TracedOpaqueActionActivation,
    umlTrace_BasicActions_TracedInvocationActionActivation,
    umlTrace_BasicActions_TracedActionActivation,
    umlTrace_Loci_TracedSemanticVisitor,
    umlTrace_IntermediateActivities_TracedDecisionNodeActivation,
    umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation,
    umlTrace_IntermediateActivities_TracedJoinNodeActivation,
    TracedObjectNodeActivation,
    umlTrace_BasicActions_TracedPinActivation,
    umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation,
    umlTrace_IntermediateActions_TracedCreateObjectActionActivation,
    umlTrace_IntermediateActions_TracedValueSpecificationActionActivation,
    TracedWriteStructuralFeatureActionActivation,
    umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation,
    TracedStructuralFeatureActionActivation,
    umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation,
    umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation,
    umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation,
    umlTrace_ecore_TracedEModelElement,
    TracedMessageEnd,
    umlTrace_uml_TracedGate,
    uml_TracedAction,
    TracedStructuredActivityNode,
    umlTrace_uml_TracedConditionalNode,
    TracedEModelElement,
    umlTrace_uml_TracedElement,
    TracedElement,
    umlTrace_uml_TracedTemplateParameterSubstitution,
    umlTrace_uml_TracedQualifierValue,
    umlTrace_uml_TracedComment,
    umlTrace_uml_TracedClause,
    umlTrace_uml_TracedNamedElement,
    TracedNamedElement,
    umlTrace_uml_TracedGeneralOrdering,
    umlTrace_uml_TracedParameterSet,
    umlTrace_uml_TracedInteractionFragment,
    uml_TracedMessageEnd,
    TracedMessageOccurrenceSpecification,
    umlTrace_uml_TracedDestructionOccurrenceSpecification,
    umlTrace_uml_TracedVertex,
    TracedVertex,
    umlTrace_uml_TracedConnectionPointReference,
    umlTrace_uml_TracedPseudostate,
    umlTrace_uml_TracedParameterableElement,
    uml_TracedParameterableElement,
    TracedPackageableElement,
    umlTrace_uml_TracedConstraint,
    TracedConstraint,
    umlTrace_uml_TracedInteractionConstraint,
    umlTrace_uml_TracedIntervalConstraint,
    TracedIntervalConstraint,
    umlTrace_uml_TracedDurationConstraint,
    uml_TracedControlFlow,
    uml_TracedTimeObservation,
    uml_TracedGate,
    uml_TracedActivityFinalNode,
    uml_TracedClassifierTemplateParameter,
    TracedInteractionFragment,
    umlTrace_uml_TracedOccurrenceSpecification,
    umlTrace_uml_TracedCombinedFragment,
    uml_TracedGeneralOrdering,
    uml_TracedElementImport,
    uml_TracedMergeNode,
    uml_TracedClearAssociationAction,
    uml_TracedLinkEndCreationData,
    uml_TracedPseudostate,
    uml_TracedComponent,
    uml_TracedReadIsClassifiedObjectAction,
    uml_TracedAbstraction,
    uml_TracedTimeExpression,
    uml_TracedValueSpecificationAction,
    uml_TracedFunctionBehavior,
    IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution,
    IntermediateActivities_TracedMergeNodeActivation,
    uml_TracedTemplateParameter,
    uml_TracedManifestation,
    uml_TracedActor,
    uml_TracedRemoveVariableValueAction,
    uml_TracedProfile,
    uml_TracedTestIdentityAction,
    uml_TracedCollaboration,
    uml_TracedSendSignalAction,
    uml_TracedInterfaceRealization,
    uml_TracedUnmarshallAction,
    uml_TracedExpression,
    uml_TracedAssociation,
    uml_TracedClearStructuralFeatureAction,
    uml_TracedAddVariableValueAction,
    uml_TracedLiteralReal,
    IntermediateActions_TracedCreateObjectActionActivation,
    uml_TracedSlot,
    uml_TracedLiteralNull,
    IntermediateActions_TracedValueSpecificationActionActivation,
    uml_TracedStartObjectBehaviorAction,
    uml_TracedLiteralBoolean,
    uml_TracedReadLinkAction,
    uml_TracedInclude,
    uml_TracedRegion,
    uml_TracedState,
    uml_TracedPrimitiveType,
    uml_TracedStringExpression,
    uml_TracedLinkEndDestructionData,
    umlTrace_uml_TracedAnyReceiveEvent,
    uml_TracedReadExtentAction,
    BasicActions_TracedOutputPinActivation,
    uml_TracedBehavioralFeature,
    uml_TracedTemplateSignature,
    umlTrace_uml_TracedTemplateParameter,
    TracedTemplateParameter,
    umlTrace_uml_TracedConnectableElementTemplateParameter,
    umlTrace_uml_TracedClassifierTemplateParameter,
    TracedPackage,
    umlTrace_uml_TracedProfile,
    umlTrace_uml_TracedModel,
    umlTrace_uml_TracedImage,
    TracedTransition,
    umlTrace_uml_TracedProtocolTransition,
    TracedWriteVariableAction,
    umlTrace_uml_TracedRemoveVariableValueAction,
    umlTrace_uml_TracedAddVariableValueAction,
    TracedInteractionUse,
    umlTrace_uml_TracedPartDecomposition,
    TracedObservation,
    umlTrace_uml_TracedTimeObservation,
    umlTrace_uml_TracedDurationObservation,
    umlTrace_uml_TracedOperationTemplateParameter,
    TracedInterval,
    umlTrace_uml_TracedDurationInterval,
    umlTrace_uml_TracedTimeInterval,
    umlTrace_uml_TracedSignalEvent,
    TracedBehavioralFeature,
    umlTrace_uml_TracedReception,
    umlTrace_uml_TracedExecutionSpecification,
    TracedDependency,
    umlTrace_uml_TracedUsage,
    umlTrace_uml_TracedAbstraction,
    TracedAbstraction,
    umlTrace_uml_TracedManifestation,
    umlTrace_uml_TracedRealization,
    TracedRealization,
    umlTrace_uml_TracedComponentRealization,
    umlTrace_uml_TracedInterfaceRealization,
    umlTrace_uml_TracedSubstitution,
    TracedInstanceSpecification,
    umlTrace_uml_TracedEnumerationLiteral,
    TracedAcceptEventAction,
    umlTrace_uml_TracedAcceptCallAction,
    umlTrace_uml_TracedLinkEndData,
    TracedLinkEndData,
    umlTrace_uml_TracedLinkEndCreationData,
    umlTrace_uml_TracedLinkEndDestructionData,
    umlTrace_uml_TracedTemplateSignature,
    umlTrace_uml_TracedStateInvariant,
    umlTrace_uml_TracedTrigger,
    umlTrace_uml_TracedSlot,
    TracedClass,
    umlTrace_uml_TracedStereotype,
    umlTrace_uml_TracedComponent,
    umlTrace_uml_TracedBehavior,
    uml_TracedInteractionFragment,
    uml_TracedBehavior,
    umlTrace_uml_TracedInteraction,
    TracedActivityEdge,
    umlTrace_uml_TracedControlFlow,
    umlTrace_uml_TracedObjectFlow,
    TracedStateMachine,
    umlTrace_uml_TracedProtocolStateMachine,
    umlTrace_uml_TracedDeployment,
    umlTrace_uml_TracedMessage,
    TracedBehavior,
    umlTrace_uml_TracedOpaqueBehavior,
    umlTrace_uml_TracedActivity,
    umlTrace_uml_TracedStateMachine,
    TracedActivityGroup,
    umlTrace_uml_TracedInterruptibleActivityRegion,
    umlTrace_uml_TracedActivityPartition,
    uml_TracedRelationship,
    TracedAssociation,
    umlTrace_uml_TracedCommunicationPath,
    umlTrace_uml_TracedExtension,
    TracedStructuralFeatureAction,
    umlTrace_uml_TracedReadStructuralFeatureAction,
    umlTrace_uml_TracedClearStructuralFeatureAction,
    umlTrace_uml_TracedWriteStructuralFeatureAction,
    TracedWriteStructuralFeatureAction,
    umlTrace_uml_TracedAddStructuralFeatureValueAction,
    umlTrace_uml_TracedRemoveStructuralFeatureValueAction,
    TracedBehavioredClassifier,
    umlTrace_uml_TracedActor,
    umlTrace_uml_TracedUseCase,
    umlTrace_uml_TracedSequenceNode,
    umlTrace_uml_TracedExceptionHandler,
    umlTrace_uml_TracedDeployedArtifact,
    uml_TracedDeployedArtifact,
    uml_TracedClassifier,
    umlTrace_uml_TracedAssociation,
    umlTrace_uml_TracedArtifact,
    TracedArtifact,
    umlTrace_uml_TracedDeploymentSpecification,
    uml_TracedActivityNode,
    uml_TracedObjectNode,
    TracedPin,
    umlTrace_uml_TracedOutputPin,
    umlTrace_uml_TracedInputPin,
    TracedInputPin,
    umlTrace_uml_TracedActionInputPin,
    umlTrace_uml_TracedValuePin,
    umlTrace_uml_TracedCollaborationUse,
    umlTrace_uml_TracedDeploymentTarget,
    umlTrace_uml_TracedMultiplicityElement,
    umlTrace_uml_TracedTypedElement,
    uml_TracedMultiplicityElement,
    umlTrace_uml_TracedPin,
    uml_TracedTypedElement,
    umlTrace_uml_TracedConnectableElement,
    umlTrace_uml_TracedObjectNode,
    uml_TracedFeature,
    umlTrace_uml_TracedStructuralFeature,
    TracedValueSpecification,
    umlTrace_uml_TracedOpaqueExpression,
    umlTrace_uml_TracedTimeExpression,
    umlTrace_uml_TracedInterval,
    umlTrace_uml_TracedExpression,
    umlTrace_uml_TracedInstanceValue,
    umlTrace_uml_TracedDuration,
    umlTrace_uml_TracedLiteralSpecification,
    TracedLiteralSpecification,
    umlTrace_uml_TracedLiteralUnlimitedNatural,
    umlTrace_uml_TracedLiteralNull,
    umlTrace_uml_TracedLiteralReal,
    umlTrace_uml_TracedLiteralBoolean,
    umlTrace_uml_TracedLiteralInteger,
    umlTrace_uml_TracedLiteralString,
    TracedVariableAction,
    umlTrace_uml_TracedReadVariableAction,
    umlTrace_uml_TracedWriteVariableAction,
    umlTrace_uml_TracedClearVariableAction,
    umlTrace_uml_TracedTimeConstraint,
    umlTrace_uml_TracedContinuation,
    TracedCombinedFragment,
    umlTrace_uml_TracedConsiderIgnoreFragment,
    TracedNode,
    umlTrace_uml_TracedDevice,
    umlTrace_uml_TracedExecutionEnvironment,
    umlTrace_uml_TracedType,
    uml_TracedType,
    TracedClassifier,
    umlTrace_uml_TracedDataType,
    umlTrace_uml_TracedInformationItem,
    umlTrace_uml_TracedInterface,
    umlTrace_uml_TracedBehavioredClassifier,
    umlTrace_uml_TracedStructuredClassifier,
    TracedStructuredClassifier,
    umlTrace_uml_TracedEncapsulatedClassifier,
    uml_TracedBehavioredClassifier,
    umlTrace_uml_TracedCollaboration,
    uml_TracedEncapsulatedClassifier,
    umlTrace_uml_TracedClass,
    TracedCallAction,
    umlTrace_uml_TracedStartObjectBehaviorAction,
    umlTrace_uml_TracedCallOperationAction,
    umlTrace_uml_TracedCallBehaviorAction,
    umlTrace_uml_TracedRelationship,
    TracedRelationship,
    umlTrace_uml_TracedDirectedRelationship,
    TracedDirectedRelationship,
    umlTrace_uml_TracedGeneralization,
    umlTrace_uml_TracedElementImport,
    umlTrace_uml_TracedProfileApplication,
    umlTrace_uml_TracedPackageMerge,
    umlTrace_uml_TracedTemplateBinding,
    umlTrace_uml_TracedPackageImport,
    umlTrace_uml_TracedProtocolConformance,
    TracedInvocationAction,
    umlTrace_uml_TracedCallAction,
    umlTrace_uml_TracedBroadcastSignalAction,
    umlTrace_uml_TracedSendSignalAction,
    umlTrace_uml_TracedSendObjectAction,
    TracedRedefinableElement,
    umlTrace_uml_TracedExtensionPoint,
    umlTrace_uml_TracedActivityEdge,
    umlTrace_uml_TracedFeature,
    TracedFeature,
    umlTrace_uml_TracedConnector,
    umlTrace_uml_TracedTemplateableElement,
    uml_TracedTemplateableElement,
    umlTrace_uml_TracedOperation,
    umlTrace_uml_TracedStringExpression,
    uml_TracedPackageableElement,
    umlTrace_uml_TracedValueSpecification,
    umlTrace_uml_TracedMessageEnd,
    uml_TracedDeploymentTarget,
    umlTrace_uml_TracedInstanceSpecification,
    uml_TracedConnectableElement,
    umlTrace_uml_TracedParameter,
    umlTrace_uml_TracedVariable,
    uml_TracedStructuralFeature,
    umlTrace_uml_TracedProperty,
    TracedProperty,
    umlTrace_uml_TracedExtensionEnd,
    umlTrace_uml_TracedPort,
    uml_TracedDirectedRelationship,
    umlTrace_uml_TracedInformationFlow,
    umlTrace_uml_TracedDependency,
    umlTrace_uml_TracedEvent,
    TracedEvent,
    umlTrace_uml_TracedMessageEvent,
    umlTrace_uml_TracedTimeEvent,
    umlTrace_uml_TracedChangeEvent,
    umlTrace_uml_TracedGeneralizationSet,
    umlTrace_uml_TracedSignal,
    umlTrace_uml_TracedLoopNode,
    umlTrace_uml_TracedInteractionUse,
    umlTrace_uml_TracedObservation,
    umlTrace_uml_TracedLifeline,
    umlTrace_uml_TracedExpansionRegion,
    TracedFinalNode,
    umlTrace_uml_TracedActivityFinalNode,
    umlTrace_uml_TracedFlowFinalNode,
    TracedControlNode,
    umlTrace_uml_TracedJoinNode,
    umlTrace_uml_TracedMergeNode,
    umlTrace_uml_TracedDecisionNode,
    umlTrace_uml_TracedFinalNode,
    umlTrace_uml_TracedForkNode,
    umlTrace_uml_TracedInitialNode,
    TracedAction,
    umlTrace_uml_TracedReplyAction,
    umlTrace_uml_TracedReadExtentAction,
    umlTrace_uml_TracedAcceptEventAction,
    umlTrace_uml_TracedInvocationAction,
    umlTrace_uml_TracedRaiseExceptionAction,
    umlTrace_uml_TracedValueSpecificationAction,
    umlTrace_uml_TracedClearAssociationAction,
    umlTrace_uml_TracedOpaqueAction,
    umlTrace_uml_TracedCreateObjectAction,
    umlTrace_uml_TracedReclassifyObjectAction,
    umlTrace_uml_TracedStartClassifierBehaviorAction,
    umlTrace_uml_TracedVariableAction,
    umlTrace_uml_TracedReadIsClassifiedObjectAction,
    umlTrace_uml_TracedTestIdentityAction,
    umlTrace_uml_TracedUnmarshallAction,
    umlTrace_uml_TracedReadSelfAction,
    umlTrace_uml_TracedReduceAction,
    umlTrace_uml_TracedStructuralFeatureAction,
    umlTrace_uml_TracedDestroyObjectAction,
    umlTrace_uml_TracedReadLinkObjectEndQualifierAction,
    umlTrace_uml_TracedReadLinkObjectEndAction,
    umlTrace_uml_TracedLinkAction,
    TracedLinkAction,
    umlTrace_uml_TracedReadLinkAction,
    umlTrace_uml_TracedWriteLinkAction,
    TracedWriteLinkAction,
    umlTrace_uml_TracedDestroyLinkAction,
    umlTrace_uml_TracedCreateLinkAction,
    TracedCreateLinkAction,
    umlTrace_uml_TracedCreateLinkObjectAction,
    uml_TracedNamedElement,
    umlTrace_uml_TracedExtend,
    umlTrace_uml_TracedInclude,
    umlTrace_uml_TracedPackageableElement,
    umlTrace_uml_TracedNamespace,
    umlTrace_uml_TracedRedefinableElement,
    ActivityContent,
    umlTrace_uml_TracedActivityGroup,
    uml_TracedRedefinableElement,
    umlTrace_uml_TracedRedefinableTemplateSignature,
    umlTrace_uml_TracedActivityNode,
    TracedActivityNode,
    umlTrace_uml_TracedControlNode,
    umlTrace_uml_TracedExecutableNode,
    TracedExecutableNode,
    umlTrace_uml_TracedAction,
    uml_TracedActivityGroup,
    uml_TracedNamespace,
    umlTrace_uml_TracedRegion,
    umlTrace_uml_TracedPackage,
    umlTrace_uml_TracedState,
    umlTrace_uml_TracedStructuredActivityNode,
    umlTrace_uml_TracedClassifier,
    umlTrace_uml_TracedBehavioralFeature,
    umlTrace_uml_TracedInteractionOperand,
    umlTrace_uml_TracedTransition,
    uml_TracedRaiseExceptionAction,
    uml_TracedCommunicationPath,
    Kernel_TracedLiteralBooleanEvaluation,
    uml_TracedEnumeration,
    uml_TracedReadLinkObjectEndAction,
    uml_TracedCallBehaviorAction,
    uml_TracedVariable,
    uml_TracedConnectorEnd,
    uml_TracedArtifact,
    uml_TracedCallOperationAction,
    uml_TracedLiteralUnlimitedNatural,
    uml_TracedDurationObservation,
    uml_TracedBehaviorExecutionSpecification,
    uml_TracedActivityParameterNode,
    uml_TracedExpansionNode,
    uml_TracedProfileApplication,
    uml_TracedAddStructuralFeatureValueAction,
    uml_TracedQualifierValue,
    uml_TracedImage,
    uml_TracedExtensionEnd,
    uml_TracedProperty,
    uml_TracedDevice,
    uml_TracedOpaqueAction,
    uml_TracedFinalState,
    uml_TracedReduceAction,
    uml_TracedDuration,
    uml_TracedTemplateParameterSubstitution,
    uml_TracedOutputPin,
    uml_TracedActionExecutionSpecification,
    uml_TracedInformationItem,
    uml_TracedOperationTemplateParameter,
    uml_TracedConnectableElementTemplateParameter,
    uml_TracedLinkEndData,
    uml_TracedDurationInterval,
    uml_TracedTransition,
    uml_TracedTrigger,
    uml_TracedReplyAction,
    uml_TracedClause,
    uml_TracedPackageMerge,
    uml_TracedDecisionNode,
    IntermediateActions_TracedReadStructuralFeatureActionActivation,
    uml_TracedReadSelfAction,
    uml_TracedOperation,
    uml_TracedObjectFlow,
    uml_TracedParameterSet,
    uml_TracedOccurrenceSpecification,
    umlTrace_uml_TracedMessageOccurrenceSpecification,
    uml_TracedAcceptEventAction,
    uml_TracedComponentRealization,
    uml_TracedDataType,
    uml_TracedComment,
    uml_TracedLoopNode,
    uml_TracedCallEvent,
    uml_TracedPackage,
    uml_TracedProtocolConformance,
    uml_TracedOpaqueBehavior,
    uml_TracedInterface,
    IntermediateActivities_TracedDecisionNodeActivation,
    uml_TracedInteractionConstraint,
    uml_TracedTimeInterval,
    uml_TracedExecutionOccurrenceSpecification,
    uml_TracedSignal,
    uml_TracedExtensionPoint,
    uml_TracedCreateLinkAction,
    Kernel_TracedLiteralIntegerEvaluation,
    uml_TracedCentralBufferNode,
    uml_TracedModel,
    uml_TracedRedefinableTemplateSignature,
    uml_TracedJoinNode,
    BasicActions_TracedOpaqueActionActivation,
    uml_TracedReadLinkObjectEndQualifierAction,
    uml_TracedRealization,
    uml_TracedConnectionPointReference,
    uml_TracedConditionalNode,
    Kernel_TracedBooleanValue,
    uml_TracedSignalEvent,
    uml_TracedLiteralInteger,
    uml_TracedDestroyLinkAction,
    IntermediateActivities_TracedActivityFinalNodeActivation,
    uml_TracedReadVariableAction,
    uml_TracedActionInputPin,
    uml_TracedUsage,
    uml_TracedDeploymentSpecification,
    uml_TracedTemplateBinding,
    uml_TracedMessageOccurrenceSpecification,
    uml_TracedReception,
    uml_TracedProtocolStateMachine,
    uml_TracedDataStoreNode,
    uml_TracedReadStructuralFeatureAction,
    uml_TracedAnyReceiveEvent,
    Kernel_TracedIntegerValue,
    uml_TracedInterval,
    uml_TracedRemoveStructuralFeatureValueAction,
    uml_TracedGeneralization,
    uml_TracedInteractionOperand,
    uml_TracedProtocolTransition,
    uml_TracedInterruptibleActivityRegion,
    uml_TracedPartDecomposition,
    uml_TracedTimeEvent,
    uml_TracedDeployment,
    Loci_TracedSemanticVisitor,
    Kernel_TracedObject,
    IntermediateActivities_TracedJoinNodeActivation,
    uml_TracedUseCase,
    uml_TracedReclassifyObjectAction,
    uml_TracedInstanceValue,
    IntermediateActions_TracedAddStructuralFeatureValueActionActivation,
    Kernel_TracedReference,
    uml_TracedForkNode,
    uml_TracedActivity,
    uml_TracedMessage,
    uml_TracedStateMachine,
    uml_TracedActivityPartition,
    IntermediateActivities_TracedActivityParameterNodeActivation,
    BasicActions_TracedCallBehaviorActionActivation,
    uml_TracedDestroyObjectAction,
    uml_TracedAssociationClass,
    uml_TracedInformationFlow,
    uml_TracedSubstitution,
    uml_TracedEnumerationLiteral,
    uml_TracedStereotype,
    uml_TracedAcceptCallAction,
    uml_TracedInstanceSpecification,
    IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution,
    uml_TracedStateInvariant,
    BasicActions_TracedInputPinActivation,
    uml_TracedLiteralString,
    uml_TracedOpaqueExpression,
    uml_TracedParameter,
    IntermediateActivities_TracedActivityNodeActivation,
    uml_TracedInteraction,
    uml_TracedBroadcastSignalAction,
    uml_TracedConstraint,
    uml_TracedClearVariableAction,
    uml_TracedInputPin,
    uml_TracedTimeConstraint,
    uml_TracedContinuation,
    uml_TracedConsiderIgnoreFragment,
    uml_TracedIntervalConstraint,
    uml_TracedExecutionEnvironment,
    uml_TracedStructuredActivityNode,
    uml_TracedExtension,
    IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution,
    uml_TracedExtend,
    uml_TracedStartClassifierBehaviorAction,
    uml_TracedSequenceNode,
    uml_TracedExceptionHandler,
    uml_TracedNode,
    uml_TracedValuePin,
    IntermediateActivities_TracedActivityExecution,
    uml_TracedCollaborationUse,
    IntermediateActivities_TracedInitialNodeActivation,
    uml_TracedPort,
    uml_TracedDependency,
    uml_TracedChangeEvent,
    uml_TracedGeneralizationSet,
    uml_TracedInteractionUse,
    uml_TracedClass,
    umlTrace_uml_TracedNode,
    umlTrace_uml_TracedAssociationClass,
    uml_TracedPackageImport,
    uml_TracedSendObjectAction,
    uml_TracedConnector,
    uml_TracedDestructionOccurrenceSpecification,
    uml_TracedDurationConstraint,
    IntermediateActivities_TracedForkNodeActivation,
    uml_TracedLifeline,
    uml_TracedCreateObjectAction,
    uml_TracedExpansionRegion,
    uml_TracedFlowFinalNode,
    uml_TracedInitialNode,
    uml_TracedCreateLinkObjectAction,
    uml_TracedCombinedFragment,
    umlTrace_Traced_TracedObjects,
    Traced_TracedObjects,
    State,
    umlTrace_Trace,
    Values_SemanticVisitor_runtimeModelElement_Value,
    Values_ActionActivation_firing_Value,
    umlTrace_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tracedexecution_is_not_abstract():
    assert not inspect.isabstract(TracedExecution)


def test_tracedexecution_constructor_exists():
    assert callable(TracedExecution.__init__)


def test_tracedexecution_constructor_args():
    sig = inspect.signature(TracedExecution.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedactivityexecution_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedActivityExecution)


def test_umltrace_intermediateactivities_tracedactivityexecution_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedActivityExecution.__init__)


def test_umltrace_intermediateactivities_tracedactivityexecution_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedActivityExecution.__init__)
    params = list(sig.parameters.keys())



def test_tracedsemanticvisitor_is_not_abstract():
    assert not inspect.isabstract(TracedSemanticVisitor)


def test_tracedsemanticvisitor_constructor_exists():
    assert callable(TracedSemanticVisitor.__init__)


def test_tracedsemanticvisitor_constructor_args():
    sig = inspect.signature(TracedSemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedactivitynodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedActivityNodeActivation)


def test_umltrace_intermediateactivities_tracedactivitynodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedActivityNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedactivitynodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedActivityNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedactivitynodeactivation_is_not_abstract():
    assert not inspect.isabstract(TracedActivityNodeActivation)


def test_tracedactivitynodeactivation_constructor_exists():
    assert callable(TracedActivityNodeActivation.__init__)


def test_tracedactivitynodeactivation_constructor_args():
    sig = inspect.signature(TracedActivityNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedobjectnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedObjectNodeActivation)


def test_umltrace_intermediateactivities_tracedobjectnodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedObjectNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedobjectnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedObjectNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedcontrolnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedControlNodeActivation)


def test_umltrace_intermediateactivities_tracedcontrolnodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedControlNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedcontrolnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedControlNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedcontrolnodeactivation_is_not_abstract():
    assert not inspect.isabstract(TracedControlNodeActivation)


def test_tracedcontrolnodeactivation_constructor_exists():
    assert callable(TracedControlNodeActivation.__init__)


def test_tracedcontrolnodeactivation_constructor_args():
    sig = inspect.signature(TracedControlNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedinitialnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedInitialNodeActivation)


def test_umltrace_intermediateactivities_tracedinitialnodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedInitialNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedinitialnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedInitialNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedmergenodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedMergeNodeActivation)


def test_umltrace_intermediateactivities_tracedmergenodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedMergeNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedmergenodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedMergeNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedforknodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedForkNodeActivation)


def test_umltrace_intermediateactivities_tracedforknodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedForkNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedforknodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedForkNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedvertex_is_not_abstract():
    assert not inspect.isabstract(uml_TracedVertex)


def test_uml_tracedvertex_constructor_exists():
    assert callable(uml_TracedVertex.__init__)


def test_uml_tracedvertex_constructor_args():
    sig = inspect.signature(uml_TracedVertex.__init__)
    params = list(sig.parameters.keys())



def test_tracedstate_is_not_abstract():
    assert not inspect.isabstract(TracedState)


def test_tracedstate_constructor_exists():
    assert callable(TracedState.__init__)


def test_tracedstate_constructor_args():
    sig = inspect.signature(TracedState.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedfinalstate_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedFinalState)


def test_umltrace_uml_tracedfinalstate_constructor_exists():
    assert callable(umlTrace_uml_TracedFinalState.__init__)


def test_umltrace_uml_tracedfinalstate_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedFinalState.__init__)
    params = list(sig.parameters.keys())



def test_tracedexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(TracedExecutionSpecification)


def test_tracedexecutionspecification_constructor_exists():
    assert callable(TracedExecutionSpecification.__init__)


def test_tracedexecutionspecification_constructor_args():
    sig = inspect.signature(TracedExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedbehaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedBehaviorExecutionSpecification)


def test_umltrace_uml_tracedbehaviorexecutionspecification_constructor_exists():
    assert callable(umlTrace_uml_TracedBehaviorExecutionSpecification.__init__)


def test_umltrace_uml_tracedbehaviorexecutionspecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedBehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_tracedoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(TracedOccurrenceSpecification)


def test_tracedoccurrencespecification_constructor_exists():
    assert callable(TracedOccurrenceSpecification.__init__)


def test_tracedoccurrencespecification_constructor_args():
    sig = inspect.signature(TracedOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedexecutionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExecutionOccurrenceSpecification)


def test_umltrace_uml_tracedexecutionoccurrencespecification_constructor_exists():
    assert callable(umlTrace_uml_TracedExecutionOccurrenceSpecification.__init__)


def test_umltrace_uml_tracedexecutionoccurrencespecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_tracedopaquebehavior_is_not_abstract():
    assert not inspect.isabstract(TracedOpaqueBehavior)


def test_tracedopaquebehavior_constructor_exists():
    assert callable(TracedOpaqueBehavior.__init__)


def test_tracedopaquebehavior_constructor_args():
    sig = inspect.signature(TracedOpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedfunctionbehavior_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedFunctionBehavior)


def test_umltrace_uml_tracedfunctionbehavior_constructor_exists():
    assert callable(umlTrace_uml_TracedFunctionBehavior.__init__)


def test_umltrace_uml_tracedfunctionbehavior_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedFunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstructuredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStructuredClassifier)


def test_uml_tracedstructuredclassifier_constructor_exists():
    assert callable(uml_TracedStructuredClassifier.__init__)


def test_uml_tracedstructuredclassifier_constructor_args():
    sig = inspect.signature(uml_TracedStructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_tracedmultiplicityelement_is_not_abstract():
    assert not inspect.isabstract(TracedMultiplicityElement)


def test_tracedmultiplicityelement_constructor_exists():
    assert callable(TracedMultiplicityElement.__init__)


def test_tracedmultiplicityelement_constructor_args():
    sig = inspect.signature(TracedMultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedconnectorend_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedConnectorEnd)


def test_umltrace_uml_tracedconnectorend_constructor_exists():
    assert callable(umlTrace_uml_TracedConnectorEnd.__init__)


def test_umltrace_uml_tracedconnectorend_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedactionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActionExecutionSpecification)


def test_umltrace_uml_tracedactionexecutionspecification_constructor_exists():
    assert callable(umlTrace_uml_TracedActionExecutionSpecification.__init__)


def test_umltrace_uml_tracedactionexecutionspecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActionExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_tracedobjectnode_is_not_abstract():
    assert not inspect.isabstract(TracedObjectNode)


def test_tracedobjectnode_constructor_exists():
    assert callable(TracedObjectNode.__init__)


def test_tracedobjectnode_constructor_args():
    sig = inspect.signature(TracedObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedexpansionnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExpansionNode)


def test_umltrace_uml_tracedexpansionnode_constructor_exists():
    assert callable(umlTrace_uml_TracedExpansionNode.__init__)


def test_umltrace_uml_tracedexpansionnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedactivityparameternode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActivityParameterNode)


def test_umltrace_uml_tracedactivityparameternode_constructor_exists():
    assert callable(umlTrace_uml_TracedActivityParameterNode.__init__)


def test_umltrace_uml_tracedactivityparameternode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcentralbuffernode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCentralBufferNode)


def test_umltrace_uml_tracedcentralbuffernode_constructor_exists():
    assert callable(umlTrace_uml_TracedCentralBufferNode.__init__)


def test_umltrace_uml_tracedcentralbuffernode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedcentralbuffernode_is_not_abstract():
    assert not inspect.isabstract(TracedCentralBufferNode)


def test_tracedcentralbuffernode_constructor_exists():
    assert callable(TracedCentralBufferNode.__init__)


def test_tracedcentralbuffernode_constructor_args():
    sig = inspect.signature(TracedCentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddatastorenode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDataStoreNode)


def test_umltrace_uml_traceddatastorenode_constructor_exists():
    assert callable(umlTrace_uml_TracedDataStoreNode.__init__)


def test_umltrace_uml_traceddatastorenode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_traceddatatype_is_not_abstract():
    assert not inspect.isabstract(TracedDataType)


def test_traceddatatype_constructor_exists():
    assert callable(TracedDataType.__init__)


def test_traceddatatype_constructor_args():
    sig = inspect.signature(TracedDataType.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedenumeration_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedEnumeration)


def test_umltrace_uml_tracedenumeration_constructor_exists():
    assert callable(umlTrace_uml_TracedEnumeration.__init__)


def test_umltrace_uml_tracedenumeration_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedprimitivetype_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedPrimitiveType)


def test_umltrace_uml_tracedprimitivetype_constructor_exists():
    assert callable(umlTrace_uml_TracedPrimitiveType.__init__)


def test_umltrace_uml_tracedprimitivetype_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_tracedmessageevent_is_not_abstract():
    assert not inspect.isabstract(TracedMessageEvent)


def test_tracedmessageevent_constructor_exists():
    assert callable(TracedMessageEvent.__init__)


def test_tracedmessageevent_constructor_args():
    sig = inspect.signature(TracedMessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcallevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCallEvent)


def test_umltrace_uml_tracedcallevent_constructor_exists():
    assert callable(umlTrace_uml_TracedCallEvent.__init__)


def test_umltrace_uml_tracedcallevent_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCallEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_activitycontent_is_not_abstract():
    assert not inspect.isabstract(uml_ActivityContent)


def test_uml_activitycontent_constructor_exists():
    assert callable(uml_ActivityContent.__init__)


def test_uml_activitycontent_constructor_args():
    sig = inspect.signature(uml_ActivityContent.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_tracedactionactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions_TracedActionActivation)


def test_basicactions_tracedactionactivation_constructor_exists():
    assert callable(BasicActions_TracedActionActivation.__init__)


def test_basicactions_tracedactionactivation_constructor_args():
    sig = inspect.signature(BasicActions_TracedActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_actionactivation_firing_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActionActivation_firing_Value)


def test_umltrace_values_actionactivation_firing_value_constructor_exists():
    assert callable(umlTrace_Values_ActionActivation_firing_Value.__init__)


def test_umltrace_values_actionactivation_firing_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActionActivation_firing_Value.__init__)
    params = list(sig.parameters.keys())
    assert "firing" in params, "Missing parameter 'firing'"

def test_umltrace_values_actionactivation_firing_value_has_firing():
    assert hasattr(umlTrace_Values_ActionActivation_firing_Value, "firing")
    descriptor = None
    for klass in umlTrace_Values_ActionActivation_firing_Value.__mro__:
        if "firing" in klass.__dict__:
            descriptor = klass.__dict__["firing"]
            break
    assert isinstance(descriptor, property)



def test_tracedliteralevaluation_is_not_abstract():
    assert not inspect.isabstract(TracedLiteralEvaluation)


def test_tracedliteralevaluation_constructor_exists():
    assert callable(TracedLiteralEvaluation.__init__)


def test_tracedliteralevaluation_constructor_args():
    sig = inspect.signature(TracedLiteralEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedliteralintegerevaluation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedLiteralIntegerEvaluation)


def test_umltrace_kernel_tracedliteralintegerevaluation_constructor_exists():
    assert callable(umlTrace_Kernel_TracedLiteralIntegerEvaluation.__init__)


def test_umltrace_kernel_tracedliteralintegerevaluation_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedLiteralIntegerEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedliteralbooleanevaluation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedLiteralBooleanEvaluation)


def test_umltrace_kernel_tracedliteralbooleanevaluation_constructor_exists():
    assert callable(umlTrace_Kernel_TracedLiteralBooleanEvaluation.__init__)


def test_umltrace_kernel_tracedliteralbooleanevaluation_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedLiteralBooleanEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_tracedprimitivevalue_is_not_abstract():
    assert not inspect.isabstract(TracedPrimitiveValue)


def test_tracedprimitivevalue_constructor_exists():
    assert callable(TracedPrimitiveValue.__init__)


def test_tracedprimitivevalue_constructor_args():
    sig = inspect.signature(TracedPrimitiveValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedbooleanvalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedBooleanValue)


def test_umltrace_kernel_tracedbooleanvalue_constructor_exists():
    assert callable(umlTrace_Kernel_TracedBooleanValue.__init__)


def test_umltrace_kernel_tracedbooleanvalue_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedBooleanValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedintegervalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedIntegerValue)


def test_umltrace_kernel_tracedintegervalue_constructor_exists():
    assert callable(umlTrace_Kernel_TracedIntegerValue.__init__)


def test_umltrace_kernel_tracedintegervalue_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedIntegerValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedevaluation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedEvaluation)


def test_umltrace_kernel_tracedevaluation_constructor_exists():
    assert callable(umlTrace_Kernel_TracedEvaluation.__init__)


def test_umltrace_kernel_tracedevaluation_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_tracedevaluation_is_not_abstract():
    assert not inspect.isabstract(TracedEvaluation)


def test_tracedevaluation_constructor_exists():
    assert callable(TracedEvaluation.__init__)


def test_tracedevaluation_constructor_args():
    sig = inspect.signature(TracedEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedliteralevaluation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedLiteralEvaluation)


def test_umltrace_kernel_tracedliteralevaluation_constructor_exists():
    assert callable(umlTrace_Kernel_TracedLiteralEvaluation.__init__)


def test_umltrace_kernel_tracedliteralevaluation_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedLiteralEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedvalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedValue)


def test_umltrace_kernel_tracedvalue_constructor_exists():
    assert callable(umlTrace_Kernel_TracedValue.__init__)


def test_umltrace_kernel_tracedvalue_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedValue.__init__)
    params = list(sig.parameters.keys())



def test_tracedvalue_is_not_abstract():
    assert not inspect.isabstract(TracedValue)


def test_tracedvalue_constructor_exists():
    assert callable(TracedValue.__init__)


def test_tracedvalue_constructor_args():
    sig = inspect.signature(TracedValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedprimitivevalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedPrimitiveValue)


def test_umltrace_kernel_tracedprimitivevalue_constructor_exists():
    assert callable(umlTrace_Kernel_TracedPrimitiveValue.__init__)


def test_umltrace_kernel_tracedprimitivevalue_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedPrimitiveValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedstructuredvalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedStructuredValue)


def test_umltrace_kernel_tracedstructuredvalue_constructor_exists():
    assert callable(umlTrace_Kernel_TracedStructuredValue.__init__)


def test_umltrace_kernel_tracedstructuredvalue_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedStructuredValue.__init__)
    params = list(sig.parameters.keys())



def test_tracedstructuredvalue_is_not_abstract():
    assert not inspect.isabstract(TracedStructuredValue)


def test_tracedstructuredvalue_constructor_exists():
    assert callable(TracedStructuredValue.__init__)


def test_tracedstructuredvalue_constructor_args():
    sig = inspect.signature(TracedStructuredValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedreference_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedReference)


def test_umltrace_kernel_tracedreference_constructor_exists():
    assert callable(umlTrace_Kernel_TracedReference.__init__)


def test_umltrace_kernel_tracedreference_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedReference.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedcompoundvalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedCompoundValue)


def test_umltrace_kernel_tracedcompoundvalue_constructor_exists():
    assert callable(umlTrace_Kernel_TracedCompoundValue.__init__)


def test_umltrace_kernel_tracedcompoundvalue_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedCompoundValue.__init__)
    params = list(sig.parameters.keys())



def test_tracedcompoundvalue_is_not_abstract():
    assert not inspect.isabstract(TracedCompoundValue)


def test_tracedcompoundvalue_constructor_exists():
    assert callable(TracedCompoundValue.__init__)


def test_tracedcompoundvalue_constructor_args():
    sig = inspect.signature(TracedCompoundValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedextensionalvalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedExtensionalValue)


def test_umltrace_kernel_tracedextensionalvalue_constructor_exists():
    assert callable(umlTrace_Kernel_TracedExtensionalValue.__init__)


def test_umltrace_kernel_tracedextensionalvalue_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedExtensionalValue.__init__)
    params = list(sig.parameters.keys())



def test_tracedextensionalvalue_is_not_abstract():
    assert not inspect.isabstract(TracedExtensionalValue)


def test_tracedextensionalvalue_constructor_exists():
    assert callable(TracedExtensionalValue.__init__)


def test_tracedextensionalvalue_constructor_args():
    sig = inspect.signature(TracedExtensionalValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedobject_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedObject)


def test_umltrace_kernel_tracedobject_constructor_exists():
    assert callable(umlTrace_Kernel_TracedObject.__init__)


def test_umltrace_kernel_tracedobject_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedObject.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_basicbehaviors_tracedopaquebehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution)


def test_umltrace_basicbehaviors_tracedopaquebehaviorexecution_constructor_exists():
    assert callable(umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution.__init__)


def test_umltrace_basicbehaviors_tracedopaquebehaviorexecution_constructor_args():
    sig = inspect.signature(umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_tracedobject_is_not_abstract():
    assert not inspect.isabstract(TracedObject)


def test_tracedobject_constructor_exists():
    assert callable(TracedObject.__init__)


def test_tracedobject_constructor_args():
    sig = inspect.signature(TracedObject.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_basicbehaviors_tracedexecution_is_not_abstract():
    assert not inspect.isabstract(umlTrace_BasicBehaviors_TracedExecution)


def test_umltrace_basicbehaviors_tracedexecution_constructor_exists():
    assert callable(umlTrace_BasicBehaviors_TracedExecution.__init__)


def test_umltrace_basicbehaviors_tracedexecution_constructor_args():
    sig = inspect.signature(umlTrace_BasicBehaviors_TracedExecution.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedElement)


def test_uml_tracedelement_constructor_exists():
    assert callable(uml_TracedElement.__init__)


def test_uml_tracedelement_constructor_args():
    sig = inspect.signature(uml_TracedElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_semanticvisitor_runtimemodelelement_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_SemanticVisitor_runtimeModelElement_Value)


def test_umltrace_values_semanticvisitor_runtimemodelelement_value_constructor_exists():
    assert callable(umlTrace_Values_SemanticVisitor_runtimeModelElement_Value.__init__)


def test_umltrace_values_semanticvisitor_runtimemodelelement_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_SemanticVisitor_runtimeModelElement_Value.__init__)
    params = list(sig.parameters.keys())



def test_tracedopaquebehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(TracedOpaqueBehaviorExecution)


def test_tracedopaquebehaviorexecution_constructor_exists():
    assert callable(TracedOpaqueBehaviorExecution.__init__)


def test_tracedopaquebehaviorexecution_constructor_args():
    sig = inspect.signature(TracedOpaqueBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_integerfunctions_tracedintegergreaterfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution)


def test_umltrace_integerfunctions_tracedintegergreaterfunctionbehaviorexecution_constructor_exists():
    assert callable(umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution.__init__)


def test_umltrace_integerfunctions_tracedintegergreaterfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_integerfunctions_tracedintegerlessfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution)


def test_umltrace_integerfunctions_tracedintegerlessfunctionbehaviorexecution_constructor_exists():
    assert callable(umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution.__init__)


def test_umltrace_integerfunctions_tracedintegerlessfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_integerfunctions_tracedintegerplusfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution)


def test_umltrace_integerfunctions_tracedintegerplusfunctionbehaviorexecution_constructor_exists():
    assert callable(umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution.__init__)


def test_umltrace_integerfunctions_tracedintegerplusfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_tracedcallactionactivation_is_not_abstract():
    assert not inspect.isabstract(TracedCallActionActivation)


def test_tracedcallactionactivation_constructor_exists():
    assert callable(TracedCallActionActivation.__init__)


def test_tracedcallactionactivation_constructor_args():
    sig = inspect.signature(TracedCallActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_basicactions_tracedcallbehavioractionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_BasicActions_TracedCallBehaviorActionActivation)


def test_umltrace_basicactions_tracedcallbehavioractionactivation_constructor_exists():
    assert callable(umlTrace_BasicActions_TracedCallBehaviorActionActivation.__init__)


def test_umltrace_basicactions_tracedcallbehavioractionactivation_constructor_args():
    sig = inspect.signature(umlTrace_BasicActions_TracedCallBehaviorActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedpinactivation_is_not_abstract():
    assert not inspect.isabstract(TracedPinActivation)


def test_tracedpinactivation_constructor_exists():
    assert callable(TracedPinActivation.__init__)


def test_tracedpinactivation_constructor_args():
    sig = inspect.signature(TracedPinActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_basicactions_tracedoutputpinactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_BasicActions_TracedOutputPinActivation)


def test_umltrace_basicactions_tracedoutputpinactivation_constructor_exists():
    assert callable(umlTrace_BasicActions_TracedOutputPinActivation.__init__)


def test_umltrace_basicactions_tracedoutputpinactivation_constructor_args():
    sig = inspect.signature(umlTrace_BasicActions_TracedOutputPinActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_basicactions_tracedinputpinactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_BasicActions_TracedInputPinActivation)


def test_umltrace_basicactions_tracedinputpinactivation_constructor_exists():
    assert callable(umlTrace_BasicActions_TracedInputPinActivation.__init__)


def test_umltrace_basicactions_tracedinputpinactivation_constructor_args():
    sig = inspect.signature(umlTrace_BasicActions_TracedInputPinActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedinvocationactionactivation_is_not_abstract():
    assert not inspect.isabstract(TracedInvocationActionActivation)


def test_tracedinvocationactionactivation_constructor_exists():
    assert callable(TracedInvocationActionActivation.__init__)


def test_tracedinvocationactionactivation_constructor_args():
    sig = inspect.signature(TracedInvocationActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_basicactions_tracedcallactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_BasicActions_TracedCallActionActivation)


def test_umltrace_basicactions_tracedcallactionactivation_constructor_exists():
    assert callable(umlTrace_BasicActions_TracedCallActionActivation.__init__)


def test_umltrace_basicactions_tracedcallactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_BasicActions_TracedCallActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedactionactivation_is_not_abstract():
    assert not inspect.isabstract(TracedActionActivation)


def test_tracedactionactivation_constructor_exists():
    assert callable(TracedActionActivation.__init__)


def test_tracedactionactivation_constructor_args():
    sig = inspect.signature(TracedActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_basicactions_tracedopaqueactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_BasicActions_TracedOpaqueActionActivation)


def test_umltrace_basicactions_tracedopaqueactionactivation_constructor_exists():
    assert callable(umlTrace_BasicActions_TracedOpaqueActionActivation.__init__)


def test_umltrace_basicactions_tracedopaqueactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_BasicActions_TracedOpaqueActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_basicactions_tracedinvocationactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_BasicActions_TracedInvocationActionActivation)


def test_umltrace_basicactions_tracedinvocationactionactivation_constructor_exists():
    assert callable(umlTrace_BasicActions_TracedInvocationActionActivation.__init__)


def test_umltrace_basicactions_tracedinvocationactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_BasicActions_TracedInvocationActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_basicactions_tracedactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_BasicActions_TracedActionActivation)


def test_umltrace_basicactions_tracedactionactivation_constructor_exists():
    assert callable(umlTrace_BasicActions_TracedActionActivation.__init__)


def test_umltrace_basicactions_tracedactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_BasicActions_TracedActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_loci_tracedsemanticvisitor_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Loci_TracedSemanticVisitor)


def test_umltrace_loci_tracedsemanticvisitor_constructor_exists():
    assert callable(umlTrace_Loci_TracedSemanticVisitor.__init__)


def test_umltrace_loci_tracedsemanticvisitor_constructor_args():
    sig = inspect.signature(umlTrace_Loci_TracedSemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_traceddecisionnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedDecisionNodeActivation)


def test_umltrace_intermediateactivities_traceddecisionnodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedDecisionNodeActivation.__init__)


def test_umltrace_intermediateactivities_traceddecisionnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedDecisionNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedactivityfinalnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation)


def test_umltrace_intermediateactivities_tracedactivityfinalnodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedactivityfinalnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedjoinnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedJoinNodeActivation)


def test_umltrace_intermediateactivities_tracedjoinnodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedJoinNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedjoinnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedJoinNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedobjectnodeactivation_is_not_abstract():
    assert not inspect.isabstract(TracedObjectNodeActivation)


def test_tracedobjectnodeactivation_constructor_exists():
    assert callable(TracedObjectNodeActivation.__init__)


def test_tracedobjectnodeactivation_constructor_args():
    sig = inspect.signature(TracedObjectNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_basicactions_tracedpinactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_BasicActions_TracedPinActivation)


def test_umltrace_basicactions_tracedpinactivation_constructor_exists():
    assert callable(umlTrace_BasicActions_TracedPinActivation.__init__)


def test_umltrace_basicactions_tracedpinactivation_constructor_args():
    sig = inspect.signature(umlTrace_BasicActions_TracedPinActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedactivityparameternodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation)


def test_umltrace_intermediateactivities_tracedactivityparameternodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedactivityparameternodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactions_tracedcreateobjectactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActions_TracedCreateObjectActionActivation)


def test_umltrace_intermediateactions_tracedcreateobjectactionactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActions_TracedCreateObjectActionActivation.__init__)


def test_umltrace_intermediateactions_tracedcreateobjectactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActions_TracedCreateObjectActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactions_tracedvaluespecificationactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActions_TracedValueSpecificationActionActivation)


def test_umltrace_intermediateactions_tracedvaluespecificationactionactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActions_TracedValueSpecificationActionActivation.__init__)


def test_umltrace_intermediateactions_tracedvaluespecificationactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActions_TracedValueSpecificationActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedwritestructuralfeatureactionactivation_is_not_abstract():
    assert not inspect.isabstract(TracedWriteStructuralFeatureActionActivation)


def test_tracedwritestructuralfeatureactionactivation_constructor_exists():
    assert callable(TracedWriteStructuralFeatureActionActivation.__init__)


def test_tracedwritestructuralfeatureactionactivation_constructor_args():
    sig = inspect.signature(TracedWriteStructuralFeatureActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactions_tracedaddstructuralfeaturevalueactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation)


def test_umltrace_intermediateactions_tracedaddstructuralfeaturevalueactionactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation.__init__)


def test_umltrace_intermediateactions_tracedaddstructuralfeaturevalueactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedstructuralfeatureactionactivation_is_not_abstract():
    assert not inspect.isabstract(TracedStructuralFeatureActionActivation)


def test_tracedstructuralfeatureactionactivation_constructor_exists():
    assert callable(TracedStructuralFeatureActionActivation.__init__)


def test_tracedstructuralfeatureactionactivation_constructor_args():
    sig = inspect.signature(TracedStructuralFeatureActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactions_tracedwritestructuralfeatureactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation)


def test_umltrace_intermediateactions_tracedwritestructuralfeatureactionactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation.__init__)


def test_umltrace_intermediateactions_tracedwritestructuralfeatureactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactions_tracedreadstructuralfeatureactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation)


def test_umltrace_intermediateactions_tracedreadstructuralfeatureactionactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation.__init__)


def test_umltrace_intermediateactions_tracedreadstructuralfeatureactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactions_tracedstructuralfeatureactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation)


def test_umltrace_intermediateactions_tracedstructuralfeatureactionactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation.__init__)


def test_umltrace_intermediateactions_tracedstructuralfeatureactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_ecore_tracedemodelelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_ecore_TracedEModelElement)


def test_umltrace_ecore_tracedemodelelement_constructor_exists():
    assert callable(umlTrace_ecore_TracedEModelElement.__init__)


def test_umltrace_ecore_tracedemodelelement_constructor_args():
    sig = inspect.signature(umlTrace_ecore_TracedEModelElement.__init__)
    params = list(sig.parameters.keys())



def test_tracedmessageend_is_not_abstract():
    assert not inspect.isabstract(TracedMessageEnd)


def test_tracedmessageend_constructor_exists():
    assert callable(TracedMessageEnd.__init__)


def test_tracedmessageend_constructor_args():
    sig = inspect.signature(TracedMessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedgate_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedGate)


def test_umltrace_uml_tracedgate_constructor_exists():
    assert callable(umlTrace_uml_TracedGate.__init__)


def test_umltrace_uml_tracedgate_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedGate.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAction)


def test_uml_tracedaction_constructor_exists():
    assert callable(uml_TracedAction.__init__)


def test_uml_tracedaction_constructor_args():
    sig = inspect.signature(uml_TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedstructuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(TracedStructuredActivityNode)


def test_tracedstructuredactivitynode_constructor_exists():
    assert callable(TracedStructuredActivityNode.__init__)


def test_tracedstructuredactivitynode_constructor_args():
    sig = inspect.signature(TracedStructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedconditionalnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedConditionalNode)


def test_umltrace_uml_tracedconditionalnode_constructor_exists():
    assert callable(umlTrace_uml_TracedConditionalNode.__init__)


def test_umltrace_uml_tracedconditionalnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedConditionalNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedemodelelement_is_not_abstract():
    assert not inspect.isabstract(TracedEModelElement)


def test_tracedemodelelement_constructor_exists():
    assert callable(TracedEModelElement.__init__)


def test_tracedemodelelement_constructor_args():
    sig = inspect.signature(TracedEModelElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedElement)


def test_umltrace_uml_tracedelement_constructor_exists():
    assert callable(umlTrace_uml_TracedElement.__init__)


def test_umltrace_uml_tracedelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedElement.__init__)
    params = list(sig.parameters.keys())



def test_tracedelement_is_not_abstract():
    assert not inspect.isabstract(TracedElement)


def test_tracedelement_constructor_exists():
    assert callable(TracedElement.__init__)


def test_tracedelement_constructor_args():
    sig = inspect.signature(TracedElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtemplateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTemplateParameterSubstitution)


def test_umltrace_uml_tracedtemplateparametersubstitution_constructor_exists():
    assert callable(umlTrace_uml_TracedTemplateParameterSubstitution.__init__)


def test_umltrace_uml_tracedtemplateparametersubstitution_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedqualifiervalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedQualifierValue)


def test_umltrace_uml_tracedqualifiervalue_constructor_exists():
    assert callable(umlTrace_uml_TracedQualifierValue.__init__)


def test_umltrace_uml_tracedqualifiervalue_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedQualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcomment_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedComment)


def test_umltrace_uml_tracedcomment_constructor_exists():
    assert callable(umlTrace_uml_TracedComment.__init__)


def test_umltrace_uml_tracedcomment_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedComment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedclause_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedClause)


def test_umltrace_uml_tracedclause_constructor_exists():
    assert callable(umlTrace_uml_TracedClause.__init__)


def test_umltrace_uml_tracedclause_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedClause.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracednamedelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedNamedElement)


def test_umltrace_uml_tracednamedelement_constructor_exists():
    assert callable(umlTrace_uml_TracedNamedElement.__init__)


def test_umltrace_uml_tracednamedelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_tracednamedelement_is_not_abstract():
    assert not inspect.isabstract(TracedNamedElement)


def test_tracednamedelement_constructor_exists():
    assert callable(TracedNamedElement.__init__)


def test_tracednamedelement_constructor_args():
    sig = inspect.signature(TracedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedgeneralordering_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedGeneralOrdering)


def test_umltrace_uml_tracedgeneralordering_constructor_exists():
    assert callable(umlTrace_uml_TracedGeneralOrdering.__init__)


def test_umltrace_uml_tracedgeneralordering_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedGeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedparameterset_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedParameterSet)


def test_umltrace_uml_tracedparameterset_constructor_exists():
    assert callable(umlTrace_uml_TracedParameterSet.__init__)


def test_umltrace_uml_tracedparameterset_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinteractionfragment_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInteractionFragment)


def test_umltrace_uml_tracedinteractionfragment_constructor_exists():
    assert callable(umlTrace_uml_TracedInteractionFragment.__init__)


def test_umltrace_uml_tracedinteractionfragment_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedmessageend_is_not_abstract():
    assert not inspect.isabstract(uml_TracedMessageEnd)


def test_uml_tracedmessageend_constructor_exists():
    assert callable(uml_TracedMessageEnd.__init__)


def test_uml_tracedmessageend_constructor_args():
    sig = inspect.signature(uml_TracedMessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_tracedmessageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(TracedMessageOccurrenceSpecification)


def test_tracedmessageoccurrencespecification_constructor_exists():
    assert callable(TracedMessageOccurrenceSpecification.__init__)


def test_tracedmessageoccurrencespecification_constructor_args():
    sig = inspect.signature(TracedMessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddestructionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDestructionOccurrenceSpecification)


def test_umltrace_uml_traceddestructionoccurrencespecification_constructor_exists():
    assert callable(umlTrace_uml_TracedDestructionOccurrenceSpecification.__init__)


def test_umltrace_uml_traceddestructionoccurrencespecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDestructionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedvertex_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedVertex)


def test_umltrace_uml_tracedvertex_constructor_exists():
    assert callable(umlTrace_uml_TracedVertex.__init__)


def test_umltrace_uml_tracedvertex_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedVertex.__init__)
    params = list(sig.parameters.keys())



def test_tracedvertex_is_not_abstract():
    assert not inspect.isabstract(TracedVertex)


def test_tracedvertex_constructor_exists():
    assert callable(TracedVertex.__init__)


def test_tracedvertex_constructor_args():
    sig = inspect.signature(TracedVertex.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedconnectionpointreference_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedConnectionPointReference)


def test_umltrace_uml_tracedconnectionpointreference_constructor_exists():
    assert callable(umlTrace_uml_TracedConnectionPointReference.__init__)


def test_umltrace_uml_tracedconnectionpointreference_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedpseudostate_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedPseudostate)


def test_umltrace_uml_tracedpseudostate_constructor_exists():
    assert callable(umlTrace_uml_TracedPseudostate.__init__)


def test_umltrace_uml_tracedpseudostate_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedPseudostate.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedparameterableelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedParameterableElement)


def test_umltrace_uml_tracedparameterableelement_constructor_exists():
    assert callable(umlTrace_uml_TracedParameterableElement.__init__)


def test_umltrace_uml_tracedparameterableelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedparameterableelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedParameterableElement)


def test_uml_tracedparameterableelement_constructor_exists():
    assert callable(uml_TracedParameterableElement.__init__)


def test_uml_tracedparameterableelement_constructor_args():
    sig = inspect.signature(uml_TracedParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_tracedpackageableelement_is_not_abstract():
    assert not inspect.isabstract(TracedPackageableElement)


def test_tracedpackageableelement_constructor_exists():
    assert callable(TracedPackageableElement.__init__)


def test_tracedpackageableelement_constructor_args():
    sig = inspect.signature(TracedPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedconstraint_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedConstraint)


def test_umltrace_uml_tracedconstraint_constructor_exists():
    assert callable(umlTrace_uml_TracedConstraint.__init__)


def test_umltrace_uml_tracedconstraint_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedConstraint.__init__)
    params = list(sig.parameters.keys())



def test_tracedconstraint_is_not_abstract():
    assert not inspect.isabstract(TracedConstraint)


def test_tracedconstraint_constructor_exists():
    assert callable(TracedConstraint.__init__)


def test_tracedconstraint_constructor_args():
    sig = inspect.signature(TracedConstraint.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinteractionconstraint_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInteractionConstraint)


def test_umltrace_uml_tracedinteractionconstraint_constructor_exists():
    assert callable(umlTrace_uml_TracedInteractionConstraint.__init__)


def test_umltrace_uml_tracedinteractionconstraint_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedintervalconstraint_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedIntervalConstraint)


def test_umltrace_uml_tracedintervalconstraint_constructor_exists():
    assert callable(umlTrace_uml_TracedIntervalConstraint.__init__)


def test_umltrace_uml_tracedintervalconstraint_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedIntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_tracedintervalconstraint_is_not_abstract():
    assert not inspect.isabstract(TracedIntervalConstraint)


def test_tracedintervalconstraint_constructor_exists():
    assert callable(TracedIntervalConstraint.__init__)


def test_tracedintervalconstraint_constructor_args():
    sig = inspect.signature(TracedIntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddurationconstraint_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDurationConstraint)


def test_umltrace_uml_traceddurationconstraint_constructor_exists():
    assert callable(umlTrace_uml_TracedDurationConstraint.__init__)


def test_umltrace_uml_traceddurationconstraint_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDurationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcontrolflow_is_not_abstract():
    assert not inspect.isabstract(uml_TracedControlFlow)


def test_uml_tracedcontrolflow_constructor_exists():
    assert callable(uml_TracedControlFlow.__init__)


def test_uml_tracedcontrolflow_constructor_args():
    sig = inspect.signature(uml_TracedControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtimeobservation_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTimeObservation)


def test_uml_tracedtimeobservation_constructor_exists():
    assert callable(uml_TracedTimeObservation.__init__)


def test_uml_tracedtimeobservation_constructor_args():
    sig = inspect.signature(uml_TracedTimeObservation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedgate_is_not_abstract():
    assert not inspect.isabstract(uml_TracedGate)


def test_uml_tracedgate_constructor_exists():
    assert callable(uml_TracedGate.__init__)


def test_uml_tracedgate_constructor_args():
    sig = inspect.signature(uml_TracedGate.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactivityfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActivityFinalNode)


def test_uml_tracedactivityfinalnode_constructor_exists():
    assert callable(uml_TracedActivityFinalNode.__init__)


def test_uml_tracedactivityfinalnode_constructor_args():
    sig = inspect.signature(uml_TracedActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedclassifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml_TracedClassifierTemplateParameter)


def test_uml_tracedclassifiertemplateparameter_constructor_exists():
    assert callable(uml_TracedClassifierTemplateParameter.__init__)


def test_uml_tracedclassifiertemplateparameter_constructor_args():
    sig = inspect.signature(uml_TracedClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_tracedinteractionfragment_is_not_abstract():
    assert not inspect.isabstract(TracedInteractionFragment)


def test_tracedinteractionfragment_constructor_exists():
    assert callable(TracedInteractionFragment.__init__)


def test_tracedinteractionfragment_constructor_args():
    sig = inspect.signature(TracedInteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedOccurrenceSpecification)


def test_umltrace_uml_tracedoccurrencespecification_constructor_exists():
    assert callable(umlTrace_uml_TracedOccurrenceSpecification.__init__)


def test_umltrace_uml_tracedoccurrencespecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcombinedfragment_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCombinedFragment)


def test_umltrace_uml_tracedcombinedfragment_constructor_exists():
    assert callable(umlTrace_uml_TracedCombinedFragment.__init__)


def test_umltrace_uml_tracedcombinedfragment_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedgeneralordering_is_not_abstract():
    assert not inspect.isabstract(uml_TracedGeneralOrdering)


def test_uml_tracedgeneralordering_constructor_exists():
    assert callable(uml_TracedGeneralOrdering.__init__)


def test_uml_tracedgeneralordering_constructor_args():
    sig = inspect.signature(uml_TracedGeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedelementimport_is_not_abstract():
    assert not inspect.isabstract(uml_TracedElementImport)


def test_uml_tracedelementimport_constructor_exists():
    assert callable(uml_TracedElementImport.__init__)


def test_uml_tracedelementimport_constructor_args():
    sig = inspect.signature(uml_TracedElementImport.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedmergenode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedMergeNode)


def test_uml_tracedmergenode_constructor_exists():
    assert callable(uml_TracedMergeNode.__init__)


def test_uml_tracedmergenode_constructor_args():
    sig = inspect.signature(uml_TracedMergeNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedclearassociationaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedClearAssociationAction)


def test_uml_tracedclearassociationaction_constructor_exists():
    assert callable(uml_TracedClearAssociationAction.__init__)


def test_uml_tracedclearassociationaction_constructor_args():
    sig = inspect.signature(uml_TracedClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedlinkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLinkEndCreationData)


def test_uml_tracedlinkendcreationdata_constructor_exists():
    assert callable(uml_TracedLinkEndCreationData.__init__)


def test_uml_tracedlinkendcreationdata_constructor_args():
    sig = inspect.signature(uml_TracedLinkEndCreationData.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedpseudostate_is_not_abstract():
    assert not inspect.isabstract(uml_TracedPseudostate)


def test_uml_tracedpseudostate_constructor_exists():
    assert callable(uml_TracedPseudostate.__init__)


def test_uml_tracedpseudostate_constructor_args():
    sig = inspect.signature(uml_TracedPseudostate.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcomponent_is_not_abstract():
    assert not inspect.isabstract(uml_TracedComponent)


def test_uml_tracedcomponent_constructor_exists():
    assert callable(uml_TracedComponent.__init__)


def test_uml_tracedcomponent_constructor_args():
    sig = inspect.signature(uml_TracedComponent.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadIsClassifiedObjectAction)


def test_uml_tracedreadisclassifiedobjectaction_constructor_exists():
    assert callable(uml_TracedReadIsClassifiedObjectAction.__init__)


def test_uml_tracedreadisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(uml_TracedReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedabstraction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAbstraction)


def test_uml_tracedabstraction_constructor_exists():
    assert callable(uml_TracedAbstraction.__init__)


def test_uml_tracedabstraction_constructor_args():
    sig = inspect.signature(uml_TracedAbstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtimeexpression_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTimeExpression)


def test_uml_tracedtimeexpression_constructor_exists():
    assert callable(uml_TracedTimeExpression.__init__)


def test_uml_tracedtimeexpression_constructor_args():
    sig = inspect.signature(uml_TracedTimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedvaluespecificationaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedValueSpecificationAction)


def test_uml_tracedvaluespecificationaction_constructor_exists():
    assert callable(uml_TracedValueSpecificationAction.__init__)


def test_uml_tracedvaluespecificationaction_constructor_args():
    sig = inspect.signature(uml_TracedValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedfunctionbehavior_is_not_abstract():
    assert not inspect.isabstract(uml_TracedFunctionBehavior)


def test_uml_tracedfunctionbehavior_constructor_exists():
    assert callable(uml_TracedFunctionBehavior.__init__)


def test_uml_tracedfunctionbehavior_constructor_args():
    sig = inspect.signature(uml_TracedFunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_integerfunctions_tracedintegergreaterfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution)


def test_integerfunctions_tracedintegergreaterfunctionbehaviorexecution_constructor_exists():
    assert callable(IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution.__init__)


def test_integerfunctions_tracedintegergreaterfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedmergenodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedMergeNodeActivation)


def test_intermediateactivities_tracedmergenodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedMergeNodeActivation.__init__)


def test_intermediateactivities_tracedmergenodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedMergeNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTemplateParameter)


def test_uml_tracedtemplateparameter_constructor_exists():
    assert callable(uml_TracedTemplateParameter.__init__)


def test_uml_tracedtemplateparameter_constructor_args():
    sig = inspect.signature(uml_TracedTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedmanifestation_is_not_abstract():
    assert not inspect.isabstract(uml_TracedManifestation)


def test_uml_tracedmanifestation_constructor_exists():
    assert callable(uml_TracedManifestation.__init__)


def test_uml_tracedmanifestation_constructor_args():
    sig = inspect.signature(uml_TracedManifestation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactor_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActor)


def test_uml_tracedactor_constructor_exists():
    assert callable(uml_TracedActor.__init__)


def test_uml_tracedactor_constructor_args():
    sig = inspect.signature(uml_TracedActor.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedremovevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRemoveVariableValueAction)


def test_uml_tracedremovevariablevalueaction_constructor_exists():
    assert callable(uml_TracedRemoveVariableValueAction.__init__)


def test_uml_tracedremovevariablevalueaction_constructor_args():
    sig = inspect.signature(uml_TracedRemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedprofile_is_not_abstract():
    assert not inspect.isabstract(uml_TracedProfile)


def test_uml_tracedprofile_constructor_exists():
    assert callable(uml_TracedProfile.__init__)


def test_uml_tracedprofile_constructor_args():
    sig = inspect.signature(uml_TracedProfile.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtestidentityaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTestIdentityAction)


def test_uml_tracedtestidentityaction_constructor_exists():
    assert callable(uml_TracedTestIdentityAction.__init__)


def test_uml_tracedtestidentityaction_constructor_args():
    sig = inspect.signature(uml_TracedTestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcollaboration_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCollaboration)


def test_uml_tracedcollaboration_constructor_exists():
    assert callable(uml_TracedCollaboration.__init__)


def test_uml_tracedcollaboration_constructor_args():
    sig = inspect.signature(uml_TracedCollaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedsendsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedSendSignalAction)


def test_uml_tracedsendsignalaction_constructor_exists():
    assert callable(uml_TracedSendSignalAction.__init__)


def test_uml_tracedsendsignalaction_constructor_args():
    sig = inspect.signature(uml_TracedSendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinterfacerealization_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInterfaceRealization)


def test_uml_tracedinterfacerealization_constructor_exists():
    assert callable(uml_TracedInterfaceRealization.__init__)


def test_uml_tracedinterfacerealization_constructor_args():
    sig = inspect.signature(uml_TracedInterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedunmarshallaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedUnmarshallAction)


def test_uml_tracedunmarshallaction_constructor_exists():
    assert callable(uml_TracedUnmarshallAction.__init__)


def test_uml_tracedunmarshallaction_constructor_args():
    sig = inspect.signature(uml_TracedUnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedexpression_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExpression)


def test_uml_tracedexpression_constructor_exists():
    assert callable(uml_TracedExpression.__init__)


def test_uml_tracedexpression_constructor_args():
    sig = inspect.signature(uml_TracedExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedassociation_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAssociation)


def test_uml_tracedassociation_constructor_exists():
    assert callable(uml_TracedAssociation.__init__)


def test_uml_tracedassociation_constructor_args():
    sig = inspect.signature(uml_TracedAssociation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedclearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedClearStructuralFeatureAction)


def test_uml_tracedclearstructuralfeatureaction_constructor_exists():
    assert callable(uml_TracedClearStructuralFeatureAction.__init__)


def test_uml_tracedclearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml_TracedClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedaddvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAddVariableValueAction)


def test_uml_tracedaddvariablevalueaction_constructor_exists():
    assert callable(uml_TracedAddVariableValueAction.__init__)


def test_uml_tracedaddvariablevalueaction_constructor_args():
    sig = inspect.signature(uml_TracedAddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedliteralreal_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLiteralReal)


def test_uml_tracedliteralreal_constructor_exists():
    assert callable(uml_TracedLiteralReal.__init__)


def test_uml_tracedliteralreal_constructor_args():
    sig = inspect.signature(uml_TracedLiteralReal.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions_tracedcreateobjectactionactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_TracedCreateObjectActionActivation)


def test_intermediateactions_tracedcreateobjectactionactivation_constructor_exists():
    assert callable(IntermediateActions_TracedCreateObjectActionActivation.__init__)


def test_intermediateactions_tracedcreateobjectactionactivation_constructor_args():
    sig = inspect.signature(IntermediateActions_TracedCreateObjectActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedslot_is_not_abstract():
    assert not inspect.isabstract(uml_TracedSlot)


def test_uml_tracedslot_constructor_exists():
    assert callable(uml_TracedSlot.__init__)


def test_uml_tracedslot_constructor_args():
    sig = inspect.signature(uml_TracedSlot.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedliteralnull_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLiteralNull)


def test_uml_tracedliteralnull_constructor_exists():
    assert callable(uml_TracedLiteralNull.__init__)


def test_uml_tracedliteralnull_constructor_args():
    sig = inspect.signature(uml_TracedLiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions_tracedvaluespecificationactionactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_TracedValueSpecificationActionActivation)


def test_intermediateactions_tracedvaluespecificationactionactivation_constructor_exists():
    assert callable(IntermediateActions_TracedValueSpecificationActionActivation.__init__)


def test_intermediateactions_tracedvaluespecificationactionactivation_constructor_args():
    sig = inspect.signature(IntermediateActions_TracedValueSpecificationActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstartobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStartObjectBehaviorAction)


def test_uml_tracedstartobjectbehavioraction_constructor_exists():
    assert callable(uml_TracedStartObjectBehaviorAction.__init__)


def test_uml_tracedstartobjectbehavioraction_constructor_args():
    sig = inspect.signature(uml_TracedStartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedliteralboolean_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLiteralBoolean)


def test_uml_tracedliteralboolean_constructor_exists():
    assert callable(uml_TracedLiteralBoolean.__init__)


def test_uml_tracedliteralboolean_constructor_args():
    sig = inspect.signature(uml_TracedLiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadlinkaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadLinkAction)


def test_uml_tracedreadlinkaction_constructor_exists():
    assert callable(uml_TracedReadLinkAction.__init__)


def test_uml_tracedreadlinkaction_constructor_args():
    sig = inspect.signature(uml_TracedReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinclude_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInclude)


def test_uml_tracedinclude_constructor_exists():
    assert callable(uml_TracedInclude.__init__)


def test_uml_tracedinclude_constructor_args():
    sig = inspect.signature(uml_TracedInclude.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedregion_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRegion)


def test_uml_tracedregion_constructor_exists():
    assert callable(uml_TracedRegion.__init__)


def test_uml_tracedregion_constructor_args():
    sig = inspect.signature(uml_TracedRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstate_is_not_abstract():
    assert not inspect.isabstract(uml_TracedState)


def test_uml_tracedstate_constructor_exists():
    assert callable(uml_TracedState.__init__)


def test_uml_tracedstate_constructor_args():
    sig = inspect.signature(uml_TracedState.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedprimitivetype_is_not_abstract():
    assert not inspect.isabstract(uml_TracedPrimitiveType)


def test_uml_tracedprimitivetype_constructor_exists():
    assert callable(uml_TracedPrimitiveType.__init__)


def test_uml_tracedprimitivetype_constructor_args():
    sig = inspect.signature(uml_TracedPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstringexpression_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStringExpression)


def test_uml_tracedstringexpression_constructor_exists():
    assert callable(uml_TracedStringExpression.__init__)


def test_uml_tracedstringexpression_constructor_args():
    sig = inspect.signature(uml_TracedStringExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedlinkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLinkEndDestructionData)


def test_uml_tracedlinkenddestructiondata_constructor_exists():
    assert callable(uml_TracedLinkEndDestructionData.__init__)


def test_uml_tracedlinkenddestructiondata_constructor_args():
    sig = inspect.signature(uml_TracedLinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedanyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedAnyReceiveEvent)


def test_umltrace_uml_tracedanyreceiveevent_constructor_exists():
    assert callable(umlTrace_uml_TracedAnyReceiveEvent.__init__)


def test_umltrace_uml_tracedanyreceiveevent_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedAnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadextentaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadExtentAction)


def test_uml_tracedreadextentaction_constructor_exists():
    assert callable(uml_TracedReadExtentAction.__init__)


def test_uml_tracedreadextentaction_constructor_args():
    sig = inspect.signature(uml_TracedReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_tracedoutputpinactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions_TracedOutputPinActivation)


def test_basicactions_tracedoutputpinactivation_constructor_exists():
    assert callable(BasicActions_TracedOutputPinActivation.__init__)


def test_basicactions_tracedoutputpinactivation_constructor_args():
    sig = inspect.signature(BasicActions_TracedOutputPinActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedbehavioralfeature_is_not_abstract():
    assert not inspect.isabstract(uml_TracedBehavioralFeature)


def test_uml_tracedbehavioralfeature_constructor_exists():
    assert callable(uml_TracedBehavioralFeature.__init__)


def test_uml_tracedbehavioralfeature_constructor_args():
    sig = inspect.signature(uml_TracedBehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtemplatesignature_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTemplateSignature)


def test_uml_tracedtemplatesignature_constructor_exists():
    assert callable(uml_TracedTemplateSignature.__init__)


def test_uml_tracedtemplatesignature_constructor_args():
    sig = inspect.signature(uml_TracedTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTemplateParameter)


def test_umltrace_uml_tracedtemplateparameter_constructor_exists():
    assert callable(umlTrace_uml_TracedTemplateParameter.__init__)


def test_umltrace_uml_tracedtemplateparameter_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_tracedtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(TracedTemplateParameter)


def test_tracedtemplateparameter_constructor_exists():
    assert callable(TracedTemplateParameter.__init__)


def test_tracedtemplateparameter_constructor_args():
    sig = inspect.signature(TracedTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedconnectableelementtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedConnectableElementTemplateParameter)


def test_umltrace_uml_tracedconnectableelementtemplateparameter_constructor_exists():
    assert callable(umlTrace_uml_TracedConnectableElementTemplateParameter.__init__)


def test_umltrace_uml_tracedconnectableelementtemplateparameter_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedConnectableElementTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedclassifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedClassifierTemplateParameter)


def test_umltrace_uml_tracedclassifiertemplateparameter_constructor_exists():
    assert callable(umlTrace_uml_TracedClassifierTemplateParameter.__init__)


def test_umltrace_uml_tracedclassifiertemplateparameter_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_tracedpackage_is_not_abstract():
    assert not inspect.isabstract(TracedPackage)


def test_tracedpackage_constructor_exists():
    assert callable(TracedPackage.__init__)


def test_tracedpackage_constructor_args():
    sig = inspect.signature(TracedPackage.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedprofile_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedProfile)


def test_umltrace_uml_tracedprofile_constructor_exists():
    assert callable(umlTrace_uml_TracedProfile.__init__)


def test_umltrace_uml_tracedprofile_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedProfile.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedmodel_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedModel)


def test_umltrace_uml_tracedmodel_constructor_exists():
    assert callable(umlTrace_uml_TracedModel.__init__)


def test_umltrace_uml_tracedmodel_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedModel.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedimage_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedImage)


def test_umltrace_uml_tracedimage_constructor_exists():
    assert callable(umlTrace_uml_TracedImage.__init__)


def test_umltrace_uml_tracedimage_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedImage.__init__)
    params = list(sig.parameters.keys())



def test_tracedtransition_is_not_abstract():
    assert not inspect.isabstract(TracedTransition)


def test_tracedtransition_constructor_exists():
    assert callable(TracedTransition.__init__)


def test_tracedtransition_constructor_args():
    sig = inspect.signature(TracedTransition.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedprotocoltransition_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedProtocolTransition)


def test_umltrace_uml_tracedprotocoltransition_constructor_exists():
    assert callable(umlTrace_uml_TracedProtocolTransition.__init__)


def test_umltrace_uml_tracedprotocoltransition_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_tracedwritevariableaction_is_not_abstract():
    assert not inspect.isabstract(TracedWriteVariableAction)


def test_tracedwritevariableaction_constructor_exists():
    assert callable(TracedWriteVariableAction.__init__)


def test_tracedwritevariableaction_constructor_args():
    sig = inspect.signature(TracedWriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedremovevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedRemoveVariableValueAction)


def test_umltrace_uml_tracedremovevariablevalueaction_constructor_exists():
    assert callable(umlTrace_uml_TracedRemoveVariableValueAction.__init__)


def test_umltrace_uml_tracedremovevariablevalueaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedRemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedaddvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedAddVariableValueAction)


def test_umltrace_uml_tracedaddvariablevalueaction_constructor_exists():
    assert callable(umlTrace_uml_TracedAddVariableValueAction.__init__)


def test_umltrace_uml_tracedaddvariablevalueaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedAddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedinteractionuse_is_not_abstract():
    assert not inspect.isabstract(TracedInteractionUse)


def test_tracedinteractionuse_constructor_exists():
    assert callable(TracedInteractionUse.__init__)


def test_tracedinteractionuse_constructor_args():
    sig = inspect.signature(TracedInteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedpartdecomposition_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedPartDecomposition)


def test_umltrace_uml_tracedpartdecomposition_constructor_exists():
    assert callable(umlTrace_uml_TracedPartDecomposition.__init__)


def test_umltrace_uml_tracedpartdecomposition_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedPartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_tracedobservation_is_not_abstract():
    assert not inspect.isabstract(TracedObservation)


def test_tracedobservation_constructor_exists():
    assert callable(TracedObservation.__init__)


def test_tracedobservation_constructor_args():
    sig = inspect.signature(TracedObservation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtimeobservation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTimeObservation)


def test_umltrace_uml_tracedtimeobservation_constructor_exists():
    assert callable(umlTrace_uml_TracedTimeObservation.__init__)


def test_umltrace_uml_tracedtimeobservation_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTimeObservation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddurationobservation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDurationObservation)


def test_umltrace_uml_traceddurationobservation_constructor_exists():
    assert callable(umlTrace_uml_TracedDurationObservation.__init__)


def test_umltrace_uml_traceddurationobservation_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDurationObservation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedoperationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedOperationTemplateParameter)


def test_umltrace_uml_tracedoperationtemplateparameter_constructor_exists():
    assert callable(umlTrace_uml_TracedOperationTemplateParameter.__init__)


def test_umltrace_uml_tracedoperationtemplateparameter_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedOperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_tracedinterval_is_not_abstract():
    assert not inspect.isabstract(TracedInterval)


def test_tracedinterval_constructor_exists():
    assert callable(TracedInterval.__init__)


def test_tracedinterval_constructor_args():
    sig = inspect.signature(TracedInterval.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddurationinterval_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDurationInterval)


def test_umltrace_uml_traceddurationinterval_constructor_exists():
    assert callable(umlTrace_uml_TracedDurationInterval.__init__)


def test_umltrace_uml_traceddurationinterval_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtimeinterval_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTimeInterval)


def test_umltrace_uml_tracedtimeinterval_constructor_exists():
    assert callable(umlTrace_uml_TracedTimeInterval.__init__)


def test_umltrace_uml_tracedtimeinterval_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedsignalevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedSignalEvent)


def test_umltrace_uml_tracedsignalevent_constructor_exists():
    assert callable(umlTrace_uml_TracedSignalEvent.__init__)


def test_umltrace_uml_tracedsignalevent_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedSignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_tracedbehavioralfeature_is_not_abstract():
    assert not inspect.isabstract(TracedBehavioralFeature)


def test_tracedbehavioralfeature_constructor_exists():
    assert callable(TracedBehavioralFeature.__init__)


def test_tracedbehavioralfeature_constructor_args():
    sig = inspect.signature(TracedBehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreception_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReception)


def test_umltrace_uml_tracedreception_constructor_exists():
    assert callable(umlTrace_uml_TracedReception.__init__)


def test_umltrace_uml_tracedreception_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReception.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExecutionSpecification)


def test_umltrace_uml_tracedexecutionspecification_constructor_exists():
    assert callable(umlTrace_uml_TracedExecutionSpecification.__init__)


def test_umltrace_uml_tracedexecutionspecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_traceddependency_is_not_abstract():
    assert not inspect.isabstract(TracedDependency)


def test_traceddependency_constructor_exists():
    assert callable(TracedDependency.__init__)


def test_traceddependency_constructor_args():
    sig = inspect.signature(TracedDependency.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedusage_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedUsage)


def test_umltrace_uml_tracedusage_constructor_exists():
    assert callable(umlTrace_uml_TracedUsage.__init__)


def test_umltrace_uml_tracedusage_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedUsage.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedabstraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedAbstraction)


def test_umltrace_uml_tracedabstraction_constructor_exists():
    assert callable(umlTrace_uml_TracedAbstraction.__init__)


def test_umltrace_uml_tracedabstraction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedAbstraction.__init__)
    params = list(sig.parameters.keys())



def test_tracedabstraction_is_not_abstract():
    assert not inspect.isabstract(TracedAbstraction)


def test_tracedabstraction_constructor_exists():
    assert callable(TracedAbstraction.__init__)


def test_tracedabstraction_constructor_args():
    sig = inspect.signature(TracedAbstraction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedmanifestation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedManifestation)


def test_umltrace_uml_tracedmanifestation_constructor_exists():
    assert callable(umlTrace_uml_TracedManifestation.__init__)


def test_umltrace_uml_tracedmanifestation_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedManifestation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedrealization_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedRealization)


def test_umltrace_uml_tracedrealization_constructor_exists():
    assert callable(umlTrace_uml_TracedRealization.__init__)


def test_umltrace_uml_tracedrealization_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedRealization.__init__)
    params = list(sig.parameters.keys())



def test_tracedrealization_is_not_abstract():
    assert not inspect.isabstract(TracedRealization)


def test_tracedrealization_constructor_exists():
    assert callable(TracedRealization.__init__)


def test_tracedrealization_constructor_args():
    sig = inspect.signature(TracedRealization.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcomponentrealization_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedComponentRealization)


def test_umltrace_uml_tracedcomponentrealization_constructor_exists():
    assert callable(umlTrace_uml_TracedComponentRealization.__init__)


def test_umltrace_uml_tracedcomponentrealization_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedComponentRealization.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinterfacerealization_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInterfaceRealization)


def test_umltrace_uml_tracedinterfacerealization_constructor_exists():
    assert callable(umlTrace_uml_TracedInterfaceRealization.__init__)


def test_umltrace_uml_tracedinterfacerealization_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedsubstitution_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedSubstitution)


def test_umltrace_uml_tracedsubstitution_constructor_exists():
    assert callable(umlTrace_uml_TracedSubstitution.__init__)


def test_umltrace_uml_tracedsubstitution_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_tracedinstancespecification_is_not_abstract():
    assert not inspect.isabstract(TracedInstanceSpecification)


def test_tracedinstancespecification_constructor_exists():
    assert callable(TracedInstanceSpecification.__init__)


def test_tracedinstancespecification_constructor_args():
    sig = inspect.signature(TracedInstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedenumerationliteral_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedEnumerationLiteral)


def test_umltrace_uml_tracedenumerationliteral_constructor_exists():
    assert callable(umlTrace_uml_TracedEnumerationLiteral.__init__)


def test_umltrace_uml_tracedenumerationliteral_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedEnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_tracedaccepteventaction_is_not_abstract():
    assert not inspect.isabstract(TracedAcceptEventAction)


def test_tracedaccepteventaction_constructor_exists():
    assert callable(TracedAcceptEventAction.__init__)


def test_tracedaccepteventaction_constructor_args():
    sig = inspect.signature(TracedAcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedacceptcallaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedAcceptCallAction)


def test_umltrace_uml_tracedacceptcallaction_constructor_exists():
    assert callable(umlTrace_uml_TracedAcceptCallAction.__init__)


def test_umltrace_uml_tracedacceptcallaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedAcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedlinkenddata_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLinkEndData)


def test_umltrace_uml_tracedlinkenddata_constructor_exists():
    assert callable(umlTrace_uml_TracedLinkEndData.__init__)


def test_umltrace_uml_tracedlinkenddata_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_tracedlinkenddata_is_not_abstract():
    assert not inspect.isabstract(TracedLinkEndData)


def test_tracedlinkenddata_constructor_exists():
    assert callable(TracedLinkEndData.__init__)


def test_tracedlinkenddata_constructor_args():
    sig = inspect.signature(TracedLinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedlinkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLinkEndCreationData)


def test_umltrace_uml_tracedlinkendcreationdata_constructor_exists():
    assert callable(umlTrace_uml_TracedLinkEndCreationData.__init__)


def test_umltrace_uml_tracedlinkendcreationdata_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLinkEndCreationData.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedlinkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLinkEndDestructionData)


def test_umltrace_uml_tracedlinkenddestructiondata_constructor_exists():
    assert callable(umlTrace_uml_TracedLinkEndDestructionData.__init__)


def test_umltrace_uml_tracedlinkenddestructiondata_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtemplatesignature_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTemplateSignature)


def test_umltrace_uml_tracedtemplatesignature_constructor_exists():
    assert callable(umlTrace_uml_TracedTemplateSignature.__init__)


def test_umltrace_uml_tracedtemplatesignature_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstateinvariant_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStateInvariant)


def test_umltrace_uml_tracedstateinvariant_constructor_exists():
    assert callable(umlTrace_uml_TracedStateInvariant.__init__)


def test_umltrace_uml_tracedstateinvariant_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtrigger_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTrigger)


def test_umltrace_uml_tracedtrigger_constructor_exists():
    assert callable(umlTrace_uml_TracedTrigger.__init__)


def test_umltrace_uml_tracedtrigger_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTrigger.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedslot_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedSlot)


def test_umltrace_uml_tracedslot_constructor_exists():
    assert callable(umlTrace_uml_TracedSlot.__init__)


def test_umltrace_uml_tracedslot_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedSlot.__init__)
    params = list(sig.parameters.keys())



def test_tracedclass_is_not_abstract():
    assert not inspect.isabstract(TracedClass)


def test_tracedclass_constructor_exists():
    assert callable(TracedClass.__init__)


def test_tracedclass_constructor_args():
    sig = inspect.signature(TracedClass.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstereotype_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStereotype)


def test_umltrace_uml_tracedstereotype_constructor_exists():
    assert callable(umlTrace_uml_TracedStereotype.__init__)


def test_umltrace_uml_tracedstereotype_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStereotype.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcomponent_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedComponent)


def test_umltrace_uml_tracedcomponent_constructor_exists():
    assert callable(umlTrace_uml_TracedComponent.__init__)


def test_umltrace_uml_tracedcomponent_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedComponent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedbehavior_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedBehavior)


def test_umltrace_uml_tracedbehavior_constructor_exists():
    assert callable(umlTrace_uml_TracedBehavior.__init__)


def test_umltrace_uml_tracedbehavior_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedBehavior.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinteractionfragment_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInteractionFragment)


def test_uml_tracedinteractionfragment_constructor_exists():
    assert callable(uml_TracedInteractionFragment.__init__)


def test_uml_tracedinteractionfragment_constructor_args():
    sig = inspect.signature(uml_TracedInteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedbehavior_is_not_abstract():
    assert not inspect.isabstract(uml_TracedBehavior)


def test_uml_tracedbehavior_constructor_exists():
    assert callable(uml_TracedBehavior.__init__)


def test_uml_tracedbehavior_constructor_args():
    sig = inspect.signature(uml_TracedBehavior.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinteraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInteraction)


def test_umltrace_uml_tracedinteraction_constructor_exists():
    assert callable(umlTrace_uml_TracedInteraction.__init__)


def test_umltrace_uml_tracedinteraction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInteraction.__init__)
    params = list(sig.parameters.keys())



def test_tracedactivityedge_is_not_abstract():
    assert not inspect.isabstract(TracedActivityEdge)


def test_tracedactivityedge_constructor_exists():
    assert callable(TracedActivityEdge.__init__)


def test_tracedactivityedge_constructor_args():
    sig = inspect.signature(TracedActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcontrolflow_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedControlFlow)


def test_umltrace_uml_tracedcontrolflow_constructor_exists():
    assert callable(umlTrace_uml_TracedControlFlow.__init__)


def test_umltrace_uml_tracedcontrolflow_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedobjectflow_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedObjectFlow)


def test_umltrace_uml_tracedobjectflow_constructor_exists():
    assert callable(umlTrace_uml_TracedObjectFlow.__init__)


def test_umltrace_uml_tracedobjectflow_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_tracedstatemachine_is_not_abstract():
    assert not inspect.isabstract(TracedStateMachine)


def test_tracedstatemachine_constructor_exists():
    assert callable(TracedStateMachine.__init__)


def test_tracedstatemachine_constructor_args():
    sig = inspect.signature(TracedStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedprotocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedProtocolStateMachine)


def test_umltrace_uml_tracedprotocolstatemachine_constructor_exists():
    assert callable(umlTrace_uml_TracedProtocolStateMachine.__init__)


def test_umltrace_uml_tracedprotocolstatemachine_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddeployment_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDeployment)


def test_umltrace_uml_traceddeployment_constructor_exists():
    assert callable(umlTrace_uml_TracedDeployment.__init__)


def test_umltrace_uml_traceddeployment_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDeployment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedmessage_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedMessage)


def test_umltrace_uml_tracedmessage_constructor_exists():
    assert callable(umlTrace_uml_TracedMessage.__init__)


def test_umltrace_uml_tracedmessage_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedMessage.__init__)
    params = list(sig.parameters.keys())



def test_tracedbehavior_is_not_abstract():
    assert not inspect.isabstract(TracedBehavior)


def test_tracedbehavior_constructor_exists():
    assert callable(TracedBehavior.__init__)


def test_tracedbehavior_constructor_args():
    sig = inspect.signature(TracedBehavior.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedopaquebehavior_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedOpaqueBehavior)


def test_umltrace_uml_tracedopaquebehavior_constructor_exists():
    assert callable(umlTrace_uml_TracedOpaqueBehavior.__init__)


def test_umltrace_uml_tracedopaquebehavior_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedOpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedactivity_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActivity)


def test_umltrace_uml_tracedactivity_constructor_exists():
    assert callable(umlTrace_uml_TracedActivity.__init__)


def test_umltrace_uml_tracedactivity_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActivity.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstatemachine_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStateMachine)


def test_umltrace_uml_tracedstatemachine_constructor_exists():
    assert callable(umlTrace_uml_TracedStateMachine.__init__)


def test_umltrace_uml_tracedstatemachine_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_tracedactivitygroup_is_not_abstract():
    assert not inspect.isabstract(TracedActivityGroup)


def test_tracedactivitygroup_constructor_exists():
    assert callable(TracedActivityGroup.__init__)


def test_tracedactivitygroup_constructor_args():
    sig = inspect.signature(TracedActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinterruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInterruptibleActivityRegion)


def test_umltrace_uml_tracedinterruptibleactivityregion_constructor_exists():
    assert callable(umlTrace_uml_TracedInterruptibleActivityRegion.__init__)


def test_umltrace_uml_tracedinterruptibleactivityregion_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedactivitypartition_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActivityPartition)


def test_umltrace_uml_tracedactivitypartition_constructor_exists():
    assert callable(umlTrace_uml_TracedActivityPartition.__init__)


def test_umltrace_uml_tracedactivitypartition_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedrelationship_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRelationship)


def test_uml_tracedrelationship_constructor_exists():
    assert callable(uml_TracedRelationship.__init__)


def test_uml_tracedrelationship_constructor_args():
    sig = inspect.signature(uml_TracedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_tracedassociation_is_not_abstract():
    assert not inspect.isabstract(TracedAssociation)


def test_tracedassociation_constructor_exists():
    assert callable(TracedAssociation.__init__)


def test_tracedassociation_constructor_args():
    sig = inspect.signature(TracedAssociation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcommunicationpath_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCommunicationPath)


def test_umltrace_uml_tracedcommunicationpath_constructor_exists():
    assert callable(umlTrace_uml_TracedCommunicationPath.__init__)


def test_umltrace_uml_tracedcommunicationpath_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedextension_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExtension)


def test_umltrace_uml_tracedextension_constructor_exists():
    assert callable(umlTrace_uml_TracedExtension.__init__)


def test_umltrace_uml_tracedextension_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExtension.__init__)
    params = list(sig.parameters.keys())



def test_tracedstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(TracedStructuralFeatureAction)


def test_tracedstructuralfeatureaction_constructor_exists():
    assert callable(TracedStructuralFeatureAction.__init__)


def test_tracedstructuralfeatureaction_constructor_args():
    sig = inspect.signature(TracedStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreadstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReadStructuralFeatureAction)


def test_umltrace_uml_tracedreadstructuralfeatureaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReadStructuralFeatureAction.__init__)


def test_umltrace_uml_tracedreadstructuralfeatureaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedclearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedClearStructuralFeatureAction)


def test_umltrace_uml_tracedclearstructuralfeatureaction_constructor_exists():
    assert callable(umlTrace_uml_TracedClearStructuralFeatureAction.__init__)


def test_umltrace_uml_tracedclearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedwritestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedWriteStructuralFeatureAction)


def test_umltrace_uml_tracedwritestructuralfeatureaction_constructor_exists():
    assert callable(umlTrace_uml_TracedWriteStructuralFeatureAction.__init__)


def test_umltrace_uml_tracedwritestructuralfeatureaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedWriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedwritestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(TracedWriteStructuralFeatureAction)


def test_tracedwritestructuralfeatureaction_constructor_exists():
    assert callable(TracedWriteStructuralFeatureAction.__init__)


def test_tracedwritestructuralfeatureaction_constructor_args():
    sig = inspect.signature(TracedWriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedaddstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedAddStructuralFeatureValueAction)


def test_umltrace_uml_tracedaddstructuralfeaturevalueaction_constructor_exists():
    assert callable(umlTrace_uml_TracedAddStructuralFeatureValueAction.__init__)


def test_umltrace_uml_tracedaddstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedAddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedremovestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedRemoveStructuralFeatureValueAction)


def test_umltrace_uml_tracedremovestructuralfeaturevalueaction_constructor_exists():
    assert callable(umlTrace_uml_TracedRemoveStructuralFeatureValueAction.__init__)


def test_umltrace_uml_tracedremovestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedRemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedbehavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(TracedBehavioredClassifier)


def test_tracedbehavioredclassifier_constructor_exists():
    assert callable(TracedBehavioredClassifier.__init__)


def test_tracedbehavioredclassifier_constructor_args():
    sig = inspect.signature(TracedBehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedactor_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActor)


def test_umltrace_uml_tracedactor_constructor_exists():
    assert callable(umlTrace_uml_TracedActor.__init__)


def test_umltrace_uml_tracedactor_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActor.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedusecase_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedUseCase)


def test_umltrace_uml_tracedusecase_constructor_exists():
    assert callable(umlTrace_uml_TracedUseCase.__init__)


def test_umltrace_uml_tracedusecase_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedUseCase.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedsequencenode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedSequenceNode)


def test_umltrace_uml_tracedsequencenode_constructor_exists():
    assert callable(umlTrace_uml_TracedSequenceNode.__init__)


def test_umltrace_uml_tracedsequencenode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedSequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedexceptionhandler_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExceptionHandler)


def test_umltrace_uml_tracedexceptionhandler_constructor_exists():
    assert callable(umlTrace_uml_TracedExceptionHandler.__init__)


def test_umltrace_uml_tracedexceptionhandler_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddeployedartifact_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDeployedArtifact)


def test_umltrace_uml_traceddeployedartifact_constructor_exists():
    assert callable(umlTrace_uml_TracedDeployedArtifact.__init__)


def test_umltrace_uml_traceddeployedartifact_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddeployedartifact_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDeployedArtifact)


def test_uml_traceddeployedartifact_constructor_exists():
    assert callable(uml_TracedDeployedArtifact.__init__)


def test_uml_traceddeployedartifact_constructor_args():
    sig = inspect.signature(uml_TracedDeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedclassifier_is_not_abstract():
    assert not inspect.isabstract(uml_TracedClassifier)


def test_uml_tracedclassifier_constructor_exists():
    assert callable(uml_TracedClassifier.__init__)


def test_uml_tracedclassifier_constructor_args():
    sig = inspect.signature(uml_TracedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedassociation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedAssociation)


def test_umltrace_uml_tracedassociation_constructor_exists():
    assert callable(umlTrace_uml_TracedAssociation.__init__)


def test_umltrace_uml_tracedassociation_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedAssociation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedartifact_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedArtifact)


def test_umltrace_uml_tracedartifact_constructor_exists():
    assert callable(umlTrace_uml_TracedArtifact.__init__)


def test_umltrace_uml_tracedartifact_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_tracedartifact_is_not_abstract():
    assert not inspect.isabstract(TracedArtifact)


def test_tracedartifact_constructor_exists():
    assert callable(TracedArtifact.__init__)


def test_tracedartifact_constructor_args():
    sig = inspect.signature(TracedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddeploymentspecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDeploymentSpecification)


def test_umltrace_uml_traceddeploymentspecification_constructor_exists():
    assert callable(umlTrace_uml_TracedDeploymentSpecification.__init__)


def test_umltrace_uml_traceddeploymentspecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDeploymentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActivityNode)


def test_uml_tracedactivitynode_constructor_exists():
    assert callable(uml_TracedActivityNode.__init__)


def test_uml_tracedactivitynode_constructor_args():
    sig = inspect.signature(uml_TracedActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedobjectnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedObjectNode)


def test_uml_tracedobjectnode_constructor_exists():
    assert callable(uml_TracedObjectNode.__init__)


def test_uml_tracedobjectnode_constructor_args():
    sig = inspect.signature(uml_TracedObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedpin_is_not_abstract():
    assert not inspect.isabstract(TracedPin)


def test_tracedpin_constructor_exists():
    assert callable(TracedPin.__init__)


def test_tracedpin_constructor_args():
    sig = inspect.signature(TracedPin.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedoutputpin_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedOutputPin)


def test_umltrace_uml_tracedoutputpin_constructor_exists():
    assert callable(umlTrace_uml_TracedOutputPin.__init__)


def test_umltrace_uml_tracedoutputpin_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedOutputPin.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinputpin_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInputPin)


def test_umltrace_uml_tracedinputpin_constructor_exists():
    assert callable(umlTrace_uml_TracedInputPin.__init__)


def test_umltrace_uml_tracedinputpin_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInputPin.__init__)
    params = list(sig.parameters.keys())



def test_tracedinputpin_is_not_abstract():
    assert not inspect.isabstract(TracedInputPin)


def test_tracedinputpin_constructor_exists():
    assert callable(TracedInputPin.__init__)


def test_tracedinputpin_constructor_args():
    sig = inspect.signature(TracedInputPin.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedactioninputpin_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActionInputPin)


def test_umltrace_uml_tracedactioninputpin_constructor_exists():
    assert callable(umlTrace_uml_TracedActionInputPin.__init__)


def test_umltrace_uml_tracedactioninputpin_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedvaluepin_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedValuePin)


def test_umltrace_uml_tracedvaluepin_constructor_exists():
    assert callable(umlTrace_uml_TracedValuePin.__init__)


def test_umltrace_uml_tracedvaluepin_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedValuePin.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcollaborationuse_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCollaborationUse)


def test_umltrace_uml_tracedcollaborationuse_constructor_exists():
    assert callable(umlTrace_uml_TracedCollaborationUse.__init__)


def test_umltrace_uml_tracedcollaborationuse_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCollaborationUse.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddeploymenttarget_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDeploymentTarget)


def test_umltrace_uml_traceddeploymenttarget_constructor_exists():
    assert callable(umlTrace_uml_TracedDeploymentTarget.__init__)


def test_umltrace_uml_traceddeploymenttarget_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedmultiplicityelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedMultiplicityElement)


def test_umltrace_uml_tracedmultiplicityelement_constructor_exists():
    assert callable(umlTrace_uml_TracedMultiplicityElement.__init__)


def test_umltrace_uml_tracedmultiplicityelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedMultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtypedelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTypedElement)


def test_umltrace_uml_tracedtypedelement_constructor_exists():
    assert callable(umlTrace_uml_TracedTypedElement.__init__)


def test_umltrace_uml_tracedtypedelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedmultiplicityelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedMultiplicityElement)


def test_uml_tracedmultiplicityelement_constructor_exists():
    assert callable(uml_TracedMultiplicityElement.__init__)


def test_uml_tracedmultiplicityelement_constructor_args():
    sig = inspect.signature(uml_TracedMultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedpin_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedPin)


def test_umltrace_uml_tracedpin_constructor_exists():
    assert callable(umlTrace_uml_TracedPin.__init__)


def test_umltrace_uml_tracedpin_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedPin.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtypedelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTypedElement)


def test_uml_tracedtypedelement_constructor_exists():
    assert callable(uml_TracedTypedElement.__init__)


def test_uml_tracedtypedelement_constructor_args():
    sig = inspect.signature(uml_TracedTypedElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedconnectableelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedConnectableElement)


def test_umltrace_uml_tracedconnectableelement_constructor_exists():
    assert callable(umlTrace_uml_TracedConnectableElement.__init__)


def test_umltrace_uml_tracedconnectableelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedobjectnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedObjectNode)


def test_umltrace_uml_tracedobjectnode_constructor_exists():
    assert callable(umlTrace_uml_TracedObjectNode.__init__)


def test_umltrace_uml_tracedobjectnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedfeature_is_not_abstract():
    assert not inspect.isabstract(uml_TracedFeature)


def test_uml_tracedfeature_constructor_exists():
    assert callable(uml_TracedFeature.__init__)


def test_uml_tracedfeature_constructor_args():
    sig = inspect.signature(uml_TracedFeature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstructuralfeature_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStructuralFeature)


def test_umltrace_uml_tracedstructuralfeature_constructor_exists():
    assert callable(umlTrace_uml_TracedStructuralFeature.__init__)


def test_umltrace_uml_tracedstructuralfeature_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_tracedvaluespecification_is_not_abstract():
    assert not inspect.isabstract(TracedValueSpecification)


def test_tracedvaluespecification_constructor_exists():
    assert callable(TracedValueSpecification.__init__)


def test_tracedvaluespecification_constructor_args():
    sig = inspect.signature(TracedValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedopaqueexpression_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedOpaqueExpression)


def test_umltrace_uml_tracedopaqueexpression_constructor_exists():
    assert callable(umlTrace_uml_TracedOpaqueExpression.__init__)


def test_umltrace_uml_tracedopaqueexpression_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedOpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtimeexpression_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTimeExpression)


def test_umltrace_uml_tracedtimeexpression_constructor_exists():
    assert callable(umlTrace_uml_TracedTimeExpression.__init__)


def test_umltrace_uml_tracedtimeexpression_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinterval_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInterval)


def test_umltrace_uml_tracedinterval_constructor_exists():
    assert callable(umlTrace_uml_TracedInterval.__init__)


def test_umltrace_uml_tracedinterval_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInterval.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedexpression_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExpression)


def test_umltrace_uml_tracedexpression_constructor_exists():
    assert callable(umlTrace_uml_TracedExpression.__init__)


def test_umltrace_uml_tracedexpression_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExpression.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinstancevalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInstanceValue)


def test_umltrace_uml_tracedinstancevalue_constructor_exists():
    assert callable(umlTrace_uml_TracedInstanceValue.__init__)


def test_umltrace_uml_tracedinstancevalue_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedduration_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDuration)


def test_umltrace_uml_tracedduration_constructor_exists():
    assert callable(umlTrace_uml_TracedDuration.__init__)


def test_umltrace_uml_tracedduration_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDuration.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedliteralspecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLiteralSpecification)


def test_umltrace_uml_tracedliteralspecification_constructor_exists():
    assert callable(umlTrace_uml_TracedLiteralSpecification.__init__)


def test_umltrace_uml_tracedliteralspecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_tracedliteralspecification_is_not_abstract():
    assert not inspect.isabstract(TracedLiteralSpecification)


def test_tracedliteralspecification_constructor_exists():
    assert callable(TracedLiteralSpecification.__init__)


def test_tracedliteralspecification_constructor_args():
    sig = inspect.signature(TracedLiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedliteralunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLiteralUnlimitedNatural)


def test_umltrace_uml_tracedliteralunlimitednatural_constructor_exists():
    assert callable(umlTrace_uml_TracedLiteralUnlimitedNatural.__init__)


def test_umltrace_uml_tracedliteralunlimitednatural_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedliteralnull_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLiteralNull)


def test_umltrace_uml_tracedliteralnull_constructor_exists():
    assert callable(umlTrace_uml_TracedLiteralNull.__init__)


def test_umltrace_uml_tracedliteralnull_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedliteralreal_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLiteralReal)


def test_umltrace_uml_tracedliteralreal_constructor_exists():
    assert callable(umlTrace_uml_TracedLiteralReal.__init__)


def test_umltrace_uml_tracedliteralreal_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLiteralReal.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedliteralboolean_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLiteralBoolean)


def test_umltrace_uml_tracedliteralboolean_constructor_exists():
    assert callable(umlTrace_uml_TracedLiteralBoolean.__init__)


def test_umltrace_uml_tracedliteralboolean_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedliteralinteger_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLiteralInteger)


def test_umltrace_uml_tracedliteralinteger_constructor_exists():
    assert callable(umlTrace_uml_TracedLiteralInteger.__init__)


def test_umltrace_uml_tracedliteralinteger_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedliteralstring_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLiteralString)


def test_umltrace_uml_tracedliteralstring_constructor_exists():
    assert callable(umlTrace_uml_TracedLiteralString.__init__)


def test_umltrace_uml_tracedliteralstring_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLiteralString.__init__)
    params = list(sig.parameters.keys())



def test_tracedvariableaction_is_not_abstract():
    assert not inspect.isabstract(TracedVariableAction)


def test_tracedvariableaction_constructor_exists():
    assert callable(TracedVariableAction.__init__)


def test_tracedvariableaction_constructor_args():
    sig = inspect.signature(TracedVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreadvariableaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReadVariableAction)


def test_umltrace_uml_tracedreadvariableaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReadVariableAction.__init__)


def test_umltrace_uml_tracedreadvariableaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedwritevariableaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedWriteVariableAction)


def test_umltrace_uml_tracedwritevariableaction_constructor_exists():
    assert callable(umlTrace_uml_TracedWriteVariableAction.__init__)


def test_umltrace_uml_tracedwritevariableaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedWriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedclearvariableaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedClearVariableAction)


def test_umltrace_uml_tracedclearvariableaction_constructor_exists():
    assert callable(umlTrace_uml_TracedClearVariableAction.__init__)


def test_umltrace_uml_tracedclearvariableaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtimeconstraint_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTimeConstraint)


def test_umltrace_uml_tracedtimeconstraint_constructor_exists():
    assert callable(umlTrace_uml_TracedTimeConstraint.__init__)


def test_umltrace_uml_tracedtimeconstraint_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTimeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcontinuation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedContinuation)


def test_umltrace_uml_tracedcontinuation_constructor_exists():
    assert callable(umlTrace_uml_TracedContinuation.__init__)


def test_umltrace_uml_tracedcontinuation_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedContinuation.__init__)
    params = list(sig.parameters.keys())



def test_tracedcombinedfragment_is_not_abstract():
    assert not inspect.isabstract(TracedCombinedFragment)


def test_tracedcombinedfragment_constructor_exists():
    assert callable(TracedCombinedFragment.__init__)


def test_tracedcombinedfragment_constructor_args():
    sig = inspect.signature(TracedCombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedconsiderignorefragment_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedConsiderIgnoreFragment)


def test_umltrace_uml_tracedconsiderignorefragment_constructor_exists():
    assert callable(umlTrace_uml_TracedConsiderIgnoreFragment.__init__)


def test_umltrace_uml_tracedconsiderignorefragment_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedConsiderIgnoreFragment.__init__)
    params = list(sig.parameters.keys())



def test_tracednode_is_not_abstract():
    assert not inspect.isabstract(TracedNode)


def test_tracednode_constructor_exists():
    assert callable(TracedNode.__init__)


def test_tracednode_constructor_args():
    sig = inspect.signature(TracedNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddevice_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDevice)


def test_umltrace_uml_traceddevice_constructor_exists():
    assert callable(umlTrace_uml_TracedDevice.__init__)


def test_umltrace_uml_traceddevice_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDevice.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedexecutionenvironment_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExecutionEnvironment)


def test_umltrace_uml_tracedexecutionenvironment_constructor_exists():
    assert callable(umlTrace_uml_TracedExecutionEnvironment.__init__)


def test_umltrace_uml_tracedexecutionenvironment_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtype_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedType)


def test_umltrace_uml_tracedtype_constructor_exists():
    assert callable(umlTrace_uml_TracedType.__init__)


def test_umltrace_uml_tracedtype_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedType.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtype_is_not_abstract():
    assert not inspect.isabstract(uml_TracedType)


def test_uml_tracedtype_constructor_exists():
    assert callable(uml_TracedType.__init__)


def test_uml_tracedtype_constructor_args():
    sig = inspect.signature(uml_TracedType.__init__)
    params = list(sig.parameters.keys())



def test_tracedclassifier_is_not_abstract():
    assert not inspect.isabstract(TracedClassifier)


def test_tracedclassifier_constructor_exists():
    assert callable(TracedClassifier.__init__)


def test_tracedclassifier_constructor_args():
    sig = inspect.signature(TracedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddatatype_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDataType)


def test_umltrace_uml_traceddatatype_constructor_exists():
    assert callable(umlTrace_uml_TracedDataType.__init__)


def test_umltrace_uml_traceddatatype_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDataType.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinformationitem_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInformationItem)


def test_umltrace_uml_tracedinformationitem_constructor_exists():
    assert callable(umlTrace_uml_TracedInformationItem.__init__)


def test_umltrace_uml_tracedinformationitem_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInformationItem.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinterface_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInterface)


def test_umltrace_uml_tracedinterface_constructor_exists():
    assert callable(umlTrace_uml_TracedInterface.__init__)


def test_umltrace_uml_tracedinterface_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInterface.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedbehavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedBehavioredClassifier)


def test_umltrace_uml_tracedbehavioredclassifier_constructor_exists():
    assert callable(umlTrace_uml_TracedBehavioredClassifier.__init__)


def test_umltrace_uml_tracedbehavioredclassifier_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedBehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstructuredclassifier_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStructuredClassifier)


def test_umltrace_uml_tracedstructuredclassifier_constructor_exists():
    assert callable(umlTrace_uml_TracedStructuredClassifier.__init__)


def test_umltrace_uml_tracedstructuredclassifier_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_tracedstructuredclassifier_is_not_abstract():
    assert not inspect.isabstract(TracedStructuredClassifier)


def test_tracedstructuredclassifier_constructor_exists():
    assert callable(TracedStructuredClassifier.__init__)


def test_tracedstructuredclassifier_constructor_args():
    sig = inspect.signature(TracedStructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedencapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedEncapsulatedClassifier)


def test_umltrace_uml_tracedencapsulatedclassifier_constructor_exists():
    assert callable(umlTrace_uml_TracedEncapsulatedClassifier.__init__)


def test_umltrace_uml_tracedencapsulatedclassifier_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedEncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedbehavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml_TracedBehavioredClassifier)


def test_uml_tracedbehavioredclassifier_constructor_exists():
    assert callable(uml_TracedBehavioredClassifier.__init__)


def test_uml_tracedbehavioredclassifier_constructor_args():
    sig = inspect.signature(uml_TracedBehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcollaboration_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCollaboration)


def test_umltrace_uml_tracedcollaboration_constructor_exists():
    assert callable(umlTrace_uml_TracedCollaboration.__init__)


def test_umltrace_uml_tracedcollaboration_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCollaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedencapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(uml_TracedEncapsulatedClassifier)


def test_uml_tracedencapsulatedclassifier_constructor_exists():
    assert callable(uml_TracedEncapsulatedClassifier.__init__)


def test_uml_tracedencapsulatedclassifier_constructor_args():
    sig = inspect.signature(uml_TracedEncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedclass_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedClass)


def test_umltrace_uml_tracedclass_constructor_exists():
    assert callable(umlTrace_uml_TracedClass.__init__)


def test_umltrace_uml_tracedclass_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedClass.__init__)
    params = list(sig.parameters.keys())



def test_tracedcallaction_is_not_abstract():
    assert not inspect.isabstract(TracedCallAction)


def test_tracedcallaction_constructor_exists():
    assert callable(TracedCallAction.__init__)


def test_tracedcallaction_constructor_args():
    sig = inspect.signature(TracedCallAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstartobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStartObjectBehaviorAction)


def test_umltrace_uml_tracedstartobjectbehavioraction_constructor_exists():
    assert callable(umlTrace_uml_TracedStartObjectBehaviorAction.__init__)


def test_umltrace_uml_tracedstartobjectbehavioraction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcalloperationaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCallOperationAction)


def test_umltrace_uml_tracedcalloperationaction_constructor_exists():
    assert callable(umlTrace_uml_TracedCallOperationAction.__init__)


def test_umltrace_uml_tracedcalloperationaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcallbehavioraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCallBehaviorAction)


def test_umltrace_uml_tracedcallbehavioraction_constructor_exists():
    assert callable(umlTrace_uml_TracedCallBehaviorAction.__init__)


def test_umltrace_uml_tracedcallbehavioraction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedrelationship_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedRelationship)


def test_umltrace_uml_tracedrelationship_constructor_exists():
    assert callable(umlTrace_uml_TracedRelationship.__init__)


def test_umltrace_uml_tracedrelationship_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_tracedrelationship_is_not_abstract():
    assert not inspect.isabstract(TracedRelationship)


def test_tracedrelationship_constructor_exists():
    assert callable(TracedRelationship.__init__)


def test_tracedrelationship_constructor_args():
    sig = inspect.signature(TracedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddirectedrelationship_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDirectedRelationship)


def test_umltrace_uml_traceddirectedrelationship_constructor_exists():
    assert callable(umlTrace_uml_TracedDirectedRelationship.__init__)


def test_umltrace_uml_traceddirectedrelationship_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_traceddirectedrelationship_is_not_abstract():
    assert not inspect.isabstract(TracedDirectedRelationship)


def test_traceddirectedrelationship_constructor_exists():
    assert callable(TracedDirectedRelationship.__init__)


def test_traceddirectedrelationship_constructor_args():
    sig = inspect.signature(TracedDirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedgeneralization_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedGeneralization)


def test_umltrace_uml_tracedgeneralization_constructor_exists():
    assert callable(umlTrace_uml_TracedGeneralization.__init__)


def test_umltrace_uml_tracedgeneralization_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedGeneralization.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedelementimport_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedElementImport)


def test_umltrace_uml_tracedelementimport_constructor_exists():
    assert callable(umlTrace_uml_TracedElementImport.__init__)


def test_umltrace_uml_tracedelementimport_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedElementImport.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedprofileapplication_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedProfileApplication)


def test_umltrace_uml_tracedprofileapplication_constructor_exists():
    assert callable(umlTrace_uml_TracedProfileApplication.__init__)


def test_umltrace_uml_tracedprofileapplication_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedProfileApplication.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedpackagemerge_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedPackageMerge)


def test_umltrace_uml_tracedpackagemerge_constructor_exists():
    assert callable(umlTrace_uml_TracedPackageMerge.__init__)


def test_umltrace_uml_tracedpackagemerge_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedPackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtemplatebinding_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTemplateBinding)


def test_umltrace_uml_tracedtemplatebinding_constructor_exists():
    assert callable(umlTrace_uml_TracedTemplateBinding.__init__)


def test_umltrace_uml_tracedtemplatebinding_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedpackageimport_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedPackageImport)


def test_umltrace_uml_tracedpackageimport_constructor_exists():
    assert callable(umlTrace_uml_TracedPackageImport.__init__)


def test_umltrace_uml_tracedpackageimport_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedPackageImport.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedprotocolconformance_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedProtocolConformance)


def test_umltrace_uml_tracedprotocolconformance_constructor_exists():
    assert callable(umlTrace_uml_TracedProtocolConformance.__init__)


def test_umltrace_uml_tracedprotocolconformance_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_tracedinvocationaction_is_not_abstract():
    assert not inspect.isabstract(TracedInvocationAction)


def test_tracedinvocationaction_constructor_exists():
    assert callable(TracedInvocationAction.__init__)


def test_tracedinvocationaction_constructor_args():
    sig = inspect.signature(TracedInvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcallaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCallAction)


def test_umltrace_uml_tracedcallaction_constructor_exists():
    assert callable(umlTrace_uml_TracedCallAction.__init__)


def test_umltrace_uml_tracedcallaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCallAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedbroadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedBroadcastSignalAction)


def test_umltrace_uml_tracedbroadcastsignalaction_constructor_exists():
    assert callable(umlTrace_uml_TracedBroadcastSignalAction.__init__)


def test_umltrace_uml_tracedbroadcastsignalaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedBroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedsendsignalaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedSendSignalAction)


def test_umltrace_uml_tracedsendsignalaction_constructor_exists():
    assert callable(umlTrace_uml_TracedSendSignalAction.__init__)


def test_umltrace_uml_tracedsendsignalaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedSendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedsendobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedSendObjectAction)


def test_umltrace_uml_tracedsendobjectaction_constructor_exists():
    assert callable(umlTrace_uml_TracedSendObjectAction.__init__)


def test_umltrace_uml_tracedsendobjectaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedSendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedredefinableelement_is_not_abstract():
    assert not inspect.isabstract(TracedRedefinableElement)


def test_tracedredefinableelement_constructor_exists():
    assert callable(TracedRedefinableElement.__init__)


def test_tracedredefinableelement_constructor_args():
    sig = inspect.signature(TracedRedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedextensionpoint_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExtensionPoint)


def test_umltrace_uml_tracedextensionpoint_constructor_exists():
    assert callable(umlTrace_uml_TracedExtensionPoint.__init__)


def test_umltrace_uml_tracedextensionpoint_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedactivityedge_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActivityEdge)


def test_umltrace_uml_tracedactivityedge_constructor_exists():
    assert callable(umlTrace_uml_TracedActivityEdge.__init__)


def test_umltrace_uml_tracedactivityedge_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedfeature_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedFeature)


def test_umltrace_uml_tracedfeature_constructor_exists():
    assert callable(umlTrace_uml_TracedFeature.__init__)


def test_umltrace_uml_tracedfeature_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedFeature.__init__)
    params = list(sig.parameters.keys())



def test_tracedfeature_is_not_abstract():
    assert not inspect.isabstract(TracedFeature)


def test_tracedfeature_constructor_exists():
    assert callable(TracedFeature.__init__)


def test_tracedfeature_constructor_args():
    sig = inspect.signature(TracedFeature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedconnector_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedConnector)


def test_umltrace_uml_tracedconnector_constructor_exists():
    assert callable(umlTrace_uml_TracedConnector.__init__)


def test_umltrace_uml_tracedconnector_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedConnector.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtemplateableelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTemplateableElement)


def test_umltrace_uml_tracedtemplateableelement_constructor_exists():
    assert callable(umlTrace_uml_TracedTemplateableElement.__init__)


def test_umltrace_uml_tracedtemplateableelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtemplateableelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTemplateableElement)


def test_uml_tracedtemplateableelement_constructor_exists():
    assert callable(uml_TracedTemplateableElement.__init__)


def test_uml_tracedtemplateableelement_constructor_args():
    sig = inspect.signature(uml_TracedTemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedoperation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedOperation)


def test_umltrace_uml_tracedoperation_constructor_exists():
    assert callable(umlTrace_uml_TracedOperation.__init__)


def test_umltrace_uml_tracedoperation_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedOperation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstringexpression_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStringExpression)


def test_umltrace_uml_tracedstringexpression_constructor_exists():
    assert callable(umlTrace_uml_TracedStringExpression.__init__)


def test_umltrace_uml_tracedstringexpression_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStringExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedpackageableelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedPackageableElement)


def test_uml_tracedpackageableelement_constructor_exists():
    assert callable(uml_TracedPackageableElement.__init__)


def test_uml_tracedpackageableelement_constructor_args():
    sig = inspect.signature(uml_TracedPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedvaluespecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedValueSpecification)


def test_umltrace_uml_tracedvaluespecification_constructor_exists():
    assert callable(umlTrace_uml_TracedValueSpecification.__init__)


def test_umltrace_uml_tracedvaluespecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedmessageend_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedMessageEnd)


def test_umltrace_uml_tracedmessageend_constructor_exists():
    assert callable(umlTrace_uml_TracedMessageEnd.__init__)


def test_umltrace_uml_tracedmessageend_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedMessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddeploymenttarget_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDeploymentTarget)


def test_uml_traceddeploymenttarget_constructor_exists():
    assert callable(uml_TracedDeploymentTarget.__init__)


def test_uml_traceddeploymenttarget_constructor_args():
    sig = inspect.signature(uml_TracedDeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinstancespecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInstanceSpecification)


def test_umltrace_uml_tracedinstancespecification_constructor_exists():
    assert callable(umlTrace_uml_TracedInstanceSpecification.__init__)


def test_umltrace_uml_tracedinstancespecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconnectableelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConnectableElement)


def test_uml_tracedconnectableelement_constructor_exists():
    assert callable(uml_TracedConnectableElement.__init__)


def test_uml_tracedconnectableelement_constructor_args():
    sig = inspect.signature(uml_TracedConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedparameter_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedParameter)


def test_umltrace_uml_tracedparameter_constructor_exists():
    assert callable(umlTrace_uml_TracedParameter.__init__)


def test_umltrace_uml_tracedparameter_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedParameter.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedvariable_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedVariable)


def test_umltrace_uml_tracedvariable_constructor_exists():
    assert callable(umlTrace_uml_TracedVariable.__init__)


def test_umltrace_uml_tracedvariable_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedVariable.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstructuralfeature_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStructuralFeature)


def test_uml_tracedstructuralfeature_constructor_exists():
    assert callable(uml_TracedStructuralFeature.__init__)


def test_uml_tracedstructuralfeature_constructor_args():
    sig = inspect.signature(uml_TracedStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedproperty_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedProperty)


def test_umltrace_uml_tracedproperty_constructor_exists():
    assert callable(umlTrace_uml_TracedProperty.__init__)


def test_umltrace_uml_tracedproperty_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedProperty.__init__)
    params = list(sig.parameters.keys())



def test_tracedproperty_is_not_abstract():
    assert not inspect.isabstract(TracedProperty)


def test_tracedproperty_constructor_exists():
    assert callable(TracedProperty.__init__)


def test_tracedproperty_constructor_args():
    sig = inspect.signature(TracedProperty.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedextensionend_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExtensionEnd)


def test_umltrace_uml_tracedextensionend_constructor_exists():
    assert callable(umlTrace_uml_TracedExtensionEnd.__init__)


def test_umltrace_uml_tracedextensionend_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedport_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedPort)


def test_umltrace_uml_tracedport_constructor_exists():
    assert callable(umlTrace_uml_TracedPort.__init__)


def test_umltrace_uml_tracedport_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedPort.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddirectedrelationship_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDirectedRelationship)


def test_uml_traceddirectedrelationship_constructor_exists():
    assert callable(uml_TracedDirectedRelationship.__init__)


def test_uml_traceddirectedrelationship_constructor_args():
    sig = inspect.signature(uml_TracedDirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinformationflow_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInformationFlow)


def test_umltrace_uml_tracedinformationflow_constructor_exists():
    assert callable(umlTrace_uml_TracedInformationFlow.__init__)


def test_umltrace_uml_tracedinformationflow_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddependency_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDependency)


def test_umltrace_uml_traceddependency_constructor_exists():
    assert callable(umlTrace_uml_TracedDependency.__init__)


def test_umltrace_uml_traceddependency_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDependency.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedEvent)


def test_umltrace_uml_tracedevent_constructor_exists():
    assert callable(umlTrace_uml_TracedEvent.__init__)


def test_umltrace_uml_tracedevent_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedEvent.__init__)
    params = list(sig.parameters.keys())



def test_tracedevent_is_not_abstract():
    assert not inspect.isabstract(TracedEvent)


def test_tracedevent_constructor_exists():
    assert callable(TracedEvent.__init__)


def test_tracedevent_constructor_args():
    sig = inspect.signature(TracedEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedmessageevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedMessageEvent)


def test_umltrace_uml_tracedmessageevent_constructor_exists():
    assert callable(umlTrace_uml_TracedMessageEvent.__init__)


def test_umltrace_uml_tracedmessageevent_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedMessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtimeevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTimeEvent)


def test_umltrace_uml_tracedtimeevent_constructor_exists():
    assert callable(umlTrace_uml_TracedTimeEvent.__init__)


def test_umltrace_uml_tracedtimeevent_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedchangeevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedChangeEvent)


def test_umltrace_uml_tracedchangeevent_constructor_exists():
    assert callable(umlTrace_uml_TracedChangeEvent.__init__)


def test_umltrace_uml_tracedchangeevent_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedgeneralizationset_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedGeneralizationSet)


def test_umltrace_uml_tracedgeneralizationset_constructor_exists():
    assert callable(umlTrace_uml_TracedGeneralizationSet.__init__)


def test_umltrace_uml_tracedgeneralizationset_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedGeneralizationSet.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedsignal_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedSignal)


def test_umltrace_uml_tracedsignal_constructor_exists():
    assert callable(umlTrace_uml_TracedSignal.__init__)


def test_umltrace_uml_tracedsignal_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedSignal.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedloopnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLoopNode)


def test_umltrace_uml_tracedloopnode_constructor_exists():
    assert callable(umlTrace_uml_TracedLoopNode.__init__)


def test_umltrace_uml_tracedloopnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLoopNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinteractionuse_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInteractionUse)


def test_umltrace_uml_tracedinteractionuse_constructor_exists():
    assert callable(umlTrace_uml_TracedInteractionUse.__init__)


def test_umltrace_uml_tracedinteractionuse_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedobservation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedObservation)


def test_umltrace_uml_tracedobservation_constructor_exists():
    assert callable(umlTrace_uml_TracedObservation.__init__)


def test_umltrace_uml_tracedobservation_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedObservation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedlifeline_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLifeline)


def test_umltrace_uml_tracedlifeline_constructor_exists():
    assert callable(umlTrace_uml_TracedLifeline.__init__)


def test_umltrace_uml_tracedlifeline_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLifeline.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedexpansionregion_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExpansionRegion)


def test_umltrace_uml_tracedexpansionregion_constructor_exists():
    assert callable(umlTrace_uml_TracedExpansionRegion.__init__)


def test_umltrace_uml_tracedexpansionregion_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_tracedfinalnode_is_not_abstract():
    assert not inspect.isabstract(TracedFinalNode)


def test_tracedfinalnode_constructor_exists():
    assert callable(TracedFinalNode.__init__)


def test_tracedfinalnode_constructor_args():
    sig = inspect.signature(TracedFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedactivityfinalnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActivityFinalNode)


def test_umltrace_uml_tracedactivityfinalnode_constructor_exists():
    assert callable(umlTrace_uml_TracedActivityFinalNode.__init__)


def test_umltrace_uml_tracedactivityfinalnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedflowfinalnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedFlowFinalNode)


def test_umltrace_uml_tracedflowfinalnode_constructor_exists():
    assert callable(umlTrace_uml_TracedFlowFinalNode.__init__)


def test_umltrace_uml_tracedflowfinalnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedFlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedcontrolnode_is_not_abstract():
    assert not inspect.isabstract(TracedControlNode)


def test_tracedcontrolnode_constructor_exists():
    assert callable(TracedControlNode.__init__)


def test_tracedcontrolnode_constructor_args():
    sig = inspect.signature(TracedControlNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedjoinnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedJoinNode)


def test_umltrace_uml_tracedjoinnode_constructor_exists():
    assert callable(umlTrace_uml_TracedJoinNode.__init__)


def test_umltrace_uml_tracedjoinnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedJoinNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedmergenode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedMergeNode)


def test_umltrace_uml_tracedmergenode_constructor_exists():
    assert callable(umlTrace_uml_TracedMergeNode.__init__)


def test_umltrace_uml_tracedmergenode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedMergeNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddecisionnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDecisionNode)


def test_umltrace_uml_traceddecisionnode_constructor_exists():
    assert callable(umlTrace_uml_TracedDecisionNode.__init__)


def test_umltrace_uml_traceddecisionnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedfinalnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedFinalNode)


def test_umltrace_uml_tracedfinalnode_constructor_exists():
    assert callable(umlTrace_uml_TracedFinalNode.__init__)


def test_umltrace_uml_tracedfinalnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedforknode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedForkNode)


def test_umltrace_uml_tracedforknode_constructor_exists():
    assert callable(umlTrace_uml_TracedForkNode.__init__)


def test_umltrace_uml_tracedforknode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedForkNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinitialnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInitialNode)


def test_umltrace_uml_tracedinitialnode_constructor_exists():
    assert callable(umlTrace_uml_TracedInitialNode.__init__)


def test_umltrace_uml_tracedinitialnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInitialNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedaction_is_not_abstract():
    assert not inspect.isabstract(TracedAction)


def test_tracedaction_constructor_exists():
    assert callable(TracedAction.__init__)


def test_tracedaction_constructor_args():
    sig = inspect.signature(TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreplyaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReplyAction)


def test_umltrace_uml_tracedreplyaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReplyAction.__init__)


def test_umltrace_uml_tracedreplyaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreadextentaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReadExtentAction)


def test_umltrace_uml_tracedreadextentaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReadExtentAction.__init__)


def test_umltrace_uml_tracedreadextentaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedaccepteventaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedAcceptEventAction)


def test_umltrace_uml_tracedaccepteventaction_constructor_exists():
    assert callable(umlTrace_uml_TracedAcceptEventAction.__init__)


def test_umltrace_uml_tracedaccepteventaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedAcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinvocationaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInvocationAction)


def test_umltrace_uml_tracedinvocationaction_constructor_exists():
    assert callable(umlTrace_uml_TracedInvocationAction.__init__)


def test_umltrace_uml_tracedinvocationaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedraiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedRaiseExceptionAction)


def test_umltrace_uml_tracedraiseexceptionaction_constructor_exists():
    assert callable(umlTrace_uml_TracedRaiseExceptionAction.__init__)


def test_umltrace_uml_tracedraiseexceptionaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedRaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedvaluespecificationaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedValueSpecificationAction)


def test_umltrace_uml_tracedvaluespecificationaction_constructor_exists():
    assert callable(umlTrace_uml_TracedValueSpecificationAction.__init__)


def test_umltrace_uml_tracedvaluespecificationaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedclearassociationaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedClearAssociationAction)


def test_umltrace_uml_tracedclearassociationaction_constructor_exists():
    assert callable(umlTrace_uml_TracedClearAssociationAction.__init__)


def test_umltrace_uml_tracedclearassociationaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedopaqueaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedOpaqueAction)


def test_umltrace_uml_tracedopaqueaction_constructor_exists():
    assert callable(umlTrace_uml_TracedOpaqueAction.__init__)


def test_umltrace_uml_tracedopaqueaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedOpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcreateobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCreateObjectAction)


def test_umltrace_uml_tracedcreateobjectaction_constructor_exists():
    assert callable(umlTrace_uml_TracedCreateObjectAction.__init__)


def test_umltrace_uml_tracedcreateobjectaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReclassifyObjectAction)


def test_umltrace_uml_tracedreclassifyobjectaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReclassifyObjectAction.__init__)


def test_umltrace_uml_tracedreclassifyobjectaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstartclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStartClassifierBehaviorAction)


def test_umltrace_uml_tracedstartclassifierbehavioraction_constructor_exists():
    assert callable(umlTrace_uml_TracedStartClassifierBehaviorAction.__init__)


def test_umltrace_uml_tracedstartclassifierbehavioraction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedvariableaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedVariableAction)


def test_umltrace_uml_tracedvariableaction_constructor_exists():
    assert callable(umlTrace_uml_TracedVariableAction.__init__)


def test_umltrace_uml_tracedvariableaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreadisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReadIsClassifiedObjectAction)


def test_umltrace_uml_tracedreadisclassifiedobjectaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReadIsClassifiedObjectAction.__init__)


def test_umltrace_uml_tracedreadisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtestidentityaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTestIdentityAction)


def test_umltrace_uml_tracedtestidentityaction_constructor_exists():
    assert callable(umlTrace_uml_TracedTestIdentityAction.__init__)


def test_umltrace_uml_tracedtestidentityaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedunmarshallaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedUnmarshallAction)


def test_umltrace_uml_tracedunmarshallaction_constructor_exists():
    assert callable(umlTrace_uml_TracedUnmarshallAction.__init__)


def test_umltrace_uml_tracedunmarshallaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedUnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreadselfaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReadSelfAction)


def test_umltrace_uml_tracedreadselfaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReadSelfAction.__init__)


def test_umltrace_uml_tracedreadselfaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreduceaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReduceAction)


def test_umltrace_uml_tracedreduceaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReduceAction.__init__)


def test_umltrace_uml_tracedreduceaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReduceAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStructuralFeatureAction)


def test_umltrace_uml_tracedstructuralfeatureaction_constructor_exists():
    assert callable(umlTrace_uml_TracedStructuralFeatureAction.__init__)


def test_umltrace_uml_tracedstructuralfeatureaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddestroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDestroyObjectAction)


def test_umltrace_uml_traceddestroyobjectaction_constructor_exists():
    assert callable(umlTrace_uml_TracedDestroyObjectAction.__init__)


def test_umltrace_uml_traceddestroyobjectaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreadlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReadLinkObjectEndQualifierAction)


def test_umltrace_uml_tracedreadlinkobjectendqualifieraction_constructor_exists():
    assert callable(umlTrace_uml_TracedReadLinkObjectEndQualifierAction.__init__)


def test_umltrace_uml_tracedreadlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreadlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReadLinkObjectEndAction)


def test_umltrace_uml_tracedreadlinkobjectendaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReadLinkObjectEndAction.__init__)


def test_umltrace_uml_tracedreadlinkobjectendaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedlinkaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLinkAction)


def test_umltrace_uml_tracedlinkaction_constructor_exists():
    assert callable(umlTrace_uml_TracedLinkAction.__init__)


def test_umltrace_uml_tracedlinkaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedlinkaction_is_not_abstract():
    assert not inspect.isabstract(TracedLinkAction)


def test_tracedlinkaction_constructor_exists():
    assert callable(TracedLinkAction.__init__)


def test_tracedlinkaction_constructor_args():
    sig = inspect.signature(TracedLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreadlinkaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReadLinkAction)


def test_umltrace_uml_tracedreadlinkaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReadLinkAction.__init__)


def test_umltrace_uml_tracedreadlinkaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedwritelinkaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedWriteLinkAction)


def test_umltrace_uml_tracedwritelinkaction_constructor_exists():
    assert callable(umlTrace_uml_TracedWriteLinkAction.__init__)


def test_umltrace_uml_tracedwritelinkaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedWriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedwritelinkaction_is_not_abstract():
    assert not inspect.isabstract(TracedWriteLinkAction)


def test_tracedwritelinkaction_constructor_exists():
    assert callable(TracedWriteLinkAction.__init__)


def test_tracedwritelinkaction_constructor_args():
    sig = inspect.signature(TracedWriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddestroylinkaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDestroyLinkAction)


def test_umltrace_uml_traceddestroylinkaction_constructor_exists():
    assert callable(umlTrace_uml_TracedDestroyLinkAction.__init__)


def test_umltrace_uml_traceddestroylinkaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcreatelinkaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCreateLinkAction)


def test_umltrace_uml_tracedcreatelinkaction_constructor_exists():
    assert callable(umlTrace_uml_TracedCreateLinkAction.__init__)


def test_umltrace_uml_tracedcreatelinkaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedcreatelinkaction_is_not_abstract():
    assert not inspect.isabstract(TracedCreateLinkAction)


def test_tracedcreatelinkaction_constructor_exists():
    assert callable(TracedCreateLinkAction.__init__)


def test_tracedcreatelinkaction_constructor_args():
    sig = inspect.signature(TracedCreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcreatelinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCreateLinkObjectAction)


def test_umltrace_uml_tracedcreatelinkobjectaction_constructor_exists():
    assert callable(umlTrace_uml_TracedCreateLinkObjectAction.__init__)


def test_umltrace_uml_tracedcreatelinkobjectaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracednamedelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedNamedElement)


def test_uml_tracednamedelement_constructor_exists():
    assert callable(uml_TracedNamedElement.__init__)


def test_uml_tracednamedelement_constructor_args():
    sig = inspect.signature(uml_TracedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedextend_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExtend)


def test_umltrace_uml_tracedextend_constructor_exists():
    assert callable(umlTrace_uml_TracedExtend.__init__)


def test_umltrace_uml_tracedextend_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExtend.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinclude_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInclude)


def test_umltrace_uml_tracedinclude_constructor_exists():
    assert callable(umlTrace_uml_TracedInclude.__init__)


def test_umltrace_uml_tracedinclude_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInclude.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedpackageableelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedPackageableElement)


def test_umltrace_uml_tracedpackageableelement_constructor_exists():
    assert callable(umlTrace_uml_TracedPackageableElement.__init__)


def test_umltrace_uml_tracedpackageableelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracednamespace_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedNamespace)


def test_umltrace_uml_tracednamespace_constructor_exists():
    assert callable(umlTrace_uml_TracedNamespace.__init__)


def test_umltrace_uml_tracednamespace_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedNamespace.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedredefinableelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedRedefinableElement)


def test_umltrace_uml_tracedredefinableelement_constructor_exists():
    assert callable(umlTrace_uml_TracedRedefinableElement.__init__)


def test_umltrace_uml_tracedredefinableelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedRedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_activitycontent_is_not_abstract():
    assert not inspect.isabstract(ActivityContent)


def test_activitycontent_constructor_exists():
    assert callable(ActivityContent.__init__)


def test_activitycontent_constructor_args():
    sig = inspect.signature(ActivityContent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedactivitygroup_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActivityGroup)


def test_umltrace_uml_tracedactivitygroup_constructor_exists():
    assert callable(umlTrace_uml_TracedActivityGroup.__init__)


def test_umltrace_uml_tracedactivitygroup_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedredefinableelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRedefinableElement)


def test_uml_tracedredefinableelement_constructor_exists():
    assert callable(uml_TracedRedefinableElement.__init__)


def test_uml_tracedredefinableelement_constructor_args():
    sig = inspect.signature(uml_TracedRedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedredefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedRedefinableTemplateSignature)


def test_umltrace_uml_tracedredefinabletemplatesignature_constructor_exists():
    assert callable(umlTrace_uml_TracedRedefinableTemplateSignature.__init__)


def test_umltrace_uml_tracedredefinabletemplatesignature_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedRedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActivityNode)


def test_umltrace_uml_tracedactivitynode_constructor_exists():
    assert callable(umlTrace_uml_TracedActivityNode.__init__)


def test_umltrace_uml_tracedactivitynode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(TracedActivityNode)


def test_tracedactivitynode_constructor_exists():
    assert callable(TracedActivityNode.__init__)


def test_tracedactivitynode_constructor_args():
    sig = inspect.signature(TracedActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcontrolnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedControlNode)


def test_umltrace_uml_tracedcontrolnode_constructor_exists():
    assert callable(umlTrace_uml_TracedControlNode.__init__)


def test_umltrace_uml_tracedcontrolnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedControlNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedexecutablenode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExecutableNode)


def test_umltrace_uml_tracedexecutablenode_constructor_exists():
    assert callable(umlTrace_uml_TracedExecutableNode.__init__)


def test_umltrace_uml_tracedexecutablenode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedexecutablenode_is_not_abstract():
    assert not inspect.isabstract(TracedExecutableNode)


def test_tracedexecutablenode_constructor_exists():
    assert callable(TracedExecutableNode.__init__)


def test_tracedexecutablenode_constructor_args():
    sig = inspect.signature(TracedExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedAction)


def test_umltrace_uml_tracedaction_constructor_exists():
    assert callable(umlTrace_uml_TracedAction.__init__)


def test_umltrace_uml_tracedaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactivitygroup_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActivityGroup)


def test_uml_tracedactivitygroup_constructor_exists():
    assert callable(uml_TracedActivityGroup.__init__)


def test_uml_tracedactivitygroup_constructor_args():
    sig = inspect.signature(uml_TracedActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracednamespace_is_not_abstract():
    assert not inspect.isabstract(uml_TracedNamespace)


def test_uml_tracednamespace_constructor_exists():
    assert callable(uml_TracedNamespace.__init__)


def test_uml_tracednamespace_constructor_args():
    sig = inspect.signature(uml_TracedNamespace.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedregion_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedRegion)


def test_umltrace_uml_tracedregion_constructor_exists():
    assert callable(umlTrace_uml_TracedRegion.__init__)


def test_umltrace_uml_tracedregion_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedRegion.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedpackage_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedPackage)


def test_umltrace_uml_tracedpackage_constructor_exists():
    assert callable(umlTrace_uml_TracedPackage.__init__)


def test_umltrace_uml_tracedpackage_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedPackage.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstate_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedState)


def test_umltrace_uml_tracedstate_constructor_exists():
    assert callable(umlTrace_uml_TracedState.__init__)


def test_umltrace_uml_tracedstate_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedState.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstructuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStructuredActivityNode)


def test_umltrace_uml_tracedstructuredactivitynode_constructor_exists():
    assert callable(umlTrace_uml_TracedStructuredActivityNode.__init__)


def test_umltrace_uml_tracedstructuredactivitynode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedclassifier_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedClassifier)


def test_umltrace_uml_tracedclassifier_constructor_exists():
    assert callable(umlTrace_uml_TracedClassifier.__init__)


def test_umltrace_uml_tracedclassifier_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedbehavioralfeature_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedBehavioralFeature)


def test_umltrace_uml_tracedbehavioralfeature_constructor_exists():
    assert callable(umlTrace_uml_TracedBehavioralFeature.__init__)


def test_umltrace_uml_tracedbehavioralfeature_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedBehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinteractionoperand_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInteractionOperand)


def test_umltrace_uml_tracedinteractionoperand_constructor_exists():
    assert callable(umlTrace_uml_TracedInteractionOperand.__init__)


def test_umltrace_uml_tracedinteractionoperand_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtransition_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTransition)


def test_umltrace_uml_tracedtransition_constructor_exists():
    assert callable(umlTrace_uml_TracedTransition.__init__)


def test_umltrace_uml_tracedtransition_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTransition.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedraiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRaiseExceptionAction)


def test_uml_tracedraiseexceptionaction_constructor_exists():
    assert callable(uml_TracedRaiseExceptionAction.__init__)


def test_uml_tracedraiseexceptionaction_constructor_args():
    sig = inspect.signature(uml_TracedRaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcommunicationpath_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCommunicationPath)


def test_uml_tracedcommunicationpath_constructor_exists():
    assert callable(uml_TracedCommunicationPath.__init__)


def test_uml_tracedcommunicationpath_constructor_args():
    sig = inspect.signature(uml_TracedCommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedliteralbooleanevaluation_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedLiteralBooleanEvaluation)


def test_kernel_tracedliteralbooleanevaluation_constructor_exists():
    assert callable(Kernel_TracedLiteralBooleanEvaluation.__init__)


def test_kernel_tracedliteralbooleanevaluation_constructor_args():
    sig = inspect.signature(Kernel_TracedLiteralBooleanEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedenumeration_is_not_abstract():
    assert not inspect.isabstract(uml_TracedEnumeration)


def test_uml_tracedenumeration_constructor_exists():
    assert callable(uml_TracedEnumeration.__init__)


def test_uml_tracedenumeration_constructor_args():
    sig = inspect.signature(uml_TracedEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadLinkObjectEndAction)


def test_uml_tracedreadlinkobjectendaction_constructor_exists():
    assert callable(uml_TracedReadLinkObjectEndAction.__init__)


def test_uml_tracedreadlinkobjectendaction_constructor_args():
    sig = inspect.signature(uml_TracedReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcallbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCallBehaviorAction)


def test_uml_tracedcallbehavioraction_constructor_exists():
    assert callable(uml_TracedCallBehaviorAction.__init__)


def test_uml_tracedcallbehavioraction_constructor_args():
    sig = inspect.signature(uml_TracedCallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedvariable_is_not_abstract():
    assert not inspect.isabstract(uml_TracedVariable)


def test_uml_tracedvariable_constructor_exists():
    assert callable(uml_TracedVariable.__init__)


def test_uml_tracedvariable_constructor_args():
    sig = inspect.signature(uml_TracedVariable.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconnectorend_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConnectorEnd)


def test_uml_tracedconnectorend_constructor_exists():
    assert callable(uml_TracedConnectorEnd.__init__)


def test_uml_tracedconnectorend_constructor_args():
    sig = inspect.signature(uml_TracedConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedartifact_is_not_abstract():
    assert not inspect.isabstract(uml_TracedArtifact)


def test_uml_tracedartifact_constructor_exists():
    assert callable(uml_TracedArtifact.__init__)


def test_uml_tracedartifact_constructor_args():
    sig = inspect.signature(uml_TracedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcalloperationaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCallOperationAction)


def test_uml_tracedcalloperationaction_constructor_exists():
    assert callable(uml_TracedCallOperationAction.__init__)


def test_uml_tracedcalloperationaction_constructor_args():
    sig = inspect.signature(uml_TracedCallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedliteralunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLiteralUnlimitedNatural)


def test_uml_tracedliteralunlimitednatural_constructor_exists():
    assert callable(uml_TracedLiteralUnlimitedNatural.__init__)


def test_uml_tracedliteralunlimitednatural_constructor_args():
    sig = inspect.signature(uml_TracedLiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddurationobservation_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDurationObservation)


def test_uml_traceddurationobservation_constructor_exists():
    assert callable(uml_TracedDurationObservation.__init__)


def test_uml_traceddurationobservation_constructor_args():
    sig = inspect.signature(uml_TracedDurationObservation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedbehaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedBehaviorExecutionSpecification)


def test_uml_tracedbehaviorexecutionspecification_constructor_exists():
    assert callable(uml_TracedBehaviorExecutionSpecification.__init__)


def test_uml_tracedbehaviorexecutionspecification_constructor_args():
    sig = inspect.signature(uml_TracedBehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactivityparameternode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActivityParameterNode)


def test_uml_tracedactivityparameternode_constructor_exists():
    assert callable(uml_TracedActivityParameterNode.__init__)


def test_uml_tracedactivityparameternode_constructor_args():
    sig = inspect.signature(uml_TracedActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedexpansionnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExpansionNode)


def test_uml_tracedexpansionnode_constructor_exists():
    assert callable(uml_TracedExpansionNode.__init__)


def test_uml_tracedexpansionnode_constructor_args():
    sig = inspect.signature(uml_TracedExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedprofileapplication_is_not_abstract():
    assert not inspect.isabstract(uml_TracedProfileApplication)


def test_uml_tracedprofileapplication_constructor_exists():
    assert callable(uml_TracedProfileApplication.__init__)


def test_uml_tracedprofileapplication_constructor_args():
    sig = inspect.signature(uml_TracedProfileApplication.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedaddstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAddStructuralFeatureValueAction)


def test_uml_tracedaddstructuralfeaturevalueaction_constructor_exists():
    assert callable(uml_TracedAddStructuralFeatureValueAction.__init__)


def test_uml_tracedaddstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml_TracedAddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedqualifiervalue_is_not_abstract():
    assert not inspect.isabstract(uml_TracedQualifierValue)


def test_uml_tracedqualifiervalue_constructor_exists():
    assert callable(uml_TracedQualifierValue.__init__)


def test_uml_tracedqualifiervalue_constructor_args():
    sig = inspect.signature(uml_TracedQualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedimage_is_not_abstract():
    assert not inspect.isabstract(uml_TracedImage)


def test_uml_tracedimage_constructor_exists():
    assert callable(uml_TracedImage.__init__)


def test_uml_tracedimage_constructor_args():
    sig = inspect.signature(uml_TracedImage.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedextensionend_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExtensionEnd)


def test_uml_tracedextensionend_constructor_exists():
    assert callable(uml_TracedExtensionEnd.__init__)


def test_uml_tracedextensionend_constructor_args():
    sig = inspect.signature(uml_TracedExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedproperty_is_not_abstract():
    assert not inspect.isabstract(uml_TracedProperty)


def test_uml_tracedproperty_constructor_exists():
    assert callable(uml_TracedProperty.__init__)


def test_uml_tracedproperty_constructor_args():
    sig = inspect.signature(uml_TracedProperty.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddevice_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDevice)


def test_uml_traceddevice_constructor_exists():
    assert callable(uml_TracedDevice.__init__)


def test_uml_traceddevice_constructor_args():
    sig = inspect.signature(uml_TracedDevice.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedopaqueaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedOpaqueAction)


def test_uml_tracedopaqueaction_constructor_exists():
    assert callable(uml_TracedOpaqueAction.__init__)


def test_uml_tracedopaqueaction_constructor_args():
    sig = inspect.signature(uml_TracedOpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedfinalstate_is_not_abstract():
    assert not inspect.isabstract(uml_TracedFinalState)


def test_uml_tracedfinalstate_constructor_exists():
    assert callable(uml_TracedFinalState.__init__)


def test_uml_tracedfinalstate_constructor_args():
    sig = inspect.signature(uml_TracedFinalState.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreduceaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReduceAction)


def test_uml_tracedreduceaction_constructor_exists():
    assert callable(uml_TracedReduceAction.__init__)


def test_uml_tracedreduceaction_constructor_args():
    sig = inspect.signature(uml_TracedReduceAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedduration_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDuration)


def test_uml_tracedduration_constructor_exists():
    assert callable(uml_TracedDuration.__init__)


def test_uml_tracedduration_constructor_args():
    sig = inspect.signature(uml_TracedDuration.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtemplateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTemplateParameterSubstitution)


def test_uml_tracedtemplateparametersubstitution_constructor_exists():
    assert callable(uml_TracedTemplateParameterSubstitution.__init__)


def test_uml_tracedtemplateparametersubstitution_constructor_args():
    sig = inspect.signature(uml_TracedTemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedoutputpin_is_not_abstract():
    assert not inspect.isabstract(uml_TracedOutputPin)


def test_uml_tracedoutputpin_constructor_exists():
    assert callable(uml_TracedOutputPin.__init__)


def test_uml_tracedoutputpin_constructor_args():
    sig = inspect.signature(uml_TracedOutputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActionExecutionSpecification)


def test_uml_tracedactionexecutionspecification_constructor_exists():
    assert callable(uml_TracedActionExecutionSpecification.__init__)


def test_uml_tracedactionexecutionspecification_constructor_args():
    sig = inspect.signature(uml_TracedActionExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinformationitem_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInformationItem)


def test_uml_tracedinformationitem_constructor_exists():
    assert callable(uml_TracedInformationItem.__init__)


def test_uml_tracedinformationitem_constructor_args():
    sig = inspect.signature(uml_TracedInformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedoperationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml_TracedOperationTemplateParameter)


def test_uml_tracedoperationtemplateparameter_constructor_exists():
    assert callable(uml_TracedOperationTemplateParameter.__init__)


def test_uml_tracedoperationtemplateparameter_constructor_args():
    sig = inspect.signature(uml_TracedOperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconnectableelementtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConnectableElementTemplateParameter)


def test_uml_tracedconnectableelementtemplateparameter_constructor_exists():
    assert callable(uml_TracedConnectableElementTemplateParameter.__init__)


def test_uml_tracedconnectableelementtemplateparameter_constructor_args():
    sig = inspect.signature(uml_TracedConnectableElementTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedlinkenddata_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLinkEndData)


def test_uml_tracedlinkenddata_constructor_exists():
    assert callable(uml_TracedLinkEndData.__init__)


def test_uml_tracedlinkenddata_constructor_args():
    sig = inspect.signature(uml_TracedLinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddurationinterval_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDurationInterval)


def test_uml_traceddurationinterval_constructor_exists():
    assert callable(uml_TracedDurationInterval.__init__)


def test_uml_traceddurationinterval_constructor_args():
    sig = inspect.signature(uml_TracedDurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtransition_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTransition)


def test_uml_tracedtransition_constructor_exists():
    assert callable(uml_TracedTransition.__init__)


def test_uml_tracedtransition_constructor_args():
    sig = inspect.signature(uml_TracedTransition.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtrigger_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTrigger)


def test_uml_tracedtrigger_constructor_exists():
    assert callable(uml_TracedTrigger.__init__)


def test_uml_tracedtrigger_constructor_args():
    sig = inspect.signature(uml_TracedTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreplyaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReplyAction)


def test_uml_tracedreplyaction_constructor_exists():
    assert callable(uml_TracedReplyAction.__init__)


def test_uml_tracedreplyaction_constructor_args():
    sig = inspect.signature(uml_TracedReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedclause_is_not_abstract():
    assert not inspect.isabstract(uml_TracedClause)


def test_uml_tracedclause_constructor_exists():
    assert callable(uml_TracedClause.__init__)


def test_uml_tracedclause_constructor_args():
    sig = inspect.signature(uml_TracedClause.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedpackagemerge_is_not_abstract():
    assert not inspect.isabstract(uml_TracedPackageMerge)


def test_uml_tracedpackagemerge_constructor_exists():
    assert callable(uml_TracedPackageMerge.__init__)


def test_uml_tracedpackagemerge_constructor_args():
    sig = inspect.signature(uml_TracedPackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddecisionnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDecisionNode)


def test_uml_traceddecisionnode_constructor_exists():
    assert callable(uml_TracedDecisionNode.__init__)


def test_uml_traceddecisionnode_constructor_args():
    sig = inspect.signature(uml_TracedDecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions_tracedreadstructuralfeatureactionactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_TracedReadStructuralFeatureActionActivation)


def test_intermediateactions_tracedreadstructuralfeatureactionactivation_constructor_exists():
    assert callable(IntermediateActions_TracedReadStructuralFeatureActionActivation.__init__)


def test_intermediateactions_tracedreadstructuralfeatureactionactivation_constructor_args():
    sig = inspect.signature(IntermediateActions_TracedReadStructuralFeatureActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadselfaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadSelfAction)


def test_uml_tracedreadselfaction_constructor_exists():
    assert callable(uml_TracedReadSelfAction.__init__)


def test_uml_tracedreadselfaction_constructor_args():
    sig = inspect.signature(uml_TracedReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedoperation_is_not_abstract():
    assert not inspect.isabstract(uml_TracedOperation)


def test_uml_tracedoperation_constructor_exists():
    assert callable(uml_TracedOperation.__init__)


def test_uml_tracedoperation_constructor_args():
    sig = inspect.signature(uml_TracedOperation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedobjectflow_is_not_abstract():
    assert not inspect.isabstract(uml_TracedObjectFlow)


def test_uml_tracedobjectflow_constructor_exists():
    assert callable(uml_TracedObjectFlow.__init__)


def test_uml_tracedobjectflow_constructor_args():
    sig = inspect.signature(uml_TracedObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedparameterset_is_not_abstract():
    assert not inspect.isabstract(uml_TracedParameterSet)


def test_uml_tracedparameterset_constructor_exists():
    assert callable(uml_TracedParameterSet.__init__)


def test_uml_tracedparameterset_constructor_args():
    sig = inspect.signature(uml_TracedParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedOccurrenceSpecification)


def test_uml_tracedoccurrencespecification_constructor_exists():
    assert callable(uml_TracedOccurrenceSpecification.__init__)


def test_uml_tracedoccurrencespecification_constructor_args():
    sig = inspect.signature(uml_TracedOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedmessageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedMessageOccurrenceSpecification)


def test_umltrace_uml_tracedmessageoccurrencespecification_constructor_exists():
    assert callable(umlTrace_uml_TracedMessageOccurrenceSpecification.__init__)


def test_umltrace_uml_tracedmessageoccurrencespecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedMessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedaccepteventaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAcceptEventAction)


def test_uml_tracedaccepteventaction_constructor_exists():
    assert callable(uml_TracedAcceptEventAction.__init__)


def test_uml_tracedaccepteventaction_constructor_args():
    sig = inspect.signature(uml_TracedAcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcomponentrealization_is_not_abstract():
    assert not inspect.isabstract(uml_TracedComponentRealization)


def test_uml_tracedcomponentrealization_constructor_exists():
    assert callable(uml_TracedComponentRealization.__init__)


def test_uml_tracedcomponentrealization_constructor_args():
    sig = inspect.signature(uml_TracedComponentRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddatatype_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDataType)


def test_uml_traceddatatype_constructor_exists():
    assert callable(uml_TracedDataType.__init__)


def test_uml_traceddatatype_constructor_args():
    sig = inspect.signature(uml_TracedDataType.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcomment_is_not_abstract():
    assert not inspect.isabstract(uml_TracedComment)


def test_uml_tracedcomment_constructor_exists():
    assert callable(uml_TracedComment.__init__)


def test_uml_tracedcomment_constructor_args():
    sig = inspect.signature(uml_TracedComment.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedloopnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLoopNode)


def test_uml_tracedloopnode_constructor_exists():
    assert callable(uml_TracedLoopNode.__init__)


def test_uml_tracedloopnode_constructor_args():
    sig = inspect.signature(uml_TracedLoopNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcallevent_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCallEvent)


def test_uml_tracedcallevent_constructor_exists():
    assert callable(uml_TracedCallEvent.__init__)


def test_uml_tracedcallevent_constructor_args():
    sig = inspect.signature(uml_TracedCallEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedpackage_is_not_abstract():
    assert not inspect.isabstract(uml_TracedPackage)


def test_uml_tracedpackage_constructor_exists():
    assert callable(uml_TracedPackage.__init__)


def test_uml_tracedpackage_constructor_args():
    sig = inspect.signature(uml_TracedPackage.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedprotocolconformance_is_not_abstract():
    assert not inspect.isabstract(uml_TracedProtocolConformance)


def test_uml_tracedprotocolconformance_constructor_exists():
    assert callable(uml_TracedProtocolConformance.__init__)


def test_uml_tracedprotocolconformance_constructor_args():
    sig = inspect.signature(uml_TracedProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedopaquebehavior_is_not_abstract():
    assert not inspect.isabstract(uml_TracedOpaqueBehavior)


def test_uml_tracedopaquebehavior_constructor_exists():
    assert callable(uml_TracedOpaqueBehavior.__init__)


def test_uml_tracedopaquebehavior_constructor_args():
    sig = inspect.signature(uml_TracedOpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinterface_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInterface)


def test_uml_tracedinterface_constructor_exists():
    assert callable(uml_TracedInterface.__init__)


def test_uml_tracedinterface_constructor_args():
    sig = inspect.signature(uml_TracedInterface.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_traceddecisionnodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedDecisionNodeActivation)


def test_intermediateactivities_traceddecisionnodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedDecisionNodeActivation.__init__)


def test_intermediateactivities_traceddecisionnodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedDecisionNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinteractionconstraint_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInteractionConstraint)


def test_uml_tracedinteractionconstraint_constructor_exists():
    assert callable(uml_TracedInteractionConstraint.__init__)


def test_uml_tracedinteractionconstraint_constructor_args():
    sig = inspect.signature(uml_TracedInteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtimeinterval_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTimeInterval)


def test_uml_tracedtimeinterval_constructor_exists():
    assert callable(uml_TracedTimeInterval.__init__)


def test_uml_tracedtimeinterval_constructor_args():
    sig = inspect.signature(uml_TracedTimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedexecutionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExecutionOccurrenceSpecification)


def test_uml_tracedexecutionoccurrencespecification_constructor_exists():
    assert callable(uml_TracedExecutionOccurrenceSpecification.__init__)


def test_uml_tracedexecutionoccurrencespecification_constructor_args():
    sig = inspect.signature(uml_TracedExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedsignal_is_not_abstract():
    assert not inspect.isabstract(uml_TracedSignal)


def test_uml_tracedsignal_constructor_exists():
    assert callable(uml_TracedSignal.__init__)


def test_uml_tracedsignal_constructor_args():
    sig = inspect.signature(uml_TracedSignal.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedextensionpoint_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExtensionPoint)


def test_uml_tracedextensionpoint_constructor_exists():
    assert callable(uml_TracedExtensionPoint.__init__)


def test_uml_tracedextensionpoint_constructor_args():
    sig = inspect.signature(uml_TracedExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcreatelinkaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCreateLinkAction)


def test_uml_tracedcreatelinkaction_constructor_exists():
    assert callable(uml_TracedCreateLinkAction.__init__)


def test_uml_tracedcreatelinkaction_constructor_args():
    sig = inspect.signature(uml_TracedCreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedliteralintegerevaluation_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedLiteralIntegerEvaluation)


def test_kernel_tracedliteralintegerevaluation_constructor_exists():
    assert callable(Kernel_TracedLiteralIntegerEvaluation.__init__)


def test_kernel_tracedliteralintegerevaluation_constructor_args():
    sig = inspect.signature(Kernel_TracedLiteralIntegerEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcentralbuffernode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCentralBufferNode)


def test_uml_tracedcentralbuffernode_constructor_exists():
    assert callable(uml_TracedCentralBufferNode.__init__)


def test_uml_tracedcentralbuffernode_constructor_args():
    sig = inspect.signature(uml_TracedCentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedmodel_is_not_abstract():
    assert not inspect.isabstract(uml_TracedModel)


def test_uml_tracedmodel_constructor_exists():
    assert callable(uml_TracedModel.__init__)


def test_uml_tracedmodel_constructor_args():
    sig = inspect.signature(uml_TracedModel.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedredefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRedefinableTemplateSignature)


def test_uml_tracedredefinabletemplatesignature_constructor_exists():
    assert callable(uml_TracedRedefinableTemplateSignature.__init__)


def test_uml_tracedredefinabletemplatesignature_constructor_args():
    sig = inspect.signature(uml_TracedRedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedjoinnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedJoinNode)


def test_uml_tracedjoinnode_constructor_exists():
    assert callable(uml_TracedJoinNode.__init__)


def test_uml_tracedjoinnode_constructor_args():
    sig = inspect.signature(uml_TracedJoinNode.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_tracedopaqueactionactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions_TracedOpaqueActionActivation)


def test_basicactions_tracedopaqueactionactivation_constructor_exists():
    assert callable(BasicActions_TracedOpaqueActionActivation.__init__)


def test_basicactions_tracedopaqueactionactivation_constructor_args():
    sig = inspect.signature(BasicActions_TracedOpaqueActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadLinkObjectEndQualifierAction)


def test_uml_tracedreadlinkobjectendqualifieraction_constructor_exists():
    assert callable(uml_TracedReadLinkObjectEndQualifierAction.__init__)


def test_uml_tracedreadlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(uml_TracedReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedrealization_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRealization)


def test_uml_tracedrealization_constructor_exists():
    assert callable(uml_TracedRealization.__init__)


def test_uml_tracedrealization_constructor_args():
    sig = inspect.signature(uml_TracedRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconnectionpointreference_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConnectionPointReference)


def test_uml_tracedconnectionpointreference_constructor_exists():
    assert callable(uml_TracedConnectionPointReference.__init__)


def test_uml_tracedconnectionpointreference_constructor_args():
    sig = inspect.signature(uml_TracedConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconditionalnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConditionalNode)


def test_uml_tracedconditionalnode_constructor_exists():
    assert callable(uml_TracedConditionalNode.__init__)


def test_uml_tracedconditionalnode_constructor_args():
    sig = inspect.signature(uml_TracedConditionalNode.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedbooleanvalue_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedBooleanValue)


def test_kernel_tracedbooleanvalue_constructor_exists():
    assert callable(Kernel_TracedBooleanValue.__init__)


def test_kernel_tracedbooleanvalue_constructor_args():
    sig = inspect.signature(Kernel_TracedBooleanValue.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedsignalevent_is_not_abstract():
    assert not inspect.isabstract(uml_TracedSignalEvent)


def test_uml_tracedsignalevent_constructor_exists():
    assert callable(uml_TracedSignalEvent.__init__)


def test_uml_tracedsignalevent_constructor_args():
    sig = inspect.signature(uml_TracedSignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedliteralinteger_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLiteralInteger)


def test_uml_tracedliteralinteger_constructor_exists():
    assert callable(uml_TracedLiteralInteger.__init__)


def test_uml_tracedliteralinteger_constructor_args():
    sig = inspect.signature(uml_TracedLiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddestroylinkaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDestroyLinkAction)


def test_uml_traceddestroylinkaction_constructor_exists():
    assert callable(uml_TracedDestroyLinkAction.__init__)


def test_uml_traceddestroylinkaction_constructor_args():
    sig = inspect.signature(uml_TracedDestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedactivityfinalnodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedActivityFinalNodeActivation)


def test_intermediateactivities_tracedactivityfinalnodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedActivityFinalNodeActivation.__init__)


def test_intermediateactivities_tracedactivityfinalnodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedActivityFinalNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadVariableAction)


def test_uml_tracedreadvariableaction_constructor_exists():
    assert callable(uml_TracedReadVariableAction.__init__)


def test_uml_tracedreadvariableaction_constructor_args():
    sig = inspect.signature(uml_TracedReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactioninputpin_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActionInputPin)


def test_uml_tracedactioninputpin_constructor_exists():
    assert callable(uml_TracedActionInputPin.__init__)


def test_uml_tracedactioninputpin_constructor_args():
    sig = inspect.signature(uml_TracedActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedusage_is_not_abstract():
    assert not inspect.isabstract(uml_TracedUsage)


def test_uml_tracedusage_constructor_exists():
    assert callable(uml_TracedUsage.__init__)


def test_uml_tracedusage_constructor_args():
    sig = inspect.signature(uml_TracedUsage.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddeploymentspecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDeploymentSpecification)


def test_uml_traceddeploymentspecification_constructor_exists():
    assert callable(uml_TracedDeploymentSpecification.__init__)


def test_uml_traceddeploymentspecification_constructor_args():
    sig = inspect.signature(uml_TracedDeploymentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtemplatebinding_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTemplateBinding)


def test_uml_tracedtemplatebinding_constructor_exists():
    assert callable(uml_TracedTemplateBinding.__init__)


def test_uml_tracedtemplatebinding_constructor_args():
    sig = inspect.signature(uml_TracedTemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedmessageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedMessageOccurrenceSpecification)


def test_uml_tracedmessageoccurrencespecification_constructor_exists():
    assert callable(uml_TracedMessageOccurrenceSpecification.__init__)


def test_uml_tracedmessageoccurrencespecification_constructor_args():
    sig = inspect.signature(uml_TracedMessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreception_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReception)


def test_uml_tracedreception_constructor_exists():
    assert callable(uml_TracedReception.__init__)


def test_uml_tracedreception_constructor_args():
    sig = inspect.signature(uml_TracedReception.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedprotocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(uml_TracedProtocolStateMachine)


def test_uml_tracedprotocolstatemachine_constructor_exists():
    assert callable(uml_TracedProtocolStateMachine.__init__)


def test_uml_tracedprotocolstatemachine_constructor_args():
    sig = inspect.signature(uml_TracedProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddatastorenode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDataStoreNode)


def test_uml_traceddatastorenode_constructor_exists():
    assert callable(uml_TracedDataStoreNode.__init__)


def test_uml_traceddatastorenode_constructor_args():
    sig = inspect.signature(uml_TracedDataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadStructuralFeatureAction)


def test_uml_tracedreadstructuralfeatureaction_constructor_exists():
    assert callable(uml_TracedReadStructuralFeatureAction.__init__)


def test_uml_tracedreadstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml_TracedReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedanyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAnyReceiveEvent)


def test_uml_tracedanyreceiveevent_constructor_exists():
    assert callable(uml_TracedAnyReceiveEvent.__init__)


def test_uml_tracedanyreceiveevent_constructor_args():
    sig = inspect.signature(uml_TracedAnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedintegervalue_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedIntegerValue)


def test_kernel_tracedintegervalue_constructor_exists():
    assert callable(Kernel_TracedIntegerValue.__init__)


def test_kernel_tracedintegervalue_constructor_args():
    sig = inspect.signature(Kernel_TracedIntegerValue.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinterval_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInterval)


def test_uml_tracedinterval_constructor_exists():
    assert callable(uml_TracedInterval.__init__)


def test_uml_tracedinterval_constructor_args():
    sig = inspect.signature(uml_TracedInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedremovestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRemoveStructuralFeatureValueAction)


def test_uml_tracedremovestructuralfeaturevalueaction_constructor_exists():
    assert callable(uml_TracedRemoveStructuralFeatureValueAction.__init__)


def test_uml_tracedremovestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml_TracedRemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedgeneralization_is_not_abstract():
    assert not inspect.isabstract(uml_TracedGeneralization)


def test_uml_tracedgeneralization_constructor_exists():
    assert callable(uml_TracedGeneralization.__init__)


def test_uml_tracedgeneralization_constructor_args():
    sig = inspect.signature(uml_TracedGeneralization.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinteractionoperand_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInteractionOperand)


def test_uml_tracedinteractionoperand_constructor_exists():
    assert callable(uml_TracedInteractionOperand.__init__)


def test_uml_tracedinteractionoperand_constructor_args():
    sig = inspect.signature(uml_TracedInteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedprotocoltransition_is_not_abstract():
    assert not inspect.isabstract(uml_TracedProtocolTransition)


def test_uml_tracedprotocoltransition_constructor_exists():
    assert callable(uml_TracedProtocolTransition.__init__)


def test_uml_tracedprotocoltransition_constructor_args():
    sig = inspect.signature(uml_TracedProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinterruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInterruptibleActivityRegion)


def test_uml_tracedinterruptibleactivityregion_constructor_exists():
    assert callable(uml_TracedInterruptibleActivityRegion.__init__)


def test_uml_tracedinterruptibleactivityregion_constructor_args():
    sig = inspect.signature(uml_TracedInterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedpartdecomposition_is_not_abstract():
    assert not inspect.isabstract(uml_TracedPartDecomposition)


def test_uml_tracedpartdecomposition_constructor_exists():
    assert callable(uml_TracedPartDecomposition.__init__)


def test_uml_tracedpartdecomposition_constructor_args():
    sig = inspect.signature(uml_TracedPartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtimeevent_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTimeEvent)


def test_uml_tracedtimeevent_constructor_exists():
    assert callable(uml_TracedTimeEvent.__init__)


def test_uml_tracedtimeevent_constructor_args():
    sig = inspect.signature(uml_TracedTimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddeployment_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDeployment)


def test_uml_traceddeployment_constructor_exists():
    assert callable(uml_TracedDeployment.__init__)


def test_uml_traceddeployment_constructor_args():
    sig = inspect.signature(uml_TracedDeployment.__init__)
    params = list(sig.parameters.keys())



def test_loci_tracedsemanticvisitor_is_not_abstract():
    assert not inspect.isabstract(Loci_TracedSemanticVisitor)


def test_loci_tracedsemanticvisitor_constructor_exists():
    assert callable(Loci_TracedSemanticVisitor.__init__)


def test_loci_tracedsemanticvisitor_constructor_args():
    sig = inspect.signature(Loci_TracedSemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedobject_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedObject)


def test_kernel_tracedobject_constructor_exists():
    assert callable(Kernel_TracedObject.__init__)


def test_kernel_tracedobject_constructor_args():
    sig = inspect.signature(Kernel_TracedObject.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedjoinnodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedJoinNodeActivation)


def test_intermediateactivities_tracedjoinnodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedJoinNodeActivation.__init__)


def test_intermediateactivities_tracedjoinnodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedJoinNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedusecase_is_not_abstract():
    assert not inspect.isabstract(uml_TracedUseCase)


def test_uml_tracedusecase_constructor_exists():
    assert callable(uml_TracedUseCase.__init__)


def test_uml_tracedusecase_constructor_args():
    sig = inspect.signature(uml_TracedUseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReclassifyObjectAction)


def test_uml_tracedreclassifyobjectaction_constructor_exists():
    assert callable(uml_TracedReclassifyObjectAction.__init__)


def test_uml_tracedreclassifyobjectaction_constructor_args():
    sig = inspect.signature(uml_TracedReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinstancevalue_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInstanceValue)


def test_uml_tracedinstancevalue_constructor_exists():
    assert callable(uml_TracedInstanceValue.__init__)


def test_uml_tracedinstancevalue_constructor_args():
    sig = inspect.signature(uml_TracedInstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions_tracedaddstructuralfeaturevalueactionactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_TracedAddStructuralFeatureValueActionActivation)


def test_intermediateactions_tracedaddstructuralfeaturevalueactionactivation_constructor_exists():
    assert callable(IntermediateActions_TracedAddStructuralFeatureValueActionActivation.__init__)


def test_intermediateactions_tracedaddstructuralfeaturevalueactionactivation_constructor_args():
    sig = inspect.signature(IntermediateActions_TracedAddStructuralFeatureValueActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedreference_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedReference)


def test_kernel_tracedreference_constructor_exists():
    assert callable(Kernel_TracedReference.__init__)


def test_kernel_tracedreference_constructor_args():
    sig = inspect.signature(Kernel_TracedReference.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedforknode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedForkNode)


def test_uml_tracedforknode_constructor_exists():
    assert callable(uml_TracedForkNode.__init__)


def test_uml_tracedforknode_constructor_args():
    sig = inspect.signature(uml_TracedForkNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactivity_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActivity)


def test_uml_tracedactivity_constructor_exists():
    assert callable(uml_TracedActivity.__init__)


def test_uml_tracedactivity_constructor_args():
    sig = inspect.signature(uml_TracedActivity.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedmessage_is_not_abstract():
    assert not inspect.isabstract(uml_TracedMessage)


def test_uml_tracedmessage_constructor_exists():
    assert callable(uml_TracedMessage.__init__)


def test_uml_tracedmessage_constructor_args():
    sig = inspect.signature(uml_TracedMessage.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstatemachine_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStateMachine)


def test_uml_tracedstatemachine_constructor_exists():
    assert callable(uml_TracedStateMachine.__init__)


def test_uml_tracedstatemachine_constructor_args():
    sig = inspect.signature(uml_TracedStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactivitypartition_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActivityPartition)


def test_uml_tracedactivitypartition_constructor_exists():
    assert callable(uml_TracedActivityPartition.__init__)


def test_uml_tracedactivitypartition_constructor_args():
    sig = inspect.signature(uml_TracedActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedactivityparameternodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedActivityParameterNodeActivation)


def test_intermediateactivities_tracedactivityparameternodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedActivityParameterNodeActivation.__init__)


def test_intermediateactivities_tracedactivityparameternodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedActivityParameterNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_tracedcallbehavioractionactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions_TracedCallBehaviorActionActivation)


def test_basicactions_tracedcallbehavioractionactivation_constructor_exists():
    assert callable(BasicActions_TracedCallBehaviorActionActivation.__init__)


def test_basicactions_tracedcallbehavioractionactivation_constructor_args():
    sig = inspect.signature(BasicActions_TracedCallBehaviorActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddestroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDestroyObjectAction)


def test_uml_traceddestroyobjectaction_constructor_exists():
    assert callable(uml_TracedDestroyObjectAction.__init__)


def test_uml_traceddestroyobjectaction_constructor_args():
    sig = inspect.signature(uml_TracedDestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedassociationclass_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAssociationClass)


def test_uml_tracedassociationclass_constructor_exists():
    assert callable(uml_TracedAssociationClass.__init__)


def test_uml_tracedassociationclass_constructor_args():
    sig = inspect.signature(uml_TracedAssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinformationflow_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInformationFlow)


def test_uml_tracedinformationflow_constructor_exists():
    assert callable(uml_TracedInformationFlow.__init__)


def test_uml_tracedinformationflow_constructor_args():
    sig = inspect.signature(uml_TracedInformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedsubstitution_is_not_abstract():
    assert not inspect.isabstract(uml_TracedSubstitution)


def test_uml_tracedsubstitution_constructor_exists():
    assert callable(uml_TracedSubstitution.__init__)


def test_uml_tracedsubstitution_constructor_args():
    sig = inspect.signature(uml_TracedSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedenumerationliteral_is_not_abstract():
    assert not inspect.isabstract(uml_TracedEnumerationLiteral)


def test_uml_tracedenumerationliteral_constructor_exists():
    assert callable(uml_TracedEnumerationLiteral.__init__)


def test_uml_tracedenumerationliteral_constructor_args():
    sig = inspect.signature(uml_TracedEnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstereotype_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStereotype)


def test_uml_tracedstereotype_constructor_exists():
    assert callable(uml_TracedStereotype.__init__)


def test_uml_tracedstereotype_constructor_args():
    sig = inspect.signature(uml_TracedStereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedacceptcallaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAcceptCallAction)


def test_uml_tracedacceptcallaction_constructor_exists():
    assert callable(uml_TracedAcceptCallAction.__init__)


def test_uml_tracedacceptcallaction_constructor_args():
    sig = inspect.signature(uml_TracedAcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinstancespecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInstanceSpecification)


def test_uml_tracedinstancespecification_constructor_exists():
    assert callable(uml_TracedInstanceSpecification.__init__)


def test_uml_tracedinstancespecification_constructor_args():
    sig = inspect.signature(uml_TracedInstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_integerfunctions_tracedintegerlessfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution)


def test_integerfunctions_tracedintegerlessfunctionbehaviorexecution_constructor_exists():
    assert callable(IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution.__init__)


def test_integerfunctions_tracedintegerlessfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstateinvariant_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStateInvariant)


def test_uml_tracedstateinvariant_constructor_exists():
    assert callable(uml_TracedStateInvariant.__init__)


def test_uml_tracedstateinvariant_constructor_args():
    sig = inspect.signature(uml_TracedStateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_tracedinputpinactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions_TracedInputPinActivation)


def test_basicactions_tracedinputpinactivation_constructor_exists():
    assert callable(BasicActions_TracedInputPinActivation.__init__)


def test_basicactions_tracedinputpinactivation_constructor_args():
    sig = inspect.signature(BasicActions_TracedInputPinActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedliteralstring_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLiteralString)


def test_uml_tracedliteralstring_constructor_exists():
    assert callable(uml_TracedLiteralString.__init__)


def test_uml_tracedliteralstring_constructor_args():
    sig = inspect.signature(uml_TracedLiteralString.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedopaqueexpression_is_not_abstract():
    assert not inspect.isabstract(uml_TracedOpaqueExpression)


def test_uml_tracedopaqueexpression_constructor_exists():
    assert callable(uml_TracedOpaqueExpression.__init__)


def test_uml_tracedopaqueexpression_constructor_args():
    sig = inspect.signature(uml_TracedOpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedparameter_is_not_abstract():
    assert not inspect.isabstract(uml_TracedParameter)


def test_uml_tracedparameter_constructor_exists():
    assert callable(uml_TracedParameter.__init__)


def test_uml_tracedparameter_constructor_args():
    sig = inspect.signature(uml_TracedParameter.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedactivitynodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedActivityNodeActivation)


def test_intermediateactivities_tracedactivitynodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedActivityNodeActivation.__init__)


def test_intermediateactivities_tracedactivitynodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedActivityNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinteraction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInteraction)


def test_uml_tracedinteraction_constructor_exists():
    assert callable(uml_TracedInteraction.__init__)


def test_uml_tracedinteraction_constructor_args():
    sig = inspect.signature(uml_TracedInteraction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedbroadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedBroadcastSignalAction)


def test_uml_tracedbroadcastsignalaction_constructor_exists():
    assert callable(uml_TracedBroadcastSignalAction.__init__)


def test_uml_tracedbroadcastsignalaction_constructor_args():
    sig = inspect.signature(uml_TracedBroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconstraint_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConstraint)


def test_uml_tracedconstraint_constructor_exists():
    assert callable(uml_TracedConstraint.__init__)


def test_uml_tracedconstraint_constructor_args():
    sig = inspect.signature(uml_TracedConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedclearvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedClearVariableAction)


def test_uml_tracedclearvariableaction_constructor_exists():
    assert callable(uml_TracedClearVariableAction.__init__)


def test_uml_tracedclearvariableaction_constructor_args():
    sig = inspect.signature(uml_TracedClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinputpin_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInputPin)


def test_uml_tracedinputpin_constructor_exists():
    assert callable(uml_TracedInputPin.__init__)


def test_uml_tracedinputpin_constructor_args():
    sig = inspect.signature(uml_TracedInputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtimeconstraint_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTimeConstraint)


def test_uml_tracedtimeconstraint_constructor_exists():
    assert callable(uml_TracedTimeConstraint.__init__)


def test_uml_tracedtimeconstraint_constructor_args():
    sig = inspect.signature(uml_TracedTimeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcontinuation_is_not_abstract():
    assert not inspect.isabstract(uml_TracedContinuation)


def test_uml_tracedcontinuation_constructor_exists():
    assert callable(uml_TracedContinuation.__init__)


def test_uml_tracedcontinuation_constructor_args():
    sig = inspect.signature(uml_TracedContinuation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconsiderignorefragment_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConsiderIgnoreFragment)


def test_uml_tracedconsiderignorefragment_constructor_exists():
    assert callable(uml_TracedConsiderIgnoreFragment.__init__)


def test_uml_tracedconsiderignorefragment_constructor_args():
    sig = inspect.signature(uml_TracedConsiderIgnoreFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedintervalconstraint_is_not_abstract():
    assert not inspect.isabstract(uml_TracedIntervalConstraint)


def test_uml_tracedintervalconstraint_constructor_exists():
    assert callable(uml_TracedIntervalConstraint.__init__)


def test_uml_tracedintervalconstraint_constructor_args():
    sig = inspect.signature(uml_TracedIntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedexecutionenvironment_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExecutionEnvironment)


def test_uml_tracedexecutionenvironment_constructor_exists():
    assert callable(uml_TracedExecutionEnvironment.__init__)


def test_uml_tracedexecutionenvironment_constructor_args():
    sig = inspect.signature(uml_TracedExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstructuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStructuredActivityNode)


def test_uml_tracedstructuredactivitynode_constructor_exists():
    assert callable(uml_TracedStructuredActivityNode.__init__)


def test_uml_tracedstructuredactivitynode_constructor_args():
    sig = inspect.signature(uml_TracedStructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedextension_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExtension)


def test_uml_tracedextension_constructor_exists():
    assert callable(uml_TracedExtension.__init__)


def test_uml_tracedextension_constructor_args():
    sig = inspect.signature(uml_TracedExtension.__init__)
    params = list(sig.parameters.keys())



def test_integerfunctions_tracedintegerplusfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution)


def test_integerfunctions_tracedintegerplusfunctionbehaviorexecution_constructor_exists():
    assert callable(IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution.__init__)


def test_integerfunctions_tracedintegerplusfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedextend_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExtend)


def test_uml_tracedextend_constructor_exists():
    assert callable(uml_TracedExtend.__init__)


def test_uml_tracedextend_constructor_args():
    sig = inspect.signature(uml_TracedExtend.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstartclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStartClassifierBehaviorAction)


def test_uml_tracedstartclassifierbehavioraction_constructor_exists():
    assert callable(uml_TracedStartClassifierBehaviorAction.__init__)


def test_uml_tracedstartclassifierbehavioraction_constructor_args():
    sig = inspect.signature(uml_TracedStartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedsequencenode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedSequenceNode)


def test_uml_tracedsequencenode_constructor_exists():
    assert callable(uml_TracedSequenceNode.__init__)


def test_uml_tracedsequencenode_constructor_args():
    sig = inspect.signature(uml_TracedSequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedexceptionhandler_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExceptionHandler)


def test_uml_tracedexceptionhandler_constructor_exists():
    assert callable(uml_TracedExceptionHandler.__init__)


def test_uml_tracedexceptionhandler_constructor_args():
    sig = inspect.signature(uml_TracedExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracednode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedNode)


def test_uml_tracednode_constructor_exists():
    assert callable(uml_TracedNode.__init__)


def test_uml_tracednode_constructor_args():
    sig = inspect.signature(uml_TracedNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedvaluepin_is_not_abstract():
    assert not inspect.isabstract(uml_TracedValuePin)


def test_uml_tracedvaluepin_constructor_exists():
    assert callable(uml_TracedValuePin.__init__)


def test_uml_tracedvaluepin_constructor_args():
    sig = inspect.signature(uml_TracedValuePin.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedactivityexecution_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedActivityExecution)


def test_intermediateactivities_tracedactivityexecution_constructor_exists():
    assert callable(IntermediateActivities_TracedActivityExecution.__init__)


def test_intermediateactivities_tracedactivityexecution_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedActivityExecution.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcollaborationuse_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCollaborationUse)


def test_uml_tracedcollaborationuse_constructor_exists():
    assert callable(uml_TracedCollaborationUse.__init__)


def test_uml_tracedcollaborationuse_constructor_args():
    sig = inspect.signature(uml_TracedCollaborationUse.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedinitialnodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedInitialNodeActivation)


def test_intermediateactivities_tracedinitialnodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedInitialNodeActivation.__init__)


def test_intermediateactivities_tracedinitialnodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedInitialNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedport_is_not_abstract():
    assert not inspect.isabstract(uml_TracedPort)


def test_uml_tracedport_constructor_exists():
    assert callable(uml_TracedPort.__init__)


def test_uml_tracedport_constructor_args():
    sig = inspect.signature(uml_TracedPort.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddependency_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDependency)


def test_uml_traceddependency_constructor_exists():
    assert callable(uml_TracedDependency.__init__)


def test_uml_traceddependency_constructor_args():
    sig = inspect.signature(uml_TracedDependency.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedchangeevent_is_not_abstract():
    assert not inspect.isabstract(uml_TracedChangeEvent)


def test_uml_tracedchangeevent_constructor_exists():
    assert callable(uml_TracedChangeEvent.__init__)


def test_uml_tracedchangeevent_constructor_args():
    sig = inspect.signature(uml_TracedChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedgeneralizationset_is_not_abstract():
    assert not inspect.isabstract(uml_TracedGeneralizationSet)


def test_uml_tracedgeneralizationset_constructor_exists():
    assert callable(uml_TracedGeneralizationSet.__init__)


def test_uml_tracedgeneralizationset_constructor_args():
    sig = inspect.signature(uml_TracedGeneralizationSet.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinteractionuse_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInteractionUse)


def test_uml_tracedinteractionuse_constructor_exists():
    assert callable(uml_TracedInteractionUse.__init__)


def test_uml_tracedinteractionuse_constructor_args():
    sig = inspect.signature(uml_TracedInteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedclass_is_not_abstract():
    assert not inspect.isabstract(uml_TracedClass)


def test_uml_tracedclass_constructor_exists():
    assert callable(uml_TracedClass.__init__)


def test_uml_tracedclass_constructor_args():
    sig = inspect.signature(uml_TracedClass.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracednode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedNode)


def test_umltrace_uml_tracednode_constructor_exists():
    assert callable(umlTrace_uml_TracedNode.__init__)


def test_umltrace_uml_tracednode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedassociationclass_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedAssociationClass)


def test_umltrace_uml_tracedassociationclass_constructor_exists():
    assert callable(umlTrace_uml_TracedAssociationClass.__init__)


def test_umltrace_uml_tracedassociationclass_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedAssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedpackageimport_is_not_abstract():
    assert not inspect.isabstract(uml_TracedPackageImport)


def test_uml_tracedpackageimport_constructor_exists():
    assert callable(uml_TracedPackageImport.__init__)


def test_uml_tracedpackageimport_constructor_args():
    sig = inspect.signature(uml_TracedPackageImport.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedsendobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedSendObjectAction)


def test_uml_tracedsendobjectaction_constructor_exists():
    assert callable(uml_TracedSendObjectAction.__init__)


def test_uml_tracedsendobjectaction_constructor_args():
    sig = inspect.signature(uml_TracedSendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconnector_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConnector)


def test_uml_tracedconnector_constructor_exists():
    assert callable(uml_TracedConnector.__init__)


def test_uml_tracedconnector_constructor_args():
    sig = inspect.signature(uml_TracedConnector.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddestructionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDestructionOccurrenceSpecification)


def test_uml_traceddestructionoccurrencespecification_constructor_exists():
    assert callable(uml_TracedDestructionOccurrenceSpecification.__init__)


def test_uml_traceddestructionoccurrencespecification_constructor_args():
    sig = inspect.signature(uml_TracedDestructionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddurationconstraint_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDurationConstraint)


def test_uml_traceddurationconstraint_constructor_exists():
    assert callable(uml_TracedDurationConstraint.__init__)


def test_uml_traceddurationconstraint_constructor_args():
    sig = inspect.signature(uml_TracedDurationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedforknodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedForkNodeActivation)


def test_intermediateactivities_tracedforknodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedForkNodeActivation.__init__)


def test_intermediateactivities_tracedforknodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedForkNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedlifeline_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLifeline)


def test_uml_tracedlifeline_constructor_exists():
    assert callable(uml_TracedLifeline.__init__)


def test_uml_tracedlifeline_constructor_args():
    sig = inspect.signature(uml_TracedLifeline.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcreateobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCreateObjectAction)


def test_uml_tracedcreateobjectaction_constructor_exists():
    assert callable(uml_TracedCreateObjectAction.__init__)


def test_uml_tracedcreateobjectaction_constructor_args():
    sig = inspect.signature(uml_TracedCreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedexpansionregion_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExpansionRegion)


def test_uml_tracedexpansionregion_constructor_exists():
    assert callable(uml_TracedExpansionRegion.__init__)


def test_uml_tracedexpansionregion_constructor_args():
    sig = inspect.signature(uml_TracedExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedflowfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedFlowFinalNode)


def test_uml_tracedflowfinalnode_constructor_exists():
    assert callable(uml_TracedFlowFinalNode.__init__)


def test_uml_tracedflowfinalnode_constructor_args():
    sig = inspect.signature(uml_TracedFlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinitialnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInitialNode)


def test_uml_tracedinitialnode_constructor_exists():
    assert callable(uml_TracedInitialNode.__init__)


def test_uml_tracedinitialnode_constructor_args():
    sig = inspect.signature(uml_TracedInitialNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcreatelinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCreateLinkObjectAction)


def test_uml_tracedcreatelinkobjectaction_constructor_exists():
    assert callable(uml_TracedCreateLinkObjectAction.__init__)


def test_uml_tracedcreatelinkobjectaction_constructor_args():
    sig = inspect.signature(uml_TracedCreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcombinedfragment_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCombinedFragment)


def test_uml_tracedcombinedfragment_constructor_exists():
    assert callable(uml_TracedCombinedFragment.__init__)


def test_uml_tracedcombinedfragment_constructor_args():
    sig = inspect.signature(uml_TracedCombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_traced_tracedobjects_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Traced_TracedObjects)


def test_umltrace_traced_tracedobjects_constructor_exists():
    assert callable(umlTrace_Traced_TracedObjects.__init__)


def test_umltrace_traced_tracedobjects_constructor_args():
    sig = inspect.signature(umlTrace_Traced_TracedObjects.__init__)
    params = list(sig.parameters.keys())



def test_traced_tracedobjects_is_not_abstract():
    assert not inspect.isabstract(Traced_TracedObjects)


def test_traced_tracedobjects_constructor_exists():
    assert callable(Traced_TracedObjects.__init__)


def test_traced_tracedobjects_constructor_args():
    sig = inspect.signature(Traced_TracedObjects.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_trace_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Trace)


def test_umltrace_trace_constructor_exists():
    assert callable(umlTrace_Trace.__init__)


def test_umltrace_trace_constructor_args():
    sig = inspect.signature(umlTrace_Trace.__init__)
    params = list(sig.parameters.keys())



def test_values_semanticvisitor_runtimemodelelement_value_is_not_abstract():
    assert not inspect.isabstract(Values_SemanticVisitor_runtimeModelElement_Value)


def test_values_semanticvisitor_runtimemodelelement_value_constructor_exists():
    assert callable(Values_SemanticVisitor_runtimeModelElement_Value.__init__)


def test_values_semanticvisitor_runtimemodelelement_value_constructor_args():
    sig = inspect.signature(Values_SemanticVisitor_runtimeModelElement_Value.__init__)
    params = list(sig.parameters.keys())



def test_values_actionactivation_firing_value_is_not_abstract():
    assert not inspect.isabstract(Values_ActionActivation_firing_Value)


def test_values_actionactivation_firing_value_constructor_exists():
    assert callable(Values_ActionActivation_firing_Value.__init__)


def test_values_actionactivation_firing_value_constructor_args():
    sig = inspect.signature(Values_ActionActivation_firing_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_state_is_not_abstract():
    assert not inspect.isabstract(umlTrace_State)


def test_umltrace_state_constructor_exists():
    assert callable(umlTrace_State.__init__)


def test_umltrace_state_constructor_args():
    sig = inspect.signature(umlTrace_State.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
TracedExecution_strategy = st.builds(
    TracedExecution,
)
umlTrace_IntermediateActivities_TracedActivityExecution_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedActivityExecution,
)
TracedSemanticVisitor_strategy = st.builds(
    TracedSemanticVisitor,
)
umlTrace_IntermediateActivities_TracedActivityNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedActivityNodeActivation,
)
TracedActivityNodeActivation_strategy = st.builds(
    TracedActivityNodeActivation,
)
umlTrace_IntermediateActivities_TracedObjectNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedObjectNodeActivation,
)
umlTrace_IntermediateActivities_TracedControlNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedControlNodeActivation,
)
TracedControlNodeActivation_strategy = st.builds(
    TracedControlNodeActivation,
)
umlTrace_IntermediateActivities_TracedInitialNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedInitialNodeActivation,
)
umlTrace_IntermediateActivities_TracedMergeNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedMergeNodeActivation,
)
umlTrace_IntermediateActivities_TracedForkNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedForkNodeActivation,
)
uml_TracedVertex_strategy = st.builds(
    uml_TracedVertex,
)
TracedState_strategy = st.builds(
    TracedState,
)
umlTrace_uml_TracedFinalState_strategy = st.builds(
    umlTrace_uml_TracedFinalState,
)
TracedExecutionSpecification_strategy = st.builds(
    TracedExecutionSpecification,
)
umlTrace_uml_TracedBehaviorExecutionSpecification_strategy = st.builds(
    umlTrace_uml_TracedBehaviorExecutionSpecification,
)
TracedOccurrenceSpecification_strategy = st.builds(
    TracedOccurrenceSpecification,
)
umlTrace_uml_TracedExecutionOccurrenceSpecification_strategy = st.builds(
    umlTrace_uml_TracedExecutionOccurrenceSpecification,
)
TracedOpaqueBehavior_strategy = st.builds(
    TracedOpaqueBehavior,
)
umlTrace_uml_TracedFunctionBehavior_strategy = st.builds(
    umlTrace_uml_TracedFunctionBehavior,
)
uml_TracedStructuredClassifier_strategy = st.builds(
    uml_TracedStructuredClassifier,
)
TracedMultiplicityElement_strategy = st.builds(
    TracedMultiplicityElement,
)
umlTrace_uml_TracedConnectorEnd_strategy = st.builds(
    umlTrace_uml_TracedConnectorEnd,
)
umlTrace_uml_TracedActionExecutionSpecification_strategy = st.builds(
    umlTrace_uml_TracedActionExecutionSpecification,
)
TracedObjectNode_strategy = st.builds(
    TracedObjectNode,
)
umlTrace_uml_TracedExpansionNode_strategy = st.builds(
    umlTrace_uml_TracedExpansionNode,
)
umlTrace_uml_TracedActivityParameterNode_strategy = st.builds(
    umlTrace_uml_TracedActivityParameterNode,
)
umlTrace_uml_TracedCentralBufferNode_strategy = st.builds(
    umlTrace_uml_TracedCentralBufferNode,
)
TracedCentralBufferNode_strategy = st.builds(
    TracedCentralBufferNode,
)
umlTrace_uml_TracedDataStoreNode_strategy = st.builds(
    umlTrace_uml_TracedDataStoreNode,
)
TracedDataType_strategy = st.builds(
    TracedDataType,
)
umlTrace_uml_TracedEnumeration_strategy = st.builds(
    umlTrace_uml_TracedEnumeration,
)
umlTrace_uml_TracedPrimitiveType_strategy = st.builds(
    umlTrace_uml_TracedPrimitiveType,
)
TracedMessageEvent_strategy = st.builds(
    TracedMessageEvent,
)
umlTrace_uml_TracedCallEvent_strategy = st.builds(
    umlTrace_uml_TracedCallEvent,
)
uml_ActivityContent_strategy = st.builds(
    uml_ActivityContent,
)
BasicActions_TracedActionActivation_strategy = st.builds(
    BasicActions_TracedActionActivation,
)
umlTrace_Values_ActionActivation_firing_Value_strategy = st.builds(
    umlTrace_Values_ActionActivation_firing_Value,
    firing=
        safe_text
)
TracedLiteralEvaluation_strategy = st.builds(
    TracedLiteralEvaluation,
)
umlTrace_Kernel_TracedLiteralIntegerEvaluation_strategy = st.builds(
    umlTrace_Kernel_TracedLiteralIntegerEvaluation,
)
umlTrace_Kernel_TracedLiteralBooleanEvaluation_strategy = st.builds(
    umlTrace_Kernel_TracedLiteralBooleanEvaluation,
)
TracedPrimitiveValue_strategy = st.builds(
    TracedPrimitiveValue,
)
umlTrace_Kernel_TracedBooleanValue_strategy = st.builds(
    umlTrace_Kernel_TracedBooleanValue,
)
umlTrace_Kernel_TracedIntegerValue_strategy = st.builds(
    umlTrace_Kernel_TracedIntegerValue,
)
umlTrace_Kernel_TracedEvaluation_strategy = st.builds(
    umlTrace_Kernel_TracedEvaluation,
)
TracedEvaluation_strategy = st.builds(
    TracedEvaluation,
)
umlTrace_Kernel_TracedLiteralEvaluation_strategy = st.builds(
    umlTrace_Kernel_TracedLiteralEvaluation,
)
umlTrace_Kernel_TracedValue_strategy = st.builds(
    umlTrace_Kernel_TracedValue,
)
TracedValue_strategy = st.builds(
    TracedValue,
)
umlTrace_Kernel_TracedPrimitiveValue_strategy = st.builds(
    umlTrace_Kernel_TracedPrimitiveValue,
)
umlTrace_Kernel_TracedStructuredValue_strategy = st.builds(
    umlTrace_Kernel_TracedStructuredValue,
)
TracedStructuredValue_strategy = st.builds(
    TracedStructuredValue,
)
umlTrace_Kernel_TracedReference_strategy = st.builds(
    umlTrace_Kernel_TracedReference,
)
umlTrace_Kernel_TracedCompoundValue_strategy = st.builds(
    umlTrace_Kernel_TracedCompoundValue,
)
TracedCompoundValue_strategy = st.builds(
    TracedCompoundValue,
)
umlTrace_Kernel_TracedExtensionalValue_strategy = st.builds(
    umlTrace_Kernel_TracedExtensionalValue,
)
TracedExtensionalValue_strategy = st.builds(
    TracedExtensionalValue,
)
umlTrace_Kernel_TracedObject_strategy = st.builds(
    umlTrace_Kernel_TracedObject,
)
umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution_strategy = st.builds(
    umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution,
)
TracedObject_strategy = st.builds(
    TracedObject,
)
umlTrace_BasicBehaviors_TracedExecution_strategy = st.builds(
    umlTrace_BasicBehaviors_TracedExecution,
)
uml_TracedElement_strategy = st.builds(
    uml_TracedElement,
)
umlTrace_Values_SemanticVisitor_runtimeModelElement_Value_strategy = st.builds(
    umlTrace_Values_SemanticVisitor_runtimeModelElement_Value,
)
TracedOpaqueBehaviorExecution_strategy = st.builds(
    TracedOpaqueBehaviorExecution,
)
umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_strategy = st.builds(
    umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution,
)
umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_strategy = st.builds(
    umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution,
)
umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_strategy = st.builds(
    umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution,
)
TracedCallActionActivation_strategy = st.builds(
    TracedCallActionActivation,
)
umlTrace_BasicActions_TracedCallBehaviorActionActivation_strategy = st.builds(
    umlTrace_BasicActions_TracedCallBehaviorActionActivation,
)
TracedPinActivation_strategy = st.builds(
    TracedPinActivation,
)
umlTrace_BasicActions_TracedOutputPinActivation_strategy = st.builds(
    umlTrace_BasicActions_TracedOutputPinActivation,
)
umlTrace_BasicActions_TracedInputPinActivation_strategy = st.builds(
    umlTrace_BasicActions_TracedInputPinActivation,
)
TracedInvocationActionActivation_strategy = st.builds(
    TracedInvocationActionActivation,
)
umlTrace_BasicActions_TracedCallActionActivation_strategy = st.builds(
    umlTrace_BasicActions_TracedCallActionActivation,
)
TracedActionActivation_strategy = st.builds(
    TracedActionActivation,
)
umlTrace_BasicActions_TracedOpaqueActionActivation_strategy = st.builds(
    umlTrace_BasicActions_TracedOpaqueActionActivation,
)
umlTrace_BasicActions_TracedInvocationActionActivation_strategy = st.builds(
    umlTrace_BasicActions_TracedInvocationActionActivation,
)
umlTrace_BasicActions_TracedActionActivation_strategy = st.builds(
    umlTrace_BasicActions_TracedActionActivation,
)
umlTrace_Loci_TracedSemanticVisitor_strategy = st.builds(
    umlTrace_Loci_TracedSemanticVisitor,
)
umlTrace_IntermediateActivities_TracedDecisionNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedDecisionNodeActivation,
)
umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation,
)
umlTrace_IntermediateActivities_TracedJoinNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedJoinNodeActivation,
)
TracedObjectNodeActivation_strategy = st.builds(
    TracedObjectNodeActivation,
)
umlTrace_BasicActions_TracedPinActivation_strategy = st.builds(
    umlTrace_BasicActions_TracedPinActivation,
)
umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation,
)
umlTrace_IntermediateActions_TracedCreateObjectActionActivation_strategy = st.builds(
    umlTrace_IntermediateActions_TracedCreateObjectActionActivation,
)
umlTrace_IntermediateActions_TracedValueSpecificationActionActivation_strategy = st.builds(
    umlTrace_IntermediateActions_TracedValueSpecificationActionActivation,
)
TracedWriteStructuralFeatureActionActivation_strategy = st.builds(
    TracedWriteStructuralFeatureActionActivation,
)
umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation_strategy = st.builds(
    umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation,
)
TracedStructuralFeatureActionActivation_strategy = st.builds(
    TracedStructuralFeatureActionActivation,
)
umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation_strategy = st.builds(
    umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation,
)
umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation_strategy = st.builds(
    umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation,
)
umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation_strategy = st.builds(
    umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation,
)
umlTrace_ecore_TracedEModelElement_strategy = st.builds(
    umlTrace_ecore_TracedEModelElement,
)
TracedMessageEnd_strategy = st.builds(
    TracedMessageEnd,
)
umlTrace_uml_TracedGate_strategy = st.builds(
    umlTrace_uml_TracedGate,
)
uml_TracedAction_strategy = st.builds(
    uml_TracedAction,
)
TracedStructuredActivityNode_strategy = st.builds(
    TracedStructuredActivityNode,
)
umlTrace_uml_TracedConditionalNode_strategy = st.builds(
    umlTrace_uml_TracedConditionalNode,
)
TracedEModelElement_strategy = st.builds(
    TracedEModelElement,
)
umlTrace_uml_TracedElement_strategy = st.builds(
    umlTrace_uml_TracedElement,
)
TracedElement_strategy = st.builds(
    TracedElement,
)
umlTrace_uml_TracedTemplateParameterSubstitution_strategy = st.builds(
    umlTrace_uml_TracedTemplateParameterSubstitution,
)
umlTrace_uml_TracedQualifierValue_strategy = st.builds(
    umlTrace_uml_TracedQualifierValue,
)
umlTrace_uml_TracedComment_strategy = st.builds(
    umlTrace_uml_TracedComment,
)
umlTrace_uml_TracedClause_strategy = st.builds(
    umlTrace_uml_TracedClause,
)
umlTrace_uml_TracedNamedElement_strategy = st.builds(
    umlTrace_uml_TracedNamedElement,
)
TracedNamedElement_strategy = st.builds(
    TracedNamedElement,
)
umlTrace_uml_TracedGeneralOrdering_strategy = st.builds(
    umlTrace_uml_TracedGeneralOrdering,
)
umlTrace_uml_TracedParameterSet_strategy = st.builds(
    umlTrace_uml_TracedParameterSet,
)
umlTrace_uml_TracedInteractionFragment_strategy = st.builds(
    umlTrace_uml_TracedInteractionFragment,
)
uml_TracedMessageEnd_strategy = st.builds(
    uml_TracedMessageEnd,
)
TracedMessageOccurrenceSpecification_strategy = st.builds(
    TracedMessageOccurrenceSpecification,
)
umlTrace_uml_TracedDestructionOccurrenceSpecification_strategy = st.builds(
    umlTrace_uml_TracedDestructionOccurrenceSpecification,
)
umlTrace_uml_TracedVertex_strategy = st.builds(
    umlTrace_uml_TracedVertex,
)
TracedVertex_strategy = st.builds(
    TracedVertex,
)
umlTrace_uml_TracedConnectionPointReference_strategy = st.builds(
    umlTrace_uml_TracedConnectionPointReference,
)
umlTrace_uml_TracedPseudostate_strategy = st.builds(
    umlTrace_uml_TracedPseudostate,
)
umlTrace_uml_TracedParameterableElement_strategy = st.builds(
    umlTrace_uml_TracedParameterableElement,
)
uml_TracedParameterableElement_strategy = st.builds(
    uml_TracedParameterableElement,
)
TracedPackageableElement_strategy = st.builds(
    TracedPackageableElement,
)
umlTrace_uml_TracedConstraint_strategy = st.builds(
    umlTrace_uml_TracedConstraint,
)
TracedConstraint_strategy = st.builds(
    TracedConstraint,
)
umlTrace_uml_TracedInteractionConstraint_strategy = st.builds(
    umlTrace_uml_TracedInteractionConstraint,
)
umlTrace_uml_TracedIntervalConstraint_strategy = st.builds(
    umlTrace_uml_TracedIntervalConstraint,
)
TracedIntervalConstraint_strategy = st.builds(
    TracedIntervalConstraint,
)
umlTrace_uml_TracedDurationConstraint_strategy = st.builds(
    umlTrace_uml_TracedDurationConstraint,
)
uml_TracedControlFlow_strategy = st.builds(
    uml_TracedControlFlow,
)
uml_TracedTimeObservation_strategy = st.builds(
    uml_TracedTimeObservation,
)
uml_TracedGate_strategy = st.builds(
    uml_TracedGate,
)
uml_TracedActivityFinalNode_strategy = st.builds(
    uml_TracedActivityFinalNode,
)
uml_TracedClassifierTemplateParameter_strategy = st.builds(
    uml_TracedClassifierTemplateParameter,
)
TracedInteractionFragment_strategy = st.builds(
    TracedInteractionFragment,
)
umlTrace_uml_TracedOccurrenceSpecification_strategy = st.builds(
    umlTrace_uml_TracedOccurrenceSpecification,
)
umlTrace_uml_TracedCombinedFragment_strategy = st.builds(
    umlTrace_uml_TracedCombinedFragment,
)
uml_TracedGeneralOrdering_strategy = st.builds(
    uml_TracedGeneralOrdering,
)
uml_TracedElementImport_strategy = st.builds(
    uml_TracedElementImport,
)
uml_TracedMergeNode_strategy = st.builds(
    uml_TracedMergeNode,
)
uml_TracedClearAssociationAction_strategy = st.builds(
    uml_TracedClearAssociationAction,
)
uml_TracedLinkEndCreationData_strategy = st.builds(
    uml_TracedLinkEndCreationData,
)
uml_TracedPseudostate_strategy = st.builds(
    uml_TracedPseudostate,
)
uml_TracedComponent_strategy = st.builds(
    uml_TracedComponent,
)
uml_TracedReadIsClassifiedObjectAction_strategy = st.builds(
    uml_TracedReadIsClassifiedObjectAction,
)
uml_TracedAbstraction_strategy = st.builds(
    uml_TracedAbstraction,
)
uml_TracedTimeExpression_strategy = st.builds(
    uml_TracedTimeExpression,
)
uml_TracedValueSpecificationAction_strategy = st.builds(
    uml_TracedValueSpecificationAction,
)
uml_TracedFunctionBehavior_strategy = st.builds(
    uml_TracedFunctionBehavior,
)
IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_strategy = st.builds(
    IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution,
)
IntermediateActivities_TracedMergeNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedMergeNodeActivation,
)
uml_TracedTemplateParameter_strategy = st.builds(
    uml_TracedTemplateParameter,
)
uml_TracedManifestation_strategy = st.builds(
    uml_TracedManifestation,
)
uml_TracedActor_strategy = st.builds(
    uml_TracedActor,
)
uml_TracedRemoveVariableValueAction_strategy = st.builds(
    uml_TracedRemoveVariableValueAction,
)
uml_TracedProfile_strategy = st.builds(
    uml_TracedProfile,
)
uml_TracedTestIdentityAction_strategy = st.builds(
    uml_TracedTestIdentityAction,
)
uml_TracedCollaboration_strategy = st.builds(
    uml_TracedCollaboration,
)
uml_TracedSendSignalAction_strategy = st.builds(
    uml_TracedSendSignalAction,
)
uml_TracedInterfaceRealization_strategy = st.builds(
    uml_TracedInterfaceRealization,
)
uml_TracedUnmarshallAction_strategy = st.builds(
    uml_TracedUnmarshallAction,
)
uml_TracedExpression_strategy = st.builds(
    uml_TracedExpression,
)
uml_TracedAssociation_strategy = st.builds(
    uml_TracedAssociation,
)
uml_TracedClearStructuralFeatureAction_strategy = st.builds(
    uml_TracedClearStructuralFeatureAction,
)
uml_TracedAddVariableValueAction_strategy = st.builds(
    uml_TracedAddVariableValueAction,
)
uml_TracedLiteralReal_strategy = st.builds(
    uml_TracedLiteralReal,
)
IntermediateActions_TracedCreateObjectActionActivation_strategy = st.builds(
    IntermediateActions_TracedCreateObjectActionActivation,
)
uml_TracedSlot_strategy = st.builds(
    uml_TracedSlot,
)
uml_TracedLiteralNull_strategy = st.builds(
    uml_TracedLiteralNull,
)
IntermediateActions_TracedValueSpecificationActionActivation_strategy = st.builds(
    IntermediateActions_TracedValueSpecificationActionActivation,
)
uml_TracedStartObjectBehaviorAction_strategy = st.builds(
    uml_TracedStartObjectBehaviorAction,
)
uml_TracedLiteralBoolean_strategy = st.builds(
    uml_TracedLiteralBoolean,
)
uml_TracedReadLinkAction_strategy = st.builds(
    uml_TracedReadLinkAction,
)
uml_TracedInclude_strategy = st.builds(
    uml_TracedInclude,
)
uml_TracedRegion_strategy = st.builds(
    uml_TracedRegion,
)
uml_TracedState_strategy = st.builds(
    uml_TracedState,
)
uml_TracedPrimitiveType_strategy = st.builds(
    uml_TracedPrimitiveType,
)
uml_TracedStringExpression_strategy = st.builds(
    uml_TracedStringExpression,
)
uml_TracedLinkEndDestructionData_strategy = st.builds(
    uml_TracedLinkEndDestructionData,
)
umlTrace_uml_TracedAnyReceiveEvent_strategy = st.builds(
    umlTrace_uml_TracedAnyReceiveEvent,
)
uml_TracedReadExtentAction_strategy = st.builds(
    uml_TracedReadExtentAction,
)
BasicActions_TracedOutputPinActivation_strategy = st.builds(
    BasicActions_TracedOutputPinActivation,
)
uml_TracedBehavioralFeature_strategy = st.builds(
    uml_TracedBehavioralFeature,
)
uml_TracedTemplateSignature_strategy = st.builds(
    uml_TracedTemplateSignature,
)
umlTrace_uml_TracedTemplateParameter_strategy = st.builds(
    umlTrace_uml_TracedTemplateParameter,
)
TracedTemplateParameter_strategy = st.builds(
    TracedTemplateParameter,
)
umlTrace_uml_TracedConnectableElementTemplateParameter_strategy = st.builds(
    umlTrace_uml_TracedConnectableElementTemplateParameter,
)
umlTrace_uml_TracedClassifierTemplateParameter_strategy = st.builds(
    umlTrace_uml_TracedClassifierTemplateParameter,
)
TracedPackage_strategy = st.builds(
    TracedPackage,
)
umlTrace_uml_TracedProfile_strategy = st.builds(
    umlTrace_uml_TracedProfile,
)
umlTrace_uml_TracedModel_strategy = st.builds(
    umlTrace_uml_TracedModel,
)
umlTrace_uml_TracedImage_strategy = st.builds(
    umlTrace_uml_TracedImage,
)
TracedTransition_strategy = st.builds(
    TracedTransition,
)
umlTrace_uml_TracedProtocolTransition_strategy = st.builds(
    umlTrace_uml_TracedProtocolTransition,
)
TracedWriteVariableAction_strategy = st.builds(
    TracedWriteVariableAction,
)
umlTrace_uml_TracedRemoveVariableValueAction_strategy = st.builds(
    umlTrace_uml_TracedRemoveVariableValueAction,
)
umlTrace_uml_TracedAddVariableValueAction_strategy = st.builds(
    umlTrace_uml_TracedAddVariableValueAction,
)
TracedInteractionUse_strategy = st.builds(
    TracedInteractionUse,
)
umlTrace_uml_TracedPartDecomposition_strategy = st.builds(
    umlTrace_uml_TracedPartDecomposition,
)
TracedObservation_strategy = st.builds(
    TracedObservation,
)
umlTrace_uml_TracedTimeObservation_strategy = st.builds(
    umlTrace_uml_TracedTimeObservation,
)
umlTrace_uml_TracedDurationObservation_strategy = st.builds(
    umlTrace_uml_TracedDurationObservation,
)
umlTrace_uml_TracedOperationTemplateParameter_strategy = st.builds(
    umlTrace_uml_TracedOperationTemplateParameter,
)
TracedInterval_strategy = st.builds(
    TracedInterval,
)
umlTrace_uml_TracedDurationInterval_strategy = st.builds(
    umlTrace_uml_TracedDurationInterval,
)
umlTrace_uml_TracedTimeInterval_strategy = st.builds(
    umlTrace_uml_TracedTimeInterval,
)
umlTrace_uml_TracedSignalEvent_strategy = st.builds(
    umlTrace_uml_TracedSignalEvent,
)
TracedBehavioralFeature_strategy = st.builds(
    TracedBehavioralFeature,
)
umlTrace_uml_TracedReception_strategy = st.builds(
    umlTrace_uml_TracedReception,
)
umlTrace_uml_TracedExecutionSpecification_strategy = st.builds(
    umlTrace_uml_TracedExecutionSpecification,
)
TracedDependency_strategy = st.builds(
    TracedDependency,
)
umlTrace_uml_TracedUsage_strategy = st.builds(
    umlTrace_uml_TracedUsage,
)
umlTrace_uml_TracedAbstraction_strategy = st.builds(
    umlTrace_uml_TracedAbstraction,
)
TracedAbstraction_strategy = st.builds(
    TracedAbstraction,
)
umlTrace_uml_TracedManifestation_strategy = st.builds(
    umlTrace_uml_TracedManifestation,
)
umlTrace_uml_TracedRealization_strategy = st.builds(
    umlTrace_uml_TracedRealization,
)
TracedRealization_strategy = st.builds(
    TracedRealization,
)
umlTrace_uml_TracedComponentRealization_strategy = st.builds(
    umlTrace_uml_TracedComponentRealization,
)
umlTrace_uml_TracedInterfaceRealization_strategy = st.builds(
    umlTrace_uml_TracedInterfaceRealization,
)
umlTrace_uml_TracedSubstitution_strategy = st.builds(
    umlTrace_uml_TracedSubstitution,
)
TracedInstanceSpecification_strategy = st.builds(
    TracedInstanceSpecification,
)
umlTrace_uml_TracedEnumerationLiteral_strategy = st.builds(
    umlTrace_uml_TracedEnumerationLiteral,
)
TracedAcceptEventAction_strategy = st.builds(
    TracedAcceptEventAction,
)
umlTrace_uml_TracedAcceptCallAction_strategy = st.builds(
    umlTrace_uml_TracedAcceptCallAction,
)
umlTrace_uml_TracedLinkEndData_strategy = st.builds(
    umlTrace_uml_TracedLinkEndData,
)
TracedLinkEndData_strategy = st.builds(
    TracedLinkEndData,
)
umlTrace_uml_TracedLinkEndCreationData_strategy = st.builds(
    umlTrace_uml_TracedLinkEndCreationData,
)
umlTrace_uml_TracedLinkEndDestructionData_strategy = st.builds(
    umlTrace_uml_TracedLinkEndDestructionData,
)
umlTrace_uml_TracedTemplateSignature_strategy = st.builds(
    umlTrace_uml_TracedTemplateSignature,
)
umlTrace_uml_TracedStateInvariant_strategy = st.builds(
    umlTrace_uml_TracedStateInvariant,
)
umlTrace_uml_TracedTrigger_strategy = st.builds(
    umlTrace_uml_TracedTrigger,
)
umlTrace_uml_TracedSlot_strategy = st.builds(
    umlTrace_uml_TracedSlot,
)
TracedClass_strategy = st.builds(
    TracedClass,
)
umlTrace_uml_TracedStereotype_strategy = st.builds(
    umlTrace_uml_TracedStereotype,
)
umlTrace_uml_TracedComponent_strategy = st.builds(
    umlTrace_uml_TracedComponent,
)
umlTrace_uml_TracedBehavior_strategy = st.builds(
    umlTrace_uml_TracedBehavior,
)
uml_TracedInteractionFragment_strategy = st.builds(
    uml_TracedInteractionFragment,
)
uml_TracedBehavior_strategy = st.builds(
    uml_TracedBehavior,
)
umlTrace_uml_TracedInteraction_strategy = st.builds(
    umlTrace_uml_TracedInteraction,
)
TracedActivityEdge_strategy = st.builds(
    TracedActivityEdge,
)
umlTrace_uml_TracedControlFlow_strategy = st.builds(
    umlTrace_uml_TracedControlFlow,
)
umlTrace_uml_TracedObjectFlow_strategy = st.builds(
    umlTrace_uml_TracedObjectFlow,
)
TracedStateMachine_strategy = st.builds(
    TracedStateMachine,
)
umlTrace_uml_TracedProtocolStateMachine_strategy = st.builds(
    umlTrace_uml_TracedProtocolStateMachine,
)
umlTrace_uml_TracedDeployment_strategy = st.builds(
    umlTrace_uml_TracedDeployment,
)
umlTrace_uml_TracedMessage_strategy = st.builds(
    umlTrace_uml_TracedMessage,
)
TracedBehavior_strategy = st.builds(
    TracedBehavior,
)
umlTrace_uml_TracedOpaqueBehavior_strategy = st.builds(
    umlTrace_uml_TracedOpaqueBehavior,
)
umlTrace_uml_TracedActivity_strategy = st.builds(
    umlTrace_uml_TracedActivity,
)
umlTrace_uml_TracedStateMachine_strategy = st.builds(
    umlTrace_uml_TracedStateMachine,
)
TracedActivityGroup_strategy = st.builds(
    TracedActivityGroup,
)
umlTrace_uml_TracedInterruptibleActivityRegion_strategy = st.builds(
    umlTrace_uml_TracedInterruptibleActivityRegion,
)
umlTrace_uml_TracedActivityPartition_strategy = st.builds(
    umlTrace_uml_TracedActivityPartition,
)
uml_TracedRelationship_strategy = st.builds(
    uml_TracedRelationship,
)
TracedAssociation_strategy = st.builds(
    TracedAssociation,
)
umlTrace_uml_TracedCommunicationPath_strategy = st.builds(
    umlTrace_uml_TracedCommunicationPath,
)
umlTrace_uml_TracedExtension_strategy = st.builds(
    umlTrace_uml_TracedExtension,
)
TracedStructuralFeatureAction_strategy = st.builds(
    TracedStructuralFeatureAction,
)
umlTrace_uml_TracedReadStructuralFeatureAction_strategy = st.builds(
    umlTrace_uml_TracedReadStructuralFeatureAction,
)
umlTrace_uml_TracedClearStructuralFeatureAction_strategy = st.builds(
    umlTrace_uml_TracedClearStructuralFeatureAction,
)
umlTrace_uml_TracedWriteStructuralFeatureAction_strategy = st.builds(
    umlTrace_uml_TracedWriteStructuralFeatureAction,
)
TracedWriteStructuralFeatureAction_strategy = st.builds(
    TracedWriteStructuralFeatureAction,
)
umlTrace_uml_TracedAddStructuralFeatureValueAction_strategy = st.builds(
    umlTrace_uml_TracedAddStructuralFeatureValueAction,
)
umlTrace_uml_TracedRemoveStructuralFeatureValueAction_strategy = st.builds(
    umlTrace_uml_TracedRemoveStructuralFeatureValueAction,
)
TracedBehavioredClassifier_strategy = st.builds(
    TracedBehavioredClassifier,
)
umlTrace_uml_TracedActor_strategy = st.builds(
    umlTrace_uml_TracedActor,
)
umlTrace_uml_TracedUseCase_strategy = st.builds(
    umlTrace_uml_TracedUseCase,
)
umlTrace_uml_TracedSequenceNode_strategy = st.builds(
    umlTrace_uml_TracedSequenceNode,
)
umlTrace_uml_TracedExceptionHandler_strategy = st.builds(
    umlTrace_uml_TracedExceptionHandler,
)
umlTrace_uml_TracedDeployedArtifact_strategy = st.builds(
    umlTrace_uml_TracedDeployedArtifact,
)
uml_TracedDeployedArtifact_strategy = st.builds(
    uml_TracedDeployedArtifact,
)
uml_TracedClassifier_strategy = st.builds(
    uml_TracedClassifier,
)
umlTrace_uml_TracedAssociation_strategy = st.builds(
    umlTrace_uml_TracedAssociation,
)
umlTrace_uml_TracedArtifact_strategy = st.builds(
    umlTrace_uml_TracedArtifact,
)
TracedArtifact_strategy = st.builds(
    TracedArtifact,
)
umlTrace_uml_TracedDeploymentSpecification_strategy = st.builds(
    umlTrace_uml_TracedDeploymentSpecification,
)
uml_TracedActivityNode_strategy = st.builds(
    uml_TracedActivityNode,
)
uml_TracedObjectNode_strategy = st.builds(
    uml_TracedObjectNode,
)
TracedPin_strategy = st.builds(
    TracedPin,
)
umlTrace_uml_TracedOutputPin_strategy = st.builds(
    umlTrace_uml_TracedOutputPin,
)
umlTrace_uml_TracedInputPin_strategy = st.builds(
    umlTrace_uml_TracedInputPin,
)
TracedInputPin_strategy = st.builds(
    TracedInputPin,
)
umlTrace_uml_TracedActionInputPin_strategy = st.builds(
    umlTrace_uml_TracedActionInputPin,
)
umlTrace_uml_TracedValuePin_strategy = st.builds(
    umlTrace_uml_TracedValuePin,
)
umlTrace_uml_TracedCollaborationUse_strategy = st.builds(
    umlTrace_uml_TracedCollaborationUse,
)
umlTrace_uml_TracedDeploymentTarget_strategy = st.builds(
    umlTrace_uml_TracedDeploymentTarget,
)
umlTrace_uml_TracedMultiplicityElement_strategy = st.builds(
    umlTrace_uml_TracedMultiplicityElement,
)
umlTrace_uml_TracedTypedElement_strategy = st.builds(
    umlTrace_uml_TracedTypedElement,
)
uml_TracedMultiplicityElement_strategy = st.builds(
    uml_TracedMultiplicityElement,
)
umlTrace_uml_TracedPin_strategy = st.builds(
    umlTrace_uml_TracedPin,
)
uml_TracedTypedElement_strategy = st.builds(
    uml_TracedTypedElement,
)
umlTrace_uml_TracedConnectableElement_strategy = st.builds(
    umlTrace_uml_TracedConnectableElement,
)
umlTrace_uml_TracedObjectNode_strategy = st.builds(
    umlTrace_uml_TracedObjectNode,
)
uml_TracedFeature_strategy = st.builds(
    uml_TracedFeature,
)
umlTrace_uml_TracedStructuralFeature_strategy = st.builds(
    umlTrace_uml_TracedStructuralFeature,
)
TracedValueSpecification_strategy = st.builds(
    TracedValueSpecification,
)
umlTrace_uml_TracedOpaqueExpression_strategy = st.builds(
    umlTrace_uml_TracedOpaqueExpression,
)
umlTrace_uml_TracedTimeExpression_strategy = st.builds(
    umlTrace_uml_TracedTimeExpression,
)
umlTrace_uml_TracedInterval_strategy = st.builds(
    umlTrace_uml_TracedInterval,
)
umlTrace_uml_TracedExpression_strategy = st.builds(
    umlTrace_uml_TracedExpression,
)
umlTrace_uml_TracedInstanceValue_strategy = st.builds(
    umlTrace_uml_TracedInstanceValue,
)
umlTrace_uml_TracedDuration_strategy = st.builds(
    umlTrace_uml_TracedDuration,
)
umlTrace_uml_TracedLiteralSpecification_strategy = st.builds(
    umlTrace_uml_TracedLiteralSpecification,
)
TracedLiteralSpecification_strategy = st.builds(
    TracedLiteralSpecification,
)
umlTrace_uml_TracedLiteralUnlimitedNatural_strategy = st.builds(
    umlTrace_uml_TracedLiteralUnlimitedNatural,
)
umlTrace_uml_TracedLiteralNull_strategy = st.builds(
    umlTrace_uml_TracedLiteralNull,
)
umlTrace_uml_TracedLiteralReal_strategy = st.builds(
    umlTrace_uml_TracedLiteralReal,
)
umlTrace_uml_TracedLiteralBoolean_strategy = st.builds(
    umlTrace_uml_TracedLiteralBoolean,
)
umlTrace_uml_TracedLiteralInteger_strategy = st.builds(
    umlTrace_uml_TracedLiteralInteger,
)
umlTrace_uml_TracedLiteralString_strategy = st.builds(
    umlTrace_uml_TracedLiteralString,
)
TracedVariableAction_strategy = st.builds(
    TracedVariableAction,
)
umlTrace_uml_TracedReadVariableAction_strategy = st.builds(
    umlTrace_uml_TracedReadVariableAction,
)
umlTrace_uml_TracedWriteVariableAction_strategy = st.builds(
    umlTrace_uml_TracedWriteVariableAction,
)
umlTrace_uml_TracedClearVariableAction_strategy = st.builds(
    umlTrace_uml_TracedClearVariableAction,
)
umlTrace_uml_TracedTimeConstraint_strategy = st.builds(
    umlTrace_uml_TracedTimeConstraint,
)
umlTrace_uml_TracedContinuation_strategy = st.builds(
    umlTrace_uml_TracedContinuation,
)
TracedCombinedFragment_strategy = st.builds(
    TracedCombinedFragment,
)
umlTrace_uml_TracedConsiderIgnoreFragment_strategy = st.builds(
    umlTrace_uml_TracedConsiderIgnoreFragment,
)
TracedNode_strategy = st.builds(
    TracedNode,
)
umlTrace_uml_TracedDevice_strategy = st.builds(
    umlTrace_uml_TracedDevice,
)
umlTrace_uml_TracedExecutionEnvironment_strategy = st.builds(
    umlTrace_uml_TracedExecutionEnvironment,
)
umlTrace_uml_TracedType_strategy = st.builds(
    umlTrace_uml_TracedType,
)
uml_TracedType_strategy = st.builds(
    uml_TracedType,
)
TracedClassifier_strategy = st.builds(
    TracedClassifier,
)
umlTrace_uml_TracedDataType_strategy = st.builds(
    umlTrace_uml_TracedDataType,
)
umlTrace_uml_TracedInformationItem_strategy = st.builds(
    umlTrace_uml_TracedInformationItem,
)
umlTrace_uml_TracedInterface_strategy = st.builds(
    umlTrace_uml_TracedInterface,
)
umlTrace_uml_TracedBehavioredClassifier_strategy = st.builds(
    umlTrace_uml_TracedBehavioredClassifier,
)
umlTrace_uml_TracedStructuredClassifier_strategy = st.builds(
    umlTrace_uml_TracedStructuredClassifier,
)
TracedStructuredClassifier_strategy = st.builds(
    TracedStructuredClassifier,
)
umlTrace_uml_TracedEncapsulatedClassifier_strategy = st.builds(
    umlTrace_uml_TracedEncapsulatedClassifier,
)
uml_TracedBehavioredClassifier_strategy = st.builds(
    uml_TracedBehavioredClassifier,
)
umlTrace_uml_TracedCollaboration_strategy = st.builds(
    umlTrace_uml_TracedCollaboration,
)
uml_TracedEncapsulatedClassifier_strategy = st.builds(
    uml_TracedEncapsulatedClassifier,
)
umlTrace_uml_TracedClass_strategy = st.builds(
    umlTrace_uml_TracedClass,
)
TracedCallAction_strategy = st.builds(
    TracedCallAction,
)
umlTrace_uml_TracedStartObjectBehaviorAction_strategy = st.builds(
    umlTrace_uml_TracedStartObjectBehaviorAction,
)
umlTrace_uml_TracedCallOperationAction_strategy = st.builds(
    umlTrace_uml_TracedCallOperationAction,
)
umlTrace_uml_TracedCallBehaviorAction_strategy = st.builds(
    umlTrace_uml_TracedCallBehaviorAction,
)
umlTrace_uml_TracedRelationship_strategy = st.builds(
    umlTrace_uml_TracedRelationship,
)
TracedRelationship_strategy = st.builds(
    TracedRelationship,
)
umlTrace_uml_TracedDirectedRelationship_strategy = st.builds(
    umlTrace_uml_TracedDirectedRelationship,
)
TracedDirectedRelationship_strategy = st.builds(
    TracedDirectedRelationship,
)
umlTrace_uml_TracedGeneralization_strategy = st.builds(
    umlTrace_uml_TracedGeneralization,
)
umlTrace_uml_TracedElementImport_strategy = st.builds(
    umlTrace_uml_TracedElementImport,
)
umlTrace_uml_TracedProfileApplication_strategy = st.builds(
    umlTrace_uml_TracedProfileApplication,
)
umlTrace_uml_TracedPackageMerge_strategy = st.builds(
    umlTrace_uml_TracedPackageMerge,
)
umlTrace_uml_TracedTemplateBinding_strategy = st.builds(
    umlTrace_uml_TracedTemplateBinding,
)
umlTrace_uml_TracedPackageImport_strategy = st.builds(
    umlTrace_uml_TracedPackageImport,
)
umlTrace_uml_TracedProtocolConformance_strategy = st.builds(
    umlTrace_uml_TracedProtocolConformance,
)
TracedInvocationAction_strategy = st.builds(
    TracedInvocationAction,
)
umlTrace_uml_TracedCallAction_strategy = st.builds(
    umlTrace_uml_TracedCallAction,
)
umlTrace_uml_TracedBroadcastSignalAction_strategy = st.builds(
    umlTrace_uml_TracedBroadcastSignalAction,
)
umlTrace_uml_TracedSendSignalAction_strategy = st.builds(
    umlTrace_uml_TracedSendSignalAction,
)
umlTrace_uml_TracedSendObjectAction_strategy = st.builds(
    umlTrace_uml_TracedSendObjectAction,
)
TracedRedefinableElement_strategy = st.builds(
    TracedRedefinableElement,
)
umlTrace_uml_TracedExtensionPoint_strategy = st.builds(
    umlTrace_uml_TracedExtensionPoint,
)
umlTrace_uml_TracedActivityEdge_strategy = st.builds(
    umlTrace_uml_TracedActivityEdge,
)
umlTrace_uml_TracedFeature_strategy = st.builds(
    umlTrace_uml_TracedFeature,
)
TracedFeature_strategy = st.builds(
    TracedFeature,
)
umlTrace_uml_TracedConnector_strategy = st.builds(
    umlTrace_uml_TracedConnector,
)
umlTrace_uml_TracedTemplateableElement_strategy = st.builds(
    umlTrace_uml_TracedTemplateableElement,
)
uml_TracedTemplateableElement_strategy = st.builds(
    uml_TracedTemplateableElement,
)
umlTrace_uml_TracedOperation_strategy = st.builds(
    umlTrace_uml_TracedOperation,
)
umlTrace_uml_TracedStringExpression_strategy = st.builds(
    umlTrace_uml_TracedStringExpression,
)
uml_TracedPackageableElement_strategy = st.builds(
    uml_TracedPackageableElement,
)
umlTrace_uml_TracedValueSpecification_strategy = st.builds(
    umlTrace_uml_TracedValueSpecification,
)
umlTrace_uml_TracedMessageEnd_strategy = st.builds(
    umlTrace_uml_TracedMessageEnd,
)
uml_TracedDeploymentTarget_strategy = st.builds(
    uml_TracedDeploymentTarget,
)
umlTrace_uml_TracedInstanceSpecification_strategy = st.builds(
    umlTrace_uml_TracedInstanceSpecification,
)
uml_TracedConnectableElement_strategy = st.builds(
    uml_TracedConnectableElement,
)
umlTrace_uml_TracedParameter_strategy = st.builds(
    umlTrace_uml_TracedParameter,
)
umlTrace_uml_TracedVariable_strategy = st.builds(
    umlTrace_uml_TracedVariable,
)
uml_TracedStructuralFeature_strategy = st.builds(
    uml_TracedStructuralFeature,
)
umlTrace_uml_TracedProperty_strategy = st.builds(
    umlTrace_uml_TracedProperty,
)
TracedProperty_strategy = st.builds(
    TracedProperty,
)
umlTrace_uml_TracedExtensionEnd_strategy = st.builds(
    umlTrace_uml_TracedExtensionEnd,
)
umlTrace_uml_TracedPort_strategy = st.builds(
    umlTrace_uml_TracedPort,
)
uml_TracedDirectedRelationship_strategy = st.builds(
    uml_TracedDirectedRelationship,
)
umlTrace_uml_TracedInformationFlow_strategy = st.builds(
    umlTrace_uml_TracedInformationFlow,
)
umlTrace_uml_TracedDependency_strategy = st.builds(
    umlTrace_uml_TracedDependency,
)
umlTrace_uml_TracedEvent_strategy = st.builds(
    umlTrace_uml_TracedEvent,
)
TracedEvent_strategy = st.builds(
    TracedEvent,
)
umlTrace_uml_TracedMessageEvent_strategy = st.builds(
    umlTrace_uml_TracedMessageEvent,
)
umlTrace_uml_TracedTimeEvent_strategy = st.builds(
    umlTrace_uml_TracedTimeEvent,
)
umlTrace_uml_TracedChangeEvent_strategy = st.builds(
    umlTrace_uml_TracedChangeEvent,
)
umlTrace_uml_TracedGeneralizationSet_strategy = st.builds(
    umlTrace_uml_TracedGeneralizationSet,
)
umlTrace_uml_TracedSignal_strategy = st.builds(
    umlTrace_uml_TracedSignal,
)
umlTrace_uml_TracedLoopNode_strategy = st.builds(
    umlTrace_uml_TracedLoopNode,
)
umlTrace_uml_TracedInteractionUse_strategy = st.builds(
    umlTrace_uml_TracedInteractionUse,
)
umlTrace_uml_TracedObservation_strategy = st.builds(
    umlTrace_uml_TracedObservation,
)
umlTrace_uml_TracedLifeline_strategy = st.builds(
    umlTrace_uml_TracedLifeline,
)
umlTrace_uml_TracedExpansionRegion_strategy = st.builds(
    umlTrace_uml_TracedExpansionRegion,
)
TracedFinalNode_strategy = st.builds(
    TracedFinalNode,
)
umlTrace_uml_TracedActivityFinalNode_strategy = st.builds(
    umlTrace_uml_TracedActivityFinalNode,
)
umlTrace_uml_TracedFlowFinalNode_strategy = st.builds(
    umlTrace_uml_TracedFlowFinalNode,
)
TracedControlNode_strategy = st.builds(
    TracedControlNode,
)
umlTrace_uml_TracedJoinNode_strategy = st.builds(
    umlTrace_uml_TracedJoinNode,
)
umlTrace_uml_TracedMergeNode_strategy = st.builds(
    umlTrace_uml_TracedMergeNode,
)
umlTrace_uml_TracedDecisionNode_strategy = st.builds(
    umlTrace_uml_TracedDecisionNode,
)
umlTrace_uml_TracedFinalNode_strategy = st.builds(
    umlTrace_uml_TracedFinalNode,
)
umlTrace_uml_TracedForkNode_strategy = st.builds(
    umlTrace_uml_TracedForkNode,
)
umlTrace_uml_TracedInitialNode_strategy = st.builds(
    umlTrace_uml_TracedInitialNode,
)
TracedAction_strategy = st.builds(
    TracedAction,
)
umlTrace_uml_TracedReplyAction_strategy = st.builds(
    umlTrace_uml_TracedReplyAction,
)
umlTrace_uml_TracedReadExtentAction_strategy = st.builds(
    umlTrace_uml_TracedReadExtentAction,
)
umlTrace_uml_TracedAcceptEventAction_strategy = st.builds(
    umlTrace_uml_TracedAcceptEventAction,
)
umlTrace_uml_TracedInvocationAction_strategy = st.builds(
    umlTrace_uml_TracedInvocationAction,
)
umlTrace_uml_TracedRaiseExceptionAction_strategy = st.builds(
    umlTrace_uml_TracedRaiseExceptionAction,
)
umlTrace_uml_TracedValueSpecificationAction_strategy = st.builds(
    umlTrace_uml_TracedValueSpecificationAction,
)
umlTrace_uml_TracedClearAssociationAction_strategy = st.builds(
    umlTrace_uml_TracedClearAssociationAction,
)
umlTrace_uml_TracedOpaqueAction_strategy = st.builds(
    umlTrace_uml_TracedOpaqueAction,
)
umlTrace_uml_TracedCreateObjectAction_strategy = st.builds(
    umlTrace_uml_TracedCreateObjectAction,
)
umlTrace_uml_TracedReclassifyObjectAction_strategy = st.builds(
    umlTrace_uml_TracedReclassifyObjectAction,
)
umlTrace_uml_TracedStartClassifierBehaviorAction_strategy = st.builds(
    umlTrace_uml_TracedStartClassifierBehaviorAction,
)
umlTrace_uml_TracedVariableAction_strategy = st.builds(
    umlTrace_uml_TracedVariableAction,
)
umlTrace_uml_TracedReadIsClassifiedObjectAction_strategy = st.builds(
    umlTrace_uml_TracedReadIsClassifiedObjectAction,
)
umlTrace_uml_TracedTestIdentityAction_strategy = st.builds(
    umlTrace_uml_TracedTestIdentityAction,
)
umlTrace_uml_TracedUnmarshallAction_strategy = st.builds(
    umlTrace_uml_TracedUnmarshallAction,
)
umlTrace_uml_TracedReadSelfAction_strategy = st.builds(
    umlTrace_uml_TracedReadSelfAction,
)
umlTrace_uml_TracedReduceAction_strategy = st.builds(
    umlTrace_uml_TracedReduceAction,
)
umlTrace_uml_TracedStructuralFeatureAction_strategy = st.builds(
    umlTrace_uml_TracedStructuralFeatureAction,
)
umlTrace_uml_TracedDestroyObjectAction_strategy = st.builds(
    umlTrace_uml_TracedDestroyObjectAction,
)
umlTrace_uml_TracedReadLinkObjectEndQualifierAction_strategy = st.builds(
    umlTrace_uml_TracedReadLinkObjectEndQualifierAction,
)
umlTrace_uml_TracedReadLinkObjectEndAction_strategy = st.builds(
    umlTrace_uml_TracedReadLinkObjectEndAction,
)
umlTrace_uml_TracedLinkAction_strategy = st.builds(
    umlTrace_uml_TracedLinkAction,
)
TracedLinkAction_strategy = st.builds(
    TracedLinkAction,
)
umlTrace_uml_TracedReadLinkAction_strategy = st.builds(
    umlTrace_uml_TracedReadLinkAction,
)
umlTrace_uml_TracedWriteLinkAction_strategy = st.builds(
    umlTrace_uml_TracedWriteLinkAction,
)
TracedWriteLinkAction_strategy = st.builds(
    TracedWriteLinkAction,
)
umlTrace_uml_TracedDestroyLinkAction_strategy = st.builds(
    umlTrace_uml_TracedDestroyLinkAction,
)
umlTrace_uml_TracedCreateLinkAction_strategy = st.builds(
    umlTrace_uml_TracedCreateLinkAction,
)
TracedCreateLinkAction_strategy = st.builds(
    TracedCreateLinkAction,
)
umlTrace_uml_TracedCreateLinkObjectAction_strategy = st.builds(
    umlTrace_uml_TracedCreateLinkObjectAction,
)
uml_TracedNamedElement_strategy = st.builds(
    uml_TracedNamedElement,
)
umlTrace_uml_TracedExtend_strategy = st.builds(
    umlTrace_uml_TracedExtend,
)
umlTrace_uml_TracedInclude_strategy = st.builds(
    umlTrace_uml_TracedInclude,
)
umlTrace_uml_TracedPackageableElement_strategy = st.builds(
    umlTrace_uml_TracedPackageableElement,
)
umlTrace_uml_TracedNamespace_strategy = st.builds(
    umlTrace_uml_TracedNamespace,
)
umlTrace_uml_TracedRedefinableElement_strategy = st.builds(
    umlTrace_uml_TracedRedefinableElement,
)
ActivityContent_strategy = st.builds(
    ActivityContent,
)
umlTrace_uml_TracedActivityGroup_strategy = st.builds(
    umlTrace_uml_TracedActivityGroup,
)
uml_TracedRedefinableElement_strategy = st.builds(
    uml_TracedRedefinableElement,
)
umlTrace_uml_TracedRedefinableTemplateSignature_strategy = st.builds(
    umlTrace_uml_TracedRedefinableTemplateSignature,
)
umlTrace_uml_TracedActivityNode_strategy = st.builds(
    umlTrace_uml_TracedActivityNode,
)
TracedActivityNode_strategy = st.builds(
    TracedActivityNode,
)
umlTrace_uml_TracedControlNode_strategy = st.builds(
    umlTrace_uml_TracedControlNode,
)
umlTrace_uml_TracedExecutableNode_strategy = st.builds(
    umlTrace_uml_TracedExecutableNode,
)
TracedExecutableNode_strategy = st.builds(
    TracedExecutableNode,
)
umlTrace_uml_TracedAction_strategy = st.builds(
    umlTrace_uml_TracedAction,
)
uml_TracedActivityGroup_strategy = st.builds(
    uml_TracedActivityGroup,
)
uml_TracedNamespace_strategy = st.builds(
    uml_TracedNamespace,
)
umlTrace_uml_TracedRegion_strategy = st.builds(
    umlTrace_uml_TracedRegion,
)
umlTrace_uml_TracedPackage_strategy = st.builds(
    umlTrace_uml_TracedPackage,
)
umlTrace_uml_TracedState_strategy = st.builds(
    umlTrace_uml_TracedState,
)
umlTrace_uml_TracedStructuredActivityNode_strategy = st.builds(
    umlTrace_uml_TracedStructuredActivityNode,
)
umlTrace_uml_TracedClassifier_strategy = st.builds(
    umlTrace_uml_TracedClassifier,
)
umlTrace_uml_TracedBehavioralFeature_strategy = st.builds(
    umlTrace_uml_TracedBehavioralFeature,
)
umlTrace_uml_TracedInteractionOperand_strategy = st.builds(
    umlTrace_uml_TracedInteractionOperand,
)
umlTrace_uml_TracedTransition_strategy = st.builds(
    umlTrace_uml_TracedTransition,
)
uml_TracedRaiseExceptionAction_strategy = st.builds(
    uml_TracedRaiseExceptionAction,
)
uml_TracedCommunicationPath_strategy = st.builds(
    uml_TracedCommunicationPath,
)
Kernel_TracedLiteralBooleanEvaluation_strategy = st.builds(
    Kernel_TracedLiteralBooleanEvaluation,
)
uml_TracedEnumeration_strategy = st.builds(
    uml_TracedEnumeration,
)
uml_TracedReadLinkObjectEndAction_strategy = st.builds(
    uml_TracedReadLinkObjectEndAction,
)
uml_TracedCallBehaviorAction_strategy = st.builds(
    uml_TracedCallBehaviorAction,
)
uml_TracedVariable_strategy = st.builds(
    uml_TracedVariable,
)
uml_TracedConnectorEnd_strategy = st.builds(
    uml_TracedConnectorEnd,
)
uml_TracedArtifact_strategy = st.builds(
    uml_TracedArtifact,
)
uml_TracedCallOperationAction_strategy = st.builds(
    uml_TracedCallOperationAction,
)
uml_TracedLiteralUnlimitedNatural_strategy = st.builds(
    uml_TracedLiteralUnlimitedNatural,
)
uml_TracedDurationObservation_strategy = st.builds(
    uml_TracedDurationObservation,
)
uml_TracedBehaviorExecutionSpecification_strategy = st.builds(
    uml_TracedBehaviorExecutionSpecification,
)
uml_TracedActivityParameterNode_strategy = st.builds(
    uml_TracedActivityParameterNode,
)
uml_TracedExpansionNode_strategy = st.builds(
    uml_TracedExpansionNode,
)
uml_TracedProfileApplication_strategy = st.builds(
    uml_TracedProfileApplication,
)
uml_TracedAddStructuralFeatureValueAction_strategy = st.builds(
    uml_TracedAddStructuralFeatureValueAction,
)
uml_TracedQualifierValue_strategy = st.builds(
    uml_TracedQualifierValue,
)
uml_TracedImage_strategy = st.builds(
    uml_TracedImage,
)
uml_TracedExtensionEnd_strategy = st.builds(
    uml_TracedExtensionEnd,
)
uml_TracedProperty_strategy = st.builds(
    uml_TracedProperty,
)
uml_TracedDevice_strategy = st.builds(
    uml_TracedDevice,
)
uml_TracedOpaqueAction_strategy = st.builds(
    uml_TracedOpaqueAction,
)
uml_TracedFinalState_strategy = st.builds(
    uml_TracedFinalState,
)
uml_TracedReduceAction_strategy = st.builds(
    uml_TracedReduceAction,
)
uml_TracedDuration_strategy = st.builds(
    uml_TracedDuration,
)
uml_TracedTemplateParameterSubstitution_strategy = st.builds(
    uml_TracedTemplateParameterSubstitution,
)
uml_TracedOutputPin_strategy = st.builds(
    uml_TracedOutputPin,
)
uml_TracedActionExecutionSpecification_strategy = st.builds(
    uml_TracedActionExecutionSpecification,
)
uml_TracedInformationItem_strategy = st.builds(
    uml_TracedInformationItem,
)
uml_TracedOperationTemplateParameter_strategy = st.builds(
    uml_TracedOperationTemplateParameter,
)
uml_TracedConnectableElementTemplateParameter_strategy = st.builds(
    uml_TracedConnectableElementTemplateParameter,
)
uml_TracedLinkEndData_strategy = st.builds(
    uml_TracedLinkEndData,
)
uml_TracedDurationInterval_strategy = st.builds(
    uml_TracedDurationInterval,
)
uml_TracedTransition_strategy = st.builds(
    uml_TracedTransition,
)
uml_TracedTrigger_strategy = st.builds(
    uml_TracedTrigger,
)
uml_TracedReplyAction_strategy = st.builds(
    uml_TracedReplyAction,
)
uml_TracedClause_strategy = st.builds(
    uml_TracedClause,
)
uml_TracedPackageMerge_strategy = st.builds(
    uml_TracedPackageMerge,
)
uml_TracedDecisionNode_strategy = st.builds(
    uml_TracedDecisionNode,
)
IntermediateActions_TracedReadStructuralFeatureActionActivation_strategy = st.builds(
    IntermediateActions_TracedReadStructuralFeatureActionActivation,
)
uml_TracedReadSelfAction_strategy = st.builds(
    uml_TracedReadSelfAction,
)
uml_TracedOperation_strategy = st.builds(
    uml_TracedOperation,
)
uml_TracedObjectFlow_strategy = st.builds(
    uml_TracedObjectFlow,
)
uml_TracedParameterSet_strategy = st.builds(
    uml_TracedParameterSet,
)
uml_TracedOccurrenceSpecification_strategy = st.builds(
    uml_TracedOccurrenceSpecification,
)
umlTrace_uml_TracedMessageOccurrenceSpecification_strategy = st.builds(
    umlTrace_uml_TracedMessageOccurrenceSpecification,
)
uml_TracedAcceptEventAction_strategy = st.builds(
    uml_TracedAcceptEventAction,
)
uml_TracedComponentRealization_strategy = st.builds(
    uml_TracedComponentRealization,
)
uml_TracedDataType_strategy = st.builds(
    uml_TracedDataType,
)
uml_TracedComment_strategy = st.builds(
    uml_TracedComment,
)
uml_TracedLoopNode_strategy = st.builds(
    uml_TracedLoopNode,
)
uml_TracedCallEvent_strategy = st.builds(
    uml_TracedCallEvent,
)
uml_TracedPackage_strategy = st.builds(
    uml_TracedPackage,
)
uml_TracedProtocolConformance_strategy = st.builds(
    uml_TracedProtocolConformance,
)
uml_TracedOpaqueBehavior_strategy = st.builds(
    uml_TracedOpaqueBehavior,
)
uml_TracedInterface_strategy = st.builds(
    uml_TracedInterface,
)
IntermediateActivities_TracedDecisionNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedDecisionNodeActivation,
)
uml_TracedInteractionConstraint_strategy = st.builds(
    uml_TracedInteractionConstraint,
)
uml_TracedTimeInterval_strategy = st.builds(
    uml_TracedTimeInterval,
)
uml_TracedExecutionOccurrenceSpecification_strategy = st.builds(
    uml_TracedExecutionOccurrenceSpecification,
)
uml_TracedSignal_strategy = st.builds(
    uml_TracedSignal,
)
uml_TracedExtensionPoint_strategy = st.builds(
    uml_TracedExtensionPoint,
)
uml_TracedCreateLinkAction_strategy = st.builds(
    uml_TracedCreateLinkAction,
)
Kernel_TracedLiteralIntegerEvaluation_strategy = st.builds(
    Kernel_TracedLiteralIntegerEvaluation,
)
uml_TracedCentralBufferNode_strategy = st.builds(
    uml_TracedCentralBufferNode,
)
uml_TracedModel_strategy = st.builds(
    uml_TracedModel,
)
uml_TracedRedefinableTemplateSignature_strategy = st.builds(
    uml_TracedRedefinableTemplateSignature,
)
uml_TracedJoinNode_strategy = st.builds(
    uml_TracedJoinNode,
)
BasicActions_TracedOpaqueActionActivation_strategy = st.builds(
    BasicActions_TracedOpaqueActionActivation,
)
uml_TracedReadLinkObjectEndQualifierAction_strategy = st.builds(
    uml_TracedReadLinkObjectEndQualifierAction,
)
uml_TracedRealization_strategy = st.builds(
    uml_TracedRealization,
)
uml_TracedConnectionPointReference_strategy = st.builds(
    uml_TracedConnectionPointReference,
)
uml_TracedConditionalNode_strategy = st.builds(
    uml_TracedConditionalNode,
)
Kernel_TracedBooleanValue_strategy = st.builds(
    Kernel_TracedBooleanValue,
)
uml_TracedSignalEvent_strategy = st.builds(
    uml_TracedSignalEvent,
)
uml_TracedLiteralInteger_strategy = st.builds(
    uml_TracedLiteralInteger,
)
uml_TracedDestroyLinkAction_strategy = st.builds(
    uml_TracedDestroyLinkAction,
)
IntermediateActivities_TracedActivityFinalNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedActivityFinalNodeActivation,
)
uml_TracedReadVariableAction_strategy = st.builds(
    uml_TracedReadVariableAction,
)
uml_TracedActionInputPin_strategy = st.builds(
    uml_TracedActionInputPin,
)
uml_TracedUsage_strategy = st.builds(
    uml_TracedUsage,
)
uml_TracedDeploymentSpecification_strategy = st.builds(
    uml_TracedDeploymentSpecification,
)
uml_TracedTemplateBinding_strategy = st.builds(
    uml_TracedTemplateBinding,
)
uml_TracedMessageOccurrenceSpecification_strategy = st.builds(
    uml_TracedMessageOccurrenceSpecification,
)
uml_TracedReception_strategy = st.builds(
    uml_TracedReception,
)
uml_TracedProtocolStateMachine_strategy = st.builds(
    uml_TracedProtocolStateMachine,
)
uml_TracedDataStoreNode_strategy = st.builds(
    uml_TracedDataStoreNode,
)
uml_TracedReadStructuralFeatureAction_strategy = st.builds(
    uml_TracedReadStructuralFeatureAction,
)
uml_TracedAnyReceiveEvent_strategy = st.builds(
    uml_TracedAnyReceiveEvent,
)
Kernel_TracedIntegerValue_strategy = st.builds(
    Kernel_TracedIntegerValue,
)
uml_TracedInterval_strategy = st.builds(
    uml_TracedInterval,
)
uml_TracedRemoveStructuralFeatureValueAction_strategy = st.builds(
    uml_TracedRemoveStructuralFeatureValueAction,
)
uml_TracedGeneralization_strategy = st.builds(
    uml_TracedGeneralization,
)
uml_TracedInteractionOperand_strategy = st.builds(
    uml_TracedInteractionOperand,
)
uml_TracedProtocolTransition_strategy = st.builds(
    uml_TracedProtocolTransition,
)
uml_TracedInterruptibleActivityRegion_strategy = st.builds(
    uml_TracedInterruptibleActivityRegion,
)
uml_TracedPartDecomposition_strategy = st.builds(
    uml_TracedPartDecomposition,
)
uml_TracedTimeEvent_strategy = st.builds(
    uml_TracedTimeEvent,
)
uml_TracedDeployment_strategy = st.builds(
    uml_TracedDeployment,
)
Loci_TracedSemanticVisitor_strategy = st.builds(
    Loci_TracedSemanticVisitor,
)
Kernel_TracedObject_strategy = st.builds(
    Kernel_TracedObject,
)
IntermediateActivities_TracedJoinNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedJoinNodeActivation,
)
uml_TracedUseCase_strategy = st.builds(
    uml_TracedUseCase,
)
uml_TracedReclassifyObjectAction_strategy = st.builds(
    uml_TracedReclassifyObjectAction,
)
uml_TracedInstanceValue_strategy = st.builds(
    uml_TracedInstanceValue,
)
IntermediateActions_TracedAddStructuralFeatureValueActionActivation_strategy = st.builds(
    IntermediateActions_TracedAddStructuralFeatureValueActionActivation,
)
Kernel_TracedReference_strategy = st.builds(
    Kernel_TracedReference,
)
uml_TracedForkNode_strategy = st.builds(
    uml_TracedForkNode,
)
uml_TracedActivity_strategy = st.builds(
    uml_TracedActivity,
)
uml_TracedMessage_strategy = st.builds(
    uml_TracedMessage,
)
uml_TracedStateMachine_strategy = st.builds(
    uml_TracedStateMachine,
)
uml_TracedActivityPartition_strategy = st.builds(
    uml_TracedActivityPartition,
)
IntermediateActivities_TracedActivityParameterNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedActivityParameterNodeActivation,
)
BasicActions_TracedCallBehaviorActionActivation_strategy = st.builds(
    BasicActions_TracedCallBehaviorActionActivation,
)
uml_TracedDestroyObjectAction_strategy = st.builds(
    uml_TracedDestroyObjectAction,
)
uml_TracedAssociationClass_strategy = st.builds(
    uml_TracedAssociationClass,
)
uml_TracedInformationFlow_strategy = st.builds(
    uml_TracedInformationFlow,
)
uml_TracedSubstitution_strategy = st.builds(
    uml_TracedSubstitution,
)
uml_TracedEnumerationLiteral_strategy = st.builds(
    uml_TracedEnumerationLiteral,
)
uml_TracedStereotype_strategy = st.builds(
    uml_TracedStereotype,
)
uml_TracedAcceptCallAction_strategy = st.builds(
    uml_TracedAcceptCallAction,
)
uml_TracedInstanceSpecification_strategy = st.builds(
    uml_TracedInstanceSpecification,
)
IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_strategy = st.builds(
    IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution,
)
uml_TracedStateInvariant_strategy = st.builds(
    uml_TracedStateInvariant,
)
BasicActions_TracedInputPinActivation_strategy = st.builds(
    BasicActions_TracedInputPinActivation,
)
uml_TracedLiteralString_strategy = st.builds(
    uml_TracedLiteralString,
)
uml_TracedOpaqueExpression_strategy = st.builds(
    uml_TracedOpaqueExpression,
)
uml_TracedParameter_strategy = st.builds(
    uml_TracedParameter,
)
IntermediateActivities_TracedActivityNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedActivityNodeActivation,
)
uml_TracedInteraction_strategy = st.builds(
    uml_TracedInteraction,
)
uml_TracedBroadcastSignalAction_strategy = st.builds(
    uml_TracedBroadcastSignalAction,
)
uml_TracedConstraint_strategy = st.builds(
    uml_TracedConstraint,
)
uml_TracedClearVariableAction_strategy = st.builds(
    uml_TracedClearVariableAction,
)
uml_TracedInputPin_strategy = st.builds(
    uml_TracedInputPin,
)
uml_TracedTimeConstraint_strategy = st.builds(
    uml_TracedTimeConstraint,
)
uml_TracedContinuation_strategy = st.builds(
    uml_TracedContinuation,
)
uml_TracedConsiderIgnoreFragment_strategy = st.builds(
    uml_TracedConsiderIgnoreFragment,
)
uml_TracedIntervalConstraint_strategy = st.builds(
    uml_TracedIntervalConstraint,
)
uml_TracedExecutionEnvironment_strategy = st.builds(
    uml_TracedExecutionEnvironment,
)
uml_TracedStructuredActivityNode_strategy = st.builds(
    uml_TracedStructuredActivityNode,
)
uml_TracedExtension_strategy = st.builds(
    uml_TracedExtension,
)
IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_strategy = st.builds(
    IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution,
)
uml_TracedExtend_strategy = st.builds(
    uml_TracedExtend,
)
uml_TracedStartClassifierBehaviorAction_strategy = st.builds(
    uml_TracedStartClassifierBehaviorAction,
)
uml_TracedSequenceNode_strategy = st.builds(
    uml_TracedSequenceNode,
)
uml_TracedExceptionHandler_strategy = st.builds(
    uml_TracedExceptionHandler,
)
uml_TracedNode_strategy = st.builds(
    uml_TracedNode,
)
uml_TracedValuePin_strategy = st.builds(
    uml_TracedValuePin,
)
IntermediateActivities_TracedActivityExecution_strategy = st.builds(
    IntermediateActivities_TracedActivityExecution,
)
uml_TracedCollaborationUse_strategy = st.builds(
    uml_TracedCollaborationUse,
)
IntermediateActivities_TracedInitialNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedInitialNodeActivation,
)
uml_TracedPort_strategy = st.builds(
    uml_TracedPort,
)
uml_TracedDependency_strategy = st.builds(
    uml_TracedDependency,
)
uml_TracedChangeEvent_strategy = st.builds(
    uml_TracedChangeEvent,
)
uml_TracedGeneralizationSet_strategy = st.builds(
    uml_TracedGeneralizationSet,
)
uml_TracedInteractionUse_strategy = st.builds(
    uml_TracedInteractionUse,
)
uml_TracedClass_strategy = st.builds(
    uml_TracedClass,
)
umlTrace_uml_TracedNode_strategy = st.builds(
    umlTrace_uml_TracedNode,
)
umlTrace_uml_TracedAssociationClass_strategy = st.builds(
    umlTrace_uml_TracedAssociationClass,
)
uml_TracedPackageImport_strategy = st.builds(
    uml_TracedPackageImport,
)
uml_TracedSendObjectAction_strategy = st.builds(
    uml_TracedSendObjectAction,
)
uml_TracedConnector_strategy = st.builds(
    uml_TracedConnector,
)
uml_TracedDestructionOccurrenceSpecification_strategy = st.builds(
    uml_TracedDestructionOccurrenceSpecification,
)
uml_TracedDurationConstraint_strategy = st.builds(
    uml_TracedDurationConstraint,
)
IntermediateActivities_TracedForkNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedForkNodeActivation,
)
uml_TracedLifeline_strategy = st.builds(
    uml_TracedLifeline,
)
uml_TracedCreateObjectAction_strategy = st.builds(
    uml_TracedCreateObjectAction,
)
uml_TracedExpansionRegion_strategy = st.builds(
    uml_TracedExpansionRegion,
)
uml_TracedFlowFinalNode_strategy = st.builds(
    uml_TracedFlowFinalNode,
)
uml_TracedInitialNode_strategy = st.builds(
    uml_TracedInitialNode,
)
uml_TracedCreateLinkObjectAction_strategy = st.builds(
    uml_TracedCreateLinkObjectAction,
)
uml_TracedCombinedFragment_strategy = st.builds(
    uml_TracedCombinedFragment,
)
umlTrace_Traced_TracedObjects_strategy = st.builds(
    umlTrace_Traced_TracedObjects,
)
Traced_TracedObjects_strategy = st.builds(
    Traced_TracedObjects,
)
State_strategy = st.builds(
    State,
)
umlTrace_Trace_strategy = st.builds(
    umlTrace_Trace,
)
Values_SemanticVisitor_runtimeModelElement_Value_strategy = st.builds(
    Values_SemanticVisitor_runtimeModelElement_Value,
)
Values_ActionActivation_firing_Value_strategy = st.builds(
    Values_ActionActivation_firing_Value,
)
umlTrace_State_strategy = st.builds(
    umlTrace_State,
)

@given(instance=TracedExecution_strategy)
@settings(max_examples=50)
def test_tracedexecution_instantiation(instance):
    assert isinstance(instance, TracedExecution)

@given(instance=umlTrace_IntermediateActivities_TracedActivityExecution_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedactivityexecution_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedActivityExecution)

@given(instance=TracedSemanticVisitor_strategy)
@settings(max_examples=50)
def test_tracedsemanticvisitor_instantiation(instance):
    assert isinstance(instance, TracedSemanticVisitor)

@given(instance=umlTrace_IntermediateActivities_TracedActivityNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedactivitynodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedActivityNodeActivation)

@given(instance=TracedActivityNodeActivation_strategy)
@settings(max_examples=50)
def test_tracedactivitynodeactivation_instantiation(instance):
    assert isinstance(instance, TracedActivityNodeActivation)

@given(instance=umlTrace_IntermediateActivities_TracedObjectNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedobjectnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedObjectNodeActivation)

@given(instance=umlTrace_IntermediateActivities_TracedControlNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedcontrolnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedControlNodeActivation)

@given(instance=TracedControlNodeActivation_strategy)
@settings(max_examples=50)
def test_tracedcontrolnodeactivation_instantiation(instance):
    assert isinstance(instance, TracedControlNodeActivation)

@given(instance=umlTrace_IntermediateActivities_TracedInitialNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedinitialnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedInitialNodeActivation)

@given(instance=umlTrace_IntermediateActivities_TracedMergeNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedmergenodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedMergeNodeActivation)

@given(instance=umlTrace_IntermediateActivities_TracedForkNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedforknodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedForkNodeActivation)

@given(instance=uml_TracedVertex_strategy)
@settings(max_examples=50)
def test_uml_tracedvertex_instantiation(instance):
    assert isinstance(instance, uml_TracedVertex)

@given(instance=TracedState_strategy)
@settings(max_examples=50)
def test_tracedstate_instantiation(instance):
    assert isinstance(instance, TracedState)

@given(instance=umlTrace_uml_TracedFinalState_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedfinalstate_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedFinalState)

@given(instance=TracedExecutionSpecification_strategy)
@settings(max_examples=50)
def test_tracedexecutionspecification_instantiation(instance):
    assert isinstance(instance, TracedExecutionSpecification)

@given(instance=umlTrace_uml_TracedBehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedbehaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedBehaviorExecutionSpecification)

@given(instance=TracedOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_tracedoccurrencespecification_instantiation(instance):
    assert isinstance(instance, TracedOccurrenceSpecification)

@given(instance=umlTrace_uml_TracedExecutionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedexecutionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExecutionOccurrenceSpecification)

@given(instance=TracedOpaqueBehavior_strategy)
@settings(max_examples=50)
def test_tracedopaquebehavior_instantiation(instance):
    assert isinstance(instance, TracedOpaqueBehavior)

@given(instance=umlTrace_uml_TracedFunctionBehavior_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedfunctionbehavior_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedFunctionBehavior)

@given(instance=uml_TracedStructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml_tracedstructuredclassifier_instantiation(instance):
    assert isinstance(instance, uml_TracedStructuredClassifier)

@given(instance=TracedMultiplicityElement_strategy)
@settings(max_examples=50)
def test_tracedmultiplicityelement_instantiation(instance):
    assert isinstance(instance, TracedMultiplicityElement)

@given(instance=umlTrace_uml_TracedConnectorEnd_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconnectorend_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConnectorEnd)

@given(instance=umlTrace_uml_TracedActionExecutionSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactionexecutionspecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActionExecutionSpecification)

@given(instance=TracedObjectNode_strategy)
@settings(max_examples=50)
def test_tracedobjectnode_instantiation(instance):
    assert isinstance(instance, TracedObjectNode)

@given(instance=umlTrace_uml_TracedExpansionNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedexpansionnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExpansionNode)

@given(instance=umlTrace_uml_TracedActivityParameterNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactivityparameternode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActivityParameterNode)

@given(instance=umlTrace_uml_TracedCentralBufferNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcentralbuffernode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCentralBufferNode)

@given(instance=TracedCentralBufferNode_strategy)
@settings(max_examples=50)
def test_tracedcentralbuffernode_instantiation(instance):
    assert isinstance(instance, TracedCentralBufferNode)

@given(instance=umlTrace_uml_TracedDataStoreNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddatastorenode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDataStoreNode)

@given(instance=TracedDataType_strategy)
@settings(max_examples=50)
def test_traceddatatype_instantiation(instance):
    assert isinstance(instance, TracedDataType)

@given(instance=umlTrace_uml_TracedEnumeration_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedenumeration_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedEnumeration)

@given(instance=umlTrace_uml_TracedPrimitiveType_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedprimitivetype_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPrimitiveType)

@given(instance=TracedMessageEvent_strategy)
@settings(max_examples=50)
def test_tracedmessageevent_instantiation(instance):
    assert isinstance(instance, TracedMessageEvent)

@given(instance=umlTrace_uml_TracedCallEvent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcallevent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCallEvent)

@given(instance=uml_ActivityContent_strategy)
@settings(max_examples=50)
def test_uml_activitycontent_instantiation(instance):
    assert isinstance(instance, uml_ActivityContent)

@given(instance=BasicActions_TracedActionActivation_strategy)
@settings(max_examples=50)
def test_basicactions_tracedactionactivation_instantiation(instance):
    assert isinstance(instance, BasicActions_TracedActionActivation)

@given(instance=umlTrace_Values_ActionActivation_firing_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_actionactivation_firing_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActionActivation_firing_Value)



@given(instance=umlTrace_Values_ActionActivation_firing_Value_strategy)
def test_umltrace_values_actionactivation_firing_value_firing_setter(instance):
    original = instance.firing
    instance.firing = original
    assert instance.firing == original

@given(instance=TracedLiteralEvaluation_strategy)
@settings(max_examples=50)
def test_tracedliteralevaluation_instantiation(instance):
    assert isinstance(instance, TracedLiteralEvaluation)

@given(instance=umlTrace_Kernel_TracedLiteralIntegerEvaluation_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedliteralintegerevaluation_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedLiteralIntegerEvaluation)

@given(instance=umlTrace_Kernel_TracedLiteralBooleanEvaluation_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedliteralbooleanevaluation_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedLiteralBooleanEvaluation)

@given(instance=TracedPrimitiveValue_strategy)
@settings(max_examples=50)
def test_tracedprimitivevalue_instantiation(instance):
    assert isinstance(instance, TracedPrimitiveValue)

@given(instance=umlTrace_Kernel_TracedBooleanValue_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedbooleanvalue_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedBooleanValue)

@given(instance=umlTrace_Kernel_TracedIntegerValue_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedintegervalue_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedIntegerValue)

@given(instance=umlTrace_Kernel_TracedEvaluation_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedevaluation_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedEvaluation)

@given(instance=TracedEvaluation_strategy)
@settings(max_examples=50)
def test_tracedevaluation_instantiation(instance):
    assert isinstance(instance, TracedEvaluation)

@given(instance=umlTrace_Kernel_TracedLiteralEvaluation_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedliteralevaluation_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedLiteralEvaluation)

@given(instance=umlTrace_Kernel_TracedValue_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedvalue_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedValue)

@given(instance=TracedValue_strategy)
@settings(max_examples=50)
def test_tracedvalue_instantiation(instance):
    assert isinstance(instance, TracedValue)

@given(instance=umlTrace_Kernel_TracedPrimitiveValue_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedprimitivevalue_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedPrimitiveValue)

@given(instance=umlTrace_Kernel_TracedStructuredValue_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedstructuredvalue_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedStructuredValue)

@given(instance=TracedStructuredValue_strategy)
@settings(max_examples=50)
def test_tracedstructuredvalue_instantiation(instance):
    assert isinstance(instance, TracedStructuredValue)

@given(instance=umlTrace_Kernel_TracedReference_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedreference_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedReference)

@given(instance=umlTrace_Kernel_TracedCompoundValue_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedcompoundvalue_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedCompoundValue)

@given(instance=TracedCompoundValue_strategy)
@settings(max_examples=50)
def test_tracedcompoundvalue_instantiation(instance):
    assert isinstance(instance, TracedCompoundValue)

@given(instance=umlTrace_Kernel_TracedExtensionalValue_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedextensionalvalue_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedExtensionalValue)

@given(instance=TracedExtensionalValue_strategy)
@settings(max_examples=50)
def test_tracedextensionalvalue_instantiation(instance):
    assert isinstance(instance, TracedExtensionalValue)

@given(instance=umlTrace_Kernel_TracedObject_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedobject_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedObject)

@given(instance=umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution_strategy)
@settings(max_examples=50)
def test_umltrace_basicbehaviors_tracedopaquebehaviorexecution_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution)

@given(instance=TracedObject_strategy)
@settings(max_examples=50)
def test_tracedobject_instantiation(instance):
    assert isinstance(instance, TracedObject)

@given(instance=umlTrace_BasicBehaviors_TracedExecution_strategy)
@settings(max_examples=50)
def test_umltrace_basicbehaviors_tracedexecution_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicBehaviors_TracedExecution)

@given(instance=uml_TracedElement_strategy)
@settings(max_examples=50)
def test_uml_tracedelement_instantiation(instance):
    assert isinstance(instance, uml_TracedElement)

@given(instance=umlTrace_Values_SemanticVisitor_runtimeModelElement_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_semanticvisitor_runtimemodelelement_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_SemanticVisitor_runtimeModelElement_Value)

@given(instance=TracedOpaqueBehaviorExecution_strategy)
@settings(max_examples=50)
def test_tracedopaquebehaviorexecution_instantiation(instance):
    assert isinstance(instance, TracedOpaqueBehaviorExecution)

@given(instance=umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_umltrace_integerfunctions_tracedintegergreaterfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution)

@given(instance=umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_umltrace_integerfunctions_tracedintegerlessfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution)

@given(instance=umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_umltrace_integerfunctions_tracedintegerplusfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution)

@given(instance=TracedCallActionActivation_strategy)
@settings(max_examples=50)
def test_tracedcallactionactivation_instantiation(instance):
    assert isinstance(instance, TracedCallActionActivation)

@given(instance=umlTrace_BasicActions_TracedCallBehaviorActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_basicactions_tracedcallbehavioractionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicActions_TracedCallBehaviorActionActivation)

@given(instance=TracedPinActivation_strategy)
@settings(max_examples=50)
def test_tracedpinactivation_instantiation(instance):
    assert isinstance(instance, TracedPinActivation)

@given(instance=umlTrace_BasicActions_TracedOutputPinActivation_strategy)
@settings(max_examples=50)
def test_umltrace_basicactions_tracedoutputpinactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicActions_TracedOutputPinActivation)

@given(instance=umlTrace_BasicActions_TracedInputPinActivation_strategy)
@settings(max_examples=50)
def test_umltrace_basicactions_tracedinputpinactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicActions_TracedInputPinActivation)

@given(instance=TracedInvocationActionActivation_strategy)
@settings(max_examples=50)
def test_tracedinvocationactionactivation_instantiation(instance):
    assert isinstance(instance, TracedInvocationActionActivation)

@given(instance=umlTrace_BasicActions_TracedCallActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_basicactions_tracedcallactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicActions_TracedCallActionActivation)

@given(instance=TracedActionActivation_strategy)
@settings(max_examples=50)
def test_tracedactionactivation_instantiation(instance):
    assert isinstance(instance, TracedActionActivation)

@given(instance=umlTrace_BasicActions_TracedOpaqueActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_basicactions_tracedopaqueactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicActions_TracedOpaqueActionActivation)

@given(instance=umlTrace_BasicActions_TracedInvocationActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_basicactions_tracedinvocationactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicActions_TracedInvocationActionActivation)

@given(instance=umlTrace_BasicActions_TracedActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_basicactions_tracedactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicActions_TracedActionActivation)

@given(instance=umlTrace_Loci_TracedSemanticVisitor_strategy)
@settings(max_examples=50)
def test_umltrace_loci_tracedsemanticvisitor_instantiation(instance):
    assert isinstance(instance, umlTrace_Loci_TracedSemanticVisitor)

@given(instance=umlTrace_IntermediateActivities_TracedDecisionNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_traceddecisionnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedDecisionNodeActivation)

@given(instance=umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedactivityfinalnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation)

@given(instance=umlTrace_IntermediateActivities_TracedJoinNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedjoinnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedJoinNodeActivation)

@given(instance=TracedObjectNodeActivation_strategy)
@settings(max_examples=50)
def test_tracedobjectnodeactivation_instantiation(instance):
    assert isinstance(instance, TracedObjectNodeActivation)

@given(instance=umlTrace_BasicActions_TracedPinActivation_strategy)
@settings(max_examples=50)
def test_umltrace_basicactions_tracedpinactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicActions_TracedPinActivation)

@given(instance=umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedactivityparameternodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation)

@given(instance=umlTrace_IntermediateActions_TracedCreateObjectActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactions_tracedcreateobjectactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActions_TracedCreateObjectActionActivation)

@given(instance=umlTrace_IntermediateActions_TracedValueSpecificationActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactions_tracedvaluespecificationactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActions_TracedValueSpecificationActionActivation)

@given(instance=TracedWriteStructuralFeatureActionActivation_strategy)
@settings(max_examples=50)
def test_tracedwritestructuralfeatureactionactivation_instantiation(instance):
    assert isinstance(instance, TracedWriteStructuralFeatureActionActivation)

@given(instance=umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactions_tracedaddstructuralfeaturevalueactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation)

@given(instance=TracedStructuralFeatureActionActivation_strategy)
@settings(max_examples=50)
def test_tracedstructuralfeatureactionactivation_instantiation(instance):
    assert isinstance(instance, TracedStructuralFeatureActionActivation)

@given(instance=umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactions_tracedwritestructuralfeatureactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation)

@given(instance=umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactions_tracedreadstructuralfeatureactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation)

@given(instance=umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactions_tracedstructuralfeatureactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation)

@given(instance=umlTrace_ecore_TracedEModelElement_strategy)
@settings(max_examples=50)
def test_umltrace_ecore_tracedemodelelement_instantiation(instance):
    assert isinstance(instance, umlTrace_ecore_TracedEModelElement)

@given(instance=TracedMessageEnd_strategy)
@settings(max_examples=50)
def test_tracedmessageend_instantiation(instance):
    assert isinstance(instance, TracedMessageEnd)

@given(instance=umlTrace_uml_TracedGate_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedgate_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedGate)

@given(instance=uml_TracedAction_strategy)
@settings(max_examples=50)
def test_uml_tracedaction_instantiation(instance):
    assert isinstance(instance, uml_TracedAction)

@given(instance=TracedStructuredActivityNode_strategy)
@settings(max_examples=50)
def test_tracedstructuredactivitynode_instantiation(instance):
    assert isinstance(instance, TracedStructuredActivityNode)

@given(instance=umlTrace_uml_TracedConditionalNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconditionalnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConditionalNode)

@given(instance=TracedEModelElement_strategy)
@settings(max_examples=50)
def test_tracedemodelelement_instantiation(instance):
    assert isinstance(instance, TracedEModelElement)

@given(instance=umlTrace_uml_TracedElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedElement)

@given(instance=TracedElement_strategy)
@settings(max_examples=50)
def test_tracedelement_instantiation(instance):
    assert isinstance(instance, TracedElement)

@given(instance=umlTrace_uml_TracedTemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtemplateparametersubstitution_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTemplateParameterSubstitution)

@given(instance=umlTrace_uml_TracedQualifierValue_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedqualifiervalue_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedQualifierValue)

@given(instance=umlTrace_uml_TracedComment_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcomment_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedComment)

@given(instance=umlTrace_uml_TracedClause_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedclause_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedClause)

@given(instance=umlTrace_uml_TracedNamedElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracednamedelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedNamedElement)

@given(instance=TracedNamedElement_strategy)
@settings(max_examples=50)
def test_tracednamedelement_instantiation(instance):
    assert isinstance(instance, TracedNamedElement)

@given(instance=umlTrace_uml_TracedGeneralOrdering_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedgeneralordering_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedGeneralOrdering)

@given(instance=umlTrace_uml_TracedParameterSet_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedparameterset_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedParameterSet)

@given(instance=umlTrace_uml_TracedInteractionFragment_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinteractionfragment_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInteractionFragment)

@given(instance=uml_TracedMessageEnd_strategy)
@settings(max_examples=50)
def test_uml_tracedmessageend_instantiation(instance):
    assert isinstance(instance, uml_TracedMessageEnd)

@given(instance=TracedMessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_tracedmessageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, TracedMessageOccurrenceSpecification)

@given(instance=umlTrace_uml_TracedDestructionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddestructionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDestructionOccurrenceSpecification)

@given(instance=umlTrace_uml_TracedVertex_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedvertex_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedVertex)

@given(instance=TracedVertex_strategy)
@settings(max_examples=50)
def test_tracedvertex_instantiation(instance):
    assert isinstance(instance, TracedVertex)

@given(instance=umlTrace_uml_TracedConnectionPointReference_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconnectionpointreference_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConnectionPointReference)

@given(instance=umlTrace_uml_TracedPseudostate_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedpseudostate_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPseudostate)

@given(instance=umlTrace_uml_TracedParameterableElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedparameterableelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedParameterableElement)

@given(instance=uml_TracedParameterableElement_strategy)
@settings(max_examples=50)
def test_uml_tracedparameterableelement_instantiation(instance):
    assert isinstance(instance, uml_TracedParameterableElement)

@given(instance=TracedPackageableElement_strategy)
@settings(max_examples=50)
def test_tracedpackageableelement_instantiation(instance):
    assert isinstance(instance, TracedPackageableElement)

@given(instance=umlTrace_uml_TracedConstraint_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconstraint_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConstraint)

@given(instance=TracedConstraint_strategy)
@settings(max_examples=50)
def test_tracedconstraint_instantiation(instance):
    assert isinstance(instance, TracedConstraint)

@given(instance=umlTrace_uml_TracedInteractionConstraint_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinteractionconstraint_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInteractionConstraint)

@given(instance=umlTrace_uml_TracedIntervalConstraint_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedintervalconstraint_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedIntervalConstraint)

@given(instance=TracedIntervalConstraint_strategy)
@settings(max_examples=50)
def test_tracedintervalconstraint_instantiation(instance):
    assert isinstance(instance, TracedIntervalConstraint)

@given(instance=umlTrace_uml_TracedDurationConstraint_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddurationconstraint_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDurationConstraint)

@given(instance=uml_TracedControlFlow_strategy)
@settings(max_examples=50)
def test_uml_tracedcontrolflow_instantiation(instance):
    assert isinstance(instance, uml_TracedControlFlow)

@given(instance=uml_TracedTimeObservation_strategy)
@settings(max_examples=50)
def test_uml_tracedtimeobservation_instantiation(instance):
    assert isinstance(instance, uml_TracedTimeObservation)

@given(instance=uml_TracedGate_strategy)
@settings(max_examples=50)
def test_uml_tracedgate_instantiation(instance):
    assert isinstance(instance, uml_TracedGate)

@given(instance=uml_TracedActivityFinalNode_strategy)
@settings(max_examples=50)
def test_uml_tracedactivityfinalnode_instantiation(instance):
    assert isinstance(instance, uml_TracedActivityFinalNode)

@given(instance=uml_TracedClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml_tracedclassifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, uml_TracedClassifierTemplateParameter)

@given(instance=TracedInteractionFragment_strategy)
@settings(max_examples=50)
def test_tracedinteractionfragment_instantiation(instance):
    assert isinstance(instance, TracedInteractionFragment)

@given(instance=umlTrace_uml_TracedOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedoccurrencespecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedOccurrenceSpecification)

@given(instance=umlTrace_uml_TracedCombinedFragment_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcombinedfragment_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCombinedFragment)

@given(instance=uml_TracedGeneralOrdering_strategy)
@settings(max_examples=50)
def test_uml_tracedgeneralordering_instantiation(instance):
    assert isinstance(instance, uml_TracedGeneralOrdering)

@given(instance=uml_TracedElementImport_strategy)
@settings(max_examples=50)
def test_uml_tracedelementimport_instantiation(instance):
    assert isinstance(instance, uml_TracedElementImport)

@given(instance=uml_TracedMergeNode_strategy)
@settings(max_examples=50)
def test_uml_tracedmergenode_instantiation(instance):
    assert isinstance(instance, uml_TracedMergeNode)

@given(instance=uml_TracedClearAssociationAction_strategy)
@settings(max_examples=50)
def test_uml_tracedclearassociationaction_instantiation(instance):
    assert isinstance(instance, uml_TracedClearAssociationAction)

@given(instance=uml_TracedLinkEndCreationData_strategy)
@settings(max_examples=50)
def test_uml_tracedlinkendcreationdata_instantiation(instance):
    assert isinstance(instance, uml_TracedLinkEndCreationData)

@given(instance=uml_TracedPseudostate_strategy)
@settings(max_examples=50)
def test_uml_tracedpseudostate_instantiation(instance):
    assert isinstance(instance, uml_TracedPseudostate)

@given(instance=uml_TracedComponent_strategy)
@settings(max_examples=50)
def test_uml_tracedcomponent_instantiation(instance):
    assert isinstance(instance, uml_TracedComponent)

@given(instance=uml_TracedReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadIsClassifiedObjectAction)

@given(instance=uml_TracedAbstraction_strategy)
@settings(max_examples=50)
def test_uml_tracedabstraction_instantiation(instance):
    assert isinstance(instance, uml_TracedAbstraction)

@given(instance=uml_TracedTimeExpression_strategy)
@settings(max_examples=50)
def test_uml_tracedtimeexpression_instantiation(instance):
    assert isinstance(instance, uml_TracedTimeExpression)

@given(instance=uml_TracedValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_uml_tracedvaluespecificationaction_instantiation(instance):
    assert isinstance(instance, uml_TracedValueSpecificationAction)

@given(instance=uml_TracedFunctionBehavior_strategy)
@settings(max_examples=50)
def test_uml_tracedfunctionbehavior_instantiation(instance):
    assert isinstance(instance, uml_TracedFunctionBehavior)

@given(instance=IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_integerfunctions_tracedintegergreaterfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution)

@given(instance=IntermediateActivities_TracedMergeNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedmergenodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedMergeNodeActivation)

@given(instance=uml_TracedTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml_tracedtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml_TracedTemplateParameter)

@given(instance=uml_TracedManifestation_strategy)
@settings(max_examples=50)
def test_uml_tracedmanifestation_instantiation(instance):
    assert isinstance(instance, uml_TracedManifestation)

@given(instance=uml_TracedActor_strategy)
@settings(max_examples=50)
def test_uml_tracedactor_instantiation(instance):
    assert isinstance(instance, uml_TracedActor)

@given(instance=uml_TracedRemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml_tracedremovevariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml_TracedRemoveVariableValueAction)

@given(instance=uml_TracedProfile_strategy)
@settings(max_examples=50)
def test_uml_tracedprofile_instantiation(instance):
    assert isinstance(instance, uml_TracedProfile)

@given(instance=uml_TracedTestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml_tracedtestidentityaction_instantiation(instance):
    assert isinstance(instance, uml_TracedTestIdentityAction)

@given(instance=uml_TracedCollaboration_strategy)
@settings(max_examples=50)
def test_uml_tracedcollaboration_instantiation(instance):
    assert isinstance(instance, uml_TracedCollaboration)

@given(instance=uml_TracedSendSignalAction_strategy)
@settings(max_examples=50)
def test_uml_tracedsendsignalaction_instantiation(instance):
    assert isinstance(instance, uml_TracedSendSignalAction)

@given(instance=uml_TracedInterfaceRealization_strategy)
@settings(max_examples=50)
def test_uml_tracedinterfacerealization_instantiation(instance):
    assert isinstance(instance, uml_TracedInterfaceRealization)

@given(instance=uml_TracedUnmarshallAction_strategy)
@settings(max_examples=50)
def test_uml_tracedunmarshallaction_instantiation(instance):
    assert isinstance(instance, uml_TracedUnmarshallAction)

@given(instance=uml_TracedExpression_strategy)
@settings(max_examples=50)
def test_uml_tracedexpression_instantiation(instance):
    assert isinstance(instance, uml_TracedExpression)

@given(instance=uml_TracedAssociation_strategy)
@settings(max_examples=50)
def test_uml_tracedassociation_instantiation(instance):
    assert isinstance(instance, uml_TracedAssociation)

@given(instance=uml_TracedClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml_tracedclearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml_TracedClearStructuralFeatureAction)

@given(instance=uml_TracedAddVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml_tracedaddvariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml_TracedAddVariableValueAction)

@given(instance=uml_TracedLiteralReal_strategy)
@settings(max_examples=50)
def test_uml_tracedliteralreal_instantiation(instance):
    assert isinstance(instance, uml_TracedLiteralReal)

@given(instance=IntermediateActions_TracedCreateObjectActionActivation_strategy)
@settings(max_examples=50)
def test_intermediateactions_tracedcreateobjectactionactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActions_TracedCreateObjectActionActivation)

@given(instance=uml_TracedSlot_strategy)
@settings(max_examples=50)
def test_uml_tracedslot_instantiation(instance):
    assert isinstance(instance, uml_TracedSlot)

@given(instance=uml_TracedLiteralNull_strategy)
@settings(max_examples=50)
def test_uml_tracedliteralnull_instantiation(instance):
    assert isinstance(instance, uml_TracedLiteralNull)

@given(instance=IntermediateActions_TracedValueSpecificationActionActivation_strategy)
@settings(max_examples=50)
def test_intermediateactions_tracedvaluespecificationactionactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActions_TracedValueSpecificationActionActivation)

@given(instance=uml_TracedStartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml_tracedstartobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, uml_TracedStartObjectBehaviorAction)

@given(instance=uml_TracedLiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml_tracedliteralboolean_instantiation(instance):
    assert isinstance(instance, uml_TracedLiteralBoolean)

@given(instance=uml_TracedReadLinkAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadlinkaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadLinkAction)

@given(instance=uml_TracedInclude_strategy)
@settings(max_examples=50)
def test_uml_tracedinclude_instantiation(instance):
    assert isinstance(instance, uml_TracedInclude)

@given(instance=uml_TracedRegion_strategy)
@settings(max_examples=50)
def test_uml_tracedregion_instantiation(instance):
    assert isinstance(instance, uml_TracedRegion)

@given(instance=uml_TracedState_strategy)
@settings(max_examples=50)
def test_uml_tracedstate_instantiation(instance):
    assert isinstance(instance, uml_TracedState)

@given(instance=uml_TracedPrimitiveType_strategy)
@settings(max_examples=50)
def test_uml_tracedprimitivetype_instantiation(instance):
    assert isinstance(instance, uml_TracedPrimitiveType)

@given(instance=uml_TracedStringExpression_strategy)
@settings(max_examples=50)
def test_uml_tracedstringexpression_instantiation(instance):
    assert isinstance(instance, uml_TracedStringExpression)

@given(instance=uml_TracedLinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_uml_tracedlinkenddestructiondata_instantiation(instance):
    assert isinstance(instance, uml_TracedLinkEndDestructionData)

@given(instance=umlTrace_uml_TracedAnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedanyreceiveevent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAnyReceiveEvent)

@given(instance=uml_TracedReadExtentAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadextentaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadExtentAction)

@given(instance=BasicActions_TracedOutputPinActivation_strategy)
@settings(max_examples=50)
def test_basicactions_tracedoutputpinactivation_instantiation(instance):
    assert isinstance(instance, BasicActions_TracedOutputPinActivation)

@given(instance=uml_TracedBehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml_tracedbehavioralfeature_instantiation(instance):
    assert isinstance(instance, uml_TracedBehavioralFeature)

@given(instance=uml_TracedTemplateSignature_strategy)
@settings(max_examples=50)
def test_uml_tracedtemplatesignature_instantiation(instance):
    assert isinstance(instance, uml_TracedTemplateSignature)

@given(instance=umlTrace_uml_TracedTemplateParameter_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtemplateparameter_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTemplateParameter)

@given(instance=TracedTemplateParameter_strategy)
@settings(max_examples=50)
def test_tracedtemplateparameter_instantiation(instance):
    assert isinstance(instance, TracedTemplateParameter)

@given(instance=umlTrace_uml_TracedConnectableElementTemplateParameter_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconnectableelementtemplateparameter_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConnectableElementTemplateParameter)

@given(instance=umlTrace_uml_TracedClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedclassifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedClassifierTemplateParameter)

@given(instance=TracedPackage_strategy)
@settings(max_examples=50)
def test_tracedpackage_instantiation(instance):
    assert isinstance(instance, TracedPackage)

@given(instance=umlTrace_uml_TracedProfile_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedprofile_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedProfile)

@given(instance=umlTrace_uml_TracedModel_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedmodel_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedModel)

@given(instance=umlTrace_uml_TracedImage_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedimage_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedImage)

@given(instance=TracedTransition_strategy)
@settings(max_examples=50)
def test_tracedtransition_instantiation(instance):
    assert isinstance(instance, TracedTransition)

@given(instance=umlTrace_uml_TracedProtocolTransition_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedprotocoltransition_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedProtocolTransition)

@given(instance=TracedWriteVariableAction_strategy)
@settings(max_examples=50)
def test_tracedwritevariableaction_instantiation(instance):
    assert isinstance(instance, TracedWriteVariableAction)

@given(instance=umlTrace_uml_TracedRemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedremovevariablevalueaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedRemoveVariableValueAction)

@given(instance=umlTrace_uml_TracedAddVariableValueAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedaddvariablevalueaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAddVariableValueAction)

@given(instance=TracedInteractionUse_strategy)
@settings(max_examples=50)
def test_tracedinteractionuse_instantiation(instance):
    assert isinstance(instance, TracedInteractionUse)

@given(instance=umlTrace_uml_TracedPartDecomposition_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedpartdecomposition_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPartDecomposition)

@given(instance=TracedObservation_strategy)
@settings(max_examples=50)
def test_tracedobservation_instantiation(instance):
    assert isinstance(instance, TracedObservation)

@given(instance=umlTrace_uml_TracedTimeObservation_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtimeobservation_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTimeObservation)

@given(instance=umlTrace_uml_TracedDurationObservation_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddurationobservation_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDurationObservation)

@given(instance=umlTrace_uml_TracedOperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedoperationtemplateparameter_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedOperationTemplateParameter)

@given(instance=TracedInterval_strategy)
@settings(max_examples=50)
def test_tracedinterval_instantiation(instance):
    assert isinstance(instance, TracedInterval)

@given(instance=umlTrace_uml_TracedDurationInterval_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddurationinterval_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDurationInterval)

@given(instance=umlTrace_uml_TracedTimeInterval_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtimeinterval_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTimeInterval)

@given(instance=umlTrace_uml_TracedSignalEvent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedsignalevent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedSignalEvent)

@given(instance=TracedBehavioralFeature_strategy)
@settings(max_examples=50)
def test_tracedbehavioralfeature_instantiation(instance):
    assert isinstance(instance, TracedBehavioralFeature)

@given(instance=umlTrace_uml_TracedReception_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreception_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReception)

@given(instance=umlTrace_uml_TracedExecutionSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedexecutionspecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExecutionSpecification)

@given(instance=TracedDependency_strategy)
@settings(max_examples=50)
def test_traceddependency_instantiation(instance):
    assert isinstance(instance, TracedDependency)

@given(instance=umlTrace_uml_TracedUsage_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedusage_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedUsage)

@given(instance=umlTrace_uml_TracedAbstraction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedabstraction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAbstraction)

@given(instance=TracedAbstraction_strategy)
@settings(max_examples=50)
def test_tracedabstraction_instantiation(instance):
    assert isinstance(instance, TracedAbstraction)

@given(instance=umlTrace_uml_TracedManifestation_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedmanifestation_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedManifestation)

@given(instance=umlTrace_uml_TracedRealization_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedrealization_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedRealization)

@given(instance=TracedRealization_strategy)
@settings(max_examples=50)
def test_tracedrealization_instantiation(instance):
    assert isinstance(instance, TracedRealization)

@given(instance=umlTrace_uml_TracedComponentRealization_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcomponentrealization_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedComponentRealization)

@given(instance=umlTrace_uml_TracedInterfaceRealization_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinterfacerealization_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInterfaceRealization)

@given(instance=umlTrace_uml_TracedSubstitution_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedsubstitution_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedSubstitution)

@given(instance=TracedInstanceSpecification_strategy)
@settings(max_examples=50)
def test_tracedinstancespecification_instantiation(instance):
    assert isinstance(instance, TracedInstanceSpecification)

@given(instance=umlTrace_uml_TracedEnumerationLiteral_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedenumerationliteral_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedEnumerationLiteral)

@given(instance=TracedAcceptEventAction_strategy)
@settings(max_examples=50)
def test_tracedaccepteventaction_instantiation(instance):
    assert isinstance(instance, TracedAcceptEventAction)

@given(instance=umlTrace_uml_TracedAcceptCallAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedacceptcallaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAcceptCallAction)

@given(instance=umlTrace_uml_TracedLinkEndData_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedlinkenddata_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLinkEndData)

@given(instance=TracedLinkEndData_strategy)
@settings(max_examples=50)
def test_tracedlinkenddata_instantiation(instance):
    assert isinstance(instance, TracedLinkEndData)

@given(instance=umlTrace_uml_TracedLinkEndCreationData_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedlinkendcreationdata_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLinkEndCreationData)

@given(instance=umlTrace_uml_TracedLinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedlinkenddestructiondata_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLinkEndDestructionData)

@given(instance=umlTrace_uml_TracedTemplateSignature_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtemplatesignature_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTemplateSignature)

@given(instance=umlTrace_uml_TracedStateInvariant_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstateinvariant_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStateInvariant)

@given(instance=umlTrace_uml_TracedTrigger_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtrigger_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTrigger)

@given(instance=umlTrace_uml_TracedSlot_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedslot_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedSlot)

@given(instance=TracedClass_strategy)
@settings(max_examples=50)
def test_tracedclass_instantiation(instance):
    assert isinstance(instance, TracedClass)

@given(instance=umlTrace_uml_TracedStereotype_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstereotype_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStereotype)

@given(instance=umlTrace_uml_TracedComponent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcomponent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedComponent)

@given(instance=umlTrace_uml_TracedBehavior_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedbehavior_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedBehavior)

@given(instance=uml_TracedInteractionFragment_strategy)
@settings(max_examples=50)
def test_uml_tracedinteractionfragment_instantiation(instance):
    assert isinstance(instance, uml_TracedInteractionFragment)

@given(instance=uml_TracedBehavior_strategy)
@settings(max_examples=50)
def test_uml_tracedbehavior_instantiation(instance):
    assert isinstance(instance, uml_TracedBehavior)

@given(instance=umlTrace_uml_TracedInteraction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinteraction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInteraction)

@given(instance=TracedActivityEdge_strategy)
@settings(max_examples=50)
def test_tracedactivityedge_instantiation(instance):
    assert isinstance(instance, TracedActivityEdge)

@given(instance=umlTrace_uml_TracedControlFlow_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcontrolflow_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedControlFlow)

@given(instance=umlTrace_uml_TracedObjectFlow_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedobjectflow_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedObjectFlow)

@given(instance=TracedStateMachine_strategy)
@settings(max_examples=50)
def test_tracedstatemachine_instantiation(instance):
    assert isinstance(instance, TracedStateMachine)

@given(instance=umlTrace_uml_TracedProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedprotocolstatemachine_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedProtocolStateMachine)

@given(instance=umlTrace_uml_TracedDeployment_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddeployment_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDeployment)

@given(instance=umlTrace_uml_TracedMessage_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedmessage_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedMessage)

@given(instance=TracedBehavior_strategy)
@settings(max_examples=50)
def test_tracedbehavior_instantiation(instance):
    assert isinstance(instance, TracedBehavior)

@given(instance=umlTrace_uml_TracedOpaqueBehavior_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedopaquebehavior_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedOpaqueBehavior)

@given(instance=umlTrace_uml_TracedActivity_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactivity_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActivity)

@given(instance=umlTrace_uml_TracedStateMachine_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstatemachine_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStateMachine)

@given(instance=TracedActivityGroup_strategy)
@settings(max_examples=50)
def test_tracedactivitygroup_instantiation(instance):
    assert isinstance(instance, TracedActivityGroup)

@given(instance=umlTrace_uml_TracedInterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinterruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInterruptibleActivityRegion)

@given(instance=umlTrace_uml_TracedActivityPartition_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactivitypartition_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActivityPartition)

@given(instance=uml_TracedRelationship_strategy)
@settings(max_examples=50)
def test_uml_tracedrelationship_instantiation(instance):
    assert isinstance(instance, uml_TracedRelationship)

@given(instance=TracedAssociation_strategy)
@settings(max_examples=50)
def test_tracedassociation_instantiation(instance):
    assert isinstance(instance, TracedAssociation)

@given(instance=umlTrace_uml_TracedCommunicationPath_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcommunicationpath_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCommunicationPath)

@given(instance=umlTrace_uml_TracedExtension_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedextension_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExtension)

@given(instance=TracedStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_tracedstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, TracedStructuralFeatureAction)

@given(instance=umlTrace_uml_TracedReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadStructuralFeatureAction)

@given(instance=umlTrace_uml_TracedClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedclearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedClearStructuralFeatureAction)

@given(instance=umlTrace_uml_TracedWriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedwritestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedWriteStructuralFeatureAction)

@given(instance=TracedWriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_tracedwritestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, TracedWriteStructuralFeatureAction)

@given(instance=umlTrace_uml_TracedAddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedaddstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAddStructuralFeatureValueAction)

@given(instance=umlTrace_uml_TracedRemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedremovestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedRemoveStructuralFeatureValueAction)

@given(instance=TracedBehavioredClassifier_strategy)
@settings(max_examples=50)
def test_tracedbehavioredclassifier_instantiation(instance):
    assert isinstance(instance, TracedBehavioredClassifier)

@given(instance=umlTrace_uml_TracedActor_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactor_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActor)

@given(instance=umlTrace_uml_TracedUseCase_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedusecase_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedUseCase)

@given(instance=umlTrace_uml_TracedSequenceNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedsequencenode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedSequenceNode)

@given(instance=umlTrace_uml_TracedExceptionHandler_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedexceptionhandler_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExceptionHandler)

@given(instance=umlTrace_uml_TracedDeployedArtifact_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddeployedartifact_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDeployedArtifact)

@given(instance=uml_TracedDeployedArtifact_strategy)
@settings(max_examples=50)
def test_uml_traceddeployedartifact_instantiation(instance):
    assert isinstance(instance, uml_TracedDeployedArtifact)

@given(instance=uml_TracedClassifier_strategy)
@settings(max_examples=50)
def test_uml_tracedclassifier_instantiation(instance):
    assert isinstance(instance, uml_TracedClassifier)

@given(instance=umlTrace_uml_TracedAssociation_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedassociation_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAssociation)

@given(instance=umlTrace_uml_TracedArtifact_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedartifact_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedArtifact)

@given(instance=TracedArtifact_strategy)
@settings(max_examples=50)
def test_tracedartifact_instantiation(instance):
    assert isinstance(instance, TracedArtifact)

@given(instance=umlTrace_uml_TracedDeploymentSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddeploymentspecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDeploymentSpecification)

@given(instance=uml_TracedActivityNode_strategy)
@settings(max_examples=50)
def test_uml_tracedactivitynode_instantiation(instance):
    assert isinstance(instance, uml_TracedActivityNode)

@given(instance=uml_TracedObjectNode_strategy)
@settings(max_examples=50)
def test_uml_tracedobjectnode_instantiation(instance):
    assert isinstance(instance, uml_TracedObjectNode)

@given(instance=TracedPin_strategy)
@settings(max_examples=50)
def test_tracedpin_instantiation(instance):
    assert isinstance(instance, TracedPin)

@given(instance=umlTrace_uml_TracedOutputPin_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedoutputpin_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedOutputPin)

@given(instance=umlTrace_uml_TracedInputPin_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinputpin_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInputPin)

@given(instance=TracedInputPin_strategy)
@settings(max_examples=50)
def test_tracedinputpin_instantiation(instance):
    assert isinstance(instance, TracedInputPin)

@given(instance=umlTrace_uml_TracedActionInputPin_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactioninputpin_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActionInputPin)

@given(instance=umlTrace_uml_TracedValuePin_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedvaluepin_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedValuePin)

@given(instance=umlTrace_uml_TracedCollaborationUse_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcollaborationuse_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCollaborationUse)

@given(instance=umlTrace_uml_TracedDeploymentTarget_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddeploymenttarget_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDeploymentTarget)

@given(instance=umlTrace_uml_TracedMultiplicityElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedmultiplicityelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedMultiplicityElement)

@given(instance=umlTrace_uml_TracedTypedElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtypedelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTypedElement)

@given(instance=uml_TracedMultiplicityElement_strategy)
@settings(max_examples=50)
def test_uml_tracedmultiplicityelement_instantiation(instance):
    assert isinstance(instance, uml_TracedMultiplicityElement)

@given(instance=umlTrace_uml_TracedPin_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedpin_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPin)

@given(instance=uml_TracedTypedElement_strategy)
@settings(max_examples=50)
def test_uml_tracedtypedelement_instantiation(instance):
    assert isinstance(instance, uml_TracedTypedElement)

@given(instance=umlTrace_uml_TracedConnectableElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconnectableelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConnectableElement)

@given(instance=umlTrace_uml_TracedObjectNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedobjectnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedObjectNode)

@given(instance=uml_TracedFeature_strategy)
@settings(max_examples=50)
def test_uml_tracedfeature_instantiation(instance):
    assert isinstance(instance, uml_TracedFeature)

@given(instance=umlTrace_uml_TracedStructuralFeature_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstructuralfeature_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStructuralFeature)

@given(instance=TracedValueSpecification_strategy)
@settings(max_examples=50)
def test_tracedvaluespecification_instantiation(instance):
    assert isinstance(instance, TracedValueSpecification)

@given(instance=umlTrace_uml_TracedOpaqueExpression_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedopaqueexpression_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedOpaqueExpression)

@given(instance=umlTrace_uml_TracedTimeExpression_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtimeexpression_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTimeExpression)

@given(instance=umlTrace_uml_TracedInterval_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinterval_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInterval)

@given(instance=umlTrace_uml_TracedExpression_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedexpression_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExpression)

@given(instance=umlTrace_uml_TracedInstanceValue_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinstancevalue_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInstanceValue)

@given(instance=umlTrace_uml_TracedDuration_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedduration_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDuration)

@given(instance=umlTrace_uml_TracedLiteralSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedliteralspecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLiteralSpecification)

@given(instance=TracedLiteralSpecification_strategy)
@settings(max_examples=50)
def test_tracedliteralspecification_instantiation(instance):
    assert isinstance(instance, TracedLiteralSpecification)

@given(instance=umlTrace_uml_TracedLiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedliteralunlimitednatural_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLiteralUnlimitedNatural)

@given(instance=umlTrace_uml_TracedLiteralNull_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedliteralnull_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLiteralNull)

@given(instance=umlTrace_uml_TracedLiteralReal_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedliteralreal_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLiteralReal)

@given(instance=umlTrace_uml_TracedLiteralBoolean_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedliteralboolean_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLiteralBoolean)

@given(instance=umlTrace_uml_TracedLiteralInteger_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedliteralinteger_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLiteralInteger)

@given(instance=umlTrace_uml_TracedLiteralString_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedliteralstring_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLiteralString)

@given(instance=TracedVariableAction_strategy)
@settings(max_examples=50)
def test_tracedvariableaction_instantiation(instance):
    assert isinstance(instance, TracedVariableAction)

@given(instance=umlTrace_uml_TracedReadVariableAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadvariableaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadVariableAction)

@given(instance=umlTrace_uml_TracedWriteVariableAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedwritevariableaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedWriteVariableAction)

@given(instance=umlTrace_uml_TracedClearVariableAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedclearvariableaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedClearVariableAction)

@given(instance=umlTrace_uml_TracedTimeConstraint_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtimeconstraint_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTimeConstraint)

@given(instance=umlTrace_uml_TracedContinuation_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcontinuation_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedContinuation)

@given(instance=TracedCombinedFragment_strategy)
@settings(max_examples=50)
def test_tracedcombinedfragment_instantiation(instance):
    assert isinstance(instance, TracedCombinedFragment)

@given(instance=umlTrace_uml_TracedConsiderIgnoreFragment_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconsiderignorefragment_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConsiderIgnoreFragment)

@given(instance=TracedNode_strategy)
@settings(max_examples=50)
def test_tracednode_instantiation(instance):
    assert isinstance(instance, TracedNode)

@given(instance=umlTrace_uml_TracedDevice_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddevice_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDevice)

@given(instance=umlTrace_uml_TracedExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedexecutionenvironment_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExecutionEnvironment)

@given(instance=umlTrace_uml_TracedType_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtype_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedType)

@given(instance=uml_TracedType_strategy)
@settings(max_examples=50)
def test_uml_tracedtype_instantiation(instance):
    assert isinstance(instance, uml_TracedType)

@given(instance=TracedClassifier_strategy)
@settings(max_examples=50)
def test_tracedclassifier_instantiation(instance):
    assert isinstance(instance, TracedClassifier)

@given(instance=umlTrace_uml_TracedDataType_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddatatype_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDataType)

@given(instance=umlTrace_uml_TracedInformationItem_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinformationitem_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInformationItem)

@given(instance=umlTrace_uml_TracedInterface_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinterface_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInterface)

@given(instance=umlTrace_uml_TracedBehavioredClassifier_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedbehavioredclassifier_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedBehavioredClassifier)

@given(instance=umlTrace_uml_TracedStructuredClassifier_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstructuredclassifier_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStructuredClassifier)

@given(instance=TracedStructuredClassifier_strategy)
@settings(max_examples=50)
def test_tracedstructuredclassifier_instantiation(instance):
    assert isinstance(instance, TracedStructuredClassifier)

@given(instance=umlTrace_uml_TracedEncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedencapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedEncapsulatedClassifier)

@given(instance=uml_TracedBehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml_tracedbehavioredclassifier_instantiation(instance):
    assert isinstance(instance, uml_TracedBehavioredClassifier)

@given(instance=umlTrace_uml_TracedCollaboration_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcollaboration_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCollaboration)

@given(instance=uml_TracedEncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml_tracedencapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, uml_TracedEncapsulatedClassifier)

@given(instance=umlTrace_uml_TracedClass_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedclass_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedClass)

@given(instance=TracedCallAction_strategy)
@settings(max_examples=50)
def test_tracedcallaction_instantiation(instance):
    assert isinstance(instance, TracedCallAction)

@given(instance=umlTrace_uml_TracedStartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstartobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStartObjectBehaviorAction)

@given(instance=umlTrace_uml_TracedCallOperationAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcalloperationaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCallOperationAction)

@given(instance=umlTrace_uml_TracedCallBehaviorAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcallbehavioraction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCallBehaviorAction)

@given(instance=umlTrace_uml_TracedRelationship_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedrelationship_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedRelationship)

@given(instance=TracedRelationship_strategy)
@settings(max_examples=50)
def test_tracedrelationship_instantiation(instance):
    assert isinstance(instance, TracedRelationship)

@given(instance=umlTrace_uml_TracedDirectedRelationship_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddirectedrelationship_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDirectedRelationship)

@given(instance=TracedDirectedRelationship_strategy)
@settings(max_examples=50)
def test_traceddirectedrelationship_instantiation(instance):
    assert isinstance(instance, TracedDirectedRelationship)

@given(instance=umlTrace_uml_TracedGeneralization_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedgeneralization_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedGeneralization)

@given(instance=umlTrace_uml_TracedElementImport_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedelementimport_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedElementImport)

@given(instance=umlTrace_uml_TracedProfileApplication_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedprofileapplication_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedProfileApplication)

@given(instance=umlTrace_uml_TracedPackageMerge_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedpackagemerge_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPackageMerge)

@given(instance=umlTrace_uml_TracedTemplateBinding_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtemplatebinding_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTemplateBinding)

@given(instance=umlTrace_uml_TracedPackageImport_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedpackageimport_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPackageImport)

@given(instance=umlTrace_uml_TracedProtocolConformance_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedprotocolconformance_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedProtocolConformance)

@given(instance=TracedInvocationAction_strategy)
@settings(max_examples=50)
def test_tracedinvocationaction_instantiation(instance):
    assert isinstance(instance, TracedInvocationAction)

@given(instance=umlTrace_uml_TracedCallAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcallaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCallAction)

@given(instance=umlTrace_uml_TracedBroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedbroadcastsignalaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedBroadcastSignalAction)

@given(instance=umlTrace_uml_TracedSendSignalAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedsendsignalaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedSendSignalAction)

@given(instance=umlTrace_uml_TracedSendObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedsendobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedSendObjectAction)

@given(instance=TracedRedefinableElement_strategy)
@settings(max_examples=50)
def test_tracedredefinableelement_instantiation(instance):
    assert isinstance(instance, TracedRedefinableElement)

@given(instance=umlTrace_uml_TracedExtensionPoint_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedextensionpoint_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExtensionPoint)

@given(instance=umlTrace_uml_TracedActivityEdge_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactivityedge_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActivityEdge)

@given(instance=umlTrace_uml_TracedFeature_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedfeature_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedFeature)

@given(instance=TracedFeature_strategy)
@settings(max_examples=50)
def test_tracedfeature_instantiation(instance):
    assert isinstance(instance, TracedFeature)

@given(instance=umlTrace_uml_TracedConnector_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconnector_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConnector)

@given(instance=umlTrace_uml_TracedTemplateableElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtemplateableelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTemplateableElement)

@given(instance=uml_TracedTemplateableElement_strategy)
@settings(max_examples=50)
def test_uml_tracedtemplateableelement_instantiation(instance):
    assert isinstance(instance, uml_TracedTemplateableElement)

@given(instance=umlTrace_uml_TracedOperation_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedoperation_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedOperation)

@given(instance=umlTrace_uml_TracedStringExpression_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstringexpression_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStringExpression)

@given(instance=uml_TracedPackageableElement_strategy)
@settings(max_examples=50)
def test_uml_tracedpackageableelement_instantiation(instance):
    assert isinstance(instance, uml_TracedPackageableElement)

@given(instance=umlTrace_uml_TracedValueSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedvaluespecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedValueSpecification)

@given(instance=umlTrace_uml_TracedMessageEnd_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedmessageend_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedMessageEnd)

@given(instance=uml_TracedDeploymentTarget_strategy)
@settings(max_examples=50)
def test_uml_traceddeploymenttarget_instantiation(instance):
    assert isinstance(instance, uml_TracedDeploymentTarget)

@given(instance=umlTrace_uml_TracedInstanceSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinstancespecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInstanceSpecification)

@given(instance=uml_TracedConnectableElement_strategy)
@settings(max_examples=50)
def test_uml_tracedconnectableelement_instantiation(instance):
    assert isinstance(instance, uml_TracedConnectableElement)

@given(instance=umlTrace_uml_TracedParameter_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedparameter_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedParameter)

@given(instance=umlTrace_uml_TracedVariable_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedvariable_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedVariable)

@given(instance=uml_TracedStructuralFeature_strategy)
@settings(max_examples=50)
def test_uml_tracedstructuralfeature_instantiation(instance):
    assert isinstance(instance, uml_TracedStructuralFeature)

@given(instance=umlTrace_uml_TracedProperty_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedproperty_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedProperty)

@given(instance=TracedProperty_strategy)
@settings(max_examples=50)
def test_tracedproperty_instantiation(instance):
    assert isinstance(instance, TracedProperty)

@given(instance=umlTrace_uml_TracedExtensionEnd_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedextensionend_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExtensionEnd)

@given(instance=umlTrace_uml_TracedPort_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedport_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPort)

@given(instance=uml_TracedDirectedRelationship_strategy)
@settings(max_examples=50)
def test_uml_traceddirectedrelationship_instantiation(instance):
    assert isinstance(instance, uml_TracedDirectedRelationship)

@given(instance=umlTrace_uml_TracedInformationFlow_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinformationflow_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInformationFlow)

@given(instance=umlTrace_uml_TracedDependency_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddependency_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDependency)

@given(instance=umlTrace_uml_TracedEvent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedevent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedEvent)

@given(instance=TracedEvent_strategy)
@settings(max_examples=50)
def test_tracedevent_instantiation(instance):
    assert isinstance(instance, TracedEvent)

@given(instance=umlTrace_uml_TracedMessageEvent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedmessageevent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedMessageEvent)

@given(instance=umlTrace_uml_TracedTimeEvent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtimeevent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTimeEvent)

@given(instance=umlTrace_uml_TracedChangeEvent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedchangeevent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedChangeEvent)

@given(instance=umlTrace_uml_TracedGeneralizationSet_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedgeneralizationset_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedGeneralizationSet)

@given(instance=umlTrace_uml_TracedSignal_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedsignal_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedSignal)

@given(instance=umlTrace_uml_TracedLoopNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedloopnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLoopNode)

@given(instance=umlTrace_uml_TracedInteractionUse_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinteractionuse_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInteractionUse)

@given(instance=umlTrace_uml_TracedObservation_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedobservation_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedObservation)

@given(instance=umlTrace_uml_TracedLifeline_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedlifeline_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLifeline)

@given(instance=umlTrace_uml_TracedExpansionRegion_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedexpansionregion_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExpansionRegion)

@given(instance=TracedFinalNode_strategy)
@settings(max_examples=50)
def test_tracedfinalnode_instantiation(instance):
    assert isinstance(instance, TracedFinalNode)

@given(instance=umlTrace_uml_TracedActivityFinalNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactivityfinalnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActivityFinalNode)

@given(instance=umlTrace_uml_TracedFlowFinalNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedflowfinalnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedFlowFinalNode)

@given(instance=TracedControlNode_strategy)
@settings(max_examples=50)
def test_tracedcontrolnode_instantiation(instance):
    assert isinstance(instance, TracedControlNode)

@given(instance=umlTrace_uml_TracedJoinNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedjoinnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedJoinNode)

@given(instance=umlTrace_uml_TracedMergeNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedmergenode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedMergeNode)

@given(instance=umlTrace_uml_TracedDecisionNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddecisionnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDecisionNode)

@given(instance=umlTrace_uml_TracedFinalNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedfinalnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedFinalNode)

@given(instance=umlTrace_uml_TracedForkNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedforknode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedForkNode)

@given(instance=umlTrace_uml_TracedInitialNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinitialnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInitialNode)

@given(instance=TracedAction_strategy)
@settings(max_examples=50)
def test_tracedaction_instantiation(instance):
    assert isinstance(instance, TracedAction)

@given(instance=umlTrace_uml_TracedReplyAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreplyaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReplyAction)

@given(instance=umlTrace_uml_TracedReadExtentAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadextentaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadExtentAction)

@given(instance=umlTrace_uml_TracedAcceptEventAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedaccepteventaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAcceptEventAction)

@given(instance=umlTrace_uml_TracedInvocationAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinvocationaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInvocationAction)

@given(instance=umlTrace_uml_TracedRaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedraiseexceptionaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedRaiseExceptionAction)

@given(instance=umlTrace_uml_TracedValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedvaluespecificationaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedValueSpecificationAction)

@given(instance=umlTrace_uml_TracedClearAssociationAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedclearassociationaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedClearAssociationAction)

@given(instance=umlTrace_uml_TracedOpaqueAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedopaqueaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedOpaqueAction)

@given(instance=umlTrace_uml_TracedCreateObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcreateobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCreateObjectAction)

@given(instance=umlTrace_uml_TracedReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReclassifyObjectAction)

@given(instance=umlTrace_uml_TracedStartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstartclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStartClassifierBehaviorAction)

@given(instance=umlTrace_uml_TracedVariableAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedvariableaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedVariableAction)

@given(instance=umlTrace_uml_TracedReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadIsClassifiedObjectAction)

@given(instance=umlTrace_uml_TracedTestIdentityAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtestidentityaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTestIdentityAction)

@given(instance=umlTrace_uml_TracedUnmarshallAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedunmarshallaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedUnmarshallAction)

@given(instance=umlTrace_uml_TracedReadSelfAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadselfaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadSelfAction)

@given(instance=umlTrace_uml_TracedReduceAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreduceaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReduceAction)

@given(instance=umlTrace_uml_TracedStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStructuralFeatureAction)

@given(instance=umlTrace_uml_TracedDestroyObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddestroyobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDestroyObjectAction)

@given(instance=umlTrace_uml_TracedReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadLinkObjectEndQualifierAction)

@given(instance=umlTrace_uml_TracedReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadLinkObjectEndAction)

@given(instance=umlTrace_uml_TracedLinkAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedlinkaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLinkAction)

@given(instance=TracedLinkAction_strategy)
@settings(max_examples=50)
def test_tracedlinkaction_instantiation(instance):
    assert isinstance(instance, TracedLinkAction)

@given(instance=umlTrace_uml_TracedReadLinkAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadlinkaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadLinkAction)

@given(instance=umlTrace_uml_TracedWriteLinkAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedwritelinkaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedWriteLinkAction)

@given(instance=TracedWriteLinkAction_strategy)
@settings(max_examples=50)
def test_tracedwritelinkaction_instantiation(instance):
    assert isinstance(instance, TracedWriteLinkAction)

@given(instance=umlTrace_uml_TracedDestroyLinkAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddestroylinkaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDestroyLinkAction)

@given(instance=umlTrace_uml_TracedCreateLinkAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcreatelinkaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCreateLinkAction)

@given(instance=TracedCreateLinkAction_strategy)
@settings(max_examples=50)
def test_tracedcreatelinkaction_instantiation(instance):
    assert isinstance(instance, TracedCreateLinkAction)

@given(instance=umlTrace_uml_TracedCreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcreatelinkobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCreateLinkObjectAction)

@given(instance=uml_TracedNamedElement_strategy)
@settings(max_examples=50)
def test_uml_tracednamedelement_instantiation(instance):
    assert isinstance(instance, uml_TracedNamedElement)

@given(instance=umlTrace_uml_TracedExtend_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedextend_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExtend)

@given(instance=umlTrace_uml_TracedInclude_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinclude_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInclude)

@given(instance=umlTrace_uml_TracedPackageableElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedpackageableelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPackageableElement)

@given(instance=umlTrace_uml_TracedNamespace_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracednamespace_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedNamespace)

@given(instance=umlTrace_uml_TracedRedefinableElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedredefinableelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedRedefinableElement)

@given(instance=ActivityContent_strategy)
@settings(max_examples=50)
def test_activitycontent_instantiation(instance):
    assert isinstance(instance, ActivityContent)

@given(instance=umlTrace_uml_TracedActivityGroup_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactivitygroup_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActivityGroup)

@given(instance=uml_TracedRedefinableElement_strategy)
@settings(max_examples=50)
def test_uml_tracedredefinableelement_instantiation(instance):
    assert isinstance(instance, uml_TracedRedefinableElement)

@given(instance=umlTrace_uml_TracedRedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedredefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedRedefinableTemplateSignature)

@given(instance=umlTrace_uml_TracedActivityNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactivitynode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActivityNode)

@given(instance=TracedActivityNode_strategy)
@settings(max_examples=50)
def test_tracedactivitynode_instantiation(instance):
    assert isinstance(instance, TracedActivityNode)

@given(instance=umlTrace_uml_TracedControlNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcontrolnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedControlNode)

@given(instance=umlTrace_uml_TracedExecutableNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedexecutablenode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExecutableNode)

@given(instance=TracedExecutableNode_strategy)
@settings(max_examples=50)
def test_tracedexecutablenode_instantiation(instance):
    assert isinstance(instance, TracedExecutableNode)

@given(instance=umlTrace_uml_TracedAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAction)

@given(instance=uml_TracedActivityGroup_strategy)
@settings(max_examples=50)
def test_uml_tracedactivitygroup_instantiation(instance):
    assert isinstance(instance, uml_TracedActivityGroup)

@given(instance=uml_TracedNamespace_strategy)
@settings(max_examples=50)
def test_uml_tracednamespace_instantiation(instance):
    assert isinstance(instance, uml_TracedNamespace)

@given(instance=umlTrace_uml_TracedRegion_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedregion_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedRegion)

@given(instance=umlTrace_uml_TracedPackage_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedpackage_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPackage)

@given(instance=umlTrace_uml_TracedState_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstate_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedState)

@given(instance=umlTrace_uml_TracedStructuredActivityNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstructuredactivitynode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStructuredActivityNode)

@given(instance=umlTrace_uml_TracedClassifier_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedclassifier_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedClassifier)

@given(instance=umlTrace_uml_TracedBehavioralFeature_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedbehavioralfeature_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedBehavioralFeature)

@given(instance=umlTrace_uml_TracedInteractionOperand_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinteractionoperand_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInteractionOperand)

@given(instance=umlTrace_uml_TracedTransition_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtransition_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTransition)

@given(instance=uml_TracedRaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_uml_tracedraiseexceptionaction_instantiation(instance):
    assert isinstance(instance, uml_TracedRaiseExceptionAction)

@given(instance=uml_TracedCommunicationPath_strategy)
@settings(max_examples=50)
def test_uml_tracedcommunicationpath_instantiation(instance):
    assert isinstance(instance, uml_TracedCommunicationPath)

@given(instance=Kernel_TracedLiteralBooleanEvaluation_strategy)
@settings(max_examples=50)
def test_kernel_tracedliteralbooleanevaluation_instantiation(instance):
    assert isinstance(instance, Kernel_TracedLiteralBooleanEvaluation)

@given(instance=uml_TracedEnumeration_strategy)
@settings(max_examples=50)
def test_uml_tracedenumeration_instantiation(instance):
    assert isinstance(instance, uml_TracedEnumeration)

@given(instance=uml_TracedReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadLinkObjectEndAction)

@given(instance=uml_TracedCallBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml_tracedcallbehavioraction_instantiation(instance):
    assert isinstance(instance, uml_TracedCallBehaviorAction)

@given(instance=uml_TracedVariable_strategy)
@settings(max_examples=50)
def test_uml_tracedvariable_instantiation(instance):
    assert isinstance(instance, uml_TracedVariable)

@given(instance=uml_TracedConnectorEnd_strategy)
@settings(max_examples=50)
def test_uml_tracedconnectorend_instantiation(instance):
    assert isinstance(instance, uml_TracedConnectorEnd)

@given(instance=uml_TracedArtifact_strategy)
@settings(max_examples=50)
def test_uml_tracedartifact_instantiation(instance):
    assert isinstance(instance, uml_TracedArtifact)

@given(instance=uml_TracedCallOperationAction_strategy)
@settings(max_examples=50)
def test_uml_tracedcalloperationaction_instantiation(instance):
    assert isinstance(instance, uml_TracedCallOperationAction)

@given(instance=uml_TracedLiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml_tracedliteralunlimitednatural_instantiation(instance):
    assert isinstance(instance, uml_TracedLiteralUnlimitedNatural)

@given(instance=uml_TracedDurationObservation_strategy)
@settings(max_examples=50)
def test_uml_traceddurationobservation_instantiation(instance):
    assert isinstance(instance, uml_TracedDurationObservation)

@given(instance=uml_TracedBehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml_tracedbehaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml_TracedBehaviorExecutionSpecification)

@given(instance=uml_TracedActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml_tracedactivityparameternode_instantiation(instance):
    assert isinstance(instance, uml_TracedActivityParameterNode)

@given(instance=uml_TracedExpansionNode_strategy)
@settings(max_examples=50)
def test_uml_tracedexpansionnode_instantiation(instance):
    assert isinstance(instance, uml_TracedExpansionNode)

@given(instance=uml_TracedProfileApplication_strategy)
@settings(max_examples=50)
def test_uml_tracedprofileapplication_instantiation(instance):
    assert isinstance(instance, uml_TracedProfileApplication)

@given(instance=uml_TracedAddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml_tracedaddstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml_TracedAddStructuralFeatureValueAction)

@given(instance=uml_TracedQualifierValue_strategy)
@settings(max_examples=50)
def test_uml_tracedqualifiervalue_instantiation(instance):
    assert isinstance(instance, uml_TracedQualifierValue)

@given(instance=uml_TracedImage_strategy)
@settings(max_examples=50)
def test_uml_tracedimage_instantiation(instance):
    assert isinstance(instance, uml_TracedImage)

@given(instance=uml_TracedExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml_tracedextensionend_instantiation(instance):
    assert isinstance(instance, uml_TracedExtensionEnd)

@given(instance=uml_TracedProperty_strategy)
@settings(max_examples=50)
def test_uml_tracedproperty_instantiation(instance):
    assert isinstance(instance, uml_TracedProperty)

@given(instance=uml_TracedDevice_strategy)
@settings(max_examples=50)
def test_uml_traceddevice_instantiation(instance):
    assert isinstance(instance, uml_TracedDevice)

@given(instance=uml_TracedOpaqueAction_strategy)
@settings(max_examples=50)
def test_uml_tracedopaqueaction_instantiation(instance):
    assert isinstance(instance, uml_TracedOpaqueAction)

@given(instance=uml_TracedFinalState_strategy)
@settings(max_examples=50)
def test_uml_tracedfinalstate_instantiation(instance):
    assert isinstance(instance, uml_TracedFinalState)

@given(instance=uml_TracedReduceAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreduceaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReduceAction)

@given(instance=uml_TracedDuration_strategy)
@settings(max_examples=50)
def test_uml_tracedduration_instantiation(instance):
    assert isinstance(instance, uml_TracedDuration)

@given(instance=uml_TracedTemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_uml_tracedtemplateparametersubstitution_instantiation(instance):
    assert isinstance(instance, uml_TracedTemplateParameterSubstitution)

@given(instance=uml_TracedOutputPin_strategy)
@settings(max_examples=50)
def test_uml_tracedoutputpin_instantiation(instance):
    assert isinstance(instance, uml_TracedOutputPin)

@given(instance=uml_TracedActionExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml_tracedactionexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml_TracedActionExecutionSpecification)

@given(instance=uml_TracedInformationItem_strategy)
@settings(max_examples=50)
def test_uml_tracedinformationitem_instantiation(instance):
    assert isinstance(instance, uml_TracedInformationItem)

@given(instance=uml_TracedOperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml_tracedoperationtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml_TracedOperationTemplateParameter)

@given(instance=uml_TracedConnectableElementTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml_tracedconnectableelementtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml_TracedConnectableElementTemplateParameter)

@given(instance=uml_TracedLinkEndData_strategy)
@settings(max_examples=50)
def test_uml_tracedlinkenddata_instantiation(instance):
    assert isinstance(instance, uml_TracedLinkEndData)

@given(instance=uml_TracedDurationInterval_strategy)
@settings(max_examples=50)
def test_uml_traceddurationinterval_instantiation(instance):
    assert isinstance(instance, uml_TracedDurationInterval)

@given(instance=uml_TracedTransition_strategy)
@settings(max_examples=50)
def test_uml_tracedtransition_instantiation(instance):
    assert isinstance(instance, uml_TracedTransition)

@given(instance=uml_TracedTrigger_strategy)
@settings(max_examples=50)
def test_uml_tracedtrigger_instantiation(instance):
    assert isinstance(instance, uml_TracedTrigger)

@given(instance=uml_TracedReplyAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreplyaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReplyAction)

@given(instance=uml_TracedClause_strategy)
@settings(max_examples=50)
def test_uml_tracedclause_instantiation(instance):
    assert isinstance(instance, uml_TracedClause)

@given(instance=uml_TracedPackageMerge_strategy)
@settings(max_examples=50)
def test_uml_tracedpackagemerge_instantiation(instance):
    assert isinstance(instance, uml_TracedPackageMerge)

@given(instance=uml_TracedDecisionNode_strategy)
@settings(max_examples=50)
def test_uml_traceddecisionnode_instantiation(instance):
    assert isinstance(instance, uml_TracedDecisionNode)

@given(instance=IntermediateActions_TracedReadStructuralFeatureActionActivation_strategy)
@settings(max_examples=50)
def test_intermediateactions_tracedreadstructuralfeatureactionactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActions_TracedReadStructuralFeatureActionActivation)

@given(instance=uml_TracedReadSelfAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadselfaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadSelfAction)

@given(instance=uml_TracedOperation_strategy)
@settings(max_examples=50)
def test_uml_tracedoperation_instantiation(instance):
    assert isinstance(instance, uml_TracedOperation)

@given(instance=uml_TracedObjectFlow_strategy)
@settings(max_examples=50)
def test_uml_tracedobjectflow_instantiation(instance):
    assert isinstance(instance, uml_TracedObjectFlow)

@given(instance=uml_TracedParameterSet_strategy)
@settings(max_examples=50)
def test_uml_tracedparameterset_instantiation(instance):
    assert isinstance(instance, uml_TracedParameterSet)

@given(instance=uml_TracedOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml_tracedoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml_TracedOccurrenceSpecification)

@given(instance=umlTrace_uml_TracedMessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedmessageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedMessageOccurrenceSpecification)

@given(instance=uml_TracedAcceptEventAction_strategy)
@settings(max_examples=50)
def test_uml_tracedaccepteventaction_instantiation(instance):
    assert isinstance(instance, uml_TracedAcceptEventAction)

@given(instance=uml_TracedComponentRealization_strategy)
@settings(max_examples=50)
def test_uml_tracedcomponentrealization_instantiation(instance):
    assert isinstance(instance, uml_TracedComponentRealization)

@given(instance=uml_TracedDataType_strategy)
@settings(max_examples=50)
def test_uml_traceddatatype_instantiation(instance):
    assert isinstance(instance, uml_TracedDataType)

@given(instance=uml_TracedComment_strategy)
@settings(max_examples=50)
def test_uml_tracedcomment_instantiation(instance):
    assert isinstance(instance, uml_TracedComment)

@given(instance=uml_TracedLoopNode_strategy)
@settings(max_examples=50)
def test_uml_tracedloopnode_instantiation(instance):
    assert isinstance(instance, uml_TracedLoopNode)

@given(instance=uml_TracedCallEvent_strategy)
@settings(max_examples=50)
def test_uml_tracedcallevent_instantiation(instance):
    assert isinstance(instance, uml_TracedCallEvent)

@given(instance=uml_TracedPackage_strategy)
@settings(max_examples=50)
def test_uml_tracedpackage_instantiation(instance):
    assert isinstance(instance, uml_TracedPackage)

@given(instance=uml_TracedProtocolConformance_strategy)
@settings(max_examples=50)
def test_uml_tracedprotocolconformance_instantiation(instance):
    assert isinstance(instance, uml_TracedProtocolConformance)

@given(instance=uml_TracedOpaqueBehavior_strategy)
@settings(max_examples=50)
def test_uml_tracedopaquebehavior_instantiation(instance):
    assert isinstance(instance, uml_TracedOpaqueBehavior)

@given(instance=uml_TracedInterface_strategy)
@settings(max_examples=50)
def test_uml_tracedinterface_instantiation(instance):
    assert isinstance(instance, uml_TracedInterface)

@given(instance=IntermediateActivities_TracedDecisionNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_traceddecisionnodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedDecisionNodeActivation)

@given(instance=uml_TracedInteractionConstraint_strategy)
@settings(max_examples=50)
def test_uml_tracedinteractionconstraint_instantiation(instance):
    assert isinstance(instance, uml_TracedInteractionConstraint)

@given(instance=uml_TracedTimeInterval_strategy)
@settings(max_examples=50)
def test_uml_tracedtimeinterval_instantiation(instance):
    assert isinstance(instance, uml_TracedTimeInterval)

@given(instance=uml_TracedExecutionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml_tracedexecutionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml_TracedExecutionOccurrenceSpecification)

@given(instance=uml_TracedSignal_strategy)
@settings(max_examples=50)
def test_uml_tracedsignal_instantiation(instance):
    assert isinstance(instance, uml_TracedSignal)

@given(instance=uml_TracedExtensionPoint_strategy)
@settings(max_examples=50)
def test_uml_tracedextensionpoint_instantiation(instance):
    assert isinstance(instance, uml_TracedExtensionPoint)

@given(instance=uml_TracedCreateLinkAction_strategy)
@settings(max_examples=50)
def test_uml_tracedcreatelinkaction_instantiation(instance):
    assert isinstance(instance, uml_TracedCreateLinkAction)

@given(instance=Kernel_TracedLiteralIntegerEvaluation_strategy)
@settings(max_examples=50)
def test_kernel_tracedliteralintegerevaluation_instantiation(instance):
    assert isinstance(instance, Kernel_TracedLiteralIntegerEvaluation)

@given(instance=uml_TracedCentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml_tracedcentralbuffernode_instantiation(instance):
    assert isinstance(instance, uml_TracedCentralBufferNode)

@given(instance=uml_TracedModel_strategy)
@settings(max_examples=50)
def test_uml_tracedmodel_instantiation(instance):
    assert isinstance(instance, uml_TracedModel)

@given(instance=uml_TracedRedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_uml_tracedredefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, uml_TracedRedefinableTemplateSignature)

@given(instance=uml_TracedJoinNode_strategy)
@settings(max_examples=50)
def test_uml_tracedjoinnode_instantiation(instance):
    assert isinstance(instance, uml_TracedJoinNode)

@given(instance=BasicActions_TracedOpaqueActionActivation_strategy)
@settings(max_examples=50)
def test_basicactions_tracedopaqueactionactivation_instantiation(instance):
    assert isinstance(instance, BasicActions_TracedOpaqueActionActivation)

@given(instance=uml_TracedReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadLinkObjectEndQualifierAction)

@given(instance=uml_TracedRealization_strategy)
@settings(max_examples=50)
def test_uml_tracedrealization_instantiation(instance):
    assert isinstance(instance, uml_TracedRealization)

@given(instance=uml_TracedConnectionPointReference_strategy)
@settings(max_examples=50)
def test_uml_tracedconnectionpointreference_instantiation(instance):
    assert isinstance(instance, uml_TracedConnectionPointReference)

@given(instance=uml_TracedConditionalNode_strategy)
@settings(max_examples=50)
def test_uml_tracedconditionalnode_instantiation(instance):
    assert isinstance(instance, uml_TracedConditionalNode)

@given(instance=Kernel_TracedBooleanValue_strategy)
@settings(max_examples=50)
def test_kernel_tracedbooleanvalue_instantiation(instance):
    assert isinstance(instance, Kernel_TracedBooleanValue)

@given(instance=uml_TracedSignalEvent_strategy)
@settings(max_examples=50)
def test_uml_tracedsignalevent_instantiation(instance):
    assert isinstance(instance, uml_TracedSignalEvent)

@given(instance=uml_TracedLiteralInteger_strategy)
@settings(max_examples=50)
def test_uml_tracedliteralinteger_instantiation(instance):
    assert isinstance(instance, uml_TracedLiteralInteger)

@given(instance=uml_TracedDestroyLinkAction_strategy)
@settings(max_examples=50)
def test_uml_traceddestroylinkaction_instantiation(instance):
    assert isinstance(instance, uml_TracedDestroyLinkAction)

@given(instance=IntermediateActivities_TracedActivityFinalNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedactivityfinalnodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedActivityFinalNodeActivation)

@given(instance=uml_TracedReadVariableAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadvariableaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadVariableAction)

@given(instance=uml_TracedActionInputPin_strategy)
@settings(max_examples=50)
def test_uml_tracedactioninputpin_instantiation(instance):
    assert isinstance(instance, uml_TracedActionInputPin)

@given(instance=uml_TracedUsage_strategy)
@settings(max_examples=50)
def test_uml_tracedusage_instantiation(instance):
    assert isinstance(instance, uml_TracedUsage)

@given(instance=uml_TracedDeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml_traceddeploymentspecification_instantiation(instance):
    assert isinstance(instance, uml_TracedDeploymentSpecification)

@given(instance=uml_TracedTemplateBinding_strategy)
@settings(max_examples=50)
def test_uml_tracedtemplatebinding_instantiation(instance):
    assert isinstance(instance, uml_TracedTemplateBinding)

@given(instance=uml_TracedMessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml_tracedmessageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml_TracedMessageOccurrenceSpecification)

@given(instance=uml_TracedReception_strategy)
@settings(max_examples=50)
def test_uml_tracedreception_instantiation(instance):
    assert isinstance(instance, uml_TracedReception)

@given(instance=uml_TracedProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml_tracedprotocolstatemachine_instantiation(instance):
    assert isinstance(instance, uml_TracedProtocolStateMachine)

@given(instance=uml_TracedDataStoreNode_strategy)
@settings(max_examples=50)
def test_uml_traceddatastorenode_instantiation(instance):
    assert isinstance(instance, uml_TracedDataStoreNode)

@given(instance=uml_TracedReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadStructuralFeatureAction)

@given(instance=uml_TracedAnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_uml_tracedanyreceiveevent_instantiation(instance):
    assert isinstance(instance, uml_TracedAnyReceiveEvent)

@given(instance=Kernel_TracedIntegerValue_strategy)
@settings(max_examples=50)
def test_kernel_tracedintegervalue_instantiation(instance):
    assert isinstance(instance, Kernel_TracedIntegerValue)

@given(instance=uml_TracedInterval_strategy)
@settings(max_examples=50)
def test_uml_tracedinterval_instantiation(instance):
    assert isinstance(instance, uml_TracedInterval)

@given(instance=uml_TracedRemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml_tracedremovestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml_TracedRemoveStructuralFeatureValueAction)

@given(instance=uml_TracedGeneralization_strategy)
@settings(max_examples=50)
def test_uml_tracedgeneralization_instantiation(instance):
    assert isinstance(instance, uml_TracedGeneralization)

@given(instance=uml_TracedInteractionOperand_strategy)
@settings(max_examples=50)
def test_uml_tracedinteractionoperand_instantiation(instance):
    assert isinstance(instance, uml_TracedInteractionOperand)

@given(instance=uml_TracedProtocolTransition_strategy)
@settings(max_examples=50)
def test_uml_tracedprotocoltransition_instantiation(instance):
    assert isinstance(instance, uml_TracedProtocolTransition)

@given(instance=uml_TracedInterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_uml_tracedinterruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, uml_TracedInterruptibleActivityRegion)

@given(instance=uml_TracedPartDecomposition_strategy)
@settings(max_examples=50)
def test_uml_tracedpartdecomposition_instantiation(instance):
    assert isinstance(instance, uml_TracedPartDecomposition)

@given(instance=uml_TracedTimeEvent_strategy)
@settings(max_examples=50)
def test_uml_tracedtimeevent_instantiation(instance):
    assert isinstance(instance, uml_TracedTimeEvent)

@given(instance=uml_TracedDeployment_strategy)
@settings(max_examples=50)
def test_uml_traceddeployment_instantiation(instance):
    assert isinstance(instance, uml_TracedDeployment)

@given(instance=Loci_TracedSemanticVisitor_strategy)
@settings(max_examples=50)
def test_loci_tracedsemanticvisitor_instantiation(instance):
    assert isinstance(instance, Loci_TracedSemanticVisitor)

@given(instance=Kernel_TracedObject_strategy)
@settings(max_examples=50)
def test_kernel_tracedobject_instantiation(instance):
    assert isinstance(instance, Kernel_TracedObject)

@given(instance=IntermediateActivities_TracedJoinNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedjoinnodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedJoinNodeActivation)

@given(instance=uml_TracedUseCase_strategy)
@settings(max_examples=50)
def test_uml_tracedusecase_instantiation(instance):
    assert isinstance(instance, uml_TracedUseCase)

@given(instance=uml_TracedReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReclassifyObjectAction)

@given(instance=uml_TracedInstanceValue_strategy)
@settings(max_examples=50)
def test_uml_tracedinstancevalue_instantiation(instance):
    assert isinstance(instance, uml_TracedInstanceValue)

@given(instance=IntermediateActions_TracedAddStructuralFeatureValueActionActivation_strategy)
@settings(max_examples=50)
def test_intermediateactions_tracedaddstructuralfeaturevalueactionactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActions_TracedAddStructuralFeatureValueActionActivation)

@given(instance=Kernel_TracedReference_strategy)
@settings(max_examples=50)
def test_kernel_tracedreference_instantiation(instance):
    assert isinstance(instance, Kernel_TracedReference)

@given(instance=uml_TracedForkNode_strategy)
@settings(max_examples=50)
def test_uml_tracedforknode_instantiation(instance):
    assert isinstance(instance, uml_TracedForkNode)

@given(instance=uml_TracedActivity_strategy)
@settings(max_examples=50)
def test_uml_tracedactivity_instantiation(instance):
    assert isinstance(instance, uml_TracedActivity)

@given(instance=uml_TracedMessage_strategy)
@settings(max_examples=50)
def test_uml_tracedmessage_instantiation(instance):
    assert isinstance(instance, uml_TracedMessage)

@given(instance=uml_TracedStateMachine_strategy)
@settings(max_examples=50)
def test_uml_tracedstatemachine_instantiation(instance):
    assert isinstance(instance, uml_TracedStateMachine)

@given(instance=uml_TracedActivityPartition_strategy)
@settings(max_examples=50)
def test_uml_tracedactivitypartition_instantiation(instance):
    assert isinstance(instance, uml_TracedActivityPartition)

@given(instance=IntermediateActivities_TracedActivityParameterNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedactivityparameternodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedActivityParameterNodeActivation)

@given(instance=BasicActions_TracedCallBehaviorActionActivation_strategy)
@settings(max_examples=50)
def test_basicactions_tracedcallbehavioractionactivation_instantiation(instance):
    assert isinstance(instance, BasicActions_TracedCallBehaviorActionActivation)

@given(instance=uml_TracedDestroyObjectAction_strategy)
@settings(max_examples=50)
def test_uml_traceddestroyobjectaction_instantiation(instance):
    assert isinstance(instance, uml_TracedDestroyObjectAction)

@given(instance=uml_TracedAssociationClass_strategy)
@settings(max_examples=50)
def test_uml_tracedassociationclass_instantiation(instance):
    assert isinstance(instance, uml_TracedAssociationClass)

@given(instance=uml_TracedInformationFlow_strategy)
@settings(max_examples=50)
def test_uml_tracedinformationflow_instantiation(instance):
    assert isinstance(instance, uml_TracedInformationFlow)

@given(instance=uml_TracedSubstitution_strategy)
@settings(max_examples=50)
def test_uml_tracedsubstitution_instantiation(instance):
    assert isinstance(instance, uml_TracedSubstitution)

@given(instance=uml_TracedEnumerationLiteral_strategy)
@settings(max_examples=50)
def test_uml_tracedenumerationliteral_instantiation(instance):
    assert isinstance(instance, uml_TracedEnumerationLiteral)

@given(instance=uml_TracedStereotype_strategy)
@settings(max_examples=50)
def test_uml_tracedstereotype_instantiation(instance):
    assert isinstance(instance, uml_TracedStereotype)

@given(instance=uml_TracedAcceptCallAction_strategy)
@settings(max_examples=50)
def test_uml_tracedacceptcallaction_instantiation(instance):
    assert isinstance(instance, uml_TracedAcceptCallAction)

@given(instance=uml_TracedInstanceSpecification_strategy)
@settings(max_examples=50)
def test_uml_tracedinstancespecification_instantiation(instance):
    assert isinstance(instance, uml_TracedInstanceSpecification)

@given(instance=IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_integerfunctions_tracedintegerlessfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution)

@given(instance=uml_TracedStateInvariant_strategy)
@settings(max_examples=50)
def test_uml_tracedstateinvariant_instantiation(instance):
    assert isinstance(instance, uml_TracedStateInvariant)

@given(instance=BasicActions_TracedInputPinActivation_strategy)
@settings(max_examples=50)
def test_basicactions_tracedinputpinactivation_instantiation(instance):
    assert isinstance(instance, BasicActions_TracedInputPinActivation)

@given(instance=uml_TracedLiteralString_strategy)
@settings(max_examples=50)
def test_uml_tracedliteralstring_instantiation(instance):
    assert isinstance(instance, uml_TracedLiteralString)

@given(instance=uml_TracedOpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml_tracedopaqueexpression_instantiation(instance):
    assert isinstance(instance, uml_TracedOpaqueExpression)

@given(instance=uml_TracedParameter_strategy)
@settings(max_examples=50)
def test_uml_tracedparameter_instantiation(instance):
    assert isinstance(instance, uml_TracedParameter)

@given(instance=IntermediateActivities_TracedActivityNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedactivitynodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedActivityNodeActivation)

@given(instance=uml_TracedInteraction_strategy)
@settings(max_examples=50)
def test_uml_tracedinteraction_instantiation(instance):
    assert isinstance(instance, uml_TracedInteraction)

@given(instance=uml_TracedBroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_uml_tracedbroadcastsignalaction_instantiation(instance):
    assert isinstance(instance, uml_TracedBroadcastSignalAction)

@given(instance=uml_TracedConstraint_strategy)
@settings(max_examples=50)
def test_uml_tracedconstraint_instantiation(instance):
    assert isinstance(instance, uml_TracedConstraint)

@given(instance=uml_TracedClearVariableAction_strategy)
@settings(max_examples=50)
def test_uml_tracedclearvariableaction_instantiation(instance):
    assert isinstance(instance, uml_TracedClearVariableAction)

@given(instance=uml_TracedInputPin_strategy)
@settings(max_examples=50)
def test_uml_tracedinputpin_instantiation(instance):
    assert isinstance(instance, uml_TracedInputPin)

@given(instance=uml_TracedTimeConstraint_strategy)
@settings(max_examples=50)
def test_uml_tracedtimeconstraint_instantiation(instance):
    assert isinstance(instance, uml_TracedTimeConstraint)

@given(instance=uml_TracedContinuation_strategy)
@settings(max_examples=50)
def test_uml_tracedcontinuation_instantiation(instance):
    assert isinstance(instance, uml_TracedContinuation)

@given(instance=uml_TracedConsiderIgnoreFragment_strategy)
@settings(max_examples=50)
def test_uml_tracedconsiderignorefragment_instantiation(instance):
    assert isinstance(instance, uml_TracedConsiderIgnoreFragment)

@given(instance=uml_TracedIntervalConstraint_strategy)
@settings(max_examples=50)
def test_uml_tracedintervalconstraint_instantiation(instance):
    assert isinstance(instance, uml_TracedIntervalConstraint)

@given(instance=uml_TracedExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml_tracedexecutionenvironment_instantiation(instance):
    assert isinstance(instance, uml_TracedExecutionEnvironment)

@given(instance=uml_TracedStructuredActivityNode_strategy)
@settings(max_examples=50)
def test_uml_tracedstructuredactivitynode_instantiation(instance):
    assert isinstance(instance, uml_TracedStructuredActivityNode)

@given(instance=uml_TracedExtension_strategy)
@settings(max_examples=50)
def test_uml_tracedextension_instantiation(instance):
    assert isinstance(instance, uml_TracedExtension)

@given(instance=IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_integerfunctions_tracedintegerplusfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution)

@given(instance=uml_TracedExtend_strategy)
@settings(max_examples=50)
def test_uml_tracedextend_instantiation(instance):
    assert isinstance(instance, uml_TracedExtend)

@given(instance=uml_TracedStartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml_tracedstartclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, uml_TracedStartClassifierBehaviorAction)

@given(instance=uml_TracedSequenceNode_strategy)
@settings(max_examples=50)
def test_uml_tracedsequencenode_instantiation(instance):
    assert isinstance(instance, uml_TracedSequenceNode)

@given(instance=uml_TracedExceptionHandler_strategy)
@settings(max_examples=50)
def test_uml_tracedexceptionhandler_instantiation(instance):
    assert isinstance(instance, uml_TracedExceptionHandler)

@given(instance=uml_TracedNode_strategy)
@settings(max_examples=50)
def test_uml_tracednode_instantiation(instance):
    assert isinstance(instance, uml_TracedNode)

@given(instance=uml_TracedValuePin_strategy)
@settings(max_examples=50)
def test_uml_tracedvaluepin_instantiation(instance):
    assert isinstance(instance, uml_TracedValuePin)

@given(instance=IntermediateActivities_TracedActivityExecution_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedactivityexecution_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedActivityExecution)

@given(instance=uml_TracedCollaborationUse_strategy)
@settings(max_examples=50)
def test_uml_tracedcollaborationuse_instantiation(instance):
    assert isinstance(instance, uml_TracedCollaborationUse)

@given(instance=IntermediateActivities_TracedInitialNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedinitialnodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedInitialNodeActivation)

@given(instance=uml_TracedPort_strategy)
@settings(max_examples=50)
def test_uml_tracedport_instantiation(instance):
    assert isinstance(instance, uml_TracedPort)

@given(instance=uml_TracedDependency_strategy)
@settings(max_examples=50)
def test_uml_traceddependency_instantiation(instance):
    assert isinstance(instance, uml_TracedDependency)

@given(instance=uml_TracedChangeEvent_strategy)
@settings(max_examples=50)
def test_uml_tracedchangeevent_instantiation(instance):
    assert isinstance(instance, uml_TracedChangeEvent)

@given(instance=uml_TracedGeneralizationSet_strategy)
@settings(max_examples=50)
def test_uml_tracedgeneralizationset_instantiation(instance):
    assert isinstance(instance, uml_TracedGeneralizationSet)

@given(instance=uml_TracedInteractionUse_strategy)
@settings(max_examples=50)
def test_uml_tracedinteractionuse_instantiation(instance):
    assert isinstance(instance, uml_TracedInteractionUse)

@given(instance=uml_TracedClass_strategy)
@settings(max_examples=50)
def test_uml_tracedclass_instantiation(instance):
    assert isinstance(instance, uml_TracedClass)

@given(instance=umlTrace_uml_TracedNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracednode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedNode)

@given(instance=umlTrace_uml_TracedAssociationClass_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedassociationclass_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAssociationClass)

@given(instance=uml_TracedPackageImport_strategy)
@settings(max_examples=50)
def test_uml_tracedpackageimport_instantiation(instance):
    assert isinstance(instance, uml_TracedPackageImport)

@given(instance=uml_TracedSendObjectAction_strategy)
@settings(max_examples=50)
def test_uml_tracedsendobjectaction_instantiation(instance):
    assert isinstance(instance, uml_TracedSendObjectAction)

@given(instance=uml_TracedConnector_strategy)
@settings(max_examples=50)
def test_uml_tracedconnector_instantiation(instance):
    assert isinstance(instance, uml_TracedConnector)

@given(instance=uml_TracedDestructionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml_traceddestructionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml_TracedDestructionOccurrenceSpecification)

@given(instance=uml_TracedDurationConstraint_strategy)
@settings(max_examples=50)
def test_uml_traceddurationconstraint_instantiation(instance):
    assert isinstance(instance, uml_TracedDurationConstraint)

@given(instance=IntermediateActivities_TracedForkNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedforknodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedForkNodeActivation)

@given(instance=uml_TracedLifeline_strategy)
@settings(max_examples=50)
def test_uml_tracedlifeline_instantiation(instance):
    assert isinstance(instance, uml_TracedLifeline)

@given(instance=uml_TracedCreateObjectAction_strategy)
@settings(max_examples=50)
def test_uml_tracedcreateobjectaction_instantiation(instance):
    assert isinstance(instance, uml_TracedCreateObjectAction)

@given(instance=uml_TracedExpansionRegion_strategy)
@settings(max_examples=50)
def test_uml_tracedexpansionregion_instantiation(instance):
    assert isinstance(instance, uml_TracedExpansionRegion)

@given(instance=uml_TracedFlowFinalNode_strategy)
@settings(max_examples=50)
def test_uml_tracedflowfinalnode_instantiation(instance):
    assert isinstance(instance, uml_TracedFlowFinalNode)

@given(instance=uml_TracedInitialNode_strategy)
@settings(max_examples=50)
def test_uml_tracedinitialnode_instantiation(instance):
    assert isinstance(instance, uml_TracedInitialNode)

@given(instance=uml_TracedCreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_uml_tracedcreatelinkobjectaction_instantiation(instance):
    assert isinstance(instance, uml_TracedCreateLinkObjectAction)

@given(instance=uml_TracedCombinedFragment_strategy)
@settings(max_examples=50)
def test_uml_tracedcombinedfragment_instantiation(instance):
    assert isinstance(instance, uml_TracedCombinedFragment)

@given(instance=umlTrace_Traced_TracedObjects_strategy)
@settings(max_examples=50)
def test_umltrace_traced_tracedobjects_instantiation(instance):
    assert isinstance(instance, umlTrace_Traced_TracedObjects)

@given(instance=Traced_TracedObjects_strategy)
@settings(max_examples=50)
def test_traced_tracedobjects_instantiation(instance):
    assert isinstance(instance, Traced_TracedObjects)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=umlTrace_Trace_strategy)
@settings(max_examples=50)
def test_umltrace_trace_instantiation(instance):
    assert isinstance(instance, umlTrace_Trace)

@given(instance=Values_SemanticVisitor_runtimeModelElement_Value_strategy)
@settings(max_examples=50)
def test_values_semanticvisitor_runtimemodelelement_value_instantiation(instance):
    assert isinstance(instance, Values_SemanticVisitor_runtimeModelElement_Value)

@given(instance=Values_ActionActivation_firing_Value_strategy)
@settings(max_examples=50)
def test_values_actionactivation_firing_value_instantiation(instance):
    assert isinstance(instance, Values_ActionActivation_firing_Value)

@given(instance=umlTrace_State_strategy)
@settings(max_examples=50)
def test_umltrace_state_instantiation(instance):
    assert isinstance(instance, umlTrace_State)
